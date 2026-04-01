#!/usr/bin/env python3
"""Experiment 39: Formation birth/split dynamics.

Studies how and when a single formation divides into two — the reverse of
the merge process studied in exp30. Three scenarios:

  1. Volume increase: sweep volume_fraction on 15x15 grid, compare K=1 vs K=2
  2. Beta decrease: adiabatic tracking as phase separation weakens
  3. Topological splitting: crack formation via edge weight reduction

Key questions:
  - Can volume increase cause split? At what volume?
  - Can beta decrease cause fragmentation? At what beta?
  - Can topology change cause birth? At what crack weight?
"""
import sys, os, json, time
import numpy as np
import scipy.sparse as sp
from scipy.ndimage import label as ndlabel

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.multi import find_k_formations
from scc.energy import EnergyComputer

BETA = 50.0
ROWS, COLS = 15, 15


def make_params(vol_frac=0.3, beta=BETA):
    return ParameterRegistry(
        beta_bd=beta,
        volume_fraction=vol_frac,
        max_iter=5000,
        n_restarts=3,
        eps_grad=1e-3,
    )


def make_cracked_grid(rows, cols, crack_col, crack_weight):
    """Standard grid but edges crossing crack_col have reduced weight."""
    n = rows * cols
    row_idx, col_idx, weights = [], [], []
    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            if c + 1 < cols:
                w = crack_weight if c == crack_col else 1.0
                row_idx.extend([idx, idx + 1])
                col_idx.extend([idx + 1, idx])
                weights.extend([w, w])
            if r + 1 < rows:
                idx2 = (r + 1) * cols + c
                row_idx.extend([idx, idx2])
                col_idx.extend([idx2, idx])
                weights.extend([1.0, 1.0])
    W = sp.csr_matrix((weights, (row_idx, col_idx)), shape=(n, n))
    return GraphState(W)


def core_components(u, rows, cols, threshold=0.5):
    """Count connected components of the core region (u >= threshold)."""
    field_2d = u.reshape(rows, cols)
    binary = (field_2d >= threshold).astype(int)
    labeled, n_components = ndlabel(binary)
    # Also compute aspect ratio of the bounding box of the largest component
    if n_components == 0:
        return 0, 0.0, 0
    sizes = []
    for i in range(1, n_components + 1):
        sizes.append(np.sum(labeled == i))
    largest = np.argmax(sizes) + 1
    ys, xs = np.where(labeled == largest)
    if len(ys) == 0:
        return n_components, 0.0, 0
    h = ys.max() - ys.min() + 1
    w = xs.max() - xs.min() + 1
    aspect = max(h, w) / max(min(h, w), 1)
    core_size = int(np.sum(binary))
    return n_components, float(aspect), core_size


# ── Scenario 1: Volume increase ───────────────────────────────────────────

