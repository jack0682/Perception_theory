> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# W8 Strategic Plan (2026-05-18 ~ 2026-05-22)

**Created:** 2026-05-16
**Entry state:** CV-1.17 SEALED (2026-05-15), **68A / 19B / 6C / 5R = 98 claims** (~70%)
**Predecessor:** `THEORY/logs/weekly/2026-05-W2/weekly_summary.md` (W7 close, CV-1.13 → CV-1.17, +15 claims, 결정 C)
**Source plan:** `/Users/ojaehong/.claude/plans/plan-scalable-plum.md` (approved 2026-05-16)

---

## 0. 주간 테마

**"Multi-Formation Atlas 작성 + Broad Exploration (국소최소 회피)"**

W7 은 세 갈래 dense track + 한 번의 결정의 호흡으로 +15 claims (CV-1.13→CV-1.17) 를 산출했고, 5/15 결정 C 가 V-AFD/R-2/z_t 회귀 패턴을 종결시켰다. W8 은 그 *결정 C framework 를 prophylactic 하게 매일 적용* 하면서, 사용자 요청 두 축을 동시 달성한다:

- **트랙 A — Multi-Formation Atlas**: 현재 canonical 의 ~40-50% 형식화 상태 (static/equilibrium 만; dynamics·MERGE-SPLIT·temporal composition 은 open) 를 *설명 가능한 형태로 정리* + *수학적 갭을 좁히는 새 정리 후보 생산*.
- **트랙 B — Broad Exploration**: 한 OP 에 깊이 파다가 국소최소에 빠지지 않도록 매일 *수학적으로 독립인* 3-5개 후보를 병렬 진행.
- **트랙 C — Numerical Probes**: sanity infra (canonical xref hash) + ≥4 새 실험으로 broad probe + V-AFD/R-2 같은 재포장 자동 차단.

세 track 은 매일 동시 진행되며, 한 track 에 60분 막히면 즉시 전환한다 — *국소최소 회피의 운영 원칙*.

**분량 목표**: 5 영업일에 ~1개월치 throughput (aggressive, non-conservative). 보수적으로 잡지 않는다.

---

## 1. 시작 상태

| 항목 | 값 |
|---|---|
| Canonical version | **CV-1.17** (sealed 2026-05-15 evening) |
| Hypothesis tree | **HT-3.8** |
| Claim count | **68A / 19B / 6C / 5R = 98 claims** (~70%) |
| H-MORSE row | **PARTIALLY CLOSED** (Local Cat B 달성; Global Cat A path = OP-HMORSE-LOCAL-A) |
| H-COMP row | **PARTIALLY CLOSED** (kernel-composed Cat B via T-CC-StableK-Kernel) |
| Package I | Cat A 완료 (AR/SDE/GI/PE) |
| T-Temporal-Identity | Cat A 완료 (all parts a,b,c,d) |
| T-σ-Inherit | parts (a,b,d-direction,e) Cat B / (c,d-σ_standard) Cat C |
| 주요 OPEN | OP-HMORSE-LOCAL-A, OP-0005-DYN, OP-0008-MERGE/SPLIT, OP-0012-SINK, OP-0021 (T_*) |
| pytest | 215 passed + 1 xfailed |

### W8 착수 시 입력 분석 (2026-05-16 작성)

| 분석 | 결과 요약 |
|---|---|
| Multi-formation canonical coverage 감사 (3-Explore parallel) | static layer ~95% / equilibrium K-selection ~80% / dynamics ~20% / σ-inheritance dynamics ~30% / temporal composition ~50% / OMS-2.0 ~100% (Appendix 자체). 형식화 가장 약한 곳 5개 식별 (OP-0021, OP-0008-MERGE/SPLIT, OP-0012-SINK, OP-0005-DYN, Commitment 16). |
| OP 의존성 그래프 + unlock chain 감사 | 3 unlock chains: (1) OP-HMORSE-LOCAL-A → Package II EK Cat B → Q3 closure (primary chain), (2) OP-0008-MERGE/SPLIT → T-σ-Inherit full → Q6 completion (W9+ chain), (3) OP-0021 → Package II + Q4-DYN unified rate (long chain). W7 archive pattern P1-P6 식별 — 같은 함정 회피 룰 정립. |
| 코드 측 multi-formation 감사 | scc/multi.py + transport.py + sigma_rich.py + k_soft.py + persistence.py 의 5개 test gap + 12개 실험 후보 + sanity test pattern 3개 식별. 새 scc/ 함수 추가 없이 experiments/ + tests/ 신규로 broad probe 가능. |

