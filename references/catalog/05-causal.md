# 因果、归纳与类比

**Causal, Inductive, and Analogical Reasoning**

从有限经验、相似性或事件顺序跳到一般、因果或预测结论。

> 使用提示：检查样本、机制、时序、对照和替代解释。

> 本文件由结构化目录生成。修改 `catalog/` 后再运行 `python scripts/fallacy_cli.py render`。

共 **27** 条。

## 快速索引

| 中文名 | English | ID |
|---|---|---|
| 草率概括 | Hasty Generalization | `hasty-generalization` |
| 过度概括 | Sweeping Generalization | `sweeping-generalization` |
| 轶事证据 | Anecdotal Evidence | `anecdotal-evidence` |
| 生动性误导 | Misleading Vividness | `misleading-vividness` |
| 懒惰归纳 | Slothful Induction | `slothful-induction` |
| 虚假因果 | False Cause | `false-cause` |
| 事后归因 | Post Hoc Ergo Propter Hoc | `post-hoc` |
| 相关即因果 | Cum Hoc Ergo Propter Hoc | `cum-hoc` |
| 单一原因谬误 | Single Cause Fallacy | `single-cause` |
| 因果过度简化 | Causal Oversimplification | `causal-oversimplification` |
| 因果倒置 | Causal Inversion | `causal-inversion` |
| 滑坡谬误 | Slippery Slope | `slippery-slope` |
| 弱类比 | Weak Analogy | `weak-analogy` |
| 诉诸概率 | Appeal to Probability | `appeal-to-probability` |
| 回归谬误 | Regression Fallacy | `regression-fallacy` |
| 赌徒谬误 | Gambler's Fallacy | `gamblers-fallacy` |
| 热手谬误 | Hot-Hand Fallacy | `hot-hand-fallacy` |
| 沉没成本谬误 | Sunk Cost Fallacy | `sunk-cost-fallacy` |
| 涅槃谬误 | Nirvana Fallacy | `nirvana-fallacy` |
| 破窗谬误 | Broken Window Fallacy | `broken-window-fallacy` |
| 劳动总量谬误 | Lump of Labor Fallacy | `lump-of-labor` |
| 零和谬误 | Zero-Sum Fallacy | `zero-sum-fallacy` |
| 完美主义标准 | Perfectionist Fallacy | `perfectionist-fallacy` |
| 事后必然论 | Retrospective Determinism | `retrospective-determinism` |
| 压倒性例外 | Overwhelming Exception | `overwhelming-exception` |
| 忽略共同原因 | Ignoring a Common Cause | `ignoring-common-cause` |
| 偶然例外谬误 | Accident Fallacy | `accident-fallacy` |

---

## 草率概括

**Hasty Generalization** · `hasty-generalization`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：以偏概全、样本不足概括

### 定义

从数量很少、代表性不足或来源单一的样本，推出适用范围更广的一般结论。

### 推理式

```text
少数样本 x1…xn 具有 F；因此目标总体 G 大体或全部具有 F。
```

### 诊断问题

1. 样本如何选出，能否代表目标总体？
2. 结论范围是否远大于样本覆盖范围？
3. 是否存在与结论相反但未纳入的案例？

### 原创例子

> 我认识的三个创业者都成功了，所以创业只要敢做就能成功。

### 何时可能不是谬误

小样本可以提供线索或个案证据；问题在于把线索升级为总体结论。

### 容易混淆

轶事证据、代表性启发、统计样本

### 相关条目

过度概括 (`sweeping-generalization`)、轶事证据 (`anecdotal-evidence`)、选择偏差 (`selection-bias`)


---

## 过度概括

**Sweeping Generalization** · `sweeping-generalization`

- 类型：非形式谬误
- 默认影响：中等
- 别名：绝对化概括、无视例外

### 定义

把一条有合理例外或适用范围的原则，使用成没有例外的全称规则。

### 推理式

```text
原则上通常 P；因此在所有情况下都必须 P，且无例外。
```

### 诊断问题

1. 原规则是否本来就带范围、程度或例外？
2. 当前案例是否落在已知例外条件中？

### 原创例子

> 运动有益健康，所以任何病人在任何情况下都应该高强度训练。

### 何时可能不是谬误

