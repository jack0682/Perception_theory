"""Experiment 32: Directional basin bounds and perturbation-soft mode misalignment.

Verifies Theorems PSM, EBC, TP from DIRECTIONAL-BASIN-BOUNDS.md:
1. Find formation, compute Hessian eigenpairs
2. Perturb alpha_bd by 5%, find new minimizer via warm-start
3. Decompose delta_u in eigenbasis
4. Measure soft-mode fraction |c_1|/||delta_u||
5. Verify ellipsoidal containment condition
"""

import numpy as np
import sys
sys.path.insert(0, '/home/jack/ex')

from scc import GraphState, ParameterRegistry, EnergyComputer, find_formation
from scc.optimizer import project_volume

np.set_printoptions(precision=6, linewidth=120)


def make_params(**overrides):
    p = ParameterRegistry()
    for k, v in overrides.items():
        setattr(p, k, v)
    return p


def compute_constrained_hessian(u, graph, ec, h=1e-5):
    """Finite-difference constrained Hessian on free variables."""
    n = len(u)
    tol = 1e-6
    free_mask = (u > tol) & (u < 1 - tol)
    free_idx = np.where(free_mask)[0]
    n_f = len(free_idx)

    # Hessian on free variables via central differences
    H = np.zeros((n_f, n_f))
    g0 = ec.gradient(u)
    for j in range(n_f):
        idx = free_idx[j]
        u_p = u.copy()
        u_m = u.copy()
        u_p[idx] += h
        u_m[idx] -= h
        gp = ec.gradient(u_p)
        gm = ec.gradient(u_m)
        H[:, j] = (gp[free_idx] - gm[free_idx]) / (2 * h)

    # Symmetrize
    H = 0.5 * (H + H.T)

    # Project onto volume-constraint tangent space: P = I - 11^T/n_f
    ones = np.ones(n_f) / np.sqrt(n_f)
    H_proj = H - np.outer(H @ ones, ones) - np.outer(ones, ones @ H) + (ones @ H @ ones) * np.outer(ones, ones)

    return H_proj, free_idx, free_mask


