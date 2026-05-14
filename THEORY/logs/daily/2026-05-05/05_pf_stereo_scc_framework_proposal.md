> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 05_pf_stereo_scc_framework_proposal.md
# P-F Framework + Stereo SCC Observation Layer: Mathematical Documentation

**Date:** 2026-05-05 (W6 Day 2 evening session)
**Status:** working draft — daily log record; not yet promoted to working/ or canonical/
**Type:** theoretical development + cross-verification
**Author:** W6 D2 evening session.
**Promotion target:** `THEORY/working/MF/stereo_observation_framework.md` (new working file, same session); canonical §1 / §3 amendment pending OP-0009-Pre full resolution (v2.0 horizon).

---

## §1. Mission

This file formally documents all premises developed in the W6 Day 2 evening session regarding:

1. The correct state space for SCC (rejection of $\Sigma^K_M$; adoption of $\Sigma_M$).
2. The relationship between SCC and a stereo-camera observation model.
3. The separation of observation layer $\mathfrak{O}_t$, primitive $\tilde{u}_t$, and inference.
4. The Born-Oppenheimer time-scale structure enabling adiabatic elimination to $K_{\text{act}}(t)$.
5. The partition function path toward OP-0005 K-Selection.

Each premise is cross-verified against existing canonical.md, theorem_status.md, and working/MF files.

---

## §2. Premises

### P1. State Space: $\Sigma_M$, Not $\Sigma^K_M$

**Statement.** The foundational state space for SCC dynamics is

$$\Sigma_M = \{u \in [0,1]^n : \textstyle\sum_{x \in X} u(x) = M\}$$

The $K$-indexed family $\Sigma^K_M = \bigsqcup_j \Sigma_{m_j}$ (K-field architecture with per-formation sub-manifolds) is a *modeling-layer* choice, not an ontological primitive. Adopting $\Sigma^K_M$ as the foundational state space presupposes the formation count $K$, which is precisely what the theory must derive — this is OP-0009-Pre (pre-objective + K-field tension).

**Implication.** On the single field $\Sigma_M$:

$$K_{\text{act}}(u) \;:=\; \#\pi_0\!\bigl(\{x : u(x) > \varepsilon\}\bigr) \;\in\; \mathbb{N}_0$$

is a *derived* observable (threshold $\varepsilon$ fixed by convention, currently $\varepsilon = \bar{m}/M = 1/K_{\text{field}}$ per Commitment 16 calibration), not a foundational parameter.

**Cross-verification.**

| Source | Status |
|--------|--------|
| canonical.md §3.3 | $u_t : X_t \to [0,1]$ stated as primitive; $K$ not in formal universe $\mathfrak{C}^{\text{soft}}$ |
| canonical.md §11.1 Commitment 16 | $K_{\text{field}}$ = architectural cap (modeling layer); $K_{\text{act}}$ = derived dynamic count |
| canonical.md CN6 | "K is kinetically determined, not thermodynamically selected" — $K_{\text{act}}$ is emergent |
| theorem_status.md OP-0009-Pre | Explicitly flags this tension: "K-field architecture imports object-like K parameter; potential CN10 violation." OPEN. |
| canonical.md CN10 | Contrastive comparison permitted; reductive identification prohibited. $K_{\text{field}}$ as numerical cap is a modeling commitment, not ontological reduction. |

**Consistency verdict:** P1 is fully consistent with existing canonical theory and sharpens the OP-0009-Pre framing. It does not resolve OP-0009-Pre (the architecture choice OP-0009-A is still OPEN).

---

### P2. Primitive: $\tilde{u}_t : \mathcal{P}_t \to [0,1]$ on 3D Point Cloud

**Statement.** For SCC applied to visual/embodied perception via stereo camera, the ontologically primitive field is

$$\tilde{u}_t : \mathcal{P}_t \to [0,1]$$

where $\mathcal{P}_t \subset \mathbb{R}^3$ is the reconstructed 3D point cloud at time $t$. The pixel-domain field $u_t : X_t \to [0,1]$ (on the 2D image grid $X_t$) is a *pullback* of $\tilde{u}_t$ via the back-projection map $b_t$ (see P3).

**Why $\mathcal{P}_t$ and not $X_t$?** The visual world is 3D; pixel coordinates are an observation artifact. Cohesion — as relational self-support — is a property of the scene geometry, not the image coordinates. Two pixels that are adjacent in image space but far apart in 3D (e.g., foreground/background) should not contribute mutual closure support. Depth-aware adjacency $E_t^{3D}$ (P4 below) encodes this; it requires $\mathcal{P}_t$.

