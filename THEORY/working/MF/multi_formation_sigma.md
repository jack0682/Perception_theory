# multi_formation_sigma.md — Multi-Formation σ Phase 5 Initiation

**Status:** working draft (Phase 5 *initiation*, not closure).
**Created:** 2026-04-28 (W5 Day 2 MODERATE Block 3, G3 P1 opening).
**Author origin:** `THEORY/logs/daily/2026-04-28/04_G3_phase5_MO1_decision.md` (decision rationale); `working/MF/from_single.md` (predecessor MF context, R22-retracted §2).
**Canonical refs:** §11.1 Commitment 14 (single-formation σ); §13 T-σ-Lemma-1/2/3 + T-σ-Theorem-3/4 (single-formation σ supporting structures); §13 T-Persist-K-Sep / T-Persist-K-Weak (K-field architecture on $\Sigma^K_M$); §11 I9 K-field paradigm.
**Working refs:** `working/SF/from_single.md` (multi-formation derived view, §2 retracted); `working/SF/step_cohesion.md` (R22 reformulation); `2026-04-27/92_critical_review_round2.md` Issue R (forward gaps register includes multi-formation σ).
**Open problems referenced:** MO-1 (canonical OP-0003, "SIDESTEPPED" for single-formation, **returns active for multi-formation σ**); F-1 (OP-0001, K=2 vacuity SPLIT-RESOLVED single-formation but multi-formation reopens questions); N-1 (working/CE/`open_problems_reframing_2026-04-19.md` — Soft-Hard Switching Asymmetry).

---

## §1. Question and Scope

### 1.1 Target

Define a **multi-formation σ-tuple** $\sigma_{\text{multi}}(\mathbf{u})$ for K-field minimizers $\mathbf{u} = (u^{(1)}, \ldots, u^{(K)})$ on $\Sigma^K_M = \Sigma_{m_1} \times \cdots \times \Sigma_{m_K}$ (canonical §11 I9), extending the single-formation σ (Commitment 14) by:

1. **Per-formation σ_j** — single-formation σ-tuple of each $u^{(j)}$ in isolation.
2. **Inter-formation σ_jk** — pair-wise cross-formation σ data (joint Hessian off-diagonal blocks; coupling-induced eigenvalue shifts).
3. **Combined σ_multi** — total invariant capturing the K-formation Aut-orbit equivalence class.

### 1.2 Why now (W5 G3 P1)

- W4 closed single-formation σ (Lemma 1/2/3 + Theorem 3/4 W5 Day 1 G0 canonical-merged).
- T-Persist-K family (canonical §12-§13) provides joint-Hessian structure on $\Sigma^K_M$ (Coupling Bound Lemma; Weyl spectral gap bound) — the analytical scaffolding for multi-formation Hessian analysis is in place.
- V5b-F mechanism (NQ-173 deferred Day 3+) — if Branch B verdict (~70% a priori) confirms bulk-localized translation Goldstone, the same mechanism transfers to inter-formation analog (each formation's bulk Goldstone, modified by the *other* formations' presence — cross-cutting synergy noted in `2026-04-27/03_v5b_f_status_update.md` §4).

### 1.3 Out of scope (this initiation)

- Closed-form proof of σ_multi well-definedness on $\Sigma^K_M$ corners (where one or more $u^{(j)}$ has saturated values 0 or 1) — this re-engages MO-1, separately handled in §6 + companion file `04_G3_phase5_MO1_decision.md`.
- Numerical K=2 baseline measurement on real graphs — Day 3 morning per script skeleton `g3_baseline_k2_sigma.py`.
- Multi-formation σ uniqueness theorem (NQ-188, Round-2 spawn 2026-04-27).
- σ-stability under K-jumps (NQ-186 placeholder).

### 1.4 Vocabulary

- **K**: number of distinct soft formations in K-field architecture. Always integer ≥ 1 in this file (per N-1 commitment to integer K — see §6.1).
- **Joint manifold**: $\Sigma^K_M := \Sigma_{m_1} \times \cdots \times \Sigma_{m_K}$ where $\Sigma_{m_j} = \{u \in [0,1]^n : \sum_i u_i = m_j\}$.
- **Joint Hessian**: $H_{\text{joint}}(\mathbf{u})$ on $T_{\mathbf{u}} \Sigma^K_M$, block structure $\{H_{jk}\}_{j,k=1}^K$ where $H_{jj}$ is per-formation Hessian (canonical T-Persist-K-Sep) and $H_{jk}$ is coupling block (proportional to $\lambda_{\text{rep}} I$ on isoperimetrically-separated regime per Coupling Bound Lemma).
- **Joint stabilizer**: $G_{\mathbf{u}} := \mathrm{Stab}_{\mathrm{Aut}(G) \wr S_K}(\mathbf{u})$ — the symmetry group is wreath-product of graph automorphisms with formation-permutation $S_K$ when formations are distinguishable, or a quotient when they are interchangeable.

---

## §2. Restatement (meta-prompt §4.1)

### 2.1 What is asked

Given a K-formation minimizer $\mathbf{u}^* = (u^{(1)*}, \ldots, u^{(K)*})$ of the joint K-field energy $\mathcal{E}_K = \sum_k \mathcal{E}(u^{(k)}) + \sum_{j < k} \lambda_{\text{rep}} \langle u^{(j)}, u^{(k)} \rangle$ on $\Sigma^K_M$, define a discrete invariant $\sigma_{\text{multi}}(\mathbf{u}^*)$ that:

(a) **Generalizes Commitment 14** — recovers single-formation σ when $K = 1$ (trivially) or when formations are well-separated and decoupled (block-diagonal joint Hessian limit).

(b) **Is well-defined as Aut-orbit invariant** — invariant under the wreath-product symmetry $\mathrm{Aut}(G) \wr S_K$ acting on $\mathbf{u}^*$ (graph automorphism on each formation; $S_K$ permutation across formations when formations are interchangeable).

(c) **Captures cross-formation data** — the σ-tuple includes information about coupling blocks $H_{jk}$ that single-formation σ cannot capture.

(d) **Refines as $K \to 1$** — taking $K = 1$ should reduce to Commitment 14.

### 2.2 What is data

- Canonical Commitment 14 σ-framework (single-formation, line 768).
- T-Persist-K-Sep proof (canonical §13 line 854-894): joint Hessian structure with Coupling Bound Lemma; spectral gap bound $\mu_{\text{joint}} \geq \min_k \mu_k - (K-1)\lambda_{\text{rep}}$ via Weyl.
- T-Persist-K-Weak (canonical §13 line 896-907): when $\mu_{\text{joint}} \leq 0$, K → K-1 merge requires barrier crossing, not gradient descent.
- T-V5b-T Goldstone characterization on translation-invariant graphs (single-formation; canonical §13 line 1117-1167).
- V5b-F partial-Goldstone mechanism status (Cat C; mechanism Branch verdict deferred per `01_NQ173_v5b_f_verdict.md`).
- Lemma 1/2/3 + Theorem 3/4 σ-supporting structures (single-formation, canonical §13 W5 Day 1 G0 entries).

