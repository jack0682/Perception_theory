"""Diagnostic: why does NEB chain collapse below K=2 endpoint energy?

Two key checks:
  (A) NEB chain K_soft profile — do interior images stay at K_soft ≈ 1.5
      (proper transition state) or collapse to K_soft ≈ 0.5 (K=1 basin)?
  (B) K=2 Hessian eigenvalue check — is K=2 truly a local minimum
      (all eigenvalues positive) or actually a saddle (one negative)?

If (A) shows K_soft collapses to ~0.5: NEB chain pulled into K=1 basin
  → fix: use K_soft-controlled init or even stronger spring
If (B) shows K=2 Hessian has negative eigenvalue: K=2 is not a local min
  → canonical T-Merge (b) interpretation requires re-examination

Usage (from CODE/):
    PYTHONPATH=. python3 scripts/diagnose_neb_collapse.py
"""

from __future__ import annotations

import json
import numpy as np
from pathlib import Path

from scc import GraphState, ParameterRegistry, find_formation
from scc.energy import EnergyComputer
from scc.k_soft import k_soft

# Use small grid for Hessian feasibility (12×12 = 144 sites, Hessian = 144² = 20k entries)
N_SIDE = 12
BETA_TEST = 30

# ============================================================
# Part 1 — Re-examine NEB chain (load from saved JSON)
# ============================================================

def part1_examine_chain(json_path):
    print("=" * 60)
    print("PART 1 — Examine NEB chain K_soft profile (from saved results)")
    print("=" * 60)
    if not Path(json_path).exists():
        print(f"  No saved results at {json_path}")
        return
    with open(json_path) as f:
        results = json.load(f)
    for r in results:
        if r.get("status") in ("crashed", "no_minima"):
            continue
        print(f"\nβ = {r['beta']}:")
        Es = r.get("energy_profile", [])
        Ks = r.get("k_soft_profile", [])
        print(f"  K_soft chain profile (image idx → K_soft):")
        for i, (E, K) in enumerate(zip(Es, Ks)):
            marker = ""
            if i == 0: marker = " ← K=1 endpoint (fixed)"
            elif i == len(Es) - 1: marker = " ← K=2 endpoint (fixed)"
            elif K > 0.85: marker = "  K=2-like"
            elif K < 0.65: marker = "  K=1-like (COLLAPSE!)"
            else: marker = "  intermediate"
            print(f"    img {i:2d}: E = {E:7.2f}, K_soft = {K:.4f}{marker}")
        # Diagnosis
        n_interior_collapsed = sum(1 for K in Ks[1:-1] if K < 0.65)
        n_interior_total = len(Ks) - 2
        print(f"  Interior images collapsed to K=1: {n_interior_collapsed}/{n_interior_total}")
        if n_interior_collapsed > n_interior_total // 2:
            print(f"  → DIAGNOSIS: NEB chain partially collapsed (k_spring insufficient)")


# ============================================================
# Part 2 — Hessian at K=2 minimum — local min or saddle?
# ============================================================

