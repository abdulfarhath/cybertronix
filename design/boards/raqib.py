#!/usr/bin/env python3
"""Raqib boards (D32): R1 logo, R2 terminal app redesign, R3 local web view. Light + dark.
Panels and keys are exactly those in docs/reference/raqib-tui-current.png (D31: never invent features).
Numbers are sample data, labelled as such."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__)) + "/canvas/project"

T = {
    "dark": dict(bg="#0A0C10", panel="#10141B", border="#232B36", strong="#2E3846", text="#E8ECF2", t2="#B7C0CD", muted="#8A94A4",
                 acc="#3D7BFF", accSoft="#1A2333", alert="#FF8A3D", ok="#2BB5A6", track="#1A212B", link="#8FB2FF"),
    "light": dict(bg="#F3F5F8", panel="#FFFFFF", border="#D8DEE7", strong="#C5CDD8", text="#0F141B", t2="#3A4453", muted="#5A6475",
                  acc="#2457C8", accSoft="#E6EDFB", alert="#B9530F", ok="#0E7C70", track="#E4E9F0", link="#2457C8"),
}

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
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400;500;600&amp;family=Geist:wght@400;500&amp;family=JetBrains+Mono:wght@400;500;700&amp;display=swap" rel="stylesheet">
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


def page(title, w, h, bg, body):
    import re
    body = re.sub(r"border-radius: (?!50%)[^;\"]+", "border-radius: 0", body)
    body = re.sub(r"\b1px (solid|dashed)", r"2px \1", body)
    return HEAD.format(title=title, w=w, h=h, bg=bg, body=body)


def mark(size, c, acc, bg, opt="C"):
    """Three options, each drawn from Raqib's own UI (D33 rule 1).
    A Meter: the Vitals RAM bar inside a panel, with the alert line.
    B Panel: a TUI box whose title slot holds the watcher's eye.
    C Gauge: an eye drawn as a gauge."""
    o = f'<svg width="{size}" height="{size}" viewBox="0 0 48 48" role="img" aria-label="Raqib logo, option {opt}">'
    if opt == "A":
        o += (f'<rect x="3" y="3" width="42" height="42" fill="{bg}" stroke="{c}" stroke-width="3"/>'
              f'<rect x="10" y="20" width="28" height="8" fill="none" stroke="{c}" stroke-width="2"/>'
              f'<rect x="10" y="20" width="21" height="8" fill="{acc}"/>'
              f'<path d="M34 15 V33" stroke="{c}" stroke-width="3"/>')
    elif opt == "B":
        o += (f'<path d="M15 6 H3 V45 H45 V6 H33" fill="{bg}" stroke="{c}" stroke-width="3"/>'
              f'<circle cx="24" cy="6" r="5" fill="{acc}"/>'
              f'<path d="M11 20 H25 M11 28 H33 M11 36 H20" stroke="{c}" stroke-width="3"/>')
    else:
        o += (f'<rect x="3" y="3" width="42" height="42" fill="{bg}" stroke="{c}" stroke-width="3"/>'
              f'<path d="M10 30 A14 14 0 0 1 38 30" fill="none" stroke="{c}" stroke-width="3"/>'
              f'<circle cx="24" cy="30" r="5" fill="{acc}"/>'
              f'<path d="M24 30 L31 21" stroke="{c}" stroke-width="3"/>')
    return o + "</svg>"


def wordmark(px, k):
    return f'<span class="mono" style="font-size: {px}px; font-weight: 700; letter-spacing: -0.02em; color: {k["text"]}">raqib<span style="color: {k["acc"]}">_</span></span>'


def r1():
    stories = {"A": ("Meter", "The RAM bar from the Vitals panel, filled to the reading, with the alert line. Says: Raqib measures."),
               "B": ("Panel", "A Raqib terminal box. The watcher's eye sits in the title slot, over the process rows. Says: Raqib watches your processes."),
               "C": ("Gauge", "An eye drawn as a gauge: arc = load, pupil = the watcher. Says: Raqib = watcher.")}
    rows = ""
    for opt, (name, story) in stories.items():
        cells = ""
        for th in ("dark", "light"):
            k = T[th]
            sizes = "".join(f'<div style="display: flex; flex-direction: column; align-items: center; gap: 6px">{mark(sz, k["text"], k["acc"], k["panel"], opt)}<span class="mono" style="font-size: 10px; color: {k["muted"]}">{sz}</span></div>' for sz in (16, 32, 64))
            monov = mark(40, k["text"], k["text"], "none", opt)
            cells += f"""<div style="flex: 1; background: {k['bg']}; color: {k['text']}; padding: 24px 28px; display: flex; align-items: center; justify-content: space-between; gap: 20px; min-width: 0; border-left: 2px solid {k['border']}">