### 2.3 Success criteria

A σ_multi proposal is **successful** if:

(S1) Definition is **explicit** — σ_multi can be computed numerically given $\mathbf{u}^*$ and $G$.
(S2) Definition is **Aut-orbit-invariant** — proof for the wreath-product symmetry.
(S3) Definition reduces to **Commitment 14** when $K = 1$.
(S4) Definition is **non-trivial** in coupling — distinguishes K-field minimizers that have identical per-formation σ_j but different joint Hessian off-diagonal blocks.
(S5) Definition is **stable** under small perturbations in the well-separated regime (consistent with T-Persist-K-Sep).
(S6) Definition **handles MO-1** — well-defined on $\Sigma^K_M$ corners (or restricted to interior with explicit boundary handling).

A proposal is **failed** if:

(F1) Definition is non-canonical — depends on basis or coordinate choice (e.g., σ-tuple ordering changes under formation re-labeling).
(F2) Definition is **trivial** — only repeats single-formation σ_j (S4 fails).
(F3) Definition violates K=1 reduction (S3 fails).
(F4) Definition silently resolves MO-1 (forbidden per meta-prompt §8.2 + canonical CN5 spirit).

---

## §3. Multi-Approach Generation (meta-prompt §4.2)

Three structurally-independent approaches to defining σ_multi, with explicit failure modes and dependencies.

### 3.1 Approach A: Block-decomposition (per-formation σ + cross-formation σ_jk)

**Core idea**: Decompose joint Hessian $H_{\text{joint}}$ into diagonal blocks (per-formation $H_{jj}$) and off-diagonal blocks ($H_{jk}$, $j \neq k$). Apply single-formation σ-extraction to each $H_{jj}$ to get σ_j. Define a separate cross-block invariant σ_jk capturing the coupling.

**Mathematical setup**:

Let $H_{\text{joint}}(\mathbf{u}^*)$ act on $\bigoplus_j T_{u^{(j)*}} \Sigma_{m_j}$. The block structure:
$$
H_{\text{joint}} = \begin{pmatrix} H_{11} & H_{12} & \cdots & H_{1K} \\ H_{21} & H_{22} & \cdots & H_{2K} \\ \vdots & & \ddots & \\ H_{K1} & \cdots & & H_{KK} \end{pmatrix}.
$$

Per Coupling Bound Lemma (canonical T-Persist-K), in the well-separated regime $H_{jj} = H_{\text{single}}(u^{(j)*}) + O(\exp(-c_0 d_{\min}))$ and $H_{jk} = \lambda_{\text{rep}} I + O(\exp(-c_0 d_{\min}))$ for $j \neq k$.

**σ_j definition (per-formation)**: Apply Commitment 14 directly to $H_{jj}$. Get $\sigma_j = (\mathcal{F}_j; \{(n_{jk}, [\rho_{jk}], \lambda_{jk})\}_k)$ where the indices in the inner tuple now refer to single-formation $H_{jj}$ eigenvalues.

**σ_jk definition (cross-formation)**: For each pair $(j, k)$ with $j < k$, the coupling block $H_{jk}$ is (in the well-separated limit) $\lambda_{\text{rep}} I$. The σ_jk tuple captures:
- Coupling strength $\lambda_{\text{rep}}^{(jk)} := \|H_{jk}\|_{\text{op}}$ (operator norm of coupling block).
- Stabilizer-of-pair representation: under the action of $G_{\mathbf{u}}$, the pair $(u^{(j)}, u^{(k)})$ has a stabilizer $G_{\mathbf{u},jk}$ that may permute or fix the pair. The coupling block $H_{jk}$ transforms under $G_{\mathbf{u},jk}$ representations on $T_{u^{(j)*}} \Sigma_{m_j} \otimes T_{u^{(k)*}} \Sigma_{m_k}$ — define the irrep decomposition of this tensor space, get $[\rho_{jk}^{(p)}]$ multiset.
- Joint-block eigenvalue: smallest eigenvalue of the 2-block sub-Hessian $\begin{pmatrix} H_{jj} & H_{jk} \\ H_{kj} & H_{kk} \end{pmatrix}$ — this is the Weyl-bound-relevant quantity per T-Persist-K-Sep.

**Combined σ_multi(A)**:
$$\sigma_{\text{multi}}^{(A)}(\mathbf{u}^*) = \big(\mathcal{F}; \{\sigma_j\}_{j=1}^K; \{\sigma_{jk}\}_{j<k}\big).$$

**Aut-orbit invariance**: under $S_K$ permutation $\pi$, the multi-set $\{\sigma_j\}$ is invariant; the multi-set of pairs $\{\sigma_{jk}\}_{j<k}$ is invariant. Under $\mathrm{Aut}(G)$, each $\sigma_j$ inherits invariance from Commitment 14. Cross-block $\sigma_{jk}$ inherits via tensor-space irrep theory (representation theory of stabilizer-of-pair).

**Reduction to K=1**: trivial. With $K=1$ no $\sigma_{jk}$ exists; σ_multi^(A) = $(\mathcal{F}; \sigma_1)$ = single-formation σ.

**Non-triviality**: σ_jk encodes coupling-block data not present in $\sigma_j$ alone. Two K-fields with identical $\{\sigma_j\}_j$ but different $\lambda_{\text{rep}}^{(jk)}$ have different σ_multi(A).

**Failure modes**:
(M1) **Tensor-space irrep handling**: Under the *full* joint stabilizer $G_{\mathbf{u}}$ (which includes $S_K$ permutation when formations are interchangeable), σ_jk is not a per-pair invariant — pair labels (j, k) are permuted by $S_K$, and the σ_jk tuple must be canonically associated to *unordered pairs*, not ordered pairs. This is fixable via multi-set treatment, but adds complexity.
(M2) **Boundary handling**: At $\Sigma^K_M$ corners (some $u^{(j)}_i = 0$ or $= 1$), the diagonal blocks $H_{jj}$ may not be defined as Morse-Hessians (touching boundary). MO-1 issue. σ_j undefined at corners.
(M3) **Beyond well-separated**: Coupling Bound Lemma assumes $|O_{jk}| \leq 0.2 \cdot \min(|\text{Core}_j|, |\text{Core}_k|)$ (well-separated regime). For overlapping formations (T-Persist-K-Weak regime), the off-diagonal $H_{jk}$ is no longer $\lambda_{\text{rep}} I$ + exp-small correction; it can be a complex spatial pattern. σ_jk extraction becomes messy.

