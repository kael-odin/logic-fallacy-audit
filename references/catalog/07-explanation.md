# 解释、模式与阴谋论式推理

**Explanation, Pattern, and Conspiratorial Reasoning**

比较解释时不可证伪、异常猎取、过度归因或采用不对称证据标准。

> 使用提示：比较至少两个竞争解释，并检查可反驳预测。

> 本文件由结构化目录生成。修改 `catalog/` 后再运行 `python scripts/fallacy_cli.py render`。

共 **14** 条。

## 快速索引

| 中文名 | English | ID |
|---|---|---|
| 异常猎取 | Anomaly Hunting | `anomaly-hunting` |
| 不可能证据标准 | Impossible Expectations | `impossible-expectation` |
| 不可证伪阴谋解释 | Unfalsifiable Conspiracy Explanation | `unfalsifiable-conspiracy` |
| 谁受益谁策划 | Cui Bono Fallacy | `cui-bono-fallacy` |
| 模式聚类错觉 | Clustering Illusion | `pattern-clustering-illusion` |
| 重大事件必有大原因 | Proportionality Bias | `proportionality-bias` |
| 阴谋动机推定 | Conspiratorial Motive Inference | `conspiratorial-motive-inference` |
| 假旗预设 | False-Flag Assumption | `false-flag-assumption` |
| 正反都赢 | Heads-I-Win-Tails-You-Lose | `heads-i-win-tails-you-lose` |
| 证据缺失推演 | Absence-of-Evidence Reasoning | `absence-of-evidence` |
| 历史学家谬误 | Historian's Fallacy | `historians-fallacy` |
| 小人谬误 | Homunculus Fallacy | `homunculus-fallacy` |
| 隐秘动机谬误 | Furtive Fallacy | `furtive-fallacy` |
| 心理学家谬误 | Psychologist's Fallacy | `psychologists-fallacy` |

---

## 异常猎取

**Anomaly Hunting** · `anomaly-hunting`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：只盯异常点、异常即隐藏真相

### 定义

在大量正常数据中专门搜索少数异常，再把异常解释成隐藏阴谋或理论证据，而不先估计随机波动和搜索次数。

### 推理式

```text
检查很多数据点；找到一个不符合常规的 A；因此理论 P 得到支持。
```

### 诊断问题

1. 一共检查了多少数据点，异常比例多大？
2. 竞争解释能否同样解释异常？
3. 异常是否在预测前就被指定？

### 原创例子

> 逐帧检查一段视频，找出一个模糊影子，因此断言整段视频背后有秘密安排。

### 何时可能不是谬误

异常可以触发调查，也可能提供真实线索；问题在于把事后发现的异常直接当作验证。

### 容易混淆

Texas sharpshooter、clustering illusion、cherry-picking

### 相关条目

德州神枪手谬误 (`texas-sharpshooter`)、模式聚类错觉 (`pattern-clustering-illusion`)、樱桃挑选 (`cherry-picking`)


---

## 不可能证据标准

**Impossible Expectations** · `impossible-expectation`

- 类型：辩证规则
- 默认影响：高影响
- 别名：永远无法满足的证据要求、完美记录要求

### 定义

给竞争解释设置现实上不可能达到的证据标准，同时对自己偏好的解释采用极低标准。

### 推理式

```text
理论 P 只需薄弱线索；反对理论 Q 被要求完全无缺口、全部原始资料和绝对确定。
```

### 诊断问题

1. 对两个竞争解释是否使用同一证据门槛？
2. 要求的证据在现实记录条件下可获得吗？

### 原创例子

> 普通事故要求完整记录每一秒才可信，而阴谋解释只需一句“他们肯定藏起来了”。

### 何时可能不是谬误

高风险结论值得更严格证据；但标准应对称、可实现，并与结论严重性成比例。

### 容易混淆

moving goalposts、special pleading、unfalsifiability

### 相关条目

移动球门 (`moving-the-goalposts`)、特殊豁免 (`special-pleading`)、不可证伪阴谋解释 (`unfalsifiable-conspiracy`)


---

## 不可证伪阴谋解释

**Unfalsifiable Conspiracy Explanation** · `unfalsifiable-conspiracy`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：反证也是阴谋、自我封闭阴谋论

### 定义

把支持、反对和缺少证据都解释成阴谋的一部分，使解释不受任何经验结果约束。

### 推理式

