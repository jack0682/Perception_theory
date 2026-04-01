# Plan — 2026-04-01 (Revised)

## 감사 결과 요약

31일 산출물 감사 결과, Gap 4/5/6 증명 문서 3개가 심각한 수학적 결함을 포함.
Strong-regime 3개 문서는 양호(6-8/10)하나 조직적 문서이지 새 증명이 아님.

### 치명적 결함 6개 (수정 필수)

| # | 문서 | 결함 | 심각도 |
|---|------|------|--------|
| 1 | Gap 6 Prop 3 | 서술 공식 vs 유도 공식 14× 불일치 (C₂ ≈ 40 vs 2.875) | CRITICAL |
| 2 | Gap 6 Thm 1 Step 4 | Γ-limit → finite-β Core 전환: 정량적 bound 없음 | HIGH |
| 3 | Gap 6 Thm 2 | iso_ratio > 1에서 15% 위반, 가정 미명시 | HIGH |
| 4 | Gap 5 ‖∂φ/∂u‖ bound | operator norm ≠ Frobenius norm 혼동; ‖(1-η)I+ηP‖≤1 미증명 | HIGH |
| 5 | Gap 5 Schauder Step 7 | energy minimizer의 초기조건 연속 의존성 — μ→0에서 IFT 실패 | MEDIUM |
| 6 | Gap 4 boundary-mode | 수치적 관찰만 존재, 해석적 증명 없음; r≥0.210 대체 정리 없음 | HIGH |

---

## 수정 계획

### Phase 1: 공식 오류 수정 (즉시)

**Task 1.1** — Gap 6 Prop 3 공식 수정
- CORE-DEPTH-ISOPERIMETRIC.md 서술부의 C₂ 공식을 유도와 일치하도록 수정
- C₂ ≤ (λ_cl·G_cl + λ_sep·G_sep) / (2λ_bd) = 2.875

**Task 1.2** — Gap 5 해석적 bound 수정
- stacked matrix operator norm 공식: ‖[A; B; C]‖_op = max(‖A‖, ‖B‖, ‖C‖), NOT √(Σ‖·‖²)
- (1-η)I + ηP의 operator norm: P는 row-stochastic → ‖P‖_op ≤ 1 → ‖(1-η)I + ηP‖_op ≤ 1 ✓ (실제로 맞지만 증명 추가 필요)
- 수정된 해석적 bound: max(1, a_cl/4, a_D(1+λ_D)/4) = max(1, 0.875, 2.5) = 2.5
- 실측 1.43은 여전히 유효하지만 해석적 상한은 2.5 (2.83이 아님)

### Phase 2: 논리적 gap 보강 (핵심)

**Task 2.1** — Gap 6 Thm 1 Step 4: Γ→finite-β 전환 증명
- 필요한 것: |Core(û_β) △ S*| = O(ε√m) where ε = α/β
- 접근: PDE analysis의 exponential saturation 결과 활용
  - 깊이 δ ≥ 1인 Core(S*) 내 site: û_β(x) ≥ 1 - C₁exp(-c₀) > 0.9 when β > 11α
  - 따라서 Core(S*) ∩ {δ_S* ≥ 1} ⊆ Core(û_β)
  - S*의 inradius ≥ 2 → Core²(S*) ≠ ∅ → Core²(û_β) ⊇ Core²(S*) \ (transition layer)
- 이것은 interior gap bound + Γ-convergence의 조합으로 증명 가능

**Task 2.2** — Gap 6 Thm 2: 조건 명시
- "near-isoperimetric" 조건 추가: iso_ratio ≤ C_iso (C_iso는 명시적 상수)
- 또는 약한 버전으로 교체: |Core²| ≥ |Core| - |∂Core| (이것은 Thm 2보다 약하지만 무조건 성립하는 항등식)
- 강한 버전은 iso_ratio 조건부로 유지

**Task 2.3** — Gap 5 Schauder Step 7 보강
- 핵심 문제: T(u_s) = argmin_u E(u) starting from OT-transported field
- 접근 A: T를 gradient flow의 infinite-time limit으로 정의 → Łojasiewicz convergence guarantees convergence → initial condition 연속 의존성은 analytic energy에서 성립 (단, 유일성 필요)
- 접근 B: T를 gradient flow의 finite-time truncation으로 정의 → ODE flow는 연속 → Schauder 적용 → 임의의 T 이후 fixed point 존재
- 접근 B가 더 깔끔: 유한 시간 flow는 연속, Σ_m은 compact convex → Schauder 적용 가능. 그 후 T→∞ limit을 separate argument로.

**Task 2.4** — Gap 4: Boundary-mode 해석적 characterization
- 왜 boundary nodes가 soft mode를 지배하는가?
- Core nodes: W''(u≈1) = 2 > 0, Laplacian 기여 4α·d ≈ 16α → Hessian ≈ 2β + 16α (large)
- Exterior nodes: W''(u≈0) = 2 > 0, Laplacian ≈ 16α → Hessian ≈ 2β + 16α (large, + box constraint)
- Boundary nodes: u ∈ (0.2, 0.8) → W''(u) can be < 0 (spinodal). At u=0.5: W''(0.5) = -1
  - Hessian ≈ -β + 16α (can be negative before projection!)
  - Boundary nodes의 constrained Hessian 기여가 가장 작음 → soft mode 지배
- 이것은 해석적으로 증명 가능: W''의 spinodal region + Laplacian 크기 비교

### Phase 3: 수정 문서 작성 & Canonical Spec 반영

**Task 3.1** — 3개 proof 문서 수정 (erratum 추가)
**Task 3.2** — Canonical Spec v2.0 erratum 반영 (Prop 3 공식, Schauder 조건)
**Task 3.3** — CHANGELOG 업데이트

---

## 우선순위

1. Phase 1 (공식 오류) — 즉시 수정, 30분
2. Phase 2.1 + 2.4 (가장 중요한 논리 gap) — 핵심 작업
3. Phase 2.2 + 2.3 (보조 gap)
4. Phase 3 (통합)

---

## 보류

- Plan_0401.md의 product-manifold / merge competitor 과제는 Gap 4/5/6 수정 완료 후로 연기
- Strong-regime 문서 3개 (8/7/6점)는 현재 수준 유지, 급한 수정 불필요
