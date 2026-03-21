#!/usr/bin/env python3
"""Fill Sector: Investment Thesis for investors in the master database."""

import csv
import re
import sys

INPUT = "/data/.openclaw/workspace/projects/investor-outreach/MASTER-investor-database-v2.csv"
OUTPUT = INPUT  # overwrite

SECTOR_COL = "Sector: Investment Thesis"
FUND_COL = "Fund"
NAME_COL = "Name"

# ── Well-known funds → sectors ──────────────────────────────────────────────
KNOWN_FUNDS = {
    "a16z": "Enterprise, Consumer, Crypto, Fintech, Bio, Healthcare, AI, Gaming",
    "andreessen horowitz": "Enterprise, Consumer, Crypto, Fintech, Bio, Healthcare, AI, Gaming",
    "sequoia": "Enterprise, Consumer, Healthcare, Fintech, AI",
    "sequoia capital": "Enterprise, Consumer, Healthcare, Fintech, AI",
    "benchmark": "Enterprise, Consumer, SaaS, Marketplace",
    "benchmark capital": "Enterprise, Consumer, SaaS, Marketplace",
    "greylock": "Enterprise, Consumer, AI, Data Infrastructure",
    "greylock partners": "Enterprise, Consumer, AI, Data Infrastructure",
    "accel": "Enterprise, SaaS, Fintech, Consumer, Security",
    "accel partners": "Enterprise, SaaS, Fintech, Consumer, Security",
    "lightspeed venture partners": "Enterprise, Consumer, Healthcare, Fintech",
    "lightspeed ventures": "Enterprise, Consumer, Healthcare, Fintech",
    "lightspeed": "Enterprise, Consumer, Healthcare, Fintech",
    "kleiner perkins": "Enterprise, Consumer, Healthcare, Sustainability, AI",
    "kpcb": "Enterprise, Consumer, Healthcare, Sustainability, AI",
    "bessemer venture partners": "Enterprise, SaaS, Healthcare, Consumer",
    "bessemer": "Enterprise, SaaS, Healthcare, Consumer",
    "index ventures": "Enterprise, Consumer, Fintech, Gaming",
    "founders fund": "Deep Tech, Enterprise, Consumer, Space, AI, Biotech",
    "general catalyst": "Enterprise, Consumer, Healthcare, Fintech, AI",
    "general catalyst partners": "Enterprise, Consumer, Healthcare, Fintech, AI",
    "khosla ventures": "Deep Tech, Healthcare, AI, Sustainability, Enterprise",
    "union square ventures": "Consumer, Fintech, Crypto, Marketplace",
    "usv": "Consumer, Fintech, Crypto, Marketplace",
    "first round capital": "Enterprise, Consumer, SaaS",
    "first round": "Enterprise, Consumer, SaaS",
    "spark capital": "Consumer, Enterprise, Fintech",
    "insight partners": "Enterprise, SaaS, Data, Security",
    "insight venture partners": "Enterprise, SaaS, Data, Security",
    "tiger global": "Enterprise, Consumer, Fintech, E-commerce",
    "tiger global management": "Enterprise, Consumer, Fintech, E-commerce",
    "coatue": "Enterprise, Consumer, Fintech, AI",
    "coatue management": "Enterprise, Consumer, Fintech, AI",
    "ribbit capital": "Fintech, Financial Services",
    "qed investors": "Fintech, Financial Services",
    "felicis ventures": "Enterprise, Consumer, Healthcare, Fintech",
    "felicis": "Enterprise, Consumer, Healthcare, Fintech",
    "floodgate": "Consumer, Enterprise, Marketplace",
    "true ventures": "Enterprise, Consumer, AI",
    "500 startups": "Enterprise, Consumer, SaaS, Fintech",
    "500 global": "Enterprise, Consumer, SaaS, Fintech",
    "y combinator": "Enterprise, Consumer, SaaS, AI",
    "yc": "Enterprise, Consumer, SaaS, AI",
    "techstars": "Enterprise, Consumer, SaaS",
    "nea": "Enterprise, Healthcare, Consumer, AI",
    "new enterprise associates": "Enterprise, Healthcare, Consumer, AI",
    "battery ventures": "Enterprise, SaaS, Data Infrastructure",
    "ivp": "Enterprise, Consumer, SaaS",
    "institutional venture partners": "Enterprise, Consumer, SaaS",
    "gv": "Enterprise, Healthcare, Consumer, AI",
    "google ventures": "Enterprise, Healthcare, Consumer, AI",
    "intel capital": "Enterprise, AI, IoT, Cloud, Semiconductor",
    "salesforce ventures": "Enterprise, SaaS, AI, Cloud",
    "softbank": "Enterprise, Consumer, AI, Robotics",
    "softbank vision fund": "Enterprise, Consumer, AI, Robotics",
    "lux capital": "Deep Tech, AI, Biotech, Space, Robotics",
    "initialized capital": "Enterprise, Consumer, AI",
    "initialized": "Enterprise, Consumer, AI",
    "cre venture capital": "Real Estate, PropTech",
    "fifth wall": "Real Estate, PropTech, Construction Tech",
    "metaprop": "Real Estate, PropTech",
    "camber creek": "Real Estate, PropTech",
    "obvious ventures": "Sustainability, Clean Tech, Healthcare",
    "breakthrough energy ventures": "Clean Tech, Climate, Energy",
    "energy impact partners": "Clean Tech, Energy, Sustainability",
    "congruent ventures": "Clean Tech, Sustainability, Energy",
    "s2g ventures": "Food & Beverage, AgTech, Clean Tech",
    "cultivian sandbox ventures": "Food & Beverage, AgTech",
    "abandoned ventures": "Food & Beverage, AgTech",
    "svb capital": "Enterprise, Healthcare, Fintech",
    "silicon valley bank": "Enterprise, Healthcare, Fintech",
    "canaan partners": "Enterprise, Healthcare, Fintech",
    "canaan": "Enterprise, Healthcare, Fintech",
    "polaris partners": "Enterprise, Healthcare",
    "arch venture partners": "Healthcare, Life Sciences, Biotech",
    "flagship pioneering": "Healthcare, Life Sciences, Biotech",
    "orbimed": "Healthcare, Life Sciences, Biotech",
    "versant ventures": "Healthcare, Life Sciences, Biotech",
    "section 32": "Healthcare, Life Sciences, AI, Deep Tech",
    "gsk ventures": "Healthcare, Life Sciences, Biotech",
    "johnson & johnson innovation": "Healthcare, Life Sciences, Biotech",
    "novo holdings": "Healthcare, Life Sciences, Biotech",
    "reach capital": "Education, EdTech",
    "owl ventures": "Education, EdTech",
    "learn capital": "Education, EdTech",
    "rethink education": "Education, EdTech",
    "sapphire ventures": "Enterprise, SaaS, AI",
    "sapphire sport": "Sports, Consumer",
    "maverick ventures": "Enterprise, Consumer, Healthcare",
    "forerunner ventures": "Consumer, DTC, Retail, E-commerce",
    "forerunner": "Consumer, DTC, Retail, E-commerce",
    "kirsten green": "Consumer, DTC, Retail, E-commerce",
    "imaginary ventures": "Consumer, DTC, Retail",
    "cotu ventures": "Consumer, Retail",
    "amplify.la": "Consumer, Media, Entertainment",
    "upfront ventures": "Consumer, Enterprise, SaaS",
    "lowercase capital": "Consumer, Enterprise",
    "foundry group": "Enterprise, SaaS",
    "foundry": "Enterprise, SaaS",
    "menlo ventures": "Enterprise, Consumer, Healthcare",
    "norwest venture partners": "Enterprise, Healthcare, Consumer",
    "norwest": "Enterprise, Healthcare, Consumer",
    "dfj": "Enterprise, Consumer, Deep Tech",
    "draper fisher jurvetson": "Enterprise, Consumer, Deep Tech",
    "redpoint ventures": "Enterprise, Consumer, Infrastructure",
    "redpoint": "Enterprise, Consumer, Infrastructure",
    "madrona": "Enterprise, AI, Cloud",
    "madrona venture group": "Enterprise, AI, Cloud",
    "maveron": "Consumer, DTC",
    "aspect ventures": "Enterprise, Consumer, AI",
    "cowboy ventures": "Enterprise, Consumer, AI",
    "softtech vc": "Consumer, Enterprise, SaaS",
    "uncork capital": "Enterprise, Consumer, SaaS",
    "eniac ventures": "Consumer, Mobile, Enterprise",
    "betaworks": "Media, Consumer, AI",
    "lerer hippeau": "Consumer, Media, E-commerce",
    "lerer hippeau ventures": "Consumer, Media, E-commerce",
    "greycroft": "Consumer, Media, E-commerce, Digital Media",
    "greycroft partners": "Consumer, Media, E-commerce, Digital Media",
    "ggv capital": "Enterprise, Consumer, E-commerce",
    "goodwater capital": "Consumer, E-commerce, Marketplace",
    "craft ventures": "Enterprise, Consumer, Fintech, Crypto",
    "8vc": "Enterprise, Deep Tech, Healthcare, Defense",
    "thrive capital": "Enterprise, Consumer, Fintech",
    "general atlantic": "Enterprise, Consumer, Healthcare, Fintech",
    "kkr": "Enterprise, Consumer, Healthcare, Infrastructure",
    "warburg pincus": "Enterprise, Consumer, Healthcare, Financial Services",
    "bain capital ventures": "Enterprise, Consumer, Healthcare, Fintech",
    "goldman sachs": "Fintech, Enterprise, Healthcare",
    "morgan stanley": "Fintech, Enterprise, Healthcare",
    "jpmorgan": "Fintech, Enterprise, Healthcare",
    "citi ventures": "Fintech, Enterprise",
    "citigroup": "Fintech, Enterprise",
    "comcast ventures": "Media, Consumer, Enterprise",
    "disney accelerator": "Media, Entertainment, Consumer",
    "walt disney": "Media, Entertainment, Consumer",
    "amazon": "Enterprise, Consumer, AI, Cloud, Logistics",
    "amazon alexa fund": "AI, Voice, Smart Home, Consumer",
    "microsoft": "Enterprise, AI, Cloud, Gaming",
    "m12": "Enterprise, AI, Cloud",
    "google": "Enterprise, AI, Consumer, Cloud",
    "meta": "Consumer, Social, AI, VR/AR",
    "apple": "Consumer, Enterprise, Healthcare",
    "nvidia": "AI, GPU, Deep Tech, Robotics",
    "qualcomm ventures": "IoT, 5G, AI, Semiconductor",
    "samsung ventures": "Consumer, Enterprise, AI, Semiconductor",
    "cisco investments": "Enterprise, Networking, Security, IoT",
    "dell technologies capital": "Enterprise, Cloud, AI, Infrastructure",
    "ibm ventures": "Enterprise, AI, Cloud, Blockchain",
    "baidu ventures": "AI, Enterprise, Consumer",
    "tencent": "Gaming, Consumer, Enterprise, AI",
    "alibaba": "E-commerce, Consumer, Enterprise, Cloud",
    "sutter hill ventures": "Enterprise, SaaS, Data",
    "emergence capital": "Enterprise, SaaS",
    "openview": "Enterprise, SaaS",
    "openview venture partners": "Enterprise, SaaS",
    "matrix partners": "Enterprise, Consumer, SaaS",
    "bvp": "Enterprise, SaaS, Healthcare, Consumer",
    "b capital group": "Enterprise, Consumer, Fintech",
    "b capital": "Enterprise, Consumer, Fintech",
    "andreessen": "Enterprise, Consumer, Crypto, Fintech, Bio, Healthcare, AI, Gaming",
    "flybridge": "Enterprise, Consumer, AI",
    "flybridge capital": "Enterprise, Consumer, AI",
    "flybridge capital partners": "Enterprise, Consumer, AI",
    "iqt": "Aerospace, Defense, Technology, AI",
    "in-q-tel": "Aerospace, Defense, Technology, AI",
    "hg ventures": "Sustainability, Clean Tech, Energy",
    "sandalphon capital": "Fintech, Digital Media, E-commerce",
    "precursor ventures": "Enterprise, Consumer, SaaS",
    "precursor": "Enterprise, Consumer, SaaS",
    "backstage capital": "Consumer, Enterprise, SaaS",
    "revolution": "Enterprise, Consumer",
    "revolution ventures": "Enterprise, Consumer",
    "revolution growth": "Enterprise, Consumer",
    "revolution's rise of the rest": "Enterprise, Consumer",
    "rise of the rest": "Enterprise, Consumer",
    "steve case": "Enterprise, Consumer",
    "neo": "Enterprise, Consumer, AI",
    "boldstart ventures": "Enterprise, SaaS, Security",
    "boldstart": "Enterprise, SaaS, Security",
    "work-bench": "Enterprise, SaaS",
    "costanoa ventures": "Enterprise, SaaS, Data",
    "costanoa": "Enterprise, SaaS, Data",
    "notation capital": "Enterprise, SaaS, Data",
    "notation": "Enterprise, SaaS, Data",
    "two sigma ventures": "AI, Data, Fintech",
    "two sigma": "AI, Data, Fintech",
    "radical ventures": "AI, Machine Learning",
    "air street capital": "AI, Machine Learning",
    "playground global": "AI, Robotics, Deep Tech",
    "dcvc": "Deep Tech, AI, Data, Enterprise",
    "data collective": "Deep Tech, AI, Data, Enterprise",
    "wing venture capital": "Enterprise, SaaS, Infrastructure",
    "wing": "Enterprise, SaaS, Infrastructure",
    "contrary": "Enterprise, Consumer, AI",
    "contrary capital": "Enterprise, Consumer, AI",
    "pear vc": "Enterprise, Consumer, AI",
    "pear": "Enterprise, Consumer, AI",
    "rough draft ventures": "Enterprise, Consumer",
    "dorm room fund": "Enterprise, Consumer",
    "hustle fund": "Enterprise, Consumer, SaaS",
    "m13": "Consumer, Enterprise, Fintech",
    "crosscut ventures": "Enterprise, Consumer",
    "mucker capital": "Enterprise, Consumer, SaaS",
    "bonfire ventures": "Enterprise, SaaS",
    "fika ventures": "Enterprise, SaaS, AI",
    "wonder ventures": "Consumer, Enterprise",
    "wavemaker partners": "Enterprise, Deep Tech",
    "susa ventures": "Enterprise, Consumer, Data",
    "susa": "Enterprise, Consumer, Data",
    "soma capital": "Enterprise, Consumer, SaaS",
    "slow ventures": "Consumer, Crypto, Media",
    "collaborative fund": "Consumer, Sustainability, Food",
    "resolute ventures": "Enterprise, Consumer",
    "nextview ventures": "Consumer, Enterprise",
    "nextview": "Consumer, Enterprise",
    "homebrew": "Enterprise, Consumer",
    "haystack": "Consumer, Enterprise, SaaS",
    "compound": "Enterprise, Consumer, Fintech",
    "compound vc": "Enterprise, Consumer, Fintech",
    "next frontier capital": "Enterprise, Consumer, SaaS",
    "right side capital": "Enterprise, Consumer",
    "right side capital management": "Enterprise, Consumer",
    "cherry ventures": "Enterprise, Consumer, SaaS",
    "point nine capital": "Enterprise, SaaS, Marketplace",
    "point nine": "Enterprise, SaaS, Marketplace",
    "balderton capital": "Enterprise, Consumer, Fintech",
    "balderton": "Enterprise, Consumer, Fintech",
    "atomico": "Enterprise, Consumer, Deep Tech",
    "northzone": "Enterprise, Consumer, Fintech",
    "creandum": "Enterprise, Consumer, SaaS",
    "earlybird": "Enterprise, Consumer, Healthcare",
    "earlybird venture capital": "Enterprise, Consumer, Healthcare",
    "hv capital": "Enterprise, Consumer, Marketplace",
    "project a": "Enterprise, Consumer, E-commerce",
    "project a ventures": "Enterprise, Consumer, E-commerce",
    "blume ventures": "Enterprise, Consumer, Fintech",
    "nexus venture partners": "Enterprise, Consumer, AI",
    "elevation capital": "Enterprise, Consumer, Fintech",
    "matrix partners india": "Enterprise, Consumer, Fintech",
    "kalaari capital": "Enterprise, Consumer, Healthcare",
    "kalaari": "Enterprise, Consumer, Healthcare",
    "jungle ventures": "Enterprise, Consumer, Fintech",
    "vertex ventures": "Enterprise, Consumer, Healthcare",
    "golden gate ventures": "Enterprise, Consumer, Fintech",
    "monk's hill ventures": "Enterprise, Consumer, SaaS",
    "winklevoss capital": "Crypto, Blockchain, Web3",
    "paradigm": "Crypto, Blockchain, Web3",
    "polychain capital": "Crypto, Blockchain, Web3",
    "pantera capital": "Crypto, Blockchain, Web3",
    "digital currency group": "Crypto, Blockchain, Web3",
    "dcg": "Crypto, Blockchain, Web3",
    "coinbase ventures": "Crypto, Blockchain, Web3",
    "binance labs": "Crypto, Blockchain, Web3",
    "animoca brands": "Crypto, Gaming, Web3",
    "dragonfly capital": "Crypto, Blockchain, Web3",
    "dragonfly": "Crypto, Blockchain, Web3",
    "a16z crypto": "Crypto, Blockchain, Web3",
    "electric capital": "Crypto, Blockchain, Web3",
    "framework ventures": "Crypto, DeFi, Web3",
    "multicoin capital": "Crypto, Blockchain, Web3",
    "1kx": "Crypto, Blockchain, Web3",
    "hack vc": "Crypto, Blockchain, Web3",
    "variant fund": "Crypto, Blockchain, Web3",
    "variant": "Crypto, Blockchain, Web3",
    "placeholder vc": "Crypto, Blockchain, Web3",
    "blockchain capital": "Crypto, Blockchain, Web3",
    "galaxy digital": "Crypto, Blockchain, Web3",
    "cms holdings": "Crypto, Blockchain, Web3",
    "delphi ventures": "Crypto, Blockchain, Web3",
    "mechanism capital": "Crypto, Blockchain, Web3",
    "maven ventures": "Consumer, Healthcare",
    "rock health": "Healthcare, Digital Health",
    "oak hc/ft": "Healthcare, Fintech",
    "healthx ventures": "Healthcare, Digital Health",
    "7wireventures": "Healthcare, Digital Health",
    "7wire ventures": "Healthcare, Digital Health",
    "f-prime capital": "Healthcare, Life Sciences, Enterprise",
    "f-prime": "Healthcare, Life Sciences, Enterprise",
    "venrock": "Healthcare, Enterprise, Consumer",
    "morningside ventures": "Healthcare, Life Sciences",
    "morningside": "Healthcare, Life Sciences",
    "deerfield management": "Healthcare, Life Sciences, Biotech",
    "deerfield": "Healthcare, Life Sciences, Biotech",
    "ra capital management": "Healthcare, Life Sciences, Biotech",
    "ra capital": "Healthcare, Life Sciences, Biotech",
    "bios partners": "Healthcare, Life Sciences, Biotech",
    "biomatics capital": "Healthcare, Life Sciences, AI",
    "cambia health solutions": "Healthcare",
    "town hall ventures": "Healthcare, Consumer",
    "future ventures": "Deep Tech, Sustainability, Space",
    "starburst": "Aerospace, Defense",
    "starburst ventures": "Aerospace, Defense",
    "starburst aerospace": "Aerospace, Defense",
    "space capital": "Aerospace, Space",
    "space angels": "Aerospace, Space",
    "seraphim capital": "Aerospace, Space",
    "seraphim": "Aerospace, Space",
    "lockheed martin ventures": "Aerospace, Defense",
    "boeing horizonx": "Aerospace, Defense",
    "airbus ventures": "Aerospace, Defense",
    "sosv": "Deep Tech, Hardware, Biotech",
    "hax": "Hardware, Robotics, Deep Tech",
    "bolt": "Hardware, Consumer, Manufacturing",
    "eclipse ventures": "Industrial, Manufacturing, Deep Tech",
    "eclipse": "Industrial, Manufacturing, Deep Tech",
    "root ventures": "Hardware, Deep Tech",
    "upside foods": "Food & Beverage, Alternative Proteins",
    "tastebud fund": "Food & Beverage",
    "prelude ventures": "Clean Tech, Sustainability, AgTech",
    "elemental excelerator": "Clean Tech, Sustainability, Energy",
    "clean energy ventures": "Clean Tech, Energy",
    "prime impact fund": "Clean Tech, Sustainability",
    "powerhouse ventures": "Clean Tech, Energy",
    "systemiq capital": "Clean Tech, Sustainability",
    "regeneration.vc": "Sustainability, Climate",
    "closed loop partners": "Sustainability, Circular Economy",
    "tesla": "Clean Tech, Energy, Automotive",
    "toyota ventures": "Mobility, Clean Tech, Robotics",
    "gm ventures": "Mobility, Clean Tech, Automotive",
    "ford": "Mobility, Clean Tech, Automotive",
    "porsche ventures": "Mobility, Automotive",
    "bmw i ventures": "Mobility, Automotive, Clean Tech",
    "mobility fund": "Mobility, Transportation",
    "fontinalis partners": "Mobility, Transportation",
    "autotech ventures": "Mobility, Automotive",
    "maniv mobility": "Mobility, Automotive",
    "500 istanbul": "Enterprise, Consumer, Fintech",
    "wamda capital": "Enterprise, Consumer, Fintech",
    "flat6labs": "Enterprise, Consumer",
    "algebra ventures": "Enterprise, Consumer, Fintech",
    "sawari ventures": "Enterprise, Consumer",
    "cathay innovation": "Enterprise, Consumer, Sustainability",
    "eurazeo": "Enterprise, Consumer, Healthcare",
    "partech": "Enterprise, Consumer, Fintech",
    "idinvest": "Enterprise, Consumer",
    "kima ventures": "Enterprise, Consumer, SaaS",
    "alven": "Enterprise, Consumer, SaaS",
    "serena": "Enterprise, Consumer, AI",
    "elaia": "Enterprise, Deep Tech, AI",
    "breega": "Enterprise, Consumer, SaaS",
    "headline": "Enterprise, Consumer, Fintech",
    "e.ventures": "Enterprise, Consumer",
    "target global": "Enterprise, Consumer, Fintech",
    "global founders capital": "Enterprise, Consumer",
    "gfc": "Enterprise, Consumer",
    "rocket internet": "E-commerce, Consumer, Marketplace",
    "speedinvest": "Enterprise, Consumer, Fintech",
    "notion capital": "Enterprise, SaaS",
    "moonfire ventures": "Enterprise, Consumer, AI",
    "hoxton ventures": "Enterprise, Consumer",
    "seedcamp": "Enterprise, Consumer, SaaS",
    "entrepreneur first": "Enterprise, Consumer, Deep Tech",
    "ef": "Enterprise, Consumer, Deep Tech",
    "antler": "Enterprise, Consumer",
    "jungle vc": "Consumer, E-commerce",
    "picus capital": "Enterprise, Consumer, SaaS",
    "btov partners": "Enterprise, Deep Tech, Healthcare",
    "cherry": "Enterprise, Consumer, SaaS",
    "lunar ventures": "Deep Tech, AI",
    "visionaries club": "Enterprise, SaaS",
    "la famiglia": "Enterprise, SaaS, Industrial",
    "10t holdings": "Fintech, Crypto, Digital Assets",
    "10t": "Fintech, Crypto, Digital Assets",
    "propel venture partners": "Fintech, Financial Services",
    "nyca partners": "Fintech, Financial Services",
    "nyca": "Fintech, Financial Services",
    "fin vc": "Fintech, Financial Services",
    "fin capital": "Fintech, Financial Services",
    "clocktower technology ventures": "Fintech, Financial Services",
    "capgemini ventures": "Enterprise, Digital Transformation",
    "sap": "Enterprise, SaaS",
    "sap.io": "Enterprise, SaaS",
    "workday ventures": "Enterprise, SaaS, HR Tech",
    "slack fund": "Enterprise, SaaS, Collaboration",
    "zoom ventures": "Enterprise, SaaS, Communication",
    "hubspot ventures": "Enterprise, SaaS, Marketing",
    "stripe": "Fintech, Payments, SaaS",
    "plaid": "Fintech, Financial Services",
    "ares management": "Enterprise, Real Estate, Infrastructure",
    "blackstone": "Enterprise, Real Estate, Infrastructure",
    "carlyle": "Enterprise, Healthcare, Defense",
    "the carlyle group": "Enterprise, Healthcare, Defense",
    "tpg": "Enterprise, Healthcare, Consumer",
    "tpg capital": "Enterprise, Healthcare, Consumer",
    "advent international": "Enterprise, Healthcare, Consumer",
    "vista equity partners": "Enterprise, SaaS",
    "vista equity": "Enterprise, SaaS",
    "thoma bravo": "Enterprise, SaaS, Security",
    "permira": "Enterprise, Consumer, Healthcare",
    "apax partners": "Enterprise, Consumer, Healthcare",
    "apax": "Enterprise, Consumer, Healthcare",
    "ey ventures": "Enterprise, Professional Services",
    "deloitte ventures": "Enterprise, Professional Services",
    "mckinsey": "Enterprise, Professional Services",
    "capricorn investment group": "Sustainability, Clean Tech, Enterprise",
    "obvious": "Sustainability, Clean Tech, Healthcare",
    "dbl partners": "Sustainability, Clean Tech, Enterprise",
    "impact engine": "Sustainability, Social Impact",
    "kapor capital": "Social Impact, Enterprise",
    "emerson collective": "Social Impact, Education, Media",
    "omidyar network": "Social Impact, Financial Inclusion, Education",
    "chan zuckerberg initiative": "Healthcare, Education, Social Impact",
    "czi": "Healthcare, Education, Social Impact",
    "bill & melinda gates foundation": "Healthcare, Education, Social Impact",
    "gates foundation": "Healthcare, Education, Social Impact",
    "skoll foundation": "Social Impact, Sustainability",
    "luminate": "Media, Social Impact",
    "pivotal ventures": "Social Impact, Gender Equity",
    "echoing green": "Social Impact",
    "village capital": "Social Impact, Fintech, Healthcare",
    "unshackled ventures": "Immigration, Enterprise, Consumer",
    "unshackled": "Immigration, Enterprise, Consumer",
    "concrete rose capital": "Consumer, Enterprise, Social Impact",
    "harlem capital": "Consumer, Enterprise, Fintech",
    "harlem capital partners": "Consumer, Enterprise, Fintech",
    "cake ventures": "Consumer, Enterprise",
    "dream ventures": "Consumer, Enterprise",
    "cross culture ventures": "Consumer, Enterprise, Media",
    "cross culture": "Consumer, Enterprise, Media",
    "talent x opportunity": "Education, Social Impact",
    "txo": "Education, Social Impact",
    "ulu ventures": "Enterprise, Consumer",
    "acrew capital": "Enterprise, Consumer, AI",
    "acrew": "Enterprise, Consumer, AI",
    "all raise": "Enterprise, Consumer",
    "female founders fund": "Consumer, Enterprise, Healthcare",
    "aspect ventures": "Enterprise, Consumer, AI",
    "bce capital": "Enterprise, Consumer",
    "springbank collective": "Consumer, Enterprise",
    "1517 fund": "Education, Deep Tech, Consumer",
    "thiel fellowship": "Deep Tech, Enterprise",
    "thiel capital": "Deep Tech, Enterprise",
    "peter thiel": "Deep Tech, Enterprise, Consumer",
    "valor ventures": "Enterprise, Consumer, SaaS",
    "valor": "Enterprise, Consumer, SaaS",
    "panoramic ventures": "Enterprise, Consumer, SaaS",
    "panoramic": "Enterprise, Consumer, SaaS",
    "base10 partners": "Enterprise, Consumer, AI",
    "base10": "Enterprise, Consumer, AI",
    "haus capital": "Enterprise, Consumer",
    "stellation capital": "Enterprise, Consumer",
    "signal peak ventures": "Enterprise, SaaS",
    "signal peak": "Enterprise, SaaS",
    "pelion venture partners": "Enterprise, SaaS",
    "pelion": "Enterprise, SaaS",
    "kickstart fund": "Enterprise, Consumer, SaaS",
    "kickstart": "Enterprise, Consumer, SaaS",
    "zetta venture partners": "AI, Machine Learning, Data",
    "zetta": "AI, Machine Learning, Data",
    "comet labs": "AI, Robotics",
    "amplify partners": "Enterprise, AI, Developer Tools",
    "gradient ventures": "AI, Machine Learning",
    "ai fund": "AI, Machine Learning",
    "samsung next": "Consumer, AI, Enterprise",
    "alexa fund": "AI, Voice, Smart Home",
}