**Strengths**:
(P1) Most direct generalization of Commitment 14 — every single-formation σ_j is the Commitment 14 σ unchanged; cross-block σ_jk is new but conceptually parallel.
(P2) Compatible with all single-formation σ-supporting structures (Lemma 1/2/3, Theorem 3/4) without modification.
(P3) Computationally tractable: numerical procedure is "compute joint Hessian, slice into blocks, apply Commitment 14 per diagonal block, apply tensor-irrep-extraction per off-diagonal block".

**Estimated effort**: 2-3 weeks for full canonical-quality proof of (S1)-(S5); MO-1 (S6) deferred separately.

### 3.2 Approach B: Joint-Hessian global σ (treat $H_{\text{joint}}$ as one matrix)

**Core idea**: Don't decompose. Treat $H_{\text{joint}}$ as a single $(\sum_j n_j) \times (\sum_j n_j)$ matrix on the joint tangent space $T_{\mathbf{u}} \Sigma^K_M$. Apply Commitment 14 σ-extraction to this single matrix, with stabilizer being the joint $G_{\mathbf{u}} = \mathrm{Aut}(G) \wr S_K$ acting on the joint tangent space.

**Mathematical setup**:

Joint tangent space: $T_{\mathbf{u}} \Sigma^K_M = \bigoplus_j (\mathbf{1}_j^\perp)$ where $\mathbf{1}_j$ is the all-ones vector in the $j$-th block. Joint stabilizer $G_{\mathbf{u}}$ acts by:
- $\sigma \in \mathrm{Aut}(G)$ acts diagonally: $(\sigma \cdot v)_j = \sigma \cdot v_j$.
- $\pi \in S_K$ (when formations are interchangeable per F-1 / N-1 considerations): acts by block permutation $(\pi \cdot v)_j = v_{\pi^{-1}(j)}$.
- Combined: wreath product acts naturally.

Apply Commitment 14 directly: σ_multi(B) = $(\mathcal{F}_{\text{total}}; \{(n_k, [\rho_k], \lambda_k)\}_k)$ where:
- $\mathcal{F}_{\text{total}}$ is the *joint* local-maxima count of $\mathbf{u}$ — the simplex constraint $\sum_k u^{(k)}(x) \leq 1$ defines a "saturation set" of sites; $\mathcal{F}_{\text{total}}$ counts joint-maxima accounting for all K formations. Or simply $\sum_j \mathcal{F}_j$ if formations don't overlap. **Definition needs care.**
- $\lambda_k$ is the $k$-th eigenvalue of $H_{\text{joint}}$ (Bohr-style ordered).
- $[\rho_k]$ is the irrep of the $k$-th eigenvector under the wreath-product $G_{\mathbf{u}}$ representation. **This is the structurally new ingredient**: irreps of wreath products are well-studied (Specht 1935, James-Kerber 1981); they have a hierarchical structure $[\rho_k] = ([\rho_{\text{outer}}] \otimes \{[\rho_{\text{inner},j}]\}_j)$.
- $n_k$ is the Courant nodal count of the $k$-th joint eigenvector. **Definition needs care**: nodal domains on joint manifold $\Sigma^K_M$ are not the same as per-formation nodal domains. A single eigenvector $v = (v_1, \ldots, v_K) \in \bigoplus_j \mathbf{1}_j^\perp$ has "nodal" structure depending on whether one counts:
  - Per-formation nodal domains: $\sum_j \mathcal{N}(v_j)$.
  - Joint sign-pattern nodal domains: connected components of $\{(j, x) : v_j(x) > 0\}$ in the disjoint union $\bigsqcup_j G$.

**Combined σ_multi(B)**: $\sigma_{\text{multi}}^{(B)}(\mathbf{u}^*) = (\mathcal{F}_{\text{total}}; \{(n_k, [\rho_k], \lambda_k)\}_k)$.

**Reduction to K=1**: $G_{\mathbf{u}} = \mathrm{Aut}(G) \wr S_1 = \mathrm{Aut}(G)$ — recovers single-formation σ Commitment 14. Trivial.

**Non-triviality**: Distinct K-fields with identical per-formation σ_j but different cross-coupling produce different joint-Hessian eigenvalues / irreps, so σ_multi(B) distinguishes them. Stronger non-triviality than (A) because joint irreps capture coupling structure intrinsically.

**Aut-orbit invariance**: Inherited from Commitment 14 applied to wreath-product representation. Mathematically clean.

**Failure modes**:
(M1) **Wreath-product irrep machinery is heavy**: full machinery requires Specht modules / James-Kerber / classical wreath-product representation theory. For SCC paper exposition, this would be a substantial addition.
(M2) **Nodal definition ambiguity**: per-formation vs joint sign-pattern definitions are not equivalent; choice affects σ-tuple. Convention required.
(M3) **$\mathcal{F}_{\text{total}}$ definition under simplex constraint**: when supports overlap (T-Persist-K-Weak regime), $\mathcal{F}$ count requires careful handling of saturation.
(M4) **Block-diagonal limit not transparent**: in well-separated regime, σ_multi(B) should reduce to σ_multi(A) "{σ_j} multi-set"; verifying this is non-trivial because wreath-product irrep on joint tangent space ≠ direct-sum of per-formation irreps in general.

**Strengths**:
(P1) **Most canonical** — single application of Commitment 14, no separate diagonal/off-diagonal split.
(P2) **Captures all coupling**: any joint-Hessian eigenvalue / eigenvector contains coupling data.
(P3) **MO-1 status clearer**: Morse theory on $\Sigma^K_M$ as a single product manifold is a known stratified-Morse problem; by treating σ_multi(B) globally, the MO-1 question is "is σ_multi(B) well-defined on $\Sigma^K_M$ corners" — a single, focused question rather than per-block.

**Estimated effort**: 4-6 weeks (longer than A) — wreath-product irrep theory is heavy; nodal definition convention requires careful argument.

### 3.3 Approach C: Per-formation σ + interaction graph

**Core idea**: Extract per-formation σ_j unchanged (per Commitment 14, as in Approach A). Replace cross-block tensor-irrep machinery with a **discrete graph** on K vertices labeled by σ_j, with edges (j, k) labeled by a small number of scalar invariants of the coupling block.

**Mathematical setup**:

Define an **interaction graph** $\mathcal{I}(\mathbf{u}^*) = (V_{\mathcal{I}}, E_{\mathcal{I}})$ where:
- $V_{\mathcal{I}} = \{1, \ldots, K\}$, vertex $j$ labeled by single-formation σ_j (Commitment 14).
- $E_{\mathcal{I}} = \{(j, k) : j < k, \|H_{jk}\|_{\text{op}} > \theta_{\mathcal{I}}\}$ for a coupling-strength threshold $\theta_{\mathcal{I}}$.
- Each edge $(j, k)$ labeled by the **coupling fingerprint** $\phi_{jk} := (\|H_{jk}\|_{\text{op}}, \langle u^{(j)}, u^{(k)} \rangle / m_j m_k, d_{\min}(u^{(j)}, u^{(k)}))$ — coupling strength, normalized inner product, support distance.

**Combined σ_multi(C)**: $\sigma_{\text{multi}}^{(C)}(\mathbf{u}^*) = (\mathcal{F}, \mathcal{I}(\mathbf{u}^*))$ — the F count plus the labeled interaction graph.

**Aut-orbit invariance**: $\mathcal{I}$ is invariant under graph isomorphism by construction (vertex relabeling is via $S_K$, vertex labels σ_j are individually $\mathrm{Aut}(G)$-invariant by Commitment 14, edge labels are pair-invariants under $\mathrm{Aut}(G) \wr S_K$).

**Reduction to K=1**: $\mathcal{I}$ has 1 vertex labeled σ_1, no edges. σ_multi(C) = $(\mathcal{F}_1, \{\sigma_1\})$ — same as Commitment 14.

**Non-triviality**: edge-labels $\phi_{jk}$ distinguish coupling regimes.

**Threshold $\theta_{\mathcal{I}}$ choice**: this is the major subtlety. The threshold controls whether weakly-coupled formations are connected by an edge or not. Two natural choices:
- **Discrete threshold**: $\theta_{\mathcal{I}} = $ canonical constant (e.g., $\lambda_{\text{rep}} \cdot 0.5$). Defines a simple graph, clean but loses information for sub-threshold edges.
- **No threshold (full graph + edge weight)**: every $(j, k)$ pair has an edge labeled $\phi_{jk}$; threshold-free. Richer but no longer a sparse graph.

