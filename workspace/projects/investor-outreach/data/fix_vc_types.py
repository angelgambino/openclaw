#!/usr/bin/env python3
"""Scan the master investor database and identify mislabeled investor types."""

import csv
import re
import sys

INPUT = "/data/.openclaw/workspace/projects/investor-outreach/MASTER-investor-database-v2.csv"
OUTPUT = "/data/.openclaw/workspace/projects/investor-outreach/data/vc-type-corrections-global.csv"

# Known VC firms (lowercase for matching)
KNOWN_VC_FIRMS = {
    # US Major
    "sequoia", "sequoia capital", "a16z", "andreessen horowitz", "benchmark", "benchmark capital",
    "craft ventures", "craft", "general catalyst", "general catalyst partners",
    "khosla ventures", "khosla", "greylock", "greylock partners", "accel", "accel partners",
    "lightspeed", "lightspeed venture partners", "lightspeed ventures",
    "founders fund", "kleiner perkins", "kleiner perkins caufield & byers", "kpcb",
    "nea", "new enterprise associates", "menlo ventures", "menlo",
    "redpoint", "redpoint ventures", "battery ventures", "battery",
    "ivp", "institutional venture partners", "bessemer", "bessemer venture partners",
    "true ventures", "floodgate", "floodgate fund", "cowboy ventures",
    "first round", "first round capital", "forerunner", "forerunner ventures",
    "initialized", "initialized capital", "slow ventures", "signalfire",
    "pear ventures", "pear vc", "freestyle", "freestyle capital",
    "uncork capital", "uncork", "softbank", "softbank vision fund",
    "tiger global", "tiger global management", "coatue", "coatue management",
    "ribbit capital", "ribbit", "insight partners", "insight venture partners", "insight",
    "matrix partners", "matrix", "crv", "charles river ventures",
    "canaan", "canaan partners", "scale venture partners", "scale ventures",
    "union square ventures", "usv", "lerer hippeau", "lerer hippeau ventures",
    "index ventures", "index", "gv", "google ventures",
    "norwest venture partners", "norwest", "spark capital", "spark",
    "bain capital ventures", "bain capital", "ggv capital", "ggv",
    "dft", "draper fisher jurvetson", "dfj", "draper associates",
    "felicis", "felicis ventures", "maverick ventures", "maverick capital",
    "thrive capital", "thrive", "altimeter", "altimeter capital",
    "addition", "d1 capital", "lone pine capital",
    "greenoaks", "greenoaks capital", "viking global",
    "dragoneer", "dragoneer investment group",
    "paradigm", "polychain capital", "pantera capital",
    "obvious ventures", "obvious", "collaborative fund",
    "eniac ventures", "eniac", "lux capital",
    "shasta ventures", "shasta", "upfront ventures", "upfront",
    "greycroft", "greycroft partners", "sutter hill ventures", "sutter hill",
    "amplify partners", "amplify", "root ventures",
    "mayfield", "mayfield fund", "august capital",
    "eclipse ventures", "eclipse", "emergence capital", "emergence",
    "icon ventures", "meritech capital", "meritech",
    "sapphire ventures", "sapphire", "trinity ventures", "trinity",
    "valar ventures", "valar", "value added ventures",
    "blumberg capital", "crosslink capital", "crosslink",
    "davidson technology growth debt", "silicon valley bank capital", "svb capital",
    "foundation capital", "foundry group", "foundry",
    "homebrew", "lowercase capital", "lowercase",
    "montage ventures", "mucker capital", "mucker",
    "new ground ventures", "next frontier capital",
    "notation capital", "notation", "precursor ventures", "precursor",
    "rre ventures", "rre", "venture guides",
    "wellspring capital", "innovation endeavors",
    "khosla impact", "kapor capital", "kapor",
    "revolution", "revolution ventures", "revolution growth",
    "NEA", "Venrock", "venrock",
    "bvp", "dcm", "dcm ventures",
    "eight roads ventures", "eight roads",
    "global founders capital",
    "goodwater capital", "goodwater",
    "harbourvest partners", "harbourvest",
    "iconiq capital", "iconiq",
    "jmi equity", "jmi",
    "marathon venture capital",
    "morningside ventures", "morningside",
    "oak hc/ft", "oak investment partners",
    "openview", "openview venture partners", "openview partners",
    "polaris partners", "polaris",
    "primavera capital",
    "qiming venture partners", "qiming",
    "softbank vision fund 2",
    "sozo ventures",
    "summit partners", "summit",
    "ta associates",
    "temasek",
    "warburg pincus",
    "wellington management",
    # More US VC
    "500 startups", "500 global",
    "abstract ventures",
    "accomplice", "accomplice vc",
    "afore capital", "afore",
    "alpine meridian ventures",
    "aspect ventures",
    "atlas venture", "atlas",
    "austin ventures",
    "boldstart ventures", "boldstart",
    "bonfire ventures", "bonfire",
    "bowery capital",
    "boxgroup", "box group",
    "breyer capital",
    "canapi ventures",
    "cendana capital",
    "cervin ventures",
    "chen capital", 
    "cienega capital",
    "cleo capital",
    "compound", "compound vc",
    "contrary", "contrary capital",
    "conversion capital",
    "costanoa ventures", "costanoa",
    "cross culture ventures",
    "data collective", "dcvc",
    "decibel partners", "decibel",
    "defy partners", "defy",
    "dell technologies capital",
    "digital currency group",
    "draper nexus", "draper nexus ventures",
    "drive capital",
    "e.ventures", "eventures",
    "elephant", "elephant partners",
    "equal ventures",
    "f-prime capital", "f prime",
    "flybridge capital partners", "flybridge",
    "fuel capital",
    "general atlantic",
    "glade brook capital",
    "goldcrest capital",
    "grasshopper bank",
    "great oaks venture capital", "great oaks",
    "gsv ventures",
    "harlem capital",
    "harvest venture partners",
    "haystack", "haystack vc",
    "high alpha",
    "hustle fund",
    "ideo ventures",
    "interplay ventures",
    "javelin venture partners", "javelin",
    "jai capital", 
    "keiretsu forum",
    "launchpad capital",
    "lead edge capital",
    "left lane capital",
    "m13",
    "m ventures",
    "marchcp", "march capital",
    "maveron",
    "menlo park capital",
    "monashees",
    "moxxie ventures",
    "mucker capital",
    "nfx",
    "next47",
    "next play capital",
    "northzone",
    "noro-moseley partners",
    "omers ventures",
    "operator partners",
    "origin ventures",
    "oxbow ventures",
    "pace capital",
    "partech", "partech partners",
    "pelion venture partners", "pelion",
    "plug and play", "plug and play ventures", "plug and play tech center",
    "point nine", "point nine capital",
    "prelude ventures",
    "resolute ventures",
    "ridge ventures",
    "s28 capital",
    "sands capital",
    "saama capital",
    "scout ventures",
    "sera ventures",
    "seven seven six", "776",
    "signature bank",
    "social capital",
    "social leverage",
    "southwestern venture capital",
    "stellation capital",
    "steps capital",
    "storm ventures",
    "stride ventures",
    "sv angel",
    "svb capital",
    "sync ventures",
    "tao capital partners",
    "tech coast angels",
    "tectonic ventures",
    "tenaya capital", "tenaya",
    "the venture city",
    "tribe capital",
    "two sigma ventures",
    "vibe capital",
    "virgilent capital",
    "westcap",
    "work-bench",
    "xfund",
    "yc", "y combinator",
    "zcash",
    "zetta venture partners", "zetta",
    # UK/European VC
    "seedcamp", "localglobe", "local globe",
    "felix capital", "balderton", "balderton capital",
    "passion capital", "hoxton ventures", "hoxton",
    "mmc ventures", "mmc",
    "atomico", "atomico ventures",
    "acton capital", "acton capital partners",
    "blossom capital", "blossom",
    "cherry ventures",
    "creandum",
    "dawn capital",
    "draper esprit", "draper spirit",
    "earlybird", "earlybird venture capital",
    "eqt ventures", "eqt",
    "european founders fund",
    "fabric ventures",
    "fly ventures",
    "frontline ventures",
    "general catalyst europe",
    "holtzbrinck ventures",
    "hv capital",
    "idinvest", "idinvest partners",
    "invested",
    "isomer capital",
    "kibo ventures",
    "kindred capital",
    "kinnevik",
    "lakestar",
    "lifeline ventures",
    "mangrove capital", "mangrove",
    "moonfire ventures",
    "mosaic ventures",
    "notion capital",
    "octopus ventures",
    "partech partners",
    "pentech ventures", "pentech",
    "piton capital",
    "picus capital",
    "project a", "project a ventures",
    "samaipata",
    "serena capital",
    "speedinvest",
    "stride vc",
    "target global",
    "talis capital",
    "valar ventures",
    "version one ventures",
    "b2venture",
    "btov partners",
    "connect ventures",
    "episode 1",
    "firstminute capital",
    "fuel ventures",
    "jag shaw baker",
    "marathon venture capital",
    "playfair capital",
    "sos ventures",
    "amadeus capital partners", "amadeus capital",
    "augmentum fintech",
    "downing ventures",
    "draper network",
    "entrepreneur first",
    "force over mass",
    "ip group",
    "jenson funding partners", "jenson",
    "mercia",
    "northern gritstone",
    "o2h ventures",
    "oxbridge angels",
    "parkwalk advisors", "parkwalk",
    "pembroke vct",
    "praetura ventures",
    "saxon capital",
    "ventures together",
    "yolo investments",
    # Additional global
    "dst global",
    "gic",
    "sovereign capital",
    "hillhouse capital",
    "sequoia capital china", "sequoia china",
    "sequoia capital india", "sequoia india",
    "matrix partners india",
    "matrix partners china",
    "beenext",
    "b capital group", "b capital",
    "vertex ventures",
    "wavemaker partners",
    "jungle ventures",
    "golden gate ventures",
    "east ventures",
    "500 durians",
    "gobi partners",
    "ceyuan ventures",
    "shunwei capital",
    "sinovation ventures",
    "zurich capital",
    "tenzing capital",
}

