"""Week 3 (27 Nov – 3 Dec 2026): trending-topic series — Black Friday, AI search, the Instagram algorithm,
Cyber Monday, 2027 design trends, Wrapped season, original content.
Run: python3 posts_w3.py [p18 p19 …]  → renders into ../out/<folder>/
"""
import sys
from posts import *  # frame, body, step_slide, cover_pair, cta_slide, chip, swipe_foot, FEED, STORY, OUT
from posts_w2 import text_slide, stat_slide
from kit import *

def steps_run(s, A, B, start, total, steps, first=None):
    first = first or A
    for i, (num, tl, txt) in enumerate(steps):
        th = first if i % 2 == 0 else (B if first is A else A)
        s.append(step_slide(th, start + i, total, num, tl, txt, asterisk(th["fg"], 130, "right:88px;top:250px")))

# =====================================================================
def p18():
    """Black Friday — Signature (charcoal + marigold)."""
    A = dict(g=T["charcoal"], fg=T["marigold"]); B = dict(g=T["marigold"], fg=T["charcoal"])
    total = 8; s = []
    L = [[("i", "Before you run")], [("r", "a Black Friday")], [("b", "sale.")]]
    f, st = cover_pair(A, total, L, "Black Friday · 27 Nov",
                       sparkle(T["marigold"], 440, "right:-130px;top:170px"),
                       sparkle(T["marigold"], 520, "right:-150px;top:330px"), 160)
    s.append(f)
    steps_run(s, A, B, 2, total, [
        ("01", [[("r", "Know your")], [("b", "margin first")]], "Work out the lowest price you can sell at and still make money. Then set the discount."),
        ("02", [[("r", "Discount the")], [("b", "right products")]], "Clear slow stock or push an entry product. Keep your bestsellers at full price."),
        ("03", [[("r", "One offer,")], [("b", "one line")]], "“Flat 20% off everything till Monday” beats a list of conditions nobody reads."),
        ("04", [[("r", "Set a real")], [("b", "end date")]], "A sale that never ends teaches customers to wait. Stop when you said you would."),
        ("05", [[("r", "Fix checkout")], [("b", "before the traffic")]], "Test the full purchase on your phone. A broken payment page wastes every rupee of ads."),
        ("06", [[("r", "Collect")], [("b", "contacts")]], "Get a WhatsApp number or email with every order, so you can sell again without a sale."),
    ], first=B)
    s.append(cta_slide(A, 8, total, [[("r", "Plan a sale")], [("b", "that builds the brand.")]], T["marigold"], T["charcoal"],
                       sparkle(T["marigold"], 300, "right:-70px;top:150px")))
    return "2026-11-27-before-you-run-a-black-friday-sale", s, st

