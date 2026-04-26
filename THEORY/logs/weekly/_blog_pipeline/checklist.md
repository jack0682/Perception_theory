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

## 11. 검증 (2단계 필수 — velite 만으로는 부족)

- [ ] **단계 1 — velite content build**: `cd /Users/ojaehong/Perception/jack0682.github.io && pnpm exec velite build` → 0 errors
  - acorn parse 에러를 잡음 (math 모드 밖 brace 표현 등 syntactic 문제)
- [ ] **단계 2 — full next.js production build**: `pnpm build` → 0 errors, 모든 페이지 prerender 성공
  - **velite 가 통과해도 next prerender 에서 잡히는 trap 이 있다** — JSX expression 이 syntactically valid 하지만 render time 에 undefined reference 인 경우 (`ReferenceError: B is not defined` 등)
  - 296+ pages prerender 가 모두 성공해야 함
- [ ] grep 으로 카운트 자기모순 점검: `grep -E "[0-9]+ Cat A|[0-9]+ Category A" content/notes/part-0/*.mdx` — 모든 페이지 동일 숫자 (`38` 등)
- [ ] 빌드 산출 review (옵션): `.velite/journal.json` 에 새 weekly post slug 등록 확인 (`grep -c "<slug>" .velite/journal.json`)

---

## 12. 커밋

- [ ] `git add` + `git commit` (블로그 레포). user 가 push 결정.
- [ ] commit message 형식: `chore: weekly W<n> close — canonical v2.X bump (Cat A +<diff>)`
  - 예: `chore: weekly W4-extended close — canonical v2.3 bump (Cat A +3)`

---

## MDX 트랩 (자주 발생하는 빌드 에러)

### Type 1: acorn parse error (velite 단계에서 잡힘)

**증상**: `error Could not parse expression with acorn body`

**원인**: math 모드 밖에서 `{...}` 가 JSX expression 으로 해석되는데, 그 안에 invalid JS syntax (`2x2` 같은 number-prefix identifier 등) 가 있을 때.

**fix**: `$...$` 로 래핑하거나 `\{...\}` 로 escape.

**흔한 케이스**:
- `R^{2x2}` → `$\mathbb{R}^{2 \times 2}$`
- `Σ^K_M` (math 밖) → `$\Sigma^K_M$`
- `\widehat{K}` (math 밖) → `$\widehat{K}$`
- `~ L^{2.8}` → `$\sim L^{2.8}$`

### Type 2: prerender ReferenceError (velite 통과, next build 에서 잡힘)

**증상**: `ReferenceError: <Letter> is not defined`. velite 빌드는 0 errors 인데 `pnpm build` 의 prerender 단계에서 specific page 가 실패.

**원인**: math 모드 밖에서 `{X, Y, Z}` 같은 패턴이 syntactically valid JS 로 파싱됨. `{B, B+C, E, C+E}` → JSX expression `<>{B, B+C, E, C+E}</>` 으로 해석 → render 시 변수 B, C, E 가 undefined → ReferenceError.

**fix**: brace 자체를 제거하거나 escape. Set notation 은 prose 로 풀어쓰기 권장:
- ❌ `Pareto frontier {B, B+C, E, C+E}` 
- ✅ `Pareto frontier 는 B, B+C, E, C+E 로 산출`
- ✅ 또는 `Pareto frontier $\{B, B+C, E, C+E\}$` (math escape)

**검출**: `grep -nE '\{[A-Z][^$]*\}' content/journal/<file>.mdx` — math 모드 밖의 대문자-시작 brace expression 찾기.

### Type 3: frontmatter YAML 오류

**증상**: 페이지가 빌드되지 않거나 frontmatter 가 깨진 채로 표시됨.

**원인**: `summary:` 등 string 값 안에 unquoted `:` 콜론이 있으면 YAML parser 가 key-value 로 오해석.

**fix**: 따옴표로 감싸기.
- ❌ `summary: This: a problem`
- ✅ `summary: "This: a problem"`

### Type 4: link slug 미스매치

**증상**: 빌드 통과되지만 사이트에서 dead link.

**원인**: `[text](/notes/part-0/canonical-spec-scc-X/)` 의 X 가 실제 slug 와 다름.

**fix**: 변경 시 모든 cross-reference grep 으로 점검. canonical 페이지의 slug 는 frontmatter `slug:` 가 truth.

### Type 5: math mode 안의 한글 / non-ASCII

**증상**: 일부 environment 에서 KaTeX 렌더링 실패.

**fix**: math 안에는 한글/한자 사용 금지. 한글 설명은 math block 밖에.

---

## 체크리스트 자체 갱신 이력

- **2026-04-26**: 초안 (W4 backfill 작업 기반)
- **2026-04-27**: §11 검증을 2단계 (velite + next build) 로 분리. Type 2 prerender ReferenceError trap 추가 (실전에서 weekly post 의 `{B, B+C, E, C+E}` set notation 에 의해 발생).
