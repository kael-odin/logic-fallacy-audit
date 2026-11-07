# 公共说服与宣传

**Public Persuasion and Propaganda**

通过身份、恐惧、重复、框架或对话控制替代和遮蔽论证。

> 使用提示：描述说服机制和对话效果，不推断发言者动机。

> 本文件由结构化目录生成。修改 `catalog/` 后再运行 `python scripts/fallacy_cli.py render`。

共 **24** 条。

## 快速索引

| 中文名 | English | ID |
|---|---|---|
| 光辉泛化 | Glittering Generality | `glittering-generality` |
| 移情联想 | Transfer | `transfer` |
| 证言式背书 | Testimonial | `testimonial` |
| 平民形象 | Plain Folks | `plain-folks` |
| 贴标签 | Name-Calling | `name-calling` |
| 委婉语掩盖 | Euphemism as Concealment | `euphemism` |
| 倾向性措辞 | Loaded Language | `loaded-language` |
| 去人化修辞 | Dehumanizing Rhetoric | `dehumanization` |
| 终止思考的陈词 | Thought-Terminating Cliche | `thought-terminating-cliche` |
| 无依据权威引用 | Unsubstantiated Authority Reference | `unsubstantiated-authority` |
| 恐惧、不确定与怀疑营销 | Fear, Uncertainty, and Doubt | `fear-uncertainty-doubt` |
| 虚假平衡 | False Balance | `false-balance` |
| 强行两边都有理 | Both-Sidesism | `both-sidesism` |
| 挑极端代表 | Nutpicking | `nutpicking` |
| 狗哨式表达 | Dog Whistling | `dog-whistling` |
| 煤气灯式否定 | Gaslighting as Argumentative Tactic | `gaslighting` |
| 否认、攻击、反转受害 | DARVO | `darvo` |
| 胁迫性框架 | Coercive Framing | `coercive-framing` |
| 欲言又止 | Apophasis | `apophasis` |
| 反问当证据 | Rhetorical Question as Assertion | `rhetorical-question-as-assertion` |
| 操纵性框架 | Framing Manipulation | `framing-manipulation` |
| 威士忌式两面话 | If-by-Whiskey | `if-by-whiskey` |
| 夸大专家分歧 | Inflation of Conflict | `inflation-of-conflict` |
| 嗤之以鼻谬误 | Pooh-Pooh Fallacy | `pooh-pooh` |

---

## 光辉泛化

**Glittering Generality** · `glittering-generality`

- 类型：修辞模式
- 默认影响：中等
- 别名：漂亮大词、美德词包装

### 定义

用自由、进步、科学、责任等高价值大词支持主张，却不说明具体含义和可检验政策。

### 推理式

```text
将 P 与高度正面的抽象词 W 绑定；因此 P 显得可取。
```

### 诊断问题

1. W 在这里的操作定义是什么？
2. 如果换成中性词，支持 P 的理由还剩什么？

### 例子（原创性人工复核）

> 这是面向未来的创新方案，所以当然应该支持。

### 何时可能不是谬误

价值词可以合法表达共同目标；问题在于抽象好感替代了具体机制和取舍。

### 容易混淆

persuasive definition、appeal to emotion、virtue words

### 相关条目

说服性定义 (`persuasive-definition`)、诉诸情感 (`appeal-to-emotion`)、倾向性措辞 (`loaded-language`)


---

## 移情联想

**Transfer** · `transfer`

- 类型：修辞模式
- 默认影响：中等
- 别名：象征转移、好感迁移

### 定义

把受尊敬、喜爱或恐惧的符号、形象和群体与目标对象关联，使受众把原本对符号的情绪迁移到对象上。

### 推理式

```text
对象 A 与符号 S 并列；受众对 S 有强情绪；因此对 A 形成相似态度。
```

### 诊断问题

1. 符号与对象之间有论证关系还是纯视觉/语言并置？
2. 去除符号后，对象的独立证据是什么？

### 例子（原创性人工复核）

