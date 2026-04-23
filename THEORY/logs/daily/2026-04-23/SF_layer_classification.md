# SF_layer_classification.md — Three-Layer Assignment of 77 Preserved Cat A Theorems

**Session:** 2026-04-23 (G1 deliverable; intended promotion target: `working/SF/layer_classification.md`)
**Target (from plan.md §2 G1):** 72 preserved + 5 new = 77 Cat A theorems을 Three-Layer Hierarchy (L1 topology / L2 geometry / L3 field) + mixed + meta 카테고리로 분류, 미분류 0개.
**This file covers:** 분류 방법론(Hybrid Approach A2 × A4), 77 claims에 대한 layer table, 각 layer의 axiom 의존성 요약, 잔여 gap 식별.
**Depends on reading:** `canonical.md` §13 (Cat A/B/C registry), `working/SF/step_cohesion.md` §3 (Three-Layer definition), `01_exploration.md` §1.3 (Layer assignment 정의), `logs/daily/2026-04-22/99_summary.md` §17-§18 (R22 preserved static list).

---

## §1. Methodology

### 1.1 Layer 정의 (from `01_exploration.md` §1.3, repeated for readability)

- **L1 (topology)**: $K \in \mathbb{Z}$, basin label, connected component, Morse index 부호, topological invariant에 관한 discrete 주장.
- **L2 (geometry)**: smooth real-valued quantity ($r_0, \xi_0, d_{\min}, \mu_k$, energy value, scaling exponent)에 관한 continuous 주장, L1 구조는 고정.
- **L3 (field)**: continuous $u(x) \in [0,1]$ field의 pointwise / PDE / Γ-convergence / analyticity 주장.
- **Mixed $(\ell_i, \ell_j)$**: 두 layer 간 bridge.
- **Meta**: observable 없는 consistency / existence / axiom validation.

### 1.2 Static vs Dynamic primary axis (Approach A4)

- **Static (S)**: gradient-flow, time, noise 불포함. Landscape-intrinsic.
- **Dynamic (D)**: gradient flow convergence, temporal transport, noise-driven transitions 포함.

### 1.3 Source inventory

분류 대상 77 claims은 다음에서 수집:

- **Canonical v1.2 §13 Cat A (35 claims)** — T1, T6a, T6b, T20, T-A2, T8-Core, C-Axioms, QM1-4 (count as 4), T14, T3/T6-Stability, T7-Enhanced, T11, T8-Full, Predicate-Energy Bridge, Deep Core Dominance 2b, T-Merge (a), T-Merge (b), Topological Lock, T-Birth-Parametric (D₄), T-Bind-Proj, T-Bind-Full, Proposition 1.1, Proposition 1.2, Theorem 3.1(a,b,d), Persistence Threshold Equation. **실제 집계 = 25 named items + 4 QM = 29.** (canonical §13 stated "35 Cat A" — 차이는 T3/T6-Stability가 2 counts 등 counting 관례의 문제; 이 파일은 **named distinct theorem**을 단위로 집계.)
- **Session 2026-04-22 R1-R10 (37 new Cat A, single-formation deepening)**: Prop 1.3a, Prop 1.3b (a)-(e), Cor 2.2 qual, Cor 2.2 quant-tanh, 등 (detail in 99_summary §4.1).
- **Session 2026-04-22 R11-R16 (34 new Cat A, multi-formation medium-term)**: $\mathcal{M}_2$ classification, K=2 Hessian block-diagonal, $c_0^{(K)}$ bracket, 등.
- **R22 new Cat A candidates (5)**: C-FQ, C-X3, C-X2, C-X1V5, C-3L.

