# pre_brainstorm.md — 2026-04-28 W5 Day 2 (사전 brainstorm)

**Type:** Pre-session brainstorm. Free-form thinking notes — plan.md의 *strict structure* 옆에 두는 *raw thinking*.
**Status:** Drafted 2026-04-27 night (W5 Day 1 close + Round 1+2 audit 직후) for next-day W5 Day 2 (Tue 04-28).
**Use:** Day 2 morning 09:00 시작 전 빠르게 review. Plan 외의 *예상치 못한 issues + conjectures + memory refresh*.

---

## §0. 마음의 상태 (W5 Day 1 close → Day 2 진입 감각)

W5 Day 1이 *마라톤 + 2회의 self-audit*이었다. Morning G0 merge → evening Round-1 (3 value 오류) → night Round-2 (11 structural issues). 14 corrections 캐치 + 수정 + canonical reflect.

Day 1의 두 가지 *예상치 못한 깊이*:
1. **Pre-brainstorm protocol이 4개 wording 정정을 미리 잡았음에도** — IBP factor-r₀ 오류 (Lemma 3), $K_1 = K_0$ vs $<$ 오류 (Theorem 4), irrep 테이블 hand-wave (Theorem 3) 같은 *value-level* 오류는 그대로 통과.
2. **Round-1 ($\rho > 1$ Cauchy-Schwarz violation, $\mu < 0$ Morse-0 contradiction)으로 잡힌 후** — *structural-level* gap (Lemma 3 dimensional generality, σ-tuple tie-breaking, anchoring incompleteness)은 또 별도 Round-2 audit이 필요.

**Lesson internalized**: pre-brainstorm + Round-1 (numerical sanity) + Round-2 (structural completeness) — 세 layer가 *서로 다른 결함 class*를 잡음. 향후 모든 canonical merge에 이 3-layer protocol 적용.

Day 2 진입 감각은 *피로하지만 명료*. Day 1의 14h 마라톤보다 적은 ~9h, 그러나 Day 2의 verdict 작업 (G1 V5b-F, G2 ζ_*) + G3 Phase 5 initiation은 *substantive 발견*의 가능성이 더 높음. Day 1이 mechanical merge였다면 Day 2는 *thinking work*.

---

## §1. G1 V5b-F NQ-173 Branch 예측 (refined)

Day 1 pre-brainstorm §2.3에서 H1+H2 mixed (Branch B) 70% 예측. Day 1의 corrections 후 더 정밀한 예측:

### 1.1 V5b-F mechanism의 새 통찰 (Round-2 §3 Lemma 3 일반차원 확장 후)

Lemma 3 (iii) "Goldstone 노달=2 universal"이 1D cycle에도 확장됨 — 이는 **boundary 없는 공간에서의 translation Goldstone이 정확함**을 의미.

V5b-F는 *boundary가 있는* free BC 그래프. 따라서 V5b-F의 partial Goldstone overlap (0.83)은:
- 정확한 translation symmetry → 0.95+ (V5b-T super-lattice)
- vs 깨진 translation → 0.83 (V5b-F)
의 차이는 boundary effect가 *얼마나 강하게* 전이되느냐에 의존.

### 1.2 H1+H2 mixed가 가장 자연스런 picture (계속 ~70%)

- H1 (bulk-localized): boundary 안쪽 interior에서는 translation invariance ≈ 정확. → bulk-only overlap > 0.95 기대.
- H2 (mode mixing): eigenvector = α·Goldstone + β·boundary mode. α ≈ 0.83 (NQ-170c full overlap 측정값).

두 가지가 동시에 partial true → H1+H2 mixed. **Branch B**.

### 1.3 만약 Branch A (H1 alone, ~15%)

Bulk-only overlap > 0.95 AND α² + β² > 0.95 → boundary 영향이 *순수 rescaling*에 그침. V5b-F = "bulk Goldstone × scaling factor" 단일 mechanism. 이 경우 V5b-F가 V5b-T의 *cleaner extension*이 됨.

