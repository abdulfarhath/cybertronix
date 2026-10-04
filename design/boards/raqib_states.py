#!/usr/bin/env python3
"""Raqib app states R4-R11 (D39: the proposed design is approved as the direction for the next Raqib).
Each state has a terminal board and a web board; each board shows dark (top) and light (bottom).
Numbers and process names are sample data."""
import os, re

from raqib import T, tbar, temp, spark, svg, mark_a, lockup, TOP_RAM, TOP_VRAM, TOP_CPU, HEAD

LABEL = "Proposed · approved D39"


def tag(k):
    return f'<span style="margin-left: 8px; padding: 0 6px; border: 1px solid {k["acc"]}; color: {k["acc"]}; font-weight: 400; font-size: 11px; white-space: nowrap">{LABEL}</span>'


def C(k, s):
    return {"ok": k["ok"], "warn": k["warn"], "crit": k["crit"]}[s]


SYM = {"ok": "●", "warn": "▲", "crit": "■"}
WORD = {"ok": "OK", "warn": "DEGRADED", "crit": "CRITICAL"}

# ------------------------------------------------------------------ state data
BASE = dict(ram=(58, "9.1/15.6 GB"), vram=(52, "3.2/6.1 GB"), load="1.09  1.46  1.48", temps=[("system", 56), ("cpu pkg", 55), ("pci", 53), ("int3400", 20)],
            work=[("ok", "model-server-a", "4121", "3.1 GB", "2.4 GB", "38%", "1h 12m", "▂▃▅▅▆▅▆", "ok"),
                  ("ok", "embed-worker", "4377", "0.9 GB", "1.6 GB", "22%", "14m", "▂▂▃▂▃▃▂", "ok")],
            act=[("21:41:17", "ok", "model-server-a started · 3.1 GB VRAM"), ("21:41:52", "ok", "embed-worker started · 0.9 GB VRAM")],
            status="ok", view="main", overlay=None, sel=0, banner=None)
DEG = dict(BASE, ram=(69, "10.8/15.6 GB"), vram=(78, "4.8/6.1 GB"), status="warn", sel=1,
           work=[BASE["work"][0], ("warn", "embed-worker", "4377", "1.7 GB", "3.9 GB", "92%", "14m", "▅▆▇▇██▇", "degraded: CPU")],
           act=[("21:54:02", "warn", "embed-worker CPU above 90% for 60 s")] + BASE["act"])
CRIT = dict(BASE, ram=(94, "14.7/15.6 GB"), vram=(97, "5.9/6.1 GB"), load="7.82  5.10  3.04", status="crit", sel=0,
            temps=[("system", 71), ("cpu pkg", 93), ("pci", 88), ("int3400", 22)],
            work=[("crit", "model-server-a", "4121", "4.2 GB", "6.8 GB", "71%", "1h 19m", "▅▆▇████", "critical: VRAM 97%"),
                  ("warn", "embed-worker", "4377", "1.7 GB", "3.9 GB", "92%", "21m", "▅▆▇▇██▇", "degraded: CPU")],
            act=[("21:58:40", "crit", "CPU package at 93°C"), ("21:58:31", "crit", "VRAM at 97% · model-server-a"), ("21:54:02", "warn", "embed-worker CPU above 90% for 60 s")],
            banner=("crit", "Critical: CPU package at 93°C and VRAM at 97%. Select a workload and press k to stop it."))
FIRST = dict(BASE, ram=(41, "6.4/15.6 GB"), vram=(4, "0.2/6.1 GB"), work=[], act=[("21:40:02", "ok", "Raqib started · watching 409 processes")], status="ok")

STATES = [
    ("R4", "Normal", "normal", BASE, "Two workloads running, everything within limits."),
    ("R5", "Degraded", "degraded", DEG, "One workload is over its CPU threshold. The header, the row and the bar turn amber."),
    ("R6", "Critical", "critical", CRIT, "Overheating and VRAM almost full. Red banner with the next step; the hottest sensor is red."),
    ("R7", "Kill confirm", "kill", dict(DEG, overlay="kill"), "Kill is always behind a confirm step that says what will be freed."),
    ("R8", "History", "history", dict(DEG, view="history"), "Press h: the last 60 minutes per metric, plus the event log."),
    ("R9", "Help", "help", dict(BASE, overlay="help"), "Press ?: every key on one panel. The same keys work in the web view."),
    ("R10", "First run", "firstrun", FIRST, "No AI workloads yet: a short how-to-start instead of an empty box."),
    ("R11", "Narrow", "narrow", dict(DEG, narrow=True), "80-column terminal; the web view at phone width. Panels stack, low-priority columns drop."),
]


