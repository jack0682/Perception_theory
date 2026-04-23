# logs/weekly/ — 주간 Rotating Buffer (Pre-Canonical Staging)

**Purpose.** Canonical 승급 전 **주 단위** staging area. 이전의 `canonical/canonical_sub.md` 단일 파일을 2026-04-23 에 본 폴더의 주간 폴더 구조로 개편. `logs/weekly/` 가 기존 chronological journal convention 이라 `canonical/` 의 authoritative 범위와 분리하여 배치.

## Folder convention

```
logs/weekly/
├── README.md                              ← 본 파일
├── 2026-04-W4/                            ← April 4th week (Apr 19–25, 2026)
│   ├── weekly_draft_storming.md           ← 일별 누적 buffer (append-only)
│   └── weekly_summary.md                  ← 주 종료 시 생성, canonical merge 전 정제 산출물
├── 2026-04-W5/                            ← 다음 주 (Apr 26–30)
│   └── weekly_draft_storming.md
└── ...
```

**Week 번호 convention.** `YYYY-MM-W<n>` — 해당 **월** 내 주차. Week 1 은 해당 월의 첫 Sunday-start 주 (첫 주 부분 주 포함). 월 경계를 넘는 주는 **시작일이 속한 월** 기준으로 폴더명 결정.

- 예: 2026-04-W4 = Apr 19 (Sun) – Apr 25 (Sat).
- 예: 2026-04-W5 = Apr 26 (Sun) – Apr 30 (Thu) + Apr 26 주간이 5월로 이어지는 경우 5월 부분은 `2026-05-W1/` 에 별도.

## 기존 logs/ 구조와의 관계

```
logs/
├── daily/YYYY-MM-DD/          ← raw chronological research journal (atomic)
├── weekly/YYYY-MM-W<n>/       ← pre-canonical staging (2026-04-23 개편; 본 폴더)
│   ├── weekly_draft_storming.md   (daily append)
│   └── weekly_summary.md          (week close 시 정제 → canonical merge 후보)
└── monthly/YYYY-MM/           ← 월간 통합 synthesis (2026-04-23 신설)
    ├── monthly_summary.md         (weekly summary 들의 cross-week 통합)
    └── monthly_retrospective.md   (옵션: narrative 회고)
```

**3-tier 역할 분화**:
- `daily/` — 원재료 (chronological, atomic)
- `weekly/` — promotion pipeline 중간 단계 (draft → summary → canonical merge 후보)
- `monthly/` — synthesis only (canonical merge 없음, arc/theme/meta-lesson 보존)

**Flow**: daily → weekly draft → weekly summary **→ canonical merge (← 여기서 canonical 업데이트 끝)** + monthly summary (parallel, 월말)

## Workflow

### 1. 매일 (daily append)

해당 주의 `weekly_draft_storming.md` 상단에 날짜 섹션 추가:

```markdown
## 2026-04-24

**Session type:** ...
**Origin:** logs/daily/2026-04-24/...

### Added
...
### Modified
...
### Pending
...
```

타입 5 종 (`Added`, `Modified`, `Retired`, `Clarified`, `Pending`) 만 사용.

### 2. 주 종료 시 (weekly close)

주 마지막 일 (또는 이른 다음 주 시작일) 에 `weekly_summary.md` 작성:

- 주간 Cat A 누적 집계
- Retirements / Modifications 목록
- Pending carry-forward 목록
- 새 NQ 집계
- **Critical self-assessment** (config-specific vs universal, reproducibility, open concerns)
- 다음 주 권고

### 3. Weekly merge (user 결정)

`weekly_summary.md` 를 user 가 리뷰:

- 승급 → `../../canonical/canonical.md` + `../../canonical/theorem_status.md` 수정 + `../../CHANGELOG.md` entry
- 보류 → 본 폴더에 freeze (이후 삭제·수정 금지)
- 새 주는 새 `YYYY-MM-W<n>/weekly_draft_storming.md` 에서 시작

### 4. Freeze policy

Merge 완료된 이전 주 폴더는 **동결 (freeze)**:

- 내용 삭제·수정 금지
- 이력 추적 용도로 보존
- 필요 시 `../../canonical/canonical.md` 에서 `*(Origin: logs/weekly/2026-04-W4/weekly_summary.md §...)*` 로 참조

## Rationale (2026-04-23 개편 배경)

기존 `canonical/canonical_sub.md` 단일 파일은:
- 2026-04-20 생성 → 4일 후 ~2200줄 (scale 문제)
- 주간 merge 후 reset 기대했으나 첫 merge 전에 overload
- 이전 주 맥락이 merge 시점에 flat 하게 사라짐 (context loss)

Weekly rotation (본 폴더) 은:
- **파일 크기 bounded** (주당 ~500줄 내외 예상)
- **맥락 보존** (merge 후에도 해당 주 폴더 동결로 historical record)
- **중간 정제 artifact** (`weekly_summary.md`) 가 canonical merge 품질 향상
- **Diff 추적 용이** (주 단위 snapshot)
- **배치 정합성** (`canonical/` 은 authoritative 문서만, `logs/weekly/` 는 journal 성격의 pre-merge staging)

## Cross-references

- Canonical pipeline 전체: `../../canonical/README.md`
- Theory main spec: `../../canonical/canonical.md`
- Theorem index: `../../canonical/theorem_status.md`
- Open problems: `../../canonical/open_problems.md`
- Changelog: `../../CHANGELOG.md`
- Daily logs: `../daily/YYYY-MM-DD/`
