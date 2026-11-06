# Logic Fallacy Audit Skill

Logic Fallacy Audit turns a passage into a structured argument review: claims, evidence, hidden premises, inferential breaks, confidence, and a repaired version of the argument.

The project is designed for Chinese and English argument analysis, debate preparation, editing, media literacy, and critical-thinking teaching. It is not a fact-checking oracle and does not infer a speaker's motives from a reasoning error.

## What it does

- Reconstructs the strongest charitable version of an argument.
- Separates deductive validity, evidential support, dialectical fairness, and rhetorical pressure.
- Matches reasoning defects to a structured, maintainable fallacy catalog.
- Requires quoted evidence, confidence labels, counterexamples, and false-positive boundaries.
- Produces quick, full, debate, or teaching reports.

## Install for Codex

```bash
git clone https://github.com/kael-odin/logic-fallacy-audit.git "${CODEX_HOME:-$HOME/.codex}/skills/logic-fallacy-audit"
```

See [README.md](README.md) for the Chinese-first documentation, architecture, validation commands, and project boundaries.

## Validation

```bash
python scripts/fallacy_cli.py validate --strict
python -m unittest discover -s tests -v
python scripts/fallacy_cli.py render --check
```

## License

MIT