# Known accelerators (lowercase)
KNOWN_ACCELERATORS = {
    "y combinator", "yc", "ycombinator",
    "techstars", "tech stars",
    "500 startups", "500 global", "500",
    "plug and play", "plug and play tech center", "plug and play ventures",
    "seedcamp",
    "entrepreneur first", "ef",
    "dreamit ventures", "dreamit",
    "alchemist accelerator", "alchemist",
    "amplify.la", "amplify la",
    "betaworks",
    "boost vc",
    "capital factory",
    "chinaccelerator",
    "creative destruction lab",
    "creamery capital",
    "gener8tor",
    "globalfoundries",
    "google for startups",
    "greentown labs",
    "hax accelerator", "hax",
    "highway1",
    "indie.vc",
    "launch accelerator",
    "lemnos labs",
    "luminari capital",
    "mach49",
    "mass challenge", "masschallenge",
    "matter.vc",
    "mucker lab",
    "newchip",
    "newlab",
    "next36",
    "on deck",
    "parallel18",
    "quake capital",
    "sos ventures", # also an accelerator
    "startmate",
    "startx",
    "starburst",
    "surge ahead",
    "susa ventures",
    "tandem launch",
    "the food-x",
    "urban-x",
    "wefunder",
    "xrc labs",
    "zurich innovation hub",
}

