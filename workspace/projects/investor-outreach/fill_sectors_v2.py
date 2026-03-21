#!/usr/bin/env python3
"""Fill Sector: Investment Thesis for investors in the master database. v2 - aggressive."""

import csv
import re
import sys
import io

INPUT = "/data/.openclaw/workspace/projects/investor-outreach/MASTER-investor-database-v2.csv"
OUTPUT = INPUT

SECTOR_COL = "Sector: Investment Thesis"
FUND_COL = "Fund"
NAME_COL = "Name"
TYPE_COL = "Type of Investor"
WEBSITE_COL = "Website"
LINKEDIN_COL = "LinkedIn"

# ── Well-known funds → sectors (extensive) ──────────────────────────────────
KNOWN_FUNDS = {}

# Build from list for compactness
_fund_data = [
    # Major VC firms
    ("a16z|andreessen horowitz|andreessen", "Enterprise, Consumer, Crypto, Fintech, Healthcare, AI, Gaming"),
    ("sequoia|sequoia capital", "Enterprise, Consumer, Healthcare, Fintech, AI"),
    ("benchmark|benchmark capital", "Enterprise, Consumer, SaaS, Marketplace"),
    ("greylock|greylock partners", "Enterprise, Consumer, AI, Data Infrastructure"),
    ("accel|accel partners", "Enterprise, SaaS, Fintech, Consumer, Security"),
    ("lightspeed|lightspeed venture partners|lightspeed ventures|lsvp", "Enterprise, Consumer, Healthcare, Fintech"),
    ("kleiner perkins|kpcb", "Enterprise, Consumer, Healthcare, Sustainability, AI"),
    ("bessemer venture partners|bessemer|bvp", "Enterprise, SaaS, Healthcare, Consumer"),
    ("index ventures", "Enterprise, Consumer, Fintech, Gaming"),
    ("founders fund", "Deep Tech, Enterprise, Consumer, Space, AI, Biotech"),
    ("general catalyst|general catalyst partners|gc", "Enterprise, Consumer, Healthcare, Fintech, AI"),
    ("khosla ventures", "Deep Tech, Healthcare, AI, Sustainability, Enterprise"),
    ("union square ventures|usv", "Consumer, Fintech, Crypto, Marketplace"),
    ("first round capital|first round", "Enterprise, Consumer, SaaS"),
    ("spark capital", "Consumer, Enterprise, Fintech"),
    ("insight partners|insight venture partners", "Enterprise, SaaS, Data, Security"),
    ("tiger global|tiger global management", "Enterprise, Consumer, Fintech, E-commerce"),
    ("coatue|coatue management", "Enterprise, Consumer, Fintech, AI"),
    ("ribbit capital", "Fintech, Financial Services"),
    ("qed investors", "Fintech, Financial Services"),
    ("felicis ventures|felicis", "Enterprise, Consumer, Healthcare, Fintech"),
    ("floodgate|floodgate fund", "Consumer, Enterprise, Marketplace"),
    ("true ventures", "Enterprise, Consumer, AI"),
    ("500 startups|500 global|500 istanbul", "Enterprise, Consumer, SaaS, Fintech"),
    ("y combinator|yc", "Enterprise, Consumer, SaaS, AI"),
    ("techstars", "Enterprise, Consumer, SaaS"),
    ("nea|new enterprise associates", "Enterprise, Healthcare, Consumer, AI"),
    ("battery ventures", "Enterprise, SaaS, Data Infrastructure"),
    ("ivp|institutional venture partners", "Enterprise, Consumer, SaaS"),
    ("gv|google ventures", "Enterprise, Healthcare, Consumer, AI"),
    ("intel capital", "Enterprise, AI, IoT, Cloud, Semiconductor"),
    ("salesforce ventures", "Enterprise, SaaS, AI, Cloud"),
    ("softbank|softbank vision fund", "Enterprise, Consumer, AI, Robotics"),
    ("lux capital", "Deep Tech, AI, Biotech, Space, Robotics"),
    ("initialized capital|initialized", "Enterprise, Consumer, AI"),
    ("fifth wall|fifth wall ventures", "Real Estate, PropTech, Construction Tech"),
    ("metaprop|metaprop nyc", "Real Estate, PropTech"),
    ("camber creek", "Real Estate, PropTech"),
    ("obvious ventures|obvious", "Sustainability, Clean Tech, Healthcare"),
    ("breakthrough energy ventures|breakthrough energy", "Clean Tech, Climate, Energy"),
    ("energy impact partners|eip", "Clean Tech, Energy, Sustainability"),
    ("congruent ventures", "Clean Tech, Sustainability, Energy"),
    ("s2g ventures", "Food & Beverage, AgTech, Clean Tech"),
    ("cultivian sandbox ventures", "Food & Beverage, AgTech"),
    ("arch venture partners", "Healthcare, Life Sciences, Biotech"),
    ("flagship pioneering", "Healthcare, Life Sciences, Biotech"),
    ("orbimed|orbimed advisors", "Healthcare, Life Sciences, Biotech"),
    ("versant ventures", "Healthcare, Life Sciences, Biotech"),
    ("section 32", "Healthcare, Life Sciences, AI, Deep Tech"),
    ("reach capital", "Education, EdTech"),
    ("owl ventures", "Education, EdTech"),
    ("learn capital", "Education, EdTech"),
    ("rethink education", "Education, EdTech"),
    ("sapphire ventures", "Enterprise, SaaS, AI"),
    ("forerunner ventures|forerunner", "Consumer, DTC, Retail, E-commerce"),
    ("imaginary ventures", "Consumer, DTC, Retail"),
    ("upfront ventures", "Consumer, Enterprise, SaaS"),
    ("foundry group|foundry", "Enterprise, SaaS"),
    ("menlo ventures", "Enterprise, Consumer, Healthcare"),
    ("norwest venture partners|norwest", "Enterprise, Healthcare, Consumer"),
    ("dfj|draper fisher jurvetson", "Enterprise, Consumer, Deep Tech"),
    ("redpoint ventures|redpoint", "Enterprise, Consumer, Infrastructure"),
    ("madrona|madrona venture group|madrona ventures", "Enterprise, AI, Cloud"),
    ("maveron", "Consumer, DTC"),
    ("cowboy ventures", "Enterprise, Consumer, AI"),
    ("uncork capital", "Enterprise, Consumer, SaaS"),
    ("eniac ventures", "Consumer, Mobile, Enterprise"),
    ("betaworks", "Media, Consumer, AI"),
    ("lerer hippeau|lerer hippeau ventures", "Consumer, Media, E-commerce"),
    ("greycroft|greycroft partners", "Consumer, Media, E-commerce, Digital Media"),
    ("ggv capital|ggv", "Enterprise, Consumer, E-commerce"),
    ("goodwater capital", "Consumer, E-commerce, Marketplace"),
    ("craft ventures", "Enterprise, Consumer, Fintech, Crypto"),
    ("8vc", "Enterprise, Deep Tech, Healthcare, Defense"),
    ("thrive capital", "Enterprise, Consumer, Fintech"),
    ("general atlantic", "Enterprise, Consumer, Healthcare, Fintech"),
    ("bain capital ventures", "Enterprise, Consumer, Healthcare, Fintech"),
    ("citi ventures", "Fintech, Enterprise"),
    ("comcast ventures", "Media, Consumer, Enterprise"),
    ("amazon alexa fund|alexa fund", "AI, Voice, Smart Home, Consumer"),
    ("m12", "Enterprise, AI, Cloud"),
    ("qualcomm ventures", "IoT, 5G, AI, Semiconductor"),
    ("samsung ventures|samsung next", "Consumer, Enterprise, AI, Semiconductor"),
    ("cisco investments", "Enterprise, Networking, Security, IoT"),
    ("dell technologies capital", "Enterprise, Cloud, AI, Infrastructure"),
    ("sutter hill ventures", "Enterprise, SaaS, Data"),
    ("emergence capital|emergence", "Enterprise, SaaS"),
    ("openview|openview venture partners", "Enterprise, SaaS"),
    ("matrix partners", "Enterprise, Consumer, SaaS"),
    ("b capital group|b capital", "Enterprise, Consumer, Fintech"),
    ("flybridge|flybridge capital|flybridge capital partners", "Enterprise, Consumer, AI"),
    ("iqt|in-q-tel", "Aerospace, Defense, Technology, AI"),
    ("precursor ventures|precursor", "Enterprise, Consumer, SaaS"),
    ("backstage capital", "Consumer, Enterprise, SaaS"),
    ("revolution|revolution ventures|revolution growth", "Enterprise, Consumer"),
    ("boldstart ventures|boldstart", "Enterprise, SaaS, Security"),
    ("work-bench", "Enterprise, SaaS"),
    ("costanoa ventures|costanoa", "Enterprise, SaaS, Data"),
    ("notation capital|notation", "Enterprise, SaaS, Data"),
    ("two sigma ventures|two sigma", "AI, Data, Fintech"),
    ("radical ventures", "AI, Machine Learning"),
    ("air street capital", "AI, Machine Learning"),
    ("playground global", "AI, Robotics, Deep Tech"),
    ("dcvc|data collective", "Deep Tech, AI, Data, Enterprise"),
    ("wing venture capital|wing", "Enterprise, SaaS, Infrastructure"),
    ("contrary|contrary capital", "Enterprise, Consumer, AI"),
    ("pear vc|pear", "Enterprise, Consumer, AI"),
    ("hustle fund", "Enterprise, Consumer, SaaS"),
    ("m13", "Consumer, Enterprise, Fintech"),
    ("crosscut ventures", "Enterprise, Consumer"),
    ("mucker capital", "Enterprise, Consumer, SaaS"),
    ("bonfire ventures", "Enterprise, SaaS"),
    ("fika ventures", "Enterprise, SaaS, AI"),
    ("wonder ventures", "Consumer, Enterprise"),
    ("susa ventures|susa", "Enterprise, Consumer, Data"),
    ("soma capital", "Enterprise, Consumer, SaaS"),
    ("slow ventures", "Consumer, Crypto, Media"),
    ("collaborative fund", "Consumer, Sustainability, Food"),
    ("homebrew", "Enterprise, Consumer"),
    ("haystack", "Consumer, Enterprise, SaaS"),
    ("compound|compound vc", "Enterprise, Consumer, Fintech"),
    ("cherry ventures|cherry", "Enterprise, Consumer, SaaS"),
    ("point nine capital|point nine", "Enterprise, SaaS, Marketplace"),
    ("balderton capital|balderton", "Enterprise, Consumer, Fintech"),
    ("atomico", "Enterprise, Consumer, Deep Tech"),
    ("northzone", "Enterprise, Consumer, Fintech"),
    ("creandum", "Enterprise, Consumer, SaaS"),
    ("earlybird|earlybird venture capital", "Enterprise, Consumer, Healthcare"),
    ("seedcamp", "Enterprise, Consumer, SaaS"),
    ("entrepreneur first|ef", "Enterprise, Consumer, Deep Tech"),
    ("antler", "Enterprise, Consumer"),
    ("winklevoss capital", "Crypto, Blockchain, Web3"),
    ("paradigm", "Crypto, Blockchain, Web3"),
    ("polychain capital", "Crypto, Blockchain, Web3"),
    ("pantera capital", "Crypto, Blockchain, Web3"),
    ("digital currency group|dcg", "Crypto, Blockchain, Web3"),
    ("coinbase ventures", "Crypto, Blockchain, Web3"),
    ("binance labs", "Crypto, Blockchain, Web3"),
    ("animoca brands", "Crypto, Gaming, Web3"),
    ("dragonfly capital|dragonfly", "Crypto, Blockchain, Web3"),
    ("a16z crypto", "Crypto, Blockchain, Web3"),
    ("electric capital", "Crypto, Blockchain, Web3"),
    ("framework ventures", "Crypto, DeFi, Web3"),
    ("multicoin capital", "Crypto, Blockchain, Web3"),
    ("blockchain capital", "Crypto, Blockchain, Web3"),
    ("galaxy digital", "Crypto, Blockchain, Web3"),
    ("rock health", "Healthcare, Digital Health"),
    ("oak hc/ft", "Healthcare, Fintech"),
    ("7wireventures|7wire ventures", "Healthcare, Digital Health"),
    ("f-prime capital|f-prime", "Healthcare, Life Sciences, Enterprise"),
    ("venrock", "Healthcare, Enterprise, Consumer"),
    ("deerfield management|deerfield", "Healthcare, Life Sciences, Biotech"),
    ("ra capital management|ra capital", "Healthcare, Life Sciences, Biotech"),
    ("future ventures", "Deep Tech, Sustainability, Space"),
    ("starburst|starburst ventures|starburst aerospace", "Aerospace, Defense"),
    ("space capital", "Aerospace, Space"),
    ("seraphim capital|seraphim", "Aerospace, Space"),
    ("sosv", "Deep Tech, Hardware, Biotech"),
    ("hax", "Hardware, Robotics, Deep Tech"),
    ("root ventures", "Hardware, Deep Tech"),
    ("eclipse ventures|eclipse", "Industrial, Manufacturing, Deep Tech"),
    ("prelude ventures", "Clean Tech, Sustainability, AgTech"),
    ("elemental excelerator", "Clean Tech, Sustainability, Energy"),
    ("clean energy ventures", "Clean Tech, Energy"),
    ("powerhouse ventures|powerhouse capital", "Clean Tech, Energy"),
    ("toyota ventures", "Mobility, Clean Tech, Robotics"),
    ("fontinalis partners", "Mobility, Transportation"),
    ("autotech ventures", "Mobility, Automotive"),
    ("cathay innovation", "Enterprise, Consumer, Sustainability"),
    ("partech", "Enterprise, Consumer, Fintech"),
    ("kima ventures", "Enterprise, Consumer, SaaS"),
    ("speedinvest", "Enterprise, Consumer, Fintech"),
    ("notion capital", "Enterprise, SaaS"),
    ("hoxton ventures", "Enterprise, Consumer"),
    ("target global", "Enterprise, Consumer, Fintech"),
    ("global founders capital|gfc", "Enterprise, Consumer"),
    ("propel venture partners", "Fintech, Financial Services"),
    ("nyca partners|nyca", "Fintech, Financial Services"),
    ("fin vc|fin capital", "Fintech, Financial Services"),
    ("vista equity partners|vista equity", "Enterprise, SaaS"),
    ("thoma bravo", "Enterprise, SaaS, Security"),
    ("kapor capital", "Social Impact, Enterprise"),
    ("emerson collective", "Social Impact, Education, Media"),
    ("omidyar network", "Social Impact, Financial Inclusion, Education"),
    ("chan zuckerberg initiative|czi", "Healthcare, Education, Social Impact"),
    ("harlem capital|harlem capital partners", "Consumer, Enterprise, Fintech"),
    ("concrete rose capital", "Consumer, Enterprise, Social Impact"),
    ("female founders fund", "Consumer, Enterprise, Healthcare"),
    ("base10 partners|base10", "Enterprise, Consumer, AI"),
    ("valor ventures|valor", "Enterprise, Consumer, SaaS"),
    ("panoramic ventures|panoramic", "Enterprise, Consumer, SaaS"),
    ("zetta venture partners|zetta", "AI, Machine Learning, Data"),
    ("amplify partners", "Enterprise, AI, Developer Tools"),
    ("gradient ventures", "AI, Machine Learning"),
    ("ai fund", "AI, Machine Learning"),
    # Additional well-known funds
    ("iconiq capital|iconiq", "Enterprise, Consumer, Technology"),
    ("bbg ventures", "Consumer, Enterprise, Media"),
    ("ame cloud ventures", "Enterprise, Consumer, AI, Cloud"),
    ("amino capital", "AI, Enterprise, Data"),
    ("temasek", "Enterprise, Consumer, Healthcare, Fintech"),
    ("tao capital partners|tao capital", "Enterprise, Consumer, Technology"),
    ("basis set ventures", "AI, Enterprise, Developer Tools"),
    ("rre ventures|rre", "Enterprise, Consumer, Fintech"),
    ("bitkraft ventures|bitkraft", "Gaming, Esports, Web3"),
    ("bowery capital", "Enterprise, SaaS"),
    ("anthemis|anthemis group", "Fintech, InsurTech"),
    ("bam ventures", "Consumer, Enterprise, Media"),
    ("correlation ventures", "Enterprise, Consumer"),
    ("inspired capital", "Consumer, Enterprise"),
    ("collab capital", "Enterprise, Consumer, SaaS"),
    ("slauson|slauson & co", "Consumer, Enterprise"),
    ("merus capital", "Enterprise, Consumer, SaaS"),
    ("founders circle capital", "Enterprise, Consumer"),
    ("swiftarc ventures", "Enterprise, Consumer, Fintech"),
    ("building ventures", "Real Estate, PropTech, Construction Tech"),
    ("cultivation capital", "Enterprise, Consumer, AgTech"),
    ("primetime partners", "Consumer, Healthcare, AgeTech"),
    ("anthos capital", "Consumer, Enterprise"),
    ("divergent capital", "Enterprise, Consumer"),
    ("nttvc", "Enterprise, AI, Communications"),
    ("columbia capital", "Enterprise, Communications, Infrastructure"),
    ("datapoint capital", "Enterprise, Data, AI"),
    ("hanaco venture capital|hanaco", "Consumer, Enterprise"),
    ("arboretum ventures", "Healthcare, Life Sciences"),
    ("allos ventures", "Enterprise, SaaS"),
    ("riverbest venture partners|rivervest", "Healthcare, Life Sciences"),
    ("illuminate ventures", "Enterprise, SaaS, Cloud"),
    ("springdale ventures", "Food & Beverage, Consumer"),
    ("bull city ventures|bull city venture partners", "Enterprise, Consumer"),
    ("sogal ventures", "Consumer, Enterprise, Diversity"),
    ("cure ventures", "Healthcare, Life Sciences"),
    ("sony innovation fund", "Media, Entertainment, Gaming, AI"),
    ("tpg growth|tpg|tpg capital", "Enterprise, Healthcare, Consumer"),
    ("warburg pincus", "Enterprise, Consumer, Healthcare, Financial Services"),
    ("jasper ridge partners", "Enterprise, Consumer"),
    ("estee lauder", "Consumer, Beauty, Fashion"),
    ("avanta ventures", "Insurance, InsurTech"),
    ("dolby family ventures", "Media, Entertainment, Technology"),
    ("geolo capital", "Consumer, Enterprise, Technology"),
    ("h.i.g. capital|hig capital", "Enterprise, Consumer, Healthcare"),
    ("kbw ventures", "Enterprise, Consumer, Technology"),
    ("soros fund management|soros", "Enterprise, Consumer, Fintech"),
    ("rockefeller capital management|rockefeller", "Enterprise, Consumer, Sustainability"),
    ("edmond de rothschild", "Enterprise, Consumer, Financial Services"),
    ("bessemer trust company na|bessemer trust", "Enterprise, Consumer"),
    ("oak hill capital partners|oak hill capital", "Enterprise, Consumer, Media"),
    ("vulcan capital|vulcan", "Enterprise, Consumer, Sustainability, Space"),
    ("acrew capital|acrew", "Enterprise, Consumer, AI"),
    ("wildcat vc|wildcat venture partners", "Enterprise, Consumer"),
    ("signia|signia venture partners", "Enterprise, Consumer, AI"),
    ("quake vc|quake capital", "Enterprise, Consumer"),
    ("engage vc|engage", "Consumer, Enterprise"),
    ("basecamp fund", "Enterprise, Consumer"),
    ("female founder collective", "Consumer, Enterprise"),
    ("invicta growth", "Enterprise, Consumer"),
    ("lumia capital", "Enterprise, Consumer, Deep Tech"),
    ("lateral capital", "Enterprise, Consumer"),
    ("halogen capital|halogen ventures", "Consumer, Enterprise"),
    ("mehta ventures", "Enterprise, Consumer, Technology"),
    ("tenOneten|tenOneten ventures", "Enterprise, Consumer, AI"),
    ("epiq capital group|epiq capital", "Enterprise, Consumer"),
    ("corigin|corigin ventures", "Real Estate, PropTech"),
    ("pruven capital", "Enterprise, Consumer"),
    ("rtp ventures|rtp global", "Enterprise, Consumer, Fintech"),
    ("jumpspeed|jumpspeed ventures", "Enterprise, Consumer"),
    ("work play ventures", "Consumer, Enterprise, Gaming"),
    ("bellco capital", "Enterprise, Consumer"),
    ("provenio capital", "Enterprise, Consumer"),
    ("ironwood capital management|ironwood capital", "Enterprise, Consumer"),
    ("shinnecock partners", "Enterprise, Consumer"),
    # Family offices with known focus
    ("emerson collective", "Social Impact, Education, Media, Healthcare"),
    ("google ventures|gv", "Enterprise, Healthcare, Consumer, AI"),
    ("wavemaker partners", "Enterprise, Deep Tech"),
    ("1517 fund", "Education, Deep Tech, Consumer"),
    ("dorm room fund", "Enterprise, Consumer"),
    ("rough draft ventures", "Enterprise, Consumer"),
    ("nextview ventures|nextview", "Consumer, Enterprise"),
    ("resolute ventures", "Enterprise, Consumer"),
    # More VCs
    ("acceleprise|forum ventures", "Enterprise, SaaS"),
    ("factore ventures", "Enterprise, Consumer"),
    ("courageous ventures", "Social Impact, Consumer"),
    ("longjourney ventures|long journey ventures", "Enterprise, Consumer"),
    ("vhf ventures", "Enterprise, Consumer"),
    ("crista galli ventures", "Enterprise, Consumer"),
    ("magarac venture partners", "Enterprise, Consumer, Industrial"),
    ("squad ventures", "Enterprise, Consumer"),
    ("red beard ventures", "Crypto, Web3"),
    ("openseed vc|openseed", "Enterprise, Consumer"),
    ("grant barco capital", "Enterprise, Consumer"),
    ("polymath capital partners|polymath capital", "Enterprise, Consumer"),
    ("lynett capital", "Enterprise, Consumer"),
    ("gravis capital", "Enterprise, Consumer"),
    # Well-known accelerators/studios
    ("angelpad", "Enterprise, Consumer, SaaS"),
    ("plug and play", "Enterprise, Consumer, SaaS"),
    ("dreamit ventures|dreamit", "Enterprise, Consumer, Healthcare"),
    ("mhs capital", "Enterprise, Consumer"),
    ("500 global", "Enterprise, Consumer, SaaS, Fintech"),
    ("launch|launch accelerator", "Enterprise, Consumer"),
    ("alchemist accelerator|alchemist", "Enterprise, SaaS"),
    # Corporate VCs
    ("microsoft ventures|microsoft m12", "Enterprise, AI, Cloud"),
    ("google|alphabet", "Enterprise, AI, Consumer, Cloud"),
    ("nvidia", "AI, GPU, Deep Tech, Robotics"),
    ("ibm ventures", "Enterprise, AI, Cloud"),
    ("stripe", "Fintech, Payments, SaaS"),
    # Additional
    ("ulu ventures", "Enterprise, Consumer"),
    ("all raise", "Enterprise, Consumer"),
    ("cake ventures", "Consumer, Enterprise"),
    ("dream ventures", "Consumer, Enterprise"),
    ("cross culture ventures|cross culture", "Consumer, Enterprise, Media"),
    ("springbank collective", "Consumer, Enterprise"),
    ("signal peak ventures|signal peak", "Enterprise, SaaS"),
    ("pelion venture partners|pelion", "Enterprise, SaaS"),
    ("kickstart fund|kickstart", "Enterprise, Consumer, SaaS"),
    ("renaissance venture capital fund|renaissance venture capital", "Enterprise, Consumer"),
    ("azure capital", "Enterprise, Consumer, Healthcare"),
    ("northleaf capital partners|northleaf capital", "Enterprise, Consumer"),
    ("monochrome capital", "Enterprise, Consumer"),
    ("exodus capital", "Enterprise, Consumer"),
    ("neon adventures|neon", "Consumer, Enterprise"),
    # More specific ones
    ("ecoprosperity capital", "Clean Tech, Sustainability"),
    ("wakestream ventures", "Enterprise, Consumer"),
    ("bluestein ventures", "Enterprise, Consumer"),
    ("quantum ventures", "Enterprise, Consumer, Deep Tech"),
    ("chetrit ventures", "Real Estate, Enterprise"),
    ("intonation ventures", "Enterprise, Consumer"),
    ("frontcourt ventures", "Enterprise, Consumer, Sports"),
    ("adit ventures", "Enterprise, Consumer, Technology"),
    ("pirque ventures", "Enterprise, Consumer"),
    ("gniteXL ventures", "Enterprise, Consumer"),
    ("saltwater capital", "Enterprise, Consumer"),
    ("soar capital", "Enterprise, Consumer"),
    ("shiro capital", "Enterprise, Consumer"),
    ("csi ventures", "Enterprise, Consumer"),
    ("cambridge ventures", "Enterprise, Consumer"),
    ("capital trust group", "Enterprise, Consumer, Financial Services"),
    ("investcorp", "Enterprise, Consumer, Technology"),
    ("tavistock group", "Enterprise, Consumer, Real Estate, Sports"),
    ("smedvig capital", "Enterprise, Consumer, Technology"),
    ("devonshire partners", "Enterprise, Consumer"),
    ("otb capital", "Enterprise, Consumer"),
    ("drd capital", "Enterprise, Consumer"),
    ("andesite capital management|andesite capital", "Enterprise, Consumer"),
    ("dorado peak capital", "Enterprise, Consumer"),
    ("ikigai ventures", "Enterprise, Consumer"),
    ("north range ventures", "Enterprise, Consumer"),
    ("enter capital", "Enterprise, Consumer"),
    ("carolwood capital management|carolwood capital", "Enterprise, Consumer"),
    ("summer hill venture partners|summer hill", "Enterprise, Consumer"),
    ("holbrook ventures", "Enterprise, Consumer"),
    ("colt ventures", "Enterprise, Consumer"),
    ("rocky point ventures", "Enterprise, Consumer"),
    ("auxano ventures", "Enterprise, Consumer"),
    ("sumo ventures", "Enterprise, Consumer"),
    ("tyden ventures", "Enterprise, Consumer"),
    ("vogl ventures", "Enterprise, Consumer"),
    ("redo ventures", "Enterprise, Consumer"),
    ("dolik ventures", "Enterprise, Consumer"),
    ("mellon stud ventures", "Enterprise, Consumer"),
    ("sm ventures", "Enterprise, Consumer"),
    ("dig ventures", "Enterprise, Consumer"),
    ("murphy family ventures", "Enterprise, Consumer"),
    ("leto ventures", "Enterprise, Consumer"),
    ("nimble ventures", "Enterprise, Consumer"),
    ("gen3 ventures", "Enterprise, Consumer"),
    ("premanco ventures", "Enterprise, Consumer"),
    ("h/l ventures", "Enterprise, Consumer"),
    ("morpheus ventures", "Enterprise, Consumer"),
    ("baruch future ventures", "Enterprise, Consumer"),
    ("concordia ventures", "Enterprise, Consumer"),
    ("set wave capital", "Enterprise, Consumer"),
    ("strand partners", "Enterprise, Consumer"),
    ("three fields capital", "Enterprise, Consumer"),
    ("cruttenden partners", "Enterprise, Consumer"),
    ("vilcap investments", "Social Impact, Enterprise"),
    ("pointu capital", "Enterprise, Consumer"),
    ("presidium partners", "Enterprise, Consumer"),
    ("willcrest partners", "Enterprise, Consumer"),
    ("tamar capital", "Enterprise, Consumer"),
    ("buena vista fund management|buena vista fund", "Enterprise, Consumer"),
    ("medley partners", "Enterprise, Consumer"),
    ("nolan capital", "Enterprise, Consumer"),
    ("s-cubed capital", "Enterprise, Consumer"),
    ("growth capital management", "Enterprise, Consumer"),
    ("northtower capital", "Enterprise, Consumer"),
    ("true capital management", "Enterprise, Consumer"),
    ("k2 capital", "Enterprise, Consumer"),
    ("coughlin capital", "Enterprise, Consumer"),
    ("prideco capital management", "Enterprise, Consumer"),
    ("davis capital partners", "Enterprise, Consumer"),
    ("big rock partners", "Enterprise, Consumer"),
    ("portola creek capital", "Enterprise, Consumer"),
    ("soho capital", "Enterprise, Consumer"),
    ("the k fund", "Enterprise, Consumer"),
    ("wu capital", "Enterprise, Consumer"),
]

