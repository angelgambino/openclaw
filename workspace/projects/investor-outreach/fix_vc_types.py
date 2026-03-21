#!/usr/bin/env python3
"""Task 1: Fix VC Type Tagging for California investors."""

import csv
import os
import re

INPUT = 'MASTER-investor-database-v2.csv'
OUTPUT = INPUT  # overwrite
CORRECTIONS_DIR = 'data'
CORRECTIONS_FILE = os.path.join(CORRECTIONS_DIR, 'vc-type-corrections.csv')

# Known VC firms (exact or partial match on Fund column)
KNOWN_VC_FIRMS = {
    # Tier 1
    'sequoia', 'a16z', 'andreessen horowitz', 'benchmark', 'craft ventures',
    'general catalyst', 'khosla ventures', 'greylock', 'accel', 'lightspeed',
    'founders fund', 'kleiner perkins', 'ggv capital', 'notable capital',
    'nea', 'new enterprise associates', 'menlo ventures', 'redpoint',
    'battery ventures', 'ivp', 'institutional venture partners', 'bessemer',
    'true ventures', 'floodgate', 'cowboy ventures', 'first round capital',
    'forerunner', 'initialized', 'slow ventures', 'signalfire',
    'pear vc', 'freestyle', 'uncork', 'abstract ventures', 'amplify partners',
    'basis set', 'bonfire ventures', 'correlation ventures', 'crosscut',
    'dcvc', 'data collective', 'define ventures', 'felicis', 'homebrew',
    'hustle fund', 'lux capital', 'mayfield', 'obvious ventures', 'susa ventures',
    'bain capital ventures', 'canaan', 'crv', 'index ventures', 'insight partners',
    'matrix partners', 'ribbit capital', 'scale venture partners', 'shasta ventures',
    'sierra ventures', 'storm ventures', 'trinity ventures', 'venrock', 'wing vc',
    'y combinator', '500 global', '500 startups', 'techstars', 'plug and play',
    # Additional known VC firms
    'acme capital', 'ame cloud ventures', 'amino capital', 'baroda ventures',
    'baruch future ventures', 'basis set ventures', 'bee partners', 'bellco capital',
    'boost vc', 'buena vista fund', 'conscience vc', 'concordia ventures',
    'core ventures', 'cure ventures', 'dolby family ventures', 'enter capital',
    'expert dojo', 'founders circle capital', 'gen3 ventures', 'gnite',
    'illuminate ventures', 'kapor capital', 'lumia capital', 'mehta ventures',
    'merus capital', 'nimble ventures', 'north range ventures', 'omidyar network',
    'pirque ventures', 'premanco ventures', 'presight capital', 'samsung next',
    'social leverage', 'softbank', 'sony innovation fund', 'spark capital',
    'tao capital partners', 'tenoneten', 'thrive capital', 'vertex ventures',
    'vilcap', 'work play ventures', 'xg ventures', '1517 fund', '1984 ventures',
    '99vc', 'slauson', 'halogen capital', 'iconiq capital',
    'samsung next', 'tpg growth',
}

# Patterns in Fund name that indicate VC
VC_PATTERNS = [
    r'\bventures?\b', r'\bcapital\b', r'\bpartners\b', r'\bfund\b', r'\bvc\b',
    r'\baccelerator\b', r'\bincubator\b',
]

# Patterns that indicate NOT a VC (family office, wealth management, etc.)
EXCLUDE_PATTERNS = [
    r'family office', r'wealth\s*(management|advisor|partner|resource)',
    r'advisory', r'advisors?\b', r'asset\s*management', r'trust\b',
    r'foundation\b', r'equit(y|ies)', r'holdings\b', r'investment office',
    r'private wealth', r'financial\s*(service|planning)', r'roush investments',
    r'real estate', r'insurance', r'accounting', r'tax\b', r'cpa\b',
    r'law\b', r'legal\b', r'llp\b',
]

# But override exclude if the fund is a KNOWN VC firm
def is_known_vc(fund_lower):
    for kv in KNOWN_VC_FIRMS:
        if kv in fund_lower:
            return True, f"Known VC firm match: {kv}"
    return False, ""

def matches_vc_pattern(fund_lower):
    for pat in VC_PATTERNS:
        if re.search(pat, fund_lower):
            return True, f"Fund name contains VC keyword pattern: {pat}"
    return False, ""

def matches_exclude(fund_lower):
    for pat in EXCLUDE_PATTERNS:
        if re.search(pat, fund_lower):
            return True
    return False

def should_reclassify(row):
    """Determine if a row should be reclassified as VC. Returns (should_change, reason)."""
    fund = row.get('Fund', '').strip()
    name = row.get('Name', '').strip()
    current_type = row.get('Type of Investor', '').strip()
    
    # Skip if already VC
    if current_type == 'VC':
        return False, ""
    
    fund_lower = fund.lower()
    name_lower = name.lower()
    
    # Check known VC firms in fund name
    known, reason = is_known_vc(fund_lower)
    if known:
        return True, reason
    
    # Check known VC firms in person name (some have crunchbase URLs as fund)
    # Skip this - names are person names not firm names
    
    # Check VC patterns in fund name, but exclude family offices etc.
    pattern_match, reason = matches_vc_pattern(fund_lower)
    if pattern_match:
        if not matches_exclude(fund_lower):
            return True, reason
        else:
            # Even if excluded, check if it's a known VC
            return False, ""
    
    return False, ""

def main():
    os.makedirs(CORRECTIONS_DIR, exist_ok=True)
    
    # Read all rows
    with open(INPUT, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    
    corrections = []
    changed = 0
    
    for row in rows:
        state = row.get('Location (State)', '').strip()
        if 'California' not in state and 'CA' not in state:
            continue
        
        should_change, reason = should_reclassify(row)
        if should_change:
            old_type = row['Type of Investor']
            row['Type of Investor'] = 'VC'
            corrections.append({
                'Name': row['Name'],
                'Fund': row.get('Fund', ''),
                'Old Type': old_type,
                'New Type': 'VC',
                'Reason': reason,
            })
            changed += 1
    
    # Write corrected CSV
    with open(OUTPUT, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    # Write corrections log
    with open(CORRECTIONS_FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Name', 'Fund', 'Old Type', 'New Type', 'Reason'])
        writer.writeheader()
        writer.writerows(corrections)
    
    print(f"Total corrections: {changed}")
    print(f"Corrections saved to: {CORRECTIONS_FILE}")

if __name__ == '__main__':
    main()
