from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUBRIC_DIR = ROOT / "evals" / "rubrics"


class SpecializedRubricTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        lines = (ROOT / "evals" / "cases.jsonl").read_text(encoding="utf-8").splitlines()
        cls.case_ids = {json.loads(line)["id"] for line in lines if line.strip()}

    def test_rubric_files_exist(self) -> None:
        expected = {
            "README.md",
            "policy.md",
            "statistics.md",
            "long-dialogue.md",
            "explainer.md",
        }
        self.assertEqual(expected, {path.name for path in RUBRIC_DIR.glob("*.md")})

    def test_rubrics_have_six_dimensions(self) -> None:
        for name in ("policy.md", "statistics.md", "long-dialogue.md", "explainer.md"):
            with self.subTest(name=name):
                text = (RUBRIC_DIR / name).read_text(encoding="utf-8")
                dimensions = [
                    line
                    for line in text.splitlines()
                    if line.startswith("|")
                    and line.endswith("|")
                    and "| 维度" not in line
                    and "---" not in line
                ]
                self.assertEqual(6, len(dimensions))

    def test_rubric_case_references_exist(self) -> None:
        text = "\n".join(path.read_text(encoding="utf-8") for path in RUBRIC_DIR.glob("*.md"))
        referenced = set(re.findall(r"`(eval-\d{3}-[a-z0-9-]+)`", text))
        self.assertTrue(referenced)
        self.assertEqual(set(), referenced - self.case_ids)


if __name__ == "__main__":
    unittest.main()
