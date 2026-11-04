"""New Narrative post kit — renders slides from the design system (tokens v2, 2026-11-03)."""
import os, pathlib

SP = pathlib.Path(__file__).resolve().parent.parent
FONTS = SP / "fonts"

T = dict(charcoal="#282828", linen="#F2EDEA", mist="#D9D9D9", paper="#FBF9FA", ink="#000000",
         white="#FFFFFF", pink="#E35E9E", cobalt="#2B65F5", marigold="#F0C060", m700="#C09B53",
         m800="#907745", lime="#B9E82B", tangerine="#E88726", sky="#57CFF4", violet="#AE6CF9",
         cream="#FEFACB", night="#1F1A2D", forest="#195D36", red="#F7200D")

def ff(pkg, fam, w, style="normal"):
    f = FONTS / pkg / "package" / "files" / f"{pkg}-latin-{w}-{style}.woff2"
    return f"@font-face{{font-family:'{fam}';src:url('file://{f}') format('woff2');font-weight:{w};font-style:{style};}}"

FONTFACES = "\n".join([
    ff("playfair-display", "Playfair Display", 800, "italic"), ff("playfair-display", "Playfair Display", 400, "italic"),
    ff("playfair-display", "Playfair Display", 400), ff("anton", "Anton", 400),
    ff("dm-serif-display", "DM Serif Display", 400), ff("dm-sans", "DM Sans", 400), ff("dm-sans", "DM Sans", 500),
    ff("fraunces", "Fraunces", 400, "italic"), ff("fraunces", "Fraunces", 600, "italic"), ff("space-grotesk", "Space Grotesk", 400), ff("space-grotesk", "Space Grotesk", 500),
    ff("cormorant-garamond", "Cormorant Garamond", 400, "italic"), ff("cormorant-garamond", "Cormorant Garamond", 500, "italic"),
    ff("manrope", "Manrope", 400), ff("manrope", "Manrope", 500),
    ff("instrument-serif", "Instrument Serif", 400, "italic"), ff("inter-tight", "Inter Tight", 400), ff("inter-tight", "Inter Tight", 500),
])

# ---------- shapes (from the system's Vectors group) ----------
def sparkle(c, size, style=""):
    return (f'<svg class="shape" style="width:{size}px;height:{size}px;{style}" viewBox="0 0 100 100">'
            f'<path d="M50 0C53 34 66 47 100 50C66 53 53 66 50 100C47 66 34 53 0 50C34 47 47 34 50 0Z" fill="{c}"/></svg>')

def asterisk(c, size, style=""):
    return (f'<svg class="shape" style="width:{size}px;height:{size}px;{style}" viewBox="0 0 100 100"><g fill="{c}">'
            '<rect x="44" y="4" width="12" height="92"/><rect x="44" y="4" width="12" height="92" transform="rotate(60 50 50)"/>'
            '<rect x="44" y="4" width="12" height="92" transform="rotate(120 50 50)"/></g></svg>')

SEAL = ("M100 50L90.21 58L96.19 69.13L84.09 72.78L85.36 85.36L72.78 84.09L69.13 96.19L58 90.21L50 100L42 90.21L30.87 96.19"
        "L27.22 84.09L14.64 85.36L15.91 72.78L3.81 69.13L9.79 58L0 50L9.79 42L3.81 30.87L15.91 27.22L14.64 14.64L27.22 15.91"
        "L30.87 3.81L42 9.79L50 0L58 9.79L69.13 3.81L72.78 15.91L85.36 14.64L84.09 27.22L96.19 30.87L90.21 42Z")

def seal(c, size, label="", tc="#000", style="", fs=34):
    lab = f'<span style="font-size:{fs}px;color:{tc}">{label}</span>' if label else ""
    return (f'<div class="seal shape" style="width:{size}px;height:{size}px;{style}"><svg viewBox="0 0 100 100">'
            f'<path d="{SEAL}" fill="{c}"/></svg>{lab}</div>')