def scenario1_volume_sweep():
    print("=" * 70)
    print("SCENARIO 1: Volume increase — does a large formation split?")
    print("=" * 70)

    grid = GraphState.grid_2d(ROWS, COLS)
    n = grid.n
    vol_fracs = np.arange(0.25, 0.76, 0.05)
    results = []

    for vf in vol_fracs:
        vf = float(round(vf, 2))
        params = make_params(vol_frac=vf)
        t0 = time.time()

        # K=1
        k1 = find_formation(grid, params)
        E_K1 = k1.energy

        # K=2 with half volume each
        m_each = vf / 2.0
        # Ensure each half is in spinodal range
        if m_each < 0.22:
            m_each = 0.22
        k2 = find_k_formations(
            grid, params, K=2,
            lambda_rep=10.0, lambda_bar=100.0,
            m_per_formation=[m_each, m_each],
            n_restarts=3, max_iter=3000,
        )
        E_K2 = k2[0].energy + k2[1].energy

        n_comp, aspect, core_sz = core_components(k1.u, ROWS, COLS)
        delta = E_K1 - E_K2  # positive means K=2 preferred
        preferred = "K=2" if delta > 0 else "K=1"
        elapsed = time.time() - t0

        row = {
            'vol_frac': vf,
            'E_K1': round(E_K1, 4),
            'E_K2': round(E_K2, 4),
            'delta_E': round(delta, 4),
            'preferred': preferred,
            'K1_components': n_comp,
            'K1_aspect': round(aspect, 2),
            'K1_core_size': core_sz,
            'elapsed': round(elapsed, 1),
        }
        results.append(row)
        print(f"  vf={vf:.2f}  E_K1={E_K1:8.4f}  E_K2={E_K2:8.4f}  "
              f"delta={delta:+8.4f}  {preferred:4s}  "
              f"comp={n_comp}  aspect={aspect:.1f}  core={core_sz}  "
              f"({elapsed:.1f}s)")

    # Summary
    k2_wins = [r for r in results if r['preferred'] == 'K=2']
    if k2_wins:
        first = min(k2_wins, key=lambda r: r['vol_frac'])
        print(f"\n  >> K=2 first preferred at vol_frac = {first['vol_frac']:.2f}")
    else:
        print("\n  >> K=1 always preferred (no volume-driven split on 15x15 grid)")

    multi_comp = [r for r in results if r['K1_components'] > 1]
    if multi_comp:
        first_mc = min(multi_comp, key=lambda r: r['vol_frac'])
        print(f"  >> K=1 core splits into multiple components at vf = {first_mc['vol_frac']:.2f}")

    return results


# ── Scenario 2: Beta decrease ─────────────────────────────────────────────

def scenario2_beta_sweep():
    print("\n" + "=" * 70)
    print("SCENARIO 2: Beta decrease — does weakening separation cause fragmentation?")
    print("=" * 70)

    grid = GraphState.grid_2d(ROWS, COLS)
    n = grid.n
    vf = 0.3
    betas = list(range(50, 4, -1))
    results = []

    # Start with high-beta formation
    params0 = make_params(vol_frac=vf, beta=50.0)
    prev_result = find_formation(grid, params0)
    prev_u = prev_result.u.copy()

    for beta in betas:
        params = make_params(vol_frac=vf, beta=float(beta))
        t0 = time.time()

        # Adiabatic: use previous formation as init
        k1 = find_formation(grid, params, u_init=prev_u)
        # Also try cold start, take best
        k1_cold = find_formation(grid, params)
        if k1_cold.energy < k1.energy:
            k1 = k1_cold
        E_K1 = k1.energy

        # K=2
        k2 = find_k_formations(
            grid, params, K=2,
            lambda_rep=10.0, lambda_bar=100.0,
            n_restarts=2, max_iter=2000,
        )
        E_K2 = k2[0].energy + k2[1].energy

        u = k1.u
        strength = float(np.max(u) - np.min(u))
        n_comp, aspect, core_sz = core_components(u, ROWS, COLS)
        delta = E_K1 - E_K2
        preferred = "K=2" if delta > 0 else "K=1"
        elapsed = time.time() - t0

        row = {
            'beta': beta,
            'E_K1': round(E_K1, 4),
            'E_K2': round(E_K2, 4),
            'delta_E': round(delta, 4),
            'preferred': preferred,
            'strength': round(strength, 4),
            'K1_components': n_comp,
            'K1_core_size': core_sz,
            'elapsed': round(elapsed, 1),
        }
        results.append(row)

        prev_u = k1.u.copy()

        if beta % 5 == 0 or beta <= 10:
            print(f"  beta={beta:3d}  E_K1={E_K1:8.4f}  E_K2={E_K2:8.4f}  "
                  f"delta={delta:+8.4f}  {preferred:4s}  "
                  f"strength={strength:.3f}  comp={n_comp}  core={core_sz}  "
                  f"({elapsed:.1f}s)")

    # Summary: find dissolution point
    dissolved = [r for r in results if r['strength'] < 0.1]
    if dissolved:
        first_d = min(dissolved, key=lambda r: r['beta'])
        # Actually we want the highest beta where it dissolves (sweep is descending)
        print(f"\n  >> Formation dissolves (strength < 0.1) at beta = {first_d['beta']}")
    else:
        print("\n  >> Formation persists across all beta values tested")

    k2_wins = [r for r in results if r['preferred'] == 'K=2']
    if k2_wins:
        first_k2 = max(k2_wins, key=lambda r: r['beta'])
        print(f"  >> K=2 first preferred at beta = {first_k2['beta']}")
    else:
        print("  >> K=1 always preferred (no beta-driven split)")

    return results