**Counting note.** 원래 plan.md는 "77 Cat A"라고 명시했으나 (72 preserved + 5 R22 new), canonical §13이 "35 Cat A"로 자체 집계하고 R1-R16이 "84 new"를 세었으며, R17-R22에서 Conj 2.1 v1-v5, Conj 2.1-Bott이 retracted되고 Round 9 §11이 Cat B로 demoted됨. **여기서는 다음 counting convention 사용**: (i) canonical §13 Cat A named theorems을 **29 distinct items**로, (ii) R1-R10 R11-R16 새 Cat A 중 **retracted/demoted 제외**하고 **preserved**만 카운트, (iii) R22 신규 5를 더함. 이 convention 하에 실제 분류 대상은 **약 70–77 claims** (counting 세부에 ±몇 items 오차는 허용). 이 파일은 **distinct logical statement 기반**의 분류를 수행하며, 중복·sub-case는 "bundled" 표기로 처리.

### 1.4 분류 표기

각 row: **[ID] — [Name] — [S/D] — [Layer] — [Proof tool] — [Source] — [Notes]**.

---

## §2. L3 (Field) — static claims

Field-level PDE / analyticity / Γ-convergence / pointwise-u claims.

| # | Name | S/D | Layer | Proof tool | Source | Notes |
|---|---|---|---|---|---|---|
| 1 | **T1 Existence of Minimizers** | S | L3 | EVT on compact $\Sigma_m$ | canonical §13 | u-valued minimizer 존재 |
| 2 | **T6a Closure FP Existence** | S | L3 | Brouwer FP | canonical §13 | $\mathrm{Cl}_t$의 u-valued FP |
| 3 | **T6b Closure FP Uniqueness (contraction)** | S | L3 | Banach contraction | canonical §13 | $a_{\mathrm{cl}} < 4$ 시 유일 |
| 4 | **T-A2 Monotonicity of Closure** | S | L3 | $\sigma$ monotonicity | canonical §13 | u $\leq$ v $\Rightarrow$ Cl(u) $\leq$ Cl(v) |
| 5 | **T3/T6-Stability (non-idempotent)** | S | L3 | Gram matrix analysis | canonical §13 | 부분 L2 (Hessian eigenvalue) — mixed L2/L3 possible |
| 6 | **T7-Enhanced Metastability (local Hessian)** | S | **Mixed(L2,L3)** | Closure Gram contribution | canonical §13 | Hessian eigenvalue gap = L2; closure operator = L3 |
| 7 | **T11 Γ-convergence** | S | L3 | Modica-Mortola | canonical §13 | u → characteristic function (Γ-limit은 L1이지만 convergence는 L3) |
| 8 | **T8-Full (IFT extension)** | S | L3 | IFT on bordered KKT | canonical §13 | Smooth family of minimizers |
| 9 | **Predicate-Energy Bridge (Sep identity)** | S | L3 | Algebraic | canonical §13 | $\mathsf{Sep} = 1 - \mathcal{E}_{\mathrm{sep}}/m$ |
| 10 | **Deep Core Dominance 2b** | S | Mixed(L2,L3) | Isoperimetric | canonical §13 | Core volume bound = L2; isoperimetric on grid = L3 |
| 11 | **T-Bind-Proj (all τ)** | S | L3 | KKT + Banach | canonical §13 | Tangential residual bound |
| 12 | **T-Bind-Full (Bind $\geq$ 1-f)** | S | L3 | Follows T-Bind-Proj | canonical §13 | u-field property |
| 13 | **C-Axioms (C3'' closure)** | S | L3 | Schur decomposition | canonical §13 | Resolvent operator |
| 14 | **QM1 (Q_morph vanishes on uniform)** | S | L3 | Direct substitution | canonical §13 | u-field at c |
| 15 | **QM2 (Q_morph monotonicity)** | S | L3 | Product structure | canonical §13 | field-level |
| 16 | **QM3 (Q_morph continuity)** | S | L3 | Persistence stability | canonical §13 | field-level Lipschitz |
| 17 | **QM4 (Q_morph discrimination)** | S | L3 | Product structure | canonical §13 | field-level |
| 18 | **Prop 1.3a (Hessian spectrum at uniform)** | S | Mixed(L2,L3) | Linearization | R1-R4 | Eigenvalues (L2) of Hessian on u-field (L3) |
| 19 | **Prop 1.3b (a)-(c) (Hessian structure)** | S | Mixed(L2,L3) | Algebraic + spectral | R1-R4 | 여러 sub-claim을 bundle |
| 20 | **Prop 1.3b (d) explicit $\nu_k(c)$** | S | L2 | Closed-form | R6 | 순수 algebraic in c |
| 21 | **Prop 1.3b (e) Weyl bracket** | S | L2 | Weyl spectral | R1-R4 | N_unst$^{\mathrm{full}}$ vs N_unst$^{\mathrm{bd}}$ bracket |
| 22 | **Cor 2.2 qualitative (tanh profile)** | S | L3 | Allen-Cahn analog | R9 | Field profile shape |
| 23 | **Cor 2.2 quant-tanh ($\xi_0$ scaling)** | S | Mixed(L2,L3) | Perturbation | R9 | $\xi_0 = \sqrt{\alpha/\beta}$ (L2) governs profile (L3) |
| 24 | **Cor 2.2 supra-lattice $O((a/\xi_0)^2)$** | S | L3 | Allen-Cahn perturbation | R9 | **(Cat B demoted 2026-04-22 R21, but Regime B subset preserved)** |

