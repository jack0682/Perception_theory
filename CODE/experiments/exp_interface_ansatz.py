#!/usr/bin/env python3
"""
exp_interface_ansatz.py — Round 13 Corollary 2.2 direct mathematical validation.

Bypasses find_formation entirely. Constructs K=1 blob analytically with
controlled interface width ξ_0, measures |B| and Per directly.

This isolates the MATHEMATICAL scaling of Cor 2.2 from the separate
question of whether find_formation converges to K=1 single mode.

Cor 2.2 (Round 13 §2.5.4):
  |B(u*)| ≤ C · ξ_0 · Per_G(A*)
  where B = {x : 0.1 < u_x < 0.9}, A* = {x : u_x ≥ 0.5}.

Test protocol:
  1. For each (grid_size, ξ_0, profile_type):
     a. Construct u = blob with tanh (or linear, or step) profile of width ξ_0
     b. Normalize to Σu = m (volume c·n)
     c. Measure |B|, Per_edge, Per_site
  2. Fit |B|/Per vs ξ_0.
  3. Compare profile types.

Three profile types:
  - 'tanh'   : u(x) = 0.5·(1 - tanh((d(x) - r_0) / ξ_0))    (smooth)
  - 'linear' : u(x) = clip(0.5 + (r_0 - d(x))/ξ_0, 0, 1)    (piecewise linear)
  - 'step'   : u(x) = 1 if d < r_0 else 0                    (sharp limit)

Expected Cor 2.2 behavior:
  - tanh: clean Modica-Mortola regime, |B|/Per ∝ ξ_0
  - linear: similar scaling with different constant
  - step: |B| = 0 (no transition band) → tests limit

Expected runtime: < 1 minute (no optimization, just u construction + measurement).

Usage:
  cd CODE && python3 experiments/exp_interface_ansatz.py [--grid-sizes 32,64,96]
"""
import sys, os, time, json, argparse
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState


def construct_ansatz(grid_size, xi_0, c=0.3, profile='tanh'):
    """Construct blob u on grid with controlled interface width ξ_0 (in lattice units).

    Strategy: place circular blob at center, choose radius to match volume,
    apply profile function of distance.
    """
    L = grid_size
    n = L * L
    m_target = c * n

    # Set up coordinates (grid 2D)
    xs, ys = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
    cx, cy = (L - 1) / 2.0, (L - 1) / 2.0

    # Distance from center
    d = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2)

    # Find radius r_0 such that Σu ≈ m_target (for given profile and ξ_0)
    # We'll bisect on r_0
    def u_from_r(r_0):
        if profile == 'tanh':
            u = 0.5 * (1.0 - np.tanh((d - r_0) / max(xi_0, 1e-6)))
        elif profile == 'linear':
            arg = (r_0 - d) / max(xi_0, 1e-6)
            u = np.clip(0.5 + 0.5 * arg, 0.0, 1.0)
        elif profile == 'step':
            u = (d < r_0).astype(float)
        else:
            raise ValueError(f"unknown profile: {profile}")
        return u.flatten()

    # Bisect r_0
    r_lo, r_hi = 0.0, L * 0.9
    for _ in range(60):
        r_mid = 0.5 * (r_lo + r_hi)
        u_mid = u_from_r(r_mid)
        m_mid = u_mid.sum()
        if m_mid < m_target:
            r_lo = r_mid
        else:
            r_hi = r_mid

    r_0 = 0.5 * (r_lo + r_hi)
    u = u_from_r(r_0)

    # Rescale to exact mass
    if profile != 'step':
        u = np.clip(u, 1e-4, 1.0 - 1e-4)
    s = u.sum()
    if s > 0:
        u = u * (m_target / s)
    u = np.clip(u, 0.0, 1.0)

    return u, r_0


