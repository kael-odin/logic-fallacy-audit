# 误报与回归看板

> 本文件由 `python scripts/regression_dashboard.py` 生成。请修改 `evals/regressions.jsonl`。

## 总览

| 状态 | 数量 |
|---|---:|
| 仍存在 | 3 |
| 已修复 | 9 |
| 已失效 | 0 |
| 边界变化 | 0 |

| Open 严重度 | 数量 |
|---|---:|
| high | 0 |
| medium | 3 |
| low | 0 |

## 仍存在

| ID | 严重度 | 类别 | 问题 | 解析版本 | 关联评测 | 证据 |
|---|---|---|---|---|---|---|
| `irony-and-reported-speech-eval-gap` | medium | evaluation | 尚缺反讽、引用与转述同时出现的长对话回归样本 | - | 无 | `docs/content-backlog.md` |
| `multi-argument-unit-eval-gap` | medium | evaluation | 尚缺同一输入包含多个独立论证单元的回归样本 | - | 无 | `docs/content-backlog.md` |
| `real-model-run-coverage` | medium | evaluation | 当前运行账本只有 curated fixture，尚缺真实模型的多种提示词版本结果 | - | `eval-044-workplace-generalization`、`eval-045-supplement-anecdote` | `docs/model-run-dashboard.md` |

## 已修复

| ID | 严重度 | 类别 | 问题 | 解析版本 | 关联评测 | 证据 |
|---|---|---|---|---|---|---|
| `citation-range-unchecked` | high | citation | 报告中的 Lx-Ly 可能越界或指向错误原文 | `v1.3.0` | `eval-031-long-dialogue-straw` | `tests/test_report_lint.py::test_out_of_range_source_location_is_reported`<br>`tests/test_report_lint.py::test_wrong_cited_text_is_reported` |
| `empty-report-field-pass` | high | report | 问题卡只有粗体字段名而没有内容也能通过 | `v1.2.0` | 无 | `tests/test_report_lint.py::test_empty_issue_field_is_reported` |
| `english-section-alias-missed` | high | report | 英文章节已解析但存在性预检查仍只匹配中文 | `v1.3.0` | `eval-030-mixed-formal` | `tests/test_report_lint.py::test_english_sample_passes_with_source_locations`<br>`examples/sample-report.en.md` |
| `eval-mode-type-crash` | high | evaluation | 非字符串 mode 会触发不可哈希类型异常 | `v1.2.0` | 无 | `tests/test_catalog.py::test_invalid_eval_value_types_do_not_crash` |
| `missing-entry-id-crash` | high | catalog | 缺失 ID 的条目会让目录校验路径崩溃 | `v1.1.0` | 无 | `tests/test_catalog.py::test_missing_id_reports_error_without_crashing` |
| `model-run-ledger-gap` | high | evaluation | 尚未建立不同模型、日期和提示词版本的运行账本 | `unreleased-v1.5` | `eval-044-workplace-generalization`、`eval-045-supplement-anecdote` | `scripts/eval_runner.py`<br>`evals/model-runs/ledger.jsonl`<br>`docs/model-run-dashboard.md`<br>`tests/test_eval_runner.py` |
| `contextomy-duplicate` | medium | content | contextomy 与 quote-mining 重复描述同一机制 | `v1.1.0` | `eval-024-legal-quote` | `tests/test_catalog.py::test_duplicate_context_is_merged`<br>`references/catalog/04-ambiguity.md` |
| `duplicate-report-section-overwrite` | medium | report | 重复必需章节会覆盖前一章节而不报错 | `v1.2.0` | 无 | `tests/test_report_lint.py::test_duplicate_required_section_is_reported` |
| `stale-generated-catalog` | medium | docs | 旧生成分类文件不会被检测或清理 | `v1.1.0` | 无 | `tests/test_docs.py::test_stale_generated_file_is_detected_and_removed` |

## 已失效

| ID | 严重度 | 类别 | 问题 | 解析版本 | 关联评测 | 证据 |
|---|---|---|---|---|---|---|
| - | - | - | 当前没有记录 | - | - | - |

## 边界变化

| ID | 严重度 | 类别 | 问题 | 解析版本 | 关联评测 | 证据 |
|---|---|---|---|---|---|---|
| - | - | - | 当前没有记录 | - | - | - |

## 使用规则

- 新发现的误报或校验缺陷先登记为 `open`。
- 修复后填写 `resolved_in` 和可复核证据。
- 如果问题被证明不是缺陷，改为 `invalidated`。
- 如果结论未变但适用边界改变，改为 `boundary`。
- fixed 记录不会删除，用于防止同类问题回归。
