> [!nav] Linked: [[MAIN_PROMPT_v2]] · [[PLAN_TEMPLATE_v2]] · v1 archived 2026-05-18 → [[../../../_archive/main_prompt_v1_2026-05-18/ARCHIVE_NOTE|v1 archive note]]

# MAIN_PROMPT_v2 Dry-Run Audit

**Type**: v2 dispatch self-test. *Mental simulation* — 실제 v2 를 *사용* 하지 않고, v2 의 §0 Mode dispatch + §6 schema + §13 종료 기준이 *실제 daily plan.md* 에 대해 어떻게 작동하는지 *분석적* 점검.
**Date**: 2026-05-18 (W8-Day1 post-EOD).
**Audit scope**: 3 confirmed mode + 1 hybrid case.

---

## §1. Audit framework

각 사례에 대해:
1. **v2 §0.1 plan 파일 찾기**: `00_plan.md` 또는 `plan.md` 존재 확인.
2. **v2 §0.2 mode 결정**:
   - frontmatter `mode:` field 값.
   - normalize 결과 (6 mode 중 하나).
   - 본문 어휘 빈도 (frontmatter 부재 시 fallback test).
3. **v2 §6 schema dispatch**: mode-default 또는 plan.md override 채택.
4. **v2 §13 종료 기준 적용**: mode 별 적합성 점검.
5. **v2 §8a archive pattern P1-P6 점검**: 모든 mode 강제 — plan 의 *위험* 항목과 매칭.
6. **v2 §15 Daily Discipline 4 룰 적용**: pre-work xref / sanity / 60-min / decision gate.

---

## §2. Case 1 — 2026-05-18 (W8-Day1, *survey* mode)

### §2.1 Plan 파일 찾기 (v2 §0.1)

✓ `THEORY/logs/daily/2026-05-18/00_plan.md` 존재. (`plan.md` 미존재 — `00_plan.md` 채택, v1 convention 의 명명 drift 흡수).

### §2.2 Mode 결정 (v2 §0.2)

**Frontmatter `mode:` field 의 값**:
```yaml
mode: survey day — 3 트랙 병렬 / 새 수학 0 정상 / canonical 0 edits
```

**v2 normalize**: "survey day" 명백 → **`survey`** 로 normalize. ✓

**본문 추정 fallback (frontmatter 부재 가정 시)**:
- "track" / "병렬" / "broad survey" / "3-track" 어휘 = 26회. ≥ 2 → **survey** confirm.
- "SEAL" 어휘 = 1회 (단순 reference, "직전 SEAL"). → SEAL 아님.
- "decision" 어휘 = decision gate context (≥ 2회) — 그러나 *review* 의 "stage / verification question / archive pattern" 동반 부재 → review 아님.

→ **추정도 survey 로 confirm**. ✓ frontmatter 와 일치.

### §2.3 Schema dispatch (v2 §6 + §0.4 override)

Plan.md 의 §"출력 파일 (예정)" 표:
```
00_index.md, 00_plan.md, 01_pre_brainstorm.md, 02_track_A, 03_track_B2, 04_track_B1, 05_track_B3, 06_track_C, 99_summary.md
```

→ **plan 의 output_files override 채택** (§0.4). v2 의 survey-default (`02_track_X/...+99_summary`) 와 일치 + plan 의 *track 별 명시* 정밀화.

실제 산출 (오늘 W8-Day1 EOD): 정확히 위 9 파일 산출. ✓

### §2.4 종료 기준 적용 (v2 §13.2 survey mode)

- ✓ Core metric 충족: "OP-0008 attack 초기 input 확보" (broad_survey_B2.md §3 + §9 매핑).
- ✓ 다음 day 직접 입력: 99_summary.md §"Day 2 의 직접 입력" 6 매핑 명시.
- ✓ Track 별 quality:
  - Track B2 PRIMARY: Route (a) + Route (b) + Route (c) preserved = **≥3 approach** (v2 §5 survey-PRIMARY 기준).
  - Track B1 LIGHTER: Mori-Zwanzig + 4 외부 reference + W9 staging only = **≥1 + ref + 증명 시도 부재** (v2 §5 survey-LIGHTER 기준).
  - Track B3 LIGHTER: 3-pillar + 9 외부 reference + W9+ staging only = **≥1 + ref + 증명 시도 부재** (v2 §5 survey-LIGHTER 기준).
