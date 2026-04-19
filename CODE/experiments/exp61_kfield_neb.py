#!/usr/bin/env python3
"""Experiment 61: K-field NEB — proper merge barrier in full ℝ^{2n} space.

exp60 was flawed: it ran NEB on single-field energy (u1+u2 combined),
completely missing the repulsion barrier λ_rep·⟨u1,u2⟩. This experiment
fixes that by running NEB in the concatenated K=2 state space:

  State = (u1, u2) ∈ ℝ^{2n}
  E_K(u1,u2) = E_self(u1) + E_self(u2) + λ_rep · Σ u1·u2

Endpoint A: optimized K=2 separated formations
Endpoint B: merged single formation + zero field = (u_merged, 0)

The NEB path traverses the full energy landscape including the repulsion
barrier that stabilizes K=2 configurations.

Also sweeps λ_rep ∈ {0, 1, 5, 10, 20} to measure how barrier scales.
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
# K=2 energy and gradient in concatenated space ℝ^{2n}
# ---------------------------------------------------------------------------

def k2_energy(x, n, ec, lambda_rep):
    """E_K(u1,u2) = E_self(u1) + E_self(u2) + λ_rep·⟨u1,u2⟩."""
    u1, u2 = x[:n], x[n:]
    E1, t1 = ec.energy(u1)
    E2, t2 = ec.energy(u2)
    E_rep = lambda_rep * float(np.dot(u1, u2))
    return E1 + E2 + E_rep, {'E_self1': E1, 'E_self2': E2, 'E_rep': E_rep}


def k2_gradient(x, n, ec, lambda_rep):
    """∇E_K in ℝ^{2n}: [∇E_self(u1) + λ_rep·u2, ∇E_self(u2) + λ_rep·u1]."""
    u1, u2 = x[:n], x[n:]
    g1 = ec.gradient(u1) + lambda_rep * u2
    g2 = ec.gradient(u2) + lambda_rep * u1
    return np.concatenate([g1, g2])


def project_k2(x, n, m1, m2):
    """Project concatenated (u1,u2) onto [0,1]^{2n} ∩ volume constraints."""
    u1 = project_volume(np.clip(x[:n], 0.0, 1.0), m1)
    u2 = project_volume(np.clip(x[n:], 0.0, 1.0), m2)
    return np.concatenate([u1, u2])


def project_k2_gradient(g, n):
    """Project gradient onto tangent space of volume constraints (per field)."""
    g1 = g[:n] - np.mean(g[:n])
    g2 = g[n:] - np.mean(g[n:])
    return np.concatenate([g1, g2])


# ---------------------------------------------------------------------------
# Energy-weighted NEB tangent
# ---------------------------------------------------------------------------

def neb_tangent(images, energies, i):
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


# ---------------------------------------------------------------------------
# K-field NEB
# ---------------------------------------------------------------------------

def kfield_neb(g, p, lambda_rep=10.0, n_images=20, k_spring=0.5,
               dt=0.001, max_iter=3000, tol=0.1, verbose=False):
    """Climbing-image NEB in full K=2 concatenated space ℝ^{2n}.

    Endpoint A: optimized K=2 separated formations (u1*, u2*)
    Endpoint B: merged formation + zero = (u_merged, 0)

    Returns dict with barrier, energy decomposition, convergence info.
    """
    n = g.n
    ec = EnergyComputer(g, p)
    ec.normalize_weights()

    # --- Endpoint A: K=2 minimizer ---
    if verbose:
        print("  Finding K=2 endpoint (separated formations)...")
    k2_results = find_k_formations(
        g, p, K=2, lambda_rep=lambda_rep, lambda_bar=100.0,
        n_restarts=3, max_iter=3000,
    )
    u1, u2 = k2_results[0].u, k2_results[1].u
    m1 = float(np.sum(u1))
    m2 = float(np.sum(u2))
    m_total = m1 + m2

    x_A = np.concatenate([u1, u2])
    E_A, terms_A = k2_energy(x_A, n, ec, lambda_rep)

    if verbose:
        print(f"  K=2: m1={m1:.2f}, m2={m2:.2f}, E={E_A:.4f}")
        print(f"    E_self1={terms_A['E_self1']:.4f}, E_self2={terms_A['E_self2']:.4f}, "
              f"E_rep={terms_A['E_rep']:.4f}")

    # --- Endpoint B: K=1 merged + zero field ---
    if verbose:
        print("  Finding K=1 endpoint (merged formation)...")
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

    # Second field is zero (but must satisfy volume constraint m2)
    # At the merged endpoint, all mass is in field 1, field 2 is uniform at m2/n
    # Actually: B = (u_merged with mass m1+m2 rescaled to m1, zero_field with mass m2)
    # No — the task says B = (u_merged, 0_vec). But 0_vec can't satisfy volume m2.
    # Use: u_merged at full mass m_total in field 1, field 2 = uniform m2/n
    # This represents "formation 2 dissolved uniformly"
    u_zero = np.full(n, m2 / n)  # uniform background for field 2

    # Rescale merged to have mass m1 in field 1... no, keep it simple:
    # Field 1 gets the merged formation at mass m1, field 2 at uniform m2/n
    # But the merged formation naturally has mass m_total. Let's keep masses consistent:
    # At endpoint B, field 1 has the merged shape at mass m1, field 2 is uniform at m2/n
    u_merged_m1 = project_volume(u_merged * (m1 / m_total), m1)

    x_B = np.concatenate([u_merged_m1, u_zero])
    E_B, terms_B = k2_energy(x_B, n, ec, lambda_rep)

    if verbose:
        print(f"  K=1 merged: E={E_B:.4f}")
        print(f"    E_self1={terms_B['E_self1']:.4f}, E_self2={terms_B['E_self2']:.4f}, "
              f"E_rep={terms_B['E_rep']:.4f}")

    E_ref = min(E_A, E_B)

    # --- Linear interpolation path ---
    total_images = n_images + 2
    images = []
    for i in range(total_images):
        t = i / (total_images - 1)
        x_interp = (1.0 - t) * x_A + t * x_B
        x_interp = project_k2(x_interp, n, m1, m2)
        images.append(x_interp.copy())

    # Compute LI barrier
    li_energies = []
    for img in images:
        E, _ = k2_energy(img, n, ec, lambda_rep)
        li_energies.append(E)
    li_energies = np.array(li_energies)
    barrier_li = float(np.max(li_energies) - E_ref)

    if verbose:
        print(f"  Linear interpolation barrier: {barrier_li:.4f}")

    # --- NEB iteration ---
    max_force_clamp = 5.0
    enable_climbing_iter = max_iter // 4
    converged = False
    history = []

    for iteration in range(max_iter):
        # Compute energies and gradients
        energies = []
        gradients = []
        for i, img in enumerate(images):
            E, _ = k2_energy(img, n, ec, lambda_rep)
            energies.append(E)
            if i == 0 or i == total_images - 1:
                gradients.append(np.zeros(2 * n))
            else:
                grad = k2_gradient(img, n, ec, lambda_rep)
                grad = project_k2_gradient(grad, n)
                gradients.append(grad)

        energies_arr = np.array(energies)

        # Climbing image = highest energy interior image
        interior_E = energies_arr[1:-1]
        climbing_idx = int(np.argmax(interior_E)) + 1
        use_climbing = (iteration >= enable_climbing_iter)

        # NEB forces
        forces = []
        for i in range(1, total_images - 1):
            tau = neb_tangent(images, energies_arr, i)
            grad_i = gradients[i]

            if i == climbing_idx and use_climbing:
                # Climbing image: invert parallel component
                f = -grad_i + 2.0 * np.dot(grad_i, tau) * tau
            else:
                # Perpendicular true force + parallel spring force
                grad_par = np.dot(grad_i, tau) * tau
                grad_perp = grad_i - grad_par

                d_plus = np.linalg.norm(images[i + 1] - images[i])
                d_minus = np.linalg.norm(images[i] - images[i - 1])
                f_spring = k_spring * (d_plus - d_minus)

                f = -grad_perp + f_spring * tau

            # Clamp
            f_norm = np.linalg.norm(f)
            clamp = max_force_clamp * np.sqrt(2 * n)
            if f_norm > clamp:
                f = f * (clamp / f_norm)

            forces.append(f)

        # Convergence check
        max_force_perp = 0.0
        for idx, i in enumerate(range(1, total_images - 1)):
            tau = neb_tangent(images, energies_arr, i)
            grad_i = gradients[i]
            grad_perp = grad_i - np.dot(grad_i, tau) * tau
            f_perp = np.linalg.norm(grad_perp) / np.sqrt(2 * n)
            max_force_perp = max(max_force_perp, f_perp)

        saddle_E = float(energies_arr[climbing_idx])
        barrier_current = saddle_E - E_ref

        history.append({
            'iter': iteration,
            'max_force_perp': float(max_force_perp),
            'barrier': float(barrier_current),
            'climbing_E': saddle_E,
        })

        if verbose and iteration % 500 == 0:
            print(f"    NEB iter {iteration}: max_f_perp={max_force_perp:.4f}, "
                  f"barrier={barrier_current:.4f}"
                  f"{' [CI]' if use_climbing else ''}")

        if max_force_perp < tol:
            converged = True
            if verbose:
                print(f"  NEB converged at iteration {iteration}")
            break

        # Steepest descent update
        for idx, i in enumerate(range(1, total_images - 1)):
            images[i] = images[i] + dt * forces[idx]
            images[i] = project_k2(images[i], n, m1, m2)

    # Final energies and decomposition
    final_energies = []
    final_decomp = []
    for img in images:
        E, terms = k2_energy(img, n, ec, lambda_rep)
        final_energies.append(E)
        final_decomp.append(terms)
    final_energies = np.array(final_energies)

    saddle_idx = int(np.argmax(final_energies[1:-1])) + 1
    barrier_neb = float(final_energies[saddle_idx] - E_ref)

    # Energy profile along path
    energy_profile = []
    for i in range(total_images):
        t = i / (total_images - 1)
        energy_profile.append({
            't': float(t),
            'E_total': float(final_energies[i]),
            'E_self1': float(final_decomp[i]['E_self1']),
            'E_self2': float(final_decomp[i]['E_self2']),
            'E_rep': float(final_decomp[i]['E_rep']),
        })

    return {
        'barrier_li': float(barrier_li),
        'barrier_neb': float(barrier_neb),
        'ratio_neb_li': float(barrier_neb / max(barrier_li, 1e-14)),
        'E_A': float(E_A),
        'E_B': float(E_B),
        'E_A_self1': float(terms_A['E_self1']),
        'E_A_self2': float(terms_A['E_self2']),
        'E_A_rep': float(terms_A['E_rep']),
        'E_B_self1': float(terms_B['E_self1']),
        'E_B_self2': float(terms_B['E_self2']),
        'E_B_rep': float(terms_B['E_rep']),
        'saddle_E': float(final_energies[saddle_idx]),
        'saddle_self1': float(final_decomp[saddle_idx]['E_self1']),
        'saddle_self2': float(final_decomp[saddle_idx]['E_self2']),
        'saddle_rep': float(final_decomp[saddle_idx]['E_rep']),
        'saddle_idx': saddle_idx,
        'converged': converged,
        'n_iter': len(history),
        'final_max_force_perp': float(history[-1]['max_force_perp']) if history else float('inf'),
        'energy_profile': energy_profile,
        'history_tail': history[-5:],
        'm1': float(m1),
        'm2': float(m2),
    }


# ---------------------------------------------------------------------------
# Main: sweep λ_rep
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("  Experiment 61: K-field NEB — Full ℝ^{2n} Merge Barrier")
    print("=" * 70)
    print()
    print("  Key fix over exp60: NEB in concatenated (u1,u2) space")
    print("  includes repulsion energy λ_rep·⟨u1,u2⟩ in the path.")
    print()

    grid_size = (10, 10)
    beta = 10
    lambda_reps = [0, 1, 5, 10, 20]
    n_images = 20
    k_spring = 0.5
    dt = 0.001
    max_iter = 3000
    tol = 0.1

    g = GraphState.grid_2d(*grid_size)
    n = g.n

    all_results = {
        'config': {
            'grid': list(grid_size),
            'beta': beta,
            'n_images': n_images,
            'k_spring': k_spring,
            'dt': dt,
            'max_iter': max_iter,
            'tol': tol,
        },
        'runs': {},
    }

    barriers_by_lrep = {}

    for lrep in lambda_reps:
        label = f"lrep_{lrep}"
        print(f"\n{'='*60}")
        print(f"  λ_rep = {lrep}")
        print(f"{'='*60}")

        t0 = time.time()

        p = ParameterRegistry(
            beta_bd=beta,
            volume_fraction=0.3,
            max_iter=5000,
            n_restarts=3,
            eps_grad=1e-3,
        )

        result = kfield_neb(
            g, p, lambda_rep=lrep,
            n_images=n_images, k_spring=k_spring,
            dt=dt, max_iter=max_iter, tol=tol,
            verbose=True,
        )

        elapsed = time.time() - t0
        result['elapsed_s'] = float(elapsed)
        result['lambda_rep'] = lrep

        print(f"\n  Results for λ_rep={lrep}:")
        print(f"    ΔE_LI  = {result['barrier_li']:.4f}")
        print(f"    ΔE_NEB = {result['barrier_neb']:.4f}")
        print(f"    NEB/LI = {result['ratio_neb_li']:.4f}")
        print(f"    Saddle decomposition:")
        print(f"      E_self1 = {result['saddle_self1']:.4f}")
        print(f"      E_self2 = {result['saddle_self2']:.4f}")
        print(f"      E_rep   = {result['saddle_rep']:.4f}")
        print(f"    Converged: {result['converged']} ({result['n_iter']} iters)")
        print(f"    Time: {elapsed:.1f}s")

        # Strip energy_profile for storage (keep summary)
        result_save = {k: v for k, v in result.items() if k != 'energy_profile'}
        # Keep just the energy values along the path
        result_save['energy_path'] = [ep['E_total'] for ep in result['energy_profile']]
        result_save['rep_path'] = [ep['E_rep'] for ep in result['energy_profile']]

        all_results['runs'][label] = result_save
        barriers_by_lrep[lrep] = {
            'barrier_li': result['barrier_li'],
            'barrier_neb': result['barrier_neb'],
        }

    # --- Summary ---
    print("\n" + "=" * 70)
    print("  SUMMARY: Barrier vs λ_rep")
    print("=" * 70)
    print(f"  {'λ_rep':>8}  {'ΔE_LI':>10}  {'ΔE_NEB':>10}  {'NEB/LI':>8}  {'Source':>12}")
    print(f"  {'─'*8}  {'─'*10}  {'─'*10}  {'─'*8}  {'─'*12}")

    for lrep in lambda_reps:
        b = barriers_by_lrep[lrep]
        ratio = b['barrier_neb'] / max(b['barrier_li'], 1e-14)
        if lrep == 0:
            source = "self only"
        else:
            source = "self+rep"
        print(f"  {lrep:>8}  {b['barrier_li']:>10.4f}  {b['barrier_neb']:>10.4f}  "
              f"{ratio:>8.4f}  {source:>12}")

    # Key diagnostic: does barrier vanish at λ_rep=0?
    b0 = barriers_by_lrep[0]['barrier_neb']
    b10 = barriers_by_lrep[10]['barrier_neb']
    print()
    if abs(b0) < 0.5:
        print("  ★ λ_rep=0: barrier ≈ 0 — confirms no self-energy barrier to merge")
    else:
        print(f"  ★ λ_rep=0: barrier = {b0:.4f} — self-energy barrier present!")

    if b10 > 1.0:
        print(f"  ★ λ_rep=10: barrier = {b10:.4f} — repulsion creates genuine barrier")
        print(f"    Barrier increment from repulsion: {b10 - b0:.4f}")
    else:
        print(f"  ★ λ_rep=10: barrier = {b10:.4f} — weak barrier even with repulsion")

    all_results['summary'] = {
        'barriers': barriers_by_lrep,
        'barrier_at_lrep0': float(b0),
        'barrier_at_lrep10': float(b10),
        'barrier_increment_from_repulsion': float(b10 - b0),
        'self_energy_barrier_present': bool(abs(b0) >= 0.5),
        'repulsion_barrier_significant': bool(b10 > 1.0),
    }

    # Save
    out_path = os.path.join(os.path.dirname(__file__), 'results', 'exp61_kfield_neb.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")


if __name__ == '__main__':
    main()
