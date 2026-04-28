"""
_f5_param_grid.py — σ_multi^(A) parameter grid Cat A extension

Phase 4 F5: extend σ_multi^(A) verification across (L, c, K) grid.
Use proper allow_outside_spinodal=True kwarg (post-F17 patch).
"""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
import scipy.sparse as sp
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.multi import _optimize_k_fields, _total_energy


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


def k_grad(fields, j, ec, lambda_rep, lambda_bar):
    K = len(fields)
    g_intra = ec.gradient(fields[j])
    g_rep = lambda_rep * sum(fields[k] for k in range(K) if k != j)
    S = sum(fields)
    g_bar = 2.0 * lambda_bar * np.maximum(0.0, S - 1.0)
    return g_intra + g_rep + g_bar


def joint_hessian_blocks(fields, ec, lambda_rep, lambda_bar, eps=1e-4):
    n = fields[0].shape[0]
    K = len(fields)
    g0 = [k_grad(fields, j, ec, lambda_rep, lambda_bar) for j in range(K)]
    H = [[np.zeros((n, n)) for _ in range(K)] for _ in range(K)]
    for k_p in range(K):
        for i in range(n):
            fp = [u.copy() for u in fields]
            fp[k_p][i] += eps
            for j in range(K):
                g_p = k_grad(fp, j, ec, lambda_rep, lambda_bar)
                H[j][k_p][:, i] = (g_p - g0[j]) / eps
    return [(H[j][j] + H[j][j].T) / 2 for j in range(K)], [(H[j][k] + H[k][j].T) / 2 for k in range(K) for j in range(k)]


def main():
    Ls = [16, 20, 24]
    cs = [0.10, 0.15]
    beta = 4.0
    xi_0 = 0.5
    lambda_rep = 0.1
    seeds = [0, 1, 2]
    results = []
    t0 = time.time()
    for L in Ls:
        for c in cs:
            d_min = max(5, L // 3)  # adaptive d_min by L
            graph, n = build_torus_2d(L)
            for seed in seeds:
                u1_init, u2_init = two_disk_ic(L, c, d_min, xi_0, seed)
                params = ParameterRegistry(
                    alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
                    a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
                    w_cl=0.0, w_sep=0.0, w_bd=1.0,
                    n_restarts=1, max_iter=2000,
                )
                # Use allow_outside_spinodal in validate
                valid, V, W = params.validate(
                    fiedler_eigenvalue=graph.fiedler,
                    allow_outside_spinodal=True,
                )
                if not valid:
                    print(f"L={L} c={c} seed={seed}: INVALID {V}", flush=True)
                    continue
                ec = EnergyComputer(graph, params)
                ec.normalize_weights()
                fields = _optimize_k_fields(
                    graph, params, ec, K=2, masses=[c*n, c*n],
                    lambda_rep=lambda_rep, lambda_bar=100.0,
                    max_iter=2000, seed=seed * 17 + 42, verbose=False,
                    init_fields=[u1_init, u2_init],
                    init_perturb=None, perturb_seed=seed,
                )
                u1, u2 = fields
                # Joint Hessian
                Hjj_list, Hjk_list = joint_hessian_blocks(fields, ec, lambda_rep, 100.0)
                H11, H22 = Hjj_list[0], Hjj_list[1]
                H12 = Hjk_list[0]
                # Project out volume tangent
                one = np.ones(n)
                P = np.eye(n) - np.outer(one, one) / n
                H11p = P @ H11 @ P
                H22p = P @ H22 @ P
                H12p = P @ H12 @ P
                eig11 = np.linalg.eigvalsh(H11p)[:6]
                eig22 = np.linalg.eigvalsh(H22p)[:6]
                # Joint
                Hjoint = np.block([[H11p, H12p], [H12p.T, H22p]])
                eig_joint = np.linalg.eigvalsh(Hjoint)[:6]
                results.append({
                    'L': L, 'c': c, 'seed': seed, 'd_min': d_min,
                    'lambda_rep': lambda_rep,
                    'u1_max': float(u1.max()), 'u2_max': float(u2.max()),
                    'inner_product': float(u1 @ u2),
                    'H12_op_norm': float(np.linalg.norm(H12p, ord=2)),
                    'H11_low_eigs': [float(e) for e in eig11],
                    'H22_low_eigs': [float(e) for e in eig22],
                    'joint_low_eigs': [float(e) for e in eig_joint],
                })
                # Compute c_eff: |joint λ_min| / λ_rep
                c_eff = abs(eig_joint[0]) / lambda_rep
                print(f"L={L} c={c} seed={seed}: H12_op={float(np.linalg.norm(H12p,ord=2)):.4f} joint_λ_min={eig_joint[0]:.4f} c_eff={c_eff:.3f}", flush=True)
    elapsed = time.time() - t0
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'f5_param_grid.json')
    with open(out_path, 'w') as f:
        json.dump({
            'meta': {
                'Ls': Ls, 'cs': cs, 'beta': beta, 'lambda_rep': lambda_rep,
                'seeds': seeds, 'elapsed_s': elapsed,
                'description': 'F5: σ_multi^(A) parameter grid (L, c) sweep',
            },
            'results': results,
        }, f, indent=2)
    print(f"\nWrote {out_path} in {elapsed:.1f}s")


if __name__ == '__main__':
    main()
