# pre_brainstorm.md — 2026-04-25 Session Pre-brainstorm

**Purpose:** 오늘 세션 진입 전 open-ended hypothesis exploration + weekly summary 전략 사전 구상.
**Reference state:** 2026-04-24 종료 — Theorem 1 V5b (Goldstone doublet + commensurability splitting 발견, Cat B conditional), Theorem 2 Cat A (Pre-Objective, graph-class independent), F-1 fully resolved, σ-framework definitional Cat A, ~29 Cat A 누적, 2 in-session retractions (V4, V5a), ~40 new NQ (NQ-125..171).
**Thinking mode:** 어제의 lesson — "user skepticism이 proper science를 강제". 오늘은 hot discovery에 홀리지 말고 검증 우선.

---

## §1. Core question refinement

**어제의 질문 (종료 시)**: "Goldstone doublet이 commensurability에 의해 split되는가?"
**어제의 답 (V5b, evidential)**: Yes — 99% Goldstone overlap (L=40, ζ=1.0) + 2D doublet splitting 직접 관측.

**오늘의 질문 (심화)**: "Commensurability splitting의 mathematical structure는 무엇인가? Finite-size artifact인가 intrinsic phenomenon인가?"

피해야 할 답: "Frenkel-Kontorova와 동일하다" (reduction claim)
추구할 답: "격자 비정합성이 SCC Goldstone의 degeneracy를 어떻게 깨는가 — SCC 맥락 안에서."

**배경 긴장**: Theorem 1이 sub-lattice (ζ<0.3)에서 "genuine orbital only" (Cat A)이고 super-lattice (ζ>0.5)에서 Goldstone doublet (V5b)이라면, 경계 ζ* ≈ 0.3–0.4는 무엇을 의미하는가? 이 first-principle explanation이 아직 없음.

---

## §2. NQ-168 deep analysis — 사전 가설 (4가지)

### 가설 D (Finite-size artifact) — 먼저 기각/지지 결정

**예측**: L → ∞에서 Δλ = λ₁ - λ₀ → 0. Torus periodic BC에서 Δλ = 0.
**검증**: L=20, 30, 40 scaling. Torus vs free BC 비교.
**의의**: D가 지지되면 오늘 발견은 methodological artifact → V5b의 super-lattice 부분 수정 필요.

### 가설 A (FK-PN style) — 기각 후 A 검증

**메커니즘**: Formation이 격자 potential well에 commensurate하게 위치. Center가 lattice site와 얼마나 misaligned되는지에 따라 x-Goldstone vs y-Goldstone 에너지 차이.
**예측**: Δλ ∝ |center_position mod 1 - 0.5| (saddle point에서 최대)
**검증**: N=5+ seed, center position 분포 측정 → Δλ vs (x_c mod 1, y_c mod 1) scatter plot

### 가설 B (격자 고조파) — 이론 기반

**메커니즘**: SCC 경계 에너지에 D₄ 격자 보정 δV₄cos(4θ) 포함. x-/y-Goldstone이 이 보정을 다르게 감지.
**예측**: Δλ ∝ ζ (linear in regime parameter), Δλ ∝ β (경계 폭 의존)
**검증**: β 변경 실험 (시간 있을 시)

### 가설 C (SCC closure 특이성) — 이론

**메커니즘**: Closure operator Cl이 interior를 c*1로 당기는 힘이 x-/y- 방향별로 다르게 작용.
**예측**: λ_cl=0 시 Δλ=0
**검증**: λ_cl scan (시간 있을 시)

**Falsification 우선순위**: D → A → (B/C는 시간 허용 시)

---

## §3. σ-Numerical Verification 상세 전략

### NQ-128 (λ₀/λ₁ ratio — Theorem 1 핵심 검증)

**V5b prediction**:
- Sub-lattice minimizers (ζ < 0.3): λ₀/λ₁ ≈ O(1) (no Goldstone, genuine orbital)
- Super-lattice minimizers (ζ > 0.5): λ₀/λ₁ << 1 (near-zero Goldstone)
- Crossover ζ* ≈ 0.3–0.4: sharp transition 예상

