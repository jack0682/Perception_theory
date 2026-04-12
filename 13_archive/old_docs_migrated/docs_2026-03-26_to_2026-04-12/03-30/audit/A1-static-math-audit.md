# A1: Static Core Mathematics Audit

**Auditor:** Static Core Mathematics Auditor (Teammate 1)
**Date:** 2026-03-30
**Scope:** Exhaustive audit of the static single-formation variational core of SCC

---

## I. THEOREM-BY-THEOREM STATUS TABLE

| # | Theorem | Claimed Status | Actual Status | Exact Gap | Severity | Minimal Fix |
|---|---------|---------------|---------------|-----------|----------|-------------|
| T1 | Energy minimizer existence | Fully proved | **VALID** | None for E_bd; self-referential continuity unverified for full E | Low | State continuity of E_cl, E_sep explicitly |
| T6a | Closure fixed point existence | Fully proved | **VALID** | None | — | — |
| T6b | Closure contraction (unique FP) | Fully proved | **VALID with caveat** | Lipschitz bound uses ‖·‖_∞ but P_t non-expansiveness needs the right norm | Low | Verify P_t is non-expansive in ‖·‖_∞ |
| T20 | Axiom consistency | Fully proved | **VALID** | None | — | — |
| T-A2 | Monotonicity | Fully proved | **VALID** | None | — | — |
| T8-Core | Phase transition (non-trivial minimizer) | Fully proved | **VALID** | None | — | — |
| T3/T6 | Non-idempotent stability advantage | Fully proved | **OVERSTATED** | Proved at fixed point only; minimizer ≠ fixed point in general | Medium | Clarify hypothesis: result holds at u* where ‖J_Cl‖_op < 1 |
| T7 | Enhanced metastability | Fully proved | **GAP** | Hessian PD ≠ deeper basin; barrier = saddle height, not curvature | **High** | Restate as "larger minimum Hessian eigenvalue," not "deeper basin" |
| T14 | Gradient flow convergence | Fully proved | **VALID with subtlety** | Analyticity of E on Σ_m needs verification; Łojasiewicz exponent not computed | Low | Verify analyticity; acknowledge unknown exponent |
| T11 | Γ-convergence | Fully proved | **SHALLOW** | Standard on graphs; "modified surface tension" is O(1) not O(1/ε), so it's a perturbation statement, not a Γ-limit modification | Medium | Distinguish leading-order Γ-limit (standard) from perturbation (novel) |
| C-Ax | Resolvent axiom satisfaction | Fully proved (with noted gap) | **C3'' HAS GAP** | Symmetrization D^{-1/2} depends on u(x); monotonicity of diagonal not formally closed | Medium | Complete the calculus: d/du(x) of D_x^{-1/2} in the Neumann series |
| QM1-4 | Q_morph axiom satisfaction | Fully proved | **QM2 INFORMAL** | "Both factors increase with structure" is not a proof of monotonicity | Low | Provide a formal monotonicity argument or weaken to "empirically monotone" |
| T8-Full | Full-energy non-trivial minimizer | Proved with gap | **GAP CONFIRMED** | IFT step unwritten; also requires λ_sep/λ_bd constraint | Medium | Write IFT argument; state λ_sep/λ_bd bound |
| Bind bound | Bind ≥ 1 - √(E_cl/n) | Proved | **VALID** | Cauchy-Schwarz is clean | — | — |
| Sep = 1 - E_sep/m | Exact equality | Proved for Sep_old | **VALID for Sep_old ONLY** | Does NOT hold for Sep_new (C_t-weighted). Paper must not claim this for Sep_new | **High** | Clearly scope: Sep_old = 1 - E_sep/m; Sep_new relationship is open |
| Proto-cohesion existence | "Proved with caveats" | **DEMONSTRATED, NOT PROVED** | Steps 3-5 lack quantitative bounds; predicate satisfaction at minimizers is computational, not analytical | **High** | Downgrade from "theorem" to "supported conjecture with partial analytical basis" |
| Transport FP existence | Proved (Brouwer) | **GAP** | Continuity of Φ requires IFT at non-degenerate points; degeneracy not excluded | Medium | State non-degeneracy as explicit hypothesis |

---

## II. DETAILED ANALYSIS

### T1: Energy Minimizer Existence

**Claimed:** On Σ_m = {u ∈ [0,1]^n : Σu = m}, the energy E attains its minimum.

**Audit:**
- **Compactness of Σ_m ∩ [0,1]^n:** Valid. Σ_m is the intersection of a hyperplane with the compact cube [0,1]^n. For 0 < m < n, this is non-empty, closed, and bounded — hence compact in R^n.
- **Continuity of E_bd:** Valid. The smoothness term u^T L u is a quadratic form (continuous), and the double-well Σ W(u_i) is a sum of polynomials (continuous).
- **Continuity of E_cl:** The closure operator Cl_t(u) is a composition of the aggregation P_t (a rational function with ε > 0 in denominator, hence smooth) and the sigmoid (smooth). So Cl_t is smooth, and E_cl = ‖u - Cl(u)‖^2 is smooth. **Valid.**
- **Continuity of E_sep:** The distinction operator D is a composition of P_t and sigmoid (smooth when b_D = 0). E_sep = Σ u_i(1 - D_i) is a composition of smooth functions. **Valid.**
- **Extreme value theorem applies.** Continuous function on compact set attains its minimum.

