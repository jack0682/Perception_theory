"""
NQ-187b: Direct discrete-grid computation of A_2/A_1 ratio on D_4 free-BC grid,
extrapolated to L → ∞.

Reconciliation path (α) for T-σ-Theorem-4 finite-L finding (3-way A_2/A_1
discrepancy: 2/3 vs 4 vs 8). See:
- working/SF/nq187b_L_extrapolation.md (post-EOD op-0008-architect, §6.1 spec)
- working/SF/sigma_theorem4_canonical_revision.md (Task #63 reconciliation triple)
- logs/daily/2026-05-01/03_t_sigma_theorem4_reconciliation.md (γ/β/α handoff)

Eigenmodes (naive convention C1, no L²-normalization):
    phi_(p,q)(i,j) = cos(p*pi*(i+1/2)/L) * cos(q*pi*(j+1/2)/L)
    for i,j in {0,...,L-1}

Cubic-equivariant integrals on L x L free-BC grid:
    A_1^L = sum_{i,j} phi_(1,0)(i,j)^4 = L * sum_i cos^4((i+1/2)*pi/L)
    A_2^L = sum_{i,j} phi_(1,0)(i,j)^2 * phi_(0,1)(i,j)^2
          = (sum_i cos^2((i+1/2)*pi/L))^2

Continuum limit (per §2.5 closed-form):
    A_1^cont -> 3*L^2/8,  A_2^cont -> L^2/4 ⇒ A_2/A_1 -> 2/3.

Extrapolation: r(L) = a + b/L^2 ⇒ a is L→∞ value.

Produced as Day 5 supplementary work (W5 Day 5 EOD 2026-05-01) to provide
W6 D1 α-path numerical anchor pre-computed.
"""

from __future__ import annotations

import json
import os
from typing import Dict, List, Tuple

import numpy as np


def phi_pq(p: int, q: int, L: int) -> np.ndarray:
    """Discrete eigenmode phi_(p,q) on L x L free-BC grid (naive convention C1)."""
    i = np.arange(L).reshape(-1, 1)
    j = np.arange(L).reshape(1, -1)
    return np.cos(p * np.pi * (i + 0.5) / L) * np.cos(q * np.pi * (j + 0.5) / L)


def A1(L: int) -> float:
    """A_1 = sum phi_(1,0)^4 on L x L grid."""
    phi = phi_pq(1, 0, L)
    return float(np.sum(phi ** 4))


def A2(L: int) -> float:
    """A_2 = sum phi_(1,0)^2 * phi_(0,1)^2 on L x L grid."""
    phi_h = phi_pq(1, 0, L)
    phi_v = phi_pq(0, 1, L)
    return float(np.sum(phi_h ** 2 * phi_v ** 2))


def ratio(L: int) -> Tuple[float, float, float]:
    """Return (A_1^L, A_2^L, A_2/A_1)."""
    a1 = A1(L)
    a2 = A2(L)
    return a1, a2, a2 / a1


def extrapolate_to_infinity(
    L_values: List[int], ratios: List[float]
) -> Tuple[float, float, float]:
    """Linear fit r(L) = a + b/L^2; return (a, b, residual_l2)."""
    x = 1.0 / np.array(L_values, dtype=float) ** 2
    y = np.array(ratios, dtype=float)
    A = np.vstack([np.ones_like(x), x]).T
    sol, residuals, rank, sv = np.linalg.lstsq(A, y, rcond=None)
    a, b = float(sol[0]), float(sol[1])
    pred = a + b * x
    res_l2 = float(np.linalg.norm(y - pred))
    return a, b, res_l2


def main(out_dir: str = None) -> Dict:
    L_values = [4, 8, 16, 32, 64, 128]
    rows = []
    ratios_only = []

    print("NQ-187b: discrete-grid A_2/A_1 evaluation")
    print(f"Convention: C1 (naive, no L^2-normalization)")
    print(f"L scan: {L_values}")
    print()
    print(f"{'L':>5} | {'A_1^L':>14} | {'A_2^L':>14} | {'A_2/A_1':>10}")
    print("-" * 55)

    for L in L_values:
        a1, a2, r = ratio(L)
        rows.append({"L": L, "A1": a1, "A2": a2, "A2_over_A1": r})
        ratios_only.append(r)
        print(f"{L:>5} | {a1:>14.4f} | {a2:>14.4f} | {r:>10.6f}")

    a, b, res = extrapolate_to_infinity(L_values, ratios_only)
    print()
    print(f"Extrapolation r(L) = a + b/L^2 (linear fit on 1/L^2):")
    print(f"  a (L=infty) = {a:.6f}")
    print(f"  b (slope)   = {b:.6f}")
    print(f"  residual L2 = {res:.2e}")
    print()
    print("Reference predictions (per nq187b_L_extrapolation.md §3):")
    print(f"  Naive C1 continuum  (2/3) = {2.0 / 3.0:.6f}")
    print(f"  R22 working file claim     = 4.000000")
    print(f"  Numerical implied (eff)    = 8.000000")
    print()
    print(f"VERDICT (this run): naive convention C1 closed-form extrapolation a = {a:.6f}")
    print(f"vs continuum target 2/3 = {2.0 / 3.0:.6f}")
    diff = abs(a - 2.0 / 3.0)
    if diff < 1e-3:
        print(f"  → matches 2/3 within {diff:.2e} (Cat A elementary trigonometric algebra confirms naive convention).")
    else:
        print(f"  → deviation {diff:.6f} from 2/3; investigate fit / convention.")

    out = {
        "spec": {
            "task": "NQ-187b",
            "purpose": (
                "Direct discrete-grid A_2/A_1 evaluation on D_4 free-BC L x L grid; "
                "alpha-path reconciliation input for T-σ-Theorem-4 3-way A_2/A_1 "
                "discrepancy (2/3 vs 4 vs 8)."
            ),
            "convention": "C1 naive (no L^2-normalization)",
            "eigenmodes": "phi_(p,q)(i,j) = cos(p*pi*(i+1/2)/L) * cos(q*pi*(j+1/2)/L)",
        },
        "L_values": L_values,
        "rows": rows,
        "extrapolation_1_over_L_squared": {
            "a_L_infty": a,
            "b_slope": b,
            "residual_l2": res,
        },
        "reference_predictions": {
            "naive_C1_continuum": 2.0 / 3.0,
            "R22_working_file_claim": 4.0,
            "numerical_implied_effective": 8.0,
        },
    }

    if out_dir is None:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "nq187b_a2_a1_extrapolation.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"Saved: {out_path}")

    return out


if __name__ == "__main__":
    main()