# ── Scenario 3: Topological splitting ─────────────────────────────────────

def scenario3_crack():
    print("\n" + "=" * 70)
    print("SCENARIO 3: Topological splitting — crack formation")
    print("=" * 70)

    crack_col = 7  # middle column of 15-wide grid
    vf = 0.3
    crack_weights = [1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]
    results = []

    for cw in crack_weights:
        grid = make_cracked_grid(ROWS, COLS, crack_col, cw)
        n = grid.n
        params = make_params(vol_frac=vf)
        t0 = time.time()

        # K=1
        k1 = find_formation(grid, params)
        E_K1 = k1.energy

        # K=2
        k2 = find_k_formations(
            grid, params, K=2,
            lambda_rep=10.0, lambda_bar=100.0,
            n_restarts=3, max_iter=3000,
        )
        E_K2 = k2[0].energy + k2[1].energy

        n_comp, aspect, core_sz = core_components(k1.u, ROWS, COLS)
        delta = E_K1 - E_K2
        preferred = "K=2" if delta > 0 else "K=1"
        fiedler = float(grid.fiedler)
        overlap = float(np.sum(k2[0].u * k2[1].u))
        elapsed = time.time() - t0

        row = {
            'crack_weight': cw,
            'fiedler': round(fiedler, 6),
            'E_K1': round(E_K1, 4),
            'E_K2': round(E_K2, 4),
            'delta_E': round(delta, 4),
            'preferred': preferred,
            'K1_components': n_comp,
            'K1_core_size': core_sz,
            'K2_overlap': round(overlap, 4),
            'elapsed': round(elapsed, 1),
        }
        results.append(row)
        print(f"  crack_w={cw:7.3f}  fiedler={fiedler:.4f}  "
              f"E_K1={E_K1:8.4f}  E_K2={E_K2:8.4f}  "
              f"delta={delta:+8.4f}  {preferred:4s}  "
              f"comp={n_comp}  overlap={overlap:.3f}  ({elapsed:.1f}s)")

    # Summary
    k2_wins = [r for r in results if r['preferred'] == 'K=2']
    if k2_wins:
        first_k2 = max(k2_wins, key=lambda r: r['crack_weight'])
        print(f"\n  >> K=2 first preferred at crack_weight = {first_k2['crack_weight']}")
        print(f"     (Fiedler eigenvalue = {first_k2['fiedler']:.6f})")
    else:
        print("\n  >> K=1 always preferred (no topology-driven split)")

    return results


# ── Main ──────────────────────────────────────────────────────────────────

def main():
    print("Experiment 39: Formation birth/split dynamics")
    print("Grid: {}x{}, beta={}\n".format(ROWS, COLS, BETA))
    t_start = time.time()

    r1 = scenario1_volume_sweep()
    r2 = scenario2_beta_sweep()
    r3 = scenario3_crack()

    total_time = time.time() - t_start
    print(f"\n{'=' * 70}")
    print(f"Total elapsed: {total_time:.1f}s")

    # Save results
    os.makedirs("experiments/results", exist_ok=True)
    output = {
        'experiment': 'exp39_formation_birth',
        'grid': f'{ROWS}x{COLS}',
        'beta_default': BETA,
        'total_time_s': round(total_time, 1),
        'scenario1_volume_sweep': r1,
        'scenario2_beta_sweep': r2,
        'scenario3_crack': r3,
    }
    with open("experiments/results/exp39_formation_birth.json", "w") as f:
        json.dump(output, f, indent=2)
    print("Results saved to experiments/results/exp39_formation_birth.json")


if __name__ == "__main__":
    main()
