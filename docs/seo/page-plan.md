# Page plan (T2)

Owner: SEO Content · Updated 2026-10-03 · Keywords: `docs/seo/keywords.md`

## Rules for every page (Build)
| Rule | Detail |
|---|---|
| Title | ≤ 60 chars, primary keyword first, brand last: `… · Cybertronix` |
| Meta | ≤ 155 chars, one benefit + Hyderabad/India + a call to action |
| H1 | One per page, real text, above the hero video |
| FAQ | Visible on the page **and** `FAQPage` JSON-LD with the same words |
| Schema on every page | `Organization` (site-wide, with `sameAs`), `BreadcrumbList` (not on home), `WebPage` |
| Canonical | Absolute URL on the final domain. `TODO(founder)`: domain (see keywords.md B1) |
| Alt text | Describe what is shown. Stock footage alt must not claim it is our robot. |
| Unknown facts | Text stays `TODO(founder)` until real. Build hides a row/answer rather than ship a TODO live. |

Lengths in brackets are character counts (checked by script).

---

## P1 · Home `/`
| Field | Value |
|---|---|
| Keyword | robotics company in Hyderabad · Cybertronix |
| Title | Cybertronix · Robotics Company in Hyderabad, India [50] |
| Meta | Cybertronix is a robotics company in Hyderabad building humanoid robots, a robotic arm, a cleaning robot and AI vision. Book a demo. [132] |
| H1 | Cybertronix: robotics company in Hyderabad |
| Schema | `Organization` + `LocalBusiness` (address from F1), `WebSite`, `FAQPage` |

**H2 outline**
1. Robots we build in Hyderabad (4 product cards → P2–P5)
2. Humanoid robots
3. Robotic arm for industry
4. Cleaning robot
5. AI vision and surveillance
6. Who we work with (industries → P8, P9 if approved)
7. Why a Hyderabad robotics team (local support, demos, visits) — only real claims
8. Questions people ask
9. Book a demo (CTA → P7)

**FAQ**
1. What does Cybertronix do?
2. Where is Cybertronix located in Hyderabad?
3. Which robots does Cybertronix make?
4. Can I see a robot demo in Hyderabad?
5. Do you supply robots outside Hyderabad, across India?

**Internal links:** P2, P3, P4, P5 (cards), P6 (about), P7 (CTA, footer), P8/P9 (industries strip).

---

## P2 · Humanoid robots `/humanoid-robots`
| Field | Value |
|---|---|
| Keyword | humanoid robot India · humanoid robot Hyderabad |
| Title | Humanoid Robot in Hyderabad, India · Cybertronix [48] |
| Meta | Humanoid robots designed by Cybertronix in Hyderabad for reception, guidance and business use. See specs, uses and pricing, and book a demo. [140] |
| H1 | Humanoid robots by Cybertronix, Hyderabad |
| Schema | `Product` (name, image, description, brand; `offers` only with a real price), `FAQPage`, `BreadcrumbList` |

**H2 outline**
1. What our humanoid robot does
2. Where it works (reception, events, showrooms, offices — only confirmed uses)
3. Specifications (spec table, D8)
4. Humanoid robot price in India (honest range or "on request" + what changes the price)
5. Built in Hyderabad (only if true)
6. Questions about humanoid robots
7. Book a humanoid robot demo

**FAQ**
1. How much does a humanoid robot cost in India?
2. What can the Cybertronix humanoid robot do?
3. Can the humanoid robot speak English, Hindi and Telugu? `TODO(founder)`
4. Can I rent a humanoid robot for an event in Hyderabad? `TODO(founder)`
5. How long does delivery and setup take? `TODO(founder)`

**Internal links:** P1, P9 (hospitality), P5 (vision inside the robot, if true), P7 (demo).

---

## P3 · Robotic arm `/robotic-arm`
| Field | Value |
|---|---|
| Keyword | industrial robotic arm India · robotic arm Hyderabad |
| Title | Industrial Robotic Arm in Hyderabad, India · Cybertronix [56] |
| Meta | An industrial robotic arm from Cybertronix, Hyderabad, for pick and place and repeat factory tasks. Specs, price guide and a live demo. [135] |
| H1 | Industrial robotic arm, made for Indian factories |
| Schema | `Product`, `FAQPage`, `BreadcrumbList` |

