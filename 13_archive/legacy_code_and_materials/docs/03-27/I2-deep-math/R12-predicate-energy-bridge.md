# Predicate-Energy Bridge — Computation Results

**Author:** Computation Analyst
**Date:** 2026-03-27
**Iteration:** 2, Round 12

---

## BRIDGE THEOREM

For volume-constrained minimizer û with formation set F:

1. **Bind(û) ≥ 1 - √(E_cl/|F|)** — verified on all 15 (β,m) pairs
2. **Sep(û) ≥ 1 - E_sep/(u_min_F · |F|)** — nearly tight at high β
3. **Inside ~ 1 - O(√δ) where δ = DW(û)/n** — structural relationship

## KEY FINDING

E_total INCREASES with β (larger double-well coefficient) but ProtoCoh ALSO increases. The bridge works because E_cl and E_sep DECREASE with β even as E_bd increases.

## PERTURBATION SENSITIVITY

Blurring boundary of β=10 formation:
- Blur 0.0: ProtoCoh = 0.837
- Blur 0.2: ProtoCoh = 0.630
- Blur 0.8: ProtoCoh = 0.355

Inside (TransitionSharpness) is most sensitive to boundary degradation.

## REVERSE DIRECTION: FAILS

High ProtoCoh does NOT imply low E. The bridge is ONE-DIRECTIONAL:
- Low E_cl, E_sep → high Bind, Sep ✓
- High Bind, Sep → low E (NOT guaranteed)
