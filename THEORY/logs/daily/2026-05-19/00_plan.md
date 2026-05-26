---
type: log/daily/plan
date: 2026-05-19
session_label: W8-Day2 (Tue) — T_*/H5 Deep Work (U-잔류 2항 고도화/증명/정리방법 모색)
mode: deep-attack — H5 (spinodal Goldstone mode degeneracy) primary; T_* (fixed-point) secondary
canonical_version: CV-1.17 (sealed 2026-05-15, untouched 예정)
predecessor: 2026-05-18 AUX-1.5 END-OF-DAY (auxiliary_structures_master.md AUX-1.0→1.5 통합)
strategic_plan: 폐기됨 — 기존 W8-Day2 OP-0008 perturbation 작업은 `_archive_W8Day2_obsolete_00_plan.md` 로 보존. 본 plan이 신 mission.
prompt_body: MAIN_PROMPT_v3.md
output_files:
  - 00_index.md  # 갱신
  - 00_plan.md   # 본 파일
  - 01_pre_brainstorm.md  # 선택 (사용자 직접)
  - 02_H5_morse_spinodal.md  # Primary working file
  - 03_T_star_fixed_point.md  # Secondary working file
  - 04_AUX-1.6_amendment.md  # 선택 — H5/T_* status update
  - 99_summary.md
cot_enforcement_level: strict
coc_enforcement_level: strict
expected_session_count: 1
---

> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]] · [[00_index]] · [[../2026-05-18/99_summary|어제 99_summary]] · [[auxiliary_structures_master|AUX-1.5 registry]] · [[MAIN_PROMPT_v3]]

# 00 — Plan (2026-05-19, W8-Day2)

## Mission

어제 (2026-05-18) AUX-1.0 → AUX-1.5 의 5번 amendment로 auxiliary structures registry 통합 마감. **2개의 진정한 U 잔류:**

- `T_*` (effective stochastic temperature) — fixed-point 구조 (자기-참조 순환)
- `H5` (Morse stability) — spinodal Goldstone mode degeneracy

**오늘 mission (사용자 지시):**
> "U — T_* (fixed-point 구조), H5 (spinodal Goldstone mode degeneracy). 이거 두개 고도화 및 증명 및 정리방법 모색"

3 목표 × 2 항목 = 6 작업:
1. 고도화 (refinement) — 수학적 정확한 formulation
2. 증명 시도 (proof attempts) — 구체적 경로
3. 정리 방법 모색 (theorem formalization route) — 적절한 framework 선택

**순서:** H5 먼저 (more concrete: Morse + bifurcation + stratification), T_* 다음.

---

## Context (왜 오늘 이 작업인가)

### 2026-05-18 마감 상태 (predecessor)

AUX-1.0 → AUX-1.5 (5 amendments):
- 65+ 항목 분류: D ~30 / A ~25 / P ~18 / Hybrid 2 / External input 1 / **U 잔류 2**
- registry size 0 → 1141 lines
- canonical 본문 0 수정
- 클레임 카운트 불변 (어제 AUX 작업 시 "83" 기준; 본 plan은 *현재 canonical state* 와 화해 필요 — §11 verification 참조)
- 후보 1=2=3 가설 (세 후보가 동일 균열의 세 얼굴) 문서적 증명

### 두 잔류 U의 의미

두 잔류 U가 *우연*이 아니라 SCC 이론의 *진짜 핵심 사건* 과 직결:

- `T_*` = 관찰자가 무엇을 noise로 처리하는가 (인식 메커니즘 자체)
- `H5` = 균질에서 분화가 일어나는 바로 그 순간 (perception의 기원)

→ 본 day의 작업은 *registry 작업* (어제) 에서 *theory 작업* (오늘) 으로 전환. SCC 이론의 진짜 미해결에 처음으로 *형식적으로* 접근.

### Entry state (2026-05-19 morning)

- CV-1.17 SEALED (2026-05-15 evening, untouched).
- 클레임 카운트: 이전 카탈로그 reference. 정확한 현재값은 §11 verification 항목 #1.
- AUX-1.5 registry: 1141 lines, T_*/H5 두 항목만 U 잔류.
- pytest 225 passed + 1 xfailed.
- 어제 W8 strategic plan의 OP-0008 perturbation 작업은 **폐기됨**. T_*/H5 작업이 대치.

---

## §A. H5 — Spinodal Goldstone Mode Degeneracy (PRIMARY, ~3.5h)

### A.1 현 상태 진단

- **Statement (canonical):** 임계점 (saddle/min) 이 perturbation `ε·R` 하에서 stable.
- **출처:** theorem_status.md L373; canonical.md L1831 부근. T-P-F-ε0-K (Cat B conditional) 의 마지막 조건.
- **AUX-1.5 §4.9.5 시도 결과:**
  - Generic regime: Morse via Sard transversality (D 가능성).
  - Spinodal critical surface: Hessian *intrinsically* zero eigenvalue (Goldstone mode 자체가 formation을 트리거).
  - Codimension-1 surface 위에서 Sard 실패.

### A.2 고도화 — 정확한 formulation