```text
证据支持 P；所以阴谋存在。证据反对 P；所以他们在掩盖。没有证据；所以控制得极好。
```

### 诊断问题

1. 哪种可观察结果会使阴谋主张被放弃？
2. 反对证据是否被无成本地吸收成支持？
3. 是否存在可独立调查的具体行为者、时间与文件？

### 原创例子

> 如果文件出现，说明他们伪造；如果文件消失，说明他们销毁；如果文件从未存在，说明他们隐藏得好。

### 何时可能不是谬误

真实阴谋会用保密和误导掩盖，所以单一反证不一定推翻；仍需可检验预测、独立证据和可失败条件。

### 容易混淆

self-sealing、unfalsifiability、impossible expectation

### 相关条目

自我封闭论证 (`self-sealing-argument`)、不可证伪性 (`unfalsifiability`)、不可能证据标准 (`impossible-expectation`)


---

## 谁受益谁策划

**Cui Bono Fallacy** · `cui-bono-fallacy`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：利益归因谬误、得利即有罪

### 定义

仅因某人或组织从事件中获益，就推出他们策划了事件，没有证明能力、动机、行动和因果链。

### 推理式

```text
事件 E 发生；A 从 E 获益；因此 A 导致 E。
```

### 诊断问题

1. 有多少无关方也从事件获益？
2. A 是否有能力、机会和实际行动证据？
3. 其他原因是否更常见或更有证据？

### 原创例子

> 事故后竞争对手销量上升，所以事故一定是竞争对手制造的。

### 何时可能不是谬误

利益可以提示调查方向，尤其结合通信、资金或行动证据时；但动机不等于实施。

### 容易混淆

appeal to motive、false cause、scapegoating

### 相关条目

诉诸动机 (`appeal-to-motive`)、虚假因果 (`false-cause`)、替罪羊归因 (`scapegoating`)


---

## 模式聚类错觉

**Clustering Illusion** · `pattern-clustering-illusion`

- 类型：非形式谬误
- 默认影响：中等
- 别名：随机聚类当信号、随机聚类误读、聚簇过度解释

### 定义

从本可由随机过程产生的聚簇、重复或序列中看出有意义的模式。

### 推理式

```text
随机数据出现聚簇 C；观察者寻找 C；因此断言背后有非随机机制。
```

### 诊断问题

1. 该聚簇在同等随机数据中有多常见？
2. 是否只因为聚簇醒目才注意到它？
3. 事先是否预测了它的位置和时间？

### 原创例子

> 地图上几个相邻街区病例较多，便断言存在秘密污染源，而未检查样本规模和随机波动。

### 何时可能不是谬误

聚簇也可能是真实信号；需要统计模型、先验假设和独立复核。

### 容易混淆

Texas sharpshooter、apophenia、anomaly hunting

### 相关条目

德州神枪手谬误 (`texas-sharpshooter`)、异常猎取 (`anomaly-hunting`)、模式幻觉 (`apophenia`)


---

## 重大事件必有大原因

**Proportionality Bias** · `proportionality-bias`

- 类型：非形式谬误
- 默认影响：中等
- 别名：大事件必有幕后大手、规模匹配偏误

### 定义

因为事件影响巨大，就推测其原因也必须同样巨大且通常是有意策划的。

### 推理式

```text
结果 R 很大；因此原因 C 必须宏大且有意；忽略小触发、系统放大和复杂反馈。
```

### 诊断问题

1. 小规模触发是否能通过系统反馈放大？
2. 自然、组织和技术因素能否共同产生巨大结果？
3. “必须有一个大人物”是否有独立证据？

### 原创例子

> 一场巨大金融波动看起来“不可能只是巧合”，所以必定由某个秘密集团操纵。

### 何时可能不是谬误

大规模结果有时确实由集中权力造成；需比较结构性解释与有意策划解释。

### 容易混淆

intentionality bias、single cause、conspiracy reasoning

### 相关条目

意向性偏差 (`intentionality-bias`)、单一原因谬误 (`single-cause`)、因果过度简化 (`causal-oversimplification`)


---

## 阴谋动机推定

**Conspiratorial Motive Inference** · `conspiratorial-motive-inference`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：他们肯定想做、动机替代行动证据

### 定义

从不透明行为、潜在收益或价值观猜测动机，再把猜测当成证明实际协调行动的证据。

### 推理式

