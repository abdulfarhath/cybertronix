# Handover to a new Claude account (2026-10-05, updated 2026-10-06)

> **Hub: read `docs/memory/README.md` first.** The founder only says "continue".

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
| Canvases (Claude artifacts) | Owned by the old account: Site `https://claude.ai/artifact/CuWwyexFMkXoxr7sUyxS2j`, Logo `https://claude.ai/artifact/2KpSqWpNxZYqE5d9TeuGdj`. The new account can't edit them. **The source is in the repo**: footage and stills in `design/footage/` (see its README for re-uploading), `design/boards/*.py` + `design/tokens.json` regenerate every board. New Design republishes a fresh canvas from it and records the new URL in `docs/START-HERE.md` |
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
1. New hub: read `docs/memory/README.md`, `docs/memory/founder-messages.md`, `CLAUDE.md`, this file, `docs/DECISIONS.md`, `docs/BOARD.md`.
2. **D45: save tokens.** Don't create chats or rebuild canvases up front. Send the existing `design/previews/` PNGs and ask for approval (memory §7).
3. After "approved": create one Build chat → resume `feature/T6-skeleton` → T7 pages → launch steps in `docs/FOUNDER-TODO.md`.
4. Canvases are rebuilt from `design/boards/` only if the founder asks to see one.

## 5b. Notes for the new Build chat (from the old Build chat)
- `feature/T6-skeleton` (c02d80f) is based on the 2026-10-03 main: merge main first; expect conflicts in `docs/BOARD.md` and `docs/PAGES.md`.
- `site/src/config/site-url.mjs` has the placeholder `cybertronix.in`. Change it to **cybertronix.tech** (D15).
- Stubs cover P1–P7 with provisional titles. Switch to the title/meta/H1/eyebrow from `content/` front matter and add P8–P13.
- Tokens are placeholders. Use `design/tokens.json`. Logo files: `design/logo/`.

## 6. How the founder likes to work
- Talks only to the hub. Short, visual, table-first, ADHD-friendly; next action first.
- Often on mobile: send screenshots as images, not artifact links.
- Delegates taste ("take your own decisions") but wants honest, impressive, brand-first work.

## 7. Gotchas we already hit (don't repeat them)
| Gotcha | Fix |
|---|---|
| Artifacts belong to one account | Rebuild from `design/boards/` + `design/footage/`, republish, update links in `START-HERE.md` and here |
| Founder can't open artifacts on the phone | Send PNG screenshots in chat (`design/previews/`, or render with Playwright + `/opt/pw-browsers`) |
| Claude's GitHub app can't create repositories | Founder creates the repo; the hub uses `add_repo` |
| A child chat's Artifact publish may need approval in that chat | Design pushes the board files to the repo; the hub publishes if Design is blocked |
| Publishing to an existing artifact needs a fresh `Artifact read` in that session | Read first, then publish |
| All chats share one usage limit | Run only the chats needed; let idle ones sleep |
| Build ran ahead of design approval | D14: Build stays paused until the founder says "approved" |

## 8. First message to paste into the new hub (optional)
`CLAUDE.md` already sends a new chat to `docs/memory/`, so the founder can just say **"continue"**. If a chat doesn't pick it up, paste:
```
You are the Cybertronix hub (founder's single chat). Read docs/memory/README.md and docs/memory/founder-messages.md,
then docs/HANDOVER.md, CLAUDE.md, docs/DECISIONS.md, docs/BOARD.md and docs/PAGES.md.
Then do docs/memory/README.md §7: send me the key screenshots as images so I can approve the design.
Don't create chats or rebuild anything until I ask (D45).
Always answer me in short visual tables.
```
