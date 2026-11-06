# Contributing

欢迎补充谬误条目、中文语料、评测案例与报告模板。先保持结构一致，再增加数量。

## 新增或修改分类条目

1. 在 `catalog/` 下找到最合适的分类文件。
2. 复制现有条目并分配稳定、唯一的 `id`。
3. 至少填写以下字段：

```toml
id = "stable-kebab-id"
name_zh = "中文名"
name_en = "English Name"
aliases = ["别名"]
category = "category-id"
kind = "formal"
severity = 2
definition = "..."
pattern = "..."
diagnostic = ["...", "..."]
example = "..."
boundary = "..."
confusions = ["..."]
related = []
```

4. 运行：

```bash
python scripts/fallacy_cli.py validate --strict
python scripts/fallacy_cli.py render
python -m unittest discover -s tests -v
```

5. 提交 `catalog/` 与生成后的 `references/catalog/`、`references/catalog-index.md` 和 `references/adjacent-biases.md`。

## 条目质量标准

- `definition` 说明推理机制，不只写“这是错误”。
- `pattern` 能表达主张之间的关系。
- `diagnostic` 至少包含两个可回答的问题。
- `example` 是原创短例，不能大段复制教材或视频文案。
- `boundary` 说明该模式何时可能合理。
- `confusions` 说明最容易混淆的邻近概念。
- 不要把人格评价、动机猜测或单一情绪词当作谬误证据。

## 命名与归类

- 一个失败机制只建立一个主条目。
- 别名写入 `aliases`，不要为同义词重复建条。
- 跨类别条目使用 `related` 关联。
- 传统名称不统一时，优先采用中文传播广、英文可检索且定义较稳定的名称。
- 认知偏差不是逻辑谬误，必须放在 `catalog/adjacent-biases.toml`。

## 提交前检查

```bash
git diff --check
python scripts/fallacy_cli.py validate --strict
python scripts/fallacy_cli.py render --check
python -m unittest discover -s tests -v
```
