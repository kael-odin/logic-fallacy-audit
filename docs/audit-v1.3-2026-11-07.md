# v1.3 输入工作流与双语报告审查

## 审查范围

- 250 条知识库的发布状态与生成目录。
- 长文本候选块、字符范围、行号与 SHA-256。
- 精确引文定位和报告 `[Lx-Ly]` 引用核验。
- 中英文报告章节、字段、判定标签与影响等级。
- 英文模板、英文样例和双语术语表。
- CI 在 Python 3.11、3.12、3.13 上的兼容性。

## 结论

v1.3 完成输入工作流的首个稳定版本。长文本现在可以生成确定性源文件映射，报告可以选用行号引用，校验器可以检查行号越界和引文文本是否落在声明范围内。

报告校验同时接受中文模板和英文模板的固定字段，不要求两套独立校验器。

## 主要变更

| 范围 | 变更 |
|---|---|
| 源文本 | `segment` 输出候选块、字符范围、行号和 SHA-256 |
| 引文 | `locate` 返回多行、全部及重叠精确匹配 |
| 报告引用 | 支持 `[L12-L14]` 并核验源文件行数 |
| 引用内容 | 单一位置且无省略号时，核验引文文本存在于对应行区间 |
| 双语报告 | 中文与英文标题、字段、判定和影响标签均可校验 |
| 英文资产 | 增加英文报告模板、英文样例和中英术语表 |
| CI | 增加长文本命令、中文样例、英文样例与引用位置检查 |

## 设计边界

- 候选块不是自动论证单元。
- 精确引文查找不会自动修正错字、合并空白或猜测近义文本。
- 多位置引文目前核验格式和行号范围；单位置引文才进一步核验文本落点。
- 行号对应规范化后的源文本，源文件改变后必须刷新 SHA-256 和引用。
- 报告结构通过不等于逻辑判断正确；谬误匹配仍需人工 rubric。

## 验证要求

发布前必须通过：

```bash
python scripts/fallacy_cli.py validate --strict
python scripts/fallacy_cli.py render --check
python scripts/fallacy_cli.py segment examples/long-text-source.txt --max-chars 80 --json
python scripts/fallacy_cli.py locate examples/long-text-source.txt --quote "三个人的经历" --json
python scripts/report_lint.py examples/sample-report.md --profile full --strict
python scripts/report_lint.py examples/sample-report.en.md --profile full --strict --source examples/long-text-source.txt --require-locators
ruff check scripts tests
ruff format --check scripts tests
python -W error -m unittest discover -s tests -v
```

本地完整测试为 53 项。英文报告、引用位置和源文本映射均进入正式回归测试；远程 CI 在发布提交后核验。
