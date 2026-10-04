# Brand-first proposal (D41)

Owner: SEO Content · 2026-10-04 · **Proposal only: nothing in `content/` is changed yet.**
The founder picks the Home headline, mission and vision (D41). Once picked, SEO Content applies all of it in one pass.

## The rule in one table
| Where | What goes there |
|---|---|
| **H1 / headlines** (visible) | Human, story-led, brand-first. No keyword stuffing. |
| **Eyebrow** (small line above the H1) | The keyword phrase, in plain words, e.g. "Robotics company · Hyderabad". Rendered as a `<p>`, **not** a heading. |
| **Title tag, meta, URL, alt, schema** | Keywords, as now. Unchanged from `page-plan.md`. |
| **First paragraph** | The keyword phrase once, naturally, in the first 1–2 sentences. |
| **H2s** | Mixed: human where it's a story; plain keyword wording where people scan (e.g. "How a custom arm project works"). |

**What SEO gives up:** a keyword in the H1 is one ranking signal among many. Google weighs the title tag
more. With the keyword in the title, eyebrow, URL, first paragraph and schema, the loss is small. The
"Hyderabad" pages stay winnable.

**Brand thread:** the logo story is *"a machine that sees"* (D35, D38). Several headlines below pick
up that line: seeing, watching, noticing. All are honest about status (D21): prototype, in development,
built to order, early build.

## Page by page
| ID | Page | (a) Proposed H1 (brand-led) | Eyebrow (small, keyword) | (b) Where the old keyword goes |
|---|---|---|---|---|
| P1 | Home | **Pick one (founder):** ① "We build machines that see." ② "Robots and AI, engineered in Hyderabad." ③ "Engineering machines that notice what people miss." | Robotics & AI engineering · Hyderabad | "robotics company in Hyderabad": title (as now), eyebrow, first paragraph, Organization/LocalBusiness schema |
| P2 | Humanoid robots | "Your humanoid robot, designed from the job up." | Custom humanoid robot development · Hyderabad | "humanoid robot development Hyderabad": title, eyebrow, first paragraph, `Service` schema |
| P3 | Robotic arm | "An arm shaped around your task." | Custom robotic arm design & build | "custom robotic arm manufacturer": title, eyebrow, H2 "How a custom arm project works", body |
| P4 | Cleaning robot | "Clean floors, without anyone pushing a machine." | Floor-cleaning robot · offices & malls · in development | "floor cleaning robot for offices and malls": title, eyebrow, first paragraph, alt text on the concept drawing |
| P5 | AI vision | "A second pair of eyes at the gowning-room door." | AI gowning & PPE compliance · prototype | "cleanroom gowning compliance AI / surgical PPE detection": title, eyebrow, the "What it's designed to check" H2, body, `Service` schema |
| P6 | About | "Engineers who build what they design." | About Cybertronix · Hyderabad | "about Cybertronix robotics": title, eyebrow, Organization schema |
| P7 | Contact | "Tell us what you want to see, clean or build." | Contact · Jubilee Hills, Hyderabad | "Cybertronix Hyderabad contact": title, eyebrow, visible NAP block, LocalBusiness schema |
| P8 | Manufacturing | "Your line, your task, our engineers." | Factory automation · Hyderabad & Telangana | "factory automation Hyderabad": title, eyebrow, first paragraph |
| P9 | Pharma & healthcare | "Every glove, every mask, before the clean zone." | AI gowning checks · pharma cleanrooms & operating theatres | "cleanroom gowning compliance AI / pharma GMP AI": title, eyebrow, H2s for cleanrooms and theatres, body |
| P10 | Team | "Four kinds of engineer. One team." | Our team · robotics engineers in Hyderabad | "robotics engineers Hyderabad": title, eyebrow, body, `Person` schema later |
| P11 | Retail & malls | "Cameras that notice, floors that clean themselves." | AI vision & floor-cleaning robots · retail & malls | "AI vision for supermarkets / floor cleaning robot for malls": title, eyebrow, the two section H2s |
| P12 | Software | "Tools we built for ourselves, now shared." | Software & projects · Cybertronix | "Cybertronix software / AI developer tools": title, eyebrow |
| P13 | Raqib | "See what your AI is really using." | Raqib · terminal monitor for AI workloads · early build | "AI workload monitor / VRAM monitor for local LLMs": title, eyebrow, the "What Raqib shows" H2, FAQ, `SoftwareApplication` schema |

Honesty check on the headlines:
- P4 "without anyone pushing a machine" is the goal; the "in development" label sits right under it.
- P5 and P9 describe what the prototype is designed to do; the "Prototype" label sits right under them.
- P12 "Tools we built for ourselves": the founder confirms this is how Raqib started (open question d from the Raqib message). If not, use "Software from our engineering team."

## Mission: pick one
Honest: no clients, no scale, no "leading".

1. **"We engineer robots and AI that take on the careful, repetitive work, so people can focus on the work that needs a person."**
2. **"To build machines that see and act reliably, starting from a real problem, in our own lab in Hyderabad."**
3. **"To design and build useful robots and AI products end to end, with one in-house team, and to be honest about what's ready."**

## Vision: pick one
These are aims, worded as aims.

1. **"A Hyderabad product company whose machines quietly keep clean rooms clean, people safe and floors spotless."**
2. **"To grow from custom builds and prototypes into a family of robotics and AI products that India's labs, hospitals and workplaces rely on."**
3. **"Machines that notice what people miss, designed and built in India."**

> Note on vision 2: "rely on" is an aim, not a claim. Keep it only if the founder is comfortable with it.

## After the founder picks
1. SEO Content updates every `content/P*.md`: new `h1`, a new `eyebrow:` front-matter field, and keyword moved into the first paragraph.
2. `page-plan.md` gets regenerated with an Eyebrow row.
3. Design swaps the headlines on the boards; Build renders the eyebrow as `<p class="eyebrow">`, never as `<h1>`/`<h2>`.
4. Mission and vision go on P1 (short) and P6 (full).
