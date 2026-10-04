#!/usr/bin/env python3
"""Cybertronix logo canvas (D35): versions of mark X "Detection C". Story: a machine that sees.
Every mark is built from square primitives on a 48-unit grid. Only ONE element carries the accent:
the seeing eye. Two detail levels: full (>= 96 px) and simple (<= 64 px). Colours from design/tokens.json."""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOK = json.load(open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "tokens.json")))
ROOT = HERE + "/logo/project"
D, L = TOK["color"]["dark"], TOK["color"]["light"]
K = {
    "dark": dict(bg=D["bg"], tile=D["surface"], rule=D["rule"], ink=D["text"], mid=D["text-muted"], acc=TOK["accent"]["dark"], t2=D["text-2"], mu=D["text-muted"]),
    "light": dict(bg=L["bg"], tile=L["surface"], rule=L["rule"], ink=L["text"], mid="#9AA3B2", acc=TOK["accent"]["light"], t2=L["text-2"], mu=L["text-muted"]),
}
SIG = TOK["signal"]["dark"]


def r(x, y, w, h, c):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>'


def brackets(a, b, L_, t, c, corners="tl tr bl br"):
    """Detection-box corner brackets on the square a..b."""
    o = ""
    if "tl" in corners: o += r(a, a, L_, t, c) + r(a, a, t, L_, c)
    if "tr" in corners: o += r(b - L_, a, L_, t, c) + r(b - t, a, t, L_, c)
    if "bl" in corners: o += r(a, b - t, L_, t, c) + r(a, b - L_, t, L_, c)
    if "br" in corners: o += r(b - L_, b - t, L_, t, c) + r(b - t, b - L_, t, L_, c)
    return o


def chead(t, top=6, bot=42, left=6, right=42, stub=8, c="#000"):
    """The C as a head: full top, left and bottom; the right side is only bracket stubs (the C opening)."""
    w, h = right - left, bot - top
    return (r(left, top, w, t, c) + r(left, bot - t, w, t, c) + r(left, top, t, h, c)
            + r(right - t, top, t, stub, c) + r(right - t, bot - stub, t, stub, c))


def m1(k, full):  # X refined
    t = 4 if full else 5
    o = brackets(3, 45, 12 if full else 13, t, k["ink"])
    ct = 5 if full else 6
    o += r(13, 13, 22, ct, k["ink"]) + r(13, 13, ct, 22, k["ink"]) + r(13, 35 - ct, 22, ct, k["ink"])
    o += r(25, 21, 6, 6, k["acc"]) if full else r(24, 20, 8, 8, k["acc"])
    return o


def m2(k, full):  # C-head, two eyes
    t = 5 if full else 6
    o = chead(t, c=k["ink"])
    if full:
        o += r(15, 17, 6, 6, k["ink"]) + r(27, 17, 6, 6, k["acc"])
        o += r(15, 29, 3, 4, k["mid"]) + r(20, 29, 3, 4, k["mid"]) + r(25, 29, 3, 4, k["mid"])
    else:
        o += r(14, 17, 8, 8, k["ink"]) + r(26, 17, 8, 8, k["acc"])
    return o


def m3(k, full):  # Visor slit
    t = 5 if full else 6
    o = chead(t, c=k["ink"])
    o += r(13, 20, 33, 6, k["acc"]) if full else r(13, 19, 33, 8, k["acc"])
    if full:
        o += r(15, 31, 14, 2, k["mid"]) + r(15, 35, 14, 2, k["mid"])
    return o


def m4(k, full):  # Head-turn: eyes shifted toward the opening
    t = 5 if full else 6
    o = chead(t, c=k["ink"])
    if full:
        o += f'<rect x="15.75" y="17.75" width="4.5" height="4.5" fill="none" stroke="{k["mid"]}" stroke-width="1.5"/>'
        o += r(24, 17, 6, 6, k["ink"]) + r(34, 17, 6, 6, k["acc"])
    else:
        o += r(22, 17, 8, 8, k["ink"]) + r(33, 17, 8, 8, k["acc"])
    return o


def octagon(cx, cy, rad):
    import math
    pts = []
    for i in range(8):
        a = math.radians(22.5 + i * 45)
        pts.append(f"{cx + rad * math.cos(a):.2f},{cy + rad * math.sin(a):.2f}")
    return " ".join(pts)


