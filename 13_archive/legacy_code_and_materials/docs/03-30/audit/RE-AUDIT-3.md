# RE-AUDIT-3: Post-Fix Verification and New Findings

**Date:** 2026-03-27
**Scope:** Verify Cycle 1-2 fixes, check ripple effects, run code, find remaining issues
**Auditor stance:** Maximally adversarial -- trust nothing, verify everything by running code

---

## VERIFIED CORRECT

### V1. BUG-1 fix is mathematically correct

The Hessian normalization in `energy.py:190-191` now reads:
```python
sigma_bd = abs(4.0 * self.params.alpha_bd * lam_max_L
               + self.params.beta_bd * W_pp)
```
The spurious factor of 2 on `W_pp` has been removed. On a 10x10 grid with default params:
- `sigma_bd = 26.0169` (matches hand computation: `|4*1.0*7.8042 + 10.0*(-0.52)| = 26.0169`)

### V2. C_t demotion is correct in the Canonical Spec

The formal universe (Spec Section 3, line 61) now reads:
```
C^soft = (T, {X_t}, {u_t}, {Cl_t}, {N_t, D_t}, {M_{t->s}})
```
C_t is absent. The change note at line 68 correctly explains the demotion. CN7 (line 858) correctly says "Operator Pair, Not Generic Self-Referentiality."

### V3. Sep is u-weighted everywhere in code

`diagnostics.py:51-63`: `Sep = sum(u*D) / sum(u)`. Correct.

### V4. QM1 normalization implemented in diagnostics.py

`inside_predicate` (line 66-82) includes the `(l_max - c)/(1 - c)` normalization that ensures uniform fields yield Q_morph = 0. Correct.

### V5. Figure 2 caption aligned with T7

Paper1 line 440: "Sharper curvature is proved; the relationship to actual barrier height requires Morse-theoretic analysis." This now matches the theorem's disclaimer at line 412. FIXED.

### V6. Operational closure language correct

Paper2 line 323 uses "operational closure" with the Maturana/Varela citation and explicitly disclaims full autopoiesis. FIXED.

### V7. Energy gradients still verified correct

All three gradients match finite differences (verified in RE-AUDIT-2, code unchanged).

---

## STILL BROKEN

### SB-1. (CRITICAL) BUG-2 "fix" is SEMANTICALLY WRONG -- stagnation != convergence

**Location:** `optimizer.py:158-163`

The Cycle 2 "fix" for BUG-2 changed the stagnation exit from `converged=False` to `converged=True`. This is **not a fix**. It relabels stagnation as convergence without addressing the underlying problem.

**Empirical evidence (10x10 grid, default params):**
- `converged = True`
- `grad_norm_history[-1] = 9.31e-02`
- `eps_grad threshold = 1e-06`
- Gradient is **93,000x above the convergence threshold**
- Energy change over last 50 iterations: `3.24e-10` (stagnated)

The optimizer declares convergence because energy has plateaued, but the **projected gradient norm is 0.093**, meaning the field is NOT at a critical point. It is stuck, not converged. The distinction matters:
- At a critical point, the projected gradient is zero (or near-zero)
- At a stagnation point, the energy is flat locally but the gradient points along the constraint manifold

**Impact:** Every result now claims `converged=True` when it should say `converged=False, stagnated=True`. The original BUG-2 was that the optimizer never converges; the "fix" hides this by lying about convergence status. The underlying convergence failure (gradient stagnation at ~0.09) is completely unaddressed.

**Correct fix:** Either (a) add a separate `stagnated` flag to `FormationResult`, or (b) only set `converged=True` when the gradient norm actually meets the threshold, or (c) relax eps_grad to ~0.1 and document this as "practical convergence."

### SB-2. (CRITICAL) C_t demotion NOT propagated to papers

Paper1 and paper2 still contain extensive C_t-as-primitive language that contradicts the spec:

