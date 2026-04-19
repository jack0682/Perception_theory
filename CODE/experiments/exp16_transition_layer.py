#!/usr/bin/env python3
"""Experiment 16: Transition layer width verification.

For grids 10x10, 15x15, 20x20 and beta in {20, 50, 100, 200}:
- Find formation, identify Core = {x : u(x) >= 0.9}
- S* = top-m nodes (m = round(0.3 * n))
- Compute transition profile: mean u at each distance d from boundary of S*
- Verify S*^(2) subset Core, measure deep core fraction |Core^(2)|/|Core|
- Compute theoretical delta_eps and Hausdorff distance d_H(Core, S*)
"""
import sys, os, time
import numpy as np
from math import ceil, log, acosh

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scipy.sparse.csgraph import shortest_path


def boundary_of(node_set, dist_matrix, n):
    """Nodes in node_set that have a neighbor (dist=1) outside node_set."""
    complement = set(range(n)) - node_set
    boundary = set()
    for v in node_set:
        for w in complement:
            if dist_matrix[v, w] == 1:
                boundary.add(v)
                break
    return boundary


def erode(node_set, dist_matrix, n, depth):
    """Erode node_set by `depth` layers: remove nodes within `depth` of complement."""
    if depth <= 0:
        return node_set
    complement = set(range(n)) - node_set
    eroded = set()
    for v in node_set:
        min_dist_to_complement = min(dist_matrix[v, w] for w in complement) if complement else float('inf')
        if min_dist_to_complement > depth:
            eroded.add(v)
    return eroded


def hausdorff_distance(set_a, set_b, dist_matrix):
    """Compute Hausdorff distance between two node sets."""
    if not set_a or not set_b:
        return float('inf')
    a_list = list(set_a)
    b_list = list(set_b)
    # max over a of min over b
    sup_a = max(min(dist_matrix[a, b] for b in b_list) for a in a_list)
    sup_b = max(min(dist_matrix[a, b] for a in a_list) for b in b_list)
    return max(sup_a, sup_b)


def signed_distance_from_boundary(nodes, boundary_set, node_set, dist_matrix):
    """Compute signed distance of each node from boundary of S*.
    Positive = inside S*, negative = outside S*."""
    boundary_list = list(boundary_set)
    if not boundary_list:
        return {}
    result = {}
    for v in nodes:
        d_to_boundary = min(dist_matrix[v, b] for b in boundary_list)
        if v in node_set:
            result[v] = d_to_boundary  # inside: positive
        else:
            result[v] = -d_to_boundary  # outside: negative
    return result


def run_single(N, beta_val):
    """Run experiment for one grid size and beta value."""
    n = N * N
    g = GraphState.grid_2d(N, N)
    p = ParameterRegistry(beta_bd=beta_val, volume_fraction=0.3)
    r = find_formation(g, p)
    u = r.u

    # Compute all-pairs shortest paths
    dist = shortest_path(g.W, method='D', unweighted=True)

    # Core = {x : u(x) >= 0.9}
    core = set(np.where(u >= 0.9)[0])

    # S* = top-m nodes by u value
    m = round(0.3 * n)
    top_indices = np.argsort(u)[-m:]
    s_star = set(top_indices)

    # Boundary of S*
    bdry = boundary_of(s_star, dist, n)

    # S*^(2) = S* eroded by 2
    s_star_eroded_2 = erode(s_star, dist, n, 2)

    # Core^(2) = Core eroded by 2
    core_eroded_2 = erode(core, dist, n, 2)

    # Check S*^(2) ⊆ Core
    s2_subset_core = s_star_eroded_2.issubset(core)

    # Deep core fraction
    deep_core_frac = len(core_eroded_2) / len(core) if len(core) > 0 else 0.0

    # Hausdorff distance d_H(Core, S*)
    d_H = hausdorff_distance(core, s_star, dist)

    # Theoretical delta_eps
    # delta_eps = ceil(log(2/eps) / arccosh(1 + beta/(2*deg_max)))
    # For 2D grid, max degree = 4
    deg_max = 4
    arg = 1 + beta_val / (2 * deg_max)
    delta_eps = ceil(log(2.0 / 0.1) / acosh(arg))

    # Transition profile: mean u at each signed distance from ∂S*
    signed_dists = signed_distance_from_boundary(range(n), bdry, s_star, dist)
    d_min_val = int(min(signed_dists.values())) if signed_dists else -3
    d_max_val = int(max(signed_dists.values())) if signed_dists else 5

    profile = {}
    for d in range(max(d_min_val, -3), min(d_max_val, 5) + 1):
        nodes_at_d = [v for v, sd in signed_dists.items() if int(round(sd)) == d]
        if nodes_at_d:
            profile[d] = float(np.mean(u[nodes_at_d]))

    return {
        'N': N, 'beta': beta_val, 'n': n, 'm': m,
        'core_size': len(core), 's_star_size': len(s_star),
        's2_size': len(s_star_eroded_2),
        'core2_size': len(core_eroded_2),
        's2_subset_core': s2_subset_core,
        'deep_core_frac': deep_core_frac,
        'd_H': d_H,
        'delta_eps_theory': delta_eps,
        'profile': profile,
        'energy': r.energy,
        'converged': r.converged,
        'u_min': float(u.min()), 'u_max': float(u.max()),
    }


