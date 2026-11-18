"""Week 2 (19–25 Nov 2026): business-owner series — websites, UX, holistic / new-age marketing.
Run: python3 posts_w2.py [p11 p12 …]  → renders into ../out/<folder>/
"""
import sys
from posts import *  # frame, body, step_slide, cover_pair, cta_slide, chip, swipe_foot, FEED, STORY, OUT
from kit import *

def lst(items):
    return '<ol class="list">' + "".join(f"<li><b>{i+1:02d}</b><span>{t}</span></li>" for i, t in enumerate(items)) + "</ol>"

def text_slide(th, n, total, lines, para, shape, size=130, label=None):
    lab = f'<span class="small">{label}</span>' if label else ""
    return frame(th, n, total, body(lab + headline(lines, size) + f'<p class="para">{para}</p>', bottom=170, gap=56), shape)

def stat_slide(th, n, total, big, lines, para, src, shape, bigc=None):
    inner = (body(f'<div class="num" style="font-size:380px;color:{bigc or th["fg"]}">{big}</div>', top=230, gap=0) +
             body(f'<div class="rule" style="background:{th["fg"]}"></div>' + headline(lines, 112) +
                  f'<p class="para">{para}</p><span class="small" style="opacity:.75;letter-spacing:.06em">{src}</span>',
                  bottom=140, gap=40))
    return frame(th, n, total, inner, shape)

def quote_slide(th, n, total, q_lines, fix, shape):
    q = '<div style="font-size:400px;font-weight:800;line-height:.62;height:200px;letter-spacing:-.05em">“</div>'
    inner = body(q + '<span class="small">What we hear</span>' + headline(q_lines, 112) +
                 f'<div class="rule" style="background:{th["fg"]}"></div>'
                 f'<span class="small">The real why</span><p class="para">{fix}</p>', bottom=150, gap=36)
    return frame(th, n, total, inner, shape)

def vs_slide(th, n, total, then, now, para, shape):
    inner = body(f'<span class="small">Then</span>'
                 f'<div class="headline" data-fit style="font-size:96px;opacity:.55"><div class="hl-line">'
                 f'<span class="w-r" style="text-decoration:line-through;text-decoration-thickness:6px">{then}</span></div></div>'
                 f'<div style="width:120px;height:80px;margin:6px 0">{ARROW}</div>'
                 f'<span class="small">Now</span>' + headline(now, 124) + f'<p class="para">{para}</p>', bottom=160, gap=34)
    return frame(th, n, total, inner, shape)

# =====================================================================
def p11():
    """Why Instagram isn't enough — Signature (charcoal + marigold)."""
    A = dict(g=T["charcoal"], fg=T["marigold"]); B = dict(g=T["marigold"], fg=T["charcoal"])
    total = 8; s = []
    L = [[("i", "Why Instagram")], [("r", "isn’t enough")], [("b", "for your business.")]]
    f, st = cover_pair(A, total, L, "For business owners",
                       sparkle(T["marigold"], 440, "right:-130px;top:170px"),
                       sparkle(T["marigold"], 520, "right:-150px;top:330px"), 150)
    s.append(f)
    s.append(stat_slide(B, 2, total, "402", [[("r", "out of"), ("b", "40,000")]],
                        "Indian MSMEs in one study had a website that actually worked.",
                        "Source: SERP Forge MSME study, Dec 2025", ""))
    steps = [("01", [[("r", "You don’t own")], [("b", "your followers")]], "A rule change or a locked account can wipe out your reach overnight. Your website and domain are yours."),
             ("02", [[("r", "People Google")], [("b", "before they buy")]], "When someone hears your name, they search it. If nothing shows up, they find someone who does."),
             ("03", [[("r", "A website")], [("b", "builds trust")]], "Prices, proof, policies and contact details in one place. That is what makes a stranger feel safe to pay."),
             ("04", [[("r", "It sells")], [("b", "while you sleep")]], "Enquiries, bookings and orders at 2 AM, without you answering every DM."),
             ("05", [[("r", "Your ads need")], [("b", "a place to land")]], "Ads work best when they send people to a page built for one action, not a profile grid.")]
    for i, (num, tl, txt) in enumerate(steps):
        th = A if i % 2 == 0 else B
        s.append(step_slide(th, i + 3, total, num, tl, txt, asterisk(th["fg"], 130, "right:88px;top:250px")))
    s.append(cta_slide(A, 8, total, [[("i", "Own your")], [("b", "online address.")]], T["marigold"], T["charcoal"],
                       sparkle(T["marigold"], 300, "right:-70px;top:150px")))
    return "2026-11-19-why-instagram-isnt-enough", s, st