---

## 2. 목표

### G1 — Multi-Formation Atlas v1.0 (트랙 A, **Primary deliverable**)

**목표:** `THEORY/working/MF/MF_atlas.md` v1.0 작성 — multi-formation 의 canonical/working/open 전체 지도. 12개 section.

**구성 (12 sections):**
1. Multi-formation primitive (D-6a, K-field architecture, Commitment 16 status)
2. Static layer (T-L1-F/M Cat A, T-Persist-K-Sep/Weak/Unified)
3. Equilibrium K-selection (T-K-Select-PF Cat B — Day 2)
4. Observed K-selection (T-K-Select-OBS Cat B — Day 2)
5. σ-inheritance (T-σ-Inherit 6 parts — Day 3)
6. Temporal composition (T-Temporal-Identity Cat A + T-CC-StableK-Kernel Cat B — Day 4)
7. OMS-2.0 Appendix lift (canonical §A-§M — Day 4)
8. Coupling regimes + Λ_coupling 파라미터화 (Day 5)
9. Dynamics gap map (OP-0005-DYN/OP-0008/OP-0012-SINK/OP-0021 unlock chain — Day 5)
10. Open problems quick index (multi-formation 관련만 추출)
11. Code mapping (scc 함수별 정리/lemma 매핑)
12. W8 daily expansion log

**각 section 강제 룰**: 끝에 *gap 또는 새 후보 1개 이상* 명시 — Atlas 가 단순 재정리로 끝나지 않게.

**예상 effort:** 5 세션 (각 day Track A 1-2 시간 분배). Day 5 P5 promotion-ready status.

### G2 — CV-1.18 SEAL (트랙 B, **확정 SEAL target**)

**Primary target (사용자 확정 2026-05-16):** **OP-HMORSE-LOCAL-A** — L-HMORSE-LOCAL Cat B → Cat A 승급.

- **Sub-task A (analytic primary):** sharper residual bound via $|\sigma''(z(u^*))| \to 0$ at saturated nodes. 현재 worst-case $|\sigma''|_{\max}$ bound 가 numerical 대비 ~10⁴× 느슨 (`CV-1.16_SEAL.md §"Non-Overclaim"` 명시).
- **Sub-task B (numerical robustness):** OP-HMORSE-SBM extension — barbell / small-world 에서 L-HMORSE-LOCAL 의 robustness.

**근거:** 모든 SEAL 문서 (CV-1.15, CV-1.16, CV-1.17) + W7 weekly summary §6 이 일관되게 CV-1.18 target 으로 지목.

**Unlock effect:** Package II Eyring-Kramers Cat B 진입 prereq (W9-W10 main work 의 직접 unlock).

**+1A → 99 claims = 69A / 19B / 6C / 5R** (최소 보장 net 변화).

### G3 — Secondary SEAL 후보 (트랙 B, stretch)

CV-1.18 primary 가 일찍 완료되거나, Day 2-3 의 working 후보가 P5-P7 통과 시 추가 SEAL. Stretch target = **CV-1.19 SEALED** (W8 총 2 SEAL).

후보 (priority 순):
1. **P-K-Select-Unified Cat B** (Day 2 working `k_select_pf_obs_unified_view.md` 산출): equilibrium-observer 다리.
2. **L-Wigner-Projection-MERGE Cat B** (Day 3 working `op0008_merge_wigner_attack.md` 산출, 2-approach 수렴 시): T-σ-Inherit (d-σ_standard) Cat C → Cat B 승급.
3. **L-Sinkhorn-Plan-Composition-Bound Cat C** (Day 4 working `op0012_sink_scaling_attack.md` 산출): 새 Cat C 등록.

**+1-3 추가 → 100-101 claims 가능.**

### G4 — Numerical Probes (트랙 C, infra + 4 실험)