for entry in _fund_data:
    names_str, sectors = entry
    for name in names_str.split('|'):
        KNOWN_FUNDS[name.strip().lower()] = sectors

# ── Well-known investors → sectors ──────────────────────────────────────────
KNOWN_INVESTORS = {}
_investor_data = [
    ("marc andreessen", "Enterprise, Consumer, Crypto, AI"),
    ("ben horowitz", "Enterprise, Consumer, Crypto, AI"),
    ("peter thiel", "Deep Tech, Enterprise, Consumer"),
    ("reid hoffman", "Enterprise, Consumer, AI"),
    ("vinod khosla", "Deep Tech, Healthcare, AI, Sustainability"),
    ("john doerr", "Enterprise, Consumer, Healthcare, Sustainability"),
    ("mary meeker", "Enterprise, Consumer, Healthcare"),
    ("bill gurley", "Enterprise, Consumer, Marketplace"),
    ("chris sacca", "Consumer, Enterprise"),
    ("keith rabois", "Enterprise, Consumer, Real Estate"),
    ("naval ravikant", "Enterprise, Consumer, Crypto"),
    ("paul graham", "Enterprise, Consumer, SaaS"),
    ("sam altman", "AI, Enterprise, Consumer"),
    ("fred wilson", "Consumer, Fintech, Crypto, Marketplace"),
    ("brad feld", "Enterprise, SaaS"),
    ("jason calacanis", "Enterprise, Consumer, AI"),
    ("tim draper", "Enterprise, Consumer, Crypto"),
    ("esther dyson", "Healthcare, Enterprise"),
    ("ron conway", "Consumer, Enterprise, SaaS"),
    ("alexis ohanian", "Consumer, Enterprise, Crypto"),
    ("garry tan", "Enterprise, Consumer, SaaS"),
    ("michael moritz", "Enterprise, Consumer"),
    ("roelof botha", "Enterprise, Consumer, Fintech"),
    ("jeff jordan", "Consumer, Marketplace, E-commerce"),
    ("arlan hamilton", "Consumer, Enterprise, SaaS"),
    ("kirsten green", "Consumer, DTC, Retail, E-commerce"),
    ("ann miura-ko", "Enterprise, Consumer"),
    ("aileen lee", "Enterprise, Consumer, AI"),
    ("jeff bezos", "Consumer, Enterprise, Space, AI"),
    ("elon musk", "AI, Space, Clean Tech, Enterprise"),
    ("mark cuban", "Consumer, Enterprise, Healthcare"),
    ("ashton kutcher", "Consumer, Enterprise, Media"),
    ("david sacks", "Enterprise, Consumer, Fintech, Crypto"),
    ("chamath palihapitiya", "Enterprise, Consumer, Healthcare"),
    ("max levchin", "Fintech, Consumer"),
    ("jack dorsey", "Fintech, Consumer, Crypto"),
    ("brian armstrong", "Crypto, Fintech"),
    ("joe lonsdale", "Enterprise, Deep Tech, Healthcare, Defense"),
    ("ev williams", "Consumer, Media, Publishing"),
    ("brian chesky", "Consumer, Travel, Marketplace"),
    ("patrick collison", "Fintech, Enterprise, SaaS"),
    ("tobi lutke", "E-commerce, Consumer, Enterprise"),
    ("mo koyfman", "Consumer, Enterprise, Media"),
    ("theresia gouw", "Enterprise, Consumer, AI, Security"),
    ("brianne kimmel", "Enterprise, SaaS, Consumer"),
    ("vinny lingham", "Crypto, Consumer, Enterprise"),
    ("spencer rascoff", "Real Estate, PropTech, Consumer"),
    ("scooter braun", "Media, Entertainment, Consumer"),
    ("ron suber", "Fintech, Financial Services"),
    ("rahul vohra", "Enterprise, SaaS, Consumer"),
    ("pejman nozad", "Enterprise, Consumer"),
    ("mark pincus", "Consumer, Gaming, Enterprise"),
    ("marlon nichols", "Consumer, Enterprise"),
    ("lan xuezhao", "AI, Enterprise"),
    ("john lilly", "Enterprise, Consumer"),
    ("jesse draper", "Consumer, Enterprise"),
    ("josh kushner", "Consumer, Healthcare, Enterprise"),
    ("susan lyne", "Consumer, Enterprise, Media"),
    ("eva ho", "AI, Enterprise, Consumer"),
    ("hunter walk", "Consumer, Enterprise"),
    ("charles hudson", "Consumer, Enterprise"),
    ("lo toney", "Enterprise, Consumer"),
    ("satya patel", "Enterprise, Consumer"),
    ("semil shah", "Enterprise, Consumer"),
    ("manu kumar", "Enterprise, Consumer, AI"),
    ("jenny lee", "Enterprise, Consumer"),
    ("hans tung", "Enterprise, Consumer, E-commerce"),
    ("will smith", "Consumer, Media, Entertainment"),
    ("jay-z|shawn carter", "Consumer, Cannabis, Media, Entertainment"),
    ("serena williams", "Consumer, Enterprise"),
    ("steph curry|stephen curry", "Consumer, Enterprise"),
    ("kevin durant", "Consumer, Enterprise, Media"),
    ("robert downey jr", "Sustainability, Clean Tech"),
    ("palmer luckey", "Defense, VR/AR"),
    ("steve chen", "Consumer, Media, Video"),
    ("daniel ek", "Consumer, Music, Media"),
    ("drew houston", "Enterprise, Consumer, Cloud"),
    ("nick pritzker|nicholas pritzker", "Enterprise, Consumer, Technology"),
    ("divesh makan", "Enterprise, Consumer, Technology"),
    ("matthew jacobson", "Enterprise, Consumer, Technology"),
    ("kevin foster", "Enterprise, Consumer, Technology"),
    ("pascal levensohn|pascal levenson", "Media, Entertainment, Technology"),
    ("ginger rothrock", "Sustainability, Clean Tech, Energy"),
    ("sara jones", "Aerospace, Defense, Technology, AI"),
    ("oliver libby", "Enterprise, Consumer"),
    ("amanda eilian", "Consumer, Enterprise"),
    ("tom baruch", "Enterprise, Consumer, Deep Tech"),
    ("sue xu", "AI, Enterprise, Data"),
    ("doug scott", "Enterprise, Consumer"),
    ("christian hernandez", "Enterprise, Consumer, Fintech"),
    ("yuri sagalov", "Enterprise, Consumer, AI"),
    ("skip fleshman", "Enterprise, Consumer"),
    ("raymond tonsing", "Enterprise, Consumer"),
    ("soona amhaz", "Crypto, Blockchain, Web3"),
    ("richard wolpert", "Consumer, Media, Entertainment"),
    ("rachel springate", "Consumer, Enterprise"),
    ("pradeep aswani", "Enterprise, Consumer"),
    ("panos papadopoulos", "Consumer, Media, Gaming"),
    ("morgan schwanke", "Enterprise, Consumer"),
    ("pascal levy-garboua", "Enterprise, Consumer, Fintech"),
    ("ian doody", "Clean Tech, Energy"),
    ("joseph miller", "Enterprise, Consumer"),
    ("oliver samwer", "E-commerce, Consumer, Marketplace"),
]

