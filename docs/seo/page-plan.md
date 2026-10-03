# Page plan (T2 → T9 → T9b)

Owner: SEO Content · Updated 2026-10-03 · Keywords: `docs/seo/keywords.md` · Text: `content/`

Generated from the front matter and headings in `content/`. If the two ever differ, `content/` wins.

## Rules for every page (Build)
| Rule | Detail |
|---|---|
| Domain | **https://cybertronix.tech** (D15). Canonicals, sitemap, Organization `url` and `sameAs` all point there. Keep the host (www or not) the same as the live site today. |
| Status labels (D21) | AI vision = **Prototype · pilot partners welcome** · Cleaning robot = **In development** (pilot partners welcome) · Humanoid + arm = **Built to order** · Retail/factory vision = **Custom project**. Nothing is "available now". |
| Wording (D23) | AI vision features are always "designed to", never "deployed", "used by" or "trusted by". |
| Clients (D26) | None anywhere. No logos, case studies or "used by". Never mention T-Hub or any incubator. |
| Schema | P2/P3/P5/P8/P9/P11 use `Service`, never `Product`. P4 has no `Product` (not on sale). No `foundingDate` anywhere (D19). `LocalBusiness` NAP exactly as P7 (D25). |
| Prices | None anywhere (D18). Use "we quote on request". |
| Year | Never show the founding year or company age (D19). |
| Stock footage | Mood only (D20). Alt text describes the scene. No caption or copy may present it as our product. The vision demo is labelled "Illustration". |
| Team (D27) | Grey "Photo coming soon" cards. Hide any card with no real name. Never use fake names or faces. |
| Title / meta | Title ≤ 60 chars, meta ≤ 155. Counts in brackets are checked by script. |
| FAQ | Visible on the page **and** in `FAQPage` JSON-LD with the same words. Hide any FAQ whose answer is still `TODO(founder)`. |
| Unknown facts | `TODO(founder)` stays in `content/` and is never shipped live. |

---

## P1 · Home `/`
| Field | Value |
|---|---|
| Keyword | robotics company in Hyderabad · Cybertronix |
| Title | Cybertronix · Robotics Company in Hyderabad, India [50] |
| Meta | Cybertronix is a robotics engineering company in Hyderabad building AI vision for gowning and PPE compliance, a floor-cleaning robot and custom robots. [151] |
| H1 | Cybertronix: robotics company in Hyderabad |
| Schema | `Organization`, `LocalBusiness`, `WebSite`, `FAQPage`, plus site-wide `Organization` |

**H2 outline:** Hero · AI vision for gowning and PPE compliance · What we're building · One in-house engineering team · Industries · Questions people ask · Tell us your requirement

**FAQ:**
1. What does Cybertronix do?
2. Where is Cybertronix located?
3. Can I buy a Cybertronix product today?
4. Does your AI vision need new cameras?
5. How much does a project cost?

**Internal links:** `/ai-vision` · `/contact` · `/industries/manufacturing` · `/industries/pharma-healthcare` · `/industries/retail` · `/team`

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
| Keyword | floor cleaning robot for offices and malls · commercial cleaning robot India · cleaning robot Hyderabad |
| Title | Floor Cleaning Robot for Offices & Malls · Cybertronix [54] |
| Meta | Cybertronix is building an autonomous floor-cleaning robot for offices and malls in Hyderabad. In development. Pilot partners welcome. [134] |
| H1 | Autonomous floor-cleaning robot for offices and malls |
| Schema | `WebPage`, `FAQPage`, `BreadcrumbList`, plus site-wide `Organization` |

**H2 outline:** Hero · What we're building · Why offices and malls · Become a pilot partner · Questions about our cleaning robot · Stay in touch

**FAQ:**
1. Can I buy the Cybertronix cleaning robot now?
2. What will it clean?
3. What does a pilot partner do?
4. Who is building it?
5. How much will it cost?

**Internal links:** `/ai-vision` · `/contact` · `/industries/retail` · `/team`

