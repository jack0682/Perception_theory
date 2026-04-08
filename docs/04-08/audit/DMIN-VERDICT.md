# d_min Formula: Cat B Review Verdict

**Date:** 2026-04-08
**Session:** d_min Cat B review
**Category:** audit
**Status:** complete

---

## 1. Question

Can the d_min formula d* = 4.8 + 0.31√(β/α) - 0.018β/α be upgraded from Cat B to Cat A?

## 2. Answer

**The quantitative formula stays Cat B.** But two new results emerge:

### Already Cat A (confirmed)
- **d_min^SCC < d_min^AC** (qualitative ordering) — via T7-Enhanced + mass redistribution
- **Three-mechanism decomposition**: core saturation (60%), mass redistribution (30%), Hessian boost (10%)

### New Cat A (proved this session)
- **Exponential tail bound**: d ≥ (2/c₀_slow)·ln(3/u_sp) guarantees metastability
  - c₀_slow uses nonlinear screening correction (W''(u_sp), not W''(0))
  - Factor 3 absorbs super-additivity correction
  - Gershgorin argument closes the midpoint→full-Hessian gap trivially
  - **Valid but very loose** (predicts d ≥ 2.5, reality needs 5-7)

### Possible Cat A (requires proof work)
- **1D kink comparison bound**: d ≥ 2R + 4ε·arctanh(...)
  - Uses discrete maximum principle to bound 2D profile by 1D tanh kink
  - Would give d ≈ 3-4, within 50% of actual
  - Standard comparison argument but not yet written

## 3. Why the Quantitative Formula Can't Be Cat A

Three fundamental issues:
1. **1D decay model fails in 2D** — c₀_theory overestimates actual decay by 8-25× (verifier confirmed)
2. **Pre-asymptotic regime dominates** — at d ≈ 5-7, tail is in interface-to-exponential transition, not pure exponential
3. **Regression coefficients (4.8, 0.31, 0.018)** — capture three different physical regimes that aren't unified by a single analytical structure

## 4. Key Discoveries

### Verifier findings
- Closure dramatically sharpens tails: peak u goes 0.8-0.9 → 0.98-1.0
- Decay rate c₀ increases 2-10× with closure
- Strong finite-size effects: d_min grows with grid size
- c₀_fit/c₀_theory ratio 0.04-0.13 — NOT a 1D vs 2D issue (c₀ is already 2D), but pre-asymptotic regime effect

### Critical correction (from critic follow-up)
- c₀ = arccosh(1 + β/(4α)) IS the correct 2D lattice rate (derived from 2D Fourier transform)
- The 1/√r Bessel prefactor makes tails SHORTER, not longer (geometric spreading)
- The 8-25× discrepancy is from **pre-asymptotic interface profile** (tanh, not exponential at short distances)
- **The right fix: 1D kink comparison principle, NOT 2D Bessel analysis**

### Critic findings  
- **Super-additivity** (not sub-): nonlinear tail superposition OVERSHOOTS linear prediction
- **Gershgorin closes trivially**: Laplacian diagonal exactly cancels Gershgorin radius
- **Nonlinear screening**: effective κ² drops 54% at spinodal vs u=0
- 1D kink comparison is the best path to a tight Cat A bound

## 5. Updated Status

| Claim | Before | After |
|-------|--------|-------|
| d_min^SCC < d_min^AC | Cat A | **Cat A** (confirmed) |
| Three mechanisms | Cat A | **Cat A** (confirmed) |
| Exponential tail bound | — | **Cat A** (new, but loose) |
| 1D kink comparison | — | **Cat A target** (proof needed) |
| Regression formula | Cat B | **Cat B** (confirmed) |

## 6. Files

- `docs/04-08/audit/DMIN-CRITIQUE.md` — 6-issue critique
- `docs/04-08/audit/DMIN-VERDICT.md` — This verdict
- `docs/04-08/experiment/DMIN-VERIFICATION.md` — Numerical verification
- `docs/04-08/experiment/dmin_raw_data.json` — Raw profile data
