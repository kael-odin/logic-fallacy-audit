# 规范、政策与价值

**Normative, Policy, and Value Reasoning**

从事实跳到应然，或政策比较中缺少价值前提、替代方案与成本分析。

> 使用提示：分开目标、手段、副作用、分配与价值排序。

> 本文件由结构化目录生成。修改 `catalog/` 后再运行 `python scripts/fallacy_cli.py render`。

共 **18** 条。

## 快速索引

| 中文名 | English | ID |
|---|---|---|
| 实然推应然 | Is-Ought Fallacy | `is-ought` |
| 自然主义谬误 | Naturalistic Fallacy | `naturalistic-fallacy` |
| 道德主义谬误 | Moralistic Fallacy | `moralistic-fallacy` |
| 诉诸法律 | Appeal to Law | `appeal-to-law` |
| 诉诸正义 | Appeal to Justice | `appeal-to-justice` |
| 两个错误等于一个正确 | Two Wrongs Make a Right | `two-wrongs-make-right` |
| 替罪羊归因 | Scapegoating | `scapegoating` |
| 受害者归因 | Victim-Blaming Inference | `victim-blaming-inference` |
| 时代势利 | Chronological Snobbery | `chronological-snobbery` |
| 诉诸进步 | Appeal to Progress | `appeal-to-progress` |
| 诉诸常识 | Appeal to Common Sense | `appeal-to-common-sense` |
| 诉诸可能性 | Appeal to Possibility | `appeal-to-possibility` |
| 政策瘫痪谬误 | Policy Paralysis | `policy-paralysis` |
| 成本收益忽视 | Cost-Benefit Neglect | `cost-benefit-neglect` |
| 道德等同 | Moral Equivalence | `moral-equivalence` |
| 公正世界推断 | Just-World Inference | `just-world-inference` |
| 诉诸现状 | Appeal to Status Quo | `appeal-to-status-quo` |
| 穷尽努力谬误 | Fallacy of Exhaustive Effort | `exhaustive-effort-fallacy` |

---

## 实然推应然

**Is-Ought Fallacy** · `is-ought`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：事实推价值、实然应然跳跃

### 定义

只凭某事物是什么、正在发生或自然如此，就推出它应该如此、正当或值得追求。

### 推理式

```text
P 是事实；因此 P 是好的、允许的或应继续。
```

### 诊断问题

1. 从事实到规范中间缺哪条价值前提？
2. 即使描述为真，是否仍可能有人有理由反对？

### 例子（原创性人工复核）

> 人们一直在规避这项规则，所以这项规则就应该被取消。

### 何时可能不是谬误

事实会约束规范判断；问题在于缺少明确的价值或制度前提，而不是事实与规范完全无关。

### 容易混淆

自然主义谬误、规范判断、描述性事实

### 相关条目

自然主义谬误 (`naturalistic-fallacy`)、道德主义谬误 (`moralistic-fallacy`)、诉诸传统 (`appeal-to-tradition`)


---

## 自然主义谬误

**Naturalistic Fallacy** · `naturalistic-fallacy`

- 类型：非形式谬误
- 默认影响：中等
- 别名：自然即善、从自然属性推道德

### 定义

从某行为或属性“自然”“符合进化”或“存在于自然”，直接推出它道德上善或应当如此。

### 推理式

```text
P 是自然的；因此 P 是善的或应当的。
```

### 诊断问题

1. “自然”指统计常见、生物功能还是非人工？
2. 哪一种价值标准把自然属性转成道德应当？

### 例子（原创性人工复核）

> 动物竞争中存在强者压制弱者，所以人类社会也应如此。

### 何时可能不是谬误

自然事实可能影响健康、能力和后果；但道德结论仍需价值原则。不同“自然”定义也会改变论证。

### 容易混淆

appeal to nature、is-ought、evolutionary ethics

### 相关条目

诉诸自然 (`appeal-to-nature`)、实然推应然 (`is-ought`)、道德主义谬误 (`moralistic-fallacy`)


---

## 道德主义谬误

**Moralistic Fallacy** · `moralistic-fallacy`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：应然推实然、善所以是事实

