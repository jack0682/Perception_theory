"""β-sweep v4 — scipy BFGS for endpoint convergence + adaptive NEB.

Critical finding from v3:
  β=10 worked (ΔE=0.31, saddle K_soft=0.996, idx=14 interior).
  β≥15 failed because endpoints not deeply converged (high β → steep gradient,
  pure gradient descent with fixed dt=0.0005 inadequate).
  At β=150, K=1 deep convergence finished with |grad|=100 (huge!) and even
  K=1 > K=2 anomaly (bad K=1 search).

v4 fixes:
  1. Use scipy.optimize.minimize (L-BFGS-B) for endpoint convergence.
     BFGS handles step size adaptively, converges where naive GD fails.
  2. Narrower β range — focus where physics is interesting (β=5..30).
  3. Print final |grad| for endpoints so user can validate.
  4. Adaptive NEB step size (already in v3).

Usage (from CODE/):
    PYTHONPATH=. python3 scripts/neb_beta_sweep_v4.py
"""

from __future__ import annotations

import time
import json
from pathlib import Path
import numpy as np
from scipy.optimize import minimize

from scc import GraphState, ParameterRegistry, find_formation
from scc.energy import EnergyComputer
from scc.k_soft import k_soft

# ============================================================
# CONFIG
# ============================================================
N_SIDE = 16
VOLUME_FRACTION = 0.25
# Narrower β range — focus on regime where convergence works
BETAS = [8, 10, 12, 15, 20, 25, 30, 40]
N_IMAGES = 17
NEB_ITER = 4000
NEB_DT = 0.0005
NEB_K_SPRING = 50.0
NEB_TOL = 5e-3
MAX_FORCE_CLIP = 30.0
SAVE_PATH = Path("logs/neb_v4_results.json")
DIAGNOSTIC_EVERY = 500
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


def deep_converge_bfgs(u_init, ec, m, n_side, max_iter=2000, tol=1e-5, label=""):
    """Use scipy L-BFGS-B with bound constraints + manual mass projection."""
    n = u_init.size

    # Wrapper: enforce volume constraint by reparametrization
    # u = u_proj, project to mass m and bounds [eps, 1-eps] before energy/grad eval
    eps = 0.001

    def obj_and_grad(u_raw):
        u_proj = project_to_simplex(u_raw, m, eps=eps)
        E = ec.energy(u_proj)[0]
        g = ec.gradient(u_proj)
        g = project_to_tangent(g)
        return E, g

    e0 = ec.energy(project_to_simplex(u_init, m, eps=eps))[0]

    # L-BFGS-B with bounds (much faster + more stable than naive GD)
    result = minimize(
        obj_and_grad, u_init, jac=True, method='L-BFGS-B',
        bounds=[(eps, 1 - eps)] * n,
        options={'maxiter': max_iter, 'gtol': tol, 'ftol': 1e-12, 'maxcor': 50}
    )
    u_final = project_to_simplex(result.x, m, eps=eps)
    e_final = ec.energy(u_final)[0]
    g_final_norm = np.linalg.norm(project_to_tangent(ec.gradient(u_final)))
    print(f"    {label} BFGS: E {e0:.4f} → {e_final:.4f}, |grad|={g_final_norm:.6f}, "
          f"converged={result.success}, K_soft={k_soft(u_final, n_side):.4f}", flush=True)
    return u_final, e_final, g_final_norm


def find_minima_bfgs(graph, params, n_side, m, ec):
    print(f"  [Find K=1 with BFGS]", flush=True)
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
    best_k1, e_k1, g1 = deep_converge_bfgs(best_k1, ec, m, n_side, max_iter=3000, label="K=1")

    print(f"  [Find K=2 with BFGS]", flush=True)
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
    if best_k2 is None:
        print(f"  [K=2 search FAILED — no init produced K_soft ∈ (0.8, 1.4)]", flush=True)
        return best_k1, e_k1, None, None, g1, None
    best_k2, e_k2, g2 = deep_converge_bfgs(best_k2, ec, m, n_side, max_iter=3000, label="K=2")
    # Verify K=2 still K=2 after deep convergence (didn't collapse)
    ks2_after = k_soft(best_k2, n_side)
    if ks2_after < 0.7:
        print(f"  [K=2 collapsed to K_soft={ks2_after:.3f} after BFGS — treating as no K=2 minimum]", flush=True)
        return best_k1, e_k1, None, None, g1, None
    return best_k1, e_k1, best_k2, e_k2, g1, g2


def smooth_chain(images, m):
    new = [images[0].copy()]
    for i in range(1, len(images) - 1):
        avg = 0.25 * images[i-1] + 0.5 * images[i] + 0.25 * images[i+1]
        avg = project_to_simplex(avg, m)
        new.append(avg)
    new.append(images[-1].copy())
    return new


