#!/usr/bin/env python3
"""Raqib boards (D32-D34).
R1  logo: 3 options drawn from Raqib's own UI (D33), each with full + simple marks, mono, app icon, lock-ups.
R2  current terminal app, 1:1 replica (reference only; no username/hostname).
R2  proposed next terminal app, dark + light (labelled Proposed, D34).
R3  proposed local web view (localhost:7070), dark + light, same panels as R2.
Numbers and process names are sample data."""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__)) + "/canvas/project"

T = {
    "dark": dict(bg="#0A0C10", panel="#10141B", raised="#141A22", border="#232B36", strong="#2E3846", text="#E8ECF2", t2="#B7C0CD", muted="#8A94A4",
                 acc="#3D7BFF", accSoft="#1A2333", track="#1A212B", link="#8FB2FF", mid="#5B6576",
                 ok="#3FB950", warn="#D29922", crit="#F85149", warnSoft="#2B2210"),
    "light": dict(bg="#F3F5F8", panel="#FFFFFF", raised="#FFFFFF", border="#D8DEE7", strong="#C5CDD8", text="#0F141B", t2="#3A4453", muted="#5A6475",
                  acc="#2457C8", accSoft="#E6EDFB", track="#E4E9F0", link="#2457C8", mid="#9AA3B2",
                  ok="#1A7F37", warn="#9A6700", crit="#CF222E", warnSoft="#FFF1CC"),
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
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400;500;600&amp;family=Geist:wght@400;500;600&amp;family=JetBrains+Mono:wght@400;500;700&amp;display=swap" rel="stylesheet">
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
    body = re.sub(r"border-radius: (?!50%)[^;\"]+", "border-radius: 0", body)
    body = re.sub(r"\b1px (solid|dashed)", r"2px \1", body)
    return HEAD.format(title=title, w=w, h=h, bg=bg, body=body)


# ---------------------------------------------------------------- R1 marks
def svg(size, inner, label):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 48 48" role="img" aria-label="{label}">{inner}</svg>'


def rect(x, y, w, h, c):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>'


def mark_a(ink, mid, acc, full=True):
    """Panel + pulse: a Raqib terminal box (title-slot gap like the TUI border), a pulse line,
    and a row of workloads where only the watched one carries the accent."""
    o = rect(3, 3, 6, 4, ink) + rect(19, 3, 26, 4, ink) + rect(3, 3, 4, 42, ink) + rect(41, 3, 4, 42, ink) + rect(3, 41, 42, 4, ink)
    if full:
        o += f'<polyline points="9,19 15,19 18,12 22,25 25,19 39,19" fill="none" stroke="{ink}" stroke-width="2.5"/>'
        o += rect(10, 29, 7, 8, mid) + rect(20, 29, 7, 8, acc) + rect(30, 29, 7, 8, mid)
    else:
        o += f'<polyline points="9,18 16,18 19,12 23,24 26,18 39,18" fill="none" stroke="{ink}" stroke-width="3.5"/>'
        o += rect(10, 28, 12, 9, mid) + rect(26, 28, 12, 9, acc)
    return o


def mark_b(ink, mid, acc, full=True):
    """Brackets + dot: the detection-box corners around a watching eye."""
    t, L = (4, 13) if full else (5, 15)
    o = ""
    for (x, y, sx, sy) in ((3, 3, 1, 1), (45, 3, -1, 1), (3, 45, 1, -1), (45, 45, -1, -1)):
        hx = x if sx > 0 else x - L
        vy = y if sy > 0 else y - L
        o += rect(hx, y if sy > 0 else y - t, L, t, ink) + rect(x if sx > 0 else x - t, vy, t, L, ink)
    if full:
        o += rect(23, 12, 2, 5, mid) + rect(23, 31, 2, 5, mid) + rect(12, 23, 5, 2, mid) + rect(31, 23, 5, 2, mid)
        o += f'<circle cx="24" cy="24" r="6" fill="{acc}"/>'
    else:
        o += f'<circle cx="24" cy="24" r="8" fill="{acc}"/>'
    return o


def mark_c(ink, mid, acc, full=True):
    """Grid R + gauge: a monospace R built on the terminal cell grid; the bowl is a gauge stroke;
    the last cell of the leg is the reading, in the accent."""
    c, x0, y0 = 6, 9, 3
    cell = lambda cx, cy, col: rect(x0 + cx * c, y0 + cy * c, c, c, col)
    o = ""
    if full:
        for cy in range(7):
            for cx in range(5):
                o += rect(x0 + cx * c + 2.5, y0 + cy * c + 2.5, 1, 1, mid)
    for cy in range(7):
        o += cell(0, cy, ink)
    o += cell(1, 0, ink) + cell(2, 0, ink) + cell(1, 3, ink) + cell(2, 3, ink)
    o += f'<path d="M{x0 + 3 * c} {y0 + 3} A{1.5 * c} {1.5 * c} 0 0 1 {x0 + 3 * c} {y0 + 3 * c + 3}" fill="none" stroke="{ink}" stroke-width="{c}"/>'
    o += cell(2, 4, ink) + cell(3, 5, ink) + cell(4, 6, acc)
    return o


MARKS = {"A": mark_a, "B": mark_b, "C": mark_c}


def lockup(opt, k, size=40, by=True):
    m = svg(size, MARKS[opt](k["text"], k["mid"], k["acc"], size > 64), f"Raqib logo option {opt}")
    sub = f'<span style="font-size: {max(11, size // 3)}px; color: {k["muted"]}">by Cybertronix</span>' if by else ""
    return (f'<div style="display: flex; align-items: center; gap: {size // 3}px">{m}<div style="display: flex; flex-direction: column; gap: 2px">'
            f'<span class="mono" style="font-size: {int(size * 0.75)}px; font-weight: 700; line-height: 1; letter-spacing: -0.02em; color: {k["text"]}">raqib</span>{sub}</div></div>')


def r1():
    stories = {
        "A": ("Panel + pulse", "A Raqib panel seen whole: the box with its title-slot gap, a pulse line and a row of workloads. Only the watched workload is blue, the way Hostelzy's \"your bed\" is the only red."),
        "B": ("Brackets + dot", "The corner brackets of a detection box around a dot: something is being watched. Ties Raqib to Cybertronix's AI vision story."),
        "C": ("Grid R + gauge", "A monospace R built on the terminal's cell grid. The bowl is a gauge stroke; the last cell of the leg is the reading, in blue."),
    }
    D, Lt = T["dark"], T["light"]
    rows = ""
    for opt, (name, story) in stories.items():
        f = MARKS[opt]
        big_d = svg(128, f(D["text"], D["mid"], D["acc"], True), f"Raqib option {opt}, full, dark")
        big_l = svg(128, f(Lt["text"], Lt["mid"], Lt["acc"], True), f"Raqib option {opt}, full, light")
        smalls = "".join(f'<figure style="margin: 0; display: flex; flex-direction: column; align-items: center; gap: 6px">{svg(s, f(Lt["text"], Lt["mid"], Lt["acc"], False), f"{opt} {s}px")}<figcaption class="mono" style="font-size: 10px; color: {Lt["muted"]}">{s}</figcaption></figure>' for s in (16, 24, 32, 64))
        mono_l = svg(48, f(Lt["text"], Lt["text"], Lt["text"], False), f"{opt} mono")
        mono_d = svg(48, f(D["text"], D["text"], D["text"], False), f"{opt} mono dark")
        icon = f'<div style="width: 96px; height: 96px; background: #FFFFFF; border: 2px solid {Lt["border"]}; display: flex; align-items: center; justify-content: center">{svg(60, f(Lt["text"], Lt["mid"], Lt["acc"], False), "app icon")}</div>'
        icon_d = f'<div style="width: 96px; height: 96px; background: {D["bg"]}; border: 2px solid {D["border"]}; display: flex; align-items: center; justify-content: center">{svg(60, f(D["text"], D["mid"], D["acc"], False), "app icon dark")}</div>'
        rows += f"""<section style="display: grid; grid-template-columns: 300px 170px 170px 1fr; border-bottom: 2px solid {D['border']}">
<div style="padding: 28px; background: {D['raised']}; color: {D['text']}; display: flex; flex-direction: column; gap: 10px; border-right: 2px solid {D['border']}"><div class="mono" style="font-size: 12px; color: {D['muted']}">Option {opt}</div><h2 class="disp" style="margin: 0; font-size: 22px; font-weight: 500">{name}</h2><p style="margin: 0; font-size: 14px; line-height: 1.55; color: {D['t2']}">{story}</p></div>
<div style="background: {D['bg']}; display: flex; align-items: center; justify-content: center; border-right: 2px solid {D['border']}">{big_d}</div>
<div style="background: {Lt['bg']}; display: flex; align-items: center; justify-content: center; border-right: 2px solid {D['border']}">{big_l}</div>
<div style="background: {Lt['bg']}; padding: 24px 28px; display: grid; grid-template-columns: 1fr 1fr; gap: 18px 24px; align-items: center">
<div style="display: flex; align-items: flex-end; gap: 14px">{smalls}</div>
<div style="display: flex; align-items: center; gap: 12px">{mono_l}<div style="padding: 6px; background: {D['bg']}">{mono_d}</div><span class="mono" style="font-size: 10px; color: {Lt['muted']}">mono</span></div>
<div style="padding: 14px 16px; background: {Lt['panel']}; border: 2px solid {Lt['border']}">{lockup(opt, Lt, 40)}</div>
<div style="padding: 14px 16px; background: {D['bg']}; border: 2px solid {D['border']}">{lockup(opt, D, 40)}</div>
<div style="display: flex; gap: 12px; align-items: center">{icon}{icon_d}<span class="mono" style="font-size: 10px; color: {Lt['muted']}">app icon</span></div>
<div class="mono" style="font-size: 12px; color: {Lt['t2']}; display: flex; align-items: center; gap: 10px"><span style="padding: 4px 10px; background: {D['bg']}; color: {D['text']}">{svg(14, f(D["text"], D["mid"], D["acc"], False), "tab icon")} raqib</span>terminal tab</div>
</div>
</section>"""
    head = f"""<header style="padding: 28px; background: {D['bg']}; color: {D['text']}; border-bottom: 2px solid {D['border']}; display: flex; justify-content: space-between; align-items: flex-end; gap: 24px">
<div><div class="mono" style="font-size: 12px; color: {D['muted']}">[R1] Raqib logo · the founder picks one (D33)</div><h1 class="disp" style="margin: 8px 0 0; font-size: 28px; font-weight: 500">Three marks, each drawn from Raqib's own screen</h1></div>
<div class="mono" style="font-size: 12px; color: {D['muted']}; text-align: right; line-height: 1.7">full mark at 96 px and up · simple mark at 64 px and down · mono · app icon<br>one accent: blue = the thing Raqib is watching · square corners</div></header>"""
    body = f'<div style="width: 1440px; height: 1160px; display: flex; flex-direction: column; background: {D["bg"]}">{head}{rows}</div>'
    return page("Raqib logo options", 1440, 1160, D["bg"], body)


# ---------------------------------------------------------------- shared sample data
TOP_RAM = [("Isolated Web Co", "1.2 GB"), ("Isolated Web Co", "1.1 GB"), ("firefox", "904 MB"), ("Isolated Web Co", "796 MB"), ("brave", "700 MB")]
TOP_VRAM = [("brave", "255 MB"), ("firefox", "153 MB"), ("gnome-shell", "110 MB"), ("ptyxis", "45 MB"), ("nautilus", "22 MB")]
TOP_CPU = [("Isolated Web Co", "93.6%"), ("brave", "14.8%"), ("ptyxis", "4.6%"), ("gnome-shell", "1.9%"), ("firefox", "1.9%")]
WORK = [("ok", "model-server-a", "4121", "3.1 GB", "2.4 GB", "38%", "1h 12m", "▂▃▅▅▆▅▆"),
        ("warn", "embed-worker", "4377", "1.7 GB", "3.9 GB", "92%", "14m", "▅▆▇▇██▇")]


# ---------------------------------------------------------------- R2 replica (current app)
def r2_replica():
    bg, fg, line, hl, lab, key = "#24273A", "#E6E8F2", "#4A5A92", "#B8C0F0", "#9AA0BE", "#8FA8FF"
    box = lambda title, inner, extra="": f'<div style="position: relative; border: 1px solid {line}; padding: 16px 6px 8px; {extra}"><span style="position: absolute; top: -10px; left: 8px; padding: 0 6px; background: {bg}; color: {lab}">{title}</span>{inner}</div>'
    rows = lambda rs: "".join(f'<div style="display: grid; grid-template-columns: 1fr 120px"><span>{n}</span><span style="text-align: right; padding-right: 40%">{v}</span></div>' for n, v in rs)
    vit = f"""<div style="height: 14px; width: 68%; background: {hl}"></div>
<div>CPU load&#160;&#160;&#160;1.09 1.46 1.48&#160;&#160;&#160;&#160;cpus: 12</div>
<div style="display: flex; align-items: center"><div style="height: 14px; width: 18%; background: {hl}"></div><span style="margin-left: 23%">VRAM&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;1114/6144 MB (1 devices)</span></div>
<div>Processes&#160;&#160;&#160;409 total&#160;&#160;&#160;0 AI workloads</div>
<div><span style="color: {lab}">Thermal</span>&#160;&#160;&#160;&#160;&#160;System Zone: 56.0°C (acpitz)&#160;&#160;CPU Package: 55.0°C (x86_pkg_temp)&#160;&#160;2: 53.0°C (TCPU_PCI)&#160;&#160;1: 20.0°C (INT3400 Thermal)</div>"""
    body = f"""<div class="mono" style="position: relative; width: 1440px; height: 900px; box-sizing: border-box; background: {bg}; color: {fg}; font-size: 13px; line-height: 1.45; padding: 14px 18px; display: flex; flex-direction: column; gap: 18px">
<div style="display: flex; justify-content: space-between"><b>raqib · 0 workloads · 0 degraded · press ? for help · web: http://localhost:7070</b><span>21:55:25</span></div>
{box("Vitals", vit)}
{box(f'<b style="color: {key}">AI Workloads</b>', '<div style="padding: 10px"><b>No AI workloads detected. Start one to begin monitoring.</b></div>', "flex: 1;")}
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px">{box("Top processes (by RAM)", rows(TOP_RAM))}{box("Top processes (by VRAM)", rows(TOP_VRAM))}{box("Top processes (by CPU %, per-core)", rows(TOP_CPU))}</div>
{box("Activity", '<div style="padding: 10px 10px 30px; font-style: italic">No recent activity.</div>')}
<div><b style="color: {key}">q</b> quit · <b style="color: {key}">j/k</b> select · <b style="color: {key}">k</b> kill (confirm) · <b style="color: {key}">h</b> history · <b style="color: {key}">?</b> help</div>
<div style="position: absolute; right: 18px; bottom: 14px; padding: 6px 10px; background: #0A0C10; color: #E8ECF2; font-size: 12px">[R2] Current app, 1:1 replica · reference only · title bar removed for privacy</div>
</div>"""
    return page("Raqib current app, replica", 1440, 900, bg, body)


# ---------------------------------------------------------------- R2 proposed terminal
def state_color(s, k):
    return {"ok": k["ok"], "warn": k["warn"], "crit": k["crit"]}[s]


def tbar(pct, k):
    col = k["crit"] if pct >= 90 else k["warn"] if pct >= 75 else k["ok"]
    return (f'<div style="position: relative; flex: 1; height: 12px; background: {k["track"]}">'
            f'<div style="width: {pct}%; height: 100%; background: {col}"></div>'
            f'<span style="position: absolute; left: 75%; top: -3px; bottom: -3px; width: 2px; background: {k["warn"]}"></span>'
            f'<span style="position: absolute; left: 90%; top: -3px; bottom: -3px; width: 2px; background: {k["crit"]}"></span></div>')


def prop(k):
    return f'<span style="margin-left: 8px; padding: 0 6px; border: 1px solid {k["acc"]}; color: {k["acc"]}; font-weight: 400; font-size: 11px">Proposed</span>'


def tbox(title, inner, k, extra="", tag=True):
    return (f'<div style="position: relative; border: 1px solid {k["strong"]}; padding: 18px 14px 10px; {extra}">'
            f'<span style="position: absolute; top: -11px; left: 10px; padding: 0 6px; background: {k["bg"]}; color: {k["text"]}; font-weight: 700">{title}{prop(k) if tag else ""}</span>{inner}</div>')


def temp(t, k):
    c = k["crit"] if t >= 85 else k["warn"] if t >= 70 else k["ok"]
    return f'<b style="color: {c}">{t:.1f}°C</b>'


ACTIVITY = [("21:54:02", "warn", "▲", "embed-worker CPU above 90% for 60 s"), ("21:41:17", "ok", "●", "model-server-a started · 3.1 GB VRAM")]


def r2(name):
    k = T[name]
    vit = f"""<div style="display: grid; grid-template-columns: 90px 1fr 190px 110px; row-gap: 10px; column-gap: 14px; align-items: center">
<span style="color: {k['muted']}">RAM</span>{tbar(69, k)}<span style="text-align: right">69% · 10.8/15.6 GB</span><span style="color: {k['muted']}">▃▄▄▅▅▆▆</span>
<span style="color: {k['muted']}">VRAM</span>{tbar(78, k)}<span style="text-align: right; color: {k['warn']}">78% · 4.8/6.1 GB</span><span style="color: {k['muted']}">▂▃▅▆▆▇▇</span>
<span style="color: {k['muted']}">CPU load</span><span>1.09&#160;&#160;1.46&#160;&#160;1.48 <span style="color: {k['muted']}">· 1/5/15 min · 12 cpus</span></span><span></span><span style="color: {k['muted']}">▂▂▃▃▂▃▃</span>
<span style="color: {k['muted']}">Thermal</span><span style="grid-column: 2 / 5; display: flex; gap: 24px">system {temp(56, k)}&#160;cpu pkg {temp(55, k)}&#160;pci {temp(53, k)}&#160;int3400 {temp(20, k)}</span>
</div>"""
    cols = "28px 1.6fr 70px 90px 90px 70px 90px 1fr"
    hdr = "".join(f'<span>{h}</span>' for h in ("", "PROCESS", "PID", "VRAM", "RAM", "CPU", "UPTIME", "LAST 60 s"))
    wrows = ""
    for i, (s, n, pid, vr, ram, cpu, up, sp) in enumerate(WORK):
        c = state_color(s, k)
        sym = "●" if s == "ok" else "▲"
        sel = f"background: {k['accSoft']}; outline: 2px solid {k['acc']};" if i == 1 else ""
        label = "ok" if s == "ok" else "degraded: CPU"
        cpu_c = c if s != "ok" else k["text"]
        wrows += (f'<div style="display: grid; grid-template-columns: {cols}; gap: 10px; padding: 6px 8px; {sel}"><span style="color: {c}">{sym}</span>'
                  f'<span>{n} <span style="color: {c}">{label}</span></span><span style="color: {k["muted"]}">{pid}</span><span>{vr}</span><span>{ram}</span>'
                  f'<span style="color: {cpu_c}">{cpu}</span><span>{up}</span><span style="color: {c}">{sp}</span></div>')
    work = f'<div style="display: grid; grid-template-columns: {cols}; gap: 10px; padding: 0 8px 6px; color: {k["muted"]}; font-size: 12px">{hdr}</div>{wrows}'
    empty = f'<div style="margin-top: 14px; max-width: 860px; padding: 10px 12px; border: 1px dashed {k["strong"]}; color: {k["t2"]}"><b style="color: {k["text"]}">Empty state:</b> No AI workloads yet. Start your model server and Raqib picks it up. Press <span style="color: {k["acc"]}">?</span> to see what counts as a workload.</div>'
    modal = (f'<div style="position: absolute; right: 40px; top: 250px; width: 420px; background: {k["bg"]}; border: 2px solid {k["crit"]}; padding: 14px 16px; display: flex; flex-direction: column; gap: 8px">'
             f'<b style="color: {k["crit"]}">Kill embed-worker (pid 4377)?</b><span style="color: {k["t2"]}">Frees about 1.7 GB VRAM and 3.9 GB RAM.</span>'
             f'<span><b style="color: {k["crit"]}">y</b> kill&#160;&#160;&#160;<b style="color: {k["acc"]}">n</b> / esc cancel</span></div>')
    tops = "".join(tbox(t, "".join(f'<div style="display: flex; justify-content: space-between; padding: 1px 0"><span>{n}</span><span style="color: {k["t2"]}">{v}</span></div>' for n, v in r), k, tag=False)
                   for t, r in [("Top by RAM", TOP_RAM), ("Top by VRAM", TOP_VRAM), ("Top by CPU · per core", TOP_CPU)])
    act = "".join(f'<div><span style="color: {k["muted"]}">{t}</span>&#160;&#160;<span style="color: {k[s]}">{sym}</span>&#160;{m}</div>' for t, s, sym, m in ACTIVITY)
    keys = " · ".join(f'<b style="color: {k["acc"]}">{a}</b> {b}' for a, b in [("q", "quit"), ("j/k", "select"), ("k", "kill (confirm)"), ("h", "history"), ("?", "help")])
    status = f'<span style="padding: 2px 10px; background: {k["warnSoft"]}; color: {k["warn"]}; font-weight: 700">▲ DEGRADED</span>'
    legend = " ".join(f'<span style="color: {c}">{s} {l}</span>' for s, c, l in (("●", k["ok"], "ok"), ("▲", k["warn"], "degraded"), ("■", k["crit"], "critical"), ("▌", k["acc"], "selected")))
    body = f"""<div class="mono" style="position: relative; width: 1440px; height: 900px; box-sizing: border-box; background: {k['bg']}; color: {k['text']}; font-size: 13px; line-height: 1.5; padding: 18px 24px; display: flex; flex-direction: column; gap: 20px">
<header style="display: flex; justify-content: space-between; align-items: center"><div style="display: flex; align-items: center; gap: 12px">{svg(16, mark_c(k["text"], k["mid"], k["acc"], False), "Raqib")}<b>raqib</b>{status}<span style="color: {k['t2']}">2 workloads · 1 degraded · web <span style="color: {k['link']}">localhost:7070</span></span>{prop(k)}</div><span style="color: {k['muted']}">{legend} · 21:55:25 · sample data</span></header>
{tbox("Vitals", vit, k)}
{tbox("AI workloads · 2", work + empty, k, "flex: 1;")}
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px">{tops}</div>
{tbox("Activity", act, k)}
<footer style="display: flex; justify-content: space-between; color: {k['t2']}"><span>{keys}</span><span style="color: {k['muted']}">16-colour ANSI safe: green · yellow · red · blue · white · grey</span></footer>
{modal}
</div>"""
    return page(f"Raqib proposed terminal app, {name}", 1440, 900, k["bg"], body)


# ---------------------------------------------------------------- R3 proposed web view
def spark(points, color, w=120, h=28):
    n = len(points)
    pts = " ".join(f"{i * w / (n - 1):.0f},{h - p * h:.0f}" for i, p in enumerate(points))
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true"><polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2"/></svg>'


def r3(name):
    k = T[name]

    def card(title, inner, extra="", tag=True):
        return (f'<section style="background: {k["panel"]}; border: 2px solid {k["border"]}; padding: 18px 20px; display: flex; flex-direction: column; gap: 12px; {extra}">'
                f'<h2 class="mono" style="margin: 0; font-size: 12px; font-weight: 500; letter-spacing: 0.06em; text-transform: uppercase; color: {k["muted"]}">{title}{prop(k) if tag else ""}</h2>{inner}</section>')

    def stat(lab, val, sub, pct, pts):
        col = k["crit"] if pct and pct >= 90 else k["warn"] if pct and pct >= 75 else k["ok"]
        bar = f'<div style="display: flex">{tbar(pct, k)}</div>' if pct is not None else ""
        vc = col if pct else k["text"]
        return (f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 13px; color: {k["muted"]}">{lab}</span>{spark(pts, k["mid"], 90, 22)}</div>'
                f'<div class="disp" style="font-size: 26px; font-weight: 500; color: {vc}">{val}</div>{bar}<div class="mono" style="font-size: 12px; color: {k["t2"]}">{sub}</div></div>')

    vit = ('<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 28px">'
           + stat("RAM", "69%", "10.8 / 15.6 GB", 69, [.5, .55, .6, .6, .65, .68, .69])
           + stat("VRAM", "78%", "4.8 / 6.1 GB · 1 device", 78, [.3, .4, .55, .65, .7, .77, .78])
           + stat("CPU load", "1.09", "1.46 · 1.48 · 12 cpus", None, [.3, .35, .4, .38, .42, .4, .45])
           + stat("Processes", "409", "2 AI workloads", None, [.5, .5, .52, .5, .51, .5, .5]) + "</div>")
    th = lambda t: f'<th scope="col" class="mono" style="text-align: left; padding: 8px 10px; font-size: 12px; font-weight: 400; color: {k["muted"]}; border-bottom: 2px solid {k["border"]}">{t}</th>'
    trs = ""
    for i, (s, n, pid, vr, ram, cpu, up, _sp) in enumerate(WORK):
        c = state_color(s, k)
        pts = [.4, .45, .5, .55, .5, .6, .58] if s == "ok" else [.6, .7, .85, .9, .95, .97, .92]
        sel = f"background: {k['accSoft']};" if i == 1 else ""
        lab = "● ok" if s == "ok" else "▲ degraded"
        cpu_c = c if s != "ok" else k["text"]
        trs += (f'<tr style="{sel}"><td style="padding: 10px; color: {c}; font-weight: 600">{lab}</td><td style="padding: 10px">{n}</td><td class="mono" style="padding: 10px; color: {k["muted"]}">{pid}</td>'
                f'<td class="mono" style="padding: 10px">{vr}</td><td class="mono" style="padding: 10px">{ram}</td><td class="mono" style="padding: 10px; color: {cpu_c}">{cpu}</td><td class="mono" style="padding: 10px">{up}</td>'
                f'<td style="padding: 10px">{spark(pts, c, 110, 22)}</td><td style="padding: 10px; text-align: right"><button type="button" style="height: 36px; padding: 0 14px; border: 2px solid {k["strong"]}; background: transparent; color: {k["text"]}; font: inherit; font-size: 13px">Kill…</button></td></tr>')
    table = f'<table style="width: 100%; border-collapse: collapse; font-size: 14px"><thead><tr>{"".join(th(t) for t in ("State", "Process", "PID", "VRAM", "RAM", "CPU", "Uptime", "Last 60 s", ""))}</tr></thead><tbody>{trs}</tbody></table>'
    confirm = (f'<div role="dialog" aria-label="Confirm kill" style="position: absolute; right: 20px; top: 100%; margin-top: -8px; width: 380px; background: {k["panel"]}; border: 2px solid {k["crit"]}; padding: 16px; display: flex; flex-direction: column; gap: 10px; z-index: 2">'
               f'<b style="color: {k["crit"]}">Kill embed-worker (pid 4377)?</b><span style="font-size: 14px; color: {k["t2"]}">Frees about 1.7 GB VRAM and 3.9 GB RAM.</span>'
               f'<div style="display: flex; gap: 10px"><button type="button" style="height: 40px; padding: 0 16px; border: none; background: {k["crit"]}; color: #FFFFFF; font: inherit; font-weight: 600">Kill process</button>'
               f'<button type="button" style="height: 40px; padding: 0 16px; border: 2px solid {k["acc"]}; background: transparent; color: {k["acc"]}; font: inherit">Cancel</button></div></div>')
    therm = "".join(f'<div style="display: flex; justify-content: space-between; padding: 8px 0; border-top: 2px solid {k["border"]}; font-size: 14px"><span>{a}</span>{temp(b, k)}</div>' for a, b in [("System zone", 56), ("CPU package", 55), ("TCPU_PCI", 53), ("INT3400", 20)])
    tl = lambda rows: "".join(f'<div style="display: flex; justify-content: space-between; padding: 7px 0; border-top: 2px solid {k["border"]}; font-size: 14px"><span>{n}</span><span class="mono" style="color: {k["t2"]}">{v}</span></div>' for n, v in rows)
    act = "".join(f'<div style="display: flex; gap: 14px; padding: 7px 0; border-top: 2px solid {k["border"]}; font-size: 14px"><span class="mono" style="color: {k["muted"]}">{t}</span><span style="color: {k[s]}">{sym}</span><span>{m}</span></div>' for t, s, sym, m in ACTIVITY)
    status = f'<span class="mono" style="padding: 6px 12px; background: {k["warnSoft"]}; color: {k["warn"]}; font-size: 13px; font-weight: 700">▲ DEGRADED · 1 of 2</span>'
    body = f"""<div style="width: 1440px; height: 1020px; box-sizing: border-box; background: {k['bg']}; color: {k['text']}; display: flex; flex-direction: column">
<div style="height: 44px; display: flex; align-items: center; gap: 12px; padding: 0 16px; background: {k['panel']}; border-bottom: 2px solid {k['border']}"><span class="mono" style="padding: 6px 14px; background: {k['bg']}; font-size: 12px; color: {k['t2']}">http://localhost:7070</span></div>
<div style="flex: 1; padding: 28px 40px; display: flex; flex-direction: column; gap: 20px">
<header style="display: flex; justify-content: space-between; align-items: center"><div style="display: flex; align-items: center; gap: 16px">{lockup("C", k, 32, by=False)}{status}{prop(k)}</div><div class="mono" style="font-size: 12px; color: {k['muted']}">same data and panels as the terminal app · updated 21:55:25 · sample data</div></header>
{card("Vitals", vit)}
<div style="position: relative">{card("AI workloads · 2", table)}{confirm}</div>
<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 20px">{card("Thermal", therm)}{card("Top by RAM", tl(TOP_RAM), tag=False)}{card("Top by VRAM", tl(TOP_VRAM), tag=False)}{card("Top by CPU · per core", tl(TOP_CPU), tag=False)}</div>
{card("Activity", act)}
</div>
</div>"""
    return page(f"Raqib proposed web view, {name}", 1440, 1020, k["bg"], body)


def write_all():
    out = {"R1-Raqib-logo.dc.html": (r1(), 1440, 1160, "[R1] Raqib logo: options A, B, C"),
           "R2-Raqib-tui-current.dc.html": (r2_replica(), 1440, 900, "[R2] Current app, 1:1 replica (reference)")}
    for n in ("dark", "light"):
        out[f"R2-Raqib-tui-{n}.dc.html"] = (r2(n), 1440, 900, f"[R2] Proposed terminal app, {n}")
    for n in ("dark", "light"):
        out[f"R3-Raqib-web-{n}.dc.html"] = (r3(n), 1440, 1020, f"[R3] Proposed web view (localhost:7070), {n}")
    for f, (src, *_r) in out.items():
        open(f"{ROOT}/{f}", "w").write(src)
    return {f: v[1:] for f, v in out.items()}


if __name__ == "__main__":
    print(write_all())
