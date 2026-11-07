---
name: logic-fallacy-audit
description: Analyze Chinese or English passages for logical fallacies, hidden premises, weak evidence, dialectical moves, and manipulative rhetoric, then produce an evidence-grounded report with confidence and false-positive boundaries. Use for argument analysis and debate critique, not for declaring whether a factual claim is true without evidence.
license: MIT
metadata:
  version: "1.4.0"
  language: "zh-CN"
---

# Logic Fallacy Audit

Turn a passage into a careful argument analysis. Identify the argument before naming a fallacy. Quote the exact evidence. Separate logical failure from factual disagreement, rhetorical style, speaker intent, and cognitive bias.

## Start Here

1. Read [references/analysis-protocol.md](references/analysis-protocol.md).
2. Read [references/taxonomy.md](references/taxonomy.md) to classify the reasoning task.
3. Read [references/report-spec.md](references/report-spec.md).
4. Read [references/false-positive-guards.md](references/false-positive-guards.md).
5. Read only the catalog files relevant to the passage from [references/catalog-index.md](references/catalog-index.md).
6. When the passage relies on Chinese idioms, internet phrases, or debate one-liners, also read [references/chinese-patterns.md](references/chinese-patterns.md).
7. For long files, subtitles, or multi-paragraph sources, read [references/long-text-workflow.md](references/long-text-workflow.md).
8. For English reports, use [assets/report-template.en.md](assets/report-template.en.md) and [references/glossary.md](references/glossary.md).
9. For teaching output, read [references/teaching-mode.md](references/teaching-mode.md).
10. For argument graphs or before/after comparison, read [references/visualization.md](references/visualization.md).
11. For the ten most common entry points, use [references/core-fallacies.md](references/core-fallacies.md).

Available modes:

- `quick`: a short diagnosis for one claim or a short exchange.
- `full`: the default report for multi-paragraph text.
- `debate`: a reply-ready analysis that also states what evidence would change the judgment.
- `teaching`: explains the reasoning slowly with examples and exercises.

If the user does not name a mode, choose `quick` for fewer than 250 Chinese characters and `full` otherwise.

If `full` is requested for a text with fewer than 250 Chinese characters or only one argument unit, limit the report to at most four primary findings. Merge labels that describe the same inferential break. Mention secondary labels under `相关但不主判`.

## Analyze in This Order

Do not begin with a list of fallacy names. Complete these steps first:

1. Preserve the source. Mark quoted text, paraphrase, and missing context separately.
2. Extract explicit claims, conclusions, evidence, and normative judgments.
3. Reconstruct the most charitable argument. Add only unstated premises needed to make the argument coherent.
4. Classify the reasoning task: deductive, inductive, causal, statistical, explanatory, definitional, normative, or policy.
5. Test the argument on the standards for that task.
6. Only then match the failure to catalog entries.
7. Run a counterfactual: state what added evidence or context would make the move reasonable.
8. Assign confidence and decide whether the issue is a fallacy, a weaker argumentative move, a rhetorical pattern, or not a logical problem.

## Four Separate Questions

Evaluate these independently:

| Layer | Question | Typical output |
|---|---|---|
| Formal | If the premises are true, must the conclusion follow? | Valid, invalid, or not a deductive argument |
| Evidential | How much support do the premises give the conclusion? | Strong, moderate, weak, or unevaluable |
| Dialectical | Does the move meet the burden of proof and rules of fair exchange? | Adequate, evasive, circular, or burden-shifting |
| Rhetorical | Does the language invite a conclusion that the evidence does not establish? | Neutral, suggestive, coercive, or manipulative |

A passage can fail at one layer and succeed at another. Do not collapse the four layers into a single "fallacy score".

## Finding Labels

Use these labels exactly:

- `确认`: the quoted structure clearly instantiates the pattern.
- `较可能`: the pattern is present, but missing context could change the judgment.
- `语境相关`: the move is fallacious only under stated conditions.
- `不构成谬误`: the move is valid, relevant, or merely a stylistic choice.

Use confidence as `高 / 中 / 低`. Explain the reason for the confidence. Never imply mathematical certainty from a text-only analysis.

## Required Report Shape

Every substantive analysis must include:

1. `## 结论摘要`: 2–4 sentences with the central logical weakness.
2. `## 论证地图`: conclusion, premises, hidden assumptions, and argument type.
3. `## 关键问题`: cards or a table sorted by importance.
4. `## 反向检验`: strongest version, counterexample, and alternative interpretation.
5. `## 改写建议`: revised argument with missing evidence made explicit.
6. `## 边界说明`: what the analysis cannot establish.