def measure_interface(u, graph, theta_low=0.1, theta_high=0.9, theta_core=0.5):
    n = graph.n
    W = graph.W.tocsr()

    in_band = (u > theta_low) & (u < theta_high)
    interface_size = int(np.sum(in_band))

    in_core = u >= theta_core
    core_size = int(np.sum(in_core))

    # Edge perimeter
    per_edge = 0
    site_bd = 0
    for i in range(n):
        if not in_core[i]:
            continue
        has_external_neighbor = False
        neighbors = W[i].indices
        for j in neighbors:
            if not in_core[j]:
                has_external_neighbor = True
                if j > i:
                    per_edge += 1
        if has_external_neighbor:
            site_bd += 1

    return {
        'interface_size': interface_size,
        'core_size': core_size,
        'per_edge': per_edge,
        'site_bd': site_bd,
    }


def run_one(grid_size, xi_0, c, profile):
    graph = GraphState.grid_2d(grid_size, grid_size)
    u, r_0 = construct_ansatz(grid_size, xi_0, c, profile)
    meas = measure_interface(u, graph)

    ratio_edge = (meas['interface_size'] / meas['per_edge']
                  if meas['per_edge'] > 0 else float('nan'))
    ratio_site = (meas['interface_size'] / meas['site_bd']
                  if meas['site_bd'] > 0 else float('nan'))

    # Theoretical continuum perimeter (disk)
    per_continuum = 2 * np.pi * r_0

    return {
        'grid_size': grid_size, 'n': grid_size ** 2,
        'xi_0': float(xi_0),
        'profile': profile,
        'r_0': float(r_0),
        'per_continuum': float(per_continuum),
        'u_max': float(u.max()), 'u_min': float(u.min()),
        'mass_achieved': float(u.sum()),
        'mass_target': float(c * grid_size ** 2),
        **meas,
        'ratio_edge': ratio_edge,
        'ratio_site': ratio_site,
    }


