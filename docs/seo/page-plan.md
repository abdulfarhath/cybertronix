# Page plan (T2, rewritten for T9)

Owner: SEO Content · Updated 2026-10-03 · Keywords: `docs/seo/keywords.md` · Text: `content/`

Generated from the front matter and headings in `content/`. If the two ever differ, `content/` wins.

## Rules for every page (Build)
| Rule | Detail |
|---|---|
| Domain | **https://cybertronix.tech** (D15). Canonicals, sitemap, Organization `url` and `sameAs` all point there. Keep the host (www or not) the same as the live site today so existing rankings carry over. |
| What's real (D16) | AI vision = **Available now** (works with existing CCTV). Cleaning robot = **In development** (pilot partners welcome). Humanoid robot and robotic arm = **Built to order**. Never imply a humanoid or arm exists, has shipped or has clients. |
| Schema | P2/P3 use `Service`, never `Product`. P4 uses no `Product` (not on sale). No `foundingDate` anywhere (D19). |
| Prices | None anywhere (D18). Use "we quote on request" wording. |
| Year | Never show the founding year or company age (D19). |
| Stock footage | Mood only (D20). Alt text describes the scene ("Robotic arm moving in a lab"). No caption or copy may present it as our product. |
| Title / meta | Title ≤ 60 chars, meta ≤ 155. Counts in brackets are checked by script. |
| H1 | One per page, real text, above the hero video. |
| FAQ | Visible on the page **and** `FAQPage` JSON-LD with the same words. Hide any FAQ whose answer is still `TODO(founder)`. |
| Unknown facts | `TODO(founder)` stays in `content/` and is never shipped live. Hide that row or sentence. |

---

## P1 · Home `/`
| Field | Value |
|---|---|
| Keyword | robotics company in Hyderabad · Cybertronix |
| Title | Cybertronix · Robotics Company in Hyderabad, India [50] |
| Meta | Cybertronix is a Hyderabad robotics engineering company. AI vision for your existing CCTV, and custom robots designed and built to order. [137] |
| H1 | Cybertronix: robotics company in Hyderabad |
| Schema | `Organization`, `LocalBusiness`, `WebSite`, `FAQPage`, plus site-wide `Organization` |

**H2 outline:** Hero · AI vision for your existing CCTV · What we do · One in-house engineering team · Who we work with · Questions people ask · Tell us your requirement

**FAQ:**
1. What does Cybertronix do?
2. Where is Cybertronix located?
3. Do you sell ready-made robots?
4. Does your AI vision need new cameras?
5. How much does a project cost?

**Internal links:** `/about` · `/ai-vision` · `/cleaning-robot` · `/contact` · `/industries/hospitality` · `/industries/manufacturing`

---

## P2 · Humanoid robot development `/humanoid-robots`
| Field | Value |
|---|---|
| Keyword | humanoid robot company Hyderabad · humanoid robot developer India · custom humanoid robot |
| Title | Humanoid Robot Development in Hyderabad · Cybertronix [53] |
| Meta | Cybertronix designs and builds custom humanoid robots in Hyderabad. In-house AI, mechatronics and electronics engineers. Tell us your requirement. [146] |
| H1 | Humanoid robot development in Hyderabad |
| Schema | `Service`, `FAQPage`, `BreadcrumbList`, plus site-wide `Organization` |

**H2 outline:** Hero · What we build to order · The team behind it · How a custom humanoid project works · How we quote · Questions about humanoid robot development · Tell us your requirement

**FAQ:**
1. Can I buy a ready-made humanoid robot from Cybertronix?
2. How much does it cost to build a custom humanoid robot in India?
3. How long does it take to build a custom humanoid robot?
4. Can the humanoid robot speak Hindi or Telugu?
5. Where is the robot designed and built?

**Internal links:** `/about` · `/ai-vision` · `/contact` · `/robotic-arm`

---

## P3 · Custom robotic arms `/robotic-arm`
| Field | Value |
|---|---|
| Keyword | custom robotic arm manufacturer · robotic arm Hyderabad · robotic arm company India |
| Title | Custom Robotic Arm Design & Build, Hyderabad · Cybertronix [58] |
| Meta | Cybertronix designs and builds custom robotic arms in Hyderabad for your task. In-house mechatronics, mechanical and AI engineers. Quote on request. [148] |
| H1 | Custom robotic arm design and build |
| Schema | `Service`, `FAQPage`, `BreadcrumbList`, plus site-wide `Organization` |

**H2 outline:** Hero · Tasks we can design for · Why a custom arm · The team behind it · How a custom arm project works · How we quote · Questions about custom robotic arms · Tell us your requirement

**FAQ:**
1. Do you sell a ready-made robotic arm?
2. How much does a custom robotic arm cost in India?
3. What information do you need to quote?
4. Can you add a camera so the arm can see?
5. How long does it take to build a custom robotic arm?

**Internal links:** `/ai-vision` · `/contact` · `/humanoid-robots` · `/industries/manufacturing`

---

## P4 · Cleaning robot (in development) `/cleaning-robot`
| Field | Value |
|---|---|
| Keyword | cleaning robot company India · cleaning robot Hyderabad |
| Title | Cleaning Robot in Development, Hyderabad · Cybertronix [54] |
| Meta | Cybertronix is building an autonomous cleaning robot in Hyderabad. It's in development and we're looking for pilot partners. Register your interest. [148] |
| H1 | Our cleaning robot: in development |
| Schema | `WebPage`, `FAQPage`, `BreadcrumbList`, plus site-wide `Organization` |

**H2 outline:** Hero · What we're building · Why we're building it · Become a pilot partner · Questions about our cleaning robot · Stay in touch

