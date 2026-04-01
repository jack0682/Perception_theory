"""Experiment 24: Test actual basin of attraction via gradient flow.

The sublevel set gives a conservative lower bound. Test whether gradient flow
converges even from perturbations MUCH larger than r_soft.

Also computes Taylor coefficients L3, L4 along soft mode for quantitative
Δ_bdy formula derivation.
"""

import numpy as np
import sys
sys.path.insert(0, '/home/jack/ex')

from scc import GraphState, ParameterRegistry, EnergyComputer, find_formation
from scc.optimizer import project_volume

def make_params(**overrides):
    p = ParameterRegistry()
    for k, v in overrides.items():
        setattr(p, k, v)
    return p


def gradient_flow_to_minimizer(u0, graph, params):
    """Use find_formation from u0 to find which minimizer it converges to."""
    res = find_formation(graph, params, normalize=True, u_init=u0)
    return res.u, res.converged, res.n_iter


def compute_hessian_and_soft_mode(u, ec, n):
    """Compute constrained Hessian, soft mode, eigenvalues."""
    tol_box = 1e-6
    free_mask = (u > tol_box) & (u < 1 - tol_box)
    free_idx = np.where(free_mask)[0]
    n_f = len(free_idx)

    if n_f < 3:
        return None

    h = 1e-5
    g0 = ec.gradient(u)
    H = np.zeros((n_f, n_f))
    for j in range(n_f):
        e_j = np.zeros(n)
        e_j[free_idx[j]] = h
        g1 = ec.gradient(u + e_j)
        H[:, j] = ((g1 - g0) / h)[free_idx]
    H = 0.5 * (H + H.T)

    # Project onto volume-constraint tangent space
    ones_f = np.ones(n_f) / np.sqrt(n_f)
    P = np.eye(n_f) - np.outer(ones_f, ones_f)
    H_proj = P @ H @ P
    eigvals, eigvecs = np.linalg.eigh(H_proj)
    nonzero = np.abs(eigvals) > 1e-10
    eigvals = eigvals[nonzero]
    eigvecs = eigvecs[:, nonzero]
    mu = eigvals[0]
    lam_max = np.max(np.linalg.eigvalsh(H))

    soft_mode = np.zeros(n)
    soft_mode[free_idx] = eigvecs[:, 0]
    soft_mode -= np.mean(soft_mode)
    soft_mode /= np.linalg.norm(soft_mode)

    return {
        'mu': mu, 'lam_max': lam_max, 'soft_mode': soft_mode,
        'free_idx': free_idx, 'n_f': n_f,
        'eigvals': eigvals[:min(5, len(eigvals))],
    }


def compute_taylor_coefficients(u_star, soft_mode, ec, m):
    """Compute L3, L4 along soft mode direction via finite differences.

    E(û + t·v) ≈ E(û) + μ/2·t² + L3/6·t³ + L4/24·t⁴

    Uses 5-point stencil for robust estimates.
    """
    def E_at(t):
        u_p = project_volume(np.clip(u_star + t * soft_mode, 0, 1), m)
        E, _ = ec.energy(u_p)
        return E

    E0 = E_at(0)

    # Use multiple step sizes and pick most stable estimate
    results = []
    for h in [0.005, 0.01, 0.02, 0.05]:
        Ep1 = E_at(h)
        Em1 = E_at(-h)
        Ep2 = E_at(2*h)
        Em2 = E_at(-2*h)

        # Second derivative (should match μ)
        E2 = (Ep1 - 2*E0 + Em1) / h**2

        # Third derivative: (-E(2h) + 2E(h) - 2E(-h) + E(-2h)) / (2h³)
        E3 = (-Ep2 + 2*Ep1 - 2*Em1 + Em2) / (2*h**3)

        # Fourth derivative: (E(2h) - 4E(h) + 6E(0) - 4E(-h) + E(-2h)) / h⁴
        E4 = (Ep2 - 4*Ep1 + 6*E0 - 4*Em1 + Em2) / h**4

        results.append({'h': h, 'E2': E2, 'E3': E3, 'E4': E4})

    # Use h=0.01 as primary (good balance of accuracy vs truncation)
    primary = results[1]
    return primary['E2'], primary['E3'], primary['E4'], results