> 产品广告把设备放在科研实验室画面中，让人以为它经过科学研究验证。

### 何时可能不是谬误

象征可以合法表达身份和共同价值；问题在于情绪联想替代事实关联。

### 容易混淆

testimonial、guilt by association、halo effect

### 相关条目

证言式背书 (`testimonial`)、关联污染 (`guilt-by-association`)、光环效应 (`halo-effect`)


---

## 证言式背书

**Testimonial** · `testimonial`

- 类型：修辞模式
- 默认影响：中等
- 别名：个人见证、名人证言

### 定义

用某人的个人经历或背书支持广泛结论，而不说明其代表性、专业性和利益关系。

### 推理式

```text
A 说“我用了 P 后很好”；因此 P 对所有人有效。
```

### 诊断问题

1. A 的经历是否有样本和机制支持？
2. A 是否因背书获益？
3. 其他人的反例和基线变化是什么？

### 例子（原创性人工复核）

> 一位主播说自己用这款面霜后皮肤变好，所以它能治疗所有皮肤问题。

### 何时可能不是谬误

消费者体验和专家证言可以是线索；还需要区分个人体验、产品效果和普遍医疗主张。

### 容易混淆

appeal to authority、anecdotal evidence、celebrity endorsement

### 相关条目

诉诸伪权威 (`appeal-to-false-authority`)、轶事证据 (`anecdotal-evidence`)、移情联想 (`transfer`)


---

## 平民形象

**Plain Folks** · `plain-folks`

- 类型：修辞模式
- 默认影响：提示
- 别名：亲民人设、你我普通人

### 定义

通过强调自己与普通人一样、说方言、吃家常饭等方式建立身份亲近感，以增加主张可信度。

### 推理式

```text
A 表现得像普通人；因此 A 的政策或产品更可信。
```

### 诊断问题

1. 亲民表现与政策证据或产品效果有何关系？
2. 身份表演是否掩盖了资源、利益与责任差异？

### 例子（原创性人工复核）

> 这位高管穿便装吃路边摊，因此他的员工政策一定更公平。

### 何时可能不是谬误

共享经验可以建立信任、说明理解；问题在于把它当能力或善意的充分证明。

### 容易混淆

appeal to popularity、flattery、authenticity signal

### 相关条目

诉诸奉承 (`appeal-to-flattery`)、诉诸流行 (`appeal-to-popularity`)、移情联想 (`transfer`)


---

## 贴标签

**Name-Calling** · `name-calling`

- 类型：修辞模式
- 默认影响：中等
- 别名：负面标签、标签化

### 定义

用贬义标签概括复杂主张或人物，使受众无需检验理由便产生排斥。

### 推理式

```text
把 P 称为“愚蠢”“极端”“洗地”等；因此不必回应 P。
```

### 诊断问题

1. 标签的定义和证据是什么？
2. 去掉标签后，是否还有具体论证可供回应？

### 例子（原创性人工复核）

> 这不是风险管理，这是懦弱，所以方案不用看。

### 何时可能不是谬误

某些准确类别词本身带有评价，但应有可检验标准；标签不能替代论证。

### 容易混淆

ad hominem、poisoning the well、loaded language

### 相关条目

人身攻击 (`ad-hominem-abusive`)、毒化井水 (`poisoning-the-well`)、倾向性措辞 (`loaded-language`)


---

## 委婉语掩盖

**Euphemism as Concealment** · `euphemism`

- 类型：修辞模式
- 默认影响：中等
- 别名：粉饰性委婉语、语言软化

### 定义

用温和、技术化或模糊的词替代会引发准确评价的表述，从而降低受众对行为成本的感知。

### 推理式

```text
把 X 称为较温和的 E；受众据 E 评估；X 的道德或风险特征被淡化。
```

### 诊断问题

1. 被描述的实际行为是什么？
2. 委婉语省略了哪些受影响对象和后果？

### 例子（原创性人工复核）

> 裁员被写成“组织活力优化”，导致责任和规模不透明。

### 何时可能不是谬误

