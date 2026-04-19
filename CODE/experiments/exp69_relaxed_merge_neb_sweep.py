#!/usr/bin/env python3
"""Exp69: aggregate exp68 relaxed merge NEB-lite sweeps.

Runs exp68 over config/lambda grids and writes summary CSV/JSON.  This is a
numerical scaffold for communication-height proxy statistics, not theorem
evidence by itself.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from experiments.exp68_relaxed_merge_neb import run


def safe_label(value: str) -> str:
    return value.replace(':', '_c').replace('.', 'p').replace('-', 'm')


def summarize(result: dict) -> dict:
    d = result['diagnostics']
    return {
        'config': result['config'],
        'lambda_rep': result['lambda_rep'],
        'lambda_bar': result['lambda_bar'],
        'n_images': result['n_images'],
        'n_iter': result['n_iter'],
        'step': result['step'],
        'spring': result['spring'],
        'source_energy': result['source_energy'],
        'initial_max_delta': result['initial']['max_delta'],
        'relaxed_max_delta': result['relaxed']['max_delta'],
        'initial_source_overlap': result['initial'].get('source_overlap', 0.0),
        'initial_max_overlap': result['initial'].get('max_overlap', 0.0),
        'initial_max_overlap_excess': result['initial'].get('max_overlap_excess', 0.0),
        'relaxed_source_overlap': result['relaxed'].get('source_overlap', 0.0),
        'relaxed_max_overlap': result['relaxed'].get('max_overlap', 0.0),
        'relaxed_max_overlap_excess': result['relaxed'].get('max_overlap_excess', 0.0),
        'improvement': d['improvement'],
        'improvement_frac': d['improvement'] / result['initial']['max_delta'] if result['initial']['max_delta'] else 0.0,
        'initial_max_index': result['initial']['max_index'],
        'relaxed_max_index': result['relaxed']['max_index'],
        'max_mass_error': d['relaxed_constraints']['max_total_mass_error'],
        'max_simplex_violation': d['relaxed_constraints']['max_simplex_violation'],
        'max_box_low_violation': d['relaxed_constraints']['max_box_low_violation'],
        'max_box_high_violation': d['relaxed_constraints']['max_box_high_violation'],
        'history_monotone': d['history']['monotone_nonincreasing'],
        'history_max_increase': d['history']['max_increase'],
    }


def main():
    ap = argparse.ArgumentParser(description='Exp69 relaxed merge NEB-lite sweep')
    ap.add_argument('--configs', nargs='+', default=['10x10:0.5', '10x10:0.6', '12x12:0.6'])
    ap.add_argument('--lambda-reps', nargs='+', type=float, default=[1.0])
    ap.add_argument('--lambda-bar', type=float, default=100.0)
    ap.add_argument('--n-images', type=int, default=9)
    ap.add_argument('--n-iter', type=int, default=50)
    ap.add_argument('--step', type=float, default=0.001)
    ap.add_argument('--spring', type=float, default=0.05)
    ap.add_argument('--n-restarts', type=int, default=1)
    ap.add_argument('--max-iter', type=int, default=300)
    ap.add_argument('--output-json', type=Path, default=REPO_ROOT / 'experiments/results/exp69_relaxed_merge_neb_sweep.json')
    ap.add_argument('--output-csv', type=Path, default=REPO_ROOT / 'experiments/results/exp69_relaxed_merge_neb_sweep.csv')
    args = ap.parse_args()

    results = []
    rows = []
    for cfg in args.configs:
        for lrep in args.lambda_reps:
            result = run(cfg, lrep, args.lambda_bar, args.n_images, args.n_iter, args.step, args.spring, args.n_restarts, args.max_iter)
            results.append(result)
            rows.append(summarize(result))
            print(f"{cfg} lambda={lrep:g}: initial={rows[-1]['initial_max_delta']:.6f} relaxed={rows[-1]['relaxed_max_delta']:.6f} improvement={rows[-1]['improvement']:.6f}")

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps({'experiment': 'exp69_relaxed_merge_neb_sweep', 'results': results, 'summary': rows}, indent=2))
    with args.output_csv.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved JSON: {args.output_json}")
    print(f"Saved CSV:  {args.output_csv}")


if __name__ == '__main__':
    main()
