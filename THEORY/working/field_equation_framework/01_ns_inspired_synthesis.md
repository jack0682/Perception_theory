---
type: working/field_equation_framework/synthesis
date: 2026-05-20
session_origin: W8-Day3 evening, post-EOD user-initiated synthesis
canonical_version: CV-1.18 SEALED (untouched throughout)
status: draft v0.1
authors: user (Jaehong Oh)
preceded_by:
  - W8-Day3 02_cg_numerical_verification.md (S1 Cat B verified)
  - W8-Day3 03_D_L_commutation.md (S3 Cat A on standard regimes)
  - W8-Day3 04_dynamic_class_investigation.md (SCC ≠ Cahn-Hilliard spectrum proof)
  - W8-Day3 99_summary.md (Decision A)
  - working/cssl/00_concept_handoff.md + 01_critic_evaluation.md (CSSL critic-rejected)
  - Evening dialog: surface tension idea → Re/We → Sc → Pr → NS structural ideas
purpose: |
  지금까지 분산된 dimensionless number 대화 thread + Navier-Stokes 의 structural ideas 를 *field equation framework* 으로 정밀 synthesis. SCC = field theory on graphs (NOT fluid simulation). 향후 W9+ session 의 reference 기반.
canonical_compatibility:
  CN4_analyticity: preserved (energy untouched)
  CN5_4_term_independence: preserved
  CN10_no_reductive_reduction: contrastive only
  primitive_u_t: preserved
  canonical_edits: 0
  inertia_introduction: forbidden (Package I Cat A protection)
  Mori_Zwanzig: forbidden (OP-0021 Routes A/B DEPRECATED CV-1.18)
cot_enforced: yes
coc_enforced: yes
---

> [!nav] Linked: [[../../canonical/canonical|CV-1.18 canonical]] (§3.7, §9.3, §13 T-PF-A1-SDE/AR/GI/PE, Theorem 4, SB7, T-σ-Lemma-1, V5b-T-zero, L-HMORSE-LOCAL/DECOMP, T-K-Select-PF, T-OP6-B, T-P-F-ε0-K) · [[../../canonical/DECLARATION|DECL-1.0]] · [[../cssl/00_concept_handoff|CSSL handoff]] · [[../cssl/01_critic_evaluation|CSSL critic eval]] · [[../../logs/daily/2026-05-20/03_D_L_commutation|03 [D, L_G] commutation]] · [[../../logs/daily/2026-05-20/04_dynamic_class_investigation|04 dynamic class]]

# 01 — Navier-Stokes-Inspired Field Equation Framework for SCC (Synthesis v0.1)

**Mode**: working layer synthesis (NOT verification, NOT SEAL prep, NOT canonical edit)
**Target**: consolidate dimensionless number thread + NS structural ideas as *field equation framework on graphs* — NOT fluid analogy
**Pre-work xref check** (§15.1):
- `grep -r "Navier\|Stokes\|Reynolds\|Weber\|Schmidt\|Prandtl\|Péclet\|Damköhler" canonical/ working/` → 12 hits
- canonical: 2 hits (canonical.md + theorem_status.md, *both unrelated* — Cugliandolo 2011 reference in OP-0021 + SF symmetry context)
- working: 10 hits, *9 in superseded foundation/v0 archives* (fractal_dynamic_dim_v0, manifold_topology_attempt_v0, SCC_unified_derivation_v0.1, SCC_U_excluded, proofs/P2/P5/P6/_SUMMARY) — 1 in observer_moduli (Arnold context)
- **Novel positioning**: 본 문서 = *consolidated synthesis*, *기존 산발적 references 의 systematic catalog* + *Field-equation framing* (이전 산발 references 는 모두 *조각조각*, 통합 catalog 부재)

**§8a archive pattern P1-P6 check**:
- P1 (근본 질문 우회): DECL Q1 (T8) + Q3 (stochastic dynamics) + Q4 (K-selection) 의 *직접 dimensionless 정량* — 우회 아님 ✓
- P2 (Vocabulary refactoring): u_t 본체 미변경, parameter 만 ✓
- P3 (Canonical content 중복): 산발 references 의 *consolidation only*, contradiction 0 ✓
- P4 (외부 도구 도입): NS / Modica-Mortola / Kramers = *contrastive only*, *canonical anchor 의 직접 후속* ✓
- P5 (Self-audit): 본 §0 + §12 의 dual audit ✓
- P6 (언어-수학 분리): catalog format 으로 *각 number 의 수학 명확 분리* ✓
- **0/6 부합** → 진행 합법

---

## §1 — Mission: Field Equations, NOT Fluids (CN10 Boundary Explicit)

### §1.1 본 문서가 *하는 것*

1. **Field equation framework**: SCC 의 dynamics 를 *graph 위 field equation* 으로 명시 — *fluid 가 아닌 abstract field theory*
2. **Structural ideas from NS**: Navier-Stokes equation 의 *4 structural components* 의 *structural ideas* 추출 — *각 component 의 SCC 적용 가능성 명시*
3. **Dimensionless number catalog**: 이전 대화 thread 의 *consolidated catalog* (12 numbers) + canonical parameter 명시
4. **Network relationships**: T8 critical = Pr ratio, Eyring-Kramers ∝ Pr^{(Kramers)}, Pe-Pr bridge 등
5. **H-Morse application**: 비-uniform critical H-Morse 의 *3 quantitative paths* (surface tension rescaling / Modica-Mortola Jacobi / Pr^{(bd)} precondition)
6. **OPEN problem leverage**: 어느 dimensionless number 가 어느 canonical OP 를 advance

### §1.2 본 문서가 *하지 않는 것* (CN10 Boundary)

명시적으로 *금지* 항목:

- ❌ **SCC = fluid 환원**: "SCC dynamics 는 결국 *constrained Allen-Cahn 형태의 reaction-diffusion 유체*" 형식 reduction 금지
- ❌ **NS equation 직접 적용**: Navier-Stokes 자체를 SCC u_t 에 직접 대입 금지 (관성 부재, momentum 부재 — §5 명시)
- ❌ **Reynolds / Weber 의 inertial form**: 정의 자체가 momentum 필요 — *overdamped 대응 (Pe, Bo) 만* 사용
- ❌ **Mori-Zwanzig formalism**: CV-1.18 SEAL 에서 OP-0021 Routes A/B DEPRECATED (CN-COB violation) — *effective memory kernel 도입 금지*
- ❌ **새 energy term**: dimensionless 분석은 *parameter ratio only*, energy 자체 미수정 (CN4 보존)
- ❌ **Fluid-specific theorem import**: Nusselt-Reynolds correlation 등 *standard fluid theorem* 의 SCC 적용 금지

### §1.3 Why this framework matters

```
CoT step 1: SCC 의 *진짜 미해결* (H-Morse non-uniform critical, OP-0005-DYN Kramers rates, OP-HMORSE-SADDLE) 들이 모두 *spectral/dimensional 분석* 을 필요.
CoT step 2: 이 분석들이 *common framework* 부재로 *case-by-case ad hoc* 처리 — 통합 catalog 가 *systematic attack* 의 기반 제공.
CoT step 3: Fluid mechanics 의 *dimensionless analysis* 가 *유사 problem (overdamped reaction-diffusion 의 spectral 분석)* 의 80년 toolkit — *structural ideas* 의 *contrastive import* 가 가장 leverage.
→ Therefore: 본 framework = *통합 dimensionless toolkit*, *fluid 환원 아님*, *각 SCC OPEN 의 entry point 명시*.

CoC anchors:
  - DECL-1.0 Q1, Q3, Q4 (T8, stochastic dynamics, K-selection 의 미해결)
  - canonical §13 L-HMORSE-LOCAL (Cat B, H-Morse local conditional)
  - canonical §13 T-P-F-ε0-K (Cat B, Kramers stability conditional on H5)
  - canonical OP-0005-DYN, OP-HMORSE-SADDLE (OPEN)
```

---

