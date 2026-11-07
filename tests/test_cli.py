from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "fallacy_cli.py"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CLI), *args],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        capture_output=True,
        check=False,
    )


class CliTests(unittest.TestCase):
    def test_stats_json(self) -> None:
        result = run_cli("stats", "--json")
        self.assertEqual(0, result.returncode, result.stderr)
        payload = json.loads(result.stdout)
        self.assertGreaterEqual(payload["total"], 230)
        self.assertGreaterEqual(payload["fallacies"], 200)
        self.assertGreaterEqual(payload["biases"], 30)

    def test_search_returns_specific_entry(self) -> None:
        result = run_cli("search", "偷换概念")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("equivocation", result.stdout)

    def test_show_known_entry(self) -> None:
        result = run_cli("show", "false-cause")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("错误归因", result.stdout)
        self.assertIn("诊断问题", result.stdout)

    def test_show_unknown_entry_fails(self) -> None:
        result = run_cli("show", "definitely-not-a-real-id")
        self.assertEqual(1, result.returncode)

    def test_render_check_is_clean(self) -> None:
        result = run_cli("render", "--check")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("一致", result.stdout)

    def test_lint_report_accepts_sample(self) -> None:
        result = run_cli(
            "lint-report",
            "examples/sample-report.md",
            "--profile",
            "full",
            "--strict",
        )
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("0 errors", result.stdout)

    def test_lint_english_report_with_source(self) -> None:
        result = run_cli(
            "lint-report",
            "examples/sample-report.en.md",
            "--profile",
            "full",
            "--source",
            "examples/long-text-source.txt",
            "--require-locators",
            "--strict",
        )
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("0 errors", result.stdout)

    def test_lint_mismatched_source_fails(self) -> None:
        result = run_cli(
            "lint-report",
            "examples/sample-report.en.md",
            "--profile",
            "full",
            "--source",
            "README.en.md",
            "--require-locators",
            "--strict",
        )
        self.assertEqual(1, result.returncode)
        self.assertIn("citation-text", result.stdout)

    def test_segment_example_returns_source_map(self) -> None:
        result = run_cli("segment", "examples/long-text-source.txt", "--json")
        self.assertEqual(0, result.returncode, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(64, len(payload["sha256"]))
        self.assertGreaterEqual(payload["block_count"], 3)
        self.assertEqual("U1", payload["blocks"][0]["id"])

    def test_locate_example_quote_returns_line_numbers(self) -> None:
        result = run_cli(
            "locate",
            "examples/long-text-source.txt",
            "--quote",
            "三个人的经历",
            "--json",
        )
        self.assertEqual(0, result.returncode, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(1, len(payload["matches"]))
        self.assertGreaterEqual(payload["matches"][0]["line_start"], 1)

    def test_locate_missing_quote_fails(self) -> None:
        result = run_cli(
            "locate",
            "examples/long-text-source.txt",
            "--quote",
            "这段文字不存在",
        )
        self.assertEqual(1, result.returncode)
        self.assertIn("未找到", result.stdout)

    def test_diagram_argument_returns_mermaid(self) -> None:
        result = run_cli("diagram", "examples/sample-report.md", "--kind", "argument")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("```mermaid", result.stdout)
        self.assertIn("P1 --> C1", result.stdout)

    def test_diagram_compare_json(self) -> None:
        result = run_cli(
            "diagram",
            "examples/sample-report.en.md",
            "--kind",
            "compare",
            "--json",
        )
        self.assertEqual(0, result.returncode, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual("compare", payload["kind"])
        self.assertEqual(2, len(payload["diagram"]["issues"]))
        self.assertIn("subgraph AFTER", payload["mermaid"])

    def test_regression_dashboard_check(self) -> None:
        result = run_cli("regression-dashboard", "--check")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("一致", result.stdout)


if __name__ == "__main__":
    unittest.main()
