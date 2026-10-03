# Page data for the boards. Words come from content/*.md (SEO Content, T9/T9b); Design only lays them out.
F = "[[TODO(founder)]]"
PROTO = "Prototype · pilot partners welcome"
DEV = "In development · pilot partners welcome"
REQ = "Tell us your requirement"
TEAM4 = [("AI engineering", "Computer vision, machine learning and decision software"), ("Mechatronics", "Motors, sensors and control systems"),
         ("Mechanical", "Frames, joints, grippers and enclosures"), ("Electronics", "Circuit boards, power and wiring")]
PAGES = []

PAGES.append(dict(id="P1", name="Home", file="Main", eyebrow="Robotics engineering · Jubilee Hills, Hyderabad",
    h1="Cybertronix: robotics company in Hyderabad",
    lead="We're a Hyderabad engineering team building AI vision that checks gowning and PPE on the CCTV cameras you already have, an autonomous floor-cleaning robot, and custom robots built to your requirement.",
    ctas=[("See AI vision", "/ai-vision"), (REQ, "/contact")], media="home",
    sections=[
        dict(type="split", sid="P1.2", h2="AI vision for gowning and PPE compliance", status=PROTO, media="vision", paras=[
            "In pharma cleanrooms and operating theatres, one missing glove or mask matters.",
            "Our AI vision prototype is designed to check gloves, masks, shoe covers and gowns on your existing CCTV, run on-site so video stays on your premises, and alert your team."],
            ctas=[("See how it's designed to work", "/ai-vision"), ("Pharma and healthcare", "/industries/pharma-healthcare")]),
        dict(type="cards", sid="P1.3", h2="What we're building"),
        dict(type="table", sid="P1.4", h2="One in-house engineering team", light=True, cols=("Discipline", "What they do"),
             intro="Everything we make is designed and built by our own engineers in Hyderabad.", rows=[
            ("AI engineering", "Computer vision and the software that makes decisions."), ("Mechatronics", "Motors, sensors and control, working together."),
            ("Mechanical", "Frames, joints and grippers."), ("Electronics", "Boards, power and wiring.")], ctas=[("Meet the team", "/team")]),
        dict(type="links", sid="P1.5", h2="Industries", items=[("Pharma and healthcare", "/industries/pharma-healthcare"), ("Retail and malls", "/industries/retail"), ("Manufacturing", "/industries/manufacturing")]),
        dict(type="faq", sid="P1.6", h2="Questions people ask", light=True, items=[
            ("What does Cybertronix do?", "Cybertronix is a robotics engineering company in Hyderabad. We're building our own products, an AI vision system for gowning and PPE compliance and an autonomous floor-cleaning robot, and we take on custom projects, including humanoid robots and robotic arms built to your requirement."),
            ("Where is Cybertronix located?", "Rd No. 10C, Gayatri Hills, Jubilee Hills, Hyderabad. Phone +91 90598 97807. See the {contact page|/contact}."),
            ("Can I buy a Cybertronix product today?", "Not yet. Our AI vision is a prototype and our cleaning robot is in development. Both are open to pilot partners. Humanoid robots and robotic arms are built to order."),
            ("Does your AI vision need new cameras?", "No. It's designed to work with your existing CCTV and run on-site."),
            ("How much does a project cost?", "Every project is different, so we quote on request.")]),
        dict(type="cta", sid="P1.7", h2=REQ, intro="Tell us what you want to check, clean or build. We'll tell you honestly what we can do.", ctas=[(REQ, "/contact")]),
    ]))

