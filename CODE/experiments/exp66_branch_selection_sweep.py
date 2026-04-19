#!/usr/bin/env python3
"""Exp66: lambda_rep branch-selection sweep for K=2 formations.

Uses exp65 formation tracking as the measurement primitive and aggregates a
branch-selection table over lambda_rep values.  This is experimental support for
R1 (K=2 branch-selection bifurcation); it does not by itself prove theorem
status changes.
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

from experiments.exp65_formation_tracking import DEFAULT_EPSILONS, parse_config, run_config


def safe_lambda_label(value: float) -> str:
    return str(value).replace('.', 'p').replace('-', 'm')


def main() -> None:
    parser = argparse.ArgumentParser(description='Exp66 branch-selection lambda_rep sweep')
    parser.add_argument('--configs', nargs='+', default=['20x20:0.6'])
    parser.add_argument('--lambda-reps', nargs='+', type=float,
                        default=[0.0, 0.005, 0.01, 0.02, 0.03, 0.04, 0.05, 0.075, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0])
    parser.add_argument('--epsilons', nargs='+', type=float, default=DEFAULT_EPSILONS)
    parser.add_argument('--lambda-bar', type=float, default=100.0)
    parser.add_argument('--n-restarts', type=int, default=3)
    parser.add_argument('--max-iter', type=int, default=1200)
    parser.add_argument('--output-json', type=Path, default=REPO_ROOT / 'experiments/results/exp66_branch_selection_sweep.json')
    parser.add_argument('--output-csv', type=Path, default=REPO_ROOT / 'experiments/results/exp66_branch_selection_sweep.csv')
    args = parser.parse_args()

    all_results = []
    summary_rows = []

    for cfg in args.configs:
        grid_size, c_ref = parse_config(cfg)
        for lam in args.lambda_reps:
            result = run_config(
                grid_size=grid_size,
                c_ref=c_ref,
                epsilons=args.epsilons,
                lambda_rep=lam,
                lambda_bar=args.lambda_bar,
                n_restarts=args.n_restarts,
                max_iter=args.max_iter,
                verbose=False,
            )
            all_results.append(result)
            s = result['summary']
            summary_rows.append({
                'config': result['config'],
                'grid_size': result['grid_size'],
                'c_ref': result['c_ref'],
                'lambda_rep': lam,
                'type_label': s['type_label'],
                'mean_center_offset_norm': s['mean_center_offset_norm'],
                'max_center_offset_norm': s['max_center_offset_norm'],
                'mean_separation': s['mean_separation'],
                'min_separation': s['min_separation'],
                'max_separation': s['max_separation'],
                'mean_soft_overlap': s['mean_soft_overlap'],
                'max_soft_overlap': s['max_soft_overlap'],
                'mean_lambda_coupling': s['mean_lambda_coupling'],
                'max_lambda_coupling': s['max_lambda_coupling'],
                'swap_count': s['swap_count'],
                'max_abs_delta_theta_mod_pi': s['max_abs_delta_theta_mod_pi'],
                'energy_asymmetry_pos_minus_neg': s['energy_asymmetry_pos_minus_neg'],
                'elapsed_s': s['elapsed_s'],
            })

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    with args.output_json.open('w', encoding='utf-8') as f:
        json.dump({'experiment': 'exp66_branch_selection_sweep', 'results': all_results, 'summary': summary_rows}, f, indent=2)

    with args.output_csv.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(summary_rows[0].keys()))
        writer.writeheader()
        writer.writerows(summary_rows)

    print(f'Saved JSON: {args.output_json}')
    print(f'Saved CSV:  {args.output_csv}')
    print('\nSummary rows:')
    for row in summary_rows:
        print(f"  {row['config']} lambda={row['lambda_rep']:>6g} {row['type_label']:<38} center={row['mean_center_offset_norm']:.3f} swaps={row['swap_count']} E_asym={row['energy_asymmetry_pos_minus_neg']:+.4f}")


if __name__ == '__main__':
    main()
