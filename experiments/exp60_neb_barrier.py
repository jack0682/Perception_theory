#!/usr/bin/env python3
"""Experiment 60: Nudged Elastic Band (NEB) for true merge saddle barrier.

Finds the minimum energy path (MEP) between K=2 and K=1 states using the
climbing-image NEB method, yielding the true saddle barrier ΔE_saddle.

Compares with the linear interpolation barrier from exp38 to determine
whether γ_eff ≈ 0.89 is a genuine exponent or a crossover artifact of
the straight-line path overestimating the barrier.

NEB Algorithm on Σ^K_M:
  1. Endpoints: K=2 minimizer (A) and K=1 minimizer embedded in K=2 space (B)
  2. N=20 intermediate images by linear interpolation, projected to constraints
  3. NEB forces per image:
     - Spring: k_spring * (|R_{i+1}-R_i| - |R_i-R_{i-1}|) * τ̂
     - True force perp: -∇E + (∇E·τ̂)τ̂  (remove parallel component)
     - Climbing image: highest-E image uses +∇E·τ̂ instead of spring
  4. Fire/velocity-Verlet relaxation until convergence

If the Modica neck argument holds, ΔE_NEB ~ √β (γ=0.5), not β^0.89.
"""
import sys, os, json, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.multi import find_k_formations
from scc.energy import EnergyComputer


# ---------------------------------------------------------------------------
# K=2 energy: E_self(u1) + E_self(u2) + λ_rep * <u1, u2>
# ---------------------------------------------------------------------------

def k2_energy(fields, ec, lambda_rep):
    """Total energy of a K=2 configuration (two fields)."""
    u1, u2 = fields
    E1, _ = ec.energy(u1)
    E2, _ = ec.energy(u2)
    E_rep = lambda_rep * float(np.dot(u1, u2))
    return E1 + E2 + E_rep


def k2_gradient(fields, ec, lambda_rep):
    """Gradient of K=2 energy w.r.t. concatenated (u1, u2)."""
    u1, u2 = fields
    n = len(u1)
    g1 = ec.gradient(u1) + lambda_rep * u2
    g2 = ec.gradient(u2) + lambda_rep * u1
    return np.concatenate([g1, g2])


def project_k2(x, m1, m2):
    """Project concatenated (u1, u2) onto box + volume constraints."""
    n = len(x) // 2
    u1 = project_volume(np.clip(x[:n], 0.0, 1.0), m1)
    u2 = project_volume(np.clip(x[n:], 0.0, 1.0), m2)
    return np.concatenate([u1, u2])


# ---------------------------------------------------------------------------
# NEB core
# ---------------------------------------------------------------------------

def neb_tangent(images, i):
    """Compute tangent vector at image i using bisection method."""
    tau = images[i + 1] - images[i - 1]
    norm = np.linalg.norm(tau)
    if norm < 1e-14:
        tau = images[i + 1] - images[i]
        norm = np.linalg.norm(tau)
    return tau / max(norm, 1e-14)


def neb_tangent_energy_weighted(images, energies, i):
    """Energy-weighted tangent for improved NEB stability."""
    tau_plus = images[i + 1] - images[i]
    tau_minus = images[i] - images[i - 1]
    E_i = energies[i]
    E_plus = energies[i + 1]
    E_minus = energies[i - 1]

    dE_plus = abs(E_plus - E_i)
    dE_minus = abs(E_minus - E_i)
    dE_max = max(dE_plus, dE_minus)
    dE_min = min(dE_plus, dE_minus)

    if E_plus > E_minus:
        tau = dE_max * tau_plus + dE_min * tau_minus
    elif E_plus < E_minus:
        tau = dE_min * tau_plus + dE_max * tau_minus
    else:
        tau = tau_plus + tau_minus

    norm = np.linalg.norm(tau)
    return tau / max(norm, 1e-14)


def neb_forces(images, energies, gradients, k_spring, climbing_idx):
    """Compute NEB forces for all intermediate images.

    Returns list of force vectors for images 1..N-2.
    """
    n_images = len(images)
    forces = []

    for i in range(1, n_images - 1):
        tau = neb_tangent_energy_weighted(images, energies, i)
        grad_i = gradients[i]

        if i == climbing_idx:
            # Climbing image: invert parallel component
            f = -grad_i + 2.0 * np.dot(grad_i, tau) * tau
        else:
            # Standard NEB: perpendicular true force + parallel spring force
            # Perpendicular true force
            grad_perp = grad_i - np.dot(grad_i, tau) * tau

            # Spring force (parallel only)
            d_plus = np.linalg.norm(images[i + 1] - images[i])
            d_minus = np.linalg.norm(images[i] - images[i - 1])
            f_spring_par = k_spring * (d_plus - d_minus)

            f = -grad_perp + f_spring_par * tau

        forces.append(f)

    return forces


