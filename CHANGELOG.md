# Changelog

All notable changes follow a simple milestone history.

## Unreleased

- Aligned the report specification with every field enforced by the linter.
- Rejected duplicate report sections and empty problem-card or reverse-test fields.
- Hardened behavior-evaluation validation against invalid mode types and missing modes.
- Updated the content backlog to distinguish completed evaluation coverage from remaining candidates.
- Expanded the catalog from 240 to 250 entries with ten mechanism-level additions.
- Expanded behavior evaluations from 33 to 43 cases so every new entry has regression coverage.
- Added deterministic long-text source maps with paragraph blocks, line spans, and SHA-256.
- Added exact quote location and `Lx-y` citation guidance for saved sources.

## 1.2.0 - 2026-11-07

- Added a deterministic Markdown report linter with Full/Debate and Quick profiles.
- Added the `lint-report` CLI command and a report-lint reference guide.
- Expanded behavior evaluations from 17 to 33 cases, including all four modes, mixed-language, long-form, and negative inputs.
- Added report linter unit tests and a CI sample-report quality gate.
- Added a v1.2 behavior audit record.

## 1.1.0 - 2026-11-07

- Merged the duplicated `contextomy` entry into `quote-mining` and added synonym coverage.
- Added 20 common fallacies and argument patterns after an external coverage cross-check.
- Added global alias collision, empty category, and safe missing-ID validation.
- Hardened full-repository validation and evaluation parsing against malformed field types.
- Added Unicode NFKC normalization for aliases, name collisions, and CLI search.
- Added stale generated-file detection and automatic cleanup.
- Removed the hard-coded category numbering map.
- Added README coverage consistency and regression tests.
- Added Ruff linting, CI concurrency, and workflow timeout guards.
- Added structured issue templates and a maintained content backlog.
- Added five behavior-evaluation cases for the new fallacy patterns.
- Corrected the merged quote-mining boundary and masked-man related references.
- Published the 2026-11-07 content and repository audit record.

## 1.0.0 - 2026-11-06

- Added the installable `logic-fallacy-audit` skill.
- Added a structured, category-based fallacy and argument-pattern catalog.
- Added argument reconstruction, confidence, false-positive, and reporting protocols.
- Added a Chinese phrase-pattern guide and explainer style guide.
- Added a standard-library CLI, catalog renderer, validators, tests, examples, and CI.
- Added Chinese-first and English project documentation.
