# Pre-Brainstorm — 2026-04-21 C+E Stage 1 Hypothesis Map

**Written:** 2026-04-20 저녁 (pre-session).
**Author:** 사용자 + 에이전트 공동 브레인스토밍.
**Purpose:** 내일 세션 (C+E Stage 1 공통 첫 세션 — G1…G6, 6 deliverable) 진입 전, 수학·물리 관점에서 leverage 가능한 가설·도구·연결을 **최대한 광범위하게** 나열. 에이전트가 `plan.md` 와 함께 본 파일을 읽어, 각 deliverable 작성 시 가설 풀을 base 로 선택·거부·확장한다.
**Scope:** 104 가설 (A–J 섹션). 가설 채택·기각은 에이전트 판단 + 사용자 검토.
**Constraint:** 본 파일은 **사전 가설 목록** 이지 증명·commitment 아님. 내일 실제 증명 대상은 `plan.md §Session goals` 에 한정.

---

## 사용 가이드

1. 각 가설 H-XX 는 3~5 줄. (명제) + (근거/출처) + (내일 활용 방식).
2. `H-A*` ~ `H-F*` 는 G1~G6 의 **직접 활용 후보**. 에이전트는 각 deliverable 작성 시 해당 섹션을 review.
3. `H-G*` 는 **교차 구조** — 3 Critical 의 관계. Dissolution mapping 의 cross-reference 로 활용.
4. `H-H*` 는 **risk / counter-hypothesis**. 각 deliverable 의 Non-goals / Pending 기록에 반영.
5. `H-J*` 는 **out-of-scope inspiration**. 내일 scope 외이나 후속 세션 아이디어 풀.
6. §I 는 가설 → deliverable priority mapping (요약).

---

## A. K_soft 정의 (G1)

### A-Math: Topology / Functional Analysis

- **H-A1.** (i) persistence weighted sum `K_soft(u) = Σᵢ ℓᵢ · φ(ℓᵢ)` 는 canonical §5.5 Q_morph 의 자연 확장 — codomain 최소 변경. φ 선택은 taste, monotone Lipschitz 가 최소 요구.
- **H-A2.** (ii) Betti integral `∫₀¹ β₀(U_θ) dθ` 과 (i) 는 **φ(ℓ) = ℓ 일 때 exact equivalent** (Fubini on filtration). NQ-1 부분 해소 — (i)(ii) merge 가능.
- **H-A3.** (iii) simplex-valued `u: X → Δ^{K_max}` 는 Fisher-Rao geometry 유도, `K_eff = exp(H(u))` — entropy 직결. C 와 자연 통합.
- **H-A4.** (iv) measure-valued 는 Wasserstein gradient flow compatible — 가장 일반적이나 discrete graph 에서 atomic measure 로 축소.
- **H-A5.** Novel hybrid: `K_soft = Σ φ(ℓᵢ) · ψ(bar entropy)` — persistence + Shannon 결합. 더 풍부한 information content, 그러나 complexity 증가.
- **H-A6.** `∇K_soft` 의 explicit formula 는 vineyard flow (bar trajectories) — stability 이론은 statement, pointwise 는 vineyard singularity 시 discontinuous.
- **H-A7.** Volume constraint `Σuᵢ = m` 는 K_soft 와 **서로 다른 축** — K_soft 는 superlevel filtration rank, m 은 integral. projection 은 well-defined.
- **H-A8.** 그러나 Σ_m 위에서 K_soft 의 extreme values 는 m 의존 — `sup_{u∈Σ_m} K_soft ~ m / ℓ_min` scaling 가능.
- **H-A9.** Sub-additivity `K_soft(u+v) ≤ K_soft(u) + K_soft(v)`: persistence stability + bar merging — 일반적 성립, equality 조건 non-trivial.
- **H-A10.** K_soft 의 reverse: `K_hard(u) = Σᵢ 1[ℓᵢ > θ]` (threshold-dependent count). K_soft 는 그 θ-average.

### A-Physics: Order Parameter / Coarse-Graining