委婉语有礼貌和降低伤害的功能；问题在于它是否掩盖决策信息。

### 容易混淆

doublespeak、loaded language、strategic vagueness

### 相关条目

倾向性措辞 (`loaded-language`)、策略性模糊 (`strategic-vagueness`)、操纵性框架 (`framing-manipulation`)


---

## 倾向性措辞

**Loaded Language** · `loaded-language`

- 类型：修辞模式
- 默认影响：中等
- 别名：情绪化词汇、评价性标签

### 定义

使用带有强评价和情绪色彩的措辞描述争议事实，使读者在被证明前先接受某种判断。

### 推理式

```text
用“打压”“纵容”“洗白”等词描述中立或待查行为；因此情绪判断先于证据。
```

### 诊断问题

1. 是否有中性词能表达同一事实？
2. 评价词所依据的判断是否已独立证明？

### 例子（原创性人工复核）

> 把正常质询称为“恶意围攻”，把未经回应称为“默认认罪”。

### 何时可能不是谬误

准确评价性词汇可以表达不可忽视的伦理特征；关键是证据是否先于标签。

### 容易混淆

framing、name-calling、loaded question

### 相关条目

贴标签 (`name-calling`)、操纵性框架 (`framing-manipulation`)、诱导性问题 (`loaded-question`)


---

## 去人化修辞

**Dehumanizing Rhetoric** · `dehumanization`

- 类型：修辞模式
- 默认影响：高影响
- 别名：非人化、群体动物化

### 定义

用非人、疾病、污染或动物化隐喻描述群体，降低受众对其痛苦和权利的同理心。

### 推理式

```text
群体 G 被描述为非人/害虫/病毒；因此对 G 的伤害显得可接受。
```

### 诊断问题

1. 隐喻是否把一个群体整体物化或污名化？
2. 它是否替代了对具体行为和责任的分析？
3. 语言是否鼓励暴力或剥夺基本权利？

### 例子（原创性人工复核）

> 把某地区居民统称为“污染源”，因此讨论强制隔离时不再考虑个体权利。

### 何时可能不是谬误

医学和风险传播会使用感染、传播等术语；关键在于是否把抽象机制准确用于行为，还是用来否定群体人格。

### 容易混淆

name-calling、appeal to spite、scapegoating

### 相关条目

替罪羊归因 (`scapegoating`)、诉诸怨恨 (`appeal-to-spite`)、胁迫性框架 (`coercive-framing`)


---

## 终止思考的陈词

**Thought-Terminating Cliche** · `thought-terminating-cliche`

- 类型：修辞模式
- 默认影响：中等
- 别名：别想太多、就是这样

### 定义

用熟悉口号、俗语或情绪化短句终止追问，让复杂问题看起来已经解决。

### 推理式

```text
面对问题 Q，回答“这就是人性”“懂的都懂”等；Q 的证据和替代解释未被讨论。
```

### 诊断问题

1. 这句话解释了哪个具体机制？
2. 它是否阻止了可回答的问题继续展开？

### 例子（原创性人工复核）

> 为什么流程失败？答案就是人性，不要再分析制度了。

### 何时可能不是谬误

口号和俗语可有效压缩共识或表达情绪；问题在于替代了当前所需的理由。

### 容易混淆

proof by assertion、appeal to common sense、sloganeering

### 相关条目

断言式证明 (`proof-by-assertion`)、诉诸常识 (`appeal-to-common-sense`)、诉诸忠诚 (`appeal-to-loyalty`)


---

## 无依据权威引用

**Unsubstantiated Authority Reference** · `unsubstantiated-authority`

- 类型：修辞模式
- 默认影响：中等
- 别名：模糊专家、研究都说了

### 定义

声称专家、研究或内部人士支持结论，却不给身份、方法、出处或可核验范围。

### 推理式

```text
模糊权威 S 支持 P；因此 P 为真。
```

### 诊断问题

1. S 具体是谁，来源在哪里？
2. S 是否直接研究该问题并给出可检查的材料？

