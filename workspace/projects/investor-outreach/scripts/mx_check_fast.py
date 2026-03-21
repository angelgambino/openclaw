#!/usr/bin/env python3
"""Fast MX check using concurrent futures with timeout."""

import socket
import csv
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

DOMAINS_FILE = "/tmp/unique_domains.txt"
OUTPUT_FILE = "/tmp/domain_mx_results.csv"

socket.setdefaulttimeout(3)  # 3 second timeout per lookup

def check_mx(domain):
    """Check if domain has MX records and resolves."""
    try:
        results = socket.getaddrinfo(domain, 'smtp', socket.AF_UNSPEC, socket.SOCK_STREAM)
        if results:
            return domain, 'yes', 'yes'
    except (socket.gaierror, socket.timeout, OSError):
        pass
    
    try:
        socket.gethostbyname(domain)
        return domain, 'no', 'yes'
    except (socket.gaierror, socket.timeout, OSError):
        return domain, 'no', 'dead'

def main():
    with open(DOMAINS_FILE) as f:
        domains = [line.strip() for line in f if line.strip()]
    
    print(f"Checking {len(domains)} domains with 50 threads...", file=sys.stderr)
    
    results = {}
    done = 0
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(check_mx, d): d for d in domains}
        for future in as_completed(futures):
            domain, has_mx, resolves = future.result()
            results[domain] = (has_mx, resolves)
            done += 1
            if done % 500 == 0:
                print(f"  Progress: {done}/{len(domains)}", file=sys.stderr)
    
    # Write results
    with open(OUTPUT_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['domain', 'has_mx', 'mx_records', 'resolves'])
        for domain in domains:
            has_mx, resolves = results.get(domain, ('no', 'dead'))
            writer.writerow([domain, has_mx, '', resolves])
    
    # Stats
    mx = sum(1 for v in results.values() if v[0] == 'yes')
    no_mx = sum(1 for v in results.values() if v[0] == 'no' and v[1] == 'yes')
    dead = sum(1 for v in results.values() if v[1] == 'dead')
    print(f"\nDone! MX Valid: {mx}, No MX but resolves: {no_mx}, Dead: {dead}", file=sys.stderr)

if __name__ == '__main__':
    main()