# ------------------------------------------------------------------ terminal
def tbox(title, inner, k, extra="", tagged=False, tcol=None):
    return (f'<div style="position: relative; border: 1px solid {k["strong"]}; padding: 18px 14px 10px; {extra}">'
            f'<span style="position: absolute; top: -11px; left: 10px; padding: 0 6px; background: {k["bg"]}; color: {tcol or k["text"]}; font-weight: 700; white-space: nowrap">{title}{tag(k) if tagged else ""}</span>{inner}</div>')


def t_header(k, st, narrow):
    s = st["status"]
    pill = f'<span style="padding: 2px 10px; background: {C(k, s)}; color: {k["bg"]}; font-weight: 700">{SYM[s]} {WORD[s]}</span>'
    n = len(st["work"])
    deg = sum(1 for w in st["work"] if w[0] != "ok")
    summ = f'{n} workloads · {deg} degraded' if n else "watching 409 processes"
    right = "" if narrow else f'<span style="color: {k["muted"]}">21:55:25 · sample data</span>'
    web_link = "" if narrow else f' · web <span style="color: {k["link"]}">localhost:7070</span>'
    return (f'<header style="display: flex; justify-content: space-between; align-items: center; gap: 12px"><div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap">'
            f'{svg(16, mark_a(k["text"], k["mid"], k["acc"], False), "Raqib")}<b>raqib</b>{pill}<span style="color: {k["t2"]}">{summ}{web_link}</span>{tag(k)}</div>{right}</header>')


def t_vitals(k, st, narrow):
    rp, rv = st["ram"]
    vp, vv = st["vram"]
    lab = 70 if narrow else 90
    val = 150 if narrow else 190
    sp = "" if narrow else "110px"
    col = lambda p: k["crit"] if p >= 90 else k["warn"] if p >= 75 else k["text"]
    temps = "".join(f'<span>{n} {temp(t, k)}</span>' for n, t in (st["temps"][:2] if narrow else st["temps"]))
    cols = f"{lab}px 1fr {val}px" + (f" {sp}" if sp else "")
    sp_cells = lambda s: "" if narrow else f'<span style="color: {k["muted"]}">{s}</span>'
    return (f'<div style="display: grid; grid-template-columns: {cols}; row-gap: 10px; column-gap: 14px; align-items: center">'
            f'<span style="color: {k["muted"]}">RAM</span>{tbar(rp, k)}<span style="text-align: right; color: {col(rp)}">{rp}% · {rv}</span>{sp_cells("▃▄▄▅▅▆▆")}'
            f'<span style="color: {k["muted"]}">VRAM</span>{tbar(vp, k)}<span style="text-align: right; color: {col(vp)}">{vp}% · {vv}</span>{sp_cells("▂▃▅▆▆▇▇")}'
            f'<span style="color: {k["muted"]}">CPU load</span><span style="grid-column: 2 / {4 if narrow else 4}">{st["load"]} <span style="color: {k["muted"]}">· 12 cpus</span></span>{sp_cells("▂▂▃▃▂▃▃")}'
            f'<span style="color: {k["muted"]}">Thermal</span><span style="grid-column: 2 / -1; display: flex; gap: 20px; flex-wrap: wrap">{temps}</span></div>')


