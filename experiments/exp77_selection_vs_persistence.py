#!/usr/bin/env python3
"""Exp77: compare persistent continuation branch against discovered competitors.

Loads an Exp76 continuation run and an Exp73 catalog, then compares total energy
E_total(lambda) = E0 + lambda * overlap at matched lambda values.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def total_energy(row, lam: float) -> float:
    return float(row['E0'] + lam * row['overlap'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--continuation-json', type=Path, required=True)
    ap.add_argument('--catalog-json', type=Path, required=True)
    ap.add_argument('--output-json', type=Path, required=True)
    ap.add_argument('--output-csv', type=Path, required=True)
    args = ap.parse_args()

    cont = json.loads(args.continuation_json.read_text())
    cat = json.loads(args.catalog_json.read_text())
    reps = cat['representatives']

    rows = []
    for r in cont['rows']:
        lam = float(r['target_lambda'])
        cont_total = total_energy(r, lam)
        best_rep = min(reps, key=lambda c: total_energy(c, lam))
        best_total = total_energy(best_rep, lam)
        rows.append({
            'lambda': lam,
            'continuation_branch_type': r['branch_type'],
            'continuation_total': cont_total,
            'continuation_E0': r['E0'],
            'continuation_overlap': r['overlap'],
            'best_catalog_key': best_rep['key'],
            'best_catalog_branch_type': best_rep['branch_type'],
            'best_catalog_source_lambda': best_rep['source_lambda'],
            'best_catalog_total': best_total,
            'best_catalog_E0': best_rep['E0'],
            'best_catalog_overlap': best_rep['overlap'],
            'energy_gap_cont_minus_best': cont_total - best_total,
        })

    out = {
        'experiment': 'exp77_selection_vs_persistence',
        'continuation_json': str(args.continuation_json),
        'catalog_json': str(args.catalog_json),
        'rows': rows,
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(out, indent=2))
    with args.output_csv.open('w', newline='', encoding='utf-8') as f:
        fieldnames = list(rows[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f'Saved JSON: {args.output_json}')
    print(f'Saved CSV: {args.output_csv}')
    for row in rows:
        print(
            f"lambda={row['lambda']}: cont_total={row['continuation_total']:.6f} "
            f"best_total={row['best_catalog_total']:.6f} gap={row['energy_gap_cont_minus_best']:.6f} "
            f"best={row['best_catalog_key']}"
        )


if __name__ == '__main__':
    main()
