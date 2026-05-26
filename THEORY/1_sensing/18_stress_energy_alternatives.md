---
type: working/sensing_pipeline/pass12_stress_energy_alternatives
version: v0
date: 2026-05-26
status: ACTIVE — Pass 12 Phase F Task 24
purpose: |
  Compare four candidate stress-energy sources for PFE: SCC E[u], Friston free energy F,
  Fisher information density, sparse-coding L1.
  For each: derive PFE form, list distinct predictions, identify empirical discriminators.
register: COMPARISON
parent: 00_INDEX
prev: 17_pass12_adversarial_extensions
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
  pai_canonical_edits: 0
  modifies_12_perception_cone: 0
  alternatives_compared: 4
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[17_pass12_adversarial_extensions]] · Pass 12 Phase F-1

# Pass 12 Phase F Task 24 — Stress-Energy Alternatives

**Question**: Iter 20 of 12_ identified SCC E[u] as the load-bearing choice for $T_{\mu\nu}^{\text{perception}}$. Four alternatives exist. Are they empirically distinguishable from SCC?

**Inherited caveat** (from Phase E Task 22): all alternatives must be considered in *equilibrium-effective* regime. Dynamical predictions of any alternative depend on its own dissipative structure.

---

## Setup

For each candidate energy/cost functional $\mathcal{F}[u, g]$, define stress-energy:
$$T_{\mu\nu}^{(\mathcal{F})} := \frac{2}{\sqrt{-g}} \frac{\delta (\sqrt{-g} \, \mathcal{F})}{\delta g^{\mu\nu}}$$

The PFE candidate becomes:
$$G_{\mu\nu}^{(s)} = \kappa^{(s)} T_{\mu\nu}^{(\mathcal{F})}$$

We compare the four $\mathcal{F}$ choices.

---

## Candidate 1: SCC $E[u]$ (current Pass 11 choice)

### Functional
$E[u] = \lambda_{cl} E_{cl} + \lambda_{sep} E_{sep} + \lambda_{bd} E_{bd} + \lambda_{tr} E_{tr}$

Continuum analog:
$E[u] = \int \big[ \lambda_{cl} u(1-u)^2 + \lambda_{sep} u(1-u) + \lambda_{bd} |\nabla u|^2 + \lambda_{tr} (\text{transport term}) \big] \sqrt{-g} \, d^3 x$

### Stress-energy structure
- $E_{cl}$ and $E_{sep}$ are *potential* terms (algebraic in $u$): contribute $T_{\mu\nu}^{\text{pot}} \propto V(u) g_{\mu\nu}$ (perfect-fluid-like, "cosmological constant"-like contribution)
- $E_{bd}$ is *kinetic* gradient term: contributes $T_{\mu\nu}^{\text{kin}} \propto \partial_\mu u \partial_\nu u - \tfrac{1}{2} g_{\mu\nu} (\partial u)^2$ (standard scalar field stress-energy)
- $E_{tr}$ is *transport* term: contributes Wasserstein-transport-induced stress-energy (less standard, requires `transport.py` machinery to evaluate)

### Predictions specific to SCC
- *Two-scale binding kernel* (closure + separation potentials create a double-well; binding occurs in spinodal range $c \in ((3-\sqrt{3})/6, (3+\sqrt{3})/6)$ ≈ (0.21, 0.79))
- *Sharp phase transitions* possible: $\beta/\alpha > 4\lambda_2 / |W''(c)|$ (T8 from SCC canonical)
- *Diagnostic vector* (Bind, Sep, Inside, Persist) — 4 independent observable directions

### Strengths
- Connects to validated SCC canonical (215 tests pass, 59 Cat A theorems)
- Diagnostic vector provides 4 measurable signals (Test 2-4 use them)
- Preserves constraint compliance (no SCC modification)

### Weaknesses
- Dynamics is dissipative (Task 22 issue)
- No information-theoretic content (free energy / Fisher information not built in)
- Cohesion field $u$ is *abstract* (no immediate biological correlate)

---

## Candidate 2: Friston Free Energy $F$