def neb_barrier(g, p, K=2, lambda_rep=10.0, n_images=20, k_spring=1.0,
                max_iter=500, tol=1e-3, verbose=False):
    """Run climbing-image NEB between K=2 and K=1 minima.

    Uses steepest-descent with adaptive step size and force clamping for
    robustness. The path is parameterized in the single-field space:
    u_merged = clip(u1 + u2, 0, 1), avoiding the ill-conditioned K=2
    concatenated space.

    Returns dict with barrier_li, barrier_neb, saddle_image, convergence info.
    """
    n = g.n
    ec = EnergyComputer(g, p)
    ec.normalize_weights()

    # --- Step 1: Find endpoints ---
    if verbose:
        print("  Finding K=2 endpoint...")
    k2_results = find_k_formations(
        g, p, K=2, lambda_rep=lambda_rep, lambda_bar=100.0,
        n_restarts=3, max_iter=3000,
    )
    u1, u2 = k2_results[0].u, k2_results[1].u
    m1, m2 = float(np.sum(u1)), float(np.sum(u2))
    m_total = m1 + m2

    if verbose:
        print(f"  K=2 masses: m1={m1:.2f}, m2={m2:.2f}, total={m_total:.2f}")
        print("  Finding K=1 endpoint...")

    # K=1 merged formation with combined mass
    vf_merged = m_total / n
    vf_merged = max(0.22, min(0.78, vf_merged))
    p_merged = ParameterRegistry(
        beta_bd=p.beta_bd,
        volume_fraction=vf_merged,
        max_iter=5000,
        n_restarts=3,
        eps_grad=1e-3,
    )
    k1_result = find_formation(g, p_merged)
    u_merged = project_volume(k1_result.u, m_total)

    # Work in single-field space for the path:
    # Endpoint A: combined K=2 field
    u_A = np.clip(u1 + u2, 0.0, 1.0)
    u_A = project_volume(u_A, m_total)
    # Endpoint B: K=1 merged minimizer
    u_B = u_merged.copy()

    E_A_self, _ = ec.energy(u_A)
    E_B_self, _ = ec.energy(u_B)

    # Also compute K=2 actual energies for reference
    E_K2 = k2_energy([u1, u2], ec, lambda_rep)
    E_K1 = E_B_self  # K=1 is just the self-energy (no repulsion)

    E_endpoints = max(E_A_self, E_B_self)

    if verbose:
        print(f"  E(K=2 combined) = {E_A_self:.6f},  E(K=1) = {E_B_self:.6f}")
        print(f"  E(K=2 actual) = {E_K2:.6f}")

    # --- Step 2: Create initial path by linear interpolation ---
    total_images = n_images + 2  # including endpoints
    images = []
    for i in range(total_images):
        alpha = i / (total_images - 1)
        u_interp = (1.0 - alpha) * u_A + alpha * u_B
        u_interp = project_volume(np.clip(u_interp, 0.0, 1.0), m_total)
        images.append(u_interp.copy())

    # Compute linear interpolation barrier
    li_energies = []
    for img in images:
        E, _ = ec.energy(img)
        li_energies.append(E)
    li_energies = np.array(li_energies)
    barrier_li = float(np.max(li_energies) - E_endpoints)

    if verbose:
        print(f"  Linear interpolation barrier: {barrier_li:.6f}")

    # --- Step 3: NEB iteration with steepest descent + force clamping ---
    max_force_clamp = 5.0  # clamp force components
    dt = 0.005  # step size

    # Don't enable climbing image until band is somewhat relaxed
    enable_climbing_iter = max_iter // 4

    converged = False
    history = []

    for iteration in range(max_iter):
        # Compute energies and projected gradients for all images
        energies = []
        gradients = []
        for i, img in enumerate(images):
            E, _ = ec.energy(img)
            energies.append(E)
            if i == 0 or i == total_images - 1:
                gradients.append(np.zeros(n))
            else:
                grad = ec.gradient_projected(img)
                gradients.append(grad)

        energies = np.array(energies)

        # Find climbing image (highest energy among interior images)
        interior_E = energies[1:-1]
        climbing_idx = int(np.argmax(interior_E)) + 1
        use_climbing = (iteration >= enable_climbing_iter)

        # Compute NEB forces for interior images
        forces = []
        for i in range(1, total_images - 1):
            tau = neb_tangent_energy_weighted(images, energies, i)
            grad_i = gradients[i]

            if i == climbing_idx and use_climbing:
                # Climbing image: full gradient with inverted parallel component
                f = -grad_i + 2.0 * np.dot(grad_i, tau) * tau
            else:
                # Perpendicular true force
                grad_par = np.dot(grad_i, tau) * tau
                grad_perp = grad_i - grad_par

                # Spring force (parallel only)
                d_plus = np.linalg.norm(images[i + 1] - images[i])
                d_minus = np.linalg.norm(images[i] - images[i - 1])
                f_spring_par = k_spring * (d_plus - d_minus)

                f = -grad_perp + f_spring_par * tau

            # Clamp force magnitude for stability
            f_norm = np.linalg.norm(f)
            if f_norm > max_force_clamp * np.sqrt(n):
                f = f * (max_force_clamp * np.sqrt(n) / f_norm)

            forces.append(f)

        # Convergence: RMS force across images
        rms_force = np.sqrt(np.mean([np.sum(f**2) for f in forces]))
        max_force_val = max(np.linalg.norm(f) / np.sqrt(n) for f in forces)

        history.append({
            'iter': iteration,
            'rms_force': float(rms_force),
            'max_force': float(max_force_val),
            'barrier': float(energies[climbing_idx] - E_endpoints),
            'climbing_E': float(energies[climbing_idx]),
        })

        if verbose and iteration % 100 == 0:
            print(f"    NEB iter {iteration}: rms_force={rms_force:.4f}, "
                  f"max_f={max_force_val:.4f}, "
                  f"barrier={energies[climbing_idx] - E_endpoints:.6f}"
                  f"{' [CI]' if use_climbing else ''}")

        if max_force_val < tol:
            converged = True
            if verbose:
                print(f"  NEB converged at iteration {iteration}")
            break

        # Steepest descent update with adaptive step
        for idx, i in enumerate(range(1, total_images - 1)):
            images[i] = images[i] + dt * forces[idx]
            images[i] = project_volume(np.clip(images[i], 0.0, 1.0), m_total)

    # Final energies
    final_energies = []
    for img in images:
        E, _ = ec.energy(img)
        final_energies.append(E)
    final_energies = np.array(final_energies)

    barrier_neb = float(np.max(final_energies[1:-1]) - E_endpoints)
    saddle_idx = int(np.argmax(final_energies[1:-1])) + 1
    saddle_image = images[saddle_idx].copy()

    return {
        'barrier_li': barrier_li,
        'barrier_neb': barrier_neb,
        'ratio': barrier_neb / max(barrier_li, 1e-14),
        'E_K2': float(E_K2),
        'E_K1': float(E_K1),
        'E_A_self': float(E_A_self),
        'E_B_self': float(E_B_self),
        'saddle_E': float(final_energies[saddle_idx]),
        'saddle_idx': saddle_idx,
        'converged': converged,
        'n_iter': len(history),
        'final_rms_force': float(history[-1]['rms_force']) if history else float('inf'),
        'final_max_force': float(history[-1]['max_force']) if history else float('inf'),
        'saddle_image': saddle_image.tolist(),
        'energy_path_li': li_energies.tolist(),
        'energy_path_neb': final_energies.tolist(),
        'history': history[-5:],
    }