**Verdict: VALID.** The proof is complete for the full energy E = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd. The self-referential nature does not break continuity because all operators are compositions of smooth functions.

---

### T6a/b: Closure Fixed Point Existence and Contraction

**Claimed:** (a) Brouwer gives existence; (b) Banach contraction at rate a_cl/4 when a_cl < 4.

**Audit of (a):** σ maps R → (0,1) ⊂ [0,1], so Cl maps [0,1]^n into (0,1)^n ⊂ [0,1]^n. Continuous self-map of compact convex set → Brouwer applies. **Valid.**

**Audit of (b):**
- The Lipschitz constant claim: ‖Cl(u) - Cl(v)‖_∞ ≤ (a_cl/4)‖u - v‖_∞.
- The chain rule gives: |Cl(u)(x) - Cl(v)(x)| ≤ max σ' · a_cl · |(1-η)(u(x)-v(x)) + η(P_t u - P_t v)(x)|.
- max σ' = 1/4 (achieved at z = 0). **Correct.**
- The term |(1-η)(u(x)-v(x)) + η(P_t u - P_t v)(x)| ≤ (1-η)‖u-v‖_∞ + η‖P_t(u-v)‖_∞.
- P_t is a row-stochastic-like matrix (sum of non-negative entries divided by their sum + ε). So ‖P_t f‖_∞ ≤ ‖f‖_∞. Actually: P_t f(x) = Σ K(x,y)f(y) / (Σ K(x,y) + ε). The denominator is Σ K(x,y) + ε, the numerator in absolute value is ≤ Σ K(x,y)|f(y)| ≤ ‖f‖_∞ · Σ K(x,y). So |P_t f(x)| ≤ ‖f‖_∞ · Σ K(x,y)/(Σ K(x,y) + ε) < ‖f‖_∞. **P_t is non-expansive in ‖·‖_∞. Valid.**
- Therefore: |(1-η)(u(x)-v(x)) + η(P_t u - P_t v)(x)| ≤ (1-η)‖u-v‖_∞ + η‖u-v‖_∞ = ‖u-v‖_∞.
- So ‖Cl(u) - Cl(v)‖_∞ ≤ (1/4) · a_cl · ‖u-v‖_∞ = (a_cl/4)‖u-v‖_∞. **Valid.**
- When a_cl < 4, the Lipschitz constant a_cl/4 < 1. Banach contraction mapping theorem on the complete metric space ([0,1]^n, ‖·‖_∞) gives unique fixed point and geometric convergence. **Valid.**

**Is the rate a_cl/4 tight?** The maximum of σ' is 1/4, achieved at z = 0. For the Lipschitz bound to be tight, we need u and v such that the pre-activation z lands at 0 for all nodes simultaneously. This is achievable (e.g., when u = v = u* with Cl(u*)(x) = 1/2 for all x, i.e., z = 0 everywhere). So the bound a_cl/4 is indeed tight as a worst-case Lipschitz constant.

**Verdict: VALID.** Clean application of standard fixed-point theory.

---

### T8-Core: Phase Transition (Non-Trivial Minimizer Existence)

**Claimed:** If β/α > 4λ₂/|W''(c)| with c in the spinodal range, the global minimizer of E_bd|_{Σ_m} is non-uniform.

**Audit of the Hessian computation:**

1. E_bd smoothness term = α Σ_{x,y} N(x,y)(u(x)-u(y))^2.
2. For symmetric N: Σ_{x,y} N(x,y)(u(x)-u(y))^2 = Σ_{x,y} N(x,y)[u(x)^2 - 2u(x)u(y) + u(y)^2] = 2 Σ_x d_x u(x)^2 - 2 Σ_{x,y} N(x,y)u(x)u(y) = 2u^T L u.
   - Here L is the standard graph Laplacian: L_{xx} = d_x = Σ_y N(x,y), L_{xy} = -N(x,y).
   - So the smoothness term = 2α u^T L u. **Correct under ordered-pair convention.**
3. Hessian of 2α u^T L u with respect to u: ∂²/∂u_i ∂u_j (2α u^T L u) = 2α · 2L_{ij} = 4α L_{ij}.
   - Wait: the Hessian of f(u) = u^T A u is 2A (not A). So Hessian of 2α u^T L u = 2 · 2α L = 4α L. **Correct.**
4. Double-well term: β Σ W(u_i) where W(u) = u²(1-u)². Hessian = β · diag(W''(u_i)). At u = c·1, this is β W''(c) I.
5. W''(u) = d²/du² [u²(1-u)²] = d/du [2u(1-u)(1-2u)] = 2[(1-u)(1-2u) + u(-1)(1-2u) + u(1-u)(-2)] = 2[(1-2u)(1-2u) - 2u(1-u)] = 2[(1-2u)² - 2u + 2u²] = 2[1 - 4u + 4u² - 2u + 2u²] = 2[1 - 6u + 6u²] = 12u² - 12u + 2. **Correct.**
6. At c = 1/2: W''(1/2) = 12/4 - 6 + 2 = 3 - 6 + 2 = -1. So |W''(1/2)| = 1, and the critical ratio is 4λ₂. **Correct.**
7. W''(c) < 0 when 6c² - 6c + 1 < 0, i.e., c ∈ ((3-√3)/6, (3+√3)/6) ≈ (0.211, 0.789). **Correct.**

