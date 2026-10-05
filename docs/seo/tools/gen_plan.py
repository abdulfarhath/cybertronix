# Regenerates docs/seo/page-plan.md from content/P*.md front matter and headings, and checks title/meta lengths and internal links.
# Run from the repo root: python3 docs/seo/tools/gen_plan.py
import re,glob
out=["# Page plan (brand first, D41–D43)","","Owner: SEO Content · Updated 2026-10-03 · Keywords: `docs/seo/keywords.md` · Text: `content/`","",
"Generated from the front matter and headings in `content/`. If the two ever differ, `content/` wins.","",
"## Rules for every page (Build)","| Rule | Detail |","|---|---|",
"| Brand first (D41) | The **H1 is written for people**, not keywords. The keyword goes in the **eyebrow** (a small `<p class=\"eyebrow\">` above the H1, never a heading), title, meta, URL, alt, schema and the first paragraph. |",
"| Market (D42, D43) | Global, with Hyderabad as the base and local SEO anchor. Titles keep \"Hyderabad\" where they target local searches. |",
"| Domain | **https://cybertronix.tech** (D15). Canonicals, sitemap, Organization `url` and `sameAs` all point there. Keep the host (www or not) the same as the live site today. |",
"| Status labels (D21, D30) | AI vision = **Prototype · pilot partners welcome** · Cleaning robot = **In development** (pilot partners welcome) · Humanoid + arm = **Built to order** · Retail/factory vision = **Custom project** · Raqib = **Early build**. Nothing is \"available now\". |",
"| Wording (D23) | AI vision features are always \"designed to\", never \"deployed\", \"used by\" or \"trusted by\". Cameras: \"standard IP CCTV cameras (RTSP)\" (D29). |",
"| Clients (D26) | None anywhere. No logos, case studies or \"used by\". Never mention T-Hub or any incubator. |",
"| Schema | P2/P3/P5/P8/P9/P11 use `Service`, never `Product`. P4 has no `Product`. P13 uses `SoftwareApplication` with no `offers`, `operatingSystem` or ratings until confirmed. No `foundingDate` anywhere (D19). `LocalBusiness` NAP exactly as P7 (D25, no PIN yet, D29). |",
"| Prices | None anywhere (D18). Use \"we quote on request\". |",
"| Year | Never show the founding year or company age (D19). |",
"| Stock footage | Mood only (D20). Alt text describes the scene. The vision demo is labelled \"Illustration\". |",
"| Team (D27) | Grey \"Photo coming soon\" cards. Hide any card with no real name. |",
"| Software (D31) | Placeholder cards say only \"Details coming soon\". Raqib copy describes only the reference screenshot. Don't publish the raw screenshot (it shows a username and hostname). |",
"| Title / meta | Title ≤ 60 chars, meta ≤ 155. Counts in brackets are checked by script. |",
"| FAQ | Visible on the page **and** in `FAQPage` JSON-LD with the same words. Hide any FAQ whose answer is still `TODO(founder)`. |",
"| Unknown facts | `TODO(founder)` stays in `content/` and is never shipped live. |",""]
names={'P1':'Home','P2':'Humanoid robot development','P3':'Custom robotic arms','P4':'Cleaning robot (in development)','P5':'AI vision (prototype)','P6':'About','P7':'Contact','P8':'Manufacturing','P9':'Pharma & healthcare','P10':'Team','P11':'Retail & malls','P12':'Software & projects','P13':'Raqib (early build)'}
bad=[]
for f in sorted(glob.glob('content/P*.md'),key=lambda x:int(re.search(r'P(\d+)',x).group(1))):
    s=open(f).read(); g=lambda k: re.search(rf'^{k}: (.*)$',s,re.M).group(1).strip('"')
    pid=g('id'); t=g('title'); d=g('description')
    if len(t)>60 or len(d)>155: bad.append(pid)
    out+=["---","",f"## {pid} · {names[pid]} `{g('url')}`","| Field | Value |","|---|---|",
          f"| Keyword | {g('keyword')} |",f"| Title | {t} [{len(t)}] |",f"| Meta | {d} [{len(d)}] |",f"| Eyebrow | {g('eyebrow')} |",f"| H1 | {g('h1')} |",
          f"| Schema | {', '.join('`'+x.strip()+'`' for x in g('schema').strip('[]').split(','))}, plus site-wide `Organization` |",""]
    h2=[re.sub(r'^## P\d+\.\d+ ','',l) for l in s.splitlines() if l.startswith('## ')]
    out+=["**H2 outline:** "+" · ".join(h2),""]
    faq=[l[4:] for l in s.splitlines() if l.startswith('### ')]
    out+=["**FAQ:**"]+[f"{i}. {q}" for i,q in enumerate(faq,1)]+[""]
    links=sorted(set(re.findall(r'(?:\]\(|→ )(/[a-z\-/]*)',s))-{g('url')})
    out+=["**Internal links:** "+" · ".join(f"`{l}`" for l in links),""]
out+=["---","","## Site-wide","| Item | Plan |","|---|---|",
"| Nav | AI vision · Cleaning robot · Custom robots (humanoid, arm) · Industries (Pharma & healthcare, Retail & malls, Manufacturing) · Software · About · Team · Contact (button: Tell us your requirement) |",
"| Mission / vision | Exactly as D42, on P1 (sections 2–3) and P6 (section 2). Organization `slogan` = mission. |",
"| Footer | NAP exactly as P7 (D25), page links, social links (`sameAs`, `TODO(founder)`) |",
"| Blog | Later. Honest topics with real demand: \"cleanroom gowning steps and common mistakes\", \"why process CCTV video on-site\", \"how to check VRAM usage when running local LLMs\". |"]
open('docs/seo/page-plan.md','w').write("\n".join(out)+"\n")
urls={re.search(r'^url: (.*)$',open(f).read(),re.M).group(1) for f in glob.glob('content/P*.md')}
for f in glob.glob('content/P*.md'):
    for l in set(re.findall(r'(?:\]\(|→ )(/[a-z\-/]*)',open(f).read())):
        if l not in urls: print("BROKEN",f,l)
print("length problems:",bad)
