# Reformulation Purpose (Stage 0 Locked)

**Selected:** C+E (Thermal Framework + Emergent-K)
**Decision date:** 2026-04-20
**Decision path:** Decision Tree (`logs/daily/2026-04-20/03_integration_and_new_open.md` §12) — Q-α YES (향후 6 개월 내 metastability claim 가능) → Q-β YES (soft-K framework 도 원함) → **C+E**.
**Estimated scope:** 17 세션 (Matrix-1 완전해결 6, Matrix-2 Cat A 상실 5~6).
**Stage 1 entry:** 2026-04-21 (C+E 공통 첫 세션 plan: `logs/daily/2026-04-21/plan.md` + `pre_brainstorm.md` 104 가설).

---

## 한 줄 선언문

K 를 H₀ persistence 기반 **derived soft quantity** 로 재정의하고 (E), 유한 온도 Gibbs framework `ℱ = ℰ − T·S` 를 편입하여 (C), **Soft-Hard Switching Asymmetry (N-1) 의 K 얼굴 제거** 와 **Zero-T Metastability Claim 공백 (P-F) 해소** 를 단일 reformulation 으로 동시 달성한다.

---

## Rationale (5 bullets)

- **Matrix-1 최대 완전해결 6** — F-1 (OP-0001), M-1 (OP-0002), MO-1 (OP-0003), K-selection (OP-0005), Integer-K/Continuous-u Mismatch (P-A), Zero-T Metastability (P-F). 8 선택지 중 최다 (단일 후보 최대는 A/E 의 5, 조합 최대는 A+C/C+E 의 6).
- **M-1 과 MO-1 의 dissolution 이 C+E 하에서 E-only 대비 훨씬 강함** — Kramers rate `τ ~ exp(ΔE/T)` 의 엄밀 편입 + Witten Laplacian / Fokker-Planck / Morse-Bott / discrete Morse (Forman) 의 4 중 대안 도구 동시 획득.
- **기존 empirical 결과의 재해석 경로 열림** — exp38 barrier exponent `β^{0.89}`, exp55 zero-merge 가 Kramers prefactor (Hessian eigenvalue scaling) 으로 재유도 가능. "empirical fit" 에서 "thermodynamically derived prediction" 으로 격상.
- **Pareto frontier 중 "조합의 왕"** — 17 세션 / 완전해결 6 / Cat A 상실 5~6 / 순수 상호작용 +긍정 (`logs/daily/2026-04-20/03_integration_and_new_open.md` §3.2). A+C (21 세션) 를 weakly Pareto-dominate.
- **기존 CN6 "kinetically determined" 의 thermodynamic substantiation** — canonical `§14 CN6/CN8/CN14` 의 implicit commitment 를 F-group 공리 framework 내부로 흡수. 기존 커밋먼트 파기가 아니라 근거 강화.

---

## Non-goals (5+)

- **Threshold 얼굴 (P-D)** · **Axiom-Switching 얼굴 (P-G)** — N-1 의 나머지 두 얼굴은 out of scope. 본 cycle 이후 별도 reformulation cycle 에서 다룸 (`working/open_problems_reframing_2026-04-19.md` §8).
- **Self-Generating Substrate (P-B, Purpose D)** — long-term, 본 cycle 과 orthogonal. `X_t`, `N_t` 는 external input 으로 유지.
- **25+ 파라미터 Genealogy 전체 해소 (P-E)** — 본 cycle 에서는 **K 관련 파라미터** (K_max, λ_rep, K_soft weighting φ) 와 **T** 만 다룸. 나머지 (a_cl, β, η, ...) genealogy 는 후속.
- **Publication Timeline Pressure 없음** — v2.0 canonical release 는 C+E 전체 완료 (17 세션) 후. 본 cycle 중 학술 공개 계획 없음.
- **Third-Mode (C_t) 의 Energy 재진입 (NQ-2)** — C 의 F-group 작업 중 자연 만나면 언급하되 primary 목표 아님. C_t 의 demotion 은 CN7 커밋먼트로 유지.
- **§12 K-field 구조의 전면 retraction** — §12 는 soft-K 재작성 대상이지만 "K-field architecture 전체 폐기" 는 현재 commitment 아님. 재작성 후 결과 따라 결정.
- **Canonical.md 직접 수정** — 본 purpose 수행 중 모든 변경은 `canonical_sub.md` 에 daily append, 주 1 회 merge.

