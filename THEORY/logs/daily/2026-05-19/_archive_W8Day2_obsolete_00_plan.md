---
type: log/daily/plan
date: 2026-05-19
session_label: W8-Day2 (Tue) — K-Selection Deep Dive + OP-0008 Perturbation Theory PRIMARY + K-soft Validation
mode: hybrid — primary deep-attack (Track B op0008 perturbation), secondary survey (Track A Atlas + Track C exp91)
canonical_version: CV-1.17 (sealed 2026-05-15, untouched 예정)
predecessor: 2026-05-18/99_summary.md (W8-Day1 survey day complete + v2/v3 meta-evolution)
strategic_plan: THEORY/logs/weekly/2026-05-W3/W8_strategic_plan.md §3 Day 2
prompt_body: MAIN_PROMPT_v3.md (first real-world use)
output_files:
  - 00_index.md
  - 00_plan.md
  - 01_pre_brainstorm.md  # 사용자 직접
  - 02_track_B_op0008_perturbation.md
  - 03_track_A_atlas_3_4.md
  - 04_track_C_exp91_ksoft.md
  - 05_track_B_op0005_dyn_secondary.md  # 선택, 10% time
  - 99_summary.md
cot_enforcement_level: strict  # deep-attack primary (Track B PRIMARY); standard for survey track A/C
coc_enforcement_level: strict  # 모든 lemma 의 anchored chain
expected_session_count: 1-2  # multi-session day (3-track 병렬)
---

> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]] · [[W8_strategic_plan]] · [[00_index]] · [[../2026-05-18/99_summary|어제 99_summary]] · [[../2026-05-18/broad_survey_B2|어제 broad_survey_B2]] · [[../MAIN_PROMPT_v3]]


# 00 — Plan (2026-05-19, W8-Day2)

## Mission

W8 의 *두 번째 영업일* — **첫 attack day**. Day 1 의 *survey 입력 확보* → Day 2 의 *Track B 본격 attack*. 핵심:

1. **Track B PRIMARY (90% time)**: `op0008_merge_wigner_perturbation.md` — broad_survey_B2.md §3 Route (a) Kato resolvent perturbation 의 explicit form 본격 attack. 5×5 toy analytic + $O(\varepsilon^2)$ Kato expansion + Schur-complement reduction + post-merger σ_standard 의 *Cat C SKETCH 또는 Cat B candidate*. **W8 plan §3 Day 2 decision gate 의 *primary metric***.

2. **Track A (1.5h)**: MF_atlas.md §3 (T-K-Select-PF) + §4 (T-K-Select-OBS) full (~80-120 lines each) + 신규 `k_select_pf_obs_unified_view.md` (P-K-Select-Unified Cat B SKETCH).

3. **Track B secondary (10% time)**: `op0005_dyn_kramers_sketch.md` — broad_survey_B3.md §3 Pillar 1 Nucleation 의 Cat C SKETCH (W9+ staging only).

4. **Track C (1.5h)**: `exp91_ksoft_hard_recovery.py` + `test_k_soft_recovery.py` (K-soft hard-K recovery + Lipschitz numerical, gap §B-5 closure) — 2 tests PASS.

**Decision gate (EOD, W8 plan §3 Day 2 의 직접 인용)**: *새 수학 = OP-0008 perturbation route candidate Cat B statement 도출. K-soft Lipschitz numerical 지지*.

**Mode**: hybrid (primary deep-attack on Track B, secondary survey on Track A + Track C). Track A 도 *substantive content* (Atlas §3/§4 full) 이지만 *기존 Cat B canonical* 의 *unified view* 작성이므로 *survey-PRIMARY 형태*.

---

## Context (왜 오늘 이 작업인가)

W8-Day1 (어제) 의 산출:

- broad_survey_B2.md (~330 lines) — **OP-0008 2-route framework 첫 매핑** 완료. §3 Route (a) Kato perturbation + §4 Route (b) RMT Wigner-Dyson + §5 수렴 framework + §6 Route (c) preserved.
- broad_survey_B1.md / broad_survey_B3.md — W9+ staging input.
- MF_atlas.md v0.1 — 12 sections × 1 paragraph + gap markers.
- 신규 sanity infra (`canonical_k2_hash` + `subthreshold_demo_check`, 10 tests PASS).
- v2/v3 prompt body evolution (parallel deployment).

