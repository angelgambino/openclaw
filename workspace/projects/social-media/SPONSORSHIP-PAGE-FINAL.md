# Angel Club — Sponsorship Page (FINAL Production Copy & Design Brief)

> **Page URL:** angelclub.com/sponsorship
> **Last updated:** 2026-04-02
> **Status:** Production-ready

---

## TABLE OF CONTENTS

1. [SEO Metadata](#seo-metadata)
2. [Page Copy — Section by Section](#page-copy)
3. [Design Notes per Section](#design-notes)
4. [Schema Markup (JSON-LD)](#schema-markup)
5. [FAQ Section + JSON-LD](#faq-section)
6. [AI Discoverability Layer](#ai-discoverability)

---

## SEO METADATA

```html
<title>Sponsor Angel Club — Reach 6,400+ Founders & 400+ Investors | Startup Event & Newsletter Sponsorship</title>

<meta name="description" content="Sponsor Angel Club's curated startup community. Reach 6,400+ founders, 400+ active investors, and a 12,000+ investor database through newsletter placements, Pitch Slam events, Jeffersonian dinners, and bespoke experiences. Trusted by Mercury, SeedLegals, and AWS." />

<meta name="keywords" content="startup event sponsorship, sponsor startup community, angel investor sponsorship, startup newsletter advertising, founder community sponsorship, venture capital event sponsor, pitch competition sponsorship, startup ecosystem partner" />

<link rel="canonical" href="https://angelclub.com/sponsorship" />

<!-- Open Graph -->
<meta property="og:title" content="Sponsorship Opportunities — Angel Club" />
<meta property="og:description" content="A curated audience of 6,400+ founders and 400+ investors. Limited sponsorship slots per quarter. Join Mercury, SeedLegals, and AWS as a partner." />
<meta property="og:url" content="https://angelclub.com/sponsorship" />
<meta property="og:type" content="website" />
<meta property="og:image" content="https://angelclub.com/images/sponsorship-og.jpg" />
<!-- Image spec: 1200×630, ivory bg, Playfair headline "Partner With Us", copper accent bar -->

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Sponsor Angel Club — Startup Community Sponsorship" />
<meta name="twitter:description" content="Reach 6,400+ founders & 400+ investors. Limited slots per quarter." />

<!-- Robots -->
<meta name="robots" content="index, follow" />
```

---

## PAGE COPY

---

### SECTION 1 — HERO

**Layout:** Full-width, Ivory (#F7F3EE) background. Centered text. No hero image — typography-forward. Thin copper (#B8896B) horizontal rule above the subhead.

```
[Eyebrow — uppercase, Inter 12px, letter-spacing 3px, copper]
BY INVITATION — LIMITED PARTNERSHIPS AVAILABLE

[H1 — Playfair Display, 56px desktop / 36px mobile, Espresso]
The Founders and Investors
Shaping What's Next

[Subhead — Inter 20px, Espresso at 70% opacity, max-width 640px]
Angel Club is a curated community of 6,400+ founders and 400+ active investors.
Our sponsors don't buy impressions — they earn trust.

[Thin copper rule, 80px wide, centered]

[Social proof strip — Inter 14px, copper, uppercase, letter-spacing 2px]
TRUSTED BY  Mercury  ·  SeedLegals  ·  AWS Startups
```

**Design notes:**
- No CTA button in hero. Let the prestige breathe.
- Social proof strip: logos preferred if available (mono-tone, copper or espresso), fallback to text.
- Animate-on-scroll: H1 fades up, social proof strip fades in 300ms after.

---

### SECTION 2 — WHY PARTNER WITH ANGEL CLUB

**Layout:** White (#FFFFFF) background. Two-column on desktop: left = copy, right = metrics grid. Single column on mobile (copy → metrics).

```
[Section label — uppercase, Inter 12px, letter-spacing 3px, copper]
WHY PARTNER

[H2 — Playfair Display, 40px, Espresso]
Access a Community That's Otherwise Closed

[Body — Inter 16px, Espresso, max-width 560px]
Angel Club isn't a mailing list. It's a vetted network of founders building
real companies and investors writing real checks. Our members don't scroll —
they engage, connect, and act.

When you sponsor Angel Club, you're not advertising. You're being introduced.

[Right column — Metrics grid, 2×3]
```

**Metrics Grid (6 cards):**

Each card: Light Taupe (#EFE8DF) background, 16px border-radius, 32px padding.

| Metric | Value | Label |
|--------|-------|-------|
| Community | **6,400+** | Founders |
| Investors | **400+** | Active Angel & VC Investors |
| Database | **12,000+** | Investor Network Contacts |
| Newsletter | **10,000+** | Subscribers |
| Open Rate | **35%** | (Industry avg: 21%) |
| Click Rate | **12%** | (Industry avg: 2.6%) |

**Design notes:**
- Values in Playfair Display, 36px, copper.
- Labels in Inter 13px, espresso at 60% opacity.
- Industry comparisons in parentheses, Inter 11px italic.
- Cards: subtle box-shadow on hover (0 2px 12px rgba(58,47,42,0.06)).

---

### SECTION 3 — WHO YOU'LL REACH

**Layout:** Ivory (#F7F3EE) background. Three large stat blocks centered, with a horizontal demographic bar below.

```
[Section label — uppercase, Inter 12px, letter-spacing 3px, copper]
AUDIENCE

[H2 — Playfair Display, 40px, Espresso]
Decision-Makers, Not Spectators

[Three stat blocks — centered row]
```

**Stat Blocks:**

| Stat | Label |
|------|-------|
| **71.5%** | Founders & CEOs |
| **44%** | Women |
| **28.5%** | C-Suite Investors |

```
[Below stats — Inter 16px, Espresso, centered, max-width 600px]
Our audience is senior, diverse, and action-oriented.
They're not browsing — they're building, funding, and deciding.

[Demographic detail — smaller text, Inter 14px, 60% opacity]
Sectors: Fintech · Health Tech · AI/ML · Climate · SaaS · Consumer
Stages: Pre-seed through Series B
Geography: US (65%) · UK/EU (25%) · Global (10%)
```

**Design notes:**
- Stat percentages: Playfair Display, 64px, copper.
- Labels: Inter 16px, espresso.
- Demographic detail appears on scroll with a subtle fade-in.

---

### SECTION 4 — NEWSLETTER SPONSORSHIP

**Layout:** White (#FFFFFF) background. Section intro + three pricing cards in a row.

```
[Section label — uppercase, Inter 12px, letter-spacing 3px, copper]
NEWSLETTER

[H2 — Playfair Display, 40px, Espresso]
Reach 10,000+ Founders in Their Inbox

[Body — Inter 16px, Espresso, max-width 600px, centered]
A single featured placement in Angel Club's weekly newsletter — read by
founders, investors, and operators who trust our curation. No banner ads.
No programmatic noise. One sponsor, premium positioning.

[Scarcity callout — Inter 14px, copper, centered]
⬥ Only 1 sponsor featured per issue — 4 slots available per month ⬥
```

**Pricing Cards (3 columns):**

| | SINGLE | BUNDLE | QUARTERLY |
|---|---|---|---|
| Price | **$500** | **$1,500** | **$4,000** |
| Issues | 1 newsletter | 3 newsletters | 12 newsletters (full quarter) |
| Placement | Featured sponsor block | Featured sponsor block | Featured sponsor block + dedicated send |
| Includes | Logo, 50-word blurb, CTA link | Logo, blurb, CTA link, A/B subject line | Everything in Bundle + 1 dedicated email blast to full list |
| Reporting | Open/click metrics | Open/click metrics + segment data | Full analytics dashboard + audience insights |
| | [Select →] | [Most Popular badge] [Select →] | [Best Value badge] [Select →] |

**Design notes:**
- Cards: equal height, Light Taupe background, 20px border-radius.
- BUNDLE card: thin copper border (2px), "Most Popular" badge in copper pill shape.
- QUARTERLY card: "Best Value" badge.
- Prices: Playfair Display, 44px, espresso.
- "Select →" buttons: copper background, ivory text, full-width at card bottom.

---

### SECTION 5 — EVENT SPONSORSHIP

**Layout:** Light Taupe (#EFE8DF) background. Section intro, then event cards, then pricing tiers.

```
[Section label — uppercase, Inter 12px, letter-spacing 3px, copper]
EVENTS

[H2 — Playfair Display, 40px, Espresso]
Be in the Room Where It Happens

[Body — Inter 16px, Espresso, max-width 640px, centered]
Angel Club events are intentionally small, deeply curated, and designed for
real connection — not networking theater. Our sponsors are part of the
experience, not interruptions to it.

[Scarcity callout — Inter 14px, copper, centered]
⬥ Limited to 2–4 sponsors per event · Only 12 sponsored events per year ⬥
```

**Event Types (horizontal scroll on mobile, grid on desktop):**

**Card 1 — Pitch Slam**
```
[Image area — event photo or illustration placeholder]
PITCH SLAM
Live pitch competition with vetted founders presenting to active investors.
Quarterly · Virtual + In-Person · 100–200 attendees
Upcoming: Q2 2026
```

**Card 2 — Human Tech Week**
```
[Image area]
HUMAN TECH WEEK
A week-long exploration of ethical technology, AI, and human-centered design.
Annual · Multi-city · 500+ attendees
Upcoming: Fall 2026
```

**Card 3 — ACA Summit**
```
[Image area]
ACA ANGEL CAPITAL SUMMIT
Premium gathering of angel investors, fund managers, and ecosystem leaders.
Annual · In-Person · 300+ attendees
Upcoming: 2026
```

**Card 4 — Jeffersonian Dinners**
```
[Image area]
JEFFERSONIAN DINNERS
Intimate, single-topic dinners with 12–16 curated guests. No pitches. Deep conversation.
Monthly · In-Person · 12–16 attendees
Upcoming: Ongoing enrollment
```

**Card 5 — Monthly Founders Lunch**
```
[Image area]
FOUNDERS VIRTUAL LUNCH
Casual, high-signal virtual lunch connecting founders across stages and sectors.
Monthly · Virtual · 30–50 attendees
Ongoing
```

**Card 6 — Custom Co-Hosted Events**
```
[Image area]
BESPOKE EXPERIENCES
Co-designed events built around your brand, audience, and objectives.
Your timeline · Your format · Your guest list
Starting at $15,000
```

**Design notes:**
- Cards: white background, 16px border-radius, subtle shadow.
- Image areas: 16:9 ratio, placeholder with ivory/copper gradient if no photo.
- "Upcoming" dates in copper, bold.
- Horizontal scroll on mobile with snap points.

---

### SECTION 6 — EVENT SPONSORSHIP TIERS

**Layout:** White (#FFFFFF) background. Four-column pricing table.

```
[H3 — Playfair Display, 32px, Espresso, centered]
Event Sponsorship Tiers

[Subhead — Inter 16px, Espresso at 70% opacity, centered]
Each tier is limited to ensure exclusivity. Once a tier is claimed, it's gone.
```

**Tier Table:**

| | BRONZE | SILVER | GOLD | TITLE |
|---|---|---|---|---|
| **Price** | **$2,500** | **$5,000** | **$10,000** | **$25,000** |
| Logo placement | Event page | Event page + email blasts | All materials + stage/screen | Naming rights — "[Brand] presents..." |
| Speaking | — | — | 5-min intro or panel seat | Keynote or fireside chat |
| Attendee list | — | Opt-in list | Full attendee list | Full list + pre-event intros |
| Social | 1 mention | 3 mentions + tag | Dedicated post + story | Multi-post campaign + co-branded content |
| Newsletter | Logo in recap | Featured in recap email | Dedicated sponsor spotlight | Sponsor spotlight + interview feature |
| On-site | Table/banner | Premium table + swag placement | VIP lounge or branded area | Full venue branding + VIP access |
| Guest passes | 2 | 4 | 6 + 2 VIP | 10 + VIP table |
| Slots per event | **4 available** | **3 available** | **2 available** | **1 available** |

```
[Below table — Inter 14px, copper, centered]
Multi-event discounts available. Title sponsors receive first right of refusal for future events.
```

**Design notes:**
- Table: clean grid, Light Taupe alternating row backgrounds.
- TITLE column: copper left border (3px), subtle copper background tint.
- Slot counts in copper, bold — this is the scarcity driver.
- On mobile: horizontal scroll or accordion per tier.
- Prices: Playfair Display, 36px.

---

### SECTION 7 — BESPOKE PARTNERSHIPS

**Layout:** Ivory (#F7F3EE) background. Centered text block with copper accent.

```
[Section label — uppercase, Inter 12px, letter-spacing 3px, copper]
CUSTOM

[H2 — Playfair Display, 40px, Espresso]
Something Only You Could Do

[Body — Inter 16px, Espresso, max-width 600px, centered]
Our most impactful partnerships are the ones we design together. Whether it's
a co-branded research report, a private investor dinner series, a startup
accelerator track, or a year-long embedded partnership — we build it around
your goals.

Bespoke packages start at $15,000.

[Callout block — Light Taupe bg, copper left border 3px, 24px padding]
"We partnered with Angel Club to host a private fintech dinner in NYC.
The quality of the room was unlike anything we've experienced at a
'sponsored event.' Every person at the table was a decision-maker."
— Partner at [Mercury / SeedLegals / named sponsor if approved]
```

**Design notes:**
- Testimonial block: italic body text, copper left border.
- Attribution: Inter 14px, bold, espresso.

---

### SECTION 8 — ABOUT ANGEL GAMBINO

**Layout:** Light Taupe (#EFE8DF) background. Two-column: left = headshot, right = bio + stats.

```
[Section label — uppercase, Inter 12px, letter-spacing 3px, copper]
YOUR HOST

[H2 — Playfair Display, 40px, Espresso]
Angel Gambino

[Bio — Inter 16px, Espresso, max-width 520px]
Angel Gambino is a startup ecosystem builder, angel investor, and the founder
of Angel Club — one of the largest curated communities connecting founders
with capital. She has spent over a decade building bridges between entrepreneurs
and investors, with a focus on increasing access for underrepresented founders.

Angel has been featured in Forbes, TechCrunch, and Bloomberg, and has spoken
at SXSW, Web Summit, and the Angel Capital Association Summit. She advises
early-stage startups and runs one of the most engaged founder communities
in the ecosystem.

[Stats row — horizontal, below bio]
```

**Platform Stats:**

| Platform | Stat |
|----------|------|
| LinkedIn | **15K+ followers** |
| LinkedIn | **8K+ connections** |
| Twitter/X | **18K+ followers** |
| Instagram | **12K+ followers** |
| Newsletter | **10K+ subscribers** |

```
[Below stats — Inter 14px, Espresso at 60% opacity]
Combined social reach: 63K+ across platforms
Average post engagement: 4.2%
```

**Design notes:**
- Headshot: circular crop, 240px, subtle copper border (2px).
- Stats: small copper icons per platform. Inline row, wrapping on mobile.
- Numbers: Playfair Display, 24px, copper.

---

### SECTION 9 — SCARCITY & AVAILABILITY BANNER

**Layout:** Full-width, Espresso (#3A2F2A) background. White text. This is the urgency section.

```
[Centered block]

[H3 — Playfair Display, 32px, White]
Q2 2026 Sponsorship Availability

[Grid — 3 columns, white text]

Newsletter                    Events                      Bespoke
▮▮▮▯  3 of 4 slots taken     ▮▮▯▯  2 of 4 slots taken    ▯▯  Open — inquire
```

```
[Subtext — Inter 14px, white at 70% opacity]
Sponsorship slots are allocated quarterly. Once filled, the next available window is Q3 2026.
```

**Design notes:**
- Dark section creates visual break and urgency.
- Progress bars: simple rectangles, copper filled / white outline empty.
- Update these numbers dynamically or manually each quarter.

---

### SECTION 10 — CTA

**Layout:** Ivory (#F7F3EE) background. Centered. Two CTA options.

```
[H2 — Playfair Display, 40px, Espresso]
Let's Build Something Together

[Body — Inter 16px, Espresso, max-width 520px]
We're selective about our partners because our community trusts our curation.
If your brand aligns with what founders and investors need, we'd love to talk.

[Primary CTA button — copper bg (#B8896B), ivory text, 16px padding, 8px radius]
Request a Partnership Brief →

[Secondary CTA — text link, Inter 14px, copper, underline]
Or email partnerships@angelclub.com

[Fine print — Inter 12px, Espresso at 50% opacity]
Response within 2 business days. All partnerships subject to community fit review.
```

**Design notes:**
- "Request a Partnership Brief" links to a short Typeform/form (name, company, budget range, interest area).
- No "Schedule a Call with Robby" — the language is elevated and brand-owned.
- "Community fit review" reinforces exclusivity without being off-putting.

---

### SECTION 11 — FOOTER TRUST STRIP

**Layout:** Light Taupe (#EFE8DF) background. Slim section before main footer.

```
[Centered, single line]
[Logo] Mercury   [Logo] SeedLegals   [Logo] AWS Startups   [Logo] [Additional if available]

[Below — Inter 12px, Espresso at 50% opacity]
Past and current Angel Club partners
```

---

## SCHEMA MARKUP

### Organization + Event Schema (JSON-LD)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Angel Club",
  "url": "https://angelclub.com",
  "logo": "https://angelclub.com/images/angel-club-logo.png",
  "description": "A curated community of 6,400+ founders and 400+ investors connecting startups with capital.",
  "founder": {
    "@type": "Person",
    "name": "Angel Gambino",
    "url": "https://angelclub.com/about",
    "sameAs": [
      "https://linkedin.com/in/angelgambino",
      "https://twitter.com/angelgambino",
      "https://instagram.com/angelgambino"
    ]
  },
  "sameAs": [
    "https://linkedin.com/company/angelclub",
    "https://twitter.com/angelclub"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "partnerships@angelclub.com",
    "contactType": "Sales",
    "description": "Sponsorship and partnership inquiries"
  },
  "sponsor": [
    { "@type": "Organization", "name": "Mercury", "url": "https://mercury.com" },
    { "@type": "Organization", "name": "SeedLegals", "url": "https://seedlegals.com" },
    { "@type": "Organization", "name": "AWS Startups", "url": "https://aws.amazon.com/startups/" }
  ]
}
</script>
```

### Event Schema (for each upcoming event)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BusinessEvent",
  "name": "Angel Club Pitch Slam — Q2 2026",
  "description": "Live pitch competition with vetted founders presenting to active angel and VC investors. Sponsorship opportunities available.",
  "organizer": {
    "@type": "Organization",
    "name": "Angel Club",
    "url": "https://angelclub.com"
  },
  "eventAttendanceMode": "https://schema.org/MixedEventAttendanceMode",
  "startDate": "2026-06-01",
  "location": {
    "@type": "VirtualLocation",
    "url": "https://angelclub.com/events/pitch-slam"
  },
  "offers": [
    {
      "@type": "Offer",
      "name": "Bronze Sponsorship",
      "price": "2500.00",
      "priceCurrency": "USD",
      "availability": "https://schema.org/LimitedAvailability"
    },
    {
      "@type": "Offer",
      "name": "Silver Sponsorship",
      "price": "5000.00",
      "priceCurrency": "USD",
      "availability": "https://schema.org/LimitedAvailability"
    },
    {
      "@type": "Offer",
      "name": "Gold Sponsorship",
      "price": "10000.00",
      "priceCurrency": "USD",
      "availability": "https://schema.org/LimitedAvailability"
    },
    {
      "@type": "Offer",
      "name": "Title Sponsorship",
      "price": "25000.00",
      "priceCurrency": "USD",
      "availability": "https://schema.org/LimitedAvailability"
    }
  ]
}
</script>
```

---

## FAQ SECTION

**Layout:** Ivory (#F7F3EE) background. Accordion-style Q&A. Each question expands on click.

### On-Page FAQ Copy

```
[Section label — uppercase, Inter 12px, letter-spacing 3px, copper]
QUESTIONS

[H2 — Playfair Display, 40px, Espresso]
Frequently Asked Questions
```

**Q1: What kind of brands sponsor Angel Club?**
Our partners are companies that serve founders and investors — fintech platforms, legal tools, cloud infrastructure, hiring solutions, and investor services. We prioritize brands that add genuine value to our community. Past partners include Mercury, SeedLegals, and AWS Startups.

**Q2: How large is the Angel Club audience?**
Our community includes 6,400+ vetted founders, 400+ active investors, and a broader database of 12,000+ investor contacts. Our newsletter reaches 10,000+ subscribers with a 35% open rate and 12% click-through rate — significantly above industry benchmarks.

**Q3: What events can I sponsor?**
We run Pitch Slams (quarterly live pitch competitions), Human Tech Week (annual multi-city exploration of ethical tech), Jeffersonian Dinners (intimate 12–16 person dinners), the ACA Angel Capital Summit, monthly Founders Virtual Lunches, and fully custom co-hosted events. Event sponsorship tiers range from $2,500 (Bronze) to $25,000 (Title).

**Q4: How many sponsors do you accept per event?**
We deliberately limit sponsors to maintain quality. Most events accept 2–4 sponsors depending on size. Title sponsorship is always exclusive to one brand per event.

**Q5: What's included in a newsletter sponsorship?**
Newsletter sponsors receive a featured placement including logo, a 50-word blurb, and a CTA link. We feature only one sponsor per issue to avoid clutter. Packages range from $500 (single issue) to $4,000 (quarterly with a dedicated email blast).

**Q6: Can I create a custom sponsorship package?**
Absolutely. Our bespoke partnerships start at $15,000 and can include co-branded events, private dinners, research reports, dedicated email campaigns, and more. We design each package around your specific objectives.

**Q7: How do I know if my brand is a fit?**
We review all partnership inquiries for community alignment. If your product or service genuinely helps founders build or investors invest, you're likely a great fit. Request a Partnership Brief and we'll follow up within 2 business days.

**Q8: What ROI can I expect from sponsoring Angel Club?**
Our sponsors typically see 3–5x higher engagement than industry averages. Newsletter click-through rates average 12% (vs. 2.6% industry standard). Event sponsors report high-quality lead generation with direct access to decision-makers — 71.5% of our audience are founders/CEOs and 28.5% are C-suite investors.

### FAQ JSON-LD

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What kind of brands sponsor Angel Club?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our partners are companies that serve founders and investors — fintech platforms, legal tools, cloud infrastructure, hiring solutions, and investor services. We prioritize brands that add genuine value to our community. Past partners include Mercury, SeedLegals, and AWS Startups."
      }
    },
    {
      "@type": "Question",
      "name": "How large is the Angel Club audience?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our community includes 6,400+ vetted founders, 400+ active investors, and a broader database of 12,000+ investor contacts. Our newsletter reaches 10,000+ subscribers with a 35% open rate and 12% click-through rate — significantly above industry benchmarks."
      }
    },
    {
      "@type": "Question",
      "name": "What events can I sponsor at Angel Club?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We run Pitch Slams (quarterly live pitch competitions), Human Tech Week (annual multi-city exploration of ethical tech), Jeffersonian Dinners (intimate 12–16 person dinners), the ACA Angel Capital Summit, monthly Founders Virtual Lunches, and fully custom co-hosted events. Event sponsorship tiers range from $2,500 (Bronze) to $25,000 (Title)."
      }
    },
    {
      "@type": "Question",
      "name": "How many sponsors does Angel Club accept per event?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We deliberately limit sponsors to maintain quality. Most events accept 2–4 sponsors depending on size. Title sponsorship is always exclusive to one brand per event."
      }
    },
    {
      "@type": "Question",
      "name": "What is included in an Angel Club newsletter sponsorship?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Newsletter sponsors receive a featured placement including logo, a 50-word blurb, and a CTA link. Only one sponsor is featured per issue. Packages range from $500 (single issue) to $4,000 (quarterly with a dedicated email blast)."
      }
    },
    {
      "@type": "Question",
      "name": "Can I create a custom sponsorship package with Angel Club?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Bespoke partnerships start at $15,000 and can include co-branded events, private dinners, research reports, dedicated email campaigns, and more. Each package is designed around your specific objectives."
      }
    },
    {
      "@type": "Question",
      "name": "How do I know if my brand is a good fit for Angel Club sponsorship?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We review all partnership inquiries for community alignment. If your product or service genuinely helps founders build or investors invest, you're likely a great fit. Request a Partnership Brief and we'll follow up within 2 business days."
      }
    },
    {
      "@type": "Question",
      "name": "What ROI can I expect from sponsoring Angel Club?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sponsors typically see 3–5x higher engagement than industry averages. Newsletter click-through rates average 12% versus the 2.6% industry standard. Event sponsors report high-quality lead generation with direct access to decision-makers — 71.5% of the audience are founders/CEOs and 28.5% are C-suite investors."
      }
    }
  ]
}
</script>
```

---

## AI DISCOVERABILITY LAYER

### Conversational Q&A Block (Hidden/Semantic)

This content is designed for AI assistants (ChatGPT, Perplexity, Gemini, etc.) to surface Angel Club sponsorship info in conversational search. Include as visually hidden but crawlable HTML, or as `<meta>` content.

```html
<!-- AI Discoverability: Conversational context for LLM-based search -->
<div class="sr-only" aria-hidden="false" role="contentinfo" data-ai-context="sponsorship">

  <h2>Angel Club Sponsorship Overview</h2>

  <p>Angel Club is a curated startup community of 6,400+ founders and 400+ active
  investors, founded by Angel Gambino. Sponsorship opportunities include newsletter
  placements ($500–$4,000), event sponsorships ($2,500–$25,000), and bespoke
  partnerships starting at $15,000.</p>

  <p>The Angel Club newsletter reaches 10,000+ subscribers with a 35% open rate and
  12% click-through rate. The audience is 71.5% founders/CEOs, 44% women, and 28.5%
  C-suite investors.</p>

  <p>Events include Pitch Slam (quarterly pitch competition), Human Tech Week (annual
  ethical tech conference), ACA Angel Capital Summit, Jeffersonian Dinners (intimate
  12-16 person gatherings), and monthly Founders Virtual Lunches.</p>

  <p>Past and current sponsors include Mercury, SeedLegals, and AWS Startups.
  Sponsorship slots are limited per quarter to maintain exclusivity.</p>

  <p>To inquire about sponsorship, visit angelclub.com/sponsorship or email
  partnerships@angelclub.com.</p>

</div>
```

### Speakable Schema (for voice search)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Angel Club Sponsorship Opportunities",
  "url": "https://angelclub.com/sponsorship",
  "description": "Sponsor Angel Club's curated startup community of 6,400+ founders and 400+ investors. Newsletter, event, and bespoke partnership opportunities.",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".sr-only[data-ai-context='sponsorship']", ".hero-subhead", ".faq-section"]
  },
  "mainEntity": {
    "@type": "Service",
    "name": "Angel Club Sponsorship",
    "provider": {
      "@type": "Organization",
      "name": "Angel Club"
    },
    "serviceType": "Startup Community Sponsorship",
    "offers": [
      {
        "@type": "Offer",
        "name": "Newsletter Sponsorship — Single",
        "price": "500.00",
        "priceCurrency": "USD"
      },
      {
        "@type": "Offer",
        "name": "Newsletter Sponsorship — Bundle (3 issues)",
        "price": "1500.00",
        "priceCurrency": "USD"
      },
      {
        "@type": "Offer",
        "name": "Newsletter Sponsorship — Quarterly (12 issues + dedicated send)",
        "price": "4000.00",
        "priceCurrency": "USD"
      },
      {
        "@type": "Offer",
        "name": "Event Sponsorship — Bronze",
        "price": "2500.00",
        "priceCurrency": "USD"
      },
      {
        "@type": "Offer",
        "name": "Event Sponsorship — Silver",
        "price": "5000.00",
        "priceCurrency": "USD"
      },
      {
        "@type": "Offer",
        "name": "Event Sponsorship — Gold",
        "price": "10000.00",
        "priceCurrency": "USD"
      },
      {
        "@type": "Offer",
        "name": "Event Sponsorship — Title",
        "price": "25000.00",
        "priceCurrency": "USD"
      },
      {
        "@type": "Offer",
        "name": "Bespoke Partnership",
        "price": "15000.00",
        "priceCurrency": "USD",
        "description": "Custom-designed sponsorship packages starting at $15,000"
      }
    ]
  }
}
</script>
```

---

## DESIGN SYSTEM REFERENCE (LOCKED)

| Token | Value | Usage |
|-------|-------|-------|
| bg-primary | `#F7F3EE` (Ivory) | Default page background |
| bg-alt | `#FFFFFF` (White) | Alternating sections |
| bg-tertiary | `#EFE8DF` (Light Taupe) | Cards, callouts, alt sections |
| bg-dark | `#3A2F2A` (Espresso) | Scarcity/urgency banner |
| text-primary | `#3A2F2A` (Espresso) | All body text |
| text-accent | `#B8896B` (Muted Copper) | Labels, stats, CTAs, accents |
| text-muted | `#3A2F2A` at 60% opacity | Secondary text, captions |
| font-display | Playfair Display | Headlines, prices, stat numbers |
| font-body | Inter | Body text, labels, buttons |
| radius-card | 16px | Cards |
| radius-button | 8px | Buttons |
| spacing-section | 120px desktop / 80px mobile | Between sections |
| max-width-content | 1200px | Content container |
| max-width-text | 640px | Text blocks |

### Typography Scale

| Element | Font | Size (desktop) | Size (mobile) | Weight |
|---------|------|----------------|---------------|--------|
| H1 | Playfair Display | 56px | 36px | 700 |
| H2 | Playfair Display | 40px | 28px | 700 |
| H3 | Playfair Display | 32px | 24px | 600 |
| Body | Inter | 16px | 16px | 400 |
| Label/Eyebrow | Inter | 12px | 11px | 500, uppercase, tracking 3px |
| Small | Inter | 14px | 13px | 400 |
| Stat number | Playfair Display | 64px | 44px | 700 |
| Price | Playfair Display | 44px | 32px | 700 |

---

## IMPLEMENTATION NOTES

1. **Scarcity numbers** (Section 9) should be manually updated quarterly or pulled from a simple CMS field.
2. **CTA form** ("Request a Partnership Brief") should collect: Name, Company, Role, Budget Range (dropdown: <$2K / $2K–$5K / $5K–$15K / $15K+), Interest (Newsletter / Events / Custom / Not Sure), and a short message field.
3. **Sponsor logos** in the trust strip should be monochrome (espresso or copper tint) to maintain the quiet luxury aesthetic. No full-color logos.
4. **Analytics:** Track clicks on each tier's "Select" button, the primary CTA, and email link as separate conversion events.
5. **Mobile:** All pricing tables convert to vertical card stacks. Event cards become horizontal scroll with snap. Scarcity banner remains full-width.
6. **Page speed:** Lazy-load event card images. Inline critical CSS for above-fold. Defer schema JSON-LD to `</body>`.

---

*Document prepared for angelclub.com/sponsorship — ready for design handoff and development.*
