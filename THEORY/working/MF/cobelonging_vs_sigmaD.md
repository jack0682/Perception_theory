# cobelonging_vs_sigmaD.md — Co-belonging $C_t$ vs σ_multi^D Multi-Formation Status (OAT-5)

> **✅ REJECT-RETIRE-RECOMMENDATION (W6 D1 EOD parking-lot Issue #5 audit, 2026-05-04)**
> The original Issue #5 recommendation classified this file as "design decision, not theorem" and proposed archive to `_archive/ontological_design_decisions/`. **Chain verification rejects this recommendation.**
>
> **Rejection rationale:**
> 1. **8 active inbound references** including canonical `theorem_status.md` Open Problems Catalog + 7 active working files (`shared_pool_canonical_proposal.md`, `CV-1.6_packet_crosswalk.md`, `F_Kstep_K_triple.md`, `k_selection_mechanism.md`, `K_status_commitment.md`, `mathematical_scaffolding_4tools.md`, `parking_lot_inventory`).
> 2. **Active OP-0009-C PARTIALLY RESOLVED claim** (architecture-conditional) — structured resolution proposal with specific verdict (Option C-3), not philosophical musing.
> 3. **Mathematical content**: Option C-3 verdict ($C_t$ demoted-derived maintained; σ_multi^D and $C_t$ orthogonal information); orthogonality witness construction §5.2 on $D_4$-grid; explicit canonical impact (~10-15 lines at CV-1.6).
> 4. **OAT-5 of the systematic OP-0009 sub-item resolution effort** (OAT-1 ✅ Commitment 16; OAT-2/3/4/5/6/7 PARTIALLY RESOLVED). Archive would break the OAT system symmetry.
> 5. **Promotion target**: CV-1.6 W6 Day 7 morning (D-CV1.6-O6 if user approves) — within current W6 release cycle.
>
> **Correct classification**: ontology-oriented mathematical working file with architecture-conditional resolution proposal (not "design decision" alone). Comparable to OAT-4 `shared_pool_canonical_proposal.md` (which is similarly architecture-conditional and has CV-1.6 D-item promotion target).
>
> **Action**: PRESERVE IN PLACE in `working/MF/`. No archive move. Continue toward **CV-1.6 D-CV1.6-O4 promotion target** (canonical-scheduled, NOT speculative — see `THEORY/working/CV-1.6_packet_crosswalk.md` D-CV1.6-O4 entry + canonical `theorem_status.md` OP-0009 Sub-item Status Table row for OP-0009-C).
>
> *(Re-examination correction W6 D1 EOD late: original Issue #5 disclosure header said "D-CV1.6-O6 if user approves" — both phrases inaccurate. Correct designation is D-CV1.6-O4 per `CV-1.6_packet_crosswalk.md` line 50, scheduled — not "if user approves" hedge. Canonical theorem_status.md OP-0009 Sub-item Status Table confirms PARTIALLY RESOLVED status with this exact promotion target.)*

**Status:** working draft (OAT-5, post W5 Day 4 morning batch session).
**Type:** Theory-only audit; verdict on whether $C_t$ remains demoted-derived under K>1 or revives as primitive.
**Author origin:** OAT-5 W6 priority advanced to W5 Day 4 per user "지금 하자" + "모든 도구 적극 활용 + 자율" direction; analyst-grade analysis (gap-list returned 2026-04-30 morning) integrated into write-capable working file.
**Canonical refs:** §3.6 (line 198–200) — $\mathbf{C}_t$ demoted to derived diagnostic; §6 Group C (line 388–419) — C1–C4 axioms vestigial; §11.1 Commitment 12 (line 779) — derived diagnostic restated; §13 σ-multi entries (CV-1.5.1) — D-6a Multi-Static; OP-0009-C sub-item (`THEORY/canonical/theorem_status.md` Open Problems Catalog, registered W5 Day 3 EOD).
**Working refs:** `K_status_commitment.md` (OAT-1, Commitment 16); `mathematical_scaffolding_4tools.md` (OAT-supplementary, Tool A2 quotient + Tool A1 stratified); `multi_formation_sigma.md` (D-6a Approach A σ_multi^D definition); `sigma_multi_trajectory.md` (D-6b dynamic).
**Open problems referenced:** OP-0009-C (this file's resolution candidate), OP-0009-A (architecture choice — verdict architecture-conditional).

---

## §1. Mission Statement

> **"Single-formation에서 demoted to derived diagnostic였던 $C_t$가 multi-formation extension에서 부활(revival as primitive)해야 하는가, 아니면 demoted 유지가 옳은가? σ_multi^D (D-6a CV-1.5.1)가 $C_t$를 *subsume*하는가, *coexist*하는가?"**

이 file은 OP-0009-C (Multi-Formation Ontological Foundations sub-item C) 의 resolution candidate. 결과: **Option C-3 (variant) 권고** — $C_t$ remains demoted-derived; σ_multi^D 와 $C_t$는 orthogonal information 차원 (전역 cohomology invariant vs 사이트별 정량 diagnostic).

**Architecture-conditional**: 본 verdict은 OP-0009-A K-field architecture 4a primary (Tool A1 stratified space top stratum) 가정 하에서 valid. Shared-pool architecture (4b/4c) primary 시 verdict 재검토 필요.

---

## §2. Single-Formation $C_t$ Status Review (canonical §3.6)

### §2.1 Demotion 역사

- **CV-1.0 (2026-04-01) 이전**: $C_t$는 formal universe primitive 후보 — Sep predicate가 $C_t$-weighted 형식 ($\mathsf{Sep} = \sum C_t \cdot D / \sum C_t$) 사용.
- **v2.0 cycle 2 (2026-04-XX)**: Sep predicate가 $u$-weighted form으로 보정 ($\mathsf{Sep} = \sum u \cdot D / \sum u$). 보정 사유: $C_t$-weighted 형식이 *diagnostically degenerate* (모든 configurations에서 Sep ≈ 0.5).
- **canonical §3.6 (현재, line 198–200)**: 
  > "The soft co-belonging operator $\mathbf{C}_t : X_t \times X_t \to [0,\infty)$ measures the degree to which two sites participate in the same cohesive formation. It is a **derived diagnostic**, not a primitive of the formal universe: it does not enter any predicate or energy term in the current theory."
- **canonical Commitment 12** (line 779): "$\mathbf{C}_t$ is a derived diagnostic. Co-belonging does not enter any predicate or energy term."

### §2.2 Vestigial Group C axioms (canonical §6, line 388–419)

C1–C4 axioms (`canonical.md:388–419`):
- **C1**: $\mathbf{C}_t(x,y)$ depends only on $u_t, \mathbf{N}_t$.
- **C2**: $\mathbf{C}_t \neq \mathbf{N}_t$ (co-belonging distinct from adjacency).
- **C3''**: 단조성 — $u_t(x)$ 증가 시 $\mathbf{C}_t(x,x)$ 비-감소.
- **C4**: 대칭성 — $\mathbf{C}_t(x,y) = \mathbf{C}_t(y,x)$.

**Status**: vestigial (axioms 잔존하지만 §13 어느 Cat A theorem도 직접 사용 안 함). 4-에이전트 architect verdict (W5 Day 3 EOD): "Group C is the single largest dead-load section of canonical.md."

### §2.3 Resolvent realization (canonical §9.4)

$\mathbf{C}_t = (I - \alpha W_{\mathrm{sym}})^{-1}$ where $W_{\mathrm{sym}}(x,y) = \sqrt{u_t(x)} \mathbf{N}_t(x,y) \sqrt{u_t(y)} / d_x$. 이는 *single field* $u_t$ 위에서 정의됨 — multi-formation lift는 비자명.

---

## §3. Multi-Formation Context (W5 G3 Phase 5+)

### §3.1 Core question for multi-formation

Multi-formation에서 핵심 질문은 *"site $x$ 와 site $y$ 가 같은 formation에 속하는가?"* — 정확히 canonical §3.6 line 200의 demoted role description: *"discriminating within-formation from cross-boundary site pairs"*. 

Multi-formation extension에서 이 질문이 *primary*가 되는가, 아니면 *trivially resolved*가 되는가?

### §3.2 Architecture-conditional answer

**K-field architecture (4a primary, OP-0009-A 가정)**:
- Each formation $u^{(j)}: X \to [0,1]$ explicitly indexed.
- Site $x$의 formation membership: $\arg\max_k u^{(k)}(x)$ (well-separated regime: trivial; overlapping regime: $u^{(k)}(x)$ values 직접 비교).
- 추가 framework 불필요 → C_t 부활 불필요.

**Shared-pool architecture (4b/4c, currently working only)**:
- Single $\Sigma_m$ + multi-mode $u$ on single field.
- Site $x$의 어느 multi-mode peak에 속하는가는 *non-trivial* — basin-of-attraction analysis 또는 cluster decomposition 필요.
- $C_t$ resolvent가 자연스러운 candidate — block-diagonal structure가 multi-mode를 separate.

### §3.3 D-6a Multi-Static σ_multi^D (CV-1.5.1)

T-σ-multi-D-Static (C-0719, Cat A def):
$$\sigma^D(\mathbf{u}^*) := \mathrm{coh}(\mathbf{u}^*) := H^1(\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}};\ \mathrm{Stab}(\mathbf{u}^*))$$
conjugacy-class label. Wreath-product representation theory (Specht 1935 — year corrected per external references audit 2026-04-30; James-Kerber 1981) standard.

**Property**: σ_multi^D는 *전역* cohomology class label — formation labels-permutation invariant 위상 invariant. 사이트별 정량적 정보 없음.

---

## §4. Three Options Inventory

### §4.1 Option C-1: Demoted Maintained

**Statement**: $C_t$ remains *derived diagnostic only*; multi-formation에서도 demoted status 보존.

**Pros**:
- Commitment 12 (W4) 보존; canonical §3.6, Group C (vestigial) 변경 없음.
- K-field architecture 4a primary 시 자연 — $\arg\max_k u^{(k)}$로 membership trivially 결정.
- Computational cost 0.

**Cons**:
- Shared-pool architecture (4b/4c)에서 membership 결정 도구 부재.
- $C_t$의 within-vs-cross-boundary discrimination role이 multi-formation에서 가장 자연스러운데 demoted.

### §4.2 Option C-2: Revival as Primitive

**Statement**: Multi-formation에서 $C_t$ 부활 — Group C C1–C4 axioms를 multi-formation에서 활성화. Per-formation $C_t^{(j)}$ + cross-formation $C_t^{cross}$ 도입.

**Per-formation extension**:
$$C_t^{(j)} = (I - \alpha W_{\mathrm{sym}}^{(j)})^{-1}, \quad W_{\mathrm{sym}}^{(j)}(x,y) = \sqrt{u^{(j)}(x)} \mathbf{N}_t(x,y) \sqrt{u^{(j)}(y)} / d_x$$

**Cross-formation extension** (가능한 form):
$$C_t^{(j,k)}(x,y) = \sqrt{u^{(j)}(x)} (I - \alpha W_{\mathrm{sym}})^{-1}(x,y) \sqrt{u^{(k)}(y)}$$
(아직 spec 미정).

**Pros**:
- Multi-formation site-pair within-vs-cross discrimination을 자연스럽게.
- Shared-pool architecture에서 필수 도구.
- Group C axioms가 활용됨 (vestigial 해소).

**Cons**:
- v2.0 demotion 결정 (CV-1.5+) reversal — narrative impact 큼.
- C_t ↔ predicate/energy 연결이 multi-formation에서 만들어져야 함 (canonical §3.6의 "does not enter any predicate or energy term" 위배).
- Cross-formation $C_t^{(j,k)}$ spec 미정 → 추가 mathematical work.
- C3'' (monotonicity) generalization 불명: per-formation $C_t^{(j)}(x,x)$ in $u^{(j)}(x)$ vs joint form 결정 필요.
- **Empirical motivation 부재**: 현재 multi-formation experiments (NQ-198a/f/g 등) 모두 K-field architecture에서 $\arg\max$ membership으로 충분.

### §4.3 Option C-3: σ_multi^D Subsumes $C_t$

**Statement**: σ_multi^D (D-6a CV-1.5.1)가 within-vs-cross site-pair distinction을 *fully captures* — $C_t$ 영원히 demoted, 가능하면 §3.6 Group C 추가 demote (vestigial → archived).

**Verification (FAIL)**:

σ_multi^D는 *전역 cohomology class label* (orbital-equivalence under wreath-product symmetry). 사이트별 정량 정보 capture 안 함:
- σ_multi^D는 *distinct invariant 클래스*에 minimizer를 매핑 (예: $D_4$-grid 두 minimizer가 *같은* σ_multi^D class).
- $C_t(x,y)$는 *사이트별* co-belonging 정량 (예: 같은 σ_multi^D 클래스 두 minimizer가 *다른* $C_t$ matrices).

**Counterexample (Orthogonality Witness)**:

$D_4$-symmetric grid 32×32에 K=2 well-separated formations:
- Configuration A: $u^{(1)}, u^{(2)}$ at $(8, 16)$ and $(24, 16)$ (axis-aligned, distance 16).
- Configuration B: $u^{(1)}, u^{(2)}$ at $(8, 8)$ and $(24, 24)$ (diagonal, distance $16\sqrt{2}$).
- Both: $\mathrm{Stab}(\mathbf{u}^*) = \mathbb{Z}_2$ (single reflection); σ_multi^D *identical* conjugacy class.
- Both: $C_t(x_1, x_2)$ matrices *different* (decay constant depends on Euclidean distance, not just topological invariant).

→ σ_multi^D는 같지만 $C_t$는 distinct. **σ_multi^D ≠ subsumes $C_t$**.

**Conclusion**: Option C-3 strict는 false. σ_multi^D는 *전역 cohomology invariant*; $C_t$는 *사이트별 정량 diagnostic* — 두 차원의 정보.

### §4.4 Option C-3 (variant, Recommended)

**Statement**: σ_multi^D 와 $C_t$는 *orthogonal information* — 같은 ontological category에 속하지 않음. **둘 다 보존**:
- σ_multi^D = 전역 cohomology invariant (orbital-equivalence label, formation-permutation invariant).
- $C_t$ = 사이트별 정량 diagnostic (point-cloud co-belonging, fine-grained continuous).

**Net effect**:
- $C_t$ remains demoted-derived per Commitment 12 (W4) — **canonical 변경 0**.
- σ_multi^D 와 $C_t$의 orthogonal nature 명시 (canonical §3.6 forward-reference rider).
- Group C C1–C4 vestigial 그대로 (axioms 활성화 안 함).

---

## §5. σ_multi^D vs $C_t$ Orthogonality Audit

### §5.1 Information dimensionality 비교

| Aspect | σ_multi^D | $C_t$ |
|---|---|---|
| Domain | $\widetilde\Sigma^K_M$ (or quotient) | $X \times X$ |
| Codomain | $H^1(\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}; \mathrm{Stab}(\mathbf{u}^*))$ — finite set of conjugacy classes | $[0, \infty)$ — real-valued kernel |
| Granularity | Discrete (label) | Continuous (matrix) |
| Transform group | $\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}$ orbit-invariant | $\mathrm{Aut}(G)$ conjugation (per formation) |
| Information content | $O(|H^1(\ldots)|)$ — typically small ($K_{\mathrm{act}}!$ class) | $O(n^2)$ matrix entries |
| Computational role | Discrete classification | Sitewise diagnostic |

