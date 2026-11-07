from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from catalog_lib import (
    CORE_FALLACY_IDS,
    COVERAGE_SNAPSHOT_DATE,
    ROOT,
    CatalogParseError,
    build_coverage_doc,
    format_catalog_stats,
    format_entry,
    generated_drift,
    iter_entry_summaries,
    load_catalog,
    search_entries,
    validate_catalog,
    validate_repository,
    write_generated_files,
)
from regression_dashboard import dashboard_is_current, write_dashboard
from report_diagram import diagram_to_dict, parse_report_diagram, render_diagram
from report_lint import format_result, lint_report_file, result_to_dict
from source_map import (
    build_source_document,
    format_quote_matches,
    format_source_document,
    locate_quote,
    quote_matches_to_dict,
    read_source,
    source_document_to_dict,
)


def _print_issues(issues: list, strict: bool) -> int:
    errors = [item for item in issues if item.level == "error"]
    warnings = [item for item in issues if item.level == "warning"]
    for item in issues:
        print(item.format(), file=sys.stderr)
    print(
        f"检查完成：{len(errors)} 个错误，{len(warnings)} 个警告。",
        file=sys.stderr,
    )
    return 1 if errors or (strict and warnings) else 0


def command_validate(args: argparse.Namespace) -> int:
    try:
        catalog = load_catalog(ROOT)
    except CatalogParseError as exc:
        print(f"[ERROR] catalog-parse: {exc}", file=sys.stderr)
        return 1
    issues = validate_repository(catalog)
    return _print_issues(issues, args.strict)


