---
type: MOC
cluster: research-journal
id: MOC_research_journal
parent: [[THEORY_INDEX]]
last_updated: 2026-05-14
---

# MOC: Research Journal (logs/daily/weekly/monthly)

> [!nav] Theory Navigation
> Parent: [[THEORY_INDEX]]
> Authority: chronological raw record; not authoritative for claims
> Status: Active (다음 promotion 의 입력)

## Purpose

3-stage promotion pipeline 의 첫 단계 — `logs/daily/YYYY-MM-DD/` 의 날것 기록. 여기서 `working/<topic>.md` 로 reorganize 되고, 다시 `canonical/canonical.md` 로 promote. 이 MOC 는 journal navigation 용이며 *수학적 권위 없음* (canonical 만 권위).

## Structure

```
logs/
├── daily/YYYY-MM-DD/    raw chronological record (2026-04-12 ~ 현재)
├── weekly/YYYY-Www/     weekly retrospective synthesis
└── monthly/YYYY-MM/     monthly digest
```

## Active Date Ranges

- **2026-04-12 ~ 2026-04-18:** Research OS 시도 → 폐기 (archive 됨)
- **2026-04-18 ~ 2026-05-04:** 현재 구조 안착 + 일일 promotion 흐름 정착
- **2026-05-04 ~ 2026-05-08:** OMS Sessions 1~8 집중 (Level-2 확장)
- **2026-05-10:** W7-FINAL — H-SINK FULLY CLOSED, CV-1.12 봉인
- **2026-05-10:** W7-CV1.13 — T-Temporal-Identity Cat A, [[CV-1.13_SEAL]]
- **2026-05-12 ~ 2026-05-13:** AFD-0 v0.1 draft, 'Cat A by construction' R-2 실패 모드 식별
- **2026-05-14 morning:** W7-Day5 Track 1, [[CV-1.15_SEAL]] (action-based temporal cost)
- **2026-05-14 evening:** W7-Day5 extension, [[CV-1.16_SEAL]] (H-MORSE Local Closure Package)

## Weekly Highlights (2026-04-W4 ~ 2026-05-W2)

- `2026-04-W4` — Research OS 잔재 정리 시작
- `2026-04-W5` — 현재 working/ 구조 안착
- `2026-05-W1` — OMS push, Sessions 1~6
- `2026-05-W2` — H-SINK closure + T-Temporal-Identity Cat A + CV-1.13~1.16 봉인 sprint

## Reading Order

1. [[CHANGELOG]] (theory-side 변경 로그 — 일지보다 abstract)
2. 가장 최근 daily/ entry (현재 상태 파악)
3. 가장 최근 weekly/ entry (retrospective synthesis)

## Dependencies (Pipeline)

```
logs/daily/  →  working/<topic>.md  →  canonical/canonical.md
   ↑              ↑                       ↑
이 MOC      [[INDEX|working/INDEX.md]]   [[MOC_canonical_authority]]
```

## Policy

- daily/ 안 내용은 **권위 없음**. wikilink 가 가능하나, 수학 주장 인용은 canonical/ 또는 working/ 의 promote 된 형태로만.
- weekly_draft_storming 과 weekly_summary 는 더 이상 *필수 staging* 이 아님 (2026-05-04 audit 에서 단순화).
- weekly_summary 는 retrospective 용으로 계속 작성.

## Related Clusters

- [[MOC_canonical_authority]] (CHANGELOG, SEAL chain)
- [[INDEX|working/INDEX.md]]
- [[MOC_open_problems_blockers]]

---

*MOC_research_journal, 2026-05-14.*
