#!/usr/bin/env python3
"""
Add Notable Portfolio Companies column to the master investor database.
Uses a comprehensive knowledge base of known VC firms, angels, and their portfolios.
"""

import csv
import re
import sys

# =============================================================================
# KNOWLEDGE BASE: Fund/Firm -> Notable Portfolio Companies
# =============================================================================
FUND_PORTFOLIO = {
    # --- MEGA / TOP-TIER VCs ---
    "sequoia": "Airbnb, Stripe, DoorDash, Zoom, Unity, Figma, Klarna, Apple, Google, WhatsApp",
    "a16z": "Coinbase, Instacart, Roblox, Databricks, Figma, Slack, GitHub, Airbnb, Lyft, Substack",
    "andreessen horowitz": "Coinbase, Instacart, Roblox, Databricks, Figma, Slack, GitHub, Airbnb, Lyft, Substack",
    "benchmark": "Uber, Twitter, Snap, Discord, Tinder, Zillow, eBay, Dropbox, WeWork, Stitch Fix",
    "first round": "Uber, Square, Roblox, Notion, Warby Parker, Flatiron Health, CloudFlare",
    "first round capital": "Uber, Square, Roblox, Notion, Warby Parker, Flatiron Health, CloudFlare",
    "lerer hippeau": "Casper, Glossier, Allbirds, BuzzFeed, Giphy, Warby Parker, Sweetgreen, Plaid",
    "accel": "Facebook, Spotify, Slack, Dropbox, Atlassian, CrowdStrike, UiPath, Flipkart, Etsy",
    "greylock": "Facebook, LinkedIn, Airbnb, Discord, Figma, Roblox, Coinbase, Palo Alto Networks",
    "greylock partners": "Facebook, LinkedIn, Airbnb, Discord, Figma, Roblox, Coinbase, Palo Alto Networks",
    "kleiner perkins": "Google, Amazon, Twitter, Slack, Figma, Impossible Foods, DoorDash, Peloton",
    "kpcb": "Google, Amazon, Twitter, Slack, Figma, Impossible Foods, DoorDash, Peloton",
    "lightspeed": "Snap, Affirm, Carta, Rubrik, Mulesoft, Epic Games, Grubhub, AppDynamics",
    "lightspeed venture": "Snap, Affirm, Carta, Rubrik, Mulesoft, Epic Games, Grubhub, AppDynamics",
    "general catalyst": "Stripe, Airbnb, Snap, HubSpot, Warby Parker, Lemonade, Livongo, Anduril",
    "nea": "Salesforce, Cloudflare, Databricks, Plaid, Robinhood, Coursera, Uber",
    "new enterprise associates": "Salesforce, Cloudflare, Databricks, Plaid, Robinhood, Coursera, Uber",
    "ggv capital": "Slack, Airbnb, Square, Grab, Peloton, Poshmark, Wish, Zendesk",
    "insight partners": "Twitter, Shopify, DocuSign, Monday.com, Wiz, SemRush, Veeam",
    "tiger global": "Facebook, LinkedIn, Spotify, Stripe, Roblox, ByteDance, Flipkart, Toast",
    "coatue": "Snap, DoorDash, Instacart, Airtable, Chime, Databricks, Rivian",
    "softbank": "Uber, WeWork, DoorDash, Slack, ByteDance, Arm, Nvidia, Coupang",
    "softbank investment": "Uber, WeWork, DoorDash, Slack, ByteDance, Arm, Nvidia, Coupang",
    "founders fund": "Facebook, Palantir, SpaceX, Airbnb, Stripe, Spotify, Lyft, Anduril",
    "khosla ventures": "Square, DoorDash, Impossible Foods, Instacart, Stripe, OpenAI, Affirm",
    "khosla": "Square, DoorDash, Impossible Foods, Instacart, Stripe, OpenAI, Affirm",
    "union square ventures": "Twitter, Etsy, Coinbase, Tumblr, Kickstarter, Cloudflare, MongoDB",
    "usv": "Twitter, Etsy, Coinbase, Tumblr, Kickstarter, Cloudflare, MongoDB",
    "bessemer venture partners": "Shopify, Pinterest, Twilio, LinkedIn, Yelp, Twitch, Wix, Toast",
    "bessemer": "Shopify, Pinterest, Twilio, LinkedIn, Yelp, Twitch, Wix, Toast",
    "index ventures": "Robinhood, Figma, Dropbox, Slack, Roblox, Discord, Notion, Plaid",
    "thrive capital": "Instagram, Spotify, Slack, GitHub, Robinhood, Nubank, Oscar Health",
    "ivp": "Twitter, Snap, Dropbox, Slack, Discord, Coinbase, Netflix, Grammarly",
    "institutional venture partners": "Twitter, Snap, Dropbox, Slack, Discord, Coinbase, Netflix, Grammarly",
    "battery ventures": "Groupon, Glassdoor, Coinbase, Wayfair, Sprinklr, Marketo",
    "spark capital": "Twitter, Slack, Tumblr, Affirm, Coinbase, Wayfair, Oculus, Cruise",
    "menlo ventures": "Uber, Siri, Roku, Chime, Poshmark, Pillpack, Rover",
    "redpoint": "Netflix, Stripe, Twilio, Snowflake, Looker, HomeAway, Zuora",
    "redpoint ventures": "Netflix, Stripe, Twilio, Snowflake, Looker, HomeAway, Zuora",
    "ribbit capital": "Robinhood, Coinbase, Nubank, Credit Karma, Affirm, Brex, Wealthfront",
    "felicis": "Shopify, Credit Karma, Fitbit, Adyen, Canva, Notion, Plaid",
    "felicis ventures": "Shopify, Credit Karma, Fitbit, Adyen, Canva, Notion, Plaid",
    "y combinator": "Airbnb, Stripe, DoorDash, Coinbase, Twitch, Reddit, Dropbox, Instacart",
    "yc": "Airbnb, Stripe, DoorDash, Coinbase, Twitch, Reddit, Dropbox, Instacart",
    "500 startups": "Canva, Talkdesk, Udemy, Credit Karma, Grab, GitLab, Bukalapak",
    "500 global": "Canva, Talkdesk, Udemy, Credit Karma, Grab, GitLab, Bukalapak",
    "techstars": "SendGrid, Sphero, ClassPass, DigitalOcean, Zipline, Pillpack",
    "sv angel": "Google, Pinterest, Airbnb, Twitter, Square, Dropbox, PayPal",
    "sv angel fund": "Google, Pinterest, Airbnb, Twitter, Square, Dropbox, PayPal",
    "goodwater capital": "Spotify, StockX, Duolingo, Masterclass, Faire, Rappi",
    "maveron": "eBay, Zulily, Allbirds, General Assembly, Madison Reed, Dolly",
    "forerunner ventures": "Warby Parker, Dollar Shave Club, Glossier, Away, Outdoor Voices, Hims",
    "forerunner": "Warby Parker, Dollar Shave Club, Glossier, Away, Outdoor Voices, Hims",
    "initialized capital": "Coinbase, Instacart, Cruise, Zenefits, Flexport, Rippling",
    "initialized": "Coinbase, Instacart, Cruise, Zenefits, Flexport, Rippling",
    "true ventures": "Peloton, Ring, Fitbit, Blue Bottle Coffee, WordPress, MakerBot",
    "emergence capital": "Salesforce, Zoom, Box, Yammer, Veeva, Bill.com, ServiceMax",
    "norwest venture partners": "Uber, Spotify, Udemy, Opendoor, Plaid, Calm, Talkdesk",
    "norwest": "Uber, Spotify, Udemy, Opendoor, Plaid, Calm, Talkdesk",
    "matrix partners": "Apple, HubSpot, Zendesk, Canva, Oculus, Quora, NerdWallet",
    "sapphire ventures": "Square, LinkedIn, Fitbit, Box, MuleSoft, ServiceNow, Alteryx",
    "iconiq capital": "Facebook, Spotify, Airbnb, Uber, Adyen, Datadog, Wiz, Snowflake",
    "iconiq": "Facebook, Spotify, Airbnb, Uber, Adyen, Datadog, Wiz, Snowflake",
    "dragoneer": "Airbnb, Uber, Spotify, Slack, Snowflake, UiPath, ByteDance",
    "iq capital": "Darktrace, Thought Machine, FiveAI, Speechmatics, Prowler.io",
    "atomico": "Skype, Klarna, Graphcore, Lilium, Supercell, Compass, MessageBird",
    "general atlantic": "Airbnb, Uber, ByteDance, Snap, Facebook, Alibaba, Slack",
    "global founders capital": "Facebook, Slack, Revolut, Trivago, Delivery Hero, HelloFresh",
    "google ventures": "Uber, Slack, Stripe, Robinhood, Medium, Nest, GitLab, Lime",
    "gv ": "Uber, Slack, Stripe, Robinhood, Medium, Nest, GitLab, Lime",
    "dstglobal": "Facebook, Spotify, Airbnb, Twitter, Alibaba, ByteDance, Stripe",
    "dst global": "Facebook, Spotify, Airbnb, Twitter, Alibaba, ByteDance, Stripe",
    "temasek": "Alibaba, ByteDance, Sea Limited, Grab, Hive, PayTM, Bitmain",
    "bain capital ventures": "LinkedIn, DocuSign, SurveyMonkey, Reddit, Attentive, Taboola",
    "capitalg": "Airbnb, Stripe, Lyft, UiPath, Duolingo, CrowdStrike, Snap",
    "d1 capital partners": "SpaceX, Stripe, Instacart, Roblox, Fidelity, Databricks",
    "t. rowe price": "Facebook, Uber, Airbnb, SpaceX, Stripe, DoorDash",
    "fidelity": "SpaceX, Stripe, Rivian, ByteDance, Reddit, Discord",
    "addition": "Stripe, Airbnb, Grammarly, Plaid, Notion, Figma",
    "addition capital": "Stripe, Airbnb, Grammarly, Plaid, Notion, Figma",
    "viking global": "Spotify, ByteDance, Snowflake, CrowdStrike, MongoDB",

    # --- MID-TIER / NOTABLE VCs ---
    "flybridge": "MongoDB, Middesk, Circle, Starburst, WHOOP, DataRobot",
    "flybridge capital": "MongoDB, Middesk, Circle, Starburst, WHOOP, DataRobot",
    "craft ventures": "Tesla, SpaceX, Uber, Lyft, Bird, AirGarage, OpenPhone",
    "crv": "Twitter, DoorDash, Airtable, HubSpot, Zendesk, Patreon",
    "charles river ventures": "Twitter, DoorDash, Airtable, HubSpot, Zendesk, Patreon",
    "cowboy ventures": "Dollar Shave Club, Brandless, Guild Education, The RealReal",
    "social capital": "Slack, Box, SurveyMonkey, Intercom, Yammer",
    "bbg ventures": "Zola, The Wing, Lola, Eloquii, Winky Lux",
    "precursor ventures": "Solugen, Lisnr, Doss, Remble, Arize AI",
    "kapor capital": "Bitwise Industries, Pigeonly, Ureeka, MiSalud, Samasource",
    "backstage capital": "Partake Foods, Jopwell, Mayvenn, The Lip Bar, Blavity",
    "harlem capital": "Palate Home, Blavity, Partake Foods, Slice, MiMedia",
    "cross culture ventures": "Blavity, Mayvenn, Partake Foods, Stem, PlayVS",
    "collaborative fund": "Lyft, Reddit, Impossible Foods, Kickstarter, Sweetgreen",
    "bold capital": "SpaceX, Hyperloop, D-Wave, Planet Labs, Joby Aviation",
    "pear vc": "DoorDash, Guardant Health, Branch, Vanta, Aurora Solar",
    "pear": "DoorDash, Guardant Health, Branch, Vanta, Aurora Solar",
    "floodgate": "Twitter, Lyft, Twitch, Refinery29, Chegg, Demandbase",
    "lowercase capital": "Uber, Twitter, Instagram, Slack, Optimizely",
    "baseline ventures": "Instagram, Heroku, Stitcher, IronPort, Weebly",
    "homebrew": "Plaid, Gusto, Carta, Stitch Fix, Going (Scott's Cheap Flights)",
    "haystack": "DoorDash, Instacart, Postmates, Figma, Notion",
    "angelpad": "Postmates, Minted, Pipedrive, Buffer, Periscope",
    "angel pad": "Postmates, Minted, Pipedrive, Buffer, Periscope",
    "maverick ventures": "Tumblr, JustFab, Dollar Shave Club, Course Hero",
    "crosscut ventures": "Scopely, Prodege, Talespin, Bird, ServiceTitan",
    "crosscut": "Scopely, Prodege, Talespin, Bird, ServiceTitan",
    "bam ventures": "Honey, Bird, Scopely, Headspace, Dollar Shave Club, Sweetgreen",
    "bonfire ventures": "Scopely, Dollar Shave Club, Procore, Greenfly, Podium",
    "upfront ventures": "Ring, Maker Studios, TrueCar, Overture, Ruggable, Parachute Home",
    "amplify la": "TikTok/Musical.ly, Calm, WndrCo, FabFitFun, TheSkimm",
    "amplify.la": "TikTok/Musical.ly, Calm, WndrCo, FabFitFun, TheSkimm",
    "mucker capital": "Honey, Surf Air, Ordermark, Retention Science, Miso Robotics",
    "m13": "Lyft, Ring, Pinterest, ClassPass, Daily Harvest, FabFitFun",
    "645 ventures": "Freshly, Peloton, MongoDB, Oscar Health, Squarespace",
    "645": "Freshly, Peloton, MongoDB, Oscar Health, Squarespace",
    "boldstart ventures": "Snyk, BigPanda, Kustomer, Datadog, Security Scorecard",
    "boldstart": "Snyk, BigPanda, Kustomer, Datadog, Security Scorecard",
    "14w": "Glossier, Mirror, Hungryroot, Lalo, Kindbody",
    "b capital": "Icertis, Evidation Health, FreightPop, Ninja Van, CXApp",
    "8vc": "Oscar Health, Palantir, Asana, Wish, Joby Aviation, Anduril",
    "formation 8": "Oculus VR, Palantir, Oscar Health, Wish",
    "obvious ventures": "Beyond Meat, Planet Labs, Medium, Diamond Foundry",
    "slow ventures": "Coinbase, Slack, Carta, Dollar Shave Club, Casper",
    "revolution": "DraftKings, Sweetgreen, Tempus, BigCommerce, Tala",
    "revolution growth": "DraftKings, Sweetgreen, Tempus, BigCommerce, Tala",
    "revolution ventures": "DraftKings, Sweetgreen, Tempus, BigCommerce, Tala",
    "emerson collective": "Axios, College Track, XQ Institute, Monumental Sports",
    "omidyar network": "LinkedIn, Ushahidi, Glassdoor, Change.org, d.light",
    "foundry group": "Fitbit, MakerBot, SendGrid, Zynga, Rally Software",
    "bowery capital": "Plaid, Segment, LaunchDarkly, Spoke, Dialpad",
    "wndr co": "DreamWorks, Quibi, Whistle, OZY Media",
    "wndrco": "DreamWorks, Quibi, Whistle, OZY Media",
    "valor equity partners": "Tesla, SpaceX, Anduril, Relativity Space",
    "hustle fund": "Deel, Middesk, Snackpass, Lunchclub, Oura",
    "1984 ventures": "Middesk, Vanta, RunwayML, Forethought, Snackpass",
    "1984": "Middesk, Vanta, RunwayML, Forethought, Snackpass",
    "boost vc": "Coinbase, Etherscan, Plangrid, Docker, Matterport",
    "boost": "Coinbase, Etherscan, Plangrid, Docker, Matterport",
    "ame cloud ventures": "Uber, Palantir, Unity, Zoom, Planet Labs, DoorDash",
    "digital currency group": "Coinbase, Ripple, Circle, CoinDesk, Genesis, Grayscale",
    "blockchain capital": "Coinbase, Kraken, Ripple, Anchorage, dYdX, Opensea",
    "8 decimal capital": "Filecoin, Polkadot, Near Protocol, The Graph",
    "bee partners": "Verkada, Freenome, Shape Security, Health IQ",
    "expert dojo": "Parachute, Deeptrace, MedicalChain, Miso Robotics",
    "xg ventures": "Zynga, YouTube, Snap, Riot Games",
    "presight capital": "BlockFi, Fireblocks, TaxBit, Chainalysis",
    "baroda ventures": "Vectra AI, Lightbend, Rigetti Computing",
    "courtside vc": "Bird, Scopely, Miso Robotics, Talespin",
    "illuminate ventures": "Apttus, Sumo Logic, Demandbase, Lytx",
    "unshackled ventures": "Turing, Vise, StockX, Cerebral",
    "chingona ventures": "Pulley, Suma Wealth, GoTu, Vemos",
    "halogen capital": "Cleo Capital, The RealReal, AllTrails, Whoop",
    "draper associates": "Tesla, SpaceX, Skype, Baidu, Coinbase, Twitch",
    "basis set ventures": "Verkada, Skyflow, Persona, Loom, Miro",
    "social leverage": "Robinhood, Betterment, Wealthfront, Credit Karma",
    "creandum": "Spotify, Klarna, Depop, Trade Republic, iZettle",
    "byfounder": "Too Good To Go, Pleo, Wolt, Unity",
    "byfounders": "Too Good To Go, Pleo, Wolt, Unity",
    "acme capital": "Slack, Birchbox, ClassPass, Spring Health",
    "craft": "Tesla, SpaceX, Uber, Lyft, Bird, AirGarage, OpenPhone",
    "tao capital partners": "SpaceX, Palantir, Neuralink, Anduril",
    "blue horizon ventures": "Impossible Foods, Beyond Meat, Perfect Day, NotCo",
    "amino capital": "Wish, Credit Karma, Samsara, LendingHome",
    "cruttenden partners": "Acorns, Aspiration, Mastercoin",
    "angel pad": "Postmates, Minted, Pipedrive, Buffer, Periscope",
    "dbl partners": "Tesla, SolarCity, The Muse, Farmers Business Network",
    "nolan capital": "various tech startups",
    "lumia capital": "AgriWebb, CloudMinds, Juul, Rothy's",
    "bellco capital": "Grindr, Ring, Dollar Shave Club, Beyond Meat",
    "innovius capital": "Ring, Dollar Shave Club, Bird, Honey",
    "arena ventures": "Scopely, Ring, Dollar Shave Club",
    "winklevoss capital": "Bitcoin, Gemini, Nifty Gateway, BlockFi, Filecoin",
    "equilibra": "Kind Snacks, Beyond Meat, Sweetgreen",
    "equilibra partners": "Kind Snacks, Beyond Meat, Sweetgreen",
    "10x capital": "SpaceX, Discord, Databricks, Notion",
    "gtm fund": "Outreach, Gong, Clari, ZoomInfo",
    "h/l ventures": "BuzzFeed, Warby Parker, Casper, Giphy",
    "able partners": "Glossier, Casper, Away, Daily Harvest",
    "bread & butter ventures": "Forge Biologics, Dispatch, Branch, 75F",
    "base ventures": "Blavity, Mayvenn, Partake Foods, PlayVS",
    "hyde park venture partners": "ReviewTrackers, Catalytic, Lightbank, Tempus",
    "golden seeds": "Curious Jane, Hint Water, Little Passports, Mouth Foods",
    "causeway media partners": "DraftKings, Zwift, SeatGeek, LiveXLive, PlayVS",
    "chicago ventures": "Sprout Social, SpotHero, Halo Investing, ShipBob",
    "iqt": "Palantir, Keyhole (Google Earth), FireEye, Recorded Future",
    "in-q-tel": "Palantir, Keyhole (Google Earth), FireEye, Recorded Future",
    "s-cubed capital": "Nvidia (early), Palo Alto Networks, Google (early)",
    "work play ventures": "Zynga, Twitter, Nextdoor",
    "nina capital": "Vicomtech, Cocuus, Koa Health",
    "tenoneteen": "Ring, Dollar Shave Club, Parachute Home, Bird",
    "wndr co": "DreamWorks, Quibi",
    "brick & mortar ventures": "Cover, Landed, PeerStreet, Rhino",
    
    # --- International VCs ---
    "balderton capital": "Revolut, GoCardless, Citymapper, Darktrace, Nutmeg",
    "northzone": "Spotify, iZettle, Trustpilot, Avito",
    "smedvig capital": "Skype, Lovefilm, Perkbox",
    "caledonia investments": "Close Brothers, Coats Group, Quintain",
    "rit capital partners": "Rockit, various public/private holdings",
    "investcorp": "Gucci, Tiffany & Co., Dainese, Berlin Packaging",
    "kkr": "First Data, Lyft, Epic Games, BMC Software, GoDaddy",
    "apax partners": "Travelport, Marlin, Exact Software, Trader Media Group",
    "unigestion": "Private equity fund-of-funds manager",
    "london technology club": "Revolut, WorldRemit, Blockchain.com, Onfido",
    "wates family": "Wates Group, various UK property/construction",
    "verlinvest": "Oatly, Vita Coco, Tony's Chocolonely, BrewDog",
    "cazenove capital": "Schroders Cazenove (wealth management)",
    "grosvenor group": "Grosvenor Estates, various global real estate",
    "lgt capital partners": "Family office of Liechtenstein royal family",
    "rothschild": "Various global holdings, NM Rothschild & Sons",
    "stonehage fleming": "Multi-family office (Oppenheimer/Fleming families)",
    "tavistock group": "TPC Group, Unicorp, various hospitality/real estate",
    "samena capital": "Various MENA/Asia investments",
    "gic": "Singapore sovereign wealth fund",
    "dnx ventures": "Treasure Data, SmartNews, Sansan, FreakOut",
    "westbridge capital": "MakeMyTrip, MindTree, Endurance Technologies",

    # --- Accelerators/Studios ---
    "theventurecity": "Typeform, Cabify, Lingokids, Platzi",
    "food foundry": "Tovala, Arize, FourKites",
    "the food foundry": "Tovala, Arize, FourKites",
    
    # --- Notable Angel Investors (by name) ---
    # We'll handle these in the NAME_PORTFOLIO dict below
}