规范原则可以是绝对规则，但需要明确来源；经验规律通常有例外。

### 容易混淆

hasty generalization、例外滥用、规则应用

### 相关条目

草率概括 (`hasty-generalization`)、特殊豁免 (`special-pleading`)、小项不当周延 (`illicit-minor`)


---

## 轶事证据

**Anecdotal Evidence** · `anecdotal-evidence`

- 类型：非形式谬误
- 默认影响：中等
- 别名：个例证明、我朋友说

### 定义

用个别、自选或难以核验的故事支持普遍因果或政策结论。

### 推理式

```text
一个故事显示 P；因此总体 P 很可能成立。
```

### 诊断问题

1. 该故事如何被选中，失败案例是否被遗漏？
2. 故事能证明存在可能，还是能估计总体频率与因果效应？

### 原创例子

> 我邻居吃了这种保健品后精神很好，所以它对所有人都有效。

### 何时可能不是谬误

个案对发现风险、提出假设、说明体验很有价值；但不能单独估计一般效果。

### 容易混淆

案例研究、hasty generalization、misleading vividness

### 相关条目

草率概括 (`hasty-generalization`)、生动性误导 (`misleading-vividness`)、选择偏差 (`selection-bias`)


---

## 生动性误导

**Misleading Vividness** · `misleading-vividness`

- 类型：非形式谬误
- 默认影响：中等
- 别名：生动个例压过统计、可记忆性偏差

### 定义

一个情绪强烈、画面鲜明或容易回忆的案例，被赋予超过数据应有的证据权重。

### 推理式

```text
生动案例 E 支持 P；因此忽略更大样本或基准率而接受 P。
```

### 诊断问题

1. 该案例是否因为罕见、戏剧化或情绪强而更醒目？
2. 总体数据和基准率显示了什么？

### 原创例子

> 一次坠机新闻让人认为坐飞机比开车危险，尽管统计风险相反。

### 何时可能不是谬误

鲜明案例可说明潜在机制和受害规模；不能替代频率估计。

### 容易混淆

availability heuristic、anecdotal evidence、base-rate neglect

### 相关条目

轶事证据 (`anecdotal-evidence`)、可得性启发 (`availability-heuristic`)、基准率忽视 (`base-rate-neglect`)


---

## 懒惰归纳

**Slothful Induction** · `slothful-induction`

- 类型：非形式谬误
- 默认影响：中等
- 别名：拒绝归纳、证据够了仍不承认

### 定义

面对重复、稳定且总体一致的模式，仍以“可能只是巧合”为由拒绝任何归纳结论，却不给替代解释。

### 推理式

```text
大量独立观察支持 P；作者只重复“不能百分百确定”；因此不作任何暂定结论。
```

### 诊断问题

1. 是否存在比 P 更好的替代解释？
2. 证据是否已达到合理决策门槛，而作者把绝对确定当成门槛？

### 原创例子

> 连续五年每个季度销量下降，他却说这只是偶然，拒绝考虑市场变化。

### 何时可能不是谬误

审慎要求确认替代解释是合理的；不能把“可能有未知因素”无限变成拒绝所有证据。

### 容易混淆

科学审慎、不可证伪、slothful induction

### 相关条目

回归谬误 (`regression-fallacy`)、不可证伪性 (`unfalsifiability`)、移动球门 (`moving-the-goalposts`)


---

## 虚假因果

**False Cause** · `false-cause`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：乱因谬误、非因果归因、错误归因

### 定义

在没有足够因果证据时，把共同出现、先后发生或象征关联当成因果关系。

### 推理式

```text
A 与 B 相关或先于 B；因此 A 导致 B。
```

### 诊断问题

1. 是否存在共同原因、反向因果或选择偏差？
2. 时序、机制、剂量反应和对照是否支持因果？

### 原创例子

> 这个城市冰淇淋销量上升后犯罪率也上升，所以冰淇淋导致犯罪。

### 何时可能不是谬误

无法排除所有混杂不意味着因果为零；需要评估总体证据强度。

### 容易混淆

post hoc、cum hoc、single cause

### 相关条目

事后归因 (`post-hoc`)、相关即因果 (`cum-hoc`)、因果过度简化 (`causal-oversimplification`)


---

## 事后归因

