#!/usr/bin/env python3
"""Experiment 58: T-Bind-Proj τ-dependence — r̄₀ vs τ across grid sizes.

Measures the mean closure residual r̄₀ = |Σ(Cl(u) - u)| / n at constrained
minimizers for τ ∈ {0.1, 0.15, 0.2, ..., 0.9} and grid sizes 5×5 to 20×20.

This provides the experimental baseline for upgrading T-Bind-Proj from
Category B (general τ) to Category A.

Key quantities measured at each (τ, n):
  - r_bar_0: per-site mean closure residual
  - r_T_norm: tangential residual ‖r_T‖₂/√n
  - bind: Bind diagnostic value
  - delta_plus, delta_minus: bulk residuals at core/exterior
  - transition_layer_size: |T| (sites with ε < u < 1-ε)
"""
import sys, os, time, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.operators import closure, closure_with_jacobian, sigmoid

# Sweep parameters
TAU_VALUES = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5,
              0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9]
GRID_SIDES = [5, 10, 15, 20]
N_RESTARTS = 3
MAX_ITER = 3000
BETA = 50.0
VOLUME_FRACTION = 0.3
A_CL = 3.5  # default, in contraction regime


def measure_residual(u, graph, params):
    """Measure all closure-residual quantities at field u."""
    n = graph.n
    Cl_u, sigma_prime, z = closure_with_jacobian(u, graph, params)
    r = Cl_u - u  # closure residual

    # r̄₀ = |Σ r_i| / n
    r_bar_0 = abs(np.sum(r)) / n

    # ‖r‖₂² / n = E_cl / n
    r_l2_sq_per_n = np.dot(r, r) / n

    # Tangential residual: r_T = r - (1ᵀr/n)·1
    r_mean = np.mean(r)
    r_T = r - r_mean
    r_T_norm = np.sqrt(np.dot(r_T, r_T) / n)

    # Bind = 1 - ‖r‖₂/√n (spec formula)
    bind = 1.0 - np.sqrt(r_l2_sq_per_n)

    # Bulk analysis: δ₊, δ₋
    tau = params.tau_cl
    a = params.a_cl
    delta_plus = 1.0 - float(sigmoid(np.array([a * (1.0 - tau)]))[0])
    delta_minus = float(sigmoid(np.array([-a * tau]))[0])

    # Transition layer: sites with ε < u < 1-ε
    eps = 0.1
    transition = np.sum((u > eps) & (u < 1.0 - eps))

    # Core/exterior classification
    core = np.sum(u >= 0.8)
    exterior = np.sum(u <= 0.2)

    # Theoretical bulk r̄₀ for binary profile
    c = params.volume_fraction
    r_bar_0_binary = abs((1 - c) * delta_minus - c * delta_plus)

    # Covariance term: Cov(s, r) / n
    s = sigma_prime  # σ'(z) = Cl(u)·(1-Cl(u))
    s_bar = np.mean(s)
    cov_sr = np.sum((s - s_bar) * r) / n

    return {
        'r_bar_0': float(r_bar_0),
        'r_T_norm': float(r_T_norm),
        'r_l2_per_sqrt_n': float(np.sqrt(r_l2_sq_per_n)),
        'bind': float(bind),
        'delta_plus': float(delta_plus),
        'delta_minus': float(delta_minus),
        'delta_asymmetry': float(abs(delta_plus - delta_minus)),
        'r_bar_0_binary_theory': float(r_bar_0_binary),
        'transition_layer_size': int(transition),
        'core_size': int(core),
        'exterior_size': int(exterior),
        'cov_sr_per_n': float(cov_sr),
        'mean_sigma_prime': float(s_bar),
    }


def run_single(side, tau, verbose=True):
    """Run formation finding and measure residuals for one (side, τ) pair."""
    graph = GraphState.grid_2d(side, side)
    n = side * side
    params = ParameterRegistry(
        tau_cl=tau,
        a_cl=A_CL,
        beta_bd=BETA,
        volume_fraction=VOLUME_FRACTION,
        max_iter=MAX_ITER,
        n_restarts=N_RESTARTS,
    )

    t0 = time.time()
    try:
        res = find_formation(graph, params, verbose=False)
        elapsed = time.time() - t0

        u = res.u
        residuals = measure_residual(u, graph, params)

        result = {
            'side': side,
            'n': n,
            'tau': tau,
            'converged': res.converged,
            'n_iter': res.n_iter,
            'energy': float(res.energy),
            'time_sec': round(elapsed, 2),
            **residuals,
        }
    except Exception as e:
        elapsed = time.time() - t0
        result = {
            'side': side,
            'n': n,
            'tau': tau,
            'converged': False,
            'error': str(e),
            'time_sec': round(elapsed, 2),
            'r_bar_0': float('nan'),
        }

    if verbose:
        r0 = result.get('r_bar_0', float('nan'))
        bind = result.get('bind', float('nan'))
        conv = result.get('converged', False)
        print(f"  τ={tau:.2f} n={n:>4} | r̄₀={r0:.6f} Bind={bind:.4f} conv={conv}")

    return result