**Sanity infra (Day 1):**
- `CODE/tests/test_sanity_canonical_xref.py` — `canonical_k2_hash()` (permutation-invariant) + `subthreshold_demo_check()` (l_second/l_max, Λ_coupling 메트릭 강제 기록)
- `CODE/experiments/exp90_sanity_canonical_xref.py` — hash idempotence + duplicate detection

**4 broad probe 실험 (Day 2-5):**
- exp91 — K-soft hard-K recovery + Lipschitz (Day 2, gap §B-5 closure)
- exp92 — σ-inheritance Wigner projection robustness (Day 3, Cat B → Cat C bridge)
- exp93 — Multi-step temporal Persist chaining (Day 4, T-Temporal-Identity 다중 형성 확장)
- exp94 — Phase diagram 3-regime grid (Day 5, W8 visual deliverable PNG)

**테스트 보강 (Day 2-3):**
- `test_k_soft_recovery.py` (Day 2, 2 tests)
- `test_sigma_rich_formulas.py` (Day 3, Lemma B2/B3 직접 검증)

**예상 pytest 진화:** 215+1xf (entry) → 217+1xf (Day 2) → 219+1xf (Day 3) → 220+1xf (Day 4) → stretch 225+1xf (Day 5).

### G5 — Broad Survey (트랙 B, Day 1 3-parallel agents)

**Day 1 3-parallel Explore agents** — *수학적으로 독립* 인 OP 후보 동시 survey:

- **Agent B1**: OP-0021 Mori-Zwanzig Route A literature + canonical `MF/pf_tstar_langevin.md` gap 5개 정리 → `working/MF/broad_survey_B1.md`
- **Agent B2**: OP-0008-MERGE Wigner-projection perturbation theory 후보 (Reed-Simon IV §XIII.5 → SCC adaptation) → `working/MF/broad_survey_B2.md`
- **Agent B3**: OP-0005-DYN Kramers 3-pillar (nucleation/metastability/coarsening) multi-formation lift 후보 → `working/MF/broad_survey_B3.md`

이 survey 결과는 Day 2-4 의 Track B sketch (op0005_dyn / op0008_merge / op0012_sink) 직접 입력.

### G6 — Working 후보 P3+ 생산 (트랙 B, 누적)

W8 의 aggressive 분량 목표는 *새 working 후보를 P3 이상으로 끌어올리는 것* 으로 달성. 신규 working files ≥6:

- `MF_atlas.md` (Day 1-5, P5 target)
- `k_select_pf_obs_unified_view.md` (Day 2, P3 target)
- `op0005_dyn_kramers_sketch.md` (Day 2, Cat C SKETCH P3)
- `op0008_merge_wigner_attack.md` (Day 3, P3-P5 target depending on 2-approach convergence)
- `op0012_sink_scaling_attack.md` (Day 4, P3 target)
- `broad_survey_{B1,B2,B3}.md` (Day 1, P1 baseline survey)

총 working ≥9 신규.

---

## 3. 우선순위 및 순서 (Day-by-Day)

세 track 매일 병렬. 한 track 에 60분 막히면 다른 track 으로 전환.

