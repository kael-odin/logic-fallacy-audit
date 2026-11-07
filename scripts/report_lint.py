from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from source_map import SourceDocument, build_source_document, read_source

REQUIRED_SECTIONS = [
    "结论摘要",
    "论证地图",
    "关键问题",
    "反向检验",
    "改写建议",
    "边界说明",
]

SECTION_ALIASES = {
    "结论摘要": ("结论摘要", "Conclusion Summary"),
    "论证地图": ("论证地图", "Argument Map"),
    "关键问题": ("关键问题", "Key Issues"),
    "反向检验": ("反向检验", "Reverse Test"),
    "改写建议": ("改写建议", "Rewrite"),
    "边界说明": ("边界说明", "Boundaries"),
}

ARGUMENT_MAP_FIELDS = [
    "最终结论",
    "显式前提",
    "必要隐含前提",
    "隐含前提的重建依据",
    "推理类型",
    "当前缺失环节",
]

ARGUMENT_MAP_ALIASES = {
    "最终结论": ("最终结论", "Final Conclusion"),
    "显式前提": ("显式前提", "Explicit Premises"),
    "必要隐含前提": ("必要隐含前提", "Necessary Implicit Premises"),
    "隐含前提的重建依据": ("隐含前提的重建依据", "Reconstruction Basis"),
    "推理类型": ("推理类型", "Reasoning Type"),
    "当前缺失环节": ("当前缺失环节", "Current Gap"),
}

ISSUE_FIELDS = [
    "原文",
    "判定",
    "机制",
    "为什么结论还不能成立",
    "影响",
    "边界",
    "相关但不主判",
    "修复条件",
]

ISSUE_FIELD_ALIASES = {
    "原文": ("原文", "Original Text"),
    "判定": ("判定", "Verdict"),
    "机制": ("机制", "Mechanism"),
    "为什么结论还不能成立": (
        "为什么结论还不能成立",
        "Why the Conclusion Does Not Yet Follow",
    ),
    "影响": ("影响", "Impact"),
    "边界": ("边界", "Boundary"),
    "相关但不主判": ("相关但不主判", "Related but Not Primary"),
    "修复条件": ("修复条件", "Repair Conditions"),
}

REVERSE_TEST_FIELDS = [
    "最强版本",
    "反例或关键测试",
    "替代解释",
    "可能误判",
]

REVERSE_TEST_ALIASES = {
    "最强版本": ("最强版本", "Strongest Version"),
    "反例或关键测试": ("反例或关键测试", "Counterexample or Key Test"),
    "替代解释": ("替代解释", "Alternative Explanation"),
    "可能误判": ("可能误判", "Possible Misjudgment"),
}

FIELD_ALIASES = {
    **ARGUMENT_MAP_ALIASES,
    **ISSUE_FIELD_ALIASES,
    **REVERSE_TEST_ALIASES,
}

FINDING_LABELS = (
    "确认",
    "较可能",
    "语境相关",
    "不构成谬误",
    "Confirmed",
    "Likely",
    "Context-dependent",
    "Not a Fallacy",
)
IMPACT_LABELS = (
    "阻断",
    "重大",
    "局部",
    "表达",
    "无",
    "Blocking",
    "Major",
    "Local",
    "Expression",
    "None",
)
CONFIDENCE_PATTERN = re.compile(
    r"(?:置信度|confidence)\s*[:：]\s*(?:高|中|低|high|medium|low)",
    re.IGNORECASE,
)
LOCATION_PATTERN = re.compile(r"\[L(\d+)(?:\s*-\s*L?(\d+))?\]")
HEADING_PATTERN = re.compile(r"^(#{2,3})\s+(.+?)\s*$")
FIELD_HEADER_PATTERN = re.compile(
    r"(?m)^(?P<indent>\s*)\*\*(?P<name>[^*\n]+)\*\*(?P<inline>[^\n]*)$"
)
PLACEHOLDER_MARKERS = (
    "[问题标题]",
    "[必要片段]",
    "[中性重述最终主张]",
    "[说明上下文缺口]",
    "[按相同结构重复。]",
    "[使结论成立所需但未明说的前提]",
    "[2–4 句",
    "[Issue title]",
    "[necessary excerpt]",
    "[neutral restatement of the final claim]",
    "[required excerpt]",
    "[explain the context gap]",
    "[repeat the same structure]",
)
FULL_PROFILES = {"full", "debate", "explainer"}


@dataclass(frozen=True)
class ReportIssue:
    level: str
    code: str
    message: str
    line: int

    def format(self) -> str:
        return f"[{self.level.upper()}] L{self.line} {self.code}: {self.message}"


