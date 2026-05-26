> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]] · [[MAIN_PROMPT_v2]] · v1 archived 2026-05-18 → [[../../../_archive/main_prompt_v1_2026-05-18/ARCHIVE_NOTE|v1 archive note]]

# Plan Template v2 — 매일 저녁 작성 (Mode-Adaptive)

> **사용법:** 전날 저녁 다음날 날짜의 디렉토리 (`THEORY/logs/daily/YYYY-MM-DD/`) 를 미리 생성하고, 이 템플릿을 `00_plan.md` 로 복사한 뒤 각 섹션을 채워 넣는다. 빈 섹션은 "없음" 또는 "N/A" 로 명시.
>
> **v1 와의 차이**: frontmatter 에 `mode:` field 추가. 이 field 하나만 정확히 입력해도 `MAIN_PROMPT_v2.md` 가 적절한 schema + quality 기준 + 종료 기준을 자동 dispatch. 본 template 은 6 mode 별 권장 section 을 모두 포함하지만, 실제 plan 작성 시 *해당 mode 의 권장 section 만* 채우면 됨.

---

## Frontmatter (모든 mode 공통, 의무)

```yaml
---
type: log/daily/plan
date: YYYY-MM-DD
session_label: <e.g., W{n}-Day{m} ({요일}) — <한 줄 mission>>
mode: <deep-attack | survey | SEAL-prep | SEAL-execute | review | hygiene>
canonical_version: CV-1.X (sealed YYYY-MM-DD, untouched 또는 to be sealed)
predecessor: <전 영업일의 99_summary.md 또는 결정 entry>
strategic_plan: <THEORY/logs/weekly/YYYY-MM-W{n}/W{n}_strategic_plan.md (있다면)>
output_files: <명시 시 MAIN_PROMPT_v2 의 default schema override; 미지정 시 mode-default 사용>
---
```

### Mode 결정 가이드

| Mode | 사용 시점 |
|---|---|
| **deep-attack** | 단일 OP / target 에 1 일 deep development. 가장 흔한 default. |
| **survey** | 2+ track 병렬 (예: Atlas + broad survey + sanity), 또는 입력 확보 day. 새 수학 산출 기대 < 50%. |
| **SEAL-prep** | CV-1.X SEAL 직전. P-Audit P1-P7 + 6-step ready 점검. canonical 미수정. |
| **SEAL-execute** | canonical 직접 수정 1회 허용. CV-1.X SEAL 실행 day. 1 주 0-1 회 정도 빈도. |
| **review** | 사용자 통찰 / 새 방향의 6-stage 검토 + Decision A/B/C. 평균 1-2 주 1 회. |
| **hygiene** | archive 분류 / dual-naming 해소 / merger / cleanup. 평균 2-4 주 1 회. |

---

## §1. Target / Mission

<mode 별 형식>:

- **deep-attack**: 단일 open problem 또는 focused subtopic. 한 문장 또는 짧은 문단.
  > 예: "N-1 (Soft-Hard Switching Asymmetry) 의 K 층위에서, K 를 H_0 persistence bar length 가중합으로 soft 화하는 접근이 E(u*_M) vs E(u*_{M/K}) 비교를 어떻게 바꾸는지 검토."

- **survey**: track 수 + 각 track 의 mission.
  > 예: "Track A Atlas skeleton + Track B broad survey 3-parallel (B2 PRIMARY OP-0008 + B1 LIGHTER OP-0021 + B3 LIGHTER OP-0005-DYN) + Track C sanity infra."

- **SEAL-prep**: SEAL target + P-Audit 범위.
  > 예: "CV-1.18 SEAL prep — OP-HMORSE-LOCAL-A Cat B → Cat A 승급. Sub-task A sharper residual + Sub-task B SBM robustness."

- **SEAL-execute**: SEAL target + 수정될 canonical file list.
  > 예: "CV-1.18 SEAL execute — L-HMORSE-LOCAL Cat A insert (canonical.md §13, theorem_status.md, hypothesis_tree.md HT-3.8 → HT-3.9, CV-1.18_SEAL.md, CHANGELOG.md)."

- **review**: 검토할 통찰 / 방향 + 6-stage 의 *결정 질문*.
  > 예: "사용자 통찰 ($u^* \to S_0 \to K_{\mathrm{read}}$) 의 6-stage 검토 — Decision A/B/C: '통찰에서 canonical CV-1.X 에 없는 구체 수학 명제가 따라나오는가?'"