def t_work(k, st, narrow):
    if not st["work"]:
        steps = "".join(f'<div><span style="color: {k["acc"]}">{i}</span>&#160;&#160;{t}</div>' for i, t in (("1", "Start your model server or any local AI workload."), ("2", "Raqib picks it up and adds a row here."), ("3", "Open localhost:7070 for the same view in your browser.")))
        return (f'<div style="padding: 18px 8px; display: flex; flex-direction: column; gap: 10px"><b style="color: {k["text"]}">No AI workloads yet.</b>'
                f'<span style="color: {k["t2"]}">Raqib is watching all 409 processes and will list AI workloads as soon as one starts.</span>{steps}'
                f'<span style="color: {k["muted"]}">Press <b style="color: {k["acc"]}">?</b> to see what counts as a workload.</span></div>')
    if narrow:
        cols, hdr = "20px 1fr 70px 50px", ("", "PROCESS", "VRAM", "CPU")
    else:
        cols, hdr = "24px 1.8fr 64px 84px 84px 60px 80px 1fr", ("", "PROCESS", "PID", "VRAM", "RAM", "CPU", "UPTIME", "LAST 60 s")
    out = f'<div style="display: grid; grid-template-columns: {cols}; gap: 10px; padding: 0 8px 6px; color: {k["muted"]}; font-size: 12px">' + "".join(f"<span>{h}</span>" for h in hdr) + "</div>"
    if st.get("banner"):
        bs, bt = st["banner"]
        out = f'<div style="margin-bottom: 10px; padding: 6px 10px; border: 1px solid {C(k, bs)}; color: {C(k, bs)}">{SYM[bs]} {bt}</div>' + out
    for i, (s, n, pid, vr, ram, cpu, up, sp, note) in enumerate(st["work"]):
        c = C(k, s)
        sel = f"background: {k['accSoft']}; outline: 2px solid {k['acc']};" if i == st["sel"] else ""
        nm = f'{n} <span style="color: {c}">{note}</span>' if not narrow else f'{n}'
        cells = [f'<span style="color: {c}">{SYM[s]}</span>', f"<span>{nm}</span>"]
        if narrow:
            cells += [f"<span>{vr}</span>", f'<span style="color: {c if s != "ok" else k["text"]}">{cpu}</span>']
        else:
            cells += [f'<span style="color: {k["muted"]}">{pid}</span>', f"<span>{vr}</span>", f"<span>{ram}</span>", f'<span style="color: {c if s != "ok" else k["text"]}">{cpu}</span>', f"<span>{up}</span>", f'<span style="color: {c}">{sp}</span>']
        out += f'<div style="display: grid; grid-template-columns: {cols}; gap: 10px; padding: 6px 8px; {sel}">{"".join(cells)}</div>'
    return out


def t_history(k, st):
    rows = [("RAM", "▃▃▃▄▄▄▄▅▅▅▅▅▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆", "peak 71% at 21:53", "text"),
            ("VRAM", "▂▂▂▂▃▃▃▃▄▄▅▅▅▆▆▆▆▆▆▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇", "peak 79% at 21:54", "warn"),
            ("CPU", "▂▂▂▂▂▂▃▃▂▂▃▃▃▃▄▄▅▅▆▆▇▇▇▇▇▇▇▇▇▇▇▇▇▆▆▆▆▆▆▆", "peak 7.1 load", "warn"),
            ("CPU °C", "▃▃▃▃▃▃▃▃▃▃▃▃▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄", "peak 58°C", "ok")]
    graph = "".join(f'<div style="display: grid; grid-template-columns: 80px 1fr 180px; gap: 14px"><span style="color: {k["muted"]}">{a}</span><span style="color: {k[c] if c != "text" else k["t2"]}; letter-spacing: 1px">{b}</span><span style="color: {k["t2"]}">{p}</span></div>' for a, b, p, c in rows)
    axis = f'<div style="display: grid; grid-template-columns: 80px 1fr 180px; gap: 14px; color: {k["muted"]}; font-size: 12px"><span></span><span style="display: flex; justify-content: space-between"><span>20:55</span><span>21:15</span><span>21:35</span><span>now</span></span><span></span></div>'
    log = [("21:54:02", "warn", "embed-worker", "CPU above 90% for 60 s"), ("21:41:52", "ok", "embed-worker", "started · 0.9 GB VRAM"),
           ("21:41:17", "ok", "model-server-a", "started · 3.1 GB VRAM"), ("21:12:40", "ok", "model-server-a", "stopped by you (k)"), ("20:58:03", "ok", "raqib", "started")]
    lg = "".join(f'<div style="display: grid; grid-template-columns: 90px 20px 160px 1fr; gap: 10px"><span style="color: {k["muted"]}">{t}</span><span style="color: {C(k, s)}">{SYM[s]}</span><span>{w}</span><span style="color: {k["t2"]}">{m}</span></div>' for t, s, w, m in log)
    return f'<div style="display: flex; flex-direction: column; gap: 8px">{graph}{axis}</div><div style="margin-top: 16px; padding-top: 12px; border-top: 1px solid {k["strong"]}; display: flex; flex-direction: column; gap: 4px">{lg}</div>'