### 定义

因为某结果道德上更可取或令人希望，就推出它在现实中为真或必然发生。

### 推理式

```text
P 应该为真或 P 若为真更好；因此 P 为真。
```

### 诊断问题

1. 道德可取性是否增加了事实概率？
2. 是否存在令人不快但可靠的相反证据？

### 例子（原创性人工复核）

> 如果人人都平等受益会更好，所以那项政策一定不会伤害任何人。

### 何时可能不是谬误

价值目标可以指导调查和政策选择；但不能改变已经存在的经验事实。

### 容易混淆

appeal to consequences、wishful thinking、is-ought

### 相关条目

实然推应然 (`is-ought`)、诉诸后果 (`appeal-to-consequences`)、愿望思维 (`wishful-thinking`)


---

## 诉诸法律

**Appeal to Law** · `appeal-to-law`

- 类型：非形式谬误
- 默认影响：中等
- 别名：合法即合理、法律等于道德

### 定义

因为某行为合法或非法，就直接推出它道德上正当或错误、有效或无效，混淆法律地位与其他规范。

### 推理式

```text
P 合法；因此 P 合乎伦理或有效。
```

### 诊断问题

1. 当前判断的是法律结论、道德结论还是效果结论？
2. 法律与所要证明的规范是否同一标准？

### 例子（原创性人工复核）

> 这家公司利用漏洞避税是合法的，所以它当然也是公平的。

### 何时可能不是谬误

在法律论证中，法条和判例可能是决定性理由；问题在于把法律地位偷换成道德或事实的全部。

### 容易混淆

legal positivism、法律与伦理、社会规范

### 相关条目

实然推应然 (`is-ought`)、诉诸权威 (`appeal-to-authority`)、诉诸常识 (`appeal-to-common-sense`)


---

## 诉诸正义

**Appeal to Justice** · `appeal-to-justice`

- 类型：非形式谬误
- 默认影响：中等
- 别名：不公平所以无效、正义直觉证明

### 定义

仅凭某结果让人感觉不公平，就断言事实主张无效、政策不可行或对方一定错误。

### 推理式

```text
P 让我觉得不公平；因此 P 为假或不能采用。
```

### 诊断问题

1. 使用的是哪一种分配原则，依据是什么？
2. 不公平判断是价值前提，还是被当作事实证据？

### 例子（原创性人工复核）

> 这个算法淘汰了更多申请人，因此它一定存在技术错误。

### 何时可能不是谬误

正义原则可以成为规范结论的合理前提；技术效果和道德评价仍需分别证明。

### 容易混淆

normative reasoning、just-world inference、appeal to emotion

### 相关条目

诉诸情感 (`appeal-to-emotion`)、公正世界推断 (`just-world-inference`)、实然推应然 (`is-ought`)


---

## 两个错误等于一个正确

**Two Wrongs Make a Right** · `two-wrongs-make-right`

- 类型：非形式谬误
- 默认影响：中等
- 别名：别人也错、以错制错

### 定义

因为另一方也做了错误行为，就推出当前错误行为正当或无需负责。

### 推理式

```text
X 对 A 做了错事；A 对 Y 做类似错事；因此 A 的行为正当。
```

### 诊断问题

1. 先前错误是否改变了当前行为的道德属性？
2. 是否存在报复、补偿或制止不法等独立规范原则？

### 例子（原创性人工复核）

> 他们先泄露我的隐私，所以我公开所有人的数据也没问题。

### 何时可能不是谬误

报复、惩罚和自卫在特定规范下可能有条件成立；需要明确条件，不能只用“对方也做过”。

### 容易混淆

whataboutism、tu quoque、retributive justice

### 相关条目

你也一样 (`tu-quoque`)、那另一个呢 (`whataboutism`)、道德等同 (`moral-equivalence`)


---

## 替罪羊归因

**Scapegoating** · `scapegoating`

- 类型：修辞模式
- 默认影响：高影响
- 别名：把责任集中给某群体、替罪羊

### 定义

