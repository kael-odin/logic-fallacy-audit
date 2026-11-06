# 认知偏差

**Cognitive Biases**

影响判断的系统性倾向，不是逻辑谬误本身。

> 使用提示：只作为背景解释，不单独充当谬误结论。

> 本文件由结构化目录生成。修改 `catalog/` 后再运行 `python scripts/fallacy_cli.py render`。

共 **32** 条。

## 快速索引

| 中文名 | English | ID |
|---|---|---|
| 确认偏差 | Confirmation Bias | `confirmation-bias` |
| 我方偏差 | Myside Bias | `myside-bias` |
| 信念偏差 | Belief Bias | `belief-bias` |
| 可得性启发 | Availability Heuristic | `availability-heuristic` |
| 代表性启发 | Representativeness Heuristic | `representativeness-heuristic` |
| 锚定效应 | Anchoring Effect | `anchoring-effect` |
| 框架效应 | Framing Effect | `framing-effect` |
| 损失厌恶 | Loss Aversion | `loss-aversion` |
| 现状偏差 | Status Quo Bias | `status-quo-bias` |
| 沉没成本偏差 | Sunk Cost Bias | `sunk-cost-bias` |
| 内群体偏差 | In-Group Bias | `in-group-bias` |
| 光环效应 | Halo Effect | `halo-effect` |
| 尖角效应 | Horn Effect | `horn-effect` |
| 基本归因错误 | Fundamental Attribution Error | `fundamental-attribution-error` |
| 行动者—观察者偏差 | Actor-Observer Bias | `actor-observer-bias` |
| 自利偏差 | Self-Serving Bias | `self-serving-bias` |
| 后见之明偏差 | Hindsight Bias | `hindsight-bias` |
| 结果偏差 | Outcome Bias | `outcome-bias` |
| 负面偏差 | Negativity Bias | `negativity-bias` |
| 乐观偏差 | Optimism Bias | `optimism-bias` |
| 虚假共识偏差 | False Consensus Bias | `false-consensus-bias` |
| 过度自信偏差 | Overconfidence Bias | `overconfidence-bias` |
| 模式幻觉 | Apophenia | `apophenia` |
| 意向性偏差 | Intentionality Bias | `intentionality-bias` |
| 能动者侦测过度 | Hyperactive Agency Detection | `hyperactive-agency-detection` |
| 正常化偏差 | Normalcy Bias | `normalcy-bias` |
| 权威偏差 | Authority Bias | `authority-bias` |
| 从众偏差 | Bandwagon Bias | `bandwagon-bias` |
| 规划谬误 | Planning Fallacy | `planning-fallacy` |
| 作为与不作为偏差 | Omission Bias | `omission-bias` |
| 愿望思维 | Wishful Thinking | `wishful-thinking` |
| 公正世界假设 | Just-World Hypothesis | `just-world-hypothesis` |

---

## 确认偏差

**Confirmation Bias** · `confirmation-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：确认偏误、选择性注意

### 定义

更愿意寻找、注意、记住和解释支持既有信念的信息，忽略相反信息。

### 推理式

```text
已有信念 P；优先收集 E+；对 E− 设置更高审查门槛。
```

### 诊断问题

1. 是否主动寻找反例和最强异议？
2. 对支持和反对证据是否使用相同标准？

### 原创例子

> 只关注夸赞产品的评论，并把差评都解释成竞争对手。

### 何时可能不是谬误

偏差影响信息处理，但单个判断仍需看具体论证；不能仅凭结论方向断言确认偏差。

### 容易混淆

cherry-picking、myside bias、选择性举证

### 相关条目

樱桃挑选 (`cherry-picking`)、我方偏差 (`myside-bias`)、信念偏差 (`belief-bias`)


---

## 我方偏差

**Myside Bias** · `myside-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：立场偏差、阵营偏向

### 定义

因为信息支持自己的群体或既有立场，就更容易接受，即使个人并不预先有强烈信念。

