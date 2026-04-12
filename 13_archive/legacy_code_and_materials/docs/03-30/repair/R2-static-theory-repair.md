# R2: Static Theory Repair Plan

**Author:** Static-Theory Repair Architect
**Date:** 2026-03-30
**Input:** A1 static math audit, A4 scaling audit, SYNTHESIS.md, Canonical Spec v2.0, R8, R12, R13

---

## Executive Summary

The static single-formation theory has a strong core: T1, T6a/b, T8-Core, T14, T-A2, T20 are rigorous. The repair work falls into three tiers: (1) restatements that fix conceptual errors without new math, (2) completable proofs where the tools exist, and (3) items that should be downgraded because proving them would require disproportionate effort or because the claimed result is simply wrong. This document addresses each gapped item with options, recommendations, and priority.

---

## I. Item-by-Item Repair Analysis

### 1. T7 — Enhanced Metastability (CONCEPTUAL ERROR)

**Problem:** The proof equates "larger minimum Hessian eigenvalue" with "deeper energy basin." Hessian curvature at a minimizer measures local bowl shape, not saddle-point barrier height. These are independent quantities.

**Option A — Restate as Hessian curvature result.**
Claim: "The minimum eigenvalue of the constrained Hessian at local minimizers of E is strictly larger than that of E_bd alone, by at least lambda_cl * 2(1 - ||J_Cl||_op)^2." This is what the existing proof actually establishes. No new math needed.

**Option B — Prove a genuine barrier result.**
Would require: (i) identifying the lowest saddle point on the separatrix of the basin of attraction in the full energy landscape, (ii) showing that adding E_cl raises this saddle. This is a Morse-theoretic analysis of the energy landscape on Sigma_m — substantially harder than anything else in the theory. The saddle point structure changes when E_cl is added, so there is no simple comparison.

**Option C — Prove a quadratic-approximation barrier result.**
Claim: "Within a ball of radius r around the minimizer, the energy barrier (minimum energy needed to escape) is at least (lambda_cl * (1 - a_cl/4)^2) * r^2 higher for SCC than for Allen-Cahn." This is a weaker but honest claim that follows directly from the Hessian eigenvalue bound. It says the *local* barrier is deeper, while remaining silent about the *global* barrier.

**Recommendation: Option A (priority), supplemented by Option C as a remark.**
- Option A is immediate (rewrite one paragraph) and makes the "4-17x deeper basins" experimental claim interpretable as "4-17x larger minimum Hessian eigenvalue," which is what the experiments actually measure.
- Option C adds value as a corollary at minimal cost.
- Option B is not worth pursuing — it would be a full paper and may not even yield the desired inequality.

**Priority: 1 (CRITICAL — current statement is wrong)**

**Likely failure point:** None for Option A — it's a restatement of what's already proved.

---

### 2. Proto-Cohesion: Theorem vs. Supported Conjecture

**Problem:** R8 claims "PROVED" but the audit reveals: T8-Core gives non-trivial minimizer for E_bd only. Steps 3-5 (Bind >= threshold, Sep >= threshold, Inside >= threshold at the full-energy minimizer) have directional arguments but no quantitative bounds. The forward predicate-energy bridge (low E_component -> high predicate) is proved, but bounding E_cl and E_sep at the *joint* minimizer is not done.

**Option A — Prove quantitative bounds via KKT analysis.**
At a minimizer of E on Sigma_m, the KKT conditions give:
  lambda_cl * grad(E_cl) + lambda_sep * grad(E_sep) + lambda_bd * grad(E_bd) = mu * 1 + nu
