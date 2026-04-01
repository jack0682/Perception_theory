# 증명 우선순위 계획 — 2026-04-02

## 목표
이론 완결성 확보: Conditional → Proved 승격, 남은 gap 폐쇄

---

## Tier 1: 즉시 실행 (1세션)

### #1. C3'' 대칭화 gap 폐쇄 ★★★★★
- **현재**: C-Axioms (Cat A)의 유일한 gap. D^{-1/2} 유사성 변환이 u_t(x)에 의존 → Neumann series monotonicity 마지막 단계 미검증
- **접근**: D^{-1/2}(u) W_sym D^{1/2}(u)의 u 미분이 monotonicity를 보존하는지 explicit 행렬 미적분
- **난이도**: Medium
- **산출물**: docs/04-02/proof/C3-SYMMETRIZATION-PROOF.md
- **효과**: C-Axioms gap 완전 폐쇄 → 정적 이론 100% 완결

### #2. Transport confinement tight bound ★★★★
- **현재**: C_conf = O(σ√(ε_OT log n))은 25-10000× 보수적. exp41에서 B1 (boundary-proportional)이 1.02× 위반
- **접근**: B1에 1.05× safety factor → formation-aware bound C_tight = 1.05·σ·√(ε_OT)·|∂Core|^{1/2} 증명
- **난이도**: Medium
- **산출물**: docs/04-02/proof/TIGHT-CONFINEMENT-PROOF.md + exp45 검증
- **효과**: Transport selection uniqueness의 실용적 sufficient condition → T-Persist-1(e) 실질적 무조건화

## Tier 2: 같은 세션 또는 다음 세션 (1-2세션)

### #3. T-Persist-1(b) Basin containment 무조건화 ★★★★★
- **현재**: Conditional on GT + NB (μ ≥ 4.1)
- **접근**: 
  - GT: tight confinement (#2)로 ε₂ bound → GT를 transport 파라미터로 환원
  - NB: "generic by Sard" → finite graph에서 non-degeneracy는 parameter space의 full-measure set임을 explicit 증명
- **난이도**: Medium-Hard
- **산출물**: docs/04-02/proof/BASIN-UNCONDITIONAL.md
- **효과**: T-Persist chain 핵심 링크 무조건화

### #4. T-Persist-K-Weak NB-K spectral gap ★★★★
- **현재**: Weyl bound 사용, NB-K 조건 충족 실험적으로만 확인
- **접근**: Cauchy interlacing / Gershgorin으로 μ_joint 하한 개선, (SR) 조건의 정량적 합리성 증명
- **난이도**: Medium
- **산출물**: docs/04-02/proof/K-WEAK-SPECTRAL.md + exp46 검증
- **효과**: T-Persist-K-Weak 조건 약화

## Tier 3: 이론 확장 (장기)

### #5. Bifurcation branch selection (μ = 0)
- Center manifold reduction, 확률적 선택 이론
- 난이도: Hard — 논문에 "open problem"으로 유지 가능

### #6. Formation birth formal theorem
- Topological birth: λ₂(G_Core) < ε_split → core disconnection
- Parametric birth: T8-Core의 역 (이미 proved)
- 난이도: Medium

### #7. T8-Full non-degeneracy
### #8. K-Strong barrier transition state (NEB)
### #9. Predicate-Energy quantitative threshold

---

## 실행 계획

**내일 (04-02) 최우선:**
1. #1 (C3'' gap) — 에이전트 1: 증명 작성
2. #2 (Tight confinement) — 에이전트 2: 증명 + 실험
3. #3 (Basin 무조건화) — 에이전트 3: GT 환원 + NB generic 증명

**#1, #2 완료 후:**
4. #4 (K-Weak spectral) — 에이전트 4: spectral bound 개선 + 실험

**목표 상태:**
- Cat A: 25 → 26 (C-Axioms gap 폐쇄)
- Conditional: 6 → 3~4 (Basin, Transport selection 무조건화)
- Open: 4 → 2~3 (tight confinement 해결)
- 이론 완결도: 88% → 93%+