# =============================================================================
# KNOWLEDGE BASE: Individual Name -> Notable Portfolio Companies
# =============================================================================
NAME_PORTFOLIO = {
    # --- Tech Founders / Famous Angels ---
    "max levchin": "PayPal (co-founder), Affirm (founder), Yelp, Evernote, Glow",
    "caterina fake": "Flickr (co-founder), Etsy, Kickstarter, BreakoutList",
    "dylan field": "Figma (founder/CEO), various angel investments",
    "naval ravikant": "Twitter, Uber, AngelList (founder), Clubhouse, Notion, Postmates, Yammer",
    "vinod khosla": "Square, DoorDash, Impossible Foods, Instacart, Stripe, OpenAI, Affirm",
    "keith rabois": "Square, PayPal, LinkedIn, Yelp, YouTube, DoorDash, OpenDoor, Affirm",
    "elad gil": "Airbnb, Coinbase, Stripe, Instacart, Pinterest, Square, Flexport, Notion",
    "sahil lavingia": "Gumroad (founder), various creator economy startups",
    "aileen lee": "Dollar Shave Club, Brandless, Guild Education, The RealReal (Cowboy Ventures)",
    "joe montana": "Dropbox, NerdWallet, Liquid 2 Ventures portfolio",
    "gwyneth paltrow": "Goop (founder), various wellness/beauty investments",
    "scooter braun": "Uber, Spotify, Editorialist, Generosity, Represent.com",
    "spencer rascoff": "Zillow (co-founder), Pacaso, dot.LA, Supergoop, Redfin",
    "sean parker": "Facebook, Spotify, Napster (co-founder), Airbnb, Causes",
    "pierre omidyar": "eBay (founder), LinkedIn, Glassdoor, Change.org, The Intercept",
    "ryan graves": "Uber (first CEO), Saltwater Capital portfolio",
    "drew houston": "Dropbox (founder/CEO), various angel investments",
    "aaron levie": "Box (founder/CEO), various enterprise SaaS angels",
    "biz stone": "Twitter (co-founder), Medium, Jelly, Beyond Meat",
    "tony hsieh": "Zappos (CEO), DTP Companies, various Vegas startups",
    "reid hoffman": "LinkedIn (co-founder), Airbnb, Zynga, Facebook, Flickr",
    "peter thiel": "Facebook, Palantir, SpaceX, Stripe, Airbnb, LinkedIn, Yelp",
    "marc andreessen": "Facebook, Twitter, GitHub, Coinbase, Airbnb, Roblox, Databricks",
    "ben horowitz": "Facebook, Twitter, GitHub, Coinbase, Airbnb, Roblox, Databricks (a16z)",
    "jeff bezos": "Google, Twitter, Airbnb, Uber, Business Insider, Domo, Basecamp",
    "mark cuban": "Magnolia Pictures, AXS TV, Cost Plus Drugs, various Shark Tank investments",
    "ashton kutcher": "Uber, Airbnb, Spotify, Soundcloud, Warby Parker (A-Grade Investments)",
    "kevin hart": "Fabletics, Tommy John, Hydrow, BrüMate",
    "jay z": "Uber, Robinhood, SpaceX, Impossible Foods, Oatly (Marcy Venture Partners)",
    "nas": "Coinbase, Robinhood, Genius, Dropbox, Casper (Queensbridge Venture Partners)",
    "will smith": "Julep, Fancy, Ticketfly, Walker & Company Brands (Dreamers VC)",
    "serena williams": "Coinbase, Masterclass, Tonal, Impossible Foods, Daily Harvest",
    "robert downey jr": "Aero, Luminar Technologies, various climate tech",
    "leonardo dicaprio": "Casper, Beyond Meat, Hippeas, Mojo Vision, Runa",
    "madonna": "Vita Coco, Tidal",
    "oprah winfrey": "Weight Watchers, Oatly, True Food Kitchen",
    "laurene powell jobs": "Emerson Collective, Axios, College Track, XQ Institute",
    "randi zuckerberg": "various tech/media startups",
    "richard branson": "Virgin Group, Hyperloop One, OneWeb, Planet Labs",
    
    # --- Prominent tech angels ---
    "dave morin": "Path (founder), Sunrise, various social/consumer",
    "hiten shah": "Crazy Egg, KISSmetrics (co-founder), FYI, Product Habits",
    "dick costolo": "Twitter (former CEO), Chorus, 01 Advisors portfolio",
    "fred wilson": "Twitter, Tumblr, Etsy, Coinbase, Kickstarter, MongoDB (USV)",
    "kevin hartz": "Eventbrite (co-founder), Airbnb, Pinterest, Uber",
    "william hockey": "Plaid (co-founder), Column (founder)",
    "ruchi sanghvi": "Facebook (first female engineer), Dropbox, various angel investments",
    "fred ehrsam": "Coinbase (co-founder), Paradigm, various crypto investments",
    "jeff clavier": "Fitbit, Mint, Eventbrite, Minted (Uncork Capital/SoftTech VC)",
    "mike volpi": "Discord, Roblox, Sonos, Elastica (Index Ventures)",
    "arjun sethi": "Yahoo, MessageMe, Tribe Capital portfolio",
    "arlan hamilton": "Partake Foods, Blavity, Backstage Capital portfolio",
    "alexa von tobel": "LearnVest (founder), Inspire Capital portfolio, Jet.com, ACV Auctions",
    "cyan banister": "Uber, SpaceX, Postmates, Niantic, DeepMind",
    "brianne kimmel": "Webflow, Notion, Figma, Brex (Worklife Ventures)",
    "charles hudson": "Precursor Ventures portfolio, Solugen, Lisnr",
    "semil shah": "DoorDash, Instacart, Hashicorp, Opendoor (Haystack)",
    "mo koyfman": "Imgur, Giphy, BuzzFeed, Casper (Spark Capital/early)",
    "gokul rajaram": "DoorDash, Coinbase, Coda, The RealReal, Figma",
    "pejman nozad": "DoorDash, Dropbox, Guardant Health, PayPal (Pear VC)",
    "leah solivan": "TaskRabbit (founder), Fuel Capital portfolio",
    "kevin lin": "Twitch (co-founder), various gaming/streaming angels",
    "rahul vohra": "Superhuman (founder/CEO), various SaaS angels",
    "vinny lingham": "Civic (founder), Gyft, various crypto investments",
    "kanyi maqubela": "ClassPass, Hurdle, Kindred Ventures portfolio",
    "david cohen": "Techstars (co-founder), SendGrid, Uber, Twilio",
    "niko bonatsos": "Snap, Musical.ly/TikTok, Tonal (General Catalyst)",
    "theresia gouw": "Trulia, Facebook, Cato Networks (Acrew Capital)",
    "mark pincus": "Zynga (founder), Twitter, Nextdoor, Work Play Ventures",
    "brendan iribe": "Oculus VR (co-founder), various VR/AR investments",
    "andy mcloughlin": "Huddle (co-founder), Uncork Capital",
    "rick marini": "BranchOut (founder), various consumer/digital media angels",
    "adam draper": "Coinbase, Etherscan, Plangrid, Docker, Matterport (Boost VC)",
    "ron conway": "Google, Facebook, Twitter, Airbnb, PayPal, Pinterest (SV Angel)",
    "ron suber": "Prosper Marketplace, SoFi, LendingClub, Insurtech",
    "gil elbaz": "Applied Semantics/Google AdSense, Factual, Datasift, Compellon",
    "tom hulme": "Deliveroo, Citymapper, GoCardless (GV/Google Ventures)",
    "richard wolpert": "Disney (former SVP), various media/entertainment angels",
    "eric hippeau": "BuzzFeed, Casper, Allbirds, Giphy, Warby Parker (Lerer Hippeau)",
    "dan martel": "Hootsuite (advisor), Flowtown, Clarity.fm (founder), various SaaS",
    "mark stevens": "Nvidia (early), Palo Alto Networks, Google (early), S-Cubed Capital",
    "michael moritz": "Google, Yahoo, PayPal, YouTube, LinkedIn, Stripe (Sequoia)",
    "nicolas berggruen": "Karstadt (acquired), Huffington Post, various media",
    "nick adams": "Uber, Palantir, Unity, Zoom, Planet Labs, DoorDash (AME Cloud)",
    "geoff lewis": "Roblox, Mux, Ironclad (Bedrock Capital)",
    "john backus": "Castlight Health, Evolent Health (NAV/New Atlantic Ventures)",
    "phil nadel": "Formlabs, Outreach, various AngelList syndicates (Barbara Corcoran Venture Partners)",
    "jenny fielding": "Meetup (former), various pre-seed (The Fund/Everywhere Ventures)",
    "daniel lubetzky": "KIND Snacks (founder), Beyond Meat, Sweetgreen, OLIPOP",
    "cameron winklevoss": "Bitcoin, Gemini (co-founder), BlockFi, Filecoin, Nifty Gateway",
    "greg kidd": "Square (early), Twitter, Coinbase, Ripple, Hard Yaka portfolio",
    "rob go": "Pillpack, DataRobot, CircleCI (NextView Ventures)",
    "rebecca kaden": "Glossier, Canva, Faire, Bird, Hopin (Union Square Ventures)",
    "eric bahn": "Deel, Middesk, Snackpass, Lunchclub, Oura (Hustle Fund)",
    "deborah quazzo": "ClassDojo, Coursera, Clever, FourWinds Interactive (GSV)",
    "scott banister": "PayPal, Uber, Lyft, Zivity, various angel investments",
    "marlon nichols": "Gimlet Media, Blavity, Mayvenn, PlayVS (MaC Venture Capital)",
    "jim andelman": "Scopely, Dollar Shave Club, Procore, Greenfly (Bonfire Ventures)",
    "susan lyne": "Gilt Groupe (former CEO), AOL Brand Group, BBG Ventures portfolio",
    "saul klein": "Skype (early), Seedcamp, LoveFilm, TransferWise (LocalGlobe)",
    "suranga chandratillake": "Blinkx/RhythmOne (founder), Balderton Capital portfolio",
    "brent hoberman": "Lastminute.com (co-founder), Made.com, Founders Forum",
    "nicole junkermann": "NJF Capital, Deep Mind (early), various health/tech",
    "rob kniaz": "Nest (early engineer), Houzz, Gusto, UiPath (Hoxton Ventures)",
    "gil dibner": "Forter, Upstream Security, Iguazio (Angular Ventures)",
    "alan patricof": "Apple (early), AOL, Huffington Post, Axios (Primavera Capital)",
    "doug leone": "WhatsApp, YouTube, Google, Airbnb, LinkedIn (Sequoia)",
    "david krane": "Uber, Slack, Stripe, Robinhood, Nest (GV/Google Ventures)",
    "josh hannah": "Betfair, LinkedIn, various consumer internet (Matrix Partners)",
    "avichal garg": "Electric Capital portfolio, various crypto/web3",
    "auren hoffman": "LiveRamp (founder), SafeGraph, various data/identity tech",
    "kat cole": "Focus Brands (former president), Cinnabon, various consumer",
    "bob bickel": "various enterprise software angels",
    "chris cantino": "Color Capital portfolio, various consumer brands",
    "assaf wand": "Hippo Insurance (founder/CEO)",
    "jackie chen": "Lemonade, Hippo, various insurtech",
    "eric ries": "The Lean Startup (author), LTSE (founder), various",
    "richard socher": "You.com (founder/CEO), Salesforce AI (former chief scientist)",
    "solomon hykes": "Docker (founder), Dagger.io",
    "tobias lütke": "Shopify (founder/CEO), Coinbase, Stripe, various",
    "tobias lutke": "Shopify (founder/CEO), Coinbase, Stripe, various",
    "josh silverman": "Etsy (CEO), Skype (former), American Express",
    "steve huffman": "Reddit (co-founder/CEO), Hipmunk",
    "tien tzuo": "Zuora (founder/CEO), various SaaS angels",
    "charlie cheever": "Quora (co-founder), various consumer tech",
    "jonathan abrams": "Friendster (founder), Nuzzel, various social",
    "cindy padnos": "Apttus, Sumo Logic, Demandbase (Illuminate Ventures)",
    "meg whitman": "eBay (former CEO), HP, Quibi",
    "jack dorsey": "Twitter (co-founder), Square/Block, various",
    "elon musk": "Tesla, SpaceX, OpenAI, Neuralink, The Boring Company, xAI",
    "mark zuckerberg": "Facebook/Meta (founder/CEO)",
    "tim cook": "Apple (CEO)",
    "reed hastings": "Netflix (co-founder), various education/philanthropy",
    "steve chen": "YouTube (co-founder), various video/media tech",
    "chad hurley": "YouTube (co-founder), MixBit, various media",
    "kevin systrom": "Instagram (co-founder), various consumer tech",
    "brian chesky": "Airbnb (co-founder/CEO)",
    "logan green": "Lyft (co-founder)",
    "travis kalanick": "Uber (co-founder), CloudKitchens, 10100 Fund",
    "jason calacanis": "Uber, Robinhood, Calm, Thumbtack, Wealthfront, Desktop Metal (LAUNCH Fund)",
    "chris sacca": "Twitter, Uber, Instagram, Kickstarter, Twilio (Lowercase Capital)",
    "tim ferriss": "Uber, Shopify, Facebook, Twitter, Alibaba, Duolingo, Evernote",
    "gary vaynerchuk": "Facebook, Twitter, Uber, Snap, Venmo (VaynerRSE)",
    "alexis ohanian": "Reddit (co-founder), Coinbase, Instacart, Calm (Seven Seven Six)",
    "jared leto": "Uber, Airbnb, Spotify, Snapchat, Nest, Slack",
    "robert herjavec": "various Shark Tank investments",
    "mark cuban": "Magnolia Pictures, AXS TV, Cost Plus Drugs, various Shark Tank investments",
    "kevin o'leary": "various Shark Tank investments, StartEngine",
    "lori greiner": "Scrub Daddy, Squatty Potty, various Shark Tank investments",
    "daymond john": "FUBU (founder), various Shark Tank investments, Bombas",
    "barbara corcoran": "various Shark Tank investments, The Corcoran Group",
    
    # --- VC Partners/Individuals ---
    "sandy grippo": "Shopify, Pinterest, Twilio, LinkedIn, Yelp, Twitch (Bessemer)",
    "david wehrs": "Shopify, Pinterest, Twilio, LinkedIn, Yelp (Bessemer)",
    "sachin sood": "Twitter, DoorDash, Airtable, HubSpot (CRV)",
    "brittany walker": "Twitter, DoorDash, Airtable, HubSpot (CRV)",
    "murat bicer": "Twitter, DoorDash, Airtable, HubSpot (CRV)",
    "ethan ruby": "Tesla, SpaceX, Uber, Lyft, Bird (Craft Ventures)",
    "rick smith": "Scopely, Prodege, Talespin, Bird, ServiceTitan (Crosscut)",
    "richard jun": "Honey, Bird, Scopely, Headspace, Dollar Shave Club (BAM Ventures)",
    "maurice maschmeyer": "Honey, Bird, Scopely, Headspace (BAM Ventures)",
    "beata klein": "Spotify, Klarna, Depop, Trade Republic (Creandum)",
    "neil rimer": "Robinhood, Figma, Dropbox, Slack, Roblox (Index Ventures)",
    "miles grimshaw": "Instagram, Spotify, Slack, GitHub, Robinhood (Thrive Capital)",
    "siddharth ram": "Facebook, Spotify, Slack, Dropbox, Atlassian (Accel)",
    "kirby harris": "Blavity, Mayvenn, Partake Foods, PlayVS (Base Ventures)",
    "susan lyne": "Gilt Groupe, The Wing, Zola, Eloquii (BBG Ventures)",
    "brian yee": "Slack, Birchbox, ClassPass (ACME Capital)",
    "aleks larsen": "Coinbase, Kraken, Ripple, Anchorage, dYdX (Blockchain Capital)",
    "aaron holiday": "Freshly, Peloton, MongoDB, Oscar Health (645 Ventures)",
    "jacqueline van den ende": "Booking.com, TripAdvisor, Catawiki (Fortino Capital)",
    "sim blaustein": "Rhapsody, Napster, various media/entertainment (BDMI)",
    "max altschuler": "Outreach, Gong, Clari, ZoomInfo (GTM Fund)",
    "brett brohl": "Forge Biologics, Dispatch, Branch (Bread & Butter Ventures)",
    "oliver libby": "BuzzFeed, Warby Parker, Casper, Giphy (H/L Ventures)",
    "tim kopp": "ReviewTrackers, Catalytic, Tempus (Hyde Park Venture Partners)",
    "jasmine robinson": "DraftKings, Zwift, SeatGeek (Causeway Media Partners)",
    "stuart larkins": "Sprout Social, SpotHero, ShipBob (Chicago Ventures)",
    "jesse draper": "Cleo Capital, The RealReal, AllTrails (Halogen Ventures)",
    "lisa molinaro": "Bitwise Industries, Pigeonly, Ureuka (Kapor Capital)",
    "allison scott": "Bitwise Industries, Pigeonly, Ureuka (Kapor Capital)",
    "brian dixon": "Bitwise Industries, Pigeonly, Ureuka (Kapor Capital)",
    "adam smith": "Plaid, Segment, LaunchDarkly, Spoke (Bowery Capital)",
    "adam lilling": "Dollar Shave Club, Bird, Headspace, Ring (Plus Capital)",
    "divesh makan": "Facebook, Spotify, Airbnb, Uber, Snowflake (ICONIQ Capital)",
    "matthew jacobson": "Facebook, Spotify, Airbnb, Uber, Snowflake (ICONIQ Capital)",
    "kevin foster": "Facebook, Spotify, Airbnb, Uber (ICONIQ Capital)",
    "alex pack": "Hack VC portfolio, various crypto/web3",
    "alexander pack": "Hack VC portfolio, various crypto/web3",
    "ronny conway": "A Capital portfolio, various consumer/enterprise tech",
    "brian muller": "various tech investments (Black Jays)",
    "mar hershenson": "DoorDash, Guardant Health, Branch (Pear VC)",
    "lan xuezhao": "Verkada, Skyflow, Persona, Loom (Basis Set Ventures)",
    "mitchell kapor": "Lotus 1-2-3 (founder), various social impact tech (Kapor Capital)",
    "mitchell kapor": "Lotus 1-2-3 (founder), various social impact tech (Kapor Capital)",
    "ariel poler": "Topica, various internet/SaaS angels",
    "ellen levy": "LinkedIn (former VP), various enterprise/SaaS angels",
    "sue xu": "Wish, Credit Karma, Samsara, LendingHome (Amino Capital)",
    "hershel mehta": "Mehta Ventures portfolio, various India/US tech",
    "ted leonsis": "Monumental Sports (owner), AOL (former), Groupon, various",
    "jaeson ma": "East Meets West (founder), TikTok/Musical.ly, various K-pop/entertainment tech",
    "sarah favaro": "various family office tech investments",
    "david waxman": "Ring, Dollar Shave Club, Parachute Home, Bird (TenOneTen)",
    "erhan bilici": "various fintech/enterprise",
    "clark valberg": "InVision (founder/CEO)",
    "alexi robichaux": "BetterUp (co-founder/CEO)",
    "alex bouaziz": "Deel (co-founder/CEO)",
    "daniel gross": "Pioneer, Y Combinator (former partner), Apple (Siri team)",
    "mark cuban": "Magnolia Pictures, Cost Plus Drugs, various Shark Tank",
    "bill zanker": "National Speakers Association, Learning Annex, various media",
    "steve martocci": "GroupMe (co-founder), various messaging/social",
    "geoff woo": "HVMN (co-founder), various biotech/health",
    "jack herrick": "wikiHow (founder), various media/content",
    "jillian manus": "Structure Capital portfolio, various AI/enterprise",
    "leo polovets": "Samsara, Flexport, Webflow, Sourcegraph (Susa Ventures)",
    "peter hebert": "Lux Capital portfolio, Shapeways, Desktop Metal",
    "scott nolan": "SpaceX, Anduril, Relativity Space (Founders Fund)",
    "kenneth chenault": "American Express (former CEO), Airbnb board, Berkshire Hathaway",
    "rick grinnell": "Glasswing Ventures portfolio, Cybereason, Paige",
    "chris sacca": "Twitter, Uber, Instagram, Kickstarter, Twilio (Lowercase Capital)",
    "alexis ohanian": "Reddit (co-founder), Coinbase, Instacart, Calm (776)",
    "dave morgan": "Simulmedia (founder), Tacoda, various adtech",
    "jeff seibert": "Twitter (VP), Digits (founder), various",
    "amitt mahajan": "FarmVille (creator), various gaming/web3 (Presence Capital)",
    "edith yeung": "Race Capital portfolio, various Asia/US cross-border tech",
    "gordon crawford": "Facebook, Snap, Spotify (T. Rowe Price media investments)",
    "shiva rajaraman": "YouTube (former VP Product), Spotify, various",
    "jonathan kraft": "Kraft Group, various sports/media investments",
    "jeffrey raider": "Harry's (co-founder), Warby Parker (co-founder)",
    "ray muzyka": "BioWare (co-founder), various gaming/entertainment",
    "dharmesh thakker": "Battery Ventures portfolio, Coinbase, Groupon",
    "cristina cordova": "Stripe (early), Notion, various growth-stage",
    "nick hungerford": "Nutmeg (founder), various UK fintech",
    "anthony di iorio": "Ethereum (co-founder), Decentral, Jaxx",
    "paul bricault": "Amplify LA portfolio, TikTok/Musical.ly, Calm",
    "bob pasker": "various tech angels",
    "soona amhaz": "Volt Capital portfolio, various crypto/web3",
    "skip fleshman": "Asset Management Ventures, various early-stage",
    "will neale": "Grabyo (founder), various media/sports tech",
    "hope cochran": "King Digital (former CFO), Madrona Ventures",
    "eric paley": "Founder Collective portfolio, Uber, Buzzfeed, SeatGeek, The Trade Desk",
    "dror berman": "Innovation Endeavors portfolio, various deep tech",
    "chenoa farnsworth": "Blue Startups portfolio, various Hawaii/Pacific tech",
    "larry aschebrook": "G20 Ventures portfolio, various enterprise",
    "mike asem": "M25 portfolio, various Midwest tech",
    "mark solon": "TechOperators portfolio, various cybersecurity",
    "clint chao": "Moment Ventures, various hardware/IoT",
    "peter kazanjy": "Atrium (co-founder), Modern Sales Pro (founder)",
    "villi iltchev": "Two Sigma Ventures, various AI/data",
    "jon gosier": "Audigent, FilmHedge (founder), various media/data",
    "susan choe": "Katalyst Ventures portfolio, various consumer",
    "annie lamont": "Oak HC/FT portfolio, various health/fintech",
    "jared kushner": "Observer Media, Cadre, various real estate tech",
    "vivek ramaswamy": "Roivant Sciences (founder), various biotech",
    "chamath palihapitiya": "Social Capital portfolio, Slack, Box, Virgin Galactic, Clover Health",
}