def p12():
    """Starting a business — Editorial light (linen / ink, marigold shapes)."""
    A = dict(g=T["linen"], fg=T["ink"]); B = dict(g=T["ink"], fg=T["linen"])
    total = 8; s = []
    L = [[("i", "Starting a business?")], [("r", "Set these up")], [("b", "first.")]]
    f, st = cover_pair(A, total, L, "Save this checklist",
                       seal(T["marigold"], 540, style="right:-190px;top:160px"),
                       seal(T["marigold"], 640, style="right:-200px;top:380px"), 150)
    s.append(f)
    steps = [("01", [[("r", "A name")], [("b", "you can own")]], "Check the domain and Instagram handle are free before you print a single card."),
             ("02", [[("r", "Google")], [("b", "Business Profile")]], "It is free, and it is how people find you on Maps and in “near me” searches."),
             ("03", [[("r", "A simple")], [("b", "website")]], "One page is enough to start: what you do, proof, packages or prices, and how to reach you."),
             ("04", [[("b", "WhatsApp"), ("r", "Business")]], "Add a catalogue, quick replies and an away message so no enquiry goes cold."),
             ("05", [[("r", "Brand")], [("b", "basics")]], "A logo, two colours and two fonts, used everywhere. Consistency reads as credibility."),
             ("06", [[("r", "One way")], [("b", "to measure")]], "Analytics or even a simple sheet. Know where every customer came from.")]
    for i, (num, tl, txt) in enumerate(steps):
        th = B if i % 2 == 0 else A
        s.append(step_slide(th, i + 2, total, num, tl, txt, asterisk(T["marigold"], 130, "right:88px;top:250px")))
    s.append(cta_slide(A, 8, total, [[("i", "Starting")], [("b", "something new?")]], T["ink"], T["linen"],
                       seal(T["marigold"], 380, style="right:-110px;top:120px")))
    return "2026-11-20-starting-a-business-checklist", s, st

def p13():
    """The 5-second test — Charcoal + sky."""
    A = dict(g=T["charcoal"], fg=T["sky"]); B = dict(g=T["sky"], fg=T["charcoal"])
    total = 8; s = []
    L = [[("i", "Does your website")], [("r", "pass the")], [("b", "5-second test?")]]
    f, st = cover_pair(A, total, L, "UX for business owners",
                       sparkle(T["sky"], 440, "right:-130px;top:170px") + seal(T["marigold"], 210, "4 questions", T["ink"], "left:600px;top:300px;transform:rotate(-10deg)", 34),
                       sparkle(T["sky"], 520, "right:-150px;top:330px") + seal(T["marigold"], 240, "4 questions", T["ink"], "left:560px;top:560px;transform:rotate(-10deg)", 38), 150)
    s.append(f)
    s.append(text_slide(B, 2, total, [[("r", "Visitors")], [("b", "decide fast.")]],
                        "In the first few seconds on your homepage, a visitor should be able to answer four questions. If they can’t, they leave.",
                        asterisk(T["charcoal"], 130, "right:88px;top:250px"), 150))
    steps = [("01", [[("r", "What do")], [("b", "you do?")]], "Say it plainly in the first headline. “Bridal wear in Jaipur” beats “Crafting dreams”."),
             ("02", [[("r", "Who is")], [("b", "it for?")]], "Name your customer, so the right people know instantly that this is for them."),
             ("03", [[("b", "Why"), ("r", "you?")]], "One clear reason, backed by proof: reviews, real work, years in the trade."),
             ("04", [[("r", "What do")], [("b", "I do next?")]], "One obvious button. Book a call, WhatsApp us or Shop now. Not five.")]
    for i, (num, tl, txt) in enumerate(steps):
        th = A if i % 2 == 0 else B
        s.append(step_slide(th, i + 3, total, num, tl, txt, asterisk(th["fg"], 130, "right:88px;top:250px")))
    s.append(text_slide(B, 7, total, [[("i", "Try it")], [("b", "today.")]],
                        "Open your site on your phone. Look for five seconds, then close it. Ask a friend the four questions.",
                        sparkle(T["charcoal"], 150, "right:88px;top:230px"), 150))
    s.append(cta_slide(A, 8, total, [[("r", "Want a")], [("b", "UX audit?")]], T["sky"], T["charcoal"],
                       sparkle(T["sky"], 300, "right:-70px;top:150px")))
    return "2026-11-21-five-second-website-test", s, st