- **H-A11.** K_soft = **order parameter rank** — 기존 u 는 order parameter (field), K_soft 는 그 field 의 "multiplicity dimension".
- **H-A12.** RG flow: local u → regional K_soft → global ⟨K_soft⟩. Block-spin renormalization 유사.
- **H-A13.** Ising cluster count 유사 — superlevel set connected components = "droplet count" at θ.
- **H-A14.** Allen-Cahn interfaces: K_soft = interface component count in Γ-convergence limit.
- **H-A15.** Neural ensemble: K_soft = "effective number of cell assemblies coactive" — sparsity measure.
- **H-A16.** Percolation: θ = percolation threshold, β₀(U_θ) = cluster count, K_soft = integrated count over θ.
- **H-A17.** Emergent scale: K_soft 는 inherently multiscale — persistence diagram 전체 encoding, single scalar 로는 축약 손실.

---

## B. F-group 공리 (G2)

### B-Math: Measure Theory / SPDE

- **H-B1.** F1 Gibbs `ℙ ∝ exp(-ℱ/T)` on compact Σ_m — normalizer `Z = ∫_{Σ_m} exp(-ℱ/T) dvol` finite (compact + continuous).
- **H-B2.** F2 Bernoulli entropy `S = -Σ[u log u + (1-u) log(1-u)]` **strictly concave on [ε, 1-ε]^n** — global max at u = m/n uniform.
- **H-B3.** F3 Langevin `u̇ = -Π_{Σ_m}(∇ℱ) + √(2T) ξ` — projected SPDE on constrained manifold. Da Prato-Zabczyk stochastic calculus.
- **H-B4.** F3 well-posedness delicate: constraint preservation + smooth boundary reflection. Alternative: logit 변환 후 unconstrained SPDE on ℝⁿ.
- **H-B5.** F4 T→0 recovery via **Laplace's method**: Gibbs concentrates on `∂ℱ = 0` critical manifold, variance `O(√T)`.
- **H-B6.** Large deviation (Freidlin-Wentzell): `P(u_T ∈ A) ~ exp(-I(A)/T)`, `I = ∫|u̇ + ∇ℱ|²/2`. Instanton 경로가 escape rate 지배.
- **H-B7.** **KL divergence** `S_KL(u ‖ u_eq) = Σ uᵢ log(uᵢ/u_eq,ᵢ)` — reference measure 필요, F2 대안.
- **H-B8.** **Fisher information** `S_F(u) = Σ|∇log u|²` — geometric, natural gradient `= (∇log u)⁻¹ ∇ℱ` 효율.
- **H-B9.** Witten Laplacian `Δ_ℱ = Δ + |∇ℱ|²/T - Δℱ/T` — low-T 에서 discrete spectrum 이 critical points encode (Simon 1985, Helffer-Sjöstrand 1985).
- **H-B10.** Hodge decomposition: harmonic forms = ground states. Witten supersymmetric QM interpretation.

### B-Physics: Stat Mech / Field Theory

- **H-B11.** F-group = **Ginzburg-Landau + thermal fluctuation** — standard mean-field 확장.
- **H-B12.** **Kubo linear response** 자동 — `χ = ∂⟨u⟩/∂h = ⟨(u - ⟨u⟩)²⟩/T`.
- **H-B13.** **FDT**: equilibrium 에서 correlation = response. Langevin dynamics 로부터 직접.
- **H-B14.** Critical phenomena: β_crit 에서 correlation length 발산. Universal class (Ising? Potts? XY?) 결정 필요.
- **H-B15.** Mean-field on fully-connected graph exactly solvable — `N → ∞` with `β · N` fixed.
- **H-B16.** **RG flow**: block-spin argument for `(T, α, β, λ_K)` — relevant/irrelevant direction 분류.
- **H-B17.** **Witten SUSY QM** ↔ F-group: ℱ = superpotential, ground states = critical points, supercharges `Q = d + dℱ*`, `Q* = d* + iota_{∇ℱ}`.
- **H-B18.** **Path integral**: `⟨O⟩ = ∫ Du · O · exp(-S/T)`, `S = ∫(u̇² + |∇ℱ|²)/2`. Feynman-Kac.
- **H-B19.** Euclidean QFT 유사: imaginary time Schrödinger = Fokker-Planck. Spectral gap = mass gap.
- **H-B20.** Free energy Legendre transform = effective action `Γ[⟨u⟩]` — vertex functions, tree-loop expansion.

---

## C. 교차 객체 ℱ_C+E (G3)

