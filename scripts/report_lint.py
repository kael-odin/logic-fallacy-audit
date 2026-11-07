from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REQUIRED_SECTIONS = [
    "结论摘要",
    "论证地图",
    "关键问题",
    "反向检验",
    "改写建议",
    "边界说明",
]

ARGUMENT_MAP_FIELDS = [
    "最终结论",
    "显式前提",
    "必要隐含前提",
    "隐含前提的重建依据",
    "推理类型",
    "当前缺失环节",
]

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

REVERSE_TEST_FIELDS = [
    "最强版本",
    "反例或关键测试",
    "替代解释",
    "可能误判",
]

FINDING_LABELS = ("确认", "较可能", "语境相关", "不构成谬误")
IMPACT_LABELS = ("阻断", "重大", "局部", "表达")
CONFIDENCE_PATTERN = re.compile(r"置信度\s*[:：]\s*(高|中|低)")
HEADING_PATTERN = re.compile(r"^(#{2,3})\s+(.+?)\s*$")
PLACEHOLDER_MARKERS = (
    "[问题标题]",
    "[必要片段]",
    "[中性重述最终主张]",
    "[说明上下文缺口]",
    "[按相同结构重复。]",
    "[使结论成立所需但未明说的前提]",
    "[2–4 句",
)


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
    bounds = sections.get(title)
    if bounds is None:
        return 0, []
    start, end = bounds
    return start + 1, lines[start + 1 : end]


def lint_report_text(text: str, path: Path, profile: str = "full") -> ReportLintResult:
    lines = text.splitlines()
    issues: list[ReportIssue] = []
    sections = _section_map(lines)

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
        if title not in sections:
            issues.append(ReportIssue("error", "missing-section", f"缺少必需章节 `## {title}`", 1))
            continue
        _, content = _section_lines(lines, sections, title)
        if not any(line.strip() for line in content):
            start, _ = _section_lines(lines, sections, title)
            issues.append(ReportIssue("error", "empty-section", f"章节 `## {title}` 为空", start))

    if profile in {"full", "debate"}:
        argument_start, argument_lines = _section_lines(lines, sections, "论证地图")
        argument_text = "\n".join(argument_lines)
        for field in ARGUMENT_MAP_FIELDS:
            if field not in argument_text:
                issues.append(
                    ReportIssue(
                        "error",
                        "argument-map-field",
                        f"论证地图缺少 `{field}`",
                        argument_start,
                    )
                )

        reverse_start, reverse_lines = _section_lines(lines, sections, "反向检验")
        reverse_text = "\n".join(reverse_lines)
        for field in REVERSE_TEST_FIELDS:
            if f"**{field}**" not in reverse_text:
                issues.append(
                    ReportIssue(
                        "error",
                        "reverse-test-field",
                        f"反向检验缺少 `{field}`",
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

    if profile in {"full", "debate"}:
        finding_blocks = re.split(r"(?m)^###\s+", problem_text)
        blocks = [block for block in finding_blocks[1:] if block.strip()]
        if not blocks:
            issues.append(
                ReportIssue("error", "no-finding-cards", "未找到 `###` 问题卡片", problem_start)
            )
        for block_index, block in enumerate(blocks, start=1):
            title = block.splitlines()[0].strip() if block.splitlines() else ""
            for field in ISSUE_FIELDS:
                if f"**{field}**" not in block:
                    issues.append(
                        ReportIssue(
                            "error",
                            "issue-field",
                            f"问题卡片 {block_index} `{title}` 缺少 `{field}`",
                            problem_start,
                        )
                    )
            if not any(line.lstrip().startswith(">") for line in block.splitlines()):
                issues.append(
                    ReportIssue(
                        "error",
                        "issue-quote",
                        f"问题卡片 {block_index} 缺少原文引用",
                        problem_start,
                    )
                )
            if not any(label in block for label in FINDING_LABELS):
                issues.append(
                    ReportIssue(
                        "error",
                        "issue-label",
                        f"问题卡片 {block_index} 缺少判定标签",
                        problem_start,
                    )
                )
            if not CONFIDENCE_PATTERN.search(block):
                issues.append(
                    ReportIssue(
                        "error",
                        "issue-confidence",
                        f"问题卡片 {block_index} 缺少置信度",
                        problem_start,
                    )
                )
            if not any(label in block for label in IMPACT_LABELS):
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

    return ReportLintResult(path=path, profile=profile, issues=issues)


def lint_report_file(path: Path, profile: str = "full") -> ReportLintResult:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return ReportLintResult(
            path=path,
            profile=profile,
            issues=[ReportIssue("error", "read-error", str(exc), 1)],
        )
    return lint_report_text(text, path, profile)


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
        choices=["full", "debate", "quick", "teaching"],
        default="full",
    )
    parser.add_argument("--strict", action="store_true", help="把警告也视为失败")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    results = [lint_report_file(path, args.profile) for path in args.files]
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
