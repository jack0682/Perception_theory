---
type: working/prolegomena/formula-catalog
version: v0
date: 2026-05-23
status: Stage 1.5 — full formal candidate notation for M1-M44 (NOT committed)
purpose: |
  01 의 44개 prose 조건을 *candidate formal mathematical notation* 으로 정리.
  *committed definition 아님* — 표기는 변경 가능.
  PAI vocabulary (Δ_interp, IPF, PA-formation 등) 는 형식화하지 않음 (OP-PAI pending).
companions:
  - 01_mathematical_conditions_v0.md (prose source; M_k 와 일대일)
  - 02_framework_skeleton_v0.md (4-layer 위치)
  - 00_field_conditions_v0.md (perception-side 평행)
constraint_compliance:
  canonical_theorem_changes: 0
  claim_count: 102 (unchanged)
  CV_version: CV-1.20 (unchanged)
  scc_edits: 0
  new_vocabulary: 0 (existing prose의 formalization 만)
  PAI_vocabulary_formalized: 0 (Δ_interp 등 모두 placeholder)
  M_k_grade_changes: 0
  proofs: 0
  theorems: 0
  status: candidate formal notation (not committed)
---

> [!nav] Parent: [[../INDEX|working/INDEX.md]] · Companions: [[01_mathematical_conditions_v0|01 Prose Source]] · [[02_framework_skeleton_v0|02 4-Layer]] · [[00_field_conditions_v0|00 Perception-side]]

# Formula Catalog — Full Formal Candidate Notation for M1–M44

## §0 — 문서 위치 / status / hard constraints

**위치**: 01 의 prose conditions 를 *candidate formal mathematical notation* 으로 정리. 02 의 4-layer 분담은 *유지* (각 M_k 의 layer 위치는 02 §1 표 참조).

**Status: candidate**. 모든 정의는 *후보 표기*. 더 자연스러운 형식 발견 시 갱신 (notation 만; M_k 조건 자체는 01 그대로).

**Hard constraints**:
- canonical / DECLARATION / scc / theorem_status 무수정.
- M_k 등급 (N / S / O) 변경 0. 6 O-grade 는 *Formal status open* 마크 유지.
- PAI vocabulary (Δ_interp, IPF, PA-formation, Action Invariance, Shared Unit Principle, Meaningless Split) 의 *자체 형식 정의* 금지 — OP-PAI-001..006 의 미해결 대상.
- 새 vocabulary 도입 0. 정리 / 명제 / 증명 0.

**Per-entry 형식**: 각 M_k 는 *Signature* (한 줄 압축 표현) + *Definition* (~3-5 줄 형식 정의) + 필요 시 *Note* (O-grade 의 경우 *Formal status open* 사유). Inter-condition 의존은 §14 표에 별도.

---

## §1 — Shared notation key

**Categorical / set-theoretic**:
- 𝒞 — ambient category (substrate). Ob(𝒞), Mor(𝒞) 표준 표기.
- 𝒮 ∈ Ob(𝒞) — primitive structure object.
- 𝒪 — frame / context category. Ob(𝒪) = frames; Mor(𝒪) = partial morphisms.
- π : ℰ → 𝒪 — bundle over 𝒪. X^o := π⁻¹(o) 는 frame o ∈ Ob(𝒪) 위의 fiber.
- 𝒲 ∈ Ob(𝒞̄) — universal limit object ("world"); 𝒞̄ 는 𝒞 의 적당한 completion.
- ℒ — label category for type classification.
- 𝒮ub(𝒮) — substructure poset of 𝒮.
- G_o — groupoid or category of admissible transformations at frame o.

**Algebraic**:
- 𝒜 — *-algebra (C*- 또는 von Neumann).
- ω : 𝒜 → ℂ — state functional (positive normalized linear).
- 𝓗 — Hilbert space (GNS representation when relevant).
- 𝓗_bdry ⊂ ∂𝒮 — boundary degrees of freedom.

**Dynamical**:
- φ_t : 𝒮 → 𝒮 — autonomous flow.
- L : T𝒮 → 𝒮 — generator of φ_t (autonomous part).
- g : 𝒮 × 𝓗 → T𝒮 — multiplicative coupling functional.
- σ_t^ω ∈ Aut(𝒜) — Tomita-Takesaki modular automorphism group.
- H_ω — modular Hamiltonian (generator of σ_t^ω).

