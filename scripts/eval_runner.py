from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from catalog_lib import ID_PATTERN, ROOT, load_catalog
from report_lint import (
    _field_value,
    _field_values,
    _section_lines,
    _section_map,
    lint_report_text,
)

CASES_PATH = ROOT / "evals" / "cases.jsonl"
LEDGER_PATH = ROOT / "evals" / "model-runs" / "ledger.jsonl"
DASHBOARD_PATH = ROOT / "docs" / "model-run-dashboard.md"
ALLOWED_RUN_TYPES = {"fixture", "model"}


@dataclass(frozen=True)
class EvalCase:
    id: str
    mode: str
    input: str
    must_detect: tuple[str, ...]
    may_detect: tuple[str, ...]
    must_not_assert: tuple[str, ...]


@dataclass(frozen=True)
class CaseResult:
    case_id: str
    report: str
    detected: tuple[str, ...]
    missing_must: tuple[str, ...]
    may_detect: tuple[str, ...]
    manual_checks: tuple[str, ...]
    lint_errors: int
    passed: bool

    def to_dict(self) -> dict[str, object]:
        return {
            "case_id": self.case_id,
            "report": self.report,
            "detected": list(self.detected),
            "missing_must": list(self.missing_must),
            "may_detect": list(self.may_detect),
            "manual_checks": list(self.manual_checks),
            "lint_errors": self.lint_errors,
            "passed": self.passed,
        }


@dataclass(frozen=True)
class RunRecord:
    run_id: str
    run_type: str
    model: str
    date: str
    prompt_version: str
    results: tuple[CaseResult, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "run_id": self.run_id,
            "run_type": self.run_type,
            "model": self.model,
            "date": self.date,
            "prompt_version": self.prompt_version,
            "results": [result.to_dict() for result in self.results],
        }


def _normalize(value: str) -> str:
    return value.casefold()


def load_cases(path: Path = CASES_PATH) -> list[EvalCase]:
    cases: list[EvalCase] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        cases.append(
            EvalCase(
                id=str(item["id"]),
                mode=str(item["mode"]),
                input=str(item["input"]),
                must_detect=tuple(str(value) for value in item["must_detect"]),
                may_detect=tuple(str(value) for value in item["may_detect"]),
                must_not_assert=tuple(str(value) for value in item["must_not_assert"]),
            )
        )
    return cases


def _verdict_text(report_text: str) -> str:
    lines = report_text.splitlines()
    sections = _section_map(lines)
    _start, problem_lines = _section_lines(lines, sections, "关键问题")
    problem_text = "\n".join(problem_lines)
    blocks = [block for block in re.split(r"(?m)^###\s+", problem_text) if block.strip()]
    verdicts: list[str] = []
    for block in blocks:
        verdict = _field_value(_field_values(block), "判定")
        if verdict:
            verdicts.append(verdict)
    return "\n".join(verdicts) if verdicts else problem_text


def detect_entry_ids(report_text: str) -> set[str]:
    catalog = load_catalog(ROOT)
    verdicts = unicodedata.normalize("NFKC", _verdict_text(report_text)).casefold()
    matches: list[tuple[int, int, str]] = []
    for entry in catalog.entries:
        tokens = [entry.id, entry.name_zh, entry.name_en, *entry.aliases]
        for token in tokens:
            normalized = unicodedata.normalize("NFKC", token).casefold().strip()
            if not normalized:
                continue
            for match in re.finditer(re.escape(normalized), verdicts):
                matches.append((match.start(), match.end(), entry.id))
    detected: set[str] = set()
    for start, end, entry_id in matches:
        contained = any(
            other_id != entry_id
            and other_start <= start
            and end <= other_end
            and (other_end - other_start) > (end - start)
            for other_start, other_end, other_id in matches
        )
        if not contained:
            detected.add(entry_id)
    return detected


def evaluate_case(
    case: EvalCase,
    report_path: Path,
    root: Path = ROOT,
) -> CaseResult:
    report_text = report_path.read_text(encoding="utf-8")
    lint = lint_report_text(report_text, report_path, profile=case.mode)
    detected = detect_entry_ids(report_text)
    missing = tuple(value for value in case.must_detect if value not in detected)
    optional = tuple(value for value in case.may_detect if value in detected)
    passed = not lint.errors and not missing
    try:
        display_path = str(report_path.relative_to(root))
    except ValueError:
        display_path = str(report_path)
    return CaseResult(
        case_id=case.id,
        report=display_path,
        detected=tuple(sorted(detected)),
        missing_must=missing,
        may_detect=optional,
        manual_checks=case.must_not_assert,
        lint_errors=len(lint.errors),
        passed=passed,
    )


