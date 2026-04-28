"""
_f7_K10_LSW.py — K=10 simulation for LSW scaling test

Phase 4 F7: K=10 K-formation gradient flow on T²_{20}, time-evolved.
Track number of "active formations" K(t) over time. Test R(t) ~ t^{1/d}
LSW prediction (`13_LSW_connection.md`).
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


def K_disks_ic(L, c, K, xi_0, seed=0):
    """Place K disks on a coarse grid."""
    n = L * L
    rng = np.random.default_rng(seed)
    fields = []
    K_x = int(np.ceil(np.sqrt(K)))
    K_y = int(np.ceil(K / K_x))
    spacing = L / max(K_x, K_y)
    r0 = np.sqrt(c * L * L / np.pi)  # if K=1 sized, but for K=10 each disk much smaller
    r0 = r0 / np.sqrt(K)  # smaller per-formation
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


def project_volume(u, m):
    u = u + (m - u.sum()) / len(u)
    u = np.clip(u, 0, 1)
    for _ in range(5):
        u = u + (m - u.sum()) / len(u)
        u = np.clip(u, 0, 1)
    return u


def count_active_formations(fields, threshold=0.3):
    """Count formations with max(u) > threshold."""
    return sum(1 for u in fields if u.max() > threshold)


def avg_R(fields, threshold=0.3):
    """Average effective radius of active formations: R = sqrt(area/π) where area = sum(u)*1"""
    Rs = []
    for u in fields:
        if u.max() > threshold:
            mass = u.sum()  # effective area in lattice units
            R = np.sqrt(mass / np.pi)
            Rs.append(R)
    return np.mean(Rs) if Rs else 0.0


def main():
    L = 20; c = 0.10; beta = 4.0; xi_0 = 0.5
    K = 10; lambda_rep = 0.05; lambda_bar = 100.0
    m_each = c * L * L  # 40 each? Too big for K=10. Use smaller per-formation.
    # For K=10 on 400 sites: each gets m = c*n/K = 0.10*400/10 = 4 sites of mass.
    m_each = c * L * L / K  # 4 per formation
    print(f"K={K}, m_each={m_each}, total mass = {m_each*K} = {c*L*L}", flush=True)

    graph, n = build_torus_2d(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c/K,  # per-formation c
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=2000,
    )
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    fields = K_disks_ic(L, c/K, K, xi_0, seed=0)
    fields = [project_volume(u, m_each) for u in fields]
    print(f"Initial: K_active = {count_active_formations(fields)}, avg R = {avg_R(fields):.3f}", flush=True)

    # Time evolve
    dt = 0.01; t_max = 200.0
    n_log = 100
    log_data = []
    n_steps = int(t_max / dt)
    log_every = max(1, n_steps // n_log)
    t = 0.0
    t0_wall = time.time()
    for step in range(n_steps):
        for j in range(K):
            grad_j = k_grad(fields, j, ec, lambda_rep, lambda_bar)
            grad_j = grad_j - grad_j.mean()
            fields[j] = fields[j] - dt * grad_j
            fields[j] = project_volume(fields[j], m_each)
        t += dt
        if step % log_every == 0:
            K_act = count_active_formations(fields)
            R_avg = avg_R(fields)
            E_total = sum(ec.energy(u)[0] for u in fields)
            for i in range(K):
                for jj in range(i+1, K):
                    E_total += lambda_rep * float(fields[i] @ fields[jj])
            log_data.append({
                't': t, 'K_active': K_act, 'R_avg': float(R_avg),
                'E_total': float(E_total),
            })
    elapsed = time.time() - t0_wall
    print(f"Final: K_active = {log_data[-1]['K_active']}, R_avg = {log_data[-1]['R_avg']:.3f}, in {elapsed:.1f}s", flush=True)

    # Fit R(t) ~ t^α
    ts = np.array([d['t'] for d in log_data if d['K_active'] >= 1])
    Rs = np.array([d['R_avg'] for d in log_data if d['K_active'] >= 1])
    if len(ts) > 5 and Rs.max() > 0:
        log_t = np.log(ts[ts > 1])
        log_R = np.log(Rs[ts > 1])
        if len(log_t) > 5:
            coeffs = np.polyfit(log_t, log_R, 1)
            alpha = coeffs[0]
            print(f"Fitted R(t) ~ t^{alpha:.3f} (LSW d=2 prediction: 1/2 = 0.5; d=3 prediction: 1/3 = 0.333)", flush=True)

    out_path = os.path.join(os.path.dirname(__file__), 'results', 'f7_K10_LSW.json')
    with open(out_path, 'w') as f:
        json.dump({
            'meta': {
                'L': L, 'c': c, 'K': K, 'beta': beta,
                'lambda_rep': lambda_rep, 'm_each': m_each,
                'dt': dt, 't_max': t_max, 'elapsed_s': elapsed,
            },
            'log_data': log_data,
        }, f, indent=2)
    print(f"Wrote {out_path}")


if __name__ == '__main__':
    main()