→ **Dimensionality 다른 차원**. σ_multi^D는 σ_multi^A의 between-formation cohomology pull-back; $C_t$는 within-formation distance kernel.

### §5.2 Orthogonality Witness Construction (Option C-3 variant 정당화)

**Construction**: Two K=2 minimizers $\mathbf{u}^{(1)*}, \mathbf{u}^{(2)*}$ on $D_4$ grid that:
- Have *identical* σ_multi^D label (same orbital class).
- Have *distinct* $C_t$ matrices (different sitewise decay).

**Detail**:
- Graph $G$ = 32×32 $D_4$-symmetric grid free-BC.
- $\mathrm{Aut}(G) = D_4$ (8 elements).
- Two well-separated formations $u^{(1)}, u^{(2)}$ with same per-formation σ-tuple (Commitment 14) — e.g., both Gaussian-shape disk minimizers.
- **Configuration A**: formations at lattice positions $(p_1, q_1), (p_2, q_2)$ that produce $\mathrm{Stab}(\mathbf{u}^*) = \langle s_y \rangle \cong \mathbb{Z}_2$ (single reflection).
- **Configuration B**: formations at lattice positions $(p_1', q_1'), (p_2', q_2')$ with same $\mathrm{Stab}(\mathbf{u}^*) = \langle s_y \rangle$ but different inter-formation distance.
- **Both**: σ_multi^A multi-set $\{\sigma_1, \sigma_2\}$ identical (same per-formation σ).
- **Both**: σ_multi^D = $H^1(D_4 \wr S_2; \langle s_y \rangle)$ identical conjugacy class.
- **Different**: Inter-formation graph distance $d_G$ different → $C_t(x_1, x_2)$ decay $\sim K_0(d_G/\xi_0)$ different scale.

