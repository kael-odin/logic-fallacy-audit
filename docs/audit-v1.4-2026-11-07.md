# v1.4 教学与可视化审查

## 审查范围

- 从 Markdown 报告生成 Mermaid 论证图。
- 问题关系图与修复前后对照图。
- Teaching 模式规范、练习与标准答案。
- 中文逻辑写作改写示例。
- CLI、CI、文档、测试与版本元数据。

## 结论

v1.4 将教学与可视化落实为可运行资产。`diagram` 命令可以读取中文或英文报告，生成 `argument`、`issues` 与 `compare` 三种 Mermaid 图。

教学模式增加六步讲解节奏、四档难度、答案结构和正式报告兼容说明。练习库提供 10 道带隐藏答案的题目，改写库提供 6 组前后对照。

## 主要变更

| 范围 | 变更 |
|---|---|
| 论证图 | 结论、显式前提和隐含前提 |
| 问题图 | 问题卡与主论证的审查关系 |
| 对照图 | Before、Issues、After 三段结构 |
| CLI | `diagram --kind argument/issues/compare` |
| Teaching | 分步讲解、难度层级、反馈顺序 |
| 练习 | 10 道题与可展开答案 |
| 改写 | 6 组中文原句与修复版本 |
| CI | 教学模式报告与 Mermaid 生成门禁 |

## 图表语义

- 实线表示报告声明的支持方向。
- `assumption` 表示重建的隐含前提。
- `affects` 表示问题影响主论证，不声称精确绑定某个前提。
- `repair` 表示问题指向改写方向。
- 图不替代原文引用、事实核验或人工 rubric。

## 验证要求

```bash
python scripts/fallacy_cli.py validate --strict
python scripts/fallacy_cli.py diagram examples/sample-report.md --kind compare
python scripts/report_lint.py examples/teaching-report.md --profile teaching --strict
ruff check scripts tests
ruff format --check scripts tests
python -W error -m unittest discover -s tests -v
```

自动测试检查练习数量、隐藏答案、主判 ID 有效性、改写数量、教学报告结构、中文和英文图表渲染及 CLI JSON 输出。

当前完整测试为 65 项；远程 CI 在发布提交后核验。

## 边界

- 生成器不推断问题精确攻击哪一条前提。
- Mermaid 在不同渲染器中的布局可能不同。
- 教学模式不把答题表现转化为人格或能力诊断。
- 练习覆盖常见机制，不代表完整题库。
