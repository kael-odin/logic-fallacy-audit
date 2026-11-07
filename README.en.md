# Logic Fallacy Audit Skill

Logic Fallacy Audit turns a passage into a structured argument review: claims, evidence, hidden premises, inferential breaks, confidence, and a repaired version of the argument.

The project is designed for Chinese and English argument analysis, debate preparation, editing, media literacy, and critical-thinking teaching. It is not a fact-checking oracle and does not infer a speaker's motives from a reasoning error.

Latest tagged release: `1.2.0`. The current `main` branch contains 250 structured entries: 218 fallacies or argument patterns and 32 adjacent cognitive biases.

## What it does

- Reconstructs the strongest charitable version of an argument.
- Separates deductive validity, evidential support, dialectical fairness, and rhetorical pressure.
- Matches reasoning defects to a structured, maintainable fallacy catalog.
- Requires quoted evidence, confidence labels, counterexamples, and false-positive boundaries.
- Creates deterministic source maps with line spans, SHA-256, and exact quote locations.
- Produces quick, full, debate, or teaching reports.

## Install for Codex

```bash
git clone https://github.com/kael-odin/logic-fallacy-audit.git "${CODEX_HOME:-$HOME/.codex}/skills/logic-fallacy-audit"
```

See [README.md](README.md) for the Chinese-first documentation, architecture, validation commands, and project boundaries.

## Validation

```bash
python scripts/fallacy_cli.py validate --strict
python scripts/report_lint.py examples/sample-report.md --profile full --strict
python scripts/fallacy_cli.py segment examples/long-text-source.txt --json
python scripts/fallacy_cli.py locate examples/long-text-source.txt --quote "三个人的经历"
python -m unittest discover -s tests -v
python scripts/fallacy_cli.py render --check
```

## License

MIT