---

## P5 · AI vision (prototype) `/ai-vision`
| Field | Value |
|---|---|
| Keyword | cleanroom gowning compliance AI · surgical PPE detection · GMP video analytics India · AI CCTV for existing cameras Hyderabad |
| Title | AI Gowning & PPE Compliance for Cleanrooms · Cybertronix [56] |
| Meta | Our AI vision prototype checks gowning and PPE (gloves, masks, shoe covers, gowns) on your existing CCTV, for pharma cleanrooms and surgery. Pilots open. [153] |
| H1 | AI vision for gowning and PPE compliance |
| Schema | `Service`, `FAQPage`, `BreadcrumbList`, plus site-wide `Organization` |

**H2 outline:** Hero · What it's designed to check · Where it fits · How it's designed to work · Your video stays on your premises · See the prototype · Become a pilot partner · Questions about AI gowning and PPE compliance · Talk to us

**FAQ:**
1. Is Cybertronix AI vision available to buy?
2. Does it work with my existing CCTV cameras?
3. Where is the video processed?
4. How are alerts sent?
5. Can it check other things besides gowning and PPE?

**Internal links:** `/contact` · `/industries/manufacturing` · `/industries/pharma-healthcare` · `/industries/retail` · `/team`

---

## P6 · About `/about`
| Field | Value |
|---|---|
| Keyword | about Cybertronix robotics |
| Title | About Cybertronix · Robotics Engineering, Hyderabad [51] |
| Meta | Cybertronix is a Hyderabad robotics engineering company building its own AI vision and cleaning robot, and taking on custom robot projects. [139] |
| H1 | About Cybertronix |
| Schema | `AboutPage`, `Organization`, `BreadcrumbList`, plus site-wide `Organization` |

**H2 outline:** Hero · What we're building · Product-first, open to projects · Our engineering team · How we work · Our base in Hyderabad · Questions about Cybertronix · Talk to us

**FAQ:**
1. Where is Cybertronix based?
2. Is Cybertronix a product company or a services company?
3. What kind of engineers work at Cybertronix?
4. Do you take on custom projects?
5. Is Cybertronix related to Cybertronix Technologies LLC in Dubai?

**Internal links:** `/ai-vision` · `/cleaning-robot` · `/contact` · `/humanoid-robots` · `/robotic-arm` · `/team`

---

## P7 · Contact `/contact`
| Field | Value |
|---|---|
| Keyword | Cybertronix Hyderabad contact / address · Cybertronix Jubilee Hills |
| Title | Contact Cybertronix · Jubilee Hills, Hyderabad [46] |
| Meta | Contact Cybertronix in Jubilee Hills, Hyderabad: +91 90598 97807, info@cybertronix.com. Join a pilot or tell us your requirement. [129] |
| H1 | Contact Cybertronix in Hyderabad |
| Schema | `ContactPage`, `LocalBusiness`, `BreadcrumbList`, plus site-wide `Organization` |

**H2 outline:** Hero · Tell us your requirement · Visit us · Call or email · Opening hours · Questions before you get in touch

**FAQ:**
1. Where is your Hyderabad office?
2. Can I visit without an appointment?
3. How do I join a pilot?
4. Do you work with clients outside Hyderabad?
5. Can I get a quote by email?

**Internal links:** 

---

## P8 · Manufacturing `/industries/manufacturing`
| Field | Value |
|---|---|
| Keyword | factory automation Hyderabad · industrial automation company Hyderabad · custom automation Telangana |
| Title | Factory Automation & Custom Robots, Hyderabad · Cybertronix [59] |
| Meta | Custom robotic arms and computer vision for factories in Hyderabad and Telangana, built to your requirement by in-house engineers. Quote on request. [148] |
| H1 | Custom robots and computer vision for Hyderabad factories |
| Schema | `Service`, `FAQPage`, `BreadcrumbList`, plus site-wide `Organization` |

