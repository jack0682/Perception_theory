# pre_brainstorm.md — 2026-04-24 Session Pre-brainstorm

**Purpose:** Open-ended hypothesis exploration before plan execution.
**Reference state:** 2026-04-23 evening — Orbital hierarchy empirically confirmed (A-01..A-03 Cat A at specific config), Axiom S1' proposed but atom-language-borrowed, Phase 1-7 methodology scoped in user dialogue, 32 new NQs.
**Thinking mode:** Cautious about borrowing trap. Seek SCC-intrinsic language at every step.

---

## §1. Core question refinement

**어제의 질문** (user): "오비탈처럼 형태적 모드가 있을 수 있나?"
**어제의 답**: Yes — Hessian eigenmode hierarchy confirmed, 56 stable at 32×32, full SCC removes F=1 disk.

**오늘의 질문** (심화): "Orbital structure 가 실제로 존재한다면, 그것의 **SCC-intrinsic generating mechanism** 은 무엇인가?"

**피해야 할 답**: "Atomic orbital 과 구조적으로 동일하다" (reduction)
**추구할 답**: "SCC 의 4-term frustration + graph symmetry 가 discrete spectrum 을 generate 한다 — 원자물리학은 이 현상의 또 다른 instance"

---

## §2. M1 irrep classification — hypotheses + subtleties

### 2.1 $D_4$ irrep structure

2D sq grid free-BC with center-aligned $u^*$: full $D_4$ preserved at center. Translation subgroup broken (finite grid, boundary).

5 irreps:
| Irrep | Dim | Basis | 기대 orbital analog |
|---|---|---|---|
| $A_1$ | 1 | constant / radial $f(r)$ | s-orbital (trivial angular) |
| $A_2$ | 1 | pseudoscalar | rare, higher $\ell$ |
| $B_1$ | 1 | $x^2 - y^2$ | d-orbital, axial |
| $B_2$ | 1 | $xy$ | d-orbital, diagonal |
| $E$ | 2 | $(x, y)$ | p-orbital |

### 2.2 Expected mode-irrep mapping

Pure 2D Laplacian eigenvectors (radial separation):
- $n=0, \ell=0$: $A_1$ (constant)
- $n=0, \ell=1$: $E$ (2-fold)
- $n=0, \ell=2$: $B_1$ + $B_2$ (split by lattice)
- $n=1, \ell=0$: $A_1$ (radial node)

### 2.3 **중요한 재해석**: Mode 0 is translation Goldstone, not orbital

어제 finding: "Mode 0 = p-dominant (ℓ=1)". 하지만:
- Mode 0 이 **near-zero eigenvalue** — Goldstone / soft mode 신호
- 2D 에서 translation invariance 부분적 보존 → 2 zero modes (x-translation, y-translation)
- Angular multipole decomposition 에서 (x, y) translation = $E$ irrep = ℓ=1 처럼 보임
- **그러나 물리적으로 translation** 이지 orbital 이 아님

→ **A-01 Cat A statement 재검토 필수**. 수정안:
- "Mode 0 (translation Goldstone, $E$ irrep): near-zero eigenvalue, ground-state spatial redundancy"
- "Mode 1 = **first genuine orbital excitation**, quadrupole ($B_1$ 또는 $B_2$) 예상"

이 refinement 가 atomic-analog 을 sharpen 하게 한다: atom 에는 translation Goldstone 없음 (localized nucleus). SCC 는 background 없이 $\Sigma_m$ 위 translational-invariant → **SCC 에는 translation orbital layer 가 자연스럽게 존재, atom 과의 중요한 차이**.

### 2.4 Why d-orbital first excited (not p) — deeper

어제 data: β ∈ [3, 12] 에서 Mode 1 = d-dominant. Atom 에서는 2p < 2d always (radial quantum number dominance).

Hypothesis for SCC reversal:
- Translation (Mode 0) absorbs pure dipole response (E irrep)
- 그 다음 orthogonal irreducible mode 가 quadrupole ($B_1$/$B_2$) 이므로 Mode 1 이 d-dominant
- 즉 **atom 과 달리 SCC 에서 p-orbital 은 "translation 의 일부" 로 흡수되어 spectrum 에서 raised**

