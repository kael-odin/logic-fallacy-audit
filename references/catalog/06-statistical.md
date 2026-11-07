# 统计、概率与样本

**Statistics, Probability, and Sampling**

误解基准率、条件概率、样本选择、变异性或检验过程。

> 使用提示：明确分母、样本来源、比较对象和不确定性。

> 本文件由结构化目录生成。修改 `catalog/` 后再运行 `python scripts/fallacy_cli.py render`。

共 **23** 条。

## 快速索引

| 中文名 | English | ID |
|---|---|---|
| 基准率忽视 | Base Rate Neglect | `base-rate-neglect` |
| 合取谬误 | Conjunction Fallacy | `conjunction-fallacy` |
| 检察官谬误 | Prosecutor's Fallacy | `prosecutors-fallacy` |
| 辩护律师谬误 | Defense Attorney's Fallacy | `defense-attorneys-fallacy` |
| 逆概率谬误 | Inverse Fallacy | `inverse-fallacy` |
| 分母忽视 | Denominator Neglect | `denominator-neglect` |
| 选择偏差 | Selection Bias | `selection-bias` |
| 抽样偏差 | Sampling Bias | `sampling-bias` |
| 幸存者偏差 | Survivorship Bias | `survivorship-bias` |
| 樱桃挑选 | Cherry Picking | `cherry-picking` |
| 德州神枪手谬误 | Texas Sharpshooter Fallacy | `texas-sharpshooter` |
| 多重比较问题 | Multiple Comparisons Problem | `multiple-comparisons` |
| P 值操纵 | P-Hacking | `p-hacking` |
| 误导性平均值 | Misleading Average | `misleading-average` |
| 虚假精确 | False Precision | `false-precision` |
| 生态谬误 | Ecological Fallacy | `ecological-fallacy` |
| 零结果谬误 | Null Result Fallacy | `null-result-fallacy` |
| 统计显著性谬误 | Statistical Significance Fallacy | `statistical-significance-fallacy` |
| 麦克纳马拉谬误 | McNamara Fallacy | `mcnemara-fallacy` |
| 辛普森悖论陷阱 | Simpson's Paradox Trap | `simpsons-paradox` |
| 重复计数 | Double Counting | `double-counting` |
| 逆赌徒谬误 | Inverse Gambler's Fallacy | `inverse-gamblers-fallacy` |
| 游戏谬误 | Ludic Fallacy | `ludic-fallacy` |

---

## 基准率忽视

**Base Rate Neglect** · `base-rate-neglect`

- 类型：统计推理
- 默认影响：高影响
- 别名：忽略先验概率、基础比率谬误

### 定义

只关注个案特征或测试结果，忽略该事件在总体中的原始发生率，导致概率判断严重偏高或偏低。

### 推理式

```text
观察到特征 E；忽略 P(P) 和总体分布；因此高估 P(P|E)。
```

### 诊断问题

1. 目标事件在没有该证据时的总体发生率是多少？
2. 检测的假阳性和假阴性率是什么？

### 原创例子

> 某种病在人群中极罕见，但一次阳性检测就被理解为几乎确诊。

### 何时可能不是谬误

基准率并非永远压过个案证据；精确评估应结合敏感度、特异度和先验概率。

### 容易混淆

representativeness heuristic、inverse fallacy、prosecutor's fallacy

### 相关条目

逆概率谬误 (`inverse-fallacy`)、代表性启发 (`representativeness-heuristic`)、生动性误导 (`misleading-vividness`)


---

## 合取谬误

**Conjunction Fallacy** · `conjunction-fallacy`

- 类型：统计推理
- 默认影响：中等
- 别名：细节越多越可信、联合事件概率误判

### 定义

认为一个包含更多细节的合取事件比其单个组成事件更可能，因为故事更连贯。

### 推理式

```text
P(P 且 Q) 被判断为大于 P(P)，违反概率论中合取不超过单项的规则。
```

### 诊断问题

1. 结论要求同时发生几件事？
2. 细节增加是否提高了可信感，却降低了先验概率？

### 原创例子

> 她更可能是“关心环保的银行柜员”，而不是“银行柜员”。

### 何时可能不是谬误

现实判断可能把不同描述解释为不同证据集合；只有按同一事件空间概率比较时才构成谬误。

### 容易混淆

representativeness、story bias、conjunction probability

### 相关条目

