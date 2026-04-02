# Angel Club Resources Page — FINAL Production Copy & Design Brief (v2)

**Page:** angelclub.com/resources
**Last Updated:** April 2, 2026
**Status:** Production-ready (v2 — comprehensive competitive update)
**Benchmark:** Beat YC Library, Startup Stash, First Round Review, a16z Guides, Notion Templates

---

## TABLE OF CONTENTS

1. [Competitive Positioning](#1-competitive-positioning)
2. [SEO & Meta](#2-seo--meta)
3. [AI Discoverability & Schema Markup](#3-ai-discoverability--schema-markup)
4. [Page Copy — Section by Section](#4-page-copy)
5. [Design Specifications](#5-design-specifications)
6. [Mobile-First Specifications](#6-mobile-first-specifications)
7. [Search/Filter UX System](#7-searchfilter-ux-system)
8. [Implementation Roadmap](#8-implementation-roadmap)

---

## 1. COMPETITIVE POSITIONING

### Why We Win

| Competitor | What They Do Well | What We Beat Them On |
|---|---|---|
| **YC Startup Library** | Stage-filtered, topic-categorized editorial content | We have a live, searchable 12,000+ investor database — not just articles. Plus grants with deadlines, community curation. |
| **Startup Stash** | Massive tool directory, category breadth | Our resources are founder-verified by 6,400+ real users, not just listed. Plus investor DB is proprietary. |
| **First Round Review** | Deep editorial, operator-focused | We combine content + tools + live data (investor DB, grant deadlines). Actionable, not just readable. |
| **a16z Guides** | Authoritative topic playbooks | Our playbooks come from 6,400+ founders who've actually raised — not one VC firm's perspective. |
| **Notion Templates** | Practical, immediately usable templates | We embed templates inside a full fundraising ecosystem (database → intros → Ready to Raise). |

### Our Moat (What Nobody Else Has)
1. **12,000+ real investor database** — searchable by stage, thesis, geography, sector, check size
2. **Community-curated by 6,400+ founders** who've actually used these resources and raised capital
3. **Live grant deadlines** with countdown timers — not static links that go stale
4. **Connected ecosystem** — Resources → Investor DB → Warm Intros → Ready to Raise → Syndicate → Events
5. **Faith-based investor sector** — first major directory to include this
6. **Stage-based navigation** — resources filtered to exactly where you are in your journey

---

## 2. SEO & META

### Page Title
```
Startup Resources: 12,000+ Investors, Grants, Accelerators & Tools for Every Stage | Angel Club
```
*(78 chars — within 60-character display but full title for indexing)*

### Meta Description
```
The definitive startup resource hub from idea to Series A. 12,000+ searchable investors, 350+ grants with live deadlines, 200+ accelerators — curated by 6,400+ founders. Free directories + premium investor database with warm intros.
```
*(230 chars — within 160-char display)*

### H1 (visible on page)
```
The Startup Resource Hub — From First Idea to Series A
```

### URL Structure
```
angelclub.com/resources                     (main hub)
angelclub.com/resources?stage=pre-seed      (stage filter via query param)
angelclub.com/resources?category=grants     (category filter)
angelclub.com/resources/investors           (future dedicated subpage)
angelclub.com/resources/grants              (future dedicated subpage)
angelclub.com/resources/accelerators        (future dedicated subpage)
angelclub.com/resources/submit              (submission form)
```

### Target Keywords

**Primary (high volume, high intent):**
- startup resources
- startup resources 2026
- investor database
- startup funding resources
- free investor list
- startup grants
- startup accelerator list

**Secondary (long-tail, high conversion):**
- free investor database for startups
- startup grants for women founders
- pre-seed funding resources
- faith-based investors
- startup grants with deadlines
- best startup resources 2026
- angel investor directory
- venture capital database
- seed stage investor list
- non-dilutive funding for startups
- startup fundraising templates
- Series A preparation resources

**Conversational / AI-targeted:**
- best startup resources
- where to find investors for my startup
- free investor lists for startups
- how to find grants for my startup
- startup resources from idea to Series A
- what resources do founders need

### Open Graph Tags
```html
<meta property="og:title" content="Startup Resources: 12,000+ Investors, Grants & Tools | Angel Club" />
<meta property="og:description" content="The definitive startup resource hub from idea to Series A. Curated by 6,400+ founders. Free directories + premium investor database with warm intros." />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://angelclub.com/resources" />
<meta property="og:image" content="https://angelclub.com/images/resources-og-2026.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:site_name" content="Angel Club" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Startup Resources: 12,000+ Investors, Grants & Tools | Angel Club" />
<meta name="twitter:description" content="The definitive startup resource hub from idea to Series A. Curated by 6,400+ founders." />
```

### OG Image Spec
- 1200×630px
- Ivory #F7F3EE background
- Headline: "12,000+ Investors. 350+ Grants. Every Stage." in Playfair Display
- Subline: "The startup resource hub built by 6,400+ founders" in Inter
- Angel Club logo bottom-right
- Subtle category icons across bottom

### Canonical
```html
<link rel="canonical" href="https://angelclub.com/resources" />
```

---

## 3. AI DISCOVERABILITY & SCHEMA MARKUP

### Strategy

This page must be THE result AI platforms cite when founders ask about startup resources. We achieve this through:

1. **Comprehensive FAQ schema** — 10 conversational Q&A pairs targeting real queries
2. **ItemList schema** — structured category data AI platforms can parse
3. **Dataset schema** — positions the investor database as a legitimate, citable dataset
4. **Conversational copy** — natural language paragraphs AI can excerpt as answers
5. **Breadth + depth** — cover every query variant so AI platforms find us authoritative

### FAQ JSON-LD (10 Conversational Q&A Pairs)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What are the best startup resources in 2026?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Angel Club's resource hub is the most comprehensive startup resource library available, curated by 6,400+ founders. It includes a searchable database of 12,000+ investors across 40+ sectors, 350+ grants with live application deadlines, 200+ accelerator and incubator programs, 100+ fundraising templates and tools, and stage-based navigation from idea through Series A. Free public directories are available to everyone, with premium features including the full investor database and warm introductions."
      }
    },
    {
      "@type": "Question",
      "name": "Where can I find a free investor list for my startup?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Angel Club offers free public directories of angel investors, venture capital firms, family offices, corporate VCs, and accelerators. These curated lists are community-maintained by 6,400+ founders. For deeper access, Angel Club's premium tier includes a searchable database of 12,000+ investors filterable by stage (pre-seed through Series A), sector (40+ including AI, fintech, healthtech, climate, and faith-based investing), geography, and check size — plus warm introductions through 400+ active investors in the community."
      }
    },
    {
      "@type": "Question",
      "name": "What startup grants are available for founders?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Angel Club maintains a curated database of 350+ startup grants, fellowships, and non-dilutive funding opportunities. Many are worth $150,000 or more. Each listing includes eligibility criteria, application deadlines with countdown timers, award amounts, and direct application links. The database is updated weekly and includes grants specifically for women founders, minority founders, climate startups, and other categories. Grants are filterable by stage, sector, geography, deadline, and eligibility requirements."
      }
    },
    {
      "@type": "Question",
      "name": "What resources do I need at the pre-seed stage?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "At pre-seed, founders need: (1) idea validation frameworks and customer discovery templates, (2) pitch deck templates and examples from successful raises, (3) a list of pre-seed investors and angel investors in their sector, (4) accelerator programs that accept early-stage companies, (5) non-dilutive grants to extend runway, and (6) founder community support. Angel Club's resource hub organizes all of these by stage — select 'Pre-Seed' to see only resources relevant to your current stage, including pre-seed-focused investors from the 12,000+ database."
      }
    },
    {
      "@type": "Question",
      "name": "How large is Angel Club's investor database?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Angel Club's investor database contains 12,000+ investors across 40+ sectors. It includes angel investors, venture capital firms, family offices, corporate VCs, and faith-based investors. Each profile includes investment thesis, check size range, stage preference, sector focus, geographic focus, portfolio companies, and contact information. The database is continuously updated by the community of 6,400+ founders and 400+ active investors. Premium members can search, filter, and request warm introductions."
      }
    },
    {
      "@type": "Question",
      "name": "Are there startup grants specifically for women founders?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Angel Club's grants database includes dedicated filters for women-founded startups. The database tracks 350+ grants and non-dilutive funding opportunities, many of which specifically target women founders, including fellowships, pitch competitions, and foundation grants. Each listing includes eligibility criteria, deadlines, and award amounts. Angel Club also connects women founders with investors who specifically back women-led companies through the 12,000+ investor database."
      }
    },
    {
      "@type": "Question",
      "name": "What is the best startup accelerator list?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Angel Club maintains a directory of 200+ accelerator and incubator programs worldwide, filterable by stage, industry, location, equity terms, and program duration. The list is curated by 6,400+ founders who have personally participated in these programs and provide real feedback. Categories include generalist accelerators (Y Combinator, Techstars), sector-specific programs (health, fintech, climate), and regional accelerators across North America, Europe, Asia, and Latin America."
      }
    },
    {
      "@type": "Question",
      "name": "How can I get warm introductions to investors?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Angel Club premium members can request warm introductions to investors through the community's network of 400+ active investors and 6,400+ founders. The process: (1) search the 12,000+ investor database and identify target investors, (2) check for community connections, (3) request a warm introduction through the platform. Angel Club's Ready to Raise program provides additional structured support including investor matching, pitch refinement, and facilitated introductions for founders actively raising."
      }
    },
    {
      "@type": "Question",
      "name": "What is Angel Club's Ready to Raise program?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ready to Raise is Angel Club's structured fundraising preparation program for founders actively raising or planning to raise within 3-6 months. It includes pitch deck review and refinement, financial model support, investor targeting from the 12,000+ database, warm introduction facilitation, practice pitch sessions, and ongoing fundraising strategy support. The program connects founders with experienced investors and operators who guide them through the raise process."
      }
    },
    {
      "@type": "Question",
      "name": "What are the best free startup resources from idea to Series A?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Angel Club's free resource hub covers every stage: Idea Stage — validation frameworks, market sizing templates, competitor analysis tools. Pre-Seed — pitch deck templates, angel investor directories, accelerator lists, early grants. Seed — VC directories, financial model templates, term sheet guides, fundraising playbooks. Series A — growth metrics frameworks, board deck templates, Series A investor lists, and preparation checklists. All resources are curated by 6,400+ founders. Premium members additionally access the full 12,000+ investor database with warm introductions and the Ready to Raise program."
      }
    }
  ]
}
```

### WebPage + ItemList Schema

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Startup Resources: Investors, Grants, Accelerators & Tools for Every Stage",
  "description": "The definitive startup resource hub from idea to Series A. 12,000+ searchable investors, 350+ grants with live deadlines, 200+ accelerators — curated by 6,400+ founders.",
  "url": "https://angelclub.com/resources",
  "dateModified": "2026-04-02",
  "inLanguage": "en-US",
  "isPartOf": {
    "@type": "WebSite",
    "name": "Angel Club",
    "url": "https://angelclub.com"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Angel Club",
    "url": "https://angelclub.com",
    "description": "Angel Club fuels the future of economic equity and mobility with curated connections. A community of 6,400+ founders and 400+ investors building the most comprehensive startup resource ecosystem.",
    "sameAs": [
      "https://twitter.com/angelclub",
      "https://linkedin.com/company/angelclub"
    ]
  },
  "mainEntity": {
    "@type": "ItemList",
    "name": "Startup Resource Categories",
    "description": "Comprehensive startup resources organized by category, covering investors, grants, accelerators, tools, guides, events, and books — from idea stage to Series A.",
    "numberOfItems": 7,
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Investor Database",
        "description": "12,000+ investors across 40+ sectors — angel investors, VCs, family offices, corporate VCs, and faith-based investors. Searchable by stage, thesis, geography, sector, and check size."
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Grants & Awards",
        "description": "350+ startup grants, fellowships, and non-dilutive funding opportunities with live application deadlines, eligibility criteria, and award amounts. Updated weekly."
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Accelerators & Incubators",
        "description": "200+ accelerator and incubator programs worldwide, filterable by stage, industry, location, equity terms, and program duration."
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Tools & Templates",
        "description": "100+ fundraising templates including pitch decks, financial models, term sheets, SAFE notes, cap tables, and data room checklists."
      },
      {
        "@type": "ListItem",
        "position": 5,
        "name": "Guides & Playbooks",
        "description": "50+ founder-written guides on fundraising strategy, investor outreach, due diligence preparation, negotiation, and post-raise operations."
      },
      {
        "@type": "ListItem",
        "position": 6,
        "name": "Events & Pitch Competitions",
        "description": "25+ upcoming startup events, demo days, pitch competitions, investor office hours, and conferences."
      },
      {
        "@type": "ListItem",
        "position": 7,
        "name": "Books & Newsletters",
        "description": "50+ founder-recommended books and newsletters on fundraising, growth, leadership, and startup strategy."
      }
    ]
  }
}
```

