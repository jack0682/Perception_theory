---
type: log/daily/plan
date: 2026-05-18
session_label: W8-Day1 (Mon) — Broad Survey + Atlas Skeleton + Sanity Infra
canonical_version: CV-1.17 (sealed, untouched)
prerequisite: 01_pre_brainstorm.md 읽기 (자기 점검 후 진입)
mode: survey day — 3 트랙 병렬 / 새 수학 0 정상 / canonical 0 edits
predecessor_decision: 2026-05-15 결정 C — 어휘 회귀 종결, 수학적 정공법 진입
---

> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]] · [[W8_strategic_plan]]


# 00 — Plan (2026-05-18, W8-Day1)

## Mission

W8 의 첫 영업일 — **세 트랙 (A Atlas / B Broad Survey / C Sanity Infra) 의 *동시 진입***. Day 1 의 핵심은 *수학 산출* 이 아니라 *W8 5 영업일의 입력 확보*:

1. **Atlas skeleton** (12 sections × ~1 paragraph + xref) — Day 2-5 에 채워질 deliverable 의 골격.
2. **Broad survey (B2 PRIMARY + B1/B3 LIGHTER)** — Day 2-4 의 Track B sketch 의 *직접 입력*. B2 는 OP-0008 attack 의 *2-route framework 첫 매핑*.
3. **Sanity infra** — W7 의 V-AFD/R-2 회귀 패턴 *자동 차단* 의 운영 도구.

**Decision gate (EOD)**: 새 수학 0 — *survey day 이므로 정상*. 핵심 metric = *OP-0008 attack 초기 input 확보*.

---

## Context (왜 오늘 이 작업인가)

W7 EOD (5/15) 의 결정 C — *어휘 회귀 패턴 (V-AFD/R-2/z_t 3 회) 의 증거 기반 종결*. 결정 C 의 직접 함의:

> 통찰의 진짜 수학적 진척 = canonical 내부 작업 (H-MORSE-LOCAL-A, Package II, σ_standard MERGE/SPLIT).

5/16 사용자 자기-진단:

> 3-theorem 압축 연습 (T8 + T-L1-F + T-Temporal-Identity) 이 *secured Cat A* 기준으로만 작동. SCC 의 *distinctive content* (σ-inheritance + OMS-2.0 quotient) 는 압축 후보로 올라오지 못함 — Cat B/C/framework-only 상태이기 때문. → W8 priority 가 secured layer 정밀화 (OP-HMORSE-LOCAL-A) 만이 아니라, **distinctive layer 의 secure (OP-0008 σ_standard MERGE/SPLIT) 도 동시에 공격하는 방향으로 재조정**.

따라서 W8 은 *3-axis simultaneous attack*. Day 1 은 그 *공격의 입력 확보* — *survey day*.

**Entry state (2026-05-18 morning):**
- CV-1.17 SEALED (2026-05-15 evening)
- HT-3.8
- 68A / 19B / 6C / 5R = 98 claims (~70%)
- pytest 215 passed + 1 xfailed
- H-MORSE row PARTIALLY CLOSED (Local Cat B; Global Cat A path = OP-HMORSE-LOCAL-A)
- T-σ-Inherit parts (a,b,d-direction,e) Cat B / (c,d-σ_standard) Cat C ← W8 distinctive priority target

---

## Day 1 작업 (3 트랙 병렬)

### Track A — Atlas Skeleton (목표 ~1.5h)

**산출 파일:** `THEORY/2_substrate/multiformation/MF_atlas.md` v0.1

**12 sections, 각 ~1 paragraph + xref + *gap 또는 새 후보 1개* 명시:**

