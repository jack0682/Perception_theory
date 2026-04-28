"""
_u4_sigma_multi_t.py — NQ-228 σ_multi^A(t) numerical implementation

Phase 9 U4: track per-formation σ-tuple at each timestep during shared-pool LSW.
Detect K-merger jumps; statistics of σ-trajectory.

Simplified σ-tuple: (m_j, peak_value, peak_location). Full Hessian-based σ
deferred to W6+ (computational cost prohibitive in long-run logging).
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


def project_total_volume(fields, m_total):
    K = len(fields)
    n = fields[0].shape[0]
    for _ in range(3):
        current_total = sum(u.sum() for u in fields)
        delta = (m_total - current_total) / (K * n)
        fields = [np.clip(u + delta, 0, 1) for u in fields]
    return fields


def sigma_multi_simplified(fields, threshold=0.5):
    """Simplified σ_multi^A entries: (m_j, peak_u, peak_loc) per formation.

    Full Hessian-based σ-tuple: out of scope for trajectory logging
    (computational cost). Phase 9 U4 uses lightweight invariant.
    """
    sigma_entries = []
    for u in fields:
        m_j = float(u.sum())
        peak_u = float(u.max())
        peak_idx = int(np.argmax(u))
        active = bool(u.max() > threshold)
        sigma_entries.append({
            'm': m_j, 'peak_u': peak_u, 'peak_idx': peak_idx, 'active': active,
        })
    return sigma_entries


def main():
    L = 30; K = 8
    n = L*L
    c_total = 0.20; m_total = c_total * n
    beta = 4.0; lambda_rep = 0.5
    xi_0 = np.sqrt(1.0/beta)
    t_max = 200.0; dt = 0.05
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

    # Log σ trajectory
    sigma_log = []
    n_steps = int(t_max / dt)
    log_every = max(1, n_steps // 200)  # high-resolution σ logging

    K_active_prev = K
    K_jumps = []  # times when K_active drops
    t0 = time.time()
    for step in range(n_steps):
        for j in range(K):
            grad = k_grad(fields, j, ec, lambda_rep, 100.0)
            fields[j] = fields[j] - dt * grad
        fields = project_total_volume(fields, m_total)
        if step % log_every == 0:
            sigma = sigma_multi_simplified(fields)
            K_active = sum(1 for s in sigma if s['active'])
            if K_active < K_active_prev:
                K_jumps.append({'t': step*dt, 'K_before': K_active_prev, 'K_after': K_active})
            K_active_prev = K_active
            sigma_log.append({'t': step*dt, 'K_active': K_active, 'sigma': sigma})

    elapsed = time.time() - t0
    print(f"Total: t={t_max}, elapsed={elapsed:.1f}s, K_jumps observed: {len(K_jumps)}", flush=True)
    for jump in K_jumps:
        print(f"  K-jump at t={jump['t']:.2f}: {jump['K_before']} → {jump['K_after']}", flush=True)

    # σ_j(t) trajectory: track first formation's m and peak_u over time
    print(f"\n=== Sample formation 0 trajectory ===", flush=True)
    for entry in sigma_log[::10]:
        s0 = entry['sigma'][0]
        print(f"  t={entry['t']:.1f}: m={s0['m']:.2f}, peak_u={s0['peak_u']:.3f}, active={s0['active']}", flush=True)

    out = {
        'meta': {
            'L': L, 'K': K, 'c_total': c_total, 'beta': beta,
            'lambda_rep': lambda_rep, 't_max': t_max, 'dt': dt, 'seed': seed,
            'elapsed_s': elapsed,
        },
        'sigma_log': sigma_log,
        'K_jumps': K_jumps,
        'note': 'Simplified σ via (m, peak_u, peak_idx); full Hessian σ deferred to W6+',
    }
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'u4_sigma_multi_t.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {out_path}")


if __name__ == '__main__':
    main()
