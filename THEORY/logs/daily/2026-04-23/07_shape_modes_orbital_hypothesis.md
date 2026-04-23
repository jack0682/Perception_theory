# 07 — Shape Modes and the Orbital Hypothesis

**Session:** 2026-04-23 (continuation; user instruction: "오비탈처럼 형태적 모드가 있을 수 있나? single formation에서 두 가지로 분리된 것이 모드 변경이라면?").
**Target:** SCC single-formation의 **형태 모드 (shape mode)** 체계 분석 — atomic orbital / 구면 조화 (spherical harmonics) 유비. "K=1 → K=2"로 보이는 전이가 **실은 K=1의 quadrupole mode instability / pinching**일 수 있는가? Layer 1 (topological $K_{\mathrm{step}}$) 과 Layer 2 (shape mode coefficients) 의 independence를 정형화.
**Depends on:** `06_gmiss4_deepening.md` §P8 (stratified Morse), `canonical.md` §13 Cor 2.2 (tanh profile); `working/SF/cardinality_open.md` §8 (Round 10 tree structure, secondary bifurcation); `working/SF/mode_count.md` (Hessian spectrum); §SF_layer_classification §1.3 (Layer 정의).

---

## §1. 사용자 제안 정형화

### 1.1 두 가지 주장

사용자 질문은 두 가지로 분해:

- **Q1 (형태 모드 존재)**: K=1 single formation 내부에 atomic orbital처럼 구분 가능한 **shape modes** (1s, 2p, 3d, ...)가 존재하는가?
- **Q2 (K 전이의 재해석)**: "K=1 → K=2"로 관측되는 현상이 사실 **K=1 내부의 shape mode 전환** (e.g., quadrupole pinching) 인가?

### 1.2 이 두 주장의 과학적 동기

고전 물리의 유비:

| 시스템 | "Ground state" | 1st excited | 2nd excited | 고차 |
|---|---|---|---|---|
| Hydrogen atom | 1s | 2s / 2p | 3s / 3p / 3d | 4s / 4p / 4d / 4f |
| Elastic membrane | 기본 진동 | 1st harmonic | 2nd harmonic | ... |
| Quantum droplet | 구형 ground | dipole | quadrupole | 고차 multipole |
| Rayleigh-Plateau instability | cylindrical jet | necking | pinching → droplet split | fragmentation cascade |
| Nuclear fission | spherical nucleus | prolate | dumbbell | split into 2 fragments |

**공통 구조**: 하나의 "대상" 내부에 angular / radial mode가 활성화되면서 형태가 변화; 고차 mode는 **topological split**로 이어질 수 있음.

### 1.3 SCC에서 어떻게 대응하나

K=1 single formation $u^*$ 주변의 Hessian $H_1 := H(u^*)$ 고유벡터를 **shape modes**로 해석:
- 고유값 $\lambda_n > 0$: 안정 모드 (교란 후 복원).
- 고유값 $\lambda_n \approx 0$: zero mode / near-zero mode (translation, rotation).
- 고유값 $\lambda_n < 0$: unstable shape mode — K=1 minimizer가 해당 mode 방향으로 분기 (secondary bifurcation).

**핵심 가설**: Some of these modes, when activated, produce **bilobed / multi-lobed configurations** that **appear as K > 1 in threshold-based counting** but are **single connected field structures**.

---

## §2. Layer 재확인 — "$K_{\mathrm{step}}$"의 임계 의존성

### 2.1 $K_{\mathrm{step}}$의 정의 (canonical 대응)

$K_{\mathrm{step}}(u; \tau) := \#\{\text{connected components of } \{x : u(x) > \tau\}\}$ (step_cohesion.md §5.1).

**$\tau$-의존성**: threshold 변경 시 $K_{\mathrm{step}}$이 변할 수 있음.

### 2.2 경계 예시

**Bilobed configuration** $u^* : [0, L] \times [0, L] \to [0, 1]$ with
$$u^*(x, y) = \tfrac{1}{2}(1 - \tanh((r_1 - \rho_0)/\xi)) + \tfrac{1}{2}(1 - \tanh((r_2 - \rho_0)/\xi))$$
with two centers $c_1, c_2$ separated by distance $d$. 중간 영역 $u^*(\text{midpoint}) = u_{\mathrm{bridge}} \in [0, 1]$ depending on $d, \xi_0, \rho_0$.

- $u_{\mathrm{bridge}} > 0.5$: $\{u > 0.5\}$은 single connected region → $K_{\mathrm{step}}(u; 0.5) = 1$.
- $u_{\mathrm{bridge}} < 0.5$: $\{u > 0.5\}$은 두 disk → $K_{\mathrm{step}}(u; 0.5) = 2$.

**같은 field $u^*$가 $\tau$에 따라 K=1 또는 K=2로 다르게 counted**.

### 2.3 Crisp topological K vs shape K

위의 예시는 $K_{\mathrm{step}}$가 **crisp topological observable**에 불과하며, **underlying field의 "실제 formation 수"**는 threshold-independent 정보로 정의되어야 함을 시사.

