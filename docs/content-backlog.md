# 内容审查候选

本文件记录已发现但尚未达到收录门槛的候选。候选不会因为名称常见就自动进入目录，必须先写成可诊断的推理机制并补齐边界。

## 概念候选

| 候选 | 方向 | 当前处理 |
|---|---|---|
| Furtive fallacy | 把结果直接归咎于决策者恶意 | 与 `conspiratorial-motive-inference` 邻近，待区分 |
| Ludic fallacy | 把受规则约束的概率模型误用到开放世界 | 与统计、尾部风险相关，需明确边界 |
| Homunculus fallacy | 用一个小型内部执行者解释同一能力 | 与解释循环相关，需与 `circular-reasoning` 区分 |
| Overwhelming exception | 例外多到使一般结论失去信息量 | 与 `sweeping-generalization` 邻近，待比较 |
| Intentional fallacy | 用作者意图替代文本证据 | 文学理论专用，需避免泛化 |
| Referential fallacy | 假定词语必然指向存在对象 | 与语言哲学相关，需给出文本分析场景 |
| Vacuous truth | 空集合使条件命题技术性为真 | 本身不是谬误，可能只作为形式说明 |
| Observation interpretation | 把观察研究关联直接当因果 | 已由 `cum-hoc` 和 `causal-oversimplification` 覆盖 |
| Garden of forking paths | 未预注册的分析自由度制造显著结果 | 已由 `p-hacking` 与 `multiple-comparisons` 覆盖 |
| Overwhelming exception | 例外多到使一般结论失去信息量 | 高价值候选，需要与 `sweeping-generalization` 明确分界 |
| Bulverism | 先假定对方错误，再只解释其为何会这样想 | 高价值候选，需与人身攻击和发生学谬误分界 |
| Courtier's reply | 以批评者缺少圈内资格为由拒绝回应内容 | 高价值候选，需与合理专业知识要求分界 |
| Ergo decedo | 把批评者视为外人，并以“不喜欢就离开”回避论证 | 高价值候选，需与合法的利益相关性和代表性要求分界 |
| Ignoring a common cause | 把两个共同结果当成彼此因果，忽略第三变量 | 高价值候选，可与 `cum-hoc`、`single-cause` 建立关联 |
| Inverse gambler's fallacy | 从当前一次结果反推此前发生过大量未观察试验 | 高价值统计候选，需与贝叶斯更新区分 |

## 评测状态

以下目标已经转为回归样本：

| 目标 | 对应案例 |
|---|---|
| 中英混杂与词义稳定性 | `eval-018`、`eval-019`、`eval-020`、`eval-030` |
| 政策、目标、成本与替代方案 | `eval-020`、`eval-029` |
| 统计、分母、基准率与样本 | `eval-008`、`eval-021`、`eval-023` |
| 有效专业意见与风险判断负样本 | `eval-025`、`eval-032` |
| 长对话与责任转移 | `eval-031` |
| 教学模式与个案证据 | `eval-033` |

仍待补充：

- 含反讽、引用和转述的长对话，检查是否误把角色话语当成作者立场。
- 同一文本包含两个独立论证单元时，检查是否错误合并结论。
- 统计结果方向相反但都真实时，检查是否遗漏冲突证据。

## 收录要求

1. 写出具体失败机制和推理式。
2. 至少提供两个诊断问题。
3. 给出原创例子。
4. 写明可能合理的情形。
5. 指向已存在条目并说明为何不能直接合并。
6. 运行严格校验、生成器检查和单元测试。
