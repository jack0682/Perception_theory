# sigma_class_category.md — σ-Class Category with Aut(G)-Equivariant Morphisms (Fukaya-Spirit)

**Status:** working draft (W5 Day 4 PM Wave 3 lead-side direct work, 2026-04-30).
**Type:** Categorification framework for σ-framework — σ-class as objects, Aut(G)-equivariant morphisms as arrows.
**Author:** team-lead@scc-wave3-deep-research.
**Canonical refs:** §11.1 Commitment 14 (σ-framework); §13 T-σ-Theorem-3/4 (closed form + first pitchfork); §14 CN10 contrastive.
**Working refs:** `sigma_lie_algebra_structure.md` (Aut(G)_{u*} stabilizer); `sigma_uniqueness_theorem.md` (NQ-188, σ-class definition); `foundational_bridges_2026.md` §4 Bridge B-3 (Geometric Langlands π_1 spirit); `formation_fundamental_group.md` (in flight, π_1(F) framework).
**External:** Fukaya, K. (1993, 2009). Fukaya category in symplectic topology. Shaw Prize 2025 spirit (CN10 contrastive).

---

## §1. Mission

Bridge B-7 (`foundational_bridges_2026.md` §X — Fukaya category was originally B-7 in early draft, repositioned to "Bridge X exploratory") proposes a Fukaya-spirit categorification of σ-framework.

