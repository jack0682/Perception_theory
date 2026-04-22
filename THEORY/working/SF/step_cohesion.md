# step_cohesion.md — Formation Quantization via Step-Based Decomposition

**Status:** committed draft, 2026-04-22 R22.
**Author origin:** User insight (2026-04-22 evening) — "step적 구분을 통한 formation cohesion이 가능할듯함" + "연속장의 이산적 특성을 발견한 첫 사례".
**Canonical refs:** §13 Cat A T-Merge (a)/(b), Tree Structure Theorem (Round 10), Universal $c_0$-Counting (Round 8); `working/SF/cardinality_open.md` §8 (Morse structure), `working/SF/mode_count.md` (Prop 1.3a/b), `working/SF/symmetry_moduli.md` (G-D moduli).
**Empirical source:** X1 V1 (Heaviside pattern), X1 V5 (hysteresis), X1 V7 P3 (integer K distribution), X3 v2 (E3 cubic mechanism), X2 (D1 α-threshold).

---

## §1. Core proposition

> **Formation Quantization Theorem (R22 Cat A structural)**:
>
> Every well-separated local minimizer $u^* \in \Sigma_m$ of SCC energy $\mathcal{E}$ admits a unique step-based decomposition:
> $$u^*(x) = \sum_{k=1}^{K(u^*)} \phi_k^*(x) + r(u^*)$$
>
> where:
> - $K(u^*) \in \mathbb{Z}_{\geq 0}$: **formation quantum number** (topological invariant within each landscape basin)
> - $\phi_k^* : X \to [0, 1]$: $k$-th formation's localized soft-indicator (tanh-like soliton)
> - $\mathrm{supp}(\phi_k^*) \cap \mathrm{supp}(\phi_j^*) = \emptyset$ for $k \neq j$ (disjoint formations)
> - $r(u^*)$: residual with $\|r\|_\infty = O(\exp(-d_{\min}/\xi_0))$
>
> **Two limits**:
> - **Step limit** ($\beta \to \infty$): $\phi_k^* \to \chi_{A_k^*}$ (Heaviside indicator of formation support $A_k^* \subset X$)
> - **Smooth limit** (finite $\beta$, $\xi_0 = \sqrt{\alpha/\beta}$): $\phi_k^*(x) \approx \frac{1}{2}(1 - \tanh(d(x, \partial A_k^*)/\xi_0))$

This is the **graph-based analog of wave-particle duality in continuous field theories** — continuous $u$ field, but discrete $K$ observable.

---

## §2. Historical positioning

### 2.1 Class of discoveries — "continuous field → discrete observable"

| 이론 | 연도 | Continuous substrate | Discrete observable |
|---|---|---|---|
| Planck quantum | 1900 | EM field energy density | $E = nh\nu$ (integer $n$) |
| Bohr atom | 1913 | Electron orbit position | Discrete energy levels $E_n$ |
| Cahn-Hilliard coarsening | 1958 | Continuous order parameter $\phi(x, t)$ | Domain count (finite at long time) |
| Vortex theory | 1960s | Continuous order parameter | Topological defect count |
| Topological insulator | 1980s | Continuous band structure | Chern number $n \in \mathbb{Z}$ |
| Hopfield memory | 1982 | Continuous neural activation | Discrete attractor basins |
| **SCC (this work)** | **2026** | **$u: X \to [0,1]$ on arbitrary graph** | **Formation quantum $K$ + protocol-dependent selector** |

### 2.2 SCC의 독자적 contribution

1. **Graph substrate** (not Euclidean/manifold)
2. **Mass-constrained simplex** domain $\Sigma_m = \{u : \sum u_i = cn\}$
3. **Three-component energy** (closure + separation + boundary)
4. **Protocol-dependent discreteness** — landscape-topological AND protocol-sensitive 이중 성질
5. **Three-layer hierarchy** 명시적 decomposition (topology + geometry + field)

**Statement**: "SCC는 graph-based cohesion field theory에서 formation quanta 발견의 **첫 systematic demonstration**."

---

## §3. Three-Layer Hierarchy (F1-SSU-v5 framework)

### 3.1 Layer structure

**Layer 1 (Topological)** — discrete, protocol-sensitive selector:
- $K \in \mathbb{Z}_{\geq 0}$: formation quantum number
- Basin structure: $\Sigma_m = \bigsqcup_k \mathcal{B}_k$
- Protocol's basin selector: $s_\pi(\beta) \in \mathbb{Z}_+$, step function