代表性启发 (`representativeness-heuristic`)、基准率忽视 (`base-rate-neglect`)、虚假精确 (`false-precision`)


---

## 检察官谬误

**Prosecutor's Fallacy** · `prosecutors-fallacy`

- 类型：统计推理
- 默认影响：高影响
- 别名：条件概率颠倒、罕见匹配即定罪

### 定义

把“在无罪条件下出现证据的概率”误当成“在出现证据条件下无罪的概率”，忽略先验概率和对照人群。

### 推理式

```text
P(E|I) 很小；因此 P(I|E) 很小或接近零。
```

### 诊断问题

1. 两个条件概率分别是什么？
2. 总体中有多少人也会匹配该证据？
3. 先验概率是否被纳入？

### 原创例子

> 匹配概率只有百万分之一，所以被告有罪的概率是 99.9999%。

### 何时可能不是谬误

若总体规模、先验和其他证据被正确纳入，匹配证据可以很强；错误在于颠倒条件方向。

### 容易混淆

base rate、inverse fallacy、defense attorney fallacy

### 相关条目

逆概率谬误 (`inverse-fallacy`)、基准率忽视 (`base-rate-neglect`)、辩护律师谬误 (`defense-attorneys-fallacy`)


---

## 辩护律师谬误

**Defense Attorney's Fallacy** · `defense-attorneys-fallacy`

- 类型：统计推理
- 默认影响：高影响
- 别名：错误强调无辜匹配人数、忽略证据概率

### 定义

因为总体中有很多人也匹配某项证据，就断言该证据对具体案件毫无证明力，忽略其他证据组合与条件概率。

### 推理式

```text
很多无辜者也能匹配 E；因此 E 不能提高有罪概率。
```

### 诊断问题

1. 证据是否与其他独立信息组合？
2. 匹配在嫌疑组和总体中的相对比例是多少？
3. 先验和条件概率是否被正确比较？

### 原创例子

> 城市里有一百个人鞋码相同，所以现场鞋印不能作为任何证据。

### 何时可能不是谬误

单一弱证据可能不足以定罪；但“单独不充分”不等于“概率上完全不提供信息”。

### 容易混淆

prosecutor's fallacy、base rate、weak evidence

### 相关条目

检察官谬误 (`prosecutors-fallacy`)、逆概率谬误 (`inverse-fallacy`)、基准率忽视 (`base-rate-neglect`)


---

## 逆概率谬误

**Inverse Fallacy** · `inverse-fallacy`

- 类型：统计推理
- 默认影响：高影响
- 别名：条件概率倒置、P(A\|B)=P(B\|A)

### 定义

错误地认为 P(A|B) 与 P(B|A) 相同，忽视两者的基准率不同。

### 推理式

```text
已知 P(B|A)；因此直接推出 P(A|B) 等于同一数值。
```

### 诊断问题

1. 两个条件事件分别是什么？
2. P(A) 与 P(B) 的基准率是否不同？

### 原创例子

> 大多数骗子会紧张，所以紧张的人大多数是骗子。

### 何时可能不是谬误

当 P(A)=P(B) 且概率对称时，两者可以相等；但这需要额外条件。

### 容易混淆

prosecutor's fallacy、base-rate neglect、conditional probability

### 相关条目

检察官谬误 (`prosecutors-fallacy`)、辩护律师谬误 (`defense-attorneys-fallacy`)、基准率忽视 (`base-rate-neglect`)


---

## 分母忽视

**Denominator Neglect** · `denominator-neglect`

- 类型：统计推理
- 默认影响：中等
- 别名：只看绝对数、总数比较错误

### 定义

比较事件数量时忽略总体规模或暴露人数，导致对风险和比例的误判。

### 推理式

```text
A 组事件数大于 B 组；因此 A 组风险更高；忽略两组的样本量。
```

### 诊断问题

1. 事件数对应的总人数、总交易数或总时长是多少？
2. 比较的是绝对数、比例还是率？

### 原创例子

> 大城市事故更多，所以大城市比小城市更危险。

### 何时可能不是谬误

绝对数对资源规划很重要；风险比较则需要分母，两者可以并存。

### 容易混淆

base rate、misleading average、raw count bias

### 相关条目

基准率忽视 (`base-rate-neglect`)、误导性平均值 (`misleading-average`)、选择偏差 (`selection-bias`)


---

## 选择偏差

**Selection Bias** · `selection-bias`

