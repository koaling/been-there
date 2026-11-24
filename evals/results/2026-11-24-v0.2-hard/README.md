# Run 2026-11-24 · v0.2 · hard set (`cases-v2.yaml`)

8 real failures where the fatal fact is **not** stated in the prompt (Bird, Color, Zirtual, Fab, Shyp, Fast, Zume, Vine) + 4 real successes that looked risky (Zoom, Canva, Twitch, Netflix streaming). None of them are in `precedents/`, so there's no leakage.

**Setups**: `plain-claude` (no skill) vs `precedent-council` v0.2 (short default output + "hunt the unstated assumption"). Same model, fresh sessions, no web search. Blind grading by a separate session (key in `blind_key.json`).

## Results

| | Hidden factor found & central (of 8) | Unconditional "go" on traps | "Give up" on controls | Rubric total (of 72) | Judged better | Avg length |
|---|---|---|---|---|---|---|
| Plain Claude | 7 | 0 | 0 | 66 | 1 | ~815 words |
| Precedent Council | 8 | 0 | 0 | **72** | **6** | **~590 words** |

5 ties on "better".

## What this tells us

- **Detection is still close.** Even with the fatal fact hidden, plain Claude finds it in 7 of 8 cases (it missed making scooter lifespan the central risk in H01). The model already knows many of these stories, so the case set is still not hard enough to separate the two on detection alone.
- **The skill wins on grounding and actionability:** it named a real, relevant precedent in 12/12 answers (plain Claude: 8/12) and always ended with a cheap 48-hour test.
- **Better on controls:** 3 of the 4 controls went to the skill, so the "lead with real user pull" rule worked; no more pessimism on successes.
- **Shorter:** the v0.2 default output is ~30% shorter than plain Claude (v0.1 was 2.5× longer).
- **No invented facts** found.

## Next

Detection needs cases the model can't recall: fictional or recent/obscure failures, and non-startup decisions (pricing, hiring, internal projects).