이것은 예상보다 깊은 insight — SCC 의 pre-objective 성 이 orbital ordering 에 흔적 남김. Translation Goldstone 이 p-symmetry 흡수 → first non-trivial orbital 이 d 가 됨. **SCC-specific phenomenon**.

---

## §3. M3 nodal count — predictions + anomalies

### 3.1 Courant-tight expected

Pure Laplacian spectrum on large graph: Courant bound $\mathcal{N}(\phi_k) \leq k$ tight for most $k$.

Expected:
- Mode 0 (translation, degenerate): nodal count = 1 or 2 (constant-like)
- Mode 1: nodal count = 2 (dipole-like) 또는 더 높음 (d-quadrupole)
- Mode 2: nodal count = 3 또는 4
- ...

### 3.2 Full SCC Hessian corrections

$H_1 = H_{\mathrm{bd}} + H_{\mathrm{cl}} + H_{\mathrm{sep}}$. Pure Laplacian (from $H_{\mathrm{bd}}$) 이 dominant 이지만 cl/sep 보정이 있다.

**Hypothesis**: cl/sep 가 mode ordering 을 shift 하지만 irrep label 은 보존 (symmetry 유지). 따라서:
- Nodal count 순서는 변화 가능
- Irrep label 순서는 불변

이 확인이 가능하면 **Courant bound 는 irrep-wise 로는 tight, 그러나 global ordering 은 SCC-specific**.

### 3.3 Falsification

- Mode 1 이 irrep $E$ 로 나오면 (p-orbital) → 어제 "d-dominant" 해석 오류 또는 angular multipole projection 의 artifact
- Mode 1 이 $B_1$ 또는 $B_2$ 로 나오면 → d-orbital 확정, SCC-specific ordering insight

---

## §4. M2 continuum limit — detailed structure

### 4.1 Effective Hamiltonian derivation

Near $u^*(r) = \frac{1}{2}(1 - \tanh((r-r_0)/\xi_0))$:
- $\delta u$ fluctuation
- $H_1 \delta u = 4\alpha(-\Delta) \delta u + \beta W''(u^*) \delta u + \mathcal{O}(\delta u^2)$

Linearize $W''(u)$ at $u^*$:
- $W(u) = u^2(1-u)^2$
- $W'(u) = 2u(1-u)(1-2u)$
- $W''(u) = 2(1-6u+6u^2)$
- $W''(0) = 2, W''(1/2) = -1, W''(1) = 2$

So $V(r) = \beta W''(u^*(r))/(4\alpha)$:
- $r \ll r_0$ (interior, $u^* \to 1$): $V \to \beta/(2\alpha)$ (positive, repulsive)
- $r \approx r_0$ ($u^* = 1/2$): $V \approx -\beta/(4\alpha)$ (negative, attractive well)
- $r \gg r_0$ (exterior, $u^* \to 0$): $V \to \beta/(2\alpha)$ (positive, repulsive)

**V(r) is a shell attractive well** — modes concentrate near interface $r = r_0$, width $\xi_0$.

### 4.2 Spectrum structure

Radial equation: $-R'' - (1/r)R' + [V(r) + \ell^2/r^2] R = \lambda R$

**NOT hydrogenic**. $V(r)$ is not $-e^2/r$ but shell well. Expected spectrum:
- Bound states concentrated in shell
- Energy gap determined by shell depth $\beta/\alpha$
- Angular quantum number $\ell$ separates within each radial $n$
- **$E_n \neq -1/n^2$** — SCC-specific scaling

### 4.3 Finite-size $D_4$ correction

Full $V(r, \theta) = V_0(r) + \delta V_4(r)\cos(4\theta) + \delta V_8(r)\cos(8\theta) + ...$ (even-order due to $D_4$).

- $\ell=2$ states: $\cos(2\theta), \sin(2\theta)$ — mix with $\ell=6$ via $\delta V_4$
- High β: $\delta V_4$ relative strength increases → mixing observed (어제 "high β mixing")
- **Quantitative prediction**: mixing ∼ $(\xi_0/r_0)^k$ for $\ell-$mixing at order $k$

### 4.4 이것이 SCC-intrinsic 인 이유

- Atomic: Coulomb $-1/r$ → all bound states, hydrogen-like
- SCC: shell well → only finitely many bound states (sometimes), specific geometric spectrum