**Audit of the tangent space projection:**
- At u = c·1 on Σ_m, the tangent space is T = {v : Σ v_i = 0}.
- The constant vector 1 is an eigenvector of L with eigenvalue 0. On T, the smallest eigenvalue of L is λ₂ (the Fiedler value).
- The Hessian restricted to T: H|_T = 4αL + βW''(c)I restricted to T.
- The Fiedler eigenvector v₂ ∈ T gives v₂^T H v₂ = 4αλ₂ + βW''(c).
- This is < 0 when β/α > 4λ₂/|W''(c)| (since W''(c) < 0). **Correct.**

**Audit of the conclusion:**
- u = c·1 is the unique uniform critical point on Σ_m: any uniform vector on Σ_m must be c·1 (since Σ u_i = m = cn).
- ∇E_bd at c·1: The gradient of 2αu^T Lu = 4αLu. At u = c·1, Lu = 0, so the smoothness gradient vanishes. The double-well gradient is βW'(c)·1. The Lagrange condition ∇E = μ·1 is satisfied with μ = βW'(c). **Valid.**
- If the Hessian has a negative eigenvalue on T, then c·1 is a saddle point (not a local minimizer on Σ_m).
- A global minimizer exists (T1) and cannot be c·1 (since it's a saddle). So the global minimizer is non-uniform.

**What happens at the spinodal boundaries?**
- At c = (3±√3)/6, W''(c) = 0. The critical ratio β/α → ∞. There is no phase transition at these boundary values — the uniform state is marginally stable (degenerate Hessian). This edge case is correctly excluded by the strict inequality in the spinodal range.

**Verdict: VALID.** This is the cleanest theorem in the theory. The proof is complete, all steps check out, and the critical ratio is correct under the ordered-pair convention.

---

### T3/T6-Stability: Non-Idempotent Stability Advantage

**Claimed:** Non-idempotent closure gives n/n positive Hessian eigenvalues; idempotent gives ≤ (n-k)/n.

**Audit:**
- The Hessian of E_cl at a point u: ∇²E_cl = 2(I - J_Cl)^T (I - J_Cl) + second-order terms involving Cl(u) - u.
  - **Wait.** E_cl = ‖u - Cl(u)‖². Let r(u) = u - Cl(u). Then ∇E_cl = 2(I - J_Cl)^T r(u). The Hessian is:
  - ∇²E_cl = 2(I - J_Cl)^T(I - J_Cl) + 2 Σ_i r_i(u) · ∇²r_i(u).
  - **At the fixed point** u* = Cl(u*), r(u*) = 0, so the second term vanishes. The Hessian simplifies to 2(I - J_Cl)^T(I - J_Cl). **Valid at the fixed point.**
  - **Away from the fixed point** (e.g., at an energy minimizer that is NOT the closure fixed point), the second-order term is nonzero and could change the eigenvalue count. This is the gap.

- For (a): At the fixed point, since ‖J_Cl‖_op < 1, all eigenvalues of J_Cl have modulus < 1. So 1 is not an eigenvalue, I - J_Cl is invertible, and (I - J_Cl)^T(I - J_Cl) is positive definite. **n/n positive eigenvalues. Valid at the fixed point.**

- For (b): For idempotent J_Cl (eigenvalues in {0,1}), eigenvectors with eigenvalue 1 give (I - J_Cl)v = 0, so the Gram matrix has zero eigenvalues. If range(J_Cl) has dimension k, there are k zero eigenvalues. **(n-k)/n positive eigenvalues. Valid.**

**Critical gap:** The theorem as stated applies at the closure fixed point u*. But energy minimizers are NOT the closure fixed point in general (they minimize the full energy, not just E_cl). The paper's Theorem 2 (paper1_math.tex line 304-321) states the hypothesis correctly: "Let u* = Cl(u*) be the unique closure fixed point with ‖J_Cl(u*)‖_op < 1." But the application to metastability (T7) then assumes the energy minimizer û is near the fixed point. The paper acknowledges this in a remark (line 407: "The proof as stated requires that û is close to the closure fixed point").

**What if J_Cl has eigenvalues near 1?** In the contraction regime, all eigenvalues of J_Cl have modulus ≤ a_cl/4 < 1. The smallest eigenvalue of (I - J_Cl)^T(I - J_Cl) is (1 - ‖J_Cl‖_op)² ≥ (1 - a_cl/4)². For a_cl = 3.5 (default), this is (1 - 0.875)² = 0.015625 — small but positive. As a_cl → 4, this → 0. **The advantage degrades near the boundary of the contraction regime.**

**Verdict: VALID at the fixed point; OVERSTATED for energy minimizers.** The hypothesis "at a non-idempotent closure fixed point" is correct in the theorem statement, but downstream usage (T7, proto-cohesion) implicitly assumes the minimizer is near the fixed point. This requires the self-consistency argument (large λ_cl forces ‖u - Cl(u)‖ small) which is proved directionally but lacks quantitative bounds.

---

### T7-Enhanced: Enhanced Metastability

**Claimed:** SCC minimizers have strictly larger energy barriers than Allen-Cahn minimizers.

**Audit — the fundamental conceptual error:**

The proof (paper1_math.tex lines 391-404) equates "larger minimum Hessian eigenvalue" with "deeper energy basin." This is **mathematically incorrect** as a general statement.

- **Energy barrier** = E(saddle) - E(minimizer), where the saddle is the lowest-energy saddle point on the boundary of the basin of attraction.
- **Minimum Hessian eigenvalue** = local curvature at the minimizer. This determines the *shape* of the basin near the minimizer, not its *depth*.
- A basin can have large curvature at the bottom but a low saddle point nearby (small barrier).
- Conversely, a basin can have small curvature but a high saddle (large barrier).

The paper's equation: Δ(barrier) ≥ λ_cl · 2(1 - ‖J_Cl‖_op)² is actually a lower bound on the minimum Hessian eigenvalue increase, NOT on the barrier height increase.

**What CAN be salvaged:**
- The closure term does add a positive-definite contribution to the Hessian at local minimizers (if they're near the closure fixed point). This means the SCC energy has strictly higher curvature at the minimizer.
- For a quadratic approximation E ≈ E_min + ½ v^T H v, the "barrier" to distance r is ½ λ_min r². Adding a positive-definite term increases λ_min, hence increases this local quadratic barrier. But the actual barrier depends on the global landscape, not just local curvature.
- The claim would be correct if the saddle point geometry is unchanged by adding E_cl. But adding E_cl changes the saddle point locations too.

**Severity: HIGH.** The theorem as stated is not proved. The paper presents a Hessian argument as a barrier argument.

**Minimal fix:** Restate as: "The minimum eigenvalue of the constrained Hessian at local minimizers of the full SCC energy is strictly larger than that of E_bd alone, by at least λ_cl · 2(1 - ‖J_Cl‖_op)²." This is what is actually proved. A genuine barrier comparison would require analyzing the saddle point structure of the full energy landscape, which is not done.

---

### T14: Gradient Flow Convergence

**Claimed:** Projected gradient flow on Σ_m converges to a critical point; exponential for analytic energy.

**Audit of analyticity:**
- The sigmoid σ(z) = 1/(1+e^{-z}) is real-analytic on all of R (it is the composition of the exponential and rational functions, both analytic; the denominator 1+e^{-z} > 0 for all z, so no singularities). **Valid.**
- The aggregation P_t f(x) = Σ K(x,y)f(y) / (Σ K(x,y) + ε). With ε > 0, the denominator is strictly positive, so this is a rational function of the field values. Rational functions with non-vanishing denominators are analytic. **Valid.**
- The closure Cl(u) = σ(a_cl((1-η)u + η P_t u - τ)) is a composition of analytic functions. **Analytic.**
- The distinction D(x;1-u) = σ(a_D(P_t u - λ_D P_t(1-u)) - τ_D). Since P_t(1-u) = P_t(1) - P_t(u), and all operations are analytic (with b_D = 0 removing the |·| non-analyticity). **Analytic.**
- E_cl = ‖u - Cl(u)‖² = composition of analytic function and polynomial. **Analytic.**
- E_sep = Σ u_i(1 - D_i) = polynomial in analytic functions. **Analytic.**
- E_bd = 2α u^T L u + β Σ W(u_i). Polynomial. **Analytic.**
- Total E = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd. Sum of analytic functions. **Analytic.**

**Audit of the Łojasiewicz argument:**
- The Łojasiewicz–Simon gradient inequality requires the energy to be analytic on a compact domain. Σ_m ∩ [0,1]^n is compact, and E is analytic on it. **Valid.**
- The inequality gives: |E(u) - E(u*)|^θ ≤ C‖∇E(u)‖ for some θ ∈ [1/2, 1) near each critical point u*.
- Combined with dE/dt = -‖Π∇E‖², standard ODE arguments give convergence of trajectories. **Valid.**
- **The Łojasiewicz exponent θ is not computed.** The proof invokes the inequality but does not determine θ. At non-degenerate critical points, θ = 1/2 (giving exponential convergence). At degenerate critical points, θ > 1/2 (giving polynomial convergence). The paper correctly states both cases.

**Subtlety: Is E actually analytic, or just C^∞?** The sigmoid is C^ω (real-analytic), not just C^∞. The distinction matters for Łojasiewicz. **It is C^ω. Valid.**

**Verdict: VALID.** The proof is correct. The only weakness is that the Łojasiewicz exponent is not computed, which is standard in the literature (computing θ is very difficult in general). The paper honestly states this.

---

### T11: Sharp-Interface Γ-Convergence

**Claimed:** As ε = α/β → 0, E_bd Γ-converges to a perimeter functional; self-referential corrections modify the surface tension.

**Audit:**

**The leading-order Γ-convergence:**
- The standard Modica-Mortola argument on graphs is: as ε → 0, the rescaled energy ε Σ_{x,y} N(u_x-u_y)² + (1/ε) Σ W(u_x) Γ-converges to σ_AC |∂S|_G where σ_AC = ∫₀¹ 2√W(s)ds.
- On finite graphs, "Γ-convergence" needs careful interpretation. The standard argument is for sequences of functionals on expanding graph families (e.g., finer and finer grids approximating a continuum). For a FIXED finite graph, the result is simpler: as ε → 0, minimizers of the rescaled energy converge to characteristic functions of minimum-perimeter sets. This is essentially a compactness + perturbation result.
- **The Rigor Auditor correctly notes this is "correct but shallow" on finite graphs** (R8-R11 audit line 31-33). On a fixed finite graph, the discretization is already finite and the "interface" is a single edge. The result is more a perturbation expansion than deep Γ-convergence theory.

**The self-referential correction:**
- The paper claims E_cl and E_sep modify the effective surface tension: σ_eff = σ_AC + δσ(λ_cl, λ_sep).
- The argument is: E_cl and E_sep are bounded on [0,1]^n and do not scale with 1/ε. So in the Γ-limit they contribute O(1) (or O(ε) after rescaling), not O(1/ε).
- **This means they do NOT modify the Γ-limit.** The Γ-limit is σ_AC |∂S|_G, period. The corrections are lower-order perturbations that vanish in the limit.
- The paper's statement "modify the effective surface tension" is misleading. What they modify is the pre-limit energy at finite ε. This is a valid perturbation statement but should not be presented as a modification of the Γ-limit.

**Verdict: LEADING ORDER VALID; SURFACE TENSION CLAIM OVERSTATED.** The standard Modica-Mortola Γ-limit is correct. The claim that self-referential terms modify the surface tension in the limit is incorrect — they are lower-order corrections that vanish. At finite ε, they contribute, but this is not a Γ-convergence statement.

---

### C-Axioms: Resolvent Co-belonging

**Claimed:** C_t = (I - α W_sym)^{-1} satisfies C1-C4.

**Audit:**
- **C1 (Dependence on u and N):** By construction, W_sym depends on u and N. Trivially valid.
- **C2 (Distinction from adjacency):** Proved by explicit witnesses (numerical). The 3-orders-of-magnitude claim is computational evidence on 5×5 grids. **Valid as computational demonstration; not a theorem.**
- **C3'' (Local monotonicity):** The claim is that C(x,x) increases when u(x) increases (other values fixed).
  - W_sym(x,y) = √u(x) N(x,y) √u(y) / d_x, where d_x = Σ_y √u(x) N(x,y) √u(y).
  - Increasing u(x) increases √u(x) in both the numerator and denominator (via d_x). The diagonal of (I - α W_sym)^{-1} = I + α W_sym + α² W_sym² + ...
  - The k-th term involves (W_sym^k)_{xx}, which sums over all length-k paths from x back to x.
  - **The gap:** When u(x) increases, d_x increases, which *decreases* the normalized entries W_sym(x,y)/d_x. So the effect is ambiguous: more weight in the numerator but also more in the denominator.
  - The paper acknowledges this gap explicitly (paper1_math.tex line 553-555).
  - **This is a genuine gap.** The intuition is correct (higher cohesion should increase self-co-belonging) but the formal proof is incomplete because the similarity transform D^{-1/2} depends on u(x).

- **C4 (Symmetry):** W_sym is symmetric by construction (W_sym(x,y) = √u(x) N(x,y) √u(y) / d_x — **wait, this is NOT symmetric** unless d_x = d_y or the normalization is different).
  - Actually, looking at the spec more carefully: the entries are "W_sym(x,y) = √u(x) N(x,y) √u(y) / d_x for appropriate degree normalization d_x." If d_x ≠ d_y, then W_sym(x,y) ≠ W_sym(y,x).
  - **The standard symmetrization** is: W_sym = D^{-1/2} W̃ D^{-1/2} where W̃(x,y) = u(x) N(x,y) u(y) (or √u · N · √u) and D is a diagonal normalization. This IS symmetric.
  - The implementation in operators.py calls `graph.cohesion_weighted_symmetric(u)` which presumably constructs a symmetric matrix. I'll assume the implementation is correct.
  - **If W_sym is symmetric, then C4 is trivially valid** since (I - αA)^{-1} is symmetric when A is symmetric.

**Verdict: C1, C2 (computational), C4 VALID. C3'' HAS A GENUINE GAP.** The gap is in the monotonicity of the diagonal under changes to a single field value, due to the competing effects of the normalization denominator.

---

### Sep = 1 - E_sep/m

**Claimed as "exact equality."**

**Audit:**
- Sep_old = (1/m) Σ u_i D_i (u-weighted average of distinction).
  - E_sep = Σ u_i(1 - D_i) = Σ u_i - Σ u_i D_i = m - m · Sep_old.
  - So Sep_old = 1 - E_sep/m. **EXACT. Valid.**

- Sep_new (C_t-weighted) = Σ C(x,x) D_x / Σ C(x,x).
  - E_sep = Σ u_i(1 - D_i). This involves u-weighting, not C(x,x)-weighting.
  - **There is NO simple relationship between Sep_new and E_sep.** The weights are different (u_i vs C(x,x)).

- The Canonical Spec (line 414) correctly states: "The exact equality Sep = 1 - E_sep/m was proved for the original (unweighted) Sep. The relationship between the C_t-weighted Sep and E_sep is an open problem."

- **However, the experimental results (results-I8.md) reveal that Sep_new ≈ 0.5 regardless of formation quality**, because it averages D over ALL nodes weighted by C(x,x). Since D ≈ 1 on interior and D ≈ 0 on exterior, the average is ≈ 0.5. The experiments switched to u-weighted Sep (Sep_old) which gives 0.87-0.93 on well-formed fields. This means **Sep_new as defined is a broken diagnostic** — it doesn't discriminate formation quality.

**Severity: HIGH for the theory's diagnostic framework.** The canonical Sep_new doesn't work empirically. The implementation uses Sep_old (u-weighted). This creates a disconnect between the formal theory and the implementation.

**Verdict:** The exact equality Sep = 1 - E_sep/m is **valid for Sep_old only**. Sep_new has no proved relationship to E_sep and is empirically broken as a diagnostic.

---

### Proto-Cohesion Existence Theorem

**Claimed:** "Proved with caveats" — minimizers achieve high Bind, Sep, Inside.

**Audit of each step:**

1. **Non-trivial minimizer exists (T8-Core):** VALID (see above). But T8-Core only covers E_bd. For the full energy, T8-Full has a gap (IFT step).

2. **Formation structure (Γ-convergence):** Only in the limit ε → 0. At finite parameters, formation structure is a computational observation, not a proved property. The Γ-convergence result says minimizers approach characteristic functions as β/α → ∞, but at the actual parameter values used (β ≈ 10, α ≈ 1), the approximation quality is unknown.

3. **Bind ≥ 1 - ε_Bind:** The argument is: at the minimizer, the first-order optimality (KKT) condition gives λ_cl ∇E_cl + ... = μ·1. So λ_cl · 2(J_Cl - I)^T(Cl(u) - u) + ... = μ·1. For large λ_cl, the closure residual ‖Cl(u) - u‖ must be small (otherwise the gradient would be dominated by the closure term and couldn't balance the Lagrange multiplier). This is a valid directional argument. **But the quantitative bound ‖Cl(u) - u‖ = O(1/λ_cl) is not proved** — it requires bounding the other gradient terms, which depend on the minimizer's structure.
   - The Cauchy-Schwarz bound Bind ≥ 1 - √(E_cl/n) is valid. But bounding E_cl at the minimizer requires more work.

4. **Sep ≥ δ_Sep:** The forward bridge says small E_sep implies high Sep_old. But at the minimizer, E_sep is jointly minimized with E_cl and E_bd. There is no guarantee that E_sep is individually small — the minimizer trades off all three terms. A formation with small E_bd (sharp interfaces) might have moderate E_sep if the distinction operator doesn't respond well to sharp boundaries.

5. **Inside ≥ μ_Inside:** The Q_morph bound is conjectured from the Γ-limit (where minimizers are characteristic functions with single connected support, giving ℓ_max = 1, Artic = 1). At finite parameters, there's a persistence stability argument, but no quantitative bound.

**The λ_sep/λ_bd tension (from R8-R11 final audit):**
- The Rigor Auditor found that H_sep has a large stabilizing Fiedler eigenvalue (~1.8M), requiring λ_sep/λ_bd < ~10^{-5} for T8's instability to survive. This means:
  - If λ_sep is comparable to λ_bd, the separation term may STABILIZE the uniform state, preventing the phase transition.
  - If λ_sep << λ_bd, the separation term has negligible effect on diagnostics.
  - This creates a genuine tension: the phase transition requires small λ_sep, but the Sep diagnostic requires non-negligible λ_sep.
- The experiments (results-I8.md) at equal weights (w_cl = w_sep = w_bd = 1) show formations exist (Inside > 0.88). This contradicts the λ_sep/λ_bd ≈ 10^{-5} requirement. **Resolution:** The experiments use Hessian normalization (EnergyComputer.normalize_weights), which effectively adjusts the λ ratios. The normalized λ_sep may indeed be ~10^{-5} of λ_bd.

**Verdict: DEMONSTRATED, NOT PROVED.** The existence backbone (T8-Core for E_bd alone) is rigorous. The predicate satisfaction at minimizers is supported by computation and informal arguments but has no complete analytical proof. The "proved with caveats" label is honest but should not be confused with a theorem.

---

### T7 (Enhanced Metastability) — CONTINUED

**Additional issue: "corresponding Allen-Cahn minimizer"**

The theorem compares SCC minimizers to "corresponding Allen-Cahn minimizers." What exactly is the correspondence? The SCC energy includes E_cl and E_sep in addition to E_bd. The minimizer of E changes when these terms are added. There is no natural bijection between SCC minimizers and Allen-Cahn minimizers. The proof implicitly assumes that the same minimizer of E_bd is also a minimizer of E (with small perturbation), but this is exactly the T8-Full gap.

---

### Gradient Formulas Audit

**∇E_cl = 2(J_Cl - I)^T (Cl(u) - u):**

Let r = Cl(u) - u. E_cl = ‖r‖² = r^T r.
∂E_cl/∂u_j = 2 Σ_i r_i ∂r_i/∂u_j = 2 Σ_i (Cl(u)_i - u_i)(∂Cl(u)_i/∂u_j - δ_{ij}) = 2(J_Cl - I)^T r.

The implementation (energy.py lines 77-87):
```python
residual = Cl_u - u
JtR = closure_jacobian_transpose_vec(residual, sigma_prime, graph, params)
return 2.0 * (JtR - residual)
```
This computes 2(J_Cl^T · residual - residual) = 2(J_Cl^T - I)(Cl(u) - u) = 2(J_Cl - I)^T(Cl(u) - u). **Correct.**

**∇E_sep = (1 - D) - J_D^T u:**

E_sep = Σ u_i(1 - D_i(u)) = Σ u_i - Σ u_i D_i(u).
∂E_sep/∂u_j = (1 - D_j) - Σ_i u_i ∂D_i/∂u_j = (1 - D_j) - (J_D^T u)_j.

The implementation (energy.py lines 100-108):
```python
frozen_part = 1.0 - D_u
jac_part = distinction_jacobian_transpose_vec(u, sigma_prime_D, graph, params)
return frozen_part - jac_part
```
This computes (1 - D) - J_D^T u. **Correct.**

**∇E_bd = 4αLu + βW'(u):**

E_bd = 2αu^T Lu + β Σ W(u_i).
∇(2αu^T Lu) = 4αLu. **Correct.**
∇(β Σ W(u_i)) = β W'(u) where W'(u) = 2u(1-u)(1-2u). **Correct (factor of 2 from I6).**

The implementation (energy.py lines 57-64):
```python
Lu = np.asarray(graph.L @ u).ravel()
return 4.0 * params.alpha_bd * Lu + params.beta_bd * double_well_deriv(u)
```
With `double_well_deriv(u) = 2.0 * u * (1.0 - u) * (1.0 - 2.0 * u)`. **Correct.**

**All gradient formulas are correct.**

---

### Hessian Normalization

**Claimed:** Dividing λ_i by Hessian spectral norms σ_i equalizes the energy terms' contributions.

**Audit:**
- The idea: different energy terms may have wildly different Hessian magnitudes at the uniform state. Normalizing λ_i = w_i / σ_i ensures each term contributes equally to the curvature at u = c·1.
- **Is this mathematically justified?** It's a heuristic for parameter selection. There's no theorem that says this normalization produces "better" formations. It's a reasonable engineering choice.
- The implementation (energy.py lines 169-231) computes σ_bd analytically and σ_cl, σ_sep via finite-difference power iteration. The analytical σ_bd = |4α λ_max(L) + 2β W''(c)| uses the Hessian of E_bd at the uniform state. **Correct.**
- **Concern:** The normalization is computed at u = c·1, but the minimizer is far from c·1 (it's a non-uniform formation). The Hessian at the minimizer may have very different spectral properties than at the uniform state.

**Verdict: VALID as a heuristic. NOT mathematically principled** as a theory of parameter selection. Correctly implemented.

---

### Coercivity (Is the energy bounded below on Σ_m?)

- E_cl = ‖u - Cl(u)‖² ≥ 0. **Bounded below by 0.**
- E_sep = Σ u_i(1 - D_i). Since u_i ∈ [0,1] and D_i ∈ [0,1] (output of sigmoid clipped to (0,1)), we have u_i(1-D_i) ∈ [0,1]. So E_sep ∈ [0, n]. **Bounded below by 0.**
- E_bd = 2α u^T L u + β Σ W(u_i). u^T L u ≥ 0 (L is PSD). W(u_i) ≥ 0. **Bounded below by 0.**
- E = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd ≥ 0. **Bounded below.**

**Verdict: VALID.** Coercivity is trivial since all terms are non-negative.

---

### KKT Conditions on Σ_m

Critical points of E|_{Σ_m} satisfy: ∇E(u) = μ·1 + ν_+ - ν_- where μ is the Lagrange multiplier for Σ u_i = m, ν_+ ≥ 0 are multipliers for u_i ≤ 1, ν_- ≥ 0 are multipliers for u_i ≥ 0. For interior points (0 < u_i < 1 for all i), the box constraints are inactive and the condition simplifies to ∇E(u) = μ·1.

The projected gradient (energy.py line 160-163) subtracts the mean: g_proj = g - mean(g). This is the projection onto T(Σ_m) = {v : Σ v_i = 0}. Setting g_proj = 0 is equivalent to ∇E = μ·1. **Correct.**

For points where some u_i = 0 or u_i = 1, the KKT conditions are more complex. The optimizer uses iterative clipping and rescaling, which is a practical heuristic, not a certified KKT solver. But on compact Σ_m, the existence of minimizers is guaranteed regardless of the optimization algorithm.

---

### Transport Fixed-Point Existence (Theorem 9 in the paper)

**Claimed:** The map Φ: Σ_m → Σ_m has a fixed point (Brouwer).

**Audit:**
- **Domain:** Σ_m is compact and convex. **Valid.**
- **Self-map:** The paper claims Φ: Σ_m → Σ_m. The last step of Φ is "minimize the static energy at time s on Σ_m," so the output is indeed in Σ_m. **Valid.**
- **Continuity:** This is the critical step.
  - Fingerprint φ_s is continuous in u_s (compositions of smooth functions). **Valid.**
  - Cost c(x,y) is continuous in φ_s. **Valid.**
  - Entropy-regularized OT solution M* is C^∞ in cost (well-known). **Valid.**
  - **The energy minimizer at time s is continuous in M*.** This requires the minimizer to be unique and non-degenerate (for the IFT to apply). If the minimizer is degenerate, or if there are multiple minimizers, the minimizer map may be discontinuous.
  - The paper acknowledges this implicitly: "at non-degenerate points (by the implicit function theorem)."
  - **GAP:** Degeneracy is not excluded. At degenerate parameter values, the energy may have bifurcating minimizers, breaking continuity of Φ.

**Verdict: VALID modulo non-degeneracy.** If all minimizers encountered in the Φ map are non-degenerate, the proof is correct. But non-degeneracy is not proved (and may fail at phase transition boundaries).

---

## III. CROSS-CUTTING ISSUES

### Issue 1: Sep_new vs Sep_old Incoherence

The theory mandates Sep_new (C_t-weighted, Spec §7.1). The experiments show Sep_new ≈ 0.5 regardless (broken diagnostic). The implementation switches to Sep_old (u-weighted, Σ u_i D_i / m). The paper's Proposition 1 (Sep Covariance Identity) analyzes Sep_new.

**The exact equality Sep = 1 - E_sep/m holds for Sep_old.** Sep_new has no energy relationship. The paper must be clear about which Sep is being used where.

### Issue 2: The Phase Transition Under Full Energy

T8-Core proves the phase transition for E_bd alone. The full energy E = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd may stabilize or destabilize the uniform state differently. The experiments show formations even below β_crit (results-I8.md line 69: "Formations appear even at β/β_crit = 0.1"). This suggests E_cl and E_sep provide additional instability mechanisms.

But the Rigor Auditor found H_sep stabilizes the Fiedler mode (positive eigenvalue). So the full-energy phase transition criterion is different from T8-Core's 4λ₂/|W''(c)|, and may be:
- **Easier** (lower β_crit) if high-frequency modes are destabilized by E_sep
- **Harder** (higher β_crit) if the Fiedler mode is stabilized by E_sep

The experimental finding of sub-critical formations likely comes from the Hessian normalization making λ_sep very small, so the effective energy is dominated by E_bd.

### Issue 3: Volume Constraint Necessity

Without the volume constraint, u ≡ 0 is the global minimizer (all energy terms vanish). The entire theory depends on the volume constraint to prevent collapse. This is correctly stated (Spec §8.0). But the Lagrange multiplier μ for the volume constraint affects all gradient and Hessian analyses. The paper correctly projects onto T(Σ_m) in the proofs.

### Issue 4: Lipschitz Constant a_cl/4 at the Boundary

The contraction rate a_cl/4 approaches 1 as a_cl → 4. Near a_cl = 4, the contraction is very slow and the unique fixed point claim still holds but convergence degrades. At a_cl = 4 exactly, the Lipschitz constant equals 1 — contraction fails. The theory correctly excludes a_cl = 4 with a strict inequality.

---

## IV. SUMMARY VERDICTS

### Fully Valid (no gaps):
- T1 (minimizer existence)
- T6a (closure FP existence via Brouwer)
- T6b (closure contraction, a_cl < 4)
- T20 (axiom consistency)
- T-A2 (monotonicity)
- **T8-Core (phase transition for E_bd)** — the theory's strongest result
- T14 (gradient flow convergence)
- Bind ≥ 1 - √(E_cl/n) (Cauchy-Schwarz)
- Sep_old = 1 - E_sep/m (exact equality for u-weighted Sep)
- All gradient formulas (verified against implementation)

### Valid with Caveats:
- T3/T6 (non-idempotent advantage) — valid at fixed point; application to minimizers needs self-consistency argument
- T11 (Γ-convergence) — leading order valid; surface tension modification is a perturbation claim, not a Γ-limit modification
- C-Axioms C1, C2, C4 — valid (C2 computational); **C3'' has a genuine gap**
- QM1-4 — QM2 (monotonicity) is informal
- Transport FP existence — valid modulo non-degeneracy hypothesis

### Gaps Requiring Fix:
- **T7 (enhanced metastability) — conceptual error: Hessian curvature ≠ basin depth** [HIGH]
- **Sep_new is empirically broken as a diagnostic** [HIGH]
- **Proto-cohesion existence is demonstrated, not proved** [HIGH]
- T8-Full — IFT step unwritten; λ_sep/λ_bd constraint missing [MEDIUM]
- C3'' — symmetrization gap unresolved [MEDIUM]

### The Theory's Mathematical Standing (Honest Assessment):

**What is rigorously proved:**
1. On E_bd alone (the Allen-Cahn part): minimizer existence, phase transition, Γ-convergence. These are clean results.
2. For the closure operator: contraction, fixed-point uniqueness, axiom consistency. Clean.
3. For the full energy: gradient flow convergence (T14). Clean.
4. Non-idempotent closure gives a strictly positive-definite Hessian contribution at the closure fixed point. Clean but narrower than claimed.

**What is NOT proved but is claimed or implied:**
1. That energy minimizers satisfy proto-cohesion (Bind, Sep, Inside above thresholds). Only demonstrated computationally.
2. That SCC formations are "more stable" than Allen-Cahn formations. T7 proves a Hessian eigenvalue increase, not a barrier increase.
3. That the Γ-limit has modified surface tension. The corrections are lower-order.
4. That Sep_new discriminates formation quality. It doesn't (stuck at ~0.5).

**What distinguishes SCC mathematically from Allen-Cahn on graphs:**
1. The closure energy E_cl (self-referential, no AC analogue) — proved to add PD Hessian at fixed points.
2. The separation energy E_sep (self-referential) — structurally novel but its role in the variational theory is quantitatively unclear.
3. The four-component diagnostic vector — a useful framework but diagnostics are not guaranteed by energy minimization.

The theory has genuine mathematical content. T8-Core and T14 are real theorems. But the bridge between energy minimization and the proto-cohesion diagnostic is the theory's Achilles heel — it's the central claim but it's only computationally demonstrated.
