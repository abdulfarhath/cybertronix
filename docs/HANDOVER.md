# Handover to a new Claude account (2026-10-05)

The founder is moving this project to a new Claude account. Everything that matters is in this repo.
Chats can't be moved between accounts, so the new account starts a fresh hub and fresh chats.

## 1. Where things stand (one glance)

| Area | State |
|---|---|
| Team model | Hub + Design + Build + SEO Content (no Media, no Marketing). See `CLAUDE.md` |
| Text | ✅ All 13 pages written, brand-first (D41–D44), in `content/`. Keyword plan in `docs/seo/` |
| Design | ✅ Everything drawn, **waiting for the founder's "approved" (T10)**. Phone previews: `design/previews/` (75 PNGs, list in its README) |
| Logos | ✅ Cybertronix = **L6 Sensor mast** (D38). Raqib = **A Panel + pulse** (D39). Files: `design/logo/`, `design/raqib-logo/` |
| Raqib app redesign | ✅ Approved direction (D39), screens R2–R11 in previews |
| Build | ⏸ **Paused (D14).** Astro skeleton is on branch `feature/T6-skeleton` (unmerged; checks passed). Resume only after the founder approves the design |
| Domain | cybertronix.tech (D15) |

## 2. Key decisions to know first (full list: `docs/DECISIONS.md`)
- **Brand first, SEO underneath (D41).** Headlines are for people; keywords go in title/meta/URL/alt/schema/eyebrow.
- **Home headline (D42):** "We build the robots the world needs next." Global market, Hyderabad base.
- **Honesty (D11, D16, D21, D26):** AI vision = Prototype · Cleaning robot = In development · Humanoid + arm = Built to order · Raqib = Early build. No clients, no prices, **never the founding year (D19)**, no incubator.
- **Design before build (D14):** nothing is merged to the site until the founder approves.
- Logo story: "a machine that sees". Only the seeing eye is accent blue (D33, D35).

## 3. Things that do NOT carry over
| Item | What to do |
|---|---|
| Old chat sessions (`docs/HUB.md`) | Belong to the old account. The new hub creates new Design / Build / SEO Content sessions on this repo and updates `docs/HUB.md` |
| Canvases (Claude artifacts) | Owned by the old account: Site `https://claude.ai/artifact/CuWwyexFMkXoxr7sUyxS2j`, Logo `https://claude.ai/artifact/2KpSqWpNxZYqE5d9TeuGdj`. The new account can't edit them. **The source is in the repo**: `design/boards/*.py` + `design/tokens.json` regenerate every board. New Design republishes a fresh canvas from it and records the new URL in `docs/START-HERE.md` |
| GitHub access | The new Claude account must connect the GitHub account that owns `abdulfarhath/cybertronix` (or be given access) |

## 4. Open questions for the founder (all hidden on the site until answered)
| # | Question |
|---|---|
| Q1 | Approve the design (T10), or list changes |
| Q2 | Cleaning robot: which modes (sweep / vacuum / mop / scrub)? Rough timing? |
| Q3 | Address: PIN 500033? Show plot no. 8-2-293/82/B/102? |
| Q4 | Typical build time for a custom humanoid or arm? Languages a humanoid could speak? |
| Q5 | LinkedIn / Instagram links, office hours |
| Q6 | Confirm no link to "Cybertronix Technologies LLC, Dubai" |
| Q7 | Raqib: download/GitHub link? Licence (free/open source/paid)? OS and GPUs? Detects Ollama? |
| Q8 | Team page: names and photos (placeholders until then) |
| Q9 | Screenshots + one line for each of the other internal tools (P12 placeholder cards) |
| Q10 | Founder's choice on the optional logo blink tie-in (Proposed) |

## 5. Next steps, in order
1. New hub: read `CLAUDE.md`, this file, `docs/DECISIONS.md`, `docs/BOARD.md`.
2. Create the Design, Build and SEO Content chats on this repo (brief each from `CLAUDE.md` roles); record IDs in `docs/HUB.md`.
3. Design: republish the canvases from `design/boards/` and send the founder phone previews (the founder works from a phone and can't open artifacts, so always send PNGs in chat).
4. Get the founder's design approval (T10). Then Build resumes `feature/T6-skeleton` → T7 pages → launch steps in `docs/FOUNDER-TODO.md`.

## 5b. Notes for the new Build chat (from the old Build chat)
- `feature/T6-skeleton` (c02d80f) is based on the 2026-10-03 main: merge main first; expect conflicts in `docs/BOARD.md` and `docs/PAGES.md`.
- `site/src/config/site-url.mjs` has the placeholder `cybertronix.in`. Change it to **cybertronix.tech** (D15).
- Stubs cover P1–P7 with provisional titles. Switch to the title/meta/H1/eyebrow from `content/` front matter and add P8–P13.
- Tokens are placeholders. Use `design/tokens.json`. Logo files: `design/logo/`.

## 6. How the founder likes to work
- Talks only to the hub. Short, visual, table-first, ADHD-friendly; next action first.
- Often on mobile: send screenshots as images, not artifact links.
- Delegates taste ("take your own decisions") but wants honest, impressive, brand-first work.
