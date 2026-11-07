from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from source_map import (
    build_source_document,
    locate_quote,
    normalize_source,
)


class SourceMapTests(unittest.TestCase):
    def test_normalizes_bom_and_line_endings(self) -> None:
        self.assertEqual("A\nB\nC", normalize_source("\ufeffA\r\nB\rC"))

    def test_builds_paragraph_blocks_and_line_spans(self) -> None:
        document = build_source_document("A\n\nB\nC\n\nD\n")
        self.assertEqual(6, document.line_count)
        self.assertEqual(3, document.block_count)
        self.assertEqual(
            [(1, 1), (3, 4), (6, 6)],
            [(block.line_start, block.line_end) for block in document.blocks],
        )
        self.assertEqual(64, len(document.sha256))

    def test_splits_long_blocks_at_sentence_boundaries(self) -> None:
        document = build_source_document("第一句。第二句。第三句。", max_chars=6)
        self.assertEqual(3, document.block_count)
        self.assertTrue(all(len(block.text) <= 6 for block in document.blocks))

    def test_locates_multiline_quote(self) -> None:
        document = build_source_document("A\n\nB\nC\n\nD\n")
        matches = locate_quote(document, "B\nC")
        self.assertEqual(1, len(matches))
        self.assertEqual(3, matches[0].line_start)
        self.assertEqual(4, matches[0].line_end)
        self.assertEqual("B\nC", matches[0].quote)

    def test_locate_returns_all_exact_occurrences(self) -> None:
        document = build_source_document("重复片段\n\n重复片段\n")
        matches = locate_quote(document, "重复片段")
        self.assertEqual(2, len(matches))
        self.assertEqual([1, 3], [match.line_start for match in matches])

    def test_locate_includes_overlapping_occurrences(self) -> None:
        document = build_source_document("aaaa")
        matches = locate_quote(document, "aa")
        self.assertEqual([0, 1, 2], [match.char_start for match in matches])


if __name__ == "__main__":
    unittest.main()
