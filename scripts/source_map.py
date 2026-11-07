from __future__ import annotations

import bisect
import hashlib
import re
import sys
from dataclasses import dataclass
from pathlib import Path

BLOCK_BOUNDARY_PATTERN = re.compile(r"[。！？!?；;\n]|\.(?=\s)")


@dataclass(frozen=True)
class SourceLine:
    number: int
    char_start: int
    char_end: int
    text: str


@dataclass(frozen=True)
class SourceBlock:
    id: str
    line_start: int
    line_end: int
    char_start: int
    char_end: int
    text: str


@dataclass(frozen=True)
class QuoteMatch:
    quote: str
    line_start: int
    line_end: int
    char_start: int
    char_end: int


@dataclass(frozen=True)
class SourceDocument:
    path: str
    text: str
    sha256: str
    lines: tuple[SourceLine, ...]
    blocks: tuple[SourceBlock, ...]
    line_starts: tuple[int, ...]

    @property
    def line_count(self) -> int:
        return len(self.lines)

    @property
    def block_count(self) -> int:
        return len(self.blocks)

    @property
    def char_count(self) -> int:
        return len(self.text)


def normalize_source(text: str) -> str:
    if text.startswith("\ufeff"):
        text = text[1:]
    return text.replace("\r\n", "\n").replace("\r", "\n")


def read_source(path: Path) -> str:
    if str(path) == "-":
        return sys.stdin.read()
    return path.read_text(encoding="utf-8-sig")


def _line_number_for_offset(line_starts: tuple[int, ...], offset: int) -> int:
    if not line_starts:
        return 1
    offset = max(0, offset)
    return max(1, bisect.bisect_right(line_starts, offset))


def _build_lines(text: str) -> tuple[SourceLine, ...]:
    lines: list[SourceLine] = []
    offset = 0
    for number, raw_line in enumerate(text.splitlines(keepends=True), start=1):
        display = raw_line[:-1] if raw_line.endswith("\n") else raw_line
        lines.append(
            SourceLine(
                number=number,
                char_start=offset,
                char_end=offset + len(display),
                text=display,
            )
        )
        offset += len(raw_line)
    return tuple(lines)


def _line_groups(lines: tuple[SourceLine, ...]) -> list[tuple[int, int]]:
    groups: list[tuple[int, int]] = []
    current_start: int | None = None
    current_end = 0
    for line in lines:
        if line.text.strip():
            if current_start is None:
                current_start = line.number
            current_end = line.number
        elif current_start is not None:
            groups.append((current_start, current_end))
            current_start = None
    if current_start is not None:
        groups.append((current_start, current_end))
    return groups


def _split_ranges(text: str, max_chars: int) -> list[tuple[int, int]]:
    if max_chars <= 0 or len(text) <= max_chars:
        return [(0, len(text))]

    ranges: list[tuple[int, int]] = []
    start = 0
    while start < len(text):
        remaining = len(text) - start
        if remaining <= max_chars:
            ranges.append((start, len(text)))
            break

        limit = start + max_chars
        window = text[start:limit]
        boundaries = [match.end() + start for match in BLOCK_BOUNDARY_PATTERN.finditer(window)]
        split_at = boundaries[-1] if boundaries else limit
        if split_at <= start:
            split_at = limit
        ranges.append((start, split_at))
        start = split_at
    return ranges


def _trim_range(text: str, start: int, end: int) -> tuple[int, int] | None:
    while start < end and text[start].isspace():
        start += 1
    while end > start and text[end - 1].isspace():
        end -= 1
    return (start, end) if start < end else None