def t_overlay(k, st, narrow):
    if st["overlay"] == "kill":
        w = st["work"][st["sel"]]
        return (f'<div style="position: absolute; {"left: 24px; right: 24px" if narrow else "right: 40px; width: 440px"}; top: 270px; background: {k["bg"]}; border: 2px solid {k["crit"]}; padding: 14px 16px; display: flex; flex-direction: column; gap: 8px; z-index: 2">'
                f'<b style="color: {k["crit"]}">Kill {w[1]} (pid {w[2]})?</b><span style="color: {k["t2"]}">Frees about {w[3]} VRAM and {w[4]} RAM. Unsaved work in it is lost.</span>'
                f'<span><b style="color: {k["crit"]}">y</b> kill&#160;&#160;&#160;<b style="color: {k["acc"]}">n</b> / esc cancel</span></div>')
    if st["overlay"] == "help":
        keys = [("j / k", "select a row"), ("k", "kill the selected workload (asks to confirm)"), ("h", "history: last 60 minutes and events"), ("?", "this help"), ("q", "quit")]
        rows = "".join(f'<div style="display: grid; grid-template-columns: 90px 1fr; gap: 12px"><b style="color: {k["acc"]}">{a}</b><span>{b}</span></div>' for a, b in keys)
        return (f'<div style="position: absolute; left: 50%; top: 200px; transform: translateX(-50%); width: {"90%" if narrow else "560px"}; background: {k["bg"]}; border: 2px solid {k["acc"]}; padding: 18px 20px; display: flex; flex-direction: column; gap: 10px; z-index: 2">'
                f'<b>Keys</b>{rows}<span style="color: {k["muted"]}; margin-top: 6px">Colours: <span style="color: {k["ok"]}">● ok</span> <span style="color: {k["warn"]}">▲ degraded</span> <span style="color: {k["crit"]}">■ critical</span> · ? or esc to close</span>'
                f'<span style="color: {k["muted"]}">The web view at localhost:7070 shows the same panels.</span></div>')
    return ""


def terminal(st, name, w):
    k = T[name]
    narrow = st.get("narrow", False)
    hist = st["view"] == "history"
    main = tbox("History · last 60 min" if hist else f"AI workloads · {len(st['work'])}", t_history(k, st) if hist else t_work(k, st, narrow), k, "flex: 1;", tagged=not narrow, tcol=k["acc"] if hist else None)
    tops = ""
    if not narrow and not hist:
        lst = lambda r: "".join(f'<div style="display: flex; justify-content: space-between; padding: 1px 0"><span>{n}</span><span style="color: {k["t2"]}">{v}</span></div>' for n, v in r)
        tops = f'<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px">{tbox("Top by RAM", lst(TOP_RAM), k)}{tbox("Top by VRAM", lst(TOP_VRAM), k)}{tbox("Top by CPU · per core", lst(TOP_CPU), k)}</div>'
    acts = st["act"][:2] if narrow else st["act"]
    act = "".join(f'<div><span style="color: {k["muted"]}">{t}</span>&#160;&#160;<span style="color: {C(k, s)}">{SYM[s]}</span>&#160;{m}</div>' for t, s, m in acts)
    if hist:
        keys = [("esc", "back"), ("←/→", "range"), ("q", "quit")]
    elif narrow:
        keys = [("q", "quit"), ("j/k", "sel"), ("k", "kill"), ("h", "hist"), ("?", "help")]
    else:
        keys = [("q", "quit"), ("j/k", "select"), ("k", "kill (confirm)"), ("h", "history"), ("?", "help")]
    kb = " · ".join(f'<b style="color: {k["acc"]}">{a}</b> {b}' for a, b in keys)
    foot_r = "" if narrow else f'<span style="color: {k["muted"]}">16-colour ANSI safe</span>'
    h = 900
    return (f'<div class="mono" style="position: relative; width: {w}px; height: {h}px; box-sizing: border-box; background: {k["bg"]}; color: {k["text"]}; font-size: 13px; line-height: 1.5; padding: 18px 24px; display: flex; flex-direction: column; gap: 20px; overflow: hidden">'
            f'{t_header(k, st, narrow)}{tbox("Vitals", t_vitals(k, st, narrow), k)}{main}{tops}{tbox("Activity", act, k)}'
            f'<footer style="display: flex; justify-content: space-between; color: {k["t2"]}"><span>{kb}</span>{foot_r}</footer>{t_overlay(k, st, narrow)}</div>'), h