PAGES.append(dict(id="P2", name="Humanoid robot development", file="P2-Humanoid", eyebrow="Custom robots · Hyderabad", status="Built to order",
    h1="Humanoid robot development in Hyderabad",
    lead="Need a humanoid robot for a specific job? Our engineers design and build it to your requirement, from the first sketch to a working robot.",
    ctas=[(REQ, "/contact?topic=humanoid")], media="humanoid",
    sections=[
        dict(type="tiles", sid="P2.2", h2="What we build to order", intro="You tell us the job. We design a humanoid robot around it. Typical requirements we can work to:", items=[
            ("Talk and respond", "A robot that greets people and answers questions."), ("Guide and move", "A robot that moves around a space safely."),
            ("Show and present", "A robot with a screen for information or branding."), ("Research and teaching", "A platform for labs and classrooms.")]),
        dict(type="table", sid="P2.3", h2="The team behind it", light=True, cols=("Discipline", "What it does in a humanoid"),
             intro="A humanoid robot needs four kinds of engineering. We have all four in-house.", rows=[
            ("AI engineering", "Vision, speech and the software that decides what to do"), ("Mechatronics", "Motors, sensors and control loops for smooth, safe movement"),
            ("Mechanical", "Body, joints and frame"), ("Electronics", "Boards, battery, power and wiring")]),
        dict(type="tiles", sid="P2.4", h2="How a custom humanoid project works", numbered=True, items=[
            ("Requirement", "You tell us what the robot must do, where, and for whom."), ("Feasibility", "We tell you honestly what is possible, and what isn't."),
            ("Design", "We share the design with you before we build."), ("Build and test", "We build and test it in Hyderabad."),
            ("Handover", "We set it up and train your team."), ("Confirm steps", F)]),
        dict(type="bullets", sid="P2.5", h2="How we quote", intro="Every humanoid robot is different, so we quote on request. The biggest factors are:", items=[
            "How it moves: a wheeled base, or walking", "How it talks: set replies, or a custom AI conversation", "How many languages it speaks", "How it looks: size, finish and branding"],
             ctas=[("Ask for a quote", "/contact?topic=humanoid")]),
        dict(type="faq", sid="P2.6", h2="Questions about humanoid robot development", light=True, items=[
            ("Can I buy a ready-made humanoid robot from Cybertronix?", "No. We don't sell a ready-made humanoid robot today. We design and build one to your requirement."),
            ("How much does it cost to build a custom humanoid robot in India?", "It depends on how the robot moves, talks and looks. We quote on request after we understand your requirement."),
            ("How long does it take to build a custom humanoid robot?", F),
            ("Can the humanoid robot speak Hindi or Telugu?", f"We can build language support to your requirement. {F}"),
            ("Where is the robot designed and built?", f"By our in-house engineers in Hyderabad. {F}")]),
        dict(type="cta", sid="P2.7", h2=REQ, intro="Describe the job. We'll tell you if a humanoid robot is the right answer and what it would take.", ctas=[(REQ, "/contact?topic=humanoid"), ("Custom robotic arms", "/robotic-arm")]),
    ]))

PAGES.append(dict(id="P3", name="Custom robotic arms", file="P3-Arm", eyebrow="Custom robots · Hyderabad", status="Built to order",
    h1="Custom robotic arm design and build",
    lead="Have a task a standard arm can't handle, or one that doesn't need a big brand robot? We design and build a robotic arm for your task, in Hyderabad.",
    ctas=[(REQ, "/contact?topic=robotic-arm")], media="arm",
    sections=[
        dict(type="table", sid="P3.2", h2="Tasks we can design for", cols=("Task", "What the arm would do"), rows=[
            ("Pick and place", "Move parts from a conveyor, tray or bin to the next station"), ("Sorting", "Separate parts by type or size. Add {AI vision|/ai-vision} to sort by what a camera sees"),
            ("Machine loading", "Load and unload a machine"), ("Packing", "Put parts into boxes or trays"), ("Lab and test work", "Repeat precise movements for testing or research")]),
        dict(type="tiles", sid="P3.3", h2="Why a custom arm", items=[
            ("Built for your part", "The reach, payload and gripper match the job."), ("Fits your space", "Designed around your line, table or machine."),
            ("Vision built in", "Our AI team can add a camera so the arm sees what it picks."), ("Local engineers", "The team that designs it is in Hyderabad.")]),
        dict(type="table", sid="P3.4", h2="The team behind it", light=True, cols=("Discipline", "What it does in a robotic arm"), rows=[
            ("Mechanical", "Links, joints, gripper and mounting"), ("Mechatronics", "Motors, drives, sensors and motion control"),
            ("Electronics", "Controller boards, power and safety circuits"), ("AI engineering", "Vision and smart picking")]),
        dict(type="tiles", sid="P3.5", h2="How a custom arm project works", numbered=True, items=[
            ("Requirement", "Your part, the task, cycle time and space."), ("Feasibility", "We tell you honestly if a custom arm makes sense."),
            ("Design", "Reach, payload and gripper, shared with you before the build."), ("Build and test", "In Hyderabad, on your sample parts."),
            ("Install", "We set it up and train your team."), ("Confirm steps", F)]),
        dict(type="bullets", sid="P3.6", h2="How we quote", intro="We quote on request. The biggest factors are:", items=[
            "Payload and reach", "Gripper or tool", "Speed and accuracy needed", "Safety and connecting to your existing machines"], ctas=[("Ask for a quote", "/contact?topic=robotic-arm")]),
        dict(type="faq", sid="P3.7", h2="Questions about custom robotic arms", light=True, items=[
            ("Do you sell a ready-made robotic arm?", "No. We design and build robotic arms to your requirement."),
            ("How much does a custom robotic arm cost in India?", "It depends on payload, reach, the gripper and the accuracy you need. We quote on request."),
            ("What information do you need to quote?", "The part (size, weight, material), the task, how fast it must run and a photo or video of the space."),
            ("Can you add a camera so the arm can see?", f"Yes. Our AI engineering team builds vision systems, so we can add a camera to the arm's design. {F}"),
            ("How long does it take to build a custom robotic arm?", F)]),
        dict(type="cta", sid="P3.8", h2=REQ, intro="Send us a photo or video of the task. We'll tell you what it would take.", ctas=[(REQ, "/contact?topic=robotic-arm"), ("Manufacturing", "/industries/manufacturing")]),
    ]))