@dataclass(frozen=True)
class ReportLintResult:
    path: Path
    profile: str
    issues: list[ReportIssue]
    source_sha256: str | None = None

    @property
    def errors(self) -> list[ReportIssue]:
        return [issue for issue in self.issues if issue.level == "error"]

    @property
    def warnings(self) -> list[ReportIssue]:
        return [issue for issue in self.issues if issue.level == "warning"]


def _section_map(lines: list[str]) -> dict[str, tuple[int, int]]:
    headings: list[tuple[int, str, int]] = []
    for index, line in enumerate(lines):
        match = HEADING_PATTERN.match(line)
        if not match:
            continue
        level, title = match.groups()
        if level == "##":
            headings.append((index, title.strip(), 2))
    sections: dict[str, tuple[int, int]] = {}
    for position, (start, title, _level) in enumerate(headings):
        end = headings[position + 1][0] if position + 1 < len(headings) else len(lines)
        sections[title] = (start, end)
    return sections


def _section_lines(
    lines: list[str],
    sections: dict[str, tuple[int, int]],
    title: str,
) -> tuple[int, list[str]]:
    for alias in SECTION_ALIASES.get(title, (title,)):
        bounds = sections.get(alias)
        if bounds is not None:
            start, end = bounds
            return start + 1, lines[start + 1 : end]
    return 0, []


def _duplicate_sections(lines: list[str]) -> list[tuple[int, str]]:
    seen: set[str] = set()
    duplicates: list[tuple[int, str]] = []
    for index, line in enumerate(lines, start=1):
        match = HEADING_PATTERN.match(line)
        if not match:
            continue
        level, title = match.groups()
        title = title.strip()
        if level != "##":
            continue
        canonical = next(
            (section for section, aliases in SECTION_ALIASES.items() if title in aliases),
            None,
        )
        if canonical is None:
            continue
        if canonical in seen:
            duplicates.append((index, canonical))
        seen.add(canonical)
    return duplicates


def _field_values(text: str) -> dict[str, str]:
    matches = list(FIELD_HEADER_PATTERN.finditer(text))
    values: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        inline = match.group("inline").strip().lstrip(":：").strip()
        following = text[match.end() : end].strip()
        value = "\n".join(part for part in (inline, following) if part)
        values[match.group("name").strip()] = value
    return values


def _field_value(fields: dict[str, str], name: str, *, prefix: bool = False) -> str | None:
    for alias in FIELD_ALIASES.get(name, (name,)):
        if alias in fields:
            return fields[alias]
        if prefix:
            for field_name, value in fields.items():
                if field_name.startswith(alias):
                    return value
    return None


def _meaningful_field(value: str | None) -> bool:
    if value is None:
        return False
    cleaned = re.sub(r"(?m)^\s*>\s?", "", value)
    cleaned = cleaned.strip(" \t\r\n`*_>“”\"'")
    return bool(cleaned)


def _citation_fragment(value: str) -> str:
    cleaned = LOCATION_PATTERN.sub("", value)
    cleaned = re.sub(r"(?m)^\s*>\s?", "", cleaned).strip()
    quoted = re.search(r"[“\"](.*?)[”\"]", cleaned, re.DOTALL)
    if quoted:
        return quoted.group(1).strip()
    return cleaned.strip(" \t\r\n`*_>“”\"'。.!?")


def _validate_citations(
    value: str,
    *,
    source_document: SourceDocument | None,
    require_locators: bool,
    card_label: str,
    report_line: int,
    issues: list[ReportIssue],
) -> None:
    matches = list(LOCATION_PATTERN.finditer(value))
    if not matches:
        if require_locators:
            issues.append(
                ReportIssue(
                    "error",
                    "citation-missing",
                    f"{card_label} 缺少 `[Lx-Ly]` 原文位置",
                    report_line,
                )
            )
        return

    for match in matches:
        start = int(match.group(1))
        end = int(match.group(2) or start)
        if start < 1 or end < start:
            issues.append(
                ReportIssue(
                    "error",
                    "citation-format",
                    f"{card_label} 包含无效位置 `{match.group(0)}`",
                    report_line,
                )
            )
            continue
        if source_document is None:
            continue
        if end > source_document.line_count:
            issues.append(
                ReportIssue(
                    "error",
                    "citation-range",
                    f"{card_label} 的 `{match.group(0)}` 超出源文本行数",
                    report_line,
                )
            )
            continue
        if len(matches) == 1:
            fragment = _citation_fragment(value)
            if "…" in fragment or "..." in fragment or len(fragment) < 4:
                continue
            source_range = "\n".join(line.text for line in source_document.lines[start - 1 : end])
            if fragment not in source_range:
                issues.append(
                    ReportIssue(
                        "error",
                        "citation-text",
                        f"{card_label} 的引用文本不在 `{match.group(0)}` 对应源文本中",
                        report_line,
                    )
                )


