"""
_v3_hessian_sigma.py — V3: Hessian-based σ_multi^A at sparse time samples

Phase 10 V3: K=8, T²_20 (smaller for tractability), shared-pool LSW.
Compute joint Hessian + extract σ-tuple at SPARSE time samples (~10 snapshots).
"""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
import scipy.sparse as sp
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer


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


def K_disks_ic(L, m_each, K, xi_0, seed=0):
    n = L * L
    rng = np.random.default_rng(seed)
    fields = []
    K_x = int(np.ceil(np.sqrt(K)))
    K_y = int(np.ceil(K / K_x))
    spacing = L / max(K_x, K_y)
    r0 = max(0.7, np.sqrt(m_each / np.pi))
    placed = 0
    for i in range(K_x):
        for j in range(K_y):
            if placed >= K: break
            cx = (i + 0.5) * spacing + rng.normal(0, 0.5)
            cy = (j + 0.5) * spacing + rng.normal(0, 0.5)
            i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
            dx = np.minimum(np.abs(i_idx - cx), L - np.abs(i_idx - cx))
            dy = np.minimum(np.abs(j_idx - cy), L - np.abs(j_idx - cy))
            r = np.sqrt(dx**2 + dy**2).flatten()
            u = 0.5 * (1.0 - np.tanh((r - r0) / xi_0))
            u = np.clip(u + rng.normal(0, 0.02, n), 0.01, 0.99)
            fields.append(u)
            placed += 1
    return fields[:K]


def k_grad(fields, j, ec, lambda_rep, lambda_bar):
    K = len(fields)
    g_intra = ec.gradient(fields[j])
    g_rep = lambda_rep * sum(fields[k] for k in range(K) if k != j)
    S = sum(fields)
    g_bar = 2.0 * lambda_bar * np.maximum(0.0, S - 1.0)
    return g_intra + g_rep + g_bar


def project_total_volume(fields, m_total):
    K = len(fields)
    n = fields[0].shape[0]
    for _ in range(3):
        current_total = sum(u.sum() for u in fields)
        delta = (m_total - current_total) / (K * n)
        fields = [np.clip(u + delta, 0, 1) for u in fields]
    return fields


def compute_hessian_one_formation(u, graph, params, eps=1e-3):
    """Per-formation Hessian via FD on intra-energy."""
    n = u.shape[0]
    from scc.energy import grad_bd
    g0 = grad_bd(u, graph, params)
    H = np.zeros((n, n))
    for i in range(n):
        u_p = u.copy()
        u_p[i] += eps
        g_p = grad_bd(u_p, graph, params)
        H[:, i] = (g_p - g0) / eps
    H = (H + H.T) / 2.0
    return H


def hessian_sigma_per_formation(u, graph, params, n_modes=4):
    """Per-formation σ-tuple: lowest n_modes Hessian eigvals + Goldstone overlaps."""
    n = u.shape[0]
    H = compute_hessian_one_formation(u, graph, params)
    one = np.ones(n)
    P = np.eye(n) - np.outer(one, one) / n
    H_proj = P @ H @ P
    eigvals, eigvecs = np.linalg.eigh(H_proj)
    sorted_idx = np.argsort(eigvals)
    low_eigs = [float(eigvals[sorted_idx[i]]) for i in range(n_modes)]
    return {'low_eigvals': low_eigs, 'u_max': float(u.max()), 'u_mass': float(u.sum())}


def main():
    L = 20; K = 8  # smaller L for tractability
    n = L*L
    c_total = 0.20
    m_total = c_total * n  # 80
    beta = 4.0; lambda_rep = 0.5
    xi_0 = np.sqrt(1.0/beta)
    t_max = 100.0; dt = 0.05
    seed = 0
    n_hess_samples = 10  # only 10 Hessian computations

    graph, _ = build_torus_2d(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=m_total/(n*K),
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=2000,
    )
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    fields = K_disks_ic(L, m_total/K, K, xi_0, seed)
    fields = project_total_volume(fields, m_total)

    n_steps = int(t_max / dt)
    hess_steps = [int(i * n_steps / n_hess_samples) for i in range(n_hess_samples + 1)]
    hess_log = []
    t0 = time.time()
    for step in range(n_steps + 1):
        if step in hess_steps:
            t_now = step * dt
            t_h = time.time()
            sigma_K = []
            for j in range(K):
                if fields[j].max() > 0.3:  # active formations only
                    sigma_j = hessian_sigma_per_formation(fields[j], graph, params)
                    sigma_K.append(sigma_j)
            print(f"t={t_now:.1f}: {len(sigma_K)} active formations, Hessian time {time.time()-t_h:.1f}s", flush=True)
            for j_idx, s in enumerate(sigma_K):
                print(f"  σ_{j_idx}: low_eigs={[f'{e:.4f}' for e in s['low_eigvals']]}, m={s['u_mass']:.2f}", flush=True)
            hess_log.append({
                't': t_now,
                'K_active': len(sigma_K),
                'sigmas': sigma_K,
            })
        if step < n_steps:
            for j in range(K):
                grad = k_grad(fields, j, ec, lambda_rep, 100.0)
                fields[j] = fields[j] - dt * grad
            fields = project_total_volume(fields, m_total)

    elapsed = time.time() - t0
    out = {
        'meta': {
            'L': L, 'K': K, 'c_total': c_total, 'beta': beta,
            'lambda_rep': lambda_rep, 't_max': t_max, 'dt': dt,
            'seed': seed, 'n_hess_samples': n_hess_samples,
            'elapsed_s': elapsed,
        },
        'hess_log': hess_log,
    }
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'v3_hessian_sigma.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {out_path} in {elapsed:.1f}s")


if __name__ == '__main__':
    main()