def m5(k, full):  # Lens eye with aperture
    t = 5 if full else 6
    o = chead(t, c=k["ink"])
    if full:
        o += f'<polygon points="{octagon(25, 24, 10)}" fill="none" stroke="{k["ink"]}" stroke-width="3"/>'
        for (x1, y1, x2, y2) in ((25, 15, 29, 21), (34, 24, 28, 27), (25, 33, 21, 27), (16, 24, 22, 21)):
            o += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{k["mid"]}" stroke-width="1.5"/>'
        o += f'<polygon points="{octagon(25, 24, 4)}" fill="{k["acc"]}"/>'
    else:
        o += f'<polygon points="{octagon(25, 24, 10)}" fill="none" stroke="{k["ink"]}" stroke-width="4"/>'
        o += f'<polygon points="{octagon(25, 24, 5)}" fill="{k["acc"]}"/>'
    return o


def m6(k, full):  # Antenna / sensor mast
    t = 5 if full else 6
    o = chead(t, top=13, stub=7, c=k["ink"])
    o += r(22, 4, 4, 9, k["ink"]) + (r(18, 2, 12, 4, k["ink"]) if full else r(19, 2, 10, 4, k["ink"]))
    if full:
        o += r(15, 22, 6, 6, k["ink"]) + r(27, 22, 6, 6, k["acc"]) + r(15, 33, 18, 2, k["mid"])
    else:
        o += r(14, 21, 8, 8, k["ink"]) + r(26, 21, 8, 8, k["acc"])
    return o


PIX = ["########",
       "#......#",
       "#.#..@..",
       "#.......",
       "#.......",
       "#.mmm...",
       "#......#",
       "########"]


def m7(k, full):  # 8x8 pixel grid
    o = ""
    for y, row in enumerate(PIX):
        for x, ch in enumerate(row):
            if ch == "#": o += r(x * 6, y * 6, 6, 6, k["ink"])
            elif ch == "@": o += r(x * 6, y * 6, 6, 6, k["acc"])
            elif ch == "m" and full: o += r(x * 6, y * 6, 6, 6, k["mid"])
    if full:
        for y in range(9):
            o += r(0, y * 6, 48, 0.25, k["mid"])
        for x in range(9):
            o += r(x * 6, 0, 0.25, 48, k["mid"])
    return o


def m8(k, full):  # Detection lock: brackets closing in on the face
    o = ""
    if full:
        o += brackets(1, 47, 8, 1.5, k["mid"])
    o += brackets(5, 43, 11, 4 if full else 5, k["ink"])
    ct = 4 if full else 5
    o += r(14, 14, 20, ct, k["ink"]) + r(14, 14, ct, 20, k["ink"]) + r(14, 34 - ct, 20, ct, k["ink"])
    o += r(25, 21, 6, 6, k["acc"]) if full else r(24, 20, 8, 8, k["acc"])
    return o


def m9(k, full):  # Blueprint: the head as a technical drawing
    t = 5 if full else 6
    o = chead(t, c=k["ink"])
    if full:
        o += r(6, 1, 36, 1, k["mid"]) + r(6, 0, 1, 3, k["mid"]) + r(41, 0, 1, 3, k["mid"])
        o += r(46, 6, 1, 36, k["mid"]) + r(45, 6, 3, 1, k["mid"]) + r(45, 41, 3, 1, k["mid"])
        o += r(18, 24, 18, 1, k["mid"]) + r(27, 15, 1, 18, k["mid"])
        o += r(24, 21, 7, 7, k["acc"])
    else:
        o += r(23, 20, 9, 9, k["acc"])
    return o


def m10(k, full):  # Hex helm: the old hexagon kept at its corners, with a visor
    import math
    pts = [(24, 3), (42.2, 13.5), (42.2, 34.5), (24, 45), (5.8, 34.5), (5.8, 13.5)]
    o = ""
    sw = 4 if full else 5
    for i, (x, y) in enumerate(pts):
        for (nx, ny) in (pts[i - 1], pts[(i + 1) % 6]):
            o += f'<line x1="{x}" y1="{y}" x2="{x + (nx - x) * 0.3:.1f}" y2="{y + (ny - y) * 0.3:.1f}" stroke="{k["ink"]}" stroke-width="{sw}" stroke-linecap="square"/>'
    o += f'<path d="M32 15 H16 V33 H32" fill="none" stroke="{k["ink"]}" stroke-width="{sw}"/>'
    o += r(19, 21, 19, 5, k["acc"]) if full else r(18, 20, 20, 7, k["acc"])
    return o