오늘 Day 2 = 어제 broad_survey_B2.md §3 의 *직접 attack*. 어제 99_summary §"Day 2 의 직접 입력" 표 의 6 매핑 모두 활성화.

5/16 사용자 자기-진단 (W8 plan §0 carry-forward):
> distinctive content (σ-inheritance + OMS-2.0) 는 압축 후보로 못 올라옴 — Cat B/C/framework-only 상태이기 때문. → W8 priority 가 distinctive layer 의 secure (OP-0008 σ_standard MERGE/SPLIT) 도 동시에 공격.

→ Track B PRIMARY 의 OP-0008 attack = distinctive layer secure 의 *직접 progress*.

**Entry state (2026-05-19 morning)**:
- CV-1.17 SEALED (2026-05-15 evening, untouched).
- HT-3.8.
- 68A / 19B / 6C / 5R = 98 claims (~70%).
- pytest 225 passed + 1 xfailed (어제 Track C 의 +10 신규 tests).
- T-σ-Inherit (c) MERGE σ_standard Cat C — **본 day Track B PRIMARY target**.

---

## Day 2 작업 (3 트랙 병렬, 시간 분배 명시)

### Track B PRIMARY — op0008 Kato perturbation explicit form (목표 ~3h, 90% time)

**산출 파일**: `THEORY/working/MF/op0008_merge_wigner_perturbation.md` (P3 target, ~200-300 lines).

**내용 (어제 broad_survey_B2.md §3 의 직접 입력 + 본격 attack)**:

1. **§1 Mission re-statement** — broad_survey_B2.md §3 의 직접 인용 + 본 day 의 *attack target* 명시 (Cat C SKETCH 또는 Cat B candidate).

2. **§2 5×5 toy analytic 의 explicit form**:
   - 5×5 graph (path graph $P_5$ 또는 cycle $C_5$) 의 K=2 stable formation 두 개.
   - $H_{i_1, i_1}$ + $H_{i_2, i_2}$ 의 *explicit eigenvalue + eigenvector* 계산 (closed form 또는 numerical anchor).
   - Cross-block $V$ 의 *explicit decay* (Coupling Bound Lemma 적용).

3. **§3 Kato resolvent expansion**:
   - $\lambda_a(\varepsilon) = \lambda_a^{(0)} + \varepsilon \langle \phi_a^{(0)}, V \phi_a^{(0)} \rangle + \varepsilon^2 \sum_{b \neq a} \frac{|\langle \phi_a^{(0)}, V \phi_b^{(0)} \rangle|^2}{\lambda_a^{(0)} - \lambda_b^{(0)}} + O(\varepsilon^3)$.
   - 5×5 toy 의 *각 항* 의 explicit calculation.
   - $O(\varepsilon^2)$ 까지 의 deterministic form.

4. **§4 Schur-complement reduction**:
   - Pre-merger $H_\mathrm{pre}$ 와 post-merger $H_\mathrm{post}$ 의 *Schur-complement* 관계.
   - Mass-rescaling factor $\mu(m_j, m_k) = m_j m_k / (m_j + m_k)$ (reduced-mass form) 의 *derivation 시도* — broad_survey_B2.md §"NOQ-B2-1" 의 직접 attack.

5. **§5 Cat 자기 분류**:
   - 5×5 toy 의 Kato $O(\varepsilon^2)$ form: Cat A (numerical anchor 완전).
   - 일반 finite graph 의 Schur-complement reduction: 잠정 Cat B (Schur 의 boundary matching 의 rigorous form 필요).
   - 일반 graph 의 reduced-mass form: 잠정 Cat C (5×5 toy 의 numerical 지지만; 일반화 미증명).

6. **§6 CoT/CoC chain inline** (v3 §7a + §7b 강제):
   - 각 lemma 별 Premise / Inference / Conclusion / Anchor 4-tuple.
   - Prior anchors: canonical §11.1 Commitment 14, working sigma_rich_wigner_derivation.md §3.3, external Reed-Simon IV §XIII.5.
   - Inverse-causation check.