把复杂问题归咎于单一群体或个人，并以该承担者替代对制度、环境和多因因果的分析。

### 推理式

```text
问题 R 复杂；选择群体 G；宣称 G 是全部原因；因此无需检查其他因素。
```

### 诊断问题

1. G 的实际因果贡献有何证据？
2. 是否存在更主要的结构性因素？
3. 归责是否与证明的贡献成比例？

### 例子（原创性人工复核）

> 团队项目失败全怪新来的实习生，因此管理层流程和需求变化都不用讨论。

### 何时可能不是谬误

某些个人或群体确实承担主要责任；问题是把责任分配当成因果调查的替代。

### 容易混淆

single cause、appeal to spite、dehumanization

### 相关条目

单一原因谬误 (`single-cause`)、谁受益谁策划 (`cui-bono-fallacy`)、去人化修辞 (`dehumanization`)


---

## 受害者归因

**Victim-Blaming Inference** · `victim-blaming-inference`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：结果反推受害者有错、受害者责任谬误

### 定义

从某人受害或遭遇不利结果，反推其一定有某种过失，并据此减少加害者或系统的责任。

### 推理式

```text
A 受害；因此 A 一定做了什么导致受害。
```

### 诊断问题

1. 受害与先把受害者的某个行为当作必要原因有何证据？
2. 有多少未受害者也做了同样行为？
3. 是否存在权力、机会或制度因素？

### 例子（原创性人工复核）

> 他被诈骗，说明他一定贪心；所以平台不需要改进风险提示。

### 何时可能不是谬误

分析风险行为和预防措施可以与责任分配分开；受害者行为不一定消除他人责任。

### 容易混淆

just-world inference、post hoc、causal oversimplification

### 相关条目

公正世界推断 (`just-world-inference`)、因果过度简化 (`causal-oversimplification`)、替罪羊归因 (`scapegoating`)


---

## 时代势利

**Chronological Snobbery** · `chronological-snobbery`

- 类型：非形式谬误
- 默认影响：中等
- 别名：旧必过时、时代优越感

### 定义

仅因为某观点来自较早时代，就断定它今天错误或没有价值。

### 推理式

```text
P 产生于过去；因此 P 已过时或为假。
```

### 诊断问题

1. 时代变化具体改变了哪些证据或条件？
2. 旧观点是否包含独立可检验的论点？

### 例子（原创性人工复核）

> 这是一百年前的心理学观点，所以其中任何观察都不可能有用。

### 何时可能不是谬误

知识会更新，旧理论可能被新证据推翻；需要指出具体失效机制，而不是只给出年代。

### 容易混淆

appeal to novelty、genetic fallacy、historical context

### 相关条目

诉诸新颖 (`appeal-to-novelty`)、发生学谬误 (`genetic-fallacy`)、诉诸进步 (`appeal-to-progress`)


---

## 诉诸进步

**Appeal to Progress** · `appeal-to-progress`

- 类型：非形式谬误
- 默认影响：中等
- 别名：历史向前所以正确、进步必然

### 定义

因为某变化代表“进步”“现代化”或未来方向，就推出它一定更好或不可避免。

### 推理式

```text
P 被视为进步；因此 P 应当采用或必然成功。
```

### 诊断问题

1. 用什么指标定义进步？
2. 变化是否可能带来分配不均、反弹或新风险？

### 例子（原创性人工复核）

> 无人化管理代表未来，所以取消所有人工客服必然提升服务质量。

### 何时可能不是谬误

长期趋势可以提供证据；但方向性叙事不能单独证明净收益。

### 容易混淆

appeal to novelty、chronological snobbery、technological solutionism

### 相关条目

诉诸新颖 (`appeal-to-novelty`)、时代势利 (`chronological-snobbery`)、实然推应然 (`is-ought`)


---

## 诉诸常识

**Appeal to Common Sense** · `appeal-to-common-sense`

- 类型：非形式谬误
- 默认影响：中等
- 别名：常识证明、显而易见

### 定义

把某说法称为常识或显而易见，而不说明其证据、定义和适用条件。

### 推理式

```text
人人都知道 P，或 P 显然；因此 P 为真。
```

