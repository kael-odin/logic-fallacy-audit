from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from catalog_lib import (  # noqa: E402
    expected_generated_files,
    load_catalog,
    validate_repository,
)


class DocumentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = load_catalog(ROOT)

    def test_repository_contracts(self) -> None:
        issues = validate_repository(self.catalog)
        self.assertEqual([], [issue.format() for issue in issues])

    def test_generated_files_are_current(self) -> None:
        for path, expected in expected_generated_files(self.catalog).items():
            self.assertTrue(path.exists(), str(path))
            self.assertEqual(expected, path.read_text(encoding="utf-8"), str(path))

    def test_sample_report_has_required_sections(self) -> None:
        text = (ROOT / "examples" / "sample-report.md").read_text(encoding="utf-8")
        for heading in [
            "## 结论摘要",
            "## 论证地图",
            "## 关键问题",
            "## 反向检验",
            "## 改写建议",
            "## 边界说明",
        ]:
            self.assertIn(heading, text)
        self.assertIn("草率概括", text)
        self.assertIn("错误归因", text)

    def test_eval_suite_is_parseable_and_nonempty(self) -> None:
        lines = (ROOT / "evals" / "cases.jsonl").read_text(encoding="utf-8").splitlines()
        cases = [json.loads(line) for line in lines if line.strip()]
        self.assertGreaterEqual(len(cases), 10)
        self.assertTrue(any(not item["must_detect"] for item in cases))

    def test_core_reference_contains_user_required_ten(self) -> None:
        text = (ROOT / "references" / "core-fallacies.md").read_text(encoding="utf-8")
        for term in [
            "稻草人谬误",
            "滑坡谬误",
            "虚假两难",
            "诉诸情感",
            "错误归因",
            "人身攻击",
            "诉诸权威",
            "以偏概全",
            "偷换概念",
            "循环论证",
        ]:
            self.assertIn(term, text)


if __name__ == "__main__":
    unittest.main()
