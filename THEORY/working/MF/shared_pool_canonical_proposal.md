# shared_pool_canonical_proposal.md — Shared-Pool Architecture I9' Canonical Proposal (OAT-4)

**Status:** working draft (OAT-4, post W5 Day 4 morning batch session).
**Type:** Theory-only canonical proposal; Shared-pool architecture I9' formal registration via Tool A1 stratified space framework.
**Author origin:** OAT-4 W6 priority advanced to W5 Day 4 per user "지금 하자" + "모든 도구 적극 활용 + 자율" direction. Tool A1 (stratified space) verification (`mathematical_scaffolding_4tools.md` §2) PASSED — Whitney-stratified semi-algebraic space.
**Canonical refs:** §11 I9 (K-field architecture, line 846 — current binding decision); §11.2 Open Design Choice #8 (line 807 — "K-field decomposition or non-contraction or spectral C_t"); §13 T-Persist-K-Sep/Weak/Unified (line 889-925); §14 CN6 (K kinetically determined); §11.1 #16 Commitment 16 K-status (CV-1.5.1).
**Working refs:** `K_status_commitment.md` (OAT-1, K_field/K_act); `mathematical_scaffolding_4tools.md` §2 Tool A1 stratified verification; `sigma_multi_trajectory.md` §1.1 (shared-pool first appearance); `multi_formation_sigma.md` §1.4 vocabulary.
**Open problems:** OP-0009-A (this file's resolution candidate); OP-0003 MO-1 (re-activation trigger architecture-conditional); OP-0008 σ^A K-jump non-determinism (orthogonal but K-jump is stratum boundary transition).

---

## §1. Mission Statement

> **"Shared-pool architecture I9' (currently working/MF/sigma_multi_trajectory.md only) — canonical 등록 권고. Tool A1 stratified space framework로 K-field architecture I9와의 정합 정식화."**

이 file은 OP-0009-A (Multi-Formation Ontological Foundations sub-item A) 의 resolution candidate.

**핵심 결론**:
- Shared-pool $\widetilde\Sigma^K_M$과 K-field $\Sigma^K_M$은 *충돌 architecture*가 아니라 **같은 Whitney-stratified space의 다른 보기**.
- $\widetilde\Sigma^K_M$ = 전체 stratified space; $\Sigma^K_M$ = top stratum의 codim-(K-1) slice (per-formation mass partition fixed).
- K-jump events = stratum boundary transitions (Tool A1 §2.4).
- T-Persist-K-* family (canonical Cat A/C)는 smooth segments only — scope clause 추가 필요.
- OP-0003 MO-1 re-activation: shared-pool primary 시 Goresky-MacPherson stratified Morse 자동 framework.

**최종 권고**: I9' shared-pool architecture를 canonical에 등록 (§11 신규 또는 I9 본문에 추가). I9 K-field와 I9' shared-pool은 *complementary modeling layers* (CN10 contrastive — same underlying ontology, different analytical perspectives).

---

## §2. Architecture Comparison

### §2.1 K-field architecture I9 (canonical, current binding decision)

**Definition** (canonical line 846):
$$\Sigma^K_M = \Sigma_{m_1} \times \cdots \times \Sigma_{m_K} = \prod_{j=1}^K \big\{ u^{(j)} \in [0, 1]^{|X|} : \sum_x u^{(j)}(x) = m_j \big\}$$
Cartesian product manifold; **K and $\{m_j\}_{j=1}^K$ fixed externally** at architecture instantiation.

**Properties**:
- Smooth manifold (product of simplices).
- Dimension: $\sum_{j=1}^K (|X| - 1) = K(|X| - 1)$.
- T-Persist-K-Sep/Weak/Unified (canonical §13) all proved on this manifold.
- `scc/multi.py` `find_k_formations` direct implementation.

### §2.2 Shared-pool architecture I9' (working only, sigma_multi_trajectory.md)

**Definition** (per `sigma_multi_trajectory.md` §1.1, formalized in `mathematical_scaffolding_4tools.md` §2.1):
$$\widetilde\Sigma^K_M := \big\{ \mathbf{u} = (u^{(1)}, \ldots, u^{(K_{\mathrm{field}})}) : \sum_{j,x} u^{(j)}(x) = M, \sum_k u^{(k)}(x) \leq 1\;\forall x \big\}$$
**Total mass** $M$ conserved; **per-formation $m_j$ variable** (formation can grow / shrink / disappear).

**Properties**:
- Whitney-stratified semi-algebraic space (Tool A1 verification PASSED).
- Stratification: $\widetilde\Sigma^K_M = \bigsqcup_{K_{\mathrm{act}}=0}^{K_{\mathrm{field}}} S_{K_{\mathrm{act}}}$.
- $S_{K_{\mathrm{act}}}$ = stratum of dimension $K_{\mathrm{act}}(|X| - 1) - 1$ (one less for total mass conservation).
- K-jump events = stratum boundary transitions ($S_K \to S_{K-1}$ codim-1).

### §2.3 Relationship — Complementary Modeling-Layer Commitments per Whitney Stratification

**Theorem 2.3** (formalization of OAT-supplementary §2.3 Claim 2.3): K-field architecture $\Sigma^K_M$ equals top stratum $S_{K_{\mathrm{field}}}$ of shared-pool $\widetilde\Sigma^K_M$ intersected with per-formation mass partition slice $\{m_j = m_{j,0}\;\forall j\}$.

**Formal**:
$$\Sigma^{K_{\mathrm{field}}}_M = S_{K_{\mathrm{field}}} \cap \{m_j(\mathbf{u}) = m_{j,0}\;\forall j\}$$
where $m_j(\mathbf{u}) = \|u^{(j)}\|_1$, and $\{m_{j,0}\}_{j=1}^{K_{\mathrm{field}}}$ are external parameters with $\sum_j m_{j,0} = M$.

**Codimension**: K_field - 1 (mass partition fixes K_field-1 free parameters).

→ K-field is *codim-(K-1) slice* of top stratum; shared-pool is *full top stratum + lower strata*.

**Corollary 2.3.1 (Complementary modeling-layer commitments).** Under the Whitney stratification of `mathematical_scaffolding_4tools.md` §2.2, I9 and I9' are **not competing architectures** but **complementary commitments at distinct modeling layers** of the same Whitney-stratified semi-algebraic ambient space $\widetilde\Sigma^K_M$:

| Modeling layer | Architecture | Stratum content | Mass regime | Analytical role |
|---|---|---|---|---|
| Static, fixed-K (within smooth segment) | I9 K-field | Codim-$(K-1)$ slice of $S_{K_{\mathrm{field}}}$ | Per-formation $m_j$ fixed externally | Per-formation persistence (T-Persist-K-Sep / Weak / Unified), σ_multi^A static (D-6a) |
| Dynamic, variable-K (across K-jump events) | I9' Shared-pool | Full $\widetilde\Sigma^K_M = \bigsqcup_{K_{\mathrm{act}}} S_{K_{\mathrm{act}}}$ | Total $M$ conserved; $m_j$ variable | σ_multi^A(t) trajectory (D-6b dynamic), Goresky-MacPherson stratified Morse (NQ-248), LSW coarsening |

**Whitney-stratification rationale for complementarity**:
- The frontier condition (Whitney (A)/(B) regularity, `mathematical_scaffolding_4tools.md` §2.2 (ii)-(iv)) ensures **smooth strata are analytically self-contained**: a trajectory confined to $S_{K_{\mathrm{field}}}$ is governed entirely by smooth-manifold gradient flow, which is precisely the I9 K-field setting.
- Stratum-boundary transitions (K-jumps, §2.4 below) occur only at codim-1 frontier crossings; between such crossings the I9 description is exact on $S_{K_{\mathrm{field}}} \cap \{m_j = m_{j,0}\,\forall j\}$.
- Therefore: **I9 is a faithful local chart of I9'** within smooth segments, and I9' is the **globally consistent ambient** required to reason across K-jumps.
- This is the layered relationship between an open dense top-stratum manifold and its Whitney-stratified closure — a *standard pattern* in stratified geometry (Goresky-MacPherson 1988 §I.1.1; Mather 2012 §3), not an SCC-specific compromise.

**Implication for Commitment 16 (K-status)**: K_field/K_act layer-distinction (CV-1.5.1) is the **modeling-layer reflex** of the I9/I9' complementarity:
- $K_{\mathrm{field}}$ is the architectural cap → fixed at instantiation → corresponds to choosing I9 (top-stratum-only) vs. I9' (full stratification).
- $K_{\mathrm{act}}(\mathbf{u})$ is the dynamical observable → varies along trajectory → indexes the active stratum $S_{K_{\mathrm{act}}}$ in I9'.
- The "two-tier" structure of Commitment 16 is *forced* by the Whitney-stratified geometry once shared-pool is admitted — not an extra ontological commitment but the natural read-out of stratum-membership.

→ **Practical consequence**: a modeler choosing I9 commits to "fixed-K smooth-segment analysis only"; choosing I9' commits to "full multi-formation lifecycle including birth/extinction/merger". Both commitments rest on the *same* stratified ambient and the *same* primitive $u_t$; they differ only in **which stratum-content is admitted as analytically active**.

---

## §3. Tool A1 Stratified Space Verification (recap from OAT-supplementary)

### §3.1 Whitney stratification verified

(See `mathematical_scaffolding_4tools.md` §2.2 for full verification.)

- ✅ Locally closed strata (each $S_{K_{\mathrm{act}}}$ smooth manifold of well-defined dimension).
- ✅ Frontier condition ($\overline{S_{K_1}} \cap S_{K_2} \neq \emptyset \Rightarrow \overline{S_{K_1}} \supseteq S_{K_2}$).
- ✅ Whitney (A) tangent regularity.
- ✅ Whitney (B) secant regularity (semi-algebraic 일반론, Hironaka 1973 — verified McKay-citation-corrected per external references audit).

### §3.2 K-jump as codim-1 transition

K-jump event $t^*$ with $\Delta K_{\mathrm{act}} = 1$ (single merger): trajectory crosses $\partial S_{K_{\mathrm{act}}(t^{*-})}$ into $S_{K_{\mathrm{act}}(t^{*-}) - 1}$. Codimension 1 (one formation's mass $m_j \to 0$).

### §3.3 Goresky-MacPherson stratified Morse applicability

Stratified Morse theory (Goresky-MacPherson 1988) applies to Whitney-stratified spaces. For $\widetilde\Sigma^K_M$:
- Critical points of $\mathcal{E}_K|_{\widetilde\Sigma^K_M}$ are *stratum-wise critical*.
- Morse index well-defined per stratum.
- Inter-stratum analysis via tangent cone variation theorem.

→ **MO-1 multi-formation re-activation 자연 framework** (OP-0003 conditional).

---

## §4. Architecture Choice Logic

### §4.1 When to use K-field I9

- **Short-time analysis**: Within smooth segment (no K-jump), K-field architecture sufficient.
- **Static σ_multi^A**: D-6a Multi-Static (CV-1.5.1 T-Commitment-14-Multi-Static C-0717) on $\widetilde\Sigma^{K,\circ}_M$ interior (Option A pragmatic) — top stratum 한정.
- **Per-formation persistence**: T-Persist-K-Sep (well-separated), T-Persist-K-Weak (overlapping) all assume K_act = K_field constant.
- **Computational implementation**: `scc/multi.py` per-formation arrays pre-allocated.
- **Cognitive correlate**: K attended objects (Pylyshyn 1989 multi-object tracking K-slots).

### §4.2 When to use Shared-pool I9'

- **Long-time dynamics**: K-jump events mandatory (formation merger / extinction / nucleation).
- **σ_multi^A(t) trajectory**: D-6b dynamic (W6+ via NQ-242) requires shared-pool.
- **LSW coarsening**: K_act → 1 long-time generic state.
- **Stratified Morse**: NQ-248 multi-formation Morse on stratified space.
- **Cognitive correlate**: Perceptual binding with variable formation count (gestalt fission/fusion).

### §4.3 Both admissible — complementary modeling-layer commitments

I9 vs I9' is **architectural choice** (complementary modeling-layer commitments per Whitney stratification, Corollary 2.3.1). Both rest on:
- Soft cohesion field $u_t$ as primitive (Commitment 1).
- K_field as architectural cap (Commitment 16).
- K_act as derived diagnostic (Commitment 16).
- The *same* Whitney-stratified ambient $\widetilde\Sigma^K_M$ (Tool A1, `mathematical_scaffolding_4tools.md` §2.2 verified PASSED).

→ Commitment 16의 layer-distinction logic이 architecture choice에도 자동 적용. Modeler chooses I9 (short-time, fixed-K, top-stratum codim-(K-1) slice) vs I9' (long-time, dynamic-K, full stratification) per analysis context. **Choice is layer-of-description, not ontology** — both architectures track the *same* stratified semi-algebraic ambient and the *same* primitive $u_t$.

### §4.3.1 Honest acknowledgment of contrastive scope (CN10)

The Whitney-stratified ambient $\widetilde\Sigma^K_M$ and its Goresky-MacPherson stratified Morse machinery are **standard mathematical scaffolding** (Tool A1 + A2), imported per CN10 *contrastively* — not as reductive identification of SCC with stratified-geometry textbook content. Two explicit honest acknowledgments anchor this scope:

1. **SCC λ_rep bilinear ≠ KKT Lagrange multiplier exactly** (per `mathematical_scaffolding_4tools.md` §5.4 partial fail; OAT-3 `lambda_rep_ontology.md` Argument B preferred over Argument C strict). The cross-formation coupling $\sum_{j<k} \lambda_{\mathrm{rep}} \langle u^{(j)}, u^{(k)}\rangle$ on $\widetilde\Sigma^K_M$ enforces simplex-like inequality $\sum_k u^{(k)}(x) \leq 1$ *softly*; it is not the strict KKT multiplier of that constraint and is not a 5th conceptually-independent energy term (CN5 within-formation 4-term independence preserved). I9' shared-pool does **not** override this — it inherits the same architectural-layer coupling on every stratum.

2. **Whitney/Goresky-MacPherson framework is contrastive scaffolding** — SCC's primitive remains $u_t$ (graded soft cohesion field), not a stratification-theoretic primitive. The strata $S_{K_{\mathrm{act}}}$ are *derived* from $K_{\mathrm{act}}$ readout (Commitment 16), not imposed externally. Stratified Morse is invoked when needed (NQ-248 W7+); it does not become canonical machinery wholesale. This honors CN10 contrastive policy (canonical §14): structural correspondence ≠ reductive identification.

Both acknowledgments are *load-bearing* for CV-1.6 packet — silently importing standard frameworks without explicit contrastive scope would violate CN10 and over-claim mathematical content.

### §4.4 Recommended primary

Per OAT-supplementary §A1 + 4-에이전트 architect verdict: **Shared-pool I9' as ontologically primary**; K-field I9 as **codim-(K-1) slice for static analysis convenience**.

**Reason**: 
- K-jump events (long-time generic state) live in shared-pool naturally.
- Stratified Morse (Goresky-MacPherson) standard on shared-pool.
- K-field is *recovered* by additional constraint (mass partition fixing).
- Commitment 16 K-status decomposition naturally aligns with shared-pool (K_act emerges in shared-pool dynamics).

**Caveat**: T-Persist-K-* canonical theorems all proved on K-field. Re-proving on shared-pool is *not* W6 budget. Recommendation: **scope clauses** added to T-Persist-K-* (smooth segments only).

---

## §5. Recommended Canonical Edits at CV-1.6 (D-CV1.6-O2)

### §5.1 New §11 Architectural Commitment block (proposed)

Canonical §11 K-field architecture paragraph (line 846)에 다음 신규 block 추가:

```markdown
### Shared-Pool Architecture I9' (W6+ added 2026-04-30, CV-1.6 candidate)

Beyond the K-field architecture I9 (per-formation mass $m_j$ fixed externally), 
the **shared-pool architecture I9'** admits per-formation mass variation under 
total mass conservation:

$$\widetilde\Sigma^K_M := \big\{ \mathbf{u} = (u^{(1)}, \ldots, u^{(K_{\mathrm{field}})}) : 
  \sum_{j,x} u^{(j)}(x) = M, \sum_k u^{(k)}(x) \leq 1\;\forall x \big\}.$$

The shared-pool is a Whitney-stratified semi-algebraic space (Tool A1, 
`working/MF/mathematical_scaffolding_4tools.md` §2.2 verified):

$$\widetilde\Sigma^K_M = \bigsqcup_{K_{\mathrm{act}}=0}^{K_{\mathrm{field}}} S_{K_{\mathrm{act}}}$$

stratified by active formation count $K_{\mathrm{act}}$ (per Commitment 16). 

The K-field architecture I9 is recovered as the codim-$(K_{\mathrm{field}}-1)$ slice 
of the top stratum:

$$\Sigma^{K_{\mathrm{field}}}_M = S_{K_{\mathrm{field}}} \cap \{m_j(\mathbf{u}) = m_{j,0}\;\forall j\}.$$

I9 and I9' are **complementary modeling-layer commitments** (per CN10 contrastive 
+ Commitment 16 layer-distinction): I9 for short-time analysis at fixed K; I9' for 
long-time dynamics including K-jump events. Per-formation persistence theorems 
(T-Persist-K-Sep / Weak / Unified) operate within smooth segments of either 
architecture. K-jump events are stratum boundary transitions in I9'; per Tool A3 
persistent homology framework (Commitment 17 (c)), σ_multi^A(t) trajectory is 
naturally formulated on I9' shared-pool with computational topology pipeline 
(NQ-242 W6+).

Multi-formation Morse theory (NQ-248 W7+) operates on I9' stratified space via 
Goresky-MacPherson stratified Morse standard (resolves OP-0003 MO-1 re-activation 
at multi-formation level if I9' canonical primary).
```

### §5.2 T-Persist-K-* Scope Clause Addition

Each T-Persist-K-* entry (canonical §13 line 889-925) appended with scope clause:

```markdown
*Scope clause (W6+ added 2026-04-30):* This theorem applies on **smooth segments** 
where $K_{\mathrm{act}}$ is constant (no K-jump events within transition window 
$[t, s]$). K-jump transitions are stratum boundary transitions in shared-pool 
architecture I9' (canonical §11); multi-formation persistence across K-jumps is 
deferred to D-6b dynamic σ_multi^A(t) (W6+ via NQ-242).
```

### §5.3 OP-0003 MO-1 entry update (architecture-conditional re-activation)

`theorem_status.md` (Open Problems Catalog) OP-0003 MO-1 entry (이미 W5 Day 3 EOD CV-1.5.1에 rider 추가됨):

```markdown
**Re-activation trigger (W5 Day 3 EOD + W6+ formalized):** 
- D-6b dynamic σ_multi^A(t) approval at CV-1.6 OR NQ-248 multi-formation 
  stratified Morse work begins → 🟠 HIGH automatic re-activation.
- **W6+ formalization (2026-04-30 OAT-4)**: I9' shared-pool architecture 
  canonical 등록 시 (CV-1.6 D-CV1.6-O2), MO-1 re-activation은 **Goresky-MacPherson 
  stratified Morse standard framework**로 처리됨 (NQ-248 6-10 weeks effort, 
  Cat A target). I9 K-field 한정 사용 시 SIDESTEPPED 보존.
```

### §5.4 OP-0009-A Status Update

CV-1.6 시점 OP-0009-A: **PARTIALLY RESOLVED**. I9' shared-pool architecture canonical 등록 (proposed §5.1) + I9와의 stratified space 관계 형식화 (Tool A1 verification + this file §2.3 Theorem). Both architectures complementary modeling-layer commitments.

### §5.5 Net canonical impact

- Lines added: ~40-50 (§5.1 ~30 + §5.2 ~5×3 = ~15 + OP status ~5).
- Predicate / energy 변경: 0 (CN10 maintain).
- Theorem status: 0 (T-Persist-K-* statements unchanged; only scope clauses added).

---

## §6. Tool A1 + Commitment 17 Consistency

This file's I9' canonical proposal is *identical content* to OAT-supplementary `mathematical_scaffolding_4tools.md` §8.2 stratified space §3.10 entry proposal + Commitment 17 (a) Mathematical Scaffolding.

→ I9' canonical 등록 + Commitment 17 등록은 **double registration redundant**. 

**Recommended approach** at CV-1.6:
- **Option D-CV1.6-O2 + O5 합쳐서**: Commitment 17 (a) 등록 시 I9' 정의를 *Commitment 17 안에서* 명시; §11 separate I9' entry 안 만듦. Net effect: single Commitment 17 covers (a) stratified space (I9') + (b) quotient + (c) PH + (d) N-phase contrast.

또는

- **Option D-CV1.6-O2 separate**: §11 I9' as standalone architectural commitment (§5.1 text); Commitment 17 cross-references §11 I9' entry. Net effect: more structured canonical.

**Preference**: Option separate (more structured). I9' 등록은 *architectural commitment*; Commitment 17은 *meta-mathematical scaffolding commitment*. 둘은 different ontological levels.

---

## §7. K-jump dynamics on shared-pool

### §7.1 K-jump as stratum boundary transition

Per Tool A1 §2.4 (verified): K-jump event at $t^*$ with $\Delta K_{\mathrm{act}} = 1$ corresponds to gradient flow trajectory crossing $\partial S_{K_{\mathrm{act}}(t^{*-})}$ into $S_{K_{\mathrm{act}}(t^{*-})-1}$.

**Mathematical content**:
- One formation $u^{(j)}$ has $m_j(\mathbf{u}(t)) \to 0$ as $t \to t^*$.
- At $t^*$: $u^{(j)}(t^*) = 0$ (formation extinct).
- Stratum index drops by 1.

### §7.2 σ^A K-jump non-determinism (OP-0008)

Per `sigma_multi_trajectory.md` Lemma 4.4.1(c) (now Cat C per Critic C3 정정 — agent 보강 완료):
> σ^A(t*+) is NOT deterministic in σ^A(t*-) alone. Merger geometry data $\mathcal{M}$ (which formations merged, post-merger relaxation) required.

**Tool A3 PH reformulation** (per OAT-supplementary §4.3): σ^A K-jump 비결정성 = **standard PH fact** (0-dim barcode ↛ 1-dim barcode at critical events, Cohen-Steiner 2007 + Carlsson-de Silva-Morozov 2009 zigzag standard).

→ σ^A K-jump 비결정성은 **shared-pool architecture I9' 위에서 자연스러운 mathematical content** (stratum boundary transition + standard PH). 별도 ontological 문제 아님; 단지 *standard mathematical caveat*.

---

## §8. R23 Empirical Anchor (per OAT-7 finding)

### §8.1 R23 fullscale dataset

Per OAT-7 (scientist agent, `single_high_F_equivalence.md`, 511 lines): R23 fullscale dataset analysis:
- 56 stable minimizers on 32×32 D₄ free-BC grid.
- $\mathcal{F} \in [5, 63]$ (mean 40.6) — F=63 maximum (이전 F=9 추정 outdated).
- $K_{\mathrm{step}} \in [1, 8]$.
- All 56: $\mathcal{F} > K_{\mathrm{step}}$ (100% gap > 0).

### §8.2 H1 (F-multi ↔ K-multi equivalence): PARTIAL

Conjecture BC-1 (OAT-2 §3.6) per-formation $\{u^{(j)*}\}$ ↔ aggregate $\mathrm{lobes}(U^*)$ bijection at *well-separated K-field*. R23 analysis shows: well-separated $K_{\mathrm{step}} = \mathcal{F}$ regime is **null set** in R23 (all 56 minimizers have $\mathcal{F} > K_{\mathrm{step}}$).

→ BC-1 conjecture는 **non-trivial** — well-separated 가정이 R23 ground state regime에서 *generic하지 않음*. 

**Implication for shared-pool**: R23 generic state는 **overlapping regime** (T-Persist-K-Weak territory). Shared-pool architecture I9'에서 자연스럽게 다뤄짐 (per-formation mass variable + simplex constraint $\sum_k u^{(k)}(x) \leq 1$ active).

### §8.3 OP-0009-Emp partial resolution via R23

OP-0009-Emp (R23 F=9 σ verification): per OAT-7 NQ-141 σ-irrep correspondence high-F validity CONFIRMED (324 obs, 0 exceptions, p < 10^{-98} under random irrep). σ-framework Cat A 클레임이 high-F regime에서도 empirical anchor 유지.

→ Shared-pool I9' canonical 등록은 R23 dataset의 *natural ambient space*; K-field I9는 *static slice* analysis.

---

## §9. Hard Constraint Verification

- [x] **canonical 직접 수정 0**: `working/MF/`. §5 proposals conditional on user approval.
- [x] **Silent resolution 0**: I9' canonical proposal explicit; OP-0009-A status PARTIALLY RESOLVED; T-Persist-K-* scope clauses 명시.
- [x] **u_t primitive maintained**: shared-pool 위에서도 per-formation $u^{(k)}$ 정의됨; K-field와 동일 ontology.
- [x] **4-energy 항 not merged**: λ_rep는 OAT-3 Argument B (architectural-layer) 처리; shared-pool 위에서도 동일.
- [x] **Closure not idempotent**: 변경 없음.
- [x] **CN10 contrastive**: I9 vs I9'은 *complementary modeling-layer commitments*, not external reduction.
- [x] **K not dual-treated abusively**: Commitment 16 (K_field/K_act) layer-distinction이 architecture choice에 자연 확장.
- [x] **No metastability claim without P-F flag**: K-jump events는 dynamics; static σ_multi^A는 P-F-free.
- [x] **No reductive equation**: Standard N-phase Allen-Cahn과 contrastive (per OAT-3 Tool A4 partial fail finding).

---

## §10. Cross-References

- `K_status_commitment.md` (OAT-1 CV-1.5.1): K_field/K_act decomposition 정의.
- `mathematical_scaffolding_4tools.md` (OAT-supplementary): §2 Tool A1 stratified space full verification.
- `sigma_multi_trajectory.md` (D-6b dynamic): shared-pool first appearance, Theorem 4.6.1 Cat B/C.
- `multi_formation_sigma.md` (D-6a static): K-field architecture σ_multi^A static, Approach A.
- `lambda_rep_ontology.md` (OAT-3): λ_rep architectural-layer parameter consistent across I9 + I9'.
- `cobelonging_vs_sigmaD.md` (OAT-5): C_t status architecture-conditional (K-field 4a primary 가정).
- `pre_objective_K_field_tension.md` (OAT-6): pre-objective + K-field tension Path A+C+Tool A2 hybrid (shared-pool primary 함의 일부 포함).
- `single_high_F_equivalence.md` (OAT-7): R23 F=63 generic state는 overlapping regime → shared-pool 자연.
- canonical §11 I9 (line 846): K-field current binding decision.
- canonical §11.2 #8 (line 807): Open Design Choice multi-formation architecture.
- canonical §13 T-Persist-K-Sep/Weak/Unified (line 889-925): scope clause target.
- daily/2026-04-30/02_4tool_mapping_summary.md.

---

## §11. Recommendation Summary

**Recommendation**: APPROVE Shared-pool architecture I9' canonical registration at CV-1.6 D-CV1.6-O2.

**Effort**: ~40-50 canonical lines (§5.1 I9' entry + §5.2 T-Persist-K-* scope clauses ×3 + §5.3 OP-0003 status formalization + §5.4 OP-0009-A status).

**Net effect**:
- I9 vs I9' "충돌 architecture" 4-month implicit ambiguity → 1 explicit relationship (codim-(K-1) slice of top stratum).
- T-Persist-K-* family scope clauses 추가 (smooth segments only).
- MO-1 multi-formation re-activation Goresky-MacPherson framework 명시.
- σ_multi^A(t) D-6b path (W6+) 자연스럽게 shared-pool 위에서 작동.
- OP-0009-A PARTIALLY RESOLVED.

**Pending**:
- R23-style dataset에서 I9' shared-pool 위 stratified Morse 직접 검증 (NQ-248 W7+).
- T-Persist-K-* re-proof on shared-pool (W6+ effort, optional — scope clauses sufficient for now).

---

## §12. Wave 3 Revision Log

### Revision W3-OAT-4 (2026-04-30, worker-2 / wave-3-oat-deepening-team-work / task 2)

**Scope**: OAT-4 shared-pool I9' refinement — strengthen Tool A1 stratified-space integration; explicit framing of K-field I9 + Shared-pool I9' as complementary modeling-layer commitments per Whitney stratification; explicit CN10 honest-acknowledgment block for contrastive scope.

**Edits applied**:

1. **§2.3 promoted to "Relationship — Complementary Modeling-Layer Commitments per Whitney Stratification"**:
   - Added **Corollary 2.3.1** with explicit table mapping {static fixed-K ↔ I9 ↔ codim-(K-1) slice of top stratum} vs {dynamic variable-K ↔ I9' ↔ full $\bigsqcup_{K_{\mathrm{act}}} S_{K_{\mathrm{act}}}$}.
   - Added **Whitney-stratification rationale for complementarity**: cited frontier condition + (A)/(B) regularity from `mathematical_scaffolding_4tools.md` §2.2 (ii)–(iv); identified I9 as a faithful local chart of I9' on smooth segments; identified I9' as the globally consistent ambient required across K-jumps.
   - Identified the I9/I9' relationship as the **standard pattern** of "open dense top stratum within Whitney-stratified closure" (Goresky-MacPherson 1988 §I.1.1; Mather 2012 §3) — *not* an SCC-specific compromise.
   - Connected Commitment 16 K_field/K_act two-tier decomposition (CV-1.5.1) to the **modeling-layer reflex** of I9/I9' complementarity: the two-tier structure is *forced* by the stratified geometry once shared-pool is admitted, not an extra ontological commitment.

2. **§4.3 retitled "Both admissible — complementary modeling-layer commitments"** with explicit reference back to Corollary 2.3.1; clarified that the architectural choice is "layer-of-description, not ontology"; both rest on the *same* stratified ambient and *same* primitive $u_t$.

3. **§4.3.1 (new) Honest acknowledgment of contrastive scope (CN10)** — two load-bearing acknowledgments added per task directive:
   - **(a)** SCC bilinear $\sum_{j<k} \lambda_{\mathrm{rep}} \langle u^{(j)}, u^{(k)}\rangle$ ≠ KKT Lagrange multiplier exactly (cross-ref `mathematical_scaffolding_4tools.md` §5.4 partial fail and OAT-3 `lambda_rep_ontology.md` Argument B preferred). I9' inherits the same architectural-layer coupling on every stratum — it does not override the partial-fail finding.
   - **(b)** Whitney/Goresky-MacPherson framework is contrastive scaffolding, not reductive identification: $u_t$ remains primitive; strata $S_{K_{\mathrm{act}}}$ are derived from $K_{\mathrm{act}}$ readout (Commitment 16), not imposed externally; stratified Morse is invoked only as needed (NQ-248 W7+), not promoted to canonical machinery wholesale.
   - Both acknowledgments flagged as **load-bearing for CV-1.6 packet** — silently importing standard frameworks without explicit contrastive scope would violate CN10 and over-claim mathematical content.

**Hard-constraint impact** (re-checked post-edit):
- canonical 직접 수정: still 0 (all edits in `working/MF/`).
- CN10 contrastive: **strengthened** — now load-bearing explicit, not implicit.
- u_t primitive: **strengthened** — explicit reaffirmation in §4.3.1 (b).
- 4-energy not merged: **strengthened** — λ_rep architectural-layer status now explicit on shared-pool, not just K-field.
- Silent resolution: still 0; OP-0008/OP-0009-A status unchanged.

**3-bullet summary (per task report directive)**:
- **Whitney-stratification framing of I9/I9' as complementary modeling-layer commitments was promoted from §2.3 prose to formal Corollary 2.3.1** with table + standard-pattern citation (Goresky-MacPherson 1988, Mather 2012); Commitment 16 two-tier K-status now derived as the modeling-layer reflex of stratified geometry, not an extra commitment.
- **Tool A1 stratified-space integration tightened** with explicit cross-citations to `mathematical_scaffolding_4tools.md` §2.2 (i)–(iv) regularity verifications; I9 reframed as "faithful local chart of I9' on smooth segments" and I9' as "globally consistent ambient across K-jumps" — making the inter-architecture relationship analytically operational, not just nominal.
- **CN10 contrastive scope made load-bearing via §4.3.1** with two honest acknowledgments: (a) SCC λ_rep bilinear ≠ KKT Lagrange multiplier exactly (Argument B preferred over Argument C strict), and (b) Whitney/Goresky-MacPherson is contrastive scaffolding only — preventing CV-1.6 packet from over-claiming reductive mathematical content while preserving the structural correspondence.

---

**End of shared_pool_canonical_proposal.md (OAT-4 deliverable, Wave 3 revised 2026-04-30).**
**Status: working draft. Shared-pool I9' canonical registration via Tool A1 stratified space framework. K-field I9 = codim-(K-1) slice of top stratum. I9 / I9' = complementary modeling-layer commitments per Whitney stratification (Corollary 2.3.1). T-Persist-K-* scope clauses (smooth segments only). MO-1 re-activation Goresky-MacPherson natural. CN10 contrastive scope load-bearing (§4.3.1). OP-0009-A PARTIALLY RESOLVED at CV-1.6.**
**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/MF/shared_pool_canonical_proposal.md`
**Created:** 2026-04-30 (W5 Day 4 morning, OAT-4 advanced from W6 Day 2).
**Wave 3 revised:** 2026-04-30 (worker-2, wave-3-oat-deepening-team-work task 2).
**Promotion target:** CV-1.6 W6 Day 7 morning (D-CV1.6-O2 candidate).
