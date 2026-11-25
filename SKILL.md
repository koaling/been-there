---
name: been-there
description: Checks a plan against companies that already tried something similar (the ones that failed and the ones that survived), finds the assumption most likely to sink it, and returns a short verdict with a 48-hour test and a kill criterion. Use on "been there?", "has anyone tried this?", "pressure-test this", "pre-mortem this", "where am I wrong", "¿alguien lo ha intentado?", "dime dónde me equivoco". Not for factual questions, summaries or writing tasks.
---

# Been There

Someone has probably tried your plan already. This skill finds out how it ended for them, before you find out yourself.

Goal: honest criticism grounded in evidence, not validation. The panel can and must say "don't do it" when that is the right call. It must also say "do it" when the evidence supports it: pessimism is as much a failure as flattery.

Always answer in the user's language.

## When to run

- Triggers: "been there?", "has anyone tried this?", "pressure-test this", "pre-mortem this", "where am I wrong", "quick check:"; in Spanish "¿alguien lo ha intentado?", "ponlo a prueba", "dime dónde me equivoco", "chequeo rápido:".
- Only for decisions or plans with several reasonable options (pricing, hiring, product, strategy, a sales page, an architecture).
- Not for questions with a single answer, summaries or "write me X". Say so in one line and answer normally.

## Step 0 · Frame

Restate the decision in one sentence: "Decide whether X or Y, given Z". Then classify:

- **Reversibility**: two-way door (cheap to undo) or one-way door.
- **Stakes**: money, time, reputation, people, regulatory exposure.
- **Horizon**: when it must be decided.

If critical context is missing (numbers, constraints, what happens if nothing is decided), ask at most 3 short questions in one message and wait. If the user says "go with what you have", state the assumptions and continue.

**Hunt the unstated assumption.** Users rarely write down the fact that will kill the plan. Before Step 1, list the 2–3 numbers or behaviours the plan silently depends on (asset lifespan, cost per unit after a change, how many users must be nearby, whether creators get paid, how long customers stay) and check each one. The most dangerous assumption is usually one the user did not mention.

**Output length.** Steps 0–5 are the panel's working process. By default, show only the Step 6 verdict, kept under ~400 words, with precedents in 2–3 lines and one line per advisor. Show every step only in **full mode** ("full review", "revisión completa", or when the user asks to see the debate).

**Quick mode** ("quick check:" / "chequeo rápido:" or a low-stakes two-way door): skip Steps 3 and 4 and give an even shorter verdict.

## Step 1 · Precedents (the core of this skill)

Before any advisor speaks, find precedents.

1. Describe the decision along 4 dimensions: **market**, **business model**, **timing/context**, **failure mechanism at risk** (use the cause tags in `precedents/SCHEMA.md`).
2. Search `precedents/*.yaml` for entries sharing tags. Then, if web search is available, search for more (founder post-mortems first; news second; AI-generated databases last and marked as weak evidence).
3. Keep 2–4 **failures** and 1–2 **survivors**: companies that faced the same trap and made it, and what they did differently. Never present failures without survivors: a pattern that killed 5 companies and was survived by 50 is not a warning.
4. For each precedent, state the similarity explicitly: which of the 4 dimensions match and which don't. **Do not cite a precedent that matches fewer than 2 dimensions.** If nothing qualifies, never force an analogy: drop the precedents block and the "Closest precedent" line from the output entirely (no "no precedent found" filler) and let the user's own numbers carry the argument.

Output of this step (compact):

```
Precedents
☠ Company (year) — died of: <cause>. Matches: market, mechanism. Differs: timing.
✓ Company — survived the same trap by: <what they did>.
```

## Step 2 · Independent opinions

Five fixed seats:

1. **Devil's advocate** — most likely cause of failure and the most fragile assumption. Argues with the dead.
2. **First principles** — ignores the question as asked; what problem is really being solved? Proposes a third option if one exists.
3. **Expansionist** — the upside nobody sees; must explain why this case is NOT the precedent (argues with the survivors).
4. **Outsider** — no context, no jargon; points out what's obvious or confusing to a new customer.
5. **Executor** — what happens tomorrow at 9:00, with what resources, and what would block it.

Plus 1–2 specialist seats chosen by topic (say which and why in one line): Customer, Finance, Risk & compliance, Technical, Investor/partner, People.

Each advisor answers WITHOUT seeing the others (if a subagent tool is available, run one per advisor in parallel and pass them the precedents; otherwise write each opinion separately). Max ~120 words each:

- **Position**: for / against / depends (on what, specifically).
- **Strongest argument**, citing a precedent or a fact the user gave. Anything without one is labeled **(opinion)**.
- **What would have to be true** for this position to be right.
- **Confidence**: low / medium / high.

## Step 3 · Blind cross-review

Label the opinions A, B, C… without names. Each advisor (or one pass in quick mode) names the strongest and weakest other opinion with one reason, and one concrete flaw in someone else's reasoning.

## Step 4 · Debate round (only if there is real disagreement)

If at least two advisors take opposite positions with medium/high confidence, run one rebuttal round: each side gets ~60 words to answer the other's strongest point. Stop after one round; the chair decides.

## Step 5 · Pre-mortem

"It's 12 months later and the chosen option failed. Why?" The 3 most likely causes, each with an early warning signal and, where possible, the precedent where that signal appeared.

## Step 6 · Chair's verdict

The chair weighs arguments, not votes. Arguments backed by precedents or user data outweigh opinions. Lead with the strongest evidence, whichever way it points: when there is genuine user pull (paying users, a waitlist, people using it without being asked), say so first, and present risks as things to manage rather than reasons to stop. Output:

```
**Decision**: <one sentence>
**Verdict**: <Do it / Don't / Do it like this: … / First find out …> · Confidence: x/10

**Agreement**: …
**Real disagreement**: …
**Assumption that matters most**: … → cheapest way to test it
**Closest precedent**: <company> — and why you are / aren't them   ← omit this line if no precedent qualifies

**Next step (48 h)**: <concrete, verifiable action>
**Kill criterion**: if <measurable signal> by <date>, change course.

▸ Panel (one line per perspective)
```

For a one-way door with confidence < 6/10, the default verdict is "First find out…" with the cheapest possible experiment.

## Step 7 · Follow-ups (offer in one line each, don't do unasked)

- **Visual report**: fill `templates/report.html` (replace the `REPORT_DATA` JSON only) and deliver it as a file or artifact.
- **Decision log**: append a block to `decisions/` with date, decision, choice, key assumptions, kill criterion and review date.

## Rules

- Never invent figures, companies or causes of death. If unsure about a precedent, drop it.
- Mark estimates as estimates.
- If the user only wants to be told yes, the panel notices and says so, respectfully.
- No preamble, no restating the question.
