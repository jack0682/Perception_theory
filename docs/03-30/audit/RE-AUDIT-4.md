# RE-AUDIT-4: Cycle 5 Adversarial Audit

**Date:** 2026-03-27
**Scope:** Verify Cycle 1-4 fixes, find what is still broken
**Auditor stance:** Maximally adversarial -- run all claims through code, trust nothing

**Previously fixed (not re-reported):**
Cycle 1: Sep u-weighted, T7 Hessian curvature, QM1 normalized, Transport conditional, autopoiesis language, MFG citation
Cycle 2: BUG-1 Hessian factor, C_t demoted in spec, beta_crit caveat, T-Bind added
Cycle 3: converged flag honest, triad->pair in papers, resolvent divergence guard
Cycle 4: project_volume Euclidean clip-shift, BUG-3 Hessian lambda_2 check, diagnostic values re-verified

---

## VERIFIED CORRECT

### V1. project_volume uses clip-shift algorithm (Cycle 4 fix)

The algorithm at `optimizer.py:39-66` correctly implements bisection on the shift parameter lambda to solve `sum(clip(u - lam, 0, 1)) = m`. This is the true Euclidean projection onto the simplex-box intersection, replacing the old multiplicative rescaling.

**However, see SB-1 for a bug in the implementation.**

### V2. BUG-3 Hessian lambda_2 check implemented (Cycle 4 fix)

`energy.py:192-196` now computes both `eig_at_max` and `eig_at_lam2`, taking `sigma_bd = max(abs(...), abs(...))`. Correct.

### V3. C_t demotion propagated to paper1 operator section

Paper1 line 149: "The theory is built on two variational operators and one derived diagnostic." Line 206: "Co-belonging enters the theory's diagnostic predicates but does not enter the energy functional." Line 235 (Figure caption): "The co-belonging operator C_t (not shown) serves as a derived diagnostic." These are all correct.

### V4. Paper1 "dual-mode" language correct in key locations

Paper1 line 71: "two variational modes and one diagnostic mode" -- correct.
Paper1 line 81: "dual-mode variational self-dependence...with a third diagnostic mode" -- correct.
Paper1 line 790: "dual-mode variational self-referential structure (self-completion and self-contrast entering the energy, with self-integration via C_t available as a derived diagnostic)" -- correct.

### V5. Converged flag honest (Cycle 3 fix)

`optimizer.py:163-165`: converged is only True when ALL three conditions are met (rel_dE, gnorm, ds). The stagnation exit at line 176-179 does NOT set converged=True. All test runs correctly report `converged=False` when gradient norm remains ~0.06.

### V6. Paper2 line 314 correctly explains C_t demotion

"Two of these modes (self-completion and self-contrast) enter the energy functional directly; the third (self-integration via C_t) enters the diagnostic predicates but not the energy---an architectural decision, not an oversight."

### V7. Persist formula inconsistency is ACKNOWLEDGED

Paper2 line 222: "The current computational implementation uses a simple field-similarity proxy rather than the core-inheritance formula above." Code `diagnostics.py:147-153` docstring: "NOTE: This does NOT implement the spec formula." Spec line 443: "Status Note. The persistence predicate has zero proved results across all iterations." Paper1 line 727: "temporal persistence has not been computationally validated." The inconsistency exists but is now honestly disclosed in all three locations. **VERIFIED as acknowledged.**

### V8. Diagnostic values approximately match papers

Current code (5 restarts, normalize=True):

| Grid  | Bind  | Sep   | Inside |
|-------|-------|-------|--------|
| 10x10 | 0.856 | 0.941 | 0.981  |
| 15x15 | 0.858 | 0.952 | 0.972  |
| 20x20 | 0.859 | 0.963 | 0.977  |

