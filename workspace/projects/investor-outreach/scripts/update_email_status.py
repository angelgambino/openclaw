#!/usr/bin/env python3
"""Update MASTER CSV with deep email verification using MX results."""

import csv
import re
import os
from collections import defaultdict

CSV_PATH = "/data/.openclaw/workspace/projects/investor-outreach/MASTER-investor-database-v2.csv"
MX_RESULTS = "/tmp/domain_mx_results.csv"
FLAGS_PATH = "/data/.openclaw/workspace/projects/investor-outreach/data/email-verification-flags.csv"

PERSONAL_DOMAINS = {
    'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com',
    'icloud.com', 'mail.com', 'protonmail.com', 'zoho.com', 'yandex.com',
    'live.com', 'msn.com', 'me.com', 'mac.com', 'hotmail.co.uk',
    'sbcglobal.net', 'optonline.net',
}

INVALID_INVESTOR_DOMAINS = {'crunchbase.com', 'linkedin.com', 'pitchbook.com'}

TYPO_DOMAINS = {
    'gmial.com': 'gmail.com', 'gmal.com': 'gmail.com', 'gmil.com': 'gmail.com',
    'yahooo.com': 'yahoo.com', 'yaho.com': 'yahoo.com',
    'hotmal.com': 'hotmail.com', 'outlok.com': 'outlook.com',
}

NON_FUND_DOMAINS = {'crunchbase.com', 'linkedin.com', 'angel.co', 'about.me', 'pitchbook.com'}

def load_mx():
    results = {}
    with open(MX_RESULTS) as f:
        for row in csv.DictReader(f):
            d = row['domain'].strip().lower()
            results[d] = {'has_mx': row['has_mx'] == 'yes', 'resolves': row['resolves']}
    return results

def extract_email(raw):
    if not raw or not raw.strip():
        return None, False
    raw = raw.strip().strip('"')
    if ',' in raw:
        parts = [p.strip() for p in raw.split(',') if '@' in p]
        return (parts[0] if parts else None), True
    return (raw if '@' in raw else None), False

def get_domain(email):
    if not email or '@' not in email:
        return None
    return email.split('@')[1].strip().lower()

def extract_fund_domain(url):
    if not url:
        return None
    url = re.sub(r'^https?://', '', url.strip().strip('"'))
    url = re.sub(r'^www\.', '', url)
    d = url.split('/')[0].split('?')[0].strip().lower()
    return d if d else None

def valid_format(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email or ''))

def main():
    mx = load_mx()
    print(f"Loaded MX results for {len(mx)} domains")

    with open(CSV_PATH, 'r', encoding='utf-8', errors='replace') as f:
        lines = list(csv.reader(f.read().splitlines()))

    header = lines[0]
    es_idx = [i for i, c in enumerate(header) if c.strip() == 'Email Status']
    en_idx = [i for i, c in enumerate(header) if c.strip() == 'Email Notes']
    print(f"Status cols: {es_idx}, Notes cols: {en_idx}")

    # Duplicate detection
    email_rows = defaultdict(list)
    for rn, row in enumerate(lines[1:], 2):
        if len(row) > 1:
            e, _ = extract_email(row[1])
            if e:
                email_rows[e.lower()].append(rn)

    flags = []
    counts = defaultdict(int)
    total = 0

    for rn, row in enumerate(lines[1:], 2):
        while len(row) < len(header):
            row.append('')
        if len(row) <= 1:
            continue

        raw = row[1].strip().strip('"')
        name = row[0].strip().strip('"')
        website = row[9].strip().strip('"') if len(row) > 9 else ''

        if not raw:
            continue
        total += 1

        email, multi = extract_email(raw)
        status = notes = issue = rec = ''

        if multi:
            status, notes = 'Malformed', f'Multiple emails in field'
            issue, rec = 'Multiple emails in single field', 'Split or pick primary'
        elif not email or not valid_format(email):
            status, notes = 'Malformed', 'Invalid email format'
            issue, rec = 'Invalid email format', 'Research correct email'
        else:
            domain = get_domain(email)
            if not domain:
                status, notes = 'Malformed', 'Cannot extract domain'
                issue, rec = 'Cannot extract domain', 'Research correct email'
            elif domain in TYPO_DOMAINS:
                status = 'Malformed'
                notes = f'Typo domain: {domain} → {TYPO_DOMAINS[domain]}'
                issue, rec = f'Domain typo: {domain}', f'Change to {TYPO_DOMAINS[domain]}'
            elif domain in INVALID_INVESTOR_DOMAINS:
                status = 'Malformed'
                notes = f'{domain} is not a real investor email domain'
                issue, rec = f'Invalid domain: {domain}', 'Research actual email'
            elif email.lower() in email_rows and len(email_rows[email.lower()]) > 1:
                others = [r for r in email_rows[email.lower()] if r != rn]
                status = 'Duplicate'
                notes = f'Same email in rows: {", ".join(str(r) for r in others)}'
                issue, rec = 'Duplicate email', 'Verify ownership'
            else:
                info = mx.get(domain)
                if not info or info['resolves'] == 'dead':
                    status, notes = 'Domain Dead', 'Domain does not resolve'
                    issue, rec = 'Domain dead', 'Email undeliverable; find new email'
                elif not info['has_mx']:
                    status, notes = 'Domain No MX', 'Domain exists but no MX records'
                    issue, rec = 'No mail server', 'May not be deliverable; verify'
                else:
                    is_personal = domain in PERSONAL_DOMAINS
                    if is_personal:
                        status = 'Personal Email — MX Valid'
                    else:
                        fd = extract_fund_domain(website)
                        if not fd:
                            status = 'Verified — MX Valid'
                            notes = 'No fund website to cross-reference'
                        else:
                            eb = '.'.join(domain.split('.')[-2:])
                            fb = '.'.join(fd.split('.')[-2:])
                            if eb == fb or domain == fd:
                                status = 'Verified — MX Valid'
                            elif fb in NON_FUND_DOMAINS:
                                status = 'Verified — MX Valid'
                                notes = 'Fund URL is profile page'
                            else:
                                status = 'Domain Mismatch'
                                notes = f'Email domain ({domain}) != fund domain ({fd})'
                                issue = 'Email/fund domain mismatch'
                                rec = 'Verify investor still at this fund'

        for i in es_idx:
            row[i] = status
        for i in en_idx:
            row[i] = notes
        counts[status] += 1
        if issue:
            flags.append({'Name': name, 'Email': raw, 'Issue': issue, 'Recommendation': rec})

    # Save
    with open(CSV_PATH, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(header)
        for row in lines[1:]:
            w.writerow(row)

    os.makedirs(os.path.dirname(FLAGS_PATH), exist_ok=True)
    with open(FLAGS_PATH, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['Name', 'Email', 'Issue', 'Recommendation'])
        w.writeheader()
        for fl in flags:
            w.writerow(fl)

    print(f"\n{'='*60}")
    print(f"EMAIL VERIFICATION SUMMARY")
    print(f"{'='*60}")
    print(f"Total emails checked: {total}")
    print(f"\nBreakdown by status:")
    for s, c in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {s:30s}: {c:5d} ({c/total*100:5.1f}%)")
    print(f"\nTotal flagged emails: {len(flags)}")
    print(f"Files saved:")
    print(f"  Updated CSV: {CSV_PATH}")
    print(f"  Flags CSV:   {FLAGS_PATH}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
