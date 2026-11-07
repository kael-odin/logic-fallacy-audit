# v1.5 评测运营首批审查

## 审查范围

- 结构化误报与回归账本。
- 自动生成的误报看板。
- 政策、统计和长对话专项 rubric。
- CLI、CI、必需文件与文档链接。

## 结论

评测运营第一批能力已落地。`evals/regressions.jsonl` 成为回归状态唯一数据源，`docs/regression-dashboard.md` 由脚本生成，CI 检查账本有效性和生成漂移。

专项 rubric 不再用同一张泛化评分表覆盖全部场景。政策、统计和长对话各自有 6 个维度，并关联现有评测案例。

## 当前账本

| 状态 | 数量 |
|---|---:|
| 已修复 | 9 |
| 仍存在 | 3 |
| 已失效 | 0 |
| 边界变化 | 0 |

仍存在的三项：

- 反讽与转述长对话评测缺口。
- 多论证单元输入评测缺口。
- 不同模型、日期和提示词版本的运行账本已建立，真实模型覆盖仍待补。

## 专项 rubric

- 政策：目标、机制、成本承担、替代方案、实施不确定性、事实与规范分离。
- 统计：估计量、基准率、抽样、因果、效应与不确定性、冲突证据。
- 长对话：说话者归属、回应忠实度、举证责任、上下文、证据追踪、动机边界。

## 验证

```bash
python scripts/fallacy_cli.py regression-dashboard --check
python -W error -m unittest discover -s tests -v
ruff check scripts tests
ruff format --check scripts tests
```

自动测试覆盖账本有效性、未知评测引用、生成漂移、专项 rubric 维度数量与案例引用。

模型运行器另以 curated fixture 验证 2 条样例报告，不能把 fixture 当作真实模型成绩。

## 边界

看板记录的是仓库已知回归与缺口，不是模型评分排行。专项 rubric 仍需人工或真实模型运行才能产生分值。
