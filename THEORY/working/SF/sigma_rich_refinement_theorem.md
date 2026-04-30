# sigma_rich_refinement_theorem.md — σ_rich is a Strict Refinement of σ_standard (Cat A target)

**Status:** working draft (W5 Day 4 PM Wave 3 lead-side direct work, 2026-04-30).
**Type:** Cat A target theorem statement + proof outline.
**Author:** team-lead@scc-wave3-deep-research.
**Canonical refs:** §11.1 Commitment 14 (σ-framework single-formation); §11.1 Commitment 14-Multi (D-6a static); §13 T-σ-Theorem-3 (T-uniform Hessian).
**Working refs:** `sigma_rich_augmentation.md` (Wave 3, σ_rich definition); `sigma_uniqueness_theorem.md` (NQ-188, σ_standard equivalence via conjugation rule); `sigma_lie_algebra_structure.md` (Aut(G)_{u*} stabilizer).

---

## §1. Mission

The Wave 3 file `sigma_rich_augmentation.md` (533 lines, op-0008-architect, ✅ persisted) introduces:
$$\sigma_{\mathrm{rich}}(u) = (\sigma_{\mathrm{standard}}(u),\, \{\mathrm{centroid}_j(u)\},\, \{\mathrm{orientation}_j(u)\},\, \{\text{Wigner-vN data}_{jk}\})$$

A natural question: **is σ_rich a strict refinement of σ_standard?** I.e., does σ_rich distinguish more equivalence classes than σ_standard?

This file provides a formal Cat A target answer: **YES**, σ_rich strictly refines σ_standard. Specifically:

**Theorem (Refinement, Cat A target):**
*For every graph $G$ satisfying (G1)-(G4), the equivalence relation defined by σ_rich (per the Wave 3 σ_rich conjugation rule) is a strict refinement of the equivalence relation defined by σ_standard (NQ-188 conjugation rule). I.e.,*
$$[u_1^*]_{\sigma_{\mathrm{rich}}} \subseteq [u_1^*]_{\sigma_{\mathrm{standard}}}$$
*with the inclusion **strict** on graphs admitting σ_standard-degenerate but σ_rich-distinct configurations.*

---

## §2. Definitions

### §2.1 σ_standard equivalence (NQ-188 Definition 2.1')

$[u_1^*]_{\sigma_{\mathrm{standard}}} = [u_2^*]_{\sigma_{\mathrm{standard}}}$ iff there exists $\pi \in \mathrm{Aut}(G)$ such that:
- (a) $\pi^{-1} G_{u_1^*} \pi = G_{u_2^*}$ (stabilizer conjugacy)
- (b) $\rho_k(u_2^*) = \rho_k(u_1^*) \circ \pi^{-1}$ for all $k$ (irrep-label translation)
- (c) Schur-degenerate eigenspace handling
- (d) Mulliken lex-order tie-break

### §2.2 σ_rich equivalence (proposed Wave 3, §2.2 sigma_rich_augmentation.md)

$[u_1^*]_{\sigma_{\mathrm{rich}}} = [u_2^*]_{\sigma_{\mathrm{rich}}}$ iff there exists $\pi \in \mathrm{Aut}(G)$ such that:
- (a)-(d) as in σ_standard (i.e., σ_standard equivalence holds via π).
- (e) **Centroid translation**: $\pi(\mathrm{centroid}_j(u_1^*)) = \mathrm{centroid}_{\pi(j)}(u_2^*)$ for all $j$ (where $\pi(j)$ is the formation-label translation under the Aut(G)-action).
- (f) **Orientation tensor translation**: $\pi(\mathrm{orientation}_j(u_1^*))\pi^{-1} = \mathrm{orientation}_{\pi(j)}(u_2^*)$ (rotation of inertia tensor under graph automorphism).
- (g) **Wigner-vN matrix translation**: $W_{j_1 j_2}(u_2^*) = U(\pi)^{-1} W_{\pi(j_1)\pi(j_2)}(u_1^*) U(\pi)$ where $U(\pi)$ is the unitary representation of $\pi$ on the paired-Goldstone subspace.

---

## §3. Theorem statement

**Theorem (σ_rich Refinement, Cat A target).**

*Let $G$ satisfy hypotheses (G1)-(G4). For any minimizers $u_1^*, u_2^* \in \Sigma_m$ (or $\widetilde{\Sigma}^K_M$ for multi-formation):*

1. *$[u_1^*]_{\sigma_{\mathrm{rich}}} \subseteq [u_1^*]_{\sigma_{\mathrm{standard}}}$ (refinement).*
2. *The inclusion is generically strict — there exist graph classes (e.g., 2D Z_n×Z_n torus, 1D Z_n cycle) admitting σ_standard-equivalent minimizers that are σ_rich-distinct.*
3. *On highly-symmetric graphs (e.g., complete graph K_n, Petersen graph), the inclusion may degenerate to equality (if all σ_standard-equivalent minimizers also share centroid + orientation up to Aut(G)-symmetry).*