### 推理式

```text
立场 S 属于我方；支持 S 的证据被快速接受；反对 S 的证据被严格审查。
```

### 诊断问题

1. 同一论证换到对方阵营是否仍被认为有效？
2. 我是否因为结论身份而调整门槛？

### 原创例子

> 自己团队提出的方案只讨论收益，竞争对手的相同方案却先被假定不可行。

### 何时可能不是谬误

熟悉领域和共享标准可能带来合理优势；需要比较具体论证而不是只给动机贴标签。

### 容易混淆

in-group bias、confirmation bias、special pleading

### 相关条目

确认偏差 (`confirmation-bias`)、内群体偏差 (`in-group-bias`)、特殊豁免 (`special-pleading`)


---

## 信念偏差

**Belief Bias** · `belief-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：结论可信度影响推理、可信结论更显有效

### 定义

因为结论听起来可信或不可信，而高估或低估论证的逻辑有效性。

### 推理式

```text
结论 C 符合既有信念；因此论证 A 被评为更有效；不考虑形式。
```

### 诊断问题

1. 把结论换成中性符号后，是否仍认为推理有效？
2. 我是在评价形式还是评价结论？

### 原创例子

> 因为结论“多睡觉有益”听起来合理，就接受一个结构无效的统计推理。

### 何时可能不是谬误

背景知识可帮助发现假前提；仍需分开形式有效性与事实真假。

### 容易混淆

confirmation bias、fallacy fallacy、wishful thinking

### 相关条目

确认偏差 (`confirmation-bias`)、我方偏差 (`myside-bias`)、谬误谬误 (`fallacy-fallacy`)


---

## 可得性启发

**Availability Heuristic** · `availability-heuristic`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：可用性偏差、易回忆即常见

### 定义

根据例子多容易被想起、想象或搜索到来判断事件频率和风险。

### 推理式

```text
事件 E 易于回忆；因此 E 被判断为更常见或更可能。
```

### 诊断问题

1. 我记得它是因为常见，还是因为媒体、情绪和近期曝光？
2. 实际频率数据是什么？

### 原创例子

> 连续看到坠机新闻后，高估航空事故而低估日常交通风险。

### 何时可能不是谬误

启发式能快速调用相关经验；高风险判断需要用数据校准。

### 容易混淆

misleading vividness、recency effect、base-rate neglect

### 相关条目

生动性误导 (`misleading-vividness`)、基准率忽视 (`base-rate-neglect`)、负面偏差 (`negativity-bias`)


---

## 代表性启发

**Representativeness Heuristic** · `representativeness-heuristic`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：像不像即概率、刻板相似判断

### 定义

根据某人或事件与某类典型形象的相似程度判断概率，忽略基准率和样本机制。

### 推理式

```text
对象 X 很像类别 C 的刻板形象；因此 X 很可能属于 C。
```

### 诊断问题

1. 类别 C 在总体中多常见？
2. 有哪些与形象相似无关的统计约束？

### 原创例子

> 某人安静爱读书，就判断他更像图书管理员而不是销售，而忽略职业总体人数。

### 何时可能不是谬误

典型特征有时包含诊断信息；需要与基准率和证据质量结合。

### 容易混淆

base-rate neglect、stereotyping、conjunction fallacy

### 相关条目

基准率忽视 (`base-rate-neglect`)、合取谬误 (`conjunction-fallacy`)、赌徒谬误 (`gamblers-fallacy`)


---

## 锚定效应

**Anchoring Effect** · `anchoring-effect`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：锚点偏差、先出现数字影响估计

### 定义

先出现的数字、报价或立场不会充分调整，成为后续估计的锚点，即使它无关或任意。

### 推理式

```text
先看到数值 A；之后估计 X，结果过度接近 A。
```

### 诊断问题

1. 估计前是否看到无关初始值？
2. 从独立数据重新估算会得到什么？

### 原创例子

> 先看到原价 999 元，再看到 399 元，便觉得它比没有原价时更便宜。

### 何时可能不是谬误

锚点也可能含有效信息，尤其历史数据和合理参考值；需要检验独立依据。

### 容易混淆

framing effect、contrast effect、adjustment heuristic

### 相关条目

框架效应 (`framing-effect`)、现状偏差 (`status-quo-bias`)、损失厌恶 (`loss-aversion`)


---

## 框架效应

**Framing Effect** · `framing-effect`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：表述框架偏差、同事实不同选择

### 定义

同一信息因被表述为收益、损失、成功率或失败率而产生不同判断。

### 推理式

```text
事实 F 可以等值表述为 F1 或 F2；选择随表述改变。
```

### 诊断问题

1. 换成等值的相反框架后，我的判断是否改变？
2. 框架强调了哪些参照点？

### 原创例子

> “成功率 90%”与“失败率 10%”导致不同风险感受。

### 何时可能不是谬误

不同框架可以突出真实不同的参照点和价值；关键是信息是否等值。

### 容易混淆

framing manipulation、loss aversion、anchoring

### 相关条目

操纵性框架 (`framing-manipulation`)、损失厌恶 (`loss-aversion`)、锚定效应 (`anchoring-effect`)


---

## 损失厌恶

**Loss Aversion** · `loss-aversion`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：损失比收益更痛、避免损失偏向

### 定义

同等大小的损失通常比收益带来更强心理影响，导致过度保守或维持现状。

### 推理式

```text
方案 A 与 B 期望相当；损失框架 B 被更强回避；因此选择改变。
```

### 诊断问题

1. 收益和损失是否按同一尺度比较？
2. 不行动是否也有损失？

### 原创例子

> 为了避免小概率损失而放弃期望收益更高的长期方案。

### 何时可能不是谬误

损失厌恶反映真实风险承受和不对称后果；不能仅按心理偏差否定风险意识。

### 容易混淆

status quo bias、sunk cost、endowment effect

### 相关条目

现状偏差 (`status-quo-bias`)、沉没成本偏差 (`sunk-cost-bias`)、框架效应 (`framing-effect`)


---

## 现状偏差

**Status Quo Bias** · `status-quo-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：默认现状偏好、改变成本高估

