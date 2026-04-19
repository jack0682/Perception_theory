#!/usr/bin/env python3
"""Experiment 34: Near-bifurcation directional basin persistence.

Tests whether ellipsoidal basin (larger transverse to soft mode) extends
Tier 1 persistence into the near-bifurcation regime where isotropic basin
containment fails.

Key idea: NB-1 says r_basin = sqrt(2*Delta_bdy/lambda_max) -> 0 as mu -> 0,
but the directional basin is 1.5-3.3x larger transverse to the soft mode.
If temporal perturbation is mostly transverse, persistence may survive.
"""
import sys, os, json, time
import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.energy import EnergyComputer


def hessian_vec_product(ec, u, v, eps=1e-5):
    """Hessian-vector product via central finite differences."""
    gp = ec.gradient(u + eps * v)
    gm = ec.gradient(u - eps * v)
    return (gp - gm) / (2 * eps)


def projected_hessian_eigdecomp(ec, u, k=8):
    """Compute eigenvalues of Hessian projected to T(Sigma_m).

    Uses dense decomposition for reliability at small/medium grid sizes.
    Returns all eigenvalues > 1e-6 (excluding the zero mode from volume constraint).
    """
    n = len(u)
    P = np.eye(n) - np.ones((n, n)) / n  # projector to T(Sigma_m)

    # Build dense projected Hessian
    H_dense = np.zeros((n, n))
    for i in range(n):
        ei = np.zeros(n)
        ei[i] = 1.0
        ei_proj = P @ ei
        Hv = hessian_vec_product(ec, u, ei_proj)
        H_dense[:, i] = P @ Hv
    H_dense = 0.5 * (H_dense + H_dense.T)

    evals, evecs = np.linalg.eigh(H_dense)

    # Filter: keep eigenvalues above threshold (skip null space of projection)
    pos_mask = evals > 1e-6
    evals_pos = evals[pos_mask]
    evecs_pos = evecs[:, pos_mask]

    # Also return smallest (possibly negative) for diagnostics
    all_evals = evals[np.abs(evals) > 1e-8]

    k_ret = min(k, len(evals_pos))
    return evals_pos[:k_ret], evecs_pos[:, :k_ret], all_evals


def energy_barrier_along(ec, u, direction, m, n_steps=100, t_max=None):
    """Walk along direction from u*, find energy barrier."""
    n = len(u)
    if t_max is None:
        t_max = 0.3 * np.sqrt(n)

    E_base = ec.energy(u)[0]
    ts = np.linspace(0, t_max, n_steps)
    energies = []

    for t in ts:
        u_t = project_volume(u + t * direction, m)
        E_t = ec.energy(u_t)[0]
        energies.append(E_t)

    energies = np.array(energies)
    delta = float(np.max(energies) - E_base)
    return max(delta, 0.0)


def run_config(grid_size, beta, noise_scales, n_eigvecs=8, n_perturb=10):
    """Run one configuration: find formation, analyze basin, test persistence."""
    N = grid_size
    n = N * N

    params = ParameterRegistry(
        beta_bd=beta,
        volume_fraction=0.3,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        max_iter=5000, n_restarts=3,
        dt_init=0.01, eps_init=0.01,
    )
    graph = GraphState.grid_2d(N, N)
    ec = EnergyComputer(graph, params)

    # 1. Find formation
    result = find_formation(graph, params)
    if not result.converged:
        return None
    u_star = result.u
    m = params.volume_fraction * n

    # 2. Hessian eigendecomposition on T(Sigma_m)
    evals_pos, evecs_pos, all_evals = projected_hessian_eigdecomp(ec, u_star, k=n_eigvecs)

    if len(evals_pos) < 2:
        return None

    mu = float(evals_pos[0])       # spectral gap (smallest positive eigenvalue)
    mu2 = float(evals_pos[1])      # second smallest
    lambda_max = float(evals_pos[-1])
    v1 = evecs_pos[:, 0]           # soft mode

    # 3. Energy barrier along soft mode
    delta_bdy = energy_barrier_along(ec, u_star, v1, m)

    # 4. Basin radii
    r_iso = np.sqrt(2 * delta_bdy / lambda_max) if lambda_max > 1e-10 else float('inf')
    r_soft = np.sqrt(2 * delta_bdy / mu)
    r_trans = np.sqrt(2 * delta_bdy / mu2)
    anisotropy = r_trans / r_iso if r_iso > 1e-10 else float('inf')

    # 5. Test persistence at multiple noise scales
    noise_results = []
    rng = np.random.RandomState(42)

    for noise_scale in noise_scales:
        iso_ok_count = 0
        dir_ok_count = 0
        soft_comps = []
        trans_comps = []
        total_disps = []

        for trial in range(n_perturb):
            noise = rng.randn(n) * noise_scale
            noise -= np.mean(noise)
            u_pert = project_volume(u_star + noise, m)

            # Re-optimize from perturbed state
            result_pert = find_formation(graph, params, u_init=u_pert)
            u_new = result_pert.u

            disp = u_new - u_star
            disp -= np.mean(disp)
            disp_norm = float(np.linalg.norm(disp))

            soft_component = abs(float(disp @ v1))
            trans_component = np.sqrt(max(disp_norm**2 - soft_component**2, 0.0))

            soft_comps.append(soft_component)
            trans_comps.append(trans_component)
            total_disps.append(disp_norm)

            iso_ok = disp_norm < r_iso
            dir_ok = (soft_component < r_soft) and (trans_component < r_trans)

            if iso_ok:
                iso_ok_count += 1
            if dir_ok:
                dir_ok_count += 1

        noise_results.append({
            'noise_scale': noise_scale,
            'iso_ok_frac': iso_ok_count / n_perturb,
            'dir_ok_frac': dir_ok_count / n_perturb,
            'mean_disp_total': float(np.mean(total_disps)),
            'mean_disp_soft': float(np.mean(soft_comps)),
            'mean_disp_trans': float(np.mean(trans_comps)),
            'gained': dir_ok_count > iso_ok_count,
        })

    return {
        'grid': N,
        'beta': beta,
        'mu': mu,
        'mu2': mu2,
        'lambda_max': lambda_max,
        'delta_bdy': delta_bdy,
        'r_iso': r_iso,
        'r_soft': r_soft,
        'r_trans': r_trans,
        'anisotropy': anisotropy,
        'noise_results': noise_results,
        'energy': result.energy,
        'n_negative_evals': int(np.sum(all_evals < -1e-6)),
    }


