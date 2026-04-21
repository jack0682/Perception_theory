"""NEB (Nudged Elastic Band) for K=1 ↔ K=2 transition path on Σ_m.

Computes minimum energy path between two K-different minima of ℰ on Σ_m,
identifies saddle (highest-energy image), and reports ΔE_barrier.

Theoretical reference: `THEORY/working/E/M1_dissolution.md` §3-§5 (Kramers).
                       `THEORY/logs/daily/2026-04-21/05_deepening_and_verification.md` §3
                       (Mountain Pass + mollification).
                       `THEORY/logs/daily/2026-04-21/07_round4_verification.md` §3-§5
                       (linear-interp upper bound + Cheeger lower bound).

Algorithm (standard NEB + climbing image):
  1. Initialize chain of N images: u_1 (K=1), u_2, ..., u_N (K=2).
     Linear interpolation default; can warm-start from path.
  2. Compute force on each interior image:
     F_i^perp  = -∇ℰ - ((-∇ℰ) · τ_i) τ_i   (project out tangent component)
     F_i^spring = k · (|u_{i+1} - u_i| - |u_i - u_{i-1}|) · τ_i
     F_i^NEB   = F_i^perp + F_i^spring
  3. Project onto Σ_m tangent space (constant 1/n removed).
  4. Climbing image (CI-NEB): highest-energy image gets force
     F_ci = -∇ℰ + 2·((-∇ℰ) · τ) · τ   (climb up the gradient along tangent).
  5. Steepest descent until ‖F‖_max < tol.

Run from `CODE/`: python3 scripts/neb_k1k2.py
"""

from __future__ import annotations

import numpy as np

from scc import GraphState, ParameterRegistry, find_formation
from scc.energy import EnergyComputer
from scc.k_soft import k_soft, bernoulli_entropy


def project_to_tangent(grad: np.ndarray) -> np.ndarray:
    """Remove constant component (project onto T_u Σ_m = 1^⊥)."""
    return grad - grad.mean()


def project_to_simplex(u: np.ndarray, m: float, eps: float = 0.001) -> np.ndarray:
    """Project u onto Σ_m ∩ [eps, 1-eps]^n (with clipping + rescale)."""
    u = np.clip(u, eps, 1 - eps)
    u = u + (m - u.sum()) / u.size
    u = np.clip(u, eps, 1 - eps)
    # Iterate to enforce volume after clip
    for _ in range(20):
        diff = m - u.sum()
        if abs(diff) < 1e-9:
            break
        # Distribute diff to interior sites (those not at boundary)
        free = (u > eps + 1e-7) & (u < 1 - eps - 1e-7)
        if free.sum() == 0:
            break
        u[free] += diff / free.sum()
        u = np.clip(u, eps, 1 - eps)
    return u


def gauss_init(n_side: int, cx: float, cy: float, sigma: float = 1.5) -> np.ndarray:
    """Gaussian bump on n_side × n_side grid."""
    xs, ys = np.meshgrid(np.arange(n_side), np.arange(n_side))
    return np.exp(-((xs - cx) ** 2 + (ys - cy) ** 2) / (2 * sigma ** 2)).flatten()