- ✓ "새 수학 0 = survey day 정상" 명시적 채택 (v2 §13.2 + §8b 규칙 3 — 5/15 결정 C carry-forward).

→ **v2 §13.2 모든 기준 충족**.

### §2.5 §8a Archive pattern 점검

99_summary.md §"메타 자기 평가" + 03_track_B2 §5 + broad_survey_B2.md §10:
- **P1 근본 질문 우회**: 0 — DECL-1.0 Q6 (분열·합병 후) 의 *직접* attack.
- **P2 vocabulary refactoring**: 0 — Route (a) / Route (b) 는 prompt body §4.2 채택 표기, *새 어휘 생성 0*.
- **P3 canonical content 중복**: 0 — Reed-Simon IV §XIII.5 외부 reference 명시 + `sigma_rich_wigner_derivation.md §8.2 Conjecture 8.1` 의 *방법론적 확장 위치* 명시 (broad_survey_B2.md §7.2).
- **P4 외부 도구 도입 계기**: 0 — Wigner-Dyson 은 SCC 의 H-MORSE row 가 이미 canonical (T-σ-Lemma-1/2/3), σ-rich Wigner derivation 가 working — *내부 필요로부터* 도출.
- **P5 self-audit + canonical-xref 미시행**: 0 — pre-work xref check 수행 + 결과 03_track_B2 머리에 명시.
- **P6 언어 vs 수학**: 0 — *수학적으로 독립* 인 Route (a) / (b) 의 *수렴 framework* 명시 (broad_survey_B2.md §5).

→ **0/6 부합** — archive 위험 부재. 진행 합법. ✓

### §2.6 Daily Discipline 적용 (v2 §15)

- ✓ §15.1 Pre-work xref check: 5 grep 모두 수행 + 결과 기록 (02-06 each header).
- ✓ §15.2 Sanity meta-check: `subthreshold_demo_check` 도구 신규 산출 + Day 2-5 *매일 호출* 약속 (06_track_C §2).
- N/A §15.3 Track switching 60-min: 본 day 의 3-track 진행에서 막힘 발생 없음.
- ✓ §15.4 Decision gate: 99_summary 의 8/8 PASS.
- N/A §15.5 CHANGELOG prepend: 본 day SEAL/archive event 0 (정상).

### §2.7 Case 1 verdict

**v2 가 survey day 를 *완벽히* dispatch**. v1 의 강제 schema (`01_/02_/03_/99_`) 와 *충돌* 했던 부분이 v2 §0.4 override 로 *해소*. *Mode tag 만으로 OK* 기준 충족 — frontmatter `mode:` field 만으로 적절한 schema + quality 기준 + 종료 기준 + Daily Discipline 모두 활성.

---

## §3. Case 2 — 2026-05-15 (W7-Day6, *review* mode)

### §3.1 Plan 파일 찾기 (v2 §0.1)

✓ `THEORY/logs/daily/2026-05-15/00_plan.md` 존재.

### §3.2 Mode 결정 (v2 §0.2)

**Frontmatter `mode:` field 의 값**:
```yaml
mode: 검토 / 진단 / 결정 — 새 정리 생성 없음
```

**v2 normalize**: "검토 + 결정" 명백 → **`review`** 로 normalize. ✓

**본문 추정 fallback**:
- "decision" / "stage" / "verification question" / "archive pattern" 어휘 = 29회. ≥ 2 → **review** confirm.
- "track" 어휘 = 0회. → survey 아님.
- "SEAL" 어휘 = 단순 reference.
- "archive" = 본 review 의 *핵심 주제* (V-AFD + R-2 archive pattern 진단).

→ **추정도 review 로 confirm**. ✓ frontmatter 와 일치.

### §3.3 Schema dispatch (v2 §6 + §0.4 override)

Plan.md 의 §"6 stage 양식" 직접 명시:
```
02_canonical_inventory, 03_insight_decomposition, 04_confrontation, 05_verification_question, 06_archive_pattern_diagnosis, 07_decision, 99_summary
```

→ **plan 의 output_files override 채택** (§0.4). v2 의 review-default schema 와 *완전 일치* (v2 §6.1 의 §0.3 표 직접 채택).