def part2_hessian_at_k2(n_side=N_SIDE, beta=BETA_TEST):
    print()
    print("=" * 60)
    print(f"PART 2 — Hessian at K=2 minimum (n_side={n_side}, β={beta})")
    print("=" * 60)
    n = n_side * n_side
    m = n / 4
    params = ParameterRegistry(
        beta_bd=beta, alpha_bd=1.0, w_cl=1.0, w_sep=1e-5, w_bd=1.0,
        volume_fraction=0.25,
    )
    graph = GraphState.grid_2d(n_side, n_side)
    ec = EnergyComputer(graph, params)

    # Find K=1 and K=2 (multi-init)
    print("  Finding K=1...")
    xs, ys = np.meshgrid(np.arange(n_side), np.arange(n_side))
    def gauss(cx, cy, sigma):
        return np.exp(-((xs - cx) ** 2 + (ys - cy) ** 2) / (2 * sigma ** 2)).flatten()
    def normalize(u):
        u = u * (m / u.sum())
        u = np.clip(u, 0.001, 0.999)
        u = u * (m / u.sum())
        return u

    best_e_k1 = float("inf"); best_k1 = None
    for sig in [0.7, 1.0, 1.3, 1.6]:
        for cx in [3, 5.5, 8]:
            for cy in [3, 5.5, 8]:
                u_min = find_formation(graph, params, u_init=normalize(gauss(cx, cy, sig))).u
                e = ec.energy(u_min)[0]
                ks = k_soft(u_min, n_side)
                if ks < 0.7 and e < best_e_k1:
                    best_e_k1 = e; best_k1 = u_min

    best_e_k2 = float("inf"); best_k2 = None
    print("  Finding K=2...")
    for sig in [0.7, 1.0, 1.3]:
        for (a, b), (c, d) in [
            ((2, 2), (9, 9)), ((2, 9), (9, 2)),
            ((1.5, 5.5), (10.5, 5.5)), ((5.5, 1.5), (5.5, 10.5)),
            ((3, 3), (8, 8)),
        ]:
            u_min = find_formation(graph, params, u_init=normalize(gauss(a, b, sig) + gauss(c, d, sig))).u
            e = ec.energy(u_min)[0]
            ks = k_soft(u_min, n_side)
            if 0.8 < ks < 1.4 and e < best_e_k2:
                best_e_k2 = e; best_k2 = u_min

    print(f"  K=1: E = {best_e_k1:.4f}, K_soft = {k_soft(best_k1, n_side):.4f}")
    print(f"  K=2: E = {best_e_k2:.4f}, K_soft = {k_soft(best_k2, n_side):.4f}")

    # Compute Hessian at K=2 via finite differences (only diagonal-heavy + sparse off-diag)
    # For 144 sites: 144² = 20736 FD evaluations × 2 = 40k. Each takes ~ms. Total ~1min.
    print(f"  Computing Hessian at K=2 (n²={n*n} entries, ~1-2 min)...")
    h = 5e-5
    H = np.zeros((n, n))
    E_k2_total, _ = ec.energy(best_k2)
    for i in range(n):
        if i % 24 == 0:
            print(f"    row {i}/{n}", flush=True)
        for j in range(i, n):
            if i == j:
                up = best_k2.copy(); up[i] += h
                um = best_k2.copy(); um[i] -= h
                E_p, _ = ec.energy(up)
                E_m, _ = ec.energy(um)
                H[i, i] = (E_p - 2 * E_k2_total + E_m) / (h * h)
            else:
                u_pp = best_k2.copy(); u_pp[i] += h; u_pp[j] += h
                u_pm = best_k2.copy(); u_pm[i] += h; u_pm[j] -= h
                u_mp = best_k2.copy(); u_mp[i] -= h; u_mp[j] += h
                u_mm = best_k2.copy(); u_mm[i] -= h; u_mm[j] -= h
                E_pp, _ = ec.energy(u_pp)
                E_pm, _ = ec.energy(u_pm)
                E_mp, _ = ec.energy(u_mp)
                E_mm, _ = ec.energy(u_mm)
                H[i, j] = (E_pp - E_pm - E_mp + E_mm) / (4 * h * h)
                H[j, i] = H[i, j]

    # Project onto 1^perp (constrained tangent space)
    P = np.eye(n) - np.ones((n, n)) / n
    H_constr = P @ H @ P
    eigvals = np.sort(np.linalg.eigvalsh(H_constr))

    print(f"  ===  Hessian eigenvalues (constrained, sorted)  ===")
    print(f"  Bottom 10: {[f'{x:.4f}' for x in eigvals[:10]]}")
    print(f"  Top 5:     {[f'{x:.4f}' for x in eigvals[-5:]]}")
    n_negative = int(np.sum(eigvals < -1e-3))
    n_zero = int(np.sum(np.abs(eigvals) < 1e-3))
    n_positive = int(np.sum(eigvals > 1e-3))
    print(f"  Eigenvalue counts: {n_negative} negative, {n_zero} zero (incl. constraint), {n_positive} positive")
    print()
    if n_negative > 0:
        print(f"  ⚠ DIAGNOSIS: K=2 has {n_negative} NEGATIVE eigenvalue(s) → SADDLE, NOT local min!")
        print(f"    canonical T-Merge (a) (K=2 local min) FAILS at this scale.")
        print(f"    NEB chain collapse explained: K=2 endpoint is a saddle, ∇ℰ has unstable direction.")
    elif n_zero > 1:
        print(f"  ⚠ DIAGNOSIS: K=2 has {n_zero - 1} zero eigenvalue(s) (excl. constraint) → DEGENERATE/Morse-Bott!")
    else:
        print(f"  ✓ K=2 is a true local minimum (all non-trivial eigenvalues positive).")
        print(f"    → NEB collapse must be due to chain detachment, not K=2 instability.")
    return best_k1, best_k2, H_constr, eigvals


# ============================================================
# Part 3 — Direct gradient flow from K=2 (does it stay or fall?)
# ============================================================

def part3_gradient_flow_from_k2(best_k2, n_side, beta, n_steps=5000, dt=0.001):
    print()
    print("=" * 60)
    print(f"PART 3 — Gradient flow from K=2 (does it stay or migrate?)")
    print("=" * 60)
    n = n_side * n_side
    m = n / 4
    params = ParameterRegistry(
        beta_bd=beta, alpha_bd=1.0, w_cl=1.0, w_sep=1e-5, w_bd=1.0,
        volume_fraction=0.25,
    )
    graph = GraphState.grid_2d(n_side, n_side)
    ec = EnergyComputer(graph, params)

    u = best_k2.copy()
    print(f"  Initial K=2: E = {ec.energy(u)[0]:.4f}, K_soft = {k_soft(u, n_side):.4f}")
    print(f"  Running pure gradient flow ({n_steps} steps, dt={dt})...")

    for step in range(n_steps):
        g = ec.gradient(u)
        g = g - g.mean()  # project to tangent space
        u = u - dt * g
        u = np.clip(u, 0.001, 0.999)
        # Re-project to mass m
        u = u * (m / u.sum())
        u = np.clip(u, 0.001, 0.999)
        u = u * (m / u.sum())
        if step % 500 == 0:
            print(f"    step {step:5d}: E = {ec.energy(u)[0]:.4f}, K_soft = {k_soft(u, n_side):.4f}")
    print(f"  Final: E = {ec.energy(u)[0]:.4f}, K_soft = {k_soft(u, n_side):.4f}")
    K_final = k_soft(u, n_side)
    if K_final < 0.7:
        print(f"  → DIAGNOSIS: K=2 migrated to K=1 under pure gradient flow!")
        print(f"    K=2 was NOT a true local minimum. It's a saddle or shallow basin.")
    elif K_final > 0.8:
        print(f"  → K=2 stayed near K=2 (true local min, but maybe slightly shifted).")
    else:
        print(f"  → K=2 partially migrated (intermediate state).")
    return u


def main():
    # Part 1: examine NEB chain from saved JSON (assumes user ran neb_beta_sweep_v2)
    part1_examine_chain("logs/neb_v2_results.json")

    # Part 2: Hessian at K=2 (12×12, β=30)
    best_k1, best_k2, H, eigvals = part2_hessian_at_k2(n_side=12, beta=30)

    # Part 3: gradient flow from K=2
    final_u = part3_gradient_flow_from_k2(best_k2, n_side=12, beta=30)


if __name__ == "__main__":
    main()