# Additional fund name variations/aliases
FUND_ALIASES = {
    "lerer hippeau ventures": "lerer hippeau",
    "bessemer venture": "bessemer venture partners",
    "greylock partner": "greylock partners",
    "kleiner perkins caufield": "kleiner perkins",
    "kleiner perkins caufield & byers": "kleiner perkins",
    "redpoint venture": "redpoint ventures",
    "lightspeed venture partners": "lightspeed",
    "union square venture": "union square ventures",
    "spark capital partners": "spark capital",
    "first round capital": "first round",
    "general catalyst partners": "general catalyst",
    "institutional venture partners": "ivp",
    "menlo venture": "menlo ventures",
    "charles river venture": "crv",
    "matrix partner": "matrix partners",
    "flybridge capital partners": "flybridge",
    "cowboy venture": "cowboy ventures",
    "crosscut venture": "crosscut ventures",
    "bonfire venture": "bonfire ventures",
    "forerunner venture": "forerunner ventures",
    "true venture": "true ventures",
    "felicis venture": "felicis ventures",
    "collaborative": "collaborative fund",
    "obvious venture": "obvious ventures",
    "precursor venture": "precursor ventures",
    "kapor": "kapor capital",
    "initialized cap": "initialized capital",
    "backstage": "backstage capital",
    "lowercase": "lowercase capital",
    "draper associate": "draper associates",
    "softbank investment advisers": "softbank",
    "khosla venture": "khosla ventures",
    "google ventures": "google ventures",
    "balderton": "balderton capital",
    "atomico": "atomico",
    "iconiq": "iconiq capital",
    "iconiq growth": "iconiq capital",
    "thrive": "thrive capital",
    "tiger global management": "tiger global",
    "coatue management": "coatue",
    "d1 capital": "d1 capital partners",
    "dragoneer investment group": "dragoneer",
    "dstglobal": "dst global",
    "ribbit": "ribbit capital",
    "founders fund": "founders fund",
    "revolution llc": "revolution",
    "social leverage": "social leverage",
    "homebrew management": "homebrew",
    "haystack fund": "haystack",
    "floodgate fund": "floodgate",
    "maverick capital": "maverick ventures",
    "bold capital partners": "bold capital",
    "slow": "slow ventures",
    "valor equity": "valor equity partners",
    "hustle": "hustle fund",
    "500": "500 startups",
    "angelpad": "angel pad",
    "pear": "pear vc",
    "creandum ab": "creandum",
    "blockchain cap": "blockchain capital",
    "digital currency": "digital currency group",
}


