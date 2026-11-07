# v2.0.1 稳健报告与审计证据修正

## 审查范围

- Full 报告在“未发现稳定谬误”时的合法输出。
- 知识覆盖审计对例子字段与原创性的证据边界。
- `coverage --json` 的机器可读字段。
- 目录搜索的标点、空格和连字符归一化。
- 评测标签检测对嵌套别名和中文短名称的处理。
- 新增样例、评测、CI、版本和文档链接。

## 发现与修复

| 发现 | 风险 | 修复 |
|---|---|---|
| `不构成谬误` 卡片没有合适的影响等级 | 报告会为了通过校验被写成虚假缺陷 | 增加 `无 / None` 影响等级 |
| 覆盖审计把“非空例子”写成“已证明原创” | 自动化证据被过度表述 | 区分结构校验与人工原创审查 |
| 搜索不统一处理连字符和空格 | 外部英文名称难以找到 | 统一 NFKC、大小写、空格和标点 |
| 评测器用子串检测标签 | 长名称可能重复命中短别名 | 抑制同一文本区间内被长名称包含的短命中 |
| 缺少无谬误的 Full 完整样例 | 质量门槛无法证明“不制造问题” | 增加稳健统计文本报告和对应评测 |

## 新增产物

- `examples/valid-argument-report.md`
- `eval-060-full-valid-argument`
- `assets/report-template.md` 与覆盖审计中的 `无` 影响说明
- `coverage --json` 的 `field_checks`、`complete_entries` 和 `example_originality_verified`

## 验证命令

```bash
python scripts/fallacy_cli.py validate --strict
python scripts/fallacy_cli.py render --check
python scripts/fallacy_cli.py coverage --json
python scripts/report_lint.py examples/valid-argument-report.md --profile full --strict
python -m unittest discover -s tests -v
ruff check scripts tests
ruff format --check scripts tests
```

发布前本地结果：

- `validate --strict`：0 错误、0 警告。
- `render --check`：生成文件无漂移。
- `coverage --json`：260 条、228 个谬误模式、260 个结构完整条目。
- `unittest`：87 项通过。
- 行为评测：60 条，五种模式均有样本。
- curated fixture：3/3 通过，其中 `eval-060-full-valid-argument` 已通过。
- Full、Explainer、English Full、Teaching 和稳健论证样例：0 错误。

## 边界

- 原创例子仍需要人工审查；结构脚本只能证明字段非空。
- `无` 影响等级只用于经复核的 `不构成谬误` 卡片，不表示外部事实已经核验。
- 新增 Full 样例不代表所有稳健论证都能自动通过；语义质量仍需人工 rubric。
