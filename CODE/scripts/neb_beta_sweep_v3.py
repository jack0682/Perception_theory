"""β-sweep v3 — fix endpoint convergence issue from diagnose_neb_collapse.py.

Critical finding from diagnostic (Part 3):
  find_formation(K=2 init) returns E=36.4, but extra gradient flow lowers to
  E=33.9. The K=2 endpoint was NOT deeply converged. NEB chain interior found
  better K=2 configurations (chain interior E < K=2 endpoint E).

v3 fixes:
  1. After find_formation, run additional projected gradient flow (deep_steps)
     until ‖grad‖ < 1e-4 (much tighter than find_formation default).
  2. Print endpoint E before/after deep convergence to verify improvement.
  3. Run NEB on the deeply-converged endpoints — chain should now find proper
     interior maximum (saddle).

Usage (from CODE/):
    PYTHONPATH=. python3 scripts/neb_beta_sweep_v3.py
"""

from __future__ import annotations

import time
import json
from pathlib import Path
import numpy as np

from scc import GraphState, ParameterRegistry, find_formation
from scc.energy import EnergyComputer
from scc.k_soft import k_soft

# ============================================================
# CONFIG
# ============================================================
N_SIDE = 16          # 16×16 = 256 sites (good speed/signal balance)
VOLUME_FRACTION = 0.25
BETAS = [10, 15, 20, 30, 50, 75, 100, 150]
N_IMAGES = 17
NEB_ITER = 3000
NEB_DT = 0.0005
NEB_K_SPRING = 50.0
NEB_TOL = 1e-2
MAX_FORCE_CLIP = 30.0
DEEP_STEPS = 20000     # extra gradient flow on endpoints
DEEP_DT = 0.0005
DEEP_TOL = 1e-5         # convergence tolerance for endpoint
SAVE_PATH = Path("logs/neb_v3_results.json")
DIAGNOSTIC_EVERY = 300
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


def deep_gradient_flow(u_init, ec, m, n_steps, dt, tol=1e-5, label=""):
    """Run pure projected gradient flow until convergence."""
    u = u_init.copy()
    e0 = ec.energy(u)[0]
    for step in range(n_steps):
        g = ec.gradient(u)
        g = project_to_tangent(g)
        gnorm = np.linalg.norm(g)
        if gnorm < tol:
            break
        u = u - dt * g
        u = project_to_simplex(u, m)
    e_final = ec.energy(u)[0]
    print(f"    {label}: E {e0:.4f} → {e_final:.4f} ({step+1} steps, |grad|={gnorm:.6f})", flush=True)
    return u


def find_minima_deep(graph, params, n_side, m, ec):
    print(f"  [Find K=1 with deep convergence]", flush=True)
    best_e_k1 = float("inf"); best_k1 = None
    for sig in [0.7, 1.0, 1.3, 1.6]:
        for cx in [n_side*0.3, n_side*0.5, n_side*0.7]:
            for cy in [n_side*0.3, n_side*0.5, n_side*0.7]:
                u0 = gauss_init(n_side, cx, cy, sig)
                u0 = u0 * (m / u0.sum())
                u0 = project_to_simplex(u0, m)
                u_min = find_formation(graph, params, u_init=u0).u
                e = ec.energy(u_min)[0]
                ks = k_soft(u_min, n_side)
                if ks < 0.7 and e < best_e_k1:
                    best_e_k1 = e; best_k1 = u_min
    # Deep flow on best K=1
    print(f"  [K=1 deep convergence]", flush=True)
    best_k1 = deep_gradient_flow(best_k1, ec, m, DEEP_STEPS, DEEP_DT, DEEP_TOL, "K=1")

    print(f"  [Find K=2 with deep convergence]", flush=True)
    best_e_k2 = float("inf"); best_k2 = None
    for sig in [0.7, 1.0, 1.3]:
        for (a, b), (c, d) in [
            ((n_side*0.25, n_side*0.25), (n_side*0.75, n_side*0.75)),
            ((n_side*0.25, n_side*0.75), (n_side*0.75, n_side*0.25)),
            ((1.5, n_side/2), (n_side-2.5, n_side/2)),
            ((n_side/2, 1.5), (n_side/2, n_side-2.5)),
            ((n_side*0.3, n_side*0.3), (n_side*0.7, n_side*0.7)),
        ]:
            u0 = gauss_init(n_side, a, b, sig) + gauss_init(n_side, c, d, sig)
            u0 = u0 * (m / u0.sum())
            u0 = project_to_simplex(u0, m)
            u_min = find_formation(graph, params, u_init=u0).u
            e = ec.energy(u_min)[0]
            ks = k_soft(u_min, n_side)
            if 0.8 < ks < 1.4 and e < best_e_k2:
                best_e_k2 = e; best_k2 = u_min
    print(f"  [K=2 deep convergence]", flush=True)
    best_k2 = deep_gradient_flow(best_k2, ec, m, DEEP_STEPS, DEEP_DT, DEEP_TOL, "K=2")

    e_k1_final = ec.energy(best_k1)[0]
    e_k2_final = ec.energy(best_k2)[0]
    return best_k1, e_k1_final, best_k2, e_k2_final


