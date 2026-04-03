# Cross-Review and Integration Summary

**Date:** 2026-04-02 (completed 2026-04-03)
**Category:** synthesis
**Status:** complete
**Task:** #5 — Cross-review all proofs, identify gaps, synthesize

---

## 1. Proofs Reviewed

| # | Document | Author | Theorems | Status |
|---|----------|--------|----------|--------|
| 1 | FORMATION-BIRTH-THEOREM.md | proof-birth | T-Birth-Param, T-Birth-Topo, T-Birth-K2 | Complete |
| 2 | C3PP-PROOF.md | proof-c3pp | C3'' (resolvent monotonicity) | Complete |
| 3 | BARRIER-EXPONENT.md | proof-dmin | ΔE_merge scaling | Complete |
| 4 | DMIN-FORMULA.md | proof-dmin | d_min*(a_cl, β, α) | Complete |

---

## 2. Cross-Consistency Check

### 2.1. Shared Dependencies on Cat A Theorems

All four proofs depend on existing Category A results. Consistency verified:

| Cat A Theorem | Used By | Consistent? |
|---|---|---|
| T8-Core (β_crit = 4αλ₂/\|W''(c)\|) | Birth (Thm 1), Barrier (§3.1) | ✓ Same formula, same summation convention |
| T11 (Γ-convergence) | Birth (Thm 2), Barrier (§1.2, §4.4) | ✓ Both use Modica-Mortola correctly |
| T7-Enhanced (Gram boost) | d_min (§2.3, §4 Step 4) | ✓ Correctly invoked for Hessian stabilization |
| T3/T6-Stability (contraction) | d_min (§6.3) | ⚠ Applied at non-fixed-point (see §3.3) |
| T1 (minimizer existence) | Birth (Thm 2b) | ✓ |
| Coupling Bound Lemma | d_min (tail decay) | ✓ |

### 2.2. Cross-Proof Consistency

**Birth ↔ Barrier:** The Birth theorem (Thm 1) proves formation nucleation at β_crit via pitchfork bifurcation. The Barrier proof assumes the existence of K=2 and K=1 minimizers and studies the energy landscape between them. These are consistent: Birth establishes when non-trivial minimizers appear; Barrier studies the transition between different minimizer types once they exist. No overlap or contradiction.

**Birth ↔ d_min:** Birth Theorem 3 (K=2 threshold) requires β > 4αλ₃/|W''(c)| for two independent unstable modes. The d_min formula addresses a different question (metastability of two *existing* formations at finite distance). These are complementary: Birth gives the spectral condition for nucleation; d_min gives the spatial condition for coexistence. Consistent.

**C3'' ↔ all others:** The C3'' proof is self-contained (resolvent monotonicity). It does not interact with the other three proofs. The only connection is the code discrepancy noted in §7.3 (arithmetic vs geometric symmetrization), which is a code issue, not a theoretical one.

**Barrier ↔ d_min:** Both discuss merge barriers. The Barrier proof analyzes ΔE_merge(β) scaling along the linear interpolation path. The d_min proof analyzes the Hessian sign at the midpoint between formations. These address different aspects (barrier height vs instability onset) and are consistent. The Barrier proof's O(β) bulk term corresponds to the d_min proof's double-well mixing penalty at reorganization nodes.

### 2.3. Notation Consistency

All proofs use consistent notation:
- Ordered-pair summation (§0 convention) giving 4αL Hessian: ✓ in Birth, Barrier
- W(u) = u²(1−u)², W''(c) = 2(1−6c+6c²): ✓ in all
- β_crit = 4αλ₂/|W''(c)|: ✓ Birth, Barrier
- Σ_m volume constraint: ✓ in all

---

## 3. Gaps and Issues Identified

### 3.1. Category A (no issues)

