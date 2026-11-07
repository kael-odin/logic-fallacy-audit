from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from report_lint import lint_report_text
from source_map import build_source_document

QUICK_REPORT = """# 快速逻辑分析

## 结论摘要

这是一个简短结论。

## 论证地图

结论依赖流行度。

## 关键问题

> 很多人在用，所以它最好。

`确认` · 诉诸流行 · 置信度：高

## 反向检验

需要比较安全测试。

## 改写建议

> 下载量只说明使用规模，不能单独证明安全。

## 边界说明

- 下载量可以作为市场接受度证据。
"""


class ReportLintTests(unittest.TestCase):
    def source_document(self):
        source_path = ROOT / "examples" / "long-text-source.txt"
        return build_source_document(
            source_path.read_text(encoding="utf-8"),
            path=str(source_path),
        )

    def test_sample_report_passes_full_profile(self) -> None:
        path = ROOT / "examples" / "sample-report.md"
        result = lint_report_text(
            path.read_text(encoding="utf-8"),
            path,
            profile="full",
        )
        self.assertEqual([], [issue.format() for issue in result.issues])

    def test_explainer_report_passes_explainer_profile(self) -> None:
        path = ROOT / "examples" / "explainer-report.md"
        result = lint_report_text(
            path.read_text(encoding="utf-8"),
            path,
            profile="explainer",
        )
        self.assertEqual([], [issue.format() for issue in result.issues])

    def test_missing_sections_and_fields_are_reported(self) -> None:
        bad = "# 报告\n\n## 结论摘要\n\n只有一句。"
        result = lint_report_text(bad, Path("bad.md"), profile="full")
        codes = {issue.code for issue in result.issues}
        self.assertIn("missing-section", codes)
        self.assertIn("no-finding-cards", codes)

    def test_missing_issue_field_is_reported(self) -> None:
        sample = (ROOT / "examples" / "sample-report.md").read_text(encoding="utf-8")
        bad = sample.replace("**相关但不主判**", "", 1)
        result = lint_report_text(bad, Path("missing-field.md"), profile="full")
        self.assertIn("issue-field", {issue.code for issue in result.issues})

    def test_empty_issue_field_is_reported(self) -> None:
        sample = (ROOT / "examples" / "sample-report.md").read_text(encoding="utf-8")
        bad = sample.replace(
            "提供离职访谈、岗位压力指标、同时期留任者比较和替代原因数据。",
            "",
            1,
        )
        result = lint_report_text(bad, Path("empty-field.md"), profile="full")
        self.assertIn("issue-field-empty", {issue.code for issue in result.issues})

    def test_duplicate_required_section_is_reported(self) -> None:
        sample = (ROOT / "examples" / "sample-report.md").read_text(encoding="utf-8")
        bad = sample.replace(
            "## 边界说明",
            "## 边界说明\n\n这是重复章节。\n\n## 边界说明",
            1,
        )
        result = lint_report_text(bad, Path("duplicate-section.md"), profile="full")
        self.assertIn("duplicate-section", {issue.code for issue in result.issues})

    def test_quick_and_teaching_profiles_use_minimal_rules(self) -> None:
        for profile in ("quick", "teaching"):
            with self.subTest(profile=profile):
                result = lint_report_text(
                    QUICK_REPORT,
                    Path(f"{profile}.md"),
                    profile=profile,
                )
                self.assertEqual([], [issue.format() for issue in result.issues])

    def test_template_placeholders_are_rejected(self) -> None:
        template = (ROOT / "assets" / "report-template.md").read_text(encoding="utf-8")
        result = lint_report_text(template, Path("template.md"), profile="full")
        self.assertIn("placeholder", {issue.code for issue in result.issues})

    def test_english_sample_passes_with_source_locations(self) -> None:
        path = ROOT / "examples" / "sample-report.en.md"
        result = lint_report_text(
            path.read_text(encoding="utf-8"),
            path,
            profile="full",
            source_document=self.source_document(),
            require_locators=True,
        )
        self.assertEqual([], [issue.format() for issue in result.issues])
        self.assertEqual(64, len(result.source_sha256 or ""))

    def test_english_template_placeholders_are_rejected(self) -> None:
        template = (ROOT / "assets" / "report-template.en.md").read_text(encoding="utf-8")
        result = lint_report_text(template, Path("template-en.md"), profile="full")
        self.assertIn("placeholder", {issue.code for issue in result.issues})

    def test_required_source_location_is_reported(self) -> None:
        sample = (ROOT / "examples" / "sample-report.en.md").read_text(encoding="utf-8")
        bad = sample.replace("[L1-L1] ", "", 1)
        result = lint_report_text(
            bad,
            Path("missing-location.md"),
            profile="full",
            source_document=self.source_document(),
            require_locators=True,
        )
        self.assertIn("citation-missing", {issue.code for issue in result.issues})

    def test_out_of_range_source_location_is_reported(self) -> None:
        sample = (ROOT / "examples" / "sample-report.en.md").read_text(encoding="utf-8")
        bad = sample.replace("[L1-L1]", "[L99-L99]", 1)
        result = lint_report_text(
            bad,
            Path("bad-range.md"),
            profile="full",
            source_document=self.source_document(),
        )
        self.assertIn("citation-range", {issue.code for issue in result.issues})

    def test_wrong_cited_text_is_reported(self) -> None:
        sample = (ROOT / "examples" / "sample-report.en.md").read_text(encoding="utf-8")
        bad = sample.replace(
            "公司去年招了三个应届生，半年内都离职了，所以现在的年轻人都吃不了苦。",
            "源文件中不存在的引文。",
            1,
        )
        result = lint_report_text(
            bad,
            Path("wrong-citation.md"),
            profile="full",
            source_document=self.source_document(),
        )
        self.assertIn("citation-text", {issue.code for issue in result.issues})


if __name__ == "__main__":
    unittest.main()
