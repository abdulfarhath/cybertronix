#!/usr/bin/env python3
"""Generate Cybertronix page boards (desktop 1440 + phone 390) from one component set."""
import json, os, html, re

ROOT = os.path.dirname(os.path.abspath(__file__)) + "/canvas/project"
B = {  # uploaded assets on the new canvas
    "hero_mp4": "/_blob/f1b9f45d7eda9b6684feb3a1124b6bbb", "hero_jpg": "/_blob/f1f5a5a534e610c1dbc900bc96d4da36",
    "arm_still": "/_blob/88f462b77fc9a102797adeefeeb17023", "factory": "/_blob/379f169d8bbd73bfc973c0cfcb7307eb",
    "arm_mp4": "/_blob/c966c99796922efb1d3543c7b8bd018a", "arm_jpg": "/_blob/7aa40f2db32d7770b19aeccb0881fab4",
    "arm_front": "/_blob/d59360b5b5ad4ba6dfbb88f1144cc02d", "arm_top": "/_blob/34d6fca0d4262f38154a8a99ca8b5605",
    "gripper": "/_blob/dd5ea2d30b9895602a72559f312cca2b", "vision_mp4": "/_blob/f1c07b2841bc266fb516623bd04e2f27",
}
e = html.escape

HELMET = """<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400;500;600&amp;family=Geist:wght@400;500&amp;family=JetBrains+Mono:wght@400;500&amp;display=swap" rel="stylesheet">
<style>
body{margin:0;background:#0A0C10;color:#E8ECF2;font-family:Geist,system-ui,sans-serif}
a{color:#8FB2FF}a:hover{color:#C4D6FF}
.lt a{color:#2457C8}.lt a:hover{color:#163C93}
.mono{font-family:'JetBrains Mono',monospace}
.disp{font-family:Unbounded,Geist,sans-serif}
.gd{background-color:#0A0C10;background-image:linear-gradient(rgba(143,178,255,0.06) 1px,transparent 1px),linear-gradient(90deg,rgba(143,178,255,0.06) 1px,transparent 1px);background-size:40px 40px}
.gl{background-color:#F3F5F8;background-image:linear-gradient(rgba(36,87,200,0.12) 1px,transparent 1px),linear-gradient(90deg,rgba(36,87,200,0.12) 1px,transparent 1px),linear-gradient(rgba(36,87,200,0.06) 1px,transparent 1px),linear-gradient(90deg,rgba(36,87,200,0.06) 1px,transparent 1px);background-size:120px 120px,120px 120px,24px 24px,24px 24px}
.ph{display:flex;align-items:center;justify-content:center;text-align:center;border:1px dashed #2E3846;background:#10141B;color:#8A94A4;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.5;padding:16px;box-sizing:border-box}
.todo{font-family:'JetBrains Mono',monospace;font-size:12px;padding:2px 8px;border:1px dashed currentColor;border-radius:6px;white-space:nowrap}
details>summary{list-style:none;cursor:pointer}details>summary::-webkit-details-marker{display:none}
</style>
</helmet>"""


def square(src):
    src = re.sub(r"border-radius: (?!50%)[^;\"]+", "border-radius: 0", src)
    src = re.sub(r"\b1px (solid|dashed)", r"2px \1", src)
    src = src.replace("border:1px dashed", "border:2px dashed").replace("border-radius:6px", "border-radius:0")
    return src


def doc(title, w, h, body):
    body = square(body)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{e(title)}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
{HELMET}
<div style="width: {w}px; min-height: {h}px; background: #0A0C10; display: flex; flex-direction: column">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
"""


def todo(text="TODO(founder)", light=False):
    c = "#B9530F" if light else "#FF8A3D"
    return f'<span class="todo" style="color: {c}">{e(text)}</span>'


def rich(s, light=False):
    """Inline markup: [[todo text]] -> todo chip, {link|href} -> link."""
    out, i = "", 0
    while i < len(s):
        if s.startswith("[[", i):
            j = s.index("]]", i)
            out += todo(s[i + 2:j], light); i = j + 2
        elif s[i] == "{":
            j = s.index("}", i); t, h = s[i + 1:j].split("|")
            out += f'<a href="{h}">{e(t)}</a>'; i = j + 1
        else:
            j = min([k for k in (s.find("[[", i), s.find("{", i)) if k != -1] or [len(s)])
            out += e(s[i:j]); i = j
    return out


# Cybertronix mark L4 "Head-turn" (D36), simple level, on dark. Same geometry as design/boards/logo.py m4.
LOGO = ('<svg width="{s}" height="{s}" viewBox="0 0 48 48" role="img" aria-label="Cybertronix logo">'
        '<rect x="6" y="6" width="36" height="6" fill="#E8ECF2"/><rect x="6" y="36" width="36" height="6" fill="#E8ECF2"/>'
        '<rect x="6" y="6" width="6" height="36" fill="#E8ECF2"/><rect x="36" y="6" width="6" height="8" fill="#E8ECF2"/>'
        '<rect x="36" y="34" width="6" height="8" fill="#E8ECF2"/><rect x="22" y="17" width="8" height="8" fill="#E8ECF2"/>'
        '<rect x="33" y="17" width="8" height="8" fill="#3D7BFF"/></svg>')
# 16 px pixel favicon (same rows as design/boards/export.py PIX16["cybertronix"]), on white
_FAV = ["................", ".##############.", ".##############.", ".##.........##..", ".##.........##..", ".##.............",
        ".##....##..@@...", ".##....##..@@...", ".##.............", ".##.............", ".##.............", ".##.........##..",
        ".##.........##..", ".##############.", ".##############.", "................"]
FAVICON = ('<svg width="16" height="16" viewBox="0 0 16 16" shape-rendering="crispEdges" aria-hidden="true"><rect width="16" height="16" fill="#FFFFFF"/>'
           + "".join(f'<rect x="{x}" y="{y}" width="1" height="1" fill="{"#0F141B" if ch == "#" else "#2457C8"}"/>'
                     for y, row in enumerate(_FAV) for x, ch in enumerate(row) if ch in "#@") + "</svg>")
def raqib_mark(sz, ink="#E8ECF2", mid="#8A94A4", acc="#3D7BFF"):
    """Raqib mark, option A "Panel + pulse" (D37), simple level. Same geometry as design/boards/raqib.py mark_a."""
    rr = lambda x, y, w, h, c: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>'
    return (f'<svg width="{sz}" height="{sz}" viewBox="0 0 48 48" role="img" aria-label="Raqib logo" style="flex-shrink: 0">'
            + rr(3, 3, 6, 4, ink) + rr(19, 3, 26, 4, ink) + rr(3, 3, 4, 42, ink) + rr(41, 3, 4, 42, ink) + rr(3, 41, 42, 4, ink)
            + f'<polyline points="9,18 16,18 19,12 23,24 26,18 39,18" fill="none" stroke="{ink}" stroke-width="3.5"/>'
            + rr(10, 28, 12, 9, mid) + rr(26, 28, 12, 9, acc) + "</svg>")


REPO = os.environ.get("CYX_REPO", "/home/user/cybertronix")


def page_title(pid):
    import glob
    for f in glob.glob(os.path.join(REPO, "content", f"{pid}-*.md")):
        m = re.search(r'^title: "(.*)"', open(f).read(), re.M)
        if m:
            return m.group(1)
    return "Cybertronix"


def tabstrip(p, m):
    urls = {"P1": "/", "P2": "/humanoid-robots", "P3": "/robotic-arm", "P4": "/cleaning-robot", "P5": "/ai-vision", "P6": "/about",
            "P7": "/contact", "P8": "/industries/manufacturing", "P9": "/industries/pharma-healthcare", "P10": "/team",
            "P11": "/industries/retail", "P12": "/software", "P13": "/software/raqib"}
    url = "cybertronix.tech" + urls.get(p["id"], "/")
    title = html.escape(page_title(p["id"]))
    w = "100%" if m else "280px"
    return (f'<div aria-hidden="true" style="height: 40px; display: flex; align-items: flex-end; gap: 12px; padding: 0 {"8" if m else "16"}px; background: #141A22; border-bottom: 2px solid #232B36">'
            f'<div style="display: flex; align-items: center; gap: 8px; height: 32px; padding: 0 12px; background: #0A0C10; max-width: {w}; min-width: 0">{FAVICON}'
            f'<span style="font-size: 12px; color: #B7C0CD; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{title}</span></div>'
            + ("" if m else f'<span class="mono" style="margin: 0 0 8px auto; font-size: 11px; color: #8A94A4">{url}</span>') + '</div>')
NAV = [("AI vision", "/ai-vision", ("P5",)), ("Cleaning robot", "/cleaning-robot", ("P4",)), ("Custom robots ▾", "/humanoid-robots", ("P2", "P3")),
       ("Industries ▾", "/industries/pharma-healthcare", ("P8", "P9", "P11")), ("Software", "/software", ("P12", "P13")), ("About", "/about", ("P6",)), ("Team", "/team", ("P10",)), ("Contact", "/contact", ("P7",))]
PRODUCTS = [("AI vision", "/ai-vision"), ("Cleaning robot", "/cleaning-robot"), ("Custom humanoid robots", "/humanoid-robots"), ("Custom robotic arms", "/robotic-arm")]
INDUSTRIES = [("Pharma and healthcare", "/industries/pharma-healthcare"), ("Retail and malls", "/industries/retail"), ("Manufacturing", "/industries/manufacturing")]


def btn(text, href, primary=True, m=False):
    pad = "16px" if m else "16px 26px"
    extra = "text-align: center; " if m else ""
    if primary:
        return f'<a href="{href}" style="{extra}padding: {pad}; background: #2F66E0; color: #FFFFFF; border-radius: 999px; text-decoration: none; font-size: 15px; font-weight: 500">{e(text)}</a>'
    return f'<a href="{href}" style="{extra}padding: {pad}; border: 1px solid #2E3846; color: #E8ECF2; border-radius: 999px; text-decoration: none; font-size: 15px">{e(text)}</a>'


def nav(active, m):
    if m:
        return f"""<nav aria-label="Main" style="height: 72px; padding: 0 20px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #1A212B; background: #0A0C10">