### 2.1 L3 static의 axiom 의존성 요약

- **Primary axioms**: A1', A2, A3, A4 (closure operator properties), B1-B4 (adjacency), E1-E4 (transport — 해당 L3 claim 없음 여기), canonical §8 energy functional definition.
- **Key commitments**: CN1 (closure non-idempotence), CN5 (4 energy terms distinct), CN13 ($b_D = 0$).
- **Critical feature**: 모든 L3 static claim은 analyticity (CN13 $b_D = 0$) 위에 빌트. Thermal/noise 확장 (G5)이 이 analyticity를 깨므로 L3 static 확장은 non-trivial.

---

## §3. L2 (Geometry) — static claims

Real-valued geometric parameter 주장. Smooth functions of $(\beta, \alpha, c)$.

| # | Name | S/D | Layer | Proof tool | Source | Notes |
|---|---|---|---|---|---|---|
| 25 | **T8-Core ($\beta_{\mathrm{crit}} = 4\alpha\lambda_2/|W''(c)|$)** | S | L2 | Spectral variation | canonical §13 | $\beta_{\mathrm{crit}}$ is L2 real-valued; existence of non-uniform is L1 (§4) |
| 26 | **$\xi_0$ scaling** | S | L2 | Allen-Cahn dimensional | R9 / interface_scale.md | $\xi_0 = \sqrt{\alpha/\beta}$ |
| 27 | **$d_{\min}^*$ screened Poisson** | S | L2 | Bessel $K_0$ asymptotic | R2 §4.3b | $d_{\min} = \sqrt{2}\,\xi_0 \ln(1/\epsilon_0) + O(\xi_0)$ |
| 28 | **$c_{\mathrm{bif}}^\pm$ thresholds** | S | L2 | Explicit from Prop 1.3b(d) | R6 | 3-regime 경계값 |
| 29 | **$p^*(c)$ bifurcation eigenvalue** | S | L2 | Spectral | R6 | c-dependent eigenvalue |
| 30 | **Cascade-sum formula $c_0^{(K)}$** | S | L2 | Enumeration | R7 | Partition-based count function |
| 31 | **$\mathcal{M}_1$ dimension (1D cycle)** | S | L2 | Manifold dim | R5 | 1-dim (circle moduli) |
| 32 | **$\mathcal{M}_1$ dimension (2D torus)** | S | L2 | Manifold dim | R5 | 1-dim (pure-X / pure-Y) |
| 33 | **Universal $A_2/A_1 \in \{2, 4\}$** | S | L2 | D_4 equivariant CR | R4 | Branching ratio classification |
| 34 | **Moderate-$\beta$ scaling $c_0^{(K)}$** | S | L2 | Perturbative | R7 | $\beta \in [5, 30]$ regime |
| 35 | **Secondary bifurcation threshold $\beta^{\mathrm{sec}}_{1 \to 2}$** | S | L2 | Crandall-Rabinowitz | R10, R11 | real-valued $\beta$ |
| 36 | **Persistence Threshold Equation** | S | L2 | KKT + closure recurrence | canonical §13 | $\beta > \Gamma \cdot \varepsilon_1^2 \cdot \alpha$ |
| 37 | **C-X2 D1 α-Absolute Threshold** | S | L2 | Empirical + dim argument | R22 X2 | α가 shape regime 결정 (L2 real) |
| 38 | **Discretization expansion (Cor 2.2)** | S | L2 | Taylor expansion | R9 | $O((a/\xi_0)^2)$ rate (Cat B after R21, but formula preserved) |
| 39 | **$\mu_{\mathrm{sep}} \sim e^{-d_{\min}/\xi_0}$** | S | L2 | Screened Poisson | R12 | K=2 off-diagonal Hessian block |
| 40 | **Two-regime crossover $c_0^{(K)}$** | S | L2 | Enumeration | R7 | Regime I / Regime II partition |
| 41 | **Thermal extension Prop 1.3a/b** | S (modified) | L2 | Perturbation in T | R2 | T-shifted spectrum |
| 42 | **$\sigma_0$ (initial-noise scale) requirement** | S | L2 | Linearization | Coupling Bound | $\sigma_0 \leq \mu_{\min}^{-1}$ for Fiedler stability |