**H2 outline:** Hero · Problems we can help with · Custom robotic arms · Computer vision on your existing CCTV · How a project starts · Questions

**FAQ:**
1. Where should a factory start with automation?
2. Can you build a robot for one specific task?
3. Do I need new cameras for vision checks?
4. How much does it cost?
5. Do you work outside Telangana?

**Internal links:** `/ai-vision` · `/contact` · `/robotic-arm` · `/team`

---

## P9 · Pharma & healthcare `/industries/pharma-healthcare`
| Field | Value |
|---|---|
| Keyword | cleanroom gowning compliance AI · pharma GMP AI India · surgeon PPE detection · pharma automation Hyderabad |
| Title | AI Gowning Compliance for Pharma & Hospitals · Cybertronix [58] |
| Meta | AI vision designed to check cleanroom gowning and surgical PPE on your existing CCTV, with video kept on-site. Prototype from Hyderabad. Pilots open. [149] |
| H1 | AI gowning checks for pharma cleanrooms and operating theatres |
| Schema | `Service`, `FAQPage`, `BreadcrumbList`, plus site-wide `Organization` |

**H2 outline:** Hero · Built next to India's pharma hub · Pharma and drug-research cleanrooms · Hospitals and operating theatres · Video stays on your premises · Questions

**FAQ:**
1. Is this system in use at pharma sites today?
2. Does it make my site GMP-compliant?
3. Does it need new cameras?
4. Does video leave our site?
5. How do we join the pilot?

**Internal links:** `/about` · `/ai-vision` · `/contact` · `/team`

---

## P10 · Team `/team`
| Field | Value |
|---|---|
| Keyword | Cybertronix team · robotics engineers Hyderabad |
| Title | Our Team · Robotics Engineers in Hyderabad · Cybertronix [56] |
| Meta | Meet the Cybertronix team: in-house AI, mechatronics, mechanical and electronics engineers in Jubilee Hills, Hyderabad, building robots and AI vision. [150] |
| H1 | The Cybertronix team |
| Schema | `AboutPage`, `Organization`, `BreadcrumbList`, plus site-wide `Organization` |

**H2 outline:** Hero · What our engineers do · People · How we work together · Join us · Questions

**FAQ:**
1. Where does the team work?
2. Does Cybertronix outsource engineering?
3. Can I meet the engineers before a project?

**Internal links:** `/about` · `/ai-vision` · `/contact`

---

## P11 · Retail & malls `/industries/retail`
| Field | Value |
|---|---|
| Keyword | AI vision for supermarkets · retail video analytics India · floor cleaning robot for malls |
| Title | AI Vision & Floor Cleaning Robots for Retail · Cybertronix [58] |
| Meta | Custom AI vision for supermarkets on your existing CCTV, and a floor-cleaning robot for malls in development. Hyderabad engineers. Tell us your need. [149] |
| H1 | AI vision and robots for supermarkets and malls |
| Schema | `Service`, `FAQPage`, `BreadcrumbList`, plus site-wide `Organization` |

**H2 outline:** Hero · Custom AI vision for supermarkets and retail · Floor-cleaning robot for malls · Questions

**FAQ:**
1. Do you have a ready-made retail analytics product?
2. Does it need new cameras?
3. Can our mall test the cleaning robot?
4. How much does it cost?
5. Where are you based?

**Internal links:** `/ai-vision` · `/cleaning-robot` · `/contact` · `/team`

---

## Site-wide
| Item | Plan |
|---|---|
| Nav | AI vision · Cleaning robot · Custom robots (humanoid, arm) · Industries (Pharma & healthcare, Retail & malls, Manufacturing) · About · Team · Contact (button: Tell us your requirement) |
| Footer | NAP exactly as P7 (D25), page links, social links (`sameAs`, `TODO(founder)`) |
| Blog | Later. Honest topics with real demand: "cleanroom gowning steps and common mistakes", "what is AI video analytics", "why process CCTV video on-site". |