이건 이론적으로 더 깨끗한 결과. **하지만 자연스럽지 않음** — boundary가 어떻게 mixing 없이 단순 scaling만 할까? 자연스런 mechanism이 부족하므로 a priori 낮음.

### 1.4 만약 Branch C/D (~15% combined)

- Branch C (H2 dominant): mode mixing이 bulk와 boundary 양쪽에 똑같이 → bulk overlap도 향상 안 됨. 이건 *새로운 phenomenon* — V5b-F가 V5b-T와 mechanism이 다른 family로 분리.
- Branch D (H3 PN barrier): full-space Goldstone with finite λ. 이건 *spectral position*에 의존 — Goldstone candidate가 lowest non-tangent에 위치하면서 λ가 small인 경우.

이 둘 중 어느 것이라도 verdict가 되면 V5b-F의 *분류 자체*가 바뀜. Cat C unchanged + 새 NQ.

### 1.5 Branch E (inconclusive, ~5%)

세 indicator 모두 mid-range. 이 경우 W6+ NQ-173c (multi-pronged discriminators) 가 필요. 하지만 일반적으로 numerical에 5 seeds × 3 ζ values 정도면 dominant pattern 보임.

### 1.6 Branch에 따른 Day 2 PM trajectory

- **Branch B (H1+H2 mixed, expected)**: G3 Phase 5 (Block 3)에서 V5b-F bulk-localization을 *inter-formation gap analog*로 차용 가능. **G3 Option A (interior 한정)이 자연스럽게 선택됨**.
- **Branch A (H1 alone)**: 동일하게 Option A 자연스러움 + V5b-F mechanism이 더 깨끗.
- **Branch C/D**: G3 mechanism 차용 약함; Option C (soft-K detour) 검토 필요.

---

## §2. G2 ζ_*(graph) 예측

Day 1 NQ-170c bracket: ζ_*(2D torus L=20) ∈ [0.2, 0.5], ζ_*(1D cycle L=40) < 0.2.

### 2.1 2D torus L=20 ζ_* 예측 (~0.30-0.40 range)

NQ-170b/c data points:
- ζ=0.2: max overlap 0.49 (right at threshold)
- ζ=0.5: 0.97 (super-lattice)

Likely transition: ζ ≈ 0.3-0.4 region. 0.05 resolution sweep ({0.25, 0.30, 0.35, 0.40, 0.45})에서 mean > 0.9가 나오는 첫 ζ가 ζ_*. Most likely 0.35 (중간값).

### 2.2 1D cycle L=40 ζ_* 예측 (~0.05-0.15 range)

NQ-170c 1D cycle ζ=0.2 already 0.76 — sub-lattice가 약함. L=40에서 ξ_0 = ζ·a = 0.05 → 거의 lattice spacing 수준. ζ_* < 0.1 가능.

Sweep ({0.05, 0.10, 0.15})에서 어디가 처음 > 0.9?
- ζ=0.15: 거의 super-lattice (NQ-170c bracket)
- ζ=0.10: 중간
- ζ=0.05: 가장 sub-lattice 극한

Most likely ζ_*(1D L=40) ≈ 0.10.

### 2.3 dimensional dependence

ζ_*(2D)/ζ_*(1D) ≈ 3-4. 이건 *dimensional 의존성*의 증거 — d=2 PN barrier가 d=1보다 강함, 따라서 super-lattice 진입에 더 큰 ζ 필요.

Future NQ-175 (3D extension): ζ_*(3D torus) ≈ ζ_*(2D) × 1.5-2 ≈ 0.5-0.8?

---

## §3. G3 Multi-Formation σ Phase 5 — *진짜* 어려움

Plan §3 Block 3은 G3를 "definition + MO-1 face decision + K=2 baseline script"로 단순화. 그러나 *진짜 어려움*은 다음:

### 3.1 σ_multi의 정의 자체