### 定义

倾向于维持当前安排，因为改变需要行动、承担不确定性或偏离默认选项。

### 推理式

```text
选择现状 S 或改动 C；即使净收益相近，默认保留 S。
```

### 诊断问题

1. 如果从零开始，我还会选现状吗？
2. 不改变的成本是否被忽略？

### 原创例子

> 明知旧流程低效，却因为设置新流程麻烦而一直不换。

### 何时可能不是谬误

现状可能包含转换成本和既得协调价值；偏差判断需比较净效果。

### 容易混淆

loss aversion、appeal to status quo、omission bias

### 相关条目

损失厌恶 (`loss-aversion`)、诉诸现状 (`appeal-to-status-quo`)、作为与不作为偏差 (`omission-bias`)


---

## 沉没成本偏差

**Sunk Cost Bias** · `sunk-cost-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：已经投入影响继续决策

### 定义

让不可回收的过去投入影响当前选择，倾向继续以证明投入没有白费。

### 推理式

```text
已投入 C；继续 P 的当前净收益为负；却因 C 而继续。
```

### 诊断问题

1. 从今天开始看，继续需要什么新增成本，能得到什么新增收益？
2. 过去的投入是否因继续而变得可回收？

### 原创例子

> 项目已经证明需求不足，但团队因投入两年而继续追加预算。

### 何时可能不是谬误

过去投入可产生承诺、学习、声誉或资产价值；需把真实未来价值计入。

### 容易混淆

sunk cost fallacy、loss aversion、commitment bias

### 相关条目

沉没成本谬误 (`sunk-cost-fallacy`)、损失厌恶 (`loss-aversion`)、现状偏差 (`status-quo-bias`)


---

## 内群体偏差

**In-Group Bias** · `in-group-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：自己人偏向、群体偏爱

