# Perception_theory Research OS 리팩토링 계획

**작성일:** 2026-04-12  
**목표:** "사유의 상태 머신" 구조로 전환  
**원칙:** 파일 삭제 없음 (archive로 이동)

---

## 현황 분석

### 현재 구조 (flat + date-partitioned)

```
Perception_theory/
├── *.md (root level, 12개)
│   ├── Canonical Spec v2.0, v2.1, v2.2 (3개 버전 혼재)
│   ├── CLAUDE.md, CONVENTIONS.md, CHANGELOG.md
│   ├── Agent Instructions.md, AGENTS.md
│   ├── RESEARCH_OVERVIEW.md, README.md
│   ├── EXP-VERIFICATION-RESULTS.md
│   └── THEORY_STATUS_2026-04-12.md
├── docs/
│   ├── 03-26, 03-27, 03-30, 03-31/
│   └── 04-01, 04-02, 04-03, 04-04, 04-06, 04-07, 04-10, 04-11, 04-12/
│       (각 폴더 내부: audit, proof, theory, analysis, synthesis 등)
├── experiments/ + results/
├── papers/ + paper_template/
├── plan/ + plan/archive/
├── result/
├── scc/ (구현 - 그대로 유지)
├── tests/ (그대로 유지)
└── scripts/
```

**문제점:**
- Root에 12개 .md가 산재
- Canonical spec이 3개 버전으로 혼재
- docs/가 날짜별로 쪼개져 있어 추적 어려움
- 실험과 결과가 분리 안 됨
- registry 없음
- ID 체계 없음
- 의존 관계 명시 없음

---

## 목표 구조 (Research OS)

```
Perception_theory/
├── 00_meta/ ..................... 헌법 & 운영 규칙
│   ├── project_manifest.md
│   ├── ontology.md
│   ├── naming_convention.md
│   ├── status_codes.md
│   ├── promotion_rules.md
│   ├── CLAUDE.md (이동)
│   ├── CONVENTIONS.md (이동)
│   └── agent_protocols/
│       ├── claude_code_system_prompt.md
│       ├── proof_agent_protocol.md
│       ├── critic_agent_protocol.md
│       ├── experiment_agent_protocol.md
│       └── archivist_agent_protocol.md
│
├── 01_canonical/ ............... 현재 정본
│   ├── canonical_latest.md
│   ├── canonical_version_1.0.md
│   ├── canonical_version_1.1.md
│   ├── canonical_version_1.2.md
│   └── release_notes/
│       ├── v1.0_release_note.md
│       ├── v1.1_release_note.md
│       └── v1.2_release_note.md
│
├── 02_roadmap/ .................. 전체 조망
│   ├── master_problem_map.md
│   ├── dependency_graph.md
│   ├── open_problems.md
│   ├── resolved_problems.md
│   ├── abandoned_paths.md
│   └── milestones/
│       ├── M1_foundations.md
│       ├── M2_formalism.md
│       └── M3_validation.md
│
├── 03_context_memory/ ........... 용어 & 기호 헌법
│   ├── concept_registry.md
│   ├── symbol_registry.md
│   ├── theorem_registry.md
│   ├── assumption_registry.md
│   ├── notation_decisions.md
│   └── glossary.md
│
├── 04_daily_log/ ............... 연구 운영 로그 (날짜별)
│   ├── 2026-04-12.md
│   ├── 2026-04-13.md
│   └── ...
│
├── 05_questions/ ............... Q-xxxx 문제 정의
│   ├── Q-0001_foundational_cohesion.md
│   ├── Q-0002_boundary_definition.md
│   └── ...
│
├── 06_claims/ .................. C-xxxx 주장
│   ├── C-0001_main_theorem.md
│   ├── C-0002_closure_consistency.md
│   └── ...
│
├── 07_proofs/ .................. P-xxxx 증명 시도 (폴더형)
│   ├── P-0001_main_theorem_proof/
│   │   ├── overview.md
│   │   ├── proof_attempt_v1.md
│   │   ├── proof_attempt_v2.md
│   │   ├── lemma_candidates.md
│   │   ├── failure_analysis.md
│   │   └── references.md
│   └── ...
│
├── 08_counterexamples/ .......... X-xxxx 반례 & 붕괴 기록
│   ├── X-0001_counterexample_to_C-0002.md
│   └── ...
│
├── 09_experiments/ ............. E-xxxx 실험 & 계산 검증
│   ├── E-0001_symbolic_check/
│   │   ├── spec.md
│   │   ├── run_001/
│   │   ├── run_002/
│   │   └── summary.md
│   └── ...
│
├── 10_results/ ................. R-xxxx 결과 & 해석
│   ├── R-0001_support_for_C-0001.md
│   ├── R-0002_failure_pattern.md
│   └── ...
│
├── 11_papers/ .................. 출판물
│   ├── outlines/
│   ├── sections/
│   ├── figures/
│   ├── bibliography/
│   └── drafts/
│
├── 12_discussions/ ............ DISC-xxxx 개념 논쟁 & 철학
│   ├── DISC-0001_why_boundary_relational.md
│   └── ...
│
├── 13_archive/ ............... 폐기되었으나 보관 필요
│   ├── deprecated_claims/
│   ├── failed_paths/
│   ├── old_canonical/
│   ├── old_docs_migrated/ (기존 docs/03-26~04-12를 여기로)
│   └── merged_notes/
│
├── 14_figures/ ................ 도식 & 개념도
│   ├── source/
│   ├── exported/
│   └── figure_registry.md
│
├── 15_scripts/ ................ 자동화 도구
│   ├── build_dependency_graph.py
│   ├── validate_headers.py
│   ├── find_unregistered_symbols.py
│   ├── promote_to_canonical.py
│   └── generate_registry_index.py
│
├── 99_templates/ .............. 문서 템플릿
│   ├── daily_log_template.md
│   ├── question_template.md
│   ├── claim_template.md
│   ├── proof_template.md
│   ├── experiment_template.md
│   ├── result_template.md
│   ├── canonical_template.md
│   └── discussion_template.md
│
├── scc/ ........................ 구현 (그대로 유지)
├── tests/ ..................... 테스트 (그대로 유지)
│
└── [옮겨질 docs/experiments/papers/plan/result] → 13_archive/ 또는 해당 폴더
```

