# Switching to flat pricing

> **Prompt:** our B2B SaaS charges €12 per seat per month. Customers find per-seat pricing annoying, so we're switching everyone to a simple flat plan of €99/month for unlimited seats. Our top 10 customers, around 60% of revenue, each have 80+ seats. Simpler pricing should help sales. Go?

Unedited answer from the blind eval run (case `F01`).

---

**Decision**: Decide whether to replace €12/seat/month with a flat €99/month unlimited-seat plan for all customers, when the top 10 accounts (80+ seats each) bring in ~60% of revenue.
**Verdict**: Don't do it as stated. Simplify, but use seat bands priced so your top accounts pay about what they pay today. · Confidence: 9/10

**The math the plan leaves out** (from your figures): each top account pays at least 80 × €12 = €960/month. Ten of them pay at least €9,600, so total MRR is at least about €16,000. On €99 flat, those ten pay €990, so you lose at least €8,600/month, or **at least 54% of total revenue**, on day one. And every customer with 8 or fewer seats (8 × €12 = €96) gets a price **increase**. You'd cut revenue from your biggest customers and raise prices on your smallest.

**Agreement**: Per-seat friction is real and worth fixing. A €99 price for unlimited seats is not the fix.
**Real disagreement**: Whether flat pricing brings in enough new logos to make up for the loss. You'd need roughly 87+ new €99 customers just to get back to today's revenue, and big buyers would get no reason to pay more as they grow.
**Assumption that matters most**: That customers object to *paying per seat*, not to *how* it works (true-ups, approving each new user, invoices that change every month). → Ask 5 to 8 customers this week what exactly annoys them.
**Closest precedents**: ☠ MoviePass: one flat price, and the heaviest users (here, your 80+ seat accounts) capture all the value. Matches: flat-price model, mechanism. Differs: B2C, and it had a cost per use. ✓ AMC A-List survived the same trap by pricing from real usage data and capping it. ✓ Basecamp (general knowledge, not from the library) is a B2B flat-price success, but it was flat from the start. It didn't move large per-seat accounts onto a lower price.

**Next step (48 h)**: Export seats per customer and model three options: (a) €99 flat, (b) bands such as ≤10 / ≤50 / ≤150 / unlimited, set so that no top-10 account's bill drops more than 10%, (c) per-seat with annual billing and no mid-term true-ups. Pick the option that keeps ≥95% of MRR.
**Kill criterion**: if a pilot of the new pricing on new signups only hasn't lifted trial-to-paid conversion by ≥20% within 90 days, keep current pricing for existing accounts. If any top-10 account asks to renegotiate down, pause the rollout.

▸ The Crew
- Nix · Devil's advocate: You'd lose at least 54% of MRR overnight, and repricing big accounts down is close to a one-way door.
- Root · First principles: The problem is friction, not the unit. Fix billing mechanics (annual seats, a fair-billing credit for inactive users).
- Nova · Expansionist: Flat pricing could work for small teams as a starter tier capped at a seat limit.
- Pip · Outsider: "Unlimited for €99" makes a buyer ask why big companies pay the same as small ones.
- Tack · Executor: You can model the bands tomorrow. Grandfather existing contracts and test on new signups first.
- Penny · Finance: Price on value, not to make the invoice simpler. Your expansion revenue goes away.

📊 Want the visual report? One page you can share with your team: Vera's verdict, the Crew with each member's position, MoviePass and AMC A-List side by side, and the three pricing options to model this week. Just say "yes".