**Post Hoc Ergo Propter Hoc** · `post-hoc`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：在此之后所以因此、时序因果

### 定义

仅因为 B 在 A 之后发生，就推出 A 是 B 的原因。

### 推理式

```text
A 先于 B；因此 A 导致 B。
```

### 诊断问题

1. 是否只是时间先后，而没有机制和对照？
2. 同一时期是否有其他变化也能解释 B？
3. 若没有 A，B 是否仍可能发生？

### 原创例子

> 我换了头像后球队连胜，所以头像带来了胜利。

### 何时可能不是谬误

A 先于 B 是因果的必要线索之一；若有机制、重复实验和对照支持，可以形成因果论证。

### 容易混淆

false cause、cum hoc、causal inversion

### 相关条目

虚假因果 (`false-cause`)、相关即因果 (`cum-hoc`)、回归谬误 (`regression-fallacy`)


---

## 相关即因果

**Cum Hoc Ergo Propter Hoc** · `cum-hoc`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：伴随发生所以导致、相关性谬误

### 定义

只凭两个变量同时变化或同时存在，就断言其中一个导致另一个。

### 推理式

```text
A 与 B 统计相关；因此 A 导致 B。
```

### 诊断问题

1. 反向因果是否同样合理？
2. 是否存在第三变量同时影响 A 和 B？
3. 相关是否由选择或分组方式制造？

### 原创例子

> 使用某学习软件的学生成绩更高，所以软件一定提升了成绩。

### 何时可能不是谬误

相关性是因果证据之一，尤其在机制、时序和自然实验中相互支持时；不能因可能混杂就忽略全部证据。

### 容易混淆

false cause、post hoc、selection bias

### 相关条目

虚假因果 (`false-cause`)、事后归因 (`post-hoc`)、选择偏差 (`selection-bias`)


---

## 单一原因谬误

**Single Cause Fallacy** · `single-cause`

- 类型：非形式谬误
- 默认影响：中等
- 别名：单因解释、唯一原因假设

### 定义

把由多因素共同作用的复杂结果归因于一个原因，并排除其他贡献因素。

### 推理式

```text
结果 B 出现；找到一个可能原因 A；因此 A 是唯一或主要充分原因。
```

### 诊断问题

1. 结果是否可能由多个必要或促进因素共同造成？
2. 其他因素的贡献是否被比较或排除？

### 原创例子

> 公司项目失败完全是因为一个实习生写错一行代码。

### 何时可能不是谬误

为了解释局部机制可以聚焦一个因素；但不能把聚焦误写成排他性因果结论。

### 容易混淆

causal oversimplification、root cause、false cause

### 相关条目

因果过度简化 (`causal-oversimplification`)、虚假因果 (`false-cause`)、基本归因错误 (`fundamental-attribution-error`)


---

## 因果过度简化

**Causal Oversimplification** · `causal-oversimplification`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：复杂因果压扁、单线因果

### 定义

把有反馈、概率、阈值、相互作用或时间延迟的因果系统，压缩成简单单向链条。

### 推理式

```text
复杂系统 S 中 A 与 B 相关；论证表示为 A → B，忽略条件 C 和反馈 F。
```

### 诊断问题

1. 因果关系是否有条件、剂量、阈值或双向反馈？
2. 简化是否改变了政策或责任结论？

### 原创例子

> 提高奖金一定提高效率，因为员工收入越高越努力。

### 何时可能不是谬误

所有模型都是简化；评估重点是简化是否保留了影响当前结论的关键结构。

### 容易混淆

single cause、false cause、broken window fallacy

### 相关条目

单一原因谬误 (`single-cause`)、虚假因果 (`false-cause`)、滑坡谬误 (`slippery-slope`)


---

## 因果倒置

**Causal Inversion** · `causal-inversion`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：反向因果、结果当原因、wrong direction

### 定义

把因果方向说反，把结果当成原因，或忽略双方相互影响。

### 推理式

```text
A 与 B 相关；断言 A → B；但更可能或同样可能是 B → A。
```

### 诊断问题

1. 哪个变化先发生，时序是否可观察？
2. B 是否能反过来影响 A？
3. 是否存在反馈循环？

### 原创例子

> 经常看病的人身体更差，所以看病损害健康。

### 何时可能不是谬误