### Functional
Variational free energy in active inference framework:
$F[u] = D_{KL}(q(u|s) \| p(u|s)) - \log p(s)$
where $q$ is recognition density, $p$ is generative model, $s$ is sensory data.

For perception (passive inference): $F$ reduces to:
$F[u] = D_{KL}(q(u) \| p(u | \text{sensory data})) + \log Z$

### Stress-energy structure
$F$ contains:
- *Entropy* term $H(q) = -\int q \log q$ — contributes $T_{\mu\nu}^{(H)}$ that depends on local entropy density
- *Cross-entropy* term $-\int q \log p$ — couples $u$ to generative model

The variational stress-energy is *information-theoretic*: $T_{\mu\nu}^{(F)}$ has units of *information density* per unit volume.

### Predictions specific to Friston
- *Precision-weighted* coupling: $T_{\mu\nu}^{(F)}$ scales with stimulus precision (inverse variance)
- *Adaptive metric* gives geometric interpretation to *precision-weighting* — high-precision regions create stronger metric perturbation
- *Hierarchical predictive structure*: $F$ at each layer of hierarchy contributes; cumulative coupling stronger than single-layer SCC

### Strengths
- Connects to broad cognitive-science framework (active inference, predictive coding)
- Information-theoretic content built in
- Hierarchical structure matches multi-stage retinal architecture

### Weaknesses
- $F$ requires explicit *generative model* $p$ — typically infinite-dimensional choice
- Variational structure conflates "perception" with "inference" — may not fit raw retinal processing
- Less computational machinery than SCC

### Distinguishing prediction from SCC
- For *low-precision* (high-noise) stimulus, Friston PFE predicts *weaker* metric perturbation (precision-scaling). SCC PFE has no such precision-dependence — cohesion contribution is independent of stimulus noise.
- **Empirical discriminator**: vary stimulus noise; measure binding-strength scaling. If binding scales with $1/\sigma^2_{\text{stim}}$, Friston-PFE supported over SCC-PFE.

---

## Candidate 3: Fisher Information Density

### Functional
$\mathcal{I}[u, g] := \int g^{\mu\nu} (\partial_\mu \log u)(\partial_\nu \log u) \, u \, \sqrt{-g} \, d^3 x$

This is the *Fisher information* of the field $u$ treated as a parameter for a probability density.

### Stress-energy structure
- Pure *kinetic* form (only gradient terms; no potential)
- $T_{\mu\nu}^{(\mathcal{I})} \propto (\partial_\mu \log u)(\partial_\nu \log u)$
- Naturally scale-invariant (Fisher information is invariant under $u \to cu$ for constant $c$)

### Predictions specific to Fisher
- *Scale invariance*: predictions invariant under global rescaling of cohesion field magnitude
- *No spontaneous phase transition*: Fisher has no double-well structure
- *Maximum information principle*: equilibrium configurations maximize Fisher information for fixed total cohesion

### Strengths
- Information-geometric — natural for sensory measurement
- Scale-invariant (no arbitrary unit choice for $u$)
- Connects to information bound at end of pipeline (file 06_ has DPI chain)

### Weaknesses
- Pure kinetic, no potential — cannot model *binding thresholds*
- No diagnostic vector analog
- Less validated empirically

### Distinguishing prediction from SCC
- For *constant* cohesion ($u = c$), Fisher PFE has $T_{\mu\nu} = 0$ (no information in constant); SCC has $T_{\mu\nu} \propto V(c) g_{\mu\nu}$ (constant potential term)
- **Empirical discriminator**: in regions of *uniform* perception (uniform cohesion), is there *baseline* binding contribution (SCC predicts yes) or *zero* contribution (Fisher predicts none)?

---

## Candidate 4: Sparse Coding L1

### Functional
$L_1[u] := \int |u| \sqrt{-g} \, d^3 x + \lambda \int (\text{reconstruction error})^2$

Olshausen-Field sparse coding loss. Cohesion field becomes the *sparse code* for the sensory input.

### Stress-energy structure
- *Non-differentiable* potential ($|u|$ has cusp at $u = 0$)
- $T_{\mu\nu}^{(L_1)}$ requires distributional treatment near $u = 0$
- Sparse equilibria: $u$ is *zero* over most of the domain, *nonzero* on a sparse set