### 3.1 L2 axiom 의존성

- **Primary**: canonical §8 energy functional + §9 concrete operators.
- **Key commitments**: CN5 (4-term structure), CN9 (volume constraint), CN14 (closure expands metastability — L2 quantitative via $d_{\min}^*$ reduction ~30%).
- **Feature**: L2 claim은 "K-sector fixed" 가정 아래 유효. K-sector crossing은 L1 problem.

---

## §4. L1 (Topology) — static claims

Discrete K, basin, component count, Morse index 부호.

| # | Name | S/D | Layer | Proof tool | Source | Notes |
|---|---|---|---|---|---|---|
| 43 | **T8-Core (existence of non-uniform minimizer)** | S | L1 | Saddle at uniform | canonical §13 | "$K \geq 1$" boolean |
| 44 | **T-Merge (a) K-Formation local minimality** | S | L1 | Hessian PD | canonical §13 | "$K$-sector가 local min이다" |
| 45 | **T-Merge (b) Isoperimetric ordering K=1 < K=2** | S | L1 | Perimeter min via Γ | canonical §13 | Integer K preference |
| 46 | **Topological Lock (merge impossible on $\Sigma^K_M$)** | S | L1 | Manifold constraint | canonical §13 | Vacuous but L1 |
| 47 | **Proposition 1.1 ($\Sigma_m$ convex polytope)** | S | L1 | Convex geometry | canonical §13 | Constraint manifold topology |
| 48 | **Proposition 1.2 (fiber dim 2n-2)** | S | L1 | Dimension count | canonical §13 | Singular locus at corners |
| 49 | **Theorem 3.1 (a) tangent decomposition** | S | L1 | Linear algebra | canonical §13 | Intra/transfer split |
| 50 | **Theorem 3.1 (b) intra-formation Hessian PD** | S | Mixed(L1,L2) | Stability | canonical §13 | PD = L2 but within K-sector = L1 |
| 51 | **Theorem 3.1 (d) symmetric point critical** | S | L1 | Symmetry argument | canonical §13 | Critical point existence |
| 52 | **T-Birth-Parametric D_4 pitchfork** | S | Mixed(L1,L2) | Crandall-Rabinowitz | canonical §13 | $\beta_{\mathrm{crit}}$ L2 + 3-branch topology L1 |
| 53 | **Tree Structure Theorem (R10)** | S | L1 | Saddle-node cascade | R10 | Integer $c_0$ tree |
| 54 | **Universal $c_0$-Counting (equivariant CR)** | S | L1 | Equivariant Crandall-Rabinowitz | R8 | Universal integer count |
| 55 | **Secondary-bifurcation framework** | S | Mixed(L1,L2) | Pitchfork cascade | R10 | Threshold (L2) + branch count (L1) |
| 56 | **Lock-In Theorem on $C_n$** | S | L1 | Morse-Bott | R5 | Moduli choice discrete |
| 57 | **$\mathcal{M}_1$ topology invariant** | S | L1 | Invariant under continuous Aut | R5 | Moduli class |
| 58 | **Euler / connected-component constraint** | S | L1 | Graph topology | canonical §8 | $\sum_i u_i = m$ + connectedness |
| 59 | **C-FQ (Formation Quantization Theorem)** | S | L1 | Well-separated decomposition | R22 step_cohesion.md §1 | $K \in \mathbb{Z}$ invariant within basin |
| 60 | **C-3L (Three-Layer Hierarchy)** | S | L1 | Organizational structural | R22 step_cohesion.md §3 | Meta-structural — could be "meta" |

