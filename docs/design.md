# Design system: Midnight Lab (direction C · Blueprint hybrid)

**Canvas:** https://claude.ai/artifact/CuWwyexFMkXoxr7sUyxS2j (owned by this account, Design chat edits it).
Carried over 1:1 on 2026-10-03 from the founder's original
(https://claude.ai/artifact/VEDcNs3Rp61FzB9hmtfSf7, other account, read-only for us).
Footage and stills were re-uploaded to the new canvas; Build can pull them from its assets.

Rule of thumb: **dark cinematic hero, then calm technical sections with faint blueprint grid lines.**
Values marked *(canvas)* are copied from the canvas. Values marked *(new)* are defined here by Design
and will appear on the canvas with the T5 page boards.

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
| `--accent` | `#3D7BFF` | Highlights, dots, detection boxes, progress |
| `--button` | `#2F66E0` | Primary button fill (white text) |
| `--link` | `#8FB2FF` | Links; hover `#C4D6FF`; focus ring |
| `--alert` | `#FF8A3D` | Warnings, "restricted" boxes; text on it `#0A0C10` |
| `--alert-soft` | `#FFC49E` | Text inside alert panels |
| `--teal` *(new)* | `#2BB5A6` | "OK / clear / online" states only |

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
| `--l-teal` | `#0E7C70` | OK states on light |

Accents (blue, orange, teal) are for buttons, dots, boxes and short labels. **Never long body text.**
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
- Radius: buttons/tags 999, cards 20, panels 24, hero video 28, inputs 10, small tiles 14.
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
| **Detection box** | 2px border, radius 4, mono label tab on top-left (fill = border colour, text `#0A0C10`). Blue = normal, orange = alert, teal = clear. |
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

## 8. Carry-over gaps to fix in T5 (canvas ≠ rules yet)
| Item on the old canvas | Fix |
|---|---|
| "Working with teams at" strip of logo placeholders | Remove. No logos until real, permitted ones exist (D11). |
| Hero stats `[00]` pilot sites / robots / cameras | Remove unless founder supplies real numbers → `TODO(founder)`. |
| Raqib (developer tool) card + section | Not in D4 product list. Asked hub; parked until answered. |
| Humanoid shown only as "future" | Founder confirmed humanoid robots as a product: add P2 `/humanoid-robots`, nav item, card. |
| Nav links are anchors | Become page links: Humanoid robots, Robotic arm, Cleaning robot, AI vision, About, Contact. |
| Vision/arm demos autoplay | Poster + play button (D10). |
| "Robotic arm, part by part": stock arm video with joint callouts, "Arm, front view" stills, spec table | Breaks D16/D20 (arm is not built; stock is mood only). Rework P3 as a capability page: "we design and build to your requirement", stock shown uncaptioned as mood, spec table = what a client specifies / what we can build to, not product specs. |
| Hero chips "Live from the lab", "Unit 01 online" on stock footage | Remove (D20). Stock stays uncaptioned mood footage. |
| Cleaning robot tag "In development", "Join the pilot" | Keep "In development" (D16). No pilot/client claims. |
| Vision demo stock clip with boxes | Allowed as an illustrated demo, labelled "Illustration" (D16: vision is real, footage is not ours). |
| Roadmap "Next · [year]" | No years (D19). |
| Email `[.com or .tech]` | `cybertronix.tech` (D15); address `TODO(founder)` until confirmed. |
| Prices | None anywhere; "Quote on request" (D18). |
| Spec values `[__]`, statuses `[Status]`, socials, privacy line | Stay as visible placeholders = `TODO(founder)`. |

Approval: Design does not self-approve in this phase (D14). The founder approves the full design via the hub (T10).
