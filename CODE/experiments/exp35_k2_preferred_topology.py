#!/usr/bin/env python3
"""Experiment 35: Find topologies where K=2 is globally preferred over K=1.

exp30 showed K=1 always wins on 15×15 grid and dumbbell (bw=1-8).
Isoperimetric ordering says: on homogeneous graphs, one big formation has
less boundary than two small ones. K=2 can only win when graph topology
imposes a prohibitive bridge cost on the single formation.

This experiment tests more extreme topologies:
  1. Near-disconnected clusters (bridge weight 0.001)
  2. Barbell with long path (L=1,3,5,10,15)
  3. Weighted bridge grid (w=1.0 down to 0.001)
  4. Star of 3 clusters through a hub node
"""
import sys, os, json, time
import numpy as np
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.multi import find_k_formations
from scc.energy import EnergyComputer

BETA = 50.0


def make_params(vol_frac=0.3):
    return ParameterRegistry(
        beta_bd=BETA,
        volume_fraction=vol_frac,
        max_iter=5000,
        n_restarts=3,
        eps_grad=1e-3,
    )


# ── Graph constructors ──────────────────────────────────────────────────

def make_barbell(cluster_size=8, path_length=1):
    """Two cs×cs grids connected by a path of length path_length."""
    cs = cluster_size
    n_path = max(0, path_length - 1)  # intermediate nodes
    n = 2 * cs * cs + n_path
    rows, cols = [], []

    # Left cluster: grid cs×cs, nodes 0..cs²-1
    for r in range(cs):
        for c in range(cs):
            idx = r * cs + c
            if c + 1 < cs:
                rows.extend([idx, idx + 1])
                cols.extend([idx + 1, idx])
            if r + 1 < cs:
                idx2 = (r + 1) * cs + c
                rows.extend([idx, idx2])
                cols.extend([idx2, idx])

    # Right cluster: nodes (cs²+n_path)..end
    offset_r = cs * cs + n_path
    for r in range(cs):
        for c in range(cs):
            idx = offset_r + r * cs + c
            if c + 1 < cs:
                rows.extend([idx, idx + 1])
                cols.extend([idx + 1, idx])
            if r + 1 < cs:
                idx2 = offset_r + (r + 1) * cs + c
                rows.extend([idx, idx2])
                cols.extend([idx2, idx])

    # Path: connect left cluster edge to right cluster edge
    left_anchor = (cs // 2) * cs + (cs - 1)
    right_anchor = offset_r + (cs // 2) * cs
    if n_path == 0:
        rows.extend([left_anchor, right_anchor])
        cols.extend([right_anchor, left_anchor])
    else:
        first_path = cs * cs
        rows.extend([left_anchor, first_path])
        cols.extend([first_path, left_anchor])
        for i in range(n_path - 1):
            rows.extend([first_path + i, first_path + i + 1])
            cols.extend([first_path + i + 1, first_path + i])
        rows.extend([first_path + n_path - 1, right_anchor])
        cols.extend([right_anchor, first_path + n_path - 1])

    data = np.ones(len(rows))
    W = sp.csr_matrix((data, (rows, cols)), shape=(n, n))
    return GraphState(W), n


def make_weighted_grid(nrows, ncols, bridge_col, bridge_weight):
    """Standard grid but edges crossing bridge_col have weight bridge_weight."""
    n = nrows * ncols
    row_idx, col_idx, weights = [], [], []
    for r in range(nrows):
        for c in range(ncols):
            idx = r * ncols + c
            if c + 1 < ncols:
                w = bridge_weight if (c == bridge_col) else 1.0
                row_idx.extend([idx, idx + 1])
                col_idx.extend([idx + 1, idx])
                weights.extend([w, w])
            if r + 1 < nrows:
                idx2 = (r + 1) * ncols + c
                row_idx.extend([idx, idx2])
                col_idx.extend([idx2, idx])
                weights.extend([1.0, 1.0])
    W = sp.csr_matrix((weights, (row_idx, col_idx)), shape=(n, n))
    return GraphState(W), n


def make_star_clusters(cluster_size=6, n_clusters=3):
    """n_clusters grids of cluster_size×cluster_size connected through a hub."""
    cs = cluster_size
    cn = cs * cs  # nodes per cluster
    hub = n_clusters * cn  # hub node index
    n = hub + 1
    rows, cols = [], []

    for k in range(n_clusters):
        offset = k * cn
        for r in range(cs):
            for c in range(cs):
                idx = offset + r * cs + c
                if c + 1 < cs:
                    rows.extend([idx, idx + 1])
                    cols.extend([idx + 1, idx])
                if r + 1 < cs:
                    idx2 = offset + (r + 1) * cs + c
                    rows.extend([idx, idx2])
                    cols.extend([idx2, idx])
        # Connect cluster center to hub
        center = offset + (cs // 2) * cs + (cs // 2)
        rows.extend([center, hub])
        cols.extend([hub, center])

    data = np.ones(len(rows))
    W = sp.csr_matrix((data, (rows, cols)), shape=(n, n))
    return GraphState(W), n


# ── Core comparison ──────────────────────────────────────────────────────

def compare_k2_vs_k1(graph, params, label, lambda_rep=10.0, n_restarts=3):
    """Find K=2, then K=1 with matched volume. Return result dict."""
    n = graph.n
    t0 = time.time()

    # K=2
    k2 = find_k_formations(
        graph, params, K=2,
        lambda_rep=lambda_rep, lambda_bar=100.0,
        n_restarts=n_restarts, max_iter=3000,
    )
    u1, u2 = k2[0].u, k2[1].u
    E_K2 = k2[0].energy + k2[1].energy

    # K=1 with merged volume
    m_merged = float(np.sum(u1) + np.sum(u2))
    vf = m_merged / n
    vf = max(0.22, min(0.78, vf))
    pm = ParameterRegistry(
        beta_bd=BETA, volume_fraction=vf,
        max_iter=5000, n_restarts=n_restarts, eps_grad=1e-3,
    )
    # Warm-start from merged field
    u_init = np.clip(u1 + u2, 0.0, 1.0)
    u_init = project_volume(u_init, vf * n)
    k1 = find_formation(graph, pm, u_init=u_init)
    # Also try cold start and take the best
    k1_cold = find_formation(graph, pm)
    if k1_cold.energy < k1.energy:
        k1 = k1_cold
    E_K1 = k1.energy
    elapsed = time.time() - t0

    # Fiedler eigenvalue
    lam2 = float(graph.fiedler)

    delta = E_K1 - E_K2
    preferred = "K=2" if delta > 0 else "K=1"
    overlap = float(np.sum(u1 * u2))

    row = {
        'label': label,
        'n': n,
        'lambda2': round(lam2, 6),
        'lambda_rep': lambda_rep,
        'E_K2_self': round(E_K2, 4),
        'E_K1': round(E_K1, 4),
        'delta_E': round(delta, 4),
        'preferred': preferred,
        'overlap': round(overlap, 4),
        'elapsed': round(elapsed, 1),
    }
    flag = "★ K=2 WINS" if preferred == "K=2" else ""
    print(f"  {label:40s} n={n:4d}  λ₂={lam2:.5f}  "
          f"E_K2={E_K2:.4f}  E_K1={E_K1:.4f}  ΔE={delta:+.4f}  "
          f"{preferred}  {flag}")
    return row


# ── Main ─────────────────────────────────────────────────────────────────

def main():
    results = []
    params_03 = make_params(vol_frac=0.3)

    # ── 1. Barbell: two 8×8 grids, varying path length ──
    print("=" * 90)
    print("BARBELL: two 8×8 clusters connected by path of length L")
    print("=" * 90)
    for L in [1, 3, 5, 10, 15]:
        g, n = make_barbell(cluster_size=8, path_length=L)
        label = f"barbell_L={L}"
        for lrep in [10.0, 1.0]:
            row = compare_k2_vs_k1(g, params_03, f"{label}_lrep={lrep}", lambda_rep=lrep)
            results.append(row)

    # ── 2. Weighted bridge: 8×16 grid with weak bridge at col 7 ──
    print()
    print("=" * 90)
    print("WEIGHTED BRIDGE: 8×16 grid, bridge column weight w")
    print("=" * 90)
    for w in [1.0, 0.5, 0.1, 0.05, 0.01, 0.001]:
        g, n = make_weighted_grid(8, 16, bridge_col=7, bridge_weight=w)
        label = f"wbridge_w={w}"
        for lrep in [10.0, 1.0]:
            row = compare_k2_vs_k1(g, params_03, f"{label}_lrep={lrep}", lambda_rep=lrep)
            results.append(row)

    # ── 3. Star of 3 clusters ──
    print()
    print("=" * 90)
    print("STAR: 3 clusters of 6×6 through hub node")
    print("=" * 90)
    g, n = make_star_clusters(cluster_size=6, n_clusters=3)
    for lrep in [10.0, 1.0]:
        row = compare_k2_vs_k1(g, params_03, f"star_3x6x6_lrep={lrep}", lambda_rep=lrep)
        results.append(row)

    # ── Summary ──
    print()
    print("=" * 90)
    print("SUMMARY")
    print("=" * 90)
    k2_wins = [r for r in results if r['preferred'] == 'K=2']
    print(f"Total configs: {len(results)}")
    print(f"K=2 preferred: {len(k2_wins)}")
    if k2_wins:
        print("\nK=2 preferred cases:")
        for r in k2_wins:
            print(f"  {r['label']:40s} ΔE={r['delta_E']:+.4f}  λ₂={r['lambda2']:.5f}")
    else:
        print("\nNo topology found where K=2 is preferred.")
        print("Isoperimetric ordering may hold universally for these graph families.")

    # Save JSON
    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "exp35_results.json")
    with open(outpath, 'w') as f:
        json.dump({'results': results, 'summary': {
            'total': len(results),
            'k2_preferred': len(k2_wins),
            'k2_cases': k2_wins,
        }}, f, indent=2)
    print(f"\nResults saved to {outpath}")


if __name__ == '__main__':
    main()