**Cross-verification.**

| Source | Status |
|--------|--------|
| canonical.md §2 | "The relational support space $X_t$ is a domain of relational loci, not a collection of pre-given objects... The theory's claim is that cohesive formation *over* $X_t$ provides a structurally richer description than objecthood *within* $X_t$." — $X_t$ is flexible; instantiating it as $\mathcal{P}_t$ is a valid modeling-layer choice. |
| canonical.md §3.2 | "$X_t$ might be a lattice of spatial positions; in a more abstract domain, it might be any finite or countable set of relational loci." — 3D point cloud is admissible. |
| canonical.md CN10 | Does not prohibit the extension to 3D; it prohibits reductive identification of SCC with e.g. depth estimation. The 3D primitive is contrastive (SCC on $\mathcal{P}_t$ vs. depth estimation on $\mathcal{P}_t$). |
| theorem_status.md OP-0009-Pre | This premise is a concrete instance of the "modeling-layer framing" resolution path for OP-0009-Pre. |

**P-F flag.** $\mathcal{P}_t$ is itself an *observed* quantity with stereo reconstruction noise (disparity estimation error, occlusion, matching failures). The field $\tilde{u}_t$ is conditioned on $\mathcal{P}_t$, not on the true 3D geometry. This is an observation model, not a claim of noiseless access to geometry.

**Consistency verdict:** P2 is consistent. It is a new application-layer proposal; no canonical contradiction. Requires OP-0009-Pre resolution for full canonical integration.

---

### P3. Back-Projection Bridge $b_t$ and Pullback

**Statement.** Given stereo reconstruction, define the partial map

$$b_t : X_L \rightharpoonup \mathcal{P}_t, \quad b_t(x_L) = z(x_L) \cdot K_{\text{cam}}^{-1} \begin{pmatrix} u_L \\ v_L \\ 1 \end{pmatrix}$$

where $(u_L, v_L)$ are pixel coordinates of $x_L \in X_L$, $z(x_L)$ is the depth from stereo disparity, and $K_{\text{cam}}$ is the left camera intrinsic matrix. The map is partial ($\rightharpoonup$) because occluded pixels and failed stereo matches have no valid 3D back-projection.

The pullback of $\tilde{u}_t$ to pixel space is

$$u_L^{\text{pix}}(x_L) = (b_t^* \tilde{u}_t)(x_L) := \tilde{u}_t(b_t(x_L)) \quad \text{for } x_L \in \text{dom}(b_t)$$

The full pixel-level observation tuple for $x_L \in \text{dom}(b_t)$ is

$$\Phi(x_L) = \bigl(f_L(x_L),\; f_R(\Pi_{LR}(x_L)),\; z(x_L),\; c(x_L),\; \tilde{u}_t(b_t(x_L))\bigr)$$

where $f_L, f_R$ are left/right image intensities, $\Pi_{LR} : X_L \rightharpoonup X_R$ is the stereo epipolar correspondence map, and $c(x_L)$ is the disparity confidence.

**Depth-aware adjacency.** The graph $G_t = (\mathcal{P}_t, E_t^{3D})$ uses depth-filtered edges:

$$E_t^{3D} = \bigl\{(b_t(x), b_t(y)) : (x,y) \in E_t^{2D},\; |z(x) - z(y)| < \delta_z \bigr\}$$

for depth threshold $\delta_z > 0$. This prevents spurious closure support across depth discontinuities.

**Cross-verification.**

| Source | Status |
|--------|--------|
| canonical.md §3.8 $\mathbf{M}_{t \to s}$ | The stereo correspondence $\Pi_{LR}$ is structurally analogous to the temporal transport kernel $\mathbf{M}_{t \to s}$ — both are partial transport maps between support spaces. This is a contrastive comparison (CN10), not identification. |
| canonical.md §3.5 soft adjacency $\mathbf{N}_t$ | $E_t^{3D}$ is a realization of $\mathbf{N}_t$ with depth-aware connectivity. Consistent with $\mathbf{N}_t$ encoding "local relational support structure." |
| working/MF/k_selection_b_kramers.md | Barrier energies computed on $G_t$ (the adjacency graph); depth-aware $G_t$ is a valid instantiation. |

