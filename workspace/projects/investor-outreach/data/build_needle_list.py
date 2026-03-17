import csv
import re
import sys

NEEDLE_SECTORS = ['artificial intelligence', 'ai', 'machine learning', 'marketing', 'martech', 
                  'e-commerce', 'ecommerce', 'commerce', 'dtc', 'direct to consumer', 'consumer',
                  'saas', 'software', 'smb', 'future of work', 'digital marketing', 'retail',
                  'advertising', 'media', 'enterprise software', 'b2b', 'marketplace']

CA_KEYWORDS = ['california', 'san francisco', 'bay area', 'los angeles', 'la', 'san diego', 'ca']
SEED_KEYWORDS = ['seed', 'preseed', 'pre-seed', 'angel', 'series a']

def sector_match_score(sectors_str):
    if not sectors_str:
        return 0
    s = sectors_str.lower()
    score = 0
    for keyword in NEEDLE_SECTORS:
        if keyword in s:
            score += 1
    return score

def is_ca_based(location_str):
    if not location_str:
        return False
    l = location_str.lower()
    return any(k in l for k in CA_KEYWORDS)

def is_stage_match(stage_str):
    if not stage_str:
        return True  # unknown = don't penalize
    s = stage_str.lower()
    return any(k in s for k in SEED_KEYWORDS)

# Process angel syndicate database
angel_investors = []
with open('/data/.openclaw/workspace/projects/investor-outreach/data/angel-syndicate.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        first = row.get('First Name', '').strip()
        last = row.get('Last Name', '').strip()
        email = row.get('Email', '').strip()
        company = row.get('Company', '').strip()
        linkedin = row.get('LinkedIn URL', '').strip()
        sectors = row.get('Industries/ Verticals of Interest', '').strip()
        investments = row.get('Past Investments', '').strip()
        
        if not email or not first:
            continue
        
        score = sector_match_score(sectors)
        if score < 2:  # need at least 2 sector matches
            continue
            
        angel_investors.append({
            'first': first, 'last': last, 'email': email, 'company': company,
            'linkedin': linkedin, 'sectors': sectors, 'investments': investments,
            'type': 'Angel/Syndicate', 'score': score, 'website': '', 'location': '',
            'source': 'angel_syndicate'
        })

# Process VC database
vc_investors = []
with open('/data/.openclaw/workspace/projects/investor-outreach/data/vc-database.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        fund = row.get('Fund', '').strip()
        location = row.get('Primary Location', '').strip()
        sectors = row.get('Investment Sectors', '').strip()
        fund_type = row.get('Fund Type', '').strip()
        stage = row.get('Stage Invested', '').strip()
        url = row.get('URL', '').strip()
        linkedin = row.get('Linkedin', '').strip()
        state = row.get('State (if U.S.)', '').strip()
        
        if not fund:
            continue
            
        score = sector_match_score(sectors)
        ca_bonus = 2 if (is_ca_based(location) or 'CA' in state) else 0
        stage_bonus = 1 if is_stage_match(stage) else 0
        total_score = score + ca_bonus + stage_bonus
        
        if score < 2:  # need at least 2 sector matches
            continue
            
        vc_investors.append({
            'first': '', 'last': '', 'email': '', 'company': fund,
            'linkedin': linkedin, 'sectors': sectors, 'investments': '',
            'type': fund_type if fund_type else 'VC', 'score': total_score,
            'website': url, 'location': location, 'stage': stage,
            'source': 'vc_database'
        })

# Process Needle list
needle_investors = []
with open('/data/.openclaw/workspace/projects/investor-outreach/data/needle-list.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        investor = row.get('Investor', '').strip()
        inv_type = row.get('Investor Type', '').strip()
        email = row.get('Investor Email', '').strip()
        website = row.get('Investor Website', '').strip()
        desc = row.get('Investor Description', '').strip()
        
        if not investor:
            continue
            
        needle_investors.append({
            'first': '', 'last': '', 'email': email, 'company': investor,
            'linkedin': '', 'sectors': desc, 'investments': '',
            'type': inv_type, 'score': 10,  # high priority
            'website': website, 'location': row.get('City', ''),
            'source': 'needle_list'
        })

# Combine and sort by score
all_investors = needle_investors + sorted(angel_investors, key=lambda x: -x['score']) + sorted(vc_investors, key=lambda x: -x['score'])

# Deduplicate by email/company
seen = set()
unique = []
skip_names = {'noushin', 'gady'}  # confirmed investors to exclude

for inv in all_investors:
    key = inv['email'].lower() if inv['email'] else inv['company'].lower()
    name_check = (inv['first'].lower() + ' ' + inv['last'].lower()).strip()
    
    if key in seen or any(s in name_check for s in skip_names):
        continue
    seen.add(key)
    unique.append(inv)

# Take top 100
top100 = unique[:100]

# Write CSV
output_path = '/data/.openclaw/workspace/projects/investor-outreach/needle-100-investors.csv'
with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['#', 'First Name', 'Last Name', 'Firm/Company', 'Investor Type', 'Email',
                     'LinkedIn URL', 'Website', 'Sectors of Interest', 'Location', 'Source DB',
                     'Match Score', 'Also Good For'])
    
    for i, inv in enumerate(top100, 1):
        # Determine cross-event fit
        also_good = []
        s = inv['sectors'].lower()
        if any(k in s for k in ['health', 'wellness', 'impact', 'sports', 'entertainment']):
            also_good.append('Human Tech Week')
        if any(k in s for k in ['angel', 'pre-seed', 'seed']):
            also_good.append('Pitch Slam')
        if any(k in s for k in ['angel', 'seed', 'early']):
            also_good.append('ACA Summit')
        
        writer.writerow([
            i, inv['first'], inv['last'], inv['company'], inv['type'], inv['email'],
            inv['linkedin'], inv['website'], inv['sectors'], inv.get('location', ''),
            inv['source'], inv['score'], '; '.join(also_good) if also_good else ''
        ])

print(f"Written {len(top100)} investors to {output_path}")
print(f"\nBreakdown by source:")
from collections import Counter
sources = Counter(inv['source'] for inv in top100)
for s, c in sources.most_common():
    print(f"  {s}: {c}")
types = Counter(inv['type'] for inv in top100)
print(f"\nBreakdown by type:")
for t, c in types.most_common():
    print(f"  {t}: {c}")
