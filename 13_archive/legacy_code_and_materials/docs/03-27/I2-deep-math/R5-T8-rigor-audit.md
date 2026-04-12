# T8 Non-Trivial Minimizer Existence — Rigor Auditor Complete Audit

**Author:** Rigor Auditor
**Date:** 2026-03-27
**Iteration:** 2, Round 5

---

## Audit Verdicts

| Claim | Verdict |
|-------|---------|
| Non-uniform minimizer exists on Σ_m | **VALID** ✓ |
| Second variation argument | **VALID** ✓ (modulo convention) |
| Eigenvalue perturbation for Cl/Sep | **VALID** for saddle preservation; **INVALID** for minimizer structure |
| Γ-convergence → formation structure | **OVERSTATEMENT** — proves binary limits, not finite-parameter quality |
| Q_morph_v2 makes Inside well-formed | **VALID** but provisional; doesn't fix threshold-discontinuity |
| L² Bind fix | **PARTIALLY LEGITIMATE** — defensible with cohesion-weighting but is a weakening |
| Critical ratio = 4λ₂/|W''(c)| | **DISPUTED** — derivation gives 2λ₂/|W''(c)| under Canonical Spec conventions |

## Critical Ratio Factor Dispute

Using Canonical Spec convention (Σ_{x,y} over ordered pairs):
- E_smooth = α · Σ_{x,y} N_t(x,y)(u(x)-u(y))² = 2α · u^T L u
- Second variation: 2α⟨v, Lv⟩ + βW''(c)‖v‖²
- At Fiedler: 2αλ₂ + βW''(c) < 0
- Critical ratio: β/α > **2λ₂/|W''(c)|**, NOT 4λ₂

The factor of 4 in the Proof Strategist's claim appears to come from writing ∇²E_smooth = 4αL, which would require E_smooth = 2α·u^T Lu having Hessian 4αL. But the Hessian of 2α·u^T Lu is 2·2α·L = 4αL. Actually this IS correct: d²/du² of u^T Au = 2A, so d²/du² of 2α·u^T Lu = 4αL. So the second variation IS 4αλ₂ + βW''(c), giving critical ratio 4λ₂/|W''(c)|.

**CORRECTION: The Proof Strategist IS correct.** My initial derivation was wrong — I was computing the first-order variation ⟨∇E, v⟩ = 2α⟨Lv, u⟩ rather than the second variation ⟨v, ∇²E·v⟩ = 4α⟨v, Lv⟩. The factor of 4 comes from the Hessian of a quadratic form u^T(2αL)u being 2·(2αL) = 4αL.

**Final verdict on critical ratio: 4λ₂/|W''(c)| is CORRECT.**

## Key Gaps Identified

1. **Γ-convergence at finite parameters** — binary limits don't imply formation structure at practical β/α
2. **Predicate-energy bridge** — THE blocking problem. Non-trivial minimizers exist but may not satisfy proto-cohesion
3. **L² Bind is a weakening** — should use cohesion-weighted norm for honesty
4. **Q_morph_v2 is provisional** — doesn't fix threshold-discontinuity in Core/Bd terms of Inside

## Overall T8 Status

**PROVED (weak form):** Non-trivial constrained minimizer exists when β/α > 4λ₂/|W''(c)|.

**NOT PROVED (strong form):** Minimizer has formation structure satisfying proto-cohesion.

The gap between these is the predicate-energy bridge.