---

## Phase 1: 메타 & 기초 설정 (00_meta, 03_context_memory)

### 1.1 00_meta/ 설정

**생성할 파일:**

1. `project_manifest.md`
   - 프로젝트 개요, 목표, 현재 우주론
   - 최근 critical problems 요약

2. `ontology.md`
   - SCC 세계관의 핵심 개념
   - 무엇이 primitive이고 무엇이 derived인가

3. `naming_convention.md`
   - ID 체계 명시
   - 파일명 규칙

4. `status_codes.md`
   - seed, draft, active, tentative, challenged, validated, accepted, deprecated, archived

5. `promotion_rules.md`
   - claim이 canonical이 되는 조건
   - 최소 요구사항 체크리스트

6. `agent_protocols/` (4개 파일)
   - 각 에이전트 역할과 제약

**이동할 파일:**
- CLAUDE.md → 00_meta/
- CONVENTIONS.md → 00_meta/

---

### 1.2 03_context_memory/ 설정 (Registry 초기화)

**생성할 파일:**

1. `concept_registry.md`
   
   ```markdown
   | ID | Name | Definition | Status | Used In | Notes |
   |----|------|-----------|--------|---------|-------|
   | D-0001 | Soft Cohesion Field | u_t : X_t → [0,1] | accepted | C-0001 | primitive |
   | D-0002 | Closure Operator | Cl_t | accepted | C-0001 | axiom A3 |
   | D-0003 | Distinction Operator | D_t | accepted | C-0001 | axiom D |
   | D-0004 | Boundary (new) | (to be defined) | tentative | C-0011 | from audit |
   | ... | ... | ... | ... | ... | ... |
   ```

2. `symbol_registry.md`
   - 기호 중복 방지

3. `theorem_registry.md`
   - 주장 & 정리 추적

4. `assumption_registry.md`
   - A-0001, A-0002 등 모든 가정

5. `notation_decisions.md`
   - 기호 선택 이유

---

## Phase 2: Canonical 정리 (01_canonical)

### 2.1 Canonical 버전 정리

**현재 상황:**
- Canonical Spec v2.0.md
- Canonical Spec v2.1.md
- Canonical Spec.md (symlink? 확인)

