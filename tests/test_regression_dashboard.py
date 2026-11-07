from __future__ import annotations

import sys
import unittest
from dataclasses import replace
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from regression_dashboard import (
    build_dashboard,
    dashboard_is_current,
    load_case_ids,
    load_regressions,
    validate_regressions,
)


class RegressionDashboardTests(unittest.TestCase):
    def test_regression_ledger_is_valid(self) -> None:
        records = load_regressions()
        issues = validate_regressions(records, load_case_ids())
        self.assertEqual([], [issue.format() for issue in issues])

    def test_dashboard_contains_status_sections(self) -> None:
        text = build_dashboard(load_regressions())
        self.assertIn("## 仍存在", text)
        self.assertIn("## 已修复", text)
        self.assertIn("`citation-range-unchecked`", text)
        self.assertIn("`model-run-ledger-gap`", text)

    def test_unknown_case_reference_is_reported(self) -> None:
        records = load_regressions()
        bad = replace(records[0], case_ids=("eval-not-found",))
        issues = validate_regressions([bad], load_case_ids())
        self.assertIn("unknown-case", {issue.code for issue in issues})

    def test_generated_dashboard_is_current(self) -> None:
        self.assertTrue(dashboard_is_current())


if __name__ == "__main__":
    unittest.main()
