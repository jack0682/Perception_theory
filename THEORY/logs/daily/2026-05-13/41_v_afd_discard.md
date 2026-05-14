---
type: log/daily
date: 2026-05-13
session_label: V-AFD discard + archive
canonical_version: CV-1.13 (untouched)
afd_version: AFD-0 v0.1 (untouched)
v_afd_version: ARCHIVED — discontinued
files_moved: 19 (THEORY/working/AFD_0/V_AFD/* → _archive/v_afd_2026-05-12/)
files_created: 3 (this log + ARCHIVE_NOTE.md + CHANGELOG.md prepend)
canonical_edits: 0
afd_0_edits: 0
---

# 41 — V-AFD 폐기 및 archive 결정

## 1. 결정

사용자 지시에 따라 **V-AFD 전체를 archive로 폐기**했다. archive 위치: `_archive/v_afd_2026-05-12/`. 원래 위치 `THEORY/working/AFD_0/V_AFD/` 디렉터리는 제거되었고, AFD-0 부모 디렉터리는 그대로 보존되었다.

19개 파일, ~8000 줄, ~430 KB 가 archive로 이동되었다. 19개 파일에는 다음을 포함한다:

| 카테고리 | 파일 수 | 내용 |
|---|---|---|
| R1 베이스라인 | 7 | README, main spec, registry, OPs, examples, audit, handoff |
| R2–R12 심화 라운드 | 11 | T13..T47 + 외부 framework bridge |
| 사후 audit | 1 | v_afd_previous_agent_audit.md (2026-05-13 작성) |

## 2. 폐기 이유

DECLARATION.md (DECL-1.0, 2026-05-07) 재독 후, V-AFD가 SCC의 근본 질문에 답하지 않음이 확인되었다.

근본 질문: **"어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?"**

V-AFD가 실제로 다룬 것: **이미 형성된 formation들의 vector projection 사이의 transition.**

V-AFD가 도입된 계기는 *내부적 필요*가 아니라 두 단계의 회피였다:

1. **회피 1 (2026-05-12 D1):** CV-1.14 Package II (정확한 EK rate)이 너무 무거워서 → AFD-0 로 후퇴 (H-MORSE 회피).
2. **회피 2 (2026-05-12 D3, 같은 날 저녁):** AFD-0 자체에는 새로운 수학 없음. GPT-5 메타-연구 보고서의 외부 추천에 따라 → V-AFD 로 reformulation.

V-AFD의 중심 결과 V-AFD-T9 (Information Loss Theorem)은 자기 자신의 projection이 비-단사임을 증명한다. 이는 *결과*이지 근본 질문의 *답*이 아니다.

세부 분석은 `_archive/v_afd_2026-05-12/ARCHIVE_NOTE.md` 와 동일 폴더 내 `v_afd_previous_agent_audit.md` 를 참조.

## 3. 영향 범위 (clean boundary)

- `canonical.md`: 영향 없음. V-AFD는 canonical을 수정한 적 없음.
- `theorem_status.md`: 영향 없음. V-AFD 정리는 canonical 카탈로그에 등재된 적 없음.
- `hypothesis_tree.md`: 영향 없음. V-AFD는 HT-3.5 에 등재된 적 없음.
- `AFD-0` (부모): 영향 없음. V-AFD는 AFD-0 파일을 한 줄도 수정한 적 없다. AFD-0 자체는 working-layer로 그대로 유지.
- 다른 working 폴더 (`CV114_*`, `CV115_*`, `temporal/`, etc.): 영향 없음. V-AFD를 참조하는 외부 파일 0건.

폐기는 **clean** 하다. 의존성 그래프 단절이 없다.

## 4. 잃은 것 / 잃지 않은 것

### 잃은 것 (의도적)

- V-AFD-D1..D17 (17개 정의)
- V-AFD-T1..T47 (~47개 정리/명제/추측)
- OP-VAFD-001..026 (~26개 OP — 의존성 없으므로 모두 폐기)
- 외부 framework bridges (T41 ML, T42 Bayesian, T43 FEP, T44 neuroscience, T46 Weinhold, T47 symbolic)
- V-AFD-T2 Pareto preorder의 vector 언어 (필요 시 archive에서 재추출 가능)
- V-AFD-T7 H-MORSE-free 진술의 vector 언어 (AFD-T9 의 재진술이므로 잉여)

### 잃지 않은 것

- 근본 질문 자체 — DECLARATION에 그대로 남음.
- T8, T14, T-Merge(b), T-Persist-1(b), T7-Enhanced, Predicate-Energy Bridge, T-Temporal-Identity 등 Cat A 결과 — V-AFD 폐기와 무관.
- AFD-0 의 H-MORSE 분리 architecture — `afd_hmorse_reclassification.md` 와 AFD-T9 가 그대로 보유.
- diagnostic vector (Bind, Sep, Inside, Persist) 자체 — canonical §7.2 에 Cat A 로 존재.

## 5. 다음 방향 (V-AFD 회피가 아니라 정면 대결)

DECLARATION 의 미답 부분으로 직진:

| 옵션 | 대상 | 근거 |
|---|---|---|
| **A** | **OP-0005 (Q4 K-selection)** — T-K-Select-PF / OBS 일치성 또는 반례 | Q4 가 6개 인식론적 질문 중 가장 뾰족한 미해결 (Cat B) |
| **B** | **OP-0008 (Q6 σ-inheritance, HIGH severity)** — K-jump 비결정성 | DECLARATION 이 Q6 를 "진행 중" 으로 표시한 자리 |
| **C** | **λ₂-collapse 비대칭** — T8 의 역방향 형식화 | "멀리 있는 두 사과가 하나로 보이는" 메커니즘. DECLARATION 의 사과 비유의 수학화 |

V-AFD R10–R12 가 시도했던 외부 framework bridge 방향(범주론, FEP, 신경과학, 열역학 기하)은 모두 **추구하지 않음**.

## 6. 파일 변경

| 파일 | 동작 |
|---|---|
| `THEORY/working/AFD_0/V_AFD/` | **REMOVED** (디렉터리) |
| `_archive/v_afd_2026-05-12/` | **CREATED** (19 archived files + ARCHIVE_NOTE.md) |
| `_archive/v_afd_2026-05-12/ARCHIVE_NOTE.md` | **CREATED** (이 폐기의 archive-side note) |
| `THEORY/logs/daily/2026-05-13/41_v_afd_discard.md` | **CREATED** (이 파일) |
| `THEORY/CHANGELOG.md` | **PREPENDED** (V-AFD discard entry, 최상단) |

## 7. 슬로건

> 정보를 줄이면 반드시 뭔가를 잃는다.
> V-AFD 는 그 손실을 정직하게 정리했지만 (T9), 그 손실을 근본 질문에 비추어 정당화하지 못했다.
> 근본으로 돌아간다 — Q4, Q6, 또는 λ₂-붕괴 비대칭.

---

*End of `41_v_afd_discard.md`. V-AFD branch closed by author decision. Archive frozen.*
