"""Experiment 33: Semi-analytical Δ_bdy formula via third-derivative decomposition.

Derives and validates:
  a₃ = D³E(û)[v₁,v₁,v₁] ≈ 12·β·λ_bd·S₃
where S₃ = Σ_{i∈bdy} (2û_i - 1)·v₁_i³  is the "skewed third moment"
across the boundary layer.

When |S₃| is appreciable (cubic regime):
  Δ_bdy ≈ 2μ³/(3·a₃²)

When S₃ ≈ 0 (symmetric boundary, quartic regime):
  Δ_bdy ≈ 3μ²/(2·a₄)    where  a₄ = 24·β·λ_bd·Σ v₁_i⁴

Compares analytical a₃ against numerical FD a₃, and Δ_predicted vs Δ_measured.

Also computes component-wise decomposition a₃ = a₃_bd + a₃_cl + a₃_sep
to diagnose configurations where E_cl/E_sep third derivatives are non-negligible
(e.g., 12×12 β=50 near shape bifurcation).
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


def compute_soft_mode(u, graph, ec):
    """Compute softest eigenvector of the constrained Hessian on free variables."""
    n = len(u)
    tol = 1e-6
    free_mask = (u > tol) & (u < 1 - tol)
    free_idx = np.where(free_mask)[0]
    n_f = len(free_idx)
    if n_f < 3:
        return None, None, None, None

    h = 1e-5
    g0 = ec.gradient(u)
    H = np.zeros((n_f, n_f))
    for j in range(n_f):
        e_j = np.zeros(n)
        e_j[free_idx[j]] = h
        g1 = ec.gradient(u + e_j)
        H[:, j] = ((g1 - g0) / h)[free_idx]
    H = 0.5 * (H + H.T)

    # Project onto Σ_m tangent space
    ones_f = np.ones(n_f) / np.sqrt(n_f)
    P = np.eye(n_f) - np.outer(ones_f, ones_f)
    H_proj = P @ H @ P
    eigvals, eigvecs = np.linalg.eigh(H_proj)
    nonzero = np.abs(eigvals) > 1e-10
    eigvals = eigvals[nonzero]
    eigvecs = eigvecs[:, nonzero]

    # Expand softest mode to full space
    soft_mode = np.zeros(n)
    soft_mode[free_idx] = eigvecs[:, 0]
    soft_mode -= np.mean(soft_mode)
    norm = np.linalg.norm(soft_mode)
    if norm > 1e-15:
        soft_mode /= norm

    lam_max = np.max(np.linalg.eigvalsh(H))
    return eigvals[0], soft_mode, free_idx, lam_max


def compute_a3_numerical(u, v1, ec, m, h=0.005):
    """Numerical 3rd derivative D³E[v₁,v₁,v₁] via central FD.

    Uses: [E(u+2hv) - 2E(u+hv) + 2E(u-hv) - E(u-2hv)] / (2h³)
    """
    def eval_E(t):
        u_p = np.clip(u + t * v1, 0, 1)
        u_p = project_volume(u_p, m)
        E, _ = ec.energy(u_p)
        return E

    E_2p = eval_E(2 * h)
    E_p = eval_E(h)
    E_m = eval_E(-h)
    E_2m = eval_E(-2 * h)
    return (E_2p - 2 * E_p + 2 * E_m - E_2m) / (2 * h**3)


def compute_a3_component(u, v1, graph, params, ec, m, component='total', h=0.005):
    """Numerical 3rd derivative for a single energy component via central FD."""
    from scc.energy import energy_bd, energy_cl, energy_sep

    def eval_E(t):
        u_p = np.clip(u + t * v1, 0, 1)
        u_p = project_volume(u_p, m)
        if component == 'total':
            E, _ = ec.energy(u_p)
            return E
        elif component == 'bd':
            return ec.lambda_bd * energy_bd(u_p, graph, params)
        elif component == 'cl':
            return ec.lambda_cl * energy_cl(u_p, graph, params)
        elif component == 'sep':
            return ec.lambda_sep * energy_sep(u_p, graph, params)

    E_2p = eval_E(2 * h)
    E_p = eval_E(h)
    E_m = eval_E(-h)
    E_2m = eval_E(-2 * h)
    return (E_2p - 2 * E_p + 2 * E_m - E_2m) / (2 * h**3)


def compute_a4_numerical(u, v1, ec, m, h=0.005):
    """Numerical 4th derivative D⁴E[v₁⁴] via central FD.

    Uses: [E(u+2hv) - 4E(u+hv) + 6E(u) - 4E(u-hv) + E(u-2hv)] / h⁴
    """
    def eval_E(t):
        u_p = np.clip(u + t * v1, 0, 1)
        u_p = project_volume(u_p, m)
        E, _ = ec.energy(u_p)
        return E

    E0 = eval_E(0)
    E_2p = eval_E(2 * h)
    E_p = eval_E(h)
    E_m = eval_E(-h)
    E_2m = eval_E(-2 * h)
    return (E_2p - 4 * E_p + 6 * E0 - 4 * E_m + E_2m) / h**4


def find_barrier_along_mode(u, v1, ec, m, max_t=5.0, n_points=2000):
    """Trace E along soft mode and find barrier height."""
    ts = np.linspace(-max_t, max_t, n_points)
    energies = np.zeros(n_points)
    for i, t in enumerate(ts):
        u_p = np.clip(u + t * v1, 0, 1)
        u_p = project_volume(u_p, m)
        E, _ = ec.energy(u_p)
        energies[i] = E

    center = n_points // 2
    E0 = energies[center]
    barriers = []
    for direction in [1, -1]:
        for i in range(1, n_points // 2):
            idx = center + direction * i
            prev = center + direction * (i - 1)
            if 0 <= idx < n_points and i > 5:
                if energies[idx] < energies[prev]:
                    barriers.append(energies[prev] - E0)
                    break
        else:
            idx = center + direction * (n_points // 2 - 1)
            if 0 <= idx < n_points:
                barriers.append(energies[idx] - E0)

    return min(barriers) if barriers else 0.0


def classify_nodes(u, theta_ext=0.1, theta_core=0.9):
    """Classify nodes into core, boundary, exterior."""
    core = u >= theta_core
    ext = u <= theta_ext
    bdy = ~core & ~ext
    return core, bdy, ext


def main():
    print("=" * 110)
    print("EXPERIMENT 33: Semi-Analytical Δ_bdy Formula — Third-Derivative Decomposition")
    print("=" * 110)

    # W'''(u) = d³/du³ [u²(1-u)²]
    # W(u) = u⁴ - 2u³ + u²
    # W'(u) = 4u³ - 6u² + 2u = 2u(1-u)(1-2u)
    # W''(u) = 12u² - 12u + 2 = 2(6u² - 6u + 1)
    # W'''(u) = 24u - 12 = 12(2u - 1)
    print("\nW'''(u) = 12(2u-1)  — third derivative of double-well potential")
    print("a₃_analytical = 12·β·λ_bd·S₃  where  S₃ = Σ_i (2û_i - 1)·v₁_i³")
    print("Δ_cubic = 2μ³/(3·a₃²)  when |S₃| appreciable")
    print("Δ_quartic = 3μ²/(2·a₄)  when S₃ ≈ 0, a₄ = 24·β·λ_bd·Σ v₁_i⁴")

    configs = [
        (8, 20), (8, 50), (10, 50), (10, 100), (12, 50), (12, 100), (15, 50),
    ]

    print(f"\n{'Config':<12} {'μ':<8} {'S₃':<12} {'a₃_ana':<12} {'a₃_num':<12} "
          f"{'a₃ ratio':<10} {'Δ_meas':<12} {'Δ_pred':<12} {'Δ ratio':<10} {'Regime':<10}")
    print("-" * 118)

    results = []

    for n_grid, beta in configs:
        try:
            g = GraphState.grid_2d(n_grid, n_grid)
            p = make_params(beta_bd=beta)
            ec = EnergyComputer(g, p)
            ec.normalize_weights()
            res = find_formation(g, p)
            u = res.u
            m = p.volume_fraction * g.n

            mu, v1, free_idx, lam_max = compute_soft_mode(u, g, ec)
            if v1 is None:
                print(f"{n_grid}x{n_grid} β={beta:<4}  SKIP (too few free vars)")
                continue

            # Classify nodes
            core, bdy, ext = classify_nodes(u)

            # S₃ = Σ_i (2û_i - 1)·v₁_i³  (sum over ALL nodes, but dominated by boundary)
            S3 = np.sum((2 * u - 1) * v1**3)
            S3_bdy = np.sum((2 * u[bdy] - 1) * v1[bdy]**3)

            # a₃ analytical: contribution from E_bd only
            # D³E_bd[v₁³] = β·Σ_i W'''(û_i)·v₁_i³ = β·12·Σ_i (2û_i-1)·v₁_i³
            # But this is the unweighted E_bd derivative. The total energy uses λ_bd weight.
            a3_analytical = 12.0 * p.beta_bd * ec.lambda_bd * S3

            # a₃ numerical (central FD of total energy)
            a3_numerical = compute_a3_numerical(u, v1, ec, m, h=0.005)

            # a₄ for quartic regime
            S4 = np.sum(v1**4)  # Σ v₁_i⁴
            # W''''(u) = 24, so a₄ = 24·β·λ_bd·Σ v₁_i⁴ (from E_bd only)
            a4_analytical = 24.0 * p.beta_bd * ec.lambda_bd * S4
            a4_numerical = compute_a4_numerical(u, v1, ec, m, h=0.005)

            # Measured barrier
            delta_measured = find_barrier_along_mode(u, v1, ec, m, max_t=5.0)

            # Classify regime
            # Use |a₃|/μ vs threshold to decide cubic vs quartic
            S3_threshold = 1e-4
            if abs(S3) > S3_threshold:
                regime = "cubic"
                # Δ_cubic = 2μ³/(3·a₃²) using NUMERICAL a₃ for fair comparison
                delta_cubic_ana = 2 * mu**3 / (3 * a3_analytical**2) if abs(a3_analytical) > 1e-15 else float('inf')
                delta_cubic_num = 2 * mu**3 / (3 * a3_numerical**2) if abs(a3_numerical) > 1e-15 else float('inf')
                delta_predicted = delta_cubic_ana
            else:
                regime = "quartic"
                # Δ_quartic = 3μ²/(2·|a₄|)
                delta_predicted = 3 * mu**2 / (2 * abs(a4_analytical)) if abs(a4_analytical) > 1e-15 else float('inf')

            a3_ratio = a3_analytical / a3_numerical if abs(a3_numerical) > 1e-15 else float('inf')
            delta_ratio = delta_predicted / delta_measured if delta_measured > 1e-15 else float('inf')

            print(f"{n_grid}x{n_grid} β={beta:<4} {mu:<8.4f} {S3:<12.6f} {a3_analytical:<12.4f} "
                  f"{a3_numerical:<12.4f} {a3_ratio:<10.4f} {delta_measured:<12.6f} "
                  f"{delta_predicted:<12.6f} {delta_ratio:<10.4f} {regime:<10}")

            results.append({
                'config': f"{n_grid}x{n_grid} β={beta}",
                'n_grid': n_grid, 'beta': beta,
                'mu': mu, 'lam_max': lam_max,
                'S3': S3, 'S3_bdy': S3_bdy, 'S4': S4,
                'a3_ana': a3_analytical, 'a3_num': a3_numerical,
                'a4_ana': a4_analytical, 'a4_num': a4_numerical,
                'delta_meas': delta_measured, 'delta_pred': delta_predicted,
                'regime': regime,
            })

        except Exception as e:
            print(f"{n_grid}x{n_grid} β={beta:<4}  ERROR: {e}")
            import traceback; traceback.print_exc()

    # -----------------------------------------------------------------------
    # Detailed analysis
    # -----------------------------------------------------------------------
    print("\n\n" + "=" * 110)
    print("DETAILED ANALYSIS")
    print("=" * 110)

    print("\n--- a₃ Decomposition: Smoothness vs Double-Well Contributions ---")
    print(f"{'Config':<14} {'a₃(DW)':<12} {'a₃(num)':<12} {'a₃(DW)/a₃(num)':<16} "
          f"{'S₃(all)':<12} {'S₃(bdy)':<12} {'S₃ bdy frac':<12}")
    print("-" * 100)
    for r in results:
        bdy_frac = r['S3_bdy'] / r['S3'] if abs(r['S3']) > 1e-15 else float('nan')
        print(f"{r['config']:<14} {r['a3_ana']:<12.4f} {r['a3_num']:<12.4f} "
              f"{r['a3_ana']/r['a3_num'] if abs(r['a3_num'])>1e-15 else float('inf'):<16.4f} "
              f"{r['S3']:<12.6f} {r['S3_bdy']:<12.6f} {bdy_frac:<12.4f}")

    print("\n--- a₄ Comparison ---")
    print(f"{'Config':<14} {'a₄_ana':<12} {'a₄_num':<12} {'a₄ ratio':<12} {'S₄':<12}")
    print("-" * 62)
    for r in results:
        a4_ratio = r['a4_ana'] / r['a4_num'] if abs(r['a4_num']) > 1e-15 else float('inf')
        print(f"{r['config']:<14} {r['a4_ana']:<12.4f} {r['a4_num']:<12.4f} "
              f"{a4_ratio:<12.4f} {r['S4']:<12.6f}")

    # Full Taylor barrier comparison
    print("\n--- Full Taylor Barrier vs Measured ---")
    print(f"{'Config':<14} {'μ':<8} {'t*(cubic)':<12} {'t*(full)':<12} "
          f"{'Δ_cubic':<12} {'Δ_full':<12} {'Δ_meas':<12} {'full/meas':<10}")
    print("-" * 100)
    for r in results:
        mu = r['mu']
        L3 = r['a3_num']  # use numerical for full formula
        L4 = r['a4_num']

        # Cubic approximation for t*
        t_cubic = -2 * mu / L3 if abs(L3) > 1e-15 else float('inf')
        delta_cubic = 2 * mu**3 / (3 * L3**2) if abs(L3) > 1e-15 else float('inf')

        # Full quartic: t*(μ + L₃/2·t* + L₄/6·t*²) = 0
        # Quadratic: L₄/6·t*² + L₃/2·t* + μ = 0
        # t* = (-3L₃ ± √(9L₃² - 24μL₄)) / (2L₄)
        disc = 9 * L3**2 - 24 * mu * L4
        if disc >= 0 and abs(L4) > 1e-15:
            sqrt_disc = np.sqrt(disc)
            t1 = (-3 * L3 + sqrt_disc) / (2 * L4)
            t2 = (-3 * L3 - sqrt_disc) / (2 * L4)
            # Pick the root closer to 0 (saddle nearest to minimizer)
            candidates = [t for t in [t1, t2] if abs(t) > 1e-15]
            if candidates:
                t_full = min(candidates, key=abs)
            else:
                t_full = t_cubic
        else:
            t_full = t_cubic

        delta_full = mu / 2 * t_full**2 + L3 / 6 * t_full**3 + L4 / 24 * t_full**4

        ratio = delta_full / r['delta_meas'] if r['delta_meas'] > 1e-15 else float('inf')
        print(f"{r['config']:<14} {mu:<8.4f} {t_cubic:<12.6f} {t_full:<12.6f} "
              f"{delta_cubic:<12.6f} {delta_full:<12.6f} {r['delta_meas']:<12.6f} {ratio:<10.4f}")

    # Summary
    print("\n\n" + "=" * 110)
    print("SUMMARY")
    print("=" * 110)
    print("""
