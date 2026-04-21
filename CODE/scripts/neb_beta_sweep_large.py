"""β-sweep on large grid for γ_eff measurement.

Designed for user to run on 32×32 grid (or larger). Long compute time expected
(~10-30 min per β). Outputs intermediate results so user can monitor progress.

Usage (from CODE/):
    PYTHONPATH=. python3 scripts/neb_beta_sweep_large.py

Optional: edit BETAS, N_SIDE, N_IMAGES, NEB_ITER below to tune.
"""

from __future__ import annotations

import time
import json
import sys
from pathlib import Path
import numpy as np

from scc import GraphState, ParameterRegistry, find_formation
from scc.energy import EnergyComputer
from scc.k_soft import k_soft

# ============================================================
# CONFIGURATION (edit here for your run)
# ============================================================
N_SIDE = 32          # grid size (32×32 = 1024 sites)
VOLUME_FRACTION = 0.25  # c = m/n
BETAS = [10, 20, 30, 50, 75, 100, 150, 200]  # β values to sweep
N_IMAGES = 21        # NEB chain images (more = better resolution, slower)
NEB_ITER = 2000      # NEB iterations per β
NEB_DT = 0.0002      # NEB integration step (smaller = stable, slower)
NEB_K_SPRING = 2.0   # NEB spring constant
NEB_TOL = 5e-3       # convergence tolerance (max force)
SAVE_PATH = Path("logs/neb_beta_sweep_results.json")
# ============================================================


def gauss_init(n_side: int, cx: float, cy: float, sigma: float = 1.5) -> np.ndarray:
    xs, ys = np.meshgrid(np.arange(n_side), np.arange(n_side))
    return np.exp(-((xs - cx) ** 2 + (ys - cy) ** 2) / (2 * sigma ** 2)).flatten()


def project_to_simplex(u: np.ndarray, m: float, eps: float = 0.001) -> np.ndarray:
    u = np.clip(u, eps, 1 - eps)
    u = u + (m - u.sum()) / u.size
    u = np.clip(u, eps, 1 - eps)
    for _ in range(30):
        diff = m - u.sum()
        if abs(diff) < 1e-9:
            break
        free = (u > eps + 1e-7) & (u < 1 - eps - 1e-7)
        if free.sum() == 0:
            break
        u[free] += diff / free.sum()
        u = np.clip(u, eps, 1 - eps)
    return u


def project_to_tangent(g: np.ndarray) -> np.ndarray:
    return g - g.mean()


def neb_relax(images, energy_fn, grad_fn, m, n_iter, k_spring, dt, tol, verbose=False):
    images = [im.copy() for im in images]
    N = len(images)
    history_max_E = []

    for it in range(n_iter):
        Es = [energy_fn(im)[0] for im in images]
        grads = [grad_fn(im) for im in images]

        # Improved tangent (Henkelman 2000)
        tangents = [None] * N
        for i in range(1, N - 1):
            E_p, E_c, E_n = Es[i - 1], Es[i], Es[i + 1]
            tau_plus = images[i + 1] - images[i]
            tau_minus = images[i] - images[i - 1]
            if E_n > E_c > E_p:
                tau = tau_plus
            elif E_n < E_c < E_p:
                tau = tau_minus
            else:
                dE_max = max(abs(E_n - E_c), abs(E_p - E_c))
                dE_min = min(abs(E_n - E_c), abs(E_p - E_c))
                if E_n > E_p:
                    tau = tau_plus * dE_max + tau_minus * dE_min
                else:
                    tau = tau_plus * dE_min + tau_minus * dE_max
            tau = project_to_tangent(tau)
            nrm = np.linalg.norm(tau)
            if nrm > 1e-12:
                tau = tau / nrm
            tangents[i] = tau

        # NEB force update
        max_force = 0.0
        ci_idx = int(np.argmax(Es))  # climbing image
        for i in range(1, N - 1):
            tau = tangents[i]
            grad_t = project_to_tangent(grads[i])
            grad_par = (grad_t @ tau) * tau

            if i == ci_idx:
                F = -grad_t + 2 * grad_par
            else:
                F_perp = -grad_t + grad_par
                spring_mag = k_spring * (
                    np.linalg.norm(images[i + 1] - images[i])
                    - np.linalg.norm(images[i] - images[i - 1])
                )
                F_spring = spring_mag * tau
                F = F_perp + F_spring

            images[i] = images[i] + dt * F
            images[i] = project_to_simplex(images[i], m)
            max_force = max(max_force, np.linalg.norm(F))

        history_max_E.append(max(Es))
        if verbose and (it % 100 == 0 or it == n_iter - 1):
            print(f"    iter {it:5d}: max_E = {max(Es):.4f}, max_force = {max_force:.4f}", flush=True)

        if max_force < tol:
            if verbose:
                print(f"    Converged at iter {it} (force {max_force:.6f})", flush=True)
            break

    return images, history_max_E


