import sys
from kit import *

OUT = SP / "out"
FEED, STORY = 1350, 1920

def frame(th, n, total, inner, shapes="", h=FEED, label=None):
    lm = "mono"  # small header lockup is mono; colour lockup only at display size on charcoal (CTA)
    right = label if label else f"{n:02d} / {total:02d}"
    head = (f'<div class="head" style="{"top:260px" if h==STORY else ""}">{logo(38, lm, th["fg"])}'
            f'<span class="count">{right}</span></div>')
    return page(head + shapes + inner, th["g"], th["fg"], h)

def swipe_foot(th, h=FEED, text="Swipe"):
    bottom = 88 if h == FEED else 360
    return (f'<div class="foot" style="bottom:{bottom}px"><span class="small" style="opacity:.8">New Narrative · Jaipur</span>'
            f'<span class="swipe">{text}<span class="abtn">{ARROW}</span></span></div>')

def body(html, top=None, bottom=None, gap=48, center=False):
    pos = (f"top:{top}px;" if top is not None else "") + (f"bottom:{bottom}px;" if bottom is not None else "")
    if center: pos = "top:0;bottom:0;justify-content:center;"
    return f'<div class="body" style="{pos}gap:{gap}px">{html}</div>'

def chip(label): return f'<span class="chip"><i></i>{label}</span>'

def cta_slide(th, n, total, lines, btn_fill, btn_text, extra_shapes=""):
    lm = "colour" if th["g"] == T["charcoal"] else "mono"
    inner = body(headline(lines, 150) +
                 f'<span class="pill" style="background:{btn_fill};color:{btn_text}">DM us to start'
                 f'<span class="dot" style="background:{btn_text};color:{btn_fill}">{ARROW}</span></span>'
                 f'<span class="url">www.newnarrative.studio</span>', top=400, gap=56)
    foot = (f'<div class="foot" style="bottom:88px;align-items:flex-end">{logo(96, lm, th["fg"])}'
            f'<span class="small" style="opacity:.8">Brand · Web · Social</span></div>')
    return frame(th, n, total, inner + foot, extra_shapes)

def step_slide(th, n, total, num, title_lines, text, shape, numc=None):
    inner = (body(f'<div class="num" style="font-size:420px;color:{numc or th["fg"]}">{num}</div>', top=230, gap=0) +
             body(f'<div class="rule" style="background:{th["fg"]}"></div>' +
                  headline(title_lines, 112) + f'<p class="para">{text}</p>', bottom=150, gap=44))
    return frame(th, n, total, inner, shape)

def cover_pair(th, total, lines, chip_label, shapes_feed, shapes_story, size=150):
    feed = frame(th, 1, total, body(chip(chip_label) + headline(lines, size), bottom=230, gap=70) + swipe_foot(th), shapes_feed)
    story = frame(th, 0, 0, body(chip(chip_label) + headline(lines, size), bottom=560, gap=70) +
                  swipe_foot(th, STORY, "See post"), shapes_story, STORY, label="NEW POST")
    return feed, story