PAGES.append(dict(id="P4", name="Cleaning robot", file="P4-Cleaning", eyebrow="Our product · offices and malls", status=DEV,
    h1="Autonomous floor-cleaning robot for offices and malls",
    lead="We're building a robot that cleans office and mall floors on its own, on a schedule, so your housekeeping team can focus on the jobs that need a person.",
    ctas=[("Become a pilot partner", "/contact?topic=cleaning-pilot")], media="cleaning",
    sections=[
        dict(type="bullets", sid="P4.2", h2="What we're building", intro="An autonomous floor-cleaning robot designed to:", items=[
            "Clean large office and mall floors on a schedule", "Find its way around people and obstacles", "Need very little staff time"],
             after=f"Cleaning modes: {F} (hidden until answered, D29)."),
        dict(type="text", sid="P4.3", h2="Why offices and malls", paras=["Offices and malls have large floors that need cleaning every day, often while people are around. It's repetitive work, which makes it a good job for a robot."]),
        dict(type="tiles", sid="P4.4", h2="Become a pilot partner", light=True, intro="We're looking for a small number of offices and malls to test the robot with us before launch.", items=[
            ("A real floor", "Gives us a real floor to test on."), ("Honest feedback", "Tells us what works and what doesn't."), ("Shape the robot", "Helps shape the final robot.")],
             after=f"Pilot terms: agreed per site, so talk to us (D29).", ctas=[("Register your interest", "/contact?topic=cleaning-pilot")]),
        dict(type="faq", sid="P4.5", h2="Questions about our cleaning robot", light=True, items=[
            ("Can I buy the Cybertronix cleaning robot now?", "Not yet. It's in development. {Register your interest|/contact?topic=cleaning-pilot} or join as a pilot partner."),
            ("What will it clean?", "Floors in offices and malls."),
            ("What does a pilot partner do?", "You give us a real floor to test on and tell us honestly how the robot performs."),
            ("Who is building it?", "Our in-house team of mechatronics, mechanical, electronics and AI engineers in Hyderabad. {Meet the team|/team}."),
            ("How much will it cost?", "We'll share pricing when it's ready. Quotes will be on request.")]),
        dict(type="cta", sid="P4.6", h2="Stay in touch", intro="Register your interest and we'll tell you when pilots start.", ctas=[("Register your interest", "/contact?topic=cleaning-pilot"), ("Retail and malls", "/industries/retail")]),
    ]))