### 例子（原创性人工复核）

> 很多顶级专家都说这项技术安全，但没有论文、机构或名单。

### 何时可能不是谬误

现实交流可以先用概括来源建立方向；高风险结论应补足出处。

### 容易混淆

appeal to authority、weasel words、appeal to false authority

### 相关条目

诉诸权威 (`appeal-to-authority`)、诉诸伪权威 (`appeal-to-false-authority`)、模糊来源词 (`weasel-words`)


---

## 恐惧、不确定与怀疑营销

**Fear, Uncertainty, and Doubt** · `fear-uncertainty-doubt`

- 类型：修辞模式
- 默认影响：高影响
- 别名：FUD、制造疑虑

### 定义

通过强调不确定、潜在灾难或模糊风险，使受众回避某方案并偏好宣传者提供的选择，而不做概率比较。

### 推理式

```text
强调 P 的未知风险；不量化概率和替代方案；因此接受 Q。
```

### 诊断问题

1. 风险的概率、严重性和可逆性是什么？
2. Q 是否也被同样审查？
3. 不确定性是否被用来制造偏向而非促进调查？

### 例子（原创性人工复核）

> 采用开放标准存在未知漏洞，所以必须购买我们的封闭系统。

### 何时可能不是谬误

不确定性是真实风险信息；问题在于只对竞争方案强调风险，不对自己的方案使用同一标准。

### 容易混淆

appeal to fear、policy paralysis、commercial FUD

### 相关条目

诉诸恐惧 (`appeal-to-fear`)、政策瘫痪谬误 (`policy-paralysis`)、虚假两难 (`false-dilemma`)


---

## 虚假平衡

**False Balance** · `false-balance`

- 类型：修辞模式
- 默认影响：高影响
- 别名：两边等重、证据不对等仍各打五十大板

### 定义

为了让报道或讨论看起来中立，给证据质量和专家共识明显不对等的立场相同篇幅或权重。

### 推理式

```text
立场 A 有强证据，B 只有微弱支持；媒体按 50:50 呈现；因此受众误以为争议对等。
```

### 诊断问题

1. 双方证据数量、质量和共识程度是否相当？
2. 篇幅平衡是否被误当成证据平衡？

### 例子（原创性人工复核）

> 几乎所有数据支持结论 A，却安排一位无相关证据的反对者与三位研究者等时辩论。

### 何时可能不是谬误

呈现异议能保护少数观点和防止群体思维；但公平不等于机械等时。

### 容易混淆

both-sidesism、false equivalence、neutrality

### 相关条目

强行两边都有理 (`both-sidesism`)、虚假等同 (`false-equivalence`)、弱人谬误 (`weak-man`)


---

## 强行两边都有理

**Both-Sidesism** · `both-sidesism`

- 类型：修辞模式
- 默认影响：中等
- 别名：凡事各打五十大板、强迫对称

### 定义

把“任何议题都有两面”当作默认结论，不管责任、证据或伤害是否实际对称。

### 推理式

```text
存在双方；因此责任和正确性各占一半。
```

### 诊断问题

1. 双方的主张、证据和行为是否真的对称？
2. “平衡”是否掩盖了单方伤害或压倒性证据？

### 例子（原创性人工复核）

> 一方提出有数据的风险报告，另一方只进行人身攻击，却被总结为“双方都有问题”。

### 何时可能不是谬误

审视多方立场是必要的；但对称性应由具体维度支持。

### 容易混淆

false balance、moral equivalence、false equivalence

### 相关条目

虚假平衡 (`false-balance`)、道德等同 (`moral-equivalence`)、虚假等同 (`false-equivalence`)


---

## 挑极端代表

**Nutpicking** · `nutpicking`

- 类型：修辞模式
- 默认影响：中等
- 别名：极端样本代表群体、挑疯子

### 定义

从某群体中挑选最极端、最荒谬的少数声音，作为整个群体或立场的代表。

### 推理式

```text
群体 G 中有极端成员 e；e 说 P；因此 G 都支持 P 或因此 G 无效。
```

