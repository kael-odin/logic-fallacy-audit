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

## 评测候选

- 中英混杂长文，检查语言切换时的词义稳定性。
- 政策演讲，检查事实前提、价值前提、可行性和替代方案。
- 统计新闻，检查分母、基准率和条件概率。
- 含反讽或转述的长对话，检查是否误把引语当作者立场。
- 一个“没有发现稳定谬误”的有效论证负样本。

## 收录要求

1. 写出具体失败机制和推理式。
2. 至少提供两个诊断问题。
3. 给出原创例子。
4. 写明可能合理的情形。
5. 指向已存在条目并说明为何不能直接合并。
6. 运行严格校验、生成器检查和单元测试。