# ── Well-known investors → sectors ──────────────────────────────────────────
KNOWN_INVESTORS = {
    "marc andreessen": "Enterprise, Consumer, Crypto, AI",
    "ben horowitz": "Enterprise, Consumer, Crypto, AI",
    "peter thiel": "Deep Tech, Enterprise, Consumer",
    "reid hoffman": "Enterprise, Consumer, AI",
    "vinod khosla": "Deep Tech, Healthcare, AI, Sustainability",
    "john doerr": "Enterprise, Consumer, Healthcare, Sustainability",
    "mary meeker": "Enterprise, Consumer, Healthcare",
    "bill gurley": "Enterprise, Consumer, Marketplace",
    "chris sacca": "Consumer, Enterprise",
    "keith rabois": "Enterprise, Consumer, Real Estate",
    "naval ravikant": "Enterprise, Consumer, Crypto",
    "paul graham": "Enterprise, Consumer, SaaS",
    "sam altman": "AI, Enterprise, Consumer",
    "fred wilson": "Consumer, Fintech, Crypto, Marketplace",
    "brad feld": "Enterprise, SaaS",
    "jason calacanis": "Enterprise, Consumer, AI",
    "tim draper": "Enterprise, Consumer, Crypto",
    "esther dyson": "Healthcare, Enterprise",
    "ron conway": "Consumer, Enterprise, SaaS",
    "stewart butterfield": "Enterprise, SaaS",
    "alexis ohanian": "Consumer, Enterprise, Crypto",
    "garry tan": "Enterprise, Consumer, SaaS",
    "michael moritz": "Enterprise, Consumer",
    "doug leone": "Enterprise, Consumer",
    "roelof botha": "Enterprise, Consumer, Fintech",
    "alfred lin": "Enterprise, Consumer",
    "jeff jordan": "Consumer, Marketplace, E-commerce",
    "satya patel": "Enterprise, Consumer",
    "manu kumar": "Enterprise, Consumer, AI",
    "semil shah": "Enterprise, Consumer",
    "hunter walk": "Consumer, Enterprise",
    "charles hudson": "Consumer, Enterprise",
    "lo toney": "Enterprise, Consumer",
    "arlan hamilton": "Consumer, Enterprise, SaaS",
    "kirsten green": "Consumer, DTC, Retail, E-commerce",
    "ann miura-ko": "Enterprise, Consumer",
    "aileen lee": "Enterprise, Consumer, AI",
    "jenny lee": "Enterprise, Consumer",
    "hans tung": "Enterprise, Consumer, E-commerce",
    "jeff bezos": "Consumer, Enterprise, Space, AI",
    "elon musk": "AI, Space, Clean Tech, Enterprise",
    "mark cuban": "Consumer, Enterprise, Healthcare",
    "ashton kutcher": "Consumer, Enterprise, Media",
    "robert downey jr": "Sustainability, Clean Tech",
    "will smith": "Consumer, Media, Entertainment",
    "jay-z": "Consumer, Cannabis, Media, Entertainment",
    "serena williams": "Consumer, Enterprise",
    "steph curry": "Consumer, Enterprise",
    "kevin durant": "Consumer, Enterprise, Media",
    "david sacks": "Enterprise, Consumer, Fintech, Crypto",
    "chamath palihapitiya": "Enterprise, Consumer, Healthcare",
    "eli broverman": "Fintech, Financial Services",
    "max levchin": "Fintech, Consumer",
    "jack dorsey": "Fintech, Consumer, Crypto",
    "brian armstrong": "Crypto, Fintech",
    "balaji srinivasan": "Crypto, Enterprise, Healthcare",
    "vitalik buterin": "Crypto, Blockchain, Web3",
    "joe lonsdale": "Enterprise, Deep Tech, Healthcare, Defense",
    "palmer luckey": "Defense, VR/AR",
    "trae stephens": "Defense, Enterprise, Deep Tech",
    "steve chen": "Consumer, Media, Video",
    "chad hurley": "Consumer, Media, Video",
    "ev williams": "Consumer, Media, Publishing",
    "biz stone": "Consumer, Social, Media",
    "kevin systrom": "Consumer, Social, Photography",
    "brian chesky": "Consumer, Travel, Marketplace",
    "drew houston": "Enterprise, Consumer, Cloud",
    "daniel ek": "Consumer, Music, Media",
    "patrick collison": "Fintech, Enterprise, SaaS",
    "john collison": "Fintech, Enterprise, SaaS",
    "tobi lutke": "E-commerce, Consumer, Enterprise",
    "stewart butterfield": "Enterprise, SaaS, Collaboration",
}