- 类型：统计推理
- 默认影响：高影响
- 别名：样本选择偏差、自选样本

### 定义

样本进入分析的过程与目标结论相关，使观察到的结果不能代表总体。

### 推理式

```text
样本 S 的选择条件 C 与结果 Y 相关；分析把 S 当成随机代表总体。
```

### 诊断问题

1. 谁被纳入、谁被排除？
2. 选择机制是否与结果变量相关？
3. 缺失样本会怎样改变结论？

### 原创例子

> 只向已购用户发满意度调查，然后把结果当成所有潜在用户评价。

### 何时可能不是谬误

不是所有非随机样本都无效；需要说明选择机制是否足以扭曲目标推断。

### 容易混淆

sampling bias、survivorship bias、response bias

### 相关条目

幸存者偏差 (`survivorship-bias`)、草率概括 (`hasty-generalization`)、相关即因果 (`cum-hoc`)


---

## 抽样偏差

**Sampling Bias** · `sampling-bias`

- 类型：统计推理
- 默认影响：高影响
- 别名：不代表性样本、抽样框错误

### 定义

抽取样本的方法系统性偏向某些群体，使样本分布与目标总体不同。

### 推理式

```text
从框架 F 中抽取 S；F 或抽取规则排除与结论相关的群体；因此总体估计失真。
```

### 诊断问题

1. 抽样框覆盖了谁，漏掉了谁？
2. 接触和自愿参与机制是否偏向某类回答？

### 原创例子

> 只在白天电话调查在职人员，然后推断全体居民对夜间政策的意见。

### 何时可能不是谬误

配额、加权和分层可纠正部分偏差；但无法弥补完全缺失的群体。

### 容易混淆

selection bias、response bias、small sample

### 相关条目

选择偏差 (`selection-bias`)、幸存者偏差 (`survivorship-bias`)、虚假共识偏差 (`false-consensus-bias`)


---

## 幸存者偏差

**Survivorship Bias** · `survivorship-bias`

- 类型：统计推理
- 默认影响：高影响
- 别名：只看到成功者、失败样本消失

### 定义

只分析通过筛选、仍在运行或留下记录的样本，忽略已经失败、退出或不可见的样本。

### 推理式

```text
只观察到幸存集合 S；据此推断所有尝试的规律；失败集合 F 未进入分母。
```

### 诊断问题

1. 谁已经退出、失败或未被记录？
2. 成功样本的共同特征是否在失败样本中也同样常见？

### 原创例子

> 研究所有成功企业后，发现它们都敢冒险，于是说冒险导致成功。

### 何时可能不是谬误

幸存样本有时是唯一可观察数据；需要明确边界并用额外方法估计缺失部分。

### 容易混淆

selection bias、survivorship、appeal to wealth

### 相关条目

选择偏差 (`selection-bias`)、抽样偏差 (`sampling-bias`)、诉诸财富 (`appeal-to-wealth`)


---

## 樱桃挑选

**Cherry Picking** · `cherry-picking`

- 类型：统计推理
- 默认影响：高影响
- 别名：只挑有利数据、挑选结果

### 定义

从大量数据中只选择支持结论的部分，不按预先一致规则报告全部分析或时间区间。

### 推理式

```text
从数据集 D 中挑选 D+ 支持 P；忽略 D− 和总体基准；因此宣称 P 获数据支持。
```

### 诊断问题

1. 时间区间、变量和排除标准是否在分析前确定？
2. 不利数据是否也被报告？
3. 如果把选择规则用于反方，会产生什么结果？

### 原创例子

> 展示产品增长最好的三个月，却不显示其余月份持续下降。

### 何时可能不是谬误

针对性分析可以合理聚焦问题；但必须说明选择依据，并避免把事后选择当预注册检验。

### 容易混淆

selective evidence、card stacking、p-hacking

### 相关条目

选择性举证 (`selective-evidence`)、堆牌说服 (`card-stacking`)、P 值操纵 (`p-hacking`)


---

## 德州神枪手谬误

**Texas Sharpshooter Fallacy** · `texas-sharpshooter`

- 类型：统计推理
- 默认影响：高影响
- 别名：先射箭后画靶、事后聚类

### 定义

先观察随机数据中的模式，再围绕该模式定义假设或边界，使结果看起来像事先预测成功。

### 推理式

```text
在数据 D 中发现区域 R 有模式；事后把假设限定为 R；因此宣称高准确率。
```

