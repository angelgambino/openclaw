#!/usr/bin/env python3
"""Generate all deal-specific investor lists from the master database."""

import csv
import os
import re
from collections import defaultdict

BASE = "/data/.openclaw/workspace/projects/investor-outreach"
MASTER = os.path.join(BASE, "MASTER-investor-database-v2.csv")
FILM = os.path.join(BASE, "data/film-investors.csv")
VIEWS = os.path.join(BASE, "views")
os.makedirs(VIEWS, exist_ok=True)

# Load master DB
with open(MASTER, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    master_fields = reader.fieldnames
    investors = list(reader)

print(f"Loaded {len(investors)} investors from master DB")
print(f"Columns: {master_fields}")

# Load film investors
with open(FILM, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    film_fields = reader.fieldnames
    film_investors = list(reader)

print(f"Loaded {len(film_investors)} film investors")

# --- Scoring function ---
def score_investor(inv):
    """Score 0-10 based on data quality criteria."""
    s = 0
    if inv.get("Email", "").strip():
        s += 1
    if inv.get("LinkedIn", "").strip():
        s += 1
    if inv.get("Sector: Investment Thesis", "").strip():
        s += 1
    if inv.get("How to Pitch This Investor", "").strip():
        s += 1
    if inv.get("Founder Reputation", "").strip():
        s += 1
    if inv.get("Fund Size", "").strip():
        s += 1
    if inv.get("Notable Portfolio Companies", "").strip():
        s += 1
    if inv.get("Priority Tier", "").strip().lower() == "high":
        s += 1
    if inv.get("Data Confidence Level", "").strip().lower() == "high":
        s += 1
    if inv.get("Pitch Submission URL", "").strip():
        s += 1
    return s

# --- Keyword matching ---
def matches_keywords(inv, keywords):
    """Check if investor's sector matches any keyword (case-insensitive)."""
    sector = inv.get("Sector: Investment Thesis", "").lower()
    # Also check fund name and type
    fund = inv.get("Fund", "").lower()
    name = inv.get("Name", "").lower()
    text = f"{sector} {fund} {name}"
    
    for kw in keywords:
        kw_lower = kw.lower()
        # Use word boundary matching for short keywords like "AI"
        if len(kw_lower) <= 3:
            if re.search(r'\b' + re.escape(kw_lower) + r'\b', text):
                return True
        else:
            if kw_lower in text:
                return True
    return False

def is_california(inv):
    """Check if investor is California-based."""
    state = inv.get("Location (State)", "").lower()
    city = inv.get("Location (City)", "").lower()
    country = inv.get("Location (Country)", "").lower()
    loc_text = f"{state} {city} {country}"
    return "california" in loc_text or "san francisco" in loc_text or "los angeles" in loc_text or "palo alto" in loc_text or "menlo park" in loc_text

# --- Deal definitions ---
deals = {
    "needle": {
        "keywords": ["AI", "artificial intelligence", "marketing", "martech", "adtech", 
                     "e-commerce", "ecommerce", "commerce", "SaaS", "software", "SMB", 
                     "consumer", "enterprise", "B2B", "retail", "DTC"],
        "best_file": "needle-best-100.csv",
        "filtered_file": "needle-filtered.csv",
        "ca_prefer": False,
    },
    "countryline": {
        "keywords": ["music", "media", "entertainment", "creator", "content", "digital media",
                     "gaming", "esports", "community", "social", "consumer", "fan", "film"],
        "best_file": "countryline-best-100.csv",
        "filtered_file": "countryline-filtered.csv",
        "ca_prefer": False,
        "include_film": True,
    },
    "psymed": {
        "keywords": ["mental health", "health", "wellness", "brain", "neuro", "psychedelic",
                     "biotech", "life science", "therapeutic", "longevity", "consciousness",
                     "behavioral", "pharma", "medtech"],
        "best_file": "psymed-best-100.csv",
        "filtered_file": "psymed-filtered.csv",
        "ca_prefer": False,
    },
    "ciis": {
        "keywords": ["mental health", "education", "health", "wellness", "psychedelic",
                     "consciousness", "brain", "behavioral", "training", "workforce"],
        "best_file": "ciis-best-100.csv",
        "filtered_file": "ciis-filtered.csv",
        "ca_prefer": False,
    },
    "htw": {
        "keywords": ["impact", "health", "wellness", "AI", "sustainability", "clean tech",
                     "social impact", "human", "longevity", "mental health", "consciousness", "ethics"],
        "best_file": "htw-best-100.csv",
        "filtered_file": "htw-filtered.csv",
        "ca_prefer": True,
    },
}

# --- Process each deal ---
deal_filtered = {}  # deal_name -> set of investor names (for multi-deal)
deal_filtered_lists = {}  # deal_name -> list of investors

summary = {}

for deal_name, config in deals.items():
    keywords = config["keywords"]
    
    # Filter matching investors
    filtered = [inv for inv in investors if matches_keywords(inv, keywords)]
    
    # For countryline, add film investors (convert to master format)
    if config.get("include_film"):
        for fi in film_investors:
            # Create a master-format record from film investor
            converted = {col: "" for col in master_fields}
            converted["Name"] = fi.get("Name", "")
            converted["Email"] = fi.get("Email", "")
            converted["Fund"] = fi.get("Fund", "")
            converted["Type of Investor"] = fi.get("Type of Investor", "")
            converted["Sector: Investment Thesis"] = fi.get("Sector", "")
            converted["LinkedIn"] = fi.get("LinkedIn", "")
            converted["Website"] = fi.get("Website", "")
            converted["Typical Check Size"] = fi.get("Typical Investment Size", "")
            # Parse location
            loc = fi.get("Location", "")
            converted["Location (City)"] = loc.split(",")[0].strip() if "," in loc else loc
            # Check if already in filtered by name
            existing_names = {inv["Name"].strip().lower() for inv in filtered}
            if converted["Name"].strip().lower() not in existing_names:
                filtered.append(converted)
    
    # Score and sort
    scored = [(inv, score_investor(inv)) for inv in filtered]
    
    # For HTW, boost California investors
    if config["ca_prefer"]:
        scored = [(inv, s + (2 if is_california(inv) else 0)) for inv, s in scored]
    
    # Sort by score desc, then name asc
    scored.sort(key=lambda x: (-x[1], x[0].get("Name", "").lower()))
    
    # Track for multi-deal
    deal_filtered[deal_name] = {inv.get("Name", "").strip().lower() for inv, _ in scored}
    deal_filtered_lists[deal_name] = scored
    
    # Write filtered (all matches)
    filtered_path = os.path.join(VIEWS, config["filtered_file"])
    with open(filtered_path, "w", newline="", encoding="utf-8") as f:
        # Add Score column
        out_fields = master_fields + ["Quality Score"]
        writer = csv.DictWriter(f, fieldnames=out_fields)
        writer.writeheader()
        for inv, s in scored:
            row = dict(inv)
            row["Quality Score"] = s
            writer.writerow(row)
    
    # Write best 100
    best = scored[:100]
    best_path = os.path.join(VIEWS, config["best_file"])
    with open(best_path, "w", newline="", encoding="utf-8") as f:
        out_fields = master_fields + ["Quality Score"]
        writer = csv.DictWriter(f, fieldnames=out_fields)
        writer.writeheader()
        for inv, s in best:
            row = dict(inv)
            row["Quality Score"] = s
            writer.writerow(row)
    
    summary[deal_name] = {
        "filtered": len(scored),
        "best": len(best),
        "top_score": best[0][1] if best else 0,
        "min_score": best[-1][1] if best else 0,
    }
    print(f"\n{deal_name.upper()}: {len(scored)} filtered, {len(best)} best")
    if best:
        print(f"  Score range in best 100: {best[-1][1]}-{best[0][1]}")

# --- MULTI-DEAL: investors matching 3+ deals ---
print("\n--- MULTI-DEAL ANALYSIS ---")

# Count how many deals each investor matches
investor_deals = defaultdict(set)
for deal_name, names in deal_filtered.items():
    for name in names:
        investor_deals[name].add(deal_name)

# Filter to 3+ deals
multi_deal_names = {name for name, d in investor_deals.items() if len(d) >= 3}
print(f"Investors matching 3+ deals: {len(multi_deal_names)}")

# Get full investor records for multi-deal
# Use the first occurrence from any deal's filtered list
multi_deal_records = []
seen = set()
for deal_name, scored_list in deal_filtered_lists.items():
    for inv, s in scored_list:
        name_key = inv.get("Name", "").strip().lower()
        if name_key in multi_deal_names and name_key not in seen:
            seen.add(name_key)
            matching = ", ".join(sorted(investor_deals[name_key]))
            multi_deal_records.append((inv, s, matching, len(investor_deals[name_key])))

# Sort by number of matching deals desc, then score desc, then name
multi_deal_records.sort(key=lambda x: (-x[3], -x[1], x[0].get("Name", "").lower()))

# Write multi-deal-investors.csv (all)
multi_all_path = os.path.join(VIEWS, "multi-deal-investors.csv")
with open(multi_all_path, "w", newline="", encoding="utf-8") as f:
    out_fields = master_fields + ["Quality Score", "Matching Deals", "Deal Count"]
    writer = csv.DictWriter(f, fieldnames=out_fields)
    writer.writeheader()
    for inv, s, matching, count in multi_deal_records:
        row = dict(inv)
        row["Quality Score"] = s
        row["Matching Deals"] = matching
        row["Deal Count"] = count
        writer.writerow(row)

# Write multi-deal-best.csv (top by score)
multi_best = multi_deal_records[:100] if len(multi_deal_records) > 100 else multi_deal_records
multi_best_path = os.path.join(VIEWS, "multi-deal-best.csv")
with open(multi_best_path, "w", newline="", encoding="utf-8") as f:
    out_fields = master_fields + ["Quality Score", "Matching Deals", "Deal Count"]
    writer = csv.DictWriter(f, fieldnames=out_fields)
    writer.writeheader()
    for inv, s, matching, count in multi_best:
        row = dict(inv)
        row["Quality Score"] = s
        row["Matching Deals"] = matching
        row["Deal Count"] = count
        writer.writerow(row)

summary["multi-deal"] = {
    "filtered": len(multi_deal_records),
    "best": len(multi_best),
}

# --- Print final summary ---
print("\n" + "="*60)
print("FINAL SUMMARY")
print("="*60)
for deal, stats in summary.items():
    print(f"{deal.upper():15s} | Best: {stats['best']:4d} | Filtered: {stats['filtered']:5d}")
print("="*60)
print("All files written to:", VIEWS)