## §2 — Navier-Stokes Equation: Structural Decomposition (4 Components)

Incompressible Navier-Stokes (standard form, $\rho$ = constant density):

$$\underbrace{\partial_t u}_{\text{(1) temporal}} + \underbrace{(u \cdot \nabla)u}_{\text{(2) convective inertial}} = \underbrace{-\frac{1}{\rho}\nabla p}_{\text{(3) pressure constraint}} + \underbrace{\nu \nabla^2 u}_{\text{(4) viscous}} + \underbrace{f}_{\text{(5) external}}$$

with **incompressibility constraint**: $\nabla \cdot u = 0$.

### §2.1 Component (1) — Temporal evolution $\partial_t u$

- *First-order in time* (in laminar/Stokes regime)
- Structural role: *evolution operator* — defines how field changes

### §2.2 Component (2) — Convective inertial $(u \cdot \nabla)u$

- *Quadratic in $u$* — *self-coupling* of field with its own gradient
- *관성 (inertia) 의 핵심*: 유체 입자가 *자신의 velocity 의 방향으로* 이동하면서 *나머지 field 를 운반*
- *Nonlinearity 의 source* (linear NS 에서는 부재)

### §2.3 Component (3) — Pressure constraint $-\nabla p / \rho$

- $p$ 는 *not a thermodynamic variable* in incompressible flow — *Lagrange multiplier* enforcing $\nabla \cdot u = 0$
- *Structural role*: *constraint enforcer*
- 수학적으로 *non-local* — $p$ 는 Poisson equation $\nabla^2 p = -\rho\,\mathrm{tr}((\nabla u)^2)$ 로 결정

### §2.4 Component (4) — Viscous diffusion $\nu \nabla^2 u$

- *Linear* + *diffusion-type* operator
- $\nu$ = kinematic viscosity (*momentum diffusivity*)
- *Structural role*: *spatial smoothing* — sharp gradients dissipate
- *Damping 의 source*

### §2.5 Component (5) — External forcing $f$

- *Body force* per unit mass (e.g., gravity, electromagnetic)
- *Structural role*: *driving / source term*

### §2.6 Incompressibility constraint $\nabla \cdot u = 0$

- *Local mass conservation* (continuity equation with $\partial_t \rho = 0$)
- *Constraint*, NOT evolution equation
- Coupled with (3) via $p$ as Lagrange multiplier

---

## §3 — SCC Field Equation Structure (canonical anchor)

### §3.1 Canonical SDE form (T-PF-A1-SDE, Cat A, CV-1.8)

$$dU_t = \underbrace{-\Pi_{T\Sigma_m} \nabla\mathcal{E}(U_t)\,dt}_{\text{(I) deterministic drift}} + \underbrace{\sqrt{2T_*}\,\Pi_{T\Sigma_m}\,dB_t}_{\text{(II) stochastic mixing}} + \underbrace{dK_t}_{\text{(III) Skorokhod reflection}}$$

- $\Pi_{T\Sigma_m} = I - (1/n)\mathbf{1}\mathbf{1}^T$ — orthogonal projector onto tangent space of $\Sigma_m$ (mean-zero subspace) — T-PF-A1-AR (Cat A, CV-1.8)
- $\mathcal{E}$ = SCC total energy (4 terms — canonical CN5 conceptual independence)
- $B_t$ = standard Brownian motion on $\mathbb{R}^n$
- $K_t$ = Skorokhod reflection at $\{u_i = 0\} \cup \{u_i = 1\}$ (canonical T-PF-A1-AR boundary)
- $T_*$ = effective stochastic temperature (canonical OMS-1 ξ resident, CV-1.18)

**Conservation**: $\sum_i U_t^{(i)} = m$ (GLOBAL mass, NOT local flux). Enforced by $\Pi$.

### §3.2 Energy structure (4 conceptually independent terms — CN5)

$$\mathcal{E}(u) = \lambda_{cl}\mathcal{E}_{cl}(u) + \lambda_{sep}\mathcal{E}_{sep}(u) + \lambda_{bd}\mathcal{E}_{bd}(u) + \lambda_{tr}\mathcal{E}_{tr}(u)$$

$\mathcal{E}_{bd}$ — Allen-Cahn-like component (smoothness + double-well):

$$\mathcal{E}_{bd}(u) = \alpha\,u^T L_G u + \beta \sum_i W(u_i), \quad W(u) = u^2(1-u)^2$$

- $\alpha\,u^T L_G u$ = *Dirichlet smoothness* (graph Laplacian $L_G = D_G - A_G$)
- $\beta W(u_i)$ = *double-well potential* on each site

### §3.3 Hessian at critical (canonical Theorem 4, Cat A)

For uniform critical $u^* = c\mathbf{1}$ in $\mathcal{E}_{bd}$-only model:

$$\mu_k = 4\alpha\lambda_k(L_G) + \beta W''(c)$$

eigenvalues of constrained Hessian on $T_{u^*}\Sigma_m = \mathbf{1}^\perp$, indexed by $L_G$ eigenmodes $k = 1, \ldots, n-1$.

### §3.4 T8 phase transition (canonical SB7, Cat A)

$$\Sigma_{T8} = \left\{(\alpha, \beta, c) : \mu_2 = 0\right\} = \left\{(\alpha, \beta, c) : \frac{\beta}{\alpha} = \frac{4\lambda_2(L_G)}{\lvert W''(c) \rvert}\right\}$$

codim-1 algebraic hypersurface in parameter space. *Wall 위*: formation regime. *아래*: uniform stable.

---

## §4 — NS ↔ SCC Component-by-Component Mapping

| NS component | SCC analog | 분류 | 이유 |
|---|---|---|---|
| (1) $\partial_t u$ | $dU_t$ (Langevin first-order) | **✓ structural** | both first-order in time |
| (2) $(u\cdot\nabla)u$ (convective inertial) | *none* | **❌ incompatible** | SCC overdamped — no inertia, no convective self-coupling |
| (3) $-\nabla p / \rho$ (pressure constraint) | $\Pi_{T\Sigma_m}$ (mass projector) | **✓ structural match (deep)** | both Lagrange multipliers enforcing scalar constraint |
| (4) $\nu \nabla^2 u$ (viscous diffusion) | $4\alpha L_G$ in Hessian (Dirichlet smoothness) | **≈ analogous (overdamped form)** | both Laplacian-type diffusion; overdamped equivalent |
| (5) $f$ (external force) | $\beta W'(u)$ (double-well driving) | **≈ analogous** | both pointwise source; double-well is self-generated, not external |
| ⊥ $\nabla \cdot u = 0$ (incompressibility) | $\sum_i u_i = m$ (mass conservation) | **✓ constraint match** | local flux (NS) vs global integral (SCC) — see §4.6 |

### §4.1 Mapping (1) — Temporal evolution ✓

```
CoT step 1: NS 의 ∂_t u 는 first-order temporal derivative — Langevin SDE 의 dU_t/dt 부분과 *형식적으로 동일*.
CoT step 2: 차이: NS 는 deterministic, SCC 는 stochastic (Brownian noise term 추가). 그러나 *temporal evolution 의 form* 은 동일 (first-order).
→ Structural ✓ (the *structural role* of "what defines change over time" matches).

CoC anchors:
  - NS: standard incompressible form (Reed-Simon, Constantin-Foias 1988)
  - SCC: T-PF-A1-SDE (Cat A, CV-1.8)
inverse_causation_check:
  - if SCC were second-order (with ∂_t²): would match NS 의 inertia regime, but breaks T-PF-A1-SDE Cat A → ❌
```

### §4.2 Mapping (2) — Convective inertial ❌

