# 模型运行账本

`ledger.jsonl` 记录每次评测运行。`fixture` 只用于验证评测流水线，不表示真实模型能力；只有 `model` 记录才能用于跨模型比较。

## 生成报告清单

创建一个 JSON 映射，把评测 ID 指向生成的 Markdown 报告：

```json
{
  "eval-044-workplace-generalization": "reports/model-a/eval-044.md",
  "eval-045-supplement-anecdote": "reports/model-a/eval-045.md"
}
```

报告必须先通过或明确记录 lint 结果。评测器会检查：

- 报告结构 lint；
- `must_detect` 是否出现在问题卡的判定字段；
- `may_detect` 是否出现；
- `must_not_assert` 作为人工复核项保留；
- 模型、日期、Prompt 版本和报告路径。

## 记录一次真实运行

```bash
python scripts/eval_runner.py run \
  --manifest reports/model-a/manifest.json \
  --run-id model-a-2026-11-08-p1 \
  --run-type model \
  --model model-a \
  --date 2026-11-08 \
  --prompt-version p1
```

运行 ID 必须唯一。失败案例会保留在账本中，不因低分删除。

## 生成看板

```bash
python scripts/eval_runner.py dashboard
python scripts/eval_runner.py dashboard --check
```

看板输出到 [docs/model-run-dashboard.md](../../docs/model-run-dashboard.md)。

## 解释边界

- 自动检测只看 `判定` 字段，不能证明论证质量。
- `must_not_assert` 需要人工检查，不能把抽象禁止项当字符串匹配。
- 不同 Prompt 版本不能合并成单一分数。
- 样例报告和 curated fixture 不计作真实模型运行。
