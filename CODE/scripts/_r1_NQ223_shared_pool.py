"""
_r1_NQ223_shared_pool.py — NQ-223 Shared-volume-pool K-field

Phase 7 R1.3: Alternative K-field architecture where mass is conserved across
all K formations (not per-formation). Σ_j Σ_x u^(j)(x) = M_total fixed but
individual masses m_j allowed to fluctuate.

Test: does this enable LSW-like coarsening dynamics?

Implementation: project Σ_j (u^(j)) total to fixed M_total at each step,
distributing change uniformly across formations and sites.
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
    """Initial: K disks each with m_total/K mass, but mass can redistribute."""
    n = L * L
    rng = np.random.default_rng(seed)
    fields = []
    K_x = int(np.ceil(np.sqrt(K)))
    K_y = int(np.ceil(K / K_x))
    spacing = L / max(K_x, K_y)
    m_each = m_total / K
    r0 = max(1.0, np.sqrt(m_each / np.pi))
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
    """Project Σ_j Σ_x u^(j)(x) = m_total. Distribute change uniformly."""
    K = len(fields)
    n = fields[0].shape[0]
    current_total = sum(u.sum() for u in fields)
    delta_per_site = (m_total - current_total) / (K * n)
    fields_proj = [u + delta_per_site for u in fields]
    fields_proj = [np.clip(u, 0, 1) for u in fields_proj]
    # Iterate
    for _ in range(3):
        current_total = sum(u.sum() for u in fields_proj)
        delta = (m_total - current_total) / (K * n)
        fields_proj = [u + delta for u in fields_proj]
        fields_proj = [np.clip(u, 0, 1) for u in fields_proj]
    return fields_proj


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


def main():
    L = 30
    K = 8
    c_total = 0.20
    n = L * L
    m_total = c_total * n  # = 180 sites total
    beta = 4.0
    xi_0 = np.sqrt(1.0/beta)  # = 0.5
    lambda_rep = 0.5
    lambda_bar = 100.0

    graph, _ = build_torus_2d(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c_total/K,  # for params validation
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=2000,
    )
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    fields = K_disks_ic(L, m_total, K, xi_0, seed=0)
    fields = project_total_volume(fields, m_total)
    print(f"Shared-pool K=8 IC: K_active={count_active(fields)}, R_avg={avg_R(fields):.3f}, Σtotal={sum(u.sum() for u in fields):.2f}", flush=True)

    dt = 0.05; t_max = 200.0
    n_steps = int(t_max / dt)
    log_every = max(1, n_steps // 60)
    log = []
    masses_initial = [u.sum() for u in fields]

    for step in range(n_steps):
        for j in range(K):
            grad = k_grad(fields, j, ec, lambda_rep, lambda_bar)
            # Project gradient: remove TOTAL gradient mean (shared pool)
            # Actually: gradient flow on shared volume manifold projects out the
            # uniform-shift direction in (u^(1), ..., u^(K)).
            # For shared pool: total volume conserved; per-formation volumes
            # can change. Use natural gradient with proper projection.
            # Simplest: subtract overall mean to keep total volume.
            fields[j] = fields[j] - dt * grad
        # Shared-pool projection
        fields = project_total_volume(fields, m_total)
        if step % log_every == 0:
            mass_per_F = [float(u.sum()) for u in fields]
            log.append({
                't': step * dt,
                'K_active': count_active(fields),
                'R_avg': avg_R(fields),
                'mass_per_F_max': max(mass_per_F),
                'mass_per_F_min': min(mass_per_F),
                'total_mass': sum(mass_per_F),
                'u_max_max': float(max(u.max() for u in fields)),
            })

    K_init = log[0]['K_active']
    K_final = log[-1]['K_active']
    R_init = log[0]['R_avg']
    R_final = log[-1]['R_avg']
    mass_min_init = log[0]['mass_per_F_min']
    mass_max_init = log[0]['mass_per_F_max']
    mass_min_final = log[-1]['mass_per_F_min']
    mass_max_final = log[-1]['mass_per_F_max']

    print(f"K_active: {K_init} → {K_final}", flush=True)
    print(f"R_avg: {R_init:.3f} → {R_final:.3f}", flush=True)
    print(f"Mass spread: [{mass_min_init:.1f}, {mass_max_init:.1f}] → [{mass_min_final:.1f}, {mass_max_final:.1f}]", flush=True)

    # Fit R(t)
    ts = np.array([d['t'] for d in log])
    Rs = np.array([d['R_avg'] for d in log])
    K_acts = np.array([d['K_active'] for d in log])
    mask = (ts > 5) & (Rs > 0.1) & (K_acts > 0)
    if mask.sum() > 5:
        coeffs = np.polyfit(np.log(ts[mask]), np.log(Rs[mask]), 1)
        alpha = coeffs[0]
        print(f"Fitted R(t) ~ t^α with α = {alpha:.3f} (LSW d=2: 0.5; d=3: 0.333)", flush=True)
    else:
        print(f"Insufficient data for fit", flush=True)

    out = {
        'meta': {
            'L': L, 'K': K, 'c_total': c_total, 'm_total': m_total,
            'beta': beta, 'lambda_rep': lambda_rep, 'lambda_bar': lambda_bar,
            'dt': dt, 't_max': t_max, 'shared_pool': True,
        },
        'log': log,
    }
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'r1_3_NQ223_shared_pool.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {out_path}")


if __name__ == '__main__':
    main()
