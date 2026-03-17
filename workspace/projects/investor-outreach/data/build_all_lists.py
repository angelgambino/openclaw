import csv

NEEDLE_KW = ['artificial intelligence','marketing','e-commerce','ecommerce','commerce','saas',
             'software','advertising','media','enterprise','b2b','marketplace','retail',
             'digital marketing','consumer','ai','smb','dtc','direct to consumer','martech',
             'future of work']

CA_KW = ['california','san francisco','bay area','los angeles','san diego','palo alto','ca']

def needle_score(sectors):
    s = sectors.lower()
    return sum(1 for k in NEEDLE_KW if k in s)

def is_ca(loc):
    if not loc: return False
    return any(k in loc.lower() for k in CA_KW)

# ============= ANGEL SYNDICATE =============
angel_investors = []
with open('/data/.openclaw/workspace/projects/investor-outreach/data/angel-syndicate.csv', 'r') as f:
    rows = list(csv.reader(f))
headers_a = rows[1]
for row in rows[2:]:
    if len(row) < 6: continue
    first, last, email, company, linkedin, sectors = row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip(), row[4].strip(), row[5].strip()
    investments = row[6].strip() if len(row) > 6 else ''
    if not email or not first: continue
    score = needle_score(sectors)
    if score < 2: continue
    angel_investors.append({
        'first': first, 'last': last, 'email': email, 'company': company,
        'linkedin': linkedin, 'sectors': sectors, 'investments': investments,
        'type': 'Angel/Syndicate', 'score': score, 'website': '', 'location': '',
        'source': 'angel_syndicate'
    })
angel_investors.sort(key=lambda x: -x['score'])

# ============= VC DATABASE =============
vc_investors = []
with open('/data/.openclaw/workspace/projects/investor-outreach/data/vc-database.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        fund = row.get('Fund','').strip()
        location = row.get('Primary Location','').strip()
        sectors = row.get('Investment Sectors','').strip()
        fund_type = row.get('Fund Type','').strip()
        stage = row.get('Stage Invested','').strip()
        url = row.get('URL','').strip()
        linkedin = row.get('Linkedin','').strip()
        state = row.get('State (if U.S.)','').strip()
        if not fund: continue
        score = needle_score(sectors)
        ca_bonus = 2 if (is_ca(location) or 'CA' in (state or '')) else 0
        if score < 2: continue
        vc_investors.append({
            'first': '', 'last': '', 'email': '', 'company': fund,
            'linkedin': linkedin, 'sectors': sectors, 'investments': '',
            'type': fund_type or 'VC', 'score': score + ca_bonus,
            'website': url, 'location': location, 'stage': stage, 'source': 'vc_database'
        })
vc_investors.sort(key=lambda x: -x['score'])

# ============= NEEDLE LIST =============
needle_investors = []
with open('/data/.openclaw/workspace/projects/investor-outreach/data/needle-list.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        investor = row.get('Investor','').strip()
        inv_type = row.get('Investor Type','').strip()
        email = row.get('Investor Email','').strip()
        website = row.get('Investor Website','').strip()
        desc = row.get('Investor Description','').strip()
        city = row.get('City','').strip()
        if not investor: continue
        needle_investors.append({
            'first': '', 'last': '', 'email': email, 'company': investor,
            'linkedin': '', 'sectors': desc, 'investments': '',
            'type': inv_type, 'score': 15, 'website': website,
            'location': city, 'source': 'needle_list'
        })

# ============= COMBINE FOR NEEDLE LIST =============
all_needle = needle_investors + angel_investors + vc_investors

seen = set()
needle_100 = []
skip = {'noushin', 'gady'}

for inv in all_needle:
    key = (inv['email'].lower() if inv['email'] else inv['company'].lower())
    name_check = f"{inv['first']} {inv['last']}".strip().lower()
    if key in seen or any(s in name_check for s in skip): continue
    seen.add(key)
    needle_100.append(inv)
    if len(needle_100) >= 100: break

# Track used keys for dedup across events
used_keys = set()
for inv in needle_100:
    key = inv['email'].lower() if inv['email'] else inv['company'].lower()
    used_keys.add(key)

# Write Needle CSV
with open('/data/.openclaw/workspace/projects/investor-outreach/needle-100-investors.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['#','First Name','Last Name','Firm/Company','Investor Type','Email','LinkedIn URL','Website','Sectors of Interest','Location','Source','Match Score','Also Good For'])
    for i, inv in enumerate(needle_100, 1):
        also = []
        s = inv['sectors'].lower()
        if any(k in s for k in ['health','wellness','impact','sports','entertainment','human']): also.append('Human Tech Week')
        if any(k in s for k in ['seed','pre-seed','angel','early']): also.append('Pitch Slam')
        w.writerow([i, inv['first'], inv['last'], inv['company'], inv['type'], inv['email'],
                     inv['linkedin'], inv['website'], inv['sectors'][:200], inv.get('location',''),
                     inv['source'], inv['score'], '; '.join(also)])

# Stats
from collections import Counter
print(f"=== NEEDLE 100 ===")
print(f"Total: {len(needle_100)}")
src = Counter(inv['source'] for inv in needle_100)
for s,c in src.most_common(): print(f"  Source {s}: {c}")
typ = Counter(inv['type'] for inv in needle_100)
print("By type:")
for t,c in typ.most_common()[:10]: print(f"  {t}: {c}")
with_email = sum(1 for inv in needle_100 if inv['email'])
print(f"With email: {with_email}")
print(f"Without email (need to find): {100 - with_email}")