대안 정의 후보:

- **$K_{\mathrm{peak}}$**: local maxima 수 (threshold-independent). bilobed u는 K_peak = 2.
- **$K_{\mathrm{mode}}$**: Hessian nontrivial mode count — K-connected-components이 아니라 shape mode 체계 기반.

### 2.4 "K=2처럼 보인다"의 해석

R17 c=0.3 β=30 $\widehat K = 7.76$ — 이것은 $K_{\mathrm{step}}$ 7-8개 components. 하지만:
- 이들이 모두 **독립 well-separated formations** (orbital-theoretically "7 ground-state 1s formations")이거나
- 아니면 **bilobed, multi-lobed K=1 minimizer**의 변환으로 7개 bumps로 보이거나
- 또는 **중간 단계 — 일부는 true formations, 일부는 같은 shape-mode family**.

**사용자의 가설 Q2는 후자 해석**. 7-8개 중 일부는 물리적으로 같은 "formation"의 orbital excited state.

---

## §3. K=1 minimizer의 Hessian 스펙트럼

### 3.1 연속 유비 (2D 원판 K=1)

2D 연속 원판 $B_\rho$에서 K=1 formation $\phi^*(r) = \frac{1}{2}(1 - \tanh((r - \rho)/\xi))$ 주변 Hessian:
$$H_1 \delta u = -4\alpha \Delta \delta u + \beta W''(\phi^*(r)) \delta u$$

**Separation of variables**: $\delta u(r, \theta) = R(r) Y_\ell(\theta)$로 $Y_\ell = e^{i\ell\theta}$ 각 mode:
$$\left[-4\alpha(\partial_r^2 + r^{-1}\partial_r - \ell^2 r^{-2}) + \beta W''(\phi^*(r))\right] R = \lambda R.$$

각 $\ell$에 대해 radial 고유값 문제. **Eigenvalue 저장**: $\lambda_{n\ell}$, $n$은 radial mode number ($n = 0, 1, 2, ...$).

### 3.2 낮은-$\ell$ 모드 분류

- **$\ell = 0$ (s-type, radial)**: radially symmetric deformation. $n=0$은 **breathing mode** (formation size change). 고유값은 질량 보존 제약 하에 양수.
- **$\ell = 1$ (p-type, dipole)**: center-of-mass shift. **Zero mode on translation-invariant domain** (torus). On free-BC disk, positive but small.
- **$\ell = 2$ (d-type, quadrupole)**: 타원 변형 (prolate ↔ oblate). **이것이 pinching의 시작 모드**.
- **$\ell = 3$ (f-type, hexapole / sextupole)**: three-fold elongation.
- **$\ell = 4$ (g-type, octupole)**: four-fold.

### 3.3 Allen-Cahn 유비로부터의 eigenvalue 공식

Allen-Cahn droplet (2D)의 well-known 결과:

**Radial mode ($\ell = 0$, $n = 0$, breathing)**:
$$\lambda_{00} = -\frac{\sigma}{\rho^2}\cdot (1 - O(\xi/\rho))\quad(\text{negative if }\rho < \rho^*)$$
where $\sigma$ is surface tension, $\rho^*$ is critical droplet size. 너무 작은 droplet은 shrink (negative mode); 너무 큰 droplet은 grow (but in constrained problem, stays stable).

**With mass constraint** (SCC): breathing mode is **zero mode** (mass conservation) OR constrained out.

**Angular mode ($\ell \geq 1$, $n = 0$)**:
$$\lambda_{0\ell} = \frac{\sigma}{\rho^3}\cdot(\ell(\ell+1) - 2) + O(\xi/\rho^3)$$
(shape stability formula for 2D droplet).

- $\ell = 1$: $\lambda_{01} = 0$ — translation zero mode.
- $\ell = 2$: $\lambda_{02} = 4\sigma/\rho^3 > 0$ — quadrupole stable at finite $\rho$.
- $\ell = 3$: $\lambda_{03} = 10\sigma/\rho^3 > 0$.
- $\ell \geq 2$: stable.

**But**: in SCC with 4-term energy, $\sigma$ depends on $\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}$, and closure correction can **reduce** effective $\sigma$ → lower shape-mode eigenvalue.

### 3.4 SCC-specific reduction of $\lambda_{0\ell}$

Closure term $\mathcal{E}_{\mathrm{cl}}$ adds self-referential correction (CN14: closure expands metastability; specifically reduces $d_{\min}^*$ by 30%). In shape-mode terms: closure **stiffens the formation interior** but **softens certain angular modes**.

**Conjecture S1**: Quadrupole mode $\lambda_{02}^{\mathrm{SCC}} < \lambda_{02}^{\mathrm{AC}}$ due to closure contribution.

**Implication**: At sufficiently high $\beta$ or specific $c$ regime, $\lambda_{02}^{\mathrm{SCC}}$ can cross zero → **quadrupole instability** → K=1 minimizer bifurcates to elongated shape → eventually pinches → "K=2" observed.

### 3.5 Graph-discrete realization

