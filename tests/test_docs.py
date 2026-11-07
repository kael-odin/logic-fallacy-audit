from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from catalog_lib import (
    expected_generated_files,
    generated_drift,
    load_catalog,
    validate_repository,
    write_generated_files,
)


class DocumentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = load_catalog(ROOT)

    def test_repository_contracts(self) -> None:
        issues = validate_repository(self.catalog)
        self.assertEqual([], [issue.format() for issue in issues])

    def test_missing_repository_files_report_errors_without_crashing(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            issues = validate_repository(self.catalog, Path(temporary))
        codes = {issue.code for issue in issues}
        self.assertIn("required-file", codes)
        self.assertIn("generated-drift", codes)

    def test_generated_files_are_current(self) -> None:
        for path, expected in expected_generated_files(self.catalog).items():
            self.assertTrue(path.exists(), str(path))
            self.assertEqual(expected, path.read_text(encoding="utf-8"), str(path))

    def test_stale_generated_file_is_detected_and_removed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            stale = root / "references" / "catalog" / "99-stale.md"
            manual = root / "references" / "catalog" / "notes.md"
            stale.parent.mkdir(parents=True)
            stale.write_text("stale\n", encoding="utf-8")
            manual.write_text("manual\n", encoding="utf-8")
            drift = generated_drift(self.catalog, root)
            self.assertIn(stale, drift)
            self.assertNotIn(manual, drift)
            _written, removed = write_generated_files(self.catalog, root)
            self.assertIn(stale, removed)
            self.assertFalse(stale.exists())
            self.assertTrue(manual.exists())

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
        self.assertGreaterEqual(len(cases), 30)
        self.assertTrue(any(not item["must_detect"] for item in cases))
        self.assertEqual(
            {"quick", "full", "debate", "teaching"},
            {item["mode"] for item in cases},
        )

    def test_readme_counts_match_catalog(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(
            f"**{len(self.catalog.entries)} 条结构化条目**："
            f"{len(self.catalog.fallacy_entries)} 条谬误/论证模式，"
            f"{len(self.catalog.bias_entries)} 条与谬误相邻的认知偏差。",
            text,
        )
        english = (ROOT / "README.en.md").read_text(encoding="utf-8")
        self.assertIn(
            f"{len(self.catalog.entries)} structured entries: "
            f"{len(self.catalog.fallacy_entries)} fallacies or argument patterns "
            f"and {len(self.catalog.bias_entries)} adjacent cognitive biases.",
            english,
        )

    def test_content_audit_record_exists(self) -> None:
        path = ROOT / "docs" / "content-audit-2026-11-07.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("240", text)
        self.assertIn("别名冲突", text)

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
