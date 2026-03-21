#!/usr/bin/env python3
"""Check MX records for domains using Python DNS resolution."""

import socket
import subprocess
import csv
import sys

DOMAINS_FILE = "/tmp/unique_domains.txt"
OUTPUT_FILE = "/tmp/domain_mx_results.csv"

def check_mx(domain):
    """Check if domain has MX records and resolves."""
    # Try getent for MX-like check (connect to SMTP port)
    try:
        results = socket.getaddrinfo(domain, 'smtp', socket.AF_UNSPEC, socket.SOCK_STREAM)
        if results:
            return True, True  # has_mx=True, resolves=True
    except socket.gaierror:
        pass
    
    # Try basic resolution (A record)
    try:
        socket.gethostbyname(domain)
        return False, True  # no MX but resolves
    except socket.gaierror as e:
        if 'Name or service not known' in str(e) or 'No address associated' in str(e):
            return False, False  # dead
        return False, False

def main():
    # Read domains
    with open(DOMAINS_FILE) as f:
        domains = [line.strip() for line in f if line.strip()]
    
    print(f"Checking {len(domains)} domains...", file=sys.stderr)
    
    with open(OUTPUT_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['domain', 'has_mx', 'mx_records', 'resolves'])
        
        for i, domain in enumerate(domains):
            if i % 500 == 0:
                print(f"  Progress: {i}/{len(domains)}", file=sys.stderr)
            
            has_mx, resolves = check_mx(domain)
            
            if has_mx:
                writer.writerow([domain, 'yes', '', 'yes'])
            elif resolves:
                writer.writerow([domain, 'no', '', 'yes'])
            else:
                writer.writerow([domain, 'no', '', 'dead'])
    
    print(f"Done. Results in {OUTPUT_FILE}", file=sys.stderr)
    
    # Quick stats
    mx_count = 0
    no_mx_count = 0
    dead_count = 0
    with open(OUTPUT_FILE) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['has_mx'] == 'yes':
                mx_count += 1
            elif row['resolves'] == 'dead':
                dead_count += 1
            else:
                no_mx_count += 1
    
    print(f"MX Valid: {mx_count}, No MX: {no_mx_count}, Dead: {dead_count}", file=sys.stderr)

if __name__ == '__main__':
    main()
