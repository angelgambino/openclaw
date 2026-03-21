# 🧮 Fundraising Calculator

> A practical planning tool for founders. Bookmark this — you'll return to it throughout your raise.

---

## 1. Round Size Calculator

**The formula:** Monthly burn rate × 18-24 months = minimum raise, then add a 20% buffer.

Your raise should cover enough runway to hit your next milestone (typically 18-24 months), plus a cushion for the inevitable delays — hiring takes longer, sales cycles slip, that "sure thing" partnership stalls.

| Monthly Burn | 18 Mo Runway | 24 Mo Runway | With 20% Buffer |
|---|---|---|---|
| $25K | $450K | $600K | $540K–$720K |
| $50K | $900K | $1.2M | $1.08M–$1.44M |
| $75K | $1.35M | $1.8M | $1.62M–$2.16M |
| $100K | $1.8M | $2.4M | $2.16M–$2.88M |
| $150K | $2.7M | $3.6M | $3.24M–$4.32M |
| $200K | $3.6M | $4.8M | $4.32M–$5.76M |

### How to use this

1. **Start with current burn** — what you spend today, monthly
2. **Add planned hires** — each engineering hire ≈ $15-20K/mo fully loaded, each sales hire ≈ $12-18K/mo
3. **Pick your runway target** — 18 months is tight, 24 months gives breathing room
4. **Apply the 20% buffer** — fundraising always takes longer than you think

> 💡 **Tip:** Track your `monthly_burn` and `runway_months` in your investor database to keep this current as your plans evolve. Update the `round_target` field when you've settled on a number.

---

## 2. Valuation Guide by Stage

Valuation is part art, part math, part leverage. Here's what the market typically looks like:

| Stage | Typical ARR | Typical Valuation | Revenue Multiple |
|---|---|---|---|
| Pre-seed | $0 | $2M–$6M | N/A (team + idea) |
| Seed | $0–$500K | $5M–$15M | 20-30x |
| Seed+ | $500K–$1.5M | $10M–$25M | 15-20x |
| Series A | $1M–$5M | $20M–$60M | 15-20x |
| Series B | $5M–$20M | $50M–$200M | 10-15x |

### What moves valuation up or down

**Higher valuation drivers:**
- Strong team pedigree (repeat founders, domain experts)
- Hot market / category tailwinds
- Competitive round dynamics (multiple term sheets)
- Exceptional growth rate (3x+ YoY)
- Capital-efficient business model

**Lower valuation drivers:**
- First-time founders (not a dealbreaker, just affects starting point)
- Crowded market without clear differentiation
- Slow or flat growth
- High churn
- Single-channel dependency

> 💡 **Tip:** Log the `valuation_expectation` in your database early. When investors push back, you'll have your reasoning documented rather than negotiating on the fly.

---

## 3. Dilution Calculator

The golden rule: **aim for 15-25% dilution per round.** Under 15% and investors may feel they don't have enough skin in the game. Over 25% and you're giving away too much too early.

| Round Size | Pre-Money | Post-Money | Dilution | Founder Owns After |
|---|---|---|---|---|
| $500K | $4.5M | $5M | 10% | 90% |
| $1M | $4M | $5M | 20% | 80% |
| $2M | $8M | $10M | 20% | 80% |
| $3M | $12M | $15M | 20% | 80% |
| $5M | $20M | $25M | 20% | 80% |

### Cumulative dilution matters

Don't just think about this round. Model the full journey:

| After... | Founder Ownership (typical) |
|---|---|
| Pre-seed (10-15%) | 85-90% |
| Seed (15-20%) | 68-77% |
| Series A (15-20%) | 54-65% |
| Series B (10-15%) | 46-59% |
| ESOP pools (10-15% total) | 39-53% |

**The math that matters:** If you own 50% at Series B and the company is worth $200M, your stake is $100M. Dilution isn't the enemy — *unnecessary* dilution is.

> 💡 **Tip:** Use your database's `round_size` and `pre_money_valuation` fields to model scenarios before committing to a number.

---

## 4. Investor Mix Calculator

Rounds don't come from one check. Here's how to layer your investor base:

### For a $2M Round

| Layer | Count | Avg Check | Total | Cumulative |
|---|---|---|---|---|
| Anchor Angels | 5 | $50K | $250K | $250K |
| Strategic Angels | 4 | $75K | $300K | $550K |
| Lead VC | 1 | $1M | $1M | $1.55M |
| Fill (syndicates) | 2 | $225K | $450K | **$2M** |