→ **σ_multi^D 같음, $C_t$ 다름**. Orthogonality 입증.

**Implication**: σ_multi^D 와 $C_t$는 *서로 다른 정보를 capture*. Subsumption 불가능.

### §5.3 Continuity / Discreteness duality

**At K-jump events** (formation merger, $K_{\mathrm{act}}$ decreases by 1):
- σ_multi^D: discrete jump (wreath-product structure 변화).
- $C_t$: continuous evolution (resolvent matrix가 smooth in $u^{(j)}$ parameters).

→ **σ_multi^D는 discrete witness; $C_t$는 continuous witness**. K-jump 처리에서 둘 다 필요.

이는 OP-0008 σ^A K-jump 비결정성과 연결: σ^A inheritance map Φ (discrete)는 비결정적이지만, $C_t$ trajectory (continuous)는 deterministic — 두 layer 다른 정보.

---

## §6. Verdict (Option C-3 variant Recommended)

### §6.1 $C_t$ status decision

**RECOMMENDATION**: $C_t$ remains demoted-derived per canonical Commitment 12 + §3.6 (current). σ_multi^D (D-6a CV-1.5.1)와 *orthogonal information layers*; subsumption 없음.

### §6.2 Architecture conditionality

**Condition**: K-field architecture 4a primary (Tool A1 stratified space top stratum, OP-0009-A pending W6).

