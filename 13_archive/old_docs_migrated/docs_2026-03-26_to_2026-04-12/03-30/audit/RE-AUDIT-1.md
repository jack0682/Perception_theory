# RE-AUDIT-1: Post-Fix Verification

**Date:** 2026-03-30
**Scope:** All files post-13 emergency fixes
**Auditor stance:** Adversarial — assume broken until verified

---

## FIXED AND VERIFIED

These items from the emergency fixes are confirmed correct and consistent:

### 1. Sep u-weighted formula: CONSISTENT across all files
- **Spec §7.1** (line 407): `Sep = Sum u(x) D(x;1-u) / Sum u(x)` -- u-weighted
- **Paper1** (line 261): Same formula, correctly described as "cohesion-weighted average"
- **Paper2** (line 184): Same formula, correctly described
- **Code** (diagnostics.py:63): `np.sum(u * D_u) / m` -- matches exactly
- **Algebraic verification:** Sep = Sum(u*D)/m = (m - E_sep)/m = 1 - E_sep/m. The proved equality **holds** for this formulation. (E_sep = Sum u(1-D) = m - Sum(u*D), so Sum(u*D) = m - E_sep, dividing by m gives the result.)

### 2. C_t codomain [0,infinity): CONSISTENT
- Spec §3.6 (line 116): `[0,infinity)` with clear explanation
- Paper2 (line 229): `[0,infinity)` -- matches

