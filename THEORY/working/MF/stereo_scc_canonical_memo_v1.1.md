> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q4_K_selection]] · [[MOC_sigma_rich_framework]] · [[THEORY_INDEX]]

# stereo_scc_canonical_memo_v1.1.md
# Canonical Memo: SCC-Stereo Soft-to-Crisp Stabilization Framework

**Version:** v1.1 (2026-05-07)
**Status:** Working-level reference memo. Cat C throughout. Not a canonical promotion.
**Scope:** Establishes precise definitions, working theorems, and re-placement table for the
  SCC-stereo integration framework. Supersedes v1 (produced in conversation 2026-05-06/07).
**Promotion target:** Feeds OP-0005 (Commitment 19 candidate), OP-0008, OP-0009-Pre amendments
  at CV-1.7+ / v2.0.

---

## §1. Research Direction

**"Given a continuous soft cohesion field, how do discrete crisp formations emerge, persist, and
stabilize — and how does stereo geometry condition this process?"**

Three interlocking directions:

| Direction | Map | Description |
|---|---|---|
| Generative | $\mathcal{X}_t \to \mathfrak{O}_t$ | Latent scene → observations (stereo images + disparity) |
| Inference | $\mathfrak{O}_t \to \rho_t$ | Observations → belief posterior over $\tilde{u}_t$ |
| Coarse-graining | $\tilde{u}_t \to K_\mathrm{act}$ | Soft field → formation count (adiabatic reduction) |

The coarse-graining direction is the core new direction. The generative and inference directions
provide the observation layer that conditions the SCC energy landscape.

---

## §2. Core Definitions (D1–D10)

### D1: Graph structure of $\mathcal{P}_t$

$$\mathcal{G}_t^P = (V_t, E_t, w_t, \mu_t)$$

- $V_t = \mathcal{P}_t$ — finite 3D point cloud from stereo disparity at time $t$
- $E_t$ — depth-filtered adjacency: $(b_t(x), b_t(y)) \in E_t$ iff $(x,y) \in E_t^{2D}$ and
  $|z(x) - z(y)| < \delta_z$ (depth threshold)
- $w_t : E_t \to \mathbb{R}_{>0}$ — edge weights encoding 3D distance and depth discontinuity
- $\mu_t : V_t \to \mathbb{R}_{>0}$ — vertex measure (e.g. uniform or confidence-weighted)

**Why $\mathcal{G}_t^P$ conditions everything:** The SCC energy $\mathcal{E}_\mathrm{SCC}[\tilde{u};\mathcal{P}_t]$
uses the Laplacian of $\mathcal{G}_t^P$ in all four energy terms. Changing $\mathcal{P}_t$
(scene/camera motion) changes the energy landscape and hence all basin boundaries, barriers, and
$K_\mathrm{act}$.

### D2: Field hierarchy

**Latent primitive:** $U_t : \mathcal{M}_t \to [0,1]$ on 3D manifold $\mathcal{M}_t$

**Visible working field:** $\tilde{u}_t = U_t|_{\mathcal{P}_t} \in \mathcal{F}_0(\mathcal{P}_t)$

*Distinction matters:* $U_t$ and $\tilde{u}_t$ are not the same object. $\tilde{u}_t$ is the
restriction of $U_t$ to the observed point cloud — not a separate field. Conflating them (writing
$\tilde{u}_t : \mathcal{M}_t \to [0,1]$) is an error; $\tilde{u}_t$ lives on $\mathcal{P}_t$ only.

### D3: Base field spaces

$$\mathcal{F}_0(\mathcal{P}) = \{\tilde{u} : \mathcal{P} \to [0,1]\}$$

Mass-constrained variant:

$$\mathcal{F}_M(\mathcal{P}) = \{\tilde{u} \in \mathcal{F}_0(\mathcal{P}) : \textstyle\sum_{x \in \mathcal{P}} \tilde{u}(x) \mu(x) = M\}$$

$\mathcal{F}_M(\mathcal{P})$ is the correct foundational state space in which SCC energy is
defined and gradient flow operates. It is NOT the same as $\Sigma_M^K$ (see D5 correction note).

