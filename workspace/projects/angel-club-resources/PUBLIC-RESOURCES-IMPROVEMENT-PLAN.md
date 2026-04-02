# Angel Club Public Resources Master List — Improvement Plan & Execution Guide

**Created:** April 2, 2026
**Purpose:** Transform the Angel Club Public Resources Google Sheet into the definitive free resource for founders from idea stage to Series A — while preserving the value gap that makes the Members-Only Master Investor Database (12,000+ investors) worth paying for.
**Status:** Planning

---

## Table of Contents

1. [Current State Assessment](#1-current-state-assessment)
2. [Rules & Constraints](#2-rules--constraints)
3. [Phase 1: Data Cleanup](#3-phase-1-data-cleanup)
4. [Phase 2: Tab Audit & Enhancement](#4-phase-2-tab-audit--enhancement)
5. [Tab-by-Tab Blueprint](#5-tab-by-tab-blueprint)
6. [Free Databases & Lists (Tab 11 Deep Dive)](#6-free-databases--lists-deep-dive)
7. [Platform Recommendation](#7-platform-recommendation)
8. [SEO & AI Discovery Strategy](#8-seo--ai-discovery-strategy)
9. [Traffic & Growth Strategy](#9-traffic--growth-strategy)
10. [What Else Is Missing](#10-what-else-is-missing)
11. [Execution Timeline](#11-execution-timeline)
12. [Maintenance Cadence](#12-maintenance-cadence)

---

## 1. Current State Assessment

### What We Know (from Tab 1 API access)
- **~100 entries** in the primary VC/investor tab, mostly diversity-focused funds
- **Columns:** Name, Sector, Geographic Focus, Link, Notes
- **Header rows** link to Angel Club events, WhatsApp group, newsletter, syndicate, banking, legal, SPVs
- **Problems identified:**
  - Duplicates (Precursor Ventures ×3, Everywhere Ventures ×2, others)
  - Individual investor names mixed with fund names
  - Missing website URLs on many entries
  - Notes misaligned (wrong entry)
  - Some broken URLs
  - No pitch submission URLs
  - No standardized format

### What We Don't Know Yet
- **The sheet has additional tabs beyond the investor list.** We could only access Tab 1 via API. Before executing this plan:

> ⚠️ **ACTION REQUIRED:** Manually audit ALL existing tabs in the Google Sheet. Some of the categories below (accelerators, events, books, etc.) may already exist in partial form. The strategy should be **enhance what exists + add what's missing**, not rebuild from scratch.

### Audit Checklist (Before Execution)
For each existing tab, document:
- [ ] Tab name
- [ ] Number of entries
- [ ] Column headers
- [ ] Data quality (completeness, accuracy, freshness)
- [ ] What's missing vs. the blueprint below
- [ ] Duplicates or errors

---

## 2. Rules & Constraints

### Non-Negotiable (Angel's Rules)
| Rule | Rationale |
|------|-----------|
| ❌ No emails | Private — members-only benefit |
| ❌ Don't rival the Master DB | 12,000+ investors is the premium product |
| ✅ Add pitch submission URLs | High value, publicly available |
| ✅ Remove individual investors | Keep funds/firms only |
| ✅ Add all resource categories | Accelerators, fellowships, events, etc. |
| ✅ Optimize for SEO + AI discovery | Drive traffic to Angel Club |

### Value Gap Strategy
The public list should be **wide but shallow** on investors. The Master DB is **deep and actionable**. Specifically:

| Dimension | Public List | Master DB (Members) |
|-----------|------------|-------------------|
| VC Funds | ~150–200 curated | 12,000+ with contacts |
| Contact Info | Website + pitch URL only | Emails, LinkedIn, intro paths |
| Check Size | General range | Specific amounts |
| Portfolio | Not included | Full portfolio data |
| Warm Intros | Not available | Available via network |
| Other Resources | Comprehensive | — |

The public list wins on **breadth of categories** (accelerators, events, books, tools, etc.). The Master DB wins on **depth of investor data**.

---

## 3. Phase 1: Data Cleanup (Tab 1 — VC Funds & Angel Groups)

### 3.1 Remove Duplicates
Known duplicates to merge:
- Precursor Ventures (3 entries → 1)
- Everywhere Ventures (2 entries → 1)
- Full duplicate audit needed across all entries

**Process:** Sort alphabetically → scan for exact and near-matches → merge, keeping the most complete data from each duplicate.

### 3.2 Remove Individual Investors
Scan for entries that are person names rather than fund/firm names. Remove them. If a person runs a notable fund, keep the fund name and remove the individual name.

**Examples of what to remove:** Individual angel investors listed by personal name
**Examples of what to keep:** Fund names, even if eponymous (e.g., "Lowercase Capital" stays)

### 3.3 Fix & Standardize URLs
- Test every URL for 404s/redirects
- Standardize format: `https://` prefix, no trailing slashes
- Fill in missing URLs via web search

### 3.4 Add "Pitch URL" Column
For each fund, check if they have a public pitch submission page. Common patterns:
- Website `/apply` or `/pitch` or `/submit` pages
- Typeform/Google Form links
- AngelList deal flow pages

### 3.5 Standardize Column Format
**Recommended columns for Tab 1:**

| Column | Format | Example |
|--------|--------|---------|
| Fund Name | Text | Precursor Ventures |
| Stage Focus | Tags | Pre-Seed, Seed |
| Sector Focus | Tags | Fintech, Health, Generalist |
| Check Size | Range | $100K–$2M |
| Geographic Focus | Text | US, Global |
| Diversity Focus | Tags | Black, Latinx, Women, LGBTQ+, None |
| Website | URL | https://precursorvc.com |
| Pitch URL | URL | https://precursorvc.com/pitch |
| Location | City, State/Country | San Francisco, CA, USA |
| Notes | Text | Led by Charles Hudson |

### 3.6 Data Cleanup Checklist
- [ ] Export current tab as backup
- [ ] Sort A-Z by Fund Name
- [ ] Identify and merge all duplicates
- [ ] Remove individual investor names
- [ ] Test all URLs (use a link checker tool or script)
- [ ] Add missing URLs
- [ ] Research and add pitch submission URLs
- [ ] Add Location column and populate
- [ ] Add Check Size where publicly available
- [ ] Standardize all Sector/Stage tags
- [ ] Final review pass

---

## 4. Phase 2: Tab Audit & Enhancement

### Target Tab Structure (13 tabs + 1 bonus)

| Tab # | Tab Name | Priority | Notes |
|-------|----------|----------|-------|
| 1 | VC Funds & Angel Groups | 🔴 High | Clean existing |
| 2 | Accelerators | 🔴 High | May partially exist |
| 3 | Startup Competitions 2026 | 🔴 High | NEW — high SEO value |
| 4 | Demo Days 2026 | 🔴 High | Time-sensitive, high value |
| 5 | Fellowships | 🟡 Medium | Niche but valuable |
| 6 | Venture Studios | 🟡 Medium | Growing category |
| 7 | Incubators | 🟡 Medium | May overlap with accelerators |
| 8 | Events & Conferences 2026 | 🔴 High | Time-sensitive |
| 9 | Grants & Awards | 🔴 High | Free money = high demand |
| 10 | Books | 🟢 Low | Evergreen, easy to build |
| 11 | Blogs & Newsletters | 🟢 Low | Evergreen |
| 12 | Podcasts | 🟢 Low | Evergreen |
| 13 | Free Databases & Lists | 🟡 Medium | Meta-resource |
| 14 | Tools & Templates | 🟡 Medium | High utility |

### Audit-First Approach
For each tab above:
1. **Check if tab already exists** in the sheet
2. **If yes:** Compare against the blueprint below → add missing columns, fill gaps, clean data
3. **If no:** Create new tab using the blueprint below

---

## 5. Tab-by-Tab Blueprint

### Tab 1: VC Funds & Angel Groups
*(See Phase 1 above for cleanup plan)*

**Columns:**
Fund Name | Stage Focus | Sector Focus | Check Size | Geographic Focus | Diversity Focus | Website | Pitch URL | Location | Notes

**Target:** 150–200 curated funds (not more — protect the Master DB value)

**Example Entries (30 to seed/validate):**

| Fund Name | Stage Focus | Sector Focus | Check Size | Geographic Focus | Diversity Focus | Location | Website | Pitch URL |
|-----------|------------|--------------|------------|-----------------|----------------|----------|---------|-----------|
| Precursor Ventures | Pre-Seed, Seed | Generalist | $100K–$2M | US | Black, Latinx | San Francisco, CA, USA | https://precursorvc.com | https://precursorvc.com/startup/ |
| Backstage Capital | Pre-Seed, Seed | Generalist | $25K–$500K | US | Black, Women, LGBTQ+ | Los Angeles, CA, USA | https://backstagecapital.com | — |
| Harlem Capital | Seed, Series A | Generalist | $1M–$3M | US | Black, Latinx | New York, NY, USA | https://www.harlemcapital.com | https://www.harlemcapital.com/submit |
| Kapor Capital | Seed, Series A | Tech for Social Impact | $250K–$2M | US | Diverse | Oakland, CA, USA | https://www.kaporcapital.com | https://www.kaporcapital.com/how-we-invest/ |
| Everywhere Ventures | Pre-Seed, Seed | Generalist | $100K–$500K | Global | General | New York, NY, USA | https://everywhere.vc | — |
| Slauson & Co | Pre-Seed, Seed | Consumer, Fintech | $100K–$500K | US | Black, Latinx | Los Angeles, CA, USA | https://www.slausonco.com | — |
| MaC Venture Capital | Seed, Series A | Enterprise, Consumer | $500K–$5M | US | Black, Latinx | Los Angeles, CA, USA | https://macventurecapital.com | — |
| Lightship Capital | Seed | Generalist | $100K–$1M | US (Midwest) | Black, Women, LGBTQ+ | Cincinnati, OH, USA | https://www.lightshipcapital.com | — |
| Collab Capital | Pre-Seed, Seed | Generalist | $100K–$500K | US | Black | Atlanta, GA, USA | https://www.collabcapital.com | https://www.collabcapital.com/apply |
| Fearless Fund | Pre-Seed, Seed | Generalist | $50K–$1M | US | Women of Color | Atlanta, GA, USA | https://www.fearless.fund | — |
| Base10 Partners | Seed, Series A, B | Tech (Automation) | $1M–$10M | US, Global | Diverse | San Francisco, CA, USA | https://base10.vc | — |
| Impact America Fund | Seed, Series A | Fintech, Health, Workforce | $250K–$2M | US | Diverse | Oakland, CA, USA | https://impactamericafund.com | — |
| Cross Culture Ventures | Seed | Consumer, Culture | $250K–$1M | US | Black, Latinx | Los Angeles, CA, USA | https://www.crossculturevc.com | — |
| Rethink Impact | Series A, B | Deep Tech, Climate | $1M–$15M | US | Women | San Francisco, CA, USA | https://rethinkimpact.com | — |
| Gaingels | Seed, Series A | Generalist | $100K–$500K | US | LGBTQ+ | New York, NY, USA | https://gaingels.com | — |
| Techstars Ventures | Seed | Generalist | $120K (standard) | Global | General | Boulder, CO, USA | https://www.techstars.com | https://www.techstars.com/accelerators |
| 500 Global | Pre-Seed, Seed | Generalist | $50K–$250K | Global | General | San Francisco, CA, USA | https://500.co | https://500.co/accelerator |
| Antler | Pre-Seed | Generalist | $100K–$250K | Global | General | Singapore | https://www.antler.co | https://www.antler.co/apply |
| First Round Capital | Seed | Tech | $500K–$5M | US | General | San Francisco, CA, USA | https://firstround.com | https://firstround.com/pitch/ |
| Floodgate | Seed | Tech | $250K–$2M | US | General | Palo Alto, CA, USA | https://floodgate.com | — |
| Hustle Fund | Pre-Seed | Generalist | $25K–$250K | US, Global | General | San Francisco, CA, USA | https://www.hustlefund.vc | https://www.hustlefund.vc/apply |
| Unshackled Ventures | Pre-Seed, Seed | Immigrant Founders | $500K–$2M | US | Immigrant | San Francisco, CA, USA | https://www.unshackledvc.com | https://www.unshackledvc.com/apply |
| Plug and Play | Seed | Generalist | $25K–$500K | Global | General | Sunnyvale, CA, USA | https://www.plugandplaytechcenter.com | https://www.plugandplaytechcenter.com/join/ |
| SOSV | Pre-Seed, Seed | DeepTech, Climate, Health | $50K–$250K | Global | General | Princeton, NJ, USA | https://sosv.com | https://sosv.com/apply |
| Founders Fund | Seed, Series A+ | Tech | $500K–$50M | US | General | San Francisco, CA, USA | https://foundersfund.com | — |
| Initialized Capital | Seed | Tech | $250K–$5M | US | General | San Francisco, CA, USA | https://initialized.com | — |
| Sequoia Capital (Scout/Arc) | Seed, Series A+ | Tech | $500K–$100M+ | US, Global | General | Menlo Park, CA, USA | https://www.sequoiacap.com | https://www.sequoiacap.com/arc/ |
| a]16z (START) | Seed | Tech | Varies | US | General | Menlo Park, CA, USA | https://a16z.com | https://a16z.com/pitchbook/ |
| Emerson Collective | Seed, Series A | Impact, Education, Climate | $500K–$5M | US | General | Palo Alto, CA, USA | https://www.emersoncollective.com | — |
| Obvious Ventures | Seed, Series A | Climate, Health, Sustainability | $500K–$10M | US | General | San Francisco, CA, USA | https://obvious.com | — |

**Sources for more:**
- Crunchbase (free tier for basic fund profiles)
- OpenVC
- NVCA member directory
- VC firm websites directly
- AngelList fund pages

**Update frequency:** Quarterly (check for new funds, update URLs, verify active status)

---

### Tab 2: Accelerators (Global)

**Columns:**
Program Name | Organizer | Stage | Sector Focus | Investment/Stipend | Equity Taken | Duration | Location | Region | Application URL | Deadline | Cohort Timing | Notes

**30 Example Entries:**

| Program Name | Organizer | Stage | Sector | Investment | Equity | Duration | Location | Region | Application URL |
|-------------|-----------|-------|--------|-----------|--------|----------|----------|--------|----------------|
| Y Combinator | YC | Idea–Seed | Generalist | $500K | 7% | 3 months | San Francisco, CA | North America | https://www.ycombinator.com/apply |
| Techstars (Multi-City) | Techstars | Seed | Generalist | $120K | 6% | 3 months | Multiple (40+ cities) | Global | https://www.techstars.com/accelerators |
| 500 Global | 500 Global | Pre-Seed–Seed | Generalist | $150K | 6% | 4 months | San Francisco / Global | Global | https://500.co/accelerator |
| Antler | Antler | Pre-Seed | Generalist | $100K–$250K | ~10% | 3–6 months | 27+ cities | Global | https://www.antler.co/apply |
| Plug and Play | Plug and Play | Seed | Multi-vertical | No equity standard | Varies | 3 months | Sunnyvale, CA + global | Global | https://www.plugandplaytechcenter.com/join |
| MassChallenge | MassChallenge | Early Stage | Generalist | $0 (prizes up to $100K+) | 0% | 4 months | Boston, Mexico, Israel, Switzerland | Global | https://masschallenge.org/programs |
| SOSV (HAX, IndieBio, Chinaccelerator, MOX) | SOSV | Pre-Seed | Deep Tech, Bio, Cross-Border | $150K–$500K | 7–10% | 3–6 months | Multiple | Global | https://sosv.com/apply |
| Seedcamp | Seedcamp | Pre-Seed–Seed | Tech | €100K–€475K | ~7.5% | Ongoing | London, UK | Europe | https://seedcamp.com/apply |
| Entrepreneur First | EF | Pre-Team | Tech | $80K–$125K | 10% | 6 months | London, Paris, Berlin, Bangalore, Singapore, Toronto | Global | https://www.joinef.com/apply |
| Startupbootcamp | SBC | Seed | Multi-vertical | €15K–€20K | 8% | 3 months | Multiple | Europe, Asia, Africa | https://www.startupbootcamp.org/apply |
| Station F (Fighters Program) | Station F | Early Stage | Generalist | Free workspace | 0% | 1 year | Paris, France | Europe | https://stationf.co/programs |
| Techstars Farm to Fork | Techstars + Cargill | Seed | AgriFood | $120K | 6% | 3 months | Minneapolis, MN | North America | https://www.techstars.com/accelerators |
| Google for Startups Accelerator | Google | Growth | AI, ML, Cloud | $0 (credits + mentorship) | 0% | 3–6 months | Multiple | Global | https://startup.google.com/programs/ |
| Microsoft for Startups (Founders Hub) | Microsoft | All stages | Tech | $0 (up to $350K credits) | 0% | Ongoing | Virtual | Global | https://www.microsoft.com/en-us/startups |
| AWS Activate | Amazon | All stages | Tech | $0 (up to $100K credits) | 0% | Ongoing | Virtual | Global | https://aws.amazon.com/activate/ |
| NVIDIA Inception | NVIDIA | Growth | AI, Deep Learning | $0 (credits + support) | 0% | Ongoing | Virtual | Global | https://www.nvidia.com/en-us/startups/ |
| Alchemist Accelerator | Alchemist | Seed | Enterprise B2B | $25K | Varies | 6 months | San Francisco, CA | North America | https://alchemistaccelerator.com/apply |
| Dreamit Ventures | Dreamit | Seed–Series A | HealthTech, UrbanTech, SecureTech | $0–$50K | 0–6% | 4 months | Philadelphia / NYC / Virtual | North America | https://www.dreamit.com/apply |
| Founders Factory | Founders Factory | Pre-Seed–Seed | Multi-vertical | £30K–£60K | 5–7% | 6 months | London, UK | Europe, Africa | https://foundersfactory.com/apply |
| Flat6Labs | Flat6Labs | Pre-Seed–Seed | Generalist | $30K–$120K | 5–10% | 4 months | Cairo, Riyadh, Abu Dhabi, Tunis, Bahrain | MENA | https://flat6labs.com/apply |
| Chinaccelerator (SOSV) | SOSV | Seed | Cross-Border (China+) | $150K | 7% | 4 months | Shanghai, China | Asia | https://chinaccelerator.com/apply |
| JFDI Asia | JFDI | Seed | Generalist | $50K | ~8% | 100 days | Singapore | Southeast Asia | https://jfdi.asia |
| Startmate | Startmate | Pre-Seed–Seed | Generalist | A$120K | 7.5% | 3 months | Sydney / Melbourne | Australia/NZ | https://www.startmate.com/accelerator |
| Creative Destruction Lab | CDL | Seed | Deep Tech, AI, Health | $0 (mentorship) | 0% | 9 months | Toronto + multiple | Global | https://creativedestructionlab.com/program |
| Parallel18 | P18 (Puerto Rico govt) | Growth | Generalist | $40K–$75K | 0% | 5 months | San Juan, Puerto Rico | Latin America + Global | https://www.parallel18.com/apply |
| Start-Up Chile | CORFO | Pre-Seed–Seed | Generalist | $30K–$100K | 0% | 6 months | Santiago, Chile | Latin America | https://startupchile.org/apply |
| CyLon (Plexal) | Plexal | Seed | Cybersecurity | £15K | ~5% | 3 months | London, UK | Europe | https://cylonlab.com/apply |
| Batch (by Numa) | Numa | Seed | AI, Deep Tech | €30K | ~4% | 4 months | Paris, France | Europe | https://www.numa.co |
| HAX (SOSV) | SOSV | Pre-Seed | Hardware, Robotics | $250K | 9% | 3–6 months | Shenzhen / Newark | Global | https://hax.co/apply |
| IndieBio (SOSV) | SOSV | Pre-Seed | Biotech, Life Science | $500K | 10% | 4 months | San Francisco / New York | Global | https://indiebio.co/apply |

**Sources for more:**
- Gust accelerator directory (https://gust.com)
- F6S accelerator listings
- Crunchbase accelerator/incubator search
- GAN (Global Accelerator Network) member list
- Seed-DB (historical)
- Each country's startup ecosystem reports

**Update frequency:** Semi-annually (check new programs, update deadlines, remove defunct)

---

### Tab 3: Startup Competitions 2026 (Global)

**Columns:**
Competition Name | Organizer | Deadline | Competition Date(s) | Prize Amount | Eligibility | Stage | Sector | Location | Region | Entry Fee | Website

**30+ Example Entries:**

| Competition Name | Organizer | Deadline | Dates | Prize | Eligibility | Stage | Sector | Location | Region | Fee | Website |
|-----------------|-----------|----------|-------|-------|-------------|-------|--------|----------|--------|-----|---------|
| TechCrunch Disrupt Startup Battlefield | TechCrunch | ~Jun 2026 | Oct 2026 | $100,000 | All startups | Seed–Series A | Tech | San Francisco, CA | North America | Free | https://techcrunch.com/events/disrupt/ |
| SXSW Pitch | SXSW | ~Nov 2025 | Mar 2026 | In-kind prizes + exposure | All startups | Early Stage | Tech, Health, Social | Austin, TX | North America | Free | https://www.sxsw.com/apply-to-participate/sxsw-pitch/ |
| Startup World Cup | Pegasus Tech Ventures | Rolling (regionals) | Sep 2026 | $1,000,000 | All startups | Seed–Growth | Generalist | San Francisco (Grand Finale) | Global | Free | https://www.startupworldcup.io |
| Rice Business Plan Competition | Rice University | ~Jan 2026 | Apr 2026 | $1,500,000+ (total) | Graduate student-led | Early Stage | Generalist | Houston, TX | North America | Free | https://rbpc.rice.edu |
| MIT $100K Entrepreneurship Competition | MIT | ~Feb 2026 | May 2026 | $100,000+ | MIT-affiliated | Idea–Seed | Tech | Cambridge, MA | North America | Free | https://www.mit100k.org |
| MassChallenge Global Finals | MassChallenge | Varies by program | Oct 2026 | $100,000+ (no equity) | All startups | Early–Growth | Generalist | Boston, MA | Global | Free | https://masschallenge.org |
| Global Startup Awards | Various | Rolling | Nov 2026 | Recognition + prizes | All startups | All stages | Generalist | Various (Grand Finale Europe) | Global | Free | https://globalstartupawards.com |
| Hult Prize | Hult International | ~Dec 2025 | Multiple 2026 | $1,000,000 | University teams | Idea | Social Enterprise | Global (regional → final) | Global | Free | https://www.hultprize.org |
| 43North | 43North | ~May 2026 | Oct 2026 | $5,000,000 (total) | All startups | Seed–Growth | Generalist | Buffalo, NY | North America | Free | https://www.43north.org |
| Pitch@Palace | Duke of York | Rolling | Varies | Network + exposure | All startups (UK/global) | Early Stage | Generalist | London, UK + global | Global | Free | https://pitchatpalace.com |
| Startup Grind Global Conference Pitch | Startup Grind | ~Jan 2026 | Apr 2026 | Investment + exposure | All startups | Early Stage | Tech | Redwood City, CA | Global | Varies | https://www.startupgrind.com/conference |
| Seedstars World Competition | Seedstars | Rolling (regional) | ~Nov 2026 | $500,000+ | Emerging market startups | Seed | Tech | Geneva (final) | Global (Emerging) | Free | https://www.seedstars.com |
| Get in the Ring | Get in the Ring | Rolling | Year-round | Investment + prizes | All startups | Seed–Growth | Generalist | Various | Global | Free | https://getinthering.co |
| Slush 100 Pitching Competition | Slush | ~Sep 2026 | Nov 2026 | Investment + exposure | All startups | Seed | Tech | Helsinki, Finland | Europe/Global | Free | https://www.slush.org |
| Web Summit PITCH | Web Summit | ~Aug 2026 | Nov 2026 | Exposure + prizes | All startups (<5 yrs, <$3M raised) | Seed–Series A | Tech | Lisbon, Portugal | Global | Varies | https://websummit.com/startups |
| GITEX Future Stars | GITEX | ~Jul 2026 | Oct 2026 | $200,000+ | All startups | Seed–Growth | Tech | Dubai, UAE | Global | Varies | https://www.gitex.com |
| Collision Pitch Competition | Collision | ~Feb 2026 | Jun 2026 | Exposure | All startups | Seed | Tech | Toronto, Canada | North America | Free | https://collisionconf.com |
| Arch Grants | Arch Grants | ~Mar 2026 | Jun 2026 | $50,000–$100,000 (non-dilutive) | Must relocate to St. Louis | Seed | Generalist | St. Louis, MO | North America | Free | https://archgrants.org |
| Amazon Alexa Next Stage | Amazon | Varies | Varies | $100,000+ | Alexa-integrated | Seed–Growth | Voice/AI | Virtual | Global | Free | — |
| Cartier Women's Initiative | Cartier | ~Jun 2026 | Oct 2026 | $100,000 (×7 regions) | Women founders | Seed–Growth | Social Impact | Global | Global | Free | https://www.cartierwomensinitiative.com |
| Chivas Venture (now paused — verify) | Chivas Regal | Verify | Verify | $1,000,000 | Social enterprises | Early Stage | Social Enterprise | Global | Global | Free | — |
| Village Capital VilCap Communities | Village Capital | Rolling | Rolling | $50,000+ | Underserved founders | Seed | Fintech, Health, Food, Climate | Multiple | Global | Free | https://vilcap.com |
| Diamond Challenge | University of Delaware | ~Jan 2026 | Mar 2026 | $100,000+ | High school + college | Idea | Generalist, Social | Newark, DE | North America | Free | https://diamondchallenge.org |
| GSEA (Global Student Entrepreneur Awards) | EO | ~Jan 2026 | Apr 2026 | $25,000+ | Student founders (undergrad) | Revenue-generating | Generalist | Various | Global | Free | https://gsea.org |
| Africa's Business Heroes | Alibaba Foundation | ~May 2026 | Nov 2026 | $1,500,000 (total) | African entrepreneurs | All stages | Generalist | Various (Africa) | Africa | Free | https://www.africabusinessheroes.org |
| MIT Enterprise Forum Arab Startup Competition | MIT Enterprise Forum | ~Jan 2026 | Apr 2026 | $160,000+ | MENA founders | Seed | Tech | Varies (MENA) | MENA | Free | https://www.mitarabcompetition.com |
| Falling Walls Venture | Falling Walls | ~Jul 2026 | Nov 2026 | €30,000 | Science-based startups | Seed | DeepTech, Science | Berlin, Germany | Global | Free | https://falling-walls.com/venture |
| Creative Business Cup | Creative Business Cup | ~Jun 2026 | Nov 2026 | Investment + mentorship | Creative industry startups | Seed | Creative Industries | Copenhagen, Denmark | Global | Free | https://creativebusinesscup.com |
| Hello Tomorrow Global Challenge | Hello Tomorrow | ~Jun 2026 | Mar 2027 | €100,000 | DeepTech startups | Seed | DeepTech | Paris, France | Global | Free | https://hello-tomorrow.org/global-challenge |
| Extreme Tech Challenge (XTC) | XTC | ~Feb 2026 | Jun 2026 | $5M+ (investment) | All startups | Seed–Growth | Impact Tech | San Francisco, CA | Global | Free | https://www.extremetechchallenge.org |
| European Innovation Council (EIC) Accelerator | European Commission | Multiple cuts/year | Ongoing | Up to €2.5M grant + €15M equity | EU-based startups | Seed–Growth | DeepTech, Green | Brussels (EU-wide) | Europe | Free | https://eic.ec.europa.eu |
| TiE50 Awards | TiE Silicon Valley | ~Mar 2026 | May 2026 | Recognition + mentorship | Tech startups | Growth | Tech | Santa Clara, CA | Global | $500+ | https://www.tiecon.org |

**Sources for more:**
- StartupCompete.co
- F6S competition listings
- University entrepreneurship center websites
- AngelList competitions
- Country/region startup ecosystem reports
- "Startup competition" Google alerts

**Update frequency:** Quarterly for deadlines; full refresh annually in Q4 for upcoming year

---

### Tab 4: Demo Days 2026 (Global)

**Columns:**
Program | Demo Day Date | Location | Virtual/In-Person | Open to Public? | Application Deadline (for startups) | Livestream URL | Region | Notes

**25 Example Entries:**

| Program | Demo Day Date | Location | Format | Public? | Application Deadline | Region |
|---------|--------------|----------|--------|---------|---------------------|--------|
| Y Combinator W26 | ~Mar 2026 | San Francisco, CA | Hybrid | Invite-only (livestream) | Oct 2025 | North America |
| Y Combinator S26 | ~Aug 2026 | San Francisco, CA | Hybrid | Invite-only (livestream) | Apr 2026 | North America |
| Techstars Multiple Programs | Varies (quarterly) | Multiple cities | Hybrid | Public (register) | Rolling | Global |
| 500 Global Batch | ~Apr/Oct 2026 | San Francisco, CA | Hybrid | Public | Rolling | Global |
| Antler Demo Days | Quarterly | 27+ cities | In-person + stream | Public | Rolling | Global |
| Seedcamp Demo Day | ~Jun 2026 | London, UK | In-person | Invite-only | Rolling | Europe |
| Entrepreneur First Demo Day | Quarterly | London, Singapore, etc. | Hybrid | Public | Rolling | Global |
| Plug and Play Summit | Quarterly | Sunnyvale, CA | In-person | Register | Rolling | Global |
| Alchemist Demo Day | ~Jun/Dec 2026 | San Francisco, CA | Invite-only | Investors only | Rolling | North America |
| IndieBio Demo Day | ~Jun/Dec 2026 | San Francisco / NYC | In-person | Public | Rolling | North America |
| HAX Demo Day | ~Jun/Dec 2026 | Newark, NJ / Shenzhen | In-person | Public | Rolling | Global |
| Startmate Demo Day | ~Jun/Dec 2026 | Sydney, Australia | Hybrid | Public | Rolling | Australia/NZ |
| Start-Up Chile Demo Day | ~Jun/Dec 2026 | Santiago, Chile | In-person | Public | Rolling | Latin America |
| Flat6Labs Demo Day | Quarterly | Cairo, Riyadh, etc. | In-person | Public | Rolling | MENA |
| Parallel18 Demo Day | ~Jun/Dec 2026 | San Juan, PR | Hybrid | Public | Rolling | Latin America |
| Google for Startups Accelerator Demo Day | Varies | Multiple | Virtual | Public | Rolling | Global |
| Creative Destruction Lab Super Session | ~Jun/Nov 2026 | Toronto + global | In-person | Invite-only | Rolling | Global |
| MassChallenge Awards | ~Oct 2026 | Boston, MA | In-person | Public | Rolling | Global |
| Founders Factory Demo Day | ~Jun/Dec 2026 | London, UK | In-person | Invite-only | Rolling | Europe/Africa |
| Dreamit Demo Day | ~Jun/Dec 2026 | Philadelphia / NYC | In-person | Public | Rolling | North America |

**Sources for more:**
- Individual accelerator websites (check "Events" pages)
- Demo Day calendars on F6S
- Startup ecosystem newsletters (The Hustle, StrictlyVC)

**Update frequency:** Monthly (dates change; new programs launch)

---

### Tab 5: Fellowships (Global)

**Columns:**
Fellowship Name | Organizer | Target Audience | Stipend/Award | Duration | Equity Taken | Stage | Location | Application URL | Deadline | Notes

**25 Example Entries:**

| Fellowship Name | Organizer | Target Audience | Stipend/Award | Duration | Equity | Location | Application URL |
|----------------|-----------|----------------|---------------|----------|--------|----------|----------------|
| Thiel Fellowship | Thiel Foundation | Under 23 | $100,000 | 2 years | 0% | Anywhere | https://thielfellowship.org |
| Echoing Green Fellowship | Echoing Green | Social entrepreneurs | $80,000 | 2 years | 0% | Anywhere | https://echoinggreen.org/fellowship |
| On Deck Founders (ODF) | On Deck | Aspiring founders | $0 (community) | 10 weeks | 0% | Virtual | https://www.beondeck.com/founders |
| Kauffman Fellows | Kauffman Foundation | Aspiring VCs | Training program | 2 years | 0% | — | https://www.kauffmanfellows.org |
| Venture for America | VFA | Recent grads | $50K+ salary (placement) | 2 years | 0% | Various US cities | https://ventureforamerica.org |
| Halcyon Incubator | Halcyon | Social entrepreneurs | Residency + mentorship | 18 months | 0% | Washington, DC | https://halcyonhouse.org |
| Activate Fellowship | Activate | Scientists → founders | $100K+ stipend | 2 years | 0% | US (various) | https://www.activate.org |
| Code2040 Fellows | Code2040 | Black/Latinx tech talent | Internship placement | Summer | 0% | San Francisco, CA | https://www.code2040.org |
| Unreasonable Fellows | Unreasonable Group | Growth-stage impact | Program + mentorship | Varies | 0% | Various | https://unreasonablegroup.com |
| New America Fellows | New America | Policy + tech leaders | $100K | 1 year | 0% | Washington, DC | https://www.newamerica.org/fellows |
| Entrepreneurs Roundtable Accelerator (ERA) | ERA | NYC founders | $100K | 4 months | 8% | New York, NY | https://www.eranyc.com |
| Schmidt Futures | Schmidt Futures | Scientists/technologists | Varies | Varies | 0% | Various | https://www.schmidtfutures.com |
| Sequoia Scout / Arc | Sequoia | Founders pre-idea | Varies | Varies | Varies | US / India / SE Asia | https://www.sequoiacap.com/arc |
| South Park Commons | SPC | Builders between things | Community + stipend | Open-ended | 0% | San Francisco, CA | https://www.southparkcommons.com |
| Entrepreneur in Residence (various firms) | Multiple VCs | Experienced operators | Salary/stipend | 6–12 months | 0% | Various | — |
| Mozilla Builders | Mozilla | Open-source founders | $75K | 12 weeks | 0% | Virtual | https://builders.mozilla.community |
| Indie.vc | Indie.vc | Profitable startups | $100K–$1M | Ongoing | Revenue share | Virtual | https://www.indie.vc |
| Pioneer | Pioneer | Global founders | $20K+ | Ongoing | 2% | Virtual (Global) | https://pioneer.app |
| Emergent Ventures | Mercatus Center | Ambitious projects | $10K–$100K+ (grant) | N/A | 0% | Anywhere | https://www.mercatus.org/emergent-ventures |
| Blue Startups | Blue Startups | Asia-Pacific bridge | $20K | 3 months | 6% | Honolulu, HI | https://www.bluestartups.com |

**Sources for more:**
- ProFellow.com
- Scholarship/fellowship aggregator sites
- University career center listings
- Foundation websites (Ford, Rockefeller, Skoll, etc.)

**Update frequency:** Semi-annually (deadlines shift; new programs launch)

---

### Tab 6: Venture Studios (Global)

**Columns:**
Studio Name | Model (co-found / build / invest) | Sector Focus | Stage | Location | Region | How They Work | Website | Application URL | Notes

**25 Example Entries:**

| Studio Name | Model | Sector | Location | Region | Website |
|------------|-------|--------|----------|--------|---------|
| Idealab | Co-found + build | Tech | Pasadena, CA | North America | https://www.idealab.com |
| High Alpha | Co-found + invest | Enterprise SaaS | Indianapolis, IN | North America | https://highalpha.com |
| Atomic | Co-found + build | Consumer + Enterprise | San Francisco, CA | North America | https://www.atomic.vc |
| Science Inc. | Build + invest | Consumer Tech | Santa Monica, CA | North America | https://www.science-inc.com |
| Pioneer Square Labs | Co-found + spin out | Tech | Seattle, WA | North America | https://www.pioneersquarelabs.com |
| Betaworks | Build + invest | Media + Tech | New York, NY | North America | https://betaworks.com |
| eFounders (now Hexa) | Co-found + build | SaaS | Paris, France | Europe | https://www.hexa.cc |
| Rocket Internet | Build + scale | Consumer Internet | Berlin, Germany | Europe/Global | https://www.rocket-internet.com |
| Blenheim Chalcot | Build + scale | FinTech, EdTech, Health | London, UK | Europe | https://www.blenheimchalcot.com |
| NEXT Studios (BCG) | Build + incubate | Enterprise | Multiple | Global | https://www.bcg.com |
| Entrepreneur First | Co-found (pre-team) | Tech | London + global | Global | https://www.joinef.com |
| Human Ventures | Build + invest | Health, Wellness | New York, NY | North America | https://www.humanventures.co |
| Expa | Build + invest | Consumer | San Francisco, CA | North America | https://expa.com |
| FJ Labs | Co-invest (marketplace focus) | Marketplaces | New York, NY | Global | https://fjlabs.com |
| Builders | Build + spin out | Multiple | Copenhagen, Denmark | Europe | https://builders.co |
| Company Studio | Build + launch | Fintech, SaaS | Toronto, Canada | North America | https://companystudio.com |
| All Turtles | Build + invest | AI | San Francisco, CA | North America | https://www.all-turtles.com |
| Diagram | Build + invest | Consumer | New York, NY | North America | https://www.diagram.com |
| Studio VC | Build (Africa) | Tech | Lagos, Nigeria | Africa | — |
| Mamazen | Build + invest | Social Impact | Turin, Italy | Europe | https://mamazen.com |
| Wilbur Labs | Build + operate | B2B Services | San Francisco, CA | North America | https://www.wilburlabs.com |
| Polymath Ventures | Build (LatAm) | LatAm middle class | Bogotá, Colombia | Latin America | https://polymathv.com |
| Deep Science Ventures | Co-found (scientific) | DeepTech, Bio | London, UK | Europe | https://deepscienceventures.com |
| Coplex | Build + launch | Tech | Scottsdale, AZ | North America | https://www.coplex.com |
| NineTwoThree Venture Studio | Build + invest | AI, Mobile | Boston, MA | North America | https://www.ninetwothree.co |

**Sources for more:**
- GSSN (Global Startup Studio Network) member list
- Crunchbase "venture studio" search
- Enhance.co studio directory

**Update frequency:** Semi-annually

---

### Tab 7: Incubators (Global)

**Columns:**
Incubator Name | Organizer/Affiliation | Sector Focus | Stage | Cost/Free | Equity | Location | Region | Services Offered | Website | Application URL

**25 Example Entries:**

| Incubator Name | Affiliation | Sector | Cost | Equity | Location | Region | Website |
|---------------|-------------|--------|------|--------|----------|--------|---------|
| Station F | Xavier Niel | Generalist | Desk fees (~€900/mo) | 0% | Paris, France | Europe | https://stationf.co |
| 1871 | Chicagoland Chamber | Tech | Membership fees | 0% | Chicago, IL | North America | https://1871.com |
| Capital Factory | Capital Factory | Tech | Membership | 0% | Austin, TX | North America | https://www.capitalfactory.com |
| Galvanize | Stride | Tech | Membership | 0% | Multiple US cities | North America | https://www.galvanize.com |
| WeWork Labs | WeWork | Generalist | Membership | 0% | Global | Global | https://www.wework.com/labs |
| Founders Space | Founders Space | Tech | Programs (paid) | 0% | San Francisco, CA | Global | https://www.foundersspace.com |
| StartX | Stanford-affiliated | Tech | Free for Stanford affiliates | 0% | Palo Alto, CA | North America | https://startx.com |
| Harvard Innovation Labs (i-lab) | Harvard | Generalist | Free for students | 0% | Boston, MA | North America | https://innovationlabs.harvard.edu |
| Columbia Startup Lab | Columbia University | Generalist | Free for alumni | 0% | New York, NY | North America | https://startuplab.gsb.columbia.edu |
| Greentown Labs | Greentown Labs | Climate/CleanTech | Membership | 0% | Somerville, MA + Houston, TX | North America | https://greentownlabs.com |
| Chinaccelerator/Chinaaccelerator | SOSV | Cross-border | Investment | 7% | Shanghai, China | Asia | https://chinaccelerator.com |
| NSRCEL (IIM Bangalore) | IIM Bangalore | Generalist | Free | 0% | Bangalore, India | Asia | https://nsrcel.org |
| Hatch Enterprise | Hatch | Social Enterprise | Low-cost programs | 0% | London, UK | Europe | https://hatchenterprise.org.uk |
| Wayra (Telefónica) | Telefónica | Telecom/Tech | Investment | Varies | Multiple (LatAm, Europe) | Global | https://www.wayra.com |
| Impact Hub | Impact Hub Network | Social Impact | Membership | 0% | 100+ cities | Global | https://impacthub.net |
| DMZ (Toronto Metropolitan University) | TMU | Tech | Free | 0% | Toronto, Canada | North America | https://dmz.torontomu.ca |
| Founder Institute | Founder Institute | Generalist | ~$500 | 3.5% warrants | 200+ cities | Global | https://fi.co |
| StartUp Health | StartUp Health | Health | Investment | 3% | Virtual | North America | https://www.startuphealth.com |
| Muru-D (Telstra) | Telstra | Tech | Investment | ~6% | Sydney, Australia | Australia/NZ | https://muru-d.com |
| CIC (Cambridge Innovation Center) | CIC | Generalist | Coworking/membership | 0% | Multiple US + global | Global | https://cic.com |

**Sources for more:**
- University incubator directories
- Country startup ecosystem websites
- International Business Innovation Association (InBIA)
- Global Entrepreneurship Network

**Update frequency:** Annually (incubators are more stable than accelerators)

---

### Tab 8: Events & Conferences 2026 (Global)

**Columns:**
Event Name | Dates | Location | Format (In-Person/Virtual/Hybrid) | Cost | Stage Focus | Sector | Region | Startup Opportunities (pitch, exhibit, discount) | Website | Notes

**30 Example Entries:**

| Event Name | Dates (Est.) | Location | Format | Cost | Region | Website |
|-----------|-------------|----------|--------|------|--------|---------|
| CES 2026 | Jan 2026 | Las Vegas, NV | In-Person | $300+ | Global | https://www.ces.tech |
| SXSW 2026 | Mar 2026 | Austin, TX | Hybrid | $600+ | Global | https://www.sxsw.com |
| Startup Grind Global Conference | Apr 2026 | Redwood City, CA | In-Person | $299+ | Global | https://www.startupgrind.com |
| Collision 2026 | Jun 2026 | Toronto, Canada | In-Person | $300+ | Global | https://collisionconf.com |
| VivaTech 2026 | Jun 2026 | Paris, France | Hybrid | Free–€300+ | Global | https://vivatechnology.com |
| TechCrunch Disrupt 2026 | Oct 2026 | San Francisco, CA | In-Person | $1,000+ | Global | https://techcrunch.com/events/disrupt |
| Web Summit 2026 | Nov 2026 | Lisbon, Portugal | In-Person | Free–€850+ | Global | https://websummit.com |
| Slush 2026 | Nov 2026 | Helsinki, Finland | In-Person | €300+ | Europe/Global | https://www.slush.org |
| Money20/20 USA | Oct 2026 | Las Vegas, NV | In-Person | $2,000+ | Global | https://us.money2020.com |
| Finovate | Various (Spring/Fall) | Various | In-Person | $1,000+ | Global | https://informaconnect.com/finovate |
| AfroTech 2026 | Nov 2026 | Houston, TX (TBD) | In-Person | $200+ | North America | https://afrotech.com |
| Essence Festival of Culture | Jul 2026 | New Orleans, LA | In-Person | Varies | North America | https://www.essencefestival.com |
| 4YFN (Four Years From Now, MWC) | Mar 2026 | Barcelona, Spain | In-Person | €100+ | Europe/Global | https://www.4yfn.com |
| RISE Conference | Mar 2026 | Hong Kong | In-Person | $300+ | Asia | https://riseconf.com |
| Techsauce Global Summit | Aug 2026 | Bangkok, Thailand | In-Person | $200+ | Asia | https://techsauce.co |
| Latitude59 | May 2026 | Tallinn, Estonia | In-Person | €200+ | Europe | https://latitude59.ee |
| TNW Conference | Jun 2026 | Amsterdam, Netherlands | In-Person | €300+ | Europe | https://thenextweb.com/conference |
| Wolves Summit | Jun 2026 | Wrocław, Poland | In-Person | €200+ | Europe | https://wolvessummit.com |
| TechBBQ | Sep 2026 | Copenhagen, Denmark | In-Person | €200+ | Europe | https://techbbq.dk |
| SaaStr Annual | Sep 2026 | San Francisco, CA | In-Person | Free–$1,000+ | Global | https://www.saastrannual.com |
| Disrupt Africa | TBD 2026 | Various (Africa) | In-Person | $50+ | Africa | https://disrupt-africa.com |
| GITEX Global | Oct 2026 | Dubai, UAE | In-Person | Varies | Global | https://www.gitex.com |
| Startup Olé | Apr 2026 | Salamanca, Spain | In-Person | €100+ | Europe | https://startupole.eu |
| TechChill | Feb 2026 | Riga, Latvia | In-Person | €150+ | Europe | https://techchill.co |
| DLD Conference | Jan 2026 | Munich, Germany | In-Person | Invite-only | Europe | https://www.dld-conference.com |
| EmTech MIT | Oct 2026 | Cambridge, MA | In-Person | $800+ | Global | https://emtech.technologyreview.com |
| Singapore FinTech Festival | Nov 2026 | Singapore | In-Person | $300+ | Asia/Global | https://www.fintechfestival.sg |
| Lagos Startup Week | TBD 2026 | Lagos, Nigeria | In-Person | Free | Africa | — |
| Startup India Summit | TBD 2026 | New Delhi, India | Hybrid | Free | Asia | https://www.startupindia.gov.in |
| Nordic Startup Awards | Oct 2026 | Nordic countries | In-Person | Free | Europe | https://nordicstartupawards.com |

**Sources for more:**
- Startup event aggregators (Startup Digest, F6S Events, Eventbrite startup category)
- Industry conference calendars
- Startup ecosystem newsletters
- Regional startup association websites

**Update frequency:** Quarterly (dates and locations change)

---

### Tab 9: Grants & Awards (Global)

**Columns:**
Grant/Award Name | Organizer | Amount | Deadline | Eligibility | Stage | Sector | Dilutive? | Location Requirement | Application URL | Notes

**25 Example Entries:**

| Grant/Award Name | Organizer | Amount | Deadline | Eligibility | Dilutive? | Application URL |
|-----------------|-----------|--------|----------|-------------|-----------|----------------|
| SBIR/STTR Grants | US Government (SBA) | $50K–$2M+ | Rolling | US small businesses | No | https://www.sbir.gov |
| NSF I-Corps | National Science Foundation | $50K | Rolling | University-linked teams | No | https://new.nsf.gov/funding/initiatives/i-corps |
| NIH SBIR/STTR | NIH | $150K–$1M+ | Multiple deadlines | Health/biotech startups | No | https://seed.nih.gov/small-business-funding |
| DARPA SBIR/STTR | DARPA | $100K–$1M+ | Rolling | Defense/tech | No | https://sbir.defensebusiness.org |
| Amazon Climate Pledge Fund | Amazon | $100K–$2M | Rolling | Climate/sustainability | Sometimes | https://www.amazonclimatepledgefund.com |
| Google.org Impact Challenge | Google.org | $25K–$2M | Annual | Nonprofits + social enterprises | No | https://impactchallenge.withgoogle.com |
| Arch Grants | Arch Grants | $50K–$100K | Annual | Relocate to St. Louis | No | https://archgrants.org |
| FedEx Small Business Grant | FedEx | $25K–$50K | Annual | US small businesses | No | https://www.fedex.com/en-us/small-business/grant-contest.html |
| Amber Grant | WomensNet | $10K/mo + $25K annual | Monthly | Women founders | No | https://ambergrantsforwomen.com |
| Cartier Women's Initiative | Cartier | $100K | Annual | Women founders | No | https://www.cartierwomensinitiative.com |
| Visa Everywhere Initiative | Visa | $50K–$100K | Rolling | Fintech startups | No | https://usa.visa.com/run-your-business/visa-everywhere-initiative.html |
| Patagonia Environmental Grants | Patagonia | $5K–$20K | Biannual | Environmental orgs | No | https://www.patagonia.com/actionworks/grants |
| Echoing Green Fellowship | Echoing Green | $80K | Annual | Social entrepreneurs | No | https://echoinggreen.org/fellowship |
| Halcyon Incubator | Halcyon | $10K + housing + mentorship | Annual | Social entrepreneurs (DC) | No | https://halcyonhouse.org |
| EIC Accelerator (EU) | European Commission | Up to €2.5M | 3 cuts/year | EU-based startups | Optional equity | https://eic.ec.europa.eu |
| Innovate UK Smart Grants | UK Research & Innovation | £25K–£500K | Quarterly | UK businesses | No | https://www.ukri.org/councils/innovate-uk |
| Canada SR&ED Tax Credit | CRA | Varies (tax credit) | With tax filing | Canadian companies doing R&D | No | https://www.canada.ca/en/revenue-agency |
| Enterprise Ireland HPSU | Enterprise Ireland | €50K–€250K | Rolling | Ireland-based startups | Sometimes | https://www.enterprise-ireland.com |
| MassChallenge Awards | MassChallenge | $100K+ | Annual | MassChallenge participants | No | https://masschallenge.org |
| Black Ambition Prize | Pharrell Williams | $1M total | Annual | Black/Latinx founders | No | https://www.blackambitionprize.com |
| Verizon Forward for Good | Verizon | $10K–$100K | Annual | Social impact, climate, ed | No | https://www.verizon.com/about/responsibility |
| Wells Fargo Startup Accelerator | Wells Fargo | $1K–$1M | Rolling | Enterprise tech | No | — |
| Rise of the Rest Seed Fund | Revolution / Steve Case | $100K–$500K | Tour-based | Non-coastal US startups | Yes (investment) | https://www.revolution.com/entity/rise-of-the-rest-seed-fund |
| Emergent Ventures (Mercatus) | Mercatus Center | $10K–$100K+ | Rolling | Ambitious projects | No | https://www.mercatus.org/emergent-ventures |
| Schmidt Futures | Schmidt Futures | Varies | Rolling | Scientists/technologists | No | https://www.schmidtfutures.com |

**Sources for more:**
- Grants.gov (US federal)
- SBIR.gov
- GrantWatch.com
- Foundation Directory Online
- Each country's innovation agency website
- Crunchbase "grants" filter

**Update frequency:** Monthly (deadlines are critical)

---

### Tab 10: Books (Startup + Investing)

**Columns:**
Title | Author | Category (Fundraising / Building / Leadership / Marketing / Investing / Mindset) | Year | Amazon/Purchase URL | Free Online? | Notes

**30 Example Entries:**

| Title | Author | Category | Year |
|-------|--------|----------|------|
| The Lean Startup | Eric Ries | Building | 2011 |
| Zero to One | Peter Thiel | Building/Mindset | 2014 |
| The Hard Thing About Hard Things | Ben Horowitz | Leadership | 2014 |
| Blitzscaling | Reid Hoffman | Building/Scaling | 2018 |
| Venture Deals | Brad Feld & Jason Mendelson | Fundraising | 2019 |
| Secrets of Sand Hill Road | Scott Kupor | Fundraising | 2019 |
| The Mom Test | Rob Fitzpatrick | Building/Customer Discovery | 2013 |
| Traction | Gabriel Weinberg & Justin Mares | Marketing/Growth | 2015 |
| Crossing the Chasm | Geoffrey Moore | Marketing | 1991 |
| High Growth Handbook | Elad Gil | Scaling | 2018 |
| The Startup Owner's Manual | Steve Blank & Bob Dorf | Building | 2012 |
| Inspired | Marty Cagan | Product | 2017 |
| Running Lean | Ash Maurya | Building | 2012 |
| Hacking Growth | Sean Ellis | Growth | 2017 |
| Lost and Founder | Rand Fishkin | Building/Mindset | 2018 |
| The $100 Startup | Chris Guillebeau | Building | 2012 |
| Rework | Jason Fried & David Heinemeier Hansson | Building/Mindset | 2010 |
| Lean Analytics | Alistair Croll & Benjamin Yoskovitz | Data/Building | 2013 |
| The Innovator's Dilemma | Clayton Christensen | Strategy | 1997 |
| Good to Great | Jim Collins | Leadership | 2001 |
| Shoe Dog | Phil Knight | Memoir/Mindset | 2016 |
| The Art of the Start 2.0 | Guy Kawasaki | Building | 2015 |
| Measure What Matters | John Doerr | Operations/OKRs | 2018 |
| Sprint | Jake Knapp | Product/Design | 2016 |
| Never Split the Difference | Chris Voss | Negotiation | 2016 |
| Super Founders | Ali Tamaseb | Data/Investing | 2021 |
| The Power Law | Sebastian Mallaby | Investing/VC History | 2022 |
| Fundraising Field Guide | Carlos Espinal | Fundraising | 2016 |
| Play Bigger | Al Ramadan et al. | Strategy/Category Design | 2016 |
| Build | Tony Fadell | Building/Product | 2022 |

**Sources for more:**
- "Best startup books" lists on HackerNews, Product Hunt, Goodreads
- VC reading lists (a16z canon, First Round recommended reading)
- Y Combinator library

**Update frequency:** Annually (new books publish yearly; classics are evergreen)

---

### Tab 11: Blogs & Newsletters (English)

**Columns:**
Name | Author/Publication | Focus | Frequency | Free/Paid | URL | Notes

**30 Example Entries:**

| Name | Author/Pub | Focus | Frequency | Free? | URL |
|------|-----------|-------|-----------|-------|-----|
| Paul Graham's Essays | Paul Graham | Startups, Philosophy | Irregular | Free | https://paulgraham.com/articles.html |
| First Round Review | First Round Capital | Operations, Hiring, Product | Weekly | Free | https://review.firstround.com |
| Lenny's Newsletter | Lenny Rachitsky | Product, Growth | Weekly | Freemium | https://www.lennysnewsletter.com |
| Stratechery | Ben Thompson | Tech Strategy | Daily | Paid | https://stratechery.com |
| The Generalist | Mario Gabriele | Deep Dives on Companies | Weekly | Freemium | https://www.readthegeneralist.com |
| StrictlyVC | Connie Loizos | VC Deals/News | Daily | Free | https://www.strictlyvc.com |
| a16z Blog | Andreessen Horowitz | Tech, Crypto, Bio | Regular | Free | https://a16z.com/blog |
| CBInsights Newsletter | CBInsights | Data/Research | Weekly | Free | https://www.cbinsights.com/newsletter |
| Mattermark Daily | Mattermark | Startup Data | Daily (verify status) | Free | — |
| SaaStr Blog | Jason Lemkin | SaaS | Daily | Free | https://www.saastr.com/blog |
| Both Sides of the Table | Mark Suster | VC, Startups | Irregular | Free | https://bothsidesofthetable.com |
| AVC | Fred Wilson | VC, Tech | Daily (verify status) | Free | https://avc.com |
| Tomasz Tunguz Blog | Tomasz Tunguz | SaaS Metrics, VC | Regular | Free | https://tomtunguz.com |
| Benedict Evans Newsletter | Benedict Evans | Tech Trends | Weekly | Free | https://www.ben-evans.com/newsletter |
| The Information | The Information | Tech Industry | Daily | Paid | https://www.theinformation.com |
| Crunchbase News | Crunchbase | Funding, M&A | Daily | Free | https://news.crunchbase.com |
| TechCrunch | TechCrunch | Startups, Tech | Daily | Free | https://techcrunch.com |
| The Hustle | The Hustle / HubSpot | Business, Tech | Daily | Free | https://thehustle.co |
| Morning Brew | Morning Brew | Business News | Daily | Free | https://www.morningbrew.com |
| Not Boring | Packy McCormick | Strategy, Tech | Weekly | Freemium | https://www.notboring.co |
| Elad Gil Blog | Elad Gil | Scaling, VC | Irregular | Free | https://blog.eladgil.com |
| Y Combinator Blog | YC | Startups, Advice | Regular | Free | https://www.ycombinator.com/blog |
| NFX Essays | NFX | Network Effects, Growth | Regular | Free | https://www.nfx.com/post |
| Bessemer Cloud Index / Blog | Bessemer | Cloud/SaaS | Regular | Free | https://www.bvp.com/atlas |
| OpenView Partners Blog | OpenView | Product-Led Growth | Regular | Free | https://openviewpartners.com/blog |
| Future | a16z | Tech Optimism | Regular | Free | https://future.com |
| Newcomer | Eric Newcomer | Silicon Valley, VC | Weekly | Paid | https://www.newcomer.co |
| Axios Pro Rata | Dan Primack | Deals, VC | Daily | Free | https://www.axios.com/newsletters/axios-pro-rata |
| Term Sheet (Fortune) | Fortune | Deals, VC | Daily | Free | https://fortune.com/newsletter/termsheet |
| Startup Stash Newsletter | Startup Stash | Tools, Resources | Weekly | Free | https://startupstash.com |

**Sources for more:**
- Substack startup/tech category
- HackerNews "Ask HN: Best newsletters"
- Product Hunt newsletter collections

**Update frequency:** Semi-annually (check for defunct newsletters, add notable new ones)

---

### Tab 12: Podcasts (English)

**Columns:**
Podcast Name | Host(s) | Focus | Episode Frequency | Platform Links (Spotify/Apple) | Notes

**30 Example Entries:**

| Podcast Name | Host(s) | Focus | Frequency |
|-------------|---------|-------|-----------|
| How I Built This | Guy Raz | Founder Stories | Weekly |
| Masters of Scale | Reid Hoffman | Scaling | Weekly |
| All-In Podcast | Chamath, Sacks, Friedberg, Calacanis | Tech, VC, Markets | Weekly |
| The Twenty Minute VC (20VC) | Harry Stebbings | VC Interviews | Daily |
| This Week in Startups (TWIST) | Jason Calacanis | Startup News | Multiple/week |
| a16z Podcast | a16z Team | Tech Trends | Weekly |
| Acquired | Ben Gilbert & David Rosenthal | Company Deep Dives | Biweekly |
| My First Million | Shaan Puri & Sam Parr | Business Ideas | Multiple/week |
| The Pitch | Josh Muccio | Live Startup Pitches | Weekly |
| StartUp Podcast | Gimlet Media | Startup Stories (verify active) | Season-based |
| Indie Hackers | Courtland Allen | Bootstrapping | Weekly |
| Mixergy | Andrew Warner | Founder Interviews | Multiple/week |
| SaaStr Podcast | Harry Stebbings / Jason Lemkin | SaaS | Weekly |
| Venture Stories / Village Global | Erik Torenberg | VC Perspectives | Weekly |
| The Tim Ferriss Show | Tim Ferriss | Performance, Business | Weekly |
| Lenny's Podcast | Lenny Rachitsky | Product, Growth | Weekly |
| Founder Coffee | Matt DeCoursey | Founder Conversations | Weekly |
| The Logan Bartlett Show | Logan Bartlett | VC + Founders | Weekly |
| Pivot | Kara Swisher & Scott Galloway | Tech, Business | Twice/week |
| Equity (TechCrunch) | TechCrunch Team | VC/Startup News | Multiple/week |
| The Full Ratchet | Nick Moran | Angel Investing | Weekly |
| Angel (Podcast) | Jason Calacanis | Angel Investing | Irregular |
| Founder's Journal | Morning Brew / Alex Lieberman | Founder Lessons | Multiple/week |
| Invest Like the Best | Patrick O'Shaughnessy | Investing Deep Dives | Weekly |
| The Knowledge Project | Shane Parrish | Mental Models | Weekly |
| Lex Fridman Podcast | Lex Fridman | Tech, AI, Science (founder eps) | Weekly |
| Greylock Partners Podcast | Greylock | VC Perspectives | Biweekly |
| Foundering (Bloomberg) | Bloomberg | Startup Failures | Season-based |
| Product Hunt Radio | Product Hunt | Product, Startups | Weekly |
| Below the Line | James Beshara | Founder Mental Health | Weekly |

**Sources for more:**
- Apple Podcasts "Business" charts
- Spotify podcast rankings
- "Best startup podcasts" annual lists
- Product Hunt podcast collections

**Update frequency:** Semi-annually (check for dead shows, add new breakouts)

---

### Tab 13: Free Databases & Lists

**Columns:**
Resource Name | Type (Database / List / Directory) | What's Included | Free Tier Limits | Premium Cost | Best For | URL | Notes

**30 Example Entries:**

| Resource Name | Type | What's Included | Free Limits | Premium Cost | Best For | URL |
|--------------|------|----------------|-------------|-------------|---------|-----|
| OpenVC | Database | 6,000+ VCs with thesis + stage + geo | Unlimited free | N/A | Finding VCs by criteria | https://openvc.app |
| Signal by NFX | Database | 15,000+ investors with warm intro paths | Unlimited free | N/A | Investor discovery + warm intros | https://signal.nfx.com |
| Crunchbase | Database | Companies, investors, funding rounds | 5 searches/day (free) | $29–$49/mo | Market research | https://www.crunchbase.com |
| AngelList / Wellfound | Platform | Startup jobs, investors, fundraising | Free to post | Rolling Close fee | Fundraising + hiring | https://wellfound.com |
| F6S | Platform | Accelerators, grants, competitions, investors | Free | N/A | Finding programs + deals | https://www.f6s.com |
| Gust | Platform | Angel groups, accelerators | Free to apply | Platform fee | Connecting with angel groups | https://gust.com |
| PitchBook (Free) | Database | Limited company + deal data | Very limited (paywall) | $20K+/yr | Enterprise-level research | https://pitchbook.com |
| VC Lab Investor List | List | Curated VC list by stage + sector | Free PDF | N/A | Quick VC lookup | https://www.vclab.fund |
| Airtable Community Lists | Lists | Various crowdsourced investor lists | Free | N/A | Community-curated data | Search "VC list" on Airtable Universe |
| Visible.vc Fundraising Database | Database | VC contacts + templates | Free trial | Paid platform | Fundraise management | https://visible.vc |
| DocSend Fundraising Network | Tools + Data | Pitch deck analytics + investor connects | Free tier | $10/mo+ | Pitch deck sharing | https://www.docsend.com |
| Product Hunt Ship | Platform | Early adopter collection + launch | Free tier | Paid options | Pre-launch + launch | https://www.producthunt.com/ship |
| Startup Stash | Directory | 12,000+ tools and resources | Free | N/A | Finding startup tools | https://startupstash.com |
| BetaList | Directory | Upcoming startups + beta signups | Free to browse | $129 to submit | Early user acquisition | https://betalist.com |
| SeedTable (Dealroom) | Database | European startup data | Limited free | Paid | European ecosystem | https://dealroom.co |
| CB Insights Free Content | Research | Industry reports, trend data | Newsletter free | $50K+/yr | Industry intelligence | https://www.cbinsights.com |
| NVCA Member Directory | Directory | US VC firms | Free to browse | N/A | Finding NVCA member VCs | https://nvca.org/membership/member-directory |
| EBAN (European Business Angels Network) | Directory | European angel groups | Free to browse | N/A | European angel investors | https://www.eban.org |
| StartupBlink Ecosystem Map | Map + Data | Global startup ecosystems ranked | Free map | Paid reports | Ecosystem comparison | https://www.startupblink.com |
| Tracxn | Database | Startups + investors | 10 free searches/mo | $500+/mo | Indian + global data | https://tracxn.com |
| PEI 300 / Private Equity Lists | List | Top PE firms | Partial free | Paid | Private equity | Various |
| Indie Hackers | Community | Revenue-transparent startups | Free | N/A | Bootstrapper community | https://www.indiehackers.com |
| MicroAcquire (now Acquire.com) | Marketplace | Startups for sale | Free to browse | Paid to list | Acquisition | https://acquire.com |
| Global Startup Ecosystem Report (Startup Genome) | Report | Ecosystem rankings + data | Summary free | $1K+ full report | Ecosystem strategy | https://startupgenome.com |
| EU Startup Monitor | Report | European startup data | Free | N/A | EU ecosystem data | — |
| SaaS Mag 1000 | List | Top SaaS companies | Free | N/A | SaaS benchmarking | https://www.saasmag.com |
| Failory | Database | Startup failures + lessons | Free | N/A | Learning from failures | https://www.failory.com |
| BuiltWith | Database | Tech stack data | Limited free | $295+/mo | Market intelligence | https://builtwith.com |
| SimilarWeb | Database | Website traffic data | Limited free | Paid | Competitive research | https://www.similarweb.com |
| LinkedIn Sales Navigator | Database | Professional network | Limited free | $79+/mo | Investor outreach | https://www.linkedin.com/sales |

**Sources for more:**
- Product Hunt "startup tools" collections
- "Free VC databases" blog posts
- Startup Twitter/X community recommendations
- HackerNews "Show HN" posts

**Update frequency:** Quarterly (check for dead links, new resources)

---

### Tab 14: Tools & Templates

**Columns:**
Tool/Template Name | Category (Pitch Deck / Financial Model / Cap Table / Legal / Operations / Marketing) | Free/Paid | URL | Notes

**30 Example Entries:**

| Tool/Template Name | Category | Free/Paid | URL |
|-------------------|----------|-----------|-----|
| Pitch Deck Templates (Slidebean) | Pitch Deck | Freemium | https://slidebean.com/templates |
| Y Combinator Series A Pitch Template | Pitch Deck | Free | YC Library |
| Sequoia Pitch Deck Template | Pitch Deck | Free | Search "Sequoia pitch deck" |
| Guy Kawasaki 10-Slide Template | Pitch Deck | Free | Search "Guy Kawasaki 10/20/30" |
| Carta | Cap Table | Freemium | https://carta.com |
| Pulley | Cap Table | Free for <25 stakeholders | https://pulley.com |
| LTSE Equity | Cap Table | Free tier | https://equity.ltse.com |
| Causal (Financial Modeling) | Financial Model | Freemium | https://www.causal.app |
| Coda / Notion Templates | Operations | Free | https://coda.io / https://notion.so |
| Stripe Atlas | Incorporation | $500 | https://stripe.com/atlas |
| Clerky | Legal (Incorporation + Docs) | Pay per doc | https://www.clerky.com |
| YC SAFE Documents | Legal (Fundraising) | Free | https://www.ycombinator.com/documents |
| NVCA Model Legal Documents | Legal (VC) | Free | https://nvca.org/model-legal-documents |
| Brex | Banking/Finance | Free | https://www.brex.com |
| Mercury | Banking | Free | https://mercury.com |
| Gusto | Payroll/HR | $40+/mo | https://gusto.com |
| Rippling | HR/IT | $8+/mo per user | https://www.rippling.com |
| Figma | Design | Free tier | https://www.figma.com |
| Canva | Design | Freemium | https://www.canva.com |
| Mailchimp | Email Marketing | Free tier | https://mailchimp.com |
| HubSpot CRM | CRM | Free tier | https://www.hubspot.com |
| Google Analytics | Analytics | Free | https://analytics.google.com |
| Mixpanel | Product Analytics | Free tier | https://mixpanel.com |
| Ahrefs / SEMrush | SEO | Paid ($99+/mo) | https://ahrefs.com |
| Loom | Video Communication | Freemium | https://www.loom.com |
| Linear | Project Management | Free tier | https://linear.app |
| Typeform | Forms/Surveys | Freemium | https://www.typeform.com |
| Vercel / Netlify | Hosting/Deploy | Free tier | https://vercel.com |
| OpenAI API | AI | Pay-per-use | https://platform.openai.com |
| Notion VCs Template | VC Tracker | Free | Search "Notion VC tracker" |

**Sources for more:**
- Product Hunt
- Startup Stash (https://startupstash.com)
- G2 startup category
- HackerNews recommendations

**Update frequency:** Semi-annually

---

## 6. Free Databases & Lists — Deep Dive

This section expands on Tab 13 with usage tips and strategic context. The goal: help founders understand **which free tool to use for what.**

### Tier 1: Best Free Investor Discovery Tools

| Tool | Best For | Pro Tips |
|------|---------|---------|
| **OpenVC** | Finding VCs by stage, sector, geography | Filter by "open for applications" — many have direct pitch forms. Best free VC database period. |
| **Signal by NFX** | Finding warm intro paths | Connect your LinkedIn — it maps who you know who can intro you. Game-changer. |
| **AngelList / Wellfound** | Rolling closes, syndicate leads | Create a strong company profile — investors browse too. Use "Raise" for fundraising. |
| **F6S** | Programs + deals, not just investors | Apply to accelerators and grants through one profile. Free deal flow. |

### Tier 2: Good Free Tiers (Limited)

| Tool | Free Limits | Worth Upgrading? |
|------|------------|-----------------|
| **Crunchbase** | 5 profile views/day | Maybe — if doing heavy market research |
| **LinkedIn** | Limited searches, no InMail | Yes — Sales Navigator is worth it for outreach |
| **PitchBook** | Almost nothing free | No for most founders — overkill |
| **Tracxn** | 10 searches/month | Only if India/Asia focused |

### Tier 3: Community / Crowdsourced

| Resource | What It Is |
|----------|-----------|
| **Airtable community lists** | Search "VC list" on Airtable — tons of crowdsourced databases |
| **Twitter/X lists** | Many VCs share lists of active investors by stage/sector |
| **Reddit r/startups** | Community-maintained resource threads |
| **Indie Hackers** | Bootstrapper community with transparent revenue data |

### ⚠️ What These Free Tools WON'T Give You
- **Verified email addresses** (that's what the Master DB provides)
- **Intro paths beyond LinkedIn** (network effects of Angel Club membership)
- **Portfolio company details** with contact info
- **Real-time deal flow intelligence**

**This is the value gap that protects the Members-Only Master Investor Database.**

---

## 7. Platform Recommendation

### Option Analysis

| Platform | Pros | Cons | Cost | SEO Potential |
|----------|------|------|------|--------------|
| **Google Sheets** (current) | Free, familiar, easy to edit, shareable | Not SEO-friendly, hard to make beautiful, limited filtering | Free | ⭐ (poor — Google doesn't index Sheets well) |
| **Airtable** | Beautiful views, filtering, forms, embeddable | Learning curve, free tier limits (1,000 records), URL structure not ideal for SEO | Free–$20/user/mo | ⭐⭐ (slightly better, but still limited) |
| **Notion** | Beautiful, free, shareable, good URL structure | Limited filtering for visitors, can feel overwhelming | Free–$8/user/mo | ⭐⭐⭐ (Notion pages get indexed) |
| **Custom Web Page** (on angelclub.com) | Full SEO control, brand cohesion, lead capture | Development cost, maintenance burden | Dev cost + hosting | ⭐⭐⭐⭐⭐ (best for SEO) |
| **Hybrid: Google Sheets + Landing Page** | Easy to maintain (Sheets) + SEO (page) | Two things to maintain | Minimal | ⭐⭐⭐⭐ (good balance) |

### 🏆 Recommendation: Hybrid Approach

**Phase 1 (Now):** Keep Google Sheets as the master data source. It's easy to update and already has infrastructure.

**Phase 2 (Soon):** Build a landing page on `angelclub.com/resources` that:
- Summarizes each tab with 10–15 highlighted entries
- Has proper SEO (title tags, meta descriptions, schema markup)
- Links to the full Google Sheet for each category
- Includes email capture ("Get updates when we add new resources")
- Has social share buttons
- Tracks traffic with UTM parameters

**Phase 3 (Later):** Consider migrating the Google Sheet to Airtable for:
- Better embeddable views on the landing page
- Filter/search functionality for visitors
- Form submissions for community additions
- Gallery/kanban views for visual browsing

**Why not all-custom?** Maintenance burden. A Google Sheet can be updated by anyone in 30 seconds. A custom database needs a developer. Angel Club should optimize for **ease of updates** to keep the data fresh — stale data kills resource lists.

---

## 8. SEO & AI Discovery Strategy

### 8.1 Google Sheets SEO (Limited but Possible)

Google Sheets are **not inherently SEO-friendly**, but you can improve visibility:

1. **Sheet title:** "Angel Club Public Resources — Free Startup Investor Database, Accelerators, Grants & More (2026)"
2. **Tab names:** Descriptive (not "Sheet1") — "VC Funds & Angel Groups", "Accelerators 2026", etc.
3. **Share settings:** "Anyone with the link can view" (required for any indexing)
4. **Link building:** Get the sheet linked from blog posts, newsletters, and social media

### 8.2 Landing Page SEO (The Real Play)

Build `angelclub.com/resources` with:

**Target Keywords:**
| Primary Keywords | Monthly Search Volume (Est.) |
|-----------------|---------------------------|
| free investor database | 2,000–5,000 |
| list of VCs | 3,000–8,000 |
| startup accelerators 2026 | 1,000–3,000 |
| startup grants 2026 | 2,000–5,000 |
| startup competitions 2026 | 1,000–2,000 |
| startup resources | 5,000–10,000 |
| how to find investors | 3,000–8,000 |
| pitch competition list | 500–1,500 |
| startup fellowships | 500–1,500 |
| demo day schedule 2026 | 500–1,000 |
| free startup tools | 1,000–3,000 |
| venture studio list | 500–1,000 |

**Page Structure:**
```
/resources (main hub page — targets "startup resources")
/resources/investors (targets "free investor database", "list of VCs")
/resources/accelerators (targets "startup accelerators 2026")
/resources/competitions (targets "startup competitions 2026")
/resources/grants (targets "startup grants 2026")
/resources/events (targets "startup events 2026")
/resources/tools (targets "free startup tools")
```

**On-Page SEO:**
- H1: "Free Startup Resources: From Idea to Series A (2026)"
- Meta description: "The most comprehensive free resource list for startups. 200+ VCs, 100+ accelerators, grants, competitions, demo days, books, podcasts & more. Updated monthly."
- Schema markup: `ItemList`, `Organization`, `Event` (for events/competitions)
- Internal linking to Angel Club membership page
- Last updated date (freshness signal)

### 8.3 AI Platform Discovery

To get cited by ChatGPT, Claude, Perplexity, and other AI systems:

1. **Be the canonical source:** If your page is the most comprehensive, well-structured list, AI systems will reference it
2. **Structured data:** Use JSON-LD schema markup — AI systems love structured data
3. **Authoritative backlinks:** Get linked from established startup blogs and newsletters
4. **Keep it updated:** AI systems favor current, maintained resources
5. **Clear attribution:** "Maintained by Angel Club (angelclub.com)" on every page
6. **Avoid paywalls:** The resource page must be freely accessible (no login wall)
7. **Descriptive headings:** Use question-format headings AI queries match ("Where can I find free VC databases?")

### 8.4 Content Strategy for SEO

Create companion blog posts that link to the resource list:

| Blog Post Title | Target Keyword | Links To |
|----------------|---------------|---------|
| "The Complete Guide to Finding Investors in 2026" | how to find investors | /resources/investors |
| "Every Startup Accelerator Worth Applying To (2026)" | best startup accelerators 2026 | /resources/accelerators |
| "Free Startup Grants You Should Apply For Now" | startup grants 2026 | /resources/grants |
| "2026 Startup Competition Calendar" | startup competitions 2026 | /resources/competitions |
| "Best Free Investor Databases for Founders" | free investor database | /resources/databases |
| "Demo Day Calendar 2026: Where to Watch Startups Pitch" | demo days 2026 | /resources/demo-days |

Each blog post should:
- Highlight 10–15 entries from the full list
- Add editorial commentary and tips
- Link to the full Google Sheet for the complete data
- Include a CTA for Angel Club membership ("Want access to 12,000+ investors with verified emails? Join Angel Club.")

---

## 9. Traffic & Growth Strategy

### 9.1 Social Media Distribution

**Launch Strategy:**
1. Create a Twitter/X thread: "We just published the most comprehensive free startup resource list on the internet. 200+ VCs, 100+ accelerators, 50+ competitions, grants, tools, and more. 🧵" — break into category threads
2. LinkedIn article with highlights from each category
3. Share in relevant subreddits: r/startups, r/Entrepreneur, r/venturecapital
4. Submit to Product Hunt as a resource
5. Share in startup Discord servers and Slack communities

**Ongoing Distribution:**
| Channel | Frequency | Content Type |
|---------|-----------|-------------|
| Twitter/X | 3–5x/week | Individual resource highlights ("Did you know [X] gives $100K non-dilutive grants?") |
| LinkedIn | 2–3x/week | Category highlights + editorial |
| Newsletter | Monthly | "New additions this month" roundup |
| Reddit | Monthly | Updated posts in relevant subreddits |
| WhatsApp groups | Monthly | Link to new additions |

### 9.2 Partnership & Link-Building

**Tier 1 — Ask for backlinks:**
- Accelerators listed in the sheet (they'll want to share a list that features them)
- Startup media outlets (TechCrunch, Crunchbase News, etc.)
- University entrepreneurship programs
- Other startup resource sites (cross-link)

**Tier 2 — Guest posts:**
- Write "best of" posts for startup blogs that link back to the full resource
- Contribute to newsletters (The Hustle, Morning Brew, etc.)

**Tier 3 — PR:**
- "Angel Club publishes the internet's most comprehensive free startup resource list" — pitch to startup media
- Annual "State of Startup Resources" report using data from the list

### 9.3 "Featured Resource" Rotation Strategy

Each week, feature one entry from the list across all social channels:

**Format:**
> 🌟 **Resource Spotlight**
> **[Resource Name]** — [One-line description]
> 💰 [What they offer]
> 🎯 [Who it's for]
> 🔗 [URL]
> Found in Angel Club's free resource database: [link]

This creates 52+ pieces of content per year from existing data.

### 9.4 Lead Capture & Conversion

Every touchpoint should include:
- Email capture for "resource updates" newsletter
- Soft CTA: "This is our free list. Our members get access to 12,000+ investors with verified contact info."
- Hard CTA on the landing page: "Join Angel Club" button

**Funnel:**
Free resource list → Email signup → Nurture sequence → Angel Club membership

### 9.5 Community Contributions

Add a "Suggest a Resource" Google Form linked from every tab:
- Let the community submit new resources
- Moderate submissions before adding
- Credit contributors ("Added by @username")
- Creates engagement and ownership

---

## 10. What Else Is Missing

### Categories We Haven't Thought Of

| Missing Category | Why It Matters | Priority |
|-----------------|---------------|----------|
| **Government Programs by Country** | SBIR is US-only; every country has startup programs | 🟡 Medium |
| **University Programs** | Many top programs accept non-students | 🟡 Medium |
| **Co-Founder Matching Platforms** | Y Combinator Co-Founder Matching, CoFoundersLab, etc. | 🔴 High |
| **Legal Resources** | Beyond templates — lawyer directories, free legal clinics | 🟡 Medium |
| **Diversity-Specific Programs** | Consolidate all programs for underrepresented founders | 🔴 High |
| **Corporate Venture / Innovation Programs** | Google, Microsoft, Amazon, Salesforce startup programs | 🟡 Medium |
| **Revenue-Based Financing** | Clearco, Pipe, Capchase — alternatives to VC | 🟡 Medium |
| **Startup Visa Programs by Country** | For founders who want to start up abroad | 🟢 Low |
| **Mentorship Programs** | SCORE, MicroMentor, Founder Mentors, etc. | 🟡 Medium |
| **Pitch Deck Examples** | Links to real pitch decks from successful raises | 🔴 High |
| **Benchmark / Metrics Databases** | SaaS benchmarks, marketplace metrics, etc. | 🟢 Low |
| **Startup Communities / Slack/Discord Groups** | Where founders hang out online | 🟡 Medium |
| **AI / No-Code Builder Tools** | Increasingly essential for early-stage founders | 🟡 Medium |

### International Considerations

| Region | What's Missing | Action |
|--------|---------------|--------|
| **Africa** | Underrepresented in most global lists. Lagos, Nairobi, Cape Town ecosystems are booming | Add Africa-specific accelerators, funds, competitions |
| **Southeast Asia** | Singapore, Jakarta, Bangkok — massive growth | Ensure SOSV programs, Antler Asia, etc. are included |
| **Latin America** | Start-Up Chile, Parallel18, but many more programs | Add LatAm-specific entries |
| **India** | Massive ecosystem with unique programs (Startup India) | Dedicated section or tagging |
| **MENA** | Dubai, Riyadh — huge government-backed programs | Ensure Flat6Labs, GITEX, etc. are included |
| **Eastern Europe** | Estonia, Poland, Czech Republic — fast-growing | Add regional programs |

### The "Ultimate Resource" Checklist

For this to be THE definitive idea-to-Series-A resource, it should answer every question a first-time founder asks:

- [x] Where do I find investors? → Tab 1 + Tab 13
- [x] What accelerators should I apply to? → Tab 2
- [x] What competitions can I enter? → Tab 3
- [x] When are demo days? → Tab 4
- [x] Are there fellowships for me? → Tab 5
- [x] What's a venture studio? → Tab 6
- [x] Should I join an incubator? → Tab 7
- [x] What events should I attend? → Tab 8
- [x] Is there free money (grants)? → Tab 9
- [x] What books should I read? → Tab 10
- [x] What blogs/newsletters should I follow? → Tab 11
- [x] What podcasts are good? → Tab 12
- [x] What free databases exist? → Tab 13
- [x] What tools do I need? → Tab 14
- [ ] How do I find a co-founder? → **Add this**
- [ ] How do I incorporate? → Partially in Tools, expand
- [ ] How do I build a pitch deck? → Partially in Tools, add examples
- [ ] What metrics should I track? → **Add this**
- [ ] How do I price my product? → **Add this (resources/guides)**
- [ ] What's the fundraising timeline? → **Add this (guide/infographic)**

---

## 11. Execution Timeline

### Week 1: Audit & Clean
- [ ] **Audit all existing tabs** in the Google Sheet — document what exists
- [ ] Clean Tab 1 (duplicates, individuals, URLs, format)
- [ ] Add Location and Pitch URL columns to Tab 1
- [ ] Create standardized column headers for all tabs

### Week 2: Build High-Priority Tabs
- [ ] Tab 2: Accelerators (populate 50+ entries)
- [ ] Tab 3: Startup Competitions 2026 (populate 30+ entries)
- [ ] Tab 9: Grants & Awards (populate 25+ entries)

### Week 3: Build Medium-Priority Tabs
- [ ] Tab 4: Demo Days 2026 (populate 20+ entries)
- [ ] Tab 5: Fellowships (populate 20+ entries)
- [ ] Tab 8: Events & Conferences 2026 (populate 30+ entries)
- [ ] Tab 13: Free Databases & Lists (populate 25+ entries)

### Week 4: Build Remaining Tabs
- [ ] Tab 6: Venture Studios (populate 25+ entries)
- [ ] Tab 7: Incubators (populate 20+ entries)
- [ ] Tab 10: Books (populate 30+ entries)
- [ ] Tab 11: Blogs & Newsletters (populate 30+ entries)
- [ ] Tab 12: Podcasts (populate 30+ entries)
- [ ] Tab 14: Tools & Templates (populate 30+ entries)

### Week 5: SEO & Launch
- [ ] Build `angelclub.com/resources` landing page
- [ ] Write first companion blog post
- [ ] Set up email capture
- [ ] Social media launch campaign
- [ ] Submit to Product Hunt, HackerNews, Reddit

### Week 6+: Growth & Maintenance
- [ ] Weekly featured resource posts
- [ ] Monthly data freshness check
- [ ] Quarterly full audit
- [ ] Build additional companion blog posts

---

## 12. Maintenance Cadence

| Task | Frequency | Time Estimate | Who |
|------|-----------|--------------|-----|
| Check for broken URLs | Monthly | 1 hour | Automated tool + manual review |
| Update competition/event deadlines | Monthly | 2 hours | Manual |
| Add new resources | Ongoing | 30 min/week | Community suggestions + research |
| Full data audit (all tabs) | Quarterly | 4–6 hours | Manual |
| Remove defunct entries | Quarterly | 1 hour | Manual |
| Update "2026" references | Annually (Q4) | 2 hours | Manual |
| Refresh SEO keywords | Semi-annually | 1 hour | Manual |
| Review community submissions | Weekly | 30 min | Manual |
| Blog post creation | Monthly | 2–3 hours | Writer |
| Social media content from list | Weekly | 30 min | Social media |

### Automated Maintenance Options
- **Broken link checker:** Use a free tool like Dead Link Checker or a Google Sheets add-on
- **Google Alerts:** Set up alerts for "new startup accelerator", "startup grant 2026", etc.
- **RSS feeds:** Subscribe to startup ecosystem newsletters for new programs

---

## Appendix A: Quick-Start Checklist

If you want to start improving the sheet TODAY, do these 10 things:

1. ☐ Open the Google Sheet and list every existing tab name
2. ☐ Sort Tab 1 alphabetically and delete obvious duplicates
3. ☐ Remove individual investor names from Tab 1
4. ☐ Add "Pitch URL" and "Location" columns to Tab 1
5. ☐ Test all URLs in Tab 1 and fix broken ones
6. ☐ Create the "Accelerators" tab with the 30 entries from this doc
7. ☐ Create the "Startup Competitions 2026" tab with the 30+ entries from this doc
8. ☐ Create the "Free Databases & Lists" tab with the 30 entries from this doc
9. ☐ Add a "Suggest a Resource" link at the top of the first tab
10. ☐ Share the updated sheet on social media

## Appendix B: Competitive Analysis

**Who else has public resource lists?**

| Competitor | What They Have | Our Advantage |
|-----------|---------------|---------------|
| Y Combinator Library | Curated, high-quality, but narrow (YC-centric) | Broader (not tied to one accelerator) |
| First Round Review | Excellent content but not a database | We're structured data, not articles |
| Startup Stash | Great tool directory but weak on investors/programs | We cover the full journey |
| F6S | Comprehensive but noisy, hard to navigate | We're curated and opinionated |
| OpenVC | Best free VC database but only VCs | We cover everything beyond VCs |
| Product Hunt | Tools and launches but not resources | We're a static, browsable reference |

**Our positioning:** The only comprehensive, curated, free resource covering the **entire startup journey** from idea to Series A — maintained by a community of active investors (Angel Club).

---

*This document is a living plan. Update it as tabs are completed, strategies are tested, and new ideas emerge.*

*Last updated: April 2, 2026*