def load_manifest(path: Path) -> dict[str, Path]:
    item = json.loads(path.read_text(encoding="utf-8"))
    return {str(case_id): Path(relative) for case_id, relative in item.items()}


def evaluate_manifest(
    manifest: dict[str, Path],
    *,
    run_id: str,
    run_type: str,
    model: str,
    date: str,
    prompt_version: str,
    root: Path = ROOT,
) -> RunRecord:
    cases = {case.id: case for case in load_cases()}
    results: list[CaseResult] = []
    for case_id, relative_path in manifest.items():
        if case_id not in cases:
            raise ValueError(f"manifest references unknown case `{case_id}`")
        report_path = relative_path if relative_path.is_absolute() else root / relative_path
        results.append(evaluate_case(cases[case_id], report_path, root))
    if not results:
        raise ValueError("manifest is empty")
    return RunRecord(
        run_id=run_id,
        run_type=run_type,
        model=model,
        date=date,
        prompt_version=prompt_version,
        results=tuple(results),
    )


def validate_run(record: RunRecord, case_ids: set[str]) -> list[str]:
    issues: list[str] = []
    if not ID_PATTERN.fullmatch(record.run_id):
        issues.append(f"invalid run id: {record.run_id}")
    if record.run_type not in ALLOWED_RUN_TYPES:
        issues.append(f"invalid run type: {record.run_type}")
    if not record.model or not record.date or not record.prompt_version:
        issues.append("model, date, and prompt_version must be non-empty")
    if not record.results:
        issues.append("run has no case results")
    seen: set[str] = set()
    for result in record.results:
        if result.case_id not in case_ids:
            issues.append(f"unknown case: {result.case_id}")
        if result.case_id in seen:
            issues.append(f"duplicate case: {result.case_id}")
        seen.add(result.case_id)
    return issues


def load_ledger(path: Path = LEDGER_PATH) -> list[RunRecord]:
    records: list[RunRecord] = []
    if not path.exists():
        return records
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        results = tuple(
            CaseResult(
                case_id=str(result["case_id"]),
                report=str(result["report"]),
                detected=tuple(result.get("detected", [])),
                missing_must=tuple(result.get("missing_must", [])),
                may_detect=tuple(result.get("may_detect", [])),
                manual_checks=tuple(result.get("manual_checks", [])),
                lint_errors=int(result.get("lint_errors", 0)),
                passed=bool(result.get("passed", False)),
            )
            for result in item.get("results", [])
        )
        records.append(
            RunRecord(
                run_id=str(item.get("run_id", "")),
                run_type=str(item.get("run_type", "")),
                model=str(item.get("model", "")),
                date=str(item.get("date", "")),
                prompt_version=str(item.get("prompt_version", "")),
                results=results,
            )
        )
    return records


def validate_ledger(records: list[RunRecord], case_ids: set[str]) -> list[str]:
    issues: list[str] = []
    seen: set[str] = set()
    for record in records:
        if record.run_id in seen:
            issues.append(f"duplicate run id: {record.run_id}")
        seen.add(record.run_id)
        issues.extend(validate_run(record, case_ids))
    return issues