```
Day 1 (Mon, 05-18) — Broad Survey + Atlas Skeleton + Sanity Infra
  Track A: MF_atlas.md skeleton (12 sections, 각 1 paragraph + xref) → v0.1
  Track B: 3 Explore agents 병렬 (B1: OP-0021, B2: OP-0008, B3: OP-0005-DYN) → 3 broad_survey 파일
  Track C: test_sanity_canonical_xref.py + exp90 (canonical_k2_hash, subthreshold_demo_check) → PASS
  Decision gate (EOD): 새 수학 0 — survey day 이므로 정상. canonical 0 edits.
  Deliverables: MF_atlas.md v0.1 + 3 broad survey + exp90 + daily logs

Day 2 (Tue, 05-19) — K-Selection Mechanism Deep Dive + OP-0005-DYN Sketch + K-soft Validation
  Track A: MF_atlas.md §3 (T-K-Select-PF) + §4 (T-K-Select-OBS) full (~80-120줄 each) + k_select_pf_obs_unified_view.md (P-K-Select-Unified Cat B SKETCH)
  Track B: op0005_dyn_kramers_sketch.md (3-pillar, Cat C target L-KRAMERS-MULTI-RATE)
  Track C: exp91 (K-soft hard-K recovery + Lipschitz, gap §B-5 closure) + test_k_soft_recovery.py (2 tests)
  Decision gate (EOD): 새 수학 = P-K-Select-Unified sketch + L-KRAMERS-MULTI-RATE sketch. K-soft Lipschitz numerical 지지.
  Deliverables: Atlas §3-§4 + 2 working files + exp91 + pytest 217+1xf

Day 3 (Wed, 05-20) — σ-Inheritance Deep Dive + OP-0008 MERGE Attack + Wigner Robustness
  Track A: MF_atlas.md §5 (σ-Inheritance 6 parts 정밀 표 ~200줄)
  Track B: op0008_merge_wigner_attack.md (2-approach: perturbation theory + RMT; 5×5 + 8×8 toy)
  Track C: exp92 (Wigner projection robustness, K=2 + ε-noise mixing 계수) + test_sigma_rich_formulas.py (Lemma B2/B3 직접 검증)
  Decision gate (EOD): 새 수학 = OP-0008-MERGE 2-approach 수렴 여부 판정. 수렴 시 → L-Wigner-Projection-MERGE Cat B 후보 P5 audit 트리거.
  Deliverables: Atlas §5 (가장 두꺼운 섹션) + op0008_merge_wigner_attack.md + exp92 + pytest 219+1xf

Day 4 (Thu, 05-21) — Temporal Composition + OP-0012-SINK Attack + **CV-1.18 SEAL**
  Track A: MF_atlas.md §6 (Temporal composition 통합 그림) + §7 (OMS-2.0 Appendix lift)
  Track B: op0012_sink_scaling_attack.md (cost-level vs plan-level scaling gap, L-Sinkhorn-Plan-Composition-Bound Cat C target)
  Track A&B 통합 — **CV-1.18 SEAL (primary OP-HMORSE-LOCAL-A)**:
    Step 1: Sub-task A analytic refinement (|σ''| saturation) audit
    Step 2: Sub-task B numerical (SBM/barbell/small-world) 검증 via exp_hmorse_sbm_robustness 확장
    Step 3: P-Audit P1-P7 표기 + canonical xref grep (W7 R-2 archive 회피)
    Step 4: SEAL 6-step (CV-1.16 SEAL template 재사용)
    Step 5: canonical.md §13 Cat A insert (L-HMORSE-LOCAL Cat A) + count 갱신
    Step 6: hypothesis_tree HT-3.8 → HT-3.9 (H-MORSE row PARTIALLY CLOSED → CLOSED, H-EK row 활성화)
  Track C: exp93 (Multi-step temporal Persist chaining, T-Temporal-Identity 다중 형성 확장)
  Decision gate (EOD): **CV-1.18 SEALED** 보장. Secondary SEAL 후보 (P-K-Select-Unified, L-Wigner-Projection-MERGE, L-Sinkhorn-Plan-Composition-Bound) 의 P5-P7 통과 여부 판정.
  Deliverables: Atlas §6-§7 + op0012_sink_scaling_attack.md + **CV-1.18 SEALED** + exp93 + CHANGELOG [CV-1.18] entry + pytest 220+1xf

Day 5 (Fri, 05-22) — Atlas v1.0 + CV-1.19 Optional Second SEAL + W8 Close
  Track A: MF_atlas.md §8 (Coupling regimes) + §9 (Dynamics gap map unlock chain 그래프) + §10-§11 (OP quick index + code mapping) + §12 (daily log 통합) → **v1.0 P5 promotion-ready**
  Track B: Secondary SEAL 시도 (stretch, optional) — Day 2-4 산출 중 P5-P7 통과 후보 → **CV-1.19 SEAL** (총 2 SEAL)
  Track C: exp94 (Phase diagram 3-regime grid, visual deliverable PNG → results/)
  W8 Close: weekly_summary.md 신설 (W6/W7 동형 8 sections) + Hard-Constraint Sweep + W9 진입 권장 (CV-1.20 target = Package II EK Cat B)
  Deliverables: Atlas v1.0 + CV-1.19 SEALED (optional) + exp94 + weekly_summary.md
```

### 분기 룰 (트랙 전환 조건)