```text
A 可能希望 R；因此 A 策划了 R；因此阴谋得到确认。
```

### 诊断问题

1. 动机是否被独立证实？
2. 是否有协调、资源、行动和时间线证据？
3. 为何其他有同样动机的人没有行动？

### 原创例子

> 这家公司可能从监管放松中获益，所以它肯定秘密写好了整套法规。

### 何时可能不是谬误

调查常从动机与受益开始，因为它们是假设来源；但仅凭动机不能证明行动。

### 容易混淆

cui bono、appeal to motive、intentionality bias

### 相关条目

谁受益谁策划 (`cui-bono-fallacy`)、诉诸动机 (`appeal-to-motive`)、意向性偏差 (`intentionality-bias`)


---

## 假旗预设

**False-Flag Assumption** · `false-flag-assumption`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：一切都是自导自演、反证式假旗

### 定义

在没有具体证据时，把事件解释成相关方自导自演，以便因此否定本来不利的信息。

### 推理式

```text
事件 E 不利立场 P；声称 P 的对手制造 E 来陷害；因此 E 不能反驳 P。
```

### 诊断问题

1. 是否有行动者、通信、资金或操作证据？
2. 该解释是否只是为了保护原立场而临时生成？
3. 正式调查和竞争解释提供了什么证据？

### 原创例子

> 任何针对某公司的可靠指控都被说成竞争对手伪造证据，但没有任何伪造线索。

### 何时可能不是谬误

假旗行动在历史上有案例，不能先验否认；每个具体主张仍需同样严格的证据。

### 容易混淆

unfalsifiable conspiracy、appeal to motive、self-sealing

### 相关条目

不可证伪阴谋解释 (`unfalsifiable-conspiracy`)、阴谋动机推定 (`conspiratorial-motive-inference`)、自我封闭论证 (`self-sealing-argument`)


---

## 正反都赢

**Heads-I-Win-Tails-You-Lose** · `heads-i-win-tails-you-lose`

- 类型：修辞模式
- 默认影响：高影响
- 别名：双向验证、结果全被吸收

### 定义

无论结果朝哪个方向，都解释成自己正确或对方错误，使主张免于任何失败风险。

### 推理式

```text
预测 P；若 P 出现则宣称对；若非 P 出现则称对方作弊或掩盖；因此仍宣称对。
```

### 诊断问题

1. 哪一种结果会被承认为失败？
2. 对成功和失败的解释是否事先对称？

### 原创例子

> 如果调查认定无问题，说明它们是一伙的；如果认定有问题，说明我早就说对了。

### 何时可能不是谬误

解释复杂世界时可以有后备假设；但后备假设必须有独立成本和可检验内容。

### 容易混淆

self-sealing、unfalsifiability、special pleading

### 相关条目

自我封闭论证 (`self-sealing-argument`)、不可证伪阴谋解释 (`unfalsifiable-conspiracy`)、移动球门 (`moving-the-goalposts`)


---

## 证据缺失推演

**Absence-of-Evidence Reasoning** · `absence-of-evidence`

- 类型：非形式谬误
- 默认影响：中等
- 别名：没找到所以不存在、没证据所以有证据

### 定义

把“没有发现证据”解释成“已经证明不存在”或“正说明被隐藏”，而不说明搜查范围、方法和基线概率。

### 推理式

```text
在有限范围内未发现 E；因此 P 为假，或因此 P 的隐藏得到确认。
```

### 诊断问题

1. 如果 P 为真，我们有多大机会找到 E？
2. 搜查是否覆盖关键地点、时间和方法？
3. 基线中本来就难以找到的证据有多少？

### 原创例子

> 档案里没找到那段通信，所以通信肯定被删了，从而证明阴谋存在。

### 何时可能不是谬误

在证据本应常见且搜索充分的领域，缺失可以显著降低概率；关键在于可发现性。

### 容易混淆

appeal to ignorance、appeal to silence、unfalsifiable conspiracy

### 相关条目

诉诸无知 (`appeal-to-ignorance`)、诉诸沉默 (`appeal-to-silence`)、不可证伪阴谋解释 (`unfalsifiable-conspiracy`)


---

## 历史学家谬误

**Historian's Fallacy** · `historians-fallacy`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：后见判断历史、用今天信息审判过去

### 定义

用后来才获得的信息和结果，判断过去行动者在当时是否本应轻易预见，并忽略其真实信息环境。

