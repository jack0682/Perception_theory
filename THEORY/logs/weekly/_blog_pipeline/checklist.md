# Canonical Bump 체크리스트 (블로그 측 12 페이지)

**언제 사용**: weekly merge 가 canonical.md 에 변경을 가한 주에만. canonical bump 없는 주의 weekly post 는 journal 만 추가하면 끝.

**대상 레포**: `/Users/ojaehong/Perception/jack0682.github.io/`

**검증**: 모든 항목 통과 후 `pnpm exec velite build` → 0 errors. 그 이후에 git commit.

---

## 0. 사전 준비

- [ ] repo 측 `weekly_summary.md` 의 "Canonical Spec Version Bump" 절을 확인 — 어느 정리가 추가/철회/이동되었는지 정리
- [ ] 새 canonical 버전 번호 결정 (v2.X → v2.X+1)
- [ ] 새 카운트 결정 (Cat A / B / C / Retracted / 총 claims / % proved)

---

## 1. canonical-spec-scc.mdx (index)

- [ ] frontmatter `title:` — "v2.X" 갱신
- [ ] frontmatter `updated:` — 새 날짜
- [ ] frontmatter `summary:` — 카운트 갱신
- [ ] 본문 첫 단락 — version 갱신
- [ ] "Key Changes from v2.{X-1}" 절 — 신규 정리 / 철회 / 변동 요약 추가
- [ ] Part 5 description — 새 카운트 + 새 정리명 포함

---

## 2. Parts 1–3 (foundations / axioms / energy)

이 세 파일은 보통 변경 없음. 헤더만 갱신:

- [ ] `canonical-spec-scc-1-foundations.mdx` — frontmatter `updated:` + 본문 헤더 v2.X
- [ ] `canonical-spec-scc-2-axioms.mdx` — 동상
- [ ] `canonical-spec-scc-3-energy.mdx` — 동상

(만약 axiom 변경이 있는 주이면 본문도 갱신)

---

## 3. canonical-spec-scc-4-interpretation.mdx (§10–§12)

- [ ] frontmatter `updated:` + `summary:`
- [ ] 본문 헤더 v2.X
- [ ] §11.1 Fixed Commitments — 신규 commitment 추가 시 새 항목 번호 부여
- [ ] §11.2 Open Design Choices — 해소된 항목 제거 / 신규 추가
- [ ] §12 Open Problems — 다음 중 해당하는 변동 반영:
  - 새 OP 해소 시 해당 절 상태 변경
  - 신규 Cat A 결과는 Foundational/Bridging/Extension 중 적절한 곳에 추가
  - 새 NQ 카려는 절 끝에 추가

---

## 4. canonical-spec-scc-5-results-registry.mdx (§13–§15) — 가장 큰 변경

- [ ] frontmatter `updated:` + `summary:` (카운트)
- [ ] 본문 헤더 v2.X
- [ ] §13 첫 단락 erratum 라인 — 카운트 + 새 버전
- [ ] §13 "Category A: Fully Proved (X theorems)" 헤더 — 카운트
- [ ] §13 신규 정리 entry — 적절한 위치에 (W<N> 추가 절 사용)
  - **statement / proof / status / source 4-필드 필수**
- [ ] §13 신규 Cat C / Cat B 도 동일하게
- [ ] §14 Commitment Notes — CN 신규 추가 시
- [ ] §15 Closing Summary — 다음 항목 모두 갱신:
  - 카운트
  - 새 정리 mention
  - W<N> close 절 (paragraph 신설 또는 추가)

---

## 5. scc-theorem-registry.mdx (별도 정리 인덱스)

- [ ] frontmatter `updated:` + `summary:`
- [ ] "Canonical Spec v1.X (YYYY-MM-DD) — Current Version" 절 신설 (이전 절 위로 push)
- [ ] 신규 정리 row 추가 (T-ID | Name | Status | Cat | Source | Proof | Experiments | Notes)
- [ ] 이전 버전 release notes 절 추가
- [ ] "Active Claims / Resolved Claims" 표 — 상태 변경 반영
- [ ] "Counterexamples & Challenges" 표 — superseded 항목 처리
- [ ] "Canonical Spec Version History" — 새 CV 절 추가
- [ ] "Open Problems (OP-xxxx)" 표 — 상태 변동
- [ ] "Proof Status Summary" — 카운트
- [ ] 마지막 footer line — Last updated / Total / Open / 추가 정리 모두 갱신

