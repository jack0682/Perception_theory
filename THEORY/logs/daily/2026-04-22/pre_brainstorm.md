# Pre-Brainstorm — 2026-04-22 SF-S1 Hypothesis Map

**Written:** 2026-04-21 저녁 (post Round 12-18, SF-S1 plan 확정 직후).
**Author:** 사용자 + 에이전트 공동.
**Purpose:** 어제 저녁 Round 12-18 의 4 Cat A (Prop 1.3a/b + Cor 2.2 qual/quant) 기반으로, **multi-formation 을 single-formation invariants `(N_unst, ξ_0)` 로부터 derive 하는 새 관점**의 가설 map 구축. Plan.md 의 G1-G7 deliverables 진입 전 사용. 어제 저녁 NEB-중심 brainstorm 교체.
**Constraint:** 가설 목록이지 commit 아님. 각 가설은 (statement + reason + testability) 3 요소 포함.

**Scale:** ~80 가설, 12 sections.

---

## §0. 사용 가이드

1. 각 가설 H-X 에 **Why** (이유) + **Test** (검증 방법) 포함.
2. §A-D = multi-formation structure derivation (K̂, size, spacing, timescale).
3. §E-G = F-1/M-1/MO-1 dissolution 의 single-formation 언어 재정식화.
4. §H-I = NQ-32 SCC profile perturbation + cl_sep operator 구조.
5. §J = G-D (Aut(G) symmetry) placeholder (scope 밖).
6. §K = risks / counter-hypotheses.
7. §L = out-of-box connections (장기 영감).
8. 산출물 작성시 각 가설의 ID 로 cross-reference 가능.

---

## §A. K̂ — Mode-Count Emergence (10 가설)

어제 Round 12 의 Mode-Count Emergence (b) heuristic: `K̂ ~ 1 + √N_unst` on 2D grid. 검증 + 확장.

### H-A1. 1D cycle: K̂ ≈ N_unst (not √N_unst)

**Statement:** 1D cycle C_n 에서 K̂(β, α, c) = N_unst (Fiedler mode 가 연속적 cosine mode 쌍).

**Why:** 1D 에서 Laplacian eigenvalues 는 `λ_k = 2(1 − cos(2π(k−1)/n))`, eigenvectors 는 sinusoidal. 불안정한 각 mode 가 **독립된 두 개의 "+/-" half-cycle** 을 만듬 → 각 mode 당 1 formation.

**Test:** 1D cycle 위 find_formation 실행, find K̂ vs N_unst(β) 그래프. scc 에 1D cycle support 있는지 확인 (없으면 작성).

### H-A2. 2D grid: K̂ ≈ 1 + √N_unst (Round 12 heuristic)

**Statement:** 2D grid 에서 Fiedler mode 가 isotropic pattern — `√N_unst` 이 각 방향 mode 수.

**Why:** 2D grid Laplacian eigenvalues 는 `λ_{p,q} = 4 sin²(πp/L) + 4 sin²(πq/L)` — tensor product. `N_unst` 개 mode 중 `√N_unst × √N_unst` 가 typical pattern.

**Test:** exp_mode_emergence.py (작성됨) 실행. β ∈ {1.5, 3, 6, 12}·β_crit 스캔.

### H-A3. 3D 일반화: K̂ ≈ N_unst^{1/d}

**Statement:** d-dimensional lattice 에서 K̂ ≈ N_unst^{1/d}.

**Why:** d-D grid Laplacian eigenvalue distribution 이 d-차원 cosine 쌍 — isotropic spatial mode count 가 `N_unst^{1/d}`.

**Test:** 3D grid 지원시 실험. 현재 scc/ 는 2D grid 만 — extension 필요.

### H-A4. SBM (stochastic block model): K̂ ≈ # of block-aligned unstable modes

**Statement:** K block 의 SBM 에서 K̂ ≈ K (block 구조가 dominant Fiedler structure 를 고정).

**Why:** SBM 의 Laplacian 의 가장 낮은 non-zero eigenvalues 는 **K−1 개의 block-indicator eigenvectors**. 이것들이 β < β_crit 전에도 강한 Fiedler structure.

**Test:** SBM 위 `exp_hessian_uniform_v2` 변형 + mode emergence 측정.

### H-A5. Barbell: K̂ = 2 universally

**Statement:** Barbell graph (두 cluster + bridge) 에서 K̂ = 2 regardless of β.

**Why:** Cheeger h(G) 매우 작음 → λ_2 가 isolated. Fiedler mode 는 **bridge cut indicator**. Higher modes 는 intra-cluster → 쉽게 stabilize.

**Test:** exp51 이 barbell 에서도 K*=1 universal 확인 — K̂ short-time 도 K=1 인가 아니면 K=2 인가 (thermal/noise regime)?

### H-A6. K̂ dependency on temperature T

**Statement:** K̂(β, α, T, c) = #{k ≥ 2 : μ_k(T) < 0} 로 T 에 따라 변화. T = 0 에서 purely spectral, T > 0 에서 entropy 가 unstable range 를 좁힘.

**Why:** Round 4 Theorem 1.1 에서 `μ_k + T/(c(1-c))` — T 증가 시 모든 μ_k shift up → N_unst 감소 → K̂ 감소.

**Test:** exp_three_regime.py (작성됨) 실행. T ∈ {0.01, 0.1, 1, 5} 에서 K̂ 측정.

### H-A7. Crossover temperature for K̂ transition

