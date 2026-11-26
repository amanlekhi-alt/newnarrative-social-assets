"""Builds the 27 Nov – 3 Dec schedule entries (week 3: trending topics, carousel + Reel with music)
and appends them to schedule.json.
New fields: reel_url, reel_cover_url, reel_caption, music_track (the original track baked into the Reel).
"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
RAW = "https://raw.githubusercontent.com/amanlekhi-alt/newnarrative-social-assets/main/"
FOOT = ("New Narrative is a branding and design studio in Jaipur: brand identity, website design & UI/UX, "
        "social media management, performance marketing and AI-assisted creative.\n\n"
        "DM us or visit www.newnarrative.studio\n\n📍 Jaipur, India · Working with brands across India\n\n")
BASE_TAGS = "#NewNarrativeStudio #DesignStudioJaipur #JaipurBusiness #SmallBusinessIndia"
TRACK = "Original track by New Narrative Studio (made with ElevenLabs Music)"

# date, slug, slides, in-app music suggestion (carousel), carousel caption, reel hook caption, hashtags
POSTS = [
 ("2026-11-27", "before-you-run-a-black-friday-sale", 8, 'Ritviz, "Liggi"',
  "Before you run a Black Friday sale, read this 🏷️\n\nKnow your margin first. Discount the right products. Say the offer in one line. Set a real end date. Fix checkout before the traffic arrives. Collect contacts so you can sell again without a sale.\n\nA good sale brings in new customers. A bad one trains your old ones to wait.\n\nSave this and send it to a founder planning a sale this weekend.",
  "Black Friday is today. Six checks before you discount anything 🏷️\n\nThe full checklist is in today's carousel on our profile. Save it for every sale you run.",
  "#BlackFriday #BlackFridaySale #D2CIndia #EcommerceIndia"),
 ("2026-11-28", "can-chatgpt-find-your-business", 9, 'Anuv Jain, "Husn"',
  "Can ChatGPT find your business? 🤖\n\n45% of consumers now use ChatGPT or other AI tools for local business recommendations (BrightLocal, 2026). In a study of 2,00,000+ local AI searches, business websites were the top source AI cited, followed by Google Business Profiles (BrightLocal, Sep 2026).\n\nFive fixes: a website that says it plainly, a complete Google profile, reviews that name the service, the same details everywhere, and an FAQ with real answers.\n\nAsk ChatGPT for \"the best [your service] in [your city]\" today. Are you in the answer?",
  "Ask ChatGPT for the best business like yours in your city. Are you in the answer? 🤖\n\nFive fixes that help AI find you are in today's carousel on our profile.",
  "#AISearch #ChatGPT #LocalSEO #GoogleBusinessProfile"),
 ("2026-11-29", "what-instagram-rewards-in-2026", 8, 'Seedhe Maut, "Namastute"',
  "What Instagram actually rewards in 2026 📈\n\nHead of Instagram Adam Mosseri has named the numbers that matter most: sends per reach, likes per reach and average watch time. Shares to a friend now count for more than comments.\n\nOriginal posts get recommended, reposts lose reach, carousels beat single photos, and hashtags help search but aren't a reach hack.\n\nSend this to the person who runs your Instagram.",
  "Comments aren't the metric that matters most on Instagram anymore 📈\n\nHere's what is, straight from the Head of Instagram. Full breakdown in today's carousel.",
  "#InstagramTips #InstagramAlgorithm #SocialMediaMarketing #ContentStrategy"),
 ("2026-11-30", "is-your-website-ready-for-sale-day", 8, 'Divine, "Mirchi"',
  "Is your website ready for sale day? 🛒\n\nIt's Cyber Monday. Before you send traffic anywhere, check five things: it loads fast on a phone, the offer is seen first, checkout takes a few taps, help is one tap away on WhatsApp, and your tracking actually works.\n\nThen place a real order on your own phone, start to finish, and fix the first thing that annoys you.",
  "Cyber Monday test: place a real order on your own website, on your phone 🛒\n\nThe five things to check are in today's carousel on our profile.",
  "#CyberMonday #WebsiteDesign #EcommerceTips #ConversionRate"),
 ("2026-12-01", "2027-design-trends-worth-stealing", 7, 'Prateek Kuhad, "cold/mess"',
  "2027 design trends worth stealing ✍️\n\nTactile textures, modern heritage, hand-drawn elements, expressive typography and bold minimalism.\n\nOur pick from a Jaipur studio: modern heritage. Old crafts like block print, set on a clean, modern grid. It's distinctive, it's local, and nobody can copy where you come from.\n\nWhich one would you use for your brand?",
  "Five design trends for 2027, and the one we'd bet on ✍️\n\nSee all five in today's carousel on our profile.",
  "#DesignTrends2027 #BrandingTrends #GraphicDesign #BrandIdentity"),
 ("2026-12-02", "make-your-brands-2026-wrapped", 8, 'The Local Train, "Choo Lo"',
  "Make your brand's 2026 Wrapped 🎁\n\nIt's recap season, and people love looking back. Give them your year in five slides: your top post, your real numbers, a customer moment, a look behind the scenes and a teaser for 2027.\n\nReal figures only. Round down, never up.\n\nSave this template for your year-end post.",
  "Everyone's sharing their year. Here's how to make your brand's 🎁\n\nThe five-slide template is in today's carousel on our profile.",
  "#YearInReview #BrandWrapped #SocialMediaIdeas #ContentIdeas"),
 ("2026-12-03", "original-content-wins", 8, 'Raftaar, "Swag Mera Desi"',
  "Original content wins on Instagram now 🎬\n\nOn 17 November 2026, Instagram announced content protection, a tool that finds unauthorised reposts of creators' Reels. Accounts that keep reposting other people's content get pushed out of recommendations.\n\nShoot your own. Stop reposting. Label AI content. Export clean, without another app's watermark. And protect your originals if you're eligible.\n\nYour shop, your team and your process are content nobody else can make.",
  "Reposting other people's Reels? Instagram is now pushing back 🎬\n\nWhat changed and what to do instead is in today's carousel on our profile.",
  "#InstagramUpdate #OriginalContent #ContentCreator #InstagramReels"),
]

def entries():
    out = []
    for date, slug, n, music, body, hook, tags in POSTS:
        folder = f"{date}-{slug}"
        feed = [f"feed_{i:02d}.jpg" for i in range(1, n + 1)]
        out.append(dict(date=date, slug=slug, folder=folder, feed=feed, story="story_01.jpg",
                        tag_username="theamanlekhishow", music_suggestion=music,
                        caption=f"{body}\n\n{FOOT}{tags} {BASE_TAGS}",
                        feed_urls=[RAW + folder + "/" + f for f in feed],
                        story_url=RAW + folder + "/story_01.jpg",
                        reel_url=RAW + folder + "/reel.mp4",
                        reel_cover_url=RAW + folder + "/reel_cover.jpg",
                        reel_caption=f"{hook}\n\n{FOOT}{tags} {BASE_TAGS}",
                        music_track=TRACK,
                        post_time_ist="10:00"))
    return out

if __name__ == "__main__":
    p = ROOT / "schedule.json"; d = json.load(open(p))
    have = {e["date"] for e in d}
    d += [e for e in entries() if e["date"] not in have]
    json.dump(d, open(p, "w"), indent=2, ensure_ascii=False); print(len(d), "entries")