### D4: $K_\mathrm{act}$ — persistent connected components

$$K_\mathrm{act}(\tilde{u}) := \#\mathrm{PersComp}(\tilde{u})$$

**Precise definition:** apply threshold filtration $\{\tilde{u} > \theta\}$ for $\theta$ decreasing
from 1 to 0; count connected components of $\mathcal{G}^P$ restricted to the superlevel set;
keep only components with persistence $> \rho_\mathrm{pers}$ (born at $\theta = b$, die at
$\theta = d$; persistence $= b - d > \rho_\mathrm{pers}$).

**NOT** $|\{j : \|\tilde{u}^{(j)}\|_\infty > \varepsilon\}|$ — that is a K-field architecture
artifact (slot-counting). The slot-count is a proxy valid only within $\mathcal{A}_{K,\alpha}$
when slots are fully activated and well-separated.

**Gauge note:** $\rho_\mathrm{pers}$ alone is insufficient for gauge/scale robustness. Full
robustness requires an admissible family $\mathcal{G} \times \mathcal{B}$ (gauge × scale
transforms) under which $K_\mathrm{act}$ is stable. $\rho_\mathrm{pers}$ is only the
filtration threshold parameter; it does not control all sources of instability.

### D5: Topological sector

$$\mathcal{B}_K(\mathcal{P}) := \{\tilde{u} \in \mathcal{F}_0(\mathcal{P}) : K_\mathrm{act}(\tilde{u}) = K\}$$

This is the **topological sector** for formation count $K$. It is an open subset of
$\mathcal{F}_0(\mathcal{P})$ (boundaries are where $K_\mathrm{act}$ is undefined — at merge/birth
events).

**Relationship to $\Sigma_M^K$:** $\Sigma_M^K = \Sigma_{m_1} \times \cdots \times \Sigma_{m_K}$
is a *local coordinate chart* for one energy basin $\mathcal{A}_{K,\alpha}(\mathcal{P}) \subset
\mathcal{B}_K(\mathcal{P})$. It is NOT the topological sector itself. See D6.

### D6: Energy basins and their relationship to $\mathcal{B}_K$

$$\mathcal{A}_{K,\alpha}(\mathcal{P}) := \text{basin of attraction of the } \alpha\text{-th local minimum of } \mathcal{E}_\mathrm{SCC}[\cdot;\mathcal{P}] \text{ within } \mathcal{B}_K(\mathcal{P})$$

Key inequality:
$$\mathcal{A}_{K,\alpha}(\mathcal{P}) \subsetneq \mathcal{B}_K(\mathcal{P}) = \bigsqcup_\alpha \mathcal{A}_{K,\alpha}(\mathcal{P}) \cup \text{(measure-zero inter-basin boundaries)}$$

A topological sector $\mathcal{B}_K$ can contain **multiple** energy basins (multiple local minima
with $K_\mathrm{act} = K$). Confusing $\mathcal{B}_K$ with a single $\mathcal{A}_{K,\alpha}$ is
an error.

$\Sigma_M^K$ (K-field product manifold) is a convenient local coordinate chart *within*
$\mathcal{A}_{K,\alpha}$ — valid when K-jumps are suppressed and the basin is approximately
product-shaped. It is a modeling-layer choice, not the foundational state space.

### D7: Partition function and multi-basin decomposition

$$Z_K(\mathcal{P}) = \int_{\mathcal{B}_K(\mathcal{P})} \exp\!\left(-\frac{\mathcal{E}_\mathrm{SCC}[\tilde{u};\mathcal{P}]}{T}\right) \mathcal{D}\tilde{u}$$

**Multi-basin decomposition** (critical — single basin is wrong):

$$Z_K(\mathcal{P}) = \sum_\alpha Z_{K,\alpha}(\mathcal{P}), \qquad Z_{K,\alpha}(\mathcal{P}) = \int_{\mathcal{A}_{K,\alpha}(\mathcal{P})} \exp\!\left(-\frac{\mathcal{E}}{T}\right) \mathcal{D}\tilde{u}$$