def compute_predicted_barrier(mu, L3, L4):
    """Predict barrier from Taylor coefficients.

    If |L3| is significant (cubic saddle):
      Saddle at t* ≈ -μ/L3 (from E'(t*) = μt* + L3/2·t*² = 0)
      Actually t* = -2μ/L3 from μ + L3·t* = 0 at leading order for E'
      Wait: E'(t) = μt + L3/2·t² + L4/6·t³
      Setting E'=0: t(μ + L3/2·t + L4/6·t²) = 0
      Non-zero root: t* ≈ -2μ/L3 (leading order)
      Barrier: Δ = E(t*) - E(0) = μ/2·t*² + L3/6·t*³
            = μ/2·(4μ²/L3²) + L3/6·(-8μ³/L3³)
            = 2μ³/L3² - 4μ³/(3L3²) = 2μ³/(3L3²)

    If L3 ≈ 0 (quartic saddle):
      E'(t) = μt + L4/6·t³ = 0 → t*² = -6μ/L4 (needs L4 < 0 for real saddle from minimum)
      Actually if μ > 0 and L4 > 0, no saddle from E' = 0 besides t=0
      If L4 < 0: t* = √(6μ/|L4|), Δ = μ/2·t*² + L4/24·t*⁴ = 3μ²/|L4| - 3μ²/(2|L4|) = 3μ²/(2|L4|)
    """
    results = {}

    if abs(L3) > 1e-6:
        t_star_cubic = -2 * mu / L3
        delta_cubic = 2 * mu**3 / (3 * L3**2)
        results['cubic'] = {'t_star': t_star_cubic, 'delta': delta_cubic}

    if L4 < -1e-6:
        t_star_quartic = np.sqrt(6 * mu / abs(L4))
        delta_quartic = 3 * mu**2 / (2 * abs(L4))
        results['quartic'] = {'t_star': t_star_quartic, 'delta': delta_quartic}
    elif L4 > 1e-6 and abs(L3) > 1e-6:
        # With both L3 and L4, solve cubic E'(t)/t = μ + L3/2·t + L4/6·t² = 0
        # t = (-L3/2 ± √(L3²/4 - 4·L4/6·μ)) / (2·L4/6)
        disc = L3**2/4 - 2*L4*mu/3
        if disc > 0:
            t1 = (-L3/2 + np.sqrt(disc)) / (L4/3)
            t2 = (-L3/2 - np.sqrt(disc)) / (L4/3)
            # Pick the one with smaller |t|
            for t_s in sorted([t1, t2], key=abs):
                if abs(t_s) > 1e-8:
                    E_saddle = mu/2 * t_s**2 + L3/6 * t_s**3 + L4/24 * t_s**4
                    if E_saddle > 0:
                        results['full'] = {'t_star': t_s, 'delta': E_saddle}
                        break

    return results


