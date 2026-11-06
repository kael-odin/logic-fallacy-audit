from __future__ import annotations

import json
import re
import tomllib
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
CATALOG_DIR = ROOT / "catalog"

ALLOWED_KINDS = {
    "formal",
    "informal",
    "dialectical",
    "rhetorical",
    "statistical",
    "bias",
}

KIND_LABELS = {
    "formal": "形式错误",
    "informal": "非形式谬误",
    "dialectical": "辩证规则",
    "rhetorical": "修辞模式",
    "statistical": "统计推理",
    "bias": "认知偏差",
}

SEVERITY_LABELS = {
    1: "提示",
    2: "中等",
    3: "高影响",
}

ENTRY_REQUIRED_FIELDS = {
    "id",
    "name_zh",
    "name_en",
    "aliases",
    "category",
    "kind",
    "severity",
    "definition",
    "pattern",
    "diagnostic",
    "example",
    "boundary",
    "confusions",
    "related",
}

CATEGORY_REQUIRED_FIELDS = {
    "id",
    "name_zh",
    "name_en",
    "description",
    "report_hint",
}

CORE_FALLACY_IDS = [
    "straw-man",
    "slippery-slope",
    "false-dilemma",
    "appeal-to-emotion",
    "false-cause",
    "ad-hominem-abusive",
    "appeal-to-authority",
    "hasty-generalization",
    "equivocation",
    "circular-reasoning",
]

ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass(frozen=True)
class Category:
    id: str
    name_zh: str
    name_en: str
    description: str
    report_hint: str


@dataclass(frozen=True)
class Entry:
    data: dict[str, Any]
    source: str

    @property
    def id(self) -> str:
        return str(self.data["id"])

    @property
    def name_zh(self) -> str:
        return str(self.data["name_zh"])

    @property
    def name_en(self) -> str:
        return str(self.data["name_en"])

    @property
    def category(self) -> str:
        return str(self.data["category"])

    @property
    def aliases(self) -> list[str]:
        return list(self.data.get("aliases", []))

    @property
    def related(self) -> list[str]:
        return list(self.data.get("related", []))

    @property
    def severity(self) -> int:
        return int(self.data["severity"])


@dataclass(frozen=True)
class Issue:
    level: str
    code: str
    message: str
    item_id: str = ""

    def format(self) -> str:
        prefix = f"[{self.level.upper()}]"
        suffix = f" ({self.item_id})" if self.item_id else ""
        return f"{prefix} {self.code}{suffix}: {self.message}"


@dataclass(frozen=True)
class Catalog:
    categories: list[Category]
    entries: list[Entry]

    @property
    def category_by_id(self) -> dict[str, Category]:
        return {item.id: item for item in self.categories}

    @property
    def entry_by_id(self) -> dict[str, Entry]:
        return {item.id: item for item in self.entries}

    @property
    def fallacy_entries(self) -> list[Entry]:
        return [item for item in self.entries if item.category != "bias"]

    @property
    def bias_entries(self) -> list[Entry]:
        return [item for item in self.entries if item.category == "bias"]

    @property
    def counts(self) -> Counter[str]:
        return Counter(item.category for item in self.entries)


class CatalogParseError(RuntimeError):
    pass


def _load_toml(path: Path) -> dict[str, Any]:
    try:
        return tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise CatalogParseError(f"{path.name}: {exc}") from exc


def load_catalog(root: Path = ROOT) -> Catalog:
    catalog_dir = root / "catalog"
    categories_path = catalog_dir / "categories.toml"
    if not categories_path.exists():
        raise CatalogParseError(f"Missing category file: {categories_path}")

    category_data = _load_toml(categories_path).get("category", [])
    categories = [
        Category(
            id=str(item.get("id", "")),
            name_zh=str(item.get("name_zh", "")),
            name_en=str(item.get("name_en", "")),
            description=str(item.get("description", "")),
            report_hint=str(item.get("report_hint", "")),
        )
        for item in category_data
    ]

    entries: list[Entry] = []
    for path in sorted(catalog_dir.glob("*.toml")):
        if path.name == "categories.toml":
            continue
        for item in _load_toml(path).get("fallacy", []):
            entries.append(Entry(data=item, source=path.name))

    return Catalog(categories=categories, entries=entries)