**Target statements (drafts to refine):**

**A.2.1 Generic Morse:** SCC 에너지 `E_λ(u) = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd` (static face `λ_tr = 0`) 는 `(λ, α, β, m)` parameter space의 *open dense* 부분집합에서 critical points가 Morse.

**A.2.2 Spinodal stratum:** Hessian degeneracy locus `Σ_Hess = {det H_T = 0}` 는 T8 phase transition surface와 *일치* (canonical.md L2496 SB7 이미 Cat A). 이 surface는 codim-1.

**A.2.3 Stratified Morse on post-bifurcation:** Post-bifurcation regime (T8 supercritical, `β/α > 4λ₂/|W''(c)|`) 의 stable basin에서 모든 critical points는 *generically* Morse.

### A.3 증명 경로 후보

| 경로 | 도구 | Pro | Con / Risk |
|---|---|---|---|
| **P1: Sard's transversality** | Sard 1942, Federer 1969 | 가장 가벼움; Cat A 후보 명확 | SCC E의 polynomial form이 Sard 가정 모두 만족하는지 확인 필요 |
| P2: Equivariant Morse | Bott 1954, Atiyah-Bott 1984 | 표준 도구 | SCC에서 Aut(G)가 보통 작거나 trivial — 항상 적용 가능 X |
| P3: Crandall-Rabinowitz fold | Crandall-Rabinowitz 1971 | SN3 (canonical L2502) 와 직결 | (SN-iii)+(SN-iv) genericity 조건 미증명 (OP-OMS-033b OPEN) |

**권장:** P1 우선; P2, P3은 auxiliary support.

### A.4 정리 방법 모색

| Option | 형식 | 권장 여부 |
|---|---|---|
| **F1: Generic Morse + spinodal stratum split** | Cat A regime = post-bifurcation stable basin (codim-0 open) ∪ spinodal critical surface (codim-1) | **권장** — 가장 가볍고 Cat A 경로 명확 |
| F2: Goresky-MacPherson stratified Morse | Whitney stratification + Morse on each stratum | F1 실패 시 fallback |
| F3: Catastrophe theory (Thom-Mather) | T8 spinodal = cusp/fold catastrophe | 보조 도구 |
| F4: Hopf bifurcation analog | Formation = symmetry-breaking bifurcation | 직관적 motivation |

### A.5 산출물

- **02_H5_morse_spinodal.md** (~200-300 lines):
  - §1 Statement (A.2.1–A.2.3 draft)
  - §2 P1 (Sard) sketch — Cat A 후보 증명 개요
  - §3 P2/P3 비교 — auxiliary support
  - §4 OP-H5-MORSE-SPINODAL draft (formal statement for canonical registration)
  - §5 T-P-F-ε0-K regime restriction draft (post-bifurcation stable basin 한정)

---

## §B. T_* — Fixed-Point Structure (SECONDARY, ~1.5h)

### B.1 현 상태 진단

- **Statement (canonical):** Effective stochastic temperature parameter in P-F-A1.
- **출처:** canonical.md §13 P-F-A1 family. OP-0021 OPEN (Mori-Zwanzig, RG fixed point — 둘 다 COB 위반).
- **AUX-1.5 §4.9.1 시도 결과:**
  - Fixed-point 구조: `T_* → π_{T_*} → Var → T_*`. 자기-참조 순환.
  - 일관 fixed-point가 *원리적으로* 존재 가능하나 *유일성* 미보장 (multi-well E에서 multiple fixed-points 가능).
  - Route C (관찰자-개인 stochastic resolution → P) 권장 — COB 통과.

### B.2 고도화 — 정확한 formulation

**Target statements:**

**B.2.1 Fixed-point map:** Define `ψ : T → ⟨(u − ⟨u⟩)²⟩_{π_T}` where `π_T(u) ∝ exp(-E(u)/T)`. Fixed point: `T_* = ψ(T_*)`.

**B.2.2 Existence (Brouwer):** ψ continuous on `[T_min, T_max]` + Brouwer's theorem → fixed point exists.

**B.2.3 Multiplicity:** SCC E is multi-well (formation regime) → potentially multiple T_*. *Uniqueness 미증명*.

**B.2.4 Observer Route C:** T_* as observer's internal noise scale (free parameter). No fixed-point constraint — T_* is *axiomatically free*. Class **P** (ξ resident).

### B.3 증명 경로 후보

| 경로 | 도구 | Pro | Con / Risk |
|---|---|---|---|
| **P1: Brouwer fixed-point** | Brouwer 1911, Schauder 1930 | 표준; existence Cat A 가능 | Uniqueness 미증명; multiple fixed-points 가능 |
| P2: Mean-field self-consistency | 통계역학 표준 | 표준 도구 | SCC가 closed system 가정 부적절 (관찰자 정보 제공) |
| P3: Information-theoretic capacity of T | Shannon-Hartley 류 | T (Stage 0) 와 직결 | T 자체 미등록 (Stage 0 §4.5) |
| **P4: Observer free parameter (Route C)** | COB framework | 가장 가벼움; COB 통과; P 분류 | "어떤 T_*도 OK" 가 너무 약함 — 대표성 살려야 |