def smooth_chain(images, m):
    new = [images[0].copy()]
    for i in range(1, len(images) - 1):
        avg = 0.25 * images[i-1] + 0.5 * images[i] + 0.25 * images[i+1]
        avg = project_to_simplex(avg, m)
        new.append(avg)
    new.append(images[-1].copy())
    return new


def neb_relax(images, energy_fn, grad_fn, m, n_iter, k_spring, dt, tol, max_force_clip,
              diagnostic_every=300, verbose=True):
    images = [im.copy() for im in images]
    N = len(images)
    history = []

    for it in range(n_iter):
        Es = [energy_fn(im)[0] for im in images]
        grads = [grad_fn(im) for im in images]

        tangents = [None] * N
        for i in range(1, N - 1):
            E_p, E_c, E_n = Es[i-1], Es[i], Es[i+1]
            tau_plus = images[i+1] - images[i]
            tau_minus = images[i] - images[i-1]
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
        # Climbing image only when peak is truly above both endpoints
        is_real_peak = (
            ci_idx not in (0, N-1) and
            (Es[ci_idx] - Es[0]) > 0.5 and (Es[ci_idx] - Es[-1]) > 0.5
        )
        for i in range(1, N - 1):
            tau = tangents[i]
            grad_t = project_to_tangent(grads[i])
            grad_par = (grad_t @ tau) * tau

            if i == ci_idx and is_real_peak:
                F = -grad_t + 2 * grad_par
            else:
                F_perp = -grad_t + grad_par
                spring_mag = k_spring * (
                    np.linalg.norm(images[i+1] - images[i]) -
                    np.linalg.norm(images[i] - images[i-1])
                )
                F = F_perp + spring_mag * tau

            F_norm = np.linalg.norm(F)
            if F_norm > max_force_clip:
                F = F * (max_force_clip / F_norm)

            images[i] = images[i] + dt * F
            images[i] = project_to_simplex(images[i], m)
            max_force = max(max_force, F_norm)

        if it > 0 and it % 100 == 0:
            images = smooth_chain(images, m)

        if verbose and (it % diagnostic_every == 0 or it == n_iter - 1):
            ci_str = f"ci={ci_idx} (CI)" if is_real_peak else f"ci={ci_idx} (no peak)"
            print(f"  iter {it:5d}: {ci_str}, max_E={max(Es):.2f}, force={max_force:.2f}", flush=True)
            print(f"    profile: [{' '.join(f'{e:.1f}' for e in Es)}]", flush=True)
            print(f"    K_soft : [{' '.join(f'{k_soft(im, int(np.sqrt(im.size))):.2f}' for im in images)}]", flush=True)

        history.append({"iter": it, "max_E": max(Es), "max_force": max_force, "ci_idx": ci_idx})
        if max_force < tol:
            print(f"  Converged at iter {it} (force {max_force:.6f})", flush=True)
            break

    return images, history