def pentomino(c, cell, cells, style=""):
    w = (max(x for x, y in cells) + 1) * cell; h = (max(y for x, y in cells) + 1) * cell
    r = "".join(f'<rect x="{x*cell}" y="{y*cell}" width="{cell}" height="{cell}" fill="{c}"/>' for x, y in cells)
    return f'<svg class="shape" style="width:{w}px;height:{h}px;{style}" viewBox="0 0 {w} {h}">{r}</svg>'

def stepbar(colors, w=44, h=30, style=""):
    return '<div class="stepbar" style="%s">%s</div>' % (style, "".join(f'<span style="background:{c};width:{w}px;height:{h}px"></span>' for c in colors))

def circle_word(word, c):
    return (f'<span class="hl">{word}<svg viewBox="0 0 200 100" preserveAspectRatio="none">'
            f'<path d="M34 16C86 0 172 4 192 38C210 72 150 97 92 95C32 93 4 72 9 46C14 26 44 12 82 9" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round"/></svg></span>')

ARROW = '<svg viewBox="0 0 120 80" class="arr"><path d="M6 40h100M76 10l30 30-30 30" fill="none" stroke="currentColor" stroke-width="10" stroke-linecap="square"/></svg>'

def logo(size, mode="mono", color=None):
    """mode colour = marigold/red/marigold (charcoal ground only); mono = one colour."""
    if mode == "colour":
        cn, cr, cs = T["marigold"], T["red"], T["marigold"]
    else:
        cn = cr = cs = color
    return (f'<div class="logo" style="font-size:{size}px"><div class="lrow"><span class="lnew" style="color:{cn}">New</span>'
            f'<span class="lnarr" style="color:{cr}">NARRATIVE</span></div><span class="lstudio" style="color:{cs}">STUDIO</span></div>')

