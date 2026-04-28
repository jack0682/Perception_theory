"""
_p1_2_F7_refined.py — Refined K-sweep for LSW scaling

Phase 5 P1.2 (resolves Phase 4 W2): K ∈ {3, 5} with proper m_each (in-spinodal
per-formation), longer evolution, R(t) tracking.
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
    r0 = np.sqrt(m_each / np.pi)
    placed = 0
    for i in range(K_x):
        for j in range(K_y):
            if placed >= K:
                break
            cx = (i + 0.5) * spacing + rng.normal(0, 0.3)
            cy = (j + 0.5) * spacing + rng.normal(0, 0.3)
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


def project_volume(u, m):
    u = u + (m - u.sum()) / len(u)
    u = np.clip(u, 0, 1)
    for _ in range(5):
        u = u + (m - u.sum()) / len(u)
        u = np.clip(u, 0, 1)
    return u


def count_active(fields, threshold=0.5):
    """Count formations with at least one site above threshold."""
    return sum(1 for u in fields if u.max() > threshold)


def avg_R(fields, threshold=0.5):
    Rs = []
    for u in fields:
        if u.max() > threshold:
            mass_high = (u > threshold).sum()
            R = np.sqrt(mass_high / np.pi)
            Rs.append(R)
    return float(np.mean(Rs)) if Rs else 0.0


def run_K(L, K, m_each, beta, lambda_rep, t_max=500.0, dt=0.02, seed=0):
    """Run a single K simulation."""
    n = L * L
    xi_0 = np.sqrt(1.0 / beta)
    graph, _ = build_torus_2d(L)
    c_per = m_each / n
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c_per,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=2000,
    )
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()
    fields = K_disks_ic(L, m_each, K, xi_0, seed)
    fields = [project_volume(u, m_each) for u in fields]

    log = []
    n_steps = int(t_max / dt)
    log_every = max(1, n_steps // 100)
    for step in range(n_steps):
        for j in range(K):
            grad = k_grad(fields, j, ec, lambda_rep, 100.0)
            grad = grad - grad.mean()
            fields[j] = fields[j] - dt * grad
            fields[j] = project_volume(fields[j], m_each)
        if step % log_every == 0:
            log.append({
                't': step * dt,
                'K_active': count_active(fields),
                'R_avg': avg_R(fields),
                'u_max_max': float(max(u.max() for u in fields)),
            })
    return log


def main():
    L = 24
    Ks = [3, 5]  # spinodal-friendly K
    # m_each chosen so c_per = m_each/n ∈ spinodal: c_per ∈ (0.21, 0.79).
    # For K=3 on L=24 (n=576): c_per = 0.25 → m_each = 144. Total mass = 432 (ok).
    # For K=5: c_per = 0.20 (just under spinodal). Use 0.22 to be safe → m_each = 127.
    K_to_meach = {3: 140, 5: 130}
    beta = 4.0
    lambda_rep = 0.05
    seeds = [0, 1, 2]

    all_logs = {}
    t0_total = time.time()
    for K in Ks:
        m_each = K_to_meach[K]
        c_per = m_each / (L*L)
        print(f"K={K}, m_each={m_each}, c_per={c_per:.3f}", flush=True)
        if c_per < 0.21:
            print(f"  WARNING: c_per below spinodal, may need allow_outside_spinodal", flush=True)
        for seed in seeds:
            print(f"  seed={seed}...", flush=True)
            t0 = time.time()
            log = run_K(L, K, m_each, beta, lambda_rep, t_max=200, dt=0.02, seed=seed)
            elapsed = time.time() - t0
            all_logs[f"K={K}_seed={seed}"] = log
            K_init = log[0]['K_active'] if log else 0
            K_final = log[-1]['K_active'] if log else 0
            R_init = log[0]['R_avg'] if log else 0
            R_final = log[-1]['R_avg'] if log else 0
            print(f"    K_act: {K_init} → {K_final}; R: {R_init:.2f} → {R_final:.2f}; t={elapsed:.1f}s", flush=True)

    # Aggregate
    print("\n=== Aggregated R(t) and K_active(t) ===", flush=True)
    for K in Ks:
        print(f"\nK={K}:")
        # Average over seeds at common time points
        sample_log = all_logs[f"K={K}_seed=0"]
        ts = [d['t'] for d in sample_log]
        for t_idx in range(0, len(ts), max(1, len(ts)//10)):
            t = ts[t_idx]
            K_act_seeds = [all_logs[f"K={K}_seed={s}"][t_idx]['K_active'] for s in seeds]
            R_seeds = [all_logs[f"K={K}_seed={s}"][t_idx]['R_avg'] for s in seeds]
            print(f"  t={t:6.2f}: K_act_mean={np.mean(K_act_seeds):.2f} R_avg_mean={np.mean(R_seeds):.3f}")

    elapsed_total = time.time() - t0_total
    out = {
        'meta': {
            'L': L, 'beta': beta, 'lambda_rep': lambda_rep,
            'Ks': Ks, 'K_to_meach': K_to_meach,
            'seeds': seeds, 't_max': 200.0, 'dt': 0.02,
            'elapsed_s': elapsed_total,
        },
        'logs': all_logs,
    }
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'p1_2_F7_refined.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {out_path} in {elapsed_total:.1f}s")


if __name__ == '__main__':
    main()