### B.4 정리 방법 모색

| Option | 형식 | 권장 여부 |
|---|---|---|
| G1: Route C (P axiomatically free) | T_* 자유 매개변수 (관찰자 선택) | 가장 가벼움 |
| G2: Brouwer fixed-point | T_* fixed-point의 한 점; *uniqueness 없음* 명시 | OP 등록용 |
| G3: Information-theoretic | T_* = T (Stage 0) 의 함수 | Stage 0 §4.5 9-조건에 흡수 가능 |
| **G1 + G3 hybrid** | T_* ∈ B_{T_*}(T) — T에 의존하는 *범위* 안에서 관찰자 자유 | **권장** |

### B.5 산출물

- **03_T_star_fixed_point.md** (~150-250 lines):
  - §1 Statement (B.2.1–B.2.4 draft)
  - §2 P1 (Brouwer) sketch
  - §3 P2/P3/P4 비교
  - §4 OP-T*-FIXED-POINT draft (formal statement)
  - §5 Route C 정식화 (G1 + G3 hybrid)
  - T_* ↔ T (Stage 0) 의존성 명시

---

## §C. 작업 흐름 (Time Allocation)

| Step | 작업 | 시간 |
|---|---|---|
| 1 | H5 working file 작성 (P1 Sard 경로 sketch) | ~2h |
| 2 | T-P-F-ε0-K regime restriction draft (H5 결과 사용) | ~1h |
| 3 | T_* working file 작성 (Brouwer + Route C) | ~1.5h |
| 4 | Cross-reference (H5 ↔ T_*, AUX-1.5 §4.7.1 ξ catalog) | ~30min |
| 5 | (선택) AUX-1.6 amendment 또는 EOD summary | ~30min |

**총 ~5.5h.**

---

## §D. 비실행 약속 (out of scope)

- **canonical 본문 0 수정.** working 단계만.
- **클레임 카운트 변경 없음.**
- **새 정리 promote 없음.**
- **OP catalog 본문 수정 없음** — OP-T*-FIXED-POINT, OP-H5-MORSE-SPINODAL은 *draft*만.
- **본격 Cat A 증명 완성 시도하지 않음** — sketch + Cat A 후보 경로 명시까지.
- **Goresky-MacPherson stratified Morse 전면 적용 안 함** — Option F1 우선.
- **Brouwer uniqueness 시도 안 함** — existence만; multi-well 다중성은 *open*으로 명시.

---

## §E. 후속 결정 (사용자 별도 결정 — 오늘 작업 후)

1. **AUX-1.6 amendment** — H5/T_* status를 registry §4.6 / §4.9에 update.
2. **theorem_status.md working candidate 등록** — `T-H5-MORSE-GENERIC` (Cat A 후보), `T-T*-EXIST-FP` (Cat B 후보).
3. **canonical OMS-1 amendment 시작** — T_* Route C를 OMS-1의 ξ resident로 정식 등록.
4. **OP-0021 본문 수정** — Route C를 OP-0021에 추가, Route A/B 폐기 명시.
5. **OP-H5-MORSE-SPINODAL 정식 등록** — canonical Open Problems Catalog 본문 수정.

---

## §11. Verification (구현 후 readback)

```bash
# 1. 현재 canonical state 확인 (어제 AUX 작업이 stale reference에 기반했는지 검증)
grep -nE "current = \*\*CV-|claims" THEORY/2_substrate/canonical/theorem_status.md | head -10

# 2. Working files 존재
ls -la THEORY/logs/daily/2026-05-19/02_H5_morse_spinodal.md
ls -la THEORY/logs/daily/2026-05-19/03_T_star_fixed_point.md

# 3. canonical.md mtime 불변
ls -la THEORY/2_substrate/canonical/canonical.md | awk '{print $6, $7, $8}'

# 4. 본 plan 파일 frontmatter
head -25 THEORY/logs/daily/2026-05-19/00_plan.md

# 5. AUX-1.5 마감 보존
grep -n "AUX-1.5" THEORY/2_substrate/canonical/auxiliary_structures_master.md | head -3
```

---

## §F. 메타 노트

AUX-1.0~1.5는 *registry 작업* (등록 + 분류). 오늘은 *theory 작업* (mathematical content).

오늘 작업의 목표:
1. 두 미해결이 *진짜로* 무엇인지 수학적으로 분리.
2. 각각의 정리 가능 / 정리 불가능 경계를 *명시*.
3. 가능한 부분 (generic Morse, Brouwer fixed-point existence) 의 Cat A 경로 sketch.
4. 불가능한 부분 (spinodal degeneracy intrinsic, T_* uniqueness in multi-well) 을 *명시적 OP*로 등록.

**SCC 이론의 *진짜 미해결*에 처음으로 *형식적으로* 접근하는 day.**

---

## §G. Archived

- `_archive_W8Day2_obsolete_00_plan.md` — 원래 W8-Day2 OP-0008 perturbation plan (18KB). 사용자 지시로 폐기 (2026-05-18 EOD). 본 plan으로 대치.