# ---------- headline: list of lines, each a list of (style, text) ----------
def headline(lines, size=124, color=None, extra=""):
    out = []
    for ln in lines:
        parts = "".join(f'<span class="w-{s}">{t}</span>' for s, t in ln)
        out.append(f'<div class="hl-line">{parts}</div>')
    return f'<div class="headline" data-fit style="font-size:{size}px;{f"color:{color};" if color else ""}{extra}">{"".join(out)}</div>'

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:transparent}
.slide{position:relative;width:1080px;overflow:hidden;font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.head{position:absolute;left:88px;right:88px;top:80px;display:flex;justify-content:space-between;align-items:flex-start;z-index:5}
.count{font-size:24px;font-weight:500;letter-spacing:.08em;font-variant-numeric:tabular-nums;padding-top:6px}
.logo{display:inline-flex;flex-direction:column;align-items:flex-start;line-height:1}
.lrow{display:flex;align-items:baseline;gap:.1em}
.lnew{font-family:'Playfair Display';font-style:italic;font-weight:800;font-size:.875em}
.lnarr{font-family:'Anton';font-size:1em;letter-spacing:.01em}
.lstudio{font-family:'Anton';font-size:.47em;letter-spacing:.04em;margin-left:2.2em;margin-top:.08em}
.body{position:absolute;left:88px;right:88px;z-index:3;display:flex;flex-direction:column}
.headline{text-transform:uppercase;letter-spacing:-.05em;line-height:.98;width:100%}
.hl-line{white-space:nowrap;display:block}
.hl-line>span+span{margin-left:.2em}
.w-b{font-weight:800}.w-r{font-weight:400}.w-i{font-weight:400;font-style:italic}
.w-p{font-family:'Playfair Display';font-style:italic;font-weight:400;text-transform:none;letter-spacing:-.02em}
.para{font-size:38px;line-height:1.38;font-weight:400;letter-spacing:-.01em;max-width:860px}
.chip{display:inline-flex;align-items:center;gap:16px;height:60px;padding:0 30px 0 24px;border-radius:999px;border:2.5px solid currentColor;font-size:25px;font-weight:500;align-self:flex-start}
.chip i{display:block;width:40px;height:16px;background:currentColor}
.pill{display:inline-flex;align-items:center;gap:22px;height:92px;padding:0 14px 0 40px;border-radius:999px;font-size:32px;font-weight:700;align-self:flex-start}
.pill .dot{width:66px;height:66px;border-radius:50%;display:grid;place-items:center}
.pill .arr{width:30px;height:20px}
.foot{position:absolute;left:88px;right:88px;display:flex;justify-content:space-between;align-items:center;z-index:5}
.swipe{display:flex;align-items:center;gap:20px;font-size:24px;font-weight:700;letter-spacing:.14em;text-transform:uppercase}
.abtn{width:76px;height:76px;border-radius:50%;border:2.5px solid currentColor;display:grid;place-items:center}
.abtn .arr{width:32px;height:22px}
.small{font-size:24px;font-weight:500;letter-spacing:.12em;text-transform:uppercase}
.shape{position:absolute;display:block;z-index:1}
.seal{display:grid;place-items:center;text-align:center}
.seal svg{position:absolute;inset:0;width:100%;height:100%}
.seal span{position:relative;font-weight:800;text-transform:uppercase;letter-spacing:-.03em;line-height:1;max-width:70%}
.stepbar{position:absolute;display:flex;z-index:2}
.hl{position:relative;display:inline-block}
.hl-line:has(.hl){margin-top:.22em;padding-left:.08em}
.hl svg{position:absolute;left:-7%;top:-22%;width:114%;height:144%;overflow:visible;pointer-events:none}
.num{font-size:250px;font-weight:300;letter-spacing:-.07em;line-height:.8;font-variant-numeric:tabular-nums}
.rule{height:3px;width:100%;opacity:.35}
.list{list-style:none;width:100%}
.list li{display:flex;gap:34px;align-items:baseline;padding:38px 0;border-top:2px solid currentColor;font-size:42px;line-height:1.25}
.list li:last-child{border-bottom:2px solid currentColor}
.list li b{font-weight:800;font-variant-numeric:tabular-nums;min-width:56px}
.sw-row{display:flex;align-items:center;gap:36px}
.sw{width:140px;height:140px;flex:none}
.hex{font-size:54px;font-weight:800;letter-spacing:-.03em;line-height:1;font-variant-numeric:tabular-nums}
.swname{font-size:30px;margin-top:8px}
.url{font-size:34px;font-weight:800;letter-spacing:-.01em;text-transform:uppercase}
"""

FIT_JS = """
document.querySelectorAll('[data-fit]').forEach(el=>{
  let s=parseFloat(getComputedStyle(el).fontSize); const max=el.clientWidth;
  const lines=[...el.querySelectorAll('.hl-line')];
  const wide=()=>Math.max(...lines.map(l=>l.scrollWidth));
  let g=0; while(wide()>max && g<200){ s-=2; el.style.fontSize=s+'px'; g++; }
});
"""

def page(inner, ground, fg, h):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTFACES}{CSS}</style></head><body>"
            f"<div class='slide' style='height:{h}px;background:{ground};color:{fg}'>{inner}</div>"
            f"<script>{FIT_JS}</script></body></html>")

def render(jobs):
    """jobs: list of (html, out_path, height)"""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        for html, out, h in jobs:
            tmp = SP / "build" / "_tmp.html"; tmp.write_text(html)
            pg.set_viewport_size({"width": 1080, "height": h})
            pg.goto(f"file://{tmp}"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(150)
            pg.evaluate(FIT_JS)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            png = str(out).replace(".jpg", ".png")
            pg.locator(".slide").screenshot(path=png)
            from PIL import Image
            Image.open(png).convert("RGB").save(out, quality=93, optimize=True); os.remove(png)
        b.close()