反向因果必须用机制和时序证据评估；不能仅凭相关性猜测方向。

### 容易混淆

cum hoc、post hoc、feedback loop

### 相关条目

相关即因果 (`cum-hoc`)、事后归因 (`post-hoc`)、虚假因果 (`false-cause`)


---

## 滑坡谬误

**Slippery Slope** · `slippery-slope`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：多米诺谬误、一路滑到底

### 定义

从一个初始变化推出一连串后果，却不证明每一中间步骤的概率、机制和可阻止措施。

### 推理式

```text
A 导致 B，B 导致 C，C 导致灾难 D；因此不能允许 A。
```

### 诊断问题

1. 每一段因果链是否有独立证据和概率？
2. 中间节点是否可以被制度、成本或反作用力阻止？
3. 比较的是 A 的实际风险，还是想象中的极端终点？

### 原创例子

> 允许学生选择一次作业主题，下一步他们就会拒绝所有课程要求，最终学校完全失控。

### 何时可能不是谬误

如果每一步都有机制、历史证据和较低阻断概率，连续后果论证可以成立；它就是风险预测，不是自动谬误。

### 容易混淆

domino fallacy、appeal to fear、causal chain

### 相关条目

诉诸恐惧 (`appeal-to-fear`)、因果过度简化 (`causal-oversimplification`)、涅槃谬误 (`nirvana-fallacy`)


---

## 弱类比

**Weak Analogy** · `weak-analogy`

- 类型：非形式谬误
- 默认影响：中等
- 别名：不当类比、错误比较

### 定义

用两个对象在表面或无关维度上的相似，推出它们在结论相关维度上也相似。

### 推理式

```text
A 与 B 都有 F；结论依赖属性 G；因此 A 与 B 在 G 上也相同。
```

### 诊断问题

1. 被比较的相似点是否与结论相关？
2. 已知差异是否足以破坏类比？
3. 类比是在提出假设，还是承担了证明？

### 原创例子

> 公司像家庭，所以员工应该无条件接受老板安排。

### 何时可能不是谬误

类比主要用于说明、发现假设和扩展模型；强类比需要关键结构相似和独立验证。

### 容易混淆

false equivalence、misleading metaphor、case comparison

### 相关条目

虚假等同 (`false-equivalence`)、误导性隐喻 (`misleading-metaphor`)、草率概括 (`hasty-generalization`)


---

## 诉诸概率

**Appeal to Probability** · `appeal-to-probability`

- 类型：非形式谬误
- 默认影响：中等
- 别名：可能所以一定、概率当必然

### 定义

从某结果可能发生或概率较高，推出它当前一定发生或将发生在特定个案。

### 推理式

```text
P 可能或很可能发生；因此 P 已经发生或将发生。
```

### 诊断问题

1. 讨论的是群体频率还是单个案例？
2. “可能/很可能”被替换成“必然”了吗？

### 原创例子

> 航班通常准时，所以这班飞机今天一定不会延误。

### 何时可能不是谬误

概率可以支持合理预期和风险管理；但不能保证单次结果。

### 容易混淆

gambler's fallacy、base-rate neglect、modal scope

### 相关条目

赌徒谬误 (`gamblers-fallacy`)、基准率忽视 (`base-rate-neglect`)、存在性谬误 (`existential-fallacy`)


---

## 回归谬误

**Regression Fallacy** · `regression-fallacy`

- 类型：统计推理
- 默认影响：中等
- 别名：均值回归误读、极端表现因果化

### 定义

把极端结果自然回归平均的变化，归因于随后采取的措施。

### 推理式

```text
极端表现 Y1 后自然出现较接近均值的 Y2；因此干预 X 导致了改善。
```

### 诊断问题

1. 样本是否因上一次极端分数而被选中？
2. 如果没有干预，均值回归是否也可能发生？

### 原创例子

> 最差的一天后进行严厉批评，第二天表现改善，于是认为批评有效。

### 何时可能不是谬误

干预可能有真实效果；需要对照组或更完整时间序列区分效果与回归。

### 容易混淆

post hoc、selection effect、regression to mean

### 相关条目

事后归因 (`post-hoc`)、选择偏差 (`selection-bias`)、误导性平均值 (`misleading-average`)


---