### 定义

更信任、更宽容或更愿帮助被视为“自己人”的成员，对外群体使用不同标准。

### 推理式

```text
A 属于内群体 G；A 的行为得到更有利解释；等效行为在外部群体受到更差评价。
```

### 诊断问题

1. 把双方身份互换后，我是否作出相同判断？
2. 是否对同行为使用不同证据门槛？

### 原创例子

> 同一错误在同事身上叫失误，在竞争对手那里叫恶意。

### 何时可能不是谬误

特殊关系可能产生真实的照顾义务和信任基础；仍需说明为何影响当前结论。

### 容易混淆

myside bias、halo effect、special pleading

### 相关条目

我方偏差 (`myside-bias`)、光环效应 (`halo-effect`)、特殊豁免 (`special-pleading`)


---

## 光环效应

**Halo Effect** · `halo-effect`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：单项优势扩散、正面总体印象

### 定义

因为某人在一个显著维度上优秀或受欢迎，就推测其在其他不相关维度也优秀。

### 推理式

```text
A 在特征 F 上正面；因此 A 在无关特征 G 上也正面。
```

### 诊断问题

1. F 和 G 是否有实证关联？
2. 我是否有独立的 G 证据？

### 原创例子

> 因为一个人演讲有魅力，就认为其财务判断也一定可靠。

### 何时可能不是谬误

某些能力之间可能真实相关；光环效应指未经检验的跨维度扩散。

### 容易混淆

horn effect、appeal to wealth、transfer

### 相关条目

尖角效应 (`horn-effect`)、诉诸财富 (`appeal-to-wealth`)、证言式背书 (`testimonial`)


---

## 尖角效应

**Horn Effect** · `horn-effect`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：负面印象扩散、一坏百坏

### 定义

因为某人在一个显著维度上表现差或不受欢迎，就推测其在其他不相关维度也都差。

### 推理式

```text
A 在特征 F 上负面；因此 A 在无关特征 G 上也负面。
```

### 诊断问题

1. 负面特征与当前能力或主张是否相关？
2. 是否有独立的 G 证据？

### 原创例子

> 他曾在某次发言中失礼，因此他的所有技术判断都不可信。

### 何时可能不是谬误

可靠性、诚信和专业能力可能存在真实联系；仍需针对维度说明。

### 容易混淆

halo effect、ad hominem、poisoning the well

### 相关条目

光环效应 (`halo-effect`)、人身攻击 (`ad-hominem-abusive`)、毒化井水 (`poisoning-the-well`)


---

## 基本归因错误

**Fundamental Attribution Error** · `fundamental-attribution-error`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：重人格轻情境、行为归因偏差

### 定义

解释他人行为时过度归因于性格、动机或能力，低估情境约束。

### 推理式

```text
A 做出行为 B；观察者归因为 A 的人格；忽略环境和角色压力。
```

### 诊断问题

1. 如果我在同样情境下会怎样？
2. 哪些制度、时间、资源和压力可能促成行为？

### 原创例子

> 员工迟到就判断其懒惰，不考虑交通中断和临时照护责任。

### 何时可能不是谬误

人格和选择确实影响行为；偏差在于系统性低估情境。

### 容易混淆

actor-observer bias、single cause、harshness bias

### 相关条目

单一原因谬误 (`single-cause`)、行动者—观察者偏差 (`actor-observer-bias`)、自利偏差 (`self-serving-bias`)


---

## 行动者—观察者偏差