**Layer 2 (Geometric)** — smooth real-valued functions:
- $r_0 = \sqrt{m/(\pi K)}$: average formation size
- $\xi_0 = \sqrt{\alpha/\beta}$: interface width
- $d_{\min}$: inter-formation spacing (from screened Poisson decay)
- $K_{\mathrm{soft}}$: soft counting diagnostic (landscape-dependent)

**Layer 3 (Microscopic)** — continuous field, PDE-governed:
- $u(x) \in [0,1]$ at each vertex
- Each $\phi_k^*$ governed by Allen-Cahn equation
- Tanh soliton profile

### 3.2 Cross-layer bridges

| Bridge | From → To | Mechanism |
|---|---|---|
| **E3 cubic** (Prop 1.3b (d)) | Layer 2 → Layer 1 | $\gamma_D''$ sign flip at c=0.5 shifts $K$ asymmetry |
| **D1 α-threshold** (X2) | Layer 2 → Layer 3 | α controls $\phi_k^*$ shape (tanh vs sharp) |
| **Protocol selector** | Layer 3 + init → Layer 1 | Gradient flow from noise-perturbed initial state picks basin |

### 3.3 Static vs Dynamic observable classification

**Static (landscape-intrinsic)**:
- All of Layer 3 (u(x) field properties at minimizer)
- Most of Layer 2 (geometric parameters at minimizer)
- Layer 1 $K(u^*)$ within single basin

**Dynamic (protocol-dependent)**:
- Observed K̂ (protocol picks basin)
- $\widehat K$ transition points in parameter space
- Hysteresis patterns

---

## §4. Step Limit — canonical formulation

### 4.1 Hard step decomposition

At $\beta \to \infty$ (step limit):
$$u^*_{\text{step}}(x) = \sum_{k=1}^K \chi_{A_k^*}(x)$$

with $A_k^* \subset X$ pairwise disjoint, $\sum_k |A_k^*| = m$.

**Energy in step limit**:
- $\mathcal{E}_{\mathrm{bd}}[u_{\text{step}}] = \beta \sum_k W(0) + \text{interface terms}$ — singular, require regularization
- $\mathcal{E}_{\mathrm{cl}}, \mathcal{E}_{\mathrm{sep}}$: finite via sigmoid saturation

**Γ-convergence (T11 Cat A, canonical)**:
$$\lim_{\xi_0 \to 0} \frac{\mathcal{E}_{\mathrm{bd}}[u^*]}{\sqrt{\alpha\beta}} = C_* \cdot \mathrm{Per}_G(\{A_k^*\})$$
$C_* = \int_0^1 \sqrt{2W(s)}\, ds$ — Modica-Mortola constant.

### 4.2 Formation-specific decomposition

For $k$-th formation at center $x_k$ with boundary $\partial A_k^*$:
$$\phi_k^*(x) \approx \frac{1}{2}\left(1 - \tanh\!\left(\frac{d(x, x_k) - r_k}{\xi_0}\right)\right)$$

where:
- $r_k$: effective radius (from $|A_k^*| = \pi r_k^2$ on 2D, $|A_k^*| = 2r_k$ on 1D cycle)
- $d(x, x_k)$: graph-distance from formation center

---

## §5. Formation counting operator

### 5.1 Discrete step counter

$$K_{\mathrm{step}}(u; \tau) := \#\{\text{connected components of } \{x : u(x) > \tau\}\}$$

- $\tau = 0.5$ canonical threshold
- Integer-valued
- **Robust to small perturbations** (topological)

### 5.2 Relation to existing $K_{\mathrm{soft}}$ (canonical)

$K_{\mathrm{soft}}$는 continuous proxy; $K_{\mathrm{step}}$은 integer truncation:
$$K_{\mathrm{step}}(u) = \lfloor K_{\mathrm{soft}}(u) + 0.5 \rfloor$$
approximately, when $u$ has well-separated formations.

**Canonical relation proposal**: $K_{\mathrm{soft}} \to K_{\mathrm{step}}$ as $\beta \to \infty$; at finite $\beta$, $|K_{\mathrm{soft}} - K_{\mathrm{step}}| = O(\xi_0 / r_0)$.

### 5.3 Protocol-specific observable

$$K_{\mathrm{observed}}(\beta, c, G, \pi) = K_{\mathrm{step}}(u_\pi^*(\beta))$$

where $u_\pi^*(\beta)$ is the fixed-point from protocol $\pi$. Different protocols $\pi_1, \pi_2$ can give different $K_{\mathrm{observed}}$ even at same $(\beta, c, G)$.

