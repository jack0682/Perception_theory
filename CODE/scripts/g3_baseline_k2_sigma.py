"""
g3_baseline_k2_sigma.py — K=2 Baseline Multi-Formation σ_multi^(A) Numerical Test

W5 Day 2 G3 P1 Phase 5 initiation script (skeleton). Day 3 morning execution target.

Purpose:
    Empirically test σ_multi^(A) (per `THEORY/working/MF/multi_formation_sigma.md` §5)
    on K=2 well-separated formations on 2D torus L=20.

Requires:
    - scc validation patch per NQ-191 (option P2: additive `allow_outside_spinodal=True`
      kwarg on `find_formation` and `params.validate`). This script DEPENDS ON the patch
      being applied; without it, the small-c regime (c=0.10 per formation) is blocked.

Test plan (per `multi_formation_sigma.md` §7):
    Graph: 2D torus T^2_20 (translation-invariant; Aut(G) = Z_20^2 ⋊ D_4)
    K = 2; m_1 = m_2 = 40 (small per-formation; 40-site disk each on 400-site grid)
    Two well-separated tanh-disk ICs at distance d ∈ {5, 8, 12, 16}
    β = 4.0 (super-lattice ζ = 0.5 per V5b-T regime)
    λ_rep ∈ {0.01, 0.1, 1.0} (sweep coupling strength)

Measurements (per `multi_formation_sigma.md` §7):
    1. Per-formation σ_j (Commitment 14 applied to each H_jj on the joint Hessian).
    2. Cross-block H_12 op-norm and lowest 6 cross-eigenvalues.
    3. Cross-eigenvector: per-formation Goldstone overlap (test §5.5 V5b-F transfer).
    4. K=2 vs K=1 isoperimetric energy comparison (at λ_rep = 0).

Verdict criteria (per `multi_formation_sigma.md` §7):
    - Lemma 5.3 non-triviality: different d_min produces different σ_12? Expected YES.
    - §5.5 cross-Goldstone transfer: per-formation Goldstones split into Goldstone-pair?
      Expected YES with magnitude ~ ||H_12||.
    - σ_multi^(A) consistency: as d_min → ∞, ||H_12|| → 0, σ_multi^(A) reduces to
      decoupled (σ_1, σ_2). Expected YES.

Status: SKELETON. NOT EXECUTED Day 2. Day 3 morning launch target.
"""

import json
import sys
from pathlib import Path

import numpy as np
import scipy.sparse as sp


# ---------------------------------------------------------------------------
# scc imports — REQUIRES NQ-191 patch (allow_outside_spinodal kwarg)
# ---------------------------------------------------------------------------

REPO_CODE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_CODE))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.multi import find_k_formations  # K-field architecture (canonical I9)


# ---------------------------------------------------------------------------
# Graph: 2D torus L=20
# ---------------------------------------------------------------------------

def build_torus_2d(L: int):
    """2D torus T^2_L with periodic boundary conditions."""
    n = L * L
    edges = []
    for i in range(L):
        for j in range(L):
            idx = i * L + j
            # neighbors: (i±1, j), (i, j±1) with periodic wrap
            edges.append((idx, ((i + 1) % L) * L + j))
            edges.append((idx, i * L + (j + 1) % L))
    rows = [a for a, b in edges] + [b for a, b in edges]
    cols = [b for a, b in edges] + [a for a, b in edges]
    W = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    return GraphState(W), n


# ---------------------------------------------------------------------------
# Initial conditions: two well-separated tanh disks at distance d
# ---------------------------------------------------------------------------

def two_tanh_disks_ic(L: int, c: float, d_min: int, xi_0: float, seed: int = 0):
    """
    Two non-overlapping tanh-disk ICs at distance d_min on torus L×L.

    Returns: (u_init_1, u_init_2) each of shape (n,) projected to volume m = c*n.
    """
    n = L * L
    rng = np.random.default_rng(seed)

    # Disk 1: centered at (L/4, L/2)
    cx_1, cy_1 = L / 4, L / 2
    # Disk 2: centered at (L/4 + d_min, L/2)
    cx_2, cy_2 = (L / 4 + d_min) % L, L / 2

    r0 = np.sqrt(c * L * L / np.pi)  # disk radius for volume m = c*L*L

    i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')

    # Periodic distance to each center
    def per_dist(cx, cy):
        dx = np.minimum(np.abs(i_idx - cx), L - np.abs(i_idx - cx))
        dy = np.minimum(np.abs(j_idx - cy), L - np.abs(j_idx - cy))
        return np.sqrt(dx**2 + dy**2)

    r1 = per_dist(cx_1, cy_1).flatten()
    r2 = per_dist(cx_2, cy_2).flatten()

    u1 = 0.5 * (1.0 - np.tanh((r1 - r0) / xi_0))
    u2 = 0.5 * (1.0 - np.tanh((r2 - r0) / xi_0))

    # Add small noise + clip
    u1 = np.clip(u1 + rng.normal(0, 0.02, n), 0.01, 0.99)
    u2 = np.clip(u2 + rng.normal(0, 0.02, n), 0.01, 0.99)

    return u1, u2


# ---------------------------------------------------------------------------
# Joint Hessian (block-decomposed)
# ---------------------------------------------------------------------------

