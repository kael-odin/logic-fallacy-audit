from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

from report_lint import (
    _field_value,
    _field_values,
    _section_lines,
    _section_map,
)

LABELLED_ITEM_PATTERN = re.compile(
    r"(?m)^\s*(?:[-*]\s*|>\s*)?(?P<id>[CPA]\d+)\s*[:：]\s*(?P<label>.+?)\s*$"
)


@dataclass(frozen=True)
class ArgumentNode:
    id: str
    label: str


@dataclass(frozen=True)
class DiagramIssue:
    id: str
    title: str
    verdict: str
    impact: str


@dataclass(frozen=True)
class ReportDiagram:
    conclusions: tuple[ArgumentNode, ...]
    premises: tuple[ArgumentNode, ...]
    assumptions: tuple[ArgumentNode, ...]
    issues: tuple[DiagramIssue, ...]
    rewrite: str


def _section_text(text: str, canonical: str) -> str:
    lines = text.splitlines()
    sections = _section_map(lines)
    _start, content = _section_lines(lines, sections, canonical)
    return "\n".join(content).strip()


def _field_text(text: str, canonical: str, *, prefix: bool = False) -> str:
    return _field_value(_field_values(text), canonical, prefix=prefix) or ""


def _labelled_items(value: str) -> tuple[ArgumentNode, ...]:
    return tuple(
        ArgumentNode(id=match.group("id"), label=match.group("label").strip())
        for match in LABELLED_ITEM_PATTERN.finditer(value)
    )


def _extract_issues(text: str) -> tuple[DiagramIssue, ...]:
    problem_text = _section_text(text, "关键问题")
    blocks = [block for block in re.split(r"(?m)^###\s+", problem_text) if block.strip()]
    issues: list[DiagramIssue] = []
    for index, block in enumerate(blocks, start=1):
        title = block.splitlines()[0].strip()
        fields = _field_values(block)
        verdict = _field_value(fields, "判定") or ""
        impact = _field_value(fields, "影响") or ""
        issues.append(
            DiagramIssue(
                id=f"I{index}",
                title=title,
                verdict=" ".join(verdict.split()),
                impact=" ".join(impact.split()),
            )
        )
    return tuple(issues)


def _first_quote(text: str, canonical: str) -> str:
    section = _section_text(text, canonical)
    for line in section.splitlines():
        if line.lstrip().startswith(">"):
            return line.lstrip()[1:].strip()
    return ""


def parse_report_diagram(text: str) -> ReportDiagram:
    argument_map = _section_text(text, "论证地图")
    conclusions = _labelled_items(_field_text(argument_map, "最终结论"))
    premises = _labelled_items(_field_text(argument_map, "显式前提"))
    assumptions = _labelled_items(_field_text(argument_map, "必要隐含前提", prefix=True))
    if not conclusions:
        raise ValueError("论证地图缺少 C1 结论")
    return ReportDiagram(
        conclusions=conclusions,
        premises=premises,
        assumptions=assumptions,
        issues=_extract_issues(text),
        rewrite=_first_quote(text, "改写建议"),
    )


def _label(text: str, limit: int = 84) -> str:
    compact = " ".join(text.split())
    compact = compact.replace("`", "").replace('"', "'").replace("[", "(").replace("]", ")")
    if len(compact) > limit:
        compact = compact[: limit - 1] + "…"
    return compact


def _argument_lines(diagram: ReportDiagram) -> list[str]:
    lines: list[str] = []
    for node in diagram.conclusions:
        lines.append(f'  {node.id}["{node.id} · {_label(node.label)}"]')
    for node in diagram.premises:
        lines.append(f'  {node.id}["{node.id} · {_label(node.label)}"]')
    for node in diagram.assumptions:
        lines.append(f'  {node.id}["{node.id} · reconstructed：{_label(node.label)}"]')
    return lines


def _edge_lines(diagram: ReportDiagram) -> list[str]:
    target = diagram.conclusions[0].id
    lines = [f"  {node.id} --> {target}" for node in diagram.premises]
    lines.extend(f"  {node.id} -.assumption.-> {target}" for node in diagram.assumptions)
    return lines


