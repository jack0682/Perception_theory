#!/usr/bin/env python3
"""Experiment 41: Tight formation-aware transport confinement bound.

The current bound C_conf = O(σ√(ε_OT log n)) is 25-10000× too loose because
it treats u_t as arbitrary. But u_t is a formation with sharp-interface
structure — transport mass concentrates within the core.

This experiment develops tighter bounds that exploit formation geometry:
  - B_naive: σ·√(ε_OT·log n)·√m  (current proof bound)
  - B1: boundary-proportional (∂Core/√n scaling)
  - B2: geometric mean of boundary and mass
  - B3: radius-fraction (R_F/diam scaling)
  - B4: fingerprint-gap exponential decay
  - B5: empirical tight bound (max observed displacement)

Tests across 6 grid configs × 4 target initializations = 24 transport runs.
"""
import sys, os, json, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.transport import (
    cohesion_fingerprint, graph_distance_matrix, transport_cost,
    sinkhorn_partial_ot, transport_field,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_params(beta=50.0, vol_frac=0.3):
    return ParameterRegistry(
        beta_bd=beta,
        volume_fraction=vol_frac,
        max_iter=5000,
        n_restarts=3,
        eps_grad=1e-3,
    )


def formation_geometry(u, graph, threshold=0.5):
    """Compute formation geometric properties.

    Returns dict with: core (mask), core_size, boundary_size, R_F, centroid.
    """
    n = graph.n
    core = u >= threshold
    core_size = int(np.sum(core))

    if core_size == 0:
        return {
            'core': core, 'core_size': 0, 'boundary_size': 0,
            'R_F': 0.0, 'centroid': None,
        }

    # Boundary: core nodes with at least one non-core neighbor
    W = graph.W.toarray() if hasattr(graph.W, 'toarray') else np.array(graph.W)
    boundary = np.zeros(n, dtype=bool)
    for i in range(n):
        if core[i]:
            neighbors = np.where(W[i] > 0)[0]
            if np.any(~core[neighbors]):
                boundary[i] = True
    boundary_size = int(np.sum(boundary))

    # Core centroid (mass-weighted by u values)
    core_indices = np.where(core)[0]
    core_weights = u[core_indices]

    # For grid graphs, convert index to 2D coordinates
    # Detect grid dimensions from graph size
    n_total = graph.n
    side = int(np.round(np.sqrt(n_total)))
    if side * side == n_total:
        rows = core_indices // side
        cols = core_indices % side
        w_sum = core_weights.sum()
        centroid_r = np.sum(rows * core_weights) / w_sum
        centroid_c = np.sum(cols * core_weights) / w_sum
        centroid_idx = int(np.round(centroid_r)) * side + int(np.round(centroid_c))
        centroid_idx = np.clip(centroid_idx, 0, n_total - 1)
    else:
        centroid_idx = core_indices[np.argmax(core_weights)]

    # R_F = max graph distance from centroid to any core node
    dist = graph_distance_matrix(graph)
    R_F = float(np.max(dist[centroid_idx, core_indices]))

    return {
        'core': core,
        'core_size': core_size,
        'boundary_size': boundary_size,
        'R_F': R_F,
        'centroid': centroid_idx,
        'dist_matrix': dist,
    }


def make_targets(u_t, graph, params, rng):
    """Create 4 different u_s targets for transport testing.

    Returns list of (name, u_s) tuples.
    """
    n = graph.n
    m = float(u_t.sum())
    targets = []

    # 1. Self-transport (u_s = u_t)
    targets.append(('self', u_t.copy()))

    # 2. Uniform field with same mass
    u_uniform = np.full(n, m / n)
    targets.append(('uniform', u_uniform))

    # 3. Random field projected to same mass
    u_rand = rng.random(n)
    u_rand = project_volume(u_rand, m)
    targets.append(('random', u_rand))

    # 4. Shifted formation: translate u_t by ~2 nodes
    side = int(np.round(np.sqrt(n)))
    if side * side == n:
        shift = 2
        u_shifted = np.zeros(n)
        for i in range(n):
            r, c = divmod(i, side)
            nr, nc = r, c + shift
            if 0 <= nr < side and 0 <= nc < side:
                u_shifted[nr * side + nc] = u_t[i]
            else:
                u_shifted[i] = u_t[i]  # wrap edge cases
        u_shifted = project_volume(u_shifted, m)
    else:
        # fallback: small perturbation
        u_shifted = u_t + 0.1 * rng.standard_normal(n)
        u_shifted = np.clip(u_shifted, 0, 1)
        u_shifted = project_volume(u_shifted, m)
    targets.append(('shifted', u_shifted))

    return targets


def compute_displacement(u_t, u_s, graph, params, sigma=1.0, gamma=1.0, eps_ot=1.0):
    """Compute transport displacement ‖ũ - u_t‖_2."""
    phi_t = cohesion_fingerprint(u_t, graph, params)
    phi_s = cohesion_fingerprint(u_s, graph, params)
    dist_matrix = graph_distance_matrix(graph)
    cost = transport_cost(phi_t, phi_s, dist_matrix, sigma=sigma, gamma=gamma)
    M, info = sinkhorn_partial_ot(cost, u_t, u_s, eps_ot)
    u_transported = transport_field(M, u_s)
    displacement = float(np.linalg.norm(u_transported - u_t))
    return displacement, M, info


def compute_fingerprint_gap(u_t, graph, params, core_mask):
    """Compute Δ_φ² = mean over core of min over exterior of ‖φ(core) - φ(ext)‖²."""
    phi = cohesion_fingerprint(u_t, graph, params)
    ext_mask = ~core_mask

    if not np.any(ext_mask) or not np.any(core_mask):
        return 0.0

    phi_core = phi[core_mask]   # (|Core|, d)
    phi_ext = phi[ext_mask]     # (|Ext|, d)

    # For each core site, find min distance to any exterior site
    # diff shape: (|Core|, |Ext|, d)
    diff = phi_core[:, np.newaxis, :] - phi_ext[np.newaxis, :, :]
    sq_dists = np.sum(diff ** 2, axis=2)  # (|Core|, |Ext|)
    min_dists = np.min(sq_dists, axis=1)  # (|Core|,)

    return float(np.mean(min_dists))


# ---------------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------------

def run_experiment():
    print("=" * 72)
    print("Experiment 41: Tight Formation-Aware Transport Confinement Bound")
    print("=" * 72)

    rng = np.random.default_rng(42)

    configs = [
        (10, 10, 30.0),
        (10, 10, 50.0),
        (15, 15, 30.0),
        (15, 15, 50.0),
        (15, 15, 100.0),
        (20, 20, 50.0),
    ]

    sigma = 1.0
    gamma = 1.0
    eps_ot = 1.0

    all_results = []

    for rows, cols, beta in configs:
        n = rows * cols
        label = f"{rows}x{cols}_beta{int(beta)}"
        print(f"\n--- Config: {rows}×{cols}, β={beta}, n={n} ---")

        graph = GraphState.grid_2d(rows, cols)
        params = make_params(beta=beta)

        # Find formation
        t0 = time.time()
        result = find_formation(graph, params)
        u_t = result.u
        m = float(u_t.sum())
        print(f"  Formation found: m={m:.2f}, E={result.energy:.4f}, "
              f"converged={result.converged} ({time.time()-t0:.1f}s)")

        # Formation geometry
        geo = formation_geometry(u_t, graph)
        core_size = geo['core_size']
        boundary_size = geo['boundary_size']
        R_F = geo['R_F']
        dist_matrix = geo.get('dist_matrix', graph_distance_matrix(graph))
        diam = float(np.max(dist_matrix[np.isfinite(dist_matrix)]))

        print(f"  Geometry: |Core|={core_size}, |∂Core|={boundary_size}, "
              f"R_F={R_F:.1f}, diam={diam:.0f}")

        # Fingerprint gap for B4
        delta_phi_sq = compute_fingerprint_gap(u_t, graph, params, geo['core'])
        print(f"  Fingerprint gap Δ_φ²={delta_phi_sq:.4f}")

        # Candidate bounds
        B_naive = sigma * np.sqrt(eps_ot * np.log(n)) * np.sqrt(m)
        B1 = sigma * np.sqrt(eps_ot) * boundary_size / np.sqrt(n) * np.sqrt(m) if n > 0 else 0
        B2 = sigma * np.sqrt(eps_ot) * np.sqrt(boundary_size * m / n) if n > 0 else 0
        B3 = sigma * np.sqrt(eps_ot) * (R_F / diam) * np.sqrt(m) if diam > 0 else 0
        B4 = sigma * np.sqrt(eps_ot) * np.sqrt(m) * np.exp(-delta_phi_sq / eps_ot) if eps_ot > 0 else 0

        print(f"  Bounds: B_naive={B_naive:.4f}, B1={B1:.4f}, B2={B2:.4f}, "
              f"B3={B3:.4f}, B4={B4:.4f}")

        # Test with 4 different targets
        targets = make_targets(u_t, graph, params, rng)
        max_disp = 0.0
        target_results = []

        for tname, u_s in targets:
            disp, M, info = compute_displacement(u_t, u_s, graph, params,
                                                  sigma=sigma, gamma=gamma,
                                                  eps_ot=eps_ot)
            max_disp = max(max_disp, disp)
            target_results.append({
                'target': tname,
                'displacement': disp,
                'ot_converged': info['converged'],
                'ot_iterations': info['iterations'],
            })
            print(f"    {tname:>8s}: disp={disp:.6f}")

        B5 = max_disp  # empirical tight bound

        # Tightness ratios
        bounds = {
            'B_naive': B_naive, 'B1': B1, 'B2': B2,
            'B3': B3, 'B4': B4, 'B5': B5,
        }
        tightness = {}
        validity = {}
        for bname, bval in bounds.items():
            if bval > 0:
                ratio = max_disp / bval
                tightness[bname] = ratio
                validity[bname] = (max_disp <= bval * 1.01)  # 1% tolerance
            else:
                tightness[bname] = float('inf')
                validity[bname] = False

        config_result = {
            'config': label,
            'n': n,
            'beta': beta,
            'm': m,
            'core_size': core_size,
            'boundary_size': boundary_size,
            'R_F': R_F,
            'diam': diam,
            'delta_phi_sq': delta_phi_sq,
            'max_displacement': max_disp,
            'bounds': {k: float(v) for k, v in bounds.items()},
            'tightness_ratios': {k: float(v) for k, v in tightness.items()},
            'validity': validity,
            'targets': target_results,
        }
        all_results.append(config_result)

        print(f"  Max displacement: {max_disp:.6f}")
        print(f"  Tightness (disp/bound): ", end='')
        for bname in ['B_naive', 'B1', 'B2', 'B3', 'B4']:
            print(f"{bname}={tightness.get(bname,0):.4f} ", end='')
        print()

    # ---------------------------------------------------------------------------
    # Summary analysis
    # ---------------------------------------------------------------------------
    print("\n" + "=" * 72)
    print("SUMMARY: Bound Comparison")
    print("=" * 72)

    header = f"{'Config':>16s} | {'n':>4s} | {'|Core|':>5s} | {'|∂C|':>4s} | {'R_F':>4s} | {'maxD':>8s} | {'B_naive':>8s} | {'B1':>8s} | {'B2':>8s} | {'B3':>8s} | {'B4':>8s}"
    print(header)
    print("-" * len(header))

    for r in all_results:
        print(f"{r['config']:>16s} | {r['n']:4d} | {r['core_size']:5d} | "
              f"{r['boundary_size']:4d} | {r['R_F']:4.1f} | "
              f"{r['max_displacement']:8.5f} | "
              f"{r['bounds']['B_naive']:8.4f} | "
              f"{r['bounds']['B1']:8.4f} | "
              f"{r['bounds']['B2']:8.4f} | "
              f"{r['bounds']['B3']:8.4f} | "
              f"{r['bounds']['B4']:8.4f}")

    print("\nBound Validity (max_disp ≤ bound across all configs):")
    bound_names = ['B_naive', 'B1', 'B2', 'B3', 'B4']
    for bname in bound_names:
        all_valid = all(r['validity'].get(bname, False) for r in all_results)
        max_ratio = max(r['tightness_ratios'].get(bname, 0) for r in all_results)
        mean_ratio = np.mean([r['tightness_ratios'].get(bname, 0) for r in all_results])
        status = "VALID" if all_valid else "INVALID (too tight)"
        print(f"  {bname:>8s}: {status:>20s} | max ratio={max_ratio:.4f} | mean ratio={mean_ratio:.4f}")

    # Identify best bound
    best = None
    best_max_ratio = float('inf')
    for bname in bound_names:
        all_valid = all(r['validity'].get(bname, False) for r in all_results)
        if all_valid:
            max_ratio = max(r['tightness_ratios'].get(bname, 0) for r in all_results)
            if max_ratio < best_max_ratio:
                best = bname
                best_max_ratio = max_ratio

    if best:
        print(f"\n  TIGHTEST VALID BOUND: {best} (max tightness ratio = {best_max_ratio:.4f})")
    else:
        print("\n  WARNING: No candidate bound is universally valid!")
        # Find which is closest
        for bname in bound_names:
            violations = sum(1 for r in all_results if not r['validity'].get(bname, False))
            max_ratio = max(r['tightness_ratios'].get(bname, 0) for r in all_results)
            print(f"    {bname}: {violations} violations, max ratio={max_ratio:.4f}")

    # Summary JSON
    summary = {
        'experiment': 'exp41_tight_confinement',
        'description': 'Tight formation-aware transport confinement bounds',
        'parameters': {
            'sigma': sigma, 'gamma': gamma, 'eps_ot': eps_ot,
            'core_threshold': 0.5,
        },
        'configs': all_results,
        'bound_summary': {},
    }
    for bname in bound_names:
        all_valid = all(r['validity'].get(bname, False) for r in all_results)
        max_ratio = max(r['tightness_ratios'].get(bname, 0) for r in all_results)
        mean_ratio = float(np.mean([r['tightness_ratios'].get(bname, 0) for r in all_results]))
        summary['bound_summary'][bname] = {
            'universally_valid': all_valid,
            'max_tightness_ratio': max_ratio,
            'mean_tightness_ratio': mean_ratio,
        }
    summary['best_bound'] = best
    summary['best_max_ratio'] = best_max_ratio if best else None

    # Save results
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'exp41_tight_confinement.json')
    with open(out_path, 'w') as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")

    return summary


if __name__ == '__main__':
    run_experiment()