- **hygiene**: 작업 list (3-7 항목).
  > 예: "1) OP-0021 dual-naming reconciliation, 2) archive 5/12 V-AFD audit, 3) working/MF/ 중복 파일 4건 merger."

---

## §2. Why now

<오늘 이 작업을 선택한 이유. 1-3 문장. 어제 carry-forward 인지, 사용자 자기-진단인지, weekly plan 일정인지, 외부 자극인지.>

---

## §3. Context refs (에이전트가 반드시 읽어야 할 소재)

mode 별 권장 (deep-attack 외 mode 는 plan 의 target 에 맞게 조정):

- `THEORY/2_substrate/canonical/canonical.md` §X.Y — <관련 섹션>
- `THEORY/2_substrate/canonical/theorem_status.md` — <해당 OP-ID / P-ID / Cat 분류 row>
- `THEORY/2_substrate/canonical/hypothesis_tree.md` — <오늘 타겟하는 HT-node>
- `THEORY/0_axis/DECLARATION.md` — <deep-attack / review mode 의무>
- `THEORY/canonical/CV-1.X_SEAL.md` — <SEAL-prep / SEAL-execute mode 의 직전 SEAL 참조>
- `THEORY/working/<file>.md` — <plan 의 직접 ancestor working files>
- 어제 로그: `THEORY/logs/daily/YYYY-MM-DD/99_summary.md` — <carry-forward>
- 외부 자료: <필요시 PDF, 논문, 다른 프로젝트>

---

## §4. Current hypotheses / approaches under consideration

<mode 별 권장>:

- **deep-attack**: 자유 서술. 오늘 아침 시점의 직관, 의심, 대안. 에이전트가 이 안에서만 움직이는 것은 아님 — 출발점.
  - 가설 1: ...
  - 가설 2: ...
  - 반례 의심: ...

- **survey**: 각 track 의 *진입 점* + *외부 reference 추측*.
  - Track A: <input>
  - Track B2 PRIMARY: <approach (a) 후보, approach (b) 후보, 외부 reference>
  - Track B1 LIGHTER: <pointer>

- **SEAL-prep / SEAL-execute**: P-Audit P1-P7 의 *우선 audit 항목* + SEAL apply-order 6-step 의 *risk 항목*.

- **review**: 검토할 통찰의 *6-stage 별 잠정 결론* 또는 *예상 V count*.

- **hygiene**: 각 작업의 *예상 사유* + *복잡도 추정*.

---

## §5. Session goals

<구체적이고 검증 가능한 형태. mode 별 강제 정도가 다름>:

- **deep-attack**: 1-3개 권장 (너무 많으면 실패).
  1. ...
  2. ...

- **survey**: track 수만큼 + core metric 1개.
  1. Track A 산출: ...
  2. Track B2 산출: ...
  3. ...
  - **Core metric**: <예: "OP-0008 attack 초기 input 확보">

- **SEAL-prep**: P-Audit 7 항목 + 6-step ready + xref clear.

- **SEAL-execute**: SEALED 보장 + 5 file 수정 + pytest regression 0.

- **review**: 6-stage 모두 수행 + Decision A/B/C 명시.

- **hygiene**: 작업 list 100% 완료.

---

## §6. Non-goals (scope 제한, 모든 mode 강제)

<오늘 다루지 않을 것. 관련은 있으나 오늘은 밀어둘 것. 명시 안 하면 scope creep 발생.>

- canonical 직접 수정 금지 (SEAL-execute 제외)
- DECL-1.0 amend 시도 금지 (별도 plan 필요)
- `scc/` 모듈 수정 금지 (`experiments/` + `tests/` 만 신규, weekly plan 의 anti-goal 따름)
- V-AFD / R-2 / z_t 부활 시도 금지 (5/15 결정 C carry-forward)
- 새 framework letter (V-, R-, U-, $D_0^*$, ...) 도입 금지 (§8b 규칙 1)
- Engineering proxy (Gaussian similarity, bilateral filter, diffusion maps, mean-shift) 도입 금지
- <오늘 plan 의 *특수* non-goal>

---

## §7. Carry-forward (어제로부터)

<전 세션 99_summary 의 "다음 day 의 직접 입력" 표 직접 채택 또는 자유 서술. 없으면 "없음".>

