#!/usr/bin/env python3
"""Wikilink integrity verifier for the Perception_theory reorganization.

Parses every Obsidian-style [[wikilink]] in all *.md files (excluding .git) and
reports links that do not resolve to an existing file (dangling), plus basenames
that are ambiguous (same basename in >1 file -> by-basename resolution is unsafe).

Resolution model (matches Obsidian):
  - target containing '/'  -> try path relative to the linking file's dir, then
                              relative to the repo root (vault root).
  - bare basename          -> resolves iff that basename exists somewhere.
Code spans (fenced ``` / ~~~ and inline `...`) are skipped.

Usage:
  verify_links.py --write-baseline scripts/migration/baseline_report.json
  verify_links.py --baseline       scripts/migration/baseline_report.json   # gate: exit 1 on regression
  verify_links.py                                                            # just print current report
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # repo root (scripts/migration/ -> repo)
WIKILINK = re.compile(r'!?\[\[([^\]\|#]+)(?:#[^\]\|]+)?(?:\|[^\]]+)?\]\]')
INLINE_CODE = re.compile(r'`[^`\n]*`')


def all_md():
    return [p for p in ROOT.rglob("*.md") if "/.git/" not in str(p)]


def strip_code_and_find_links(text):
    """Yield link targets, skipping fenced blocks and inline code spans."""
    in_fence = False
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line_no_code = INLINE_CODE.sub("", line)
        for m in WIKILINK.finditer(line_no_code):
            yield m.group(1).strip()


def build_report():
    mds = all_md()
    by_basename = defaultdict(list)
    for p in mds:
        by_basename[p.stem].append(p)
    ambiguous = {
        b: sorted(str(x.relative_to(ROOT)) for x in v)
        for b, v in by_basename.items() if len(v) > 1
    }
    basenames = set(by_basename)

    def resolves(target, src):
        if "/" in target:
            rel = (src.parent / (target + ".md")).resolve()
            if rel.exists():
                return True
            vault = (ROOT / (target + ".md"))
            return vault.exists()
        return target in basenames

    dangling = []
    for p in mds:
        text = p.read_text(encoding="utf-8", errors="replace")
        for tgt in strip_code_and_find_links(text):
            if not resolves(tgt, p):
                dangling.append([str(p.relative_to(ROOT)), tgt])

    return {
        "file_count": len(mds),
        "dangling": sorted(dangling),
        "ambiguous_basenames": dict(sorted(ambiguous.items())),
        "dangling_count": len(dangling),
        "ambiguous_count": len(ambiguous),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline")
    ap.add_argument("--write-baseline")
    args = ap.parse_args()

    report = build_report()
    summary = (f"files={report['file_count']} "
               f"dangling={report['dangling_count']} "
               f"ambiguous={report['ambiguous_count']}")

    if args.write_baseline:
        Path(args.write_baseline).write_text(
            json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"[baseline written] {summary}")
        return 0

    if args.baseline:
        base = json.loads(Path(args.baseline).read_text(encoding="utf-8"))
        # Translate baseline source paths through the rename-map so a pre-existing
        # dangler whose SOURCE file merely moved is not falsely flagged as new.
        rmap = {}
        mp = ROOT / "scripts/migration/rename_map.tsv"
        if mp.exists():
            import csv as _csv
            for r in _csv.DictReader(mp.open(encoding="utf-8"), delimiter="\t"):
                rmap[r["old_path"]] = r["new_path"]
        base_dangling = {(rmap.get(src, src), tgt) for src, tgt in (tuple(x) for x in base["dangling"])}
        cur_dangling = {tuple(x) for x in report["dangling"]}
        new_dangling = sorted(cur_dangling - base_dangling)
        new_ambig = sorted(set(report["ambiguous_basenames"]) - set(base["ambiguous_basenames"]))
        print(summary)
        if new_dangling or new_ambig:
            print("REGRESSION vs baseline:", file=sys.stderr)
            for f, t in new_dangling:
                print(f"  new dangling: {f} -> [[{t}]]", file=sys.stderr)
            for b in new_ambig:
                print(f"  new ambiguous basename: {b} -> {report['ambiguous_basenames'][b]}", file=sys.stderr)
            return 1
        print("OK: no new dangling links or ambiguities vs baseline")
        return 0

    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