def measure_one_beta(beta):
    n = N_SIDE * N_SIDE
    m = n / 4
    params = ParameterRegistry(
        beta_bd=beta, alpha_bd=1.0, w_cl=1.0, w_sep=1e-5, w_bd=1.0,
        volume_fraction=VOLUME_FRACTION,
    )
    graph = GraphState.grid_2d(N_SIDE, N_SIDE)
    ec = EnergyComputer(graph, params)

    t0 = time.time()
    print(f"\n=== β = {beta} (n_side={N_SIDE}, m={m}) ===", flush=True)
    k1, e1, k2, e2 = find_minima_deep(graph, params, N_SIDE, m, ec)
    if k1 is None or k2 is None:
        return {"beta": beta, "status": "no_minima"}
    print(f"  Final K=1: E = {e1:.4f}, K_soft = {k_soft(k1, N_SIDE):.4f}", flush=True)
    print(f"  Final K=2: E = {e2:.4f}, K_soft = {k_soft(k2, N_SIDE):.4f}", flush=True)
    print(f"  ΔE_minima = {e2 - e1:.4f}", flush=True)

    images = []
    for i in range(N_IMAGES):
        t = i / (N_IMAGES - 1)
        u_i = (1 - t) * k1 + t * k2
        u_i = project_to_simplex(u_i, m)
        images.append(u_i)

    init_Es = [ec.energy(im)[0] for im in images]
    print(f"  Linear-interp max E: {max(init_Es):.2f}", flush=True)
    print(f"  Initial profile: [{' '.join(f'{e:.0f}' for e in init_Es)}]", flush=True)

    print(f"  NEB: {N_IMAGES} images, k_spring={NEB_K_SPRING}, force_clip={MAX_FORCE_CLIP}", flush=True)
    images, history = neb_relax(
        images, lambda u: ec.energy(u), lambda u: ec.gradient(u), m,
        NEB_ITER, NEB_K_SPRING, NEB_DT, NEB_TOL, MAX_FORCE_CLIP,
        diagnostic_every=DIAGNOSTIC_EVERY, verbose=True,
    )

    Es = [ec.energy(im)[0] for im in images]
    saddle_idx = int(np.argmax(Es))
    e_saddle = Es[saddle_idx]
    higher_min = max(e1, e2)
    dE = e_saddle - higher_min
    elapsed = time.time() - t0

    if saddle_idx in (0, N_IMAGES - 1):
        status = "saddle_at_endpoint"
    elif dE < 0.05:
        status = "barrier_too_small"
    else:
        status = "ok"

    print(f"  → saddle: idx={saddle_idx}, E={e_saddle:.4f}, K_soft={k_soft(images[saddle_idx], N_SIDE):.4f}", flush=True)
    print(f"  → ΔE_barrier = {dE:.4f} (status: {status}, elapsed: {elapsed:.1f}s)", flush=True)

    return {
        "beta": beta, "status": status, "n_side": N_SIDE, "m": m,
        "e_k1": e1, "e_k2": e2, "e_saddle": e_saddle,
        "saddle_idx": saddle_idx, "saddle_ks": k_soft(images[saddle_idx], N_SIDE),
        "delta_E_barrier": dE,
        "energy_profile": Es,
        "k_soft_profile": [k_soft(im, N_SIDE) for im in images],
        "elapsed_sec": elapsed,
    }


def main():
    print("=" * 60)
    print(f"NEB β-sweep v3: {N_SIDE}×{N_SIDE}, deep endpoint convergence")
    print(f"  k_spring={NEB_K_SPRING}, n_images={N_IMAGES}, n_iter={NEB_ITER}")
    print(f"  deep_steps={DEEP_STEPS}, deep_tol={DEEP_TOL}")
    print("=" * 60)

    SAVE_PATH.parent.mkdir(parents=True, exist_ok=True)
    results = []
    for beta in BETAS:
        try:
            r = measure_one_beta(beta)
        except Exception as e:
            import traceback
            print(f"  β={beta} CRASHED: {e}", flush=True)
            traceback.print_exc()
            r = {"beta": beta, "status": "crashed", "error": str(e)}
        results.append(r)
        with open(SAVE_PATH, "w") as f:
            json.dump(results, f, indent=2, default=str)

    print()
    print("=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    print(f"{'β':>6} {'ΔE_barrier':>14} {'saddle_K':>10} {'idx':>5} {'status':>22}")
    valid = []
    for r in results:
        if r.get("status") == "ok":
            print(f"{r['beta']:>6} {r['delta_E_barrier']:>14.4f} {r['saddle_ks']:>10.4f} "
                  f"{r['saddle_idx']:>5} {r['status']:>22}")
            valid.append((r["beta"], r["delta_E_barrier"]))
        else:
            print(f"{r['beta']:>6} {'---':>14} {'---':>10} {'---':>5} {r.get('status', 'unk'):>22}")

    if len(valid) >= 4:
        bs = np.array([b for b, _ in valid])
        ds = np.array([d for _, d in valid])
        log_b = np.log(bs); log_d = np.log(ds)
        gamma_eff, log_c = np.polyfit(log_b, log_d, 1)
        c = np.exp(log_c)
        print()
        print(f"Power-law fit (n={len(valid)}): ΔE_barrier = {c:.4f} · β^{gamma_eff:.4f}")
        print(f"  → γ_eff = {gamma_eff:.3f}")
        residuals = log_d - (gamma_eff * log_b + log_c)
        rss = (residuals ** 2).sum()
        tss = ((log_d - log_d.mean()) ** 2).sum()
        r2 = 1 - rss / tss if tss > 0 else 0
        print(f"  R² = {r2:.4f}")
        print()
        print(f"Comparison:")
        print(f"  Modica-Mortola sharp: γ_eff = 0.5")
        print(f"  Bulk linear:          γ_eff = 1.0")
        print(f"  canonical exp38:      γ_eff ≈ 0.89")
        print(f"  Our v3 ({N_SIDE}×{N_SIDE}):    γ_eff = {gamma_eff:.3f}")
    print(f"\nFull results: {SAVE_PATH}")


if __name__ == "__main__":
    main()