**Actor-Observer Bias** · `actor-observer-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：自己看情境别人看人格、双向归因

### 定义

对自己的行为更强调情境，对他人的同类行为更强调性格。

### 推理式

```text
我失败因为环境；他失败因为能力。
```

### 诊断问题

1. 同一行为发生在自己身上时，我会怎么解释？
2. 我是否能看到对方的情境信息？

### 原创例子

> 自己迟到是因为交通，同事迟到是因为不守时。

### 何时可能不是谬误

自我和他人可获得的情境信息不同；偏差判断需比较证据可得性。

### 容易混淆

fundamental attribution error、self-serving bias、halo effect

### 相关条目

基本归因错误 (`fundamental-attribution-error`)、自利偏差 (`self-serving-bias`)、内群体偏差 (`in-group-bias`)


---

## 自利偏差

**Self-Serving Bias** · `self-serving-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：成功归己失败归环境、自利归因

### 定义

更把成功归因于自身能力，把失败归因于外部因素，以维护自尊和形象。

### 推理式

```text
成功 S 因我；失败 F 因别人或环境。
```

### 诊断问题

1. 成功和失败是否使用相同归因标准？
2. 是否有独立数据支持我的贡献比例？

### 原创例子

> 项目成功是领导有方，失败是市场突然变化。

### 何时可能不是谬误

外部因素和自身能力都可能真实作用；偏差在于系统性不对称。

### 容易混淆

actor-observer bias、egocentric bias、fundamental attribution error

### 相关条目

行动者—观察者偏差 (`actor-observer-bias`)、基本归因错误 (`fundamental-attribution-error`)、我方偏差 (`myside-bias`)


---

## 后见之明偏差

**Hindsight Bias** · `hindsight-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：早就知道、事后诸葛亮

### 定义

知道结果后高估自己事前预测到该结果的概率，并认为结果原本显而易见。

### 推理式

```text
结果 R 已知；回忆预测时把不确定性抹去；因此认为决策者本应轻易预见。
```

### 诊断问题

1. 结果出现前的记录和概率判断是什么？
2. 当时可获得的替代方案和不确定性有哪些？

### 原创例子

> 公司破产后，人们说商业模式一开始就很明显不行，却忽略当时同类公司大量成功。

### 何时可能不是谬误

后见评价可以揭示可改进流程；不能把结果本身当作过程合理性的唯一证据。

### 容易混淆

outcome bias、confirmation bias、post hoc

### 相关条目

结果偏差 (`outcome-bias`)、事后归因 (`post-hoc`)、过度自信偏差 (`overconfidence-bias`)


---

## 结果偏差

**Outcome Bias** · `outcome-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：只看结果评价决策、好结果等于好过程

### 定义

仅根据结果好坏评价决策质量，忽略当时信息、概率、风险和可选方案。

### 推理式

```text
决策 D 得到好结果 R；因此 D 过程正确；或坏结果则过程错误。
```

### 诊断问题

1. 决策当时可获得哪些信息和选项？
2. 同样过程在多次重复中会有什么结果分布？

### 原创例子

> 一次高风险赌博赚了大钱，于是把赌徒式决策当成优秀判断。

### 何时可能不是谬误

结果当然需要评估；问题是不能让它完全替代过程审查。

### 容易混淆

hindsight bias、resulting、self-serving bias

### 相关条目

后见之明偏差 (`hindsight-bias`)、过度自信偏差 (`overconfidence-bias`)、回归谬误 (`regression-fallacy`)


---

## 负面偏差

**Negativity Bias** · `negativity-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：坏消息权重更高、负性偏向

### 定义

负面信息、威胁和损失比同等强度的正面信息更容易吸引注意并影响判断。

### 推理式

```text
正负信息强度相当；负面信息被赋予更高权重。
```

### 诊断问题

1. 正负证据是否使用同样标准？
2. 威胁是否因情绪强度而被估计得更高？

### 原创例子

> 十条好评和一条差评中，只反复关注差评并推断产品整体很差。

### 何时可能不是谬误

负面信息有时具有更高诊断价值和风险预警意义；需要按影响和频率判断。

### 容易混淆

availability heuristic、loss aversion、appeal to fear

### 相关条目

可得性启发 (`availability-heuristic`)、损失厌恶 (`loss-aversion`)、诉诸恐惧 (`appeal-to-fear`)


---

## 乐观偏差

**Optimism Bias** · `optimism-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：坏结果不会轮到我、过度乐观