- **H-C1.** **`λ_K ~ T` scaling**: `ℱ = ℰ - T(S - λ_K K_soft / T)`. "Effective entropy" = `S - λ_K K_soft / T`. 두 information measure 통합.
- **H-C2.** **`λ_K ~ β = 1/T` scaling**: K_soft 가 low-T dominant penalty. Discrete K 로 수렴.
- **H-C3.** **`λ_K ~ O(1)` T-independent**: K_soft 가 fixed cost. 가장 단순, T=0 과 T→∞ 가 topologically different regime.
- **H-C4.** **Phase diagram `(T, λ_K)`** 4 corners:
  - (0, 0): canonical v1.2 SCC
  - (0, ∞): K-fixed zero-T (strict soft-K-integer)
  - (∞, 0): infinite-T thermal disorder
  - (∞, ∞): competing limits — 계산 필요
- **H-C5.** Modified Gibbs: `exp(-ℱ_C+E/T) = exp(-ℰ/T) · exp(S - λ_K K_soft/T)` — "energy weight" × "complexity weight" 분리.
- **H-C6.** Information decomposition: Shannon S (local uncertainty) + persistence K_soft (topological complexity) 두 축 orthogonal.
- **H-C7.** Multiscale variational: ℰ (local bulk + nonlocal transport), S (site-wise), K_soft (topological). **Three-scale competition.**
- **H-C8.** Minimizer `(T, λ_K)` 의존: small λ_K → thermal SCC minimizer, large λ_K → quantized K_soft ≈ integer. **Crossover region** 존재 가설.
- **H-C9.** **Degenerate lift**: `λ_K > 0` breaks K=1 degeneracy (mode choice) — symmetry breaking 메커니즘.
- **H-C10.** `δK_soft/δu` 는 vineyard 에서 explicit. `∇ℱ_C+E = ∇ℰ - T∇S + λ_K · δK_soft/δu`. Bar birth/death 순간 discontinuous.

---

## D. F-1 Dissolution (G4)

- **H-D1.** "Vacuity" 는 integer-K category 에서만 정의 — "K=2 requires external m_j" 는 K 가 discrete 할 때. Soft-K 에서 m_j 는 distribution 의 conditional mass.
- **H-D2.** K=2 는 distribution regime: `K_soft(u) ≈ 2` = H₀ diagram 두 dominant bars. 외부 m_j 없이 정의.
- **H-D3.** K-resolved partition: `Z = ∫_{Σ_m} exp(-ℱ/T) du = Σ_K ∫_{K_soft≈K} exp(-ℱ/T) du = Σ_K Z_K`. 각 K sector 에 well-defined free energy.
- **H-D4.** F-1 의 "4.66 vs 2.25" 는 ℰ 차이. Free energy `F_K = ℰ_K - T S_K + λ_K · K`. S_K (configuration count at K_soft≈K) 가 K 와 증가 → **thermal 에서 K=2 compete.**
- **H-D5.** **Critical T_c**: `T_c · (S_2 - S_1) ≈ ℰ_2 - ℰ_1 ≈ 2.41`. S_2 - S_1 = log(microstates_2/microstates_1) 근사 추정.
- **H-D6.** **Crossover temperature**: T < T_c 에서 K=1 thermodynamic preferred, T > T_c 에서 K=2 entropically preferred.
- **H-D7.** F-1 은 **zero-T artifact** — T > 0 에서는 "K=2 metastable with occupation probability `Z_2/Z`" 정확 statement.
- **H-D8.** exp62/63 결과는 T = 0 gradient descent — `Z_K` 대신 `minₖ ℰ_K` 측정했기 때문. Thermal 확장 시 재측정.

---

## E. M-1 Dissolution (G5 — 가장 묵직)

- **H-E1.** **Isoperimetric feature**: Modica-Mortola (1977) `ε∫|∇u|² + W(u) → perimeter`. Single-phase 가 minimum perimeter → K=1 preferred.
- **H-E2.** Feature (bug 아님): K=1 preference 는 geometry 로부터 derive 되는 결과. 이론 내부 일관성.
- **H-E3.** **Kramers-Eyring rate**: `τ = (2π/|ω_s|) · (det H_a / |det H_s|)^{1/2} · exp(ΔE/T)`. ω_s = saddle negative eigenvalue, H_a/H_s = attractor/saddle Hessian.
- **H-E4.** exp38 `γ_eff ≈ 0.89` 는 Hessian scaling — `β^{0.89} ~ (det H)^{0.89/2} ~` (Hessian eigenvalue) 비례. `0.89 = 2 × 0.445` → eigenvalue exponent `0.445 ~ ½` (naive).
- **H-E5.** **Freidlin-Wentzell** instanton: `P(escape) ~ exp(-I/T)`, `I = ∫_γ |γ̇ + ∇ℱ|²/2`. Optimal path saddle 경유.
- **H-E6.** **K>1 metastability 3 origin**:
  - (α) **Energy barrier** (Kramers) — classical.
  - (β) **Topological obstruction** — K-mode distributions 의 homotopy class.
  - (γ) **Entropic stabilization** — high T 에서 configuration count.
