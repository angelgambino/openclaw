#!/usr/bin/env python3
"""Build Pitch Slam 100 investor list from three data sources."""
import csv
import re
import json
import sys

# Target sectors for matching
TARGET_SECTORS = [
    'impact', 'health', 'wellness', 'human potential', 'sports', 'entertainment',
    'media', 'ai', 'artificial intelligence', 'machine learning', 'fitness',
    'digital media', 'social impact', 'mental health', 'life sciences',
    'healthcare', 'biotech', 'biotechnology', 'pharmaceutical', 'medical',
    'consumer', 'diversity', 'female founders', 'clean tech', 'sustainability',
    'education', 'creator economy', 'content', 'music', 'video', 'gaming',
    'esports', 'lifestyle', 'beauty', 'food', 'beverage'
]

# Sectors that are STRONG matches (core thesis)
STRONG_SECTORS = [
    'impact', 'health', 'wellness', 'human potential', 'sports', 'entertainment',
    'media', 'ai', 'artificial intelligence', 'machine learning', 'fitness',
    'digital media', 'social impact', 'mental health', 'creator economy',
    'music', 'gaming', 'esports', 'content', 'video'
]

def sector_score(sectors_text):
    """Score how well sectors match target. Higher = better."""
    if not sectors_text:
        return 0
    text = sectors_text.lower()
    strong = sum(1 for s in STRONG_SECTORS if s in text)
    general = sum(1 for s in TARGET_SECTORS if s in text)
    return strong * 3 + general

def classify_investor_type(fund_type_text, sectors_text=''):
    """Classify investor type."""
    if not fund_type_text:
        return 'Angel'
    t = fund_type_text.lower()
    if 'accelerator' in t:
        return 'Accelerator'
    if 'corporate' in t or 'cvc' in t:
        return 'CVC'
    if 'family office' in t:
        return 'Family Office'
    if 'impact' in t:
        return 'VC'
    if 'vc' in t or 'venture capital' in t or 'institutional' in t:
        return 'VC'
    if 'growth' in t:
        return 'VC'
    if 'studio' in t:
        return 'VC'
    return 'VC'

def has_early_stage(stage_text):
    """Check if investor does early stage."""
    if not stage_text:
        return True  # Unknown = maybe
    t = stage_text.lower()
    return any(s in t for s in ['seed', 'pre-seed', 'preseed', 'series a', 'angel', 'early'])

def map_sectors_display(sectors_text):
    """Create a clean display of matching sectors."""
    if not sectors_text:
        return ''
    text = sectors_text.lower()
    found = []
    mapping = {
        'AI': ['artificial intelligence', 'ai', 'machine learning'],
        'Health & Wellness': ['health', 'wellness', 'fitness'],
        'Impact': ['impact', 'social impact', 'sustainability', 'clean tech'],
        'Media & Entertainment': ['media', 'entertainment', 'digital media', 'content', 'music', 'video'],
        'Sports': ['sports', 'esports', 'gaming'],
        'Healthcare': ['healthcare', 'biotech', 'life sciences', 'medical', 'pharmaceutical'],
        'Consumer': ['consumer', 'lifestyle', 'beauty', 'food'],
        'Education': ['education', 'edtech'],
    }
    for label, keywords in mapping.items():
        if any(k in text for k in keywords):
            found.append(label)
    return ', '.join(found) if found else sectors_text[:80]

def generate_why_fit(name, firm, sectors_display, inv_type):
    """Generate a one-sentence 'Why They're a Fit'."""
    sector_str = sectors_display if sectors_display else 'early-stage startups'
    if 'AI' in sectors_display and 'Health' in sectors_display:
        return f"{name}'s focus on AI and health/wellness at {firm} directly aligns with Pitch Slam's core thesis areas, making them an ideal breakout room host for founders at the intersection of technology and human potential."
    elif 'AI' in sectors_display:
        return f"{name}'s active AI investment thesis at {firm} makes them a perfect match for Pitch Slam's AI-focused founders seeking early-stage capital."
    elif 'Health' in sectors_display or 'Healthcare' in sectors_display:
        return f"{name}'s health and wellness investment focus at {firm} aligns perfectly with Pitch Slam's human potential and wellness track."
    elif 'Impact' in sectors_display:
        return f"{name}'s impact investing thesis at {firm} connects directly with Pitch Slam's mission-driven founders building for positive social outcomes."
    elif 'Media' in sectors_display or 'Entertainment' in sectors_display:
        return f"{name}'s media and entertainment expertise at {firm} makes them an ideal breakout room host for Pitch Slam's creative economy founders."
    elif 'Sports' in sectors_display:
        return f"{name}'s sports and entertainment investment focus at {firm} directly matches Pitch Slam's sports and human potential tracks."
    elif 'Consumer' in sectors_display:
        return f"{name}'s consumer-focused thesis at {firm} aligns with Pitch Slam's consumer health, wellness, and lifestyle founders."
    else:
        return f"{name}'s investment focus at {firm} in {sector_str} aligns with Pitch Slam's early-stage founders building innovative solutions."

