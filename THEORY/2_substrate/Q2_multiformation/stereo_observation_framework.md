> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q4_K_selection]] · [[MOC_sigma_rich_framework]] · [[THEORY_INDEX]]

# stereo_observation_framework.md
# Stereo-SCC Observation Layer and Born-Oppenheimer K-Dynamics

**Status:** working draft (W6 Day 2 evening, 2026-05-05).
**Type:** Application-layer framework + OP-0005/0008/0009-Pre structural proposals.
**Author:** W6 D2 evening session.
**Canonical refs:** §1 primitive ontology; §3 formal universe; §11.1 Commitment 16; §14 CN2/CN5/CN6/CN8/CN10/CN14/CN15; §12 kinetic paradigm.
**Working refs:** `k_selection_mechanism.md` (OP-0005 candidates); `k_selection_b_kramers.md` (Kramers rates); `n1_kramers_extension.md` (N-1 ↔ Kramers bridge); `pre_objective_K_field_tension.md` (OP-0009-Pre); `layered_ambient_architecture_candidate.md` (related architecture discussion); `k_selection_a_free_energy.md` (free energy candidate).
**Source log:** `THEORY/logs/daily/2026-05-05/05_pf_stereo_scc_framework_proposal.md` (full cross-verification).

---

## §1. Mission and Scope

This file develops the **stereo-SCC observation framework**: a principled separation of the SCC soft cohesion primitive $\tilde{u}_t$ from the observation layer $\mathfrak{O}_t$ (stereo camera data), connected via a back-projection bridge. The framework has three interlocking goals:

1. **Correct state space**: Establish $\Sigma_M$ (single field, no $K$ presupposed) as the foundational state space; derive $K_{\text{act}}$ as an emergent observable.
2. **Observation layer**: Define $\mathfrak{O}_t$ and MAP inference cleanly; preserve CN5 by placing photometric terms in the likelihood (not the prior).
3. **BO + Kramers K-dynamics**: Establish Born-Oppenheimer time-scale separation, enabling adiabatic elimination of the fast SCC dynamics and recovery of an effective Markov jump process over $K_{\text{act}}(t)$. This is the structural path toward OP-0005 resolution.

**Scope limitation.** This is a modeling-layer and structural proposal. All stochastic claims (Kramers rates, partition functions, equilibrium distributions) carry **P-F flags**: they require a well-defined stochastic extension of SCC dynamics (Langevin on $\Sigma_M$) before quantitative claims can be made. No canonical claims are asserted here; this file is a CV-1.7+ / v2.0 development target.

---

## §2. Correct State Space: $\Sigma_M$ over $\Sigma^K_M$

### §2.1 The $\Sigma^K_M$ trap

The K-field architecture in current canonical SCC (I9, $\Sigma^K_M = \bigsqcup_{j=1}^{K_{\text{field}}} \Sigma_{m_j}$) fixes $K_{\text{field}}$ as a modeling parameter before dynamics begin. This imports an object-like parameter $K$ — the very quantity the theory should derive. This is OP-0009-Pre.

Specifically: using $\Sigma^K_M$ as a *foundational* state space presupposes that a count of $K$ distinguishable formations exists prior to any dynamical computation. The theory then explains how formations evolve given $K$, but not how $K$ itself emerged. This is a pre-objective tension (CN10: object-level count as input to soft theory).

### §2.2 The correct state space

The ontologically prior state space is

$$\Sigma_M = \bigl\{u \in [0,1]^n : \textstyle\sum_{x} u(x) = M\bigr\}$$

a single $(n-1)$-dimensional simplex face. No $K$ is presupposed. The SCC energy $\mathcal{E}$ is defined on $\Sigma_M$.

The *derived* formation count:

$$K_{\text{act}}(u) := \#\pi_0\!\bigl(\{x \in X : u(x) > \varepsilon\}\bigr)$$

is a topological observable on $\Sigma_M$ — the number of connected components of the $\varepsilon$-superlevel set. The $\varepsilon$ convention follows Commitment 16: $\varepsilon = \bar{m}/M$ with $\bar{m} = M/K_{\text{field}}$ (calibrated to the architectural mean; $K_{\text{field}}$ enters only as a calibration constant, not as an ontological parameter).

### §2.3 Relationship to K-field architecture

The K-field architecture $\Sigma^K_M$ is a *modeling-layer* choice (Commitment 16 (i): $K_{\text{field}}$ = architectural cap, not ontological count). On $\Sigma_M$, the K-field architecture can be recovered as a coordinate chart: each metastable $K$-basin $\mathcal{B}_K \subset \Sigma_M$ is a region where $K_{\text{act}} = K$. The K-field optimization (per-field $u^{(j)}$ with inter-field repulsion) is an efficient numerical search within $\mathcal{B}_K$, not an independent theory.