<div style="display: flex; align-items: center; gap: 16px">{mark(64, k['text'], k['acc'], k['panel'], opt)}{wordmark(30, k)}</div>
<div style="display: flex; align-items: flex-end; gap: 16px">{sizes}<div style="display: flex; flex-direction: column; align-items: center; gap: 6px">{monov}<span class="mono" style="font-size: 10px; color: {k['muted']}">mono</span></div></div>
</div>"""
        rows += f"""<div style="display: flex; border-bottom: 2px solid #232B36; min-height: 0; flex: 1">
<div style="width: 280px; flex-shrink: 0; box-sizing: border-box; padding: 28px 28px; background: #141A22; color: #E8ECF2; display: flex; flex-direction: column; gap: 8px; justify-content: center"><div class="mono" style="font-size: 12px; color: #8A94A4">Option {opt}</div><div class="disp" style="font-size: 22px; font-weight: 500">{name}</div><div style="font-size: 14px; line-height: 1.55; color: #B7C0CD">{story}</div></div>
{cells}</div>"""
    head = """<div style="padding: 28px 32px; background: #0A0C10; color: #E8ECF2; border-bottom: 2px solid #232B36; display: flex; justify-content: space-between; align-items: flex-end"><div><div class="mono" style="font-size: 12px; color: #8A94A4">[R1] Raqib logo · founder picks one (D33 rule 7)</div><div class="disp" style="font-size: 28px; font-weight: 500; margin-top: 8px">Three options, each drawn from Raqib's own screen</div></div><div class="mono" style="font-size: 12px; color: #8A94A4">simple mark ≤ 64 px · mono · favicon = 16 px · dark | light</div></div>"""
    body = f'<div style="width: 1440px; height: 1100px; display: flex; flex-direction: column; overflow: hidden; background: #0A0C10">{head}{rows}</div>'
    return page("Raqib logo options", 1440, 1100, "#0A0C10", body)


# ---------- shared sample data (illustrative; from the reference screenshot's layout) ----------
TOP_RAM = [("Isolated Web Co", "1.2 GB"), ("Isolated Web Co", "1.1 GB"), ("firefox", "904 MB"), ("Isolated Web Co", "796 MB"), ("brave", "700 MB")]
TOP_VRAM = [("brave", "255 MB"), ("firefox", "153 MB"), ("gnome-shell", "110 MB"), ("ptyxis", "45 MB"), ("nautilus", "22 MB")]
TOP_CPU = [("Isolated Web Co", "93.6%"), ("brave", "14.8%"), ("ptyxis", "4.6%"), ("gnome-shell", "1.9%"), ("firefox", "1.9%")]


def bar(pct, k, h=10, color=None):
    color = color or (k["alert"] if pct >= 90 else k["t2"])
    return f'<div style="flex: 1; height: {h}px; background: {k["track"]}; border-radius: 3px; overflow: hidden"><div style="width: {pct}%; height: 100%; background: {color}"></div></div>'


def tbox(title, inner, k, extra="", tc=None):
    """Terminal box with the title set into the top border."""
    return f'<div style="position: relative; border: 1px solid {k["strong"]}; border-radius: 6px; padding: 18px 16px 12px; {extra}"><span style="position: absolute; top: -10px; left: 12px; padding: 0 6px; background: {k["bg"]}; color: {tc or k["t2"]}; font-weight: 700">{title}</span>{inner}</div>'


def proc_rows(rows, k, sel=False):
    out = ""
    for i, (n, v) in enumerate(rows):
        hl = f"background: {k['accSoft']}; color: {k['text']};" if sel and i == 0 else ""
        out += f'<div style="display: flex; justify-content: space-between; padding: 2px 6px; border-radius: 3px; {hl}"><span>{n}</span><span style="color: {k["t2"]}">{v}</span></div>'
    return out


