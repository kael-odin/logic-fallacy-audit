# 论证图与问题关系图

可视化用于帮助读者看清支持链和问题位置，不替代原文证据。图应能从报告中追溯到结论、前提、隐含前提和问题卡。

## 1. 生成命令

```bash
python scripts/fallacy_cli.py diagram examples/sample-report.md --kind argument
python scripts/fallacy_cli.py diagram examples/sample-report.md --kind issues
python scripts/fallacy_cli.py diagram examples/sample-report.md --kind compare
```

三种图：

| 类型 | 内容 |
|---|---|
| `argument` | 结论、显式前提和重建的隐含前提 |
| `issues` | 论证结构与问题节点 |
| `compare` | 修复前、问题和修复后 |

`--json` 同时返回结构化节点和 Mermaid 文本。

## 2. 图的语义

- 实线箭头表示报告声明的支持方向。
- 虚线 `assumption` 表示隐含前提支持主结论。
- 虚线 `affects` 表示问题影响主论证，不声称已精确绑定某个前提。
- `repair` 表示修复条件指向改写方向，不表示改写已经得到事实证明。
- 改写节点只是报告中的建议，不是作者原话。

如果报告没有写明问题具体攻击哪条前提，图不得自行推断更精确的边。

## 3. 颜色

| 节点 | 含义 |
|---|---|
| 黄色 | 最终结论 |
| 蓝色 | 显式前提 |
| 紫色 | 重建的隐含前提 |
| 红色 | 问题卡 |
| 绿色 | 改写方向 |

颜色只帮助扫描，不承担逻辑含义。

## 4. 文本约束

- 节点只放中性摘要，不放完整段落。
- 长引文继续使用报告中的 `[Lx-Ly]`。
- 一个问题节点只保留一个主标签。
- 多结论文本应分别生成图，不把所有结论强行合成一个节点。
- 图中出现的人格化语言应退回报告改写。

## 5. 输出格式

命令生成 ```mermaid 代码块，可直接放入 GitHub Markdown。仓库不把图当作独立证据，也不保证 Mermaid 在所有编辑器中一致渲染。

## 6. 当前限制

- 生成器读取六个核心报告中已有的论证地图和问题卡。
- 生成器不判断问题最精确地攻击哪条前提。
- 生成器不自动布局大型论证网络。
- 图不替代误报复核、事实状态或人工 rubric。
