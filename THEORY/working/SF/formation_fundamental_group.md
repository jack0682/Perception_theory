# formation_fundamental_group.md — Formation Fundamental Group π_1(F) (NQ-263 Working File)

> **⚠️ PARTIAL RETIRE-CANDIDATE (W6 D1 EOD parking-lot Issue #4 audit, 2026-05-04)**
> **Retire scope:** Geometric Langlands apparatus framing (étale π_1, profinite completion, Galois cohomology, dual group, categorical equivalence) — entirely absent from SCC's strictly finite-graph setting; Gaitsgory-Raskin 2024 framing is heuristic motivation only.
> **Preserve scope:** (1) **Definition 3.1**: $\pi_1(F; u^*) := \mathrm{Aut}(G)_{u^*}$ (formation fundamental group as the stabilizer subgroup of $\mathrm{Aut}(G)$ at minimizer $u^*$) — SCC-intrinsic finite-group invariant; (2) **Worked examples §5, §6** on $C_n, T^2_L, R23$; (3) **σ-class enumeration consequence** (orbit-counting application to NQ-188).
> **Important framing**: $\pi_1(F)$ as defined IS just the stabilizer $\mathrm{Aut}(G)_{u^*}$, a standard finite-group object — NOT a fundamental group in any topological sense. The "$\pi_1$" label is **marketing** borrowed from Geometric Langlands framing; the mathematics is **orbit algebra**, equivalent to NQ-188's stabilizer-based σ-class enumeration.
> **Future split (W7+ recommended):** absorb Definition 3.1 + worked examples into `working/SF/sigma_uniqueness_theorem.md` (which already handles NQ-188 σ-class enumeration via Aut(G)_{u*} stabilizer, so this would consolidate). Retire Langlands apparatus framing + Gaitsgory-Raskin references to `_archive/cv17_speculative_retired_2026-05-04/`.
> **4 active inbound references** (op003_mo1_status_review, sigma_class_category, parking_lot_inventory, WAVE3_MASTER_INDEX) → split must preserve link integrity (sigma_class_category itself is FULL RETIRE candidate; op003 is index-only).
> **CN10 disclosure**: SCC π_1(F) as "stabilizer subgroup of Aut(G)" is well-defined finite-group object. The "fundamental group" naming evokes algebraic-topology / Geometric-Langlands intuition that does NOT apply (no continuous loop space, no profinite completion). Naming should be reconsidered: `Stab(F)` or `Aut(F; u*)` would be more precise; `π_1(F)` is misleading. **Recommend renaming in W7+ split.**

**Status:** working draft (Wave 3 NEW theoretical work, 2026-04-30, W5 Day 4 PM).
**Created:** 2026-04-30 by team-lead@scc-wave3-deep-research, Task #24 (formal definition).
**Author origin:** Direct spawn from `working/MF/foundational_bridges_2026.md` §4 Bridge B-3 (Gaitsgory-Raskin Geometric Langlands ↔ SCC multi-layer encirclement). Bridge B-3 proposed NQ-263 as the formal-definition target; this file delivers the definition + worked examples + σ-class enumeration consequence.
**Canonical refs:** §11.1 Commitment 14 (σ-tuple definition); §11.1 Commitment 17 (proposed, Tool A2 quotient picture); §13 T-σ-Lemma-1 (Aut(G)-equivariance); §13 T-σ-Theorem-3/4 (D_4 free-BC σ-tuple); §14 CN10 (contrastive vs reductive); §14 CN17 (σ-Labeled Formation Quantization).
**Working refs:** `working/MF/foundational_bridges_2026.md` §4 Bridge B-3 (NQ-263 source); `working/SF/sigma_lie_algebra_structure.md` §3 (Aut(G)_{u*} stabilizer); `working/SF/sigma_uniqueness_theorem.md` §2 Definition 2.1' (NQ-188 conjugation rule); `working/MF/mathematical_scaffolding_4tools.md` (Tool A2 finite-group quotient).
**External refs:** Gaitsgory, D. and Raskin, S. (2024) "The geometric Langlands conjecture (proof outline)," arXiv:2405.03648 (✅ verified, plus 4 companions); Drinfeld, V.G. (1980) "Langlands' conjecture for GL(2) over functional fields"; Serre, J.-P. (1977) *Linear Representations of Finite Groups*, Springer; Hatcher, A. (2002) *Algebraic Topology*, Cambridge UP §1.1 (fundamental group of based loop space).

**Hard constraints (CN10 + Commitment 17 dependency):**
- SCC is NOT Geometric Langlands. π_1(F) here is a **finite-group analog** of a fundamental group acting on a moduli space; it is NOT the étale fundamental group of an algebraic curve nor the Langlands π_1 of a function field. All Langlands references are STRUCTURAL ANALOGIES (CN10).
- Cat target: **C** — depends on Tool A2 canonical promotion at CV-1.6 via proposed Commitment 17. Until then, π_1(F) is well-defined definitionally but the moduli-space framing is a candidate, not a theorem.
- Direct canonical edits: 0. NQ-263 is W7+ priority (8-12 weeks effort) per `foundational_bridges_2026.md` §10.
- Open problems (F-1, M-1, MO-1, OP-0005, OP-0008, OP-0009) are NOT silently resolved. NQ-258 McKay-spirit (`sigma_lie_algebra_structure.md` §5) is independent and remains Cat C.

---

## §1. Mission

**Bridge B-3 (Geometric Langlands spirit) — define π_1(F) for SCC formations.** This file delivers the formal definition of the **formation fundamental group** π_1(F; u*) := Aut(G)_{u*}, the local automorphism stabilizer of a fixed reference σ-class minimizer u* ∈ Σ_m. The definition realizes the Bridge B-3 program (`foundational_bridges_2026.md` §4): import the *spirit* of Geometric Langlands (a fundamental group acting on moduli stacks of bundles) into the SCC σ-framework via the Tool A2 finite-group quotient, without claiming SCC reduces to Langlands theory.

**Three deliverables.**

1. **Formal definition (§3).** π_1(F; u*) is the stabilizer subgroup of Aut(G) at u*, a finite group acting faithfully on the σ-tuple irrep components ρ_k of T_{u*}Σ_m (Tool A2 quotient picture).
2. **Worked examples (§5).** Explicit π_1 computation on R23 (D_4 free-BC) and 1D Z_n cycle, both at the uniform configuration u_uniform and at the first pitchfork minimizer u*_pitchfork.
3. **σ-class enumeration consequence (§6).** σ-class count on R23 (NQ-188) ↔ orbit decomposition of the minimizer set L(G, α, β, c) under π_1(F) action, connecting to the McKay-spirit conjecture (NQ-258).

**Contrastive position (CN10).** Geometric Langlands π_1 is the étale fundamental group of an algebraic curve C/F_q acting on the moduli stack Bun_G(C) of G-bundles on C; it is profinite and arises from algebraic geometry over function fields. SCC's π_1(F; u*) is a **finite group** Aut(G)_{u*} acting on the **finite minimizer set** L (or equivalently the irrep components of the discrete tangent space T_{u*}Σ_m); it is purely combinatorial. The shared *spirit* is: a fundamental group encodes loops in a moduli-like space, and acts on the representation-theoretic data attached to each point. SCC borrows this organizational principle, not the underlying algebraic-geometric machinery.

---

## §2. Background — Geometric Langlands π_1 and Moduli Stacks of Bundles

### §2.1 Source statement (Gaitsgory-Raskin 2024)

The geometric Langlands conjecture (Gaitsgory-Raskin 2024, arXiv:2405.03648, ✅ verified per `foundational_bridges_2026.md` §12) establishes an equivalence of categories between:

- **Automorphic side.** D-modules (or perverse sheaves) on the moduli stack Bun_G(C) of G-bundles on a smooth projective curve C over F_q.
- **Spectral side.** Quasi-coherent sheaves on the moduli stack LocSys_{G^∨}(C) of G^∨-local systems on C, where G^∨ is the Langlands dual group.

The étale fundamental group π_1^ét(C, c̄) of the curve (with respect to a geometric point c̄) acts on both sides via Galois representations, and the equivalence is π_1-equivariant. The moduli stacks Bun_G(C) and LocSys_{G^∨}(C) thus carry compatible π_1-actions, organizing the representation data into orbits indexed by Galois cohomology.

### §2.2 Spirit imported into SCC

The structural lesson from Gaitsgory-Raskin 2024 relevant to SCC is **multi-layer encirclement**: organize representation-theoretic data (irreps, characters) on a moduli space (configuration space of formations) via a fundamental group encoding loops/symmetries.

| Geometric Langlands (Gaitsgory-Raskin 2024) | SCC analog (this file) |
|---|---|
| Curve C / F_q | Graph G (finite) |
| Moduli stack Bun_G(C) | Minimizer set L(G, α, β, c) ⊂ Σ_m ; or Tool A1 stratified-space $\widetilde\Sigma^K_M$ |
| Étale fundamental group π_1^ét(C, c̄) (profinite) | Formation fundamental group π_1(F; u*) := Aut(G)_{u*} (finite) |
| Galois action on Bun_G(C) | Aut(G)_{u*}-action on σ-tuple irreps ρ_k (Tool A2 quotient) |
| π_1-equivariant equivalence Bun_G ↔ LocSys_{G^∨} | π_1(F)-equivariant decomposition of T_{u*}Σ_m as Aut(G)_{u*}-module |

The SCC analog is **strictly finite**: G is a finite graph, Aut(G) is a finite group, and Aut(G)_{u*} ≤ Aut(G) is a finite subgroup. There is no profinite completion, no Galois cohomology, no algebraic stack. The borrowed spirit is the *organizational principle* of a fundamental group acting on representation data.

### §2.3 CN10 contrastive checkpoint

| Feature | Geometric Langlands | SCC π_1(F; u*) |
|---|---|---|
| Underlying space | Algebraic curve C / F_q (continuous, geometric) | Finite graph G (discrete, combinatorial) |
| Group type | Profinite étale π_1 | Finite stabilizer subgroup |
| Moduli object | Algebraic stack Bun_G(C) | Finite minimizer set L or Tool A1 strata |
| Equivalence target | Categorical (D-modules ↔ QCoh) | Representation-theoretic (irrep decomposition of T_{u*}Σ_m) |
| Galois action | Yes | No (no field extension; Aut(G) replaces Gal) |
| Dual group | Langlands dual G^∨ | None (no duality claim) |

**SCC is not Geometric Langlands.** The dual-group structure (G ↔ G^∨) is absent in SCC; π_1(F) is one-sided. This is the principal CN10 contrast.

---

## §3. Definition — π_1(F; u*) := Aut(G)_{u*}

### §3.1 The definition

**Definition 3.1 (formation fundamental group).** Let G = (X, E) be a finite connected graph. Let u* ∈ Σ_m^∘ be a fixed reference σ-class minimizer (a representative of an equivalence class under σ-equivalence per `sigma_uniqueness_theorem.md` §2 Definition 2.1'). Define the **formation fundamental group based at u*** by

$$\pi_1(\mathcal{F}; u^*) := \mathrm{Aut}(G)_{u^*} = \{\pi \in \mathrm{Aut}(G) : P_\pi u^* = u^*\},$$

the local automorphism stabilizer of u* under the permutation action P_π of Aut(G) on ℝ^n.

**Properties (immediate).**

- (P1) π_1(F; u*) is a finite group: subgroup of the finite group Aut(G), hence |π_1(F; u*)| divides |Aut(G)| ≤ n!.
- (P2) Conjugation between σ-equivalent base points: if u_2* = π · u_1* for π ∈ Aut(G), then π_1(F; u_2*) = π · π_1(F; u_1*) · π^{-1} (conjugate subgroups of Aut(G)). Hence the conjugacy class [π_1(F; u*)] is a σ-class invariant — `sigma_uniqueness_theorem.md` §2 Definition 2.1' clause (a).
- (P3) π_1(F; u_uniform) = Aut(G) when u_uniform is the constant configuration (full automorphism preservation). At the symmetry-broken pitchfork u*_pitchfork, π_1 is a strict subgroup.

### §3.2 Faithful action on σ-tuple irrep components

By the Schur-commutation lemma (`sigma_lie_algebra_structure.md` §4.1), the Hessian H(u*)|_{T_{u*}Σ_m} commutes with the Aut(G)_{u*} action on T_{u*}Σ_m. By Maschke's theorem and Schur's lemma (Serre 1977 §2.2), the tangent space decomposes:

$$T_{u^*}\Sigma_m \cong \bigoplus_{k=1}^{K_{\mathrm{irr}}} V_{\rho_k}^{\oplus n_k},$$

where ρ_k ∈ Irr(π_1(F; u*)) are the irreducible representations of π_1(F; u*) and n_k are multiplicities. The σ-tuple

$$\sigma(u^*) = \big(\mathcal{F}(u^*);\ \{(n_k, [\rho_k], \lambda_k)\}_{k=1}^{K_{\mathrm{irr}}}\big)$$

(Commitment 14, canonical §11.1) is precisely the irrep-decomposition data of T_{u*}Σ_m as a π_1(F; u*)-module, augmented by the Hessian eigenvalues λ_k on each irrep block.

**Faithfulness.** The action of π_1(F; u*) on the direct sum ⊕_k V_{ρ_k}^{⊕n_k} is faithful: a non-trivial π ∈ π_1(F; u*) acts non-trivially on at least one irrep block ρ_k (since the regular representation of any non-trivial finite group is faithful, and T_{u*}Σ_m contains every irrep with multiplicity at least the dimension of the irrep on the regular representation, restricted to the n-1 dimensional tangent space).

**Tool A2 quotient picture.** The faithful action realizes the Tool A2 finite-group quotient (`mathematical_scaffolding_4tools.md`): the σ-tuple is the quotient datum

$$T_{u^*}\Sigma_m \;\big/\; \pi_1(\mathcal{F}; u^*) \;=\; \{[\rho_k], n_k, \lambda_k\}_k$$

— the orbit-and-eigenvalue decomposition of the tangent space under the formation fundamental group. This is the SCC analog of the π_1-equivariant decomposition of Bun_G(C) in Gaitsgory-Raskin 2024 (§2.2 table row 4).

### §3.3 Loops in formation moduli space ↔ symmetry-group elements

In algebraic-geometric Langlands theory, π_1^ét(C, c̄) is generated by classes of loops (étale paths) at the base point c̄. In the SCC finite-group analog, the "loops" are interpreted as follows:

**Definition 3.2 (formation loop, heuristic).** A *loop in formation moduli space at u*** is an automorphism π ∈ π_1(F; u*) ⊆ Aut(G), interpreted as a permutation of the support set X that fixes u* setwise (P_π u* = u*) and hence returns the configuration to itself after the action. The "loop" traces the orbit X → π·X = X with u* invariant.

This is a finite-group analog of based loops in topology: π_1^top(Y, y*) is the group of homotopy classes of continuous loops [0,1] → Y with γ(0) = γ(1) = y*. In SCC, "homotopy" is replaced by "graph automorphism," and "continuous loop" by "discrete permutation cycle."

**No fundamental polygon.** Unlike a topological space where π_1 is generated by 2g loops on a genus-g surface, π_1(F; u*) here is determined directly by the combinatorial symmetry of the graph G and the symmetry-breaking pattern at u*. There is no continuous generation; the group structure is given as a finite presentation inherited from Aut(G).

---

## §4. Cat Target — Cat C, Depending on Commitment 17 Promotion

### §4.1 Cat C target

**Cat target: C (conditional, dependent on Tool A2 canonical promotion).**

Per `foundational_bridges_2026.md` §10, NQ-263 is rated Cat C with W7+ effort (8-12 weeks). The Cat C status reflects:

1. **Definitional content is Cat A.** The definition π_1(F; u*) := Aut(G)_{u*} is a definitional restatement of the existing stabilizer subgroup (already used in `sigma_lie_algebra_structure.md` §3.2, `sigma_uniqueness_theorem.md` §2 Definition 2.1', NQ-190 Claim 3.1). No new mathematical content beyond renaming and framing.

2. **Moduli-space framing is Cat C.** The interpretation of L(G, α, β, c) as a "moduli space" of formations, with π_1(F) acting via the Tool A2 quotient, depends on the canonical promotion of Commitment 17 (proposed at CV-1.6, currently in `working/MF/shared_pool_canonical_proposal.md` and `working/MF/K_status_commitment.md`). Until Commitment 17 is promoted, the moduli-space framing is a candidate, not a canonical theorem.

3. **Geometric Langlands parallel is structural only (CN10).** The Bridge B-3 spirit imports organizational principle, never theorems. No transfer of Langlands results to SCC is claimed.

### §4.2 Promotion gate

Before NQ-263 enters CV-1.6 packet:
1. Commitment 17 (Tool A2 quotient picture) must be canonical-promoted.
2. NQ-258 McKay-spirit (`sigma_lie_algebra_structure.md` §5) should be at least Cat B (explicit example with |π_1(F; u*)| ≥ 6).
3. NQ-259 (explicit Aut(G)_{u*} computation on R23, prerequisite per `sigma_lie_algebra_structure.md` §12) must be complete with the 56 R23 minimizer stabilizers tabulated.
4. CN10 contrastive language re-verified post-promotion.

### §4.3 Effort estimate

8-12 weeks per `foundational_bridges_2026.md` §10. Breakdown:
- 2-3 weeks: NQ-259 prerequisite (Aut(G)_{u*} computation on R23).
- 2-3 weeks: Commitment 17 promotion review.
- 2-3 weeks: §5 worked examples expansion (R23 + 1D cycle + 2D torus benchmarks).
- 2-3 weeks: §6 σ-class enumeration consequence + NQ-258 cross-validation.

---

## §5. Worked Examples

### §5.1 R23: D_4 free-BC 32×32 grid

**Graph G_{R23}.** 32×32 free-BC grid with Aut(G_{R23}) = D_4 (dihedral group of order 8: 4 rotations + 4 reflections). Per `sigma_lie_algebra_structure.md` §3.1 and T-σ-Theorem-3/4 (canonical §13).

**Base point u_uniform = (m/n) · 1.** The constant configuration with u_i = m/n for all i. All π ∈ Aut(G_{R23}) = D_4 fix u_uniform setwise, hence

$$\pi_1(\mathcal{F}; u_{\mathrm{uniform}}) = \mathrm{Aut}(G_{R23}) = D_4 \quad \text{(order 8, full graph automorphism group)}.$$

The σ-tuple at u_uniform decomposes T_{u_uniform}Σ_m into the 5 D_4 irreps {A_1, A_2, B_1, B_2, E} (Mulliken order). Multiplicities n_k follow the regular-representation decomposition restricted to the n-1 dimensional tangent space.

**Base point u*_pitchfork (first pitchfork minimizer).** At β slightly above β_crit^(2), the first non-trivial minimizer u*_pitchfork breaks a reflection symmetry while preserving the perpendicular reflection axis. By T-σ-Theorem-4 (i'), the residual stabilizer is the order-2 subgroup ⟨s_y⟩ ≤ D_4 (or a conjugate ⟨r^k s_y r^{-k}⟩ for k ∈ {0, 1, 2, 3}). Specifically, an axis-aligned single-disk minimizer along the y = const axis yields:

$$\pi_1(\mathcal{F}; u^*_{\mathrm{pitchfork}}) = \langle s_y \rangle \cong \mathbb{Z}_2 \quad \text{(order 2)}.$$

**Refined claim — π_1 = D_2 for axis-aligned higher-symmetry pitchforks.** For a minimizer that preserves both the x-axis and y-axis reflections (e.g., a centered single-disk maintained by the vertical and horizontal mirror planes), the residual stabilizer is the Klein four-group D_2 = ⟨s_x, s_y⟩ ≅ Z_2 × Z_2 of order 4. This is the axis-aligned subgroup of D_4 indicated in the task definition.

| Base point | π_1(F; u*) | Order | Index in Aut(G) | Residual irreps |
|---|---|---|---|---|
| u_uniform | D_4 | 8 | 1 | {A_1, A_2, B_1, B_2, E} (5 irreps) |
| u*_pitchfork (D_2-axis aligned) | D_2 = Z_2 × Z_2 | 4 | 2 | {(++), (+-), (-+), (--)} (4 irreps) |
| u*_pitchfork (Z_2-single mirror) | Z_2 | 2 | 4 | {[+1], [-1]} (2 irreps) |
| u*_generic (broken full) | {1} (trivial) | 1 | 8 | {[trivial]} (1 irrep) |

**σ-class enumeration on R23 (preview, NQ-188 cross-link).** The 56 stable R23 minimizers (`CODE/scripts/results/exp_orbital_fullscale.json`) partition into σ-classes whose count is bounded by the number of distinct π_1(F; u*) conjugacy-class types appearing across L_{R23}. From `sigma_lie_algebra_structure.md` §12 NQ-259: most R23 minimizers have |π_1| = 1 (generic, fully symmetry-broken); a few have |π_1| ∈ {2, 4} (axis-aligned formations). The exact distribution is the NQ-259 deliverable.

### §5.2 1D Z_n cycle: dihedral D_n stabilizer

**Graph G_{cycle,n}.** n-vertex cycle C_n with Aut(C_n) = D_n (dihedral group of order 2n: n rotations + n reflections, for n ≥ 3).

**Base point u_uniform.** Constant u_i = m/n. All π ∈ D_n fix u_uniform setwise, hence

$$\pi_1(\mathcal{F}; u_{\mathrm{uniform}}) = D_n \quad \text{(order 2n, full Aut(C_n))}.$$

The tangent space T_{u_uniform}Σ_m decomposes into D_n irreps via the standard Fourier decomposition: 1D irreps {A, B} (for n even) or {A} (for n odd), plus 2D irreps E_ℓ for ℓ = 1, …, ⌊(n-1)/2⌋ (rotation-eigenvalue pairs).

**Base point u*_pitchfork (first pitchfork on cycle).** At the first instability, a single low-frequency Fourier mode condenses (e.g., the ℓ = 1 cosine mode produces a single-bump minimizer). The residual stabilizer is the reflection across the bump axis:

$$\pi_1(\mathcal{F}; u^*_{\mathrm{pitchfork}}) = \langle s \rangle \cong \mathbb{Z}_2 \quad \text{(order 2)}.$$

This is the SCC analog of breaking continuous SO(2) → Z_2 in classical pattern formation, except SO(2) is replaced by the discrete D_n.

| Base point | π_1(F; u*) | Order | Index in Aut(C_n) |
|---|---|---|---|
| u_uniform | D_n | 2n | 1 |
| u*_pitchfork (ℓ=1 single-bump) | Z_2 | 2 | n |

**Note on n = 2.** For n = 2 (degenerate cycle K_2), Aut(K_2) = S_2 = Z_2 itself; π_1(F; u*) ∈ {Z_2, {1}} only. The σ-framework on n = 2 is degenerate (open problem F-1, K=2 vacuity, canonical §14); π_1(F) does not silently resolve F-1.

### §5.3 2D torus Z_n × Z_n (W7+ extension)

**Graph G_{torus,n}.** n × n periodic-BC grid with Aut(G_{torus,n}) ⊇ (Z_n × Z_n) ⋊ D_4 (translation × dihedral). Order = 8n².

**Base point u_uniform.** π_1(F; u_uniform) = full automorphism group, order 8n².

**Base point u*_pitchfork (single-disk on torus).** The translation symmetry is broken (single localized disk), but the D_4 dihedral is preserved if the disk is centered. Hence

$$\pi_1(\mathcal{F}; u^*_{\mathrm{pitchfork,torus}}) = D_4 \quad \text{(order 8, only the dihedral residue)}.$$

This example shows that π_1(F) on the torus is **strictly smaller** than at u_uniform but **strictly larger** than the R23 free-BC analog at the same φ structure: torus translations are broken but D_4 is preserved, whereas free-BC R23 already had only D_4 from the start.

---

## §6. σ-Class Enumeration via π_1(F)

### §6.1 σ-class ↔ orbit decomposition under π_1(F) action

The σ-class count |σ-classes(G, α, β, c)| (NQ-188, `sigma_uniqueness_theorem.md` §2 Definition 2.1') equals the number of distinct σ-tuples appearing in L(G, α, β, c). Per §3.2 above and `sigma_lie_algebra_structure.md` §4.3, the σ-tuple at u* is determined by:

(σ1) The conjugacy class [π_1(F; u*)] of the formation fundamental group as a subgroup of Aut(G).
(σ2) The irrep decomposition of T_{u*}Σ_m as a π_1(F; u*)-module: multiplicities n_k of each ρ_k ∈ Irr(π_1(F; u*)).
(σ3) The Hessian eigenvalues λ_k on each irrep block.
(σ4) The local-maxima count F(u*).

**Claim 6.1 (σ-class ↔ π_1-orbit decomposition).** The σ-class count satisfies:

$$|\sigma\text{-classes}(G, \alpha, \beta, c)| = \big|\{[\pi_1(\mathcal{F}; u^*)] : u^* \in \mathcal{L}\} \times \{(n_k, \lambda_k)\}\big| \;/\; \mathrm{Aut}(G)\text{-conjugation},$$

i.e., σ-classes are in bijection with pairs (conjugacy class of π_1, irrep multiplicity + eigenvalue data) modulo Aut(G)-conjugation.

This generalizes Lemma 3.2 of `sigma_uniqueness_theorem.md` (Aut(G)-orbit ⊆ σ-class): every σ-class is a union of Aut(G)-orbits sharing the same π_1 conjugacy-class label.

### §6.2 Connection to NQ-188 R23 enumeration

For R23 with 56 stable minimizers and Aut(G_{R23}) = D_4 of order 8, the possible π_1(F; u*) types are subgroups of D_4 (up to conjugacy):

$$\{1\}, \;\langle s \rangle \cong \mathbb{Z}_2, \;\langle r^2 \rangle \cong \mathbb{Z}_2, \;\langle r \rangle \cong \mathbb{Z}_4, \;\langle s, r^2\rangle \cong D_2, \;D_4 \quad \text{(6 conjugacy classes of subgroups)}.$$

Hence the σ-class count on R23 is **bounded by 6 × (eigenvalue-multiplicity count)**, where the eigenvalue-multiplicity factor is empirically O(10) per `sigma_lie_algebra_structure.md` §5.2 NQ-258 estimate. This gives a heuristic upper bound |σ-classes(R23)| ≲ 60, consistent with the 56 distinct approx σ-classes from `CODE/scripts/sigma_class_count_R23.py`.

### §6.3 Connection to NQ-258 McKay-spirit

The NQ-258 McKay-spirit conjecture (`sigma_lie_algebra_structure.md` §5) proposes that σ-tuple irrep multiplicities are determined by the Sylow normalizer N_{π_1(F)}(P) for a Sylow p-subgroup P. In the π_1(F)-language of this file:

- For R23 with π_1(F; u*) = D_4 of order 8 = 2^3, p = 2, P = D_4 (single prime), so N_{π_1}(P) = π_1 trivially. NQ-258 is vacuous on R23 D_4 stabilizers.
- For graphs where π_1(F; u*) has multiple prime factors (e.g., a hexagonal lattice with π_1 of order 6 = 2·3 or 12 = 4·3), NQ-258 becomes non-vacuous and predicts σ-tuple multiplicities from Sylow normalizers.
- This file's π_1(F) framing makes the NQ-258 prerequisite explicit: NQ-258 requires graphs with multi-prime |π_1(F; u*)|, i.e., the formation fundamental group must have non-trivial Sylow structure.

---

## §7. W6+ Priority — NQ-263 Cat C, 8-12 Weeks

| Question | Cat | Effort | Priority | W-band |
|---|---|---|---|---|
| NQ-263 (this file) — define π_1(F) on R23 + Z_n cycle | C | 8-12 weeks | MEDIUM | W7+ |
| NQ-258 prerequisite — McKay-spirit non-vacuous example | C → B | 4-6 weeks | HIGH | W6 |
| NQ-259 prerequisite — Aut(G)_{u*} R23 computation | A | 2-3 weeks | HIGH | W6 |
| NQ-263 extension — 2D torus + hexagonal lattice π_1 | C | 6-8 weeks | LOW | W8+ |
| NQ-263 extension — π_1-equivariant cohomology of L | C | 12+ weeks | LOW | W9+ |

**Promotion target:** none direct. NQ-263 is W7+ exploratory per `foundational_bridges_2026.md` §10; promotion gate at §4.2 above. Earliest CV-1.6+ canonical packet candidate (after Commitment 17 promotion).

---

## §8. Hard Constraint Verification (CN10 + u_t Primitive)

**u_t primitive maintained.** All formulations respect u_t : X_t → [0,1] as the SCC primitive entity. The σ-tuple irrep components ρ_k act on the **tangent space** T_{u*}Σ_m of the cohesion-field configuration space at u*; π_1(F; u*) acts on the cohesion field and its perturbations, not on any independent algebraic-geometric object.

**CN10 contrastive (SCC ≠ Geometric Langlands).** Recorded throughout:
- §1 mission: "π_1(F) here is a finite-group analog... NOT the étale fundamental group of an algebraic curve nor the Langlands π_1 of a function field."
- §2.3 contrastive table: 6-row comparison Geometric Langlands vs SCC π_1(F).
- §3.3 finite-group analog of based loops: "No fundamental polygon... no continuous generation."
- §6.3 NQ-258 cross-link: McKay conjecture in finite-group setting only, not Langlands McKay.

**4-energy not merged.** π_1(F) acts on the Hessian H(u*) of the full energy E = λ_cl·E_cl + λ_sep·E_sep + λ_bd·E_bd + λ_tr·E_tr; the 4 conceptually independent energy terms are preserved.

**No silent resolution of open problems.**
- F-1 (K=2 vacuity): §5.2 explicitly notes π_1(F) does not resolve F-1 on n=2 cycles.
- M-1 (K=1 preference): unaffected; π_1(F; u*) for K=1 minimizer is well-defined regardless.
- MO-1 (Morse inapplicability): unaffected; π_1(F) is defined via stabilizer subgroup, independent of Morse-theoretic structure.
- OP-0005 (K-Selection): unaffected; π_1(F) is defined per minimizer, agnostic to K-selection axiom.
- OP-0008 (σ^A K-jump non-determinism): the multi-formation π_1(F) extension to π_1(F; **u**) for K-fields is W7+ exploratory; not addressed in this file.
- OP-0009 (Multi-Formation Ontological Foundations): unaffected; this file is single-formation only.

**No canonical edits.** Direct canonical edits: 0. NQ-263 is W7+ working-file content; CV-1.6+ promotion gated by §4.2.

**CN10 violations checklist (must be empty).**

| Claim | Status |
|---|---|
| "SCC IS Geometric Langlands" | NOT claimed; §2.3, §3.3, §6.3 explicitly contrastive |
| "π_1(F; u*) IS étale π_1" | NOT claimed; §1, §3.1 explicitly finite-group analog |
| "Aut(G) IS Galois group" | NOT claimed; §2.2 table row 5: "no Galois action" |
| "Bun_G(C) ↔ L(G, α, β, c)" structural identification | Imported as STRUCTURAL ANALOGY only (§2.2 table); no theorem transfer |
| "Langlands dual G^∨ exists in SCC" | NOT claimed; §2.3 last row: "SCC π_1(F) is one-sided." |

CN10 compliant. ✓

---

## §9. References

### §9.1 External

- **Gaitsgory, D. and Raskin, S. (2024).** "The geometric Langlands conjecture (proof outline)." arXiv:2405.03648. ✅ verified per `foundational_bridges_2026.md` §12.1. Bridge B-3 source.
- **Drinfeld, V.G. (1980).** "Langlands' conjecture for GL(2) over functional fields." Foundational reference for Langlands ↔ moduli of bundles framework.
- **Serre, J.-P. (1977).** *Linear Representations of Finite Groups.* Springer GTM 42. §2.2 Schur's Lemma; §3 character theory; basis for §3.2 faithful-action argument.
- **Hatcher, A. (2002).** *Algebraic Topology.* Cambridge UP. §1.1 fundamental group of based loop space; SCC's §3.3 finite-group analog.

### §9.2 Working files (SCC internal)

- **`working/MF/foundational_bridges_2026.md` §4 Bridge B-3.** NQ-263 source; this file is the §4 deliverable.
- **`working/SF/sigma_lie_algebra_structure.md` §3 Aut(G)_{u*} stabilizer.** Definitional foundation; this file's §3 inherits the stabilizer definition.
- **`working/SF/sigma_uniqueness_theorem.md` §2 Definition 2.1' conjugation rule.** §3.1 (P2) and §6.1 inherit the σ-equivalence-by-conjugation framing.
- **`working/SF/sigma_topological_invariance.md` §3 Claim 3.1'.** Inter-graph version of §6.1 σ-class ↔ π_1 orbit correspondence.
- **`working/MF/mathematical_scaffolding_4tools.md` Tool A2.** Finite-group quotient picture, this file's §3.2 realization.
- **`working/MF/multi_formation_sigma.md` §1.4 joint stabilizer Aut(G)≀S_K.** Multi-formation extension of π_1(F) (W7+ deferred).

### §9.3 Canonical (no edits proposed)

- §11.1 Commitment 14 — σ-tuple definition; this file's §3.2 representation-theoretic restatement.
- §11.1 Commitment 17 (proposed) — Tool A2 quotient picture; §4.1 dependency.
- §13 T-σ-Lemma-1 — Aut(G)-equivariance; §3.2 Schur-commutation prerequisite.
- §13 T-σ-Theorem-3/4 — D_4 free-BC σ-tuple; §5.1 example basis.
- §14 CN10 — contrastive vs reductive; §8 verification.
- §14 CN17 — σ-Labeled Formation Quantization; π_1(F) framing aligned.

---

## §10. Cross-References

| Reference | Content | Relation to this file |
|---|---|---|
| `foundational_bridges_2026.md` §4 Bridge B-3 (NQ-263) | Gaitsgory-Raskin 2024 → SCC multi-layer encirclement | **Primary source.** This file is the §4 NQ-263 formal-definition deliverable. |
| `sigma_lie_algebra_structure.md` §3 Aut(G)_{u*} | Stabilizer subgroup, Lie-algebra reading | §3 inherits stabilizer definition; §3.2 uses §4 Schur-commutation. |
| `sigma_lie_algebra_structure.md` §5 NQ-258 McKay-spirit | Sylow-normalizer determination of σ-tuple | §6.3 cross-validates: π_1(F) framing makes NQ-258 prerequisite explicit (multi-prime |π_1|). |
| `sigma_lie_algebra_structure.md` §12 NQ-259 | Aut(G)_{u*} R23 computation | §4.2 promotion gate; §5.1 R23 example data source. |
| `sigma_uniqueness_theorem.md` §2 Definition 2.1' | NQ-188 conjugation rule | §3.1 (P2) inherits clauses (a)-(d); §6.1 σ-class ↔ π_1 orbit correspondence. |
| `sigma_topological_invariance.md` §3 Claim 3.1' | NQ-190 inter-graph σ-invariance | §6.1 inter-graph version (W7+ extension). |
| `mathematical_scaffolding_4tools.md` Tool A2 | Finite-group quotient | §3.2 realization. |
| `multi_formation_sigma.md` §1.4 Aut(G)≀S_K | Multi-formation joint stabilizer | π_1(F; **u**) for K-field — W7+ exploratory (OP-0009). |
| `working/MF/foundational_bridges_2026.md` B-2 (NQ-262) | Schramm locality of σ at first pitchfork | §5.1 R23 first-pitchfork π_1 = D_2 example: NQ-262's "locality theorem" hypothesis. Bilateral cross-link. |
| `working/SF/schramm_sigma_locality_theorem.md` (Wave 3, in flight) | NQ-262 Cat BC formulation | §5.1 first pitchfork π_1 corresponds to NQ-262 "local automorphism stabilizer" (`foundational_bridges_2026.md` §3.3 step 1). |

---

*File closed 2026-04-30. No canonical edits. NQ-263 registered as W7+ exploratory; Cat C target conditional on Commitment 17 promotion. Bilateral cross-links to `foundational_bridges_2026.md` §4 (Bridge B-3 source), `sigma_lie_algebra_structure.md` §3/§5/§12, `sigma_uniqueness_theorem.md` §2 (NQ-188 conjugation rule), and Wave 3 in-flight `schramm_sigma_locality_theorem.md` (NQ-262 locality).*