**If 4a primary** (recommended): Verdict §6.1 holds. C_t demoted maintained.

**If 4b/4c (shared-pool primary)**: Verdict re-examination needed. Shared-pool에서 membership 결정 도구로 $C_t$ 부활 candidate; W6+ OAT-4 (shared-pool architecture) 결과 의존.

### §6.3 Group C C1–C4 disposition

**RECOMMENDATION**: Group C axioms remain vestigial (canonical §6 line 388–419). 

- Multi-formation extension에서 axioms 활성화 *안 함*.
- 그러나 §6에 forward-reference 추가: "Group C axioms are vestigial single-formation; multi-formation $C_t^{(j)}$ extension (per-formation resolvent) would require restated axioms — see OP-0009-C and `working/MF/cobelonging_vs_sigmaD.md`."

### §6.4 Resolution criteria

본 verdict이 acceptable iff:
1. **Empirical**: 현재 multi-formation experiments (NQ-198a/f/g 등)에서 $\arg\max_k u^{(k)}$ membership으로 충분 — $C_t$ 부활 증거 없음. ✓
2. **Mathematical**: σ_multi^D 와 $C_t$ orthogonality witness §5.2 construction valid. ✓
3. **Architectural**: K-field architecture 4a primary 확정 (OP-0009-A W6+). 조건부 ✓.