def r2(name):
    k = T[name]
    vit = f"""<div style="display: grid; grid-template-columns: 110px 1fr 240px; row-gap: 10px; column-gap: 14px; align-items: center">
<span style="color: {k['muted']}">RAM</span><div style="position: relative; flex: 1; display: flex">{bar(69, k)}<span title="Proposed: alert line at 90%" style="position: absolute; left: 90%; top: -4px; bottom: -4px; width: 2px; background: {k['alert']}"></span></div><span style="text-align: right">10.8/15.6 GB</span>
<span style="color: {k['muted']}">VRAM</span>{bar(18, k)}<span style="text-align: right">1114/6144 MB · 1 dev</span>
<span style="color: {k['muted']}">CPU load</span><span>1.09&#160;&#160;1.46&#160;&#160;1.48 <span style="color: {k['muted']}">(1/5/15 min)</span></span><span style="text-align: right">cpus: 12</span>
<span style="color: {k['muted']}">Processes</span><span>409 total · 0 AI workloads</span><span></span>
<span style="color: {k['muted']}">Thermal</span><span style="grid-column: 2 / 4; display: flex; gap: 22px; flex-wrap: wrap"><span>System zone <b>56.0°C</b></span><span>CPU package <b>55.0°C</b></span><span>TCPU_PCI <b>53.0°C</b></span><span>INT3400 <b>20.0°C</b></span></span>
</div>"""
    ai = f'<div style="height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px; color: {k["t2"]}"><span style="font-size: 28px; color: {k["muted"]}">◉</span><span style="font-weight: 700; color: {k["text"]}">No AI workloads detected.</span><span>Start one to begin monitoring.</span></div>'
    tops = "".join(tbox(t, proc_rows(r, k, sel=(i == 0)), k) for i, (t, r) in enumerate([("Top by RAM", TOP_RAM), ("Top by VRAM", TOP_VRAM), ("Top by CPU % · per core", TOP_CPU)]))
    keys = " · ".join(f'<span style="color: {k["acc"]}; font-weight: 700">{a}</span> {b}' for a, b in [("q", "quit"), ("j/k", "select"), ("k", "kill (confirm)"), ("h", "history"), ("?", "help")])
    body = f"""<div class="mono" style="width: 1440px; height: 900px; box-sizing: border-box; background: {k['bg']}; color: {k['text']}; font-size: 14px; line-height: 1.5; padding: 22px 26px; display: flex; flex-direction: column; gap: 22px">
<header style="display: flex; justify-content: space-between; align-items: center">
<div style="display: flex; align-items: center; gap: 14px">{mark(22, k['text'], k['acc'], k['panel'])}<b>raqib</b><span style="color: {k['muted']}">0 workloads · 0 degraded · web <span style="color: {k['link']}">localhost:7070</span> · ? help</span></div>
<span style="color: {k['muted']}"><span style="padding: 2px 8px; border: 2px solid {k['alert']}; color: {k['alert']}">Proposed design (D34)</span> · 21:55:25 · sample data</span></header>
{tbox("Vitals", vit, k)}
{tbox("AI workloads", ai, k, "flex: 1;")}
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px">{tops}</div>
{tbox("Activity", f'<span style="color: {k["muted"]}; font-style: italic">No recent activity.</span>', k)}
<footer style="color: {k['t2']}">{keys}</footer>
</div>"""
    return page(f"Raqib terminal app, {name}", 1440, 900, k["bg"], body)


def card(title, inner, k, extra=""):
    return f'<section style="background: {k["panel"]}; border: 1px solid {k["border"]}; border-radius: 16px; padding: 20px; display: flex; flex-direction: column; gap: 14px; {extra}"><h2 class="mono" style="margin: 0; font-size: 12px; font-weight: 500; letter-spacing: 0.06em; text-transform: uppercase; color: {k["muted"]}">{title}</h2>{inner}</section>'