### 诊断问题

1. e 在群体中的影响力和代表性有多大？
2. 主流或最强版本怎么说？
3. 选择 e 是否因为更容易攻击？

### 例子（原创性人工复核）

> 找到社交平台上一个极端评论，便宣称整个职业群体都持有这种观点。

### 何时可能不是谬误

如果极端声音掌握权力、构成官方立场或造成主要影响，批评它可以具有代表性；仍需证明。

### 容易混淆

weak man、straw man、hasty generalization

### 相关条目

弱人谬误 (`weak-man`)、草率概括 (`hasty-generalization`)、空人谬误 (`hollow-man`)


---

## 狗哨式表达

**Dog Whistling** · `dog-whistling`

- 类型：修辞模式
- 默认影响：中等
- 别名：隐性群体信号、双关动员

### 定义

使用表面中性但特定群体能识别为动员或排斥信号的措辞，使发言者保留可否认性。

### 推理式

```text
表达 E 表面含义中性；在特定历史或社群语境中暗示 G；受众据此动员。
```

### 诊断问题

1. 该词是否有可记录的特定社群用法和历史？
2. 发言者是否持续使用同一编码模式？
3. 是否有独立的行为或政策后果支持其功能判断？

### 例子（原创性人工复核）

> 使用一个在特定论坛长期用于排斥某群体的暗语，却在被质疑时声称只是字面意思。

### 何时可能不是谬误

判断狗哨高度依赖语境，误读风险高；仅凭一个词不应给出高置信度。

### 容易混淆

loaded language、coded speech、mind reading

### 相关条目

倾向性措辞 (`loaded-language`)、胁迫性框架 (`coercive-framing`)、操纵性框架 (`framing-manipulation`)


---

## 煤气灯式否定

**Gaslighting as Argumentative Tactic** · `gaslighting`

- 类型：修辞模式
- 默认影响：高影响
- 别名：否认对方现实、让你怀疑自己

### 定义

通过持续否认已发生事实、歪曲记录和质疑对方感知，使对方怀疑自己的记忆或判断。

### 推理式

```text
事实 F 有记录；发言者反复说 F 从未发生、对方记错或有病；因此对方放弃基于 F 的论证。
```

### 诊断问题

1. 是否存在可核验的记录和时间线？
2. 否认是否持续且与证据直接冲突？
3. 模式是否使对方无法稳定讨论事实？

### 例子（原创性人工复核）

> 会议明确作出承诺，之后领导反复说“你理解错了，大家从没这么说过”。

### 何时可能不是谬误

单次记忆分歧不等于煤气灯；需要持续模式、权力语境和可核验事实。不能据此诊断人格障碍。

### 容易混淆

lying、invalidating、DARVO

### 相关条目

否认、攻击、反转受害 (`darvo`)、自我封闭论证 (`self-sealing-argument`)、胁迫性框架 (`coercive-framing`)


---

## 否认、攻击、反转受害

**DARVO** · `darvo`

- 类型：修辞模式
- 默认影响：高影响
- 别名：Deny Attack Reverse Victim and Offender

### 定义

面对指责依次否认、攻击指责者、把自己塑造成受害者，从而转移对原问题的审查。

### 推理式

```text
被指控 A；否认；攻击指控者可信度；宣称自己受迫害；因此 A 不再被讨论。
```

### 诊断问题

1. 原指控的证据是否被具体回应？
2. 攻击与反转是否是替代证据的转移？
3. 双方权力和伤害是否被对称呈现？

### 例子（原创性人工复核）

> 被指出泄露数据后，他先说没有，再攻击举报者别有用心，最后说自己是网络暴力受害者。

### 何时可能不是谬误

被指控者也可能真的无辜并受到攻击；DARVO 需要看顺序、证据回应和权力语境，不能仅凭否认判断。

### 容易混淆

tu quoque、victim blaming、gaslighting

### 相关条目

煤气灯式否定 (`gaslighting`)、你也一样 (`tu-quoque`)、语气警察 (`tone-policing`)


