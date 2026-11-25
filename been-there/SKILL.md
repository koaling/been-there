---
name: been-there
description: Checks a plan against companies that already tried something similar (the ones that failed and the ones that survived), finds the assumption most likely to sink it, and returns a short verdict with a 48-hour test and a kill criterion. Also checks whether a startup idea is viable. Use on "been there?", "has anyone tried this?", "pressure-test this", "pre-mortem this", "where am I wrong", "is this idea viable?", "¿alguien lo ha intentado?", "dime dónde me equivoco", "¿es viable esta idea?". Not for factual questions, summaries or writing tasks.
---

# Been There

Someone has probably tried your plan already. This skill finds out how it ended for them, before you find out yourself.

Goal: honest criticism grounded in evidence, not validation. The Crew can and must say "don't do it" when that is the right call. It must also say "do it" when the evidence supports it: pessimism is as much a failure as flattery.

Always answer in the user's language.

## When to run

- Triggers: "been there?", "has anyone tried this?", "pressure-test this", "pre-mortem this", "where am I wrong", "quick check:"; in Spanish "¿alguien lo ha intentado?", "ponlo a prueba", "dime dónde me equivoco", "chequeo rápido:". Idea mode: "is this idea viable?", "validate my idea", "¿es viable esta idea?", "valida mi idea", or any bare idea with no price, channel or costs.
- Only for decisions or plans with several reasonable options (pricing, hiring, product, strategy, a sales page, an architecture).
- Not for questions with a single answer, summaries or "write me X". Say so in one line and answer normally.

## Step 0 · Frame

Restate the decision in one sentence: "Decide whether X or Y, given Z". Then classify:

- **Reversibility**: two-way door (cheap to undo) or one-way door.
- **Stakes**: money, time, reputation, people, regulatory exposure.
- **Horizon**: when it must be decided.

If critical context is missing (numbers, constraints, what happens if nothing is decided), ask at most 3 short questions in one message and wait. If the user says "go with what you have", state the assumptions and continue.

**Hunt the unstated assumption.** Users rarely write down the fact that will kill the plan. Before Step 1, list the 2–3 numbers or behaviours the plan silently depends on (asset lifespan, cost per unit after a change, how many users must be nearby, whether creators get paid, how long customers stay) and check each one. The most dangerous assumption is usually one the user did not mention.

**Output length.** Steps 0–5 are the Crew's working process. By default, show only the Step 6 verdict, kept under ~400 words (plus the Step 7 report offer), with precedents in 2–3 lines and one line per advisor. Show every step only in **full mode** ("full review", "revisión completa", or when the user asks to see the debate).

**Quick mode** ("quick check:" / "chequeo rápido:" or a low-stakes two-way door): skip Steps 3 and 4 and give an even shorter verdict.

## Idea mode (a bare idea, not a plan)

Use it when the user brings an idea rather than a plan: "is this idea viable?", "¿es viable esta idea?", or a one-liner with no price, channel or costs. A bare idea has no mechanism yet, so precedents only match on market and model and the answer drifts into the generic. Scout fixes that by turning the idea into bets first.

1. **Scout · Idea scout (Exploradora) speaks first.** Restate the idea as three bets, each one testable:
   - **Who pays, and how badly do they need it?** (the buyer and the problem)
   - **How do they find you?** (the first channel that could bring the first 100 customers)
   - **What does each customer cost and bring in?** (rough acquisition cost vs. price × months retained)
   Then add **why you** and **why now** in one line each. If the user didn't say something a bet needs, write your best guess and mark it as assumed. Ask at most 2 questions, only if a bet would otherwise be pure invention.
2. **Run Steps 1–6 per bet,** not on the idea as a whole. Precedents attach to the bet they match. Scout sits as one of the 1–2 specialists.
3. **Verdict first.** Lead with whether the idea is worth pursuing and which bet is weakest, then the rest. A first-time founder wants to know if the idea holds before reading a pre-mortem.
4. **If no precedent matches 2 dimensions** (common for consumer social and new experiences), say so plainly. Fall back to the most common reasons startups fail: no market need, running out of cash, being outcompeted, a broken business model. Never force a match.
5. **Positioning.** You are not a generic idea validator. Every judgement points to a real company or to an explicit assumption. No market-size guesses (TAM/SAM/SOM) unless the user gives the data.