**Statement:** T̄_k = `c(1-c)·[β|W''(c)| - 4α·λ_k]` (mode k 의 온도 경계). T 가 T̄_k 와 T̄_{k+1} 사이면 정확히 k-1 개 모드 불안정.

**Why:** Prop 1.3 의 direct consequence. Round 4 Thm 2.1 three-regime 의 refinement.

**Test:** 해석적 formula — 수치 검증은 exp_hessian_uniform 에 T 차원 추가.

### H-A8. Volume fraction c effect on K̂

**Statement:** c = 0.5 에서 K̂ 최대. c → spinodal 경계 (0.211 or 0.789) 에서 K̂ → 0 (bifurcation 사라짐).

**Why:** `W''(c)` 가 c = 0.5 에서 최대 크기 (절댓값 1). 경계에서 0 → β_crit → ∞.

**Test:** c ∈ {0.2, 0.3, 0.4, 0.5} 에서 K̂ 스캔.

### H-A9. Noise-amplitude dependence

**Statement:** K̂ ≈ N_unst only at small noise. Large noise → **K̂ increases** (noise itself seeds extra modes beyond linear instability).

**Why:** Langevin 의 stochastic forcing 이 모든 방향에 energy 주입 → stable modes 도 transient excitation.

**Test:** exp_mode_emergence.py 의 noise_amplitude 변화.

### H-A10. Finite-grid correction to K̂ formula

**Statement:** Small grid (n ≤ 100) 에서 K̂ 예측은 `1 + √N_unst` 보다 systematic **overestimate** (discretization effect).

**Why:** 작은 grid 에서 Fiedler mode 의 공간 구조가 grid size 와 비견 가능 → mode density 과평가.

**Test:** 여러 grid size 에서 K̂ vs N_unst slope — `1 + √N_unst` 로부터 deviation 측정.

---

## §B. Formation Size Distribution (8 가설)

### H-B1. Equal partition: m_k ≈ m/K̂ at short time

**Statement:** Short-time emergence 직후 각 formation 의 mass 는 `m / K̂` (uniform partition).

**Why:** Fiedler-mode saturation 이 ±half-cycle 대칭적 → mass 도 대칭.

**Test:** exp_mode_emergence.py 에서 각 formation 의 mass 측정 (watershed labeling + summation).

### H-B2. Long-time Ostwald ripening → unequal partition

**Statement:** t > t_Ostwald 에서 formations 간 mass 재분배 → dominant formation 1개 + 작은 formations. Lifshitz-Slyozov scaling.

**Why:** T-Merge (b) isoperimetric → larger formation 에 mass 흡수가 energetically 유리.

**Test:** Langevin long-time dynamics + mass histogram over time.

### H-B3. Critical size m_crit = π·r_0² with r_0 = √(m·ξ_0)

**Statement:** Formation 이 stable 하려면 최소 mass `m_crit ≈ π·ξ_0²·C` (interface cost 가 bulk gain 보다 낮아야).

**Why:** Classical nucleation theory. Interface cost `α·Per ≈ α·2π·r`, bulk energy gain `β·π·r²·ΔW`. Cross-over at r_crit ~ α/β = ξ_0².

**Test:** 작은 perturbation 에서 formation 이 살아남는 최소 크기 측정.

### H-B4. Volume constraint Σu = m 과의 relationship

**Statement:** Σ m_k = m (conservation) forces `K̂ ≤ m/m_crit` — K̂ 의 upper bound 는 volume 과 critical size 로부터.

**Why:** m_crit 보다 작은 formation 은 decay, 따라서 K̂ · m_crit ≤ m.

**Test:** Small volume fraction (c ≤ 0.1) 에서 K̂ 가 N_unst 보다 작은지 확인.

### H-B5. Graph topology 에 의한 constraint

**Statement:** `Aut(G)` orbit 이 K̂ 의 quantization 을 유도. 예: grid 는 K̂ ∈ {1, 2, 4, 9, ...} (square numbers).

**Why:** Aut(grid) = D_4 × translations. K̂ 개 formation 의 이상적 배치는 D_4-invariant subgroup 의 orbit.

**Test:** Grid vs random graph 에서 K̂ distribution 비교. Peaks at `(integer)²` ?

### H-B6. Mass-length scaling m_k ~ size_k^2 (2D)

**Statement:** 2D grid 에서 각 formation 의 linear extent `r_k ≈ √(m_k/π)`. Per_k ≈ 2π·r_k ≈ 2√(π·m_k).

**Why:** Isoperimetric inequality on 2D grid — disk shape minimizes perimeter.

**Test:** Linear regression size vs √mass per formation.

### H-B7. Fiedler-mode signature in mass distribution

**Statement:** Short-time `m_k` histogram 이 Fiedler mode amplitude distribution 과 correlate.

**Why:** Linear instability 직후 u ≈ c + Σ_{k unstable} a_k·φ_k. Nonlinear saturation 이 a_k → ± O(1) 로 고정하되 부호는 initial noise 로 결정.

**Test:** Fiedler eigenvectors 와 observed formation locations 의 cross-correlation.

### H-B8. Mass gap between "primary" and "secondary" formations

**Statement:** 대부분의 realization 에서 **largest formation 이 전체 mass 의 ~70-90%**, 나머지 K̂-1 개 formations 가 합쳐 10-30%.

**Why:** Nonlinear saturation 이 Fiedler mode 의 dominant amplitude 를 먼저 성장시키면 다른 mode 들이 suppression.

**Test:** Mass distribution histogram. Gini coefficient 측정.

---

## §C. Inter-Formation Spacing (8 가설)

