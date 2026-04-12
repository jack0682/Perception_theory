#!/usr/bin/env python3
"""Exp74: family-matched analysis on top of Exp73 branch catalogs.

Loads one or more Exp73 catalog JSON files, anchors at the best discovered
source-lambda=0 representative, and compares:

1. the first frozen crossing against any discovered representative;
2. the nearest matched-family representative using branch type + geometry +
   overlap jointly.

The purpose is to separate true branch-family continuation from catalog-wide
family switching.
"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import math
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def parse_side(config: str) -> int:
    side_s = config.split(':', 1)[0]
    return int(side_s.lower().split('x')[0]) if 'x' in side_s.lower() else int(side_s)


def metric_or_default(a: dict, b: dict, key: str, scale: float) -> float:
    if key not in a or key not in b:
        return 0.0
    return ((a[key] - b[key]) / scale) ** 2


def family_distance(a: dict, b: dict, side: int) -> float:
    n = side * side
    total = 0.0
    total += ((a['center_offset_norm'] - b['center_offset_norm']) / 0.03) ** 2
    total += ((a['overlap'] - b['overlap']) / 0.75) ** 2
    total += ((a['separation'] - b['separation']) / (0.15 * side)) ** 2
    total += metric_or_default(a, b, 'tau0p1_count_min', 0.05 * n)
    total += metric_or_default(a, b, 'tau0p1_count_max', 0.05 * n)
    total += metric_or_default(a, b, 'tau0p1_components_min', 2.0)
    total += metric_or_default(a, b, 'tau0p1_components_max', 2.0)
    total += metric_or_default(a, b, 'tau0p2_count_min', 0.05 * n)
    total += metric_or_default(a, b, 'tau0p2_count_max', 0.05 * n)
    total += metric_or_default(a, b, 'tau0p2_components_min', 2.0)
    total += metric_or_default(a, b, 'tau0p2_components_max', 2.0)
    total += metric_or_default(a, b, 'tau0p1_overlap_nodes', 0.03 * n)
    total += metric_or_default(a, b, 'tau0p2_overlap_nodes', 0.03 * n)
    return math.sqrt(total)


def threshold(a: dict, b: dict):
    denom = a['overlap'] - b['overlap']
    if denom <= 1e-12:
        return None
    return (b['E0'] - a['E0']) / denom


def summarize_catalog(data: dict, distance_threshold: float) -> dict:
    reps = sorted(data['representatives'], key=lambda r: r['E0'])
    side = parse_side(data['config'])
    zero_reps = [r for r in reps if abs(r['source_lambda']) < 1e-12]
    if not zero_reps:
        raise ValueError(f"No source-lambda=0 representative in {data['config']}")

    base = min(zero_reps, key=lambda r: r['E0'])

    global_cross = None
    global_rep = None
    for r in reps:
        if r is base:
            continue
        lam = threshold(base, r)
        if lam is None or lam < 0 or not math.isfinite(lam):
            continue
        if global_cross is None or lam < global_cross:
            global_cross = lam
            global_rep = r

    same_type = [r for r in reps if r is not base and r['source_lambda'] > 0 and r['branch_type'] == base['branch_type']]
    nearest_distance = None
    nearest_rep = None
    for r in same_type:
        d = family_distance(base, r, side)
        if nearest_distance is None or d < nearest_distance:
            nearest_distance = d
            nearest_rep = r

    matched_rep = None
    matched_cross = None
    if nearest_rep is not None and nearest_distance is not None and nearest_distance <= distance_threshold:
        matched_rep = nearest_rep
        matched_cross = threshold(base, matched_rep)
        if matched_cross is not None and (matched_cross < 0 or not math.isfinite(matched_cross)):
            matched_cross = None

    return {
        'config': data['config'],
        'n_representatives': len(reps),
        'base_key': base['key'],
        'base_branch_type': base['branch_type'],
        'base_source_lambda': base['source_lambda'],
        'base_E0': base['E0'],
        'base_overlap': base['overlap'],
        'global_cross': global_cross,
        'global_cross_key': None if global_rep is None else global_rep['key'],
        'global_cross_branch_type': None if global_rep is None else global_rep['branch_type'],
        'global_cross_source_lambda': None if global_rep is None else global_rep['source_lambda'],
        'global_cross_E0': None if global_rep is None else global_rep['E0'],
        'global_cross_overlap': None if global_rep is None else global_rep['overlap'],
        'matched_distance': nearest_distance,
        'matched_key': None if matched_rep is None else matched_rep['key'],
        'matched_branch_type': None if matched_rep is None else matched_rep['branch_type'],
        'matched_source_lambda': None if matched_rep is None else matched_rep['source_lambda'],
        'matched_E0': None if matched_rep is None else matched_rep['E0'],
        'matched_overlap': None if matched_rep is None else matched_rep['overlap'],
        'matched_cross': matched_cross,
        'matched_within_threshold': bool(matched_rep is not None),
        'distance_threshold': distance_threshold,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input-glob', default=str(REPO_ROOT / 'experiments/results/exp73_catalog_*.json'))
    ap.add_argument('--distance-threshold', type=float, default=2.5)
    ap.add_argument('--output-json', type=Path, default=REPO_ROOT / 'experiments/results/exp74_family_match_summary.json')
    ap.add_argument('--output-csv', type=Path, default=REPO_ROOT / 'experiments/results/exp74_family_match_summary.csv')
    args = ap.parse_args()

    rows = []
    for path in sorted(glob.glob(args.input_glob)):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        rows.append(summarize_catalog(data, distance_threshold=args.distance_threshold))

    out = {
        'experiment': 'exp74_branch_family_match',
        'input_glob': args.input_glob,
        'distance_threshold': args.distance_threshold,
        'rows': rows,
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(out, indent=2))
    with args.output_csv.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved JSON: {args.output_json}")
    print(f"Saved CSV: {args.output_csv}")
    for row in rows:
        print(
            f"{row['config']}: global_cross={row['global_cross']} matched_cross={row['matched_cross']} "
            f"matched_distance={row['matched_distance']} matched_key={row['matched_key']}"
        )


if __name__ == '__main__':
    main()