### 3. T7 Hessian curvature qualification: Paper1 CORRECT
- Paper1 Theorem 4 (line 387-413) correctly states "minimum eigenvalue of Hessian strictly exceeds" -- not "energy barriers"
- Remark at line 411-413 explicitly disclaims the gap between Hessian eigenvalue and actual barrier height
- Paper1 is honest here. (**But see STILL BROKEN #1 below for the spec.**)

### 4. QM1 normalized formula in code: CORRECT
- Code (diagnostics.py:78-82) implements `(l_max - c)/(1-c) * artic` with proper guards
- Edge case c near 1: guarded at line 79 (returns 0.0)
- Edge case l_max < c: `max(0.0, ...)` clamp at line 81 (returns 0.0)
- Edge case c = 0: l_max = 0, caught at line 76 (returns 0.0)
- Uniform field u = c*1: l_max = c (sole surviving component), numerator = 0. QM1 satisfied.

### 5. Transport FP conditional: Paper1 CORRECT
- Paper1 Theorem 6 (temporal persistence) is labeled conditional on proof gaps

### 6. Autopoiesis -> operational closure: Paper2 CORRECT
- Paper2 (line 696-700) uses "operational closure" with explicit qualification: "not full autopoiesis"

### 7. Persist placeholder: Code CORRECT
- diagnostics.py:147-160 clearly labeled as "PLACEHOLDER" with explanation

---

## NEW ISSUES (Introduced by the Fixes)

### N1. **CRITICAL: Spec claims C_t enters Sep -- it no longer does**

The Sep fix to u-weighting removed C_t from the separation predicate, but three places in the spec still claim C_t enters Sep:

- **Spec §3.6** (line 120): "Co-belonging enters the theory's predicates (specifically, the separation predicate Sep)"
- **Spec Group C** (line 334): "Co-belonging enters the separation predicate Sep but does not enter the energy functional E"
- **Spec §11.1 item 12** (line 695): "C_t is diagnostic, not variational. Co-belonging enters predicates but not the energy functional."

**Problem:** After the u-weighted fix, C_t enters **no** predicate. Sep uses u(x) as weights, not C_t(x,x). The co-belonging operator currently has no role in any predicate or energy term -- it is computed but unused in the diagnostic pipeline. This undermines the claimed "diagnostic role" that justified keeping C_t in the formal universe.

**Severity:** HIGH. This is not a typo -- it's a structural claim about the theory's architecture that became false when Sep was fixed. Either (a) update the spec to acknowledge C_t has no current predicate role, or (b) re-introduce C_t into some predicate formula.

### N2. **Code has dead import from pre-fix state**

diagnostics.py line 10: `from scc.operators import closure, distinction, resolvent_diagonal`

`resolvent_diagonal` is imported but never called in any predicate function. This is a residual from when Sep used C_t-weighting. Not a correctness issue, but a code smell that signals the fix was incomplete.

### N3. **Paper1 Open Problem 5 has confused terminology**

Paper1 line 845-847:
> "The exact bridge Sep_old = 1 - E_sep/m holds for the unweighted separation predicate."

This is wrong on two levels:
1. The equality holds for the **u-weighted** formulation (the current one), not an "unweighted" one
2. The naming "Sep_old" is ambiguous -- in the paper's naming convention, Sep_old was the pre-C_t version, but the current u-weighted Sep was introduced after both Sep_old and Sep_new

The equality Sep = 1 - E_sep/m holds because E_sep = Sum u(1-D) and Sep = Sum(uD)/Sum(u). This is specific to the u-weighted formula. The original "Sep_old" (simple average of D over crisp interior) does NOT satisfy this equality.

---

## STILL BROKEN (From Original Audit, Not Yet Fixed)

### S1. **T7-Enhanced overstatement in spec**

Spec line 808-810:
> "Non-trivial constrained minimizers of SCC energy have strictly larger **energy barriers** than corresponding Allen-Cahn minimizers"

Paper1 correctly limits this to "larger minimum Hessian eigenvalue" (line 389) and explicitly disclaims the barrier height connection (line 411-413). The spec still claims "energy barriers" without qualification. The Hessian eigenvalue is a local curvature measure; actual barrier height (saddle energy minus minimizer energy) requires Morse-theoretic analysis that hasn't been done.

**Status:** Paper1 is correct; spec overstates.

### S2. **Q_morph formula inconsistency across files**

There are TWO formulas for Q_morph and they appear inconsistently:

| Location | Formula | Version |
|----------|---------|---------|
| Spec §7.1 line 424-425 | `l_max * Artic` | Unnormalized |
| Spec §7.1 line 435 | `(l_max - c)/(1-c) * Artic` | Normalized |
| Spec line 866 (closing summary) | `l_max * Artic` | Unnormalized |
| Paper1 line 267 | `(l_max - u_bar)/(1 - u_bar) * Artic` | **Normalized** |
| Paper2 line 200 | `l_max * Artic` | **Unnormalized** |
| Code implementation (line 81) | `(l_max - c)/(1-c) * artic` | Normalized |
| Code docstring (line 67) | "l_max * Artic" | Unnormalized |

The spec is internally inconsistent: line 419 says `Inside = Q_morph`, line 425 defines Q_morph as unnormalized, and then line 435 separately introduces a "normalized Q_morph" that satisfies QM1. There is no clear statement that Inside = **normalized** Q_morph. Paper1 and paper2 use different formulas. The code implements normalized but its docstring says unnormalized.

**Severity:** HIGH. This affects whether the theory claims QM1 holds. The unnormalized version does NOT satisfy QM1 (uniform fields give Q_morph = c != 0). Only the normalized version satisfies QM1.

### S3. **A1' theta_support is undefined**

Spec line 246: "where... theta_support in (0,1] is a support threshold."

No value is specified anywhere -- not in the spec, not in params.py, not in the papers. The axiom A1' is formally incomplete without a specified or constrained theta_support. The sigmoid closure satisfies A1' for some theta_support (since sigma is monotone and the pre-activation includes both self and neighbor terms), but the precise range of admissible theta_support values has not been characterized.

### S4. **C3'' gap still open (documented but unfixed)**

Spec line 794 and Paper1 line 558-560 both acknowledge the gap: the symmetrization step (D^{-1/2} depends on u(x)) in the Neumann series monotonicity argument awaits formal verification. Documented but still open.

### S5. **beta_crit -> 0 at scale: not explicitly addressed**

For grid graphs, lambda_2 ~ O(1/n) as n -> infinity. The T8-Core condition beta/alpha > 4*lambda_2/|W''(c)| becomes trivially satisfied for large graphs (beta_crit -> 0). This means:
- The phase transition theorem is vacuously true at large scale (any beta > 0 suffices)
- The theorem provides no structural information about large-scale behavior
- This is not a bug per se, but the papers present T8-Core as a substantive result without noting its vacuousness at scale

Neither the spec nor the papers mention this scaling issue.

### S6. **Paper2 Persist formula differs from spec and paper1**

Paper2 line 219:
```
Persist(u_t, u_s, M) = |Core_t ∩ M^{-1}(Core_s)| / |Core_t|
```

Spec line 440 and Paper1 line 272-274:
```
Persist_W(u) = min_{t<s} Sum_{Core_t} Sum_{Core_s} M(x,y) u_s(y) / rho_persist
```

These are fundamentally different formulas. Paper2 uses crisp set cardinality ratios; the spec/paper1 use soft transport-weighted sums. Paper2's formula requires crisp Core sets and a crisp inverse-image M^{-1}, while the spec's formula is fully soft.

### S7. **Predicate-energy bridge remains one-directional (acknowledged)**

The spec (line 741) and paper1 (line 820) acknowledge that low energy implies high predicates, but high predicates do not imply low energy. This is documented as an open problem -- not a "bug" but the theory's largest structural gap after temporal persistence.

---

## NEWLY DISCOVERED

### D1. **Spec §7.1 defines Inside ambiguously between two Q_morph formulas**

The spec creates a chain:
1. Line 419: `Inside_t(u_t) = Q_morph(u_t)` (the definition)
2. Line 424-425: `Q_morph = l_max * Artic` (the "provisional definition")
3. Line 435: "The **normalized** Q_morph = (l_max - c)/(1-c) * Artic satisfies QM1-4"

This is structurally confused. Is Inside equal to the unnormalized Q_morph (line 425) or the normalized version (line 435)? The spec appears to define Inside as the unnormalized version and then prove QM axioms only for the normalized version. The code and paper1 use normalized. Paper2 uses unnormalized. Nobody agrees.

The fix should be: update the definition at line 425 to be the normalized version, and state clearly that this IS Q_morph (not a variant of it).

### D2. **C_t has no functional role in the current theory**

After the Sep fix, C_t (co-belonging) enters:
- No predicate (Sep uses u-weighting)
- No energy term (by design)
- No optimization target

C_t is computed in the code (operators.py has resolvent_diagonal and resolvent_full), imported in diagnostics.py, but never called in any active predicate. The formal universe includes C_t as a primitive, but it is architecturally orphaned.

This raises a foundational question: if C_t has no role in any predicate or energy term, why is it in the formal universe? The spec's answer was "it enters Sep" -- but that's no longer true.

**Options:** (a) Find a new role for C_t (e.g., use it in a weighted version of Bind or Inside), (b) demote C_t from the formal universe to a derived diagnostic (like T_t was demoted), (c) reintroduce C_t-weighting into Sep alongside u-weighting. This is a theoretical design decision, not a mechanical fix.

### D3. **E_sep gradient ignores the Σu normalization in Sep**

The energy E_sep = Sum u(1-D) and its gradient ∇E_sep = (1-D) - J_D^T u are correctly implemented (verified against FD to 1e-9). However, the diagnostic Sep = Sum(uD)/Sum(u) uses division by Sum(u). If anyone ever tried to optimize Sep directly (rather than E_sep), the gradient would need the quotient rule, not just the numerator gradient. This is not a bug -- the code correctly optimizes E_sep, not Sep -- but worth noting for future development.

### D4. **Paper1 Prop 3.5 (Sep Covariance Identity) is about a rejected formulation**

Paper1 lines 564-570 prove a proposition about the C_t-weighted Sep (called "Sep_new"), which is the formulation that was **rejected** because it averages ~0.5 regardless. The proposition is mathematically correct but concerns a formulation the theory no longer uses. It's still in the paper without clear indication that it's about the rejected version (the label "Sep_new" is confusing since the current Sep is actually the newest).

### D5. **Hessian normalization suggests lambda_sep/lambda_bd ~ 10^-5, but experiments use ratio ~1**

The spec (line 745) and paper1 (line 854) note that Hessian normalization suggests lambda_sep/lambda_bd ~ 10^{-5}. But the experiments (paper1 line 768, paper2 line 667) report a sweet spot at lambda_sep/lambda_bd ~ 1.0. This is a 5-order-of-magnitude discrepancy between the theoretical suggestion and the empirical finding. Neither paper acknowledges or explains this discrepancy.

### D6. **W''(c) formula inconsistency in paper1 proof**

Paper1 line 339 states `W''(c) = 12c^2 - 12c + 2`.
But W(u) = u^2(1-u)^2, so W'(u) = 2u(1-u)(1-2u) = 2u - 6u^2 + 4u^3.
W''(u) = 2 - 12u + 12u^2. This equals 2(1 - 6u + 6u^2) = 12u^2 - 12u + 2. **Correct.**
(Just verifying -- this one checks out.)

### D7. **project_volume is not a true projection onto the constraint manifold**

optimizer.py:39-55 uses iterative clip-and-rescale. This is a heuristic, not a proper projection onto {v in [0,1]^n : sum(v) = m}. The true projection requires solving a KKT system (essentially isotonic regression). The heuristic converges in practice (15 iterations), but:
- No convergence guarantee is provided
- The projection may not be the nearest point in Euclidean metric
- For fields near the boundary of [0,1]^n, the heuristic may cycle

This is documented nowhere. For the current experiments it works, but it could silently fail for edge-case parameter regimes.

---

## NEXT PRIORITY (Ranked)

1. **Fix C_t/Sep architectural claim (N1 + D2)** -- Three places in the spec falsely claim C_t enters Sep. This is the most urgent because it misrepresents the theory's current structure. Either update the spec to acknowledge C_t's orphaned status, or deliberately reintroduce C_t into a predicate.

2. **Unify Q_morph formula across all files (S2 + D1)** -- The spec, paper1, paper2, and code must all agree on whether Q_morph is normalized or unnormalized. The normalized version is correct (satisfies QM1). Update: spec line 425 (define Q_morph as normalized), spec line 866, paper2 line 200, code docstring line 67.

3. **Fix T7-Enhanced overstatement in spec (S1)** -- Change "energy barriers" to "minimum Hessian eigenvalue" or "local curvature" to match the paper's honest qualification.

4. **Fix paper1 Open Problem 5 terminology (N3)** -- The Sep_old/Sep_new naming is confusing. Clarify that Sep = 1 - E_sep/m holds for the current u-weighted formulation.

5. **Fix paper2 Persist formula (S6)** -- Paper2's Persist formula should match the spec, or the discrepancy should be explained (e.g., "this is a simplified illustration").

6. **Address theta_support (S3)** -- Either specify theta_support, prove it exists for a range of values, or explicitly mark A1' as parametrically incomplete.

7. **Address beta_crit scaling (S5)** -- Add a remark in the spec and papers noting that the phase transition condition is asymptotically vacuous on expanding graphs, and discuss implications.

8. **Address Hessian normalization discrepancy (D5)** -- Explain why the theoretical lambda_sep/lambda_bd ~ 10^-5 disagrees with the experimental sweet spot at ~1.0.

9. **Clean up dead code (N2)** -- Remove unused `resolvent_diagonal` import from diagnostics.py.

10. **Clarify Paper1 Prop 3.5 status (D4)** -- Add a sentence noting that the Sep Covariance Identity concerns the rejected C-weighted formulation, not the current Sep.
