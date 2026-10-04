// Render canvas boards (.dc.html) to phone-friendly PNG previews (1040 px wide = 520 css px at 2x).
// Usage: node preview.cjs <out-dir> <board.dc.html>[:<css-width>] ...
// Footage on the canvas is served as /_blob/<id>; set BLOB_DIR to a folder of local copies named <id>.<ext>
// (or BLOB_MAP to a JSON {id: path}) so heroes render; otherwise they show empty.
const fs = require('fs'), path = require('path');
let pw;
try { pw = require('playwright'); } catch (e) { pw = require('/opt/node-tools/node_modules/playwright'); }
const outDir = process.argv[2];
const map = process.env.BLOB_MAP ? JSON.parse(fs.readFileSync(process.env.BLOB_MAP, 'utf8')) : {};
(async () => {
  const proxy = process.env.HTTPS_PROXY || process.env.https_proxy;
  const browser = await pw.chromium.launch(proxy ? { proxy: { server: proxy } } : {});
  for (const arg of process.argv.slice(3)) {
    const [file, wArg] = arg.split(':');
    const w = parseInt(wArg || (file.includes('phone') ? '390' : '1440'), 10);
    const ctx = await browser.newContext({ viewport: { width: w, height: 900 }, deviceScaleFactor: 1040 / w, ignoreHTTPSErrors: true });
    const page = await ctx.newPage();
    await page.route('**/_blob/**', route => {
      const id = route.request().url().split('/_blob/')[1].split(/[?#]/)[0];
      const p = map[id];
      if (p && fs.existsSync(p)) return route.fulfill({ path: p });
      return route.fulfill({ status: 404, body: '' });
    });
    await page.goto('file://' + path.resolve(file), { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
    await page.evaluate(() => document.fonts.ready);
    const h = await page.evaluate(() => document.querySelector('x-dc > div').scrollHeight);
    await page.setViewportSize({ width: w, height: h });
    const out = path.join(outDir, path.basename(file).replace('.dc.html', '.png'));
    await page.screenshot({ path: out, fullPage: true });
    console.log('preview', out, w, h);
    await ctx.close();
  }
  await browser.close();
})();