**Failure modes**:
(M1) **Threshold ambiguity** (per CN16 P-D unprincipled-threshold concern): no principled choice of $\theta_{\mathcal{I}}$.
(M2) **σ_multi(C) is not a tuple but a graph**: existing canonical Commitment 14 σ-tuple format is a *tuple*; introducing a *labeled graph* changes the σ-data structure. Either accept a structural change or insist on a tuple-encoding of $\mathcal{I}$ (e.g., adjacency-matrix flattening with canonical vertex ordering — but vertex ordering isn't canonical since σ_j multi-set).
(M3) **Edge-label fingerprint $\phi_{jk}$ is empirically motivated**: not a derived invariant from first principles. Three numbers (op-norm, inner product, support distance) chosen by intuition; would need justification.
(M4) **Boundary handling MO-1**: same as Approach A, σ_j on corners undefined.

**Strengths**:
(P1) **Simpler than wreath-product irreps** — uses single-formation σ + a discrete combinatorial structure.
(P2) **Visually intuitive** — σ_multi as a "decorated graph of formations" matches the cognitive picture of "K objects with relationships". Good for paper exposition.
(P3) **Computationally lightweight** — extracting interaction graph is O(K²) vs joint-Hessian-irrep is O((sum n)²).

**Estimated effort**: 1-2 weeks for definition + Aut-invariance proof + canonical proposal (lightest of three).

### 3.4 Independence Check (meta-prompt §5)

Are A / B / C **mathematically independent** in the sense required by meta-prompt §5?

**Test 1: Same idea in different notation?**
- A and B both end up needing "joint Hessian eigenvalue / irrep structure" in some form. **However**: A treats blocks separately + adds tensor-irrep on coupling block; B treats joint matrix uniformly. The mathematical objects are different: in A, σ_j uses $\mathrm{Aut}(G)$ irreps and σ_jk uses $\mathrm{Stab}_{\mathrm{Aut}(G) \wr S_K}(jk)$ tensor-irreps; in B, σ_multi(B) uses wreath-product irreps directly. Different irrep theories.
- C uses single-formation σ + a labeled-graph layer, no irrep theory beyond Commitment 14. Distinct from both A and B.

**Test 2: Different failure modes?**
- A fails on tensor-space irrep handling (M1 of A).
- B fails on wreath-product machinery weight (M1 of B) and nodal-definition ambiguity (M2 of B).
- C fails on threshold choice (M1 of C) and structural change to σ-data type (M2 of C).
- Failure modes are **non-overlapping**. ✓

**Test 3: Different success conditions?**
- A succeeds when Coupling Bound Lemma's well-separated assumption holds.
- B succeeds when wreath-product irrep machinery is digestible (paper-quality exposition).
- C succeeds when the threshold $\theta_{\mathcal{I}}$ can be principled-chosen.
- Different conditions. ✓

**Verdict**: A, B, C are mathematically independent approaches (per meta-prompt §5).

---

## §4. Primary Approach Selection (meta-prompt §4.3)

**Selection: Approach A (Block-decomposition).**

### 4.1 Rationale

Three criteria weigh:

1. **Continuity with single-formation σ-framework**:
   - A: each σ_j is the unmodified Commitment 14. Strongest continuity.
   - B: requires re-statement of Commitment 14 under wreath-product symmetry; partial continuity.
   - C: Commitment 14 unchanged at vertex labels; new combinatorial layer added. Continuous on the σ_j part, structurally different overall.

2. **Compatibility with V5b-F mechanism transfer**:
   - A: each σ_j is a single-formation Goldstone analysis; V5b-F mechanism (NQ-173 Branch verdict, Day 3+) applies per-formation. Cross-block σ_jk captures *inter-formation boundary effects* analogous to V5b-F's *single-formation boundary effects* — direct transfer per `2026-04-27/03_v5b_f_status_update.md` §4 cross-cutting synergy.
   - B: V5b-F analog is a global wreath-product property; transfer is less direct.
   - C: V5b-F analog goes into edge fingerprints $\phi_{jk}$; loses Goldstone-mode-level data.

3. **Effort budget for W5+ (single-week initiation)**:
   - A: 2-3 weeks for full proof (within W5 + W6 budget).
   - B: 4-6 weeks (outside reasonable initiation budget).
   - C: 1-2 weeks (most lightweight) but trades depth.

A maximizes (1) and (2); B is theoretically richer but computationally heavier; C is lightweight but loses Goldstone-mode-level detail.

**Decision**: Approach A is primary. B and C are preserved for follow-up:
- B as **W7+ deepening** (when wreath-product irrep machinery is needed for global σ-uniqueness theorem NQ-188).
- C as **paper §4 exposition layer** (graph-of-formations visualization is reader-friendly, useful for §4 Paper 1 Foundational SCC theory section).

### 4.2 Risks if A fails

- (M1 of A: tensor-space irrep handling): If the tensor-irrep extraction proves intractable, fall back to **A-light** — define σ_jk only via op-norm of $H_{jk}$ (a scalar, not an irrep), losing irrep-decomposition data on the coupling block. A-light is a hybrid of A (per-formation σ_j) + C (scalar coupling fingerprint).
- (M2 of A: corner handling MO-1): MO-1 is the W5 G3 P1 Decision 2 (Day 4 morning per W5_strategic_plan.md §0.4) — handled separately in `04_G3_phase5_MO1_decision.md`.
- (M3 of A: beyond well-separated regime): For strongly-overlapping formations (T-Persist-K-Weak regime), defer to W6+ — σ_multi(A) will be defined for well-separated formations only in the initial canonical entry; overlapping case is a known forward gap (NQ-188 / NQ-186 placeholder).

---

## §5. Approach A Substantive Development (meta-prompt §4.4)

### 5.1 Definition (formal)

**Definition 5.1 (σ_multi^(A) in well-separated regime)**. Let $\mathbf{u}^* \in \Sigma^K_M$ be a Morse-index-0 joint local minimum of $\mathcal{E}_K$ in the well-separated regime (per T-Persist-K-Sep hypotheses (H1-K), (WI), (SR), (NB-K), $\varepsilon$-gentle transition). Let $H_{\text{joint}}$ be the joint Hessian on $T_{\mathbf{u}^*} \Sigma^K_M$ with block decomposition $\{H_{jk}\}_{j,k=1}^K$. Define:

(a) **Per-formation σ_j**: For each $j \in \{1, \ldots, K\}$, let $\sigma_j := \sigma(u^{(j)*})$ via Commitment 14 applied to $H_{jj}$ on $T_{u^{(j)*}} \Sigma_{m_j}$ with stabilizer $G_{u^{(j)*}} = \mathrm{Stab}_{\mathrm{Aut}(G)}(u^{(j)*})$.

(b) **Cross-formation σ_jk**: For each ordered pair $(j, k)$ with $j < k$ and $\|H_{jk}\|_{\text{op}} > 0$, define the cross-block 2×2 sub-Hessian $\tilde H_{jk} := \begin{pmatrix} H_{jj} & H_{jk} \\ H_{kj} & H_{kk} \end{pmatrix}$ acting on $T_{u^{(j)*}} \Sigma_{m_j} \oplus T_{u^{(k)*}} \Sigma_{m_k}$.

Let $G_{\mathbf{u}^*, jk} := \mathrm{Stab}_{\mathrm{Aut}(G) \wr S_2}(u^{(j)*}, u^{(k)*})$ be the pair-stabilizer (treating $j, k$ as distinguishable indices but acted on by $S_2$ if $u^{(j)*}, u^{(k)*}$ are in the same $\mathrm{Aut}(G)$-orbit).

Define σ_jk-tuple via:
- **Cross-eigenvalue tuple**: $(\lambda_{jk}^{(p)})_{p=1}^{n_j + n_k}$ where $\lambda_{jk}^{(p)}$ are eigenvalues of $\tilde H_{jk}$ in increasing order.
- **Cross-irrep tuple**: $([\rho_{jk}^{(p)}])_{p}$ where $[\rho_{jk}^{(p)}]$ is the irrep of the $p$-th eigenvector of $\tilde H_{jk}$ under $G_{\mathbf{u}^*, jk}$ acting on the joint pair tangent space.
- **Cross-nodal tuple**: $(n_{jk}^{(p)})_p$ where $n_{jk}^{(p)}$ is the Courant nodal count of the $p$-th eigenvector restricted to *each* formation's component (definition: $n_{jk}^{(p)} := (\mathcal{N}(v_p|_j), \mathcal{N}(v_p|_k))$ — pair of integers, one per formation; total nodal "size" if scalarization needed).

$\sigma_{jk} := \big( \{(n_{jk}^{(p)}, [\rho_{jk}^{(p)}], \lambda_{jk}^{(p)})\}_p \big)$ — the multi-tuple of cross-eigenvalue triples.

(c) **Combined σ_multi^(A)**: Let
$$
\sigma_{\text{multi}}^{(A)}(\mathbf{u}^*) := \big( \mathcal{F}_{\text{total}}(\mathbf{u}^*); \{\sigma_j\}_{j=1}^K; \{\sigma_{jk}\}_{1 \leq j < k \leq K} \big),
$$
where $\mathcal{F}_{\text{total}} := \sum_j \mathcal{F}_j$ in the well-separated regime (formations don't overlap, joint $\mathcal{F}$ count is sum of per-formation counts).

**Convention (multi-set treatment under $S_K$)**: When formations are interchangeable under $S_K$, both $\{\sigma_j\}$ and $\{\sigma_{jk}\}$ are taken as multi-sets (unordered with multiplicity). This makes σ_multi^(A) invariant under $S_K$ permutation of formation labels.

### 5.2 Lemma 5.1 (σ_multi^(A) is well-defined in well-separated regime)

**Statement**: Under the hypotheses of Definition 5.1, σ_multi^(A) is well-defined and is invariant under $\mathrm{Aut}(G) \wr S_K$.

**Proof sketch (Cat B, jul not yet complete in this initiation)**:

*Step 1 (per-formation σ_j is well-defined and Aut(G)-orbit-invariant)*: By Commitment 14 + canonical T-σ-Lemma-1, σ_j is well-defined and invariant under $\mathrm{Aut}(G)$. Each $u^{(j)*}$ is a Morse-0 minimizer of the *single-formation* effective energy $\mathcal{E}_{\text{eff},j}$ on $\Sigma_{m_j}$ obtained by restricting $\mathcal{E}_K$ to fix $\{u^{(k)*}\}_{k \neq j}$. By T-Persist-K-Sep Coupling Bound Lemma, this restriction is $\mathcal{E}_{\text{single}}(u^{(j)}) + O(\exp(-c_0 d_{\min}))$, and Hessian $H_{jj}$ inherits the same decomposition. Thus σ_j extraction is Commitment 14 unchanged. ✓

*Step 2 (σ_jk is well-defined)*: The cross-block 2×2 sub-Hessian $\tilde H_{jk}$ is symmetric (by Hessian symmetry of $\mathcal{E}_K$), hence diagonalizable with real eigenvalues. By Coupling Bound Lemma in well-separated regime, $\|H_{jk}\|_{\text{op}} = \lambda_{\text{rep}} \cdot \|I\|_{\text{op}} + O(\exp(-c_0 d_{\min})) = \lambda_{\text{rep}} + O(\exp(-c_0 d_{\min}))$, finite. Spectrum of $\tilde H_{jk}$ has $n_j + n_k$ eigenvalues; ordering is canonical. ✓

*Step 3 (σ_jk is $G_{\mathbf{u}^*, jk}$-invariant)*: By Lemma 1 application to $\tilde H_{jk}$ with stabilizer $G_{\mathbf{u}^*, jk}$. Tensor-space irrep theory of subgroup $G_{\mathbf{u}^*, jk} \leq \mathrm{Aut}(G) \wr S_2$ gives well-defined irrep labels $[\rho_{jk}^{(p)}]$ of eigenvectors. ✓ *(This step has a subtle dependency on whether* $u^{(j)*}$ *and* $u^{(k)*}$ *are in the same* $\mathrm{Aut}(G)$*-orbit; if so, $S_2$ acts; if not, only the diagonal subgroup of $\mathrm{Aut}(G) \times \mathrm{Aut}(G)$ acts.)*

*Step 4 ($S_K$ permutation invariance)*: Under $\pi \in S_K$ permuting formation labels, $\{\sigma_j\}_{j=1}^K \to \{\sigma_{\pi^{-1}(j)}\}_{j=1}^K$ which is the same multi-set; similarly for $\{\sigma_{jk}\}_{j<k}$. ✓

*Step 5 (combined well-definedness)*: $\sigma_{\text{multi}}^{(A)} = (\mathcal{F}_{\text{total}}; \text{multi-set}_1; \text{multi-set}_2)$ where each piece is individually well-defined and invariant; tuple of three invariant pieces is invariant. ✓

**Status**: **sketched** (per meta-prompt §7 unclassified-uncertainty marker). Step 3 has the tensor-space irrep dependency which needs careful pair-orbit handling. **Cat B target** for full canonical-quality proof.

### 5.3 Lemma 5.2 (Reduction to single-formation when K=1)

**Statement**: When $K = 1$, $\sigma_{\text{multi}}^{(A)}(\mathbf{u}^*) = \sigma_{\text{single}}(u^{(1)*})$ per Commitment 14.

**Proof**: When $K = 1$:
- $\{\sigma_j\}_{j=1}^1 = \{\sigma_1\}$ — single per-formation σ.
- $\{\sigma_{jk}\}_{j < k} = \emptyset$ — no pair indices.
- $\mathcal{F}_{\text{total}} = \mathcal{F}_1$.

Hence $\sigma_{\text{multi}}^{(A)} = (\mathcal{F}_1; \{\sigma_1\}; \emptyset)$ which after extracting the single multi-set element equals $(\mathcal{F}_1; \sigma_1)$ — the Commitment 14 σ-tuple, modulo notation. ✓

**Status**: **proved** (Cat A — trivial verification).

### 5.4 Lemma 5.3 (Non-triviality: σ_multi^(A) distinguishes coupling)

**Statement**: There exist K-fields $\mathbf{u}^{(1)}, \mathbf{u}^{(2)}$ on the same graph $G$ with same per-formation $\{\sigma_j\}$ multi-set but different $\sigma_{\text{multi}}^{(A)}$ via differing $\sigma_{jk}$.

**Proof (constructive sketch)**:

Take $G = $ 2D torus $T^2_L$, $L = 20$. Two K=2 configurations:

**Config 1**: Two well-separated tanh-disk formations $u^{(1), (1)}, u^{(1), (2)}$ at distance $d_{\min}^{(1)} = 8$ from each other (well-separated regime, $|O_{12}| = 0$).

**Config 2**: Same per-formation profiles but at distance $d_{\min}^{(2)} = 5$ (still well-separated per WI assumption $|O| \leq 0.2 \min |\text{Core}|$, but tighter).

Each config has same per-formation σ_j (same single-disk minimizers, same individual $H_{jj}$ spectrum). But:

- $\|H_{12}^{(1)}\|_{\text{op}}$ vs $\|H_{12}^{(2)}\|_{\text{op}}$: per Coupling Bound Lemma, $\|H_{jk}\|_{\text{op}} \approx \lambda_{\text{rep}} \cdot \exp(-c_0 \cdot d_{\min})$ (heuristic; actual scaling per CBL Item 2-3). Different $d_{\min}$ → different op-norms.
- Cross-eigenvalues $\lambda_{12}^{(1, p)}$ vs $\lambda_{12}^{(2, p)}$: by Weyl interlacing applied to $\tilde H_{12} = \mathrm{block-diag}(H_{11}, H_{22}) + \begin{pmatrix} 0 & H_{12} \\ H_{21} & 0 \end{pmatrix}$, the perturbation magnitude $\|H_{12}\|$ shifts the joint eigenvalues by amount $O(\|H_{12}\|)$. Different $d_{\min}$ → different shifts → different $\sigma_{jk}$ tuples.

Hence $\sigma_{\text{multi}}^{(A)}(\mathbf{u}^{(1)}) \neq \sigma_{\text{multi}}^{(A)}(\mathbf{u}^{(2)})$ even though $\{\sigma_j\}$ multi-sets are identical. ✓

**Status**: **sketched** with explicit construction; actual numerical verification requires K=2 baseline script (G3 Day 3 morning per `g3_baseline_k2_sigma.py`). **Cat B target** post-numerical.

### 5.5 Goldstone analog on σ_multi^(A) (V5b-F transfer)

**Observation 5.4 (cross-formation Goldstone)**:

In the well-separated translation-invariant graph case (e.g., 2D torus), each per-formation $u^{(j)*}$ has its own translation Goldstone (canonical T-V5b-T-(b)). In the joint Hessian $\tilde H_{jk}$, these per-formation Goldstones are **two near-zero eigenvalues** (one per formation), shifted by coupling.

By Weyl perturbation theorem applied to $\tilde H_{jk} = \mathrm{block-diag}(H_{jj}, H_{kk}) + V_{jk}$ where $V_{jk}$ has off-diagonal coupling $H_{jk}$, the two near-zero eigenvalues split into two close-but-not-equal eigenvalues:
$$\lambda_{jk}^{(\text{Goldstone-pair})} \in \{\lambda_{\text{single},j}^{(\text{Goldstone})} \pm O(\|H_{jk}\|), \lambda_{\text{single},k}^{(\text{Goldstone})} \pm O(\|H_{jk}\|)\}.$$

The joint eigenvectors are linear combinations of per-formation translation modes plus boundary corrections.

This is the **multi-formation analog of V5b-F**: the per-formation Goldstones are *partially* preserved (each formation's translation-invariance is broken locally by the *other* formation's presence, just as in V5b-F where translation-invariance is broken locally by the boundary). The mechanism transfer (per Day 1 carry analysis in `2026-04-27/03_v5b_f_status_update.md` §4):
- V5b-F (single-formation, free BC): translation broken by graph boundary.
- Multi-formation analog: translation broken by *other-formation presence* on translation-invariant graph.

Both produce **partial Goldstones with bulk-localized character**. The H1 (bulk-localized) hypothesis from V5b-F transfers directly: each formation's Goldstone is a near-perfect translation in its bulk (far from the other formation), with mode mixing near the inter-formation boundary.

**Implication**: NQ-179 (W6+ candidate, registered in `2026-04-27/03_v5b_f_status_update.md` §5): **V5b-F mechanism transfer to multi-formation σ inter-formation gap**.

**Status**: **observed/sketched**. Quantitative confirmation requires K=2 baseline numerical (G3 Day 3+).

### 5.6 What this initiation does NOT establish (honest gap inventory)

To meet meta-prompt §7 rigor:

- **Approach A's M1 (tensor-space irrep handling on cross-block)**: §5.1(b) defines the cross-irrep tuple but the *full* representation theory on $T_{u^{(j)*}} \Sigma_{m_j} \oplus T_{u^{(k)*}} \Sigma_{m_k}$ under $G_{\mathbf{u}^*, jk}$ requires explicit decomposition of pair-tangent space. Two cases:
  - If $u^{(j)*}, u^{(k)*}$ are *in the same Aut(G)-orbit*: pair-stabilizer includes a $\mathbb{Z}_2$ swap; tangent-space decomposition involves induced/restricted irreps.
  - If *different orbits*: pair-stabilizer is direct product; tangent decomposition is direct sum of per-formation irrep restrictions.

  **Both cases need explicit treatment**; not done in this initiation. **Forward gap.**

- **Approach A's M3 (overlapping formations beyond well-separated regime)**: when $|O_{jk}| > 0.2 \min$, Coupling Bound Lemma's $H_{jk} \approx \lambda_{\text{rep}} I$ approximation fails; off-diagonal blocks become spatial patterns, not multiples of identity. σ_jk extraction needs different handling. **Forward gap (NQ-188 / NQ-186 territory).**

- **Approach A's M2 (MO-1 corners)**: σ_j undefined when $u^{(j)*}$ touches boundary; σ_jk inherits this issue. **Decision deferred to companion file `04_G3_phase5_MO1_decision.md`.**

- **σ_multi uniqueness**: NQ-188 (Round-2 spawn 2026-04-27) — how many distinct σ_multi-classes per parameter regime? Not addressed.

- **σ_multi crisp recovery (CN10 / Commitment 11 derivative-objecthood)**: NQ-189 — how does σ_multi → crisp-K + per-object structure? Not addressed.

- **σ_multi cascade**: how σ_multi changes as $\beta$ crosses bifurcation thresholds (Round-2 spawn NQ-186 placeholder). Not addressed.

These gaps are **registered explicitly** to comply with meta-prompt §8.2 (no silent resolution).

---

## §6. Open Questions Sharpened by This Initiation (meta-prompt §4.6)

This initiation generates new specific open questions:

### 6.1 OQ-A1: Pair-stabilizer tensor-irrep decomposition

For ordered pair $(j, k)$ with $u^{(j)*}, u^{(k)*}$ in same Aut(G)-orbit, what is the explicit irrep decomposition of $T_{u^{(j)*}} \Sigma_{m_j} \oplus T_{u^{(k)*}} \Sigma_{m_k}$ under $G_{\mathbf{u}^*, jk}$? Two subgroup cases ("same orbit" with $S_2$ swap; "different orbits" with diagonal Aut(G)). Frobenius reciprocity and induced-representation calculation needed.

### 6.2 OQ-A2: σ_jk eigenvalue exact splitting from $H_{jj}, H_{kk}, H_{jk}$

In the well-separated regime, $H_{jk} = \lambda_{\text{rep}} I + \text{exp-small}$. The exact splitting of $\tilde H_{jk}$'s eigenvalues from $H_{jj}, H_{kk}$ is captured by Bloch-Brillouin / Schur-complement / Weyl interlacing — which formulation gives the cleanest σ_jk closed form?

### 6.3 OQ-A3: $\mathcal{F}_{\text{total}}$ definition under simplex constraint

When $\sum_k u^{(k)}(x) \leq 1$ saturates (some sites have full simplex saturation), the joint local-maxima count $\mathcal{F}_{\text{total}}$ may not equal $\sum_j \mathcal{F}_j$. Definition refinement needed for T-Persist-K-Weak regime.

### 6.4 OQ-A4: Compatibility with V5b-F mechanism transfer (NQ-179 connection)

If NQ-173 Day 3 verdict produces Branch B for V5b-F (~70% a priori), the bulk-localized Goldstone mechanism transfers to multi-formation. **Question**: in σ_multi^(A) §5.5, does the cross-block σ_jk Goldstone-pair eigenvalue splitting *exactly* match the V5b-F H1 "bulk overlap > 0.95, full-space overlap 0.5-0.85" pattern? Or is the inter-formation case quantitatively different?

### 6.5 OQ-A5: σ_multi^(A) vs σ_multi^(B) reduction in well-separated regime

In well-separated regime, σ_multi^(A) (block decomposition) and σ_multi^(B) (joint Hessian + wreath irreps) should agree up to redundancy (B's joint eigenvalues = A's per-block eigenvalues + cross-block eigenvalues; B's wreath irreps = A's per-formation irreps + cross-tensor irreps modulo wreath structure). **Verifying this equivalence proof** is OQ-A5; would solidify A as the operational definition with B as "theoretically-equivalent rich version".

### 6.6 OQ-A6: σ_multi behavior at $S_K$ orbit boundaries

When two formations $u^{(j)*}, u^{(k)*}$ converge to coincidence ($u^{(j)*} = u^{(k)*}$), $S_K$ stabilizer enlarges (continuous transition from "trivially different" to "$S_2$-equivalent"). σ_multi^(A) should be **continuous** through this convergence. Is it? Continuity check for σ_multi^(A) against $u^{(j)*} \to u^{(k)*}$ limit.

### 6.7 New canonical/working entries flagged

If σ_multi^(A) reaches Cat B-target status:
- Canonical §13 candidate entry "T-σ_multi-A" (analog of T-σ-Lemma-1).
- Canonical §11.1 Commitment 14 candidate addendum: extension to multi-formation.
- Working file series: `working/MF/sigma_multi_lemma1.md`, `working/MF/sigma_multi_theorem3.md` etc., paralleling W4-04-24 single-formation σ supporting structures.

---

## §7. K=2 Baseline Numerical Plan (Day 3 morning carry-forward)

Per plan.md §3 Block 3 (15:30-16:00) — script skeleton drafted in `CODE/scripts/g3_baseline_k2_sigma.py`. Day 3 09:00 actual run target.

**Test setup** (subject to scc validation patch per `01_NQ173_v5b_f_verdict.md` §5 Option P2):
- Graph: 2D torus $T^2_{20}$ (translation-invariant; $\mathrm{Aut}(G) = \mathbb{Z}_{20}^2 \rtimes D_4$).
- K = 2; $m_1 = m_2 = 40$ (small per-formation; need patch for $c_j = 0.10$).
- Two well-separated tanh-disk ICs at distance $d \in \{5, 8, 12, 16\}$.
- $\beta = 4.0$ (super-lattice $\zeta = 0.5$).
- $\lambda_{\text{rep}} \in \{0.01, 0.1, 1.0\}$ (sweep coupling strength).

**Measurements**:
1. Per-formation σ_j (Commitment 14 applied to each $H_{jj}$).
2. Cross-block $H_{12}$ op-norm and lowest 6 cross-eigenvalues.
3. Cross-eigenvector: per-formation Goldstone overlap (test §5.5 V5b-F transfer claim).
4. K=2 vs K=1 isoperimetric energy comparison (at $\lambda_{\text{rep}} = 0$).

**Verdict criteria**:
- Lemma 5.3 non-triviality: do different $d_{\min}$ produce different $\sigma_{12}$? Expected YES.
- §5.5 cross-Goldstone transfer: do per-formation Goldstones split into Goldstone-pair? Expected YES with magnitude $\sim \|H_{12}\|$.
- σ_multi^(A) consistency: as $d_{\min}$ → ∞, $\|H_{12}\|$ → 0, σ_multi^(A) reduces to two decoupled σ_1, σ_2. Expected YES.

---

## §8. Hard Constraint Verification (meta-prompt §8 + canonical CN list)

- [x] **canonical 직접 수정 0** — this is `working/MF/`, not canonical/. No edit to canonical/.
- [x] **Silent resolution 0** — MO-1 explicitly DEFERRED to companion file `04_G3_phase5_MO1_decision.md`. F-1, M-1, OP-0001..OP-0007 not silently resolved. NQ-188, NQ-189, NQ-186 referenced as open.
- [x] **No Research OS resurrection** — no D-/S-/T-/A-/E-/Q-/C-/P-/X- registry, no 5-role daily logs, no numbered subdirs.
- [x] **Not reductive to external framework** — σ_multi^(A) is intrinsic SCC mathematics (CN10). Comparisons to wreath-product irrep theory (Approach B) are *contrastive* not reductive.
- [x] **u_t is primitive, objects are derivative** — all definitions operate on $u^{(j)} : X \to [0,1]$; $\mathcal{F}$ count is *derived* from $u^{(j)}$ (per Commitment 11). No "object-first" treatment.
- [x] **4 energy terms not merged** — $\mathcal{E}_K = \sum_k \mathcal{E}(u^{(k)}) + \lambda_{\text{rep}}$ inter-coupling preserves the 4-term structure per formation; rep-coupling is a *new* fifth term distinct from cl/sep/bd/tr.
- [x] **closure not assumed idempotent** — A3 contraction acknowledged; no idempotence claim.
- [x] **K not dual-treated** — K is integer throughout (per N-1 commitment, see §6.1 vocabulary). No "K continuous on optimization manifold + integer for counting" abuse.
- [x] **No metastability claim without P-F flag** — when discussing well-separated regime persistence (§5.1), this rests on canonical T-Persist-K-Sep which is itself a static (zero-T) Hessian result, not dynamic metastability.

  *However*: §5.5 V5b-F mechanism transfer to multi-formation Goldstone analog inherits the V5b-F metastability question from `01_NQ173_v5b_f_verdict.md` §6.4 (the entire static-Hessian σ-framework operates in metastable regime at zero T). **P-F flagged**: full thermodynamic / kinetic treatment of multi-formation persistence is open (P-F deepening for multi-formation case = NQ-191 + NQ-192 territory).

- [x] **No primitive K override** — K is the user-set count of fields in K-field architecture (canonical I9). σ_multi defines a discrete invariant FROM K-field minimizer state; doesn't redefine K.

---

## §9. Forward Roadmap (W6+)

### W6 (post-W5 close)
- OQ-A1 (pair-stabilizer tensor-irrep decomposition) — key technical step for σ_jk well-definedness Cat B → A.
- OQ-A5 (σ_multi^(A) vs σ_multi^(B) equivalence) — solidifies A as operational with B as theoretical.
- σ_multi^(A) canonical proposal text (W6 working/draft → W7 canonical merge if Cat B reached).

### W7-W8
- T-Persist-K-Weak regime extension (overlapping formations, per A's M3 forward gap).
- σ_multi cascade NQ-186 — how σ_multi changes across $\beta$ bifurcation thresholds.
- σ_multi uniqueness NQ-188 — count distinct σ_multi-classes per parameter regime.

### W9+
- Approach C (interaction graph) as paper §4 exposition layer.
- σ_multi → crisp-K recovery NQ-189.
- σ_multi topological invariance NQ-190.

### W12+
- Multi-formation σ-framework completion → Paper 1 §4.

---

## §10. Cross-References (single-source-of-truth pointers)

- Single-formation σ Commitment 14: `canonical.md` §11.1 line 768.
- Single-formation σ supporting structures: `canonical.md` §13 T-σ-Lemma-1/2/3 + T-σ-Theorem-3/4 (W5 Day 1 G0 entries).
- T-Persist-K family (joint Hessian structure): `canonical.md` §13 T-Persist-K-Sep / T-Persist-K-Weak (line 854-907).
- K-field architecture I9: `canonical.md` §11 + line 829.
- V5b-F mechanism (deferred Day 3+): `THEORY/logs/daily/2026-04-28/01_NQ173_v5b_f_verdict.md`.
- Cross-cutting V5b-F → multi-formation analog: `THEORY/logs/daily/2026-04-27/03_v5b_f_status_update.md` §4.
- Round-2 forward gaps register: `THEORY/logs/daily/2026-04-27/92_critical_review_round2.md` Issue R.
- MO-1 decision Option A/B/C: `THEORY/logs/daily/2026-04-28/04_G3_phase5_MO1_decision.md` (companion file).
- N-1 Soft-Hard Switching: `THEORY/working/open_problems_reframing_2026-04-19.md`.
- F-1 / M-1 / MO-1 status: `canonical.md` §12 + `open_problems.md` OP-0001/OP-0002/OP-0003.

---

**End of multi_formation_sigma.md (Phase 5 initiation).**
**Status: working draft. Approach A primary. K=1 reduction proved (Cat A); well-defined-in-well-separated sketched (Cat B target); non-triviality sketched (Cat B target); MO-1 DEFERRED. 6 OQs registered. Forward roadmap W6-W12.**
