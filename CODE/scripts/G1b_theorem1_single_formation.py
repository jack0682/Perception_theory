"""G1b: Direct test of Theorem 1 on F=1 pure E_bd minimizer.

R23 stable minimizers are F≥5 multi-peak, so do NOT test Theorem 1 (bulk-localized single formation).
This script directly tests Theorem 1 by:
  1. Finding F=1 pure E_bd minimizer at several (L, β) — true single disk
  2. Computing its Hessian spectrum (full SCC Hessian at this u*)
  3. Testing λ_0/λ_1 ratio and λ_0 ~ exp(-d_*/ξ_0) scaling

Also tests Pöschl-Teller NQ-136 predictions at this SAME configuration.

Run: cd CODE && python3 scripts/G1b_theorem1_single_formation.py
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.energy import EnergyComputer, grad_bd, grad_cl, grad_sep


def count_local_maxima(u, L):
    g = u.reshape(L, L)
    F = 0
    for i in range(L):
        for j in range(L):
            v = g[i, j]
            ok = True
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < L and 0 <= nj < L and g[ni, nj] >= v:
                    ok = False
                    break
            if ok:
                F += 1
    return F


def com_distance_to_boundary(u, L):
    """CoM of u, then distance to nearest boundary."""
    g = u.reshape(L, L)
    # Weighted COM
    total = g.sum()
    if total < 1e-6:
        return (L/2, L/2), L/2
    x_idx, y_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
    cx = (g * x_idx).sum() / total
    cy = (g * y_idx).sum() / total
    d = min(cx, L - 1 - cx, cy, L - 1 - cy)
    return (cx, cy), d


def compute_constrained_hessian_fd(u_star, graph, params, n_modes=8, eps=1e-4):
    """Finite-difference Hessian on T(Σ_m), then compute lowest n_modes eigenvalues.

    Following exp_orbital_discovery.py pattern.
    """
    n = graph.n
    g0 = _full_gradient(u_star, graph, params)
    g0_proj = g0 - g0.mean()

    # Build Hessian via FD
    H = np.zeros((n, n))
    for i in range(n):
        u_plus = u_star.copy()
        u_plus[i] += eps
        g_plus = _full_gradient(u_plus, graph, params)
        H[:, i] = (g_plus - g0) / eps

    # Symmetrize
    H = (H + H.T) / 2.0

    # Project onto T(Σ_m) = 1^perp
    # H_proj = P H P where P = I - (1/n) 1 1^T
    one = np.ones(n)
    P = np.eye(n) - np.outer(one, one) / n
    H_proj = P @ H @ P

    # Dense eigendecomposition (symmetric)
    eigvals = np.linalg.eigvalsh(H_proj)
    eigvals.sort()
    # First eigenvalue is tangent direction (should be ≈ 0)
    # Take next n_modes
    return eigvals[:n_modes + 1]  # include the tangent-zero


def _full_gradient(u, graph, params):
    return (params.w_bd * grad_bd(u, graph, params)
            + params.w_cl * grad_cl(u, graph, params)
            + params.w_sep * grad_sep(u, graph, params))


def find_F1_disk_pure(L, beta=30.0, c=0.5, n_tries=15):
    """Find a pure-E_bd F=1 single-disk minimizer."""
    graph = GraphState.grid_2d(L, L)
    p_pure = ParameterRegistry(
        alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
        a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
        w_cl=0.0, w_sep=0.0, w_bd=1.0,
        n_restarts=2, max_iter=5000,
    )
    best = None
    for seed in range(n_tries):
        np.random.seed(seed * 13 + 7)
        # Localized initial condition (bulk blob)
        u_init = np.zeros(L*L)
        cx, cy = L/2, L/2
        r0 = np.sqrt(c * L * L / np.pi)
        x_idx, y_idx = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
        r = np.sqrt((x_idx - cx)**2 + (y_idx - cy)**2).flatten()
        u_init = 0.5 * (1.0 - np.tanh((r - r0) / 1.0))  # xi=1 ~ lattice
        # Small random perturbation
        u_init = np.clip(u_init + np.random.normal(0, 0.02, size=L*L), 0.01, 0.99)
        try:
            res = find_formation(graph, p_pure, normalize=False, verbose=False, u_init=u_init)
            if res.converged:
                F = count_local_maxima(res.u, L)
                if F == 1 and (best is None or res.energy < best[1]):
                    best = (res.u, res.energy)
        except Exception:
            pass
    return best


def main():
    print("=" * 70)
    print("G1b: Direct Theorem 1 Test on F=1 Pure E_bd Single-Disk Minimizer")
    print("=" * 70)

    L_list = [12, 16, 20]  # small to medium
    beta = 30.0
    alpha = 1.0
    c = 0.5

    results = []
    for L in L_list:
        print(f"\n--- L={L} ---")
        xi_0 = np.sqrt(alpha / beta)
        r_0 = np.sqrt(c * L * L / np.pi)

        # Find F=1 minimizer
        found = find_F1_disk_pure(L, beta=beta, c=c, n_tries=10)
        if found is None:
            print(f"  L={L}: No F=1 minimizer found.")
            continue
        u_disk, energy_pure = found
        F = count_local_maxima(u_disk, L)
        (cx, cy), d_star = com_distance_to_boundary(u_disk, L)
        print(f"  Pure E_bd F={F}, energy={energy_pure:.3f}, COM=({cx:.2f},{cy:.2f}), d*={d_star:.2f}")
        print(f"  xi_0={xi_0:.4f}, r_0={r_0:.2f}, d_*/xi_0={d_star/xi_0:.1f}")

        # Compute full-SCC Hessian at this disk minimizer
        graph = GraphState.grid_2d(L, L)
        p_full = ParameterRegistry(
            alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
            a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
            w_cl=1.0, w_sep=1.0, w_bd=1.0,
        )
        p_pure = ParameterRegistry(
            alpha_bd=1.0, beta_bd=beta, volume_fraction=c,
            a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0,
            w_cl=0.0, w_sep=0.0, w_bd=1.0,
        )

        print(f"  Computing Hessian spectrum (pure E_bd, size {L*L}x{L*L})...")
        # Pure E_bd Hessian first (baseline)
        eigs_pure = compute_constrained_hessian_fd(u_disk, graph, p_pure, n_modes=8, eps=1e-4)
        print(f"  Pure E_bd eigenvalues [0:8]: {[f'{e:.3f}' for e in eigs_pure[:8]]}")

        # Note: pure E_bd eigs[0] should be tangent (~0). Mode 0 = eigs[1].
        lam_tangent = eigs_pure[0]
        lam_0_pure = eigs_pure[1]
        lam_1_pure = eigs_pure[2]
        ratio_pure = lam_0_pure / lam_1_pure
        print(f"  Pure E_bd λ_0={lam_0_pure:.4f}, λ_1={lam_1_pure:.4f}, ratio={ratio_pure:.4f}")

        # Full SCC Hessian at same u_disk
        print(f"  Computing Hessian spectrum (full SCC, size {L*L}x{L*L})...")
        eigs_full = compute_constrained_hessian_fd(u_disk, graph, p_full, n_modes=8, eps=1e-4)
        print(f"  Full SCC eigenvalues [0:8]: {[f'{e:.3f}' for e in eigs_full[:8]]}")

        morse_full = sum(1 for e in eigs_full[1:] if e < -1e-3)
        print(f"  Morse index (full SCC at pure E_bd disk): {morse_full}")
        print(f"  (Morse > 0 confirms Theorem 2: disk is saddle under full SCC)")

        # Pöschl-Teller prediction for comparison (NQ-136 Cat A)
        pt_preds = [beta + 4*alpha*(ell**2 - 0.25)/r_0**2 for ell in range(6)]
        print(f"  Pöschl-Teller pred (ℓ=0..5): {[f'{p:.3f}' for p in pt_preds]}")

        results.append({
            'L': L,
            'F': F,
            'energy_pure': energy_pure,
            'com': [float(cx), float(cy)],
            'd_star': float(d_star),
            'xi_0': float(xi_0),
            'r_0': float(r_0),
            'd_over_xi': float(d_star / xi_0),
            'eigs_pure': [float(e) for e in eigs_pure.tolist()],
            'eigs_full': [float(e) for e in eigs_full.tolist()],
            'lam_0_pure': float(lam_0_pure),
            'lam_1_pure': float(lam_1_pure),
            'ratio_pure': float(ratio_pure),
            'morse_full': int(morse_full),
            'pt_predictions': [float(p) for p in pt_preds],
        })

    # Theorem 1 scaling test
    if len(results) >= 2:
        print("\n" + "=" * 70)
        print("Theorem 1 scaling test: log λ_0 vs d_*/xi_0")
        print("=" * 70)
        d_over_xi = np.array([r['d_over_xi'] for r in results])
        lam_0 = np.array([r['lam_0_pure'] for r in results])
        log_lam = np.log(lam_0)
        slope, intercept = np.polyfit(d_over_xi, log_lam, 1)
        print(f"  Fit: log λ_0 = {intercept:.3f} + ({slope:.5f}) * (d_*/xi_0)")
        print(f"  Theorem 1 predicts slope = -1 (exp decay)")
        print(f"  Observed slope: {slope}")
        print(f"  {'✓' if slope < -0.5 else '✗'} slope {'consistent' if slope < -0.5 else 'inconsistent'} with Goldstone")

    # Pöschl-Teller comparison
    if results:
        print("\n" + "=" * 70)
        print("Pöschl-Teller comparison at F=1 disk minimizer")
        print("=" * 70)
        for r in results:
            eigs = r['eigs_pure'][1:7]  # skip tangent
            preds = r['pt_predictions']
            print(f"  L={r['L']}: obs λ[0:6]={[f'{e:.2f}' for e in eigs]}")
            print(f"          PT λ[0:6]={[f'{p:.2f}' for p in preds]}")

    # Save
    out = os.path.join(os.path.dirname(__file__), 'results', 'G1b_theorem1_single_formation.json')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump({'beta': beta, 'alpha': alpha, 'c': c, 'results': results}, f, indent=2)
    print(f"\nSaved: {out}")


if __name__ == "__main__":
    main()
