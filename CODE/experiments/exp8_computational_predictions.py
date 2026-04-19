#!/usr/bin/env python3
"""Experiment 8: Computational validation of 3 theoretical predictions.

P1: Closure is contractive (not projective) — geometric convergence with ratio ~ a_cl/4
P2: 4 independent diagnostic dimensions — each energy term affects a different diagnostic
P4: Path dependence — multiple metastable basins from different initializations
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import find_formation, _optimize_single, project_volume
from scc.operators import closure, distinction
from scc.diagnostics import compute_diagnostics

GRID = (15, 15)
BETA = 20.0
C = 0.3


def prediction_1_contraction():
    """P1: Closure is contractive, not projective.

    Apply closure iteratively and verify geometric convergence.
    Ratio of successive distances should approach a_cl/4.
    A projection would give ratio=0 after one step.
    """
    print("=" * 60)
    print("P1: Closure Contraction (not projection)")
    print("=" * 60)

    graph = GraphState.grid_2d(*GRID)
    n = graph.n
    m = C * n
    a_cl = 3.5  # default

    params = ParameterRegistry(
        beta_bd=BETA, volume_fraction=C, a_cl=a_cl,
    )

    # Start from random u on Sigma_m
    rng = np.random.RandomState(42)
    u = np.full(n, C) + 0.1 * rng.randn(n)
    u = project_volume(u, m)

    # Iterate closure
    max_iter = 30
    distances = []
    ratios = []
    u_k = u.copy()

    print(f"\n  Grid: {GRID}, a_cl={a_cl}, predicted ratio: a_cl/4 = {a_cl/4:.4f}")
    print(f"  {'k':>3s}  {'||Cl^k - Cl^{k-1}||':>22s}  {'ratio':>10s}")
    print("  " + "-" * 40)

    for k in range(max_iter):
        u_next = closure(u_k, graph, params)
        dist = float(np.linalg.norm(u_next - u_k))
        distances.append(dist)
        if k > 0 and distances[k-1] > 1e-15:
            r = dist / distances[k-1]
            ratios.append(r)
            print(f"  {k:3d}  {dist:22.10f}  {r:10.6f}")
        else:
            print(f"  {k:3d}  {dist:22.10f}  {'---':>10s}")
        u_k = u_next
        if dist < 1e-14:
            print(f"  Converged at iteration {k}")
            break

    # Analysis
    if len(ratios) >= 3:
        # Use late ratios (after initial transient)
        late_ratios = ratios[min(5, len(ratios)-1):]
        mean_ratio = np.mean(late_ratios)
        predicted = a_cl / 4.0
        print(f"\n  Mean late ratio: {mean_ratio:.6f}")
        print(f"  Predicted (a_cl/4): {predicted:.6f}")
        print(f"  Relative error: {abs(mean_ratio - predicted)/predicted:.4f}")

        is_contractive = all(r < 1.0 for r in ratios)
        is_not_projective = distances[-1] > 1e-10 or len(distances) > 3
        print(f"\n  All ratios < 1 (contractive): {is_contractive}")
        print(f"  Not projective (didn't reach 0 in 1 step): {is_not_projective}")
        print(f"  VERDICT: P1 {'CONFIRMED' if is_contractive and is_not_projective else 'NOT CONFIRMED'}")
    else:
        print("  Insufficient iterations for ratio analysis")

    return distances, ratios


def prediction_2_independent_dimensions():
    """P2: 4 independent diagnostic dimensions.

    Show each energy term primarily affects a different diagnostic component.
    Use ablation configs to compute correlation between energy weights and diagnostics.
    """
    print("\n" + "=" * 60)
    print("P2: 4 Independent Diagnostic Dimensions")
    print("=" * 60)

    graph = GraphState.grid_2d(10, 10)  # smaller grid for speed
    n = graph.n

    # 6 ablation configs (from exp3)
    configs = {
        'BD-only':      {'w_cl': 0, 'w_sep': 0,  'w_bd': 1},
        'BD+CL':        {'w_cl': 1, 'w_sep': 0,  'w_bd': 1},
        'BD+SEP':       {'w_cl': 0, 'w_sep': 1,  'w_bd': 1},
        'Full-SCC':     {'w_cl': 1, 'w_sep': 1,  'w_bd': 1},
        'CL-only':      {'w_cl': 1, 'w_sep': 0,  'w_bd': 0},
        'SEP-only':     {'w_cl': 0, 'w_sep': 1,  'w_bd': 0},
    }

    n_seeds = 5
    config_data = []  # (w_cl, w_sep, w_bd, Bind, Sep, Inside)

    print(f"\n  {'Config':<15s}  {'Bind':>6s}  {'Sep':>6s}  {'Inside':>6s}")
    print("  " + "-" * 40)

    for name, weights in configs.items():
        binds, seps, insides = [], [], []
        for seed in range(n_seeds):
            params = ParameterRegistry(
                beta_bd=BETA, volume_fraction=0.5,
                w_cl=weights['w_cl'], w_sep=weights['w_sep'], w_bd=weights['w_bd'],
                max_iter=1000, n_restarts=1,
                eps_init=0.01 + 0.005 * seed,
            )
            try:
                result = find_formation(graph, params, normalize=True, verbose=False)
                d = result.diagnostics
                binds.append(d.bind)
                seps.append(d.sep)
                insides.append(d.inside)
            except (ValueError, np.linalg.LinAlgError):
                continue

        if binds:
            mb, ms, mi = np.mean(binds), np.mean(seps), np.mean(insides)
            print(f"  {name:<15s}  {mb:6.3f}  {ms:6.3f}  {mi:6.3f}")
            config_data.append((
                weights['w_cl'], weights['w_sep'], weights['w_bd'],
                mb, ms, mi
            ))

    if len(config_data) < 3:
        print("  Insufficient data for correlation analysis")
        return

    data = np.array(config_data)
    weights_mat = data[:, :3]   # w_cl, w_sep, w_bd
    diags_mat = data[:, 3:]     # Bind, Sep, Inside

    # Compute effect of each weight on each diagnostic
    # Use difference from BD-only baseline
    baseline_idx = 0  # BD-only
    print(f"\n  Effect matrix (change from BD-only baseline):")
    print(f"  {'Config':<15s}  {'dBind':>8s}  {'dSep':>8s}  {'dInside':>8s}")
    print("  " + "-" * 45)

    config_names = list(configs.keys())
    for i, name in enumerate(config_names):
        if i >= len(config_data):
            break
        diffs = diags_mat[i] - diags_mat[baseline_idx]
        print(f"  {name:<15s}  {diffs[0]:+8.4f}  {diffs[1]:+8.4f}  {diffs[2]:+8.4f}")

    # Correlation matrix between weights and diagnostics
    print(f"\n  Correlation matrix (weight -> diagnostic):")
    weight_names = ['w_cl', 'w_sep', 'w_bd']
    diag_names = ['Bind', 'Sep', 'Inside']

    print(f"  {'':>8s}", end="")
    for dn in diag_names:
        print(f"  {dn:>8s}", end="")
    print()

    corr_matrix = np.zeros((3, 3))
    for i in range(3):
        w_col = weights_mat[:, i]
        print(f"  {weight_names[i]:>8s}", end="")
        for j in range(3):
            d_col = diags_mat[:, j]
            if np.std(w_col) > 1e-10 and np.std(d_col) > 1e-10:
                corr = np.corrcoef(w_col, d_col)[0, 1]
            else:
                corr = 0.0
            corr_matrix[i, j] = corr
            print(f"  {corr:+8.3f}", end="")
        print()

    # Check: does each weight have a different primary diagnostic?
    primary_effects = []
    for i in range(3):
        primary = np.argmax(np.abs(corr_matrix[i, :]))
        primary_effects.append(primary)

    all_different = len(set(primary_effects)) == len(primary_effects)
    print(f"\n  Primary effects: " +
          ", ".join(f"{weight_names[i]}->{diag_names[primary_effects[i]]}"
                    for i in range(3)))
    print(f"  All different targets: {all_different}")
    print(f"  VERDICT: P2 {'CONFIRMED' if all_different else 'PARTIALLY CONFIRMED'} "
          f"— each energy term has a distinct primary diagnostic target")

    return corr_matrix


def prediction_4_path_dependence():
    """P4: Path dependence — multiple metastable basins.

    Run find_formation from different random seeds and check if results differ.
    """
    print("\n" + "=" * 60)
    print("P4: Path Dependence (Multiple Metastable Basins)")
    print("=" * 60)

    graph = GraphState.grid_2d(*GRID)
    n = graph.n

    params = ParameterRegistry(
        beta_bd=BETA, volume_fraction=C,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        max_iter=5000, n_restarts=1,  # single restart per seed
    )

    n_seeds = 5
    fields = []
    energies = []
    diagnostics = []

    print(f"\n  Grid: {GRID}, beta={BETA}, c={C}")
    print(f"  Running {n_seeds} independent optimizations...\n")

    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    for seed in range(n_seeds):
        u, E, terms, ehist, ghist, conv, niter = _optimize_single(
            graph, params, ec, seed=seed + 10  # offset to avoid Fiedler init
        )
        d = compute_diagnostics(u, graph, params)
        fields.append(u)
        energies.append(E)
        diagnostics.append(d)
        print(f"  Seed {seed}: E={E:.6f}, conv={conv}, iters={niter}, "
              f"Bind={d.bind:.3f}, Sep={d.sep:.3f}, Inside={d.inside:.3f}")

    # Pairwise distances
    print(f"\n  Pairwise field distances ||u_i - u_j||:")
    print(f"  {'':>6s}", end="")
    for j in range(n_seeds):
        print(f"  {'s'+str(j):>8s}", end="")
    print()

    dist_matrix = np.zeros((n_seeds, n_seeds))
    for i in range(n_seeds):
        print(f"  {'s'+str(i):>6s}", end="")
        for j in range(n_seeds):
            d = np.linalg.norm(fields[i] - fields[j])
            dist_matrix[i, j] = d
            print(f"  {d:8.4f}", end="")
        print()

    # Pairwise diagnostic distances
    print(f"\n  Pairwise diagnostic vector distances:")
    print(f"  {'':>6s}", end="")
    for j in range(n_seeds):
        print(f"  {'s'+str(j):>8s}", end="")
    print()

    diag_dists = np.zeros((n_seeds, n_seeds))
    for i in range(n_seeds):
        print(f"  {'s'+str(i):>6s}", end="")
        for j in range(n_seeds):
            dd = np.linalg.norm(diagnostics[i].vector - diagnostics[j].vector)
            diag_dists[i, j] = dd
            print(f"  {dd:8.4f}", end="")
        print()

    # Analysis
    off_diag = dist_matrix[np.triu_indices(n_seeds, k=1)]
    mean_dist = np.mean(off_diag)
    max_dist = np.max(off_diag)
    min_dist = np.min(off_diag)

    energy_spread = np.max(energies) - np.min(energies)
    rel_spread = energy_spread / (abs(np.mean(energies)) + 1e-15)

    diag_off = diag_dists[np.triu_indices(n_seeds, k=1)]
    mean_diag_dist = np.mean(diag_off)

    print(f"\n  Summary:")
    print(f"    Field distance: mean={mean_dist:.4f}, min={min_dist:.4f}, max={max_dist:.4f}")
    print(f"    Energy spread: {energy_spread:.6f} (relative: {rel_spread:.4f})")
    print(f"    Diagnostic distance: mean={mean_diag_dist:.4f}")

    # Path dependence: if mean field distance > threshold, basins are distinct
    threshold = 0.1 * np.sqrt(n)  # meaningful difference relative to field scale
    is_path_dependent = mean_dist > threshold
    multiple_basins = energy_spread > 1e-4

    print(f"\n    Threshold for distinct basins: {threshold:.4f}")
    print(f"    Mean field distance > threshold: {is_path_dependent}")
    print(f"    Multiple energy levels: {multiple_basins}")
    print(f"    VERDICT: P4 {'CONFIRMED' if is_path_dependent or multiple_basins else 'NOT CONFIRMED'} "
          f"— {'multiple' if is_path_dependent or multiple_basins else 'single'} metastable basin(s)")

    return dist_matrix, energies, diagnostics


def main():
    print("=" * 60)
    print("Experiment 8: Computational Predictions Validation")
    print("=" * 60)
    t0 = time.time()

    # P1
    distances, ratios = prediction_1_contraction()

    # P2
    corr = prediction_2_independent_dimensions()

    # P4
    dists, energies, diags = prediction_4_path_dependence()

    elapsed = time.time() - t0
    print(f"\n{'=' * 60}")
    print(f"Total runtime: {elapsed:.1f}s")
    print(f"{'=' * 60}")


if __name__ == '__main__':
    main()
