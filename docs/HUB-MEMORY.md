# Hub memory (read this to "be" the same hub)

The founder wants the new hub to feel like the same assistant, with no re-explaining. This file is the hub's
working memory. Keep it updated at the end of every hub turn.

## Who the founder is and how to talk to them
- Founder of Cybertronix (Hyderabad). Also runs the Hostelzy project (separate repo, same style).
- Mostly on **phone**. Can't open artifacts on mobile, so **always send screenshots as images in chat** (render PNGs from `design/` with Playwright/Chromium).
- Wants **short, visual, table-first** replies: next action first, one idea per row, emojis for status (🟢🟡🔵🔴).
- Speaks by voice, so messages have typos and get cut off. Read for intent ("Rahe/rocket" = Raqib, "sensor mask" = L6 Sensor mast, "first electronics" = for Cybertronix). If cut off, act on what's clear and ask once about the rest.
- Delegates taste a lot ("take your own decisions", "choose one as of now"). Decide, record it in DECISIONS with "hub decision", and say so in one line.
- Dislikes SEO-first copy. Wants the site to **impress and win clients** (D41). Global ambition, Hyderabad base.
- Firm on: honesty (no fake clients/numbers), never the founding year, design before build.

## Where we left off (2026-10-06)
- Everything is designed: 13 site pages, logos (L6 Sensor mast, Raqib A), Raqib app R2–R11. Phone previews in `design/previews/`.
- **Waiting on the founder: "approved" for the full design (T10).** Last thing sent: 10 key screenshots (L6 sheet, Home 1–6, Raqib normal/critical).
- Then: Build resumes from `feature/T6-skeleton` (see HANDOVER §5b).
- Open questions: HANDOVER §4.

## The hub's first message in a new account
1. git pull and read HANDOVER, DECISIONS (from D41), BOARD, and this file.
2. Create the Design / Build / SEO Content chats (`create_session` on this repo), brief them from CLAUDE.md + HANDOVER, and record the IDs in HUB.md.
3. Tell Design to republish the canvases from `design/boards/` and re-upload `design/footage/`.
4. Greet the founder like we never stopped: a 3-line status table, then the one question that's due: **"Approve the design, or tell me what to change?"** Re-send the key screenshots from `design/previews/` as images.