### 定义

低估自己遭遇负面事件或项目失败的概率，高估有利结果。

### 推理式

```text
基准风险 B 适用于群体；个人判断风险远低于 B；无具体依据。
```

### 诊断问题

1. 与自己相似的人实际失败率是多少？
2. 我的优势是否有可核验证据，而非愿望？

### 原创例子

> 知道多数创业公司失败，却认为自己项目几乎没有失败风险。

### 何时可能不是谬误

风险异质性真实存在，个体可因资源与经验不同而低于平均；需要证据。

### 容易混淆

planning fallacy、wishful thinking、overconfidence

### 相关条目

规划谬误 (`planning-fallacy`)、愿望思维 (`wishful-thinking`)、过度自信偏差 (`overconfidence-bias`)


---

## 虚假共识偏差

**False Consensus Bias** · `false-consensus-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：大家都和我一样、共识高估

### 定义

高估他人与自己持相同意见、行为或选择的比例，因为周围样本和自身视角过于显眼。

### 推理式

```text
我持 P；我周围多数人持 P；因此总体多数持 P。
```

### 诊断问题

1. 我的社交圈是否是总体代表样本？
2. 独立调查或投票数据是什么？

### 原创例子

> 朋友圈都在支持某观点，便认为“公众已经形成共识”。

### 何时可能不是谬误

群体规范可以影响行为；需要区分局部环境和总体分布。

### 容易混淆

appeal to popularity、in-group bias、representativeness

### 相关条目

诉诸流行 (`appeal-to-popularity`)、内群体偏差 (`in-group-bias`)、抽样偏差 (`sampling-bias`)


---

## 过度自信偏差

**Overconfidence Bias** · `overconfidence-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：高估准确率、确定性过高

### 定义

对自己判断的准确度、知识范围和预测能力评估过高，置信区间过窄。

### 推理式

```text
真实正确率 A；主观置信度 B>>A；仍未校准。
```

### 诊断问题

1. 过去同类判断的实际准确率是多少？
2. 我是否记录了置信度和校准结果？

### 原创例子

> 连续几次预测正确后，把下次判断说成几乎确定。

### 何时可能不是谬误

经验可能带来真实专长；过度自信要通过校准而非语气判断。

### 容易混淆

Dunning-Kruger、optimism bias、false precision

### 相关条目

乐观偏差 (`optimism-bias`)、虚假精确 (`false-precision`)、规划谬误 (`planning-fallacy`)


---

## 模式幻觉

**Apophenia** · `apophenia`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：无意义关联、强行看出规律

### 定义

在随机或无关信息中感知有意义的联系、规律或叙事。

### 推理式

```text
随机数据 D 中出现表面组合；观察者赋予意义 P；没有检验随机基线。
```

### 诊断问题

1. 同样模式在随机数据中出现的概率多大？
2. 模式是否在观察前被预测？

### 原创例子

> 从连续几天的数字中看出某种神秘规律，并据此预测下一步。

### 何时可能不是谬误

模式发现是科学和艺术的重要起点；需要独立验证和统计基线。

### 容易混淆

clustering illusion、pareidolia、pattern-seeking

### 相关条目

模式聚类错觉 (`pattern-clustering-illusion`)、异常猎取 (`anomaly-hunting`)、意向性偏差 (`intentionality-bias`)


---

## 意向性偏差