PAGES.append(dict(id="P5", name="AI vision", file="P5-Vision", eyebrow="Our product · existing CCTV", status=PROTO,
    h1="AI vision for gowning and PPE compliance",
    lead="A wrong glove, a missing mask or an uncovered shoe can compromise a cleanroom or an operating theatre. Our AI vision prototype is designed to check gowning and PPE on the CCTV cameras you already have, and to alert your team before someone walks into a critical zone.",
    ctas=[("Become a pilot partner", "/contact?topic=ai-vision"), ("See the prototype", "#p5-6")], media=None,
    sections=[
        dict(type="table", sid="P5.2", h2="What it's designed to check", light=True, cols=("Item", "What it looks for"), rows=[
            ("Gloves", "Gloves on both hands"), ("Mask", "Mask worn over nose and mouth"), ("Shoe covers", "Shoe covers on both feet"),
            ("Gown or coverall", "The right gown is worn"), ("Dress code", "Your site's rules, such as hair covers or goggles")]),
        dict(type="tiles", sid="P5.3", h2="Where it fits", items=[
            ("Pharma and drug-research cleanrooms", "Gowning rooms and airlocks before entry to a clean zone. {Pharma and healthcare|/industries/pharma-healthcare}"),
            ("Hospitals", "Surgical teams' PPE before entering the operating theatre."),
            ("Other sites, as custom projects", "Supermarkets and retail ({Retail and malls|/industries/retail}) and factories ({Manufacturing|/industries/manufacturing}).")]),
        dict(type="tiles", sid="P5.4", h2="How it's designed to work", numbered=True, items=[
            ("Uses your existing CCTV", "Standard IP CCTV cameras (RTSP). No new cameras needed."), ("Runs on-site", "A small edge computer sits next to your CCTV system, so video stays on your premises."),
            ("Alerts your team", "On a dashboard on screen and by email. WhatsApp alerts are planned."), ("Optional cloud dashboard", "Alerts and compliance summaries, not raw video.")]),
        dict(type="text", sid="P5.5", h2="Your video stays on your premises", light=True, paras=["The system is designed so video is processed on-site, on the edge computer, and not sent to the cloud. The cloud dashboard is optional and shows alerts and compliance summaries, not raw video."]),
        dict(type="split", sid="P5.6", h2="See the prototype", media="vision", paras=["An illustration of how the system marks each person and checks their gowning.", "Labels are real text around the video, never burned into it."]),
        dict(type="text", sid="P5.7", h2="Become a pilot partner", paras=["We're looking for a small number of pharma sites, labs and hospitals to test the prototype with us. A pilot partner gives us a real gowning area to test in and honest feedback, and helps shape the product.", "Pilot terms are agreed per site, so talk to us."],
             ctas=[("Become a pilot partner", "/contact?topic=ai-vision")]),
        dict(type="faq", sid="P5.8", h2="Questions about AI gowning and PPE compliance", light=True, items=[
            ("Is Cybertronix AI vision available to buy?", "Not yet. It's a working prototype, and we're looking for pilot partners to test it in real gowning areas."),
            ("Does it work with my existing CCTV cameras?", "Yes. It's designed to work with standard IP CCTV cameras (RTSP)."),
            ("Where is the video processed?", "On your site. It's designed to run on a small edge computer next to your CCTV, so video stays on your premises. A cloud dashboard is optional."),
            ("How are alerts sent?", "On an on-screen dashboard and by email. WhatsApp alerts are planned."),
            ("Can it check other things besides gowning and PPE?", "Yes, as a custom project, for example in supermarkets, retail and factories. {Tell us your requirement|/contact?topic=ai-vision}.")]),
        dict(type="cta", sid="P5.9", h2="Talk to us", intro="Pharma site, lab or hospital? Help us test the prototype.", ctas=[("Become a pilot partner", "/contact?topic=ai-vision"), ("Pharma and healthcare", "/industries/pharma-healthcare")]),
    ]))

