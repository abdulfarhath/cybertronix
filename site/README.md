# Cybertronix site (Astro)

| Command | What |
|---|---|
| `npm ci` | Install |
| `npm run dev` | Local dev server |
| `npm run build` | Static build into `dist/` |
| `npm run check` | Build, then check every page: title, meta description, canonical, one H1, valid JSON-LD, img alt + size, no broken internal links, sitemap URLs resolve |
| `npm run lighthouse` | Lighthouse mobile on every built page; fails under 90 for Performance, SEO, Accessibility (needs Chrome; set `CHROME_PATH` if not found) |

CI: `.github/workflows/site-check.yml` runs `check` and `lighthouse` on every PR and push to `main`.

## Where things are
| What | Where |
|---|---|
| Company facts (address, phone: `TODO(founder)`) | `src/config/site.ts` |
| Domain | `src/config/site-url.mjs` (or `SITE_URL` env var) |
| Design tokens (placeholder until `docs/design.md`) | `src/styles/tokens.css` |
| SEO head (title, description, canonical, OG, Twitter) | `src/components/SeoHead.astro` |
| JSON-LD helpers: Organization, LocalBusiness, Product, FAQPage, BreadcrumbList, WebPage | `src/lib/schema.ts` |
| Images: AVIF/WebP, width/height, lazy by default (`priority` for the hero) | `src/components/Img.astro` |
| Hero video: muted loop, poster first, `preload="none"`, no autoplay < 768px or reduced motion | `src/components/HeroVideo.astro` |
| Pages P1–P7, 404, robots.txt | `src/pages/` |

## Rules
- One `<h1>` per page, real text. Title ≤ 60 chars, description ≤ 160 (the check enforces both).
- Every `<Img>` needs `alt`. Only the hero image gets `priority`.
- Schema helpers drop empty fields; never fill an unknown fact with a placeholder value.
- Hero footage goes in `public/video/` (H.264 MP4, muted, ≤ ~3 MB) and its poster in `src/assets/`.

## Hosting
Static output. Cloudflare Pages: root `site`, build `npm run build`, output `dist`, env `NODE_VERSION=22`.
Vercel: root directory `site`, framework Astro (`vercel.json` sets clean URLs). Steps for the founder: `docs/FOUNDER-TODO.md`.
