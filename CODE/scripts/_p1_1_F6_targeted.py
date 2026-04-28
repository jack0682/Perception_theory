"""
_p1_1_F6_targeted.py — Targeted Hessian-eigenvector perturbation for K=2

Phase 5 P1.1 (resolves Phase 4 W1): Compute joint Hessian, identify lowest-
eigenvalue eigenvector (antisym Goldstone), perturb along it, ODE-integrate.
Measure exponential growth rate; verify against T-σ-Multi-1.
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


def project_volume(u, m):
    u = u + (m - u.sum()) / len(u)
    u = np.clip(u, 0, 1)
    for _ in range(5):
        u = u + (m - u.sum()) / len(u)
        u = np.clip(u, 0, 1)
    return u


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

    u1_init, u2_init = two_disk_ic(L, c, d_min, xi_0, seed)
    fields_stat = _optimize_k_fields(
        graph, params, ec, K=2, masses=[c*n, c*n],
        lambda_rep=lambda_rep, lambda_bar=100.0,
        max_iter=2000, seed=42, verbose=False,
        init_fields=[u1_init, u2_init],
        init_perturb=None, perturb_seed=0,
    )
    print(f"Stationary K=2: u1.max={fields_stat[0].max():.3f}, <u1,u2>={fields_stat[0]@fields_stat[1]:.3f}", flush=True)

    # Compute joint Hessian + project volume tangents
    print("Computing joint Hessian...", flush=True)
    t0 = time.time()
    H = joint_hessian(fields_stat, ec, lambda_rep, 100.0)
    # Project out the two volume tangents (one per formation)
    one = np.ones(n)
    # Volume tangent for formation 1: (1,0) repeated; for formation 2: (0,1) repeated
    e1 = np.concatenate([one/np.sqrt(n), np.zeros(n)])
    e2 = np.concatenate([np.zeros(n), one/np.sqrt(n)])
    P = np.eye(2*n) - np.outer(e1, e1) - np.outer(e2, e2)
    Hp = P @ H @ P
    eigvals, eigvecs = np.linalg.eigh(Hp)
    print(f"Joint H computed + projected in {time.time()-t0:.1f}s", flush=True)
    print(f"Lowest 6 eigvals: {[round(float(e), 4) for e in eigvals[:6]]}", flush=True)

    # Pick the lowest eigenvector as antisym Goldstone candidate
    psi_anti = eigvecs[:, 0]  # lowest eigvec
    lam_anti = eigvals[0]
    print(f"Antisym Goldstone candidate: λ = {lam_anti:.4f}, T-σ-Multi-1 prediction: τ_lin = {1/abs(lam_anti):.2f}", flush=True)

    # Perturb along this eigenvector
    epsilon = 0.005
    delta1 = epsilon * psi_anti[:n]
    delta2 = epsilon * psi_anti[n:]
    fields_pert = [
        fields_stat[0] + delta1,
        fields_stat[1] + delta2,
    ]
    fields_pert = [project_volume(u, c * n) for u in fields_pert]
    print(f"Perturbation applied. Initial perturbation norm: {epsilon:.4f}", flush=True)

    # ODE evolve and track antisym amplitude
    dt = 0.01; t_max = 100.0
    n_steps = int(t_max / dt)
    log_every = max(1, n_steps // 200)
    log = []
    fields = [u.copy() for u in fields_pert]
    masses = [u.sum() for u in fields_stat]
    t0_wall = time.time()
    for step in range(n_steps):
        for j in range(2):
            grad = k_grad(fields, j, ec, lambda_rep, 100.0)
            grad = grad - grad.mean()
            fields[j] = fields[j] - dt * grad
            fields[j] = project_volume(fields[j], masses[j])
        if step % log_every == 0:
            # Antisym amplitude: project displacement onto psi_anti
            disp = np.concatenate([fields[0] - fields_stat[0], fields[1] - fields_stat[1]])
            amp_anti = float(disp @ psi_anti)
            disp_norm = float(np.linalg.norm(disp))
            log.append({
                't': step * dt,
                'amp_anti': amp_anti,
                'disp_norm': disp_norm,
                'u1_max': float(fields[0].max()),
                'inner_product': float(fields[0] @ fields[1]),
            })
    elapsed = time.time() - t0_wall
    print(f"Time evolution: {elapsed:.1f}s", flush=True)

    # Fit exponential growth rate to log
    ts = np.array([d['t'] for d in log])
    amps = np.array([abs(d['amp_anti']) for d in log])
    # Take early-time portion (before saturation): say t ∈ [1, 30]
    mask = (ts > 1) & (ts < 30) & (amps > 1e-6)
    if mask.sum() > 5:
        log_amps = np.log(amps[mask])
        coeffs = np.polyfit(ts[mask], log_amps, 1)
        rate_measured = coeffs[0]
        print(f"Fitted exponential rate: {rate_measured:.4f} (T-σ-Multi-1 prediction: |λ_anti| = {abs(lam_anti):.4f})", flush=True)
        print(f"Ratio measured/predicted: {rate_measured/abs(lam_anti):.3f}", flush=True)
    else:
        print(f"Insufficient data for fit (mask sum: {mask.sum()})", flush=True)

    out = {
        'meta': {
            'L': L, 'c': c, 'beta': beta, 'd_min': d_min,
            'lambda_rep': lambda_rep, 'epsilon': epsilon,
            'lam_antisym_predicted': float(lam_anti),
            'tau_predicted': float(1/abs(lam_anti)),
        },
        'lowest_6_eigvals': [float(e) for e in eigvals[:6]],
        'log': log,
    }
    if mask.sum() > 5:
        out['rate_measured'] = float(rate_measured)
        out['ratio_measured_predicted'] = float(rate_measured / abs(lam_anti))
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'p1_1_F6_targeted.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {out_path}")


if __name__ == '__main__':
    main()