<a href="/" style="display: flex; align-items: center; gap: 10px; text-decoration: none; color: #E8ECF2">{LOGO.format(s=30)}<span class="disp" style="font-size: 16px; font-weight: 600; letter-spacing: -0.02em">cybertronix</span></a>
<div style="display: flex; gap: 8px; align-items: center">
<a href="/contact" style="padding: 12px 16px; background: #2F66E0; color: #FFFFFF; border-radius: 999px; text-decoration: none; font-size: 13px; font-weight: 500">Contact us</a>
<button type="button" aria-label="Open menu" style="width: 44px; height: 44px; border-radius: 50%; border: 1px solid #2E3846; background: transparent; display: flex; align-items: center; justify-content: center; padding: 0"><svg width="18" height="14" viewBox="0 0 18 14" aria-hidden="true"><path d="M1 1 H17 M1 7 H17 M1 13 H17" stroke="#E8ECF2" stroke-width="2" stroke-linecap="round"/></svg></button>
</div>
</nav>"""
    links = ""
    for t, h, pids in NAV:
        on = active in pids
        style = "background: #232B36; color: #E8ECF2" if on else "color: #B7C0CD"
        cur = ' aria-current="page"' if on else ""
        links += f'<a href="{h}"{cur} style="padding: 12px 11px; border-radius: 999px; {style}; text-decoration: none; font-size: 14px; white-space: nowrap">{t}</a>\n'
    return f"""<nav aria-label="Main" style="height: 104px; padding: 0 80px; display: flex; align-items: center; justify-content: space-between; background: #0A0C10">
