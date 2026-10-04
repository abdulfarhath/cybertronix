#!/usr/bin/env python3
"""Export the chosen logos as real asset files (D38, D39).

  python3 design/boards/export.py            # from the repo root
  node design/boards/render.cjs design/build-png.json   # renders the PNGs (Playwright)
  (export.py runs render.cjs and ImageMagick for you when they are available)

Writes design/logo/ (Cybertronix, L6 Sensor mast, D38) and design/raqib-logo/ (Raqib, option A Panel + pulse):
SVG full / simple / mono / light / dark / on-accent, horizontal and stacked lock-ups,
PNG app icons 16 32 48 180 192 512, favicon.ico, and a 1200x630 og-image.
Colours come from design/tokens.json. Marks come from logo.py (m6) and raqib.py (mark_a)."""
import json, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
TOKENS = os.path.join(REPO, "design", "tokens.json")
sys.argv = [sys.argv[0], TOKENS]
sys.path.insert(0, HERE)
import logo  # noqa: E402  (reads tokens from sys.argv[1])
import raqib  # noqa: E402

TOK = json.load(open(TOKENS))
D, L = TOK["color"]["dark"], TOK["color"]["light"]
ACC_D, ACC_L, BTN = TOK["accent"]["dark"], TOK["accent"]["light"], TOK["accent"]["button"]["dark"]

# colour versions: name -> (ink, mid, eye, ground or None)
VERSIONS = {
    "dark": (D["text"], D["text-muted"], ACC_D, D["bg"]),
    "light": (L["text"], "#9AA3B2", ACC_L, L["bg"]),
    "mono-black": ("#000000", "#000000", "#000000", None),
    "mono-white": ("#FFFFFF", "#FFFFFF", "#FFFFFF", None),
    "on-accent": ("#FFFFFF", "#FFFFFF", D["bg"], BTN),
}

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@600&amp;family=JetBrains+Mono:wght@700'
         '&amp;family=Geist:wght@400;500&amp;display=swap" rel="stylesheet">')


def cyx(ink, mid, eye, full):
    return logo.m6({"ink": ink, "mid": mid, "acc": eye}, full)


def rqb(ink, mid, eye, full):
    return raqib.mark_a(ink, mid, eye, full)


BRANDS = {
    "cybertronix": dict(dir="design/logo", mark=cyx, word="cybertronix", sub=None,
                        word_style="font-family: Unbounded, sans-serif; font-weight: 600; letter-spacing: -0.02em",
                        og_line="Robotics engineering · Hyderabad"),
    "raqib": dict(dir="design/raqib-logo", mark=rqb, word="raqib", sub="by Cybertronix",
                  word_style="font-family: 'JetBrains Mono', monospace; font-weight: 700; letter-spacing: -0.02em",
                  og_line="A terminal monitor for AI workloads"),
}


def svg_mark(inner, size=48, ground=None, pad=0):
    """A standalone SVG. pad = clear space in grid units added around the 48-unit mark."""
    vb = 48 + 2 * pad
    bg = f'<rect x="{-pad}" y="{-pad}" width="{vb}" height="{vb}" fill="{ground}"/>' if ground else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="{-pad} {-pad} {vb} {vb}">'
            f'{bg}{inner}</svg>\n')


def svg_lockup(b, version, stacked=False):
    ink, mid, eye, ground = VERSIONS[version]
    inner = b["mark"](ink, mid, eye, True)
    sub = b["sub"]
    if not stacked:
        w, h = 48 + 14 + len(b["word"]) * 22 + 8, 48
        text = f'<text x="62" y="{31 if not sub else 26}" font-size="30" fill="{ink}" style="{b["word_style"]}">{b["word"]}</text>'
        if sub:
            text += f'<text x="62" y="43" font-size="10" fill="{mid if version in ("dark", "light") else ink}" font-family="Geist, sans-serif">{sub}</text>'
        mark = inner
    else:
        w = max(48, len(b["word"]) * 22) + 16
        h = 48 + 50 + (14 if sub else 0)
        mx = (w - 48) / 2
        mark = f'<g transform="translate({mx} 0)">{inner}</g>'
        text = f'<text x="{w / 2}" y="86" font-size="28" text-anchor="middle" fill="{ink}" style="{b["word_style"]}">{b["word"]}</text>'
        if sub:
            text += f'<text x="{w / 2}" y="104" font-size="10" text-anchor="middle" fill="{mid if version in ("dark", "light") else ink}" font-family="Geist, sans-serif">{sub}</text>'
    bg = f'<rect width="{w}" height="{h}" fill="{ground}"/>' if ground else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w * 4}" height="{h * 4}" viewBox="0 0 {w} {h}">'
            f'<!-- Text uses the brand font; outline it in a vector editor before print use. -->{bg}{mark}{text}</svg>\n')


def html_page(w, h, body, bg="transparent"):
    return (f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>html,body{{margin:0;background:{bg}}}'
            f'body{{width:{w}px;height:{h}px;overflow:hidden}}</style></head><body>{body}</body></html>')


# Hand-drawn 16x16 pixel versions for 16 and 32 px (crisp at small sizes).
# '#' ink, 'm' mid grey, '@' the one accent element, '.' empty.
PIX16 = {
    "cybertronix": ["......####......",
                    ".......##.......",
                    ".......##.......",
                    ".......##.......",
                    ".##############.",
                    ".##############.",
                    ".##.........##..",
                    ".##.........##..",
                    ".##..##..@@.....",
                    ".##..##..@@.....",
                    ".##.............",
                    ".##.........##..",
                    ".##.........##..",
                    ".##############.",
                    ".##############.",
                    "................"],
    "raqib": ["................",
              ".##...#########.",
              ".#............#.",
              ".#.....#......#.",
              ".#....#.#.....#.",
              ".#.###..#.###.#.",
              ".#.......#....#.",
              ".#............#.",
              ".#............#.",
              ".#.mmm.@@@.mmm#.",
              ".#.mmm.@@@.mmm#.",
              ".#.mmm.@@@.mmm#.",
              ".#............#.",
              ".#............#.",
              ".##############.",
              "................"],
}