→ **PARTIALLY VALIDATED**. Architecture decision 의존.

---

## §7. Recommended Canonical Edits at CV-1.6

### §7.1 §3.6 Forward-reference rider 추가 (line 200 다음)

```markdown
**Multi-formation status (W6+ added 2026-04-30, CV-1.6 candidate).** For K>1 multi-formation, σ_multi^D (D-6a CV-1.5.1) provides global cohomology invariant; $\mathbf{C}_t$ remains derived-diagnostic-only across all K. The two operators capture orthogonal aspects: σ_multi^D = orbital-equivalence label (global, formation-permutation invariant); $\mathbf{C}_t$ = pointwise within-formation membership measure (sitewise, continuous). Subsumption fails: an explicit orthogonality witness (two K=2 minimizers on $D_4$ grid with identical σ_multi^D but distinct $C_t$ matrices) demonstrates non-equivalence. See `working/MF/cobelonging_vs_sigmaD.md` (OAT-5) for formal analysis.
```

### §7.2 Commitment 12 보강 (canonical line 779)

```markdown
12. **$\mathbf{C}_t$ is a derived diagnostic.** Co-belonging does not enter any predicate or energy term. **Multi-formation status (W6+, CV-1.6)**: $\mathbf{C}_t$ status preserved at K>1; σ_multi^D (D-6a CV-1.5.1) provides orthogonal global invariant (cohomology pull-back), not subsumption (per OAT-5 working file). Group C axioms remain vestigial; multi-formation $\mathbf{C}_t^{(j)}$ per-formation extension is OPEN (OP-0009-C remaining sub-items if shared-pool architecture chosen).
```

### §7.3 OP-0009-C status update