On 2D lattice (not continuous disk), "spherical harmonics" are approximated by graph eigenmodes:
- $\ell = 0$: trivial irrep of local $D_4$ rotation.
- $\ell = 2$: 2-dim irrep of $D_4$ (quadrupole approximation).
- $\ell = 4$: axis-selected 1-dim irrep.

**Round 4** $\Phi_4$ = $\int \psi^4$ ratio classification ($A_2/A_1 \in \{2, 4\}$) reflects exactly **quadrupole mode's angular symmetry**. So Round 4 Cat A **implicitly covers the orbital mode transition**.

---

## §4. Orbital taxonomy in SCC

### 4.1 Proposed nomenclature

For K=1 formation at minimizer $u^*$, define **orbital classification**:

| Orbital | Analog | Radial ($n$) | Angular ($\ell$) | Shape |
|---|---|---|---|---|
| **1s** | Ground state | 0 | 0 | Radially symmetric single disk |
| **2s** | Breathing excited | 1 | 0 | Single disk with radial node |
| **2p** | Translation | 0 | 1 | Shifted disk (trivial on torus) |
| **2d / 3d** | Quadrupole | 0 | 2 | Elongated / dumbbell |
| **3f / 4f** | Hexapole | 0 | 3 | Tri-lobed |
| **4g** | Octupole | 0 | 4 | Four-lobed cross |
| **5h** | etc. | 0 | 5 | ... |

**Notation**: $n\ell$ in atomic notation (principal + angular). The first number is total node count ($n + \ell + 1$ in some conventions).

### 4.2 Ground-state analog: 1s

Canonical Cor 2.2 Cat A tanh profile **IS** the 1s orbital of SCC K=1. All of Cor 2.2's supra-lattice analysis is the SCC equivalent of "hydrogen 1s ground state."

### 4.3 Excited-state modes as bifurcation products

**First-excited**: 2p — translation, zero mode on symmetric domain. Not a "new" minimizer; just displacement.

**2d / 3d quadrupole**: **genuine new shape**. Elongated K=1 configuration. Arises as secondary bifurcation from 1s when $\lambda_{02} \to 0$.

**Higher modes**: tertiary bifurcation cascade.

### 4.4 Connection to Round 10 Tree Structure

Round 10 (R22) "Tree Structure Theorem + saddle-node mechanism" describes cascade of bifurcations. In orbital language:

- **Primary bifurcation** (T-Birth-Parametric): uniform (K=0) → K=1 1s at $\beta_{\mathrm{crit}}^{(2)}$.
- **Secondary bifurcation 1**: K=1 1s → K=1 2d (quadrupole activated) at some $\beta_{\mathrm{sec}}^{1\to 2d}$.
- **Secondary bifurcation 2**: K=1 2d → K=2 (pinching) OR K=1 3d (higher multipole).
- **Cascade**: further secondary bifurcations up to fragmentation.

**Round 10 Cat A tree** corresponds to **orbital excitation ladder**.

### 4.5 Claim (orbital classification)

> **Claim 4.1 (Orbital classification, Cat B structural)**: Every well-separated local minimizer of SCC energy on $\Sigma_m$ with $K_{\mathrm{step}} = 1$ has a unique orbital label $n\ell$ (or mixed label for non-radially-symmetric domains) corresponding to Hessian eigenmode excitation pattern.

Proof sketch: At $u^*$, the Hessian $H_1$ has eigenbasis. The perturbation structure of $u^*$ from its "1s ground state" (pure tanh) decomposes into eigenmodes. Dominant angular component determines the orbital label.

**Status**: **Cat B** — requires formalizing the "ground state" reference and the decomposition. Not elementary on graph (angular symmetry broken).

---

## §5. Bifurcation from 1s via orbital mode activation

### 5.1 Quadrupole (2d) bifurcation

Consider K=1 1s at parameters $(\beta, c, G)$ with $\lambda_{02}(\beta, c, G) > 0$ (quadrupole stable).

As $\beta$ (or some parameter) increases past $\beta_{\mathrm{sec}}^{1\to 2d}$: $\lambda_{02}$ crosses zero. **Supercritical pitchfork** emerges — two new minimizers with nonzero quadrupole amplitude.

Near bifurcation (Crandall-Rabinowitz):
$$u^*_{\mathrm{2d}}(\beta) = u^*_{\mathrm{1s}}(\beta) + A_{2d}(\beta) \cdot \psi_{02}(x) + O((\beta - \beta_{\mathrm{sec}})^{3/2})$$

with $A_{2d}(\beta) \propto (\beta - \beta_{\mathrm{sec}})^{1/2}$ (standard pitchfork).

Quadrupole mode $\psi_{02}$ on 2D lattice: $D_4$ 2-dim irrep. Corresponds to elongation along one of two axes.

### 5.2 Pinching transition

As $A_{2d}(\beta)$ grows (with $\beta$ increasing), the elongated 1s formation develops a constriction at center. When $u^*(\text{center}) < \tau = 0.5$:
- Constriction pinches off → $K_{\mathrm{step}}$ jumps from 1 to 2.
- Field $u^*$ continuous across this — no topological change at Layer 3 (continuous level), only at Layer 1 (threshold count).