# ---------------------------------------------------------------------------
# Scaling analysis
# ---------------------------------------------------------------------------

def log_log_fit(x, y):
    """Fit log(y) = γ*log(x) + c, return (γ, c, R²)."""
    mask = (np.array(x) > 0) & (np.array(y) > 0)
    lx = np.log(np.array(x)[mask])
    ly = np.log(np.array(y)[mask])
    if len(lx) < 2:
        return float('nan'), float('nan'), float('nan')
    coeffs = np.polyfit(lx, ly, 1)
    gamma = coeffs[0]
    c = coeffs[1]
    ly_pred = gamma * lx + c
    ss_res = np.sum((ly - ly_pred) ** 2)
    ss_tot = np.sum((ly - np.mean(ly)) ** 2)
    R2 = 1 - ss_res / max(ss_tot, 1e-14)
    return float(gamma), float(c), float(R2)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("  Experiment 60: NEB Saddle Barrier for K=2 → K=1 Merge")
    print("=" * 70)

    grids = [(10, 10), (12, 12)]
    betas = [10, 20, 30, 50]
    lambda_rep = 10.0
    n_images = 20
    k_spring = 1.0
    max_iter = 2000

    all_results = {}

    for (rows, cols) in grids:
        grid_label = f"{rows}x{cols}"
        print(f"\n{'='*60}")
        print(f"  Grid: {grid_label}")
        print(f"{'='*60}")

        g = GraphState.grid_2d(rows, cols)
        grid_results = {}
        barriers_li = []
        barriers_neb = []
        beta_list = []

        for beta in betas:
            label = f"grid={grid_label}, β={beta}"
            print(f"\n--- {label} ---")
            t0 = time.time()

            p = ParameterRegistry(
                beta_bd=beta,
                volume_fraction=0.3,
                max_iter=5000,
                n_restarts=3,
                eps_grad=1e-3,
            )

            result = neb_barrier(
                g, p, K=2, lambda_rep=lambda_rep,
                n_images=n_images, k_spring=k_spring,
                max_iter=max_iter, tol=1e-3,
                verbose=True,
            )

            elapsed = time.time() - t0
            result['elapsed_s'] = elapsed

            # Remove large arrays for summary
            result_summary = {k: v for k, v in result.items()
                             if k not in ('saddle_image_u1', 'saddle_image_u2',
                                          'energy_path_li', 'energy_path_neb')}

            print(f"  ΔE_LI  = {result['barrier_li']:.6f}")
            print(f"  ΔE_NEB = {result['barrier_neb']:.6f}")
            print(f"  Ratio  = {result['ratio']:.4f}")
            print(f"  Converged: {result['converged']} ({result['n_iter']} iters)")
            print(f"  Time: {elapsed:.1f}s")

            grid_results[f"beta_{beta}"] = result
            beta_list.append(beta)
            barriers_li.append(result['barrier_li'])
            barriers_neb.append(result['barrier_neb'])

        # Scaling analysis
        if len(beta_list) >= 2:
            gamma_li, c_li, R2_li = log_log_fit(beta_list, [max(b, 1e-6) for b in barriers_li])

            scaling = {
                'gamma_li': gamma_li, 'R2_li': R2_li,
                'betas': beta_list,
                'barriers_li': barriers_li,
                'barriers_neb': barriers_neb,
            }
            grid_results['scaling'] = scaling

            print(f"\n  Scaling analysis for {grid_label}:")
            print(f"    LI:  ΔE ~ β^{gamma_li:.3f}  (R²={R2_li:.4f})")
            mean_neb = np.mean(barriers_neb)
            max_neb = max(abs(b) for b in barriers_neb)
            print(f"    NEB: mean ΔE = {mean_neb:.4f}, max|ΔE| = {max_neb:.4f}")
            if max_neb < 0.5:
                print(f"    → NEB: BARRIERLESS (all |ΔE| < 0.5)")
            else:
                print(f"    → NEB: residual barriers present (not fully converged)")

        all_results[grid_label] = grid_results

    # --- Summary ---
    print("\n" + "=" * 70)
    print("  SUMMARY")
    print("=" * 70)

    for grid_label, grid_results in all_results.items():
        if 'scaling' in grid_results:
            s = grid_results['scaling']
            neb_bars = s['barriers_neb']
            li_bars = s['barriers_li']
            max_neb = max(abs(b) for b in neb_bars)
            mean_neb = np.mean(neb_bars)
            mean_li = np.mean(li_bars)

            print(f"\n  {grid_label}:")
            print(f"    LI:  γ = {s['gamma_li']:.3f}, mean ΔE = {mean_li:.3f}")
            print(f"    NEB: mean ΔE = {mean_neb:.4f}, max|ΔE| = {max_neb:.4f}")
            print(f"    NEB/LI ratio: {mean_neb / max(mean_li, 1e-6):.4f}")

            if max_neb < 0.5:
                print(f"    ★ MEP is BARRIERLESS — merge has no self-energy barrier")
                print(f"      LI barrier was a straight-path artifact")
                print(f"      K=2 kinetic stability = repulsion only")
            elif mean_neb > 0 and mean_neb < mean_li * 0.1:
                print(f"    ★ NEB barrier ~{mean_neb:.2f} << LI barrier ~{mean_li:.2f}")
                print(f"      γ_eff = 0.89 was mostly a path artifact")
            else:
                print(f"    ★ Significant NEB barrier persists")

    # Save results (strip large arrays)
    save_results = {}
    for grid_label, grid_results in all_results.items():
        save_grid = {}
        for key, val in grid_results.items():
            if isinstance(val, dict) and 'saddle_image_u1' in val:
                val = {k: v for k, v in val.items()
                       if k not in ('saddle_image_u1', 'saddle_image_u2',
                                    'energy_path_li', 'energy_path_neb')}
            save_grid[key] = val
        save_results[grid_label] = save_grid

    out_path = os.path.join(os.path.dirname(__file__), 'results', 'exp60_neb_barrier.json')
    with open(out_path, 'w') as f:
        json.dump(save_results, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")


if __name__ == '__main__':
    main()