def _build_blocks(
    text: str,
    lines: tuple[SourceLine, ...],
    line_starts: tuple[int, ...],
    max_chars: int,
) -> tuple[SourceBlock, ...]:
    blocks: list[SourceBlock] = []
    for line_start, line_end in _line_groups(lines):
        block_start = lines[line_start - 1].char_start
        block_end = lines[line_end - 1].char_end
        block_text = text[block_start:block_end]
        for relative_start, relative_end in _split_ranges(block_text, max_chars):
            trimmed = _trim_range(
                block_text,
                relative_start,
                relative_end,
            )
            if trimmed is None:
                continue
            local_start, local_end = trimmed
            char_start = block_start + local_start
            char_end = block_start + local_end
            blocks.append(
                SourceBlock(
                    id=f"U{len(blocks) + 1}",
                    line_start=_line_number_for_offset(line_starts, char_start),
                    line_end=_line_number_for_offset(line_starts, max(char_start, char_end - 1)),
                    char_start=char_start,
                    char_end=char_end,
                    text=text[char_start:char_end],
                )
            )
    return tuple(blocks)


def build_source_document(
    text: str,
    *,
    path: str = "<input>",
    max_chars: int = 0,
) -> SourceDocument:
    normalized = normalize_source(text)
    lines = _build_lines(normalized)
    line_starts = tuple(line.char_start for line in lines)
    blocks = _build_blocks(normalized, lines, line_starts, max_chars)
    return SourceDocument(
        path=path,
        text=normalized,
        sha256=hashlib.sha256(normalized.encode("utf-8")).hexdigest(),
        lines=lines,
        blocks=blocks,
        line_starts=line_starts,
    )


def locate_quote(document: SourceDocument, quote: str) -> list[QuoteMatch]:
    normalized_quote = normalize_source(quote)
    if not normalized_quote:
        raise ValueError("quote must not be empty")

    matches: list[QuoteMatch] = []
    start = 0
    while True:
        index = document.text.find(normalized_quote, start)
        if index < 0:
            break
        end = index + len(normalized_quote)
        matches.append(
            QuoteMatch(
                quote=normalized_quote,
                line_start=_line_number_for_offset(document.line_starts, index),
                line_end=_line_number_for_offset(document.line_starts, max(index, end - 1)),
                char_start=index,
                char_end=end,
            )
        )
        start = index + 1
    return matches


def source_document_to_dict(document: SourceDocument) -> dict[str, object]:
    return {
        "path": document.path,
        "sha256": document.sha256,
        "line_count": document.line_count,
        "block_count": document.block_count,
        "char_count": document.char_count,
        "blocks": [
            {
                "id": block.id,
                "line_start": block.line_start,
                "line_end": block.line_end,
                "char_start": block.char_start,
                "char_end": block.char_end,
                "text": block.text,
            }
            for block in document.blocks
        ],
    }


def quote_matches_to_dict(matches: list[QuoteMatch]) -> list[dict[str, object]]:
    return [
        {
            "line_start": match.line_start,
            "line_end": match.line_end,
            "char_start": match.char_start,
            "char_end": match.char_end,
            "quote": match.quote,
        }
        for match in matches
    ]


def format_source_document(document: SourceDocument) -> str:
    lines = [
        f"来源：{document.path}",
        f"SHA-256：{document.sha256}",
        f"行数：{document.line_count}；字符数：{document.char_count}；候选块：{document.block_count}",
    ]
    for block in document.blocks:
        preview = " ".join(block.text.splitlines()).strip()
        if len(preview) > 100:
            preview = preview[:100] + "…"
        lines.append(
            f"{block.id} [L{block.line_start}-L{block.line_end}] "
            f"chars={block.char_end - block.char_start}：{preview}"
        )
    return "\n".join(lines)


def format_quote_matches(matches: list[QuoteMatch]) -> str:
    if not matches:
        return "未找到完全匹配的原文片段。"
    lines = [f"找到 {len(matches)} 处匹配："]
    for index, match in enumerate(matches, start=1):
        lines.append(
            f"{index}. [L{match.line_start}-L{match.line_end}] "
            f"chars={match.char_start}-{match.char_end}"
        )
        lines.append(f"> {match.quote}")
    return "\n".join(lines)
