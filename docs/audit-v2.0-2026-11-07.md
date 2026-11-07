# v2.0 解说模式与知识覆盖审查

## 审查范围

- `explainer` 模式的入口、模板、完整样例、专项评分表和回归案例。
- 260 条结构化目录的定义、推理式、诊断问题、例子、误判边界、混淆项、关联项和别名。
- 用户指定的十类核心谬误深度分析卡。
- 外部名称差异扫描后的十项新增机制与已有条目别名补强。
- Skill、报告校验、评测校验、CLI、README、Citation、Changelog 与 CI 的版本一致性。
- v1.5 已完成事项与真实模型运行缺口的区分。

## 结论

v2.0 增加的是“同一证据标准下的另一种表达方式”，不是降低严谨度换取视频感。`explainer` 与 `full` 复用同一组必需章节和问题卡字段，只增加七拍表达节奏、专项 rubric 和解说样例。

知识覆盖由 `python scripts/fallacy_cli.py coverage` 从 `catalog/` 直接生成。当前 260 条全部具备定义、推理式、至少两个诊断问题、非空例子、误判边界、至少一个混淆项、至少一个关联条目和至少一个检索别名。原创性由人工内容审查，不由结构脚本证明。这个结果证明结构完整，不证明所有学派都已覆盖，也不证明每一个定义永远无需修订。

## Explainer 设计

七拍结构：

1. 用承担真实推理功能的原句进入。
2. 中性重述表面主张。
3. 一次揭示一个隐藏前提。
4. 说明推理连接在哪里断开。
5. 用只改变关键变量的最小反例测试。
6. 给出最强反方解释和可能不是谬误的边界。
7. 用更窄、更可检验的版本收束。

新增文件：

- `assets/report-template.explainer.md`
- `examples/explainer-report.md`
- `references/explainer-style.md`
- `evals/rubrics/explainer.md`
- `eval-048-explainer-ai-jobs`
- `eval-049-explainer-school-phones`
- `eval-050` 至 `eval-059`：新增机制回归覆盖

## 知识覆盖

自动审计维度：

| 维度 | 结果 |
|---|---:|
| 结构化条目 | 260/260 |
| 谬误或论证模式 | 228 |
| 相邻认知偏差 | 32 |
| 主分类 | 10 |
| 每条至少 2 个诊断问题 | 260/260 |
| 每条有非空例子（原创性人工复核） | 260/260 |
| 每条有误判边界 | 260/260 |
| 每条有关联条目 | 260/260 |
| 每条有检索别名 | 260/260 |

完整机器生成表见 `references/knowledge-coverage.md`。

## 核心十类

`references/core-fallacies.md` 保留速查表，并增加十张深度卡。每张卡包含：

- 一句话机制；
- 三步结构测试；
- 最小反例；
- 合理边界或可能不是谬误的条件；
- 常见混淆；
- 可直接使用的报告句式。

## 验证命令

```bash
python scripts/fallacy_cli.py validate --strict
python scripts/fallacy_cli.py render --check
python scripts/fallacy_cli.py coverage --json
python scripts/report_lint.py examples/sample-report.md --profile full --strict
python scripts/report_lint.py examples/explainer-report.md --profile explainer --strict
python scripts/report_lint.py examples/teaching-report.md --profile teaching --strict
python -m unittest discover -s tests -v
ruff check scripts tests
ruff format --check scripts tests
```

发布前本地结果：

- `validate --strict`：0 错误、0 警告。
- `render --check`：生成文件无漂移。
- `coverage --json`：260 条、10 类、核心十类 10/10。
- `unittest`：83 项通过。
- 行为评测：59 条，五种模式均有样本。
- `ruff check` 与 `ruff format --check`：通过。
- 中文 Full、英文 Full、Teaching、Explainer 样例报告：0 错误。
- 回归看板与模型运行看板：与账本一致。

## 边界

- 真实模型运行仍需在 `evals/model-runs/ledger.jsonl` 中记录；curated fixture 不得冒充模型成绩。
- 目录扩充来自公开名称差异扫描；条目边界和例子仍按本项目标准重写。
- `explainer` 不复制 B 站 UP 主的逐字稿、画面、口头禅或独有分类。
- 覆盖审计统计的是结构字段，不测量定义争议、专业事实或报告聪明程度。
- 任何新增条目仍必须通过目录校验、生成漂移、链接、评测引用和完整测试。
