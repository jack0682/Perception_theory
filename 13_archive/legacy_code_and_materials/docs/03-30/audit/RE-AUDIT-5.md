# RE-AUDIT-5: Cycle 6 Final Adversarial Audit

**Date:** 2026-03-27
**Scope:** Full cross-file formula verification, code execution, residual C_t issues, hostile reviewer simulation
**Auditor stance:** Maximally adversarial -- harshest possible reading, zero benefit of the doubt

**Previously fixed (verified correct in this audit):**
- C1: Sep u-weighted, T7 Hessian curvature, QM1 normalized, Transport conditional, autopoiesis language, MFG citation
- C2: BUG-1 Hessian factor, C_t demoted in spec, beta_crit caveat, T-Bind added
- C3: converged flag honest, triad->pair, resolvent guard
- C4: project_volume Euclidean, BUG-3 lambda_2, diagnostics re-verified
- C5: projection early-exit fix, "4-17x" -> "1.2-13x", paper2 C_t intro/equation/autopoiesis, T4 Gauss-Newton qualification, Gestalt table C_t diagnostic, projection description updated

---

## VERIFIED CORRECT

### V1. Cross-file formula consistency: ALL energy terms match

| Formula | Spec | Paper1 | Paper2 | Code |
|---------|------|--------|--------|------|
| E_cl = \|\|u - Cl(u)\|\|^2 | Sec 8.2 | Eq 6 (L221) | Eq 4 (L270) | energy.py:72-74 |
| E_sep = sum u(1-D) | Sec 8.3 | Eq 7 (L228) | Eq 5 (L277) | energy.py:94-97 |
| E_bd = alpha*sum_ord N(u_x-u_y)^2 + beta*sum W(u) | Sec 8.4 | Eq 8 (L242) | Eq 6 (L284) | energy.py:46-54 |
| Cl(u)(x) = sigma(a_cl*((1-eta)*u + eta*Pu - tau)) | Sec 9.2 | Eq 3 (L164) | Sec II-B | operators.py:49-60 |
| D(x;1-u) = sigma(a_D*(Pu - lam_D*P(1-u)) - tau_D) | Sec 9.3 | Eq 4 (L185) | Sec II-C | operators.py:109-120 |
| C_t = (I - alpha*W_sym)^{-1} | Sec 9.4 | Eq 5 (L198) | Eq 2 (L231) | operators.py:163-202 |
| Bind = 1 - \|\|u-Cl(u)\|\|_2 / sqrt(n) | Sec 7.1 | Eq 9 (L256) | Sec II-E | diagnostics.py:39-48 |
| Sep = sum(u*D) / sum(u) | Sec 7.1 | Eq 10 (L261) | Sec II-C | diagnostics.py:51-63 |
| Inside = (l_max - c)/(1-c) * Artic | Sec 7.1 | Eq 11 (L267) | N/A (simplified) | diagnostics.py:66-82 |
| Phase transition: beta/alpha > 4*lam2/\|W''(c)\| | T8-Core | Thm 3 (L337) | N/A | params.py:118-123 |

ALL formulas are consistent across all four sources. No cross-file discrepancies found.

### V2. Gradient formulas: code matches theory

- grad_bd = 4*alpha*L*u + beta*W'(u) where W'(u) = 2u(1-u)(1-2u): energy.py:57-64. Correct.
- grad_cl = 2*(J_Cl^T - I)*(Cl(u)-u): energy.py:77-87. Uses exact Jacobian transpose. Correct.
- grad_sep = (1-D) - J_D^T @ u: energy.py:100-108. Correct.
- Hessian normalization: sigma_bd computed from max(|4*alpha*lam_max_L + beta*W''(c)|, |4*alpha*lam2_L + beta*W''(c)|): energy.py:186-196. Correct.

### V3. project_volume works correctly (C5 fix verified)

```
Test (a): u=[0.5]*10, m=5.0 -> v=[0.5]*10, sum=5.0   PASS
Test (b): u=[1.5,-0.5,0.8,0.3,0.9], m=2.0 -> sum=2.0  PASS
Test (c): u=[0]*5, m=1.0 -> v=[0.2]*5, sum=1.0         PASS
```

### V4. find_formation produces correct diagnostics

10x10 grid, beta_bd=20, volume_fraction=0.5, 5 restarts:
- Bind=0.856, Sep=0.941, Inside=0.981, Persist=1.000
- Energy=2.677, converged=False (gradient stagnation, NOT false convergence claim)
- Paper claims: Bind~0.86, Sep~0.93, Inside~0.98. Actual values match or slightly exceed.

### V5. Formal universe matches spec after C_t demotion

Spec line 61: C^soft = (T, {X_t}, {u_t}, {Cl_t}, {N_t, D_t}, {M_{t->s}})
C_t removed from formal universe. Correct.

Papers do not re-state the formal universe tuple (they describe the operators individually), so no cross-file conflict exists.

### V6. C5 fixes all verified

