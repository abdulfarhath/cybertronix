#!/usr/bin/env python3
"""Final logo rule boards (D36 Cybertronix L4, D37 Raqib A): clear space, minimum sizes,
colour versions, lock-ups, and (Cybertronix) the proposed nav tie-in to the hero head-turn."""
import os, re, sys

REPO = os.environ.get("CYX_REPO", "/home/user/cybertronix")
sys.path.insert(0, os.path.join(REPO, "design", "boards"))
import export as X  # noqa: E402  (BRANDS, VERSIONS, svg_mark, svg_lockup, pix_svg, logo, raqib)

D, L = X.D, X.L

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
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400;500;600&amp;family=Geist:wght@400;500;600&amp;family=JetBrains+Mono:wght@400;500;700&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0;background:#0A0C10;font-family:Geist,system-ui,sans-serif}}
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


def sized(svg, w=None, h=None):
    """Inline an export SVG at a given display size (drops xmlns, sets width/height)."""
    svg = svg.replace(' xmlns="http://www.w3.org/2000/svg"', "").strip()
    svg = re.sub(r'<!--.*?-->', "", svg)
    if w is not None:
        svg = re.sub(r'width="[\d.]+"', f'width="{w}"', svg, 1)
    if h is not None:
        svg = re.sub(r'height="[\d.]+"', f'height="{h}"', svg, 1)
    elif w is not None:
        vb = re.search(r'viewBox="([-\d. ]+)"', svg).group(1).split()
        svg = re.sub(r'height="[\d.]+"', f'height="{float(w) * float(vb[3]) / float(vb[2]):.0f}"', svg, 1)
    return svg.replace("<svg ", '<svg style="display: block" ', 1)


def cap(t, dark=False):
    return f'<span class="mono" style="font-size: 11px; color: {D["text-muted"] if dark else L["text-muted"]}">{t}</span>'


def h2(t):
    return f'<h2 class="disp" style="margin: 0; font-size: 18px; font-weight: 500; color: {L["text"]}">{t}</h2>'


def eyes_forward(ink, mid, eye):
    """Cybertronix head before the turn: eyes centred (frame 1 of the proposed nav tie-in)."""
    lg = X.logo
    return lg.chead(6, c=ink) + lg.r(14, 17, 8, 8, ink) + lg.r(26, 17, 8, 8, eye)