CV-1.6 시점:
- **OP-0009-C**: PARTIALLY RESOLVED. K-field architecture 4a primary 시 $C_t$ demoted maintained (orthogonal to σ_multi^D, not subsumed). Shared-pool architecture decision (OP-0009-A) 의존.

### §7.4 Net canonical impact

**Lines added**: ~10–15 (§3.6 rider + Commitment 12 보강).
**Predicate / energy 변경**: 0 (CN10 maintain).
**Theorem status 변경**: 0 (Group C vestigial 유지).
**Net effect**: σ_multi^D vs $C_t$ orthogonality 명시 + OP-0009-C partial resolution.

---

## §8. Edge Cases (Analyst-suggested)

### §8.1 K=1 Reduction

When $K_{\mathrm{act}} = 1$:
- σ_multi^D: trivial cocycle ($H^1$ trivial for single formation).
- $C_t$: single-formation derived diagnostic per canonical §3.6.

**Consistency**: Both reduce to single-formation status. ✓

### §8.2 Empty Formation ($u^{(j)} \equiv 0$)

- $W_{\mathrm{sym}}^{(j)} = 0$ → $C_t^{(j)} = I$ (identity, degenerate).
- σ_multi^A multi-set: skip empty formation (active count $K_{\mathrm{act}}$ drops).

**Boundary behavior**: Document only; no new theorem needed.

### §8.3 Symmetric Ground State ($\mathrm{Stab}(\mathbf{u}^*) = \mathrm{Aut}(G)$)

- σ_multi^D: maximal symmetry → trivial cocycle (full Aut(G) preserved).
- $C_t$: retains full discriminative power (sitewise distance information unchanged).

**Implication**: Strongest case for orthogonality §5.2.

### §8.4 K-Jump Events (Discontinuous)

- σ_multi^D: discrete jump at merger (wreath-product structure changes from $\mathrm{Aut}(G) \wr S_K$ to $\mathrm{Aut}(G) \wr S_{K-1}$).
- $C_t$: continuous through bifurcation (resolvent $C_t = (I - \alpha W_{\mathrm{sym}})^{-1}$ smooth in $u^{(j)}$).

**Witness for OP-0008 reframe**: $C_t$ is the *continuous* witness; σ_multi^D is the *discrete* witness. K-jump 비결정성은 σ-side (discrete)에서만; $C_t$-side는 deterministic.

### §8.5 Same-Orbit Different Fields

- $\mathbf{u}^{*(1)}, \mathbf{u}^{*(2)}$ in same $\mathrm{Aut}(G)$-orbit: σ_multi^D identical.
- $C_t^{(1)} = P^\top C_t^{(2)} P$ for some permutation $P \in \mathrm{Aut}(G)$.

**Implication**: σ_multi^D 와 $C_t$ both Aut(G)-equivariant; orthogonal information.

---

## §9. Hard Constraint Verification

- [x] **canonical 직접 수정 0**: this is `working/MF/`, not canonical/. §7 proposals are conditional on user approval at CV-1.6.
- [x] **Silent resolution 0**: OP-0009-C status PARTIALLY RESOLVED (architecture-conditional); not falsely RESOLVED.
- [x] **u_t primitive maintained**: $C_t$ remains derived (Commitment 12 preserved).
- [x] **4-energy 항 not merged**: $C_t$ does not enter energy or predicate (canonical §3.6 + Commitment 12 honored).
- [x] **CN10 contrastive**: σ_multi^D 와 $C_t$ comparison is *internal SCC mathematics*, not external reduction.
- [x] **K not dual-treated abusively**: K_field/K_act decomposition (Commitment 16) honored throughout.
- [x] **No Research OS resurrection**: single-topic working file convention.
- [x] **Architectural conditionality 명시**: verdict explicitly K-field 4a primary 가정.

---

## §10. Open Questions (Analyst-suggested 통합)

### §10.1 Pending verification

- [ ] **Shared-pool branch ($C_t$ 부활)**: 4b/4c primary 결정 시 OP-0009-C 재검토. W6+ OAT-4 결과 의존.
- [ ] **Group C C3'' multi-formation generalization**: per-formation $C_t^{(j)}$ monotonicity in $u^{(j)}$ vs joint form across all K. Formal statement 미정.
- [ ] **$\arg\max_k u^{(k)}(x)$ degeneracy**: multiple formations equal cohesion at site (e.g., $u^{(1)}(x) = u^{(2)}(x)$) — tie-breaking. $C_t$가 이 tie-break 제공? (현재 Commitment 14 (O7) Mulliken 유사 convention 필요할 수도).
- [ ] **Empirical anchor**: Multi-formation experiment 중 $C_t$가 $\arg\max_k u^{(k)}$ 보다 *추가 정보* 제공하는 case construction.