**Consistency verdict:** P3 is consistent. The back-projection is a modeling-layer choice for implementing $X_t$ in visual perception. Not a canonical claim; working-level proposal.

---

### P4. Observation / Primitive / Prior / Likelihood Separation

**Statement.** The theoretical structure separates into four layers:

**(a) Observation layer** $\mathfrak{O}_t$: the raw sensor data tuple
$$\mathfrak{O}_t = (X_L, X_R, f_L, f_R, \Pi_{LR}, \delta, z, c)$$
where $\delta$ is disparity, $z$ is reconstructed depth, $c$ is disparity confidence.

**(b) Primitive** $\tilde{u}_t : \mathcal{P}_t \to [0,1]$: the SCC field on the 3D scene; the ontological entity.

**(c) Prior** (SCC energy): 
$$P(\tilde{u}) \propto \exp\bigl(-\mathcal{E}_{\text{SCC}}[\tilde{u};\mathcal{P}_t] / T\bigr)$$
where $\mathcal{E}_{\text{SCC}} = \lambda_{\text{cl}} E_{\text{cl}} + \lambda_{\text{sep}} E_{\text{sep}} + \lambda_{\text{bd}} E_{\text{bd}} + \lambda_{\text{tr}} E_{\text{tr}}$ — the four canonical SCC energy terms (CN5).

**(d) Likelihood** (photometric): 
$$P(\mathfrak{O}_t \mid \tilde{u}) \propto \exp\bigl(-\mathcal{L}_{\text{obs}}[\mathfrak{O}_t \mid \tilde{u}]\bigr)$$
The photometric consistency term $E_{\text{photo}}$ lives here, **not** in the prior. This preserves CN5 (four energy terms conceptually independent; photometric consistency is observation-layer information, not SCC structural energy).

**(e) MAP inference**:
$$\tilde{u}_t^* = \arg\min_{\tilde{u} \in \Sigma_M(\mathcal{P}_t)} \bigl[\mathcal{E}_{\text{SCC}}[\tilde{u};\mathcal{P}_t] + \mathcal{L}_{\text{obs}}[\mathfrak{O}_t \mid \tilde{u}]\bigr]$$

**Cross-verification.**

| Source | Status |
|--------|--------|
| canonical.md CN5 | "Four-Term Independence Is Conceptual, Not Mathematical." Explicitly states the four terms address logically independent structural requirements. Placing $E_{\text{photo}}$ in $\mathcal{L}_{\text{obs}}$ (likelihood) rather than $\mathcal{E}_{\text{SCC}}$ (prior) strictly preserves CN5 — the four terms remain the complete prior. |
| canonical.md §2 | "The cohesion field $u_t$ is not a posterior probability, not a class membership score, and not a segmentation mask." — The Bayesian framing must not conflate $\tilde{u}_t$ with a segmentation mask; the MAP solution $\tilde{u}_t^*$ is a soft cohesion field, not a label assignment. |
| canonical.md CN10 | The Bayesian framing is a contrastive comparison to Bayesian segmentation (not reductive identification). SCC is not "just" Bayesian segmentation: the prior is the SCC energy, not an i.i.d. pixel prior. |
| canonical.md CN4 | Group F (crisp recovery interface) is architecturally distinct. MAP here operates at the soft layer; crisp recovery (if needed) is a downstream step. |

**Consistency verdict:** P4 is consistent and specifically mandated by CN5. The separation is precisely what CN5 requires.

---

### P5. Born-Oppenheimer Time-Scale Separation

**Statement.** SCC dynamics on $\mathcal{P}_t$ involves three time scales:

$$\tau_{\text{frame}} \;\ll\; \tau_{\text{fast}} \;\ll\; \tau_{\mathcal{P}} \;\lesssim\; \tau_{\text{slow}}$$

where:
- $\tau_{\text{frame}}$: camera frame period (hardware-fixed, $\sim 33$ms at 30fps).
- $\tau_{\text{fast}}$: relaxation time of $\tilde{u}_t$ within a $K$-basin under Langevin/gradient flow on $\Sigma_M(\mathcal{P}_t)$ (fast variable). Under this flow, $\tilde{u}_t$ equilibrates to the nearest metastable minimum while $\mathcal{P}_t$ is approximately constant.
- $\tau_{\mathcal{P}}$: time scale over which $\mathcal{P}_t$ changes significantly (scene geometry change — object motion, camera motion). $\mathcal{P}_t$ is an *observation-conditioned external parameter* — it is stochastic (stereo noise, matching failures) but treated as a slowly-varying conditioning variable.
- $\tau_{\text{slow}}$: time scale for $K_{\text{act}}$ transitions (Kramers barrier crossings, formation births/mergers). These are rare events: $\tau_{\text{slow}} \gg \tau_{\text{fast}}$.