7. **§7 Day 3 의 직접 입력**:
   - Route (b) RMT 와의 *수렴 분석* 의 입력 (Day 3 `op0008_merge_wigner_rmt.md` 의 §"수렴 audit").
   - 8×8 / 12×12 toy numerical cross-check 의 *initial config* (Day 3 exp92).

**예상 effort**: 3-4h. Day 2 의 *single primary task*.

**Pre-work xref check** (의무, §15.1 of MAIN_PROMPT_v3):
```bash
grep -r "op0008_merge_wigner_perturbation\|Kato resolvent.*SCC\|5x5 toy.*K-jump" THEORY/canonical/ THEORY/working/MF/
```

### Track A — Atlas §3 + §4 full + k_select_pf_obs_unified_view (목표 ~1.5h)

**산출 파일 1**: `THEORY/working/MF/MF_atlas.md` v0.1 → v0.2 (§3 + §4 full).

**§3 Equilibrium K-selection (T-K-Select-PF Cat B) full**:
- T-K-Select-PF (canonical Cat B, CV-1.10 Session R 2026-05-06) 정리 본문 재기술.
- P-F-A1 Package I (Cat A, CV-1.9) 의 4 정리 (T-PF-A1-AR / SDE / GI / PE) 의 *입력 chain*.
- $p_K = \pi_{T_*}(\mathcal{B}_K) = Z_K / Z$ explicit form.
- $K^* = \arg\max_K p_K$ + $K^*$ uniqueness 의 *open question* 명시.
- Cat A path: explicit $\sigma_M$-null computation in T-PF-A1-AR coordinates.

**§4 Observed K-selection (T-K-Select-OBS Cat B) full**:
- T-K-Select-OBS (canonical Cat B, CV-1.11 Session Y 2026-05-06) 정리 본문 재기술.
- Posterior $p_K(\mathfrak{O}_t) = Z_K^\mathrm{obs} / Z^\mathrm{obs}$ explicit form.
- Bayes on Gibbs prior (Package I) with LM1-LM3 likelihood.
- exp85 ALL PASSED (3/3 scenarios, 12×12 grid) numerical anchor.
- Cat A path: full stereo likelihood $(H_L, H_R)$ canonicalization.

**산출 파일 2**: `THEORY/working/MF/k_select_pf_obs_unified_view.md` (P3 target, ~80-120 lines).

**내용**:
- T-K-Select-PF + T-K-Select-OBS 의 *통합 view* — observation 부재 시 prior recovery + observation 충분 시 likelihood dominance.
- **P-K-Select-Unified Cat B SKETCH** 후보 — 가설: "$K^*(\mathfrak{O}_t)$ 는 $\mathcal{L}_\mathrm{obs} \to 1$ 의 limit 에서 $K^*$ (prior) 로 *연속* 수렴".
- CoT/CoC chain inline.

**Pre-work xref check**:
```bash
grep -r "k_select_pf_obs_unified\|P-K-Select-Unified\|prior recovery limit" THEORY/canonical/ THEORY/working/MF/
```

### Track C — exp91 + test_k_soft_recovery (목표 ~1.5h)

**산출 파일**: `CODE/experiments/exp91_ksoft_hard_recovery.py` + `CODE/tests/test_k_soft_recovery.py`.

**핵심 함수 (test 의 의무)**:
- `test_ksoft_recovers_hard_K_in_well_separated` — well-separated regime 에서 $K_\mathrm{soft} \approx K_\mathrm{act}$ 확인.
- `test_ksoft_lipschitz_constant_bound` — $K_\mathrm{soft}$ 의 Lipschitz constant $L_K \leq 4 \cdot L_\phi \cdot n$ (canonical §8 ksoft_phi_proof.md 의 Lipschitz bound) 의 numerical 지지.

**exp91 내용** (gap §B-5 closure):
- 15×15 grid, K=2/3/4 stable formation.
- $\phi_\mathrm{sat}$ (default) + $\phi_\mathrm{lin}$ variant.
- $K_\mathrm{soft}$ vs $K_\mathrm{act}$ scatter — well-separated regime ($\Lambda_\mathrm{coupling} < 0.01$) 에서 일치 확인.
- Lipschitz constant numerical bound 측정 — 이론 $4 L_\phi n$ 와 비교.