1. Multi-formation primitive (D-6a, K-field architecture, Commitment 16 status) — xref `canonical.md §3` + Comm.16
2. Static layer (T-L1-F/M Cat A, T-Persist-K-Sep/Weak/Unified) — xref `canonical.md §13`
3. Equilibrium K-selection (T-K-Select-PF Cat B target) — Day 2 채움
4. Observed K-selection (T-K-Select-OBS Cat B target) — Day 2 채움
5. σ-inheritance (T-σ-Inherit 6 parts) — Day 3 채움
6. Temporal composition (T-Temporal-Identity Cat A + T-CC-StableK-Kernel Cat B) — Day 4 채움
7. OMS-2.0 Appendix lift — Day 4 채움
8. Coupling regimes + Λ_coupling 파라미터화 — Day 5 채움
9. Dynamics gap map (OP-0005-DYN/OP-0008/OP-0012-SINK/OP-0021 unlock chain) — Day 5 채움
10. Open problems quick index (multi-formation 관련만 추출)
11. Code mapping (scc 함수별 정리/lemma 매핑) — Day 2-5 누적
12. W8 daily expansion log — 각 day 결과 prepend

**각 section 강제 룰:** 끝에 *gap 또는 새 후보 1개 이상* 명시 — Atlas 가 단순 재정리로 끝나지 않게 (W8 plan §2 G1).

**Pre-work xref check (필수):**
```bash
grep -r "MF_atlas\|multi-formation atlas" THEORY/canonical/ THEORY/working/
```

### Track B — Broad Survey 3-parallel (목표 ~3h, B2 PRIMARY)

**3-parallel Explore agents — *수학적으로 독립* 인 OP 후보 동시 survey** (W8 plan §2 G5):

#### Agent B2 PRIMARY — OP-0008 Wigner-projection 2-route mapping

**산출 파일:** `THEORY/2_substrate/multiformation/broad_survey_B2.md` (가장 두꺼움, ~150-250줄 목표)

**내용:**
- Approach (a) **Perturbation theory**: $H_{\mathrm{merged}} = H_1 \oplus H_2 + V_{\mathrm{coup}}$, $\lVert V_{\mathrm{coup}} \rVert_F = O(d_{\mathrm{inter}}^{-\alpha})$, Kato resolvent expansion (Reed-Simon IV §XIII.5) 의 SCC adaptation 가능성.
- Approach (b) **RMT level repulsion**: GOE projection, $P(s) \sim s$ as $s \to 0$, Aut(G) character data 결여 bypass 가능성.
- **두 route 의 *동일 σ_standard map* 산출 수렴 분석 framework** — Day 2 (perturbation thrust) / Day 3 (RMT + audit) 의 *직접 입력*.
- 8×8, 12×12 toy 의 numerical cross-check 계획 (Day 3 exp92).

#### Agent B1 LIGHTER — OP-0021 Mori-Zwanzig + canonical MF/pf_tstar_langevin.md gap 5개

**산출 파일:** `THEORY/2_substrate/multiformation/broad_survey_B1.md` (~80-120줄)

**내용:** W9 staging only — Mori-Zwanzig Route A literature + canonical `MF/pf_tstar_langevin.md` 의 5 gap (NOP-F / NOP-J 중 가장 가벼운 것) 식별.

#### Agent B3 LIGHTER — OP-0005-DYN Kramers 3-pillar multi-formation lift

**산출 파일:** `THEORY/2_substrate/multiformation/broad_survey_B3.md` (~80-120줄)

**내용:** W9+ staging only — nucleation / metastability / coarsening 의 multi-formation 확장 후보. Package II 입력.

**Pre-work xref check (필수):**
```bash
grep -r "OP-0008\|Wigner-projection\|MERGE/SPLIT" THEORY/canonical/ THEORY/working/MF/
grep -r "Mori-Zwanzig\|OP-0021\|T_\*" THEORY/canonical/ THEORY/working/
grep -r "OP-0005-DYN\|Kramers.*rate\|metastability" THEORY/canonical/ THEORY/working/
```

### Track C — Sanity Infra (목표 ~1.5h)

**산출 파일:**
- `CODE/experiments/exp90_sanity_canonical_xref.py`
- `CODE/tests/test_sanity_canonical_xref.py`

