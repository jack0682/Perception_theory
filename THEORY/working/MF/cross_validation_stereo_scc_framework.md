> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q4_K_selection]] · [[MOC_sigma_rich_framework]] · [[THEORY_INDEX]]

# cross_validation_stereo_scc_framework.md
# Cross-Validation of Existing SCC Theories under the Stereo-Conditioned Soft-to-Crisp Framework

**Status:** working draft (W6 Day 2 evening, 2026-05-05).
**Type:** Comprehensive cross-validation / theory audit.
**Author:** W6 D2 evening session.
**Reference framework:** `stereo_observation_framework.md` (W6 D2, this session).
**Source log:** `logs/daily/2026-05-05/05_pf_stereo_scc_framework_proposal.md`.
**Canonical refs:** canonical.md CV-1.5.2; theorem_status.md (all active OPs).
**Working refs:** all working/MF/*.md files audited below.

---

## Preamble: The Reference Structure

The new framework against which all existing theories are validated:

$$\mathfrak{O}_t = (X_L, X_R, f_L, f_R, \Pi_{LR}, \delta, z, c) \quad \text{[Observation layer]}$$

$$\tilde{u}_t : \mathcal{P}_t \to [0,1] \quad \text{[Primitive soft field on 3D support]}$$

$$\mathcal{X}_t = (\mathcal{M}_t, \mu_t, U_t) \quad \text{[Latent scene field; extends to occluded regions]}$$

$$P(\tilde{u} \mid \mathfrak{O}_t) \propto P(\mathfrak{O}_t \mid \tilde{u})\, P(\tilde{u}) \quad \text{[Bayesian inference structure]}$$

$$\tilde{u}_t^* = \arg\min_{\tilde{u}} \bigl[\mathcal{E}_{\mathrm{SCC}}[\tilde{u}] + \mathcal{L}_{\mathrm{obs}}[\mathfrak{O}_t \mid \tilde{u}]\bigr] \quad \text{[MAP]}$$

$$K_{\mathrm{act}} = \#\{\text{persistent metastable components of } \tilde{u}\} \quad \text{[Derived observable]}$$

$$F(K;\mathcal{P}) = -T \log \int_{\mathcal{B}_K(\mathcal{P})} \exp\!\left(-\frac{\mathcal{E}_{\mathrm{SCC}}[\tilde{u};\mathcal{P}]}{T}\right) D\tilde{u} \quad \text{[Effective free energy]}$$

$$\Gamma^{K \to K'}(\mathcal{P}) = A_{K \to K'}(\mathcal{P}) \exp\!\left(-\frac{\Delta E_{K \to K'}(\mathcal{P})}{T}\right) \quad \text{[Kramers transition rates]}$$

**Seven-layer decomposition (A–G):**

| Layer | Symbol | Content |
|-------|--------|---------|
| A | $\mathfrak{O}_t$ | Raw observation (camera, pixels, correspondence, depth, confidence) |
| B | $\mathcal{P}_t$, $\tilde{u}_t$ | Visible 3D support + soft field over it |
| C | $\mathcal{X}_t = (\mathcal{M}_t, \mu_t, U_t)$ | Latent scene (occluded parts, belief, full-scene support) |
| D | $P(\tilde{u}) \propto e^{-\mathcal{E}_{\mathrm{SCC}}}$ | SCC prior (4 energy terms) |
| E | $P(\mathfrak{O}_t \mid \tilde{u})$ | Observation likelihood ($E_{\mathrm{photo}}$, reprojection, confidence) |
| F | $K_{\mathrm{act}}, B_t, \sigma^A$ | Topological / derived observables |
| G | $K_{\mathrm{act}}(t)$, $\Gamma^{K \to K'}$, $F(K;\mathcal{P})$ | Effective slow dynamics (BO-reduced) |

---

## §1. Existing Theory Inventory

### §1.1 Master Table

Each row: (Theory/Concept, Original Role, New Framework Position, Disposition, Related OPs, Dangerous Assumptions)

| # | Theory / Concept | Original role | New layer | Disposition | OPs | Dangerous assumptions |
|---|-----------------|--------------|-----------|-------------|-----|----------------------|
| 1 | SCC primitive $u_t : X_t \to [0,1]$ | Foundational primitive | B (if $X_t = \mathcal{P}_t$) | **Maintain** | OP-0009-Pre | $X_t$ interpreted as 2D pixel grid conflates layers A and B |
| 2 | Closure energy $E_{\mathrm{cl}} = \|(I-P)u\|^2$ | Self-reinforcement term in prior | D (SCC prior) | **Maintain** | — | None; well-defined on any graph |
| 3 | Separation energy $E_{\mathrm{sep}}$ | Inter-formation repulsion prior | D (SCC prior) | **Maintain** | OP-0009-λ | $\lambda_{\mathrm{rep}}$ as a 5th energy term risks CN5 violation |
| 4 | Boundary energy $E_{\mathrm{bd}} = 2\alpha u^T L u$ | Interface regularity prior | D (SCC prior) | **Maintain** | OP-0006 | Threshold-based boundary conflates D and F |
| 5 | Transport energy $E_{\mathrm{tr}}$ | Temporal coherence prior | D (SCC prior) | **Maintain with clarification** | OP-0011 | May conflate temporal prior with likelihood |
| 6 | CN5 (4-term independence) | Conceptual independence of 4 priors | D — meta-constraint on prior | **Maintain; sharpened** | — | $E_{\mathrm{photo}}$ classified as 5th prior violates CN5 |
| 7 | $K$-field architecture ($\Sigma^K_M$) | Foundational state space | Modeling-layer chart over $\mathcal{B}_K \subset \Sigma_M$ | **Demote** from foundational to chart | OP-0009-Pre, OP-0009-A | Using $\Sigma^K_M$ as foundational presupposes $K$ |
| 8 | Shared-pool manifold $\widetilde\Sigma^K_M$ | Alternative state space | Modeling-layer sub-manifold | **Demote** (same as above) | OP-0009-A | Same pre-supposition as K-field |
| 9 | $\Sigma_M$ | Single-field simplex | **B: correct foundational state space** | **Promote to foundational** | OP-0009-Pre | None; $K_{\mathrm{act}}$ derived from $\pi_0$ |
| 10 | Commitment 16 ($K_{\mathrm{field}}/K_{\mathrm{act}}$) | Two-tier K decomposition | G (architectural cap) + F (derived count) | **Maintain; re-read** | OP-0009-K | $K_{\mathrm{field}}$ as ontological entity; should be numerical truncation |
| 11 | $K_{\mathrm{act}} = \#\{j : \|u^{(j)}\|_1 > \varepsilon\}$ | Active-slot count | F (topological observable) | **Maintain; redefine cleanly** | — | Threshold $\varepsilon$ as free parameter; should be $\pi_0$ of $\varepsilon$-superlevel |
| 12 | $K_{\mathrm{act}} = \#\pi_0(\{x : \tilde{u}(x) > \varepsilon\})$ | New definition (this session) | F (topological observable on $\Sigma_M$) | **New canonical candidate** | OP-0009-Pre | None given $\varepsilon$ fixed by Commitment 16 calibration |
| 13 | Multi-formation static $\sigma$ | $\sigma$-signature at static minimizer | F (topological / group-theoretic label) | **Maintain** | OP-0008 | $\sigma$ at static minimizer may differ from $\sigma$ at dynamic endpoint |
| 14 | $\sigma^A$ K-jump inheritance | Deterministic label rule at K-jump | F + G interface | **Redefine** as conditional posterior | OP-0008 | Deterministic $\sigma^A$ assumes no randomness in Kramers path |
| 15 | OP-0005 K-Selection | Missing mechanism question | G (effective dynamics) | **Partially addressed** by $F(K;\mathcal{P})$ path | OP-0005 | Conflating static energy minimization with dynamical selection |
| 16 | OP-0006 Boundary precision | Threshold-based boundary imprecision | F + B interface | **Reframe** as persistence/metastability boundary | OP-0006 | Threshold boundary conflates observations with field structure |
| 17 | OP-0008 $\sigma^A$ non-determinism | Label inheritance non-determinism | F + G interface | **Reframe** as Kramers-conditioned posterior | OP-0008 | Deterministic assignment ignores transition stochasticity |
| 18 | OP-0009-Pre K-field tension | K presupposed in architecture | Architectural layer | **Sharpen**: $\Sigma_M$ resolves, $\Sigma^K_M$ perpetuates | OP-0009-Pre | $K_{\mathrm{field}}$ as primitive; should be truncation parameter |
| 19 | OP-0011 Transport uniqueness | Non-uniqueness of $M_{t \to s}$ | D (transport prior) + C (latent) | **Reframe** as prior + latent separation | OP-0011 | Temporal transport conflated with spatial stereo correspondence |
| 20 | OP-0012 Persistence composition | Multi-step temporal persistence | D (transport prior) + G (dynamics) | **Maintained** as open | OP-0012 | — |
| 21 | P-F framework | No metastability without stochastic ext. | G (flags metastability claims) | **Maintain; formalize as Axiom v0** | All OPs | P-F as informal flag; should be formal axiom |
| 22 | Fokker-Planck on $\Sigma_M$ | Probability density $\rho_t(\tilde{u})$ on field space | G (field-level stochastic) | **Maintain as two-level** | OP-0021 | Conflating field-level FP with K-level master equation |
| 23 | Kramers transition / escape | K-jump rate formula | G (effective dynamics) | **Maintain; extend to $\mathcal{P}$-conditional** | OP-0005, OP-0008 | Using K-field saddle instead of $\Sigma_M$ saddle |
| 24 | MFPT formula | Mean first passage time to K-basin escape | G (effective dynamics) | **Maintain; distinguish 3 types** | OP-0008, OP-0011 | MFPT conflated across K-escape/persistence/transport |
| 25 | Transport kernel $M_{t \to s}$ | Temporal transport / inheritance | D (prior) for temporal coherence | **Redefine role** as field-support transport | OP-0011 | $M_{t \to s}$ as object-level matching vs. field transport |
| 26 | Diagnostic vector $\mathbf{d} = (\mathrm{Bind}, \mathrm{Sep}, \mathrm{Inside}, \mathrm{Persist})$ | 4D quality summary | F (derived observable) | **Maintain** | — | None |
| 27 | Boundary band $B_t$ | $D_t$-threshold based boundary | F + D interface | **Redefine** as gradient ridge of $|\nabla_{\mathcal{P}_t}\tilde{u}_t|$ | OP-0006 | Threshold boundary unstable under gauge/scale changes |
| 28 | Persistent homology / $H_0$ | Formation count via death-birth persistence | F (topological observable) | **Promote; connect to $K_{\mathrm{act}}$ definition** | — | 2-parameter ($\theta, \ell$) filtration not yet canonical |
| 29 | $T$-Merge (b) — noiseless $K_{\mathrm{act}} \searrow$ | Monotone decreasing $K_{\mathrm{act}}$ under noiseless flow | G ($T \to 0$ limit) | **Maintain; recovered from BO** | OP-0005 | Noiseless $=$ $T=0$ Kramers; not all physical situations |
| 30 | T-L1-F Hard-Bar / Active-Count Bridge | $K_{\mathrm{bar}} = K_{\mathrm{act}}$ under L1-J regime | F (counting bridge) | **Maintain; layer-A agnostic** | OP-0005 | Conditional on $(P0)$–$(P11)$ hypothesis package |
| 31 | Phase-field / Allen-Cahn analogy | Continuum limit of $E_{\mathrm{cl}} + E_{\mathrm{bd}}$ | D (prior analogy, contrastive) | **Maintain as contrastive** | — | CN10: reductive identification prohibited |
| 32 | Ginzburg-Landau / $\phi^4$ analogy | Double-well potential $W(u)$ | D (prior analogy) | **Maintain as contrastive** | — | $W(u) = u^2(1-u)^2 \neq \phi^4$ exactly |
| 33 | Raw pixel field $f_t : X_L \to \mathbb{R}^3$ | Appearance / luminance field | A (observation layer) | **Reclassify** to obs layer | — | Conflating $f_t$ with $\tilde{u}_t$ is layer confusion |
| 34 | Stereo correspondence $\Pi_{LR}$ | Spatial correspondence map | A (observation layer) | **Maintain in obs layer** | — | $\Pi_{LR}$ as transport conflates A and G layers |
| 35 | Visible 3D support $\mathcal{P}_t$ | 3D scene point cloud | B (visible reconstruction) | **New canonical concept** | OP-0009-Pre | $\mathcal{P}_t$ conflated with true scene geometry |
| 36 | Latent scene field $U_t : \mathcal{M}_t \to [0,1]$ | Full-scene primitive (including occluded) | C (latent layer) | **New; extend from $\tilde{u}_t$** | — | $U_t$ undefined in current canonical |
| 37 | Measured latent state $\mathcal{X}_t = (\mathcal{M}_t, \mu_t, U_t)$ | Structured scene state | C (latent layer) | **New; not in canonical** | — | $\mathcal{M}_t$ definition unclear |
| 38 | Gauge/scale appearance structure $\mathcal{B}(f)$ | Scale-space filtration of appearance | A (obs) + E (likelihood) | **Maintain in likelihood** | — | Gauge transform not the same as SCC automorphism |
| 39 | $\sigma$-signature (Commitment 14) | $\mathrm{Aut}(G)$-invariant label at minimizer | F (topological / group label) | **Maintain** | OP-0008, OP-0009-Emp | Static $\sigma$ ≠ dynamic $\sigma$ trajectory |
| 40 | Layered ambient architecture (working/MF) | Three-layer K ontology | Partial overlap with B/C/G | **Superseded by current framework; preserve useful sub-definitions** | OP-0009-A | Uses $\Sigma^K_M$ as ambient, not $\Sigma_M$ |
| 41 | $k\_selection\_a\_free\_energy.md$ $F(K)$ | Thermodynamic free energy for K | G candidate | **Superseded** by $F(K;\mathcal{P})$; extend or replace | OP-0005 | $F(K)$ defined on $\Sigma^K_M$; missing $\mathcal{P}$-dependence |
| 42 | $k\_selection\_b\_kramers.md$ rates | Kramers rate on K-field submanifold | G (effective dynamics) | **Maintain; extend to $\Sigma_M$ saddle** | OP-0005, OP-0008 | Saddle defined on $\Sigma^K_M$, not $\Sigma_M$ |
| 43 | N-1 Soft-Hard Switching Asymmetry | Asymmetric barrier heights birth vs. merger | G ($T \to 0$ Kramers asymmetry) | **Maintain; recovered from BO** | OP-0005, OP-0008 | Already well-placed |
| 44 | CN6 ($K$ kinetically determined) | K emerges from dynamics, not energy min | G | **Maintain; sharpened by BO** | OP-0005 | "Kinetically determined" now has precise Kramers rate formula |
| 45 | CN15 Static/Dynamic Separation | Static min ≠ dynamic endpoint | G (explains why) | **Maintain; BO formalizes it** | OP-0005, OP-0009 | Still underpins the whole kinetic paradigm |
| 46 | co-belonging $\mathbf{C}_t$ (derived diagnostic) | Non-local structural integration | D (derived; not in prior) | **Maintain as diagnostic** | — | $\mathbf{C}_t$ NOT in energy, NOT in obs likelihood |
| 47 | Predicate-energy bridge Sep = $1 - E_{\mathrm{sep}}/m$ | Exact equivalence between Sep predicate and energy | F (derived equivalence) | **Maintain** | — | None; Cat A |
| 48 | Morphological quality $\mathcal{Q}_{\mathrm{morph}}$ | TDA-based morphology measure | F (topological observable) | **Maintain** | OP-0006 | Filtration-based; consistent with Layer F |
| 49 | T-PreObj-1 / T-PreObj-1G | $\mathcal{F}=1$ disk non-critical under full SCC | D + F (landscape structure) | **Maintain; layer D correctly** | — | None; Cat A |
| 50 | Phase 10 V4 $\Delta t \propto t^{1.315}$ | Empirical coarsening exponent | G (numerical anchor) | **Maintain; compare to Allen-Cahn $t^{1/3}$** | OP-0005 | OQ-4: 1.315 ≠ 4/3 requires explanation |

---

## §2. Layer Assignment Table (Compact)

| Layer | Entities in this layer |
|-------|----------------------|
| **A: Observation** | $\mathfrak{O}_t$, $X_L$, $X_R$, $f_L$, $f_R$, $\Pi_{LR}$, $\delta$, $z$, $c$, camera intrinsics $K_{\mathrm{cam}}$, disparity error model, frame rate $\tau_{\mathrm{frame}}$; raw pixel field $f_t$; gauge/scale appearance $\mathcal{B}(f)$ |
| **B: Visible Reconstruction** | $\mathcal{P}_t$ (3D point cloud), $\tilde{u}_t : \mathcal{P}_t \to [0,1]$, depth-aware graph $G_t = (\mathcal{P}_t, E_t^{3D})$, back-projection $b_t$, pullback $u_L^{\mathrm{pix}}$; 2D pixel-SCC as degenerate case when $\mathcal{P}_t = X_L$ |
| **C: Latent Scene** | $\mathcal{M}_t$ (full 3D scene manifold including occluded), $\mu_t$ (scene measure), $U_t : \mathcal{M}_t \to [0,1]$ (full latent field); $\tilde{u}_t = U_t\big|_{\mathcal{P}_t}$ (restriction to visible) |
| **D: SCC Prior** | $\mathcal{E}_{\mathrm{SCC}} = E_{\mathrm{cl}} + E_{\mathrm{sep}} + E_{\mathrm{bd}} + E_{\mathrm{tr}}$; closure operator $\mathrm{Cl}_t$; distinction $\mathbf{D}_t$; adjacency $\mathbf{N}_t$; double-well $W(u)$; phase-field analogy (Allen-Cahn on $\mathcal{P}_t$ as contrastive comparison); co-belonging $\mathbf{C}_t$ (diagnostic, NOT in prior) |
| **E: Observation Likelihood** | $\mathcal{L}_{\mathrm{obs}} = E_{\mathrm{photo}}$ (photometric consistency, stereo matching, reprojection); confidence weighting $c(x_L)$; gauge/scale observation variance; $\Pi_{LR}$-based consistency |
| **F: Topological Observables** | $K_{\mathrm{act}} = \#\pi_0(\{x : \tilde{u}(x) > \varepsilon\})$; boundary band $B_t = $ gradient ridge of $|\nabla_{\mathcal{P}_t}\tilde{u}_t|$; $\sigma$-signature (Commitment 14, static); $\sigma^A$ (dynamic, K-jump conditioned); $T$-L1-F hard-bar bridge; persistent homology / $H_0$ bars; $\mathcal{Q}_{\mathrm{morph}}$; diagnostic vector $\mathbf{d}$; predicate-energy bridge |
| **G: Effective Slow Dynamics** | $K_{\mathrm{act}}(t)$ Markov jump process; $\Gamma^{K \to K'}(\mathcal{P})$ Kramers rates; $F(K;\mathcal{P})$ effective free energy; $Z_K(\mathcal{P})$ basin partition function; $P_{\mathrm{eq}}(K|\mathcal{P})$ Boltzmann distribution; N-1 asymmetry ($\Delta E_{\mathrm{birth}} > \Delta E_{\mathrm{merger}}$); T-Merge (b) at $T=0$; CN6 (kinetic determination); CN15 (static/dynamic separation); BO time-scale structure |

### Multi-layer entities (decomposed)

| Entity | Layer decomposition |
|--------|-------------------|
| Transport kernel $M_{t \to s}$ | D (temporal coherence prior) for $\tilde{u}_t$ on $\mathcal{P}_t$; C (latent transport) for $U_t$ on $\mathcal{M}_t$ |
| $K_{\mathrm{field}}$ (architectural cap) | Numerical truncation parameter; enters B/G as a calibration constant for $\varepsilon$ convention; NOT foundational ontology |
| Stereo correspondence $\Pi_{LR}$ | A (raw observation) and E (likelihood computation); structurally analogous to $M_{t \to s}$ (contrastive, CN10) |
| Gradient flow on $\Sigma_M$ | D + B: defines SCC dynamics on the visible field; fast timescale $\tau_{\mathrm{fast}}$ |
| Fokker-Planck / Langevin | B+D (field-level stochastic, undefined in canonical) AND G (K-level master equation via Kramers) |
| $\sigma^A$ K-jump inheritance | F (label at minimizer) and G (conditioned on Kramers transition event) |
| Persistent homology | F (static: $K_{\mathrm{act}}$ from $H_0$) and G (dynamic: 2-parameter $(\theta, \ell)$ filtration for $K$-stability) |

---

## §3. Theory-by-Theory Verification (15 Questions)

The 15 verification questions:

1. Q1: Does this theory mistake observation for primitive?
2. Q2: Does it presuppose $K$ or object identity?
3. Q3: Does it maintain $\tilde{u}$ or $U$ as soft primitive?
4. Q4: Is $K_{\mathrm{act}}$ clearly a topological observable, not a state-space index?
5. Q5: Is stereo likelihood mixed into SCC prior?
6. Q6: Is boundary defined by persistence/metastability (not threshold)?
7. Q7: Is transport field-level (not object-level)?
8. Q8: Is $\sigma^A$ a posterior (not deterministic rule)?
9. Q9: Is time-scale separation explicit?
10. Q10: Is K-selection via free energy / stationary distribution (not energy minimization)?
11. Q11: Is $K_{\mathrm{max}} / K_{\mathrm{field}}$ kept as numerical truncation (not ontology)?
12. Q12: Are 2D/3D/latent layers distinct?
13. Q13: Does the framework hold for mono/stereo/occlusion?
14. Q14: Is gauge/scale sensitivity treated as likelihood (not noise)?
15. Q15: Minimum modification needed to fit new framework?

**Verdict key:** ✓ = PASS; △ = PARTIAL PASS; ✗ = FAIL; ? = UNCLEAR

### §3.1 SCC canonical core (canonical.md §1–§14)

| Q | Verdict | Notes |
|---|---------|-------|
| Q1 | △ | $X_t$ is flexible but examples default to pixel grid; 2D $\neq$ 3D conflation possible at implementation |
| Q2 | △ | Formal universe does not presuppose $K$; but K-field architecture (§12) does import $K_{\mathrm{field}}$ |
| Q3 | ✓ | $u_t$ firmly primitive (§3.3, §2); objects are derivative |
| Q4 | △ | $K_{\mathrm{act}}$ defined via threshold count on K-field slots (Commitment 16); should be $\pi_0$ of superlevel set |
| Q5 | ✓ | No observation term in $\mathcal{E}_{\mathrm{SCC}}$ currently; CN5 strict |
| Q6 | ✗ | $B_t$ defined via $D_t$ threshold (§5); not persistence-based (OP-0006 OPEN HIGH) |
| Q7 | △ | $M_{t \to s}$ axioms E1-E4 are field-level; but "external features $\varphi$" in realization may conflate A and D |
| Q8 | ✗ | $\sigma^A$ not defined as posterior; OP-0008 records non-determinism but leaves it unresolved |
| Q9 | ✗ | No time-scale separation in canonical; gradient flow iteration $\tau$ is CN2 (implementation detail), not BO |
| Q10 | △ | CN15 says static min $\neq$ endpoint; CN6 says kinetic; but neither gives $F(K;\mathcal{P})$ structure |
| Q11 | △ | Commitment 16 calls $K_{\mathrm{field}}$ "architectural cap"; but it enters $\Sigma^K_M$ as a foundational parameter |
| Q12 | ✗ | No distinction between 2D pixel support and 3D point cloud support; $X_t$ is undifferentiated |
| Q13 | ✗ | Monocular only (no stereo, no depth, no $\mathcal{P}_t$); occlusion handling undefined |
| Q14 | ? | Gauge/scale not mentioned; appearance field $f_t$ not in formal universe |
| Q15 | Add: $X_t = \mathcal{P}_t$ instantiation; Layer C latent extension; BO time-scale structure; $K_{\mathrm{act}} = \#\pi_0$ |

### §3.2 $k\_selection\_a\_free\_energy.md$ — Free Energy Candidate (a)

| Q | Verdict | Notes |
|---|---------|-------|
| Q1 | ✓ | No observation in free energy |
| Q2 | ✗ | **FAIL**: $F(K)$ defined on $\widetilde\Sigma^K_M$ — requires K as index into state space |
| Q3 | ✓ | $u$ soft field maintained |
| Q4 | ✗ | **FAIL**: $K$ is a state-space index, not a derived observable; $\mathcal{E}^*_K$ minimized over $\Sigma^K_M$ sub-manifold |
| Q5 | ✓ | No observation likelihood |
| Q6 | ? | Not addressed |
| Q7 | ? | Not addressed |
| Q8 | ? | Not addressed |
| Q9 | ✗ | No time-scale separation; static $F(K)$, no dynamics |
| Q10 | △ | $F(K) = E^*(K) - T S(K)$; entropy term present but $S(K)$ is combinatorial count (discrete), not basin volume in $\Sigma_M$ |
| Q11 | ✗ | **FAIL**: $K$ enters as state-space index into $\widetilde\Sigma^K_M$; not numerical truncation |
| Q12 | ✗ | No 3D support; 2D only |
| Q13 | ✗ | Monocular / no observation layer |
| Q14 | ? | Not addressed |
| Q15 | Redefine $F(K)$ on $\Sigma_M$: $F(K;\mathcal{P}) = -T\log Z_K(\mathcal{P})$ where $Z_K = \int_{\mathcal{B}_K} e^{-\mathcal{E}/T} D\tilde{u}$; replace combinatorial $S(K)$ with basin volume $S_{\mathrm{config}}(K;\mathcal{P}) = \log \mathrm{Vol}(\mathcal{B}_K(\mathcal{P}))$ |

**Summary verdict**: Q2, Q4, Q11 FAIL — the core definition is built on $\Sigma^K_M$. The structure is salvageable by replacing the K-field formulation with the single-field $\Sigma_M$ partition function. The thermodynamic logic is correct; the state space is wrong.

### §3.3 $k\_selection\_b\_kramers.md$ — Kramers Candidate (b)

| Q | Verdict | Notes |
|---|---------|-------|
| Q1 | ✓ | No observation layer |
| Q2 | △ | Barrier $\Delta E_{K' \to K'-1}^{(jk)}$ defined on K-field sub-manifold; saddle $u_s^{(jk)}$ is on $\Sigma^{K'}_M$, not $\Sigma_M$ |
| Q3 | ✓ | $u$ soft field at saddle and minimum |
| Q4 | △ | $K'$ used as state-space index in energy evaluation; should be that $K_{\mathrm{act}}$ is $\pi_0$ count |
| Q5 | ✓ | No observation likelihood |
| Q6 | ? | Boundary of formation implicit in saddle structure; not explicitly addressed |
| Q7 | ? | Not addressed |
| Q8 | △ | $\sigma$ behavior at K-jump mentioned in §11.2 (OP-0008 connection); not formalized as posterior |
| Q9 | △ | "MFPT cascade" implies time-scale separation but BO structure not explicit |
| Q10 | ✓ | K-selection via Kramers kinetics, not energy minimization |
| Q11 | △ | $K_{\mathrm{field}}$ as cap acknowledged; but saddle computation done on K-field sub-manifold |
| Q12 | ✗ | No 3D support; 2D graph only |
| Q13 | ✗ | No observation layer |
| Q14 | ? | Not addressed |
| Q15 | Replace saddle definition: from $\Sigma^{K'}_M$ saddle to $\Sigma_M$ saddle; add $\mathcal{P}$-conditioning to all barrier computations; already done in `stereo_observation_framework.md` §6 |

**Summary verdict**: Mostly solid; the saddle geometry is the main issue (defined on K-field sub-manifold rather than $\Sigma_M$). Salvageable with §6 of `stereo_observation_framework.md` extension.

### §3.4 $k\_selection\_mechanism.md$ — Three Candidates Overview

| Q | Verdict | Notes |
|---|---------|-------|
| Q2 | △ | Candidate (a) and (b) use K-field sub-manifolds; candidate (c) does not presuppose K directly (automorphism-stabilizer approach) |
| Q10 | ✓ | All three candidates explicitly reject energy-minimization-only selection |
| Q15 | Candidate (c) stabilizer approach is the most K-presupposition-free; candidates (a) and (b) need $\Sigma_M$ reformulation |

### §3.5 $n1\_kramers\_extension.md$ — N-1 ↔ Kramers Bridge

| Q | Verdict | Notes |
|---|---------|-------|
| Q2 | ✓ | No K presupposition; barrier asymmetry is between birth and merger events |
| Q3 | ✓ | $u$ is primitive; barriers computed from $\mathcal{E}_{\mathrm{SCC}}$ |
| Q9 | △ | N-1 asymmetry implies time-scale separation but BO not explicit |
| Q10 | ✓ | Asymmetric Kramers rates → kinetic selection |
| Q15 | Add BO §5 structure: N-1 asymmetry = $T \to 0$ limit of BO-reduced $\Gamma^{K \to K+1} / \Gamma^{K \to K-1}$. Already done in `stereo_observation_framework.md` §6.3 |

**Summary verdict**: Good. Already the most aligned with new framework.

### §3.6 $pre\_objective\_K\_field\_tension.md$ — OP-0009-Pre

| Q | Verdict | Notes |
|---|---------|-------|
| Q2 | △ | Path A+C quotient approach acknowledges $K$-presupposition but uses unordered configuration space $\widetilde\Sigma^K_M / S_{K_{\mathrm{field}}}$ as resolution — still parameterized by $K_{\mathrm{field}}$ |
| Q11 | △ | Recognizes the tension but resolves via quotient, not via $\Sigma_M$ |
| Q15 | New resolution: $\Sigma_M$ is the ontologically primary state space; $\Sigma^K_M$ is a local chart for the $K$-basin $\mathcal{B}_K \subset \Sigma_M$; quotient is unnecessary if we adopt $\Sigma_M$ from the start |

### §3.7 $layered\_ambient\_architecture\_candidate.md$

| Q | Verdict | Notes |
|---|---------|-------|
| Q1 | ✓ | No observation layer assumed |
| Q2 | △ | Three layers are I9 K-field / I9' shared-pool / topological count — all still parameterized by $K_{\mathrm{field}}$ |
| Q4 | △ | Correctly distinguishes unlabelled topological count vs labelled active count; but uses $\Sigma^K_M$ as ambient |
| Q11 | ✗ | $K_{\mathrm{field}}$ appears in all three layers as architectural cap; not numerical truncation |
| Q15 | Replace ambient $\widetilde\Sigma^K_M$ with $\Sigma_M$; keep layer decomposition concept (useful); reinterpret $K_{\mathrm{field}}$-indexed layers as local charts within $\Sigma_M$ |

---

## §4. SCC 4-Energy / CN5 Re-examination

### §4.1 The four terms as prior components

Each energy term under the new framework:

**$E_{\mathrm{cl}} = \|(I-P)\tilde{u}\|^2$** (closure energy)

- Role in new framework: measures how far $\tilde{u}$ deviates from its relationally completed form $P\tilde{u}$.
- Bayesian interpretation: $P(\tilde{u}) \propto \exp(-\lambda_{\mathrm{cl}} E_{\mathrm{cl}})$ is a Gaussian prior on $\tilde{u} - P\tilde{u}$ (pulling $\tilde{u}$ toward closure-fixed-point).
- Layer D: pure prior. No observation dependence. **CONFIRMED as prior.**
- Continuum limit on $\mathcal{P}_t$: $E_{\mathrm{cl}} \approx \epsilon^2 \int_{\mathcal{P}_t} |\nabla_{\mathcal{P}_t}\tilde{u}|^2 dA$ (Laplace-Beltrami; graph Laplacian $L$ approximates $-\Delta_{S_t}$). This is the Dirichlet energy on the visible surface.

**$E_{\mathrm{sep}} = \sum_j \sum_{x \in X} u^{(j)}(x) D(x; 1 - u^{(j)})$ (separation energy in K-field form)** 

- In single-field $\Sigma_M$: $E_{\mathrm{sep}}$ is the $u$-weighted mean distinction $D(x; 1-u)$ — measures how much high-$u$ regions are distinguished from their complement.
- Layer D: pure prior. Creates the drive toward well-separated distinct components. **CONFIRMED as prior.**
- Creates metastable basin structure: high $\lambda_{\mathrm{sep}}$ increases barrier height between $K$-basins.
- Generates effective repulsion between components via high-$u$ region separation.

**$E_{\mathrm{bd}} = 2\alpha u^T L u$** (boundary energy)

- Layer D: pure prior. Measures total "surface area" of the transition layer (Dirichlet form).
- Bayesian interpretation: regularizes $\tilde{u}$ toward smooth fields; penalizes rough boundaries.
- Continuum: $E_{\mathrm{bd}} \approx \alpha \int_{\mathcal{P}_t} |\nabla_{\mathcal{P}_t}\tilde{u}|^2 dA$ — same as $E_{\mathrm{cl}}$ in continuum limit. The two terms are mathematically related but conceptually independent (CN5).
- **CONFIRMED as prior.**

**$E_{\mathrm{tr}}$ (transport energy)**

- Original role: temporal coherence prior — penalizes deviation from the transported previous field.
- Layer ambiguity: if $E_{\mathrm{tr}} = \|u_t - M_{t-1 \to t}^* u_{t-1}\|^2$ (deviation from transported predecessor), this is a **prior** on temporal consistency — Layer D.
- However: if the transport $M_{t-1 \to t}$ depends on observed image features ($\varphi(x) = f_t(x)$), then the realization mixes Layer A (observation) into Layer D (prior). This is a CN5 violation risk.
- **Assessment**: The transport kernel axioms (E1-E4) are pure field-level; the *realization* using external features $\varphi$ mixes layers.
- **Minimum modification**: Separate the transport prior (D) from the transport likelihood ($E_{\mathrm{tr,obs}}$, Layer E). Pure transport prior: $E_{\mathrm{tr}}^{\mathrm{prior}} = \|u_t - P^*(G_t, G_{t-1}) u_{t-1}\|^2$ where $P^*(G_t, G_{t-1})$ depends only on graph structure, not image features.

### §4.2 Photometric term placement

**Claim**: $E_{\mathrm{photo}}$ (photometric consistency) must be in $\mathcal{L}_{\mathrm{obs}}$ (Layer E), not $\mathcal{E}_{\mathrm{SCC}}$ (Layer D).

**Argument**:
1. $E_{\mathrm{photo}}$ depends on $f_L$, $f_R$, $\Pi_{LR}$ — all Layer A quantities.
2. A prior $P(\tilde{u})$ should be independent of the specific observation $\mathfrak{O}_t$. $E_{\mathrm{photo}}$ depends on $\mathfrak{O}_t$ directly.
3. Adding $E_{\mathrm{photo}}$ to $\mathcal{E}_{\mathrm{SCC}}$ would make the prior observation-dependent — this destroys the Bayesian structure (prior must be independent of likelihood).
4. CN5 says the four terms address "logically independent structural requirements." Photometric consistency is not a structural requirement of cohesion; it is an observation constraint.

**Verdict**: $E_{\mathrm{photo}}$ in Layer E (likelihood). **CN5 preserved.**

### §4.3 Was CN5 previously violated?

In the current canonical theory (2D pixel SCC without stereo), there is no $E_{\mathrm{photo}}$ term, so CN5 is not violated. The risk of violation arises only when adding observation terms to the energy — which the new framework explicitly prevents by the prior/likelihood separation.

**The transport energy realization risk**: if $E_{\mathrm{tr}}$ in practice uses image features $\varphi(x) = (u(x), \mathrm{Cl}(u)(x), D(x;1-u), \mathbf{C}(x,x))$ as transport cost features, and these depend only on $u_t$, then Layer D is maintained. If they depend on $f_t$ (image intensity), Layer A contaminates Layer D. **This should be explicitly checked.**

### §4.4 CN5 re-statement under new framework

$$\mathcal{E}_{\mathrm{SCC}}[\tilde{u}] = E_{\mathrm{cl}}[\tilde{u}] + E_{\mathrm{sep}}[\tilde{u}] + E_{\mathrm{bd}}[\tilde{u}] + E_{\mathrm{tr}}[\tilde{u}, \tilde{u}_{t-1}]$$

All four terms depend only on the soft field $\tilde{u}$ (and its predecessor $\tilde{u}_{t-1}$ for transport) and the graph structure $G_t = (\mathcal{P}_t, E_t^{3D})$ — never on raw image data $\mathfrak{O}_t$.

The stereo photometric term:

$$\mathcal{L}_{\mathrm{obs}}[\mathfrak{O}_t \mid \tilde{u}] = \lambda_{\mathrm{photo}} \sum_{x_L \in \mathrm{dom}(b_t)} c(x_L) \cdot \Psi(f_L(x_L), f_R(\Pi_{LR}(x_L)), \tilde{u}(b_t(x_L)))$$

is in $\mathcal{L}_{\mathrm{obs}}$ (Layer E). **CN5 holds.**

---

## §5. K-field Architecture Critique

### §5.1 Where K-field violates the canonical promise

The canonical promise is "soft → crisp": the theory moves from the soft cohesion field to crisp object-level structure, not the other way. The K-field architecture ($\Sigma^K_M$) violates this in the following specific ways:

**Violation 1: $K$ presupposed in state space definition.**
$\Sigma^K_M = \bigsqcup_{j=1}^{K_{\mathrm{field}}} \Sigma_{m_j}$ requires specifying $K_{\mathrm{field}}$ before the dynamics begin. $K_{\mathrm{field}}$ is an object-level count (how many formations) imposed at the theory level. The theory should derive $K_{\mathrm{act}}$; instead, K-field imports it as an architectural constant. This is OP-0009-Pre.

**Violation 2: Per-field sub-manifolds $\Sigma_{m_j}$ impose formation identity.**
The decomposition $\mathbf{u} = (u^{(1)}, \ldots, u^{(K_{\mathrm{field}})})$ assigns a numerical identity $j$ to each formation before dynamics. The formation's identity (which slot $j$ it occupies) is architecturally assigned, not emergent. This imports object-level individuation into the foundational structure.

**Violation 3: Saddle-point geometry on $\Sigma^K_M$ vs. $\Sigma_M$.**
In `k_selection_b_kramers.md`, barriers are computed between K-field sub-manifold minima. The saddle $u_s^{(jk)}$ lives on $\Sigma^{K'}_M$. In $\Sigma_M$, the saddle between the $K'$-basin and the $(K'-1)$-basin is a different object — it lives on $\Sigma_M$ itself, not on any sub-manifold. The K-field barrier is an approximation to the $\Sigma_M$ barrier; the approximation quality is unknown.

**Violation 4: Inter-field repulsion $\lambda_{\mathrm{rep}} \langle u^{(j)}, u^{(k)} \rangle$ is an artificial coupling.**
This term is introduced to prevent formation overlap in the K-field architecture. In $\Sigma_M$, formation overlap is naturally handled by the phase separation structure of $E_{\mathrm{sep}}$ (which drives components apart). The $\lambda_{\mathrm{rep}}$ term is an architectural artifact.

### §5.2 What K-field architecture gets right

Despite these violations, K-field has genuine strengths that must be preserved:

- **Numerical tractability**: Optimizing $K$ decoupled sub-problems is far easier than searching $\Sigma_M$ directly.
- **K-jump tracking**: The active-set $A \subseteq \{1, \ldots, K_{\mathrm{field}}\}$ provides a concrete way to track formation emergence/disappearance.
- **T-L1-F foundation**: The Hard-Bar / Active-Count Bridge (Cat A conditional, CV-1.5.2) is proved on $\widetilde\Sigma^K_M$ (shared-pool); this proof does not transfer immediately to $\Sigma_M$.

### §5.3 Resolution: K-field as local chart

The correct reinterpretation:

$$\Sigma^K_M \;\cong\; \text{local coordinate chart for the K-basin } \mathcal{B}_K \subset \Sigma_M$$

Specifically: in a neighborhood of a metastable $K$-component configuration $u^*_K \in \Sigma_M$ with $K_{\mathrm{act}}(u^*_K) = K$, we can introduce $K$ "formation coordinates" $(u^{(1)}, \ldots, u^{(K)})$ where $u^{(j)} = u \cdot \mathbf{1}_{C_j}$ (restriction to component $j$'s support $C_j$). This is a local chart on $\Sigma_M$ near the $K$-basin minimum, not a global state space.

In this reading:
- $K_{\mathrm{field}}$ = the maximum $K$ for which we maintain a chart (numerical truncation).
- $K_{\mathrm{act}}$ = $\#\pi_0(\{x : u(x) > \varepsilon\})$ derived from $u \in \Sigma_M$.
- T-L1-F proof applies within each chart (L1-J regime $\Leftrightarrow$ chart non-degeneracy conditions).

### §5.4 Shared-pool vs K-field

The shared-pool $\widetilde\Sigma^K_M$ (variable $K_{\mathrm{act}}$ within $K_{\mathrm{field}}$ cap) is closer to the correct structure: it allows $K_{\mathrm{act}}$ to vary from 0 to $K_{\mathrm{field}}$ within a single optimization. This is the correct direction. The residual issue: $K_{\mathrm{field}}$ still enters as an architectural parameter.

**Under $\Sigma_M$**: $K_{\mathrm{field}}$ does not appear. $K_{\mathrm{act}}$ ranges freely over $\mathbb{N}_0$, bounded in practice by $|\mathcal{P}_t|$. The shared-pool manifold is the $K \leq K_{\mathrm{field}}$ sub-union of K-basins, which is a proper sub-region of $\Sigma_M$.

---

## §6. P-F Framework Re-positioning

### §6.1 Two-level stochastic structure

The P-F framework applies at two distinct levels:

**Level 1 — Field-level stochastic dynamics (Langevin on $\Sigma_M$):**

$$d\tilde{u} = -\nabla_{\tilde{u}} \mathcal{E}_{\mathrm{SCC}}[\tilde{u};\mathcal{P}_t]\, dt + \sqrt{2T}\, dW_t$$

This is the SCC gradient flow plus noise. The Fokker-Planck equation for the density $\rho_t(\tilde{u})$ over $\Sigma_M$:

$$\frac{\partial \rho_t}{\partial t} = \nabla_{\tilde{u}} \cdot \left(\rho_t \nabla_{\tilde{u}} \mathcal{E}_{\mathrm{SCC}} + T \nabla_{\tilde{u}} \rho_t\right)$$

Stationary distribution: $\rho_{\mathrm{eq}}(\tilde{u}) \propto \exp(-\mathcal{E}_{\mathrm{SCC}}[\tilde{u}]/T)$.

**P-F flag**: This level is **undefined in current canonical SCC**. The noise $T$ and the measure $D\tilde{u}$ on $\Sigma_M$ have no canonical definition. All claims at this level require P-F flag.

**Level 2 — Coarse-grained K-level master equation:**

$$\frac{d}{dt} P(K, t) = \sum_{K'} \left[\Gamma^{K' \to K}(\mathcal{P}_t) P(K', t) - \Gamma^{K \to K'}(\mathcal{P}_t) P(K, t)\right]$$

This is the adiabatically reduced dynamics after integrating out the fast field variable $\tilde{u}$. The Kramers rates $\Gamma^{K \to K'}$ bridge Level 1 and Level 2.

**P-F flag**: Also undefined; depends on Level 1 stochastic formalization.

### §6.2 Kramers theory as bridge

Kramers rate theory provides the explicit formula connecting Level 1 to Level 2:

$$\Gamma^{K \to K'}(\mathcal{P}) = A_{K \to K'}(\mathcal{P}) \exp\!\left(-\frac{\Delta \mathcal{E}^{K \to K'}_{\mathrm{barrier}}(\mathcal{P})}{T}\right)$$

The barrier $\Delta \mathcal{E}^{K \to K'}_{\mathrm{barrier}}$ is a Level 1 quantity (saddle point on $\Sigma_M$); the rate $\Gamma^{K \to K'}$ is a Level 2 quantity.

### §6.3 MFPT: three distinct quantities

MFPT appears in three different contexts; confusing them is a persistent error:

| MFPT type | Formula | Layer | OP |
|-----------|---------|-------|-----|
| $\tau_{K \to K'}$: K-basin escape time | $1 / \Gamma^{K \to K'}(\mathcal{P})$ | G | OP-0005 |
| $\tau_{\mathrm{persist}}$: formation temporal persistence time | Time until $\mathrm{Persist}(\tilde{u}_t, \tilde{u}_{s}) < \theta_{\mathrm{persist}}$ | D + G | OP-0012 |
| $\tau_{\mathrm{transport}}$: transport kernel uncertainty time | Time until $M_{t \to s}^*$ becomes unreliable due to scene change | D + C | OP-0011 |

These are NOT the same quantity. Prior work (k_selection_b_kramers.md §4.4 "MFPT cascade") partially conflates them.

### §6.4 P-F framework impact on OPs

| OP | P-F blocks what | What stochastic extension would provide |
|----|----------------|----------------------------------------|
| OP-0005 | $F(K;\mathcal{P})$ cannot be computed without $T$ and $D\tilde{u}$ defined | Langevin on $\Sigma_M$ → partition function $Z_K$ → $P_{\mathrm{eq}}(K)$ |
| OP-0008 | $\sigma^A$ posterior at K-jump requires stochastic path integral over transition event | Kramers path distribution → conditional $P(\sigma' \mid \mathrm{event})$ |
| OP-0011 | Transport kernel uniqueness: without stochastic formulation, transport axioms E1-E4 may have multiple realizations with no natural selection | Stochastic optimal transport on $\Sigma_M$ → natural entropy-regularized unique solution |
| OP-0012 | Persistence composition requires bounding multi-step transport uncertainty | Stochastic bound on $\|M_{t_1 \to t_2} \circ M_{t_2 \to t_3} - M_{t_1 \to t_3}\|$ |

### §6.5 P-F Axiom v0 (formal statement)

> **Proposed P-F Axiom (v0):** *No canonical claim concerning metastable equilibrium distributions, Kramers escape times, effective free energies $F(K;\mathcal{P})$, K-level transition rates $\Gamma^{K \to K'}$, or formation persistence times in the stochastic sense may be asserted as Category A or B until the following are canonically defined:*
> *(i) a Langevin process on $\Sigma_M$ with noise temperature $T > 0$;*
> *(ii) a well-defined measure $D\tilde{u}$ on $\Sigma_M$ (Riemannian volume form or equivalent);*
> *(iii) the existence and uniqueness of the stationary distribution $\rho_{\mathrm{eq}} \propto \exp(-\mathcal{E}_{\mathrm{SCC}}/T)$ on $\Sigma_M$.*
> *Until these are established, all such claims are Category C at best, with explicit P-F flag.*

This makes the P-F framework operational rather than ad-hoc. CV-1.7 Axiom Group G candidate.

---

## §7. $k\_selection\_a\_free\_energy.md$ Detailed Verification

### §7.1 Is $F(K)$ in the existing document a true free energy?

**Partial answer.** The document defines:

$$F(K) = \mathcal{E}^*_K - T \cdot S(K)$$

where:
- $\mathcal{E}^*_K = \min_{\mathbf{u} \in \widetilde\Sigma^K_M, K_{\mathrm{act}}=K} \mathcal{E}_K(\mathbf{u})$ — energy minimum within K-field sub-manifold.
- $S(K) = \log|\{\text{inequivalent K-formation minimizers}\}|$ — discrete count of symmetry-inequivalent minimizers.

**Problems:**

(P1) $\mathcal{E}^*_K$ is the **ground state energy** within $\Sigma^K_M$, not the free energy. True free energy requires integrating over the entire basin, not just the minimum.

(P2) $S(K)$ is a **discrete combinatorial count** (number of inequivalent minimizers). True configurational entropy requires the basin volume in $\Sigma_M$ (continuous measure). The discrete count is a crude approximation.

(P3) The exponential weight $e^{-\mathcal{E}/T}$ is not used; the document uses $F = E^* - TS$ directly. This is the **saddle-point / Laplace approximation** of the true free energy. It is valid only when $T$ is small relative to energy curvatures. The approximation is not stated.

(P4) No $\mathcal{P}$-dependence. The geometry of the point cloud $\mathcal{P}_t$ affects both $\mathcal{E}^*_K$ (through the adjacency graph $G_t$) and $S(K)$ (through the possible component configurations). Both should be $\mathcal{P}$-conditional.

### §7.2 Correspondence with new $F(K;\mathcal{P})$

$$F(K;\mathcal{P}) = -T\log Z_K(\mathcal{P}) = -T \log \int_{\mathcal{B}_K(\mathcal{P})} \exp\!\left(-\frac{\mathcal{E}_{\mathrm{SCC}}[\tilde{u};\mathcal{P}]}{T}\right) D\tilde{u}$$

Under Laplace approximation around the basin minimum:

$$Z_K(\mathcal{P}) \approx \exp\!\left(-\frac{\mathcal{E}^*(K;\mathcal{P})}{T}\right) \cdot \frac{(2\pi T)^{(n-1)/2}}{\sqrt{\det H_{\min,K}(\mathcal{P})}}$$

$$F(K;\mathcal{P}) \approx \mathcal{E}^*(K;\mathcal{P}) - \frac{(n-1)T}{2}\log(2\pi T) + \frac{T}{2}\log \det H_{\min,K}(\mathcal{P})$$

So: $S_{\mathrm{config}}(K;\mathcal{P}) = \frac{n-1}{2}\log(2\pi T e) - \frac{1}{2}\log\det H_{\min,K}(\mathcal{P})$.

The existing $S(K)$ (discrete count) is a crude proxy for $-\frac{1}{2}\log\det H_{\min,K}$ (Hessian-entropy). The Hessian determinant is computable from existing `energy.py` + `optimizer.py` code. This is **OQ-1** from the daily log (NQ-ST-1).

### §7.3 Can stereo geometry enter $F(K;\mathcal{P})$?

Yes. The dependence on $\mathcal{P}$ enters through:
- $\mathcal{E}^*(K;\mathcal{P})$: the K-basin minimum energy, which depends on the adjacency graph $G_t = (\mathcal{P}_t, E_t^{3D})$.
- $H_{\min,K}(\mathcal{P})$: the Hessian at the minimum, which depends on $G_t$.
- $\mathcal{B}_K(\mathcal{P})$: the basin itself changes with $\mathcal{P}$ (depth changes split or merge depth-separated components).

Stereo depth directly affects $E_t^{3D}$ (depth-filtered adjacency), which changes the SCC energy landscape and hence $F(K;\mathcal{P})$. Two formations that are adjacent in 2D but depth-separated will have a higher barrier $\Delta\mathcal{E}^{K \to K-1}(\mathcal{P})$ — meaning stereo depth provides formation stability evidence.

### §7.4 Is $F(K;\mathcal{P})$ sufficient to resolve OP-0005?

**No.** Even with the correct partition function, OP-0005 requires:
- (i) A mechanism for selecting $K_{\mathrm{act}}$ from $\{1, \ldots, K_{\mathrm{field}}\}$ — $P_{\mathrm{eq}}(K|\mathcal{P})$ gives equilibrium probabilities, not a deterministic selection rule.
- (ii) A protocol for how initial conditions ($u_0$) determine which basin is reached — this is CN15 (initial conditions matter).
- (iii) The stochastic extension (P-F flag) to define $Z_K$.

$F(K;\mathcal{P})$ gives **equilibrium K statistics** (which K is most likely at thermal equilibrium), not the **dynamical selection rule** (which K will $\tilde{u}_t$ be in at time $t$ given $u_0$). These are related (by $P_{\mathrm{eq}}$) but not identical in finite-time dynamics.

---

## §8. Boundary Theory Re-examination

### §8.1 Current definition and its weakness

Current canonical boundary: $B_t = \{x : D_t(u_t)(x) > \theta\}$ for threshold $\theta$ (§5 of canonical.md). This is a threshold-based definition with the following weaknesses:

- $\theta$ is a free parameter; different $\theta$ give different boundaries. No canonical choice of $\theta$.
- Under scale change (image zoom), the intensity values change but the true boundary does not; threshold-based boundary is not gauge/scale invariant.
- $D_t$ measures exterior asymmetry at site $x$; a high $D_t$ value means $x$ is significantly different from the exterior. But this is a single-site property, not a global boundary condition.
- Threshold boundaries are crisp by construction — they output a binary mask. This conflates Layer F (topological observables) with Layer A (crisp image edges).

### §8.2 Better definitions under the new framework

**Definition 1 — Gradient ridge:**

$$B_t = \bigl\{x \in \mathcal{P}_t : |\nabla_{\mathcal{P}_t} \tilde{u}_t(x)| \text{ is a local maximum along the gradient direction}\bigr\}$$

This is the gradient magnitude ridge of $\tilde{u}_t$. Properties:
- Scale-equivariant: if $\tilde{u}$ is scaled, the ridge location is unchanged.
- Threshold-free: no free parameter.
- Connected to Canny edge detection (2D analogue).

**Definition 2 — Persistent transition layer:**

$$B_t = \bigl\{x \in \mathcal{P}_t : \exists \epsilon > 0 \text{ s.t. } x \in \{u > \theta_1\} \setminus \{u > \theta_2\} \text{ for all } \theta_1 < \theta_{\mathrm{edge}} < \theta_2 \text{ in an interval of width } \epsilon\bigr\}$$

The persistent transition layer is the set of sites that remain in the "boundary zone" across a range of threshold levels — this is precisely a persistence-diagram concept ($H_0$ generators with lifetime $> \epsilon$).

**Definition 3 — Depth discontinuity:**

In the stereo setting, depth discontinuities in $\mathcal{P}_t$ (from $E_t^{3D}$ construction) mark physical scene boundaries. These are NOT boundaries of $\tilde{u}_t$ but boundaries of the *support space*:

$$\partial\mathcal{P}_t = \{b_t(x_L) : |z(x_L) - z(y_L)| \geq \delta_z \text{ for some neighbor } y_L\}$$

This is a Layer B quantity (geometry of the visible reconstruction), distinct from the Layer F boundary $B_t$ of the soft field $\tilde{u}_t$. Confusing them is a Layer B/F conflation error.

### §8.3 Layer assignments

| Boundary concept | Layer | Definition quality |
|-----------------|-------|-------------------|
| $D_t$-threshold boundary (current canonical) | F (but poorly defined) | Weak: threshold-dependent, scale-sensitive |
| Gradient ridge of $|\nabla_{\mathcal{P}_t}\tilde{u}_t|$ | F | Better: threshold-free, scale-equivariant |
| Persistent transition layer ($H_0$ persistence) | F | Best: topologically grounded, threshold-free |
| Depth discontinuity $\partial\mathcal{P}_t$ | B | Different concept: support boundary, not field boundary |
| Image edge (pixel-level) | A | Should not be in SCC theory directly |

**OP-0006 reframing**: Boundary precision OP-0006 should be resolved by adopting Definition 2 (persistent transition layer) as the canonical boundary definition, replacing the current threshold-based $B_t$.

---

## §9. $\sigma$-Signature / Label Inheritance Re-examination

### §9.1 $\sigma$ as static vs dynamic

The $\sigma$-signature is currently defined as a static quantity: $\sigma(u^*)$ at a minimizer $u^*$ (Commitment 14; T-σ-Lemma-1/2/3 + T-σ-Theorem-3). It is an $\mathrm{Aut}(G)$-invariant label of the minimizer's symmetry class.

**Static $\sigma$ (Layer F, static):** $\sigma(u^*) = $ irrep of $\mathrm{Aut}(G)$ acting on the Hessian tangent space at $u^*$. Well-defined. Cat A for single-formation case.

**Dynamic $\sigma$ trajectory (Layer F+G):** Under gradient flow, $\tilde{u}_t$ evolves; $\sigma(\tilde{u}_t)$ may change when $\tilde{u}_t$ crosses a bifurcation or undergoes a K-jump. The trajectory $\sigma(t)$ is a Layer G object (depends on slow dynamics).

### §9.2 $\sigma^A$ at K-jump

OP-0008 asks: after a K-jump ($K \to K-1$, two formations merge), what $\sigma^A$ does the surviving formation inherit?

**Current status**: non-deterministic (OP-0008 OPEN HIGH). The merged formation's $\sigma$ depends on which formations merged (which pair $(j,k)$), the saddle geometry, and the post-saddle relaxation path.

**New framework (P8 from `stereo_observation_framework.md`):**

The saddle field $u_{\mathrm{saddle}}^{(jk)}$ has a definite $\sigma$-structure (its symmetry group is determined by the graph geometry and formation positions). The post-saddle descent to $u_{\min,K-1}$ determines $\sigma^A_{\mathrm{after}}$ deterministically given the saddle.

But the Kramers transition is **stochastic** — the noise $dW_t$ in the Langevin dynamics determines which of the available saddles is crossed first. Hence:

$$\sigma^A_{\mathrm{after}} \sim P(\sigma' \mid \text{Kramers transition event via pair }(j,k))$$

This is a conditional posterior, where the conditioning event is "the Langevin path crossed saddle $(j,k)$ first."

**Is $\sigma^A$ deterministic given the saddle?** Yes — if we condition on which saddle is crossed, $\sigma^A_{\mathrm{after}}$ is deterministically given by the saddle's symmetry structure and the post-saddle gradient descent. The non-determinism is in *which saddle* is crossed first (controlled by Kramers rates $\Gamma^{K \to K-1}_{jk}$).

### §9.3 $\sigma^A$ and formation transport

At a K-jump ($K \to K-1$ via merger of formations $j$ and $k$):
- The surviving formation inherits the $\sigma$ of the merged state $u_{\min,K-1}$ (which may be a symmetry-broken version of the old $\sigma^{(j)}$ or $\sigma^{(k)}$).
- The transport kernel $M_{t \to t^+}$ (temporal transport across the jump event) maps $u_{\min,K}$ to $u_{\min,K-1}$ along the merger path.
- The $\sigma$-label of the resulting formation is determined by the symmetry of $u_{\min,K-1}$, not by either $\sigma^{(j)}$ or $\sigma^{(k)}$ individually.

This is the **$\sigma$-fusion rule**: $\sigma^A_{\mathrm{after}} = \sigma(u_{\min,K-1})$ where $u_{\min,K-1}$ is the post-merge basin minimum.

---

## §10. Transport Theory Re-examination

### §10.1 Three transport maps

Under the new framework, three distinct transport maps exist:

| Transport map | Domain | Codomain | Layer | Role |
|--------------|--------|----------|-------|------|
| $\Pi_{LR} : X_L \rightharpoonup X_R$ | Left pixels | Right pixels | A (observation) | Stereo epipolar correspondence |
| $b_t : X_L \rightharpoonup \mathcal{P}_t$ | Left pixels | 3D points | A → B (back-projection) | Depth reconstruction |
| $M_{t \to s} : \mathcal{P}_t \rightharpoonup \mathcal{P}_s$ | Visible 3D at $t$ | Visible 3D at $s$ | D (prior) or C (latent) | Temporal coherence / scene motion |

**Structural analogy (CN10 contrastive):** $\Pi_{LR}$ (spatial, A) and $M_{t \to s}$ (temporal, D) are both partial optimal transport maps. Their mathematical structure is identical — both solve regularized partial OT between measures. This contrastive parallel motivates a unified treatment but does NOT mean they are the same object.

### §10.2 Classification of existing transport energy $E_{\mathrm{tr}}$

$E_{\mathrm{tr}}[\tilde{u}_t, \tilde{u}_{t-1}; M_{t-1 \to t}] = \lambda_{\mathrm{tr}} \cdot d_{\mathrm{OT}}(\tilde{u}_t \cdot \mu, M_{t-1 \to t}^* (\tilde{u}_{t-1} \cdot \mu))$

where $d_{\mathrm{OT}}$ is an OT distance and $M_{t-1 \to t}^*$ is the pushforward.

**If $M_{t-1 \to t}$ is determined by graph structure alone** (adjacency-based OT cost): Layer D (pure prior).

**If $M_{t-1 \to t}$ is determined using image features $\varphi(x) = f_t(x)$**: Layer A contaminates Layer D — CN5 violation risk.

**If $M_{t-1 \to t}$ is the self-referential cohesion fingerprint** $\varphi(x) = (u(x), \mathrm{Cl}(u)(x), D(x;1-u), \mathbf{C}(x,x))$: Layer D maintained (features depend only on $\tilde{u}$, not on $\mathfrak{O}$).

**Current realization (canonical.md §9.4):** uses cohesion fingerprint — **Layer D maintained.** The self-referential realization is CN5-safe.

### §10.3 OP-0011 re-formulation

OP-0011 asks: is the transport kernel $M_{t \to s}$ unique? Under the new framework:

- Given $\mathcal{P}_t$, $\mathcal{P}_s$, and the SCC fields $\tilde{u}_t, \tilde{u}_s$, there are generally multiple transport plans satisfying E1-E4.
- Uniqueness requires either: (a) strict convexity of the OT cost (achieved by entropy regularization); (b) a canonical cost function derived from SCC structure.
- The entropy-regularized Sinkhorn realization provides existence and uniqueness given fixed regularization $\gamma$.

**Reframing**: OP-0011 is about the canonical choice of OT cost and regularization within the SCC prior. This is a Layer D question.

### §10.4 $\Pi_{LR}$ vs $M_{t \to s}$ — unification possibility

Both $\Pi_{LR}$ and $M_{t \to s}$ solve a partial OT problem:
- $\Pi_{LR}$ transports left pixel mass to right pixel mass, with photometric cost.
- $M_{t \to s}$ transports scene support mass from time $t$ to time $s$, with geometric cost.

A unified framework: both are instances of regularized partial OT on different support spaces with different cost functions. The difference is in their role (A vs D) and cost ($E_{\mathrm{photo}}$ vs $\mathcal{E}_{\mathrm{SCC}}$-derived). **This unification is a contrastive parallel, not an identification.**

---

## §11. Phase-Field / Physics Analogy Verification

### §11.1 Which analogies are structural vs mathematical

| Analogy | Type | Status | Notes |
|---------|------|--------|-------|
| $W(u) = u^2(1-u)^2$ ↔ $\phi^4$ double well | Mathematical | **Structural only**: $\phi^4$ has $W(\phi) = (\phi^2 - 1)^2 / 4$ near $\phi = \pm 1$; SCC double-well is $(0,1)$-valued, not $(-1,+1)$-valued; related by $u = (\phi+1)/2$ |
| $E_{\mathrm{cl}} + E_{\mathrm{bd}} \to $ Dirichlet energy on $\mathcal{P}_t$ | Mathematical | **Approximate identity** in continuum limit: $E_{\mathrm{cl}} \approx \epsilon^2 \int |\nabla_{S_t}\tilde{u}|^2 dA$ |
| Allen-Cahn on $S_t$ | Mathematical | **Approximate identity** for $\mathcal{E}_{\mathrm{SCC}}$ in continuum limit (see §9 of `stereo_observation_framework.md`) |
| Ginzburg-Landau / Modica-Mortola | Mathematical | **Structural**: $\Gamma$-convergence of $\int[\epsilon|\nabla u|^2 + W(u)/\epsilon]$ to perimeter → T-Merge (b) basis |
| Cahn-Hilliard | Structural only | **Wrong for SCC**: Cahn-Hilliard is conserved-phase PDE ($\partial_t u = -\Delta(\Delta u - W'(u))$); SCC uses gradient flow on $\Sigma_m$ (conserved mass) which is closer to Allen-Cahn with constraint |
| Mumford-Shah | Structural only | **Weaker analogy**: Mumford-Shah uses explicit sharp boundary variable $\Gamma$; SCC uses diffuse boundary encoded in $u$ itself; Ambrosio-Tortorelli regularization (uses auxiliary field $v \approx 0$ at boundary) is structurally closer to SCC |
| LSW coarsening $t^{1/3}$ | Mathematical | **Allen-Cahn 2D prediction**: $R(t) \sim t^{1/3}$; coarsening time $\tau \sim R^3$ for circular components. Applies to $\mathcal{P}_t$ in 2D surface limit. Discrepancy with empirical $\Delta t \propto t^{1.315}$ needs explanation |
| Kramers rate theory | Mathematical | **Structural identity**: Kramers (1940) + Hänggi-Talkner-Borkovec (1990) directly applicable to SCC energy landscape on $\Sigma_M$; this is a valid mathematical framework, not merely an analogy |

### §11.2 Mass conservation

SCC uses volume constraint $\Sigma_M = \{u : \sum u_i = M\}$. This is conservation of **cohesion mass** (not physical mass). In phase-field terms:
- Allen-Cahn: **non-conserved** order parameter ($\partial_t u = -\delta E/\delta u$, no conservation law).
- Cahn-Hilliard: **conserved** order parameter ($\partial_t u = \nabla^2(\delta E/\delta u)$, conserves $\int u$).

SCC gradient flow on $\Sigma_M$ is a **constrained Allen-Cahn equation** (non-conserved gradient flow projected onto the simplex face $\Sigma_M$). It conserves mass by projection, not by a divergence-form PDE. This is closer to Allen-Cahn + constraint than to Cahn-Hilliard.

**Canonical recommendation**: Use "constrained Allen-Cahn" as the descriptive name for the SCC dynamics; avoid "Cahn-Hilliard" which implies a different PDE structure.

### §11.3 Coarsening exponent discrepancy

Allen-Cahn 2D coarsening (area-law): $R(t) \sim t^{1/2}$, so $K(t) \sim t^{-1}$, $\tau(K \to K-1) \sim K^{-1}$. The time to merge two formations of size $R$ scales as $\tau \sim R^2/D$ (diffusion-limited).

SCC empirical: $\Delta t \propto t^{1.315}$ (Phase 10 V4) → merger time grows as $t^{1.315}$, suggesting faster-than-Allen-Cahn growth. The exponent $1.315 \approx 4/3$ is closer to the LSW Ostwald ripening exponent ($t^{1/3}$ for $R$, so $t$ for coarsening time would be cubic in $R$).

**Explanation candidates:**
- Closure operator raises barrier height ($O(\beta^{0.89})$ vs Allen-Cahn $O(\beta^{0.85})$) — this alone modifies the prefactor but not the exponent.
- 3D geometry effects: on a 2D surface $S_t$ in 3D, the effective dimensionality of diffusion changes.
- Mass-conserved constraint: the simplex constraint modifies the transport equation.

OQ-4 (from daily log): this discrepancy remains unresolved. **Treat empirical exponent as Cat B (working); Allen-Cahn analogy as contrastive only.**

---

## §12. Final Synthesis

### §12.1 Existing theory: maintain / modify / demote / discard

**MAINTAIN (no change needed):**
- $u_t : X_t \to [0,1]$ as SCC primitive (correctly foundational)
- CN5 4-term independence (correctly stated; sharpened by prior/likelihood separation)
- CN10 contrastive comparison (correctly stated)
- CN15 Static/Dynamic Separation (correctly stated; BO formalizes it)
- CN6 kinetic determination (correctly stated; BO gives it quantitative form)
- CN8 metastability (correctly stated)
- T-Merge (b) (Cat A; recovered as $T \to 0$ BO limit)
- T-L1-F Hard-Bar/Active-Count Bridge (Cat A conditional; layer A-agnostic)
- N-1 Soft-Hard Switching Asymmetry (correct; now = Kramers rate asymmetry)
- Diagnostic vector $\mathbf{d}$, predicate-energy bridge
- $\sigma$-signature static (Cat A; T-σ-Lemma-1/2/3 + T-σ-Theorem-3)
- Phase-field analogies (as contrastive comparisons; not identifications)

**MODIFY (minor adjustment needed):**
- Transport energy $E_{\mathrm{tr}}$: ensure realization uses only cohesion fingerprint (not raw image features); flag if otherwise
- $K_{\mathrm{act}}$ definition: from "active slot count" to "$\#\pi_0(\{u > \varepsilon\})$" — cleaner, K-field-independent
- Boundary band $B_t$: from threshold-based to persistence/gradient ridge definition (OP-0006 resolution path)
- Kramers rates in $k\_selection\_b\_kramers.md$: extend from $\Sigma^K_M$ saddle to $\Sigma_M$ saddle; add $\mathcal{P}$-conditioning
- $F(K)$ in $k\_selection\_a\_free\_energy.md$: extend from combinatorial entropy to Hessian-determinant entropy; add $\mathcal{P}$-conditioning
- $\sigma^A$ K-jump rule: from deterministic to conditional posterior $P(\sigma' \mid \text{Kramers event})$

**DEMOTE (remains valid but not foundational):**
- K-field architecture $\Sigma^K_M$: from foundational state space to local coordinate chart for $\mathcal{B}_K \subset \Sigma_M$
- Shared-pool $\widetilde\Sigma^K_M$: same demotion
- $K_{\mathrm{field}}$: from architectural parameter to numerical truncation constant for $\varepsilon$ calibration
- Layered ambient architecture: partially superseded; keep layer distinction concept; replace $\Sigma^K_M$ ambient with $\Sigma_M$
- Per-field repulsion $\lambda_{\mathrm{rep}} \langle u^{(j)}, u^{(k)} \rangle$: demote to architectural artifact of K-field; in $\Sigma_M$ it is unnecessary (phase separation handles it via $E_{\mathrm{sep}}$)

**DISCARD / REPLACE:**
- Threshold-based boundary $B_t = \{D_t > \theta\}$: replace with persistence/gradient ridge definition
- $F(K)$ on $\Sigma^K_M$ with discrete $S(K)$: replace with $F(K;\mathcal{P})$ on $\Sigma_M$ with Hessian entropy (subsumes the old definition as an approximation)

**NEW (not in existing canonical; promote to working):**
- $\mathcal{P}_t$ as 3D visible support (Layer B)
- $b_t : X_L \rightharpoonup \mathcal{P}_t$ back-projection (Layer A → B)
- $E_t^{3D}$ depth-aware adjacency (Layer B)
- $\mathcal{X}_t = (\mathcal{M}_t, \mu_t, U_t)$ latent scene (Layer C)
- Four-layer separation: $\mathfrak{O}_t$ / $\tilde{u}_t$ / prior $\mathcal{E}_{\mathrm{SCC}}$ / likelihood $\mathcal{L}_{\mathrm{obs}}$
- BO time-scale structure: $\tau_{\mathrm{frame}} \ll \tau_{\mathrm{fast}} \ll \tau_{\mathcal{P}} \lesssim \tau_{\mathrm{slow}}$
- $Z_K(\mathcal{P})$ partition function, $F(K;\mathcal{P})$, $P_{\mathrm{eq}}(K|\mathcal{P})$
- P-F Axiom v0

### §12.2 OP Re-interpretation Table

| OP | Previous framing | New framing under stereo-SCC | Status change |
|----|-----------------|------------------------------|--------------|
| OP-0005 K-Selection | Missing mechanism for $K_{\mathrm{act}}$ | $F(K;\mathcal{P}) = -T\log Z_K(\mathcal{P})$ → $P_{\mathrm{eq}}(K|\mathcal{P})$; Kramers rates give dynamics | OPEN; structural path formalized |
| OP-0006 Boundary precision | Threshold-based $B_t$ imprecise | $B_t$ = persistent transition layer / gradient ridge of $|\nabla_{\mathcal{P}_t}\tilde{u}_t|$ | OPEN; clear resolution candidate |
| OP-0008 $\sigma^A$ non-determinism | Label assignment non-deterministic | $P(\sigma' \mid \text{Kramers event}(j,k))$; saddle geometry determines $\sigma^A_{\mathrm{after}}$ | OPEN; posterior formulation proposed |
| OP-0009-Pre K-field tension | K-field imports object-like K | $\Sigma_M$ is foundational; $\Sigma^K_M$ is local chart; $K_{\mathrm{act}} = \#\pi_0$ derived | OPEN; resolution path clearest yet |
| OP-0009-K K status | What is K? | $K_{\mathrm{field}}$ = truncation; $K_{\mathrm{act}} = \#\pi_0$ on $\Sigma_M$ | RESOLVED (Commitment 16) + reinforced |
| OP-0009-A Architecture choice | I9 vs I9' | Both are coordinate charts on $\Sigma_M$; not competing architectures | OPEN; reframed |
| OP-0009-λ $\lambda_{\mathrm{rep}}$ ontology | 5th energy term? | In $\Sigma_M$ formulation, $\lambda_{\mathrm{rep}}$ is unnecessary (phase separation handles it) | OPEN; lean toward resolution |
| OP-0011 Transport uniqueness | Multiple $M_{t \to s}$ realizations | Entropy-regularized Sinkhorn gives canonical unique solution given cost; cost choice is the open sub-problem | OPEN; reframed as cost-choice question |
| OP-0012 Persistence composition | Multi-step transport error bounds | Level G: bounds on composition of Kramers transition paths | OPEN; reformulated at correct level |
| OP-0021 Stochastic dynamics | Thermal fluctuations undefined | Langevin on $\Sigma_M$ is precisely the Level 1 stochastic SCC; P-F Axiom v0 makes this the prerequisite for all G-layer claims | OPEN; central unblocking problem |

### §12.3 Definitions ready for canonical consideration

The following definitions are sufficiently precise to be candidates for canonical integration (subject to further audit):

**D-candidate-1**: State space $\Sigma_M = \{u \in [0,1]^n : \sum_x u(x) = M\}$ as the foundational single-field state space; $K_{\mathrm{act}}(u) = \#\pi_0(\{x : u(x) > \varepsilon\})$ as the canonical derived formation count.

**D-candidate-2**: Back-projection $b_t : X_L \rightharpoonup \mathcal{P}_t$, $b_t(x_L) = z(x_L) K_{\mathrm{cam}}^{-1}[u_L, v_L, 1]^T$; depth-aware adjacency $E_t^{3D} = \{(b_t(x), b_t(y)) : (x,y) \in E_t^{2D}, |z(x) - z(y)| < \delta_z\}$ (both as modeling-layer choices, not canonical axioms).

**D-candidate-3**: Four-layer Bayesian separation: prior $P(\tilde{u}) \propto \exp(-\mathcal{E}_{\mathrm{SCC}}[\tilde{u}])$ with exactly four energy terms; likelihood $P(\mathfrak{O}_t|\tilde{u})$ contains all observation-dependent terms including $E_{\mathrm{photo}}$.

**D-candidate-4**: Boundary definition: $B_t = \{x \in \mathcal{P}_t : |\nabla_{\mathcal{P}_t}\tilde{u}_t(x)|$ is a local maximum along gradient direction$\}$ OR the persistent transition layer from $H_0$ persistence.

**D-candidate-5**: P-F Axiom v0 (as stated in §6.5 above).

All five are working-level proposals; none are ready for direct canonical promotion without Critic audit and (for D-candidate-5) proof of stochastic formalization feasibility.

### §12.4 Claims requiring proof or experiment

| Claim | Type | What's needed |
|-------|------|--------------|
| $\Sigma_M$ saddle geometry = K-field saddle + correction | Analytical | Derive the relationship between $\Sigma_M$ saddle and $\Sigma^K_M$ saddle; quantify approximation error |
| $S_{\mathrm{config}}(K;\mathcal{P}) \approx -\frac{1}{2}\log\det H_{\min,K}(\mathcal{P})$ (Laplace approx) | Numerical | Compute $\det H$ at K-basin minima on R23 dataset; compare to empirical basin volumes |
| Stereo depth separation increases K-barrier height | Numerical | Show $\Delta\mathcal{E}^{K \to K-1}(\mathcal{P})$ increases when depth discontinuity separates two formations |
| Coarsening exponent $\Delta t \propto t^{1.315}$ ≠ Allen-Cahn $t^{1/2}$ | Analytical/numerical | Explain exponent: closure effect? 3D geometry? constraint? |
| $B_t$ (gradient ridge) is gauge/scale stable | Analytical | Prove $B_t$ invariant under $\tilde{u} \mapsto \phi(\tilde{u})$ for monotone $\phi$ |
| $P(\sigma' \mid \text{Kramers event})$ is computable from Hessian at saddle | Analytical | Derive $\sigma(u_{\mathrm{saddle}})$ from saddle geometry; connect to $\sigma(u_{\min,K-1})$ via descent |

### §12.5 Top 10 dangerous hidden assumptions

1. **$X_t = $ pixel grid** (Layer A/B conflation). Assuming 2D pixel coordinates carry the SCC structure conflates the observation support with the primitive field support. The primitive should live on $\mathcal{P}_t$ (3D).

2. **$K_{\mathrm{field}}$ is ontological** (OP-0009-Pre). Using $K_{\mathrm{field}}$ as a foundational parameter presupposes the count of formations. It is a numerical truncation constant, not an ontological entity.

3. **$K_{\mathrm{act}}$ is a state-space index** (Q4 failure pattern). Treating $K_{\mathrm{act}}$ as an index into $\Sigma^K_M$ sub-manifolds conflates the foundational state space with a derived observable.

4. **$E_{\mathrm{photo}}$ belongs in the prior** (CN5 violation). Adding photometric consistency to $\mathcal{E}_{\mathrm{SCC}}$ violates CN5; it must be in the likelihood.

5. **Threshold boundary is canonical** (OP-0006). The $D_t$-threshold definition of $B_t$ is unstable under scale changes and has a free parameter. Using it as if canonical is dangerous.

6. **T-Merge (b) implies dynamical K=1** (CN15 confusion). The static global minimum is $K=1$, but dynamics can maintain $K>1$ metastably. Equating static minimum with dynamic endpoint is the classic CN15 error.

7. **$\sigma^A$ is deterministic at K-jump** (OP-0008). Assuming a deterministic label inheritance rule ignores the Kramers stochasticity. $\sigma^A$ should be a conditional posterior.

8. **Kramers barrier is the K-field sub-manifold barrier** (saddle confusion). The saddle in $\Sigma^K_M$ is an approximation to the true saddle in $\Sigma_M$. The approximation quality is unknown; at large $K_{\mathrm{field}}$, the K-field saddle may be significantly different.

9. **P-F flag is optional** (stochastic assumptions). Any claim about metastability times, equilibrium distributions, or thermal effects is invalid without the stochastic extension. The P-F flag is not a stylistic warning; it is a logical barrier.

10. **$\mathcal{P}_t$ = true 3D geometry** (stereo reconstruction error). The reconstructed point cloud $\mathcal{P}_t$ has stereo noise (disparity errors, occlusion, matching failures). The field $\tilde{u}_t$ is conditioned on $\mathcal{P}_t$, not on the true geometry. Treating $\mathcal{P}_t$ as noiseless is dangerous.

### §12.6 Next Work Priority Order

| Priority | Task | Type | Blocking what |
|----------|------|------|--------------|
| P0 | Formalize Langevin on $\Sigma_M$ (stochastic SCC v1) | Theory (P-F Axiom v0 → Axiom G) | All G-layer claims; OP-0005, OP-0008, OP-0021 |
| P0 | Redefine $K_{\mathrm{act}} = \#\pi_0(\{u > \varepsilon\})$ in canonical (Commitment 16 amendment) | Canonical edit | OP-0009-Pre; cleaner K-field demotion |
| P1 | Replace threshold $B_t$ with persistent transition layer (OP-0006 resolution) | Working → canonical | OP-0006 OPEN HIGH closure |
| P1 | Compute $\det H_{\min,K}$ at R23 minimizers (NQ-ST-1) | Numerical | $F(K;\mathcal{P})$ Laplace approximation validation |
| P1 | Derive $\Sigma_M$ saddle vs $\Sigma^K_M$ saddle relationship | Analytical | Barrier accuracy; OP-0005 candidate (b) rigor |
| P2 | $\sigma$-posterior at K-jump: derive $\sigma(u_{\mathrm{saddle}})$ for representative $(j,k)$ pairs on R23 | Numerical | OP-0008 Path B; Commitment 18 candidate |
| P2 | $\mathcal{P}$-conditional free energy: build experiment verifying $F(K;\mathcal{P})$ changes with depth separation | Numerical | OP-0005 stereo-conditioned prediction |
| P2 | Canonical §3 amendment: $X_t$ instantiation as $\mathcal{P}_t$ (modeling-layer note) | Canonical (minor) | OP-0009-Pre modeling-layer framing |
| P3 | Latent scene layer $\mathcal{X}_t = (\mathcal{M}_t, \mu_t, U_t)$ formal definition | Theory | OP-0020 dynamic topology; occlusion handling |
| P3 | Coarsening exponent explanation: why $t^{1.315}$ (OQ-4) | Analytical | V4 numerical anchor theoretical grounding |

### §12.7 Summary

The stereo-conditioned soft-to-crisp framework provides a clean 7-layer decomposition (A–G) that resolves the following structural confusions in existing SCC theory:

1. **Layer A/B conflation** (2D pixel support vs 3D scene support): resolved by distinguishing $\mathfrak{O}_t$ (A) from $\mathcal{P}_t, \tilde{u}_t$ (B).

2. **Prior/likelihood conflation** (observation terms in SCC energy): resolved by CN5-compliant separation — $\mathcal{E}_{\mathrm{SCC}}$ is pure prior; $\mathcal{L}_{\mathrm{obs}}$ contains all observation-dependent terms.

3. **$K$ as foundational vs derived**: resolved by adopting $\Sigma_M$ as foundational state space and $K_{\mathrm{act}} = \#\pi_0$ as derived observable; $\Sigma^K_M$ is a local chart.

4. **Fast vs slow dynamics conflation**: resolved by BO time-scale separation — $\tilde{u}_t$ (fast, within K-basin) integrates out to give $K_{\mathrm{act}}(t)$ (slow, Markov jump process).

5. **Static $K$ selection vs dynamic $K$ statistics**: resolved by $F(K;\mathcal{P})$ (equilibrium statistics) + $\Gamma^{K \to K'}(\mathcal{P})$ (dynamical rates), connected by detailed balance.

The existing theories are largely salvageable; the main required changes are (1) demotion of $\Sigma^K_M$ from foundational to chart, (2) extension of $F(K)$ to $F(K;\mathcal{P})$ with correct Hessian entropy, (3) formalization of stochastic SCC (P-F Axiom v0), (4) redefinition of boundary $B_t$ as persistent transition layer. Once these changes are made, the entire existing theory embedding is consistent with the new framework.

---

**End of cross_validation_stereo_scc_framework.md.**

**Status:** Working draft, W6 Day 2 evening, 2026-05-05. Comprehensive cross-validation of all existing SCC theories against the stereo-conditioned framework. No canonical claims asserted; all items working-level. P-F flags throughout. Feeds: OP-0005 Commitment 19, OP-0006 resolution path, OP-0008 Commitment 18, OP-0009-Pre canonical §1 amendment (v2.0 horizon), OP-0021 stochastic extension (highest-priority blocker).

**File:** `THEORY/working/MF/cross_validation_stereo_scc_framework.md`
**Created:** 2026-05-05 W6 D2 evening.
**Promotion target:** No direct canonical promotion; feeds multiple working files and OP resolution paths. CV-1.8+ / v2.0 horizon for canonical §1/§3/§14 amendments.
