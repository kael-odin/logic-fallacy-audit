# Changelog

All notable changes follow a simple milestone history.

## Unreleased

- No changes yet.

## 2.0.0 - 2026-11-07

- Added `explainer` as a fifth report mode with a dedicated template, complete sample, style guide, specialized rubric, and two regression cases.
- Added the seven-beat explainer flow: quote, surface claim, hidden premise, break, minimal counterexample, boundary, and testable repair.
- Expanded the catalog from 250 to 260 entries with accident, ambiguous-middle-term, exhaustive-effort, furtive, if-by-whiskey, inflation-of-conflict, nut-picking, pooh-pooh, referential, and psychologist's-fallacy mechanisms.
- Added common external-name aliases for existing entries, including argument-from-fallacy, argument-from-ignorance, false-authority, wrong-direction, Ipse Dixit, and Garden of Forking Paths.
- Added a generated knowledge-coverage audit that verifies all 260 entries have definitions, reasoning patterns, at least two diagnostic questions, examples, boundaries, confusions, related entries, and aliases.
- Expanded the ten requested core fallacies into deep analysis cards with structure tests, minimal counterexamples, legitimate boundaries, common confusions, and report-ready wording.
- Extended report linting and evaluation validation to include `explainer` while reusing the full evidence contract.
- Added a dedicated explainer rubric covering hook fidelity, charitable reconstruction, stepwise clarity, minimal counterexamples, boundary integrity, and separation of spoken and evidentiary layers.
- Completed the v1.5 evaluation-operations documentation and reconciled the roadmap, Skill metadata, Citation File Format, README, and release version.

## 1.5.0 - 2026-11-07

- Added a structured false-positive and regression ledger.
- Added a generated regression dashboard with open, fixed, invalidated, and boundary states.
- Added specialized rubrics for policy, statistics, and long-dialogue evaluation.
- Added CLI and CI checks for regression ledger validity and dashboard drift.
- Added a model-run ledger with explicit fixture/model separation and a generated run dashboard.
- Added reported-speech/irony and multi-argument-unit regression coverage.
- Closed the first v1.5 implementation batch while keeping real-model coverage as an explicit open item.

## 1.4.0 - 2026-11-07

- Added a report diagram generator for Mermaid argument, issue, and before/after views.
- Added `diagram` CLI support for Chinese and English Markdown reports.
- Added teaching-mode guidance, ten graded exercises with answers, and a complete teaching sample.
- Added six Chinese before/after rewrite examples.
- Added CI and unit-test coverage for teaching materials and diagram generation.

## 1.3.0 - 2026-11-07

- Aligned the report specification with every field enforced by the linter.
- Rejected duplicate report sections and empty problem-card or reverse-test fields.
- Hardened behavior-evaluation validation against invalid mode types and missing modes.
- Updated the content backlog to distinguish completed evaluation coverage from remaining candidates.
- Expanded the catalog from 240 to 250 entries with ten mechanism-level additions.
- Expanded behavior evaluations from 33 to 43 cases so every new entry has regression coverage.
- Added deterministic long-text source maps with paragraph blocks, line spans, and SHA-256.
- Added exact quote location and `Lx-y` citation guidance for saved sources.
- Added optional source-backed citation validation and required-locator mode.
- Added an English report template, complete English sample, and bilingual glossary.
- Extended report linting to accept both Chinese and English headings, fields, verdicts, and impact labels.
- Added CI checks for English reports with source-backed citation locations.

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