<a href="/" style="display: flex; align-items: center; gap: 12px; text-decoration: none; color: #E8ECF2">{LOGO.format(s=36)}<span class="disp" style="font-size: 19px; font-weight: 600; letter-spacing: -0.02em">cybertronix</span></a>
<div style="display: flex; gap: 2px; padding: 6px; background: #141A22; border: 1px solid #232B36; border-radius: 999px">
{links}</div>
<a href="/contact" style="padding: 14px 22px; background: #2F66E0; color: #FFFFFF; border-radius: 999px; text-decoration: none; font-size: 14px; font-weight: 500; white-space: nowrap">Tell us your requirement</a>
</nav>"""


def crumbs(name, m):
    pad = "0 20px" if m else "0 80px"
    return f'<nav aria-label="Breadcrumb" class="mono" style="padding: {pad}; font-size: 12px; color: #8A94A4; display: flex; gap: 8px"><a href="/" style="color: #8A94A4">Home</a><span aria-hidden="true">/</span><span aria-current="page" style="color: #B7C0CD">{e(name)}</span></nav>'


def media(kind, m, h):
    r = "20px" if m else "28px"
    chip = lambda t: f'<div class="mono" style="position: absolute; top: 16px; left: 16px; padding: 6px 12px; border: 1px solid #2E3846; border-radius: 999px; background: #0A0C10; font-size: 11px; color: #B7C0CD">{e(t)}</div>'
    grad = '<div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(10,12,16,0.92) 0%, rgba(10,12,16,0.35) 40%, rgba(10,12,16,0.1) 100%)"></div>'
    wrap = lambda inner: f'<div style="position: relative; height: {h}px; border-radius: {r}; overflow: hidden; border: 1px solid #232B36">{inner}</div>'
    play = '<button type="button" aria-label="Play video" style="position: absolute; left: 16px; bottom: 16px; width: 44px; height: 44px; border-radius: 50%; border: none; background: #2F66E0; display: flex; align-items: center; justify-content: center; padding: 0"><svg width="14" height="16" viewBox="0 0 14 16" aria-hidden="true"><path d="M1 1 L13 8 L1 15 Z" fill="#FFFFFF"/></svg></button>'
    if kind == "home":
        if m:
            return wrap(f'<img src="{B["hero_jpg"]}" alt="Robotic arm in a lab (stock footage)" style="display:block;width:100%;height:100%;object-fit:cover">{grad}{chip("Poster on phone · illustrative footage")}')
        return wrap(f'<video src="{B["hero_mp4"]}" poster="{B["hero_jpg"]}" muted loop playsinline aria-label="Robotic arm in a lab (stock footage)" style="display:block;width:100%;height:100%;object-fit:cover"></video>{grad}{chip("Illustrative footage · head-turn frames replace this")}' + play.replace("Play video", "Pause hero video"))
    if kind == "humanoid":
        return f'<div class="ph" style="height: {h}px; border-radius: {r}; flex-direction: column; gap: 10px">[Humanoid render or concept drawing]<span>TODO(founder): real image (F8). Not a stock photo of another company\'s robot.</span></div>'
    if kind == "arm":
        return wrap(f'<img src="{B["arm_jpg"]}" alt="Robotic arm moving parts in a lab (stock footage)" style="display:block;width:100%;height:100%;object-fit:cover">{grad}{chip("Illustrative footage")}{"" if m else play}')
    if kind == "cleaning":
        return f'<div style="height: {h}px; border-radius: {r}; overflow: hidden; border: 1px solid #232B36; position: relative"><svg viewBox="0 0 300 300" width="100%" height="{h}" preserveAspectRatio="xMidYMid slice" style="display: block" role="img" aria-label="Cleaning robot, side view (drawing)"><defs><linearGradient id="cbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#171D27"/><stop offset="1" stop-color="#0C0F14"/></linearGradient><linearGradient id="cbody" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2E3846"/><stop offset="1" stop-color="#141A22"/></linearGradient></defs><rect width="300" height="300" fill="url(#cbg)"/><ellipse cx="150" cy="238" rx="120" ry="12" fill="#05070A" opacity="0.8"/><rect x="118" y="112" width="64" height="40" rx="10" fill="#1E2530" stroke="#3A4452"/><rect x="132" y="98" width="36" height="18" rx="9" fill="#0B0E13" stroke="#3D7BFF"/><rect x="40" y="150" width="220" height="70" rx="35" fill="url(#cbody)" stroke="#3A4452" stroke-width="2"/><path d="M60 196 L240 196" stroke="#3D7BFF" stroke-width="3" stroke-linecap="round"/><circle cx="90" cy="222" r="16" fill="#0B0E13" stroke="#2E3846" stroke-width="4"/><circle cx="210" cy="222" r="16" fill="#0B0E13" stroke="#2E3846" stroke-width="4"/><path d="M52 162 C120 150 180 150 248 162" fill="none" stroke="#8FB2FF" stroke-opacity="0.5" stroke-width="2"/></svg>{chip("Drawing · in development")}</div>'
    if kind == "vision":
        return vision_demo(m, h)
    if kind == "factory":
        return wrap(f'<img src="{B["factory"]}" alt="Factory floor (stock photo)" style="display:block;width:100%;height:100%;object-fit:cover">{grad}{chip("Illustrative photo")}')
    if kind == "lab":
        return f'<div class="ph" style="height: {h}px; border-radius: {r}">[Photo of the Hyderabad lab]<br>TODO(founder) (F8)</div>'
    if kind == "map":
        return f'<div class="ph" style="height: {h}px; border-radius: {r}; flex-direction: column; gap: 10px">[Google Map, lazy-loaded after click]<span>Rd No. 10C, Gayatri Hills, Jubilee Hills · Get directions</span></div>'
    if kind == "raqib":
        rows = "".join(f'<div style="display: flex; justify-content: space-between"><span>{n}</span><span style="color: #B7C0CD">{v}</span></div>' for n, v in [("Isolated Web Co", "1.2 GB"), ("firefox", "904 MB"), ("brave", "700 MB")])
        b = lambda p, c: f'<div style="flex: 1; height: 8px; background: #1A212B; border-radius: 2px; overflow: hidden"><div style="width: {p}%; height: 100%; background: {c}"></div></div>'
        return f'''<figure class="mono" style="margin: 0; height: {h}px; box-sizing: border-box; background: #0D1016; border: 1px solid #232B36; border-radius: {r}; padding: {16 if m else 24}px; display: flex; flex-direction: column; gap: 14px; font-size: {11 if m else 13}px; color: #E8ECF2; overflow: hidden">
<div style="display: flex; align-items: center; gap: 10px; color: #8A94A4">{raqib_mark(22)}<b style="color: #E8ECF2">raqib</b> · 0 workloads · web <span style="color: #8FB2FF">localhost:7070</span></div>
<div style="display: flex; align-items: center; gap: 10px"><span style="width: 48px; color: #8A94A4">RAM</span>{b(69, "#B7C0CD")}<span>69%</span></div>
<div style="display: flex; align-items: center; gap: 10px"><span style="width: 48px; color: #8A94A4">VRAM</span>{b(18, "#B7C0CD")}<span>18%</span></div>
<div style="color: #8A94A4">CPU load 1.09 1.46 1.48 · cpus 12</div>
<div style="border: 1px solid #2E3846; border-radius: 6px; padding: 10px 12px; display: flex; flex-direction: column; gap: 4px"><span style="color: #8A94A4">Top by RAM</span>{rows}</div>
<div style="margin-top: auto; color: #B7C0CD"><span style="color: #8FB2FF">q</span> quit · <span style="color: #8FB2FF">j/k</span> select · <span style="color: #8FB2FF">k</span> kill (confirm) · <span style="color: #8FB2FF">?</span> help</div>
<figcaption style="color: #8A94A4">Raqib terminal app · sample data</figcaption>
</figure>'''
    raise KeyError(kind)


def vision_demo(m, h):
    vh = 200 if m else h - 190
    boxes = "" if m else """<div style="position: absolute; left: 8%; top: 28%; width: 32%; height: 58%; border: 2px solid #E8ECF2; border-radius: 4px"><span class="mono" style="position: absolute; top: -26px; left: -2px; padding: 3px 8px; background: #E8ECF2; color: #0A0C10; font-size: 12px; white-space: nowrap">Gowning area (example)</span></div>
<div style="position: absolute; left: 58%; top: 22%; width: 20%; height: 64%; border: 2px solid #FF8A3D; border-radius: 4px"><span class="mono" style="position: absolute; top: -26px; left: -2px; padding: 3px 8px; background: #FF8A3D; color: #0A0C10; font-size: 12px; white-space: nowrap">Clean-zone door</span></div>"""
    if m:
        boxes = '<div style="position: absolute; left: 30px; top: 50px; width: 140px; height: 110px; border: 2px solid #E8ECF2; border-radius: 4px"></div>'
    return f"""<figure style="margin: 0; background: #141A22; border: 1px solid #232B36; border-radius: {16 if m else 24}px; overflow: hidden">
