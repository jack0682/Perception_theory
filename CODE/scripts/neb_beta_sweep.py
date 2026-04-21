"""β-sweep for γ_eff measurement via NEB.

Measures ΔE_barrier(β) for K=1 ↔ K=2 transition at multiple β values,
fits log-log slope to extract effective exponent γ_eff.

Theoretical reference: canonical Cat B "γ_eff ≈ 0.89 (exp38)".
                       Round 6 §1 honest closure: γ_eff ∈ [0.5, 1.0],
                       protocol-dependent.
                       NQ-15 quantitative resolution attempt.

Run from CODE/: PYTHONPATH=. python3 scripts/neb_beta_sweep.py
"""

from __future__ import annotations

import numpy as np

from scc import GraphState, ParameterRegistry, find_formation
from scc.energy import EnergyComputer
from scc.k_soft import k_soft

from scripts.neb_k1k2 import (
    gauss_init,
    project_to_simplex,
    neb_relax,
)


def find_minima(graph: GraphState, params: ParameterRegistry, n_side: int, m: float):
    """Multi-init search for K=1 and K=2 globals."""
    ec = EnergyComputer(graph, params)

    # K=1
    best_e_k1 = float("inf"); best_k1 = None
    for sig in [0.7, 1.0, 1.3]:
        for cx in [3, 5.5, 8]:
            for cy in [3, 5.5, 8]:
                u0 = gauss_init(n_side, cx, cy, sig)
                u0 = u0 * (m / u0.sum())
                u0 = project_to_simplex(u0, m)
                u_min = find_formation(graph, params, u_init=u0).u
                e = ec.energy(u_min)[0]
                ks = k_soft(u_min, n_side)
                if ks < 0.7 and e < best_e_k1:
                    best_e_k1 = e; best_k1 = u_min

    # K=2
    best_e_k2 = float("inf"); best_k2 = None
    for sig in [0.7, 1.0]:
        for (a, b), (c, d) in [
            ((2, 2), (9, 9)), ((2, 9), (9, 2)),
            ((1, 5.5), (10, 5.5)), ((5.5, 1), (5.5, 10)),
            ((3, 3), (8, 8)),
        ]:
            u0 = gauss_init(n_side, a, b, sig) + gauss_init(n_side, c, d, sig)
            u0 = u0 * (m / u0.sum())
            u0 = project_to_simplex(u0, m)
            u_min = find_formation(graph, params, u_init=u0).u
            e = ec.energy(u_min)[0]
            ks = k_soft(u_min, n_side)
            if 0.8 < ks < 1.4 and e < best_e_k2:
                best_e_k2 = e; best_k2 = u_min

    return best_k1, best_e_k1, best_k2, best_e_k2


def measure_barrier(beta: float, n_side: int = 12, n_images: int = 11, n_iter: int = 300):
    """Measure ΔE_barrier at given β via NEB."""
    n = n_side * n_side
    m = n / 4
    params = ParameterRegistry(
        beta_bd=beta, alpha_bd=1.0, w_cl=1.0, w_sep=1e-5, w_bd=1.0,
        volume_fraction=0.25,
    )
    graph = GraphState.grid_2d(n_side, n_side)
    ec = EnergyComputer(graph, params)

    print(f"\n=== β = {beta} ===")
    best_k1, e_k1, best_k2, e_k2 = find_minima(graph, params, n_side, m)
    print(f"  K=1: E = {e_k1:.4f}, K_soft = {k_soft(best_k1, n_side):.4f}")
    print(f"  K=2: E = {e_k2:.4f}, K_soft = {k_soft(best_k2, n_side):.4f}")

    # NEB chain
    images = []
    for i in range(n_images):
        t = i / (n_images - 1)
        u_i = (1 - t) * best_k1 + t * best_k2
        u_i = project_to_simplex(u_i, m)
        images.append(u_i)

    # NEB run
    images = neb_relax(
        images,
        energy_fn=lambda u: ec.energy(u),
        grad_fn=lambda u: ec.gradient(u),
        m=m,
        n_iter=n_iter, k_spring=5.0, dt=0.0005, climbing=True, tol=1e-3, verbose=False,
    )

    Es = [ec.energy(im)[0] for im in images]
    saddle_idx = int(np.argmax(Es))
    e_saddle = Es[saddle_idx]
    higher_min = max(e_k1, e_k2)
    delta_E_barrier = e_saddle - higher_min
    saddle_ks = k_soft(images[saddle_idx], n_side)

    print(f"  NEB: saddle E = {e_saddle:.4f} (idx {saddle_idx}), K_soft = {saddle_ks:.4f}")
    print(f"  ΔE_barrier = {delta_E_barrier:.4f} (above higher min)")
    return delta_E_barrier


def main():
    betas = [10, 20, 30, 50, 75, 100]
    barriers = []
    for beta in betas:
        try:
            dE = measure_barrier(beta)
            barriers.append(dE)
        except Exception as e:
            print(f"  β={beta} FAILED: {e}")
            barriers.append(None)

    print()
    print("=== β-sweep summary ===")
    print(f"{'β':>6} {'ΔE_barrier':>14} {'log10(ΔE)':>12}")
    valid = [(b, d) for b, d in zip(betas, barriers) if d is not None and d > 0]
    for b, d in valid:
        print(f"{b:>6} {d:>14.4f} {np.log10(d):>12.4f}")

    if len(valid) >= 3:
        bs = np.array([b for b, d in valid])
        ds = np.array([d for b, d in valid])
        # Fit log(ΔE) = γ_eff · log(β) + const
        log_bs = np.log(bs)
        log_ds = np.log(ds)
        gamma_eff, log_c = np.polyfit(log_bs, log_ds, 1)
        c = np.exp(log_c)
        print()
        print(f"Power-law fit: ΔE_barrier = {c:.3f} · β^{gamma_eff:.3f}")
        print(f"  → γ_eff = {gamma_eff:.3f}")
        print()
        print(f"Comparison:")
        print(f"  Modica-Mortola sharp-interface limit:  γ_eff = 0.5")
        print(f"  Bulk linear limit:                      γ_eff = 1.0")
        print(f"  canonical exp38 (Cat B):                γ_eff ≈ 0.89")
        print(f"  Our measurement on 12×12 grid:          γ_eff = {gamma_eff:.3f}")
        if 0.5 <= gamma_eff <= 1.0:
            print(f"  → Within Round 6 predicted bound [0.5, 1.0] ✓")
        else:
            print(f"  ⚠ Outside Round 6 bound [0.5, 1.0]")

        # Diagnostic: protocol differences
        print()
        print("Note: γ_eff is protocol-dependent (Round 6 §1 honest closure).")
        print(f"  Our protocol: 12×12 grid, m={(12*12)/4}, c=0.25, NEB w/ {11} images.")
        print(f"  canonical exp38 protocol details unknown; direct comparison not strict.")


if __name__ == "__main__":
    main()