- **H-E7.** **Nucleation theory** (Becker-Döring): K=1 → K=2 는 droplet nucleation, critical radius `r* = 2σ / Δμ`. σ = surface tension (E_bd), Δμ = chemical potential difference.
- **H-E8.** **Ostwald ripening**: K>1 modes coarsen via mass exchange. Time scale `~ L³/D` (Lifshitz-Slyozov).
- **H-E9.** **Allen-Cahn → mean curvature flow**: interfaces shrink, K 감소. 시간 척도 `~ 1/curvature²`.
- **H-E10.** **Supercooled liquid 유사**: K>1 metastable = glass (long-lived, non-equilibrium). K=1 = crystal (equilibrium).
- **H-E11.** **`β^{0.89}` universality 검토**: 2D Ising ν = 1, 3D Ising ν ≈ 0.63, XY ν ≈ 0.67. 0.89 은 fitted empirical — Kramers prefactor 해석 시 단순 Hessian scaling 으로 설명.
- **H-E12.** **Dynamic quench**: T(t) 시간 변화. Fast quench → K>1 trapped, slow anneal → K=1.
- **H-E13.** **Eyring transition state theory** — saddle 에서 transmission coefficient κ. `τ = κ · (2π/|ω_s|) · exp(ΔE/T)`. κ ~ 1 for simple barrier crossing.
- **H-E14.** **Lifetime 구체 계산**: `τ/τ_0 = (det H_a / |det H_s|)^{1/2} · exp(2.41/T)`. T ~ 1 → `τ/τ_0 ≈ 11 · Hessian ratio`. Observable timescale.

---

## F. MO-1 Dissolution (G6 — Morse Theory 대안 풍부)

- **H-F1.** Σ²_M corner (m_j=0 경계) = integer K artifact. Soft-K 에서 `K_soft ∈ ℝ≥0` 연속 → **코너 소멸**.
- **H-F2.** **Smooth Morse 복원**: Σ_m interior 는 smooth manifold without boundary, ℱ_C+E smooth → standard Morse.
- **H-F3.** **Morse-Bott** 확장: degenerate critical submanifold 허용. `K_soft = const` level set 이 submanifold.
- **H-F4.** **Stratified Morse** (Goresky-MacPherson) 여전히 필요한 경우: Σ_m 의 simplex edge 에서. Soft-K interior 에서는 불필요.
- **H-F5.** **Witten Laplacian** `Δ_ℱ = e^{ℱ/T} Δ e^{-ℱ/T} + e^{-ℱ/T} Δ e^{ℱ/T}`. Kernel = critical point 대응 (Witten 1982).
- **H-F6.** **Helffer-Sjöstrand semiclassical**: low T 에서 Witten spectrum 의 small eigenvalues = `exp(-barrier/T) · Hessian det factor`. **Kramers rate 의 rigorous derivation.**
- **H-F7.** **Fokker-Planck operator** `L = div(u ∇ℱ) + T Δ`. Spectral gap = inverse relaxation time.
- **H-F8.** **Hodge decomposition** on Witten complex: harmonic = ground state = stable configuration.
- **H-F9.** **Morse inequalities**: `#Crit_k ≥ b_k(Σ_m)`. Topological lower bound.
- **H-F10.** **Forman's discrete Morse theory** — combinatorial, finite graph 에 직접 적용. Σ_m 의 cell complex 위 discrete gradient vector field.
- **H-F11.** **Reeb graph** of ℱ_C+E — level set topology. 1D structure capturing critical info.
- **H-F12.** **Reeb barcode = persistence diagram of (Σ_m, ℱ_C+E)** — K_soft definition 의 theoretical foundation.
- **H-F13.** **Floer homology** 유사 (infinite-dim Morse) — SCC continuous limit 에서.
- **H-F14.** **Cerf theory**: 1-parameter families of Morse functions. T 를 parameter 로 → bifurcation tree.

