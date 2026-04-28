"""
_t3_hybrid_gamma.py — NQ-229 Hybrid architecture with γ mass-leak rate

Phase 8 T3: K=8, γ ∈ {0, 0.001, 0.01, 0.1, 1.0} interpolating between
per-formation pool (γ=0) and shared pool (γ→∞).

Mechanism: at each step, allow fraction γ·dt of mass to redistribute between
formations toward the shared-pool average.

m_j(t+dt) = (1-γ·dt) m_j(t) + γ·dt · m_avg
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


def hybrid_project(fields, m_total, m_per_target, gamma, dt):
    """Hybrid projection: per-formation volume relaxes toward m_per_target at rate γ."""
    K = len(fields)
    n = fields[0].shape[0]
    # Step 1: Each formation's actual mass
    m_actual = [u.sum() for u in fields]
    # Step 2: Target = (1-γ·dt) * m_actual + γ·dt * m_per_target (where m_per_target is
    # current shared-pool target, recomputed)
    m_total_actual = sum(m_actual)
    m_per_shared = m_total_actual / K
    m_target = [(1 - gamma * dt) * m_actual[j] + gamma * dt * m_per_shared for j in range(K)]
    # Step 3: Re-scale total to enforce m_total fixed
    correction = (m_total - sum(m_target)) / K
    m_target = [m + correction for m in m_target]
    # Step 4: Project each formation to its m_target
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


def run_gamma(L, K, m_total, beta, lambda_rep, gamma, t_max=100.0, dt=0.05, seed=0):
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
    m_per_init = m_total / K
    # Initialize fields with m_per_init each
    for j in range(K):
        fields[j] = fields[j] + (m_per_init - fields[j].sum()) / n
        fields[j] = np.clip(fields[j], 0, 1)

    log = []
    n_steps = int(t_max / dt)
    log_every = max(1, n_steps // 40)
    for step in range(n_steps):
        for j in range(K):
            grad = k_grad(fields, j, ec, lambda_rep, 100.0)
            fields[j] = fields[j] - dt * grad
        fields = hybrid_project(fields, m_total, m_per_init, gamma, dt)
        if step % log_every == 0:
            mass_per = [float(u.sum()) for u in fields]
            log.append({
                't': step * dt,
                'K_active': count_active(fields),
                'R_avg': avg_R(fields),
                'mass_max': max(mass_per),
                'mass_min': min(mass_per),
            })
    return log


def main():
    L = 30; K = 8
    n = L*L
    c_total = 0.20
    m_total = c_total * n
    beta = 4.0
    lambda_rep = 0.5
    gammas = [0.0, 0.001, 0.01, 0.1, 1.0]
    seeds = [0, 1]
    t_max = 80.0; dt = 0.05

    results = {}
    t0 = time.time()
    for gamma in gammas:
        print(f"\n=== γ={gamma} ===", flush=True)
        for seed in seeds:
            t_cfg = time.time()
            log = run_gamma(L, K, m_total, beta, lambda_rep, gamma, t_max, dt, seed)
            elapsed = time.time() - t_cfg
            K_init = log[0]['K_active']
            K_final = log[-1]['K_active']
            R_init = log[0]['R_avg']
            R_final = log[-1]['R_avg']
            print(f"  seed={seed}: K_act {K_init} → {K_final}, R {R_init:.2f} → {R_final:.2f}, t={elapsed:.1f}s", flush=True)
            results[f"γ={gamma}_seed={seed}"] = log

    # Fit α per γ
    print(f"\n=== α(γ) ===", flush=True)
    fit = {}
    for gamma in gammas:
        all_t = []; all_R = []
        for s in seeds:
            log = results[f"γ={gamma}_seed={s}"]
            for d in log:
                if d['t'] > 5 and d['R_avg'] > 0.3 and d['K_active'] > 0:
                    all_t.append(d['t'])
                    all_R.append(d['R_avg'])
        if len(all_t) > 5:
            coeffs = np.polyfit(np.log(all_t), np.log(all_R), 1)
            alpha = float(coeffs[0])
            fit[gamma] = alpha
            print(f"  γ={gamma}: α = {alpha:.3f}", flush=True)

    elapsed = time.time() - t0
    out = {
        'meta': {
            'L': L, 'K': K, 'c_total': c_total, 'beta': beta,
            'lambda_rep': lambda_rep, 'gammas': gammas, 'seeds': seeds,
            't_max': t_max, 'dt': dt, 'elapsed_s': elapsed,
        },
        'fit_alpha_per_gamma': fit,
        'results': results,
    }
    out_path = os.path.join(os.path.dirname(__file__), 'results', 't3_hybrid_gamma.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {out_path} in {elapsed:.1f}s")


if __name__ == '__main__':
    main()
