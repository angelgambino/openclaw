import csv
from collections import Counter

# ===== LOAD ALL DATA =====

# Angel Syndicate
angel_all = []
with open('/data/.openclaw/workspace/projects/investor-outreach/data/angel-syndicate.csv', 'r') as f:
    rows = list(csv.reader(f))
for row in rows[2:]:
    if len(row) < 6: continue
    first, last, email, company, linkedin, sectors = row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip(), row[4].strip(), row[5].strip()
    investments = row[6].strip() if len(row) > 6 else ''
    if not email or not first: continue
    angel_all.append({
        'first': first, 'last': last, 'email': email, 'company': company,
        'linkedin': linkedin, 'sectors': sectors, 'investments': investments,
        'type': 'Angel/Syndicate', 'website': '', 'location': '', 'source': 'angel_syndicate'
    })

# VC Database
vc_all = []
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
        check = row.get('Average check size','').strip()
        if not fund: continue
        vc_all.append({
            'first': '', 'last': '', 'email': '', 'company': fund,
            'linkedin': linkedin, 'sectors': sectors, 'investments': '',
            'type': fund_type or 'VC', 'website': url, 'location': location,
            'stage': stage, 'state': state, 'check': check, 'source': 'vc_database'
        })

# ===== LOAD NEEDLE LIST (already used) =====
needle_used = set()
with open('/data/.openclaw/workspace/projects/investor-outreach/needle-100-investors.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        key = (row.get('Email','').lower().strip() or row.get('Firm/Company','').lower().strip())
        if key: needle_used.add(key)

print(f"Needle used keys: {len(needle_used)}")

# ===== SCORING FUNCTIONS =====
PITCHSLAM_KW = ['health', 'wellness', 'impact', 'sports', 'entertainment', 'media', 
                'artificial intelligence', 'ai', 'machine learning', 'fitness',
                'human', 'mental health', 'social impact', 'diversity', 'consumer',
                'digital media', 'gaming', 'esports', 'music', 'content']

HTW_KW = ['health', 'wellness', 'impact', 'longevity', 'mental health', 'biotech',
          'life sciences', 'artificial intelligence', 'ai', 'machine learning',
          'human', 'social impact', 'sustainability', 'clean tech', 'ethics',
          'governance', 'fitness', 'biopharma', 'medtech', 'diagnostics']

def score(sectors, keywords):
    s = sectors.lower()
    return sum(1 for k in keywords if k in s)

def is_us(loc, state=''):
    if state: return True
    if not loc: return False
    l = loc.lower()
    us_kw = ['new york', 'california', 'san francisco', 'bay area', 'los angeles', 'boston',
             'chicago', 'miami', 'seattle', 'washington', 'texas', 'colorado', 'philadelphia',
             'united states', 'usa', 'us']
    return any(k in l for k in us_kw)

def is_ca(loc, state=''):
    if 'CA' in (state or ''): return True
    if not loc: return False
    l = loc.lower()
    return any(k in l for k in ['california', 'san francisco', 'bay area', 'los angeles', 'san diego', 'palo alto'])

def is_preseed_seed(stage):
    if not stage: return True
    s = stage.lower()
    return any(k in s for k in ['seed', 'preseed', 'pre-seed', 'angel', 'series a'])

def is_series_a_plus(stage):
    if not stage: return True
    s = stage.lower()
    return any(k in s for k in ['series a', 'series b', 'growth'])

# Determine HTW dinner type
def htw_dinner_type(inv):
    t = inv.get('type', '').lower()
    sectors = inv.get('sectors', '').lower()
    if 'family office' in t: return 'Family Office'
    if 'sovereign' in t or 'government' in t: return 'Sovereign Funds'
    if 'angel' in t or 'syndicate' in t: return 'Angel Investor'
    if any(k in t for k in ['growth', 'institutional', 'vc']): return 'Venture Capital'
    # Fallback based on check size or stage
    stage = inv.get('stage', '').lower()
    if 'growth' in stage or 'series b' in stage: return 'Venture Capital'
    if 'pre' in stage or 'seed' in stage: return 'Angel Investor'
    return 'Venture Capital'  # default

# ===== BUILD PITCH SLAM LIST =====
print("\n=== BUILDING PITCH SLAM 100 ===")

ps_candidates = []

# Angels first (they're the primary target for Pitch Slam)
for inv in angel_all:
    key = inv['email'].lower()
    if key in needle_used: continue
    s = score(inv['sectors'], PITCHSLAM_KW)
    if s < 2: continue
    inv['ps_score'] = s
    ps_candidates.append(inv)

# VCs that do pre-seed/seed
for inv in vc_all:
    key = inv['email'].lower() if inv['email'] else inv['company'].lower()
    if key in needle_used: continue
    s = score(inv['sectors'], PITCHSLAM_KW)
    if s < 2: continue
    if not is_us(inv.get('location',''), inv.get('state','')): continue
    stage_bonus = 2 if is_preseed_seed(inv.get('stage','')) else 0
    inv['ps_score'] = s + stage_bonus
    ps_candidates.append(inv)

ps_candidates.sort(key=lambda x: -x['ps_score'])

# Deduplicate and select top 100
ps_used = set()
pitchslam_100 = []
for inv in ps_candidates:
    key = inv['email'].lower() if inv['email'] else inv['company'].lower()
    if key in ps_used: continue
    ps_used.add(key)
    pitchslam_100.append(inv)
    if len(pitchslam_100) >= 100: break

# Write Pitch Slam CSV
with open('/data/.openclaw/workspace/projects/investor-outreach/pitchslam-100-investors.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['#','First Name','Last Name','Firm/Company','Investor Type','Email','LinkedIn URL','Website','Sectors of Interest','Location','Source','Match Score','Also Good For'])
    for i, inv in enumerate(pitchslam_100, 1):
        also = []
        s = inv['sectors'].lower()
        if any(k in s for k in ['longevity','mental health','human potential','ethics']): also.append('Human Tech Week')
        if any(k in s for k in ['angel','early']): also.append('ACA Summit')
        w.writerow([i, inv['first'], inv['last'], inv['company'], inv['type'], inv['email'],
                     inv['linkedin'], inv.get('website',''), inv['sectors'][:200], inv.get('location',''),
                     inv['source'], inv.get('ps_score',0), '; '.join(also)])

# Add all pitchslam keys to used
all_used = needle_used.copy()
for inv in pitchslam_100:
    key = inv['email'].lower() if inv['email'] else inv['company'].lower()
    all_used.add(key)

print(f"Pitch Slam: {len(pitchslam_100)} investors")
src = Counter(inv['source'] for inv in pitchslam_100)
for s,c in src.most_common(): print(f"  {s}: {c}")
with_email = sum(1 for inv in pitchslam_100 if inv['email'])
print(f"  With email: {with_email}")

# ===== BUILD HUMAN TECH WEEK LIST =====
print("\n=== BUILDING HUMAN TECH WEEK 100 ===")

htw_candidates = []

for inv in angel_all:
    key = inv['email'].lower()
    if key in all_used: continue
    s = score(inv['sectors'], HTW_KW)
    if s < 2: continue
    inv['htw_score'] = s
    htw_candidates.append(inv)

for inv in vc_all:
    key = inv['email'].lower() if inv['email'] else inv['company'].lower()
    if key in all_used: continue
    s = score(inv['sectors'], HTW_KW)
    if s < 2: continue
    if not is_ca(inv.get('location',''), inv.get('state','')): continue  # CA only for HTW
    stage_bonus = 2 if is_series_a_plus(inv.get('stage','')) else 0
    inv['htw_score'] = s + stage_bonus
    htw_candidates.append(inv)

htw_candidates.sort(key=lambda x: -x.get('htw_score', 0))

htw_used = set()
htw_100 = []
for inv in htw_candidates:
    key = inv['email'].lower() if inv['email'] else inv['company'].lower()
    if key in htw_used: continue
    htw_used.add(key)
    inv['dinner'] = htw_dinner_type(inv)
    htw_100.append(inv)
    if len(htw_100) >= 100: break

# Balance dinners - count per type
dinner_counts = Counter(inv['dinner'] for inv in htw_100)
print(f"HTW dinner distribution: {dict(dinner_counts)}")

# Write HTW CSV
with open('/data/.openclaw/workspace/projects/investor-outreach/htw-100-investors.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['#','First Name','Last Name','Firm/Company','Investor Type','Email','LinkedIn URL','Website','Sectors of Interest','Location','Source','Match Score','Assigned Dinner','Also Good For'])
    for i, inv in enumerate(htw_100, 1):
        also = []
        s = inv['sectors'].lower()
        if any(k in s for k in ['seed','angel','early']): also.append('ACA Summit')
        w.writerow([i, inv['first'], inv['last'], inv['company'], inv['type'], inv['email'],
                     inv['linkedin'], inv.get('website',''), inv['sectors'][:200], inv.get('location',''),
                     inv['source'], inv.get('htw_score',0), inv['dinner'], '; '.join(also)])

# Update all_used
for inv in htw_100:
    key = inv['email'].lower() if inv['email'] else inv['company'].lower()
    all_used.add(key)

print(f"HTW: {len(htw_100)} investors")
src = Counter(inv['source'] for inv in htw_100)
for s,c in src.most_common(): print(f"  {s}: {c}")
with_email = sum(1 for inv in htw_100 if inv['email'])
print(f"  With email: {with_email}")

# ===== BUILD ACA SUMMIT LIST =====
print("\n=== BUILDING ACA SUMMIT 100 ===")

ACA_KW = ['health', 'wellness', 'impact', 'sports', 'entertainment', 'media',
           'artificial intelligence', 'ai', 'machine learning', 'fitness',
           'human', 'angel', 'seed', 'early', 'consumer', 'social impact']

aca_candidates = []

for inv in angel_all:
    key = inv['email'].lower()
    if key in all_used: continue
    s = score(inv['sectors'], ACA_KW)
    if s < 1: continue  # Lower threshold since we need to fill
    inv['aca_score'] = s
    aca_candidates.append(inv)

for inv in vc_all:
    key = inv['email'].lower() if inv['email'] else inv['company'].lower()
    if key in all_used: continue
    s = score(inv['sectors'], ACA_KW)
    if s < 1: continue
    if not is_us(inv.get('location',''), inv.get('state','')): continue
    inv['aca_score'] = s
    aca_candidates.append(inv)

aca_candidates.sort(key=lambda x: -x.get('aca_score', 0))

aca_used = set()
aca_100 = []
for inv in aca_candidates:
    key = inv['email'].lower() if inv['email'] else inv['company'].lower()
    if key in aca_used: continue
    aca_used.add(key)
    aca_100.append(inv)
    if len(aca_100) >= 100: break

with open('/data/.openclaw/workspace/projects/investor-outreach/aca-100-investors.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['#','First Name','Last Name','Firm/Company','Investor Type','Email','LinkedIn URL','Website','Sectors of Interest','Location','Source','Match Score','Also Good For'])
    for i, inv in enumerate(aca_100, 1):
        w.writerow([i, inv['first'], inv['last'], inv['company'], inv['type'], inv['email'],
                     inv['linkedin'], inv.get('website',''), inv['sectors'][:200], inv.get('location',''),
                     inv['source'], inv.get('aca_score',0), ''])

print(f"ACA: {len(aca_100)} investors")
src = Counter(inv['source'] for inv in aca_100)
for s,c in src.most_common(): print(f"  {s}: {c}")
with_email = sum(1 for inv in aca_100 if inv['email'])
print(f"  With email: {with_email}")

# ===== SUMMARY =====
print(f"\n=== TOTAL UNIQUE INVESTORS: {len(needle_used) + len(pitchslam_100) + len(htw_100) + len(aca_100)} ===")
print(f"  Needle: 100")
print(f"  Pitch Slam: {len(pitchslam_100)}")
print(f"  HTW: {len(htw_100)}")
print(f"  ACA: {len(aca_100)}")
