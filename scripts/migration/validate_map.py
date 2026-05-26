#!/usr/bin/env python3
"""Validate rename_map.tsv before any git mv: existence, uniqueness, frozen safety."""
import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAP = ROOT / "scripts/migration/rename_map.tsv"

rows = list(csv.DictReader(MAP.open(encoding="utf-8"), delimiter="\t"))
errors = []

# 1. every old_path exists
for r in rows:
    if not (ROOT / r["old_path"]).exists():
        errors.append(f"old_path missing: {r['old_path']}")

# 2. no two rows map to the same new_path
newc = Counter(r["new_path"] for r in rows)
for p, c in newc.items():
    if c > 1:
        errors.append(f"new_path collision ({c}x): {p}")

# 3. no new_path equals an existing unmoved file
moved = {r["old_path"] for r in rows}
for r in rows:
    np = r["new_path"]
    if (ROOT / np).exists() and np not in moved:
        errors.append(f"new_path already exists (unmoved): {np}")

# 4. report extensions in scope (catch unexpected non-md sweeps)
exts = Counter(Path(r["old_path"]).suffix for r in rows)

# 5. COLLISION flags remaining
coll = [r for r in rows if r["link_safe_basename"] != "yes"]

print(f"rows: {len(rows)}")
print(f"extensions moved: {dict(exts)}")
print(f"COLLISION-flagged rows: {len(coll)}")
for r in coll:
    print(f"  {r['old_path']} -> {r['new_path']}")
if errors:
    print(f"\nERRORS ({len(errors)}):")
    for e in errors[:50]:
        print("  " + e)
    sys.exit(1)
print("\nOK: map valid (all old exist, new unique, no clobber)")