MARKS = [
    ("L1", "X refined", m1, "The chosen mark, polished: detection corners around a square C; the blue square is what the camera found."),
    ("L2", "C-head", m2, "The C becomes a head. Two eyes; only the right one is a live lens, in blue."),
    ("L3", "Visor", m3, "One visor slit runs out through the C's opening: the machine scans the room."),
    ("L4", "Head-turn", m4, "The eyes have turned toward the opening, as if looking at you. Matches the P1 hero head-turn."),
    ("L5", "Lens eye", m5, "One camera lens with aperture blades inside the C. The blue iris is the only colour."),
    ("L6", "Sensor mast", m6, "A sensor mast on top of the C-head: a robot that is listening as well as seeing."),
    ("L7", "Pixel 8×8", m7, "Built on an 8×8 grid, so it is pixel-perfect at 16 px. One blue pixel is the eye."),
    ("L8", "Detection lock", m8, "The brackets close in on the face: the moment the system locks on. Faint outer corners show where they started."),
    ("L9", "Blueprint", m9, "Wildcard. The C-head drawn as a technical drawing, with dimension lines; the eye sits on the crosshair."),
    ("L10", "Hex helm", m10, "Wildcard. Today's hexagon kept only at its corners, as a helmet, with a blue visor."),
]


def svg(size, inner, label):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 48 48" role="img" aria-label="{label}" style="display: block">{inner}</svg>'


def mark(fn, theme, size, full=None, mono=False):
    k = dict(K[theme])
    if full is None:
        full = size > 64
    if mono:
        k["acc"] = k["mid"] = k["ink"]
    return svg(size, fn(k, full), "Cybertronix logo")


def lockup(fn, theme, size=48):
    k = K[theme]
    return (f'<div style="display: flex; align-items: center; gap: {int(size * 0.3)}px">{mark(fn, theme, size)}'
            f'<span class="disp" style="font-size: {int(size * 0.62)}px; font-weight: 600; letter-spacing: -0.02em; line-height: 1; color: {k["ink"]}">cybertronix</span></div>')


HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400;500;600&amp;family=Geist:wght@400;500;600&amp;family=JetBrains+Mono:wght@400;500&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{bg};font-family:Geist,system-ui,sans-serif}}
.mono{{font-family:'JetBrains Mono',monospace}}
.disp{{font-family:Unbounded,Geist,sans-serif}}
</style>
</helmet>
{body}
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


def page(title, w, h, body):
    body = re.sub(r"border-radius: (?!50%)[^;\"]+", "border-radius: 0", body)
    return HEAD.format(title=title, w=w, h=h, bg=D["bg"], body=body)


def cap(t, theme="light"):
    return f'<span class="mono" style="font-size: 11px; color: {K[theme]["mu"]}">{t}</span>'


def tab(fn, theme):
    k = K[theme]
    return (f'<div style="display: flex; align-items: center; gap: 8px; padding: 8px 12px; background: {k["tile"]}; border: 2px solid {k["rule"]}; width: 190px">'
            f'{mark(fn, theme, 16)}<span style="font-size: 13px; color: {k["ink"]}">Cybertronix</span><span style="margin-left: auto; color: {k["mu"]}; font-size: 12px">×</span></div>')