def main():
    grids = [10, 15, 20]
    betas = [20, 50, 100, 200]

    print("=" * 72)
    print("  Exp16: Transition Layer Width Verification")
    print("=" * 72)

    all_results = []
    t0 = time.time()

    for N in grids:
        for beta_val in betas:
            print(f"\n--- Grid {N}x{N}, beta={beta_val} ---")
            t1 = time.time()
            res = run_single(N, beta_val)
            dt = time.time() - t1
            all_results.append(res)

            print(f"  Converged: {res['converged']}, E={res['energy']:.4f}")
            print(f"  u range: [{res['u_min']:.4f}, {res['u_max']:.4f}]")
            print(f"  |Core|={res['core_size']}, |S*|={res['s_star_size']}, "
                  f"|S*^(2)|={res['s2_size']}, |Core^(2)|={res['core2_size']}")
            print(f"  S*^(2) ⊆ Core: {res['s2_subset_core']}")
            print(f"  Deep core fraction |Core^(2)|/|Core|: {res['deep_core_frac']:.3f}")
            print(f"  d_H(Core, S*): {res['d_H']:.1f}")
            print(f"  Theoretical δ_ε: {res['delta_eps_theory']}")
            print(f"  Transition profile (dist → mean u):")
            for d in sorted(res['profile'].keys()):
                bar = '█' * int(res['profile'][d] * 40)
                print(f"    d={d:+2d}: {res['profile'][d]:.4f}  {bar}")
            print(f"  Time: {dt:.1f}s")

    total_time = time.time() - t0

    # Summary table
    print("\n" + "=" * 72)
    print("  SUMMARY TABLE")
    print("=" * 72)
    print(f"{'Grid':>6} {'β':>5} {'|Core|':>6} {'|S*|':>5} {'S²⊆C':>5} "
          f"{'DC frac':>7} {'d_H':>5} {'δ_th':>4}")
    print("-" * 52)
    for res in all_results:
        print(f"{res['N']:>3}x{res['N']:<3} {res['beta']:>5} {res['core_size']:>6} "
              f"{res['s_star_size']:>5} {str(res['s2_subset_core']):>5} "
              f"{res['deep_core_frac']:>7.3f} {res['d_H']:>5.1f} "
              f"{res['delta_eps_theory']:>4}")

    # Verification checks
    print("\n" + "=" * 72)
    print("  VERIFICATION")
    print("=" * 72)
    s2_all_pass = all(r['s2_subset_core'] for r in all_results)
    print(f"  S*^(2) ⊆ Core (all configs): {'PASS' if s2_all_pass else 'FAIL'}")

    dc_fracs = [r['deep_core_frac'] for r in all_results if r['beta'] >= 50]
    if dc_fracs:
        print(f"  Deep core fraction (β≥50) min={min(dc_fracs):.3f}, "
              f"mean={np.mean(dc_fracs):.3f}")

    dh_vals = [r['d_H'] for r in all_results]
    print(f"  d_H range: [{min(dh_vals):.1f}, {max(dh_vals):.1f}]")

    # Check that d_H <= delta_eps for each config
    dh_check = all(r['d_H'] <= r['delta_eps_theory'] + 1 for r in all_results)
    print(f"  d_H ≤ δ_ε + 1 (all configs): {'PASS' if dh_check else 'FAIL'}")

    print(f"\n  Total time: {total_time:.1f}s")


if __name__ == '__main__':
    main()