def _require_text(
    entry: Entry,
    field: str,
    issues: list[Issue],
    *,
    min_chars: int = 1,
) -> str:
    value = entry.data.get(field)
    if not isinstance(value, str) or not value.strip():
        issues.append(Issue("error", "missing-text", f"字段 `{field}` 必须是非空字符串", entry.id))
        return ""
    if len(value.strip()) < min_chars:
        issues.append(
            Issue(
                "error",
                "short-text",
                f"字段 `{field}` 少于 {min_chars} 个字符",
                entry.id,
            )
        )
    return value.strip()


def _require_string_list(
    entry: Entry,
    field: str,
    issues: list[Issue],
    *,
    min_items: int,
) -> list[str]:
    value = entry.data.get(field)
    if not isinstance(value, list):
        issues.append(Issue("error", "invalid-list", f"字段 `{field}` 必须是数组", entry.id))
        return []
    if len(value) < min_items:
        issues.append(
            Issue(
                "error",
                "short-list",
                f"字段 `{field}` 至少需要 {min_items} 项",
                entry.id,
            )
        )
    cleaned: list[str] = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            issues.append(
                Issue(
                    "error",
                    "invalid-list-item",
                    f"字段 `{field}` 第 {index + 1} 项必须是非空字符串",
                    entry.id,
                )
            )
            continue
        cleaned.append(item.strip())
    return cleaned