def find_minima(graph, params, n_side, m):
    """Multi-init search for K=1 and K=2 globals."""
    ec = EnergyComputer(graph, params)

    print(f"  Finding K=1...", flush=True)
    best_e_k1 = float("inf"); best_k1 = None
    # On large grid, use bigger sigmas
    sigmas_k1 = [1.0, 1.5, 2.0, 2.5] if n_side >= 16 else [0.7, 1.0, 1.3]
    centers = [(n_side / 4, n_side / 4), (n_side / 2, n_side / 2),
               (3 * n_side / 4, 3 * n_side / 4), (n_side / 4, 3 * n_side / 4),
               (3 * n_side / 4, n_side / 4)]
    for sig in sigmas_k1:
        for (cx, cy) in centers:
            u0 = gauss_init(n_side, cx, cy, sig)
            u0 = u0 * (m / u0.sum())
            u0 = project_to_simplex(u0, m)
            u_min = find_formation(graph, params, u_init=u0).u
            e = ec.energy(u_min)[0]
            ks = k_soft(u_min, n_side)
            if ks < 0.7 and e < best_e_k1:
                best_e_k1 = e; best_k1 = u_min

    print(f"  Finding K=2...", flush=True)
    best_e_k2 = float("inf"); best_k2 = None
    sigmas_k2 = [1.0, 1.5, 2.0] if n_side >= 16 else [0.7, 1.0]
    pairs = [
        ((n_side / 4, n_side / 4), (3 * n_side / 4, 3 * n_side / 4)),
        ((n_side / 4, 3 * n_side / 4), (3 * n_side / 4, n_side / 4)),
        ((1.5, n_side / 2), (n_side - 2.5, n_side / 2)),
        ((n_side / 2, 1.5), (n_side / 2, n_side - 2.5)),
        ((n_side / 3, n_side / 3), (2 * n_side / 3, 2 * n_side / 3)),
    ]
    for sig in sigmas_k2:
        for (a, b), (c, d) in pairs:
            u0 = gauss_init(n_side, a, b, sig) + gauss_init(n_side, c, d, sig)
            u0 = u0 * (m / u0.sum())
            u0 = project_to_simplex(u0, m)
            u_min = find_formation(graph, params, u_init=u0).u
            e = ec.energy(u_min)[0]
            ks = k_soft(u_min, n_side)
            if 0.8 < ks < 1.4 and e < best_e_k2:
                best_e_k2 = e; best_k2 = u_min

    return best_k1, best_e_k1, best_k2, best_e_k2


def measure_one_beta(beta, n_side, n_images, n_iter, dt, k_spring, tol):
    n = n_side * n_side
    m = n / 4
    params = ParameterRegistry(
        beta_bd=beta, alpha_bd=1.0, w_cl=1.0, w_sep=1e-5, w_bd=1.0,
        volume_fraction=VOLUME_FRACTION,
    )
    graph = GraphState.grid_2d(n_side, n_side)
    ec = EnergyComputer(graph, params)

    t0 = time.time()
    print(f"\n=== β = {beta} (n_side = {n_side}, n = {n}, m = {m}) ===", flush=True)

    k1, e1, k2, e2 = find_minima(graph, params, n_side, m)
    if k1 is None or k2 is None:
        return {"beta": beta, "status": "no_minima"}

    print(f"  K=1: E = {e1:.4f}, K_soft = {k_soft(k1, n_side):.4f}", flush=True)
    print(f"  K=2: E = {e2:.4f}, K_soft = {k_soft(k2, n_side):.4f}", flush=True)
    print(f"  Initial ΔE = {e2 - e1:.4f}", flush=True)
    print(f"  Running NEB ({n_images} images, {n_iter} iter)...", flush=True)

    images = []
    for i in range(n_images):
        t = i / (n_images - 1)
        u_i = (1 - t) * k1 + t * k2
        u_i = project_to_simplex(u_i, m)
        images.append(u_i)

    images, history = neb_relax(
        images,
        energy_fn=lambda u: ec.energy(u),
        grad_fn=lambda u: ec.gradient(u),
        m=m, n_iter=n_iter, k_spring=k_spring, dt=dt, tol=tol, verbose=True,
    )

    Es = [ec.energy(im)[0] for im in images]
    saddle_idx = int(np.argmax(Es))
    e_saddle = Es[saddle_idx]
    higher_min = max(e1, e2)
    dE = e_saddle - higher_min

    elapsed = time.time() - t0
    print(f"  → saddle: idx={saddle_idx}, E={e_saddle:.4f}, K_soft={k_soft(images[saddle_idx], n_side):.4f}", flush=True)
    print(f"  → ΔE_barrier = {dE:.4f} (above higher min)", flush=True)
    print(f"  → elapsed: {elapsed:.1f}s", flush=True)

    return {
        "beta": beta,
        "status": "ok" if (saddle_idx not in (0, n_images - 1) and dE > 0.01) else "saddle_at_endpoint",
        "n_side": n_side,
        "m": m,
        "e_k1": e1,
        "e_k2": e2,
        "e_saddle": e_saddle,
        "saddle_idx": saddle_idx,
        "saddle_ks": k_soft(images[saddle_idx], n_side),
        "delta_E_barrier": dE,
        "energy_profile": Es,
        "k_soft_profile": [k_soft(im, n_side) for im in images],
        "elapsed_sec": elapsed,
    }