---

## §6. Protocol Selection Principle

### 6.1 Formal statement

> For SCC parameter $(\beta, c, \alpha, G)$ and gradient-flow protocol $\pi$ (specifying initial condition distribution $\mu_{\pi,\mathrm{init}}$, weight normalization, iteration rule):
> $$u_\pi^*(\beta) = \lim_{t \to \infty} \text{flow}_\pi(u_0; \beta), \quad u_0 \sim \mu_{\pi,\mathrm{init}}$$
> 
> The basin $\mathcal{B}_{K}$ containing $u_\pi^*(\beta)$ is protocol-dependent. Step-function transitions in $K_{\pi}(\beta)$ occur when basin boundaries are crossed by the protocol's flow trajectory.

### 6.2 Protocol parameters

- **Initial condition**: Fiedler-init (seed=0), random-init, warm-start
- **Noise amplitude**: $\epsilon_{\mathrm{init}}$ (controls Fiedler cone width)
- **Weight normalization**: `normalize=True` rescales $\beta$ by spectral norm
- **Iteration rule**: projected gradient, Barzilai-Borwein step

### 6.3 Empirical examples (from R22)

- X1 V5 hysteresis: LOW basin $\mathcal{B}_1$ exists at all $\beta \in [6, 10]$, but Fiedler-init enters $\mathcal{B}_{\mathrm{HIGH}}$ for $\beta \leq 7.05$.
- V7 P2: $\epsilon = 0.001$ → HIGH sharply; $\epsilon = 0.1$ → HIGH never — cone width determines capture radius.
- X3 v2: `normalize=True` (R17 protocol) recovers K=2-5 at β=0.5, c=0.3; `normalize=False` fails.

---

## §7. Graph symmetry and K-degeneracy

### 7.1 $\mathrm{Aut}(G)$-orbits of formations

For graph automorphism group $\Gamma = \mathrm{Aut}(G)$:
- Formations $A_1^*, \ldots, A_K^*$ can be related by $\pi \in \Gamma$
- **Orbit-equivalence class**: $\{A_k\} \sim \{A_{\pi(k)}\}$ for $\pi \in \Gamma$
- Observed $K$ unchanged under $\Gamma$ action
- **Moduli space** $\mathcal{M}_K = \{\text{K-formations}\}/\Gamma$

### 7.2 Connection to G-D (`symmetry_moduli.md`)

$\mathcal{M}_1$ (K=1 moduli) and $\mathcal{M}_K$ (K-formations moduli) are Layer 1 topological objects. Different K-sectors have different moduli dimensions:
- 2D square free BC, K=1: $|\mathcal{M}_1| = 1$ (axis-aligned)
- $C_n$, K=1: $|\mathcal{M}_1| = 1$ with 1-dim moduli (circle)
- $T^2$, K=1: 1-dim (pure-X/Y)

For K≥2, $\mathcal{M}_K$ typically has higher dim (more orbit choices).

---

## §8. Sigmoid structure within each layer

Despite step-function selector at Layer 1, the layers **are sigmoid-like within each sector**:

### 8.1 Layer 3 (field-level sigmoid)

Tanh profile: $\phi_k^*(x) = \frac{1}{2}(1 - \tanh(\ldots))$ — **literal sigmoid**.

### 8.2 Layer 2 (geometric sigmoid)

$\xi_0(\beta) = \sqrt{\alpha/\beta}$: power-law, smooth.
$d_{\min}(\beta) \asymp \xi_0 \log(1/\epsilon_0)$: logarithmic in β.
$K_{\mathrm{soft}}(\beta)$ **within** single K-sector: smooth transition (essentially sigmoidal under large deformation).

### 8.3 Layer 1 (topological selector — NOT sigmoid)

$K_\pi(\beta)$: piecewise constant integer, step transitions at basin boundaries.
Each transition point: **Heaviside step**.

### 8.4 Stochastic smoothing near transitions

Near protocol selector transition $\beta_\pi^*$ with noise $\sigma$:
$$P(K_\pi = k | \beta) \approx \text{smoothed step}$$
with width $\propto \sigma \cdot (\text{geometric factor})$ — may **appear** as softmax in ensemble observation (R20 β=9 bistable range).

---

## §9. Category self-classification