def lint_report_text(
    text: str,
    path: Path,
    profile: str = "full",
    *,
    source_document: SourceDocument | None = None,
    require_locators: bool = False,
) -> ReportLintResult:
    lines = text.splitlines()
    issues: list[ReportIssue] = []
    sections = _section_map(lines)

    for index, title in _duplicate_sections(lines):
        issues.append(
            ReportIssue("error", "duplicate-section", f"必需章节 `## {title}` 重复", index)
        )

    for marker in PLACEHOLDER_MARKERS:
        for index, line in enumerate(lines, start=1):
            if marker in line:
                issues.append(
                    ReportIssue("error", "placeholder", f"报告仍包含模板占位符 `{marker}`", index)
                )
    for index, line in enumerate(lines, start=1):
        if "TODO" in line or "FIXME" in line or "待补充" in line:
            issues.append(ReportIssue("error", "unfinished", "报告仍有未完成标记", index))

    for title in REQUIRED_SECTIONS:
        start, content = _section_lines(lines, sections, title)
        if start == 0:
            issues.append(ReportIssue("error", "missing-section", f"缺少必需章节 `## {title}`", 1))
            continue
        if not any(line.strip() for line in content):
            issues.append(ReportIssue("error", "empty-section", f"章节 `## {title}` 为空", start))

    if profile in FULL_PROFILES:
        argument_start, argument_lines = _section_lines(lines, sections, "论证地图")
        argument_text = "\n".join(argument_lines)
        argument_fields = _field_values(argument_text)
        for field in ARGUMENT_MAP_FIELDS:
            value = _field_value(argument_fields, field, prefix=True)
            if value is None:
                issues.append(
                    ReportIssue(
                        "error",
                        "argument-map-field",
                        f"论证地图缺少 `{field}`",
                        argument_start,
                    )
                )
            elif not _meaningful_field(value):
                issues.append(
                    ReportIssue(
                        "error",
                        "argument-map-empty",
                        f"论证地图字段 `{field}` 为空",
                        argument_start,
                    )
                )

        reverse_start, reverse_lines = _section_lines(lines, sections, "反向检验")
        reverse_text = "\n".join(reverse_lines)
        reverse_fields = _field_values(reverse_text)
        for field in REVERSE_TEST_FIELDS:
            value = _field_value(reverse_fields, field)
            if value is None:
                issues.append(
                    ReportIssue(
                        "error",
                        "reverse-test-field",
                        f"反向检验缺少 `{field}`",
                        reverse_start,
                    )
                )
            elif not _meaningful_field(value):
                issues.append(
                    ReportIssue(
                        "error",
                        "reverse-test-empty",
                        f"反向检验字段 `{field}` 为空",
                        reverse_start,
                    )
                )

        rewrite_start, rewrite_lines = _section_lines(lines, sections, "改写建议")
        if not any(line.lstrip().startswith(">") for line in rewrite_lines):
            issues.append(
                ReportIssue(
                    "error",
                    "rewrite-quote",
                    "改写建议应包含可直接引用的改写段落",
                    rewrite_start,
                )
            )

        boundary_start, boundary_lines = _section_lines(lines, sections, "边界说明")
        if not any(line.lstrip().startswith(("-", "*")) for line in boundary_lines):
            issues.append(
                ReportIssue(
                    "error",
                    "boundary-list",
                    "边界说明应列出至少一项明确限制",
                    boundary_start,
                )
            )

    problem_start, problem_lines = _section_lines(lines, sections, "关键问题")
    problem_text = "\n".join(problem_lines)
    if not any(line.strip() for line in problem_lines):
        issues.append(ReportIssue("error", "no-findings", "关键问题章节为空", problem_start))

    if profile in FULL_PROFILES:
        finding_blocks = re.split(r"(?m)^###\s+", problem_text)
        blocks = [block for block in finding_blocks[1:] if block.strip()]
        if not blocks:
            issues.append(
                ReportIssue("error", "no-finding-cards", "未找到 `###` 问题卡片", problem_start)
            )
        for block_index, block in enumerate(blocks, start=1):
            title = block.splitlines()[0].strip() if block.splitlines() else ""
            fields = _field_values(block)
            for field in ISSUE_FIELDS:
                value = _field_value(fields, field)
                if value is None:
                    issues.append(
                        ReportIssue(
                            "error",
                            "issue-field",
                            f"问题卡片 {block_index} `{title}` 缺少 `{field}`",
                            problem_start,
                        )
                    )
                elif not _meaningful_field(value):
                    issues.append(
                        ReportIssue(
                            "error",
                            "issue-field-empty",
                            f"问题卡片 {block_index} `{title}` 的 `{field}` 为空",
                            problem_start,
                        )
                    )
            quote = _field_value(fields, "原文")
            if not _meaningful_field(quote) or not any(
                line.lstrip().startswith(">") for line in (quote or "").splitlines()
            ):
                issues.append(
                    ReportIssue(
                        "error",
                        "issue-quote",
                        f"问题卡片 {block_index} 缺少原文引用",
                        problem_start,
                    )
                )
            _validate_citations(
                quote or "",
                source_document=source_document,
                require_locators=require_locators,
                card_label=f"问题卡片 {block_index}",
                report_line=problem_start,
                issues=issues,
            )
            verdict = _field_value(fields, "判定") or ""
            if not any(label in verdict for label in FINDING_LABELS):
                issues.append(
                    ReportIssue(
                        "error",
                        "issue-label",
                        f"问题卡片 {block_index} 缺少判定标签",
                        problem_start,
                    )
                )
            if not CONFIDENCE_PATTERN.search(verdict):
                issues.append(
                    ReportIssue(
                        "error",
                        "issue-confidence",
                        f"问题卡片 {block_index} 缺少置信度",
                        problem_start,
                    )
                )
            impact = _field_value(fields, "影响") or ""
            if not any(label in impact for label in IMPACT_LABELS):
                issues.append(
                    ReportIssue(
                        "error",
                        "issue-impact",
                        f"问题卡片 {block_index} 缺少影响等级",
                        problem_start,
                    )
                )
    else:
        if not any(label in problem_text for label in FINDING_LABELS):
            issues.append(
                ReportIssue("error", "quick-label", "Quick 报告缺少判定标签", problem_start)
            )
        if not CONFIDENCE_PATTERN.search(problem_text):
            issues.append(
                ReportIssue("error", "quick-confidence", "Quick 报告缺少置信度", problem_start)
            )
        if not any(line.lstrip().startswith(">") for line in problem_lines):
            issues.append(
                ReportIssue("error", "quick-quote", "Quick 报告缺少原文引用", problem_start)
            )
        quote_text = "\n".join(line for line in problem_lines if line.lstrip().startswith(">"))
        _validate_citations(
            quote_text,
            source_document=source_document,
            require_locators=require_locators,
            card_label="Quick 报告",
            report_line=problem_start,
            issues=issues,
        )

    return ReportLintResult(
        path=path,
        profile=profile,
        issues=issues,
        source_sha256=source_document.sha256 if source_document else None,
    )