def _style_lines() -> list[str]:
    return [
        "  classDef conclusion fill:#FDE68A,stroke:#92400E,color:#111827;",
        "  classDef premise fill:#DBEAFE,stroke:#1D4ED8,color:#111827;",
        "  classDef assumption fill:#EDE9FE,stroke:#6D28D9,color:#111827;",
        "  classDef issue fill:#FEE2E2,stroke:#B91C1C,color:#111827;",
        "  classDef rewrite fill:#DCFCE7,stroke:#15803D,color:#111827;",
    ]


def _class_assignments(diagram: ReportDiagram) -> list[str]:
    lines: list[str] = []
    if diagram.conclusions:
        lines.append(f"  class {','.join(node.id for node in diagram.conclusions)} conclusion;")
    if diagram.premises:
        lines.append(f"  class {','.join(node.id for node in diagram.premises)} premise;")
    if diagram.assumptions:
        lines.append(f"  class {','.join(node.id for node in diagram.assumptions)} assumption;")
    return lines


def render_argument_mermaid(diagram: ReportDiagram) -> str:
    lines = [
        "```mermaid",
        "flowchart TD",
        *_argument_lines(diagram),
        *_edge_lines(diagram),
        *_style_lines(),
        *_class_assignments(diagram),
        "```",
    ]
    return "\n".join(lines)


def render_issues_mermaid(diagram: ReportDiagram) -> str:
    target = diagram.conclusions[0].id
    lines = ["```mermaid", "flowchart TD", *_argument_lines(diagram), *_edge_lines(diagram)]
    for issue in diagram.issues:
        verdict = _label(issue.verdict, 64)
        impact = _label(issue.impact, 42)
        lines.append(
            f'  {issue.id}["{issue.id} · {_label(issue.title)}<br/>{verdict}<br/>{impact}"]'
        )
        lines.append(f"  {issue.id} -.affects.-> {target}")
    lines.extend(_style_lines())
    lines.extend(_class_assignments(diagram))
    if diagram.issues:
        lines.append(f"  class {','.join(issue.id for issue in diagram.issues)} issue;")
    lines.append("```")
    return "\n".join(lines)


def render_compare_mermaid(diagram: ReportDiagram) -> str:
    lines = [
        "```mermaid",
        "flowchart LR",
        "  subgraph BEFORE[Before / 修复前]",
        *[f"    {line.strip()}" for line in _argument_lines(diagram)],
        *[f"    {line.strip()}" for line in _edge_lines(diagram)],
        "  end",
        "  subgraph ISSUES[Issues / 问题]",
    ]
    for issue in diagram.issues:
        lines.append(
            f'    {issue.id}["{issue.id} · {_label(issue.title, 58)}<br/>'
            f'{_label(issue.impact, 36)}"]'
        )
    lines.extend(
        [
            "  end",
            "  subgraph AFTER[After / 修复后]",
            f'    R1["R1 · {_label(diagram.rewrite or "按修复条件收窄结论", 110)}"]',
            "  end",
        ]
    )
    for issue in diagram.issues:
        lines.append(f"  {issue.id} -.repair.-> R1")
    if not diagram.issues:
        lines.append(f"  {diagram.conclusions[0].id} -.rewrite.-> R1")
    lines.extend(_style_lines())
    lines.extend(_class_assignments(diagram))
    if diagram.issues:
        lines.append(f"  class {','.join(issue.id for issue in diagram.issues)} issue;")
    lines.append("  class R1 rewrite;")
    lines.append("```")
    return "\n".join(lines)


def render_diagram(diagram: ReportDiagram, kind: str) -> str:
    if kind == "argument":
        return render_argument_mermaid(diagram)
    if kind == "issues":
        return render_issues_mermaid(diagram)
    if kind == "compare":
        return render_compare_mermaid(diagram)
    raise ValueError(f"unsupported diagram kind: {kind}")


def diagram_to_dict(diagram: ReportDiagram) -> dict[str, object]:
    return {
        "conclusions": [node.__dict__ for node in diagram.conclusions],
        "premises": [node.__dict__ for node in diagram.premises],
        "assumptions": [node.__dict__ for node in diagram.assumptions],
        "issues": [issue.__dict__ for issue in diagram.issues],
        "rewrite": diagram.rewrite,
    }


def load_report_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def diagram_command_payload(path: Path, kind: str) -> dict[str, object]:
    diagram = parse_report_diagram(load_report_text(path))
    return {
        "path": str(path),
        "kind": kind,
        "diagram": diagram_to_dict(diagram),
        "mermaid": render_diagram(diagram, kind),
    }


def payload_to_json(payload: dict[str, object]) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2)