- **트랙 A 막힘** (Atlas section 작성 60분 답보) → 트랙 C 실험으로 전환 (numerical 입력 확보 후 복귀)
- **트랙 B 막힘** (working sketch 60분 답보) → 트랙 A Atlas 다른 section 으로 전환
- **트랙 C 막힘** (실험 60분 답보) → 트랙 A 또는 B 로 전환, 실험은 다음 날 재시도
- **3 트랙 모두 막힘** (드물지만 가능) → 5/15 결정 C 6-stage framework 즉시 적용 → archive 결정 또는 broad survey 재실행

---

## 4. Success Criteria (수치)

| 항목 | Entry (5/16) | Target (5/22 EOD) | Stretch |
|---|---|---|---|
| Canonical version | CV-1.17 | **CV-1.18** (1 SEAL) | **CV-1.19** (2 SEAL) |
| Total claims | 98 | **99-101** (+1-3) | **105+** (+7) |
| Cat A 승급 | — | **≥1** (OP-HMORSE-LOCAL-A) | ≥2 |
| New Cat B candidates | — | **≥3** | ≥5 |
| New Cat C candidates | — | **≥2** | ≥3 |
| New experiments | — | **≥4** | ≥6 |
| Multi-Formation Atlas | 없음 | **v1.0** P5-ready | v1.1 promotion review |
| pytest | 215+1xf | **220+1xf** | 225+1xf |
| Working files (W8 신규) | 0 | **≥9** | ≥15 |
| OP 신규 / 해결 | — | ≥2 신규 / **≥1 해결** (OP-HMORSE-LOCAL-A) | ≥4 신규 / ≥2 해결 |
| HT version | HT-3.8 | **HT-3.9** | HT-3.10 |

---

## 5. Anti-Goals (W8 하지 않을 것)

5/15 결정 C 직접 carry-forward. 아래 시도 자체가 결정 C 위반.

- **z_t / S_0 / K_read reformulation 부활 시도** — `06_archive_pattern_diagnosis.md` 의 archive 패턴 6/6 부합 항목.
- **새 framework letter 도입** (V-, R-, U-, ...).
- **DECL-1.0 amend** — 별도 plan 없이 self-limitation 변경 금지.
- **u_t 단일장 가정 변경** — Q1 의 근본 가정.
- **scc/ 모듈 수정** — W7 와 동일 정책 (experiments/ + tests/ 만 신규).
- **Engineering proxy 도입** — Gaussian similarity, bilateral filter, diffusion maps, mean-shift 등 표준 도구 의 어휘적 차용.

---

## 6. Daily Discipline (매일 강제)

W7 회귀 패턴 (V-AFD/R-2) 재발 방지 운영 룰.

1. **Pre-work canonical xref check** (5분): 새 working file 생성 전 `grep -r "<핵심개념>" THEORY/canonical/ THEORY/working/` — 중복 사전 차단. W7 R-2 archive 의 직접 사유 (Round 4 audit) 가 이 단계 누락이었음.

2. **Sanity meta-check** (Day 1 infra 활용): 새 K=2 결과는 항상 `canonical_k2_hash()` 통과 + (l_second/l_max, Λ_coupling) 메트릭 강제 기록.

3. **Track switching**: 한 track 에 60분 막히면 즉시 다른 track 으로 이동.

4. **Decision gate (매일 EOD)**: 그 날 산출물에 *새 수학* 이 있는가?
   - YES → 정상 진행
   - NO + survey day → 정상 (Day 1, 또는 broad day)
   - NO + non-survey day → archive 분류 후보 (V-AFD/R-2 패턴) → 5/15 6-stage framework 즉시 적용

5. **CHANGELOG prepend**: 매 SEAL + 매 archive event 즉시 기록 (W7 누적 5 entries 동일 패턴).

---

## 7. Critical Files (수정 대상)

**Canonical (수정 가능, SEAL 시):**
- `THEORY/canonical/canonical.md` — §13 신규 entry insert (Day 4 CV-1.18, optional Day 5 CV-1.19)
- `THEORY/canonical/theorem_status.md` — count update + OP Quick Index 갱신 + L-HMORSE-LOCAL Cat B → Cat A row 갱신
- `THEORY/canonical/hypothesis_tree.md` — HT-3.8 → HT-3.9 (H-MORSE row CLOSED + H-EK 활성화) → stretch HT-3.10
- `THEORY/canonical/CV-1.18_SEAL.md` (신설), 옵션 `CV-1.19_SEAL.md`
- `THEORY/CHANGELOG.md` — W8 entries prepend ([CV-1.18], [W8 CLOSE], optional [CV-1.19])