# ------------------------------------------------------------------ web
def web(st, name, w):
    k = T[name]
    narrow = st.get("narrow", False)
    hist = st["view"] == "history"

    def card(title, inner, extra="", tagged=False):
        return (f'<section style="background: {k["panel"]}; border: 2px solid {k["border"]}; padding: {"14px" if narrow else "18px 20px"}; display: flex; flex-direction: column; gap: 12px; min-width: 0; {extra}">'
                f'<h2 class="mono" style="margin: 0; font-size: 12px; font-weight: 500; letter-spacing: 0.06em; text-transform: uppercase; color: {k["muted"]}">{title}{tag(k) if tagged else ""}</h2>{inner}</section>')

    def stat(lab, val, sub, pct, pts):
        col = k["crit"] if pct is not None and pct >= 90 else k["warn"] if pct is not None and pct >= 75 else k["text"]
        bar = f'<div style="display: flex">{tbar(pct, k)}</div>' if pct is not None else ""
        return (f'<div style="display: flex; flex-direction: column; gap: 8px; min-width: 0"><div style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 13px; color: {k["muted"]}">{lab}</span>{spark(pts, k["mid"], 80, 20)}</div>'
                f'<div class="disp" style="font-size: {22 if narrow else 26}px; font-weight: 500; color: {col}">{val}</div>{bar}<div class="mono" style="font-size: 12px; color: {k["t2"]}">{sub}</div></div>')

    rp, rv = st["ram"]
    vp, vv = st["vram"]
    hot = max(st["temps"], key=lambda t: t[1])
    hcol = k["crit"] if hot[1] >= 85 else k["warn"] if hot[1] >= 70 else k["text"]
    vit = (f'<div style="display: grid; grid-template-columns: {"1fr 1fr" if narrow else "repeat(4, minmax(0, 1fr))"}; gap: {18 if narrow else 28}px">'
           + stat("RAM", f"{rp}%", rv, rp, [.5, .55, .6, .6, .65, .68, rp / 100]) + stat("VRAM", f"{vp}%", vv, vp, [.3, .4, .55, .65, .7, .77, vp / 100])
           + stat("CPU load", st["load"].split()[0], "1 / 5 / 15 min · 12 cpus", None, [.3, .35, .4, .38, .42, .4, .45])
           + f'<div style="display: flex; flex-direction: column; gap: 8px"><span style="font-size: 13px; color: {k["muted"]}">Hottest sensor</span><div class="disp" style="font-size: {22 if narrow else 26}px; font-weight: 500; color: {hcol}">{hot[1]:.1f}°C</div><div class="mono" style="font-size: 12px; color: {k["t2"]}">{hot[0]}</div></div></div>')
    banner = ""
    if st.get("banner"):
        bs, bt = st["banner"]
        banner = f'<div role="alert" style="padding: 12px 16px; border: 2px solid {C(k, bs)}; color: {C(k, bs)}; font-weight: 600">{SYM[bs]} {bt.replace("press k", "use Kill")}</div>'
    if not st["work"]:
        steps = "".join(f'<li style="display: flex; gap: 12px; padding: 10px 0; border-top: 2px solid {k["border"]}"><span class="mono" style="color: {k["acc"]}">0{i}</span><span>{t}</span></li>' for i, t in ((1, "Start your model server or any local AI workload."), (2, "Raqib picks it up and adds a row here."), (3, "Leave this tab open; the terminal app shows the same view.")))
        work = (f'<div style="display: flex; flex-direction: column; gap: 10px"><b style="font-size: 18px">No AI workloads yet</b><span style="color: {k["t2"]}">Raqib is watching all 409 processes and will list AI workloads as soon as one starts.</span>'
                f'<ol style="margin: 0; padding: 0; list-style: none">{steps}</ol></div>')
    elif narrow:
        work = ""
        for i, (s, n, pid, vr, ram, cpu, up, sp, note) in enumerate(st["work"]):
            c = C(k, s)
            sel = f"outline: 2px solid {k['acc']};" if i == st["sel"] else ""
            work += (f'<div style="padding: 12px; border: 2px solid {k["border"]}; {sel} display: flex; flex-direction: column; gap: 6px"><div style="display: flex; justify-content: space-between"><b>{n}</b><span style="color: {c}; font-weight: 600">{SYM[s]} {note}</span></div>'
                     f'<div class="mono" style="font-size: 12px; color: {k["t2"]}">VRAM {vr} · RAM {ram} · CPU <span style="color: {c if s != "ok" else k["t2"]}">{cpu}</span> · {up}</div>'
                     f'<button type="button" style="align-self: flex-start; height: 40px; padding: 0 14px; border: 2px solid {k["strong"]}; background: transparent; color: {k["text"]}; font: inherit; font-size: 13px">Kill…</button></div>')
    else:
        th = lambda t: f'<th scope="col" class="mono" style="text-align: left; padding: 8px 10px; font-size: 12px; font-weight: 400; color: {k["muted"]}; border-bottom: 2px solid {k["border"]}">{t}</th>'
        trs = ""
        for i, (s, n, pid, vr, ram, cpu, up, sp, note) in enumerate(st["work"]):
            c = C(k, s)
            pts = [.4, .45, .5, .55, .5, .6, .58] if s == "ok" else [.6, .7, .85, .9, .95, .97, .92]
            sel = f"background: {k['accSoft']};" if i == st["sel"] else ""
            trs += (f'<tr style="{sel}"><td style="padding: 10px; color: {c}; font-weight: 600; white-space: nowrap">{SYM[s]} {note}</td><td style="padding: 10px">{n}</td><td class="mono" style="padding: 10px; color: {k["muted"]}">{pid}</td>'
                    f'<td class="mono" style="padding: 10px">{vr}</td><td class="mono" style="padding: 10px">{ram}</td><td class="mono" style="padding: 10px; color: {c if s != "ok" else k["text"]}">{cpu}</td><td class="mono" style="padding: 10px">{up}</td>'
                    f'<td style="padding: 10px">{spark(pts, c, 100, 22)}</td><td style="padding: 10px; text-align: right"><button type="button" style="height: 36px; padding: 0 14px; border: 2px solid {k["strong"]}; background: transparent; color: {k["text"]}; font: inherit; font-size: 13px">Kill…</button></td></tr>')
        work = f'<table style="width: 100%; border-collapse: collapse; font-size: 14px"><thead><tr>{"".join(th(t) for t in ("State", "Process", "PID", "VRAM", "RAM", "CPU", "Uptime", "Last 60 s", ""))}</tr></thead><tbody>{trs}</tbody></table>'
    if hist:
        def chart(lab, pts, col, peak):
            return (f'<div style="display: flex; flex-direction: column; gap: 6px; min-width: 0"><div style="display: flex; justify-content: space-between; font-size: 13px"><span style="color: {k["muted"]}">{lab}</span><span class="mono" style="color: {k["t2"]}">{peak}</span></div>'
                    f'<div style="border-bottom: 2px solid {k["border"]}">{spark(pts, col, 560 if not narrow else 320, 60)}</div></div>')
        p = lambda a, b: [a + (b - a) * i / 15 for i in range(16)]
        charts = (f'<div style="display: grid; grid-template-columns: {"1fr" if narrow else "1fr 1fr"}; gap: 22px">'
                  + chart("RAM", p(.45, .69), k["t2"], "peak 71% · 21:53") + chart("VRAM", p(.3, .79), k["warn"], "peak 79% · 21:54")
                  + chart("CPU load", [.2, .2, .22, .25, .3, .3, .35, .4, .5, .6, .7, .78, .8, .76, .72, .7], k["warn"], "peak 7.1") + chart("CPU package °C", p(.5, .58), k["ok"], "peak 58°C") + "</div>")
        log = [("21:54:02", "warn", "embed-worker", "CPU above 90% for 60 s"), ("21:41:52", "ok", "embed-worker", "started · 0.9 GB VRAM"), ("21:41:17", "ok", "model-server-a", "started · 3.1 GB VRAM"), ("21:12:40", "ok", "model-server-a", "stopped by you")]
        lg = "".join(f'<div style="display: grid; grid-template-columns: 80px 24px 1fr; gap: 10px; padding: 8px 0; border-top: 2px solid {k["border"]}; font-size: 14px"><span class="mono" style="color: {k["muted"]}">{t}</span><span style="color: {C(k, s)}">{SYM[s]}</span><span><b>{w2}</b> <span style="color: {k["t2"]}">{m}</span></span></div>' for t, s, w2, m in log)
        range_tabs = "".join(f'<button type="button" style="height: 36px; padding: 0 12px; border: 2px solid {k["acc"] if r == "1 h" else k["strong"]}; background: {k["accSoft"] if r == "1 h" else "transparent"}; color: {k["text"]}; font: inherit; font-size: 13px">{r}</button>' for r in ("15 min", "1 h", "6 h"))
        main = card("History", f'<div style="display: flex; gap: 8px">{range_tabs}</div>{charts}', tagged=True) + card("Events", lg)
    else:
        main = card(f"AI workloads · {len(st['work'])}", banner + work, tagged=True)
    therm = "".join(f'<div style="display: flex; justify-content: space-between; padding: 7px 0; border-top: 2px solid {k["border"]}; font-size: 14px"><span>{a}</span>{temp(b, k)}</div>' for a, b in st["temps"])
    tl = lambda rows: "".join(f'<div style="display: flex; justify-content: space-between; padding: 7px 0; border-top: 2px solid {k["border"]}; font-size: 14px"><span>{n}</span><span class="mono" style="color: {k["t2"]}">{v}</span></div>' for n, v in rows)
    act = "".join(f'<div style="display: flex; gap: 14px; padding: 7px 0; border-top: 2px solid {k["border"]}; font-size: 14px"><span class="mono" style="color: {k["muted"]}">{t}</span><span style="color: {C(k, s)}">{SYM[s]}</span><span>{m}</span></div>' for t, s, m in st["act"])
    if narrow:
        lower = card("Thermal", therm) + card("Activity", act)
    elif hist:
        lower = ""
    else:
        lower = (f'<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 20px">{card("Thermal", therm)}{card("Top by RAM", tl(TOP_RAM))}{card("Top by VRAM", tl(TOP_VRAM))}{card("Top by CPU · per core", tl(TOP_CPU))}</div>'
                 + card("Activity", act))
    s = st["status"]
    pill = f'<span class="mono" style="padding: 6px 12px; background: {C(k, s)}; color: {k["bg"]}; font-size: 13px; font-weight: 700">{SYM[s]} {WORD[s]}</span>'
    overlay = ""
    if st["overlay"] == "kill":
        wk = st["work"][st["sel"]]
        overlay = (f'<div style="position: absolute; inset: 0; background: rgba(0,0,0,0.45); display: flex; align-items: center; justify-content: center; z-index: 3"><div role="dialog" aria-label="Confirm kill" style="width: {"88%" if narrow else "460px"}; background: {k["panel"]}; border: 2px solid {k["crit"]}; padding: 22px; display: flex; flex-direction: column; gap: 12px">'
                   f'<b style="color: {k["crit"]}; font-size: 18px">Kill {wk[1]} (pid {wk[2]})?</b><span style="font-size: 15px; color: {k["t2"]}">Frees about {wk[3]} VRAM and {wk[4]} RAM. Unsaved work in it is lost.</span>'
                   f'<div style="display: flex; gap: 10px"><button type="button" style="height: 44px; padding: 0 18px; border: none; background: {k["crit"]}; color: #FFFFFF; font: inherit; font-weight: 600">Kill process</button>'
                   f'<button type="button" style="height: 44px; padding: 0 18px; border: 2px solid {k["acc"]}; background: transparent; color: {k["acc"]}; font: inherit">Cancel</button></div></div></div>')
    elif st["overlay"] == "help":
        keys = [("j / k", "select a row"), ("k", "kill the selected workload (asks to confirm)"), ("h", "history"), ("?", "this help"), ("esc", "close")]
        rows = "".join(f'<div style="display: grid; grid-template-columns: 80px 1fr; gap: 12px; padding: 8px 0; border-top: 2px solid {k["border"]}"><span class="mono" style="color: {k["acc"]}; font-weight: 700">{a}</span><span>{b}</span></div>' for a, b in keys)
        overlay = (f'<div style="position: absolute; inset: 0; background: rgba(0,0,0,0.45); display: flex; align-items: center; justify-content: center; z-index: 3"><div role="dialog" aria-label="Keyboard shortcuts" style="width: {"88%" if narrow else "520px"}; background: {k["panel"]}; border: 2px solid {k["acc"]}; padding: 22px; display: flex; flex-direction: column; gap: 10px">'
                   f'<b style="font-size: 18px">Keyboard shortcuts</b><span style="color: {k["t2"]}; font-size: 14px">The same keys as the terminal app.</span>{rows}'
                   f'<span style="font-size: 13px; color: {k["muted"]}">Colours: <span style="color: {k["ok"]}">● ok</span> · <span style="color: {k["warn"]}">▲ degraded</span> · <span style="color: {k["crit"]}">■ critical</span></span></div></div>')
    pad = "16px" if narrow else "28px 40px"
    hdr_r = "" if narrow else f'<div class="mono" style="font-size: 12px; color: {k["muted"]}">updated 21:55:25 · sample data</div>'
    body = (f'<div style="position: relative; width: {w}px; box-sizing: border-box; background: {k["bg"]}; color: {k["text"]}; display: flex; flex-direction: column">'
            f'<div style="height: 40px; display: flex; align-items: center; padding: 0 12px; background: {k["panel"]}; border-bottom: 2px solid {k["border"]}"><span class="mono" style="padding: 5px 12px; background: {k["bg"]}; font-size: 12px; color: {k["t2"]}">localhost:7070</span></div>'
            f'<div style="padding: {pad}; display: flex; flex-direction: column; gap: {16 if narrow else 20}px">'
            f'<header style="display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap"><div style="display: flex; align-items: center; gap: 14px; flex-wrap: wrap">{lockup("A", k, 28 if narrow else 32, by=False)}{pill}{tag(k)}</div>{hdr_r}</header>'
            f'{card("Vitals", vit)}{main}{lower}</div>{overlay}</div>')
    return body