**핵심 함수:**
- `canonical_k2_hash(state) -> str` — permutation-invariant K=2 state hash; 동일 K=2 결과가 *재포장* 으로 들어오면 hash 동일 → duplicate detection.
- `subthreshold_demo_check(result) -> bool` — `(l_second/l_max, Λ_coupling)` 메트릭 *강제 기록*; sub-threshold demo 의 R-2-style "K-tuple smooth" 실패 패턴 자동 검출.

**테스트 시나리오:**
- hash idempotence (동일 state ↔ 동일 hash, permutation 무시).
- duplicate detection (V-AFD/R-2 의 K_act 같은 라벨 변경 시 hash 불변 확인).
- subthreshold_demo_check 의 양/음 case (canonical 15×15 substrate).

**검증 (EOD):**
```bash
cd CODE
python3 -m pytest tests/test_sanity_canonical_xref.py -v
python3 experiments/exp90_sanity_canonical_xref.py
```

**예상 pytest:** 215+1xf (entry) → 215+1xf (Day 1 sanity test 는 *별도 추가 — 기존 215 변동 없음*, 정확히는 215 + N_new + 1xf). W8 plan §2 G4 의 step.

---

## 분기 룰 (트랙 전환 조건, W8 plan §3)

- **Track A 막힘** (Atlas section 작성 60분 답보) → Track C 실험으로 전환.
- **Track B 막힘** (broad survey 60분 답보) → Track A Atlas 다른 section 으로 전환.
- **Track C 막힘** (실험 60분 답보) → Track A 또는 B 로 전환, 실험은 Day 2 재시도.
- **3 트랙 모두 막힘** (드물지만 가능) → 5/15 결정 C 6-stage framework 즉시 적용 → archive 결정 또는 broad survey 재실행.

---

## Decision gate (Day 1 EOD)

| 검사 | Day 1 통과 기준 |
|---|---|
| **canonical 0 edits** | canonical.md / theorem_status.md / hypothesis_tree.md / CHANGELOG.md *수정 없음* (Day 1 survey day) |
| **새 어휘 생성 금지** | V-, R-, U-, P1/P2/... 같은 framework letter *0 도입* (5/15 결정 C carry-forward) |
| **OP-0008 attack 초기 input 확보** | broad_survey_B2.md 가 *2-route framework 의 첫 매핑* 을 명시적으로 담음 — Day 2 perturbation thrust 의 *직접 입력* 가능 |
| **Atlas v0.1 skeleton** | 12 sections × ~1 paragraph + xref + *gap 또는 새 후보 1개* 명시 |
| **Sanity infra PASS** | exp90 + test_sanity_canonical_xref.py PASS |
| **새 수학 0** | *정상* — survey day. archive 분류 대상 아님. |
| **Pre-work xref check** | 모든 신규 working 파일 작성 *전* grep 수행 기록 |
| **archive 재포장 회피** | "z_t/S_0/K_read 가 사실 OP-0008 의 부분 시도" 식 *후행 정합화* 시도 금지 |

---

## Out-of-scope (오늘)

- canonical 직접 수정 (Day 4-5 의 SEAL day)
- DECL-1.0 amend (W8 anti-goal §5)
- `scc/` 모듈 수정 (W8 anti-goal §5 — `experiments/` + `tests/` 만)
- V-AFD/R-2/z_t 부활 시도 (5/15 결정 C 직접 carry-forward)
- 새 framework letter 도입 (V-, R-, U-, ...)
- u_t 단일장 가정 변경 (Q1 의 근본 가정)
- Engineering proxy 도입 (Gaussian similarity, bilateral filter, diffusion maps, mean-shift)
- Day 2-5 의 작업 *선취* — Day 1 은 *입력 확보* 만

---

## 호흡 (시간 운용)

**5/18 은 single-session 가정 안 함.** 3-track 병렬 day.

- Track A (Atlas skeleton) ≥ 1.5h
- Track B (Broad Survey, B2 PRIMARY) ≥ 3h (B2 가장 두꺼움)
- Track C (Sanity infra + exp90) ≥ 1.5h
- 한 track 60분 막힘 → 즉시 다른 track 전환