def board(key, lid, decision, story):
    b = X.BRANDS[key]
    V = X.VERSIONS
    full = lambda v, s: sized(X.svg_mark(b["mark"](V[v][0], V[v][1], V[v][2], True), s), s)  # no ground: the tile is the ground
    simple = lambda v, s: sized(X.svg_mark(b["mark"](V[v][0], V[v][1], V[v][2], False), s), s)
    pix = lambda v, s: sized(X.pix_svg(key, V[v][0], V[v][1], V[v][2], s), s)
    # clear space: x = 1/6 of the mark (8 of 48 units)
    clear = (f'<div style="position: relative; width: 240px; height: 240px; background: {L["surface"]}; border: 2px solid {L["rule"]}; display: flex; align-items: center; justify-content: center">'
             f'<div style="position: relative; padding: 30px; outline: 2px dashed {X.TOK["signal"]["light"]}; outline-offset: 0">{full("light", 120)}'
             f'<span class="mono" style="position: absolute; left: 6px; top: 4px; font-size: 11px; color: {X.TOK["signal"]["light"]}">x</span>'
             f'<span class="mono" style="position: absolute; right: 6px; bottom: 4px; font-size: 11px; color: {X.TOK["signal"]["light"]}">x</span></div></div>')
    tiles = ""
    for v, label in (("dark", "Dark"), ("light", "Light"), ("mono-black", "Mono black"), ("mono-white", "Mono white"), ("on-accent", "On accent")):
        bg = V[v][3] or ("#FFFFFF" if v == "mono-black" else D["bg"])
        tiles += (f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="height: 150px; background: {bg}; border: 2px solid {L["rule"]}; display: flex; align-items: center; justify-content: center">{full(v, 96)}</div>{cap(label)}</div>')
    lock = lambda v, st, w: sized(X.svg_lockup(b, v, st), w)
    lockups = (f'<div style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 14px">'
               f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="padding: 28px; background: {L["bg"]}; border: 2px solid {L["rule"]}">{lock("light", False, 380)}</div>'
               f'<div style="padding: 28px; background: {D["bg"]}; border: 2px solid {D["rule"]}">{lock("dark", False, 380)}</div>{cap("Horizontal · default")}</div>'
               f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="flex: 1; padding: 20px; background: {L["bg"]}; border: 2px solid {L["rule"]}; display: flex; align-items: center; justify-content: center">{lock("light", True, 170)}</div>{cap("Stacked · square spaces")}</div>'
               f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="flex: 1; padding: 20px; background: {D["bg"]}; border: 2px solid {D["rule"]}; display: flex; align-items: center; justify-content: center">{full("dark", 112)}</div>{cap("Mark only · icons, avatars")}</div></div>')
    mins = (f'<div style="display: flex; align-items: flex-end; gap: 28px; padding: 20px; background: {L["bg"]}; border: 2px solid {L["rule"]}">'
            f'<div style="display: flex; flex-direction: column; gap: 6px; align-items: center">{pix("light", 16)}{cap("16 px pixel mark")}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 6px; align-items: center">{pix("light", 32)}{cap("32 px = 2× pixel")}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 6px; align-items: center">{simple("light", 48)}{cap("48–64 px simple")}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 6px; align-items: center">{full("light", 96)}{cap("96 px and up: full")}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 6px">{lock("light", False, 120)}{cap("lock-up min 120 px wide")}</div></div>')
    tie = ""
    if key == "cybertronix":
        k = X.VERSIONS["dark"]
        f1 = sized(X.svg_mark(eyes_forward(k[0], k[1], k[2]), 40), 40)
        f2 = simple("dark", 40)
        nav = lambda m, note: (f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="display: flex; align-items: center; gap: 12px; padding: 14px 18px; background: {D["bg"]}; border: 2px solid {D["rule"]}">'
                               f'{m}<span class="disp" style="font-size: 18px; font-weight: 600; color: {D["text"]}">cybertronix</span>'
                               f'<span style="margin-left: auto; font-size: 13px; color: {D["text-2"]}">AI vision · Cleaning robot · …</span></div>{cap(note)}</div>')
        tie = (f'<section style="display: flex; flex-direction: column; gap: 12px">{h2("Hero tie-in")}'
               f'<div style="display: flex; gap: 10px; align-items: center"><span class="mono" style="padding: 2px 8px; border: 2px solid {X.ACC_L}; color: {X.ACC_L}; font-size: 11px">Proposed</span>'
               f'<span style="font-size: 14px; color: {L["text-2"]}">The nav eyes shift once when the P1 hero head turns. One move, no loop, nothing with prefers-reduced-motion (D10).</span></div>'
               f'<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px">{nav(f1, "Frame 1 · page load: eyes ahead")}{nav(f2, "Frame 2 · after the hero head-turn: eyes look out (L4)")}</div></section>')
    name = "Cybertronix · L4 Head-turn" if key == "cybertronix" else "Raqib · A Panel + pulse"
    H = 1500 if key == "cybertronix" else 1340
    body = f"""<div style="width: 1440px; height: {H}px; box-sizing: border-box; background: {L['bg']}; display: flex; flex-direction: column">
<header style="padding: 32px; background: {D['bg']}; color: {D['text']}; display: flex; gap: 40px; align-items: center; border-bottom: 2px solid {D['rule']}">
{full("dark", 120)}
<div style="display: flex; flex-direction: column; gap: 10px"><div style="display: flex; gap: 12px; align-items: center"><span class="mono" style="font-size: 12px; color: {D['text-muted']}">[{lid}] Final</span><span class="mono" style="padding: 3px 10px; background: {X.ACC_D}; color: #FFFFFF; font-size: 12px">Chosen ({decision})</span></div>
<h1 class="disp" style="margin: 0; font-size: 32px; font-weight: 500">{name}</h1><p style="margin: 0; font-size: 16px; color: {D['text-2']}; line-height: 1.55; max-width: 900px">{story}</p>
<span class="mono" style="font-size: 12px; color: {D['text-muted']}">Asset files: {b['dir']}/ · SVG, PNG icons 16–512, favicon.ico, og-image · generated by design/boards/export.py</span></div></header>
<div style="padding: 32px; display: flex; flex-direction: column; gap: 28px">
<div style="display: grid; grid-template-columns: 300px 1fr; gap: 32px">
<section style="display: flex; flex-direction: column; gap: 12px">{h2("Clear space")}{clear}<span style="font-size: 14px; color: {L['text-2']}; line-height: 1.5">Keep x = one sixth of the mark's width clear on every side. Nothing else enters the dashed box.</span></section>
<section style="display: flex; flex-direction: column; gap: 12px">{h2("Minimum sizes and detail levels")}{mins}
<span style="font-size: 14px; color: {L['text-2']}; line-height: 1.5">16 and 32 px use the hand-drawn pixel mark. 48–64 px use the simple mark. 96 px and up use the full mark. Never smaller than 16 px.</span></section></div>
<section style="display: flex; flex-direction: column; gap: 12px">{h2("Colour versions")}<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 14px">{tiles}</div>
<span style="font-size: 14px; color: {L['text-2']}">Only one element is ever blue. In mono versions it takes the ink colour; on the accent ground it turns ink-dark.</span></section>
<section style="display: flex; flex-direction: column; gap: 12px">{h2("Lock-ups")}{lockups}</section>
{tie}
</div>
</div>"""
    body = re.sub(r"border-radius: (?!50%)[^;\"]+", "border-radius: 0", body)
    return HEAD.format(title=f"{lid} final", w=1440, h=H, body=body), H


STORIES = {
    "cybertronix": ("L4", "D36", "A machine that sees. The C is a robot's head; its eyes have turned to look out through the opening. Only the leading eye is blue. It echoes the hero head-turn."),
    "raqib": ("R1", "D37", "A Raqib panel seen whole: the terminal box with its title-slot gap, a pulse line and a row of workloads. Only the watched workload is blue."),
}

if __name__ == "__main__":
    for k, (lid, dec, st) in STORIES.items():
        src, h = board(k, lid, dec, st)
        print(k, h, len(src))
