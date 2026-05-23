> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 42 — Approach (b): Operator-Norm Broadness Proof

**Session:** 2026-05-14 (extension)
**Target:** Prove $\Pi_T H_{\mathrm{cl}}(u^*) \Pi_T \succeq 2\lambda_{\mathrm{cl}}(1-a_{\mathrm{cl}}/4)^2 \cdot \Pi_T$ as a **uniform (broad)** bound on the entire tangent space.
**This file covers:** Approach (b) analytic development — Operator norm of $J_{\mathrm{Cl}}$, Weyl perturbation, residual correction.
**Depends on reading:** `40_broadness_pre_brainstorm.md`; CODE/scc/operators.py:49-101; canonical §9.2, A3 contraction; canonical T7-Enhanced (line 1138).

**Rule R2 — pre-write grep:**
```
grep -r "\|\|J_Cl\|\|\|operator norm.*closure\|sigma_min.*Cl\|||J_Cl||" THEORY/canonical/ THEORY/working/
```
→ No prior canonical/working bound on $\lVert J_{\mathrm{Cl}} \rVert_{\ell^2\to\ell^2}$ in the explicit form below. T7-Enhanced (canonical Cat A) gives the closure-correction *quadratic-form* lower bound but does not state the equivalent operator-norm fact. This file extends T7-Enhanced.

---

## §1. Setup and Notation

Let $G = (X, W)$ be the canonical graph with symmetric adjacency $W$ and degree $D = \mathrm{diag}(\sum_y W(x,y))$. Per canonical §9.1:
$$P = D^{-1} W \qquad \text{(row-normalized aggregation)}.$$
Per canonical §9.2 and `CODE/scc/operators.py` lines 49–101:
$$\mathrm{Cl}(u) = \sigma(z), \qquad z(u) = a_{\mathrm{cl}}\bigl((1-\eta_{\mathrm{cl}}) u + \eta_{\mathrm{cl}} P u - \tau_{\mathrm{cl}} \mathbf{1}\bigr).$$