---

## 胁迫性框架

**Coercive Framing** · `coercive-framing`

- 类型：修辞模式
- 默认影响：高影响
- 别名：不给反对空间、选择即忠诚

### 定义

把政策或事实争论重新框成忠诚、身份或生存选择，使反对者面临社会惩罚。

### 推理式

```text
P 被定义为唯一正确立场；反对 P 被描述为背叛/敌意；因此 P 免受实质检验。
```

### 诊断问题

1. 反对 P 是否被允许作为事实或价值问题讨论？
2. 身份惩罚是否替代了证据？

### 例子（原创性人工复核）

> 支持团队就必须无条件支持这项决定，提出问题等于破坏团结。

### 何时可能不是谬误

道德底线和紧急行动确实可能限制选择；但需要独立论证为什么普通质疑应被排除。

### 容易混淆

appeal to loyalty、argumentum ad baculum、thought-terminating cliche

### 相关条目

诉诸忠诚 (`appeal-to-loyalty`)、诉诸威胁 (`argumentum-ad-baculum`)、终止思考的陈词 (`thought-terminating-cliche`)


---

## 欲言又止

**Apophasis** · `apophasis`

- 类型：修辞模式
- 默认影响：提示
- 别名：我不是说他坏、声明不提及却提及

### 定义

声称不讨论某事，却通过否定式提及把指控或联想植入受众心中。

### 推理式

```text
“我不谈 A，但大家知道 A”；因此 A 被暗示且可否认。
```

### 诊断问题

1. 作者是否主动引入了本可省略的负面内容？
2. 这个否定式提及是否意在保留可否认性？

### 例子（原创性人工复核）

> 我不讨论他的资金来源，只是提醒大家为什么他最近换了好车。

### 何时可能不是谬误

澄清“我不会讨论隐私”可能合理；判断要看内容是否实际产生攻击效果。

### 容易混淆

innuendo、JAQing off、poisoning the well

### 相关条目

我只是问问 (`jaqing-off`)、毒化井水 (`poisoning-the-well`)、倾向性措辞 (`loaded-language`)


---

## 反问当证据

**Rhetorical Question as Assertion** · `rhetorical-question-as-assertion`

- 类型：修辞模式
- 默认影响：提示
- 别名：答案显然的反问、问句式断言

### 定义

用带强烈暗示的反问让受众自行补出结论，避免承担该结论所需的论证责任。

### 推理式

```text
“难道不是 P 吗？”使 P 显得显然，但没有支持 P 的证据。
```

### 诊断问题

1. 反问要求受众接受什么结论？
2. 如果改成陈述句，作者是否能提供证据？

### 例子（原创性人工复核）

> 连这么简单的问题都解决不了，你还敢说团队有能力吗？

### 何时可能不是谬误

反问可有效强调共识、引导反思和节省解释；问题是暗示的结论没有独立支持。

### 容易混淆

loaded question、JAQing off、appeal to ridicule

### 相关条目

诱导性问题 (`loaded-question`)、我只是问问 (`jaqing-off`)、诉诸嘲笑 (`appeal-to-ridicule`)


---

## 操纵性框架

**Framing Manipulation** · `framing-manipulation`

- 类型：修辞模式
- 默认影响：中等
- 别名：议题重述、框架置换

### 定义

通过选择参照点、命名方式和议题边界，使受众在未经说明的价值框架下理解事实。

### 推理式

```text
事实 F 可置于框架 A 或 B；论证只呈现 B 并使结论看起来唯一；框架本身未受检验。
```

### 诊断问题

1. 等值但不同的框架会怎样改变判断？
2. 哪些事实被边界排除？
3. 框架中的价值前提是否明示？

### 例子（原创性人工复核）

> 把裁员描述为“释放人才进入市场”，因此不再讨论失去收入和团队知识。

### 何时可能不是谬误

所有叙述都需要框架；问题在于框架隐蔽、单边或阻止替代描述被比较。

### 容易混淆

framing effect、loaded language、strategic vagueness

