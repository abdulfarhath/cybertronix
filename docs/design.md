# Design system: Midnight Lab (direction C · Blueprint hybrid)

**Canvas:** https://claude.ai/artifact/CuWwyexFMkXoxr7sUyxS2j (owned by this account, Design chat edits it).
Carried over 1:1 on 2026-10-03 from the founder's original
(https://claude.ai/artifact/VEDcNs3Rp61FzB9hmtfSf7, other account, read-only for us).
Footage and stills were re-uploaded to the new canvas; Build can pull them from its assets.

Rule of thumb: **dark cinematic hero, then calm technical sections with faint blueprint grid lines.**

**D33 (Hostelzy-inspired) applies to everything below:**
| Rule | How it shows up |
|---|---|
| One token file | `design/tokens.json` is the only source for colours, type and shape. Build reads it. Boards are generated from the same values. |
| One accent, one meaning | **Blue = you can act** (buttons, links, focus, the selected item). Orange is not an accent: alerts and `TODO(founder)` chips only. Teal is retired. Status labels are neutral text. |
| Square, 2 px | Radius 0 on every container, button and input. Rules and borders 2 px. Round shapes only for status dots and the play button. |
| Light + dark, 360 px | Every page board has desktop 1440 and phone 390; layouts stack down to 360. |
| One-page brand guide | Canvas board `[B1] Brand guide and tokens`: logo, colours, type, shape, tone, do/don't. |
| Logo canvas (D35) | https://claude.ai/artifact/2KpSqWpNxZYqE5d9TeuGdj: L1–L10 versions of mark X, story "a machine that sees", only the seeing eye is blue. Generator: `design/boards/logo.py`. |
| Logo options | Raqib: 3 options on `[R1]` (A Panel + pulse, B Brackets + dot, C Grid R + gauge). Cybertronix: current hex C stays; 2 refresh options on `[B1]` (X Detection C, Y Hex corners). Founder picks. |
Values marked *(canvas)* are copied from the canvas. Values marked *(new)* are defined here by Design
and are on the canvas style guide and page boards.

---

## 1. Colour tokens

### Dark sections (hero, product demos, footer) *(canvas)*
| Token | Hex | Use |
|---|---|---|
| `--bg` | `#0A0C10` | Page background |
| `--surface` | `#141A22` | Cards, panels, nav pill |
| `--surface-sunk` | `#10141B` | Placeholders, video wells |
| `--terminal` | `#0D1016` | Terminal / code panels |
| `--divider` | `#1A212B` | Section rules |
| `--border` | `#232B36` | Card and table borders |
| `--border-strong` | `#2E3846` | Inputs, secondary buttons, tags |
| `--border-hover` | `#3A4452` | Hover border |
| `--text` | `#E8ECF2` | Headings, body |
| `--text-2` | `#B7C0CD` | Paragraphs, lead |
| `--text-muted` | `#8A94A4` | Labels, captions (6.4:1 on bg) |
| `--accent` | `#3D7BFF` | **Only** things you can act on: links, focus, selected item (D33) |
| `--button` | `#2F66E0` | Primary button fill (white text) |
| `--link` | `#8FB2FF` | Links; hover `#C4D6FF`; focus ring |
| `--alert` | `#FF8A3D` | Warnings, "restricted" boxes; text on it `#0A0C10` |
| `--alert-soft` | `#FFC49E` | Text inside alert panels |


### Light sections (spec tables, FAQ, About, long reading) *(new)*
| Token | Hex | Use |
|---|---|---|
| `--l-bg` | `#F3F5F8` | Section background |
| `--l-surface` | `#FFFFFF` | Cards, table body |
| `--l-border` | `#D8DEE7` | Borders, table rules |
| `--l-text` | `#0F141B` | Headings, body |
| `--l-text-2` | `#3A4453` | Paragraphs |
| `--l-text-muted` | `#5A6475` | Labels (5.3:1 on `--l-bg`) |
| `--l-accent` | `#2457C8` | Links, highlights (6.0:1) |
| `--l-alert` | `#B9530F` | Warnings on light |

Blue is for things you can act on; orange for alerts and TODO chips (D33). **Never long body text.**
A page alternates at most dark → light → dark; the hero and footer are always dark.

## 2. Type *(canvas)*
Google Fonts, `display=swap`: **Unbounded** (display), **Geist** (text), **JetBrains Mono** (labels).

| Style | Font | Size / line | Desktop → phone |
|---|---|---|---|
| H1 / display | Unbounded 500, -0.01em | 60/65 | → 34/38 |
| H2 section | Unbounded 500 | 44/51 | → 28/32 |
| H3 card | Unbounded 500 | 20/28 | → 16/22 |
| Stat value | Unbounded 400 | 22 | → 18 |
| Lead | Geist 400 | 19/30 | → 16/26 |
| Body | Geist 400 | 15/23 (17/27 in section intros) | → 15/23 |
| Mono label / tag | JetBrains Mono 400 | 13/20 (12 small) | → 12/11 |
| Spec value | JetBrains Mono 400 | 15 | same |

One H1 per page, always real text, never inside video or images.

## 3. Grid lines (the "blueprint" layer) *(new)*
- Dark sections: 1px lines, `rgba(143,178,255,0.06)`, 40px square grid. Hero: grid only on the text
  side, fading out with a mask toward the video.
- Light sections: 1px minor lines `rgba(36,87,200,0.06)` every 24px; major lines
  `rgba(36,87,200,0.12)` every 120px.
- CSS background only (`linear-gradient` pairs). No images, no motion. Hidden in print.
- Section edges: 1px `--divider` rule (dark) or `--l-border` (light).

## 4. Layout and spacing *(canvas)*
- 8px base. Container max 1280, 12 columns, 20px gap. Gutter 80 desktop, 20 phone.
- Section padding: 120 top desktop, 56 phone.
- Radius: **0 everywhere** (D33). Borders and rules 2 px.
- Breakpoints: 390, 768, 1024, 1280, 1440.
- Touch targets ≥ 44px. Focus: 2px outline `--link`, offset 2px.

## 5. Components
| Component | Spec |
|---|---|
| **Nav** | 104 tall (72 phone). Logo hex mark + "Cybertronix" Unbounded 18. Centre links in a pill (`--surface`, 1px `--border`, active item `--border` fill). Right: primary "Book a demo" (44 tall). Phone: logo, small CTA, 44px menu button. |
| **Hero** | 920 tall, 2 columns. Left: mono eyebrow with accent dot, H1, lead (max 520), primary + secondary buttons. Right: 700 tall video panel, radius 28, bottom gradient `rgba(10,12,16,.92)→.35@40%→.1`, mono status chips, play/pause control bar. Phone: text first, then poster image 380 tall (no video). |
| **Product card** | `--surface`, 1px `--border`, radius 20. Media 300 tall on top, then 24 padding: mono status tag, H3, one-line body, text link. 4-up desktop, horizontal list (88px thumb) on phone. |
| **Spec table** | Two columns: label (`--text-muted`) left, value (mono) right, 18px row padding, 1px `--border` rows. Unknown values stay as `[__ unit]` placeholders = `TODO(founder)`. On light sections use `--l-*`. Real `<table>` with `<th scope="row">`. |
| **Callout parts** | On product video: accent dot 10px + label chip (`--surface`, 1px `--border-strong`, radius 10). |
| **Detection box** | 2px border, square, mono label tab on top-left (fill = border colour, text `#0A0C10`). Neutral `#E8ECF2` = normal, orange = alert. |
| **FAQ** *(new)* | Light section. H2, then `<details>`/`<summary>` list: 1px `--l-border` between items, summary Geist 500 17, plus/minus icon right, answer `--l-text-2` 15/23, max 720 wide. No animation beyond native open. FAQPage schema. |
| **CTA band** | Dark. H2 + one line + primary/secondary buttons, or the contact grid (details list left, form card right, radius 24). |
| **Form** | Labels above inputs, input 48 tall, `--bg` fill, 1px `--border-strong`, radius 10. Submit 52 tall, full pill. |
| **Footer** | 120 tall, 1px `--divider` top, © line left, links right, `--text-muted` 14. Phone: stacked. |
| **Buttons** | Primary: `--button`, white, 52/48/44 tall, 26px side padding. Hover fill `--accent`. Secondary: 1px `--border-strong`, `--text`; hover border `--border-hover`. |
| **Tag** | Mono 12, 1px `--border-strong`, pill. |

## 6. Footage grade *(canvas)*
Same grade on all stock and future real footage, so they sit together:
- Brightness −10, contrast +18, saturation 55%, slight blue lift in shadows.
- ffmpeg approximation: `eq=brightness=-0.04:contrast=1.18:saturation=0.55,colorbalance=bs=0.06:ms=0.02`
- Overlay gradients in CSS (not baked in), so text contrast can be tuned.
- Video: 1080p, 30 fps, H.264 MP4 + WebM, muted, loop, **under 2 MB**, always a `poster` (JPG/WebP).
- Current assets (stand-ins, free licence): 3 Pexels lab-arm clips (hero, arm, vision demo),
  arm stills (front/side/top/gripper), 1 Unsplash factory still by Shavr IK. Credit in page footer or credits page.
- Real product photos/footage replace them when the founder has them (D9).

## 7. Motion (D10)
- **Only** motion: the hero robot head-turn. 90–120 WebP frames (1280×1400), looking down → sideways → up,
  scrubbed by scroll. Until the 3D frames exist, the hero shows the muted looping clip.
- Hero video: muted, loop, `playsinline`, poster, play/pause button. **No autoplay under 768px** and none
  with `prefers-reduced-motion`: show the poster.
- Product and demo videos: poster until the user presses play.
- Everything else: still. Hover = colour/border change only, 150ms. No parallax, no fade-ins on scroll.

## 8. Carry-over gaps (all fixed on the T5 boards, 2026-10-03)
The original home boards are kept on the canvas page "Original canvas" for reference only. Build from the "Site P1–P9" page.

| Item on the old canvas | Fix |
|---|---|
| "Working with teams at" strip of logo placeholders | Remove. No logos until real, permitted ones exist (D11). |
| Hero stats `[00]` pilot sites / robots / cameras | Remove unless founder supplies real numbers → `TODO(founder)`. |
| Raqib (developer tool) card + section | Raqib stays (D30): P12 `/software`, P13 `/software/raqib`, plus R1–R3 boards. Status "Early build". |
| Humanoid shown only as "future" | P2 `/humanoid-robots` board, "Built to order" (D16). |
| Nav links are anchors | Page links per page plan: AI vision · Cleaning robot · Custom robots ▾ · Industries ▾ · About · Team · Contact; button "Tell us your requirement". |
| Vision/arm demos autoplay | Poster + play button (D10). |
| "Robotic arm, part by part": stock arm video with joint callouts, "Arm, front view" stills, spec table | Breaks D16/D20 (arm is not built; stock is mood only). Rework P3 as a capability page: "we design and build to your requirement", stock shown uncaptioned as mood, spec table = what a client specifies / what we can build to, not product specs. |
| Hero chips "Live from the lab", "Unit 01 online" on stock footage | Remove (D20). Stock stays uncaptioned mood footage. |
| Cleaning robot wording | "In development · pilot partners welcome" is allowed: an invitation, not a claim. Never an existing pilot, client, deployment, number or spec (hub ruling). |
| Product status labels | D21: AI vision = "Prototype · pilot partners welcome", Cleaning robot = "In development", Humanoid + Arm = "Built to order". Shown as a mono pill under the hero eyebrow and on cards. |
| Vision demo stock clip with boxes | Kept as an illustration of the gowning check (gloves / mask / shoe covers), captioned "Illustration on stock footage". Real gowning-room footage `TODO(founder)`. |
| Roadmap "Next · [year]" | No years (D19). |
| Email and address | Confirmed (D25): Rd No. 10C, Gayatri Hills, Jubilee Hills · +91 90598 97807 · info@cybertronix.com. In the footer on every board. |
| Prices | None anywhere; "Quote on request" (D18). |
| Spec values `[__]`, statuses `[Status]`, socials, privacy line | Stay as visible placeholders = `TODO(founder)`. |

Approval: Design does not self-approve in this phase (D14). The founder approves the full design via the hub (T10).

## 9. Canvas map
| Canvas page | Boards |
|---|---|
| Site P1–P13 | Style guide; `[P1]`…`[P13]` each desktop 1440 + phone 390. Section IDs (`P2.4`…) shown as mono labels, matching `content/`. |
| Raqib R1–R3 | `[R1]` 3 logo options drawn from Raqib's own screen: A Panel + pulse, B Brackets + dot, C Grid R + gauge. Each has a full mark, a simple mark (≤ 64 px), mono, app icon and "raqib by Cybertronix" lock-ups on light and dark. `[R2]` current app 1:1 replica (reference, title bar removed for privacy) + proposed terminal app dark/light. `[R3]` proposed web view dark/light with the same panels. Proposed ideas: status header ok/degraded/critical, threshold bars with numbers, workload rows (process, PID, VRAM, RAM, CPU, uptime, trend), sparklines, thermal colour, empty-state hint, kill always behind confirm. 16-colour ANSI safe. Sample data only. |
| Original canvas | Founder's original home boards, archived. Not for building. They still show the old PIN; ignore it (D29). |

All words on the boards come from `content/` (SEO Content). Design does not write copy.
New components on the boards: status pill (hero + section), people card ("Photo coming soon", D27),
2-column info table (dark or light), numbered step tiles, link tiles for industries.

**Regenerating the boards:** `design/boards/gen.py` builds every page board from one component set
(`pages.py` = page data from `content/`, `raqib.py` = R1–R3). Run `python3 gen.py` in a folder holding the canvas's
`project/` files, then `node measure.cjs > m.json && python3 fit.py` to fit frame heights, and publish to the canvas.
P4 has no spec table until the cleaning modes are confirmed (hub ruling 2026-10-03, D8 vs D29).

## 10. Chosen logos (D36, D37)
| Brand | Mark | Files | Rules board |
|---|---|---|---|
| Cybertronix | L4 Head-turn: the C is a robot head, eyes looking out of the opening; only the leading eye is blue | `design/logo/` | Logo canvas `[L4] Final` |
| Raqib | A Panel + pulse: terminal box, pulse line, only the watched workload is blue | `design/raqib-logo/` | Main canvas `[R1] Final` |

- Each folder: SVG marks (full, simple, 16 px pixel) in dark, light, mono black, mono white, on-accent; horizontal and stacked lock-ups; PNG icons 16 32 48 180 192 512; `favicon.ico`; `*-og-1200x630.png`.
- Clear space: x = one sixth of the mark width on every side. Minimum: 16 px (pixel mark). 48–64 px simple mark; 96 px and up full mark. Lock-up at least 120 px wide.
- Lock-up SVGs use the brand font as text (Unbounded 600 / JetBrains Mono 700); outline before print.
- Regenerate: `python3 design/boards/export.py` (needs Playwright Chromium and ImageMagick).
- Proposed (not approved): the nav eyes shift once when the P1 hero head turns; no loop; off with prefers-reduced-motion.
- Previews for the founder's phone: `design/previews/` (made by `design/boards/preview.cjs`).
