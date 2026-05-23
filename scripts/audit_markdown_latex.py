#!/usr/bin/env python3
"""Audit and repair Markdown + LaTeX safety issues in Perception_theory repo.

Conservative auto-fixes (A-class):
- \\big|, \\bigg|, \\Big|, \\Bigg| restrictions  -> \\big\\vert etc.
- \\|...\\| norms  -> \\lVert ... \\rVert
- |x| absolute value (short content)  -> \\lvert x \\rvert
- Set-builder {... | ...}  -> {... \\mid ...} (inside math)

All transformations apply ONLY inside math regions (inline $...$ or display $$...$$).
Code fences (``` / ~~~) and inline code (`...`) are skipped.

Hard-untouched files (canonical specs) are excluded.

Usage:
  python3 scripts/audit_markdown_latex.py            # scan only, write report
  python3 scripts/audit_markdown_latex.py --apply    # apply A-class + write report
  python3 scripts/audit_markdown_latex.py --include-logs   # include THEORY/logs/
"""
import argparse
import os
import re
import sys
from pathlib import Path

EXCLUDED_DIRS = {".git", "_archive", "node_modules", "venv", ".venv",
                 "__pycache__", "dist", "build", ".next", ".cache"}

EXCLUDED_FILE_PATTERNS = [
    re.compile(r"(?:^|/)THEORY/canonical/canonical\.md$"),
    re.compile(r"(?:^|/)THEORY/canonical/theorem_status\.md$"),
    re.compile(r"(?:^|/)THEORY/canonical/DECLARATION\.md$"),
    re.compile(r"(?:^|/)THEORY/canonical/hypothesis_tree\.md$"),
    re.compile(r"(?:^|/)THEORY/canonical/CV-.*_SEAL\.md$"),
    # SCC_CANONICAL/ holds sealed SCC-CT v0.1 canonical chapters
    re.compile(r"(?:^|/)SCC_CANONICAL/"),
    # Don't touch the audit report itself
    re.compile(r"(?:^|/)markdown_latex_audit_report\.md$"),
]

INCLUDED_EXTENSIONS = {".md", ".markdown", ".mdx"}

LOGS_PATTERN = re.compile(r"(?:^|/)THEORY/logs/")

# ---- Region detection ------------------------------------------------------

FENCE_OPEN = re.compile(r"^(\s*)(`{3,}|~{3,})")


def find_fenced_ranges(lines):
    """Line-based fenced code block ranges (inclusive)."""
    ranges = []
    in_fence = False
    fence_marker = None
    start = None
    for i, line in enumerate(lines):
        m = FENCE_OPEN.match(line)
        if not in_fence and m:
            in_fence = True
            fence_marker = m.group(2)[0] * 3  # ``` or ~~~
            start = i
        elif in_fence and line.lstrip().startswith(fence_marker):
            ranges.append((start, i))
            in_fence = False
            fence_marker = None
            start = None
    if in_fence:
        ranges.append((start, len(lines) - 1))
    return ranges


def in_ranges(line_no, ranges):
    return any(s <= line_no <= e for s, e in ranges)


def find_inline_code_spans(line):
    """Return list of (start, end) for inline code spans within a line."""
    spans = []
    pos = 0
    n = len(line)
    while pos < n:
        if line[pos] == '`':
            run_start = pos
            while pos < n and line[pos] == '`':
                pos += 1
            marker = line[run_start:pos]
            close_pos = line.find(marker, pos)
            if close_pos >= 0:
                end = close_pos + len(marker)
                spans.append((run_start, end))
                pos = end
            else:
                break
        else:
            pos += 1
    return spans