def run_config(n_grid, beta, delta_alpha_frac=0.05):
    """Run directional basin analysis for one configuration."""
    print(f"\n{'='*70}")
    print(f"Grid: {n_grid}x{n_grid}, beta={beta}, delta_alpha={delta_alpha_frac*100}%")
    print(f"{'='*70}")

    # Step 1: Find original formation
    g = GraphState.grid_2d(n_grid, n_grid)
    p = make_params(beta_bd=beta)
    ec = EnergyComputer(g, p)
    ec.normalize_weights()

    res_t = find_formation(g, p)
    u_t = res_t.u
    n = len(u_t)
    print(f"Original formation: E={res_t.energy:.6f}, converged={res_t.converged}")

    # Step 2: Compute constrained Hessian eigenpairs at u_t
    H_proj, free_idx, free_mask = compute_constrained_hessian(u_t, g, ec)
    n_f = len(free_idx)

    # Eigendecompose (exclude the zero eigenvalue from volume constraint)
    eigvals, eigvecs = np.linalg.eigh(H_proj)
    # Skip the smallest eigenvalue (should be ~0, from volume constraint projection)
    skip = 0
    for i in range(len(eigvals)):
        if abs(eigvals[i]) < 1e-6:
            skip = i + 1
    eigvals = eigvals[skip:]
    eigvecs = eigvecs[:, skip:]
    n_modes = len(eigvals)

    mu_1 = eigvals[0]  # smallest (soft mode)
    mu_max = eigvals[-1]  # largest (hard mode)
    v1 = eigvecs[:, 0]  # soft mode eigenvector

    print(f"Free variables: {n_f}, Modes: {n_modes}")
    print(f"mu_1 (soft) = {mu_1:.4f}, mu_max (hard) = {mu_max:.4f}")
    print(f"Condition number: {mu_max/mu_1:.1f}")

    # Classify soft mode: boundary vs core
    theta_deep = 0.9
    bdy_in_free = [i for i, idx in enumerate(free_idx) if u_t[idx] < theta_deep]
    core_in_free = [i for i, idx in enumerate(free_idx) if u_t[idx] >= theta_deep]
    n_bdy = len(bdy_in_free)
    n_core_f = len(core_in_free)

    bdy_frac_v1 = np.sum(v1[bdy_in_free]**2) if bdy_in_free else 0.0
    print(f"Boundary nodes: {n_bdy}, Core-free nodes: {n_core_f}")
    print(f"Soft mode boundary fraction: {bdy_frac_v1:.3f}")

    # Step 3: Perturb alpha_bd and find new minimizer via warm-start
    alpha_orig = p.alpha_bd
    alpha_new = alpha_orig * (1 + delta_alpha_frac)
    p_s = make_params(beta_bd=beta, alpha_bd=alpha_new)
    ec_s = EnergyComputer(g, p_s)
    ec_s.normalize_weights()

    # Warm-start from u_t
    res_s = find_formation(g, p_s, u_init=u_t)
    u_s = res_s.u
    print(f"Perturbed formation: E={res_s.energy:.6f}, converged={res_s.converged}")

    # Step 4: Compute delta_u and decompose in eigenbasis
    delta_u_full = u_s - u_t
    delta_u = delta_u_full[free_idx]  # restrict to free variables
    delta_u_norm = np.linalg.norm(delta_u)

    if delta_u_norm < 1e-12:
        print("WARNING: delta_u ~ 0, perturbation too small")
        return None

    # Decompose in eigenbasis
    c = eigvecs.T @ delta_u  # c_k = <v_k, delta_u>
    c_norm = np.sqrt(np.sum(c**2))

    # Soft-mode fraction
    f1 = abs(c[0]) / c_norm if c_norm > 1e-12 else 0
    print(f"\n--- Perturbation Decomposition ---")
    print(f"||delta_u|| = {delta_u_norm:.6f}")
    print(f"Soft-mode fraction |c_1|/||c|| = {f1:.4f}")
    print(f"Predicted bound sqrt(n_bdy/n_F) = {np.sqrt(n_bdy/n_f):.4f}")
    print(f"Top 5 mode fractions: {np.sort(np.abs(c)/c_norm)[::-1][:5]}")

    # Step 5: Also compute gradient perturbation direction
    # delta(grad E) = delta_alpha * 4 * L * u_t (for the alpha_bd perturbation)
    Lu = np.asarray(g.L @ u_t).ravel()
    delta_grad = delta_alpha_frac * alpha_orig * 4 * Lu
    delta_grad_free = delta_grad[free_idx]
    dg_norm = np.linalg.norm(delta_grad_free)

    if dg_norm > 1e-12:
        # Project onto volume constraint tangent space
        delta_grad_proj = delta_grad_free - np.mean(delta_grad_free)
        dg_proj_norm = np.linalg.norm(delta_grad_proj)
        if dg_proj_norm > 1e-12:
            c_grad = eigvecs.T @ delta_grad_proj
            f1_grad = abs(c_grad[0]) / np.linalg.norm(c_grad)
            print(f"\n--- Gradient Perturbation Direction ---")
            print(f"Soft-mode fraction of delta(grad E): {f1_grad:.4f}")
            print(f"Bound sqrt(n_bdy/n_F) = {np.sqrt(n_bdy/n_f):.4f}")

    # Step 6: Ellipsoidal containment check
    # Basin radii per mode
    # Use minimum barrier: approximate as quadratic along soft mode
    # Delta_min from §9 of BASIN-ESCAPE-ANALYSIS: use empirical energy trace
    # For now, use the quadratic approximation Delta ~ mu_1 * r_soft^2 / 2
    # We'll trace energy along soft mode to find actual barrier
    print(f"\n--- Ellipsoidal Basin Containment ---")

    # Trace energy along soft mode to find barrier
    v1_full = np.zeros(n)
    v1_full[free_idx] = v1
    m = p.volume_fraction * n

    def energy_along(t):
        u_test = u_t + t * v1_full
        u_test = project_volume(u_test, m)
        E, _ = ec.energy(u_test)
        return E

    E_star = energy_along(0.0)
    # Search for barrier by scanning
    t_max = 2.0
    n_scan = 200
    ts = np.linspace(-t_max, t_max, n_scan)
    Es = np.array([energy_along(t) for t in ts])
    Delta_soft = np.max(Es) - E_star

    # More precise: find local max near 0
    dEs = Es - E_star
    # Find first local max on positive side
    Delta_pos = 0
    for i in range(1, len(ts)):
        if ts[i] > 0 and dEs[i] < dEs[i-1] and dEs[i-1] > 0:
            Delta_pos = dEs[i-1]
            break
    Delta_neg = 0
    for i in range(len(ts)-2, -1, -1):
        if ts[i] < 0 and dEs[i] < dEs[i+1] and dEs[i+1] > 0:
            Delta_neg = dEs[i+1]
            break

    Delta_min = min(d for d in [Delta_pos, Delta_neg, Delta_soft] if d > 0) if any(d > 0 for d in [Delta_pos, Delta_neg]) else Delta_soft

    print(f"Energy barrier along soft mode: Delta_min = {Delta_min:.6f}")
    print(f"r_iso = sqrt(2*Delta_min/mu_max) = {np.sqrt(2*Delta_min/mu_max):.6f}")
    print(f"r_soft = sqrt(2*Delta_min/mu_1) = {np.sqrt(2*Delta_min/mu_1):.6f}")

    # Directional basin radii
    r_k = np.sqrt(2 * Delta_min / eigvals)

    # Ellipsoidal check: sum (c_k / r_k)^2
    ellip_sum = np.sum((c / r_k)**2)
    iso_check = delta_u_norm**2 / (2 * Delta_min / mu_max)

    print(f"\nEllipsoidal sum: {ellip_sum:.6f} (need < 1 for containment)")
    print(f"Isotropic check: {iso_check:.6f} (need < 1 for containment)")
    print(f"Ellipsoidal contained: {ellip_sum < 1}")
    print(f"Isotropic contained: {iso_check < 1}")

    if iso_check >= 1 and ellip_sum < 1:
        print(">>> ELLIPSOIDAL WINS: perturbation outside isotropic ball but inside ellipsoid!")
    elif ellip_sum < iso_check:
        print(f">>> Ellipsoidal improvement factor: {iso_check/ellip_sum:.2f}x")

    # Step 7: Effective basin radius from Theorem TP
    if f1 > 0 and f1 < 1:
        r1 = r_k[0]
        r_last = r_k[-1]
        r_eff_sq = (r1**2 * r_last**2) / (f1**2 * r_last**2 + (1 - f1**2) * r1**2)
        r_eff = np.sqrt(r_eff_sq)
        r_iso = np.sqrt(2 * Delta_min / mu_max)
        print(f"\n--- Theorem TP Effective Basin ---")
        print(f"f_1 (soft-mode fraction) = {f1:.4f}")
        print(f"r_eff (transverse) = {r_eff:.6f}")
        print(f"r_iso (isotropic)  = {r_iso:.6f}")
        print(f"Improvement: {r_eff/r_iso:.2f}x")

    return {
        'grid': n_grid, 'beta': beta,
        'n_f': n_f, 'n_bdy': n_bdy, 'n_modes': n_modes,
        'mu_1': mu_1, 'mu_max': mu_max,
        'delta_u_norm': delta_u_norm,
        'f1': f1, 'f1_bound': np.sqrt(n_bdy/n_f),
        'Delta_min': Delta_min,
        'ellip_sum': ellip_sum, 'iso_check': iso_check,
        'bdy_frac_v1': bdy_frac_v1,
    }