- Paper1 line 412: "1.2x to 13x" -- CORRECT (was 4-17x)
- Paper2 line 76: Now says "two variational operators...A third operator, co-belonging (C), depends on u but serves as a structural diagnostic" -- CORRECT
- Paper2 line 698: Now says "self-referential operator structure---self-completion (Cl) and self-contrast (D) as variational operators, with self-integration (C) as a derived diagnostic" -- CORRECT
- Paper2 line 355 (Gestalt table): "C_t (co-belonging, diagnostic)" -- CORRECT
- Paper1 line 707: Now says "exact Euclidean projection via bisection on the shift parameter (clip-and-shift algorithm)" -- CORRECT
- Paper1 line 395/412: Curvature language correct, Gauss-Newton qualification present -- CORRECT
- No "triad" language found anywhere

### V7. No import errors or deprecated patterns

All imports resolve cleanly. No deprecated patterns detected.

### V8. converged flag remains honest

optimizer.py:163-165 requires all three thresholds (rel_dE, gnorm, ds). Stagnation exit (line 176-179) does NOT set converged=True. Current 10x10 run correctly reports converged=False.

---

## STILL BROKEN

### SB-1. (MODERATE) Paper1 line 206: C_t falsely claimed to enter Sep predicate

**Location:** `paper1_math.tex:206`

**Text:** "Co-belonging enters the theory's diagnostic predicates (specifically, the separation predicate Sep) but does not enter the energy functional."

**Problem:** This is factually wrong. The separation predicate Sep (defined at line 261 in the same paper) is:

    Sep(u) = sum_x u(x) * D(x; 1-u) / sum_x u(x)

This is u-weighted. C_t does NOT appear in this formula. C_t does not enter ANY diagnostic predicate (Bind, Sep, Inside, or Persist) in the current theory. C_t is a standalone diagnostic tool -- it can be computed for structural analysis, but it is not embedded in any predicate formula.

This sentence is a stale leftover from an intermediate version where Sep was C_t-weighted (the version that was rejected because it averages ~0.5 regardless of formation quality, as noted at line 764 of the same paper).

**Severity:** MODERATE. A reviewer checking the Sep formula against the architectural claim will find a direct contradiction within the same paper.

**Fix:** Change to: "Co-belonging serves as a standalone structural diagnostic (analyzing which sites are integrated into the formation) but does not enter the energy functional or the diagnostic predicates."

### SB-2. (MODERATE) Paper1 line 78: Same stale C_t-enters-predicates claim

**Location:** `paper1_math.tex:78`

**Text:** "Co-belonging enters the theory's diagnostic predicates but not the energy functional---an architectural decision confirmed by our analysis."

**Problem:** Same as SB-1. C_t does NOT enter any diagnostic predicate. This is the Introduction section -- the first time a reader encounters the architectural claim.

**Fix:** Change to: "Co-belonging serves as a structural diagnostic but enters neither the energy functional nor the diagnostic predicates---an architectural decision confirmed by our analysis."

### SB-3. (MODERATE) Paper2 line 316: C_t still in the flow equation feeding into E

**Location:** `paper2_cogsci.tex:316`

**Equation:**
```
u -> (Cl_t, D_t, C_t) -> E -> u
```

**Problem:** This was flagged in RE-AUDIT-4 as SB-4 and was NOT fixed in C5. The arrow from `(Cl_t, D_t, C_t)` to `E` visually implies C_t feeds into the energy. The surrounding text (line 314) correctly explains that only two modes enter the energy, but the equation directly contradicts this by placing all three operators in the same arrow chain.

**Fix:** Split into two paths:
```
u -> (Cl_t, D_t) -> E -> u
u -> C_t -> d  (diagnostic)
```
Or simply remove C_t: `u -> (Cl_t, D_t) -> E -> u`

### SB-4. (LOW) Paper1 Open Problem 6 (line 845): Sep-energy identity misattributed

**Location:** `paper1_math.tex:845-847`

**Text:** "The exact bridge Sep_old = 1 - E_sep/m holds for the unweighted separation predicate."

**Problem:** The identity Sep = 1 - E_sep/m holds for the CURRENT u-weighted Sep, not just "Sep_old." Proof: Sep_u = sum(u*D)/m and E_sep = sum(u*(1-D)) = sum(u) - sum(u*D) = m - m*Sep_u, so Sep_u = 1 - E_sep/m. QED.

The spec (line 412) correctly states this: "The exact equality Sep = 1 - E_sep/m holds for this u-weighted formulation." But the paper attributes it to "Sep_old" and frames the C_t-weighted version as the problem, suggesting the current Sep does not have a clean energy bridge when in fact it does.

**Fix:** Replace with: "The exact bridge Sep = 1 - E_sep/m holds for the current u-weighted separation predicate (immediate from the definitions). The C_t-weighted alternative Sep_new does not yield a clean bridge (Proposition 1 provides a covariance decomposition but not a direct energy relationship)."

---

## ITEMS FOR HOSTILE REVIEWER