def lint_report_file(
    path: Path,
    profile: str = "full",
    *,
    source_path: Path | None = None,
    require_locators: bool = False,
) -> ReportLintResult:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return ReportLintResult(
            path=path,
            profile=profile,
            issues=[ReportIssue("error", "read-error", str(exc), 1)],
        )
    source_document: SourceDocument | None = None
    source_issue: ReportIssue | None = None
    if source_path is not None:
        try:
            source_document = build_source_document(
                read_source(source_path),
                path=str(source_path),
            )
        except (OSError, UnicodeError) as exc:
            source_issue = ReportIssue("error", "source-read", str(exc), 1)
    result = lint_report_text(
        text,
        path,
        profile,
        source_document=source_document,
        require_locators=require_locators,
    )
    if source_issue is not None:
        result.issues.append(source_issue)
    return result


def format_result(result: ReportLintResult) -> str:
    lines = [
        f"{result.path}: {len(result.errors)} errors, {len(result.warnings)} warnings",
        *[issue.format() for issue in result.issues],
    ]
    return "\n".join(lines)


def result_to_dict(result: ReportLintResult) -> dict[str, object]:
    return {
        "path": str(result.path),
        "profile": result.profile,
        "errors": len(result.errors),
        "warnings": len(result.warnings),
        "source_sha256": result.source_sha256,
        "issues": [
            {
                "level": issue.level,
                "code": issue.code,
                "message": issue.message,
                "line": issue.line,
            }
            for issue in result.issues
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="report_lint",
        description="校验逻辑分析报告的结构、证据与边界字段",
    )
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument(
        "--profile",
        choices=["full", "debate", "quick", "teaching", "explainer"],
        default="full",
    )
    parser.add_argument("--strict", action="store_true", help="把警告也视为失败")
    parser.add_argument("--source", type=Path, help="可选源文本，用于核验 `[Lx-Ly]`")
    parser.add_argument(
        "--require-locators",
        action="store_true",
        help="要求每个问题卡提供至少一个 `[Lx-Ly]` 位置",
    )
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    results = [
        lint_report_file(
            path,
            args.profile,
            source_path=args.source,
            require_locators=args.require_locators,
        )
        for path in args.files
    ]
    if args.json:
        print(
            json.dumps([result_to_dict(result) for result in results], ensure_ascii=False, indent=2)
        )
    else:
        for result in results:
            print(format_result(result), file=sys.stderr if result.issues else sys.stdout)

    failed = any(result.errors or (args.strict and result.warnings) for result in results)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