def trace_energy_barrier(u_star, soft_mode, ec, m, max_t=5.0, n_points=1000):
    """Numerically find actual barrier along soft mode."""
    ts = np.linspace(-max_t, max_t, n_points)
    E0, _ = ec.energy(u_star)
    energies = np.zeros(n_points)
    for i, t in enumerate(ts):
        u_p = project_volume(np.clip(u_star + t * soft_mode, 0, 1), m)
        energies[i], _ = ec.energy(u_p)

    center = n_points // 2
    barriers = []
    for direction in [1, -1]:
        for i in range(1, n_points // 2):
            idx = center + direction * i
            prev = center + direction * (i - 1)
            if 0 <= idx < n_points and 0 <= prev < n_points:
                if i > 5 and energies[idx] < energies[prev]:
                    barriers.append(energies[prev] - E0)
                    break
        else:
            edge = center + direction * (n_points // 2 - 1)
            if 0 <= edge < n_points:
                barriers.append(energies[edge] - E0)

    return min(barriers) if barriers else 0.0


def test_basin(n_grid, beta, n_trials=10):
    g = GraphState.grid_2d(n_grid, n_grid)
    p = make_params(beta_bd=beta)
    ec = EnergyComputer(g, p)
    ec.normalize_weights()
    res = find_formation(g, p)
    u_star = res.u
    m = p.volume_fraction * g.n
    n = len(u_star)

    hess = compute_hessian_and_soft_mode(u_star, ec, n)
    if hess is None:
        return None

    soft_mode = hess['soft_mode']
    mu = hess['mu']
    lam_max = hess['lam_max']

    # Compute Taylor coefficients
    E2, L3, L4, taylor_all = compute_taylor_coefficients(u_star, soft_mode, ec, m)

    # Compute actual barrier along soft mode
    delta_actual = trace_energy_barrier(u_star, soft_mode, ec, m)

    # Predicted barrier
    predictions = compute_predicted_barrier(mu, L3, L4)

    # r_soft from sublevel set estimate
    r_soft = np.sqrt(2 * max(delta_actual, 0) / lam_max) if lam_max > 0 else 0

    # Test convergence at increasing distances along soft mode
    soft_results = []
    for eps in [0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 3.0, 5.0]:
        u0 = project_volume(np.clip(u_star + eps * soft_mode, 0, 1), m)
        actual_dist = np.linalg.norm(u0 - u_star)

        u_final, converged, n_iter = gradient_flow_to_minimizer(u0, g, p)
        dist_to_star = np.linalg.norm(u_final - u_star)
        returned = dist_to_star < 0.1

        soft_results.append({
            'eps': eps, 'actual_dist': actual_dist,
            'converged': converged, 'returned': returned,
            'dist_final': dist_to_star, 'n_iter': n_iter,
        })

    # Also test random directions
    rng = np.random.RandomState(42)
    random_results = []
    for eps in [0.1, 0.5, 1.0, 2.0, 5.0]:
        successes = 0
        for trial in range(n_trials):
            v = rng.randn(n)
            v -= np.mean(v)
            v /= np.linalg.norm(v)
            u0 = project_volume(np.clip(u_star + eps * v, 0, 1), m)
            u_final, converged, n_iter = gradient_flow_to_minimizer(u0, g, p)
            dist = np.linalg.norm(u_final - u_star)
            if dist < 0.1:
                successes += 1
        random_results.append({'eps': eps, 'success_rate': successes / n_trials})

    return {
        'mu': mu, 'lam_max': lam_max,
        'soft_mode_results': soft_results,
        'random_results': random_results,
        'n_grid': n_grid, 'beta': beta,
        'E2': E2, 'L3': L3, 'L4': L4,
        'taylor_all': taylor_all,
        'delta_actual': delta_actual,
        'predictions': predictions,
        'r_soft': r_soft,
        'n_f': hess['n_f'],
        'eigvals': hess['eigvals'],
    }


def main():
    print("=" * 100)
    print("EXPERIMENT 24: Actual Basin of Attraction via Gradient Flow")
    print("  + Taylor Coefficient Analysis for Quantitative Δ_bdy Formula")
    print("=" * 100)

    # Focus on the problematic configurations (small r_soft in exp23)
    configs = [
        (8, 50), (10, 100), (12, 150),  # Small r_soft
        (10, 50), (10, 30),  # Larger r_soft for comparison
    ]

    all_results = []

    for n_grid, beta in configs:
        print(f"\n{'='*80}")
        print(f"Grid: {n_grid}x{n_grid}, β={beta}")
        print(f"{'='*80}")

        r = test_basin(n_grid, beta)
        if r is None:
            print("  Too few free variables")
            continue
        all_results.append(r)

        print(f"  μ = {r['mu']:.4f}, λ_max = {r['lam_max']:.4f}, n_free = {r['n_f']}")
        print(f"  First 5 eigenvalues: {[f'{v:.4f}' for v in r['eigvals']]}")

        print(f"\n  --- Taylor Coefficients along soft mode ---")
        print(f"  E''(0) = {r['E2']:.6f}  (should ≈ μ = {r['mu']:.6f})")
        print(f"  L3 = E'''(0) = {r['L3']:.6f}")
        print(f"  L4 = E''''(0) = {r['L4']:.6f}")
        print(f"  |L3|/μ ratio = {abs(r['L3'])/r['mu']:.4f}" if r['mu'] > 1e-10 else "")

        print(f"\n  --- Barrier Analysis ---")
        print(f"  Actual barrier (traced): Δ_actual = {r['delta_actual']:.6f}")
        print(f"  r_soft (sublevel): {r['r_soft']:.4f}")
        for key, pred in r['predictions'].items():
            print(f"  Predicted ({key}): Δ = {pred['delta']:.6f}, t* = {pred['t_star']:.4f}")

        # Stability of Taylor estimates
        print(f"\n  Taylor stability across step sizes:")
        for t in r['taylor_all']:
            print(f"    h={t['h']:.3f}: E2={t['E2']:.4f}, L3={t['E3']:.4f}, L4={t['E4']:.4f}")

        print(f"\n  --- Gradient Flow Basin Test (soft mode direction) ---")
        print(f"  {'ε':<8} {'Actual dist':<14} {'Returned?':<12} {'Final dist':<12} {'Iters':<8}")
        print(f"  {'-'*58}")

        last_good_eps = 0
        for s in r['soft_mode_results']:
            status = 'YES' if s['returned'] else 'no'
            print(f"  {s['eps']:<8.2f} {s['actual_dist']:<14.4f} {status:<12} "
                  f"{s['dist_final']:<12.4f} {s['n_iter']:<8}")
            if s['returned']:
                last_good_eps = s['eps']

        print(f"\n  Empirical soft-mode basin radius: ε ≥ {last_good_eps}")
        if r['r_soft'] > 0:
            ratio = last_good_eps / r['r_soft']
            print(f"  Ratio (empirical / sublevel): {ratio:.1f}x")

        print(f"\n  --- Random Direction Basin Test ---")
        for rr in r['random_results']:
            print(f"  ε={rr['eps']:.1f}: {rr['success_rate']*100:.0f}% return")

    # Summary table
    print(f"\n\n{'='*100}")
    print("SUMMARY: Sublevel Estimate vs Empirical Basin")
    print(f"{'='*100}")
    print(f"{'Config':<14} {'μ':<8} {'Δ_actual':<12} {'r_soft':<10} {'r_empirical':<14} {'Ratio':<8} {'L3':<12} {'L4':<12} {'Δ_pred':<12}")
    print(f"{'-'*100}")

    for r in all_results:
        last_good = 0
        for s in r['soft_mode_results']:
            if s['returned']:
                last_good = s['eps']
        ratio = last_good / r['r_soft'] if r['r_soft'] > 1e-8 else float('inf')

        # Best prediction
        best_pred = 0
        for key, pred in r['predictions'].items():
            if pred['delta'] > best_pred:
                best_pred = pred['delta']

        print(f"{r['n_grid']}x{r['n_grid']} β={r['beta']:<4} "
              f"{r['mu']:<8.4f} {r['delta_actual']:<12.6f} {r['r_soft']:<10.4f} "
              f"ε≥{last_good:<12} {ratio:<8.1f} {r['L3']:<12.4f} {r['L4']:<12.4f} {best_pred:<12.6f}")

    # Δ_bdy formula verification
    print(f"\n\n{'='*100}")
    print("Δ_BDY FORMULA VERIFICATION")
    print("Testing: Δ_bdy ≈ 2μ³/(3·L3²) [cubic] or 3μ²/(2·|L4|) [quartic]")
    print(f"{'='*100}")
    print(f"{'Config':<14} {'Δ_actual':<12} {'Δ_cubic':<12} {'Δ_quartic':<12} {'Δ_full':<12} {'Best fit':<12}")
    print(f"{'-'*80}")

    for r in all_results:
        delta_cubic = 2 * r['mu']**3 / (3 * r['L3']**2) if abs(r['L3']) > 1e-6 else float('inf')
        delta_quartic = 3 * r['mu']**2 / (2 * abs(r['L4'])) if r['L4'] < -1e-6 else float('inf')
        delta_full = r['predictions'].get('full', {}).get('delta', float('inf'))

        errors = {}
        if delta_cubic < 1e6:
            errors['cubic'] = abs(delta_cubic - r['delta_actual']) / max(r['delta_actual'], 1e-10)
        if delta_quartic < 1e6:
            errors['quartic'] = abs(delta_quartic - r['delta_actual']) / max(r['delta_actual'], 1e-10)
        if delta_full < 1e6:
            errors['full'] = abs(delta_full - r['delta_actual']) / max(r['delta_actual'], 1e-10)

        best = min(errors, key=errors.get) if errors else 'N/A'

        print(f"{r['n_grid']}x{r['n_grid']} β={r['beta']:<4} "
              f"{r['delta_actual']:<12.6f} "
              f"{delta_cubic:<12.6f} " if delta_cubic < 1e6 else f"{'N/A':<12} ",
              end="")
        print(f"{delta_quartic:<12.6f} " if delta_quartic < 1e6 else f"{'N/A':<12} ", end="")
        print(f"{delta_full:<12.6f} " if delta_full < 1e6 else f"{'N/A':<12} ", end="")
        print(f"{best} (err={errors.get(best, 0):.1%})" if best != 'N/A' else "N/A")

    print("\n\nKEY FINDINGS:")
    print("1. If empirical basin >> r_soft, sublevel estimate is overly conservative")
    print("2. L3 ≈ 0 → symmetric (quartic) saddle; |L3| >> 0 → asymmetric (cubic) saddle")
    print("3. Formula Δ_bdy should use the full cubic+quartic saddle computation")


if __name__ == '__main__':
    main()
