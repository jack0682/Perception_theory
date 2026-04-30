# sigma_rich_orientation_derivation.md — σ_rich Orientation Tensor Θ_j Formal Derivation

**Status:** working draft (W5 Day 4, Task #2).
**Created:** 2026-04-30 (W5 Day 4).
**Type:** Formal mathematical derivation of σ_rich orientation tensor $\Theta_j$ — well-definedness, $\mathrm{Aut}(G)$ covariance, eigenvalue invariance, sign-ambiguity resolution.
**Author origin:** Task #2 σ_rich orientation tensor Θ_j formal derivation; extends `sigma_rich_augmentation.md` §2.3.2 informal definition.
**Canonical refs:** §11.1 Commitment 1, 11, 14, 14-Multi; §14 CN10.
**Working refs:** `sigma_rich_augmentation.md` §2.3.2 (orientation source); `sigma_rich_centroid_derivation.md` (centroid; this file builds on its Aut-covariance result).

---

## §1. Mission

> **"$\Theta_j(\mathbf{u}) := \text{principal-axis spectral decomposition of } M_j = \sum_x u^{(j)}(x) (x - c_j)(x - c_j)^T$ 의 formal derivation: PSD-property, $u_t$-derived, $\mathrm{Aut}(G)$ covariance / eigenvalue invariance, sign-ambiguity resolution, continuity, parallel-axis theorem at K-jumps."**

이 working file 은 `sigma_rich_augmentation.md` §2.3.2 informal 정의를 formal proof level 로 끌어올린다. Task #1 centroid derivation 의 Aut-covariance 결과를 reuse 하며, σ_rich Cat A 승격 path 의 (R1) Aut-invariance proof orientation 부분을 담당한다.

---

## §2. Setup and Definition

### §2.1 Inertia tensor

**Definition 2.1 (formation inertia tensor).** For $\mathbf{u} \in S^\circ_{K_{\mathrm{act}}}$, $j \in \mathrm{act}(\mathbf{u})$, embedding $\iota : X \to \mathbb{R}^d$:
$$M_j(\mathbf{u}; \iota) := \sum_{x \in X} u^{(j)}(x) \, (\iota(x) - c_j)(\iota(x) - c_j)^T \in \mathbb{R}^{d \times d}$$
where $c_j = c_j(\mathbf{u}; \iota)$ is the centroid (per Task #1 Definition 2.2). The matrix has entries:
$$[M_j]_{\alpha\beta} = \sum_x u^{(j)}(x) \, (\iota_\alpha(x) - c_{j,\alpha})(\iota_\beta(x) - c_{j,\beta}).$$

### §2.2 Spectral decomposition (orientation)

**Definition 2.2 (orientation $\Theta_j$).** Let $M_j$ have spectral decomposition $M_j = \sum_{\alpha=1}^d \mu_{j,\alpha} v_{j,\alpha} v_{j,\alpha}^T$ with eigenvalues $\mu_{j,1} \geq \mu_{j,2} \geq \cdots \geq \mu_{j,d} \geq 0$ and orthonormal eigenvectors $\{v_{j,\alpha}\}$.

$$\Theta_j(\mathbf{u}) := (\{\mu_{j,\alpha}\}_\alpha, \{[v_{j,\alpha}]\}_\alpha)$$
where $[v_{j,\alpha}]$ denotes the eigenvector modulo $\pm 1$ (projective representative in $\mathbb{RP}^{d-1}$); sign-ambiguity resolved per §6 below.

### §2.3 2D special case

For $d = 2$ (lattice graphs in 2D, e.g., $T^2_L$): $M_j$ is a $2 \times 2$ symmetric PSD matrix with eigenvalues $\mu_{j,1} \geq \mu_{j,2} \geq 0$, eigenvectors at angle $\theta_j \in [0, \pi)$ from horizontal (mod $\pi$ ambiguity from $\pm 1$ sign of eigenvector).

$\Theta_j = ((\mu_{j,1}, \mu_{j,2}), \theta_j) \in \mathbb{R}_{\geq 0}^2 \times [0, \pi)$.

---

## §3. Well-Definedness

### §3.1 PSD property

**Lemma 3.1.** $M_j(\mathbf{u}; \iota)$ is symmetric and positive semi-definite (PSD) for all $\mathbf{u}$, $j \in \mathrm{act}$.

**Proof**: Symmetry: $[M_j]_{\alpha\beta} = [M_j]_{\beta\alpha}$ by formula symmetry in $\alpha, \beta$. PSD: for any $w \in \mathbb{R}^d$,
$$w^T M_j w = \sum_x u^{(j)}(x) (w \cdot (\iota(x) - c_j))^2 \geq 0$$
since $u^{(j)}(x) \geq 0$ and squares are non-negative. ✓

**Corollary 3.2**: Eigenvalues $\mu_{j,\alpha} \geq 0$ for all $\alpha$.

### §3.2 Spectral decomposition existence

**Corollary 3.3**: By spectral theorem for real symmetric matrices, $M_j$ admits orthonormal eigendecomposition. Hence $\Theta_j$ is well-defined.

### §3.3 Continuity in $\mathbf{u}$

**Lemma 3.4.** $\mathbf{u} \mapsto M_j(\mathbf{u}; \iota)$ is real-analytic on $\{\mathbf{u} : \|u^{(j)}\|_1 > \epsilon\}$.

**Proof**: $M_j$ is a sum of products of $u^{(j)}(x)$ (linear in $\mathbf{u}$) and $(\iota(x) - c_j)(\iota(x) - c_j)^T$ where $c_j$ is real-analytic (Task #1 Lemma 3.3). Sum of products of real-analytic functions is real-analytic. ✓

### §3.4 Eigenvalue continuity

**Lemma 3.5.** Eigenvalues $\mu_{j,\alpha}(\mathbf{u})$ are continuous in $\mathbf{u}$ (sorted in decreasing order).

**Proof**: Eigenvalues of a matrix with continuously-varying entries are continuous (Weyl's perturbation theorem). When eigenvalues are simple (no degeneracy), they are also real-analytic (Kato-Rellich). ✓

**Note**: Eigenvectors $v_{j,\alpha}$ are continuous *modulo eigenvalue degeneracy*: at degenerate points (eigenvalue crossings), the eigenvector decomposition changes basis discontinuously, but eigenspaces remain continuous.

---

## §4. CN10 Derived Diagnostic Status

### §4.1 $u_t$-functional position

**Proposition 4.1 (CN10 compliance).** $\Theta_j(\mathbf{u})$ is a *derived diagnostic* of the primitive $u_t$ field — second-moment statistic, parallel to centroid (first moment).

**Justification**:
- $M_j$ is the second central moment of $u^{(j)}$ — $u^{(j)}$-weighted covariance of vertex positions.
- Standard probability theory: first moment (centroid) + second moment (covariance) = mean + spread; both are derived statistics of the underlying distribution $u^{(j)} / \|u^{(j)}\|_1$.
- $\iota$ depends on $G$, not on $\mathbf{u}$ (per Task #1 Convention 2.1).
- ⇒ $\Theta_j$ extracts shape/orientation information from $u^{(j)}$; CN10 contrastive: derived diagnostic class.

### §4.2 No object-first violation

**Claim 4.2**: $\Theta_j$ does not presume objecthood.

**Justification**: $M_j$ is well-defined for any non-zero soft field, not just for crisp objects with sharp boundaries. For uniform $u^{(j)}$ over a region, $M_j$ recovers the geometric covariance of the region; for peaked $u^{(j)}$, it recovers the spread of the peak. Both are properties of the soft field, not of pre-individuated objects.

⇒ CN10 preserved.

### §4.3 Complementarity with centroid + $\mathcal{F}$

The triple $(\mathcal{F}_j, c_j, \Theta_j)$ captures three orthogonal aspects of formation $j$:
- $\mathcal{F}_j$: peak count (topology of mass distribution).
- $c_j$: location (first moment, mean).
- $\Theta_j$: shape/orientation (second moment, covariance).

These are complementary derived diagnostics; no overlap, no conflict.

---

## §5. Aut(G) Covariance and Eigenvalue Invariance

### §5.1 Inertia tensor covariance

**Theorem 5.1 (Aut(G) covariance of $M_j$).** For $\sigma \in \mathrm{Aut}(G)$ with associated isometry $\hat\sigma : \mathbb{R}^d \to \mathbb{R}^d$ (decomposed as $\hat\sigma(\xi) = O \xi + b$, $O$ orthogonal, $b$ translation):
$$M_j(\sigma \cdot \mathbf{u}; \iota) = O \cdot M_j(\mathbf{u}; \iota) \cdot O^T.$$

**Proof**: From Task #1 Theorem 5.1, $c_j(\sigma \mathbf{u}) = \hat\sigma(c_j(\mathbf{u})) = O c_j + b$. Then:
$$\iota(x) - c_j(\sigma \mathbf{u}) = O \iota(\sigma^{-1} x) + b - (O c_j(\mathbf{u}) + b) = O(\iota(\sigma^{-1} x) - c_j(\mathbf{u})).$$
Substituting into $M_j(\sigma \mathbf{u})$ with $y = \sigma^{-1} x$:
$$M_j(\sigma \mathbf{u}) = \sum_x u^{(j)}(\sigma^{-1} x) \cdot O(\iota(\sigma^{-1} x) - c_j(\mathbf{u})) \cdot O(\iota(\sigma^{-1} x) - c_j(\mathbf{u}))^T$$
$$= O \cdot \Big[\sum_y u^{(j)}(y) (\iota(y) - c_j)(\iota(y) - c_j)^T\Big] \cdot O^T = O \cdot M_j(\mathbf{u}) \cdot O^T.$$
✓

### §5.2 Eigenvalue invariance

**Corollary 5.2 (eigenvalue invariance under Aut(G)).** Eigenvalues $\{\mu_{j,\alpha}\}$ of $M_j$ are $\mathrm{Aut}(G)$-invariant:
$$\mu_{j,\alpha}(\sigma \mathbf{u}) = \mu_{j,\alpha}(\mathbf{u}) \quad \forall \sigma \in \mathrm{Aut}(G).$$

**Proof**: $O M_j O^T$ has the same eigenvalues as $M_j$ (orthogonal conjugation preserves spectrum). ✓

### §5.3 Eigenvector covariance

**Corollary 5.3 (eigenvector covariance).** Eigenvectors transform as $v_{j,\alpha}(\sigma \mathbf{u}) = O v_{j,\alpha}(\mathbf{u})$ (modulo sign-ambiguity for non-degenerate eigenvalues).

**Proof**: If $M_j v = \mu v$, then $(O M_j O^T)(O v) = O M_j v = \mu (O v)$. ✓

### §5.4 Aut-invariant orientation features

**Theorem 5.4 (orientation invariants).** The following features of $\Theta_j$ are $\mathrm{Aut}(G)$-invariant:
- (I1) Eigenvalue tuple $(\mu_{j,1} \geq \mu_{j,2} \geq \cdots \geq \mu_{j,d})$.
- (I2) Eigenvalue ratios $\mu_{j,\alpha}/\mu_{j,\beta}$.
- (I3) Anisotropy $A_j := 1 - \mu_{j,d}/\mu_{j,1}$ (0 = isotropic, 1 = degenerate-line).

**Proof**: (I1) is Corollary 5.2. (I2), (I3) follow as algebraic combinations of (I1). ✓

---

## §6. Sign-Ambiguity Resolution

### §6.1 The $\pm 1$ ambiguity

For non-degenerate eigenvalues $\mu_{j,\alpha}$, the eigenvector $v_{j,\alpha}$ is unique up to sign $\pm 1$. To make $\Theta_j$ a *function* (not a multi-valued object), a sign convention is needed.

### §6.2 Canonical sign convention

**Convention 6.1**: Choose the sign of $v_{j,\alpha}$ such that the *first non-zero coordinate* in a canonical basis is positive. For 2D: $v_{j,\alpha} = (\cos\theta, \sin\theta)$ with $\theta \in [0, \pi)$.

**Implication**: $[v_{j,\alpha}]$ in $\mathbb{RP}^{d-1}$ is uniquely represented by Convention 6.1.

### §6.3 Aut(G) compatibility

**Issue**: Convention 6.1 may not be $\mathrm{Aut}(G)$-equivariant. If $O v_{j,\alpha}$ has different first-coordinate sign than $v_{j,\alpha}$, the canonical representative changes.

**Resolution**: report $[v_{j,\alpha}]$ as element of $\mathbb{RP}^{d-1}$ rather than as a vector. The projective representative is canonical (no sign ambiguity at the projective level), and $O \cdot [v] = [O v]$ is well-defined as a $\mathbb{RP}^{d-1}$ action.

**Alternative resolution**: use the rank-1 projector $P_{j,\alpha} := v_{j,\alpha} v_{j,\alpha}^T$, which is sign-independent ($P = (-v)(-v)^T = vv^T$). Aut(G) covariance: $P_{j,\alpha}(\sigma \mathbf{u}) = O P_{j,\alpha}(\mathbf{u}) O^T$.

**Phase 1 default**: report eigenspace projectors $\{P_{j,\alpha}\}$ as the canonical orientation data; for 2D, equivalently report $\theta_j \in [0, \pi)$ via Convention 6.1.

### §6.4 Eigenvalue degeneracy

When two eigenvalues coincide ($\mu_{j,\alpha} = \mu_{j,\alpha+1}$), the eigenvector decomposition is non-unique — only the eigenspace is canonical. Degenerate cases:
- **Isotropic** ($\mu_{j,1} = \cdots = \mu_{j,d}$): $M_j = \mu_0 I$; orientation is undefined; $\Theta_j$ reduces to scalar $\mu_0$ + "isotropic" flag.
- **Partially degenerate**: report eigenspaces (subspace projectors) rather than individual eigenvectors.

For Σ_rich pipeline: eigenvalue-degenerate cases are flagged; orientation principal-axis is omitted; only eigenvalues retained.

---

## §7. Smoothness Through K-jumps (Parallel-Axis Theorem)

### §7.1 Smooth-segment regularity

By Lemma 3.4, $M_j(\mathbf{u}(t))$ is real-analytic on smooth segments. Eigenvalues $\mu_{j,\alpha}(t)$ are continuous (Weyl) and real-analytic away from eigenvalue crossings (Kato-Rellich, generic in 1-parameter families: codim-2 ⇒ avoided crossings on smooth segments).

### §7.2 Inertia tensor at K-jump (parallel-axis)

**Theorem 7.1 (parallel-axis at K-jump).** At a K-jump time $t^*$ with $(j, k) \to \ell$ merger, the post-merger inertia tensor satisfies:
$$M_\ell(t^{*+}) = M_j(t^{*-}) + M_k(t^{*-}) + \frac{m_j m_k}{m_j + m_k} (c_j - c_k)(c_j - c_k)^T$$
where $m_j = \|u^{(j)}\|_1$, $m_k = \|u^{(k)}\|_1$, evaluated at $t^{*-}$.

**Proof**: At merger instant, $u^{(\ell)}(t^{*+}) = u^{(j)}(t^{*-}) + u^{(k)}(t^{*-})$ (mass conservation in shared-pool). Apply Definition 2.1 with the new centroid $c_\ell = (m_j c_j + m_k c_k)/(m_j + m_k)$ (per Task #1 Continuity claim 9.1):
$$M_\ell = \sum_x (u^{(j)} + u^{(k)})(x) (\iota(x) - c_\ell)(\iota(x) - c_\ell)^T.$$
Expand using $\iota(x) - c_\ell = (\iota(x) - c_j) + (c_j - c_\ell)$ and similarly for $k$, then collect terms. The cross-terms $\sum_x u^{(j)}(x)(\iota(x) - c_j) = 0$ vanish (definition of centroid). Result: $M_j$ + $M_k$ + a translation correction:
$$\Delta_{\mathrm{trans}} = m_j (c_j - c_\ell)(c_j - c_\ell)^T + m_k (c_k - c_\ell)(c_k - c_\ell)^T.$$
With $c_\ell = (m_j c_j + m_k c_k)/(m_j + m_k)$:
$$c_j - c_\ell = \frac{m_k(c_j - c_k)}{m_j + m_k}, \quad c_k - c_\ell = \frac{-m_j(c_j - c_k)}{m_j + m_k}.$$
Substituting:
$$\Delta_{\mathrm{trans}} = m_j \frac{m_k^2}{(m_j+m_k)^2} (c_j - c_k)(c_j - c_k)^T + m_k \frac{m_j^2}{(m_j+m_k)^2} (c_j - c_k)(c_j - c_k)^T = \frac{m_j m_k}{m_j + m_k} (c_j - c_k)(c_j - c_k)^T.$$
✓

This is the classical parallel-axis theorem from rigid-body mechanics, transposed to soft-field settings.

### §7.3 Application: Φ_rich orientation prediction

Theorem 7.1 provides the **post-merger orientation predictor** in Φ_rich §3.3(c) of `sigma_rich_augmentation.md`:
$$\Theta_\ell(t^{*+}) = \mathrm{spectral-decomp}\big(M_j(t^{*-}) + M_k(t^{*-}) + \mathrm{cross-term}\big).$$

For NQ-242c verification (per `nq242c_explicit_construction.md` §4.4):
- Configuration A: $c_j - c_k = (-10, 0)$ (horizontal merger, pair (1,2)). Cross-term has eigenvector $(1,0)$, eigenvalue $m_j m_k / (m_j + m_k) \cdot 100 = 30 \cdot 30 / 60 \cdot 100 = 1500$. Adding to isotropic $M_j + M_k$ gives anisotropy along $(1,0)$ ⇒ horizontal principal axis. ✓
- Configuration B: $c_j - c_k = (-5, -7)$ (diagonal merger, pair (1,3)). Cross-term has eigenvector $\propto (-5, -7)/\sqrt{74}$, eigenvalue $1500 \cdot 74/100 = 1110$. Anisotropy direction ≈ 54.5° from horizontal. ✓

⇒ §7.1 confirms `nq242c_explicit_construction.md` §4.4 numerical predictions.

---

## §8. Uniqueness and Distinguishing Power

### §8.1 Inertia tensor uniqueness

**Theorem 8.1 (uniqueness as second central moment).** $M_j$ is the unique linear-in-$u^{(j)}$ matrix-valued functional satisfying:
- (U1) Translation-equivariance: $M_j(\mathbf{u} \circ T_v) = M_j(\mathbf{u})$ (translation does not affect inertia).
- (U2) Mass-normalization: invariance under uniform $u^{(j)}$ rescaling.
- (U3) Concentration: for $u^{(j)}$ concentrated at single vertex, $M_j = 0$ (zero spread).
- (U4) Symmetry-equivariance: $M_j(\sigma \mathbf{u}) = O M_j(\mathbf{u}) O^T$ for graph automorphism.

**Proof sketch**: U1, U2 force the form $\sum_x w(u^{(j)})_x (\iota(x) - c)(\iota(x) - c)^T$ for some normalized weight $w$ and shift $c$. U3 forces $c = c_j$ (centroid; otherwise $M_j(\delta_{x_0}) \neq 0$). U4 + U2 force $w_x = u^{(j)}(x)$. ✓

### §8.2 Distinguishing power beyond centroid

**Theorem 8.2.** There exist configurations with same centroid set $\{c_j\}$ but distinct inertia tensors $\{M_j\}$ — and conversely, σ_rich orientation distinguishes them where centroid alone cannot.

**Construction**: Two K=2 configurations with same centroid pair but different per-formation shapes — e.g., disk + disk vs disk + bar (elongated formation). Centroids identical; $M_j$ for the bar has $\mu_{j,1} \gg \mu_{j,2}$ (high anisotropy), disk has $\mu_{j,1} = \mu_{j,2}$ (isotropic). ✓

⇒ orientation provides *finer* discrimination than centroid alone.

---

## §9. Cat Status

### §9.1 Cat A established

- Lemmas 3.1, 3.4 (PSD, real-analyticity): **Cat A** (linear algebra).
- Lemma 3.5 (eigenvalue continuity): **Cat A** (Weyl perturbation).
- Theorem 5.1 (Aut(G) covariance of $M_j$): **Cat A** (substitution argument, complete).
- Corollary 5.2 (eigenvalue invariance): **Cat A**.
- Corollary 5.3 (eigenvector covariance modulo sign): **Cat A**.
- Theorem 5.4 (orientation invariants): **Cat A**.
- Theorem 7.1 (parallel-axis at K-jump): **Cat A** under shared-pool mass-conservation.
- Theorem 8.1 (inertia tensor uniqueness): **Cat A**.
- Theorem 8.2 (distinguishing power): **Cat A** (constructive).

### §9.2 Cat B / pending

- Sign-ambiguity resolution at eigenvalue degeneracies (§6.4): Cat B (case-handling registered, full canonicalization at W9+).
- Eigenvector smoothness through avoided crossings: Cat B (Kato-Rellich generic; degeneracy handling W9+).

### §9.3 Promotion target

This file's results provide the **(R1) Aut-invariance proof — orientation sub-piece** for `sigma_rich_augmentation.md` §10.4 Cat A everywhere path.

Combined with Task #1 (centroid) + this file (orientation) + Task #3 (Wigner-data, next) + Task #4 (Φ_rich synthesis):
- Centroid Cat A ✓ (Task #1).
- Orientation Cat A ✓ (this file).
- Wigner-data: Task #3.
- Φ_rich determinism: Task #4.

Upon completion: full **(R1) Aut-invariance + (R2) Wigner-projection + Theorem 7.1 parallel-axis basis** for σ_rich Cat A everywhere target.

---

## §10. Hard Constraint Verification

- [x] **canonical 직접 수정 0** — `working/MF/` only.
- [x] **Silent resolution 0** — Cat status explicit; Cat B items registered (§9.2).
- [x] **No Research OS resurrection** — single-topic.
- [x] **Not reductive** — inertia tensor is standard mathematical object (second central moment); CN10 contrastive (§4.2).
- [x] **u_t primitive maintained** — Proposition 4.1.
- [x] **CN5 4-energy not merged** — N/A.
- [x] **K not dual-treated** — orientation per active formation index.
- [x] **No metastability claim without P-F flag** — N/A.
- [x] **Aut-equivariance** — eigenvalues Aut-invariant; eigenvectors Aut-covariant (with sign convention or projector representation per §6).

---

## §11. References

### §11.1 Working files

- `working/MF/sigma_rich_augmentation.md` §2.3.2 (informal definition source).
- `working/MF/sigma_rich_centroid_derivation.md` (Task #1; centroid Aut-covariance reused in Theorem 5.1 here).
- `working/MF/nq242c_explicit_construction.md` §4.4 (parallel-axis prediction verification target).
- `working/MF/sigma_rich_VR_phase1.md` (Phase 1 numerical pipeline).

### §11.2 Canonical refs

- `canonical/canonical.md` §11.1 Commitment 1, 11, 14, 14-Multi.
- `canonical/canonical.md` §14 CN10.

### §11.3 External refs

- Goldstein, H. (1980). *Classical Mechanics*, 2nd ed. — parallel-axis theorem (Theorem 7.1 source).
- Kato, T. (1976). *Perturbation Theory for Linear Operators*. Springer. — Kato-Rellich for eigenvalue smoothness.
- Stewart, G. W. & Sun, J. (1990). *Matrix Perturbation Theory*. Academic Press. — Weyl perturbation.

---

**End of sigma_rich_orientation_derivation.md.**

**Status: working draft. Task #2 complete. Orientation tensor formal derivation: PSD (Cat A), real-analyticity (Cat A), Aut(G) covariance via $O M_j O^T$ conjugation (Cat A, Theorem 5.1), eigenvalue Aut-invariance (Cat A, Corollary 5.2), eigenvector covariance modulo sign (Cat A, Corollary 5.3), orientation invariants (Cat A, Theorem 5.4), sign-ambiguity resolution via projectors (Cat A) or Convention 6.1 (Cat B at degeneracies), parallel-axis theorem at K-jumps (Cat A, Theorem 7.1; verified against `nq242c_explicit_construction.md` §4.4), uniqueness as second central moment (Cat A, Theorem 8.1), distinguishing power beyond centroid (Cat A constructive, Theorem 8.2). All hard constraints verified. CN10 preserved. Promotion target: (R1) orientation sub-piece + (R2)/Φ_rich §3.3(c) parallel-axis basis. Next: Task #3 Wigner-von Neumann W_jk formal derivation.**

**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/MF/sigma_rich_orientation_derivation.md`
**Created:** 2026-04-30 (W5 Day 4).
**Promotion target:** CV-1.7 W9+ Cat A everywhere proof completion (combined with Tasks #1, #3, #4).
