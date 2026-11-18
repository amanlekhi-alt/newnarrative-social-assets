"""Builds the 19–25 Nov schedule entries (week 2) and appends them to schedule.json."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
RAW = "https://raw.githubusercontent.com/amanlekhi-alt/newnarrative-social-assets/main/"
FOOT = ("New Narrative is a branding and design studio in Jaipur: brand identity, website design & UI/UX, "
        "social media management, performance marketing and AI-assisted creative.\n\n"
        "DM us or visit www.newnarrative.studio\n\n📍 Jaipur, India · Working with brands across India\n\n")
BASE_TAGS = "#NewNarrativeStudio #DesignStudioJaipur #JaipurBusiness #SmallBusinessIndia"
POSTS = [
 ("2026-11-19", "why-instagram-isnt-enough", 8, 'Bonobo, "Kerala"',
  "Why Instagram isn't enough for your business 📲\n\nInstagram is rented space. Your website is owned. In one study of 40,000 Indian MSMEs, only 402 had a website that actually worked (SERP Forge, Dec 2025).\n\nA website gets you found on Google, earns trust before the first call, takes enquiries while you sleep and gives your ads somewhere to land.\n\nSave this for the day your reach drops.",
  "#WebsiteDesign #SmallBusinessWebsite #DigitalPresence #BusinessGrowth"),
 ("2026-11-20", "starting-a-business-checklist", 8, 'Tycho, "Awake"',
  "Starting a business? Set these 6 things up first ✅\n\nA name you can own, a Google Business Profile, a simple website, WhatsApp Business, brand basics and one way to measure what's working.\n\nNone of it is expensive. All of it is easier to do on day one than to fix in year two.\n\nSave this checklist and send it to a friend who's starting up.",
  "#StartupIndia #NewBusiness #BusinessSetup #EntrepreneurIndia"),
 ("2026-11-21", "five-second-website-test", 8, 'FKJ, "Ylang Ylang"',
  "Does your website pass the 5-second test? ⏱️\n\nIn the first few seconds, a visitor should know what you do, who it's for, why you and what to do next. If they can't, they leave.\n\nA quick UX check from 8+ years of designing digital products: open your site on your phone, look for five seconds, close it, and ask a friend the four questions.",
  "#UXDesign #WebsiteUX #ConversionRate #WebDesignIndia"),
 ("2026-11-22", "one-channel-is-not-a-strategy", 8, 'Khruangbin, "Maria También"',
  "One channel is not a marketing strategy 🔁\n\nHolistic marketing means every channel has a job: social and ads get you found, your website builds trust, WhatsApp and checkout convert, follow-ups bring people back, and reviews turn customers into fans.\n\nWhen one piece is missing, the rest work harder for less.",
  "#HolisticMarketing #DigitalMarketing #MarketingStrategy #MarketingFunnel"),
 ("2026-11-23", "why-your-ads-arent-converting", 7, 'Nujabes, "Aruarian Dance"',
  "Why your ads aren't converting 📉\n\nUsually it isn't the ad. It's the setup: no landing page, no Meta Pixel or tracking, boosting instead of real campaigns, stopping too early, or an offer that isn't clear.\n\nFix these five before you spend another rupee.",
  "#PerformanceMarketing #MetaAds #GoogleAds #LeadGeneration"),
 ("2026-11-24", "what-business-owners-tell-us", 7, 'Prateek Kuhad, "Kasoor"',
  "Things business owners tell us every week 💬\n\n\"I post every day but get no sales.\" \"Ads don't work for my business.\" \"I don't have time for marketing.\"\n\nEach one has a real reason behind it, and a fix. Swipe for the why behind each.\n\nWhich one sounds like you? Tell us in the comments.",
  "#BusinessOwner #MarketingTips #SocialMediaMarketing #WebsiteDesign"),
 ("2026-11-25", "old-school-vs-new-age-marketing", 7, 'Ritviz, "Udd Gaye"',
  "Old-school vs new-age marketing 🔄\n\nPamphlets became Google Business Profile. Visiting cards became a website. Word of mouth became reviews. Newspaper ads became targeted digital ads. Gut feel became data.\n\nThe goal hasn't changed: be found, be trusted, be chosen. The tools have.",
  "#DigitalMarketingIndia #NewAgeMarketing #GoogleBusinessProfile #MarketingStrategy"),
]
def entries():
    out = []
    for date, slug, n, music, body, tags in POSTS:
        folder = f"{date}-{slug}"
        feed = [f"feed_{i:02d}.jpg" for i in range(1, n + 1)]
        out.append(dict(date=date, slug=slug, folder=folder, feed=feed, story="story_01.jpg",
                        tag_username="theamanlekhishow", music_suggestion=music,
                        caption=f"{body}\n\n{FOOT}{tags} {BASE_TAGS}",
                        feed_urls=[RAW + folder + "/" + f for f in feed],
                        story_url=RAW + folder + "/story_01.jpg", post_time_ist="10:00"))
    return out
if __name__ == "__main__":
    p = ROOT / "schedule.json"; d = json.load(open(p))
    have = {e["date"] for e in d}
    d += [e for e in entries() if e["date"] not in have]
    json.dump(d, open(p, "w"), indent=2, ensure_ascii=False); print(len(d), "entries")
