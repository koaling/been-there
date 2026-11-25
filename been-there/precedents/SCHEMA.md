# Precedent schema

One file per company: `precedents/<slug>.yaml`. Keep entries short, factual and sourced.

```yaml
name: Webvan
slug: webvan
type: failure            # failure | survivor
years: 1996-2001
region: US               # US | EU | ES | LATAM | ASIA | global
sector: grocery-delivery
business_model: b2c-delivery-own-infrastructure
funding: "~$800M (incl. IPO)"   # approximate, with ~ when unsure
causes:                  # 1-3 tags from the list below, most important first
  - premature-scaling
  - unit-economics
root_cause: >
  One or two sentences: the mechanism, not the final symptom
  ("ran out of money" is a symptom, not a cause).
warning_signs:
  - Early signal that was visible before the end.
survived_by: [instacart] # slugs of survivors that faced the same trap
lesson: One sentence a founder can act on.
sources:
  - type: founder-postmortem | news | analysis | ai-generated
    title: ...
    url: ...
notes: Optional context (e.g. the brand was relaunched later).
status: needs-source     # needs-source | verified
```

Survivors use the same fields, with `type: survivor`, `causes` = the traps they faced, and `root_cause` = what they did differently.

## Cause tags

| tag | meaning |
|---|---|
| no-market-need | Solved a problem not enough people had |
| unit-economics | Lost money on every unit sold |
| pricing | Price too low to sustain or too high to adopt |
| premature-scaling | Scaled spend/infrastructure before product or economics worked |
| competition | Outcompeted by a cheaper, free or bigger alternative |
| timing | Market, tech or behaviour not ready (or too late) |
| overengineering | Product far more complex/expensive than the need |
| regulation | Legal, regulatory or compliance blow-up |
| labor-model | Workforce model broke (classification, churn, quality) |
| distribution | Couldn't reach customers at a sustainable cost |
| retention | Customers didn't stay |
| trust-privacy | Users or society rejected it on trust/privacy grounds |
| team | Founder or team breakdown |
| fraud | Misrepresentation of the product or numbers |
| platform-dependency | Killed by a platform it depended on |

## Evidence weight

1. `founder-postmortem` — strongest (but biased toward external causes).
2. `news` / `analysis` — good for facts and numbers.
3. `ai-generated` (e.g. AI-written database summaries) — weak; never the only source.

Entries with `status: needs-source` must get at least one source before being marked `verified`.
