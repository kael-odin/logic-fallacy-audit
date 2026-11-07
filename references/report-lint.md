# 报告结构校验

`scripts/report_lint.py` 检查 Markdown 逻辑分析报告是否包含可复核的结构。它不判断论证结论是否正确，也不能替代人工 rubric。

## 使用

```bash
python scripts/report_lint.py examples/sample-report.md --profile full --strict
python scripts/report_lint.py examples/explainer-report.md --profile explainer --strict
python scripts/fallacy_cli.py lint-report examples/sample-report.md --strict
python scripts/report_lint.py examples/sample-report.en.md --profile full --strict --source examples/long-text-source.txt --require-locators
```

## Full / Debate / Explainer 检查

- 六个必需章节：结论摘要、论证地图、关键问题、反向检验、改写建议、边界说明。
- 论证地图包含结论、显式前提、隐含前提、重建依据、推理类型和当前缺口。
- 每张问题卡包含原文、判定、机制、结论为何不成立、影响、边界、相关但不主判和修复条件。
- 字段必须有内容；只保留粗体标题不算通过。
- 问题卡有原文引用、判定标签和 `高 / 中 / 低` 置信度。
- 反向检验包含最强版本、关键测试、替代解释和可能误判。
- 改写建议包含可直接引用的改写段落。
- 边界说明包含至少一项明确限制。
- 必需章节不能重复出现后静默覆盖前文。
- 中文模板与英文模板的固定字段均可识别。

`explainer` 使用与 Full 相同的问题卡和数据门槛，额外允许 `## 解说节奏`、`## 口播层` 等展示章节。展示章节不能替代六个核心章节。

## Quick 检查

Quick 模式仍保留六个核心章节，并检查原文引用、判定标签和置信度。它不要求完整问题卡字段。

## Teaching 检查

Teaching 使用与 Quick 相同的最小结构规则。教学模式可以增加讲解步骤、例子和练习，但正式文件仍必须包含六个核心章节、原文引用、判定标签和置信度。

完整教学结构见 [teaching-mode.md](teaching-mode.md)，样例见 [teaching-report.md](../examples/teaching-report.md)。

## 源文件引用核验

提供 `--source` 时，校验器会检查：

- `[Lx-Ly]` 的行号是否为正；
- 结束行是否早于开始行；
- 结束行是否超过源文件行数；
- 单一位置且没有省略号的引文是否存在于对应行区间。

`--require-locators` 要求每个 Full / Debate / Explainer 问题卡和 Quick 报告至少有一个 `[Lx-Ly]`。

多位置引文当前只核验位置范围，不逐一匹配每段引文。包含省略号的压缩引用也不做全文精确匹配。

## 明确不检查

- 谬误标签是否真的最适合该论证。
- 事实是否真实或来源是否可靠。
- 反例是否足够有力。
- 改写是否改变作者原意。
- 语气是否适合特定受众。

这些仍需使用 `evals/rubric.md` 和人工判断。
