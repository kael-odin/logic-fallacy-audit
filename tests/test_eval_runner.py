from __future__ import annotations

import sys
import unittest
from dataclasses import replace
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from eval_runner import (
    dashboard_is_current,
    detect_entry_ids,
    evaluate_manifest,
    load_cases,
    load_ledger,
    load_manifest,
    validate_ledger,
)


class EvalRunnerTests(unittest.TestCase):
    def test_case_suite_has_fixture_cases(self) -> None:
        cases = load_cases()
        self.assertGreaterEqual(len(cases), 45)
        self.assertIn("eval-044-workplace-generalization", {case.id for case in cases})

    def test_curated_fixture_passes(self) -> None:
        record = evaluate_manifest(
            load_manifest(ROOT / "evals" / "model-runs" / "fixture-manifest.json"),
            run_id="fixture-test",
            run_type="fixture",
            model="fixture",
            date="2026-11-07",
            prompt_version="test",
        )
        self.assertEqual(3, len(record.results))
        self.assertTrue(all(result.passed for result in record.results))
        self.assertIn("hasty-generalization", record.results[0].detected)
        valid_result = next(
            result for result in record.results if result.case_id == "eval-060-full-valid-argument"
        )
        self.assertEqual((), valid_result.detected)

    def test_nested_alias_is_not_double_counted(self) -> None:
        report = """# 报告

## 关键问题

### 1. 处境式攻击

**判定**

`Confirmed` · Circumstantial Ad Hominem · Confidence: High
"""
        detected = detect_entry_ids(report)
        self.assertIn("ad-hominem-circumstantial", detected)
        self.assertNotIn("ad-hominem-abusive", detected)

    def test_ledger_is_valid(self) -> None:
        records = load_ledger()
        case_ids = {case.id for case in load_cases()}
        self.assertEqual([], validate_ledger(records, case_ids))
        self.assertGreaterEqual(len(records), 1)

    def test_generated_dashboard_is_current(self) -> None:
        self.assertTrue(dashboard_is_current())

    def test_duplicate_run_id_is_reported(self) -> None:
        records = load_ledger()
        duplicate = replace(records[0])
        issues = validate_ledger(
            [duplicate, duplicate],
            {case.id for case in load_cases()},
        )
        self.assertIn("duplicate run id: fixture-2026-11-07-curated", issues)


if __name__ == "__main__":
    unittest.main()