### For a $5M Round

| Layer | Count | Avg Check | Total | Cumulative |
|---|---|---|---|---|
| Anchor Angels | 5 | $50K | $250K | $250K |
| Strategic Angels | 5 | $100K | $500K | $750K |
| Lead VC | 1 | $2.5M | $2.5M | $3.25M |
| Co-Lead/Follow VCs | 2 | $500K | $1M | $4.25M |
| Fill | 3 | $250K | $750K | **$5M** |

### Strategy by layer

1. **Anchor Angels first** — These are believers. Friends, former colleagues, people who trust *you* before the metrics. They create early momentum.
2. **Strategic Angels next** — Industry operators who add credibility and signal. Their names on the cap table tell a story.
3. **Lead VC** — The big domino. Once a lead commits, everything accelerates. Most of your energy should go here.
4. **Fill** — Syndicates, follow-on funds, and smaller VCs who ride the lead's due diligence. These close fast once the lead is in.

> 💡 **Tip:** Tag each investor contact in your database with `investor_type` (angel / strategic / vc_lead / vc_follow / syndicate) and `typical_check_size` to map your round structure against real names.

---

## 5. Timeline Estimator

Fundraising always takes longer than you expect. Plan accordingly:

| Stage | Avg Weeks to Close | Meetings Needed | Investors to Approach |
|---|---|---|---|
| Pre-seed | 4–8 weeks | 15–25 | 30–50 |
| Seed | 6–12 weeks | 25–50 | 50–100 |
| Series A | 8–16 weeks | 30–60 | 40–80 |
| Series B | 10–20 weeks | 20–40 | 30–50 |

### Working backward from your deadline

If you have 6 months of runway left and you're raising a seed:

| Week | Activity |
|---|---|
| Weeks 1-2 | Prep: deck, data room, target list, warm intros |
| Weeks 3-4 | Soft launch: 10-15 first meetings, test the pitch |
| Weeks 5-8 | Full launch: 30-40 meetings, iterate on pitch |
| Weeks 9-10 | Follow-ups, partner meetings, diligence |
| Weeks 11-12 | Term sheet negotiation, close |
| Weeks 13-16 | Buffer for legal, wire delays |

**Start fundraising when you have 6+ months of runway.** If you wait until 3 months, you're negotiating from desperation.

> 💡 **Tip:** Use the `status` and `last_contact` fields in your database to track where each investor sits in this timeline. Set `next_step` and `follow_up_date` religiously.

---

## 6. Conversion Funnel

This is the cold math of fundraising. Know it. Internalize it. Plan for it.

| Stage | Cold Emails Sent | Replies | First Meetings | Second Meetings | Term Sheets | Closed |
|---|---|---|---|---|---|---|
| Rate | 100% | 15–25% | 10–15% | 5–8% | 2–4% | 1–2% |
| For 100 emails | 100 | 15–25 | 10–15 | 5–8 | 2–4 | 1–2 |

### What this means in practice

**To get 2 term sheets, you likely need to email 100 investors.**

Not 20. Not 50. **One hundred.**

| If you want... | You need to approach... |
|---|---|
| 1 term sheet | ~50 investors |
| 2 term sheets (ideal) | ~100 investors |
| 3+ term sheets (competitive) | ~150 investors |

### How to improve your conversion

- **Warm intros convert 3-5x better** than cold emails. Prioritize them ruthlessly.
- **Timing matters** — VCs are most active Jan-Apr and Sep-Nov. Summer and holidays are dead zones.
- **Social proof compounds** — Every "yes" makes the next one easier. Start with your highest-conviction investors.
- **Your deck isn't the pitch** — It's the leave-behind. The pitch is the story you tell in the room.

> 💡 **Tip:** Track `outreach_method` (warm_intro / cold_email / event / inbound) in your database. After 30 outreaches, analyze which channel converts best and double down.

---

## 7. SAFE vs. Priced Round Decision Tree

Not every round needs a term sheet and a law firm on retainer. Here's how to decide:

```
                    How much are you raising?
                    ┌─────────┼─────────┐
                  <$1M    $1M-$2M      >$2M
                    │         │           │
                  SAFE    Either       Priced
                    │      works        Round
                    │         │           │
                    │    ┌────┴────┐      │
                    │  Speed     Have     │
                    │  matters?  lead?    │
                    │    │         │      │
                    │   SAFE    Priced    │
                    │                     │
                    └─────────────────────┘
```

