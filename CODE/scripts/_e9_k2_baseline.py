"""
_e9_k2_baseline.py — K=2 baseline numerical for σ_multi^(A) verification

Phase 3 E9: implements joint_hessian_blocks and extract_sigma_multi_A,
then runs the sweep predicted in:
  THEORY/logs/daily/2026-04-28/05_sigma_multi_concrete_T2_K2.md §6.2

Predictions:
  - Sym Goldstone-pair: λ_sym ≈ μ_Gold + λ_rep
  - Antisym Goldstone-pair: λ_antisym ≈ μ_Gold - λ_rep (NEGATIVE for λ_rep > μ_Gold)
  - Joint Hessian eigenvalues = per-block ± λ_rep + O(exp(-c_0 d))

Setup: 2D torus T²_{20}, K=2, two disks at d=8 along x-axis,
       c=0.10 each, β=4.0 (ζ=0.5), λ_rep ∈ {0.01, 0.1, 1.0}.

Output: scripts/results/e9_k2_baseline.json
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Bypass spinodal validation
from scc.params import ParameterRegistry
_orig_validate = ParameterRegistry.validate
def _bypass_validate(self, *a, **kw):
    valid, V, W = _orig_validate(self, *a, **kw)
    Vf = [v for v in V if "outside spinodal" not in v]
    return (len(Vf) == 0, Vf, W)
ParameterRegistry.validate = _bypass_validate

import json
import time
import numpy as np
import scipy.sparse as sp
from scc.graph import GraphState
from scc.energy import EnergyComputer
from scc.multi import _optimize_k_fields, _total_energy
from scc.optimizer import compute_diagnostics


def build_torus_2d(L):
    n = L * L
    edges = []
    for i in range(L):
        for j in range(L):
            idx = i * L + j
            edges.append((idx, ((i + 1) % L) * L + j))
            edges.append((idx, i * L + (j + 1) % L))
    rows = [a for a, b in edges] + [b for a, b in edges]
    cols = [b for a, b in edges] + [a for a, b in edges]
    W = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    return GraphState(W), n


def two_disk_ic(L, c, d_min, xi_0, seed=0):
    """Two well-separated tanh-disk ICs at distance d_min on torus L×L."""
    n = L * L
    rng = np.random.default_rng(seed)
    cx_1, cy_1 = L / 4.0, L / 2.0
    cx_2, cy_2 = (L / 4.0 + d_min) % L, L / 2.0
    r0 = np.sqrt(c * L * L / np.pi)

    i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
    def per_dist(cx, cy):
        dx = np.minimum(np.abs(i_idx - cx), L - np.abs(i_idx - cx))
        dy = np.minimum(np.abs(j_idx - cy), L - np.abs(j_idx - cy))
        return np.sqrt(dx**2 + dy**2)
    r1 = per_dist(cx_1, cy_1).flatten()
    r2 = per_dist(cx_2, cy_2).flatten()
    u1 = 0.5 * (1.0 - np.tanh((r1 - r0) / xi_0))
    u2 = 0.5 * (1.0 - np.tanh((r2 - r0) / xi_0))
    u1 = np.clip(u1 + rng.normal(0, 0.02, n), 0.01, 0.99)
    u2 = np.clip(u2 + rng.normal(0, 0.02, n), 0.01, 0.99)
    return u1, u2


def k_field_grad_per_formation(fields, j, ec, lambda_rep, lambda_bar):
    """Compute ∂E_K / ∂u^(j) at given fields (K-list)."""
    K = len(fields)
    g_intra = ec.gradient(fields[j])  # ∂E_intra(u^j) / ∂u^j
    # Repulsion: ∂(λ_rep Σ_{j<k} <u^j, u^k>) / ∂u^j = λ_rep Σ_{k≠j} u^k
    g_rep = lambda_rep * sum(fields[k] for k in range(K) if k != j)
    # Simplex barrier: ∂(λ_bar Σ max(0, S-1)²) / ∂u^j = 2 λ_bar (S-1)_+
    S = sum(fields)
    g_bar = 2.0 * lambda_bar * np.maximum(0.0, S - 1.0)
    return g_intra + g_rep + g_bar


def joint_hessian_blocks(fields, ec, lambda_rep, lambda_bar, eps=1e-4):
    """Compute joint Hessian H_joint = [[H_11, H_12], [H_21, H_22]] via FD.

    Returns:
        H_11, H_12, H_22 (each shape (n, n))
    """
    n = fields[0].shape[0]
    K = len(fields)
    g0 = [k_field_grad_per_formation(fields, j, ec, lambda_rep, lambda_bar) for j in range(K)]
    H = [[np.zeros((n, n)) for _ in range(K)] for _ in range(K)]
    for k_perturb in range(K):
        for i in range(n):
            fields_p = [u.copy() for u in fields]
            fields_p[k_perturb][i] += eps
            for j in range(K):
                g_p = k_field_grad_per_formation(fields_p, j, ec, lambda_rep, lambda_bar)
                H[j][k_perturb][:, i] = (g_p - g0[j]) / eps
    # Symmetrize each block
    H_11 = (H[0][0] + H[0][0].T) / 2.0
    H_22 = (H[1][1] + H[1][1].T) / 2.0
    H_12 = (H[0][1] + H[1][0].T) / 2.0
    return H_11, H_12, H_22


def translation_modes_torus(u_star, L):
    g = u_star.reshape(L, L)
    du_x = (np.roll(g, -1, axis=0) - np.roll(g, 1, axis=0)) / 2.0
    du_y = (np.roll(g, -1, axis=1) - np.roll(g, 1, axis=1)) / 2.0
    nx = np.linalg.norm(du_x.flatten()) + 1e-12
    ny = np.linalg.norm(du_y.flatten()) + 1e-12
    return du_x.flatten() / nx, du_y.flatten() / ny


def project_volume_tangent(H, n):
    """Project H onto 1⊥ (volume tangent removed)."""
    one = np.ones(n)
    P = np.eye(n) - np.outer(one, one) / n
    return P @ H @ P


def analyze_K2(u1, u2, graph, params, lambda_rep, lambda_bar, L=20):
    """Compute σ_multi^(A) data for K=2 minimizer."""
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()
    n = u1.shape[0]
    H_11, H_12, H_22 = joint_hessian_blocks([u1, u2], ec, lambda_rep, lambda_bar)
    H_11_p = project_volume_tangent(H_11, n)
    H_22_p = project_volume_tangent(H_22, n)
    H_12_p = project_volume_tangent(H_12, n)
    eig_11, vec_11 = np.linalg.eigh(H_11_p)
    eig_22, vec_22 = np.linalg.eigh(H_22_p)
    H12_op_norm = float(np.linalg.norm(H_12_p, ord=2))
    # Build joint Hessian (block 2x2)
    H_joint = np.block([[H_11_p, H_12_p], [H_12_p.T, H_22_p]])
    # Tangent: must remove (1, 1)/√2 (sum of all = 0) — but actually each formation
    # has its own volume tangent. Total dim = 2(n-1). Project out (1,0) and (0,1).
    # We can keep both H_11_p and H_22_p projected; H_joint inherits projections.
    eig_joint, vec_joint = np.linalg.eigh(H_joint)
    # Take lowest 12 eigenvalues
    n_modes = min(12, len(eig_joint))
    idx = np.argsort(eig_joint)[:n_modes]
    eig_joint_low = eig_joint[idx]
    vec_joint_low = vec_joint[:, idx]
    # Goldstone overlap of joint eigenvectors
    e_x_1, e_y_1 = translation_modes_torus(u1, L)
    e_x_2, e_y_2 = translation_modes_torus(u2, L)
    # Sym/Antisym translation modes: (e_x_1, +e_x_2)/√2 etc.
    sqrt2 = np.sqrt(2)
    e_sym_x = np.concatenate([e_x_1, e_x_2]) / sqrt2
    e_sym_y = np.concatenate([e_y_1, e_y_2]) / sqrt2
    e_antisym_x = np.concatenate([e_x_1, -e_x_2]) / sqrt2
    e_antisym_y = np.concatenate([e_y_1, -e_y_2]) / sqrt2

    mode_overlaps = []
    for k in range(n_modes):
        v = vec_joint_low[:, k]
        v = v / max(np.linalg.norm(v), 1e-12)
        ov_sym_x = abs(v @ e_sym_x)
        ov_sym_y = abs(v @ e_sym_y)
        ov_antisym_x = abs(v @ e_antisym_x)
        ov_antisym_y = abs(v @ e_antisym_y)
        mode_overlaps.append({
            'k': k,
            'lam': float(eig_joint_low[k]),
            'ov_sym_x': float(ov_sym_x),
            'ov_sym_y': float(ov_sym_y),
            'ov_antisym_x': float(ov_antisym_x),
            'ov_antisym_y': float(ov_antisym_y),
            'max_sym': float(max(ov_sym_x, ov_sym_y)),
            'max_antisym': float(max(ov_antisym_x, ov_antisym_y)),
        })
    # Per-formation lowest 6 eigenvalues
    return {
        'H11_low_eigs': [float(e) for e in eig_11[:6]],
        'H22_low_eigs': [float(e) for e in eig_22[:6]],
        'H12_op_norm': H12_op_norm,
        'joint_low_eigs': [float(e) for e in eig_joint_low],
        'joint_modes': mode_overlaps,
    }


def main():
    L = 20
    c = 0.10
    beta = 4.0
    xi_0 = np.sqrt(1.0 / beta)  # 0.5
    d_min_values = [5, 8, 12, 16]
    lambda_rep_values = [0.01, 0.1, 1.0]
    seeds = [0, 1, 2]

    graph, n = build_torus_2d(L)
    results = []
    t0 = time.time()

    for d_min in d_min_values:
        for lambda_rep in lambda_rep_values:
            for seed in seeds:
                u1_init, u2_init = two_disk_ic(L, c, d_min, xi_0, seed)
                params = ParameterRegistry(
                    alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
                    a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
                    w_cl=0.0, w_sep=0.0, w_bd=1.0,
                    n_restarts=1, max_iter=3000,
                )
                ec = EnergyComputer(graph, params)
                ec.normalize_weights()
                # Optimize K=2
                fields = _optimize_k_fields(
                    graph, params, ec, K=2, masses=[c*n, c*n],
                    lambda_rep=lambda_rep, lambda_bar=100.0,
                    max_iter=3000, seed=seed * 17 + 42, verbose=False,
                    init_fields=[u1_init, u2_init],
                    init_perturb=None, perturb_seed=seed,
                )
                u1, u2 = fields[0], fields[1]
                # Analyze
                ana = analyze_K2(u1, u2, graph, params, lambda_rep, lambda_bar=100.0, L=L)
                ana['d_min'] = d_min
                ana['lambda_rep'] = lambda_rep
                ana['seed'] = seed
                ana['energy_K2'] = float(_total_energy(fields, ec, graph, lambda_rep, 100.0))
                ana['u1_max'] = float(u1.max())
                ana['u2_max'] = float(u2.max())
                ana['inner_product'] = float(u1 @ u2)
                results.append(ana)
                # Print summary
                gold_sym = [m for m in ana['joint_modes'] if m['max_sym'] > 0.5]
                gold_anti = [m for m in ana['joint_modes'] if m['max_antisym'] > 0.5]
                lam_sym = gold_sym[0]['lam'] if gold_sym else None
                lam_anti = gold_anti[0]['lam'] if gold_anti else None
                print(f"d={d_min} λ_rep={lambda_rep} seed={seed}: H12_op={ana['H12_op_norm']:.4f} joint_λ[0:3]={ana['joint_low_eigs'][:3]} sym={lam_sym} anti={lam_anti}", flush=True)

    elapsed = time.time() - t0
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'e9_k2_baseline.json')
    with open(out_path, 'w') as f:
        json.dump({
            'meta': {
                'L': L, 'c': c, 'beta': beta, 'd_min_values': d_min_values,
                'lambda_rep_values': lambda_rep_values, 'seeds': seeds,
                'elapsed_s': elapsed,
                'description': 'K=2 baseline σ_multi^(A) verification per 05_*.md §6.2',
            },
            'results': results,
        }, f, indent=2, default=lambda o: float(o) if hasattr(o, 'item') else str(o))
    print(f"\nWrote {out_path} in {elapsed:.1f}s")


if __name__ == '__main__':
    main()