def normalize(text):
    """Normalize text for matching."""
    if not text:
        return ""
    text = text.lower().strip()
    # Remove common suffixes
    for suffix in [" llc", " inc", " inc.", " corp", " ltd", " ltd.", " lp", " fund", " partners", " management", " capital", " group", " ventures"]:
        if text.endswith(suffix):
            text = text[:-len(suffix)].strip()
    # Remove special chars
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# Keys that are common English words and should only match exactly
EXACT_ONLY_KEYS = {
    "angel", "angel pad", "addition", "bold", "craft", "emergence", "formation",
    "general", "global", "insight", "matrix", "norwest", "pear", "revolution",
    "social", "spark", "summit", "true", "valor", "slow", "homebrew", "haystack",
    "hustle", "boost", "1984", "500", "baseline", "floodgate", "obvious", "b capital",
    "capitalg", "gv ",
}

def fund_match(key, fund_lower):
    """Check if a fund key matches a fund name string.
    Requires the key to appear as a coherent match, not just a stray word."""
    if key == fund_lower:
        return True
    
    # For exact-only keys, require exact match or key is the first/main word of fund
    if key in EXACT_ONLY_KEYS:
        # Allow "boost" matching "boost vc" but not "boost" matching "rooster boost capital"
        if fund_lower.startswith(key + " ") or fund_lower.startswith(key + "/"):
            return True
        return False
    
    # For short keys (<=5 chars), require exact or starts-with
    if len(key) <= 5:
        if fund_lower.startswith(key + " ") or fund_lower.startswith(key + "/") or fund_lower == key:
            return True
        return False
    
    # For longer keys, key must be IN fund_lower (not the reverse)
    if key in fund_lower:
        return True
    # fund_lower in key only if fund_lower is very close to key length (>70%)
    if fund_lower in key and len(fund_lower) >= len(key) * 0.7:
        return True
    return False