**Paper1:**
- Line 71: "self-referential loop... operates through **three** structurally distinct modes" -- should say two variational + one diagnostic
- Line 78: Lists C_t as item 3 in the operator enumeration without stating it is diagnostic-only
- Line 81: "**triple-mode** structure of the self-dependence" -- should be dual-mode
- Line 81: "specific **operator-triad** structure of the cost function" -- should be operator-pair
- Line 123: "setup, **operator triad**, energy functional" -- should be operator pair
- Line 146: Section titled "**The Operator Triad**" -- should say "The Operators" or "The Operator Pair"
- Line 149: "**three** self-referential operators" -- should be two + one diagnostic
- Line 235: Figure caption: "field u defines the operators Cl_t, D_t, **C_t**; these define the energy" -- C_t does NOT define the energy
- Line 582: "cohesion fingerprint that encapsulates the **operator triad** at each site"
- Line 587: "**operator triad** that governs the static theory"
- Line 790: "Cl, D, **and** C all depend on the field u... **triple-mode** self-referential structure"
- Line 862: "self-referential through **three** structurally distinct modes"

**Paper2:**
- Line 60: "specific variational architecture (the **operator triad**)"
- Line 76: "defines **three** operators -- closure, distinction, and co-belonging"
- Line 314: "three operators -- closure, distinction, and co-belonging" (but then correctly notes two variational + one diagnostic)
- Line 316: Figure equation: `u -> (Cl_t, D_t, C_t) -> E -> u` -- C_t does not feed into E
- Line 355: Table maps Gestalt "Similarity / Common Fate" to C_t
- Line 368: "operator triad"
- Line 435: Table: "Self-reference: Structural (**operator triad**)"
- Line 448: "operator triad's self-referential energy minimization"
- Line 491: Table: "Integration measure: C_t (field-dependent co-belonging)" -- comparison with IIT's Phi
- Line 502: "high co-belonging C_t"
- Line 692: "association (adjacency N_t + co-belonging C_t)"
- Line 698: "self-referential **operator triad**"

**Paper2 line 314** is the closest to correct: it says "Two of these modes enter the energy directly; the third enters the diagnostic predicates." But it still frames this as "three operators" and calls it "The Operator Triad" language throughout.

**Required changes:** All "operator triad" must become "operator pair + diagnostic" or similar. All "three modes" must become "two variational modes + one diagnostic mode." The Figure caption and equation showing `C_t -> E` must be corrected.

### SB-3. (MODERATE) ISSUE-4: project_volume still clip-rescale, not true projection

**Location:** `optimizer.py:39-55`

Confirmed still unfixed. Empirical comparison:
- Code (clip-rescale): distance 0.597 from original
- True projection (clip-shift): distance 0.520 from original
- Code gives a point 15% farther than the nearest feasible point

This biased projection likely contributes to the gradient stagnation in SB-1.

### SB-4. (MODERATE) BUG-3: Hessian norm ignores eigenvalue at lambda_2

**Location:** `energy.py:183-191`

Still unfixed. The code only checks the eigenvalue at `lambda_max(L)`:
```
sigma_bd = |4*alpha*lambda_max + beta*W''(c)|
```
The correct spectral norm on T(Sigma_m) is:
```
sigma_bd = max_k |4*alpha*lambda_k + beta*W''(c)|
```
which requires checking BOTH `lambda_max` and `lambda_2` (where `W''(c) < 0` makes the eigenvalue most negative).

On default parameters (10x10 grid, beta=10):
- Eigenvalue at lambda_max: +26.02 (dominates)
- Eigenvalue at lambda_2: -4.81

BUG-3 does NOT bite for default params. It bites when beta > ~30 on a 10x10 grid. The threshold scales with graph size.

### SB-5. (MODERATE) ISSUE-7: W_sym negative eigenvalues unguarded in resolvent

Confirmed still unfixed. With `alpha_C = 2.0` on a 5x5 grid:
- Resolvent diagonal values: 130 to 272 (should be near 1)
- The Neumann series diverges silently
- No runtime guard or warning