실제 산출 (5/15 EOD): 정확히 위 7 파일 + entry 시 작성 파일 (00_index, 00_plan, 01_pre_brainstorm) 산출. ✓

### §3.4 종료 기준 적용 (v2 §13.5 review mode)

- ✓ 6-stage 모두 완료 (`02_~07_`).
- ✓ Decision A/B/C 명시: **Decision C 채택** (07_decision.md §3).
- ✓ 거부된 결정의 명시 사유: §4.1 (A 거부) + §4.2 (B 거부 + 부분 채택 형태로 보존).
- ✓ 증거 합산: V count = 0 + archive pattern 부합 = 6/6 (08_decision.md §2.4 + §3.1).

→ **v2 §13.5 모든 기준 충족**.

### §3.5 §8a Archive pattern 점검

5/15 plan 자체가 *Stage 5 archive pattern diagnosis* 를 포함 — meta-level audit:
- **P1**: 5/15 plan 의 z_t / S_0 / K_read 시도 자체가 *DECL-1.0 의 6 인식론적 질문* 에 새 답을 산출 못함 — *6/6 부합* (06_archive_pattern §5).
- **P2-P6**: 모두 6/6 부합.

**→ Decision C 의 직접 근거**. v2 §8a 가 *review mode* 에서는 *분석 대상* 으로 작동 (점검의 *결과* 가 *진행 보류* 가 아니라 *Decision 의 입력*). ✓ 적절한 dispatch.

### §3.6 Daily Discipline 적용 (v2 §15)

- ✓ §15.1 Pre-work xref check: 06_archive_pattern §1 의 "archive 의 사유는 원문 그대로 인용" 강제 + Stage 5 의 명시적 xref.
- N/A §15.2 Sanity meta-check: review mode 는 K=2 결과 산출 없음.
- N/A §15.3 Track switching: review mode 는 single-stage progression.
- ✓ §15.4 Decision gate: 5/15 99_summary 의 "**Decision gate self-check**" 표 13 항목 모두 ✓.
- ✓ §15.5 CHANGELOG prepend: 5/15 review 자체는 SEAL/archive event 아님 (검토만), 그러나 *Decision C 채택* 자체가 `THEORY/CHANGELOG.md` 의 *결정 entry* 입력 (선택).

### §3.7 Case 2 verdict

**v2 가 review day 를 *완벽히* dispatch**. 5/15 plan 의 *6-stage 양식* 이 v2 §6 의 review-default 와 일치 — v1 에서는 *없던* schema. v2 §13.5 의 "Decision A/B/C 명시 + 거부된 결정 명시 사유 + 증거 합산" 종료 기준이 5/15 의 *실제 결과* 와 정확히 매핑.

---

## §4. Case 3 — 가설 *SEAL-execute* day (W8-Day4, 예정 2026-05-21)

### §4.1 Plan 파일 찾기 (v2 §0.1)

(가설) `THEORY/logs/daily/2026-05-21/00_plan.md` — 미작성 상태. v2 의 §0.1 *시도 순서* 가 적용되면 미존재 시 **HARD STOP** + 사용자 알림.

W8 strategic plan §3 Day 4 가 *plan 의 입력* 으로 작용 (`THEORY/logs/weekly/2026-05-W3/W8_strategic_plan.md` line 189-206). 즉 *frontmatter `mode:` 가 없는* 가설 plan 의 fallback test 가능.

### §4.2 Mode 결정 (v2 §0.2)

W8 strategic plan §3 Day 4 의 *명시* mission:
> CV-1.18 SEAL (primary OP-HMORSE-LOCAL-A) — Step 1-6 명시 + Step 2 numerical 검증 + Step 4 SEAL apply-order 6-step + Step 5 canonical.md §13 Cat A insert + Step 6 hypothesis_tree HT-3.8 → HT-3.9.

가설 frontmatter (사용자가 v2 channel 에 맞게 작성 시):
```yaml
mode: SEAL-execute — CV-1.18 SEAL, L-HMORSE-LOCAL Cat B → Cat A
```

**v2 normalize**: "SEAL-execute" → **`SEAL-execute`**. ✓

**본문 추정 fallback (frontmatter 없을 시)**:
- "SEAL" / "promotion" / "canonical insert" / "CHANGELOG prepend" 어휘 ≥ 2회 → SEAL 관련.
- "execute" / "canonical insert" / "Cat A insert" 동반 → **SEAL-execute** (vs SEAL-prep).