# ── Keyword patterns for fund-name inference ────────────────────────────────
KEYWORD_RULES = [
    # (pattern, sector_string)
    (re.compile(r'\b(health|bio|life\s*sci|genom|medic|pharma|therapeut|oncolog)\b', re.I),
     "Healthcare, Life Sciences, Biotech"),
    (re.compile(r'\b(ai\b|artificial\s*intell|machine\s*learn|deep\s*learn)\b', re.I),
     "AI, Machine Learning"),
    (re.compile(r'\bdata\b', re.I),
     "AI, Data"),
    (re.compile(r'\b(fintech|fin\s*vc|financial\s*tech)\b', re.I),
     "Fintech, Financial Services"),
    (re.compile(r'\b(consumer|brand[s]?|dtc|direct.to.consumer|retail)\b', re.I),
     "Consumer, DTC, Retail"),
    (re.compile(r'\b(clean\s*tech|climate|clean\s*energy|green|sustainab|carbon|decarboni|carbon)\b', re.I),
     "Clean Tech, Sustainability"),
    (re.compile(r'\b(energy|solar|wind\s*power|battery|electri[cf])\b', re.I),
     "Clean Tech, Energy"),
    (re.compile(r'\b(media|entertainment|content|stream|broadcast|film|music|tv)\b', re.I),
     "Media, Entertainment, Digital Media"),
    (re.compile(r'\b(real\s*estate|prop\s*tech|property|housing)\b', re.I),
     "Real Estate, PropTech"),
    (re.compile(r'\b(cyber|security)\b', re.I),
     "Cybersecurity"),
    (re.compile(r'\b(food|agri|agtech|ag\s*tech|farm)\b', re.I),
     "Food & Beverage, AgTech"),
    (re.compile(r'\b(edtech|education|ed\s*tech|learn)\b', re.I),
     "Education, EdTech"),
    (re.compile(r'\b(social|community)\b', re.I),
     "Social, Community"),
    (re.compile(r'\b(creator)\b', re.I),
     "Creator Economy"),
    (re.compile(r'\b(space|aero|rocket|satellite|orbit)\b', re.I),
     "Aerospace, Space"),
    (re.compile(r'\b(robot|automat)\b', re.I),
     "Robotics, Automation"),
    (re.compile(r'\b(crypto|blockchain|web3|defi|nft|token)\b', re.I),
     "Crypto, Blockchain, Web3"),
    (re.compile(r'\b(mobility|transport|auto|vehicle|ev\b|fleet)\b', re.I),
     "Mobility, Transportation"),
    (re.compile(r'\b(logistics|supply\s*chain|freight|shipping)\b', re.I),
     "Logistics, Supply Chain"),
    (re.compile(r'\b(insur)\b', re.I),
     "Insurance, InsurTech"),
    (re.compile(r'\b(gaming|game|esport)\b', re.I),
     "Gaming, Esports"),
    (re.compile(r'\b(femtech|women.s\s*health)\b', re.I),
     "FemTech, Women's Health"),
    (re.compile(r'\b(cannabis|hemp|cbd)\b', re.I),
     "Cannabis"),
    (re.compile(r'\b(defense|defence|military)\b', re.I),
     "Defense, National Security"),
    (re.compile(r'\b(hardware|device|sensor|chip|semiconductor)\b', re.I),
     "Hardware, Devices"),
    (re.compile(r'\b(saas|software)\b', re.I),
     "SaaS, Software"),
    (re.compile(r'\b(construction|infra|infrastructure)\b', re.I),
     "Infrastructure, Construction"),
    (re.compile(r'\b(travel|hotel|hospitality|tourism)\b', re.I),
     "Travel, Hospitality"),
    (re.compile(r'\b(mental\s*health|wellness|mindful)\b', re.I),
     "Mental Health, Wellness"),
    (re.compile(r'\b(pet|animal|vet)\b', re.I),
     "Pet, Animal Health"),
    (re.compile(r'\b(sport|fitness|athletic)\b', re.I),
     "Sports, Fitness"),
    (re.compile(r'\b(fashion|apparel|beauty|cosmetic)\b', re.I),
     "Fashion, Beauty"),
    (re.compile(r'\b(legal|law\s*tech)\b', re.I),
     "Legal, LegalTech"),
    (re.compile(r'\b(hr\s*tech|human\s*resource|talent|recruit)\b', re.I),
     "HR Tech, Talent"),
    (re.compile(r'\b(marketing|adtech|ad\s*tech|advertising)\b', re.I),
     "Marketing, AdTech"),
]