where nu handles box constraints. For large lambda_cl relative to lambda_sep, lambda_bd, the closure gradient must be small (otherwise it dominates and the KKT condition can't balance). This gives ||grad(E_cl)|| = O(lambda_bd / lambda_cl), and since grad(E_cl) = 2(J_Cl - I)^T(Cl(u) - u), the residual ||Cl(u) - u|| = O(lambda_bd / (lambda_cl * (1 - a_cl/4))). Combined with the Cauchy-Schwarz bound Bind >= 1 - sqrt(E_cl/n), this yields:

  **Bind >= 1 - C * (lambda_bd / lambda_cl) * (1/(1 - a_cl/4))**

for a computable constant C. This is a genuine quantitative bound. The same approach for E_sep gives Sep_old bounds but requires bounding ||grad(E_sep)|| relative to the other terms.

**Proof route for Bind:** The key insight is that at a minimizer, the gradient of each energy term is constrained by the gradients of the others via the KKT equation. Large lambda_cl forces small E_cl residual. This is provable with existing tools (just careful estimates on the gradient norms).

**Proof route for Sep:** Harder. The Sep bound requires showing D(x) is close to 1 on interior sites. This follows from the distinction operator's structure IF the field has sharp boundaries (Gamma-convergence gives this in the limit). At finite parameters, we need: (i) the field is approximately binary (from E_bd at the minimizer — bounded by compactness), (ii) D responds correctly to approximately binary fields (from the sigmoid analysis with a_D large enough). This is provable but requires more careful bookkeeping.

**Proof route for Inside:** Hardest. Q_morph = l_max * Artic depends on the persistence diagram, which is a global topological property. The only route is: in the Gamma-limit, minimizers are characteristic functions of connected sets, giving l_max -> 1, Artic -> 1. At finite parameters, the persistence stability theorem gives |Q_morph(u) - Q_morph(chi_S)| <= C * ||u - chi_S||_infty, and Gamma-convergence bounds ||u - chi_S||. But this chain has multiple approximation steps and the constants may be poor.

**Option B — Downgrade to "supported conjecture with partial analytical basis."**
State: "T8-Core proves non-trivial minimizer existence. The Cauchy-Schwarz bound and KKT gradient balance provide directional evidence for predicate satisfaction. Quantitative threshold bounds are demonstrated computationally (Bind > 0.85, Sep > 0.87, Inside > 0.88 across all tested parameter regimes) but are not analytically proved."

**Option C — Hybrid: prove Bind bound, conjecture Sep/Inside.**
The Bind bound (Option A, first route) is genuinely provable with a clean argument. Sep and Inside are harder. Split the claim: "Bind >= 1 - C * lambda_bd/lambda_cl is proved (Theorem X). Sep and Inside satisfaction at minimizers is supported by computation and asymptotic arguments (Gamma-limit) but lacks finite-parameter analytical bounds."

**Recommendation: Option C.**
- The Bind bound via KKT gradient balance is the lowest-hanging fruit in the entire repair agenda. It converts the weakest part of the theory's central claim into a genuine theorem.
- Sep and Inside bounds are provable in principle but the chain of estimates is long and the constants may not be useful. Downgrading these to "demonstrated" is honest and appropriate.
- This gives the proto-cohesion result a precise status: "Non-trivial minimizer exists (T8-Core, proved). Bind satisfaction is proved quantitatively. Sep and Inside satisfaction is demonstrated computationally and supported by asymptotic analysis."

**Priority: 1 (the theory's central claim)**

**Likely failure point for Bind proof:** Bounding the non-closure gradient terms at the minimizer. The E_bd gradient is 4*alpha*L*u + beta*W'(u), which depends on the minimizer's structure. Need: ||grad(E_bd)||_2 <= C * sqrt(n) * max(4*alpha*lambda_max(L), beta*max|W'|). Since W'(u) = 2u(1-u)(1-2u) <= 2/(3*sqrt(3)) and lambda_max(L) is bounded for bounded-degree graphs, this is manageable.

---

### 3. T8-Full: IFT Argument

**Problem:** T8-Core proves non-trivial minimizer for E_bd. T8-Full needs to show this survives when lambda_cl * E_cl + lambda_sep * E_sep is added as a perturbation.

**Option A — Write the IFT argument.**
The standard approach: at the T8-Core minimizer u*, the constrained Hessian H_bd|_T is non-degenerate (all eigenvalues nonzero — positive at the minimizer). The perturbation lambda_cl * E_cl + lambda_sep * E_sep is smooth on Sigma_m. By the implicit function theorem for constrained optimization, for lambda_cl, lambda_sep sufficiently small, the perturbed energy has a critical point u*(lambda_cl, lambda_sep) smoothly depending on the perturbation parameters, and it remains a local minimizer (Hessian stays positive-definite by continuity).

**What needs to be checked:**
1. Non-degeneracy of H_bd at u*: The constrained Hessian restricted to T(Sigma_m) must be positive-definite. At the T8-Core minimizer, this is not automatically guaranteed — T8-Core only proves u* is non-uniform and is the *global* minimizer (which might be degenerate). Need: the global minimizer of E_bd on Sigma_m has a non-degenerate constrained Hessian. This is generically true but not proved for specific graphs.

2. Lambda bound: The IFT gives a neighborhood in (lambda_cl, lambda_sep) space where the perturbed minimizer exists. The size of this neighborhood depends on the minimum Hessian eigenvalue of H_bd at u* and the Hessian norms of E_cl, E_sep. This gives:
   lambda_cl < delta_1(graph, params), lambda_sep < delta_2(graph, params).

**Option B — State as conditional on non-degeneracy.**
"If the T8-Core minimizer has a non-degenerate constrained Hessian, then for lambda_cl, lambda_sep sufficiently small, the full energy has a nearby non-uniform local minimizer." This is a standard one-paragraph IFT application. The non-degeneracy hypothesis is generically satisfied (degenerate critical points form a set of measure zero in parameter space by Sard's theorem).

**Recommendation: Option B.**
- Writing the full IFT argument is straightforward but requires specifying the lambda bound explicitly, which depends on graph-specific quantities (Hessian eigenvalues at u*) that are not available in closed form.
- The conditional statement is clean, honest, and standard. The non-degeneracy hypothesis is mild (generically satisfied).
- Add a remark: "The experiments confirm that full-energy minimizers exist at the default parameters, validating the non-degeneracy hypothesis computationally."

**Priority: 2 (important but not blocking — T8-Core alone is already a strong result)**

**Likely failure point:** Non-degeneracy might fail at specific symmetry points (e.g., on highly symmetric graphs where the T8-Core minimizer has a discrete symmetry group, causing Hessian eigenvalue multiplicity). This is a non-generic but not impossible scenario.

---

### 4. C3'' — Resolvent Monotonicity

**Problem:** The claim is that the resolvent diagonal C(x,x) = [(I - alpha * W_sym)^{-1}]_{xx} increases when u(x) increases (other values fixed). The Neumann series gives C(x,x) = 1 + alpha * W_sym(x,x) + alpha^2 * (W_sym^2)(x,x) + ... Each term (W_sym^k)(x,x) sums over length-k closed paths from x to x. When u(x) increases, sqrt(u(x)) increases in the numerator of W_sym entries involving x, but the degree normalization d_x also increases, creating a competing effect.

**Option A — Complete the symmetrization calculus.**
The key derivative: d/du(x) of W_sym(x,y) for y ~ x (neighbors of x). Write W_sym = D^{-1/2} * W_tilde * D^{-1/2} where W_tilde(x,y) = sqrt(u(x)) * N(x,y) * sqrt(u(y)) and D = diag(row sums of W_tilde). Then:

d W_sym(x,y) / d u(x) = d/du(x) [W_tilde(x,y) / sqrt(D_x * D_y)]

For the diagonal: W_sym(x,x) = W_tilde(x,x) / D_x. If the kernel includes self-loops (K(x,x) > 0), then W_tilde(x,x) = u(x) * K(x,x) and D_x = sum_y sqrt(u(x)) * N(x,y) * sqrt(u(y)). The derivative involves:
- Numerator increases: d/du(x) [u(x) * K(x,x)] = K(x,x)
- Denominator increases: d/du(x) [D_x] > 0

The sign of the total depends on whether the numerator growth rate exceeds the denominator growth rate. For the first-order term alpha * W_sym(x,x), this is a concrete calculus problem. For higher-order terms, the competing effects compound.

**Estimated difficulty:** The first-order term (k=1) is tractable. The general k-th term requires showing that the positive effect of more weight on x-to-x paths dominates the negative effect of increased normalization. This is plausible when u(x) is not the dominant contributor to d_x (i.e., when the graph has many neighbors), but may fail when x has few neighbors with high u values.

**Option B — Weaken C3'' to "C3''-weak: monotonicity for alpha sufficiently small."**
For small alpha, the Neumann series is dominated by the first-order term. If the first-order term's derivative is positive (provable under reasonable graph conditions), the total derivative is positive for alpha below a threshold. This is a weaker but provable statement.

**Option C — Replace C3'' with a different monotonicity axiom.**
Instead of requiring monotonicity of the diagonal, require: "C(x,x) is larger when u(x) > 0 than when u(x) = 0, for any fixed values of u at other sites." This is a one-sided comparison (u(x) > 0 vs u(x) = 0) rather than full monotonicity. It captures the essential meaning ("participating sites have higher self-co-belonging") without requiring the derivative to be positive everywhere.

**Recommendation: Option B, with Option C as fallback.**
- Option A is likely provable for the k=1 term but the general case may require graph-specific conditions (minimum degree, bounded degree ratio). This makes it an incomplete theorem.
- Option B gives a clean result: "For alpha * rho(W_sym) < alpha_0 (a computable threshold), C3'' holds." Since alpha is already required to be small for convergence (alpha * rho(W_sym) < 1), this is a tighter but compatible condition.
- If Option B encounters technical obstacles, Option C preserves the axiom's spirit without the full monotonicity claim.

**Priority: 3 (important for axiom completeness, not blocking for the main results)**

**Likely failure point:** The degree normalization D_x may dominate for high-degree nodes, making the monotonicity fail for specific graph topologies (e.g., star graphs where the center has much higher degree than leaves).

---

### 5. A1' theta_support: Specify or Remove

**Problem:** A1' (conditional extensivity) requires (P_t u)(x) >= theta_support * u(x) as a precondition, but theta_support is never specified. T20 claims A1' is satisfied without specifying the threshold, making the axiom vacuously true for theta_support = 0.

**Option A — Specify theta_support = eta_cl (the aggregation weight).**
Rationale: A1' says "if the neighborhood supports x enough, closure should increase x's cohesion." The natural threshold is: "x's neighbors provide at least as much support as x's self-retention." Since the closure input is (1-eta_cl)*u(x) + eta_cl*(P_t u)(x), the aggregation contributes at least eta_cl*(P_t u)(x). Requiring (P_t u)(x) >= eta_cl * u(x) means the neighborhood contributes at least eta_cl^2 * u(x) to the total, which is the regime where closure extension is natural.

**Option B — Remove theta_support from the axiom system.**
A1' was introduced because A1 (unconditional extensivity) was incompatible with A3. But A1' with unspecified theta_support is vacuous. If the axiom can't be meaningfully parameterized, it should be removed and replaced with the honest statement: "Closure is not unconditionally extensive. It is extensive in regimes where neighborhood support exceeds self-support, and contractive otherwise. This is a feature, not a bug: regions without neighborhood support should not gain cohesion."

**Option C — Replace A1' with a qualitative axiom.**
"A1'': There exists a non-empty open set of fields u such that Cl_t(u)(x) > u(x) for all x in a non-trivial subset of X_t." This is provable (just exhibit such a field — any field with all values in (0, sigma(a_cl * (0.5 - tau_cl)))) and non-vacuous.

**Recommendation: Option B.**
- The original A1 was a natural requirement (closure should support cohesion). Its failure for sigmoid closure is a genuine property of the operator, not a defect.
- A1' with unspecified theta_support is worse than no axiom at all — it's a placeholder that pretends to be a constraint.
- Removing A1' and replacing with the qualitative remark is the most honest approach. The closure's behavior is fully characterized by T6a/b and T-A2; adding a conditional extensivity axiom doesn't strengthen the theory.
- If the axiom system must have an extensivity-type axiom, Option C is clean and provable.

**Priority: 4 (axiom hygiene, not mathematically blocking)**

**Likely failure point:** None — this is a definitional choice, not a proof task.

---

### 6. beta_crit -> 0 at Scale

**Problem:** The phase transition threshold beta_crit = 4*alpha*lambda_2/|W''(c)| vanishes as the graph grows (lambda_2 ~ 1/k^2 for k x k grid). On a 100x100 grid, beta_crit ~ 0.006. The theory's central prediction — "formations emerge when beta > beta_crit" — is trivially satisfied on large graphs.

**Option A — Find a scale-invariant criterion.**
Replace the absolute parameters (alpha, beta) with intensive (per-site) quantities. Define:
- alpha_hat = alpha * lambda_max(L) (dimensionless smoothness weight)
- beta_hat = beta * |W''(c)| (dimensionless double-well weight)
The phase transition condition becomes beta_hat/alpha_hat > 4 * lambda_2/lambda_max(L). For grid graphs, lambda_2/lambda_max ~ 1/k^2 * 1/8 = 1/(8k^2), so this ratio still vanishes.

**The fundamental issue:** On large graphs, lambda_2 is small because the graph has long-range modes that are nearly zero-cost to excite. The smoothness penalty can't prevent large-scale variations. This is not a defect of the theory — it's a physical fact: on large domains, diffuse modulations are always cheap.

**Option B — Scale alpha with n to maintain a meaningful threshold.**
Set alpha = alpha_0 * n (or alpha = alpha_0 / lambda_2). Then beta_crit = 4*alpha_0*n*lambda_2/|W''(c)|. For grid graphs, n*lambda_2 ~ pi^2, giving beta_crit = 4*alpha_0*pi^2/|W''(c)| = O(1). This is a deliberate parameter choice, not a theorem.

**Option C — Restrict claims to finite graphs with explicit lambda_2.**
State honestly: "The phase transition theorem is meaningful on graphs where lambda_2 is bounded below (e.g., expander graphs, fixed-size grids). On large grid-like graphs, lambda_2 -> 0 and the threshold is trivially exceeded. In this regime, formation quality (measured by the diagnostic vector) replaces the phase transition as the meaningful criterion."

**Option D — Introduce a quality-aware phase transition.**
Instead of "does a non-trivial minimizer exist?" (which is trivially yes on large graphs), ask "does a minimizer exist with diagnostic vector d above a threshold?" This requires the quantitative bounds from Item 2 (proto-cohesion), making it a downstream result.

**Recommendation: Option C, with Option D as a long-term goal.**
- Option A fails because no rescaling can fix the fundamental issue that lambda_2 -> 0.
- Option B works but is ad hoc — it's parameter tuning disguised as theory.
- Option C is honest and correct. The phase transition theorem is genuinely informative on graphs where lambda_2 = Omega(1) (bounded-degree expanders, small graphs, graphs with spectral gaps). On large grids, it's the diagnostic vector that carries the information, not the phase transition.
- Option D is the right long-term goal but requires solving Item 2 first.

**Priority: 2 (affects the theory's interpretive claims on real-world graphs)**

**Likely failure point:** Option C requires careful language to avoid the impression that the theory breaks on large graphs. It doesn't break — formations still exist and have good diagnostics. The phase *transition* criterion just becomes vacuous while the *formations* remain meaningful.

---

### 7. T7 Restatement (What Exactly?)

This is the positive counterpart to Item 1's fix. Once T7 is correctly restated as a Hessian curvature result, what should it claim?

**Recommended statement:**

> **Theorem (Hessian Enhancement).** Let u* be a local minimizer of E on Sigma_m such that u* is near the closure fixed point (||u* - Cl(u*)|| < delta). Then the minimum eigenvalue of the constrained Hessian H_E|_{T(Sigma_m)} at u* satisfies:
>
> lambda_min(H_E) >= lambda_min(H_{E_bd}) + lambda_cl * 2(1 - ||J_Cl(u*)||_op)^2 - R(delta)
>
> where R(delta) -> 0 as delta -> 0. In particular, the self-referential closure term makes the energy landscape strictly more curved at formation-structured minimizers than the Allen-Cahn energy alone.

**Experimental restatement:** The "4-17x deeper basins" should become "4-17x larger minimum Hessian eigenvalue" or equivalently "4-17x greater local curvature at the energy minimum."

**Priority: 1 (paired with Item 1)**

---

### 8. T11 — Gamma-Convergence: Standard vs. Novel

**Problem:** The leading-order Gamma-limit (Modica-Mortola on graphs) is standard. The claim that self-referential terms "modify the surface tension" is incorrect as a Gamma-limit statement — they are O(1) perturbations that vanish in the limit.

**Option A — Separate the standard from the novel.**
Theorem (Standard): As epsilon = alpha/beta -> 0, E_bd Gamma-converges to sigma_AC * |partial S|_G. (Reference: Modica-Mortola on graphs, well-known.)
Proposition (Novel): At finite epsilon, the self-referential terms E_cl and E_sep contribute O(1) corrections to the pre-limit energy. These corrections break the exact Z_2 symmetry of Allen-Cahn (u <-> 1-u) because the operators Cl and D are not Z_2-symmetric. Consequence: the optimal volume fraction at finite epsilon depends on lambda_cl, lambda_sep, which is a genuinely novel effect.

**Option B — Drop the surface tension claim entirely.**
State only the standard Gamma-convergence result for E_bd, and note that E_cl and E_sep are bounded perturbations that do not affect the Gamma-limit but influence finite-parameter behavior.

**Recommendation: Option A.**
- The Z_2 symmetry breaking is genuinely novel and mathematically clean. Allen-Cahn has u <-> 1-u symmetry; SCC breaks it because sigma(a*(1-eta)*u + ...) is not symmetric under u <-> 1-u. This gives a concrete, provable, novel prediction.
- The "modified surface tension" claim should be replaced with "broken Z_2 symmetry at finite epsilon."

**Priority: 3 (cleanup, not urgent)**

**Likely failure point:** None — this is a restatement.

---

### 9. Predicate-Energy Bridge: Reverse Direction

**Problem:** The bridge is one-way: low E -> high diagnostics (proved). High diagnostics -> low E (fails — a field can satisfy all predicates while having high energy).

**Option A — Prove reverse under additional hypotheses.**
If the field is constrained to be a minimizer (not just any field), then high diagnostics might imply low energy relative to other minimizers. But this is circular — minimizers already have the lowest energy by definition.

**Option B — Accept one-way and explain why.**
The forward direction is the useful one: the energy is the optimization target, and the diagnostics are the interpretive readout. Asking "if diagnostics are high, must energy be low?" conflates the optimization objective with the diagnostic. A field can satisfy Bind, Sep, Inside while having suboptimal boundary morphology (high E_bd) — the diagnostics don't measure morphological efficiency.

**Option C — Prove a conditional reverse: high diagnostics + minimality -> bounded energy.**
"Among all fields on Sigma_m with d >= d_0 (component-wise), the energy is bounded: E <= E_max(d_0, graph, params)." This is a constrained optimization problem: minimize E subject to d >= d_0 on Sigma_m. The bound exists trivially (Sigma_m is compact, d >= d_0 defines a closed subset, E is continuous). But this says nothing useful beyond existence.

**Recommendation: Option B.**
- The one-way bridge is not a defect. It's the natural direction: energy minimization produces formations, and diagnostics verify their quality. The reverse (diagnostics constrain energy) is not how the theory is used.
- State explicitly: "The predicate-energy bridge is forward-only by design. Energy minimization is the generative mechanism; the diagnostic vector is the interpretive lens. They play complementary roles, not symmetric ones."
- This is honest, philosophically coherent, and requires no new math.

**Priority: 4 (interpretive clarity, not mathematical)**

**Likely failure point:** None.

---

### 10. QM1 — Vanishing on Uniform Fields (FALSE)

**Problem:** QM1 claims Q_morph = 0 on uniform fields. But for u = c * 1 with c > 0, the superlevel-set filtration gives a single component that persists from threshold 0 to threshold c, so l_max = c, not 0. And if there's only one bar, Artic = 1. So Q_morph = c * 1 = c != 0.

**Option A — Redefine Q_morph to subtract baseline.**
Q_morph_new = max(0, l_max - c) * Artic, where c = m/n is the volume fraction. For uniform fields, l_max = c and Q_morph_new = 0. For well-formed formations with l_max close to 1, Q_morph_new = (1-c) * Artic.

**Option B — Redefine using normalized persistence.**
Q_morph_new = (l_max - c)/(1 - c) * Artic. This normalizes to [0,1] and gives 0 on uniform fields, 1 on ideal characteristic functions.

**Option C — Change QM1 to "Q_morph is minimized on uniform fields."**
This is true: uniform fields give Q_morph = c, while well-formed formations give Q_morph close to 1. The axiom becomes: Q_morph achieves its minimum value c at uniform fields.

**Recommendation: Option B.**
- It fixes QM1 while preserving QM2-QM4.
- The normalization (l_max - c)/(1-c) maps [c, 1] -> [0, 1], giving a clean range.
- For the current experiments, this changes Inside values from ~0.88 to ~(0.88 - 0.25)/(1 - 0.25) = ~0.84. The qualitative story is unchanged.
- Update the code and spec simultaneously.

**Priority: 1 (CRITICAL — false theorem in the registry)**

---

## II. Priority Ranking

| Rank | Item | Type | Effort | Impact |
|------|------|------|--------|--------|
| 1 | T7 restatement (Items 1, 7) | Rewrite | 1 day | Fixes wrong theorem |
| 1 | QM1 fix (Item 10) | Redefine + code | 1 day | Fixes false theorem |
| 1 | Proto-cohesion Bind bound (Item 2, partial) | New proof | 3-5 days | Upgrades central claim |
| 2 | T8-Full IFT (Item 3) | Write proof | 2-3 days | Completes phase transition |
| 2 | beta_crit scaling (Item 6) | Analysis + text | 2-3 days | Honest scaling claims |
| 3 | C3'' monotonicity (Item 4) | Complete calculus | 3-5 days | Axiom completeness |
| 3 | T11 standard/novel split (Item 8) | Rewrite | 1 day | Accurate claims |
| 4 | A1' theta_support (Item 5) | Decision | 0.5 day | Axiom hygiene |
| 4 | Bridge reverse direction (Item 9) | Text | 0.5 day | Interpretive clarity |

---

## III. Proof Sketches for Top-Priority New Results

### Bind Quantitative Bound (Rank 1, new math)

**Theorem.** Let u* minimize E = lambda_cl * E_cl + lambda_sep * E_sep + lambda_bd * E_bd on Sigma_m with 0 < u*_i < 1 for all i. Then:

  Bind(u*) >= 1 - (1/sqrt(n)) * (lambda_bd * G_bd + lambda_sep * G_sep) / (lambda_cl * 2(1 - a_cl/4))

where G_bd = ||Pi_T(grad E_bd(u*))||_2 (projected gradient norm of E_bd at u*) and G_sep = ||Pi_T(grad E_sep(u*))||_2.

**Proof sketch:**
1. At the minimizer, KKT gives: lambda_cl * grad(E_cl) + lambda_sep * grad(E_sep) + lambda_bd * grad(E_bd) = mu * 1.
2. Project onto T(Sigma_m): lambda_cl * Pi_T(grad E_cl) = -lambda_sep * Pi_T(grad E_sep) - lambda_bd * Pi_T(grad E_bd).
3. Take norms: lambda_cl * ||Pi_T(grad E_cl)|| <= lambda_sep * G_sep + lambda_bd * G_bd.
4. Now grad E_cl = 2(J_Cl - I)^T(Cl(u) - u). The projected gradient has norm >= 2(1 - ||J_Cl||_op) * ||Cl(u) - u|| (since (I - J_Cl)^T is invertible with min singular value >= 1 - a_cl/4, and projection onto T only removes one dimension).
   - **Subtlety:** The projection onto T removes the constant direction. Need: ||(I - J_Cl)^T r - mean((I - J_Cl)^T r) * 1|| >= (1 - a_cl/4) * ||r - mean(r) * 1|| - ||mean((I - J_Cl)^T r) * 1||. This requires more careful estimation. The key bound is ||Pi_T((I - J_Cl)^T r)|| >= (1 - a_cl/4 - 1/n) * ||r|| for ||r|| not aligned with 1 direction. For well-formed formations, Cl(u) - u has near-zero mean (it's positive on boundary and negative elsewhere, approximately canceling). So the projection is mild.
5. Combining: ||Cl(u*) - u*|| <= (lambda_bd * G_bd + lambda_sep * G_sep) / (2 * lambda_cl * (1 - a_cl/4 - epsilon)).
6. Cauchy-Schwarz: Bind = 1 - ||Cl(u*) - u*||/sqrt(n) >= 1 - (lambda_bd * G_bd + lambda_sep * G_sep) / (2 * lambda_cl * (1 - a_cl/4 - epsilon) * sqrt(n)).
7. Bound G_bd: ||grad E_bd||_2 = ||4*alpha*L*u* + beta*W'(u*)||_2 <= 4*alpha*||L||_op*sqrt(n) + beta*max|W'|*sqrt(n). Since ||L||_op = lambda_max(L) and max|W'| = 2/(3*sqrt(3)), this gives G_bd = O(sqrt(n)).
8. Final bound: Bind(u*) >= 1 - C * (lambda_bd + lambda_sep) / lambda_cl for a computable graph-dependent constant C.

**This is provable.** The main technical step is step 4 (lower bounding the projected gradient norm of E_cl). The rest is standard.

### T8-Full IFT (Rank 2)

**Theorem.** Let u* be a non-degenerate local minimizer of E_bd on Sigma_m (i.e., H_{E_bd}|_T has all positive eigenvalues, min eigenvalue = lambda_min > 0). Then for lambda_cl, lambda_sep < lambda_min / (2 * max(||H_{E_cl}||, ||H_{E_sep}||)), the full energy E has a local minimizer u*(lambda_cl, lambda_sep) with ||u* - u*(lambda_cl, lambda_sep)|| = O(lambda_cl + lambda_sep).

**Proof sketch:** Standard IFT for constrained optimization. The map F(u, lambda) = Pi_T(grad E(u; lambda)) satisfies F(u*, 0) = 0 and D_u F(u*, 0) = H_{E_bd}|_T is invertible. Apply IFT to get a smooth curve of critical points. The Hessian at (u*(lambda), lambda) = H_{E_bd} + lambda_cl * H_{E_cl} + lambda_sep * H_{E_sep} remains positive-definite for small lambda because the perturbation is O(lambda) and the minimum eigenvalue is lambda_min > 0.

**This is a routine IFT application.** The only subtlety is that the Hessian norms of E_cl and E_sep at u* are needed, which are bounded but not computed in closed form.

---

## IV. Items NOT Recommended for Proof

### Reverse predicate-energy bridge
The asymmetry is structural, not a gap. Accept it.

### T-Persist-2 (transport concentration)
Requires new technical machinery (concentration inequalities for optimal transport on graphs). Defer to temporal theory phase.

### b_D = 0 expressiveness justification
The b_D = 0 choice is motivated by analyticity (T14). The "expressiveness" question (does the theory lose something by dropping the gradient term?) is an empirical question best answered by experiments, not proofs.

### Full barrier height comparison (T7 as barrier)
Morse-theoretic analysis of the saddle structure is a multi-month project with uncertain payoff. The Hessian restatement is sufficient.

---

## V. Recommended Work Order

**Week 1: Emergency fixes (no new proofs)**
1. Restate T7 as Hessian curvature result (Item 1/7)
2. Fix QM1 with normalized persistence (Item 10)
3. Write the T11 standard/novel split (Item 8)
4. Remove or replace A1' theta_support (Item 5)
5. State predicate-energy bridge one-way design (Item 9)

**Week 2: Completable proofs**
6. Prove the Bind quantitative bound (Item 2 partial) — this is the highest-value new math
7. Write T8-Full IFT argument (Item 3)
8. Write the beta_crit scaling analysis and honest claims (Item 6)

**Week 3: Harder completions**
9. Attempt C3'' first-order monotonicity (Item 4, Option B)
10. If C3'' first-order works, attempt general case; otherwise adopt Option C fallback
11. Downgrade proto-cohesion status: "Bind bound proved; Sep/Inside demonstrated"

**Outcome:** After 3 weeks, the static theory would have:
- 0 false theorems (T7, QM1 fixed)
- 1 new quantitative theorem (Bind bound at minimizers)
- 1 completed proof (T8-Full, conditional on non-degeneracy)
- Honest scaling claims (beta_crit)
- Clean axiom system (A1' resolved, C3'' addressed)
- Accurate Gamma-convergence claims (T11)
- Transparent proto-cohesion status: proved backbone + proved Bind + demonstrated Sep/Inside