For each issue, include:

- exact excerpt;
- `确认 / 较可能 / 语境相关 / 不构成谬误`;
- fallacy or pattern name;
- reasoning mechanism, not just a label;
- why the conclusion does not yet follow;
- confidence and what would raise or lower it.

Use [assets/report-template.md](assets/report-template.md) for Chinese `full` and `debate` output. Use [assets/report-template.en.md](assets/report-template.en.md) for English output. The headings and field names in either template are accepted by the report linter.

If you save the report as a Markdown file in this repository, validate it:

```bash
python scripts/report_lint.py path/to/report.md --profile full --strict
```

For a saved long source, generate stable locations before writing findings:

```bash
python scripts/fallacy_cli.py segment path/to/source.txt --json
python scripts/fallacy_cli.py locate path/to/source.txt --quote "exact excerpt"
```

Cite located excerpts as `[L12-L14] "exact text"` and record the source SHA-256 in the report metadata.

For a saved report, generate Mermaid diagrams:

```bash
python scripts/fallacy_cli.py diagram path/to/report.md --kind argument
python scripts/fallacy_cli.py diagram path/to/report.md --kind issues
python scripts/fallacy_cli.py diagram path/to/report.md --kind compare
```

## Non-Negotiable Constraints

- Do not infer motive, mental illness, identity, or moral character from a logical flaw.
- Do not call a claim false because its argument is weak. A bad argument can support a true conclusion.
- Do not call disagreement with a conclusion a fallacy.
- Do not use a formal fallacy label unless the passage contains a deductive inference.
- Do not treat correlation, anecdote, tradition, authority, emotion, or popularity as automatically invalid. Test relevance and sufficiency.
- Do not count one sentence as several independent fallacies just because several labels could fit.
- Do not use "cognitive bias" and "logical fallacy" as synonyms. Bias is a tendency; a fallacy is a defect in reasoning or argumentation.
- Do not diagnose manipulation from vocabulary alone. Identify the mechanism and the conversational effect.
- Treat rhetorical questions and idioms as speech acts first. If they are merely expressive or elliptical, do not rewrite them as full factual claims. If they carry an inference, quote them, mark the reconstruction, and then evaluate that inference.
- When the passage is satire, fiction, reported speech, or a hypothetical, analyze it as such.
- When context is missing, lower confidence and state the exact missing information.

## Query the Catalog

Use the bundled CLI when a fast lookup helps:

```bash
python scripts/fallacy_cli.py search "稻草人"
python scripts/fallacy_cli.py show straw-man
python scripts/fallacy_cli.py categories
```

If the CLI cannot run, read the relevant generated category file under `references/catalog/`.

## Additional References

- [references/taxonomy.md](references/taxonomy.md): classification and overlap rules.
- [references/core-fallacies.md](references/core-fallacies.md): ten high-frequency fallacies with boundaries.
- [references/logic-basics.md](references/logic-basics.md): validity, conditionals, quantifiers, induction, probability, and norms.
- [references/task-matrix.md](references/task-matrix.md): choose the correct evaluation route by reasoning task.
- [references/argument-reconstruction.md](references/argument-reconstruction.md): how to expose hidden premises without inventing them.
- [references/evidence-and-confidence.md](references/evidence-and-confidence.md): confidence calibration.
- [references/long-text-workflow.md](references/long-text-workflow.md): source segmentation, line locations, and clean-input boundaries.
- [references/glossary.md](references/glossary.md): fixed Chinese-English terms for report sections, labels, and reasoning types.
- [references/teaching-mode.md](references/teaching-mode.md): lesson flow, difficulty levels, answer keys, and feedback.
- [references/visualization.md](references/visualization.md): Mermaid argument, issue, and before/after diagrams.
- [evals/rubrics/README.md](evals/rubrics/README.md): specialized policy, statistics, and long-dialogue rubrics.
- [evals/model-runs/README.md](evals/model-runs/README.md): real model-run recording and fixture/model separation.
- [references/report-lint.md](references/report-lint.md): automatically check report structure.
- [references/explainer-style.md](references/explainer-style.md): clear explainer structure inspired by short critical-thinking videos.
- [references/research-sources.md](references/research-sources.md): source basis and citation policy.
- [references/adjacent-biases.md](references/adjacent-biases.md): cognitive biases that are not automatically fallacies.
