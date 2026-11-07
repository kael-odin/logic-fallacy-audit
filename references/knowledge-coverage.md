# 知识覆盖审计

> 本文件由 `python scripts/fallacy_cli.py render` 生成。请修改 `catalog/` 后重新生成。

审计快照：**2026-11-07**。本表证明目录的结构完整性与可诊断性，不宣称覆盖所有哲学传统。

## 总览

| 指标 | 数量 |
|---|---:|
| 结构化条目 | 260 |
| 谬误/论证模式 | 228 |
| 相邻认知偏差 | 32 |
| 主分类 | 10 |
| 同时通过全部结构门槛 | 260 |

## 字段完整性

| 分析维度 | 通过 | 覆盖率 |
|---|---:|---:|
| 定义至少 20 字 | 260/260 | 100.0% |
| 独立推理式 | 260/260 | 100.0% |
| 至少 2 个诊断问题 | 260/260 | 100.0% |
| 原创例子 | 260/260 | 100.0% |
| 误判边界 | 260/260 | 100.0% |
| 至少 1 个易混淆项 | 260/260 | 100.0% |
| 至少 1 个关联条目 | 260/260 | 100.0% |
| 至少 1 个检索别名 | 260/260 | 100.0% |

每个条目都具备：

- 可复述的失败机制，而不是只有名称；
- 能用于定位断点的推理式；
- 至少两个诊断问题；
- 一个原创例子；
- 一条“何时可能不是谬误”的边界；
- 易混淆概念和关联条目；
- 中英文检索入口与至少一个别名。

## 分类覆盖

| 分类 | 条目数 | 报告提示 |
|---|---:|---|
| 形式与演绎错误 (`formal`) | 20 | 仅用于存在明确演绎推理的文本。 |
| 相关性与人身攻击 (`relevance`) | 42 | 先区分主张真假、证据可信度和说话者资格。 |
| 预设、责任与辩证规则 (`presumption`) | 33 | 明确初始主张、举证责任和可反驳条件。 |
| 歧义、定义与语言 (`ambiguity`) | 26 | 标出同一词在不同出现处的实际含义。 |
| 因果、归纳与类比 (`causal`) | 27 | 检查样本、机制、时序、对照和替代解释。 |
| 统计、概率与样本 (`statistical`) | 24 | 明确分母、样本来源、比较对象和不确定性。 |
| 解释、模式与阴谋论式推理 (`explanation`) | 14 | 比较至少两个竞争解释，并检查可反驳预测。 |
| 规范、政策与价值 (`normative`) | 18 | 分开目标、手段、副作用、分配与价值排序。 |
| 公共说服与宣传 (`rhetorical`) | 24 | 描述说服机制和对话效果，不推断发言者动机。 |
| 认知偏差 (`bias`) | 32 | 只作为背景解释，不单独充当谬误结论。 |

## 核心十类

| 中文名 | English | ID | 分类 | 诊断问题 |
|---|---|---|---|---:|
| 稻草人谬误 | Straw Man | `straw-man` | 相关性与人身攻击 | 2 |
| 滑坡谬误 | Slippery Slope | `slippery-slope` | 因果、归纳与类比 | 3 |
| 虚假两难 | False Dilemma | `false-dilemma` | 预设、责任与辩证规则 | 2 |
| 诉诸情感 | Appeal to Emotion | `appeal-to-emotion` | 相关性与人身攻击 | 2 |
| 虚假因果 | False Cause | `false-cause` | 因果、归纳与类比 | 2 |
| 人身攻击 | Abusive Ad Hominem | `ad-hominem-abusive` | 相关性与人身攻击 | 2 |
| 诉诸权威 | Appeal to Authority | `appeal-to-authority` | 相关性与人身攻击 | 3 |
| 草率概括 | Hasty Generalization | `hasty-generalization` | 因果、归纳与类比 | 3 |
| 偷换概念 | Equivocation | `equivocation` | 歧义、定义与语言 | 2 |
| 循环论证 | Circular Reasoning | `circular-reasoning` | 预设、责任与辩证规则 | 2 |

核心十类的逐项测试、反例、常见误判和报告句式见 [`core-fallacies.md`](core-fallacies.md)。

## 外部参照

覆盖差距检查参考以下公开资料，但条目定义、例子和边界均为本项目重新整理：

- [Stanford Encyclopedia of Philosophy: Fallacies](https://plato.stanford.edu/entries/fallacies/)
- [Internet Encyclopedia of Philosophy: Fallacies](https://iep.utm.edu/fallacy/)
- [Purdue OWL: Logical Fallacies](https://owl.purdue.edu/owl/general_writing/academic_writing/logic_in_argumentative_writing/fallacies.html)
- [UNC Writing Center: Fallacies](https://writingcenter.unc.edu/tips-and-tools/fallacies/)
- [Wikipedia: List of Fallacies](https://en.wikipedia.org/wiki/List_of_fallacies)

外部资料用于名称与概念差距核对。它们彼此并不完全一致，因此本仓库不把任何单一清单当作绝对标准。

## 复现

```bash
python scripts/fallacy_cli.py coverage
python scripts/fallacy_cli.py coverage --json
python scripts/fallacy_cli.py validate --strict
python scripts/fallacy_cli.py render --check
```

## 解释边界

- 结构完整不等于每条定义都无需修订。
- 条目数量不等于分析质量；报告仍需论证重建、原文证据和误报复核。
- 同一概念可能因学派不同而使用不同名称；别名只用于检索，不用于制造额外发现。
- 专业领域论证仍需相应领域知识与事实核查。