**Critical $\beta_{\mathrm{pinch}}$**: value where $u^*(\text{center}) = \tau$.
- $\beta_{\mathrm{pinch}}$ is **later** than $\beta_{\mathrm{sec}}^{1\to 2d}$.
- $(\beta_{\mathrm{sec}}, \beta_{\mathrm{pinch}})$: region of **"bilobed K=1"** — Hessian quadrupole activated but $K_{\mathrm{step}}$ still 1.

### 5.3 Cascade: 2d → 3d → 4d → ...

Continuing bifurcations:
- 1s → 2d (quadrupole) at $\beta_{\mathrm{sec}}^{1\to 2d}$.
- 2d → 3d (hexapole added) at $\beta_{\mathrm{sec}}^{2d \to 3d}$.
- 3d → 4d (octupole) at $\beta_{\mathrm{sec}}^{3d \to 4d}$.

Each higher multipole activation can pinch formation into **K=2, K=3, K=4, ...** components respectively (through τ-threshold crossings at different locations).

### 5.4 Claim (K-step cascade vs orbital cascade)

> **Claim 5.1 (orbital-K_step correspondence, Cat B)**: The sequence of $K_{\mathrm{step}}$-increasing pinching events
> $$K=1 \to K=2 \to K=3 \to \ldots$$
> under gradient flow with increasing $\beta$ **may correspond** to orbital excitation sequence
> $$\text{1s} \to \text{2d} \to \text{3d} \to \ldots$$
> via successive shape-mode instabilities.

**Status**: Cat B **hypothesis**. Requires verification — not every $K_{\mathrm{step}}$ transition is an orbital transition; some may be independent nucleation events.

### 5.5 Test: multi-K from orbital vs nucleation

Two mechanisms for $K_{\mathrm{step}}$ change:
- **(A) Orbital pinching**: K=1 field distorts + pinches → K≥2 from within. Field remains **continuous across transition**; just τ-crossing.
- **(B) Independent nucleation**: separate formation nucleates from uniform regions of u ≈ c. **Topological birth** — new field peaks where previously flat.

**Diagnostic**: 
- In (A), field has **one central region** with distortions — not true "two separate formations" at Layer 3.
- In (B), field has **two distinct peaks** separated by flat minimum.

Numerically: compute field's **connected components at $\tau = \tau_\star$ below $\min u^*$**. If single, it's (A). If multiple, it's (B) or (A) post-pinch.

---

## §6. Revisit Formation Quantization in light of orbitals

### 6.1 Formation Quantization (step_cohesion.md §1) says:

$$u^* = \sum_{k=1}^{K(u^*)} \phi_k^* + r(u^*)$$

with $K(u^*) \in \mathbb{Z}_{\geq 0}$ topological invariant.

### 6.2 Orbital refinement

If some of the $\phi_k^*$ are not independent formations but **lobes of one formation's higher orbital**, the decomposition should be:
$$u^* = \sum_{f=1}^{\mathcal{F}} \Phi_f^*(x; n_f, \ell_f) + r(u^*)$$

where:
- $\mathcal{F}$ = number of **true formations** (topologically-independent).
- $\Phi_f^*$ = formation $f$ with **orbital label** $(n_f, \ell_f)$.
- Single formation $\Phi_f$ with $\ell_f > 0$ has **multiple lobes** visible as $K_{\mathrm{step}}$ > 1 pieces **at small $\tau$**.

### 6.3 Revised K_step interpretation

$K_{\mathrm{step}}(u^*; \tau)$ at canonical $\tau = 0.5$ does NOT necessarily count true formations. It counts **threshold-crossings**.

**True formation count $\mathcal{F}$** should be:
$$\mathcal{F}(u^*) := \#\{\text{connected components of } \{x : u^*(x) > \tau_{\mathrm{min}}\}\}$$
with $\tau_{\mathrm{min}} = \min_x u^*(x) + \varepsilon$ for small $\varepsilon$ — i.e., counts connected components at very low threshold.

At very low $\tau$, even bilobed K=1 1s is single component (background fills connecting region). Only true-independent formations give multiple connected components.

**Alternative**: **Morse count** — number of local maxima of $u^*$. This is topologically robust.

### 6.4 Layer refinement

- **Layer 1_a (threshold-K, $\tau$-dependent)**: $K_{\mathrm{step}}(u^*; 0.5)$ — **protocol / threshold observable**.
- **Layer 1_b (topological-K, $\tau$-independent)**: $\mathcal{F}(u^*)$ = number of local maxima — **intrinsic to field**.
- **Layer 2 (orbital label)**: $(n_f, \ell_f)$ per formation — shape descriptor.

### 6.5 Claim (orbital-aware Formation Quantization)