<div style="display: flex; justify-content: space-between; align-items: center; padding: 14px 18px; border-bottom: 1px solid #232B36"><div class="mono" style="font-size: 13px">CAM-04 · illustration</div><div class="mono" style="font-size: 12px; color: #8A94A4">Detection replay</div></div>
<div style="position: relative; height: {vh}px">
<video src="{B['vision_mp4']}" poster="{B['arm_top']}" muted loop playsinline aria-label="Robot cell with detection boxes (sample footage)" style="display:block;position:absolute;inset:0;width:100%;height:100%;object-fit:cover"></video>
{boxes}
<button type="button" aria-label="Play demo" style="position: absolute; left: 16px; bottom: 16px; width: 44px; height: 44px; border-radius: 50%; border: none; background: #2F66E0; display: flex; align-items: center; justify-content: center; padding: 0"><svg width="14" height="16" viewBox="0 0 14 16" aria-hidden="true"><path d="M1 1 L13 8 L1 15 Z" fill="#FFFFFF"/></svg></button>
</div>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); border-top: 1px solid #232B36">
<div style="padding: 14px 18px; border-right: 1px solid #232B36"><div style="font-size: 12px; color: #8A94A4">Gloves</div><div class="mono" style="font-size: 14px; margin-top: 4px; color: #E8ECF2">on</div></div>
<div style="padding: 14px 18px; border-right: 1px solid #232B36"><div style="font-size: 12px; color: #8A94A4">Mask</div><div class="mono" style="font-size: 14px; margin-top: 4px; color: #E8ECF2">on</div></div>
<div style="padding: 14px 18px"><div style="font-size: 12px; color: #8A94A4">Shoe covers</div><div class="mono" style="font-size: 14px; margin-top: 4px; color: #FF8A3D">missing</div></div>
</div>
<figcaption style="padding: 12px 18px; border-top: 1px solid #232B36; font-size: 13px; color: #8A94A4">Illustration on stock footage: how the prototype is designed to mark each person and check gowning. Real gowning-room footage: <span class="todo" style="color: #FF8A3D">TODO(founder)</span></figcaption>
</figure>"""


# ---------- sections ----------

def hero(p, m):
    eyebrow = f'<div class="mono" style="display: flex; align-items: center; gap: 10px; font-size: {12 if m else 13}px; color: #8A94A4"><span style="width: 8px; height: 8px; border-radius: 50%; background: {"#8A94A4"}"></span>{e(p["eyebrow"])}</div>'
    if p.get("status"):
        eyebrow += f'<div><span class="mono" style="display: inline-block; padding: 8px 14px; border: 1px solid #2E3846; border-radius: 999px; font-size: 12px; color: #E8ECF2; background: #141A22">{e(p["status"])}</span></div>'
    h1 = f'<h1 class="disp" style="margin: 0; font-size: {34 if m else (60 if p["id"] == "P1" else 52)}px; line-height: 1.1; font-weight: 500; letter-spacing: -0.01em">{e(p["h1"])}</h1>'
    lead = f'<p style="margin: 0; font-size: {16 if m else 19}px; line-height: 1.6; color: #B7C0CD; max-width: 560px">{rich(p["lead"])}</p>'
    ctas = "".join(btn(t, h, i == 0, m) for i, (t, h) in enumerate(p["ctas"]))
    ctas = f'<div style="display: flex; {"flex-direction: column; gap: 10px" if m else "gap: 12px"}">{ctas}</div>'
    cr = crumbs(p["name"], m) if p["id"] != "P1" else ""
    if not p.get("media"):
        if m:
            return f'<section class="gd" style="padding: 24px 20px 48px; display: flex; flex-direction: column; gap: 20px; border-bottom: 1px solid #1A212B">{cr.replace("padding: 0 20px", "padding: 0")}{eyebrow}{h1}{lead}{ctas}</section>'
        return f'<section class="gd" style="padding: 24px 80px 96px; display: flex; flex-direction: column; gap: 28px; border-bottom: 1px solid #1A212B">{cr.replace("padding: 0 80px", "padding: 0")}<div style="display: flex; flex-direction: column; gap: 28px; max-width: 820px; padding-top: 48px">{eyebrow}{h1}{lead}{ctas}</div></section>'
    if m:
        return f'<section class="gd" style="padding: 24px 20px 48px; display: flex; flex-direction: column; gap: 20px; border-bottom: 1px solid #1A212B">{cr.replace("padding: 0 20px", "padding: 0")}{eyebrow}{h1}{lead}{ctas}{media(p["media"], True, 300 if p["media"] != "vision" else 0)}</section>'
    hh = 640 if p["id"] == "P1" else 560
    return f"""<section class="gd" style="padding: 16px 80px 96px; display: flex; flex-direction: column; gap: 32px; border-bottom: 1px solid #1A212B">
{cr.replace("padding: 0 80px", "padding: 0")}
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 56px; align-items: center">
<div style="display: flex; flex-direction: column; gap: 28px">{eyebrow}{h1}{lead}{ctas}</div>
{media(p["media"], False, hh)}
</div>
</section>"""


def shell(sec, m, inner, light=False):
    cls = "gl lt" if light else ""
    bg = "" if light else "background: #0A0C10; "
    color = "color: #0F141B; " if light else ""
    pad = "56px 20px" if m else "112px 80px"
    border = "border-bottom: 1px solid #D8DEE7" if light else "border-bottom: 1px solid #1A212B"
    sid = sec.get("sid", "")
    return f'<section id="{sid.replace(".", "-").lower()}" class="{cls}" style="{bg}{color}padding: {pad}; display: flex; flex-direction: column; gap: {20 if m else 40}px; {border}">\n{inner}\n</section>'


def head(sec, m, light):
    c2 = "#3A4453" if light else "#B7C0CD"
    label = f'<div class="mono" style="font-size: 12px; color: {"#5A6475" if light else "#8A94A4"}">{e(sec["sid"])}</div>' if sec.get("sid") else ""
    h2 = f'<h2 class="disp" style="margin: 0; font-size: {28 if m else 40}px; font-weight: 500; line-height: 1.15; max-width: 760px">{e(sec["h2"])}</h2>'
    if sec.get("status"):
        h2 += f'<div><span class="mono" style="display: inline-block; padding: 6px 12px; border: 1px solid {"#D8DEE7" if light else "#2E3846"}; border-radius: 999px; font-size: 12px">{e(sec["status"])}</span></div>'
    intro = f'<p style="margin: 0; font-size: {15 if m else 17}px; color: {c2}; line-height: 1.6; max-width: 640px">{rich(sec["intro"], light)}</p>' if sec.get("intro") else ""
    if m or not intro:
        return f'<div style="display: flex; flex-direction: column; gap: 12px">{label}{h2}{intro}</div>'
    return f'<div style="display: grid; grid-template-columns: 7fr 5fr; gap: 48px; align-items: end"><div style="display: flex; flex-direction: column; gap: 12px">{label}{h2}</div>{intro}</div>'


def bullets(items, m, light):
    c = "#0F141B" if light else "#E8ECF2"
    dot = "#5A6475" if light else "#8A94A4"
    lis = "".join(f'<li style="display: flex; gap: 12px; align-items: baseline; padding: 14px 0; border-top: 1px solid {"#D8DEE7" if light else "#232B36"}"><span aria-hidden="true" style="flex-shrink: 0; width: 8px; height: 8px; border-radius: 2px; background: {dot}; transform: translateY(-2px)"></span><span>{rich(i, light)}</span></li>' for i in items)
    cols = "1fr" if m else "repeat(2, minmax(0, 1fr))"
    return f'<ul style="margin: 0; padding: 0; list-style: none; display: grid; grid-template-columns: {cols}; column-gap: 40px; font-size: {15 if m else 16}px; line-height: 1.55; color: {c}">{lis}</ul>'


def tiles(items, m, light, numbered=False):
    """items: (title, text) -> cards."""
    surf = "#FFFFFF" if light else "#141A22"
    bd = "#D8DEE7" if light else "#232B36"
    c2 = "#3A4453" if light else "#B7C0CD"
    acc = "#5A6475" if light else "#8A94A4"
    n = len(items)
    cols = 1 if m else (4 if n == 4 else 3 if n in (3, 6) else 2)
    out = ""
    for k, (t, txt) in enumerate(items):
        num = f'<div class="mono" style="font-size: 12px; color: {acc}">{k + 1:02d}</div>' if numbered else ""
        out += f'<article style="background: {surf}; border: 1px solid {bd}; border-radius: {16 if m else 20}px; padding: {18 if m else 24}px; display: flex; flex-direction: column; gap: 10px">{num}{raqib_mark(40, *(("#0F141B", "#9AA3B2", "#2457C8") if light else ())) if t.startswith("Raqib") else ""}<h3 class="disp" style="margin: 0; font-size: {16 if m else 19}px; font-weight: 500; line-height: 1.35">{e(t)}</h3><p style="margin: 0; font-size: 15px; color: {c2}; line-height: 1.55">{rich(txt, light)}</p></article>'
    return f'<div style="display: grid; grid-template-columns: repeat({cols}, minmax(0, 1fr)); gap: {12 if m else 20}px">{out}</div>'


def table(rows, m, light, cols):
    bd = "#D8DEE7" if light else "#232B36"
    lab = "#5A6475" if light else "#8A94A4"
    surf = "#FFFFFF" if light else "#141A22"
    trs = ""
    for r in rows:
        mc = "mono" if len(r[1]) < 32 else ""
        if m:
            trs += f'<tr style="border-top: 1px solid {bd}"><th scope="row" style="display: block; padding: 14px 16px 2px; text-align: left; font-weight: 400; font-size: 13px; color: {lab}">{e(r[0])}</th><td class="{mc}" style="display: block; padding: 2px 16px 14px; font-size: 14px">{rich(r[1], light)}</td></tr>'
        else:
            extra = "".join(f'<td style="padding: 16px 24px; font-size: 15px; color: {"#3A4453" if light else "#B7C0CD"}">{rich(c, light)}</td>' for c in r[2:])
            trs += f'<tr style="border-top: 1px solid {bd}"><th scope="row" style="padding: 16px 24px; text-align: left; font-weight: 400; color: {lab}; width: 30%">{e(r[0])}</th><td class="{mc}" style="padding: 16px 24px; font-size: 15px">{rich(r[1], light)}</td>{extra}</tr>'
    thead = "" if m else "<thead><tr>" + "".join(f'<th scope="col" class="mono" style="padding: 14px 24px; text-align: left; font-weight: 400; font-size: 12px; color: {lab}">{e(c)}</th>' for c in cols) + "</tr></thead>"
    return f'<div style="background: {surf}; border: 1px solid {bd}; border-radius: {16 if m else 20}px; overflow: hidden"><table style="width: 100%; border-collapse: collapse; font-size: 15px">{thead}<tbody>{trs}</tbody></table></div>'


def faq(items, m, light=True):
    bd = "#D8DEE7" if light else "#232B36"
    c2 = "#3A4453" if light else "#B7C0CD"
    out = ""
    for k, (q, a) in enumerate(items):
        op = " open" if k == 0 else ""
        out += f'''<details{op} style="border-top: 1px solid {bd}"><summary style="display: flex; justify-content: space-between; align-items: center; gap: 16px; padding: {18 if m else 22}px 0; min-height: 44px; font-size: {16 if m else 18}px; font-weight: 500"><h3 style="margin: 0; font: inherit">{e(q)}</h3><span aria-hidden="true" class="mono" style="flex-shrink: 0; width: 32px; height: 32px; border: 1px solid {bd}; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 16px">{"−" if op else "+"}</span></summary><p style="margin: 0 0 22px; max-width: 720px; font-size: 15px; line-height: 1.6; color: {c2}">{rich(a, light)}</p></details>'''
    return f'<div style="max-width: 880px; border-bottom: 1px solid {bd}">{out}</div>'


def product_cards(m):
    cards = [
        ("AI vision", "Prototype · pilot partners welcome", "#B7C0CD", "Gowning and PPE checks on your existing CCTV, for pharma cleanrooms and surgery.", "/ai-vision", "Explore AI vision", "factory"),
        ("Cleaning robot", "In development", "#B7C0CD", "An autonomous floor-cleaning robot for offices and malls.", "/cleaning-robot", "Explore the cleaning robot", "cleaning"),
        ("Custom humanoid robots", "Built to order", "#B7C0CD", "We design and build humanoid robots to your requirement.", "/humanoid-robots", "Humanoid robot development", "humanoid"),
        ("Custom robotic arms", "Built to order", "#B7C0CD", "We design and build robotic arms for your task.", "/robotic-arm", "Custom robotic arms", "arm_still"),
    ]
    out = ""
    for t, st, sc, txt, h, link, img in cards:
        if img == "humanoid":
            mh = '<div class="ph" style="height: 100%; border: none">[Humanoid image]<br>TODO(founder)</div>'
        elif img == "cleaning":
            mh = '<svg viewBox="0 0 300 300" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" style="display: block" role="img" aria-label="Cleaning robot (drawing)"><rect width="300" height="300" fill="#171D27"/><rect x="118" y="112" width="64" height="40" rx="10" fill="#1E2530" stroke="#3A4452"/><rect x="132" y="98" width="36" height="18" rx="9" fill="#0B0E13" stroke="#3D7BFF"/><rect x="40" y="150" width="220" height="70" rx="35" fill="#2E3846" stroke="#3A4452" stroke-width="2"/><path d="M60 196 L240 196" stroke="#3D7BFF" stroke-width="3" stroke-linecap="round"/><circle cx="90" cy="222" r="16" fill="#0B0E13" stroke="#2E3846" stroke-width="4"/><circle cx="210" cy="222" r="16" fill="#0B0E13" stroke="#2E3846" stroke-width="4"/></svg>'
        else:
            alt = "Robotic arm (stock photo, illustration)" if img == "arm_still" else "Camera view of a work floor (stock photo, illustration)"
            mh = f'<img src="{B[img]}" alt="{alt}" style="display:block;width:100%;height:100%;object-fit:cover">'
        if m:
            out += f'<article style="display: flex; gap: 14px; background: #141A22; border: 1px solid #232B36; border-radius: 16px; padding: 14px; align-items: center"><div style="width: 88px; height: 88px; border-radius: 12px; overflow: hidden; flex-shrink: 0">{mh.replace("[Humanoid image]<br>TODO(founder)", "TODO")}</div><div style="display: flex; flex-direction: column; gap: 4px"><div class="mono" style="font-size: 11px; color: {sc}">{st}</div><h3 class="disp" style="margin: 0; font-size: 16px; font-weight: 500"><a href="{h}" style="color: #E8ECF2; text-decoration: none">{t}</a></h3><p style="margin: 0; font-size: 14px; color: #B7C0CD; line-height: 1.5">{rich(txt)}</p></div></article>'
        else:
            out += f'<article style="display: flex; flex-direction: column; background: #141A22; border: 1px solid #232B36; border-radius: 20px; overflow: hidden"><div style="height: 260px; border-bottom: 1px solid #232B36; overflow: hidden">{mh}</div><div style="padding: 24px; display: flex; flex-direction: column; gap: 10px; flex-grow: 1"><div class="mono" style="font-size: 12px; color: {sc}">{st}</div><h3 class="disp" style="margin: 0; font-size: 20px; font-weight: 500">{t}</h3><p style="margin: 0; font-size: 15px; color: #B7C0CD; line-height: 1.55; flex-grow: 1">{rich(txt)}</p><a href="{h}" style="font-size: 15px; margin-top: 8px">{link}</a></div></article>'
    cols = "1fr" if m else "repeat(4, minmax(0, 1fr))"
    return f'<div style="display: grid; grid-template-columns: {cols}; gap: {12 if m else 20}px">{out}</div>'


def feature_rows(items, m):
    """Home: one row per product with link (P1.3-P1.6)."""
    out = ""
    for sid, h2, txt, link, href in items:
        if m:
            out += f'<div style="padding: 20px 0; border-top: 1px solid #232B36; display: flex; flex-direction: column; gap: 10px"><div class="mono" style="font-size: 11px; color: #8A94A4">{sid}</div><h2 class="disp" style="margin: 0; font-size: 22px; font-weight: 500; line-height: 1.2">{e(h2)}</h2><p style="margin: 0; font-size: 15px; color: #B7C0CD; line-height: 1.6">{rich(txt)}</p><a href="{href}" style="font-size: 15px">{e(link)}</a></div>'
        else:
            out += f'<div style="display: grid; grid-template-columns: 1fr 5fr 5fr 2fr; gap: 32px; padding: 36px 0; border-top: 1px solid #232B36; align-items: baseline"><div class="mono" style="font-size: 12px; color: #8A94A4">{sid}</div><h2 class="disp" style="margin: 0; font-size: 28px; font-weight: 500; line-height: 1.2">{e(h2)}</h2><p style="margin: 0; font-size: 16px; color: #B7C0CD; line-height: 1.6">{rich(txt)}</p><a href="{href}" style="font-size: 15px; justify-self: end">{e(link)}</a></div>'
    return f'<div style="border-bottom: 1px solid #232B36">{out}</div>'


def links_row(items, m, light=False):
    bd = "#D8DEE7" if light else "#2E3846"
    surf = "#FFFFFF" if light else "#141A22"
    c = "#0F141B" if light else "#E8ECF2"
    out = "".join(f'<a href="{h}" style="display: flex; justify-content: space-between; align-items: center; gap: 16px; padding: {18 if m else 24}px; background: {surf}; border: 1px solid {bd}; border-radius: 16px; text-decoration: none; color: {c}; font-size: {16 if m else 18}px"><span>{e(t)}</span><span aria-hidden="true" class="mono">→</span></a>' for t, h in items)
    cols = "1fr" if m else f"repeat({len(items)}, minmax(0, 1fr))"
    return f'<div style="display: grid; grid-template-columns: {cols}; gap: 12px">{out}</div>'


def contact_block(m):
    fields = [("Your name", "text", True, "Priya Reddy"), ("Company", "text", False, ""), ("Phone", "tel", True, "+91"), ("Email", "email", False, "")]
    inp = 'style="height: 48px; padding: 0 14px; background: #0A0C10; border: 1px solid #2E3846; border-radius: 10px; color: #E8ECF2; font: inherit; font-size: 15px"'
    f = "".join(f'<label style="display: flex; flex-direction: column; gap: 8px; font-size: 14px; color: #B7C0CD">{l}{" *" if r else " (optional)"}<input type="{t}" placeholder="{p}" {inp}></label>' for l, t, r, p in fields)
    grid = "1fr" if m else "repeat(2, minmax(0, 1fr))"
    form = f"""<form style="padding: {20 if m else 36}px; background: #141A22; border: 1px solid #232B36; border-radius: {16 if m else 24}px; display: flex; flex-direction: column; gap: 18px">