**재구성:**

1. `canonical_version_1.0.md`
   - 04-01 시점의 spec (원본)

2. `canonical_version_1.1.md`
   - 04-03 PLAN_0403 Tier 1 완료 후 (3개 Cat B→A 승격)

3. `canonical_version_1.2.md`
   - 2026-04-12 감시 후 수정 (명시적 가정 추가, F-1 응답)

4. `canonical_latest.md`
   - 관문 파일 (현재 읽을 파일 지시)

5. `release_notes/`
   - v1.0, v1.1, v1.2 각각에 대해 무엇이 바뀌었는가

---

## Phase 3: Roadmap 구성 (02_roadmap)

### 3.1 현재 docs/에서 추출

**master_problem_map.md 작성:**
- 전체 문제 계층도
- Q-0001, Q-0002, ... 등 매핑

**dependency_graph.md 작성:**
- D-0001 → D-0004 → C-0011 → P-0008 → R-0003 → CV-1.2 흐름

**open_problems.md 작성:**
- OP-0001: F-1 "K=2 vacuous" (critical)
- OP-0002: M-1 "K=1 preferred" (critical)
- OP-0003: MO-1 "Morse theory fails" (critical)
- ... (기존 docs/에서 추출)

---

## Phase 4: Daily Log 초기화 (04_daily_log)

### 4.1 기존 docs/를 daily_log로 변환

```
기존: docs/04-07/analysis/, docs/04-07/proof/, docs/04-07/synthesis/
새로: 04_daily_log/2026-04-07.md

2026-04-07.md 구조:
## Today's objective
- [from docs/04-07 INDEX]

## Worked on
- P-0008 (proof)
- E-0005 (experiment)

## Decisions made
- Type A vs Type B 분류 시도

## New artifacts created
- Type classification framework

## Broken paths discovered
- Type B 관찰 실패

## Promotion candidates
- (none yet)

## Next actions
- exp65 검증

## References
- ../13_archive/old_docs_migrated/04-07/
```

---

## Phase 5: 기존 docs 마이그레이션 (13_archive)

### 5.1 docs/03-26~04-12를 archive로 이동

```
13_archive/old_docs_migrated/
├── 2026-03-26/
├── 2026-03-27/
├── 2026-03-30/
├── 2026-03-31/
├── 2026-04-01/
├── 2026-04-02/
├── 2026-04-03/
├── 2026-04-04/
├── 2026-04-06/
├── 2026-04-07/
├── 2026-04-10/
├── 2026-04-11/
└── 2026-04-12/

각 폴더 내부에 INDEX.md 추가:
"이 폴더의 내용은 새로운 Research OS 구조로 마이그레이션되었습니다.
참조: 04_daily_log/2026-04-07.md, 02_roadmap/open_problems.md 등"
```

---

## Phase 6: Questions, Claims, Proofs 구조화 (05-07)

### 6.1 기존 claims 추출 & ID 부여

```
기존: "K=2가 안정적인가?" → 여러 docs에 산재
새로: 
  Q-0001_k_field_stability.md
  C-0001_k_field_global_minimum.md
  P-0001_k_field_global_minimum/
    ├── overview.md
    ├── proof_attempt_v1.md (04-01)
    ├── proof_attempt_v2.md (04-03)
    ├── failure_analysis.md (04-06 critic)
    ├── hidden_dependencies.md
    └── references.md
  X-0001_counterexample_k_equals_1_cheaper.md
  E-0001_energy_landscape_check/
  R-0001_empirical_support.md
```

### 6.2 Phase 4 critical problems 변환

```
OP-0001: F-1 "K=2 vacuous" 
  → Q-0002_why_k2_if_k1_cheaper.md
  → C-0002_k_selection_model.md (아직 없음)
  → P-0002_... (미증명)

OP-0002: M-1 "K=1 always preferred"
  → Q-0003_isoperimetric_ordering.md
  → C-0003_isoperimetric_bound.md
  → P-0003_... (부분 증명)

OP-0003: MO-1 "Morse theory fails"
  → Q-0004_stratified_morse_framework.md
  → (아직 형식화 안 됨)
```

---

## Phase 7: Experiments & Results 분리 (09-10)

### 7.1 기존 experiments/results 재분류

