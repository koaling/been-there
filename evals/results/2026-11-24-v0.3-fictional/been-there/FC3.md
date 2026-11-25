**Decision**: Replace the home-built login with a managed auth provider (about 2 weeks, behind a feature flag), or keep the current one.
**Verdict**: Do it like this: migrate, but make rollback real before you flip the flag, and price the vendor at 3x your current user count. · Confidence: 7/10

**Precedents**: no strong precedent found. Nothing in the library matches 2 or more dimensions; the startup failure cases (Webvan, MoviePass and others) are about business models, not build-vs-buy infrastructure. This verdict rests on your numbers and on general engineering knowledge.

**Agreement**: 1 dev-day a week is about 20% of one engineer, so 2 weeks of work pays back in about 10 weeks (estimate). "If it works, don't touch it" leaves out a hidden cost: login is security-critical code. Every month it stays home-built, you own MFA, password resets, brute-force protection and breach response yourselves.

**Real disagreement**: Whether this is really a two-way door. The flag reverts the code, not the data. Once users reset passwords, enrol MFA or sign up on the provider, flipping back strands those accounts unless changes sync both ways.

**Assumption that matters most**: That you can move password hashes without forcing everyone to reset. Many providers import common formats (e.g. bcrypt). A custom or salted-SHA scheme may need "lazy migration" (check against the old store on first login, then move the user over). → Cheapest test: export 100 test accounts and import them into the provider's free or dev tier this week.

**Other silent assumptions**: (1) per-user pricing stays affordable as you grow; (2) the 1 day/week is measured, not felt; check the last 8 weeks of tickets and commits on auth; (3) the vendor's outage or breach becomes yours, so plan a status page and a degraded mode.

**Next step (48 h)**: Spike: hash import of 100 test users, plus a written rollback plan that covers accounts created or changed after cutover.
**Kill criterion**: If hashes can't be imported without a mass reset, or projected cost at 3x users exceeds the value of 1 dev-day/week, stop by the end of week 1 and harden the in-house system instead.

▸ Council
- Devil's advocate: rollback is a data problem, not a flag problem; risky if ignored.
- First principles: the real goal is auth security and time back; a third option is to keep it but outsource MFA only (opinion).
- Expansionist: you get SSO, MFA and passkeys almost for free, which opens B2B deals.
- Outsider: users only notice if they're forced to reset or see a new login screen. Keep it seamless.
- Executor: 2 weeks is realistic only if hash import works; add 1 week of buffer for edge cases (social logins, locked accounts).
- Specialist, Risk & compliance (auth = sensitive data): review the vendor's DPA, data residency (EU) and certifications before signing.

*Want a visual report or a decision-log entry? I can do either.*
