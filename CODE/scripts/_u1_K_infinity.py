"""
_u1_K_infinity.py — NQ-235 K → ∞ thermodynamic extrapolation

Phase 9 U1: K ∈ {5, 10, 15, 20, 30, 40} on T²_{40} shared-pool LSW.
Fit α(K) = α_∞ + B/K^p; extract α_∞.
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


def run_K(L, K, m_total, beta, lambda_rep, t_max, dt, seed):
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
    log_every = max(1, n_steps // 40)
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
    return log


def main():
    L = 40
    Ks = [5, 10, 15, 20, 30, 40]
    c_total = 0.20
    n = L * L
    m_total = c_total * n  # 320
    beta = 4.0
    lambda_rep = 0.5
    t_max = 150.0; dt = 0.05
    seeds = [0, 1, 2]

    fit_results = {}
    all_logs = {}
    t0 = time.time()
    for K in Ks:
        m_each = m_total / K
        print(f"\n=== K={K} (m_each={m_each:.1f}) ===", flush=True)
        for seed in seeds:
            t_cfg = time.time()
            log = run_K(L, K, m_total, beta, lambda_rep, t_max, dt, seed)
            elapsed = time.time() - t_cfg
            all_logs[f"K={K}_seed={seed}"] = log
            print(f"  seed={seed}: K_act {log[0]['K_active']}→{log[-1]['K_active']}, R {log[0]['R_avg']:.2f}→{log[-1]['R_avg']:.2f}, t={elapsed:.1f}s", flush=True)
        # Fit
        all_t = []; all_R = []
        for s in seeds:
            log = all_logs[f"K={K}_seed={s}"]
            for d in log:
                if d['t'] > 5 and d['R_avg'] > 0.3 and d['K_active'] > 0:
                    all_t.append(d['t'])
                    all_R.append(d['R_avg'])
        if len(all_t) > 5:
            coeffs = np.polyfit(np.log(all_t), np.log(all_R), 1)
            alpha = float(coeffs[0])
            fit_results[K] = alpha
            print(f"  α(K={K}) = {alpha:.3f}", flush=True)

    # Asymptotic fit α(K) = α_∞ + B/K^p
    Ks_arr = np.array(sorted(fit_results.keys()))
    alphas_arr = np.array([fit_results[k] for k in Ks_arr])
    # Fit α(K) = α_∞ + B/K
    if len(Ks_arr) >= 3:
        A = np.column_stack([np.ones(len(Ks_arr)), 1.0/Ks_arr])
        sol, *_ = np.linalg.lstsq(A, alphas_arr, rcond=None)
        alpha_inf = float(sol[0])
        B = float(sol[1])
        print(f"\n=== α(K) = {alpha_inf:.3f} + {B:.3f}/K ===", flush=True)
        print(f"α_∞ extrapolation: {alpha_inf:.3f}", flush=True)
    else:
        alpha_inf = None
        B = None

    elapsed = time.time() - t0
    out = {
        'meta': {
            'L': L, 'Ks': Ks, 'c_total': c_total, 'm_total': m_total,
            'beta': beta, 'lambda_rep': lambda_rep,
            't_max': t_max, 'dt': dt, 'seeds': seeds,
            'elapsed_s': elapsed,
        },
        'fit_alpha_per_K': fit_results,
        'alpha_infinity_fit': {'alpha_inf': alpha_inf, 'B': B},
        'logs': all_logs,
    }
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'u1_K_infinity.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {out_path} in {elapsed:.1f}s")


if __name__ == '__main__':
    main()
