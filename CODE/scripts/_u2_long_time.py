"""
_u2_long_time.py — NQ-233 Long-time α stabilization

Phase 9 U2: K=10 single shared-pool LSW, t_max=1000, log α(t) at multiple
time-windows.
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


def K_disks_ic(L, m_total, K, xi_0, seed=0):
    n = L * L
    rng = np.random.default_rng(seed)
    fields = []
    K_x = int(np.ceil(np.sqrt(K)))
    K_y = int(np.ceil(K / K_x))
    spacing = L / max(K_x, K_y)
    m_each = m_total / K
    r0 = max(0.7, np.sqrt(m_each / np.pi))
    placed = 0
    for i in range(K_x):
        for j in range(K_y):
            if placed >= K:
                break
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
    L = 30; K = 10; c_total = 0.20
    n = L*L; m_total = c_total * n
    beta = 4.0; lambda_rep = 0.5
    xi_0 = np.sqrt(1.0/beta)
    t_max = 1000.0; dt = 0.1  # larger dt for long run
    seed = 0

    graph, _ = build_torus_2d(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=m_total/(n*K),
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=2000,
    )
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    fields = K_disks_ic(L, m_total, K, xi_0, seed)
    fields = project_total_volume(fields, m_total)

    log = []
    n_steps = int(t_max / dt)
    log_every = max(1, n_steps // 100)
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
                'R_avg': avg_R(fields),
            })
    elapsed = time.time() - t0
    print(f"Total: t={t_max}, elapsed={elapsed:.1f}s, K_act final={log[-1]['K_active']}, R_avg final={log[-1]['R_avg']:.3f}", flush=True)

    # Multi-window α fit
    windows = [
        (5, 50), (10, 100), (50, 200), (100, 300), (200, 500),
        (300, 700), (500, 1000),
    ]
    alpha_per_window = {}
    for t_start, t_end in windows:
        ts = []; Rs = []
        for d in log:
            if t_start < d['t'] < t_end and d['R_avg'] > 0.5 and d['K_active'] > 0:
                ts.append(d['t'])
                Rs.append(d['R_avg'])
        if len(ts) > 5:
            coeffs = np.polyfit(np.log(ts), np.log(Rs), 1)
            alpha_per_window[f"{t_start}-{t_end}"] = float(coeffs[0])

    print("\n=== α per time window ===", flush=True)
    for window, alpha in alpha_per_window.items():
        print(f"  t∈[{window}]: α = {alpha:.3f}", flush=True)

    out = {
        'meta': {
            'L': L, 'K': K, 'c_total': c_total, 'beta': beta,
            'lambda_rep': lambda_rep, 't_max': t_max, 'dt': dt, 'seed': seed,
            'elapsed_s': elapsed,
        },
        'log': log,
        'alpha_per_window': alpha_per_window,
    }
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'u2_long_time.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {out_path}")


if __name__ == '__main__':
    main()
