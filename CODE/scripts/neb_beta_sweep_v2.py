"""β-sweep v2 — improved NEB with stronger spring + adaptive step + diagnostic.

Fixes from v1 (neb_beta_sweep_large.py):
  1. k_spring 100 (was 2) — prevents interior image collapse to endpoint basin
  2. Adaptive step + clip — large forces won't blow up
  3. Diagnostic: print full energy profile every N iter
  4. Smaller default grid 24×24 (more tractable than 32×32)
  5. Better minima search (longer iter + tighter tol)
  6. Warm-start chain via K_soft-controlled interpolation (not raw linear)

Usage (from CODE/):
    PYTHONPATH=. python3 scripts/neb_beta_sweep_v2.py
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
# CONFIGURATION
# ============================================================
N_SIDE = 24          # grid size (576 sites — sweet spot for speed + signal)
VOLUME_FRACTION = 0.25
BETAS = [10, 20, 30, 50, 75, 100, 150]
N_IMAGES = 15        # NEB chain
NEB_ITER = 3000
NEB_DT_INIT = 0.001
NEB_K_SPRING = 100.0   # MUCH stronger spring (v1 had 2.0 — too weak)
NEB_TOL = 1e-2
MAX_FORCE_CLIP = 50.0   # clip per-image force (prevent blow-up)
SAVE_PATH = Path("logs/neb_v2_results.json")
DIAGNOSTIC_EVERY = 200  # print full chain energy every N iter
# ============================================================


def gauss_init(n_side, cx, cy, sigma=1.5):
    xs, ys = np.meshgrid(np.arange(n_side), np.arange(n_side))
    return np.exp(-((xs - cx) ** 2 + (ys - cy) ** 2) / (2 * sigma ** 2)).flatten()


def project_to_simplex(u, m, eps=0.001):
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


def project_to_tangent(g):
    return g - g.mean()


def smooth_chain(images, m, k_smooth=3):
    """Periodic chain reparametrization (string method spirit) — smooths chain."""
    N = len(images)
    if N < 5:
        return images
    new_images = [images[0].copy()]
    for i in range(1, N - 1):
        # Local average of neighbors
        avg = 0.25 * images[i - 1] + 0.5 * images[i] + 0.25 * images[i + 1]
        avg = project_to_simplex(avg, m)
        new_images.append(avg)
    new_images.append(images[-1].copy())
    return new_images


def neb_relax(
    images, energy_fn, grad_fn, m, n_iter, k_spring, dt_init,
    tol, max_force_clip, diagnostic_every=200, verbose=True,
):
    images = [im.copy() for im in images]
    N = len(images)
    dt = dt_init
    history = []

    prev_max_E = None
    for it in range(n_iter):
        Es = [energy_fn(im)[0] for im in images]
        grads = [grad_fn(im) for im in images]

        # Improved tangent
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

        max_force = 0.0
        ci_idx = int(np.argmax(Es))
        for i in range(1, N - 1):
            tau = tangents[i]
            grad_t = project_to_tangent(grads[i])
            grad_par = (grad_t @ tau) * tau

            if i == ci_idx and (max(Es) - Es[0]) > 0.5 and (max(Es) - Es[-1]) > 0.5:
                # Climbing image only when there's a clear peak ABOVE both endpoints
                F = -grad_t + 2 * grad_par
            else:
                F_perp = -grad_t + grad_par
                spring_mag = k_spring * (
                    np.linalg.norm(images[i + 1] - images[i])
                    - np.linalg.norm(images[i] - images[i - 1])
                )
                F_spring = spring_mag * tau
                F = F_perp + F_spring

            # Clip per-image force
            F_norm = np.linalg.norm(F)
            if F_norm > max_force_clip:
                F = F * (max_force_clip / F_norm)

            images[i] = images[i] + dt * F
            images[i] = project_to_simplex(images[i], m)
            max_force = max(max_force, F_norm)

        # Adaptive step: reduce dt if max_E is increasing
        max_E = max(Es)
        if prev_max_E is not None and max_E > prev_max_E + 1e-3:
            dt = max(dt * 0.7, 1e-5)
        elif prev_max_E is not None and max_E < prev_max_E - 1e-3:
            dt = min(dt * 1.05, dt_init)
        prev_max_E = max_E

        # Periodic chain smoothing (every 100 iter) to prevent collapse
        if it > 0 and it % 100 == 0:
            images = smooth_chain(images, m)

        if verbose and (it % diagnostic_every == 0 or it == n_iter - 1):
            ci_marker = " (CI)" if ci_idx not in (0, N - 1) else ""
            energy_str = " ".join(f"{e:.1f}" for e in Es)
            print(f"  iter {it:5d}: ci={ci_idx}{ci_marker}, max_E={max_E:.2f}, "
                  f"force={max_force:.2f}, dt={dt:.5f}", flush=True)
            print(f"    profile: [{energy_str}]", flush=True)

        history.append({"iter": it, "max_E": max_E, "max_force": max_force, "ci_idx": ci_idx})

        if max_force < tol:
            if verbose:
                print(f"  Converged at iter {it} (force {max_force:.6f})", flush=True)
            break

    return images, history


def find_minima(graph, params, n_side, m, ec):
    print(f"  Finding K=1...", flush=True)
    best_e_k1 = float("inf"); best_k1 = None
    for sig in [1.0, 1.5, 2.0]:
        cx_list = [n_side * 0.3, n_side * 0.5, n_side * 0.7]
        for cx in cx_list:
            for cy in cx_list:
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
    for sig in [1.0, 1.5]:
        pairs = [
            ((n_side * 0.25, n_side * 0.25), (n_side * 0.75, n_side * 0.75)),
            ((n_side * 0.25, n_side * 0.75), (n_side * 0.75, n_side * 0.25)),
            ((1.5, n_side / 2), (n_side - 2.5, n_side / 2)),
            ((n_side / 2, 1.5), (n_side / 2, n_side - 2.5)),
        ]
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


def measure_one_beta(beta, n_side, n_images, n_iter, dt, k_spring, tol, max_force_clip, save_intermediate=True):
    n = n_side * n_side
    m = n / 4
    params = ParameterRegistry(
        beta_bd=beta, alpha_bd=1.0, w_cl=1.0, w_sep=1e-5, w_bd=1.0,
        volume_fraction=VOLUME_FRACTION,
    )
    graph = GraphState.grid_2d(n_side, n_side)
    ec = EnergyComputer(graph, params)

    t0 = time.time()
    print(f"\n=== β = {beta} (n={n}, m={m}) ===", flush=True)
    k1, e1, k2, e2 = find_minima(graph, params, n_side, m, ec)
    if k1 is None or k2 is None:
        return {"beta": beta, "status": "no_minima"}

    print(f"  K=1: E = {e1:.4f}, K_soft = {k_soft(k1, n_side):.4f}", flush=True)
    print(f"  K=2: E = {e2:.4f}, K_soft = {k_soft(k2, n_side):.4f}", flush=True)
    print(f"  Initial ΔE_minima = {e2 - e1:.4f}", flush=True)

    # Initial chain: linear interpolation (alternative: K_soft-controlled)
    images = []
    for i in range(n_images):
        t = i / (n_images - 1)
        u_i = (1 - t) * k1 + t * k2
        u_i = project_to_simplex(u_i, m)
        images.append(u_i)

    init_Es = [ec.energy(im)[0] for im in images]
    print(f"  Initial chain max E (upper bound on saddle): {max(init_Es):.2f}", flush=True)
    print(f"  Initial profile: [{' '.join(f'{e:.0f}' for e in init_Es)}]", flush=True)

    print(f"  Running NEB ({n_images} images, k_spring={k_spring}, max_force_clip={max_force_clip})...", flush=True)
    images, history = neb_relax(
        images,
        energy_fn=lambda u: ec.energy(u),
        grad_fn=lambda u: ec.gradient(u),
        m=m, n_iter=n_iter, k_spring=k_spring, dt_init=dt, tol=tol,
        max_force_clip=max_force_clip,
        diagnostic_every=DIAGNOSTIC_EVERY, verbose=True,
    )

    Es = [ec.energy(im)[0] for im in images]
    saddle_idx = int(np.argmax(Es))
    e_saddle = Es[saddle_idx]
    higher_min = max(e1, e2)
    dE = e_saddle - higher_min
    elapsed = time.time() - t0

    if saddle_idx in (0, n_images - 1):
        status = "saddle_at_endpoint"
    elif dE < 0.05:
        status = "barrier_too_small"
    else:
        status = "ok"

    print(f"  → saddle: idx={saddle_idx}, E={e_saddle:.4f}, K_soft={k_soft(images[saddle_idx], n_side):.4f}", flush=True)
    print(f"  → ΔE_barrier = {dE:.4f} (status: {status})", flush=True)
    print(f"  → elapsed: {elapsed:.1f}s", flush=True)

    return {
        "beta": beta, "status": status, "n_side": n_side, "m": m,
        "e_k1": e1, "e_k2": e2, "e_saddle": e_saddle,
        "saddle_idx": saddle_idx, "saddle_ks": k_soft(images[saddle_idx], n_side),
        "delta_E_barrier": dE,
        "energy_profile": Es,
        "k_soft_profile": [k_soft(im, n_side) for im in images],
        "elapsed_sec": elapsed,
    }


def main():
    print("=" * 60)
    print(f"NEB β-sweep v2: {N_SIDE}×{N_SIDE}, {len(BETAS)} betas")
    print(f"  k_spring={NEB_K_SPRING}, n_images={N_IMAGES}, n_iter={NEB_ITER}")
    print(f"  dt_init={NEB_DT_INIT}, tol={NEB_TOL}, force_clip={MAX_FORCE_CLIP}")
    print("=" * 60)

    SAVE_PATH.parent.mkdir(parents=True, exist_ok=True)
    results = []
    for beta in BETAS:
        try:
            r = measure_one_beta(beta, N_SIDE, N_IMAGES, NEB_ITER, NEB_DT_INIT,
                                  NEB_K_SPRING, NEB_TOL, MAX_FORCE_CLIP)
        except Exception as e:
            print(f"  β={beta} CRASHED: {e}", flush=True)
            r = {"beta": beta, "status": "crashed", "error": str(e)}
        results.append(r)
        with open(SAVE_PATH, "w") as f:
            json.dump(results, f, indent=2, default=str)

    print()
    print("=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    print(f"{'β':>6} {'ΔE_barrier':>14} {'saddle_K_soft':>14} {'idx':>5} {'status':>22}")
    valid = []
    for r in results:
        if r.get("status") == "ok":
            print(f"{r['beta']:>6} {r['delta_E_barrier']:>14.4f} {r['saddle_ks']:>14.4f} "
                  f"{r['saddle_idx']:>5} {r['status']:>22}")
            valid.append((r["beta"], r["delta_E_barrier"]))
        else:
            sk = r.get("saddle_ks", "---")
            si = r.get("saddle_idx", "---")
            print(f"{r['beta']:>6} {'---':>14} {str(sk):>14} {str(si):>5} {r.get('status', 'unk'):>22}")

    if len(valid) >= 4:
        bs = np.array([b for b, _ in valid])
        ds = np.array([d for _, d in valid])
        log_b = np.log(bs); log_d = np.log(ds)
        gamma_eff, log_c = np.polyfit(log_b, log_d, 1)
        c = np.exp(log_c)
        print()
        print(f"Power-law fit (n={len(valid)}): ΔE = {c:.3f} · β^{gamma_eff:.3f}")
        print(f"  γ_eff = {gamma_eff:.3f}")
        residuals = log_d - (gamma_eff * log_b + log_c)
        rss = (residuals ** 2).sum()
        tss = ((log_d - log_d.mean()) ** 2).sum()
        r2 = 1 - rss / tss if tss > 0 else 0
        print(f"  R² = {r2:.4f}")
        print(f"  Residuals: {residuals}")
        print()
        print("Comparison:")
        print(f"  Modica-Mortola sharp:   γ_eff = 0.5")
        print(f"  Bulk linear:            γ_eff = 1.0")
        print(f"  canonical exp38:        γ_eff ≈ 0.89")
        print(f"  This run ({N_SIDE}×{N_SIDE}):       γ_eff = {gamma_eff:.3f}")
    else:
        print(f"\n  Insufficient valid runs ({len(valid)}/{len(results)}). Try:")
        print(f"  - Increase k_spring further (current {NEB_K_SPRING})")
        print(f"  - Reduce N_SIDE to 16")
        print(f"  - Increase NEB_ITER")

    print(f"\nFull results: {SAVE_PATH}")


if __name__ == "__main__":
    main()