def validate_catalog(catalog: Catalog) -> list[Issue]:
    issues: list[Issue] = []

    category_ids: set[str] = set()
    category_names: set[str] = set()
    for category in catalog.categories:
        missing = [
            field
            for field in CATEGORY_REQUIRED_FIELDS
            if not str(getattr(category, field)).strip()
        ]
        if missing:
            issues.append(
                Issue(
                    "error",
                    "category-fields",
                    f"分类缺少字段: {', '.join(sorted(missing))}",
                    category.id,
                )
            )
        if not ID_PATTERN.fullmatch(category.id):
            issues.append(
                Issue("error", "category-id", "分类 ID 必须是 kebab-case", category.id)
            )
        if category.id in category_ids:
            issues.append(Issue("error", "duplicate-category", "分类 ID 重复", category.id))
        if category.name_zh in category_names:
            issues.append(
                Issue("error", "duplicate-category-name", "分类中文名重复", category.name_zh)
            )
        category_ids.add(category.id)
        category_names.add(category.name_zh)

    entry_ids: set[str] = set()
    zh_names: set[str] = set()
    en_names: set[str] = set()
    for entry in catalog.entries:
        missing_fields = sorted(ENTRY_REQUIRED_FIELDS - set(entry.data))
        if missing_fields:
            issues.append(
                Issue(
                    "error",
                    "missing-fields",
                    f"条目缺少字段: {', '.join(missing_fields)}",
                    entry.id,
                )
            )

        if not ID_PATTERN.fullmatch(entry.id):
            issues.append(Issue("error", "invalid-id", "ID 必须是 kebab-case", entry.id))
        if entry.id in entry_ids:
            issues.append(Issue("error", "duplicate-id", "条目 ID 重复", entry.id))
        entry_ids.add(entry.id)

        zh = _require_text(entry, "name_zh", issues, min_chars=2)
        en = _require_text(entry, "name_en", issues, min_chars=2)
        if zh in zh_names:
            issues.append(Issue("error", "duplicate-zh-name", "中文名重复", entry.id))
        if en.casefold() in en_names:
            issues.append(Issue("error", "duplicate-en-name", "英文名重复", entry.id))
        zh_names.add(zh)
        en_names.add(en.casefold())

        aliases = _require_string_list(entry, "aliases", issues, min_items=0)
        if entry.id in aliases:
            issues.append(Issue("error", "self-alias", "别名不能与 ID 相同", entry.id))
        if len(aliases) != len(set(aliases)):
            issues.append(Issue("error", "duplicate-alias", "别名数组存在重复项", entry.id))

        category = str(entry.data.get("category", ""))
        if category not in category_ids:
            issues.append(
                Issue("error", "unknown-category", f"未知分类 `{category}`", entry.id)
            )

        kind = str(entry.data.get("kind", ""))
        if kind not in ALLOWED_KINDS:
            issues.append(Issue("error", "unknown-kind", f"未知 kind `{kind}`", entry.id))
        if category == "bias" and kind != "bias":
            issues.append(
                Issue("error", "bias-kind", "bias 分类的 kind 必须是 bias", entry.id)
            )
        if category != "bias" and kind == "bias":
            issues.append(
                Issue("error", "non-bias-kind", "非 bias 分类不能使用 bias kind", entry.id)
            )

        severity = entry.data.get("severity")
        if not isinstance(severity, int) or isinstance(severity, bool) or severity not in {1, 2, 3}:
            issues.append(Issue("error", "severity", "severity 必须是 1、2 或 3", entry.id))

        _require_text(entry, "definition", issues, min_chars=20)
        _require_text(entry, "pattern", issues, min_chars=8)
        _require_text(entry, "example", issues, min_chars=12)
        _require_text(entry, "boundary", issues, min_chars=15)
        _require_string_list(entry, "diagnostic", issues, min_items=2)
        _require_string_list(entry, "confusions", issues, min_items=1)
        related = _require_string_list(entry, "related", issues, min_items=0)
        if len(related) != len(set(related)):
            issues.append(Issue("error", "duplicate-related", "related 数组存在重复项", entry.id))
        if entry.id in related:
            issues.append(Issue("error", "self-related", "related 不能引用自身", entry.id))

    for entry in catalog.entries:
        for related_id in entry.related:
            if related_id not in entry_ids:
                issues.append(
                    Issue(
                        "error",
                        "missing-related",
                        f"related 指向不存在的条目 `{related_id}`",
                        entry.id,
                    )
                )

    for core_id in CORE_FALLACY_IDS:
        if core_id not in entry_ids:
            issues.append(
                Issue("error", "missing-core", f"核心十类缺少条目 `{core_id}`", core_id)
            )

    if len(catalog.fallacy_entries) < 180:
        issues.append(
            Issue(
                "error",
                "coverage",
                f"谬误/论证模式少于 180 条，当前 {len(catalog.fallacy_entries)} 条",
            )
        )
    if len(catalog.bias_entries) < 30:
        issues.append(
            Issue(
                "error",
                "bias-coverage",
                f"认知偏差少于 30 条，当前 {len(catalog.bias_entries)} 条",
            )
        )

    return issues


def _severity_label(entry: Entry) -> str:
    if entry.category == "bias":
        return "背景偏差"
    return SEVERITY_LABELS[entry.severity]


def _kind_label(entry: Entry) -> str:
    return KIND_LABELS[str(entry.data["kind"])]


def _md_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def _alias_text(entry: Entry) -> str:
    return "、".join(entry.aliases) if entry.aliases else "无"


def _related_text(entry: Entry, entry_by_id: dict[str, Entry]) -> str:
    if not entry.related:
        return "无"
    return "、".join(
        f"{entry_by_id[item].name_zh} (`{item}`)" for item in entry.related
    )


def _category_filename(category_id: str) -> str:
    order = {
        "formal": "01",
        "relevance": "02",
        "presumption": "03",
        "ambiguity": "04",
        "causal": "05",
        "statistical": "06",
        "explanation": "07",
        "normative": "08",
        "rhetorical": "09",
        "bias": "10",
    }
    return f"{order[category_id]}-{category_id}.md"