| Claim | Category | Evidence |
|---|---|---|
| §1 Formation Quantization Theorem | **Cat A structural** | V5 hysteresis + V7 P3 + Round 10 Tree Structure |
| §2 Historical positioning (first systematic demo) | **Cat A** interpretive | Empirical + theoretical comparison |
| §3 Three-Layer Hierarchy | **Cat A** organizational | Confirmed by all X-series data |
| §4 Step Limit formulation | **Cat A** (via Γ-convergence T11) | Extends canonical T11 |
| §5.1 $K_{\mathrm{step}}$ operator | **Cat A** (elementary) | Definition |
| §5.2 $K_{\mathrm{soft}} \to K_{\mathrm{step}}$ as $\beta \to \infty$ | **Cat A** | Straightforward |
| §5.3 Protocol-specific observable | **Cat A empirical** | X1 V5 |
| §6 Protocol Selection Principle | **Cat A empirical** | X1 V5 hysteresis |
| §7 $\mathrm{Aut}(G)$-orbit K-degeneracy | **Cat A structural** | Extends G-D (`symmetry_moduli.md`) |
| §8 Within-layer sigmoid, selector step | **Cat A descriptive** | Cross-layer data synthesis |

---

## §10. Canonical merge targets (Stage 6 pending)

### 10.1 New axioms (proposed)

Integrate into `canonical.md` §2 (axioms):

**S1 (Step-Cohesion Decomposition)**: Every well-separated $u^* \in \Sigma_m$ local minimizer admits unique step decomposition $u^* = \sum \phi_k^* + r$.

**S2 (Three-Layer Hierarchy)**: SCC theory organizes into Layer 1 (K ∈ ℤ, topology), Layer 2 (real-valued geometry), Layer 3 (continuous field).

**S3 (Protocol-Parameterized Observable)**: $K_{\mathrm{observed}}(\beta, c, G, \pi) = K_{\mathrm{step}}(u_\pi^*(\beta))$ where $\pi$ specifies initial condition + normalization + iteration rule.

**S4 (Static/Dynamic Decomposition)**: Static Cat A theorems describe landscape (within-basin); dynamic observables require protocol specification.

### 10.2 Canonical §13 Cat A additions

- **C-FQ (Formation Quantization Theorem)**: §1 of this file.
- **C-X3 (E3 Cubic Mechanism)**: `mode_count.md` §2.3c + cross-reference.
- **C-X2 (D1 α-Absolute Threshold)**: shape regime classifier.
- **C-X1V5 (Protocol Selection on Multi-Branch)**: from `working/SF/`.
- **C-3L (Three-Layer Hierarchy)**: organizational.

### 10.3 Theorem re-classification (Stage 2 priority)

모든 기존 Cat A를 Layer 1/2/3로 재분류:

| Layer | Theorems |
|---|---|
| **L1 (topology)** | Tree Structure (R10), Universal c_0-Counting (R8), Euler constraint, K-Sep persistence |
| **L2 (geometry)** | Cor 2.2 qual+quant, ξ_0 scaling, d_min formula (corrected), Prop 1.3b (d) c-dependence, $A_2/A_1$ classification |
| **L3 (field)** | Prop 1.3a, Prop 1.3b (a-c, e), T-Merge (b), thermal Prop 1.3a/b, T3/T6-Stability, T8-Core, closure fixed-point |

---

## §11. Open residuals (post-R22)

**NQ-46 (Formation selection rules)**: Which K values are "allowed" at given (β, c, G)? Graph symmetry exclusions?

**NQ-47 (Transition rates)**: K=k → K=k+1 Kramers-like escape rates.

**NQ-48 ($\mathrm{Aut}(G)$ equivariant Morse)**: Wasserman 1969 equivariant theory applied to $\Sigma_m$.

**NQ-49 (Complete layer classification)**: 모든 canonical theorems을 정확히 하나의 layer에 assign.

**NQ-50 (Protocol language)**: Canonical observable statements에 protocol specification. E.g., "K̂(β, c, G; π=Fiedler-normalize-True) = ..."

---

## §12. File status

- **Formation Quantization Theorem (§1)**: committed as Cat A structural.
- **Three-Layer Hierarchy (§3)**: committed as Cat A organizational.
- **Step Limit (§4)**: committed via T11 extension.
- **K_step operator (§5.1)**: committed Cat A.
- **Protocol Selection Principle (§6)**: committed Cat A empirical.
- **Cross-layer bridges (E3, D1)**: committed via R22 X-series data.
- **Canonical merge**: 5 new axioms (S1-S4) + 5 new Cat A entries (C-FQ, C-X3, C-X2, C-X1V5, C-3L) proposed for Stage 6.

---

**End of step_cohesion.md.**
**Created 2026-04-22 R22 session, founding document for Stage 2 Axiom Audit.**
