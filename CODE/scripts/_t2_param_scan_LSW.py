"""
_t2_param_scan_LSW.py — NQ-226 parameter scan for shared-pool LSW α

Phase 8 T2: K=10 fixed, scan β ∈ {2, 4, 8}, c_total ∈ {0.10, 0.20}, λ_rep ∈ {0.1, 0.5, 1.0}.
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


def run_config(L, K, m_total, beta, lambda_rep, t_max=120.0, dt=0.05, seed=0):
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
    log_every = max(1, n_steps // 30)
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
    L = 30
    K = 10
    n = L*L
    betas = [2.0, 4.0, 8.0]
    c_totals = [0.10, 0.20]
    lambda_reps = [0.1, 0.5, 1.0]
    seeds = [0, 1]
    t_max = 100.0; dt = 0.05

    results = {}
    t0 = time.time()
    for beta in betas:
        for c_total in c_totals:
            for lam in lambda_reps:
                m_total = c_total * n
                key = f"β={beta}_c={c_total}_λ={lam}"
                print(f"{key}...", flush=True, end="")
                t_cfg = time.time()
                logs = []
                for seed in seeds:
                    log = run_config(L, K, m_total, beta, lam, t_max, dt, seed)
                    logs.append(log)
                # Aggregate fit
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
                K_final_avg = np.mean([log[-1]['K_active'] for log in logs])
                R_final_avg = np.mean([log[-1]['R_avg'] for log in logs])
                results[key] = {
                    'beta': beta, 'c_total': c_total, 'lambda_rep': lam,
                    'K_final_avg': K_final_avg, 'R_final_avg': R_final_avg,
                    'alpha': alpha,
                    'n_fit_pts': len(all_t),
                }
                alpha_str = f"{alpha:.3f}" if alpha is not None else "N/A"
                print(f" K_f={K_final_avg:.1f} R_f={R_final_avg:.2f} α={alpha_str} dt={time.time()-t_cfg:.1f}s", flush=True)

    elapsed = time.time() - t0
    print(f"\n=== α dependence summary ===", flush=True)
    for key, r in results.items():
        if r['alpha'] is not None:
            print(f"  {key}: α = {r['alpha']:.3f}", flush=True)

    out = {
        'meta': {
            'L': L, 'K': K, 'betas': betas, 'c_totals': c_totals,
            'lambda_reps': lambda_reps, 'seeds': seeds,
            't_max': t_max, 'dt': dt, 'elapsed_s': elapsed,
        },
        'results': results,
    }
    out_path = os.path.join(os.path.dirname(__file__), 'results', 't2_param_scan_LSW.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {out_path}")


if __name__ == '__main__':
    main()
