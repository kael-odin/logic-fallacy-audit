from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from report_diagram import (
    parse_report_diagram,
    render_argument_mermaid,
    render_compare_mermaid,
    render_issues_mermaid,
)


class ReportDiagramTests(unittest.TestCase):
    def sample_text(self, name: str = "sample-report.md") -> str:
        return (ROOT / "examples" / name).read_text(encoding="utf-8")

    def test_parses_argument_and_issue_nodes(self) -> None:
        diagram = parse_report_diagram(self.sample_text())
        self.assertEqual("C1", diagram.conclusions[0].id)
        self.assertEqual(3, len(diagram.premises))
        self.assertEqual(4, len(diagram.assumptions))
        self.assertEqual(4, len(diagram.issues))
        self.assertTrue(diagram.rewrite)

    def test_renders_argument_mermaid(self) -> None:
        text = render_argument_mermaid(parse_report_diagram(self.sample_text()))
        self.assertIn("```mermaid", text)
        self.assertIn("flowchart TD", text)
        self.assertIn("P1 --> C1", text)
        self.assertIn("A1 -.assumption.-> C1", text)

    def test_renders_issue_mermaid(self) -> None:
        text = render_issues_mermaid(parse_report_diagram(self.sample_text()))
        self.assertIn("I1", text)
        self.assertIn("I1 -.affects.-> C1", text)
        self.assertIn("class I1,I2,I3,I4 issue;", text)

    def test_renders_compare_mermaid(self) -> None:
        text = render_compare_mermaid(parse_report_diagram(self.sample_text()))
        self.assertIn("subgraph BEFORE[Before / 修复前]", text)
        self.assertIn("subgraph AFTER[After / 修复后]", text)
        self.assertIn("I1 -.repair.-> R1", text)

    def test_parses_english_report(self) -> None:
        diagram = parse_report_diagram(self.sample_text("sample-report.en.md"))
        self.assertEqual("C1", diagram.conclusions[0].id)
        self.assertEqual(2, len(diagram.issues))

    def test_missing_argument_map_raises(self) -> None:
        with self.assertRaises(ValueError):
            parse_report_diagram("# Empty\n\nNo argument map.")


if __name__ == "__main__":
    unittest.main()