### 诊断问题

1. 这里所谓常识的具体命题是什么？
2. 统计上多数人相信它吗？多数信念是否足以证明它？

### 例子（原创性人工复核）

> 管理就应该强势一点，这是常识，不用再研究员工反馈。

### 何时可能不是谬误

常识可以快速调用共享知识并触发合理默认值；争议或反直觉问题需要可检验依据。

### 容易混淆

appeal to popularity、appeal to authority、background knowledge

### 相关条目

诉诸流行 (`appeal-to-popularity`)、断言式证明 (`proof-by-assertion`)、不可信论证 (`argument-from-incredulity`)


---

## 诉诸可能性

**Appeal to Possibility** · `appeal-to-possibility`

- 类型：非形式谬误
- 默认影响：中等
- 别名：可能所以成立、只要有可能

### 定义

从某解释在逻辑上可能或不能被排除，推出它值得相信或应作为政策依据。

### 推理式

```text
P 可能为真；因此 P 为真或应据此行动。
```

### 诊断问题

1. P 的概率有多大，和哪些竞争解释相比？
2. 决策是否只需排除可能，还是需要概率与后果比较？

### 例子（原创性人工复核）

> 这项措施也许能降低风险，所以应该无条件采用，不必比较成本。

### 何时可能不是谬误

在低概率高损害情境中，预防原则可能使可能性变得相关；仍需说明概率、成本和替代方案。

### 容易混淆

appeal to ignorance、precaution、possibility vs probability

### 相关条目

诉诸无知 (`appeal-to-ignorance`)、存在性谬误 (`existential-fallacy`)、诉诸概率 (`appeal-to-probability`)


---

## 政策瘫痪谬误

**Policy Paralysis** · `policy-paralysis`

- 类型：非形式谬误
- 默认影响：中等
- 别名：不完美所以不行动、等待绝对确定

### 定义

因为证据仍有不确定性，就推出任何行动都不可辩护，忽略不行动本身的风险与成本。

### 推理式

```text
关于 P 仍不确定；因此不能采取任何措施；忽略基线风险和可逆试验。
```

### 诊断问题

1. 不行动的风险和成本是什么？
2. 是否存在可逆、渐进或监测式措施？
3. 所需确定性是否与风险成比例？

### 例子（原创性人工复核）

> 气候影响仍有误差，所以暂时什么政策都不该做。

### 何时可能不是谬误

不确定时审慎是合理的；问题在于把不确定等同于零信息和零成本。

### 容易混淆

nirvana fallacy、appeal to ignorance、precautionary principle

### 相关条目

涅槃谬误 (`nirvana-fallacy`)、诉诸无知 (`appeal-to-ignorance`)、现状偏差 (`status-quo-bias`)


---

## 成本收益忽视

**Cost-Benefit Neglect** · `cost-benefit-neglect`

- 类型：非形式谬误
- 默认影响：中等
- 别名：只看收益不看成本、单边政策论证

### 定义

政策论证只强调目标收益，不评估实施成本、副作用、机会成本和受影响群体。

### 推理式

```text
P 可能带来收益 B；因此 P 应实施；忽略成本 C、替代方案与分配效应。
```

### 诊断问题

1. 总成本与边际成本是什么？
2. 谁支付、谁受益？
3. 同等资源用于其他方案效果如何？

### 例子（原创性人工复核）

> 安装全方位监控能提升安全，所以无论隐私和运维成本多高都值得。

### 何时可能不是谬误

有些权利或伦理原则不能被简单成本收益化；即使采用成本分析，也要明确不可交易价值。

### 容易混淆

nirvana fallacy、single cause、policy analysis

### 相关条目

涅槃谬误 (`nirvana-fallacy`)、单一原因谬误 (`single-cause`)、破窗谬误 (`broken-window-fallacy`)


---

## 道德等同

**Moral Equivalence** · `moral-equivalence`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：两边都坏、错误程度等同

### 定义

因为两方都做过错误或有责任，就断言错误的类型、程度、意图和后果完全相同。

### 推理式