**Implication for OP-0009-Pre.** The resolution path: $\Sigma_M$ is ontologically primary; $\Sigma^K_M$ is a convenient modeling parameterization of the metastable $K$-basin. This is the "modeling-layer commitment" framing in `pre_objective_K_field_tension.md` (Path A+C hybrid). The present file fleshes it out dynamically via the BO structure (§5).

---

## §3. The 3D Primitive and Observation Layer

### §3.1 Primitive: $\tilde{u}_t$ on 3D Point Cloud

For visual perception via stereo camera, the SCC primitive is

$$\tilde{u}_t : \mathcal{P}_t \to [0,1]$$

where $\mathcal{P}_t \subset \mathbb{R}^3$ is the reconstructed 3D point cloud from stereo disparity at time $t$. The support space $X_t$ in the formal universe (canonical.md §3.2) is instantiated as $\mathcal{P}_t$: a finite set of 3D relational loci.

This choice is motivated by:
- Cohesion is a property of scene geometry, not image coordinates.
- Two pixels adjacent in $X_L$ but separated in depth (foreground/background) should have low adjacency weight in $\mathbf{N}_t$ — depth-aware adjacency (§3.3) enforces this.
- The same physical formation can project to non-contiguous regions under rotation/occlusion; tracking in $\mathcal{P}_t$ is more stable.

**CN10 compliance.** This is a realization of SCC on a 3D support space, not an identification of SCC with depth estimation or 3D reconstruction. The SCC theory operates on $\mathcal{P}_t$ as a relational substrate; depth estimation produces $\mathcal{P}_t$ upstream of SCC.

### §3.2 Observation Layer $\mathfrak{O}_t$

$$\mathfrak{O}_t = (X_L,\, X_R,\, f_L,\, f_R,\, \Pi_{LR},\, \delta,\, z,\, c)$$

- $X_L, X_R$: left and right image pixel grids.
- $f_L : X_L \to \mathbb{R}^3$, $f_R : X_R \to \mathbb{R}^3$: left and right image appearance (RGB or feature) fields.
- $\Pi_{LR} : X_L \rightharpoonup X_R$: epipolar stereo correspondence (partial map; undefined at occlusions and matching failures).
- $\delta : X_L \to \mathbb{R}_{>0}$: disparity field.
- $z : X_L \to \mathbb{R}_{>0}$: depth field, $z(x_L) = f_{\text{cam}} \cdot b / \delta(x_L)$ (stereo formula, $f_{\text{cam}}$ focal length, $b$ baseline).
- $c : X_L \to [0,1]$: disparity confidence / match quality.

$\mathfrak{O}_t$ is the raw observation: the entire sensor readout. The SCC primitive $\tilde{u}_t$ is not in $\mathfrak{O}_t$ — it is inferred from it.

**Monocular vs stereo.** Monocular observation $\mathfrak{O}_t^{\text{mono}} = (X_L, f_L)$ is an underconstrained special case: depth $z$ is underdetermined, so $\mathcal{P}_t$ cannot be reliably reconstructed. The SCC theory can still operate with $X_t = X_L$ (pixel grid), but the 3D primitive and depth-aware adjacency are unavailable. Stereo is the depth-constraining case; monocular degenerates to the 2D SCC formulation.

### §3.3 Back-Projection Bridge

Define the partial back-projection map

$$b_t : X_L \rightharpoonup \mathcal{P}_t, \qquad b_t(x_L) = z(x_L)\, K_{\text{cam}}^{-1} \begin{pmatrix} u_L \\ v_L \\ 1 \end{pmatrix}$$

where $(u_L, v_L)$ are pixel coordinates of $x_L$ and $K_{\text{cam}} \in \mathbb{R}^{3 \times 3}$ is the left camera intrinsic matrix. The partiality: $b_t$ is undefined for $x_L$ with $c(x_L) = 0$ (failed stereo match) or $x_L$ in occluded regions.

Pullback of $\tilde{u}_t$ to pixel space:

$$u_L^{\text{pix}}(x_L) = (b_t^* \tilde{u}_t)(x_L) = \tilde{u}_t(b_t(x_L)), \quad x_L \in \text{dom}(b_t)$$

Full pixel observation tuple:

$$\Phi(x_L) = \bigl(f_L(x_L),\; f_R(\Pi_{LR}(x_L)),\; z(x_L),\; c(x_L),\; \tilde{u}_t(b_t(x_L))\bigr)$$

