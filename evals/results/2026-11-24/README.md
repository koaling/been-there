# Run 2026-11-24 · v0.1

**Setups**
- `plain-claude`: Claude with no skill, fresh session, prompt only.
- `precedent-council`: same model, fresh session, with `SKILL.md` + `precedents/` (6 entries) loaded.
- Same model for both. No web search in either.
- The original LLM Council skill was **not** tested in this run.

**Grading**: blind (answers shuffled as X/Y; key in `blind_key.json`) by a separate model session using `evals/RUBRIC.md`. Raw scores are in `grades.json`.

## Results

| | Traps caught (of 10) | False alarms (of 3) | Rubric total (of 78) | Judged better overall | Avg length |
|---|---|---|---|---|---|
| Plain Claude | 10 | 0 | 76 | 3 | ~815 words |
| Precedent Council | 10 | 0 | 77 | 7 | ~2,050 words |

(3 ties on "better overall".)

## What this tells us

- **The test set is too easy.** Every prompt states its own red flag ("loses €4 per order", "you can squeeze the packs by hand"), so plain Claude catches all 10 traps too. The rubric can't separate the setups. v0.2 needs subtler traps where the warning sign is not in the prompt.
- **The skill's edge is in usefulness, not detection.** The grader preferred it 7–3, mainly for dated kill criteria with numbers and more precise next tests.
- **It's ~2.5× longer.** Too long for many uses → a shorter default output is needed.
- **No invented facts** were found in either setup.
- **Mild pessimism on controls:** the skill leads with the devil's advocate on C02/C03 but never says "stop".
- **Leakage:** 4 traps (T01–T04) are in the precedent library. The skill's advantage holds on T05–T10 too (4 better, 2 ties, 0 worse), but the sample is tiny.