<div style="display: grid; grid-template-columns: {grid}; gap: 18px">{f}</div>
<label style="display: flex; flex-direction: column; gap: 8px; font-size: 14px; color: #B7C0CD">What’s it about? *<select {inp}><option>AI vision pilot</option><option>Cleaning robot pilot</option><option>Custom humanoid robot</option><option>Custom robotic arm</option><option>Custom computer vision</option><option>Something else</option></select></label>
<label style="display: flex; flex-direction: column; gap: 8px; font-size: 14px; color: #B7C0CD">City (optional)<input type="text" {inp}></label>
<label style="display: flex; flex-direction: column; gap: 8px; font-size: 14px; color: #B7C0CD">Your requirement (optional)<textarea rows="4" style="padding: 12px 14px; background: #0A0C10; border: 1px solid #2E3846; border-radius: 10px; color: #E8ECF2; font: inherit; font-size: 15px; resize: none"></textarea></label>
<button type="submit" style="height: 52px; background: #2F66E0; color: #FFFFFF; border: none; border-radius: 999px; font: inherit; font-size: 15px; font-weight: 500">Send</button>
<p style="margin: 0; font-size: 13px; color: #8A94A4">After sending: "Thanks. We've got your message and will reply soon."</p>
</form>"""
    return form


def footer(m):
    prod = "".join(f'<li><a href="{h}" style="color: #B7C0CD; text-decoration: none">{t}</a></li>' for t, h in PRODUCTS)
    ind = "".join(f'<li><a href="{h}" style="color: #B7C0CD; text-decoration: none">{t}</a></li>' for t, h in INDUSTRIES)
    co = '<li><a href="/about" style="color: #B7C0CD; text-decoration: none">About</a></li><li><a href="/team" style="color: #B7C0CD; text-decoration: none">Team</a></li><li><a href="/software" style="color: #B7C0CD; text-decoration: none">Software</a></li><li><a href="/contact" style="color: #B7C0CD; text-decoration: none">Contact</a></li>'
    ul = 'style="margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 10px; font-size: 14px"'
    colh = 'class="mono" style="font-size: 12px; color: #8A94A4; margin-bottom: 14px"'
    nap = f'<address style="font-style: normal; font-size: 14px; line-height: 1.7; color: #B7C0CD">Cybertronix<br>Rd No. 10C, Gayatri Hills, Jubilee Hills<br>Hyderabad, Telangana<br><a href="tel:+919059897807">+91 90598 97807</a> · <a href="mailto:info@cybertronix.com">info@cybertronix.com</a></address>'
    social = '<div class="mono" style="display: flex; flex-wrap: wrap; gap: 16px; font-size: 12px; color: #8A94A4"><span>[LinkedIn]</span><span>[YouTube]</span><span>[Instagram]</span><span class="todo" style="color: #FF8A3D">TODO(founder) URLs</span></div>'
    cols = "1fr" if m else "4fr 2fr 2fr 2fr"
    pad = "40px 20px" if m else "72px 80px 40px"
    return f"""<footer style="margin-top: auto; padding: {pad}; border-top: 1px solid #1A212B; background: #0A0C10; display: flex; flex-direction: column; gap: 40px">
