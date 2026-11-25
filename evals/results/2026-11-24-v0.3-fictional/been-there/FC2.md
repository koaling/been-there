**Decision**: Raise list price 30% for new customers only (existing customers keep their price), based on an A/B test of ~200 visitors.
**Verdict**: Do it like this: ship the new price, but don't trust the test. Treat the rollout itself as the real test, with a kill criterion. · Confidence: 6/10

Assumptions (you didn't say): a typical conversion rate of 2–10%, self-serve signup, and a price you can change back easily. That last one makes this a two-way door.

**Agreement**: 200 visitors proves almost nothing. Split ~100/100 at a 3% conversion rate, that is about 3 conversions per arm. "Conversion didn't change" can't rule out a 50% drop. Spotting the drop that matters would take roughly 10k visitors per arm at 3% conversion, or ~2.7k at 10% (estimate, 80% power). But the math is on your side: at +30%, conversion can fall up to **~23%** before revenue per visitor goes down. Keeping existing customers on their old price removes the main backlash risk.

**Real disagreement**: whether to keep testing or just ship. The Executor says ship: the change is cheap to undo, and a longer test at your traffic could take months. The Devil's advocate says the test only measured signups. Higher-paying customers may churn faster or ask for more refunds, and that shows up 1–3 billing cycles later.

**Assumption that matters most**: that the new cohort *stays* as well as the old one, not just that they sign up. → Cheapest test: compare 30/60-day churn, refunds and downgrades of the new-price cohort against the last 2–3 old-price cohorts.

**Closest precedent**: no strong precedent found in the library. MoviePass and AMC A-List are pricing cases, but they're about pricing below cost vs. pricing from usage data. Netflix's 2011 price hike, the famous backlash, hit *existing* subscribers, which is exactly the trap you avoid. Neither qualifies as a close match.

**Next step (48 h)**: write down your baseline: conversion per 1,000 visitors over the last 8 weeks, plus first-month churn and refunds. Then switch 100% of new traffic to the new price and log the date.

**Kill criterion**: change course (roll back or try +15%) if, after ~4 weeks or 50+ conversions, whichever is later, conversion is down >20% vs. baseline, or new-cohort 30-day churn is >1.5× the old cohort's.

▸ Council
- **Devil's advocate**: against trusting the data. The test is noise, and it measured signups, not retention. (medium)
- **First principles**: the real question is "are we underpriced?" Win/loss reasons and sales objections answer that better than 200 visitors. (medium)
- **Expansionist**: for it. The 23% break-even gives a big buffer, and new revenue compounds. (medium)
- **Outsider**: will new customers see the old price somewhere (cached pages, review sites, referrals) and feel cheated? (opinion, low)
- **Executor**: for it. One config change, reversible in minutes. Without a baseline, though, you'll never know if it worked. (high)
- **Finance** (seat added because this is a revenue decision): judge it on revenue per visitor and 90-day LTV, not on conversion. (high)

Want the visual report or a decision-log entry? Just say so.
