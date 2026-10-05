# Cybertronix website: rules for every Claude working on this repo

Cybertronix is a Hyderabad robotics engineering company. Real today: AI vision on existing CCTV, and a
cleaning robot in development. Humanoids and robotic arms are custom-build capabilities, not products
yet (D16). Never show the founding year (D19). This repo holds its website and the team's shared memory.

**New here? Read `docs/HANDOVER.md`, then `docs/START-HERE.md`.**

## Always, first
1. `git pull`, then read `docs/START-HERE.md`, `docs/BOARD.md`, `docs/DECISIONS.md` and `docs/PAGES.md`.
2. Never contradict `docs/DECISIONS.md`. If it seems wrong, ask the founder through the hub.
3. Before you end a turn, commit and push. Chats can't see each other's conversations; the repo is the memory.

## The team: one hub, three chats
The founder talks **only to the hub**. The hub hands out work (`send_message`), checks in and reports
milestones. Session IDs are in `docs/HUB.md`.

| Chat | Role | Writes to |
|---|---|---|
| **Hub** | Founder's single contact: ideas, decisions, status, orchestration | `docs/` (not `docs/seo/`) |
| **Design** | Keeps the Midnight Lab canvas 1:1 with the site | The canvas artifact, Design notes in `docs/PAGES.md`, `docs/design.md` |
| **Build** | Builds the site and owns technical SEO | `site/`, `.github/`, `docs/BOARD.md` status, `docs/PAGES.md` Build column, `docs/FOUNDER-TODO.md` steps |
| **SEO Content** | Keywords, page plan, every word on the site | `docs/seo/`, page text in `content/` |

No Media and no Marketing chats (founder decision). We use the footage we already have.

## Standing approval
- **Design phase (D14): the founder approves the complete design before any site code is merged.**
  Design does not self-approve. Build stays paused until the hub says the design is approved.
- After design approval: Build merges its own PR to `main` once the checks in `docs/START-HERE.md` pass.
- **Only the founder** does physical steps: domain, hosting account, Google Search Console, Google
  Business Profile, photos, payments. Put those in `docs/FOUNDER-TODO.md`.

## Hard rules
- **Design = site, 1:1.** `docs/PAGES.md` lists every page and section with an ID (`P1`, `P1.2`…).
  The canvas has one board per page, titled with its ID. Add a page → PAGES entry → Design board → Build.
- **Honest.** No fake clients, logos, numbers, awards, certifications or reviews. Specs only if real.
  If a fact is unknown, leave a visible `TODO(founder)` in the docs, never invent it.
- **SEO first.** Every page targets one keyword group from `docs/seo/keywords.md`. Real HTML text
  (never text inside images or video), one H1, title, meta description, alt text, schema.
- **Fast.** Green Core Web Vitals on mobile. Hero video is muted, compressed, has a poster, and does
  not autoplay on phones. The H1 is real text above it.
- **Calm motion.** The head-turn in the hero only. Everything else stays still or hover-only.
- **Accent colours** (blue, orange, teal) are for buttons and highlights, never long body text.
- **Secrets.** Never commit keys or passwords.

## Talking to the founder (hub only)
Visual and tabular, ADHD-friendly: short lines, one idea per row, the next action first.
Only interrupt for milestones, blockers that need the founder, or a chat that died.
