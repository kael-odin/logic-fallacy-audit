# 内容审查候选

本文件记录已发现但尚未达到收录门槛的候选。候选不会因为名称常见就自动进入目录，必须先写成可诊断的推理机制并补齐边界。

## 概念候选

| 候选 | 方向 | 当前处理 |
|---|---|---|
| Intentional fallacy | 用作者意图替代文本证据 | 文学理论专用，需避免泛化 |
| Vacuous truth | 空集合使条件命题技术性为真 | 本身不是谬误，可能只作为形式说明 |
| Observation interpretation | 把观察研究关联直接当因果 | 已由 `cum-hoc` 和 `causal-oversimplification` 覆盖 |
| Garden of forking paths | 未预注册的分析自由度制造显著结果 | 已由 `p-hacking` 与 `multiple-comparisons` 覆盖 |

## v1.3 已收录的补强

本轮从候选池转为正式条目：

- `overwhelming-exception`
- `bulverism`
- `courtiers-reply`
- `ergo-decedo`
- `false-attribution`
- `politicians-syllogism`
- `ignoring-common-cause`
- `inverse-gamblers-fallacy`
- `homunculus-fallacy`
- `ludic-fallacy`

## v2.0 新增

本轮名称差异扫描后新增：

- `accident-fallacy`
- `ambiguous-middle-term`
- `exhaustive-effort-fallacy`
- `furtive-fallacy`
- `if-by-whiskey`
- `inflation-of-conflict`
- `nut-picking`
- `pooh-pooh`
- `referential-fallacy`
- `psychologists-fallacy`

同时给已有条目补充常见外部名称别名，例如 `argument from fallacy`、`argument from ignorance`、`false authority`、`wrong direction`、`ipse dixit` 和 `garden of forking paths`。

## 评测状态

以下目标已经转为回归样本：

| 目标 | 对应案例 |
|---|---|
| 中英混杂与词义稳定性 | `eval-018`、`eval-019`、`eval-020`、`eval-030` |
| 政策、目标、成本与替代方案 | `eval-020`、`eval-029` |
| 统计、分母、基准率与样本 | `eval-008`、`eval-021`、`eval-023` |
| 有效专业意见与风险判断负样本 | `eval-025`、`eval-032` |
| 长对话、引用归属与责任转移 | `eval-031`、`eval-046` |
| 多论证单元拆分 | `eval-047` |
| 教学模式与个案证据 | `eval-033` |
| 250 条补强中的全部新机制 | `eval-034` 至 `eval-043` |
| v2.0 新增的十项机制 | `eval-050` 至 `eval-059` |

仍待补充：

- 统计结果方向相反但都真实时，检查是否遗漏冲突证据。

## 收录要求

1. 写出具体失败机制和推理式。
2. 至少提供两个诊断问题。
3. 给出原创例子。
4. 写明可能合理的情形。
5. 指向已存在条目并说明为何不能直接合并。
6. 运行严格校验、生成器检查和单元测试。