## 赌徒谬误

**Gambler's Fallacy** · `gamblers-fallacy`

- 类型：统计推理
- 默认影响：中等
- 别名：独立事件补偿、该轮到我了

### 定义

在独立或近似独立事件中，认为过去结果会改变下一次结果的概率。

### 推理式

```text
随机事件连续出现 A；因此下一次更可能出现 B。
```

### 诊断问题

1. 事件是否真的独立，系统是否有记忆？
2. “长期平均”是否被误用到下一次单次事件？

### 原创例子

> 硬币连续五次正面，所以下一次更应该是反面。

### 何时可能不是谬误

若抽取不放回、系统有磨损或结果不独立，过去结果可能改变概率；关键是机制。

### 容易混淆

hot hand、law of large numbers、regression

### 相关条目

热手谬误 (`hot-hand-fallacy`)、诉诸概率 (`appeal-to-probability`)、代表性启发 (`representativeness-heuristic`)


---

## 热手谬误

**Hot-Hand Fallacy** · `hot-hand-fallacy`

- 类型：统计推理
- 默认影响：中等
- 别名：连续成功即趋势、手气正热

### 定义

从短时间连续成功推断能力或状态已发生稳定变化，却没有检查真实转移概率。

### 推理式

```text
某人连续成功 k 次；因此下一次成功概率显著更高。
```

### 诊断问题

1. 成功率是否高于基准且有足够样本？
2. 连续序列在随机过程中是否本来就会常见？

### 原创例子

> 球员连进三球，所以下一次投篮的命中率一定会更高。

### 何时可能不是谬误

某些真实技能、信心或对手调整确实会产生状态相关；需要数据而非只看连续感。

### 容易混淆

gambler's fallacy、small sample、clustering illusion

### 相关条目

赌徒谬误 (`gamblers-fallacy`)、草率概括 (`hasty-generalization`)、回归谬误 (`regression-fallacy`)


---

## 沉没成本谬误

**Sunk Cost Fallacy** · `sunk-cost-fallacy`

- 类型：非形式谬误
- 默认影响：中等
- 别名：已经投入不能放弃、沉没成本

### 定义

因为过去已经投入时间、金钱或声誉而继续一个项目，即使未来收益不再值得继续成本。

### 推理式

```text
已经投入 C；因此必须继续 P，哪怕继续 P 的边际收益为负。
```

### 诊断问题

1. 过去的投入能否收回，是否会因继续而变化？
2. 从今天起比较继续、停止和替代方案的未来成本收益。

### 原创例子

> 这部电影票已经买了，即使很难看也要坐到最后。

### 何时可能不是谬误

过去投入可能带来承诺、学习、资产或声誉价值；这些价值需作为未来收益重新计入，而不是凭“不能浪费”。

### 容易混淆

承诺一致性、损失厌恶、机会成本

### 相关条目

损失厌恶 (`loss-aversion`)、现状偏差 (`status-quo-bias`)、沉没成本偏差 (`sunk-cost-bias`)


---

## 涅槃谬误

**Nirvana Fallacy** · `nirvana-fallacy`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：完美方案谬误、完美主义谬误

### 定义

把现实方案与理想完美方案比较，因为现实方案有缺陷就拒绝它，而不与其他可行方案比较。

### 推理式

```text
P 不能完全解决问题；因此 P 没有价值，应该拒绝。
```

### 诊断问题

1. 当前比较对象是否是可行替代，而不是想象中的完美方案？
2. P 是否仍能带来净收益或减少损害？

### 原创例子

> 这项反腐措施不能根除所有腐败，所以完全没必要实施。

### 何时可能不是谬误

如果方案成本高、副作用大或挤占更好方案，拒绝可以合理；问题在于只用完美标准。

### 容易混淆

现实比较、false dilemma、causal oversimplification

### 相关条目

虚假两难 (`false-dilemma`)、滑坡谬误 (`slippery-slope`)、完美主义标准 (`perfectionist-fallacy`)


---

## 破窗谬误

**Broken Window Fallacy** · `broken-window-fallacy`

- 类型：非形式谬误
- 默认影响：中等
- 别名：破坏也能创造就业、有形的机会成本忽视

### 定义

只看见破坏带来的可见支出和就业，忽略被挤出的资源以及未发生的替代用途。

