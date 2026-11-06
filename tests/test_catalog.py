from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from catalog_lib import (  # noqa: E402
    CORE_FALLACY_IDS,
    load_catalog,
    search_entries,
    validate_catalog,
)


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = load_catalog(ROOT)

    def test_catalog_is_valid(self) -> None:
        issues = validate_catalog(self.catalog)
        self.assertEqual([], [issue.format() for issue in issues])

    def test_coverage_thresholds(self) -> None:
        self.assertGreaterEqual(len(self.catalog.fallacy_entries), 180)
        self.assertGreaterEqual(len(self.catalog.bias_entries), 30)
        self.assertEqual(10, len(self.catalog.categories))

    def test_core_ten_exist(self) -> None:
        ids = set(self.catalog.entry_by_id)
        self.assertEqual([], [item for item in CORE_FALLACY_IDS if item not in ids])

    def test_core_ten_aliases_and_names(self) -> None:
        expected = {
            "straw-man": "稻草人谬误",
            "slippery-slope": "滑坡谬误",
            "false-dilemma": "虚假两难",
            "appeal-to-emotion": "诉诸情感",
            "false-cause": "虚假因果",
            "ad-hominem-abusive": "人身攻击",
            "appeal-to-authority": "诉诸权威",
            "hasty-generalization": "草率概括",
            "equivocation": "偷换概念",
            "circular-reasoning": "循环论证",
        }
        for entry_id, name_zh in expected.items():
            self.assertEqual(name_zh, self.catalog.entry_by_id[entry_id].name_zh)
        self.assertIn("错误归因", self.catalog.entry_by_id["false-cause"].aliases)
        self.assertIn("以偏概全", self.catalog.entry_by_id["hasty-generalization"].aliases)

    def test_search_by_alias(self) -> None:
        matches = search_entries(self.catalog, "稻草人", limit=3)
        self.assertIn("straw-man", [item.id for item in matches])

    def test_search_by_mechanism(self) -> None:
        matches = search_entries(self.catalog, "第三变量", limit=20)
        self.assertIn("cum-hoc", [item.id for item in matches])


if __name__ == "__main__":
    unittest.main()