def p14():
    """Holistic marketing — Cobalt + white."""
    A = dict(g=T["cobalt"], fg=T["white"]); B = dict(g=T["white"], fg=T["cobalt"])
    total = 8; s = []
    L = [[("i", "One channel")], [("r", "is not a")], [("b", "strategy.")]]
    f, st = cover_pair(A, total, L, "Holistic marketing",
                       asterisk(T["white"], 500, "right:-150px;top:160px"),
                       asterisk(T["white"], 600, "right:-170px;top:300px"), 170)
    s.append(f)
    s.append(text_slide(B, 2, total, [[("r", "Marketing is")], [("b", "a system.")]],
                        "Every channel has one job. When they work together, a stranger becomes a customer, then a fan.",
                        sparkle(T["cobalt"], 150, "right:88px;top:230px"), 140))
    steps = [("01", [[("b", "Get"), ("r", "found")]], "Instagram, Reels, Google and ads bring new people to you."),
             ("02", [[("b", "Build"), ("r", "trust")]], "Your website shows proof, prices and process. This is where people decide."),
             ("03", [[("b", "Convert")]], "One clear action: WhatsApp, a booking or checkout. Remove every extra step."),
             ("04", [[("r", "Stay in")], [("b", "touch")]], "WhatsApp broadcasts, email and retargeting bring people back when they’re ready."),
             ("05", [[("r", "Turn customers")], [("b", "into fans")]], "Reviews, referrals and repeat offers. Happy customers are your cheapest marketing.")]
    for i, (num, tl, txt) in enumerate(steps):
        th = A if i % 2 == 0 else B
        s.append(step_slide(th, i + 3, total, num, tl, txt, asterisk(th["fg"], 130, "right:88px;top:250px")))
    s.append(cta_slide(A, 8, total, [[("r", "Build the")], [("b", "whole system.")]], T["white"], T["cobalt"],
                       asterisk(T["white"], 340, "right:-90px;top:140px")))
    return "2026-11-22-one-channel-is-not-a-strategy", s, st

def p15():
    """Why your ads aren't converting — Triad (charcoal / lime, pink pop once)."""
    A = dict(g=T["charcoal"], fg=T["lime"]); B = dict(g=T["lime"], fg=T["charcoal"])
    total = 7; s = []
    L = [[("i", "Why your ads")], [("r", "aren’t")], [("b", "converting.")]]
    f, st = cover_pair(A, total, L, "Performance marketing",
                       sparkle(T["lime"], 440, "right:-130px;top:170px") + seal(T["pink"], 210, "5 reasons", T["ink"], "left:600px;top:300px;transform:rotate(-10deg)", 38),
                       sparkle(T["lime"], 520, "right:-150px;top:330px") + seal(T["pink"], 240, "5 reasons", T["ink"], "left:560px;top:560px;transform:rotate(-10deg)", 42), 170)
    s.append(f)
    steps = [("01", [[("r", "No page built")], [("b", "to convert")]], "Sending ad traffic to your profile grid makes people hunt for the thing they clicked on."),
             ("02", [[("b", "No tracking"), ("r", "set up")]], "Without the Meta Pixel and Google tags, you can’t see which ad made a sale, so you can’t scale it."),
             ("03", [[("r", "Boosting")], [("b", "isn’t a strategy")]], "The Boost button chases likes. Real campaigns are set up for leads or sales."),
             ("04", [[("r", "Stopping")], [("b", "too early")]], "Ads need time and data to learn. Judge them on cost per lead, not on day two."),
             ("05", [[("r", "The offer")], [("b", "isn’t clear")]], "Great targeting can’t fix a vague offer. Say what they get, what it costs and why now.")]
    for i, (num, tl, txt) in enumerate(steps):
        th = B if i % 2 == 0 else A
        s.append(step_slide(th, i + 2, total, num, tl, txt, asterisk(th["fg"], 130, "right:88px;top:250px")))
    s.append(cta_slide(A, 7, total, [[("r", "Make every")], [("b", "rupee count.")]], T["lime"], T["charcoal"],
                       sparkle(T["lime"], 300, "right:-70px;top:150px")))
    return "2026-11-23-why-your-ads-arent-converting", s, st