def main():
    configs = [
        (10, 10), (10, 15), (10, 20), (10, 30), (10, 50),
        (12, 15), (12, 20), (12, 30), (12, 50),
        (15, 10), (15, 15), (15, 20), (15, 30),
    ]
    noise_scales = [0.05, 0.15, 0.30]

    results = []
    t0 = time.time()

    print("=" * 130)
    print(f"{'Grid':>5} {'β':>4} {'μ':>8} {'μ2':>8} {'λ_max':>8} {'Δ_bdy':>8} "
          f"{'r_iso':>7} {'r_soft':>7} {'r_trans':>7} {'aniso':>6} "
          f"{'ε=.05':>12} {'ε=.15':>12} {'ε=.30':>12}")
    hdr2 = " " * 73 + "iso%/dir%    iso%/dir%    iso%/dir%"
    print(hdr2)
    print("-" * 130)

    for grid_size, beta in configs:
        t1 = time.time()
        print(f"  Running {grid_size}x{grid_size} β={beta}...", end='', flush=True)

        try:
            r = run_config(grid_size, beta, noise_scales, n_eigvecs=8, n_perturb=10)
        except Exception as e:
            print(f" ERROR: {e}")
            continue

        elapsed = time.time() - t1
        if r is None:
            print(f" did not converge ({elapsed:.1f}s)")
            continue

        nr = r['noise_results']
        noise_strs = []
        for ns in nr:
            g = '*' if ns['gained'] else ' '
            noise_strs.append(f"{ns['iso_ok_frac']:.0%}/{ns['dir_ok_frac']:.0%}{g}")

        print(f"\r{r['grid']:>5} {r['beta']:>4} {r['mu']:>8.3f} {r['mu2']:>8.3f} "
              f"{r['lambda_max']:>8.2f} {r['delta_bdy']:>8.4f} "
              f"{r['r_iso']:>7.4f} {r['r_soft']:>7.4f} {r['r_trans']:>7.4f} "
              f"{r['anisotropy']:>6.2f} "
              f"{'  '.join(noise_strs):>36}  ({elapsed:.1f}s)")
        results.append(r)

    total = time.time() - t0
    print("=" * 130)
    print(f"Total time: {total:.1f}s")

    # Summary analysis
    print("\n--- SUMMARY ---")
    for ns_idx, ns_val in enumerate(noise_scales):
        gained = sum(1 for r in results if r['noise_results'][ns_idx]['gained'])
        iso_fail = sum(1 for r in results if r['noise_results'][ns_idx]['iso_ok_frac'] < 1.0)
        dir_fail = sum(1 for r in results if r['noise_results'][ns_idx]['dir_ok_frac'] < 1.0)
        print(f"ε={ns_val}: {gained}/{len(results)} gained directional | "
              f"iso failures: {iso_fail}/{len(results)} | dir failures: {dir_fail}/{len(results)}")

    # Basin anisotropy statistics
    aniso = [r['anisotropy'] for r in results]
    print(f"\nBasin anisotropy (r_trans/r_iso): "
          f"mean={np.mean(aniso):.2f}, min={np.min(aniso):.2f}, max={np.max(aniso):.2f}")

    # Soft-mode fraction of displacement
    print("\nSoft-mode fraction of displacement (f₁ = d_soft/d_total):")
    for ns_idx, ns_val in enumerate(noise_scales):
        fracs = []
        for r in results:
            nr = r['noise_results'][ns_idx]
            d_total = nr['mean_disp_total']
            if d_total > 1e-12:
                fracs.append(nr['mean_disp_soft'] / d_total)
        if fracs:
            print(f"  ε={ns_val}: mean f₁={np.mean(fracs):.3f}, max f₁={np.max(fracs):.3f}")

    # Key finding
    print("\n--- KEY FINDING ---")
    any_gain = any(
        r['noise_results'][ns_idx]['gained']
        for r in results
        for ns_idx in range(len(noise_scales))
    )
    if any_gain:
        print("YES: Directional basin analysis extends persistence in some configs.")
        for r in results:
            for ns_idx, ns_val in enumerate(noise_scales):
                nr = r['noise_results'][ns_idx]
                if nr['gained']:
                    print(f"  {r['grid']}x{r['grid']} β={r['beta']} ε={ns_val}: "
                          f"iso={nr['iso_ok_frac']:.0%} -> dir={nr['dir_ok_frac']:.0%} "
                          f"(anisotropy={r['anisotropy']:.2f})")
    else:
        print("NO directional gain observed. Possible explanations:")
        print("  1. Optimizer re-converges to same basin (displacement << basin radius)")
        print("  2. Basin anisotropy doesn't help because perturbations are isotropic")
        print("  3. Near-bifurcation regime not reached (all configs well above critical)")

    # Save results
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'exp34_nearbif_directional.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    # Convert for JSON serialization
    results_json = []
    for r in results:
        rj = {k: v for k, v in r.items()}
        results_json.append(rj)
    with open(out_path, 'w') as f:
        json.dump(results_json, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == '__main__':
    main()