### 诊断问题

1. 假设和分组是否在看见结果前确定？
2. 若随机生成同样数据，最显眼的聚类可能有多大？

### 原创例子

> 在地图上圈出癌症最多的几个街区，然后宣称该圈是预测中的高风险区。

### 何时可能不是谬误

探索性分析是合法研究阶段；问题在于把事后发现直接当成验证性证据。

### 容易混淆

multiple comparisons、p-hacking、post hoc

### 相关条目

多重比较问题 (`multiple-comparisons`)、P 值操纵 (`p-hacking`)、樱桃挑选 (`cherry-picking`)


---

## 多重比较问题

**Multiple Comparisons Problem** · `multiple-comparisons`

- 类型：统计推理
- 默认影响：高影响
- 别名：多重检验、反复测试必出显著

### 定义

进行很多假设检验后，只报告偶然达到显著的结果，却不校正整体错误率。

### 推理式

```text
同时检验 H1…Hn；在未校正情况下挑出 p<0.05 的 Hk；因此宣称发现真实效应。
```

### 诊断问题

1. 一共测试了多少假设、亚组和终点？
2. 是否预先指定主分析并做多重比较校正？

### 原创例子

> 比较几十种颜色与转化率，只报告唯一达到显著的一种。

### 何时可能不是谬误

多重检验校正不是机械门槛；探索性发现可用于提出新假设，但不能冒充确认性证据。

### 容易混淆

p-hacking、Texas sharpshooter、cherry-picking

### 相关条目

P 值操纵 (`p-hacking`)、德州神枪手谬误 (`texas-sharpshooter`)、樱桃挑选 (`cherry-picking`)


---

## P 值操纵

**P-Hacking** · `p-hacking`

- 类型：统计推理
- 默认影响：高影响
- 别名：数据挖掘到显著、规格搜索

### 定义

反复尝试不同分组、协变量、排除标准或停止规则，直到获得统计显著，再把选择过程隐藏。

### 推理式

```text
测试多种分析规格 A1…An；选择 p 值最小且符合叙事的结果；报告为单一确认性检验。
```

### 诊断问题

1. 分析规格是否事先固定？
2. 是否因结果而决定继续采样、排除异常或更换指标？

### 原创例子

> 不断添加控制变量，直到目标变量显著，然后只报告最终模型。

### 何时可能不是谬误

数据探索和模型调整可以合理；关键是披露全部尝试，并用独立数据验证。

### 容易混淆

multiple comparisons、cherry-picking、Texas sharpshooter

### 相关条目

多重比较问题 (`multiple-comparisons`)、樱桃挑选 (`cherry-picking`)、德州神枪手谬误 (`texas-sharpshooter`)


---

## 误导性平均值

**Misleading Average** · `misleading-average`

- 类型：统计推理
- 默认影响：中等
- 别名：平均数掩盖分布、均值误读

### 定义

用单一平均数或中位数概括高度偏斜、异质或多峰的分布，掩盖大多数人的实际状况。

### 推理式

```text
分布 D 高度偏斜；报告均值 M；因此推断典型个体接近 M。
```

### 诊断问题

1. 分布的形状、分位数和极值是什么？
2. 目标是总额、典型值还是特定群体？

### 原创例子

> 某公司平均奖金十万元，但大多数员工只拿到一千元，少数高管拿走大部分。

### 何时可能不是谬误

均值在比较总量和期望值时可能合适；错误在于把它解释成典型个案。

### 容易混淆

denominator neglect、ecological fallacy、type-token confusion

### 相关条目

分母忽视 (`denominator-neglect`)、生态谬误 (`ecological-fallacy`)、类型与个例混淆 (`type-token-confusion`)


---

## 虚假精确

**False Precision** · `false-precision`

- 类型：统计推理
- 默认影响：中等
- 别名：伪精确、小数位超过数据质量

### 定义

给不确定、粗略或主观估计加上过多小数位或精确数字，使受众高估其可靠性。

### 推理式

```text
数据只有粗略范围；论证报告精确值 X.XX%；因此产生不应有的确定感。
```

### 诊断问题

1. 原始测量的误差和有效数字是多少？
2. 精确数字是否来自估计、模型或任意权重？

### 原创例子

> 根据未经验证的模型，项目成功率是 87.436%。

### 何时可能不是谬误