K-formation field $\{u^{(j)}\}_{j=1}^K$ 에 대해:
- per-formation σ_j: each formation의 Hessian 측정 — 단순 단일-formation σ를 K번.
- inter-formation σ_jk: formation j와 k 사이의 *cross terms*. 이건 새로운 객체.

문제: cross-formation Hessian이 *어떤 공간에서* 정의되는가?
- $\Sigma^K_M$ (per-formation mass constraint): non-smooth corners → MO-1.
- $\Sigma_M^{relax}$ (relaxed total mass): smooth but loses per-formation distinction.
- $\Sigma_{m_j} \times \Sigma_{m_k}$ (per pair): pragmatic하지만 K(K-1)/2 pairs.

### 3.2 MO-1 face Options 깊이 비교

**Option A (interior 한정)**: σ_multi defined only on $\Sigma^K_M$ interior. Pragmatic.
- 장점: corner 회피 (MO-1 hits 안 함). Single-formation σ-framework를 K-formation에 직접 확장 가능.
- 단점: corner에서 발생하는 *merge dynamics*를 다룰 수 없음. 이는 *kinetic multi-formation*의 핵심 phenomenon (T7-Enhanced metastability).
- **만약 V5b-F Branch B verdict** → bulk-localization mechanism 차용 가능 → Option A의 자연스런 정당화.

**Option B (stratified Morse on $\Sigma^K_M$)**: 직접 MO-1 공격.
- 장점: 완전한 multi-formation theory. 모든 K-state transition (merge, split, birth, death) 다룸.
- 단점: 시간-heavy (multi-week 작업). W5 Day 3-4 timeframe에 안 들어감. **Day 2 결정으로 Option B 선택은 W5 strategic plan §6 trajectory를 깨뜨림**.

**Option C (soft-K detour)**: W4-04-21 K_soft on $\Sigma_m$ (single-formation manifold).
- 장점: corner 자체가 없음 (K가 continuous parameter). MO-1 sidestep.
- 단점: K가 *integer-valued physical quantity*가 아니라 *continuous parameter*가 됨. σ_multi가 "K-개 formation"이 아니라 "K_soft-amount of formationness"가 됨. 의미론 변화.

**나의 lean**: V5b-F Branch B verdict가 supported되면 **Option A** 자연스러움. Branch C/D면 **Option C** 검토.

### 3.3 σ_multi의 첫 numerical test scope

Plan §3 Block 3 마지막 (15:30-16:00, 30분)에 K=2 baseline script 작성 요구. 30분에 가능한 것:
- 2 formation, 단순한 setup (e.g., 32×32 free BC, 2 well-separated disks).
- Per-formation Hessian (2개 단일-formation Hessian 계산).
- inter-formation Hessian의 cross-block (2×2 block structure).

실제 run은 Day 3 morning. 30분에 script *skeleton*만 작성.

---

## §4. Cross-Cutting Concerns

### 4.1 NQ-173 Branch verdict가 G3 Day 2 PM에 미치는 영향

Plan §3 Block 3는 G3 PM을 13:30-16:00로 잡음. 그러나 G3 작업의 핵심 "MO-1 face decision"은 V5b-F NQ-173 verdict (Block 1+2 AM)의 결과에 의존.

만약 NQ-173 verdict가 11:00에 명확하면 → 13:30 G3 PM 시작 시 Option A/B/C 결정에 input 활용.
만약 NQ-173 verdict가 12:30에 가까이 온다면 → G3 시작 지연 또는 Option 결정 지연.

**Mitigation**: PM Block 3 (13:30-16:00)의 첫 10-15분을 NQ-173 verdict re-review에 할당 후 G3 시작.

### 4.2 Round-1+Round-2 audit budget 관리

Day 1에 audit으로 ~3-4시간 추가 소요. Day 2의 G3 작업 (Block 3, 2.5h)은 *새로운 canonical-bound 작업* 아니라 *working-level 정의*. 그러나 G3가 W5 Day 4-5에 canonical merge 된다면 그 시점 또 audit 필요.