<div style="display: grid; grid-template-columns: {cols}; gap: 32px">
<div style="display: flex; flex-direction: column; gap: 16px"><a href="/" style="display: flex; align-items: center; gap: 12px; text-decoration: none; color: #E8ECF2">{LOGO.format(s=30)}<span class="disp" style="font-size: 16px; font-weight: 600; letter-spacing: -0.02em">cybertronix</span></a>{nap}</div>
<div><div {colh}>Robots</div><ul {ul}>{prod}</ul></div>
<div><div {colh}>Industries</div><ul {ul}>{ind}</ul></div>
<div><div {colh}>Company</div><ul {ul}>{co}</ul></div>
</div>
<div style="display: flex; {"flex-direction: column; gap: 12px" if m else "justify-content: space-between"}; padding-top: 24px; border-top: 1px solid #1A212B; font-size: 13px; color: #8A94A4"><span>© Cybertronix · Hyderabad, India</span>{social}</div>
</footer>"""


def cta_band(sec, m):
    ctas = "".join(btn(t, h, i == 0, m) for i, (t, h) in enumerate(sec["ctas"]))
    return f"""<section class="gd" style="padding: {"56px 20px" if m else "120px 80px"}; display: flex; flex-direction: column; align-items: {"stretch" if m else "flex-start"}; gap: 24px; border-bottom: 1px solid #1A212B">