### 相关条目

框架效应 (`framing-effect`)、倾向性措辞 (`loaded-language`)、委婉语掩盖 (`euphemism`)


---

## 威士忌式两面话

**If-by-Whiskey** · `if-by-whiskey`

- 类型：修辞模式
- 默认影响：中等
- 别名：两面讨好修辞、条件式骑墙、if by whiskey fallacy

### 定义

对争议问题用“如果……那么支持；如果……那么反对”的对称措辞同时取悦双方，却不明确自己的实际立场和承诺条件。

### 推理式

```text
若按解释 A 理解 P，则我赞成；若按解释 B 理解 P，则我反对；因此听众各自认为作者支持自己。
```

### 诊断问题

1. 作者究竟承诺采用哪一种解释或政策？
2. 两个“如果”分支是否会导致不同的实际行动？
3. 去掉华丽措辞后，立场能否被反驳或追责？

### 例子（原创性人工复核）

> 如果这项改革能提高公平，我完全支持；如果它损害效率，我当然反对。至于具体方案，我不表态。

### 何时可能不是谬误

有条件立场和承认权衡可以合理；问题是用条件句隐藏不可同时兑现的承诺，避免说明实际选择。

### 容易混淆

偷换概念、护城河与城堡、倾向性措辞

### 相关条目

偷换概念 (`equivocation`)、护城河与城堡 (`motte-and-bailey`)、倾向性措辞 (`loaded-language`)


---

## 夸大专家分歧

**Inflation of Conflict** · `inflation-of-conflict`

- 类型：修辞模式
- 默认影响：中等
- 别名：冲突膨胀、把细节争议说成整体共识崩塌

### 定义

把专业领域内关于范围、估计或方法的局部争议，扩大成整体结论没有证据或专家毫无共识，从而取消现有证据权重。

### 推理式

```text
专家在细节 D 上存在分歧；因此结论 C 完全没有可靠支持。
```

### 诊断问题

1. 争议涉及核心结论、参数范围还是方法细节？
2. 多数独立证据和系统综述怎样分布？
3. 分歧是否改变结论方向、强度或不确定性？

### 例子（原创性人工复核）

> 两项研究对风险下降 20% 还是 15% 有分歧，所以专家根本不知道这项措施有没有效果。

### 何时可能不是谬误

真实而根本的专家冲突会降低置信度；问题是把有限争议扩大到整个证据体系。

### 容易混淆

虚假平衡、诉诸权威、诉诸无知

### 相关条目

虚假平衡 (`false-balance`)、诉诸权威 (`appeal-to-authority`)、诉诸无知 (`appeal-to-ignorance`)


---

## 嗤之以鼻谬误

**Pooh-Pooh Fallacy** · `pooh-pooh`

- 类型：修辞模式
- 默认影响：中等
- 别名：轻蔑否定、不值得回应式反驳、pooh-poohing

### 定义

不说明对方主张或证据哪里错误，只用嘲笑、轻蔑或“这不值一驳”的姿态让受众跳过论证本身。

### 推理式

```text
A 提出 P 和理由；B 说 P 很可笑、不值讨论；因此受众把 P 当作已被反驳。
```

### 诊断问题

1. B 是否具体回应了 P 的证据和推理？
2. 如果移除嘲讽语气，还剩什么反驳？
3. 被嘲笑的内容是否可能事实正确但表达笨拙？

### 例子（原创性人工复核）

> 有人提出测试数据可能有统计缺陷，主持人笑着说这问题不值一驳，于是继续原结论。

### 何时可能不是谬误

简短的轻蔑回应可能只是拒绝低质量挑衅；当它替代对可检验论证的回应时才构成问题。

### 容易混淆

诉诸嘲笑、诉诸顽石、断言式证明

### 相关条目

诉诸嘲笑 (`appeal-to-ridicule`)、诉诸顽石 (`argumentum-ad-lapidem`)、断言式证明 (`proof-by-assertion`)


[返回分类索引](../catalog-index.md)