canonical T-d_min-Formula 가 `d_min ∝ √(β/α)` 인데 이 dimensional 가 역순. Cor 2.2 quantitative 의 `ξ_0 = √(α/β)` 와 직접 충돌. 재측정 필요 (NQ-30).

### H-C1. Correct scaling: d_min* ∝ √(α/β) = ξ_0

**Statement:** Inter-formation minimum separation scales as ξ_0, **not** 1/ξ_0.

**Why:** Interface-interface interaction is via tail of exponential decay `exp(-κ·d) = exp(-d/ξ_0·√2)`. Decay length IS ξ_0, so minimum "non-interaction" distance scales with ξ_0.

**Test:** canonical T-d_min-Formula 실험 재측정, α 축 scan 추가. `d_min_new(α, β)` 가 `ξ_0` 와 비례하는지.

### H-C2. canonical formula `4.8 + 0.31·√(β/α)` 의 의미 재해석

**Statement:** 기존 formula 는 `4.8` baseline (lattice spacing O(1) minimum) + `0.31·√(β/α)` 가 실제로는 **formation size** 의 의존성 (β 증가 → sharper interface → 같은 formation 이 작아짐 → 더 많은 formation 가능 → 가상 spacing 감소).

**Why:** Fit 이 `formation size` 와 `spacing` 를 구별하지 못해서 coefficient 가 dimensionally 혼란된 것.

**Test:** exp_alpha_scan_v3 의 각 configuration 에서 formation 개수 × size × spacing 동시 측정. 분리된 회귀.

### H-C3. Spacing ~ Cheeger constant h(G)

**Statement:** `d_min* ≥ C/h(G)` for any connected graph.

**Why:** Cheeger inequality gives λ_2 ≥ h²/2. Interface interaction scale ∝ 1/√λ_2 = 1/κ ∝ 1/h.

**Test:** Graph topology 변화 (grid, barbell, expander) 에서 d_min 측정 + h(G) 와 비교.

### H-C4. Spacing 의 nonlinear correction term

**Statement:** `d_min*(α, β) = C_1·ξ_0 + C_2·log(β/α) + O(ξ_0³)` — logarithmic correction from tanh tail.

**Why:** Interface coupling 은 `exp(-d/ξ_0)·d` (multiplicative factor) → log correction.

**Test:** 4-point spacing fit: `log(d_min − C_1·ξ_0)` vs `log(β/α)`.

### H-C5. Minimum K̂ from volume + spacing

**Statement:** `K̂_max = floor(L² / (π·r_0² + 2π·r_0·d_min*))` — volume 이 허용하는 최대 formation 수.

**Why:** Each formation needs disk of area π·r_0² + surrounding "exclusion zone" of width d_min*/2.

**Test:** K̂ 가 `K̂_max` 에 saturate 하는지 — large β regime 에서 K̂ 더 이상 증가 안 하는 threshold.

### H-C6. Spacing robustness to closure (CN14)

**Statement:** Closure 가 `d_min*` 를 **축소** (canonical CN14 의 "30% reduction"). 이는 closure 의 self-reinforcement 가 formation 의 effective size 를 키우기 때문이 아니라 **interface coupling 을 suppress** 하기 때문.

**Why:** Closure 가 formation interior 의 field value 를 1 근처로 안정화 → interface tail 이 빨리 decay → closer packing 가능.

**Test:** w_cl = 0 vs w_cl = 1 에서 d_min* 직접 측정.

### H-C7. Disconnected graph 의 d_min 은 의미 상실

**Statement:** Disconnected graph 에서 inter-component spacing 은 잘 정의됨 (graph distance = ∞), 하지만 같은 component 내 formation 간 spacing 이 주요.

**Why:** Disconnected components 는 independent single-formation system 들.

**Test:** 2-component graph 에서 각 component 독립 분석.

### H-C8. Non-uniform c 의 공간적 varying spacing

**Statement:** If volume c varies spatially (e.g., external field), d_min*(x) 가 x 에 따라 변함. 공간 변화율 `|∇c|` 에 의해 modulate.

**Why:** Local c 변화 → local β_crit 변화 → local interface width.

**Test:** c(x) profile 있는 modified energy 에서 실험.

---

## §D. Timescale Structure (8 가설)

Multi-formation 의 dynamic view: emergence → metastable → coarsening.

### H-D1. Three timescales: t_emerge ≪ t_metastable ≪ t_coarsen

**Statement:** 
- **t_emerge ~ 1/|μ_{min}|** (fastest Fiedler mode saturation, unit of time)
- **t_metastable ~ ∞ at T=0, `exp(ΔF/T)` at T>0**
- **t_coarsen ~ ** big Ostwald ripening timescale

**Why:** Linear instability exponential → nonlinear saturation → Kramers escape → Ostwald.

**Test:** Langevin trajectory 의 K_soft(t) 3 regime 시각화.

### H-D2. t_emerge 의 universal scaling: `|μ_{min}|^{-1}`

**Statement:** t_emerge = α / (4α·λ_2·(β/β_crit − 1)) — standard spinodal time.

**Why:** Linear growth rate of most unstable mode = |μ_{min}|.

**Test:** exp_mode_emergence 의 early time (t < 10·dt) 의 K_soft(t) exponential fit.

### H-D3. t_metastable = τ_Kramers·exp(ΔF/T)

**Statement:** K̂ 가 감소하는 첫 번째 merge event 의 평균 시간은 Kramers escape.

**Why:** K→K−1 merge 는 energy barrier crossing. Freidlin-Wentzell theory.

