#!/usr/bin/env python3
"""Add 'Red Flags / Won't Invest' column to the master investor database."""

import csv
import sys

INPUT_FILE = "/data/.openclaw/workspace/projects/investor-outreach/MASTER-investor-database-v2.csv"
OUTPUT_FILE = INPUT_FILE  # Overwrite

# Red flags by investor name (case-insensitive matching)
INVESTOR_RED_FLAGS = {
    # --- Major VCs / Firms (by individual name) ---
    "fred wilson": "Won't invest outside network effects / marketplace / community thesis. Won't do deep tech or biotech. Historically NYC-focused. Dislikes overly polished decks — be direct. Source: AVC blog (avc.com), USV published thesis (usv.com/thesis).",
    "vinod khosla": "Won't invest in small markets or incremental improvements. Wants moonshot-scale impact. Won't back founders who don't deeply understand the science. Polarizing board member — can be very hands-on/opinionated. Source: khoslaventures.com/blog, multiple keynotes.",
    "keith rabois": "Very direct/blunt — low tolerance for unfocused pitches. Won't invest in 'bullets' (people who need direction) — only 'barrels' (self-directed executors). Moves fast and expects founders to move fast. Source: 20VC podcast, Stanford lectures, Twitter.",
    "naval ravikant": "Won't invest in founders who can't articulate clearly and concisely. Values first-principles thinking — dislikes pattern-matching pitches. Small check sizes ($25K-$250K). Source: Naval Podcast, Twitter tweetstorms, The Almanack of Naval Ravikant.",
    "max levchin": "Looks for strong technical abilities — won't invest in non-technical founders for technical products. Values 'immigrant mentality' — relentless drive. Source: Stanford CS183 talks, fintech conference keynotes.",
    "elad gil": "Decides fast — if he doesn't respond quickly, it's likely a pass. Won't invest in founders who aren't 'learning machines.' Prefers inflection-point companies. Source: High Growth Handbook (free online), blog.eladgil.com.",
    "sahil lavingia": "Won't invest in companies that require massive VC funding to survive. Values capital efficiency and indie/bootstrapper ethos. Makes decisions in days. Source: 'The Minimalist Entrepreneur' book, sahillavingia.com blog, Twitter @shl.",
    "dick costolo": "Focused on companies at intersection of large audiences and technology. Won't invest if you can't articulate your 'attention platform' story. Source: 01 Advisors content, multiple CEO/leadership talks.",
    "hiten shah": "Won't invest without strong product-market fit signals (retention, engagement, NPS). Wants to see data-driven founders with metrics dashboards. Source: hitenism.com blog, Twitter @hnshah, The Startup Chat podcast.",
    "mark pincus": "Focused on gaming, social, consumer internet. Won't invest without understanding of viral growth and engagement loops. Source: Zynga founding talks, Twitter.",
    "dylan field": "Backs 'multiplayer' products — tools designed for collaboration. Values design-forward thinking and developer experience. Source: Figma Config keynotes, Twitter @zoink.",
    "kevin lin": "Focused on gaming, creator economy, live streaming. Values founders who understand community engagement. Source: Twitch founding story talks.",
    "william hockey": "Focused on fintech infrastructure and API companies. Values founders building developer-facing financial tools. Source: Plaid founding story talks.",
    "kevin hartz": "Backs 'company builders' — repeat founders or operators who've scaled before. Values clear distribution/GTM thinking. Source: podcasts, Eventbrite founding talks.",
    "ruchi sanghvi": "Backs technical founders, especially women in tech. Looks for deep product thinking, virality, and network effects from first principles. Source: Twitter, South Park Commons community content.",
    "fred ehrsam": "Invests in crypto/web3 infrastructure and protocols only. Values technical founders at protocol layer. Medium decision timeline. Source: medium.com/@FEhrsam blog, Paradigm research papers.",
    "caterina fake": "Invests in 'products that delight' — consumer experiences with genuine joy. Values product taste and design sensibility. Source: caterina.net blog, Twitter @caterina.",
    "leah solivan": "Focused on marketplace companies and female founders. Values founders who understand two-sided marketplace dynamics. Source: TaskRabbit founding story talks, Fuel Capital content.",
    "adam draper": "Focused on 'sci-fi founders' building what seems impossible (VR/AR, crypto, space). Apply through boostvc.com accelerator. Source: adamdraper.com blog, Boost VC demos.",
    "dave morin": "Focused on climate, health, and community. Won't invest outside these areas. Source: Twitter @davemorin, Offline Ventures thesis.",
    "rahul vohra": "Won't invest without 'delightful' user experience. Values design-obsessed founders with extreme attention to detail. Source: PMF survey framework (First Round Review), rahulvohra.com blog.",
    "spencer rascoff": "Focused on real estate tech, media, and LA-based startups. Source: spencerrascoff.com blog, Twitter, Office Hours podcast.",
    "arlan hamilton": "Exclusively backs underrepresented founders (women, POC, LGBTQ+). Apply through backstagecapital.com. Source: 'It's About Damn Time' book, Your First Million podcast.",
    "cyan banister": "Looks for 'weird' and unconventional founders who don't fit typical VC pattern. Values authenticity and original thinking over pedigree. Source: interviews, Twitter @cyantist.",
    "pierre omidyar": "Focused on 'responsible technology' and 'individual empowerment.' Can be slow/bureaucratic process. Source: omidyar.com/blog, published areas of focus.",
    "laurene powell jobs": "Focused on education, immigration reform, environment, and media. Highly selective — warm intros required. Can be slow process. Source: emersoncollective.com.",
    "michael moritz": "Legendary but now largely retired from active Sequoia investing. Known for intense diligence. Source: multiple books, Sequoia content.",
    "divesh makan": "ICONIQ is ultra-exclusive — manages money for tech billionaires. Warm intros through LP network essential. Won't take cold outreach. Source: general industry knowledge.",
    "scooter braun": "Entertainment/media focused — unlikely to invest outside cultural/entertainment space. Source: TQ Ventures thesis, Twitter.",
    "gwyneth paltrow": "Only invests in wellness, beauty, and consumer health aligned with 'clean living' ethos. Limited traditional VC experience. Source: Goop content.",
    "dan martel": "Focused on SaaS only. Values founders who understand SaaS metrics deeply. Source: danmartell.com blog, YouTube channel, 'Buy Back Your Time' book.",
    "pejman nozad": "Looks for technical co-founding teams at earliest stages. Values 'raw talent and determination' over pedigree. Source: pear.vc/blog, Stanford talks.",
    "mar hershenson": "Invests at earliest stages in technical founders only. Pear runs a fellowship — apply there. Values deep technical ability. Source: pear.vc/blog, Stanford talks.",
    "jeff clavier": "Pioneer of micro-VC. Values 'founder obsession' — deep, almost irrational commitment to the problem. Writes small-to-medium seed checks. Source: jeff.uncork.vc blog, Twitter.",
    "charles hudson": "Pre-seed only. Values 'strong founder-market fit.' Invests before most VCs will. Accessible and responsive. Source: charleshudson.net blog, Twitter, precursorvc.com/blog.",
    "eric bahn": "Hustle Fund: Won't invest over $1M check size. Won't lead rounds. Backs 'hustlers, not pedigrees.' Values scrappiness and capital efficiency. 48-hour decisions. Source: hustlefund.vc website, Twitter @ericbahn.",
    "semil shah": "Pre-seed only in 'platforms and marketplaces.' Small checks ($100K-$500K). Makes fast decisions. Source: semilshah.com blog, haystackvc.com, Venture Stories podcast.",
    "geoff lewis": "Invests only in 'narrative violations' — companies where consensus narrative is wrong. Won't invest in consensus plays. Source: bedrockcap.com/letters, Twitter.",
    "aileen lee": "Coined 'unicorn.' Invests seed-stage only. Values diversity and inclusion. Source: cowboy.vc/blog, original TechCrunch 2013 unicorn piece.",
    "vinny lingham": "Focused on crypto, identity, African tech. Some controversy around Civic project. Source: general community knowledge, Twitter.",
    "david cohen": "Techstars co-founder. Values mentorship-driven approach. Source: davidgcohen.com blog, 'Do More Faster' book, Techstars content.",
    "arjun sethi": "Tribe Capital uses quantitative 'Magic 8-Ball' approach. Won't invest without strong retention curves and engagement metrics. Lead with product data, not narrative. Source: tribecap.co/blog.",
    "jason calacanis": "Won't invest if you can't explain it in 60 seconds. Hates long decks. Wants to see hustle and speed. Source: This Week in Startups podcast, LAUNCH events.",
    "greg kidd": "Focused on fintech, identity, and crypto only. Source: Hard Yaka thesis (hardyaka.com), Twitter.",
    "brianne kimmel": "Focused on future-of-work, SaaS, and community-driven products. Values technical founders building work tools. Source: briannekimmel.com blog, Twitter, Worklife newsletter.",
    "peter livingston": "Invests in 'unpopular' ideas — contrarian bets other VCs pass on. Apply through rolling fund. Source: unpopular.vc website.",
    "avichal garg": "Electric Capital: crypto/web3 infrastructure only. Values technical founders at protocol level. Source: electriccapital.com, annual Developer Report.",
    "auren hoffman": "Focused on data infrastructure and B2B data companies. Values founders who understand data as competitive moat. Source: summation.net blog, World of DaaS podcast.",
    "joe montana": "Liquid 2 Ventures: Accessible but lead with strong founding team credentials. Source: liquid2.vc thesis.",
    "niko bonatsos": "General Catalyst: Focused on consumer, gaming, media. Looks for 'culturally aware' founders who understand generational shifts. Source: generalcatalyst.com/perspectives, Twitter.",
    "mike volpi": "Index Ventures: Looks for 'category-defining companies.' Values founders who can articulate 'why now.' Source: indexventures.com/perspectives.",
    "marlon nichols": "MaC Venture Capital: Focused on diverse founders and companies leveraging cultural trends. Source: macventurecapital.com/blog.",
    "jesse draper": "Halogen: Focused on female-founded companies in consumer, health, family. Source: halogenvc.com, Valley Girl Show.",
    "deborah quazzo": "GSV: EdTech focus only. Looks for companies transforming how people learn. Source: gsv.com, ASU+GSV Summit.",
    "jennifer carolan": "Reach Capital: EdTech only. Needs 'efficacy data' — proof product improves learning outcomes. Source: reachcap.com.",
    "susan lyne": "BBG Ventures: Focused on female-founded consumer companies. Products 'designed for how women actually live.' Source: bbgventures.com/blog.",
    "theresia gouw": "Acrew Capital: Focused on cybersecurity, enterprise SaaS, marketplaces. Backs diverse founders. Source: acrewcapital.com/insights, Twitter.",
    "alexa von tobel": "Inspired Capital: Focused on fintech, insurance, 'resiliency' companies. Values mission-driven founders. Source: alexavontobel.com, 'Financially Fearless' book.",
    "edith yeung": "Race Capital: Focused on Asia/US cross-border tech. Backs founders building for global (especially Asian) markets. Source: edith.co blog, race.capital.",
    "ron suber": "Focused on lending, insurtech, wealth management technology only. Values founders who understand regulatory complexity. Source: public fintech talks.",
    "kanyi maqubela": "Kindred Ventures: Invests in 'kind founders' building with empathy and for communities. Impact investing and diverse founders focus. Source: blog.kanyi.me, Twitter.",
    "cindy padnos": "Illuminate Ventures: Enterprise/SaaS cloud companies at early stage only. Source: illuminate.com/insights.",
    "chris cantino": "Color Capital: Consumer brands and DTC only. Values brand building and customer acquisition expertise. Source: color.capital.",
}

