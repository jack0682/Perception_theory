# Deep Mathematical Audit of SCC Proofs

**Auditor:** Hostile Mathematical Reviewer
**Date:** 2026-03-30
**Scope:** All theorem statements and proof sketches in `paper1_math.tex`, cross-referenced against `Canonical Spec v2.0.md` Section 13, `BIND-BOUND-PROOF.md`, `energy.py`, `operators.py`.

---

## Notation

- **SOUND**: Proof is mathematically correct as stated, with all hypotheses explicit.
- **GAP**: The theorem statement is likely true, but the proof has an identifiable missing step or unstated hypothesis. The gap is specified.
- **ERROR**: The proof contains a mathematical mistake, or the theorem statement is false/misleading as written.

---

## Theorem 1: Closure Contraction (paper Thm 1 / Spec T6a+T6b)

**Statement (paper):** (a) Brouwer gives existence. (b) For $a_{\mathrm{cl}} < 4$, unique fixed point, geometric convergence at rate $a_{\mathrm{cl}}/4$.

### Verdict: SOUND

**Detailed analysis:**

1. **Completeness of the metric space.** $([0,1]^n, \|\cdot\|_\infty)$ is a closed subset of $\mathbb{R}^n$, hence complete. Correct.

2. **Self-mapping.** $\sigma : \mathbb{R} \to (0,1) \subset [0,1]$, so $\mathrm{Cl} : [0,1]^n \to (0,1)^n \subset [0,1]^n$. Correct.

3. **Lipschitz bound.** The proof claims:
$$\|\mathrm{Cl}(u) - \mathrm{Cl}(v)\|_\infty \leq \frac{a_{\mathrm{cl}}}{4}\|u-v\|_\infty$$
Let me verify. For each component:
$$|\mathrm{Cl}(u)_i - \mathrm{Cl}(v)_i| = |\sigma(z_i^u) - \sigma(z_i^v)| \leq \max_z \sigma'(z) \cdot |z_i^u - z_i^v|$$
Now $z_i^u = a_{\mathrm{cl}}((1-\eta)u_i + \eta(Pu)_i - \tau)$, so:
$$|z_i^u - z_i^v| = a_{\mathrm{cl}}|(1-\eta)(u_i - v_i) + \eta(Pu - Pv)_i|$$
$$\leq a_{\mathrm{cl}}((1-\eta)|u_i - v_i| + \eta|(Pu - Pv)_i|)$$
Since $P$ is row-stochastic (up to $\varepsilon$-correction): $|(Pu - Pv)_i| \leq \|u - v\|_\infty$ (convex combination). So:
$$|z_i^u - z_i^v| \leq a_{\mathrm{cl}} \|u-v\|_\infty$$
Combined with $\max \sigma' = 1/4$: the bound holds. **Correct.**

