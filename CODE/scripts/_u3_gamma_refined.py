"""
_u3_gamma_refined.py — NQ-229b refined γ* fit

Phase 9 U3: γ ∈ {0, 0.03, 0.05, 0.07, 0.1, 0.15, 0.2, 0.3, 0.5, 1.0}
at (β, c) ∈ {(4, 0.10), (4, 0.20), (8, 0.10)}. Fit γ*(β, c).
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


def hybrid_project(fields, m_total, m_per_target, gamma, dt):
    K = len(fields)
    n = fields[0].shape[0]
    m_actual = [u.sum() for u in fields]
    m_total_actual = sum(m_actual)
    m_per_shared = m_total_actual / K
    m_target = [(1 - gamma * dt) * m_actual[j] + gamma * dt * m_per_shared for j in range(K)]
    correction = (m_total - sum(m_target)) / K
    m_target = [m + correction for m in m_target]
    fields_proj = []
    for j, u in enumerate(fields):
        u_proj = u + (m_target[j] - u.sum()) / n
        u_proj = np.clip(u_proj, 0, 1)
        for _ in range(2):
            u_proj = u_proj + (m_target[j] - u_proj.sum()) / n
            u_proj = np.clip(u_proj, 0, 1)
        fields_proj.append(u_proj)
    return fields_proj


def count_active(fields, threshold=0.5):
    return sum(1 for u in fields if u.max() > threshold)


def avg_R(fields, threshold=0.5):
    Rs = []
    for u in fields:
        if u.max() > threshold:
            mass_high = (u > threshold).sum()
            Rs.append(np.sqrt(mass_high / np.pi))
    return float(np.mean(Rs)) if Rs else 0.0


def run_gamma(L, K, m_total, beta, lambda_rep, gamma, t_max=80.0, dt=0.05, seed=0):
    n = L * L
    xi_0 = np.sqrt(1.0/beta)
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
    m_per_init = m_total / K
    for j in range(K):
        fields[j] = fields[j] + (m_per_init - fields[j].sum()) / n
        fields[j] = np.clip(fields[j], 0, 1)

    log = []
    n_steps = int(t_max / dt)
    log_every = max(1, n_steps // 30)
    for step in range(n_steps):
        for j in range(K):
            grad = k_grad(fields, j, ec, lambda_rep, 100.0)
            fields[j] = fields[j] - dt * grad
        fields = hybrid_project(fields, m_total, m_per_init, gamma, dt)
        if step % log_every == 0:
            log.append({'t': step * dt, 'K_active': count_active(fields), 'R_avg': avg_R(fields)})
    return log


def main():
    L = 30; K = 8
    n = L*L
    configs = [
        (4.0, 0.10),
        (4.0, 0.20),
        (8.0, 0.10),
    ]
    gammas = [0.0, 0.03, 0.05, 0.07, 0.1, 0.15, 0.2, 0.3, 0.5, 1.0]
    seeds = [0, 1]
    t_max = 70.0; dt = 0.05

    results = {}
    t0_total = time.time()
    for beta, c_total in configs:
        m_total = c_total * n
        cfg_key = f"β={beta}_c={c_total}"
        results[cfg_key] = {}
        print(f"\n=== {cfg_key} ===", flush=True)
        for gamma in gammas:
            t_g = time.time()
            logs = []
            for seed in seeds:
                log = run_gamma(L, K, m_total, beta, 0.5, gamma, t_max, dt, seed)
                logs.append(log)
            all_t = []; all_R = []
            for log in logs:
                for d in log:
                    if d['t'] > 5 and d['R_avg'] > 0.3 and d['K_active'] > 0:
                        all_t.append(d['t'])
                        all_R.append(d['R_avg'])
            if len(all_t) > 5:
                coeffs = np.polyfit(np.log(all_t), np.log(all_R), 1)
                alpha = float(coeffs[0])
            else:
                alpha = None
            results[cfg_key][gamma] = alpha
            alpha_str = f"{alpha:.3f}" if alpha is not None else "N/A"
            print(f"  γ={gamma}: α={alpha_str} (t={time.time()-t_g:.1f}s)", flush=True)

    # Find γ* for each config
    print(f"\n=== γ*(β, c) ===", flush=True)
    gamma_stars = {}
    for cfg_key, gamma_alphas in results.items():
        valid = [(g, a) for g, a in gamma_alphas.items() if a is not None]
        if valid:
            gamma_star, alpha_max = max(valid, key=lambda x: x[1])
            gamma_stars[cfg_key] = {'gamma_star': gamma_star, 'alpha_max': alpha_max}
            print(f"  {cfg_key}: γ* = {gamma_star}, α_max = {alpha_max:.3f}", flush=True)

    elapsed = time.time() - t0_total
    out = {
        'meta': {
            'L': L, 'K': K, 'configs': configs, 'gammas': gammas,
            'seeds': seeds, 't_max': t_max, 'dt': dt,
            'elapsed_s': elapsed,
        },
        'results': results,
        'gamma_stars': gamma_stars,
    }
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'u3_gamma_refined.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {out_path} in {elapsed:.1f}s")


if __name__ == '__main__':
    main()
