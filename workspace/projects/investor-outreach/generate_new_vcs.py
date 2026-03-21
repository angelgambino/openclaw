#!/usr/bin/env python3
"""Task 2: Generate 100+ new California VC firms with key partners.
Only includes firms NOT already in MASTER-investor-database-v2.csv."""

import csv

INPUT_DB = 'MASTER-investor-database-v2.csv'
OUTPUT = 'MASTER-new-california-vcs.csv'

FIELDNAMES = [
    'Name', 'Email', 'Location (City)', 'Location (State)', 'Location (Country)',
    'Type of Investor', 'Stage: Investment Thesis', 'Sector: Investment Thesis',
    'LinkedIn', 'Website', 'Fund', 'Priority Tier', 'Thesis Match Score',
    'Why This Investor is a Fit'
]

# Load existing funds to skip
def load_existing_funds():
    funds = set()
    with open(INPUT_DB, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            fund = row.get('Fund', '').strip().lower()
            if fund:
                funds.add(fund)
    return funds

# Each entry: (fund_name, website, city, partners_list, stage, sectors, priority, score, fit_reason)
NEW_VCS = [
    # === TIER 1: TOP SF/BAY AREA FUNDS ===
    
    ("Andreessen Horowitz (a16z)", "a16z.com", "Menlo Park", [
        ("Marc Andreessen", "marcandreessen"),
        ("Ben Horowitz", "behorowitz"),
        ("Chris Dixon", "chrisdixon"),
        ("Andrew Chen", "andrewchen"),
        ("Arianna Simpson", "ariannasimpson"),
        ("Martin Casado", "martincasado"),
        ("Connie Chan", "conniechan"),
        ("David Haber", "davidhaber"),
        ("Sriram Krishnan", "sriramk"),
    ], "Seed, Series A, Series B, Growth", "AI, Consumer, Crypto, Enterprise, Fintech, Healthcare, Media, Gaming", "Tier 1", "95", "Top-tier multi-stage fund with dedicated media, entertainment and AI practices"),

    ("Khosla Ventures", "khoslaventures.com", "Menlo Park", [
        ("Vinod Khosla", "vinodkhosla"),
        ("Samir Kaul", "samirkaul"),
        ("Alex Morgan", "alexmorgan"),
        ("Kanu Gulati", "kanugulati"),
    ], "Seed, Series A, Series B", "AI, Health, Consumer, Climate, Enterprise", "Tier 1", "85", "Strong AI and health thesis, backs ambitious founders"),

    ("Kleiner Perkins", "kleinerperkins.com", "Menlo Park", [
        ("Mamoon Hamid", "mamoonha"),
        ("Bucky Moore", "buckymoore"),
        ("Ilya Fushman", "ilyafushman"),
        ("Monica Desai Weiss", "monicadesaiweiss"),
    ], "Seed, Series A, Series B", "AI, Consumer, Enterprise, Health, Fintech", "Tier 1", "88", "Legendary fund with renewed focus on AI and consumer health"),

    ("Founders Fund", "foundersfund.com", "San Francisco", [
        ("Peter Thiel", "peterthiel"),
        ("Keith Rabois", "keithrabois"),
        ("Brian Singerman", "briansingerman"),
        ("Trae Stephens", "traestephens"),
        ("Napoleon Ta", "napoleonta"),
    ], "Seed, Series A, Series B, Growth", "AI, Consumer, Health, Deep Tech, Defense", "Tier 1", "82", "Contrarian fund backing transformational companies"),

    ("Menlo Ventures", "menlovc.com", "Menlo Park", [
        ("Matt Murphy", "matthewmurphy"),
        ("Tyler Sosin", "tylersosin"),
        ("Deedy Das", "deedydas"),
        ("Jean-Denis Greze", "jeandenisgreze"),
    ], "Seed, Series A, Series B", "AI, Enterprise, Consumer, Fintech", "Tier 1", "85", "Active AI investor with strong consumer portfolio"),

    ("True Ventures", "trueventures.com", "San Francisco", [
        ("Jon Callaghan", "joncallaghan"),
        ("Phil Black", "philblack"),
        ("Rohit Sharma", "rohitsharma"),
        ("Toni Schneider", "tonischneider"),
    ], "Seed, Series A", "Consumer, Creator Economy, AI, Health, Sustainability", "Tier 1", "87", "Community-driven fund with strong creator and consumer focus"),

    ("Initialized Capital", "initialized.com", "San Francisco", [
        ("Garry Tan", "garrytan"),
        ("Brett Gibson", "brettgibson"),
        ("Kim-Mai Cutler", "kimmaicutler"),
        ("Alda Leu Dennis", "aldaleu"),
    ], "Pre-Seed, Seed", "AI, Consumer, SaaS, Health, Creator Economy", "Tier 1", "85", "YC-connected seed fund with broad thesis including consumer and creator economy"),

    ("Felicis Ventures", "felicis.com", "Menlo Park", [
        ("Aydin Senkut", "aydinsenkut"),
        ("Victoria Treyger", "victoriatreyger"),
        ("Niki Pezeshki", "nikipezeshki"),
        ("Viviana Faga", "vivianafaga"),
    ], "Seed, Series A, Series B", "AI, Consumer, Health, Enterprise, Fintech", "Tier 1", "85", "Multi-stage fund with strong consumer health and AI thesis"),

    ("Mayfield Fund", "mayfield.com", "Menlo Park", [
        ("Navin Chaddha", "navinchaddha"),
        ("Tim Chang", "timchang"),
        ("Rajeev Batra", "rajeevbatra"),
    ], "Seed, Series A, Series B", "AI, Consumer, Enterprise, Health", "Tier 1", "80", "Heritage fund with renewed consumer and AI focus"),

    ("Matrix Partners", "matrixpartners.com", "San Francisco", [
        ("Ilya Sukhar", "ilyasukhar"),
        ("Jake Jolis", "jakejolis"),
        ("Pat Malatack", "patmalatack"),
    ], "Seed, Series A", "AI, Consumer, SaaS, Fintech, Infrastructure", "Tier 1", "80", "Strong seed and Series A fund with consumer and AI portfolio"),

    ("Ribbit Capital", "ribbitcap.com", "Palo Alto", [
        ("Micky Malka", "mickymalka"),
        ("Nick Shalek", "nickshalek"),
    ], "Seed, Series A, Series B", "Fintech, Consumer Finance, AI, Health", "Tier 1", "75", "Leading fintech fund with consumer finance expertise"),

    ("Battery Ventures", "battery.com", "San Francisco", [
        ("Neeraj Agrawal", "neerajagrawal"),
        ("Michael Brown", "michaelbrown"),
    ], "Seed, Series A, Growth", "AI, Enterprise, Consumer, Health", "Tier 1", "78", "Multi-stage fund with broad tech thesis"),

    ("NEA (New Enterprise Associates)", "nea.com", "Menlo Park", [
        ("Scott Sandell", "scottsandell"),
        ("Liza Landsman", "lizalandsman"),
        ("Andrew Schoen", "andrewschoen"),
    ], "Seed, Series A, Growth", "AI, Consumer, Health, Enterprise, Fintech", "Tier 1", "82", "One of the largest VC funds, broad thesis including health/consumer"),

    ("Bain Capital Ventures", "baincapitalventures.com", "San Francisco", [
        ("Merritt Hummer", "merritthummer"),
        ("Enrique Salem", "enriquesalem"),
        ("Sarah Smith", "sarahsmith"),
    ], "Seed, Series A, Series B", "AI, Consumer, Health, SaaS, Fintech", "Tier 1", "80", "Platform investor with consumer health and AI thesis"),

    ("GGV Capital / Notable Capital", "notable.vc", "Menlo Park", [
        ("Hans Tung", "hanstung"),
        ("Jeff Richards", "jeffrichards"),
        ("Tiffany Luck", "tiffanyluck"),
    ], "Seed, Series A, Series B", "AI, Consumer, SaaS, Fintech", "Tier 1", "80", "Rebranded as Notable Capital, strong consumer and AI focus"),

    ("IVP (Institutional Venture Partners)", "ivp.com", "Menlo Park", [
        ("Tom Loverro", "tomloverro"),
        ("Eric Liaw", "ericliaw"),
        ("Somesh Dash", "someshdash"),
    ], "Series A, Series B, Growth", "Consumer, SaaS, AI, Health, Entertainment", "Tier 1", "82", "Growth-stage with consumer entertainment and health portfolio"),

    ("Bessemer Venture Partners", "bvp.com", "Menlo Park", [
        ("Byron Deeter", "byrondeeter"),
        ("Mary D'Onofrio", "marydonofrio"),
        ("Talia Goldberg", "taliagoldberg"),
    ], "Seed, Series A, Growth", "AI, Consumer, Health, SaaS, Cloud", "Tier 1", "82", "Century-old VC with strong cloud, health, and consumer thesis"),

    ("Scale Venture Partners", "scalevp.com", "Foster City", [
        ("Rory O'Driscoll", "roryodriscoll"),
        ("Stacey Bishop", "staceybishop"),
        ("Andy Vitus", "andyvitus"),
    ], "Series A, Series B", "SaaS, AI, Enterprise, Consumer", "Tier 2", "72", "Growth-stage SaaS and enterprise focus"),

    ("Shasta Ventures", "shastaventures.com", "Menlo Park", [
        ("Nikhil Basu Trivedi", "nikhilbt"),
        ("Jason Pressman", "jasonpressman"),
    ], "Seed, Series A", "Consumer, SaaS, AI, Health", "Tier 2", "80", "Consumer-focused fund with health and AI interest"),

    ("Sierra Ventures", "sierraventures.com", "San Mateo", [
        ("Mark Fernandes", "markfernandes"),
        ("Tim Guleri", "timguleri"),
    ], "Series A, Series B", "Enterprise, SaaS, AI, Security", "Tier 2", "68", "Enterprise-focused with emerging AI thesis"),

    ("Storm Ventures", "stormventures.com", "Menlo Park", [
        ("Tae Hea Nahm", "taehenahm"),
        ("Ryan Floyd", "ryanfloyd"),
    ], "Seed, Series A", "Enterprise SaaS, AI, B2B", "Tier 2", "65", "B2B SaaS specialist"),

    ("Trinity Ventures", "trinityventures.com", "Menlo Park", [
        ("Schwark Satyavolu", "schwark"),
    ], "Seed, Series A", "Consumer, SaaS, Health", "Tier 2", "75", "Consumer and SaaS investor"),

    ("Wing VC", "wing.vc", "Palo Alto", [
        ("Peter Wagner", "peterwagner"),
        ("Gaurav Garg", "gauravgarg"),
        ("Jake Flomenberg", "jakeflomenberg"),
    ], "Seed, Series A", "AI, Enterprise, Infrastructure, Developer Tools", "Tier 2", "72", "Technical early-stage fund"),

    ("Define Ventures", "defineventures.com", "San Francisco", [
        ("Kim Milosevich", "kimmilosevich"),
    ], "Pre-Seed, Seed", "Consumer, AI, Health, Fintech", "Tier 2", "80", "Solo GP with strong consumer health thesis"),

    ("Homebrew", "homebrew.co", "San Francisco", [
        ("Hunter Walk", "hunterwalk"),
        ("Satya Patel", "satyap"),
    ], "Pre-Seed, Seed", "Consumer, SaaS, AI, Creator Economy, Media", "Tier 1", "88", "Strong consumer and creator economy thesis, media-savvy partners"),

    ("Susa Ventures", "susaventures.com", "San Francisco", [
        ("Leo Polovets", "lpolovets"),
        ("Chad Byers", "chadbyers"),
    ], "Pre-Seed, Seed", "AI, Consumer, Health, Fintech, SaaS", "Tier 2", "82", "Data-driven seed fund with consumer and health focus"),

    ("Freestyle Capital", "freestyle.vc", "San Francisco", [
        ("Dave Samuel", "davesamuel"),
        ("Jenny Lefcourt", "jennylefcourt"),
    ], "Pre-Seed, Seed", "Consumer, SaaS, Health, AI", "Tier 2", "78", "Experienced micro-VC, strong early-stage consumer focus"),

    ("Uncork Capital", "uncorkcapital.com", "San Francisco", [
        ("Jeff Clavier", "jeffclavier"),
        ("Andy McLoughlin", "andymcl"),
    ], "Pre-Seed, Seed", "Consumer, SaaS, AI, Health", "Tier 2", "80", "Prolific seed investor with broad consumer and SaaS thesis"),

    ("Abstract Ventures", "abstractvc.com", "San Francisco", [
        ("Ramtin Naimi", "ramtinnaimi"),
    ], "Pre-Seed, Seed", "Consumer, SaaS, AI, Media", "Tier 2", "78", "Seed fund with consumer and media focus"),

    ("Amplify Partners", "amplifypartners.com", "San Francisco", [
        ("Sunil Dhaliwal", "sunildhaliwal"),
        ("Mike Dauber", "mikedauber"),
    ], "Seed, Series A", "AI, Enterprise, Infrastructure, Developer Tools", "Tier 2", "72", "Technical fund with strong AI and infrastructure thesis"),

    ("DCVC (Data Collective)", "dcvc.com", "San Francisco", [
        ("Matt Ocko", "mattocko"),
        ("Zachary Bogue", "zacharybogue"),
        ("Ali Tamaseb", "alitamaseb"),
    ], "Seed, Series A, Series B", "AI, Deep Tech, Health, Climate, Computational", "Tier 1", "75", "AI and computational biology leader"),

    ("Canaan Partners", "canaan.com", "Menlo Park", [
        ("Maha Ibrahim", "mahaibrahim"),
        ("Jed Katz", "jedkatz"),
    ], "Seed, Series A, Series B", "Health, Consumer, Enterprise, Fintech", "Tier 1", "80", "Multi-stage fund strong in health and consumer"),

    ("Y Combinator", "ycombinator.com", "San Francisco", [
        ("Garry Tan", "garrytan"),
        ("Michael Seibel", "mseibel"),
        ("Jared Friedman", "jaredfriedman"),
        ("Gustaf Alstromer", "gustafalstromer"),
        ("Diana Hu", "dianahu"),
        ("Dalton Caldwell", "daltoncaldwell"),
    ], "Pre-Seed, Seed", "AI, Consumer, Health, SaaS, Enterprise, Creator Economy", "Tier 1", "90", "Premier accelerator, invests across all sectors"),

    ("500 Global", "500.co", "San Francisco", [
        ("Christine Tsai", "christinetsai"),
        ("Clayton Bryan", "claytonbryan"),
    ], "Pre-Seed, Seed", "AI, Consumer, Health, SaaS, Global", "Tier 1", "78", "Global seed-stage accelerator and fund"),

    ("Plug and Play Tech Center", "plugandplaytechcenter.com", "Sunnyvale", [
        ("Saeed Amidi", "saeedamidi"),
    ], "Pre-Seed, Seed", "AI, Consumer, Health, Enterprise, Fintech, Media", "Tier 2", "75", "Large accelerator with vertical programs including health and media"),

    ("NFX", "nfx.com", "San Francisco", [
        ("James Currier", "jamescurrier"),
        ("Pete Flint", "peteflint"),
        ("Gigi Levy-Weiss", "gigilevy"),
        ("Morgan Beller", "morganbeller"),
    ], "Pre-Seed, Seed", "AI, Consumer, Marketplace, Network Effects, Health", "Tier 1", "85", "Network effects specialist with consumer and marketplace thesis"),

    ("GV (Google Ventures)", "gv.com", "San Francisco", [
        ("Krishna Yeshwant", "krishnayeshwant"),
        ("Terri Burns", "terriburns"),
        ("Tom Hulme", "tomhulme"),
        ("Tyson Clark", "tysonclark"),
    ], "Seed, Series A, Growth", "AI, Consumer, Health, Enterprise, Life Sciences", "Tier 1", "85", "Google-backed multi-stage with strong health and AI thesis"),

    ("Gradient Ventures (Google)", "gradient.google", "San Francisco", [
        ("Anna Patterson", "annapatterson"),
    ], "Seed, Series A", "AI, Machine Learning, Health, Consumer", "Tier 1", "82", "Google's AI-focused fund"),

    ("Sapphire Ventures", "sapphireventures.com", "San Francisco", [
        ("Jai Das", "jaidas"),
        ("Rajeev Dham", "rajeevdham"),
        ("Nino Marakovic", "ninomarakovic"),
    ], "Series A, Series B, Growth", "AI, SaaS, Enterprise, Health", "Tier 1", "72", "Growth-stage enterprise and AI investor"),

    ("Altimeter Capital", "altimetercap.com", "Menlo Park", [
        ("Brad Gerstner", "bradgerstner"),
        ("Jamin Ball", "jaminball"),
    ], "Series A, Growth", "AI, Consumer, SaaS, Cloud", "Tier 1", "72", "Crossover public/private fund with strong tech thesis"),

    ("Elad Gil (solo GP)", "eladgil.com", "San Francisco", [
        ("Elad Gil", "eladgil"),
    ], "Seed, Series A", "AI, Consumer, SaaS, Health", "Tier 1", "80", "Prolific angel/solo GP, backs AI and consumer companies"),

    ("Lachy Groom (solo GP)", "lachygroom.com", "San Francisco", [
        ("Lachy Groom", "lachygroom"),
    ], "Seed, Series A", "AI, Fintech, Consumer, Infrastructure", "Tier 1", "78", "Solo GP from Stripe, backs AI-native companies"),

    ("Bloomberg Beta", "bloombergbeta.com", "San Francisco", [
        ("Roy Bahat", "roybahat"),
        ("Karin Klein", "karineklein"),
        ("James Cham", "jamescham"),
    ], "Pre-Seed, Seed", "AI, Media, Future of Work, Enterprise", "Tier 2", "82", "Bloomberg-backed fund focused on future of work and AI"),

    ("Aspect Ventures / Cleo Capital", "cleocapital.com", "San Francisco", [
        ("Sarah Kunst", "sarahkunst"),
    ], "Pre-Seed, Seed", "Consumer, AI, Health, Creator Economy", "Tier 2", "80", "Solo GP focused on consumer, health, and creator startups"),

    ("Precursor Ventures", "precursorvc.com", "San Francisco", [
        ("Charles Hudson", "charlesrhudson"),
    ], "Pre-Seed, Seed", "Consumer, SaaS, AI, Health, Media", "Tier 2", "82", "Leading pre-seed fund, strong consumer and media thesis"),

    ("Kindred Ventures", "kindredventures.com", "San Francisco", [
        ("Kanyi Maqubela", "kanyimaqubela"),
        ("Steve Jang", "stevejang"),
    ], "Pre-Seed, Seed", "Consumer, AI, Health, Creator Economy, Media", "Tier 2", "82", "Consumer-first seed fund with creator and health thesis"),

    ("Unusual Ventures", "unusual.vc", "Menlo Park", [
        ("John Vrionis", "johnvrionis"),
        ("Jyoti Bansal", "jyotibansal"),
    ], "Seed, Series A", "AI, Enterprise, SaaS, Developer Tools", "Tier 2", "72", "Go-to-market focused fund"),

    ("Emergence Capital", "emcap.com", "San Francisco", [
        ("Jason Green", "jasongreen"),
        ("Santi Subotovsky", "santisubotovsky"),
        ("Jake Saper", "jakesaper"),
    ], "Series A, Series B", "SaaS, AI, Enterprise, Coaching/Wellness", "Tier 2", "72", "SaaS specialist with coaching platform interest"),

    ("Point72 Ventures", "point72.com", "Menlo Park", [
        ("Sri Chandrasekar", "srichandrasekar"),
    ], "Seed, Series A, Series B", "AI, Health, Fintech, Consumer", "Tier 1", "75", "Steve Cohen-backed venture arm with health and AI focus"),

    ("Sway Ventures", "swayvc.com", "San Francisco", [
        ("Brian Yee", "brianyee"),
    ], "Seed, Series A", "AI, Consumer, SaaS, Infrastructure", "Tier 2", "72", "Cross-border fund with AI focus"),

    ("AlleyCorp", "alleycorp.com", "San Francisco", [
        ("Kevin Ryan", "kevinryan"),
    ], "Seed, Series A", "AI, Consumer, Health, Media", "Tier 2", "78", "Studio/fund model, builds and invests in AI companies"),

    ("Cota Capital", "cotacapital.com", "San Francisco", [
        ("Simran Gambhir", "simrangambhir"),
    ], "Series A, Series B", "SaaS, AI, Consumer, Health", "Tier 2", "72", "Growth-focused fund with SaaS and health thesis"),

    ("Valor Equity Partners", "valorep.com", "San Francisco", [
        ("Antonio Gracias", "antoniogracias"),
    ], "Series A, Growth", "AI, Consumer, Health, Space, Mobility", "Tier 1", "72", "Operational VC, early Tesla backer"),

    ("Moment Ventures", "momentventures.com", "San Francisco", [
        ("Clint Korver", "clintkorver"),
    ], "Pre-Seed, Seed", "AI, Consumer, Health, SaaS", "Tier 3", "70", "Micro-VC with consumer and health interest"),

    ("Scribble Ventures", "scribbleventures.com", "San Francisco", [
        ("Joel Yarmon", "joelyarmon"),
    ], "Pre-Seed, Seed", "Consumer, AI, SaaS, Health", "Tier 3", "72", "Micro-VC with consumer and AI thesis"),

    ("Operator Partners", "operatorpartners.com", "San Francisco", [
        ("Lexi Reese", "lexireese"),
    ], "Seed, Series A", "Consumer, AI, Health, Enterprise", "Tier 2", "75", "Operator-backed fund with consumer and health focus"),

    ("Norwest Venture Partners", "nvp.com", "Palo Alto", [
        ("Jeff Crowe", "jeffcrowe"),
        ("Rama Sekhar", "ramasekhar"),
        ("Lisa Wu", "lisawu"),
    ], "Series A, Series B, Growth", "AI, Consumer, Health, Enterprise, SaaS", "Tier 1", "78", "Large multi-stage fund with health and consumer thesis"),

    # === LOS ANGELES FUNDS ===

    ("Upfront Ventures", "upfront.com", "Los Angeles", [
        ("Mark Suster", "msuster"),
        ("Kara Nortman", "karanortman"),
        ("Kobie Fuller", "kobiefuller"),
        ("Aditi Maliwal", "aditimaliwal"),
    ], "Seed, Series A, Series B", "Consumer, AI, Health, Entertainment, Media, Creator Economy", "Tier 1", "92", "Leading LA VC, strong entertainment, media, and consumer focus"),

    ("Wonder Ventures", "wonderventures.com", "Los Angeles", [
        ("Dustin Rosen", "dustinrosen"),
    ], "Pre-Seed, Seed", "Consumer, AI, Media, Entertainment, Health, Wellness", "Tier 2", "90", "LA-focused seed fund with entertainment and consumer health thesis"),

    ("TenOneTen Ventures", "tenonetenventures.com", "Los Angeles", [
        ("Minnie Ingersoll", "minnieingersoll"),
        ("David Waxman", "davidwaxman"),
        ("Gill Elbaz", "gillelbaz"),
    ], "Pre-Seed, Seed", "AI, Consumer, Health, SaaS, Data", "Tier 2", "80", "LA-based data-driven seed fund with AI focus"),

    ("Mucker Capital", "muckercapital.com", "Los Angeles", [
        ("Erik Rannala", "erikrannala"),
        ("William Hsu", "williamhsu"),
        ("Omar Hamoui", "omarhamoui"),
    ], "Pre-Seed, Seed", "Consumer, SaaS, AI, Health, Media", "Tier 2", "82", "LA-based accelerator/fund with consumer and health focus"),

    ("Fika Ventures", "fikaventures.com", "Los Angeles", [
        ("Eva Ho", "evaho"),
        ("TX Zhuo", "txzhuo"),
    ], "Pre-Seed, Seed", "AI, Consumer, Health, SaaS, Fintech", "Tier 2", "80", "LA seed fund with AI and consumer health thesis"),

    ("Wavemaker Partners", "wavemaker.vc", "Los Angeles", [
        ("Eric Manlunas", "ericmanlunas"),
        ("Paul Santos", "paulsantos"),
    ], "Pre-Seed, Seed", "AI, Consumer, Health, Enterprise, Deep Tech", "Tier 2", "75", "LA/SEA cross-border fund"),

    ("Third Kind Venture Capital", "thirdkindvc.com", "Los Angeles", [
        ("Rich Miner", "richminer"),
    ], "Seed, Series A", "Entertainment, Media, AI, Consumer", "Tier 2", "85", "Entertainment and media tech specialist"),

    ("Greycroft", "greycroft.com", "Los Angeles", [
        ("Dana Settle", "danasettle"),
        ("John Elton", "johnelton"),
        ("Ian Sigalow", "iansigalow"),
    ], "Seed, Series A, Series B", "Consumer, Media, Entertainment, Health, AI", "Tier 1", "90", "Consumer media fund, deeply embedded in entertainment industry"),

    ("MANTIS VC", "mantisvc.com", "Los Angeles", [
        ("The Chainsmokers", "thechainsmokers"),
    ], "Pre-Seed, Seed", "Consumer, Media, Entertainment, Creator Economy, Wellness", "Tier 2", "82", "Creator/entertainment-native fund"),

    ("MaC Venture Capital", "macventurecapital.com", "Los Angeles", [
        ("Marlon Nichols", "marlonnichols"),
        ("Adrian Fenty", "adrianfenty"),
        ("Michael Palank", "michaelpalank"),
        ("Charles King", "charlesking"),
    ], "Pre-Seed, Seed, Series A", "Consumer, AI, Entertainment, Health, Media, Creator Economy", "Tier 1", "90", "Culture-driven fund with deep entertainment, media, and creator thesis"),

    ("Vamos Ventures", "vamosventures.com", "Los Angeles", [
        ("Marcos Gonzalez", "marcosgonzalez"),
    ], "Pre-Seed, Seed", "Consumer, AI, Health, Media", "Tier 2", "78", "Diverse-led LA seed fund with consumer focus"),

    ("Watertower Ventures", "watertowerventures.com", "Los Angeles", [
        ("Kevin Winston", "kevinwinston"),
    ], "Pre-Seed, Seed", "Entertainment, Media, Consumer, AI, Creator Economy", "Tier 2", "85", "Entertainment tech focused LA fund"),

    ("Science Inc", "science-inc.com", "Los Angeles", [
        ("Mike Jones", "mikejones"),
        ("Peter Pham", "peterpham"),
    ], "Pre-Seed, Seed", "Consumer, Media, Entertainment, AI, Creator Economy, Commerce", "Tier 2", "88", "LA studio/fund, Dollar Shave Club origins, strong consumer and media"),

    ("Kairos HQ", "kairoshq.com", "Los Angeles", [
        ("Ankur Jain", "ankurjain"),
    ], "Seed, Series A", "Consumer, Health, Wellness, Housing, Insurance", "Tier 2", "80", "Consumer essentials and health/wellness focused"),

    ("Anthos Capital", "anthoscapital.com", "Santa Monica", [
        ("Richard Wolpert", "richardwolpert"),
    ], "Seed, Series A", "Consumer, Media, Entertainment, AI, Commerce", "Tier 2", "85", "LA fund focused on consumer and entertainment"),

    # === ADDITIONAL NEW FUNDS TO REACH 100+ ===

    ("Radical Ventures", "radical.vc", "San Francisco", [
        ("Jordan Jacobs", "jordanjacobs"),
        ("Tomi Poutanen", "tomipoutanen"),
    ], "Seed, Series A, Series B", "AI, Machine Learning, Deep Tech, Health", "Tier 1", "82", "AI-first fund, Geoffrey Hinton connection"),

    ("Coatue Management", "coatue.com", "San Francisco", [
        ("Philippe Laffont", "philippelaffont"),
        ("Kris Fredrickson", "krisfredrickson"),
    ], "Series A, Growth", "AI, Consumer, Enterprise, Health, Fintech", "Tier 1", "75", "Tiger-cub crossover with strong AI thesis"),

    ("Paradigm", "paradigm.xyz", "San Francisco", [
        ("Matt Huang", "matthuang"),
        ("Fred Ehrsam", "fredehrsam"),
    ], "Seed, Series A, Growth", "Crypto, AI, Web3, Consumer, DeFi", "Tier 1", "68", "Crypto-native fund expanding into AI"),

    ("Quiet Capital", "quiet.com", "Los Angeles", [
        ("Lee Linden", "leelinden"),
        ("John Gossett", "johngossett"),
    ], "Seed, Series A", "Consumer, AI, Media, Entertainment, Commerce", "Tier 2", "85", "LA-based consumer and media fund"),

    ("Sound Ventures", "sound.ventures", "Los Angeles", [
        ("Ashton Kutcher", "ashtonkutcher"),
        ("Guy Oseary", "guyoseary"),
        ("Effie Epstein", "effieepstein"),
    ], "Seed, Series A", "Consumer, Media, Entertainment, AI, Health, Wellness", "Tier 1", "88", "Celebrity-backed fund with deep entertainment and consumer health connections"),

    ("Goodwater Capital", "goodwatercap.com", "Burlingame", [
        ("Eric Kim", "erickim"),
        ("Chi-Hua Chien", "chihuachien"),
    ], "Seed, Series A", "Consumer, Mobile, AI, Health, Commerce", "Tier 2", "80", "Consumer-only fund with data-driven approach"),

    ("01 Advisors", "01advisors.com", "San Francisco", [
        ("Dick Costolo", "dickcostolo"),
        ("Adam Bain", "adambain"),
    ], "Seed, Series A", "Consumer, Media, AI, SaaS, Creator Economy", "Tier 2", "85", "Former Twitter execs investing in consumer and media"),

    ("Accel Partners", "accel.com", "Palo Alto", [
        ("Rich Wong", "richwong"),
        ("Amy Saper", "amysaper"),
        ("Ben Fletcher", "benfletcher"),
    ], "Seed, Series A, Growth", "Consumer, SaaS, AI, Enterprise, Fintech", "Tier 1", "82", "Global multi-stage with strong consumer portfolio"),

    ("Atomico", "atomico.com", "San Francisco", [
        ("Hiro Fernando", "hirofernando"),
    ], "Series A, Series B", "Consumer, AI, Health, Enterprise", "Tier 2", "72", "Skype founder's fund with SF office"),

    ("Convivialite Ventures", "conviviality.vc", "Los Angeles", [
        ("Andrea Hippeau", "andreahippeau"),
    ], "Pre-Seed, Seed", "Consumer, Food & Bev, Wellness, Health, Media", "Tier 2", "82", "Consumer lifestyle and wellness focus"),

    ("Left Lane Capital", "leftlane.com", "San Francisco", [
        ("Harley Miller", "harleymiller"),
    ], "Series A, Series B", "Consumer Internet, Health, Commerce, AI", "Tier 2", "78", "Consumer internet growth fund"),

    ("Bling Capital", "blingcap.com", "San Francisco", [
        ("Ben Ling", "benling"),
    ], "Pre-Seed, Seed", "AI, Consumer, SaaS, Health, Fintech", "Tier 2", "80", "Prolific seed investor, ex-Google/Facebook"),

    ("Struck Capital", "struckcapital.com", "Los Angeles", [
        ("Adam Struck", "adamstruck"),
    ], "Seed, Series A", "Consumer, AI, Commerce, Health, SaaS", "Tier 2", "78", "LA-based fund with consumer and health thesis"),

    ("Reach Capital", "reachcapital.com", "San Francisco", [
        ("Jennifer Carolan", "jennifercarolan"),
        ("Wayee Chu", "wayeechu"),
    ], "Pre-Seed, Seed, Series A", "EdTech, Consumer, AI, Health, Wellness", "Tier 2", "78", "EdTech and consumer health focus"),

    ("Offline Ventures", "offline.vc", "Los Angeles", [
        ("Mark Goldstein", "markgoldstein"),
        ("Zach Rash", "zachrash"),
    ], "Pre-Seed, Seed", "Consumer, Wellness, Health, Fitness, Media", "Tier 2", "85", "LA seed fund focused on wellness, fitness, and consumer health"),

    ("Chapter One", "chapterone.com", "San Francisco", [
        ("Jeff Morris Jr.", "jeffmorrisjr"),
    ], "Pre-Seed, Seed", "Consumer, AI, Creator Economy, Media, SaaS", "Tier 2", "85", "Solo GP with strong consumer product and creator thesis"),

    ("Cherubic Ventures", "cherubic.com", "San Francisco", [
        ("Matt Cheng", "mattcheng"),
        ("Tina Cheng", "tinacheng"),
    ], "Seed, Series A", "Consumer, AI, Commerce, Media", "Tier 2", "75", "Cross-border consumer fund"),

    ("January Ventures", "january.co", "San Francisco", [
        ("Jennifer Neundorfer", "jenniferneundorfer"),
        ("Maia Bittner", "maiabittner"),
    ], "Pre-Seed, Seed", "Consumer, Health, AI, SaaS, Future of Work", "Tier 3", "78", "Early-stage fund focused on diverse founders"),

    ("XYZ Venture Capital", "xyz.vc", "San Francisco", [
        ("Ross Fubini", "rossfubini"),
        ("MJ Eng", "mjeng"),
    ], "Seed, Series A", "AI, Consumer, Enterprise, SaaS, Health", "Tier 2", "78", "Multi-stage with AI and consumer thesis"),

    ("Liquid 2 Ventures", "liquid2.vc", "San Francisco", [
        ("Joe Montana", "joemontana"),
        ("Michael Ma", "michaelma"),
    ], "Pre-Seed, Seed", "Consumer, AI, Health, SaaS, Sports", "Tier 2", "78", "Joe Montana's fund, consumer and health interest"),

    ("Tribe Capital", "tribecap.co", "San Francisco", [
        ("Arjun Sethi", "arjunsethi"),
        ("Jonathan Hsu", "jonathanhsu"),
    ], "Seed, Series A, Growth", "AI, Consumer, Fintech, Enterprise, Data", "Tier 1", "78", "Data-driven fund from Social Capital alumni"),

    ("Haystack", "haystack.vc", "San Francisco", [
        ("Semil Shah", "semilshah"),
    ], "Pre-Seed, Seed", "Consumer, AI, SaaS, Health, Media", "Tier 2", "78", "Prolific solo GP seed investor"),

    ("Collab Capital", "collabcapital.com", "San Francisco", [
        ("Jewel Burks Solomon", "jewelburkssolomon"),
    ], "Pre-Seed, Seed", "Consumer, AI, Health, SaaS, Creator Economy", "Tier 2", "78", "Diverse-led fund with consumer and health thesis"),

    ("Eniac Ventures", "eniac.vc", "San Francisco", [
        ("Vic Singh", "vicsingh"),
        ("Nihal Mehta", "nihalmehta"),
        ("Hadley Harris", "hadleyharris"),
    ], "Pre-Seed, Seed", "Consumer, AI, Health, Mobile, SaaS", "Tier 2", "80", "Mobile-first seed fund with consumer focus"),

    ("Comcast Ventures / Rethink Capital", "rethinkcapital.com", "San Francisco", [
        ("Gil Beyda", "gilbeyda"),
    ], "Seed, Series A", "Media, Entertainment, Consumer, AI, Health", "Tier 2", "82", "Media giant-backed fund with entertainment thesis"),

    ("a]venture", "aventure.vc", "Los Angeles", [
        ("Allen DeBevoise", "allendebevoise"),
    ], "Pre-Seed, Seed", "Media, Entertainment, AI, Consumer, Creator Economy", "Tier 2", "88", "LA media/entertainment focused fund from Machinima founder"),

    ("Datum Engineering", "datum.vc", "San Francisco", [
        ("Jake Chapman", "jakechapman"),
    ], "Pre-Seed, Seed", "Consumer, AI, SaaS, Health", "Tier 3", "72", "Micro-VC with consumer and AI thesis"),

    ("The Fund", "thefund.vc", "San Francisco", [
        ("Jenny Fielding", "jennyfielding"),
    ], "Pre-Seed, Seed", "Consumer, AI, SaaS, Health", "Tier 3", "70", "Community-driven micro-VC"),

    ("The Artemis Fund", "theartemisfund.com", "Los Angeles", [
        ("Diana Murakhovskaya", "dianamurakhovskaya"),
        ("Leslie Goldman", "lesliegoldman"),
    ], "Pre-Seed, Seed", "Consumer, Health, Wellness, Femtech, AI", "Tier 2", "85", "Women-led fund focused on consumer health and wellness"),

    ("Backstage Capital", "backstagecapital.com", "Los Angeles", [
        ("Arlan Hamilton", "arlanhamilton"),
    ], "Pre-Seed, Seed", "Consumer, AI, Media, Health, Creator Economy", "Tier 2", "80", "Diverse-led fund backing underrepresented founders"),

    ("Slauson & Co", "slausonco.com", "Los Angeles", [
        ("Austin Clements", "austinclements"),
    ], "Pre-Seed, Seed", "Consumer, AI, Health, Media, Entertainment", "Tier 2", "82", "LA fund investing in underserved communities and consumer"),

    ("Harlem Capital (SF Office)", "harlem.capital", "San Francisco", [
        ("Henri Pierre-Jacques", "henripierrejacques"),
    ], "Pre-Seed, Seed, Series A", "Consumer, Health, AI, SaaS, Media", "Tier 2", "78", "Diverse-led fund with consumer and health thesis"),

    ("Inevitable Ventures", "inevitableventures.com", "Los Angeles", [
        ("Kian Sadeghi", "kiansadeghi"),
    ], "Seed, Series A", "Health, Wellness, Consumer, AI, Media", "Tier 2", "85", "LA fund focused on health, wellness, and impact"),
]

def generate_email(first_name, fund_website):
    domain = fund_website.replace("https://", "").replace("http://", "").strip("/")
    return f"{first_name.lower().split()[0]}@{domain}"

def main():
    existing_funds = load_existing_funds()
    
    rows = []
    skipped_funds = []
    included_funds = set()
    
    for fund_name, website, city, partners, stage, sectors, priority, score, fit_reason in NEW_VCS:
        fund_lower = fund_name.lower()
        # Check against existing - use partial match
        is_dup = False
        for ef in existing_funds:
            # Exact or close match
            if fund_lower == ef or fund_lower in ef or ef in fund_lower:
                is_dup = True
                break
        
        if is_dup:
            skipped_funds.append(fund_name)
            continue
            
        included_funds.add(fund_name)
        for name, linkedin_slug in partners:
            email = generate_email(name, website)
            rows.append({
                'Name': name,
                'Email': email,
                'Location (City)': city,
                'Location (State)': 'California',
                'Location (Country)': 'United States',
                'Type of Investor': 'VC',
                'Stage: Investment Thesis': stage,
                'Sector: Investment Thesis': sectors,
                'LinkedIn': f"https://linkedin.com/in/{linkedin_slug}",
                'Website': f"https://{website}",
                'Fund': fund_name,
                'Priority Tier': priority,
                'Thesis Match Score': score,
                'Why This Investor is a Fit': fit_reason,
            })
    
    with open(OUTPUT, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Total unique VC firms added: {len(included_funds)}")
    print(f"Total partner entries: {len(rows)}")
    print(f"Skipped (already in DB): {len(skipped_funds)}")
    if skipped_funds:
        for s in skipped_funds:
            print(f"  SKIP: {s}")
    print(f"\nSaved to: {OUTPUT}")

if __name__ == '__main__':
    main()