---

## G. 교차 구조 — F-1 / M-1 / MO-1 의 관계

- **H-G1.** **세 Critical 는 하나의 수학적 source** (Integer K). Soft-K 로 동시 소멸. N-1 single-root hypothesis 의 수학적 구현.
- **H-G2.** 소프트화 후 **residual 문제**:
  - F-1 잔여: K_soft 규모가 volume m 에 의존 — "vacuity-like" scaling.
  - M-1 잔여: single-mode preference 유지 — feature 로 재분류되나 남음.
  - MO-1 잔여: smooth Morse 가 interior 에서만 작동 — Σ_m boundary 에서 여전히 stratified 필요.
- **H-G3.** **세 Critical dissolution 은 "재언어화"** — 새 language (soft-K + thermal) 에서 새 문제 등장 가능:
  - 새 vacuity: soft-K distribution 의 volume 의존성.
  - 새 preference: single-mode vs multi-mode 의 crossover T_c.
  - 새 Morse obstacle: Σ_m boundary 에서의 smoothness.
- **H-G4.** **Gauge theory 유사성**: integer K 는 topological charge (homotopy class), soft K 는 continuous order parameter. **Topological sector decomposition.**
- **H-G5.** **Disorder-order phase transition**: high-T K_soft large (disordered), low-T K_soft = 1 (ordered). β_crit 에서 transition.
- **H-G6.** **세 Critical 가 동일 Hessian structure 를 공유**: Σ^K_M 의 Hessian 이 F-1 (stability), M-1 (isoperimetric direction), MO-1 (non-degeneracy) 모두 에 등장. Hessian 분석이 세 건 통합.
- **H-G7.** **Universality**: C+E framework 가 SCC-specific 하지 않고, integer → continuous 재정의 패턴이 다른 phase-field theories (Cahn-Hilliard, phase-field crystal) 에도 적용 가능.

---

## H. Risk / Counter-Hypothesis

- **H-H1.** K_soft (i) 가 Σ_m 위에서 **not Lipschitz**: vineyard 에서 bar birth/death 시점에 persistence diagram discontinuous → K_soft sudden jump. 실제로는 generic 하게 Lipschitz 이나 non-generic set 존재.
- **H-H2.** F-group ↔ 기존 공리 **hidden conflict**: A3 closure contraction `max σ' = 1/4` 의 T 의존? σ 가 T 함수가 되면 A3 변경. NQ-5 의 구체 사례.
- **H-H3.** **Kramers formula 가 finite graph 에서 부정확**: Σ_m constraint 로 Hessian rank-deficient. Moore-Penrose pseudoinverse 로 우회 필요.
- **H-H4.** **Witten semiclassical `ε = T` small 가정**: 실제 T sufficiently small 이어야. SCC 의 α, β 와의 relative scale 조정 필요.
- **H-H5.** **`β^{0.89}` overfit risk**: Kramers prefactor 에 억지로 맞춤. Independent prediction 검증 필수 (exp77+).
- **H-H6.** **(T, λ_K) degeneracy**: 관측에서 두 파라미터 분리 불가. 추가 constraint (K_soft 의 independent probe) 필요.
- **H-H7.** **K_soft 의 physical motivation 약함**: H₀ persistence 는 mathematical convenience — "이것이 왜 physical K 인가" unclear. Fisher information 이나 effective rank 대안이 더 natural 할 수 있음.
- **H-H8.** **Scope creep**: §12 전면 재작성 유혹. 내일은 preliminary dissolution mapping 만 — 각 1~2 페이지 상한 엄수.
- **H-H9.** **1년 고착 해제 이후 새 stuck**: 3 Critical dissolve 후 P-F metastability framework 완성 에서 다시 막힐 가능성. C+E 가 P-F 해소 경로이나 completion 은 Stage 2 이후.
- **H-H10.** **Witten Laplacian 의 infinite-dim 주의**: SCC 는 finite-dim (Σ_m ⊂ ℝⁿ) 이나 continuum limit 에서 infinite-dim. 내일 scope 는 finite 만.
- **H-H11.** **T = 0 추출 정정성**: F4 T→0 이 canonical v1.2 와 정확 일치? `ℱ_C+E → ℰ + λ_K K_soft` — λ_K > 0 시 canonical 과 different limit. λ_K 의 T→0 극한 거동 별도 조정.