**Intentionality Bias** · `intentionality-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：结果都有人策划、过度归因意图

### 定义

倾向把事件解释成某人有意识设计的结果，即使它也可能由习惯、系统或偶然造成。

### 推理式

```text
观察结果 R；快速假设有人故意造成 R；不比较非意向机制。
```

### 诊断问题

1. 是否存在系统性、非意图或无行动者的解释？
2. 所谓意图是否有通信或行动证据？

### 原创例子

> 看到一组随机失败，就认为有人暗中故意破坏。

### 何时可能不是谬误

有意图的行为真实且常见；偏差在于不给非意向解释合理权重。

### 容易混淆

hyperactive agency detection、conspiratorial motive、reification

### 相关条目

能动者侦测过度 (`hyperactive-agency-detection`)、阴谋动机推定 (`conspiratorial-motive-inference`)、重大事件必有大原因 (`proportionality-bias`)


---

## 能动者侦测过度

**Hyperactive Agency Detection** · `hyperactive-agency-detection`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：过度寻找行动者、有动静就有人

### 定义

对模糊刺激快速推断存在有意图的行动者，以优先避免潜在威胁。

### 推理式

```text
模糊事件 E；可能有人/生物造成；因此判断有意行动者存在，而不先比较自然原因。
```

### 诊断问题

1. 自然或机制性原因能否解释？
2. 行动者假设是否有独立痕迹？

### 原创例子

> 夜里听到房屋声响，就立刻认定有人闯入，而不先考虑管道和风。

### 何时可能不是谬误

感知行动者的快速机制有安全价值；风险决策仍需证据。

### 容易混淆

intentionality bias、apophenia、agent detection

### 相关条目

意向性偏差 (`intentionality-bias`)、模式幻觉 (`apophenia`)、阴谋动机推定 (`conspiratorial-motive-inference`)


---

## 正常化偏差

**Normalcy Bias** · `normalcy-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：不会出大事、低估异常风险

### 定义

面对异常或潜在灾难时，低估其发生和后果，假设生活将继续正常。

### 推理式

```text
出现风险信号 S；因为过去没有灾难而弱化 S；因此不准备应对。
```

### 诊断问题

1. 历史未发生是否意味着未来概率低？
2. 预警信号是否与已知失效模式相符？

### 原创例子

> 警报持续响起，但员工认为从未出过事故，所以没有疏散。

### 何时可能不是谬误

多数警报可能为假，持续恐慌也有成本；需要根据概率、严重性和更新信息行动。

### 容易混淆

status quo bias、optimism bias、appeal to tradition

### 相关条目

现状偏差 (`status-quo-bias`)、乐观偏差 (`optimism-bias`)、诉诸传统 (`appeal-to-tradition`)


---

## 权威偏差

**Authority Bias** · `authority-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：盲信权威、地位影响判断

### 定义

因为信息来源具有高地位、制服、头衔或权威形象，就降低对其内容的审查。

### 推理式

```text
来源 S 有权威标志；因此主张 P 被赋予高于证据的权重。
```

### 诊断问题

1. S 是否具备相关专长和证据？
2. 如果去掉头衔，我还会接受吗？

### 原创例子

> 穿实验室外套的人推荐产品，就默认其具有科学功效。

### 何时可能不是谬误

权威可以作为合理信息捷径；偏差在于身份取代内容检验。

### 容易混淆

appeal to authority、halo effect、transfer

### 相关条目

诉诸权威 (`appeal-to-authority`)、诉诸伪权威 (`appeal-to-false-authority`)、光环效应 (`halo-effect`)


---

## 从众偏差

**Bandwagon Bias** · `bandwagon-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：羊群效应、跟随多数

### 定义

因为相信多数人正在采用某行为或观点，就更可能跟随，而不是独立评估。

### 推理式

```text
观察他人选择 C；把 C 当作社会正确信号；因此选择 C。
```

### 诊断问题

1. 多数选择提供了效果信息，还是只提供社会压力？
2. 我的偏好是否在没有观察他人时不同？

### 原创例子

> 看到某软件下载量高，就不再检查隐私政策直接采用。

### 何时可能不是谬误

社会信息有时是有效捷径，如其他人已试错；仍需处理信息级联。

### 容易混淆

appeal to popularity、false consensus、herd behavior