**Correlation / threshold**:
- C_o(τ) — autocorrelation function at frame o.
- C_A(τ) := ω(A_τ A_0) − ω(A)² — centered two-point correlation of observable A.
- Ω_o — pre-objective baseline (state functional).
- θ_O — objecthood threshold.

**SCC substrate (reuse without redefinition; canonical.md 참조)**:
- u_t : X_t → [0, 1], E_cl, E_sep, E_bd, E_tr, λ_2, W''(c) — 모두 SCC canonical 그대로.

**PAI placeholder symbols (RESERVED; not used in any formula below)**:
- Δ_interp(F), 𝓘_perc, 𝓘_act, 𝓐(u), d_PA — *signature 만*, OP-PAI-001..006 미해결.

---

## §2 — Category I: Negation (M1-M5)

### **M1** [N] — 𝒮 is not a Set morphism
- **Signature**: 𝒮 ∉ Mor(Set).
- **Definition**: ¬ ∃ A, B ∈ Ob(Set), f ∈ Hom_Set(A, B) such that 𝒮 = f. The data of 𝒮 is not specified by giving two sets and a function between them.
- **Note**: Forbids the "function on pre-given carrier" template that grounds most classical models.

### **M2** [N] — No primitive topology
- **Signature**: U : 𝒞 → Top is not a primitive datum.
- **Definition**: There is no input functor U : 𝒞 → Top assigning 𝒮 a topological space. Instead, ∃ derivation 𝒟 : 𝒞 → Top with 𝒟(𝒮) constructed from intrinsic data (e.g., correlation, spectrum, modular flow). Topology is a *derived invariant*.

### **M3** [N] — Flow in primitive datum
- **Signature**: ∃ φ = {φ_t}_{t ∈ ℝ}, φ_t ∈ Aut(𝒮), one-parameter group.
- **Definition**: 𝒮 carries a one-parameter automorphism group φ : ℝ × 𝒮 → 𝒮 with φ_0 = id_𝒮, φ_{s+t} = φ_s ∘ φ_t. Tangent functor τ satisfies τ((d/dt) φ_t|_{t=0, h=0}) ≢ 0_{T𝒮}. The flow belongs to *primitive* data, not derived from a static structure.

### **M4** [N] — No global section
- **Signature**: Γ_global(𝒮) = ∅.
- **Definition**: ¬ ∃ s ∈ Γ_global(𝒮) over the entire context category 𝒪. Only frame-local sections {s_o ∈ Γ(X^o)}_{o ∈ Ob(𝒪)} are admitted. Compatibility between distinct s_o is not required (Kochen-Specker analogue).

### **M5** [N] — Non-separability
- **Signature**: ¬ ∃ canonical iso 𝒮 ≅ A ⊗ B in 𝒞.
- **Definition**: ¬ ∃ A, B ∈ Ob(𝒞), iso 𝒮 ≅ A ⊗ B (canonical, not coincidental). The structure 𝒮 admits no canonical tensor decomposition into independently-defined sub-objects.

---

## §3 — Category II: Frame Indexing (M6-M9)

### **M6** [N] — Bundle section over frame
- **Signature**: π : ℰ → 𝒪 bundle; X^o := π⁻¹(o).
- **Definition**: All observables of 𝒮 are sections of a bundle π : ℰ → 𝒪 over the context category 𝒪. For o ∈ Ob(𝒪), the fiber X^o := π⁻¹(o) is the set of o-frame observables. Sections are defined frame-by-frame: s_o ∈ Γ(X^o).

### **M7** [N] — Partial morphisms only
- **Signature**: ¬ ∃ canonical iso between distinct o, o' ∈ Ob(𝒪).
- **Definition**: The category 𝒪 admits only *partial morphisms*: for o, o' ∈ Ob(𝒪), Hom_𝒪(o, o') may be empty, partial, or non-invertible. In general, ∄ canonical iso o ≅ o'.