def loglog_fit(xi_arr, ratio_arr):
    mask = (ratio_arr > 0) & (xi_arr > 0) & np.isfinite(ratio_arr)
    if mask.sum() < 3:
        return None
    x = np.log(xi_arr[mask])
    y = np.log(ratio_arr[mask])
    A = np.vstack([x, np.ones(len(x))]).T
    coef, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
    slope, intercept = float(coef[0]), float(coef[1])
    pred = slope * x + intercept
    ss_res = np.sum((y - pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return {
        'slope': slope,
        'intercept_log_C': intercept,
        'C': float(np.exp(intercept)),
        'R2': r2,
        'n_points': int(mask.sum()),
    }


def linear_fit(xi_arr, ratio_arr):
    mask = (ratio_arr > 0) & (xi_arr > 0) & np.isfinite(ratio_arr)
    if mask.sum() < 3:
        return None
    A = np.vstack([xi_arr[mask], np.ones(mask.sum())]).T
    coef, _, _, _ = np.linalg.lstsq(A, ratio_arr[mask], rcond=None)
    C, b = float(coef[0]), float(coef[1])
    pred = C * xi_arr[mask] + b
    ss_res = np.sum((ratio_arr[mask] - pred) ** 2)
    ss_tot = np.sum((ratio_arr[mask] - np.mean(ratio_arr[mask])) ** 2)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return {
        'C': C, 'intercept_b': b, 'R2': r2,
        'n_points': int(mask.sum()),
    }


def main():
    parser = argparse.ArgumentParser(description='Cor 2.2 analytical ansatz validation')
    parser.add_argument('--grid-sizes', type=str, default='32,64,96')
    parser.add_argument('--xi-values', type=str,
                        default='0.25,0.5,0.75,1.0,1.5,2.0,2.5,3.0,4.0,6.0,8.0',
                        help='ξ_0 in LATTICE UNITS')
    parser.add_argument('--profiles', type=str, default='tanh,linear')
    parser.add_argument('--c', type=float, default=0.3)
    parser.add_argument('--output', default='experiments/results/exp_interface_ansatz.json')
    args = parser.parse_args()

    grid_sizes = [int(g) for g in args.grid_sizes.split(',')]
    xi_values = [float(x) for x in args.xi_values.split(',')]
    profiles = args.profiles.split(',')

    print("=" * 78)
    print("Round 13 Corollary 2.2 analytical ansatz validation")
    print(f"Bypasses find_formation: direct u construction with controlled ξ_0")
    print(f"Grid sizes: {grid_sizes}")
    print(f"ξ_0 values (lattice units): {xi_values}")
    print(f"Profiles: {profiles}")
    print(f"Volume fraction c: {args.c}")
    print("=" * 78)

    results = []
    t_total = time.time()

    for grid_size in grid_sizes:
        for profile in profiles:
            print(f"\n--- Grid {grid_size}x{grid_size}, profile={profile} ---")
            for xi_0 in xi_values:
                try:
                    r = run_one(grid_size, xi_0, args.c, profile)
                    results.append(r)
                    print(f"  ξ_0={xi_0:>4.2f}: r_0={r['r_0']:>5.2f}, "
                          f"|B|={r['interface_size']:>4d}, "
                          f"Per_e={r['per_edge']:>4d}, site_bd={r['site_bd']:>4d}, "
                          f"ratio_E={r['ratio_edge']:>6.3f}, "
                          f"ratio_S={r['ratio_site']:>6.3f}")
                except Exception as e:
                    print(f"  ξ_0={xi_0}: ERROR {e}")

    # Fits per (grid_size, profile)
    fits = {}
    for grid_size in grid_sizes:
        for profile in profiles:
            subset = [r for r in results if r['grid_size'] == grid_size
                      and r['profile'] == profile]
            if len(subset) < 3:
                continue

            xi_arr = np.array([r['xi_0'] for r in subset])
            ratio_edge_arr = np.array([r['ratio_edge'] for r in subset])
            ratio_site_arr = np.array([r['ratio_site'] for r in subset])

            key = f'{grid_size}_{profile}'
            fits[key] = {
                'edge_linear': linear_fit(xi_arr, ratio_edge_arr),
                'edge_loglog': loglog_fit(xi_arr, ratio_edge_arr),
                'site_linear': linear_fit(xi_arr, ratio_site_arr),
                'site_loglog': loglog_fit(xi_arr, ratio_site_arr),
            }

    # Print fits
    print(f"\n{'=' * 78}")
    print("FITS — ratio = C · ξ_0 + b  AND  log(ratio) = slope · log(ξ_0) + const")
    print(f"{'=' * 78}")
    for key, f in fits.items():
        print(f"\n[{key}]")
        for metric in ['edge', 'site']:
            lf = f[f'{metric}_linear']
            llf = f[f'{metric}_loglog']
            if lf is None or llf is None:
                continue
            print(f"  {metric}_perimeter:")
            print(f"    Linear:  ratio = {lf['C']:>6.3f}·ξ_0 + {lf['intercept_b']:>6.3f}  "
                  f"(R²={lf['R2']:.3f})")
            print(f"    Log-log: slope = {llf['slope']:>5.3f}  "
                  f"(expect 1.0, R²={llf['R2']:.3f})")
            slope_ok = 0.7 < llf['slope'] < 1.3
            b_small = abs(lf['intercept_b']) < 2.0
            print(f"    Cor 2.2 consistency: slope_OK={slope_ok}, b_near_zero={b_small}")

    # Save
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump({
            'experiment': 'exp_interface_ansatz',
            'round_ref': 'Round 13 Cor 2.2 direct mathematical validation',
            'params': vars(args),
            'results': results,
            'fits': fits,
            'total_time_sec': round(time.time() - t_total, 2),
        }, f, indent=2, default=str)
    print(f"\nResults saved: {args.output}")
    print(f"Total time: {time.time() - t_total:.1f}s")


if __name__ == '__main__':
    main()
