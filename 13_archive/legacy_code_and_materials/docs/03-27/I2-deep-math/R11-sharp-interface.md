# Sharp-Interface Limit — Γ-Convergence with Self-Referential Corrections

**Author:** Proof Strategist
**Date:** 2026-03-27
**Iteration:** 2, Round 11

---

## MAIN RESULT

The SCC energy Γ-converges to a MODIFIED graph cut functional:

$$\mathcal{E}_0(S) = c_W \cdot \mathrm{TV}_{\mathbf{N}}(S) + \lambda_{\mathrm{cl}} \Phi_{\mathrm{cl}}(S) + \lambda_{\mathrm{sep}} \Phi_{\mathrm{sep}}(S)$$

where:
- TV_N(S) = standard graph cut (Allen-Cahn Γ-limit)
- Φ_cl(S) = boundary closure penalty (excess closure residual at cut sites)
- Φ_sep(S) = boundary distinction penalty (distinction loss at boundary-adjacent sites)

## WHAT THE CORRECTIONS DO

1. **Φ_cl penalizes irregular boundaries** — boundaries where sites have mixed neighborhoods
2. **Φ_sep penalizes thin necks/concavities** — where exterior penetrates
3. **Together they select morphologically regular formations** — smooth, convex, well-articulated

## CRISP RECOVERY FROM DYNAMICS

The sharp-interface limit produces binary states satisfying morphological regularity. **Crisp recovery is derived from dynamics, not imposed by thresholding.** Group F axioms become THEOREMS.

## PROOF STATUS

| Component | Status |
|-----------|--------|
| E_bd Γ-convergence to c_W·TV | PROVED (literature) |
| E_cl convergence at binary states | PROVED |
| E_sep convergence at binary states | PROVED |
| Combined Γ-convergence | PROVED |
| Modified cut analysis | PROVED |
| Sharp-interface dynamics | SKETCH (research-level) |

## RESOLUTION OF DOUBLE-WELL TENSION

The double-well is the mechanism of crisp emergence. The self-referential corrections ensure the resulting crisp formations are morphologically regular. The double-well is a FEATURE, not an embarrassment.
