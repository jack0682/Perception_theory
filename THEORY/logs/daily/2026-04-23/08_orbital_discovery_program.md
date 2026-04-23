# 08 — Orbital Discovery Program: From Metaphor to Substantive Theory

**Session:** 2026-04-23 (continuation; user instruction: 오비탈 유비가 진짜 연결되려면 **다양한 모양이 특정되고 발견되어야 함**. 확률분포 / boundary-blurring / mode-identity / invisible-made-visible 관점 포함).
**Target:** (i) 확률분포 parallel 정형화 (u_field ↔ $|\psi|^2$); (ii) mode identity가 경계 흐릿에도 불구하고 robust하다는 점 증명; (iii) "invisible made visible" 의미 정확화 + SCC에서 보이지 않는 구조 enumerate; (iv) **per-graph 구체적 orbital enumeration** (2D sq, 2D torus, 1D cycle, $K_n$, trees); (v) **Discovery protocol** — SCC에서 orbital을 실제로 발견하는 알고리즘.
**Depends on:** `07_shape_modes_orbital_hypothesis.md` (orbital hypothesis 정형화, S1' Axiom), `canonical.md` §13 T-Birth-Parametric (D_4 pitchfork), `working/SF/symmetry_moduli.md` (Round 4 equivariant CR), `working/SF/mode_count.md` (Prop 1.3a/b spectral base).

---

## §1. 사용자 통찰의 정형화

### 1.1 사용자 논점 네 가지

> "오비탈적 특성을 보고싶다면 결국에 그것도 **확률분포로써 경계 흐릿 문제**도 있지만, 그것은 **모드로 구별이 가능**하고 **보이지 않는 상태를 보이게 만들기도 한다**. 이는 SCC와 연결되지만 **진짜로 연결되려면 오비탈처럼 다양한 모양이 특정되어야 하고 발견되어야 할 텐데**."

네 가지 논점으로 분해:

- **(P1)** 확률 분포 유비: atomic orbital은 sharp boundary가 아닌 continuous $|\psi|^2$. SCC의 $u$도 그렇다 (soft cohesion).
- **(P2)** Mode-identity robustness: boundary가 흐릿해도 **mode label은 이산**이고 robust.
- **(P3)** 보이지 않는 상태의 가시화: orbital 관점은 기존 관측 (classical density)이 놓치는 구조를 드러낸다.
- **(P4)** Substantive challenge: 진짜 연결이 되려면 **구체적 shape enumeration** + **실제 discovery**가 있어야.

본 파일은 이 네 논점을 **research program**으로 정형화.

---

## §2. 확률 분포 parallel 정형화 (P1)

### 2.1 Atomic orbital

Quantum mechanics:
- Wave function $\psi(\mathbf{r}, t) \in \mathbb{C}$, normalized $\int |\psi|^2 d^3r = 1$.
- Probability density $\rho(\mathbf{r}) := |\psi(\mathbf{r})|^2 \in [0, \infty)$ with $\int \rho = 1$.
- $\rho$는 **asymptotic exponential decay** — sharp boundary 없음.
- Orbital SHAPE: labels $(n, \ell, m)$. Radial factor + spherical harmonic $Y_{\ell m}$.
- $\rho$는 연속 scalar field; **orbital label은 이산**.

### 2.2 SCC cohesion field

Soft Cognitive Cohesion:
- Field $u : X \to [0, 1]$, constrained $\sum_i u_i = m$ (canonical §8.0).
- $u$는 **graded cohesion**, site-wise probability-like quantity (참여도).
- Interface is tanh-soft with width $\xi_0$ — sharp boundary 없음 (Cor 2.2 Cat A).
- 현재 canonical: continuous field $u$, discrete observable $K_{\mathrm{step}}$ (threshold count).
- **그러나** $K_{\mathrm{step}}$은 $\tau$-의존 (§07 §2.2) — intrinsic 이산 label 아님.

### 2.3 Parallel table

| 구조 | Quantum orbital | SCC cohesion |
|---|---|---|
| 연속 scalar 장 | $\rho = |\psi|^2 \in [0, \infty)$ | $u \in [0, 1]$ |
| 정규화 | $\int \rho = 1$ | $\sum u_i = m$ |
| Soft boundary | Exponential tails $\rho \sim e^{-r/a_0}$ | Sigmoid $u \sim \tanh(r/\xi_0)$ |
| 기저 방정식 | Schrödinger $H\psi = E\psi$ | Variational $\nabla\mathcal{E}(u) = 0$ (KKT) |
| 연산자 | $H = -\tfrac{\hbar^2}{2m}\nabla^2 + V$ | $H_1 = -4\alpha\Delta + \beta W''$ + cl_sep |
| 이산 label | $(n, \ell, m) \in \mathbb{Z} \times \{0,1,\ldots\} \times \{-\ell,\ldots,\ell\}$ | $(n, \ell)$ + orbital label per formation |
| **관측 가능 양** | Spectroscopy → $(n, \ell)$ 드러남 | ??? — 현재 $K_{\mathrm{step}}$만 사용, orbital 미사용 |

### 2.4 관측 gap

Quantum mechanics는 **spectroscopy**로 orbital label을 직접 관측 (photon emission at $E_{n\ell} - E_{n'\ell'}$). SCC는 현재 **$K_{\mathrm{step}}$에 갇혀** orbital label을 관측하지 않음.

**사용자 P3 (invisible made visible)의 의미**: SCC의 orbital label은 **이미 존재하지만 기존 observable로 보이지 않음**. 적절한 diagnostic을 구축하면 드러날 것.

---

## §3. Mode identity robustness (P2)

### 3.1 왜 이산 label이 연속 분포를 살아남는가

**Hydrogen atom**: 2p orbital과 3d orbital의 $|\psi|^2$은 **continuous smooth functions**. 둘 다 exponential tails. 그러나 각각 고유한:
- **Radial node 수**: 2p = 0, 3d = 0. 2s = 1.
- **Angular pattern**: s (spherical), p (dumbbell), d (four-lobe or donut).
- **에너지**: 2p는 3d보다 낮음.

이 세 구조적 특징은 **boundary blurring에 무관**. 노드 수, 대칭성, 에너지 — 모두 이산 / 위상적 / 대수적 불변량.

### 3.2 SCC에서의 유비

SCC formation $u^*$의 불변량:
- **Local max 수 ($\mathcal{F}$)** — 위상적, threshold-independent.
- **Angular symmetry** ($\mathrm{Aut}(G)$-orbit type of $u^*$) — 대수적, 이산.
- **Hessian index** (Morse index) — 정수.
- **Hessian eigenvalue ordering** — 이산 sequence.

이 네 가지가 SCC의 "quantum number" 역할. 각각 boundary blurring에 견디는 이산 label.

### 3.3 Claim (mode robustness)

> **Claim 3.1 (Mode identity robust to boundary blurring, Cat A structural)**: For any SCC minimizer $u^*$ on graph $G$, the quadruple
> $$\Lambda(u^*) = (\mathcal{F}(u^*),\ \Gamma\text{-orbit type},\ \mathrm{ind}(u^*),\ \{\lambda_n\}_{n=1}^N)$$
> is invariant under:
> (i) threshold choice $\tau \in (0, 1)$ — $\mathcal{F}$ is local-max count, $\tau$-independent.
> (ii) $\xi_0 \to 0$ limit — eigenvalue ordering preserved, index stable.
> (iii) Small perturbations of $u^*$ within basin — by continuity.
>
> $\Lambda$는 orbital label의 역할.

**Status**: Cat A structural (definitions + standard continuity).

### 3.4 "보이지 않는 상태" 식별

다음 SCC states는 $K_{\mathrm{step}}$로는 구별 안되지만 $\Lambda$로 구별됨:

**Example A**: c=0.5 2D torus β=30 R18 observation $K_{\mathrm{step}} = 1$.
- 후보 1: **1s ground state** — single disk formation, $\mathcal{F} = 1$, axial symmetry A_1.
- 후보 2: **stripe mode** — torus-winding stripe, $\mathcal{F} = 0$ (bounded field, no local max inside), different Γ-orbit type.
- 후보 3: **bilobed 2d orbital** with bridge above τ — $\mathcal{F} = 2$ at low τ, different Hessian spectrum.

세 모두 $K_{\mathrm{step}} = 1$로 보이나 $\Lambda$는 다름. **기존 observable은 이 셋을 구별 못함**.

**Example B**: R17 c=0.3 β=30 $K_{\mathrm{step}} = 7.76$.
- 후보 1: 7개 independent **1s formations** (classical multi-nucleation, Mechanism B).
- 후보 2: 1개 **4g orbital excited formation** pinched into 7 lobes (Mechanism A).
- 후보 3: Mixed — 일부 1s + 일부 orbital excited.

Again, $K_{\mathrm{step}}$만으로는 구별 불가.

### 3.5 Key hypothesis

> **Claim 3.2 (mode differentiation hypothesis, Cat C)**: The SCC landscape contains **distinct orbital states** with same $K_{\mathrm{step}}$ at τ=0.5 but different $\Lambda$. Current experiments (R17-R22) have not distinguished them because $K_{\mathrm{step}}$ is used as sole count observable.

---

## §4. Per-graph orbital enumeration

사용자 P4 ("진짜로 연결되려면 다양한 모양이 특정되어야"): 각 graph class에 대한 explicit orbital taxonomy.

### 4.1 2D square grid (free BC), $\Gamma = D_4$ (order 8)

$D_4$ irreducible representations:
- $A_1$ (trivial, 1D): $\chi(g) = 1$ for all $g$.
- $A_2$ (sign of rotation, 1D): $\chi(r) = 1$, $\chi(s) = -1$.
- $B_1$ (x-axis reflection, 1D): axis-aligned.
- $B_2$ (diagonal reflection, 1D): diagonal.
- $E$ (2D): dipole pair, hexapole pair, etc.

**Orbital shapes** (lowest energy per irrep):

| Label | Irrep | Shape | SCC realization |
|---|---|---|---|
| **1s** | $A_1$ | Single central blob, radially symmetric | Cor 2.2 tanh disk at domain center |
| **2p** | $E$ | Dipole pair (px, py) | Translated disk (broken on free-BC by $A_1$ 기준) |
| **3d$_{x^2-y^2}$** | $B_1$ | Axis-aligned elongation (prolate along x or y) | Elongated along lattice axis |
| **3d$_{xy}$** | $B_2$ | Diagonal elongation | Elongated along diagonal |
| **4f** | $E$ | Hexapole pair (three-lobe) | Three-lobed formation |
| **5g$_{x^4+y^4}$** | $A_1$ | Four-lobed tetrapole (axis-aligned) | Four lobes along axes |
| **5g$_{x^2 y^2}$** | $A_2$ | Four-lobed with sign (antisymm) | Alternating four-lobe |
| **5g$_{xy(x^2-y^2)}$** | $B_1$ or $B_2$ | Higher quadrupole | Complex |

**첫 secondary bifurcation** (R22 Round 10 Tree Structure의 첫 분기):
- 보통 $E$-irrep 통해 2p or 4f mode 활성화.
- Round 4 $\Phi_4$ ratio 분석 = cubic coefficient $A_2/A_1 \in \{2, 4\}$ 는 2D mode bifurcation structure.

### 4.2 2D torus ($T^2 = (\mathbb{Z}_L)^2$), $\Gamma = (\mathbb{Z}_L)^2 \rtimes D_4$

추가 (ℤ_L)² translation symmetry → Fourier-mode orbital:
- Momentum $\mathbf{k} = (k_1, k_2)/L$ labels.
- Stripe mode $\mathbf{k} = (1, 0)$: horizontal stripe.
- Diagonal stripe $\mathbf{k} = (1, 1)$.
- Checker $\mathbf{k} = (L/2, L/2)$ (if $L$ even).

| Label | Momentum | Shape on torus | SCC realization |
|---|---|---|---|
| **1s (torus)** | $(0, 0)$ | Uniform ($u \equiv c$) | Uniform state (unstable at $\beta > \beta_{\mathrm{crit}}$) |
| **$\mathbf{k}=(1,0)$ stripe** | (1,0) | Horizontal stripe, one period | First-excited mode |
| **$\mathbf{k}=(1,1)$ diagonal** | (1,1) | Diagonal stripe | |
| **$\mathbf{k}=(2,0)$ double stripe** | (2,0) | Two horizontal stripes | K_step=2 mode |
| **Disk orbital (local)** | — | Radially symmetric disk at specific location | If radius ≪ L/2 |

**R18 c=0.5 torus β=30 $K_{\mathrm{step}} = 1$ 재해석**:
- 1s (uniform): unstable at β=30 → 배제.
- $\mathbf{k}=(1,0)$ stripe: half-torus occupied as stripe → $K_{\mathrm{step}} = 1$ (torus wrap) → **plausible**.
- Disk: radius ≈ 12.8 on L=32 → occupies quarter; $K_{\mathrm{step}} = 1$ → plausible.

**Prediction (NQ-92 refined)**: Measure $\mathcal{F}$ at R18 u* — if it's a stripe, $\mathcal{F} = 0$ (no local max, just gradient); if it's a disk, $\mathcal{F} = 1$.

### 4.3 1D cycle $C_n$, $\Gamma = D_n$

Fourier modes: $\psi_k(x) = e^{2\pi i k x/n}$, $k \in \{-n/2, \ldots, n/2\}$.

Irreps:
- $A_1$ (trivial): $k = 0$.
- $A_2$ (sign): $k = n/2$ (if n even).
- $E_k$ (2D, $k \neq 0, n/2$): $(\cos(2\pi kx/n), \sin(2\pi kx/n))$ pair.

**Orbital shapes**:

| Label | Irrep | Mode | Pattern | Formation shape |
|---|---|---|---|---|
| **1s** | $A_1$ | k=0 | Uniform | Uniform (unstable at β > β_crit) |
| **2p** | $E_1$ | k=1 | One period sinusoid | Single-arc formation |
| **3d** | $E_2$ | k=2 | Two periods | Two-arc (K_step=2) |
| **4f** | $E_3$ | k=3 | Three periods | Three-arc |
| ... | ... | ... | ... | K_step = k arcs |

**중요**: 1D cycle에서 $K_{\mathrm{step}} = k$는 **mode index $k$와 1:1 대응**. 즉 1D cycle은 "orbital label = $K_{\mathrm{step}}$"이 성립 → 1D cycle은 orbital과 topological K가 일치하는 특수 경우.

**Empirical match**:
- R18 1D cycle c=0.5 β=30 $\widehat K = 56$: orbital $k=56$ mode 활성화. Many Fourier modes가 near-simultaneously 활성화.
- R19 c=0.7 β=30 $\widehat K = 45$: similar.

### 4.4 Complete graph $K_n$, $\Gamma = S_n$

$S_n$ irreps: trivial $(1)$ + standard $(n-1)$ + 더 high-dim irreps (예: (n-2)-dim partition, etc.).

**Orbital shapes**:

| Label | Irrep | Shape | Description |
|---|---|---|---|
| **1s** | trivial | $u \equiv c$ | Uniform |
| **2s-like** | standard | "one vertex high, rest low" | Indicator-type configuration |
| **3d-like** | higher partition | "two vertices high, rest low" | |
| **4f-like** | even higher | "three vertices high" | |

**$K_n$의 특수성**: 모든 critical point는 indicator-type (§05 §B.3.2). Orbital "shape"는 index partition type.

### 4.5 Tree graphs

Tree $T$ has $\Gamma$ = symmetric group of leaves (if balanced) 또는 trivial (asymmetric). Shape modes are highly localized on branches.

**Orbital shapes on balanced binary tree**:
- **1s**: formation on root.
- **2p**: formation on left or right subtree (2-dim irrep of tree symmetry).
- **3d**: formation on deeper branches (specific symmetry).

Tree's 1D-like connectivity → Fourier-like orbital structure, but strongly constrained by tree hierarchy.

### 4.6 SBM (Stochastic Block Model)

**Low-SNR SBM**: $\Gamma$ generically trivial (no automorphisms beyond within-block permutations).

**High-SNR SBM**: within-block permutations are automorphisms → $\Gamma = S_{k_1} \times \ldots \times S_{k_K}$ (permutations within each block).

**Orbital shapes**:
- **1s per-block**: formation on one block (restricted to $k_i$ sites).
- **2p block-pair**: formation on two blocks.
- **$K_{\mathrm{block}}$ multi-block**: formation = union of all blocks.

**Mode = block partition type**. Application EX-SBM-1 (from `A_application_scoping.md`) tests whether these modes are recoverable.

### 4.7 Cross-graph orbital summary

각 graph 별 "orbital zoo" 요약:

| Graph class | Symmetry | 특징 | 제일 쉬운 orbital probe |
|---|---|---|---|
| 2D sq free-BC | $D_4$ | s/p/d/f/g classical | 2d axis vs diag (R4 Φ_4 ratio) |
| 2D torus | $(\mathbb{Z}_L)^2 \rtimes D_4$ | Stripe modes | Wavelength-based |
| 1D cycle $C_n$ | $D_n$ | Fourier modes | k-index mode |
| $K_n$ complete | $S_n$ | Partition-type | "How many high?" |
| Tree | Branch-symmetry | Hierarchical | Subtree localization |
| SBM | Block permutation | Block-based | Block count / partition |
| Generic graph | $\{e\}$ | No reduction | Hessian eigenvector decomp only |

---

## §5. Discovery protocol

사용자 P4 ("발견되어야 할 텐데"): SCC simulation에서 실제로 orbital을 찾는 프로토콜.

### 5.1 Algorithm 5.1 — Orbital Signature from Minimizer

```python
def orbital_signature(u_star, graph, energy_computer, n_modes=30):
    """
    Extract orbital label from SCC minimizer u_star.
    Returns: dict with keys 'F' (local max count), 
                           'gamma_orbit' (Aut(G)-orbit type),
                           'morse_index' (Hessian index),
                           'eigenvalues' (top n_modes positive eigenvalues),
                           'angular_modes' (per-mode angular decomposition)
    """
    # Step 1: Local max count (topological, tau-independent)
    F = count_local_maxima(u_star, graph)
    
    # Step 2: Aut(G)-orbit identification
    gamma_orbit = identify_orbit_type(u_star, graph.automorphism_group)
    
    # Step 3: Constrained Hessian at u_star
    H = energy_computer.hessian_at(u_star, project_constraint=True)
    
    # Step 4: Eigendecomposition (smallest n_modes eigenvalues)
    eigvals, eigvecs = sparse.linalg.eigsh(H, k=n_modes, which='SM')
    
    # Step 5: Morse index
    morse_index = (eigvals < -1e-8).sum()
    
    # Step 6: Angular decomposition of each low-mode
    angular_modes = []
    for i in range(n_modes):
        mode = eigvecs[:, i]
        ell = fit_angular_multipole(mode, graph)  # dominant ell (0,1,2,...)
        n_rad = count_radial_nodes(mode, graph)
        angular_modes.append((n_rad, ell))
    
    return {
        'F': F,
        'gamma_orbit': gamma_orbit,
        'morse_index': morse_index,
        'eigenvalues': eigvals,
        'angular_modes': angular_modes,
        'orbital_label': classify_orbital(angular_modes)  # 1s, 2p, 2d, etc.
    }
```

### 5.2 Algorithm 5.2 — Mode-Seeded Minimizer Search

기존 gradient flow는 random / Fiedler-init으로 시작. Orbital-targeted search는:

```python
def search_orbital_minimizer(target_label, graph, params, n_trials=10):
    """
    Find local minimizer with specified orbital label (e.g. '2d_x2-y2').
    Uses mode-seeded initial conditions.
    """
    # Step 1: Generate initial conditions seeded by target mode's eigenfunction
    target_mode = get_mode_eigenfunction(target_label, graph)
    
    found_minimizers = []
    for trial in range(n_trials):
        eps = 0.01 + 0.05 * trial  # scan amplitude
        u_0 = graph.uniform_field(c) + eps * target_mode + small_noise
        
        u_star = gradient_flow(u_0, params, until_convergence=True)
        
        sig = orbital_signature(u_star, graph, params.energy)
        
        if sig['orbital_label'] == target_label:
            found_minimizers.append(u_star)
    
    return found_minimizers
```

### 5.3 Algorithm 5.3 — Bifurcation Cascade Tracer

Round 10 Tree Structure의 경험적 확장:

```python
def trace_bifurcation_cascade(graph, beta_range, c=0.5):
    """
    Track which orbital modes activate as beta increases.
    Returns cascade tree: (beta, from_label, to_label, branch_structure)
    """
    cascade = []
    
    # Start at beta_crit^{(2)} + eps, with 1s minimizer
    beta = find_beta_crit_2(graph, c) + 0.01
    u_star = find_1s_minimizer(graph, beta, c)
    
    while beta < beta_range[1]:
        sig = orbital_signature(u_star, graph, Energy(beta, c))
        
        # Find lowest positive eigenvalue
        lambda_min_pos = min(ev for ev in sig['eigenvalues'] if ev > 0)
        
        # Advance beta until this eigenvalue crosses zero
        beta_next = find_zero_crossing(u_star, beta, graph, lambda_min_pos)
        
        # At beta_next, secondary bifurcation occurs
        # Identify which mode went unstable
        unstable_mode = ...
        new_label = classify_bifurcation_mode(unstable_mode)
        
        cascade.append((beta_next, sig['orbital_label'], new_label))
        
        # Continue with new branch
        u_star = follow_branch(u_star, unstable_mode, beta_next + epsilon)
        beta = beta_next + epsilon
    
    return cascade
```

### 5.4 Discovery experiment design

**Experiment EX-Orbital-1**: 2D sq grid L=32, c=0.5, β-scan. Execute Algorithm 5.3. Expected discovery:
- $\beta_c^{(2)}$: 1s emerges.
- $\beta_{\mathrm{sec}}^{1s \to 2d_{x^2-y^2}}$: 2d axis mode.
- $\beta_{\mathrm{sec}}^{2d \to 3d}$ or higher: cascade.

**Expected pattern**: sequence of discrete orbital labels with bifurcation points, forming a tree.

**Experiment EX-Orbital-2**: 2D sq grid + various $c$. Compare orbital cascade structure across $c$ regimes.

**Experiment EX-Orbital-3**: R22 V7 P3 setup (β=9, 1D cycle c=0.7, 200 seeds). For each seed, compute orbital signature. Hypothesis: Gaussian $\widehat K = 13 \pm 1.5$ distribution corresponds to $k=13$ mode activation with noise-induced mixing between $k \in \{11, 12, 13, 14, 15\}$.

### 5.5 What discovery looks like

"Discovery" = **identifying a specific orbital with specific (n, ℓ) label, appearing in specific parameter regime, with specific basin volume, in SCC simulation**.

**Success criterion for orbital-theory validation**:
1. Computed orbital cascade reproduces Round 10 Tree Structure.
2. Mode-seeded search finds minimizers with predicted labels.
3. Bifurcation points $\beta_{\mathrm{sec}}$ match theoretical predictions from equivariant CR.
4. Diagnostic $\Lambda(u^*)$ distinguishes between 1s and excited-orbital K_step=1 states.

**Failure mode**: Mode-seeded search fails to converge to target orbital; or minimizers have no consistent orbital structure.

### 5.6 What's needed before execution

- Implement `orbital_signature` in `scc/diagnostics.py`.
- Implement `find_angular_multipole` — angular decomposition on graph.
- Implement `classify_orbital` — rule-based $(n, \ell)$ labeling.
- Write `CODE/experiments/exp_orbital_cascade.py`.

**Status**: plan.md non-goals: no experiment execution today. But implementation plan is **concretely specified** for next session.

---

## §6. "Invisible made visible" — what exactly

### 6.1 SCC's invisible structure (currently)

기존 observables가 놓치는 것:

- **$\mathcal{F}$ (local max count)**: 측정된 적 없음; distinguishes bilobed K_step=1 from true 1s.
- **Γ-orbit type**: 측정된 적 없음; distinguishes axis-aligned 2d from diagonal 2d (R4's $\Phi_4$ ratio는 이를 이론적으로 구별했으나 실험적 식별 아직).
- **Hessian eigenmode angular decomposition**: 측정된 적 없음; gives $(n, \ell)$ label.
- **Stable branch orbital label along parameter curve**: 측정된 적 없음; traces which orbital the basin follows.

### 6.2 Gaining visibility

Each item in §6.1 has a diagnostic in §5.1 Algorithm. 구현하면 이 네 quantity가 관측 가능해짐.

**"Invisible made visible"의 SCC 번역**:
- 기존 $K_{\mathrm{step}}$만으로 구별 불가능한 상태 (§3.4 Examples A, B)
- Orbital signature $\Lambda$로 구별 가능해짐.

### 6.3 Predicted discoveries

구현 이후 예상 발견:

1. **R18 c=0.5 torus K_step=1 → 실제로 stripe mode**, not disk.
2. **R17 c=0.3 K_step=7.76 → 7 independent 1s formations** (Mechanism B), **not** orbital-excited single formation.
3. **V7 P3 Gaussian K=13 → orbital excitation mixing** around dominant mode.

*(These are predictions, to be verified.)*

---

## §7. 진짜 연결 vs metaphor — 판단 기준

### 7.1 Metaphor 단계 (현재)

- Orbital 유비가 **conceptually suggestive**.
- Hessian eigenbasis = orbital basis (Cat A structural).
- Round 4, Round 10의 bifurcation이 orbital 언어로 재해석 가능.
- 구체적 shape enumeration (§4) + Discovery protocol (§5) 제공됨.

### 7.2 Substantive 단계 요건

- Algorithm 5.1-5.3 구현 + `exp_orbital_cascade.py` 실행.
- Specific orbital minimizer의 empirical confirmation.
- Bifurcation cascade tree 실측.
- Mode-seeded search의 reproducibility.

### 7.3 Falsification 단계

다음이 **관측되면 orbital hypothesis 반증**:
- Mode-seeded search가 consistently fail (mode 없음).
- Bifurcation cascade가 trivial (한번 bifurcate 후 additional modes 활성화 안 됨).
- $\mathcal{F}$ 항상 $= K_{\mathrm{step}}$ (orbital structure absent).

### 7.4 현재 수준

**Cat A**: Hessian eigenbasis의 존재 (basic linear algebra).
**Cat B**: Orbital labels $(n, \ell)$이 Hessian 고유모드에 대응 (§07 §4.5).
**Cat C**: Specific per-graph orbital taxonomy (§4).
**Conjecture**: "K_step > 1 appearances are sometimes orbital-excited K_step=1" (§07 §5.4, §6.5).

**진짜 연결 완성**: Discovery program 실행 후 (NQ-98 이하).

---

## §8. Canonical merge impact

### 8.1 새 section 제안: canonical §6.S1'+ §6.OR

- §6.S1': Orbital-Augmented Formation Quantization (from §07 §12).
- **§6.OR (new)**: Orbital Mode Classification. Per-graph-class orbital enumeration (§4 this file).

### 8.2 Modification to Layer classification (§SF_layer)

Layer 2a → explicit orbital label table per graph class (from §4).

### 8.3 Revision to working file proposals

- `working/SF/orbital_modes.md` (신규 from §07).
- `working/SF/orbital_enumeration.md` (신규 from §4 this file — per-graph table).
- `working/SF/orbital_discovery_protocol.md` (신규 from §5 — algorithm specification).

---

## §9. New NQ from this file

- **NQ-98**: Implement `orbital_signature(u_star, graph)` in `scc/diagnostics.py`.
- **NQ-99**: Implement `classify_orbital` — rule-based $(n, \ell)$ labeling on graph.
- **NQ-100**: Execute EX-Orbital-1 (2D sq β-scan cascade).
- **NQ-101**: Execute EX-Orbital-2 (c-scan across regimes).
- **NQ-102**: Execute EX-Orbital-3 (V7 P3 re-analysis).
- **NQ-103**: Per-graph orbital cascade database — 5 graph classes × 3 $(c, \sigma_0)$ regimes = 15 entries.
- **NQ-104**: Mode-seeded search convergence criteria (when does Algorithm 5.2 succeed?).
- **NQ-105**: Empirical vs theoretical bifurcation point agreement (quantitative).

**Total this file**: 8 new NQ (NQ-98..NQ-105).

**Cumulative 2026-04-23**: 25 + 8 + 5 + 8 + 6 + 8 = **60 new NQ**.

---

## §10. Strategic recommendation

사용자 P4 요구 (진짜 연결 위해 specific shape 발견)를 충족하려면:

**Priority sequence**:
1. **NQ-98 + NQ-99** (diagnostic implementation) — 1-2 sessions.
2. **NQ-100** (2D sq cascade experiment) — 1 session.
3. **NQ-102** (V7 P3 re-analysis) — 1 session (smallest-scale, immediate).
4. **NQ-101, NQ-103** (systematic scan) — 2-3 sessions.

**Critical insight**: Without experimental execution, orbital theory stays metaphorical. NQ-98..NQ-102가 commit되면 orbital 이론이 Cat A empirical foundation을 가지게 됨.

**Timeline proposal**: 2026-04-24 Stage 2 Axiom Audit **대신** (or in parallel), execute NQ-98+NQ-102 orbital discovery. Payoff: Formation Quantization 개정 (S1 → S1') + Layer 2a 확립.

---

## §11. File status

- **User P1 (probability distribution parallel)**: 정형화 완료 (§2).
- **User P2 (mode-identity robust)**: Claim 3.1 Cat A (§3.3).
- **User P3 (invisible made visible)**: 구체적 예시 (§3.4, §6) + $\Lambda(u^*)$ diagnostic 제안.
- **User P4 (substantive connection)**: per-graph orbital enumeration (§4) + Discovery protocol (§5) + 실행 priority (§10).
- **New NQ**: 8 (NQ-98..NQ-105). 누적 60.
- **Intended promotion**: 세 개 신규 working file — `orbital_modes.md`, `orbital_enumeration.md`, `orbital_discovery_protocol.md`.

**End of 08_orbital_discovery_program.md.**