def r3(name):
    k = T[name]
    def stat(lab, val, sub, pct=None):
        b = f'<div style="display: flex">{bar(pct, k, 8)}</div>' if pct is not None else ""
        return f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="font-size: 13px; color: {k["muted"]}">{lab}</div><div class="disp" style="font-size: 26px; font-weight: 500; color: {k["text"]}">{val}</div>{b}<div class="mono" style="font-size: 12px; color: {k["t2"]}">{sub}</div></div>'
    vit = f'<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 24px">{stat("RAM", "69%", "10.8 / 15.6 GB", 69)}{stat("VRAM", "18%", "1114 / 6144 MB · 1 device", 18)}{stat("CPU load", "1.09", "1.46 · 1.48 · 12 cpus")}{stat("Processes", "409", "0 AI workloads")}{stat("Hottest sensor", "56.0°C", "System zone")}</div>'
    therm = "".join(f'<div style="display: flex; justify-content: space-between; padding: 8px 0; border-top: 1px solid {k["border"]}"><span>{a}</span><span class="mono">{b}</span></div>' for a, b in [("System zone", "56.0°C"), ("CPU package", "55.0°C"), ("TCPU_PCI", "53.0°C"), ("INT3400", "20.0°C")])
    tl = lambda rows: "".join(f'<div style="display: flex; justify-content: space-between; padding: 8px 0; border-top: 1px solid {k["border"]}; font-size: 14px"><span>{n}</span><span class="mono" style="color: {k["t2"]}">{v}</span></div>' for n, v in rows)
    kill = f'<button type="button" style="height: 36px; padding: 0 14px; border-radius: 999px; border: 1px solid {k["strong"]}; background: transparent; color: {k["text"]}; font: inherit; font-size: 13px">Kill… (asks to confirm)</button>'
    body = f"""<div style="width: 1440px; height: 1040px; box-sizing: border-box; background: {k['bg']}; color: {k['text']}; display: flex; flex-direction: column">
<div style="height: 44px; display: flex; align-items: center; gap: 12px; padding: 0 16px; background: {k['panel']}; border-bottom: 1px solid {k['border']}"><span style="width: 10px; height: 10px; border-radius: 50%; background: {k['strong']}"></span><span style="width: 10px; height: 10px; border-radius: 50%; background: {k['strong']}"></span><span style="width: 10px; height: 10px; border-radius: 50%; background: {k['strong']}"></span><span class="mono" style="margin-left: 12px; padding: 6px 14px; border-radius: 8px; background: {k['bg']}; font-size: 12px; color: {k['t2']}">http://localhost:7070</span></div>
<div style="flex: 1; padding: 28px 40px; display: flex; flex-direction: column; gap: 20px; box-sizing: border-box">
<header style="display: flex; justify-content: space-between; align-items: center"><div style="display: flex; align-items: center; gap: 12px">{mark(32, k['text'], k['acc'], k['panel'])}{wordmark(24, k)}<span class="mono" style="padding: 6px 12px; border: 1px solid {k['strong']}; border-radius: 999px; font-size: 12px; color: {k['t2']}">Early build</span></div>
<div class="mono" style="font-size: 12px; color: {k['muted']}"><span style="padding: 2px 8px; border: 2px solid {k['alert']}; color: {k['alert']}">Proposed design (D34)</span> · 0 workloads · 0 degraded · updated 21:55:25 · sample data</div></header>
{card("Vitals", vit, k)}
<div style="display: grid; grid-template-columns: 2fr 1fr; gap: 20px">
{card("AI workloads", f'<div style="min-height: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; border: 1px dashed {k["strong"]}; border-radius: 12px"><b>No AI workloads detected.</b><span style="color: {k["t2"]}; font-size: 14px">Start one to begin monitoring.</span></div>', k)}
{card("Thermal", f'<div style="font-size: 14px">{therm}</div>', k)}
</div>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px">
{card("Top by RAM", tl(TOP_RAM), k)}{card("Top by VRAM", tl(TOP_VRAM), k)}{card("Top by CPU · per core", tl(TOP_CPU) + kill, k)}
</div>
{card("Activity", f'<span style="color: {k["muted"]}; font-style: italic; font-size: 14px">No recent activity.</span>', k)}
</div>
</div>"""
    return page(f"Raqib web view, {name}", 1440, 1040, k["bg"], body)


def write_all():
    out = {"R1-Raqib-logo.dc.html": (r1(), 1440, 1100, "[R1] Raqib logo: 3 options, dark + light")}
    for n in ("dark", "light"):
        out[f"R2-Raqib-tui-{n}.dc.html"] = (r2(n), 1440, 900, f"[R2] Raqib terminal app, {n}")
        out[f"R3-Raqib-web-{n}.dc.html"] = (r3(n), 1440, 1040, f"[R3] Raqib web view (localhost:7070), {n}")
    for f, (src, *_rest) in out.items():
        open(f"{ROOT}/{f}", "w").write(src)
    return {f: v[1:] for f, v in out.items()}


if __name__ == "__main__":
    print(write_all())
