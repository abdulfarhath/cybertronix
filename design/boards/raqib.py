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
    return HEAD.format(title=title, w=w, h=h, bg=bg, body=body)


def mark(size, c, acc, bg):
    """Raqib mark: a watchful eye drawn as a gauge. Arc = load, pupil = the watcher."""
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 48 48" role="img" aria-label="Raqib logo">'
            f'<rect x="2" y="2" width="44" height="44" rx="12" fill="{bg}" stroke="{c}" stroke-width="2.5"/>'
            f'<path d="M10 28 A14 14 0 0 1 38 28" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round"/>'
            f'<path d="M10 28 A14 14 0 0 1 30.5 15.6" fill="none" stroke="{acc}" stroke-width="3" stroke-linecap="round"/>'
            f'<circle cx="24" cy="28" r="5" fill="{acc}"/>'
            f'<path d="M24 28 L31 19" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/></svg>')


def wordmark(px, k):
    return f'<span class="mono" style="font-size: {px}px; font-weight: 700; letter-spacing: -0.02em; color: {k["text"]}">raqib<span style="color: {k["acc"]}">_</span></span>'


def r1():
    halves = ""
    for name in ("dark", "light"):
        k = T[name]
        sizes = "".join(f'<div style="display: flex; flex-direction: column; align-items: center; gap: 8px">{mark(s, k["text"], k["acc"], k["panel"])}<span class="mono" style="font-size: 11px; color: {k["muted"]}">{s}px</span></div>' for s in (16, 24, 32, 48, 96))
        halves += f"""<section aria-label="Raqib logo, {name}" style="flex: 1; background: {k['bg']}; padding: 56px; display: flex; flex-direction: column; gap: 40px; color: {k['text']}">
<div class="mono" style="font-size: 12px; color: {k['muted']}">[R1] {name}</div>
<div style="display: flex; align-items: center; gap: 24px">{mark(120, k['text'], k['acc'], k['panel'])}{wordmark(72, k)}</div>
<div style="display: flex; align-items: flex-end; gap: 28px; padding: 24px; border: 1px solid {k['border']}; border-radius: 16px; background: {k['panel']}">{sizes}</div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px">
<div style="padding: 20px; border: 1px solid {k['border']}; border-radius: 16px; background: {k['panel']}; display: flex; align-items: center; gap: 12px">{mark(32, k['text'], k['acc'], k['bg'])}{wordmark(22, k)}<span class="mono" style="font-size: 12px; color: {k['muted']}">· by Cybertronix</span></div>
<div class="mono" style="padding: 20px; border: 1px solid {k['border']}; border-radius: 16px; background: {k['panel']}; font-size: 14px; color: {k['t2']}; line-height: 1.6"><span style="color: {k['acc']}; font-weight: 700">[◉]</span> raqib <span style="color: {k['muted']}">· mark in the TUI title bar</span></div>
</div>
</section>"""
    note = """<div style="background: #141A22; color: #B7C0CD; padding: 28px 56px; font-size: 15px; line-height: 1.6; border-top: 1px solid #232B36">
<strong style="color: #E8ECF2">Idea:</strong> Raqib means "watcher". The mark is an eye drawn as a gauge: the arc is load (blue = used), the pupil is the watcher, the needle points at the current reading. Lower-case mono wordmark with a blinking-cursor underscore ties it to the terminal. Works at 16px as a favicon and as a box-drawing glyph in the TUI title.
</div>"""
    body = f'<div style="width: 1440px; height: 900px; display: flex; flex-direction: column; overflow: hidden"><div style="flex: 1; display: flex">{halves}</div>{note}</div>'
    return page("Raqib logo", 1440, 900, "#0A0C10", body)


# ---------- shared sample data (illustrative; from the reference screenshot's layout) ----------
TOP_RAM = [("Isolated Web Co", "1.2 GB"), ("Isolated Web Co", "1.1 GB"), ("firefox", "904 MB"), ("Isolated Web Co", "796 MB"), ("brave", "700 MB")]
TOP_VRAM = [("brave", "255 MB"), ("firefox", "153 MB"), ("gnome-shell", "110 MB"), ("ptyxis", "45 MB"), ("nautilus", "22 MB")]
TOP_CPU = [("Isolated Web Co", "93.6%"), ("brave", "14.8%"), ("ptyxis", "4.6%"), ("gnome-shell", "1.9%"), ("firefox", "1.9%")]