def find_inline_math_spans(line, code_spans):
    """Find $...$ math spans (not $$, not escaped \\$, not inside code)."""
    def in_code(p):
        return any(s <= p < e for s, e in code_spans)

    spans = []
    pos = 0
    n = len(line)
    while pos < n:
        ch = line[pos]
        if ch != '$':
            pos += 1
            continue
        # Escaped \$
        if pos > 0 and line[pos - 1] == '\\':
            pos += 1
            continue
        # Display $$  -> skip both
        if pos + 1 < n and line[pos + 1] == '$':
            pos += 2
            continue
        if in_code(pos):
            pos += 1
            continue
        # Look for matching closing $
        search = pos + 1
        found = -1
        while search < n:
            if line[search] == '$':
                prev_escape = (search > 0 and line[search - 1] == '\\')
                is_display = (search + 1 < n and line[search + 1] == '$')
                if not prev_escape and not is_display and not in_code(search):
                    found = search
                    break
            search += 1
        if found < 0:
            break
        spans.append((pos, found))
        pos = found + 1
    return spans


def find_display_math_ranges(lines, fenced):
    """Return line ranges (inclusive) for display $$...$$ blocks.

    Conservative: treat standalone $$ on its own line as toggle. Inline $$..$$
    on same line is treated separately.
    """
    ranges = []
    in_display = False
    start = None
    for i, line in enumerate(lines):
        if in_ranges(i, fenced):
            continue
        stripped = line.strip()
        # Standalone $$ delimiter
        if stripped == '$$':
            if in_display:
                ranges.append((start, i))
                in_display = False
                start = None
            else:
                in_display = True
                start = i
            continue
        # Same-line $$ ... $$: don't enter display state, but mark for processing
        if '$$' in line:
            # Count $$ occurrences
            count = line.count('$$')
            if count % 2 != 0:
                # Toggle display state
                if in_display:
                    ranges.append((start, i))
                    in_display = False
                    start = None
                else:
                    in_display = True
                    start = i
    if in_display:
        ranges.append((start, len(lines) - 1))
    return ranges


# ---- Transformations -------------------------------------------------------

def transform_math_content(s):
    """Apply A-class transforms to a math content string.

    Returns (new_s, n_changes).
    """
    original = s
    changes = 0

    # 1. Restriction bars: \big|, \bigg|, \Big|, \Bigg|
    s, c = re.subn(r"\\Bigg\|", r"\\Bigg\\vert", s); changes += c
    s, c = re.subn(r"\\bigg\|", r"\\bigg\\vert", s); changes += c
    s, c = re.subn(r"\\Big\|",  r"\\Big\\vert",  s); changes += c
    s, c = re.subn(r"\\big\|",  r"\\big\\vert",  s); changes += c

    # 2. Norm \|...\| -> \lVert ... \rVert  (non-greedy paired match)
    def norm_repl(m):
        return r"\lVert " + m.group(1).strip() + r" \rVert"
    s, c = re.subn(r"\\\|(.*?)\\\|", norm_repl, s); changes += c

    # 3. Set-builder: \{ X | Y \} -> \{ X \mid Y \}
    # Only within \{...\} groups (escaped braces, LaTeX set notation)
    def setbuilder_repl(m):
        inner = m.group(1)
        # Replace unescaped | with \mid
        # Be cautious: don't double-replace existing \mid
        new_inner = re.sub(r"(?<!\\)\|", r" \\mid ", inner)
        new_inner = re.sub(r"\s+", " ", new_inner).strip()
        return r"\{ " + new_inner + r" \}"
    # Match \{ ... | ... \} where '...' has no { or } or unescaped \{ \}
    s_new, c = re.subn(
        r"\\\{([^{}]*(?<!\\)\|[^{}]*)\\\}", setbuilder_repl, s)
    changes += c
    s = s_new

    # 4. Absolute value / cardinality: |X| -> \lvert X \rvert
    #    Conservative: content must be short (1..80 chars), no embedded |,
    #    no newlines, and not preceded by \ (which would indicate \| norm
    #    we already handled). Also not adjacent to word chars (avoids
    #    table separators in markdown - but inside math anyway).
    def abs_repl(m):
        inner = m.group(1).strip()
        return r"\lvert " + inner + r" \rvert"
    # Pattern: (not preceded by \) | (content without |) | (not followed by digit/letter context)
    s, c = re.subn(
        r"(?<![\\\w|])\|([^|\n\\]{1,80}?)\|(?![\w|])",
        abs_repl, s)
    changes += c

    # Cleanup multiple spaces (only within math; conservative)
    # Don't aggressively collapse - just collapse \vert + space artifacts
    s = re.sub(r"\\vert  +", r"\\vert ", s)
    s = re.sub(r"  +\\vert", r" \\vert", s)

    return s, (1 if s != original else 0)