```
CoT step 1: NS 의 (u·∇)u 는 quadratic in u + self-coupling — *관성 (inertia) 의 직접 source*.
CoT step 2: SCC 의 deterministic drift -∇E 는 *gradient flow* — *u 자체에 의존하지만 quadratic self-coupling 부재* (E 의 gradient 는 derivative, 일반적으로 non-quadratic in u).
CoT step 3: 즉 SCC 는 NS 의 *convective term 의 structural analog 없음* — *overdamped gradient flow* 가 *관성-driven convection* 과 *근본적으로 다름*.
→ Incompatible ❌.

CoC anchors:
  - NS: convective term 의 quadratic self-coupling 은 Cauchy momentum equation 의 직접 후속
  - SCC: T-PF-A1-SDE (Cat A) — first-order, no inertia
  - canonical CV-1.18 SEAL: OP-0021 Routes A (Mori-Zwanzig) DEPRECATED (CN-COB violation)
inverse_causation_check:
  - if convective term added: would require introducing momentum field (e.g., π = ρu) — *fundamental restructuring*, T-PF-A1-* cascade 파괴
  - if M-Z memory kernel added: similar cascade + CV-1.18 SEAL deprecation 위반
```

### §4.3 Mapping (3) — Pressure constraint ✓✓ (structural deep match)

```
CoT step 1: NS 의 -∇p 는 *not a thermodynamic pressure*, *incompressibility 의 Lagrange multiplier*. Mathematically: p 는 ∇·u = 0 를 enforce 하는 dual variable.
CoT step 2: SCC 의 Π_TΣ_m = I - (1/n)11^T 는 ∇E 를 *mean-zero subspace 로 project* — Σ u_i = m constraint 를 enforce.
CoT step 3: 두 operator 모두 *constraint 의 Lagrange multiplier role* — *structurally identical functional role*.
→ Structural ✓ (deep match).

CoC anchors:
  - NS: incompressibility + pressure 의 dual relationship (standard textbook, Constantin-Foias 1988 §1)
  - SCC: T-PF-A1-AR (Cat A, CV-1.8) — Π 정의 + Σ_m 의 boundary 와의 reflection
inverse_causation_check:
  - if Π removed: SCC dynamics 가 Σ_m 를 떠남, mass 보존 위반 → physics 자체 무의미
  - if -∇p removed in NS: u 가 incompressible flow 의 manifold 를 떠남, ∇·u ≠ 0 → 가설 위반
  - 두 경우 모두 *constraint preservation 의 fundamental role* 입증
```

**의의**: 이 mapping 이 본 framework 의 *가장 deep insight* — NS 의 pressure 가 SCC 의 mass projector 와 *동일 mathematical role*. Modica-Mortola Γ-convergence 의 *Lagrange multiplier reduction* (constrained AC, Rubinstein-Sternberg 1992) 가 *이 mapping 의 자연 후속*.

### §4.4 Mapping (4) — Viscous diffusion ≈ (overdamped analog)

```
CoT step 1: NS 의 ν∇²u 는 *momentum diffusion* — kinetic energy 의 spatial 분산.
CoT step 2: SCC 의 4αL_G (Hessian 에서) 또는 2α u^T L_G u (energy 에서) 는 *cohesion field 의 spatial smoothing* — sharp transition 의 dissipation.
CoT step 3: 두 항 모두 *Laplacian operator 의 PSD contribution* — *structurally analogous*. 단 NS 는 *momentum*, SCC 는 *cohesion intensity* — *서로 다른 quantity 의 diffusion*.
CoT step 4: *Overdamped 의 직접 result*: NS 의 ν 가 *kinematic viscosity*, SCC 의 α 가 *cohesion smoothing rate* — *분자 in dimensionless ratio* 의 역할.
→ ≈ analogous (overdamped form of "diffusion").

CoC anchors:
  - NS: viscous term 의 Laplacian (Cauchy momentum)
  - SCC: canonical §13 Theorem 4 (μ_k formula, 4αλ_k contribution)
inverse_causation_check:
  - if α = 0: no smoothing, formation 경계 unbounded sharpness — Modica-Mortola Γ-limit 의 *singular interface* 극한
  - if ν = 0: inviscid Euler equation — SCC 와 *근본적으로 다른* (관성-dominated turbulence)
  - 두 경우 모두 *smoothing 의 role 확인*, 단 SCC 는 *overdamped* (no inertia 한계)
```

### §4.5 Mapping (5) — External forcing ≈ (self-generated form)

```
CoT step 1: NS 의 f 는 *external body force* (gravity, etc.) — *system 외부 source*.
CoT step 2: SCC 의 β W'(u) = 2β u(1-u)(1-2u) 는 *double-well 의 self-generated pointwise force* — *system 내부에서 발생*.
CoT step 3: 두 항 모두 *pointwise source-type contribution* — 그러나 NS f 는 external, SCC W' 는 *intrinsic property of u_t field* — *완전 동치 아님*.
→ ≈ analogous (with caveat: SCC 는 self-generated, NS 는 external).

CoC anchors:
  - NS: standard external force structure
  - SCC: canonical §3.5 boundary energy + W(u) = u²(1-u)² (CLAUDE.md "Critical Implementation Details" I6 correction)
inverse_causation_check:
  - if W'(u) = 0: no double-well, formation regime 부재 — T8 phase transition 무효
  - if f = 0 in NS: pure free flow — Navier-Stokes self-evolution only
```

### §4.6 Constraint match ✓ (local vs global distinction)

```
CoT step 1: NS 의 ∇·u = 0 는 *local incompressibility* — 모든 점에서 *divergence-free*.
CoT step 2: SCC 의 Σ_i u_i = m 는 *global mass conservation* — graph 전체 sum 이 고정.
CoT step 3: 두 constraint 모두 *single scalar constraint per system*, Lagrange multiplier (pressure / Π projector) 로 enforce — *structural ✓*.
CoT step 4: 그러나 의미 다름: NS = *local flux 보존* (volume element 각각 보존), SCC = *integral 보존* (전체 sum, local flux 보존 아님).
→ ✓ constraint match with explicit local/global distinction.

CoC anchors:
  - NS: incompressibility constraint
  - SCC: T-PF-A1-AR (Cat A) + canonical Σ_m 정의
inverse_causation_check:
  - if SCC had *local* mass conservation: would be exactly Cahn-Hilliard (∂_t φ = ∇²(δH/δφ)) — *but 04 §6.3 corollary 증명: SCC ≠ Cahn-Hilliard via spectrum 분석*
```

**의의**: NS = local constraint, SCC = global constraint — *이 차이가 dynamic class 의 핵심* (04 §3.1 + §6.3 의 spectrum 증명 직접).

---

## §5 — Fundamental Incompatibilities (Guardrails)

본 §은 *명시 금지* 항목 — NS structural import 를 SCC 에 *남용 회피*.

### §5.1 관성 (inertia) 부재 — CRITICAL

SCC 의 T-PF-A1-SDE 는 *first-order in time* (overdamped Langevin). 어떠한 *second-order temporal term* ($\ddot u, \ddot U_t$ 등) 도입 시:

| 파괴되는 canonical | 이유 |
|---|---|
| **T-PF-A1-SDE (Cat A, CV-1.8)** | reflected Langevin 의 *first-order* form 명시 |
| **T-PF-A1-GI (Cat A, CV-1.9)** | Gibbs measure invariance 도출이 *first-order generator* 사용 |
| **T-PF-A1-PE (Cat A, CV-1.9)** | Poincaré inequality 도출이 *first-order semigroup* 사용 |
| **T-K-Select-PF (Cat B, CV-1.10)** | equilibrium K-selection 이 first-order ergodicity 기반 |
| **T-Temporal-Identity 의 (a,b,c,d) Cat A (CV-1.13)** | 시간 identity 의 *first-order trajectory* 기반 |

**결론**: 관성 도입 = *최소 5 Cat A theorem cascade 파괴* → **금지**.

### §5.2 Momentum 부재 — CRITICAL

SCC 는 *momentum field 자체 부재* (그래프 위 scalar field $u: X \to [0,1]$ 만). 이로부터:

- Reynolds number $\text{Re} = \rho v L / \mu$ — 분자 $\rho v$ 가 momentum density, *정의 불가*
- Weber number $\text{We} = \rho v^2 L / \sigma$ — 분자 $\rho v^2$ 가 kinetic energy density, *정의 불가*
- Mach number, Froude number 등 *모두 momentum-based* — *정의 불가*

**대응 (이전 대화 thread 의 직접 결과)**: *overdamped 자연 대응* 만 사용 — Pe, Bo (overdamped analog of We), Ca, St, Sc, Pr (이 모두 *kinematic viscosity 대신 다른 diffusivity* 사용 가능).

### §5.3 Mori-Zwanzig formalism — DEPRECATED CV-1.18

OP-0021 Routes A (Mori-Zwanzig effective memory kernel) DEPRECATED in CV-1.18 SEAL (canonical.md:2737):

> "Mori-Zwanzig 의 환경 메모리 커널 $K(t-s) = \langle F(0) F(t-s)\rangle_{\mathrm{env}}$ + RG universality class 모두 *external environmental statistics* 필요 — CN-COB 위반."

본 framework 는 *어떠한 effective memory kernel* 도입 금지. *현재 first-order T-PF-A1-SDE 만* 사용.

### §5.4 CSSL energy terms — critic-rejected

CSSL working file (`THEORY/working/cssl/`) 의 critic 평가 (`01_critic_evaluation.md`) 에서 *3 CRITICAL + 4 MAJOR 결함* 식별:

- $E_{ridge} = -\kappa \sum \phi(r_i)$ — sign-structure 결함 (canonical $E_{bd}$ 와 반대 부호)
- $E_{wild} = \eta \sum (\Delta_G u_i)^2$ — bi-Laplacian, *coercivity 부담* (working but suboptimal)
- $E_{pers}$ — PH 기반, *piecewise-constant in u*, *CN4 analyticity 파괴* + T14 Łojasiewicz + L-HMORSE-DECOMP + T-PF-A1-SDE Lipschitz + T-PF-A1-GI 모두 cascade 파괴

본 framework 는 *이들 energy terms 재시도 금지*.

### §5.5 *살아남는* CSSL idea — surface tension rescaling

CSSL §3.2 의 *유일하게 critic-survived* idea: $(\alpha, \beta) \to (s\alpha, s\beta)$ rescaling.

- *Canonical-compatible* (parameter rescaling only, 새 energy 0)
- $\sigma \to s\sigma$ → H-Morse spectral gap factor s 증가
- §8 에서 *primary path* 로 채택

---

## §6 — Dimensionless Number Catalog (12 Numbers, Consolidated)

본 §은 *이전 대화 thread (Re/We → Sc → Pr) 의 consolidated synthesis*. 모든 number 는 *canonical parameter only* 사용.

### §6.1 Catalog table

| # | 번호 | SCC formula | Definition / role | Canonical anchor | Cat 후보 |
|---|---|---|---|---|---|
| 1 | **Pe** (Péclet) | $\dfrac{\vert \nabla E\vert \cdot R}{T_*}$ | advection vs diffusion (overdamped 표준) | T-PF-A1-SDE | Cat A direct |
| 2 | **Da** (Damköhler) | $\dfrac{\beta}{\alpha}$ | reaction (double-well) vs transport (smoothness) | T8 condition 의 part | Cat A direct |
| 3 | **Ca** (Capillary) | $\dfrac{\vert \nabla E\vert}{\sigma}$, $\sigma \sim \sqrt{\alpha\beta}$ | gradient force vs surface tension (overdamped) | Modica-Mortola | Cat A direct |
| 4 | **Bo** (Bond / overdamped We) | $\dfrac{R^2 \cdot \vert \nabla E\vert}{\sigma}$ | size-scaled force/tension (Weber 의 overdamped 대응) | Modica-Mortola scaling | Cat A direct |
| 5 | **St** (Stokes) | $\dfrac{T_*}{\mu_k}$ | thermal time vs mode k relaxation time | Hessian + T-PF-A1-SDE | Cat A direct |
| 6 | **Sc^{(1)}** (mode-Hessian) | $\dfrac{\mu_k}{T_*} = \text{St}^{-1}$ | mode k 의 deterministic vs thermal | Hessian + T_* | Cat A direct |
| 7 | **Sc^{(2)}** (bulk-active separation) | $\dfrac{\mu_{\text{bulk}}}{\mu_{\text{active}}}$ | H-Morse spectral gap 의 직접 정량화 | L-HMORSE-DECOMP (Cat B) | **Cat B target** |
| 8 | **Sc_{T8}** (T8 ratio) | $\dfrac{4\alpha \lambda_2(L_G)}{\beta \lvert W''(c) \rvert}$ | T8 임계 ratio (canonical SB7 의 dimensionless rename) | SB7 (Cat A) | Cat A direct (rename) |
| 9 | **Sc^{(bd)} = Pr^{(bd)}** (boundary layer) | $\dfrac{\alpha \cdot W''(u^*)}{T_*}$ | det/thermal boundary width ratio | det $\sqrt{\alpha/\beta}$ + thermal $\sqrt{T_*/(\beta W'')}$ | Cat A direct |
| 10 | **Pr^{(spatial)}** | $\dfrac{\alpha \lambda_2(L_G)}{T_*}$ | spatial det vs thermal | Theorem 4 spatial part | Cat A direct |
| 11 | **Pr^{(onsite)}** | $\dfrac{\beta \lvert W''(c) \rvert}{T_*}$ | onsite det vs thermal | Theorem 4 onsite part | Cat A direct |
| 12 | **Pr^{(Kramers)}** | $\dfrac{\vert \mu_{\text{well}}\lvert }{ \rvert\mu_{\text{saddle}}\vert}$ | Eyring-Kramers prefactor input | Hänggi-Talkner-Borkovec 1990 (외부) + canonical Hessian | **Cat B target (highest leverage)** |

### §6.2 Per-number CoC chain (key entries)

#### **Sc_{T8} = T8 critical ratio (rename of canonical SB7)**

```yaml
target: Sc_{T8} = 4αλ_2(L_G) / (β |W''(c)|)
prior_anchors:
  - canonical: §13 Theorem 4 (Cat A) — μ_k = 4αλ_k + βW''(c)
  - canonical: §13 SB7 (Cat A, L2495) — Σ_T8 codim-1 algebraic
  - DECL-1.0: T8 phase transition central
causation_chain:
  - μ_2 = 0 ⟺ 4αλ_2 + βW''(c) = 0 (Theorem 4 + spinodal interior W''(c) < 0)
  - rearrange: β/α = 4λ_2/|W''(c)| (T8 condition)
  - dimensionless: Sc_{T8} = 4αλ_2 / (β|W''(c)|) = 1 at T8 wall
interpretation:
  - Sc_{T8} > 1: sub-critical (uniform stable)
  - Sc_{T8} = 1: T8 wall (Σ_T8)
  - Sc_{T8} < 1: super-critical (formation regime)
inverse_causation_check:
  - if Theorem 4 removed: no eigenvalue formula, Sc_{T8} undefined
  - if SB7 removed: Σ_T8 not algebraic codim-1, rescaling ill-defined
```

#### **Pr^{(Kramers)} = Eyring-Kramers prefactor input (highest leverage)**