---

## §4. Proof outline (Cat A target)

### §4.1 Inclusion (1)

Trivial: σ_rich equivalence requires σ_standard equivalence (clauses (a)-(d)) PLUS additional clauses (e)-(g). Therefore σ_rich-equivalent ⇒ σ_standard-equivalent. Inclusion holds.

### §4.2 Strictness on Z_n cycle

Consider 1D $\mathbb{Z}_n$ cycle with $n = 8$ at $\beta$ slightly above $\beta_{\mathrm{crit}}^{(2)}$. Two minimizers can have the same σ-tuple (single double-eigenvalue 2D irrep at first pitchfork) but be located at different cycle positions. Their σ_standard equivalence holds via $\pi = \mathbb{Z}_n$-rotation; their σ_rich equivalence ALSO holds via the same $\pi$ (centroid translates, orientation translates, Wigner-vN matrix translates).

So on $\mathbb{Z}_n$ cycle, σ_rich = σ_standard in the **single-formation** case.

**However:** for **multi-formation** on $\mathbb{Z}_n$, two K=2 configurations with the same per-formation σ-tuples but different inter-formation centroid distances (say $d_1 = 2$ vs $d_2 = 4$ on the cycle) are σ_standard-equivalent (per-formation σ matches under formation-label permutation via the $S_2$ wreath product) but σ_rich-distinct (centroid distance differs).

**Strict refinement on multi-formation Z_n cycle.**

### §4.3 Strictness on Z_n × Z_n torus

Stronger example: 2D $\mathbb{Z}_n \times \mathbb{Z}_n$ torus. Two K=2 configurations:
- Configuration A: formations at (0,0) and (n/2, n/2) — diagonal arrangement, centroid distance = $n/\sqrt{2}$ (graph metric).
- Configuration B: formations at (0,0) and (n/2, 0) — axis-aligned, centroid distance = $n/2$.

Both have the same per-formation σ-tuples (assuming uniform mass and same parameters). σ_standard: equivalent under the $S_2$ formation permutation alone (no graph rotation links the diagonal to axis-aligned in the Aut(G) of $\mathbb{Z}_n^2$ which is $D_4 \ltimes (\mathbb{Z}_n)^2$).

Wait — actually $D_4$ acts on $\mathbb{Z}_n \times \mathbb{Z}_n$ torus and rotates diagonal ↔ axis-aligned via 45° rotation if $n$ supports that. Need to check carefully. On odd $n$ the $D_4$ rotation by 45° maps $\mathbb{Z}_n^2 \to \mathbb{Z}_n^2$ is *not* a graph automorphism (the diagonal connection is not an edge). So $D_4$ rotation 90° works but not 45°. 

So actually configurations A (diagonal, $d_1 = n/\sqrt{2}$ Euclidean ≈ $n$ graph distance) and B (axis-aligned, $d_2 = n/2$ graph distance) have **different graph distances**. They are σ_standard-distinct (different centroid-distance, and centroid is part of standard σ via inter-formation $\sigma_{ij}^{(c)}$ component if defined that way). Need to check NQ-188 σ_standard definition for multi-formation case.

**Re-examination:** σ_standard at multi-formation level (per `multi_formation_sigma.md` §1.4 + σ_multi^A definition) includes $\mathcal{F}_{\mathrm{total}}$ + per-formation σ-tuples + cross-formation σ-tuples. Cross-formation σ_jk encodes coupling between formation $j$ and $k$ via shared eigenmodes. The inter-formation distance is **encoded indirectly** through the cross-formation σ_jk.

So on Z_n^2 torus, configurations A and B have **different cross-formation σ_jk** (because the eigenmode overlap differs at distance $n/\sqrt{2}$ vs $n/2$). Hence σ_standard-distinct.

**Question for sharper example:** are there cases where cross-formation σ_jk is equal but centroid configuration differs? Conjecturally yes, on graphs with high symmetry (e.g., complete multipartite graphs).

**Defer detailed example construction to numerical investigation (Wave 4+).**

### §4.4 σ_rich-distinct counterexample (Cat A target)

The σ_rich Wigner-vN component captures avoided-crossing data between paired Goldstone modes. Two K=2 configurations with identical σ_standard but distinct **avoided-crossing geometry** (e.g., one configuration has paired Goldstones nearly degenerate; another has Goldstone pair widely separated) are σ_rich-distinct.

