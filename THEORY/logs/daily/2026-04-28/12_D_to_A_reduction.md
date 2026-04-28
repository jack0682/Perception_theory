# 12_D_to_A_reduction.md — σ_multi^(D) → σ_multi^(A) Reduction in Well-Separated Regime

**Session:** 2026-04-28 (W5 Day 2 Phase 3, E6).
**Target:** Formal proof of the claim in `06_approach_AB_equivalence_and_D.md` §3.5: "σ_multi^(D) reduces to (a refinement of) Commitment 14 / σ_multi^(A) when K=1 — and more generally, in the well-separated regime, D's information is determined by A's continuous data plus a discrete orbit-type label."
**Resolves:** Phase 3 weakness #6 (D → A claim was sketched without proof).
**Depends on reading:** `06_approach_AB_equivalence_and_D.md` §3 (Approach D framework); `10_sigma_multi_D_concrete.md` (concrete σ_multi^(D) computation); `08_lemma5_1_step3_proof.md` §2 (Frobenius reciprocity); `05_sigma_multi_concrete_T2_K2.md` §3-§5.
**Status:** **Cat C → Cat B target**. Proof for K=2 well-separated case; general K open.

---

## §1. Statement to Prove

**Theorem (D → A in well-separated regime, K=2)**: Let $\mathbf{u}^* \in \Sigma^{2, \circ}_{(m_1, m_2)}$ be a K=2 well-separated joint minimizer (T-Persist-K-Sep hypotheses). Let $\sigma_{\mathrm{multi}}^{(A)}(\mathbf{u}^*) = (\mathcal{F}; \{\sigma_1, \sigma_2\}; \sigma_{12})$ per Definition 5.1 of `working/MF/multi_formation_sigma.md`. Let $\sigma_{\mathrm{multi}}^{(D)}(\mathbf{u}^*) = [G_{\mathbf{u}^*, 12}]_{\mathrm{conj}}$ + cohomology data per `10_sigma_multi_D_concrete.md` §2-§3.

**Claim**: σ_multi^(D) is **determined** by σ_multi^(A) + a finite combinatorial label (the orbit-type conjugacy class), and conversely σ_multi^(A) determines σ_multi^(D) **up to** this finite combinatorial freedom.

**Equivalent statement**: σ_multi^(D) factors as
$$\sigma_{\mathrm{multi}}^{(D)} = (\text{orbit-type conjugacy class}) \otimes (\text{σ_multi^(A) per-orbit data}). \tag{1.1}$$

---

## §2. Proof Sketch

### 2.1 K=1 Reduction (Trivial)

For K=1, $\Gamma = \mathrm{Aut}(G) \wr S_1 = \mathrm{Aut}(G)$, no swap factor. σ_multi^(D) = orbit-type label = conjugacy class of $\mathrm{Stab}_{\mathrm{Aut}(G)}(u^*)$, plus its cohomology.

σ_multi^(A) for K=1 = Commitment 14 σ-tuple, which by canonical T-σ-Lemma-1 includes irrep labels $[\rho_k] \in \mathrm{Irr}(\mathrm{Stab}_G(u^*))$. The set of irreps $\mathrm{Irr}$ depends ONLY on the conjugacy class of the stabilizer (by Maschke).

So **D = A + ε** where ε is the orbit-type label (= conjugacy class of stabilizer), which is **encoded in** the irrep theory used by A.

For K=1 with single conjugacy class of stabilizer, σ_multi^(A) determines σ_multi^(D) **completely**: the orbit-type label is implicit in which Irr-set the σ_k are drawn from.

### 2.2 K=2 well-separated case

By `08_*` §2, the joint stabilizer is $G_{\mathbf{u}^*, 12} = D \wr S_2$ where $D \cong \mathrm{Stab}(u^{(j)*})$ (per-formation stabilizer, equal up to conjugation by canonical iso $\rho$).

σ_multi^(A) cross-block σ_jk uses irreps of $D \wr S_2$ in the permutation-module setting (per `08_*` §2.5).

σ_multi^(D) orbit-type = $[D \wr S_2]$ conjugacy class in $\Gamma = \mathrm{Aut}(G) \wr S_2$.

**Two pieces of information in D**:
- (D1) Conjugacy class of $D \wr S_2$ in $\Gamma$ — depends on:
  - Conjugacy class of $D$ in $\mathrm{Aut}(G)$ (per-formation stabilizer type).
  - "Position" of the swap involution $\rho \in \mathrm{Aut}(G)$ swapping the two formations.

- (D2) Cohomology data $H^*(B(D \wr S_2))$ — depends purely on **abstract group structure** of $D \wr S_2$, i.e., on $D$.

**A's contribution**:
- σ_j is per-formation, depends on $D$ (its irrep theory).
- σ_jk uses $D \wr S_2$ permutation-module irreps, depends on $D$ + structure of swap.