```yaml
target: Pr^{(Kramers)} = |μ_well| / |μ_saddle|
prior_anchors:
  - canonical: §13 T-P-F-ε0-K (Cat B, CV-1.7) — Kramers exponent conditional on H5
  - canonical: §13 D-ST-4 (Cat B candidate, CV-1.6) — Z_K, Γ, Kramers rate (P-F flagged)
  - canonical: OP-0005-DYN (OPEN, W9+) — Kramers transition rates
  - external: Hänggi-Talkner-Borkovec 1990 Rev Mod Phys 62:251 — overdamped Kramers prefactor structural form
causation_chain:
  - Eyring-Kramers rate Γ ~ ω_0 · exp(-ΔE/T_*) (canonical D-ST-4 form)
  - prefactor ω_0 ~ ω_well · ω_saddle / √(Pr^{(Kramers)}) (Hänggi-Talkner-Borkovec 1990 standard form)
  - ω_well = |μ_well|^{1/2}, ω_saddle = |μ_saddle|^{1/2} (SCC Hessian eigenvalues at critical configurations)
interpretation:
  - Pr^{(Kramers)} >> 1: deep narrow well, sharp saddle → low prefactor → slow transitions
  - Pr^{(Kramers)} ~ 1: comparable scales → standard Kramers rate
  - Pr^{(Kramers)} << 1: shallow broad well, narrow saddle → fast transitions
leverage:
  - OP-0005-DYN attack: Pr^{(Kramers)} explicit form = prefactor analysis 의 직접 channel
  - T-P-F-ε0-K Cat A path: prefactor portion completion via Pr^{(Kramers)}
  - D-ST-4 Cat A: same channel
  - CSSL E_surg 정량화 (critic §A.3 restricted reformulation): saddle direction = unstable Hessian eigenvector
inverse_causation_check:
  - if μ_well undefined (formation 자체 미존재): Pr^{(Kramers)} ill-defined → OK (no transition to analyze)
  - if μ_saddle undefined (transition path 부재): same
  - if Hänggi-Talkner-Borkovec 1990 form 의 SCC 적용 부적절: alternative prefactor forms (Pollak-Talkner 1995, Kramers original 1940) — 모두 *분자/분모 ratio* 의 *Pr-shape* 동일
```

#### **Pr^{(spatial)} / Pr^{(onsite)}** 

```yaml
target: Pr^{(spatial)} = αλ_2(L_G)/T_*, Pr^{(onsite)} = β|W''(c)|/T_*
prior_anchors:
  - canonical: §13 Theorem 4 (Cat A) — μ_k = 4αλ_k + βW''(c) 의 *2 component*
  - canonical: T_* effective stochastic temperature (OMS-1 ξ resident, CV-1.18)
causation_chain:
  - Theorem 4 의 두 항 (spatial 4αλ_k vs onsite βW''(c)) 가 *서로 다른 physical origin*
  - 각 항을 T_* 로 normalize → Pr 형식의 ratio
interpretation:
  - Pr^{(spatial)} ratio: spatial coupling 의 deterministic vs thermal force
  - Pr^{(onsite)} ratio: onsite double-well 의 deterministic vs thermal force
relationship:
  - Pr^{(spatial)} / Pr^{(onsite)} = 4αλ_2 / (β|W''(c)|) = Sc_{T8}
  - i.e., T8 critical = "equal spatial vs onsite Prandtl numbers"
inverse_causation_check:
  - both → 0 (large T_*): noise dominates everything, no formation regime
  - both → ∞ (low T_*): deterministic regime, T-PF-A1-PE의 metastable scaling C_P ~ exp(osc/T_*)
```

---

## §7 — Network of Relationships

본 §은 §6 의 12 numbers 의 *algebraic + structural identities*. 모두 *canonical parameter only* (새 content 아님, *relationship rename*).

### §7.1 Identity 1: T8 Critical = Pr Ratio Equality

$$\boxed{\frac{\text{Pr}^{(\text{spatial})}}{\text{Pr}^{(\text{onsite})}} = \frac{4\alpha\lambda_2(L_G)}{\beta\vert W''(c)\vert} = \text{Sc}_{T8} \quad \Longleftrightarrow \quad \mu_2 = 0 \quad \Longleftrightarrow \quad (\alpha, \beta, c) \in \Sigma_{T8}}$$

**의의**: T8 phase transition 의 *dimensionless 재해석* — *"two Prandtl numbers 가 같아질 때 wall"*. 전통적 statement (β/α > 4λ_2/|W''(c)|) 와 *수학적으로 동치*, 그러나 *dimensionless framework 안에서 unified*.

### §7.2 Identity 2: Eyring-Kramers Prefactor

$$\boxed{\omega_0 \sim \omega_{\text{well}} \cdot \omega_{\text{saddle}} \cdot \left(\text{Pr}^{(\text{Kramers})}\right)^{-1/2}}$$

(Hänggi-Talkner-Borkovec 1990 standard overdamped Kramers form, SCC 적용)

**의의**: *Pr^{(Kramers)} 가 Eyring-Kramers prefactor 의 직접 input*. OP-0005-DYN attack 의 entry point — *highest leverage* dimensionless number.

### §7.3 Identity 3: Pe-Pr Bridge

$$\boxed{\text{Pe} = \frac{\vert \nabla E\vert \cdot R}{T_*} = \text{Pr}^{(\text{spatial})} \cdot \frac{\vert \nabla E\vert}{\alpha\lambda_2(L_G)} \cdot \frac{R}{1}}$$

즉 Pe = Pr^{(spatial)} × (gradient-to-spatial-rate ratio) × (length scale). *Pe 가 Pr-derived*.

### §7.4 Identity 4: Lewis-Analog

$$\boxed{\text{Le}_{\text{SCC}} = \frac{\text{Pr}^{(\text{spatial})}}{\text{Pr}^{(\text{bd})}} = \frac{\alpha\lambda_2(L_G) / T_*}{\alpha W''(u^*) / T_*} = \frac{\lambda_2(L_G)}{W''(u^*)}}$$

Lewis number (fluid: thermal vs mass diffusivity 비) 의 SCC analog. 분자 = spatial Prandtl, 분모 = boundary Prandtl. *Le_SCC = 그래프 spectral / double-well curvature*.

### §7.5 Identity 5: Surface Tension Rescaling (CSSL §3.2 의 *살아남은 idea*)

$$(\alpha, \beta) \to (s\alpha, s\beta) \quad \Longrightarrow \quad \begin{cases} \beta/\alpha = \text{Da} & \text{보존} \\ \sqrt{\alpha/\beta} = \ell_{bd} & \text{보존} \\ \sigma = \sqrt{\alpha\beta}/3 \to s\sigma & \times s \\ \text{Ca} = \vert \nabla E\vert /\sigma \to \text{Ca}/s & /s \\ \text{Hessian} \to s \cdot \text{Hessian} & \times s \\ \text{Goldstone modes } \mu = 0 & \text{보존} \\ \text{non-Goldstone gap} \to s \cdot \text{gap} & \times s \\ \text{Sc}_{T8}, \text{Sc}^{(bd)}, \text{Pr}^{(spatial,onsite)} & \text{보존} \\ \text{Pe}, \text{Bo}, \text{St}, \text{Sc}^{(1)} & \text{depend on T_* 도} \end{cases}$$

**의의**: 단일 parameter s 의 rescaling 이 *H-Morse spectral gap 을 linear 로 expand* — Goldstone modes 는 zero 유지, non-Goldstone 만 stiffen. *§8.1 의 primary H-Morse attack path*.

### §7.6 Identity 6: Sc^{(1)} ↔ St Duality

$$\text{Sc}^{(1)}_k = \frac{\mu_k}{T_*} = \frac{1}{\text{St}_k}$$

*같은 quantity 의 reciprocal* — mode k 의 *thermal vs deterministic relaxation time ratio*. 본 framework 에서는 *Sc^{(1)} 표기 우선* (Prandtl-family 일관성).

---

## §8 — Application to H-Morse Non-Uniform Critical (Original Motivation)

본 §은 *비-uniform critical 의 H-Morse 문제* 를 *§6 dimensionless framework* 으로 *3 quantitative paths*.

### §8.1 Path 1: Surface tension rescaling — Cat A direct

$$\boxed{\text{Apply } (\alpha, \beta) \to (s\alpha, s\beta) \text{ for } s \gg 1}$$