def board(lid, name, fn, story):
    Dk, Lk = K["dark"], K["light"]
    sizes = "".join(f'<figure style="margin: 0; display: flex; flex-direction: column; align-items: center; gap: 6px">{mark(fn, "light", s)}<figcaption>{cap(str(s) + (" full" if s > 64 else ""))}</figcaption></figure>' for s in (128, 64, 32, 24, 16))
    sizes_d = "".join(f'<figure style="margin: 0; display: flex; flex-direction: column; align-items: center; gap: 6px">{mark(fn, "dark", s)}<figcaption>{cap(str(s), "dark")}</figcaption></figure>' for s in (64, 32, 24, 16))
    icon = lambda th, bgc: f'<div style="width: 120px; height: 120px; background: {bgc}; border: 2px solid {K[th]["rule"]}; display: flex; align-items: center; justify-content: center">{mark(fn, th, 76, full=False)}</div>'
    body = f"""<div style="width: 1440px; height: 780px; display: grid; grid-template-columns: 320px 360px 1fr; grid-template-rows: auto 1fr; background: {Lk['bg']}">
<header style="grid-column: 1 / -1; padding: 24px 32px; background: {Dk['bg']}; color: {Dk['ink']}; border-bottom: 2px solid {Dk['rule']}; display: flex; gap: 32px; align-items: baseline">
<span class="mono" style="font-size: 13px; color: {Dk['mu']}">[{lid}]</span>{tag(lid)}<h1 class="disp" style="margin: 0; font-size: 28px; font-weight: 500">{name}</h1><p style="margin: 0; font-size: 16px; color: {Dk['t2']}; line-height: 1.5; max-width: 760px">{story}</p></header>
<div style="background: {Dk['bg']}; border-right: 2px solid {Dk['rule']}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 28px; padding: 24px">
{mark(fn, "dark", 200)}{cap("full · dark", "dark")}
<div style="display: flex; align-items: flex-end; gap: 16px">{sizes_d}</div>
</div>
<div style="background: {Lk['bg']}; border-right: 2px solid {Lk['rule']}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 28px; padding: 24px">
{mark(fn, "light", 200)}{cap("full · light")}
<div style="display: flex; gap: 16px; align-items: center">{mark(fn, "light", 56, mono=True)}<div style="padding: 8px; background: {Dk['bg']}">{mark(fn, "dark", 56, mono=True)}</div>{cap("mono")}</div>
</div>
<div style="padding: 28px 32px; display: flex; flex-direction: column; gap: 22px; color: {Lk['ink']}">
<div style="display: flex; flex-direction: column; gap: 10px">{cap("Two detail levels: full at 96 px and up, simple at 64 px and down")}<div style="display: flex; align-items: flex-end; gap: 22px; padding: 16px; background: {Lk['tile']}; border: 2px solid {Lk['rule']}">{sizes}</div></div>
<div style="display: grid; grid-template-columns: auto auto 1fr; gap: 22px; align-items: center">
<div style="display: flex; flex-direction: column; gap: 6px">{icon("light", "#FFFFFF")}{cap("app icon")}</div>
<div style="display: flex; flex-direction: column; gap: 6px">{icon("dark", Dk['bg'])}{cap("app icon · dark")}</div>
<div style="display: flex; flex-direction: column; gap: 10px">{tab(fn, "light")}{tab(fn, "dark")}{cap("favicon · 16 px simple mark")}</div>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px">
<div style="padding: 22px; background: {Lk['tile']}; border: 2px solid {Lk['rule']}">{lockup(fn, "light", 48)}</div>
<div style="padding: 22px; background: {Dk['bg']}; border: 2px solid {Dk['rule']}">{lockup(fn, "dark", 48)}</div>
</div>
</div>
</div>"""
    return page(f"{lid} {name}", 1440, 780, body)


CHOSEN = "L6"
CHOSEN_TAG = f'<span class="mono" style="padding: 3px 10px; background: {TOK["accent"]["dark"]}; color: #FFFFFF; font-size: 12px">Chosen (D38)</span>'
PREV_TAG = '<span class="mono" style="padding: 3px 10px; border: 2px solid #8A94A4; color: #8A94A4; font-size: 12px">Previous pick (D36)</span>'


def tag(lid):
    return CHOSEN_TAG if lid == CHOSEN else PREV_TAG if lid == "L4" else ""


def dont_tile(inner, label):
    return (f'<figure style="margin: 0; display: flex; flex-direction: column; gap: 8px"><div style="position: relative; height: 150px; background: {K["light"]["tile"]}; border: 2px solid {K["light"]["rule"]}; display: flex; align-items: center; justify-content: center">'
            f'{inner}<svg width="18" height="18" viewBox="0 0 18 18" style="position: absolute; left: 8px; top: 8px" aria-hidden="true"><path d="M2 2 L16 16 M16 2 L2 16" stroke="{SIG}" stroke-width="3"/></svg></div>'
            f'<figcaption style="font-size: 14px; color: {K["light"]["ink"]}">{label}</figcaption></figure>')