PAGES.append(dict(id="P6", name="About", file="P6-About", eyebrow="Robotics engineering · Jubilee Hills, Hyderabad",
    h1="About Cybertronix",
    lead="Cybertronix is a robotics engineering company in Jubilee Hills, Hyderabad. We're building our own products, and we take on custom robot and computer-vision projects for clients.",
    ctas=[(REQ, "/contact")], media=None,
    sections=[
        dict(type="table", sid="P6.2", h2="What we're building", cols=("Product", "Status"), rows=[
            ("{AI vision|/ai-vision} for gowning and PPE compliance on existing CCTV", PROTO), ("{Floor-cleaning robot|/cleaning-robot} for offices and malls", "In development"),
            ("{Custom humanoid robots|/humanoid-robots}", "Built to order"), ("{Custom robotic arms|/robotic-arm}", "Built to order")]),
        dict(type="text", sid="P6.3", h2="Product-first, open to projects", paras=["We want to be a product company: we build our own systems and improve them with pilot partners. We also take on client projects when our engineering fits the problem."]),
        dict(type="table", sid="P6.4", h2="Our engineering team", light=True, cols=("Discipline", "What they do"), rows=TEAM4, ctas=[("Meet the team", "/team")]),
        dict(type="tiles", sid="P6.5", h2="How we work", items=[
            ("Honest about status", "We say clearly what's a prototype, what's in development and what we build to order."),
            ("Requirement first", "We start from your problem, not from a product we need to sell."),
            ("One team, start to finish", "The engineers who design a system build it and support it.")]),
        dict(type="split", sid="P6.6", h2="Our base in Hyderabad", media="lab", paras=["We work from Rd No. 10C, Gayatri Hills, Jubilee Hills, Hyderabad.", f"What happens there and visits: {F}"]),
        dict(type="faq", sid="P6.7", h2="Questions about Cybertronix", light=True, items=[
            ("Where is Cybertronix based?", "In Jubilee Hills, Hyderabad, Telangana. See the {contact page|/contact}."),
            ("Is Cybertronix a product company or a services company?", "Product first. We're building our own AI vision system and cleaning robot, and we also take on client projects."),
            ("What kind of engineers work at Cybertronix?", "AI, mechatronics, mechanical and electronics engineers, all in-house. {Meet the team|/team}."),
            ("Do you take on custom projects?", "Yes. Custom robots and computer-vision systems built to your requirement."),
            ("Is Cybertronix related to Cybertronix Technologies LLC in Dubai?", F)]),
        dict(type="cta", sid="P6.8", h2="Talk to us", intro="Tell us what you want to check, clean or build.", ctas=[(REQ, "/contact")]),
    ]))

PAGES.append(dict(id="P7", name="Contact", file="P7-Contact", eyebrow="Jubilee Hills, Hyderabad",
    h1="Contact Cybertronix in Hyderabad",
    lead="Join a pilot, ask about a custom build or just ask a question. An engineer on our team will reply.",
    ctas=[], media=None,
    sections=[
        dict(type="contact", sid="P7.2", h2=REQ, intro="The topic is pre-selected from the page you came from."),
        dict(type="split", sid="P7.3–P7.5", h2="Visit, call or email", media="map", paras=[
            "Cybertronix, Rd No. 10C, Gayatri Hills, Jubilee Hills, Hyderabad, Telangana 500033. Please book a visit before you come.",
            "Phone: {+91 90598 97807|tel:+919059897807}", "Email: {info@cybertronix.com|mailto:info@cybertronix.com}",
            f"WhatsApp: {F}", f"Opening hours: {F} (hidden until confirmed)"]),
        dict(type="faq", sid="P7.6", h2="Questions before you get in touch", light=True, items=[
            ("Where is your Hyderabad office?", "Rd No. 10C, Gayatri Hills, Jubilee Hills, Hyderabad."),
            ("Can I visit without an appointment?", "Please call or email first so the right engineer is free to meet you."),
            ("How do I join a pilot?", "Choose \"AI vision pilot\" or \"Cleaning robot pilot\" in the form and tell us about your site."),
            ("Do you work with clients outside Hyderabad?", F),
            ("Can I get a quote by email?", "Yes. Tell us your requirement and we'll send a quote. Every quote is on request.")]),
    ]))

