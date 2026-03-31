# Iteration 6 R1 — Consistency Verification: Summation Convention

**Author:** Consistency Verifier | **Date:** 2026-03-27

## CONFIRMED

- Ordered-pair convention: Σ_{x,y} N(x,y)(u(x)-u(y))² = 2α·uᵀLu ✓
- Hessian: 4αL ✓
- Critical ratio: 4λ₂/|W''(c)| ✓ (R13 correction was correct)

## ⚠️ ERROR FOUND: I3 Gradient Formula Missing Factor of 2

**I3 writes:** ∇E_bd = 4α·Lu + β·u(1-u)(1-2u)

**Correct:** ∇E_bd = 4α·Lu + **2**β·u(1-u)(1-2u)

W(u) = u²(1-u)², W'(u) = **2**u(1-u)(1-2u). The factor of 2 was dropped.

**Impact:** T8-Core and T14 theorems SAFE. But I3 implementation would compute half-strength double-well force → more diffuse formations than intended.

**Fix:** Add factor of 2 to double-well gradient in Canonical Spec v2.0 and flag for I8 implementation correction.