def l0():
    Dk, Lk = K["dark"], K["light"]
    cells = ""
    for lid, name, fn, _s in MARKS:
        cells += (f'<div style="padding: 20px; background: {Dk["bg"]}; border: 2px solid {TOK["accent"]["dark"] if lid == CHOSEN else Dk["rule"]}; display: flex; flex-direction: column; align-items: center; gap: 14px">'
                  f'{mark(fn, "dark", 120)}<div style="display: flex; gap: 12px; align-items: flex-end">{mark(fn, "dark", 32)}{mark(fn, "dark", 16)}<div style="padding: 4px; background: {Lk["bg"]}">{mark(fn, "light", 32)}</div></div>'
                  f'<div style="text-align: center"><div class="mono" style="font-size: 12px; color: {Dk["mu"]}">{lid}</div>{tag(lid)}<div style="font-size: 16px; font-weight: 600; color: {Dk["ink"]}">{name}</div></div></div>')
    k = dict(Lk)
    base = m2(k, True)
    rounded = svg(96, f'<rect x="6" y="6" width="36" height="36" rx="10" fill="none" stroke="{k["ink"]}" stroke-width="5"/>' + r(15, 17, 6, 6, k["ink"]) + r(27, 17, 6, 6, k["acc"]), "rounded, wrong")
    grad = svg(96, f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7C4DFF"/><stop offset="1" stop-color="#3D7BFF"/></linearGradient></defs>' + chead(5, c="url(#g)") + r(15, 17, 6, 6, k["ink"]) + r(27, 17, 6, 6, k["acc"]), "gradient, wrong")
    smile = svg(96, chead(5, c=k["ink"]) + r(15, 17, 6, 6, k["ink"]) + r(27, 17, 6, 6, k["acc"]) + f'<path d="M15 29 Q24 37 33 29" fill="none" stroke="{k["ink"]}" stroke-width="3"/>', "smile, wrong")
    twoacc = svg(96, chead(5, c=k["ink"]) + r(15, 17, 6, 6, k["acc"]) + r(27, 17, 6, 6, k["acc"]) + r(15, 29, 18, 3, SIG), "two accents, wrong")
    tilt = svg(96, f'<g transform="rotate(-12 24 24)">{base}</g>', "rotated, wrong")
    shadow = svg(96, f'<g transform="translate(2 2)" opacity="0.35">{chead(5, c="#000")}</g>' + base, "shadow, wrong")
    donts = "".join(dont_tile(s, t) for s, t in [(rounded, "No rounded corners"), (grad, "No gradients"), (smile, "No cartoon smile: a machine, not a mascot"),
                                                  (twoacc, "One accent only: the seeing eye"), (tilt, "No tilting or rotating"), (shadow, "No shadows or 3D")])
    dos = "".join(f'<li style="padding: 8px 0; border-top: 2px solid {Lk["rule"]}">{x}</li>' for x in [
        "Square corners. Strokes and rules on the 2 px logic of the site.",
        "Blue only on the seeing eye. Everything else ink, with grey for detail.",
        "Use the simple mark at 64 px and below, the full mark at 96 px and up.",
        "The face stays a machine: lenses, slits and brackets, never a mouth that smiles.",
        "Colours from design/tokens.json only."])
    body = f"""<div style="width: 1440px; height: 1340px; display: flex; flex-direction: column; background: {Dk['bg']}">
<header style="padding: 32px; border-bottom: 2px solid {Dk['rule']}; color: {Dk['ink']}; display: flex; justify-content: space-between; align-items: flex-end; gap: 32px">
<div><div class="mono" style="font-size: 12px; color: {Dk['mu']}">[L0] Cybertronix logo · versions of mark X "Detection C" (D35) · the founder picks one</div><h1 class="disp" style="margin: 10px 0 0; font-size: 34px; font-weight: 500">A machine that sees</h1></div>
<p style="margin: 0; font-size: 16px; color: {Dk['t2']}; line-height: 1.55; max-width: 620px">The detection-box corners that form the C are also a robot's head. The eyes inside are camera lenses. Like Hostelzy's "only your bed is red", only one thing is blue: the seeing eye.</p></header>
<div style="padding: 28px 32px; display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 16px">{cells}</div>
<section style="flex: 1; background: {Lk['bg']}; padding: 28px 32px; display: grid; grid-template-columns: 2fr 1fr; gap: 32px; color: {Lk['ink']}">
<div style="display: flex; flex-direction: column; gap: 14px"><h2 class="disp" style="margin: 0; font-size: 20px; font-weight: 500">Don't</h2><div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px">{donts}</div></div>
<div style="display: flex; flex-direction: column; gap: 14px"><h2 class="disp" style="margin: 0; font-size: 20px; font-weight: 500">Do</h2><ul style="margin: 0; padding: 0; list-style: none; font-size: 15px; line-height: 1.5">{dos}</ul></div>
</section>
</div>"""
    return page("L0 Cybertronix logo comparison", 1440, 1340, body)


def write_all():
    os.makedirs(ROOT, exist_ok=True)
    out = {"Main.dc.html": (l0(), 1440, 1340, "[L0] Comparison · do and don't")}
    for lid, name, fn, story in MARKS:
        out[f"{lid}-{re.sub(r'[^A-Za-z0-9]+', '-', name).strip('-')}.dc.html"] = (board(lid, name, fn, story), 1440, 780, f"[{lid}] {name}")
    for f, (src, *_r) in out.items():
        open(f"{ROOT}/{f}", "w").write(src)
    import finals
    fsrc, fh = finals.board("cybertronix", *finals.STORIES["cybertronix"])
    open(f"{ROOT}/{CHOSEN}-Final.dc.html", "w").write(fsrc)
    boards, order = {}, []
    l4 = [f for f in out if f.startswith(CHOSEN + "-")][0]
    boards[f"{CHOSEN}-Final.dc.html"] = {"x": 0, "y": 0, "w": 1440, "h": fh, "title": f"[{CHOSEN}] Final · Chosen (D38) · rules and lock-ups"}
    boards[l4] = {"x": 1520, "y": 0, "w": 1440, "h": 780, "title": f"[{CHOSEN}] Sensor mast · Chosen (D38)"}
    y0 = fh + 340
    boards["Main.dc.html"] = {"x": 0, "y": y0, "w": 1440, "h": 1340, "title": out["Main.dc.html"][3]}
    i = 0
    for f, v in out.items():
        if f in ("Main.dc.html", l4):
            continue
        col, row = i % 2, i // 2
        boards[f] = {"x": col * 1520, "y": y0 + 1340 + 340 + row * (780 + 140), "w": 1440, "h": 780, "title": v[3] + (" · Previous pick (D36)" if f.startswith("L4-") else "")}
        i += 1
    order = list(boards)
    canvas = {"v": 3, "createdOnFiles": {"v": 1, "at": "2026-10-03T17:10:00Z"}, "title": "Cybertronix · Logo",
              "launch": {"view": "canvas"}, "pages": [], "boards": boards, "order": order, "designSystems": [],
              "notes": {"t0": {"kind": "title1", "text": "Chosen: L6 Sensor mast (D38)", "x": 0, "y": -300, "maxW": 2960},
                        "t2": {"kind": "title1", "text": "Comparison of all versions", "x": 0, "y": y0 - 300, "maxW": 2960},
                        "t1": {"kind": "title1", "text": "Versions L1–L10 · each: full + simple marks, mono, app icon, favicon, lock-up", "x": 0, "y": y0 + 1340 + 40, "maxW": 2960},
                        "n1": {"x": 3040, "y": 0, "w": 420, "fill": "blue", "text": "Built from square primitives on a 48-unit grid. Colours from design/tokens.json. Generator: design/boards/logo.py in the repo."},
                        "n2": {"x": 3040, "y": 420, "w": 420, "fill": "blue", "text": "L6 is chosen (D38; L4 was the previous pick, D36). Asset files: design/logo/ in the repo (SVG, PNG icons 16–512, favicon.ico, og-image), generated by design/boards/export.py."}}}
    json.dump(canvas, open(ROOT + "/canvas.json", "w"), ensure_ascii=False, indent=1)
    return list(out)


if __name__ == "__main__":
    print(write_all())