**H2 outline**
1. What the robotic arm does
2. Tasks it automates (pick and place, sorting, machine tending — only confirmed)
3. Specifications (axes, payload, reach, repeatability, controller) — table
4. Robotic arm price in India
5. Installation and support in Hyderabad and across India
6. Questions about our robotic arm
7. See the arm working (CTA)

**FAQ**
1. What is the price of an industrial robotic arm in India?
2. What payload and reach does the Cybertronix arm have? `TODO(founder)`
3. Is it a cobot that can work next to people? `TODO(founder)`
4. Can it be programmed without a robotics engineer?
5. Do you install and service the arm in Hyderabad?

**Internal links:** P1, P8 (manufacturing), P5 (vision for quality/safety), P7.

---

## P4 · Cleaning robot `/cleaning-robot`
| Field | Value |
|---|---|
| Keyword | commercial cleaning robot India · cleaning robot Hyderabad |
| Title | Commercial Cleaning Robot in India · Cybertronix [48] |
| Meta | Autonomous cleaning robot by Cybertronix, Hyderabad, for offices, malls and facilities in India. See how it works, specs and pricing. [133] |
| H1 | Commercial cleaning robot by Cybertronix |
| Schema | `Product`, `FAQPage`, `BreadcrumbList` |

**H2 outline**
1. What the cleaning robot cleans (`TODO(founder)`: floors? solar panels? both?)
2. Where it works (only confirmed spaces)
3. How it works (mapping, schedule, docking — only real features)
4. Specifications — table
5. Cleaning robot price in India
6. Questions about our cleaning robot
7. Book a cleaning robot demo

**FAQ**
1. How much does a commercial cleaning robot cost in India?
2. What surfaces and spaces can it clean?
3. Does it vacuum, mop or scrub? `TODO(founder)`
4. How long does it run on one charge? `TODO(founder)`
5. Does it need staff to operate it?

**Internal links:** P1, P9 (hospitality), P8 (if for factories), P7.

> If the founder confirms it is a **solar panel** cleaning robot, the keyword group switches to "solar panel cleaning robot India / Hyderabad" and title becomes `Solar Panel Cleaning Robot in India · Cybertronix` [49].

---

## P5 · AI vision / surveillance `/ai-vision`
| Field | Value |
|---|---|
| Keyword | AI video analytics Hyderabad · AI surveillance India · PPE detection |
| Title | AI Video Analytics & PPE Detection, Hyderabad · Cybertronix [59] |
| Meta | Cybertronix AI vision turns CCTV into real-time alerts for PPE, intrusion and safety. Built in Hyderabad for Indian sites. Book a demo. [135] |
| H1 | AI vision and surveillance for safer sites |
| Schema | `Service` (or `SoftwareApplication` if sold as software), `FAQPage`, `BreadcrumbList` |

**H2 outline**
1. What our AI vision detects (PPE: helmet, vest; intrusion; others only if real)
2. Live demo (the existing canvas demo, real HTML labels around it)
3. Works with your CCTV? (`TODO(founder)`)
4. Where it runs: on-site or cloud, and your data (`TODO(founder)`)
5. Industries: factories, construction, warehouses (→ P8)
6. Questions about AI surveillance
7. Book an AI vision demo

**FAQ**
1. What is AI video analytics?
2. Can it work with my existing CCTV cameras? `TODO(founder)`
3. What does PPE detection check for?
4. Where is the video processed and stored? `TODO(founder)`
5. How are alerts sent (app, SMS, WhatsApp, email)? `TODO(founder)`

**Internal links:** P1, P8, P3 (vision + arm), P7.

---

## P6 · About `/about`
| Field | Value |
|---|---|
| Keyword | about Cybertronix robotics |
| Title | About Cybertronix · Robotics Team in Hyderabad [46] |
| Meta | Meet Cybertronix, a Hyderabad robotics team building humanoid robots, a robotic arm, a cleaning robot and AI vision for India. [126] |
| H1 | About Cybertronix |
| Schema | `AboutPage`, `Organization` (founder, foundingDate, address — only real), `BreadcrumbList` |