**Test:** Low T Langevin 에서 first-merge 시간 histogram.

### H-D4. t_coarsen ~ L^2 (Lifshitz-Slyozov, 2D)

**Statement:** Late-stage coarsening follows `K(t) ~ t^{-1/2}` in 2D (LSW theory).

**Why:** Allen-Cahn 2D 의 classical scaling. SCC 에서 self-referential correction 으로 exponent 가 수정될 수 있음.

**Test:** Long Langevin 에서 K(t) power-law fit.

### H-D5. t_emerge / t_coarsen ratio 가 K̂ 관찰 가능 여부 결정

**Statement:** 실제 system 에서 K̂ 를 관찰하려면 `t_obs ∈ [t_emerge, t_coarsen]` 이어야 함. 짧으면 K̂ = 1 (아직 emerge 안 함), 길면 K̂ = 1 (이미 coarsen).

**Why:** Classical metastable window.

**Test:** Multiple observation times 에서 K_soft 측정.

### H-D6. Closure 가 t_metastable 을 expand

**Statement:** Closure (w_cl > 0) 가 ΔF 를 키워 Kramers exponent 를 증가 → t_metastable 증가.

**Why:** canonical CN14 "closure expands multi-formation stability" 의 dynamic 해석.

**Test:** w_cl = 0 vs w_cl = 1 에서 first-merge time 비교.

### H-D7. Two-formation merge barrier ∝ √(αβ) · Per_saddle

**Statement:** K=2 → K=1 merge 시 saddle 의 interface energy ≈ `√(αβ)·Per_saddle`.

**Why:** Modica-Mortola sharp-interface limit 에서 barrier 는 perimeter-dominated.

**Test:** NEB (어제 Stage 5 작업) 에서 saddle Per 측정 + fit.

### H-D8. Temperature-dependent t_emerge 역시 존재

**Statement:** T > 0 에서 t_emerge ~ 1/|μ_min| · (1 − T/T̄_2) — μ_min 에 T 의존이 있어 emergence 느림.

**Why:** H-A6 에서 T 가 μ_k 모두 shift up.

**Test:** exp_three_regime 의 mid-T regime 에서 emergence 속도.

---

## §E. F-1 Reframing — "K=2 vacuity" dissolution (7 가설)

### H-E1. F-1 은 integer-K language 의 artifact

**Statement:** "K=2 vacuity" 는 integer K 가 free parameter 일 때만 의미. Single-field u 에서는 vacuous — `N_unst ≥ 2` regime 에서 K≥2 가 자연 emergence.

**Why:** External m_j constraint 가 integer K 와 함께 도입된 파생 문제.

**Test:** F-1 재정식화 문서에서 integer-K vs single-field 를 비교 표.

### H-E2. 어제 C+E dissolution 과의 통합

**Statement:** 어제 `F1_dissolution.md` 의 C+E dissolution (thermal occupation) 과 오늘의 `N_unst` dissolution 은 **two different angles of the same phenomenon**. 전자 = thermodynamic, 후자 = kinetic.

**Why:** Thermodynamic 에서 K=2 가 Boltzmann-populated (T > T_c), Kinetic 에서 K=2 가 spontaneously emergent (β > β_crit^(2)).

**Test:** Round 18 의 3-tier status (mathematical / qualitative / SCC full) 와 compatible.

### H-E3. F-1 empirical evidence (exp62/63) 의 재해석

**Statement:** canonical exp62/63 의 "K=2 E ≈ 4.66 vs K=1 E ≈ 2.25" 는 **두 개의 서로 다른 local minima** (둘 다 Σ_m critical points). F-1 은 "vacuous" 가 아니라 "K=2 not global".

**Why:** Round 15 E-17 (multi-init essential) + Round 16 (Σ_m multiple minima).

**Test:** exp62/63 configuration 에서 `N_unst` 계산 + 두 minima 의 Morse index 측정.

### H-E4. F-1 이 multi-field K-architecture 에서 발생하는 것은 맞지만 single-field 에서 발생 안 함

**Statement:** canonical §12 의 K-field architecture (I9) 에서 `Σ^K_M = Σ_{m_1} × ... × Σ_{m_K}` 가 external m_j 가정 필요 — 이 level 에서는 F-1 이 valid. Single-field ℱ_C+E 에서는 F-1 이 ill-posed.

**Why:** Manifold structure 의 차이.

**Test:** `integer_K_dependency_map.md` 업데이트에서 F-1 이 K-field architecture 내 내재적 문제임을 explicit.

### H-E5. Retired K-theorems 의 재이해

**Statement:** 어제 retire 된 6개 정리 (T-Merge (a), Topological Lock, Coupling Bound 등) 는 **"K-field architecture 내 valid 하지만 single-field 에서는 vacuous"** — retire 는 not because wrong, but because not needed in new framework.

**Why:** Integer-K 는 single-field 의 derived concept (H-E1).

**Test:** 각 retired 정리에 "valid in K-field only" tag 추가.

### H-E6. F-1 의 canonical §11 "K>1 is kinetic" commitment 강화

**Statement:** canonical line 784 "multi-formation is kinetic" 가 본 감사로 **정량 내용** 획득 — "kinetic" = "Fiedler-mode instability emergence timescale t_emerge".

**Why:** F-1 의 vacuity claim 은 thermodynamic framing. Kinetic framing 에서는 K>1 이 natural.

**Test:** canonical §11 의 commitment 을 H-E1 + H-D2 와 cross-reference.