def neb_relax(images, energy_fn, grad_fn, m, n_iter, k_spring, dt_init, tol, max_force_clip,
              n_side, diagnostic_every=500, verbose=True):
    images = [im.copy() for im in images]
    N = len(images)
    dt = dt_init
    prev_max_E = None

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

        max_E = max(Es)
        if prev_max_E is not None:
            if max_E > prev_max_E + 1e-3:
                dt = max(dt * 0.7, 1e-5)
            elif max_E < prev_max_E - 1e-3:
                dt = min(dt * 1.05, dt_init)
        prev_max_E = max_E

        if it > 0 and it % 100 == 0:
            images = smooth_chain(images, m)

        if verbose and (it % diagnostic_every == 0 or it == n_iter - 1):
            ci_str = f"ci={ci_idx} (CI)" if is_real_peak else f"ci={ci_idx} (no peak)"
            print(f"  iter {it:5d}: {ci_str}, max_E={max_E:.2f}, force={max_force:.2f}, dt={dt:.5f}", flush=True)
            print(f"    profile: [{' '.join(f'{e:.1f}' for e in Es)}]", flush=True)
            print(f"    K_soft : [{' '.join(f'{k_soft(im, n_side):.2f}' for im in images)}]", flush=True)

        if max_force < tol:
            print(f"  Converged at iter {it} (force {max_force:.6f})", flush=True)
            break

    return images


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
    k1, e1, k2, e2, g1, g2 = find_minima_bfgs(graph, params, N_SIDE, m, ec)
    if k1 is None:
        return {"beta": beta, "status": "no_K1_minimum"}
    if k2 is None:
        print(f"  → No K=2 metastable minimum at β={beta} (canonical CN8 / T-Merge (a) regime not reached)", flush=True)
        return {"beta": beta, "status": "no_K2_metastable", "e_k1": e1, "g1": g1}
    print(f"  Endpoints converged. K=1: E={e1:.4f}, |grad|={g1:.5f}; K=2: E={e2:.4f}, |grad|={g2:.5f}", flush=True)
    print(f"  K_soft: K=1={k_soft(k1, N_SIDE):.4f}, K=2={k_soft(k2, N_SIDE):.4f}", flush=True)
    print(f"  ΔE_minima = {e2 - e1:.4f}", flush=True)

    images = []
    for i in range(N_IMAGES):
        t = i / (N_IMAGES - 1)
        u_i = (1 - t) * k1 + t * k2
        u_i = project_to_simplex(u_i, m)
        images.append(u_i)

    init_Es = [ec.energy(im)[0] for im in images]
    print(f"  Linear-interp max E: {max(init_Es):.2f}", flush=True)

    print(f"  NEB: {N_IMAGES} images, k_spring={NEB_K_SPRING}, force_clip={MAX_FORCE_CLIP}", flush=True)
    images = neb_relax(
        images, lambda u: ec.energy(u), lambda u: ec.gradient(u), m,
        NEB_ITER, NEB_K_SPRING, NEB_DT, NEB_TOL, MAX_FORCE_CLIP, N_SIDE,
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
        "e_k1": e1, "e_k2": e2, "e_saddle": e_saddle, "g1": g1, "g2": g2,
        "saddle_idx": saddle_idx, "saddle_ks": k_soft(images[saddle_idx], N_SIDE),
        "delta_E_barrier": dE,
        "energy_profile": Es,
        "k_soft_profile": [k_soft(im, N_SIDE) for im in images],
        "elapsed_sec": elapsed,
    }


def main():
    print("=" * 60)
    print(f"NEB β-sweep v4: {N_SIDE}×{N_SIDE} with BFGS endpoints")
    print(f"  βs: {BETAS}")
    print(f"  k_spring={NEB_K_SPRING}, n_images={N_IMAGES}, n_iter={NEB_ITER}")
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
    print(f"{'β':>6} {'ΔE_barrier':>14} {'saddle_K':>10} {'idx':>5} {'g1':>10} {'g2':>10} {'status':>22}")
    valid = []
    for r in results:
        if r.get("status") == "ok":
            print(f"{r['beta']:>6} {r['delta_E_barrier']:>14.4f} {r['saddle_ks']:>10.4f} "
                  f"{r['saddle_idx']:>5} {r.get('g1', 0):>10.5f} {r.get('g2', 0):>10.5f} {r['status']:>22}")
            valid.append((r["beta"], r["delta_E_barrier"]))
        else:
            g1v = r.get('g1', 0) if r.get('g1') is not None else 0
            g2v = r.get('g2', 0) if r.get('g2') is not None else 0
            print(f"{r['beta']:>6} {'---':>14} {'---':>10} {'---':>5} "
                  f"{g1v:>10.5f} {g2v:>10.5f} {r.get('status', 'unk'):>22}")

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
        print(f"  Residuals: {residuals}")
        print()
        print(f"Comparison:")
        print(f"  Modica-Mortola sharp:   γ_eff = 0.5")
        print(f"  Bulk linear:            γ_eff = 1.0")
        print(f"  canonical exp38:        γ_eff ≈ 0.89")
        print(f"  Round 6 envelope:       γ_eff ∈ [0.5, 1.0]")
        print(f"  Our v4 ({N_SIDE}×{N_SIDE}):       γ_eff = {gamma_eff:.3f}")
    else:
        print(f"\n  Insufficient valid runs ({len(valid)}/{len(results)})")

    print(f"\nFull results: {SAVE_PATH}")


if __name__ == "__main__":
    main()