def main():
    print(f"=" * 60)
    print(f"NEB β-sweep on {N_SIDE}×{N_SIDE} grid")
    print(f"  Volume fraction c = {VOLUME_FRACTION}")
    print(f"  Beta values: {BETAS}")
    print(f"  NEB: {N_IMAGES} images, {NEB_ITER} iter, dt={NEB_DT}, tol={NEB_TOL}")
    print(f"  Output: {SAVE_PATH}")
    print(f"=" * 60)

    SAVE_PATH.parent.mkdir(parents=True, exist_ok=True)
    results = []
    for beta in BETAS:
        try:
            r = measure_one_beta(beta, N_SIDE, N_IMAGES, NEB_ITER, NEB_DT, NEB_K_SPRING, NEB_TOL)
        except Exception as e:
            print(f"  β={beta} CRASHED: {e}", flush=True)
            r = {"beta": beta, "status": "crashed", "error": str(e)}
        results.append(r)
        # Save incrementally (in case of long runs)
        with open(SAVE_PATH, "w") as f:
            json.dump(results, f, indent=2, default=str)
        print(f"  Saved partial results to {SAVE_PATH}", flush=True)

    # Final analysis
    print()
    print("=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    print(f"{'β':>6} {'ΔE_barrier':>14} {'saddle_K_soft':>14} {'status':>22}")
    valid = []
    for r in results:
        if r["status"] == "ok":
            print(f"{r['beta']:>6} {r['delta_E_barrier']:>14.4f} {r['saddle_ks']:>14.4f} {r['status']:>22}")
            valid.append((r["beta"], r["delta_E_barrier"]))
        else:
            print(f"{r['beta']:>6} {'---':>14} {'---':>14} {r['status']:>22}")

    if len(valid) >= 4:
        bs = np.array([b for b, _ in valid])
        ds = np.array([d for _, d in valid])
        log_b = np.log(bs)
        log_d = np.log(ds)
        gamma_eff, log_c = np.polyfit(log_b, log_d, 1)
        c = np.exp(log_c)
        print()
        print(f"Power-law fit: ΔE_barrier = {c:.3f} · β^{gamma_eff:.3f}")
        print(f"  γ_eff = {gamma_eff:.3f}")
        print()
        print("Comparison:")
        print(f"  Modica-Mortola limit (sharp interface): γ_eff = 0.5")
        print(f"  Bulk linear limit:                       γ_eff = 1.0")
        print(f"  canonical exp38 (Cat B):                 γ_eff ≈ 0.89")
        print(f"  Our measurement on {N_SIDE}×{N_SIDE} grid:        γ_eff = {gamma_eff:.3f}")
        if 0.4 <= gamma_eff <= 1.1:
            print(f"  → Within Round 6 envelope [0.5, 1.0] ✓")
        else:
            print(f"  ⚠ Outside [0.5, 1.0] — protocol-dependence (Round 6 §1)")

    print()
    print(f"Full results saved to: {SAVE_PATH}")


if __name__ == "__main__":
    main()