So **A includes**:
- $D$ structure (via σ_j irreps).
- Swap-related structure (via σ_jk irreps + Sym/Antisym splitting).

A does NOT directly include:
- (D1.b) "Position" of the swap involution as a specific element of $\mathrm{Aut}(G)$. Two configurations with same $D$ but different swap conjugates have same A but **different D**.

### 2.3 Counterexample (showing D contains MORE than A in some cases)

**Example**: $G = T^2_{20}$, K=2, with two configurations:
- Config X: disks at $(0, 0)$ and $(8, 0)$, swap $\rho_X = $ 180° rotation about $(4, 0)$.
- Config Y: disks at $(0, 0)$ and $(8, 0)$ same as X, but swap $\rho_Y = $ 180° rotation about $(4, 10)$.

For $\rho_X$: maps $(0,0) \to (8, 0)$, $(8, 0) \to (0, 0)$. ✓
For $\rho_Y$: maps $(0,0) \to (8, -20) = (8, 0) \mod 20$ ... wait, $(0,0) \to (8 - 0, 20 - 0) = (8, 20) \equiv (8, 0)$. ✓
And $(8, 0) \to (8 - 8, 20 - 0) = (0, 20) \equiv (0, 0)$. ✓

So both $\rho_X$ and $\rho_Y$ are valid swap involutions. Are they conjugate in $\Gamma$?

Conjugating $\rho_X$ by translation $T_{(0, k)}$ gives 180° rotation about $(4, k)$. So $\rho_X$ and $\rho_Y$ are conjugate by $T_{(0, 10)}$ → same conjugacy class.

Hmm so actually X and Y have the same orbit-type (after translation conjugation). Bad counterexample.

**Better counterexample**: 
- Config X: 2 disks at $(0, 0), (8, 0)$ on $T^2_{20}$.
- Config Y: 2 disks at $(0, 0), (10, 0)$ on $T^2_{20}$.

For Y, the swap involution would be 180° rotation about $(5, 0)$. Maps $(0,0) \to (10, 0)$ ✓ and $(10, 0) \to (0, 0)$ ✓. ✓

Are Configs X and Y in same orbit-type? X has separation 8 (along x), Y has separation 10. Translation can only shift positions, not change separation. Rotation by 90° maps x-separation to y-separation but preserves magnitude. So separation 8 vs 10 are DIFFERENT orbit-types.

For these:
- σ_multi^(A): both have stabilizer $D_4 \wr S_2$ same abstract group → σ_jk irreps drawn from same set → A might be similar **for the PER-FORMATION σ_j** (same $D_4$) but different **for σ_12 cross-block** (different $\lambda_{\mathrm{rep}} \cdot $ depending on cluster-overlap, etc.).

Continuous A data could distinguish (say through different inner product $\langle u^{(1)}, u^{(2)} \rangle$, different H_12 op_norm, etc.). But these continuous values change with $\lambda_{\mathrm{rep}}$ even within a single orbit-type.

**Discrete D label**: the conjugacy class of $D_4 \wr S_2$ in $\Gamma$ — separation 8 case vs separation 10 case give DIFFERENT conjugacy classes (because the swap involution is rotated about different lattice points; these are conjugate in $\Gamma$ only if a translation maps one to the other, which requires equal separation). So D distinguishes 8 vs 10 separations.

### 2.4 Reduction theorem (precise)

**Theorem 2.1**: In well-separated regime, σ_multi^(D) decomposes as:
$$\sigma_{\mathrm{multi}}^{(D)}(\mathbf{u}^*) = (\text{topological orbit-type label } [G_{\mathbf{u}^*}]_{\Gamma}) \otimes (\text{cohomology of stabilizer } H^*(BG_{\mathbf{u}^*})). \tag{2.1}$$

The first factor (topological orbit-type label) is **NOT** determined by σ_multi^(A) — it depends on the geometric placement (e.g., separation distance) of the formations on the graph.

The second factor (cohomology of stabilizer) IS determined by σ_multi^(A) — because A uses irreps of $G_{\mathbf{u}^*}$ which encode the abstract group structure.

**Conclusion**:
- D contains MORE information than A (via the topological orbit-type).
- A determines the abstract-group portion of D.
- D and A are **complementary** invariants.

### 2.5 Reverse direction: A from D?

Can σ_multi^(D) determine σ_multi^(A)?

σ_multi^(D) = orbit-type + cohomology. Continuous data in σ_multi^(A) (eigenvalues like $\mu_{\mathrm{Gold}}$, $H_{12}$ op-norm) is **NOT** determined by D — different parameter values $(\beta, c, \lambda_{\mathrm{rep}})$ give same orbit-type but different A.

**Conclusion (reverse)**: D does NOT determine A. Continuous data is missing from D.