4. **Worst-case vs typical rate.** The theorem states the rate as $a_{\mathrm{cl}}/4$, which is the worst-case upper bound. The proof is explicit that this is worst-case ($\max \sigma' = 1/4$ achieved at $z=0$). For practical inputs away from $z=0$, the effective rate is much better. **The statement is honest — it is a worst-case guarantee.** No issue.

5. **Dependence on $P$.** The non-expansiveness of $P$ requires $P$ to be (approximately) row-stochastic. The implementation uses $P(x,y) = N(x,y)/(\sum_y N(x,y) + \varepsilon)$, so $\sum_y P(x,y) = d_x/(d_x + \varepsilon) < 1$. This means $P$ is strictly sub-stochastic, which only strengthens the contraction (the effective Lipschitz constant is even smaller). **No issue.**

6. **$P$ non-expansive in $\|\cdot\|_\infty$?** For row-stochastic $P$: $\|Pv\|_\infty = \max_i |\sum_j P_{ij} v_j| \leq \max_i \sum_j P_{ij} |v_j| \leq \max_j |v_j| = \|v\|_\infty$. Yes. For sub-stochastic, even stricter. **Correct.**

**Minor note:** The $\varepsilon$-regularization means $P\mathbf{1} \neq \mathbf{1}$ exactly. This has no effect on the contraction proof but does affect later results (see T-Bind).

---

## Theorem 2: Non-Idempotent Stability Advantage (paper Thm 2 / Spec T3/T6-Stability)

**Statement:** At a contraction fixed point ($\|J_{\mathrm{Cl}}\|_{\mathrm{op}} < 1$), the closure Hessian $2(I-J_{\mathrm{Cl}})^T(I-J_{\mathrm{Cl}})$ is strictly positive definite.

### Verdict: GAP (minor)

**Detailed analysis:**

1. **Hessian computation.** The paper claims $\nabla^2 \mathcal{E}_{\mathrm{cl}} = 2(I-J_{\mathrm{Cl}})^T(I-J_{\mathrm{Cl}})$. This is the **Gauss-Newton approximation**, not the exact Hessian. The exact Hessian of $\|f(u)\|^2$ where $f(u) = \mathrm{Cl}(u) - u$ is:
$$\nabla^2 \mathcal{E}_{\mathrm{cl}} = 2(J_f)^T J_f + 2\sum_i f_i(u) \nabla^2 f_i(u)$$
where $J_f = J_{\mathrm{Cl}} - I$. The second term involves the Hessian of each component of $\mathrm{Cl}(u) - u$, multiplied by the residual $f_i(u)$.

2. **At the fixed point** $u^*$, $f(u^*) = 0$, so the residual term vanishes **exactly**. Therefore $\nabla^2 \mathcal{E}_{\mathrm{cl}}(u^*) = 2(I-J_{\mathrm{Cl}})^T(I-J_{\mathrm{Cl}})$ is exact at the fixed point. **This part is correct.**

3. **Away from the fixed point** (which is where the energy minimizer $\hat{u}$ typically is), the Gauss-Newton approximation has an error proportional to $\|r\|$. The paper's Theorem 4 (Metastability) uses this at a minimizer $\hat{u}$ which is NOT the closure fixed point. This is where the gap matters — see Theorem 4 below.

4. **Positive definiteness argument.** $I - J_{\mathrm{Cl}}$ is invertible iff 1 is not an eigenvalue of $J_{\mathrm{Cl}}$. Since $\|J_{\mathrm{Cl}}\|_{\mathrm{op}} < 1$, all eigenvalues of $J_{\mathrm{Cl}}$ have modulus $< 1$, so 1 is not an eigenvalue. Hence $I - J_{\mathrm{Cl}}$ has trivial kernel, so $(I-J_{\mathrm{Cl}})^T(I-J_{\mathrm{Cl}})$ is positive definite. **Correct.**

5. **Idempotent case.** The argument that idempotent $J_{\mathrm{Cl}}$ (projection) has eigenvalue 1 with multiplicity $k$, giving $k$ zero eigenvalues of $(I-J_{\mathrm{Cl}})^T(I-J_{\mathrm{Cl}})$, is standard linear algebra. **Correct.**

**The gap:** The theorem statement says "at a non-idempotent closure fixed point" but is used in Theorem 4 at an energy minimizer $\hat{u} \neq u^*$. At $\hat{u}$, the Hessian is NOT $2(I-J_{\mathrm{Cl}})^T(I-J_{\mathrm{Cl}})$ but includes the residual correction. The theorem itself is **sound as stated** (it IS evaluated at the fixed point), but its **application** in Theorem 4 introduces a gap.

---

## Theorem 3: Phase Transition (paper Thm 3 / Spec T8-Core)

**Statement:** If $\beta/\alpha > 4\lambda_2/|W''(c)|$ with $c$ in the spinodal range, the global minimizer of $\mathcal{E}_{\mathrm{bd}}|_{\Sigma_m}$ is non-uniform.

### Verdict: SOUND

**Detailed analysis:**

1. **Tangent space membership of Fiedler vector.** The Fiedler vector $v_2$ is the eigenvector of $L$ for $\lambda_2 > 0$. Since $L\mathbf{1} = 0$ (Laplacian has constant vector in kernel), and $L$ is symmetric, $v_2 \perp \mathbf{1}$, i.e., $\sum_i (v_2)_i = 0$. Therefore $v_2 \in T(\Sigma_m)$. **Explicitly verified. Correct.**

2. **Hessian computation.** The ordered-pair convention gives:
$$\mathcal{E}_{\mathrm{bd}} = 2\alpha u^T L u + \beta \sum W(u_i)$$
Hessian: $4\alpha L + \beta W''(c) I$ at $u = c\mathbf{1}$. The factor of 4 (not 2) comes from $\frac{d^2}{du^2}[2\alpha u^T L u] = 4\alpha L$. **Correct, and consistent with `energy.py` lines 58-64.**

3. **Second variation on tangent space.** $v_2^T H v_2 = 4\alpha\lambda_2 + \beta W''(c)$. For $c$ in the spinodal $((3-\sqrt{3})/6, (3+\sqrt{3})/6)$, $W''(c) < 0$. The condition $\beta/\alpha > 4\lambda_2/|W''(c)|$ gives $\beta|W''(c)| > 4\alpha\lambda_2$, i.e., $4\alpha\lambda_2 + \beta W''(c) < 0$ (since $W''(c) = -|W''(c)|$). **Correct.**

4. **Saddle point argument.** Negative second variation implies $c\mathbf{1}$ is a saddle, not a minimum. Since $\mathcal{E}_{\mathrm{bd}}$ is continuous on compact $\Sigma_m$, a global minimum exists (extreme value theorem). It cannot be $c\mathbf{1}$, so it is non-uniform. **Correct.**

5. **Boundary of $\Sigma_m \cap [0,1]^n$?** The constraint is $\Sigma_m = \{u \in [0,1]^n : \sum u_i = m\}$. This is compact. The global minimizer could have some $u_i = 0$ or $u_i = 1$ (box boundary). The proof does NOT claim the minimizer is interior — it only claims the minimizer is non-uniform. If the minimizer is on the box boundary, it is certainly non-uniform (not all equal to $c$). **The Hessian analysis at $c\mathbf{1}$ only needs to show $c\mathbf{1}$ is not a local minimum, which it does. No issue.**

6. **Is $c\mathbf{1}$ the ONLY homogeneous critical point?** On $\Sigma_m$, the only homogeneous feasible point is $u = c\mathbf{1}$ (since $\sum u_i = m$ and $u_i = c$ for all $i$). **Correct.**

**This is the strongest theorem in the paper. Fully rigorous.**

---

## Theorem 4: Enhanced Metastability (paper Thm 4 / Spec T7-Enhanced)

**Statement:** The minimum eigenvalue of $\nabla^2\mathcal{E}|_{T\Sigma_m}$ at a non-trivial minimizer strictly exceeds that of $\nabla^2\mathcal{E}_{\mathrm{bd}}|_{T\Sigma_m}$, with enhancement $\geq \lambda_{\mathrm{cl}} \cdot 2(1-\|J_{\mathrm{Cl}}\|_{\mathrm{op}})^2$.

### Verdict: GAP (significant)

**Detailed analysis:**

1. **Gauss-Newton approximation.** The proof uses $\nabla^2\mathcal{E}_{\mathrm{cl}} \approx 2(I-J_{\mathrm{Cl}})^T(I-J_{\mathrm{Cl}})$. As noted in Theorem 2 analysis, this is exact only at the closure fixed point. At the energy minimizer $\hat{u}$, the exact Hessian is:
$$\nabla^2\mathcal{E}_{\mathrm{cl}}(\hat{u}) = 2(I-J_{\mathrm{Cl}})^T(I-J_{\mathrm{Cl}}) + 2\sum_i r_i \nabla^2 (\mathrm{Cl}_i - \mathrm{id}_i)(\hat{u})$$
The residual term $r = \mathrm{Cl}(\hat{u}) - \hat{u}$ is nonzero at $\hat{u}$.

2. **Is the residual small?** The paper claims (line 400): "At well-formed minimizers ($\mathrm{Bind} \geq 0.85$), the residual is $O(0.15\sqrt{n})$." This is circular — the claim that Bind is high IS the claim that the residual is small. The correct question is: **can we bound the residual BEFORE invoking the theorem?**

   The T-Bind proof (BIND-BOUND-PROOF.md) shows $\|r_T\|_2 = O((\lambda_{\mathrm{bd}} + \lambda_{\mathrm{sep}})/\lambda_{\mathrm{cl}})$, but this only controls the tangential component, and only under strict interiority. The residual correction to the Hessian is:
$$\left\|\sum_i r_i \nabla^2 \mathrm{Cl}_i\right\|_{\mathrm{op}} \leq \|r\|_1 \cdot \max_i \|\nabla^2 \mathrm{Cl}_i\|_{\mathrm{op}}$$
Each $\nabla^2 \mathrm{Cl}_i$ involves the second derivative of $\sigma$, which is bounded. So the correction is $O(\|r\|_1)$. For the Gauss-Newton approximation to be valid, we need $\|r\|_1 \cdot C \ll 2(1-\|J_{\mathrm{Cl}}\|_{\mathrm{op}})^2$, where $C$ is the max second-derivative constant.

3. **The "hope" diagnosis.** The BIND-BOUND-PROOF demonstrates that the mean residual $\bar{r}_0$ is NOT controlled by $\lambda_{\mathrm{cl}}$ through KKT. The tangential part IS controlled, but bounding $\|r\|_1$ requires bounding both components. Without a proven bound on $\bar{r}_0$, the Gauss-Newton validity is indeed a **hope, not a theorem**.

4. **Is the E_sep Hessian contribution positive or negative?** The proof assumes "$\lambda_{\mathrm{sep}} \nabla^2\mathcal{E}_{\mathrm{sep}}$ does not dominate negatively." This is an unstated hypothesis. The separation Hessian is NOT guaranteed positive semidefinite (it involves products of sigmoids). If $\nabla^2\mathcal{E}_{\mathrm{sep}}$ has sufficiently negative eigenvalues, the "enhancement" could be cancelled. The proof needs either:
   - A bound showing $\lambda_{\mathrm{sep}}\nabla^2\mathcal{E}_{\mathrm{sep}}$ is positive semidefinite at minimizers, OR
   - An explicit condition on the parameter ratio $\lambda_{\mathrm{sep}}/\lambda_{\mathrm{cl}}$.

5. **The minimum eigenvalue bound.** The claim $\sigma_{\min}(I-J_{\mathrm{Cl}}) \geq 1 - \|J_{\mathrm{Cl}}\|_{\mathrm{op}}$ is correct (Weyl's inequality). But $\|J_{\mathrm{Cl}}\|_{\mathrm{op}}$ is the operator norm AT $\hat{u}$, not at the fixed point. The paper states $\|J_{\mathrm{Cl}}\|_{\mathrm{op}} \leq a_{\mathrm{cl}}/4$ uniformly over $[0,1]^n$ (from $\max \sigma' = 1/4$). **This uniform bound is correct** (see the BIND-BOUND-PROOF Step 3a verification). So the lower bound $2(1-a_{\mathrm{cl}}/4)^2$ holds.

**Summary of gaps:**
- **Gap 1 (Gauss-Newton):** The Hessian formula is approximate at $\hat{u}$, with residual correction not bounded.
- **Gap 2 (E_sep Hessian sign):** Unstated hypothesis that $\nabla^2\mathcal{E}_{\mathrm{sep}}$ is not excessively negative.
- **Severity:** The theorem is conditionally true — it holds when $\lambda_{\mathrm{cl}}$ is large enough relative to $\lambda_{\mathrm{sep}}$ and $\lambda_{\mathrm{bd}}$. The paper's remark acknowledges the Gauss-Newton qualification but does not give a computable condition.

---

## Theorem 5: Gradient Flow Convergence (paper Thm 5 / Spec T14)

**Statement:** Projected gradient flow on $\Sigma_m$ converges to a critical point, exponentially at non-degenerate points.

### Verdict: SOUND (with one step requiring verification)

**Detailed analysis:**

1. **Energy decrease.** $\frac{d}{dt}\mathcal{E} = \langle \nabla\mathcal{E}, \dot{u}\rangle = -\|\Pi_{\Sigma_m}\nabla\mathcal{E}\|^2 \leq 0$. **Correct** (standard calculation for projected gradient flow).

2. **Analyticity of $\mathcal{E}$ on $\mathbb{R}^n$.** The paper checks:
   - $\mathcal{E}_{\mathrm{bd}}$: polynomial — **analytic**. Correct.
   - $\mathcal{E}_{\mathrm{cl}}$: $\|\sigma(a \cdot \text{affine}(u)) - u\|^2$. The sigmoid $\sigma(z) = 1/(1+e^{-z})$ is real-analytic on $\mathbb{R}$. Compositions of analytic functions are analytic. Sums and squares of analytic functions are analytic. **Correct.**
   - $\mathcal{E}_{\mathrm{sep}}$: $\sum u_i(1 - \sigma(\text{stuff}))$. Same argument. **Correct.**
   - **Requires $b_D = 0$**: The absolute value $|u_x - u_y|$ in the original gradient term would break analyticity. Setting $b_D = 0$ removes this. **Correct and explicitly noted.**

3. **Analyticity on the constrained manifold $\Sigma_m$.** The Lojasiewicz inequality on manifolds requires the function to be analytic when restricted to the manifold. $\Sigma_m = \{u : \sum u_i = m\} \cap [0,1]^n$. The hyperplane part $\{\sum u_i = m\}$ is an affine subspace, and the restriction of an analytic function to an affine subspace is analytic. **Correct.**

   **The step requiring verification:** $\Sigma_m$ is not just a hyperplane — it is a hyperplane intersected with $[0,1]^n$, which is a polytope (compact, convex, with corners). At the boundary (where some $u_i = 0$ or $u_i = 1$), the manifold has corners, and the Lojasiewicz inequality on manifolds-with-corners requires either:
   - Working in the interior of $\Sigma_m$ (where the constraint $u \in (0,1)^n$ is inactive), or
   - Using the extended Lojasiewicz inequality for semi-algebraic sets (which $\Sigma_m \cap [0,1]^n$ IS, since it is defined by polynomial inequalities).

   The paper cites Lojasiewicz for "compact semi-algebraic sets." Since $[0,1]^n$ is semi-algebraic and $\{\sum u_i = m\}$ is algebraic, $\Sigma_m$ is semi-algebraic, and the Lojasiewicz inequality applies by Bochnak-Coste-Roy or Kurdyka's extension. **This step is correct but would benefit from an explicit citation.**

4. **Convergence from Lojasiewicz.** The argument that monotone energy decrease + Lojasiewicz inequality + compactness gives convergence to a single critical point is standard (Chill 2003, Simon 1983). The exponential rate at non-degenerate points ($\theta = 1/2$) and polynomial rate at degenerate points ($\theta > 1/2$) are textbook. **Correct.**

5. **Projected gradient flow well-posedness.** The flow $\dot{u} = -\Pi\nabla\mathcal{E}$ is an ODE on $\Sigma_m$ with locally Lipschitz right-hand side (since $\nabla\mathcal{E}$ is $C^1$). By Picard-Lindelof, solutions exist and are unique locally. Global existence follows from the invariance of $\Sigma_m$ (the projection keeps the trajectory on the manifold) and compactness (no blow-up). **Correct.**

**The one step:** The application of Lojasiewicz on the polytope $\Sigma_m \cap [0,1]^n$ is valid via the semi-algebraic extension but is not cited precisely. This is a minor technical point, not a gap in the argument.

---

## Theorem 6: Axiom Consistency (paper Thm 6 / Spec T20)

**Statement:** Sigmoid closure satisfies A1', A2, A3, A4. A1 + A3 are jointly unsatisfiable.

### Verdict: SOUND

**Detailed analysis:**

1. **A2 (monotonicity).** $P$ preserves order (nonneg kernel, convex combo). $z_i^u = a_{\mathrm{cl}}((1-\eta)u_i + \eta(Pu)_i - \tau)$ is order-preserving in $u$. $\sigma$ is increasing. Composition preserves order. **Correct.**

2. **A3 (contraction).** Proved in Theorem 1. **Correct.**

3. **A4 (continuity).** Composition of smooth functions. **Correct (trivially).**

4. **A1' (conditional extensivity).** The proof sketch says: when $(Pu)(x) \geq \theta \cdot u(x)$, then the sigmoid argument $\geq a_{\mathrm{cl}}(u - \tau)$, and for appropriate $\tau$, $\sigma(a_{\mathrm{cl}}(u-\tau)) \geq u$. This requires specifying $\theta$ — the proof says "appropriate" but the Spec (Section 5, A1') defines the condition. The argument is not fully explicit but the claim is correct: for a fixed $\tau$ and $a_{\mathrm{cl}}$, there exists a support threshold $\theta$ such that the extensivity condition holds for supported sites with $u$ not too close to 1. **Sound modulo parameter specification.**

