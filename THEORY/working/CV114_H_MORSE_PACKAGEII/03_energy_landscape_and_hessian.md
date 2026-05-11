# 03 — Energy Landscape and Hessian

Agent B (Mathematical Analyst) — explicit Hessian structure on $\Sigma_m$ for the full SCC energy.

---

## 1. Energy

Canonical full SCC energy (canonical.md §10–§13):

$$\mathcal E(u) = \lambda_\mathrm{cl}\,\mathcal E_\mathrm{cl}(u) + \lambda_\mathrm{sep}\,\mathcal E_\mathrm{sep}(u) + \lambda_\mathrm{bd}\,\mathcal E_\mathrm{bd}(u),$$

with components (using canonical conventions, $b_D = 0$, $a_\mathrm{cl} \in (0,4)$):

- **Boundary morphology** (Allen-Cahn):
$$\mathcal E_\mathrm{bd}(u) = 2\alpha \cdot u^T L u + \beta \sum_{i \in X_t} W(u_i),\quad W(u) = u^2 (1-u)^2.$$
Note canonical factor 4 in the gradient: $\nabla \mathcal E_\mathrm{bd} = 4\alpha L u + \beta W'(u)$, with $W'(u) = 2u(1-u)(1-2u)$ (CLAUDE.md "ordered-pair sum" convention).

- **Closure**: $\mathcal E_\mathrm{cl}(u) = \frac{1}{2}\|u - \mathrm{Cl}(u)\|^2$, where $\mathrm{Cl}$ is the canonical closure operator (sigmoid + $a_\mathrm{cl}$-scaled smoothing, `operators.py`).

- **Separation**: $\mathcal E_\mathrm{sep}(u)$ — penalty for boundary co-belonging (u-weighted, see `predicates.py` and canonical §9.3).

---

## 2. Constrained domain

$$\Sigma_m = \{u \in [0,1]^n : \mathbf 1^T u = m\}.$$

This is a **convex polytope** of dimension $n - 1$ with corners. Its interior $\Sigma_m^\circ = \{u : 0 < u_i < 1,\, \mathbf 1^T u = m\}$ is a smooth $(n-1)$-manifold.

**Tangent space at interior point**:
$$T_u \Sigma_m^\circ = \mathbf 1^\perp = \{v \in \mathbb R^n : \mathbf 1^T v = 0\}.$$

**Tangent projector** (orthogonal projection onto $\mathbf 1^\perp$):
$$\Pi_T = I - \frac{1}{n}\mathbf 1 \mathbf 1^T.$$

Properties: $\Pi_T^2 = \Pi_T$, $\Pi_T^T = \Pi_T$, $\Pi_T \mathbf 1 = 0$, eigenvalues $\{0, 1, 1, \ldots, 1\}$ (the 0-eigenspace is $\mathbb R \mathbf 1$).

---

## 3. Critical point equation

KKT on $\Sigma_m^\circ$: there exists a Lagrange multiplier $\mu \in \mathbb R$ such that

$$\nabla \mathcal E(u^*) = \mu \mathbf 1, \quad \mathbf 1^T u^* = m.$$

Equivalently: $\Pi_T \nabla \mathcal E(u^*) = 0$.

At an interior critical point, the Lagrange multiplier is $\mu = \frac{1}{n}\mathbf 1^T \nabla \mathcal E(u^*)$.

---

## 4. Projected Hessian

Full Hessian at $u^*$:
$$H_\mathcal E(u^*) = H_\mathrm{cl}(u^*) + H_\mathrm{sep}(u^*) + H_\mathrm{bd}(u^*).$$

**Boundary Hessian** (Allen-Cahn, explicit):
$$H_\mathrm{bd}(u) = 4\alpha L + \beta \cdot \mathrm{diag}(W''(u))$$
where $W''(u) = 2 - 12u + 12u^2$ for the double-well $W(u) = u^2(1-u)^2$.