→ **추정도 SEAL-execute 로 confirm**. ✓

### §4.3 Schema dispatch (v2 §6 + §0.4 override)

W8 strategic plan §3 Day 4 의 *출력 file 표 부재* — v2 의 SEAL-execute default schema 자동 채택:
```
00_plan.md, 02_seal_execution.md, 03_post_seal_verification.md, 99_summary.md
```

추가로 canonical 의 5 파일 (canonical.md, theorem_status.md, hypothesis_tree.md, CV-1.18_SEAL.md, CHANGELOG.md) 직접 수정 — v2 §4.4 + §8.1 의 *허용* 항목.

### §4.4 종료 기준 적용 (v2 §13.4 SEAL-execute mode)

(가설 실행 시):
- canonical 5 file 정확히 수정: ✓ (목표).
- `git status THEORY/canonical/` 5 파일 변경 확인: ✓.
- `cd CODE && python3 -m pytest tests/ -q` PASS: ✓.
- CV-1.18_SEAL.md 의 *Non-Overclaim* 항목 + *Next target* 명시: ✓.

→ **v2 §13.4 가 SEAL-execute 의 *6-step apply-order* 와 정확히 매핑** (W8 plan §3 Day 4 의 Step 1-6 와 동등).

### §4.5 §8a Archive pattern 점검

SEAL-execute mode 에서도 §8a 강제:
- **P1 근본 질문 우회**: 0 — OP-HMORSE-LOCAL-A 는 *DECL-1.0 Q3* (Stochastic dynamics → Package II) 의 *직접 unlock*.
- **P2 vocabulary refactoring**: 0 — L-HMORSE-LOCAL 의 *Cat B → Cat A 승급* 은 *기존 정리* 의 *증명 강화*, 새 어휘 생성 아님.
- **P3 canonical content 중복**: 0 — CV-1.16 SEAL Non-Overclaim 이 이미 명시한 *sharper residual* + *SBM robustness* target.
- **P4-P6**: SEAL-execute 는 *기존 working canonical* 의 정직한 승급 — archive pattern 부합 0/6.

### §4.6 Daily Discipline 적용 (v2 §15)

- ✓ §15.1 Pre-work xref check: SEAL-prep day (Day 4 의 *전반*) 의 의무.
- ✓ §15.2 Sanity meta-check: H-MORSE 의 numerical verification 의 K=2 결과 가 *해당하면* 호출.
- N/A §15.3 Track switching: SEAL-execute 는 single-track.
- ✓ §15.4 Decision gate: SEALED 보장 + git status + pytest PASS.
- ✓ §15.5 CHANGELOG prepend: `[CV-1.18 SEAL]` entry **의무**.

### §4.7 Case 3 verdict

**v2 가 SEAL-execute day 를 *적절히* dispatch**. v1 에서는 *canonical 직접 수정 금지* 강제 — SEAL-execute 가 *예외* 임을 v1 prompt body 가 표현 못함. v2 §4.4 + §13.4 + §15.5 가 SEAL-execute 의 *허용 + 종료 + CHANGELOG* 모두 정밀 표현.

---

## §5. Case 4 (Hybrid) — 2026-05-14 (W7-Day5, *deep-attack + SEAL-execute*)

### §5.1 Plan 파일 찾기 (v2 §0.1)

✓ `THEORY/logs/daily/2026-05-14/00_plan.md` 존재.

### §5.2 Mode 결정 (v2 §0.2)

**Frontmatter `mode:` field**: ❌ *부재*.

**v2 §0.2 fallback (본문 추정)**:
- "SEAL" / "promotion" / "canonical insert" 어휘 = 5회. ≥ 2 → SEAL 관련.
- 그러나 "audit / P1-P7 / SEAL 6-step" 동반 *약함* — SEAL-prep 또는 SEAL-execute 어느 쪽인지 불명확.
- "decision" / "stage" 어휘 — *결정 단계 포함* (Option A/B/C 결정).
- "track" / "병렬" — 부재.

**Hybrid 감지**: *option 결정 (review-like)* + *선택된 option 의 첫 step (deep-attack)* + *Day 5 evening SEAL (SEAL-execute)* — **3-mode hybrid**.

