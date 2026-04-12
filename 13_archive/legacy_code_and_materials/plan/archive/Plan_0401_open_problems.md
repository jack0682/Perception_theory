# 미해결 문제 계획 — 2026-04-01

---

## 우선순위 A: 이론 완성에 필수

### A1. Strong-Regime Transport Selection (Gap 5 + Topic 6)
**문제:** Schauder는 고정점 존재만 보장. λ_tr이 크고 ε_OT이 작을 때 여러 고정점 가능 — 어떤 것이 û_t 근처인지 선택 규칙 없음.
**중요도:** T-Persist-Full의 (WR') 조건을 완화하려면 필수.
**접근 전략:**
1. **Degree theory**: T: Σ_m → Σ_m의 Leray-Schauder degree 계산. deg(I-T, B_r(û_t)) ≠ 0이면 û_t 근방에 고정점 존재 (유일성 불필요)
2. **Continuation argument**: WR' 만족하는 약한 체제에서 시작 → λ_tr 증가 → 고정점이 연속적으로 이동 → implicit function theorem으로 continuation
3. **수치 실험**: λ_tr을 0.01 → 10으로 sweep, 고정점 개수와 위치 추적
**예상 난이도:** HIGH — 새로운 수학 필요
**산출물:** 증명 문서 + exp29

### A2. T-Persist-K-Strong Merge Dichotomy (Topic 4)
**문제:** μ_overlap ≤ 0 → K-formation이 saddle → gradient flow가 (K-1)-formation으로 하강? 증명 없음.
**중요도:** Multi-formation 이론의 최대 gap.
**접근 전략:**
1. **Product-manifold Morse theory**: Σ^K_M 위의 saddle → descending manifold 분석
2. **Explicit (K-1) competitor 구성**: overlap pair (j,k)를 merged field로 내리는 ansatz
3. **Sublevel connectivity**: K-branch와 (K-1)-branch 사이 sublevel set 연결성
4. **수치 실험**: K=2에서 overlap 증가시키며 flow trajectory 추적
**예상 난이도:** VERY HIGH — Morse theory on constrained manifold
**산출물:** 증명 시도 문서 + exp30

---

## 우선순위 B: 이론 강화에 중요

### B1. Exact β_crit Threshold for Deep Core (Topic 5)
**문제:** 증명은 β ≥ 58α, 실험은 β ≥ 20α. 갭이 3×.
**접근:** 
1. Markov transfer의 threshold ε₀ = 0.4를 최적화 → β threshold 감소
2. C₂ bound를 formation-conditional로 tighten (현재 worst-case)
3. Phase diagram: (β/α, m) 평면에서 deep core 존재 경계 정밀 측정
**예상 난이도:** MEDIUM
**산출물:** CORE-DEPTH 문서 erratum + exp31

### B2. Directional Basin Bounds / Ellipsoidal Structure (Topic 7)
**문제:** Isotropic r_basin은 soft mode 방향의 worst case. Perturbation이 soft mode에 수직이면 basin 훨씬 넓음.
**접근:**
1. Hessian eigenbasis에서 방향별 r_k = √(2Δ_k/μ_k) 계산
2. Temporal perturbation의 soft mode 성분 bound → 실효적 basin radius
3. "Transverse persistence" 정리: soft mode 수직 방향으로는 basin 항상 O(1)
**예상 난이도:** MEDIUM
**산출물:** BASIN-ESCAPE 문서 §10 + exp32

### B3. Near-Bifurcation Boundary-Layer Dynamics (Topic 8)
**문제:** NB-1/NB-2는 deep core 생존만 보장. Boundary nodes의 운명은?
**접근:**
1. Slow manifold theory: μ→0 근방에서 boundary nodes의 slow dynamics 분석
2. Center manifold reduction: soft mode 방향으로 reduced ODE 유도
3. Boundary node field value의 τ-dependence 추적
**예상 난이도:** HIGH
**산출물:** NB-LOCAL-THEORY 문서 확장

---

## 우선순위 C: 장기 과제

### C1. Product-Manifold Basin Theory on Σ^K_M
Plan_0401에서 연기됨. A2 해결 후 진행.

### C2. Formation Birth/Death Theory
K-Strong merge의 역과정. 완전히 미탐색.

### C3. Δ_bdy Geometry Formula
Taylor normal form은 유도됨. Formation shape parameters로의 번역 필요.

---

## 즉시 실행 가능한 작업 (오늘)

1. **B1 (β_crit tightening)** — Markov threshold 최적화 + exp31
2. **B2 (Directional basin)** — Hessian eigenbasis 분석 + exp32
3. **A1 시작** — λ_tr sweep 실험 (exp29) + degree theory 문헌 조사

A2 (K-Strong merge)는 가장 어렵고 장기적 — 오늘 착수하되 완결 기대 않음.