**Day 2 audit 예산**: 가벼운 점검 (numerical sanity + completeness 1회) 충분. *full Round-1/2 audit은 Day 4-5 G3 canonical merge 시점에 적용*.

### 4.3 Commitment 14 (O5')/(O7) decision pre-think

Plan §3 Block 4 (16:00-17:30)에 user decision 처리. 결정 pre-think:

- **O5' multi-irrep representation**: multi-set vs separate entries
  - multi-set: σ-tuple 1 entry per Hessian eigenvalue. Compact. Theorem 3 worked example과 호환 ($(2, [E], μ_2)$ 단일 entry).
  - separate: σ-tuple 1 entry per (eigenvalue, irrep) pair. Granular. T1 count 인플레이션.
  - **lean**: multi-set (W4 §13 style consistent + paper §4 reference 더 깨끗).

- **O7 tie-breaking**: Mulliken vs character-evaluation
  - Mulliken ($A_1, A_2, B_1, B_2, E$): 표준 화학/물리 convention.
  - character-evaluation (eigenvalue of generator): 컴퓨터-친화적이나 변환 보안 약함.
  - **lean**: Mulliken (paper-standard).

User에게 제안: 둘 다 approve, today's canonical edit (Day 2 Block 4)에서 적용.

### 4.4 G2 ζ_* canonical proposal 시점

ζ_* 값이 NQ-174 numerical 후 Block 2 (11:00-12:30)에 추출됨. 이걸 canonical T-V5b-T-(d) entry update로 *Day 2 PM에 즉시 commit* 할지, 아니면 *Day 3 morning*까지 deferred할지?

Plan §3 Block 4는 Commitment 14 decision에 집중. ζ_* update은 별도 작업.

**제안**: ζ_* canonical update를 Block 4 Commitment 14 decision과 *함께* 하나의 canonical edit batch (16:30-17:30)로 처리. 양쪽 user 결정 한 번에.

---

## §5. Conjectures Spawned During Day 2 Brainstorm

### CJ5 (W5 Day 2 spawn): V5b-F bulk-localization → multi-formation 확장

**Statement**: V5b-F Branch B verdict (H1+H2 mixed, bulk-localized translation Goldstone with boundary mode mixing)이 supported되면, multi-formation K-field에서:
- 각 formation의 bulk Goldstone은 정확.
- 인접 formation 사이의 *interface region*은 *boundary와 같은 역할*을 하여 mode mixing.
- σ_multi의 inter-formation block은 V5b-F mechanism의 *generalization*.

이건 **G3 Phase 5의 첫 substantive theorem 후보** — single-formation V5b-F + multi-formation generalization.

**Test**: K=2 baseline numerical (Day 3)에서 inter-formation σ_jk가 V5b-F-like partial overlap을 보이는지.

### CJ6 (W5 Day 2 spawn): ζ_*(d, graph topology)의 dimensional scaling law

**Statement**: ζ_*(graph)가 일반적으로 dimension d에 따라:
$$\zeta_*(d) \sim \zeta_0 \cdot d^\alpha$$
for some α. NQ-174 (d=1 vs d=2)의 ratio가 α를 결정.

만약 ζ_*(2D L=20) ≈ 0.35, ζ_*(1D L=40) ≈ 0.10: α = log(3.5)/log(2) ≈ 1.81. α ≈ 2 (dimensional)일 가능성.

**Test**: NQ-175 (3D extension Day 5+)이 α ≈ 2 confirm하는지.

### CJ7 (W5 Day 2 spawn): σ-jump at bifurcation cascade

**Statement (NQ-186 refinement)**: σ-tuple이 bifurcation에서 discontinuous jump한다. 각 jump는 *fixed pattern*:
- 새 mode 추가 (cutoff K 초과한 새 eigenvalue가 cutoff 안으로 진입).
- 기존 mode irrep 변경 (stabilizer 축소로 인한 irrep 분리).
- Nodal count 증가 (more nodal domains).