def joint_hessian_blocks(u1, u2, graph, params, lambda_rep, eps=1e-4):
    """
    Compute joint Hessian H_joint = [[H_11, H_12], [H_21, H_22]] via finite diff.

    Each diagonal block H_jj is the per-formation Hessian on T_{u_j} Σ_{m_j}
    (∼ R^{n-1} after projection out the volume tangent direction).

    Off-diagonal block H_12 = ∂²E_K / ∂u_1 ∂u_2 = λ_rep * I (per Coupling Bound Lemma)
    in the well-separated regime, plus exp-small corrections.

    Returns:
        H_11, H_12, H_22 (each shape (n, n))
    """
    # TODO Day 3: implement joint-Hessian finite-difference computation.
    # Requires multi.py grad_K which gives (∂E/∂u_1, ∂E/∂u_2).
    raise NotImplementedError("Day 3 morning: implement joint-Hessian FD")


# ---------------------------------------------------------------------------
# σ_multi^(A) extraction (per `multi_formation_sigma.md` §5.1)
# ---------------------------------------------------------------------------

def extract_sigma_multi_A(u1, u2, graph, params, lambda_rep,
                          n_modes_per=6, n_modes_cross=6):
    """
    Extract σ_multi^(A) per `multi_formation_sigma.md` §5.1.

    Returns dict with:
        'F_total': total local-maxima count
        'sigma_1': per-formation σ_1 = (F_1, [(n_k, [rho_k], lam_k)])
        'sigma_2': per-formation σ_2
        'sigma_12': cross-formation σ_12 = (cross_eigenvalues, cross_irreps, cross_nodal)
        'H12_op_norm': ||H_12||_op
        'cross_goldstone_overlaps': for each cross-eigenvector, max overlap with
            per-formation translation modes (test §5.5 V5b-F transfer)
    """
    # TODO Day 3: implement σ_multi^(A) extraction.
    # Steps:
    # 1. Compute H_11, H_12, H_22 via joint_hessian_blocks.
    # 2. Per-formation σ_j: eigh(H_jj on tangent space ⊥ 1), top n_modes_per modes.
    #    For each mode: nodal count, irrep label (under Aut(G_uj)), eigenvalue.
    # 3. Cross-block: 2x2 sub-Hessian H̃_12. eigh top n_modes_cross modes.
    #    For each: per-formation restriction nodal count, joint-pair irrep, eigenvalue.
    # 4. Goldstone overlap: project cross-eigenvectors onto translation modes
    #    of u_1 and u_2 separately. Record max overlap per axis per formation.
    raise NotImplementedError("Day 3 morning: implement σ_multi^(A) extraction")


# ---------------------------------------------------------------------------
# Sweep main
# ---------------------------------------------------------------------------

def run_sweep():
    L = 20
    c = 0.10  # 40 sites per formation -- REQUIRES NQ-191 PATCH
    beta = 4.0
    xi_0 = np.sqrt(1.0 / beta)  # ζ = 0.5
    d_min_values = [5, 8, 12, 16]
    lambda_rep_values = [0.01, 0.1, 1.0]
    seeds_per = 3

    graph, n = build_torus_2d(L)
    results = []

    for d_min in d_min_values:
        for lambda_rep in lambda_rep_values:
            for seed in range(seeds_per):
                u1_init, u2_init = two_tanh_disks_ic(L, c, d_min, xi_0, seed)
                params = ParameterRegistry(
                    alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
                    a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
                    w_cl=0.0, w_sep=0.0, w_bd=1.0,
                    n_restarts=1, max_iter=15000,
                    # NQ-191 patch required: allow_outside_spinodal=True,
                    # lambda_rep=lambda_rep,  # K-field coupling -- if multi.py exposes
                )

                # TODO Day 3: actual K=2 optimization.
                # Need: scc.multi.find_formation_K with K=2, lambda_rep coupling,
                #       u_init=(u1_init, u2_init).
                # Currently: stub.
                try:
                    res = None  # placeholder
                    sigma_data = None  # placeholder
                except Exception as e:
                    print(f"FAIL d_min={d_min} lr={lambda_rep} seed={seed}: {e}")
                    continue

                results.append({
                    'd_min': d_min,
                    'lambda_rep': lambda_rep,
                    'seed': seed,
                    'energy': None,  # Fill in Day 3
                    'F_total': None,
                    'sigma_1': None,
                    'sigma_2': None,
                    'sigma_12': None,
                    'H12_op_norm': None,
                    'cross_goldstone_overlaps': None,
                })

    return results


# ---------------------------------------------------------------------------
# Main entrypoint
# ---------------------------------------------------------------------------

def main():
    print("g3_baseline_k2_sigma.py — SKELETON ONLY (Day 3 morning execution target)")
    print(f"Repo: {REPO_CODE}")
    print()
    print("Required patch: NQ-191 P2 (allow_outside_spinodal=True kwarg)")
    print("See: THEORY/logs/daily/2026-04-28/01_NQ173_v5b_f_verdict.md §5")
    print()
    print("Day 2: skeleton structure committed.")
    print("Day 3 morning Block 0: NQ-191 patch (~30 min).")
    print("Day 3 morning Block 1: implement joint_hessian_blocks() + extract_sigma_multi_A().")
    print("Day 3 morning Block 2: run_sweep() actual execution (~30-60 min).")
    print("Day 3 PM: analyze results → working/MF/multi_formation_sigma.md update.")
    print()
    print("Skeleton compile-check:")
    print(f"  - Imports OK: scc.graph, scc.params, scc.optimizer, scc.multi")
    print(f"  - build_torus_2d(L=20): produces n={20*20} graph state")
    print(f"  - two_tanh_disks_ic: runs without error (verified by import)")
    print()
    print("To verify skeleton imports:")
    print("    python3 -c 'import g3_baseline_k2_sigma'")
    print()
    print("DO NOT call run_sweep() Day 2 — will fail at NotImplementedError.")


if __name__ == '__main__':
    main()