5. **A1+A3 incompatibility.** The proof: A1 requires $\sigma(a_{\mathrm{cl}}(u - \tau)) \geq u$ for all $u$. At $u = 0.9$: $a_{\mathrm{cl}}(0.9 - \tau) \geq \sigma^{-1}(0.9) = \ln(9) \approx 2.197$. For $\tau = 0.5$: $a_{\mathrm{cl}} \geq 2.197/0.4 \approx 5.49$. But A3 requires $a_{\mathrm{cl}} < 4$. **Correct and sharp.**

---

## Theorem 7: Gamma-Convergence (paper Thm 7 / Spec T11)

**Statement:** As $\varepsilon = \alpha/\beta \to 0$, $\widetilde{\mathcal{E}}_{\mathrm{bd}}^\varepsilon$ Gamma-converges to a perimeter functional with modified surface tension.

### Verdict: GAP (moderate)

**Detailed analysis:**

1. **Leading-order result.** The standard Modica-Mortola argument on graphs (van Gennip & Bertozzi 2012). The paper follows the standard proof: Cauchy-Schwarz lower bound, optimal profile recovery sequence. **The leading-order Gamma-convergence is sound**, modulo the question of what graph topology is used.

2. **Finite graph vs. continuum limit.** The paper says "family of graphs $G_\varepsilon$." This is ambiguous. Van Gennip & Bertozzi prove Gamma-convergence for **fixed finite graphs** as $\varepsilon \to 0$. On a fixed graph, $\varepsilon \to 0$ means the double-well dominates, and minimizers approach $\{0,1\}^n$. This is NOT the same as the continuum Modica-Mortola (where both $\varepsilon \to 0$ and the mesh refines). **The paper conflates two limits:**
   - Fixed graph, $\varepsilon \to 0$: minimizers become binary; the Gamma-limit is a graph cut functional. This IS proved by van Gennip & Bertozzi.
   - Mesh refinement + $\varepsilon \to 0$ simultaneously: recovers the continuum perimeter. This requires assumptions on the graph family.

   **The theorem statement says "family of graphs $G_\varepsilon$" without specifying how the family relates to $\varepsilon$. This should be made precise.** If the intent is the fixed-graph result, the "family" language is misleading.

