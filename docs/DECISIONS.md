# Decisions

## Current rules
| # | Date | Decision |
|---|---|---|
| D1 | 2026-10-03 | Team = Hub + Design + Build + SEO Content. No Media, no Marketing. |
| D2 | 2026-10-03 | Design direction C · Blueprint hybrid, "Midnight Lab" palette. |
| D3 | 2026-10-03 | Market: Hyderabad first, then India. |
| D4 | 2026-10-03 | Products: humanoid robots, robotic arm, cleaning robot, AI vision / surveillance. |
| D5 | 2026-10-03 | Stack: Astro static site (real HTML, fast, good for SEO). Code in `site/`. |
| D6 | 2026-10-03 | Hosting: a free static host (Cloudflare Pages or Vercel). Founder picks and creates the account. |
| D7 | 2026-10-03 | SEO targets, in order: brand name → "robotics company in Hyderabad" → product + Hyderabad/India → broad terms later. |
| D8 | 2026-10-03 | One keyword group per page. Every product page has a spec table and an FAQ block. |
| D9 | 2026-10-03 | (see D20) Use the existing graded stock footage. Real product photos replace it when the founder has them. |
| D10 | 2026-10-03 | Motion: hero head-turn only. Hero video muted loop with poster; no autoplay on phones. |
| D11 | 2026-10-03 | Honesty: no fake clients, numbers, reviews, awards or specs. Unknown facts stay `TODO(founder)`. |
| D12 | 2026-10-03 | Free SEO tools only for now: Keyword Surfer, Ubersuggest free tier, Google Keyword Planner, Trends, Search Console. |
| D13 | 2026-10-03 | Hub decision: industry pages P8 `/industries/manufacturing` and P9 `/industries/hospitality` approved. Claims stay general and honest until real use cases come in. Prices read "price on request" until the founder answers. |
| D14 | 2026-10-03 | **Founder: design first, build later.** No site code is merged until the founder approves the complete design. Design does NOT self-approve; the founder approves through the hub. Overrides the standing approval in CLAUDE.md for this phase. |
| D15 | 2026-10-03 | Domain: **cybertronix.tech** (founder's existing site). The new site launches on it. |
| D16 | 2026-10-03 | (AI vision part superseded by D21) **What is real today:** AI vision works with existing CCTV. Cleaning robot is **in development, no clients yet**. Humanoid and robotic arm are **not built**: they are custom-build capabilities ("we design and build to your requirement"). The site must never say or imply that a humanoid or arm exists, has shipped, or has clients. |
| D17 | 2026-10-03 | Positioning: Cybertronix is a **Hyderabad robotics engineering company** with an in-house team in AI engineering, mechatronics, mechanics and electronics, which builds custom robots and AI vision systems to order. |
| D18 | 2026-10-03 | No prices anywhere. Product pages say "Quote on request". |
| D19 | 2026-10-03 | **Never show the founding year** or company age anywhere on the site, in schema (no foundingDate) or in copy. |
| D20 | 2026-10-03 | Stock footage of robot arms is mood/illustration only. It is never captioned or framed as a Cybertronix product. |
| D21 | 2026-10-03 | **AI vision is a prototype**, not yet deployed, with no clients. Status label: "Prototype · pilot partners welcome". Nothing is "Available now". Statuses: AI vision = Prototype, Cleaning robot = In development, Humanoid + Arm = Built to order. |
| D22 | 2026-10-03 | AI vision's real focus: **gowning / PPE compliance for surgeons and pharma (drug research) cleanrooms**: gloves, masks, shoe covers, gowns and dress code. Works with existing CCTV. Also open to other computer-vision uses (supermarkets, retail, factories) as custom projects. |
| D23 | 2026-10-03 | Hub decision (founder delegated): AI vision is **designed to run on-site** on a small edge computer next to the existing CCTV (video stays on the premises), with an optional cloud dashboard. Alerts: on-screen dashboard + email, WhatsApp later. Always worded "designed to", never "deployed". |
| D24 | 2026-10-03 | Cleaning robot: autonomous **floor cleaning for offices and malls**. In development, no timing shown. |
| D25 | 2026-10-03 | Contact facts confirmed: Rd 10C, Gayatri Hills, Jubilee Hills, Hyderabad · +91 90598 97807 · info@cybertronix.com. |
| D26 | 2026-10-03 | Company: aiming to be **product-based**, open to client projects. Standalone: not at any incubator, so never mention T-Hub or any incubator. No clients yet anywhere on the site. |
| D27 | 2026-10-03 | New page **P10 Team** (`/team`): founder adds names and photos later. Design uses grey placeholder cards labelled "Photo coming soon" (never fake faces or names). Build hides cards with no name. |
| D28 | 2026-10-03 | Hub decision: **P9 becomes Pharma & healthcare** (`/industries/pharma-healthcare`), the strongest real AI vision use. Hospitality is dropped. **P11 Retail & malls** (`/industries/retail`) added: supermarket vision + floor-cleaning robot, both as invitations. |
| D29 | 2026-10-03 | Hub decisions: surgeons / operating-theatre entry is a confirmed P9 target (founder named surgeons). AI vision is "designed to work with standard IP CCTV cameras (RTSP)"; the optional cloud dashboard shows alerts and compliance summaries, not raw video. Pilot terms read "agreed per site, so talk to us". Cleaning modes stay hidden until the founder answers. |
| D30 | 2026-10-03 | **Raqib stays.** It's Cybertronix's own software: a terminal app (plus a local web view at `localhost:7070`) that watches AI workloads on a machine: RAM, CPU load, VRAM, thermals, AI processes, top processes, activity, and kill with confirm. Reference screenshot: `docs/reference/raqib-tui-current.png`. Status label: "Early build". |
| D31 | 2026-10-03 | New section **Software & projects**: P12 `/software` (all tools; placeholder cards "Details coming soon" for tools the founder will share later) and P13 `/software/raqib`. Never invent features: only what's in the screenshot. |
| D32 | 2026-10-03 | Design also owns, as separate boards on the canvas: **[R1] Raqib logo**, **[R2] Raqib terminal app redesign** (same panels as the screenshot), **[R3] Raqib web dashboard** (localhost:7070 view), each light + dark. They're shown to the founder for approval with the site. |
| D33 | 2026-10-03 | **Founder: take inspiration from Hostelzy's design and brand system.** Borrowed rules: (1) the logo tells the product's story, drawn from the product's own UI (Hostelzy = the bed picker); (2) one accent colour with one meaning; (3) two levels of logo detail (a simple mark at ≤64 px), plus a mono version and a favicon; (4) one token file is the single source for colours; (5) square corners, 2 px rules, light + dark, works on 360 px phones; (6) a one-page brand guide (logo, colours, type, tone, do/don't); (7) the founder picks from 2–3 logo options. |
| D34 | 2026-10-03 | Raqib's current app bugs are out of scope (it's built by a company engineer, not the founder). The R2/R3 boards are **the design of the Raqib we'll build next**: improvements are welcome, labelled "Proposed". The website (P13) still describes only what the real app does today. |
| D35 | 2026-10-03 | **Founder picked Cybertronix mark X "Detection C"** as the base. Design makes a **separate logo canvas** ("Cybertronix · Logo") with more versions of X. Story (hub decision): **"a machine that sees"**. The detection-box corners that form the C are also a robot's head/visor, and the eyes inside are camera lenses. Like Hostelzy's "only your bed is red", **only one thing gets the accent: the seeing eye**. Founder picks the final version. |
| D36 | 2026-10-04 | Founder delegated the pick: **Cybertronix logo = L4 "Head-turn"**. The C is a robot head and its eyes look out through the opening; only the leading eye is accent blue. It links to the hero head-turn animation. Can be swapped later if the founder prefers another L-version. |
| D37 | 2026-10-04 | Founder delegated the pick: **Raqib logo = R1 option A "Panel + pulse"**. A terminal panel with a pulse line; only the watched workload block is accent blue (the same rule as Hostelzy's red bed and the Cybertronix eye). |
