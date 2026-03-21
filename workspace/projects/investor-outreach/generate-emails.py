#!/usr/bin/env python3
"""Generate 200 personalized cold email templates from the investor database."""

import csv
import sys
import re

CSV_PATH = "/data/.openclaw/workspace/projects/investor-outreach/MASTER-investor-database-v2.csv"
OUT_PATH = "/data/.openclaw/workspace/projects/investor-outreach/TEMPLATE-EMAILS-TOP200.md"

# Read CSV
with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames
    rows = list(reader)

print(f"Total rows: {len(rows)}")
print(f"Headers: {len(headers)}")

# Skip Angel Gambino herself (row 1)
rows = [r for r in rows if r.get('Name', '').strip() != 'Angel Gambino']

# Count non-empty fields per row
def completeness(row):
    return sum(1 for v in row.values() if v and v.strip())

# Sort by completeness descending
rows.sort(key=completeness, reverse=True)

# Take top 200
top200 = rows[:200]

print(f"Top 200 completeness range: {completeness(top200[0])} - {completeness(top200[-1])}")

# Helper to get field value or empty string
def g(row, field):
    return (row.get(field) or '').strip()

def truncate_sectors(sectors_str, max_items=5):
    """Pick a few representative sectors from a long list."""
    if not sectors_str:
        return ""
    # Split on commas, clean up quotes
    items = [s.strip().strip('"').strip("'") for s in sectors_str.split(',')]
    items = [s for s in items if s]
    if len(items) <= max_items:
        return ', '.join(items)
    # Pick first few meaningful ones
    return ', '.join(items[:max_items])

def pick_key_sectors(sectors_str, max_items=3):
    """Pick the most distinctive/specific sectors."""
    if not sectors_str:
        return []
    items = [s.strip().strip('"').strip("'") for s in sectors_str.split(',')]
    items = [s for s in items if s]
    # Prioritize specific sectors over generic ones
    generic = {'Technology', 'Software', 'SaaS', 'Enterprise', 'Consumer', 'B2B', 'B2C', 'Mobile'}
    specific = [s for s in items if s not in generic]
    if specific:
        return specific[:max_items]
    return items[:max_items]

def make_subject(name, fund, sectors, portfolio):
    """Generate a tailored subject line."""
    key_sectors = pick_key_sectors(sectors, 2)
    
    if key_sectors:
        sector_str = ' & '.join(key_sectors[:2])
        variants = [
            f"Quick note on {sector_str} trends",
            f"Non-obvious shifts in {sector_str}",
            f"{sector_str} — seeing something interesting",
            f"Connecting on {sector_str} opportunities",
            f"A perspective on where {sector_str} is heading",
            f"Thoughts on emerging {sector_str} dynamics",
        ]
    elif fund:
        variants = [
            f"Quick note for {fund}",
            f"Connecting with {fund}",
            f"A perspective that may interest {fund}",
        ]
    else:
        variants = [
            f"Quick note — investor-to-investor",
            f"Connecting on emerging opportunities",
            f"A non-obvious perspective",
        ]
    
    # Use hash of name for deterministic but varied selection
    idx = hash(name) % len(variants)
    return variants[idx]

