#!/usr/bin/env python3
"""[B1] One-page brand guide (D33 rule 6), generated from design/tokens.json (rule 4)."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOK = json.load(open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "tokens.json")))
ROOT = HERE + "/canvas/project"
D, L = TOK["color"]["dark"], TOK["color"]["light"]
ACC, SIG = TOK["accent"], TOK["signal"]

# Cybertronix mark L6 "Sensor mast" (D38), simple level. {c} = ink, {a} = the one accent (the seeing eye); {f} unused.
LOGO = ('<svg width="{s}" height="{s}" viewBox="0 0 48 48" role="img" aria-label="Cybertronix logo">'
        '<rect x="6" y="13" width="36" height="6" fill="{c}"/><rect x="6" y="36" width="36" height="6" fill="{c}"/>'
        '<rect x="6" y="13" width="6" height="29" fill="{c}"/><rect x="36" y="13" width="6" height="7" fill="{c}"/>'
        '<rect x="36" y="35" width="6" height="7" fill="{c}"/><rect x="22" y="4" width="4" height="9" fill="{c}"/>'
        '<rect x="19" y="2" width="10" height="4" fill="{c}"/><rect x="14" y="21" width="8" height="8" fill="{c}"/>'
        '<rect x="26" y="21" width="8" height="8" fill="{a}"/></svg>')


def refresh_x(ink, acc, size):
    r = lambda x, y, w, h, c: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>'
    o = ""
    for (x, y, sx, sy) in ((3, 3, 1, 1), (45, 3, -1, 1), (3, 45, 1, -1), (45, 45, -1, -1)):
        o += r(x if sx > 0 else x - 12, y if sy > 0 else y - 4, 12, 4, ink) + r(x if sx > 0 else x - 4, y if sy > 0 else y - 12, 4, 12, ink)
    o += r(13, 13, 22, 5, ink) + r(13, 13, 5, 22, ink) + r(13, 30, 22, 5, ink) + r(26, 21, 6, 6, acc)
    return f'<svg width="{size}" height="{size}" viewBox="0 0 48 48" role="img" aria-label="Cybertronix refresh option X">{o}</svg>'


def refresh_y(ink, acc, size):
    pts = [(24, 3), (42, 13.5), (42, 34.5), (24, 45), (6, 34.5), (6, 13.5)]
    segs = ""
    for i, (x, y) in enumerate(pts):
        for (nx, ny) in (pts[i - 1], pts[(i + 1) % 6]):
            segs += f'<line x1="{x}" y1="{y}" x2="{x + (nx - x) * 0.32:.1f}" y2="{y + (ny - y) * 0.32:.1f}" stroke="{ink}" stroke-width="4" stroke-linecap="square"/>'
    segs += f'<path d="M30 17 H18 V31 H30" fill="none" stroke="{ink}" stroke-width="4"/><rect x="26" y="21.5" width="5" height="5" fill="{acc}"/>'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 48 48" role="img" aria-label="Cybertronix refresh option Y">{segs}</svg>'


def h2(t, c):
    return f'<h2 class="disp" style="margin: 0; font-size: 20px; font-weight: 500; color: {c}">{t}</h2>'


def sw(hexv, name, txt, mut, border):
    return f'<div><div style="height: 48px; background: {hexv}; border: 2px solid {border}"></div><div style="font-size: 13px; margin-top: 6px; color: {txt}">{name}</div><div class="mono" style="font-size: 12px; color: {mut}">{hexv}</div></div>'


def build():
    dk = "".join(sw(v, k, D["text"], D["text-muted"], D["rule"]) for k, v in D.items())
    lt = "".join(sw(v, k, L["text"], L["text-muted"], L["rule"]) for k, v in L.items())
    logos = "".join(f'<div style="display: flex; flex-direction: column; align-items: center; gap: 8px">{LOGO.format(s=s, f=D["surface"], a=ACC["dark"], c=D["text"])}<span class="mono" style="font-size: 11px; color: {D["text-muted"]}">{s}px</span></div>' for s in (16, 32, 64, 96))
    mono = LOGO.format(s=64, f="none", a=D["text"], c=D["text"])
    mono_l = LOGO.format(s=64, f="none", a=L["text"], c=L["text"])
    sc = TOK["type"]["scale"]
    type_rows = "".join(f'<div style="display: flex; justify-content: space-between; align-items: baseline; padding: 10px 0; border-top: 2px solid {D["rule"]}"><span class="{cls}" style="font-size: {min(sc[k][0], 44)}px; line-height: 1.15; font-weight: {w}">{lab}</span><span class="mono" style="font-size: 12px; color: {D["text-muted"]}">{fam} {sc[k][0]}/{sc[k][1]}</span></div>'
                        for k, lab, cls, w, fam in [("h1", "Display / H1", "disp", 500, "Unbounded 500"), ("h2", "Section H2", "disp", 500, "Unbounded 500"), ("h3", "Card H3", "disp", 500, "Unbounded 500"),
                                                   ("lead", "Lead paragraph", "", 400, "Geist 400"), ("body", "Body text", "", 400, "Geist 400"), ("label", "MONO LABEL · DATA", "mono", 400, "JetBrains Mono 400")])
    do = ["Say the real status: Prototype, In development, Built to order, Early build.", "Use blue only where someone can act.", "Keep corners square and rules 2 px.",
          "Leave a visible TODO(founder) when a fact is missing.", "Caption stock footage as illustration."]
    dont = ["Invent clients, logos, numbers, faces, prices or years.", "Use blue or orange for decoration or long text.", "Round corners, shadows, gradients on UI.",
            "Put the H1 or any text inside a video or image.", "Animate anything except the P1 hero head-turn."]
    li = lambda xs, c, mark: "".join(f'<li style="display: flex; gap: 10px; padding: 8px 0; border-top: 2px solid {L["rule"]}"><span class="mono" style="color: {c}; font-weight: 500">{mark}</span><span>{x}</span></li>' for x in xs)
    body = f"""<div style="width: 1440px; height: 1960px; box-sizing: border-box; background: {D['bg']}; color: {D['text']}; display: flex; flex-direction: column">
