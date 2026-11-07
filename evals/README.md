# 行为评测

`cases.jsonl` 是 Skill 的人工/模型评测集，不是传统单元测试。自动化脚本只校验格式、目录 ID 和必需字段；推理质量仍需按 [rubric.md](rubric.md) 评审。

## 运行方式

1. 把一条 `input` 原样交给已加载 `$logic-fallacy-audit` 的模型。
2. 要求模型按 `mode` 输出报告。
3. 检查是否覆盖 `must_detect`，是否合理处理 `may_detect`。
4. 检查是否出现 `must_not_assert` 中禁止的高确定性断言。
5. 把完整报告保存为临时 Markdown，运行 `python scripts/report_lint.py <report.md> --profile <mode> --strict`。
6. 按通用 [rubric.md](rubric.md) 评分；政策、统计和长对话案例再按 [专项评分表](rubrics/README.md) 复核。

`must_detect` 表示当前文本中可稳定识别的主要问题，不要求逐字使用某个标签，但报告必须描述同一推理机制。

## 回归原则

- 新增误报、虚构事实或动机诊断案例时，应加入评测。
- 不要用固定标题和措辞做文本字符串测试。
- 模型表现变化时，保存输入、输出、模型与日期。
- 评测输入应短小、原创、可公开，不包含真实隐私或攻击性个人信息。
- 新发现的误报或校验缺陷登记到 [regressions.jsonl](regressions.jsonl)，看板由脚本生成。
