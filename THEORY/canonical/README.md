# THEORY/canonical/ — 완결된 권위 (Settled Authority)

**이 폴더는 승급(promoted)된 내용만 들어온다. 진행 중인 작업이나 검증 전 가설은 금지.**

## Contents

- **`canonical.md`** — 권위 스펙 (현재 v1.2, 1216줄, 2026-04-12 기준). 이 레포의 이론에 관한 유일한 authoritative 문서.
- **`theorem_status.md`** — 정리 인덱스 (증명/조건부/열린/철회). `canonical.md`와 일치해야 함.
- **`open_problems.md`** — F-1 (K=2 vacuity), M-1 (K=1 preference), MO-1 (Morse inapplicable). 현재 critical 3건.

## Governance

### 들어오는 조건 (Promotion In)

`../working/<topic>.md`에서 다음 조건을 모두 만족할 때만 승급:
1. 증명 완료 (Category A) 또는 명시적 조건부 (Category B/C, 조건 명시)
2. 실험/테스트 검증 (해당 시)
3. 기존 canonical 내용과 무모순

승급 방법:
- 새 정리 → `canonical.md` 해당 섹션에 본문 추가 + `theorem_status.md`에 행 추가
- 기존 정리 수정 → `canonical.md`에 `*(Erratum YYYY-MM-DD: 사유)*` 인라인 추가
- **모든 변경은 `../CHANGELOG.md`에 날짜별 기록.**

### 나가는 조건 (Retraction Out)

오직 **명시적 철회(retract)**만 허용. 철회된 내용:
1. `canonical.md`에서 해당 섹션을 지우지 말고 `*(Retracted YYYY-MM-DD: 사유)*` 표시 + 본문 유지
2. `theorem_status.md`에 상태 변경
3. `../CHANGELOG.md`에 철회 사유 기록

**역류 금지.** canonical에 있던 내용을 working으로 "다시 작업 중"이라고 되돌리는 일은 없다. 철회는 철회로만.

## Why this discipline matters

canonical/이 단방향 승급만 받는 이유는 이론을 오염으로부터 구조적으로 보호하기 위함. 진행 중인 아이디어, 미검증 추측, 작업 중 수정은 모두 `../working/`에 살고, 그곳에서 충분히 정리·검증된 후에야 이곳으로 올라온다. 이 경계가 흐려지면 canonical의 권위가 붕괴된다.