**Depth-aware adjacency.** The adjacency graph on $\mathcal{P}_t$ uses depth-filtered edges:

$$E_t^{3D} = \bigl\{(b_t(x), b_t(y)) : (x,y) \in E_t^{2D},\;\; \lvert z(x) - z(y) \rvert < \delta_z\bigr\}$$

for depth threshold $\delta_z > 0$. This prevents closure support from bridging across depth discontinuities (foreground/background boundaries). The resulting graph $G_t = (\mathcal{P}_t, E_t^{3D})$ is the substrate for $\mathbf{N}_t$ in this instantiation.

**Structural analogy (CN10 contrastive).** The stereo correspondence $\Pi_{LR} : X_L \rightharpoonup X_R$ is structurally analogous to the temporal transport kernel $\mathbf{M}_{t \to s} : X_t \rightharpoonup X_s$ — both are partial transport maps between support spaces, implementing either spatial (left↔right) or temporal ($t \to s$) transfer. Both can be realized as regularized partial optimal transport. This is a contrastive comparison for structural illumination; not a reductive identification.

---

## §4. Prior / Likelihood Separation (CN5 Compliance)

### §4.1 The structure

The Bayesian inference structure for $\tilde{u}_t$ given $\mathfrak{O}_t$:

**(Prior)** — SCC structural energy:
$$P(\tilde{u}) \propto \exp\!\left(-\frac{\mathcal{E}_{\text{SCC}}[\tilde{u};\mathcal{P}_t]}{T}\right)$$
$$\mathcal{E}_{\text{SCC}} = \lambda_{\text{cl}} E_{\text{cl}} + \lambda_{\text{sep}} E_{\text{sep}} + \lambda_{\text{bd}} E_{\text{bd}} + \lambda_{\text{tr}} E_{\text{tr}}$$

The prior contains exactly the four canonical energy terms. No photometric term here.

**(Likelihood)** — observation-conditioned term:
$$P(\mathfrak{O}_t \mid \tilde{u}) \propto \exp\!\left(-\mathcal{L}_{\text{obs}}[\mathfrak{O}_t \mid \tilde{u}]\right)$$

A natural form for $\mathcal{L}_{\text{obs}}$:

$$\mathcal{L}_{\text{obs}} = \lambda_{\text{photo}} \sum_{x_L \in \text{dom}(b_t)} c(x_L) \cdot \Psi\!\bigl(f_L(x_L),\, f_R(\Pi_{LR}(x_L)),\, \tilde{u}_t(b_t(x_L))\bigr)$$

where $\Psi$ measures photometric consistency weighted by the coherence field value and disparity confidence $c(x_L)$. The exact form of $\Psi$ is a modeling choice (e.g., $\Psi = \lVert f_L - f_R \rVert^2 \cdot \tilde{u}$ — inconsistent regions with high cohesion are penalized).

**(MAP inference)**:
$$\tilde{u}_t^* = \arg\min_{\tilde{u} \in \Sigma_M(\mathcal{P}_t)} \bigl[\mathcal{E}_{\text{SCC}}[\tilde{u};\mathcal{P}_t] + \mathcal{L}_{\text{obs}}[\mathfrak{O}_t \mid \tilde{u}]\bigr]$$

### §4.2 CN5 compliance argument

CN5 (canonical.md §14): "The four energy terms address four logically independent structural requirements." CN5 is about the *prior* (SCC energy); it says nothing about the likelihood. Placing $E_{\text{photo}}$ in $\mathcal{L}_{\text{obs}}$ rather than $\mathcal{E}_{\text{SCC}}$ strictly preserves CN5: the prior is the SCC energy with exactly four terms; photometric consistency is observation-layer information external to the theory's structural axioms.

This is the only CN5-compliant placement. Adding $E_{\text{photo}}$ to $\mathcal{E}_{\text{SCC}}$ would add a fifth energy term with a qualitatively different role (data fidelity, not structural), violating CN5's conceptual independence commitment.

### §4.3 Relationship to OP-0009-λ

OP-0009-λ asks whether $\lambda_{\text{rep}} \langle u^j, u^k \rangle$ is a 5th SCC energy term or a coupling realization. In the present framework, if we use the single-field $\Sigma_M$ formulation, the inter-formation repulsion enters $\mathcal{E}_{\text{SCC}}$ implicitly via the phase separation structure of $E_{\text{sep}}$ on $\Sigma_M$ (no separate $\lambda_{\text{rep}}$ term needed). The K-field repulsion term $\lambda_{\text{rep}} \sum_{j \neq k} \langle u^{(j)}, u^{(k)} \rangle$ is a K-field architecture artifact; it does not appear in the single-field $\Sigma_M$ formulation. This supports OP-0009-λ's "architectural-layer coupling" resolution path.