**두 system 의 orbital structure 는 구조적으로 parallel 이지만 spectrum 은 다르다**. 이것이 "borrowing but not reduction" 의 구체 content.

---

## §5. Frustration mechanism — why orbital emerges at all

### 5.1 Counterfactual reasoning

만약 SCC 에 $\mathcal{E}_{\mathrm{cl}}$, $\mathcal{E}_{\mathrm{sep}}$ 없이 $\mathcal{E}_{\mathrm{bd}}$ 만 있다면:
- Single disk stable (Modica-Mortola)
- Orbital spectrum 있지만 **trivial** — 모든 excited modes 가 unstable against translation/deformation
- "Orbital hierarchy" 가 pattern 으로 drawn out 되지 않음

$\mathcal{E}_{\mathrm{cl}}$ 추가:
- Interior $u=1$ 이 closure FP $c^*$ 와 mismatch
- Energy cost ∝ interior volume × $(1-c^*)^2$
- Interior 가 커지면 cost 증가 → **radial excited state (2s-like)** 가 경쟁력 얻음

$\mathcal{E}_{\mathrm{sep}}$ 추가:
- Uniform interior (all neighbors $u=1$) 는 $D_t = 0$
- Separation wants $D_t > 0$ → interior 가 diversified
- **Angular excited states (2p, 2d)** 가 interior diversity 를 제공

결론: 3 energy term 이 각각 **different orbital direction 을 선호** → orbital hierarchy 는 이 frustration 의 structural 결과.

### 5.2 Frustration quantification

Ideal minimizers per term:
- $u^*_{\mathrm{bd}}$: $\chi_A$ for minimal-perimeter $A$ (disk)
- $u^*_{\mathrm{cl}}$: $c^* \cdot \mathbf{1}$ (uniform at FP)
- $u^*_{\mathrm{sep}}$: checkerboard-like (max local diversity)

Three way conflict:
- No configuration satisfies all three simultaneously
- Ground state = **compromise** minimum of weighted sum
- Compromise has specific spatial structure (orbital mode shells)

Quantify: $\mathcal{F}_{\mathrm{trs}} := \min \mathcal{E} - \sum_i \lambda_i \min \mathcal{E}_i$

Hypothesis: Orbital energy gap ∼ $\mathcal{F}_{\mathrm{trs}}$ (approximately).

### 5.3 Pre-objective connection

"Why SCC is pre-objective" — 이 frustration 이 object (단일 disk) 를 수학적으로 금지한다. Self-reference (closure) 가 localization 을 방지하고, separation (anti-cohesion) 이 internal structure 를 강제한다.

오늘 G4 + G5 작업에서 이것을 **명시적 theorem** 으로 만드는 것이 중요 target: "Theorem (Pre-Objective Structure): For $(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}) \neq 0$, no global minimum of $\mathcal{E}$ on $\Sigma_m$ admits $K_{\mathrm{step}} = \mathcal{F} = 1$ configuration simultaneously."

(Statement level Cat B/C 로 시작, 증명 필요)

---

## §6. Axiom S1' redraft attempt — SCC-intrinsic

### 6.1 Current (Apr 23) formulation (atom-borrowed)

> "$\mathrm{Formation}(u^*) = \{(c_k, \xi_k, n_k, \ell_k) : k = 1, \ldots, \mathcal{F}(u^*)\}$ where $(n_k, \ell_k)$ is dominant Hessian eigenmode."

Problem: $(n, \ell)$ 은 atomic QM 용어. "Dominant" 는 vague.

### 6.2 Redraft v1 (SCC-intrinsic)

> **Axiom S1' (Cohesion Mode Quantization).** Let $u^*$ be a Morse-index-0 local minimum of $\mathcal{E}[u]$ on $\Sigma_m$. Then:
>
> (i) $\mathcal{F}(u^*) := |\{i \in X : u^*(i) > u^*(j) \ \forall j \sim i\}| \in \mathbb{Z}_{\geq 1}$ is well-defined.
>
> (ii) For each $k = 1, \ldots, K$ where $K$ is spectral-dimension cutoff, the $k$-th lowest nontrivial (post-Goldstone) eigenvector $\phi_k$ of $\mathrm{Hess}\,\mathcal{E}(u^*)$ admits:
>    - nodal domain count $n_k \in \mathbb{Z}_{\geq 0}$ (M3, graph-intrinsic)
>    - irrep class $[\rho_k] \in \widehat{\mathrm{Stab}_G(u^*)}$ (M1)
>    - eigenvalue $\lambda_k \in \mathbb{R}_{>0}$
>
> (iii) The **cohesion signature** $\sigma(u^*) = \big(\mathcal{F}(u^*);\ \{(n_k, [\rho_k], \lambda_k)\}_{k=1}^K\big)$ determines formation identity up to $\mathrm{Aut}(G)$-orbit.
>
> (iv) **Observable bridge**: $K_{\mathrm{step}}(u^*; \tau) \leq \mathcal{F}(u^*)$; equality at $\tau = 1/2$ iff signature is "single-mode" ($n_k \equiv 0$ for $k \leq K$).

