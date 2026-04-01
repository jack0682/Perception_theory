#!/usr/bin/env python3
"""Experiment 30: K=2 → K=1 merge flow dynamics.

Studies the merge dichotomy problem: when K=2 formations overlap enough,
does the K-formation critical point become a saddle, and does gradient flow
from that saddle lead to a K=1 solution?

Two scenarios:
  A) Homogeneous 15×15 grid — baseline where K=1 dominates.
  B) Dumbbell graph (two 8×8 clusters connected by a bridge of width w).
     Sweep bridge width w from 1 to 8 to find the K=2 → K=1 transition.

Phase 1: lambda_rep sweep on dumbbell to track overlap.
Phase 2: Compare K=2 self-energy vs optimized K=1 merged energy.
Phase 3: Hessian curvature in the merge direction.
Phase 4: Gradient flow from the saddle.
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
LAMBDA_REPS = [20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.01]


def make_params(beta=BETA, vol_frac=0.3):
    return ParameterRegistry(
        beta_bd=beta,
        volume_fraction=vol_frac,
        max_iter=5000,
        n_restarts=3,
        eps_grad=1e-3,
    )


def make_dumbbell(cluster_size=8, bridge_width=1):
    """Two cluster_size×cluster_size grids connected by bridge_width edges.

    Layout: left cluster (rows 0..cs-1, cols 0..cs-1),
            right cluster (rows 0..cs-1, cols cs..2*cs-1),
            bridge connects the middle bridge_width rows at col cs-1 ↔ col cs.
    """
    cs = cluster_size
    rows, cols = cs, 2 * cs
    n = rows * cols
    row_idx, col_idx = [], []

    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            # Right neighbor
            if c + 1 < cols:
                # Block the bridge column boundary except for bridge rows
                if c == cs - 1:
                    # Only connect if in bridge band
                    mid = cs // 2
                    half_bw = bridge_width // 2
                    lo = max(0, mid - half_bw)
                    hi = min(cs, mid - half_bw + bridge_width)
                    if lo <= r < hi:
                        row_idx.extend([idx, idx + 1])
                        col_idx.extend([idx + 1, idx])
                else:
                    row_idx.extend([idx, idx + 1])
                    col_idx.extend([idx + 1, idx])
            # Down neighbor
            if r + 1 < rows:
                idx2 = (r + 1) * cols + c
                row_idx.extend([idx, idx2])
                col_idx.extend([idx2, idx])

    data = np.ones(len(row_idx))
    W = sp.csr_matrix((data, (row_idx, col_idx)), shape=(n, n))
    return GraphState(W), (rows, cols)


def overlap(u1, u2):
    """Pointwise overlap: sum(u1 * u2)."""
    return float(np.sum(u1 * u2))


def run_k2_vs_k1(graph, params, label, lambda_reps=None):
    """Core experiment: sweep lambda_rep, compare K=2 vs merged K=1.

    Returns (phase1_rows, phase2_rows, phase3_rows, phase4_result).
    """
    if lambda_reps is None:
        lambda_reps = LAMBDA_REPS
    n = graph.n

    # ---- Phase 1: lambda_rep sweep ----
    print("=" * 70)
    print(f"[{label}] PHASE 1: Lambda_rep sweep — K=2 overlap tracking")
    print("=" * 70)

    prev_fields = None
    phase1 = []

    for lrep in lambda_reps:
        t0 = time.time()
        k2 = find_k_formations(
            graph, params, K=2,
            lambda_rep=lrep, lambda_bar=100.0,
            n_restarts=3 if prev_fields is None else 1,
            max_iter=3000,
            init_fields=prev_fields,
        )
        elapsed = time.time() - t0
        u1, u2 = k2[0].u, k2[1].u
        E1, E2 = k2[0].energy, k2[1].energy
        ov = overlap(u1, u2)
        row = {
            'lambda_rep': lrep, 'overlap': ov,
            'E1': E1, 'E2': E2, 'E_K2_self': E1 + E2,
            'elapsed': elapsed,
        }
        phase1.append(row)
        prev_fields = [u1.copy(), u2.copy()]
        print(f"  λ_rep={lrep:6.2f}  overlap={ov:.4f}  "
              f"E_self={E1+E2:.4f}  ({elapsed:.1f}s)")

    # ---- Phase 2: merge comparison ----
    print()
    print("=" * 70)
    print(f"[{label}] PHASE 2: K=2 self-energy vs K=1 merged")
    print("=" * 70)

    prev_fields = None
    phase2 = []
    for lrep in lambda_reps:
        t0 = time.time()
        k2 = find_k_formations(
            graph, params, K=2,
            lambda_rep=lrep, lambda_bar=100.0,
            n_restarts=1, max_iter=3000,
            init_fields=prev_fields,
        )
        u1, u2 = k2[0].u, k2[1].u
        prev_fields = [u1.copy(), u2.copy()]
        E_K2 = k2[0].energy + k2[1].energy

        # Merged K=1 competitor
        u_merged = np.clip(u1 + u2, 0.0, 1.0)
        m_merged = np.sum(u1) + np.sum(u2)
        u_merged = project_volume(u_merged, m_merged)
        vf = m_merged / n
        # Clamp volume fraction to spinodal range
        vf = max(0.22, min(0.78, vf))
        pm = ParameterRegistry(
            beta_bd=params.beta_bd, volume_fraction=vf,
            max_iter=5000, n_restarts=1, eps_grad=1e-3,
        )
        k1 = find_formation(graph, pm, u_init=u_merged)
        E_K1 = k1.energy
        ov = overlap(u1, u2)
        merge_pref = E_K1 < E_K2
        elapsed = time.time() - t0

        row = {
            'lambda_rep': lrep, 'overlap': ov,
            'E_K2_self': E_K2, 'E_K1': E_K1,
            'delta_E': E_K1 - E_K2,
            'merge_preferred': bool(merge_pref),
            'elapsed': elapsed,
        }
        phase2.append(row)
        flag = "<<< MERGE" if merge_pref else ""
        print(f"  λ_rep={lrep:6.2f}  overlap={ov:.4f}  "
              f"E_K2={E_K2:.4f}  E_K1={E_K1:.4f}  "
              f"ΔE={E_K1 - E_K2:+.4f}  {flag}")

    # ---- Phase 3: Hessian curvature ----
    print()
    print("=" * 70)
    print(f"[{label}] PHASE 3: Merge-direction curvature")
    print("=" * 70)

    ec = EnergyComputer(graph, params)
    ec.normalize_weights()
    sample_lreps = [lambda_reps[0], lambda_reps[len(lambda_reps)//2],
                    lambda_reps[-2], lambda_reps[-1]]
    phase3 = []
    prev_fields = None
    for lrep in sample_lreps:
        k2 = find_k_formations(
            graph, params, K=2,
            lambda_rep=lrep, lambda_bar=100.0,
            n_restarts=2 if prev_fields is None else 1,
            max_iter=3000, init_fields=prev_fields,
        )
        u1, u2 = k2[0].u, k2[1].u
        prev_fields = [u1.copy(), u2.copy()]
        ov = overlap(u1, u2)

        norm_u2 = np.linalg.norm(u2)
        if norm_u2 < 1e-12:
            continue
        delta = u2 / norm_u2
        eps_h = 1e-3
        E_c = float(ec.energy(u1)[0]) + float(ec.energy(u2)[0])
        u1p = project_volume(u1 + eps_h * delta, np.sum(u1))
        u2m = project_volume(u2 - eps_h * delta, np.sum(u2))
        E_p = float(ec.energy(u1p)[0]) + float(ec.energy(u2m)[0])
        u1m = project_volume(u1 - eps_h * delta, np.sum(u1))
        u2p = project_volume(u2 + eps_h * delta, np.sum(u2))
        E_m = float(ec.energy(u1m)[0]) + float(ec.energy(u2p)[0])
        curv = (E_p + E_m - 2 * E_c) / (eps_h ** 2)
        is_saddle = curv < 0

        row = {'lambda_rep': lrep, 'overlap': ov,
               'curvature': curv, 'is_saddle': bool(is_saddle)}
        phase3.append(row)
        tag = "SADDLE" if is_saddle else "stable"
        print(f"  λ_rep={lrep:6.2f}  overlap={ov:.4f}  "
              f"d²E/dε²={curv:+.6f}  [{tag}]")

    # ---- Phase 4: gradient flow from perturbed K=2 ----
    print()
    print("=" * 70)
    print(f"[{label}] PHASE 4: Gradient flow from K=2 → K=1?")
    print("=" * 70)

    # Use lowest lambda_rep (most overlap)
    target_lrep = lambda_reps[-1]
    k2 = find_k_formations(
        graph, params, K=2,
        lambda_rep=target_lrep, lambda_bar=100.0,
        n_restarts=2, max_iter=3000,
    )
    u1, u2 = k2[0].u, k2[1].u
    ov_init = overlap(u1, u2)
    print(f"  K=2 at λ_rep={target_lrep}, overlap={ov_init:.4f}")

    norm_u2 = np.linalg.norm(u2)
    if norm_u2 < 1e-12:
        print("  u2 collapsed — already at K=1")
        phase4 = {'merged': True, 'reason': 'u2_zero'}
    else:
        delta = u2 / norm_u2
        u_flow = u1 + 0.1 * delta  # perturbation toward merge
        m_total = np.sum(u1) + np.sum(u2)
        u_flow = project_volume(u_flow, m_total)
        vf = m_total / n
        vf = max(0.22, min(0.78, vf))
        pf = ParameterRegistry(
            beta_bd=params.beta_bd, volume_fraction=vf,
            max_iter=5000, n_restarts=1, eps_grad=1e-3,
        )
        res = find_formation(graph, pf, u_init=u_flow)
        E_K2 = k2[0].energy + k2[1].energy
        E_flow = res.energy
        core_size = int(np.sum(res.u > 0.5))

        print(f"  E_K2={E_K2:.4f}, E_flow={E_flow:.4f}, "
              f"ΔE={E_flow - E_K2:+.4f}, core={core_size}")
        if E_flow < E_K2:
            print("  >>> MERGE preferred — gradient flow found lower energy")
        else:
            print("  >>> K=2 remains preferred — flow did not improve")

        phase4 = {
            'target_lrep': target_lrep, 'overlap_init': ov_init,
            'E_K2_self': E_K2, 'E_flow': E_flow,
            'delta_E': E_flow - E_K2, 'core_size': core_size,
            'merge_preferred': bool(E_flow < E_K2),
        }

    return phase1, phase2, phase3, phase4


def print_summary(label, phase2, phase3):
    """Print summary table."""
    print()
    print("=" * 70)
    print(f"[{label}] SUMMARY")
    print("=" * 70)
    print(f"{'λ_rep':>8} {'overlap':>8} {'E_K2':>10} {'E_K1':>10} "
          f"{'ΔE':>10} {'merge?':>7} {'curv':>12} {'saddle?':>8}")
    print("-" * 78)
    hmap = {r['lambda_rep']: r for r in phase3}
    for r in phase2:
        lr = r['lambda_rep']
        h = hmap.get(lr, {})
        cs = f"{h['curvature']:+.4f}" if 'curvature' in h else "—"
        ss = "YES" if h.get('is_saddle') else ("no" if 'is_saddle' in h else "—")
        ms = "YES" if r['merge_preferred'] else "no"
        print(f"{lr:8.2f} {r['overlap']:8.4f} {r['E_K2_self']:10.4f} "
              f"{r['E_K1']:10.4f} {r['delta_E']:+10.4f} {ms:>7} "
              f"{cs:>12} {ss:>8}")


def main():
    print("Experiment 30: K=2 → K=1 Merge Flow Dynamics")
    print(f"β={BETA}")
    print()
    t_start = time.time()

    all_results = {}

    # ===== Scenario A: Homogeneous 15×15 grid =====
    print("\n" + "#" * 70)
    print("# SCENARIO A: Homogeneous 15×15 grid")
    print("#" * 70)
    graph_a = GraphState.grid_2d(15, 15)
    params_a = make_params()
    print(f"n={graph_a.n}, λ₂={graph_a.fiedler:.4f}\n")
    p1a, p2a, p3a, p4a = run_k2_vs_k1(graph_a, params_a, "HomoGrid")
    print_summary("HomoGrid", p2a, p3a)
    all_results['scenario_A'] = {
        'type': 'homogeneous_grid', 'n': graph_a.n,
        'phase1': p1a, 'phase2': p2a, 'phase3': p3a, 'phase4': p4a,
    }

    # ===== Scenario B: Bridge-width sweep on dumbbell =====
    print("\n" + "#" * 70)
    print("# SCENARIO B: Dumbbell graph — bridge width sweep")
    print("#" * 70)

    bridge_widths = [1, 2, 3, 4, 6, 8]
    bridge_results = []
    for bw in bridge_widths:
        print(f"\n--- Bridge width = {bw} ---")
        graph_b, (rows, cols) = make_dumbbell(cluster_size=8, bridge_width=bw)
        print(f"n={graph_b.n}, λ₂={graph_b.fiedler:.4f}")
        params_b = make_params(vol_frac=0.3)

        # Just run Phase 2 comparison at a few lambda_rep values (faster)
        short_lreps = [10.0, 1.0, 0.1, 0.01]
        _, p2b, _, p4b = run_k2_vs_k1(graph_b, params_b,
                                        f"Dumbbell(bw={bw})",
                                        lambda_reps=short_lreps)
        # Key metric: is K=2 ever preferred?
        k2_preferred_at = [r['lambda_rep'] for r in p2b if not r['merge_preferred']]
        merge_at = [r['lambda_rep'] for r in p2b if r['merge_preferred']]

        brow = {
            'bridge_width': bw,
            'n': graph_b.n,
            'fiedler': graph_b.fiedler,
            'k2_preferred_lreps': k2_preferred_at,
            'merge_preferred_lreps': merge_at,
            'phase2': p2b,
            'phase4': p4b,
        }
        bridge_results.append(brow)

        if k2_preferred_at:
            print(f"  K=2 preferred at λ_rep: {k2_preferred_at}")
        else:
            print(f"  K=1 always preferred (merge dominates)")

    all_results['scenario_B'] = bridge_results

    elapsed_total = time.time() - t_start

    # ===== Final summary =====
    print("\n" + "=" * 70)
    print("FINAL SUMMARY: Bridge Width → Merge Transition")
    print("=" * 70)
    print(f"{'bw':>4} {'n':>5} {'λ₂':>8} {'K2 pref?':>10} {'merge pref?':>12}")
    print("-" * 45)
    for br in bridge_results:
        k2 = len(br['k2_preferred_lreps']) > 0
        print(f"{br['bridge_width']:4d} {br['n']:5d} {br['fiedler']:8.4f} "
              f"{'YES' if k2 else 'no':>10} "
              f"{'YES' if not k2 else 'partial':>12}")

    print(f"\nTotal runtime: {elapsed_total:.1f}s")

    # Save
    all_results['total_time_s'] = elapsed_total
    all_results['beta'] = BETA
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'exp30_merge_flow_results.json')
    with open(out_path, 'w') as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")


if __name__ == '__main__':
    main()