def build_catalog_index(catalog: Catalog) -> str:
    counts = catalog.counts
    entry_by_id = catalog.entry_by_id
    lines = [
        "# 分类目录索引",
        "",
        "> 本文件由 `python scripts/fallacy_cli.py render` 生成。请修改 `catalog/` 后重新生成。",
        "",
        f"当前共 **{len(catalog.fallacy_entries)}** 条谬误/论证模式和 **{len(catalog.bias_entries)}** 条相邻认知偏差。",
        "",
        "## 核心十类",
        "",
        "| 中文名 | English | ID | 默认影响 |",
        "|---|---|---|---|",
    ]
    for core_id in CORE_FALLACY_IDS:
        item = entry_by_id[core_id]
        lines.append(
            f"| {_md_escape(item.name_zh)} | {_md_escape(item.name_en)} | `{item.id}` | {_severity_label(item)} |"
        )

    lines.extend(
        [
            "",
            "## 完整分类",
            "",
            "| 分类 | English | 条目数 | 目录 |",
            "|---|---|---:|---|",
        ]
    )
    for category in catalog.categories:
        filename = _category_filename(category.id)
        lines.append(
            f"| {_md_escape(category.name_zh)} | {_md_escape(category.name_en)} | {counts[category.id]} | [{filename}](catalog/{filename}) |"
        )

    lines.extend(
        [
            "",
            "## 使用顺序",
            "",
            "1. 先读 [`analysis-protocol.md`](analysis-protocol.md)。",
            "2. 再读 [`taxonomy.md`](taxonomy.md)，确定论证任务和主分类。",
            "3. 只打开当前场景相关的分类文件。",
            "4. 最后读 [`false-positive-guards.md`](false-positive-guards.md) 复核误报。",
            "",
        ]
    )
    return "\n".join(lines)


def build_category_doc(catalog: Catalog, category_id: str) -> str:
    category = catalog.category_by_id[category_id]
    items = [item for item in catalog.entries if item.category == category_id]
    entry_by_id = catalog.entry_by_id

    lines = [
        f"# {category.name_zh}",
        "",
        f"**{category.name_en}**",
        "",
        category.description,
        "",
        f"> 使用提示：{category.report_hint}",
        "",
        "> 本文件由结构化目录生成。修改 `catalog/` 后再运行 `python scripts/fallacy_cli.py render`。",
        "",
        f"共 **{len(items)}** 条。",
        "",
        "## 快速索引",
        "",
        "| 中文名 | English | ID |",
        "|---|---|---|",
    ]
    for item in items:
        lines.append(
            f"| {_md_escape(item.name_zh)} | {_md_escape(item.name_en)} | `{item.id}` |"
        )

    for item in items:
        diagnostic = "\n".join(
            f"{index + 1}. {_md_escape(str(question))}"
            for index, question in enumerate(item.data["diagnostic"])
        )
        lines.extend(
            [
                "",
                "---",
                "",
                f"## {item.name_zh}",
                "",
                f"**{item.name_en}** · `{item.id}`",
                "",
                f"- 类型：{_kind_label(item)}",
                f"- 默认影响：{_severity_label(item)}",
                f"- 别名：{_md_escape(_alias_text(item))}",
                "",
                "### 定义",
                "",
                str(item.data["definition"]),
                "",
                "### 推理式",
                "",
                f"```text\n{item.data['pattern']}\n```",
                "",
                "### 诊断问题",
                "",
                diagnostic,
                "",
                "### 原创例子",
                "",
                f"> {item.data['example']}",
                "",
                "### 何时可能不是谬误",
                "",
                str(item.data["boundary"]),
                "",
                "### 容易混淆",
                "",
                "、".join(str(value) for value in item.data["confusions"]),
                "",
                "### 相关条目",
                "",
                _related_text(item, entry_by_id),
                "",
            ]
        )

    lines.extend(["", "[返回分类索引](../catalog-index.md)", ""])
    return "\n".join(lines)