**검증 (EOD)**:
```bash
cd CODE
python3 -m pytest tests/test_k_soft_recovery.py -v
python3 experiments/exp91_ksoft_hard_recovery.py
```

**예상 pytest**: 225+1xf (entry) → 227+1xf (+2 신규).

**Sanity meta-check** (어제 sanity infra 의 *첫 호출*):
- exp91 의 K=2 결과 → `canonical_k2_hash()` + `subthreshold_demo_check()` 의무 호출.
- `(l_second/l_max, Λ_coupling)` 메트릭 강제 기록 → `04_track_C_exp91_ksoft.md` 의 §"Sanity check" 에 inline.

**Pre-work xref check**:
```bash
grep -r "exp91_ksoft\|test_k_soft_recovery\|K_soft.*hard.*recovery" CODE/ THEORY/
```

### Track B secondary — op0005_dyn_kramers_sketch (목표 ~30min, 10% time)

**산출 파일**: `THEORY/working/MF/op0005_dyn_kramers_sketch.md` (P3 target, Cat C SKETCH, ~80-120 lines).

**내용 (어제 broad_survey_B3.md §3 Pillar 1 Nucleation 의 입력)**:
- $\Gamma_{K_0 \to K_0+1}$ 의 *Cat C SKETCH* form.
- *W9+ staging only* — *증명 시도 부재* 명시.
- Heterogeneous nucleation 의 *spatial preference* 의 *outline* (Langer 1967 + Bovier-Manzo 2002 외부 reference).
- Cat C SKETCH (Cat B 승급은 W9+).

**Pre-work xref check**:
```bash
grep -r "op0005_dyn_kramers_sketch\|nucleation.*multi.*formation" THEORY/canonical/ THEORY/working/MF/
```

---

## 분기 룰 (트랙 전환 조건, W8 plan §3)

- **Track B PRIMARY 막힘** (60분 답보) → Track A Atlas 작성으로 전환 (Track A 의 *기존 canonical 재기술* 이 *심리적 reset* 제공).
- **Track A 막힘** (60분 답보) → Track C exp91 으로 전환 (numerical 입력 확보 후 복귀).
- **Track C 막힘** (60분 답보) → Track B secondary 또는 Track B PRIMARY 의 다른 section 으로 전환.
- **3 트랙 모두 막힘** (드물지만 가능) → 5/15 결정 C 6-stage framework 즉시 적용 → archive 결정 또는 plan 재검토 (review mode 로 *내부 전환*).

---

## Decision gate (Day 2 EOD, W8 plan §3 Day 2 직접 인용)

| 검사 | Day 2 통과 기준 |
|---|---|
| **새 수학 — OP-0008 perturbation route candidate Cat B statement 도출** | Track B PRIMARY 의 op0008_merge_wigner_perturbation.md 가 *substantive lemma* 의 Cat C SKETCH 또는 Cat B candidate 산출 |
| **K-soft Lipschitz numerical 지지** | Track C exp91 의 Lipschitz constant bound 측정 + 이론 $4 L_\phi n$ 와 *일치* (factor 2 이내) |
| **canonical 0 edits** | `git status THEORY/canonical/` 0 changes |
| **새 어휘 생성 0** | V-, R-, U-, framework letter *0 도입* (§8b 규칙 1 of MAIN_PROMPT_v3) |
| **Atlas §3 + §4 full** | MF_atlas.md v0.1 → v0.2 (§3 + §4 각 80-120 lines) |
| **신규 working files: 3건** | op0008_merge_wigner_perturbation + op0005_dyn_kramers_sketch + k_select_pf_obs_unified_view |
| **Sanity infra 첫 호출** | exp91 의 K=2 결과에 `canonical_k2_hash()` + `subthreshold_demo_check()` 호출 + 메트릭 기록 |
| **Pre-work xref check (4건)** | Track B/A/C/B-secondary 의 4 grep 모두 수행 + 결과 보고 file 머리에 기록 |
| **§7a CoT enforcement (Track B PRIMARY strict)** | Track B 의 각 lemma 의 Premise/Inference/Conclusion/Anchor 4-tuple 명시 |
| **§7b CoC enforcement (모든 mandatory 위치 strict)** | 각 lemma 의 prior_anchors + causation_chain + inverse_causation_check 3-block |
| **§8a archive pattern P1-P6 자가 점검** | 0-2/6 부합 (3+ 위험 시 inline 보고) |
| **pytest regression 0** | 225+1xf → 227+1xf (+2 신규 K-soft tests; 기존 225 변동 0) |

