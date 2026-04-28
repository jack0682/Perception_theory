"""
_r1_NQ222_no_clip.py — NQ-222 Dynamic test without [0,1] clipping

Phase 7 R1.2: Q1 setup but allow u outside [0,1] during gradient flow.
Tests whether [0,1] box constraint clipping stabilizes the perturbation.
"""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
import scipy.sparse as sp
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.multi import _optimize_k_fields


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


def joint_hessian(fields, ec, lambda_rep, lambda_bar, eps=1e-4):
    n = fields[0].shape[0]
    K = len(fields)
    g0 = [k_grad(fields, j, ec, lambda_rep, lambda_bar) for j in range(K)]
    big = np.zeros((K*n, K*n))
    for kp in range(K):
        for i in range(n):
            fp = [u.copy() for u in fields]
            fp[kp][i] += eps
            for j in range(K):
                gp = k_grad(fp, j, ec, lambda_rep, lambda_bar)
                big[j*n:(j+1)*n, kp*n+i] = (gp - g0[j]) / eps
    big = (big + big.T) / 2
    return big


def project_volume_only(u, m):
    """Volume project WITHOUT box clipping."""
    return u + (m - u.sum()) / len(u)


def main():
    L = 20; c = 0.10; beta = 4.0; xi_0 = 0.5
    d_min = 8; lambda_rep = 0.1; seed = 0
    EPSILON = 0.05

    graph, n = build_torus_2d(L)
    params = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=1, max_iter=2000,
    )
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()

    u1_init, u2_init = two_disk_ic(L, c, d_min, xi_0, seed)
    fields_stat = _optimize_k_fields(
        graph, params, ec, K=2, masses=[c*n, c*n],
        lambda_rep=lambda_rep, lambda_bar=100.0,
        max_iter=2000, seed=42, verbose=False,
        init_fields=[u1_init, u2_init],
        init_perturb=None, perturb_seed=0,
    )
    print(f"Stationary K=2: u1.max={fields_stat[0].max():.3f}, <u1,u2>={fields_stat[0]@fields_stat[1]:.3f}", flush=True)

    H = joint_hessian(fields_stat, ec, lambda_rep, 100.0)
    one = np.ones(n) / np.sqrt(n)
    e1 = np.concatenate([one, np.zeros(n)])
    e2 = np.concatenate([np.zeros(n), one])
    P = np.eye(2*n) - np.outer(e1, e1) - np.outer(e2, e2)
    Hp = P @ H @ P
    eigvals, eigvecs = np.linalg.eigh(Hp)
    print(f"Volume-projected H lowest 6: {[round(float(e), 4) for e in eigvals[:6]]}", flush=True)

    chosen_idx = None
    for i in range(20):
        v = eigvecs[:, i]
        if abs(v[:n].sum()) < 1e-6 and abs(v[n:].sum()) < 1e-6:
            chosen_idx = i
            break
    if chosen_idx is None:
        chosen_idx = 0
    chosen_lam = eigvals[chosen_idx]
    psi = eigvecs[:, chosen_idx]
    print(f"Selected eigvec {chosen_idx}: λ = {chosen_lam:.4f}", flush=True)

    delta1 = EPSILON * psi[:n]
    delta2 = EPSILON * psi[n:]
    fields_pert = [
        fields_stat[0] + delta1,
        fields_stat[1] + delta2,
    ]
    # Volume project but NO clipping
    fields_pert = [project_volume_only(u, c * n) for u in fields_pert]

    print(f"Initial u outside [0,1]? min={min(fields_pert[0].min(), fields_pert[1].min()):.4f}, max={max(fields_pert[0].max(), fields_pert[1].max()):.4f}", flush=True)

    dt = 0.01; t_max = 30.0  # Shorter for stability concerns
    n_steps = int(t_max / dt)
    log_every = max(1, n_steps // 100)
    log = []
    fields = [u.copy() for u in fields_pert]
    masses = [u.sum() for u in fields_stat]
    for step in range(n_steps):
        for j in range(2):
            grad = k_grad(fields, j, ec, lambda_rep, 100.0)
            grad = grad - grad.mean()
            fields[j] = fields[j] - dt * grad
            fields[j] = project_volume_only(fields[j], masses[j])  # NO CLIP
        if step % log_every == 0:
            disp = np.concatenate([fields[0] - fields_stat[0], fields[1] - fields_stat[1]])
            amp = float(disp @ psi)
            log.append({
                't': step * dt,
                'amp': amp,
                'disp_norm': float(np.linalg.norm(disp)),
                'inner_product': float(fields[0] @ fields[1]),
                'u_min': float(min(fields[0].min(), fields[1].min())),
                'u_max': float(max(fields[0].max(), fields[1].max())),
            })

    ts = np.array([d['t'] for d in log])
    amps = np.array([abs(d['amp']) for d in log])
    mask = (ts > 0.5) & (ts < 15) & (amps > 1e-7) & np.isfinite(amps)
    if mask.sum() > 5:
        log_a = np.log(amps[mask])
        coeffs = np.polyfit(ts[mask], log_a, 1)
        rate = coeffs[0]
        print(f"Measured rate (no clip): {rate:.4f} (predicted |λ|={abs(chosen_lam):.4f}); ratio={rate/abs(chosen_lam):.3f}", flush=True)
    else:
        rate = None
        print(f"Insufficient data for fit", flush=True)

    u_min_max = max(abs(d['u_min']) for d in log)
    u_max_max = max(d['u_max'] for d in log)
    print(f"u range during evolution: min={-u_min_max:.3f}, max={u_max_max:.3f}", flush=True)

    out = {
        'meta': {
            'L': L, 'c': c, 'beta': beta, 'd_min': d_min,
            'lambda_rep': lambda_rep, 'epsilon': EPSILON, 'no_clip': True,
        },
        'eigvals': [float(e) for e in eigvals[:10]],
        'chosen_idx': chosen_idx,
        'chosen_lam': float(chosen_lam),
        'rate_measured': float(rate) if rate is not None else None,
        'log': log,
    }
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'r1_2_NQ222_no_clip.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {out_path}")


if __name__ == '__main__':
    main()
