# Contributing to Been There

Thanks for helping. The most valuable contributions are small and factual.

## 1. Add a precedent (best first contribution)

A precedent is one company, in one YAML file, that faced a trap and either died of it or survived it.

1. Copy an existing file in [`been-there/precedents/`](been-there/precedents/) (e.g. `webvan.yaml`) and rename it `<company-slug>.yaml`.
2. Fill in the fields described in [`precedents/SCHEMA.md`](been-there/precedents/SCHEMA.md). Use 1–3 cause tags from the list.
3. Add **at least one source** with a URL. Founder post-mortems are best, then reputable news. AI-generated summaries don't count as the only source.
4. Set `status: verified` only if every fact in the entry is backed by a source.
5. Open a pull request. The CI check validates the YAML automatically.

Most wanted: **survivors** (companies that beat a trap that killed others), **European and Spanish cases**, and **regulatory failures** (GDPR, health, fintech).

## 2. Add an eval case

Eval cases keep the skill honest. Add one to `evals/cases-v3.yaml` (fictional) or `evals/cases-v2.yaml` (real, disguised):

- The fatal flaw must be **derivable from the prompt** but never stated as a problem.
- Include `expected`: what a good answer should catch.
- Controls (good plans that look risky) are just as useful as traps.

## 3. Improve the skill

Changes to `SKILL.md` should come with evidence: run the affected eval cases before and after (see [`evals/RUBRIC.md`](evals/RUBRIC.md)) and paste the result in the PR.

## 4. Translate

The skill answers in the user's language. Trigger phrases and README sections in more languages are welcome.

## Ground rules

- Facts over opinions; sources over memory.
- Be kind in reviews. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
- By contributing you agree your code is MIT-licensed and your precedent entries CC BY 4.0.