**SCC-intrinsic ingredients**:
- $\mathcal{F}$ — graph local maxima
- Nodal count — graph-intrinsic
- Irrep class — $\mathrm{Aut}(G)$ group-theoretic
- Hessian eigenvalue — geometric on $\Sigma_m$

**차용 언어 최소화**: "orbital" 단어 전혀 사용 안 됨. "Mode", "signature", "irrep" 은 generic math/physics 용어.

### 6.3 Axiom S1' verification checklist

- (a) **Axiomatic naturality (AN)**: 기존 canonical axioms A1'-A4, Group B-E 와 충돌 없음?
- (b) **Proof-structural naturality (PSN)**: 기존 단일-formation Cat A 증명이 $\sigma$ framework 하에 재작성 가능?
- (c) **Observable naturality (ON)**: $\sigma$ 이 기존 observables ($K_{\mathrm{step}}$, $\widehat K$, energy) 를 specialization 으로 포함?

이 3 check 가 오늘 G5 에서 수행할 substantive 작업.

---

## §7. CN proof-of-need — 각 CN 필요성

### 7.1 CN15 (Static/Dynamic Separation)

**Why needed**: 
- $F(K)$ Landau monotone argument → $K_{\mathrm{global}} = 1$ (Apr 23 morning, MF §7)
- Observed $\widehat K = 7.76$ (R17) or orbital-excited $\mathcal{F} \gg 1$ (Apr 23 evening)
- 두 사실 **apparent contradiction**

**Without CN15**: 한 쪽을 부정해야 함.
- $F(K)$ monotone 부정 → 이론 재작업
- 관측 부정 → 실험 무효

**With CN15**: 두 정보 양립. 
- Static $K_{\mathrm{global}}$ = energy landscape 의 global minimum
- Dynamic $\widehat K$ = protocol-specific gradient flow endpoint
- 서로 **structurally decoupled**

**Falsification test**: 
- Slow annealing protocol (T → 0 quasi-statically) 이 generic IC 에서 $K_{\mathrm{global}} = 1$ state 에 도달하면 → CN15 weak (thermal dynamics 가 static 을 dominate)
- 도달 못하면 → CN15 supported (topological obstacle 존재, not just kinetic)
- NQ-124 target

**Current evidence**:
- R17 $\widehat K = 7.76$ : 강한 empirical
- Apr 22 X1 V5 hysteresis: different protocols give different $\widehat K$

### 7.2 CN16 (Protocol-Parameterized Observables)

**Why needed**:
- 어떤 observables 은 protocol-invariant (energy, static landscape features)
- 다른 observables 은 protocol-dependent ($\widehat K$, basin identification)
- 구분 규칙 canonical 에 부재

**Without CN16**: 이 두 종류 observables 가 혼용되어 claim ambiguity

**With CN16**: 각 theorem statement 가 "invariant" 또는 "protocol-conditional" 라벨 가짐

**Falsification**: 발견된 protocol-invariant 가 실제 어떤 protocol 에서 변화하면 그 라벨 errata

### 7.3 CN17 (Orbital-Labeled Formation Quantization)

**Why needed**:
- $K_{\mathrm{step}}$ 은 threshold-dependent, $\tau$ 조절로 값 변화
- 진짜 invariant 는 $\mathcal{F}$ (local maxima count) + signature $\sigma$

**Without CN17**: $K$ 를 integer count 로 다루는 기존 모든 theorem 이 partial

**With CN17**: $\mathcal{F}$ 와 signature 가 primary, $K_{\mathrm{step}}$ 은 derived

