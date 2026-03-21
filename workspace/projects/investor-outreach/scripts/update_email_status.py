#!/usr/bin/env python3
"""
Email verification: Update MASTER-investor-database-v2.csv with deep email verification.
Uses MX record results from domain_mx_results.csv and applies pattern checks.
"""

import csv
import re
import sys
from collections import defaultdict

CSV_PATH = "/data/.openclaw/workspace/projects/investor-outreach/MASTER-investor-database-v2.csv"
MX_RESULTS = "/tmp/domain_mx_results.csv"
OUTPUT_PATH = CSV_PATH  # overwrite
FLAGS_PATH = "/data/.openclaw/workspace/projects/investor-outreach/data/email-verification-flags.csv"

# Personal email domains (well-known free email providers)
PERSONAL_DOMAINS = {
    'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com',
    'icloud.com', 'mail.com', 'protonmail.com', 'zoho.com', 'yandex.com',
    'live.com', 'msn.com', 'me.com', 'mac.com', 'hotmail.co.uk',
    'sbcglobal.net', 'optonline.net', 'hotmail.co.uk',
}

# Known invalid email domains for investors (not real personal email domains)
INVALID_INVESTOR_DOMAINS = {
    'crunchbase.com', 'linkedin.com', 'pitchbook.com',
}

# Common domain typos
TYPO_DOMAINS = {
    'gmial.com': 'gmail.com',
    'gmal.com': 'gmail.com',
    'gmil.com': 'gmail.com',
    'yahooo.com': 'yahoo.com',
    'yaho.com': 'yahoo.com',
    'hotmal.com': 'hotmail.com',
    'outlok.com': 'outlook.com',
    'gooogle.com': 'google.com',
}

