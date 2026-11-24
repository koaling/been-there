# Precedent Council 🏛️

**A Claude skill that pressure-tests your decisions with a council of advisors who argue from real precedents — the startups that died of the same mistake, and the ones that survived it.**

*[Español abajo](#español)*

> LLM-council skills give you five opinions from the same model. Precedent Council makes them bring evidence, review each other blind, and tell you who already tried this — and how it ended.

<!-- TODO: demo GIF here -->

## Benchmark

**Hard set** (v0.2): 8 real failures where the fatal fact is *not* in the prompt + 4 real successes that looked risky. Graded blind.

| | Hidden flaw found (of 8) | Rubric score (of 72) | Judged better | Avg length |
|---|---|---|---|---|
| Plain Claude | 7 | 66 | 1 | ~815 words |
| **Precedent Council** | **8** | **72** | **6** | **~590 words** |
| LLM Council | – | – | – | – |

(5 ties.) On a third set of 12 **fictional** cases (the flaw is hidden in the numbers, nothing to recall), both found 8/8 flaws and it was a tie (72 vs 71). Honest read: detection is close; the skill wins on real precedents (12/12 vs 8/12), cheap next steps and not being pessimistic on good ideas, while being shorter. Raw answers, grades and caveats: [`evals/results/`](evals/results/).

## What makes it different

- **Precedents first.** Before anyone gives an opinion, the council finds companies that faced the same trap. Failures *and* survivors, because a pattern that killed 5 companies and was survived by 50 isn't a warning.
- **Explicit similarity.** Each precedent shows which dimensions match (market, model, timing, mechanism) and which don't. Weak analogies are dropped.
- **Evidence or label.** Arguments without a precedent or a fact you gave are marked *(opinion)*, and the chair weighs them less.
- **Blind review and a debate round** when the advisors really disagree.
- **A verdict you can act on:** confidence, the one assumption to test, a 48-hour next step and a kill criterion.
- **Shareable visual report** (`templates/report.html`).

## Install

Paste into Claude Code (or any Claude surface with skills):

```
Install this Claude skill: https://github.com/<you>/precedent-council
```

Or copy the folder into `~/.claude/skills/precedent-council/`.

## Use

```
Council this: should I raise prices this month or wait for more customers?
```

Also: `quick council:`, `pressure-test this`, `where am I wrong`, `consejo:`.

## Contribute a precedent

The precedent library is the heart of the project. Add a company in one YAML file: see [`precedents/SCHEMA.md`](precedents/SCHEMA.md). Rules: factual, short, with at least one source; founder post-mortems preferred. Survivors are as welcome as failures. EU and Spanish cases especially wanted.

## Roadmap

- [x] v0.1 — council, precedent schema, 10+3 evals, HTML report
- [x] v0.2 — short default output, "hunt the unstated assumption", hard eval set (8+4)
- [ ] Eval cases the model can't recall (fictional/recent failures, non-startup decisions)
- [ ] 30 verified precedents (failures + survivors)
- [ ] Publish benchmark results
- [ ] Regulatory pack (GDPR, health, fintech, AI Act)
- [ ] Decision log review reminders

---

## Español

**Una skill de Claude que somete tus decisiones a un consejo de asesores que argumentan con precedentes reales: las startups que murieron por el mismo error y las que lo superaron.**

- **Primero los precedentes.** Antes de opinar, el consejo busca empresas que cayeron en la misma trampa, y también las que sobrevivieron.
- **Parecido explícito.** Cada precedente muestra en qué se parece a tu caso y en qué no. Las analogías flojas se descartan.
- **O pruebas o etiqueta.** Lo que no está respaldado se marca como *(opinión)*.
- **Revisión a ciegas y ronda de debate** cuando los asesores chocan.
- **Veredicto accionable:** confianza, el supuesto clave, el paso para las próximas 48 h y un criterio para cambiar de rumbo.

Uso: `Consejo: ¿subo precios este mes o espero a tener más clientes?`

Contribuir: añade una empresa en un YAML siguiendo [`precedents/SCHEMA.md`](precedents/SCHEMA.md). Se buscan especialmente casos europeos y españoles.

## License

Code and skill: MIT. Precedent library: CC BY 4.0.
