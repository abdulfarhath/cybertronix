// Post-build checks (run via `npm run check`, which builds first).
// Every page: <title>, meta description, canonical, exactly one <h1>, valid JSON-LD.
// Every internal link / asset reference resolves to a file in dist/. sitemap.xml and robots.txt exist.
import { readdir, readFile, stat } from 'node:fs/promises';
import { join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';
import { SITE_URL } from '../src/config/site-url.mjs';

const DIST = fileURLToPath(new URL('../dist/', import.meta.url));
const errors = [];
const fail = (file, msg) => errors.push(`${file}: ${msg}`);

async function walk(dir) {
  const out = [];
  for (const e of await readdir(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) out.push(...(await walk(p)));
    else out.push(p);
  }
  return out;
}

async function exists(p) {
  try { return (await stat(p)).isFile(); } catch { return false; }
}

/** Resolve a root-relative URL path the way Cloudflare Pages / Vercel cleanUrls would. */
async function resolves(urlPath) {
  const p = decodeURI(urlPath.split(/[?#]/)[0]);
  if (p === '' || p === '/') return exists(join(DIST, 'index.html'));
  const base = join(DIST, p);
  return (await exists(base)) || (await exists(base + '.html')) || (await exists(join(base, 'index.html')));
}

const attr = (tag, name) => tag.match(new RegExp(`\\s${name}\\s*=\\s*("([^"]*)"|'([^']*)'|([^\\s>]+))`, 'i'))?.slice(2).find((x) => x !== undefined);

const files = await walk(DIST);
const pages = files.filter((f) => f.endsWith('.html'));
if (pages.length === 0) fail('dist', 'no HTML pages built');

for (const required of ['sitemap-index.xml', 'robots.txt', '404.html']) {
  if (!(await exists(join(DIST, required)))) fail('dist', `missing ${required}`);
}

for (const file of pages) {
  const rel = relative(DIST, file);
  const html = await readFile(file, 'utf8');
  const tags = html.match(/<[a-z][^>]*>/gi) ?? [];

  const title = html.match(/<title>([^<]*)<\/title>/i)?.[1]?.trim();
  if (!title) fail(rel, 'missing <title>');
  else if (title.length > 60) fail(rel, `title is ${title.length} chars (max 60): "${title}"`);

  const metaDesc = tags.find((t) => /^<meta\s/i.test(t) && attr(t, 'name') === 'description');
  const desc = metaDesc && attr(metaDesc, 'content')?.trim();
  if (!desc) fail(rel, 'missing meta description');
  else if (desc.length > 160) fail(rel, `meta description is ${desc.length} chars (max 160)`);

  if (!tags.some((t) => /^<link\s/i.test(t) && attr(t, 'rel') === 'canonical')) fail(rel, 'missing canonical link');

  const h1s = (html.match(/<h1[\s>]/gi) ?? []).length;
  if (h1s !== 1) fail(rel, `expected exactly 1 <h1>, found ${h1s}`);

  if (!/<html[^>]*\slang=/i.test(html)) fail(rel, 'missing <html lang>');

  const ldBlocks = [...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/gi)];
  if (ldBlocks.length === 0) fail(rel, 'no JSON-LD schema');
  for (const [, json] of ldBlocks) {
    try {
      const data = JSON.parse(json);
      if (!data['@context'] || !data['@type']) fail(rel, 'JSON-LD block without @context/@type');
    } catch (e) {
      fail(rel, `invalid JSON-LD: ${e.message}`);
    }
  }

  for (const t of tags) {
    if (/^<img\s/i.test(t)) {
      if (attr(t, 'alt') === undefined && !/\salt[\s>]/i.test(t)) fail(rel, `img without alt: ${t.slice(0, 80)}`);
      if (!attr(t, 'width') || !attr(t, 'height')) fail(rel, `img without width/height: ${t.slice(0, 80)}`);
    }
  }

  // Internal links and assets
  const refs = new Set();
  for (const t of tags) {
    if (/^<link\s/i.test(t) && attr(t, 'rel') === 'canonical') continue;
    for (const name of ['href', 'src', 'poster', 'data-src']) {
      const v = attr(t, name);
      if (v) refs.add(v);
    }
    const srcset = attr(t, 'srcset');
    if (srcset) srcset.split(',').forEach((s) => refs.add(s.trim().split(/\s+/)[0]));
  }
  for (let ref of refs) {
    if (ref.startsWith(SITE_URL)) ref = ref.slice(SITE_URL.length) || '/';
    if (!ref.startsWith('/') || ref.startsWith('//')) continue; // external, mailto:, tel:, #hash
    if (!(await resolves(ref))) fail(rel, `broken internal link: ${ref}`);
  }
}

// Sitemap URLs must resolve too
const sitemaps = files.filter((f) => /sitemap-\d+\.xml$/.test(f));
for (const sm of sitemaps) {
  const xml = await readFile(sm, 'utf8');
  for (const [, loc] of xml.matchAll(/<loc>([^<]+)<\/loc>/g)) {
    const path = loc.startsWith(SITE_URL) ? loc.slice(SITE_URL.length) || '/' : loc;
    if (!(await resolves(path))) fail(relative(DIST, sm), `sitemap URL does not resolve: ${loc}`);
  }
}

if (errors.length) {
  console.error(`\n✗ check failed (${errors.length}):\n  ` + errors.join('\n  '));
  process.exit(1);
}
console.log(`✓ check passed: ${pages.length} pages, ${sitemaps.length} sitemap(s)`);
