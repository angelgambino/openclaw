# Angel Club Resources Page — FINAL Production Copy & Design Brief

**Page:** angelclub.com/resources
**Last Updated:** April 2, 2026
**Status:** Production-ready

---

## TABLE OF CONTENTS

1. [SEO & Meta](#1-seo--meta)
2. [AI Discoverability & Schema Markup](#2-ai-discoverability--schema-markup)
3. [Page Copy — Section by Section](#3-page-copy--section-by-section)
4. [Design Specifications](#4-design-specifications)
5. [Mobile Specifications](#5-mobile-specifications)
6. [Search/Filter UX Recommendations](#6-searchfilter-ux-recommendations)
7. [Implementation Notes](#7-implementation-notes)

---

## 1. SEO & META

### Page Title
```
Startup Resources: 12,000+ Investors, Grants & Tools | Angel Club
```

### Meta Description
```
The most comprehensive startup resource library — built by 6,400+ founders. Free investor directories, grant databases with deadlines, accelerator lists, and templates. Premium members access 12,000+ investors across 40+ sectors with warm intros.
```

### H1 (visible on page)
```
The Startup Resource Library Built by 6,400+ Founders
```

### URL Structure
```
angelclub.com/resources (main)
angelclub.com/resources/investors (future subpage)
angelclub.com/resources/grants (future subpage)
angelclub.com/resources/accelerators (future subpage)
```

### Target Keywords (Primary)
- startup resources
- investor database
- startup funding resources
- free investor list
- startup grants with deadlines

### Target Keywords (Secondary)
- angel investor directory
- venture capital database
- faith-based investors
- startup accelerator list
- founder resources
- fundraising templates
- startup funding database
- investor warm introductions

### Open Graph Tags
```html
<meta property="og:title" content="Startup Resources: 12,000+ Investors, Grants & Tools | Angel Club" />
<meta property="og:description" content="The most comprehensive startup resource library — built by 6,400+ founders. Free directories, grants, tools. Premium: 12,000+ investor database with warm intros." />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://angelclub.com/resources" />
<meta property="og:image" content="https://angelclub.com/images/resources-og.jpg" />
<!-- OG image spec: 1200x630, ivory bg, headline text, category icons, Angel Club logo -->
```

### Canonical & Hreflang
```html
<link rel="canonical" href="https://angelclub.com/resources" />
```

---

## 2. AI DISCOVERABILITY & SCHEMA MARKUP

### FAQ JSON-LD (Place in `<head>`)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What startup resources does Angel Club offer for free?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Angel Club provides free public directories of angel investors, VCs, family offices, corporate VCs, accelerators, and incubators. Free members also get access to fundraising templates, pitch deck guides, founder playbooks, recommended books, and a curated events calendar. All resources are community-contributed by 6,400+ founders."
      }
    },
    {
      "@type": "Question",
      "name": "How large is Angel Club's investor database?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Angel Club's premium investor database includes 12,000+ investors across 40+ sectors, including angel investors, venture capitalists, family offices, corporate VCs, and faith-based investors. The database is continuously updated by the community and includes contact information, investment thesis, check sizes, and sector focus."
      }
    },
    {
      "@type": "Question",
      "name": "Can I get warm introductions to investors through Angel Club?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Angel Club premium members can request warm introductions to investors in the database through the community's network of 400+ active investors and 6,400+ founders. The Ready to Raise program provides structured fundraising support including investor matching and introduction facilitation."
      }
    },
    {
      "@type": "Question",
      "name": "What is Angel Club's Ready to Raise program?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ready to Raise is Angel Club's structured fundraising preparation program. It helps founders get investor-ready with pitch refinement, financial modeling support, investor targeting from the 12,000+ database, and warm introductions — all guided by experienced founders and investors in the community."
      }
    },
    {
      "@type": "Question",
      "name": "Does Angel Club have startup grants with deadlines?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Angel Club maintains a curated list of startup grants worth $150,000 or more, complete with application deadlines, eligibility criteria, and direct application links. This list is regularly updated and available to all members."
      }
    },
    {
      "@type": "Question",
      "name": "Is Angel Club's investor list free?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Angel Club offers two tiers. The free public resource directory includes curated lists of investors, accelerators, books, events, and templates. The premium investor database with 12,000+ investors, detailed profiles, sector filtering, and warm introduction access requires an Angel Club membership."
      }
    },
    {
      "@type": "Question",
      "name": "What sectors does Angel Club's investor database cover?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The database covers 40+ sectors including AI/ML, fintech, healthtech, climate, edtech, SaaS, biotech, consumer, hardware, Web3, faith-based investing, impact investing, and many more. Each investor profile includes their specific sector preferences and investment criteria."
      }
    }
  ]
}
```

### WebPage + ItemList Schema (Place in `<head>`)

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Startup Resources: Investors, Grants & Tools",
  "description": "The most comprehensive startup resource library — built by 6,400+ founders. Free directories, grants, tools. Premium: 12,000+ investor database with warm intros.",
  "url": "https://angelclub.com/resources",
  "publisher": {
    "@type": "Organization",
    "name": "Angel Club",
    "url": "https://angelclub.com",
    "description": "Angel Club fuels the future of economic equity and mobility with curated connections. A community of 6,400+ founders and 400+ investors."
  },
  "mainEntity": {
    "@type": "ItemList",
    "name": "Startup Resource Categories",
    "numberOfItems": 6,
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Investor Database",
        "description": "12,000+ investors across 40+ sectors — angel investors, VCs, family offices, corporate VCs, and faith-based investors"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Accelerators & Incubators",
        "description": "Curated directory of startup accelerators and incubator programs worldwide"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Grants & Non-Dilutive Funding",
        "description": "Startup grants worth $150K+ with application deadlines and eligibility criteria"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Fundraising Templates & Playbooks",
        "description": "Pitch deck templates, financial models, fundraising playbooks contributed by successful founders"
      },
      {
        "@type": "ListItem",
        "position": 5,
        "name": "Books & Learning",
        "description": "Founder-recommended books on fundraising, growth, leadership, and startup strategy"
      },
      {
        "@type": "ListItem",
        "position": 6,
        "name": "Events & Community",
        "description": "Curated startup events, pitch competitions, demo days, and networking opportunities"
      }
    ]
  }
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

## 3. PAGE COPY — SECTION BY SECTION

---

### SECTION 1: HERO

**Background:** Ivory #F7F3EE
**Layout:** Centered text, generous whitespace (120px top/bottom padding desktop, 80px mobile)

#### Copy

**Eyebrow** (small caps, Inter 12px, letter-spacing 2px, Muted Copper #B8896B):
```
THE STARTUP RESOURCE LIBRARY
```

**Headline** (Playfair Display, 48px desktop / 32px mobile, Espresso #3A2F2A):
```
Built by 6,400+ founders.
Open to everyone.
```

**Subhead** (Inter 18px desktop / 16px mobile, Espresso #3A2F2A at 70% opacity, max-width 640px):
```
The most comprehensive collection of investor databases, grants, accelerator directories, fundraising templates, and tools — curated and maintained by the Angel Club community.
```

**Stat Bar** (horizontal row, centered, separated by thin vertical dividers in Muted Copper at 30% opacity):

| Stat | Label |
|------|-------|
| 12,000+ | Investors |
| 40+ | Sectors |
| 6,400+ | Founders |
| 400+ | Active Investors |

*Design: Each stat uses Playfair Display 32px for the number, Inter 13px uppercase for the label. Muted Copper numbers, Espresso labels.*

**CTA Buttons** (side by side, centered, 16px gap):

- **Primary:** `Browse Free Resources` → scrolls to Section 2
  - Style: Muted Copper #B8896B background, white text, Inter 14px semibold, 48px height, 24px horizontal padding, 6px border-radius
- **Secondary:** `Unlock Full Database` → links to membership/pricing page
  - Style: Transparent background, Espresso #3A2F2A border (1.5px), Espresso text, same dimensions

---

### SECTION 2: RESOURCE CATEGORIES — VISUAL GRID

**Background:** White #FFFFFF
**Layout:** 3-column grid desktop, 2-column tablet, 1-column mobile. 80px vertical padding.

#### Section Header

**Eyebrow** (Muted Copper, small caps):
```
EXPLORE BY CATEGORY
```

**Headline** (Playfair Display, 36px desktop / 28px mobile):
```
Every resource a founder needs — in one place
```

#### Category Cards

Each card: Light Taupe #EFE8DF background, 24px padding, 8px border-radius, subtle hover lift (translateY -2px, box-shadow). No border.

**Card structure:**
- Icon (32x32, line-style, Muted Copper stroke)
- Category name (Inter 16px semibold, Espresso)
- Count badge (Inter 12px, Muted Copper bg at 15% opacity, Muted Copper text, pill shape)
- One-line description (Inter 14px, Espresso at 60% opacity)
- Arrow icon →

##### Cards:

**1. Angel Investors**
- Icon: Wings / angel icon
- Count: `4,200+`
- Description: Individual investors by sector, check size, and stage
- Links to: Investor database (premium) or public angel list (free)

**2. Venture Capital Firms**
- Icon: Chart-up icon
- Count: `3,800+`
- Description: VC firms filtered by stage, sector focus, and geography
- Links to: Investor database (premium) or public VC list (free)

**3. Family Offices & CVCs**
- Icon: Building icon
- Count: `2,100+`
- Description: Family offices, corporate VCs, and strategic investors
- Links to: Investor database (premium) or public list (free)

**4. Grants & Non-Dilutive Funding** ← NEW badge
- Icon: Gift / money icon
- Count: `200+`
- Description: Grants worth $150K+ with deadlines and eligibility
- Links to: Grants directory

**5. Accelerators & Incubators**
- Icon: Rocket icon
- Count: `500+`
- Description: Global programs by stage, industry, and location
- Links to: Accelerator directory

**6. Faith-Based Investors** ← NEW badge
- Icon: Heart-handshake icon
- Count: `300+`
- Description: Values-aligned investors across faith traditions
- Links to: Faith investors section (premium)

**7. Templates & Playbooks**
- Icon: Document icon
- Count: `75+`
- Description: Pitch decks, financial models, term sheets, and SAFE notes
- Links to: Templates section

**8. Books & Guides**
- Icon: Book icon
- Count: `120+`
- Description: Founder-recommended reads on fundraising and growth
- Links to: Books section

**9. Events & Pitch Competitions**
- Icon: Calendar icon
- Count: `50+`
- Description: Upcoming demo days, pitch events, and conferences
- Links to: Events calendar

*"NEW" badge design: Muted Copper background, white text, Inter 10px bold, uppercase, 4px border-radius, positioned top-right of card.*

---

### SECTION 3: FEATURED / RECENTLY ADDED

**Background:** Ivory #F7F3EE
**Layout:** 60px vertical padding

#### Section Header

**Eyebrow** (Muted Copper, small caps):
```
RECENTLY ADDED
```

**Headline** (Playfair Display, 36px desktop / 28px mobile):
```
Fresh resources from the community
```

#### Featured Items (2-column layout desktop, stacked mobile)

**Card 1: Faith-Based Investor Directory**

```
NEW SECTOR