# =====================================================================
def p05():
    """Font pairings — Signature (charcoal + marigold), slides swap ground."""
    A = dict(g=T["charcoal"], fg=T["marigold"]); B = dict(g=T["marigold"], fg=T["charcoal"])
    total = 7; s = []
    L = [[("i", "Font pairings")], [("r", "that just")], [("b", "work.")]]
    f, st = cover_pair(A, total, L, "Type notes",
                       sparkle(T["marigold"], 440, "right:-130px;top:170px"),
                       sparkle(T["marigold"], 520, "right:-150px;top:330px"), 190)
    s.append(f)
    pairs = [("Playfair Display", "italic", 400, "Inter", "Editorial and confident. Great for fashion, lifestyle and studios."),
             ("DM Serif Display", "normal", 400, "DM Sans", "A matched family. Clean, safe and easy to scale across a website."),
             ("Fraunces", "italic", 600, "Space Grotesk", "Warm serif, techy sans. Perfect for modern D2C brands."),
             ("Cormorant Garamond", "italic", 500, "Manrope", "Luxury and calm. Built for jewellery, bridal and hospitality."),
             ("Instrument Serif", "italic", 400, "Inter Tight", "Sharp and current. Ideal for agencies and portfolios.")]
    for i, (serif, sty, w, sans, txt) in enumerate(pairs):
        th = B if i % 2 == 0 else A
        inner = body(
            f'<span class="small">Pair {i+1:02d}</span>'
            f'<div style="font-family:\'{serif}\';font-style:{sty};font-weight:{w};font-size:460px;line-height:.82;letter-spacing:-.02em">Aa</div>'
            f'<div style="font-family:\'{serif}\';font-style:{sty};font-weight:{w};font-size:76px;line-height:1.05;letter-spacing:-.01em">Every brand has a story.</div>'
            f'<p class="para" style="font-family:\'{sans}\';font-size:40px">{txt}</p>'
            f'<div style="display:flex;gap:16px"><span class="chip" style="font-family:\'{serif}\';font-style:{sty}">{serif}</span>'
            f'<span class="chip" style="font-family:\'{sans}\'">{sans}</span></div>', bottom=150, gap=40)
        s.append(frame(th, i + 2, total, inner, asterisk(th["fg"], 120, "right:88px;top:200px")))
    s.append(cta_slide(A, 7, total, [[("i", "Need a")], [("b", "type system?")]], T["marigold"], T["charcoal"],
                       sparkle(T["marigold"], 300, "right:-70px;top:150px")))
    return "2026-11-05-font-pairings-that-work", s, st

def p06():
    """Palettes from Jaipur — Editorial light (linen / ink / marigold / tangerine pop)."""
    A = dict(g=T["linen"], fg=T["ink"]); B = dict(g=T["ink"], fg=T["linen"])
    total = 6; s = []
    L = [[("i", "Palettes")], [("r", "borrowed from")], [("b", "Jaipur.")]]
    f, st = cover_pair(A, total, L, "Colour study",
                       seal(T["marigold"], 540, style="right:-190px;top:160px") + sparkle(T["tangerine"], 110, "right:330px;top:560px"),
                       seal(T["marigold"], 640, style="right:-200px;top:380px") + sparkle(T["tangerine"], 130, "right:380px;top:760px"), 168)
    s.append(f)
    pals = [("Pink", "City", [("#E28A7A", "Hawa Mahal"), ("#B5523B", "Terracotta"), ("#E9C9A5", "Sandstone"), ("#F6EFE6", "Lime wash")]),
            ("Indigo", "block print", [("#1E2A5A", "Deep indigo"), ("#3B5BA9", "Sanganer blue"), ("#9FB3D9", "Faded dye"), ("#F2EDE4", "Raw cotton")]),
            ("Marigold", "market", [("#F2A007", "Marigold"), ("#E4572E", "Sindoor"), ("#7A1F2B", "Rani"), ("#FFF4D6", "Ghee")]),
            ("Amber Fort", "dusk", [("#C9813A", "Amber"), ("#6E3B2A", "Fort wall"), ("#2E2A3B", "Night sky"), ("#EBD9C0", "Marble")])]
    for i, (b, r, sw) in enumerate(pals):
        th = B if i % 2 == 0 else A
        rows = "".join(f'<div class="sw-row"><div class="sw" style="background:{h};box-shadow:inset 0 0 0 2px {th["fg"]}22"></div>'
                       f'<div><div class="hex">{h}</div><div class="swname">{n}</div></div></div>' for h, n in sw)
        inner = body(f'<span class="small">Palette {i+1:02d} / 04</span>' + headline([[("b", b), ("i", r)]], 110) +
                     f'<div style="display:flex;flex-direction:column;gap:24px;margin-top:16px">{rows}</div>', bottom=110, gap=32)
        s.append(frame(th, i + 2, total, inner, asterisk(T["marigold"], 130, "right:88px;bottom:110px")))
    s.append(cta_slide(A, 6, total, [[("i", "Find your")], [("b", "colours.")]], T["ink"], T["linen"],
                       seal(T["marigold"], 380, style="right:-110px;top:120px")))
    return "2026-11-06-palettes-from-jaipur", s, st