# Words that are too generic in fund names to infer sector — skip these
SKIP_GENERIC = re.compile(
    r'^(capital|ventures?|partners?|group|fund|management|holdings|investment[s]?|'
    r'equity|llc|llp|inc|co|company|the|global|international|advisors?|associates?|'
    r'growth|labs?|studio[s]?|collective|alliance|network|first|new|next|one|two|'
    r'three|four|five|six|seven|eight|nine|ten|angel|angels?|vc)$',
    re.I
)


def normalize(s):
    """Lowercase, strip whitespace/quotes/newlines."""
    if not s:
        return ""
    return re.sub(r'\s+', ' ', s.replace('\n', ' ').replace('\r', ' ').replace('"', '').strip()).lower()


def lookup_fund(fund_raw):
    """Try to match fund name against known funds dict."""
    fund = normalize(fund_raw)
    if not fund:
        return None
    # Direct match
    if fund in KNOWN_FUNDS:
        return KNOWN_FUNDS[fund]
    # Try without trailing suffixes
    for suffix in [' ventures', ' capital', ' partners', ' fund', ' vc', ' group', ' management', ' llc', ' inc']:
        stripped = fund.rstrip()
        if fund.endswith(suffix):
            base = fund[:-len(suffix)].strip()
            if base in KNOWN_FUNDS:
                return KNOWN_FUNDS[base]
    # Try adding common suffixes
    for suffix in [' ventures', ' capital', ' partners']:
        augmented = fund + suffix
        if augmented in KNOWN_FUNDS:
            return KNOWN_FUNDS[augmented]
    return None