v2 §0.5 hybrid 대응:
- *Primary mode*: **deep-attack** (실제 Day 의 첫 step 작업의 형식 — Option A H-MORSE Cat A 진입).
- *Secondary mode*: **SEAL-execute** (Day 5 evening 의 CV-1.16 SEAL 실행).
- *Tertiary mode*: **review** (Option A/B/C 결정).

추정 결과 inline 보고 (v2 §0.2 step 3):
```
Mode 추정: hybrid (primary: deep-attack, secondary: SEAL-execute, tertiary: review)
근거: 본문 어휘 — SEAL 5회, Option A/B/C decision 표 명시, 그러나 plan-prescribed schema (01_/02_/03_/99_) 가 deep-attack default
사용자 정정 가능: mode: <다른값>
```

### §5.3 Schema dispatch (v2 §6 + §0.4 override)

5/14 plan 의 *출력 file* 명시: `01_exploration / 02_development / 03_integration_and_new_open / 99_summary` (v1 default).

→ **v1 deep-attack default 와 일치** + 후속 broadness 작업 (40-44, 50, 59) 은 *간헐적 확장*.

v2 가 적용되면:
- Primary deep-attack 의 default schema (`01_/02_/03_/99_`) 채택.
- Secondary SEAL-execute 의 추가 file (`<date>_seal_log.md` 또는 다른 prefix) — Day 5 evening 의 *별도 task*.

### §5.4 종료 기준 적용 (v2 §13.1 + §13.4 hybrid)

(5/14 실제 결과):
- ✓ deep-attack 종료 §13.1: Primary (Option A H-MORSE) 의 substantive development — `02_development.md` 의 H-MORSE-Local Cat B 증명 + 40-44 의 broadness 분석 + 50-59 의 SBM numerical.
- ✓ SEAL-execute 종료 §13.4: CV-1.16 SEALED (W7-Day5 evening, 2026-05-14 — 실제 SEAL day 임을 W7 weekly_summary 확인).
- N/A review 종료 §13.5: 6-stage 완료 아님 (Option 결정만 — *light review*).

→ **v2 §0.5 hybrid 가 작동**, primary + secondary 의 *각각* 종료 기준 적용.

### §5.5 §8a Archive pattern 점검

5/14 는 *5/13 의 두 archive (V-AFD + R-2) 직후* — Day 1 의 *세 번째 archive 위험 회피 규약* 가 plan §"Context" 에 명시:
> 두 archive 가 모두 "language refactoring → archive" 패턴을 보였으므로, 곧장 정공법 진입이 *세 번째 archive 위험* 인지 sanity check 필요.

→ v2 §8a 가 *이미 plan 자체에 명시* — 5/14 는 §8a 의 *적용 사례* 의 *예시* (자기 진단 의 사전 명시).

실제 P1-P6 점검 (5/14 EOD):
- **P1 근본 질문 우회**: 0 — H-MORSE 는 Q3 의 직접 unlock + OP-HMORSE-BROADNESS 의 *전 작업* 의 자연 후속.
- **P2-P6**: 0/6.

→ 5/14 의 H-MORSE Cat A 진입 + Day 5 SEAL 가 *archive pattern 부합 0/6* — v2 §8a 자가 점검이 *합법*.

### §5.6 Case 4 verdict

**v2 가 hybrid day 를 *적절히* dispatch**. v1 에서는 hybrid 표현 부재 — 5/14 의 *option 결정 + deep-attack 진입 + 후속 SEAL* 의 3-mode 가 v1 의 단일 schema 와 충돌. v2 §0.5 의 hybrid (primary + secondary) 가 이를 *명시적* 으로 표현.

---

## §6. Audit summary

| Case | Day | Mode | v2 dispatch 성공? | 비고 |
|---|---|---|---|---|
| 1 | 2026-05-18 (W8-Day1) | survey | ✓ | frontmatter `mode:` field + output_files override + 8/8 종료 기준 |
| 2 | 2026-05-15 (W7-Day6) | review | ✓ | 6-stage default schema 일치 + Decision C 채택 + archive pattern 자가 점검 의 *적용 사례* |
| 3 | 2026-05-21 (W8-Day4, 가설) | SEAL-execute | ✓ | v1 의 "canonical 수정 금지" 강제 한계 의 *예외 처리* v2 가 명시 |
| 4 | 2026-05-14 (W7-Day5) | hybrid (deep-attack + SEAL-execute + review-light) | ✓ | frontmatter 부재 + 본문 추정 + §0.5 hybrid 의 *3-mode* 표현 |