PAGES.append(dict(id="P8", name="Manufacturing", file="P8-Manufacturing", eyebrow="Industries · Manufacturing",
    h1="Custom robots and computer vision for Hyderabad factories",
    lead="Have a task a standard machine doesn't fit? Our engineers design and build a robot or vision system around it.",
    ctas=[(REQ, "/contact?topic=robotic-arm")], media="factory",
    sections=[
        dict(type="bullets", sid="P8.2", h2="Problems we can help with", items=["Repetitive tasks that tire people out and cause mistakes", "Safety or PPE rules that are hard to check on every shift", "Tasks a standard robot doesn't fit"]),
        dict(type="tiles", sid="P8.3–P8.4", h2="What we can build for you", items=[
            ("Custom robotic arms · Built to order", "We design and build a {robotic arm|/robotic-arm} for your task, matched to your part and your space."),
            ("Computer vision on your existing CCTV · Custom project", "Our {AI vision|/ai-vision} prototype checks PPE on existing CCTV. For factories, we can adapt it to your safety or quality checks, designed to run on-site so video stays in your plant.")]),
        dict(type="tiles", sid="P8.5", h2="How a project starts", numbered=True, items=[
            ("Site visit", "We see your floor, cameras and the task."), ("Feasibility", "We tell you honestly what's possible."), ("Design and quote", "Quotes are on request.")]),
        dict(type="faq", sid="P8.6", h2="Questions", light=True, items=[
            ("Where should a factory start with automation?", "With one task you can measure every shift. We'll help you pick it on a site visit."),
            ("Can you build a robot for one specific task?", "Yes. We design and build custom robotic arms to your requirement."),
            ("Do I need new cameras for vision checks?", "No. Our vision system is designed to use your existing CCTV."),
            ("How much does it cost?", "It depends on the task. We quote on request."), ("Do you work outside Telangana?", F)]),
        dict(type="cta", sid="P8.7", h2=REQ, intro="Tell us about one task on your floor.", ctas=[(REQ, "/contact"), ("Custom robotic arms", "/robotic-arm")]),
    ]))

PAGES.append(dict(id="P9", name="Pharma & healthcare", file="P9-Pharma", eyebrow="Industries · Pharma and healthcare", status=PROTO,
    h1="AI gowning checks for pharma cleanrooms and operating theatres",
    lead="Gowning mistakes are easy to make and hard to spot on a busy shift. Our AI vision prototype is designed to check every person's gowning on your existing CCTV, before they enter a clean zone or theatre.",
    ctas=[("Become a pilot partner", "/contact?topic=ai-vision")], media=None,
    sections=[
        dict(type="text", sid="P9.2", h2="Built next to India's pharma hub", paras=["Hyderabad is home to many pharma and life-sciences companies. We're a Hyderabad engineering team building this system for exactly these sites, so we can visit, test and improve it with you in person."]),
        dict(type="bullets", sid="P9.3", h2="Pharma and drug-research cleanrooms", intro="At gowning rooms and airlocks, the system is designed to check:", items=[
            "Gloves, mask, shoe covers and gown or coverall", "Your own dress-code rules, such as hair covers or goggles", "And to alert the supervisor when something is missing"],
             after="It is designed to support your gowning checks and records, not to replace your quality team."),
        dict(type="text", sid="P9.4", h2="Hospitals and operating theatres", paras=["Before a surgical team enters the theatre, the system is designed to check masks, gloves, gowns and shoe covers, and to flag a miss on the dashboard."]),
        dict(type="text", sid="P9.5", h2="Video stays on your premises", light=True, paras=["The system is designed to run on a small edge computer next to your CCTV, so video is processed on-site. Alerts appear on a dashboard and by email. A cloud dashboard is optional."]),
        dict(type="faq", sid="P9.6", h2="Questions", light=True, items=[
            ("Is this system in use at pharma sites today?", "Not yet. It's a prototype. We're looking for pilot partners to test it in real gowning areas."),
            ("Does it make my site GMP-compliant?", "No system can do that on its own. It's designed to support your gowning checks by flagging misses as they happen. Your quality processes stay in charge."),
            ("Does it need new cameras?", "No. It's designed to use your existing CCTV."),
            ("Does video leave our site?", "It's designed so video is processed on-site. A cloud dashboard is optional."),
            ("How do we join the pilot?", "{Register your interest|/contact?topic=ai-vision} and tell us about your site. Pilot terms are agreed per site.")]),
        dict(type="cta", sid="P9.7", h2="Become a pilot partner", intro="A real gowning area and honest feedback help shape the product.", ctas=[("Become a pilot partner", "/contact?topic=ai-vision"), ("How AI vision works", "/ai-vision")]),
    ]))

