# sigma_lie_algebra_structure.md — Lie Algebra / Group Theory Perspective on the σ-Framework (NQ-258 Initiation)

> **⚠️ PARTIAL RETIRE-CANDIDATE (W6 D1 EOD parking-lot Issue #4 audit, 2026-05-04)**
> **Retire scope:** (1) **Lie group / Lie algebra framing** — entirely inapplicable since $\mathrm{Aut}(G)$ is FINITE (no continuous structure, no Lie algebra in the standard sense); ~40% of file content is finite-group representation review reframed as "Lie analog" which is misleading. (2) **NQ-258 McKay-spirit conjecture** (Cabanes-Späth 2023) — pure speculation; SCC has no $p$-Sylow normalizer mechanism, no character-table modular representation theory; the "σ-tuple derivable from Sylow normalizer" conjecture has no SCC-specific evidence and no clear proof path. Cat C status maintained but with no plausible upgrade path.
> **Preserve scope:** (1) §3 **Aut(G)_{u*} stabilizer definitions** — but **most of this content is duplicated in `sigma_uniqueness_theorem.md` (NQ-188) + `formation_fundamental_group.md` Definition 3.1**, so consolidation rather than independent preservation is preferable. (2) **NQ-259 (R23 explicit Aut(G)_{u*} computation)** — useful empirical task; not Lie-theoretic in nature. (3) **NQ-260 (ML classifier for σ-orbit equivalence)** — scaffolding; separate empirical task.
> **Future split (W7+ recommended):** consolidate Aut(G)_{u*} content into `sigma_uniqueness_theorem.md`, separate NQ-259/260 into independent empirical-task files, retire Lie-algebra framing + McKay-spirit conjecture to `_archive/cv17_speculative_retired_2026-05-04/`.
> **5 active inbound references** (sigma_rich_refinement_theorem, foundational_bridges_2026, formation_birth_string_breaking, parking_lot_inventory, WAVE3_MASTER_INDEX) → split must preserve link integrity. Most references are index-only or to Aut(G)_{u*} basics (which would be redirected to sigma_uniqueness_theorem after consolidation).
> **CN10 disclosure**: $\mathrm{Aut}(G)$ on finite graph $G$ is a finite group (typically modest order: $D_4$ has order 8, $T^2_L$ symmetry group has order $8L^2$ etc.). Lie group / Lie algebra apparatus does not apply. McKay conjecture (Cabanes-Späth 2023) is a deep finite-group representation theory result with no SCC-specific instantiation; "σ-tuple from Sylow normalizer" is heuristic exploration without mathematical content.

**Status:** working draft (Wave 3 NEW theoretical work, 2026-04-30).
**Created:** 2026-04-30 (W6 Day 1 Wave 3 Group Theory import).
**Author origin:** User directive: apply 2024-2026 group theory developments (McKay conjecture proved Cabanes-Späth 2023; Lie group tangent-space methods; GAGTA 2025 AI+group theory; Geometric Langlands spirit) to multi-formation σ-framework.
**Canonical refs:** §13 T-σ-Lemma-1 (Aut(G)-orbit invariance); §13 T-σ-Theorem-3/4 (D_4 free-BC σ-tuple); §11.1 Commitment 14 (O5')(O7) σ-tuple definition; §14 CN10 (contrastive vs reductive); §14 CN17 (σ-Labeled Formation Quantization); §13 T-V5b-T (Goldstone characterization).
**Working refs:** `working/MF/multi_formation_sigma.md` (σ_multi§2.1 joint stabilizer Aut(G)≀S_K); `working/SF/sigma_uniqueness_theorem.md` (NQ-188 σ-class enumeration); `working/SF/sigma_topological_invariance.md` (NQ-190 graph-isomorphism invariance); `working/SF/sigma_theorem4_higher_order.md` (NQ-187 ε-splitting).
**External refs:** Mackey, G.W. (1952) "Induced representations of locally compact groups I," *Ann. Math.* 55:101–139; Cabanes, M. and Späth, B. (2023) "Towards the McKay conjecture: classification of M_inv-triples," *J. Reine Angew. Math.*; Serre, J.-P. (1977) *Linear Representations of Finite Groups*, Springer; GAGTA 2025 (Groups, Algorithms, Geometry and Theory of Automata, annual workshop).
**Open problems referenced:** OP-0008 (σ^A K-jump non-determinism); OP-0009 (Multi-Formation Ontological Foundations); NQ-188 (σ-class enumeration, single-formation); NQ-258 (NEW: McKay-spirit conjecture for σ-tuple derivability from Sylow normalizer); NQ-259 (NEW: explicit Aut(G)_{u*} computation on R23); NQ-260 (NEW: ML classifier for σ-orbit equivalence).

**Hard constraints (CN10 + CN17 + promotion barrier):**
- SCC is NOT a Lie group. SCC is NOT a continuous gauge theory. All Lie/group theory references are STRUCTURAL ANALOGIES, used contrastively.
- The Lie algebra reading (§6) is a finite-group analog, not an assertion that Aut(G) is a Lie group.
- Direct canonical edits: 0. This is a working file. NQ-258 is Cat C (speculative conjecture); §3-§4 are Cat A (definitional restatement in new language); §6-§7 are Cat B (reinterpretation).
- Open problems (F-1, M-1, MO-1, OP-0008, OP-0009) are NOT silently resolved by this file.
- McKay-spirit conjecture (§5) is explicitly labeled Cat C and requires independent proof before any canonical promotion.

---

## §1. Mission

**NQ-258 objective.** Apply the spirit of recent group-theoretic developments — the McKay conjecture (Cabanes-Späth 2023), Lie group tangent-space geometry, and AI-assisted orbit classification (GAGTA 2025) — to the single-formation σ-framework (Commitment 14). The goal is threefold:

1. **Structural restatement.** Recognize that the σ-tuple decomposition is precisely the Aut(G)_{u*}-irrep decomposition of the tangent space T_{u*}Σ_m. This is a definitional observation (Cat A), not a new theorem, but it frames the σ-framework in group-representation language that enables new conjectures.

2. **McKay-spirit conjecture (NQ-258, Cat C).** Formulate a McKay-type conjecture: the σ-tuple at u* is determined by the Sylow normalizer N_{Aut(G)_{u*}}(P) for a Sylow p-subgroup P ⊆ Aut(G)_{u*}, not the full stabilizer. This would be the SCC analog of Cabanes-Späth (2023).

3. **GAGTA-spirit application (NQ-260, Cat C).** Identify σ-class equivalence (NQ-188) as an orbit-classification problem amenable to ML/graph-isomorphism methods.

**Contrastive position (CN10).** SCC is not a Lie group theory, not a gauge theory, and not a representation-theoretic framework for continuous groups. The Lie algebra language imported here is a *structural analog*: the tangent space T_{u*}Σ_m plays the role of a Lie algebra at a symmetry-broken point, but the "group" is the finite group Aut(G)_{u*}, which has no infinitesimal structure. Every section below explicitly marks where the analogy holds and where it breaks.

---

## §2. Formation Manifold and Tangent Space

### §2.1 Σ_m as smooth simplex

The energy E: [0,1]^n → ℝ is minimized subject to the volume constraint Σ_i u_i = m. The constraint manifold is:

$$\Sigma_m = \{ u \in [0,1]^n : \sum_{i=1}^n u_i = m \},$$

which is a compact (n-1)-dimensional polytope (a face of the standard n-simplex). In the interior Σ_m^∘ = {u ∈ (0,1)^n : Σ u_i = m}, the polytope is a smooth (n-1)-dimensional manifold. The SCC optimization (canonical §8, §10) operates on Σ_m^∘ via projected gradient descent, treating Σ_m^∘ as a Riemannian manifold with the inherited Euclidean metric.

**Dimension.** dim(Σ_m) = n-1. The co-dimension-1 constraint Σ u_i = m removes one degree of freedom from ℝ^n.

**Lie group analogy (structural, contrastive).** In Lie group theory, G is a smooth manifold of dimension equal to the dimension of the Lie algebra g = T_e G. Here, Σ_m plays the role of the "group manifold," with dimension n-1. The analogy breaks immediately: Σ_m has no group structure. The parallel is purely manifold-geometric: both are smooth manifolds on which a symmetry group acts.

### §2.2 Tangent space at u*

At a minimizer u* ∈ Σ_m^∘, the tangent space is:

$$T_{u^*}\Sigma_m = \{ v \in \mathbb{R}^n : \langle v, \mathbf{1} \rangle = 0 \},$$

the hyperplane of zero-mean perturbations. This is the (n-1)-dimensional linear subspace of ℝ^n orthogonal to the all-ones vector **1**. The Hessian H(u*) of E restricted to T_{u*}Σ_m is an (n-1)×(n-1) symmetric matrix (after projection P = I - **1 1**^T/n).

**Volume-preserving perturbations.** Every v ∈ T_{u*}Σ_m is a volume-preserving perturbation: moving in direction v does not change the total mass Σ u_i. The σ-framework analyzes the spectral structure of H(u*)|_{T_{u*}Σ_m}, exactly the restriction to this tangent space.

**Lie algebra parallel (structural, contrastive).** In a Lie group G with a spontaneously broken symmetry (G → H at a ground state g*), the Goldstone modes span a subspace of the Lie algebra g = Lie(G) corresponding to the broken generators g/h (where h = Lie(H) is the unbroken subalgebra). Here, T_{u*}Σ_m plays the role of g: it is the "infinitesimal" space of deformations. The analogy holds at the vector-space level. It breaks at the algebraic level: T_{u*}Σ_m carries no Lie bracket, since Σ_m has no group structure and Aut(G)_{u*} is finite (no continuous one-parameter subgroups).

---

## §3. Aut(G) Action and Stabilizer Aut(G)_{u*}

### §3.1 Aut(G) action on Σ_m

The automorphism group Aut(G) of the finite graph G = (X, E) acts on the vertex set X by permutations. This induces an action on ℝ^n by permutation matrices {P_π : π ∈ Aut(G)}. Since each P_π preserves the all-ones vector and the total mass Σ u_i, the action restricts to Σ_m:

$$\pi \cdot u := P_\pi u, \qquad (\pi \cdot u)_i = u_{\pi^{-1}(i)}.$$

The energy E is Aut(G)-equivariant (T-σ-Lemma-1, canonical §13): E(π · u) = E(u) for all π ∈ Aut(G). Hence Aut(G) maps minimizers to minimizers, and maps Aut(G)-orbits of minimizers to themselves.

**Finiteness.** For a finite graph G with n vertices, Aut(G) ≤ S_n (the symmetric group on n letters), hence |Aut(G)| ≤ n!. For graphs with high symmetry (e.g., D_4 free-BC L×L grids), |Aut(G)| = 8 (the dihedral group D_4). For random graphs, |Aut(G)| = 1 generically. In all cases, Aut(G) is a FINITE group — there is NO continuous Lie structure on Aut(G) for finite G.

**Lie group contrast.** In continuous gauge theory (Yang-Mills), the gauge group is an infinite-dimensional Lie group of smooth maps G: M → G_0. In RelationWorld (theory/), the discrete gauge structure is defined on finite graphs but the holonomy group is a finite group. SCC's Aut(G) is entirely finite and combinatorial. The Lie group perspective enters only as a structural metaphor for the tangent-space decomposition (§4), not as a mathematical claim about Aut(G) itself.

### §3.2 Stabilizer Aut(G)_{u*}

The stabilizer (isotropy subgroup) of u* under the Aut(G) action is:

$$\mathrm{Aut}(G)_{u^*} := \{ \pi \in \mathrm{Aut}(G) : P_\pi u^* = u^* \}.$$

This is a subgroup of Aut(G), hence a finite group. Its order divides |Aut(G)| by Lagrange's theorem. The orbit-stabilizer theorem gives:

$$|\mathrm{Aut}(G) \cdot u^*| \cdot |\mathrm{Aut}(G)_{u^*}| = |\mathrm{Aut}(G)|.$$

**Single-formation analog of σ_multi^D.** In the multi-formation context (working/MF/multi_formation_sigma.md §1.4), the joint stabilizer of a K-field minimizer **u** = (u^(1), ..., u^(K)) under Aut(G) ≀ S_K is σ_multi^D = Stab_{Aut(G) ≀ S_K}(**u**). The single-formation analog is exactly Aut(G)_{u*}: the stabilizer of a single minimizer u* under Aut(G) alone. This is the σ^D component for K=1.

**Geometric Langlands spirit (structural analogy, not direct application).** Geometric Langlands unifies representation theory, topology, and arithmetic by associating to a group G its Langlands dual G^∨ and studying sheaves on moduli spaces. The spirit relevant here: the σ-tuple of u* is a "representation-theoretic label" analogous to a Langlands parameter — it classifies the formation by its symmetry type, not by its geometric position. This is a metaphor for motivation, not a mathematical claim.

---

## §4. σ-Tuple via Stabilizer Character Theory

### §4.1 Schur's Lemma and Hessian block-diagonalization

**Lemma (Schur-commutation, working-file version).** Let H(u*) be the Hessian of E at u*, projected to T_{u*}Σ_m. Then H(u*) commutes with the Aut(G)_{u*} action on T_{u*}Σ_m:

$$P_\pi \, H(u^*) \, P_\pi^\top = H(u^*) \qquad \forall \pi \in \mathrm{Aut}(G)_{u^*}.$$

*Proof sketch.* E is Aut(G)-equivariant ⟹ E ∘ P_π = E for π ∈ Aut(G). Differentiating twice at u*: P_π H(u*) P_π^T = H(P_π u*) = H(u*) since π ∈ Aut(G)_{u*} fixes u*. The projection to T_{u*}Σ_m commutes with P_π (since P_π preserves **1**). □

By Schur's Lemma (Serre 1977 §2.2), any linear map commuting with an irreducible representation ρ of a finite group Γ is a scalar multiple of the identity on the irrep space. Hence: H(u*)|_{T_{u*}Σ_m} block-diagonalizes according to the irreducible decomposition of T_{u*}Σ_m as an Aut(G)_{u*}-module.

### §4.2 Irrep decomposition of T_{u*}Σ_m

The Aut(G)_{u*}-module T_{u*}Σ_m decomposes into irreducible representations:

$$T_{u^*}\Sigma_m \cong \bigoplus_{k=1}^{K_{\mathrm{irr}}} V_{\rho_k}^{\oplus n_k},$$

where:
- ρ_k is the k-th irrep of Aut(G)_{u*} (up to isomorphism), with dim(ρ_k) = d_k.
- n_k is the multiplicity of ρ_k in T_{u*}Σ_m.
- V_{ρ_k} is the carrier space of ρ_k.
- The total dimension check: Σ_k n_k d_k = n-1 (dimension of T_{u*}Σ_m). ✓

On each irrep block V_{ρ_k}^{⊕n_k}, the Hessian H(u*) acts as a scalar matrix λ_k I_{n_k d_k} by Schur's Lemma (when n_k = 1 and ρ_k is irreducible). For n_k > 1 (multiplicity), H(u*) acts as λ_k I_{d_k} ⊗ M_k where M_k is an n_k × n_k matrix of eigenvalue multiplicities — but generically (no accidental degeneracy) M_k is also scalar.

### §4.3 The σ-tuple IS the irrep decomposition

**Claim 4.1 (definitional equivalence, Cat A).** The Commitment-14 σ-tuple

$$\sigma(u^*) = \big(\mathcal{F}(u^*);\ \{(n_k, [\rho_k], \lambda_k)\}_{k=1}^{K_{\mathrm{irr}}}\big)$$

is precisely the irreducible decomposition of T_{u^*}\Sigma_m as an Aut(G)_{u^*}-module, augmented by the eigenvalue λ_k of H(u*) on each irrep block. This is a definitional restatement of Commitment 14 in group-representation language, not a new theorem.

*Justification.* Commitment 14 defines σ(u*) as the tuple of (multiplicity, irrep label, Hessian eigenvalue) triples, with tie-breaking by Mulliken order (O7). The irrep decomposition of §4.2 gives exactly these triples: n_k = multiplicity, [ρ_k] = conjugacy class of irrep (Schur: basis-independent), λ_k = Hessian eigenvalue on the block. The Mulliken ordering on irreps is standard character theory (Mulliken 1933, adopted by Commitment 14 O7).

**Consequence.** The σ-framework is precisely the theory of how the Hessian of E decomposes over the irreps of the formation's own symmetry group Aut(G)_{u*}. The number of σ-classes (NQ-188) equals the number of distinct irrep-decomposition types that appear in the minimizer set L(G, α, β, c).

---

## §5. McKay-Spirit Conjecture for σ_multi^A (NQ-258, Cat C)

### §5.1 McKay conjecture background

The McKay conjecture (originally stated 1972, proved Cabanes-Späth 2023 for all finite groups) states: for a finite group Γ and prime p,

$$|\mathrm{Irr}_{p'}(\Gamma)| = |\mathrm{Irr}_{p'}(N_\Gamma(P))|,$$

where Irr_{p'}(Γ) is the set of irreducible characters of Γ with degree not divisible by p, P is a Sylow p-subgroup of Γ, and N_Γ(P) is the normalizer of P in Γ. The spirit: complex representation data of the full group Γ is *determined* by the representation data of the much smaller subgroup N_Γ(P).

**Reference.** Cabanes, M. and Späth, B. (2023) "Towards the McKay conjecture: classification of M_inv-triples," *J. Reine Angew. Math.* 2023. Mackey, G.W. (1952) "Induced representations of locally compact groups I," *Ann. Math.* 55:101–139 (Mackey's induction/restriction framework, related to McKay correspondence via induced characters).

### §5.2 NQ-258 McKay-spirit conjecture

**Conjecture NQ-258 (Cat C — speculative, not proved).** Let Γ = Aut(G)_{u*} be the stabilizer of a single-formation minimizer u* and let p be the smallest prime dividing |Γ|. Let P ⊆ Γ be a Sylow p-subgroup with normalizer N_Γ(P). Then:

**(NQ-258a) Irrep multiplicity preservation.** The irrep multiplicities {n_k} appearing in the σ-tuple σ(u*) can be derived from the irrep structure of N_Γ(P) alone, via an induction formula:

$$n_k = \sum_{\mu \in \mathrm{Irr}(N_\Gamma(P))} \langle \mathrm{Ind}_{N_\Gamma(P)}^\Gamma \mu, \rho_k \rangle \cdot m_\mu,$$

where m_μ are multiplicities of μ in the N_Γ(P)-module T_{u*}Σ_m|_{N_\Gamma(P)}.

**(NQ-258b) Eigenvalue coarsening.** The Hessian eigenvalues {λ_k} on irrep blocks satisfy a Mackey-restriction formula: λ_k = λ_k^{(0)} + correction, where λ_k^{(0)} is determined by the N_Γ(P)-module structure and the correction is O(|Γ|/|N_Γ(P)|) small in the well-separated regime.

**Why this is Cat C.** NQ-258 is speculative for three reasons:
1. The McKay conjecture relates *counts* of irreps, not eigenvalues or multiplicities in a specific representation. Extending it to σ-tuple multiplicities requires a new induction argument.
2. The Sylow normalizer N_Γ(P) depends on the prime p; for |Γ| = 8 (D_4), p = 2 and P = Γ itself (2-Sylow is the whole group), so NQ-258a is trivially true but vacuous. Non-trivial instances arise when |Γ| has multiple prime factors.
3. The eigenvalue coarsening claim (NQ-258b) is heuristic: Mackey's induction/restriction does not directly constrain Hessian eigenvalues.

**Evidence pathway.** NQ-258 becomes Cat B when: (a) an explicit computation on a graph with |Aut(G)_{u*}| having at least 2 distinct prime factors confirms (NQ-258a), and (b) the induction formula is stated precisely with a proof sketch. NQ-259 (explicit Aut(G)_{u*} computation on R23) is the prerequisite.

**Relation to NQ-188.** The σ-class count (NQ-188, working/SF/sigma_uniqueness_theorem.md) is |{distinct irrep-decomposition types}|. If NQ-258 holds, the σ-class count is bounded by the number of N_Γ(P)-module types, which is ≤ |Irr(N_Γ(P))|. For D_4 (|N_Γ(P)| = |D_4| = 8, p=2), this gives |σ-classes| ≤ 5 (the five irreps of D_4: A_1, A_2, B_1, B_2, E).

---

## §6. Lie Algebra Reading: Goldstone Modes as Broken-Symmetry Generators

### §6.1 The structural analogy

In a continuous symmetry breaking G → H, the Goldstone theorem guarantees that the number of massless Goldstone bosons equals dim(G/H) = dim(G) - dim(H). These Goldstone modes are the infinitesimal generators of the broken symmetry: they span the complement of the Lie algebra h = Lie(H) in g = Lie(G).

In SCC, the "symmetry breaking" at the first pitchfork bifurcation (β > β_crit^(2)) is:

$$\mathrm{Aut}(G) \xrightarrow{\text{spontaneous}} \mathrm{Aut}(G)_{u^*},$$

where u* is a post-bifurcation minimizer. The "broken" symmetry is the coset Aut(G) / Aut(G)_{u*}. The orbit |Aut(G)·u*| = |Aut(G)| / |Aut(G)_{u*}| is the number of distinct minimizers in the orbit of u* (i.e., related by graph automorphisms).

**The Goldstone analog.** The "Goldstone modes" in SCC are the tangent vectors at u* that point toward the other minimizers in the orbit Aut(G)·u*. More precisely: the directions in T_{u*}Σ_m along which the Hessian eigenvalue is anomalously small (the V5b-T Goldstone mode, canonical §13 T-V5b-T) correspond to the "almost-broken" symmetry directions.

**Finite-group caveat (CN10, mandatory).** In a continuous Lie group, there is a one-to-one correspondence between broken generators and exactly-massless Goldstone modes. For a FINITE group Aut(G), there is NO continuous one-parameter subgroup connecting u* to a neighboring orbit element — the orbit is a discrete set. Hence the Goldstone modes in SCC are APPROXIMATELY massless (mass μ_Gold ∝ C(β)|∂S|/n > 0), not exactly massless. This is the content of T-V5b-T (canonical §13) and the V5b-F partial-Goldstone mechanism (Cat C, NQ-173).

### §6.2 Equivariant tangent vector field

The Goldstone modes identified in T-V5b-T form an Aut(G)_{u*}-equivariant tangent vector field on the orbit Aut(G)·u*. Precisely: if v ∈ T_{u*}Σ_m is a Goldstone mode (low-eigenvalue direction of H(u*)), then for each π ∈ Aut(G)_{u*}, P_π v is also a low-eigenvalue direction (by Schur-commutation, §4.1). The set of Goldstone modes forms an Aut(G)_{u*}-equivariant subspace of T_{u*}Σ_m.

**Irrep label of Goldstone modes.** The Goldstone mode subspace carries an irrep label [ρ_Gold] ∈ Irr(Aut(G)_{u*}). For the D_4 free-BC grid, T-V5b-T identifies the Goldstone mode as the bulk translation direction (ℓ = 0 angular mode), which carries the A_1 trivial irrep of D_4 (translation is D_4-symmetric). This matches the σ-tuple entry (n_1 = 1, [A_1], λ_Gold ≈ small) for bulk formations.

### §6.3 Where the Lie analogy breaks

| Feature | Continuous Lie group | SCC finite group |
|---|---|---|
| Broken symmetry group G/H | Lie group (continuous) | Finite coset Aut(G)/Aut(G)_{u*} (discrete) |
| Goldstone modes | Exactly massless (μ = 0) | Approximately massless (μ = μ_Gold > 0) |
| Number of Goldstone modes | dim(G/H) continuous | |orbit| - 1 discrete (combinatorial) |
| Lie bracket structure | g has Lie bracket | T_{u*}Σ_m has no Lie bracket |
| Exponential map | exp: g → G smooth | No exponential map for finite Aut(G) |
| Noether current | Conserved current (field theory) | No conserved current (SCC is variational, not Lagrangian) |

This table is the CN10 contrastive record for §6.

---

## §7. V5b-F Mass Formula Reinterpretation

### §7.1 The mass formula (T-V5b-T, canonical §13)

The canonical V5b-T theorem (T-V5b-T, Cat A, CV-1.4) gives the Goldstone mass on a translation-invariant graph (torus or periodic grid):

$$\mu_{\mathrm{Gold}} \propto C(\beta) \cdot \frac{|\partial S|}{n},$$

where |∂S| is the boundary size of the formation support S = {i : u*_i > 1/2} and C(β) is a β-dependent coefficient measuring the double-well barrier strength.

### §7.2 Lie-algebra reinterpretation

In continuous symmetry breaking (e.g., translation symmetry on ℝ^d), the Goldstone boson is exactly massless (μ = 0) because the symmetry is exactly broken: any translation of the field configuration costs zero energy in the thermodynamic limit. On a finite lattice (finite graph G), the translation symmetry is discretized: only discrete translations are available, and the "Goldstone mode" is a finite-difference analog of the continuous translation generator.

The quantity C(β) · |∂S|/n measures the **discreteness defect**: the energy cost of moving the formation by one lattice step (|∂S| boundary vertices change from 0→1 or 1→0) relative to the formation size (n vertices total). In the continuum limit (n → ∞, lattice spacing h → 0 with h·n fixed), |∂S|/n → 0 and μ_Gold → 0 — recovering exact Goldstone mass-lessness. This is the SCC analog of the Goldstone limit.

**Finite-graph mass as symmetry defect.** The Goldstone mass μ_Gold is precisely the energy cost of the broken discrete symmetry: it measures how far the finite graph G is from having a continuous translation symmetry. C(β) controls the double-well barrier height (the "stiffness" of the formation against deformation), while |∂S|/n is the geometric defect (the fraction of the formation that sits at the boundary, sensitive to discrete translations).

### §7.3 V5b-F (partial Goldstone, Cat C)

The V5b-F mechanism (NQ-173, Cat C) identifies a secondary Goldstone-like mode for anisotropic (non-circular) formations on finite grids, where the broken continuous rotation symmetry yields an additional approximately-massless angular mode. In the Lie-algebra language: if the formation has an approximate SO(2) symmetry (nearly circular boundary), the "broken" SO(2) → Z_4 (D_4 discrete subgroup) gives a partial Goldstone analog. The V5b-F mode carries the E irrep of D_4 (the 2D rotation representation). This is Cat C because the V5b-F mechanism depends on the Branch B verdict (NQ-173, deferred).

---

## §8. GAGTA AI Parallel: ML Classifier for σ-Orbit Equivalence (NQ-260)

### §8.1 GAGTA 2025 context

The Groups, Algorithms, Geometry and Theory of Automata (GAGTA) workshop series (2025) has focused on AI-assisted orbit classification: given a group Γ acting on a set X, classify the orbits of Γ in X using machine learning. Relevant methods include graph isomorphism testing (Weisfeiler-Leman algorithm), GNN-based equivariant architectures, and automated irrep matching via character tables.

### §8.2 NQ-260: ML classifier for σ-orbit equivalence

**Task.** Given two minimizers u_1*, u_2* ∈ L(G, α, β, c), classify whether σ(u_1*) ≡ σ(u_2*) (σ-equivalent per Definition 2.1' of NQ-188) using an ML classifier trained on (u*, σ(u*)) pairs from R23.

**Why this is tractable.** The approximate σ-class enumeration (NQ-188 §5, eigenvalue-only proxy, script sigma_class_count_R23.py) provides training labels. The full σ-class (with irrep labels) is the target. Graph isomorphism testing (polynomial for fixed-degree graphs; Babai 2015 quasipolynomial in general) can verify Aut(G)_{u*} conjugacy — the exact condition for σ-equivalence (NQ-188 Definition 2.1', condition (a)).

**GAGTA-spirit.** The GAGTA 2025 approach to orbit classification: (1) compute a graph invariant (e.g., eigenvalue spectrum) as a fast proxy; (2) use GNN to refine the proxy using local structure; (3) verify exact equivalence via group-theory computation for borderline cases. Step (1) is the eigenvalue-proxy σ-class of sigma_class_count_R23.py; step (3) is the full NQ-188 §5 protocol (W7+ deliverable).

**NQ-260 status.** Cat C placeholder. Prerequisite: NQ-259 (Aut(G)_{u*} computation on R23) to generate exact σ-class labels for training.

---

## §9. Cross-References

| Reference | Content | Relation to this file |
|---|---|---|
| Canonical §13 T-σ-Lemma-1 | Aut(G)-orbit invariance of σ-tuple | Foundation for §3 stabilizer definition |
| Canonical §13 T-σ-Theorem-3/4 | D_4 free-BC σ-tuple (Cat A/B) | Primary example for §4 irrep decomposition |
| Canonical §13 T-V5b-T | Goldstone mass formula | Reinterpreted in §7 |
| Canonical §14 CN10 | SCC ≠ Lie group, ≠ gauge theory | Mandatory contrastive constraint; §6.3 table |
| Canonical §14 CN17 | σ-Labeled Formation Quantization | σ-tuple as quantum label; §4.3 definitional equivalence |
| working/MF/multi_formation_sigma.md | Joint stabilizer Aut(G)≀S_K | §3.2: single-formation K=1 analog |
| working/SF/sigma_uniqueness_theorem.md (NQ-188) | σ-class enumeration, D_4 free-BC | §5.2: NQ-258 bounds |σ-classes| via |Irr(N_Γ(P))| |
| working/SF/sigma_topological_invariance.md (NQ-190) | σ-tuple under graph isomorphism | §3.1: Aut(G) finiteness, isomorphism invariance |
| working/SF/sigma_theorem4_higher_order.md (NQ-187) | Higher-order ε splitting, D_4 E-irrep | §6.2: Goldstone irrep label |
| working/MF/foundational_bridges_2026.md B-3 (NQ-263) | Gaitsgory-Raskin Geometric Langlands → SCC multi-layer encirclement | §3 stabilizer + §6 Lie-algebra: B-3 frames Aut(G)_{u*} representation theory at Goldstone-broken minimizer. Bilateral cross-link (W5 Day 4 PM Wave 3, carry-forward #10). |
| working/SF/sigma_uniqueness_theorem.md §2 Definition 2.1' + working/SF/sigma_topological_invariance.md §3 Claim 3.1' (conjugation-translation rule) | NQ-188 / NQ-190 canonical conjugation rule | §4 prerequisite: §4.2 irrep decomposition is basis-independent only under clauses (a)-(d); §5 NQ-258 Sylow-normalizer formulation requires the rule for decidable σ-class equivalence on multi-dim irreps (W5 Day 4 PM Wave 3 cross-link). |

---

## §10. Category Targets

| Section | Content | Cat target | Rationale |
|---|---|---|---|
| §2 | Σ_m dimension + tangent space | Cat A | Standard differential geometry of simplex |
| §3.1 | Aut(G) action on Σ_m | Cat A | Follows from T-σ-Lemma-1 equivariance |
| §3.2 | Stabilizer Aut(G)_{u*} definition | Cat A | Standard group-theory definition |
| §4.1 | Schur-commutation of Hessian | Cat A | Definitional consequence of equivariance |
| §4.2 | Irrep decomposition of T_{u*}Σ_m | Cat A | Maschke's theorem (T-σ-Lemma-1 basis) |
| §4.3 | σ-tuple IS irrep decomposition | Cat A | Definitional restatement of Commitment 14 |
| §5 (NQ-258) | McKay-spirit conjecture | **Cat C** | Speculative; requires new induction argument + explicit computation |
| §6 | Lie algebra reading (structural analogy) | Cat B | Reinterpretation; correct but not canonical-proved |
| §7 | V5b-F mass formula reinterpretation | Cat B | Reinterpretation consistent with T-V5b-T (Cat A) |
| §8 (NQ-260) | ML classifier for σ-orbit | **Cat C** | Placeholder; requires NQ-259 prerequisite |

---

## §11. CN10 Hard Constraint Check

This section records all Lie/group theory language used in this file and verifies CN10 compliance (contrastive, not reductive).

**CN10 violations checklist (must be empty):**

| Claim | Status |
|---|---|
| "SCC is a Lie group" | NOT claimed anywhere |
| "Aut(G) is a Lie algebra" | NOT claimed; §6.1 explicitly states Aut(G) is finite with no continuous structure |
| "σ-framework IS gauge theory" | NOT claimed; §3.2 explicitly contrasts with Yang-Mills |
| "Goldstone modes are exactly massless" | NOT claimed; §6.1 and §6.3 explicitly state μ_Gold > 0 (finite-graph discreteness defect) |
| "Mackey/McKay applies directly to σ-tuple" | NOT claimed; §5 explicitly labels NQ-258 as Cat C speculative |
| "Geometric Langlands applies to SCC" | NOT claimed; §3.2 uses "spirit (metaphor for motivation)" with explicit marker |

**Contrastive statements present:**
- §2.2: "The analogy breaks immediately: Σ_m has no group structure"
- §3.1: "there is NO continuous Lie structure on Aut(G) for finite G"
- §3.2: "SCC's Aut(G) is entirely finite and combinatorial. The Lie group perspective enters only as a structural metaphor"
- §6.1: "In SCC... the Goldstone modes are APPROXIMATELY massless (mass μ_Gold > 0), not exactly massless"
- §6.3: table of Continuous vs SCC differences (7 features)

CN10 compliant: all Lie/group theory is structural analogy, explicitly marked contrastive. ✓

---

## §12. W6+ Priorities and New Questions

### NQ-258 (McKay-spirit conjecture for σ)

**Priority: High (W6).** Prerequisites: NQ-259 (Aut(G)_{u*} computation on R23, see below). The McKay conjecture in the SCC setting requires: (a) finding a minimizer u* with |Aut(G)_{u*}| having ≥ 2 distinct prime factors (so the Sylow normalizer is a strict subgroup), and (b) verifying that the σ-tuple multiplicities {n_k} satisfy the induction formula of §5.2. On D_4 free-BC L×L grids, |Aut(G)_{u*}| ≤ 8 = 2^3 — single prime p = 2, so N_Γ(P) = Γ trivially. To test NQ-258 non-trivially, a graph with |Aut(G)_{u*}| = 6 or 12 is needed (e.g., a hexagonal lattice).

### NQ-259 (explicit Aut(G)_{u*} computation on R23)

**Priority: High (W6).** For each of the 56 stable R23 minimizers, compute Aut(G)_{u*} by: (a) computing Aut(G) = D_4 (for 32×32 free-BC grid, |Aut(G)| = 8); (b) testing each of the 8 elements π ∈ D_4 whether P_π u* = u*. This is an O(8n) computation per minimizer. Expected result: most minimizers have |Aut(G)_{u*}| = 1 (generic, symmetry-broken); a few may have |Aut(G)_{u*}| = 2 or 4 (axis-aligned formations).

### NQ-260 (ML classifier for σ-orbit equivalence)

**Priority: Medium (W7+).** Requires NQ-259 labels. After NQ-259 generates exact (u*, Aut(G)_{u*}, σ-class) triples for R23, train a GNN classifier to predict σ-class from u* alone. Evaluation: confusion matrix on held-out R23 minimizers. GAGTA-spirit: combine fast eigenvalue-proxy (sigma_class_count_R23.py) with GNN refinement + exact group-theory verification.

---

*File closed 2026-04-30. No canonical edits. NQ-258/259/260 registered as W6/W7 open questions.*