def build_adjacent_biases_doc(catalog: Catalog) -> str:
    category = catalog.category_by_id["bias"]
    items = catalog.bias_entries
    entry_by_id = catalog.entry_by_id
    lines = [
        "# 与谬误相邻的认知偏差",
        "",
        f"**{category.name_en}**",
        "",
        category.description,
        "",
        "> 认知偏差是判断倾向，不是逻辑谬误。报告只有在能指出具体推理步骤受影响时，才可把偏差作为解释背景。",
        "",
        f"当前收录 **{len(items)}** 条。完整机器可读数据位于 `catalog/10-adjacent-biases.toml`。",
        "",
        "## 偏差速查",
        "",
        "| 中文名 | English | ID |",
        "|---|---|---|",
    ]
    for item in items:
        lines.append(
            f"| {_md_escape(item.name_zh)} | {_md_escape(item.name_en)} | `{item.id}` |"
        )

    for item in items:
        diagnostic = "\n".join(
            f"{index + 1}. {_md_escape(str(question))}"
            for index, question in enumerate(item.data["diagnostic"])
        )
        lines.extend(
            [
                "",
                "---",
                "",
                f"## {item.name_zh}",
                "",
                f"**{item.name_en}** · `{item.id}`",
                "",
                f"- 别名：{_md_escape(_alias_text(item))}",
                "",
                "### 定义",
                "",
                str(item.data["definition"]),
                "",
                "### 模式",
                "",
                f"```text\n{item.data['pattern']}\n```",
                "",
                "### 诊断问题",
                "",
                diagnostic,
                "",
                "### 例子",
                "",
                f"> {item.data['example']}",
                "",
                "### 与谬误的边界",
                "",
                str(item.data["boundary"]),
                "",
                "### 相关条目",
                "",
                _related_text(item, entry_by_id),
                "",
            ]
        )
    lines.extend(["", "[返回分类索引](catalog-index.md)", ""])
    return "\n".join(lines)


def expected_generated_files(catalog: Catalog) -> dict[Path, str]:
    outputs: dict[Path, str] = {
        ROOT / "references" / "catalog-index.md": build_catalog_index(catalog),
        ROOT / "references" / "adjacent-biases.md": build_adjacent_biases_doc(catalog),
    }
    for category in catalog.categories:
        path = ROOT / "references" / "catalog" / _category_filename(category.id)
        outputs[path] = build_category_doc(catalog, category.id)
    return outputs


def write_generated_files(catalog: Catalog) -> list[Path]:
    written: list[Path] = []
    for path, content in expected_generated_files(catalog).items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        written.append(path)
    return written


def generated_drift(catalog: Catalog) -> list[Path]:
    drift: list[Path] = []
    for path, content in expected_generated_files(catalog).items():
        if not path.exists():
            drift.append(path)
            continue
        current = path.read_text(encoding="utf-8")
        if current != content:
            drift.append(path)
    return drift