- ...

---

## §8. Success criterion for today

<단일 문장. mode 별 형식>:

- **deep-attack**: "오늘 세션이 성공이라면 무엇을 얻고 있어야 하는가" — 단일 문장.
  > 예: "Primary approach 의 proof 또는 명시적 실패 분석 도달."

- **survey**: "오늘 의 core metric 충족 + 다음 day 의 직접 입력 준비".
  > 예: "OP-0008 attack 초기 input 확보 + Day 2 op0008_merge_wigner_perturbation.md 의 직접 입력 가능."

- **SEAL-prep**: "P-Audit P1-P7 모두 PASS + SEAL 6-step ready + xref clear."

- **SEAL-execute**: "CV-1.X SEALED + canonical 5 file 수정 + pytest regression 0."

- **review**: "Decision A/B/C 명시 + 증거 합산 (V count + archive pattern 부합 정량)."

- **hygiene**: "작업 list 100% 완료 + ARCHIVE_NOTE/HYGIENE_LOG 작성 + canonical 무손상."

---

## §9. Decision gate (EOD, 모든 mode 강제, §15.4 of MAIN_PROMPT_v2)

99_summary.md 에 *명시* 점검 표:

| 검사 | mode 별 결과 기준 |
|---|---|
| canonical 0 edits | ✓ (SEAL-execute 제외) |
| 새 어휘 생성 0 | ✓ (§8b 규칙 1) |
| Mode 별 core metric 충족 | ✓ (§8 참조) |
| Pre-work xref check 수행 기록 | ✓ (§15.1) |
| §8a archive pattern P1-P6 자가 점검 | ✓ |
| Silent OP resolution 0 | ✓ |
| (mode 별 추가 검사 — 아래 표) | ... |

### Mode 별 추가 Decision gate 항목

- **deep-attack**: 4 core file (01_/02_/03_/99_) 존재. ≥3 approach 생성. Primary substantive development. 새 OQ 수집.
- **survey**: Track 수만큼의 보고 파일 + working file. PRIMARY ≥3 approach + LIGHTER ≥1+ref. Core metric 충족. 다음 day 직접 입력 매핑 명시.
- **SEAL-prep**: P-Audit P1-P7 모두 PASS. 6-step ready. `grep -r "<핵심정리이름>" THEORY/canonical/` clear.
- **SEAL-execute**: `git status THEORY/canonical/` 5 file. `pytest tests/ -q` PASS. CV-1.X_SEAL.md 신설 + Non-Overclaim + Next target.
- **review**: 6 stage file 존재. Decision A/B/C 명시. 거부된 결정의 명시 사유.
- **hygiene**: 작업 list 100%. ARCHIVE_NOTE/HYGIENE_LOG 작성. canonical/scc/ 무손상.

---

## §10. Output files (예정)

<mode 별 default schema 또는 plan-specific override>:

### deep-attack default

| 파일 | 단계 |
|---|---|
| `00_plan.md` | 본 file |
| `01_exploration.md` | Restatement + Multi-approach + Primary selection |
| `02_development.md` | Primary 심층 전개 |
| `03_integration_and_new_open.md` | Integration + New open questions |
| `99_summary.md` | EOD summary |

### survey default

| 파일 | 단계 |
|---|---|
| `00_plan.md` | 본 file |
| `01_pre_brainstorm.md` (선택) | 진입 점검 |
| `02_track_A_<topic>.md` | Track A 보고 |
| `03_track_B_<topic>.md` | Track B 보고 (PRIMARY 라면 가장 두꺼움) |
| `04_track_<...>.md` | 추가 track |
| `99_summary.md` | EOD summary |

### SEAL-prep default

| 파일 | 단계 |
|---|---|
| `00_plan.md` | 본 file |
| `02_audit.md` | P-Audit P1-P7 결과 |
| `03_seal_prep_steps.md` | 6-step ready 점검 |
| `99_summary.md` | EOD summary + 다음 day SEAL-execute 입력 |

### SEAL-execute default

| 파일 | 단계 |
|---|---|
| `00_plan.md` | 본 file |
| `02_seal_execution.md` | canonical 수정 5 file 의 wording 결정 + 실행 log |
| `03_post_seal_verification.md` | git status + pytest + CV-1.X_SEAL.md Non-Overclaim |
| `99_summary.md` | EOD summary |

### review default

