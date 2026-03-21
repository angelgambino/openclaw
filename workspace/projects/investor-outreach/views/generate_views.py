#!/usr/bin/env python3
import csv
import re
import os

INPUT = '/data/.openclaw/workspace/projects/investor-outreach/MASTER-investor-database-v2.csv'
OUT_DIR = '/data/.openclaw/workspace/projects/investor-outreach/views'

# Read all rows
with open(INPUT, 'r', encoding='utf-8', errors='replace') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

print(f"Total rows: {len(rows)}")
print(f"Columns: {fieldnames}")

def sector_matches(row, keywords):
    sector = (row.get('Sector: Investment Thesis') or '').lower()
    for kw in keywords:
        if kw.lower() in sector:
            return True
    return False

def stage_matches(row, stages):
    stage = (row.get('Stage: Investment Thesis') or '').lower()
    for s in stages:
        if s.lower() in stage:
            return True
    return False

def sort_key_priority_confidence(row):
    tier_order = {'high': 0, 'medium': 1, 'low': 2, '': 3}
    conf_order = {'high': 0, 'medium': 1, 'low': 2, '': 3}
    tier = (row.get('Priority Tier') or '').strip().lower()
    conf = (row.get('Data Confidence Level') or '').strip().lower()
    return (tier_order.get(tier, 3), conf_order.get(conf, 3))

def write_csv(rows, filepath, extra_fieldnames=None):
    fnames = list(fieldnames) + (extra_fieldnames or [])
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fnames, extrasaction='ignore')
        writer.writeheader()
        for r in rows:
            writer.writerow(r)
    print(f"  Written {len(rows)} rows to {os.path.basename(filepath)}")

# --- VIEW 1: Needle ---
needle_kw = ['AI', 'marketing', 'martech', 'adtech', 'e-commerce', 'commerce', 'SaaS', 'software', 'consumer', 'DTC', 'enterprise', 'B2B', 'retail']
needle_stages = ['seed', 'series a', 'pre-seed']
needle = [r for r in rows if sector_matches(r, needle_kw) and stage_matches(r, needle_stages)]
needle.sort(key=sort_key_priority_confidence)
write_csv(needle, os.path.join(OUT_DIR, 'needle-filtered.csv'))

# --- VIEW 2: CountryLine ---
cl_kw = ['music', 'media', 'entertainment', 'creator', 'social', 'community', 'content', 'digital media', 'gaming', 'esports', 'consumer']
cl_stages = ['seed', 'series a', 'pre-seed']
countryline = [r for r in rows if sector_matches(r, cl_kw) and stage_matches(r, cl_stages)]
countryline.sort(key=sort_key_priority_confidence)
write_csv(countryline, os.path.join(OUT_DIR, 'countryline-filtered.csv'))

# --- VIEW 3: Psymed ---
psymed_kw = ['mental health', 'health', 'wellness', 'biotech', 'life science', 'pharma', 'therapeutic', 'medical', 'brain', 'neuro', 'psychedelic', 'consciousness', 'fitness', 'longevity']
psymed = [r for r in rows if sector_matches(r, psymed_kw)]
psymed.sort(key=sort_key_priority_confidence)
write_csv(psymed, os.path.join(OUT_DIR, 'psymed-filtered.csv'))

# --- VIEW 4: HTW Dinners ---
htw_kw = ['impact', 'health', 'wellness', 'AI', 'sustainability', 'clean tech', 'social impact', 'human', 'longevity', 'mental health', 'consciousness', 'ethics']
htw = [r for r in rows if sector_matches(r, htw_kw)]
# Sort: California first, then priority/confidence
def htw_sort(row):
    state = (row.get('Location (State)') or '').strip().lower()
    ca = 0 if state == 'california' else 1
    return (ca,) + sort_key_priority_confidence(row)
htw.sort(key=htw_sort)
write_csv(htw, os.path.join(OUT_DIR, 'htw-filtered.csv'))