**Working (신설, 최소 ≥9 파일):**
- `THEORY/working/MF/MF_atlas.md` (메인 deliverable, Day 1-5 누적)
- `THEORY/working/MF/broad_survey_{B1,B2,B3}.md` (Day 1, 3 Explore outputs)
- `THEORY/working/MF/k_select_pf_obs_unified_view.md` (Day 2)
- `THEORY/working/MF/op0005_dyn_kramers_sketch.md` (Day 2)
- `THEORY/working/MF/op0008_merge_wigner_attack.md` (Day 3)
- `THEORY/working/MF/op0012_sink_scaling_attack.md` (Day 4)
- `THEORY/logs/daily/2026-05-18 ~ 2026-05-22/` (5 directories, 각 ~5-10 files)
- `THEORY/logs/weekly/2026-05-W3/weekly_summary.md` (Day 5)

**Code (신설):**
- `CODE/experiments/exp90_sanity_canonical_xref.py` (Day 1)
- `CODE/experiments/exp91_ksoft_hard_recovery.py` (Day 2)
- `CODE/experiments/exp92_wigner_projection_robustness.py` (Day 3)
- `CODE/experiments/exp93_temporal_persist_chaining.py` (Day 4)
- `CODE/experiments/exp94_phase_diagram_3regime_grid.py` (Day 5)
- `CODE/tests/test_sanity_canonical_xref.py` (Day 1)
- `CODE/tests/test_k_soft_recovery.py` (Day 2)
- `CODE/tests/test_sigma_rich_formulas.py` (Day 3)

**Code (수정 금지 — W8 read-only):**
- `CODE/scc/*.py` 전부

---

## 8. 기존 함수 재사용 (Phase 1 감사 결과)

| Function | Path | Use case |
|---|---|---|
| `find_k_formations()` | `CODE/scc/multi.py` | K=1/2/3 ground-truth (exp91, exp93, exp94) |
| `transport_k_formations(phase2_mode=...)` | `CODE/scc/multi.py` | exp93 multi-step composition |
| `coupling_strength()` | `CODE/scc/multi.py` | exp94 phase diagram Λ_coupling contour |
| `classify_regime(method="geometric")` | `CODE/scc/multi.py` | exp94 regime heatmap |
| `compute_sigma_rich()` | `CODE/scc/sigma_rich.py` | exp92 Wigner robustness + Day 3 Atlas §5 직관 확인 |
| `persist_transport()` | `CODE/scc/transport.py` | exp93 Persist chaining |
| `k_soft()` (φ-sat default) | `CODE/scc/k_soft.py` | exp91 hard-K recovery |
| `persistence_h0()` | `CODE/scc/persistence.py` | exp91 H₀ bar 측정 |
| `EnergyComputer.hessian_finite_diff()` | `CODE/scc/energy.py` | Day 3 Wigner projection numerical Hessian (Lemma B3 path) |

→ **새 scc/ 함수 추가 0** 목표. 모두 기존 함수 재사용 + experiments/ + tests/ 신규.

---

## 9. Verification

### 매일 (Day 1-5 EOD)
```bash
cd /Users/ojaehong/Perception/Perception_theory/CODE
python3 -m pytest tests/ -v       # Day 1: 215+1xf / Day 2: 217+1xf / Day 3: 219+1xf / Day 4: 220+1xf
python3 experiments/exp9{X}_*.py   # 그 날 신규 실험
```

### SEAL 직전 (Day 4, optional Day 5)
1. `THEORY/working/<file>` 에 P1-P6 audit 명시적 표기
2. `grep -r "<핵심정리이름>" THEORY/canonical/` — duplicate 사전 차단
3. Block D 일관성 audit 13/13 PASS (cardinality / no-double-classification / cross-reference / hypothesis-tree-structure / CHANGELOG-ordering)
4. SEAL apply-order 6-step (CV-1.16 SEAL §F template 재사용)

### W8 Close (Day 5)
```bash
cd /Users/ojaehong/Perception/Perception_theory/CODE
python3 -m pytest tests/ -v       # ≥220+1xf (stretch 225+1xf)
ls THEORY/working/MF/             # MF_atlas.md + ≥5 새 working files
# theorem_status.md count check
```