**Protocol**:
1. R23 exp_orbital_fullscale.json 로드 → 56 stable minimizer
2. 각 minimizer에서 ξ₀ (interface width), a (lattice constant) 추출 → ζ = ξ₀/a
3. Hessian lowest 2 eigenvalue (λ₀, λ₁) 추출
4. λ₀/λ₁ vs ζ 산점도

**위험**: R23 데이터가 lowest eigenvalue를 저장하지 않은 경우 → Hessian 재계산 (시간 +1h)

### NQ-137 (nodal × irrep — σ-framework 검증)

**Protocol**:
1. 각 minimizer의 lowest 20 Hessian eigenvector
2. Nodal count: n_k = connected components of {i: φ_k(i) > 0} + {i: φ_k(i) < 0}
3. D₄ irrep projection (8 symmetry ops: identity, r90, r180, r270, rx, ry, rd1, rd2)
4. σ-class (n_k, [ρ_k]) 분포 통계

**Lemma 3 검증**: Mode 0 (Goldstone)의 irrep = E (ℓ=1 basis), Mode 1 = B₁ or B₂ (d-orbital)

### NQ-141 (σ ↔ orbital taxonomy cross-check)

**Protocol**: R23의 기존 angular multipole label (ℓ=0,1,2)과 σ-irrep 비교.
**핵심 체크**: "Mode 0 = ℓ=1 dominant" (R23 measurement) vs "Mode 0 = E-irrep Goldstone" (Lemma 3 prediction) — consistent?

---

## §4. Weekly Summary 작성 전략

### W4 Narrative Thread (Apr 19–25)

| 날짜 | 핵심 사건 |
|-----|---------|
| Apr 19 | CODE/THEORY 분리 재구조화 |
| Apr 20 | Stage 0 Purpose Decision materials + integer-K dependency map + canonical_sub.md 신설 |
| Apr 21–22 | (확인 필요: weekly_draft 참조) |
| Apr 23 | Orbital hierarchy 경험적 발견 (A-01..A-05) + CN15/16/17 proposals + 32 NQ + weekly rotation 결정 |
| Apr 24 | σ-framework + Theorem 2 (Cat A) + F-1 resolved + V5b discovery + ~29 Cat A |
| Apr 25 | W4 close + V5b verification attempt + σ-numerical |

**W4의 dominant narrative**: "Orbital analogy (Apr 23) → SCC-intrinsic σ-framework (Apr 24 오전) → Pre-Objective theorem (Apr 24 오후) → Goldstone doublet discovery (Apr 24 밤)"

### Tier 분류 기준 (weekly_summary 내)

| Tier | 정의 | 조건 |
|-----|-----|-----|
| T1 (merge 가능) | 증명 완료 + graph-class independent | Theorem 2 family, F-1 resolution |
| T2 (conditional) | 증명 있으나 regime 한정 또는 1-class only | Theorem 1 V5b, Lemma 1/2/3, σ-definitional |
| T3 (sketch) | 개념 + 부분 증거 | G4 continuum, C3 super-lattice qualitative |
| T4 (retracted) | In-session retracted | V4, V5a |

**Anti-over-claim rule**: T2 → T1 격상은 graph-class independent numerical 확인 필요. 오늘 세션으로 불가.

### 3 Self-weaknesses to document honestly

1. **Theorem 1 6회 개정**: V1→V5b는 발견의 깊이이지만 동시에 "아직 stable 하지 않음" 신호.
2. **29 Cat A 중 T1 2건**: "29 Cat A"는 양적이나 T1은 2건뿐. weekly_summary에서 정직하게.
3. **G2/G3 미실행 사유 미기록**: 어제 plan.md P0가 실행되지 않은 공식 사유가 없음.

### Canonical Merge 권고안 (초안)

**T1 → merge 권고**:
- `canonical.md` §13: Theorem 2 family (Pre-Objective, (i)-(v)+2-G+Lemma 4)
- `open_problems.md` OP-0001 (F-1): UNRESOLVED → RESOLVED ✅ (Cat A both layers)
- `open_problems.md` OP-0002 (M-1): 상태 업데이트 (layer-clarified, premise 붕괴 명시)
- `open_problems.md` OP-0003 (MO-1): scope note 추가 (sidestepped via single-formation)

