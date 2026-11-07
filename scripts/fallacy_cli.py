from __future__ import annotations

import argparse
import json
import sys

from catalog_lib import (
    ROOT,
    CatalogParseError,
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