def lookup_investor(name_raw):
    """Try to match investor name against known investors dict."""
    name = normalize(name_raw)
    if not name:
        return None
    if name in KNOWN_INVESTORS:
        return KNOWN_INVESTORS[name]
    return None


def infer_from_keywords(fund_raw, name_raw):
    """Infer sector from fund name or investor name keywords."""
    # Combine fund + name for keyword search, but fund takes priority
    texts = []
    if fund_raw:
        texts.append(normalize(fund_raw))
    if name_raw:
        texts.append(normalize(name_raw))
    
    combined = ' '.join(texts)
    if not combined.strip():
        return None
    
    # Remove generic words to avoid false matches on "Capital", "Ventures" etc.
    words = combined.split()
    meaningful = [w for w in words if not SKIP_GENERIC.match(w)]
    meaningful_text = ' '.join(meaningful)
    
    if not meaningful_text.strip():
        return None
    
    # Collect all matching sectors
    sectors = []
    for pattern, sector_string in KEYWORD_RULES:
        if pattern.search(meaningful_text):
            sectors.append(sector_string)
    
    if sectors:
        # Deduplicate while preserving order
        seen = set()
        unique = []
        for s in sectors:
            for part in s.split(', '):
                if part not in seen:
                    seen.add(part)
                    unique.append(part)
        return ', '.join(unique)
    
    return None


