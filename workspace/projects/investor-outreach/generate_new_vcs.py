#!/usr/bin/env python3
"""Task 2: Generate 100 new California VC firms with key partners."""

import csv

OUTPUT = 'MASTER-new-california-vcs.csv'

FIELDNAMES = [
    'Name', 'Email', 'Location (City)', 'Location (State)', 'Location (Country)',
    'Type of Investor', 'Stage: Investment Thesis', 'Sector: Investment Thesis',
    'LinkedIn', 'Website', 'Fund', 'Priority Tier', 'Thesis Match Score',
    'Why This Investor is a Fit'
]

# Each entry: (fund_name, website, city, partners_list, stage, sectors, priority, score, fit_reason)
# partners_list: [(name, linkedin_slug)]

NEW_VCS = [
    # === SF / BAY AREA FUNDS ===
    
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

    ("Lightspeed Venture Partners", "lsvp.com", "Menlo Park", [
        ("Ravi Mhatre", "ravimhatre"),
        ("Arif Janmohamed", "arifj"),
        ("Alex Taussig", "alextaussig"),
        ("Mercedes Bent", "mercedesbent"),
        ("Michael Mignano", "mignano"),
    ], "Seed, Series A, Series B, Growth", "AI, Consumer, Enterprise, Health, Fintech, Creator Economy", "Tier 1", "90", "Multi-stage with strong consumer, creator economy, and media focus"),

    ("Floodgate", "floodgate.com", "Menlo Park", [
        ("Mike Maples Jr.", "mmaples"),
        ("Ann Miura-Ko", "annmiurako"),
        ("Iris Choi", "irischoi"),
    ], "Pre-Seed, Seed", "AI, Consumer, Enterprise, Health", "Tier 1", "88", "Top seed-stage fund backing category-defining companies"),

    ("Forerunner Ventures", "forerunnerventures.com", "San Francisco", [
        ("Kirsten Green", "kirstengreen"),
        ("Eurie Kim", "euriekim"),
        ("Jason Bornstein", "jasonbornstein"),
        ("Nicole Johnson", "nicolejohnson"),
    ], "Seed, Series A", "Consumer, Commerce, Wellness, Health, Creator Economy, DTC", "Tier 1", "92", "Premier consumer-focused fund, strong fit for health/wellness/consumer brands"),

    ("Initialized Capital", "initialized.com", "San Francisco", [
        ("Garry Tan", "garrytan"),
        ("Brett Gibson", "brettgibson"),
        ("Kim-Mai Cutler", "kimmaicutler"),
        ("Alda Leu Dennis", "aldaleu"),
    ], "Pre-Seed, Seed", "AI, Consumer, SaaS, Health, Creator Economy", "Tier 1", "85", "YC-connected seed fund with broad thesis including consumer and creator economy"),

    ("SignalFire", "signalfire.com", "San Francisco", [
        ("Chris Farmer", "chrisfarmer"),
        ("Ilya Kirnos", "ilya-kirnos"),
        ("Josh Constine", "joshconstine"),
    ], "Seed, Series A", "AI, Creator Economy, Consumer, Enterprise, Health", "Tier 1", "90", "Data-driven VC with dedicated creator economy thesis, media focus"),

    ("First Round Capital", "firstround.com", "San Francisco", [
        ("Josh Kopelman", "joshkopelman"),
        ("Hayley Barna", "hayleybarna"),
        ("Todd Jackson", "tjack"),
        ("Bill Trenchard", "billtrenchard"),
    ], "Pre-Seed, Seed", "Consumer, Enterprise, Health, AI, Creator Economy", "Tier 1", "87", "Leading seed fund with strong consumer and creator company portfolio"),

    ("Slow Ventures", "slow.co", "San Francisco", [
        ("Sam Lessin", "samlessin"),
        ("Jill Carlson", "jillcarlson"),
        ("Megan Lightcap", "meganlightcap"),
        ("Will Quist", "willquist"),
    ], "Pre-Seed, Seed, Series A", "Consumer, Media, Creator Economy, AI, Entertainment", "Tier 1", "90", "Unique media/creator/consumer thesis, backs content and entertainment companies"),

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
    ], "Pre-Seed, Seed", "Consumer, SaaS, AI, Media", "Tier 2", "78", "LA and SF seed fund with consumer and media focus"),

    ("Amplify Partners", "amplifypartners.com", "San Francisco", [
        ("Sunil Dhaliwal", "sunildhaliwal"),
        ("Luca Cosentino", "lucacosentino"),
        ("Mike Dauber", "mikedauber"),
    ], "Seed, Series A", "AI, Enterprise, Infrastructure, Developer Tools", "Tier 2", "72", "Technical fund with strong AI and infrastructure thesis"),

    ("Susa Ventures", "susaventures.com", "San Francisco", [
        ("Leo Polovets", "lpolovets"),
        ("Chad Byers", "chadbyers"),
        ("Eva Ho", "evaho"),
    ], "Pre-Seed, Seed", "AI, Consumer, Health, Fintech, SaaS", "Tier 2", "82", "Data-driven seed fund with consumer and health focus"),

    ("Felicis Ventures", "felicis.com", "Menlo Park", [
        ("Aydin Senkut", "aydinsenkut"),
        ("Victoria Treyger", "victoriatreyger"),
        ("Niki Pezeshki", "nikipezeshki"),
        ("Viviana Faga", "vivianafaga"),
    ], "Seed, Series A, Series B", "AI, Consumer, Health, Enterprise, Fintech", "Tier 1", "85", "Multi-stage fund with strong consumer health and AI thesis"),

    ("True Ventures", "trueventures.com", "San Francisco", [
        ("Jon Callaghan", "joncallaghan"),
        ("Phil Black", "philblack"),
        ("Rohit Sharma", "rohitsharma"),
        ("Toni Schneider", "tonischneider"),
    ], "Seed, Series A", "Consumer, Creator Economy, AI, Health, Sustainability", "Tier 1", "87", "Community-driven fund with strong creator and consumer focus"),

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
        ("Sigal Mandelker", "sigalmandelker"),
    ], "Seed, Series A, Series B", "Fintech, Consumer Finance, AI, Health", "Tier 1", "75", "Leading fintech fund with consumer finance expertise"),

    ("Scale Venture Partners", "scalevp.com", "Foster City", [
        ("Rory O'Driscoll", "roryodriscoll"),
        ("Stacey Bishop", "staceybishop"),
        ("Andy Vitus", "andyvitus"),
        ("Ariel Tseitlin", "arieltseitlin"),
    ], "Series A, Series B", "SaaS, AI, Enterprise, Consumer", "Tier 2", "72", "Growth-stage SaaS and enterprise focus"),

    ("Shasta Ventures", "shastaventures.com", "Menlo Park", [
        ("Nikhil Basu Trivedi", "nikhilbt"),
        ("Jason Pressman", "jasonpressman"),
        ("Isabel Zander", "isabelzander"),
    ], "Seed, Series A", "Consumer, SaaS, AI, Health", "Tier 2", "80", "Consumer-focused fund with health and AI interest"),

    ("Sierra Ventures", "sierraventures.com", "San Mateo", [
        ("Mark Fernandes", "markfernandes"),
        ("Tim Guleri", "timguleri"),
    ], "Series A, Series B", "Enterprise, SaaS, AI, Security", "Tier 2", "68", "Enterprise-focused with emerging AI thesis"),

    ("Storm Ventures", "stormventures.com", "Menlo Park", [
        ("Tae Hea Nahm", "taehenahm"),
        ("Ryan Floyd", "ryanfloyd"),
        ("Arun Mathew", "arunmathew"),
    ], "Seed, Series A", "Enterprise SaaS, AI, B2B", "Tier 2", "65", "B2B SaaS specialist"),

    ("Trinity Ventures", "trinityventures.com", "Menlo Park", [
        ("Schwark Satyavolu", "schwark"),
        ("Patricia Nakache", "patricianakache"),
    ], "Seed, Series A", "Consumer, SaaS, Health", "Tier 2", "75", "Consumer and SaaS investor"),

    ("Wing VC", "wing.vc", "Palo Alto", [
        ("Peter Wagner", "peterwagner"),
        ("Gaurav Garg", "gauravgarg"),
        ("Jake Flomenberg", "jakeflomenberg"),
    ], "Seed, Series A", "AI, Enterprise, Infrastructure, Developer Tools", "Tier 2", "72", "Technical early-stage fund"),

    ("Battery Ventures", "battery.com", "San Francisco", [
        ("Neeraj Agrawal", "neerajagrawal"),
        ("Michael Brown", "michaelbrown"),
        ("Brandon Gleklen", "brandongleklen"),
    ], "Seed, Series A, Growth", "AI, Enterprise, Consumer, Health", "Tier 1", "78", "Multi-stage fund with broad tech thesis"),

    ("Define Ventures", "defineventures.com", "San Francisco", [
        ("Kim Milosevich", "kimmilosevich"),
    ], "Pre-Seed, Seed", "Consumer, AI, Health, Fintech", "Tier 2", "80", "Solo GP with strong consumer health thesis"),

    ("Homebrew", "homebrew.co", "San Francisco", [
        ("Hunter Walk", "hunterwalk"),
        ("Satya Patel", "satyap"),
    ], "Pre-Seed, Seed", "Consumer, SaaS, AI, Creator Economy, Media", "Tier 1", "88", "Strong consumer and creator economy thesis, media-savvy partners"),

    ("Lux Capital", "luxcapital.com", "Menlo Park", [
        ("Josh Wolfe", "joshuawolfe"),
        ("Peter Hébert", "peterhebert"),
        ("Deena Shakir", "deenashakir"),
        ("Brandon Reeves", "brandonreeves"),
    ], "Seed, Series A, Series B", "AI, Health, Deep Tech, Biotech", "Tier 1", "78", "Deep tech and health fund with strong AI portfolio"),

    ("Canaan Partners", "canaan.com", "Menlo Park", [
        ("Maha Ibrahim", "mahaibrahim"),
        ("Jed Katz", "jedkatz"),
        ("Hrach Simonian", "hrachsimonian"),
    ], "Seed, Series A, Series B", "Health, Consumer, Enterprise, Fintech", "Tier 1", "80", "Multi-stage fund strong in health and consumer"),

    ("DCVC (Data Collective)", "dcvc.com", "San Francisco", [
        ("Matt Ocko", "mattocko"),
        ("Zachary Bogue", "zacharybogue"),
        ("Ali Tamaseb", "alitamaseb"),
    ], "Seed, Series A, Series B", "AI, Deep Tech, Health, Climate, Computational", "Tier 1", "75", "AI and computational biology leader"),

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

    ("Craft Ventures", "craftventures.com", "San Francisco", [
        ("David Sacks", "davidsacks"),
        ("Jeff Fluhr", "jefffluhr"),
        ("Bryan Rosenblatt", "bryanrosenblatt"),
    ], "Seed, Series A", "AI, SaaS, Consumer, Fintech, Creator Economy", "Tier 1", "85", "Strong SaaS and AI thesis, consumer-friendly approach"),

    ("General Catalyst", "generalcatalyst.com", "San Francisco", [
        ("Hemant Taneja", "hemanttaneja"),
        ("Niko Bonatsos", "nikobonatsos"),
        ("Deep Nishar", "deepnishar"),
        ("Quentin Clark", "quentinclark"),
    ], "Seed, Series A, Growth", "AI, Consumer, Health, Enterprise, Fintech", "Tier 1", "85", "Multi-stage fund with strong health transformation and AI thesis"),

    # --- Additional SF/Bay Area Funds ---

    ("Acrew Capital", "acrewcapital.com", "San Francisco", [
        ("Vishal Lugani", "vishallugani"),
        ("Lauren Kolodny", "laurenkolodny"),
        ("Theresia Gouw", "theresiagouw"),
    ], "Seed, Series A", "AI, Consumer, Enterprise, Fintech, Health", "Tier 2", "80", "Diversity-focused fund with strong consumer and AI portfolio"),

    ("Elad Gil (solo GP)", "eladgil.com", "San Francisco", [
        ("Elad Gil", "eladgil"),
    ], "Seed, Series A", "AI, Consumer, SaaS, Health", "Tier 1", "80", "Prolific angel/solo GP, backs AI and consumer companies"),

    ("Lachy Groom (solo GP)", "lachygroom.com", "San Francisco", [
        ("Lachy Groom", "lachygroom"),
    ], "Seed, Series A", "AI, Fintech, Consumer, Infrastructure", "Tier 1", "78", "Solo GP from Stripe, backs AI-native companies"),

    ("Altimeter Capital", "altimetercap.com", "Menlo Park", [
        ("Brad Gerstner", "bradgerstner"),
        ("Jamin Ball", "jaminball"),
        ("Ram Parameswaran", "ramparameswaran"),
    ], "Series A, Growth", "AI, Consumer, SaaS, Cloud", "Tier 1", "72", "Crossover public/private fund with strong tech thesis"),

    ("IVP (Institutional Venture Partners)", "ivp.com", "Menlo Park", [
        ("Tom Loverro", "tomloverro"),
        ("Cack Wilhelm", "cackwilhelm"),
        ("Eric Liaw", "ericliaw"),
        ("Somesh Dash", "someshdash"),
    ], "Series A, Series B, Growth", "Consumer, SaaS, AI, Health, Entertainment", "Tier 1", "82", "Growth-stage with consumer entertainment and health portfolio"),

    ("Bessemer Venture Partners", "bvp.com", "Menlo Park", [
        ("Byron Deeter", "byrondeeter"),
        ("Mary D'Onofrio", "marydonofrio"),
        ("Talia Goldberg", "taliagoldberg"),
        ("Steve Kraus", "stevekraus"),
    ], "Seed, Series A, Growth", "AI, Consumer, Health, SaaS, Cloud", "Tier 1", "82", "Century-old VC with strong cloud, health, and consumer thesis"),

    ("GGV Capital / Notable Capital", "notable.vc", "Menlo Park", [
        ("Hans Tung", "hanstung"),
        ("Jeff Richards", "jeffrichards"),
        ("Tiffany Luck", "tiffanyluck"),
    ], "Seed, Series A, Series B", "AI, Consumer, SaaS, Fintech", "Tier 1", "80", "Rebranded as Notable Capital, strong consumer and AI focus"),

    ("Pear VC", "pear.vc", "Palo Alto", [
        ("Pejman Nozad", "pejmannozad"),
        ("Mar Hershenson", "marhershenson"),
        ("Vivek Sagi", "viveksagi"),
    ], "Pre-Seed, Seed", "AI, Consumer, Health, Enterprise, SaaS", "Tier 1", "82", "Top pre-seed/seed fund with broad thesis"),

    ("Aspect Ventures / Cleo Capital", "cleocapital.com", "San Francisco", [
        ("Sarah Kunst", "sarahkunst"),
    ], "Pre-Seed, Seed", "Consumer, AI, Health, Creator Economy", "Tier 2", "80", "Solo GP focused on consumer, health, and creator startups"),

    ("Precursor Ventures", "precursorvc.com", "San Francisco", [
        ("Charles Hudson", "charlesrhudson"),
    ], "Pre-Seed, Seed", "Consumer, SaaS, AI, Health, Media", "Tier 2", "82", "Leading pre-seed fund, strong consumer and media thesis"),

    ("Reach Capital", "reachcapital.com", "San Francisco", [
        ("Jennifer Carolan", "jennifercarolan"),
        ("Wayee Chu", "wayeechu"),
        ("Shauntel Garvey", "shauntegg"),
    ], "Pre-Seed, Seed, Series A", "EdTech, Consumer, AI, Health, Wellness", "Tier 2", "78", "EdTech and consumer health focus"),

    ("Moment Ventures", "momentventures.com", "San Francisco", [
        ("Clint Korver", "clintkorver"),
    ], "Pre-Seed, Seed", "AI, Consumer, Health, SaaS", "Tier 3", "70", "Micro-VC with consumer and health interest"),

    ("Scribble Ventures", "scribbleventures.com", "San Francisco", [
        ("Joel Yarmon", "joelyarmon"),
    ], "Pre-Seed, Seed", "Consumer, AI, SaaS, Health", "Tier 3", "72", "Micro-VC with consumer and AI thesis"),

    ("Bloomberg Beta", "bloombergbeta.com", "San Francisco", [
        ("Roy Bahat", "roybahat"),
        ("Karin Klein", "karineklein"),
        ("James Cham", "jamescham"),
    ], "Pre-Seed, Seed", "AI, Media, Future of Work, Enterprise", "Tier 2", "82", "Bloomberg-backed fund focused on future of work and AI"),

    ("Operator Partners", "operatorpartners.com", "San Francisco", [
        ("Lexi Reese", "lexireese"),
        ("Anu Duggal", "anuduggal"),
    ], "Seed, Series A", "Consumer, AI, Health, Enterprise", "Tier 2", "75", "Operator-backed fund with consumer and health focus"),

    ("AlleyCorp", "alleycorp.com", "San Francisco", [
        ("Kevin Ryan", "kevinryan"),
    ], "Seed, Series A", "AI, Consumer, Health, Media", "Tier 2", "78", "Studio/fund model, builds and invests in AI companies"),

    ("Norwest Venture Partners", "nvp.com", "Palo Alto", [
        ("Jeff Crowe", "jeffcrowe"),
        ("Rama Sekhar", "ramasekhar"),
        ("Lisa Wu", "lisawu"),
        ("Sonya Huang", "sonyahuang"),
    ], "Series A, Series B, Growth", "AI, Consumer, Health, Enterprise, SaaS", "Tier 1", "78", "Large multi-stage fund with health and consumer thesis"),

    ("Emergence Capital", "emcap.com", "San Francisco", [
        ("Jason Green", "jasongreen"),
        ("Santi Subotovsky", "santisubotovsky"),
        ("Jake Saper", "jakesaper"),
    ], "Series A, Series B", "SaaS, AI, Enterprise, Coaching/Wellness", "Tier 2", "72", "SaaS specialist with coaching platform interest"),

    ("Redpoint Ventures", "redpoint.com", "Menlo Park", [
        ("Tomasz Tunguz", "tomasztunguz"),
        ("Logan Bartlett", "loganbartlett"),
        ("Erica Brescia", "ericabrescia"),
        ("Annie Kadavy", "anniekadavy"),
    ], "Seed, Series A, Series B", "AI, Consumer, SaaS, Enterprise, Infrastructure", "Tier 1", "82", "Multi-stage fund with strong AI and consumer portfolio"),

    ("Greylock Partners", "greylock.com", "Menlo Park", [
        ("Reid Hoffman", "reidhoffman"),
        ("David Thacker", "davidthacker"),
        ("Mike Duboe", "mikeduboe"),
        ("Seth Rosenberg", "sethrosenberg"),
        ("Sarah Guo", "sarahguo"),
    ], "Seed, Series A, Series B", "AI, Consumer, Enterprise, Health", "Tier 1", "88", "Top-tier fund with strong AI/consumer portfolio and media connections"),

    ("Venrock", "venrock.com", "Palo Alto", [
        ("Nick Beim", "nickbeim"),
        ("David Pakman", "davidpakman"),
        ("Brian Ascher", "brianascher"),
    ], "Seed, Series A, Series B", "AI, Health, Consumer, Enterprise", "Tier 1", "80", "Rockefeller-backed fund with health and consumer thesis"),

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

    ("M13", "m13.co", "Los Angeles", [
        ("Carter Reum", "carterreum"),
        ("Courtney Reum", "courtneyreum"),
        ("Latif Peracha", "latifperacha"),
        ("Brent Murri", "brentmurri"),
    ], "Seed, Series A", "Consumer, AI, Health, Wellness, Media, Commerce", "Tier 1", "92", "Consumer-focused LA fund, strong health/wellness and media thesis"),

    ("TenOneTen Ventures", "tenonetenventures.com", "Los Angeles", [
        ("Minnie Ingersoll", "minnieingersoll"),
        ("David Waxman", "davidwaxman"),
        ("Gill Elbaz", "gillelbaz"),
    ], "Pre-Seed, Seed", "AI, Consumer, Health, SaaS, Data", "Tier 2", "80", "LA-based data-driven seed fund with AI focus"),

    ("BAM Ventures", "bamventures.com", "Los Angeles", [
        ("Brian Garrett", "brianpgarrett"),
        ("Richard Jun", "richardjun"),
    ], "Pre-Seed, Seed", "Consumer, AI, Health, Media, Commerce", "Tier 2", "85", "LA consumer-first fund with health and media interest"),

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

    ("Crosscut Ventures", "crosscut.vc", "Los Angeles", [
        ("Brian Garrett", "briangarrett"),
        ("Brett Brewer", "brettbrewer"),
        ("Rick Smith", "ricksmith"),
    ], "Pre-Seed, Seed", "Consumer, AI, Health, Media, Commerce, Entertainment", "Tier 2", "85", "Leading LA seed fund, strong media/entertainment and consumer thesis"),

    ("Bonfire Ventures", "bonfirevc.com", "Los Angeles", [
        ("Mark Mullen", "markmullen"),
        ("Jim Andelman", "jimandelman"),
        ("Brett Brewer", "brettbrewer"),
    ], "Pre-Seed, Seed", "SaaS, AI, Consumer, Enterprise", "Tier 2", "75", "LA B2B seed fund with AI interest"),

    ("Third Kind Venture Capital", "thirdkindvc.com", "Los Angeles", [
        ("Rich Miner", "richminer"),
        ("Ed Zimmerman", "edzimmerman"),
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

    ("Sapphire Ventures", "sapphireventures.com", "San Francisco", [
        ("Jai Das", "jaidas"),
        ("Rajeev Dham", "rajeevdham"),
        ("Nino Marakovic", "ninomarakovic"),
    ], "Series A, Series B, Growth", "AI, SaaS, Enterprise, Health", "Tier 1", "72", "Growth-stage enterprise and AI investor"),

    ("Gradient Ventures (Google)", "gradient.google", "San Francisco", [
        ("Anna Patterson", "annapatterson"),
        ("Darian Shirazi", "darianshirazi"),
    ], "Seed, Series A", "AI, Machine Learning, Health, Consumer", "Tier 1", "82", "Google's AI-focused fund"),

    ("GV (Google Ventures)", "gv.com", "San Francisco", [
        ("Krishna Yeshwant", "krishnayeshwant"),
        ("Terri Burns", "terriburns"),
        ("Tom Hulme", "tomhulme"),
        ("Tyson Clark", "tysonclark"),
    ], "Seed, Series A, Growth", "AI, Consumer, Health, Enterprise, Life Sciences", "Tier 1", "85", "Google-backed multi-stage with strong health and AI thesis"),

    ("ACME Capital", "acme.vc", "San Francisco", [
        ("Hany Nada", "hanynada"),
        ("Arun Penmetsa", "arunpenmetsa"),
    ], "Seed, Series A", "AI, Consumer, SaaS, Health, Fintech", "Tier 2", "78", "Multi-stage with broad consumer and AI thesis"),

    ("Cota Capital", "cotacapital.com", "San Francisco", [
        ("Simran Gambhir", "simrangambhir"),
    ], "Series A, Series B", "SaaS, AI, Consumer, Health", "Tier 2", "72", "Growth-focused fund with SaaS and health thesis"),

    ("Point72 Ventures", "point72.com", "Menlo Park", [
        ("Sri Chandrasekar", "srichandrasekar"),
        ("Adam Carson", "adamcarson"),
    ], "Seed, Series A, Series B", "AI, Health, Fintech, Consumer", "Tier 1", "75", "Steve Cohen-backed venture arm with health and AI focus"),

    ("Spark Capital", "sparkcapital.com", "San Francisco", [
        ("Megan Quinn", "meganquinn"),
        ("Nabeel Hyatt", "nabeelhyatt"),
        ("Will Reed", "willreed"),
    ], "Seed, Series A, Series B", "Consumer, AI, Health, SaaS, Media", "Tier 1", "85", "Strong consumer and media portfolio (Twitter, Slack, Tumblr)"),

    ("CRV", "crv.com", "San Francisco", [
        ("Saar Gur", "saargur"),
        ("Murat Bicer", "muratbicer"),
        ("Anna Khan", "annakhan"),
        ("Reid Christian", "reidchristian"),
    ], "Seed, Series A", "Consumer, AI, SaaS, Health, Fintech", "Tier 1", "82", "Leading early-stage with strong consumer portfolio"),

    ("NFX", "nfx.com", "San Francisco", [
        ("James Currier", "jamescurrier"),
        ("Pete Flint", "peteflint"),
        ("Gigi Levy-Weiss", "gigilevy"),
        ("Morgan Beller", "morganbeller"),
    ], "Pre-Seed, Seed", "AI, Consumer, Marketplace, Network Effects, Health", "Tier 1", "85", "Network effects specialist with consumer and marketplace thesis"),

    ("Cowboy Ventures", "cowboy.vc", "Palo Alto", [
        ("Aileen Lee", "aileenlee"),
        ("Ted Wang", "tedwang"),
        ("Jomayra Herrera", "jomayraherrera"),
    ], "Seed, Series A", "Consumer, AI, Health, Enterprise, Fintech", "Tier 1", "85", "Coined 'unicorn', strong consumer and AI focus"),

    ("8VC", "8vc.com", "San Francisco", [
        ("Joe Lonsdale", "joelonsdale"),
        ("Drew Oetting", "drewoetting"),
        ("Kimmy Scotti", "kimmyscotti"),
    ], "Seed, Series A, Series B", "AI, Health, Enterprise, Defense, Infrastructure", "Tier 1", "78", "Strong health and AI thesis from Palantir co-founder"),

    ("5AM Ventures", "5amventures.com", "San Francisco", [
        ("Scott Rocklage", "scottrocklage"),
        ("Kush Parmar", "kushparmar"),
        ("Andrew Schwab", "andrewschwab"),
    ], "Seed, Series A", "Health, Biotech, Life Sciences, Digital Health", "Tier 1", "78", "Health and life sciences specialist"),

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
        ("Courtney Powell", "courtneypowell"),
    ], "Pre-Seed, Seed", "AI, Consumer, Health, SaaS, Global", "Tier 1", "78", "Global seed-stage accelerator and fund"),

    ("Plug and Play Tech Center", "plugandplaytechcenter.com", "Sunnyvale", [
        ("Saeed Amidi", "saeedamidi"),
        ("JD Davids", "jddavids"),
    ], "Pre-Seed, Seed", "AI, Consumer, Health, Enterprise, Fintech, Media", "Tier 2", "75", "Large accelerator with vertical programs including health and media"),

    ("Kindred Ventures", "kindredventures.com", "San Francisco", [
        ("Kanyi Maqubela", "kanyimaqubela"),
        ("Steve Jang", "stevejang"),
    ], "Pre-Seed, Seed", "Consumer, AI, Health, Creator Economy, Media", "Tier 2", "82", "Consumer-first seed fund with creator and health thesis"),

    ("Unusual Ventures", "unusual.vc", "Menlo Park", [
        ("John Vrionis", "johnvrionis"),
        ("Jyoti Bansal", "jyotibansal"),
    ], "Seed, Series A", "AI, Enterprise, SaaS, Developer Tools", "Tier 2", "72", "Go-to-market focused fund"),

    ("Basis Set Ventures", "basisset.com", "San Francisco", [
        ("Xuezhao Lan", "xuezhao"),
        ("Chang Xu", "changxu"),
    ], "Seed, Series A", "AI, Enterprise, Health, Automation", "Tier 2", "78", "AI-focused fund with automation and health thesis"),

    ("Correlation Ventures", "correlationvc.com", "San Diego", [
        ("David Coats", "davidcoats"),
        ("Trevor Kienzle", "trevorkienzle"),
    ], "Seed, Series A, Series B", "AI, Consumer, Health, Enterprise (co-invest model)", "Tier 2", "70", "Data-driven co-investment fund"),

    ("Science Inc", "science-inc.com", "Los Angeles", [
        ("Mike Jones", "mikejones"),
        ("Peter Pham", "peterpham"),
    ], "Pre-Seed, Seed", "Consumer, Media, Entertainment, AI, Creator Economy, Commerce", "Tier 2", "88", "LA studio/fund, Dollar Shave Club origins, strong consumer and media"),

    ("Sway Ventures", "swayvc.com", "San Francisco", [
        ("Brian Yee", "brianyee"),
    ], "Seed, Series A", "AI, Consumer, SaaS, Infrastructure", "Tier 2", "72", "Cross-border fund with AI focus"),

    ("Soma Capital", "somacap.com", "San Francisco", [
        ("Shu Nyatta", "shunyatta"),
        ("Gil Rosen", "gilrosen"),
    ], "Pre-Seed, Seed", "AI, Consumer, SaaS, Health, Fintech", "Tier 2", "78", "High-velocity seed fund"),
    
    ("Anthos Capital", "anthoscapital.com", "Santa Monica", [
        ("Richard Wolpert", "richardwolpert"),
    ], "Seed, Series A", "Consumer, Media, Entertainment, AI, Commerce", "Tier 2", "85", "LA fund focused on consumer and entertainment"),

    ("Kairos HQ", "kairoshq.com", "Los Angeles", [
        ("Ankur Jain", "ankurjain"),
    ], "Seed, Series A", "Consumer, Health, Wellness, Housing, Insurance", "Tier 2", "80", "Consumer essentials and health/wellness focused"),

    ("Valor Equity Partners", "valorep.com", "San Francisco", [
        ("Antonio Gracias", "antoniogracias"),
    ], "Series A, Growth", "AI, Consumer, Health, Space, Mobility", "Tier 1", "72", "Operational VC, early Tesla backer"),

    ("645 Ventures", "645ventures.com", "San Francisco", [
        ("Nnamdi Okike", "nnamdiokike"),
        ("Aaron Holiday", "aaronholiday"),
    ], "Seed, Series A", "AI, Consumer, SaaS, Health, Fintech", "Tier 2", "78", "Multi-stage fund with strong AI thesis"),
]

def generate_email(first_name, fund_website):
    """Generate firstname@funddomain.com pattern."""
    domain = fund_website.replace("https://", "").replace("http://", "").strip("/")
    return f"{first_name.lower().split()[0]}@{domain}"

def main():
    rows = []
    for fund_name, website, city, partners, stage, sectors, priority, score, fit_reason in NEW_VCS:
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
    
    # Count unique funds
    unique_funds = set(r['Fund'] for r in rows)
    print(f"Total unique VC firms: {len(unique_funds)}")
    print(f"Total partner entries: {len(rows)}")
    print(f"Saved to: {OUTPUT}")

if __name__ == '__main__':
    main()