# Known CVCs (corporate venture capital)
KNOWN_CVCS = {
    "google ventures", "gv",
    "intel capital",
    "salesforce ventures",
    "microsoft ventures", "m12",
    "nvidia gpu ventures",
    "qualcomm ventures",
    "samsung next", "samsung ventures",
    "cisco investments",
    "dell technologies capital",
    "comcast ventures",
    "verizon ventures",
    "t-mobile ventures",
    "amazon alexa fund",
    "american express ventures",
    "mastercard start path",
    "visa ventures",
    "jpmorgan chase",
    "goldman sachs growth equity",
    "citi ventures",
    "capital one ventures",
    "wells fargo strategic capital",
    "bosch venture capital",
    "bmw i ventures",
    "porsche ventures",
    "toyota ventures",
    "honda innovations",
    "mitsubishi ufj capital",
    "sumitomo corporation equity asia",
    "recruit strategic partners",
    "ntt venture capital",
    "softbank vision fund",
    "sony innovation fund",
    "baidu ventures",
    "tencent investment",
    "alibaba entrepreneurs fund",
    "xiaomi",
    "huawei capital",
    "samsung catalyst fund",
    "lg technology ventures",
    "slack fund",
    "workday ventures",
    "sap.io",
    "siemens venture capital",
    "shell ventures",
    "bp ventures",
    "chevron technology ventures",
    "total energy ventures",
    "exxonmobil ventures",
    "unilever ventures",
    "henkel ventures",
    "p&g ventures",
    "nike ventures",
    "adidas ventures",
    "novartis venture fund",
    "johnson & johnson innovation",
    "jnj innovation",
    "merck global health innovation fund",
    "pfizer ventures",
    "novo ventures",
    "roche venture fund",
    "astrazeneca",
    "bayer g4a",
    "abbvie ventures",
    "medtronic",
    "next47", # siemens
    "Robert Bosch Venture Capital",
    "bosch ventures",
    "caterpillar venture capital",
    "john deere ventures",
    "ge ventures",
    "honeywell ventures",
    "schneider electric ventures",
    "airbus ventures",
    "boeing horizonx",
    "lockheed martin ventures",
    "raytheon ventures",
    "northrop grumman",
}

