# THEORY/logs/ — 연구 기록 (Research Journal)

**시간순 날것 기록.** 오늘 뭘 했는지, 무엇을 시도했는지, 어디서 막혔는지 자유롭게 기록.

## 구조

```
logs/
├── daily/       YYYY-MM-DD.md   (필요시)
├── weekly/      YYYY-Www.md     (주간 요약, 선택)
└── monthly/     YYYY-MM.md      (월간 요약, 선택)
```

### daily/

**필요할 때만 작성.** 매일 강제 아님. 무언가 진전·발견·막힘이 있을 때 날짜 파일 하나.

파일명: `YYYY-MM-DD.md` (예: `2026-04-20.md`)

형식 자유. 권장 골격:

```markdown
# YYYY-MM-DD

## What happened today

<narrative>

## What I tried

- <attempt 1>
- <attempt 2>

## What I learned / decided

<observations>

## Blockers / open questions

<what's stuck>

## Next

<tomorrow's seed>
```

### weekly/ (선택)

주가 끝날 때 돌아보면서 쓴다. `YYYY-Www.md` (ISO week, 예: `2026-W17.md`).

- 이번 주 전체에서 건진 것
- 실패한 방향 (다시 돌아올 것인가?)
- 다음 주 초점

매주 강제 아님. 의미 있을 때만.

### monthly/ (선택)

월말 재정렬. `YYYY-MM.md` (예: `2026-04.md`).

- 한 달 단위 방향 전환 기록
- canonical/에 승급된 것, working/에 남은 것, logs/에만 있는 것의 총 정리

## 기록 ↔ 이론 분리

**중요:** 여기 적는 것은 이론 자체가 아니다. 날것의 연구 흐름이다. 

- "오늘 F-1에 대해 X 접근을 시도했다가 Y 반례를 만났다" → `daily/2026-04-20.md`에 기록
- "F-1 전체 현황과 현재 가장 유망한 경로" → `working/F-1_kinetic.md`에 통합
- "F-1이 해결되어 증명이 완성되었다" → `canonical/canonical.md`에 추가 + `working/F-1_kinetic.md`는 흡수/아카이브

**logs/에 쓰인 내용을 보고 canonical을 수정하지 않는다.** 반드시 working을 경유.

## Research OS와 구별

- 5역할 분할 없음 (lead/proof/critic/experiment/archivist 포맷 재도입 금지)
- 메타데이터 프론트매터 없음
- 매일 강제 없음
- 디렉토리 깊이 최대 2단계 (`logs/daily/`)

2026-04-13~19의 `02_roadmap/04_daily_log/` 5역할 강제 포맷은 04-16부터 붕괴하며 폐기됨 (`_archive/research_os_2026-04-12/`). 재도입 금지.
