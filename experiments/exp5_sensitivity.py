#!/usr/bin/env python3
"""Experiment 5: Parameter sensitivity analysis.

For each parameter, sweep across a range while holding all others at baseline.
Measures formation quality (diagnostic vector) to assess robustness.
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation

GRID = (15, 15)
N_RESTARTS = 2
MAX_ITER = 1000

# Parameter sweeps: (param_name, values)
SWEEPS = [
    ("a_cl",            [1.0, 2.0, 3.0, 3.5, 3.9]),
    ("eta_cl",          [0.1, 0.3, 0.5, 0.7, 0.9]),
    ("tau_cl",          [0.3, 0.4, 0.5, 0.6, 0.7]),
    ("a_D",             [2.0, 3.0, 5.0, 8.0, 12.0]),
    ("w_cl",            [0.0, 0.5, 1.0, 2.0, 5.0]),
    ("w_sep",           [0.0, 0.5, 1.0, 2.0, 5.0]),
    ("w_bd",            [0.5, 1.0, 2.0, 5.0, 10.0]),
    ("beta_bd",         [5.0, 10.0, 20.0, 50.0, 100.0]),
    ("volume_fraction", [0.25, 0.35, 0.5, 0.65, 0.75]),
]


def run_sweep(graph, param_name, values):
    """Sweep one parameter, return list of result dicts."""
    results = []
    for val in values:
        kwargs = {
            param_name: val,
            "max_iter": MAX_ITER,
            "n_restarts": N_RESTARTS,
        }
        params = ParameterRegistry(**kwargs)
        t0 = time.time()
        res = find_formation(graph, params)
        elapsed = time.time() - t0
        d = res.diagnostics
        results.append({
            "param": param_name,
            "value": val,
            "bind": d.bind,
            "sep": d.sep,
            "inside": d.inside,
            "persist": d.persist,
            "min_diag": d.min_score,
            "mean_diag": d.mean_score,
            "energy": res.energy,
            "converged": res.converged,
            "n_iter": res.n_iter,
            "time": elapsed,
        })
    return results


def main():
    print(f"=== Experiment 5: Parameter Sensitivity ===")
    print(f"Grid: {GRID[0]}x{GRID[1]}, restarts={N_RESTARTS}, max_iter={MAX_ITER}")
    print()

    graph = GraphState.grid_2d(*GRID)

    # Print baseline
    baseline = ParameterRegistry(max_iter=MAX_ITER, n_restarts=N_RESTARTS)
    res_base = find_formation(graph, baseline)
    d = res_base.diagnostics
    print(f"BASELINE: Bind={d.bind:.3f} Sep={d.sep:.3f} Inside={d.inside:.3f} "
          f"min_diag={d.min_score:.3f} converged={res_base.converged}")
    print()

    all_results = []

    for param_name, values in SWEEPS:
        print(f"--- Sweeping {param_name} ---")
        results = run_sweep(graph, param_name, values)
        all_results.extend(results)

        for r in results:
            tag = " *" if not r["converged"] else ""
            print(f"  {param_name}={r['value']:<8} "
                  f"Bind={r['bind']:.3f} Sep={r['sep']:.3f} "
                  f"Inside={r['inside']:.3f} min={r['min_diag']:.3f} "
                  f"E={r['energy']:.4f} iter={r['n_iter']}{tag}")

        mins = [r["min_diag"] for r in results]
        print(f"  => min_diag range: [{min(mins):.3f}, {max(mins):.3f}], "
              f"mean={np.mean(mins):.3f}")
        print()

    # Summary table
    print("=" * 70)
    print("SUMMARY: min_diag statistics per parameter sweep")
    print(f"{'Parameter':<20} {'Min':>8} {'Max':>8} {'Mean':>8} {'All>0.7?':>10}")
    print("-" * 70)

    for param_name, values in SWEEPS:
        param_results = [r for r in all_results if r["param"] == param_name]
        mins = [r["min_diag"] for r in param_results]
        robust = "YES" if all(m > 0.7 for m in mins) else "NO"
        print(f"{param_name:<20} {min(mins):>8.3f} {max(mins):>8.3f} "
              f"{np.mean(mins):>8.3f} {robust:>10}")

    print("-" * 70)

    # Overall
    all_mins = [r["min_diag"] for r in all_results]
    n_pass = sum(1 for m in all_mins if m > 0.7)
    print(f"\nOverall: {n_pass}/{len(all_mins)} configurations have min_diag > 0.7")
    print(f"Global min_diag: {min(all_mins):.3f}, Global max: {max(all_mins):.3f}, "
          f"Mean: {np.mean(all_mins):.3f}")

    return all_results


if __name__ == "__main__":
    all_results = main()
