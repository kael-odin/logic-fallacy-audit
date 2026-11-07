# 架构

## 1. 分层

```text
SKILL.md
  └─ 分析协议 / 报告规范 / 误报防线
       └─ 分类知识库（catalog）
            └─ 生成的人类可读目录
                 └─ CLI / tests / CI
                       └─ 报告结构校验（report_lint）
                            └─ 源文本映射（source_map）
                                 └─ 图表生成（report_diagram）
```

## 2. 唯一数据源

`catalog/*.toml` 是知识库唯一数据源。`references/catalog/`、`references/catalog-index.md` 和 `references/adjacent-biases.md` 由脚本生成，不应手工修改。

`references/knowledge-coverage.md` 也从同一数据源生成，用于记录全部条目的字段完整性、分类分布、核心十类覆盖和复现命令。

这样处理的原因：

- 避免文档与检索结果不一致；
- 让新增条目可通过 schema 校验；
- 支持中英文搜索、分类统计与关联检查；
- 让人工阅读仍然方便。

生成器会移除 `references/catalog/` 中不再属于当前分类集合的旧 Markdown 文件。`render --check` 同时检查缺失、内容漂移和残留文件。

## 3. 条目字段

| 字段 | 用途 |
|---|---|
| `id` | 稳定英文标识 |
| `name_zh` / `name_en` | 中文与英文主名称 |
| `aliases` | 检索别名 |
| `category` | 主分类 |
| `kind` | 形式、非形式、辩证、修辞、统计、偏差 |
| `severity` | 默认影响等级，不是恶意等级 |
| `definition` | 失败机制 |
| `pattern` | 论证式 |
| `diagnostic` | 至少两个诊断问题 |
| `example` | 示例；要求原创并使用低争议场景，原创性由人工复核 |
| `boundary` | 可能合理的情形 |
| `confusions` | 相邻概念 |
| `related` | 关联条目 ID |

## 4. 运行时

Skill 被调用时：

1. 读取入口和核心协议。
2. 根据输入选择模式。
3. 按分类索引只读取相关目录。
4. 长文本生成候选块、SHA-256 与引文行号。
5. 输出报告。

Skill 不依赖网络、数据库或第三方 Python 包。目录检索可由 CLI 完成，也可让模型直接读取生成后的 Markdown。

## 5. 源文本映射

`scripts/source_map.py` 对保存的 UTF-8 文本执行确定性处理：

```text
原文
  → BOM / 换行归一化
  → 段落候选块
  → SHA-256
  → 精确引文定位
  → Lx-Ly 字符范围
```

候选块不是自动认定的论证单元。工具只负责来源定位，结论、前提和论证边界由分析协议判断。

## 6. 生成流水线

```text
catalog/*.toml
  → load_catalog()
  → validate_catalog()
  → build Markdown
  → write references/
  → render --check in CI
```

如果目录字段、关联 ID 或生成文件不一致，CI 失败。

## 7. 失败模式

| 失败 | 防线 |
|---|---|
| 只贴标签 | SKILL 要求先重建并解释机制 |
| 误报 | 善意解释、边界、反例、置信度 |
| 条目漂移 | 自动生成目录 + 漂移检查 |
| 同义词重复 | 别名归并、关联 ID |
| 认知偏差滥用 | 独立 bias 分类与报告约束 |
| 事实越界 | 单独事实状态和边界说明 |
| 生成器破坏链接 | Markdown 链接检查 |
| 旧分类文件残留 | 生成目录白名单 + 自动清理 |
| 别名与其他 ID/主名冲突 | 全局别名冲突检查 |
| 条目缺 ID 导致校验崩溃 | 安全 ID 读取与结构化错误 |
| 报告章节或证据字段缺失 | `report_lint.py` + CI 样例门禁 |
| 引文无法追溯或源文本版本漂移 | `source_map.py` + SHA-256 + 行号定位 |
| 图表关系超出报告证据 | 只从论证地图与问题卡生成，不推断精确攻击目标 |
| 行为退化 | 固定评测集 + rubric |
| 条目数量被误当成知识完整性 | 生成知识覆盖审计 + 字段完整性门槛 |
| 解说表达削弱证据 | Explainer 复用 Full 的问题卡和边界校验 |

## 8. 扩展原则

- 先复用现有条目，再新增。
- 新增的必须是可识别、可解释、可边界的推理机制。
- 非谬误概念不放入 fallacy 列表，除非明确标记为偏差或修辞模式。
- 不按网络热度无限堆词条。
- 不在同一条目复制多份定义。