**BO condition:** $\tau_{\text{fast}} \ll \tau_{\mathcal{P}}$ (fast variable equilibrates before scene geometry changes significantly). This enables adiabatic elimination (P6).

**Cross-verification.**

| Source | Status |
|--------|--------|
| canonical.md §12 "Coarsening dynamics" | "Under gradient flow with small noise, K>1 formations should coarsen toward K=1. The coarsening dynamics are kinetically determined." — coarsening operates on $\tau_{\text{slow}}$; gradient flow on $\tau_{\text{fast}}$. |
| canonical.md CN2 | "$\tau$ (Within-Time) Is Not a Primitive." — the optimization iteration count $\tau$ is $\tau_{\text{fast}}$ in BO language; it is an implementation detail. Consistent: BO demotes $\tau_{\text{fast}}$ to a fast variable, recovering CN2. |
| canonical.md CN6 | "K is kinetically determined" — $K_{\text{act}}$ changes on $\tau_{\text{slow}}$; BO gives this the Kramers rate interpretation. |
| working/MF/n1_kramers_extension.md §4 | "N-1 Soft-Hard Switching Asymmetry = Kramers rate asymmetry." The rate asymmetry $\Delta E_{\text{birth}} > \Delta E_{\text{merger}}$ implies $\tau_{\text{slow}}^{K \to K+1} \gg \tau_{\text{slow}}^{K \to K-1}$ at low $T$. |
| working/MF/k_selection_b_kramers.md | Kramers rates formalized for $K \to K-1$ transitions; $\tau_{\text{slow}}$ is the Kramers escape time. |

**Consistency verdict:** P5 is fully consistent with existing kinetic multi-formation paradigm (canonical.md §15 "Multi-formation paradigm" paragraph). The BO framing organizes the existing kinetic language into a rigorous separation-of-scales structure.

---

### P6. Adiabatic Elimination: Effective Slow Dynamics as Markov Jump Process

**Statement.** Under the BO condition (P5), $\tilde{u}_t$ rapidly equilibrates within a metastable $K$-basin. After adiabatic elimination of the fast variable $\tilde{u}_t$, the effective slow dynamics is a **Markov jump process** over $K_{\text{act}} \in \{0, 1, \ldots, K_{\text{field}}\}$:

$$K_{\text{act}}(t) \xrightarrow{\Gamma^{K \to K'}(\mathcal{P}_t)} K_{\text{act}}(t')$$

with transition rates (Kramers–Eyring form)

$$\Gamma^{K \to K'}(\mathcal{P}) = A_{K \to K'}(\mathcal{P}) \cdot \exp\!\left(-\frac{\Delta\mathcal{E}^{K \to K'}_{\text{barrier}}(\mathcal{P})}{T}\right)$$

where:
- $\Delta\mathcal{E}^{K \to K'}_{\text{barrier}}(\mathcal{P}) = \mathcal{E}_{\text{SCC}}(u_{\text{saddle}}^{(K \to K')};\mathcal{P}) - \mathcal{E}_{\text{SCC}}(u_{\min,K};\mathcal{P})$ — energy barrier between $K$-basin minimum and saddle point connecting $K \to K'$ basin.
- $A_{K \to K'}(\mathcal{P})$ — prefactor (Kramers attempt frequency); in full Eyring-Kramers form:
$$A_{K \to K-1}(\mathcal{P}) = \frac{|\lambda_-|}{2\pi} \sqrt{\frac{\det H_{\min,K}}{\bigl|\det' H_{\text{saddle}}^{K \to K-1}\bigr|}}$$
where $\lambda_-$ is the unique negative eigenvalue of $H_{\text{saddle}}$, $\det'$ is the product of all nonzero eigenvalues.
- $T$ — effective noise temperature (P-F flagged; requires stochastic SCC extension, i.e., Langevin on $\Sigma_M$, before quantitative claims).

**Two protagonists.** At the microscopic level, the dynamical variable is $\tilde{u}_t : \mathcal{P}_t \to [0,1]$ (SCC primitive). After adiabatic elimination, the effective slow protagonist is $K_{\text{act}}(t)$ (coarse-grained Markov process). Both must coexist: $\tilde{u}_t$ cannot be eliminated ontologically (it is the primitive); it can only be integrated out *dynamically* on the fast time scale.

**Cross-verification.**

| Source | Status |
|--------|--------|
| canonical.md §12 Pillar III | "Coarsening dynamics are kinetically determined: formations merge when noise-driven fluctuations bring them below barrier crossing threshold." — BO + Kramers gives precise mathematical form for "below barrier crossing threshold." |
| working/MF/n1_kramers_extension.md §4 | Exact Kramers rate formula quoted for $k_{K \to K \pm 1}$. P6 extends to full $\mathcal{P}$-conditional form. |
| working/MF/k_selection_b_kramers.md | $\Delta E_{K' \to K'-1}^{(jk)} = \mathcal{E}_K(u_s^{(jk)}) - \mathcal{E}_K(u_{\min,K'})$ (K-field architecture version). P6 gives the single-field $\Sigma_M$ version of the same quantity. |
| canonical.md CN8 | "Proto-cohesive formations are metastable critical points of the energy, not necessarily global minimizers." — $u_{\min,K}$ is a local minimum; $u_{\text{saddle}}^{K \to K-1}$ is the connecting saddle. Consistent. |
| canonical.md CN6 | "K emerges kinetically from initial conditions." — P6 gives the Kramers rate that determines how $K_{\text{act}}$ evolves after initialization. |
| theorem_status.md OP-0005 | See P7 below. |
| theorem_status.md OP-0021 | "Stochastic Dynamics: Theory focuses on deterministic gradient descent. How do thermal fluctuations affect dynamics?" — P6 is a substantive advance on OP-0021. |

**P-F flag (mandatory).** All quantitative claims about $\Gamma^{K \to K'}$ require a well-defined stochastic extension of SCC dynamics. Currently, SCC is deterministic gradient flow on $\Sigma_M$. The noise temperature $T$ is not defined in the canonical theory. This is the P-F barrier: *no metastability rate claim without stochastic extension*. The rate formula above is a structural proposal, not a proved theorem. Status: Cat C candidate pending stochastic SCC formalization.

**Consistency verdict:** P6 is consistent with the kinetic paradigm and N-1/Kramers working files. New content: single-field $\Sigma_M$ Kramers formulation with explicit $\mathcal{P}$-conditioning. P-F flag required throughout.

---

### P7. OP-0005 Resolution Path: Partition Function → Free Energy → Equilibrium K Distribution

**Statement.** The OP-0005 K-Selection mechanism admits a formal resolution path via:

**(a) Basin partition function** (conditioned on $\mathcal{P}$):
$$Z_K(\mathcal{P}) = \int_{\mathcal{B}_K(\mathcal{P})} \exp\!\left(-\frac{\mathcal{E}_{\text{SCC}}[\tilde{u};\mathcal{P}]}{T}\right) D\tilde{u}$$
where $\mathcal{B}_K(\mathcal{P}) = \{\tilde{u} \in \Sigma_M(\mathcal{P}) : K_{\text{act}}(\tilde{u}) = K\}$ is the $K$-basin.

**(b) Effective free energy**:
$$F(K;\mathcal{P}) = -T \log Z_K(\mathcal{P})$$

Decomposed as $F(K;\mathcal{P}) = E^*(K;\mathcal{P}) - T S_{\text{config}}(K;\mathcal{P})$ where $E^*(K;\mathcal{P})$ is the basin minimum energy and $S_{\text{config}}$ is the basin entropy (logarithm of basin volume in $\Sigma_M$).

**(c) Equilibrium K distribution** (under detailed balance at temperature $T$):
$$P_{\text{eq}}(K \mid \mathcal{P}) \propto \exp\!\left(-\frac{F(K;\mathcal{P})}{T}\right)$$

with detailed balance: $P_{\text{eq}}(K) \cdot \Gamma^{K \to K-1} = P_{\text{eq}}(K-1) \cdot \Gamma^{K-1 \to K}$.

**(d) K-crossover temperature** $T_c$: at low $T$, $P_{\text{eq}}$ concentrates on $K_{\text{min-energy}}$ (the K-basin with globally lowest $E^*$); at high $T$, entropy dominates and $P_{\text{eq}}$ favors high-degeneracy K values. The crossover $T_c(K_1, K_2;\mathcal{P})$ satisfies $F(K_1;\mathcal{P}) = F(K_2;\mathcal{P})$.

**Cross-verification.**

| Source | Status |
|--------|--------|
| theorem_status.md OP-0005 | "OPEN; partial via 4-layer composite (free-energy / Kramers / numerical anchor / Commitment 16); CV-1.7+ Commitment 19 candidate." — P7 is a formalization of the "free-energy / Kramers" layers. |
| working/MF/k_selection_mechanism.md §3 candidate (a) | Free energy $F(K) = E^*(K) - T S_{\text{config}}(K)$ is candidate (a). P7 extends it to full $\mathcal{P}$-conditional form and connects to candidate (b) Kramers via detailed balance. |
| working/MF/k_selection_a_free_energy.md | Free energy candidate (a) working file; P7 is the $\mathcal{P}$-conditional generalization. |
| working/MF/k_selection_b_kramers.md | Kramers candidate (b); P7 connects it via the Boltzmann equilibrium structure. |
| canonical.md §12 Pillar II | "Metastability across three regimes" — P7's $Z_K$ partition function is the formal expression of metastability in each regime. |
| theorem_status.md OP-0009-λ | $\lambda_{\text{rep}} \langle u^j, u^k \rangle$ as 5th energy term vs coupling realization. In P7 the interaction enters $\mathcal{E}_{\text{SCC}}[\tilde{u};\mathcal{P}]$ in the K-field realization via the inter-field repulsion term. Status of this term in the single-field $\Sigma_M$ formulation remains OP-0009-λ (OPEN). |

**P-F flag.** $Z_K$ requires: (i) a well-defined measure $D\tilde{u}$ on $\Sigma_M$ (currently undefined in canonical theory); (ii) the noise temperature $T$ (currently undefined). Both are P-F barriers. This is a structural proposal in the Cat C range.

**OP non-resolution statement.** P7 provides a *structural resolution path* for OP-0005, not a resolution. OP-0005 remains 🟠 OPEN HIGH. The partition function formulation requires (at minimum): (a) stochastic SCC dynamics (Langevin on $\Sigma_M$) formalized; (b) basin $\mathcal{B}_K$ measure-theoretically defined; (c) $Z_K$ computed or bounded analytically; (d) empirical verification of $P_{\text{eq}}$ predictions. None of these are established as of 2026-05-05.

**Consistency verdict:** P7 is consistent with OP-0005's 4-layer composite path. New content: $\mathcal{P}$-conditional partition function, free energy decomposition, detailed balance K distribution. Candidate mechanism, not proof.

---

### P8. OP-0008 Connection: $\sigma$-Inheritance at K-Jump via Conditional Posterior

**Statement.** OP-0008 asks: after a K-jump event (Kramers transition $K \to K-1$, e.g. two formations merge), what $\sigma$-signature does the surviving formation inherit?

Under the Bayesian/Kramers framework:

$$\sigma^A_{\text{after}} = \arg\max_\sigma P\bigl(\sigma \mid \text{Kramers transition event},\, \mathcal{P}_t\bigr)$$

where the posterior factors as

$$P(\sigma \mid \text{event}, \mathcal{P}) \propto P(\sigma \mid u_{\text{saddle}}^{K \to K-1}) \cdot P(\text{event} \mid \sigma, \mathcal{P})$$

The saddle-point field $u_{\text{saddle}}^{K \to K-1}$ has a specific $\sigma$-signature (the symmetry group of the saddle is determined by the graph geometry and formation positions), which constrains the post-jump $\sigma$-distribution.

**Cross-verification.**

| Source | Status |
|--------|--------|
| theorem_status.md OP-0008 | "σ^A K-jump Inheritance Non-Determinism: OPEN (CV-1.5.1, W5 Day 4); Path B σ-rich + Φ-rich Cat B target." — P8 provides a Bayesian framing of Path B; the conditional posterior is a concrete proposal. |
| working/MF/sigma_multi_trajectory.md | K-jump events (Definition 2.2) are the events over which P8 conditions. |
| working/MF/commitment_18_sigma_rich_packet.md | Commitment 18 (σ-rich + Φ-rich) is the canonical target for OP-0008 resolution; P8's posterior is a candidate mechanism feeding into Commitment 18. |
| canonical.md §11.1 N-1 | "Soft → Hard requires larger fluctuations than Hard → Soft." At the K-jump event, the saddle-point geometry determines which σ irreps are accessible. |

**P-F flag.** $P(\sigma \mid u_{\text{saddle}})$ requires the Hessian computation at the saddle point and the saddle's symmetry group — both undefined in current canonical theory. Cat C candidate.

**Consistency verdict:** P8 is consistent. New content: conditional posterior framing for σ-inheritance at K-jump. Feeds OP-0008 Path B.

---

## §3. Cross-Verification Summary Table

| Premise | Key Canonical Anchors | Hard Constraint Status | OP Impact |
|---------|----------------------|----------------------|-----------|
| P1 (State space $\Sigma_M$) | §3.3 primitive, CN6, Commitment 16 | CN10 ✓, CN5 ✓ | OP-0009-Pre (sharpens framing) |
| P2 (Primitive $\tilde{u}_t$ on $\mathcal{P}_t$) | §2 on $X_t$ flexibility, §3.2, CN10 | CN10 ✓ (contrastive, not reductive) | OP-0009-Pre (modeling-layer resolution path) |
| P3 (Back-projection $b_t$) | §3.5 adjacency, §3.8 transport analogy | CN10 ✓ | None direct |
| P4 (Obs/Prior/Likelihood separation) | CN5, §2, CN4, CN10 | CN5 ✓ (4 terms preserved in prior) | None (preserves existing) |
| P5 (BO time-scale separation) | §12 Pillar III, CN2, CN6, N-1/Kramers | P-F ⚠️ (T undefined) | OP-0021 (advances) |
| P6 (Adiabatic elimination, Markov K-process) | §12 kinetic paradigm, CN8, n1_kramers, k_sel_b_kramers | P-F ⚠️ (T, Langevin undefined) | OP-0005 (structural path), OP-0021 |
| P7 (Partition function, $F(K;\mathcal{P})$) | OP-0005 4-layer composite, k_selection_mechanism (a)(b) | P-F ⚠️ ($D\tilde{u}$ measure undefined) | OP-0005 (formalized path; NOT resolved) |
| P8 ($\sigma$-posterior at K-jump) | OP-0008 Path B, sigma_multi_trajectory, N-1 | P-F ⚠️ (saddle σ undefined) | OP-0008 (candidate mechanism) |

**Legend:** ✓ = consistent and non-violating; ⚠️ = consistent but P-F flag required; all P-F items require stochastic SCC extension before quantitative claims.

---

## §4. New Content (Not Present in Existing Working Files)

The following items from tonight's session are not explicitly in any existing working/MF file and represent new theoretical content:

1. **$\mathcal{P}$-conditional partition function $Z_K(\mathcal{P})$** with full $\tilde{u}$ integration — extends k_selection_a_free_energy.md which has $F(K)$ without $\mathcal{P}$ conditioning.

2. **Back-projection bridge $b_t$ and pullback $u_L^{\text{pix}}$** — no existing file in working/MF addresses the pixel↔3D connection. New working file created: `working/MF/stereo_observation_framework.md`.

3. **Depth-aware adjacency $E_t^{3D}$** — depth-filtered edges. Not in any current working file.

4. **Four-layer separation** (Obs / Primitive / Prior / Likelihood) — partially addressed in `layered_ambient_architecture_candidate.md` but not with explicit Bayesian / MAP formulation or $E_{\text{photo}}$ in likelihood layer.

5. **Revised BO time scale chain**: $\tau_{\text{frame}} \ll \tau_{\text{fast}} \ll \tau_{\mathcal{P}} \lesssim \tau_{\text{slow}}$ — the distinction between $\tau_{\text{frame}}$ and $\tau_{\text{fast}}$ and between $\tau_{\mathcal{P}}$ and $\tau_{\text{slow}}$ is new; existing files only discuss the fast/slow split.

6. **Allen-Cahn / surface field theory connection** — SCC on $\mathcal{P}_t$ → continuum limit on visible surface $S_t$: $\int_{S_t}[\frac{\alpha}{2}|\nabla_{S_t}\tilde{u}|^2 + \beta W(\tilde{u})]dA_{S_t}$, connecting to LSW coarsening $t^{4/3}$ (k_selection_b_kramers Phase 10 V4 exponent $\approx 1.315 \approx 4/3$).

7. **Two-protagonist articulation** — explicit naming: $\tilde{u}_t$ = ontological/microscopic protagonist; $K_{\text{act}}(t)$ = effective/macroscopic protagonist after BO reduction. Neither can be eliminated; they operate on different time scales.

---

## §5. Hard Constraint Compliance Checklist

- [x] **$u_t$ primitive maintained**: $\tilde{u}_t : \mathcal{P}_t \to [0,1]$ is the primitive in all premises; $K_{\text{act}}$ is derived.
- [x] **CN5 four-term independence**: $E_{\text{photo}}$ placed in $\mathcal{L}_{\text{obs}}$ (likelihood), not in $\mathcal{E}_{\text{SCC}}$ (prior). The prior has exactly the four canonical terms.
- [x] **CN10 contrastive only**: All connections to Allen-Cahn, Bayesian segmentation, depth estimation are explicitly contrastive. No reductive identification.
- [x] **P-F flag on noise**: All stochastic/metastability claims carry explicit P-F flag. Temperature $T$ is undefined in current canonical theory; no quantitative rate claims are made without this flag.
- [x] **OP not silently resolved**: OP-0005 explicitly declared OPEN HIGH with structural path only. OP-0008 has candidate mechanism only. OP-0009-Pre has modeling-layer framing only.
- [x] **No canonical reverse flow**: This is a daily log file. No edits to canonical.md proposed without formal promotion pipeline.
- [x] **Commitment 16 respected**: $K_{\text{field}}$ = architectural cap; $K_{\text{act}}$ = dynamic count. $K_{\text{field}}$ does not appear as a fundamental parameter in P1–P8.

---

## §6. Promotion Targets

| Content | Target | Priority | Status |
|---------|--------|----------|--------|
| Full framework (P1–P8) | `working/MF/stereo_observation_framework.md` (new) | P1 | Created this session |
| P7 $Z_K(\mathcal{P})$ formalization | `working/MF/k_selection_mechanism.md` §3 amendment | P1 | Pending P-F stochastic extension |
| P5–P6 BO structure | `working/MF/n1_kramers_extension.md` §5 extension | P2 | Pending |
| P8 $\sigma$-posterior | `working/MF/commitment_18_sigma_rich_packet.md` | P2 | Pending |
| P2 $\tilde{u}_t$ on $\mathcal{P}_t$ | canonical.md §1 / §3 amendment | v2.0 | Requires OP-0009-Pre resolution |

---

## §7. Open Questions Generated

**OQ-1.** Can $Z_K(\mathcal{P})$ be approximated analytically under the saddle-point (Laplace) approximation? The Laplace approximation gives:
$$Z_K(\mathcal{P}) \approx \exp\!\left(-\frac{E^*(K;\mathcal{P})}{T}\right) \cdot \frac{(2\pi T)^{n/2}}{\sqrt{\det H_{\min,K}}}$$
This converts basin entropy $S_{\text{config}}$ into a Hessian determinant — computable from existing SCC code.

**OQ-2.** Under what conditions is the BO approximation valid for SCC? The standard BO condition $\tau_{\text{fast}} \ll \tau_{\mathcal{P}}$ translates to: the intra-basin relaxation time (inverse of second eigenvalue of Hessian at $u_{\min,K}$) is much smaller than the time scale of $\mathcal{P}_t$ change. This is an empirical question requiring exp design.

**OQ-3.** What is the correct measure $D\tilde{u}$ on $\Sigma_M(\mathcal{P}_t)$ for the path integral? The natural choice is the Riemannian volume form on $\Sigma_M$ with metric induced by $\mathcal{E}_{\text{SCC}}$'s Hessian (curved measure). Alternative: uniform Lebesgue measure restricted to $\Sigma_M$. The choice affects $S_{\text{config}}$ quantitatively.

**OQ-4.** Does the surface field theory limit (Allen-Cahn on $S_t$, coarsening $t^{4/3}$) match k_selection_b_kramers Phase 10 V4 exponent $\approx 1.315$? The LSW coarsening exponent for the Allen-Cahn equation in 2D is $t^{1/2}$ (area law), not $t^{4/3}$. The $t^{4/3}$ exponent suggests a different coarsening mechanism. This requires clarification.

---

**End of 05_pf_stereo_scc_framework_proposal.md.**

**Session:** W6 Day 2 evening, 2026-05-05. All premises working-level; no canonical claims made. P-F flag on all stochastic content. Working file `stereo_observation_framework.md` created concurrently in `working/MF/`.