**FAQ:**
1. Can I buy the Cybertronix cleaning robot now?
2. What will it clean?
3. When will it be available?
4. What does a pilot partner do?
5. How much will it cost?

**Internal links:** `/ai-vision` · `/contact` · `/industries/hospitality`

---

## P5 · AI vision `/ai-vision`
| Field | Value |
|---|---|
| Keyword | AI video analytics Hyderabad · AI CCTV India · PPE detection |
| Title | AI Video Analytics for Your CCTV, Hyderabad · Cybertronix [57] |
| Meta | Cybertronix AI vision works with the CCTV cameras you already have. Real-time alerts for safety, such as PPE checks. Built in Hyderabad. Book a demo. [149] |
| H1 | AI vision for your existing CCTV cameras |
| Schema | `Service`, `FAQPage`, `BreadcrumbList`, plus site-wide `Organization` |

**H2 outline:** Hero · No new cameras needed · What it detects · Live demo · Where the video is processed · Who it's for · Questions about AI video analytics · Book an AI vision demo

**FAQ:**
1. What is AI video analytics?
2. Does it work with my existing CCTV cameras?
3. What does PPE detection check for?
4. How are alerts sent?
5. How much does it cost?

**Internal links:** `/about` · `/contact` · `/industries/hospitality` · `/industries/manufacturing` · `/robotic-arm`

---

## P6 · About `/about`
| Field | Value |
|---|---|
| Keyword | about Cybertronix robotics |
| Title | About Cybertronix · Robotics Engineering, Hyderabad [51] |
| Meta | Cybertronix is a Hyderabad robotics engineering company with in-house AI, mechatronics, mechanical and electronics engineers. Meet the team. [140] |
| H1 | About Cybertronix |
| Schema | `AboutPage`, `Organization`, `BreadcrumbList`, plus site-wide `Organization` |

**H2 outline:** Hero · What we do · Our engineering team · How we work · Our base in Hyderabad · Careers · Questions about Cybertronix · Talk to us

**FAQ:**
1. Where is Cybertronix based?
2. What kind of engineers work at Cybertronix?
3. Is Cybertronix related to Cybertronix Technologies LLC in Dubai?
4. Do you take on custom projects?
5. Is Cybertronix hiring?

**Internal links:** `/ai-vision` · `/cleaning-robot` · `/contact` · `/humanoid-robots` · `/robotic-arm`

---

## P7 · Contact `/contact`
| Field | Value |
|---|---|
| Keyword | Cybertronix Hyderabad contact / address |
| Title | Contact Cybertronix · Robotics Company, Hyderabad [49] |
| Meta | Contact Cybertronix in Hyderabad. Book an AI vision demo, ask about a custom robot or join our cleaning robot pilot. Quotes on request. [135] |
| H1 | Contact Cybertronix in Hyderabad |
| Schema | `ContactPage`, `LocalBusiness`, `BreadcrumbList`, plus site-wide `Organization` |

**H2 outline:** Hero · Tell us your requirement · Visit us · Call or email · Opening hours · Questions before you get in touch

**FAQ:**
1. Where is your Hyderabad office?
2. Can I visit without an appointment?
3. How fast do you reply?
4. Do you work with clients outside Hyderabad?
5. Can I get a quote by email?

**Internal links:** 

---

## P8 · Manufacturing `/industries/manufacturing`
| Field | Value |
|---|---|
| Keyword | factory automation Hyderabad · industrial automation company Hyderabad |
| Title | Factory Automation in Hyderabad · Cybertronix [45] |
| Meta | AI vision for your factory's existing CCTV, and custom robotic arms built for your task, from a Hyderabad robotics engineering team. Book a visit. [146] |
| H1 | AI vision and custom robots for Hyderabad factories |
| Schema | `Service`, `FAQPage`, `BreadcrumbList`, plus site-wide `Organization` |

**H2 outline:** Hero · Problems we help with · AI vision on your existing CCTV: available now · Custom robotic arms: built to order · How we start · Questions

**FAQ:**
1. Where should a factory start with automation?
2. Do I need new cameras?
3. Can you build a robot for one specific task?
4. How much does it cost?
5. Do you work outside Telangana?

**Internal links:** `/ai-vision` · `/contact` · `/robotic-arm`

---

## P9 · Hospitality `/industries/hospitality`
| Field | Value |
|---|---|
| Keyword | AI CCTV for hotels and malls · robots for hotels India |
| Title | AI CCTV & Robots for Hotels, Malls, Offices · Cybertronix [57] |
| Meta | AI vision for your existing CCTV, a cleaning robot in pilot, and custom humanoid robots built to order, for hotels, malls and offices. Hyderabad. [145] |
| H1 | AI vision and robots for hotels, malls and offices |
| Schema | `Service`, `FAQPage`, `BreadcrumbList`, plus site-wide `Organization` |

**H2 outline:** Hero · AI vision on your existing CCTV: available now · Cleaning robot: in development, pilot partners welcome · Custom humanoid robots: built to order · Questions

**FAQ:**
1. Do you have a reception robot I can buy now?
2. Does AI vision need new cameras?
3. Can my hotel or mall join the cleaning robot pilot?
4. How much does it cost?
5. Do you work outside Hyderabad?

**Internal links:** `/ai-vision` · `/cleaning-robot` · `/contact` · `/humanoid-robots`

---

## Site-wide
| Item | Plan |
|---|---|
| Nav | AI vision · Cleaning robot · Custom humanoids · Custom robotic arms · Industries · About · Contact (button: Tell us your requirement) |
| Footer | NAP (same as Google Business Profile), page links, social links (`sameAs`) |
| Blog | Later. Ideas with real demand that we can answer honestly: "what is AI video analytics", "PPE detection on existing CCTV", "how a custom robot is built". |