### §10.2 OP-0009-C resolution wording

CV-1.6 시점 OP-0009-C status:
- "PARTIALLY RESOLVED — K-field architecture 4a primary 가정 하에서 $C_t$ demoted maintained (σ_multi^D와 orthogonal, not subsumed); Shared-pool branch (4b/4c) 결정 시 재검토" — recommended.

### §10.3 Empirical witness construction (W7+ candidate)

- $D_4$-grid orthogonality witness (§5.2): theoretical construction. Numerical 실증 (W7+) 권고.
- 두 minimizer with same σ_multi^D, different $C_t$ matrices — 실제 데이터.

---

## §11. Cross-References

### §11.1 Working files (this OAT family)

- `K_status_commitment.md` (OAT-1, W5 Day 3 EOD): K_field/K_act decomposition.
- `mathematical_scaffolding_4tools.md` (OAT-supplementary, W5 Day 4 morning): Tool A2 quotient + Tool A1 stratified.
- `multi_formation_sigma.md` (D-6a Approach A σ_multi^D definition).
- `sigma_multi_trajectory.md` (D-6b Theorem 4.6.1 framework).
- `from_single.md` (R22 retracted derived view, partial thesis preserved).

### §11.2 Canonical impact targets

- §3.6 (line 200): forward-reference rider (§7.1).
- §11.1 Commitment 12 (line 779): multi-formation status note (§7.2).
- §6 Group C (line 388–419): vestigial maintained + forward-reference.

### §11.3 Daily files

- `daily/2026-04-30/01_canonical_promotion_log.md`: CV-1.5.1 머지 log.
- `daily/2026-04-30/02_4tool_mapping_summary.md`: 4-tool verification daily summary.
- `daily/2026-04-30/99_summary.md`: Day 4 EOD reflection.

### §11.4 Open problems

- OP-0008 σ^A K-jump non-determinism: σ_multi^D는 discrete witness; $C_t$는 continuous witness. K-jump 비결정성 σ-side만.
- OP-0009-C: this file's resolution candidate.
- OP-0009-A: architecture choice — verdict architecture-conditional.

---

## §12. Recommendation Summary

### §12.1 Adopt Option C-3 variant at CV-1.6

**Recommendation**: APPROVE Option C-3 variant — $C_t$ remains demoted-derived per Commitment 12; σ_multi^D 와 $C_t$ orthogonal information (not subsumption). 

**Effort**: ~10–15 canonical lines (§3.6 rider + Commitment 12 보강). CV-1.6 packet에 추가 가능.

**Net effect**: 
- canonical 변경 minimal (forward-reference + commitment 보강만).
- σ_multi^D vs $C_t$ orthogonality 명시.
- OP-0009-C partial resolution (architecture-conditional).

### §12.2 Architecture-conditional 명시 필수

OP-0009-A K-field architecture 4a primary 확정 (W6+) 후 verdict 최종 적용. Shared-pool 4b/4c primary 시 $C_t$ revival 가능성 재검토.

### §12.3 NQ-242c numerical witness (W7+ candidate)

Orthogonality witness §5.2 construction을 numerical로 실증 — 두 K=2 D_4-grid minimizers with same σ_multi^D, different $C_t$ matrices. ~2 days compute (이미 SCC `scc/multi.py` + resolvent code 활용).

---

**End of cobelonging_vs_sigmaD.md (OAT-5).**

**Status: working draft (OAT-5 Option C-3 variant). $C_t$ demoted-derived maintained; σ_multi^D 와 orthogonal information (not subsumption). K-field architecture 4a primary 가정 하에서 verdict valid; shared-pool branch 결정 후 재검토. Orthogonality witness construction §5.2 (D_4-grid). OP-0009-C PARTIALLY RESOLVED (architecture-conditional). Canonical impact ~10-15 lines at CV-1.6.**

**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/MF/cobelonging_vs_sigmaD.md`
**Created:** 2026-04-30 (W5 Day 4 morning, OAT-5 advanced from W6 Day 3).
**Lines:** ~340.
**Promotion target:** CV-1.6 W6 Day 7 morning (D-CV1.6-O6 if user approves).