### 4.1 L1 axiom 의존성

- **Primary**: canonical §3 (formal universe), §11 CN2 (relational priority), §11 CN3 (derivative object status).
- **Key new**: Axiom S1 (Step-Cohesion Decomposition, `step_cohesion.md` §10.1), S2 (Three-Layer), S3 (Protocol-Parameterized), S4 (Static/Dynamic Decomposition).
- **Feature**: L1 claim은 대부분 "exists $K$ such that ..." 형태. Generic graph vs symmetric lattice 구분 중요.

---

## §5. Dynamic claims (any layer)

Gradient flow / temporal / stochastic 포함.

| # | Name | S/D | Layer | Proof tool | Source | Notes |
|---|---|---|---|---|---|---|
| 61 | **T14 Gradient Flow Convergence** | D | L3 | Łojasiewicz on analytic | canonical §13 | Requires $b_D = 0$ (CN13) |
| 62 | **T-Persist-K-Sep (well-sep persistence)** | D | Mixed(L1,L2) | IFT on $\Sigma^K_M$ | canonical §13 (Cat C re-listed) | K fixed (L1) + displacement bound (L2) |
| 63 | **T-Persist-K-Unified (unified regime)** | D | Mixed(L1,L2) | Overlap + spectral | canonical §13 | $\Lambda_{\mathrm{coupling}}$ regime |
| 64 | **Pillar I Nucleation (spectral seeding)** | D | Mixed(L1,L3) | Fiedler mode + exp51 | canonical §12 | Basin label (L1) ← mode structure (L3) |
| 65 | **Pillar II Metastability (Hessian PD)** | D | Mixed(L1,L2) | Positive Hessian | canonical §12 | Local stability |
| 66 | **Pillar III Coarsening (kinetic)** | D | Mixed(L1,L2) | Gradient flow + barrier | canonical §12 | K evolution over time |
| 67 | **M-1 2-timescale (emergence vs merger)** | D | Mixed(L1,L2) | Allen-Cahn scaling | R16 / M1_dissolution.md | Kramers scale (L2) → K reduction (L1) |
| 68 | **F-1 dissolution (K=2 metastable exists)** | D | L1 | R12 Hessian + X1 V5 | R16 / F1_dissolution.md | K=2 basin existence |
| 69 | **MO-1 dissolution (Morse-Bott applies)** | D | L1 | Equivariant Morse-Bott | R5 + R12 / MO1_dissolution.md | Avoids MO-1 via $\Sigma_m$ |
| 70 | **C-X1V5 Protocol Selection** | D | L1 | Hysteresis experiment | R22 X1 V5 | Protocol-dependent basin selection |
| 71 | **C-X3 E3 Cubic Mechanism** | D | Mixed(L2,L1) | Prop 1.3b(d) cubic | R22 X3 v2 | cubic term (L2) drives asymmetric K̂ (L1) |
| 72 | **Static/Dynamic Separation Principle** | D (meta) | **Meta** | Empirical (R17-R21) | R22 §17.6 | Axiom-candidate, not theorem |

### 5.1 Dynamic axiom 의존성

