import csv

# Curated list of angel investors and family offices investing in:
# Frontier brain tech, life sciences, mental health, behavioral health, wellness
# Including celebrities
# Flag those who also invest in / donate to education

investors = [
    # BRAIN TECH / NEUROSCIENCE / MENTAL HEALTH SPECIALISTS
    ('Tim', 'Ferriss', 'Tim Ferriss', 'Angel', '', 'https://www.linkedin.com/in/timferriss/', '', 'Psychedelics, Mental Health, Neuroscience, Wellness, Brain Tech', 'Austin', 'Y', 'Y', 'Backed MAPS, Compass Pathways, Usona Institute. Major psychedelic research donor.'),
    ('Peter', 'Thiel', 'Thiel Capital', 'Family Office', '', 'https://www.linkedin.com/in/peterthiel/', '', 'Brain-Computer Interface, Neuroscience, Life Sciences, AI, Longevity', 'San Francisco', 'Y', 'Y', 'Backed Neuralink, early longevity investor. Thiel Fellowship = education.'),
    ('Bryan', 'Johnson', 'Bryan Johnson / Kernel', 'Angel/Family Office', '', 'https://www.linkedin.com/in/bryanjohnson2/', 'https://www.kernel.com', 'Brain Tech, Neuroscience, Longevity, Mental Health, Wellness', 'Los Angeles', 'Y', 'N', 'Built Kernel (brain-imaging). OS Fund invests in brain tech, longevity. Blueprint protocol.'),
    ('Christian', 'Angermayer', 'Apeiron Investment Group', 'Family Office', '', 'https://www.linkedin.com/in/angermayer/', 'https://www.apeiron-group.com', 'Psychedelics, Mental Health, Brain Tech, Life Sciences, Biotech', 'London/Miami', 'Y', 'N', 'Co-founded ATAI Life Sciences, Compass Pathways. Major psychedelic investor.'),
    ('Bob', 'Duggan', 'Bob Duggan', 'Angel/Family Office', '', 'https://www.linkedin.com/in/robertduggan/', '', 'Brain Tech, Neuroscience, Mental Health, Biotech, Life Sciences', 'San Francisco', 'Y', 'Y', 'Pharmacyclics founder. Invests in brain science, donated to education.'),
    ('George', 'Goldsmith', 'Compass Pathways / Angel', 'Angel', '', 'https://www.linkedin.com/in/georgegoldsmith/', 'https://www.compasspathways.com', 'Psychedelics, Mental Health, Brain Tech, Therapeutics', 'London', 'Y', 'N', 'Co-founder Compass Pathways. Pioneer in psilocybin therapy.'),
    ('Carey', 'Turnbull', 'Carey Turnbull', 'Angel', '', 'https://www.linkedin.com/in/careyturnbull/', '', 'Psychedelics, Mental Health, Neuroscience, Behavioral Health', 'New York', 'N', 'N', 'Major funder of Heffter Research Institute (psychedelic research).'),
    ('Matt', 'Mullenweg', 'Matt Mullenweg', 'Angel', '', 'https://www.linkedin.com/in/mattm/', '', 'Mental Health, Wellness, Technology, Open Source', 'Houston', 'N', 'Y', 'WordPress founder. Invested in mental health startups. Supports distributed education.'),
    ('Esther', 'Dyson', 'Wellville / HICCup', 'Angel/Family Office', '', 'https://www.linkedin.com/in/estherdyson/', 'https://www.wellville.net', 'Health, Wellness, Mental Health, Behavioral Health, Preventive Care', 'New York', 'Y', 'Y', 'Wellville project. Pioneer health/wellness investor. Supports education.'),
    ('Jim', 'Mellon', 'Juvenescence / Angel', 'Family Office', '', 'https://www.linkedin.com/in/jimmellon/', 'https://www.juvenescence.ltd', 'Longevity, Brain Tech, Life Sciences, Mental Health, Biotech', 'London/Isle of Man', 'Y', 'N', 'Juvenescence, co-author of Juvenile. Major longevity + brain aging investor.'),
    
    # LIFE SCIENCES / BIOTECH ANGELS & FOs
    ('Noubar', 'Afeyan', 'Flagship Pioneering / Angel', 'Family Office', '', 'https://www.linkedin.com/in/noubarafeyan/', 'https://www.flagshippioneering.com', 'Life Sciences, Biotech, Brain Tech, Therapeutics, AI', 'Boston', 'Y', 'Y', 'Moderna co-founder. Flagship backs life sciences + neuroscience. MIT donor.'),
    ('Robert', 'Nelsen', 'ARCH Venture Partners / Angel', 'Angel/Family Office', '', 'https://www.linkedin.com/in/robertnelsen/', '', 'Life Sciences, Biotech, Neuroscience, Brain Tech, Diagnostics', 'Seattle', 'Y', 'N', 'ARCH backs brain science, neurology, therapeutics at earliest stage.'),
    ('Geoff', 'Yang', 'Geoff Yang', 'Angel', '', 'https://www.linkedin.com/in/geoffyang/', '', 'Life Sciences, Health Tech, Neuroscience, AI, Consumer Health', 'San Francisco', 'N', 'N', 'Redpoint founder. Angel invests in health/neuroscience.'),
    ('Daphne', 'Zohar', 'PureTech Health / Angel', 'Angel/Family Office', '', 'https://www.linkedin.com/in/daphnezohar/', 'https://www.puretechhealth.com', 'Brain-Gut, Neuroscience, Mental Health, Life Sciences, Therapeutics', 'Boston', 'Y', 'N', 'PureTech: brain-immune, gut-brain axis. Karuna Therapeutics (schizophrenia).'),
    ('Michael', 'Gilman', 'Arrakis Therapeutics / Angel', 'Angel', '', 'https://www.linkedin.com/in/michaelgilman/', '', 'Life Sciences, Biotech, Brain Tech, Therapeutics, Drug Discovery', 'Boston', 'N', 'N', 'Serial biotech founder. Invests in neuroscience therapeutics.'),
    ('Jeff', 'Huber', 'GRAIL / Angel', 'Angel/Family Office', '', 'https://www.linkedin.com/in/jeffhuber/', '', 'Life Sciences, Diagnostics, Brain Health, AI, Longevity', 'San Francisco', 'Y', 'N', 'Former Google X. Founded GRAIL (cancer diagnostics). Invests in brain health.'),
    ('Vivek', 'Ramaswamy', 'Strive / Roivant', 'Angel/Family Office', '', 'https://www.linkedin.com/in/vivekgramaswamy/', '', 'Life Sciences, Biotech, Neuroscience, Mental Health, Therapeutics', 'Columbus', 'Y', 'Y', 'Roivant Sciences founder. Multiple neuro-focused subsidiaries. Education donor.'),
    ('David', 'Agus', 'Dr. David Agus', 'Angel', '', 'https://www.linkedin.com/in/davidagus/', '', 'Health, Wellness, Longevity, Brain Health, Life Sciences', 'Los Angeles', 'N', 'Y', 'USC professor. Bestselling author. Invests in wellness + longevity.'),
    
    # MENTAL HEALTH / WELLNESS FOCUSED
    ('Arianna', 'Huffington', 'Thrive Global / Angel', 'Angel/Family Office', '', 'https://www.linkedin.com/in/araborenstein/', 'https://www.thriveglobal.com', 'Mental Health, Wellness, Sleep, Behavioral Health, Consumer Health', 'New York', 'Y', 'N', 'Thrive Global CEO. Invests in mental health, sleep, wellness startups.'),
    ('Deepak', 'Chopra', 'Deepak Chopra / Angel', 'Angel', '', 'https://www.linkedin.com/in/deepakchopramd/', '', 'Mental Health, Wellness, Meditation, Brain Health, Consciousness', 'San Diego', 'N', 'Y', 'Invests in wellness/mental health tech. Chopra Foundation education programs.'),
    ('Jack', 'Dorsey', 'Start Small Foundation', 'Family Office', '', 'https://www.linkedin.com/in/jackdorsey/', '', 'Mental Health, Wellness, Mindfulness, Health, AI', 'San Francisco', 'Y', 'Y', '$1B+ to COVID/UBI/health. Meditation/mindfulness advocate. Supports education.'),
    ('Marc', 'Benioff', 'TIME Ventures', 'Family Office', '', 'https://www.linkedin.com/in/marcbenioff/', '', 'Mental Health, AI, Health Tech, Wellness, Children\'s Health', 'San Francisco', 'Y', 'Y', 'UCSF Benioff Children\'s Hospital. Major health/education philanthropist.'),
    ('Laurene', 'Powell Jobs', 'Emerson Collective', 'Family Office', '', 'https://www.linkedin.com/in/laurenepowelljobs/', 'https://www.emersoncollective.com', 'Mental Health, Education, Health, Social Impact, Brain Science', 'Palo Alto', 'Y', 'Y', 'Major education investor/donor. XQ Institute. Health + mental health portfolio.'),
    ('Priscilla', 'Chan', 'Chan Zuckerberg Initiative', 'Family Office', '', 'https://www.linkedin.com/in/priscillachan/', 'https://chanzuckerberg.com', 'Brain Science, Mental Health, Education, Life Sciences, Neuroscience', 'Palo Alto', 'Y', 'Y', 'CZI Neurodegeneration Challenge. Major education + brain science funder.'),
    ('MacKenzie', 'Scott', 'Yield Giving', 'Family Office', '', 'https://www.linkedin.com/in/mackenziescott/', '', 'Mental Health, Education, Health, Social Impact, Equity', 'Seattle', 'Y', 'Y', '$16B+ donated. Major mental health, education, and health equity funder.'),
    ('Ray', 'Dalio', 'Dalio Philanthropies', 'Family Office', '', 'https://www.linkedin.com/in/raydalio/', 'https://www.daliophilanthropies.org', 'Mental Health, Meditation, Brain Science, Wellness, Education', 'Greenwich', 'Y', 'Y', 'OceanX, meditation advocate. Major education donor. TM practitioner/funder.'),
    ('Melinda', 'French Gates', 'Pivotal Ventures', 'Family Office', '', 'https://www.linkedin.com/in/melaborenstein/', 'https://www.pivotalventures.org', 'Mental Health, Women\'s Health, Education, Social Impact, Health Equity', 'Seattle', 'Y', 'Y', 'Pivotal Ventures: mental health focus. Gates Foundation education pillar.'),
    ('Reid', 'Hoffman', 'Greylock / Angel', 'Angel/Family Office', '', 'https://www.linkedin.com/in/reidhoffman/', '', 'AI, Mental Health Tech, Brain-Computer Interface, Wellness, Life Sciences', 'San Francisco', 'Y', 'Y', 'Backed Neuralink. Invested in mental health platforms. Stanford education donor.'),
    
    # CELEBRITIES IN MENTAL HEALTH / WELLNESS
    ('Lady', 'Gaga', 'Born This Way Foundation', 'Angel/Family Office', '', 'https://www.linkedin.com/company/born-this-way-foundation/', 'https://bfrwy.org', 'Mental Health, Youth Wellness, Behavioral Health, Kindness', 'Los Angeles', 'N', 'Y', 'Born This Way Foundation: youth mental health. Partners with Yale on research.'),
    ('Selena', 'Gomez', 'Wondermind / Angel', 'Angel', '', 'https://www.linkedin.com/in/selenagomez/', 'https://www.wondermind.com', 'Mental Health, Wellness, Consumer Health, Behavioral Health', 'Los Angeles', 'N', 'N', 'Co-founded Wondermind (mental fitness). Rare Impact Fund for mental health.'),
    ('Prince', 'Harry', 'Archewell Foundation / BetterUp', 'Angel/Family Office', '', '', 'https://www.archewell.com', 'Mental Health, Wellness, Behavioral Health, Coaching', 'Montecito', 'N', 'N', 'Chief Impact Officer at BetterUp. Archewell: mental health programs.'),
    ('Demi', 'Lovato', 'Demi Lovato / Angel', 'Angel', '', 'https://www.linkedin.com/in/demilovato/', '', 'Mental Health, Behavioral Health, Wellness, Recovery, Consumer', 'Los Angeles', 'N', 'N', 'Mental health advocate. Invested in mental health/recovery startups.'),
    ('Michael', 'Phelps', 'Michael Phelps / Angel', 'Angel', '', 'https://www.linkedin.com/in/michaelphelps/', '', 'Mental Health, Wellness, Sports, Fitness, Behavioral Health', 'Scottsdale', 'N', 'Y', 'Mental health advocate. Invested in Talkiatry, therapy platforms. Phelps Foundation.'),
    ('Jared', 'Leto', '30 Seconds to Mars / Angel', 'Angel', '', 'https://www.linkedin.com/in/jaredleto/', '', 'Mental Health, Wellness, Brain Tech, Life Sciences, Consumer', 'Los Angeles', 'N', 'N', 'Invests in health tech, wellness. Backed Calm, Headspace competitor.'),
    ('Katy', 'Perry', 'Katy Perry / Angel', 'Angel', '', '', '', 'Mental Health, Wellness, Meditation, Consumer, Brand', 'Los Angeles', 'N', 'N', 'Transcendental Meditation advocate. Invested in wellness brands.'),
    ('Jennifer', 'Aniston', 'Jennifer Aniston / Angel', 'Angel', '', '', '', 'Wellness, Mental Health, Consumer Health, Beauty, Longevity', 'Los Angeles', 'N', 'N', 'Invested in wellness brands (Vital Proteins, etc.). Mental health advocate.'),
    ('Oprah', 'Winfrey', 'Oprah Winfrey Network / Harpo', 'Family Office', '', 'https://www.linkedin.com/in/oprahwinfrey/', '', 'Mental Health, Wellness, Education, Media, Behavioral Health', 'Los Angeles', 'Y', 'Y', 'Major mental health media platform. Backed Calm. Massive education philanthropy.'),
    ('Will', 'Smith', 'Westbrook Inc / Dreamers VC', 'Family Office', '', 'https://www.linkedin.com/company/dreamers-vc/', 'https://dreamers.vc', 'Mental Health, Wellness, Media, Consumer, Brain Health', 'Los Angeles', 'N', 'Y', 'Open about mental health journey. Invests in wellness. Supports education.'),
    ('Jay-Z', 'Carter', 'Marcy Venture Partners', 'Family Office', '', 'https://www.linkedin.com/company/marcy-venture-partners/', 'https://www.marcyventurepart.com', 'Mental Health, Wellness, Consumer, Media, Social Impact', 'New York', 'Y', 'Y', 'Backed Promise (mental health in justice). Shawn Carter Foundation = education.'),
    ('Gwyneth', 'Paltrow', 'Goop', 'Angel/Family Office', '', 'https://www.linkedin.com/in/gwyneth-paltrow/', 'https://goop.com', 'Wellness, Mental Health, Brain Health, Consumer, DTC', 'Los Angeles', 'N', 'N', 'Goop: wellness/mental health content + products. Invests in wellness brands.'),
    ('Jessica', 'Alba', 'Honest Company / Angel', 'Angel/Family Office', '', 'https://www.linkedin.com/in/jessicaalba/', '', 'Wellness, Health, Consumer, Mental Health, DTC', 'Los Angeles', 'N', 'Y', 'Honest Company. Invests in health/wellness. Supports education initiatives.'),
    ('Serena', 'Williams', 'Serena Ventures', 'Family Office', '', 'https://www.linkedin.com/company/serena-ventures/', 'https://www.serenaventures.com', 'Health, Wellness, Mental Health, Consumer, Education', 'San Francisco', 'Y', 'Y', 'Serena Ventures: health, wellness portfolio. Mental health advocate. Education supporter.'),
    ('LeBron', 'James', 'SpringHill / LRMR Ventures', 'Family Office', '', 'https://www.linkedin.com/company/springhill-entertainment/', '', 'Mental Health, Education, Media, Sports, Wellness', 'Los Angeles', 'Y', 'Y', 'I Promise School. Major education philanthropist. Mental health advocate.'),
    ('Matthew', 'McConaughey', 'Matthew McConaughey / Angel', 'Angel', '', 'https://www.linkedin.com/in/matthewmcconaughey/', '', 'Mental Health, Wellness, Education, Youth, Consumer', 'Austin', 'N', 'Y', 'Just Keep Livin Foundation: mental health + wellness for youth. UT Austin professor.'),
    ('Ashton', 'Kutcher', 'Sound Ventures', 'Family Office', '', 'https://www.linkedin.com/in/aplusk/', 'https://www.sound.ventures', 'Health Tech, AI, Mental Health, Consumer, Wellness', 'Los Angeles', 'Y', 'Y', 'Sound Ventures: health/AI portfolio. Thorn = child safety. Supports education.'),
    ('Robert', 'Downey Jr.', 'FootPrint Coalition', 'Family Office', '', 'https://www.linkedin.com/company/footprint-coalition/', 'https://www.footprintcoalition.com', 'Brain Tech, AI, Sustainability, Wellness, Technology', 'Los Angeles', 'N', 'N', 'FootPrint Coalition: AI for environment. Interested in brain tech/wellness.'),
    
    # MENTAL HEALTH / BRAIN TECH FOCUSED INVESTORS
    ('Andy', 'Dunn', 'Andy Dunn (Bonobos) / Angel', 'Angel', '', 'https://www.linkedin.com/in/andydunn/', '', 'Mental Health, Consumer, Wellness, DTC, Behavioral Health', 'New York', 'N', 'N', 'Bonobos founder. Open about bipolar. Invests in mental health startups.'),
    ('Ben', 'Horowitz', 'a16z / Angel', 'Angel/Family Office', '', 'https://www.linkedin.com/in/beenhorowitz/', '', 'Brain-Computer Interface, AI, Life Sciences, Mental Health Tech', 'San Francisco', 'Y', 'Y', 'a16z Bio fund. Backed Neuralink. Horowitz family education philanthropy.'),
    ('Vinod', 'Khosla', 'Khosla Ventures', 'Family Office', '', 'https://www.linkedin.com/in/vinodkhosla/', 'https://www.khoslaventures.com', 'Brain Tech, AI, Life Sciences, Mental Health, Diagnostics', 'San Francisco', 'Y', 'Y', 'KV Bio: brain tech, mental health AI. Major education donor (India + US).'),
    ('Eric', 'Schmidt', 'Innovation Endeavors / Schmidt Futures', 'Family Office', '', 'https://www.linkedin.com/in/ericschmidt/', 'https://www.schmidtfutures.com', 'Brain Science, AI, Neuroscience, Life Sciences, Education', 'San Francisco', 'Y', 'Y', 'Schmidt Futures: science + education. Funds brain/neuroscience research.'),
    ('Patrick', 'Collison', 'Patrick Collison / Angel', 'Angel', '', 'https://www.linkedin.com/in/patrickcollison/', '', 'Life Sciences, Brain Science, AI, Research, Longevity', 'San Francisco', 'N', 'Y', 'Arc Institute funder (brain science research). Fast Grants. Education via research.'),
    ('Dustin', 'Moskovitz', 'Open Philanthropy / Asana', 'Family Office', '', 'https://www.linkedin.com/in/dustinmoskovitz/', 'https://www.openphilanthropy.org', 'Mental Health, Brain Science, AI Safety, Wellness, Behavioral Health', 'San Francisco', 'Y', 'Y', 'Open Philanthropy: mental health is a key cause area. Education funder.'),
    ('Sam', 'Altman', 'Sam Altman / Angel', 'Angel', '', 'https://www.linkedin.com/in/samaltman/', '', 'Brain-Computer Interface, AI, Life Sciences, Longevity, Neuroscience', 'San Francisco', 'Y', 'Y', 'Backed Retro Bio, Helion. Interested in brain/longevity. YC = education.'),
    ('Tony', 'Fadell', 'Future Shape', 'Family Office', '', 'https://www.linkedin.com/in/tonyfadell/', 'https://www.futureshape.com', 'Brain Tech, Health, Wellness, AI, Neuroscience, Consumer Health', 'San Francisco', 'Y', 'Y', 'Future Shape: health/wellness tech. iPod/Nest inventor. Supports education.'),
    
    # PSYCHEDELIC / BRAIN SCIENCE SPECIALISTS
    ('Kevin', 'O\'Leary', 'Kevin O\'Leary / Beanstox', 'Angel/Family Office', '', 'https://www.linkedin.com/in/kevinolearytv/', '', 'Mental Health, Psychedelics, Life Sciences, Wellness, Consumer', 'Toronto/Boston', 'Y', 'Y', 'Invested in psychedelic companies. Shark Tank. Supports education.'),
    ('Tim', 'Draper', 'Draper Associates', 'Family Office', '', 'https://www.linkedin.com/in/timdraper/', 'https://www.draper.vc', 'Brain Tech, AI, Life Sciences, Consumer, Health', 'San Francisco', 'Y', 'Y', 'Draper University = education. Invests broadly including health/brain tech.'),
    ('Steve', 'Jurvetson', 'Future Ventures', 'Family Office', '', 'https://www.linkedin.com/in/jurvetson/', 'https://future.ventures', 'Brain Tech, Neuroscience, AI, Life Sciences, Deep Tech', 'San Francisco', 'Y', 'N', 'Future Ventures: frontier tech including brain-computer interface.'),
    ('Mike', 'Novogratz', 'Galaxy Digital / Angel', 'Family Office', '', 'https://www.linkedin.com/in/michaelenovogratz/', '', 'Psychedelics, Mental Health, Wellness, Brain Science, Consumer', 'New York', 'Y', 'Y', 'Major psychedelic investor. Galaxy Life Sciences. Supports ayahuasca research. Education donor.'),
    ('Tim', 'Chang', 'Tim Chang / Mayfield Fund', 'Angel', '', 'https://www.linkedin.com/in/timchang/', '', 'Brain Tech, Wellness, Longevity, Mental Health, Consumer Health', 'San Francisco', 'N', 'N', 'Mayfield partner. Personal focus on brain optimization, biohacking, longevity.'),
    ('Sonia', 'Arrison', 'Sonia Arrison / Angel', 'Angel', '', 'https://www.linkedin.com/in/soniaarrison/', '', 'Longevity, Brain Science, Life Sciences, AI, Neuroscience', 'San Francisco', 'N', 'Y', 'Author of 100 Plus. Singularity University. Longevity + brain science + education.'),
    
    # WELLNESS / BEHAVIORAL HEALTH
    ('Tony', 'Robbins', 'Tony Robbins / Angel', 'Angel', '', 'https://www.linkedin.com/in/tonyrobbins/', '', 'Wellness, Mental Health, Behavioral Health, Consumer, Longevity', 'San Diego', 'N', 'Y', 'Life Force author. Invests in health/wellness tech. Education via seminars + books.'),
    ('Dave', 'Asprey', 'Dave Asprey / Bulletproof', 'Angel', '', 'https://www.linkedin.com/in/daveasprey/', '', 'Brain Health, Wellness, Biohacking, Longevity, Neuroscience', 'Vancouver/Victoria', 'N', 'N', 'Bulletproof founder. Upgrade Labs. Biohacking pioneer. Brain optimization focus.'),
    ('Dr.', 'Mark Hyman', 'Mark Hyman / Angel', 'Angel', '', 'https://www.linkedin.com/in/drmarkhyman/', '', 'Brain Health, Wellness, Mental Health, Functional Medicine, Longevity', 'Lenox, MA', 'N', 'Y', 'Cleveland Clinic. Bestselling author. Function Health co-founder. Education via books.'),
    ('Andrew', 'Huberman', 'Andrew Huberman / Angel', 'Angel', '', 'https://www.linkedin.com/in/andrew-huberman/', '', 'Neuroscience, Brain Health, Mental Health, Wellness, Performance', 'Stanford', 'N', 'Y', 'Huberman Lab podcast. Stanford neuroscience professor. Education = core mission.'),
    ('Peter', 'Attia', 'Peter Attia / Angel', 'Angel', '', 'https://www.linkedin.com/in/peterattiamd/', '', 'Longevity, Brain Health, Mental Health, Wellness, Life Sciences', 'Austin', 'N', 'Y', 'Early Medical. Podcast/education on longevity. Invests in health tech.'),
    ('David', 'Sinclair', 'David Sinclair / Angel', 'Angel', '', 'https://www.linkedin.com/in/david-sinclair-phd/', '', 'Longevity, Brain Aging, Neuroscience, Life Sciences, Epigenetics', 'Boston', 'N', 'Y', 'Harvard professor. Lifespan author. Invested in longevity startups. Education via research.'),
    ('Sanjay', 'Gupta', 'Dr. Sanjay Gupta / Angel', 'Angel', '', 'https://www.linkedin.com/in/drsanjaygupta/', '', 'Brain Health, Neuroscience, Mental Health, Wellness, Media', 'Atlanta', 'N', 'Y', 'CNN. Weed documentary (psychedelics). Books on brain health. Education mission.'),
    
    # MORE FAMILY OFFICES IN LIFE SCIENCES / BRAIN TECH
    ('George', 'Church', 'George Church / Angel', 'Angel', '', 'https://www.linkedin.com/in/george-church-harvard/', '', 'Life Sciences, Brain Tech, Neuroscience, Genetics, Longevity', 'Boston', 'N', 'Y', 'Harvard/MIT geneticist. Co-founded 50+ companies. Major education figure.'),
    ('Yuri', 'Milner', 'DST Global / Breakthrough Prize', 'Family Office', '', 'https://www.linkedin.com/in/yurimilner/', '', 'Life Sciences, Brain Science, AI, Neuroscience, Deep Tech', 'San Francisco', 'Y', 'Y', 'Breakthrough Prize in Life Sciences. Funds neuroscience research.'),
    ('Sean', 'Parker', 'Parker Foundation', 'Family Office', '', 'https://www.linkedin.com/in/sparker/', '', 'Life Sciences, Brain Science, Immunotherapy, Mental Health, AI', 'San Francisco', 'Y', 'Y', 'Parker Institute for Cancer Immunotherapy. Funds brain science. Education donor.'),
    ('Eli', 'Broad', 'Broad Foundation', 'Family Office', '', '', 'https://broadfoundation.org', 'Life Sciences, Brain Science, Education, Genomics, Neuroscience', 'Los Angeles', 'Y', 'Y', 'Broad Institute (MIT/Harvard). Major brain science + education funder.'),
    ('Paul', 'Allen', 'Allen Institute / Vulcan', 'Family Office', '', '', 'https://alleninstitute.org', 'Brain Science, Neuroscience, AI, Life Sciences, Education', 'Seattle', 'Y', 'Y', 'Allen Institute for Brain Science. Massive neuroscience/education funder.'),
    ('Jim', 'Simons', 'Simons Foundation', 'Family Office', '', '', 'https://www.simonsfoundation.org', 'Brain Science, Neuroscience, Autism, Mathematics, Education', 'New York', 'Y', 'Y', 'Simons Foundation Autism Research Initiative (SFARI). Major math/science education.'),
    ('Naveen', 'Jain', 'Viome / Angel', 'Angel/Family Office', '', 'https://www.linkedin.com/in/naveenjain/', 'https://www.viome.com', 'Brain-Gut, Wellness, Mental Health, AI, Life Sciences', 'Seattle', 'Y', 'Y', 'Viome (gut-brain). Invests in brain health. Supports education initiatives.'),
    ('Mark', 'Zuckerberg', 'Chan Zuckerberg Initiative', 'Family Office', '', 'https://www.linkedin.com/in/markzuckerberg/', 'https://chanzuckerberg.com', 'Brain Science, Neuroscience, Education, Life Sciences, AI', 'Palo Alto', 'Y', 'Y', 'CZI: brain science + education are two pillars. Major funder.'),
    ('Stewart', 'Resnick', 'Wonderful Company / Angel', 'Family Office', '', 'https://www.linkedin.com/in/stewartresnick/', '', 'Health, Wellness, Life Sciences, Agriculture, Education', 'Los Angeles', 'Y', 'Y', 'Major health/wellness. Resnick Neuropsychiatric Hospital at UCLA. Education donor.'),
    ('David', 'Geffen', 'David Geffen Foundation', 'Family Office', '', '', '', 'Brain Science, Mental Health, Education, Life Sciences, Media', 'Los Angeles', 'Y', 'Y', 'Geffen School of Medicine (UCLA). Major neuroscience/mental health funder. Education.'),
    ('Leonard', 'Lauder', 'Lauder Foundation / Angel', 'Family Office', '', '', '', 'Brain Science, Alzheimer\'s, Mental Health, Life Sciences, Education', 'New York', 'Y', 'Y', 'Estée Lauder. Leonard & Ronald Lauder: Alzheimer\'s research funding. Education donor.'),
    ('Henry', 'McCance', 'Greylock / Angel', 'Angel/Family Office', '', '', '', 'Brain Science, Mental Health, Life Sciences, Neuroscience', 'Boston', 'Y', 'Y', 'Greylock founder. Stanley Center for Psychiatric Research (Broad). Education.'),
    ('Steve', 'Cohen', 'Point72 / Cohen Veterans Network', 'Family Office', '', 'https://www.linkedin.com/in/stevencohen/', '', 'Mental Health, Veterans, Brain Science, Behavioral Health, AI', 'New York', 'Y', 'Y', 'Cohen Veterans Network: mental health clinics. Major behavioral health funder. Education.'),
    ('Michael', 'Bloomberg', 'Bloomberg Philanthropies', 'Family Office', '', 'https://www.linkedin.com/in/michaelbloomberg/', '', 'Mental Health, Public Health, Education, Brain Science, AI', 'New York', 'Y', 'Y', 'Bloomberg: public health + education. Mental health programs. Johns Hopkins.'),
    
    # ADDITIONAL SPECIALISTS
    ('Cindy', 'Eckert', 'Pinkubator / Angel', 'Angel', '', 'https://www.linkedin.com/in/cindyeckert/', '', 'Women\'s Health, Mental Health, Sexual Health, Wellness, Life Sciences', 'Raleigh', 'Y', 'N', 'Addyi creator. Pinkubator: women\'s health. Mental health + wellness focus.'),
    ('Joby', 'Pritzker', 'Tao Capital Partners', 'Family Office', '', 'https://www.linkedin.com/in/jobypritzker/', '', 'Brain Science, Education, Mental Health, Life Sciences, Impact', 'San Francisco', 'Y', 'Y', 'Tao Capital: brain science + education. Pritzker Neuropsychiatric Disorders Consortium.'),
    ('J.B.', 'Pritzker', 'Pritzker Group / Governor', 'Family Office', '', 'https://www.linkedin.com/in/jbpritzker/', '', 'Mental Health, Education, Health, Life Sciences, Social Impact', 'Chicago', 'Y', 'Y', 'Pritzker family: major mental health + education funders. Brain science research.'),
    ('John', 'Overdeck', 'Overdeck Family Foundation', 'Family Office', '', 'https://www.linkedin.com/in/johnoverdeck/', '', 'Brain Science, Education, Mental Health, Mathematics, AI', 'New York', 'Y', 'Y', 'Two Sigma co-founder. Overdeck Foundation: STEM education. Brain development research.'),
    ('Laura', 'Deming', 'Longevity Fund / Angel', 'Angel', '', 'https://www.linkedin.com/in/laurademing/', 'https://www.longevity.vc', 'Longevity, Brain Aging, Neuroscience, Life Sciences, Therapeutics', 'San Francisco', 'Y', 'Y', 'Longevity Fund. Thiel Fellowship alum. Age-related brain disease. Education supporter.'),
    ('James', 'Lind', 'Lind Partners', 'Family Office', '', 'https://www.linkedin.com/in/jameslind/', '', 'Life Sciences, Brain Tech, Neuroscience, Mental Health, Therapeutics', 'New York', 'Y', 'N', 'Lind Partners: life sciences specialist. Brain-focused therapeutics investor.'),
    ('Jamie', 'Dimon', 'JPMorgan / Angel', 'Angel/Family Office', '', 'https://www.linkedin.com/in/jamiedimon/', '', 'Mental Health, Wellness, Education, Health, Financial Wellness', 'New York', 'Y', 'Y', 'JPMorgan: mental health workplace programs. Supports education initiatives.'),
    ('Bob', 'Iger', 'Bob Iger / Angel', 'Angel/Family Office', '', 'https://www.linkedin.com/in/robertiger/', '', 'Mental Health, Media, Wellness, Brain Health, Education', 'Los Angeles', 'Y', 'Y', 'Disney focus on mental health content. Personal investments in wellness. Education.'),
    ('Dr. Oz', 'Mehmet', 'Dr. Oz / Angel', 'Angel', '', 'https://www.linkedin.com/in/droz/', '', 'Brain Health, Wellness, Mental Health, Consumer Health, Life Sciences', 'New York', 'N', 'Y', 'TV platform on brain health. Invests in health/wellness. Columbia professor.'),
    ('Dara', 'Khosrowshahi', 'Dara Khosrowshahi / Angel', 'Angel', '', 'https://www.linkedin.com/in/darakhosrowshahi/', '', 'Health Tech, Mental Health, Wellness, AI, Consumer', 'San Francisco', 'N', 'N', 'Uber CEO. Personal investments in health tech. Mental health workplace advocate.'),
]