3. **Self-referential corrections.** The paper claims $\mathcal{E}_{\mathrm{cl}}$ and $\mathcal{E}_{\mathrm{sep}}$ contribute a "lower-order perturbation" $\delta\sigma$. The proof says: these terms are "bounded on $[0,1]^n$ and do not scale with $1/\varepsilon$." This is true: $\mathcal{E}_{\mathrm{cl}} \leq n$ and $\mathcal{E}_{\mathrm{sep}} \leq n$ (trivially), while $\widetilde{\mathcal{E}}_{\mathrm{bd}}^\varepsilon$ scales as $O(1/\varepsilon)$ near the interface.

   **However**: the modified surface tension $\delta\sigma(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}})$ is stated to "depend on the closure and separation operators evaluated at the sharp-interface profile." But:
   - The sharp-interface profile has $u \in \{0,1\}^n$. At such profiles, $\mathcal{E}_{\mathrm{cl}} > 0$ in general (the closure fixed point is not $\{0,1\}^n$). So $\delta\sigma$ depends on how the self-referential terms behave at the optimal profile, not at the binary limit.
   - The paper does not compute $\delta\sigma$ or give a formula. The existence of a correction is claimed but not proved to be nonzero.

4. **Gamma-convergence of the FULL energy vs. E_bd only.** The Gamma-convergence is stated for $\widetilde{\mathcal{E}}_{\mathrm{bd}}^\varepsilon$, not for the full $\mathcal{E} = \lambda_{\mathrm{cl}}\mathcal{E}_{\mathrm{cl}} + \lambda_{\mathrm{sep}}\mathcal{E}_{\mathrm{sep}} + \lambda_{\mathrm{bd}}\widetilde{\mathcal{E}}_{\mathrm{bd}}^\varepsilon$. The self-referential corrections are additive perturbations that are bounded and continuous, so they do not affect the Gamma-limit of the leading term. **But the paper's claim about $\sigma_{\mathrm{eff}} = \sigma_{\mathrm{AC}} + \delta\sigma$ is informal — "modify the effective surface tension" is a heuristic, not a proved Gamma-convergence statement.** The rigorous statement should be: the Gamma-limit of $\mathcal{E}_{\mathrm{bd}}$ is the cut functional, and the self-referential terms contribute $O(1)$ corrections that vanish relative to the $O(1/\varepsilon)$ leading term.