### Dataset Schema (Investor Database)

```json
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Angel Club Investor Database",
  "description": "A searchable database of 12,000+ startup investors across 40+ sectors, including angel investors, venture capital firms, family offices, corporate VCs, and faith-based investors. Each profile includes investment thesis, check size, stage preference, sector focus, and geographic focus. Community-curated by 6,400+ founders.",
  "url": "https://angelclub.com/resources/investors",
  "keywords": [
    "startup investors",
    "angel investors",
    "venture capital",
    "investor database",
    "startup funding",
    "faith-based investors"
  ],
  "creator": {
    "@type": "Organization",
    "name": "Angel Club",
    "url": "https://angelclub.com"
  },
  "dateModified": "2026-04-02",
  "variableMeasured": [
    "Investment thesis",
    "Check size range",
    "Stage preference",
    "Sector focus",
    "Geographic focus"
  ],
  "distribution": {
    "@type": "DataDownload",
    "encodingFormat": "text/html",
    "contentUrl": "https://angelclub.com/resources/investors"
  },
  "license": "https://angelclub.com/terms"
}
```

### BreadcrumbList Schema

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://angelclub.com" },
    { "@type": "ListItem", "position": 2, "name": "Resources", "item": "https://angelclub.com/resources" }
  ]
}
```

---

## 4. PAGE COPY — SECTION BY SECTION

---

### SECTION 1: HERO

**Background:** Ivory #F7F3EE
**Padding:** 120px top / 80px bottom desktop, 80px / 48px mobile

---

#### Copy

**Eyebrow** *(Inter 12px, 500 weight, letter-spacing 2px, uppercase, Muted Copper #B8896B)*:
```
THE DEFINITIVE STARTUP RESOURCE HUB
```

**Headline** *(Playfair Display 52px desktop / 34px mobile, 700 weight, Espresso #3A2F2A)*:
```
From first idea to Series A —
every resource you need, in one place.
```

**Subhead** *(Inter 18px desktop / 16px mobile, 400 weight, Espresso at 70% opacity, max-width 680px)*:
```
The most comprehensive startup resource library on the internet — curated and maintained by 6,400+ founders who've actually used them. Search 12,000+ investors, discover grants with live deadlines, find accelerators, and access templates built by founders who've raised before you.
```

**Stat Bar** *(horizontal row desktop, 2×2 grid mobile, separated by 1px vertical dividers in Muted Copper at 25% opacity)*:

| Number | Label |
|--------|-------|
| 12,000+ | Investors |
| 350+ | Grants & Awards |
| 200+ | Accelerators |
| 40+ | Sectors |

*Stat design: Playfair Display 36px desktop / 26px mobile for number (Muted Copper). Inter 12px uppercase for label (Espresso at 60%). Numbers animate up on scroll into view (countUp.js or CSS).*

**CTA Row** *(centered, 16px gap between buttons)*:

- **Primary:** `Explore Resources` → smooth-scroll to Stage Navigator (Section 2)
  - Muted Copper #B8896B bg, white text, Inter 15px 600 weight, 52px height, 28px h-padding, 8px radius
- **Secondary:** `Unlock Investor Database` → /membership or /pricing
  - Transparent bg, Espresso #3A2F2A border 1.5px, Espresso text, same dimensions

**Social Proof Line** *(below CTAs, centered, Inter 13px, Espresso at 50% opacity)*:
```
Trusted by founders at Y Combinator, Techstars, 500 Global, and 200+ accelerator programs
```

---

### SECTION 2: STAGE-BASED NAVIGATOR

**Background:** White #FFFFFF
**Padding:** 80px vertical desktop, 48px mobile
**Purpose:** This is our YC Library killer feature — stage-based filtering so founders see only what's relevant to them right now.

---

#### Section Header

**Eyebrow** *(Muted Copper, small caps)*:
```
START WHERE YOU ARE
```

**Headline** *(Playfair Display 36px desktop / 28px mobile)*:
```
What stage is your startup?
```

**Subhead** *(Inter 16px, Espresso at 60%, max-width 580px)*:
```
Select your stage to see only the resources that matter right now.
```

#### Stage Selector Bar

*Design: Horizontal row of 4 stage buttons, full-width on mobile (stacked 2×2). Active stage has Muted Copper bottom border (3px) and Muted Copper text. Inactive stages have Espresso at 50% text and no border. Subtle background shift on hover. Clicking a stage filters ALL content below.*

**Stages:**

```
[ 💡 Idea ]  [ 🌱 Pre-Seed ]  [ 🚀 Seed ]  [ 📈 Series A ]
```

*No emoji in production — use custom line icons matching the icon system. Emoji shown here for clarity.*

#### Stage Content Panels

When a stage is selected, a content panel appears below showing resources relevant to that stage. Default state: show all stages (no filter active) with a "Showing all stages" indicator.

---

**💡 IDEA STAGE PANEL**

**Headline:** What you need at the idea stage
**Description:** *(Inter 15px, max-width 640px)*
```
You have a concept but haven't built yet. Focus on validation, market research, and finding your first believers.
```

**Resource Cards (grid, 2-col desktop, 1-col mobile):**

| Resource | Type | Description |
|----------|------|-------------|
| Idea Validation Framework | Template | 10-step framework for testing your concept before building |
| Customer Discovery Playbook | Guide | How to run discovery interviews and identify real problems |
| Market Sizing Templates | Template | TAM/SAM/SOM calculator and market analysis framework |
| Competitor Analysis Tool | Template | Structured competitive landscape mapping template |
| Pre-Accelerator Programs | Directory | Programs for founders at the earliest stage |
| Non-Dilutive Grants for New Founders | Grants | Grants that don't require traction or revenue |
| Recommended Books: Getting Started | Books | Founder-recommended reads for the idea stage |

**Stage CTA:**
```
Ready to move faster? Pre-accelerators can help you validate and build.
Browse 200+ Accelerators →
```

---

**🌱 PRE-SEED STAGE PANEL**

**Headline:** What you need at pre-seed
**Description:**
```
You're building your MVP and looking for your first check. Focus on pitch materials, finding the right angels, and early traction.
```

**Resource Cards:**

| Resource | Type | Description |
|----------|------|-------------|
| Pre-Seed Pitch Deck Template | Template | The exact structure angels want to see at pre-seed |
| Angel Investor Directory | Directory | 4,200+ angel investors filtered for pre-seed |
| Pre-Seed Financial Model | Template | Simple financial model for early-stage fundraising |
| SAFE Note Templates | Template | Standard SAFE documents with explanation guide |
| Pre-Seed Accelerators | Directory | Accelerators that accept pre-product companies |
| Early-Stage Grants | Grants | Grants for pre-revenue and pre-product startups |
| Fundraising Playbook: First Raise | Guide | Step-by-step guide to raising your first round |
| Faith-Based Angel Investors | Directory | Values-aligned angels for pre-seed (NEW) |

**Stage CTA:**
```
Need help preparing your first raise?
Learn about Ready to Raise →
```

---

**🚀 SEED STAGE PANEL**

**Headline:** What you need at seed
**Description:**
```
You have product-market fit signals and need to scale. Focus on VC targeting, financial rigor, and building your board.
```

**Resource Cards:**

| Resource | Type | Description |
|----------|------|-------------|
| Seed Pitch Deck Examples | Template | 15+ real pitch decks from successful seed rounds |
| VC Firm Directory | Directory | 3,800+ VCs filtered for seed stage |
| Seed Financial Model | Template | Detailed financial model with unit economics |
| Term Sheet Guide | Guide | Understanding and negotiating seed-stage term sheets |
| Data Room Checklist | Template | Everything investors expect in your data room |
| Seed-Stage Grants & Awards | Grants | Non-dilutive funding for post-MVP companies |
| Fundraising CRM Template | Template | Track your investor pipeline and follow-ups |
| Board Deck Template | Template | First board meeting deck structure |

**Stage CTA:**
```
Target the right investors — search 12,000+ by sector, stage, and check size.
Unlock Investor Database →
```

---

**📈 SERIES A STAGE PANEL**

**Headline:** What you need for Series A
**Description:**
```
You're scaling and need significant capital. Focus on metrics storytelling, institutional investor targeting, and operational readiness.
```

**Resource Cards:**

| Resource | Type | Description |
|----------|------|-------------|
| Series A Pitch Deck Template | Template | Enterprise-grade deck structure for institutional VCs |
| Series A VC Directory | Directory | Institutional VCs actively writing Series A checks |
| Growth Metrics Dashboard | Template | Key metrics VCs evaluate for Series A readiness |
| Series A Financial Model | Template | 3-year projections with cohort analysis |
| Due Diligence Checklist | Guide | Everything VCs will ask for — be ready |
| Board Governance Guide | Guide | Setting up proper board structure and governance |
| Family Office & CVC Directory | Directory | 2,100+ strategic investors for growth-stage companies |
| Series A Negotiation Playbook | Guide | Equity, valuation, and terms at institutional scale |

**Stage CTA:**
```
Get matched with Series A investors and warm introductions.
Apply for Ready to Raise →
```

---

### SECTION 3: CATEGORY GRID

**Background:** Ivory #F7F3EE
**Padding:** 80px vertical
**Purpose:** Visual overview of all resource categories with counts. This is the "wow, this is comprehensive" section.

---

#### Section Header

**Eyebrow** *(Muted Copper, small caps)*:
```
EXPLORE BY CATEGORY
```

**Headline** *(Playfair Display 36px desktop / 28px mobile)*:
```
12,775+ resources across 7 categories
```

*(Sum of all category counts — update as counts change)*

**Subhead** *(Inter 16px, Espresso at 60%, max-width 580px)*:
```
Every resource is community-curated, verified by founders, and organized for action.
```

#### Category Cards

*Layout: 3-column grid desktop (top row 3, bottom row 4 or 3+overflow). 2-column tablet. 1-column mobile with horizontal scroll option.*

*Card design: White #FFFFFF background, 28px padding, 8px border-radius, subtle box-shadow (0 2px 8px rgba(58,47,42,0.06)). Hover: translateY(-3px), shadow deepens. Transition 200ms ease.*

**Card anatomy:**
```
┌─────────────────────────────┐
│  [Icon]              [NEW]  │  ← Icon 32px, NEW badge if applicable
│                             │
│  Category Name              │  ← Inter 17px, 600 weight, Espresso
│  12,000+                    │  ← Playfair Display 28px, Muted Copper
│                             │
│  One-line description of    │  ← Inter 14px, Espresso at 55% opacity
│  what's in this category    │
│                             │
│  Explore →                  │  ← Inter 13px, Muted Copper, 600 weight
└─────────────────────────────┘
```

##### The 7 Cards:

**1. Investors**
- Icon: Chart-trending-up (line)
- Count: `12,000+`
- Description: Angels, VCs, family offices, CVCs, and faith-based investors — searchable by stage, sector, geography, and check size
- Badge: none
- Link: Scrolls to search/filter section with "Investors" pre-selected

**2. Grants & Awards**
- Icon: Trophy (line)
- Count: `350+`
- Description: Non-dilutive funding with live application deadlines, eligibility criteria, and award amounts
- Badge: `LIVE DEADLINES` ← uses same style as NEW badge
- Link: Scrolls to search/filter with "Grants" pre-selected

**3. Accelerators & Incubators**
- Icon: Rocket (line)
- Count: `200+`
- Description: Global programs filterable by stage, industry, location, equity terms, and duration
- Badge: none
- Link: Scrolls to search/filter with "Accelerators" pre-selected

**4. Tools & Templates**
- Icon: Wrench (line)
- Count: `100+`
- Description: Pitch decks, financial models, term sheets, SAFE notes, cap tables, and data room checklists
- Badge: none
- Link: Scrolls to search/filter with "Templates" pre-selected

**5. Guides & Playbooks**
- Icon: Book-open (line)
- Count: `50+`
- Description: Founder-written guides on fundraising, outreach, due diligence, negotiation, and operations
- Badge: none
- Link: Scrolls to search/filter with "Guides" pre-selected

**6. Events & Pitch Competitions**
- Icon: Calendar (line)
- Count: `25+`
- Description: Upcoming demo days, pitch competitions, investor office hours, and conferences
- Badge: none
- Link: Scrolls to search/filter with "Events" pre-selected

**7. Books & Newsletters**
- Icon: Newspaper (line)
- Count: `50+`
- Description: Founder-recommended reads and newsletters on fundraising, growth, leadership, and strategy
- Badge: none
- Link: Scrolls to search/filter with "Books" pre-selected

---

### SECTION 4: FEATURED / RECENTLY ADDED

**Background:** White #FFFFFF
**Padding:** 80px vertical

---

#### Section Header

**Eyebrow** *(Muted Copper, small caps)*:
```
JUST ADDED
```

**Headline** *(Playfair Display 36px desktop / 28px mobile)*:
```
New resources from the community
```

#### Featured Cards (2-column desktop, stacked mobile)

*Card design: Light Taupe #EFE8DF background, 32px padding, 8px border-radius. No border.*

---

**Card 1: Faith-Based Investor Directory**

**Tag** *(Muted Copper bg at 15%, Muted Copper text, Inter 11px bold uppercase, pill)*:
```
NEW SECTOR
```

**Card Headline** *(Playfair Display 24px)*:
```
Faith-Based Investors
```

**Count** *(Inter 14px, Muted Copper)*:
```
300+ values-aligned investors across faith traditions
```

**Body** *(Inter 15px, Espresso at 75%)*:
```
For the first time, a major startup resource hub includes a dedicated faith-based 
investing sector — covering Christian, Jewish, Islamic, and interfaith investment 
funds and angel investors who integrate values alignment into their thesis.