# Red flags by fund/firm name (case-insensitive matching on Fund column)
FUND_RED_FLAGS = {
    "bessemer venture partners": "Famous anti-portfolio: passed on Google, Apple, Facebook, Airbnb, PayPal, Snapchat, eBay, Intel, FedEx. Won't invest pre-revenue at Series A — need clear path to $100M ARR. Medium-slow process (3-6 weeks). Source: bvp.com/anti-portfolio, Bessemer Roadmaps.",
    "bessemer": "Famous anti-portfolio: passed on Google, Apple, Facebook, Airbnb, PayPal, Snapchat, eBay, Intel, FedEx. Won't invest pre-revenue at Series A — need clear path to $100M ARR. Medium-slow process (3-6 weeks). Source: bvp.com/anti-portfolio, Bessemer Roadmaps.",
    "iqt": "CIA's venture arm — requires defense/national security relevance. Very specific use case. Slow process (2-6 months). Source: iqt.org published focus areas.",
    "iconiq capital": "Ultra-exclusive — manages money for tech billionaires (Zuckerberg, Dorsey, etc.). Warm intros through LP network essential. Won't take cold outreach. Medium-slow process. Source: general industry knowledge.",
    "softbank investment advisers": "Known for aggressive deal terms and pushing for high valuations. WeWork debacle hurt reputation significantly. Can be over-involved and push hypergrowth at cost of sustainability. Slow process (2-6 months). Source: extensive media coverage of WeWork, Masa Son's investment style.",
    "softbank": "Known for aggressive deal terms and pushing for high valuations. WeWork debacle hurt reputation significantly. Can be over-involved and push hypergrowth at cost of sustainability. Slow process (2-6 months). Source: extensive media coverage of WeWork, Masa Son's investment style.",
    "digital currency group": "Major crypto conglomerate but some concerns post-Genesis/Grayscale issues in 2022-23. Genesis filed bankruptcy. Check current status of DCG entities before engaging. Source: extensive 2022-23 media coverage.",
    "craft ventures": "David Sacks' firm — very opinionated. Known for strong product opinions on All-In Podcast. Can be vocal publicly about portfolio disagreements. Source: Craft Ventures writing, All-In Podcast.",
    "hustle fund": "Won't invest over $1M check size. Won't lead rounds. Pre-seed focus only. Values scrappiness over pedigree. 48-hour decisions. Source: hustlefund.vc website.",
    "emerson collective": "Impact/social focus required — won't invest purely for returns. Slow/bureaucratic process. Source: emersoncollective.com.",
    "backstage capital": "Exclusively backs underrepresented founders (women, POC, LGBTQ+). Small check sizes. Source: backstagecapital.com.",
    "kapor capital": "Focused on 'gap-closing' companies — must close gaps of access/opportunity for underrepresented communities. Social impact requirement. Source: kaporcapital.com/blog.",
    "cowboy ventures": "Seed-stage only. Values diversity and inclusion. Source: cowboy.vc/blog.",
    "tribe capital": "Data-driven 'Magic 8-Ball' approach — needs strong retention curves and engagement metrics upfront. Won't invest on narrative alone. Source: tribecap.co/blog.",
    "nfx": "Focused on companies with network effects — won't invest without a clear network effect. Published taxonomy at nfx.com. Source: nfx.com/post.",
    "pear vc": "Pre-seed/seed only. Technical co-founding teams required. Runs fellowship program. Source: pear.vc/blog.",
    "precursor ventures": "Pre-seed only. Values 'strong founder-market fit.' Source: precursorvc.com/blog.",
    "basis set ventures": "AI/ML companies only. Source: basisset.ventures/blog.",
    "haystack": "Pre-seed only in 'platforms and marketplaces.' Small checks. Source: haystackvc.com.",
    "bedrock capital": "Only invests in 'narrative violations' — won't do consensus plays. Source: bedrockcap.com/letters.",
    "electric capital": "Crypto/web3 infrastructure only. Source: electriccapital.com.",
    "boost vc": "Focused on 'sci-fi' frontier tech (VR/AR, crypto, space). Accelerator model — apply through boostvc.com. Source: boost.vc.",
    "chingona ventures": "Diversity-focused fund. Invests in underrepresented founders. Source: chingona.ventures.",
    "harlem capital": "Diversity-focused investing. Source: harlem.capital/blog.",
    "illuminate ventures": "Enterprise/SaaS cloud only. Source: illuminate.com/insights.",
    "halogen": "Female-founded companies focus. Consumer, health, family. Source: halogenvc.com.",
    "halogen capital": "Female-founded companies focus. Consumer, health, family. Source: halogenvc.com.",
    "bbg ventures": "Focused on female-founded consumer companies. Source: bbgventures.com/blog.",
    "bonfire ventures": "B2B software in LA only. Source: bonfirevc.com/blog.",
    "bam ventures": "Pre-seed/seed consumer brands in LA. Source: bamventures.com/blog.",
    "crosscut ventures": "LA-based seed fund. Source: crosscut.vc/blog.",
    "tenoneten": "LA-based seed fund focused on data science-driven companies. Source: tenoneten.net/blog.",
    "dbl partners": "Double bottom line required — social/environmental impact alongside returns. Source: dblinvestors.com.",
    "omidyar network": "Impact investing focus — 'responsible technology' and 'individual empowerment.' Can be slow/bureaucratic. Source: omidyar.com.",
    "angelpad": "Accelerator. Small check sizes ($50K-$120K). Source: angelpad.com.",
    "expert dojo": "Accelerator model. Small fund ($20M). Source: expertdojo.com.",
    "acrew capital": "Focused on cybersecurity, enterprise SaaS, marketplaces. Backs diverse founders. Source: acrewcapital.com/insights.",
    "inspired capital": "Focused on fintech, insurance, 'resiliency' companies. Source: Alexa von Tobel's published content.",
    "worklife ventures": "Future-of-work, SaaS, community-driven products only. Source: Brianne Kimmel's published thesis.",
    "social leverage": "Fintech seed investing focus. Source: socialleverage.com.",
    "volt capital": "Crypto/web3 only. Source: volt.capital.",
    "race capital": "Asia/US cross-border tech focus. Source: race.capital.",
    "kindred ventures": "Community-focused. Invests in 'kind founders' building with empathy. Source: kindredventures.com.",
    "mac venture capital": "Diversity-focused. Leveraging cultural trends. Source: macventurecapital.com/blog.",
    "blockchain capital": "Crypto/blockchain only. Source: blockchaincapital.com/research.",
    "paradigm": "Crypto/web3 infrastructure and protocols only. Source: paradigm.xyz research.",
    "1984 ventures": "Early-stage AI and enterprise focus. Source: 1984ventures.com/blog.",
    "645 ventures": "Data-driven seed investing, AI and data companies. Source: 645ventures.com/blog.",
    "a capital": "Deep tech and frontier companies. Source: A Capital thesis.",
    "acme capital": "Consumer and enterprise focus. Source: acme.vc/perspectives.",
    "crv": "Well-established but medium-slow process (3-6 weeks). Source: crv.com/content.",
    "charles river ventures": "Well-established but medium-slow process (3-6 weeks). Source: crv.com/content.",
    "flybridge": "Seed-stage in NYC. Enterprise and AI with strong technical teams. Source: flybridge.com.",
    "index ventures": "Looks for 'category-defining companies.' Values founders who articulate 'why now.' Source: indexventures.com/perspectives.",
    "general catalyst": "Large fund — can be slow. Medium process (3-6 weeks). Source: generalcatalyst.com/perspectives.",
    "khosla ventures": "Won't invest in small markets or incremental improvements. Wants moonshot-scale. Polarizing board involvement. Source: khoslaventures.com/blog.",
    "accel": "Top-tier but medium process (3-6 weeks). Source: accel.com/noteworthy.",
    "temasek": "Massive Singapore sovereign wealth fund. Very long process (2-6 months). Professional but bureaucratic. Source: temasek.com.sg.",
}

