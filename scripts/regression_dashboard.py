from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from catalog_lib import ID_PATTERN, ROOT

REGRESSIONS_PATH = ROOT / "evals" / "regressions.jsonl"
CASES_PATH = ROOT / "evals" / "cases.jsonl"
DASHBOARD_PATH = ROOT / "docs" / "regression-dashboard.md"

ALLOWED_STATUSES = {"fixed", "open", "invalidated", "boundary"}
ALLOWED_SEVERITIES = {"high", "medium", "low"}


@dataclass(frozen=True)
class RegressionRecord:
    id: str
    status: str
    severity: str
    category: str
    summary: str
    introduced: str
    resolved_in: str | None
    case_ids: tuple[str, ...]
    evidence: tuple[str, ...]


@dataclass(frozen=True)
class DashboardIssue:
    code: str
    message: str
    record_id: str = ""

    def format(self) -> str:
        suffix = f" ({self.record_id})" if self.record_id else ""
        return f"[ERROR] {self.code}{suffix}: {self.message}"


def load_case_ids(path: Path = CASES_PATH) -> set[str]:
    ids: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            item = json.loads(line)
            ids.add(str(item.get("id", "")))
    return ids


def load_regressions(path: Path = REGRESSIONS_PATH) -> list[RegressionRecord]:
    records: list[RegressionRecord] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        records.append(
            RegressionRecord(
                id=str(item.get("id", "")),
                status=str(item.get("status", "")),
                severity=str(item.get("severity", "")),
                category=str(item.get("category", "")),
                summary=str(item.get("summary", "")),
                introduced=str(item.get("introduced", "")),
                resolved_in=item.get("resolved_in"),
                case_ids=tuple(str(value) for value in item.get("case_ids", [])),
                evidence=tuple(str(value) for value in item.get("evidence", [])),
            )
        )
    return records


def validate_regressions(
    records: list[RegressionRecord],
    case_ids: set[str],
) -> list[DashboardIssue]:
    issues: list[DashboardIssue] = []
    seen: set[str] = set()
    for record in records:
        if not ID_PATTERN.fullmatch(record.id):
            issues.append(DashboardIssue("invalid-id", "回归 ID 必须是 kebab-case", record.id))
        if record.id in seen:
            issues.append(DashboardIssue("duplicate-id", "回归 ID 重复", record.id))
        seen.add(record.id)
        if record.status not in ALLOWED_STATUSES:
            issues.append(DashboardIssue("invalid-status", "status 无效", record.id))
        if record.severity not in ALLOWED_SEVERITIES:
            issues.append(DashboardIssue("invalid-severity", "severity 无效", record.id))
        if not record.category or not record.summary or not record.introduced:
            issues.append(DashboardIssue("missing-text", "文本字段不能为空", record.id))
        if record.status == "fixed" and not record.resolved_in:
            issues.append(
                DashboardIssue("missing-resolution", "fixed 记录缺少 resolved_in", record.id)
            )
        if record.status != "fixed" and record.resolved_in:
            issues.append(
                DashboardIssue(
                    "unexpected-resolution", "非 fixed 记录不应填写 resolved_in", record.id
                )
            )
        if not record.evidence:
            issues.append(DashboardIssue("missing-evidence", "至少需要一条证据", record.id))
        for case_id in record.case_ids:
            if case_id not in case_ids:
                issues.append(
                    DashboardIssue("unknown-case", f"引用不存在评测 `{case_id}`", record.id)
                )
    return issues


def _status_label(status: str) -> str:
    return {
        "fixed": "已修复",
        "open": "仍存在",
        "invalidated": "已失效",
        "boundary": "边界变化",
    }[status]


def _sorted(records: list[RegressionRecord]) -> list[RegressionRecord]:
    severity_order = {"high": 0, "medium": 1, "low": 2}
    return sorted(records, key=lambda record: (severity_order[record.severity], record.id))


def build_dashboard(records: list[RegressionRecord]) -> str:
    status_counts = Counter(record.status for record in records)
    severity_counts = Counter(record.severity for record in records if record.status == "open")
    lines = [
        "# 误报与回归看板",
        "",
        "> 本文件由 `python scripts/regression_dashboard.py` 生成。请修改 `evals/regressions.jsonl`。",
        "",
        "## 总览",
        "",
        "| 状态 | 数量 |",
        "|---|---:|",
    ]
    for status in ["open", "fixed", "invalidated", "boundary"]:
        lines.append(f"| {_status_label(status)} | {status_counts[status]} |")
    lines.extend(
        [
            "",
            "| Open 严重度 | 数量 |",
            "|---|---:|",
        ]
    )
    for severity in ["high", "medium", "low"]:
        lines.append(f"| {severity} | {severity_counts[severity]} |")

    for status in ["open", "fixed", "invalidated", "boundary"]:
        subset = _sorted([record for record in records if record.status == status])
        lines.extend(
            [
                "",
                f"## {_status_label(status)}",
                "",
                "| ID | 严重度 | 类别 | 问题 | 解析版本 | 关联评测 | 证据 |",
                "|---|---|---|---|---|---|---|",
            ]
        )
        if not subset:
            lines.append("| - | - | - | 当前没有记录 | - | - | - |")
            continue
        for record in subset:
            cases = "、".join(f"`{case_id}`" for case_id in record.case_ids) or "无"
            evidence = "<br>".join(f"`{path}`" for path in record.evidence)
            resolved = f"`{record.resolved_in}`" if record.resolved_in else "-"
            lines.append(
                f"| `{record.id}` | {record.severity} | {record.category} | "
                f"{record.summary} | {resolved} | {cases} | {evidence} |"
            )
    lines.extend(
        [
            "",
            "## 使用规则",
            "",
            "- 新发现的误报或校验缺陷先登记为 `open`。",
            "- 修复后填写 `resolved_in` 和可复核证据。",
            "- 如果问题被证明不是缺陷，改为 `invalidated`。",
            "- 如果结论未变但适用边界改变，改为 `boundary`。",
            "- fixed 记录不会删除，用于防止同类问题回归。",
            "",
        ]
    )
    return "\n".join(lines)


def write_dashboard(output: Path = DASHBOARD_PATH) -> Path:
    records = load_regressions()
    case_ids = load_case_ids()
    issues = validate_regressions(records, case_ids)
    if issues:
        raise ValueError("\n".join(issue.format() for issue in issues))
    output.write_text(build_dashboard(records), encoding="utf-8", newline="\n")
    return output


def dashboard_is_current(output: Path = DASHBOARD_PATH) -> bool:
    records = load_regressions()
    case_ids = load_case_ids()
    issues = validate_regressions(records, case_ids)
    if issues:
        return False
    return output.exists() and output.read_text(encoding="utf-8") == build_dashboard(records)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="校验回归账本并生成误报看板")
    parser.add_argument("--check", action="store_true", help="只检查生成文件是否漂移")
    args = parser.parse_args(argv)
    try:
        records = load_regressions()
        issues = validate_regressions(records, load_case_ids())
    except (OSError, json.JSONDecodeError) as exc:
        print(f"[ERROR] ledger-read: {exc}", file=sys.stderr)
        return 1
    if issues:
        for issue in issues:
            print(issue.format(), file=sys.stderr)
        return 1
    if args.check:
        if not dashboard_is_current():
            print("[DRIFT] docs/regression-dashboard.md", file=sys.stderr)
            return 1
        print("回归看板已与账本一致。")
        return 0
    output = write_dashboard()
    print(f"已生成 {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