Faith-Based Investors
300+ values-aligned investors across faith traditions

For the first time, Angel Club's investor database includes a dedicated 
faith-based investing sector — covering Christian, Jewish, Islamic, and 
interfaith investment funds and angel investors who integrate values 
alignment into their investment thesis.

Available to premium members →
```

*Design: White card, 32px padding, 8px border-radius. "NEW SECTOR" label in Muted Copper small caps. Headline in Playfair Display 24px. Body in Inter 15px. Link in Muted Copper with arrow.*

**Card 2: High-Value Grants Database**

```
UPDATED WEEKLY

$150K+ Startup Grants with Deadlines
200+ grants, fellowships, and non-dilutive funding opportunities

Stop searching dozens of sites for grant deadlines. Our community maintains 
a single, filterable database of grants worth $150,000 or more — complete 
with eligibility criteria, application links, and deadline alerts.

Browse grants →
```

*Same card design as above.*

---

### SECTION 4: FREE vs PREMIUM COMPARISON

**Background:** White #FFFFFF
**Layout:** Two-column comparison, 80px vertical padding

#### Section Header

**Eyebrow** (Muted Copper, small caps):
```
TWO WAYS TO ACCESS
```

**Headline** (Playfair Display, 36px desktop / 28px mobile):
```
Free resources for every founder. Premium tools for serious fundraisers.
```

#### Comparison Table

*Design: Two cards side by side, equal height. Free card has Light Taupe background. Premium card has a subtle Muted Copper left border (3px) on white background.*

##### FREE — Public Resources

**Price label:** Free, forever
**Description:** Everything you need to start your fundraising research.

**Includes:**
- ✓ Public investor directories (curated lists)
- ✓ Accelerator & incubator directory
- ✓ Fundraising templates & playbooks
- ✓ Recommended books list
- ✓ Events calendar
- ✓ Community-contributed guides

**CTA Button:** `Access Free Resources` (secondary style — outlined)

##### PREMIUM — Angel Club Membership

**Price label:** Membership required
**Description:** The full investor database with warm introductions and community support.

**Includes:**
- ✓ **Everything in Free, plus:**
- ✓ **12,000+ investor database** with advanced filtering
- ✓ **40+ sector filters** including faith-based investing
- ✓ **Warm introductions** through 400+ active investors
- ✓ **$150K+ grants database** with deadline alerts
- ✓ **Ready to Raise** fundraising preparation program
- ✓ **Private events** — investor office hours, AMAs, pitch practice
- ✓ **Founder community** — 6,400+ members, private channels
- ✓ **Priority support** from the Angel Club team

**CTA Button:** `Join Angel Club` (primary style — filled Muted Copper)

**Below comparison, centered:**
```
Not sure which is right for you?
```
**Link:** `Learn about Ready to Raise →` (Muted Copper, underline on hover)

---

### SECTION 5: SEARCH & FILTER INTERFACE

**Background:** Light Taupe #EFE8DF
**Layout:** 60px vertical padding

#### Section Header

**Headline** (Playfair Display, 32px):
```
Find exactly what you need
```

**Subhead** (Inter 16px, 60% opacity):
```
Search and filter across every resource in our library.
```

#### Search Bar

*Design: Full-width (max 720px), centered, white background, 1px Espresso border at 15% opacity, 48px height, 12px border-radius, search icon left-aligned in Muted Copper, Inter 15px placeholder text.*

**Placeholder text:**
```
Search investors, grants, accelerators, templates...
```

#### Filter Pills (horizontal scrollable row below search)

**Filter groups:**

- **Type:** All | Investors | Grants | Accelerators | Templates | Books | Events
- **Stage:** Pre-Seed | Seed | Series A | Series B+
- **Sector:** All Sectors | AI/ML | Fintech | Healthtech | Climate | SaaS | Faith-Based | [+37 more]
- **Check Size:** <$50K | $50K–$250K | $250K–$1M | $1M+
- **Access:** Free | Premium

*Design: Pill-shaped buttons, Light Taupe background, Espresso text at 70% opacity. Active state: Muted Copper background, white text. Horizontal scroll with fade-out gradient on mobile edges.*

#### Resource Table / Cards

**Desktop view:** Clean data table
- Columns: Name | Type | Sector Focus | Stage | Check Size | Access Level
- Sortable columns (click header to sort)
- Hover row highlight (Ivory background)
- Pagination: 25 results per page, numbered pagination

**Mobile view:** Card layout (NOT table)
- Each result as a card with key info stacked vertically
- Swipe-friendly
- Load more button instead of pagination

*Design note: This replaces the current embedded Airtable/Notion table that requires desktop viewing. Build as a native responsive component.*

---

### SECTION 6: COMMUNITY CONTRIBUTORS

**Background:** Ivory #F7F3EE
**Layout:** 60px vertical padding, centered

#### Section Header

**Eyebrow** (Muted Copper, small caps):
```
COMMUNITY-POWERED
```

**Headline** (Playfair Display, 32px):
```
Built by founders, for founders
```

**Body** (Inter 16px, max-width 640px, centered):
```
Every resource in this library was contributed, verified, or maintained by 
members of the Angel Club community. Special thanks to our most active 
contributors:
```

#### Contributors

*Design: Horizontal row of circular avatar placeholders (48px) with names below, or a clean text list if no avatars available. Max 8 shown, "and X more" link.*

**Named Contributors:**
- Eva Dobrzanska
- Anna Phan
- Lolita Taub
- [Additional community contributors as currently listed on page]

**Below contributors:**
```
Want to contribute? We welcome additions from founders, investors, and 
advisors who want to help the community.
```

**CTA Link:** `Submit a resource →` (opens form/modal, NOT email)

*Design note: Replace the current "email admin@angelclub.com" CTA with a form submission. Fallback if no form exists: mailto link styled as a button, with copy "Submit a Resource" rather than exposing the raw email address.*

---

### SECTION 7: PRIMARY CTA BLOCK

**Background:** Espresso #3A2F2A (dark section — inverted colors)
**Layout:** Centered text, 100px vertical padding desktop, 60px mobile

#### Copy

**Headline** (Playfair Display, 40px desktop / 28px mobile, White):
```
Ready to fundraise with confidence?
```

**Body** (Inter 16px, White at 80% opacity, max-width 560px):
```
Join 6,400+ founders who use Angel Club to find the right investors, 
prepare their raise, and get warm introductions that actually convert.
```

**CTA Buttons** (side by side, centered, 16px gap):

- **Primary:** `Join Angel Club` → membership page
  - Style: Muted Copper background, white text, 48px height, 8px border-radius
- **Secondary:** `Apply for Ready to Raise` → RTR application
  - Style: Transparent, white border (1.5px), white text, same dimensions

**Small text below** (Inter 13px, White at 50% opacity):
```
Free tier available. No credit card required to start.
```

---

### SECTION 8: FAQ

**Background:** White #FFFFFF
**Layout:** 60px vertical padding, max-width 720px centered, accordion style

#### Section Header

**Headline** (Playfair Display, 32px):
```
Frequently asked questions
```

#### FAQ Items (Accordion — click to expand)

*Design: Each question is Inter 16px semibold, Espresso. Expand/collapse with + / − icon in Muted Copper. Answer is Inter 15px, Espresso at 80% opacity. 1px bottom border in Espresso at 10% opacity between items.*

**Q: What startup resources does Angel Club offer for free?**
A: Our free tier includes public directories of angel investors, VCs, family offices, corporate VCs, accelerators, and incubators. You also get access to fundraising templates, pitch deck guides, founder playbooks, curated book recommendations, and an events calendar. All resources are contributed and maintained by our community of 6,400+ founders.

**Q: How is the premium investor database different from the free lists?**
A: The free public directories are curated "best of" lists — great for getting started. The premium database contains 12,000+ investors across 40+ sectors with detailed profiles, investment criteria, check sizes, portfolio companies, and contact information. Premium members can also filter by stage, sector, geography, and check size, and request warm introductions through the community.

**Q: How often are resources updated?**
A: The investor database is updated continuously by our community. Grant deadlines are reviewed weekly. Public directories and templates are updated monthly. Our 6,400+ member community ensures information stays current and accurate.

**Q: Can I get warm introductions to investors?**
A: Yes — premium members can request warm introductions through our network of 400+ active investors and thousands of connected founders. Our Ready to Raise program provides structured support including investor matching and introduction facilitation.

**Q: What is the Ready to Raise program?**
A: Ready to Raise is our structured fundraising preparation program. It helps founders refine their pitch, build financial models, identify target investors from our 12,000+ database, and secure warm introductions. It's designed for founders who are actively raising or preparing to raise in the next 3–6 months.

**Q: Do you have grants for startups?**
A: Yes. We maintain a curated database of 200+ grants and non-dilutive funding opportunities worth $150,000 or more. Each listing includes eligibility criteria, application deadlines, and direct application links. The grants database is updated weekly.

**Q: What sectors does the investor database cover?**
A: Over 40 sectors including AI/ML, fintech, healthtech, climate tech, edtech, SaaS, biotech, consumer, hardware, Web3, impact investing, and our newest addition — faith-based investing. Each investor profile includes their specific sector preferences.

**Q: Is Angel Club only for US-based founders?**
A: No. Angel Club has members from around the world, and our investor database includes global investors. While the majority of resources are US-focused, we're continuously expanding international coverage.

---

### SECTION 9: DISCLAIMERS

**Background:** Ivory #F7F3EE
**Layout:** 40px vertical padding, max-width 720px, centered

*Design: Inter 13px, Espresso at 50% opacity. Compact, not visually prominent.*

```
Disclaimer: Angel Club does not provide financial, investment, or legal 
advice. The resources on this page are for informational purposes only. 
Inclusion in our directories does not constitute an endorsement. Always 
conduct your own due diligence before engaging with any investor, program, 
or funding opportunity. Be cautious of unlicensed fundraisers and verify 
credentials independently. Angel Club is not a broker-dealer, investment 
advisor, or funding platform.