**Closure Hessian** (uses sigmoid Jacobian; cf. H-SINK-1 + canonical.md §9.2):
$$H_\mathrm{cl}(u) = (I - J_\mathrm{Cl}(u))^T (I - J_\mathrm{Cl}(u)) + \text{(2nd-order terms from } u - \mathrm{Cl}(u)\text{)}.$$
At a critical point with small closure residual $r := u^* - \mathrm{Cl}(u^*)$, the dominant contribution is $(I - J_\mathrm{Cl})^T(I - J_\mathrm{Cl})$, which is positive semidefinite.

**Separation Hessian** $H_\mathrm{sep}(u)$: derivation similar; contributes nonnegative contribution in the spinodal interior (cf. canonical §13).

**Projected Hessian on $T_{u^*}\Sigma_m^\circ$:**
$$H^\mathrm{proj}_\mathcal E(u^*) = \Pi_T H_\mathcal E(u^*) \Pi_T.$$

The Lagrange-multiplier term does NOT appear: since $\nabla(\mathbf 1^T u) = \mathbf 1$ has zero Hessian, the bordered Hessian on the constraint surface coincides with the orthogonal projection of $H_\mathcal E$.

---

## 5. Sign structure of contributions

### 5.1 Boundary Hessian on $\Sigma_m$

For $u \equiv c \mathbf 1$ (uniform state), $\Pi_T H_\mathrm{bd} \Pi_T = 4\alpha \Pi_T L \Pi_T + \beta W''(c) \Pi_T$.

- $\Pi_T L \Pi_T$ has eigenvalues $\{0, \lambda_2, \lambda_3, \ldots, \lambda_n\}$ where the 0-eigenvalue is $\Pi_T$'s null space. On $T_{u^*}\Sigma_m^\circ$ the effective spectrum starts at $\lambda_2$ (Fiedler).
- $W''(c)$ is negative on the **spinodal interval** $c \in ((3-\sqrt 3)/6, (3+\sqrt 3)/6)$.

**Phase transition condition (T8-Full, Cat A):** uniform state $u \equiv c$ in spinodal interior is unstable iff $\beta/\alpha > 4\lambda_2 / |W''(c)|$. **At the threshold $\beta/\alpha = 4\lambda_2/|W''(c)|$, the Hessian has an exact zero eigenvalue** (the Fiedler direction) — bifurcation point, **non-Morse**.

This is itself a structural counterexample to unconditional H-MORSE: at any threshold parameter, the system has a zero Hessian eigenvalue. (CV-1.14 H-MORSE-Local must explicitly exclude bifurcation parameters by working strictly above threshold.)

### 5.2 Closure-correction gap (canonical.md §13 line 1139, Cat A)

> Non-trivial constrained minimizers of SCC energy have strictly larger minimum Hessian eigenvalue than corresponding Allen-Cahn minimizers, due to the self-referential closure correction.

This is a Cat A theorem. At a non-trivial single-formation minimizer $u^*$ of full $\mathcal E$ (not of $\mathcal E_\mathrm{bd}$ alone — those are different critical points by T-PreObj-1!):

$$\mu_\mathrm{min}(H^\mathrm{proj}_\mathcal E(u^*)) > \mu_\mathrm{min}(H^\mathrm{proj}_{\mathcal E_\mathrm{bd}}(\tilde u^*))$$

for the corresponding Allen-Cahn minimizer $\tilde u^*$ with the same support. The gap is strict because $(I - J_\mathrm{Cl})^T(I - J_\mathrm{Cl})$ is positive definite when $J_\mathrm{Cl}$ has spectral norm $< 1$ (canonical axiom A3: $a_\mathrm{cl} < 4$ implies $L_\mathrm{cl} < 1$ from H-SINK-1).

**This gap is the key analytical input** for H-MORSE-Local. It is Cat A, available, and quantitative.

### 5.3 Symmetry-induced zero modes

