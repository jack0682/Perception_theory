"""
_f8_K3_baseline.py — K=3 σ_multi^(A) baseline

Phase 4 F8: Verify σ_multi^(A) extension to K=3 with three disks at triangular config.
Joint Hessian decomposition: σ_1, σ_2, σ_3, σ_12, σ_13, σ_23.
"""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
import scipy.sparse as sp
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.multi import _optimize_k_fields


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


def K3_triangular_ic(L, c, xi_0, seed=0):
    """Three disks at vertices of equilateral triangle on torus."""
    n = L * L
    rng = np.random.default_rng(seed)
    # Triangle vertices around (L/2, L/2) with radius L/4
    angles = [np.pi/2, np.pi/2 + 2*np.pi/3, np.pi/2 + 4*np.pi/3]
    radius = L / 4.0
    centers = [
        ((L/2 + radius * np.cos(a)) % L, (L/2 + radius * np.sin(a)) % L)
        for a in angles
    ]
    fields = []
    r0 = np.sqrt(c * L * L / np.pi)
    i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
    for cx, cy in centers:
        dx = np.minimum(np.abs(i_idx - cx), L - np.abs(i_idx - cx))
        dy = np.minimum(np.abs(j_idx - cy), L - np.abs(j_idx - cy))
        r = np.sqrt(dx**2 + dy**2).flatten()
        u = 0.5 * (1.0 - np.tanh((r - r0) / xi_0))
        u = np.clip(u + rng.normal(0, 0.02, n), 0.01, 0.99)
        fields.append(u)
    return fields


def k_grad(fields, j, ec, lambda_rep, lambda_bar):
    K = len(fields)
    g_intra = ec.gradient(fields[j])
    g_rep = lambda_rep * sum(fields[k] for k in range(K) if k != j)
    S = sum(fields)
    g_bar = 2.0 * lambda_bar * np.maximum(0.0, S - 1.0)
    return g_intra + g_rep + g_bar


def joint_hessian_K3(fields, ec, lambda_rep, lambda_bar, eps=1e-4):
    n = fields[0].shape[0]
    K = 3
    g0 = [k_grad(fields, j, ec, lambda_rep, lambda_bar) for j in range(K)]
    H = [[np.zeros((n, n)) for _ in range(K)] for _ in range(K)]
    for k_p in range(K):
        for i in range(n):
            fp = [u.copy() for u in fields]
            fp[k_p][i] += eps
            for j in range(K):
                g_p = k_grad(fp, j, ec, lambda_rep, lambda_bar)
                H[j][k_p][:, i] = (g_p - g0[j]) / eps
    return H


def main():
    L = 20; c = 0.10; beta = 4.0; xi_0 = 0.5
    K = 3
    lambda_rep = 0.1
    seed = 0
    graph, n = build_torus_2d(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=2000,
    )
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    fields_init = K3_triangular_ic(L, c, xi_0, seed)
    print(f"K=3 IC: u_max per formation: {[float(u.max()) for u in fields_init]}", flush=True)

    t0 = time.time()
    fields = _optimize_k_fields(
        graph, params, ec, K=3, masses=[c*n, c*n, c*n],
        lambda_rep=lambda_rep, lambda_bar=100.0,
        max_iter=2000, seed=42, verbose=False,
        init_fields=fields_init,
        init_perturb=None, perturb_seed=0,
    )
    print(f"K=3 optimized in {time.time()-t0:.1f}s, u_max: {[float(u.max()) for u in fields]}", flush=True)
    print(f"Inner products: <1,2>={fields[0]@fields[1]:.3f}, <1,3>={fields[0]@fields[2]:.3f}, <2,3>={fields[1]@fields[2]:.3f}", flush=True)

    # Joint Hessian
    t1 = time.time()
    H = joint_hessian_K3(fields, ec, lambda_rep, 100.0)
    print(f"Joint Hessian computed in {time.time()-t1:.1f}s", flush=True)

    # Project, extract eigvals
    one = np.ones(n)
    P = np.eye(n) - np.outer(one, one) / n
    H_proj = [[P @ H[j][k] @ P for k in range(K)] for j in range(K)]

    # Per-formation H_jj
    eigs_per = []
    for j in range(K):
        eigs = np.linalg.eigvalsh(H_proj[j][j])[:6]
        eigs_per.append([float(e) for e in eigs])
        print(f"H_{j}{j} low eigvals: {eigs[:4]}", flush=True)

    # Cross-block op-norms
    op_norms = {}
    for j in range(K):
        for k in range(j+1, K):
            op_norms[f"H_{j}{k}"] = float(np.linalg.norm(H_proj[j][k], ord=2))
    print(f"Cross-block op-norms: {op_norms}", flush=True)

    # Joint Hessian (3K x 3K block matrix)
    big = np.zeros((K*n, K*n))
    for j in range(K):
        for k in range(K):
            big[j*n:(j+1)*n, k*n:(k+1)*n] = H_proj[j][k]
    eig_joint = np.linalg.eigvalsh(big)[:18]
    print(f"Joint H lowest 12: {[round(float(e), 4) for e in eig_joint[:12]]}", flush=True)

    out_path = os.path.join(os.path.dirname(__file__), 'results', 'f8_K3_baseline.json')
    with open(out_path, 'w') as f:
        json.dump({
            'meta': {
                'L': L, 'c': c, 'K': K, 'beta': beta, 'lambda_rep': lambda_rep,
                'config': 'triangular',
            },
            'u_max_per_formation': [float(u.max()) for u in fields],
            'inner_products': {
                '12': float(fields[0]@fields[1]),
                '13': float(fields[0]@fields[2]),
                '23': float(fields[1]@fields[2]),
            },
            'H_jj_low_eigs': eigs_per,
            'cross_block_op_norms': op_norms,
            'joint_low_eigs': [float(e) for e in eig_joint],
        }, f, indent=2)
    print(f"Wrote {out_path}")


if __name__ == '__main__':
    main()