<header style="padding: 56px 80px 40px; border-bottom: 2px solid {D['rule']}; display: flex; justify-content: space-between; align-items: flex-end">
<div style="display: flex; flex-direction: column; gap: 12px"><div class="mono" style="font-size: 12px; color: {D['text-muted']}">[B1] · one-page brand guide · source: design/tokens.json</div><h1 class="disp" style="margin: 0; font-size: 44px; font-weight: 500">Cybertronix · Midnight Lab</h1></div>
<div style="font-size: 15px; color: {D['text-2']}; max-width: 460px; line-height: 1.6">Dark cinematic hero, calm technical sections with blueprint grid lines. Square, honest, one accent.</div></header>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0">
<section style="padding: 40px 80px; border-right: 2px solid {D['rule']}; border-bottom: 2px solid {D['rule']}; display: flex; flex-direction: column; gap: 20px">{h2("Logo", D['text'])}
<div style="display: flex; align-items: center; gap: 18px">{LOGO.format(s=72, f=D['surface'], a=ACC['dark'], c=D['text'])}<span class="disp" style="font-size: 34px; font-weight: 600; letter-spacing: -0.02em">cybertronix</span></div>
<div style="display: flex; align-items: flex-end; gap: 28px">{logos}</div>
<div style="display: flex; gap: 12px"><div style="padding: 16px; border: 2px solid {D['rule']}">{mono}</div><div style="padding: 16px; background: {L['bg']}; border: 2px solid {L['rule']}">{mono_l}</div><div style="font-size: 13px; color: {D['text-muted']}; line-height: 1.6; align-self: center">Mono versions. Chosen mark: L6 Sensor mast (D38).<br>Rules, sizes and lock-ups: logo canvas [L6] Final.<br>Files: design/logo/.</div></div>
</section>
<section style="padding: 40px 80px; border-bottom: 2px solid {D['rule']}; display: flex; flex-direction: column; gap: 20px">{h2("One accent, one meaning", D['text'])}
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px">
<div style="padding: 20px; border: 2px solid {D['rule']}; display: flex; flex-direction: column; gap: 12px"><div style="height: 56px; background: {ACC['button']['dark']}"></div><b>Blue = you can act</b><span style="font-size: 14px; color: {D['text-2']}; line-height: 1.55">Buttons, links, focus ring, the selected item. Never status or decoration.</span><span class="mono" style="font-size: 12px; color: {D['text-muted']}">{ACC['dark']} · button {ACC['button']['dark']} · light {ACC['light']}</span></div>
<div style="padding: 20px; border: 2px solid {D['rule']}; display: flex; flex-direction: column; gap: 12px"><div style="height: 56px; background: {SIG['dark']}"></div><b>Orange = attention</b><span style="font-size: 14px; color: {D['text-2']}; line-height: 1.55">Alerts and TODO(founder) chips only. Not an accent.</span><span class="mono" style="font-size: 12px; color: {D['text-muted']}">{SIG['dark']} · light {SIG['light']}</span></div>
</div>
<div style="display: flex; gap: 12px; align-items: center; flex-wrap: wrap"><a href="#b" style="padding: 16px 26px; background: {ACC['button']['dark']}; color: #FFFFFF; text-decoration: none; font-size: 15px; font-weight: 500">Primary action</a><a href="#b" style="padding: 16px 26px; border: 2px solid {D['rule-strong']}; color: {D['text']}; text-decoration: none; font-size: 15px">Secondary</a><a href="#b" style="font-size: 15px; color: {D['link']}">Text link</a><span class="mono" style="padding: 8px 14px; border: 2px solid {D['rule-strong']}; font-size: 12px; color: {D['text']}">Prototype · pilot partners welcome</span><span class="mono" style="font-size: 12px; padding: 2px 8px; border: 2px dashed {SIG['dark']}; color: {SIG['dark']}">TODO(founder)</span></div>
</section>
<section style="padding: 40px 80px; border-right: 2px solid {D['rule']}; border-bottom: 2px solid {D['rule']}; display: flex; flex-direction: column; gap: 16px">{h2("Dark colours", D['text'])}<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px">{dk}</div></section>
<section style="padding: 40px 80px; border-bottom: 2px solid {D['rule']}; display: flex; flex-direction: column; gap: 16px; background-color: {L['bg']}; background-image: linear-gradient({TOK['grid']['light']['major']} 1px,transparent 1px),linear-gradient(90deg,{TOK['grid']['light']['major']} 1px,transparent 1px),linear-gradient({TOK['grid']['light']['minor']} 1px,transparent 1px),linear-gradient(90deg,{TOK['grid']['light']['minor']} 1px,transparent 1px); background-size: 120px 120px,120px 120px,24px 24px,24px 24px">{h2("Light colours (spec tables, FAQ)", L['text'])}<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px">{lt}</div></section>
<section style="padding: 40px 80px; border-right: 2px solid {D['rule']}; border-bottom: 2px solid {D['rule']}; display: flex; flex-direction: column; gap: 12px">{h2("Type", D['text'])}<div>{type_rows}</div></section>
<section style="padding: 40px 80px; border-bottom: 2px solid {D['rule']}; display: flex; flex-direction: column; gap: 16px">{h2("Shape and layout", D['text'])}
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px">
<div style="height: 96px; border: 2px solid {D['rule-strong']}; display: flex; align-items: center; justify-content: center" class="mono">radius 0</div>
<div style="height: 96px; border-top: 2px solid {D['text']}; display: flex; align-items: center; justify-content: center" class="mono">2 px rules</div>
<div style="height: 96px; background-color: {D['bg']}; background-image: linear-gradient({TOK['grid']['dark']['line']} 1px,transparent 1px),linear-gradient(90deg,{TOK['grid']['dark']['line']} 1px,transparent 1px); background-size: 40px 40px; border: 2px solid {D['rule']}; display: flex; align-items: center; justify-content: center" class="mono">grid 40 px</div></div>
<div class="mono" style="font-size: 12px; color: {D['text-muted']}; line-height: 1.8">8 px base · container 1280 · 12 columns, 20 gap · gutter 80 / 20 phone · section 112 / 56 phone<br>Breakpoints 360 · 390 · 768 · 1024 · 1280 · 1440 · works on 360 px phones<br>Round shapes only for status dots and the play button (icons, not containers)</div></section>
</div>
<section style="flex: 1; padding: 40px 80px; background: {L['bg']}; color: {L['text']}; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 48px">
<div style="display: flex; flex-direction: column; gap: 14px">{h2("Tone", L['text'])}<p style="margin: 0; font-size: 16px; line-height: 1.6; color: {L['text-2']}">Plain, calm and specific. Short sentences. Say what is real today and what is not. No hype words ("revolutionary", "cutting-edge", "best in India"). Words come from <span class="mono">content/</span>, written by SEO Content.</p>
<p style="margin: 0; font-size: 15px; line-height: 1.6; color: {L['text']}; padding: 16px; background: {L['surface']}; border: 2px solid {L['rule']}">"Our AI vision prototype is designed to check gloves, masks, shoe covers and gowns on your existing CCTV."</p></div>
<div style="display: flex; flex-direction: column; gap: 10px">{h2("Do", L['text'])}<ul style="margin: 0; padding: 0; list-style: none; font-size: 15px; line-height: 1.5">{li(do, L['text'], "✓")}</ul></div>
<div style="display: flex; flex-direction: column; gap: 10px">{h2("Don't", L['text'])}<ul style="margin: 0; padding: 0; list-style: none; font-size: 15px; line-height: 1.5">{li(dont, SIG['light'], "✕")}</ul></div>
</section>
</div>"""
    src = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Cybertronix brand guide</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400;500;600&amp;family=Geist:wght@400;500&amp;family=JetBrains+Mono:wght@400;500&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{D['bg']};color:{D['text']};font-family:Geist,system-ui,sans-serif}}
a{{color:{D['link']}}}a:hover{{color:#C4D6FF}}
.mono{{font-family:'JetBrains Mono',monospace}}
.disp{{font-family:Unbounded,Geist,sans-serif}}
</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1440,"height":1960}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
"""
    open(ROOT + "/StyleGuide.dc.html", "w").write(src)
    return 1440, 1960


if __name__ == "__main__":
    print(build())