# --- VIEW 5: CIIS Donors ---
ciis_kw = ['mental health', 'education', 'health', 'wellness', 'psychedelic', 'consciousness', 'brain', 'behavioral', 'training', 'workforce']
ciis = [r for r in rows if sector_matches(r, ciis_kw)]
ciis.sort(key=sort_key_priority_confidence)
write_csv(ciis, os.path.join(OUT_DIR, 'ciis-filtered.csv'))

# --- VIEW 6: Multi-Deal Investors ---
# Check each row against views 1-5 criteria
def matches_needle(r):
    return sector_matches(r, needle_kw) and stage_matches(r, needle_stages)
def matches_countryline(r):
    return sector_matches(r, cl_kw) and stage_matches(r, cl_stages)
def matches_psymed(r):
    return sector_matches(r, psymed_kw)
def matches_htw(r):
    return sector_matches(r, htw_kw)
def matches_ciis(r):
    return sector_matches(r, ciis_kw)

deal_checks = [
    ('Needle', matches_needle),
    ('CountryLine', matches_countryline),
    ('Psymed', matches_psymed),
    ('HTW Dinners', matches_htw),
    ('CIIS Donors', matches_ciis),
]

multi = []
for r in rows:
    matching = [name for name, fn in deal_checks if fn(r)]
    if len(matching) >= 3:
        r_copy = dict(r)
        r_copy['Matching Deals'] = '; '.join(matching)
        multi.append(r_copy)

multi.sort(key=lambda r: (-len(r['Matching Deals'].split('; ')),) + sort_key_priority_confidence(r))
write_csv(multi, os.path.join(OUT_DIR, 'multi-deal-investors.csv'), extra_fieldnames=['Matching Deals'])

# --- SUMMARY ---
def top10_names(rows):
    names = []
    for r in rows[:10]:
        name = (r.get('Name') or '').strip()
        fund = (r.get('Fund') or '').strip()
        tier = (r.get('Priority Tier') or '').strip()
        if name:
            entry = f"**{name}**"
            if fund:
                entry += f" ({fund})"
            if tier:
                entry += f" — {tier}"
            names.append(entry)
    return names

views_info = [
    ('Needle (AI/Martech/DTC/SaaS)', needle, 'needle-filtered.csv'),
    ('CountryLine (Music/Media/Entertainment/Creator)', countryline, 'countryline-filtered.csv'),
    ('Psymed (Mental Health/Brain/Wellness)', psymed, 'psymed-filtered.csv'),
    ('HTW Dinners (Impact/Health/AI/Human Potential)', htw, 'htw-filtered.csv'),
    ('CIIS Donors (Mental Health/Education/Psychedelics)', ciis, 'ciis-filtered.csv'),
    ('High-Value Multi-Sector (3+ deals)', multi, 'multi-deal-investors.csv'),
]

summary_lines = ['# Investor Database — Filtered Views Summary\n']
summary_lines.append(f'Generated from master DB with **{len(rows)}** total investors.\n')
summary_lines.append('## Overview\n')
summary_lines.append('| View | Count | File |')
summary_lines.append('|------|-------|------|')
for name, data, fname in views_info:
    summary_lines.append(f'| {name} | {len(data)} | `{fname}` |')
summary_lines.append('')

for name, data, fname in views_info:
    summary_lines.append(f'## {name}\n')
    summary_lines.append(f'**{len(data)} investors** → `{fname}`\n')
    top = top10_names(data)
    if top:
        summary_lines.append('### Top 10\n')
        for i, t in enumerate(top, 1):
            summary_lines.append(f'{i}. {t}')
    summary_lines.append('')

with open(os.path.join(OUT_DIR, 'VIEW-SUMMARY.md'), 'w') as f:
    f.write('\n'.join(summary_lines))
print("Summary written to VIEW-SUMMARY.md")