# ---- File processing -------------------------------------------------------

CANONICAL_PATTERNS = [
    re.compile(r"(?:^|/)THEORY/canonical/canonical\.md$"),
    re.compile(r"(?:^|/)THEORY/canonical/theorem_status\.md$"),
    re.compile(r"(?:^|/)THEORY/canonical/DECLARATION\.md$"),
    re.compile(r"(?:^|/)THEORY/canonical/hypothesis_tree\.md$"),
    re.compile(r"(?:^|/)THEORY/canonical/CV-.*_SEAL\.md$"),
    re.compile(r"(?:^|/)SCC_CANONICAL/"),
]


def is_excluded(rel_path_str, include_logs=False, include_canonical=False):
    s = rel_path_str.replace("\\", "/")
    # Always-excluded patterns (audit report itself)
    if re.search(r"(?:^|/)markdown_latex_audit_report\.md$", s):
        return True
    # Canonical patterns - excluded unless --include-canonical
    if not include_canonical:
        for pat in CANONICAL_PATTERNS:
            if pat.search(s):
                return True
    # Other excluded patterns
    for pat in EXCLUDED_FILE_PATTERNS:
        if pat.search(s):
            # Skip if it's a canonical pattern and we're including canonical
            is_canonical = any(cp.search(s) for cp in CANONICAL_PATTERNS)
            if is_canonical and include_canonical:
                continue
            return True
    if not include_logs and LOGS_PATTERN.search(s):
        return True
    return False


def find_markdown_files(root, include_logs=False, include_canonical=False):
    root = Path(root)
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
        for name in filenames:
            if Path(name).suffix in INCLUDED_EXTENSIONS:
                fp = Path(dirpath) / name
                try:
                    rel = fp.relative_to(root)
                except ValueError:
                    continue
                if not is_excluded(str(rel), include_logs, include_canonical):
                    yield fp, rel