Atlas §1-§7 의 *살 채우기* 는 Day 4 EOD 까지 보장 — Day 1 은 *skeleton 만* (W8 plan §10 risk mitigation).

---

## 위험 (사전 인지)

| Risk | Mitigation |
|---|---|
| OP-0008 B2 survey 가 "재포장된 V-AFD/R-2" 가 됨 | Pre-work xref check 의무 + B2 산출물 *2-route framework* 형태 (perturbation + RMT) 명시적 distinct 유지 |
| Atlas skeleton 이 *단순 재정리* 로 끝남 | 각 section *gap 또는 새 후보 1개 이상* 강제 (W8 plan §2 G1 명시) |
| Track B 가 Track A 시간 잠식 | Day 1 시간 분배 *명시* (위 §"호흡") — Atlas skeleton 은 1.5h 보장 |
| Sanity infra 가 *trivial* 함 | hash idempotence + duplicate detection 의 *수치 PASS* 자체가 Day 2-5 의 운영 도구 (수학적 substantive 가 아니라 *operational substantive*) |
| 5/15 결정 C 의 *carry-forward 실수* | Pre-brainstorm §"5/15 결정 C carry-forward" 통과 후에만 작업 진입 |
| Decision gate "새 수학 0" 의 *심리적 압박* | 5/15 결정 C 자체가 "survey day 에 새 수학 0 = 정상" 을 정의 — *결정 C carry-forward* |

---

## 출력 파일 (예정)

| 파일 | 단계 |
|---|---|
| `00_index.md` | ✓ 작성 완료 |
| `00_plan.md` | ✓ 본 파일 |
| `01_pre_brainstorm.md` | 진입 전 |
| `02_track_A_atlas_skeleton.md` | Track A 산출 보고 |
| `03_track_B2_op0008_primary.md` | Track B Agent B2 PRIMARY 산출 보고 |
| `04_track_B1_op0021_lighter.md` | Track B Agent B1 LIGHTER 산출 보고 |
| `05_track_B3_op0005_lighter.md` | Track B Agent B3 LIGHTER 산출 보고 |
| `06_track_C_sanity_infra.md` | Track C 산출 + pytest PASS 보고 |
| `99_summary.md` | EOD — Decision gate 결과 + Day 2 입력 준비 |

---

## Verification (Day 1 EOD)

```bash
cd /home/jack/Perception_theory/CODE

# Track C
python3 -m pytest tests/test_sanity_canonical_xref.py -v
python3 experiments/exp90_sanity_canonical_xref.py

# 기존 pytest regression check
python3 -m pytest tests/ -v   # 215 passed + 1 xfailed (+ Day 1 신규)

# Track A
ls -la THEORY/2_substrate/multiformation/MF_atlas.md   # exists + 12 sections

# Track B
ls -la THEORY/working/MF/broad_survey_{B1,B2,B3}.md   # 3 파일 존재

# canonical untouched check
git status THEORY/canonical/   # 0 changes
```

---

## 다음 (Day 2 Tue 5/19) 입력 준비

Day 1 EOD 의 산출이 Day 2 의 *직접 입력*:

- broad_survey_B2.md (Day 1) → `op0008_merge_wigner_perturbation.md` (Day 2 PRIMARY, Kato resolvent expansion + 5×5 toy analytic)
- broad_survey_B3.md (Day 1) → `op0005_dyn_kramers_sketch.md` (Day 2, Cat C SKETCH, W9+ staging)
- MF_atlas.md v0.1 (Day 1) → §3 (T-K-Select-PF) + §4 (T-K-Select-OBS) full ~80-120줄 each (Day 2)
- exp90 + test_sanity_canonical_xref (Day 1) → Day 2-5 *매일 호출 보조 도구*

---

*5/18 의 first principle: survey day. 새 수학 0 정상. OP-0008 attack 초기 input 확보가 day 의 핵심 metric. canonical 0 edits.*
