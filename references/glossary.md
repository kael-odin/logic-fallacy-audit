# 中英术语表

本表固定报告结构、判定标签和核心推理类型的英译。英文报告使用 [report-template.en.md](../assets/report-template.en.md) 的字段名，避免同一概念在同一报告中反复改名。

## 1. 报告章节

| 中文 | English | 用途 |
|---|---|---|
| 结论摘要 | Conclusion Summary | 最终主张、主要断点和影响范围 |
| 论证地图 | Argument Map | 结论、前提、隐含前提与推理类型 |
| 关键问题 | Key Issues | 按影响排序的问题卡 |
| 反向检验 | Reverse Test | 最强版本、测试、替代解释与误判 |
| 改写建议 | Rewrite | 可直接引用的修复版本 |
| 边界说明 | Boundaries | 事实、语境与专业限制 |

## 2. 论证地图字段

| 中文 | English |
|---|---|
| 最终结论 | Final Conclusion |
| 显式前提 | Explicit Premises |
| 必要隐含前提（重建） | Necessary Implicit Premises (Reconstructed) |
| 隐含前提的重建依据 | Reconstruction Basis |
| 推理类型 | Reasoning Type |
| 当前缺失环节 | Current Gap |

## 3. 问题卡字段

| 中文 | English |
|---|---|
| 原文 | Original Text |
| 判定 | Verdict |
| 机制 | Mechanism |
| 为什么结论还不能成立 | Why the Conclusion Does Not Yet Follow |
| 影响 | Impact |
| 边界 | Boundary |
| 相关但不主判 | Related but Not Primary |
| 修复条件 | Repair Conditions |

## 4. 反向检验字段

| 中文 | English |
|---|---|
| 最强版本 | Strongest Version |
| 反例或关键测试 | Counterexample or Key Test |
| 替代解释 | Alternative Explanation |
| 可能误判 | Possible Misjudgment |

## 5. 判定标签

| 中文 | English | 条件 |
|---|---|---|
| 确认 | Confirmed | 结构清楚，善意解释不能消除 |
| 较可能 | Likely | 线索明显但缺上下文 |
| 语境相关 | Context-dependent | 只在特定对话或证据条件下成为问题 |
| 不构成谬误 | Not a Fallacy | 经复核后模式合理或只是修辞 |

## 6. 影响等级

| 中文 | English | 含义 |
|---|---|---|
| 阻断 | Blocking | 主结论直接依赖当前断点 |
| 重大 | Major | 关键支持明显不足 |
| 局部 | Local | 只影响例子、支线或局部结论 |
| 表达 | Expression | 主要是语言、框架或修辞风险 |

## 7. 置信度

| 中文 | English |
|---|---|
| 高 | High |
| 中 | Medium |
| 低 | Low |

英文问题卡写作：

```text
`Confirmed` · Hasty Generalization · Confidence: High
```

## 8. 推理类型

| 中文 | English |
|---|---|
| 演绎 | deductive |
| 归纳 | inductive |
| 因果 | causal |
| 统计 | statistical |
| 解释 | explanatory |
| 定义 | definitional |
| 规范 | normative |
| 政策 | policy |

## 9. 核心十类

| 中文 | English | 目录 ID |
|---|---|---|
| 稻草人谬误 | Straw Man | `straw-man` |
| 滑坡谬误 | Slippery Slope | `slippery-slope` |
| 虚假两难 | False Dilemma | `false-dilemma` |
| 诉诸情感 | Appeal to Emotion | `appeal-to-emotion` |
| 错误归因 | False Cause | `false-cause` |
| 人身攻击 | Ad Hominem | `ad-hominem-abusive` |
| 诉诸权威 | Appeal to Authority | `appeal-to-authority` |
| 以偏概全 | Hasty Generalization | `hasty-generalization` |
| 偷换概念 | Equivocation | `equivocation` |
| 循环论证 | Circular Reasoning | `circular-reasoning` |

## 10. 使用规则

- 中文报告默认使用中文标签；英文报告使用本表英译。
- 同一报告不混用多个同义译法。
- `Confirmed` 表示当前文本证据下的判断，不表示事实主张已被外部核验。
- 英文报告也必须保留原文语言；理解翻译不能替代必要引文。