def audit_file(path, apply=False):
    try:
        content = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        return {'path': str(path), 'error': 'unicode_error',
                'a_count': 0, 'issues_b': [], 'issues_c': [], 'modified': False}

    original = content
    lines = content.split('\n')

    fenced = find_fenced_ranges(lines)
    display = find_display_math_ranges(lines, fenced)

    issues_b = []
    issues_c = []
    a_count = 0

    # B-class: heading with math (not in code fence)
    for i, line in enumerate(lines):
        if in_ranges(i, fenced):
            continue
        if re.match(r'^#+\s', line) and '$' in line:
            issues_b.append((i + 1, 'heading_with_math',
                             line.strip()[:80]))

    # B-class: link text contains math
    for i, line in enumerate(lines):
        if in_ranges(i, fenced):
            continue
        if re.search(r'\[\$[^\]]*\$[^\]]*\]\(', line):
            issues_b.append((i + 1, 'link_with_math', line.strip()[:80]))

    # C-class: unbalanced $ (count across non-fenced lines; minus \$ and $$)
    cleaned_content = []
    for i, line in enumerate(lines):
        if in_ranges(i, fenced):
            continue
        c = re.sub(r'\\\$', '', line)
        c = re.sub(r'\$\$', '', c)
        # Also strip inline code spans for accurate count
        code_spans = find_inline_code_spans(line)
        if code_spans:
            buf = []
            last = 0
            for s, e in code_spans:
                buf.append(c[last:s])
                last = e
            buf.append(c[last:])
            c = ''.join(buf)
        cleaned_content.append(c)
    dollar_count = sum(l.count('$') for l in cleaned_content)
    if dollar_count % 2 != 0:
        issues_c.append(('unbalanced_dollars', dollar_count))

    # Transform math content
    new_lines = []
    for i, line in enumerate(lines):
        if in_ranges(i, fenced):
            new_lines.append(line)
            continue

        in_disp = in_ranges(i, display)
        code_spans = find_inline_code_spans(line)

        if in_disp:
            # Lines inside display $$..$$. Don't transform delimiter lines.
            if line.strip() == '$$':
                new_lines.append(line)
                continue
            # Treat the entire line as math content (display block interior)
            transformed, _ = transform_math_content(line)
            if transformed != line:
                a_count += 1
            new_lines.append(transformed)
        else:
            spans = find_inline_math_spans(line, code_spans)
            if not spans:
                # Check for inline $$ ... $$ on same line (single line display)
                if '$$' in line:
                    # Look for $$ pairs on same line
                    def inline_disp_repl(m):
                        nonlocal a_count
                        inner = m.group(1)
                        new_inner, _ = transform_math_content(inner)
                        if new_inner != inner:
                            a_count += 1
                        return '$$' + new_inner + '$$'
                    line = re.sub(r'\$\$(.*?)\$\$', inline_disp_repl, line)
                new_lines.append(line)
            else:
                modified = line
                # Process right-to-left to preserve indices
                for start, end in reversed(spans):
                    math = modified[start:end + 1]
                    if not (math.startswith('$') and math.endswith('$')):
                        continue
                    inner = math[1:-1]
                    new_inner, _ = transform_math_content(inner)
                    if new_inner != inner:
                        a_count += 1
                        modified = (modified[:start] + '$' + new_inner +
                                    '$' + modified[end + 1:])
                # Also handle inline $$ on this line
                if '$$' in modified:
                    def inline_disp_repl(m):
                        nonlocal a_count
                        inner = m.group(1)
                        new_inner, _ = transform_math_content(inner)
                        if new_inner != inner:
                            a_count += 1
                        return '$$' + new_inner + '$$'
                    modified = re.sub(r'\$\$(.*?)\$\$', inline_disp_repl,
                                      modified)
                new_lines.append(modified)

    new_content = '\n'.join(new_lines)
    modified = (new_content != original)

    if apply and modified:
        path.write_text(new_content, encoding='utf-8')

    return {
        'path': str(path),
        'a_count': a_count,
        'issues_b': issues_b,
        'issues_c': issues_c,
        'modified': modified,
    }


# ---- Report ---------------------------------------------------------------