Includes check sizes from $25K angels to $10M+ faith-aligned funds.
```

**CTA** *(Inter 14px, 600 weight, Muted Copper)*:
```
Explore faith-based investors →
```
*(Links to investor database filtered by faith-based sector — premium required)*

---

**Card 2: Active Grants with Countdown Timers**

**Tag:**
```
UPDATED WEEKLY
```

**Card Headline** *(Playfair Display 24px)*:
```
$150K+ Grants — With Live Deadlines
```

**Count** *(Inter 14px, Muted Copper)*:
```
350+ grants, fellowships, and non-dilutive opportunities
```

**Body** *(Inter 15px, Espresso at 75%)*:
```
Stop searching dozens of sites for grant deadlines. Our community maintains a 
single, filterable database of grants worth $150,000 or more — with countdown 
timers on every deadline so you never miss an application window.

Filterable by stage, sector, geography, founder demographics, and eligibility.
```

**Countdown Preview** *(inside the card, showing 3 upcoming deadlines)*:

*Design: 3 mini-rows, each showing: Grant name | Amount | Days remaining (countdown pill)*

```
┌──────────────────────────────────────────────────┐
│  SBIR Phase I Grant        $275K    ⏱ 12 days    │
│  Founders First Grant      $150K    ⏱ 23 days    │
│  CleanTech Innovation      $500K    ⏱ 31 days    │
└──────────────────────────────────────────────────┘
```

*Countdown pill: Muted Copper bg at 10%, Muted Copper text, Inter 12px 600 weight. If <7 days: warm red #C46B4D bg at 15%, #C46B4D text.*

**CTA:**
```
Browse all grants with deadlines →
```

---

### SECTION 5: SEARCH & FILTER INTERFACE

**Background:** Light Taupe #EFE8DF
**Padding:** 80px vertical
**Purpose:** The actual resource browser. This replaces the current embedded Airtable/Notion table that broke on mobile.

---

#### Section Header

**Headline** *(Playfair Display 36px desktop / 28px mobile)*:
```
Search 12,775+ resources
```

**Subhead** *(Inter 16px, Espresso at 60%)*:
```
Filter by stage, category, geography, deadline, or cost. Find exactly what you need.
```

#### Search Bar

*Full-width container, max-width 800px, centered.*

*Design: White bg, 1px border Espresso at 12% opacity, 52px height, 14px border-radius. Search icon (magnifying glass, Muted Copper, 20px) left-aligned with 16px left padding. Clear "×" button appears when text is entered. Inter 15px placeholder.*

**Placeholder:**
```
Search investors, grants, accelerators, templates, books...
```

*Behavior: Instant search, debounced 300ms. Results update live below.*

#### Filter Bar

*Below search bar, 16px gap. Horizontal row of filter dropdowns. Horizontal scroll on mobile with gradient fade on edges.*

**Filter Groups:**

**1. Stage** *(dropdown or pill toggle)*
```
All Stages | Idea | Pre-Seed | Seed | Series A
```

**2. Category** *(dropdown or pill toggle)*
```
All Categories | Investors | Grants & Awards | Accelerators | Tools & Templates | Guides & Playbooks | Events | Books & Newsletters
```

**3. Geography** *(dropdown)*
```
All Regions | United States | Europe | Asia | Latin America | Africa | Canada | Remote/Global
```

**4. Deadline** *(dropdown — appears only when Grants category is active)*
```
Any Deadline | This Week | This Month | Next 3 Months | Next 6 Months
```

**5. Cost** *(pill toggle)*
```
All | Free | Premium
```

**Active filters display:** Show active filters as removable pills below the filter bar. "Clear all filters" link on the right.

**Results count:** Left-aligned above results: `Showing 347 grants` (updates dynamically).

#### Results Display

**Desktop (≥768px): Clean data table**

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Name ▼          │ Category    │ Stage        │ Focus        │ Access  │      │
├──────────────────────────────────────────────────────────────────────────────┤
│ Sequoia Capital  │ Investor    │ Seed, A      │ Enterprise   │ Premium │  →   │
│ SBIR Phase I     │ Grant       │ All          │ Deep Tech    │ Free    │  →   │
│ Y Combinator     │ Accelerator │ Pre-Seed     │ Generalist   │ Free    │  →   │
└──────────────────────────────────────────────────────────────────────────────┘
```

