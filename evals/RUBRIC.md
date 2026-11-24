# How to run and score the evals

Goal: show, with numbers, whether Precedent Council beats a baseline (e.g. the original LLM Council skill, or plain Claude) at spotting real failure patterns **without** becoming a blanket pessimist.

## Run

For each case in `cases.yaml`, in a **fresh conversation**, paste only the `prompt`. Run it once with each setup:

- **A — baseline**: plain Claude, or another council skill.
- **B — precedent-council**.

Save each answer as `evals/results/<setup>/<id>.md`. Use the same model for both setups and note it in `results/README.md`.

## Score (per answer)

| Criterion | Points |
|---|---|
| **Mechanism**: names the real failure mechanism (`pattern`) in its own words | 0 / 1 / 2 |
| **Verdict**: trap → not an unconditional "go"; control → not an outright "don't" | 0 / 2 |
| **Grounding**: cites at least one relevant precedent that matches ≥2 dimensions, with no invented facts | 0 / 1 |
| **Actionable**: next step is a cheap test that would reveal the problem | 0 / 1 |

Max 6 per case. Any invented company or fact → grounding = 0 and flag it.

Report:

- **Traps caught**: traps with Verdict = 2 (out of 10).
- **False alarms**: controls with Verdict = 0 (out of 3).
- **Average score** per setup.

## Fairness rules

- Don't edit prompts between setups.
- The grader shouldn't know which setup produced the answer (shuffle and hide labels), or use a separate model as grader with this rubric.
- Publish all raw answers, including the ones where B loses.
- **Leakage**: if a case's `based_on` company is in `precedents/`, B is partly being tested on retrieval. Report scores split into "in library" and "not in library"; the second number is the honest one.