**H2 outline**
1. Our story (`TODO(founder)`: year, why we started)
2. What we build
3. The team (`TODO(founder)`: names/photos with permission)
4. Our lab in Hyderabad
5. How we work: honest specs, local support
6. Careers (if hiring)
7. Talk to us

**FAQ**
1. When was Cybertronix founded? `TODO(founder)`
2. Who founded Cybertronix? `TODO(founder)`
3. Are your robots designed in India?
4. Is Cybertronix related to Cybertronix Technologies LLC in Dubai? (answer: `TODO(founder)` — likely "no")
5. Is Cybertronix hiring?

**Internal links:** P1, P2–P5, P7.

---

## P7 · Contact `/contact`
| Field | Value |
|---|---|
| Keyword | Cybertronix Hyderabad contact / address |
| Title | Contact Cybertronix · Robot Demo in Hyderabad [45] |
| Meta | Call, email or visit Cybertronix in Hyderabad. Book a demo of our humanoid robot, robotic arm, cleaning robot or AI vision. [123] |
| H1 | Contact Cybertronix in Hyderabad |
| Schema | `ContactPage`, `LocalBusiness` (name, address, phone, geo, openingHours — all from F1), `BreadcrumbList` |

**H2 outline**
1. Book a demo (form: name, company, phone, product, message)
2. Visit us (address + Google Map embed, lazy-loaded)
3. Call or email
4. Opening hours (`TODO(founder)`)
5. Questions before you visit

**FAQ**
1. Where is your Hyderabad office?
2. Can I visit the lab without an appointment?
3. How fast do you reply to an enquiry?
4. Do you give demos outside Hyderabad?
5. Can I get a quote by email?

**Internal links:** P1, P2–P5 (product dropdown in form).

---

## P8 · Manufacturing `/industries/manufacturing` (approved, D13)
| Field | Value |
|---|---|
| Keyword | factory automation Hyderabad · industrial automation company Hyderabad |
| Title | Factory Automation in Hyderabad · Cybertronix [45] |
| Meta | Robots and AI vision for factories in Hyderabad and Telangana: a robotic arm for repeat tasks, PPE detection for safety. Book a site visit. [139] |
| H1 | Factory automation for Hyderabad manufacturers |
| Schema | `Service` (areaServed Hyderabad, Telangana, India), `FAQPage`, `BreadcrumbList` |

**H2s:** Problems we solve on the shop floor · Robotic arm for repeat tasks (→P3) · AI vision for safety and quality (→P5) · How a project runs (visit, trial, install) · Questions · Book a site visit
**FAQ:** Where do I start with automation in a small factory? · How long does a pilot take? · Do I need to change my line? · What does support look like after install? · Do you work outside Telangana?

## P9 · Hospitality `/industries/hospitality` (approved, D13)
| Field | Value |
|---|---|
| Keyword | robots for hotels India · reception robot for hotel |
| Title | Robots for Hotels & Hospitality in India · Cybertronix [54] |
| Meta | Humanoid reception robots and cleaning robots for hotels, malls and offices in India, from Cybertronix, Hyderabad. See uses and book a demo. [140] |
| H1 | Robots for hotels, malls and offices |
| Schema | `Service`, `FAQPage`, `BreadcrumbList` |

**H2s:** Greet guests with a humanoid robot (→P2) · Keep floors clean with a cleaning robot (→P4) · Guest safety with AI vision (→P5) · Getting started · Questions · Book a demo
**FAQ:** What can a reception robot do in a hotel? · Do guests like talking to robots? (no invented stats) · Can it speak local languages? · How much floor can the cleaning robot cover? · Can we try it before buying?

---

## Site-wide
| Item | Plan |
|---|---|
| Nav | Humanoid · Robotic arm · Cleaning robot · AI vision · About · Contact (button: Book a demo) |
| Footer | NAP (same as GBP), product links, industries, LinkedIn/YouTube/Instagram (`sameAs`) |
| Blog | Later. Ideas with clear search demand: "humanoid robot price in India", "robotic arm price in India", "what is PPE detection". |
