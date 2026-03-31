"""Experiment 6: Multi-formation (K=2) on 20x20 grid.

Tests the K-field architecture from I9 with varying repulsion strengths.
Shows that two formations emerge in different spatial locations.
"""

import sys
import os
import time
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.multi import find_k_formations


def run_experiment():
    print("=" * 60)
    print("Experiment 6: K=2 Multi-Formation on 20x20 Grid")
    print("=" * 60)

    graph = GraphState.grid_2d(20, 20)
    params = ParameterRegistry(volume_fraction=0.25)
    n = graph.n  # 400

    lambda_reps = [1.0, 10.0, 100.0]
    regime_names = ["weak", "moderate", "strong"]

    all_results = {}

    for lam, regime in zip(lambda_reps, regime_names):
        print(f"\n{'─' * 50}")
        print(f"Regime: {regime} (lambda_rep = {lam})")
        print(f"{'─' * 50}")

        t0 = time.time()
        results = find_k_formations(
            graph, params, K=2,
            lambda_rep=lam,
            lambda_bar=100.0,
            m_per_formation=[0.25, 0.25],
            n_restarts=3,
            max_iter=2000,
            verbose=True,
        )
        elapsed = time.time() - t0

        all_results[regime] = results

        for k, r in enumerate(results):
            print(f"\n  Formation {k+1}:")
            print(f"    Energy: {r.energy:.6f}")
            print(f"    Diagnostics: {r.diagnostics}")
            print(f"    Mass: {np.sum(r.u):.2f} (target: {0.25 * n:.0f})")
            print(f"    Max u: {np.max(r.u):.4f}, Min u: {np.min(r.u):.4f}")

        # Spatial separation analysis
        u1, u2 = results[0].u, results[1].u
        overlap = float(u1 @ u2)
        # Center of mass (for grid)
        coords = np.array([(i // 20, i % 20) for i in range(n)])
        com1 = np.average(coords, axis=0, weights=u1 + 1e-12)
        com2 = np.average(coords, axis=0, weights=u2 + 1e-12)
        com_dist = np.linalg.norm(com1 - com2)

        print(f"\n  Interaction metrics:")
        print(f"    Overlap (u1 . u2): {overlap:.4f}")
        print(f"    Center-of-mass distance: {com_dist:.2f}")
        print(f"    CoM1: ({com1[0]:.1f}, {com1[1]:.1f})")
        print(f"    CoM2: ({com2[0]:.1f}, {com2[1]:.1f})")
        print(f"    Time: {elapsed:.2f}s")

    # Save text heatmap for strong regime
    print(f"\n{'=' * 60}")
    print("Spatial Layout (strong regime, 20x20 grid)")
    print("1 = formation 1 dominant, 2 = formation 2 dominant, . = low")
    print("=" * 60)
    u1 = all_results["strong"][0].u
    u2 = all_results["strong"][1].u
    for r in range(20):
        row = ""
        for c in range(20):
            idx = r * 20 + c
            if u1[idx] > 0.5:
                row += "1"
            elif u2[idx] > 0.5:
                row += "2"
            elif u1[idx] > 0.2:
                row += "+"
            elif u2[idx] > 0.2:
                row += "x"
            else:
                row += "."
            row += " "
        print(row)

    return all_results


if __name__ == "__main__":
    results = run_experiment()
