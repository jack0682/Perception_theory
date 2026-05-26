#!/usr/bin/env python3
"""Phase 3: rewrite Obsidian wikilinks + inline file-path references per rename_map.tsv.

Correctness rules:
  * A bare-basename wikilink [[X]] is globally rewritten X->Y ONLY when X was
    *unambiguous in the OLD tree* (exactly one file had that basename). Ambiguous
    basenames (plan, README, 00_index, ...) are never globally rewritten.
  * A path-bearing wikilink [[a/b/c]] is normalized to its bare (possibly renamed)
    basename when that basename is unique in the NEW tree (this also repairs the
    pre-existing off-by-one relative links). If not unique, it is left unchanged.
  * Inline file-path references (THEORY/.../*.md) are replaced old->new, longest-first.
  * Wikilinks inside fenced code blocks are left untouched; inline-code spans are
    skipped for wikilink rewriting. Inline path strings are replaced everywhere.

Idempotent: a second run makes no changes. DRY-RUN unless --apply.
"""
import csv
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAP = ROOT / "scripts/migration/rename_map.tsv"
APPLY = "--apply" in sys.argv

rows = list(csv.DictReader(MAP.open(encoding="utf-8"), delimiter="\t"))

# --- old-tree basename multiplicity (from the premigration-baseline tag) ---
old_tree = subprocess.run(
    ["git", "ls-tree", "-r", "--name-only", "premigration-baseline"],
    cwd=ROOT, capture_output=True, text=True).stdout.splitlines()
old_md = [p for p in old_tree if p.endswith(".md")]
old_bn_count = Counter(Path(p).stem for p in old_md)

# --- new-tree basename multiplicity (current working tree) ---
new_md = [str(p.relative_to(ROOT)) for p in ROOT.rglob("*.md") if "/.git/" not in str(p)]
new_bn_count = Counter(Path(p).stem for p in new_md)

# basename rewrite: only for old-unambiguous renamed files
renamed_basename = {
    r["old_basename"]: r["new_basename"]
    for r in rows
    if r["old_basename"] != r["new_basename"] and old_bn_count[r["old_basename"]] == 1
}

# inline path pairs (with extension), longest old first
path_pairs = sorted(
    ((r["old_path"], r["new_path"]) for r in rows if r["old_path"] != r["new_path"]),
    key=lambda p: -len(p[0]))

WIKILINK = re.compile(r'(!?)\[\[([^\]\|#]+)((?:#[^\]\|]+)?)(\|[^\]]+)?\]\]')
INLINE_CODE = re.compile(r'`[^`\n]*`')


def rewrite_wikilink(m):
    bang, target, heading, disp = m.groups()
    heading, disp = heading or "", disp or ""
    t = target.strip()
    base = t.rsplit("/", 1)[-1]
    base_new = renamed_basename.get(base, base)
    if "/" in t:
        # path-bearing: normalize to bare basename iff unique in new tree
        if new_bn_count.get(base_new, 0) == 1:
            newt = base_new
        else:
            newt = t  # ambiguous -> leave unchanged
    else:
        newt = base_new
    if newt == target:
        return m.group(0)
    return f'{bang}[[{newt}{heading}{disp}]]'


def rewrite_wikilinks_in_prose(text):
    """Apply wikilink rewriting outside fenced code; skip inline-code spans."""
    out, in_fence = [], False
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        # protect inline code spans
        parts, last = [], 0
        for cm in INLINE_CODE.finditer(line):
            parts.append(WIKILINK.sub(rewrite_wikilink, line[last:cm.start()]))
            parts.append(cm.group(0))
            last = cm.end()
        parts.append(WIKILINK.sub(rewrite_wikilink, line[last:]))
        out.append("".join(parts))
    return "".join(out)


def rewrite_inline_paths(text):
    for old, new in path_pairs:
        if old in text:
            text = text.replace(old, new)
    return text


def main():
    changed = 0
    for md in ROOT.rglob("*.md"):
        if "/.git/" in str(md):
            continue
        src = md.read_text(encoding="utf-8")
        dst = rewrite_inline_paths(rewrite_wikilinks_in_prose(src))
        if dst != src:
            changed += 1
            print(f"[{'WRITE' if APPLY else 'DRY'}] {md.relative_to(ROOT)}")
            if APPLY:
                md.write_text(dst, encoding="utf-8")
    print(f"\n{changed} files {'changed' if APPLY else 'would change'}.")
    print(f"renamed-basename rules: {len(renamed_basename)} | path pairs: {len(path_pairs)}")


if __name__ == "__main__":
    main()