def bar(pct, k, h=10, color=None):
    color = color or (k["alert"] if pct >= 90 else k["acc"])
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
<span style="color: {k['muted']}">RAM</span>{bar(69, k)}<span style="text-align: right">10.8/15.6 GB</span>
<span style="color: {k['muted']}">VRAM</span>{bar(18, k)}<span style="text-align: right">1114/6144 MB · 1 dev</span>
<span style="color: {k['muted']}">CPU load</span><span>1.09&#160;&#160;1.46&#160;&#160;1.48 <span style="color: {k['muted']}">(1/5/15 min)</span></span><span style="text-align: right">cpus: 12</span>
<span style="color: {k['muted']}">Processes</span><span>409 total · <span style="color: {k['acc']}">0 AI workloads</span></span><span></span>
<span style="color: {k['muted']}">Thermal</span><span style="grid-column: 2 / 4; display: flex; gap: 22px; flex-wrap: wrap"><span>System zone <b>56.0°C</b></span><span>CPU package <b>55.0°C</b></span><span>TCPU_PCI <b>53.0°C</b></span><span>INT3400 <b>20.0°C</b></span></span>
</div>"""
    ai = f'<div style="height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px; color: {k["t2"]}"><span style="font-size: 28px; color: {k["muted"]}">◉</span><span style="font-weight: 700; color: {k["text"]}">No AI workloads detected.</span><span>Start one to begin monitoring.</span></div>'
    tops = "".join(tbox(t, proc_rows(r, k, sel=(i == 0)), k) for i, (t, r) in enumerate([("Top by RAM", TOP_RAM), ("Top by VRAM", TOP_VRAM), ("Top by CPU % · per core", TOP_CPU)]))
    keys = " · ".join(f'<span style="color: {k["acc"]}; font-weight: 700">{a}</span> {b}' for a, b in [("q", "quit"), ("j/k", "select"), ("k", "kill (confirm)"), ("h", "history"), ("?", "help")])
    body = f"""<div class="mono" style="width: 1440px; height: 900px; box-sizing: border-box; background: {k['bg']}; color: {k['text']}; font-size: 14px; line-height: 1.5; padding: 22px 26px; display: flex; flex-direction: column; gap: 22px">
<header style="display: flex; justify-content: space-between; align-items: center">
<div style="display: flex; align-items: center; gap: 14px">{mark(22, k['text'], k['acc'], k['panel'])}<b>raqib</b><span style="color: {k['muted']}">0 workloads · 0 degraded · web <span style="color: {k['link']}">localhost:7070</span> · ? help</span></div>
<span style="color: {k['muted']}">21:55:25 · sample data</span></header>
{tbox("Vitals", vit, k)}
{tbox("AI workloads", ai, k, "flex: 1;", k['acc'])}
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
    body = f"""<div style="width: 1440px; height: 1000px; box-sizing: border-box; background: {k['bg']}; color: {k['text']}; display: flex; flex-direction: column">
<div style="height: 44px; display: flex; align-items: center; gap: 12px; padding: 0 16px; background: {k['panel']}; border-bottom: 1px solid {k['border']}"><span style="width: 10px; height: 10px; border-radius: 50%; background: {k['strong']}"></span><span style="width: 10px; height: 10px; border-radius: 50%; background: {k['strong']}"></span><span style="width: 10px; height: 10px; border-radius: 50%; background: {k['strong']}"></span><span class="mono" style="margin-left: 12px; padding: 6px 14px; border-radius: 8px; background: {k['bg']}; font-size: 12px; color: {k['t2']}">http://localhost:7070</span></div>
<div style="flex: 1; padding: 28px 40px; display: flex; flex-direction: column; gap: 20px; box-sizing: border-box">
<header style="display: flex; justify-content: space-between; align-items: center"><div style="display: flex; align-items: center; gap: 12px">{mark(32, k['text'], k['acc'], k['panel'])}{wordmark(24, k)}<span class="mono" style="padding: 6px 12px; border: 1px solid {k['strong']}; border-radius: 999px; font-size: 12px; color: {k['t2']}">Early build</span></div>
<div class="mono" style="font-size: 12px; color: {k['muted']}">0 workloads · 0 degraded · updated 21:55:25 · sample data</div></header>
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
    return page(f"Raqib web view, {name}", 1440, 1000, k["bg"], body)


def write_all():
    out = {"R1-Raqib-logo.dc.html": (r1(), 1440, 900, "[R1] Raqib logo, dark + light")}
    for n in ("dark", "light"):
        out[f"R2-Raqib-tui-{n}.dc.html"] = (r2(n), 1440, 900, f"[R2] Raqib terminal app, {n}")
        out[f"R3-Raqib-web-{n}.dc.html"] = (r3(n), 1440, 1000, f"[R3] Raqib web view (localhost:7070), {n}")
    for f, (src, *_rest) in out.items():
        open(f"{ROOT}/{f}", "w").write(src)
    return {f: v[1:] for f, v in out.items()}


if __name__ == "__main__":
    print(write_all())
