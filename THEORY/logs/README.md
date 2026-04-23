# THEORY/logs/ — 연구 기록 (Research Journal) + Pre-Canonical Staging

**시간순 기록 + promotion pipeline 중간 단계.** daily 는 날것 기록, weekly/monthly 는 canonical 승급 파이프라인의 staging/synthesis layer.

## 구조 (2026-04-23 개편, 3-tier)

```
logs/
├── daily/     YYYY-MM-DD/       (원재료, atomic, 필요시)
├── weekly/    YYYY-MM-W<n>/     (pre-canonical staging, 주 단위 rotating buffer)
│   ├── weekly_draft_storming.md     (daily append)
│   └── weekly_summary.md            (week close 시 정제 → canonical merge 후보)
└── monthly/   YYYY-MM/          (월간 synthesis, canonical merge 없음)
    ├── monthly_summary.md           (weekly summary 들의 cross-week 통합)
    └── monthly_retrospective.md     (옵션: narrative 회고)
```

**3-tier 역할 분화**:

| Layer | 목적 | 생성 빈도 | Canonical merge 대상? |
|---|---|---|---|
| `daily/` | 원재료 기록 | 필요할 때만 | ❌ (working 경유 필수) |
| `weekly/` | Promotion staging | 주 단위 rotating | ✅ (weekly_summary.md) |
| `monthly/` | Macro synthesis | 월 1 회 | ❌ (집계만) |

각 layer 에 전용 README 존재:
- `weekly/README.md` — daily append → week close workflow
- `monthly/README.md` — 월간 통합 + retrospective workflow

### daily/

**필요할 때만 작성.** 매일 강제 아님. 무언가 진전·발견·막힘이 있을 때 해당 날짜 폴더 또는 파일.

- 단순 노트: `daily/YYYY-MM-DD.md`
- 다중 session/topic 날: `daily/YYYY-MM-DD/*.md` (예: `01_exploration.md`, `99_summary.md`)

형식 자유. 권장 골격:

```markdown
# YYYY-MM-DD

## What happened today
<narrative>

## What I tried
- <attempt 1>

## What I learned / decided
<observations>

## Blockers / open questions
<what's stuck>

## Next
<tomorrow's seed>
```

### weekly/ (pre-canonical staging — 2026-04-23 개편)

**기존 canonical_sub.md 단일 파일을 주간 rotating 구조로 개편**. 이전의 선택적 weekly journal 역할을 넘어 **canonical merge 파이프라인의 정규 중간 단계** 가 됨.

파일/폴더 명명: `YYYY-MM-W<n>/` (월 내 주차; "시작일 속한 월" 기준으로 결정). 상세 workflow 는 `weekly/README.md`.

Flow:
1. **Daily append**: 매일 해당 주 `weekly_draft_storming.md` 에 날짜 섹션 추가 (Added/Modified/Retired/Clarified/Pending 타입)
2. **Week close**: 주 종료일 (Sat) 에 `weekly_summary.md` 작성 (주간 정제 산출물)
3. **Canonical merge**: user 가 `weekly_summary.md` 리뷰 후 선별적으로 `canonical/canonical.md` + `theorem_status.md` 에 merge, `CHANGELOG.md` entry
4. **Freeze**: merge 완료된 이전 주 폴더 동결 (삭제·수정 금지)

### monthly/ (월간 synthesis — 2026-04-23 신설)

**해당 월의 weekly_summary.md 들의 macro-view 통합**. Canonical 에 직접 merge 되지 않는 synthesis-only layer. 상세는 `monthly/README.md`.

생성 트리거: 해당 월의 마지막 weekly_summary.md 가 close 된 시점 (통상 다음 월 첫 Sun 근처).

내용:
- 각 weekly summary 의 bullet integration
- 월간 Cat A / Retirements / NQ 집계
- Cross-week narrative (theme continuity, turning points)
- Long-arc meta-lessons
- 다음 월 권고

옵션으로 `monthly_retrospective.md` — narrative 회고 (major pivots, abandoned directions, epistemic failures).

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