### HR-1. What a J. Math. Phys. reviewer would attack FIRST

**Target: Theorem 4 (Enhanced Metastability) proof rigor.**

The proof's claim that the Hessian of E_cl at a minimizer is 2(I - J_Cl)^T(I - J_Cl) is correct ONLY at the closure fixed point where the residual Cl(u) - u = 0. At an energy minimizer (which is NOT a closure fixed point -- the minimizer balances all three energy terms), the residual is nonzero, and the full Hessian includes second-order terms:

    H_{E_cl} = 2(I - J_Cl)^T(I - J_Cl) + 2 * sum_i (Cl(u)_i - u_i) * H_i[Cl]

Paper1 line 400 acknowledges this ("Gauss-Newton approximation, valid when the closure residual is small") and line 408 notes the self-consistency ("for large lambda_cl, the gradient balance ensures ||u - Cl(u)|| = O(1/lambda_cl)"). But a referee would correctly point out:

1. The theorem STATEMENT (line 389) does not contain the Gauss-Newton qualification -- it presents the result unconditionally.
2. The bound lambda_cl * 2(1 - ||J_Cl||)^2 is stated without the qualification that it's approximate.
3. The self-consistency argument is circular: "the conclusion holds IF the residual is small, and the residual is small IF lambda_cl is large, but lambda_cl is a free parameter."

**Recommendation:** Add "under the Gauss-Newton approximation" to the theorem statement, or prove that the second-order terms are dominated by the first-order terms at energy minimizers.

### HR-2. What a Cognitive Science reviewer would attack FIRST

**Target: The formation is driven entirely by Allen-Cahn.**

The ablation study (paper1 lines 736-741, paper2 lines 640-643) honestly shows that E_bd alone produces excellent formations (Bind=0.85, Inside=1.0). The self-referential terms (E_cl, E_sep) provide marginal refinement: Sep goes from 0.924 to 0.938. A hostile CogSci reviewer would ask: "Why should I care about the self-referential apparatus when Allen-Cahn does 95% of the work?"

Paper2 line 645 addresses this honestly ("the self-referential terms are not yet shown to be essential for formation existence"), but the abstract (line 29) and introduction (line 76) lead with the self-referential operators as the "central formal novelty." A reviewer might see a disconnect between the claims of novelty and the experimental evidence of marginal improvement.

**Recommendation:** No fix needed -- the papers are honest about this. But be prepared for this critique.

### HR-3. Sep being u-weighted is trivially related to E_sep

The identity Sep = 1 - E_sep/m means the separation predicate is a linear rescaling of the separation energy. This makes Sep diagnostically redundant with E_sep. A reviewer could argue that the "four-dimensional diagnostic vector" effectively has only three independent dimensions (Bind, Inside, Persist), with Sep being a trivial function of a known energy term. Paper1 Open Problem 6 (line 845) actually obscures this by misattributing the identity to "Sep_old."

**Recommendation:** Acknowledge this directly. The predicate-energy bridge is a feature (it validates the predicate design), not a bug. But it does reduce the diagnostic vector's effective dimensionality from 4 to 3 for fields near energy minimizers.

---

## PRIORITY RANKING

1. **SB-1 (MODERATE): Paper1 line 206 -- C_t falsely claimed to enter Sep.** Direct factual error, contradicts the Sep formula in the same paper.

2. **SB-2 (MODERATE): Paper1 line 78 -- Same C_t-enters-predicates error.** In the Introduction, highest-visibility location.

3. **SB-3 (MODERATE): Paper2 line 316 -- C_t in flow equation.** Unfixed from RE-AUDIT-4 (was SB-4). Visually implies C_t -> E.

4. **SB-4 (LOW): Paper1 Open Problem 6 misattributes Sep-energy identity.** Claims Sep = 1 - E_sep/m is for "Sep_old" when it actually holds for the current u-weighted Sep. Misleading to a reader trying to understand the predicate-energy bridge.

---

## SUMMARY

The codebase is clean. All energy formulas, gradient formulas, operator definitions, and diagnostic predicates are consistent across spec, paper1, paper2, and code. The projection algorithm works correctly. The optimizer produces results matching paper claims. All C1-C5 fixes are verified correct.

Four issues remain, all in the papers' prose (not in formulas, not in code):

- Two instances in paper1 (lines 78 and 206) where C_t is falsely claimed to enter the diagnostic predicates. This is a stale leftover from the rejected C_t-weighted Sep.
- One unfixed equation in paper2 (line 316) showing C_t feeding into the energy.
- One misattribution in paper1's Open Problem section (line 845) where the Sep-energy identity is attributed to "Sep_old" instead of the current u-weighted Sep.

None of these affect the mathematical correctness of the theorems, the code, or the experimental results. They are editorial/prose issues that would confuse a careful reader or give a hostile reviewer easy targets.

**Verdict: NOT CLEAN AUDIT.** Four issues remain, all prose-level. The mathematics, code, and cross-file formula consistency are verified correct.