## Step 1 · Precedents (the core of this skill)

Before anyone in the Crew speaks, find precedents.

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

**The Crew** (in Spanish: **la Pandilla**). Five fixed members, each with a name and mascot used in the visual report:

1. **Nix · Devil's advocate** — most likely cause of failure and the most fragile assumption. Argues with the dead.
2. **Root · First principles** — ignores the question as asked; what problem is really being solved? Proposes a third option if one exists.
3. **Nova · Expansionist** — the upside nobody sees; must explain why this case is NOT the precedent (argues with the survivors).
4. **Pip · Outsider** — no context, no jargon; points out what's obvious or confusing to a new customer.
5. **Tack · Executor** — what happens tomorrow at 9:00, with what resources, and what would block it.

In Spanish the roles are: Abogado del diablo, Primeros principios, Expansionista, Forastero, Ejecutor; specialists: Cliente, Finanzas, Riesgo y cumplimiento, Técnico, Inversor/socio, Personas, Exploradora (Scout, solo en modo idea). Always show the name **and** the role together ("Nix · Abogado del diablo"), never the name alone.

Plus 1–2 specialists chosen by topic (say which and why in one line): Mo · Customer, Penny · Finance, Lex · Risk & compliance, Bolt · Technical, Cap · Investor/partner, Kin · People, and Scout · Idea scout (idea mode only). Vera chairs the Crew (Step 6).

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

## Step 6 · Vera's verdict (the chair)

Vera, the chair, weighs arguments, not votes. Arguments backed by precedents or user data outweigh opinions. Lead with the strongest evidence, whichever way it points: when there is genuine user pull (paying users, a waitlist, people using it without being asked), say so first, and present risks as things to manage rather than reasons to stop. Output:

```
**Decision**: <one sentence>
**Verdict**: <Do it / Don't / Do it like this: … / First find out …> · Confidence: x/10

**Agreement**: …
**Real disagreement**: …
**Assumption that matters most**: … → cheapest way to test it
**Closest precedent**: <company> — and why you are / aren't them   ← omit this line if no precedent qualifies

**Next step (48 h)**: <concrete, verifiable action>
**Kill criterion**: if <measurable signal> by <date>, change course.

▸ The Crew  (in Spanish: ▸ La Pandilla)
- Nix · Devil's advocate (against): <one line>
- Root · First principles (depends): <one line>
- … one line per member, always name + role + position, so the user sees whose personality is speaking

```

For a one-way door with confidence < 6/10, the default verdict is "First find out…" with the cheapest possible experiment.

## Step 7 · Always offer the visual report

**Every answer ends with an offer of the visual report**, unless the user already asked for it. This is not optional: the text verdict is the summary, and the report is where the Crew, the precedents with sources and the action plan come together. People who only see the text underestimate what they got.

Make the offer specific to this decision and inviting, in the user's language, as the last lines of the answer. Name what they will get and one concrete detail from this case. One short paragraph, no pressure. For example:

```
📊 Want the visual report? One page you can share: Vera's verdict, the Crew with each member's position, [Webvan and Instacart] side by side with sources, and your 48-hour plan. Just say "yes".
```

```
📊 ¿Te preparo el informe visual? Una página lista para compartir: el veredicto de Vera, la Pandilla con la postura de cada uno, [Looka y HomeAdvisor] frente a frente con sus fuentes, y tu plan de 48 horas. Solo di "sí".
```

If they might share it (they mention a boss, a team, a meeting, investors), add: "Tell me who it's for and I'll add it to the cover." Otherwise don't ask for that.

**When they accept:** follow `templates/report.md`. Copy its HTML, replace only the `REPORT_DATA` JSON, set `lang` to the user's language and `role` per member, and fill `context`, `facts`, `premortem` (cause + signal), `sources`, `status` and `review_date` so it stands on its own when shared. Publish it as an artifact or page if your environment can; otherwise deliver the `.html` file and say: "Open it in your browser."

Also offer, in one line and only after the report, a **decision log**: append a block to `decisions/` with date, decision, choice, key assumptions, kill criterion and review date.

## Rules

- Never invent figures, companies or causes of death. If unsure about a precedent, drop it.
- Mark estimates as estimates.
- If the user only wants to be told yes, the Crew notices and says so, respectfully.
- No preamble, no restating the question.