```text
A 和 B 都犯错；因此 A 与 B 的道德责任完全等同。
```

### 诊断问题

1. 比较的是哪种错误、规模、意图、权力和后果？
2. 哪些差异会改变责任或补救要求？

### 例子（原创性人工复核）

> 两个人都在争吵中插话，所以他们的责任和伤害完全一样。

### 何时可能不是谬误

等同比较可以帮助避免双标；但必须说明相关维度，不能只凭“都有错”。

### 容易混淆

false equivalence、false balance、two wrongs

### 相关条目

虚假等同 (`false-equivalence`)、两个错误等于一个正确 (`two-wrongs-make-right`)、虚假平衡 (`false-balance`)


---

## 公正世界推断

**Just-World Inference** · `just-world-inference`

- 类型：非形式谬误
- 默认影响：高影响
- 别名：善有善报所以受害者有错、世界公平预设

### 定义

因为希望世界公平，就从某人遭遇不幸反推其必然做过错事，或从某人处境良好反推其一定道德优秀。

### 推理式

```text
A 遭遇坏事；因此 A 必然做了什么导致它；或 B 很成功；因此 B 必然努力且正直。
```

### 诊断问题

1. 结果与个人行为之间有何独立证据？
2. 是否存在运气、权力、制度和随机因素？

### 例子（原创性人工复核）

> 他这么成功，所以他人品一定很好。

### 何时可能不是谬误

行为和选择会影响结果，也可以讨论责任；问题是从结果本身反推道德应得。

### 容易混淆

victim blaming、appeal to wealth、halo effect

### 相关条目

受害者归因 (`victim-blaming-inference`)、诉诸财富 (`appeal-to-wealth`)、公正世界假设 (`just-world-hypothesis`)


---

## 诉诸现状

**Appeal to Status Quo** · `appeal-to-status-quo`

- 类型：非形式谬误
- 默认影响：中等
- 别名：现状即合理、默认现状

### 定义

因为某安排是当前默认状态，就推出它更合理、更安全或不应改变，而不比较替代方案。

### 推理式

```text
现状是 S；因此应保持 S。
```

### 诊断问题

1. 现状的历史形成和分配结果是什么？
2. 改变与不改变各自的成本、风险和受益者是谁？

### 例子（原创性人工复核）

> 这个流程一直存在，所以不需要重新设计，哪怕它已经造成大量浪费。

### 何时可能不是谬误

现状具有协调、转换成本和既得预期，这些是真实因素；但不能自动证明现状最优。

### 容易混淆

status quo bias、appeal to tradition、loss aversion

### 相关条目

诉诸传统 (`appeal-to-tradition`)、现状偏差 (`status-quo-bias`)、损失厌恶 (`loss-aversion`)


---

## 穷尽努力谬误

**Fallacy of Exhaustive Effort** · `exhaustive-effort-fallacy`

- 类型：非形式谬误
- 默认影响：中等
- 别名：次优条件叠加、最大化剩余条件、second best fallacy

### 定义

在无法满足最优方案的全部条件时，假定尽可能多满足其余条件就必然产生次优结果，却忽略条件之间的依赖和替代关系。

### 推理式

```text
最佳方案要求 A+B+C；C 无法满足；于是尽量满足 A+B；因此 B 一定优于其他可行方案。
```

### 诊断问题

1. 各项条件是否彼此独立，还是必须联合满足？
2. 是否比较了违反部分条件但整体更优的替代方案？
3. “尽可能多”是以什么目标函数衡量？

### 例子（原创性人工复核）

> 完美医疗方案需要低成本、全覆盖和零等待；零等待做不到，所以先把成本压到最低就一定是次优选择。

### 何时可能不是谬误

在条件近似独立、目标可加且没有替代互动时，逐项补齐可以合理；政策和复杂系统通常需要比较整体方案。

### 容易混淆

涅槃谬误、虚假两难、分解式政策

### 相关条目

涅槃谬误 (`nirvana-fallacy`)、虚假两难 (`false-dilemma`)、滑坡谬误 (`slippery-slope`)


[返回分类索引](../catalog-index.md)