# Keywords that suggest VC firm (in fund name)
VC_KEYWORDS = [
    "ventures", "venture partners", "venture capital",
    "growth equity", "growth capital",
    "vc fund", "seed fund",
    "early stage fund",
]

# These suggest VC but only for Angel→VC reclassification (not family office)
MODERATE_VC_KEYWORDS = ["capital partners"]

# Keywords that on their own are not sufficient (need context)
WEAK_VC_KEYWORDS = ["capital", "partners", "fund", "equity", "growth"]

# Known individual VCs (name -> firm mapping for recognition)
KNOWN_VC_PEOPLE = {
    "marc andreessen": "a16z",
    "ben horowitz": "a16z",
    "peter thiel": "founders fund",
    "vinod khosla": "khosla ventures",
    "reid hoffman": "greylock",
    "john doerr": "kleiner perkins",
    "mary meeker": "bond capital",
    "bill gurley": "benchmark",
    "alfred lin": "sequoia",
    "roelof botha": "sequoia",
    "mike moritz": "sequoia",
    "jim goetz": "sequoia",
    "brian singerman": "founders fund",
    "keith rabois": "founders fund",
    "sam altman": "y combinator",
    "paul graham": "y combinator",
    "jessica livingston": "y combinator",
    "brad feld": "foundry group",
    "fred wilson": "union square ventures",
    "chris sacca": "lowercase capital",
    "chamath palihapitiya": "social capital",
    "naval ravikant": "angellist",
    "tim draper": "draper associates",
    "steve jurvetson": "future ventures",
    "ann miura-ko": "floodgate",
    "mike maples": "floodgate",
    "kirsten green": "forerunner ventures",
    "josh kopelman": "first round capital",
    "howard morgan": "first round capital",
    "david lee": "sv angel",
    "ron conway": "sv angel",
    "garry tan": "initialized capital",
    "alexis ohanian": "seven seven six",
    "aileen lee": "cowboy ventures",
    "mitch lasky": "benchmark",
    "sarah tavel": "benchmark",
    "eric vishria": "benchmark",
    "jeff jordan": "a16z",
    "scott belsky": "a16z",
    "connie chan": "a16z",
    "andrew chen": "a16z",
    "chris dixon": "a16z",
    "katie haun": "haun ventures",
    "hemant taneja": "general catalyst",
    "niko bonatsos": "general catalyst",
    "kyle dent": "general catalyst",
    "satya patel": "homebrew",
    "hunter walk": "homebrew",
    "jenny lefcourt": "freestyle",
    "josh stein": "threshold ventures",
    "theresia gouw": "acrew capital",
    "jenny lee": "ggv capital",
    "hans tung": "ggv capital",
    "ravi viswanathan": "newview capital",
    "li jin": "atelier ventures",
    "sahil lavingia": "gumroad",
    "josh buckley": "buckley ventures",
    "lachy groom": "lachy groom",
    "elad gil": "color genomics",
    "david sacks": "craft ventures",
    "bill trenchard": "first round capital",
    "phin barnes": "first round capital",
    "lee fixel": "addition",
    "byron deeter": "bessemer",
    "ethan kurzweil": "bessemer",
    "talia goldberg": "bessemer",
    "matt turck": "firstmark capital",
    "amish jani": "firstmark capital",
    "bijan sabet": "spark capital",
    "nabeel hyatt": "spark capital",
    "jeremy liew": "lightspeed",
    "ravi mhatre": "lightspeed",
    "nicole quinn": "lightspeed",
    "mike vernal": "lightspeed",
    "peter fenton": "benchmark",
    "chetan puttagunta": "benchmark",
    "matt cohler": "benchmark",
    "rich barton": "benchmark",
    "kevin efrusy": "accel",
    "sonali de rycker": "accel",
    "arun mathew": "accel",
    "sameer gandhi": "accel",
    "lise buyer": "class v group",
    "arjun sethi": "tribe capital",
    "mamoon hamid": "kleiner perkins",
    "bucky moore": "kleiner perkins",
    "ilya fushman": "kleiner perkins",
    "josh lerner": "slow ventures",
    "sam lessin": "slow ventures",
    "will quist": "slow ventures",
    "scott stanford": "sherpa capital",
    "soraya darabi": "tmv",
    "sunil dhaliwal": "amplify partners",
    "mike dauber": "amplify partners",
    "lenny pruss": "amplify partners",
    "samir kaul": "khosla ventures",
    "david weiden": "khosla ventures",
    "sven strohband": "khosla ventures",
    "semil shah": "haystack",
    "charles hudson": "precursor ventures",
    "sydney thomas": "precursor ventures",
}