```
기존: experiments/exp62_f_double_prime.py, experiments/results/exp62_....json

새로:
09_experiments/
├── E-0001_energy_landscape_sweep/
│   ├── spec.md (exp62)
│   ├── run_001/
│   └── summary.md
└── E-0002_hessian_direct_test/
    ├── spec.md (exp63)
    └── run_001/

10_results/
├── R-0001_f_double_prime_analysis.md (exp62/63 결과)
├── R-0002_type_ab_classification_failure.md (exp65 결과)
└── R-0003_empirical_energy_costs.md
```

---

## Phase 8: Papers 정리 (11_papers)

### 8.1 기존 papers/ → 11_papers/

```
11_papers/
├── paper1_math.tex (기존 papers/)
├── paper2_cogsci.tex (기존 papers/)
├── outlines/
├── sections/
├── figures/
└── bibliography/
```

---

## Phase 9: Scripts & Automation (15_scripts)

### 9.1 생성할 자동화 도구

```python
# build_dependency_graph.py
# - 모든 md의 depends_on 필드 읽기
# - mermaid DAG 생성
# - dependency_graph.md 자동 갱신

# validate_headers.py
# - 모든 md 파일 header 검사
# - 누락된 id, type, status 찾기

# find_unregistered_symbols.py
# - 문서에 등장한 C-xxxx, P-xxxx 등이 registry에 있는지 확인

# promote_to_canonical.py
# - claim → canonical 승격 체크리스트 자동 실행
```

---

## Phase 10: Templates 작성 (99_templates)

### 10.1 각 문서 타입별 템플릿

```markdown
daily_log_template.md
question_template.md (Q-xxxx)
claim_template.md (C-xxxx)
proof_template.md (P-xxxx)
experiment_template.md (E-xxxx)
result_template.md (R-xxxx)
```

---

## 마이그레이션 체크리스트

### 파일 이동 요약

| 현재 위치 | 새 위치 | 작업 | 파일명 변경 |
|-----------|--------|------|-----------|
| `/Canonical Spec v2.1.md` | `/01_canonical/canonical_version_1.2.md` | 이동 & 수정 | Yes |
| `/CLAUDE.md` | `/00_meta/CLAUDE.md` | 이동 | No |
| `/CONVENTIONS.md` | `/00_meta/CONVENTIONS.md` | 이동 | No |
| `/docs/` | `/13_archive/old_docs_migrated/` | 이동 | No (구조 유지) |
| `/experiments/` | `/09_experiments/` | 재구성 | Partial |
| `/papers/` | `/11_papers/` | 이동 | No |
| `/plan/` | `/13_archive/old_plans/` | 이동 | No |

### 파일 삭제 금지 목록

- ✗ 삭제 금지: 모든 기존 .md, 모든 docs/ 폴더
- ✓ 이동: 13_archive로 이동
- ✓ 재구성: 새 구조에 맞춰 폴더/파일 정리

---

## 실행 순서

### 즉시 (계획 확정 후)
1. Phase 1: 00_meta, 03_context_memory 폴더 생성 & 초기 파일 작성
2. Phase 2: 01_canonical 폴더 생성 & canonical 정리

### 다음 세션
3. Phase 3-4: 02_roadmap, 04_daily_log 생성
4. Phase 5: 기존 docs/ → 13_archive/ 이동
5. Phase 6-7: 05-10 폴더 생성 & 기존 claims/proofs/experiments 재구성
6. Phase 8-10: papers, scripts, templates

### 최종
- CLAUDE.md 수정 (새 구조 안내)
- CHANGELOG.md 기록

---

## 주의사항

1. **ID 충돌 방지**: 기존 주장들을 어떤 ID로 매핑할지 미리 정하기
2. **Registry 정확성**: concept_registry가 매우 중요 → 신중히
3. **Canonical 버전**: v1.0, v1.1, v1.2 중 어느 것이 "현재 믿을만한 정본"인가?
4. **Daily log 자동화**: 기존 docs를 모두 daily log로 변환하는 스크립트 필요?

---

## 예상 시간

- Phase 1-2: 2시간
- Phase 3-4: 2시간
- Phase 5-7: 3시간
- Phase 8-10: 1시간
- **총 8시간 (2-3회 세션)**

---

**다음 단계:** 이 계획이 적절한가? 수정 필요?