for entry in _investor_data:
    names_str, sectors = entry
    for name in names_str.split('|'):
        KNOWN_INVESTORS[name.strip().lower()] = sectors

# ── Keyword patterns for fund-name inference ────────────────────────────────
KEYWORD_RULES = [
    (re.compile(r'\b(health|bio|life\s*sci|genom|medic|pharma|therapeut|oncolog|biopharma)\b', re.I),
     "Healthcare, Life Sciences, Biotech"),
    (re.compile(r'\bai\b|artificial\s*intell|machine\s*learn|deep\s*learn', re.I),
     "AI, Machine Learning"),
    (re.compile(r'\bdata\b', re.I),
     "AI, Data"),
    (re.compile(r'\b(fintech|fin\s*vc|financial\s*tech)\b', re.I),
     "Fintech, Financial Services"),
    (re.compile(r'\b(consumer|brand[s]?|dtc|direct.to.consumer|retail)\b', re.I),
     "Consumer, DTC, Retail"),
    (re.compile(r'\b(clean\s*tech|climate|green|sustainab|carbon|decarboni)\b', re.I),
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
    (re.compile(r'\b(social)\b', re.I),
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
    (re.compile(r'\b(water)\b', re.I),
     "Water Solutions, Clean Tech"),
    (re.compile(r'\b(impact|social\s*good|tech\s*for\s*good)\b', re.I),
     "Social Impact"),
]

# Words too generic to infer sector
SKIP_GENERIC = re.compile(
    r'^(capital|ventures?|partners?|group|fund|management|holdings|investment[s]?|'
    r'equity|llc|llp|inc|co|company|the|global|international|advisors?|associates?|'
    r'growth|labs?|studio[s]?|collective|alliance|network|first|new|next|one|two|'
    r'three|four|five|six|seven|eight|nine|ten|angel|angels?|vc|trust|wealth|'
    r'private|office|family|advisers?|limited|corp|corporation|na|of|and|&|'
    r'managing|director|ceo|cfo|cto|coo|president|chairman|founder|'
    r'mr|mrs|ms|dr|jr|sr|ii|iii|iv|'
    r'north|south|east|west|upper|lower|'
    r'asset|assets|financial|consulting|services|solutions|'
    r'point|hill|rock|stone|wood|lake|river|mountain|valley|creek|ridge|peak|'
    r'oak|pine|maple|cedar|elm|willow|birch|'
    r'blue|red|green|black|white|silver|golden|amber|'
    r'alpha|beta|gamma|delta|epsilon|'
    r'advisories|counsel|fiduciary)$',
    re.I
)


def normalize(s):
    if not s:
        return ""
    return re.sub(r'\s+', ' ', s.replace('\n', ' ').replace('\r', ' ').replace('"', '').strip()).lower()


def lookup_fund(fund_raw):
    fund = normalize(fund_raw)
    if not fund:
        return None
    # Direct match
    if fund in KNOWN_FUNDS:
        return KNOWN_FUNDS[fund]
    # Strip common suffixes
    for suffix in [', llc', ', inc', ', inc.', ' llc', ' inc', ' inc.', ', ltd', ' ltd',
                   ', lp', ' lp', ', l.p.', ' l.p.', ' na', ', na']:
        if fund.endswith(suffix):
            fund = fund[:-len(suffix)].strip()
            if fund in KNOWN_FUNDS:
                return KNOWN_FUNDS[fund]
    # Try without common trailing words
    for suffix in [' ventures', ' capital', ' partners', ' fund', ' vc', ' group',
                   ' management', ' llc', ' inc', ' advisors', ' advisory']:
        if fund.endswith(suffix):
            base = fund[:-len(suffix)].strip()
            if base in KNOWN_FUNDS:
                return KNOWN_FUNDS[base]
    # Try adding common suffixes
    for suffix in [' ventures', ' capital', ' partners', ' fund']:
        augmented = fund + suffix
        if augmented in KNOWN_FUNDS:
            return KNOWN_FUNDS[augmented]
    return None


def lookup_investor(name_raw):
    name = normalize(name_raw)
    if not name:
        return None
    if name in KNOWN_INVESTORS:
        return KNOWN_INVESTORS[name]
    return None


def infer_from_keywords(fund_raw, name_raw, website_raw=""):
    texts = []
    if fund_raw:
        texts.append(normalize(fund_raw))
    # Also check website URL for clues
    if website_raw:
        ws = normalize(website_raw)
        # Extract domain keywords
        ws_clean = re.sub(r'https?://(www\.)?', '', ws)
        ws_clean = re.sub(r'\.(com|co|io|vc|org|net|fund|capital|ventures|ai|tech|health).*', '', ws_clean)
        texts.append(ws_clean)
    
    combined = ' '.join(texts)
    if not combined.strip():
        return None
    
    words = combined.split()
    meaningful = [w for w in words if not SKIP_GENERIC.match(w)]
    meaningful_text = ' '.join(meaningful)
    
    if not meaningful_text.strip():
        return None
    
    sectors = []
    for pattern, sector_string in KEYWORD_RULES:
        if pattern.search(meaningful_text):
            sectors.append(sector_string)
    
    if sectors:
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
    with open(INPUT, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    reader = csv.DictReader(io.StringIO(content))
    fieldnames = reader.fieldnames
    rows = list(reader)
    total = len(rows)
    
    already_filled = sum(1 for r in rows if r.get(SECTOR_COL, '').strip())
    print(f"Total rows: {total}")
    print(f"Already have sector data: {already_filled} ({already_filled*100/total:.1f}%)")
    
    filled_by_fund_lookup = 0
    filled_by_investor_lookup = 0
    filled_by_keyword = 0
    
    for row in rows:
        existing = row.get(SECTOR_COL, '').strip()
        if existing:
            continue
        
        fund = row.get(FUND_COL, '') or ''
        name = row.get(NAME_COL, '') or ''
        website = row.get(WEBSITE_COL, '') or ''
        
        # Skip URL-only fund names
        fund_clean = fund.strip()
        if fund_clean.startswith('http'):
            fund_clean = ''
        
        # 1. Fund lookup
        result = lookup_fund(fund_clean)
        if result:
            row[SECTOR_COL] = result
            filled_by_fund_lookup += 1
            continue
        
        # 2. Investor name lookup
        result = lookup_investor(name)
        if result:
            row[SECTOR_COL] = result
            filled_by_investor_lookup += 1
            continue
        
        # 3. Keyword inference (fund name + website)
        result = infer_from_keywords(fund_clean, name, website)
        if result:
            row[SECTOR_COL] = result
            filled_by_keyword += 1
            continue
    
    now_filled = sum(1 for r in rows if r.get(SECTOR_COL, '').strip())
    
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
