# Page text (owned by SEO Content)

One file per page ID, matching `docs/PAGES.md` and `docs/seo/page-plan.md`.

## Format
- Front matter: `id`, `url`, `title`, `description` (meta), `eyebrow`, `h1`, `schema`, `keyword`.
- **Brand first (D41):** the H1 is written for people. The keyword goes in the eyebrow (a small `<p class="eyebrow">` above the H1, never a heading), the title, the meta, the URL, alt text, schema and the first paragraph.
- `## ` headings = the page's H2s, in order. Section IDs (`P1.2`) match PAGES.md.
- `**CTA:**` lines = button text → link.
- `> Build note:` lines are for Build only, never shown on the site.
- `TODO(founder)` = a real fact we don't have yet. **Build: do not ship a TODO live.** Hide that row,
  sentence or FAQ until the text here is updated.
- FAQ blocks: `### Question` then the answer. Use the same words in the `FAQPage` JSON-LD.

## Voice
Plain, calm and specific. Short sentences. No hype words ("revolutionary", "cutting-edge", "best in India").
No numbers, clients, awards or specs unless they are real and confirmed.