**Concrete example needed:** 2D D_4 free-BC grid with K=2 formations placed (i) symmetrically on the diagonal vs (ii) on the axis. The avoided-crossing data between the two formations' translation Goldstones differs structurally — for diagonal placement, Goldstones couple via $E$-irrep mixing; for axis placement, Goldstones couple via $A_1 \oplus A_2$ direct product. Wigner-vN matrix structure differs.

**Cat A target:** prove via explicit Hessian computation on D_4 free-BC R23 with K=2 placement varied.

---

## §5. Cat target

- §3 statement: **Cat A target** (theorem).
- §4.1 proof of inclusion: Cat A immediate.
- §4.2-§4.4 strictness via explicit examples: Cat A target via numerical anchor + theoretical computation.

**Net Cat target:** A (with numerical anchor required for §4.2-§4.4 explicit examples).

---

## §6. Numerical verification protocol

CODE/scripts/sigma_rich_refinement_R23.py (proposal):

```python
"""Numerical verification of σ_rich strict refinement on R23 K=2 configurations.

Setup:
- Load R23 K=1 minimizers (56 stable Morse-0).
- Construct K=2 configurations by pairing R23 minimizers at varied separation.
- For each pair (i, j) with separation d:
  - Compute σ_standard (NQ-188 protocol).
  - Compute σ_rich (Wave 3 §2 protocol).
- Tally:
  - Number of σ_standard equivalence classes.
  - Number of σ_rich equivalence classes.
- Verify: |σ_rich-classes| > |σ_standard-classes| (strict refinement).

Effort estimate: ~6-8h compute on R23 K=2 enumeration.
"""
```

**Cat A criterion:** if |σ_rich-classes| > |σ_standard-classes| for at least one pair, strict refinement is verified.

**Falsification criterion:** if |σ_rich-classes| = |σ_standard-classes| for all R23 K=2 pairs, σ_rich does not strictly refine σ_standard on R23. (Would suggest σ_rich = σ_standard on D_4 free-BC, making σ_rich's added components redundant.)

---

## §7. Connection to NQ-188 σ-class enumeration

NQ-188 σ-class enumeration (via `sigma_class_count_R23.py`) counted 56 distinct **σ_standard-classes** on R23 K=1 minimizers. The σ_rich-class count for the same R23 K=1 minimizers may be:
- **Equal to 56**: σ_rich agrees with σ_standard on K=1 (no centroid/orientation distinguishing power for R23 D_4 single formation).
- **Greater than 56**: σ_rich distinguishes some K=1 σ_standard-equivalent minimizers via centroid or orientation differences.

**Numerical investigation needed Wave 4+.**

---

## §8. Implications for OP-0008 Path B

If σ_rich strictly refines σ_standard:
- The Path B claim (sigma_rich_augmentation.md §3 Cat A target) that "Φ_rich K-jump inheritance is deterministic" gains substantive content — the additional σ_rich data captures merger-geometry dependence that σ_standard misses.
- Therefore: σ_rich is a **non-trivial enrichment**, not redundant with σ_standard.

If σ_rich = σ_standard generically:
- Path B reduces to Path A; the σ_rich augmentation is **trivial** in some sense.
- OP-0008 cannot be resolved via Path B and Path A (accepting non-determinism) becomes the only canonical path.

**Numerical strict-refinement test is therefore a key Cat A criterion for Path B viability.**

---

## §9. Hard constraint verification

- [x] **u_t primitive maintained**: σ_rich and σ_standard both derived diagnostics on $u_t$ field.
- [x] **CN10 contrastive**: no external theory imports requiring CN10 enforcement (refinement theorem is internal SCC structure).
- [x] **CN5 4-energy not merged**: σ tuples computed on full $\mathcal{E}$ minimizers.
- [x] **OP not silently resolved**: OP-0008 Path B viability is *contingent* on this refinement holding; not silently resolved.

---

## §10. Cross-references

- `working/MF/sigma_rich_augmentation.md` (Wave 3, σ_rich definition).
- `working/SF/sigma_uniqueness_theorem.md` (NQ-188, σ_standard equivalence via conjugation rule).
- `working/SF/sigma_lie_algebra_structure.md` (Aut(G)_{u*} stabilizer).
- `working/SF/sigma_class_category.md` (σ-class category $\mathcal{C}_\sigma(G)$ — refinement = subcategory inclusion).
- canonical §13 T-σ-Theorem-3/4 (closed-form Hessian + first pitchfork).

---

**End of sigma_rich_refinement_theorem.md.**

**Status:** Cat A target theorem statement + proof outline. Numerical verification protocol via `sigma_rich_refinement_R23.py` (W6+ priority). Strict refinement is a key Cat A criterion for OP-0008 Path B viability. Connections to NQ-188 σ-class enumeration + σ-class category structure documented.