def normalize(s):
    """Lowercase, strip, remove extra whitespace."""
    if not s:
        return ""
    return re.sub(r'\s+', ' ', s.strip().lower())


def check_vc_firm_match(text, firm_set, is_name_field=False):
    """Check if text matches any known firm."""
    text_norm = normalize(text)
    if not text_norm:
        return None
    # Skip URLs
    if text_norm.startswith("http"):
        return None
    # Exact match
    if text_norm in firm_set:
        return text_norm
    # Check if any firm name is contained in the text
    # Only do substring matching for firms with 2+ words or 8+ chars to avoid false positives
    for firm in firm_set:
        words = firm.split()
        # For short/single-word firms, require near-exact match
        if len(words) == 1 and len(firm) < 8:
            # Only match if text starts with or equals the firm name
            # e.g., "spark" should not match "August Spark" 
            if text_norm == firm or text_norm.startswith(firm + " "):
                return firm
        elif len(words) >= 2 and len(firm) >= 8 and firm in text_norm:
            # For multi-word firm names 8+ chars, require word boundary at start
            import re as _re
            if _re.search(r'(?:^|\b)' + _re.escape(firm), text_norm):
                return firm
        elif len(words) == 1 and len(firm) >= 8:
            # Single-word firm, 8+ chars: require word boundary match
            import re as _re
            if _re.search(r'\b' + _re.escape(firm) + r'\b', text_norm):
                if is_name_field:
                    continue
                return firm
    return None


def has_vc_keywords(fund_name):
    """Check if fund name contains VC-indicating keywords."""
    fn = normalize(fund_name)
    if not fn:
        return False
    for kw in VC_KEYWORDS:
        if kw in fn:
            return True
    return False


def has_weak_vc_keywords(fund_name):
    """Check if fund name has weaker VC indicators."""
    fn = normalize(fund_name)
    if not fn:
        return False
    # Must have at least one weak keyword AND not be obviously non-VC
    non_vc_indicators = ["family", "wealth", "trust", "foundation", "charity", "consulting", 
                          "advisory", "real estate", "property", "holdings", "insurance",
                          "bank", "banking", "mortgage", "legal", "law firm", "accounting"]
    for indicator in non_vc_indicators:
        if indicator in fn:
            return False
    
    for kw in WEAK_VC_KEYWORDS:
        if kw in fn:
            return True
    return False