> **Claim 6.1 (Orbital-aware FQ, Cat B structural)**: Every well-separated K=1 (at $\tau = 0.5$ after pinching) minimizer is either:
> (i) A **true K=2 independent formation** (via independent nucleation, Mechanism B), OR
> (ii) A **K=1 2d orbital** (via quadrupole pinching, Mechanism A)
> and these are distinguishable via $\mathcal{F}(u^*)$ (Mechanism A: $\mathcal{F} = 1$; B: $\mathcal{F} = 2$).

---

## §7. Connection to R22 V5 (protocol-dependent basin selection)

### 7.1 V5 hysteresis finding

R22 V5 hysteresis (step_cohesion.md §6 C-X1V5): at β ≈ 7, LOW branch and HIGH branch coexist. LOW is K=1 1s pattern, HIGH corresponds to K-HIGH (e.g., K=13).

### 7.2 Orbital interpretation of V5

LOW branch: 1s ground-state formation (low energy).
HIGH branch: could be either
- (A) Independent nucleation of many formations (K_step = 13 as independent bumps).
- (B) High-orbital K=1 state (1s + multipole excitations giving 13 visible lobes).

**V7 P3 distribution** (β=9, 200 seeds): Gaussian around K̂=13, σ≈1.5. If (A), distribution would peak at integer values (discrete). If (B), distribution would be continuous (shape-mode amplitude variations give continuum of K_step).

**V7 P3 empirical**: Gaussian-looking distribution (continuous), consistent with **(B) orbital excitation**.

### 7.3 Alternative: spectral protocol-seed hypothesis

Spectral seeding (Fiedler-init) may align with **specific orbital mode** of K=1:
- Low-σ Fiedler-init: seeds 1s ground state.
- High-σ random-init: seeds higher orbital modes (2d, 3d, ...) due to noise spread across eigenmodes.

**Implication**: Protocol noise amplitude $\sigma_0$ controls **orbital excitation level**. This is a **protocol-aware orbital theory**.

### 7.4 Claim 7.1 (protocol-orbital hypothesis, Cat C)

> **Claim 7.1 (Protocol-orbital, Cat C)**: Protocol noise amplitude $\sigma_0$ controls orbital excitation level $(n, \ell)$ of the landing basin. Low $\sigma_0$ → 1s ground state; high $\sigma_0$ → higher multipole states, appearing as $K_{\mathrm{step}} > 1$ at threshold τ=0.5 via lobe pinching.

**Testable**: Fix $(β, c, G)$; vary $\sigma_0$. If Claim 7.1 correct, $\widehat K$ should **grow with $\sigma_0$** continuously.

**Empirical context**: V7 P2 noise sensitivity (logs 2026-04-22 §18.1): "higher noise ⇒ HIGH branch vanishes entirely" — **opposite of prediction!** At **very high** noise ($\epsilon = 0.1$), HIGH basin vanishes. Reason: noise is too large to settle into any specific basin; flow is destabilized.

Refined: Claim 7.1 works in **moderate-noise** regime. At low $\sigma_0$: 1s. At moderate $\sigma_0$: higher orbitals (K>1 apparent). At very high $\sigma_0$: no settled basin. 

**Trinary regime**:
- $\sigma_0 < \sigma_*^{(1)}$: 1s deterministic (K=1).
- $\sigma_*^{(1)} < \sigma_0 < \sigma_*^{(2)}$: orbital excitation — higher $n\ell$ modes active.
- $\sigma_0 > \sigma_*^{(2)}$: destabilized — settling fails.

---

## §8. Implications for Theorem G-miss-4 v2

### 8.1 $\widehat K = 1$ reinterpretation

All (S1)-(S9) of §06 are about **$K_{\mathrm{step}} = 1$**, i.e., single connected super-threshold region. Under orbital theory:

- **$K_{\mathrm{step}} = 1$** could be EITHER 1s ground OR 2p/3d/... orbital (bilobed, tri-lobed, ... still single connected at $\tau = 0.5$).
- The physics of "single formation" (at $\mathcal{F} = 1$ level) is **more general** than $K_{\mathrm{step}} = 1$.

### 8.2 True K=1 vs apparent K=1

**True K=1** ($\mathcal{F} = 1$): one local maximum of field.
**Apparent K=1** ($K_{\mathrm{step}} = 1$ at τ=0.5): one connected super-threshold region.

These differ when:
- Bilobed configuration has bridge above 0.5 → apparent K=1 but $\mathcal{F} = 2$.
- Multi-lobe "sunflower" configuration with single central peak → apparent K=1 and $\mathcal{F} = 1$.

### 8.3 Revised Theorem G-miss-4 conditions

Conditions (S1)-(S9) guarantee **apparent K=1** ($K_{\mathrm{step}} = 1$ at τ=0.5). Under orbital theory:

- Conditions (S1), (S4) (near-critical, small-noise): 1s ground state → $\mathcal{F} = 1$, true K=1.
- Condition (S5) c=1/2 involution: maps any K-disk config to complement → $\mathcal{F}$ ambiguous (complement has no local max).
- Condition (S8) geometric c > c_max: K≥2 forbidden → true K=1.

**Refinement**: Conditions (S1), (S4), (S8) give **true K=1**. Conditions (S5), (S6) give **apparent K=1** which may be orbital-excited.