<div class="mono" style="font-size: 12px; color: #8A94A4">{e(sec["sid"])}</div>
<h2 class="disp" style="margin: 0; font-size: {28 if m else 44}px; font-weight: 500; line-height: 1.15; max-width: 820px">{e(sec["h2"])}</h2>
<p style="margin: 0; font-size: {16 if m else 19}px; color: #B7C0CD; line-height: 1.6; max-width: 620px">{rich(sec["intro"])}</p>
<div style="display: flex; {"flex-direction: column; gap: 10px" if m else "gap: 12px"}">{ctas}</div>
</section>"""


def render_section(sec, m):
    t = sec["type"]
    light = sec.get("light", False)
    if t == "cta":
        return cta_band(sec, m)
    body = ""
    if t == "cards": body = product_cards(m)
    elif t == "features": return shell(sec, m, feature_rows(sec["items"], m))
    elif t == "bullets": body = bullets(sec["items"], m, light)
    elif t == "tiles": body = tiles(sec["items"], m, light, sec.get("numbered", False))
    elif t == "table": body = table(sec["rows"], m, light, sec["cols"])
    elif t == "faq": body = faq(sec["items"], m, light)
    elif t == "text": body = "".join(f'<p style="margin: 0; max-width: 760px; font-size: {15 if m else 17}px; line-height: 1.6; color: {"#3A4453" if light else "#B7C0CD"}">{rich(x, light)}</p>' for x in sec["paras"])
    elif t == "links": body = links_row(sec["items"], m, light)
    elif t == "media": body = media(sec["media"], m, 240 if m else 560)
    elif t == "contact": body = contact_block(m)
    elif t == "people":
        card = '<article style="background: #141A22; border: 1px solid #232B36; border-radius: 20px; overflow: hidden"><div class="ph" style="height: 220px; border: none; border-bottom: 1px solid #232B36">Photo coming soon</div><div style="padding: 18px; display: flex; flex-direction: column; gap: 6px"><div class="mono" style="font-size: 12px; color: #8A94A4">[Name, added by founder]</div><div style="font-size: 15px; color: #B7C0CD">[Role]</div></div></article>'
        body = f'<div style="display: grid; grid-template-columns: {"repeat(2, minmax(0, 1fr))" if m else "repeat(4, minmax(0, 1fr))"}; gap: {12 if m else 20}px">' + card * 4 + '</div>' 
    elif t == "split":  # text + media
        left = "".join(f'<p style="margin: 0; font-size: {15 if m else 17}px; line-height: 1.6; color: #B7C0CD">{rich(x)}</p>' for x in sec["paras"])
        md = media(sec["media"], m, 240 if m else 420)
        body = f'<div style="display: grid; grid-template-columns: {"1fr" if m else "5fr 7fr"}; gap: {20 if m else 56}px; align-items: start"><div style="display: flex; flex-direction: column; gap: 16px">{left}</div>{md}</div>'
    if sec.get("after"):
        body += f'<p style="margin: 0; font-size: 15px; line-height: 1.6; color: {"#3A4453" if light else "#B7C0CD"}; max-width: 760px">{rich(sec["after"], light)}</p>'
    if sec.get("ctas"):
        body += '<div style="display: flex; gap: 12px; flex-wrap: wrap">' + "".join(btn(t2, h, i == 0, m) for i, (t2, h) in enumerate(sec["ctas"])) + "</div>"
    return shell(sec, m, head(sec, m, light) + "\n" + body, light)


def est_height(p, m):
    h = 72 if m else 104
    h += (1150 if p.get("media") and m else 560) if m else (900 if p.get("media") else 520)
    for s in p["sections"]:
        t = s["type"]
        n = len(s.get("items", s.get("rows", s.get("paras", []))))
        if m:
            base = {"cards": 280 + n * 130, "features": 150 + n * 230, "bullets": 220 + n * 75, "tiles": 220 + n * 170,
                    "table": 260 + n * 72, "faq": 240 + n * 95 + 120, "text": 200 + n * 150, "links": 220 + n * 80,
                    "media": 520, "contact": 1100, "split": 720, "cta": 440, "people": 900}[t]
        else:
            base = {"cards": 820, "features": 300 + n * 140, "bullets": 360 + ((n + 1) // 2) * 60, "tiles": 380 + ((n + 2) // 3) * 210,
                    "table": 400 + n * 58, "faq": 360 + n * 76 + 90, "text": 320 + n * 90, "links": 340,
                    "media": 900, "contact": 1050, "split": 780, "cta": 500, "people": 700}[t]
        if s.get("intro"): base += 60 if m else 0
        if s.get("after"): base += 110 if m else 60
        if s.get("ctas") and t != "cta": base += 130 if m else 80
        h += base
    h += 640 if m else 380
    return int(h * 1.04 / 20) * 20


def board(p, m):
    w = 390 if m else 1440
    h = est_height(p, m)
    body = tabstrip(p, m) + nav(p["id"], m) + "\n<main>\n" + hero(p, m) + "\n" + "\n".join(render_section(s, m) for s in p["sections"]) + "\n</main>\n" + footer(m)
    return doc(f'{p["id"]} {p["name"]}, {"phone" if m else "desktop"}', w, h, body), w, h


exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "pages.py")).read())

def main():
    os.makedirs(ROOT, exist_ok=True)
    canvas = json.load(open(ROOT + "/canvas.json"))
    # archive the original home boards (renamed copies)
    boards, order = {}, []
    pages = [{"id": "site", "name": "Site P1–P9"}, {"id": "original", "name": "Original canvas"}]
    # style guide on row 0
    boards["StyleGuide.dc.html"] = {"x": 0, "y": 0, "w": 1440, "h": 1700, "title": "[B1] Brand guide and tokens", "page": "site"}
    order.append("StyleGuide.dc.html")
    x, y = 0, 2100
    for p in PAGES:
        for m in (False, True):
            src, w, h = board(p, m)
            fn = ("Main" if p["id"] == "P1" and not m else p["file"].replace("Main", "P1-Home") + ("-phone" if m else "-desktop")) + ".dc.html"
            if p["id"] == "P1" and not m: fn = "Main.dc.html"
            open(f"{ROOT}/{fn}", "w").write(src)
            bx = x if not m else x + 1440 + 80
            boards[fn] = {"x": bx, "y": y, "w": w, "h": h, "title": f'[{p["id"]}] {p["name"]}, {"phone 390" if m else "desktop 1440"}', "page": "site"}
            order.append(fn)
        x += 1440 + 80 + 390 + 240
    import raqib
    rx = 0
    for f, (w, h, title) in raqib.write_all().items():
        boards[f] = {"x": rx, "y": 0, "w": w, "h": h, "title": title, "page": "raqib"}
        order.append(f)
        rx += w + 80
    pages.insert(1, {"id": "raqib", "name": "Raqib R1–R3"})
    boards["Original-Home-desktop.dc.html"] = {"x": 0, "y": 0, "w": 1440, "h": 6700, "title": "Original: Home, desktop 1440 (founder canvas, archived)", "page": "original"}
    boards["Original-Home-phone.dc.html"] = {"x": 1520, "y": 0, "w": 390, "h": 2380, "title": "Original: Home, phone 390 (archived)", "page": "original"}
    order = ["Original-Home-desktop.dc.html", "Original-Home-phone.dc.html"] + order
    order.remove("Main.dc.html"); order.insert(2, "Main.dc.html")
    canvas["boards"] = boards
    canvas["order"] = order
    canvas["pages"] = pages
    canvas["launch"] = {"view": "canvas", "page": "site"}
    W = x
    canvas["notes"] = {
        "t1": {"kind": "title1", "maxW": W, "text": "Cybertronix website · Midnight Lab · one board per page (docs/PAGES.md)", "x": 0, "y": 1780, "page": "site"},
        "t2": {"kind": "title1", "maxW": rx, "text": "Raqib · logo, terminal app and local web view (D32)", "x": 0, "y": -300, "page": "raqib"},
        "n7": {"x": 0, "y": 1300, "w": 520, "fill": "orange", "page": "raqib", "text": "Panels, keys and labels match the current Raqib screenshot (docs/reference/raqib-tui-current.png) only. Numbers and process names are sample data. Founder approves with the site (T10)."},
        "t0": {"kind": "title1", "maxW": 2960, "text": "Original founder canvas, archived (do not build from this)", "x": 0, "y": -300, "page": "original"},
        "n1": {"x": 1520, "y": 0, "w": 420, "fill": "blue", "page": "site", "text": "Footage grade: brightness -10, contrast +18, saturation 55%, blue lift. All stock is mood only (D20): uncaptioned as product, alt text says stock. Full spec: docs/design.md."},
        "n2": {"x": 1520, "y": 340, "w": 420, "fill": "blue", "page": "site", "text": "Hero head-turn (P1 only, the only motion): 90–120 WebP frames 1280×1400, down → sideways → up, scrubbed by scroll. Poster under 768px and with prefers-reduced-motion. Until frames exist the hero shows the muted stock loop with a pause button."},
        "n3": {"x": 1520, "y": 700, "w": 420, "fill": "orange", "page": "site", "text": "Orange dashed chips = TODO(founder). Build hides any row, sentence or FAQ still marked TODO. Nothing on these boards is a real number, client or logo."},
        "n4": {"x": 1520, "y": 1040, "w": 420, "fill": "orange", "page": "site", "text": "P2 and P3 copy on the boards follows D16 (built to order, not shipped). SEO Content's T9 rewrite of content/ replaces it; layout stays."},
        "n5": {"x": 2000, "y": 0, "w": 420, "fill": "gray", "page": "site", "text": "Build: one H1, real text above any video. Dark hero → light spec/FAQ sections with blueprint grid → dark CTA and footer. Spec table = <table> with th scope=row. FAQ = <details> + FAQPage JSON-LD with the same words."},
        "n6": {"x": 2000, "y": 360, "w": 420, "fill": "gray", "page": "site", "text": "Raqib (developer tool) from the original canvas is parked: not in D4. Waiting on hub/founder."},
    }
    json.dump(canvas, open(ROOT + "/canvas.json", "w"), ensure_ascii=False, indent=1)
    print("boards:", len(boards))
    for k, v in boards.items(): print(k, v["w"], v["h"])


if __name__ == "__main__":
    main()
