---
type: log/daily/plan
date: 2026-05-14
session_label: W7-Day5 — OQ-H decision + 실제 작업 진입
canonical_version: CV-1.13 (sealed, untouched)
prerequisite: 01_pre_brainstorm.md 읽기 (또는 사용자 직접 결정)
---

> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]


# 00 — Plan (2026-05-14)

## Context

5/13 의 두 archive (V-AFD + R-2) 후속. 어제 99_summary.md Blocks H-K + 두 archive note 가 권장한 다음 방향은 state report §7.5 **Roadmap C 정면 공격**. 그러나 두 archive 가 모두 "language refactoring → archive" 패턴을 보였으므로, 곧장 정공법 진입이 *세 번째 archive 위험* 인지 sanity check 필요.

이번 plan 의 deliverable 은:
1. OQ-H (5/13 추가 OQ) 결정사항 명시화.
2. 선택된 트랙의 첫 step 명시.
3. 4-6주 timeline 의 거친 schedule.
4. 세 번째 archive 위험 회피 규약.

01_pre_brainstorm.md 의 결론에 따라 어느 옵션이든 받아들일 수 있도록 모든 옵션의 첫 step 을 사전 정의.

---

## Options (5/13 99_summary OQ-H, 5/14 진입점 결정)

### Option A — H-MORSE Cat A 정면 공격 (Roadmap C 1)

**Target.** canonical critical-point Hessian 의 양정성 (positive definiteness) 일반 증명. 현재 ~Cat B 수치 지지 (μ_min ∈ [0.96, 60.2] 모든 tested config) 가 있으나 일반 증명 부재.

**Rationale.** state report §7.5 권장 1순위. P-F-A1 Package I 전체 Cat A (canonical) 이 Package II 진입의 토대를 마련함 → SDE 존재 + Gibbs 불변 + Poincaré 부등식. Package II = Eyring-Kramers prefactor = Hessian determinant 필요.

**First step (5/14 첫 작업).**
- `THEORY/working/SF/sigma_m_hessian_convention_audit.md` 열어서 prerequisite 점검.
- Allen-Cahn Morse 전이 문헌 (Bates-Fife-Wang 1997, Fei-Wang-Zhou 2019) + T7-Enhanced Cat A 결합 가능성 평가.
- 5/14 종료까지: H-MORSE 일반 증명 *시도 가능* 한 lemma 구조 (P-Hessian-Reg + P-Spectrum-Lower 등 ~3-5 lemmas) 의 working draft.

**Risk.** H-MORSE 자체가 까다로움 — D-4-symmetric minimizer, Goldstone family, T8-Full 분기점 등에서 *적극적으로 violations*. 일반 증명 불가능할 수 있음.

**Mitigation.** Path B (H-MORSE-Local Cat B target — M-A1/M-A2/M-A3 조건부) 로 graceful degradation. 일반 Cat A 가 어려우면 조건부 Cat B 로 진입.

### Option B — OP-0008-MERGE-σ Wigner-projection Cat C → Cat B (Roadmap C 4)

**Target.** σ_standard post-merge inheritance 의 Wigner-projection theorem. canonical W9+ 가 현재 blocker.

**Rationale.** Q6 σ-Inheritance 의 *핵심 미해결*. R-2 가 archive 되었지만 R-2 의 stratification insight (centroid+orientation Cat B / σ_standard Cat C) 가 정직한 분류였음을 보여줌. canonical OP-0008-MERGE-σ part c 직격.

**First step.**
- `THEORY/working/MF/sigma_inherit_k_jump.md` §3.3(d) + `THEORY/working/MF/sigma_rich_phi_proof.md` Conjecture 8.1 정독.
- Wigner-von Neumann avoided-crossing theorem 의 SCC 변형 가능성 평가.
- 5/14 종료까지: Cat C → Cat B 시도의 working draft (lemma structure proposal).

**Risk.** Wigner-projection 자체가 어려운 수학 — H-MORSE 보다 *더* 어려울 수 있음. Σ_m 상의 reflected-Langevin EK adaptation 미해결.

**Mitigation.** 5/14 단일 세션에서 Cat C→B 완결은 비현실. 첫 lemma 정도 시도.

### Option C — OP-0021 T_* 정규 등록 (Roadmap C 2)

**Target.** T_* 정규화 — Mori-Zwanzig route 5 gap closure 또는 RG fixed-point route.

**Rationale.** Package II 진입 조건. H-MORSE 와 병렬로 진행 가능. state report §3.3 에서 OP-0021 PARTIAL OPEN.

**First step.**
- 5/13 state report 의 OP-0021 5 gap 검토.
- Mori-Zwanzig NOP-F / NOP-J 중 가장 가벼운 gap 식별.
- 5/14 종료까지: 1개 gap 의 부분 해결 시도.

**Risk.** OP-0021 도 H-MORSE 만큼 까다로움. 5/14 single session 으로는 부분 진척만 가능.

### Option D — CV-1.15 P7 promotion turn (오전 작업 완성)

**Target.** 5/13 오전 작업의 closure. `04_proposed_amendments.md` §F apply-order 실행 → canonical/theorem_status/hypothesis_tree/CHANGELOG 직접 수정.

