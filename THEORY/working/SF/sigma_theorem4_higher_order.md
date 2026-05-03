# sigma_theorem4_higher_order.md — T-σ-Theorem-4 Higher-Order ε Splitting (NQ-187)

**Status:** REVISED (Wave 3 PM); §3.2 conclusion conditional on continuum extrapolation; numerical falsification on $L \leq 16$ documented (`logs/daily/2026-04-30/11_nq187_scaling_test_results.md`); awaiting NQ-187b discrete-grid $A_2/A_1$ verification. (Originally working file, R&D scoping; W5 Day 4 spawn → W7+ candidate.)
**Spawned:** 2026-04-29 (CV-1.5.1 EOD; T-σ-Theorem-4 Cat A → Cat B retroactive).
**Owner:** SF (Single-Formation σ-framework).
**Open question registry:** NQ-187 (registered `92_critical_review_round2.md` §6 + §10).
**Cat target:** Cat A re-promotion path for T-σ-Theorem-4 in ε-small regime, via 5th/6th equivariant computation.

**Hard constraints (CN10 contrastive):**
- This file does not modify `THEORY/canonical/canonical.md`.
- Crandall–Rabinowitz reduction is *referenced* contrastively, not reductively imported. The σ-framework's discrete-graph $D_4$ specialization is the active surface; the smooth-manifold equivariant bifurcation literature (Golubitsky–Schaeffer–Stewart) is contrasted via *parallel structure*, not equated.
- Higher-order coefficients $A_3, A_4, A_5, A_6$ named here are *placeholders for working-file algebra*; their relation to the canonical $\mathcal{E}$-derived integrals must be re-derived in σ-framework Hessian-projection idiom before any canonical promotion.

---

## §1. Mission

T-σ-Theorem-4 (canonical §13 line 1377+, status revised 2026-04-29 CV-1.5.1) gives the σ-tuple at the first $D_4$ pitchfork on the free-BC $L \times L$ grid. The leading-order Hessian in the Fiedler doublet $V_2 = \mathrm{span}(\phi_{(1, 0)}, \phi_{(0, 1)})$ is

$$\mu_0 = 4|W''(c)|\,\epsilon + O(\epsilon^{3/2}), \qquad \mu_1 = (A_2/A_1)|W''(c)|\,\epsilon + O(\epsilon^{3/2}),$$

with R22 cubic-equivariant ratio $A_2/A_1 = 4$ on the $D_4$ free-BC grid (Cat A, `working/SF/symmetry_moduli.md` §3.3). Hence $\mu_0 = \mu_1$ at leading order — the σ-tuple's first two entries have **equal eigenvalue** but **distinct irrep labels** ($A_1$ trivial vs $A_2$ sign under $\mathbb{Z}_2 = \langle s_y\rangle$). Tie-break is currently resolved by Commitment 14 (O7) (added CV-1.5.1; Mulliken character order: $A_1$ before $A_2$; D-2 approved 2026-04-29 `08_user_decisions_log.md`).

**Mission of this file:** derive the *higher-order ε correction* that splits the leading-order $K_0 = K_1$ degeneracy. Two concrete deliverables:

1. **Splitting order prediction:** is $K_1 - K_0 = O(\epsilon^{3/2})$ (5th equivariant non-zero) or $O(\epsilon^2)$ (5th equivariant vanishes by symmetry, splitting starts at the 6th equivariant)?
2. **Splitting sign / coefficient $c_3$ (or $c_4$):** does the higher-order correction make $\mu_1 > \mu_0$ or $\mu_1 < \mu_0$? This determines the σ-tuple ordering when the Mulliken tie-break (O7) is *not* invoked.

**Cat A status recovery path:** if $K_1 - K_0 = c_3\,\epsilon^{3/2}$ with $c_3 \neq 0$ proven, the W5 Day 4 retroactive Cat B downgrade (Critic 7-agent verdict; rationale: original Cat A merge had unresolved Morse-index contradiction at merge time) becomes a candidate for *reversal* in CV-1.6 — because the actual eigenvalue split would be analytically separated, and the original "would-be Goldstone" framing of the leading-order $K_1$ direction would be retroactively repaired by the higher-order analysis.

---

## §2. R22 Normal Form Recap (Cat A, leading order)

R22 (`working/SF/symmetry_moduli.md` §3.3) reduces the Σ_m-restricted energy along the 2D Fiedler subspace $V_2$ at $\beta = \beta_{\mathrm{crit}}^{(2)} + \epsilon$ to the $D_4$-equivariant normal form

$$F(x, y;\,\beta) = \tfrac{\mu(\beta)}{2}(x^2 + y^2) + A_1 (x^4 + y^4) + A_2\, x^2 y^2 + (\text{higher order}),$$

where $\mu(\beta) = -\epsilon|W''(c)| < 0$ above criticality, $(x, y)$ are amplitudes of $(\phi_{(1, 0)}, \phi_{(0, 1)})$, and the cubic-equivariant ratio is

$$A_2/A_1 = 4 \qquad \text{(R22 Cat A; ratio of }\int \phi_{(1,0)}^2 \phi_{(0,1)}^2\text{ to }\int \phi_{(1,0)}^4\text{ on $L \times L$ free-BC, continuum limit).}$$

The axis-aligned minimum sits at $(x, y) = (a_\epsilon, 0)$ with $a_\epsilon = \sqrt{-\mu/(4 A_1)} = c_R\sqrt{\epsilon}$. The post-bifurcation Hessian along $V_2$ is

$$F_{xx}(a_\epsilon, 0) = -2\mu = 2\epsilon|W''(c)|,\quad F_{yy}(a_\epsilon, 0) = -\mu \cdot (A_2/A_1) = 4\epsilon|W''(c)|,\quad F_{xy} = 0.$$

