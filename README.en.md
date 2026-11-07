# Logic Fallacy Audit Skill

Logic Fallacy Audit turns a passage into a structured argument review: claims, evidence, hidden premises, inferential breaks, confidence, and a repaired version of the argument.

The project is designed for Chinese and English argument analysis, debate preparation, editing, media literacy, and critical-thinking teaching. It is not a fact-checking oracle and does not infer a speaker's motives from a reasoning error.

Current release: `1.4.0`. The catalog contains 250 structured entries: 218 fallacies or argument patterns and 32 adjacent cognitive biases.

## What it does

- Reconstructs the strongest charitable version of an argument.
- Separates deductive validity, evidential support, dialectical fairness, and rhetorical pressure.
- Matches reasoning defects to a structured, maintainable fallacy catalog.
- Requires quoted evidence, confidence labels, counterexamples, and false-positive boundaries.
- Creates deterministic source maps with line spans, SHA-256, and exact quote locations.
- Generates Mermaid argument maps, issue graphs, and before/after comparisons from reports.
- Includes teaching-mode guidance, graded exercises with answers, and Chinese rewrite examples.
- Includes specialized policy, statistics, and long-dialogue rubrics plus a generated regression dashboard.
- Includes a model-run ledger and dashboard that distinguish curated fixtures from real model runs.
- Produces quick, full, debate, or teaching reports.

## Install for Codex

```bash
git clone https://github.com/kael-odin/logic-fallacy-audit.git "${CODEX_HOME:-$HOME/.codex}/skills/logic-fallacy-audit"
```

See [README.md](README.md) for the Chinese-first documentation, architecture, validation commands, and project boundaries.

English reports can use [assets/report-template.en.md](assets/report-template.en.md). The bilingual terminology is fixed in [references/glossary.md](references/glossary.md).

## Validation

```bash
python scripts/fallacy_cli.py validate --strict
python scripts/report_lint.py examples/sample-report.md --profile full --strict
python scripts/fallacy_cli.py segment examples/long-text-source.txt --json
python scripts/fallacy_cli.py locate examples/long-text-source.txt --quote "三个人的经历"
python scripts/fallacy_cli.py diagram examples/sample-report.md --kind compare
python scripts/fallacy_cli.py regression-dashboard --check
python scripts/eval_runner.py dashboard --check
python -m unittest discover -s tests -v
python scripts/fallacy_cli.py render --check
```

## License

MIT