### SB-6. (LOW) ISSUE-5: Double gradient computation per step

`optimizer.py`: gradient computed at line 101 and again at line 133 (for BB). On the next iteration, line 101 recomputes the same gradient. Still unfixed.

---

## NEW FINDINGS

### NF-1. (CRITICAL) Diagnostic values do NOT match paper claims

The BUG-1 fix changed the Hessian normalization, which changes the effective energy weights, which changes the optimized field, which changes ALL diagnostic values. The papers were written with the buggy normalization.

**Paper claims vs. current code (10x10 grid, 3 restarts):**

| Predicate | Paper1 claim | Paper2 claim | Current code |
|-----------|-------------|-------------|-------------|
| Bind      | ~0.86       | ~0.86       | 0.864        |
| Sep       | ~0.93       | ~0.93       | 0.883        |
| Inside    | ~0.98       | ~0.98       | 0.933        |

Bind is approximately correct. **Sep is 5 points lower (0.88 vs 0.93). Inside is 5 points lower (0.93 vs 0.98).** These differences are significant and directly caused by the BUG-1 fix changing the energy weight balance.

**Multi-size comparison (current code):**

| Grid   | Bind  | Sep   | Inside |
|--------|-------|-------|--------|
| 5x5    | 0.861 | 0.766 | 0.982  |
| 10x10  | 0.864 | 0.883 | 0.933  |
| 15x15  | 0.863 | 0.918 | 0.937  |

The 5x5 result is particularly bad: Sep = 0.766, far from the claimed ~0.93.

**Impact:** ALL diagnostic numbers in both papers, ALL ablation results, and ALL sensitivity analyses were computed with the buggy normalization. They must be re-run and the papers updated. The qualitative story (Bind limited by boundary residual, Sep responds to lambda_sep/lambda_bd ratio, Inside near 1.0) is likely still correct, but the specific numbers are wrong.

### NF-2. (CRITICAL) "4-17x larger Hessian eigenvalues" claim is unreliable

Paper1 line 412 cites a "computational observation of 4-17x larger minimum Hessian eigenvalues." This observation was made with:
1. Buggy normalization (BUG-1) -- different energy weights
2. Non-converged optimizer (SB-1) -- field not at critical point
3. Biased projection (SB-3) -- systematic drift

The 4-17x number was computed at a non-critical point with wrong energy weights. It may or may not survive re-computation. Until re-run with the corrected code, this claim should be marked as unverified.

### NF-3. (MODERATE) Theorem 4 proof has a gap

Paper1, Theorem 4 (Enhanced Metastability), lines 387-404:

**Gap 1:** The proof claims the E_cl Hessian is `2(I - J_Cl)^T(I - J_Cl)`. This is only the Gauss-Newton approximation of the Hessian, valid when the residual `Cl(u) - u` is zero (i.e., at a closure fixed point). At actual minimizers, Bind ~ 0.87, meaning `||Cl(u) - u||/sqrt(n) ~ 0.13`. The second-order term `2 * sum_i r_i * H_i[Cl]` (involving the Hessian of Cl) is dropped without justification.

**Gap 2:** The proof claims "min_eig(full Hessian) > min_eig(E_bd Hessian)" because adding a PD matrix increases eigenvalues. But the full Hessian is `lambda_cl * H_cl + lambda_sep * H_sep + lambda_bd * H_bd`. The proof only shows H_cl is PD (approximately). It says nothing about H_sep, which could be indefinite. If H_sep has sufficiently negative eigenvalues, they could overwhelm the PD contribution of H_cl, breaking the inequality.