def generate_personalized_intro(first_name, firm, sectors_display, inv_type, past_investments=''):
    """Generate a personalized 2-3 sentence email intro."""
    # Reference specific portfolio companies if available
    portfolio_ref = ''
    if past_investments:
        companies = [c.strip() for c in past_investments.split(',') if c.strip()][:3]
        if companies:
            portfolio_ref = f" Your portfolio — including {', '.join(companies)} — "
    
    if 'AI' in sectors_display and 'Health' in sectors_display:
        return f"Hi {first_name}, I've been following {firm}'s work at the intersection of AI and health — exactly the kind of thesis-driven investing we celebrate at Pitch Slam.{portfolio_ref or ' '} As a breakout room host, you'd be matched with early-stage founders building in AI and human potential — the founders who are redefining how technology serves human wellness. I think you'd love the caliber of pitches and the energy of the room."
    elif 'AI' in sectors_display:
        return f"Hi {first_name}, {firm}'s commitment to AI-first companies caught my attention.{portfolio_ref or ' '} We're hosting Pitch Slam with SeedLegals and I'd love to feature you as a breakout room host — you'd meet pre-screened AI founders building real products, matched specifically to your thesis. The format is high-energy, high-signal, and designed for investors who want to cut through the noise."
    elif 'Health' in sectors_display or 'Healthcare' in sectors_display:
        return f"Hi {first_name}, {firm}'s focus on health and wellness innovation is exactly why I'm reaching out.{portfolio_ref or ' '} For our upcoming Pitch Slam (co-hosted with SeedLegals), we're looking for breakout room hosts who can give health-focused founders real, actionable feedback — and potentially write checks. Your expertise would make a huge difference for the founders in the room."
    elif 'Impact' in sectors_display:
        return f"Hi {first_name}, {firm}'s impact-driven thesis resonated with what we're building at Angel Club.{portfolio_ref or ' '} Pitch Slam is our signature virtual pitch event, and as a breakout room host, you'd be matched with mission-driven founders whose work aligns with your investment focus. Over 30% of past pitches have led to follow-up meetings — this is real deal flow."
    elif 'Media' in sectors_display or 'Entertainment' in sectors_display:
        return f"Hi {first_name}, {firm}'s position in media and entertainment investing makes you a perfect fit for Pitch Slam.{portfolio_ref or ' '} We're curating breakout rooms by sector, and I'd love you to host the media & entertainment track — meeting founders building the next wave of content, creator tools, and digital experiences. It's a high-signal format designed for serious investors."
    elif 'Sports' in sectors_display:
        return f"Hi {first_name}, {firm}'s sports and entertainment thesis is exactly what our Pitch Slam founders need.{portfolio_ref or ' '} As a breakout room host, you'd meet pre-vetted founders building in sports tech and human performance. The event is virtual, high-energy, and designed to maximize quality conversations between investors and founders."
    elif 'Consumer' in sectors_display:
        return f"Hi {first_name}, {firm}'s consumer investment thesis aligns beautifully with the founders pitching at our upcoming Pitch Slam.{portfolio_ref or ' '} As a breakout room host, you'd be matched with consumer health, wellness, and lifestyle startups tailored to your areas of interest. It's a curated, high-signal format — no wasted time."
    else:
        return f"Hi {first_name}, I've been impressed by {firm}'s investment approach and think you'd be a fantastic breakout room host at our upcoming Pitch Slam.{portfolio_ref or ' '} Co-hosted with SeedLegals, the event matches investors like you with early-stage founders in your thesis areas. Over 30% of past pitches led to follow-up meetings and investment — this is real, curated deal flow."