def neb_relax(
    images: list[np.ndarray],
    energy_fn,  # u → (E, dict)
    grad_fn,  # u → ∇E
    m: float,
    n_iter: int = 500,
    k_spring: float = 5.0,
    dt: float = 0.005,
    climbing: bool = True,
    tol: float = 1e-3,
    verbose: bool = False,
) -> list[np.ndarray]:
    """Run NEB relaxation. Returns final image chain.

    Endpoints (images[0], images[-1]) are held fixed (K=1 / K=2 minima).
    """
    images = [im.copy() for im in images]
    N = len(images)
    n = images[0].size

    for it in range(n_iter):
        # Compute energies and gradients at each interior image
        Es = [energy_fn(im)[0] for im in images]
        grads = [grad_fn(im) for im in images]

        # Compute tangent vectors (improved tangent definition - Henkelman 2000)
        tangents = [None] * N
        for i in range(1, N - 1):
            E_prev, E_curr, E_next = Es[i - 1], Es[i], Es[i + 1]
            tau_p = images[i + 1] - images[i]
            tau_m = images[i] - images[i - 1]
            if E_next > E_curr > E_prev:
                tau = tau_p
            elif E_next < E_curr < E_prev:
                tau = tau_m
            else:
                # Local extremum: weighted by energy difference
                dE_max = max(abs(E_next - E_curr), abs(E_prev - E_curr))
                dE_min = min(abs(E_next - E_curr), abs(E_prev - E_curr))
                if E_next > E_prev:
                    tau = tau_p * dE_max + tau_m * dE_min
                else:
                    tau = tau_p * dE_min + tau_m * dE_max
            # Project onto tangent space + normalize
            tau = project_to_tangent(tau)
            norm = np.linalg.norm(tau)
            if norm > 1e-12:
                tau = tau / norm
            tangents[i] = tau

        # Compute NEB force and update interior images
        max_force = 0.0
        ci_idx = int(np.argmax(Es)) if climbing else -1
        for i in range(1, N - 1):
            tau = tangents[i]
            grad = grads[i]
            grad_t = project_to_tangent(grad)
            grad_par = (grad_t @ tau) * tau

            if i == ci_idx:
                # Climbing image: invert parallel gradient component
                F = -grad_t + 2 * grad_par
            else:
                # Standard NEB: perpendicular component + spring along tangent
                F_perp = -grad_t + grad_par
                spring_mag = k_spring * (
                    np.linalg.norm(images[i + 1] - images[i])
                    - np.linalg.norm(images[i] - images[i - 1])
                )
                F_spring = spring_mag * tau
                F = F_perp + F_spring

            # Update with steepest descent + projection back to Σ_m
            images[i] = images[i] + dt * F
            images[i] = project_to_simplex(images[i], m)
            max_force = max(max_force, np.linalg.norm(F))

        if verbose and (it % 50 == 0 or it == n_iter - 1):
            print(f"  iter {it:4d}: max_E = {max(Es):.4f}, max_force = {max_force:.4f}")

        if max_force < tol:
            if verbose:
                print(f"  Converged at iter {it} (max_force {max_force:.6f})")
            break

    return images


def find_minimum_with_seed(
    graph: GraphState,
    params: ParameterRegistry,
    u_init: np.ndarray,
) -> np.ndarray:
    """Wrapper around find_formation with explicit init."""
    result = find_formation(graph, params, u_init=u_init)
    return result.u