def p19():
    """Can ChatGPT find your business — Charcoal + sky."""
    A = dict(g=T["charcoal"], fg=T["sky"]); B = dict(g=T["sky"], fg=T["charcoal"])
    total = 9; s = []
    L = [[("i", "Can ChatGPT")], [("r", "find your")], [("b", "business?")]]
    f, st = cover_pair(A, total, L, "AI search",
                       sparkle(T["sky"], 440, "right:-130px;top:170px") + seal(T["marigold"], 210, "5 fixes", T["ink"], "left:600px;top:300px;transform:rotate(-10deg)", 40),
                       sparkle(T["sky"], 520, "right:-150px;top:330px") + seal(T["marigold"], 240, "5 fixes", T["ink"], "left:560px;top:560px;transform:rotate(-10deg)", 44), 160)
    s.append(f)
    s.append(stat_slide(B, 2, total, "45%", [[("r", "of consumers")], [("b", "ask AI")]],
                        "use ChatGPT or other generative AI for local business recommendations.",
                        "Source: BrightLocal consumer survey, 2026", ""))
    s.append(stat_slide(A, 3, total, "42%", [[("r", "of AI answers")], [("b", "cite websites")]],
                        "In 2,00,000+ local AI searches, business websites were the top source. Google Business Profile came next, at about 29%.",
                        "Source: BrightLocal local AI visibility study, Sep 2026", ""))
    steps_run(s, A, B, 4, total, [
        ("01", [[("r", "A website that")], [("b", "says it plainly")]], "What you do, where you are and who it is for, in words a customer would type."),
        ("02", [[("r", "A complete")], [("b", "Google profile")]], "Category, hours, services, photos and a link to your site. Fill in every field."),
        ("03", [[("r", "Reviews that")], [("b", "name the service")]], "“Best bridal lehenga fitting in Jaipur” tells AI far more than “Great experience”."),
        ("04", [[("r", "The same details")], [("b", "everywhere")]], "Name, address and phone should match on your site, Google, Instagram and listings."),
        ("05", [[("r", "Answer real")], [("b", "questions")]], "Add an FAQ with prices, delivery areas and timelines. AI quotes clear answers."),
    ], first=B)
    s.append(cta_slide(A, 9, total, [[("r", "Get found")], [("b", "by people and AI.")]], T["sky"], T["charcoal"],
                       sparkle(T["sky"], 300, "right:-70px;top:150px")))
    return "2026-11-28-can-chatgpt-find-your-business", s, st

def p20():
    """What Instagram rewards in 2026 — Pink + ink."""
    A = dict(g=T["pink"], fg=T["ink"]); B = dict(g=T["ink"], fg=T["pink"])
    total = 8; s = []
    L = [[("i", "What Instagram")], [("r", "actually rewards")], [("b", "in 2026.")]]
    f, st = cover_pair(A, total, L, "Straight from Instagram",
                       sparkle(T["ink"], 380, "right:-90px;top:250px"),
                       sparkle(T["ink"], 460, "right:-120px;top:340px"), 150)
    s.append(f)
    s.append(text_slide(B, 2, total, [[("r", "Three numbers")], [("b", "matter most.")]],
                        "Head of Instagram Adam Mosseri has named them: sends per reach, likes per reach and average watch time.",
                        sparkle(T["pink"], 150, "right:88px;top:230px"), 140))
    steps_run(s, A, B, 3, total, [
        ("01", [[("r", "Posts people")], [("b", "send to a friend")]], "Sends now count for more than comments. Make things worth sharing: a checklist, a tip, a truth."),
        ("02", [[("r", "Likes from")], [("b", "the right people")]], "Likes are measured against how many people saw the post, not as a raw count."),
        ("03", [[("r", "Watch time")], [("b", "still counts")]], "Hook in the first second. Cut anything that doesn’t earn the next one."),
        ("04", [[("b", "Originals"), ("r", "win")]], "The original version of a post gets recommended. Accounts that keep reposting lose reach."),
        ("05", [[("b", "Carousels"), ("r", "beat")], [("r", "single photos")]], "And hashtags help people find you in search. They are not a reach hack."),
    ])
    s.append(cta_slide(A, 8, total, [[("r", "Post what")], [("b", "people share.")]], T["ink"], T["pink"],
                       sparkle(T["ink"], 300, "right:-70px;top:150px")))
    return "2026-11-29-what-instagram-rewards-in-2026", s, st