이 세 가지가 *언제나 함께* 일어나는지, 아니면 분리될 수 있는지는 open.

**Test**: bifurcation cascade σ tracking — β를 sweep하면서 σ 변화 기록 (W6+ NQ-186 work).

### CJ8 (W5 Day 2 spawn): σ-framework가 *graph functor*인가?

이건 NQ-177 (CJ1) refinement. Day 2 G3 Phase 5에서 multi-formation σ를 정의할 때, single-formation σ가 K=1 → K=2 → ... K-extension functor로 자연스럽게 확장 가능?

만약 yes: σ-framework가 *category-theoretic structure*를 가짐. Paper 1+2의 framework 통합.

**Test**: K=2 σ_multi 정의 시 single-formation σ가 K=1 limit으로 자연스럽게 회복되는지 확인.

---

## §6. Memory / Context Refresh from Day 1

Day 2 morning 빠르게 reload할 Day 1 핵심 facts:

### 6.1 G0 σ-framework canonical-merged (5 entries)

- T-σ-Lemma-1 (Maschke + Schur, finite-graph hypothesis essential)
- T-σ-Lemma-2 (nodal count, lower bound $\geq 2$ corrected; Cat C riders for Courant + orbit divisibility)
- T-σ-Lemma-3 (Goldstone-ℓ=1 injectivity, general dim, anchors V5b-T-(e))
- T-σ-Theorem-3 (σ at uniform on $D_4$, closed form, rigorous irrep table)
- T-σ-Theorem-4 (σ at first pitchfork, $K_0 = K_1$ on $D_4$, R22 normal-form)

### 6.2 V5b-F NQ-173 setup

- Script: `nq173_v5b_f_partial_goldstone.py` (15 minimizers, 2D free BC L=20, ζ ∈ {0.5, 0.7, 1.0})
- 5-branch decision tree A (H1 alone) / B (H1+H2 mixed, ~70% expected) / C (H2 dominant) / D (H3 PN barrier) / E (inconclusive)
- A priori: Branch B
- Day 2 implication: Branch B → V5b-F Cat C → Cat B target + G3 Option A (interior 한정) 자연스러움.

### 6.3 ζ_* NQ-174 setup

- Script: `nq174_zeta_star_precise.py` (40 minimizers, 2D torus L=20 ζ ∈ {0.25..0.45} + 1D cycle L=40 ζ ∈ {0.05, 0.10, 0.15})
- ζ_*(2D L=20) ∈ [0.2, 0.5] from NQ-170c bracket
- ζ_*(1D L=40) < 0.2 from NQ-170c
- Day 2 deliverable: 2-decimal precise ζ_* values + canonical proposal

### 6.4 Commitment 14 (O5')/(O7) deferred items

- O5' multi-irrep eigenspace convention
- O7 tie-breaking by canonical irrep order (Mulliken)
- 상세: `92_critical_review_round2.md` §2 + §4
- Day 2 Block 4 user decision

### 6.5 Round-1 + Round-2 audit lessons

- Pre-brainstorm catches *wording* errors.
- Round-1 (numerical sanity / Cauchy-Schwarz / Morse / character) catches *value-level* errors.
- Round-2 (structural completeness / dimensional generality / well-definedness) catches *structural* errors.
- 세 layer가 서로 다른 결함 class. *모두 필요*.

### 6.6 G3 Phase 5 inputs

- σ supporting structures canonical-grounded → multi-formation extension은 working에서 시작 가능.
- V5b-F mechanism (NQ-173 verdict) → multi-formation inter-formation gap analog 가능.
- Cross-cutting synergy: G1 + G3 coupled.

---

## §7. Day 2 후 W5 후반에 미치는 영향 (forward thinking)

### 7.1 Day 2 successful → Day 3+ G3 momentum