### 推理式

```text
决策 D 在时间 t 基于信息 I_t 作出；分析者用后来信息 I_t+ 评判；因此 D 当时显然错误。
```

### 诊断问题

1. 决策时实际可获得哪些信息和选项？
2. 后来的结果是概率性后果还是当时已知的确定事实？

### 原创例子

> 用今天才知道的故障原因，断言当年的工程师“显然”忽略了所有线索。

### 何时可能不是谬误

历史行动者仍需对当时可合理获得的信息、预警和流程负责；后见信息可以用于学习而非直接定罪。

### 容易混淆

后见之明偏差、结果偏差、事后归因

### 相关条目

后见之明偏差 (`hindsight-bias`)、结果偏差 (`outcome-bias`)、事后归因 (`post-hoc`)


---

## 小人谬误

**Homunculus Fallacy** · `homunculus-fallacy`

- 类型：非形式谬误
- 默认影响：中等
- 别名：内部小人解释、解释者回归、用能力解释能力

### 定义

用内部小主体或同一能力来解释待解释现象，使解释只是把问题缩小或复制，没有给出更基本机制。

### 推理式

```text
现象 X 需要解释；内部实体 H 具有 X 能力；因此 X 得到解释。
```

### 诊断问题

1. 内部实体的机制是否比原现象更清楚？
2. 解释是否把同一问题原样复制到更小层级？
3. 能否指出可观察步骤而不是再假设一个执行者？

### 原创例子

> 人为什么能理解语言？因为大脑里有一个小翻译官能理解所有语言。

### 何时可能不是谬误

多主体模型和简化执行者可以是计算或教学工具；只要进一步说明其操作步骤，就不必构成循环解释。

### 容易混淆

循环论证、具体化谬误、心智投射谬误

### 相关条目

循环论证 (`circular-reasoning`)、具体化谬误 (`reification`)、心智投射谬误 (`mind-projection-fallacy`)


---

## 隐秘动机谬误

**Furtive Fallacy** · `furtive-fallacy`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：恶意决策推定、结果反推阴谋

### 定义

因为出现了坏结果，就推定决策者必然出于隐秘、恶意或操纵动机，而没有先比较无能、误判、制度约束和偶然因素。

### 推理式

```text
结果 R 很坏；因此某人必然暗中想让 R 发生；未提供意图、通信或行动证据。
```

### 诊断问题

1. 除恶意意图外，有哪些非意图或制度性解释？
2. 决策者当时的信息、能力和激励是什么？
3. 是否存在能区分疏忽与故意行为的具体证据？

### 原创例子

> 系统发生重大故障，所以管理层一定早就知道并故意隐瞒，而不是存在未发现的测试缺口。

### 何时可能不是谬误

有会议记录、刻意销毁证据或重复隐瞒时，意图假设可以成立；问题是从坏结果直接跳到恶意内心。

### 容易混淆

诉诸动机、阴谋动机推定、意图性偏差

### 相关条目

阴谋动机推定 (`conspiratorial-motive-inference`)、诉诸动机 (`appeal-to-motive`)、意向性偏差 (`intentionality-bias`)


---

## 心理学家谬误

**Psychologist's Fallacy** · `psychologists-fallacy`

- 类型：非形式谬误
- 默认影响：中等
- 别名：观察者知识投射、把自己的理解当作对象状态

### 定义

分析者把自己已经知道的信息、概念或反应，直接当成被观察者在当时也拥有或正在经历的状态。

### 推理式

```text
观察者 O 知道 X；因此被观察者 A 在情境中也必然知道或体验到 X。
```

### 诊断问题

1. 被观察者在当时实际接触到哪些信息？
2. 观察者使用了哪些后来才获得的概念？
3. 能否区分文本表达、读者反应和作者意图？

### 原创例子

> 现代读者一眼看出这段诗在写失去，所以诗人写作时一定清楚自己在表达这种心理状态。

### 何时可能不是谬误

解释者需要理解行动者的理由，但也能指出行动者未意识到的结构；问题是把分析者的知识直接替代对象的视角。

### 容易混淆

历史学家谬误、心智投射谬误、意图谬误

### 相关条目

历史学家谬误 (`historians-fallacy`)、心智投射谬误 (`mind-projection-fallacy`)、后见之明偏差 (`hindsight-bias`)


[返回分类索引](../catalog-index.md)