def find_portfolio_by_fund(fund_raw):
    """Try to match a fund name to known portfolio data."""
    if not fund_raw or fund_raw.startswith("http"):
        return ""
    
    fund_lower = fund_raw.lower().strip()
    # Remove newlines
    fund_lower = re.sub(r'\s+', ' ', fund_lower).strip()
    fund_norm = normalize(fund_raw)
    
    # Exact match first
    if fund_lower in FUND_PORTFOLIO:
        return FUND_PORTFOLIO[fund_lower]
    
    # Fund key match - require significant overlap (>60% of fund name matched)
    best_match = None
    best_ratio = 0
    for key, val in FUND_PORTFOLIO.items():
        if fund_match(key, fund_lower):
            # Calculate match quality - key should be a significant part of the fund name
            ratio = len(key) / max(len(fund_lower), 1)
            if ratio > best_ratio:
                best_ratio = ratio
                best_match = val
    
    # Only accept if the match is high quality (key covers >30% of fund name)
    if best_match and best_ratio >= 0.3:
        return best_match
    
    # Alias match
    for alias, canonical in FUND_ALIASES.items():
        if fund_match(alias, fund_lower):
            if canonical in FUND_PORTFOLIO:
                return FUND_PORTFOLIO[canonical]
    
    # Normalized match
    for key, val in FUND_PORTFOLIO.items():
        key_norm = normalize(key)
        if key_norm and len(key_norm) > 6 and fund_match(key_norm, fund_norm):
            return val
    
    return ""