**Summary of gaps:**
- **Gap 1:** The graph family $G_\varepsilon$ is not specified.
- **Gap 2:** The surface tension correction $\delta\sigma$ is informal; the Gamma-limit of the full energy is the same as that of $\mathcal{E}_{\mathrm{bd}}$ alone (the corrections vanish).
- **Severity:** The leading-order Gamma-convergence is standard and sound. The "modified surface tension" is marketing, not mathematics. The theorem should be stated as Gamma-convergence of $\mathcal{E}_{\mathrm{bd}}$, with the self-referential terms as bounded perturbations.

---

## Theorem 8: Resolvent Co-Belonging (paper Thm 8 / Spec C-Axioms)

**Statement:** $(I - \alpha W_{\mathrm{sym}})^{-1}$ satisfies C1-C4.

### Verdict: GAP (known, explicitly flagged)

**Detailed analysis:**

1. **C1 (dependence).** By construction. **Trivially correct.**

2. **C2 (discrimination).** The "3+ orders of magnitude" claim is **computational, not proved.** The proof sketch describes the mechanism (exponential suppression of cross-boundary paths) but the quantitative claim is from numerical experiments on specific graphs (5x5 grids). **This is an empirical claim, not a theorem.**

   To prove it rigorously: on a graph with clear formation structure (e.g., two cliques connected by a single edge), the Neumann series concentrates within each clique. The ratio $C(x,y)_{\mathrm{within}} / C(x,y)_{\mathrm{across}}$ depends on $\alpha$ and the spectral gap. For separated cliques, this ratio is $\Omega((1/\alpha)^{d_G(x,y)})$ where $d_G$ is the graph distance. But this is not what the paper proves.

   **Status: Empirical observation, not a theorem. The "3+" language should be downgraded to "empirically observed."**

