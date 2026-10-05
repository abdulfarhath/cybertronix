# SEO Content (owned by the SEO Content chat)

Files:
- `keywords.md`: every keyword with intent, rough volume (from free tools or Google suggestions), target page
- `page-plan.md`: per page: title (≤60 chars), meta description (≤155), H1, H2s, FAQ questions, schema type
- `../../content/`: final page text, one markdown file per page ID

Honest volumes only: if a number isn't from a tool, write "est." or leave it blank.
- `tools/gen_plan.py`: regenerates `page-plan.md` from `content/` and checks title/meta lengths and internal links. Run from the repo root after any content change.