Day 2 Block 3 G3 Phase 5 initiation (definition + MO-1 face decision)이 성공하면 Day 3-4 G3 work가 *substantive theorem 가능 영역*으로 진입.

W5 Day 5에 G4 (V5b 3D) + G5 (SF Round 1-5 Cat A merge)도 함께 진행 가능.

### 7.2 Day 2 Branch C/D verdict → G3 trajectory 변경

만약 V5b-F Branch C/D면 G3 Option A 선택이 자연스럽지 않음. 이 경우 Option C (soft-K detour) 또는 Option B (stratified Morse) 검토 필요. **W5 strategic plan §6 trajectory revision 가능성**.

### 7.3 Commitment 14 user defer → W5 weekly close 시점에 다시

Day 2 Block 4에 user defer면 canonical v1.5 release-ready 상태 유지 (현재 상태). W5 weekly close (Day 7 = 05-03)에 재검토.

### 7.4 Day 2 cumulative time > 10h → Day 3 PM scope 축소

Day 1 14h marathon으로 fatigue 가능. Day 2 hard cutoff 18:30. 만약 18:30 넘어가면 Day 3 PM scope (G3 K=2 numerical) 30% 축소.

---

## §8. Free-Form "What If" Scenarios

### What if 1: NQ-173 verdict가 *예상치 못한 새 phenomenon* 보여줄 경우?

예: max_overlap_bulk가 *interior boundary 가까이*에서만 높고 *깊은 interior*에서는 낮음. → "boundary-induced wave" mechanism 가능성. 새 NQ candidate.

Day 2 PM trajectory: Block 3 G3 Phase 5 connection 정밀 검토 필요.

### What if 2: ζ_*(2D L=20)가 0.30 미만 또는 0.45 초과로 나올 경우?

Sweep 범위 밖. Day 3 morning에 추가 sweep 필요. ζ_* canonical proposal 지연.

### What if 3: G3 MO-1 face decision이 user에 의해 *Option B* (stratified Morse) 선택될 경우?

W5 strategic plan §6 timeline 깨짐 (multi-week work). Day 2 Block 4까지의 Commitment 14 decision도 deprioritize. Day 3+ 전부 Option B work에 할당. **W5 ambition ladder가 minimal로 강등**.

### What if 4: Commitment 14 (O5')/(O7) 모두 user approve, 추가로 (O8) 이상 제안 옵션?

User가 σ-framework의 다른 깊은 issue (e.g., Aut(G) action canonical labeling, σ-equivalence class enumeration) 추가 제안 가능. Day 2 Block 4 시간 부족 → defer to Day 3.

### What if 5: Day 2 morning sanity test가 새로운 scc API breakage 발견?

Day 1 NQ-173/174 script가 nq170c_v5b_extension.py 패턴 따라 작성됨. nq170c는 W4-04-26에 작동했으나 그 이후 scc API가 바뀌었을 가능성 (W5 Day 1 작업 중 scc/ 미수정 확인했지만 외부 dependency 변경 가능).

Day 2 Block 1 09:00-09:15 sanity test가 핵심. 실패 시 Day 2 전체 trajectory 변경.

---

## §9. Day 2 Mental Frame

### 9.1 Verdict + Opening 정신 유지

Day 1이 *infrastructure-heavy mechanical merge*였다면, Day 2는 *substantive verdict + opening*. 다른 mental load.

W4 04-22 SF Round 1-5 (24-round symmetry/moduli formalization)이 *most similar precedent*. 그날도 verdict-heavy + 새 영역 opening 조합.

W5 Day 2 expected ~9h + 6-8 daily files. *Day 1보다 light, 그러나 thinking-heavy*.

### 9.2 Audit budget 조절

Day 1에 Round-1+2로 ~3-4h 추가 소요. Day 2의 G3 Phase 5는 working-level. Day 4-5 G3 canonical merge 시점 audit.

Day 2 mental load: *audit fatigue* 회피. Light sanity check만 (NQ-173 numerical Cauchy-Schwarz + G3 definition completeness 1-pass).