---

## §5. Born-Oppenheimer Time-Scale Separation

### §5.1 Three time scales

SCC dynamics in the stereo setting involves:

| Scale | Symbol | Typical value | Process |
|-------|--------|--------------|---------|
| Camera frame | $\tau_{\text{frame}}$ | 33 ms (30 fps) | Image acquisition |
| SCC intra-basin relaxation | $\tau_{\text{fast}}$ | $\ll \tau_{\mathcal{P}}$ | Gradient flow of $\tilde{u}_t$ within a $K$-basin |
| Point cloud change | $\tau_{\mathcal{P}}$ | 100 ms – 1 s | Scene/camera motion |
| K-jump (Kramers crossing) | $\tau_{\text{slow}}$ | $\tau_0 e^{\Delta E / T}$ | Formation merger/birth |

Ordering: $\tau_{\text{frame}} \ll \tau_{\text{fast}} \ll \tau_{\mathcal{P}} \lesssim \tau_{\text{slow}}$.

Note: $\tau_{\text{frame}} \ll \tau_{\text{fast}}$ means multiple frames are acquired during a single intra-basin relaxation (the camera is faster than the SCC dynamics at the fast scale). $\tau_{\text{fast}} \ll \tau_{\mathcal{P}}$ is the BO condition: $\tilde{u}_t$ equilibrates before the geometry changes.

### §5.2 The BO condition and its consequence

**BO condition:** $\tau_{\text{fast}} \ll \tau_{\mathcal{P}}$.

Consequence: treat $\mathcal{P}_t$ as a slowly-varying *external parameter* (akin to nuclear coordinates in molecular BO). For each fixed $\mathcal{P}$, the fast variable $\tilde{u}$ equilibrates rapidly to a metastable minimum $u_{\min,K}(\mathcal{P})$ in the $K$-basin. The basin minimum depends parametrically on $\mathcal{P}$:

$$u_{\min,K}(\mathcal{P}) = \arg\min_{u \in \mathcal{B}_K(\mathcal{P})} \mathcal{E}_{\text{SCC}}[u;\mathcal{P}]$$

The adiabatic potential for the slow variable $K_{\text{act}}$:

$$V_K(\mathcal{P}) := \mathcal{E}_{\text{SCC}}\bigl[u_{\min,K}(\mathcal{P});\mathcal{P}\bigr]$$

### §5.3 Effective slow dynamics

After adiabatic elimination of $\tilde{u}$ (integrating out the fast variable), the effective dynamics of $K_{\text{act}}(t)$ is a **continuous-time Markov jump process** on $\{0, 1, \ldots, K_{\text{field}}\}$:

$$\frac{d}{dt} P(K,t) = \sum_{K'} \Gamma^{K' \to K}(\mathcal{P}_t) P(K',t) - \Gamma^{K \to \cdot}(\mathcal{P}_t) P(K,t)$$

with Kramers–Eyring transition rates (see §6). The time-varying $\mathcal{P}_t$ makes this a *non-autonomous* Markov process.

**Two protagonists — neither eliminable.**

- *Microscopic protagonist*: $\tilde{u}_t : \mathcal{P}_t \to [0,1]$ — the SCC primitive; carries all structural/morphological information; cannot be eliminated ontologically.
- *Effective macroscopic protagonist*: $K_{\text{act}}(t)$ — the coarse-grained slow observable; carries the formation-count information; emerges from $\tilde{u}_t$ via BO reduction.

The microscopic protagonist is necessary for: (a) computing barrier energies and prefactors (§6); (b) defining $\sigma$-signatures (§8); (c) recovering $u^*_t$ at any time by basin minimization. The macroscopic protagonist is sufficient for: predicting long-time K-statistics; providing the effective description for perceptual stability modeling.

---

## §6. Kramers Rates: $\mathcal{P}$-Conditional Formulation

### §6.1 Barrier definition

For a transition $K \to K-1$ (merger of two formations $j,k$):

$$\Delta\mathcal{E}^{K \to K-1}_{jk}(\mathcal{P}) := \mathcal{E}_{\text{SCC}}\bigl(u_{\text{saddle}}^{(jk)}(\mathcal{P});\mathcal{P}\bigr) - \mathcal{E}_{\text{SCC}}\bigl(u_{\min,K}(\mathcal{P});\mathcal{P}\bigr)$$

where $u_{\text{saddle}}^{(jk)}$ is the index-1 saddle point of $\mathcal{E}_{\text{SCC}}$ on $\Sigma_M(\mathcal{P})$ connecting the $K$-basin to the $(K-1)$-basin along the $j$-$k$ merger path.

The total $K \to K-1$ rate sums over all formation pairs:

$$\Gamma^{K \to K-1}(\mathcal{P}) = \sum_{j < k,\, j,k \in A_{K}} A_{K \to K-1}^{(jk)}(\mathcal{P}) \cdot \exp\!\left(-\frac{\Delta\mathcal{E}^{K \to K-1}_{jk}(\mathcal{P})}{T}\right)$$

### §6.2 Prefactor (Eyring-Kramers form)

$$A^{(jk)}_{K \to K-1}(\mathcal{P}) = \frac{\vert \lambda_-^{(jk)}\vert}{2\pi} \sqrt{\frac{\det H_{\min,K}(\mathcal{P})}{\bigl\vert \det' H_{\text{saddle}}^{(jk)}(\mathcal{P})\bigr\vert}}$$

where:
- $\lambda_-^{(jk)}$: the unique negative eigenvalue of $H_{\text{saddle}}^{(jk)}$ (index-1 saddle condition).
- $H_{\min,K}$: Hessian of $\mathcal{E}_{\text{SCC}}$ at $u_{\min,K}$ (on $\Sigma_M$).
- $H_{\text{saddle}}^{(jk)}$: Hessian at saddle (on $\Sigma_M$); $\det'$ = product of nonzero eigenvalues.

**Connection to existing results.** From `k_selection_b_kramers.md` §3 (K-field architecture version):

$$\Delta E_{K' \to K'-1}^{(jk)} = \mathcal{E}_K(u_s^{(jk)}) - \mathcal{E}_K(u_{\min,K'})$$

The present $\mathcal{P}$-conditional formulation is the single-field $\Sigma_M$ analogue; in the K-field architecture limit, $\mathcal{E}_K = \mathcal{E}_{\text{SCC}}$ on the per-field sub-manifold, and the two agree.

**Barrier scaling.** From `k_selection_b_kramers.md` §4: $\Delta E \sim \lambda_{\text{rep}} m_j m_k / \lvert X \rvert^{d-2}$ (scaling with inter-formation mass product). This is the K-field architecture form; the single-field $\Sigma_M$ analogue involves the isoperimetric barrier for two connected-component mergers (barrier $\sim$ boundary length between components, $O(\beta^{0.89})$ empirically, exp38/55).

### §6.3 N-1 asymmetry recovered

From `n1_kramers_extension.md` §4: N-1 Soft-Hard Switching Asymmetry (canonical §11.1) is exactly the statement that

$$\Delta\mathcal{E}^{K \to K+1}_{\text{birth}} > \Delta\mathcal{E}^{K \to K-1}_{\text{merger}}$$

in general. At low $T$:

$$\frac{\Gamma^{K \to K+1}}{\Gamma^{K \to K-1}} = \exp\!\left(-\frac{\Delta\mathcal{E}_{\text{birth}} - \Delta\mathcal{E}_{\text{merger}}}{T}\right) \xrightarrow{T \to 0} 0$$

At $T = 0$ (noiseless gradient flow), $\Gamma^{K \to K+1} = 0$ (birth forbidden) and $\Gamma^{K \to K-1}$ dominates — this is exactly NQ-253 §4.3 Claim 4.3 and T-Merge (b) (monotone non-increasing $K_{\text{act}}$ under noiseless flow).

Therefore: **N-1 + T-Merge (b) + K-Selection (b) Kramers + BO adiabatic elimination are four perspectives on the same physics**, valid at different levels of description.

---

## §7. OP-0005 Resolution Path: Partition Function

### §7.1 Basin partition function

⚠️ **P-F flagged.** Requires stochastic SCC extension (Langevin on $\Sigma_M$, temperature $T$ defined) before quantitative claims.

For fixed $\mathcal{P}$, define the restricted partition function over the $K$-basin:

$$Z_K(\mathcal{P}) = \int_{\mathcal{B}_K(\mathcal{P})} \exp\!\left(-\frac{\mathcal{E}_{\text{SCC}}[\tilde{u};\mathcal{P}]}{T}\right) D\tilde{u}$$

where $D\tilde{u}$ is the natural measure on $\Sigma_M(\mathcal{P})$ (Riemannian volume form; specific form is an open question — see OQ-3 in the daily log).

**Effective free energy:**
$$F(K;\mathcal{P}) = -T \log Z_K(\mathcal{P}) = E^*(K;\mathcal{P}) - T S_{\text{config}}(K;\mathcal{P})$$

**Laplace approximation** (valid at low $T$):
$$Z_K(\mathcal{P}) \approx \exp\!\left(-\frac{E^*(K;\mathcal{P})}{T}\right) \cdot \frac{(2\pi T)^{(n-1)/2}}{\sqrt{\det H_{\min,K}(\mathcal{P})}}$$

giving $S_{\text{config}} \approx \frac{n-1}{2}\log(2\pi T e) - \frac{1}{2}\log\det H_{\min,K}$ (Hessian-determinant entropy). This is computable from existing SCC code.

### §7.2 Equilibrium K distribution

Under detailed balance at temperature $T$:

$$P_{\text{eq}}(K \mid \mathcal{P}) \propto \exp\!\left(-\frac{F(K;\mathcal{P})}{T}\right)$$

Detailed balance condition:

$$P_{\text{eq}}(K) \cdot \Gamma^{K \to K-1}(\mathcal{P}) = P_{\text{eq}}(K-1) \cdot \Gamma^{K-1 \to K}(\mathcal{P})$$

$$\Rightarrow \quad \frac{P_{\text{eq}}(K)}{P_{\text{eq}}(K-1)} = \frac{\Gamma^{K-1 \to K}}{\Gamma^{K \to K-1}} = \exp\!\left(-\frac{\Delta\mathcal{E}_{\text{birth}} - \Delta\mathcal{E}_{\text{merger}}}{T}\right)$$

At low $T$: $P_{\text{eq}}(K) \ll P_{\text{eq}}(K-1)$ (birth barrier dominates → equilibrium concentrates at $K=1$, consistent with T-Merge (b)).

At high $T$: $P_{\text{eq}}(K)$ determined by basin entropy ratio $S_{\text{config}}(K) / S_{\text{config}}(K-1)$.

### §7.3 Connection to OP-0005 4-layer composite

The existing OP-0005 partial path (`k_selection_mechanism.md` §3, `k_selection_a_free_energy.md`) proposes:
- **Candidate (a)**: $F(K) = E^*(K) - T S_{\text{config}}(K)$ — P7's $F(K;\mathcal{P})$ is the $\mathcal{P}$-conditional generalization.
- **Candidate (b)**: Kramers escape time $\tau_{K \to K'} \sim \exp(\beta \Delta E)$ — P7's $\Gamma^{K \to K'}$ is the rate version of this.
- **Candidate (c)**: Symmetry-broken stabilizer — not directly addressed here; connects to $\sigma$-framework.

The partition function formulation **unifies (a) and (b)**: $F(K;\mathcal{P})$ encodes both energetic preference (via $E^*$) and entropic selection (via $S_{\text{config}}$); the Kramers rates are the dynamical expression of the free-energy landscape. Candidate (c) may enter via the prefactor $A_{K \to K'}$ (whose dependence on stabilizer size is unexplored — NQ-301/302/303 from `k_selection_mechanism.md`).

**OP-0005 status.** OPEN HIGH. This framework provides a structural resolution path (CV-1.7+ Commitment 19 candidate) but does not constitute a resolution: (i) stochastic SCC not formalized; (ii) $Z_K$ not analytically computed; (iii) predictions not empirically verified.

---

## §8. OP-0008 Connection: $\sigma$-Posterior at K-Jump

⚠️ **P-F flagged.** Requires saddle-point $\sigma$-computation (undefined in current canonical theory).

At a K-jump event ($K \to K-1$ Kramers transition via saddle $u_{\text{saddle}}^{(jk)}$), the post-jump $\sigma$-signature is determined by:

$$\sigma^A_{\text{after}} = \arg\max_\sigma P\bigl(\sigma \mid \text{transition event via saddle } u_{\text{saddle}}^{(jk)},\, \mathcal{P}_t\bigr)$$

The saddle-point field $u_{\text{saddle}}^{(jk)}$ has a well-defined $\sigma$-signature (the symmetry group of the saddle is constrained by the graph geometry and the relative positions of formations $j$ and $k$). The post-jump $\sigma$ is not arbitrary; it is the $\sigma$-signature of the merged formation at $u_{\min,K-1}$ reached by steepest descent from the saddle.

**Connection to OP-0008 Path B.** From `commitment_18_sigma_rich_packet.md`: Commitment 18 candidate requires $\sigma$-rich + $\Phi$-rich path. The saddle-conditioned posterior provides a mechanistic explanation for why $\sigma_{\text{after}}$ is determined: the saddle-to-minimum descent path is $\sigma$-deterministic given the graph and formation geometry. Stochasticity enters only in *which* saddle is crossed (which pair $(j,k)$ merges first) — this is the remaining non-determinism in OP-0008.

**Connection to `k_selection_mechanism.md` candidate (c).** The stabilizer $\text{Aut}(G)_{[u^*(K)]}$ (symmetry group of the post-jump minimizer) is related to the saddle geometry: as two formations merge, the stabilizer can only increase (more symmetry at merged state). The jump $K \to K-1$ selects the $\sigma$ with *larger* stabilizer — K-selection candidate (c) framed dynamically.

---

## §9. Surface Field Theory Connection (CN10 Contrastive)

Under continuum limit of SCC on $\mathcal{P}_t$, with $\mathcal{P}_t$ approximating the visible scene surface $S_t \subset \mathbb{R}^3$:

$$\mathcal{E}_{\text{SCC}}[\tilde{u};S_t] \to \int_{S_t} \left[\frac{\alpha}{2} \bigl\vert \nabla_{S_t}\tilde{u}\bigr\vert ^2 + \beta W(\tilde{u})\right] dA_{S_t}$$

where $\nabla_{S_t}$ is the surface gradient (Laplace-Beltrami), $dA_{S_t}$ is the surface area element, and $W(u) = u^2(1-u)^2$ is the double-well potential.

**Mechanistic correspondence:**
- $E_{\text{cl}} = \lVert (I-P)\tilde{u} \rVert^2 \approx \epsilon^2 \int_{S_t} \vert \nabla_{S_t}\tilde{u}\vert ^2 dA_{S_t}$ (Laplace-Beltrami approximation of closure energy; $\epsilon$ = graph mesh scale).
- $E_{\text{bd}} = 2\alpha \tilde{u}^T L \tilde{u} \approx \frac{\alpha}{2}\int_{S_t}\vert \nabla_{S_t}\tilde{u}\vert ^2 dA_{S_t}$ (boundary energy as Dirichlet form).
- $E_{\text{sep}}$: phase separation, proportional to $\int W(\tilde{u}) dA$.

This is an Allen-Cahn equation on the visible 2D surface $S_t$ embedded in $\mathbb{R}^3$. The Allen-Cahn coarsening exponent in 2D is $t^{1/3}$ (area law by Bray 1994). The LSW (Lifshitz-Slyozov-Wagner) coarsening exponent for 2D Ostwald ripening is $t^{1/3}$.

**V4 Phase 10 connection.** From `k_selection_b_kramers.md` Phase 10 V4: $\Delta t \propto t^{1.315}$ suggests an empirical coarsening exponent. The classical Allen-Cahn exponent $t^{1/3}$ gives merger time $\tau \propto R^3 \propto m^{3/2}$ (formation radius $R \sim m^{1/2}$). The deviation $1.315 \neq 4/3$ requires investigation — possibly related to closure's effect on barrier heights (CN14: closure raises barrier by factor $\beta^{0.89}$ vs $\beta^{0.85}$, modifying effective coarsening exponent).

**CN10 compliance.** The Allen-Cahn / surface field theory limit is a contrastive comparison for continuum approximation; SCC is not "just" Allen-Cahn on a surface. The SCC closure operator has no Allen-Cahn analogue; the σ-framework has no Allen-Cahn analogue; the discrete graph structure (non-manifold, topology changes, occlusion boundaries) has no smooth surface analogue.

---

## §10. Cross-Reference Map

```
stereo_observation_framework.md (this file)
│
├── §2 State space Σ_M
│   ├── pre_objective_K_field_tension.md (OP-0009-Pre, Path A+C)
│   └── K_status_commitment.md (Commitment 16, K_field/K_act)
│
├── §3 Back-projection + 3D primitive
│   ├── layered_ambient_architecture_candidate.md (related architecture)
│   └── [new content — no existing file covers b_t explicitly]
│
├── §4 Prior/Likelihood separation
│   ├── k_selection_a_free_energy.md (P(K) free energy)
│   └── lambda_rep_ontology.md (OP-0009-λ)
│
├── §5–6 BO + Kramers
│   ├── n1_kramers_extension.md (N-1 ↔ Kramers bridge)
│   ├── k_selection_b_kramers.md (K-jump rates)
│   └── k_selection_mechanism.md §3 (candidate (b))
│
├── §7 Partition function Z_K
│   ├── k_selection_mechanism.md §3 candidate (a) [extends to P-conditional]
│   ├── k_selection_a_free_energy.md [extends to P-conditional]
│   └── k_selection_compatibility_proof.md
│
├── §8 σ-posterior at K-jump
│   ├── commitment_18_sigma_rich_packet.md (OP-0008 Path B)
│   ├── sigma_multi_trajectory.md (K-jump event definitions)
│   └── k_selection_mechanism.md §3 candidate (c) [stabilizer connection]
│
└── §9 Surface field theory
    └── k_selection_b_kramers.md Phase 10 V4 [coarsening exponent]
```

---

## §11. Hard Constraint Verification

- [x] **$u_t$ primitive**: $\tilde{u}_t : \mathcal{P}_t \to [0,1]$ is primitive throughout. $K_{\text{act}}$ derived from $u$ via $\pi_0$.
- [x] **CN5 preserved**: Prior has exactly $E_{\text{cl}} + E_{\text{sep}} + E_{\text{bd}} + E_{\text{tr}}$; $E_{\text{photo}}$ in likelihood only.
- [x] **CN10 contrastive**: All Allen-Cahn / Bayesian / depth-estimation comparisons are explicitly contrastive.
- [x] **P-F flagged**: Kramers rates, partition function, $\sigma$-posterior all carry P-F flags. Temperature $T$ undefined until stochastic SCC formalized.
- [x] **OP not silently resolved**: OP-0005 OPEN; OP-0008 OPEN; OP-0009-Pre OPEN. Each section states structural path only.
- [x] **CN6 respected**: $K_{\text{act}}$ is kinetically determined (via Kramers rates); not thermodynamically selected from energy minimization alone (entropy enters via $S_{\text{config}}$).
- [x] **CN8**: Formations are metastable, not globally optimal. $u_{\min,K}$ is a local minimum; $K^* = 1$ is the global minimum (T-Merge (b)).
- [x] **Commitment 16**: $K_{\text{field}}$ appears only as a calibration constant for the $\varepsilon$ convention, not as an ontological parameter.

---

## §12. Status and Promotion Plan

| Section | Content | Status | Promotion target |
|---------|---------|--------|-----------------|
| §2 State space | $\Sigma_M$ vs $\Sigma^K_M$ | Consistent with canonical; modeling-layer proposal | OP-0009-Pre §Path A+C amendment in `pre_objective_K_field_tension.md` |
| §3 Observation layer | $\mathfrak{O}_t$, $b_t$, $E_t^{3D}$ | New content (Cat C / working) | No existing file; this file is primary |
| §4 Prior/Likelihood | MAP structure, CN5 compliance | Consistent; working proposal | Feeds CV-1.7 vision/robotics application layer (long-term) |
| §5–6 BO + Kramers | Time-scale separation, jump rates | Extends existing Kramers files; new $\mathcal{P}$-conditional form | Amendment to `n1_kramers_extension.md` §5; `k_selection_b_kramers.md` §5 |
| §7 Partition function | $Z_K(\mathcal{P})$, $F(K;\mathcal{P})$ | Cat C candidate; P-F flagged | `k_selection_mechanism.md` §3 update; OP-0005 Commitment 19 input |
| §8 σ-posterior | K-jump $\sigma$-inheritance | Cat C candidate; P-F flagged | `commitment_18_sigma_rich_packet.md` amendment |
| §9 Surface field theory | Allen-Cahn on $S_t$, coarsening | Exploratory (OQ-4 open) | `k_selection_b_kramers.md` Phase 10 follow-up |

**NQ generated.** NQ-ST-1: Laplace approximation of $Z_K$ via existing SCC Hessian computation — test whether $\det H_{\min,K}$ computable from current `energy.py` / `optimizer.py` infrastructure.

**P-F axiom v0 candidate.** From tonight's analysis, the P-F flag has a precise form as an axiom:

> **P-F Axiom (v0):** *No metastability rate claim — including Kramers escape times $\tau_{K \to K'}$, K-jump equilibrium distributions $P_{\text{eq}}(K)$, or effective temperatures $T_c(K_1, K_2)$ — may be asserted as a canonical SCC claim until a stochastic extension of the SCC dynamics (a well-defined Langevin process on $\Sigma_M$ with temperature $T > 0$ and invariant measure $\propto \exp(-\mathcal{E}_{\text{SCC}}/T) D\tilde{u}$) has been canonically formalized.*

This axiom makes the P-F flag operational rather than ad hoc. It is a CV-1.7 Axiom Group G candidate (W6 D2 proposal).

---

**End of stereo_observation_framework.md.**

**Status:** Working draft, W6 Day 2 evening, 2026-05-05. All content Cat C / working-level. P-F flags throughout. Not ready for canonical promotion. Feeds OP-0005 Commitment 19, OP-0008 Commitment 18, OP-0009-Pre v2.0 §1 amendment.
