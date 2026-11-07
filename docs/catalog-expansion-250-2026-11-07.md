# 250 条目录扩充审查

## 审查范围

- 对公开常见谬误清单进行第二轮名称差距扫描。
- 对照现有 240 条目录，排除别名、上位概念和已有条目已覆盖的机制。
- 为候选补齐定义、推理式、诊断问题、原创例子、边界、易混概念和关联项。
- 为每个新增条目增加行为评测，防止只扩充名称而没有验收场景。

## 结论

目录从 240 条扩展到 250 条。当前共有 218 条谬误或论证模式，以及 32 条与谬误相邻的认知偏差。

本轮新增 10 条：

| ID | 分类 | 独立机制 |
|---|---|---|
| `politicians-syllogism` | formal | 从“必须行动”偷换到“必须采用某个具体方案” |
| `bulverism` | relevance | 先假定对方错误，再只解释其为何会这样想 |
| `courtiers-reply` | relevance | 用圈内资格要求替代对可检验批评的回应 |
| `ergo-decedo` | relevance | 把批评者标成外人，以“离开”回避内容 |
| `false-attribution` | relevance | 把观点或证据归给错误来源以增加可信度 |
| `overwhelming-exception` | causal | 例外多到吞掉一般结论，却保留原概括语气 |
| `ignoring-common-cause` | causal | 把两个共同结果当成彼此因果，忽略第三变量 |
| `inverse-gamblers-fallacy` | statistical | 从一次罕见结果反推大量未观察试验 |
| `ludic-fallacy` | statistical | 把封闭规则模型的概率直接当成开放世界风险 |
| `homunculus-fallacy` | explanation | 用同一能力的内部执行者解释该能力本身 |

## 未直接收录

`vacuous truth` 继续保留为形式逻辑概念候选。它可以是技术性为真的命题，但本身不自动构成谬误，除非被用来误导结论。

`intentional fallacy` 和 `referential fallacy` 仍需要更明确的文本分析边界，避免把文学理论或语言哲学概念泛化成通用标签。

## 评测覆盖

行为评测从 33 条扩展到 43 条。`eval-034` 至 `eval-043` 分别覆盖本轮 10 个新增机制。

新增案例同时检查：

- 是否正确命名主机制；
- 是否把相邻概念限制为 `may_detect`；
- 是否避免从逻辑问题推断恶意、造假或事实真假；
- 是否在没有外部核验时保持事实边界。

## 质量要求

发布前必须通过：

```bash
python scripts/fallacy_cli.py validate --strict
python scripts/fallacy_cli.py render --check
python scripts/report_lint.py examples/sample-report.md --profile full --strict
ruff check scripts tests
ruff format --check scripts tests
python -W error -m unittest discover -s tests -v
```

## 验证结果

- `validate --strict`：0 错误，0 警告。
- `render --check`：生成目录无漂移。
- 行为评测：43 条，四种模式均有样本。
- 单元测试：37 项全部通过。
- Ruff 静态检查与格式检查通过。
- Skill 规范校验通过。

## 边界

本扩充不是对任何外部清单的机械导入。名称相似、机制不稳定或主要属于专业领域规则的候选不会仅因公开列表出现就进入目录。