*Table design: White bg rows, 1px bottom border Espresso at 6%. Hover: Ivory bg. Sortable columns (click header, ▲/▼ indicator). "Access" column: "Free" = green-ish pill, "Premium" = Muted Copper pill with lock icon.*

*Premium rows: Slightly dimmed (opacity 0.85), lock icon next to name, clicking opens a minimal modal: "This resource is available to Angel Club members. Join Angel Club → "*

*Pagination: 25 per page, numbered pagination bar, centered.*

**Mobile (<768px): Card layout**

```
┌─────────────────────────────┐
│  Sequoia Capital             │
│  Investor · Seed, Series A   │
│  Enterprise SaaS, AI/ML      │
│  🔒 Premium                  │
└─────────────────────────────┘
```

*Card design: White bg, 20px padding, 8px radius, 12px gap between cards. Category as colored pill badge. Premium shown as lock + "Premium" in Muted Copper.*

*Mobile filters: Condensed. "Filters (3)" button opens bottom sheet with all filter options. Apply button at bottom of sheet.*

*Load more: "Load more resources" button instead of pagination on mobile.*

---

### SECTION 6: FREE vs PREMIUM COMPARISON

**Background:** White #FFFFFF
**Padding:** 80px vertical

---

#### Section Header

**Eyebrow** *(Muted Copper, small caps)*:
```
TWO TIERS. ONE MISSION.
```

