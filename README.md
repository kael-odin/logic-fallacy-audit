# 逻辑谬误分析 Skill

[![validate](https://github.com/kael-odin/logic-fallacy-audit/actions/workflows/validate.yml/badge.svg)](https://github.com/kael-odin/logic-fallacy-audit/actions/workflows/validate.yml)

把一段文字拆成**主张、证据、隐藏前提、推理断点与可修正版本**。

这不是“贴标签式找茬”工具。它会先重建对方最强版本，再判断问题出在演绎有效性、证据强度、论证责任、语言歧义还是说服手法。报告必须给原文依据、置信度和误判边界。

## 它适合什么

- 分析社交媒体长文、评论区争论、短视频口播稿或辩论发言。
- 检查文章中的因果跳跃、统计误读、偷换概念、稻草人、循环论证。
- 为反驳准备“引用原句 → 指出断点 → 给出反例 → 说明何种证据能修复”的结构。
- 教学、写作和审稿时区分“观点不同”“证据不足”“逻辑无效”“修辞操纵”。

## 它刻意不做什么

- 不根据一段文字判断发言者的人格、动机或精神状态。
- 不因为结论令人反感，就宣布论证错误。
- 不把认知偏差、宣传技巧、谬误名称混为一谈。
- 不把“有关联”写成“已证明因果”，也不把“有专家说过”当作事实核验。
- 不在缺少上下文时给出虚假的高置信度。

## 核心能力

| 能力 | 产出 |
|---|---|
| 论证重建 | 结论、显式前提、必要隐含前提、论证类型 |
| 四层评估 | 形式有效性、证据支持、辩证充分性、修辞效果 |
| 谬误匹配 | 名称、机制、原文证据、置信度、修复条件 |
| 误报防御 | 最强版本、反例、语境相关判定 |
| 改写建议 | 补充证据后的可检验论证 |
| 报告模式 | `quick`、`full`、`debate`、`teaching` |

## 快速使用

### 在 Codex 中安装

Windows PowerShell：

```powershell
git clone https://github.com/kael-odin/logic-fallacy-audit.git "$env:USERPROFILE\.codex\skills\logic-fallacy-audit"
```

macOS / Linux：

```bash
git clone https://github.com/kael-odin/logic-fallacy-audit.git "${CODEX_HOME:-$HOME/.codex}/skills/logic-fallacy-audit"
```

重新打开 Codex 后，可显式调用：

```text
$logic-fallacy-audit 分析下面这段话，使用 full 模式：
“……”
```

### 直接使用仓库

```bash
python scripts/fallacy_cli.py validate
python scripts/fallacy_cli.py stats
python scripts/fallacy_cli.py search "因果"
python scripts/fallacy_cli.py show post-hoc
python scripts/fallacy_cli.py render
```

仅依赖 Python 3.11+ 标准库。

## 工作流

```text
原文
  ↓
切分事实、观点、规范判断与转述
  ↓
重建最强论证
  ↓
判断推理任务：演绎 / 归纳 / 因果 / 统计 / 解释 / 规范 / 政策
  ↓
四层评估
  ↓
匹配知识条目并做误报复核
  ↓
输出带原文证据与置信度的报告
  ↓
给出更强版本和修复所需证据
```

## 一个最小示例

原句：

> 公司去年招的三个应届生都离职了，所以现在的年轻人都吃不了苦。

报告不会只写“以偏概全”。它会先说明：

1. 结论是“现在的年轻人整体如何”，样本却只有同一公司的三个人。
2. 离职也可能由岗位、管理、薪酬、通勤或招聘匹配造成，原文没有排除这些解释。
3. “吃不了苦”缺少可操作标准，可能把不同情况重新描述后再归因。
4. 更强版本应改成：“在这家公司，三名应届生半年内离职；离职访谈显示共同原因之一是工作强度，但这仍不足以推广到所有年轻人。”

完整示例见 [examples/sample-report.md](examples/sample-report.md)。

## 知识库

知识库按论证功能分类，而不是只按传统教科书目录排列。当前 v1 覆盖：

**221 条结构化条目**：189 条谬误/论证模式，32 条与谬误相邻的认知偏差。

- 形式与演绎错误
- 相关性与人身攻击
- 预设、责任与辩证规则
- 歧义、定义与语言操纵
- 因果、归纳与类比
- 统计、概率与样本
- 解释、模式与阴谋论式推理
- 规范、政策与价值推理
- 公共说服与宣传手法
- 与谬误相邻的认知偏差

人类可读目录从 [references/catalog-index.md](references/catalog-index.md) 进入。结构化数据在 [catalog/](catalog/)；修改数据后运行 `python scripts/fallacy_cli.py render`，生成文件会同步更新。

## 报告质量原则

每份正式报告必须遵守 [references/report-spec.md](references/report-spec.md)：

- 先描述论证，再命名谬误。
- 每个问题引用原文，并解释“为什么结论还不能由此推出”。
- 区分 `确认 / 较可能 / 语境相关 / 不构成谬误`。
- 对每个高影响发现给出最强反方解释。
- 把修复条件写成可检查的证据，而不是“多思考”。
- 结尾明确说明文字分析无法证明什么。

## 仓库结构

```text
.
├── SKILL.md                    # Skill 入口
├── README.md                   # 中文项目说明
├── agents/openai.yaml          # UI 元数据
├── catalog/                    # 结构化知识库（唯一数据源）
├── references/                 # 分析协议、分类和生成目录
├── assets/                     # 报告模板与图标
├── examples/                   # 完整示例报告
├── evals/                      # 行为评测用例
├── scripts/                    # 校验、检索、生成工具
├── tests/                      # 标准库单元测试
└── .github/workflows/          # CI 质量门
```

## 设计与规划

- [产品规格](docs/product-spec.md)：目标用户、场景、模式、非目标与成功指标。
- [架构说明](docs/architecture.md)：唯一数据源、生成流水线与失败模式。
- [质量方案](docs/quality.md)：自动检查、人工评测与误报回归。
- [路线图](docs/roadmap.md)：v1.0 状态与后续方向。
- [核心十类速查](references/core-fallacies.md)：你给出的十类可直接从这里进入。
- [逻辑基础](references/logic-basics.md)：有效性、条件、量词、归纳、概率与规范推理。
- [任务矩阵](references/task-matrix.md)：按演绎、因果、统计、政策等任务选择分析路线。
- [模式示例](examples/modes.md)：Quick、Full、Debate、Teaching 的输出差异。

## 开发与验证

```bash
python scripts/fallacy_cli.py validate --strict
python -m unittest discover -s tests -v
python scripts/fallacy_cli.py render --check
```

CI 会检查：

- Skill frontmatter 与必要引用；
- 目录 ID、别名、关联项和字段完整性；
- 分类数量与生成文档是否漂移；
- 报告模板必需章节；
- 评测样例结构；
- Python 脚本与单元测试。

## 来源与边界

本项目的分类综合了形式逻辑、非形式逻辑、论证理论、传播学与认知科学中的常见概念。不同教材对同一谬误的命名、边界和归类并不统一；本仓库优先考虑“能否稳定用于文本分析”，不宣称存在唯一正统分类。

主要参考方向与引用政策见 [references/research-sources.md](references/research-sources.md)。仓库不复制受版权保护教材的大段内容，例子和报告均为本项目改写或原创。

## 致谢

分析风格受到短篇批判性思维科普内容的启发，尤其参考了 B 站 UP 主“WY的灯塔”常见的“引语切入、拆隐藏前提、找逻辑断点、给反例与修复方式”表达节奏。本项目与其无隶属关系，也不复制其视频文案或观点。

## License

[MIT](LICENSE)