### **M8** [S] — Frame is derived
- **Signature**: 𝒪 ∈ Out(theory), 𝒪 ∉ In(theory).
- **Definition**: The context category 𝒪 is *not* given as external input. 𝒪 is constructed within the theory from primitive data — candidates: 𝒪 = Spec(self-reference structure of 𝒮), or 𝒪 = state-selection groupoid via Connes-Rovelli thermal time, or 𝒪 = Doering-Isham context category V(𝒜). The precise construction is theory-specific and open (related to OP-NEW-B in 02 §6).

### **M9** [O] — Non-atomic frames
- **Signature**: Ob(𝒪) may include groupoids, 2-categories, colimits.
- **Definition**: Objects o ∈ Ob(𝒪) need not be atomic. Admissible o include: (a) groupoids, (b) 2-categories of sub-frames, (c) colimits of sub-frames.
- **Note**: *Formal status open* — the precise admissible class of non-atomic frames is unsettled.

---

## §4 — Category III: World Limit (M10-M14)

### **M10** [N] — Universal limit object
- **Signature**: ∃! 𝒲 ∈ Ob(𝒞̄), 𝒲 ≅ lim_{o ∈ 𝒪} X^o (up to canonical iso).
- **Definition**: In a completion 𝒞̄ of 𝒞, the limit 𝒲 = lim_{o ∈ 𝒪} X^o exists and is unique up to canonical isomorphism. 𝒲 plays the role of "world": the global object indexed by all frames. (Brunetti-Fredenhagen-Verch's inductive limit varinjlim A(O) instantiates this.)

### **M11** [N] — Universal property only
- **Signature**: 𝒲 specified solely by Hom_𝒞̄(-, 𝒲) (Yoneda).
- **Definition**: 𝒲 has no internal characterization (no formula for its elements). It is specified solely by its universal property: 𝒲 ≅ Y(𝒲) where Y : 𝒞̄ → Set^{𝒞̄^op} is the Yoneda embedding. Element-level access to 𝒲 is unavailable.

### **M12** [N] — Boundary coupling only
- **Signature**: External coupling h(t) ∈ 𝓗_bdry ⊂ ∂𝒮.
- **Definition**: External influence enters 𝒮 only as a boundary perturbation h(t) on 𝓗_bdry ⊂ ∂𝒮. No additive source term in the bulk equations. Coupling acts via ∂_t 𝒮 = L(𝒮) ⊙ (1 + g(h)) form rather than ∂_t 𝒮 = L(𝒮) + h(t).

### **M13** [N] — Multiplicative coupling
- **Signature**: L : T𝒮 → 𝒮 autonomous, L|_{h=0} ≢ 0; g : 𝒮 × 𝓗 → T𝒮 with g(·, 0) = 0.
- **Definition**: The dynamical generator L is non-vanishing at zero coupling: L|_{h=0} ≢ 0. Coupling enters multiplicatively through g : 𝒮 × 𝓗 → T𝒮 satisfying g(·, 0) = 0. Equivalently: d𝒮_t = L(𝒮_t) dt + g(𝒮_t) dh_t with the autonomous part L(𝒮) dt non-trivial.

### **M14** [S] — Decoupling limit
- **Signature**: ∃ regime such that ‖L‖ / ‖g(·, h)‖ → ∞.
- **Definition**: There exists a parametric regime in which ‖L(𝒮)‖ ≫ ‖g(𝒮, h)‖, providing a strong autonomy limit. In this limit, dynamics ∂_t 𝒮 = L(𝒮) is effectively decoupled from external h.

---

## §5 — Category IV: Autonomous Order (M15-M18)

### **M15** [N] — Autonomous flow non-trivial
- **Signature**: ∂_t ω(A)|_{h=0} ≢ 0 for some A ∈ 𝒜.
- **Definition**: At h = 0, the autonomous flow produces non-trivial time evolution: ∃ A ∈ 𝒜 such that t ↦ ω(A_t) is not constant. The system is not at static equilibrium under autonomous dynamics alone.

### **M16** [N] — Non-trivial invariant measure
- **Signature**: ∃ μ ∈ Inv(L), supp(μ) ≠ {pt}, H(μ) > 0.
- **Definition**: There exists an L-invariant probability measure μ on the state space Σ_state such that supp(μ) is not concentrated on a single point and the entropy H(μ) > 0. The baseline is not a Dirac mass.

### **M17** [N] — Baseline non-vanishing correlation
- **Signature**: ∀ A ∈ 𝒜_nonconst : C_A(τ) := ω(A_τ A_0) − ω(A)² ≢ 0.
- **Definition**: For every non-constant observable A ∈ 𝒜_nonconst, the centered two-point correlation C_A(τ) does not vanish identically. Some temporal correlation persists at all observable scales (baseline is not white noise).

### **M18** [O] — Generator axiomatic origin
- **Signature**: L is introduced as a primitive axiom; ¬ ∃ reduction R : ExternalData → L.
- **Definition**: The dynamical generator L is taken as a primitive axiom of the theory. There is no reduction from external constraints, prior physics, or empirical data. Formally: L ∈ AxiomSet(theory), and the map R : (prior structure) → L is not constructed.
- **Note**: *Formal status open* — the question of what selects L from a larger admissible class is unanswered.

---

## §6 — Category V: 1차 / 2차 Operation (M19-M22)

### **M19** [N] — First-order substructure generation
- **Signature**: 𝒮ub(𝒮) = Image(Op_1(L) : 𝒮 → 𝒮ub(𝒮)).
- **Definition**: Stable substructures (object-like invariants) are generated by a first-order operator Op_1 acting on 𝒮 via the generator L. The operation is direct (one application of L on 𝒮), not iterated or higher-order.

### **M20** [N] — Second-order classification functor
- **Signature**: Λ : 𝒮ub(𝒮) → ℒ functor.
- **Definition**: Type classification of substructures is a second-order functor Λ : 𝒮ub(𝒮) → ℒ, where ℒ is the label category. For F ∈ 𝒮ub(𝒮), Λ(F) ∈ Ob(ℒ) is its type label. Λ is functorial — preserves substructure inclusions.

### **M21** [N] — No distinguished label
- **Signature**: ℒ has no distinguished initial/terminal object; ¬ ∃ ⊥, ⊤ ∈ Ob(ℒ).
- **Definition**: The label category ℒ has neither distinguished initial (⊥) nor terminal (⊤) object. All labels in ℒ are a priori equivalent; no label has structural privilege.

### **M22** [S] — Decision invariants
- **Signature**: Λ-decision = (τ_pers, Cmp, χ).
- **Definition**: The classification Λ(F) of a substructure F is determined by three invariants:
  - (a) Persistence: τ_pers(F) := sup{T ≥ 0 : φ_t(F) ∼_𝒮 F for all t ∈ [0, T]}.
  - (b) Consistency: Cmp(F, F') := compatibility predicate for F' ∈ 𝒮ub(𝒮) co-existing with F.
  - (c) Responsiveness: χ_F(h) := δF / δh restricted to F's support domain.

---

## §7 — Category VI: Algebraic Setting (M23-M26)

### **M23** [S] — State as positive normalized functional
- **Signature**: ω ∈ S(𝒜) := {ω : 𝒜 → ℂ | linear, ω(a*a) ≥ 0 ∀ a, ω(1) = 1}.
- **Definition**: A state is a positive normalized linear functional ω on the *-algebra 𝒜. States are *not* required to be fixed Hilbert vectors; GNS construction recovers Hilbert representations when needed. (Algebraic QFT / Haag-Kastler convention.)

### **M24** [N] — Frame-indexed states, non-unique
- **Signature**: VAC := {ω_o ∈ S(𝒜) | ω_o satisfies B1-B3}_{o ∈ Ob(𝒪)}, |VAC / iso| > 1.
- **Definition**: Admissible baseline states (vacua / ground states) form a frame-indexed family VAC = {ω_o}_{o ∈ Ob(𝒪)} satisfying baseline axioms (B1 positivity, B2 normalization, B3 minimum-variance under L). Uniqueness fails: |VAC / iso| > 1 in general.

### **M25** [S] — Threshold structure
- **Signature**: ∃ θ_O > 0 : {ω ∈ S(𝒜) | 0 < ‖C_ω(τ)‖ < θ_O for some τ} ≠ ∅.
- **Definition**: There exists a threshold θ_O > 0 such that the baseline regime — states ω with autocorrelation C_ω(τ) strictly between 0 and θ_O — is non-empty. Separates pre-objective baselines from objecthood-emergent states.

### **M26** [S] — Substructure emergence condition
- **Signature**: (‖C_o‖ ≥ θ_O) ∧ G_o-Inv(F) ∧ Cohesion(F) ⟹ F ∈ 𝒮ub_stable(𝒮).
- **Definition**: When (a) the autocorrelation magnitude ‖C_o‖ crosses θ_O, (b) F is G_o-invariant, and (c) F satisfies spatial cohesion (compact support up to exponential decay), then F constitutes a *stable* substructure: F ∈ 𝒮ub_stable(𝒮).

---

## §8 — Category VII: Invariance Structure (M27-M30)

### **M27** [S] — Substructure identity by G_o-orbit
- **Signature**: Identity(F) := Orbit_{G_o}(F) ∈ 𝒮ub(𝒮) / G_o.
- **Definition**: The identity of a substructure F ∈ 𝒮ub(𝒮) is defined as its G_o-orbit: Identity(F) := {g · F : g ∈ G_o}. Two substructures F, F' represent the same identity iff F' ∈ Orbit_{G_o}(F). (Klein-Erlangen at the substructure level.)

### **M28** [S] — Groupoid (not group)
- **Signature**: G_o ∈ Ob(Cat) (not Grp); ∀ g ∈ Mor(G_o), invertibility not guaranteed.
- **Definition**: G_o is a groupoid or general category — not necessarily a group. Morphisms g ∈ Mor(G_o) need not have inverses. This admits asymmetric, irreversible transformations (e.g., time, memory recall, linguistic re-description).

### **M29** [O] — Cross-fiber invariance — **PAI core**
- **Signature**: ∃ M_cross ⊂ Mor(ℰ → ℰ) over distinct o ≠ o'; F invariant under M_cross-equivalence.
- **Definition**: There exists a class M_cross ⊂ Mor(ℰ) of morphisms between fibers of π over *distinct* base objects o ≠ o' (e.g., visual ↔ tactile modality shifts; Lorentz boost analogue). Substructures F are required to be M_cross-invariant: F ≡ M_cross(F).
- **Note**: *Formal status open* — **native model 부재**. 5 영역 (작용소대수 / 범주론 / 동역학 / 이산-관계론 / 정보-인지) 어디에도 *기본 구조 수준*에서 존재하지 않음. **PAI 핵심**: 02 §6 의 OP-NEW-C; PAI 수학화의 first real entry point.

### **M30** [O] — Partial coverage
- **Signature**: ∃ F ∈ 𝒮ub(𝒮) : supp(F) ⊂ ℰ' ⊊ ℰ over 𝒪' ⊊ Ob(𝒪).
- **Definition**: Some substructures F exist only over a sub-bundle ℰ' ⊊ ℰ rather than the full bundle — i.e., F is supported on a proper sub-collection of frames. Symmetry-breaking analogue: massive vs massless particle classes; partial modal coverage in perception.
- **Note**: *Formal status open* — admissible partial-coverage taxonomy not yet defined.

---

## §9 — Category VIII: Derived Structures (M31-M34)

### **M31** [S] — Spatial metric from correlation decay
- **Signature**: d(x, y) := −log ‖C(x, y)‖ + O((·)²), mod gauge.
- **Definition**: The spatial metric d : X × X → ℝ_≥0 is derived from the decay of cross-correlation: d(x, y) := −log ‖C(x, y)‖ + corrections, well-defined modulo a gauge choice (additive constant or local rescaling). Generalizations include Connes spectral distance d(x, y) = sup{|f(x) − f(y)| : ‖[D, f]‖ ≤ 1} and Ryu-Takayanagi-style mutual information.

### **M32** [O] — Modular time (Tomita-Takesaki)
- **Signature**: ∃ KMS_β state ω : ω(a σ_t^ω(b)) = ω(σ_{t − iβ}^ω(b) a), σ_t^ω ∈ Aut(𝒜).
- **Definition**: Temporal flow is induced by Tomita-Takesaki modular automorphism group σ_t^ω derived from a KMS state ω at inverse temperature β. The KMS condition ω(a σ_t^ω(b)) = ω(σ_{t − iβ}^ω(b) a) defines σ_t^ω uniquely (up to inner equivalence). Generator: H_ω = i (d/dt) σ_t^ω|_{t=0}.
- **Note**: *Formal status open* — applicability depends on the type of von Neumann algebra in which ω lives (Type I, II, III). Connes-Rovelli thermal time hypothesis (gr-qc/9406019) is the leading interpretation.

### **M33** [N] — Carrier derived
- **Signature**: X = spec(𝒜) or X = supp(ρ); X ∉ In(theory), X ∈ Out(theory).
- **Definition**: The underlying carrier X (where structures live — graph, manifold, discrete set) is *derived* from primitive data. Candidates: X = spec(𝒜) (Gelfand spectrum), X = supp(ρ) (Finster's causal fermion system measure), X = inductive limit of correlation graphs. X is not an input datum of the theory.

### **M34** [S] — Value space derived
- **Signature**: V := Compl({order relations from data}); [0, 1] ⊂ V as special case.
- **Definition**: The value space V (where field values live) is constructed as the completion of accumulated order relations from the data. The interval [0, 1] is a special case (totally ordered, bounded). V is not assumed primitive — it is the closure of measured comparisons.

---

## §10 — Category IX: Accessibility / Probing (M35-M39)

### **M35** [N] — Variational accessibility
- **Signature**: δ𝒮 / δh(t) ∈ T_𝒮 well-defined.
- **Definition**: The boundary deformation h ↦ h + δh induces a structural deformation δ𝒮 ∈ T_𝒮 (tangent space at 𝒮). The variational derivative δ𝒮 / δh(t) is well-defined as a functional derivative (Fréchet or Gateaux). Information about 𝒮 is accessible through boundary probing.

### **M36** [N] — Inter-frame morphism transmits comparison
- **Signature**: ∀ f : o → o' ∈ Mor(𝒪) : F(f) : X^o → X^{o'} carries comparison data.
- **Definition**: For every existing inter-frame morphism f ∈ Hom_𝒪(o, o'), the induced map F(f) : X^o → X^{o'} carries comparison information between frames. F is functorial: F(f' ∘ f) = F(f') ∘ F(f). When Hom_𝒪(o, o') = ∅, no comparison is possible (consistent with M7).

### **M37** [S] — Partial functor to standard categories
- **Signature**: ∃ F : 𝒞 → 𝒞', 𝒞' ∈ {Top, Prob, Cat}; F generally non-surjective, non-faithful.
- **Definition**: There exist partial functors F : 𝒞 → 𝒞' into standard categories (𝒞' ∈ {Top, Prob, Cat}). These are partial — F is generally non-surjective and non-faithful. No global embedding 𝒞 ↪ 𝒞' exists. Examples: Gelfand transform 𝒜 → C(spec(𝒜)), GNS construction ω ↦ (H_ω, π_ω, Ω_ω).

### **M38** [N] — Linear response (Kubo)
- **Signature**: χ_{AB}(τ) := δω(A_τ) / δh_B(0), well-defined and non-trivial.
- **Definition**: The linear response function χ_{AB}(τ) := δω(A_τ) / δh_B(0) is well-defined and non-trivial. This is the Kubo formula in standard form. Together with M17, fluctuation-dissipation theorem follows: χ_{AB}(τ) ↔ C_{AB}(τ) by Fourier-Laplace duality (with appropriate analyticity).

### **M39** [N] — Gödelian internal self-reference
- **Signature**: ∃ γ_𝒮 ∈ L_internal(𝒮) : γ_𝒮 ⟺ ¬Provable_𝒮(γ_𝒮).
- **Definition**: In the internal language L_internal of 𝒮, there exists a Gödelian sentence γ_𝒮 satisfying the self-referential fixed point γ_𝒮 ⟺ ¬Provable_𝒮(γ_𝒮). Equivalent categorical encoding: ¬ ∃ φ : A → B^A point-surjective in CCC such that all f : B → B have fixed points (Lawvere 1969).
- **Note**: *Formal status open* — concrete encoding depends on the internal logic of 𝒮; Lawvere fixed point theorem in CCC is the leading candidate (see 02 §5).

---

## §11 — Category X: Continuity / Integration (M40-M44)

### **M40** [S] — Continuous emergence
- **Signature**: E_emerge : Param → 𝒮ub(𝒮), continuous of order ≥ 2.
- **Definition**: The substructure emergence operator E_emerge : Param → 𝒮ub(𝒮), parametrized by control variables (β, α, T, etc.), is continuous of order ≥ 2 in some natural parametrization — i.e., second-order or higher phase transition. No discrete jumps at the emergence threshold. (Compatible with renormalization group critical exponents.)

### **M41** [N] — Integrated time slice
- **Signature**: ¬ ∃ ω_t^(1), ω_t^(2) : ω_t = ω_t^(1) ⊗ ω_t^(2) (canonical, not coincidental).
- **Definition**: At every time t, the state ω_t admits no canonical tensor decomposition ω_t = ω_t^(1) ⊗ ω_t^(2) into two independently-defined sub-states. The time slice is *integrated* (non-separable). Analogous to entanglement in quantum theory; consistent with M5 extended to the time axis.

### **M42** [S] — Distinguished generator (now)
- **Signature**: σ_t^ω has distinguished generator H_ω such that τ = 0 is well-defined in every representation.
- **Definition**: The modular automorphism group σ_t^ω possesses a distinguished generator H_ω = i (d/dt) σ_t^ω|_{t=0}, such that the current moment τ = 0 is well-defined in every state representation. This formalizes "now-ness" within the modular flow framework.

### **M43** [O] — Measurement as observable selection
- **Signature**: Meas : 𝒜 → 𝒜*, A ↦ ω(A · _).
- **Definition**: Measurement is formalized as the map Meas : 𝒜 → 𝒜* defined by A ↦ ω(A · _) — selecting a test observable A defines a linear functional on 𝒜. The measurement value is the functional ω(A · _) ∈ 𝒜*.
- **Note**: *Formal status open* — the precise category-theoretic structure of measurement (CP-map? process matrix? operator system morphism?) remains undecided. Choice depends on the measurement framework adopted.

### **M44** [S] — Time interval / germ / jet primitive
- **Signature**: ⟨ψ, ω⟩ := ∫_ℝ ψ(t) ω_t dt for ψ ∈ 𝒟(ℝ).
- **Definition**: The primitive temporal unit is an interval, germ, or jet — not a point. Observables are paired with time test functions: ⟨ψ, ω⟩ := ∫_ℝ ψ(t) ω_t dt for ψ ∈ 𝒟(ℝ) (compactly-supported smooth test functions). Point-valued time observation is recovered only as a limit (Dirac δ approximation). (Factorization algebra / histories formulation convention.)

---

## §12 — Open conditions (O-grade) summary

| M_k | Open 사유 (한 줄) |
|---|---|
| **M9** | Non-atomic frame 의 admissible class 미정 (groupoid? 2-cat? colimit?). |
| **M18** | L 의 origin 이 axiomatic — *어떤 axiom 이* selects L 의 reduction map 미구성. |
| **M29** | **Cross-fiber morphism class M_cross 의 native model 부재**. 5 영역 어디에도 없음. *PAI 핵심* (OP-NEW-C). |
| **M30** | Partial coverage taxonomy 미정의 — sub-bundle ℰ' 분류 체계 없음. |
| **M32** | Modular flow 적용은 ω 가 속한 von Neumann 대수 type (I, II, III) 의존; 일반론 미정. |
| **M43** | Measurement 의 category-theoretic 구조 미선택 (CP-map / process matrix / operator system 사이 결정 대기). |

6 O-grade 모두 *formal status open* 마크 유지. 본 문서에서 *해결 시도 0*.

---

## §13 — PAI vocabulary placeholder (NOT formalized)

본 문서는 *M_k 형식화* 에 한정. PAI 6 vocabulary 의 자체 형식 정의는 별도 작업 (OP-PAI-001..006 미해결).

| PAI vocabulary | Signature (placeholder) | Definition status |
|---|---|---|
| Δ_interp(F) | Δ_interp : 𝒮ub(𝒮) → ℝ_≥0 (또는 distance 구조) | OP-PAI-001 pending; 3 미정 component (𝓘_perc, 𝓘_act, d) |
| IPF (Interpretation-Preserving Formation) | IPF ⊂ 𝒮ub(𝒮) : high d_SCC ∧ small Δ_interp | OP-PAI-001 의존 |
| PA-formation | "cohesive unit usable for action without destructive re-tokenization" | prose only; OP-PAI-006 |
| Action Invariance | 3 candidate forms: equivariance / commutativity / low-distortion | OP-PAI-003 (choice not made) |
| Shared Unit Principle | thesis: min(perception unit) ≅ min(action interpretation unit) | thesis-level; 수학화 미결정 |
| Meaningless Split | negative target: fragmentation 이 perception-action invariance 보존하지 않음 | prose only |

**규칙**: 03 의 어느 M_k 정의도 Δ_interp / 𝓘_perc / 𝓘_act / 𝓐 / d_PA / IPF 를 사용하지 않음. 위 기호들은 *예약* (PAI 작업용).

---

## §14 — Inter-condition references

어느 M_k 가 어느 M_k 의 기호 / 구조를 사용하는지:

| M_k | 의존하는 M_k | 메커니즘 |
|---|---|---|
| M6 | M7 | bundle π 의 partial morphism 구조 |
| M10 | M6, M7 | world limit = lim_{o ∈ 𝒪} X^o 가 frame indexing 위에 |
| M11 | M10 | 𝒲 의 universal property 가 lim 의 정의 |
| M13 | M3, M12 | autonomous L 가 M3 의 flow, coupling g 가 M12 의 boundary |
| M15 | M3, M13 | autonomous flow 의 non-trivial 시간 evolution |
| M16, M17 | M15 | invariant measure / correlation 가 autonomous dynamics 의 결과 |
| M22 | M3, M19, M35 | τ_pers (flow), Cmp (substructure), χ (variational) |
| M23 | (basis for §7) | 모든 algebraic 설정의 출발 |
| M24, M25, M26 | M23 | state functional 위의 frame-family / threshold / emergence |
| M26 | M17, M25, M27 | C_o, θ_O, G_o-invariance |
| M27, M28 | M19 | substructure on Sub(𝒮); groupoid 작용 |
| M29 | M27, M28, M6 | cross-fiber 가 bundle 위 G_o-invariance 의 fiber 간 일반화 — **단 native model 부재** |
| M30 | M6, M27 | sub-bundle 위 partial G_o-invariance |
| M31 | M17 | correlation 으로부터 metric 유도 |
| M32 | M23, M42, M44 | modular flow 가 state 로부터 시간 유도 |
| M33 | M23, M31 | carrier 가 algebra spectrum 으로 derived |
| M34 | M33 | value space 가 carrier 위 order relations 의 completion |
| M38 | M17, M35 | linear response 가 fluctuation-dissipation 통해 correlation 과 연결 |
| M39 | M37 | internal language 위의 self-reference (categorical 인코딩) |
| M41 | M5 | non-separability 의 시간축 확장 |
| M42 | M32 | modular flow 의 generator |
| M44 | M3, M32 | flow / modular flow 의 jet/germ primitive 형태 |

(완전한 의존 그래프는 별도 시각화 작업 — 본 plan 외.)

---

## §15 — 본 문서가 *하지 않는* 것

- M_k 등급 (N / S / O) 변경. 01 그대로.
- 새 M_{k > 44} 추가. 44 개 catalog 고정.
- PAI vocabulary (Δ_interp, IPF 등) 의 자체 정의. §13 placeholder 만.
- canonical.md / DECLARATION.md / theorem_status.md / scc/ 수정.
- *committed* formal definition 주장. 모든 정의는 *candidate notation*; 갱신 가능.
- 정리 / 명제 / 증명. 03 은 *형식 catalog* 일 뿐.
- 5 OP-NEW (02 §6) 의 해결. 명시만.
- 4-layer (02) 의 *layer-by-layer* 형식화. 본 문서는 *M_k 별* 형식화; layer 별은 02 §1 참조.

---

## §16 — Changelog

- **v0 (2026-05-23)**: 44 M_k 의 full formal candidate notation 초안. 6 O-grade *Formal status open* 마크. PAI 6 vocabulary placeholder (§13). Inter-condition reference 표 (§14). canonical / scc / theorem_status 무수정.

---

*Formula Catalog v0 — 2026-05-23. 44 M_k full formal candidate notation. 정리 0. 명제 0. 증명 0. 새 OP 등록 0. PAI vocabulary 형식화 0. canonical / scc 무수정. CV-1.20 그대로. 102 claims 그대로. 모든 정의는 candidate — committed 아님.*