Paper claims: Bind ~0.86, Sep ~0.93, Inside ~0.98. Current values are Bind ~0.86 (match), Sep ~0.94-0.96 (slightly HIGHER than claimed 0.93), Inside ~0.97-0.98 (match). The Sep improvement is a genuine improvement from the Cycle 4 projection fix. **The papers understate Sep by ~2 points but this is conservative, not misleading.** The prompt's claim that "Sep is HIGHER than claimed" is correct -- papers should ideally be updated to ~0.95 but the current ~0.93 claim is conservative.

**Verdict:** MINOR -- papers are slightly conservative on Sep. Not broken.

---

## STILL BROKEN

### SB-1. (MODERATE) BUG in project_volume: early-exit uses wrong lambda

**Location:** `optimizer.py:55-66`

**Bug:** When bisection converges early (line 63-64 `break`), the convergence check happens AFTER the lo/hi update (lines 59-62). So if `s == m` exactly at `mid`, the code updates `hi = mid` (since `s > m` is false when `s == m`), then breaks. Line 66 then computes `(lo + hi) / 2` which is NOT the converged `mid` -- it is the midpoint of the old `lo` and the just-updated `hi`.

**Empirical evidence:**
```
u = [0.5]*10, m = 5.0 (already feasible, should be identity)
Expected: v = [0.5]*10, sum = 5.0
Actual:   v = [0.75]*10, sum = 7.5
```

The bug fires whenever bisection converges in a small number of iterations (uniform or near-uniform inputs). In practice during optimization, the field is rarely uniform, so the bug fires mainly at initialization -- the initial `u = c*1 + eps*v` projected via `project_volume` gets slightly distorted on the first call.

**Impact on results:** Moderate. After the first few optimization steps, the field is non-uniform enough that bisection takes many iterations and the final `(lo+hi)/2` is accurate. But the initial projection is wrong, potentially biasing the starting point.

**Fix:** Move the convergence check BEFORE the lo/hi update, or use `mid` directly:
```python
for _ in range(60):
    mid = (lo + hi) / 2.0
    v = np.clip(u - mid, 0.0, 1.0)
    s = np.sum(v)
    if abs(s - m) < 1e-12:
        break
    if s > m:
        lo = mid
    else:
        hi = mid
return np.clip(u - mid, 0.0, 1.0)
```

### SB-2. (CRITICAL) "4-17x larger minimum Hessian eigenvalues" claim is WRONG

**Location:** Paper1 line 412

**Theorem 4 (Enhanced Metastability) says:** At the SCC minimizer, min_eig(full Hessian) > min_eig(bd-only Hessian at same point). This is the correct comparison -- same point, add PD matrix, eigenvalues increase.

**Paper claims:** "The computational observation of 4--17x larger minimum Hessian eigenvalues (Section VII)."

**Actual values (corrected code, finite-difference Hessian, projected onto T(Sigma_m)):**

| Grid  | bd-only min_eig | full min_eig | Ratio |
|-------|----------------|--------------|-------|
| 5x5   | 0.155          | 0.348        | 2.2x  |
| 7x7   | 0.272          | 0.338        | 1.2x  |
| 10x10 | 0.013          | 0.168        | 13.2x |
| 15x15 | 0.075          | 0.152        | 2.0x  |

**The range is 1.2-13.2x, NOT 4-17x.** The 7x7 case gives only 1.2x, far below the claimed 4x lower bound. The 5x5 and 15x15 cases are ~2x, also below 4x. Only the 10x10 case (13.2x) falls within the claimed range.

The original "4-17x" was computed with (a) buggy Hessian normalization (BUG-1), (b) biased projection (old multiplicative rescaling), and (c) possibly different parameter settings. The corrected code does NOT reproduce this claim.

**The theorem itself is still true** -- the ratio is always > 1.0 (which is what the theorem guarantees). But the specific "4-17x" quantitative claim is wrong and must be removed or corrected to "1.2-13.2x" (or more conservatively, "the enhancement ratio varies with grid size and can range from modest (~1.2x) to substantial (~13x)").

**Priority:** CRITICAL -- this is a specific numerical claim in the paper that is falsified by corrected code.