def main():
    # Setup: 12×12 grid, β = 30, c = 0.25 (canonical-style)
    n_side = 12
    n = n_side * n_side
    m = n / 4
    params = ParameterRegistry(
        beta_bd=30.0, alpha_bd=1.0, w_cl=1.0, w_sep=1e-5, w_bd=1.0,
        volume_fraction=0.25,
    )
    graph = GraphState.grid_2d(n_side, n_side)
    ec = EnergyComputer(graph, params)

    print(f"NEB on {n_side}×{n_side} grid, m={m}, β={params.beta_bd}")
    print()

    # Energy function and gradient
    def energy_fn(u):
        return ec.energy(u)

    def grad_fn(u):
        return ec.gradient(u)

    # Step 1: find K=1 and K=2 minima (multi-init for global)
    print("Finding K=1 minimum (multi-init)...")
    best_e_k1 = float("inf")
    best_k1 = None
    for sig in [0.7, 1.0, 1.3]:
        for cx in [3, 5.5, 8]:
            for cy in [3, 5.5, 8]:
                u0 = gauss_init(n_side, cx, cy, sig)
                u0 = u0 * (m / u0.sum())
                u0 = project_to_simplex(u0, m)
                u_min = find_minimum_with_seed(graph, params, u0)
                e_min = ec.energy(u_min)[0]
                ks = k_soft(u_min, n_side)
                if ks < 0.7 and e_min < best_e_k1:
                    best_e_k1 = e_min
                    best_k1 = u_min
    print(f"  K=1: E = {best_e_k1:.4f}, K_soft = {k_soft(best_k1, n_side):.4f}")

    print("Finding K=2 minimum (multi-init)...")
    best_e_k2 = float("inf")
    best_k2 = None
    for sig in [0.7, 1.0]:
        for (a, b), (c, d) in [
            ((2, 2), (9, 9)), ((2, 9), (9, 2)),
            ((1, 5.5), (10, 5.5)), ((5.5, 1), (5.5, 10)),
            ((3, 3), (8, 8)), ((4, 4), (7, 7)),
        ]:
            u0 = gauss_init(n_side, a, b, sig) + gauss_init(n_side, c, d, sig)
            u0 = u0 * (m / u0.sum())
            u0 = project_to_simplex(u0, m)
            u_min = find_minimum_with_seed(graph, params, u0)
            e_min = ec.energy(u_min)[0]
            ks = k_soft(u_min, n_side)
            if 0.8 < ks < 1.4 and e_min < best_e_k2:
                best_e_k2 = e_min
                best_k2 = u_min
    print(f"  K=2: E = {best_e_k2:.4f}, K_soft = {k_soft(best_k2, n_side):.4f}")
    print(f"  Initial ΔE = {best_e_k2 - best_e_k1:.4f}")
    print()

    # Step 2: Initialize NEB chain (linear interpolation)
    N_images = 11
    print(f"Initializing NEB chain ({N_images} images, linear interp)...")
    images = []
    for i in range(N_images):
        t = i / (N_images - 1)
        u_i = (1 - t) * best_k1 + t * best_k2
        u_i = project_to_simplex(u_i, m)
        images.append(u_i)

    # Compute initial energy profile
    print("Initial energy profile (linear interp):")
    for i, im in enumerate(images):
        E, _ = ec.energy(im)
        ks = k_soft(im, n_side)
        print(f"  image {i:2d}: E = {E:.4f}, K_soft = {ks:.4f}")
    initial_max_E = max(ec.energy(im)[0] for im in images)
    print(f"  Linear-interp max E (upper bound on saddle): {initial_max_E:.4f}")
    print(f"  Round 4 §4 corrected estimate was ~ 47.5; observed: {initial_max_E:.4f}")
    print()

    # Step 3: NEB relaxation
    print("Running NEB relaxation...")
    images = neb_relax(
        images, energy_fn, grad_fn, m,
        n_iter=300, k_spring=5.0, dt=0.001, climbing=True, tol=1e-3, verbose=True,
    )

    # Step 4: Final energy profile
    print()
    print("Final energy profile (post-NEB):")
    Es_final = [ec.energy(im)[0] for im in images]
    for i, im in enumerate(images):
        E = Es_final[i]
        ks = k_soft(im, n_side)
        marker = " ← SADDLE (climbing image)" if i == int(np.argmax(Es_final)) else ""
        print(f"  image {i:2d}: E = {E:.4f}, K_soft = {ks:.4f}{marker}")

    # Step 5: Saddle properties
    saddle_idx = int(np.argmax(Es_final))
    saddle = images[saddle_idx]
    E_saddle = Es_final[saddle_idx]
    delta_F_barrier = E_saddle - best_e_k2  # K=2 → K=1 barrier (climb from K=2)
    delta_E_K2K1 = E_saddle - max(best_e_k1, best_e_k2)
    print()
    print(f"=== Saddle analysis ===")
    print(f"Saddle index: {saddle_idx}")
    print(f"E_saddle = {E_saddle:.4f}")
    print(f"K_soft(saddle) = {k_soft(saddle, n_side):.4f}")
    print(f"ΔE (K=2 → K=1, from K=2 minimum): {E_saddle - best_e_k2:.4f}")
    print(f"ΔE (K=1 → K=2, from K=1 minimum): {E_saddle - best_e_k1:.4f}")
    print(f"ΔE_barrier (above higher minimum): {E_saddle - max(best_e_k1, best_e_k2):.4f}")
    print()
    print(f"=== Comparison with Round 4 estimates ===")
    print(f"Linear-interp upper bound (Round 4 §4 corrected): ΔF ≤ 40.7")
    print(f"Cheeger lower bound (Round 4 §5):                ΔF ≥ 2.3")
    print(f"NEB measured ΔE_barrier:                          {E_saddle - max(best_e_k1, best_e_k2):.4f}")
    print(f"Compared to canonical exp38 reference (~ 20):    {E_saddle - max(best_e_k1, best_e_k2):.4f}")
    print()
    return E_saddle, best_e_k1, best_e_k2, saddle, best_k1, best_k2


if __name__ == "__main__":
    main()
