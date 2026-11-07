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


if __name__ == "__main__":
    unittest.main()