def make_body(row):
    """Generate a personalized email body."""
    name = g(row, 'Name')
    email = g(row, 'Email') or '[email needed]'
    fund = g(row, 'Fund') or ''
    sectors = g(row, 'Sector: Investment Thesis')
    stage = g(row, 'Stage: Investment Thesis')
    portfolio = g(row, 'Notable Portfolio Companies')
    how_to_pitch = g(row, 'How to Pitch This Investor')
    red_flags = g(row, 'Red Flags / Won\'t Invest')
    content = g(row, 'Investor Content')
    open_access = g(row, 'Open Access / Office Hours')
    investor_type = g(row, 'Type of Investor')
    check_size = g(row, 'Typical Check Size')
    fund_size = g(row, 'Fund Size')
    location_city = g(row, 'Location (City)')
    location_country = g(row, 'Location (Country)')
    co_investors = g(row, 'Known Co-Investors')
    reputation = g(row, 'Reputation Notes')
    takes_board = g(row, 'Takes Board Seats?')
    diversity = g(row, 'Founder Diversity Track Record')
    decision_auth = g(row, 'Decision Authority')
    
    first_name = name.split()[0] if name else "there"
    
    key_sectors = pick_key_sectors(sectors, 3)
    sector_display = ', '.join(key_sectors) if key_sectors else 'innovation'
    
    # Clean fund name (remove LinkedIn URLs etc.)
    if fund and ('linkedin.com' in fund or 'http' in fund):
        fund = ''
    
    # Clean email (remove trailing commas)
    email = email.rstrip(',').strip()
    
    # LINE 1: Opening — reference their specific thesis/sector
    if fund and key_sectors:
        line1 = f"I'm reaching out given {fund}'s focus on {sector_display}."
    elif fund:
        line1 = f"I'm reaching out given {fund}'s investment approach."
    elif key_sectors:
        line1 = f"I'm reaching out given your focus on {sector_display}."
    else:
        line1 = f"I'm reaching out as a fellow investor with complementary deal flow."
    
    # If they have content (blog/podcast), reference it
    if content and 'Blog' in content:
        blog_ref = content.split('|')[0].strip()
        line1 += f" I've been following your writing ({blog_ref.replace('Blog: ', '')}) and find your perspective sharp."
    elif content and 'Podcast' in content:
        pod_ref = content.split('|')[0].strip()
        line1 += f" I've enjoyed your podcast ({pod_ref.replace('Podcast: ', '')}) — great insights."
    elif content and 'Newsletter' in content:
        news_ref = content.split('|')[0].strip()
        line1 += f" Your newsletter ({news_ref.replace('Newsletter: ', '')}) has been a valuable read."
    
    # If they have notable portfolio, reference it
    portfolio_ref = ""
    if portfolio:
        companies = [c.strip() for c in portfolio.split(',')][:2]
        if companies and companies[0]:
            portfolio_ref = f" Your early conviction in {' and '.join(companies)} speaks to strong pattern recognition."
    
    # LINE 2: Tease value — reference their area
    if key_sectors:
        primary = key_sectors[0]
        line2_variants = [
            f"I'm seeing non-obvious shifts in {primary} that don't seem to be on most investors' radar yet — and may be highly relevant to your thesis.",
            f"There are emerging dynamics in {primary} that I think create asymmetric opportunity — the kind of thing that's easy to miss from deal flow alone.",
            f"I've been tracking inflection points in {primary} that could reshape the landscape over the next 18 months.",
            f"From what I'm seeing across my network of 6,000+ founders, {primary} is about to enter a very different phase — and I think it maps to your thesis.",
        ]
    else:
        line2_variants = [
            "I'm seeing non-obvious shifts across several sectors that may be relevant to your portfolio strategy.",
            "There are emerging dynamics I've been tracking across my founder network that I think you'd find valuable.",
            "From my vantage point across 6,000+ founders, I'm seeing patterns that aren't showing up in typical deal flow yet.",
        ]
    line2 = line2_variants[hash(name + 'l2') % len(line2_variants)]
    
    # LINE 3: Credibility
    line3_variants = [
        "I've been investing for 20+ years and run Angel Club — a community of 6,000+ founders and 400+ investors focused on impact and innovation.",
        "For context, I'm an investor with 20+ years of experience and the founder of Angel Club (6,000+ founders, 400+ investors), focused on connecting capital with meaningful innovation.",
        "A bit about me: I've spent 20+ years investing and built Angel Club, a 6,000+ founder / 400+ investor community at the intersection of impact and opportunity.",
    ]
    line3 = line3_variants[hash(name + 'l3') % len(line3_variants)]
    
    # LINE 4: The ask — soft CTA, incorporate open access info
    if open_access and 'Office Hours' in open_access:
        line4 = f"I noticed you offer office hours — would that be a good venue to connect, or would a brief call work better?"
    elif open_access and 'DMs Open' in open_access:
        line4 = "Would you be open to a brief exchange? Happy to connect however works best for you — DM, email, or a quick call."
    elif open_access and 'Events' in open_access:
        line4 = "Would you be open to connecting? I'd also love to cross paths at one of your upcoming events."
    elif how_to_pitch and 'cold email' in how_to_pitch.lower():
        line4 = "Would you be open to a 15-minute call to exchange perspectives? I think there could be real synergy."
    else:
        line4_variants = [
            "Would you be open to connecting for a brief call? I think there's meaningful overlap worth exploring.",
            "Would you be open to a quick exchange? I'd love to share what I'm seeing and hear your perspective.",
            "I'd welcome the chance to connect — even 15 minutes could surface something valuable for both of us.",
            "Would you be open to a brief conversation? I think we'd find real alignment.",
        ]
        line4 = line4_variants[hash(name + 'l4') % len(line4_variants)]
    
    # Add portfolio reference if available
    body_parts = [f"Hi {first_name},", "", line1]
    if portfolio_ref:
        body_parts.append(portfolio_ref.strip())
    body_parts.extend(["", line2, "", line3, "", line4, "", "Best,", "Angel Gambino"])
    
    return '\n'.join(body_parts)


# Generate output
output_lines = [
    "# Template Pitch Emails — Top 200 Investors",
    "",
    f"_Generated from MASTER-investor-database-v2.csv — sorted by data completeness._",
    f"_Style: Angel Gambino's cold outreach approach. Templates only — NOT sent._",
    "",
    "---",
    "",
]

for i, row in enumerate(top200):
    name = g(row, 'Name')
    email = g(row, 'Email') or '[email needed]'
    email = email.rstrip(',').strip()
    fund = g(row, 'Fund') or 'Independent'
    
    # Clean fund display
    fund_display = fund
    if 'linkedin.com' in fund or 'http' in fund:
        # Try to extract fund name from reputation notes
        rep = g(row, 'Reputation Notes')
        if rep:
            # Often starts with "FundName." — extract just the name
            fund_name = rep.split('.')[0].strip()
            # Filter out descriptions that aren't fund names
            if fund_name and len(fund_name) < 40 and not any(w in fund_name.lower() for w in ['angel', 'legendary', 'established', 'prominent', 'known', 'early', 'active']):
                fund_display = fund_name
            else:
                fund_display = 'Independent'
        else:
            fund_display = 'Independent'
    
    sectors = g(row, 'Sector: Investment Thesis')
    portfolio = g(row, 'Notable Portfolio Companies')
    
    subject = make_subject(name, fund_display, sectors, portfolio)
    body = make_body(row)
    
    output_lines.append(f"## {i+1}. {name} — {fund_display}")
    output_lines.append(f"**To:** {email}")
    output_lines.append(f"**Subject:** {subject}")
    output_lines.append("")
    output_lines.append(body)
    output_lines.append("")
    output_lines.append("---")
    output_lines.append("")

# Write output
with open(OUT_PATH, 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print(f"\nGenerated {len(top200)} email templates → {OUT_PATH}")
print(f"Emails with addresses: {sum(1 for r in top200 if g(r, 'Email'))}")
print(f"Emails needing addresses: {sum(1 for r in top200 if not g(r, 'Email'))}")
