# Start here

## The product
A marketing website for **Cybertronix**, a robotics company in **Hyderabad**.
Goal: rank #1 on Google for "robotics company in Hyderabad", the brand name, and humanoid /
robotic arm / AI vision searches in Hyderabad and India, then turn visitors into enquiries.

## Products (founder confirmed)
| Product | Page |
|---|---|
| Humanoid robots | `/humanoid-robots` |
| Robotic arm | `/robotic-arm` |
| Cleaning robot | `/cleaning-robot` |
| AI vision / surveillance | `/ai-vision` |

## Current state (2026-10-03)
- Design direction **C · Blueprint hybrid**, palette **"Midnight Lab"**: dark cinematic hero, then
  clean technical sections with faint blueprint grid lines.
- Existing canvas (made by the founder's other Claude account):
  https://claude.ai/artifact/VEDcNs3Rp61FzB9hmtfSf7. It has desktop, phone and style guide, with
  graded stock footage (3 Pexels lab-arm clips, 1 Unsplash factory photo).
- Repo created; no site code yet. See `docs/BOARD.md`.

## Where things live
| What | Where |
|---|---|
| Rules | `CLAUDE.md` |
| Decisions | `docs/DECISIONS.md` |
| Tasks and status | `docs/BOARD.md` |
| Every page and section | `docs/PAGES.md` |
| Keywords and SEO plan | `docs/seo/` |
| Founder's physical steps | `docs/FOUNDER-TODO.md` |
| Chat session IDs | `docs/HUB.md` |
| Site code | `site/` (Build creates it) |

## Checks before merging (Build)
`npm run build` passes, no broken links, Lighthouse mobile ≥ 90 for Performance, SEO and
Accessibility on every page, every page has title + meta description + one H1 + schema.