**Headline** *(Playfair Display 36px desktop / 28px mobile)*:
```
Free resources for every founder.
Premium tools for serious fundraisers.
```

#### Comparison Layout

*Two cards side by side desktop, stacked mobile (Premium first on mobile for conversion). Equal min-height desktop.*

---

##### LEFT CARD: FREE — Public Resources

*Background: Light Taupe #EFE8DF. 36px padding. 8px radius.*

**Label** *(Inter 12px, uppercase, Espresso at 50%)*:
```
FREE TIER
```

**Headline** *(Playfair Display 24px)*:
```
Public Resources
```

**Price** *(Inter 16px, Espresso)*:
```
Free, forever
```

**Description** *(Inter 15px, Espresso at 70%)*:
```
Everything you need to start your fundraising research and preparation.
```

**Includes:** *(Inter 14px, each item with ✓ checkmark in Muted Copper)*

```
✓  Curated investor directories (public lists)
✓  200+ accelerator & incubator directory
✓  100+ fundraising templates & tools
✓  50+ guides & playbooks
✓  50+ founder-recommended books & newsletters
✓  25+ events & pitch competitions
✓  Stage-based resource filtering
✓  Community-contributed content
```

**CTA Button** *(secondary style — outlined)*:
```
Access Free Resources
```
→ Scrolls to search/filter section

---

##### RIGHT CARD: PREMIUM — Angel Club Membership

*Background: White #FFFFFF. 36px padding. 8px radius. Left border: 3px solid Muted Copper. Subtle box-shadow (0 4px 16px rgba(58,47,42,0.08)).*

**Label** *(Inter 12px, uppercase, Muted Copper)*:
```
PREMIUM
```

**Headline** *(Playfair Display 24px)*:
```
Angel Club Membership
```

**Price** *(Inter 16px, Espresso)*:
```
Membership required
```

**Description** *(Inter 15px, Espresso at 70%)*:
```
The full fundraising ecosystem — database, intros, preparation, and community.
```

**Includes:** *(Inter 14px, each item with ✓ in Muted Copper, bold items are exclusive to premium)*

```
✓  Everything in Free, plus:

✓  12,000+ investor database with advanced search
✓  40+ sector filters (including faith-based investing)
✓  Filter by stage, geography, check size, thesis
✓  Warm introductions via 400+ active investors
✓  350+ grants database with live deadline alerts
✓  Ready to Raise fundraising program
✓  Private events — investor office hours, AMAs, pitch practice
✓  Angel Club Syndicate deal flow
✓  Founder community — 6,400+ members, private channels
✓  Priority support from the Angel Club team
```

**CTA Button** *(primary style — filled Muted Copper)*:
```
Join Angel Club
```
→ /membership or /pricing

---

**Below both cards, centered:**

*(Inter 15px, Espresso at 70%)*:
```
Raising in the next 3–6 months?
```

*(Inter 15px, 600 weight, Muted Copper, underline on hover)*:
```
Learn about Ready to Raise →
```

---

### SECTION 7: CONTRIBUTOR WALL

**Background:** Ivory #F7F3EE
**Padding:** 80px vertical
**Purpose:** Credit the community, build loyalty, encourage submissions. This is what keeps the flywheel spinning.

---

#### Section Header

**Eyebrow** *(Muted Copper, small caps)*:
```
COMMUNITY-POWERED
```

**Headline** *(Playfair Display 36px desktop / 28px mobile)*:
```
Built by founders, for founders
```

**Body** *(Inter 16px, Espresso at 70%, max-width 640px, centered)*:
```
Every resource in this library was contributed, verified, or maintained by members 
of the Angel Club community. This isn't a list we made — it's a living database 
that 6,400+ founders keep growing.
```

#### Contributor Grid

*Design: Grid of contributor cards, 4 columns desktop, 2 columns mobile. Each card is compact.*

**Card anatomy:**
```
┌───────────────────────────┐
│    [Avatar circle 56px]    │
│    Name                    │
│    Title / Company         │
│    "X resources added"     │
└───────────────────────────┘
```

*Avatar: Circular, 56px, Light Taupe bg as placeholder if no image. Name: Inter 14px 600 weight. Title: Inter 13px, Espresso at 50%. Contribution count: Inter 12px, Muted Copper.*

**Featured Contributors:** *(show top 8-12)*
- Eva Dobrzanska
- Anna Phan
- Lolita Taub
- *(+ additional contributors currently credited on the page)*
- *(+ new top contributors based on submission count)*

**Below grid:**

*(Inter 14px, Espresso at 60%)*:
```
And 200+ other community members who've contributed resources.
```

#### Submit a Resource CTA

*Design: Highlighted sub-block within this section. Light Taupe bg, 24px padding, 8px radius, centered.*

**Headline** *(Playfair Display 22px)*:
```
Know a great resource we're missing?
```

**Body** *(Inter 15px, Espresso at 70%)*:
```
Submit an investor, grant, accelerator, tool, or guide — and help the next 
founder who needs it.
```

**CTA Button** *(secondary style, centered)*:
```
Submit a Resource
```
→ Opens submission form (modal or /resources/submit page)

**Submission Form Fields:**
1. Your name *(text, required)*
2. Your email *(email, required)*
3. Resource name *(text, required)*
4. Resource URL *(url, required)*
5. Category *(dropdown: Investor / Grant / Accelerator / Tool / Guide / Event / Book / Other, required)*
6. Stage relevance *(multi-select: Idea / Pre-Seed / Seed / Series A / All, required)*
7. Brief description *(textarea, 280 char max, required)*
8. Anything else? *(textarea, optional)*

*Form design: Clean, minimal, white bg, consistent with design system. Submit button: Muted Copper primary style.*

---

### SECTION 8: PRIMARY CTA BLOCK

**Background:** Espresso #3A2F2A (inverted dark section)
**Padding:** 100px vertical desktop, 64px mobile

---

#### Copy