def p16():
    """What owners tell us — Pink + ink."""
    A = dict(g=T["pink"], fg=T["ink"]); B = dict(g=T["ink"], fg=T["pink"])
    total = 7; s = []
    L = [[("i", "Things business")], [("r", "owners tell us")], [("b", "every week.")]]
    f, st = cover_pair(A, total, L, "Real problems, real fixes",
                       sparkle(T["ink"], 380, "right:-90px;top:250px"),
                       sparkle(T["ink"], 460, "right:-120px;top:340px"), 150)
    s.append(f)
    qs = [([[("r", "I post every day")], [("b", "but get no sales.”")]], "Posting isn’t a funnel. Every post needs a next step: a link, an offer or a reason to DM."),
          ([[("r", "My nephew")], [("b", "made my website.”")]], "A good start. But a site also has to load fast on phones, show up on Google and lead to an enquiry."),
          ([[("r", "Ads don’t work")], [("b", "for my business.”")]], "Usually it’s the setup: no tracking, no landing page, no clear offer. Fix those first."),
          ([[("r", "I don’t have")], [("b", "time for marketing.”")]], "You need a system, not more effort: a calendar, batched content and someone to run it."),
          ([[("r", "I don’t know")], [("b", "what’s working.”")]], "Watch three numbers every month: enquiries, cost per enquiry and where they came from.")]
    for i, (ql, fix) in enumerate(qs):
        th = B if i % 2 == 0 else A
        s.append(quote_slide(th, i + 2, total, ql, fix, sparkle(th["fg"], 150, "right:88px;top:230px")))
    s.append(cta_slide(A, 7, total, [[("r", "Sound")], [("b", "familiar?")]], T["ink"], T["pink"],
                       sparkle(T["ink"], 300, "right:-70px;top:150px")))
    return "2026-11-24-what-business-owners-tell-us", s, st

def p17():
    """Old-school vs new-age marketing — Tangerine + ink."""
    A = dict(g=T["tangerine"], fg=T["ink"]); B = dict(g=T["ink"], fg=T["tangerine"])
    total = 7; s = []
    L = [[("i", "Old-school")], [("r", "vs")], [("b", "new-age marketing.")]]
    pent = [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]
    f, st = cover_pair(A, total, L, "Then → now",
                       pentomino(T["ink"], 130, pent, "right:-110px;top:170px"),
                       pentomino(T["ink"], 160, pent, "right:-140px;top:400px"), 150)
    s.append(f)
    rows = [("Pamphlets", [[("b", "Google")], [("r", "Business Profile")]], "People search “near me” before they step out. Be the first result they see."),
            ("Visiting cards", [[("r", "A")], [("b", "website")]], "One link with your work, prices and contact details, shared anywhere."),
            ("Word of mouth", [[("b", "Reviews"), ("r", "and")], [("b", "referrals")]], "Word of mouth still works. Now it’s written down where strangers can read it."),
            ("Newspaper ads", [[("r", "Targeted")], [("b", "digital ads")]], "Reach the people most likely to buy, and see what every rupee did."),
            ("Gut feel", [[("b", "Data")]], "Track enquiries and sales by source, so the next decision is easier.")]
    for i, (then, now, txt) in enumerate(rows):
        th = B if i % 2 == 0 else A
        sh = pentomino(th["fg"], 60, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], "right:88px;top:250px")
        s.append(vs_slide(th, i + 2, total, then, now, txt, sh))
    s.append(cta_slide(A, 7, total, [[("r", "Upgrade")], [("b", "your marketing.")]], T["ink"], T["tangerine"],
                       pentomino(T["ink"], 110, pent, "right:-60px;top:140px")))
    return "2026-11-25-old-school-vs-new-age-marketing", s, st

POSTS2 = dict(p11=p11, p12=p12, p13=p13, p14=p14, p15=p15, p16=p16, p17=p17)

if __name__ == "__main__":
    keys = sys.argv[1:] or list(POSTS2)
    jobs = []
    for k in keys:
        folder, slides, story = POSTS2[k]()
        for i, h in enumerate(slides):
            jobs.append((h, OUT / folder / f"feed_{i+1:02d}.jpg", FEED))
        jobs.append((story, OUT / folder / "story_01.jpg", STORY))
    render(jobs)
    print("rendered", len(jobs))