def pix_svg(key, ink, mid, eye, size, ground=None):
    rows = PIX16[key]
    o = f'<rect width="16" height="16" fill="{ground}"/>' if ground else ""
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            c = {"#": ink, "m": mid, "@": eye}.get(ch)
            if c:
                o += f'<rect x="{x}" y="{y}" width="1" height="1" fill="{c}"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 16 16" shape-rendering="crispEdges">{o}</svg>\n'


def icon_html(b, size, key=None):
    if key and size in (16, 32):
        return html_page(size, size, pix_svg(key, L["text"], "#9AA3B2", ACC_L, size, "#FFFFFF"))
    if size == 48:
        inner = b["mark"](L["text"], "#9AA3B2", ACC_L, False)
        return html_page(48, 48, f'<div style="width:48px;height:48px;background:#FFFFFF">{svg_mark(inner, 48)}</div>')
    return icon_html_tile(b, size)


def icon_html_tile(b, size):
    """App icon / favicon tile: white square, simple mark at <= 64 px, full mark above."""
    full = size > 64
    inner = b["mark"](L["text"], "#9AA3B2", ACC_L, full)
    pad = 2 if size <= 48 else 10
    s = size
    svg = svg_mark(inner, s, ground=None, pad=pad).replace('width="' + str(s) + '" height="' + str(s) + '"', f'width="{s}" height="{s}"')
    return html_page(s, s, f'<div style="width:{s}px;height:{s}px;background:#FFFFFF">{svg}</div>')


def og_html(b):
    ink, mid, eye, ground = VERSIONS["dark"]
    mark = svg_mark(b["mark"](ink, mid, eye, True), 168)
    sub = f'<div style="font-family: Geist, sans-serif; font-size: 30px; color: {D["text-muted"]}; margin-top: 8px">{b["sub"]}</div>' if b["sub"] else ""
    grid = ("background-color:#0A0C10;background-image:linear-gradient(rgba(143,178,255,0.06) 2px,transparent 2px),"
            "linear-gradient(90deg,rgba(143,178,255,0.06) 2px,transparent 2px);background-size:40px 40px")
    body = (f'<div style="width:1200px;height:630px;{grid};display:flex;flex-direction:column;justify-content:center;padding:0 110px;box-sizing:border-box;gap:44px">'
            f'<div style="display:flex;align-items:center;gap:48px">{mark}<div><div style="{b["word_style"]};font-size:112px;line-height:1;color:{ink}">{b["word"]}</div>{sub}</div></div>'
            f'<div style="height:2px;background:{D["rule"]}"></div>'
            f'<div style="font-family: Geist, sans-serif; font-size: 34px; color: {D["text-2"]}">{b["og_line"]}</div></div>')
    return html_page(1200, 630, body, "#0A0C10")


def main():
    jobs = []
    tmp = os.path.join(REPO, "design", ".build")
    os.makedirs(tmp, exist_ok=True)
    for key, b in BRANDS.items():
        out = os.path.join(REPO, b["dir"])
        os.makedirs(out, exist_ok=True)
        files = []
        for v, (ink, mid, eye, ground) in VERSIONS.items():
            for lvl, full in (("full", True), ("simple", False)):
                name = f"{key}-mark-{lvl}-{v}.svg"
                open(os.path.join(out, name), "w").write(svg_mark(b["mark"](ink, mid, eye, full), 192 if full else 64, ground))
                files.append(name)
        for v, (ink, mid, eye, ground) in VERSIONS.items():
            name = f"{key}-mark-16px-{v}.svg"
            open(os.path.join(out, name), "w").write(pix_svg(key, ink, mid, eye, 16, ground))
            files.append(name)
        for v in ("dark", "light", "mono-black", "mono-white"):
            for st in (False, True):
                name = f"{key}-lockup-{'stacked' if st else 'horizontal'}-{v}.svg"
                open(os.path.join(out, name), "w").write(svg_lockup(b, v, st))
                files.append(name)
        for s in (16, 32, 48, 180, 192, 512):
            h = os.path.join(tmp, f"{key}-icon-{s}.html")
            open(h, "w").write(icon_html(b, s, key))
            jobs.append({"html": h, "w": s, "h": s, "out": os.path.join(out, f"{key}-icon-{s}.png")})
        h = os.path.join(tmp, f"{key}-og.html")
        open(h, "w").write(og_html(b))
        jobs.append({"html": h, "w": 1200, "h": 630, "out": os.path.join(out, f"{key}-og-1200x630.png")})
        print(key, len(files), "svg files")
    manifest = os.path.join(tmp, "png-jobs.json")
    json.dump(jobs, open(manifest, "w"), indent=1)
    subprocess.run(["node", os.path.join(HERE, "render.cjs"), manifest], check=True)
    for key, b in BRANDS.items():
        out = os.path.join(REPO, b["dir"])
        if shutil.which("convert"):
            subprocess.run(["convert"] + [os.path.join(out, f"{key}-icon-{s}.png") for s in (16, 32, 48)] + [os.path.join(out, "favicon.ico")], check=True)
    shutil.rmtree(tmp)


if __name__ == "__main__":
    main()