# ===== PROCESS ANGEL SYNDICATE DATA =====
print("Processing Angel Syndicate data...")
angel_investors = []
with open('angel-syndicate.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)
    # Find header row
    header_idx = None
    for i, row in enumerate(rows):
        if len(row) >= 5 and row[0].strip() == 'First Name' and row[1].strip() == 'Last Name':
            header_idx = i
            break
    
    if header_idx is not None:
        headers = rows[header_idx]
        for row in rows[header_idx+1:]:
            if len(row) >= 5 and row[0].strip():
                first = row[0].strip()
                last = row[1].strip()
                email = row[2].strip() if len(row) > 2 else ''
                company = row[3].strip() if len(row) > 3 else ''
                linkedin = row[4].strip() if len(row) > 4 else ''
                sectors = row[5].strip() if len(row) > 5 else ''
                past_inv = row[6].strip() if len(row) > 6 else ''
                
                if not email or not first:
                    continue
                
                score = sector_score(sectors)
                angel_investors.append({
                    'first_name': first,
                    'last_name': last,
                    'email': email,
                    'firm': company,
                    'linkedin': linkedin,
                    'sectors_raw': sectors,
                    'sectors_display': map_sectors_display(sectors),
                    'past_investments': past_inv,
                    'investor_type': 'Angel',
                    'stage': 'Pre-seed, Seed',
                    'website': '',
                    'twitter': '',
                    'score': score,
                    'source': 'angel_syndicate'
                })

print(f"  Found {len(angel_investors)} angel investors with emails")

# ===== PROCESS VC DATABASE =====
print("Processing VC Database...")
vc_investors = []
with open('vc-database.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)
    if rows:
        headers = rows[0]
        # Fund,Primary Location,Investment Sectors,Fund Type,Current Fund Size,Stage Invested,Average check size,State (if U.S.),Investment Geography,Info,URL,Linkedin,Country
        for row in rows[1:]:
            if len(row) < 10:
                continue
            fund = row[0].strip()
            location = row[1].strip()
            sectors = row[2].strip()
            fund_type = row[3].strip()
            fund_size = row[4].strip()
            stage = row[5].strip()
            check_size = row[6].strip()
            state = row[7].strip() if len(row) > 7 else ''
            geo = row[8].strip() if len(row) > 8 else ''
            info = row[9].strip() if len(row) > 9 else ''
            url = row[10].strip() if len(row) > 10 else ''
            linkedin = row[11].strip() if len(row) > 11 else ''
            country = row[12].strip() if len(row) > 12 else ''
            
            if not fund:
                continue
            
            # US filter
            is_us = 'United States' in country or bool(state)
            if not is_us:
                continue
            
            # Stage filter
            if not has_early_stage(stage):
                continue
            
            score = sector_score(sectors)
            inv_type = classify_investor_type(fund_type, sectors)
            
            vc_investors.append({
                'first_name': '',  # VC funds don't have individual names in this sheet
                'last_name': '',
                'email': '',  # No individual emails
                'firm': fund,
                'linkedin': linkedin,
                'sectors_raw': sectors,
                'sectors_display': map_sectors_display(sectors),
                'past_investments': '',
                'investor_type': inv_type,
                'stage': stage,
                'website': url,
                'twitter': '',
                'score': score,
                'source': 'vc_database',
                'state': state,
                'location': location,
                'info': info
            })

print(f"  Found {len(vc_investors)} US-based early-stage VC funds")

# ===== PROCESS NEEDLE LIST =====
print("Processing Needle List...")
needle_investors = []
with open('needle-list.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)
    if rows:
        headers = rows[0]
        for row in rows[1:]:
            if len(row) < 7:
                continue
            investor = row[1].strip()
            inv_type = row[2].strip()
            email = row[3].strip()
            website = row[4].strip()
            city = row[5].strip()
            description = row[6].strip()
            country = row[10].strip() if len(row) > 10 else ''
            social = row[14].strip() if len(row) > 14 else ''
            
            if not investor or not email:
                continue
            
            # US filter
            is_us = country == 'US' or any(c in city for c in ['San Francisco', 'New York', 'Los Angeles', 'Chicago', 'Boston'])
            if not is_us:
                continue
            
            # Map investor type
            if 'Family Office' in inv_type:
                mapped_type = 'Family Office'
            elif 'CVC' in inv_type or 'Strategic' in inv_type:
                mapped_type = 'CVC'
            else:
                mapped_type = 'VC'
            
            score = sector_score(description)
            
            needle_investors.append({
                'first_name': '',
                'last_name': '',
                'email': email,
                'firm': investor,
                'linkedin': '',
                'sectors_raw': description,
                'sectors_display': map_sectors_display(description),
                'past_investments': '',
                'investor_type': mapped_type,
                'stage': 'Seed, Series A',
                'website': website,
                'twitter': '',
                'score': score,
                'source': 'needle',
                'city': city
            })

print(f"  Found {len(needle_investors)} US-based Needle investors")

# ===== COMBINE AND SELECT TOP 100 =====
print("\nSelecting top 100 investors...")

# Priority 1: Angel investors with high sector match and email
angel_sorted = sorted(angel_investors, key=lambda x: x['score'], reverse=True)
# Priority 2: Needle investors (curated, with emails)
needle_sorted = sorted(needle_investors, key=lambda x: x['score'], reverse=True)
# Priority 3: VC funds with high sector match (many won't have individual emails)
vc_sorted = sorted(vc_investors, key=lambda x: x['score'], reverse=True)

# Build final list
selected = []
seen_emails = set()
seen_firms = set()

def add_investor(inv):
    key = inv['email'].lower() if inv['email'] else inv['firm'].lower()
    firm_key = inv['firm'].lower()
    if key in seen_emails or (not inv['email'] and firm_key in seen_firms):
        return False
    if inv['email']:
        seen_emails.add(key)
    seen_firms.add(firm_key)
    selected.append(inv)
    return True

# First pass: Angel investors with score >= 6 (strong sector match)
for inv in angel_sorted:
    if inv['score'] >= 6 and len(selected) < 100:
        add_investor(inv)

print(f"  After high-score angels: {len(selected)}")

# Second pass: Needle investors
for inv in needle_sorted:
    if len(selected) < 100:
        add_investor(inv)

print(f"  After needle list: {len(selected)}")

# Third pass: VC funds with strong match (even without individual emails, the fund contact info is on their website)
for inv in vc_sorted:
    if inv['score'] >= 9 and len(selected) < 100:
        add_investor(inv)

print(f"  After high-score VCs: {len(selected)}")

# Fourth pass: remaining angels with moderate match
for inv in angel_sorted:
    if inv['score'] >= 3 and len(selected) < 100:
        add_investor(inv)

print(f"  After moderate angels: {len(selected)}")

# Fifth pass: remaining VCs with moderate match
for inv in vc_sorted:
    if inv['score'] >= 6 and len(selected) < 100:
        add_investor(inv)

print(f"  After moderate VCs: {len(selected)}")

# Sixth pass: fill remaining with best available
for inv in vc_sorted:
    if inv['score'] >= 3 and len(selected) < 100:
        add_investor(inv)

print(f"  After remaining VCs: {len(selected)}")

# Last pass if still under 100
for inv in angel_sorted:
    if inv['score'] >= 1 and len(selected) < 100:
        add_investor(inv)

print(f"  Final count: {len(selected)}")

# ===== WRITE CSV =====
print("\nWriting CSV...")
output_path = '/data/.openclaw/workspace/projects/investor-outreach/pitchslam-100-investors.csv'

with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([
        'Number', 'First Name', 'Last Name', 'Firm/Company', 'Investor Type',
        'Email', 'LinkedIn URL', 'Website', 'Twitter/X', 'Sectors of Interest',
        'Stage Invested', 'Why They\'re a Fit', 'Personalized Email Intro'
    ])
    
    for i, inv in enumerate(selected, 1):
        first = inv['first_name']
        last = inv['last_name']
        firm = inv['firm']
        
        # For VC funds without individual names, try to extract from firm name
        display_name = first if first else firm
        
        why_fit = generate_why_fit(display_name, firm, inv['sectors_display'], inv['investor_type'])
        personalized = generate_personalized_intro(
            first if first else 'there',
            firm,
            inv['sectors_display'],
            inv['investor_type'],
            inv.get('past_investments', '')
        )
        
        writer.writerow([
            i,
            first,
            last,
            firm,
            inv['investor_type'],
            inv['email'],
            inv['linkedin'],
            inv.get('website', ''),
            inv.get('twitter', ''),
            inv['sectors_display'],
            inv['stage'],
            why_fit,
            personalized
        ])

print(f"CSV written to {output_path}")

# ===== GENERATE SUMMARY STATS =====
print("\nGenerating summary stats...")
stats = {
    'total': len(selected),
    'by_type': {},
    'by_source': {},
    'by_sector': {},
    'with_email': 0,
    'without_email': 0,
}

for inv in selected:
    # By type
    t = inv['investor_type']
    stats['by_type'][t] = stats['by_type'].get(t, 0) + 1
    
    # By source
    s = inv['source']
    stats['by_source'][s] = stats['by_source'].get(s, 0) + 1
    
    # Email availability
    if inv['email']:
        stats['with_email'] += 1
    else:
        stats['without_email'] += 1
    
    # Sectors
    for sector in inv['sectors_display'].split(', '):
        if sector:
            stats['by_sector'][sector] = stats['by_sector'].get(sector, 0) + 1

# Write stats as JSON for summary generation
with open('stats.json', 'w') as f:
    json.dump(stats, f, indent=2)

print(json.dumps(stats, indent=2))
print("\nDone!")
