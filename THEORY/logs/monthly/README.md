# logs/monthly/ — 월간 통합 Summary

**Purpose.** 해당 월의 weekly_summary.md 들을 기반으로 **macro-view + long-arc narrative** 제공. Canonical 의 직접 merge 대상은 아니며, cross-week theme, turning point, meta-lesson 을 정리하는 retrospective layer.

**Scope differentiation.**
- `daily/` — 날것 research journal (atomic)
- `weekly/` — pre-canonical staging (draft → summary → canonical merge)
- `monthly/` — **synthesis only**, canonical merge 없음. 해당 월의 arc 를 기록

## Folder convention

```
logs/monthly/
├── README.md                              ← 본 파일
├── 2026-04/                               ← April 2026
│   ├── monthly_summary.md                 ← 해당 월 weekly summary 들의 통합 (필수)
│   └── monthly_retrospective.md           ← 옵션: narrative 회고, turning points, abandoned directions
├── 2026-05/
│   └── monthly_summary.md
└── ...
```

**월 명명 convention.** `YYYY-MM` — 해당 월 그대로. 월 경계를 넘는 주는 `weekly/` 에서 "시작일이 속한 월" 기준으로 이미 분할되어 있으므로 monthly 는 자연스럽게 해당 월의 모든 `YYYY-MM-W<n>/` 를 포괄.

- 예: 2026-04/ = `weekly/2026-04-W4/` + `weekly/2026-04-W5/` (+ W1–W3 구조 도입 전이므로 없음)
- 예: 2026-05/ = `weekly/2026-05-W1/` + `weekly/2026-05-W2/` + ...

## Workflow

### 1. 생성 트리거 (When to generate)

해당 월의 **마지막 weekly_summary.md** 가 close 된 시점에 monthly_summary.md 작성.

- 2026-04 예: 2026-04-W5 (Apr 26 – May 2) 의 weekly_summary.md 가 2026-05-03 (Sun) 경에 close → 같은 날 2026-04/monthly_summary.md 작성
- 즉 월 전환기 (Sun 첫 주 시작 전후) 가 natural generation 시점

### 2. monthly_summary.md 내용 구조

1. **해당 월의 weekly arc** — 각 weekly_summary.md 의 핵심을 한 단락으로 통합 (chronological)
2. **월간 Cat A 집계** — canonical 에 merge 된 것 + pending 대기 중인 것 모두
3. **월간 Retirements / Modifications** — 철회된 것 + 수정된 것의 누적
4. **월간 NQ 집계** — 신규 발생 NQ 수 + close / promote 된 NQ 수
5. **Cross-week narrative** — 여러 주에 걸친 theme 연속성, key turning points, paradigm shifts
6. **Long-arc meta-lessons** — 단순 기술적 학습이 아닌 방법론적 / 인식론적 발견
7. **다음 월 권고** — macro-planning level (단일 세션이 아닌 월 수준 방향성)

### 3. monthly_retrospective.md (옵션)

Narrative reflection 이 필요한 달에만 생성. 예:
- Major pivots (예: 2026-04-23 orbital discovery turn)
- Abandoned directions + why
- Epistemic failures (overclaimed, under-tested)
- Tool / infrastructure decisions (예: weekly rotation 구조 도입)

Retrospective 은 factual summary 와 분리하여 **voice 를 유지** — "무엇을 했다" 가 아니라 "무엇을 배웠고 무엇을 다르게 했어야 했나".

### 4. Freeze policy

Monthly summary 작성 후:
- 해당 월의 모든 `weekly/YYYY-MM-W<n>/` 폴더는 이미 frozen (weekly README 참조)
- Monthly summary 자체도 **작성 후 freeze** (삭제·수정 금지)
- 필요 시 `canonical.md` 에서 `*(Origin: logs/monthly/2026-04/monthly_summary.md §...)*` 로 참조

### 5. Monthly → Canonical 관계

**Monthly summary 는 canonical 에 직접 merge 되지 않는다.** Canonical merge 는 **weekly level** 에서만 발생 (weekly_summary.md → user review → canonical.md). Monthly 는 이미 이루어진 canonical merge 들의 **집계 + narrative**.

단 예외: Monthly retrospective 에서 발견된 meta-pattern 이 canonical CN (Canonical Note) 추가를 촉발할 수 있음. 이 경우 해당 CN 은 **다음 주의 weekly_draft_storming.md** 를 통해 정규 pipeline 으로 승급.

## Rationale

Weekly rotation 은 scale 문제를 해결하지만 **cross-week continuity 가 flat 하게 사라지는 부작용** 이 있음. 각 weekly_summary 는 해당 주에 focused 되어 있어, 여러 주에 걸친 arc (예: R17-R22 6 rounds, 또는 pre-theory → empirical pivot) 가 명시적으로 남지 않음.

Monthly layer 는:
- **Arc 보존** — 여러 주의 theme continuity 명시
- **Turning point 기록** — 단일 주 내에서 보이지 않던 전환점 (예: theoretical → empirical pivot)
- **Meta-lesson 축적** — 단일 주 관점에서 교훈으로 보이지 않던 패턴
- **Canonical CN 후보 산실** — 월간 반복되는 패턴이 CN 으로 승급 대상이 되는 source

## 월별 status (이 섹션은 매월 말 갱신)

| 월 | Weeks covered | Monthly summary | Retrospective | Canonical merges this month |
|---|---|---|---|---|
| 2026-04 | W4 (+ W5 예정) | 🔨 2026-05-03 target | TBD | pending (weekly review 대기) |

## Cross-references

- Daily logs: `../daily/YYYY-MM-DD/`
- Weekly staging: `../weekly/YYYY-MM-W<n>/` + `../weekly/README.md`
- Canonical pipeline: `../../canonical/README.md`
- Theory main spec: `../../canonical/canonical.md`
- Changelog: `../../CHANGELOG.md`