def build_dashboard(records: list[RunRecord]) -> str:
    lines = [
        "# 模型运行看板",
        "",
        "> 本文件由 `python scripts/eval_runner.py dashboard` 生成。请修改 `evals/model-runs/ledger.jsonl`。",
        "",
        "## 总览",
        "",
        "| 项目 | 数量 |",
        "|---|---:|",
        f"| 运行记录 | {len(records)} |",
        f"| 模型运行 | {sum(record.run_type == 'model' for record in records)} |",
        f"| Fixture 运行 | {sum(record.run_type == 'fixture' for record in records)} |",
        "",
        "## 最近运行",
        "",
        "| Run | 类型 | 模型 | 日期 | Prompt | 通过 | 案例数 |",
        "|---|---|---|---|---|---:|---:|",
    ]
    for record in records:
        passed = sum(result.passed for result in record.results)
        lines.append(
            f"| `{record.run_id}` | {record.run_type} | {record.model} | {record.date} | "
            f"`{record.prompt_version}` | {passed} | {len(record.results)} |"
        )
    if not records:
        lines.append("| - | - | - | - | - | 0 | 0 |")

    failures = [
        (record, result) for record in records for result in record.results if not result.passed
    ]
    lines.extend(
        [
            "",
            "## 失败与缺口",
            "",
            "| Run | Case | 缺失主判 | Lint 错误 | 手动检查 |",
            "|---|---|---|---:|---|",
        ]
    )
    if failures:
        for record, result in failures:
            missing = "、".join(result.missing_must) or "无"
            manual = "、".join(result.manual_checks) or "无"
            lines.append(
                f"| `{record.run_id}` | `{result.case_id}` | {missing} | "
                f"{result.lint_errors} | {manual} |"
            )
    else:
        lines.append("| - | - | 当前没有自动失败 | 0 | - |")

    model_counts = Counter(
        result.case_id
        for record in records
        if record.run_type == "model"
        for result in record.results
        if result.passed
    )
    lines.extend(
        [
            "",
            "## 覆盖摘要",
            "",
            "`must_not_assert` 保留为人工复核项；自动看板只判断结构、主判覆盖和可选邻近标签。",
            "",
            f"已通过真实模型案例数：{len(model_counts)}（按 case 去重）。",
            "",
        ]
    )
    return "\n".join(lines)


def append_run(record: RunRecord, path: Path = LEDGER_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record.to_dict(), ensure_ascii=False) + "\n")


def write_dashboard(records: list[RunRecord], output: Path = DASHBOARD_PATH) -> Path:
    output.write_text(build_dashboard(records), encoding="utf-8", newline="\n")
    return output


def dashboard_is_current(output: Path = DASHBOARD_PATH) -> bool:
    records = load_ledger()
    case_ids = {case.id for case in load_cases()}
    return (
        not validate_ledger(records, case_ids)
        and output.exists()
        and output.read_text(encoding="utf-8") == build_dashboard(records)
    )


def run_command(args: argparse.Namespace) -> int:
    manifest = load_manifest(Path(args.manifest))
    record = evaluate_manifest(
        manifest,
        run_id=args.run_id,
        run_type=args.run_type,
        model=args.model,
        date=args.date,
        prompt_version=args.prompt_version,
    )
    case_ids = {case.id for case in load_cases()}
    issues = validate_run(record, case_ids)
    if issues:
        for issue in issues:
            print(f"[ERROR] {issue}", file=sys.stderr)
        return 1
    append_run(record)
    write_dashboard(load_ledger())
    passed = sum(result.passed for result in record.results)
    print(f"已记录 {record.run_id}: {passed}/{len(record.results)} 通过")
    return 0 if passed == len(record.results) else 1


def dashboard_command(args: argparse.Namespace) -> int:
    records = load_ledger()
    case_ids = {case.id for case in load_cases()}
    issues = validate_ledger(records, case_ids)
    if issues:
        for issue in issues:
            print(f"[ERROR] {issue}", file=sys.stderr)
        return 1
    if args.check:
        if not dashboard_is_current():
            print("[DRIFT] docs/model-run-dashboard.md", file=sys.stderr)
            return 1
        print("模型运行看板已与账本一致。")
        return 0
    output = write_dashboard(records)
    print(f"已生成 {output.relative_to(ROOT)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="记录模型评测运行并生成看板")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="从一个报告清单记录评测运行")
    run_parser.add_argument("--manifest", required=True)
    run_parser.add_argument("--run-id", required=True)
    run_parser.add_argument("--run-type", choices=sorted(ALLOWED_RUN_TYPES), required=True)
    run_parser.add_argument("--model", required=True)
    run_parser.add_argument("--date", required=True)
    run_parser.add_argument("--prompt-version", required=True)
    run_parser.set_defaults(func=run_command)

    dashboard_parser = subparsers.add_parser("dashboard", help="生成模型运行看板")
    dashboard_parser.add_argument("--check", action="store_true")
    dashboard_parser.set_defaults(func=dashboard_command)

    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"[ERROR] eval-runner: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