def p07():
    """One rule we break — Cobalt (cobalt + white), slides swap ground."""
    A = dict(g=T["cobalt"], fg=T["white"]); B = dict(g=T["white"], fg=T["cobalt"])
    total = 5; s = []
    L = [[("i", "One rule")], [("r", "we break on")], [("b", "purpose.")]]
    f, st = cover_pair(A, total, L, "Studio notes",
                       asterisk(T["white"], 500, "right:-150px;top:160px"),
                       asterisk(T["white"], 600, "right:-170px;top:300px"), 160)
    s.append(f)
    q = '<div style="font-size:300px;font-weight:800;line-height:.6;height:150px;letter-spacing:-.05em">“</div>'
    q = '<div style="font-size:520px;font-weight:800;line-height:.62;height:260px;letter-spacing:-.05em">“</div>'
    s.append(frame(B, 2, total, body(f'{q}<span class="small">The rule</span>' +
        headline([[("r", "Never use")], [("b", "more than two")], [("b", "typefaces.”")]], 140), bottom=150, gap=44),
        sparkle(T["cobalt"], 150, "right:88px;top:230px")))
    s.append(frame(A, 3, total, body(headline([[("r", "Our logo")], [("b", "uses three.")]], 140) +
        f'<div style="margin:30px 0 10px">{logo(150, "mono", T["white"])}</div>'
        '<p class="para">A cursive serif for warmth, a condensed sans for punch, a clean sans for everything else.</p>', top=300, gap=44),
        sparkle(T["white"], 200, "right:88px;top:200px")))
    s.append(frame(B, 4, total, body(headline([[("i", "Rules are a")], [("i", "starting point.")]], 96) +
        headline([[("b", "A system makes")], [("b", "breaking them")], [("r", "look")], [("b", circle_word("intentional.", T["cobalt"]))]], 120),
        bottom=170, gap=80), asterisk(T["cobalt"], 150, "right:88px;top:230px")))
    s.append(cta_slide(A, 5, total, [[("r", "Break the")], [("b", "right rules.")]], T["white"], T["cobalt"],
                       asterisk(T["white"], 340, "right:-90px;top:140px")))
    return "2026-11-07-one-rule-we-break", s, st

def p08():
    """UX mistakes — Triad (charcoal / lime / sky accent / pink pop once)."""
    A = dict(g=T["charcoal"], fg=T["lime"]); B = dict(g=T["lime"], fg=T["charcoal"])
    total = 7; s = []
    L = [[("i", "UX mistakes")], [("r", "killing your")], [("b", "conversions.")]]
    f, st = cover_pair(A, total, L, "From 8+ years in UX",
                       sparkle(T["sky"], 440, "right:-130px;top:170px") + seal(T["pink"], 210, "5 fixes", T["ink"], "left:560px;top:300px;transform:rotate(-10deg)", 40),
                       sparkle(T["sky"], 520, "right:-150px;top:330px") + seal(T["pink"], 240, "5 fixes", T["ink"], "left:540px;top:560px;transform:rotate(-10deg)", 44), 160)
    s.append(f)
    steps = [("01", [[("r", "Hiding")], [("b", "the price")]], "If people have to DM to find out what something costs, most won’t."),
             ("02", [[("r", "Too many")], [("b", "choices")]], "Six buttons on a homepage means none of them win. Give every page one job."),
             ("03", [[("r", "Forms that ask")], [("b", "for everything")]], "Every extra field is a reason to leave. Ask only for what you need right now."),
             ("04", [[("r", "Designing for")], [("b", "desktop first")]], "Most of your visitors are on a phone. Design there first, then scale up."),
             ("05", [[("b", "Slow"), ("r", "pages")]], "Heavy images and autoplay sliders lose people before they see anything.")]
    for i, (num, tl, txt) in enumerate(steps):
        th = B if i % 2 == 0 else A
        numc = T["charcoal"] if th is B else T["sky"]
        sh = asterisk(th["fg"] if th is B else T["sky"], 130, "right:88px;top:250px")
        s.append(step_slide(th, i + 2, total, num, tl, txt, sh, numc))
    s.append(cta_slide(A, 7, total, [[("r", "Let’s fix")], [("b", "your website.")]], T["lime"], T["charcoal"],
                       sparkle(T["sky"], 300, "right:-70px;top:150px")))
    return "2026-11-08-ux-mistakes-conversions", s, st