---

## 영향 받는 Canonical 섹션 (예상, §Stage 2 Axiom Audit 확정)

- **§3.3** (u 의 codomain) — K_soft 관련 codomain 변경 여부.
- **§5** (derived morphology) — K_soft 정의 추가.
- **§5.5** (transition diagnostics) — persistence stability 활용 확장.
- **§6 Group F (신설)** — thermal 공리 F1–F4.
- **§8.1** (energy functional) — `ℱ_C+E = ℰ − TS + λ_K K_soft` 로 확장.
- **§12 Multi-formation** — soft-K 언어로 전면 재작성.
- **§13 Cat A/B/C** — integer-K load-bearing 10 개 정리 (`working/integer_K_dependency_map.md`) 재분류:
  - Cat A Retire 5, Cat A Re-prove-retain 1, Cat B Retire 1, Cat C Re-prove 3.
  - 단일 formation Cat A 19~20 생존.
- **§14 CN6/CN8/CN14** — "kinetically determined" 의 thermodynamic 재해석.

---

## 17-세션 대략 분배 (Stage 1–6)

| Stage | 내용 | 세션 |
|---|---|---|
| 1 (Definition Foundation) | K_soft commit + F-group F1–F2 + ℱ_C+E well-def + 3 Critical dissolution mapping | 3 |
| 2 (Axiom Audit) | §6 F-group 확정, Group A–E 재검토, `working/integer_K_dependency_map.md` 정밀화 | 3 |
| 3 (Definition & Derivation) | F3 Langevin well-posedness, Kramers prefactor 유도, Witten semiclassical expansion | 4 |
| 4 (Theorem Rewrite) | T-Persist-K-Sep/Weak/Unified 재증명 (Cat C → Cat A), T-Merge (b) soft-K rewrite | 3 |
| 5 (Numerical Validation) | exp38/55 재해석 + 신규 exp77+ (Kramers prefactor prediction vs data) | 2 |
| 6 (Promotion) | §12 재작성, §13 재분류 적용, CN 업데이트, v2.0 release note | 2 |

**Stage 1 세션 3 개 계획:**
1. **2026-04-21** (plan.md 확정): C+E 공통 첫 — G1–G6 (K_soft + F1/F2 + ℱ_C+E + 3 Critical dissolution).
2. Stage 1 둘째 (날짜 미정): E-S2 §12 재작성 골격 + C-S2 Langevin well-posedness preliminary.
3. Stage 1 셋째 (날짜 미정): CE-S2 phase diagram (T, λ_K), NQ-1 후보 (ii)(iii)(iv) 재검토.

---

## Risk Profile (`logs/daily/2026-04-20/03_integration_and_new_open.md` §11 CS-1~4 참조)

- **CS-1 Soft-K 정의 실패 (확률 낮음):** persistence stability 는 30+ 년 성숙. 단 volume constraint compatibility 는 **2026-04-21 G1/G3 에서 검증 대상**. 실패 시 A (portfolio 접근) 로 pivot.
- **CS-2 Thermal 결국 필요 (확률 중간):** C+E 는 이미 이를 수용 — 본 risk 는 E-only 선택 시 발생. C+E 에서는 null.
- **CS-3 Publication 우선 (확률 낮음~중간):** 현재 없음 — 발생 시 C+E cycle 중단 + B 단독 삽입.
- **CS-4 Substrate 혁명 (확률 낮음~중간):** D 는 본 cycle 과 orthogonal. 우선순위 변경 시 C+E 완료 후 D 진입.

---

## Stage 0 Exit 확인 체크

- [x] 한 줄 선언문.
- [x] 선택 후보 (C+E).
- [x] Rationale 5 개.
- [x] Non-goals 6 개 (3+ 요구 충족).
- [x] Decision tree 경로 기록 (Q-α YES → Q-β YES).
- [x] Sensitivity / risk profile.
- [x] 17-세션 stage 분배 대략.
- [x] Stage 1 첫 세션 plan (2026-04-21) 준비 완료.

**Stage 0 LOCKED.** Stage 1 이 2026-04-21 에 entry.