### Archive 발생 시 (예방적 절차)
W7 V-AFD/R-2 와 같은 사이클 감지 시:
1. `_archive/<topic>_2026-05-W3/` 신설 + `ARCHIVE_NOTE.md` (사유 명시)
2. CHANGELOG `[ARCHIVE]` entry prepend
3. canonical / scc 무손상 확인
4. **archive 자체는 실패 아님** — *언어 재배치를 새 수학으로 잘못 인식한 것의 정직한 종결*. W7 의 두 archive 가 이 패턴.

---

## 10. Risk & Mitigation

| Risk | Probability | Mitigation |
|---|---|---|
| OP-HMORSE-LOCAL-A sharper residual 가 ~10⁴× gap closure 실패 | MED | Sub-task B (OP-HMORSE-SBM) 로 우회; CV-1.18 SEAL 은 secondary 후보 (P-K-Select-Unified 등) 로 |
| OP-0008-MERGE 2-approach (perturbation + RMT) 수렴 실패 | MED-HIGH | working candidate 로 보존, Cat C status 유지, W9+ deferred |
| OP-0012-SINK plan-level scaling gap 닫히지 않음 | HIGH | Cat C 신규 등록 만 (Cat B 승급 시도 안 함) |
| 사용자 메타-자각 ("또 회귀 아닌가?") | LOW (W7 결정 C 후) | 5/15 6-stage framework 즉시 적용; archive 빠른 결정 |
| Atlas 가 단순 canonical 재정리에 머무름 | MED | 매 section 끝 *gap 또는 새 후보 1개 이상* 강제 명시 룰 |
| pytest regression | LOW | Day 1 sanity infra + scc/ 무수정 정책 |
| 3 트랙 동시 막힘 (드물지만 가능) | LOW | 5/15 6-stage framework 적용 → archive 또는 broad survey 재실행 |

---

## 11. W9+ Preview (W8 close 시 갱신)

W9 (2026-05-25 ~ 2026-05-29) Phase 1 후보:

- **CV-1.20 target**: Package II Eyring-Kramers Cat B 진입 (OP-HMORSE-LOCAL-A Cat A + OP-0021 결합)
- **W9 main work 후보 1**: T-σ-Inherit (d-σ_standard) Cat C → Cat B 승급 (W8 Day 3 op0008_merge_wigner_attack 산출이 기반)
- **W9 main work 후보 2**: OP-0021 T_* registration 본격 (Mori-Zwanzig Route A or RG Route B — W8 Day 1 Agent B1 survey 가 입력)
- **W9 어시스턴스**: §F Step 2 housekeeping (CV-1.15 deferred), OP-0021 dual-naming reconciliation (CV-1.15/CV-1.16 carried)

W10+ 장기 후보:

- Package II Eyring-Kramers Cat A 승급
- OP-0008-MERGE/SPLIT σ_standard Wigner-projection Cat B → Cat A
- OP-0005-DYN Kramers rate full Cat A (Package II 의존)
- Commitment 16 (K-status) 최종 결정 plan
- DECL-1.0 amend plan (필요 시)

---

## 12. References

- **Source plan**: `/Users/ojaehong/.claude/plans/plan-scalable-plum.md` (approved 2026-05-16)
- **Predecessor week**: `THEORY/logs/weekly/2026-05-W2/weekly_summary.md` (W7 close)
- **Predecessor week plan**: `THEORY/logs/weekly/2026-05-W2/W7_strategic_plan.md` (형식 reference)
- **CV-1.17 SEAL**: `THEORY/canonical/CV-1.17_SEAL.md`
- **CV-1.16 SEAL** (OP-HMORSE-LOCAL-A target 명시): `THEORY/canonical/CV-1.16_SEAL.md §"Non-Overclaim"`
- **5/15 결정 C 6-stage framework**: `THEORY/logs/daily/2026-05-15/{02..07,99}.md`
- **DECLARATION.md DECL-1.0**: `THEORY/canonical/DECLARATION.md`
- **Hypothesis tree HT-3.8**: `THEORY/canonical/hypothesis_tree.md`
- **Open Problems Catalog**: `THEORY/canonical/theorem_status.md`
