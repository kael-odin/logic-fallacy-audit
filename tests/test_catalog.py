from __future__ import annotations

import json
import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from catalog_lib import (
    CORE_FALLACY_IDS,
    Catalog,
    Entry,
    load_catalog,
    search_entries,
    validate_catalog,
    validate_evals,
    validate_repository,
)


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = load_catalog(ROOT)

    def test_catalog_is_valid(self) -> None:
        issues = validate_catalog(self.catalog)
        self.assertEqual([], [issue.format() for issue in issues])

    def test_coverage_thresholds(self) -> None:
        self.assertGreaterEqual(len(self.catalog.entries), 260)
        self.assertGreaterEqual(len(self.catalog.fallacy_entries), 228)
        self.assertGreaterEqual(len(self.catalog.bias_entries), 30)
        self.assertEqual(10, len(self.catalog.categories))

    def test_gap_audit_entries_exist(self) -> None:
        expected = {
            "argument-to-moderation",
            "masked-man-fallacy",
            "affirmative-conclusion-from-negative-premise",
            "negative-conclusion-from-affirmative-premises",
            "exclusive-premises",
            "etymological-fallacy",
            "incomplete-comparison",
            "suppressed-correlative",
            "appeal-to-poverty",
            "appeal-to-minority",
            "appeal-to-accomplishment",
            "appeal-to-shame",
            "package-deal-fallacy",
            "historians-fallacy",
            "retrospective-determinism",
            "double-counting",
            "mind-projection-fallacy",
            "proving-too-much",
            "invincible-ignorance",
            "entitlement-to-opinion",
            "politicians-syllogism",
            "bulverism",
            "courtiers-reply",
            "ergo-decedo",
            "false-attribution",
            "overwhelming-exception",
            "ignoring-common-cause",
            "inverse-gamblers-fallacy",
            "ludic-fallacy",
            "homunculus-fallacy",
            "accident-fallacy",
            "ambiguous-middle-term",
            "exhaustive-effort-fallacy",
            "furtive-fallacy",
            "if-by-whiskey",
            "inflation-of-conflict",
            "nut-picking",
            "pooh-pooh",
            "referential-fallacy",
            "psychologists-fallacy",
        }
        self.assertEqual(set(), expected - set(self.catalog.entry_by_id))

    def test_duplicate_context_is_merged(self) -> None:
        self.assertNotIn("contextomy", self.catalog.entry_by_id)
        self.assertIn("contextomy", self.catalog.entry_by_id["quote-mining"].aliases)
        self.assertIn("语境剥离", self.catalog.entry_by_id["quote-mining"].aliases)
        quote_mining = self.catalog.entry_by_id["quote-mining"]
        self.assertEqual(3, len(quote_mining.data["diagnostic"]))
        self.assertIn("跨语境", quote_mining.data["boundary"])
        self.assertNotIn(
            "scope-of-negation",
            self.catalog.entry_by_id["masked-man-fallacy"].related,
        )

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

    def test_search_by_external_name_alias(self) -> None:
        matches = search_entries(self.catalog, "argument from fallacy", limit=5)
        self.assertEqual("fallacy-fallacy", matches[0].id)
        matches = search_entries(self.catalog, "argument-from-fallacy", limit=5)
        self.assertEqual("fallacy-fallacy", matches[0].id)

    def test_search_normalizes_fullwidth_text(self) -> None:
        matches = search_entries(self.catalog, "ＳＴＲＡＷ　ＭＡＮ", limit=3)
        self.assertEqual("straw-man", matches[0].id)

    def test_missing_id_reports_error_without_crashing(self) -> None:
        entry = Entry(
            data={
                "aliases": [],
                "category": "formal",
                "kind": "formal",
                "severity": 2,
                "definition": "这是一个用于测试缺少 ID 时校验行为的最小定义。",
                "pattern": "P；因此 Q。",
                "diagnostic": ["问题一？", "问题二？"],
                "example": "这是一个长度足够的原创测试例子。",
                "boundary": "这只是校验器测试，不用于真实分析。",
                "confusions": ["测试概念"],
                "related": [],
                "name_zh": "缺少标识",
                "name_en": "Missing Identifier",
            },
            source="test.toml",
        )
        issues = validate_catalog(Catalog(categories=self.catalog.categories, entries=[entry]))
        self.assertIn("missing-id", {issue.code for issue in issues})
        repository_issues = validate_repository(
            Catalog(categories=self.catalog.categories, entries=[entry]),
            ROOT,
        )
        self.assertIn("missing-id", {issue.code for issue in repository_issues})

    def test_invalid_field_types_report_errors_without_crashing(self) -> None:
        entry = Entry(
            data={
                "id": "invalid-field-types",
                "name_zh": 123,
                "name_en": None,
                "aliases": "not-a-list",
                "category": ["formal"],
                "kind": ["formal"],
                "severity": "high",
                "definition": "这是一个用于测试非法字段类型的最小定义。",
                "pattern": "P；因此 Q。",
                "diagnostic": [{"question": "问题一"}, {"question": "问题二"}],
                "example": "这是一个长度足够的原创测试例子。",
                "boundary": "这只是校验器测试，不用于真实分析。",
                "confusions": [["嵌套列表"]],
                "related": {"bad": "type"},
            },
            source="test.toml",
        )
        issues = validate_catalog(Catalog(categories=self.catalog.categories, entries=[entry]))
        codes = {issue.code for issue in issues}
        self.assertIn("missing-text", codes)
        self.assertIn("invalid-list", codes)
        self.assertIn("invalid-list-item", codes)
        self.assertIn("severity", codes)

    def test_duplicate_alias_is_reported(self) -> None:
        first = deepcopy(self.catalog.entry_by_id["straw-man"].data)
        second = deepcopy(self.catalog.entry_by_id["weak-man"].data)
        first.update(
            id="test-entry-a",
            name_zh="测试条目甲",
            name_en="Test Entry A",
            aliases=["共享别名"],
            category="formal",
            kind="formal",
            related=[],
        )
        second.update(
            id="test-entry-b",
            name_zh="测试条目乙",
            name_en="Test Entry B",
            aliases=["共享别名"],
            category="formal",
            kind="formal",
            related=[],
        )
        issues = validate_catalog(
            Catalog(
                categories=self.catalog.categories,
                entries=[
                    Entry(data=first, source="test.toml"),
                    Entry(data=second, source="test.toml"),
                ],
            )
        )
        self.assertIn("alias-conflict", {issue.code for issue in issues})

    def test_alias_cannot_be_another_entry_id(self) -> None:
        first = deepcopy(self.catalog.entry_by_id["straw-man"].data)
        second = deepcopy(self.catalog.entry_by_id["weak-man"].data)
        first.update(
            id="test-entry-a",
            name_zh="测试条目甲",
            name_en="Test Entry A",
            aliases=["test-entry-b"],
            category="formal",
            kind="formal",
            related=[],
        )
        second.update(
            id="test-entry-b",
            name_zh="测试条目乙",
            name_en="Test Entry B",
            aliases=[],
            category="formal",
            kind="formal",
            related=[],
        )
        issues = validate_catalog(
            Catalog(
                categories=self.catalog.categories,
                entries=[
                    Entry(data=first, source="test.toml"),
                    Entry(data=second, source="test.toml"),
                ],
            )
        )
        self.assertIn("alias-id-collision", {issue.code for issue in issues})

    def test_normalized_alias_collision_is_reported(self) -> None:
        first = deepcopy(self.catalog.entry_by_id["straw-man"].data)
        second = deepcopy(self.catalog.entry_by_id["weak-man"].data)
        first.update(
            id="test-entry-a",
            name_zh="测试条目甲",
            name_en="Test Entry A",
            aliases=["shared-alias"],
            category="formal",
            kind="formal",
            related=[],
        )
        second.update(
            id="test-entry-b",
            name_zh="测试条目乙",
            name_en="Test Entry B",
            aliases=["ＳＨＡＲＥＤ－ＡＬＩＡＳ"],
            category="formal",
            kind="formal",
            related=[],
        )
        issues = validate_catalog(
            Catalog(
                categories=self.catalog.categories,
                entries=[
                    Entry(data=first, source="test.toml"),
                    Entry(data=second, source="test.toml"),
                ],
            )
        )
        self.assertIn("alias-conflict", {issue.code for issue in issues})

    def test_invalid_eval_value_types_do_not_crash(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "evals" / "cases.jsonl"
            path.parent.mkdir(parents=True)
            path.write_text(
                json.dumps(
                    {
                        "id": "eval-invalid-types",
                        "mode": ["quick"],
                        "input": "这是一个长度足够的行为评测输入。",
                        "must_detect": [{"bad": "id"}],
                        "may_detect": [["bad"]],
                        "must_not_assert": [{"bad": "assertion"}],
                    },
                    ensure_ascii=False,
                )
                + "\n",
                encoding="utf-8",
            )
            issues = validate_evals(self.catalog, root)
        codes = {issue.code for issue in issues}
        self.assertIn("eval-mode", codes)
        self.assertIn("eval-mode-coverage", codes)
        self.assertIn("eval-list-item", codes)
        self.assertIn("eval-forbidden-items", codes)


if __name__ == "__main__":
    unittest.main()
