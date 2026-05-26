#!/usr/bin/env python3
"""Phase 2: execute `git mv` for every row of rename_map.tsv (moves only, no edits)."""
import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAP = ROOT / "scripts/migration/rename_map.tsv"
APPLY = "--apply" in sys.argv

rows = list(csv.DictReader(MAP.open(encoding="utf-8"), delimiter="\t"))
fail = []
for r in rows:
    old, new = ROOT / r["old_path"], ROOT / r["new_path"]
    if not old.exists():
        fail.append(f"missing old: {r['old_path']}")
        continue
    if new.exists():
        fail.append(f"dest exists: {r['new_path']}")
        continue
    if APPLY:
        new.parent.mkdir(parents=True, exist_ok=True)
        res = subprocess.run(["git", "mv", r["old_path"], r["new_path"]],
                             cwd=ROOT, capture_output=True, text=True)
        if res.returncode != 0:
            fail.append(f"git mv failed {r['old_path']}: {res.stderr.strip()}")
    else:
        print(f"[DRY] {r['old_path']} -> {r['new_path']}")

print(f"\n{'APPLIED' if APPLY else 'DRY-RUN'} {len(rows)} moves; failures: {len(fail)}")
for f in fail[:50]:
    print("  " + f)
sys.exit(1 if fail else 0)