def get_red_flags(name, fund, investor_type, sectors):
    """Look up red flags for a given investor."""
    if not name:
        return ""
    
    name_lower = name.strip().lower()
    # Remove CFA, etc. suffixes for matching
    for suffix in [", cfa", " cfa", " iii", " iv", " jr.", " jr", " sr.", " sr"]:
        if name_lower.endswith(suffix):
            name_lower = name_lower[:-len(suffix)].strip()
    
    # Check by investor name
    if name_lower in INVESTOR_RED_FLAGS:
        return INVESTOR_RED_FLAGS[name_lower]
    
    # Check partial name matches (first + last)
    for key, value in INVESTOR_RED_FLAGS.items():
        if key in name_lower or name_lower in key:
            return value
    
    # Check by fund name
    if fund:
        fund_lower = fund.strip().lower()
        for key, value in FUND_RED_FLAGS.items():
            if key in fund_lower or fund_lower in key:
                return value
    
    return ""


def main():
    # Read the CSV
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)
    
    # Find column indices
    name_idx = 0  # Name is first column
    fund_idx = headers.index("Fund") if "Fund" in headers else None
    type_idx = headers.index("Type of Investor") if "Type of Investor" in headers else None
    sector_idx = headers.index("Sector: Investment Thesis") if "Sector: Investment Thesis" in headers else None
    
    # Add new column header
    headers.append("Red Flags / Won't Invest")
    
    filled_count = 0
    total_count = len(rows)
    
    for row in rows:
        # Ensure row has enough columns
        while len(row) < len(headers) - 1:
            row.append("")
        
        name = row[name_idx] if name_idx < len(row) else ""
        fund = row[fund_idx] if fund_idx and fund_idx < len(row) else ""
        inv_type = row[type_idx] if type_idx and type_idx < len(row) else ""
        sectors = row[sector_idx] if sector_idx and sector_idx < len(row) else ""
        
        red_flags = get_red_flags(name, fund, inv_type, sectors)
        row.append(red_flags)
        
        if red_flags:
            filled_count += 1
    
    # Write output
    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    
    print(f"Total rows processed: {total_count}")
    print(f"Red flags filled: {filled_count}")
    print(f"Left blank: {total_count - filled_count}")
    print(f"\nSample filled entries:")
    
    count = 0
    for row in rows:
        if row[-1] and count < 15:
            print(f"  - {row[0]}: {row[-1][:80]}...")
            count += 1


if __name__ == "__main__":
    main()