### H-E7. F-1 의 post-commit status

**Statement:** Prop 1.3 Cat A commit 후 F-1 은 **완전 dissolve**. 잔여 문제는 NQ-32 (profile perturbation) 뿐.

**Why:** Integer-K 가 derived, vacuity framing 이 의미 상실.

**Test:** `F1_dissolution.md` 의 post-Round 18 섹션에 명시.

---

## §F. M-1 Reframing — "K=1 always preferred" feature not bug (7 가설)

### H-F1. M-1 은 two-timescale confounding

**Statement:** M-1 의 "K=1 always preferred" 는 **long-time thermodynamic limit** 의 진술. Short-time `N_unst ≥ 2` emergence 는 K≥2 가 preferred. M-1 은 두 timescale 의 혼동.

**Why:** T-Merge (b) Cat A 는 global minimum statement. Emergence 는 kinetic.

**Test:** Dynamic Langevin: early time K̂, late time K=1 각각 측정.

### H-F2. M-1 의 canonical proof (T-Merge (b)) 는 유효

**Statement:** T-Merge (b) 의 isoperimetric proof (Γ-convergence) 는 건재. M-1 은 T-Merge (b) 의 **framing 오독** 이었음.

**Why:** Framing: "K=1 always globally preferred" (맞음) vs "K>1 never emerges" (틀림).

**Test:** T-Merge (b) proof 는 수정 불필요. Framing 수정만 dissolution 파일에.

### H-F3. M-1 의 disconnected graph exception

**Statement:** M-1 은 connected graph 만 성립. Disconnected graph 에서는 K=#components 가 global minimum.

**Why:** Isoperimetric on connected graph. 어제 02_development §4.5 에서 식별.

**Test:** 2-component graph 에서 K* measurement.

### H-F4. Kramers metastability 의 정량 내용

**Statement:** K=2 → K=1 merge 의 mean first-passage time `τ ~ exp(ΔF/T)` 은 **effectively infinite at T = 0**. 따라서 T=0 에서 K=2 는 "forever metastable" — M-1 의 "preferred" 는 time-infinite limit.

**Why:** 어제 C+E Kramers framework (G5).

**Test:** Kramers formula 의 저온 regime.

### H-F5. M-1 과 CN6 ("K kinetically determined") 의 통일

**Statement:** CN6 의 "kinetic" = Fiedler mode instability + Kramers escape. 두 mechanism 이 합쳐서 observed K 를 결정.

**Why:** H-A6 + H-D3 + H-F4 의 통합.

**Test:** canonical §11 "Three Pillars" (Nucleation, Metastability, Coarsening) 가 (N_unst, ξ_0, τ_Kramers) 로 각각 mapping.

### H-F6. 어제 M1_dissolution 의 Kramers 부분과 오늘 Reframing 의 관계

**Statement:** 어제 M-1 의 C+E Kramers dissolution 은 **long-time exit rate**. 오늘 reframing 은 **short-time emergence**. 두 부분이 함께 M-1 을 완전 dissolve.

**Why:** Complementary timescales.

**Test:** `M1_dissolution.md` 재정식화 섹션에서 두 부분을 명시.

### H-F7. M-1 의 exp38 γ_eff=0.89 finding 과의 관계

**Statement:** exp38 의 barrier exponent γ_eff = 0.89 는 **specific protocol** 측정치. Round 11 Stage 5 NEB 에서 재현 불가. ΔF(K̂=2 → K̂=1) 이 graph/β/α/c 에 따라 protocol-dependent 하다는 Round 6 §1 honest closure 의 유지.

**Why:** 어제 Round 11 결과.

**Test:** 본 재정식화에서 γ_eff 문제는 **scope 밖** (C-S2 carry).

---

## §G. MO-1 Reframing — "Morse inapplicable" (6 가설)

### H-G1. MO-1 은 Σ²_M manifold choice 의 artifact

**Statement:** Σ²_M = Σ_{m_1} × Σ_{m_2} 가 **제품 manifold** — K-field architecture 의 구조물. Single-field Σ_m 는 smooth convex polytope. Morse 는 **Σ_m^ε \ V (smooth interior) 에서 well-defined**.

**Why:** 어제 G6 + 오늘 G-C.

**Test:** canonical §13 Prop 1.1 (Σ_m is convex polytope, manifold with corners) + Round 16 (Prop 1.3 on Σ_m^ε interior) 통합.

### H-G2. K_hard = Morse index counts on Σ_m

**Statement:** `K_hard(β, α, G, c) = N_crit(Σ_m, ℱ) / |Aut(G)|` where N_crit = number of local minima.

**Why:** 어제 G-C formulation. `K_hard` 는 canonical 의 integer K, 지금까지 external assumption.

**Test:** NQ-31 — Multi-init Morse index survey 로 lower bound.

### H-G3. Morse inequality 의 constraint

**Statement:** `N_crit_k ≥ b_k(Σ_m^ε)` for each index k. Σ_m^ε 는 polytope interior — contractible (Prop 1.1) → b_0 = 1, b_k = 0 for k≥1.

**Why:** Morse inequality.

**Test:** Σ_m^ε 의 Euler characteristic = 1. K_hard 의 minimum count = 1 (global min exists).

### H-G4. Stratified Morse for corners

**Statement:** Σ_m 의 corners (u_i ∈ {0,1}) 는 stratified singularities. Goresky-MacPherson stratified Morse 가 necessary extension.

**Why:** Σ_m 은 manifold with corners, interior 만 smooth.

