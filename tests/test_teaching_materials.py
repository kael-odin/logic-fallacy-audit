from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from catalog_lib import load_catalog
from report_lint import lint_report_text


class TeachingMaterialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = load_catalog(ROOT)

    def test_exercise_bank_has_ten_answered_prompts(self) -> None:
        text = (ROOT / "examples" / "exercises.md").read_text(encoding="utf-8")
        self.assertEqual(10, len(re.findall(r"(?m)^## 练习\s+\d+", text)))
        self.assertEqual(10, text.count("<details>"))
        self.assertEqual(10, text.count("<summary>答案</summary>"))

    def test_exercise_primary_ids_exist(self) -> None:
        text = (ROOT / "examples" / "exercises.md").read_text(encoding="utf-8")
        ids = re.findall(r"\*\*主判\*\*：`([^`]+)`", text)
        self.assertEqual(10, len(ids))
        self.assertEqual(set(), set(ids) - set(self.catalog.entry_by_id))

    def test_rewrite_examples_have_before_and_after(self) -> None:
        text = (ROOT / "examples" / "rewrites.md").read_text(encoding="utf-8")
        self.assertEqual(6, len(re.findall(r"(?m)^##\s+\d+\.", text)))
        self.assertEqual(6, text.count("**原句**："))
        self.assertEqual(6, text.count("**改写**："))

    def test_teaching_report_passes_teaching_lint(self) -> None:
        path = ROOT / "examples" / "teaching-report.md"
        result = lint_report_text(
            path.read_text(encoding="utf-8"),
            path,
            profile="teaching",
        )
        self.assertEqual([], [issue.format() for issue in result.issues])


if __name__ == "__main__":
    unittest.main()