3. **C3'' (local monotonicity).** The paper explicitly flags the gap in a remark: "The C3'' proof has a subtle gap: the symmetrization step involves degree normalization $d_x$ that itself depends on $u(x)$, and the monotonicity of $d_x^{-1/2}$ with respect to $u(x)$ requires verification."

   Let me examine this more carefully. $W_{\mathrm{sym}}(x,y) = d_x^{-1/2} \tilde{W}(x,y) d_y^{-1/2}$ where $\tilde{W}(x,y) = \sqrt{u(x)u(y)} N(x,y)$ and $d_x = \sum_y \tilde{W}(x,y)$. Increasing $u(x)$ increases $\tilde{W}(x,y)$ for all $y$, but also increases $d_x$, and the $d_x^{-1/2}$ factor decreases. The net effect on $(W_{\mathrm{sym}}^k)_{xx}$ is not obviously monotone.

   **However**, there is a simpler formulation. Looking at `operators.py` line 176: `W_sym = graph.cohesion_weighted_symmetric(u)`. The exact construction matters. If $W_{\mathrm{sym}}$ is defined without degree normalization (just $\sqrt{u_x u_y} N_{xy}$), then the Neumann series argument works. If it includes degree normalization, the gap is real.

   **Status: Gap explicitly acknowledged in both paper and spec. The gap is real and specific.**

4. **C4 (symmetry).** $W_{\mathrm{sym}}$ symmetric $\implies$ all powers symmetric $\implies$ resolvent symmetric. **Correct (trivial).**

---

## T-Bind: Quantitative Bind Bound (BIND-BOUND-PROOF.md / Spec T-Bind)

**Statement:** At a constrained minimizer with strict interiority, the tangential residual satisfies $\|r_T\|_2 \leq F / (2\lambda_{\mathrm{cl}}(1-a_{\mathrm{cl}}/4))$ where $F$ is bounded by gradient norms.

### Verdict: GAP (explicitly acknowledged, honest)

**Detailed analysis:**

1. **KKT conditions.** At a minimizer of $\mathcal{E}$ on $\Sigma_m$ with strict interiority ($0 < \hat{u}_i < 1$), the KKT conditions are $\nabla\mathcal{E} = \nu\mathbf{1}$. **Correct (standard constrained optimization).**

2. **Projection onto $T(\Sigma_m)$.** Projecting both sides: $\Pi_T(\nabla\mathcal{E}) = 0$ (since $\Pi_T(\nu\mathbf{1}) = 0$). This eliminates $\nu$. **Correct.**

3. **Restricted operator bound.** The key claim: $A_T = \Pi_T(I-J_{\mathrm{Cl}})^T|_T$ has $\sigma_{\min}(A_T) \geq 1 - a_{\mathrm{cl}}/4$.

   Proof: For $v \in T$ with $\|v\| = 1$: $\langle A_T v, v\rangle = \langle (I-J_{\mathrm{Cl}})^T v, v\rangle = 1 - v^T J_{\mathrm{Cl}} v$. Since $|v^T J_{\mathrm{Cl}} v| \leq \|J_{\mathrm{Cl}}\|_2 \leq a_{\mathrm{cl}}/4$: $\langle A_T v, v\rangle \geq 1 - a_{\mathrm{cl}}/4 > 0$. By Cauchy-Schwarz: $\|A_T v\| \geq \langle A_T v, v\rangle / \|v\| = \langle A_T v, v\rangle \geq 1 - a_{\mathrm{cl}}/4$.

   **Wait — is this correct?** The Cauchy-Schwarz step: $\langle A_T v, v\rangle \leq \|A_T v\| \cdot \|v\| = \|A_T v\|$. Therefore $\|A_T v\| \geq \langle A_T v, v\rangle \geq 1 - a_{\mathrm{cl}}/4$. **Yes, correct.** The minimum singular value is at least the minimum of the numerical range, which is at least $1 - a_{\mathrm{cl}}/4$.

4. **The mean residual gap.** The proof document is admirably honest. It shows that $\bar{r}_0 = |\sum_i (\mathrm{Cl}(\hat{u})_i - \hat{u}_i)|/n$ cannot be controlled through KKT alone. This is a structural limitation: the closure operator does not preserve mass, so the mean component of the residual is determined by the nonlinear structure of $\sigma$, not by the energy weights.

   The bound as stated splits into:
   - Tangential part: $\|r_T\|_2$ is controlled.
   - Mean part: $\bar{r}_0$ is empirically small ($< 0.02$) but not theoretically bounded.

   **This is an honest gap. The tangential bound is proved; the full Bind bound carries an uncontrolled $\bar{r}_0$ term.**

5. **Are $G_{\mathrm{sep}}$ and $G_{\mathrm{bd}}$ bounded on $\Sigma_m \cap [0,1]^n$?** Yes. All functions involved (sigmoid, polynomial, Laplacian action) are continuous on the compact set $[0,1]^n$, hence bounded. The explicit bounds are given in Section IV:
   - $G_{\mathrm{bd}}/\sqrt{n} \leq 4\alpha\lambda_{\max}(L) + 2\beta/(3\sqrt{3})$
   - $G_{\mathrm{sep}}/\sqrt{n} \leq 1 + a_D(1+\lambda_D)/4$

   **Correct and explicit.**