def p09():
    """How to brief a designer — Night + Lime (violet shapes on night)."""
    A = dict(g=T["night"], fg=T["lime"]); B = dict(g=T["lime"], fg=T["night"])
    total = 7; s = []
    L = [[("i", "How to")], [("b", "brief a designer")], [("r", "(properly).")]]
    pent = [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]
    f, st = cover_pair(A, total, L, "Save this",
                       pentomino(T["violet"], 130, pent, "right:-110px;top:170px"),
                       pentomino(T["violet"], 160, pent, "right:-140px;top:400px"), 150)
    s.append(f)
    steps = [("01", [[("r", "Start with")], [("b", "the why")]], "What’s changing in your business, and why now?"),
             ("02", [[("r", "Name your")], [("b", "audience")]], "Who should this speak to, and who should it not?"),
             ("03", [[("b", "Show,"), ("r", "don’t")], [("b", "describe")]], "Share references you love and hate. ‘Clean and modern’ means something different to everyone."),
             ("04", [[("r", "List your")], [("b", "must-haves")]], "Formats, sizes, deadlines and where the work will live."),
             ("05", [[("r", "Define")], [("b", "success")]], "More enquiries? A sharper look? Decide before the first draft.")]
    for i, (num, tl, txt) in enumerate(steps):
        th = B if i % 2 == 0 else A
        sh = (pentomino(T["night"], 60, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], "right:88px;top:250px") if th is B
              else pentomino(T["violet"], 60, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], "right:88px;top:250px"))
        s.append(step_slide(th, i + 2, total, num, tl, txt, sh))
    s.append(cta_slide(A, 7, total, [[("r", "Got a")], [("b", "brief ready?")]], T["lime"], T["night"],
                       pentomino(T["violet"], 110, pent, "right:-60px;top:140px")))
    return "2026-11-09-how-to-brief-a-designer", s, st

def p10():
    """How we use AI — Pink (pink + ink), slides swap ground."""
    A = dict(g=T["pink"], fg=T["ink"]); B = dict(g=T["ink"], fg=T["pink"])
    total = 5; s = []
    L = [[("r", "How we use")], [("b", "AI")], [("i", "(and how we don’t).")]]
    f, st = cover_pair(A, total, L, "Behind the studio",
                       sparkle(T["ink"], 380, "right:-90px;top:250px"),
                       sparkle(T["ink"], 460, "right:-120px;top:340px"), 150)
    s.append(f)
    def lst(items): return '<ol class="list">' + "".join(f"<li><b>{i+1:02d}</b><span>{t}</span></li>" for i, t in enumerate(items)) + "</ol>"
    s.append(frame(B, 2, total, body(headline([[("b", "What AI")], [("r", "does for us")]], 130), top=250) +
        body(lst(["Research and competitor scans", "Moodboard exploration", "First-draft copy to react to", "Resizing assets for every format"]), bottom=150),
        asterisk(T["pink"], 130, "right:88px;top:250px")))
    s.append(frame(A, 3, total, body(headline([[("b", "What it")], [("r", "never does")]], 130), top=250) +
        body(lst(["Your brand strategy", "Final creative decisions", "Anything that should sound like you", "Replace a conversation with you"]), bottom=150),
        asterisk(T["ink"], 130, "right:88px;top:250px")))
    s.append(frame(B, 4, total, body(headline([[("r", "AI makes us")], [("i", "faster.")]], 120) +
        headline([[("b", "Taste, judgment")], [("b", "and your story")], [("r", "are still")], [("b", circle_word("human", T["pink"])), ("b", "<span style=\"margin-left:.15em\">work.</span>")]], 120),
        bottom=170, gap=80), sparkle(T["pink"], 150, "right:88px;top:230px")))
    s.append(cta_slide(A, 5, total, [[("b", "Human-led,")], [("i", "AI-assisted.")]], T["ink"], T["pink"],
                       sparkle(T["ink"], 300, "right:-70px;top:150px")))
    return "2026-11-10-how-we-use-ai", s, st

POSTS = dict(p05=p05, p06=p06, p07=p07, p08=p08, p09=p09, p10=p10)

if __name__ == "__main__":
    keys = sys.argv[1:] or list(POSTS)
    jobs = []
    for k in keys:
        folder, slides, story = POSTS[k]()
        for i, h in enumerate(slides):
            jobs.append((h, OUT / folder / f"feed_{i+1:02d}.jpg", FEED))
        jobs.append((story, OUT / folder / "story_01.jpg", STORY))
    render(jobs)
    print("rendered", len(jobs))