---

## Out-of-scope (오늘)

- canonical 직접 수정 (Day 4-5 의 SEAL day).
- DECL-1.0 amend (W8 anti-goal §5).
- `scc/` 모듈 수정 (W8 anti-goal §5 — `experiments/` + `tests/` 만 신규).
- V-AFD/R-2/z_t 부활 시도 (5/15 결정 C carry-forward).
- 새 framework letter (V-, R-, U-, $D_0^*$, ...) 도입.
- Engineering proxy (Gaussian similarity, bilateral filter, diffusion maps, mean-shift) 도입.
- Route (b) RMT 의 본격 attack (Day 3 작업).
- 8×8 / 12×12 toy numerical cross-check (Day 3 exp92 작업).
- T-σ-Inherit 4 parts partial canonical promotion (Day 5 Gate B fallback).
- Day 3-5 의 작업 *선취* — Day 2 는 *Track B PRIMARY 의 첫 attack day* 만.

---

## 호흡 (시간 운용)

**5/19 는 multi-session 가정** (3-track 병렬 day, 어제와 동일).

- Track B PRIMARY ≥ 3-4h (가장 두꺼움, deep-attack mode strict CoT/CoC)
- Track A ≥ 1.5h
- Track C ≥ 1.5h
- Track B secondary ≥ 0.5h

한 track 60분 막힘 → 즉시 다른 track 전환 (분기 룰 §"분기").

Track B PRIMARY 의 *substantive lemma 도출* 이 Day 2 의 *single most important deliverable*. 다른 track 의 *완성도* 보다 *Track B 의 깊이* 우선.

---

## 위험 (사전 인지)

| Risk | Mitigation |
|---|---|
| Track B 의 Kato expansion 의 explicit form 도출 불가 (5×5 toy 의 closed form 어려움) | 5×5 path graph $P_5$ 의 explicit eigenvalues (well-known) 사용 + numerical anchor 로 대체 + Cat C SKETCH 로 fallback |
| Schur-complement reduction 의 *boundary matching* rigorous form 불가 | 본 day 는 *informal derivation* 만, Day 3+ 의 rigorous form 으로 이연 + Cat C SKETCH 만 |
| Reduced-mass form $\mu = m_j m_k / (m_j + m_k)$ 의 *5×5 toy 에서 numerical 지지 부재* | Cat C → 다른 functional form 시도 (e.g., $\mu = \min(m_j, m_k)$, $\mu = (m_j + m_k) / 2$) — broad_survey_B2.md §"NOQ-B2-1" 의 attack 의 자연 분기 |
| Track A Atlas §3-§4 full 작성 의 *기존 canonical 재기술* 만 끝나 *gap/new candidate* 명시 미흡 | W8 plan §2 G1 의 강제 룰 (각 section 끝 gap/new candidate ≥1) inline 명시; *재정리 회피* 자기 강제 |
| Track C exp91 의 Lipschitz constant numerical bound 가 *이론 $4 L_\phi n$ 와 불일치* | exp91 의 실패는 *theory 의 수정 신호* — Day 3 의 추가 numerical anchor 로 *원인 분석* 후 결정 |
| Sanity infra 첫 호출 의 *기능 검증 부족* (어제 작성한 도구) | exp91 의 K=2 결과 가 *expected hash 와 일치* 확인; 불일치 시 sanity infra 의 *bug 추적* — Track C 의 작업 list 1건 추가 |
| v3 의 first real-world use 의 *over-engineering* | Plan-mode entry §A-§G 작성 시 *light* form 채택 가능 (§A + §G 만, sketch level plan 의 경우) — audit §7.2 #2 |
| §7a CoT 4-tuple form 의 *과부담* | Track B PRIMARY 만 strict, Track A/C 는 standard — *adaptive enforcement* |