if __name__ == '__main__':
    configs = [
        (8, 50),
        (10, 50),
        (10, 100),
        (12, 50),
        (12, 100),
    ]

    results = []
    for n_grid, beta in configs:
        try:
            r = run_config(n_grid, beta)
            if r is not None:
                results.append(r)
        except Exception as e:
            print(f"FAILED: {n_grid}x{n_grid} beta={beta}: {e}")
            import traceback
            traceback.print_exc()

    # Summary table
    print(f"\n\n{'='*90}")
    print("SUMMARY TABLE")
    print(f"{'='*90}")
    print(f"{'Config':<15} {'n_F':>4} {'n_bdy':>5} {'mu_1':>7} {'mu_max':>7} {'f1':>6} {'bound':>6} {'ellip':>7} {'iso':>7} {'contained':>10}")
    print(f"{'-'*90}")
    for r in results:
        contained = "ELLIP" if r['ellip_sum'] < 1 and r['iso_check'] >= 1 else ("BOTH" if r['ellip_sum'] < 1 else "NEITHER")
        print(f"{r['grid']}x{r['grid']} b={r['beta']:<4} {r['n_f']:>4} {r['n_bdy']:>5} {r['mu_1']:>7.3f} {r['mu_max']:>7.1f} {r['f1']:>6.3f} {r['f1_bound']:>6.3f} {r['ellip_sum']:>7.4f} {r['iso_check']:>7.4f} {contained:>10}")