def _strip_fenced_blocks(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def validate_markdown_links(root: Path = ROOT) -> list[Issue]:
    issues: list[Issue] = []
    link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = _strip_fenced_blocks(path.read_text(encoding="utf-8"))
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().strip("<>")
            if (
                not target
                or target.startswith("#")
                or target.startswith("http://")
                or target.startswith("https://")
                or target.startswith("mailto:")
                or target.startswith("codex://")
            ):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                issues.append(
                    Issue(
                        "error",
                        "external-relative-link",
                        f"相对链接跳出仓库: {raw_target}",
                        str(path.relative_to(root)),
                    )
                )
                continue
            if not resolved.exists():
                issues.append(
                    Issue(
                        "error",
                        "missing-link",
                        f"链接目标不存在: {raw_target}",
                        str(path.relative_to(root)),
                    )
                )
    return issues


def validate_skill(root: Path = ROOT) -> list[Issue]:
    path = root / "SKILL.md"
    if not path.exists():
        return [Issue("error", "missing-skill", "缺少 SKILL.md")]
    text = path.read_text(encoding="utf-8")
    issues: list[Issue] = []
    if not text.startswith("---\n"):
        issues.append(Issue("error", "frontmatter", "SKILL.md 必须以 YAML frontmatter 开始"))
        return issues
    parts = text.split("---", 2)
    if len(parts) < 3:
        issues.append(Issue("error", "frontmatter", "SKILL.md frontmatter 未闭合"))
        return issues
    frontmatter = parts[1]
    if "name: logic-fallacy-audit" not in frontmatter:
        issues.append(Issue("error", "skill-name", "Skill name 必须为 logic-fallacy-audit"))
    if "description:" not in frontmatter:
        issues.append(Issue("error", "skill-description", "SKILL.md 缺少 description"))
    required_refs = [
        "references/analysis-protocol.md",
        "references/report-spec.md",
        "references/false-positive-guards.md",
        "references/taxonomy.md",
        "references/chinese-patterns.md",
    ]
    for ref in required_refs:
        if ref not in text:
            issues.append(Issue("error", "skill-reference", f"SKILL.md 未引用 {ref}"))
    return issues


def validate_report_template(root: Path = ROOT) -> list[Issue]:
    path = root / "assets" / "report-template.md"
    if not path.exists():
        return [Issue("error", "missing-template", "缺少 assets/report-template.md")]
    text = path.read_text(encoding="utf-8")
    required = [
        "## 结论摘要",
        "## 论证地图",
        "## 关键问题",
        "## 反向检验",
        "## 改写建议",
        "## 边界说明",
    ]
    return [
        Issue("error", "template-section", f"报告模板缺少章节 `{section}`")
        for section in required
        if section not in text
    ]


def validate_evals(catalog: Catalog, root: Path = ROOT) -> list[Issue]:
    path = root / "evals" / "cases.jsonl"
    if not path.exists():
        return [Issue("error", "missing-evals", "缺少 evals/cases.jsonl")]
    issues: list[Issue] = []
    seen: set[str] = set()
    entry_ids = set(catalog.entry_by_id)
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            issues.append(
                Issue("error", "eval-json", f"第 {line_number} 行 JSON 无效: {exc}")
            )
            continue
        for field in ["id", "mode", "input", "must_detect", "may_detect", "must_not_assert"]:
            if field not in item:
                issues.append(
                    Issue("error", "eval-field", f"第 {line_number} 行缺少 `{field}`")
                )
        case_id = str(item.get("id", ""))
        if case_id in seen:
            issues.append(Issue("error", "eval-duplicate", "评测 ID 重复", case_id))
        seen.add(case_id)
        if item.get("mode") not in {"quick", "full", "debate", "teaching"}:
            issues.append(Issue("error", "eval-mode", "评测 mode 无效", case_id))
        if not isinstance(item.get("input"), str) or len(item.get("input", "").strip()) < 10:
            issues.append(Issue("error", "eval-input", "评测 input 至少 10 个字符", case_id))
        for field in ["must_detect", "may_detect"]:
            values = item.get(field)
            if not isinstance(values, list):
                issues.append(Issue("error", "eval-list", f"`{field}` 必须是数组", case_id))
                continue
            for value in values:
                if value not in entry_ids:
                    issues.append(
                        Issue("error", "eval-entry", f"`{field}` 指向未知条目 `{value}`", case_id)
                    )
        must_not = item.get("must_not_assert")
        if not isinstance(must_not, list) or not must_not:
            issues.append(
                Issue("error", "eval-forbidden", "must_not_assert 必须是非空数组", case_id)
            )
    if len(seen) < 10:
        issues.append(Issue("error", "eval-coverage", "评测案例少于 10 条"))
    return issues


def validate_repository(catalog: Catalog, root: Path = ROOT) -> list[Issue]:
    issues = validate_catalog(catalog)
    issues.extend(validate_skill(root))
    issues.extend(validate_report_template(root))
    issues.extend(validate_evals(catalog, root))
    issues.extend(validate_markdown_links(root))

    required_files = [
        "README.md",
        "README.en.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "agents/openai.yaml",
        ".github/workflows/validate.yml",
        "references/catalog-index.md",
        "references/core-fallacies.md",
        "references/logic-basics.md",
        "references/task-matrix.md",
        "assets/report-template.md",
        "assets/checklist.md",
        "examples/sample-report.md",
        "examples/modes.md",
        "docs/product-spec.md",
        "docs/architecture.md",
        "docs/quality.md",
        "docs/roadmap.md",
    ]
    for relative in required_files:
        if not (root / relative).exists():
            issues.append(
                Issue("error", "required-file", f"缺少必需文件 `{relative}`")
            )
    return issues


def search_entries(catalog: Catalog, query: str, limit: int = 10) -> list[Entry]:
    needle = query.strip().casefold()
    if not needle:
        return []
    scored: list[tuple[int, int, Entry]] = []
    for item in catalog.entries:
        haystacks = [item.id, item.name_zh, item.name_en, *item.aliases]
        folded = [value.casefold() for value in haystacks]
        score = 0
        if needle in folded:
            score = 100
        elif any(value.startswith(needle) for value in folded):
            score = 90
        elif any(needle in value for value in folded):
            score = 80
        else:
            body = " ".join(
                str(item.data[field])
                for field in ["definition", "pattern", "example", "boundary"]
            ).casefold()
            if needle in body:
                score = 30
            else:
                diagnostics = " ".join(item.data["diagnostic"]).casefold()
                if needle in diagnostics:
                    score = 20
        if score:
            scored.append((score, -item.severity, item))
    scored.sort(key=lambda value: (value[0], value[1], value[2].name_zh), reverse=True)
    return [entry for _, _, entry in scored[:limit]]


def format_catalog_stats(catalog: Catalog) -> str:
    counts = catalog.counts
    lines = [
        f"条目总数：{len(catalog.entries)}",
        f"谬误/论证模式：{len(catalog.fallacy_entries)}",
        f"相邻认知偏差：{len(catalog.bias_entries)}",
        f"分类数：{len(catalog.categories)}",
        "",
        "分类分布：",
    ]
    for category in catalog.categories:
        lines.append(f"- {category.name_zh} (`{category.id}`): {counts[category.id]}")
    return "\n".join(lines)


def format_entry(item: Entry, catalog: Catalog) -> str:
    lines = [
        f"{item.name_zh} / {item.name_en}",
        f"ID: {item.id}",
        f"分类: {catalog.category_by_id[item.category].name_zh}",
        f"类型: {KIND_LABELS[str(item.data['kind'])]}",
        f"默认影响: {_severity_label(item)}",
        f"别名: {_alias_text(item)}",
        "",
        "定义:",
        str(item.data["definition"]),
        "",
        "推理式:",
        str(item.data["pattern"]),
        "",
        "诊断问题:",
        *[f"- {question}" for question in item.data["diagnostic"]],
        "",
        "例子:",
        str(item.data["example"]),
        "",
        "边界:",
        str(item.data["boundary"]),
        "",
        "易混淆:",
        "、".join(str(value) for value in item.data["confusions"]),
        "",
        "相关条目:",
        _related_text(item, catalog.entry_by_id),
    ]
    return "\n".join(lines)


def iter_entry_summaries(entries: Iterable[Entry]) -> Iterable[str]:
    for item in entries:
        yield f"{item.name_zh}\t{item.name_en}\t{item.id}"