**Test:** Corners 에 boundary critical points 있는지 search.

### H-G5. Witten Laplacian 이 MO-1 의 spectral 대안

**Statement:** 어제 G6 의 Witten Laplacian framework 이 MO-1 dissolution 의 spectral variant. Morse 의 discrete graph extension.

**Why:** H-S 1985 + Coupling Bound Item 5 의 decay.

**Test:** Witten Δ 의 small eigenvalue 수 = K_hard (경험적).

### H-G6. Forman discrete Morse 의 combinatorial 대안

**Statement:** 어제 G6 의 Forman framework. Σ_m 의 simplicial decomposition 위 combinatorial Morse.

**Why:** Alternative to smooth Morse.

**Test:** Forman critical cells 와 Morse index 일치 (combinatorial 실험).

---

## §H. NQ-32 — SCC Profile Perturbation (8 가설)

Round 18 의 핵심 발견: SCC full ℰ 의 K=1 minimizer 가 pure tanh 에서 deviation. cl_sep structural operator 가 원인.

### H-H1. Profile shape = tanh × (1 + ε·cl_sep_correction)

**Statement:** u*_SCC(s) ≈ u*_tanh(s/ξ_0) · (1 + ε(β, α, G)·v_cl_sep(s)) where v_cl_sep 은 cl_sep eigenmode.

**Why:** First-order perturbation of Allen-Cahn by cl + sep.

**Test:** Profile fit (exp_profile_fit.py) 의 residual 분석.

### H-H2. ε(β, α) scaling 의 가설

**Statement:** `ε ~ |H_cl_sep|·ξ_0` — cl_sep 의 operator norm × interface scale.

**Why:** Perturbation theory: correction ~ perturbation strength × length scale.

**Test:** ε(β, α) 측정 + scaling fit.

### H-H3. Effective ξ_0^{fitted} vs theoretical √(α/β)

**Statement:** ξ_0^{fitted} = √(α/β) · (1 + δ(β, α)), δ = O(ξ_0).

**Why:** cl_sep 이 interface shape 을 subtly perturb — effective width 가 shift.

**Test:** radial tanh fit + ξ_0^{fitted} extraction.

### H-H4. Profile deviation 이 formation size 에 미치는 영향

**Statement:** ξ_0^{fitted} > ξ_0^{theoretical} → effective formation 이 기대보다 larger.

**Why:** H-H1 의 cl_sep correction 가 interface 확장.

**Test:** Formation `|Core|` 실측 vs Cor 2.2 예측 비교.

### H-H5. Closure effect isolation

**Statement:** cl_sep 의 contribution 중 **closure (E_cl)** 와 **separation (E_sep)** 가 독립적으로 다른 shape correction.

**Why:** 어제 Round 16 에서 w_cl/w_sep 둘 다 1 로 측정 — 개별 분리 안 됨.

**Test:** w_cl ∈ {0, 1}, w_sep ∈ {0, 1} 네 조합 Hessian 측정.

### H-H6. Profile asymmetry

**Statement:** cl_sep 의 non-symmetric spectrum (negatives vs positives) 가 interface profile 을 **asymmetric** 하게 — interior vs exterior side 에서 다른 decay.

**Why:** E_sep 의 self-reference (D(x; 1-u)) 가 interior/exterior 구별.

**Test:** Radial profile 의 u_in / u_out asymmetry 측정.

### H-H7. Self-referential correction 의 RG interpretation

**Statement:** cl_sep 이 effective `(α, β)` 를 **dress** — renormalized values `α_eff, β_eff`.

**Why:** RG block-spin analog.

**Test:** RG-like analysis — `ξ_0^{fitted}` 로부터 `α_eff/β_eff` 역추출.

### H-H8. Profile shape 이 graph topology 의존

**Statement:** Grid vs SBM vs barbell 에서 profile correction 형태가 다름. Grid 에서 가장 작은 deviation (Aut(G) 가 richest).

**Why:** Symmetry 가 cl_sep eigenmode structure 를 제약.

**Test:** Multi-graph profile fit 비교.

---

## §I. cl_sep Structural Operator (6 가설)

어제 Round 16 의 핵심 발견: `H_cl_sep` 이 β-invariant 구조 operator.

### H-I1. cl_sep spectrum 의 graph-spectral interpretation

**Statement:** H_cl_sep eigenvalues 가 **graph Laplacian spectrum 의 polynomial function**. 예: `H_cl_sep ≈ P(L_G) + Q(L_G)` for 일부 poly P, Q.

**Why:** cl, sep 둘 다 graph operations (kernel P_t, D_t) — Laplacian functional 로 표현 가능 가설.

**Test:** H_cl_sep 의 Laplacian eigenbasis 에서 대각화 시도.

### H-I2. cl_sep 의 1641 negatives 가 graph-structural

**Statement:** 1641 ≈ 0.4·n 은 2D grid 의 **specific spectral property** — 다른 graph 에서 다른 fraction.

**Why:** Graph-dependent.

**Test:** SBM, barbell, random geometric graph 에서 cl_sep negative count 측정.

### H-I3. cl_sep 의 dominant eigenvectors 와 Fiedler 의 관계

**Statement:** cl_sep 의 가장 큰 negative eigenvalue 의 eigenvector 가 Fiedler mode φ_2 에 가까움.

**Why:** 둘 다 "large-scale partition" favored.

**Test:** 내적 `⟨v_cl_sep^{(1)}, φ_2⟩` 측정.

### H-I4. cl_sep 의 α 의존성