Δ_bdy as a semi-analytical function of formation parameters:

  1. Compute the soft mode v₁ (minimum constrained Hessian eigenvector).
  2. Compute S₃ = Σ_i (2û_i - 1)·v₁_i³   — skewed third moment.
  3. If |S₃| > threshold (cubic regime):
       a₃ = 12·β·λ_bd·S₃
       Δ_bdy ≈ 2μ³/(3·a₃²)
     Else (quartic regime):
       a₄ = 24·β·λ_bd·Σ v₁_i⁴
       Δ_bdy ≈ 3μ²/(2·a₄)

  Physical interpretation:
  - S₃ measures the asymmetry of the soft mode across the boundary layer.
  - When boundary nodes are distributed symmetrically around u=0.5
    (equal amounts above and below), the factors (2û_i - 1) cancel and S₃ ≈ 0.
  - Asymmetric boundaries (more nodes on one side of the spinodal) give |S₃| > 0,
    producing a cubic saddle with lower barrier.

  Key identity: W'''(u) = 12(2u - 1)
  This is why (2û_i - 1) appears — it is W'''(û_i)/12, the local curvature
  asymmetry of the double-well at each node.
""")

    # -----------------------------------------------------------------------
    # Component decomposition: a₃ = a₃_bd + a₃_cl + a₃_sep
    # -----------------------------------------------------------------------
    print("\n" + "=" * 110)
    print("COMPONENT DECOMPOSITION: a3 = a3_bd + a3_cl + a3_sep")
    print("=" * 110)
    print(f"\n{'Config':<14} {'a₃_bd(FD)':<12} {'a₃_cl(FD)':<12} {'a₃_sep(FD)':<12} "
          f"{'a₃_total':<12} {'|cl+sep|/|tot|':<16}")
    print("-" * 80)

    for n_grid, beta in configs:
        try:
            g = GraphState.grid_2d(n_grid, n_grid)
            p = make_params(beta_bd=beta)
            ec = EnergyComputer(g, p)
            ec.normalize_weights()
            res = find_formation(g, p)
            u = res.u
            m = p.volume_fraction * g.n

            mu, v1, free_idx, lam_max = compute_soft_mode(u, g, ec)
            if v1 is None:
                continue

            a3_bd = compute_a3_component(u, v1, g, p, ec, m, 'bd')
            a3_cl = compute_a3_component(u, v1, g, p, ec, m, 'cl')
            a3_sep = compute_a3_component(u, v1, g, p, ec, m, 'sep')
            a3_total = compute_a3_component(u, v1, g, p, ec, m, 'total')

            clsep_frac = abs(a3_cl + a3_sep) / abs(a3_total) if abs(a3_total) > 1e-15 else float('inf')

            print(f"{n_grid}x{n_grid} β={beta:<4} {a3_bd:<12.4f} {a3_cl:<12.4f} {a3_sep:<12.4f} "
                  f"{a3_total:<12.4f} {clsep_frac:<16.1%}")

        except Exception as e:
            print(f"{n_grid}x{n_grid} β={beta:<4}  ERROR: {e}")


if __name__ == '__main__':
    main()