```
CoT step 1: H-Morse non-uniform critical 의 *문제* (사용자 표현): "잔잔하고 부드러운데 변화가 너무 쉽게" — Hessian 의 non-Goldstone eigenvalue 가 0 근처.
CoT step 2: §7.5 identity: rescaling $(\alpha, \beta) \to (s\alpha, s\beta)$ 가 Hessian → s · Hessian, Goldstone 보존, non-Goldstone gap × s.
CoT step 3: 따라서 *H-Morse spectral gap 이 s 에 linear* — *parameter regime 변경만으로 H-Morse 자동 보장*.
→ Cat A direct (from canonical Theorem 4 trivially).

CoC anchors:
  - canonical: §13 Theorem 4 (Hessian 의 linear-in-(α,β) 형식)
  - canonical: T-V5b-T-zero (Cat A) — Goldstone modes 의 zero invariance
  - CSSL §3.2 (critic-survived idea)
inverse_causation_check:
  - if Hessian 의 *비-linear* parameter dependence 있으면: rescaling argument 위반 — *그러나 Theorem 4 는 strictly linear*
  - if Goldstone modes 가 s-dependent: T-V5b-T-zero Cat A 위반 — *그러나 canonical 보장*
```

**Stop condition**: $s$ 가 *너무 큼* 시 thermal $T_*$ 와의 비 (Pe, Sc^{(1)}) 가 흐트러짐 — *optimal s* 는 *Pe ~ O(1)* 영역 (deterministic-thermal 균형).

### §8.2 Path 2: Modica-Mortola Jacobi — Cat B target

$$\boxed{\text{Sharp-interface limit } \text{Sc}_{T8} \to 0 \text{ (or large } s\text{)} \quad \Longrightarrow \quad \text{Hessian} \to \text{Jacobi operator on } \Gamma}$$

```
CoT step 1: Modica-Mortola Γ-convergence (Modica 1987 + Sternberg 1988): Allen-Cahn-like ε-energy → sharp-interface energy σ · Perimeter(Γ).
CoT step 2: Second variation at non-uniform critical: Hessian 의 active-set restriction → Jacobi operator J_Γ = -Δ_Γ - |A|² (Γ 의 Laplace-Beltrami + second fundamental form).
CoT step 3: Jacobi spectrum: 0 (translation Goldstone) + 0 (rotation if applicable) + positive wobble modes.
CoT step 4: 따라서 *sharp-interface limit 에서 H-Morse 자동* (kernel = Goldstone only by classical Jacobi analysis).
→ Cat B target (Modica-Mortola SCC 적용은 graph → continuum step 이 Cat B conditional).

CoC anchors:
  - external: Modica 1987 Arch Rat Mech Anal 98:123 (Cat A in PDE literature)
  - external: Sternberg 1988 Arch Rat Mech Anal 101:209 (Cat A in PDE)
  - external: Allard 1972, Simon 1968, Reilly 1977 (Jacobi operator on submanifolds — Cat A)
  - canonical: §13 T-PF-A1-AR (Cat A, polytope boundary)
  - canonical: §13 V5b-T-zero (Cat A, Goldstone exact zero)
inverse_causation_check:
  - if graph → continuum limit 의 *discrete graph correction* 미고려: 직접 Γ-convergence 적용 불가 (van Gennip-Bertozzi 2012)
  - if Aut(G) 가 비-translation 형 (e.g., D_4 grid): Jacobi spectrum 의 *isotypic decomposition* 추가 분석 필요
```

### §8.3 Path 3: Pr^{(bd)} threshold — H-Morse precondition

$$\boxed{\text{D-HMORSE-LOCAL (C2′) implicit prerequisite}: \quad \text{Pr}^{(bd)} = \frac{\alpha W''(u^*)}{T_*} > 1}$$

```
CoT step 1: D-HMORSE-LOCAL (C2′) 의 "active set well-defined" 조건은 *active band 의 spatial width 가 thermal smearing 보다 큼* 가설 — *암묵적*.
CoT step 2: §6 Pr^{(bd)} = α W''(u^*)/T_* = ratio of deterministic boundary width² / thermal width² (factor scaling).
CoT step 3: Pr^{(bd)} > 1: deterministic > thermal → active set 의 *형상 보존* → (C2′) 자동.
CoT step 4: Pr^{(bd)} < 1: thermal > deterministic → active set *흐림* → (C2′) 위반 가능.
→ Pr^{(bd)} > 1 가 *H-Morse 의 implicit precondition*.

CoC anchors:
  - canonical: §13 D-HMORSE-LOCAL (C2′) Cat B (active set 조건)
  - det/thermal width derivation (이전 Sc 답변 §"boundary 분석")
inverse_causation_check:
  - if T_* → 0 (zero-temperature limit): Pr^{(bd)} → ∞, (C2′) 자동 — *그러나 zero-temp metastability flag* (P-F-A1 Package II 미수립, §9.10 prompt body)
  - if T_* → ∞: Pr^{(bd)} → 0, (C2′) 위반 — *formation 자체 무의미*
```

### §8.4 통합 의의

3 paths 가 *상호 강화*:
- Path 1 (rescaling): *작용 변수* (s, parameter regime 변경)
- Path 2 (Modica-Mortola): *분석 framework* (sharp-interface limit 에서 Jacobi)
- Path 3 (Pr^{(bd)} threshold): *implicit precondition 정량화*

→ *비-uniform critical 의 H-Morse 가 3 가지 path 로 *quantitatively addressable*. 본 framework 의 *primary H-Morse contribution*.

---

## §9 — Cat Assignment Table

각 element 의 *honest Cat 분류*:

| Element | Cat 후보 | 근거 |
|---|---|---|
| §6 numbers 1-6, 8-11 (Pe, Da, Ca, Bo, St, Sc^{(1)}, Sc_{T8}, Sc^{(bd)}, Pr^{(spatial,onsite,bd)}) | **Cat A direct** | canonical parameter 의 *trivial algebraic combination*; canonical Theorem 4 + T-PF-A1-* anchor 직접 |
| §6 #7 Sc^{(2)} (bulk-active) | **Cat B target** | L-HMORSE-DECOMP (Cat B conditional) 의 *Schur complement* 정량화 필요 |
| §6 #12 Pr^{(Kramers)} | **Cat B target (highest leverage)** | μ_well, μ_saddle 의 *explicit form* 이 SCC formation regime 에서 *별도 derivation 필요* — OP-0005-DYN entry |
| §7 Identity 1 (T8 = Pr ratio) | **Cat A direct (rename)** | canonical SB7 의 dimensionless 재표현, 새 content 0 |
| §7 Identity 2 (Eyring-Kramers) | **Cat B target** | Hänggi-Talkner-Borkovec 1990 standard form 의 SCC 적용 — 적용 자체는 Cat B conditional |
| §7 Identity 3 (Pe-Pr bridge) | Cat A direct (algebraic) | trivial 대수 |
| §7 Identity 4 (Le-analog) | Cat A direct (algebraic) | trivial 대수 |
| §7 Identity 5 (rescaling) | **Cat A direct** | canonical Theorem 4 의 linearity 직접 — *§8.1 의 핵심* |
| §7 Identity 6 (Sc^{(1)} ↔ St duality) | Cat A direct (definition) | trivial 정의 |
| §8 Path 1 (surface tension rescaling) | **Cat A direct** | §7.5 Identity 5 직접 |
| §8 Path 2 (Modica-Mortola Jacobi) | **Cat B target** | continuum limit + Γ-convergence 적용 필요 |
| §8 Path 3 (Pr^{(bd)} threshold) | Cat B target | D-HMORSE-LOCAL (C2′) 의 *quantitative threshold* 도출 |

### §9.1 Net Cat distribution

- **Cat A direct**: 11 elements (catalog definitions + algebraic identities + Path 1)
- **Cat B target**: 5 elements (Sc^{(2)}, Pr^{(Kramers)}, Identity 2, Path 2, Path 3)
- **Cat C / OPEN**: 0 elements (본 framework 는 *후보 catalog only*, OPEN problem 의 *attack point 명시* — *해결 시도 아님*)

### §9.2 Highest leverage (W9+ priority)

