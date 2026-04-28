"""
_f6_time_dep_K2.py — Time-dependent K=2 simulation, measure τ_linear

Phase 4 F6: integrate K=2 gradient flow ODE from perturbed K=2 IC.
Track antisym mode amplitude over time; fit exponential to extract τ_linear.
Verify against T-σ-Multi-1 prediction τ = 1/|μ_antisym|.
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


def two_disk_ic(L, c, d_min, xi_0, seed=0):
    n = L * L
    rng = np.random.default_rng(seed)
    cx_1, cy_1 = L / 4.0, L / 2.0
    cx_2, cy_2 = (L / 4.0 + d_min) % L, L / 2.0
    r0 = np.sqrt(c * L * L / np.pi)
    i_idx, j_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
    def per_dist(cx, cy):
        dx = np.minimum(np.abs(i_idx - cx), L - np.abs(i_idx - cx))
        dy = np.minimum(np.abs(j_idx - cy), L - np.abs(j_idx - cy))
        return np.sqrt(dx**2 + dy**2)
    r1 = per_dist(cx_1, cy_1).flatten()
    r2 = per_dist(cx_2, cy_2).flatten()
    u1 = 0.5 * (1.0 - np.tanh((r1 - r0) / xi_0))
    u2 = 0.5 * (1.0 - np.tanh((r2 - r0) / xi_0))
    u1 = np.clip(u1 + rng.normal(0, 0.02, n), 0.01, 0.99)
    u2 = np.clip(u2 + rng.normal(0, 0.02, n), 0.01, 0.99)
    return u1, u2


def k_grad(fields, j, ec, lambda_rep, lambda_bar):
    K = len(fields)
    g_intra = ec.gradient(fields[j])
    g_rep = lambda_rep * sum(fields[k] for k in range(K) if k != j)
    S = sum(fields)
    g_bar = 2.0 * lambda_bar * np.maximum(0.0, S - 1.0)
    return g_intra + g_rep + g_bar


def project_volume(u, m):
    """Project to volume m and clip to [0,1]."""
    u = u + (m - u.sum()) / len(u)
    u = np.clip(u, 0, 1)
    # Iterate to converge volume
    for _ in range(10):
        u = u + (m - u.sum()) / len(u)
        u = np.clip(u, 0, 1)
    return u


def time_evolve_K2(graph, ec, params, fields_init, lambda_rep, lambda_bar=100.0,
                   dt=0.01, t_max=200.0, n_log=200):
    """Gradient flow K=2 with simple Euler + volume projection."""
    K = 2
    n = fields_init[0].shape[0]
    masses = [u.sum() for u in fields_init]
    fields = [u.copy() for u in fields_init]
    times = []
    log_data = []
    n_steps = int(t_max / dt)
    log_every = max(1, n_steps // n_log)
    t = 0.0
    for step in range(n_steps):
        # Compute gradients
        grads = [k_grad(fields, j, ec, lambda_rep, lambda_bar) for j in range(K)]
        # Project gradients (remove volume tangent)
        for j in range(K):
            grads[j] = grads[j] - grads[j].mean()
        # Step
        for j in range(K):
            fields[j] = fields[j] - dt * grads[j]
            fields[j] = project_volume(fields[j], masses[j])
        t += dt
        if step % log_every == 0:
            E1, _ = ec.energy(fields[0])
            E2, _ = ec.energy(fields[1])
            ip = float(fields[0] @ fields[1])
            E_total = E1 + E2 + lambda_rep * ip
            times.append(t)
            log_data.append({
                't': t, 'E_total': float(E_total),
                'inner_product': ip,
                'u1_max': float(fields[0].max()),
                'u2_max': float(fields[1].max()),
                'fields_diff': float(np.linalg.norm(fields[0] - fields[1])),
            })
    return fields, log_data


def main():
    L = 20; c = 0.10; beta = 4.0; xi_0 = 0.5
    d_min = 8; lambda_rep = 0.1
    seed = 0
    graph, n = build_torus_2d(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=2000,
    )
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    # First find K=2 stationary point via _optimize_k_fields
    from scc.multi import _optimize_k_fields
    u1_init, u2_init = two_disk_ic(L, c, d_min, xi_0, seed)
    fields_stat = _optimize_k_fields(
        graph, params, ec, K=2, masses=[c*n, c*n],
        lambda_rep=lambda_rep, lambda_bar=100.0,
        max_iter=2000, seed=42, verbose=False,
        init_fields=[u1_init, u2_init],
        init_perturb=None, perturb_seed=0,
    )
    print(f"K=2 stationary: u1.max={fields_stat[0].max():.3f}, <u1,u2>={fields_stat[0]@fields_stat[1]:.3f}", flush=True)

    # Add small antisym perturbation: (eps · g, -eps · g) where g is random
    rng = np.random.default_rng(7)
    g = rng.normal(0, 1, n)
    g = g - g.mean()
    g = g / np.linalg.norm(g)
    epsilon = 0.01
    fields_perturbed = [
        fields_stat[0] + epsilon * g,
        fields_stat[1] - epsilon * g,
    ]
    # Project to volumes
    fields_perturbed[0] = project_volume(fields_perturbed[0], c * n)
    fields_perturbed[1] = project_volume(fields_perturbed[1], c * n)

    # Time evolve
    print("Starting time evolution...", flush=True)
    t0 = time.time()
    fields_final, log_data = time_evolve_K2(
        graph, ec, params, fields_perturbed,
        lambda_rep=lambda_rep, lambda_bar=100.0,
        dt=0.01, t_max=300.0, n_log=300,
    )
    elapsed = time.time() - t0
    print(f"Time evolution complete in {elapsed:.1f}s", flush=True)
    print(f"Final: u1.max={fields_final[0].max():.3f}, <u1,u2>={fields_final[0]@fields_final[1]:.3f}", flush=True)
    print(f"fields_diff (1 - 2): start={log_data[0]['fields_diff']:.4f} → end={log_data[-1]['fields_diff']:.4f}", flush=True)

    out_path = os.path.join(os.path.dirname(__file__), 'results', 'f6_time_dep_K2.json')
    with open(out_path, 'w') as f:
        json.dump({
            'meta': {
                'L': L, 'c': c, 'beta': beta, 'd_min': d_min,
                'lambda_rep': lambda_rep, 'epsilon_perturbation': epsilon,
                'dt': 0.01, 't_max': 300.0,
                'elapsed_s': elapsed,
                'description': 'F6: time-dep K=2 with antisym perturbation, measure τ_linear',
            },
            'log_data': log_data,
        }, f, indent=2)
    print(f"Wrote {out_path}")


if __name__ == '__main__':
    main()