def p21():
    """Cyber Monday website check — Cobalt + white."""
    A = dict(g=T["cobalt"], fg=T["white"]); B = dict(g=T["white"], fg=T["cobalt"])
    total = 8; s = []
    L = [[("i", "Is your website")], [("r", "ready for")], [("b", "sale day?")]]
    f, st = cover_pair(A, total, L, "Cyber Monday · 30 Nov",
                       asterisk(T["white"], 500, "right:-150px;top:160px"),
                       asterisk(T["white"], 600, "right:-170px;top:300px"), 160)
    s.append(f)
    steps_run(s, A, B, 2, total, [
        ("01", [[("r", "It loads fast")], [("b", "on a phone")]], "Most sale traffic is mobile. Compress images and test on mobile data, not office Wi-Fi."),
        ("02", [[("r", "The offer is")], [("b", "seen first")]], "Put the deal at the top of the homepage, not three scrolls down."),
        ("03", [[("r", "Checkout in")], [("b", "a few taps")]], "Guest checkout, UPI and saved addresses. Every extra form field loses buyers."),
        ("04", [[("r", "Help is")], [("b", "one tap away")]], "A WhatsApp button on every product page answers the question that stops a sale."),
        ("05", [[("r", "Tracking")], [("b", "works")]], "Check the Meta Pixel and Google tags fire on purchase, so you know what sold."),
    ], first=B)
    s.append(text_slide(B, 7, total, [[("i", "Test it")], [("b", "today.")]],
                        "Place a real order on your own phone, start to finish. Fix the first thing that annoys you.",
                        sparkle(T["cobalt"], 150, "right:88px;top:230px"), 150))
    s.append(cta_slide(A, 8, total, [[("r", "Want a")], [("b", "website check?")]], T["white"], T["cobalt"],
                       asterisk(T["white"], 340, "right:-90px;top:140px")))
    return "2026-11-30-is-your-website-ready-for-sale-day", s, st

def p22():
    """2027 design trends — Editorial light (linen / ink, marigold shapes)."""
    A = dict(g=T["linen"], fg=T["ink"]); B = dict(g=T["ink"], fg=T["linen"])
    total = 7; s = []
    L = [[("i", "2027 design trends")], [("r", "worth")], [("b", "stealing.")]]
    f, st = cover_pair(A, total, L, "Trend report",
                       seal(T["marigold"], 540, style="right:-190px;top:160px"),
                       seal(T["marigold"], 640, style="right:-200px;top:380px"), 140)
    s.append(f)
    trends = [("01", [[("r", "Tactile")], [("b", "textures")]], "Paper grain, fabric weave, emboss. Brands want to feel touchable again, even on a screen."),
              ("02", [[("r", "Modern")], [("b", "heritage")]], "Old crafts in a new layout. Think block-print motifs on a clean grid. Jaipur has this in its bones."),
              ("03", [[("r", "Hand-drawn")], [("b", "elements")]], "Doodles, arrows and rough marks that prove a person made it."),
              ("04", [[("r", "Expressive")], [("b", "typography")]], "Type as the hero. Big, mixed weights, set with intent."),
              ("05", [[("r", "Bold")], [("b", "minimalism")]], "Fewer elements, louder ones. One colour, one shape, one message.")]
    for i, (num, tl, txt) in enumerate(trends):
        th = B if i % 2 == 0 else A
        s.append(step_slide(th, i + 2, total, num, tl, txt, asterisk(T["marigold"], 130, "right:88px;top:250px")))
    s.append(cta_slide(A, 7, total, [[("r", "Ready for")], [("b", "a 2027 refresh?")]], T["ink"], T["linen"],
                       seal(T["marigold"], 380, style="right:-110px;top:120px")))
    return "2026-12-01-2027-design-trends-worth-stealing", s, st