1. **Pr^{(Kramers)}** (Cat B target) → OP-0005-DYN attack → T-P-F-ε0-K Cat A path + D-ST-4 Cat A
2. **Surface tension rescaling** (Cat A direct) → §8.1 의 H-Morse parameter regime 보장
3. **Modica-Mortola Jacobi** (Cat B target) → §8.2 의 *non-uniform H-Morse 의 analytical framework*

---

## §10 — Risk Catalog (CN10 Drift + NS Literal Interpretation)

### §10.1 R1 — CN10 drift to fluid reduction

**Severity**: HIGH (if happens)
**Likelihood**: MED (NS structural mappings 가 *환원 충동* trigger)
**Mitigation**:
- 모든 mapping 의 ✓/≈/❌ 명시 (§4)
- 5 fundamental incompatibilities 명시 (§5)
- *contrastive only* 표현 enforcement (§1.2)

### §10.2 R2 — NS literal interpretation (관성 도입 충동)

**Severity**: CRITICAL (Package I Cat A cascade 파괴 시)
**Likelihood**: LOW (§5.1 명시적 금지)
**Mitigation**:
- §5.1 의 5 Cat A theorem cascade 표
- *Reynolds / Weber 의 직접 form* 사용 0 (§5.2)
- Mori-Zwanzig 0 (§5.3)

### §10.3 R3 — Mori-Zwanzig 재시도 충동

**Severity**: HIGH (CV-1.18 SEAL deprecation 위반)
**Likelihood**: LOW (CV-1.18 SEAL 명시적 deprecation 인지)
**Mitigation**: §5.3 명시

### §10.4 R4 — CSSL energy terms 재시도

**Severity**: HIGH (critic-rejected, CN4 파괴 위험)
**Likelihood**: LOW (critic 평가 명시적 review)
**Mitigation**: §5.4 명시 + working/cssl/01_critic_evaluation.md 참조

### §10.5 R5 — Sc, Pr 의 *과도한 Cat A 주장*

**Severity**: MED (silent OP resolution 위험)
**Likelihood**: MED (catalog 정의가 *trivial 해 보임*)
**Mitigation**:
- §9 의 *honest Cat 분류* (단순 catalog = Cat A direct, application = Cat B target)
- Pr^{(Kramers)} Cat B 명시 (Eyring-Kramers prefactor 의 *SCC 적용* 은 derivation 필요)

### §10.6 R6 — Dimensionless framework 의 *philosophical drift*

**Severity**: LOW
**Likelihood**: MED (dimensionless 표현이 *physics-like vocabulary* 도입)
**Mitigation**:
- 모든 number 의 *canonical parameter only* (no new abstract concept)
- *contrastive standard tool* 명시 (CN10 compliance)

---

## §11 — Canonical OPEN Problem Leverage Map

본 §은 *어느 dimensionless number 가 어느 canonical OPEN problem 의 advance 의 channel* 인지 명시.

### §11.1 OPEN problems table

| Canonical OP / 정리 | 현재 status | dimensionless 분석 후 가능한 advance |
|---|---|---|
| **OP-HMORSE-SADDLE** (canonical.md:594, OPEN) | OPEN, saddle-point Hessian regularity | critic §A.3 restricted reformulation + §8.1 surface tension rescaling + §8.2 Modica-Mortola Jacobi |
| **OP-0005-DYN** (Kramers transition rates, OPEN W9+) | OPEN | **§6 Pr^{(Kramers)} 가 prefactor 의 structural input — *highest leverage*** |
| **T-P-F-ε0-K** (Cat B conditional on H5, CV-1.7) | Cat B | Cat A path 의 *prefactor portion* 완성 via Pr^{(Kramers)} (Identity 2) |
| **D-ST-4** (Cat B candidate, CV-1.6) | Cat B, P-F flagged | Pr^{(Kramers)} explicit form 후 Cat A 가능 |
| **OP-0008** (σ^A K-jump 비결정성) | Cat C partial | Pr^{(Kramers)} prefactor 의 *부분 quantification* |
| **L-HMORSE-LOCAL** (Cat B, CV-1.16) → Cat A | Cat B | §8.1 rescaling + §8.3 Pr^{(bd)} threshold → uniform critical 부분 Cat A 강화 (오늘 03 §6 NEW L-INV-1/2/3 후속) |
| **L-HMORSE-DECOMP** (Cat B conditional, CV-1.16) | Cat B | Sc^{(2)} 의 bulk-active spectral 분리 정량화 → conditional 해소 path |
| **L-BOUNDARY-MODE-EXCLUSION** (Cat C, CV-1.16) | Cat C | Modica-Mortola Jacobi (§8.2) 의 boundary wobble eigenvalue 정량 |
| **P-F-A1 Package II** (OPEN) | OPEN | Eyring-Kramers Cat A 진입 시 Package II 의 *완성 path* |
| **OP-0009 Multi-Formation Foundations** (OPEN) | OPEN | K-jump events 의 Pr^{(Kramers)} 분석 (T-K-Select-PF 와 결합) |

### §11.2 Leverage prioritization

**Tier 1 (Pr^{(Kramers)} 의 multi-OP advance)**: OP-0005-DYN + T-P-F-ε0-K + D-ST-4 + OP-0008 부분 → *5 OPEN/Cat-B status 동시 advance 가능*

**Tier 2 (Surface tension rescaling + Modica-Mortola)**: OP-HMORSE-SADDLE + L-HMORSE-LOCAL 강화 + L-BOUNDARY-MODE-EXCLUSION + L-HMORSE-DECOMP → *비-uniform critical H-Morse 전반 advance*

**Tier 3 (보조 정량화)**: Sc^{(2)} (H-Morse spectral gap quantification) → Tier 2 의 supporting infrastructure

### §11.3 Critical caveat

본 framework 는 *attack point 명시 only*; *실제 해결 시도 아님*. 각 OPEN problem 의 advance 는 *별도 W9+ working session* 필요 — 본 framework 는 그 *entry framework*.

---

## §12 — CoT/CoC Archival + Hard Constraint Check

### §12.1 핵심 CoT chain archive (mode-level)

```
CoT-CORE: 본 framework 의 정당화 chain

CoT step 1: SCC 의 H-Morse non-uniform critical + OP-0005-DYN + OP-HMORSE-SADDLE 는 모두 *spectral/dimensional 분석* 필요.
CoT step 2: 이들의 *common framework* 부재로 attack 이 *case-by-case ad hoc*.
CoT step 3: Fluid mechanics 의 dimensionless analysis 는 *유사 problem (overdamped reaction-diffusion spectral)* 의 80-year toolkit — *structural ideas* 의 *contrastive import* 가 highest leverage.
CoT step 4: NS equation 의 4 structural components (temporal/convective/pressure/viscous/forcing) 중 (1)(3)(4)(5) 는 SCC 와 ✓/✓✓/≈/≈ mapping; (2) convective 만 ❌ incompatible (관성 부재).
CoT step 5: 이 mapping 의 *수학적 implication* = dimensionless numbers (Pe, Da, Ca, Bo, Sc, Pr) 가 *canonical parameter only* 로 정의 가능 + T8 critical 의 *dimensionless rename* (Sc_{T8}) + Eyring-Kramers prefactor 의 *highest leverage attack* (Pr^{(Kramers)}).
→ Therefore: 본 framework = *consolidated dimensionless toolkit*, *fluid 환원 아님*, *각 SCC OPEN 의 entry point 명시*.
```

### §12.2 핵심 CoC anchored chain