| Theorem | Status | Notes |
|---|---|---|
| T-Birth-Param (pitchfork) | **Sound** | Simple eigenvalue hypothesis is generic; equivariant extension handles degenerate case. Supercriticality κ>0 from W''''=24>0. |
| T-Birth-Topo (Γ-convergence) | **Sound** | Elementary on finite-dim spaces. Volume-split optimality (ν₁=ν₂) correctly justified via envelope theorem. |
| T-Birth-K2 (threshold) | **Sound** | Direct Hessian eigenvalue count; necessary condition only. |
| C3'' (resolvent mono) | **Sound** | Elegant Schur complement + M-matrix argument. Key cancellation f'(s) = v^T G₀ v is rigorous. |
| ΔE_LI = Θ(β) | **Sound** | Follows from T11; sharp-interface limit is standard. |
| d_min^SCC ≤ d_min^AC | **Sound** | Qualitative, from T7-Enhanced positive-definiteness. |

### 3.2. Category B (minor issues)

| Claim | Issue | Severity |
|---|---|---|
| γ ≈ 0.89 effective exponent | Two-term model (Aβ+B√β with B>0) cannot produce γ_local > 1, but data shows γ_local = 1.45 at low β. Model incomplete at low β. | Medium — does not affect asymptotic claims |
| ΔE_saddle = Θ(√β) | Modica neck construction on discrete graphs needs discretization. Category B is correct. | Low — standard continuum argument, discretization expected to be routine |

### 3.3. Category C / Heuristic (significant issues)

| Claim | Issue | Severity |
|---|---|---|
| d_min quantitative formula | Single-site analysis gives 0.3% reduction vs 30% observed. "Collective Gram boost" scaling argument is dimensionally incorrect (eigenvalue shift ≠ sum of diagonal boosts). | **High** — the quantitative formula does not work |
| Interface sharpening mechanism | Plausible alternative for ~30% d_min reduction, but not formalized | Medium — needs investigation |
| T3/T6 at non-fixed-point | d_min §6.3 invokes contraction bound at exterior midpoint (not a closure fixed point) | Low — the Gram contribution is still positive; only the specific lower bound is technically invalid |
| κ² inconsistency in d_min | §2.1 uses κ²=β/(2α), §4 Step 1 uses κ²=β/α | Low — factor of 2, affects numerics not logic |

### 3.4. Code Issue

The C3'' proof (§7.3) identifies that `graph.py:cohesion_weighted_symmetric` uses arithmetic-mean symmetrization while the proof requires geometric-mean (D^{-1/2}). The proof is valid for D^{-1/2}; a separate proof or code change is needed to cover the arithmetic-mean form. **Recommended: align code to spec (one-line change), then run full test suite.**

---

## 4. Updated Theorem Registry

### New Category A (8 new theorems — updated after gap resolution)

| Name | Statement | Proof Method |
|---|---|---|
| **T-Birth-Param(a)** | Uniform state is saddle for β > β_crit; branches emerge | Second variation + Crandall-Rabinowitz |
| **T-Birth-Param(b) supercriticality** | κ > 0 on D₄-symmetric graphs; axial branches stable | D₄ equivariant branching lemma; W''''=24 > 0 |
| **T-Birth-Topo** | Γ-convergence as w→0; two-formation limit; IFT O(w) | Finite-dim Γ-convergence + IFT |
| **T-Birth-K2(a,b)** | Eigenvalue count for unstable directions | Hessian eigenvalue analysis |
| **T-Birth-K2(c)** | β > β_crit^(2) necessary for K=2 (Gap Condition) | Block-Kronecker + Weyl inequality |
| **C3'' (closed)** | Resolvent C(x,x) non-decreasing in u(x) | Schur complement + M-matrix + PD of G₀ |
| **ΔE_LI = Θ(β)** | Linear-interpolation barrier asymptotically linear in β | T11 Γ-convergence |
| **f₁^IFT bound** | f₁ ≤ κ_B²·n_bdy/n_F under BSR condition | BMD + IFT structure + boundary spectral ratio |

### New Category B (3 — updated)

| Name | Statement | Condition |
|---|---|---|
| **d_min^SCC < d_min^AC** | Closure reduces d_min via core saturation + mass redistribution | Qualitative proved; quantitative Cat B (exterior values numerical) |
| **γ_eff ≈ 0.89** | Effective barrier exponent in crossover regime | Empirical; β ∈ [20,100] |
| **TC'' tightened bound** | Transport displacement within 1-10× of actual | Three mechanisms Cat A; inherited Cat B from BC' dependency |

### Significant improvements (not new theorems)

| Name | Improvement |
|---|---|
| **H3 tightening** | β > 11α → β > 7α (formation-conditioned C₂^eff ≤ 0.671); asymptotically trivial |
| **d_min mechanism** | Identified true mechanism: nonlinear 3-chain (core saturation → mass redistribution → exterior depletion) |
| **TC' → TC''** | Transport bound tightened 300-4000× → 1-10× of actual displacement |

---

## 5. Updated Totals

**Before this session (from 20260402STATUS.md):**
- Category A: 28
- Category B: 3
- Category C: 4 + 1 new (T-Persist-K-Unified)
- Retracted: 2

**After gap resolution (Phase 1+2):**
- Category A: **36** (+8: T-Birth-Param(a), T-Birth-Param(b) equivariant, T-Birth-Topo, T-Birth-K2(a,b), T-Birth-K2(c) with Gap Condition, C3'' closed, ΔE_LI=Θ(β), f₁^IFT under BSR)
- Category B: **6** (+3: d_min^SCC<d_min^AC, γ_eff≈0.89, TC'')
- Category C: **4** + 1 new (unchanged; H3 tightened to β > 7α within Cat C)
- Retracted: 2 (unchanged)
- **Total: 46 claims + 1 new, 78% fully proved**

**Gap resolution upgrades:** Birth supercriticality B→A (equivariant), K2(c) B→A (Kronecker+Weyl), f₁ bound proved (BSR), TC'' tightened 300×, d_min mechanism corrected, H3 tightened.

---

## 6. Open Problems Resolved

| Open Problem (from FORMATION-BIRTH-THEORY.md §5) | Status |
|---|---|
| Formal birth theorem | **Resolved** (T-Birth-Param, T-Birth-Topo, T-Birth-K2) |
| C3'' symmetrization gap | **Resolved** (C3PP-PROOF.md) |
| Barrier exponent γ≈0.89 | **Partially resolved** (asymptotic Θ(β) proved; effective exponent explained but not derived) |
| d_min* formula | **Partially resolved** (qualitative d_min^SCC < d_min^AC proved; quantitative formula failed) |
| Multi-birth K→K+2 | **Open** (Birth Thm 3 gives necessary condition; sufficient condition requires codim-2 equivariant analysis) |

---

## 7. Recommended Next Steps

1. **Code alignment:** Update `graph.py:cohesion_weighted_symmetric` to D^{-1/2} form, run tests.
2. **Barrier γ_local fix:** Investigate the superlinear behavior at low β (γ_local > 1). Likely needs a third term in the expansion or explicit β-dependence of |R|.
3. **d_min mechanism:** Replace collective Gram scaling with interface sharpening analysis (closure increases effective c₀ via sharper profiles → faster exponential decay → smaller d_min).
4. **Canonical Spec update:** Register T-Birth-Param, T-Birth-Topo, T-Birth-K2, C3'' closure in §13.
5. **CHANGELOG update:** Log all 6 new Cat A results.