---

## 출력 파일 (예정)

| 파일 | 단계 |
|---|---|
| `00_index.md` | ✓ 작성 완료 |
| `00_plan.md` | ✓ 본 파일 |
| `01_pre_brainstorm.md` | 진입 전 (사용자 직접 또는 에이전트 plan-mode 에서) |
| `02_track_B_op0008_perturbation.md` | Track B PRIMARY 산출 보고 |
| `03_track_A_atlas_3_4.md` | Track A 산출 보고 |
| `04_track_C_exp91_ksoft.md` | Track C 산출 보고 |
| `05_track_B_op0005_dyn_secondary.md` | Track B secondary 산출 보고 (10% time, 선택) |
| `99_summary.md` | EOD — Decision gate 결과 + Day 3 입력 준비 + v3 first real-world audit |

추가 working files:
| 파일 | 단계 | Cat 후보 |
|---|---|---|
| `THEORY/working/MF/op0008_merge_wigner_perturbation.md` | Day 2 primary deliverable | Cat B candidate or Cat C SKETCH |
| `THEORY/working/MF/k_select_pf_obs_unified_view.md` | Day 2 Track A 신규 | Cat B SKETCH (P-K-Select-Unified) |
| `THEORY/working/MF/op0005_dyn_kramers_sketch.md` | Day 2 Track B secondary | Cat C SKETCH (W9+ staging) |
| `THEORY/working/MF/MF_atlas.md` v0.1 → v0.2 | Day 2 Track A 갱신 | n/a (working atlas) |

추가 code files:
| 파일 | 단계 |
|---|---|
| `CODE/experiments/exp91_ksoft_hard_recovery.py` | Track C 신규 |
| `CODE/tests/test_k_soft_recovery.py` | Track C 신규 (2 tests PASS) |

---

## Verification (Day 2 EOD)

```bash
cd /home/jack/Perception_theory/CODE

# Track C — 신규 test PASS
python3 -m pytest tests/test_k_soft_recovery.py -v
python3 experiments/exp91_ksoft_hard_recovery.py

# 기존 pytest regression check
python3 -m pytest tests/ -q   # 225 + 2 신규 + 1xf, 기존 225 변동 없음

# Track A — file existence
ls -la THEORY/working/MF/MF_atlas.md  # v0.2 (§3 + §4 full)
ls -la THEORY/working/MF/k_select_pf_obs_unified_view.md  # 신규

# Track B — file existence
ls -la THEORY/working/MF/op0008_merge_wigner_perturbation.md  # primary
ls -la THEORY/working/MF/op0005_dyn_kramers_sketch.md  # secondary

# canonical untouched
git status THEORY/canonical/   # 0 changes

# scc/ untouched
git status CODE/scc/   # 0 changes

# daily log 7+ files
ls THEORY/logs/daily/2026-05-19/
```

---

## 다음 (Day 3 Wed 2026-05-20) 입력 준비

Day 2 EOD 의 산출이 Day 3 의 *직접 입력*:

- `op0008_merge_wigner_perturbation.md` (Day 2 primary) → `op0008_merge_wigner_rmt.md` (Day 3 PRIMARY, RMT Wigner-Dyson + 2-approach 수렴 audit)
- `op0008_merge_wigner_perturbation.md` (Day 2 primary) → exp92 (Day 3 8×8 + 12×12 toy numerical cross-check) 의 *initial config*
- MF_atlas.md v0.2 (Day 2) → §5 σ-inheritance 6 parts full (~200 lines, Day 3 가장 두꺼움)
- exp91 + test_k_soft_recovery (Day 2 Track C) → exp92 의 *Track C 입력* (numerical pipeline 안정 확인)

---

*5/19 의 first principle: deep-attack day. Track B PRIMARY 의 *substantive lemma 도출* 이 single most important deliverable. canonical 0 edits. v3 의 first real-world use — over-engineering 위험 인지 + adaptive enforcement.*