**Statement:** α 증가 → cl_sep spectrum 좌표이동 없이 shape 유지 (cl/sep 는 α 무관 항).

**Why:** E_cl, E_sep 의 Hessian 이 α 에 독립 (E_bd 만 α 포함).

**Test:** α ∈ {0.1, 1, 10} 에서 cl_sep spectrum 동일한가 확인.

### H-I5. Closure vs separation 의 개별 기여

**Statement:** `H_cl` 은 **positive semi-definite** (closure FP Hessian 구조), `H_sep` 은 **indefinite** (self-referential D 가 mixed sign). 1641 negatives 는 H_sep 지배.

**Why:** E_cl(u) = ||Cl(u) − u||² 는 least-squares, positive semi-definite. E_sep 는 self-reference.

**Test:** H_cl, H_sep 개별 측정 (H-H5 와 연계).

### H-I6. cl_sep 이 uniform 이외 config 에서의 구조

**Statement:** K=1 minimizer 에서 H_cl_sep 는 uniform 때와 다른 구조 — more concentrated near interface region.

**Why:** Closure / separation operator 가 spatially varying (formation interior vs exterior).

**Test:** K=1 minimizer 에서 H_cl_sep 측정 + 비교.

---

## §J. G-D — Aut(G) Symmetry (5 가설, scope 밖 placeholder)

G-D 는 본 plan 의 non-goal 이나 후속을 위한 placeholder.

### H-J1. K=1 formation 의 moduli space = Σ_m/Aut(G)

**Statement:** K=1 minimizer orbit 은 Aut(G) 작용 하 single orbit. Moduli space 는 quotient.

**Why:** Group action on solution space.

**Test:** Grid 에서 K=1 formations 이 translation/rotation 에 의해 일관되게 mapped.

### H-J2. Fiedler mode degeneracy 가 K=2 orbit 를 결정

**Statement:** 2D grid 에서 λ_2 가 2-fold degenerate ((1,0) + (0,1)) → K=2 formations 의 방향 orbit 가 Aut(G) 에 의해 enumerate.

**Why:** Degenerate eigenvalue + group action.

**Test:** K=2 configurations 의 orientation histogram.

### H-J3. Higher-K moduli space 의 structure

**Statement:** K̂ formations 의 moduli space = configuration space of K̂ points on graph / Aut(G).

**Why:** Symmetric product of positions.

**Test:** K=3, 4 에서 configurations enumerate.

### H-J4. Symmetry breaking 의 Ising-like phase structure

**Statement:** β increase → Aut(G) symmetry spontaneously broken → specific K̂ realization selected.

**Why:** Standard Ising-like symmetry breaking picture.

**Test:** Long Langevin 의 K̂ 및 orientation distribution (ergodic vs broken).

### H-J5. Graph symmetry 와 K_hard quantization

**Statement:** K_hard ∈ `{orbit sizes of Aut(G)}` — 특정 quantization.

**Why:** Aut(G) orbit 가 물리적으로 equivalent configurations.

**Test:** Grid (D_4) 에서 K_hard ∈ {1, 2, 4, 8, ...}.

---

## §K. Risks / Counter-Hypotheses (6 가설)

### H-K1. K̂ formula 가 grid 밖에서 breakdown

**Risk:** 비 regular graph (random, scale-free) 에서 K̂ ~ f(N_unst) heuristic 실패. Grid-specific pattern 일 뿐.

**Why:** Fiedler mode structure 가 graph 에 따라 크게 달라짐.

**Mitigation:** H-A1~5 의 graph-specific hypotheses 각각 검증.

### H-K2. cl_sep structural discovery 의 scope

**Risk:** H_cl_sep 의 β-invariance 가 uniform 에서만 — K=1 minimizer 에서는 β-dependent 가 될 수 있음.

**Why:** Minimizer location 이 β 에 의존 → Hessian location 도 의존.

**Mitigation:** H-I6 검증 (K=1 minimizer 에서 H_cl_sep 측정).

### H-K3. Multi-formation 의 cl_sep effect 예측 불가

**Risk:** K≥2 configurations 의 interface profile 및 formation arrangement 가 cl_sep 에 의해 qualitatively perturb 될 수 있음. Pure Allen-Cahn picture 가 quantitatively off.

**Why:** cl_sep 의 non-trivial structure.

**Mitigation:** K=2 configurations 의 profile fit + cl_sep 보정 직접 측정.

### H-K4. Discretization floor 의 재등장

**Risk:** Multi-formation 에서도 small ξ_0 regime 에서 discretization 이 theory 와 decouple.

**Why:** 어제 Round 14 + v2 alpha_scan 에서 관찰된 패턴.

**Mitigation:** 큰 grid (≥ 96) 에서만 결론 도출.

### H-K5. 시간 부족 위험

**Risk:** 어제 3 세션 연속 (morning, afternoon, evening) → 오늘 energy depleted 가능.

**Why:** Fatigue.

**Mitigation:** 본 plan minimum = G1 + G2. G3-G7 은 carry 가능.

### H-K6. Over-commitment 에 의한 Cat A 경 commit

**Risk:** 4 Cat A candidates 를 너무 빠르게 canonical 화 → 추후 retraction 필요.

**Why:** 수치 검증은 Cat A 수준이나 수학적 proof 의 통일성은 아직.

**Mitigation:** working/SF/ 에만 commit, canonical 직접 수정은 Stage 6 까지 대기.

---

## §L. Out-of-the-box Connections (6 가설, 장기 영감)

