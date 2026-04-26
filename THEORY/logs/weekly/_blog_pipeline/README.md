# Blog Pipeline — Weekly Summary 발행 절차

**위치**: `THEORY/logs/weekly/_blog_pipeline/` (weekly 코호트와 동일 레벨, leading underscore 로 분리)

**목적**: Perception_theory 의 weekly close 결과를 `jack0682.github.io` 깃블로그에 매주 일관되게 발행하기 위한 워크플로우 + 체크리스트 + 템플릿.

**대상 블로그 레포**: `/Users/ojaehong/Perception/jack0682.github.io/`

---

## 운영 결정사항 (2026-04-26 정착)

| 항목 | 결정 |
|------|------|
| **블로그 게시 위치** | `content/journal/YYYY-MM-DD-perception-week-<N>.mdx` (단일 — date-stamped journal) |
| **소스 → 블로그 변환** | repo 의 `weekly_summary.md` 를 공개용으로 redact 후 mirror (실패/재현성 위기/음의 결과는 그대로 보존, 단 내부 도구명·경로 등 정제) |
| **canonical bump 트리거** | user 가 명시적으로 weekly merge 결정한 주에만 (현재 repo policy 와 동일) — weekly 발행과 canonical bump 는 분리 |
| **자동화 단계** | Phase 0 (지금): 수동, template + checklist 사용 / Phase 2 (W7+): `weekly_to_blog.mjs` 변환 스크립트 / Phase 3: 안정화 후 카운트 자동 갱신 |
| **데일리 로그** | 발행 안 함 (너무 자주) |

---

## 매주 워크플로우 (반복)

```
[Day 7 — weekly close, repo side]
1. THEORY/logs/weekly/YYYY-MM-W<n>/weekly_summary.md 정제 완료
2. (옵션) canonical merge 결정 → canonical.md + theorem_status.md + CHANGELOG.md 갱신
   ↓
[Day 7 또는 Day 8 — 블로그 발행]
3. weekly_summary.md 를 공개용 redact (내부 path / dev tooling 명 / 미공개 NQ 정제)
4. /Users/ojaehong/Perception/jack0682.github.io/content/journal/YYYY-MM-DD-perception-week-<n>.mdx 작성
   - template.mdx 복사 → frontmatter 채우기 → 본문 redact 결과 붙여넣기
5. canonical merge 가 발생한 주이면 → checklist.md 의 "canonical bump 체크리스트" 진행
6. cd /Users/ojaehong/Perception/jack0682.github.io && pnpm exec velite build
   - 0 errors 확인 (서버는 켜지 않음)
7. git commit (블로그 레포)
   ↓
[Optional]
8. 사용자가 시각 확인 후 push
```

---

## 파일

- `README.md` — 본 문서 (운영 결정 + 워크플로우)
- `checklist.md` — canonical bump 시 일괄 변경 대상 체크리스트 (12 페이지)
- `template.mdx` — weekly post 표준 포맷 (frontmatter + 절 구조)

---

## 첫 backfill 대상

**W4 + W4-extended (2026-04-19 ~ 2026-04-26)** — Critical-3 OPs 모두 해소 + T-V5b-T 승급. 블로그의 canonical 페이지는 이미 v2.3 으로 bump 완료 (2026-04-26). 남은 작업: weekly journal post 작성.

target file: `/Users/ojaehong/Perception/jack0682.github.io/content/journal/2026-04-26-perception-week-4-extended.mdx`

---

## 주의사항

- **canonical bump 없는 주의 weekly post 도 발행한다**. 그래야 working/ 단계의 진행과 음의 결과도 기록된다 (블로그의 가치).
- **redact 원칙**: 실패/철회/재현성 위기 = 보존 / 내부 인프라 = 정제.
- **canonical bump 주에는 checklist 12 항목 모두 통과**해야 발행 (자기모순 방지).
- **service 는 안 켠다** — `pnpm exec velite build` 만으로 검증. dev server 는 user 가 직접 띄움.
- **data 만 갱신, 구조 변경 금지** — sidebar / route / theme 변경은 별도 작업.