```yaml
target: dimensionless framework 가 canonical CN1-16 + DECL-1.0 Q1-Q6 와 호환되며 canonical OPEN problem 의 systematic advance 의 leverage 제공.

prior_anchors:
  - canonical: §13 Theorem 4 (Cat A, μ_k formula) — §6 의 모든 Hessian-based numbers 의 source
  - canonical: §13 SB7 (Cat A, Σ_T8 codim-1) — §7.1 Identity 1 의 source
  - canonical: §13 T-PF-A1-SDE (Cat A, CV-1.8) — §3.1 의 source + §5.1 의 inertia 금지 anchor
  - canonical: §13 T-PF-A1-AR (Cat A, CV-1.8) — §4.3 의 mass projector source
  - canonical: §13 T-V5b-T-zero (Cat A) — §7.5 Identity 5 의 Goldstone 보존 source
  - canonical: §13 L-HMORSE-LOCAL/DECOMP (Cat B, CV-1.16) — §8 H-Morse application source
  - canonical: §13 T-P-F-ε0-K (Cat B, CV-1.7) — Eyring-Kramers anchor
  - canonical: OP-0005-DYN, OP-HMORSE-SADDLE (OPEN) — §11 leverage map target
  - CV-1.18 SEAL Non-Overclaim (OP-0021 Routes A/B DEPRECATED) — §5.3 M-Z 금지 anchor
  - DECL-1.0 Q1 (T8 boundary), Q3 (stochastic dynamics), Q4 (K-selection) — §1.3 motivation
  - external: Modica 1987, Sternberg 1988, Bray 1994, Rubinstein-Sternberg 1992 — contrastive analytical tools
  - external: Hänggi-Talkner-Borkovec 1990 — Eyring-Kramers prefactor structural form

causation_chain:
  - canonical Theorem 4 + T-PF-A1-* Package I → SCC 의 first-order Langevin + Hessian spectrum framework (intermediate I1)
  - I1 + dimensionless rationing of (α, β, T_*, μ_k, λ_2, W'', |∇E|, R, σ) → §6 catalog of 12 numbers (intermediate I2)
  - I2 + algebraic 재구성 → §7 의 6 identities (T8 = Pr ratio 등) (intermediate I3)
  - I3 + Eyring-Kramers prefactor (Hänggi-Talkner-Borkovec) 의 SCC 적용 → Pr^{(Kramers)} 가 OP-0005-DYN attack entry (intermediate I4)
  - I3 + Modica-Mortola Γ-convergence 의 SCC 적용 → §8.2 Jacobi operator H-Morse path (intermediate I5)
  - I4 + I5 → §11 leverage map (target)

inverse_causation_check:
  - if Theorem 4 또는 T-PF-A1-* 가 Cat A 가 아니면: 전체 framework 의 *trivial Cat A 부분* 모두 conditional 으로 격하
  - if canonical CN4 (analyticity) 가 변경: dimensionless 분석 의 *parameter rationing* 안전 보장 약화
  - if CN-COB (CV-1.18) 가 변경: Mori-Zwanzig 재허용 → 전체 framework 의 *first-order 가정* 위반
```

### §12.3 Hard constraint check (canonical CN1-16, prompt body §8.1-§8.10)

| Constraint | Status | Evidence |
|---|---|---|
| **CN1** canonical 직접 수정 0 | ✓ | 본 문서 = working layer draft; canonical 미접근 |
| **CN2** Silent OP resolution 0 | ✓ | §11 의 *attack point 명시*, *해결 주장 부재* |
| **CN3** Research OS 재도입 0 | ✓ | 본 문서 = single working file, *new registry directory 0* |
| **CN4 (analyticity, b_D=0)** | ✓ | 새 energy term 0, dimensionless 분석은 *parameter ratio only* |
| **CN5 (4-term independence)** | ✓ | E_cl, E_sep, E_bd, E_tr 별개 처리 |
| **Closure idempotence 가정 0** | ✓ | 미적용 |
| **K 이중 취급 0** | ✓ | K-어휘 부재 (K_field, K_act, K_soft 모두 미사용 in dimensionless framework) |
| **Zero-temp metastability flag** | ✓ | §8.3 inverse causation check 에서 명시 (P-F-A1 Package II 미수립 inline flag) |
| **OMC 풀 오케스트레이션 0** | ✓ | 호출 0 |
| **CN10 (no reductive reduction)** | ✓ | §1.2 + §10.1 명시; 모든 NS reference *contrastive only* |
| **Primitive 전도 0** | ✓ | u_t primitive 유지; dimensionless numbers = derived diagnostic |
| **Inertia 0** | ✓ | §5.1 + §10.2 명시 |
| **Mori-Zwanzig 0** | ✓ | §5.3 + §10.3 명시 |
| **CSSL energy terms 0** | ✓ | §5.4 + §10.4 명시 |
| **DECL-1.0 amend 0** | ✓ | DECL 미수정 |
| **scc/ 수정 0** | ✓ | 본 문서 = doc-only |

**16/16 ✓ verified**.

---

## §13 — Closing Notes + W9+ Forward Hooks

### §13.1 본 framework 의 *scope 명시*

- **What it IS**: dimensionless framework synthesis, OPEN problem leverage map, H-Morse attack toolkit
- **What it IS NOT**: Cat A 증명, canonical promotion, numerical experiment, CSSL 재시도, fluid reduction

### §13.2 향후 W9+ session 의 directly leveraged channels

**Tier 1 priority** (highest leverage):
- `02_kramers_prefactor_op_0005_attack.md` — Pr^{(Kramers)} 의 explicit form derivation + OP-0005-DYN attack (§11 Tier 1)
- `03_surface_tension_rescaling_cat_a.md` — §8.1 path 의 *명시 정리*: L-SURFACE-TENSION-RESCALE Cat A direct
- `04_modica_mortola_jacobi_cat_b.md` — §8.2 path 의 *Cat B target* derivation

**Tier 2 priority** (H-Morse 강화):
- `05_h_morse_pr_bd_threshold.md` — §8.3 의 D-HMORSE-LOCAL (C2′) 의 *Pr^{(bd)} explicit lower bound*
- `06_sc_2_bulk_active_quantification.md` — §6 #7 Sc^{(2)} 의 L-HMORSE-DECOMP Cat B 해소

### §13.3 *Critic re-review trigger*

본 framework 가 *W9+ 의 어느 child file* 에 적용 시, *child file* 의 critic re-review 권장. 본 framework 자체는 *catalog only*, critic 의 fundamental review 불필요.

### §13.4 *canonical entry path*

본 framework 는 *canonical 미진입* (working layer draft). 그러나 *Pr^{(Kramers)} 분석 후 OP-0005-DYN advance 시* 별도 SEAL-prep session 에서:
- canonical OPEN problem catalog (theorem_status.md) 의 OP-0005-DYN status update
- T-P-F-ε0-K Cat B → Cat A path 의 prefactor portion 의 canonical insertion
- CV-1.X SEAL 의 dimensionless framework reference

---

## §14 — One-Sentence Summary

**Navier-Stokes equation 의 4 structural components (temporal/pressure/viscous/external) 가 SCC 의 first-order Langevin + mass projector + smoothness Laplacian + double-well 와 ✓/✓✓/≈/≈ mapping (convective inertial 만 ❌); *overdamped 자연 dimensionless numbers* (Pe, Da, Ca, Bo, St, Sc^{(1-3)}, Pr^{(spatial/onsite/bd/Kramers)}) 12 개가 *canonical parameter only* 로 정의 가능 + *T8 critical = Pr ratio equality* + *Eyring-Kramers prefactor = Pr^{(Kramers)}^{-1/2}* 의 unification; 비-uniform critical H-Morse 의 *3 quantitative paths* (surface tension rescaling Cat A + Modica-Mortola Jacobi Cat B + Pr^{(bd)} precondition Cat B); 5 canonical OPEN/Cat-B status (OP-0005-DYN + T-P-F-ε0-K + D-ST-4 + L-HMORSE-* + OP-HMORSE-SADDLE) 의 *highest leverage attack point* = Pr^{(Kramers)} 분석; *fluid 환원 아님*, *contrastive standard tools only* (CN10), *canonical CN1-16 + CV-1.18 SEAL Non-Overclaim 완전 보존* (16/16 ✓).**

---

*W8-Day3 evening synthesis 완료. CV-1.18 SEALED untouched. CSSL working track 와 별개 fork (working/field_equation_framework/01). W9+ session 의 Tier 1 priority = Pr^{(Kramers)} explicit derivation (02 file candidate).*
