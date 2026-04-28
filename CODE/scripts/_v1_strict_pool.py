"""
_v1_strict_pool.py — NQ-240 STRICT per-formation pool (no relaxation)

Phase 10 V1: m_j strictly fixed throughout. Each formation has independent
volume m_j = m_total/K, projection to m_j only (no shared-pool relaxation).
Verify α ≈ 0 (no LSW under strict per-formation).
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
            # Strict m_each volume per formation
            u = u + (m_each - u.sum()) / n
            u = np.clip(u, 0, 1)
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


def project_strict(u, m):
    """STRICT per-formation projection: u sums to m exactly."""
    u = u + (m - u.sum()) / len(u)
    u = np.clip(u, 0, 1)
    for _ in range(5):
        u = u + (m - u.sum()) / len(u)
        u = np.clip(u, 0, 1)
    return u


def count_active(fields, threshold=0.5):
    return sum(1 for u in fields if u.max() > threshold)


def avg_R(fields, threshold=0.5):
    Rs = []
    for u in fields:
        if u.max() > threshold:
            mass_high = (u > threshold).sum()
            Rs.append(np.sqrt(mass_high / np.pi))
    return float(np.mean(Rs)) if Rs else 0.0


def main():
    L = 30; K = 8
    n = L*L
    c_total = 0.20
    m_total = c_total * n
    m_each = m_total / K  # = 22.5 per formation, STRICTLY FIXED
    beta = 4.0; lambda_rep = 0.5
    xi_0 = np.sqrt(1.0/beta)
    t_max = 200.0; dt = 0.05
    seeds = [0, 1, 2]

    graph, _ = build_torus_2d(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=m_each/n,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=2000,
    )
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    all_logs = {}
    t0_total = time.time()
    for seed in seeds:
        print(f"=== seed={seed} (STRICT m_j={m_each:.1f}) ===", flush=True)
        fields = K_disks_ic(L, m_each, K, xi_0, seed)
        fields = [project_strict(u, m_each) for u in fields]

        log = []
        n_steps = int(t_max / dt)
        log_every = max(1, n_steps // 50)
        t0 = time.time()
        for step in range(n_steps):
            for j in range(K):
                grad = k_grad(fields, j, ec, lambda_rep, 100.0)
                fields[j] = fields[j] - dt * grad
                # STRICT per-formation projection (no shared pool)
                fields[j] = project_strict(fields[j], m_each)
            if step % log_every == 0:
                log.append({
                    't': step * dt,
                    'K_active': count_active(fields),
                    'R_avg': avg_R(fields),
                    'mass_check': [float(u.sum()) for u in fields],
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
        print(f"\nSTRICT pool α = {alpha:.3f} ({len(all_t)} pts)", flush=True)
    else:
        alpha = None

    # Mass conservation check
    print(f"\nMass conservation check (final):", flush=True)
    for s in seeds:
        log = all_logs[f"seed={s}"]
        masses = log[-1]['mass_check']
        print(f"  seed={s}: masses = {[f'{m:.3f}' for m in masses]}, all ≈ {m_each:.2f}", flush=True)

    elapsed_total = time.time() - t0_total
    out = {
        'meta': {
            'L': L, 'K': K, 'c_total': c_total, 'm_each': m_each,
            'beta': beta, 'lambda_rep': lambda_rep,
            't_max': t_max, 'dt': dt, 'seeds': seeds,
            'elapsed_s': elapsed_total,
            'architecture': 'STRICT per-formation pool',
        },
        'alpha': alpha,
        'logs': all_logs,
    }
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'v1_strict_pool.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {out_path}")


if __name__ == '__main__':
    main()