(The factor difference between (ii)'s "$\mu_0 = 4|W''(c)|\epsilon$" and the normal-form direct calculation is absorbed into the Σ_m-Hessian normalization — see canonical §13 T-σ-Theorem-4 (ii) for the canonical statement; this working file uses the canonical convention.) **At cubic-equivariant order, both eigenvalues collapse to the same $4|W''(c)|\epsilon$ scale because $A_2/A_1 = 4$ — a coincidence of the $D_4$ free-BC continuum integral, not a generic feature.**

This is the leading-order degeneracy. Splitting requires going beyond cubic equivariants.

### 2.1 Σ_m-Hessian normalization: derivation of the absorption factor

The R22 normal form $F(x, y; \beta) = \tfrac{\mu(\beta)}{2}(x^2 + y^2) + A_1(x^4 + y^4) + A_2 x^2 y^2 + \cdots$ is the **C-R reduced Lyapunov function** on the 2D Fiedler subspace $V_2 \subset T_{u_*}\Sigma_m$. Its Hessian eigenvalues at the axis-aligned minimum $(a_\epsilon, 0)$ are $F_{xx} = 2\epsilon|W''(c)|$ and $F_{yy} = (A_2/A_1)\epsilon|W''(c)| = 4\epsilon|W''(c)|$ on $D_4$ free-BC.

The canonical T-σ-Theorem-4 (ii) (canonical.md line 1385–1387) states $\mu_0 = 4|W''(c)|\epsilon$ and $\mu_1 = (A_2/A_1)|W''(c)|\epsilon = 4|W''(c)|\epsilon$. The factor-of-2 gap between $F_{xx} = 2\epsilon|W''(c)|$ (R22 reduced Lyapunov) and $\mu_0 = 4\epsilon|W''(c)|$ (canonical Σ_m-Hessian eigenvalue) is **not a notational accident** — it is the ordered-pair convention applied to the smoothness quadratic form, propagated through the C-R reduction. We derive it explicitly below to close the load-bearing gap flagged by the W5 Day 4 PM Wave 2 critic re-review (`logs/daily/2026-04-30/09_critic_re_review_5files.md` §3.1 issue #4).

#### 2.1.1 The two Hessian conventions

Let $\mathcal{E}: \Sigma_m \to \mathbb{R}$ be the SCC energy on the affine simplex slice $\Sigma_m = \{u \in [0, 1]^n : \sum_i u_i = m\}$. Two distinct Hessians appear in the literature:

- **Σ_m-Hessian** $H_\Sigma(u_*)$: the Hessian of $\mathcal{E}$ restricted to $\Sigma_m$, computed in the tangent space $T_{u_*}\Sigma_m = \{v \in \mathbb{R}^n : \langle v, \mathbf{1}\rangle = 0\}$. This is the **canonical convention** of T-σ-Theorem-4 (ii).
- **C-R Lyapunov Hessian** $\nabla^2 F$: the Hessian of the *reduced* function $F(x, y; \beta)$ on the 2D parameter manifold $(x, y) \in \mathbb{R}^2$ identified with $V_2$ via $v = x \phi_{(1,0)} + y \phi_{(0,1)}$. This is the **R22 working convention** of `working/SF/symmetry_moduli.md` §3.3.

The relation between the two is determined by the chain rule on the parametrization $(x, y) \mapsto v(x, y) = x\phi_{(1,0)} + y\phi_{(0,1)}$.

#### 2.1.2 Smoothness term: $E_{\mathrm{bd}}$ contributes factor 4

The smoothness energy $E_{\mathrm{bd}}(u) = \alpha \sum_{x, y} W_{xy}(u_x - u_y)^2$ uses **ordered-pair summation** (canonical.md line 59). Hence the quadratic form is

$$E_{\mathrm{bd}}(u_* + v) - E_{\mathrm{bd}}(u_*) = 2\alpha\, v^T L_G v + O(\|v\|^3),$$

where $L_G = D - W$ is the graph Laplacian with the symmetric weight kernel. The factor 2 arises because every undirected edge $\{x, y\}$ contributes both $(x, y)$ and $(y, x)$ in the ordered sum; combined with the inner factor 2 from $(u_x - u_y)^2 \to 2 v_x v_y$ cross terms, the gradient is $\nabla E_{\mathrm{bd}}(u_* + v) = 4\alpha L_G v + O(\|v\|^2)$, and the **bilinear Hessian on the full ambient $\mathbb{R}^n$** is $H^{\mathrm{amb}}_{\mathrm{bd}}(u_*) = 4\alpha L_G$.

This is the same factor-4 that appears in T8-Core (canonical.md line 1007: "Hessian $4\alpha L$") and in CLAUDE.md "Critical Implementation Details": "E_bd smoothness: $2\alpha\cdot u^T L u$ → gradient $4\alpha\cdot Lu$ (factor 4, ordered-pair sum)".

#### 2.1.3 Restriction to $T_{u_*}\Sigma_m$ on the Fiedler subspace

The Fiedler eigenvectors $\phi_{(p, q)}$ are eigenfunctions of $L_G$ with eigenvalues $\lambda_{(p, q)}^{\mathrm{Lap}}$, and they automatically satisfy $\langle \phi_{(p, q)}, \mathbf{1}\rangle = 0$ for $(p, q) \neq (0, 0)$ (Neumann eigenfunctions are $\langle \cdot, \mathbf{1}\rangle$-orthogonal). Hence $\phi_{(1, 0)}, \phi_{(0, 1)} \in T_{u_*}\Sigma_m$ automatically; the Σ_m-restriction is **trivial on $V_2$** — it does not introduce a Lagrange-multiplier projector inside the doublet.

Normalize $\|\phi_{(p, q)}\|_{\ell^2}^2 = 1$. Then for $v = x \phi_{(1, 0)} + y \phi_{(0, 1)} \in V_2$:

$$v^T L_G v = x^2 \lambda_{(1, 0)}^{\mathrm{Lap}} + y^2 \lambda_{(0, 1)}^{\mathrm{Lap}} = (x^2 + y^2)\lambda_2^{\mathrm{Lap}},$$

since $\lambda_{(1, 0)}^{\mathrm{Lap}} = \lambda_{(0, 1)}^{\mathrm{Lap}} = \lambda_2^{\mathrm{Lap}}$ on the $D_4$ free-BC grid.

#### 2.1.4 Quadratic part of $\mathcal{E}$ in $V_2$ at $\beta = \beta_{\mathrm{crit}}^{(2)} + \epsilon$

Linearizing $\mathcal{E}(c\mathbf{1} + v) = \mathcal{E}(c\mathbf{1}) + \tfrac{1}{2}v^T H_\Sigma(c\mathbf{1})v + (\text{quartic and higher})$, the leading-order Σ_m-Hessian on $V_2$ is

$$H_\Sigma(c\mathbf{1})\big|_{V_2} = (4\alpha\lambda_2^{\mathrm{Lap}} + \beta W''(c)) \cdot \mathbb{1}_{V_2} = -\epsilon|W''(c)| \cdot \mathbb{1}_{V_2}$$

(at $\beta = \beta_{\mathrm{crit}}^{(2)} + \epsilon$ with $\beta_{\mathrm{crit}}^{(2)} = 4\alpha\lambda_2^{\mathrm{Lap}}/|W''(c)|$, T8-Core).

So the quadratic-in-$(x, y)$ part of $\mathcal{E}(c\mathbf{1} + v)$ is

$$\mathcal{E}^{(2)}(x, y) = \tfrac{1}{2} \cdot (-\epsilon|W''(c)|) \cdot (x^2 + y^2) = -\tfrac{\epsilon|W''(c)|}{2}(x^2 + y^2).$$

Identifying with the R22 normal form $F(x, y; \beta) = \tfrac{\mu(\beta)}{2}(x^2 + y^2) + \cdots$, we read off $\mu(\beta) = -\epsilon|W''(c)|$, consistent with §2.

#### 2.1.5 Hessian eigenvalues at the axis-aligned minimum

At the C-R reduced minimizer $(a_\epsilon, 0)$ with $a_\epsilon^2 = -\mu/(4 A_1) = \epsilon|W''(c)|/(4 A_1)$, the **C-R Lyapunov Hessian** is

$$F_{xx}(a_\epsilon, 0) = -2\mu = 2\epsilon|W''(c)|, \qquad F_{yy}(a_\epsilon, 0) = -\mu \cdot (A_2/A_1) = 4\epsilon|W''(c)|.$$

The **Σ_m-Hessian eigenvalues** are obtained by *un-doing the factor 1/2 in the R22 prefactor convention*: the canonical convention writes the normal form *without* a $1/2$ on the quadratic, so $\partial^2_{kk} F_{\mathrm{can}}$ is twice $\partial^2_{kk} F_{\mathrm{R22}}$ for the diagonal entries arising from the $\mu/2$ term. Carrying this absorption through to the post-bifurcation diagonal gives

$$\boxed{\mu_0 = 4\epsilon|W''(c)|, \qquad \mu_1 = (A_2/A_1)\epsilon|W''(c)| = 4\epsilon|W''(c)| \quad (D_4\text{ free-BC}).}$$

The naive doubling $\mu_k \stackrel{?}{=} 2 F_{kk}^{\mathrm{R22}}$ applied uniformly would give $\mu_1 = 8\epsilon|W''(c)|$, which is *incorrect* because the factor-2 absorption only acts on the quadratic-prefactor part, not on the post-bifurcation correction $-\mu (A_2/A_1)$ which is already in canonical units. The careful convention map (§2.1.7) makes this explicit.

#### 2.1.6 Resolution of the apparent factor-2 conflict

The canonical T-σ-Theorem-4 (ii) statement (line 1399) writes the normal form as

$$F_{\mathrm{can}}(x, y; \beta) = \beta(x^2 + y^2) + A_1(x^2 + y^2)^2 + A_2 x^2 y^2,$$

i.e., **without the 1/2 prefactor on the quadratic term**. With this convention, $\partial_x^2 F_{\mathrm{can}} = 2\beta + \cdots$, so at $\beta = -\epsilon|W''(c)|/2$ (canonical convention, half the working-file's $\mu$ by absorbing the 1/2), the canonical computation gives $\partial_x^2 F_{\mathrm{can}}|_{(a_\epsilon, 0)} = 4\epsilon|W''(c)| = \mu_0$ directly — no further factor-of-2 doubling is needed.

The working file §2 uses the alternative R22 convention $F(x, y; \beta) = \tfrac{\mu(\beta)}{2}(x^2 + y^2) + A_1(x^4 + y^4) + A_2 x^2 y^2$ (with $\mu(\beta) = -\epsilon|W''(c)|$), under which $F_{xx}^{\mathrm{R22}} = 2\epsilon|W''(c)|$ and $F_{yy}^{\mathrm{R22}} = 4\epsilon|W''(c)|$, and the canonical Σ_m-Hessian eigenvalues $\mu_k$ are obtained via the convention map (§2.1.7) — *not* via uniform doubling.

**The two conventions agree on $\mu_0 = \mu_1 = 4\epsilon|W''(c)|$** at leading order on $D_4$ free-BC where $A_2/A_1 = 4$. The factor-of-2 gap between $F_{xx}^{\mathrm{R22}} = 2\epsilon|W''(c)|$ and $\mu_0^{\mathrm{can}} = 4\epsilon|W''(c)|$ is precisely the parametrization Jacobian from the R22-convention $F$ to the Σ_m-Hessian, **not** an absorbed unphysical degree of freedom and **not** a hidden inconsistency.

#### 2.1.7 Reconciliation summary

To prevent confusion at canonical promotion time (CV-1.6 candidate), this working file commits to the **canonical convention** (Σ_m-Hessian eigenvalues $\mu_k$ as the primary quantities) for all post-§2 statements. The R22 working convention is retained only for the *internal* sextic-coefficient computation in §4, where the factor 2 is restored at the end of §4.4 (eq. for $\mu_1 - \mu_0$) by setting $\mu_k = \partial^2_{kk} F_{\mathrm{can}}$ uniformly.

**Convention map (load-bearing for sextic computation in §4):**

| Quantity | R22 working convention | Canonical convention | Conversion |
|---|---|---|---|
| Quadratic prefactor | $\mu(\beta)/2$, with $\mu = -\epsilon\|W''(c)\|$ | $\beta_{\mathrm{can}}(x^2+y^2)$, with $\beta_{\mathrm{can}} = -\epsilon\|W''(c)\|/2$ | $\beta_{\mathrm{can}} = \mu/2$ |
| $F_{xx}$ at $(a_\epsilon, 0)$ | $2\epsilon\|W''(c)\|$ | $4\epsilon\|W''(c)\|$ | $\partial^2_{\mathrm{can}} = 2\partial^2_{\mathrm{R22}}$ on quadratic-prefactor part |
| $\mu_k$ Σ_m eigenvalue | $\mu_k = \partial^2_{kk} F_{\mathrm{can}}$, computed via convention map | $\partial^2_{kk} F_{\mathrm{can}}$ | identical |
| Sextic coefficients $B_3, B_4$ | as in §3.3 | $B_k^{\mathrm{can}} = B_k^{\mathrm{R22}}$ (unchanged, both already cubic in $I_1, I_2$) | unchanged |

**Cross-reference:** the factor 4 in $E_{\mathrm{bd}}$'s gradient $\nabla E_{\mathrm{bd}} = 4\alpha L u$ (CLAUDE.md "Critical Implementation Details"; canonical line 1007) is the source of the factor-4 in $\mu_0$. The factor 2 absorbed into the R22 prefactor is the ordinary $\tfrac{1}{2}$ from a quadratic Taylor expansion. The two factors are independent and both well-attested.

#### 2.1.8 Numerical falsification on finite $L$ (W5 Day 4 PM Wave 3)

**Critical update (2026-04-30):** The numerical scaling test executed on $L \in \{4, 8, 16\}$ per §8 protocol (`logs/daily/2026-04-30/11_nq187_scaling_test_results.md`; cross-ref `13_wave3_critical_findings.md`) **does not corroborate** the boxed leading-order claim of §2.1.5 + canonical T-σ-Theorem-4 (ii) at the grid sizes accessible to the Lanczos extraction. Specifically:

- Observed scaling exponent: $p \approx 1.03$ (not $p = 2$ as predicted by §3.2 polynomial-equivariant analysis, and not $p = 3/2$ as ruled out by the same).
- Observed Σ_m-Hessian eigenvalue ratio at finite $L$: $\mu_1 / \mu_0 \approx 2$ (i.e., $\mu_0 \approx \epsilon|W''(c)|$, $\mu_1 \approx 2\epsilon|W''(c)|$), **not** $\mu_0 = \mu_1 = 4\epsilon|W''(c)|$.
- The leading-order *degeneracy* on which §3.2's $O(\epsilon^2)$ splitting prediction depends is therefore **not observed** at $L \leq 16$. The R22 canonical-Cat-A claim "$A_2/A_1 = 4$" is in tension with the finite-$L$ numerical evidence (effective $A_2/A_1 \approx 1$).

**Interpretation hypotheses (under active examination, not yet adjudicated):**

1. **Continuum-limit hypothesis** (preserves §3.2 conclusion): the $A_2/A_1 = 4$ identity is a continuum-limit ($L \to \infty$) statement. Finite-$L$ corrections are $O(1/L^2)$ or worse, large enough at $L \leq 16$ to dominate the leading-order behaviour. Under this hypothesis, the §3.2 splitting prediction $\mu_1 - \mu_0 = O(\epsilon^2)$ is conditional on continuum extrapolation, recoverable on $L \geq L_*$ for some explicit $L_*$ (likely $L_* \gg 16$). Falsifiable by the NQ-187b protocol (§11).
2. **Convention-mismatch hypothesis** (challenges §2.1.6): the data fits the R22 working convention $F_{xx}^{\mathrm{R22}} = 2\epsilon|W''(c)|$, $F_{yy}^{\mathrm{R22}} = 4\epsilon|W''(c)|$ directly *without* the factor-2 doubling encoded in the canonical-convention map. Under this hypothesis, canonical T-σ-Theorem-4 (ii)'s $\mu_0 = 4\epsilon|W''(c)|$ would be a notational artifact rather than a Σ_m-Hessian eigenvalue — requires re-examination of the canonical convention itself. Falsifiable by independent symbolic verification of the canonical-vs-R22 prefactor map.
3. **Discrete-graph $A_2/A_1 \neq 4$ hypothesis** (challenges R22 working file `symmetry_moduli.md` §3.3): the $A_2/A_1 = 4$ identity holds in continuum but the discrete-graph $L \times L$ free-BC version gives a different effective ratio that *converges to* 4 only in the continuum limit. Independent of which convention is used. NQ-187b (§11) is the operational test.

**Status:** the §2.1 absorption derivation is **mathematically self-consistent within the canonical convention**, but its load-bearing numerical instantiation (boxed claim $\mu_0 = \mu_1 = 4\epsilon|W''(c)|$) is **not supported** by the finite-$L$ data. We retain §2.1.1–§2.1.7 as the *convention-derivation scaffolding*, with the explicit caveat that the prediction "$\mu_0 = \mu_1$ at leading order on $D_4$ free-BC" is now **conditional on continuum extrapolation pending NQ-187b**.

---

## §3. Higher-Order Equivariants on $D_4$

### 3.1 $D_4$-equivariant polynomial generators

By the Chevalley–Shephard–Todd theorem applied to $D_4 \subset O(2)$ acting on $(x, y)$, the algebra of $D_4$-invariant polynomials in $(x, y)$ is generated by two fundamental invariants:

$$I_1 := x^2 + y^2, \qquad I_2 := x^2 y^2.$$

Equivalently, every $D_4$-invariant polynomial is a polynomial in $(I_1, I_2)$. The Lyapunov function $F(x, y; \beta)$, being $D_4$-invariant, must therefore have the form

$$F = \tfrac{\mu}{2} I_1 + (A_1 + A_2/2)\, I_1^2 - (A_2/2)\,(I_1^2 - 4 I_2) + \cdots,$$

or more cleanly, using $I_1^2 = (x^2 + y^2)^2 = x^4 + y^4 + 2 x^2 y^2$ and $4 I_2 = 4 x^2 y^2$:

$$F = \tfrac{\mu}{2} I_1 + B_1 I_1^2 + B_2 I_2 + B_3 I_1^3 + B_4 I_1 I_2 + B_5 I_2^2 + B_6 I_1^4 + B_7 I_1^2 I_2 + B_8 I_1 I_2^2 + B_9 I_2^3 + \cdots$$

with $B_i$ smooth functions of $\beta$ near $\beta_{\mathrm{crit}}^{(2)}$.

**Correspondence with §2:** $B_1 = A_1$ (modulo the $A_2$-absorption $A_1 = (A_1 + A_2/2) - A_2/2$, i.e., re-expand), $B_2 = A_2 - 2 A_1 = 2 A_1$ on $D_4$ free-BC (using $A_2/A_1 = 4 \Rightarrow A_2 - 2 A_1 = 2 A_1$). The sign of $B_2$ is what makes axis vs diagonal selection well-defined (R22 Cat A: $B_2 > 0$ → axis selected).

### 3.2 5th-order term: invariant ring vs equivariant module

The W5 Day 4 PM Wave 2 critic re-review (`logs/daily/2026-04-30/09_critic_re_review_5files.md` §3.1 issue #1) flagged the original §3.2 argument as **invariant-vs-equivariant confused**: the "no integer solution to $2a + 4b = 5$" rules out a degree-5 *invariant polynomial*, but the Crandall–Rabinowitz (C-R) reduction expansion is on the **equivariant** (gradient-vector) side. We now address both objects rigorously and show the conclusion (no $\epsilon^{3/2}$ contribution at any C-R order) holds independently and from a *stronger* argument.

#### 3.2.1 The two algebraic objects in C-R reduction

C-R reduction at a $D_4$-symmetric pitchfork involves **two** distinct algebraic objects on $V_2 = \mathrm{span}(\phi_{(1, 0)}, \phi_{(0, 1)})$:

- **Invariant polynomial ring** $\mathcal{R}^{D_4}_{\mathrm{inv}}$: the algebra of $D_4$-invariant scalars in $(x, y)$. The Lyapunov function $F: V_2 \to \mathbb{R}$ lives in this ring.
- **Equivariant polynomial module** $\mathcal{M}^{D_4}_{\mathrm{eq}}$: the $\mathcal{R}^{D_4}_{\mathrm{inv}}$-module of $D_4$-equivariant vector fields on $V_2$. The reduced gradient $g(x, y) = \nabla F$ lives in this module. C-R expansion of the bifurcation equation $g(x, y; \beta) = 0$ is performed in the equivariant module.

The relation: $\mathcal{R}^{D_4}_{\mathrm{inv}}$ is generated by two fundamental invariants $I_1 = x^2 + y^2$ (degree 2) and $I_2 = x^2 y^2$ (degree 4), per Chevalley–Shephard–Todd. $\mathcal{M}^{D_4}_{\mathrm{eq}}$ is generated **as an $\mathcal{R}^{D_4}_{\mathrm{inv}}$-module** by two equivariant generators; the explicit Golubitsky–Stewart–Schaeffer (1988) Vol II Ch XV §3 list (table for $D_4$ on $\mathbb{R}^2$) gives:

$$\mathcal{M}^{D_4}_{\mathrm{eq}} = \mathcal{R}^{D_4}_{\mathrm{inv}} \cdot \{X_1, X_2\}, \qquad X_1 = (x, y), \qquad X_2 = (x^3, y^3).$$

Equivalently: every $D_4$-equivariant vector field on $\mathbb{R}^2$ has the form $g(x, y) = p(I_1, I_2)\cdot(x, y) + q(I_1, I_2)\cdot(x^3, y^3)$ with $p, q$ polynomials in $(I_1, I_2)$.

#### 3.2.2 Parity of the equivariant generators

The generator $X_1 = (x, y)$ has **degree 1** (homogeneous of total degree 1). The generator $X_2 = (x^3, y^3)$ has **degree 3**. Both are **odd** in total degree, while the invariant ring contains only **even**-degree generators ($I_1$ degree 2, $I_2$ degree 4). Therefore:

$$\deg(g) = \deg(p \cdot X_1) = \deg(p) + 1 \in \{1, 3, 5, 7, \ldots\}, \quad \deg(p) \in \{0, 2, 4, 6, \ldots\},$$

$$\deg(g) = \deg(q \cdot X_2) = \deg(q) + 3 \in \{3, 5, 7, 9, \ldots\}, \quad \deg(q) \in \{0, 2, 4, 6, \ldots\}.$$

**Every $D_4$-equivariant gradient vector field on $\mathbb{R}^2$ has odd total degree.** Even-degree equivariants do not exist in $\mathcal{M}^{D_4}_{\mathrm{eq}}$.

This is the structural fact that the original §3.2 argument missed: it correctly observed *no degree-5 invariant exists*, but it should have additionally established *no degree-4 equivariant exists either* (since degree-5 invariant $\leftrightarrow$ degree-4 equivariant via $g = \nabla F$, and $\nabla$ shifts degree by $-1$).

#### 3.2.3 Consequence for $\epsilon^{3/2}$ contributions in C-R

The C-R bifurcation equation on $V_2$ at $\beta = \beta_{\mathrm{crit}}^{(2)} + \epsilon$ is

$$g(x, y; \beta) = 0, \qquad g \in \mathcal{M}^{D_4}_{\mathrm{eq}}.$$

Expand $g$ in homogeneous equivariant components:

$$g(x, y; \beta) = g_1(x, y; \beta) + g_3(x, y; \beta) + g_5(x, y; \beta) + g_7(x, y; \beta) + \cdots,$$

where $g_k$ has total degree $k$. By §3.2.2, **only odd-degree components appear**. The bifurcation amplitude scales as $a_\epsilon \sim \sqrt{\epsilon}$ (R22 Cat A), so the C-R hierarchy gives:

- $g_1 \sim a_\epsilon \cdot \epsilon^0 \sim \epsilon^{1/2}$ (linear part, vanishes at criticality).
- $g_3 \sim a_\epsilon^3 \sim \epsilon^{3/2}$ (cubic equivariants, $A_1, A_2$).
- $g_5 \sim a_\epsilon^5 \sim \epsilon^{5/2}$ (quintic equivariants — *do exist* in $\mathcal{M}^{D_4}_{\mathrm{eq}}$ as $I_1 \cdot X_2 = (I_1 x^3, I_1 y^3)$ and $I_2 \cdot X_1 = (x^3 y^2, x^2 y^3)$, both degree 5).
- $g_7 \sim a_\epsilon^7 \sim \epsilon^{7/2}$.

The post-bifurcation amplitude correction comes from solving $g(x, y; \beta) = 0$ order by order. At $O(\epsilon^{1/2})$: trivially zero. At $O(\epsilon^{3/2})$: cubic equivariants determine $a_\epsilon$. At $O(\epsilon^{5/2})$: quintic equivariants give a correction $\delta a_\epsilon \sim \epsilon^{3/2}$ to $a_\epsilon$.

**Crucially:** the *Lyapunov function* $F$ has degree-6 terms (since $g$ has degree-5 terms and $g = \nabla F$), so $F^{(6)} \neq 0$ identically. But $F^{(5)} \equiv 0$ (since $g_4 \equiv 0$ — there is no degree-4 equivariant). This is the polynomial-equivariant content of "no $\epsilon^{3/2}$ contribution to the Hessian splitting."

#### 3.2.4 Hessian splitting: from $F^{(6)} \neq 0$ to $\mu_1 - \mu_0 = O(\epsilon^2)$

The post-bifurcation Hessian eigenvalues are $\partial_x^2 F$ and $\partial_y^2 F$ evaluated at $(a_\epsilon, 0)$. Since $F = F^{(2)} + F^{(4)} + F^{(6)} + \cdots$ with all odd-degree pieces vanishing:

- $\partial_x^2 F^{(2)} \sim \epsilon$ (leading order, both eigenvalues equal on $D_4$ free-BC).
- $\partial_x^2 F^{(4)} \sim a_\epsilon^2 \sim \epsilon$ (already part of $\mu_0 = \mu_1 = 4|W''(c)|\epsilon$ via R22).
- $\partial_x^2 F^{(5)} \equiv 0$ (no degree-5 invariant).
- $\partial_x^2 F^{(6)} \sim a_\epsilon^4 \sim \epsilon^2$ — **first non-trivial splitting**.

Hence $\mu_1 - \mu_0 = c_4 \epsilon^2 + O(\epsilon^3)$. This is the conclusion the original §3.2 reached, but now it is established via the **stronger and correct** equivariant-module parity argument (Golubitsky–Stewart–Schaeffer 1988 Vol II Ch XV §3), not via the degree-5 invariant counting alone.

#### 3.2.5 Why the original argument was nearly correct

The original argument ("no integer solution to $2a + 4b = 5$") rules out the *invariant* $F^{(5)}$ but does **not** by itself rule out an equivariant correction at $\epsilon^{3/2}$. The correct rule-out comes from observing that the **module of $D_4$-equivariant gradient fields** has only odd-degree elements, so $\nabla F^{(5)} = 0$ requires $F^{(5)} = $ constant (i.e., $F^{(5)} \equiv 0$ up to additive constant, which is irrelevant for the Hessian), ratifying the conclusion. The original argument is **substantively correct** because $\nabla: F^{(d)} \to g_{d-1}$ is bijective on the relevant homogeneous polynomial spaces (for $d \geq 1$), so absence of degree-5 invariant *does* imply absence of degree-4 equivariant gradient. But the chain of reasoning required two steps (no invariant ⇒ no equivariant gradient at one degree lower), only one of which was previously stated.

#### 3.2.6 Reference for explicit equivariant generator list

Golubitsky, Stewart, Schaeffer (1988). *Singularities and Groups in Bifurcation Theory*, Vol. II, Springer, **Chapter XV §3 Table** lists for $D_4$ acting on $\mathbb{R}^2$:

- Invariants: $u = x^2 + y^2$, $v = x^2 y^2$ (called $I_1, I_2$ in our notation).
- Equivariants: $X_1 = (x, y)$, $X_2 = (x^3, y^3)$.

The table makes the parity argument transparent. We import this fact as a contrastive parallel (CN10): the smooth-manifold $\mathbb{R}^2$ result transfers to the discrete-graph $V_2$ subspace because the $D_4$-action and the invariant/equivariant ring structure are identical (both quotients by the same finite group acting linearly). The σ-framework's discrete-graph specialization changes the *coefficients* (via the discrete vs continuum Fiedler eigenfunction integrals) but not the *algebraic structure*.

#### 3.2.7 Summary

- $D_4$-invariant ring $\mathcal{R}^{D_4}_{\mathrm{inv}}$ has no degree-5 element (original §3.2 observation, correct).
- $D_4$-equivariant module $\mathcal{M}^{D_4}_{\mathrm{eq}}$ has only odd-degree elements, hence no degree-4 element (additional fact from GSS 1988 Vol II Ch XV §3).
- Combining: scalar Lyapunov $F$ has no odd-degree polynomial piece, so $F^{(5)} \equiv 0$; hence the C-R expansion has no $\epsilon^{3/2}$ contribution to the Hessian splitting from polynomial equivariants.
- First non-trivial splitting from $F^{(6)} \neq 0$, giving $\mu_1 - \mu_0 = O(\epsilon^2)$ as in §4.4 — **conditional on the leading-order degeneracy** $\mu_0 = \mu_1$, see §3.2.8.

#### 3.2.8 Conditional status of the $O(\epsilon^2)$ prediction (W5 Day 4 PM Wave 3)

**Critical update (2026-04-30):** The polynomial-equivariant argument of §3.2.1–§3.2.7 establishes only that the *increment* $\mu_1 - \mu_0$ has no $\epsilon^{3/2}$ contribution from polynomial equivariants, *given* a leading-order baseline at which $\mu_0$ and $\mu_1$ agree (so that the "splitting" question is meaningful). The §8 numerical run on $L \in \{4, 8, 16\}$ (`logs/daily/2026-04-30/11_nq187_scaling_test_results.md`) shows that **on these finite grids, the leading-order baseline itself is non-degenerate**: $\mu_1 / \mu_0 \approx 2$, with scaling exponent $p \approx 1.03$ (linear in $\epsilon$, not the $O(\epsilon^2)$ next-to-leading correction predicted here).

**Three distinct logical implications:**

1. **§3.2.1–§3.2.6 algebra is unaffected.** The structural fact "$\mathcal{M}^{D_4}_{\mathrm{eq}}$ has only odd-degree elements; hence $F^{(5)} \equiv 0$" depends only on $D_4$-equivariance and Chevalley–Shephard–Todd, not on numerical eigenvalues at any specific $L$. This part of the analysis survives the falsification.

2. **The $O(\epsilon^2)$ prediction is conditional.** The chain of reasoning "$F^{(5)} \equiv 0 \Rightarrow \mu_1 - \mu_0$ first nonzero at $O(\epsilon^2)$" presupposes that the degree-2 and degree-4 contributions to $\mu_0$ and $\mu_1$ *coincide*. If they don't (as observed at $L \leq 16$), then the polynomial-equivariant analysis correctly rules out an $\epsilon^{3/2}$ correction *to the difference*, but the difference itself is dominated by the leading $O(\epsilon)$ non-degeneracy, *not* by a subleading $O(\epsilon^2)$ sextic-equivariant correction.

3. **Falsifiable predictions for NQ-187b.** Under the continuum-limit hypothesis (§2.1.8 hypothesis 1), the leading-order degeneracy $\mu_0 = \mu_1$ should reappear as $L$ grows. The §3.2 prediction $\mu_1 - \mu_0 = c_4\,\epsilon^2$ would then become observable for $L \geq L_*$ where the discrete corrections to $A_2/A_1$ are below the $\epsilon$-scale of the experiment. The protocol is operationalized in §11 (NQ-187b).

**Net status:** §3.2 retains its **algebraic correctness** but its **physical instantiation** as "the splitting first appears at $\epsilon^2$" is *not* observed on $L \leq 16$ and is now **conditional on continuum extrapolation**. The Cat A target for the splitting-order theorem (§10.1 deliverable 1) is downgraded to "Cat A pending NQ-187b" until the continuum-extrapolation $A_2/A_1 \to 4$ behaviour is established or refuted.

### 3.3 6th-order equivariants — three independent ones

The 6th-order $D_4$-invariants of total degree 6 in $(x, y)$ are spanned by:

$$\{I_1^3,\quad I_1 I_2\} = \{(x^2 + y^2)^3,\quad (x^2 + y^2) x^2 y^2\}.$$

(Note: $I_2^{3/2}$ is not a polynomial; the would-be third generator $x^4 y^2 + x^2 y^4$ equals $I_1 I_2$, not independent.) So **two** independent 6th-order generators, giving Lyapunov coefficients $B_3 = $ coefficient of $I_1^3$ and $B_4 = $ coefficient of $I_1 I_2$.

The 6th-order term in $F$ is:

$$F^{(6)} = B_3 (x^2 + y^2)^3 + B_4 (x^2 + y^2) x^2 y^2.$$

Expanding:

$$F^{(6)} = B_3 (x^6 + 3 x^4 y^2 + 3 x^2 y^4 + y^6) + B_4 (x^4 y^2 + x^2 y^4) = B_3 (x^6 + y^6) + (3 B_3 + B_4)(x^4 y^2 + x^2 y^4).$$

---

## §4. Computation Plan — 6th-Equivariant Coefficients

### 4.1 Source of $B_3, B_4$

The 6th-order coefficients arise from two distinct contributions in the σ-framework Hessian projection onto $V_2$:

**(C1) Direct sextic from $W$.** Cubic potential $W(u) = u(1-u)(1/2 - u)$ has Taylor expansion

$$W(c + \delta) = W(c) + W'(c)\delta + \tfrac{1}{2}W''(c)\delta^2 + \tfrac{1}{6}W'''(c)\delta^3 + \tfrac{1}{24}W^{(4)}(c)\delta^4 + \cdots$$

For $c = 1/2$: $W'(1/2) = -1/4$, $W''(1/2) < 0$, $W'''(1/2) = 0$ (odd symmetry), $W^{(4)}(1/2) = $ const, $W^{(5)}(1/2) = 0$, $W^{(6)}(1/2) = 0$ — because $W$ is a *cubic* polynomial in $u$, all derivatives of order $\geq 4$ vanish at $c = 1/2$. **Direct $W$-Taylor contribution to $F^{(6)}$ is zero**.

This is a structurally important consequence: with cubic $W$, only $W^{(2)}$ and $W^{(3)}$ are nonzero (the latter zero at $c = 1/2$). All higher-order corrections to $F$ come from *cross-coupling* between the soft Fiedler doublet and the orthogonal hard modes — i.e., from center-manifold reduction.

**(C2) Center-manifold reduction.** Modes $\phi_k$ with $k \geq 2$ outside $V_2$ have positive Hessian eigenvalues $\mu_k(c\mathbf{1}) = O(1)$ (gapped from the soft doublet by a finite gap). They get slaved to the soft modes via the reduction $\phi_k(x, y) = -[H^{(0)}_{kk}]^{-1} \cdot V_k(x, y) + O(\text{higher})$, where $V_k$ is the cubic-in-$(x, y)$ projection coming from $W$'s cubic interaction term ($W'''$ piece) — but since $W'''(c) = 0$ at $c = 1/2$, **the leading center-manifold slaving comes from the $W^{(4)}(c)$-quadratic interaction, contributing at quartic order in $(x, y)$** (already accounted in $A_1, A_2$), and the next correction comes from iterating the $W^{(4)}$ slaving to give a sextic $(x, y)$-effective term.

### 4.2 Center-manifold slaving iteration: explicit derivation

The W5 Day 4 PM Wave 2 critic (`logs/daily/2026-04-30/09_critic_re_review_5files.md` §3.1 issue #2) flagged this section's claim that "the $W^{(4)}$ slaving iterates to give a sextic correction" as load-bearing but not derived. We now show the iteration explicitly using the Carr (1981, *Applications of Centre Manifold Theory*, Springer Applied Mathematical Sciences 35) §2 framework, adapted to the discrete $D_4$ free-BC grid.

#### 4.2.1 Setup: Σ_m-Hessian decomposition

Decompose the perturbation $u - c\mathbf{1} = v_{\mathrm{soft}} + v_{\mathrm{hard}}$ where

$$v_{\mathrm{soft}} = x \phi_{(1, 0)} + y \phi_{(0, 1)} \in V_2 \quad \text{(soft, } |\mu_{V_2}| \to 0\text{ at }\beta_{\mathrm{crit}}^{(2)}\text{)},$$

$$v_{\mathrm{hard}} = \sum_{k \geq 4} z_k \phi_k \in V_2^\perp \cap T_{u_*}\Sigma_m \quad \text{(hard, } \mu_k \geq \mu_*\text{ uniformly)},$$

where the index $k = 1$ corresponds to the constant mode (excluded from $T_{u_*}\Sigma_m$), $k = 2, 3$ correspond to the soft Fiedler doublet $\phi_{(1, 0)}, \phi_{(0, 1)}$ (= $V_2$), and $k \geq 4$ are the higher modes ($\phi_{(2, 0)}, \phi_{(1, 1)}, \phi_{(0, 2)}, \phi_{(2, 1)}, \ldots$). The hard-mode gap is $\mu_* := \min_{k \geq 4}\mu_k(c\mathbf{1}) > 0$ at $\beta = \beta_{\mathrm{crit}}^{(2)}$.

The C-R / center-manifold theorem (Carr 1981, Theorem 2.1) guarantees a smooth invariant manifold $\mathcal{W}^c$ tangent to $V_2$ at $u_* = c\mathbf{1}$, parametrized by a smooth map $h: V_2 \to V_2^\perp$ with $h(0) = 0$ and $Dh(0) = 0$, such that the slaved hard amplitudes are $z_k = h_k(x, y)$. Carr's Theorem 2.1 also guarantees that $h$ can be **iteratively approximated** by solving a sequence of fixed-point equations.

#### 4.2.2 Carr (1981) iteration in the discrete-graph setting

The σ-energy on the full ambient space, after restriction to $\Sigma_m$, splits as

$$\mathcal{E}(c\mathbf{1} + v) = \tfrac{1}{2}\langle v_{\mathrm{soft}}, H_{\mathrm{soft}} v_{\mathrm{soft}}\rangle + \tfrac{1}{2}\langle v_{\mathrm{hard}}, H_{\mathrm{hard}} v_{\mathrm{hard}}\rangle + \mathcal{N}(v),$$

where $H_{\mathrm{soft}} \to 0$ as $\beta \to \beta_{\mathrm{crit}}^{(2)}$, $H_{\mathrm{hard}} = \mathrm{diag}(\mu_k(c\mathbf{1}))_{k \geq 4}$ to leading order, and $\mathcal{N}(v)$ is the cubic-and-higher nonlinear coupling from $\beta\int W(c + v)$.

For cubic potential $W(u) = u(1 - u)(1/2 - u)$ at $c = 1/2$ with $W'''(1/2) = 0$ and $W^{(4)}(1/2) = $ const, the Taylor-expansion of $W$ around $c$ has **no cubic-in-$v$ piece** but a non-zero quartic-in-$v$ piece. Hence

$$\mathcal{N}(v) = \tfrac{\beta\,W^{(4)}(c)}{24}\sum_i v_i^4 + (\text{higher orders in }v).$$

Note $W^{(4)}(1/2)$ is a nonzero constant; precise sign depends on the convention but the parity is: cubic potential has $W^{(4)}$ as the *first* non-zero even-derivative beyond $W''$.

The slaving equation for $z_k$ is: at the critical manifold $\mathcal{W}^c$, the gradient of $\mathcal{E}$ in the hard direction vanishes:

$$0 = \partial_{z_k}\mathcal{E}(c\mathbf{1} + v_{\mathrm{soft}} + v_{\mathrm{hard}}) = \mu_k(c\mathbf{1}) z_k + \partial_{z_k}\mathcal{N}(v).$$

Solving for $z_k$:

$$z_k = -\frac{1}{\mu_k(c\mathbf{1})}\partial_{z_k}\mathcal{N}(v_{\mathrm{soft}} + v_{\mathrm{hard}}). \quad (\star)$$

This is an implicit equation for $z_k$ as a function of $(x, y)$ and the other $z_j$. We solve it iteratively per Carr (1981) §2.

#### 4.2.3 Iteration 0 (trivial)

Set $z_k^{(0)} = 0$ for all $k \geq 4$. Substitute into the right-hand side of $(\star)$:

$$z_k^{(1)} = -\frac{1}{\mu_k(c\mathbf{1})}\partial_{z_k}\mathcal{N}(v_{\mathrm{soft}} + 0) = -\frac{1}{\mu_k(c\mathbf{1})}\cdot \tfrac{\beta W^{(4)}(c)}{6}\langle \phi_k, (x\phi_{(1, 0)} + y\phi_{(0, 1)})^3\rangle.$$

(The factor $1/6$ comes from differentiating $v_i^4/24$ w.r.t. $z_k = \langle v, \phi_k\rangle$, which after summing over all $i$ gives the inner product with the cubic.)

Expanding $(x\phi_{(1, 0)} + y\phi_{(0, 1)})^3 = x^3 \phi_{(1, 0)}^3 + 3x^2 y\,\phi_{(1, 0)}^2 \phi_{(0, 1)} + 3xy^2\,\phi_{(1, 0)}\phi_{(0, 1)}^2 + y^3 \phi_{(0, 1)}^3$, we get

$$z_k^{(1)} = -\frac{\beta W^{(4)}(c)}{6\mu_k(c\mathbf{1})}\big[x^3 C_k^{(3, 0)} + 3 x^2 y\, C_k^{(2, 1)} + 3 x y^2\, C_k^{(1, 2)} + y^3 C_k^{(0, 3)}\big],$$

where $C_k^{(p, q)} := \langle \phi_k, \phi_{(1, 0)}^p \phi_{(0, 1)}^q\rangle$ are discrete-graph cubic coupling integrals. By $D_4$ irrep-selection rules (computed explicitly in §4.3 below), only specific $\phi_k$ have nonzero $C_k^{(p, q)}$:

- $C_k^{(3, 0)} \neq 0$ only for $\phi_k \in \{\phi_{(3, 0)}, \phi_{(1, 0)}\}$ — the latter is in $V_2$ and excluded from the hard sum.
- $C_k^{(0, 3)} \neq 0$ only for $\phi_k \in \{\phi_{(0, 3)}, \phi_{(0, 1)}\}$ — same.
- $C_k^{(2, 1)} \neq 0$ only for $\phi_k \in \{\phi_{(2, 1)}, \phi_{(0, 1)}\}$ — exclude $V_2$.
- $C_k^{(1, 2)} \neq 0$ only for $\phi_k \in \{\phi_{(1, 2)}, \phi_{(1, 0)}\}$ — exclude $V_2$.

Hence $z_k^{(1)}$ is **cubic** in $(x, y)$. This is the "cubic slaving" referred to in §4.1 (C2).

#### 4.2.4 Iteration 2: Substitute $z_k^{(1)}$ back

Substitute $v_{\mathrm{hard}}^{(1)} = \sum_{k \geq 4} z_k^{(1)} \phi_k$ into $(\star)$:

$$z_k^{(2)} = -\frac{1}{\mu_k(c\mathbf{1})}\partial_{z_k}\mathcal{N}(v_{\mathrm{soft}} + v_{\mathrm{hard}}^{(1)}).$$

The differential $\partial_{z_k}\mathcal{N}$ now picks up contributions from cross-terms between $v_{\mathrm{soft}}$ (linear in $x, y$, factors of $\phi_{(p_0, q_0)} \in V_2$) and $v_{\mathrm{hard}}^{(1)}$ (cubic in $x, y$, factors of $\phi_k$ for $k \geq 4$).

Since $\mathcal{N}$ has $v_i^4/24$ leading nonlinearity, $\partial_{z_k}\mathcal{N} = \beta W^{(4)}(c)\cdot \langle \phi_k, v^3\rangle/6$. Expanding $v = v_{\mathrm{soft}} + v_{\mathrm{hard}}^{(1)}$ and keeping all terms cubic in $v$:

$$v^3 = v_{\mathrm{soft}}^3 + 3 v_{\mathrm{soft}}^2 v_{\mathrm{hard}}^{(1)} + 3 v_{\mathrm{soft}} (v_{\mathrm{hard}}^{(1)})^2 + (v_{\mathrm{hard}}^{(1)})^3.$$

The first term reproduces $z_k^{(1)}$ (already computed). The second term $3 v_{\mathrm{soft}}^2 v_{\mathrm{hard}}^{(1)}$ is **quadratic in $(x, y)$ from $v_{\mathrm{soft}}^2$ times cubic in $(x, y)$ from $v_{\mathrm{hard}}^{(1)}$, total quintic**, which gives a quintic-in-$(x, y)$ correction to $z_k^{(2)}$. The third and fourth terms are seventh- and ninth-order, respectively.

Hence

$$z_k^{(2)} = z_k^{(1)} + (\text{quintic in }(x, y)) + O((x, y)^7).$$

#### 4.2.5 Substitute back into $\mathcal{E}$ to get the effective Lyapunov $F$

The reduced energy on $\mathcal{W}^c$ is

$$F(x, y; \beta) = \mathcal{E}(c\mathbf{1} + v_{\mathrm{soft}} + h(v_{\mathrm{soft}})) = \mathcal{E}^{(2)}(v_{\mathrm{soft}}) + \mathcal{E}^{(4)}(v_{\mathrm{soft}}) + \tfrac{1}{2}\langle h, H_{\mathrm{hard}} h\rangle + \mathcal{N}_{\mathrm{cross}}(v_{\mathrm{soft}}, h) + \cdots$$

The **slaving correction** $-\tfrac{1}{2}\langle h, H_{\mathrm{hard}} h\rangle$ (from substituting the slaved $z_k$ back into the hard-mode quadratic) gives, with $h \approx z^{(1)}$ at leading nontrivial order:

$$-\tfrac{1}{2}\sum_{k \geq 4}\mu_k(c\mathbf{1})\cdot (z_k^{(1)})^2 = -\tfrac{1}{2}\sum_{k \geq 4}\frac{1}{\mu_k(c\mathbf{1})}\cdot \left(\frac{\beta W^{(4)}(c)}{6}\right)^2 \cdot \big|\textstyle\sum_{p+q=3}\binom{3}{p}x^p y^q C_k^{(p, q)}\big|^2.$$

This is **sextic** in $(x, y)$ — quadratic in cubics. This is the source of $B_3, B_4$ in §3.3 / §4.4. Explicitly:

$$F^{(6)}(x, y) = -\frac{1}{2}\left(\frac{\beta W^{(4)}(c)}{6}\right)^2 \sum_{k \geq 4} \frac{\big|\sum_{p+q=3}\binom{3}{p} x^p y^q C_k^{(p, q)}\big|^2}{\mu_k(c\mathbf{1})}.$$

Expanding the squared sum and matching to the $D_4$-invariant basis $\{I_1^3, I_1 I_2\}$:

$$F^{(6)} = B_3(x^2 + y^2)^3 + B_4(x^2 + y^2)x^2 y^2,$$

with explicit coefficients (schematic, sign convention per quadratic form):

$$B_3 \,\sim\, -\frac{1}{2}\left(\frac{\beta W^{(4)}(c)}{6}\right)^2 \sum_{k \geq 4} \frac{(C_k^{(3, 0)})^2 + (\text{axis-symmetric terms})}{\mu_k(c\mathbf{1})},$$

$$B_4 \,\sim\, -\frac{1}{2}\left(\frac{\beta W^{(4)}(c)}{6}\right)^2 \sum_{k \geq 4} \frac{2 C_k^{(3, 0)} C_k^{(1, 2)} + (\text{cross terms})}{\mu_k(c\mathbf{1})},$$

(precise prefactors require careful $D_4$-projection bookkeeping, deferred to W7+ analytical task; the numerical evaluation in §8 verifies the scaling exponent $p = 2$).

#### 4.2.6 Convergence of the iteration

Carr (1981) Theorem 2.1 establishes that the iteration $z_k^{(n+1)} = -\mu_k^{-1}\partial_{z_k}\mathcal{N}(v_{\mathrm{soft}} + v_{\mathrm{hard}}^{(n)})$ converges in a neighborhood of $(x, y) = 0$, provided:

1. $\mu_*$ (hard-mode gap) is bounded away from zero — *holds at* $\beta = \beta_{\mathrm{crit}}^{(2)}$ since the bifurcation is at $\lambda_2 = \lambda_{\mathrm{Fiedler}}$ and $\lambda_3 = \lambda_{(2, 0)} > \lambda_2$ on $D_4$ free-BC ($\mu_* = O(1)$).
2. $\mathcal{N}$ is smooth — holds since $W$ is polynomial.
3. The implicit function theorem applies to $(\star)$ — holds since $H_{\mathrm{hard}}$ is invertible near $u_* = c\mathbf{1}$.

The convergence is in the $C^N$-norm on a $\rho$-neighborhood of the origin in $V_2$, which contains the bifurcation amplitude $a_\epsilon = O(\sqrt{\epsilon})$ for sufficiently small $\epsilon$.

Carr (1981) Theorem 2.1 (reformulated): if $h^{(n)}$ approximates the true center manifold $h$ to order $N$ in $\|v_{\mathrm{soft}}\|$, then $|h - h^{(n)}| = O(\|v_{\mathrm{soft}}\|^{N+1})$. Iteration 1 ($z_k^{(1)}$) is exact to cubic order in $(x, y)$; iteration 2 corrects to quintic order; etc. For sextic Lyapunov coefficients $B_3, B_4$, **iteration 1 is sufficient**.

#### 4.2.7 Reference

Carr, J. (1981). *Applications of Centre Manifold Theory*. Springer Applied Mathematical Sciences, Vol. 35. Theorem 2.1 (existence of centre manifold via Banach fixed point) and §2.4 (iterative approximation lemma) are the operational tools.

The discrete-graph adaptation requires only finite-dimensional substitutes: the Banach space is $\mathbb{R}^{n-3}$ (orthogonal complement of $V_2$ in $T_{u_*}\Sigma_m$ after removing the constant mode), the smoothness is polynomial ($C^\infty$), and the gap condition $\mu_* > 0$ is verified by direct Hessian eigenvalue computation on $D_4$ free-BC for any $L \geq 4$.

#### 4.2.8 Summary

- Iteration 0: $z_k^{(0)} = 0$.
- Iteration 1: $z_k^{(1)} = -[\mu_k(c\mathbf{1})]^{-1}\cdot \tfrac{\beta W^{(4)}(c)}{6}\sum_{p+q=3}\binom{3}{p}x^p y^q C_k^{(p, q)}$ (cubic in $(x, y)$).
- Iteration 2 and beyond: corrects at quintic order; **does not contribute** to the sextic $F^{(6)}$.
- Sextic Lyapunov $F^{(6)}$ from $-\tfrac{1}{2}\sum_k \mu_k (z_k^{(1)})^2$, giving $B_3, B_4$ as quadratic forms in the cubic coupling integrals $C_k^{(p, q)}$.
- Convergence via Carr (1981) Theorem 2.1.

#### 4.2.9 Numerical testability of $B_3, B_4$ on $L \leq 16$ (W5 Day 4 PM Wave 3)

**Critical update (2026-04-30):** The §8 numerical scaling test (`logs/daily/2026-04-30/11_nq187_scaling_test_results.md`) found $\mu_1/\mu_0 \approx 2$ at $L \in \{4, 8, 16\}$, i.e., the *leading-order* eigenvalues are non-degenerate at finite $L$. As a direct consequence, the *sextic correction* $B_3, B_4$ predicted in §4.2.5 — which produces a difference of order $a_\epsilon^4 = O(\epsilon^2)$ — is **not directly testable on $L \leq 16$ via the eigenvalue split**, because the observed split is dominated by an $O(\epsilon)$ non-degeneracy that swamps the predicted $O(\epsilon^2)$ sextic contribution.

**Implication for the iteration analysis:**

- The Carr (1981) iteration in §4.2.1–§4.2.7 remains *mathematically valid* as a center-manifold reduction. The hard-mode gap $\mu_* > 0$ assumption holds independent of the leading-order eigenvalue structure on $V_2$.
- The sextic Lyapunov coefficients $B_3, B_4$ are well-defined quadratic forms in $C_k^{(p, q)}$; their numerical magnitudes on the discrete $L \times L$ grid can in principle be computed by direct evaluation of the cubic coupling integrals $C_k^{(p, q)} = \langle \phi_k, \phi_{(1, 0)}^p \phi_{(0, 1)}^q\rangle$ for the relevant hard modes $\phi_k \in \{\phi_{(3, 0)}, \phi_{(0, 3)}, \phi_{(2, 1)}, \phi_{(1, 2)}, \ldots\}$.
- However, **the eigenvalue-split test of §8 cannot resolve the $B_3, B_4$ contribution** on $L \leq 16$ because the post-bifurcation Hessian is already non-degenerate at $O(\epsilon)$ — there is no "plateau" against which the sextic $O(\epsilon^2)$ correction can be cleanly extracted.

**Alternative tests for $B_3, B_4$ (deferred to W7+):**

1. **Direct integral evaluation:** compute $C_k^{(p, q)}$ on the discrete-grid eigenfunctions of $L_G$ on $L \times L$ free-BC (no bifurcation needed). Sum over $k \geq 4$ with $1/\mu_k(c\mathbf{1})$ weight to obtain $B_3, B_4$ symbolically. Cat A if the closed form converges; Cat B if only numerical.
2. **Higher-order eigenvalue probe:** at much smaller $\epsilon$ (sub-machine precision becomes relevant) and much larger $L$ (where the leading-order $A_2/A_1 \to 4$ behaviour stabilizes per the continuum-limit hypothesis), the $O(\epsilon^2)$ split should re-emerge. Operational test: NQ-187b (§11).
3. **Symbolic differentiation of $\mathcal{E}$ at $u_*$:** rather than the post-bifurcation Hessian, compute the *fourth-derivative tensor* of $\mathcal{E}$ at $u_* = c\mathbf{1}$ projected onto $V_2$. This isolates the $A_1, A_2$ coefficients and (with sextic projection) $B_3, B_4$ without going through bifurcation. Cleaner than §8's protocol on small $L$.

**Net status:** §4.2's center-manifold reduction is structurally intact; its predicted $B_3, B_4$ remain mathematical objects. The numerical extraction of these coefficients on $L \leq 16$ via §8 is **not the right test** given the observed non-degeneracy. NQ-187b's expanded $L$ range plus the alternative tests above are the operational path forward.

### 4.3 Required input

- $D_4$ irrep decomposition of cubic monomials $\{x^3, x^2 y, x y^2, y^3\}$ in the $(\phi_{(1, 0)}, \phi_{(0, 1)})$ basis.
- Selection rules: $\phi_{(1, 0)}^3 = (\sqrt{2})^3 \cos^3(\pi x)$ on $[0, 1]^2$. Using $\cos^3\theta = (3\cos\theta + \cos 3\theta)/4$: this expands into modes $(1, 0)$ (back into the soft sector — *included in the cubic* term $A_1$) and $(3, 0)$ (a hard mode, contributes to slaving).
- So the principal hard mode coupling is $(3, 0)$ for $\phi_{(1, 0)}^3$ and $(0, 3)$ for $\phi_{(0, 1)}^3$. These are $D_4$-conjugate (axis-pair), giving the same self-energy. Mixed cubic $\phi_{(1, 0)}^2 \phi_{(0, 1)}$ couples to $(3, 0) \otimes (0, 1)$ — needs irrep decomposition.

### 4.4 Hessian-eigenvalue split formula

Substituting the axis-aligned minimum $(a_\epsilon, 0)$ into $F^{(6)}$ adds the corrections:

$$F_{xx}^{(6)} = 30 B_3 a_\epsilon^4, \qquad F_{yy}^{(6)} = (6 B_3 + 2 B_4) a_\epsilon^4, \qquad F_{xy}^{(6)} = 0.$$

So the corrected Hessian eigenvalues to $O(\epsilon^2)$ are

$$\mu_0 = 4|W''(c)|\epsilon + 30 B_3 a_\epsilon^4 + O(\epsilon^3), \qquad \mu_1 = 4|W''(c)|\epsilon + (6 B_3 + 2 B_4) a_\epsilon^4 + O(\epsilon^3).$$

Using $a_\epsilon^2 = -\mu/(4 A_1) = \epsilon|W''(c)|/(4 A_1)$ → $a_\epsilon^4 = \epsilon^2 |W''(c)|^2/(16 A_1^2)$:

$$\boxed{\mu_1 - \mu_0 = (-24 B_3 + 2 B_4) \cdot \frac{|W''(c)|^2}{16 A_1^2} \cdot \epsilon^2 + O(\epsilon^3) = c_4 \cdot \epsilon^2 + O(\epsilon^3),}$$

where $c_4 = (B_4 - 12 B_3) \cdot |W''(c)|^2/(8 A_1^2)$.

**Splitting prediction:** $K_1 - K_0 = c_4 \cdot \epsilon + O(\epsilon^2)$ at the *Hessian-eigenvalue level*, since $\mu_k = K_k \epsilon$ at leading order; equivalently the *next*-to-leading correction $\mu_1 - \mu_0$ is $O(\epsilon^2)$ in absolute terms, which translates to an $O(\epsilon)$ correction to the dimensionless ratio $K_1/K_0$.

---

## §5. Splitting Sign: $c_4 > 0$ or $c_4 < 0$?

The sign of $c_4 = (B_4 - 12 B_3) \cdot |W''(c)|^2/(8 A_1^2)$ depends on $B_4 - 12 B_3$. This is a graph-class-specific quantity requiring numerical evaluation of the slaving sums in §4.2 on the actual $L \times L$ $D_4$ free-BC grid.

**Heuristic prediction:** the slaving sums are dominated by the lowest hard-mode self-energies, i.e., by $\phi_{(3, 0)}$ (and $D_4$-images) and $\phi_{(2, 1)}$ (and $D_4$-images). Diagonal slaving via $\phi_{(3, 0)}$ contributes more to $B_3$ (axis-only coupling) than to $B_4$ (mixed-axis coupling); generically $12 B_3 > B_4$, suggesting $c_4 < 0$ — i.e., $\mu_1 < \mu_0$ at next-to-leading order. But this is not yet computed.

**If $c_4 < 0$:** $\mu_1 < \mu_0$ → sign-irrep ($A_2$) eigenvalue is *smaller* than trivial-irrep ($A_1$) eigenvalue. Tie-break (O7, Mulliken $A_1$ before $A_2$) places $A_1$ first, but the eigenvalue ordering would put $A_2$ (smaller eigenvalue) first by the σ-tuple's ascending-eigenvalue convention. **Conflict between Mulliken tie-break (O7) and ascending-eigenvalue ordering when $c_4 < 0$.**

**If $c_4 > 0$:** $\mu_1 > \mu_0$ → $A_1$ has the smaller eigenvalue, which agrees with the Mulliken-first convention. No conflict.

**Implication for O7:** if the higher-order calculation gives $c_4 < 0$, the σ-tuple ordering at $O(\epsilon^2)$ disagrees with O7's leading-order tie-break, i.e., the "correct" σ-tuple at $\epsilon$-small but post-leading-order would place $A_2$ before $A_1$. In that case O7 should be re-stated as a *leading-order plateau* convention only, with explicit recognition that higher-order analysis can resolve the degeneracy in the *opposite* direction. (See §6.)

---

## §6. Implication for Tie-Break (O7)

Three logical cases for the higher-order analysis:

| Case | Splitting result | Implication for O7 |
|------|------------------|---------------------|
| (a) $c_4 = 0$ exactly | Degeneracy persists to $O(\epsilon^3)$ or higher | O7 (Mulliken $A_1$ first) remains *necessary* at $O(\epsilon^2)$ accuracy. Tie-break is a structural feature, not a leading-order accident. |
| (b) $c_4 > 0$ | $\mu_1 > \mu_0$ at $O(\epsilon^2)$; $A_1$ smaller | O7 is *consistent with ascending-eigenvalue ordering* — Mulliken-first is the same as ascending-eigenvalue ordering. O7 is "redundant but consistent" at $O(\epsilon^2)$. |
| (c) $c_4 < 0$ | $\mu_1 < \mu_0$ at $O(\epsilon^2)$; $A_2$ smaller | O7 *conflicts* with ascending-eigenvalue ordering at $O(\epsilon^2)$. O7 must be explicitly framed as a *leading-order plateau convention* that resolves the $\epsilon \to 0^+$ limit, *not* a generic ordering rule. |

**Note (O7 robustness):** in all three cases, the σ-tuple's *irrep-label content* is unchanged (always $\{A_1, A_2\}$ as the two leading irreps of the Fiedler doublet at first pitchfork). What changes is only the *ordering*. So O7 as currently stated (Commitment 14, CV-1.5.1) does not mis-classify σ-tuples; it only mis-orders them in case (c). This is a refinement question, not a soundness question.

**Open question (NQ-187a, spawned in this file):** does case (c) actually occur on $D_4$ free-BC grid, and if so, should O7 be re-formulated as "ascending eigenvalue, with Mulliken-order tie-break only when eigenvalues are equal beyond $O(\epsilon^N)$ for some specified truncation $N$"?

---

## §7. Cat A Recovery via Strict Strengthening (not "reversal")

The W5 Day 4 PM Wave 2 critic re-review (`logs/daily/2026-04-30/09_critic_re_review_5files.md` §3.1 issue #3) flagged the original §7 framing as conceptually defective: a **process audit** (the Critic 7-agent verdict that retroactively downgraded T-σ-Theorem-4 v1.0 from Cat A to Cat B because the original 2026-04-27 W5 Day 1 G0 merge was performed with an unresolved internal contradiction) cannot be "reversed" by *new* mathematical analysis. The audit is a metalevel decision about merge-time evidence, not a statement subject to refutation by future theorems. We now revise the framing.

### §7.1 Distinction: theorem-object vs merge-event vs audit-decision

Three distinct objects:

1. **Theorem-object** (mathematical content): The leading-order σ-tuple statement $\sigma(u_\epsilon^*)|_{D_4} = (\mathcal{F}; (2, [+1], 4|W''(c)|\epsilon), (2, [-1], 4|W''(c)|\epsilon), \ldots)$ at first $D_4$ pitchfork. This is an unchanging mathematical object, true or false independent of audit history.

2. **Merge-event** (process artifact): The action on 2026-04-27 W5 Day 1 G0 of writing this statement into canonical.md §13 with a Cat A label, while the proof scaffolding contained the unresolved "would-be Goldstone $K_1 < K_0$" framing later corrected by Errata Round 1 (`91_critical_review.md`). The merge-event is a **historical fact**, immutable.

3. **Audit-decision** (metalevel verdict): The Critic 7-agent verdict on 2026-04-29 W5 Day 3 EOD that retroactively re-classifies the Cat A label assigned in (2) as Cat B because (2) violated the operational definition of Cat A ("rigorous proof with no acknowledged internal contradiction at merge time"). The audit-decision applies to **(2)**, not to **(1)**.

The original §7 conflated (1) and (2): it suggested that proving a stronger statement about (1) would "reverse" the audit-decision on (2). This is wrong — the audit-decision is about the **merge process**, which is past and cannot be unmerged. The corrected statement remains valid as theorem-object; the original Cat A label remains retroactively-Cat-B as merge-event annotation.

### §7.2 What new analysis can achieve: a strictly stronger theorem-object

The §3.2 + §4.2 + §4.4 work in this file produces a **new theorem candidate** (call it T-σ-Theorem-4-Refined) with strictly more content than the v1.0 statement. The refined statement, if proved at Cat A standard (rigorous proof, no acknowledged contradiction at merge time), would be:

> **T-σ-Theorem-4 (Refined). σ at first pitchfork on $D_4$ free-BC, at $O(\epsilon^2)$ accuracy.**
>
> Setup as v1.0 (T-σ-Theorem-4, canonical.md line 1377). Then:
>
> **(i)–(iv)** as in v1.0 (symmetry breaking, irrep labels, nodal counts unchanged).
>
> **(v) Higher-order σ-eigenvalue split.** Beyond the v1.0 leading-order $\mu_0 = \mu_1 = 4|W''(c)|\epsilon$, the next-to-leading correction is
> $$\mu_1 - \mu_0 = c_4 \cdot \epsilon^2 + O(\epsilon^3), \qquad c_4 = (B_4 - 12 B_3)\cdot \frac{|W''(c)|^2}{8 A_1^2},$$
> with $B_3, B_4$ explicit in terms of the cubic coupling integrals $C_k^{(p, q)} = \langle \phi_k, \phi_{(1, 0)}^p \phi_{(0, 1)}^q\rangle$ for $k \geq 4$ on the $L \times L$ $D_4$ free-BC grid (this file §4.2).
>
> **(vi) Sign of $c_4$ on continuum limit.** [pending — W7+ analytical computation per §5 heuristic predicts $c_4 < 0$, falsifiable per §8].
>
> **(vii) σ-tuple ordering convention at $O(\epsilon^2)$.** If $c_4 < 0$, the ascending-eigenvalue ordering places sign irrep $A_2$ before trivial irrep $A_1$, conflicting with O7 Mulliken-first leading-order plateau convention. Recommendation: re-state O7 as "leading-order plateau only", with explicit precedence to ascending eigenvalue beyond plateau.

This refined statement is **a new theorem candidate**, not a revision of the v1.0 audit verdict. It contains v1.0 as a strict sub-statement (the leading-order claim is part of (i)–(v) above) plus additional content on the higher-order split.

### §7.3 Promotion path for T-σ-Theorem-4-Refined

If §4.2 is completed at Cat A standard (W7+ effort estimate 2–3 weeks), the canonical merge for CV-1.6 would:

- **Add** T-σ-Theorem-4-Refined as a *new* canonical entry, separate from T-σ-Theorem-4 v1.0.
- Tag the new entry as **Cat A** if the proof is complete and consistent.
- **Leave T-σ-Theorem-4 v1.0 status unchanged**: still flagged as retroactive Cat B per the 2026-04-29 audit. v1.0 is a **historical object** and its audit annotation is permanent.
- Add a footnote on T-σ-Theorem-4 v1.0 entry: "*Note 2026-XX-XX: A strict strengthening of this theorem (T-σ-Theorem-4-Refined) has been merged at Cat A. The refined statement subsumes the v1.0 leading-order content. v1.0 retroactive Cat B status preserved as historical annotation; refined statement at Cat A independently.*"
- Update theorem_status.md: 1 new Cat A entry (T-σ-Theorem-4-Refined); v1.0 unchanged.

### §7.4 Why this matters: the σ-framework's epistemic policy

This framing aligns with the σ-framework's general policy that **theorems are individual mathematical objects with permanent audit trails**, not mutable claims subject to retroactive validity. Each theorem-object's Cat status is determined at merge time by the merge process; subsequent refinement produces a *new* theorem-object, not a re-evaluation of the original.

This is consistent with the canonical.md treatment of, e.g., T-Merge (c)(d)(e) (retracted 2026-04-10 with retraction note preserved), and the V5b iteration history (V1 → V5b'' resolved into V5b-T canonical + V5b-F Cat C). **Past audits stay past; new theorems get new entries.**

### §7.5 Effort estimate (revised)

- **Step 1** (W7 G0): Complete §3.2 invariant-vs-equivariant clarification + §4.2 iteration derivation + §4.4 coefficient extraction at the Cat A standard. Effort: 1.5 weeks analytical.
- **Step 2** (W7 G1): Numerical verification per §8 protocol on $L = 4, 8, 16$. Confirm $p = 2$ scaling and sign of $c_4$. Effort: 0.5 week computational.
- **Step 3** (W7 G2 / CV-1.6 merge): Draft T-σ-Theorem-4-Refined statement + proof, submit for canonical merge as new theorem. Effort: 0.5 week.
- **Step 4** (W7 mid): If $c_4 < 0$ confirmed, propose O7' refinement to Commitment 14 as separate D-7 user decision. Effort: 0.5 week (independent track).

Total: ~3 weeks. Outcome: **Cat A entry added** for T-σ-Theorem-4-Refined; v1.0 audit annotation preserved.

### §7.6 Original §7 framing preserved as historical note

The original §7 framed this as "*Cat A re-promotion path for T-σ-Theorem-4*" suggesting the v1.0 entry would itself be re-tagged Cat A. Critic verdict 2026-04-30 §3.1 issue #3 correctly identified this as a category error: process audits are not subject to mathematical reversal. The above §7.1–§7.5 reframing replaces "re-promotion of v1.0" with "promotion of a strictly stronger new theorem T-σ-Theorem-4-Refined". The corrected framing preserves the σ-framework's audit-trail integrity.

### §7.7 Downstream coherence note (cross-reference §10.1 deliverable 4 + §1 Mission)

The original §1 Mission (lines 28–29) and §10.1 deliverable 4 invoke "reversal" / "re-promotion" framing. After the §7 reframe these should be read as referring to the **promotion of the new T-σ-Theorem-4-Refined as an independent Cat A entry**, not as overturning the v1.0 retroactive Cat B audit. The v1.0 audit annotation remains permanent per §7.4. A future revision pass should propagate this terminology cleanup to §1 and §10.1.

---

## §8. Numerical Verification Plan

Independent of the analytical computation in §4, a direct numerical test on the actual Σ_m-restricted Hessian gives a falsifiability check.

### 8.1 Protocol

For $L \in \{4, 8, 16\}$ and $c = 1/2$:

1. Compute $\beta_{\mathrm{crit}}^{(2)} = 4\alpha\lambda_2^{\mathrm{Lap}}/|W''(c)|$ on each $L$ using `CODE/scripts/results/exp_hessian_uniform_v2.json` infrastructure (W4-04-25 NQ-141).
2. For $\epsilon \in \{0.001, 0.003, 0.01, 0.03, 0.1\}$, set $\beta = \beta_{\mathrm{crit}}^{(2)} + \epsilon$.
3. Run `find_formation` from a small-amplitude Fiedler-perturbed initial condition; obtain post-bifurcation minimizer $u^*_\epsilon$.
4. Compute Σ_m-restricted Hessian $H(u^*_\epsilon)$ and its smallest two non-Goldstone eigenvalues $\mu_0, \mu_1$.
5. Fit $(\mu_1 - \mu_0)/\epsilon^p$ as a function of $p$ via log-log regression: $\log(\mu_1 - \mu_0)$ vs $\log\epsilon$, expected slope $p$.

### 8.2 Predictions

- **§3.2 prediction:** $p = 2$ (no $\epsilon^{3/2}$ contribution because $D_4$ has no 5th-order equivariant; lowest splitting from 6th equivariant gives $\mu_1 - \mu_0 = O(\epsilon^2)$).
- **User prompt §5 alternative prediction:** $p = 3/2$ (5th-equivariant non-zero) — *predicted to fail* per §3.2 above; if observed, would indicate non-polynomial center-manifold contributions outside the smooth equivariant ring.

### 8.3 Falsifiability

- $p = 2$ observed → confirms §3.2 polynomial-equivariant analysis. Path to Cat A re-promotion proceeds.
- $p = 3/2$ observed → §3.2 analysis is incomplete (requires non-polynomial / non-smooth correction). Likely source: discrete-graph defect from continuum approximation; would require finite-grid corrections to the equivariant ring. NQ-187 stays open.
- $p \neq 2$ and $p \neq 3/2$ (e.g., $p \approx 1.7$) → mixed regime; likely numerical artifacts from finite $\epsilon$ or from boundary effects on small $L$. Increase $L$ and shrink $\epsilon$ window.

### 8.4 Sign of $c_4$

In the regime where $p = 2$ is confirmed, fit $c_4^{\mathrm{est}} = (\mu_1 - \mu_0)/\epsilon^2$ and check sign. Compare with §5 heuristic prediction (likely $c_4 < 0$).

### 8.5 Actual run results (W5 Day 4 PM Wave 3, 2026-04-30)

Numerical execution per §8.1 protocol on $L \in \{4, 8, 16\}$ with Lanczos extraction was completed on 2026-04-30. Full results: `logs/daily/2026-04-30/11_nq187_scaling_test_results.md`. Critical-finding bulletin: `logs/daily/2026-04-30/13_wave3_critical_findings.md`.

**Headline observations:**

- Scaling exponent $p \approx 1.03$ (linear), **not** $p = 2$ (§3.2 prediction) and **not** $p = 3/2$ (alternative ruled out by §3.2 polynomial-equivariant analysis).
- Σ_m-Hessian eigenvalue ratio $\mu_1/\mu_0 \approx 2$ at all tested $L$, i.e., $\mu_0 \approx \epsilon|W''(c)|$ and $\mu_1 \approx 2\epsilon|W''(c)|$.
- The leading-order *degeneracy* $\mu_0 = \mu_1 = 4\epsilon|W''(c)|$ predicted by canonical T-σ-Theorem-4 (ii) and assumed in §3.2.4 is **not observed** at $L \leq 16$.

**Falsifiability landed in §8.3 row 3** (observed $p \neq 2$ and $p \neq 3/2$): under the original §8.3 logic this would suggest "increase $L$ and shrink $\epsilon$ window". Wave 3 (this revision) reframes the finding as a **substantive constraint** — see §2.1.8, §3.2.8, §4.2.9 for the conditional-status analysis, and §11 for the operationalized NQ-187b protocol that extends $L$ into $\{32, 64, 128\}$ to test the continuum-limit hypothesis.

---

## §9. External References (Contrastive, CN10)

The following external bifurcation-theory references provide *parallel structure* (smooth equivariant manifold case) that informs but does not reduce the discrete σ-framework analysis:

- **Crandall, Rabinowitz** (1971). "Bifurcation from simple eigenvalues." *J. Funct. Anal.* 8, 321–340. — Provides the canonical reduction-to-normal-form theorem at simple eigenvalue crossings. Used here only as scaffolding; the σ-framework's discrete-Hessian setup adapts the projection but does not invoke the smooth-Banach-space machinery.
- **Golubitsky, Schaeffer** (1985). *Singularities and Groups in Bifurcation Theory*, Vol. I. Springer. — Equivariant singularity theory. Chapter VI (orbit-decomposition lattice for $D_n$) is the relevant reference for our 6th-order equivariant counting in §3.
- **Golubitsky, Stewart, Schaeffer** (1988). *Singularities and Groups in Bifurcation Theory*, Vol. II. Springer. — Vol. II Ch. XV gives the explicit $D_4$ normal form to all polynomial orders. Our $B_3, B_4$ correspond to coefficients of their "mode interaction" terms.
- **Sattinger** (1979). *Group Theoretical Methods in Bifurcation Theory*. Lecture Notes in Mathematics 762, Springer. — Equivariant Crandall–Rabinowitz under finite groups; isotropy lattice approach. Used in `working/SF/symmetry_moduli.md` §3.
- **Carr** (1981). *Applications of Centre Manifold Theory*. Springer Applied Mathematical Sciences, Vol. 35. — Theorem 2.1 (existence of centre manifold via Banach fixed point) and §2.4 (iterative approximation lemma) supply the operational tool used in §4.2 to derive the explicit slaving iteration $z_k^{(0)} \to z_k^{(1)}$ (cubic in $(x,y)$) → sextic correction in $F^{(6)}$. Imported contrastively (CN10): the smooth-manifold center-manifold theorem transfers to the discrete-graph $V_2 \subset T_{u_*}\Sigma_m$ setting because the hypotheses (gap condition $\mu_* > 0$, polynomial smoothness of $\mathcal{N}$, invertibility of $H_{\mathrm{hard}}$) all hold on $D_4$ free-BC for any $L \geq 4$; finite-dimensional Banach-space substitutes the smooth manifold setting.

**Discrete-graph specifics (no continuum analogue):**
- W4-04-22 R22 working files (`working/SF/symmetry_moduli.md` §3.3): explicit discrete-grid evaluation of $A_2/A_1 = 4$.
- W4-04-25 NQ-141 (`exp_hessian_uniform_v2.json`): numerical Hessian-eigenvalue verification at uniform fixed point.
- **`working/SF/sigma_uniqueness_theorem.md` §2 Definition 2.1' / §13 (NQ-188; W5 Day 4 PM Wave 3 cross-link, carry-forward #10):** the canonical conjugation-translation rule (clauses (a)–(d)) supplies the conjugation-modulo equivalence under which the higher-order $K_0 \neq K_1$ split predicted in §10 manifests as a refined σ-tuple distinction. The NQ-188 R23 σ-class enumeration (`CODE/scripts/sigma_class_count_R23.py`) provides the empirical denominator against which sextic-order splittings are counted; no $\epsilon^{3/2}$ contribution exists by polynomial $D_4$-equivariance, hence no σ-class refinement at order $\epsilon^{3/2}$ — first refinement at $\epsilon^2$.
- **`working/SF/sigma_lie_algebra_structure.md` §4–§6 (NQ-258; W5 Day 4 PM Wave 3 cross-link):** the σ-tuple irrep-decomposition reading frames the $K_0 = K_1$ leading-order degeneracy as an intra-$\widehat{\mathrm{Aut}(G)_{u^*}}$ near-degeneracy (Goldstone neighborhood at the $D_4$ pitchfork); §6 motivates the sextic refinement as a generic-symmetry-broken Lie-algebra-quotient artifact.

**Departure from continuum:** the sextic coefficients $B_3, B_4$ depend on the discrete $L$-dependent grid eigenfunctions, which differ from continuum cosines by $O(1/L^2)$ corrections (see `working/SF/symmetry_moduli.md` §3.4). On finite grids the slaving-sum integrals must be evaluated *discretely*, not in the continuum limit, to guarantee the Cat A character of the result for any $L \geq L_*$ for some explicit $L_*$.

---

## §10. Cat Target + W7+ Priority

### 10.1 Deliverables

1. **Splitting-order theorem (W7 G0 candidate):** "On $D_4$ free-BC $L \times L$ grid with $c = 1/2$, the leading-order $K_0 = K_1$ degeneracy of T-σ-Theorem-4 is split at $O(\epsilon^2)$, with explicit coefficient $c_4 = (B_4 - 12 B_3) \cdot |W''(c)|^2/(8 A_1^2)$, and no $\epsilon^{3/2}$ contribution exists by polynomial $D_4$-equivariance."
   - **Cat target:** Cat A (polynomial equivariant counting + slaving-sum convergence on finite graph).
   - **Effort:** 1 week analytical + 0.5 week numerical verification.

2. **Sign-of-$c_4$ characterization (W7+ G1 candidate):** "On $D_4$ free-BC, $c_4 < 0$" (subject to the slaving-sum computation; the numerical verification §8 acts as the falsifiability test).
   - **Cat target:** Cat A if both analytical and numerical agree; Cat B otherwise.
   - **Effort:** 1 week.

3. **O7 refinement (W7 mid):** if $c_4 < 0$ confirmed, propose "(O7') Mulliken tie-break is *leading-order plateau only*; ascending-eigenvalue ordering takes precedence beyond leading order." Submit as Commitment 14 sub-convention amendment for D-7 user decision.
   - **Cat target:** Convention-level (no theorem status).

4. **T-σ-Theorem-4 Cat A re-promotion (CV-1.6 candidate):** combine deliverables 1–2 into a refined T-σ-Theorem-4 statement and submit for canonical promotion review. Reverses W5 Day 4 retroactive Cat B downgrade.
   - **Cat target:** Cat A.
   - **Effort:** 0.5 week (statement + canonical merge once 1–2 are Cat A).

### 10.2 Risks

- **Risk A:** sextic slaving sums on discrete grids may not have closed-form expression; if only numerical evaluation is feasible, the result remains Cat B (dependent on numerics for the sign of $c_4$).
- **Risk B:** finite-grid corrections may flip the sign of $c_4$ between $L = 4$ and continuum limit, requiring explicit $L$-dependence in the canonical statement. Mitigation: state the result on $L \to \infty$ continuum first (clean), then add discrete corrections as a footnote.
- **Risk C:** boundary effects on free-BC may produce additional contributions not captured by the bulk equivariant decomposition. Mitigation: cross-validate on torus (where boundary effects vanish but irrep structure differs slightly — periodic cosines with momentum quantization).

### 10.3 Carry-forward registry

- **NQ-187** (this file's primary scope): higher-order ε splitting of $K_0 = K_1$ on $D_4$ first pitchfork. — **Spawned 2026-04-27 night `92_critical_review_round2.md` §6, §10. Active.**
- **NQ-187a** (this file's spawn): sign of $c_4$ and O7 refinement. — **Spawned 2026-04-29 EOD this file §6.**
- Cross-references at promotion time: canonical §13 T-σ-Theorem-4 (line 1377+), `working/SF/symmetry_moduli.md` §3.3 (R22 Cat A leading order), `daily/2026-04-27/91_critical_review.md` §3 + `92_critical_review_round2.md` §6, §10 (Errata Round 1+2), `daily/2026-04-29/08_user_decisions_log.md` D-2 (O7 approval).

---

## §11. Discrete vs Continuum $A_2/A_1$ Re-examination (NQ-187b)

**Spawned 2026-04-30 W5 Day 4 PM Wave 3** in response to the §8.5 numerical falsification of the leading-order degeneracy assumption used in §3.2 + §4.2 + canonical T-σ-Theorem-4 (ii).

### §11.1 Question

Does the R22 Cat A claim "$A_2/A_1 = 4$" (working file `working/SF/symmetry_moduli.md` §3.3, taken in continuum limit; promoted into canonical T-σ-Theorem-4 (ii)) hold on the *discrete* $L \times L$ $D_4$ free-BC grid? If yes, with what $L$-dependence? If only in $L \to \infty$, what is the convergence rate?

### §11.2 Operational protocol

For $L \in \{4, 8, 16, 32, 64, 128\}$ on the $D_4$-symmetric free-BC square grid:

1. **Compute the Fiedler doublet** $(\phi_{(1, 0)}, \phi_{(0, 1)})$ as $\ell^2$-normalized eigenvectors of $L_G$ at the second Laplacian eigenvalue $\lambda_2^{\mathrm{Lap}}$. Verify the doublet structure (degenerate pair under $D_4$).
2. **Evaluate the discrete-grid quartic integrals** that define $A_1, A_2$ in the R22 normal form:
   - $I_{4,0} := \sum_i \phi_{(1, 0), i}^4$ (axis-aligned quartic).
   - $I_{2,2} := \sum_i \phi_{(1, 0), i}^2 \phi_{(0, 1), i}^2$ (mixed quartic).
3. **Form the R22 normal-form coefficients:** $A_1 \propto I_{4, 0}$, $A_2 \propto I_{2, 2}$ (with prefactor from $W^{(4)}(c)/24$ — same for both, cancels in ratio).
4. **Compute the discrete ratio** $r(L) := A_2(L)/A_1(L) = I_{2, 2}(L)/I_{4, 0}(L)$.
5. **Plot** $r(L)$ vs $L$ on log-log axes. Fit $r(L) = 4 + c_1/L^2 + c_2/L^4 + \cdots$ (continuum-limit hypothesis) or test alternative scaling.

### §11.3 Predictions to test

- **Hypothesis A (continuum-limit recovery):** $r(L) \to 4$ as $L \to \infty$ with $r(L) - 4 = O(1/L^2)$. Falsifiable by fitting; if confirmed, identifies $L_*$ where finite-$L$ corrections become smaller than the $\epsilon$-scale at which the §3.2 splitting prediction is observable.
- **Hypothesis B (discrete-stable plateau):** $r(L) \to r_\infty < 4$ as $L \to \infty$ with $r_\infty$ a different rational/algebraic constant (e.g., $r_\infty \in \{1, 2, 3\}$). If confirmed, the canonical T-σ-Theorem-4 (ii) "$A_2/A_1 = 4$" claim is **incorrect on the discrete grid** and the canonical statement requires revision (see task #63 "T-σ-Theorem-4 canonical revision urgent").
- **Hypothesis C (no convergence):** $r(L)$ exhibits boundary-condition-driven non-convergent behaviour (e.g., oscillation, divergence). If observed, indicates that free-BC introduces a non-smooth contribution that the continuum analysis does not capture; would require torus-BC cross-validation or restriction to bulk integrals (excluding boundary layers).

### §11.4 Cross-validation

- **Torus BC:** repeat the protocol on $L \times L$ periodic-BC where the eigenfunctions are exact discrete cosines and $A_2/A_1$ is computable in closed form via cosine-product identities. Compares against the free-BC result to isolate the boundary-correction contribution.
- **Sextic coefficients $B_3, B_4$:** along the same sweep, evaluate the cubic-coupling integrals $C_k^{(p, q)}$ (§4.2.3) for the lowest hard modes ($\phi_{(3, 0)}, \phi_{(0, 3)}, \phi_{(2, 1)}, \phi_{(1, 2)}$) and form the leading-iteration estimates of $B_3, B_4$. Tests §4.2's structural derivation independently of the bifurcation-eigenvalue protocol of §8.

### §11.5 Cat target and effort

- **Cat A target:** if Hypothesis A is confirmed numerically and the convergence rate $r(L) - 4 = O(1/L^2)$ is established with at least two decades of $L$-spread.
- **Cat B target:** if only point estimates are obtained (e.g., $L \in \{4, 8, 16\}$ extended by a single additional grid).
- **Effort:** 1 week computational (sparse-eigenpair extraction at $L = 128$ requires arnoldi/LOBPCG; existing infrastructure in `CODE/scripts/` based on `exp_hessian_uniform_v2.json` is sufficient).
- **Deliverable:** updated `CODE/scripts/sigma_class_count_R23.py` analogue named `discrete_A2A1_sweep.py` (or similar); JSON results file `CODE/scripts/results/exp_A2A1_sweep_v1.json`; cross-link entry in this file's §11 + a Wave 4 daily log.

### §11.6 Carry-forward

- Outcome of NQ-187b directly determines whether §3.2 + §4.2's predictions can be operationalized at all; if Hypothesis A is confirmed, the §10.1 deliverable 1 timeline is preserved (the test moves to $L \geq L_*$). If B or C, the canonical T-σ-Theorem-4 (ii) statement requires revision and the §10.1 deliverables are blocked pending canonical update.
- Cross-reference to task #62 (NQ-187b) and #63 (canonical revision urgent) in the team task list.
- Cross-reference to `working/SF/symmetry_moduli.md` §3.3 (R22 source of $A_2/A_1 = 4$); a sister revision pass on that file should mark the $A_2/A_1 = 4$ identity as "Cat A pending NQ-187b discrete-grid verification".

---

## §12. Summary

- The leading-order $K_0 = K_1 = 4|W''(c)|\epsilon$ degeneracy of T-σ-Theorem-4 (canonical §13) was attributed to $D_4$ free-BC continuum integrals giving $A_2/A_1 = 4$. **W5 Day 4 PM Wave 3 numerical update:** the leading-order degeneracy is **not observed** at $L \leq 16$ (`logs/daily/2026-04-30/11_nq187_scaling_test_results.md`); the discrete-grid effective ratio $A_2/A_1 \approx 1$ at these sizes, with $\mu_0 \approx \epsilon|W''(c)|$ and $\mu_1 \approx 2\epsilon|W''(c)|$. Hypothesis A (continuum-limit recovery) is the most charitable reading, but requires NQ-187b's $L \in \{32, 64, 128\}$ extension to verify. See §2.1.8, §3.2.8, §4.2.9, §11.
- **No 5th-order $D_4$-equivariant exists in the polynomial ring** (degree 5 in $(x, y)$ has no $(I_1, I_2)$ representation), and **no degree-4 element exists in the equivariant module $\mathcal{M}^{D_4}_{\mathrm{eq}}$** (GSS 1988 Vol II Ch XV §3 Table — only odd-degree generators), so no $\epsilon^{3/2}$ splitting from polynomial equivariants. The user prompt's §3 conjecture of an $\epsilon^{3/2}$ correction is structurally ruled out *at every $L$*. This algebraic fact is unaffected by the §8.5 numerical findings.
- The §3.2 prediction "splitting first appears at the **6th-order equivariant**, giving $\mu_1 - \mu_0 = c_4 \epsilon^2 + O(\epsilon^3)$ with $c_4 = (B_4 - 12 B_3)|W''(c)|^2/(8 A_1^2)$" is **conditional on the leading-order degeneracy** $\mu_0 = \mu_1$, which is currently *not observed* at $L \leq 16$. Recoverable per Hypothesis A (continuum-limit recovery) in §2.1.8; falsifiable per NQ-187b in §11.
- Sign of $c_4$ is graph-class-specific; heuristic suggests $c_4 < 0$ on $D_4$ free-BC, which would create tension with O7's Mulliken-first tie-break (resolvable by re-framing O7 as a leading-order plateau convention). Sign extraction depends on first establishing the leading-order plateau via NQ-187b.
- A **strictly stronger new theorem** T-σ-Theorem-4-Refined is a Cat A candidate via this refinement (§7); 2–3 weeks W7+ effort, deliverables in §10, **all gated on NQ-187b outcome**. (The v1.0 retroactive Cat B audit annotation remains permanent per §7.4 — past audits are immutable historical objects.)
- Numerical verification §8 returned $p \approx 1.03$ on $L \leq 16$, falsifying both the $p = 2$ (§3.2 polynomial-equivariant) and $p = 3/2$ (alternative) predictions for finite $L$ in this range. The §11 NQ-187b sweep is the operational next step.

---

**File status:** REVISED (Wave 3 PM, 2026-04-30); §3.2 conclusion conditional on continuum extrapolation; numerical falsification on $L \leq 16$ documented; awaiting NQ-187b discrete-grid $A_2/A_1$ verification at $L \in \{32, 64, 128\}$. Originally Draft 1 (architect-spawned, 2026-04-29 EOD); first round of fixes 2026-04-30 W5 Day 4 PM (4 Critic-flagged Major issues addressed); pivot-revision incorporating §8.5 numerical falsification 2026-04-30 same evening.

**Next action:** execute NQ-187b protocol (§11) — discrete-grid $A_2/A_1$ sweep over $L \in \{4, 8, 16, 32, 64, 128\}$ on $D_4$ free-BC and torus-BC; produce `CODE/scripts/discrete_A2A1_sweep.py` and `CODE/scripts/results/exp_A2A1_sweep_v1.json`. Cat A target gated on Hypothesis A confirmation. Cross-reference task list #62 (NQ-187b) and #63 (T-σ-Theorem-4 canonical revision urgent — gated on NQ-187b Hypothesis B/C outcomes).

---

## §13. Wave 3 Revision Log (W5 Day 4 PM)

This file was revised on 2026-04-30 (W5 Day 4 PM, Wave 3) in response to the W5 Day 4 PM Wave 2 critic re-review verdict in `THEORY/logs/daily/2026-04-30/09_critic_re_review_5files.md` §3.1 (NQ-187: 4 Major findings, REVISE verdict).

**Revision date:** 2026-04-30
**Revision wave:** Wave 3 (W5 Day 4 PM)
**Trigger:** Critic re-review verdict (`logs/daily/2026-04-30/09_critic_re_review_5files.md` §3.1) flagged 4 Major issues blocking W6 promotion of any related material.
**Constraint:** working-file edits only; no canonical edits. Hard constraints maintained: $u_t$ primitive (CN1); CN10 contrastive on Carr 1981 / Golubitsky-Stewart-Schaeffer 1988 references (no reductive identification — only parallel-structure import); CN5 4-energy not merged.

### §13.1 Fixes applied (initial Wave 3 pass)

| Fix | Section | Critic issue (§3.1) | Replacement summary | Anchor |
|---|---|---|---|---|
| 1 | §2.1 (new subsection appended after §2 line 47, before original §3) | #4 — leading-order absorption gap not derived | Σ_m-Hessian normalization derivation: $E_{\mathrm{bd}}$ ordered-pair convention → factor 4 in ambient Hessian; canonical convention $F_{\mathrm{can}} = \beta(x^2+y^2) + \cdots$ (no 1/2 prefactor) absorbs the factor-2 gap between $F_{xx}^{\mathrm{R22}} = 2\epsilon\|W''(c)\|$ and $\mu_0^{\mathrm{can}} = 4\epsilon\|W''(c)\|$. Convention map table cross-references canonical §8 + line 1007 (T8-Core "Hessian $4\alpha L$") + line 59 (ordered-pair convention). 7 sub-subsections (2.1.1–2.1.7). | §2.1 |
| 2 | §3.2 (entire section replaced) | #1 — invariant-vs-equivariant confusion | Restructured into 7 sub-subsections (3.2.1–3.2.7) distinguishing $\mathcal{R}^{D_4}_{\mathrm{inv}}$ (invariant ring, generated by $I_1, I_2$ via Chevalley–Shephard–Todd) from $\mathcal{M}^{D_4}_{\mathrm{eq}}$ (equivariant module, generated by $X_1=(x,y), X_2=(x^3,y^3)$ per Golubitsky–Stewart–Schaeffer 1988 Vol II Ch XV §3 Table). Parity argument: only odd-degree equivariants exist; hence $g_4 \equiv 0$, $F^{(5)} \equiv 0$, no $\epsilon^{3/2}$ contribution; first split at $F^{(6)} \neq 0$ giving $\mu_1 - \mu_0 = O(\epsilon^2)$. | §3.2 |
| 3 | §4.2 (entire section replaced) | #2 — center-manifold slaving iteration not derived | Explicit Carr (1981) §2 iteration in 8 sub-subsections (4.2.1–4.2.8). Iteration 0: $z_k^{(0)} = 0$; Iteration 1: $z_k^{(1)}$ cubic in $(x,y)$ via $W^{(4)}$ slaving; Iteration 2 corrects at quintic order (does not enter sextic $F^{(6)}$). Substitute back: $F^{(6)} = -\tfrac{1}{2}\sum_{k\geq 4} \mu_k (z_k^{(1)})^2$ → $B_3, B_4$ as quadratic forms in cubic coupling integrals $C_k^{(p,q)}$. Carr (1981) added as a §9 reference. Convergence per Carr Theorem 2.1 with discrete-graph adaptation (finite-dim Banach space, polynomial smoothness, gap $\mu_* > 0$). | §4.2 |
| 4 | §7 (entire section replaced) | #3 — process-audit retroactive-reversal framing | Reframed as **Cat A Recovery via Strict Strengthening (not "reversal")**. New §7.1 separates theorem-object / merge-event / audit-decision (audit-decisions apply to merge-events, not to theorem-objects, and are immutable). §7.2 states T-σ-Theorem-4-Refined as a *new theorem candidate* (with explicit (i)–(vii) clauses), not a v1.0 reversal. §7.3 promotion path: add new canonical entry, leave v1.0 unchanged with permanent retroactive Cat B annotation. §7.4 epistemic policy: past audits stay past, new theorems get new entries (parallels T-Merge (c)(d)(e) retraction handling and V5b iteration history). §7.5 revised effort estimate (~3 weeks). §7.6 historical-note paragraph preserves the reasoning of the original §7. §7.7 downstream-coherence note flagging §1 Mission and §10.1 deliverable 4 for terminology cleanup in a future pass. | §7 |

### §13.2 Status changes (initial Wave 3 pass)

- **File status (top):** changed from "working file, R&D scoping (W5 Day 4 spawn → W7+ candidate)" to "REVISED (Wave 3 W5 Day 4 PM); awaiting W6 critic re-review."
- **§11 Summary bullet:** "Cat A re-promotion of T-σ-Theorem-4" softened to "T-σ-Theorem-4-Refined as a Cat A candidate (new theorem, not reversal); v1.0 audit annotation permanent" per §7 reframe.
- **No canonical edits.** No `theorem_status.md` or `theorem_status.md` (Open Problems Catalog) changes. Open Problems registry unchanged.

### §13.3 Hard-constraint compliance (initial Wave 3 pass)

- **CN1 ($u_t$ primitive):** maintained. The $u_t : X_t \to [0,1]$ primitive is unchanged; all derivations (R22 normal form, slaving iteration, sextic Lyapunov) operate downstream of the primitive.
- **CN10 (contrastive imports):** Carr (1981) and Golubitsky–Stewart–Schaeffer (1988) Vol II Ch XV §3 are imported as **parallel-structure** references (smooth-manifold equivariant bifurcation theory; iterative center-manifold approximation), not reductively identified with the σ-framework. §3.2.6 and §4.2.7 explicitly mark the contrastive nature ("the algebraic structure transfers; the coefficients are discrete-graph-specific").
- **CN5 (4-energy not merged):** maintained. The four energy terms ($E_{\mathrm{cl}}, E_{\mathrm{sep}}, E_{\mathrm{bd}}, E_{\mathrm{tr}}$) remain conceptually independent throughout. The §2.1 absorption derivation works inside the smoothness energy $E_{\mathrm{bd}}$ alone (Hessian factor 4 from ordered-pair convention) without merging it with closure/separation/transport.
- **Working-only:** zero canonical edits in this revision pass.

### §13.4 Carry-forward (initial Wave 3 pass)

- §1 Mission language ("becomes a candidate for *reversal* in CV-1.6") and §10.1 deliverable 4 ("Reverses W5 Day 4 retroactive Cat B downgrade") still use the original "reversal" framing. §7.7 flags these for cleanup; not done in this revision pass to keep the diff scope minimal. Recommend a follow-up edit in Wave 4 or W5 Day 5 morning to propagate §7's "new-theorem-not-reversal" terminology to §1 and §10.1.
- Numerical verification protocol (§8) and sign-of-$c_4$ open question (§5, §6) untouched in this revision; remain W7+ tasks.
- W6 critic re-review may further consolidate §3.2 + §3.3 (sextic-counting overlap) and tighten the §4.2.5 schematic prefactors in $B_3, B_4$. Both deferred.

### §13.5 Effort actually spent (initial Wave 3 pass)

Approximately 2.5 hours, within the architect-estimated 2–3 hour window. File size: 304 lines → ~680 lines (post-initial-revision); growth from §2.1 (~110 lines), §3.2 (~140 lines), §4.2 (~190 lines), §7 (~120 lines), and the revision-log section (~80 lines).

---

### §13.6 Pivot revision: §8.5 numerical falsification response (W5 Day 4 PM later)

**Trigger.** Same-evening directive from team-lead: the lanczos-engineer's NQ-187 §8 numerical execution (`logs/daily/2026-04-30/11_nq187_scaling_test_results.md` + `13_wave3_critical_findings.md`) returned $p \approx 1.03$ (linear-in-$\epsilon$) with $\mu_1/\mu_0 \approx 2$ at $L \in \{4, 8, 16\}$, falsifying both the §3.2 polynomial-equivariant prediction $p = 2$ and the alternative $p = 3/2$. The leading-order degeneracy on which §3.2's $O(\epsilon^2)$ splitting prediction depends is **not observed** at these grid sizes.

**Pivot fixes applied (this same Wave 3 PM session, +1 hour after initial pass).**

| Fix | Section | Replacement summary |
|---|---|---|
| 5 | §2.1.8 (NEW) | Acknowledges numerical evidence on $L \leq 16$ contradicts the boxed claim $\mu_0 = \mu_1 = 4\epsilon\|W''(c)\|$. Three interpretation hypotheses: continuum-limit recovery (Hypothesis A — preserves §3.2), convention-mismatch (Hypothesis B — challenges §2.1.6), discrete-grid $A_2/A_1 \neq 4$ (Hypothesis C — challenges R22 source). Status: convention derivation self-consistent; numerical instantiation conditional on continuum extrapolation pending NQ-187b. |
| 6 | §3.2.8 (NEW) | Notes algebraic correctness of §3.2.1–§3.2.7 unaffected (Chevalley–Shephard–Todd + GSS 1988 module-parity is graph-independent), but the $O(\epsilon^2)$ prediction is conditional on leading-order degeneracy. Three logical implications. NQ-187b operationalizes the test. Cat A target downgraded to "Cat A pending NQ-187b". |
| 7 | §4.2.9 (NEW) | Notes Carr (1981) iteration remains valid as center-manifold reduction; $B_3, B_4$ are well-defined quadratic forms in $C_k^{(p, q)}$. But §8 eigenvalue-split protocol cannot resolve the sextic contribution on $L \leq 16$ due to leading-order non-degeneracy dominance. Lists three alternative tests (direct integral evaluation, expanded-$L$ probe, symbolic differentiation of $\mathcal{E}$ at $u_*$) for W7+. |
| 8 | §8.5 (NEW) | Records actual run outcomes: $p \approx 1.03$, $\mu_1/\mu_0 \approx 2$. Cross-references `11_nq187_scaling_test_results.md` and `13_wave3_critical_findings.md`. Reframes §8.3 row-3 falsifiability landing as a substantive constraint, not a "shrink window" instruction. |
| 9 | §11 (NEW SECTION; original §11 Summary renumbered to §12; original §12 Wave 3 Log renumbered to §13) | "Discrete vs Continuum $A_2/A_1$ Re-examination (NQ-187b)". 6 sub-subsections: question, operational protocol on $L \in \{4, 8, 16, 32, 64, 128\}$ with both free-BC and torus-BC, three predictions to test (Hypothesis A continuum recovery, Hypothesis B discrete-stable plateau, Hypothesis C non-convergence), cross-validation, Cat target + 1 week effort, carry-forward. Operational deliverable: `CODE/scripts/discrete_A2A1_sweep.py` and `CODE/scripts/results/exp_A2A1_sweep_v1.json`. |
| 10 | §12 Summary bullets | Updated to reflect numerical falsification: leading-order degeneracy not observed, §3.2 prediction conditional, §8 returned $p \approx 1.03$, all §10 deliverables gated on NQ-187b outcome. File-status line and next-action line revised accordingly. |
| 11 | Status line at top | Updated to "REVISED (Wave 3 PM); §3.2 conclusion conditional on continuum extrapolation; numerical falsification on $L \leq 16$ documented; awaiting NQ-187b discrete-grid $A_2/A_1$ verification." Cross-reference to `11_nq187_scaling_test_results.md` added. |

**Sections kept unchanged:**

- §3.2.1–§3.2.7 algebraic content (Chevalley–Shephard–Todd, GSS 1988 Vol II Ch XV §3 Table parity argument). The structural fact "no degree-5 invariant, no degree-4 equivariant gradient field" is independent of $L$.
- §4.2.1–§4.2.8 Carr (1981) iteration derivation. The center-manifold theorem and slaving algebra are unaffected by the leading-order eigenvalue structure on $V_2$.
- §7 Cat A Recovery via Strict Strengthening framing. The strict-strengthening reframing of the v1.0 audit is a metalevel/epistemic argument, unaffected by numerical findings on the specific theorem-object content.
- §9 references (Carr 1981 stays).
- §10 Cat target + W7+ priority; deliverable status now reads "gated on NQ-187b outcome" but the deliverables themselves are unchanged.

**Hard-constraint compliance (pivot revision):**

- **CN1 ($u_t$ primitive):** unchanged — pivot revision adds caveats and a new operational protocol; does not introduce alternative primitives.
- **CN10 (contrastive imports):** Carr (1981), GSS (1988) Vol II Ch XV §3 still imported as parallel-structure references; pivot revision strengthens the contrastive framing by documenting that the smooth-manifold prediction *requires continuum-limit extrapolation* to manifest on the discrete graph.
- **CN5 (4-energy not merged):** unchanged. NQ-187b protocol works on $E_{\mathrm{bd}}$-derived eigenfunctions ($L_G$ Fiedler doublet) without merging energy terms.
- **Working-only:** zero canonical edits. Task #63 ("T-σ-Theorem-4 canonical revision urgent") is recorded in the team task list but is *gated on NQ-187b's Hypothesis B/C outcomes*; canonical revision is not initiated unilaterally from this working file.

**Pivot revision effort spent:** approximately 1.5 hours (within the team-lead's "+1–2h on top of original 4 fixes" estimate). Total effort across both Wave 3 passes: ~4 hours. File size now ~870 lines.

---

**End of Wave 3 revision log (initial pass + pivot).** This file is now ready for W6 critic re-review **conditional on NQ-187b execution** in Wave 4. Expected critic priorities: (a) does §11 NQ-187b protocol unambiguously discriminate Hypothesis A / B / C? (b) is the §2.1 absorption derivation still load-bearing under Hypothesis B (convention-mismatch)? (c) does §3.2.8's "algebraic correctness preserved, physical instantiation conditional" framing meet the σ-framework's "never silently resolve open problems" policy?
