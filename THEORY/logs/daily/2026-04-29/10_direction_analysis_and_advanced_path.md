# 10_direction_analysis_and_advanced_path.md — Day 3 방향 분석 + 고도화 방향 제시

**Session:** 2026-04-29 (W5 Day 3 — comprehensive direction synthesis)
**Target:** 사용자 요청 "오늘 방향 분석후 고도화방향제시" — Day 3에 일관된 방향성을 추출하고, 그것을 바탕으로 short/medium/long-term 고도화 경로를 제시. 단순 Day 4 todo 나열이 아닌, **이론 발전의 메타-구조** 차원에서 방향 정의.
**This file covers:** §1 Day 3 방향 분석 (5 차원); §2 발견된 핵심 패턴; §3 고도화 방향 (5 layers: immediate / short / medium / long / structural); §4 Day 4 → W5 close → W6+ roadmap; §5 risk register; §6 priority decisions for user.
**Depends on reading:** 모든 Day 3 daily files (`00_*` ~ `09_*`), `99_*` summary.

---

## §1. Day 3 방향 분석 (5 차원)

### §1.1 Theoretical-empirical balance (이론↔실험 축)

**관찰**: Day 3는 이론(`04_*`, `05_*`)과 실험(`07_*`)을 **번갈아** 진행. 핵심은 NQ-198a 실험이 **이론을 refute** 한 것:

```
Phase 3 heuristic (이론) ──┐
                          ├──→ NQ-198a (실험) ──→ μ ∝ |∂S|/n (둘 다 reject)
Day 3 §4 derivation (이론) ┘
```

이는 **method "iterative dialogue between theory and experiment"** 의 명시적 발현. Phase 1-10 (Day 2)에서도 비슷한 패턴이 6 cycles에 걸쳐 나타났음 (Phase 6 refutation, Phase 7 recovery, Phase 9 revision).

**의미**: SCC 이론 발전 동력은 **단일 axiom system 의 deductive expansion** 이 아니라 **assumption-test-revision loop**. Numerical experiment가 axiom-level이 아니라 **empirical anchor** 역할로 격상됨.

### §1.2 Multi-formation σ-framework 의 maturation depth (성숙도 축)

| Layer | Day 2 EOD | Day 3 EOD |
|---|---|---|
| σ_multi^A 정의 (well-defined-ness) | Cat B target | Cat A under involution iso (D-6a 승인 대기) |
| σ_multi^D 정의 (orbit-type cohomology) | Cat A | Cat A (D-6a 승인 대기) |
| T-σ-Multi-1 Goldstone-pair instability | Cat A static | Cat A static (D-6a 승인 대기) |
| **σ_multi^A(t) trajectory dynamic** | **Cat B sketch** | **Cat B target with Theorem 4.6.1 framework + explicit failure modes** (`04_*`) |
| K-jump σ-inheritance | sketch | **Lemma 4.4.1**: left/right limits Cat A; **σ^A non-determinism** asserted (Cat C; not Cat B) |
| σ^D K-jump inheritance | not addressed | **Proposition 4.5.1**: cohomology pull-back (Cat B sketch) |

**의미**: D-6a static layer는 canonical-ready. D-6b dynamic layer는 Day 3에 substantive framework까지 발전했지만 아직 **canonical-ready 아님** (NQ-242 W6+ 필요). 단순히 "defer indefinitely"였던 Day 3 morning 상태에서 "structured Cat B target with Cat A path" 상태로 격상.

### §1.3 V5b family 의 분화 (regime taxonomy 축)