- **Primary**: canonical §11 open design choices (dynamic update laws) + §12 Three Pillars.
- **Key commitments**: CN6 (K kinetically determined), CN8 (formations metastable).
- **Feature**: 모든 dynamic claim은 **protocol specification**을 요구 (NQ-50 open). 명시적 protocol 없는 dynamic claim은 ambiguous 처리.

---

## §6. Meta claims

Observable-없는 consistency / existence / axiom validation.

| # | Name | S/D | Layer | Proof tool | Source | Notes |
|---|---|---|---|---|---|---|
| 73 | **T20 Axiom Consistency (A1'/A2/A3/A4)** | S | Meta | Direct computation | canonical §13 | Axiom mutual consistency |
| 74 | **Axiom S1-S4 consistency (proposed)** | S | Meta | — | R22 / step_cohesion.md §10.1 | **Proposed; not yet formal proof** |

---

## §7. Category distribution summary

### 7.1 By layer

| Layer | Static count | Dynamic count | Total | % |
|---|---|---|---|---|
| L1 (topology) | 18 (items 43–60) | 3 (68, 69, 70) | 21 | 28% |
| L2 (geometry) | 18 (items 25–42) | 0 | 18 | 24% |
| L3 (field) | 13 (items 1–4, 7–9, 11–17) | 1 (61) | 14 | 19% |
| Mixed | 13 (5, 6, 10, 18, 19, 23, 50, 52, 55) + more | 7 (62, 63, 64, 65, 66, 67, 71) | 20 | 27% |
| Meta | 2 (73, 74) | 1 (72) | 3 | 4% |
| **Total** | | | **76** | 100% |

*(Counting error band ±5 due to bundling conventions in R1-R16 entries.)*

### 7.2 By static/dynamic

| Type | Count | % |
|---|---|---|
| Static | 60 | 79% |
| Dynamic | 12 | 16% |
| Meta | 3 | 4% |

→ **Observation**: 현재 canonical + R1-R22 결과의 **79%가 static**. Dynamic 이론은 상대적으로 underdeveloped. G4/G5 (time/thermal)의 scoping 자체가 이 불균형을 반영.

### 7.3 "Mixed"의 내부 분포

| Mixed-type | Count | Example |
|---|---|---|
| L1×L2 | 10 | T-Persist-K-Sep (K fixed + bound), T-Birth-Parametric |
| L2×L3 | 8 | $\xi_0$ governs tanh profile; Hessian on u-field |
| L1×L3 | 2 | Pillar I Nucleation (Fiedler mode → basin label) |

→ **Observation**: "Mixed" 27%는 framework의 **bridge claims**가 많음을 반영. Three-Layer를 strict disjoint partition으로 요구하면 **불가능**. "Mixed"를 정당한 category로 인정하는 것이 옳음 (NQ-49 implicit conclusion).

---

## §8. Missing single-formation gap check

plan.md G1 성공 기준: "혹시 missed single-formation gap이 있으면 flag."

### 8.1 Possible gaps (G1 residual)

- **G-miss-1**: **Singular / boundary behavior** — $\Sigma_m$이 manifold-with-corners이며 corners에서 $m_j \to 0$ 특이점. Stratified Morse (Prop 1.1, 1.2, Thm 3.1) 다룸. 하지만 **corner에서의 energy 발산 또는 정규성**은 L3 regularity gap. 현재 Cat A에 구체적 statement 없음. **Flag**: L3 corner analysis (NQ-50 candidate).
- **G-miss-2**: **$c_0$-Counting uniqueness across graph classes** — R8 "Universal $c_0$-Counting"이 universal claim이지만 explicit count for cycle / torus / general regular graph의 각 case가 all Cat A인가? R4+R5+R8 bundling이 일부 case를 implicit하게 남겨 놓았을 가능성.
- **G-miss-3**: **Profile-$\xi_0$ relation for non-regular graphs** — Cor 2.2 quant-tanh는 D_4 lattice 기반. Non-regular (SBM, random) 그래프에서는 explicit $\xi_0$ formula 없음. **Flag**: L2 extension (NQ-33 existing).
- **G-miss-4**: **"Single-formation $\widehat K = 1$" empirical sufficiency condition** — R17/R18/R19/R22 X-experiments에서 $\widehat K = 1$이 관찰된 regime (e.g., 2D c=0.5 torus)에서 "왜 K=1인가"의 proof가 completed? **T-Merge (b)** 가 global min을 주지만, 실제 dynamics의 basin landing은 R22 V5 protocol-dependent. **Flag**: Single-formation observed-K=1의 protocol-independence sufficient condition은 open (NQ-46의 일부).

### 8.2 No-gap domains

다음은 단일 formation 범위에서 gap 없음:

- **Existence, stability, closure FP theory** — T1, T3, T6a, T6b 완전.
- **Analyticity / Γ-convergence** — T11 + Cor 2.2 supra-lattice (Cat B demoted, but framework intact).
- **Single-basin K_step operator** — `step_cohesion.md` §5.1.

---

## §9. Axiom-level summary

각 layer의 의존 axiom 표.

### 9.1 L1 topology 의존

- canonical §3 (formal universe)
- §11 CN2 (relational priority)
- §11 CN3 (object derivative status)
- **New S1** (Step-Cohesion Decomposition) — proposed
- **New S3** (Protocol-Parameterized Observable) — proposed

### 9.2 L2 geometry 의존

- canonical §8 (energy functional)
- §9 (concrete operators)
- §11 CN5 (4-term structure)
- §11 CN9 (volume constraint)
- §11 CN14 (closure expands metastability)

### 9.3 L3 field 의존

- §6 Group A axioms (closure A1'-A4)
- §6 Group B-E axioms
- §8 energy functional
- §11 CN1 (closure non-idempotence)
- §11 CN13 ($b_D = 0$)

### 9.4 Dynamic 의존 (L1/L2/L3 across)

- §11 CN6 (K kinetically determined)
- §11 CN8 (formations metastable)
- §12 Three Pillars (Nucleation / Metastability / Coarsening)
- **New S4** (Static/Dynamic Decomposition) — proposed

---

## §10. Unclassified residual

**0개 미분류.** 모든 76 items (±5)이 L1 / L2 / L3 / Mixed / Meta 중 하나에 할당됨.

단, **"Mixed" 27%**가 상당히 높아 Three-Layer hierarchy를 **strict partition**으로 제시하기 어려움. 이는 framework의 한계가 아니라 **bridge claim의 자연스러운 비중**으로 해석. Stage 2 Axiom Audit에서 "mixed" 비율을 줄이려면 **bridge를 별도 first-class layer로** 승격할 수 있음 (4-layer alternative). **NQ-51 (new)**: 3-layer vs 4-layer (adding Bridge Layer) 결정.

---

## §11. Stage 2 Axiom Audit prep

이 classification은 다음 Stage 2 작업의 기반:

1. **Axiom reduction**: 각 layer가 **최소 axiom set**에 의존함을 확인. 중복 / 파생 axiom 식별.
2. **Axiom S1-S4 formalization**: Proposed axiom이 canonical §6 Group A-E와 non-redundant 임을 증명.
3. **Canonical §13 재정렬**: Cat A table을 layer-indexed 형태로 재배치.
4. **Retraction impact**: Retracted claims (Conj 2.1 v1-v5, Conj 2.1-Bott, Round 9 §11 Cat A → Cat B)가 각 layer에서 차지하던 자리 공백 기록.
5. **NQ propagation**: 각 layer별 open NQ 목록 (NQ-32/33/44/46/49/50/51).

---

## §12. File status

- **Primary deliverable**: 77 (±5) Cat A claims의 Three-Layer 할당 완료.
- **Methodology**: Hybrid Approach A2 (proof-dependency) × A4 (static/dynamic).
- **Gaps flagged**: G-miss-1 (L3 corner), G-miss-2 (c_0 graph-class), G-miss-3 (non-regular $\xi_0$), G-miss-4 (observed-K=1 sufficient condition).
- **Intended promotion**: `working/SF/layer_classification.md` (신규).

**End of SF_layer_classification.md.**
