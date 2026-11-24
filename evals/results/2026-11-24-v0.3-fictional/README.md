# Run 2026-11-24 · v0.2 skill · fictional set (`cases-v3.yaml`)

12 fictional cases the model can't recall: 8 traps whose fatal flaw is derivable from the prompt's own numbers or details (pricing, hiring vs runway, marketplace take rate, exclusive distributor, LTV/CAC, GDPR health data, seasonality, team overload) + 4 sound plans that look risky. Same model, fresh sessions, no web search, blind grading.

| | Flaw found & central (of 8) | Rubric total (of 72) | Judged better | Avg length |
|---|---|---|---|---|
| Plain Claude | 8 | 71 | 3 | ~720 words |
| Precedent Council | 8 | 72 | 4 | ~565 words |

5 ties.

## What this tells us

- **Effectively a tie.** When the flaw is in the numbers, plain Claude finds it too. The skill does not add detection power on these cases.
- **What the skill does add:** a consistent, shorter format (verdict + confidence + 48 h test + kill criterion), about 20% fewer words.
- **Weakness found:** when no precedent fits, the skill sometimes adds "no precedent in library" filler. To fix: omit the precedents line when none qualifies.
- **Caveat:** one plain-Claude answer (FC3) mentioned context that wasn't in the prompt (a healthcare client), which looks like personal context leaking from the test environment. It cost that answer one point.