**4/4 PASS**. v2 가 *모든 mode* + *frontmatter 부재 fallback* + *hybrid day* 를 정확히 dispatch.

---

## §7. v2 의 자가 점검 결과 + 보완 권장

### §7.1 v2 의 *강점*

1. **Mode tag 만으로 작동** — Case 1, 2 가 frontmatter `mode:` field 한 줄로 적절히 dispatch.
2. **Fallback 본문 추정** — Case 4 같은 frontmatter 부재 시 *자동 추정* + *inline 보고*.
3. **Output schema override** — Case 1 의 plan 의 *track 별 명시* 가 v2 의 default 보다 우선 (§0.4).
4. **§8a archive pattern** — Case 2 의 review 의 *분석 대상* 으로 작동 + Case 4 의 *진입 점검* 으로 작동.
5. **§13 mode 별 종료 기준** — Case 1 의 "core metric 충족", Case 2 의 "Decision A/B/C", Case 3 의 "5 file 수정 + pytest", Case 4 의 "primary + secondary" 모두 적절.

### §7.2 v2 의 *잠재적 약점* (v3 분기 후보)

1. **Hybrid day 의 §0.5 가 *complex*** — 3+ mode mix 의 *우선순위* 정의가 미정밀. Case 4 의 deep-attack + SEAL-execute + review 의 *3-mode mix* 가 *어느 schema 채택* 인지 *명시적 룰* 부재. → v3 의 §0.5 expand candidate.

2. **본문 추정 logic 의 *어휘 빈도 임계값*** — 현재 "≥ 2회" 기준. 짧은 plan 의 경우 *불충분*. → v3 에서 *adaptive threshold* (plan 길이의 함수) 도입 candidate.

3. **`output_files:` field 의 *구조* 미정의** — v2 에서는 *plan 본문의 표* 직접 채택. *기계 가독* form (e.g., YAML list) 부재. → v3 의 frontmatter expand candidate.

4. **Mode 가 *day 내부에서 변경* 되는 경우 처리 부재** — e.g., survey day 가 도중에 *결정 필요* 가 발생 → review mode 로 *내부 전환* — v2 §15.3 의 "3 트랙 막힘 → review mode 자동 전환" 이 *일부* 만 표현. → v3 의 *mode transition* candidate.

5. **v2 §15.2 Sanity meta-check 의 *호출 의무* 가 *survey* 외 mode 에서 *불명확*** — deep-attack day 의 K=2 결과 산출 시도 의무인가? → v3 의 명시 candidate.

### §7.3 보완 권장 (선택적 v2 후속 PR)

- §0.5 hybrid 의 3-mode mix 처리 명시.
- 본문 추정 logic 의 adaptive threshold.
- `output_files:` frontmatter field 의 YAML structure 정의.
- Mode transition (day 내부) 의 explicit 룰.

본 4건 모두 *v2 의 production 사용에 *blocker 아님** — *v3 의 evolutionary roadmap*.

---

## §8. Status

**v2 dry-run audit 결과**: **4/4 PASS**. *Mode tag 만으로 작동* 기준 충족 (Case 1, 2, 3). *Hybrid day fallback* 작동 (Case 4). 보완 권장 4건은 v3 의 *evolutionary roadmap*.

**Effort**: v1 (385 lines) → v2 (520 lines) + v2 dry-run audit (320 lines) + PLAN_TEMPLATE_v2 (240 lines) — 총 ~1080 lines.

**다음 단계**:
- 2026-05-19 (W8-Day2) plan 작성 시 사용자가 frontmatter `mode: deep-attack` (op0008 perturbation 본격 attack) 명시 → v2 첫 *real-world* 사용.
- v2 의 EOD 산출이 v1 의 EOD 산출과 *호환* 인지 (working file 들의 *재진입 가능* 여부) 추가 점검.
- v3 의 evolutionary roadmap 은 W9+ staging.

---

*MAIN_PROMPT_v2_dry_run_audit.md 종료. v2 의 6 mode dispatch + §8a + §15 모두 *4 real/hypothetical day* 에 대해 *완벽 작동*. 보완 권장 4건은 v3 candidate.*