© 2026 Angel Club. All rights reserved.
Privacy Policy  |  Terms of Service  |  Contact
```

---

## 4. DESIGN SPECIFICATIONS

### Color Palette (Locked)

| Token | Hex | Usage |
|-------|-----|-------|
| Ivory | #F7F3EE | Primary background, alternating sections |
| Espresso | #3A2F2A | Primary text, headings, dark section bg |
| Muted Copper | #B8896B | Accent, CTAs, links, icons, stat numbers |
| White | #FFFFFF | Card backgrounds, alternating sections |
| Light Taupe | #EFE8DF | Card fills, alt section backgrounds, filter bar bg |

### Typography

| Element | Font | Weight | Size (Desktop) | Size (Mobile) |
|---------|------|--------|-----------------|---------------|
| Eyebrow | Inter | 500 | 12px, 2px tracking | 11px |
| H1 (Hero) | Playfair Display | 700 | 48px / 1.15 | 32px / 1.2 |
| H2 (Section) | Playfair Display | 600 | 36px / 1.2 | 28px / 1.25 |
| H3 (Card title) | Inter | 600 | 16px / 1.4 | 16px / 1.4 |
| Body | Inter | 400 | 16px / 1.6 | 15px / 1.6 |
| Small / Caption | Inter | 400 | 13px / 1.5 | 12px / 1.5 |
| Stat Number | Playfair Display | 700 | 32px | 24px |
| Button | Inter | 600 | 14px | 14px |

### Spacing System

- Section padding: 80px–120px desktop, 48px–80px mobile
- Card padding: 24px–32px
- Grid gap: 24px desktop, 16px mobile
- Max content width: 1200px
- Max text width: 640px (for readability)

### Interactive States

- **Links:** Muted Copper, underline on hover
- **Buttons (primary):** Muted Copper bg → darken 10% on hover, subtle shadow
- **Buttons (secondary):** Espresso border → Espresso fill + white text on hover
- **Cards:** translateY(-2px) + subtle box-shadow on hover
- **Accordion:** Smooth 300ms ease-in-out expand
- **Filter pills:** Muted Copper fill + white text when active

### Iconography

- Style: Line icons, 1.5px stroke weight
- Color: Muted Copper #B8896B
- Size: 32px in category cards, 20px inline
- Source recommendation: Phosphor Icons or Lucide (both MIT, line style matches aesthetic)

---

## 5. MOBILE SPECIFICATIONS

### Critical Changes from Current Page

**Current problem:** Page warns "best viewed on desktop" due to embedded table.
**Solution:** Eliminate embedded table dependency. Build native responsive components.

### Breakpoints

| Breakpoint | Width | Layout Changes |
|------------|-------|----------------|
| Desktop | ≥1024px | 3-column grid, side-by-side comparison, data table |
| Tablet | 768–1023px | 2-column grid, stacked comparison, data table |
| Mobile | <768px | 1-column stack, cards instead of table, bottom-sheet filters |

### Mobile-Specific UX

1. **Hero:** Stack stat bar as 2×2 grid instead of horizontal row
2. **Category grid:** Single column, full-width cards
3. **Featured cards:** Full-width, stacked
4. **Free vs Premium:** Stacked vertically, Premium card first (higher conversion)
5. **Search/Filter:** 
   - Sticky search bar at top of resource section
   - Filter pills: horizontal scroll with gradient fade edges
   - "Filters" button opens bottom sheet with all filter options
6. **Resource results:** Card layout, not table. Each card shows: Name, Type badge, Key detail, Access level badge
7. **FAQ accordion:** Full-width, larger touch targets (min 48px tap area)
8. **CTAs:** Full-width buttons stacked vertically, 12px gap
9. **Contributors:** Horizontal scroll of avatars, or 2-column grid

### Performance (Mobile)

- Lazy-load resource cards below the fold
- Skeleton loading states for search results
- Target: <3s First Contentful Paint on 3G
- Image optimization: WebP with JPEG fallback, responsive srcset

---

## 6. SEARCH/FILTER UX RECOMMENDATIONS

### Architecture

**Option A (Recommended for MVP):** Client-side filtering with pre-loaded JSON
- Load all public resources as JSON on page load
- Filter/search in-browser with instant results
- Premium resources show as locked cards with "Unlock with membership" overlay
- Pro: Fast, no server calls. Con: Initial payload larger.

**Option B (Recommended for scale):** API-backed search
- Search endpoint returns filtered results
- Supports pagination, complex queries
- Premium results returned but gated behind auth
- Pro: Scales to any size. Con: Requires backend work.

### Search Behavior

1. **Instant search:** Results update as user types (debounced 300ms)
2. **Empty state:** Show category cards when no query entered
3. **No results:** "No resources found. Try adjusting your filters or [submit a resource request →]"
4. **Premium lock:** Show premium results in search with lock icon + "Premium" badge. Clicking opens membership CTA modal.

### Filter Logic

- Filters are AND within groups, OR between options in same group
- Active filter count shown on mobile "Filters" button: `Filters (3)`
- "Clear all" resets to default state
- URL params update with filter state (shareable filtered views)

### Sort Options

- Relevance (default for search)
- Recently added
- Alphabetical (A–Z, Z–A)
- Check size (high to low, low to high) — investors only

---

## 7. IMPLEMENTATION NOTES

### Priority Order

1. **P0 — Ship first:** Hero, Category grid, Free vs Premium, CTA block, FAQ, Disclaimers, SEO meta, Schema markup
2. **P1 — Fast follow:** Featured/New section, Search bar (basic), Mobile-responsive resource cards, Contributors section
3. **P2 — Iterate:** Advanced filtering, Sort options, URL param state, Premium lock UX, Grant deadline alerts

### Content to Migrate

- All existing public resource lists (angel investors, VCs, family offices, CVCs, accelerators, incubators, books, events, playbooks, templates)
- Community contributor credits
- Existing disclaimers (updated copy above)

### Content to Create

- Category counts (verify exact numbers from database)
- Faith-based investor section description
- Grants database with deadlines
- Resource submission form (replace email CTA)
- OG image for social sharing

### Technical SEO Checklist

- [ ] Page title and meta description implemented
- [ ] H1 tag contains primary keyword
- [ ] Schema markup (FAQ, WebPage, ItemList, BreadcrumbList) in `<head>`
- [ ] Open Graph tags for social sharing
- [ ] Canonical URL set
- [ ] Internal links to /resources from homepage, nav, and other pages
- [ ] Alt text on all images/icons
- [ ] Page speed: <3s LCP on mobile
- [ ] Mobile-friendly: passes Google Mobile-Friendly Test
- [ ] Semantic HTML: proper heading hierarchy, landmark regions
- [ ] Sitemap: /resources included in XML sitemap

### Accessibility

- All interactive elements: min 48px touch targets
- Color contrast: Espresso on Ivory = 10.5:1 (passes AAA)
- Color contrast: White on Muted Copper = 3.8:1 (passes AA large text — use only for large text/buttons)
- Color contrast: White on Espresso = 10.5:1 (passes AAA)
- Accordion: aria-expanded, aria-controls
- Filter pills: role="radiogroup" or role="checkbox" as appropriate
- Search: role="search", aria-label
- Skip navigation link for keyboard users
- Alt text for all decorative and informational icons

---

*Document prepared for Angel Club. All copy, design specifications, and technical recommendations are production-ready pending final content verification (exact resource counts) and brand review.*