**T2 → 보류 (merge 없음)**:
- Theorem 1 V5b → working/에 동결, NQ-168 검증 후 재평가
- σ-framework → NQ-128/137/141 후 재평가
- Axiom S1' v1 → user 리뷰 후

---

## §5. Risks & Tensions

### 5.1 Time risk (G0 의무 vs G1/G2 욕구)

**위험**: NQ-168 에 시간을 쏟다가 G0 weekly_summary 미완성.
**완화**: Evening 3h는 G0에 고정. G1/G2가 막히면 G0 먼저.

### 5.2 V5b 추가 falsification 위험

**위험**: NQ-168 결과가 V5b 일부를 falsify.
**완화**: V5b는 Cat B (conditional). Falsification이 science. Doublet 자체(99% overlap)는 분리 — mechanism만 수정될 수 있음.

### 5.3 σ-framework over-reach

**위험**: "definitional Cat A"가 σ-derived 모든 결과를 자동 Cat A로 격상.
**완화**: σ 의 definitional 부분과 σ-derived theorem 을 명시 분리.

### 5.4 weekly_summary 성과 압박

**위험**: "W4 strong close" 압박 → T2를 T1로 격상 유혹.
**완화**: Tier 표 먼저 작성 (기계적), narrative는 나중.

### 5.5 G3 결정의 혼돈

**위험**: D₄ irrep이 σ에 포괄되는지 모른 채 실행/포기.
**완화**: 세션 시작 30분 내 명시적 결정 + 사유 commit.

---

## §6. Deep Questions for Today

- **Q-T1**: Δλ의 L-scaling이 Δλ → 0 (artifact)인가 Δλ → const (intrinsic)인가? → 가설 D 결정.

- **Q-T2**: σ-framework가 D₄ irrep 분류 (G2)를 완전히 포괄하는가, 아니면 독립 정보를 추가하는가? → G3 결정.

- **Q-T3**: V5b의 ζ* ≈ 0.3–0.4 crossover는 물리적으로 무엇인가? ξ₀ = a 조건의 SCC-intrinsic 의미?

- **Q-T4**: In-session retraction (V4, V5a)의 원인이 "새 정보 도달"인가 "사전 검증 부족"인가? → process 개선 결정.

- **Q-T5**: F-1 resolution을 "Cat A resolved"로 weekly_summary에 기록하면, open_problems.md 실제 갱신은 user 리뷰 후인가, weekly_summary 작성 시인가? (canonical 경계 질문)

---

## §7. Mental Setup Check

시작 전 자기 점검:

- [ ] 어제 V5b 발견에 대한 흥분이 "이미 확정" 착각으로 이어지지 않는가?
- [ ] G0 (weekly_summary)가 "boring administrative"가 아니라 "이론 신뢰성을 지키는 핵심"임을 인식하는가?
- [ ] G3 결정이 "먼저 결론 후 사유 끼워맞추기" 방향이 아닌 "사유 먼저"인가?
- [ ] 오늘의 목표가 "새 Cat A 추가"가 아닌 "어제 Cat A의 검증"임을 인식하는가?
- [ ] weekly_summary에서 Tier 표가 narrative보다 먼저 작성되는가?
- [ ] NQ 누적 수 (~171)가 triage 세션 필요 임계치에 근접했음을 인식하는가?
- [ ] 사용자의 skeptical 질문이 올 경우, 그것이 science를 강제하는 힘임을 환영하는가?

---

## §8. Core Message

> **"어제는 만들었다. 오늘은 확인한다. V5b는 current best, not proven. σ는 defined, not verified. weekly_summary는 의무, not optional. Tier 분류가 narrative보다 먼저. Silent resolution은 0건."**

---

**End of pre_brainstorm.md for 2026-04-25.**
**Theme: Verify over discover. Honest close over impressive summary. V5b pinned numerically, or honestly retracted.**