**Goal of this file:** provide a precise definition of the **σ-class category** $\mathcal{C}_\sigma(G)$ as the categorification of σ-framework on a fixed graph $G$:
- **Objects:** σ-classes of minimizers (per NQ-188 Definition 2.1' canonical conjugation rule).
- **Morphisms:** Aut(G)-equivariant transition operators between σ-classes.

CN10 contrastive: SCC is **not** symplectic geometry; the Fukaya-category spirit is structural inspiration for categorical organization, not subject-matter import.

---

## §2. σ-Class Category $\mathcal{C}_\sigma(G)$ Definition

### §2.1 Objects

$\mathrm{Ob}(\mathcal{C}_\sigma(G))$ = set of σ-classes [u*] of minimizers $u^* \in \Sigma_m$ on graph $G$, modulo NQ-188 conjugation rule (Definition 2.1'):
$$[u_1^*] = [u_2^*] \iff \exists \pi \in \mathrm{Aut}(G) \text{ s.t. } \pi^{-1} G_{u_1^*} \pi = G_{u_2^*} \text{ and } \rho_k(u_2^*) = \rho_k(u_1^*) \circ \pi^{-1} \text{ for all } k$$

For R23 ($G = D_4$ free-BC 32×32 grid, $c = 0.5$, $\beta = 30$, $\alpha = 1$): 56 stable Morse-0 minimizers ↔ 56 distinct approximate σ-classes (NQ-188 §5 protocol; `sigma_class_count_R23.py` enumeration).

### §2.2 Morphisms

For two σ-classes $[u_1^*], [u_2^*] \in \mathrm{Ob}(\mathcal{C}_\sigma(G))$, the morphism set is:
$$\mathrm{Hom}_{\mathcal{C}_\sigma(G)}([u_1^*], [u_2^*]) := \{\text{Aut}(G)\text{-equivariant transition operators } T: \Sigma_m \to \Sigma_m\}$$

A transition operator $T$ between σ-classes is **Aut(G)-equivariant** if:
$$T(\pi \cdot u) = \pi \cdot T(u) \quad \forall \pi \in \mathrm{Aut}(G), u \in \Sigma_m$$

and $T$ maps neighborhoods of representatives of $[u_1^*]$ to neighborhoods of $[u_2^*]$.

### §2.3 Composition

For morphisms $T: [u_1^*] \to [u_2^*]$ and $S: [u_2^*] \to [u_3^*]$:
$$S \circ T: \Sigma_m \to \Sigma_m, \quad (S \circ T)(u) := S(T(u))$$

Aut(G)-equivariance is preserved under composition (since both $S$ and $T$ are Aut(G)-equivariant).

### §2.4 Identity

For each $[u^*]$: $\mathrm{id}_{[u^*]}: \Sigma_m \to \Sigma_m$ identity map (trivially Aut(G)-equivariant).

### §2.5 Category axioms

Associativity: $(R \circ S) \circ T = R \circ (S \circ T)$ — holds by function composition.
Identity: $\mathrm{id}_{[u^*]} \circ T = T = T \circ \mathrm{id}_{[u'^*]}$ — holds.

**$\mathcal{C}_\sigma(G)$ is a well-defined category.**

---

## §3. Examples on R23

### §3.1 Trivial morphisms

For each $[u^*]$, the identity $\mathrm{id}_{[u^*]}$ is a morphism $[u^*] \to [u^*]$.

The Aut(G)-action gives non-trivial morphisms within each σ-class: for each $\pi \in \mathrm{Aut}(G)$ and $[u^*]$, the map $u \mapsto \pi \cdot u$ is an automorphism of $[u^*]$ (an "internal" morphism). These form the automorphism group $\mathrm{Aut}([u^*]) = \mathrm{Aut}(G) / \mathrm{Aut}(G)_{u^*}$ (quotient by stabilizer).

### §3.2 Gradient flow morphisms (cross-class)

For two σ-classes $[u_1^*], [u_2^*]$ such that gradient flow on $\Sigma_m$ from a perturbation of $u_1^*$ converges to (a representative of) $[u_2^*]$, the gradient flow defines an Aut(G)-equivariant transition operator $T_{1 \to 2}$.

This is **not** a one-step transition: $T_{1 \to 2}$ depends on the basin-of-attraction structure between $u_1^*$ and $u_2^*$.

**For R23 minimizers:** a transition $T: [u_1^*] \to [u_2^*]$ exists iff some perturbation neighborhood of $[u_1^*]$ flows to $[u_2^*]$. By the energy-decreasing nature of gradient flow, $\mathcal{E}(u_2^*) \leq \mathcal{E}(u_1^*)$ for any such transition. Thus $\mathcal{C}_\sigma(G)$ has a **partial order** structure compatible with energy ordering.

### §3.3 Morse-class (for non-Morse-0 minimizers, future extension)

For Morse-index-1 saddle points (currently excluded from R23 stable enumeration), there exist canonical "rising" and "falling" trajectories. Including these saddles in $\mathrm{Ob}$ would give a genuine morphism structure linking different σ-classes via gradient-flow trajectories. This is the **Morse-Floer-style refinement**, deferred to W7+.

---

## §4. Categorical structure refinements

### §4.1 Symmetric monoidal structure (additive over disjoint formations?)

For multi-formation states $\mathbf{u} = (u^{(1)}, \ldots, u^{(K)}) \in \Sigma_M^K$, the σ-class of $\mathbf{u}$ at the well-separated regime ($D_{\mathrm{sep}} \geq 3$) decomposes as a tuple of single-formation σ-classes (per `multi_formation_sigma.md` D-6a Cat A in well-separated). 

**Conjecture (Cat C):** $\mathcal{C}_\sigma(G)$ admits a symmetric monoidal structure where $[u_1^*] \otimes [u_2^*] := [\text{disjoint multi-formation state}]$, with $\otimes$ associative and commutative up to canonical isomorphism.

This is the categorical analog of the Tool A2 quotient by $S_K$ (formation-label symmetry).

### §4.2 σ-class category as enriched category

$\mathcal{C}_\sigma(G)$ may be enriched over the category of $\mathrm{Aut}(G)$-equivariant sets: $\mathrm{Hom}([u_1^*], [u_2^*])$ carries an $\mathrm{Aut}(G)$-action by $\pi \cdot T := \pi \circ T \circ \pi^{-1}$.

This enrichment captures the Aut(G)-symmetry of transitions explicitly.

### §4.3 Triangulated structure (highly conjectural)

Fukaya categories in symplectic topology are triangulated. Whether $\mathcal{C}_\sigma(G)$ admits a triangulated structure (with shift functor + distinguished triangles) is unclear — **probably not** in general, since SCC has no symplectic structure. CN10 contrastive: import categorical concept (= categorification of σ-framework) without symplectic content.

---

## §5. Connection to other structures

### §5.1 Connection to σ-class enumeration (NQ-188)

The objects of $\mathcal{C}_\sigma(G)$ are exactly the σ-classes enumerated by NQ-188. R23 numerical (sigma_class_count_R23.py) gives 56 objects.

### §5.2 Connection to π_1(F) (Bridge B-3, formation_fundamental_group.md)

The "internal" automorphisms within each σ-class form the group $\pi_1(\mathcal{F}; [u^*]) = \mathrm{Aut}(G)/\mathrm{Aut}(G)_{u^*}$ (per Bridge B-3 and NQ-188 conjugation rule). Thus $\pi_1(\mathcal{F}; [u^*]) = \mathrm{Aut}([u^*])$ in $\mathcal{C}_\sigma(G)$ — the formation fundamental group is exactly the categorical automorphism group.

### §5.3 Connection to McKay-spirit conjecture (NQ-258, sigma_lie_algebra_structure.md)

NQ-258 (Cat C): σ-tuple irrep multiplicities $n_k$ derivable from Sylow normalizer of $\mathrm{Aut}(G)_{u^*}$.

In $\mathcal{C}_\sigma(G)$ this means: the categorical "fingerprint" of an object $[u^*]$ (its σ-tuple) is determined by the local stabilizer's Sylow structure. **Compatible with NQ-258 conjecture.**

### §5.4 Connection to Vafa-Witten invariants (Bridge X, exploratory)

Vafa-Witten invariants count moduli space objects with sign weights. In $\mathcal{C}_\sigma(G)$ analog: count σ-classes weighted by $(-1)^{\mathrm{Morse}([u^*])}$ + Aut(G)-equivariant character. Cat C exploratory; defer to W8+.

---

## §6. Cat target

**Cat C primary:** $\mathcal{C}_\sigma(G)$ as a category is a definitional construction. Cat A would require establishing all category axioms rigorously (done above § §2.5) plus a substantive theorem within the categorical framework. Currently:

- §2 definitions: Cat A (definitional, immediate verification of axioms).
- §3.2 gradient flow morphisms: Cat B (depends on basin-of-attraction structure, conjectured but not proved).
- §4.1 symmetric monoidal structure: Cat C (conjecture, well-separated regime only).
- §5.1-5.3 connections: Cat C (consistency conjectures with NQ-188/258 + Bridge B-3).
- §5.4 Vafa-Witten analog: Cat C exploratory.

**Net Cat target for the file:** C (with §2 Cat A definitional spine).

---

## §7. CV-1.7+ promotion path

**Not** for CV-1.6 (release target W6 Day 7 EOD; this file is W7+ scope).

For CV-1.7 or beyond:
- §2 Cat A definitional content: ~50 lines canonical §11.1 supplementary or §13 supporting structure.
- §3-§4 conjectures: stay working/SF/.
- §5 cross-references: footnotes only at canonical level.

**Effort:** ~30-50 canonical lines for Cat A definitional spine; rest deferred.

---

## §8. Hard constraint verification

- [x] **u_t primitive maintained**: σ-classes are equivalence classes of cohesion field minimizers; primitive unchanged.
- [x] **CN10 contrastive throughout**: Fukaya category is structural inspiration only; SCC is not symplectic geometry. §1, §4.3, §5.4 explicit.
- [x] **CN5 4-energy not merged**: σ-classes are defined on full $\mathcal{E}$ minimizers (4 terms preserved).
- [x] **Aut(G)-equivariance**: morphisms required Aut(G)-equivariant (§2.2); category structure naturally compatible with NQ-188 conjugation rule.
- [x] **OP not silently resolved**: NQ-188 σ-class enumeration unchanged; this file provides a categorical organization, not a resolution.

---

## §9. Cross-references

### §9.1 Working files
- `working/SF/sigma_lie_algebra_structure.md` — Aut(G)_{u*} stabilizer + McKay-spirit NQ-258.
- `working/SF/sigma_uniqueness_theorem.md` — NQ-188 σ-class definition (Definition 2.1').
- `working/SF/sigma_topological_invariance.md` — NQ-190 σ-class topology.
- `working/SF/formation_fundamental_group.md` (in flight, pi1-formation-prover) — π_1(F) = Aut(G)_{u*}.
- `working/MF/foundational_bridges_2026.md` §4 Bridge B-3 (Langlands π_1 spirit), §X Fukaya bridge (exploratory).
- `working/MF/sigma_rich_augmentation.md` (Wave 3) — σ_rich enrichment compatible with $\mathcal{C}_\sigma(G)$ morphisms.

### §9.2 External references
- Fukaya, K. (1993). "Morse homotopy, $A_\infty$-category, and Floer homologies." *Proc. GARC Workshop on Geometry and Topology*. — Original Fukaya category construction in symplectic topology.
- Fukaya, K. (2009). "Application of Floer homology of Lagrangian submanifolds to symplectic topology." *Morse Theoretic Methods in Nonlinear Analysis and in Symplectic Topology*. — Modern reference.
- Shaw Prize Foundation (2025). Kenji Fukaya award. [⚠️ exact citation pending verification.]

---

**End of sigma_class_category.md.**

**Status:** working draft, Cat C primary (with §2 Cat A definitional spine). Categorical framework for σ-class organization. CN10 contrastive (Fukaya category spirit, not symplectic content). Connections to NQ-188 / NQ-258 / Bridge B-3 / σ_rich / σ_topological_invariance documented. CV-1.6 not targeted; W7+ CV-1.7 candidate.