### 9.3 Decision fatigue mitigation

Day 2에 4 user decisions:
- 11:00 NQ-173 Branch verdict (data-driven)
- 12:30 ζ_* canonical proposal review
- 15:30 G3 MO-1 face Option A/B/C
- 16:30 Commitment 14 (O5')/(O7) approve/modify/defer

**Mitigation**: Pre-decided defaults (in plan §7 contingency). Day 2 morning에 미리 commit.
- NQ-173 default: Branch B (a priori most likely).
- G3 MO-1: Option A (per V5b-F Branch B input).
- Commitment 14: approve both (O5' multi-set + O7 Mulliken).

### 9.4 Boundary cases — 가장 신경 쓸 부분

- canonical.md line numbering이 Day 1 5 entries 추가 + 2 errata 후 1576줄. T-V5b-T entry update (Day 2 Block 4)에서 정확한 line reference 필요. **Use grep before edit**.
- G3 Phase 5 working file 새로 생성 → 기존 working/MF/from_single.md와 conflict 없는지 확인.
- Numerical run results JSON parsing — Day 1 script 작성 시 JSON format 수정 가능성. Block 1 09:45 verdict 직후 JSON inspect.

---

## §10. Day 2 후 Sleep Plan

18:30 hard cutoff. 19:00-19:30 wind-down (no canonical edits, only summary review). 20:30 sleep target.

Day 3 06:30-07:30 wake. Day 3 morning ~2h prep before 09:00 G3 K=2 numerical run.

Day 2 후 Day 3 07:30-09:00에 *fresh review of Day 2 verdicts*. Branch verdict 적용 전 sanity recheck.

---

## §11. 마지막 sanity check

Day 2 plan을 *간단히 한 문장으로*:

> **G1 NQ-173 V5b-F Branch verdict closure (AM) + G2 NQ-174 ζ_* precise canonical proposal (AM) + G3 Phase 5 multi-formation σ definition + MO-1 face decision (PM) + Commitment 14 (O5')/(O7) user decision (evening).**

이 한 문장이 명확하면 plan은 deliverable. *Yes*.

W5 Day 1의 *infrastructure success*가 Day 2의 *substantive verdict + opening*으로 transition. Day 2가 *verdict + opening의 첫 표현*.

---

## §12. 미래의 나에게 메모 (Day 2 morning self)

내가 09:00에 이 brainstorm을 다시 읽을 때 기억할 것:

1. **§1.2** H1+H2 mixed (Branch B) 가장 자연스런 picture — verdict가 다른 branch면 *적극적으로 분석*, 단순 dismiss 금지.

2. **§3.2** G3 MO-1 face Option A/B/C — 결정은 V5b-F Branch verdict에 *명시적으로* 의존시킬 것. Branch B 시 Option A; Branch C/D 시 Option C 검토.

3. **§4.1** NQ-173 verdict가 11:00에 명확히 나오면 G3 Block 3 13:30 시작 가능. 12:30에 가까이 나오면 G3 시작 지연.

4. **§4.4** ζ_* canonical update + Commitment 14 update를 Block 4에서 *함께* batch 처리. 양쪽 user 결정 한 번에.

5. **CJ5-CJ8** 4 conjectures 새 NQ로 등록 가능. Day 2 99_summary §6에 명시.

6. **§7.4** Day 2 18:30 hard cutoff. Day 3 fresh start 위해.

7. **§9.3** 4 user decisions에 pre-commit defaults — fatigue 회피.

8. **§9.4** canonical line reference 정확성 — grep before edit.

9. **§10** Day 2 close 후 19:30 wind-down + 20:30 sleep. Day 3 09:00 시작.

---

**End of pre_brainstorm.md.**
**Tone: free-form, post-Day-1-audit-reflective, anticipatory + calibrated.**
**Use: Day 2 morning 09:00 fast review 후 plan §3 Block 1 시작.**