---

## I. Priority Mapping — 가설 → Deliverable

| G# | 핵심 가설 (즉시 활용) | Carry (E-S2, C-S2) |
|---|---|---|
| **G1** | H-A1 (persistence canonical), H-A2 (Betti equivalence), H-A7 (volume compat) | H-A5 (hybrid), H-A6 (vineyard gradient) |
| **G2** | H-B1 (Gibbs well-posed), H-B2 (entropy concave), H-B5 (Laplace T→0) | H-B3-B4 (Langevin), H-B9 (Witten) |
| **G3** | H-C1-C3 (λ_K scaling 3 option), H-C4 (phase diagram 4 corners) | H-C8 (crossover), H-C10 (vineyard gradient) |
| **G4** | H-D4-D7 (thermal K-resolved, crossover T_c) | H-D3 (Z_K partition 정량) |
| **G5** | H-E1-E3 (isoperimetric + Kramers), H-E6 (3 origin), H-E14 (lifetime) | H-E11 (β^{0.89} universality), H-E4 (Hessian scaling) |
| **G6** | H-F2 (smooth Morse 복원), H-F5-F7 (Witten/FP), H-F10 (Forman discrete) | H-F11-F12 (Reeb-K_soft), H-F13 (Floer) |

**Risk reminders (all G):** H-H1 (Lipschitz), H-H3 (Kramers on constrained), H-H5 (overfit), H-H8 (scope creep).

---

## J. Out-of-the-box (내일 scope 외, 후속 영감)

- **H-J1.** Categorical: SCC as sheaf on poset of thresholds. Persistence functor.
- **H-J2.** Information geometry: Fisher-Rao metric on u-space. Natural gradient.
- **H-J3.** Quantum-inspired: `ψ = √u`, `|ψ|² = u`. C_t 를 interference 로 재복원.
- **H-J4.** Symplectic: `T*Σ_m` Hamiltonian. T→0 classical, T>0 dissipative.
- **H-J5.** Random matrix: Hessian spectrum GOE/GUE. Large N limit.
- **H-J6.** Turing pattern: reaction-diffusion analog. K_soft = spot count.
- **H-J7.** Cellular automata: discrete u. Wolfram 에 가까움.
- **H-J8.** Neural field theory: brain dynamics analog.
- **H-J9.** Noncommutative geometry: graph Dirac operator.
- **H-J10.** RG flow with K_soft as relevant operator — scaling dimension 계산.

---

## 총계

- **A–F (deliverable 직접):** 76 가설
- **G (교차 구조):** 7
- **H (risk):** 11
- **J (out-of-scope):** 10
- **총 104 가설**

---

## 본 파일의 내일 역할

1. 에이전트는 G1 작성 전 §A 읽음 → H-A1 (persistence canonical) commit, H-A2 (Betti equivalence) 를 NQ-1 부분 해소 근거로, H-A7–A8 을 volume compatibility (Q1) 분석 base 로.
2. G2 작성 전 §B 읽음 → H-B1/B2 well-definedness 근거, H-B5 T→0 recovery 스케치 base.
3. G3 작성 전 §C 읽음 → H-C1–C4 (λ_K scaling 3 option + phase diagram) 를 λ_K scaling 논증 (Q2) 의 출발.
4. G4 작성 전 §D 읽음 → H-D4–D7 을 F-1 thermal re-reading 의 core.
5. G5 작성 전 §E 읽음 (가장 묵직) → H-E1–E3 (isoperimetric + Kramers), H-E6 (3 origin), H-E14 (lifetime 구체).
6. G6 작성 전 §F 읽음 → H-F2/F5/F7/F10 (4 Morse 대안 도구) 를 dissolution 의 richness 기반.
7. 각 deliverable 에 §H 의 해당 risk 기록 (Pending 섹션).

내일 실제 commit 은 가설 풀 중 일부만 — **사용자 판단 + 수학적 엄밀성** 기준. 본 파일의 가설 중 기각된 것은 저녁 canonical_sub.md 에 **Pending (고려했으나 채택 안 함)** 으로도 기록 가능.