6. **Vacuity at default parameters.** The proof honestly shows that for $\lambda_{\mathrm{cl}} = \lambda_{\mathrm{bd}} = \lambda_{\mathrm{sep}} = 1$, the bound is vacuous ($\|r_T\|_2/\sqrt{n} \approx 157 > 1$). It becomes non-vacuous only after Hessian normalization gives $\lambda_{\mathrm{cl}} \gg \lambda_{\mathrm{bd}}$. **This is a correct and important caveat.**

---

## Sep = 1 - E_sep/m (Predicate-Energy Identity, Spec "Predicate-Energy Bridge")

**Statement:** For the $u$-weighted Sep: $\mathrm{Sep} = 1 - \mathcal{E}_{\mathrm{sep}}/m$.

### Verdict: SOUND

**Verification:**

$\mathrm{Sep} = \frac{\sum_i u_i D_i}{\sum_i u_i} = \frac{\sum_i u_i D_i}{m}$

$\mathcal{E}_{\mathrm{sep}} = \sum_i u_i(1 - D_i) = \sum_i u_i - \sum_i u_i D_i = m - \sum_i u_i D_i$

Therefore: $\sum_i u_i D_i = m - \mathcal{E}_{\mathrm{sep}}$

$\mathrm{Sep} = \frac{m - \mathcal{E}_{\mathrm{sep}}}{m} = 1 - \frac{\mathcal{E}_{\mathrm{sep}}}{m}$ $\quad\square$

**This is a 3-line algebraic identity. Fully proved. The paper states it as Proposition 1 (Sep Covariance Identity) but the simple identity above is the core result.** The covariance form in the paper is a more elaborate version involving $\mathbf{C}$-weighting. The simple identity should be stated separately and prominently.

---

## Theorem 9: Transport Fixed-Point Existence (paper Thm 9)

**Statement (conditional):** Under non-degeneracy, $\Phi : \Sigma_m \to \Sigma_m$ is continuous, hence has a fixed point by Brouwer.

### Verdict: SOUND (as a conditional theorem)

**Detailed analysis:**

1. **Brouwer hypotheses.** $\Sigma_m$ is compact and convex. $\Phi$ must be a continuous self-map. **Correct setup.**

2. **Continuity of $\Phi$.** The chain: $u_s \mapsto \phi_s$ (continuous by analyticity of $\mathrm{Cl}, D, C$) $\mapsto c(x,y)$ (continuous) $\mapsto M^*$ (continuous by strict convexity of entropy-regularized OT, Peyre 2019) $\mapsto u_s'$ (continuous by IFT at non-degenerate minimizer). **Each step is correct.**

3. **The non-degeneracy condition.** At Maxwell points (equal-energy minima), the minimizer can jump discontinuously. The paper explicitly flags this as the reason the theorem is conditional. **Honest and correct.**

4. **Self-mapping.** Does $\Phi$ map $\Sigma_m$ to $\Sigma_m$? The transported field may not lie on $\Sigma_m$ (sub-stochastic transport), but the subsequent energy minimization is on $\Sigma_m$, so the output is in $\Sigma_m$. **Correct.**

**This is a clean application of Brouwer. The conditionality is appropriately flagged.**

---

## Theorem 10: Temporal Core Inheritance (paper Thm 10, conditional)

**Statement:** Under epsilon-gentle transition and non-degeneracy, the minimizer persists and the core is inherited.

### Verdict: GAP (3 open gaps explicitly listed)

The proof sketch lists 3 closed gaps and 3 open gaps:
- **Closed:** epsilon-gentle definition precise; IFT on constrained manifold verified; volume re-projection bounded.
- **Open:** (4) basin radius via Morse theory; (5) transport concentration (core-to-core mapping); (6) interior gap lower bound.

Part (a) uses the implicit function theorem, which is standard. Part (c) uses $\|u_s - u_t\|_\infty \leq \|u_s - u_t\|_2$, which is correct. Part (d) uses Lipschitz continuity of Bind, which requires verifying that Bind is Lipschitz in the field (it is, since $\mathrm{Cl}$ is Lipschitz).

**The open gaps are explicitly listed and honestly assessed. The proved parts are sound.**

---

## Cross-Cutting Issues

### 1. Are all theorem hypotheses explicitly stated?

**Mostly yes, with exceptions:**
- Theorem 4 (Metastability) has an implicit "Gauss-Newton approximation valid" hypothesis and an implicit "$\nabla^2\mathcal{E}_{\mathrm{sep}}$ not too negative" condition.
- Theorem 7 (Gamma) has an implicit graph family specification.
- T-Bind has the explicit-but-uncontrolled $\bar{r}_0$ parameter.

### 2. Are any theorems stated for "general graphs" but only proved for grid graphs?

**No.** All theorems that are proved are proved for general finite weighted graphs. The computational claims (3 orders of magnitude discrimination, formation existence at 100% success rate) are specific to grid graphs but are clearly labeled as experimental.

### 3. Is the volume constraint $\Sigma_m$ used consistently?

**Yes.** The same $m$ (and $c = m/n$) appears throughout: T8-Core uses it for the phase transition criterion, the gradient projection uses it for feasibility, and the convergence theorem uses it for compactness. The constraint $\sum u_i = m$ is the same object everywhere.