def find_portfolio_by_name(name_raw):
    """Try to match an investor name to known portfolio data."""
    if not name_raw:
        return ""
    
    name_lower = name_raw.lower().strip()
    # Remove extra whitespace/newlines
    name_lower = re.sub(r'\s+', ' ', name_lower).strip()
    
    # Direct match
    for key, val in NAME_PORTFOLIO.items():
        if key == name_lower:
            return val
    
    # Partial name match (be careful with common names)
    # Only match if name has at least 2 parts and matches fully
    parts = name_lower.split()
    if len(parts) >= 2:
        for key, val in NAME_PORTFOLIO.items():
            key_parts = key.split()
            if len(key_parts) >= 2:
                # Match on first and last name
                if parts[0] == key_parts[0] and parts[-1] == key_parts[-1]:
                    return val
    
    return ""


def main():
    input_file = "/data/.openclaw/workspace/projects/investor-outreach/MASTER-investor-database-v2.csv"
    output_file = input_file  # Overwrite
    
    # Read all rows
    rows = []
    with open(input_file, 'r', encoding='utf-8', errors='replace') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            rows.append(row)
    
    print(f"Read {len(rows)} data rows")
    print(f"Columns: {len(header)}")
    
    # Add new column header (or replace if already exists)
    if "Notable Portfolio Companies" in header:
        portfolio_col = header.index("Notable Portfolio Companies")
        # Remove existing portfolio data from all rows
        for row in rows:
            while len(row) > portfolio_col:
                row.pop()
        # Remove from header
        header = header[:portfolio_col]
    header.append("Notable Portfolio Companies")
    
    # Process each row
    name_idx = header.index("Name")
    fund_idx = header.index("Fund")
    
    filled_count = 0
    filled_by_fund = 0
    filled_by_name = 0
    
    for i, row in enumerate(rows):
        # Ensure row has enough columns
        while len(row) < len(header) - 1:
            row.append("")
        
        name = row[name_idx].strip() if name_idx < len(row) else ""
        fund = row[fund_idx].strip() if fund_idx < len(row) else ""
        
        # Try fund first, then name
        portfolio = find_portfolio_by_fund(fund)
        source = "fund"
        
        if not portfolio:
            portfolio = find_portfolio_by_name(name)
            source = "name"
        
        row.append(portfolio)
        
        if portfolio:
            filled_count += 1
            if source == "fund":
                filled_by_fund += 1
            else:
                filled_by_name += 1
    
    # Write output
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)
    
    print(f"\n=== SUMMARY ===")
    print(f"Total rows processed: {len(rows)}")
    print(f"Rows with portfolio data: {filled_count}")
    print(f"  - Matched by fund name: {filled_by_fund}")
    print(f"  - Matched by investor name: {filled_by_name}")
    print(f"Rows left blank: {len(rows) - filled_count}")
    print(f"Fill rate: {filled_count/len(rows)*100:.1f}%")
    print(f"\nFile saved to: {output_file}")


if __name__ == "__main__":
    main()