### 推理式

```text
破坏产生维修需求 B；因此破坏带来净经济收益；忽略本来可用于其他生产的机会 C。
```

### 诊断问题

1. 被破坏资源原本还能如何使用？
2. 新增需求是否挤占其他消费或生产？
3. 净效应而非仅可见支出是什么？

### 原创例子

> 打碎窗户让玻璃工有工作，所以打碎窗户有利于经济。

### 何时可能不是谬误

灾后重建可能带来某些局部机会，但整体净效应仍需计入损失和机会成本。

### 容易混淆

机会成本、零和谬误、可见性偏差

### 相关条目

零和谬误 (`zero-sum-fallacy`)、劳动总量谬误 (`lump-of-labor`)、可得性启发 (`availability-heuristic`)


---

## 劳动总量谬误

**Lump of Labor Fallacy** · `lump-of-labor`

- 类型：非形式谬误
- 默认影响：中等
- 别名：岗位总数固定、工作总量固定

### 定义

假设经济中的岗位数量固定，因此某个群体就业增加必然减少另一个群体就业。

### 推理式

```text
工作岗位总量固定为 N；组 A 获得更多岗位；因此组 B 必然少同样多。
```

### 诊断问题

1. 岗位总量是否真的固定？
2. 生产率变化是否会创造新需求和新职业？
3. 短期与长期效应是否区分？

### 原创例子

> 自动化让机器做一份工作，就必然永久减少一份人类工作。

### 何时可能不是谬误

短期局部替代确实可能发生，特定劳动者也可能受损；不能由此直接推出总体岗位数恒定。

### 容易混淆

zero-sum、short-run vs long-run、fixed pie

### 相关条目

零和谬误 (`zero-sum-fallacy`)、破窗谬误 (`broken-window-fallacy`)、现状偏差 (`status-quo-bias`)


---

## 零和谬误

**Zero-Sum Fallacy** · `zero-sum-fallacy`

- 类型：非形式谬误
- 默认影响：中等
- 别名：固定蛋糕思维、一方受益必有一方受损

### 定义

在没有证据时，把互动假设为总量固定的零和关系，忽略正和、负和或分配变化。

### 推理式

```text
A 获得收益；因此 B 必然等量受损。
```

### 诊断问题

1. 总价值是否可能增加或减少，而非固定转移？
2. 双方是否存在合作、交易成本和外部性？

### 原创例子

> 学生 A 成绩提高，所以学生 B 一定是被挤下去的。

### 何时可能不是谬误

许多场景确实竞争固定资源，如单一名额或预算；零和假设需要根据制度证明，而非默认。

### 容易混淆

机会成本、竞争关系、trade-off

### 相关条目

破窗谬误 (`broken-window-fallacy`)、劳动总量谬误 (`lump-of-labor`)、虚假等同 (`false-equivalence`)


---

## 完美主义标准

**Perfectionist Fallacy** · `perfectionist-fallacy`

- 类型：非形式谬误
- 默认影响：中等
- 别名：不完美所以无效、全有或全无

### 定义

要求方案在所有方面达到完美，否则就把它等同于完全失败或毫无价值。

### 推理式

```text
P 不能达到理想结果 I；因此 P 与零效果无差异。
```

### 诊断问题

1. 是否存在可比较的部分改善、风险管理或替代方案？
2. 评估使用的是绝对标准还是现实基线？

### 原创例子

> 这款安全工具不能挡住所有攻击，所以装上它没有意义。

### 何时可能不是谬误

某些安全、医疗或法律标准确实要求通过硬门槛；仍需区分必要门槛与全面完美要求。

### 容易混淆

nirvana fallacy、false dilemma、risk policy

### 相关条目

涅槃谬误 (`nirvana-fallacy`)、虚假两难 (`false-dilemma`)、因果过度简化 (`causal-oversimplification`)


---

## 事后必然论

**Retrospective Determinism** · `retrospective-determinism`

- 类型：非形式谬误
- 默认影响：中等
- 别名：结果反推必然、既然发生所以不可避免

### 定义

因为某事件已经发生，就断言当时的环境使它不可避免，并把事后解释提升为必然因果。

### 推理式

```text
E 已发生，且发生时存在 C；因此 C 必然导致 E。
```