If $\sigma \in \mathrm{Aut}(G)$ fixes $u^*$ (i.e., $u^* \circ \sigma = u^*$ as functions on vertices), then the orbital decomposition theorem (canonical.md line 1362, Cat A) gives a block decomposition of $H^\mathrm{proj}$ according to irreducible representations of $\mathrm{Stab}_{\mathrm{Aut}(G)}(u^*)$. **Degeneracies within each irrep are structural** and cannot be removed without breaking symmetry.

For translation-invariant graphs (canonical.md V5b-T-zero, Cat A): the discrete translation group $\mathbb Z_L^d$ generically does NOT fix any non-uniform minimizer; instead it acts freely, producing an orbit of equienergetic minimizers. The Goldstone directions tangent to this orbit are **exact zero modes** of $H^\mathrm{proj}$ in the sub-spinodal regime.

---

## 6. T7-Enhanced provides basin depth, not Morse

T7-Enhanced (Theorem 7 enhanced metastability, hypothesis_tree.md Q3 reference) gives:

$$\Delta \mathcal E := \mathcal E(\text{saddle}) - \mathcal E(\text{minimum}) > \Delta \mathcal E_0 > 0$$

— a positive barrier. This is essential for Eyring-Kramers (the Arrhenius exponent $\exp(-\Delta\mathcal E/T_*)$), but it says **nothing** about nondegeneracy of the saddle Hessian. A degenerate saddle still has a barrier height but the EK prefactor (involving $|\det H^\mathrm{proj}|^{1/2}$ at the saddle) becomes singular or undefined.

**Conclusion:** T7-Enhanced gates the Arrhenius exponent; H-MORSE gates the prefactor. They are independent.

---

## 7. T14 convergence requires only Łojasiewicz, not Morse

T14 (canonical Cat A, canonical.md line 1131): gradient flow converges to a critical point via Łojasiewicz-Simon inequality for analytic energy.

This works **even at degenerate critical points** (Łojasiewicz exponent $\theta \in (0, 1/2]$). T14 does NOT require Morse nondegeneracy. Therefore:

- Convergence to a critical point: Cat A unconditional.
- Convergence with exponential rate (requires Morse): currently unproved → opens the same gap as H-MORSE.
- Eyring-Kramers prefactor: requires Morse-2 nondegeneracy.

H-MORSE is a strict strengthening of what T14 needs.

---

## 8. Small finite-graph symbolic checks

### 8.1 Two-node graph $K_2$, $m = 1$

$n = 2$, $\Sigma_m = \{(u_1, u_2) : u_1 + u_2 = 1, 0 \leq u_i \leq 1\}$ — a 1-simplex (line segment).

Tangent space: $\mathbf 1^\perp = \mathrm{span}\{(1, -1)/\sqrt 2\}$, dim 1.

Laplacian: $L = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$, eigenvalues $\{0, 2\}$.

For uniform $u = (1/2, 1/2)$:
- $\Pi_T L \Pi_T$ has the single nontrivial eigenvalue 2.
- $\Pi_T W''(1/2) I \Pi_T = W''(1/2) \cdot 1 = -1$ (since $W''(1/2) = -1$, in spinodal).
- $\Pi_T H_\mathrm{bd} \Pi_T = 4\alpha \cdot 2 - \beta = 8\alpha - \beta$.
- Sign: at $\beta/\alpha = 8$, zero eigenvalue (bifurcation); for $\beta/\alpha > 8 = 4\lambda_2/|W''(1/2)| = 4 \cdot 2 / 1$, the uniform state is unstable.

This matches T8-Full. The non-uniform minimizers of the full SCC energy break the $\mathbb Z_2$ symmetry of $K_2$; they have stabilizer $\{e\}$, so M-A2 holds and the closure-correction gap applies. **H-MORSE-Local would yield $\mu_\mathrm{min} > 0$ at the non-uniform minimizer on $K_2$, $m=1$.**

### 8.2 Cycle $C_n$ — counterexample to unconditional H-MORSE