计算中可保留高精度中间值；最终沟通应与数据不确定性和决策需要一致。

### 容易混淆

false precision bias、overconfidence、scientific notation

### 相关条目

误导性平均值 (`misleading-average`)、基准率忽视 (`base-rate-neglect`)、过度自信偏差 (`overconfidence-bias`)


---

## 生态谬误

**Ecological Fallacy** · `ecological-fallacy`

- 类型：统计推理
- 默认影响：高影响
- 别名：群体平均推个体、地区数据误推个人

### 定义

从群体层面的统计关系推断个体层面的关系，而群体内部可能存在巨大异质性。

### 推理式

```text
群体 G 的平均 X 与平均 Y 相关；因此每个个体 g 的 X 与 Y 也相关。
```

### 诊断问题

1. 数据和结论处于同一个人群层次吗？
2. 群体内部是否存在相反关系或高方差？

### 原创例子

> 某地区平均收入高且平均寿命长，所以住在这里的每个富人都更长寿。

### 何时可能不是谬误

群体层结论本身可以合法；错误发生在把群体模式直接下推到个体。

### 容易混淆

division、collective-distributive、misleading average

### 相关条目

分割谬误 (`division`)、集体与个体混淆 (`collective-distributive`)、辛普森悖论陷阱 (`simpsons-paradox`)


---

## 零结果谬误

**Null Result Fallacy** · `null-result-fallacy`

- 类型：统计推理
- 默认影响：中等
- 别名：不显著即无效、没有差异等于相同

### 定义

把统计上未达到显著或不显著差异，解释为已经证明没有效应。

### 推理式

```text
检验未发现显著差异；因此效应为零。
```

### 诊断问题

1. 置信区间跨度有多大？
2. 样本量是否足以检测目标效应？
3. 研究是否有足够统计功效？

### 原创例子

> 小样本试验没有显示差异，于是宣称两种治疗完全相同。

### 何时可能不是谬误

不显著可以表明证据不足或效应不太可能很大；不能自动证明精确等价。

### 容易混淆

statistical significance、absence of evidence、power failure

### 相关条目

统计显著性谬误 (`statistical-significance-fallacy`)、证据缺失推演 (`absence-of-evidence`)、诉诸无知 (`appeal-to-ignorance`)


---

## 统计显著性谬误

**Statistical Significance Fallacy** · `statistical-significance-fallacy`

- 类型：统计推理
- 默认影响：高影响
- 别名：p 值即效果、显著即重要

### 定义

把“统计显著性”当作效应很大、现实重要或假设为真的充分证据，忽略效应量、不确定性和模型假设。

### 推理式

```text
p<0.05；因此效应重要、解释正确或可推广。
```

### 诊断问题

1. 效应量和置信区间是多少？
2. 研究设计、模型假设和多重比较是否可靠？
3. 统计显著对现实决策意味着什么？

### 原创例子

> 新药只让指标改善 0.1%，但因为样本巨大而显著，所以被说成重大突破。

### 何时可能不是谬误

统计显著可以是一个有用信号；问题在于赋予它超过定义范围的含义。

### 容易混淆

p-hacking、null result、effect size

### 相关条目

零结果谬误 (`null-result-fallacy`)、P 值操纵 (`p-hacking`)、虚假精确 (`false-precision`)


---

## 麦克纳马拉谬误

**McNamara Fallacy** · `mcnemara-fallacy`

- 类型：非形式谬误
- 默认影响：中等
- 别名：只量化容易量化的、指标代替目标

### 定义

因为某项指标容易测量，就把它当作目标本身，忽略难以量化但同样重要的因素。

### 推理式

```text
目标 G 难测；指标 M 与 G 相关且易测；因此优化 M 被当成实现 G。
```

### 诊断问题

1. 指标是目标的代理还是目标本身？
2. 优化指标会产生哪些未测副作用？
3. 哪些重要因素因为难量化被忽略？

### 原创例子

> 用代码行数衡量生产力，导致员工写更多冗余代码。

### 何时可能不是谬误

量化能提高反馈和比较能力；关键是使用多指标并定期检查代理偏差。

### 容易混淆

surrogation、Goodhart's law、false precision

### 相关条目

虚假精确 (`false-precision`)、误导性平均值 (`misleading-average`)、幸存者偏差 (`survivorship-bias`)


---

## 辛普森悖论陷阱

**Simpson's Paradox Trap** · `simpsons-paradox`