def load_mx_results():
    """Load domain MX check results."""
    results = {}
    with open(MX_RESULTS, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            domain = row['domain'].strip().lower()
            results[domain] = {
                'has_mx': row['has_mx'].strip().lower() == 'yes',
                'resolves': row['resolves'].strip().lower(),
            }
    return results

def extract_email(email_field):
    """Extract the primary email from a potentially malformed field."""
    if not email_field or not email_field.strip():
        return None, False
    
    email_field = email_field.strip().strip('"')
    
    # Check if multiple emails (contains comma within the email string)
    if ',' in email_field:
        # Multiple emails - this is malformed
        parts = [p.strip() for p in email_field.split(',') if '@' in p]
        if parts:
            return parts[0], True  # Return first, flag as malformed
        return None, True
    
    email = email_field.strip()
    if '@' not in email:
        return None, False
    
    return email, False

def get_domain(email):
    """Extract domain from email."""
    if not email or '@' not in email:
        return None
    return email.split('@')[1].strip().lower()

def extract_fund_domain(website):
    """Extract domain from a website URL."""
    if not website:
        return None
    website = website.strip().strip('"')
    # Remove protocol
    website = re.sub(r'^https?://', '', website)
    # Remove www.
    website = re.sub(r'^www\.', '', website)
    # Get just domain
    domain = website.split('/')[0].split('?')[0].strip().lower()
    return domain if domain else None

def is_valid_format(email):
    """Basic email format validation."""
    if not email:
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def main():
    mx_results = load_mx_results()
    print(f"Loaded MX results for {len(mx_results)} domains")
    
    # Read the CSV
    with open(CSV_PATH, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Parse CSV properly
    lines = list(csv.reader(content.splitlines()))
    if not lines:
        print("Empty CSV!")
        return
    
    header = lines[0]
    
    # Find relevant column indices
    name_idx = 0  # Name
    email_idx = 1  # Email
    website_idx = 9  # Website
    fund_idx = 10  # Fund
    
    # Find the Email Status columns (there are TWO - we update both)
    email_status_indices = []
    email_notes_indices = []
    for i, col in enumerate(header):
        if col.strip() == 'Email Status':
            email_status_indices.append(i)
        elif col.strip() == 'Email Notes':
            email_notes_indices.append(i)
    
    print(f"Email Status columns at indices: {email_status_indices}")
    print(f"Email Notes columns at indices: {email_notes_indices}")
    
    # Track email occurrences for duplicate detection
    email_count = defaultdict(list)
    for row_num, row in enumerate(lines[1:], start=2):
        if len(row) <= email_idx:
            continue
        email_raw = row[email_idx].strip().strip('"')
        if not email_raw:
            continue
        primary_email, _ = extract_email(email_raw)
        if primary_email:
            email_count[primary_email.lower()].append(row_num)
    
    # Process each row
    flags = []  # For the flags CSV
    status_counts = defaultdict(int)
    total_checked = 0
    
    for row_num, row in enumerate(lines[1:], start=2):
        if len(row) <= email_idx:
            continue
            
        # Ensure row has enough columns
        while len(row) < len(header):
            row.append('')
        
        email_raw = row[email_idx].strip().strip('"')
        name = row[name_idx].strip().strip('"')
        website = row[website_idx].strip().strip('"') if len(row) > website_idx else ''
        fund = row[fund_idx].strip().strip('"') if len(row) > fund_idx else ''
        
        if not email_raw:
            # No email - skip
            continue
        
        total_checked += 1
        primary_email, is_multi = extract_email(email_raw)
        
        new_status = ''
        new_notes = ''
        flag_issue = ''
        flag_recommendation = ''
        
        # Method 2: Check for malformed (multiple emails)
        if is_multi:
            new_status = 'Malformed'
            new_notes = f'Multiple emails in field: {email_raw}'
            flag_issue = 'Multiple emails in single field'
            flag_recommendation = 'Split into separate records or pick primary email'
        elif not primary_email or not is_valid_format(primary_email):
            new_status = 'Malformed'
            new_notes = f'Invalid email format'
            flag_issue = 'Invalid email format'
            flag_recommendation = 'Research correct email'
        else:
            domain = get_domain(primary_email)
            
            if not domain:
                new_status = 'Malformed'
                new_notes = 'Cannot extract domain'
                flag_issue = 'Cannot extract domain'
                flag_recommendation = 'Research correct email'
            else:
                # Check for typo domains
                if domain in TYPO_DOMAINS:
                    new_status = 'Malformed'
                    new_notes = f'Likely typo domain: {domain} → {TYPO_DOMAINS[domain]}'
                    flag_issue = f'Domain typo: {domain}'
                    flag_recommendation = f'Change to {TYPO_DOMAINS[domain]}'
                
                # Check for known invalid investor domains
                elif domain in INVALID_INVESTOR_DOMAINS:
                    new_status = 'Malformed'
                    new_notes = f'{domain} is not a real email domain for investors'
                    flag_issue = f'Invalid investor domain: {domain}'
                    flag_recommendation = 'Research actual email address'
                
                # Check duplicates
                elif primary_email.lower() in email_count and len(email_count[primary_email.lower()]) > 1:
                    other_rows = [r for r in email_count[primary_email.lower()] if r != row_num]
                    new_status = 'Duplicate'
                    new_notes = f'Same email used by rows: {", ".join(str(r) for r in other_rows)}'
                    flag_issue = 'Duplicate email across multiple records'
                    flag_recommendation = 'Verify which person owns this email'
                
                else:
                    # Method 1: DNS/MX Check
                    mx_info = mx_results.get(domain)
                    
                    if mx_info is None:
                        # Domain wasn't checked (shouldn't happen)
                        new_status = 'Domain Dead'
                        new_notes = 'Domain not found in DNS'
                        flag_issue = 'Domain does not resolve'
                        flag_recommendation = 'Email likely undeliverable; research new email'
                    elif mx_info['resolves'] == 'dead':
                        new_status = 'Domain Dead'
                        new_notes = 'Domain does not resolve (NXDOMAIN)'
                        flag_issue = 'Domain is dead'
                        flag_recommendation = 'Email undeliverable; research new email'
                    elif not mx_info['has_mx']:
                        if mx_info['resolves'] in ('yes', 'maybe'):
                            new_status = 'Domain No MX'
                            new_notes = 'Domain exists but has no MX records'
                            flag_issue = 'No mail server configured'
                            flag_recommendation = 'Email may not be deliverable; verify or find alternative'
                        else:
                            new_status = 'Domain Dead'
                            new_notes = 'Domain does not resolve'
                            flag_issue = 'Domain does not resolve'
                            flag_recommendation = 'Email undeliverable; research new email'
                    else:
                        # Domain has MX records
                        is_personal = domain in PERSONAL_DOMAINS
                        
                        if is_personal:
                            new_status = 'Personal Email — MX Valid'
                            new_notes = ''
                        else:
                            # Method 3: Cross-reference domain with fund website
                            fund_domain = extract_fund_domain(website)
                            email_domain = domain
                            
                            # Check if email domain matches fund/website domain
                            domain_matches = False
                            if fund_domain:
                                # Compare base domains (strip subdomains)
                                email_base = '.'.join(email_domain.split('.')[-2:])
                                fund_base = '.'.join(fund_domain.split('.')[-2:])
                                domain_matches = (email_base == fund_base) or (email_domain == fund_domain)
                            
                            if not fund_domain:
                                new_status = 'Verified — MX Valid'
                                new_notes = 'No fund website to cross-reference'
                            elif domain_matches:
                                new_status = 'Verified — MX Valid'
                                new_notes = ''
                            else:
                                # Domain mismatch but MX is valid
                                # Check if it's a crunchbase/linkedin/angel.co fund URL (not real fund domains)
                                non_fund_domains = {'crunchbase.com', 'linkedin.com', 'angel.co', 'about.me', 'pitchbook.com'}
                                fund_base = '.'.join(fund_domain.split('.')[-2:]) if fund_domain else ''
                                
                                if fund_base in non_fund_domains:
                                    new_status = 'Verified — MX Valid'
                                    new_notes = 'Fund URL is a profile page, not fund website'
                                else:
                                    new_status = 'Domain Mismatch'
                                    new_notes = f'Email domain ({email_domain}) != fund domain ({fund_domain})'
                                    flag_issue = 'Email domain does not match fund website'
                                    flag_recommendation = 'Verify investor still at this fund; may have moved'
        
        # Update all Email Status and Email Notes columns
        for idx in email_status_indices:
            if idx < len(row):
                row[idx] = new_status
        for idx in email_notes_indices:
            if idx < len(row):
                row[idx] = new_notes
        
        status_counts[new_status] += 1
        
        # Add to flags if there's an issue
        if flag_issue:
            flags.append({
                'Name': name,
                'Email': email_raw,
                'Issue': flag_issue,
                'Recommendation': flag_recommendation,
            })
    
    # Write updated CSV
    with open(OUTPUT_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in lines[1:]:
            writer.writerow(row)
    
    print(f"\nUpdated CSV saved to: {OUTPUT_PATH}")
    
    # Write flags CSV
    import os
    os.makedirs(os.path.dirname(FLAGS_PATH), exist_ok=True)
    with open(FLAGS_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Name', 'Email', 'Issue', 'Recommendation'])
        writer.writeheader()
        for flag in flags:
            writer.writerow(flag)
    
    print(f"Flags CSV saved to: {FLAGS_PATH}")
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"EMAIL VERIFICATION SUMMARY")
    print(f"{'='*60}")
    print(f"Total emails checked: {total_checked}")
    print(f"\nBreakdown by status:")
    for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
        pct = (count / total_checked * 100) if total_checked > 0 else 0
        print(f"  {status:30s}: {count:5d} ({pct:5.1f}%)")
    print(f"\nTotal flagged emails: {len(flags)}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