```
V5b family
├── V5b-T (super-lattice, ζ > ζ_*, c ∈ spinodal)
│     → exponentially-suppressed Goldstone, μ ~ β·exp(-c_d/ξ_0)
│     Cat A canonical (CV-1.4)
├── V5b-T-(c) interior sub-lattice commensurability splitting
│     Cat A canonical (CV-1.4)
├── V5b-T' (sub-lattice, c < c_s, translation-invariant)
│     → corner-saturated, μ ?? (Day 3 §4 predicts 2α; UNTESTED on torus)
│     Cat C → B target depending on NQ-198f
└── V5b-F (sub-lattice, c < c_s, translation-broken / free-BC)
      → corner-saturated, μ ≈ 13|∂S|/n (NQ-198a empirical)
      Cat B empirical
```

**관찰**: V5b family 가 Day 2에서는 3개 (T, T', F)였고 Day 3에 **regime/topology gradient** 가 더 명확화됨. 그러나 V5b-T'와 V5b-F의 **scaling difference** 가 처음 인식됨 (`07_*` §5):
- V5b-F: $\mu \propto |\partial S|/n$ (finite-size collective)
- V5b-T' (untested): possibly $\mu \approx $ const (continuum-Goldstone-like)

이 분화는 **단일 PN-barrier formula** 가설 (`2026-04-28/11_*` §4) 을 약화시킴. Cat A unified formula는 더 어려운 목표가 됨.

### §1.4 Hard constraint compliance under pressure (구속력 축)

`plan.md` §6 hard constraints + meta-prompt §8 hard constraints — Day 3에 9개 daily files 생산하면서 모두 유지:

| Constraint | Day 3 status |
|---|---|
| canonical 직접 수정 0 | ✓ (모든 edit는 proposal/template level) |
| Silent resolution 0 | ✓ (D-6b non-determinism explicit; V5b regime conflation explicit) |
| u_t primitive | ✓ |
| 4 energy term not merged | ✓ |
| K not dual-treated | ✓ |
| P-F flag inline | △ (`05_*`, `07_*` 누락; `09_*` §6.4에서 self-flagged) |
| Reductive equation 0 | △ (Allen-Cahn / cohomology 인용은 correspondence; 경계선) |
| OMC pull orchestration 0 | ✓ |
| Phase 11 numerical < 30min | △ (NQ-198a 3.7min; OK. 그러나 Phase 11 자체는 plan에서 deprioritize했었음) |
| No git commits | ✓ |

**의미**: 9 deliverables 압축 진행에도 hard constraints 대체로 유지. 약 1-2 minor near-miss 만 발생; 모두 self-identified (`09_*`)되어 Day 4 morning correction queue에 들어감.

### §1.5 Methodology rigor 축

5개 approach 생성 → 1 primary 선택 → development 의 패턴이 두 번 적용됨 (`04_*`, `05_*`). 그러나:

- `04_*`: primary (Approach 1+2 hybrid) 발전 잘됨; alternatives (3, 4, 5)는 "preserved as fallback"으로 언급만.
- `05_*`: primary가 **잘못된 답** 도출 (μ ≈ const). Secondary verification 없이 발표; NQ-198a이 사실상의 self-critique 역할.

**의미**: meta-prompt §4 framework가 정상 작동하지만, **secondary approach validation 단계**가 누락. `09_*` §4.2에서 lesson으로 명시.

---

## §2. 발견된 핵심 패턴

### §2.1 Substantive negative results의 가치

Day 3의 가장 큰 contribution 두 개 모두 **negative result**:

1. **`04_*` Lemma 4.4.1(c)**: σ^A K-jump inheritance is non-deterministic in σ^A alone — *prior assumption (deterministic inheritance) refuted*.
2. **`07_*` §3.3-§4**: μ ∝ |∂S|/n empirical scaling — *both Phase 3 heuristic and Day 3 §4 derivation refuted*.

이들은 "Cat B target sketches"보다 더 informative. **Theory honesty**를 향상시키며, future work direction을 명확히 함 (rich σ-augmentation; 1/n derivation).

**Pattern**: positive result에 대한 회의보다 *negative result를 적극적으로 추구* 하는 것이 (a) theory 변형 가능성을 검증하고, (b) 예상치 못한 finite-size physics를 드러낼 수 있음.

### §2.2 Single-cycle deepening의 한계

Day 2 phase 1-10 expansion은 10 self-critique cycles로 발전. Day 3 deepening은 **single-pass** (`04_*` 발표, `05_*` 발표, `06_*` synthesis — iteration 없음). 결과: `05_*`의 V5b-T'/V5b-F regime conflation이 single-pass에서 잡히지 않고 NQ-198a 후 `09_*`에서야 발견됨.

**Pattern**: deepening은 적어도 **1-cycle self-critique**를 포함해야 robust. (2-3 cycles까지는 sweet spot; 그 이상은 diminishing.)

### §2.3 Numerical-experimental verification의 시간-비용 비대칭

NQ-198a: ~3.7 min compute, ~30 min script-write, ~1h analysis = ~1.5h 총. 그러나 결과의 정보량은 weeks의 이론 작업에 해당.

**Pattern**: SCC 이론에서 *low-cost numerical experiment* (n < 1000 single-formation Hessian) 는 **해석적 derivation 보다 더 즉시적**. 이는 Day 2 Phase 1-10에서도 입증됨 (246 numerical attempts → 5+ Cat A claims).

**고도화 함의**: 분석적 Cat A path (NQ-198b WKB, NQ-198c Allen-Cahn) 보다 **다양한 regime numerical scan** (NQ-198f/g/h)이 더 빨리 ROI 발생.

### §2.4 Plan-to-execution drift

`plan.md`: MODERATE-CONSOLIDATION, 7-8h, 3-5 files, 1300-2300 lines.
실제: **9 deliverables, ~12h, ~3700 lines** (3× plan budget).

User 추가 요청 ("내용 고도화 및 해결 안된 문제 계속 디벨롭" → "이거 진행하고 현재 오늘자 문제점을 다시 분석" → "오늘 방향 분석후 고도화방향제시") 이 매번 scope를 1.5-2× 확장.

**Pattern**: 사용자의 mid-session escalation 은 **rule, not exception**. 향후 plan은 "core target" + "expansion menu" 형태로 작성 권장.

### §2.5 Reconciliation의 brittleness

Block 0.5 reconciliation (`00_*`)은 D-1..D-6b 의 6개 proposal text를 "FINAL state" 로 declare 함. 그러나 그 directly 후의 deepening (`05_*`) 과 numerical (`07_*`) 이 D-5 text를 substantive하게 revision 시킴.

**Pattern**: theoretical reconciliation pass alone 은 충분하지 않음. **Numerical falsifiability check** 가 reconciliation 의 일부가 되어야 함.

`09_*` §4.4 에서 lesson 명시: "Future reconciliations should include 'is the proposal text falsifiable by a 30-min numerical?' check."

---

## §3. 고도화 방향 (5 Layers)

### §3.1 Layer A: Immediate (Day 4 morning, ~3-4h)

**목표**: Day 3 EOD 산출물을 정합성 있는 canonical merge 상태로 만들기.

| 순서 | 작업 | 시간 | 우선도 |
|---|---|---|---|
| 1 | `09_*` §7의 7개 priority correction 적용 (`00_*`/`02_*`/`05_*`/`04_*` 미세 수정) | ~30 min | HIGH |
| 2 | **NQ-198f 실행** (V5b-T' torus mass-dep test) — `05_*` §4 derivation의 마지막 변호 가능성 | ~30 min | **CRITICAL** |
| 3 | NQ-198f 결과로 D-5 V5b-T' canonical text 추가 refinement (V5b-T' torus regime 명시) | ~15 min | HIGH |
| 4 | Block 1 canonical merge (D-1..D-5 with finalized text + D-6a) — user authorize 필요 | ~75 min | depends on user |
| 5 | `04_*` Theorem 4.6.1 → `THEORY/working/MF/sigma_multi_trajectory.md` promote | ~30 min | MEDIUM |
| 6 | Day 4 99_summary | ~30 min | required |

**Layer A 산출물 (예상)**: `01a_canonical_promotion_log.md`, `02_NQ198f_torus_results.md` (NQ-198f), `03_Theorem_4_6_1_working_promotion.md`, `99_summary.md`. 4-5 files, ~1500 lines, ~3h Block 1 application + ~1h numerical + ~30min misc.

### §3.2 Layer B: Short-term (W5 Days 4-7, ~3-4 days remaining)

**목표**: W5 Stretch ladder 달성 — CV-1.5.1 release + Paper §4 LaTeX integration start.

**경로 1 (D-1..D-5 + D-6a 모두 승인 시)**:

| Day | 핵심 작업 |
|---|---|
| Day 4 (Wed) | Block 1 application + NQ-198f + V5b-T' text refinement + working promotion |
| Day 5 (Thu) | NQ-244 (3D LSW T³_15 K=10) ~1-2h compute + Paper §4.5.5 update; NQ-198g (β-dep of C) ~30min |
| Day 6 (Fri) | NQ-198h (ξ_0-dep of C) ~30min; combine NQ-198g/h → C(β, ξ_0) 함수형 결정; G5 SF Round 1-5 merge prep |
| Day 7 (Sat) | W5 weekly close, weekly_summary, Paper §4 LaTeX skeleton (W6+ extension) |

**경로 2 (Conservative D-1..D-4 만 승인 시)**:

| Day | 핵심 작업 |
|---|---|
| Day 4 | Block 1 small (D-1..D-4 only) + Phase 11 NQ-244 1-2h + NQ-198f |
| Day 5 | D-5/D-6a maturation (additional verifications) → 추가 Block 1.5 application |
| Day 6 | Phase 11 expansion (NQ-198g/h, NQ-242 prep) |
| Day 7 | W5 close |

### §3.3 Layer C: Medium-term (W6, ~1주)

**목표**: D-6b dynamic σ_multi^A(t) trajectory를 Cat B sketch → Cat A path 로 진전; V5b-T'/V5b-F unified scaling 결정.

| Priority | NQ | Effort | Cat target |
|---|---|---|---|
| 1 | **NQ-244** (3D LSW T³_15) | 1-2h compute + analysis | Paper §4.5.5 publishable |
| 2 | **NQ-198g/h/i** (β/ξ_0/small-cluster scans) | each ~30 min | Cat B refinement |
| 3 | **NQ-242 prep** (full Hessian σ-tuple time-series numerical infrastructure) | 1-2 days | Cat A path foundation |
| 4 | **NQ-198e** (rigorous 1/n derivation analytical) | 2-4 weeks | Cat A V5b-F |
| 5 | **NQ-198c** (discrete Allen-Cahn lattice correction) | 2-4 weeks | Cat A V5b-T' alternative |
| 6 | **CV-1.6 release prep** | end of W6 | merge D-6b + V5b-T'/F refinements |

W6 close target: **CV-1.6 release** with D-6b dynamic + V5b family unified scaling.

### §3.4 Layer D: Long-term (W7+, multi-week)

**목표**: Cat A path 들 완성; Paper 1 draft.

| NQ | Subject | Cat target | Effort |
|---|---|---|---|
| NQ-242 (full) | σ_multi^A(t) full Hessian + rigorous K-jump theory | Cat A | 4-6 weeks |
| NQ-242c | σ^A non-determinism explicit construction (Lemma 4.4.1c upgrade) | Cat A | 2-3 weeks |
| NQ-242d | σ^D symmetry-emergence characterization | Cat A | 2-3 weeks |
| NQ-198b | V5b-T' WKB + tight-binding | Cat A | 3-5 weeks |
| NQ-247 | V5b-T'/F cluster-hop dynamics | Cat B | 1-2 weeks |
| NQ-248 | Multi-formation Morse stratification | Cat A | 6-10 weeks |
| NQ-217 | Continuum limit Γ-convergence rigorous | Cat A | 4-6 weeks |
| NQ-200 | Non-involution canonical iso K ≥ 3 | Cat A extension | 3-5 weeks |
| **Paper 1** | SCC σ-framework Paper draft | publication | 8-12 weeks |

W10-W12 target: **Paper 1 submission**.

### §3.5 Layer E: Structural (long-term methodological)

**목표**: SCC research methodology 자체를 더 robust하게.

#### §3.5.1 Pre-registered numerical experiment 패턴

**Issue**: NQ-198a 결과는 prior derivation들을 refuted. 만약 NQ-198a를 사전에 *pre-register* (prediction을 명시 + 실험 setup 명시) 했다면, refutation을 더 정량적으로 quantify 할 수 있음.

**Pattern proposal**: 모든 future numerical experiment에 다음 형식의 pre-registration:
```
NQ-X pre-reg:
  Setup: [exact parameters]
  Prediction A (theory 1): μ ≈ ...
  Prediction B (theory 2): μ ≈ ...
  Falsifiability criterion: |observed - predicted| > X% → reject
  Resolution priority: [HIGH/MED/LOW]
```

#### §3.5.2 Multi-approach iteration as default

**Issue**: `05_*` primary approach가 잘못된 답 도출. Secondary verification 없이 발표.

**Pattern proposal**: Multi-approach framework의 strict version:
1. 5+ approaches 생성 (existing).
2. Primary approach development (existing).
3. **Secondary approach minimum-viable derivation** (NEW; 1h budget per secondary).
4. **Cross-check primary vs secondary** (NEW; if disagree → flag both as Cat C until reconciled).
5. Tertiary approaches as fallback (existing).

#### §3.5.3 Self-critique pass per file

**Issue**: Day 3 deepening files (`04_*`, `05_*`)가 single-pass.

**Pattern proposal**: 각 substantive file의 마지막 §X에 다음 구조:
```
§X. What could be wrong with this analysis?
  - Assumption A1 might fail when ...
  - Result R1 disagrees with intuition because ...
  - Numerical anchor N1 only covers regime R; untested in R'.
  - If empirical result refuted, fallback hypothesis: ...
```

This is 1-paragraph per file, ~5 min cost, but catches issues like the V5b-T'/V5b-F regime conflation.

#### §3.5.4 Plan-budget flex margin

**Issue**: plan §4 1300-2300 lines vs actual 3700 lines (2× over).

**Pattern proposal**: future `plan.md` should have:
- "Core target" budget (e.g., "1500 lines, 5 files, 7h").
- "Expansion menu" with explicit trigger conditions (e.g., "if user requests deepening, +1500 lines, +3 files, +3h").
- "Hard cap" (e.g., "10 files, 5000 lines max — beyond this, defer to next day").

#### §3.5.5 Reconciliation with falsifiability check

**Issue**: `00_*` reconciliation declared D-5 "FINAL" but `05_*` + `07_*` revised it.

**Pattern proposal**: reconciliation passes should include for each "FINAL" item:
- Theoretical Phase ≥ source orthogonality check (existing).
- **NEW**: 30-min numerical falsifiability test sketch — "if I ran a numerical varying [parameter], would it confirm the proposal text or could it refute?"
- If falsifiable in 30-min: schedule the test BEFORE declaring FINAL.

This would have caught D-5 text issue Day 3 morning.

#### §3.5.6 Promotion pipeline discipline

**Issue**: `04_*` substantive Theorem 4.6.1 framework is in raw daily-log; should be in `THEORY/working/MF/`.

**Pattern proposal**: any daily file with **Cat A or Cat B target theorem** triggers automatic promotion task (~30 min) at session close. Daily files with Cat C / sketches stay in daily/.

---

## §4. Day 4 → W5 Close → W6+ Roadmap

### §4.1 Day 4 (Wed, 2026-04-30) — Critical Path

**Morning (09:00-12:00, 3h)**:
1. (~10 min) Read `08_*` user-decision log + `09_*` self-critique.
2. (~30 min) Apply 7 priority corrections per `09_*` §7.
3. (~30 min) NQ-198f (V5b-T' torus mass-dep test) — **CRITICAL**.
4. (~15 min) NQ-198f result analysis; refine D-5 V5b-T'-(c) text accordingly.
5. (~75 min) Block 1 canonical apply (D-1..D-5 with finalized text + D-6a).
6. (~30 min) `04_*` Theorem 4.6.1 → `working/MF/sigma_multi_trajectory.md` promote.

**Afternoon (13:00-17:00, 4h)**:
1. (~1-2h) NQ-244 (3D LSW T³_15 K=10) — Paper §4.5.5 publishable α.
2. (~30 min) NQ-198g (β-dep of C) — combine with NQ-198a/f for C(β) functional form.
3. (~30 min) Day 4 99_summary + weekly_draft 04-30 entry.
4. (~1h flex / buffer for any overruns).

**Day 4 EOD outputs**: 5-7 daily files + canonical merge + 2 numerical results.

### §4.2 Day 5 (Thu, 2026-05-01)

**Focus**: NQ-198h + NQ-242 prep + Paper §4 LaTeX skeleton.

- (~30 min) NQ-198h (ξ_0-dep of C).
- (~1h) Combine NQ-198g/h → fit C(β, ξ_0) full form. Update D-5 canonical text again if needed.
- (~2h) NQ-242 numerical infrastructure: dense Hessian σ-tuple sampler; K-jump event detector.
- (~2h) Paper §4 LaTeX skeleton in `papers/` (extending existing structure with §4 σ-framework).
- (~30 min) Day 5 99_summary.

### §4.3 Day 6 (Fri, 2026-05-02)

**Focus**: G5 SF Round 1-5 Cat A merge prep + W5 weekly_summary draft start.

- (~3h) G5 SF Round 1-5 review and merge candidates.
- (~2h) W5 weekly_summary draft (incomplete; finalize Day 7).
- (~1h) NQ-242 development continuation.

### §4.4 Day 7 (Sat, 2026-05-03)

**Focus**: W5 close + Paper §4 first complete pass.

- (~2h) W5 weekly_summary finalize.
- (~3h) Paper §4 LaTeX first complete pass (to be reviewed W6).
- (~1h) W6 plan draft.
- (~1h) Day 7 99_summary + Day 7 close.

**W5 close target (Day 7 EOD)**:
- CV-1.5.1 released (Day 4 if approved).
- 3D LSW α published value (Day 4 NQ-244).
- C(β, ξ_0) characterized empirically (Day 4-5 NQ-198g/h).
- Paper §4 LaTeX-ready.
- W5 weekly_summary committed.

### §4.5 W6 (2026-05-04 ~ 05-10) — D-6b Cat A path advance

**W6 Day 1**: NQ-198f (if not done W5 Day 4) + NQ-242 numerical run start.
**W6 Day 2-3**: NQ-242 dense Hessian σ-tuple time-series; K-jump event analysis.
**W6 Day 4-5**: NQ-198e (1/n analytical derivation start) + NQ-242c (σ^A non-determinism construction).
**W6 Day 6**: CV-1.6 prep — D-6b Cat B target text drafting based on NQ-242 results.
**W6 Day 7**: W6 weekly close + CV-1.6 release if D-6b mature.

**W6 close target**:
- CV-1.6 released with D-6b dynamic σ_multi^A(t) Cat B target (or Cat A if NQ-242c succeeds).
- V5b family scaling unified (Cat B+).
- Paper 1 draft Section 4 mature.

### §4.6 W7+ — Paper 1 + Cat A paths

**W7-W8**: NQ-198b (V5b-T' WKB) + NQ-198e (1/n) parallel.
**W9-W10**: Paper 1 §1-§3 (introduction + framework + single-formation).
**W11**: Paper 1 §5-§6 (multi-formation + open problems + discussion).
**W12**: Paper 1 review + submission prep.

---

## §5. Risk Register

### §5.1 Risk-A: NQ-198f가 V5b-T' torus에서도 μ ∝ |∂S|/n 발견

**Likelihood**: 50% (could go either way).

**Impact (if 발생)**:
- `05_*` §4 derivation 완전히 폐기 (V5b-T'/V5b-F 둘 다 finite-size collective).
- D-5 V5b-T'-(c) text를 또 한 번 revision.
- `02_paper_section4_polished.md` §4.4.2 V5b-T' Theorem 4.4.2 의 "claim (c)" 도 영향.
- Cat status: V5b-T' Cat C → Cat B empirical (instead of Cat B target).

**Mitigation**: Day 4 morning에 NQ-198f를 Block 1 apply 보다 *먼저* 실행. 결과에 따라 D-5 text 미리 finalize.

### §5.2 Risk-B: User가 D-1..D-5+D-6a 거부 또는 partial 승인

**Likelihood**: 20%.

**Impact**:
- CV-1.5.1 release 지연 (W5 Stretch 달성 difficulty).
- Paper §4 polish는 영향 없음 (canonical-independent).
- W6 schedule 압박 증가.

**Mitigation**: `01_*` §3 option matrix에 conservative path 명시; Day 4 morning에 partial 승인 시 신속 적용.

### §5.3 Risk-C: NQ-244 3D simulation 실패 또는 너무 느림

**Likelihood**: 30% (T³_15 = 3375 sites; Hessian 계산은 ~10-15min/sample).

**Impact**: Paper §4.5.5 의 "publishable α value" 미달성. W5 Standard 달성은 가능하지만 Stretch는 불가.

**Mitigation**: Backup: T³_12 K=8 (smaller; ~30 min), gives partial result. Or: skip 3D dynamic LSW and instead numerical-anchor V5 structural finding.

### §5.4 Risk-D: Day 4 budget overrun (12h+ 필요)

**Likelihood**: 60% (Day 3에서 이미 50% overrun; pattern 계속).

**Impact**: W5 schedule 전반 지연.

**Mitigation**: §3.5.4 patten "core target + expansion menu" 도입; Day 4 핵심은 Block 1 + NQ-198f 만; 나머지는 flex.

### §5.5 Risk-E: NQ-242 (W6 main task) under-resourced

**Likelihood**: 40% (full Hessian σ-tuple time-series + rigorous K-jump theory는 4-6 weeks; 1 week W6에서 시작-진행 정도).

**Impact**: D-6b Cat A path 완성 지연; CV-1.6 W6 release 못 함.

**Mitigation**: W6 close target을 "NQ-242 *foundation* + Cat B target text" 로 setting; Cat A는 W7+로 둠.

---

## §6. Priority Decisions for User (Day 4 Morning Selectable)

User에게 다음 선택지를 명시:

### §6.1 Decision-α: NQ-198f priority

**α-1 (RECOMMENDED)**: Day 4 morning에 NQ-198f 먼저 실행 (~30 min) → D-5 text 추가 refinement → Block 1 apply.

**α-2**: Block 1 apply 먼저 (D-5 with current finalized text) → NQ-198f 결과 따라 CV-1.5.2 patch.

**α-3**: NQ-198f 미실행 → V5b-T' canonical에서 torus regime 명시적 caveat (`07_*` §6.1 현재 형태).

### §6.2 Decision-β: Block 1 application timing

**β-1 (RECOMMENDED)**: Day 4 morning per §4.1 schedule (after 7 corrections + NQ-198f).

**β-2**: Day 4 PM (after Day 4 morning self-review of corrections).

**β-3**: Defer to Day 5 (more verification cycles).

### §6.3 Decision-γ: W5 ladder target

**γ-1 (Stretch RECOMMENDED)**: CV-1.5.1 release Day 4 + 3D LSW Day 4 PM + Paper §4 LaTeX Day 7 → Paper 1 draft start W6.

**γ-2 (Standard)**: CV-1.5.1 release Day 4 + 3D LSW Day 5 → W5 close at Standard ladder; Paper 1 W7+.

**γ-3 (Conservative)**: D-5/D-6a defer; W5 close at Ambitious ladder; CV-1.5.1 W6 release.

### §6.4 Decision-δ: §3.5 structural improvements adoption

**δ-1**: 모두 채택 → next session plan에 explicit margin / pre-registration / self-critique-per-file.

**δ-2 (RECOMMENDED)**: §3.5.1 (pre-registration) + §3.5.3 (self-critique per file) only. 가장 cheap한 두 패턴.

**δ-3**: 변화 없음 (current methodology 유지).

---

## §7. Hard Constraint Verification

- [x] canonical 직접 수정 0.
- [x] Silent resolution 0 — Decision-α/β/γ/δ 모두 explicit user choice; no hidden default.
- [x] No primitive override.
- [x] No 4-term merging.
- [x] K not dual-treated.
- [x] No metastability without P-F flag (NQ-198f / NQ-244 setup에 포함될 P-F flag 명시).
- [x] No reductive equation.
- [x] All NQ priority labels (CRITICAL/HIGH/MED/LOW) attached with rationale.
- [x] Risk register explicit; mitigations stated.
- [x] Roadmap covers Day 4 → Day 7 → W6 → W7+ → Paper 1; each layer with concrete deliverables.

---

## §8. Summary

**Day 3 방향 5축 분석**:
1. Theory↔experiment dialogue가 핵심 동력 (NQ-198a refuted both prior derivations).
2. σ-framework multi-formation maturation: D-6a static Cat A ready; D-6b dynamic Cat B target.
3. V5b family regime 분화 (T / T' / F)가 더 명확화 + V5b-T'/V5b-F scaling 차이 발견.
4. Hard constraint 9/10 fully observed; minor near-misses self-flagged.
5. Methodology rigor: multi-approach framework 작동하지만 secondary verification 단계 추가 필요.

**핵심 패턴**:
- Substantive negative results > optimistic positive results.
- Single-cycle deepening은 robust하지 않음 (`05_*` regime conflation 사례).
- Low-cost numerical (NQ-198a 3.7min) > weeks of analytical work in ROI.
- Plan drift는 normal이라 가정 → "core + expansion menu" 패턴 필요.

**고도화 5 layers**:
- A: Day 4 morning ~3-4h (corrections + NQ-198f + Block 1 + working promotion).
- B: W5 Days 4-7 (CV-1.5.1 + 3D LSW + C(β,ξ_0) + Paper §4 LaTeX).
- C: W6 (NQ-244 + NQ-198g/h/i/e + NQ-242 prep + CV-1.6 prep).
- D: W7+ (NQ-198b + NQ-242 full + Paper 1).
- E: Structural (pre-registration; multi-approach iteration; self-critique per file; flex margin; falsifiability-aware reconciliation).

**Day 4 critical path**: NQ-198f → D-5 finalize → Block 1 apply → Theorem 4.6.1 promote.

**4 user decisions surfaced** (α NQ-198f priority / β Block 1 timing / γ W5 ladder target / δ structural improvements adoption).

---

**End of 10_direction_analysis_and_advanced_path.md.**
**Status: Day 3 방향 분석 완료; 5-layer 고도화 경로 (immediate / short / medium / long / structural) 제시; Day 4 → W5 → W6+ → Paper 1 roadmap 작성; risk register + 4 user decisions 정리.**
**Day 3 file count: 11 (`00`-`09`, `10`, `99`).**
**Day 3 line count: ~4500 (10층 ~600 lines 포함).**