def p23():
    """Your brand's 2026 Wrapped — Triad (charcoal / lime)."""
    A = dict(g=T["charcoal"], fg=T["lime"]); B = dict(g=T["lime"], fg=T["charcoal"])
    total = 8; s = []
    L = [[("i", "Make your brand’s")], [("r", "2026")], [("b", "Wrapped.")]]
    f, st = cover_pair(A, total, L, "Wrapped season",
                       sparkle(T["lime"], 440, "right:-130px;top:170px") + seal(T["pink"], 210, "Year-end post", T["ink"], "left:600px;top:300px;transform:rotate(-10deg)", 32),
                       sparkle(T["lime"], 520, "right:-150px;top:330px") + seal(T["pink"], 240, "Year-end post", T["ink"], "left:560px;top:560px;transform:rotate(-10deg)", 36), 160)
    s.append(f)
    s.append(text_slide(B, 2, total, [[("r", "Everyone shares")], [("b", "their year.")]],
                        "December is when people love a recap. Give them yours: one carousel that tells your brand’s year in five slides.",
                        asterisk(T["charcoal"], 130, "right:88px;top:250px"), 140))
    steps_run(s, A, B, 3, total, [
        ("01", [[("r", "Your top")], [("b", "post")]], "Show the post your audience loved most, and say why you think it worked."),
        ("02", [[("r", "Your real")], [("b", "numbers")]], "Orders shipped, clients served, cities reached. Real figures only. Round down, never up."),
        ("03", [[("r", "A customer")], [("b", "moment")]], "A review, a thank-you message or a photo a customer sent you, shared with permission."),
        ("04", [[("r", "Behind the")], [("b", "scenes")]], "The messy desk, the first sample, the late night. People follow people."),
        ("05", [[("r", "What’s next")], [("b", "in 2027")]], "One teaser for next year gives people a reason to follow now."),
    ])
    s.append(cta_slide(A, 8, total, [[("r", "Want us to")], [("b", "design yours?")]], T["lime"], T["charcoal"],
                       sparkle(T["lime"], 300, "right:-70px;top:150px")))
    return "2026-12-02-make-your-brands-2026-wrapped", s, st

def p24():
    """Original content wins — Tangerine + ink."""
    A = dict(g=T["tangerine"], fg=T["ink"]); B = dict(g=T["ink"], fg=T["tangerine"])
    total = 8; s = []
    L = [[("i", "Original content")], [("r", "wins on")], [("b", "Instagram now.")]]
    pent = [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]
    f, st = cover_pair(A, total, L, "Platform update",
                       pentomino(T["ink"], 130, pent, "right:-110px;top:170px"),
                       pentomino(T["ink"], 160, pent, "right:-140px;top:400px"), 150)
    s.append(f)
    s.append(text_slide(B, 2, total, [[("r", "Instagram is")], [("b", "protecting originals.")]],
                        "On 17 November 2026 Instagram announced content protection: a tool that finds unauthorised reposts of creators’ Reels.",
                        pentomino(T["tangerine"], 60, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], "right:88px;top:250px"), 130))
    steps_run(s, A, B, 3, total, [
        ("01", [[("r", "Shoot")], [("b", "your own")]], "Your shop, your team, your process. Nobody else can post that."),
        ("02", [[("r", "Stop")], [("b", "reposting")]], "Accounts that keep reposting other people’s content get pushed out of recommendations."),
        ("03", [[("r", "Label")], [("b", "AI content")]], "Instagram says AI content isn’t held back for being AI. Label it and keep it yours."),
        ("04", [[("r", "Export")], [("b", "clean")]], "Editing apps are fine. Another app’s watermark on your video is not."),
        ("05", [[("r", "Protect")], [("b", "your originals")]], "If you’re eligible, enrol in content protection when the notification shows up."),
    ])
    s.append(cta_slide(A, 8, total, [[("r", "Make content")], [("b", "only you can make.")]], T["ink"], T["tangerine"],
                       pentomino(T["ink"], 110, pent, "right:-60px;top:140px")))
    return "2026-12-03-original-content-wins", s, st

POSTS3 = dict(p18=p18, p19=p19, p20=p20, p21=p21, p22=p22, p23=p23, p24=p24)

if __name__ == "__main__":
    keys = sys.argv[1:] or list(POSTS3)
    jobs = []
    for k in keys:
        folder, slides, story = POSTS3[k]()
        for i, h in enumerate(slides):
            jobs.append((h, OUT / folder / f"feed_{i+1:02d}.jpg", FEED))
        jobs.append((story, OUT / folder / "story_01.jpg", STORY))
    render(jobs)
    print("rendered", len(jobs))