---

## 6. scc-status-2026-04.mdx (status 롤업)

- [ ] frontmatter `updated:` + `title:` (월 변경 시 slug 도) + `summary:`
- [ ] 본문 헤더 ("Last updated", "Canonical version")
- [ ] "Theorem ledger" 절 — 카테고리별 카운트 + 신규 정리
- [ ] "Open problems" 절 — W<N> 변동 반영
- [ ] "Implementation" 절 — test count 변경 시
- [ ] (큰 구조 변동이 있는 주만) Repository structure 절

---

## 7. scc-research-overview.mdx (narrative overview)

- [ ] frontmatter `updated:` + `summary:`
- [ ] 본문 첫 단락 ("Date / Canonical version / Theorem status")
- [ ] §5 Theorem Registry table — 카운트
- [ ] §5 Group N — 신규 정리 추가 (그룹 번호 sequential)
- [ ] §6 What Remains Open — 해소된 OP 제거 / 신규 추가
- [ ] §8 test count

---

## 8. scc-glossary.mdx (용어집)

- [ ] frontmatter `updated:` + `summary:`
- [ ] 신규 용어 entry (CN, σ-framework 같은 핵심 용어 등장 시)
- [ ] OP 상태 변경 entry — F-1/M-1/MO-1 같은 항목의 상태 라인 갱신
- [ ] Quick-Reference by Question — "What's broken?" / "Are theorems right?" 답변 갱신
- [ ] footer Last updated

---

## 9. claim-c0001 / claim-c0002 (claim 페이지)

이 두 파일은 보통 변경 없지만 의존 변동 시:

- [ ] `claim-c0001-soft-cohesion-primitive.mdx` — Validation Status 표의 카운트
- [ ] `claim-c0002-k-field-architecture.mdx` — 의존 OP 상태 변동 시 Status 라인 / Confidence 재평가

---

## 10. journal weekly post 작성

- [ ] `content/journal/YYYY-MM-DD-perception-week-<n>.mdx` 신규 파일
- [ ] template.mdx 복사 → frontmatter 채우기
- [ ] redact 된 weekly_summary 본문 삽입
- [ ] canonical bump 한 주이면 `canonicalImpact: bumped` + `canonicalVersion: v2.X` 명시
- [ ] Pointers 절에 변경된 canonical 페이지 절 링크 첨부

---

## 11. 검증

- [ ] `cd /Users/ojaehong/Perception/jack0682.github.io && pnpm exec velite build` → 0 errors
- [ ] grep 으로 카운트 자기모순 점검: `grep -E "[0-9]+ Cat A|[0-9]+ Category A" content/notes/part-0/*.mdx` — 모든 페이지 동일 숫자 (`38` 등)
- [ ] 빌드 산출 review (옵션): `.velite/` 출력에서 새 entry 등록 확인

---

## 12. 커밋

- [ ] `git add` + `git commit` (블로그 레포). user 가 push 결정.
- [ ] commit message 형식: `chore: weekly W<n> close — canonical v2.X bump (Cat A +<diff>)`
  - 예: `chore: weekly W4-extended close — canonical v2.3 bump (Cat A +3)`

---

## MDX 트랩 (자주 발생하는 빌드 에러)

- **acorn parse error "Could not parse expression with body"**: math 모드 밖에서 `{...}` 가 JSX expression 으로 해석. fix → `$...$` 로 래핑하거나 `\{...\}` 로 escape.
  - 흔한 케이스: `R^{2x2}`, `Σ^K_M` (밖에서 사용 시), `\widehat{K}` (math 모드 밖)
- **frontmatter YAML 오류**: `summary:` 안에 `:` 콜론이 unquoted 로 있으면 깨짐. 따옴표로 감싸기.
- **link slug 미스매치**: `/notes/part-0/canonical-spec-scc-X/` 경로에서 X 가 실제 slug 와 안 맞으면 dead link.