def main():
    print("=" * 70)
    print("Experiment 58: T-Bind-Proj τ-Dependence Sweep")
    print(f"τ ∈ {TAU_VALUES}")
    print(f"Grids: {[f'{s}×{s}' for s in GRID_SIDES]}")
    print(f"a_cl={A_CL}, β={BETA}, c={VOLUME_FRACTION}")
    print("=" * 70)

    t_start = time.time()
    all_results = []

    for side in GRID_SIDES:
        print(f"\n--- Grid {side}×{side} (n={side*side}) ---")
        for tau in TAU_VALUES:
            result = run_single(side, tau)
            all_results.append(result)

    total_time = time.time() - t_start

    # ===== Analysis =====
    print("\n" + "=" * 70)
    print("ANALYSIS")
    print("=" * 70)

    # Table 1: r̄₀ vs τ for each grid
    print("\n### Table 1: r̄₀(τ, n) — Mean Closure Residual")
    header = f"{'τ':>6}"
    for s in GRID_SIDES:
        header += f" | {s}×{s:>2}{'':>6}"
    print(header)
    print("-" * len(header))

    for tau in TAU_VALUES:
        row = f"{tau:>6.2f}"
        for side in GRID_SIDES:
            match = [r for r in all_results
                     if r['side'] == side and r['tau'] == tau]
            if match and not np.isnan(match[0]['r_bar_0']):
                row += f" | {match[0]['r_bar_0']:>10.6f}"
            else:
                row += f" | {'N/A':>10}"
        print(row)

    # Table 2: Bind vs τ for each grid
    print("\n### Table 2: Bind(τ, n)")
    header = f"{'τ':>6}"
    for s in GRID_SIDES:
        header += f" | {s}×{s:>2}{'':>6}"
    print(header)
    print("-" * len(header))

    for tau in TAU_VALUES:
        row = f"{tau:>6.2f}"
        for side in GRID_SIDES:
            match = [r for r in all_results
                     if r['side'] == side and r['tau'] == tau]
            if match and 'bind' in match[0] and not np.isnan(match[0].get('bind', float('nan'))):
                row += f" | {match[0]['bind']:>10.4f}"
            else:
                row += f" | {'N/A':>10}"
        print(row)

    # Table 3: δ asymmetry vs τ (grid-independent)
    print("\n### Table 3: Bulk Asymmetry δ₊ - δ₋ vs τ")
    print(f"{'τ':>6} | {'δ₊':>10} | {'δ₋':>10} | {'|δ₊-δ₋|':>10} | {'r̄₀(binary)':>12}")
    print("-" * 60)
    for tau in TAU_VALUES:
        match = [r for r in all_results if r['tau'] == tau and 'delta_plus' in r]
        if match:
            r = match[0]
            print(f"{tau:>6.2f} | {r['delta_plus']:>10.6f} | {r['delta_minus']:>10.6f} "
                  f"| {r['delta_asymmetry']:>10.6f} | {r['r_bar_0_binary_theory']:>12.6f}")

    # Curve fitting for largest grid
    print("\n### Curve Fitting: r̄₀ vs τ (20×20 grid)")
    largest = max(GRID_SIDES)
    data_large = [(r['tau'], r['r_bar_0']) for r in all_results
                  if r['side'] == largest and not np.isnan(r['r_bar_0'])]

    if len(data_large) >= 5:
        taus = np.array([d[0] for d in data_large])
        r0s = np.array([d[1] for d in data_large])

        # Fit 1: r̄₀ = a|τ - 1/2| + b
        x_abs = np.abs(taus - 0.5)
        A_lin = np.column_stack([x_abs, np.ones_like(x_abs)])
        coeffs_lin, res_lin, _, _ = np.linalg.lstsq(A_lin, r0s, rcond=None)
        r0_lin = A_lin @ coeffs_lin
        ss_res_lin = np.sum((r0s - r0_lin) ** 2)
        ss_tot = np.sum((r0s - np.mean(r0s)) ** 2)
        R2_lin = 1.0 - ss_res_lin / ss_tot if ss_tot > 0 else 0.0
        print(f"  Linear: r̄₀ = {coeffs_lin[0]:.6f}|τ-0.5| + {coeffs_lin[1]:.6f}  (R²={R2_lin:.6f})")

        # Fit 2: r̄₀ = a(τ - 1/2)² + b
        x_sq = (taus - 0.5) ** 2
        A_quad = np.column_stack([x_sq, np.ones_like(x_sq)])
        coeffs_quad, _, _, _ = np.linalg.lstsq(A_quad, r0s, rcond=None)
        r0_quad = A_quad @ coeffs_quad
        ss_res_quad = np.sum((r0s - r0_quad) ** 2)
        R2_quad = 1.0 - ss_res_quad / ss_tot if ss_tot > 0 else 0.0
        print(f"  Quadratic: r̄₀ = {coeffs_quad[0]:.6f}(τ-0.5)² + {coeffs_quad[1]:.6f}  (R²={R2_quad:.6f})")

        # Fit 3: r̄₀ = a|τ-0.5|^p + b (power law)
        # Use log fit on |τ-0.5| > 0
        mask = x_abs > 0.01
        if np.sum(mask) >= 4 and np.all(r0s[mask] > 0):
            try:
                from scipy.optimize import curve_fit

                def power_model(x, a, p, b):
                    return a * np.abs(x - 0.5) ** p + b

                popt, pcov = curve_fit(power_model, taus[mask], r0s[mask],
                                       p0=[0.1, 1.0, 0.001], maxfev=5000,
                                       bounds=([0, 0.1, 0], [10, 5, 1]))
                r0_power = power_model(taus, *popt)
                ss_res_pow = np.sum((r0s - r0_power) ** 2)
                R2_pow = 1.0 - ss_res_pow / ss_tot if ss_tot > 0 else 0.0
                print(f"  Power: r̄₀ = {popt[0]:.6f}|τ-0.5|^{popt[1]:.3f} + {popt[2]:.6f}  (R²={R2_pow:.6f})")
            except Exception as e:
                print(f"  Power fit failed: {e}")
                R2_pow = -1

        # Best fit
        fits = [('Linear', R2_lin), ('Quadratic', R2_quad)]
        if 'R2_pow' in dir() and R2_pow > 0:
            fits.append(('Power', R2_pow))
        best = max(fits, key=lambda x: x[1])
        print(f"\n  Best fit: {best[0]} (R²={best[1]:.6f})")

    # n-scaling analysis: for each τ, fit log(r̄₀) vs log(n)
    print("\n### n-Scaling: r̄₀ ∝ n^α")
    print(f"{'τ':>6} | {'slope α':>10} | {'expected':>10} | {'match?':>8}")
    print("-" * 50)
    for tau in TAU_VALUES:
        data_tau = [(r['n'], r['r_bar_0']) for r in all_results
                    if r['tau'] == tau and not np.isnan(r['r_bar_0']) and r['r_bar_0'] > 1e-10]
        if len(data_tau) >= 3:
            ns = np.array([d[0] for d in data_tau])
            r0s = np.array([d[1] for d in data_tau])
            # Only fit if there's variation
            if r0s.max() / max(r0s.min(), 1e-15) > 1.2:
                log_n = np.log(ns)
                log_r = np.log(r0s)
                slope, intercept = np.polyfit(log_n, log_r, 1)
                expected = -0.5 if abs(tau - 0.5) < 0.05 else 0.0
                match = "YES" if abs(slope - expected) < 0.3 else "NO"
                print(f"{tau:>6.2f} | {slope:>10.3f} | {expected:>10.1f} | {match:>8}")
            else:
                print(f"{tau:>6.2f} | {'flat':>10} | {'~0':>10} | {'~':>8}")
        else:
            print(f"{tau:>6.2f} | {'N/A':>10} | {'':>10} | {'':>8}")

    # Save results
    summary = {
        'experiment': 'exp58_bind_tau_sweep',
        'params': {
            'a_cl': A_CL, 'beta': BETA, 'volume_fraction': VOLUME_FRACTION,
            'n_restarts': N_RESTARTS, 'max_iter': MAX_ITER,
        },
        'tau_values': TAU_VALUES,
        'grid_sides': GRID_SIDES,
        'results': all_results,
        'total_time_sec': round(total_time, 2),
    }

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'exp58_bind_tau_sweep.json')
    with open(out_path, 'w') as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")
    print(f"Total time: {total_time:.1f}s")

    return summary


if __name__ == '__main__':
    main()