def write_report(results, args, report_path):
    total = len(results)
    modified = sum(1 for r in results if r.get('modified'))
    total_a = sum(r.get('a_count', 0) for r in results)
    total_b = sum(len(r.get('issues_b', [])) for r in results)
    total_c = sum(len(r.get('issues_c', [])) for r in results)
    errors = [r for r in results if r.get('error')]

    out = []
    out.append("# Markdown + LaTeX Audit Report")
    out.append("")
    out.append(f"Generated by `scripts/audit_markdown_latex.py` "
               f"(mode: **{'APPLY' if args.apply else 'SCAN-ONLY'}**)")
    out.append("")
    out.append("## §1 Summary")
    out.append("")
    out.append(f"- Files scanned: **{total}**")
    out.append(f"- Files modified (auto-fix applied): **{modified}**" if args.apply
               else f"- Files that would be modified: **{modified}**")
    out.append(f"- A-class transforms (auto-fix): **{total_a}**")
    out.append(f"- B-class issues (manual review): **{total_b}**")
    out.append(f"- C-class issues (report only): **{total_c}**")
    out.append(f"- Read errors: **{len(errors)}**")
    out.append("")
    out.append("**Excluded**: `_archive/`, `THEORY/canonical/canonical.md`, "
               "`theorem_status.md`, `DECLARATION.md`, `hypothesis_tree.md`, "
               "`CV-*_SEAL.md`, `markdown_latex_audit_report.md`.")
    if not args.include_logs:
        out.append("**Logs excluded** (default): `THEORY/logs/`. "
                   "Use `--include-logs` to scan.")
    out.append("")

    # Per-file changes
    out.append("## §2 Per-file changes (modified or flagged)")
    out.append("")
    any_change = False
    for r in results:
        if not (r.get('modified') or r.get('issues_b') or r.get('issues_c')
                or r.get('error')):
            continue
        any_change = True
        out.append(f"### `{r['path']}`")
        if r.get('error'):
            out.append(f"- ERROR: {r['error']}")
        if r.get('a_count'):
            verb = "applied" if args.apply else "would apply"
            out.append(f"- A-class auto-fixes {verb}: **{r['a_count']}**")
        for li, kind, snippet in r.get('issues_b', []):
            out.append(f"- B `L{li}` {kind}: `{snippet}`")
        for c in r.get('issues_c', []):
            out.append(f"- C {c[0]}: {c[1] if len(c) > 1 else ''}")
        out.append("")
    if not any_change:
        out.append("*(none)*")
        out.append("")

    # Manual review section
    out.append("## §3 Manual review queue")
    out.append("")
    out.append("B-class: math in heading/link (auto-rewrite skipped — context-sensitive).")
    out.append("C-class: unbalanced `$` (parser may be confused, requires human inspection).")
    out.append("")

    # Remaining risk
    out.append("## §4 Remaining risk")
    out.append("")
    out.append("- Markdown table cells with complex math: not transformed beyond A-class.")
    out.append("- Asterisk `*` multiplication inside math: NOT touched (ambiguous with convolution / adjoint).")
    out.append("- Math in headings: kept (anchor generation may differ across renderers).")
    out.append("- Renderer-specific behavior (GitHub Pages/Jekyll, MDX, Obsidian, KaTeX, MathJax) NOT verified by this script.")
    out.append("")

    # Style guide
    out.append("## §5 Recommended future writing rules")
    out.append("")
    out.append("- Use `$...$` for short inline math.")
    out.append("- Use `$$...$$` (own lines) for block math.")
    out.append("- In tables, NEVER use raw `|` inside math. Use `\\lvert x \\rvert`, `\\lVert x \\rVert`, `\\mid`, `\\vert`.")
    out.append("- Use backticks for filenames, paths, ROS topics, package names, shell variables.")
    out.append("- Avoid complex math in headings and links.")
    out.append("- Escape non-math dollar signs as `\\$`.")
    out.append("- Do not modify content inside fenced code blocks.")
    out.append("")

    out.append("---")
    out.append("")
    out.append("*End of report.*")

    Path(report_path).write_text('\n'.join(out), encoding='utf-8')


# ---- CLI ------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true',
                    help='Apply A-class auto-fixes (default: scan only)')
    ap.add_argument('--root', default='.',
                    help='Repo root (default: cwd)')
    ap.add_argument('--report', default='markdown_latex_audit_report.md',
                    help='Report output path (default: <root>/markdown_latex_audit_report.md)')
    ap.add_argument('--include-logs', action='store_true',
                    help='Include THEORY/logs/ in scan')
    ap.add_argument('--include-canonical', action='store_true',
                    help='Include THEORY/canonical/canonical.md, theorem_status.md, '
                         'DECLARATION.md, hypothesis_tree.md, CV-*_SEAL.md, SCC_CANONICAL/')
    args = ap.parse_args()

    root = Path(args.root).resolve()
    print(f"Root: {root}", file=sys.stderr)
    print(f"Mode: {'APPLY' if args.apply else 'SCAN-ONLY'}", file=sys.stderr)

    results = []
    for path, rel in find_markdown_files(
            root,
            include_logs=args.include_logs,
            include_canonical=args.include_canonical):
        r = audit_file(path, apply=args.apply)
        results.append(r)

    report_path = (Path(args.report) if Path(args.report).is_absolute()
                   else root / args.report)
    write_report(results, args, report_path)

    total = len(results)
    modified = sum(1 for r in results if r.get('modified'))
    total_a = sum(r.get('a_count', 0) for r in results)
    total_b = sum(len(r.get('issues_b', [])) for r in results)
    total_c = sum(len(r.get('issues_c', [])) for r in results)
    print(f"Scanned: {total}  Modified: {modified}  "
          f"A: {total_a}  B: {total_b}  C: {total_c}", file=sys.stderr)
    print(f"Report: {report_path}", file=sys.stderr)


if __name__ == '__main__':
    main()