| 파일 | 단계 |
|---|---|
| `00_plan.md` | 본 file |
| `02_inventory.md` | Stage 1 — canonical 담김 정량 |
| `03_decomposition.md` | Stage 2 — 통찰 N 명제 분해 |
| `04_confrontation.md` | Stage 3 — N × canonical 대조 |
| `05_verification_question.md` | Stage 4 — V count |
| `06_archive_pattern_diagnosis.md` | Stage 5 — P1-P6 부합 정량 |
| `07_decision.md` | Stage 6 — Decision A/B/C |
| `99_summary.md` | EOD summary |

### hygiene default

| 파일 | 단계 |
|---|---|
| `00_plan.md` | 본 file |
| `02_classification.md` | 작업 list 의 각 항목 분류 사유 |
| `03_cleanup_log.md` | 실제 cleanup 실행 log |
| `99_summary.md` | EOD summary + CHANGELOG entry |

---

## §11. Verification (mode 별)

EOD 의 verification 명령 — 99_summary 의 `## Verification` 섹션에서 결과 보고:

### 모든 mode 공통

```bash
cd /home/jack/Perception_theory

# canonical untouched (SEAL-execute 제외)
git status THEORY/canonical/

# scc/ untouched (weekly plan 의 anti-goal 따름)
git status CODE/scc/

# Pre-work xref check 기록 확인
grep "Pre-work xref check" THEORY/logs/daily/{DATE}/*.md
```

### Mode 별 추가 verification

- **deep-attack**:
  ```bash
  ls THEORY/logs/daily/{DATE}/01_*.md 02_*.md 03_*.md 99_summary.md
  ```

- **survey**:
  ```bash
  ls THEORY/logs/daily/{DATE}/02_track_*.md
  ls THEORY/working/MF/<신규 file들>.md
  cd CODE && python3 -m pytest tests/ -q  # regression 0
  ```

- **SEAL-prep**:
  ```bash
  grep "P-Audit P[1-7] PASS" THEORY/logs/daily/{DATE}/02_audit.md
  grep "step [1-6] ready" THEORY/logs/daily/{DATE}/03_seal_prep_steps.md
  ```

- **SEAL-execute**:
  ```bash
  git status THEORY/canonical/  # 5 file 변경 확인
  cd CODE && python3 -m pytest tests/ -q  # regression 0
  ls THEORY/canonical/CV-1.X_SEAL.md
  head -1 THEORY/CHANGELOG.md  # [CV-1.X SEAL] entry
  ```

- **review**:
  ```bash
  ls THEORY/logs/daily/{DATE}/0{2,3,4,5,6,7}_*.md  # 6 stage file
  grep "Decision [ABC]" THEORY/logs/daily/{DATE}/07_decision.md
  ```

- **hygiene**:
  ```bash
  ls _archive/<topic>_YYYY-MM-Wn/ARCHIVE_NOTE.md  # 또는 HYGIENE_LOG.md
  head -3 THEORY/CHANGELOG.md  # [ARCHIVE] 또는 [HYGIENE] entry
  ```

---

## §12. 다음 (Day {N+1}) 입력 준비

<오늘 EOD 의 산출이 다음 day 의 *직접 입력* 으로 어떻게 사용되는지 명시. 99_summary 의 *Day N+1 의 직접 입력* 표 와 일치해야.>

| Day {N+1} target | 본 day 의 입력 file |
|---|---|
| ... | ... |
| ... | ... |

---

## 메모

- 이 파일은 저녁에 작성되고 다음날 아침 에이전트에게 주어지는 **입력 문서**. 에이전트의 출력은 같은 디렉토리의 mode-default schema (§10) 또는 본 plan 의 `output_files:` override 에 따라 쌓인다.
- 에이전트가 받는 `MAIN_PROMPT_v2.md` 가 이 파일의 frontmatter `mode:` field 를 자동으로 dispatch.
- 저녁 작성은 자동화하지 않음 — 사용자 직접 판단.
- 본 template 의 모든 §-섹션을 채울 필요 없음. 해당 mode 의 권장 section 만 채우면 됨 (e.g., review mode 는 §10 의 review default schema 만 명시).

---

*PLAN_TEMPLATE_v2.md 종료. 6 mode 별 권장 section 모두 포함. 실제 사용 시 해당 mode 의 항목만 채우면 됨. v1 (69 lines) → v2 (~240 lines).*