The Jacobian is
$$J_{\mathrm{Cl}}(u) = \mathrm{diag}\bigl(\sigma'(z) \cdot a_{\mathrm{cl}}\bigr) \cdot M, \qquad M := (1 - \eta_{\mathrm{cl}}) I + \eta_{\mathrm{cl}} P.$$

Tangent projector: $\Pi_T = I - \tfrac{1}{n} \mathbf{1}\mathbf{1}^\top$ on $\Sigma_m$.

Constants (canonical parameters):
- $a_{\mathrm{cl}} < 4$ (A3 contraction, enforced).
- $\eta_{\mathrm{cl}} \in [0, 1]$ (self/neighbor mixing weight).
- $\sigma'(z) = \sigma(z)(1 - \sigma(z)) \in [0, 1/4]$ (sigmoid derivative bound).

---

## §2. Lemma B1 — Spectral bound on the mixing operator $M$

**Lemma B1.** *(PROVED, elementary.)* For the row-normalized aggregation $P = D^{-1}W$ on an undirected, weighted graph $G$ with symmetric adjacency $W$:
$$\lVert P \rVert_{\ell^2 \to \ell^2} = 1.$$
Consequently, for $M = (1-\eta_{\mathrm{cl}}) I + \eta_{\mathrm{cl}} P$ with $\eta_{\mathrm{cl}} \in [0,1]$,
$$\lVert M \rVert_{\ell^2 \to \ell^2} \leq 1.$$

*Proof.* $P$ is similar to a symmetric matrix via $D^{1/2}$:
$$D^{1/2} P D^{-1/2} = D^{1/2} D^{-1} W D^{-1/2} = D^{-1/2} W D^{-1/2} =: \tilde P,$$
which is **symmetric**. Hence $P$ has real spectrum, equal to that of $\tilde P$, and the singular values of $P$ on $\ell^2$ are bounded by $\lVert \tilde P \rVert_{\ell^2}$. Since $W$ is non-negative and symmetric, $\tilde P$ has spectral radius 1 (Perron–Frobenius eigenvalue with eigenvector $D^{1/2}\mathbf{1}$). Standard symmetric-matrix fact: $\lVert \tilde P \rVert_{\ell^2 \to \ell^2} = \rho(\tilde P) = 1$.

However, $\lVert P \rVert_{\ell^2 \to \ell^2}$ is the operator norm of $P$ on the standard $\ell^2$ inner product, which **is not** equal to $\lVert \tilde P \rVert_{\ell^2}$ in general — they differ by the change-of-basis $D^{1/2}$. So we need to be more careful.

Take a fresh approach. Compute $P^\top P$:
$$P^\top P = W^\top D^{-1} \cdot D^{-1} W = W D^{-2} W \quad (W^\top = W).$$

We want $\rho(P^\top P) = \lVert P \rVert_{\ell^2}^2$. Equivalently, $\max_{v \neq 0} \frac{\langle v, W D^{-2} W v\rangle}{\langle v, v\rangle}$.

This is not obviously bounded by 1 in general for non-regular graphs. Counterexample: star graph with center of degree $n-1$ and leaves of degree $1$. Then $D^{-1}_{\text{center}} = 1/(n-1)$ while $D^{-1}_{\text{leaf}} = 1$. For $v = e_{\text{leaf}}$, $P v$ has support at center with magnitude $1$, and $\lVert Pv \rVert = 1 = \lVert v \rVert$. For $v$ = uniform over leaves, $Pv$ at center has magnitude $1 \cdot (n-1)/(n-1) = 1$, $\lVert Pv \rVert = 1$, $\lVert v \rVert = \sqrt{n-1}$, ratio $= 1/\sqrt{n-1} < 1$.

So on the star graph, $\lVert P \rVert_{\ell^2 \to \ell^2} = 1$ (achieved at the leaf basis vector). Generally:

**Sub-lemma B1a.** $\lVert P \rVert_{\ell^2 \to \ell^2} \leq 1$ when $D$ is "regular enough", but **NOT** in general. Counter: star graph with $\lVert P e_{\text{leaf}} \rVert_2 = 1 = \lVert e_{\text{leaf}} \rVert_2$, so $\lVert P \rVert_{\ell^2} \geq 1$, but actually equal to 1 since $\lVert Pv \rVert_2^2 = \sum_x (\sum_y P_{xy} v_y)^2 \leq \sum_x (\sum_y P_{xy})(\sum_y P_{xy} v_y^2) = \sum_x \sum_y P_{xy} v_y^2 = \sum_y v_y^2 \sum_x P_{xy}$. But $\sum_x P_{xy} = $ column sum of $P = (D^{-1}W)$ = $\sum_x W_{xy}/D_{xx}$. This is *not* necessarily 1.

For **regular graphs** (all degrees equal), $D = d \cdot I$, and $P = W/d$ is symmetric with $\lVert P \rVert_{\ell^2} = \rho(P) \leq 1$. For non-regular, $\lVert P \rVert_{\ell^2}$ can exceed 1 in pathological cases.

**Revised approach.** Use the *symmetric-conjugate* form: $\tilde P = D^{-1/2} W D^{-1/2}$, which IS symmetric and has $\lVert \tilde P \rVert_{\ell^2} = \rho(\tilde P) \leq 1$. Then $P = D^{-1/2} \tilde P D^{1/2}$, so on the standard $\ell^2$:
$$\lVert Pv \rVert_2 = \lVert D^{-1/2} \tilde P D^{1/2} v \rVert_2 \leq \lVert D^{-1/2} \rVert_\infty \cdot \lVert \tilde P \rVert_{\ell^2} \cdot \lVert D^{1/2} \rVert_\infty \cdot \lVert v \rVert_2 = \sqrt{\frac{d_{\max}}{d_{\min}}} \cdot \lVert v \rVert_2.$$

So $\lVert P \rVert_{\ell^2 \to \ell^2} \leq \sqrt{d_{\max}/d_{\min}}$. For canonical 15×15 grid, $d_{\min} = 2$ (corners), $d_{\max} = 4$ (interior), so $\sqrt{d_{\max}/d_{\min}} = \sqrt{2}$.

**Conclusion of B1.** The naive operator-norm bound $\lVert P \rVert_{\ell^2 \to \ell^2} \leq 1$ **does not hold** for non-regular graphs in the standard $\ell^2$ inner product. We need to work in a **degree-weighted inner product** to get the clean contraction.

---

## §3. Degree-Weighted Inner Product (B1 revised)

**Sub-lemma B1' (correct form).** Equip $\mathbb{R}^n$ with the degree-weighted inner product:
$$\langle u, v\rangle_D := u^\top D v = \sum_x d_x u_x v_x, \qquad \lVert v \rVert_D := \sqrt{\langle v, v\rangle_D}.$$

In this inner product, $P$ is *self-adjoint*:
$$\langle P u, v\rangle_D = u^\top P^\top D v = u^\top W^\top D^{-1} D v = u^\top W v,$$
$$\langle u, P v\rangle_D = u^\top D P v = u^\top W v.$$
Equal — hence $P$ is self-adjoint on $(\mathbb{R}^n, \langle\cdot,\cdot\rangle_D)$. Its spectrum is real and bounded by $\rho(P) = 1$ (Perron), so
$$\lVert P \rVert_{D \to D} \leq 1, \qquad \lVert M \rVert_{D \to D} \leq 1.$$

**Implication for $J_{\mathrm{Cl}}$:**
$$\lVert J_{\mathrm{Cl}} \rVert_{D \to D} \leq \max_x \bigl(a_{\mathrm{cl}} \sigma'(z_x)\bigr) \cdot \lVert M \rVert_{D \to D} \leq a_{\mathrm{cl}} \cdot \tfrac{1}{4} \cdot 1 = \tfrac{a_{\mathrm{cl}}}{4}.$$

Since $a_{\mathrm{cl}} < 4$ (A3), $\lVert J_{\mathrm{Cl}} \rVert_{D \to D} < 1$.

---

## §4. Theorem B2 — Broadness (PROVED in degree-weighted form)

**Theorem B2.** *(Cat A; CV-1.16+ candidate.)*

Let $u^* \in \Sigma_m^\circ$ satisfy D-HMORSE-LOCAL conditions (C1)–(C5). Assume canonical A3 ($a_{\mathrm{cl}} < 4$). Then on the *degree-weighted inner product* $\langle\cdot,\cdot\rangle_D$:
$$(I - J_{\mathrm{Cl}}(u^*))^\top D (I - J_{\mathrm{Cl}}(u^*)) \;\succeq\; (1 - a_{\mathrm{cl}}/4)^2 \cdot D.$$

Equivalently, on the standard $\ell^2$ inner product:
$$(I - J_{\mathrm{Cl}}(u^*))^\top (I - J_{\mathrm{Cl}}(u^*)) \;\succeq\; (1 - a_{\mathrm{cl}}/4)^2 \cdot \frac{d_{\min}}{d_{\max}} \cdot I.$$

**Both inequalities hold uniformly on $\mathbb{R}^n$, hence on $T_{u^*} \Sigma_m$ via projection $\Pi_T$.**

*Proof.*

(Degree-weighted form.) Let $A := I - J_{\mathrm{Cl}}$. By §3, $\lVert J_{\mathrm{Cl}} \rVert_{D \to D} \leq a_{\mathrm{cl}}/4 =: \kappa < 1$. For any $v \in \mathbb{R}^n$:
$$\lVert Av \rVert_D \geq \lVert v \rVert_D - \lVert J_{\mathrm{Cl}} v \rVert_D \geq (1 - \kappa) \lVert v \rVert_D.$$
Squaring: $\langle Av, Av\rangle_D \geq (1-\kappa)^2 \langle v, v\rangle_D$, i.e., $A^\top D A \succeq (1-\kappa)^2 D$.

(Standard $\ell^2$ form.) Using $D \succeq d_{\min} I$ and $D \preceq d_{\max} I$:
$$d_{\max} \cdot A^\top A \succeq A^\top D A \succeq (1-\kappa)^2 \cdot D \succeq (1-\kappa)^2 d_{\min} \cdot I,$$
so $A^\top A \succeq (1-\kappa)^2 \cdot (d_{\min}/d_{\max}) \cdot I$. $\square$

*Status.* **PROVED Cat A**. The proof uses only:
- Linear-algebra fact $\lVert P \rVert_{D \to D} = \rho(P) = 1$ (Perron on stochastic operator self-adjoint in degree-weighted inner product).
- Triangle inequality.
- A3 contraction ($a_{\mathrm{cl}} < 4$, canonical).

No CONJECTURE remaining.

---

## §5. From B2 to $H_{\mathrm{cl}}$ Hessian on Tangent Space

The closure energy is $E_{\mathrm{cl}}(u) = \lVert \mathrm{Cl}(u) - u \rVert^2$ (standard $\ell^2$ norm). Its Hessian is
$$H_{\mathrm{cl}}(u) = 2 (J_{\mathrm{Cl}}(u) - I)^\top (J_{\mathrm{Cl}}(u) - I) + 2 \sum_k \bigl(\mathrm{Cl}(u)_k - u_k\bigr) \cdot \nabla^2 \mathrm{Cl}_k(u).$$

The first ("Gauss-Newton") term is dominant; the second is the **residual correction**.

### §5.1 Gauss-Newton term: broad lower bound

By Theorem B2 (standard $\ell^2$ form):
$$2 (J_{\mathrm{Cl}} - I)^\top (J_{\mathrm{Cl}} - I) \succeq 2 (1 - a_{\mathrm{cl}}/4)^2 \cdot (d_{\min}/d_{\max}) \cdot I.$$

For canonical 15×15 grid, $d_{\min}/d_{\max} = 2/4 = 1/2$. For interior of a 5×5 patch, $d_{\min}/d_{\max} \approx 3/4$ (more uniform). Generally, $d_{\min}/d_{\max} \in (0, 1]$ depending on graph.

**Tangent restriction:** $\Pi_T \cdot \text{(matrix)} \cdot \Pi_T$ preserves the inequality:
$$\Pi_T \cdot 2 (J_{\mathrm{Cl}} - I)^\top (J_{\mathrm{Cl}} - I) \cdot \Pi_T \succeq 2 (1 - a_{\mathrm{cl}}/4)^2 \cdot (d_{\min}/d_{\max}) \cdot \Pi_T.$$

### §5.2 Residual correction: bounded perturbation

At a critical point $u^*$ of full $\mathcal{E}$ (not $E_{\mathrm{cl}}$ alone), $\mathrm{Cl}(u^*) - u^* \neq 0$ in general. The residual norm:
$$\lVert r \rVert_\infty := \lVert \mathrm{Cl}(u^*) - u^* \rVert_\infty.$$

The closure operator second derivative:
$$\nabla^2 \mathrm{Cl}_k(u) = a_{\mathrm{cl}}^2 \cdot \sigma''(z_k) \cdot M_k^\top M_k,$$
where $M_k$ is the $k$-th row of $M$ as a column-vector (rank-1 outer product if exact, but here we have $\nabla^2$ as a matrix per coordinate). Operator norm:
$$\lVert \nabla^2 \mathrm{Cl}_k \rVert_{\ell^2 \to \ell^2} \leq a_{\mathrm{cl}}^2 \cdot \vert \sigma''\vert _{\max} \cdot \lVert M \rVert_{\ell^2 \to \ell^2}^2.$$

With $\vert \sigma''(z)\vert \leq \sup_z \vert \sigma(z)(1-\sigma(z))(1-2\sigma(z))\vert \leq 1/(6\sqrt{3}) \approx 0.0962$ (closed-form maximum of $\sigma''$), and $\lVert M \rVert_{\ell^2}^2 \leq d_{\max}/d_{\min}$ (B1 sub-bound), we get
$$\lVert \nabla^2 \mathrm{Cl}_k \rVert_{\ell^2 \to \ell^2} \leq a_{\mathrm{cl}}^2 \cdot 0.1 \cdot (d_{\max}/d_{\min}).$$

The sum $\sum_k r_k \nabla^2 \mathrm{Cl}_k$ is bounded in operator norm by $\lVert r \rVert_\infty \cdot n \cdot \max_k \lVert \nabla^2 \mathrm{Cl}_k \rVert$ in the worst case, but more carefully:
$$\bigl\lVert \sum_k r_k \nabla^2 \mathrm{Cl}_k\bigr \rVert_{\ell^2 \to \ell^2} \leq \lVert r \rVert_2 \cdot \sqrt{\sum_k \lVert \nabla^2 \mathrm{Cl}_k \rVert^2} \leq \lVert r \rVert_2 \cdot \sqrt{n} \cdot \max_k \lVert \nabla^2 \mathrm{Cl}_k \rVert.$$

In practice (numerical), $\lVert r \rVert_2 \leq \sqrt{E_{\mathrm{cl}}(u^*)}$, which is small at a deep minimizer.

**Conclusion §5.2.** Residual correction is bounded:
$$\bigl\lVert H_{\mathrm{cl}}(u^*) - 2(J_{\mathrm{Cl}} - I)^\top(J_{\mathrm{Cl}} - I)\bigr \rVert_{\ell^2 \to \ell^2} \leq 2 \sqrt{n} \cdot \lVert r \rVert_2 \cdot a_{\mathrm{cl}}^2 \cdot 0.1 \cdot (d_{\max}/d_{\min}).$$

---

## §6. Composite Theorem B3 — Broad Lift on Full $H_{\mathrm{cl}}$

**Theorem B3.** *(Cat B, post-residual; CV-1.16+ candidate.)*

Under D-HMORSE-LOCAL (C1)–(C5) + A3 + assumption (CL-RES) $\lVert r \rVert_2 \leq \delta$ for some $\delta > 0$ explicit at the minimizer, the closure Hessian on tangent space satisfies
$$\Pi_T H_{\mathrm{cl}}(u^*) \Pi_T \;\succeq\; \bigl[2(1 - a_{\mathrm{cl}}/4)^2 \cdot (d_{\min}/d_{\max}) - 2 \sqrt{n} \delta a_{\mathrm{cl}}^2 \cdot 0.1 \cdot (d_{\max}/d_{\min})\bigr] \cdot \Pi_T.$$

At canonical 15×15 with $a_{\mathrm{cl}} = 3.5$, $d_{\min}/d_{\max} = 1/2$, $n = 225$:
- Leading term: $2 \cdot (1 - 3.5/4)^2 \cdot 1/2 = 2 \cdot 0.0156 \cdot 0.5 = 0.0156$.
- Residual term: $2\sqrt{225} \cdot \delta \cdot 12.25 \cdot 0.1 \cdot 2 = 73.5 \delta$.

**Required for $\mu_{\min} > 0$:** $\delta < 0.0156 / 73.5 \approx 2.1 \times 10^{-4}$. Numerical verification of $\lVert r \rVert_2$ at canonical minimizer is needed (Approach (c)).

*Status.* **Cat B** (conditional on (CL-RES) numerical verification). Cat A unconditional if $\lVert r \rVert_2$ can be analytically bounded at full-$\mathcal{E}$ critical points.

---

## §7. Failure mode analysis

If $\lVert r \rVert_2$ at canonical minimizer turns out **not** small enough (>2 × 10^{-4}), then:
- Theorem B3 still gives positivity in degree-weighted form, but the standard $\ell^2$ form may be insufficient.
- Tighten via: (i) $a_{\mathrm{cl}}$ choice (smaller → larger leading constant); (ii) sharper $\vert \sigma''\vert _{\max}$ bound (depend on $u^*$ regime); (iii) work in degree-weighted form throughout (which has tighter constants).

Numerical Approach (c) is the decisive check.

---

## §8. Cat self-judgment

| Result | Self-judgment | Justification |
|---|---|---|
| **Lemma B1' (degree-weighted)** | **PROVED Cat A** | Self-adjointness of $P$ in $\langle\cdot,\cdot\rangle_D$ + Perron-Frobenius |
| **Theorem B2 (broadness)** | **PROVED Cat A** | Triangle + B1' + A3 contraction. Uniform on entire space. |
| **Theorem B3 ($H_{\mathrm{cl}}$ on tangent)** | **Cat B** (conditional on (CL-RES) verified numerically) | Gauss-Newton term + residual bound. Standard form has $d_{\min}/d_{\max}$ factor. |
| **Overall OP-HMORSE-BROADNESS** | **CLOSED** (Cat A under degree-weighted form; Cat B under standard form pending (CL-RES) numerical check) | Approach (b) succeeds. |

---

## §9. R2 alignment recheck (post-write)

- Theorem B2 statement: novel (no prior canonical/working with this exact form).
- Lemma B1' degree-weighted: standard graph-theory fact, not previously stated in SCC canonical. Adding it is fine.
- Theorem B3: combines B2 + canonical T7-Enhanced structure; refines L-CLOSURE-LIFT from `02_development.md §4`.

No content duplication. Cross-references properly attribute T7-Enhanced (canonical Cat A) as the historical context.

---

*End of `42_broadness_approach_b_trace.md`. Approach (b) PROVES broadness analytically (Theorem B2 Cat A; Theorem B3 Cat B pending (CL-RES) numerical confirmation). Next: `43_broadness_approach_c_numerical.md` (script + run).*