### 2.6 Summary

A and D are **complementary**, neither determines the other:
- A → continuous spectrum (depends on $\beta, c, \lambda_{\mathrm{rep}}$); abstract-group structure (independent of position).
- D → discrete topological label (depends on position); cohomology (abstract group).
- Intersection (mutual): abstract-group structure of stabilizer.
- A's exclusive: continuous parameter dependence.
- D's exclusive: topological orbit position.

**Joint invariant** σ_multi^(A) ⊕ σ_multi^(D) (or σ_multi^(A) × σ_multi^(D) as a 4-tuple) carries strictly more information than either alone.

---

## §3. K=1 Special Case: D = A + Triviality

For K=1, no swap factor, no relative position between formations. σ_multi^(D) = orbit-type of $\mathrm{Stab}_{\mathrm{Aut}(G)}(u^*)$ + its cohomology.

σ_multi^(A) for K=1 = Commitment 14 σ-tuple. The irrep theory used by A depends on conjugacy class of stabilizer — this is exactly the orbit-type.

So **for K=1, σ_multi^(A) → σ_multi^(D) is a function** (D's discrete label is encoded in which Irr-set σ_k are drawn from).

Conversely, σ_multi^(D) → σ_multi^(A) is NOT a function (continuous σ_k eigenvalues missing).

For K=1 case: D ⊆ A (D is implicitly contained in A's irrep labels).

**This recovers the K=1 reduction claim** in `06_*` §3.5 ("D reduces to (a refinement of) Commitment 14 when K=1"). The "refinement" is just the conjugacy class of stabilizer made explicit.

---

## §4. K ≥ 3 Generalization

For K=3, $\Gamma = \mathrm{Aut}(G) \wr S_3$. σ_multi^(D) orbit-type involves:
- Conjugacy class of per-formation stabilizer.
- Conjugacy class of $S_3$ swap action (with possible reduction to subgroups when not all 3 formations are equivalent).
- Topological position label.

σ_multi^(A) for K=3 has more cross-blocks ($\sigma_{12}, \sigma_{13}, \sigma_{23}$) but no full $S_3$-irrep theory beyond pairwise.

**Generalization of (2.1)**:
$$\sigma_{\mathrm{multi}}^{(D)}(\mathbf{u}^*) = (\text{topological orbit-type}) \otimes (\text{cohomology of stabilizer}). \tag{4.1}$$

Same structure as K=2, but the wreath product becomes $G \wr S_K$ (or appropriate sub-structure if not all formations equivalent).

**NQ-207** (Phase 3 E6 NEW, W7+): Generalize Theorem 2.1 to K ≥ 3 formally. Verify orbit-type label still factors out cleanly from A's continuous data.

---

## §5. Implication for Practical Use

### 5.1 When to use A vs D

- **A primary use**: numerical computation, predictions in specific parameter regimes, eigenvalue tracking with $\lambda_{\mathrm{rep}}$.
- **D primary use**: distinguishing topological orbit-types (different separations / geometric placements), persistence under continuous parameter variation.

### 5.2 Combined invariant for canonical proposal

If σ_multi (Cat A target) is to be the most-informative discrete invariant of K-formation states, the combined A ⊕ D form is preferable:
$$\sigma_{\mathrm{multi}}(\mathbf{u}^*) := (\sigma_{\mathrm{multi}}^{(A)}, \sigma_{\mathrm{multi}}^{(D)}). \tag{5.1}$$

Each piece carries different information; together they distinguish all configurations.

For paper §4 exposition: present A as the operational σ-tuple computation (Phase 2 + Phase 3 contribution); present D as the persistence / topological complementary layer (Phase 3 contribution).

**NQ-208** (Phase 3 E6 NEW, W7+): Canonical proposal for σ_multi as A ⊕ D combined invariant. Vs alternative: A only with D as a "footer" remark.

---

## §6. Cross-References

- `06_approach_AB_equivalence_and_D.md` §3: Approach D framework + §3.5 reduction claim.
- `10_sigma_multi_D_concrete.md`: σ_multi^(D) concrete computation.
- `05_sigma_multi_concrete_T2_K2.md`: σ_multi^(A) concrete.
- `08_lemma5_1_step3_proof.md`: wreath-product irrep theory (Frobenius reciprocity).
- canonical T-σ-Lemma-1 + Commitment 14 (single-formation σ).

---

**End of 12_D_to_A_reduction.md.**
**Status: D and A are complementary (not equivalent). D adds topological orbit-type; A adds continuous spectrum. Theorem 2.1 (K=2): σ_multi^(D) = topological orbit-type ⊗ cohomology of stabilizer. Reduction K=1: σ_multi^(A) ⊇ σ_multi^(D) (D is encoded in A's irrep labels). NQ-207, NQ-208 spawned.**