**Falsification**: 만약 $\mathcal{F}$ 와 $K_{\mathrm{step}}$ 이 실제로 always equal 이면 CN17 redundant. 오늘의 "bilobed K=1" counterexample 이 CN17 을 증거함.

---

## §8. Risks & unresolved tensions

### 8.1 Mode 0 reinterpretation may invalidate A-01 as stated

어제 A-01 Cat A statement 가 "Mode 0 = p-dominant" 을 포함. 만약 Mode 0 = translation Goldstone 으로 판명되면:
- A-01 의 empirical content 는 여전히 참 (Hessian spectrum 계층 존재)
- 하지만 "p-dominant" 표현은 misleading — "E-irrep Goldstone" 으로 수정
- Canonical merge 전에 correction 필수

### 8.2 SCC orbital ordering vs atomic ordering

Atomic: 1s < 2s < 2p < 3s < 3p < 3d
SCC (예상): 1s < (translation Goldstone) < 2d < 2p < 3s < ...?

Translation 이 p-symmetry 흡수 → SCC 에서 2p 가 나타나지 않거나 matter-specific 위치에 있음. 이것이 atom 과의 **구조적 차이** — orbital analogy 는 partial, not complete.

### 8.3 Continuum limit approximation quality

32×32 grid 는 finite. Continuum limit 이 얼마나 good approximation?
- Small $n$: $D_4$ mixing 심함
- Large $n$: continuous limit 근접하지만 finite
- Quantify: mixing strength vs $n$ scaling

### 8.4 "Cohesion signature" complexity

$\sigma = (\mathcal{F}; \{(n_k, [\rho_k], \lambda_k)\})$ 은 많은 구성요소. User 에게 실제 utility 있는가? 
- Pro: complete specification
- Con: 복잡해서 practical observable 로 쓰기 어려움

→ "lightweight signature" + "full signature" 분리 고려. 오늘 G5 작성 시 balance 필요.

---

## §9. Priority ranking (refined)

Highest value per hour:

1. **G2 (M1 irrep)** — 기존 데이터 재분석, 2-3시간, Cat A rigorous upgrade 가능
2. **G3 (M3 nodal)** — G2 와 병렬, 1-2시간 추가
3. **G1 (Axiom Audit)** — Stage 2 closure, 2-3시간, high strategic value
4. **G5 (Axiom S1' + CN)** — G1-G4 synthesis, 2-3시간, canonical-ready output
5. **G4 (M2 continuum)** — theory-intensive, 2-3시간, peer-reviewable prose

즉 **G2+G3 morning → G1 afternoon → G4/G5 evening** 구조.

**Single most important deliverable**: G2 irrep classification table + Cat A refinement 판단 (A-01 revision or confirmation).

---

## §10. Core message to carry into tomorrow

> **"어제의 empirical discovery 를 오늘 graph-intrinsic theorem 으로 올린다. Orbital 언어는 scaffolding, SCC 자체의 structural identification 이 goal. Success = Axiom S1' v1 draft (SCC-intrinsic) + A-01 refinement (Mode 0 reinterpretation if needed) + 77 Cat A 4-layer classification."**

---

## §11. Deep questions (돌아볼 질문들)

- **Q-D5**: Translation Goldstone 이 p-orbital 을 "흡수" 한다면, SCC 의 orbital spectrum 은 atom 보다 **depleted** (fewer distinct orbitals)? 또는 **enriched** (new non-atomic orbitals)?
- **Q-D6**: Pre-objective 개념의 수학적 정의 — "no global minimum has $\mathcal{F} = 1$" 이 충분한가, 더 강한 statement 필요?
- **Q-D7**: Multi-formation orbital 확장 (Phase 5) 에서 "bonding/antibonding" 이 SCC 에서 어떻게 나타나는가? $\widehat K = 2$ 두 formation 의 공간 배치 + Hessian coupling?
- **Q-D8**: SCC 가 discrete spectrum 을 가진다는 것 자체가 **quasi-quantum character** — 하지만 dynamics 는 entirely classical (deterministic gradient flow). 이 조합의 novelty 를 어떻게 formalize?

---

**End of pre_brainstorm.md for 2026-04-24.**
**Theme: Scaffolding → Structure. Orbital borrowing → SCC-intrinsic language. Empirical Cat A → Structural Cat A.**