**One subtlety:** The closure fixed point $u^*$ (from T6b) does NOT lie on $\Sigma_m$ in general ($\sum u^*_i \neq m$). This is acknowledged in the BIND-BOUND-PROOF as the source of the mean residual gap. The energy minimizer $\hat{u} \in \Sigma_m$ is not the closure fixed point. This distinction is correctly maintained throughout.

### 4. Implementation consistency

**Checked against code:**
- `energy.py:52`: $2\alpha u^T L u$ for smoothness — matches ordered-pair convention. **Correct.**
- `energy.py:64`: gradient $4\alpha Lu$ — matches. **Correct.**
- `energy.py:36`: $W'(u) = 2u(1-u)(1-2u)$ — matches I6 correction. **Correct.**
- `energy.py:87`: $\nabla\mathcal{E}_{\mathrm{cl}} = 2(J^T r - r)$ — matches the formula $-2(I-J)^T r$ (note: $J^T r - r = -(I-J)^T r$ when transposed correctly... let me check). Actually: $\nabla\mathcal{E}_{\mathrm{cl}} = 2(J_{\mathrm{Cl}} - I)^T(\mathrm{Cl}(u) - u)$. The code computes `JtR - residual` where `residual = Cl_u - u` and `JtR = J_Cl^T @ residual`. So the code gives $2(J_{\mathrm{Cl}}^T r - r) = 2(J_{\mathrm{Cl}}^T - I)r = -2(I - J_{\mathrm{Cl}})^T r$... wait. $(J_{\mathrm{Cl}} - I)^T = J_{\mathrm{Cl}}^T - I$. So $\nabla\mathcal{E}_{\mathrm{cl}} = 2(J_{\mathrm{Cl}}^T - I)r = 2(J_{\mathrm{Cl}}^T r - r)$. The code computes exactly this. **Correct.**
- `energy.py:108`: $\nabla\mathcal{E}_{\mathrm{sep}} = (1-D) - J_D^T u$ — this is the correct product-rule gradient: $\partial/\partial u_j[\sum_i u_i(1-D_i)] = (1-D_j) - \sum_i u_i \partial D_i/\partial u_j = (1-D)_j - (J_D^T u)_j$. **Correct.**
- `operators.py:97-102`: $J_{\mathrm{Cl}}^T v = ((1-\eta)I + \eta P^T)(\sigma' \cdot a_{\mathrm{cl}} \cdot v)$. Since $J_{\mathrm{Cl}} = \mathrm{diag}(\sigma' a_{\mathrm{cl}}) \cdot ((1-\eta)I + \eta P)$, the transpose is $((1-\eta)I + \eta P^T) \cdot \mathrm{diag}(\sigma' a_{\mathrm{cl}})$, applied to $v$: $((1-\eta)I + \eta P^T)(\sigma' a_{\mathrm{cl}} v)$. **Correct.**

---

## Summary Table

| Theorem | Paper Label | Verdict | Key Issue |
|---------|-------------|---------|-----------|
| Closure Contraction (T6) | Thm 1 | **SOUND** | Clean Banach contraction on complete metric space |
| Non-Idempotent Advantage (T3/T6) | Thm 2 | **GAP (minor)** | Sound at fixed point; Gauss-Newton extrapolation to minimizer uncontrolled |
| Phase Transition (T8-Core) | Thm 3 | **SOUND** | Strongest result. Fiedler vector in tangent space verified. Factor of 4 correct. |
| Enhanced Metastability (T7) | Thm 4 | **GAP (significant)** | Gauss-Newton residual not bounded; E_sep Hessian sign unstated |
| Gradient Flow (T14) | Thm 5 | **SOUND** | Lojasiewicz on semi-algebraic sets; all analyticity requirements met with $b_D = 0$ |
| Axiom Consistency (T20) | Thm 6 | **SOUND** | A1+A3 incompatibility is sharp |
| Gamma-Convergence (T11) | Thm 7 | **GAP (moderate)** | Graph family unspecified; surface tension correction is informal, not proved |
| Resolvent C1-C4 | Thm 8 | **GAP (known)** | C2 is computational; C3'' symmetrization gap is real and flagged |
| Transport FP Existence | Thm 9 | **SOUND** | Clean Brouwer, conditionality honest |
| Temporal Persistence | Thm 10 | **GAP (3 open)** | Open gaps explicitly listed; proved parts sound |
| Sep = 1 - E_sep/m | Prop 1 | **SOUND** | 3-line algebraic identity |
| T-Bind | Appendix | **GAP (honest)** | Tangential bound proved; mean residual uncontrolled; vacuous at default params |

**Bottom line:** 5 theorems are fully sound (T6, T8-Core, T14, T20, Sep identity). 1 has a minor gap (T3/T6-Stability, sound as stated but misapplied in T7). 4 have explicit, honestly flagged gaps (T7-Enhanced, T11, C-Axioms, T-Bind, T10). The strongest results — contraction, phase transition, gradient flow convergence — are clean. The weakest — metastability, Gamma surface tension correction — conflate proved results with heuristic claims.

**The single most damaging gap is Theorem 4 (Metastability):** the lower bound $\lambda_{\mathrm{cl}} \cdot 2(1-\|J\|)^2$ requires the Gauss-Newton approximation to dominate the residual correction, which requires a bound on $\|r\|$ that is not available without the mean residual control. Fix: either prove a full $\|r\|$ bound, or weaken the theorem to "enhancement holds for $\lambda_{\mathrm{cl}}$ sufficiently large" with an explicit threshold.