PAGES.append(dict(id="P10", name="Team", file="P10-Team", eyebrow="In-house engineers · Hyderabad",
    h1="The Cybertronix team",
    lead="One in-house team of engineers in Hyderabad. The people who design our systems are the people who build them.",
    ctas=[(REQ, "/contact")], media=None,
    sections=[
        dict(type="table", sid="P10.2", h2="What our engineers do", cols=("Discipline", "What they work on"), rows=[
            ("AI engineering", "Computer vision, machine learning and the software behind AI vision"), ("Mechatronics", "Motors, sensors and control systems that make robots move safely"),
            ("Mechanical", "Frames, joints, grippers and enclosures"), ("Electronics", "Circuit boards, power and wiring")]),
        dict(type="people", sid="P10.3", h2="People", intro="Names and photos added by the founder (D27). Cards without a name are hidden on the site. Never fake faces or names."),
        dict(type="bullets", sid="P10.4", h2="How we work together", light=True, items=[
            "One team, start to finish: design, build and testing happen in-house.", "Honest about status: we say clearly what's a prototype, what's in development and what we build to order.", "Requirement first: we start from your problem."]),
        dict(type="text", sid="P10.5", h2="Join us", paras=[f"Hiring? {F} If not, this section is removed."]),
        dict(type="faq", sid="P10.6", h2="Questions", light=True, items=[
            ("Where does the team work?", "At our base in Jubilee Hills, Hyderabad."), ("Does Cybertronix outsource engineering?", F),
            ("Can I meet the engineers before a project?", f"Yes. {{Get in touch|/contact}} and we'll set up a meeting. {F}")]),
        dict(type="cta", sid="P10.7", h2=REQ, intro="Meet the engineers who would build it.", ctas=[(REQ, "/contact"), ("About Cybertronix", "/about")]),
    ]))

PAGES.append(dict(id="P11", name="Retail & malls", file="P11-Retail", eyebrow="Industries · Retail and malls",
    h1="AI vision and robots for supermarkets and malls",
    lead="Have a store problem you'd like a camera to solve? Our engineers build custom computer vision on your existing CCTV. Our floor-cleaning robot for malls is also in development.",
    ctas=[(REQ, "/contact?topic=ai-vision")], media=None,
    sections=[
        dict(type="bullets", sid="P11.2", h2="Custom AI vision for supermarkets and retail", status="Custom project",
             intro="Our AI team can build a vision system around your question, using the cameras you already have. Examples of what we could build for:", items=[
            "Spotting empty shelves", "Noticing long checkout queues", "Checking staff dress code or hygiene rules in food areas"],
             after="It's designed to run on-site, next to your CCTV, so video stays in your store."),
        dict(type="split", sid="P11.3", h2="Floor-cleaning robot for malls", status=DEV, media="cleaning", paras=[
            "We're building an autonomous {floor-cleaning robot|/cleaning-robot} for offices and malls. If you run a mall, you can help test it as a pilot partner."],
             ctas=[("Become a pilot partner", "/contact?topic=cleaning-pilot")]),
        dict(type="faq", sid="P11.4", h2="Questions", light=True, items=[
            ("Do you have a ready-made retail analytics product?", "No. For retail we build custom computer vision to your requirement."),
            ("Does it need new cameras?", "No. It's designed to use your existing CCTV."),
            ("Can our mall test the cleaning robot?", "Yes, you can register as a pilot partner. It's in development and not on sale yet."),
            ("How much does it cost?", "We quote on request."), ("Where are you based?", "In Jubilee Hills, Hyderabad. See the {contact page|/contact}.")]),
        dict(type="cta", sid="P11.5", h2=REQ, intro="Tell us the question you'd like your cameras to answer.", ctas=[(REQ, "/contact"), ("AI vision", "/ai-vision")]),
    ]))