### 相关条目

诉诸流行 (`appeal-to-popularity`)、虚假共识偏差 (`false-consensus-bias`)、内群体偏差 (`in-group-bias`)


---

## 规划谬误

**Planning Fallacy** · `planning-fallacy`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：低估耗时成本、项目计划过度乐观

### 定义

系统性地低估任务时间、成本和风险，尤其依据最佳情形而非过去类似项目。

### 推理式

```text
新项目 P 计划成本 C1；参考类别项目平均成本 C2>>C1；仍采用 C1。
```

### 诊断问题

1. 类似项目的实际分布是什么？
2. 计划是否基于最佳情形而忽略依赖和返工？

### 原创例子

> 软件项目预计两周完成，尽管过去同类功能平均需要两个月。

### 何时可能不是谬误

新工具和独特条件可能确实改变效率；需要参考类别数据。

### 容易混淆

optimism bias、overconfidence、base-rate neglect

### 相关条目

乐观偏差 (`optimism-bias`)、过度自信偏差 (`overconfidence-bias`)、基准率忽视 (`base-rate-neglect`)


---

## 作为与不作为偏差

**Omission Bias** · `omission-bias`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：不作为更可接受、行动伤害权重更高

### 定义

相比同样由不作为造成的伤害，更严厉评价主动行为造成的伤害。

### 推理式

```text
行为 A 与不行为 N 产生相近结果 R；A 被判定更不道德。
```

### 诊断问题

1. 如果主动和不主动的结果对受影响者相同，我的评价是否改变？
2. 不行动的基线风险是否被计入？

### 原创例子

> 拒绝有效疫苗的主动风险与感染风险被不同方式评价。

### 何时可能不是谬误

作为与不作为在责任、意图和权利上可能有真实差异；偏差在于把差异无限扩大。

### 容易混淆

status quo bias、loss aversion、moral luck

### 相关条目

现状偏差 (`status-quo-bias`)、损失厌恶 (`loss-aversion`)、政策瘫痪谬误 (`policy-paralysis`)


---

## 愿望思维

**Wishful Thinking** · `wishful-thinking`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：希望即现实、愿望影响概率

### 定义

因为希望某结果发生或害怕某结果发生，就调整对其概率和证据的评估。

### 推理式

```text
希望 P；因此高估 P 的证据和概率。
```

### 诊断问题

1. 如果结果相反，我会怎样解释同一证据？
2. 愿望是否独立影响事实判断？

### 原创例子

> 因为太希望投资成功，就把反对数据解释为暂时噪声。

### 何时可能不是谬误

目标会影响注意力和行动，这是正常动机；偏差在于愿望改变事实评价。

### 容易混淆

optimism bias、moralistic fallacy、motivated reasoning

### 相关条目

乐观偏差 (`optimism-bias`)、道德主义谬误 (`moralistic-fallacy`)、确认偏差 (`confirmation-bias`)


---

## 公正世界假设

**Just-World Hypothesis** · `just-world-hypothesis`

- 类型：认知偏差
- 默认影响：背景偏差
- 别名：世界公平倾向、善有善报偏差

### 定义

相信世界基本公平、每个人得到应得结果，从而用结果反推个人品德和行为。

### 推理式

```text
结果 R 已发生；公平世界假设要求 R 与应得相匹配；因此受害者被推定有错或成功者被推定高尚。
```

### 诊断问题

1. 结果与行为之间有独立因果证据吗？
2. 随机、权力和制度因素是否被忽略？

### 原创例子

> 看到某人生活困顿，就推断他一定不努力。

### 何时可能不是谬误

行为和选择会影响结果；偏差在于从结果本身反推道德应得。

### 容易混淆

just-world inference、victim blaming、halo effect

### 相关条目

公正世界推断 (`just-world-inference`)、受害者归因 (`victim-blaming-inference`)、光环效应 (`halo-effect`)


[返回分类索引](../catalog-index.md)
