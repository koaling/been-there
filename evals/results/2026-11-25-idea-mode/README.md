# Idea-mode feasibility check (2026-11-25)

**Question:** can Been There find useful precedents for a bare startup *idea* (no price, channel or costs yet)?
**Pass rule (from the skill):** an idea passes if it gets **≥2 precedents that each match ≥2 of the 4 dimensions** (market, model, timing, mechanism).
**Go/no-go agreed beforehand:** build idea mode only if **≥6 of 10** ideas pass.

Ten typical idea-stage prompts, written to resemble what first-time founders post. Each was scored twice: using only the repo's precedent library (35 cases), and with the live research the skill is allowed to do.

| # | Idea | Library only | With research | Precedents found (dimensions matched) |
|---|---|---|---|---|
| 1 | On-demand dog walking by subscription | ✅ | ✅ | Homejoy (model, mechanism), Shyp (model, mechanism) |
| 2 | Healthy meal kits by subscription | ❌ 1 | ✅ | Munchery (market, model), Blue Apron (market, model) |
| 3 | Online marketplace for private tutors | ❌ 0 | ✅ | Preply (market, model), Varsity Tutors (market, model) |
| 4 | AI app that files freelancers' tax returns | ❌ 0 | ✅ | Taxfix (market, model), TurboTax (market, model) |
| 5 | Social network for pet owners | ❌ 0 | ❌ | Only loose matches on one dimension |
| 6 | AR glasses for cyclists | ❌ 0 | ✅ | Recon Jet (market, model), Google Glass (model, mechanism) |
| 7 | B2B shift scheduling for restaurants | ❌ 0 | ✅ | 7shifts (market, model), Homebase (market, model) |
| 8 | Flexible coworking in mid-sized cities | ❌ 0 | ✅ | WeWork (market, model), IWG (market, model) |
| 9 | AI-powered escape rooms | ❌ 0 | ❌ | No precedent matching two dimensions |
| 10 | App matching older people with companionship volunteers | ❌ 1 | ⚠️ borderline | Papa (market, model), Homejoy (model, mechanism) |

**Result:** 8/10 pass with research (7 clear + 1 borderline) → **go**, above the 6/10 bar. With the library alone, only **1/10** passes.

## What this tells us

1. **Idea mode works, but it leans on live research, not on the library.** The library is built from plan-stage failures (delivery, scooters, fintech) and has almost nothing for the categories founders bring most: consumer apps, edtech, SMB SaaS, coworking, wearables.
2. **Mechanism is the missing dimension.** In 8 of 10 ideas the matches came from market + model, because a bare idea has no mechanism yet. That supports the "decompose the idea into its 3 bets first" step (who pays, how they find you, what each customer costs).
3. **Consumer social and experience ideas (5, 9) don't get precedents.** For those, idea mode should say so plainly and fall back to the generic failure causes instead of forcing matches.

## Caveats

- Not blind: the same model wrote the ideas, ran the matching and judged it. Treat as a feasibility check, not an eval.
- Precedent facts for the non-library cases come from general knowledge and still need sourcing before they are added to the library.
- Small sample (10).

## Next steps

- Add an "idea mode" section to `SKILL.md` (decompose into 3 bets → precedents per bet → verdict first).
- Add ~10 idea-stage precedents with sources: WeWork, Blue Apron, Recon Jet, Google Glass, Preply, Taxfix, 7shifts and similar.