def classify_investor(name, fund, old_type):
    """
    Return (new_type, reason) or (None, None) if no change needed.
    """
    name_norm = normalize(name)
    fund_norm = normalize(fund)
    old_type_norm = normalize(old_type)
    
    # Skip if already correctly typed as VC, CVC, or Accelerator
    if any(t in old_type_norm for t in ["venture capital", "vc fund", "corporate venture"]):
        # Already has VC-like type
        pass
    
    # Check if the old type contains "angel" or "family office" — these are the ones to fix
    is_angel = "angel" in old_type_norm
    is_family_office = "family office" in old_type_norm
    is_already_vc = "vc" in old_type_norm.split(",")[0].strip() if old_type_norm else False
    
    # If already properly tagged, skip
    if not is_angel and not is_family_office:
        # Also check for generic types that might hide VCs
        if old_type_norm and ("investor" in old_type_norm or "limited partner" in old_type_norm):
            pass  # These might need fixing too
        else:
            return None, None
    
    # Check for known accelerators first
    accel_match = check_vc_firm_match(fund, KNOWN_ACCELERATORS) or check_vc_firm_match(name, KNOWN_ACCELERATORS, is_name_field=True)
    if accel_match:
        return "Accelerator", f"Known accelerator: {accel_match}"
    
    # Check for known CVCs
    cvc_match = check_vc_firm_match(fund, KNOWN_CVCS) or check_vc_firm_match(name, KNOWN_CVCS, is_name_field=True)
    if cvc_match:
        return "CVC", f"Known corporate VC: {cvc_match}"
    
    # Check for known VC firms
    vc_match = check_vc_firm_match(fund, KNOWN_VC_FIRMS) or check_vc_firm_match(name, KNOWN_VC_FIRMS, is_name_field=True)
    if vc_match:
        if is_family_office:
            return "VC", f"Known VC firm: {vc_match} (was Family Office)"
        return "VC", f"Known VC firm: {vc_match}"
    
    # Check for known VC people
    if name_norm in KNOWN_VC_PEOPLE:
        firm = KNOWN_VC_PEOPLE[name_norm]
        if is_angel:
            return "Angel/VC", f"Known VC partner at {firm} (also angel invests)"
        return "VC", f"Known VC partner at {firm}"
    
    # Check fund name for VC keywords
    if fund_norm:
        if has_vc_keywords(fund_norm):
            if is_angel:
                return "VC", f"Fund name contains VC keywords: '{fund}'"
            elif is_family_office:
                # Only reclassify family offices if it has strong VC keywords (not just "capital partners")
                if any(kw in fund_norm for kw in ["ventures", "venture partners", "venture capital", "vc fund", "seed fund"]):
                    return "Family Office/VC", f"Fund name contains VC keywords: '{fund}'"
                # Otherwise leave as Family Office
        elif any(kw in fund_norm for kw in MODERATE_VC_KEYWORDS):
            if is_angel:
                return "VC", f"Fund name suggests VC: '{fund}'"
            # Don't reclassify family offices on moderate keywords alone
    
    # Check name field for VC-like names (the entity IS a VC firm)
    if name_norm and not fund_norm:
        if has_vc_keywords(name_norm):
            if is_angel:
                return "VC", f"Name appears to be a VC firm: '{name}'"
            elif is_family_office:
                return "VC", f"Name appears to be a VC firm: '{name}'"
    
    return None, None


def main():
    corrections = []
    total_rows = 0
    
    with open(INPUT, 'r', encoding='utf-8', errors='replace') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_rows += 1
            name = row.get('Name', '').strip()
            fund = row.get('Fund', '').strip()
            old_type = row.get('Type of Investor', '').strip()
            location_city = row.get('Location (City)', '').strip()
            location_state = row.get('Location (State)', '').strip()
            location_country = row.get('Location (Country)', '').strip()
            
            location = ', '.join(filter(None, [location_city, location_state, location_country]))
            
            new_type, reason = classify_investor(name, fund, old_type)
            
            if new_type and new_type != old_type:
                corrections.append({
                    'Name': name,
                    'Fund': fund,
                    'Location': location,
                    'Old Type': old_type,
                    'New Type': new_type,
                    'Reason': reason,
                })
    
    # Write corrections log
    with open(OUTPUT, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Name', 'Fund', 'Location', 'Old Type', 'New Type', 'Reason'])
        writer.writeheader()
        writer.writerows(corrections)
    
    # Summary
    print(f"\nTotal rows scanned: {total_rows}")
    print(f"Total corrections: {len(corrections)}")
    print(f"\nCorrections by new type:")
    from collections import Counter
    type_counts = Counter(c['New Type'] for c in corrections)
    for t, count in type_counts.most_common():
        print(f"  {t}: {count}")
    
    print(f"\nCorrections by country:")
    country_counts = Counter()
    for c in corrections:
        parts = c['Location'].split(', ')
        country = parts[-1] if parts else 'Unknown'
        country_counts[country] += 1
    for country, count in country_counts.most_common(20):
        print(f"  {country}: {count}")
    
    print(f"\nSample corrections:")
    for c in corrections[:30]:
        print(f"  {c['Name']} | {c['Fund']} | {c['Old Type']} → {c['New Type']} | {c['Reason']}")
    
    print(f"\nOutput saved to: {OUTPUT}")


if __name__ == "__main__":
    main()