### Quick reference

| Situation | Recommendation | Why |
|---|---|---|
| Raising <$1M | **SAFE** | Faster, cheaper legal ($0-2K vs $15-25K), no board seat negotiation |
| Raising $1M–$2M, speed matters | **SAFE** | Can close in days, not weeks |
| Raising $1M–$2M, have a lead | **Priced round** | Lead will set terms anyway; formalize it |
| Raising >$2M | **Priced round** | Investors expect it, better governance, clearer cap table |
| No lead investor | **SAFE** | Avoid premature valuation negotiation until you have leverage |

### SAFE specifics to know

- **Use the [standard YC SAFE](https://www.ycombinator.com/documents)** — don't let lawyers customize it
- **Valuation cap** = the max valuation at which your SAFE converts
- **Post-money SAFEs** (YC standard) are cleaner — dilution is predictable
- **Discount-only SAFEs** are rare now — most investors want a cap

> 💡 **Tip:** Record `deal_structure` (safe / priced / convertible_note) in your database for each investor conversation. Some investors have hard preferences — know them before the meeting.

---

## 8. Use of Funds Template

Investors want to know where their money goes. Here's the standard allocation:

| Category | % of Raise | For $2M Round | For $5M Round |
|---|---|---|---|
| Engineering / Product | 50–60% | $1M–$1.2M | $2.5M–$3M |
| GTM / Sales / Marketing | 20–30% | $400K–$600K | $1M–$1.5M |
| Operations / G&A | 10–15% | $200K–$300K | $500K–$750K |
| Buffer | 5–10% | $100K–$200K | $250K–$500K |

### What each bucket typically covers

**Engineering / Product (50-60%)**
- 3-5 engineers (your biggest cost)
- Design and product management
- Infrastructure and tooling
- Contractor/agency work for specialized needs

**GTM / Sales / Marketing (20-30%)**
- 1-2 sales hires or SDRs
- Marketing spend (content, ads, events)
- Sales tools (CRM, outreach platforms)
- Customer success (often shared with product early on)

**Operations / G&A (10-15%)**
- Legal and accounting
- Office / co-working space
- Insurance
- Software subscriptions
- Travel

**Buffer (5-10%)**
- This is not optional. Things always cost more.
- Covers hiring delays, unexpected legal, that conference you didn't plan for
- If you don't use it, it extends your runway — that's a feature, not a bug

### What investors actually want to hear

They're not looking for a line-item budget. They want to know:

1. **What milestones will this money help you hit?** (e.g., "$1M ARR," "product-market fit," "Series A readiness")
2. **How does spending map to those milestones?** (e.g., "Engineering hires to ship v2, which unlocks enterprise sales")
3. **When will you need to raise again?** (e.g., "This gives us 20 months of runway to hit $2M ARR, positioning us for a Series A")

> 💡 **Tip:** Keep your use-of-funds narrative in your data room. When an investor asks "what will you do with the money?" — your answer should take 60 seconds and connect dollars to milestones, not line items.

---

## Quick Reference Card

| Question | Answer |
|---|---|
| How much should I raise? | Burn × 18-24 months + 20% buffer |
| What's my company worth? | See Stage Valuation Guide above |
| How much dilution is normal? | 15-25% per round |
| How long will this take? | 2-4 months (add buffer) |
| How many investors do I need to talk to? | 50-100 for a seed round |
| SAFE or priced round? | <$1M = SAFE, >$2M = priced |
| Where does the money go? | 50-60% product, 20-30% GTM, rest is ops + buffer |

---

## Your Fundraising Checklist

Before you start outreach:

- [ ] Calculate your target raise (Section 1)
- [ ] Set your valuation expectation (Section 2)
- [ ] Model your dilution (Section 3)
- [ ] Map your investor mix (Section 4)
- [ ] Build your timeline (Section 5)
- [ ] Build a target list of 100+ investors
- [ ] Decide SAFE vs. priced round (Section 7)
- [ ] Prepare your use-of-funds narrative (Section 8)
- [ ] Populate your investor database with targets, types, and check sizes
- [ ] Prep your data room (deck, financials, cap table, product demo)

---

*Return to this document throughout your raise. Update your numbers as reality diverges from the plan — it always does.*