**Rationale.** 오전 작업이 P7 만 남은 상태로 보류됨. Roadmap C 작업과 *별도 트랙* 이며, 단일 세션 내 완결 가능.

**First step.**
- 사용자에게 P7 명시적 허가 요청.
- 허가 후 §F apply-order 6 step 실행 + Block D post-patch consistency audit.
- CV-1.15_SEAL.md 작성.

**Risk.** P7 미허가 시 진행 불가. 사용자 결정 의존.

### Option E — Deeper pre-brainstorm (deferred decision)

**Target.** 두 archive 직후의 정직한 자기 평가 후 5/15 에 트랙 결정.

**Rationale.** V-AFD + R-2 두 번의 ~24h archive 사이클 직후, 곧장 정공법 진입이 *세 번째 archive 위험* 일 가능성. 더 깊은 pre-brainstorm 으로 진정한 막힘 위치 식별 + ETA 평가.

**First step.**
- 01_pre_brainstorm.md 를 *full session 분량* 으로 확장 (300줄 → 800+줄).
- DECL-1.0 Q1-Q6 의 *수학적 어려움 분석* (각 Q 의 미해결 도구 + ETA).
- Roadmap C 4-6주 schedule 의 정직한 평가.
- 5/14 종료까지: 5/15 의 명시적 트랙 결정.

**Risk.** *또 다른 메타-우회* 위험. 두 archive 의 lesson 이 "더 phenomenology 하지 말고 정공법" 이라면, Option E 자체가 세 번째 우회.

---

## 권장 (pre-brainstorm 결과 의존)

**01_pre_brainstorm.md 의 §6 권장** 에 따라 결정. 본 plan 은 모든 옵션의 first step 을 사전 정의하므로 어느 결정이든 즉시 진행 가능.

**Default (사용자 별도 결정 없을 시):** Option E (deeper pre-brainstorm) → 5/15 에 정식 트랙 결정. 두 archive 직후 곧장 정공법 진입의 위험을 한 번 더 sanity check.

**보수적 alternative:** Option D (CV-1.15 P7 promotion) — Roadmap C 와 무관한 *closure 작업*. 5/14 single session 완결 가능. 두 archive 의 학습 없이 즉시 가치 생산.

**적극적 alternative:** Option A (H-MORSE Cat A) — Roadmap C 정공법. 두 archive note 의 공통 권장. *세 번째 archive 위험* 을 받아들이면서 진입.

---

## Decision gate (어느 옵션이든 적용)

| 검사 | 통과 기준 |
|---|---|
| **언어 재조직 회피** | "새 명칭 / 새 reframe / 새 framework" 일체 금지. 작업은 canonical 기존 어휘 위에서. |
| **canonical alignment 사전 검사** | 새 lemma 시도 전 `canonical.md` + `theorem_status.md` + 관련 `working/MF/` 또는 `working/SF/` 등에서 동일 / 유사 content 의 존재 grep 필수. |
| **수치 demo 의무화** | 새 Cat B / Cat A 주장 시 *반드시* numerical verification (canonical 15×15 또는 적절한 substrate) 동반. |
| **Cat 상태 정직 표기** | PROVED / SKETCH / CONJECTURE / OPEN — definitional tautology 를 PROVED 로 표기 금지. |
| **5/15 또는 그 이후 외부 audit** | 5/14 작업의 결과물에 대해 R-2 의 Round 4 Explore alignment audit 패턴 적용 — *canonical working content 와의 alignment* 별도 검사. |

세 번째 archive 위험 방지의 *operational rule*.

---

## Timeline (Roadmap C 기준, 4-6 주)

```
Week 1 (5/14 ~ 5/20): Option A or B 진입, 첫 lemma 1-2개 working draft
Week 2 (5/21 ~ 5/27): 첫 lemma 의 Cat B 시도 + Round 4 외부 alignment audit
Week 3 (5/28 ~ 6/3):  Cat B 완결 + Cat A 시도
Week 4 (6/4 ~ 6/10):  Cat A 외부 audit + canonical promotion candidate
Week 5-6 (6/11 ~ 6/24): P7 promotion turn 시도 (사용자 결정 의존)
```

ETA: 첫 Cat B 결과 ~2주, 첫 Cat A ~4-6주. 두 archive lifetime (각 ~24h) 와 *완전히 다른 timeline* — 정공법은 오래 걸림.

---

## Out-of-scope (5/14)

- V-AFD 또는 R-2 부활 / vocabulary 추출 (시기상조)
- AFD-0 modification (working layer 보존)
- 새 R-2-like working folder 생성 (세 번째 archive 위험)
- DECL-1.0 수정 (foundational)
- canonical/theorem_status/hypothesis_tree 직접 수정 (P7 별도)

---

## Files written (planned)

| 파일 | 작성 시점 |
|---|---|
| `00_index.md` | 세션 시작 ✓ |
| `00_plan.md` (이 파일) | 세션 시작 ✓ |
| `01_pre_brainstorm.md` | OQ-H 결정 *전* |
| `02_*.md` ~ `09_*.md` | OQ-H 결정 *후*, 선택된 트랙에 따라 |
| `99_summary.md` | 세션 종료 시 |

---

*5/14 의 first principle: 두 archive 의 lesson 보존. 언어 재조직이 아닌 수학적 정공법. Cross-reference canonical alignment 의무화.*
