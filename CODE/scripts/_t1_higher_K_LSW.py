"""
_t1_higher_K_LSW.py — Higher-K shared-pool LSW (K∈{5,10,15,20})

Phase 8 T1: Multiple K values to identify finite-K vs asymptotic α.
Each K with 3 seeds for statistical robustness.
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
            R = np.sqrt(mass_high / np.pi)
            Rs.append(R)
    return float(np.mean(Rs)) if Rs else 0.0


def run_K(L, K, m_total, beta, lambda_rep, lambda_bar, t_max, dt, seed):
    n = L * L
    xi_0 = np.sqrt(1.0 / beta)
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
    log_every = max(1, n_steps // 50)
    for step in range(n_steps):
        for j in range(K):
            grad = k_grad(fields, j, ec, lambda_rep, lambda_bar)
            fields[j] = fields[j] - dt * grad
        fields = project_total_volume(fields, m_total)
        if step % log_every == 0:
            log.append({
                't': step * dt,
                'K_active': count_active(fields),
                'R_avg': avg_R(fields),
            })
    return log


def main():
    L = 30
    Ks = [5, 10, 15, 20]
    c_total = 0.20
    n = L * L
    m_total = c_total * n  # 180 sites total
    beta = 4.0
    lambda_rep = 0.5
    lambda_bar = 100.0
    t_max = 200.0
    dt = 0.05
    seeds = [0, 1, 2]

    all_logs = {}
    t0_total = time.time()
    for K in Ks:
        print(f"\n=== K={K} (m_each={m_total/K:.1f}) ===", flush=True)
        for seed in seeds:
            print(f"  seed={seed}...", flush=True, end="")
            t0 = time.time()
            log = run_K(L, K, m_total, beta, lambda_rep, lambda_bar, t_max, dt, seed)
            elapsed = time.time() - t0
            all_logs[f"K={K}_seed={seed}"] = log
            K_init = log[0]['K_active'] if log else 0
            K_final = log[-1]['K_active'] if log else 0
            R_init = log[0]['R_avg'] if log else 0
            R_final = log[-1]['R_avg'] if log else 0
            print(f" K_act: {K_init} → {K_final}; R: {R_init:.2f} → {R_final:.2f}; t={elapsed:.1f}s", flush=True)

    # Aggregate per K, fit α
    print("\n=== α(K) from log-log fit ===", flush=True)
    fit_results = {}
    for K in Ks:
        # Combine seeds
        sample = all_logs[f"K={K}_seed=0"]
        ts = [d['t'] for d in sample]
        all_R = []
        all_t = []
        for s in seeds:
            log = all_logs[f"K={K}_seed={s}"]
            for d in log:
                if d['t'] > 5 and d['R_avg'] > 0.3 and d['K_active'] > 0:
                    all_t.append(d['t'])
                    all_R.append(d['R_avg'])
        all_t = np.array(all_t)
        all_R = np.array(all_R)
        if len(all_t) > 10:
            log_t = np.log(all_t)
            log_R = np.log(all_R)
            coeffs = np.polyfit(log_t, log_R, 1)
            alpha = float(coeffs[0])
            R0 = float(np.exp(coeffs[1]))
            fit_results[K] = {'alpha': alpha, 'R0': R0, 'n_pts': len(all_t)}
            print(f"K={K}: α = {alpha:.3f}, R₀ = {R0:.3f} ({len(all_t)} pts)", flush=True)
        else:
            fit_results[K] = None
            print(f"K={K}: insufficient data", flush=True)

    elapsed_total = time.time() - t0_total
    out = {
        'meta': {
            'L': L, 'Ks': Ks, 'c_total': c_total, 'm_total': m_total,
            'beta': beta, 'lambda_rep': lambda_rep, 'lambda_bar': lambda_bar,
            't_max': t_max, 'dt': dt, 'seeds': seeds,
            'elapsed_s': elapsed_total,
        },
        'fit_results': fit_results,
        'logs': all_logs,
    }
    out_path = os.path.join(os.path.dirname(__file__), 'results', 't1_higher_K_LSW.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {out_path} in {elapsed_total:.1f}s")


if __name__ == '__main__':
    main()