def command_stats(args: argparse.Namespace) -> int:
    catalog = load_catalog(ROOT)
    if args.json:
        payload = {
            "total": len(catalog.entries),
            "fallacies": len(catalog.fallacy_entries),
            "biases": len(catalog.bias_entries),
            "categories": {
                category.id: {
                    "name_zh": category.name_zh,
                    "name_en": category.name_en,
                    "count": catalog.counts[category.id],
                }
                for category in catalog.categories
            },
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(format_catalog_stats(catalog))
    return 0


def command_coverage(args: argparse.Namespace) -> int:
    catalog = load_catalog(ROOT)
    if args.json:
        payload = {
            "snapshot_date": COVERAGE_SNAPSHOT_DATE,
            "total": len(catalog.entries),
            "fallacies": len(catalog.fallacy_entries),
            "biases": len(catalog.bias_entries),
            "categories": len(catalog.categories),
            "core_fallacies": {
                entry_id: {
                    "name_zh": catalog.entry_by_id[entry_id].name_zh,
                    "name_en": catalog.entry_by_id[entry_id].name_en,
                    "diagnostic_questions": len(catalog.entry_by_id[entry_id].data["diagnostic"]),
                }
                for entry_id in CORE_FALLACY_IDS
            },
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(build_coverage_doc(catalog))
    return 0


def command_categories(args: argparse.Namespace) -> int:
    catalog = load_catalog(ROOT)
    for category in catalog.categories:
        print(
            f"{category.id}\t{category.name_zh}\t{category.name_en}\t{catalog.counts[category.id]}"
        )
    return 0


def command_search(args: argparse.Namespace) -> int:
    catalog = load_catalog(ROOT)
    matches = search_entries(catalog, args.query, limit=args.limit)
    if args.json:
        print(
            json.dumps(
                [item.data | {"source": item.source} for item in matches],
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0
    if not matches:
        print("没有匹配条目。")
        return 0
    for line in iter_entry_summaries(matches):
        print(line)
    return 0


def command_show(args: argparse.Namespace) -> int:
    catalog = load_catalog(ROOT)
    item = catalog.entry_by_id.get(args.id)
    if item is None:
        matches = search_entries(catalog, args.id, limit=5)
        if matches:
            print(f"未找到 ID `{args.id}`。你可能要找：", file=sys.stderr)
            for line in iter_entry_summaries(matches):
                print(line, file=sys.stderr)
        else:
            print(f"未找到 ID `{args.id}`。", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(item.data | {"source": item.source}, ensure_ascii=False, indent=2))
    else:
        print(format_entry(item, catalog))
    return 0


def command_list(args: argparse.Namespace) -> int:
    catalog = load_catalog(ROOT)
    entries = catalog.entries
    if args.category:
        if args.category not in catalog.category_by_id:
            print(f"未知分类：{args.category}", file=sys.stderr)
            return 1
        entries = [item for item in entries if item.category == args.category]
    for line in iter_entry_summaries(entries):
        print(line)
    return 0


def command_render(args: argparse.Namespace) -> int:
    catalog = load_catalog(ROOT)
    issues = validate_catalog(catalog)
    errors = [item for item in issues if item.level == "error"]
    if errors:
        for item in errors:
            print(item.format(), file=sys.stderr)
        print("目录存在错误，未生成文件。", file=sys.stderr)
        return 1

    if args.check:
        drift = generated_drift(catalog)
        if drift:
            for path in drift:
                print(f"[DRIFT] {path.relative_to(ROOT)}", file=sys.stderr)
            print("生成文件与 catalog 数据不一致，请运行 render。", file=sys.stderr)
            return 1
        print("生成文件已与 catalog 数据一致。")
        return 0

    written, removed = write_generated_files(catalog)
    for path in written:
        print(f"已生成 {path.relative_to(ROOT)}")
    for path in removed:
        print(f"已移除残留 {path.relative_to(ROOT)}")
    return 0


def command_lint_report(args: argparse.Namespace) -> int:
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
            json.dumps(
                [result_to_dict(result) for result in results],
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        for result in results:
            print(format_result(result))
    failed = any(result.errors or (args.strict and result.warnings) for result in results)
    return 1 if failed else 0


def _load_source(args: argparse.Namespace):
    try:
        text = read_source(args.source)
    except (OSError, UnicodeError) as exc:
        print(f"[ERROR] source-read: {exc}", file=sys.stderr)
        return None
    max_chars = int(getattr(args, "max_chars", 0))
    if max_chars < 0:
        print("[ERROR] max-chars: 必须是非负整数", file=sys.stderr)
        return None
    return build_source_document(
        text,
        path=str(args.source),
        max_chars=max_chars,
    )


def command_segment(args: argparse.Namespace) -> int:
    document = _load_source(args)
    if document is None:
        return 1
    if args.json:
        print(json.dumps(source_document_to_dict(document), ensure_ascii=False, indent=2))
    else:
        print(format_source_document(document))
    return 0


def command_locate(args: argparse.Namespace) -> int:
    document = _load_source(args)
    if document is None:
        return 1
    try:
        matches = locate_quote(document, args.quote)
    except ValueError as exc:
        print(f"[ERROR] quote: {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(
            json.dumps(
                {
                    "path": document.path,
                    "sha256": document.sha256,
                    "matches": quote_matches_to_dict(matches),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(format_quote_matches(matches))
    return 0 if matches else 1


def command_diagram(args: argparse.Namespace) -> int:
    try:
        text = args.report.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"[ERROR] report-read: {exc}", file=sys.stderr)
        return 1
    try:
        diagram = parse_report_diagram(text)
        mermaid = render_diagram(diagram, args.kind)
    except ValueError as exc:
        print(f"[ERROR] diagram: {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(
            json.dumps(
                {
                    "path": str(args.report),
                    "kind": args.kind,
                    "diagram": diagram_to_dict(diagram),
                    "mermaid": mermaid,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(mermaid)
    return 0


def command_regression_dashboard(args: argparse.Namespace) -> int:
    if args.check:
        if not dashboard_is_current():
            print("[DRIFT] docs/regression-dashboard.md", file=sys.stderr)
            return 1
        print("回归看板已与账本一致。")
        return 0
    try:
        output = write_dashboard()
    except (OSError, ValueError) as exc:
        print(f"[ERROR] regression-dashboard: {exc}", file=sys.stderr)
        return 1
    print(f"已生成 {output.relative_to(ROOT)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="fallacy_cli",
        description="逻辑谬误目录校验、检索与 Markdown 生成工具",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate", help="校验仓库、目录、链接和评测")
    validate_parser.add_argument(
        "--strict",
        action="store_true",
        help="把警告也视为失败",
    )
    validate_parser.set_defaults(func=command_validate)

    stats_parser = subparsers.add_parser("stats", help="显示条目统计")
    stats_parser.add_argument("--json", action="store_true")
    stats_parser.set_defaults(func=command_stats)

    coverage_parser = subparsers.add_parser("coverage", help="显示知识覆盖与字段完整性审计")
    coverage_parser.add_argument("--json", action="store_true")
    coverage_parser.set_defaults(func=command_coverage)

    categories_parser = subparsers.add_parser("categories", help="列出分类")
    categories_parser.set_defaults(func=command_categories)

    search_parser = subparsers.add_parser("search", help="搜索条目")
    search_parser.add_argument("query")
    search_parser.add_argument("--limit", type=int, default=10)
    search_parser.add_argument("--json", action="store_true")
    search_parser.set_defaults(func=command_search)

    show_parser = subparsers.add_parser("show", help="显示一个条目的完整内容")
    show_parser.add_argument("id")
    show_parser.add_argument("--json", action="store_true")
    show_parser.set_defaults(func=command_show)

    list_parser = subparsers.add_parser("list", help="列出所有或某一分类的条目")
    list_parser.add_argument("category", nargs="?")
    list_parser.set_defaults(func=command_list)

    render_parser = subparsers.add_parser("render", help="生成 Markdown 分类目录")
    render_parser.add_argument(
        "--check",
        action="store_true",
        help="只检查生成文件是否有漂移",
    )
    render_parser.set_defaults(func=command_render)

    report_parser = subparsers.add_parser(
        "lint-report",
        help="校验 Markdown 逻辑分析报告的章节、证据与边界",
    )
    report_parser.add_argument("files", nargs="+", type=Path)
    report_parser.add_argument(
        "--profile",
        choices=["full", "debate", "quick", "teaching", "explainer"],
        default="full",
    )
    report_parser.add_argument("--strict", action="store_true")
    report_parser.add_argument("--source", type=Path, help="可选源文本，用于核验 `[Lx-Ly]`")
    report_parser.add_argument(
        "--require-locators",
        action="store_true",
        help="要求每个问题卡提供至少一个 `[Lx-Ly]` 位置",
    )
    report_parser.add_argument("--json", action="store_true")
    report_parser.set_defaults(func=command_lint_report)

    segment_parser = subparsers.add_parser(
        "segment",
        help="按段落生成源文本行号与候选块",
    )
    segment_parser.add_argument("source", type=Path, help="UTF-8 文本文件；使用 - 读取标准输入")
    segment_parser.add_argument(
        "--max-chars",
        type=int,
        default=0,
        help="可选的长块字符上限；0 表示不按长度切分",
    )
    segment_parser.add_argument("--json", action="store_true")
    segment_parser.set_defaults(func=command_segment)

    locate_parser = subparsers.add_parser(
        "locate",
        help="在源文本中查找精确引文并返回行号",
    )
    locate_parser.add_argument("source", type=Path, help="UTF-8 文本文件；使用 - 读取标准输入")
    locate_parser.add_argument("--quote", required=True, help="需要精确定位的原文片段")
    locate_parser.add_argument("--json", action="store_true")
    locate_parser.set_defaults(func=command_locate)

    diagram_parser = subparsers.add_parser(
        "diagram",
        help="从 Markdown 报告生成 Mermaid 论证图或问题关系图",
    )
    diagram_parser.add_argument("report", type=Path)
    diagram_parser.add_argument(
        "--kind",
        choices=["argument", "issues", "compare"],
        default="argument",
    )
    diagram_parser.add_argument("--json", action="store_true")
    diagram_parser.set_defaults(func=command_diagram)

    dashboard_parser = subparsers.add_parser(
        "regression-dashboard",
        help="校验回归账本并生成误报看板",
    )
    dashboard_parser.add_argument("--check", action="store_true")
    dashboard_parser.set_defaults(func=command_regression_dashboard)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except CatalogParseError as exc:
        print(f"[ERROR] catalog-parse: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