The theorem statement may still be true (it's about minimizers, where second-order conditions hold), but the proof as written has gaps.

### NF-4. (MODERATE) Paper2 Persist formula differs from spec and paper1

Paper2 line 219 gives the Persist predicate as:
```
Persist(u_t, u_s, M) = |Core_t intersection M^{-1}(Core_s)| / |Core_t|
```
This is a **crisp** (set-based) formula using thresholded cores. The spec (Section 7.1) and paper1 should use the same formula, but the code (`diagnostics.py:146-160`) implements a completely different L2 field-similarity proxy:
```python
1 - ||u_curr - u_prev|| / ||u_prev||
```
The three versions (paper2 crisp, spec, code proxy) are all different. This was flagged in RE-AUDIT-2 item S6 but remains unresolved.

### NF-5. (LOW) Paper1 line 395 conflates curvature with barrier height

The proof text says "The energy barrier from a local minimizer u_hat is determined by the smallest eigenvalue of the Hessian." This is false in general -- Hessian eigenvalue determines local curvature, not barrier height (which depends on saddle-point analysis). The remark at line 412 correctly disclaims this, but the proof text itself makes the false claim. The variable name `Delta(barrier)` at line 402 should be `Delta(curvature)` or `Delta(min_eigenvalue)`.

---

## DIAGNOSTIC VALUES SUMMARY

**After BUG-1 fix, all published diagnostic numbers are stale.** Current values from the corrected code:

| Grid | Bind | Sep | Inside | Persist | converged | |grad| |
|------|------|-----|--------|---------|-----------|--------|
| 5x5  | 0.861 | 0.766 | 0.982 | 1.0 | False | 8.82e-02 |
| 10x10 | 0.864 | 0.883 | 0.933 | 1.0 | True* | 9.31e-02 |
| 15x15 | 0.863 | 0.918 | 0.937 | 1.0 | False | 7.14e-02 |

*converged=True via stagnation exit, NOT via gradient convergence (grad norm is 93,000x above threshold)

**Key observations:**
1. Bind is stable at ~0.86 across sizes (matches papers, unaffected by normalization change)
2. Sep is 0.77-0.92, significantly lower than claimed ~0.93
3. Inside is 0.93-0.98, lower than claimed ~0.98 on larger grids
4. No run achieves true gradient convergence; all stagnate at |grad| ~ 0.07-0.09

---

## PRIORITY RANKING

1. **SB-2 (CRITICAL): C_t demotion not propagated to papers.** Both papers say "operator triad" / "three modes" dozens of times. This directly contradicts the updated spec. Text-level fix, no math changes needed, but extensive.

2. **NF-1 (CRITICAL): Diagnostic numbers are wrong in both papers.** All experiments must be re-run with corrected normalization and numbers updated. The qualitative story survives but specific values change.

3. **SB-1 (CRITICAL): BUG-2 "fix" is a lie.** Setting stagnation=converged hides the convergence failure. The optimizer still does not converge; it just claims to. Must either (a) fix the convergence issue (biased projection SB-3 is a likely culprit), or (b) honestly report that results are from stagnated, non-converged runs.

4. **NF-2 (CRITICAL): "4-17x Hessian eigenvalue" claim unverified.** Computed with wrong normalization at non-converged points. Must re-compute or remove.

5. **NF-3 (MODERATE): Theorem 4 proof has gaps.** The Gauss-Newton approximation and the ignored E_sep Hessian need to be addressed. The theorem may survive with a corrected proof, but the current proof is incomplete.

6. **SB-3 (MODERATE): project_volume is biased.** Known fix available (clip-shift via Brent's method). Likely contributes to convergence failure.

7. **SB-4 (MODERATE): BUG-3 still present.** Does not bite for default params but is mathematically wrong for large beta.

8. **NF-4 (MODERATE): Persist formula inconsistency across documents.** Three different formulas in three different places.

9. **SB-5 (MODERATE): Resolvent divergence unguarded.** Silent numerical corruption for alpha_C >= ~1.

10. **NF-5 (LOW): Proof text conflates curvature with barrier height.**

11. **SB-6 (LOW): Double gradient computation.** Performance, not correctness.