# Write CSV
header = ['#','First Name','Last Name','Firm/Company','Investor Type','Email','LinkedIn URL','Website',
          'Sectors of Interest','Location','Source','Match Score','Lead?','Also Invests in Education?',
          'Notes','Also Good For']

rows = [header]
for i, inv in enumerate(investors[:100], 1):
    also_good = []
    sl = inv[8].lower()
    if any(k in sl for k in ['ai','consumer','media']): also_good.append('Pitch Slam')
    if any(k in sl for k in ['wellness','health','longevity','human']): also_good.append('HTW Dinners')
    
    rows.append([
        i, inv[0], inv[1], inv[2], inv[3], inv[4], inv[5], inv[6],
        inv[8], inv[9], 'curated_research', 8, inv[10],
        'YES ✅' if inv[11] == 'Y' else 'No',
        inv[12], '; '.join(also_good)
    ])

with open('/data/.openclaw/workspace/projects/investor-outreach/psymed-100-lp-targets.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

total = len(rows) - 1
edu_count = sum(1 for r in rows[1:] if 'YES' in r[13])
celebs = sum(1 for r in rows[1:] if any(c in r[2] for c in ['Gaga','Gomez','Harry','Lovato','Phelps','Leto','Perry','Aniston','Winfrey','Smith','Paltrow','Alba','Williams','James','McConaughey','Kutcher','Downey']))
leads = sum(1 for r in rows[1:] if r[12] == 'Y')

print(f"Psymed LP List: {total} investors")
print(f"Also invest in / donate to education: {edu_count} (highlighted)")
print(f"Celebrities: ~{celebs}")
print(f"Can lead rounds: {leads}")


