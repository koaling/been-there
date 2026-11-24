## The Council

**The Pragmatist (CTO hat)**
One developer-day a week is about 20% of an engineer. Over a year that's roughly 50 dev-days recovered for a 10-day investment, so it pays for itself in about 10 weeks. With a feature-flag rollback, the downside is capped. Go.

**The Security Officer**
Home-built auth is a liability even when it "works". "It works" usually means "nobody has broken it yet." A managed provider gives you MFA, passkeys, breached-password detection, brute-force protection, anomaly detection and fast patching, and you'd struggle to build any of these well yourselves. You also stop owning password hashes, which takes a big target off your back. Go, with conditions (below).

**The Skeptic ("if it works, don't touch it")**
That's a fair instinct, so here's the strongest version of it:
- **Migration risk:** if bcrypt/argon2 hashes can't be imported, users may need a forced reset or a lazy migration on first login.
- **The rollback flag is only half true.** Rolling back the login screen is easy. Rolling back *data* is not: users who sign up, change passwords or enrol MFA in the new system while the flag is on won't exist in the old one. Unless you dual-write or sync, rollback gets messy after day one.
- **Lock-in and cost:** per-MAU pricing scales with you, and leaving later is painful.
- **New dependency:** if their outage happens, your login goes down too.

**The Compliance / Legal voice**
This one matters for you specifically. If this touches the healthcare client's environment, check before signing anything:
- Data residency (EU region), GDPR DPA, and sub-processors
- Their certifications (ISO 27001, SOC 2) and whether the client's ISO scope or security policy allows a third-party IdP
- Whether the client's restricted network can even reach the provider's endpoints
This could be the real blocker, more than the technical side.

**The Product / UX voice**
Users only notice auth when it breaks. Look at the hosted vs. embedded login UI, email deliverability (reset/verification emails from a new domain land in spam), and session continuity. Nobody should be logged out en masse on cutover day.

---

## Verdict: **Go, conditionally**

The "don't touch it" argument holds for code that's stable *and* cheap to maintain. Yours costs a developer-day every week, and it's security-critical code, the worst kind of thing to keep custom. The ROI is clear and the risk can be managed.

**Conditions before you start:**
1. **Compliance check first** (residency, DPA, client/ISO approval). Half a day, and it can kill the project, so do it before anything else.
2. **Confirm the password hash import** works with your hashing scheme. If it doesn't, plan a lazy migration (verify against the old store on first login, then move the user over).
3. **Make the rollback real:** decide how you'll handle users created or changed during the new-system window (dual-write, a sync job, or a short and explicit point of no return).
4. **Gradual rollout:** internal users, then 5%, then 25%, then 100%, watching login success rate, error rates and support tickets.
5. **Exit plan:** confirm you can export users (including hashes) if you ever leave.
6. **Keep the old system read-only for 30 to 60 days** before decommissioning it.

**To win over the skeptics:** don't argue. Show them the numbers (dev-day cost vs. migration cost), name the specific risks they're worried about, and show how each one is mitigated. Also give them a clear kill criterion, for example: "if login success drops more than X% or the compliance check fails, we stop."