### 8.4 New observation: R18 c=0.5 torus

R18 empirical $\widehat K = 1.00$ at c=0.5 torus β=30: is this 1s ground state or 2d orbital? 

- If 1s: single disk formation of radius $r_0 = \sqrt{0.5 n/\pi} \approx 12.8$ on $L=32$ torus. Fits with periodic boundary.
- If 2d: elongated formation or stripe configuration on torus. Fits perfectly (stripe wraps torus).

**Prediction**: Measure $\mathcal{F}$ (local max count) or Hessian spectrum at R18's $u^*$. If $\mathcal{F} = 1$, it's 1s. If $\mathcal{F} > 1$, it's orbital-excited despite $K_{\mathrm{step}} = 1$.

**NQ-92 (new)**: Distinguish 1s ground vs 2d/3d orbital at R18 c=0.5 torus β=30 — experiment proposal.

---

## §9. Connection to physics / mathematical literature

### 9.1 Atomic orbital analogy

Strengths:
- Hessian eigenbasis ↔ orbital basis.
- Angular ($\ell$) + radial ($n$) classification.
- Secondary bifurcation ↔ excited state.

Differences:
- SCC has no fixed "nucleus"; formation is self-organizing.
- SCC's orbital eigenvalue positivity ensures formation stability — in hydrogen, orbital energies are negative (bound states).
- SCC has mass constraint $\sum u_i = m$; no analog in hydrogen.

### 9.2 Rayleigh-Plateau instability

Classical Rayleigh-Plateau: cylindrical jet of liquid is unstable to sinusoidal modulation → pinches into droplets.
Modes: $\delta r(z) = \epsilon \cos(kz)$; instability for $k r_0 < 1$.

SCC analog: elongated formation with sinusoidal density modulation → pinches into multiple lobes.

Connection: **Rayleigh-Plateau is the 1D analog** of quadrupole pinching in 2D.

### 9.3 Nuclear fission

Liquid-drop model: spherical nucleus deforms to prolate → dumbbell → scission.
Bohr-Wheeler theory: fission barrier.

SCC analog: K=1 formation → 2d quadrupole → pinched K=2.

**SCC-specific**: closure term CN14 modifies fission barrier. Predicted: SCC fission barrier is higher than pure-Allen-Cahn by factor of $O(e^{-\Delta/T})$ where $\Delta$ depends on closure strength.

### 9.4 Quantum droplet / BEC

Bose-Einstein condensate droplet: order parameter $\psi(\mathbf{r})$ with gradient-term cost. Ground state = single droplet; excited states = vortex, quadrupole, ...

SCC is **classical analog** with soft cohesion field $u$ in [0,1] (instead of complex $\psi$). 4-term energy with closure / separation / boundary / transport replaces 2-term BEC energy.

**Shared structure**: shape-mode spectrum, excitation ladder, pinching transitions.

---

## §10. Orbital signature experiment design

### 10.1 Test predictions

**P10.1**: At c=0.5 2D torus β=30 (R18 $\widehat K = 1$), Hessian eigenvalue spectrum has specific orbital structure.
- If 1s dominant: $\lambda_{00}$ small (breathing), $\lambda_{02}$ large (stable quadrupole), $\lambda_{04}$ large.
- If 2d excited: $\lambda_{02}$ small or zero (near instability).

**P10.2**: At c=0.3 2D sq β=30 (R17 $\widehat K = 7.76$): distinguish "7 independent formations" vs "1 formation with 4d+3g combined excitation."
- Measure $\mathcal{F}(u^*)$ via local-maxima count.
- Measure $u^*(x)$ at inter-formation midpoints: if $u^* \sim c$, they're independent; if $u^* > \tau$ slightly above $\tau$, they're bridged (orbital).

**P10.3**: Varying $\sigma_0$ (noise amplitude) at fixed $(β, c, G)$: $\widehat K_{\mathrm{step}}$ and $\mathcal{F}$ should behave differently.
- $K_{\mathrm{step}}$: may grow with $\sigma_0$ (more orbitals excited).
- $\mathcal{F}$: true K count; less $\sigma_0$-dependent (topologically protected).

### 10.2 Implementation sketch

Add to `CODE/scc/diagnostics.py`:
```python
def formation_local_max_count(u, graph, tau_low=0.01):
    """F(u) = # connected components of {u > tau_low}."""
    mask = u > tau_low
    # ... graph-connected-components via BFS
    return n_components

def orbital_signature(u_star, H):
    """Return (n, ell) label via Hessian eigenmode analysis."""
    eigvals, eigvecs = sparse.linalg.eigsh(H, k=20, which='SM')
    # Classify by angular symmetry: dominant eigenvector's angular mode.
    return (n_radial, ell_angular)
```

### 10.3 Status

- **P10.1-P10.3**: testable, not yet performed.
- **plan.md non-goal**: today does not execute experiments. But **test protocol is formalized** for future session.
- **NQ-93 (new)**: P10 experiment design + execution.

---