Integrating over a single basin $\mathcal{A}_{K,\alpha}$ gives $Z_{K,\alpha}$; the full sector
partition function sums over all basins. The Laplace approximation of $Z_{K,\alpha}$ gives the
Hessian-determinant entropy (see `stereo_observation_framework.md` §7.1).

**P-F flag:** $T$ (temperature / noise scale) is undefined until a stochastic extension of SCC
dynamics is canonically formalized (P-F-A1 Langevin on $\mathcal{F}_M(\mathcal{P})$). All
quantitative claims about $Z_K$ are P-F flagged.

**Effective free energy:**

$$F(K;\mathcal{P}) = -T \log Z_K(\mathcal{P})$$

Note: $F(K;\mathcal{P})$ is **P-conditioned** — the graph structure $\mathcal{G}^P$ enters via
the energy $\mathcal{E}_\mathrm{SCC}[\cdot;\mathcal{P}]$.

### D8: Observation layer

$$\mathfrak{O}_t = (X_L,\, X_R,\, f_L,\, f_R,\, \Pi_{LR},\, \delta,\, z,\, c)$$

- $X_L, X_R$ — left/right pixel grids
- $f_L : X_L \to \mathbb{R}^3$, $f_R : X_R \to \mathbb{R}^3$ — appearance fields (RGB/feature)
- $\Pi_{LR} : X_L \rightharpoonup X_R$ — epipolar stereo correspondence (**partial** map;
  undefined at occlusions and matching failures; **sub-stochastic / unbalanced coupling**,
  NOT doubly stochastic)
- $\delta : X_L \to \mathbb{R}_{>0}$ — disparity
- $z(x_L) = f_\mathrm{cam} \cdot b / \delta(x_L)$ — depth
- $c : X_L \to [0,1]$ — disparity confidence

$M_{t \to s} : \mathcal{P}_t \rightharpoonup \mathcal{P}_s$ (temporal transport) is structurally
analogous to $\Pi_{LR}$ — both are **partial / unbalanced** couplings (occlusion,
partial visibility → source measure $\neq$ target measure; NOT doubly stochastic).

### D9: Backprojection and pullback

**Backprojection** (partial map from pixel grid to 3D point cloud):

$$b_t : X_L^\mathrm{valid} \rightharpoonup \mathcal{P}_t, \qquad b_t(x_L) = z(x_L)\, K_\mathrm{cam}^{-1} \begin{pmatrix} u_L \\ v_L \\ 1 \end{pmatrix}$$

defined for $x_L$ with $c(x_L) > 0$ (valid stereo match). Undefined at occluded pixels.

**Pullback** (pixel-level cohesion):

$$u_L^\mathrm{pix}(x_L) = (b_t^*\tilde{u}_t)(x_L) = \tilde{u}_t(b_t(x_L)), \quad x_L \in \mathrm{dom}(b_t)$$

This preserves pixel-level correspondence — it does NOT discard $\Pi_{LR}$. The full observation
tuple at pixel $x_L$ is:

$$\Phi(x_L) = \bigl(f_L(x_L),\; f_R(\Pi_{LR}(x_L)),\; z(x_L),\; c(x_L),\; \tilde{u}_t(b_t(x_L))\bigr)$$

### D10: Three directions (summary)

```
GENERATIVE:       X_t  →  O_t              [latent scene → stereo observation]
INFERENCE:        O_t  →  ρ_t              [MAP: ũ* = argmin(E_SCC + L_obs)]
COARSE-GRAINING:  ũ_t  →  K_act(t)         [PersComp → effective Markov chain]
```

The three directions are logically orthogonal:
- Generative is about what $U_t$ produces
- Inference is about estimating $\tilde{u}_t$ from $\mathfrak{O}_t$
- Coarse-graining is about compressing $\tilde{u}_t$ to an integer

---

## §3. Working Theorems (Cat C — not canonical claims)

### T1: Topological sector partition

