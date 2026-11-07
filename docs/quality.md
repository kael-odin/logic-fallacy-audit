# 质量与验证

## 1. 自动检查

```bash
python scripts/fallacy_cli.py validate --strict
python scripts/fallacy_cli.py render --check
python scripts/fallacy_cli.py segment examples/long-text-source.txt --json
python scripts/fallacy_cli.py locate examples/long-text-source.txt --quote "三个人的经历"
python scripts/report_lint.py examples/sample-report.md --profile full --strict
python scripts/report_lint.py examples/sample-report.en.md --profile full --strict --source examples/long-text-source.txt --require-locators
python scripts/report_lint.py examples/teaching-report.md --profile teaching --strict
python scripts/fallacy_cli.py diagram examples/sample-report.md --kind compare
python scripts/fallacy_cli.py regression-dashboard --check
python scripts/eval_runner.py dashboard --check
ruff check scripts tests
ruff format --check scripts tests
python -m unittest discover -s tests -v
```

检查内容：

- TOML 可解析；
- 必需字段完整；
- ID 唯一且符合 kebab-case；
- 分类存在；
- 分类非空；
- 关联 ID 有效；
- 别名不与任何其他 ID、主名或别名冲突；
- 缺少 ID 时返回校验错误而不是崩溃；
- 核心十类存在；
- 条目覆盖达到门槛；
- SKILL frontmatter 与必要引用存在；
- 报告模板必需章节存在；
- 样例报告通过结构、引用、标签、置信度和边界字段校验；
- 英文样例通过双语字段和源文件行号核验；
- 教学报告、练习答案和 Mermaid 图表生成通过测试；
- 回归账本、专项 rubric 与误报看板通过测试和漂移检查；
- 模型运行账本区分 fixture 与真实模型，并检查运行看板漂移；
- 重复章节、空字段和未完成占位符会被拒绝；
- SKILL、CITATION 与 CHANGELOG 版本一致；
- 评测案例可解析且引用有效；
- 评测 mode 类型有效，且四种模式均有样本；
- 长文本候选块、SHA-256、行号与精确引文定位通过测试；
- Markdown 相对链接不失效；
- 生成目录无缺失、漂移或残留文件；
- CLI 和示例报告关键行为通过测试。
- Python 代码通过固定版本的 Ruff 静态检查。

## 2. 人工检查

自动检查无法判断分析是否聪明。发布前用 `evals/cases.jsonl` 走真实模型测试。

每份输出按 `evals/rubric.md` 看：

- 是否先重建论证；
- 是否准确引用；
- 是否解释机制；
- 是否给出最强反方解释；
- 是否避免动机推断；
- 是否说明什么证据会改变判断。

## 3. 新增条目的审查问题

1. 这个条目是否描述一个稳定、可复述的失败机制？
2. 它是否只是另一个条目的别名？
3. 例子是否原创且不会依赖具体政治争议？
4. 边界是否说明什么时候模式合理？
5. 诊断问题是否能帮助分析者查看原文？
6. 关联条目是否指向真实 ID？
7. 是否把认知偏差误放进谬误分类？

## 4. 误报回归

发现以下情况时，应新增评测：

- 因为语气强硬被判谬误；
- 因为结论令人反感被判论证无效；
- 合理的专家意见被一律判为诉诸权威；
- 有机制支持的连续风险被一律判为滑坡；
- 统计相关被要求证明绝对因果才可讨论；
- “没有满足不现实的证据标准”被误写成证据缺失；
- 认知偏差成为人格或动机指控。

## 5. 版本门槛

发布前必须：

- 目录校验通过；
- 生成文件无漂移；
- 单元测试通过；
- 至少 40 条行为评测案例存在；
- README 安装命令与仓库名一致；
- GitHub Actions 在支持版本上通过。