### H-L1. Quantum mechanics analogy (canonical QM-1~4 확장)

**Statement:** Witten Laplacian ↔ Schrödinger. cl_sep operator ↔ non-Hermitian Hamiltonian.

**Why:** canonical §11.3 QM framework.

**When to activate:** Post-Stage-1 spectral work.

### H-L2. Renormalization group (NQ-10)

**Statement:** `(N_unst, ξ_0)` 가 scale-dependent. Coarse-graining 에서 effective β/α flow.

**Why:** RG on Allen-Cahn.

**When:** Stage 3 (Definition & Derivation).

### H-L3. Reaction-diffusion pattern formation (Turing)

**Statement:** SCC 의 multi-formation 이 Turing pattern 의 discrete graph analog.

**Why:** Fiedler mode + nonlinear saturation 이 Turing 과 동일 structure.

**When:** Extension work.

### H-L4. Information geometry on u-space

**Statement:** Fisher-Rao metric on `[0,1]^n` 가 SCC 의 natural gradient 구조.

**Why:** canonical §8.7 Shahshahani metric 언급.

**When:** NQ-10 후속.

### H-L5. Stochastic thermodynamics

**Statement:** Langevin SCC 의 fluctuation-dissipation relations 가 emergence 시의 entropy production 를 quantify.

**Why:** T>0 regime 의 natural framework.

**When:** Stage 5 numerical / Langevin 구현 후.

### H-L6. Neural manifold hypothesis

**Statement:** 생물학적 neural population dynamics 가 SCC 의 multi-formation 으로 model 가능. Each formation = neural assembly.

**Why:** Ontological analog (soft cohesion ↔ coherent neural ensemble).

**When:** Out of math scope; cognitive paper direction.

---

## §M. 우선순위 요약

| Section | Priority | 관련 Goal |
|---|---|---|
| **§A K̂ emergence** | HIGH | G3 (from_single) |
| **§B Formation size** | MEDIUM | G3 |
| **§C Spacing** | HIGH | G3, G6 (integer_K_dep) |
| **§D Timescale** | MEDIUM | G3 |
| **§E F-1 reframe** | HIGH | G4 |
| **§F M-1 reframe** | HIGH | G4 |
| **§G MO-1 reframe** | HIGH | G4 |
| **§H Profile pert** | MEDIUM | G5 (profile_fit script) |
| **§I cl_sep operator** | MEDIUM | G1 (working/SF/mode_count) |
| **§J Aut(G)** | LOW | post-Stage-1 |
| **§K Risks** | HIGH | 전체 |
| **§L Out-of-box** | LOW | future |

**Total: 80 hypotheses**, 어제 57 대비 +40% — 새 관점 확장이 많음.

---

## §N. Hypothesis ID Cross-Reference Map

**K̂ formula 관련**: H-A1, H-A2, H-A3, H-A4, H-A5 — graph-specific K̂ structure.

**(N_unst, ξ_0) 의 multi-formation derivation**: H-B1, H-C1, H-C5 — direct derivation from single-formation.

**Timescale 3-regime**: H-D1, H-D2, H-D3, H-D4, H-D5 — emergence → metastable → coarsening.

**F-1/M-1/MO-1 통합 framework**: H-E1, H-F1, H-G1 — 3 Critical 의 single-formation dissolution.

**NQ-32 조사 체계**: H-H1, H-H2, H-H3, H-H4 — profile fit + effective ξ_0.

**cl_sep operator deep structure**: H-I1, H-I5, H-I6 — structural property.

**Risk management**: H-K1, H-K5, H-K6 — scope + fatigue + over-commit.

---

## 사용 가이드 (작성시)

1. G1 `working/SF/` 작성시: H-E1, H-F1, H-G1 의 language 사용.
2. G3 `working/MF/from_single.md` 작성시: §A, §B, §C, §D 의 가설들을 직접 인용.
3. G4 dissolution 재정식화: §E, §F, §G 각각의 가설 풀에서.
4. G5 profile_fit script: §H 의 H-H1, H-H3 이 fit 대상.
5. G6 integer_K_dep 업데이트: §C 의 H-C1, H-C2 로 `d_min*` 재측정 motivate.
6. G7 errata cleanup: §K-H-K6 에 따라 conservative.

---

## 가설 풀 통계

| Section | 가설 수 | 평균 granularity |
|---|---|---|
| A (K̂ emergence) | 10 | medium-heavy |
| B (size) | 8 | medium |
| C (spacing) | 8 | medium-heavy |
| D (timescale) | 8 | medium |
| E (F-1 reframe) | 7 | medium |
| F (M-1 reframe) | 7 | medium |
| G (MO-1 reframe) | 6 | medium |
| H (profile pert) | 8 | medium-heavy |
| I (cl_sep) | 6 | medium |
| J (symmetry) | 5 | light (scope 밖) |
| K (risks) | 6 | light |
| L (out-of-box) | 6 | light |
| **TOTAL** | **85** | — |

**어제 pre_brainstorm**: 57 가설 (NEB-focused). **오늘**: 85 가설 (SF consolidation + MF reframe). 확장된 scope.

---

**End of 2026-04-22 SF-S1 pre-brainstorm.**

**Meta**: 본 brainstorm 은 **어제 Round 18 완료 직후 (저녁) 작성**. SF-S1 의 G1-G7 deliverables 의 이론적 material 을 85 가설로 preview. 세션 중 각 가설의 USED / PARKED / REJECTED / UNTOUCHED 분류는 세션 말 04_hypothesis_audit.md 에서 수행.