# ------------------------------------------------------------------ boards
def page(title, w, h, bg, body):
    body = re.sub(r"border-radius: (?!50%)[^;\"]+", "border-radius: 0", body)
    body = re.sub(r"\b1px (solid|dashed)", r"2px \1", body)
    return HEAD.format(title=title, w=w, h=h, bg=bg, body=body)


def board(rid, name, st, story, surface, heights):
    narrow = st.get("narrow", False)
    if surface == "terminal":
        w = 680 if narrow else 1440
        frames = [terminal(st, th, w)[0] for th in ("dark", "light")]
        fh = [900, 900]
    else:
        w = 390 if narrow else 1440
        frames = [web(st, th, w) for th in ("dark", "light")]
        fh = heights
    label = (f'<div style="padding: 18px 24px; background: #141A22; color: #E8ECF2; display: flex; flex-direction: column; gap: 6px; border-bottom: 2px solid #232B36">'
             f'<div class="mono" style="font-size: 12px; color: #8A94A4">[{rid}] {surface} · dark, then light · {LABEL}</div>'
             f'<div class="disp" style="font-size: {18 if narrow else 22}px; font-weight: 500">{name}</div><div style="font-size: 14px; color: #B7C0CD; line-height: 1.5">{story}</div></div>')
    stack = "".join(f'<div style="height: {h}px; overflow: hidden">{f}</div>' for f, h in zip(frames, fh))
    total = (150 if not narrow else 190) + sum(fh)
    body = f'<div style="width: {w}px; height: {total}px; display: flex; flex-direction: column; background: #0A0C10; overflow: hidden">{label}{stack}</div>'
    return page(f"{rid} {name} {surface}", w, total, "#0A0C10", body), w, total


def write_all(root, web_heights=None):
    """web_heights: {(rid, theme): px} measured by measure.cjs; defaults are generous."""
    out = {}
    for rid, name, key, st, story in STATES:
        for surface in ("terminal", "web"):
            if surface == "web":
                d = 1500 if st.get("narrow") else (1200 if st["view"] == "history" else 1180)
                hs = [(web_heights or {}).get(f"{rid}-dark", d), (web_heights or {}).get(f"{rid}-light", d)]
            else:
                hs = None
            src, w, h = board(rid, name, st, story, surface, hs)
            fn = f"{rid}-Raqib-{key}-{surface}.dc.html"
            open(os.path.join(root, fn), "w").write(src)
            out[fn] = (w, h, f"[{rid}] {name} · {surface} · {LABEL}")
    return out


def measure_pages(root):
    """Standalone pages of each web frame, so their natural height can be measured."""
    res = {}
    for rid, name, key, st, story in STATES:
        for th in ("dark", "light"):
            w = 390 if st.get("narrow") else 1440
            fn = f"_m-{rid}-{th}.html"
            open(os.path.join(root, fn), "w").write(page("m", w, 100, "#0A0C10", web(st, th, w)))
            res[f"{rid}-{th}"] = (fn, w)
    return res
