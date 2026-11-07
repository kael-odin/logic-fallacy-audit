# v1.2 报告验收与行为审查

## 审查范围

- Markdown 报告校验器的章节、引用、判定、置信度、影响、边界、替代解释和修复条件。
- Full、Debate、Quick 与 Teaching 分析模式的报告兼容性。
- 行为评测的格式、条目引用、模式覆盖、负样本和长文输入。
- CLI、CI、版本元数据、README 链接和生成目录一致性。
- 模板占位符、未完成标记与失效相对链接的失败路径。

## 结论

v1.2 增加确定性报告结构门禁，并将行为评测从 17 条扩展到 33 条。报告校验不能判断分析是否聪明，但能阻止缺少原文证据、置信度、边界或修复条件的报告进入发布流程。

本版本没有新增谬误条目。知识库仍为 240 条结构化条目：208 条谬误或论证模式，32 条相邻认知偏差。

## 主要变更

| 范围 | 变更 | 验收方式 |
|---|---|---|
| 报告校验 | 新增 `scripts/report_lint.py` | 六个必需章节、问题卡字段和引用检查 |
| CLI | 新增 `lint-report` 子命令 | 单元测试与样例报告门禁 |
| Full / Debate | 要求论证地图、问题卡、反向检验和改写证据 | `--profile full --strict` |
| Quick | 保留核心章节、原文引用、判定标签和置信度 | `--profile quick --strict` |
| Teaching | 使用最小结构规则，允许讲解与练习扩展 | `--profile teaching --strict` |
| 评测 | 从 17 条扩展到 33 条 | 数量门槛提升至 30，四种模式全部覆盖 |
| CI | 独立 lint job 校验样例报告 | GitHub Actions |
| 文档 | 增加报告校验规范和本审查记录 | 严格相对链接检查 |

## 行为评测覆盖

当前 33 条评测的分布如下：

| 模式 | 数量 | 重点 |
|---|---:|---|
| Full | 21 | 多段论述、因果、统计、政策、修辞与解释 |
| Quick | 9 | 短句、混合语言与单一推理断点 |
| Debate | 2 | 对话责任、稻草人与证据转换条件 |
| Teaching | 1 | 个案证据、因果替代解释与教学讲解 |

新增案例覆盖：

- 中英混杂的技术论证；
- 多轮对话中的稻草人和责任转移；
- 有效专家意见、风险预防与统计相关等负样本；
- `must_not_assert` 中的人格、动机和事实越界；
- 长文输入中的主问题收敛。

## 自动验收

本地发布门禁包括：

```bash
python scripts/fallacy_cli.py validate --strict
python scripts/fallacy_cli.py render --check
python scripts/report_lint.py examples/sample-report.md --profile full --strict
ruff check scripts tests
ruff format --check scripts tests
python -W error -m unittest discover -s tests -v
```

35 项测试覆盖目录 schema、别名冲突、生成文件漂移、链接、版本、CLI、报告字段、四模式评测覆盖和模板占位符。

## 失败路径

校验器会拒绝以下报告：

- 缺少六个核心章节；
- 引用、判定、置信度或影响等级缺失；
- Full / Debate 问题卡缺少边界、相关但不主判或修复条件；
- 论证地图没有说明隐含前提的重建依据；
- 反向检验缺少最强版本、关键测试或替代解释；
- 改写建议没有可直接引用的段落；
- 正文残留模板占位符、`TODO`、`FIXME` 或“待补充”。

## 边界

- 结构完整不等于判断正确。谬误匹配、事实状态和反例质量仍需人工 rubric。
- 报告校验器不联网核验事实，也不评估来源可信度。
- 当前评测集是质量回归样本，不代表对所有领域、文体和模型的无偏覆盖。
- Teaching 目前只有一条行为评测，后续仍需增加练习生成、难度分层和答案一致性评测。