### 诊断问题

1. 在事件发生前，C 条件下 E 的概率有多大？
2. 是否存在未发生的替代结果和阻断因素？

### 原创例子

> 球队穿新球鞋后赢了，所以那双鞋使胜利不可避免。

### 何时可能不是谬误

确定性系统可以由定律和初始条件推出结果；复杂社会事件通常仍需概率和反事实比较。

### 容易混淆

事后归因、后见之明偏差、模态辖域谬误

### 相关条目

事后归因 (`post-hoc`)、后见之明偏差 (`hindsight-bias`)、模态辖域谬误 (`modal-scope-fallacy`)


---

## 压倒性例外

**Overwhelming Exception** · `overwhelming-exception`

- 类型：非形式谬误
- 默认影响：中等
- 别名：例外吞掉结论、限定过多、只剩特例的概括

### 定义

一般结论不断加上大量例外，排除后只剩极窄范围，却仍保留原来的强概括语气和结论。

### 推理式

```text
一般命题 P 适用于 X；追加例外 E1、E2……；剩余范围远小于 P 的表面含义；仍用 P 支撑原结论。
```

### 诊断问题

1. 例外覆盖了目标范围的多大比例？
2. 去掉例外后，原结论还剩多少信息量？
3. 标题和结论是否明确承认收窄后的范围？

### 原创例子

> 公司充分听取所有员工意见，当然，新员工、外包、远程员工和一线值班人员除外；所以不存在沟通问题。

### 何时可能不是谬误

合理概括可以包含有限例外；问题是例外太多使原命题失去预测力，而表述仍暗示范围很广。

### 容易混淆

过度概括、草率概括、没有真正的苏格兰人

### 相关条目

过度概括 (`sweeping-generalization`)、草率概括 (`hasty-generalization`)、没有真正的苏格兰人 (`no-true-scotsman`)


---

## 忽略共同原因

**Ignoring a Common Cause** · `ignoring-common-cause`

- 类型：非形式谬误
- 默认影响：中等
- 别名：第三变量忽略、混杂因素忽略、共同因素误判

### 定义

观察到两个现象相关，就推断其中一个导致另一个，却没有检查是否存在同时影响二者的第三因素。

### 推理式

```text
A 与 B 相关；因此 A 导致 B；未检查共同原因 C。
```

### 诊断问题

1. 是否存在同时影响 A 和 B 的第三变量？
2. 控制该变量后关联是否减弱？
3. 时间顺序和干预证据能否区分共同原因与因果方向？

### 原创例子

> 冰淇淋销量和溺水人数一起上升，所以吃冰淇淋导致溺水。

### 何时可能不是谬误

共同原因必须可解释、可测量，而不是无限添加未知变量；控制混杂后相关仍可支持因果。

### 容易混淆

相关即因果、虚假因果、单一原因谬误

### 相关条目

相关即因果 (`cum-hoc`)、虚假因果 (`false-cause`)、单一原因谬误 (`single-cause`)


---

## 偶然例外谬误

**Accident Fallacy** · `accident-fallacy`

- 类型：非形式谬误
- 默认影响：中等
- 别名：偶然谬误、一般规则忽略例外、destroying the exception

### 定义

把一条通常适用的一般规则套到具有相关特殊性的个案上，却不检查该例外是否改变了规则原本要保护的目的。

### 推理式

```text
一般规则 R 在正常条件下支持结论 C；个案 X 具有相关例外特征；仍直接套用 R 推出 C。
```

### 诊断问题

1. 个案的哪个特征可能使一般规则不适用？
2. 规则的目的和例外条件是否允许当前套用？
3. 如果处理这个例外，是否会造成相反但可解释的结果？

### 原创例子

> 公司原则上禁止远程办公，所以员工家人在急诊时也不能临时远程处理紧急工作。

### 何时可能不是谬误

规则可以有意保留有限例外以维持可执行性；问题是把经验概括当成没有边界的绝对规则。

### 容易混淆

草率概括、没有真正的苏格兰人、规则与例外

### 相关条目

草率概括 (`hasty-generalization`)、没有真正的苏格兰人 (`no-true-scotsman`)、虚假两难 (`false-dilemma`)


[返回分类索引](../catalog-index.md)
