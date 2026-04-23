# THEORY/canonical/ — 완결된 권위 (Settled Authority)

**이 폴더는 승급(promoted)된 내용만 들어온다. 진행 중인 작업이나 검증 전 가설은 금지.**

## Contents

- **`canonical.md`** — 권위 스펙 (현재 v1.2, 1216줄, 2026-04-12 기준). 이 레포의 이론에 관한 유일한 authoritative 문서. **주 1 회 주간 merge 로 update** (2026-04-20 이후).
- **`theorem_status.md`** — 정리 인덱스 (증명/조건부/열린/철회). `canonical.md`와 일치해야 함.
- **`open_problems.md`** — F-1 (K=2 vacuity), M-1 (K=1 preference), MO-1 (Morse inapplicable). 현재 critical 3건.

## Pre-merge staging (외부 위치)

Pre-merge buffer 는 본 폴더 밖 `../logs/weekly/YYYY-MM-W<n>/` 로 이전 (2026-04-23 개편). 각 주별 폴더 안에 `weekly_draft_storming.md` (일별 누적) + `weekly_summary.md` (주 종료 시 정제). 자세한 workflow 는 `../logs/weekly/README.md`.

## Governance

### Pipeline (2026-04-23 개정 — weekly rotation at logs/weekly/)

```
working/<topic>.md                                          (증명/검증 완료분)
    ↓ daily append
logs/weekly/YYYY-MM-W<n>/weekly_draft_storming.md           (1주 buffer)
    ↓ weekly close — 주 종료 시 정제 요약
logs/weekly/YYYY-MM-W<n>/weekly_summary.md                  (user 리뷰 대상)
    ↓ weekly merge (user 결정)
canonical/canonical.md                                      (main, 주 1회 update)
canonical/theorem_status.md                                 (main 동기)
```

**Rationale (2026-04-23).** 이전 single-file `canonical_sub.md` 가 4일만에 2200줄 돌파 → weekly-folder 분할로 scale 관리 + 각 주 맥락 동결 + weekly_summary 중간 artifact 도입. 위치는 기존 `logs/weekly/` (journal 성격) 을 그대로 활용 — canonical/ 은 authoritative 문서만 보관.

### 들어오는 조건 (Promotion In)

`../working/<topic>.md`에서 다음 조건을 모두 만족할 때만 **현재 주의 `../logs/weekly/YYYY-MM-W<n>/weekly_draft_storming.md`** 에 daily append:
1. 증명 완료 (Category A) 또는 명시적 조건부 (Category B/C, 조건 명시)
2. 실험/테스트 검증 (해당 시)
3. 기존 canonical 내용과 무모순
4. working/daily reference 출처 명시

`weekly_draft_storming.md` append 방법:
- 해당 날짜 섹션에 `### Added` / `### Modified` / `### Retired` / `### Clarified` / `### Pending` 중 하나로 기록
- `canonical.md` 와 `theorem_status.md` 는 **본 시점에 직접 수정 안 함**

주 종료 시 (weekly close):
- 본 주의 `weekly_draft_storming.md` 전체를 정제 → **`weekly_summary.md`** (같은 폴더) 생성
- user 가 `weekly_summary.md` 리뷰

Weekly merge (user 결정 후):
- 새 정리 → `canonical.md` 해당 섹션 insert + `theorem_status.md` 행 추가
- 기존 정리 수정 → `canonical.md` 에 `*(Erratum YYYY-MM-DD: 사유)*` 인라인 추가
- **모든 변경은 `../CHANGELOG.md` 주간 entry 로 기록.**
- Merge 후: 이전 주 폴더는 **freeze** (삭제/수정 금지). 새 주는 새 `YYYY-MM-W<n>/weekly_draft_storming.md` 에서 시작.

### 나가는 조건 (Retraction Out)

오직 **명시적 철회(retract)**만 허용. 철회된 내용:
1. `canonical.md`에서 해당 섹션을 지우지 말고 `*(Retracted YYYY-MM-DD: 사유)*` 표시 + 본문 유지
2. `theorem_status.md`에 상태 변경
3. `../CHANGELOG.md`에 철회 사유 기록

**역류 금지.** canonical에 있던 내용을 working으로 "다시 작업 중"이라고 되돌리는 일은 없다. 철회는 철회로만.

## Why this discipline matters

canonical/이 단방향 승급만 받는 이유는 이론을 오염으로부터 구조적으로 보호하기 위함. 진행 중인 아이디어, 미검증 추측, 작업 중 수정은 모두 `../working/`에 살고, 그곳에서 충분히 정리·검증된 후에야 이곳으로 올라온다. 이 경계가 흐려지면 canonical의 권위가 붕괴된다.
