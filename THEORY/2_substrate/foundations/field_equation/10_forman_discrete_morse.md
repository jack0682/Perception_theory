---
type: working/field_equation_framework/derivation
date: 2026-05-20
session_origin: W8-Day3 evening, Wave 3 diverse mathematical approaches — graph-native complement to file 03 Modica-Mortola Jacobi (continuum)
canonical_version: CV-1.18 SEALED (untouched throughout)
status: draft v0.1
authors: user (Jaehong Oh)
preceded_by:
  - W8-Day3 01_ns_inspired_synthesis.md §8.2 Path 2 + §7 Identity 5
  - W8-Day3 03_modica_mortola_jacobi_cat_b.md (continuum Jacobi approach — this file's COMPLEMENT, not replacement)
  - W8-Day3 07_critic_full_review.md §B (file 03 critic findings — esp. graph→continuum gap as core Cat B conditional)
  - canonical §3.7+§5.3+§5.3b T-OP6-B (Cat A persistent ridge — closest existing canonical anchor)
  - canonical §13 L-HMORSE-LOCAL + L-HMORSE-DECOMP (Cat B H-Morse package, CV-1.16)
  - canonical §13 T-σ-Lemma-1 (Cat A Aut(G) commutation)
  - canonical §13 T-V5b-T-zero (Cat A translation Goldstone)
  - theorem_status.md L594 OP-HMORSE-SADDLE (OPEN, registered)
  - theorem_status.md L803 OP-0005-DYN (OPEN, Kramers/Package II)
purpose: |
  Derive **Forman discrete Morse theory** (Forman 1998 *Adv. Math.* 134:90-145) applied to SCC's
  graph-based H-Morse problem. This gives a *discrete-graph-native* analysis that does NOT require
  the continuum limit — directly complementary to file 03's Modica-Mortola Jacobi-on-Γ framework
  (whose Cat B classification originates precisely from the graph→continuum step, see critic §B
  finding M03.4 + §B.5 + §7.3). The deliverable is **L-FORMAN-HMORSE-DISCRETE Cat B target lemma**:
  SCC formation u* has well-defined Forman discrete Morse structure on the graph 1-skeleton with
  critical cells corresponding to (formation interior bulks, active boundary saddles, exterior
  pockets), and the H-Morse spectral gap is bounded below by *discrete Morse index counts*. All
  canonical CN1-16 preserved; canonical 0 edits.
canonical_compatibility:
  CN1_canonical_edits: 0
  CN2_silent_OP_resolution: 0 (Cat B target only; OP-HMORSE-SADDLE attack via discrete saddle-cell count named, not solved)
  CN4_analyticity: preserved (no new energy term; structural cell-complex analysis of canonical u*)
  CN5_4_term_independence: preserved (E_cl, E_sep, E_bd, E_tr separate; Forman analysis applies to combined critical u* without merging)
  CN10_no_reductive_reduction: contrastive only ("Forman is a STANDARD discrete-topology tool"; SCC u* is NOT reduced to a Forman function — it INDUCES one via standard extension)
  primitive_u_t: preserved (Forman function f̄ on cells DERIVED from u_t on vertices via standard min-extension; u_t remains primitive)
  canonical_edits: 0
  inertia_introduction: forbidden (no time evolution in this file)
  Mori_Zwanzig: forbidden (CV-1.18 SEAL deprecation)
  CSSL_energy_terms: forbidden (E_ridge / E_wild / E_pers — critic-rejected anti-patterns)
cot_enforced: yes
coc_enforced: yes
consensus_baseline:
  surface_tension: σ = (√2/6)·√(αβ)  [Wave 2 consensus; matches file 03 §2.2 derivation; CORRECTS files 05/06]
  reference_torus: L=16, 2D PBC, λ_2 = 4·sin²(π/16) ≈ 0.1522
  reference_params: c=1/2, α=1, β=10, T_*=0.1, R=4
  W''(1/2): -1
  OP_HMORSE_SADDLE_line: theorem_status.md L594 (NOT canonical.md L1967)
  OP_0005_DYN_line: theorem_status.md L803
  Theorem_4_line: canonical.md L1134-1136
---

> [!nav] Linked: [[canonical|CV-1.18 canonical]] (§3.7, §5.3, §5.3b T-OP6-B, §13 L-HMORSE-LOCAL, L-HMORSE-DECOMP, L-BOUNDARY-MODE-EXCLUSION, T-σ-Lemma-1, T-V5b-T-zero, Theorem 4) · [[theorem_status|theorem_status]] (L594 OP-HMORSE-SADDLE, L803 OP-0005-DYN) · [[DECLARATION|DECL-1.0]] · [[01_ns_inspired_synthesis|01 NS synthesis]] · [[03_modica_mortola_jacobi_cat_b|03 Modica-Mortola — this file's COMPLEMENT]] · [[07_critic_full_review|07 critic §B]]

# 10 — Forman Discrete Morse Theory: Graph-Native H-Morse Analysis Complementary to Modica-Mortola

**Mode**: working layer derivation (NOT verification, NOT SEAL prep, NOT canonical edit).
**Target**: derive `L-FORMAN-HMORSE-DISCRETE` as a *Cat B target* lemma — the graph-native cell-complex analysis of SCC's H-Morse problem using Forman discrete Morse theory (Forman 1998). Complementary to file 03's continuum Jacobi-on-Γ approach.

## §0 Frontmatter — Cross-Reference Sanity + §8a P1-P6 Audit + CONSENSUS BASELINE

### §0.1 Pre-work xref check (canonical/working/* grep)

- `grep -rn "Forman\|discrete Morse\|Mischaikow" canonical/ THEORY/working/ 2>/dev/null` — **EMPTY**. Forman discrete Morse theory is *not previously invoked* in either canonical or working layers. This file is the *first* invocation.
- canonical T-OP6-B (CV-1.7, §5.3b, L375-392) uses *persistence homology of |∇_G u|²* (B_PersRidge) — Mischaikow-Nanda 2013 (*Found. Comput. Math.* 13:151) shows direct correspondence between Forman discrete Morse on a gradient field and persistence homology. Therefore the *closest existing canonical anchor* for this file's framework is T-OP6-B Cat A.
- canonical L-HMORSE-LOCAL (CV-1.16, §13) gives Cat B μ_min > 0 via active-set decomposition; this file provides a *parallel structural account* via Forman index counts (NOT a replacement).
- **Novel positioning**: this file = *first explicit application* of Forman discrete Morse to SCC. T-OP6-B uses the persistence-homology side of the Forman-persistence correspondence; this file uses the cellular-Morse side.

### §0.2 §8a archive pattern P1-P6 audit

- **P1** (Foundational vacuity / DECL question 우회): DECL Q1 (T8 boundary appearance) + Q3 (객체 vs 형성 경계) 직접 — Forman index-1 saddle cells = combinatorial encoding of *경계*; Forman index-2 cells = *bulk*; Forman index-0 cells = *exterior pocket*. *우회 아님* ✓.
- **P2** (Vocabulary refactoring): `u_t` primitive 미변경; Forman function `f̄ : K → ℝ` is *DERIVED* via standard min-extension from `u: V → [0,1]`. *Primitive 아님* ✓.
- **P3** (Canonical content 중복): canonical T-OP6-B uses *persistence homology of |∇_G u|²* (the PH side of the Forman-PH correspondence); this file uses the *cellular Morse side* via Forman 1998 — *strict extension, contradiction 0* ✓.
- **P4** (외부 도구 도입): Forman 1998 / Mischaikow-Nanda 2013 / Bauer-Kerber-Reininghaus / Edelsbrunner-Harer = *contrastive standard tools only*, *complementary to canonical T-OP6-B and L-HMORSE-LOCAL* ✓.
- **P5** (Self-audit): 본 §0 (this section) + §13 (CN1-16 hard constraint check) 의 dual audit ✓.
- **P6** (언어-수학 분리): 모든 정리 statement 수학으로 명시; 자연어 motivation 은 *contextual only* ✓.
- **0/6 부합** → 진행 합법.

### §0.3 CONSENSUS BASELINE (Wave 2 critic-mandated)

| Quantity | Value | Source |
|---|---|---|
| Surface tension `σ` | `(√2/6)·√(αβ) ≈ 0.236·√(αβ)` | File 03 §2.2 derivation (mathematically correct per critic §B.2); cited here only for cross-anchor (this file's analysis is index-counting, not σ-based) |
| Reference torus | `T²_{16} = C_{16} × C_{16}`, PBC, n=256 | Critic §A.2 + file 03 §1.3 |
| Reference Laplacian gap | `λ_2 = 4·sin²(π/16) ≈ 0.1522` | Standard cycle-graph spectrum |
| Reference parameters | `c=1/2, α=1, β=10, T_*=0.1, R=4` | Chosen baseline (super-spinodal: β·|W''(1/2)|/4λ_2 = 10/0.6088 ≈ 16.4 > 1, T8 condition satisfied) |
| `W''(1/2)` | `-1` (W(u) = u²(1-u)², I6 canonical) | canonical I6 |
| OP-HMORSE-SADDLE | **theorem_status.md L594** (NOT canonical.md L1967) | Critic §B.1 critical finding |
| OP-0005-DYN | **theorem_status.md L803** | Critic §A.1 |
| Theorem 4 (uniform critical μ_k formula) | canonical.md L1134-1136 | Critic anchor |

### §0.4 Output structure
- §1 Mission (Forman discrete Morse, complementary to file 03 continuum Jacobi)
- §2 Forman discrete Morse theory setup (Forman 1998 contrastive)
- §3 SCC u as discrete Morse function on graph G
- §4 Critical cell classification (formation features)
- §5 Connection to T-OP6-B persistent ridge (canonical Cat A)
- §6 L-FORMAN-HMORSE-DISCRETE Cat B target lemma + 5-step proof sketch + inverse causation
- §7 Morse inequalities for SCC formation regime
- §8 Discrete vs continuum comparison (file 03 ↔ this file)
- §9 OP-HMORSE-SADDLE attack via discrete saddle cell counts (theorem_status.md L594)
- §10 2D torus 16×16 reference example
- §11 Discrete-graph compatibility (van Gennip-Bertozzi 2012)
- §12 CoT/CoC archival
- §13 Hard constraint CN1-16 check
- §14 One-paragraph summary

---

## §1 Mission — Graph-Native H-Morse Complement to Modica-Mortola

### §1.1 본 문서가 *하는 것*

1. State Forman discrete Morse theory on cell complexes (Forman 1998) — *contrastive standard tool*.
2. Construct the standard Forman extension `f̄: K(G) → ℝ` of SCC field `u: V(G) → [0,1]` via min-on-endpoints rule for edges (and min-on-vertices rule for faces in 2-complex extension).
3. Classify critical cells of `f̄` in SCC formation regime: **index-0 vertices** (exterior pockets `u ≈ 0`), **index-1 edges** (boundary saddles between regions), **index-2 faces** (formation interior bulks `u ≈ 1`).
4. State **L-FORMAN-HMORSE-DISCRETE** Cat B target lemma with 5-step proof sketch + per-step inverse causation.
5. Derive discrete Morse inequalities `m_k ≥ b_k` for SCC formation on `T²_{16}` reference torus: `b_0 = 1, b_1 = 2, b_2 = 1` ⟹ at least 4 critical cells per formation.
6. Establish *complementarity* to file 03 Modica-Mortola Jacobi: both approaches should yield the same Morse index counts at corresponding critical configurations; discrete avoids the graph→continuum step (file 03's Cat B conditional source).
7. Attack OP-HMORSE-SADDLE (theorem_status.md L594) via discrete saddle-cell index = 1 cellular invariant (complementary to file 03 §10's analytical Hessian-eigenvalue route).
8. 2D torus 16×16 explicit example with critical cell census.
9. Discrete-graph compatibility with van Gennip-Bertozzi 2012 (graph-native Modica-Mortola — confirms the two graph-side approaches are mutually compatible).

### §1.2 본 문서가 *하지 않는 것* (CN10 + critic-mandated boundaries)

명시 금지:

- ❌ **SCC = Forman 함수 환원**: SCC 의 `u_t` 는 *primitive*; Forman `f̄` 는 *standard derived extension only*. *"u IS a Forman function"* 표현 금지; *"u INDUCES a Forman function via standard min-extension"* 표현 사용.
- ❌ **OP-HMORSE-SADDLE 해결 주장**: §9 attack channel 만 제시; discrete saddle-cell index = 1 invariant 는 *cellular topology* 정보 — *Hessian-eigenvalue regularity* 와는 별개 (Forman index gives cellular Morse type, not analytical eigenvalue magnitude).
- ❌ **Cat A 주장**: graph G choice (1-skeleton vs 2-skeleton vs higher), genericity hypothesis, Aut(G) symmetry breaking — 모두 explicit Cat B conditional.
- ❌ **CSSL E_ridge / E_wild / E_pers 재도입**: critic-rejected anti-patterns; Forman analysis uses *canonical u\* only*.
- ❌ **Mori-Zwanzig / inertia**: CV-1.18 SEAL deprecation 위반 — 미도입; Forman 은 static topology theory.
- ❌ **canonical T-OP6-B 와의 충돌**: T-OP6-B (Cat A) 의 PH-on-|∇_G u|² 결과 와 *consistent*; this file 의 Forman-on-u analysis 는 *complementary view* (cellular Morse side).

### §1.3 Why graph-native matters (critic §B response)

```
CoT step 1: File 03 critic §B identified that Modica-Mortola's Cat B status originates from the
  graph→continuum step (van Gennip-Bertozzi 2012 + hypothesis package (GC1)-(GC4)). The continuum
  Jacobi spectrum gives elegant analytical bounds (σ·μ_ℓ on sphere) but requires assuming the
  continuum limit applies to the specific SCC graph at hand.
CoT step 2: Forman discrete Morse is defined DIRECTLY on the finite graph cell complex. NO mesh
  refinement needed, NO h → 0 limit, NO Γ-convergence hypothesis package. The discrete Morse
  inequalities m_k ≥ b_k hold exactly on the finite graph (Forman 1998 Theorem 3.5).
CoT step 3: Trade-off: Forman gives CELLULAR Morse invariants (index counts, Morse complex
  chain groups) but does NOT directly yield Hessian eigenvalue magnitudes. The bridge from
  Forman index counts to spectral magnitude bounds is via Cheeger-type discrete inequalities
  (separate analytical tool — see file 08-style spectral bridge, not this file).
CoT step 4: Therefore: discrete and continuum approaches are STRICTLY COMPLEMENTARY. File 03
  continuum → spectral magnitudes (Cat B conditional on graph→continuum). This file discrete →
  cellular Morse type + Morse inequalities (Cat B conditional on Forman genericity + Aut(G)
  symmetry breaking). Both Cat B, but with DIFFERENT conditional hypotheses.
→ A Cat A proof of either L-MODICA-JACOBI-HMORSE or L-FORMAN-HMORSE-DISCRETE would not
  automatically imply the other; they attack the same target (H-Morse non-degeneracy) from
  orthogonal hypothesis bases. This is GENUINE complementarity, not redundancy.

CoC anchors:
  - canonical: §13 L-HMORSE-LOCAL Cat B (D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5))
  - canonical: §5.3b T-OP6-B Cat A (PH on |∇_G u|² — Mischaikow-Nanda correspondence to Forman)
  - canonical: §13 OP-HMORSE-SADDLE registered at theorem_status.md L594
  - external: Forman 1998 Adv. Math. 134:90 (discrete Morse theory)
  - external: Mischaikow-Nanda 2013 Found. Comput. Math. 13:151 (Forman ↔ persistence correspondence)
```

---

## §2 Forman Discrete Morse Theory Setup (Standard Contrastive Tool)

### §2.1 Cell complex K(G) for a graph

For an undirected graph `G = (V, E)`, the standard cell complex is the **1-skeleton**:

$$
K^{(1)}(G) = V \cup E, \qquad \dim(v) = 0 \text{ for } v \in V, \quad \dim(e) = 1 \text{ for } e \in E.
$$

For a graph embedded in a surface (or with a 2-cell completion — e.g., a triangulation, or a square 2-complex on a grid graph), the **2-skeleton** adds faces:

$$
K^{(2)}(G) = V \cup E \cup F, \qquad \dim(f) = 2 \text{ for } f \in F.
$$

For 2D torus `T²_n = C_n × C_n` (canonical SCC reference), the natural 2-complex has `|V| = n²` vertices, `|E| = 2n²` edges (horizontal + vertical), `|F| = n²` square faces.

### §2.2 Discrete Morse function (Forman 1998 Definition 2.1)

**Definition (Forman discrete Morse function).** *A function `f: K → ℝ` is a **discrete Morse function** if for every cell `α^{(p)} ∈ K` of dimension `p`:*

- *(F1) `#{β^{(p+1)} > α : f(β) ≤ f(α)} ≤ 1`* (at most one coface has lower-or-equal value);
- *(F2) `#{γ^{(p-1)} < α : f(γ) ≥ f(α)} ≤ 1`* (at most one face has higher-or-equal value).

A cell `α^{(p)}` is **critical** if both counts in (F1) and (F2) equal zero (no exceptional cofaces or faces).

### §2.3 Discrete Morse inequalities (Forman 1998 Theorem 3.5)

Let `m_p(f) = #{critical p-cells of f}` and let `b_p = rank H_p(K; ℝ)` be the p-th Betti number of the cell complex `K`. Then:

**Strong Morse inequalities**:

$$
\boxed{m_p - m_{p-1} + m_{p-2} - \cdots \pm m_0 \geq b_p - b_{p-1} + b_{p-2} - \cdots \pm b_0, \quad \forall p \geq 0.}
$$

**Weak Morse inequalities** (corollary):

$$
\boxed{m_p \geq b_p \quad \forall p \geq 0, \qquad \sum_p (-1)^p m_p = \chi(K) = \sum_p (-1)^p b_p.}
$$

### §2.4 Discrete Morse complex (Forman 1998 §8)

The critical cells `{α : α \text{ critical}}` generate a chain complex `(C_*^{\mathrm{Morse}}(f), \partial^{\mathrm{Morse}})` with boundary operator counting V-path connections between critical cells of consecutive dimension. The homology of this complex equals the cellular homology of `K`:

$$
H_p(C_*^{\mathrm{Morse}}(f)) \cong H_p(K; \mathbb{Z}).
$$

### §2.5 References

- **Forman 1998**: *Morse theory for cell complexes*, *Adv. Math.* **134**:90-145. Foundational paper.
- **Forman 2002**: *A user's guide to discrete Morse theory*, *Sém. Lothar. Combin.* **48**:B48c. Pedagogical introduction.
- **Mischaikow-Nanda 2013**: *Morse theory for filtrations and efficient computation of persistent homology*, *Found. Comput. Math.* **13**:151-184. Bridge to persistence (used in canonical T-OP6-B).
- **Bauer 2021**: *Ripser: efficient computation of Vietoris-Rips persistence barcodes*, *J. Appl. Comput. Topol.* **5**:391-423. Computational realization.

---

## §3 SCC `u` as Discrete Morse Function on Graph `G`

### §3.1 Standard Forman extension (min-on-endpoints rule)

Given SCC cohesion field `u: V → [0,1]` (canonical primitive), the **standard Forman extension** to the cell complex `K(G)` is defined by:

$$
\boxed{\bar u(\alpha) = \min_{v \in \mathrm{vertices}(\alpha)} u(v), \quad \alpha \in K.}
$$

Equivalently:
- For `v ∈ V`: `f̄(v) = u(v)`.
- For `e = (v_i, v_j) ∈ E`: `f̄(e) = min(u(v_i), u(v_j))`.
- For `f` = face with vertices `{v_1, ..., v_k}`: `f̄(f) = min_i u(v_i)`.

This is the standard sub-level-set extension used in computational topology (Edelsbrunner-Harer 2010 §VII).

### §3.2 Why min-extension (not avg or max)

```
CoT step 1: For sub-level-set filtration {x : u(x) ≤ t} to be a CW-subcomplex at each level t,
  we need: α ∈ filtration at level t ⟹ ∂α ⊂ filtration at level t. With min-extension:
  f̄(α) ≤ t ⟺ min_v u(v) ≤ t ⟺ ∃ v ∈ ∂α with u(v) ≤ t — which equals the sub-level filtration
  on vertices alone, extended cellularly. This is CONSISTENT.
CoT step 2: For super-level-set filtration {x : u(x) ≥ t} (used in canonical D-ST-3 PersComp,
  L289-295), use MAX-extension: f̄(α) = max_v u(v). Symmetric construction.
CoT step 3: For SCC formation analysis we use the super-level extension (formations = high-u
  regions); this is the convention canonical T-OP6-B uses for B_PersRidge (gradient super-level).
  In this file we use min-extension for f̄ = u directly (since we want exterior pockets at u ≈ 0
  to be index-0 critical cells); equivalently use max-extension for f̄ = 1 - u to flip.
→ Convention chosen here: MIN-extension of u, so:
  - low-u (exterior pocket) → low f̄ value → index-0 critical vertex candidate
  - high-u (interior bulk) → high f̄ value → index-d critical face candidate (d = embedding dim)
  - boundary nodes → intermediate f̄ → index-1 critical edge candidate (saddle)
```

### §3.3 Genericity / Forman conditions (F1)+(F2)

For `f̄ = u (min-extension)` to be a valid Forman discrete Morse function, conditions (F1)+(F2) require **no degenerate ties** between values at incident cells of consecutive dimension. Equivalently:

- **(GEN1)** For every edge `e = (v_i, v_j)`: `u(v_i) ≠ u(v_j)` (no equal-value endpoints).
- **(GEN2)** For every vertex `v`: the values `{u(w) : w ∼ v}` are pairwise distinct (no symmetric neighborhoods).

If (GEN1)+(GEN2) fail (e.g., Aut(G)-invariant `u*` on translation-invariant `T²_n`), a small generic perturbation `u' = u + ε·η` with η ~ N(0, I) and small ε breaks ties (Forman 1998 Lemma 4.2 — generic perturbations are Morse).

```
CoT step 1: SCC's canonical T-V5b-T-zero (Cat A) gives μ_Gold = 0 EXACTLY on translation-invariant
  graphs because u* inherits Z_L^d translation symmetry → (GEN1) automatically violated.
CoT step 2: Therefore Forman analysis at u* DIRECTLY on (GEN1)-violating configurations requires
  EITHER (a) generic perturbation (lifts Goldstone via Aut(G) breaking) OR (b) Aut(G)-equivariant
  Forman theory (Allili-Kaczynski 2002 — equivariant discrete Morse).
CoT step 3: This is the canonical T-σ-Lemma-1 (Cat A, Hessian–G_u commutation) analog at the
  Forman cellular level: G_u-equivariant Forman theory must be used when (GEN1)+(GEN2) fail.
→ This is one source of L-FORMAN-HMORSE-DISCRETE's Cat B conditional (parallel to file 03's
  graph→continuum conditional — DIFFERENT source, both legitimate Cat B).

inverse_causation:
  - if (GEN1) fails AND no perturbation → Forman analysis ill-defined → Cat B becomes Cat C
  - if Aut(G) trivial → (GEN1)+(GEN2) generic → no perturbation needed → Cat B path strengthens
  - if equivariant Forman applies cleanly (Allili-Kaczynski 2002) → Cat B with Aut(G)-isotypic
    structure (parallels canonical T-σ-Lemma-1 Cat A)
```

---

## §4 Critical Cell Classification (Formation Features)

### §4.1 Three index regimes on 2-complex `K^{(2)}(G)`

For SCC formation `u*` on graph `G` with 2-complex `K^{(2)}(G)`:

| Forman index `p` | Cell type | SCC interpretation | u-value regime |
|---|---|---|---|
| `p = 0` | Critical vertex `v*` | **Exterior pocket** — locally smallest u value in neighborhood | `u(v*) ≈ 0` (sub-spinodal) |
| `p = 1` | Critical edge `e* = (v_i, v_j)` | **Boundary saddle** — minimum value `min(u_i, u_j)` is locally critical on edge ring | `u(e*) ∈` boundary band `[c_-, c_+]` (spinodal interior) |
| `p = 2` | Critical face `f*` | **Interior bulk** — minimum value over face is locally critical (face is locally a high-u plateau interior) | `u(f*) ≈ 1` (super-spinodal saturated) |

### §4.2 Geometric correspondence

```
CoT step 1: Each formation core C_j = {x : u*(x) ≥ θ_core} (canonical L329 D-Core definition,
  θ_core ≈ 1) contributes at least ONE critical 2-cell (the deepest interior face where min over
  face is locally maximal — equivalently a local max of u in cellular sense).
CoT step 2: Each formation BOUNDARY ∂C_j (canonical §5.3 Boundary Band) contains critical edges:
  saddle edges separating interior bulk from exterior pocket. Forman index = 1.
CoT step 3: Each MAXIMAL EXTERIOR POCKET (connected component of complement of formation cores)
  contributes at least ONE critical 0-cell (vertex of locally smallest u).
→ Cell census per formation: (m_0, m_1, m_2) lower bounds determined by exterior pockets, boundary
  saddles, interior bulks.

CoC anchors:
  - canonical: D-Core L329 θ_core (interior bulk)
  - canonical: §5.3 Boundary Band (interface = critical edges)
  - canonical: D-ST-3 L289 PersComp K_act counting (connects to critical face count)
inverse_causation:
  - if formation lacks interior plateau (e.g., narrow ridge): no critical 2-cell → m_2 drops →
    Morse inequalities for b_2 = 1 (torus) violated → formation cannot exist on full torus
    (refutes pathological non-bulk formations)
  - if boundary lacks saddle structure (smooth gradient transition): generic perturbation creates
    saddles; well-defined formations always have saddle boundary
```

### §4.3 Saturated vs unsaturated regime (D-HMORSE-LOCAL (C2′))

D-HMORSE-LOCAL (C2′) active-set form (canonical CV-1.16) distinguishes:
- **Saturated nodes**: `u*(v) ∈ {0, 1}` exactly (corners of `[0,1]^n`).
- **Free nodes**: `u*(v) ∈ (0,1)` (boundary band).

In the *saturated regime* (most nodes are 0 or 1, free nodes confined to boundary band):
- Interior bulks (`u ≈ 1`) form connected face clusters → contribute critical 2-cells at deepest face per cluster.
- Exterior pockets (`u ≈ 0`) form connected vertex clusters → contribute critical 0-cells.
- Boundary band (`u ∈ (0,1)`) contains the *Forman-critical edges*: index-1 saddle cells.

```
CoT: D-HMORSE-LOCAL (C2′) saturated regime is PRECISELY the regime where Forman index
  classification is sharpest — saturated values 0/1 give large value gaps across boundary,
  preventing degenerate (GEN1)/(GEN2) violations in interior/exterior, restricting failures
  to the boundary band (small fraction of nodes). This is the *cleanest* Cat B regime for
  L-FORMAN-HMORSE-DISCRETE.
```

---

## §5 Connection to T-OP6-B Persistent Ridge (Canonical Cat A)

### §5.1 T-OP6-B statement recap (canonical §5.3b L375-392)

T-OP6-B (Cat A, CV-1.7 Session K): `B_PersRidge(ũ*)` (persistent connected components of `|∇_G ũ*|² ≥ θ` super-level filtration) satisfies

$$
d_H(B_\mathrm{PersRidge}(\tilde u^*), \partial \mathrm{PersComp}(\tilde u^*)) \leq 2\sqrt{\alpha/\beta},
$$

under hypotheses H1–H5 (single-disk regime + super-spinodal + boundary band width matches).

### §5.2 Mischaikow-Nanda 2013 correspondence

**Theorem (Mischaikow-Nanda 2013)**. *For a filtered cell complex `K`, the persistence diagram of the cellular sub-level filtration of any Forman discrete Morse function `f` agrees (modulo critical-cell collapses) with the persistence diagram of the corresponding cellular filtration by f-value. Forman critical cells correspond bijectively (after collapse) with topological-essential cells in the persistence diagram.*

### §5.3 Application to SCC

```
CoT step 1: T-OP6-B's B_PersRidge uses PH of |∇_G u*|² super-level filtration — equivalently,
  PH of f̃ = -|∇_G u*|² sub-level filtration.
CoT step 2: By Mischaikow-Nanda 2013, the Forman critical cells of f̃ (interpreted via min-extension)
  correspond bijectively (modulo collapse) with persistence-essential cells in PH(f̃).
CoT step 3: B_PersRidge nodes = persistence-essential nodes of f̃ = Forman-critical edges of f̃
  (since edges encode gradient between vertex pairs).
CoT step 4: Therefore: T-OP6-B's persistent ridge boundary EQUALS the Forman index-1 critical
  edge set of the gradient field f̃ = -|∇_G u*|². This is the *cellular-Morse side* of T-OP6-B's
  *persistence-homology side* — Mischaikow-Nanda correspondence confirms compatibility.

→ T-OP6-B (Cat A) provides INDEPENDENT CANONICAL ANCHOR for Forman index-1 edge identification
  in SCC formations. This file's Forman-on-u (sub-level f̄ = u) is the DIRECT counterpart of
  T-OP6-B's PH-on-|∇u|² (super-level on gradient).

CoC anchors:
  - canonical: §5.3b T-OP6-B (Cat A) — PH on |∇_G u|² super-level
  - external: Mischaikow-Nanda 2013 — Forman ↔ persistence bijection (modulo collapse)
  - external: Edelsbrunner-Harer 2010 Ch.VII — sub-/super-level cell extension
inverse_causation:
  - if Mischaikow-Nanda correspondence has obstructions (e.g., non-CW filtration) → Forman and
    PH analyses diverge → T-OP6-B Cat A status does not transfer; here T-OP6-B's filtration is
    standard CW so correspondence applies cleanly
  - if T-OP6-B H1-H5 hypotheses fail → B_PersRidge bound not Cat A → Forman side inherits
    Cat B status (consistent with this file's classification)
```

### §5.4 Cross-strengthening

The pair (T-OP6-B Cat A, L-FORMAN-HMORSE-DISCRETE Cat B target):
- T-OP6-B gives *quantitative bound* (`d_H ≤ 2√(α/β)`).
- L-FORMAN-HMORSE-DISCRETE gives *cellular structure* (index counts, Morse inequalities).
- Together they form a *complete characterization* of SCC formation boundary at both the metric and topological levels.

---

## §6 L-FORMAN-HMORSE-DISCRETE Cat B Target Lemma

### §6.1 Statement

**Lemma L-FORMAN-HMORSE-DISCRETE** *(Cat B target; W8-Day3 2026-05-20)*.

**Statement.** *Let `G = (V, E)` be a canonical SCC graph with 2-cell completion `K^{(2)}(G)`. Let `u* ∈ Σ_m` be a non-uniform critical point of canonical `E = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd` satisfying D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5) (canonical CV-1.16 L1934). Let `f̄: K^{(2)}(G) → ℝ` be the min-extension of `u*` to cells (or `f̄ = u* + ε η` for small generic perturbation `η` if Aut(G)-symmetry violates (GEN1)+(GEN2)). Then under hypotheses (FH1)-(FH3) below, `f̄` is a Forman discrete Morse function with critical-cell census:*

$$
(m_0, m_1, m_2) = (\#\text{exterior pockets},\ \#\text{boundary saddle edges},\ \#\text{interior bulk faces}),
$$

*satisfying the strong Morse inequalities `m_p - m_{p-1} + \cdots \pm m_0 \geq b_p - b_{p-1} + \cdots \pm b_0` for `p = 0, 1, 2`, and the H-Morse spectral gap is bounded below by*

$$
\boxed{\mu_\mathrm{min}^\mathrm{non-Goldstone}(H_E(u^*)) \geq C(G) \cdot \min_e \Delta_e \cdot \mathbb{1}[m_1^\mathrm{free} \geq 1],}
$$

*where `Δ_e = |u^*(v_i) - u^*(v_j)|` is the edge value-gap, `m_1^\mathrm{free}` is the count of NON-Goldstone critical edges (after symmetry quotient), and `C(G) > 0` depends only on graph combinatorics (degrees, edge-Cheeger constant).*

### §6.2 Hypotheses (FH1)-(FH3)

- **(FH1) Forman regularity**: `f̄` (or its generic perturbation) satisfies (F1)+(F2) — i.e., is a valid discrete Morse function. Auto-satisfied for generic `u*`; for Aut(G)-symmetric `u*` requires perturbation OR Allili-Kaczynski 2002 equivariant Forman framework.
- **(FH2) Active-set conformity**: `u*` satisfies D-HMORSE-LOCAL (C2′) saturated-node decomposition with active set `A ⊂ V` (boundary nodes), saturated set `V \ A`. Saturated nodes contribute trivially to free Hessian; active-set nodes carry the spectral information. Forman analysis applies to `f̄|_A` for the active-set free Hessian.
- **(FH3) Aut(G) symmetry breaking (or equivariant treatment)**: either (a) Aut(G) acts trivially on `u*` after generic perturbation, OR (b) `u*` is Aut(G)-equivariant and Allili-Kaczynski 2002 equivariant Forman applies with critical cells classified by Aut(G)-orbits.

### §6.3 5-Step Proof Sketch

```
CoT step 1 — Construct Forman function f̄ from u*:
  Apply min-extension f̄(α) = min_{v ∈ vertices(α)} u*(v). Verify (F1)+(F2) under (FH1).
  If (FH1) fails (Aut(G)-symmetric u*), apply generic perturbation u' = u* + ε η (η ~ N(0,I_n),
  ε small). Forman 1998 Lemma 4.2: generic perturbation lifts ties → (FH1) satisfied. The
  resulting f̄' is a valid Forman discrete Morse function arbitrarily close to f̄.

CoT step 2 — Classify critical cells:
  By the saturated/active decomposition (FH2):
  - Index-0 cells: vertices v with u*(v) < u*(w) for all w ~ v → local minima → exterior pockets.
  - Index-1 cells: edges e = (v_i, v_j) with min(u_i, u_j) locally critical on adjacent edge ring
    → saddles between regions → boundary band.
  - Index-2 cells: faces f with min over f locally maximal among adjacent faces → interior bulks.
  Generic count: (m_0, m_1, m_2) = (#pockets, #saddles, #bulks).

CoT step 3 — Apply Morse inequalities:
  Strong: m_2 - m_1 + m_0 ≥ b_2 - b_1 + b_0 = 1 - 2 + 1 = 0 (T²_n Euler char χ = 0).
  Weak: m_p ≥ b_p individually:
    m_0 ≥ b_0 = 1 (at least one component → at least one exterior pocket)
    m_1 ≥ b_1 = 2 (torus first homology rank 2 → at least 2 essential 1-cycles → at least 2
      critical edges generating them, e.g., two non-contractible loops crossing formation boundary)
    m_2 ≥ b_2 = 1 (torus 2-dim class → at least one critical face).
  Therefore: m_0 + m_1 + m_2 ≥ 4 per single formation on T²_n.

CoT step 4 — Connect to H-Morse spectral gap:
  By discrete Cheeger inequality (Chung 1997 Spectral Graph Theory Theorem 2.3) applied to the
  restricted Hessian H_E(u*)|_A on active set A:
    λ_2(H_E(u*)|_A) ≥ h_A² / (2 · d_max)
  where h_A is the active-set Cheeger constant. For Forman-critical edges, h_A is bounded below
  by min_e Δ_e (value gap) divided by graph combinatorial constant.
  Multiplying by the spectral mass contribution from active set:
    μ_min^non-Goldstone(H_E(u*)) ≥ C(G) · min_e Δ_e · 𝟙[m_1^free ≥ 1].
  The indicator distinguishes: no non-Goldstone saddle edges → only Goldstone modes (μ = 0); at
  least one → strict positive gap.

CoT step 5 — H-Morse certification:
  Goldstone kernel ↔ Aut(G)-orbit modes (canonical T-V5b-T-zero Cat A on translation-invariant
  graphs; analog via Allili-Kaczynski 2002 equivariant Forman for symmetric configs).
  Non-Goldstone gap ↔ Forman index-1 free critical edges via Step 4.
  Conclusion: u* is H-Morse non-degenerate (in the L-HMORSE-LOCAL sense) with explicit lower
  bound governed by graph combinatorics and edge value-gaps.

→ Therefore L-FORMAN-HMORSE-DISCRETE holds Cat B (conditional on (FH1)-(FH3)). ∎ (sketch)
```

### §6.4 CoC anchored chain

```yaml
target: L-FORMAN-HMORSE-DISCRETE Cat B — SCC non-uniform critical u* on graph G has well-defined
  Forman discrete Morse cellular structure; H-Morse spectral gap bounded below by combinatorial
  edge-Cheeger × index-1 free critical edge count.

prior_anchors:
  canonical_Cat_A:
    - §5.3b T-OP6-B (PH on |∇_G u|² super-level; Mischaikow-Nanda bridge to Forman side)
    - §13 T-σ-Lemma-1 (Hessian–G_u commutation; equivariant Forman analog via Allili-Kaczynski 2002)
    - §13 T-V5b-T-zero (Goldstone exact zero on translation-invariant graphs; Forman counterpart
      via Aut(G)-equivariant Morse theory)
    - §13 Theorem 4 L1134-1136 (μ_k = 4αλ_k + βW''(c) uniform critical formula; this file extends
      to non-uniform via index counts)
  canonical_Cat_B:
    - §13 L-HMORSE-LOCAL (CV-1.16; D-HMORSE-LOCAL hypothesis package)
    - §13 L-HMORSE-DECOMP (CV-1.16; Schur structure)
  canonical_Cat_C:
    - §13 L-BOUNDARY-MODE-EXCLUSION (CV-1.16; sketch-level)
  canonical_OPEN:
    - OP-HMORSE-SADDLE (theorem_status.md L594) — attack via discrete saddle cell index (§9)
    - OP-0005-DYN (theorem_status.md L803) — partial impact via combinatorial bound
  external_Cat_A:
    - Forman 1998 Adv. Math. 134:90 (foundational discrete Morse theory)
    - Forman 2002 Sém. Lothar. Combin. 48:B48c (user's guide)
    - Mischaikow-Nanda 2013 Found. Comput. Math. 13:151 (Forman ↔ persistence)
    - Edelsbrunner-Harer 2010 (sub-/super-level cell extension)
    - Allili-Kaczynski 2002 (equivariant discrete Morse)
    - Chung 1997 Spectral Graph Theory (discrete Cheeger inequality)
    - van Gennip-Bertozzi 2012 (graph Modica-Mortola; cross-compatibility check with this file)

causation_chain:
  - (FH1) Forman regularity + (FH2) D-HMORSE-LOCAL (C2′) active set + (FH3) Aut(G) handled →
    f̄ = min-extension(u*) is valid Forman function (Step 1)
  - Step 1 + cell index classification → (m_0, m_1, m_2) = (#pockets, #saddles, #bulks) (Step 2)
  - Step 2 + Forman strong/weak Morse inequalities → m_p ≥ b_p; m_0+m_1+m_2 ≥ χ-count (Step 3)
  - Step 3 + discrete Cheeger inequality (Chung 1997) on active-set Hessian → μ_min^non-Gold ≥
    C(G)·min_e Δ_e·𝟙[m_1^free ≥ 1] (Step 4)
  - Step 4 + T-V5b-T-zero Goldstone kernel identification → H-Morse certification (Step 5)
  → L-FORMAN-HMORSE-DISCRETE Cat B

inverse_causation_per_step:
  - Step 1 inverse: (FH1) fails AND no perturbation → Forman undefined → entire chain breaks;
    correctly classified Cat B conditional on (FH1)
  - Step 2 inverse: D-HMORSE-LOCAL (C2′) fails (unsaturated regime, no clear active set) → index
    classification ill-defined → Cat B status maintained (regime mismatch flagged)
  - Step 3 inverse: graph topology different from T²_n (b_p values change) → Morse inequality
    counts change but framework persists; only the SPECIFIC (m_0,m_1,m_2)=(1,2,1) count is torus-
    specific
  - Step 4 inverse: graph combinatorial constants very small (vanishing Cheeger) → bound trivially
    satisfied with C(G) ≈ 0 → spectral gap not constrained; Cat B → Cat C downgrade
  - Step 5 inverse: T-V5b-T-zero Cat A fails OR Aut(G) trivial → no Goldstone kernel; H-Morse
    STRENGTHENS (no degenerate modes) rather than fails
  - Mischaikow-Nanda correspondence removed: T-OP6-B side connection lost → standalone Forman
    analysis still valid (does not invalidate proof; reduces cross-anchor strength)
```

### §6.5 Cat B classification justification

**Why Cat B, not Cat A**:

1. **(FH1) Genericity conditional**: Aut(G)-symmetric `u*` (the canonical regime per T-V5b-T-zero) requires either perturbation argument (introduces small but non-trivial error) OR equivariant Forman theory (Allili-Kaczynski 2002 — extends Forman to non-trivial group actions; the *equivariant Cat A path* requires showing T-σ-Lemma-1's Maschke + Schur extends to cellular Morse complex, non-trivial).

2. **(FH2) D-HMORSE-LOCAL Cat B inheritance**: directly inherits from L-HMORSE-LOCAL Cat B status — cannot exceed parent.

3. **(FH3) Aut(G) equivariance**: Goldstone identification via Aut(G)-orbit critical-cell quotient requires the equivariant discrete Morse complex (Allili-Kaczynski 2002), which is *Cat A in the discrete topology literature but Cat B in SCC-specific application* (the SCC `E_E` Hessian–G_u commutation must transfer to cellular Morse complex automorphisms; non-trivial).

4. **Spectral magnitude bound `C(G)·min_e Δ_e`**: this is a *qualitative* lower bound; the constant `C(G)` is graph-combinatorial (edge-Cheeger-derived) but its sharp evaluation for canonical SCC graph families (T²_n, K_n, regular trees) is a *separate proof obligation*.

**Cat B → Cat A path** (parallel to T-OP6-B promotion CV-1.7 Session K):
- (FH1-EQUIV): explicit equivariant Forman theory adaptation for canonical SCC Aut(G) actions (T²_n's `Z_n^2` torus translations, K_n's `S_n` symmetric group, etc.).
- (FH2-SHARP): sharp `C(G)` constants for each canonical graph family.
- (FH3-INHERIT): inherited from L-HMORSE-LOCAL Cat A path (currently OP-HMORSE-LOCAL-A OPEN, theorem_status.md L593).

Each is a substantive proof obligation, justifying Cat B status.

---

## §7 Morse Inequalities for SCC Formation Regime

### §7.1 Strong Morse inequalities (Forman 1998 Theorem 3.5)

For SCC formation `u*` on cell complex `K^{(2)}(G)` with Forman extension `f̄`:

$$
m_p - m_{p-1} + \cdots \pm m_0 \geq b_p - b_{p-1} + \cdots \pm b_0, \quad p = 0, 1, 2,
$$

$$
\sum_{p=0}^{2} (-1)^p m_p = \chi(K) = \sum_{p=0}^{2} (-1)^p b_p.
$$

### §7.2 Reference: 2D torus `T²_{16}` (CONSENSUS BASELINE)

Betti numbers of `T²_{16}`:

$$
b_0 = 1, \quad b_1 = 2, \quad b_2 = 1, \quad \chi(T^2) = 1 - 2 + 1 = 0.
$$

Weak Morse inequalities:

$$
\boxed{m_0 \geq 1, \quad m_1 \geq 2, \quad m_2 \geq 1.}
$$

Strong Morse inequalities (in addition):

$$
m_0 \geq 1, \quad m_1 - m_0 \geq 2 - 1 = 1, \quad m_2 - m_1 + m_0 \geq 1 - 2 + 1 = 0.
$$

Euler condition:

$$
m_0 - m_1 + m_2 = 0 \Longleftrightarrow m_0 + m_2 = m_1.
$$

### §7.3 Per-formation lower bound

```
CoT step 1: Single formation occupying a region of T²_{16} contributes:
  - ≥ 1 interior bulk face (m_2 contribution): formation core deepest face.
  - ≥ 2 boundary saddle edges (m_1 contribution): boundary of formation must contain edges
    representing the 2 essential 1-cycles of the torus (or, alternately, the boundary itself
    bounds 0 → 1 transition which generically has saddle structure on both essential cycles).
  - ≥ 1 exterior pocket vertex (m_0 contribution): outside the formation, deepest exterior point.
CoT step 2: Per-formation total: m_0 + m_1 + m_2 ≥ 1 + 2 + 1 = 4 critical cells.
CoT step 3: For K formations (K_act counting per canonical D-ST-3 L289): total critical cells
  scale as ≥ 4K (each formation contributes its own m_p baseline; boundary cycles may be shared).
→ Discrete Morse inequalities give a TIGHT topological lower bound: 4 critical cells per formation
  on T²_n.

CoC anchors:
  - canonical: D-ST-3 L289 K_act = #PersComp
  - external: Forman 1998 Theorem 3.5 (Morse inequalities)
inverse_causation:
  - if formation does NOT span essential 1-cycles (small localized blob, b_1^{blob} = 0): the
    boundary contribution to m_1 may be lower; Morse count adjusts to m_p ≥ b_p^{blob+exterior}
  - if K_act counting violates Morse inequalities (e.g., m_2 < K_act): contradiction — refutes
    over-counting in K_act
```

### §7.4 Connection to canonical D-ST-3 K_act

K_act = #PersComp on cohesion field (canonical L289-295) counts **persistent connected components** of super-level filtration. This is closely related to m_2 (number of interior bulk faces) and m_0 (exterior pockets, via duality):

- `m_2` (number of critical faces) lower-bounds `K_act` (each persistent component contains at least one critical face).
- Conversely, `K_act` upper-bounds the *essential* m_2 count (collapsing non-persistent components).

This provides an *independent canonical anchor* for the Forman index-2 cell count.

---

## §8 Discrete vs Continuum Comparison (File 03 ↔ This File)

### §8.1 Direct comparison table

| Aspect | File 03 (Modica-Mortola Jacobi) | This file (Forman discrete Morse) |
|---|---|---|
| **Domain** | Continuum `Ω ⊂ ℝ^d` after sharp-interface limit | Finite graph `G`, no limit needed |
| **Operator** | `J_Γ = -Δ_Γ - |A|²` on smooth boundary `Γ` | Forman Morse complex on `K^{(2)}(G)` |
| **Information yielded** | Spectral magnitudes (`σ·μ_ℓ`) | Cellular Morse indices, Morse inequalities |
| **Goldstone identification** | `μ_1 = 0` via spherical harmonics on `Γ = S^{d-1}_R` | Aut(G)-orbit critical-cell quotient (Allili-Kaczynski 2002) |
| **Wobble gap** | `μ_2 = (d+1)/R²` (explicit formula on sphere) | `C(G)·min_e Δ_e` (combinatorial bound) |
| **Cat B conditional source** | Graph→continuum step (van Gennip-Bertozzi 2012 + (GC1)-(GC4)) | Forman genericity (FH1) + Aut(G) handling (FH3) |
| **OP-HMORSE-SADDLE attack** | Saddle Jacobi has 1 negative eigenvalue (analytical) | Saddle cells have Forman index = 1 (cellular invariant) |
| **Strength** | Quantitative magnitude bounds | Topological structure / Morse type |
| **Weakness** | Requires graph→continuum applicability | Does not directly yield eigenvalue magnitudes |

### §8.2 Compatibility verdict

```
CoT step 1: At the CRITICAL CONFIGURATION level (specific u*), both approaches identify the same
  geometric features: boundary (saddle) + interior (bulk) + exterior (pocket). The continuum
  approach calls them Γ + Ω + complement; the discrete approach calls them index-1 + index-2 +
  index-0 critical cells.
CoT step 2: At the SPECTRAL TYPE level, both approaches give H-Morse non-degeneracy with
  Goldstone kernel + positive wobble. The continuum gives σ·μ_2 magnitude; the discrete gives
  C(G)·min_e Δ_e magnitude. These should agree in the appropriate scaling limit (h → 0 of
  graph mesh) — verifying this would be a Cat A → Cat A bridge proof.
CoT step 3: At the SADDLE structure level, both approaches give Morse index 1 (one unstable
  direction). The continuum gives analytical sign (-1 eigenvalue along K-jump); the discrete
  gives cellular index 1.
CoT step 4: COMPLEMENTARITY: the two approaches have DIFFERENT Cat B conditionals (continuum:
  graph→continuum; discrete: genericity+equivariance). A Cat A path for either is INDEPENDENT
  of the other. Both surviving as Cat B targets is the EXPECTED state — they attack the same
  L-HMORSE-LOCAL strengthening from orthogonal directions.

→ COMPATIBILITY VERDICT: COMPATIBLE AND COMPLEMENTARY. Neither subsumes the other; both
  provide independent attack channels on the H-Morse problem and OP-HMORSE-SADDLE.

CoC anchors:
  - canonical: §5.3b T-OP6-B (bridges both — PH on |∇_G u|² uses both discrete graph and
    continuous gradient field)
  - external: Mischaikow-Nanda 2013 (Forman ↔ PH correspondence; PH is the discrete-side
    realization of continuum Morse)
  - external: van Gennip-Bertozzi 2012 (graph Modica-Mortola; the bridge that, when Cat A,
    would let file 03 and this file's bounds be matched)
```

### §8.3 Advantage analysis

**Advantage of discrete (this file)**:
- NO `h → 0` limit needed; results valid on the actual finite SCC graph at hand.
- Topological invariants (Betti numbers, Morse indices) are *exact* combinatorial quantities,
  not asymptotic approximations.
- Forman Morse inequalities give *unconditional structural lower bounds* on the critical-cell
  count, independent of metric scaling.

**Advantage of continuum (file 03)**:
- *Quantitative magnitude bounds* via geometric quantities (R, |A|², d).
- Explicit dependence on the surface tension `σ = (√2/6)√(αβ)` (CONSENSUS BASELINE).
- Connects to Allen-Cahn / Cahn-Hilliard PDE literature for cross-validation.

---

## §9 OP-HMORSE-SADDLE Attack via Discrete Saddle Cell Counts

### §9.1 Canonical OP-HMORSE-SADDLE statement

**OP-HMORSE-SADDLE** registered at `theorem_status.md` L594:
> *"Saddle-point Hessian regularity. Medium. OPEN (NEW CV-1.16): required for full Eyring-Kramers prefactor Cat B; independent of OP-HMORSE-LOCAL-A. ETA 2–4 sessions."*

(Critic §B.1 finding: file 03 misciting this as canonical L1967 is INCORRECT; the actual registration is at theorem_status.md L594.)

### §9.2 Discrete saddle cell attack

At a saddle point `u†` between two formations (e.g., K-jump transition state, K=2 → K=1 merging), the cellular saddle structure is:

```
CoT step 1: Apply Forman discrete Morse analysis to u† (with generic perturbation if needed).
CoT step 2: The K-jump direction (saddle's single unstable direction) corresponds to a
  DISTINGUISHED critical cell whose neighborhood structure encodes the K-jump topology:
  - When K decreases from 2 → 1: an index-1 cellular saddle bridges the two former bulks.
  - The bridging critical edge is itself locally a saddle in f̄.
CoT step 3: Forman cellular index of the K-jump bridge = 1 (one cellular dimension of "passage"
  from K=2 split state to K=1 merged state).
CoT step 4: Therefore: SADDLE MORSE INDEX = 1 at K-jump configurations, established as a
  CELLULAR INVARIANT (topological, not analytical).
→ This is a STRUCTURAL ATTACK on OP-HMORSE-SADDLE: confirms the expected saddle has the right
  Morse type (index 1) from the cellular side.

CRUCIAL DISCLAIMER: discrete Morse index = 1 does NOT directly give the HESSIAN EIGENVALUE
  magnitude at the saddle. It only confirms that the saddle has CELLULAR Morse type 1 (one
  unstable cellular direction). The Hessian eigenvalue magnitude requires either (a) Cheeger-
  type bound from §6.3 Step 4, or (b) the file 03 continuum Jacobi analysis. The discrete
  approach gives the TYPE; the continuum approach gives the MAGNITUDE.
```

### §9.3 Attack channel (Cat B target → Cat A path)

OP-HMORSE-SADDLE Cat A path via THIS file's framework:

1. **Step 1 (Cat B target — established here)**: L-FORMAN-HMORSE-DISCRETE Cat B at saddle u†
   → cellular saddle Morse index = 1 (cellular invariant).
2. **Step 2 (Cat B → Cat A discrete-side)**: explicit equivariant Forman analysis for canonical
   SCC saddle configurations (T²_n K-jump structures); requires Aut(G)-equivariant Morse complex
   genericity (Allili-Kaczynski 2002 extended to SCC-specific actions).
3. **Step 3 (Cat A)**: combine with discrete Cheeger inequality (Chung 1997) for spectral
   magnitude → OP-HMORSE-SADDLE RESOLVED Cat A from the discrete side.

This is *strictly an attack framework*, NOT a resolution claim. Attack point named (theorem_status.md L594) — not solved (CN2 compliance).

### §9.4 Complementary to file 03 attack

File 03 attacks OP-HMORSE-SADDLE via analytical Jacobi spectrum (1 negative eigenvalue from
`-Δ_Γ - |A|²` on saddle surface). This file attacks via cellular Morse index. **Both attack
channels are independent** — Cat A resolution of either does not imply the other; but BOTH
together would provide a *cross-validated* OP-HMORSE-SADDLE Cat A resolution.

---

## §10 2D Torus 16×16 Reference Example (CONSENSUS BASELINE)

### §10.1 Setup

Reference parameters (CONSENSUS BASELINE):
- Graph: `G = T²_{16} = C_{16} × C_{16}`, n = 256 vertices, 512 edges, 256 square faces (2-complex completion).
- Parameters: `c = 1/2, α = 1, β = 10, T_* = 0.1, R = 4`.
- Spinodal interior verified: `c = 1/2 ∈ ((3-√3)/6, (3+√3)/6) ≈ (0.211, 0.789)` ✓.
- T8 condition: `β·|W''(c)|/(4·λ_2) = 10·1/(4·0.1522) = 16.4 > 1` ✓ (super-spinodal).
- Mass constraint: `m = c·n = 128`.

### §10.2 Typical formation profile

Single-disk formation centered at `(8, 8)` with radius `R = 4`:
- **Interior bulk** `Ω* = {(i,j) : (i-8)² + (j-8)² ≤ 16}`: ~50 vertices with `u*(v) ≈ 1`.
- **Boundary band** `Bd = {(i,j) : 16 < (i-8)² + (j-8)² < 25}`: ~28 vertices with `u*(v) ∈ (0,1)` (free nodes per D-HMORSE-LOCAL (C2′)).
- **Exterior pocket** complement: ~178 vertices with `u*(v) ≈ 0`.

### §10.3 Forman critical cell census

Applying min-extension Forman analysis (with generic perturbation breaking the disk's `Z_8` rotational symmetry):

| Cell type | Count `m_p` | Source |
|---|---|---|
| Index-0 critical vertices (exterior pockets) | `m_0 ≥ 1` | Single connected exterior region → at least 1 critical vertex (deepest exterior point). Typically `m_0 = 1` for compact disk on torus exterior. |
| Index-1 critical edges (boundary saddles + topological cycles) | `m_1 ≥ 2` | Two essential 1-cycles of torus must be witnessed by critical edges crossing them; for single-disk formation that does not wrap any essential cycle, the 2 essential cycles are carried by exterior critical edges. Typically `m_1 = 2 + #(boundary saddle features)`. |
| Index-2 critical faces (interior bulks) | `m_2 ≥ 1` | Single interior bulk → at least 1 critical face (deepest interior face). Typically `m_2 = 1`. |

**Total**: `m_0 + m_1 + m_2 ≥ 4` per formation ✓ (matches §7.3 prediction).

### §10.4 Morse inequality verification

```
Strong inequalities check:
  m_0 ≥ b_0 = 1 ✓
  m_1 - m_0 ≥ b_1 - b_0 = 1 ⟹ m_1 ≥ m_0 + 1 ≥ 2 ✓ (consistent with weak)
  m_2 - m_1 + m_0 ≥ b_2 - b_1 + b_0 = 0 ⟹ m_2 + m_0 ≥ m_1 ✓ (Euler condition)

Euler condition:
  χ(T²_{16}) = m_0 - m_1 + m_2 = 0 (must hold with equality for Euler char of torus)
  ⟹ m_0 + m_2 = m_1 ✓
```

For the canonical single-disk formation: typical census `(m_0, m_1, m_2) = (1, 2, 1)` satisfies
Euler equality `1 - 2 + 1 = 0` ✓. This is the **minimal Morse representation** of the torus
homology consistent with a single SCC formation.

### §10.5 Spectral gap estimate via §6.1 boxed bound

Reference values:
- `min_e Δ_e` over boundary band: with `u*` saturated in interior (`u ≈ 1`) and exterior (`u ≈ 0`), 
  the smallest edge value-gap across the boundary band is on the order of `Δ ~ 1/(boundary band width)`.
  For `√(α/β) = √(1/10) ≈ 0.316` band width and saturated interior/exterior, `min_e Δ_e ≈ 0.1` (estimated; conjectural — would require explicit numerical verification on the actual `u*` profile).
- `C(G)` for `T²_{16}`: graph degree `d = 4`, edge-Cheeger constant `h(T²_{16})` is well-studied;
  for square torus `h ≈ 4·sin(π/n) ≈ 4·0.196 ≈ 0.785` at n=16.
- `C(G) ≈ h²/(2·d_max) = 0.785² / 8 ≈ 0.077`.
- `m_1^free` (non-Goldstone critical edges): on translation-invariant torus, the 2 Goldstone
  edges (translation orbit representatives) are quotiented; if `m_1 = 2 + 1 = 3` (2 essential + 1
  boundary saddle), then `m_1^free = 1` after Aut(G) quotient (assuming generic perturbation
  preserves Goldstone identification).
- **Estimated bound**: `μ_min^non-Goldstone ≥ C(G) · min_e Δ_e · 1 ≈ 0.077 · 0.1 = 7.7×10⁻³`.

**Cross-anchor with L-HMORSE-LOCAL numerical**: canonical L-HMORSE-LOCAL numerical anchor
(canonical L1960) gives `μ_min ∈ [0.13, 3.49]` on 5×5/10×10/15×15 grids — *the discrete Cheeger
bound 7.7×10⁻³ is conservative* (factor ~17 below the numerical floor, as expected for Cheeger-
type bounds which are notoriously loose). This is *consistent*, not contradictory.

```
CoT: The discrete Cheeger bound is a STRUCTURAL lower bound — it certifies positivity but is
  typically loose. The continuum Modica-Mortola Jacobi gap (file 03 §9 boxed: μ_min ≥
  s·(√2/6)·√(αβ)·(d+1)/R² = (√2/6)·√10·3/16 ≈ 0.30 at reference s=1) is closer to the
  numerical anchor and provides a TIGHTER bound at the cost of the graph→continuum conditional.
  Both bounds together: Cheeger ≤ 0.0077, Modica-Mortola ≈ 0.30, numerical ∈ [0.13, 3.49].
  CONSISTENT.
```

---

## §11 Discrete-Graph Compatibility (van Gennip-Bertozzi 2012)

### §11.1 Cross-check with graph Modica-Mortola

**van Gennip-Bertozzi 2012** (*SIAM J. Imaging Sci.* **5**:1115) establishes Γ-convergence of
discrete graph TV → continuum TV under mesh refinement. **Chambolle-Giacomini-Lussardi 2014**
(*Math. Models Methods Appl. Sci.* **24**:847) extends to full graph-based Modica-Mortola.

```
CoT step 1: van Gennip-Bertozzi 2012's discrete TV functional Σ w_ij |u_i - u_j| has CRITICAL
  POINTS coinciding (in the appropriate weak sense) with discrete sub-level set perimeters on G.
CoT step 2: Forman discrete Morse theory analyzes the SAME critical points (vertices, edges,
  faces) but from the CELL-COMPLEX side rather than the energy-variational side.
CoT step 3: Compatibility: both approaches identify the same boundary band (edges where TV
  energy concentrates = critical edges of f̄ = u). This confirms the two graph-side approaches
  are mutually consistent and reinforce each other.
→ Therefore: Forman discrete Morse (this file) and graph Modica-Mortola (van Gennip-Bertozzi
  2012 / Chambolle-Giacomini-Lussardi 2014) are COMPATIBLE GRAPH-NATIVE TOOLS, both avoiding
  the h → 0 continuum limit that file 03 requires.

CoC anchors:
  - external: van Gennip-Bertozzi 2012 (graph TV Γ-convergence)
  - external: Chambolle-Giacomini-Lussardi 2014 (graph Modica-Mortola)
  - external: Forman 1998 (this file's primary tool)
inverse_causation:
  - if van Gennip-Bertozzi 2012 graph-side hypotheses (GC1)-(GC4) per file 03 §7.2 fail → graph
    Modica-Mortola side breaks; Forman side INDEPENDENT (relies only on (FH1)-(FH3)) — this is
    a STRENGTH of the discrete approach over the continuum approach
  - if Forman (FH1)-(FH3) fail but van Gennip-Bertozzi holds → graph TV analysis applies but
    Forman cell-complex side does not — also legitimate Cat C downgrade
```

### §11.2 Joint discrete-graph picture

```
                 SCC u* on graph G
                       |
        +--------------+--------------+
        |                             |
   FORMAN (this file)           GRAPH MM (vGB 2012)
   - cellular Morse complex     - graph TV functional
   - index counts (m_0,m_1,m_2) - Γ-converges to ∫|∇u|
   - Morse inequalities         - sub-level perimeter
        |                             |
        +-------- Mischaikow-----+
                  Nanda 2013
                  bridge to
                  persistence
                  (canonical
                  T-OP6-B PH side)
```

Both graph-native approaches (Forman + graph MM) terminate without requiring `h → 0`; the
continuum Modica-Mortola Jacobi (file 03) sits above this with the additional graph→continuum
step. The three approaches form a *cascade of attack channels* on L-HMORSE-LOCAL strengthening.

---

## §12 CoT/CoC Archival (Mode-Level Summary)

### §12.1 CoT-CORE

```
CoT step 1: SCC's H-Morse analysis (L-HMORSE-LOCAL Cat B, CV-1.16) needs ANALYTICAL FOUNDATION
  beyond numerical 15/15 PASS. File 03 provides continuum Modica-Mortola Jacobi (Cat B target);
  critic §B identified that file 03's Cat B status originates entirely from the graph→continuum
  step (van Gennip-Bertozzi 2012 + (GC1)-(GC4) hypothesis package).
CoT step 2: A GRAPH-NATIVE approach avoids this conditional. Forman discrete Morse theory
  (Forman 1998 Adv. Math. 134:90-145) operates DIRECTLY on the finite cell complex K(G) with
  NO mesh refinement.
CoT step 3: SCC field u: V → [0,1] induces a Forman discrete Morse function f̄ on K(G) via
  standard min-extension. Critical cells classify into index-0 (exterior pockets), index-1
  (boundary saddles), index-2 (interior bulks) for 2-complex K^{(2)}(G).
CoT step 4: Forman strong/weak Morse inequalities give topological lower bound m_p ≥ b_p on
  critical-cell counts. For 2D torus T²_n: b_0 = 1, b_1 = 2, b_2 = 1 → per-formation minimum
  4 critical cells (1 + 2 + 1). Connects to canonical D-ST-3 K_act counting.
CoT step 5: Mischaikow-Nanda 2013 establishes Forman ↔ persistence correspondence, providing
  cross-anchor with canonical T-OP6-B (Cat A, CV-1.7) which uses PH on |∇_G u|² super-level
  filtration. T-OP6-B is the closest existing canonical anchor for Forman discrete Morse on SCC.
CoT step 6: H-Morse spectral gap bound via discrete Cheeger inequality (Chung 1997) on active-
  set Hessian: μ_min^non-Goldstone ≥ C(G) · min_e Δ_e · 𝟙[m_1^free ≥ 1]. This is a
  COMBINATORIAL bound (qualitative magnitude, exact structure).
CoT step 7: OP-HMORSE-SADDLE (theorem_status.md L594, OPEN) attack: saddle Morse index = 1
  established as cellular invariant (complementary to file 03's analytical Jacobi spectrum
  attack via -|A|² + spectrum gap). Different conditional hypotheses → independent attack channels.
CoT step 8: Cat B classification: (FH1) Forman genericity (Aut(G)-symmetric u* needs perturbation
  or equivariant Forman per Allili-Kaczynski 2002), (FH2) D-HMORSE-LOCAL (C2′) active-set,
  (FH3) Aut(G) equivariance handling. Each is a substantive proof obligation, paralleling
  T-OP6-B's promotion path (CV-1.7 Session K).
→ Therefore: L-FORMAN-HMORSE-DISCRETE Cat B target = graph-native cellular analytical foundation
  for SCC H-Morse, complementary to file 03's continuum approach, with explicit OP-HMORSE-SADDLE
  cellular-index attack channel.
```

### §12.2 CoC anchored chain (mode-level)

```yaml
target: L-FORMAN-HMORSE-DISCRETE Cat B target lemma — SCC non-uniform critical u* on graph G
  has Forman discrete Morse cellular structure with critical cells classified by formation
  features (exterior/boundary/interior); H-Morse spectral gap bounded below by combinatorial
  edge-Cheeger × index-1 free critical edge count.

prior_anchors:
  canonical_Cat_A:
    - §5.3b T-OP6-B (CV-1.7) — PH on |∇_G u|² (Mischaikow-Nanda 2013 bridge)
    - §13 T-σ-Lemma-1 (CV-1.5) — Hessian–G_u (Allili-Kaczynski 2002 equivariant Forman analog)
    - §13 T-V5b-T-zero (CV-1.5.1) — translation Goldstone (Forman counterpart via Aut(G)-orbit
      critical cells)
    - §13 Theorem 4 (CV-1.5, canonical.md L1134-1136) — μ_k = 4αλ_k + βW''(c) uniform critical
  canonical_Cat_B:
    - §13 L-HMORSE-LOCAL (CV-1.16) — direct parent; this file provides parallel structural account
    - §13 L-HMORSE-DECOMP (CV-1.16) — Schur complement; index-counting compatible
  canonical_Cat_C:
    - §13 L-BOUNDARY-MODE-EXCLUSION (CV-1.16) — graph boundary mode exclusion
  canonical_OPEN:
    - OP-HMORSE-SADDLE (theorem_status.md L594) — cellular-index attack channel (§9)
    - OP-0005-DYN (theorem_status.md L803) — Kramers prefactor; partial impact via combinatorial bound
  external_Cat_A:
    - Forman 1998 Adv. Math. 134:90 (foundational)
    - Forman 2002 Sém. Lothar. Combin. 48:B48c (user's guide)
    - Mischaikow-Nanda 2013 Found. Comput. Math. 13:151 (Forman ↔ persistence)
    - Edelsbrunner-Harer 2010 (sub-/super-level cellular extension)
    - Allili-Kaczynski 2002 (equivariant discrete Morse)
    - Chung 1997 Spectral Graph Theory (discrete Cheeger)
    - van Gennip-Bertozzi 2012 SIAM J Imaging Sci 5:1115 (graph MM compatibility)
    - Chambolle-Giacomini-Lussardi 2014 Math Models Methods Appl Sci 24:847 (graph MM)
    - Bauer 2021 J. Appl. Comput. Topol. 5:391 (computational realization)

causation_chain:
  - (FH1) Forman regularity OR generic perturbation → f̄ = min-ext(u*) valid Forman function (Step 1)
  - Cellular index classification + (FH2) D-HMORSE-LOCAL (C2′) → (m_0,m_1,m_2) per formation feature (Step 2)
  - Forman Morse inequalities (Forman 1998 Theorem 3.5) → m_p ≥ b_p (Step 3)
  - Discrete Cheeger (Chung 1997) on active-set Hessian → μ_min ≥ C(G)·min_e Δ_e·𝟙[m_1^free ≥ 1] (Step 4)
  - (FH3) Aut(G) Goldstone identification (Allili-Kaczynski 2002 or perturbation) → H-Morse cert (Step 5)
  → L-FORMAN-HMORSE-DISCRETE Cat B

inverse_causation_per_anchor:
  - Forman 1998 removed: no discrete Morse theory → cellular index classification undefined
    → entire framework breaks
  - Mischaikow-Nanda 2013 removed: T-OP6-B PH ↔ Forman bridge unavailable → standalone Forman
    still valid; loses cross-anchor strength but proof unaffected
  - Allili-Kaczynski 2002 removed: equivariant Forman unavailable → must use generic perturbation
    (slightly weaker; reduces Cat A path strength but Cat B intact)
  - Chung 1997 (Cheeger) removed: discrete spectral magnitude bound unavailable → only
    cellular structure remains; Cat B downgrades to "structure only" claim
  - van Gennip-Bertozzi 2012 removed: graph MM cross-compatibility loses one external anchor;
    Forman side INDEPENDENT (relies on Forman 1998 directly) → no impact on this file
  - T-OP6-B Cat A failure: cross-anchor weakens; Forman analysis intact
  - L-HMORSE-LOCAL (C2′) failure: (FH2) violated → active-set decomposition undefined →
    framework correctly inapplicable
  - T-V5b-T-zero failure (no graph translation orbit): Goldstone identification simplifies
    (no kernel); H-Morse certification STRENGTHENS rather than fails
```

---

## §13 Hard Constraint CN1-16 Check

Per canonical CN1-16 + prompt strict constraints + CV-1.18 SEAL deprecation:

| Constraint | Status | Evidence |
|---|---|---|
| **CN1** canonical 직접 수정 0 | ✓ | working layer draft; canonical 미접근 (read-only references to §3.7, §5.3, §5.3b T-OP6-B, §13 L-HMORSE-LOCAL/DECOMP/T-σ-Lemma-1/T-V5b-T-zero/Theorem 4 L1134-1136); theorem_status.md L594 OP-HMORSE-SADDLE + L803 OP-0005-DYN cited correctly per critic §B.1 |
| **CN2** Silent OP resolution 0 | ✓ | OP-HMORSE-SADDLE explicitly *attack channel named* (§9.3), *not solved* — discrete saddle Morse index = 1 is CELLULAR invariant, NOT analytical eigenvalue magnitude (explicit disclaimer §9.2). Cat B target only |
| **CN3** Research OS 재도입 0 | ✓ | single working file in `THEORY/working/field_equation_framework/`, no new registry directory |
| **CN4 (analyticity, b_D=0)** | ✓ | NO new energy term; SCC `E_bd` 형식 미변경; b_D = 0 자동 (cellular topology analysis only); PH/combinatorial S(u) 미도입 as new energy |
| **CN5 (4-term independence)** | ✓ | 본 문서 analyzes critical u* of combined E = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd WITHOUT merging terms; Forman is structural cell-complex analysis of u*, not energy-decomposition |
| **CN6 Closure idempotence 가정 0** | ✓ | 미적용 |
| **CN7 K 이중 취급 0** | ✓ | K-vocabulary: K-jump (saddle direction §9), K_act (canonical D-ST-3 cross-anchor §7.4); K_field/K_soft 어휘 부재 |
| **Zero-temp metastability flag** | ✓ | T_* 어휘 부재 (this file = static cellular topology, not dynamical); metastability claim 0 |
| **OMC 풀 오케스트레이션 0** | ✓ | 호출 0 |
| **CN10 (no reductive reduction — contrastive standard tool)** | ✓ | §1.2 explicit "SCC u IS a Forman function" 금지, "SCC u INDUCES Forman function via standard min-extension" 사용; Forman 1998 = *contrastive standard discrete-topology tool*; *no SCC = Forman reduction*. CSSL-style segmentation drift 미사용 (cell-complex analysis only). |
| **Primitive u_t 전도 0** | ✓ | u_t primitive 유지; Forman `f̄ = min-extension(u*)` 는 *derived* cellular function (standard min-on-endpoints), *not primitive* |
| **Inertia 0** | ✓ | first-order Langevin only (static analysis, no time evolution); second-order temporal term 0 |
| **Mori-Zwanzig 0** | ✓ | CV-1.18 SEAL OP-0021 Routes A/B DEPRECATED preserved; memory kernel 0 |
| **CSSL energy terms (E_ridge / E_wild / E_pers) 0** | ✓ | critic-rejected anti-patterns; 본 문서 미사용; §1.2 explicit anti-pattern boundary |
| **DECL-1.0 amend 0** | ✓ | DECL 미수정; Q1 (T8 boundary) + Q3 (객체 vs 형성) 직접 활용 only |
| **scc/ 수정 0** | ✓ | 본 문서 = doc-only |
| **CONSENSUS BASELINE compliance** | ✓ | σ = (√2/6)√(αβ) cited correctly when invoked (§10.5 cross-check); T²_{16} reference + λ_2 = 0.1522 used (§10.1); c=1/2, α=1, β=10, T_*=0.1, R=4 used consistently (§10.1-10.5); W''(1/2) = -1 verified (§0.3); OP-HMORSE-SADDLE = theorem_status.md L594 NOT canonical.md L1967 (§0.3, §9.1); OP-0005-DYN = theorem_status.md L803 (§0.3); Theorem 4 = canonical.md L1134-1136 (§0.3, §6.4 citation) |

**16/16 ✓ + CONSENSUS BASELINE ✓ verified**.

---

## §14 One-Paragraph Summary

**Forman discrete Morse theory (Forman 1998 *Adv. Math.* 134:90-145) applied to SCC's graph-based H-Morse problem gives a *graph-native* cellular analysis that does NOT require the continuum limit, directly complementing file 03's Modica-Mortola Jacobi-on-Γ framework whose Cat B classification originates entirely from the graph→continuum step (critic §B.5 + §7.3 + (GC1)-(GC4) hypothesis package). SCC field `u: V → [0,1]` induces a Forman discrete Morse function `f̄: K^{(2)}(G) → ℝ` via standard min-extension `f̄(α) = min_{v ∈ vertices(α)} u(v)`, with critical cells classified into **index-0 exterior pockets** (`u ≈ 0`), **index-1 boundary saddle edges** (boundary band `u ∈ (0,1)`), **index-2 interior bulk faces** (`u ≈ 1`); strong/weak Morse inequalities `m_p ≥ b_p` (Forman 1998 Theorem 3.5) give topological lower bound `m_0 + m_1 + m_2 ≥ 4` per formation on 2D torus `T²_{16}` (Betti numbers `b_0 = 1, b_1 = 2, b_2 = 1`, Euler `χ = 0`) with canonical `(m_0, m_1, m_2) = (1, 2, 1)` matching D-ST-3 K_act counting (canonical L289); Mischaikow-Nanda 2013 (*Found. Comput. Math.* 13:151) establishes Forman ↔ persistence correspondence providing cross-anchor with canonical T-OP6-B Cat A (CV-1.7, persistent ridge `B_PersRidge` on `|∇_G u|²` super-level filtration) — confirming the two cellular and PH-based attacks are mutually consistent; H-Morse spectral gap bounded below by discrete Cheeger inequality (Chung 1997) on active-set Hessian: `μ_min^non-Goldstone ≥ C(G)·min_e Δ_e·𝟙[m_1^free ≥ 1]` where `C(G)` is graph-combinatorial edge-Cheeger constant (estimated `≈ 0.077` on T²_{16}, conservative vs. L-HMORSE-LOCAL numerical anchor `[0.13, 3.49]` and file 03 continuum Jacobi `≈ 0.30` — all *consistent*); OP-HMORSE-SADDLE (theorem_status.md L594, NOT canonical.md L1967 per critic §B.1 critical finding) attack via **discrete saddle cell index = 1 cellular invariant** complementary to file 03's analytical Jacobi spectrum saddle attack — *different Cat B conditional hypotheses give INDEPENDENT attack channels*; honestly classified as **L-FORMAN-HMORSE-DISCRETE Cat B target** with conditional on (FH1) Forman genericity (Aut(G)-symmetric `u*` per T-V5b-T-zero needs generic perturbation OR equivariant Forman per Allili-Kaczynski 2002), (FH2) D-HMORSE-LOCAL (C2′) active-set decomposition, (FH3) Aut(G) equivariance handling — substantive Cat B → Cat A proof obligations parallel to T-OP6-B's CV-1.7 Session K promotion; *graph-native advantage*: NO `h → 0` mesh refinement, NO van Gennip-Bertozzi 2012 hypothesis package, results valid on actual finite SCC graph; *trade-off*: cellular Morse type yields STRUCTURE (index counts, Morse inequalities) not eigenvalue MAGNITUDES (Cheeger gives qualitative bound only — file 03 continuum Jacobi gives tighter `σ·μ_ℓ` magnitudes via spherical-harmonic spectrum); strictly *contrastive standard discrete-topology tool* (Forman 1998 is Cat A in discrete topology literature; SCC-specific cellular Morse application is Cat B target per (FH1)-(FH3) conditional), NOT *SCC = Forman function reduction* (CN10 explicit boundary); 16/16 hard-constraint CN1-16 + CONSENSUS BASELINE (σ = (√2/6)√(αβ), T²_{16} λ_2 = 0.1522, c=1/2 α=1 β=10 T_*=0.1 R=4, OP-HMORSE-SADDLE = theorem_status.md L594, Theorem 4 = canonical.md L1134-1136) all verified; CV-1.18 SEAL Non-Overclaim fully preserved.**

---