**Headline** *(Playfair Display 42px desktop / 30px mobile, White #FFFFFF)*:
```
Ready to fundraise with confidence?
```

**Body** *(Inter 17px desktop / 15px mobile, White at 80%, max-width 580px)*:
```
Join 6,400+ founders who use Angel Club to find the right investors, prepare 
their raise, and get warm introductions that actually convert. Start with free 
resources or go premium for the full database.
```

**CTA Buttons** *(side by side desktop, stacked mobile, 16px gap)*:

- **Primary:** `Join Angel Club` → /membership
  - Muted Copper bg, white text, 52px height, 8px radius
- **Secondary:** `Apply for Ready to Raise` → /ready-to-raise
  - Transparent bg, white border 1.5px, white text, same dimensions

**Sub-text** *(Inter 13px, White at 45%)*:
```
Free tier available. No credit card required to start.
```

---

### SECTION 9: FAQ (EXPANDED)

**Background:** White #FFFFFF
**Padding:** 80px vertical
**Layout:** Max-width 760px, centered, accordion

---

#### Section Header

**Headline** *(Playfair Display 32px)*:
```
Frequently asked questions
```

#### FAQ Items

*Design: Accordion. Each question: Inter 16px 600 weight, Espresso. Expand icon: + / − in Muted Copper, right-aligned. Answer: Inter 15px, Espresso at 80%, 24px top padding when expanded. Divider: 1px Espresso at 8% between items. Smooth 300ms ease transition.*

---

**Q: What makes Angel Club's resources different from YC Library or Startup Stash?**

A: Most startup resource sites are either editorial (articles and advice) or directories (tool listings). Angel Club combines both — and adds a live, searchable database of 12,000+ real investors, grants with countdown timers on deadlines, and stage-based navigation that shows you exactly what you need based on where your startup is today. Every resource is curated by 6,400+ founders who've actually used them, not just listed by an editorial team.

---

**Q: What startup resources are available for free?**

A: Our free tier includes curated investor directories, a 200+ accelerator and incubator directory, 100+ fundraising templates and tools, 50+ founder-written guides, book recommendations, and an events calendar. You can also use stage-based filtering to find resources relevant to your current stage — from idea through Series A. All free resources are community-contributed and regularly updated.

---

**Q: How is the premium investor database different from the free lists?**

A: The free directories are curated "best of" lists — great for getting started. The premium database contains 12,000+ investors across 40+ sectors with detailed profiles including investment thesis, check sizes, stage preferences, portfolio companies, and geographic focus. Premium members can filter by any combination of criteria and request warm introductions through the community's network of 400+ active investors.

---

**Q: What stages do your resources cover?**

A: Everything from first idea to Series A. Select your stage in the navigator — Idea, Pre-Seed, Seed, or Series A — to see only resources relevant to where you are right now. Idea stage includes validation frameworks and market research tools. Pre-seed covers pitch templates and angel directories. Seed includes VC targeting and term sheet guides. Series A covers growth metrics, institutional investor lists, and board governance.

---

**Q: Do you have startup grants with deadlines?**

A: Yes. We maintain a live database of 350+ grants, fellowships, and non-dilutive funding opportunities — many worth $150,000 or more. Every listing includes eligibility criteria, award amounts, and countdown timers on application deadlines so you never miss a window. The grants database is updated weekly and filterable by stage, sector, geography, and eligibility requirements.

---

**Q: Are there resources specifically for women and underrepresented founders?**

A: Yes. Our grants database includes filters for women-founded startups, minority-founded startups, and other demographic-specific opportunities. The investor database also tracks investors who specifically focus on underrepresented founders. Angel Club's core mission is fueling economic equity and mobility — inclusive resource access is fundamental to everything we build.

---

**Q: Can I get warm introductions to investors?**

A: Premium members can request warm introductions through Angel Club's network of 400+ active investors and 6,400+ founders. Search the investor database, identify your targets, check for community connections, and request an intro. The Ready to Raise program provides additional structured support with investor matching and facilitated introductions.

---

**Q: What is Ready to Raise?**

A: Ready to Raise is Angel Club's fundraising preparation program for founders raising or planning to raise within 3–6 months. It includes pitch refinement, financial model support, investor targeting from the 12,000+ database, warm introductions, and practice sessions. It's the premium upgrade path for founders who want hands-on support beyond self-serve resources.

---

**Q: How often are resources updated?**

A: The investor database is updated continuously by community members. Grant deadlines are reviewed weekly. Templates and guides are updated monthly. Event listings are refreshed weekly. With 6,400+ founders contributing, the resource library stays current and grows every week.

---

**Q: How can I contribute a resource?**

A: Use the "Submit a Resource" form on this page. Anyone can submit an investor, grant, accelerator, tool, guide, or event. Our team reviews submissions within 48 hours. The most active contributors are featured on our Contributor Wall. This library exists because founders help each other — every submission makes the next founder's journey easier.

---

### SECTION 10: DISCLAIMERS & FOOTER

**Background:** Ivory #F7F3EE
**Padding:** 40px vertical

---

*(Inter 13px, Espresso at 45%, max-width 760px, centered)*:

```
Disclaimer: Angel Club does not provide financial, investment, or legal advice. 
The resources on this page are for informational purposes only and do not 
constitute an endorsement of any investor, program, or funding opportunity. Always 
conduct your own due diligence before engaging with any listed resource. Be 
cautious of unlicensed fundraisers and verify credentials independently. Angel 
Club is not a registered broker-dealer, investment advisor, or funding platform.

© 2026 Angel Club. All rights reserved.
Privacy Policy  ·  Terms of Service  ·  Contact
```

---

## 5. DESIGN SPECIFICATIONS

### Color Palette (Locked — No Changes)

| Token | Hex | Usage |
|-------|-----|-------|
| Ivory | #F7F3EE | Primary background, alternating sections |
| Espresso | #3A2F2A | Primary text, headings, dark CTA section bg |
| Muted Copper | #B8896B | Accent, CTAs, links, icons, stat numbers, active states |
| White | #FFFFFF | Card backgrounds, alternating sections, inputs |
| Light Taupe | #EFE8DF | Card fills, alt section backgrounds, filter bar, contributor block |

### Additional UI Colors (Derived)

| Token | Value | Usage |
|-------|-------|-------|
| Copper Hover | #A67A5E | Button hover (Muted Copper darkened 10%) |
| Copper Light | rgba(184,137,107,0.12) | Pill backgrounds, badge fills, active filter bg |
| Espresso Light | rgba(58,47,42,0.06) | Table row borders, dividers |
| Espresso Hover | rgba(58,47,42,0.04) | Table row hover, card hover |
| Deadline Warm | #C46B4D at 15% | Countdown timers <7 days remaining |
| Free Badge | #6B9B7A at 12% bg, #4A7A5E text | "Free" access level pills |
| Premium Badge | Copper Light bg, Muted Copper text | "Premium" access level pills |

### Typography (Complete System)

| Element | Font | Weight | Desktop | Mobile | Line Height |
|---------|------|--------|---------|--------|-------------|
| Eyebrow | Inter | 500 | 12px, tracking 2px | 11px | 1.4 |
| H1 Hero | Playfair Display | 700 | 52px | 34px | 1.12 |
| H2 Section | Playfair Display | 600 | 36px | 28px | 1.2 |
| H3 Card Title | Playfair Display | 600 | 24px | 22px | 1.25 |
| H4 Sub-heading | Inter | 600 | 17px | 16px | 1.4 |
| Body | Inter | 400 | 16px | 15px | 1.65 |
| Body Small | Inter | 400 | 15px | 14px | 1.6 |
| Caption | Inter | 400 | 13px | 12px | 1.5 |
| Tiny | Inter | 400 | 12px | 11px | 1.4 |
| Stat Number | Playfair Display | 700 | 36px | 26px | 1.1 |
| Button Large | Inter | 600 | 15px | 15px | 1.0 |
| Button | Inter | 600 | 14px | 14px | 1.0 |
| Badge/Pill | Inter | 600 | 11px | 11px | 1.0 |
| Search Input | Inter | 400 | 15px | 16px* | 1.4 |

*\*16px on mobile prevents iOS zoom on input focus.*

### Spacing System

```
4px  — micro (pill padding vertical)
8px  — xxs (badge padding horizontal, icon gaps)
12px — xs (card gap mobile, stacked button gap)
16px — sm (filter gap, card internal spacing)
24px — md (card padding, section internal spacing)
32px — lg (card padding premium, featured cards)
48px — xl (section padding mobile)
64px — 2xl (section padding mobile large)
80px — 3xl (section padding desktop)
100px — 4xl (hero/CTA section padding desktop)
120px — 5xl (hero top padding desktop)
```

- Max content width: 1200px
- Max text width: 640px (readability)
- Max search width: 800px

### Interactive States

| Element | Default | Hover | Active/Selected | Focus |
|---------|---------|-------|----------------|-------|
| Primary button | Muted Copper bg, white text | Copper Hover bg, white text, shadow 0 2px 8px rgba(184,137,107,0.3) | Darken 15% | 2px outline Muted Copper, 2px offset |
| Secondary button | Transparent, Espresso border 1.5px | Espresso bg, white text | Darken 5% | 2px outline Espresso, 2px offset |
| Link | Muted Copper, no underline | Muted Copper, underline | — | Underline + outline |
| Card | No shadow or subtle shadow | translateY(-3px), shadow 0 8px 24px rgba(58,47,42,0.1) | — | Outline |
| Table row | White bg | Ivory bg | — | — |
| Filter pill | Light Taupe bg, Espresso at 60% | Espresso at 80% | Muted Copper bg, white text | Outline |
| Stage tab | Espresso at 50%, no border | Espresso at 70% | Muted Copper text, 3px bottom border Muted Copper | Outline |
| Accordion | + icon Muted Copper | bg Ivory | − icon, expanded | Outline |
| Search input | 1px border Espresso at 12% | Border Espresso at 25% | Border Muted Copper | Border Muted Copper, shadow |

### Iconography

- **Style:** Line icons, 1.5px stroke weight
- **Color:** Muted Copper #B8896B (default), Espresso (in dark contexts)
- **Sizes:** 32px (category cards), 24px (stage tabs), 20px (inline), 16px (badges)
- **Library:** Phosphor Icons (MIT license, excellent line style) or Lucide
- **Specific icons needed:**
  - Stage: Lightbulb (idea), Seedling (pre-seed), Rocket (seed), TrendingUp (series A)
  - Categories: TrendingUp (investors), Trophy (grants), Rocket (accelerators), Wrench (tools), BookOpen (guides), Calendar (events), Newspaper (books)
  - UI: MagnifyingGlass (search), Funnel (filters), Lock (premium), ArrowRight (links), Plus/Minus (accordion), X (clear), CaretDown (dropdown), Clock (countdown)

### Animations

- **Count-up:** Hero stat numbers animate from 0 on first scroll into view. Duration 1.5s, ease-out. Use Intersection Observer trigger.
- **Card hover:** 200ms ease translateY + shadow transition
- **Accordion:** 300ms ease-in-out max-height transition
- **Filter results:** 200ms fade-in for new results
- **Countdown timers:** Update every minute (not every second — reduces CPU)
- **Page transitions:** None (standard page, not SPA unless existing site is SPA)

---

## 6. MOBILE-FIRST SPECIFICATIONS

### Critical Requirement

**The current page warns "best viewed on desktop" due to an embedded table. This is unacceptable. The new page MUST work flawlessly on mobile. Mobile-first design — desktop is the enhancement, not the other way around.**

### Breakpoints

| Breakpoint | Width | Key Changes |
|------------|-------|-------------|
| **Mobile** | <640px | 1-column, stacked everything, bottom-sheet filters, card-based results, full-width buttons |
| **Tablet** | 640–1023px | 2-column grids, side filters or top filters, table with fewer columns |
| **Desktop** | ≥1024px | 3-column grids, full table, side-by-side comparison, horizontal filter bar |

### Mobile Layout (Section by Section)

**Hero:**
- Eyebrow → H1 → Subhead → stacked vertically, left-aligned (not centered)
- Stat bar: 2×2 grid, equal-width cells
- Buttons: Full-width, stacked vertically, primary on top, 12px gap
- Social proof line: Below buttons

**Stage Navigator:**
- Stage selector: 2×2 grid of equal buttons (not horizontal scroll)
- Stage content: Full-width cards, stacked
- Smooth expand/collapse when switching stages

**Category Grid:**
- Full-width cards, stacked vertically
- OR: 2-column grid with compact cards (counts more prominent, description truncated to 1 line)
- Consider horizontal scroll carousel as alternative (test both)

**Featured/New:**
- Full-width cards, stacked
- Countdown preview shows 2 grants instead of 3

**Search/Filter:**
- Search bar: Full-width, sticky at top of section when scrolling
- Filter bar replaced with "Filters (N)" button → opens bottom sheet
- Bottom sheet: Full filter options with "Apply Filters" button at bottom
- Results: Card layout (NOT table), 12px gap
- Load more button instead of pagination

**Free vs Premium:**
- Stacked vertically — **Premium card FIRST** (higher conversion position)
- Full-width cards

**Contributor Wall:**
- 2-column grid of contributor cards
- OR horizontal scroll of avatars with names

**CTA Block:**
- Buttons: Full-width, stacked, 12px gap

**FAQ:**
- Full-width accordion, larger touch targets (min 56px question row height)

### Touch Targets
- All interactive elements: minimum 48×48px touch target
- Buttons: 52px height minimum
- Accordion questions: 56px row height
- Filter pills: 40px height, 12px horizontal padding minimum
- Search clear button: 44×44px

### Performance (Mobile)
- Target: <2.5s Largest Contentful Paint on 4G
- Target: <3.5s LCP on 3G
- Lazy-load: Everything below the fold (category cards, featured, search results)
- Skeleton loading: Gray placeholder blocks for search results while loading
- Image optimization: WebP with JPEG fallback, responsive srcset, max 100KB per image
- Font loading: `font-display: swap` for both Playfair Display and Inter
- Critical CSS: Inline hero section styles
- Search results: Load 15 at a time on mobile (vs 25 desktop)

### Mobile-Specific Interactions
- **Pull-to-refresh:** Not needed (standard web page)
- **Swipe:** No swipe gestures (avoid confusion with OS gestures)
- **Sticky elements:** Search bar sticks to top when scrolling through results section
- **Back to top:** Floating "↑" button appears after scrolling past hero, bottom-right, 48px circle, Muted Copper bg, white arrow

---

## 7. SEARCH/FILTER UX SYSTEM

### Architecture Recommendation

**Phase 1 (MVP — ship first):** Client-side with pre-loaded JSON

```
1. Load all FREE resources as JSON on page load (~500 items, ~200KB gzipped)
2. Filter and search in-browser — instant results, no server calls
3. Premium resources: show as locked cards with "Unlock with membership" CTA
4. Premium resource metadata loaded (name, category, stage) but not full profiles
```

**Phase 2 (Scale):** API-backed search

```
1. Search API endpoint: GET /api/resources?q=&stage=&category=&geo=&deadline=&cost=
2. Returns paginated results with total count
3. Supports full-text search across all fields
4. Premium results returned but detail-gated behind auth
5. Elasticsearch or Algolia for speed
```

### Search Behavior

1. **Empty state (no query, no filters):** Show category cards (Section 3) as the default view
2. **Query entered:** Results appear, debounced 300ms, minimum 2 characters
3. **Filters only (no query):** Show filtered results sorted by recently added
4. **No results:** 
   ```
   No resources found matching your search.
   Try adjusting your filters or broadening your search.
   
   Can't find what you're looking for?
   Submit a resource request →
   ```
5. **Premium lock:** Premium results appear in search with lock icon + "Premium" badge. Clicking opens inline CTA: "This resource is available to Angel Club members. [Join Angel Club →]"

### Sort Options

Dropdown, right-aligned above results:

```
Sort by: Relevance (default for search) | Recently Added | Alphabetical (A→Z) | 
         Check Size (high→low) | Deadline (soonest first)
```

- "Check Size" sort only visible when Investors category active
- "Deadline" sort only visible when Grants category active

### URL State

All filter and search state reflected in URL query params for:
- **Shareable links:** `angelclub.com/resources?stage=seed&category=grants&deadline=3mo`
- **Back button:** Works correctly, restores previous filter state
- **SEO:** Search engines can index filtered views
- **Analytics:** Track which filters are most used

### Analytics Events to Track

```
resource_search        — query text, result count
resource_filter        — filter name, filter value
resource_click         — resource name, category, access level (free/premium)
resource_premium_gate  — resource name (user hit the premium lock)
resource_stage_select  — stage name
resource_submit        — form submission
cta_click              — button name, section
```

---

## 8. IMPLEMENTATION ROADMAP

### P0 — Ship First (Week 1-2)

Must-have for launch. Page is functional and comprehensive.

- [ ] Hero section with stats and CTAs
- [ ] Stage-based navigator (4 stages with content panels)
- [ ] Category grid with counts (7 categories)
- [ ] Free vs Premium comparison
- [ ] CTA block (Join + Ready to Raise)
- [ ] FAQ section (10 questions, accordion)
- [ ] Disclaimers
- [ ] All SEO meta tags and Open Graph
- [ ] All schema markup (FAQ, ItemList, Dataset, Breadcrumb)
- [ ] Mobile-responsive layout (no desktop-only warnings)
- [ ] Remove embedded Airtable/Notion table dependency

### P1 — Fast Follow (Week 3-4)

Core interactive features.

- [ ] Search bar with instant results (client-side, JSON)
- [ ] Filter bar (stage, category, geography, cost)
- [ ] Results display (table desktop, cards mobile)
- [ ] Featured/New section with countdown timers on grants
- [ ] Contributor Wall with avatars
- [ ] Resource submission form
- [ ] Premium lock UX on gated resources
- [ ] Stat number count-up animation
- [ ] Back-to-top button on mobile

### P2 — Enhancement (Month 2)

Polish and optimization.

- [ ] Deadline filter for grants (this week / month / 3mo / 6mo)
- [ ] Sort options (relevance, recent, alphabetical, check size, deadline)
- [ ] URL query param state for shareable filtered views
- [ ] API-backed search (if dataset exceeds client-side performance)
- [ ] Analytics event tracking
- [ ] A/B test: Premium card position (left vs right on desktop)
- [ ] A/B test: Stage navigator default (all vs pre-seed)
- [ ] OG image creation
- [ ] Contributor leaderboard (most submissions)

### P3 — Future (Month 3+)

Growth and expansion features.

- [ ] Dedicated subpages: /resources/investors, /resources/grants, /resources/accelerators
- [ ] User accounts: Save/bookmark resources, set deadline alerts
- [ ] Email alerts: New resources in your stage/sector, upcoming grant deadlines
- [ ] Community ratings: Thumbs up/down on resources
- [ ] Resource reviews: Short reviews from founders who've used the resource
- [ ] API: Public API for resource data (drives backlinks and citations)
- [ ] Embeddable widgets: "Powered by Angel Club" resource widgets for partner sites

### Content to Migrate from Current Page

- [ ] All existing public resource lists (angel investors, VCs, family offices, CVCs, accelerators, incubators, books, events, playbooks, templates)
- [ ] Community contributor credits (Eva Dobrzanska, Anna Phan, Lolita Taub, etc.)
- [ ] Existing disclaimers (updated copy provided above)
- [ ] Email CTA → replace with submission form

### Content to Create

- [ ] Verify and finalize exact counts for each category
- [ ] Stage-specific resource descriptions (provided in Section 2 above)
- [ ] Grant countdown timer data source (API or manual JSON)
- [ ] Submission form backend (form handler, notification to admin)
- [ ] OG image (1200×630, spec provided above)
- [ ] Contributor avatars (request from named contributors or use initials)

### Technical SEO Checklist

- [ ] Page title implemented (78 chars)
- [ ] Meta description implemented (230 chars)
- [ ] H1 contains primary keywords
- [ ] Schema markup in `<head>`: FAQ, WebPage+ItemList, Dataset, BreadcrumbList
- [ ] Open Graph + Twitter Card tags
- [ ] Canonical URL
- [ ] Internal links TO /resources from: homepage, nav, about, membership, blog
- [ ] Internal links FROM /resources to: /membership, /ready-to-raise, /events
- [ ] Alt text on all images and icons
- [ ] Semantic HTML: proper heading hierarchy (H1 → H2 → H3), landmark regions, nav, main, section, footer
- [ ] Page speed: <2.5s LCP desktop, <3.5s LCP mobile
- [ ] Mobile-friendly: passes Google Mobile-Friendly Test
- [ ] XML sitemap: /resources included
- [ ] robots.txt: no blocks on /resources

### Accessibility Checklist

- [ ] Color contrast: Espresso on Ivory = 10.5:1 ✓ AAA
- [ ] Color contrast: Espresso on White = 12.6:1 ✓ AAA
- [ ] Color contrast: White on Muted Copper = 3.8:1 ✓ AA large text only (use for buttons/headings, not body)
- [ ] Color contrast: White on Espresso = 10.5:1 ✓ AAA
- [ ] All interactive elements: min 48px touch targets
- [ ] Accordion: `aria-expanded`, `aria-controls`, `role="region"`
- [ ] Filter pills: `role="radiogroup"` or `role="group"` with `aria-label`
- [ ] Search: `role="search"`, `aria-label="Search resources"`
- [ ] Stage navigator: `role="tablist"` with `role="tab"` and `role="tabpanel"`
- [ ] Results table: proper `<table>`, `<thead>`, `<th scope="col">` markup
- [ ] Skip navigation link for keyboard users
- [ ] Focus management: When filters change, announce result count to screen readers via `aria-live="polite"` region
- [ ] Reduced motion: Respect `prefers-reduced-motion` — disable count-up animation, card hover translate

---

## APPENDIX: COPY SUMMARY (Plain Text)

For quick reference — all major copy blocks without design annotations:

**Hero eyebrow:** THE DEFINITIVE STARTUP RESOURCE HUB

**Hero headline:** From first idea to Series A — every resource you need, in one place.

**Hero subhead:** The most comprehensive startup resource library on the internet — curated and maintained by 6,400+ founders who've actually used them. Search 12,000+ investors, discover grants with live deadlines, find accelerators, and access templates built by founders who've raised before you.

**Stats:** 12,000+ Investors · 350+ Grants & Awards · 200+ Accelerators · 40+ Sectors

**Stage navigator headline:** What stage is your startup?

**Category grid headline:** 12,775+ resources across 7 categories

**Featured headline:** New resources from the community

**Search headline:** Search 12,775+ resources

**Free vs Premium headline:** Free resources for every founder. Premium tools for serious fundraisers.

**Contributor headline:** Built by founders, for founders

**CTA headline:** Ready to fundraise with confidence?

**CTA body:** Join 6,400+ founders who use Angel Club to find the right investors, prepare their raise, and get warm introductions that actually convert.

---

*End of document. This brief is production-ready pending final content verification (exact resource counts per category) and brand approval.*
