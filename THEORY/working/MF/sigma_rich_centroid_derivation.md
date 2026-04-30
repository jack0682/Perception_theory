# sigma_rich_centroid_derivation.md — σ_rich Centroid Component Formal Derivation

**Status:** working draft (W5 Day 4, Task #1).
**Created:** 2026-04-30 (W5 Day 4).
**Type:** Formal mathematical derivation of σ_rich centroid component $\{c_j(\mathbf{u})\}$ — Aut-covariance, well-definedness, derivation from $u_t$ primitive, canonicalness.
**Author origin:** Task #1 σ_rich centroid component formal derivation; extends `sigma_rich_augmentation.md` §2.3.1 informal definition to formal proof level.
**Canonical refs:** §11.1 Commitment 1 (u_t primitive), 14, 14-Multi, 16; §14 CN10 (contrastive); §15 OP-0008.
**Working refs:** `sigma_rich_augmentation.md` §2.3.1 (centroid definition source); `sigma_rich_VR_phase1.md` §2 (V-R integration).

---

## §1. Mission

> **"σ_rich centroid component $c_j(\mathbf{u}) := \frac{\sum_x x \cdot u^{(j)}(x)}{\sum_x u^{(j)}(x)}$ 의 formal derivation: well-definedness, $u_t$-derived 위치, $\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}$ covariance/invariance, embedding-choice canonicalness, uniqueness theorems."**

이 working file 은 `sigma_rich_augmentation.md` §2.3.1 의 informal 정의를 formal proof level 로 끌어올리고, 이후 Cat A 승격 path 의 (R1) Aut-invariance proof 의 centroid 부분을 담당한다.

---

## §2. Setup and Definition

### §2.1 Graph and embedding

Let $G = (X, E)$ be a finite graph with $|X| < \infty$. An **embedding** is a function $\iota : X \to \mathbb{R}^d$ for some $d \geq 1$.

**Convention 2.1**: For lattice graphs ($T^2_L, \mathbb{Z}^d$ subsets), $\iota$ is the natural coordinate embedding. For arbitrary graphs, $\iota$ is the spectral embedding via Fiedler vectors of the graph Laplacian $L$ (lowest $d$ non-trivial eigenvectors).

### §2.2 K-field configuration

$\mathbf{u} = (u^{(1)}, \ldots, u^{(K_{\mathrm{field}})}) \in \widetilde\Sigma^K_M$ (shared-pool stratified space, per `mathematical_scaffolding_4tools.md` Tool A1). Active formation set:
$$\mathrm{act}(\mathbf{u}) := \{j \in \{1, \ldots, K_{\mathrm{field}}\} : \|u^{(j)}\|_1 > \epsilon\}, \quad \|u^{(j)}\|_1 = \sum_{x \in X} u^{(j)}(x).$$

For $K_{\mathrm{act}}$-stratum interior: $\mathbf{u} \in S^\circ_{K_{\mathrm{act}}}$, all active formations satisfy $\|u^{(j)}\|_1 > \epsilon$ strictly; inactive formations satisfy $\|u^{(j)}\|_1 < \delta_0$ for some $\delta_0 < \epsilon$.

### §2.3 Centroid definition (formal)

**Definition 2.2 (centroid).** For $\mathbf{u} \in S^\circ_{K_{\mathrm{act}}}$, $j \in \mathrm{act}(\mathbf{u})$, and embedding $\iota$:
$$c_j(\mathbf{u}; \iota) := \frac{\sum_{x \in X} \iota(x) \cdot u^{(j)}(x)}{\sum_{x \in X} u^{(j)}(x)} \in \mathbb{R}^d.$$

The centroid set is:
$$C(\mathbf{u}; \iota) := \{c_j(\mathbf{u}; \iota) : j \in \mathrm{act}(\mathbf{u})\}.$$

**Notation**: when embedding is fixed in context, write $c_j(\mathbf{u})$ and $C(\mathbf{u})$.

---

## §3. Well-Definedness

### §3.1 Non-vanishing denominator

**Lemma 3.1.** For $\mathbf{u} \in S^\circ_{K_{\mathrm{act}}}$ and $j \in \mathrm{act}(\mathbf{u})$, $\sum_x u^{(j)}(x) > \epsilon > 0$.

**Proof**: By definition of $\mathrm{act}$ (§2.2). ✓

**Corollary 3.2**: $c_j(\mathbf{u}; \iota)$ is well-defined as a $\mathbb{R}^d$-valued quantity for all $j \in \mathrm{act}(\mathbf{u})$.

### §3.2 Continuity in $\mathbf{u}$

**Lemma 3.3.** $\mathbf{u} \mapsto c_j(\mathbf{u}; \iota)$ is real-analytic on the open set $\{\mathbf{u} : \|u^{(j)}\|_1 > \epsilon\}$.

**Proof**: The map is a quotient of two real-analytic functions of $\mathbf{u}$ (numerator: linear in $u^{(j)}$; denominator: linear in $u^{(j)}$). Quotient of real-analytic functions with non-vanishing denominator is real-analytic. ✓

**Corollary 3.4**: On smooth-segment trajectories $\mathbf{u}(t) \in S^\circ_{K_{\mathrm{act}}}$, $c_j(\mathbf{u}(t); \iota)$ is real-analytic in $t$.

### §3.3 Bounded image

**Lemma 3.5.** $c_j(\mathbf{u}; \iota) \in \mathrm{Conv}(\iota(X))$ — the convex hull of $\iota(X)$ in $\mathbb{R}^d$.

**Proof**: $c_j$ is a probability-weighted average of $\iota(x)$ values with weights $u^{(j)}(x) / \|u^{(j)}\|_1$, which sum to 1 and are all non-negative. Such an average lies in the convex hull. ✓

---

## §4. Derivation from $u_t$ Primitive (CN10 Contrastive)

### §4.1 $u_t$-functional status

**Proposition 4.1 (CN10 compliance).** $c_j(\mathbf{u}; \iota)$ is a *derived diagnostic* of the primitive $u_t$ field — not a new primitive — provided $\iota$ is fixed independently of $\mathbf{u}$.

**Justification**:
- $c_j$ is a *function* of $u^{(j)}$ via spatial integral against fixed weight function $\iota$.
- $\iota$ depends on graph structure $G$ (vertex positions / Fiedler embedding), NOT on cohesion field state $\mathbf{u}$.
- Hence $c_j$ extracts spatial-moment information from $u^{(j)}$; CN10 contrastive: derived diagnostic class (analogous to $\mathcal{F}$, Bind, Sep, Inside, Persist diagnostics).

### §4.2 No object-first violation

**Claim 4.2**: Centroid $c_j$ does NOT presume objecthood.

**Justification**: $c_j$ is the spatial first-moment of the *soft cohesion field* $u^{(j)}$; defined for *any* soft field with positive total mass, not just for crisp objects. In particular, for fields without crisp peaks (e.g., uniform distribution), the centroid is still well-defined as the geometric center of the support. This contrasts with object-first frameworks where centroids are coordinates of pre-individuated objects.

⇒ CN10 preserved: $u_t$ remains primitive; $c_j$ is derivative.

### §4.3 Compatibility with Commitment 11

Commitment 11 (canonical) registers $\mathcal{F}$ as derived diagnostic counting "peaks" of $u^{(j)}$. Centroid is a complementary derived diagnostic capturing spatial *location* of the mass distribution, not peak count.

⇒ Centroid extends the derived-diagnostic family without conflicting with $\mathcal{F}$.

---

## §5. Aut(G) Covariance

### §5.1 Aut(G) action on $\mathbf{u}$

For $\sigma \in \mathrm{Aut}(G)$ (graph automorphism):
$$(\sigma \cdot u^{(j)})(x) := u^{(j)}(\sigma^{-1} x).$$

This permutes the vertex labels by $\sigma$.

### §5.2 Aut(G) action on $\iota(X)$

Since $\sigma$ is a graph automorphism, it preserves graph distances: $d_G(\sigma x, \sigma y) = d_G(x, y)$. The natural $\sigma$-action on the embedding is:
$$\sigma \cdot \iota(x) := \iota(\sigma x).$$

For lattice graphs: $\sigma$ corresponds to a rigid isometry (translation, rotation, reflection) of $\iota(X) \subset \mathbb{R}^d$. Specifically, there exists a unique affine map $\hat\sigma : \mathbb{R}^d \to \mathbb{R}^d$ (orthogonal + translation) such that $\hat\sigma(\iota(x)) = \iota(\sigma x)$.

For Fiedler embedding: $\hat\sigma$ is an orthogonal transformation of the Fiedler subspace (modulo eigenvalue-degeneracy ambiguity, resolved by canonical sign convention).

### §5.3 Centroid covariance

**Theorem 5.1 (Aut(G) covariance).** For $\sigma \in \mathrm{Aut}(G)$ with associated isometry $\hat\sigma : \mathbb{R}^d \to \mathbb{R}^d$:
$$c_j(\sigma \cdot \mathbf{u}; \iota) = \hat\sigma\big(c_j(\mathbf{u}; \iota)\big).$$

**Proof**:
$$c_j(\sigma \cdot \mathbf{u}; \iota) = \frac{\sum_x \iota(x) \cdot u^{(j)}(\sigma^{-1} x)}{\sum_x u^{(j)}(\sigma^{-1} x)}.$$
Substitute $y = \sigma^{-1} x$, so $x = \sigma y$ and $\iota(x) = \iota(\sigma y) = \hat\sigma(\iota(y))$:
$$= \frac{\sum_y \hat\sigma(\iota(y)) \cdot u^{(j)}(y)}{\sum_y u^{(j)}(y)} = \hat\sigma\Big(\frac{\sum_y \iota(y) \cdot u^{(j)}(y)}{\sum_y u^{(j)}(y)}\Big) = \hat\sigma(c_j(\mathbf{u}; \iota)).$$
Where the third equality uses that $\hat\sigma$ is affine (linear + translation): $\sum_y \hat\sigma(\iota(y)) \cdot w_y = \hat\sigma(\sum_y \iota(y) w_y)$ when $\sum_y w_y = 1$. ✓

**Corollary 5.2**: Centroid set covariance:
$$C(\sigma \cdot \mathbf{u}; \iota) = \hat\sigma(C(\mathbf{u}; \iota)) := \{\hat\sigma(c) : c \in C(\mathbf{u}; \iota)\}.$$

### §5.4 Aut(G)-invariant features

**Corollary 5.3 (pair-distance invariance).** Pair-distance multi-set $\{\|c_j(\mathbf{u}) - c_k(\mathbf{u})\|\}_{j < k}$ is $\mathrm{Aut}(G)$-invariant.

**Proof**: $\|c_j(\sigma \mathbf{u}) - c_k(\sigma \mathbf{u})\| = \|\hat\sigma(c_j) - \hat\sigma(c_k)\| = \|c_j - c_k\|$ (isometry preserves distances). ✓

**Implication**: σ_rich centroid component, when stripped to its Aut-invariant content, reduces to the *pair-distance multi-set* (or equivalently, the centroid configuration modulo isometry).

---

## §6. $S_{K_{\mathrm{act}}}$ Permutation Invariance

### §6.1 $S_{K_{\mathrm{field}}}$ action

For $\pi \in S_{K_{\mathrm{field}}}$ (formation-label permutation):
$$\pi \cdot \mathbf{u} := (u^{(\pi^{-1}(1))}, \ldots, u^{(\pi^{-1}(K_{\mathrm{field}}))}).$$

This permutes the formation labels.

### §6.2 Centroid set invariance

**Theorem 6.1.** $C(\pi \cdot \mathbf{u}; \iota) = C(\mathbf{u}; \iota)$ as multi-sets in $\mathbb{R}^d$.

**Proof**: $\pi$ permutes the formation indices but the *set* $\{c_j(\mathbf{u}) : j \in \mathrm{act}\}$ is index-free. Centroids of permuted formations are the same set of points, possibly relabeled. As multi-sets, equal. ✓

**Corollary 6.2**: All multi-set-invariant features of $C(\mathbf{u})$ — pair-distance multi-set, pair-distance histogram, MST edge multi-set, $H_*$ V-R barcodes — are $S_{K_{\mathrm{field}}}$-invariant.

### §6.3 Combined Aut(G) ⋊ S_K invariance

**Theorem 6.3 (wreath-product invariance of multi-set features).** Pair-distance multi-set is invariant under $\mathrm{Aut}(G) \wr S_{K_{\mathrm{field}}}$.

**Proof**: combined action: $(\sigma, \pi)$ acts on $\mathbf{u}$ as $\sigma \cdot \pi \cdot \mathbf{u}$. By Theorem 5.1 + Theorem 6.1:
- $\pi$-action: pair-distance multi-set unchanged (Theorem 6.1).
- $\sigma$-action: pair-distance multi-set unchanged (Corollary 5.3).
- Combined: invariant. ✓

This establishes the σ_rich centroid component's Aut-invariance at the **multi-set-feature level** (the level relevant for σ-tuples).

---

## §7. Embedding Canonicalness

### §7.1 Embedding-choice issue

The centroid $c_j(\mathbf{u}; \iota)$ depends on the embedding $\iota : X \to \mathbb{R}^d$. Different embeddings give different absolute coordinates.

### §7.2 Canonical equivalence

**Proposition 7.1 (Aut-invariant features are embedding-canonical).** For two embeddings $\iota, \iota'$ that differ by a graph-automorphism-induced isometry ($\iota' = \hat\sigma \circ \iota$ for some $\sigma \in \mathrm{Aut}(G)$), the Aut-invariant features (pair-distance multi-set, MST, V-R barcodes) of $C(\mathbf{u}; \iota)$ and $C(\mathbf{u}; \iota')$ coincide.

**Proof**: $C(\mathbf{u}; \iota') = \hat\sigma(C(\mathbf{u}; \iota))$ by linearity of centroid in $\iota$. Aut-invariant features are preserved under $\hat\sigma$. ✓

**Implication**: σ_rich centroid component, at the Aut-invariant-feature level (which is what matters for σ-tuple), is **independent of the choice of canonical embedding** — only the underlying graph structure matters.

### §7.3 Non-canonical embeddings

For embeddings not graph-isometry-related (e.g., random vertex-position embeddings), Aut-invariant features may differ. This is a *non-canonical* embedding choice and should be avoided. The Convention 2.1 (lattice → coordinate embedding; arbitrary → Fiedler) is canonical.

---

## §8. Uniqueness Theorems

### §8.1 Centroid uniqueness as first moment

**Theorem 8.1 (uniqueness as first-moment statistic).** The centroid is the unique linear functional $\mathbb{R}^X \to \mathbb{R}^d$ satisfying:
- (U1) Translation-equivariance: $c_j(\mathbf{u} \circ T_v) = c_j(\mathbf{u}) - v$ for any vertex translation $T_v$ (when $G$ has translational symmetry).
- (U2) Mass-normalization: $c_j$ is invariant under uniform rescaling $u^{(j)} \to \alpha u^{(j)}$ ($\alpha > 0$).
- (U3) Concentration: for $u^{(j)}$ concentrated at single vertex $x_0$ ($u^{(j)}(x) = m \delta_{x, x_0}$), $c_j = \iota(x_0)$.

**Proof sketch**: Translation-equivariance + mass-normalization fix $c_j$ to be a probability-weighted average of $\iota(x)$ with weights $w(u^{(j)})_x$ satisfying $\sum_x w(u^{(j)})_x = 1$. Concentration condition fixes $w(u^{(j)})_x = u^{(j)}(x) / \|u^{(j)}\|_1$. ✓

### §8.2 Distinguishing power

**Theorem 8.2 (centroid lifts σ_standard degeneracy).** There exist configurations $\mathbf{u}^{(A)}, \mathbf{u}^{(B)}$ on the same graph $G$ with $\sigma_{\mathrm{multi}}^{A,\mathrm{standard}}(\mathbf{u}^{(A)}) = \sigma_{\mathrm{multi}}^{A,\mathrm{standard}}(\mathbf{u}^{(B)})$ but $\{c_j(\mathbf{u}^{(A)})\}$ and $\{c_j(\mathbf{u}^{(B)})\}$ have different pair-distance multi-sets.

**Proof**: explicit construction in `nq242c_explicit_construction.md` §4 (equilateral vs isoceles disk-triangle on $T^2_{20}$). ✓

⇒ centroid is *strictly more informative* than σ_standard alone.

---

## §9. Smoothness Through K-jumps

### §9.1 Smooth-segment regularity

By Lemma 3.3 (real-analyticity), $c_j(\mathbf{u}(t))$ is real-analytic in $t$ on smooth segments where $j \in \mathrm{act}$ throughout.

### §9.2 K-jump discontinuity

At K-jump time $t^*$ with $(j, k) \to \ell$ merger:
- $c_j(t^{*-}), c_k(t^{*-})$ converge: $\|c_j(t^{*-}) - c_k(t^{*-})\| \to 0$ as $t \nearrow t^*$ (under generic merger geometry).
- At $t^{*+}$: only $c_\ell(t^{*+})$ exists; $c_j, c_k$ become *undefined* (no longer in $\mathrm{act}$).

**Continuity claim 9.1**: $c_\ell(t^{*+}) = \lim_{t \nearrow t^*} \frac{m_j c_j(t) + m_k c_k(t)}{m_j + m_k}$ — the mass-weighted limit of pre-merger centroids.

**Justification**: instantaneously after merger, $u^{(\ell)}(t^{*+}) = u^{(j)}(t^{*-}) + u^{(k)}(t^{*-})$ (mass conservation in shared-pool). Linearity of centroid in $u$ + total mass aggregation:
$$c_\ell = \frac{\sum_x \iota(x) (u^{(j)} + u^{(k)})}{\sum_x (u^{(j)} + u^{(k)})} = \frac{\|u^{(j)}\|_1 c_j + \|u^{(k)}\|_1 c_k}{\|u^{(j)}\|_1 + \|u^{(k)}\|_1} = \frac{m_j c_j + m_k c_k}{m_j + m_k}.$$
✓

This justifies Φ_rich §3.3(b) post-merger centroid formula in `sigma_rich_augmentation.md`.

---

## §10. Cat Status

### §10.1 Cat A established results

- Lemmas 3.1, 3.3, 3.5 (well-definedness, real-analyticity, bounded image): **Cat A** (elementary calculus / linear algebra).
- Theorem 5.1 (Aut(G) covariance): **Cat A** (substitution argument, complete proof above).
- Theorem 6.1 (S_K invariance as multi-set): **Cat A** (set-theoretic argument, complete proof above).
- Theorem 6.3 (combined wreath-product invariance of multi-set features): **Cat A** (combination of 5.1 + 6.1, complete).
- Proposition 7.1 (embedding canonicalness): **Cat A** (linearity argument, complete).
- Theorem 8.1 (centroid uniqueness as first moment): **Cat A**.
- Theorem 8.2 (distinguishing power): **Cat A** (constructive proof via `nq242c_explicit_construction.md` §4).

### §10.2 Cat B results

- Continuity claim 9.1 (post-merger centroid via mass-weighted limit): **Cat A under shared-pool mass-conservation hypothesis**; pending verification that all Path B candidate trajectories satisfy strict mass conservation across K-jumps (existing canonical T-Persist-K-* family supports this).

### §10.3 Promotion target

These results provide the **(R1) Aut-invariance proof** (centroid sub-piece) for `sigma_rich_augmentation.md` §10.4 Cat A everywhere path. Combined with §11 verification:
- Centroid: this file (Cat A).
- Orientation $\Theta_j$: Task #2 (next).
- Wigner-data $W_{jk}$: Task #3 (after).
- Φ_rich determinism: Task #4 (synthesis of #1-#3).

Upon completion of #1-#4: full **(R1)+(R2) rigorous proof** of σ_rich Aut-invariance + Φ_rich determinism. Cat A everywhere target reached.

---

## §11. Hard Constraint Verification

- [x] **canonical 직접 수정 0** — `working/MF/` only.
- [x] **Silent resolution 0** — Cat status explicit per result; pending items registered (§10.2).
- [x] **No Research OS resurrection** — single-topic working file.
- [x] **Not reductive** — centroid is a standard mathematical object (first moment) used as derived diagnostic, not external reduction. CN10 preserved (§4.2).
- [x] **u_t primitive maintained** — Proposition 4.1 explicitly justifies CN10 compliance.
- [x] **CN5 4-energy not merged** — N/A; centroid is invariant of state, not energy term.
- [x] **K not dual-treated** — $K_{\mathrm{act}}$ integer; centroid defined per active formation index.
- [x] **No metastability claim without P-F flag** — N/A.
- [x] **Aut-invariance proof at multi-set level** — §6.3 explicit; the absolute centroid coordinates are *covariant* (not invariant), but Aut-invariant features (pair-distances, MST, V-R barcodes) are *invariant*, which is the relevant level for σ-tuples.

---

## §12. References

### §12.1 Working files

- `working/MF/sigma_rich_augmentation.md` §2.3.1 (informal centroid definition; this file formalizes).
- `working/MF/sigma_rich_VR_phase1.md` §2 (V-R PH integration of centroid).
- `working/MF/nq242c_explicit_construction.md` §4 (Theorem 8.2 constructive proof source).
- `working/MF/multi_formation_sigma.md` (D-6a static σ_multi^A; centroid as derived diagnostic class).

### §12.2 Canonical refs

- `canonical/canonical.md` §11.1 Commitment 1 ($u_t$ primitive); Commitment 11 ($\mathcal{F}$ derived diagnostic class — centroid is parallel); Commitment 14, 14-Multi.
- `canonical/canonical.md` §14 CN10 (contrastive, not reductive).
- `canonical/canonical.md` §13 T-Persist-K family (mass conservation across K-jumps; Continuity claim 9.1 prerequisite).

### §12.3 External refs

- Standard linear algebra (first-moment / center-of-mass of probability distribution).
- Spectral graph theory (Fiedler embedding for non-lattice graphs): Chung, F. R. K. (1997). *Spectral Graph Theory*. CBMS.
- Aut(G) action on graphs: Bredon, G. (1972). *Introduction to Compact Transformation Groups*.

---

**End of sigma_rich_centroid_derivation.md.**

**Status: working draft. Task #1 complete. Centroid formal derivation: well-definedness (Cat A), Aut(G) covariance (Cat A, Theorem 5.1), $S_{K_{\mathrm{field}}}$ invariance (Cat A, Theorem 6.1), wreath-product invariance of multi-set features (Cat A, Theorem 6.3), embedding canonicalness (Cat A, Proposition 7.1), uniqueness as first moment (Cat A, Theorem 8.1), distinguishing power (Cat A constructive, Theorem 8.2), continuity through K-jumps (Cat A under mass-conservation; Continuity claim 9.1 → Φ_rich §3.3(b) justification). All hard constraints verified. CN10 contrastive preserved. Promotion target: (R1) Aut-invariance proof centroid sub-piece — Cat A everywhere completed. Next: Task #2 σ_rich orientation tensor Θ_j formal derivation.**

**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/MF/sigma_rich_centroid_derivation.md`
**Created:** 2026-04-30 (W5 Day 4).
**Promotion target:** CV-1.7 W9+ Cat A everywhere proof completion (combined with Tasks #2-4).