## §11. Answering the user's questions directly

### 11.1 Q1: "오비탈처럼 형태적 모드가 있을 수 있나?" — YES

SCC K=1 formation has Hessian eigenmode basis decomposable by angular / radial structure (§3). On 2D domain, these correspond to {1s, 2s, 2p, 2d, 3d, ...}. Each eigenmode is a **shape mode** — a perturbation direction characterized by angular frequency $\ell$ and radial node count $n$.

**Cat A structural** (existence of Hessian eigenbasis, immediate).
**Cat B claim** (orbital classification corresponds to mode labels, §4.5).

### 11.2 Q2: "Single formation에서 두 가지로 분리된 것이 모드 변경이라면?" — PARTIALLY YES

- **Sometimes yes**: "K=2" observation could be **K=1 2d quadrupole pinching** (§5.2). In this case:
  - Topologically, field remains single connected at low $\tau$ — $\mathcal{F} = 1$.
  - At $\tau = 0.5$, bridge below threshold → $K_{\mathrm{step}} = 2$.
  - Really a K=1 shape-mode excitation, not two independent formations.
  
- **Sometimes no**: "K=2" observation can be **independent nucleation** — two separate peaks, true $\mathcal{F} = 2$.

**Disambiguation** requires measuring $\mathcal{F}(u^*)$ or Hessian eigenmode structure (§5.5).

### 11.3 Implication for Formation Quantization theorem

Formation Quantization (§MF §3.6 Thm 3.2) **needs refinement**:
- $K(u^*) \in \mathbb{Z}$ as "true formation count" $\mathcal{F}(u^*)$, not $K_{\mathrm{step}}$.
- Decomposition $u^* = \sum_{f=1}^{\mathcal{F}} \Phi_f^*(n_f, \ell_f)$ with orbital-labeled formations.
- Original theorem still correct with "K_step" replaced by $\mathcal{F}$, or "well-separated" interpreted as orbital-independent.

---

## §12. New framework proposal — **Orbital-Augmented Formation Quantization**

### 12.1 Revised ontology

| Layer | Concept | Observable |
|---|---|---|
| Layer 1a | Threshold-K (protocol) | $K_{\mathrm{step}}(u; \tau)$ |
| **Layer 1b (new)** | **True formation count** | $\mathcal{F}(u)$ = local max count |
| **Layer 2a (new)** | **Orbital labels** | $(n_f, \ell_f)$ per formation |
| Layer 2b | Geometry | $(r_f, \xi_0, d_{\min})$ |
| Layer 3 | Field | $u(x)$ |

### 12.2 Revised Axiom S1 (proposed)

**S1'** (Orbital-augmented): Every well-separated local minimizer $u^*$ admits unique decomposition
$$u^*(x) = \sum_{f=1}^{\mathcal{F}(u^*)} \Phi_f^*(x; n_f, \ell_f, c_f, r_f) + r(u^*),$$
where:
- $\mathcal{F}(u^*) \in \mathbb{Z}_{\geq 0}$ = **true formation count** (topological, $\tau$-independent).
- $\Phi_f^*$ = $f$-th formation with orbital state $(n_f, \ell_f)$, center $c_f$, size $r_f$.
- $\|r\|_\infty$ = $O(\exp(-d_{\min}/\xi_0))$ as before.

### 12.3 Relation to current FQ (Thm 3.2)

Current Thm 3.2 (§MF §3.6) uses $K$ implicitly as $K_{\mathrm{step}}$. Under **S1'**:
- Current Thm 3.2's $K$ = $\mathcal{F}$ for 1s-dominant formations.
- For higher-orbital formations, current Thm 3.2's $K$ ≠ $\mathcal{F}$ in general.

**Compatibility**: Thm 3.2 is **Cat A for well-separated, orbital-independent** formations (1s + 1s + ...). For orbital-excited (e.g., 2d pinched), need S1' refinement.

### 12.4 Canonical merge implication

**Proposal (Stage 6)**: Replace step_cohesion.md §1 Formation Quantization Theorem with Orbital-Augmented version S1'. Original is special case.

---

## §13. Multi-perspective integration

This orbital analysis is a **9th perspective** complementing the 8 in `06_gmiss4_deepening.md`:

**P9 (orbital shape modes)**: K=1 formation has internal shape-mode excitation structure; "higher K" may sometimes be K=1 with excited orbital.

**Integration with 06 Theorem G-miss-4 v2**:
- (S1) near-critical: 1s ground-state — **orbital unique** (single 1s).
- (S5), (S6) c=1/2 involution: may give 1s OR 2d even orbital (complement involution ambiguous).
- (S8) geometric c > c_max: forces K_step = 1 but field may be orbital-excited.
- **New (S10) orbital-ground-state protocol**: $\sigma_0 < \sigma_*^{(1)}$ keeps flow in 1s basin — ensures true K=1 (not apparent).

### 13.1 Orbital-aware Theorem G-miss-4 v3

$\widehat K_{\mathrm{step}} = 1$ a.s. (any of the §06 conditions). Additionally:

**Orbital refinement** (Cat B):
- **Claim 13.1**: Under (S1) + $\sigma_0 < \sigma_*^{(1)}$ (low noise), $\widehat K_{\mathrm{step}} = 1$ AND $\mathcal{F} = 1$ (true K=1, 1s ground state).
- **Claim 13.2**: Under (S5), (S6), (S8) alone (higher noise), $\widehat K_{\mathrm{step}} = 1$ but $\mathcal{F}$ may be $\geq 1$ depending on orbital excitation.

---

## §14. New NQ from orbital perspective

- **NQ-92**: R18 c=0.5 torus β=30 at K_step=1 — is it 1s ground or 2d orbital? Local-max count + Hessian spectrum experiment.
- **NQ-93**: Orbital-signature diagnostic implementation in `scc/diagnostics.py` (§10.2).
- **NQ-94**: Quantitative formula for $\lambda_{02}^{\mathrm{SCC}}$ in terms of $\alpha, \beta, \lambda_{\mathrm{cl}}, c$ — closure correction to quadrupole mode.
- **NQ-95**: Cascade bifurcation structure — $\beta_{\mathrm{sec}}^{1s \to 2d}, \beta_{\mathrm{sec}}^{2d \to 3d}, \ldots$ sequence determination.
- **NQ-96**: $\mathcal{F}$ vs $K_{\mathrm{step}}$ discrepancy in R17 (c=0.3 β=30 $\widehat K = 7.76$) — how many are 1s independent vs 1 orbital-excited?
- **NQ-97**: Orbital-ground protocol $\sigma_0 < \sigma_*^{(1)}$ quantitative threshold.

**Total this file**: 6 new NQ (NQ-92..NQ-97).

**Cumulative 2026-04-23**: 25 (03) + 8 (04) + 5 (05) + 8 (06) + 6 (07) = **52 new NQ**.

---

## §15. Canonical merge impact

### 15.1 Proposed new section in canonical

> **§6.S1' (Orbital-Augmented Formation Quantization)**: Single-formation landscape structure decomposes into orbital shape modes $(n, \ell)$. Higher orbital excitation can produce $K_{\mathrm{step}} > 1$ appearance without topological split (§5).

### 15.2 Revision to step_cohesion.md §1

Thm 3.2 (Formation Quantization Uniqueness) → **orbital-augmented S1'** as stronger form; original is 1s-restricted special case.

### 15.3 Revision to SF layer classification

§SF_layer §1.3 Layer definitions extended to include Layer 1a/1b distinction ($K_{\mathrm{step}}$ vs $\mathcal{F}$) and Layer 2a (orbital labels).

---

## §16. Speculative extensions (beyond current SCC)

### 16.1 Orbital "chemistry"

If formations have orbital labels, can **formation interactions** depend on orbital structure?

- Two 1s + 1s formations: weak inter-formation repulsion (pair interaction §MF §5).
- **Two 2d + 2d formations**: directional repulsion — lobes aligned = strong, orthogonal = weak. **Anisotropic pair interaction**.
- 1s + 2d: mixed interaction.

**Speculative**: SCC may exhibit "orbital-dependent chemistry" — analog of molecular bonding based on orbital overlap. **Not currently in scope**.

### 16.2 Orbital hybridization

Analogous to sp3 hybridization in chemistry: in SCC, could **two orbitals mix** to form hybrid state with lower energy?

This would be a **configuration interaction** — linear combination of pure orbitals optimizing nonlinear energy.

### 16.3 Multi-formation orbital configurations

Extension of §MF §2 basin stratification:
$$\mathcal{B}_{K, \vec{o}} = \{u : K(u) = K, \text{orbital config } \vec o = (n_1, \ell_1, n_2, \ell_2, \ldots)\}$$

Basin partition refined by orbital configuration.

### 16.4 Selection rules

In atomic physics, dipole transitions follow $\Delta \ell = \pm 1$ selection rule. In SCC: can secondary bifurcations have analogous **orbital selection rules**?

**Conjectural**: From $(n, \ell)$ to $(n', \ell')$ bifurcation allowed iff specific symmetry conditions met. Round 4 Φ_4 analysis might be the SCC selection rule.

---

## §17. File status

- **Primary deliverable**: orbital hypothesis (Q1 + Q2) formalized. 17 sections covering Hessian eigenmodes, bifurcation cascade, $\mathcal{F}$ vs $K_{\mathrm{step}}$ distinction, S1' Axiom proposal.
- **Answer to user**: YES orbitals exist (Cat A Hessian eigenbasis); PARTIALLY K=1 → K=2 is mode transition (Cat B, depends on mechanism A vs B).
- **New framework**: Orbital-Augmented Formation Quantization (S1') with Layer 1a/1b + Layer 2a distinctions.
- **6 new NQ (NQ-92..NQ-97)**, 52 cumulative session.
- **Intended promotion**: `working/SF/orbital_modes.md` (신규) + `working/SF/step_cohesion.md` §1 update to S1'.

**End of 07_shape_modes_orbital_hypothesis.md.**