- 类型：统计推理
- 默认影响：中等
- 别名：分组反转、总体趋势与子组相反

### 定义

总体数据与分组数据出现相反趋势时，忽略分组结构而直接解释总体关系。

### 推理式

```text
在总体中 A 与 B 正相关；在按关键变量分层后，各组内为负相关。
```

### 诊断问题

1. 是否存在影响分组比例的混杂变量？
2. 因果问题应在总体层还是分层层回答？

### 原创例子

> 两家医院总体死亡率看似不同，但按病情严重程度分组后，各层结论相反。

### 何时可能不是谬误

分层不一定越细越好，可能引入碰撞偏差；关键是明确目标因果结构和变量角色。

### 容易混淆

ecological fallacy、confounding、collider bias

### 相关条目

生态谬误 (`ecological-fallacy`)、选择偏差 (`selection-bias`)、误导性平均值 (`misleading-average`)


---

## 重复计数

**Double Counting** · `double-counting`

- 类型：统计推理
- 默认影响：高影响
- 别名：同一证据算两次、重叠样本重复汇总

### 定义

把同一事件、样本或收益在多个类别中重复相加，使证据量、概率或收益被系统性夸大。

### 推理式

```text
同一集合 S 同时被计入 A 与 B；论证把 |A|+|B| 当作独立总量，忽略重叠 |A∩B|。
```

### 诊断问题

1. 不同类别是否使用同一批人或事件？
2. 概率相加时是否可能超过 100%？
3. 收益是否已在成本或其他项目中计算过？

### 原创例子

> 一百名用户同时点赞两条帖子，却被报告为两百次独立用户支持。

### 何时可能不是谬误

互动次数和独立人数可以分别统计；问题在于分母和指标未说明，导致重复解释。

### 容易混淆

分母忽视、多重比较、平均数的误导

### 相关条目

分母忽视 (`denominator-neglect`)、多重比较问题 (`multiple-comparisons`)、误导性平均值 (`misleading-average`)


---

## 逆赌徒谬误

**Inverse Gambler's Fallacy** · `inverse-gamblers-fallacy`

- 类型：统计推理
- 默认影响：中等
- 别名：罕见结果反推多次尝试、逆赌徒、结果反推未观察试验

### 定义

从一次罕见结果推断此前已经发生大量未观察到的尝试，却没有给出试验次数、选择过程或先验证据。

### 推理式

```text
观察到罕见结果 R；因此 R 之前已有大量未观察试验 N。
```

### 诊断问题

1. 对试验次数 N 是否有直接证据？
2. 结果 R 在单次试验和多次试验模型下的概率各是多少？
3. 观察者是否只看到被选中的罕见案例？

### 原创例子

> 他第一次买彩票就中了大奖，所以之前肯定已经暗中买过成千上万次。

### 何时可能不是谬误

在已知抽样模型下，罕见观测可以更新对试验次数的概率判断；关键是先验、似然和选择机制。

### 容易混淆

赌徒谬误、多重比较、选择偏差

### 相关条目

赌徒谬误 (`gamblers-fallacy`)、多重比较问题 (`multiple-comparisons`)、选择偏差 (`selection-bias`)


---

## 游戏谬误

**Ludic Fallacy** · `ludic-fallacy`

- 类型：统计推理
- 默认影响：高影响
- 别名：封闭模型当开放世界、把概率游戏当现实、规则世界误推

### 定义

把受明确规则约束、概率分布已知的模型结果直接用于开放世界，忽略未知事件、规则变化和模型外风险。

### 推理式

```text
模型 M 在封闭规则下给出概率 P；现实属于开放系统；因此现实风险等于 P。
```

### 诊断问题

1. 模型边界是否覆盖了现实中的主要不确定来源？
2. 未知事件或反馈是否会改变分布本身？
3. 决策在模型失效时是否仍然稳健？

### 原创例子

> 过去十年数据算出最大损失，所以未来任何损失都不会超过这个数。

### 何时可能不是谬误

简化模型是必要工具，压力测试和情景分析也能改善决策；问题是把模型的已知范围误当成世界的全部范围。

### 容易混淆

虚假精确、不可能证据标准、过度自信偏差

### 相关条目

虚假精确 (`false-precision`)、不可能证据标准 (`impossible-expectation`)、过度自信偏差 (`overconfidence-bias`)


[返回分类索引](../catalog-index.md)
