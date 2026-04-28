"""
_v5_3D_torus.py — 3D Torus T³_L σ-framework verification

Phase 10 V5: K=4 on T³_8 (n=512) shared-pool LSW.
Verify: (a) 3D σ_multi^A structure works; (b) 3D LSW α prediction (=1/3 classical).
"""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
import scipy.sparse as sp
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer


def build_torus_3d(L):
    """3D torus T^3_L, periodic in all 3 dims."""
    n = L * L * L
    edges = []
    for i in range(L):
        for j in range(L):
            for k in range(L):
                idx = i * L * L + j * L + k
                idx_x = ((i + 1) % L) * L * L + j * L + k
                idx_y = i * L * L + ((j + 1) % L) * L + k
                idx_z = i * L * L + j * L + (k + 1) % L
                edges.append((idx, idx_x))
                edges.append((idx, idx_y))
                edges.append((idx, idx_z))
    rows = [a for a, b in edges] + [b for a, b in edges]
    cols = [b for a, b in edges] + [a for a, b in edges]
    W = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    return GraphState(W), n


def K_disks_3d_ic(L, m_each, K, xi_0, seed=0):
    n = L * L * L
    rng = np.random.default_rng(seed)
    fields = []
    # Place K disks on a coarse 3D grid
    K_per_dim = int(np.ceil(K**(1/3)))
    spacing = L / K_per_dim
    r0 = max(0.5, (m_each * 3 / (4 * np.pi))**(1/3))  # 3D ball radius
    placed = 0
    for ii in range(K_per_dim):
        for jj in range(K_per_dim):
            for kk in range(K_per_dim):
                if placed >= K: break
                cx = (ii + 0.5) * spacing + rng.normal(0, 0.3)
                cy = (jj + 0.5) * spacing + rng.normal(0, 0.3)
                cz = (kk + 0.5) * spacing + rng.normal(0, 0.3)
                i_idx, j_idx, k_idx = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing='ij')
                dx = np.minimum(np.abs(i_idx - cx), L - np.abs(i_idx - cx))
                dy = np.minimum(np.abs(j_idx - cy), L - np.abs(j_idx - cy))
                dz = np.minimum(np.abs(k_idx - cz), L - np.abs(k_idx - cz))
                r = np.sqrt(dx**2 + dy**2 + dz**2).flatten()
                u = 0.5 * (1.0 - np.tanh((r - r0) / xi_0))
                u = np.clip(u + rng.normal(0, 0.02, n), 0.01, 0.99)
                fields.append(u)
                placed += 1
            if placed >= K: break
        if placed >= K: break
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


def count_active(fields, threshold=0.5):
    return sum(1 for u in fields if u.max() > threshold)


def avg_R_3d(fields, threshold=0.5):
    Rs = []
    for u in fields:
        if u.max() > threshold:
            mass_high = (u > threshold).sum()
            R = (mass_high * 3 / (4 * np.pi))**(1/3)  # 3D ball
            Rs.append(R)
    return float(np.mean(Rs)) if Rs else 0.0


def main():
    L = 10; K = 4
    n = L*L*L  # 1000
    c_total = 0.30  # larger fraction for viable 3D formations
    m_total = c_total * n  # 300
    beta = 4.0; lambda_rep = 0.3
    xi_0 = np.sqrt(1.0/beta)
    t_max = 100.0; dt = 0.05
    seeds = [0, 1]

    graph, _ = build_torus_3d(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=m_total/(n*K),
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=2000,
    )
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    all_logs = {}
    t0_total = time.time()
    for seed in seeds:
        print(f"=== T³_{L} K={K} seed={seed} ===", flush=True)
        fields = K_disks_3d_ic(L, m_total/K, K, xi_0, seed)
        fields = project_total_volume(fields, m_total)

        log = []
        n_steps = int(t_max / dt)
        log_every = max(1, n_steps // 30)
        t0 = time.time()
        for step in range(n_steps):
            for j in range(K):
                grad = k_grad(fields, j, ec, lambda_rep, 100.0)
                fields[j] = fields[j] - dt * grad
            fields = project_total_volume(fields, m_total)
            if step % log_every == 0:
                log.append({
                    't': step * dt,
                    'K_active': count_active(fields),
                    'R_avg': avg_R_3d(fields),
                })
        elapsed = time.time() - t0
        print(f"  K_act {log[0]['K_active']}→{log[-1]['K_active']}, R {log[0]['R_avg']:.2f}→{log[-1]['R_avg']:.2f}, t={elapsed:.1f}s", flush=True)
        all_logs[f"seed={seed}"] = log

    # Fit α
    all_t = []; all_R = []
    for s in seeds:
        log = all_logs[f"seed={s}"]
        for d in log:
            if d['t'] > 5 and d['R_avg'] > 0.3 and d['K_active'] > 0:
                all_t.append(d['t'])
                all_R.append(d['R_avg'])
    if len(all_t) > 5:
        coeffs = np.polyfit(np.log(all_t), np.log(all_R), 1)
        alpha = float(coeffs[0])
        print(f"\n3D LSW α = {alpha:.3f} (classical 3D LSW: 0.333)", flush=True)
    else:
        alpha = None

    elapsed_total = time.time() - t0_total
    out = {
        'meta': {
            'L': L, 'K': K, 'n': n, 'c_total': c_total, 'm_total': m_total,
            'beta': beta, 'lambda_rep': lambda_rep,
            't_max': t_max, 'dt': dt, 'seeds': seeds,
            'elapsed_s': elapsed_total,
            'dimension': 3,
        },
        'alpha_3D': alpha,
        'logs': all_logs,
    }
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'v5_3D_torus.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {out_path}")


if __name__ == '__main__':
    main()