### SB-3. (MODERATE) Paper2 line 76 still says "three operators...define an energy functional"

**Location:** `paper2_cogsci.tex:76`

**Text:** "The cohesion field u defines three operators---closure (Cl), distinction (D), and co-belonging (C)---which depend on u itself. These operators then define an energy functional whose minimization determines u."

**Problem:** The second sentence says all three operators "define an energy functional." This is wrong -- C_t does NOT enter the energy. Line 314 correctly explains the demotion, but line 76 in the introduction does not. A reader encountering line 76 first gets the wrong impression.

**Fix:** Change to: "The cohesion field u defines three operators---closure (Cl), distinction (D), and co-belonging (C)---which depend on u itself. Two of these (closure and distinction) define an energy functional whose minimization determines u; the third (co-belonging) serves as a structural diagnostic."

### SB-4. (MODERATE) Paper2 line 316 equation shows C_t feeding into energy

**Location:** `paper2_cogsci.tex:316`

**Equation:**
```
u -> (Cl_t, D_t, C_t) -> E -> u
```

**Problem:** The arrow from `(Cl_t, D_t, C_t)` to `E` implies all three define the energy. But C_t does NOT enter E. The text at line 314 says this correctly, but the equation contradicts it.

**Fix:** Either:
- `u -> (Cl_t, D_t) -> E -> u` (remove C_t from the equation), or
- `u -> (Cl_t, D_t) -> E -> u` with a separate branch `u -> C_t -> d` showing diagnostics

### SB-5. (MODERATE) Paper2 line 698 says "operator pair" then lists THREE operators

**Location:** `paper2_cogsci.tex:698`

**Text:** "The self-referential operator pair---self-completion (Cl), self-contrast (D), self-integration (C)---exhibits a structural analogue of autopoietic organization."

**Problem:** Calling it an "operator pair" while listing three operators is a direct contradiction within the same sentence.

**Fix:** "The self-referential operator structure---self-completion (Cl) and self-contrast (D) as variational operators, with self-integration (C) as a diagnostic---exhibits..."

### SB-6. (LOW) Paper2 Gestalt table (line 355) maps C_t to Similarity/Common Fate without noting diagnostic status

**Location:** `paper2_cogsci.tex:355`

The table entry `Similarity / Common Fate -> C_t (co-belonging operator) -> Structural analogue (non-local)` does not note that C_t is diagnostic-only. A reader would assume C_t has the same status as Cl_t and D_t in the theory.

**Fix:** Add "(diagnostic)" to the SCC Counterpart column.

---

## NEW FINDINGS

### NF-1. (MODERATE) Theorem 4 proof gap (T4/NF-3) -- Gauss-Newton approximation

**Location:** Paper1 lines 392-404

**Gap 1 (persists from RE-AUDIT-3):** The proof uses `H_cl = 2(I - J_Cl)^T(I - J_Cl)` which is the Gauss-Newton approximation of the E_cl Hessian. The full Hessian is `2(I - J_Cl)^T(I - J_Cl) + 2 * sum_i r_i * H_i[Cl]` where `r_i = Cl(u)_i - u_i` is the residual. At optimized formations, `Bind ~ 0.86`, meaning residuals are non-negligible (~0.14 * sqrt(n)). The second-order term is dropped without justification.

The Gauss-Newton approximation is a LOWER BOUND on the true Hessian only if the residuals are small relative to the curvature. At actual minimizers:
- Residual contribution could be negative (if residuals anti-correlate with Hessian of Cl)
- The PD claim for H_cl could fail if the second-order term has sufficiently negative eigenvalues

**Gap 2 (persists from RE-AUDIT-3):** The proof claims adding a PD matrix increases min_eig. But the full Hessian includes `lambda_sep * H_sep`, and H_sep could be indefinite. The proof ignores this:

```
min_eig(lambda_cl * H_cl + lambda_sep * H_sep + lambda_bd * H_bd)
   >= min_eig(lambda_bd * H_bd)  [only if lambda_cl*H_cl + lambda_sep*H_sep >= 0]
```

The theorem's conclusion (strictly larger) requires `lambda_cl * H_cl + lambda_sep * H_sep` to be at least PSD, but only H_cl PD is shown.

**Verdict:** The theorem is likely true in practice (the computational evidence confirms ratios > 1), but the proof has two gaps. The theorem should either be qualified ("assuming the Gauss-Newton approximation holds and H_sep is PSD") or the gaps should be closed.

### NF-2. (LOW) Paper1 line 707 still says "iterative clipping and rescaling"

**Location:** `paper1_math.tex:707`

**Text:** "Projection onto Sigma_m intersect [0,1]^n uses iterative clipping and rescaling."

**Problem:** The code now uses clip-and-shift bisection (Cycle 4 fix), not clipping and rescaling. The paper description is stale.

### NF-3. (LOW) Paper1 line 395 still conflates curvature with barrier height

**Location:** `paper1_math.tex:395`

**Text:** "The energy barrier from a local minimizer u_hat is determined by the smallest eigenvalue of the Hessian."

**Problem (persists from RE-AUDIT-3 NF-5):** Hessian eigenvalue determines local curvature, not barrier height. The barrier height is determined by the saddle-point energy minus the minimizer energy, which depends on global landscape features, not just local curvature. The variable name `Delta(barrier)` at line 402 should be `Delta(curvature)` or `Delta(min\_eigenvalue)`.

The remark at line 412 correctly disclaims this, but the proof text itself makes the incorrect claim.

---

## PRIORITY RANKING

1. **SB-2 (CRITICAL): "4-17x Hessian eigenvalue" claim is falsified.** Corrected code gives 1.2-13.2x. The specific numbers must be updated or removed from paper1 line 412. The theorem itself is NOT invalidated (ratio > 1 is confirmed), only the specific quantitative claim.

2. **SB-3 (MODERATE): Paper2 line 76 says three operators define energy.** Misleading in the introduction -- the most prominent location in the paper.

3. **SB-4 (MODERATE): Paper2 line 316 equation shows C_t -> E.** Directly contradicts the demotion.

4. **SB-5 (MODERATE): Paper2 line 698 "operator pair" lists three.** Self-contradictory sentence.

5. **SB-1 (MODERATE): project_volume early-exit bug.** Returns wrong result for near-uniform inputs. Affects initialization but unlikely to change final results significantly.

6. **NF-1 (MODERATE): Theorem 4 proof gaps.** Two mathematical gaps in the proof. Does not invalidate the theorem (computation confirms it) but weakens the paper's rigor.

7. **SB-6 (LOW): Paper2 Gestalt table C_t entry.** Missing diagnostic annotation.

8. **NF-2 (LOW): Paper1 projection description stale.** Says "clipping and rescaling" but code now uses clip-and-shift.

9. **NF-3 (LOW): Curvature/barrier conflation in proof text.** Disclaimer exists but proof text still incorrect.

---

## SUMMARY

The major Cycle 1-4 fixes (Sep u-weighting, Hessian factor, C_t demotion in spec, converged flag, Euclidean projection, lambda_2 check) are all correctly implemented. The diagnostic values now approximately match paper claims (Bind ~0.86, Sep ~0.94-0.96, Inside ~0.97-0.98), with Sep actually slightly higher than the papers' conservative ~0.93.

The single most important remaining issue is **SB-2**: the "4-17x Hessian eigenvalue" claim is falsified by corrected code (actual range: 1.2-13.2x). This is a specific quantitative claim that appears in paper1 and must be corrected.

The C_t demotion is correctly done in the spec and in paper1's operator section, but paper2 still has three locations (lines 76, 316, 698) where the language contradicts the demotion.

A new bug was found in `project_volume` (SB-1) where the early-exit path returns the wrong result for near-uniform inputs.