$n$ vertices, Laplacian $L_\mathrm{cycle}$ with eigenvalues $\{2 - 2\cos(2\pi k/n) : k = 0, 1, \ldots, n-1\}$, eigenvectors $\phi_k(j) = \cos(2\pi kj/n)$ or $\sin(2\pi kj/n)$.

Discrete translation group $\mathbb Z_n$ acts freely on configuration space; a localized single-blob minimizer $u^*$ has an orbit of $n$ translates, all equienergetic. The orbit-tangent direction $\delta u_x = u^* \circ \mathrm{shift}_1 - u^*$ is in the **exact** zero-eigenspace of $H^\mathrm{proj}$ (V5b-T-zero Cat A for sub-spinodal; V5b-T-b super-lattice for exponentially small positive in spinodal).

**Unconditional H-MORSE FAILS on $C_n$.** H-MORSE-Local needs M-A2 (symmetry-broken), which $C_n$ violates.

### 8.3 Three-node path $P_3$

$L_{P_3} = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix}$, eigenvalues $\{0, 1, 3\}$, Fiedler $= 1$.

Path graph has $\mathbb Z_2$ symmetry (reflection). A non-uniform single-formation minimizer can either:
- Break the reflection → orbit of 2 minimizers, each with stabilizer $\{e\}$ → M-A2 holds.
- Respect the reflection → fixed by reflection → orbital decomposition into symmetric + antisymmetric blocks. Each block separately Morse but they may share a degenerate eigenvalue.

**On $P_3$ with reflection-symmetric minimizer**, H-MORSE-Local needs additional work: either restrict to symmetry-broken minimizers (M-A2 exclusion) or apply orbital quotient (Theorem 1 of canonical §13).

### 8.4 2×2 grid

$D_4$ symmetry. Uniform state $u \equiv c$ fixed by full $D_4$. Non-uniform single-formation minimizers exist (e.g., "two adjacent corners high, two opposite low" — but this requires $K = 2$); the canonical $K = 1$ minimizer is just the uniform state, which is symmetric.

Conclusion: **2×2 is too small** for nontrivial single-formation $K=1$ minimizers. Need at least 3×3 or 5×5.

### 8.5 3×3 grid

$D_4$ symmetry, $n = 9$. Plausible single-formation $K = 1$ minimizer: localized blob centered at any of 9 sites. The $D_4$ orbit has 9 (or fewer, if center) elements.

Center-located minimizer has full $D_4$ stabilizer (8 elements); off-center has smaller stabilizer. Generic perturbation moves to off-center minima with $\{e\}$ stabilizer satisfying M-A2.

**Conclusion:** On 3×3, H-MORSE-Local Cat B applies to off-center minimizers; center-located requires orbital quotient.

### 8.6 Canonical 15×15

$D_4$ symmetry, $n = 225$. Single-formation $K = 1$ minimizers from `find_formation` typically settle to off-center positions when initial conditions are random; their stabilizer is generically $\{e\}$ (M-A2 holds). The canonical exp01 / exp83 anchor uses 15×15 with off-center single-formation; H-MORSE-Local Cat B should apply directly.

---

## 9. Summary

The Hessian structure on $\Sigma_m^\circ$ has:
- A **clearly identifiable positive contribution** from the closure-correction gap (Cat A).
- **Structural zero modes** from discrete translation (V5b-T-zero / V5b-T-b Cat A) and graph automorphism (Theorem 1 orbital Cat A).
- A **bifurcation singularity** at the T8-Full threshold (must be excluded by working in the spinodal interior with strict $\beta/\alpha > 4\lambda_2/|W''(c)|$).
- A **boundary stratum** $\partial\Sigma_m$ requiring stratified Morse (deferred).

H-MORSE-Local on $\Sigma_m^\circ$ at symmetry-broken minimizers in the canonical phase-separated regime is **the right CV-1.14 target**. Cat B classification appropriate.

Do not generalize beyond the cases checked above without explicit canonical anchoring.