$$\mathcal{F}_0(\mathcal{P}) = \bigsqcup_{K=0}^{\infty} \mathcal{B}_K(\mathcal{P}) \cup \partial$$

where $\partial$ (the boundaries between sectors) has measure zero under $\mathcal{D}\tilde{u}$.

*Status:* follows from continuity of the persistence diagram as a function of $\tilde{u}$;
codimension-1 boundaries are at configurations where two persistence bars merge.

### T2: Born-Oppenheimer adiabatic reduction

Under the timescale hierarchy

$$\tau_\mathrm{frame} \ll \tau_\mathrm{fast} \ll \tau_{\mathcal{P}} \lesssim \tau_\mathrm{slow}$$

($\tau_\mathrm{fast}$ = intra-basin SCC relaxation; $\tau_{\mathcal{P}}$ = point cloud change;
$\tau_\mathrm{slow}$ = Kramers K-jump time), the dynamics of $K_\mathrm{act}(t)$ reduces to an
effective continuous-time Markov jump process:

$$\frac{d}{dt} P(K,t) = \sum_{K'} \Gamma^{K' \to K}(\mathcal{P}_t) P(K',t) - \Gamma^{K \to \cdot}(\mathcal{P}_t) P(K,t)$$

The time-varying $\mathcal{P}_t$ makes this non-autonomous.

*Status:* Cat C sketch. Requires (a) well-defined stochastic SCC on $\mathcal{F}_M(\mathcal{P})$
(P-F-A1); (b) time-scale separation verification for specific $\mathcal{P}$ instances.

**P-F flag on all quantitative claims.**

### T3: Partition function multi-basin decomposition

$$Z_K(\mathcal{P}) = \sum_{\alpha=1}^{n_K(\mathcal{P})} Z_{K,\alpha}(\mathcal{P})$$

where $n_K(\mathcal{P})$ = number of local minima of $\mathcal{E}_\mathrm{SCC}[\cdot;\mathcal{P}]$
within $\mathcal{B}_K(\mathcal{P})$.

*Correction from v1:* v1 wrote $Z_K = \int_{\mathcal{A}_K(\mathcal{P})} \exp(-\mathcal{E}/T) \mathcal{D}\tilde{u}$
(single basin $\mathcal{A}_K$). This is wrong when $\mathcal{B}_K$ contains multiple basins.
Correct integration domain is $\mathcal{B}_K(\mathcal{P})$ (full topological sector), decomposed
as $\sum_\alpha Z_{K,\alpha}$.

### T4: Prior/likelihood separation (MAP inference)

$$\tilde{u}_t^* = \arg\min_{\tilde{u} \in \mathcal{F}_M(\mathcal{P}_t)} \bigl[\underbrace{\mathcal{E}_\mathrm{SCC}[\tilde{u};\mathcal{P}_t]}_{\text{SCC prior}} + \underbrace{\mathcal{L}_\mathrm{obs}[\mathfrak{O}_t \mid \tilde{u}]}_{\text{observation likelihood}}\bigr]$$

where:
- $\mathcal{E}_\mathrm{SCC} = \lambda_\mathrm{cl} E_\mathrm{cl} + \lambda_\mathrm{sep} E_\mathrm{sep} + \lambda_\mathrm{bd} E_\mathrm{bd} + \lambda_\mathrm{tr} E_\mathrm{tr}$ (exactly 4 terms, CN5)
- $\mathcal{L}_\mathrm{obs}[\mathfrak{O}_t | \tilde{u}] = \lambda_\mathrm{photo} \sum_{x_L} c(x_L) \cdot \Psi(f_L(x_L), f_R(\Pi_{LR}(x_L)), \tilde{u}_t(b_t(x_L)))$

$E_\mathrm{photo}$ (photometric consistency) is in $\mathcal{L}_\mathrm{obs}$ — the **likelihood** —
NOT in $\mathcal{E}_\mathrm{SCC}$. Adding it to the prior would violate CN5 (5th energy term
with qualitatively different role). This is the only CN5-compliant placement.

### T5: Stereo geometry raises merger barriers (split: T-ST-5a Cat A + T-ST-5b Cat B)

**T-ST-5a (Cat A — W6 D4 Session E):** Hard-cut topological locking. If depth threshold removes all bridge edges ($G^P = G_1 \sqcup G_2$, disconnected), K=2 is topologically locked — barrier = +∞. No P-F flag.

**T-ST-5b (Cat B — formally signed off W6 D4 Session G):** Smooth barrier raising under full SCC energy. For smooth depth-weighted adjacency ($w_{ij} = w_{2D} \cdot \exp(-\lambda_z|z_i - z_j|^2)$), the K=2→K=1 merger barrier exceeds the flat-adjacency baseline **under full SCC energy (E_cl + E_sep active).** GL-only energy is NULL. Monotone dependence on $\Delta z$ is NOT confirmed.

*Original claim text (superseded):* "increases with $\Delta z_{jk}$" — monotonicity is NOT established by exp02e (barrier plateaus from $\Delta z=0.5$ at $\beta=10$; non-monotone at $\beta=20$).

*Mechanism (T-ST-5b):* smooth adjacency modifies the closure energy ($\alpha \cdot \tilde{u}^T L_{\mathrm{smooth}} \tilde{u}$), reducing cross-region cohesive pull and raising the merger cost. Effect absent for GL-only. Hard-cut (T-ST-5a) involves depth-filtered adjacency removing bridge edges; formation merger requires crossing zero-weight edges, incurring infinite cost.

*Warning:* T-ST-5b is NOT a universal theorem. Applies only under: (1) full SCC energy; (2) intermediate β (~10); (3) smooth depth-weighted adjacency.

*Status:* T-ST-5a **Cat A**. T-ST-5b **Cat B**. Cat A for T-ST-5b requires: monotonicity sweep + analytical lower bound on barrier gap. P-F flag for Kramers interpretation. Empirical: exp02e (Session F) — see `CODE/experiments/results/exp02e_single_field_neb_summary.md`.

---

## §4. Corrected OP Placements

| OP | Correct framing | Common error | Source |
|---|---|---|---|
| **OP-0006** | **Boundary precision**: how does soft transition zone of $\tilde{u}$ become crisp/persistent boundary? | ~~K-dynamics (how K changes)~~ | theorem_status.md OP-0006 |
| **OP-0008** | $\sigma^A$ K-jump inheritance: post-merger $\sigma^A(t^{*+})$ is non-deterministic in $\sigma^A(t^{*-})$ alone; requires merger geometry data | ~~deterministic σ-inheritance~~ | theorem_status.md OP-0008 |
| **OP-0009-Pre** | K-field architecture tension with pre-objecthood; G3.2 quotient addresses labeling *within* K-field local chart only; foundational issue remains | ~~G3.2 substantially resolves OP-0009-Pre~~ | `pre_objective_K_field_tension.md` |
| **OP-0005** | K-selection: thermodynamic ($F(K;\mathcal{P})$ minimum), kinetic (Kramers $\Gamma^{K \to K'}(\mathcal{P})$), numerical anchor, Commitment 16 cap — all four layers needed | ~~single mechanism suffices~~ | `k_selection_mechanism.md` |

---

## §5. Existing Theory Re-placement Table

| Concept | New placement | What it is NOT | Consequence |
|---|---|---|---|
| $\Sigma_M^K$ | Local coordinate chart of $\mathcal{A}_{K,\alpha}(\mathcal{P})$ | Foundational SCC state space | Free energy, Z_K, BO reduction all operate on $\mathcal{B}_K(\mathcal{P})$ not $\Sigma_M^K$ |
| G3.2 quotient $\widetilde{\widetilde\Sigma}^K_M$ | Removes labeling redundancy *within* K-field local chart | Resolution of OP-0009-Pre at foundational level | Pre-objecthood tension with K-field architecture still open |
| K_act slot-count | K-field architecture artifact, valid proxy within well-separated regime | Correct definition of $K_\mathrm{act}$ | Correct definition: $K_\mathrm{act} = \#\mathrm{PersComp}(\tilde{u})$ |
| $E_\mathrm{photo}$ | Observation likelihood $\mathcal{L}_\mathrm{obs}[\mathfrak{O}_t \mid \tilde{u}]$ | 5th SCC prior energy term | CN5 (4-term independence) preserved strictly |
| $\Pi_{LR}$, $M_{t \to s}$ | Partial/unbalanced optimal transport couplings | Doubly stochastic couplings | Occlusion and partial visibility → sub-stochastic source/target mass |
| $\rho_\mathrm{pers}$ | One parameter of persistence filtration threshold | Sufficient control for $K_\mathrm{act}$ gauge robustness | Full robustness requires admissible $\mathcal{G} \times \mathcal{B}$ family |

---

## §6. Timescale Hierarchy

| Scale | Symbol | Typical | Process |
|---|---|---|---|
| Camera frame | $\tau_\mathrm{frame}$ | 33 ms (30 fps) | Image acquisition |
| SCC intra-basin | $\tau_\mathrm{fast}$ | $\ll \tau_{\mathcal{P}}$ | Gradient flow of $\tilde{u}$ within $\mathcal{A}_{K,\alpha}$ |
| Point cloud change | $\tau_{\mathcal{P}}$ | 100 ms – 1 s | Scene / camera motion |
| K-jump (Kramers) | $\tau_\mathrm{slow}$ | $\tau_0 e^{\Delta\mathcal{E}/T}$ | Formation merger/birth |

Ordering: $\tau_\mathrm{frame} \ll \tau_\mathrm{fast} \ll \tau_{\mathcal{P}} \lesssim \tau_\mathrm{slow}$

BO condition: $\tau_\mathrm{fast} \ll \tau_{\mathcal{P}}$ — $\tilde{u}$ equilibrates within a
K-basin before $\mathcal{P}$ changes.

---

## §7. Hard Constraint Verification

- [x] **$u_t$ primitive**: $\tilde{u}_t$ (= $U_t|_{\mathcal{P}_t}$) is primitive throughout. $K_\mathrm{act}$ derived.
- [x] **CN5**: prior has exactly 4 energy terms; $E_\mathrm{photo}$ in likelihood only.
- [x] **CN10 contrastive**: stereo correspondence, depth estimation, etc. are upstream inputs; SCC is not identified with them.
- [x] **P-F flagged**: all stochastic claims (T2, T3, Kramers rates, $Z_K$) carry P-F flags.
- [x] **OP not silently resolved**: OP-0005 OPEN; OP-0006 OPEN; OP-0008 OPEN; OP-0009-Pre OPEN.
- [x] **No new canonical claims**: all T1–T5 are working-level, Cat C.

---

## §8. Open Problems (Specific to This Framework)

| Label | Problem | Status |
|---|---|---|
| OQ-1 | Measure $\mathcal{D}\tilde{u}$ on $\mathcal{F}_M(\mathcal{P})$ — Riemannian volume form? flat measure? | Open; affects $Z_K$ quantitatively |
| OQ-2 | Persistence threshold $\rho_\mathrm{pers}$ — how to calibrate from $\mathcal{G}^P$ geometry? | Open; gauge stability question |
| OQ-3 | Multi-basin count $n_K(\mathcal{P})$ — how does it depend on $\mathcal{P}$? | Open; topology of $\mathcal{B}_K(\mathcal{P})$ |
| OQ-4 | Allen-Cahn coarsening exponent on $S_t \subset \mathbb{R}^3$ — V4 $t^{1.315}$ vs $t^{4/3}$ | Open; see `k_selection_b_kramers.md` §7.4 |
| OQ-5 | Admissible gauge-scale family $\mathcal{G} \times \mathcal{B}$ — explicit characterization | Open; affects $K_\mathrm{act}$ robustness |

---

## §9. Summary Architecture Diagram

```
Latent:  U_t : M_t → [0,1]         (primitive; not directly observable)
               ↓ restriction to P_t
Working: ũ_t : P_t → [0,1]          (F_0(P_t), base field space)
               ↓ SCC energy
Energy:  E_SCC[ũ;P_t] = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd + λ_tr E_tr
               ↓ gradient flow
K-basins: B_K(P_t) = {ũ: K_act(ũ)=K}   [topological sector]
          A_{K,α}(P_t) ⊂ B_K           [energy basin, multiple α per K]
               ↓ BO adiabatic elimination (τ_fast ≪ τ_P)
Slow var: K_act(t) ∈ {0,1,...,K_field}  [effective Markov chain]

Observation layer (external to SCC prior):
  O_t = (X_L, X_R, f_L, f_R, Π_LR, δ, z, c)
  b_t: X_L^valid ⇀ P_t          [backprojection]
  u_L^pix(x) = ũ_t(b_t(x))     [pullback to pixels]
  MAP: ũ* = argmin [E_SCC + L_obs]   [L_obs = photometric likelihood, NOT 5th prior term]
```

---

## §10. Change Log v1 → v1.1

Nine corrections applied:

| # | Item | v1 error | v1.1 correction |
|---|---|---|---|
| 1 | K_act definition | Slot-count $|\{j: \|u^{(j)}\|_\infty > \varepsilon\}|$ | $K_\mathrm{act}(\tilde{u}) = \#\mathrm{PersComp}(\tilde{u})$ via persistence filtration |
| 2 | OP-0006 | K-dynamics (how K changes) | Boundary precision (how soft $\tilde{u}$ transition → crisp persistent boundary) |
| 3 | Field notation | $\tilde{u}_t = U_t$ (conflation) | $\tilde{u}_t = U_t|_{\mathcal{P}_t}$ (restriction of latent $U_t$ to $\mathcal{P}_t$) |
| 4 | Pixel-P_t | Ambiguous $b_L$ domain | $b_t: X_L^\mathrm{valid} \rightharpoonup \mathcal{P}_t$ (partial map; undefined at occlusions) |
| 5 | Gauge/scale | $\rho_\mathrm{pers}$ controls robustness | $\rho_\mathrm{pers}$ = filtration threshold only; full robustness requires admissible $\mathcal{G} \times \mathcal{B}$ family |
| 6 | $\Pi_{LR}$, $M_{t \to s}$ | Doubly stochastic / general transport | Unbalanced partial couplings (sub-stochastic; source ≠ target measure) |
| 7 | $E_\mathrm{photo}$ | 5th SCC prior energy term | Observation likelihood $\mathcal{L}_\mathrm{obs}[\mathfrak{O}_t \mid \tilde{u}]$; CN5 preserved |
| 8 | G3.2 quotient | Substantially resolves OP-0009-Pre | Removes labeling within K-field local chart only; pre-objective tension at foundational level unresolved |
| 9 | $Z_K$ domain | $\int_{\mathcal{A}_K} \cdots$ (single basin) | $\int_{\mathcal{B}_K(\mathcal{P})} \cdots = \sum_\alpha Z_{K,\alpha}$ (full sector, multi-basin) |

---

## §11. Monocular Degeneration and Posterior Broadening

**Core idea.** Closing one eye removes an observation channel, not half of the phenomenal world. Monocular vision is not a deletion of appearance; it is a weakening of geometric likelihood constraints. The perceived world remains unified because the cognitive system maintains a posterior over latent scene fields.

### Observation Channels

**Stereo observation:**
$$\mathfrak{O}_t^{\mathrm{stereo}} = (f_L, f_R, \Pi_{LR}, \delta, z, c)$$

where $f_L$, $f_R$ are left/right image frames, $\Pi_{LR}$ is the stereo correspondence map, $\delta$ is disparity, $z$ is depth, and $c$ is a confidence/validity mask.

**Monocular observation:**
$$\mathfrak{O}_t^{\mathrm{mono}} = (f_L)$$

### Shared Latent Target

Both observation channels condition on the same latent scene state:
$$\mathcal{X}_t = (\mathcal{M}_t, \mu_t, U_t)$$

where $\mathcal{M}_t$ is the scene manifold, $\mu_t$ is a measure on $\mathcal{M}_t$, and $U_t : \mathcal{M}_t \to [0,1]$ is the latent soft cohesion field.

### Posteriors

$$\rho_t^{\mathrm{stereo}} = P(\mathcal{X}_t \mid \mathfrak{O}_{1:t}^{\mathrm{stereo}})$$
$$\rho_t^{\mathrm{mono}} = P(\mathcal{X}_t \mid \mathfrak{O}_{1:t}^{\mathrm{mono}})$$

### Key Claim: Posterior Broadening

$$H(\rho_t^{\mathrm{stereo}}) < H(\rho_t^{\mathrm{mono}})$$

or at minimum, under comparable conditions:

$$\mathrm{Var}_{\rho^{\mathrm{stereo}}}(z) < \mathrm{Var}_{\rho^{\mathrm{mono}}}(z)$$

Stereo provides a high-confidence geometric likelihood channel via $\delta$ and $\Pi_{LR}$; monocular vision loses depth-from-disparity but retains shading, perspective, occlusion contours, motion parallax, and temporal continuity as weaker likelihood signals.

**Closing one eye removes an observation channel, not half of the phenomenal world.**

**A missing eye does not create a missing world; it creates a broader posterior.**

### Role of $\mathcal{P}_t$

$\mathcal{P}_t$ (the stereo support space $X_L^{\mathrm{valid}} \times Z_t$, D-ST-2) should be understood as the MAP/visible support induced by the posterior over $\mathcal{X}_t$, not as the deepest ontological primitive. The primitive is the latent scene state $\mathcal{X}_t = (\mathcal{M}_t, \mu_t, U_t)$; $\mathcal{P}_t$ is the observationally grounded projection of that state onto the pixel support. This framing strengthens the role of $\mathcal{X}_t$ as the true ontological carrier and avoids treating $\mathcal{P}_t$ as self-standing. Under monocular observation, $\mathcal{P}_t$ degenerates to $X_L^{\mathrm{valid}}$ (no depth axis), but the latent $\mathcal{X}_t$ is unchanged.

### Effect on $K_{\mathrm{act}}$

The posterior over the formation count:
$$P(K_{\mathrm{act}} \mid \mathfrak{O}_t^{\mathrm{stereo}}) \quad \text{vs} \quad P(K_{\mathrm{act}} \mid \mathfrak{O}_t^{\mathrm{mono}})$$

Stereo tends to sharpen $P(K_{\mathrm{act}} \mid \mathfrak{O}_t)$: depth discontinuities localize formation boundaries, remove cross-boundary edges from $G_t^\mathcal{P}$ (D-ST-1), and topologically lock $K_{\mathrm{act}}$ via graph disconnection (exp02-NEB: flat K=1 vs stereo K=2). Monocular observation broadens $P(K_{\mathrm{act}} \mid \mathfrak{O}_t)$: without disparity, formation boundaries must be inferred from weaker cues alone. However, monocular vision may still infer the same $K$ through priors, temporal continuity, occlusion cues, shading, perspective, and motion parallax.

**Stereo is a high-confidence geometric likelihood channel; monocular vision is a weaker but still valid observation model over the same latent scene field.**

*(Added 2026-05-06 W6 D4 Session B. Status: working-level, Cat C. P-F flag applies to all posterior/entropy claims — quantitative $H(\rho^{\mathrm{stereo}}) < H(\rho^{\mathrm{mono}})$ requires Langevin P-F-A1 formalization.)*

---

**End of stereo_scc_canonical_memo_v1.1.md.**

**Status:** Working-level reference memo (Cat C). Saves Canonical Memo v1.1 produced in
conversation 2026-05-06/07. No canonical claims. All stochastic content P-F flagged.
Supersedes v1 (conversation-only, not saved to file).
Feeds: OP-0005 Commitment 19 candidate, OP-0008 Commitment 18, OP-0009-Pre v2.0 §1 amendment.