### Predictions specific to L1
- *Sparse equilibrium* support — most of retina has $u = 0$, with localized "active" regions
- *Discontinuous transitions* (cohesion turns on/off, not graded)
- *Reconstruction-optimal* (binds to maximize sensory-input recovery)

### Strengths
- Validated for early visual cortex (Olshausen-Field 1996)
- Sparse activity matches retinal/cortical recordings
- Computationally tractable

### Weaknesses
- Non-smooth (distributional treatment required)
- No diagnostic-vector analog
- Discontinuous transitions may conflict with continuous σ-judgments (Task 1 fuzzy boundary)

### Distinguishing prediction from SCC
- L1 predicts *sparse* activation — only isolated regions have $u > 0$; SCC predicts *graded* fields throughout
- **Empirical discriminator**: image stimulation, MEA recording. If active ganglion cells are *sparse* (small subset only), L1-PFE supported. If activation is *graded across many cells*, SCC-PFE supported.
- Caveat: actual retinal recordings show *sparse but not extreme* — partial support for both, with SCC modification (could add L1-like penalty to SCC energy).

---

## Empirical discriminator summary

| Discriminator | Stimulus | SCC predicts | Friston predicts | Fisher predicts | L1 predicts |
|---------------|----------|--------------|------------------|------------------|-------------|
| Low-noise vs high-noise binding | Vary stimulus noise | No noise-dep | Stronger at low-noise | No noise-dep | No noise-dep |
| Uniform field background | Constant uniform stim | Baseline $T \propto g$ | Variable (depends $p$) | Zero $T$ | Zero $T$ |
| Active-cell sparsity | Image stim, MEA | Graded many cells | Mixed | Mixed | Sparse few cells |
| Sharp phase transitions | Param sweep | Yes ($\beta/\alpha$ threshold) | Mixed | No | Yes (discontinuous) |
| Scale invariance of $u$ | Rescale $u$ | No invariance | No | YES | No |

### Single critical experiment

**Noise-scaling experiment**: vary stimulus contrast/noise. Measure binding strength.

- SCC: binding $\sim$ constant (no precision scaling)
- Friston: binding $\sim$ 1/noise²
- Fisher: binding $\sim$ constant (scale-invariant)
- L1: binding $\sim$ thresholded (zero below noise threshold)

**One experiment discriminates four candidates**. Feasible with standard psychophysics; would take ~weeks.

### Aggregate verdict on Task 24

**WEAKEN the load-bearing SCC choice — but with computational mitigation**. Confidence: medium-high.

SCC E[u] is *one* of four serious candidates. Each makes *distinct* predictions:
- SCC: graded everywhere, phase transitions, no precision dependence
- Friston: precision-weighted, hierarchical, requires generative model
- Fisher: scale-invariant, no thresholds, information-geometric
- L1: sparse, discontinuous, reconstruction-optimal

The *correct* choice is empirical. Pass 11's selection of SCC was on *constraint-preservation* grounds (no canonical modification), not on *empirical fit*. Until the noise-scaling experiment is done, SCC is *one plausible candidate among four*.

### Recommended next step

**Mixed-strategy implementation**: in Pass 13, build a *parametrized* PFE that interpolates between candidates:
$\mathcal{F}^{(\lambda)} := \lambda_S E_{SCC} + \lambda_F F_{Friston} + \lambda_I \mathcal{I}_{Fisher} + \lambda_L L_1$

Fit $\lambda$-weights from empirical data. The fitted weights identify which candidate dominates in actual retina.

### New OP registered
**OP-PFE-16**: Execute noise-scaling discriminator experiment; fit $\lambda$-weights in mixed-strategy PFE; identify dominant stress-energy candidate.

---

*Phase F Task 24 v0. 4 candidates compared, single critical experiment identified, mixed-strategy implementation recommended for Pass 13. canonical/SCC/PAI/8-retractions 0 modifications. Next: Task 25 in 19_delta_interp_synthesis.md.*