def main():
    # Read CSV
    with open(INPUT, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Parse with csv module
    import io
    reader = csv.DictReader(io.StringIO(content))
    fieldnames = reader.fieldnames
    
    if SECTOR_COL not in fieldnames:
        print(f"ERROR: Column '{SECTOR_COL}' not found. Columns: {fieldnames}")
        sys.exit(1)
    
    rows = list(reader)
    total = len(rows)
    
    # Count initial state
    already_filled = sum(1 for r in rows if r.get(SECTOR_COL, '').strip())
    print(f"Total rows: {total}")
    print(f"Already have sector data: {already_filled} ({already_filled*100/total:.1f}%)")
    
    # Process empty sectors
    filled_by_fund_lookup = 0
    filled_by_investor_lookup = 0
    filled_by_keyword = 0
    
    for row in rows:
        existing = row.get(SECTOR_COL, '').strip()
        if existing:
            continue
        
        fund = row.get(FUND_COL, '') or ''
        name = row.get(NAME_COL, '') or ''
        
        # 1. Try fund lookup
        result = lookup_fund(fund)
        if result:
            row[SECTOR_COL] = result
            filled_by_fund_lookup += 1
            continue
        
        # 2. Try investor name lookup
        result = lookup_investor(name)
        if result:
            row[SECTOR_COL] = result
            filled_by_investor_lookup += 1
            continue
        
        # 3. Try keyword inference
        result = infer_from_keywords(fund, name)
        if result:
            row[SECTOR_COL] = result
            filled_by_keyword += 1
            continue
    
    # Count final state
    now_filled = sum(1 for r in rows if r.get(SECTOR_COL, '').strip())
    
    # Write output
    with open(OUTPUT, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\n=== RESULTS ===")
    print(f"Filled by fund lookup: {filled_by_fund_lookup}")
    print(f"Filled by investor lookup: {filled_by_investor_lookup}")
    print(f"Filled by keyword inference: {filled_by_keyword}")
    print(f"Total newly filled: {filled_by_fund_lookup + filled_by_investor_lookup + filled_by_keyword}")
    print(f"Total with sector data now: {now_filled} / {total} ({now_filled*100/total:.1f}%)")
    print(f"Still empty: {total - now_filled}")


if __name__ == '__main__':
    main()
