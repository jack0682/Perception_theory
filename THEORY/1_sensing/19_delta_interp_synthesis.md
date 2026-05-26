---
type: working/sensing_pipeline/pass12_delta_interp_synthesis
version: v0
date: 2026-05-26
status: ACTIVE — Pass 12 Phase F Task 25
purpose: |
  Following Task 19 (Phase D), rank the 4 Δ_interp candidates by:
  (i) PAI consistency, (ii) operational testability, (iii) compatibility with Pass 11 geometric framework.
  Pick recommended candidate; justify; note PAI substrate dependencies.
register: SYNTHESIS
parent: 00_INDEX
prev: 18_stress_energy_alternatives
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
  pai_canonical_edits: 0
  modifies_12_perception_cone: 0
  candidates_ranked: 4
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[18_stress_energy_alternatives]] · Pass 12 Phase F-2

# Pass 12 Phase F Task 25 — $\Delta_{\text{interp}}$ Candidates: Ranking & Synthesis

**Inherited from Task 19 (Phase D)**: 4 candidates introduced — $\alpha$ (metric geodesic), $\beta$ (KL), $\gamma$ (categorical), $\delta$ (Wasserstein). Task 19's brief recommendation was $\delta$. This task: full ranking against 3 explicit criteria, justification, integration with PAI substrate.

---

## Criteria

### Criterion 1: PAI consistency
$\Delta_{\text{interp}}$ must:
- Be *symmetric* between perception and action interpretations (PAI vocabulary treats them as dual)
- *Vanish* when interpretations coincide (zero gap is meaningful "PA-formation")
- *Compose* across formation chains (interpretation gap of $F_1 \circ F_2$ relates to gaps of components)

### Criterion 2: Operational testability
$\Delta_{\text{interp}}$ must:
- Be *computable* from finite empirical data
- Have a *natural falsification route* (predicted relationships to measurable quantities)
- Not require unmeasured *generative model* or *prior structure*

### Criterion 3: PFE-geometric compatibility
$\Delta_{\text{interp}}$ must:
- Connect naturally to Pass 11's geometric framework (cone, metric, curvature)
- Allow *bridge propositions* between PAI and PFE (e.g., "small $\Delta_{\text{interp}}$ ⟺ cones coincide")
- Be invariant under PFE's reduced symmetry group (Task 21: spatial-diffeomorphism tensorial covariance)

---

## Ranking

### Candidate $\alpha$ (geodesic distance in metric space)

**PAI consistency**: $d_{\text{metric-space}}(g^P, g^A)$ is symmetric by definition of metric. Vanishes iff metrics coincide. Composition: if $F = F_1 \circ F_2$, then $g_F^P = g_{F_1}^P \cdot g_{F_2}^P$ in some composition; geodesic distance respects triangle inequality. **PASS**.

**Operational testability**: $g^P$ and $g^A$ must be *measured*. Per PAI, $g^P$ from perception observer-class; $g^A$ from action observer-class. Measurement of *full metric* from finite trials is hard — requires sampling many $(t, x, y)$ configurations. **WEAK**.

**PFE-geometric compatibility**: Lives entirely in the *space of metrics* — same mathematical universe as PFE. Natural bridge: $\Delta_{\text{interp}}$ is the "distance traveled" in metric-space; PFE evolves the metric in time. **STRONG**.

**Score**: PAI ✓, Operational ✗, PFE-geometric ✓. **2/3**.

### Candidate $\beta$ (KL divergence)

**PAI consistency**: KL is *asymmetric* ($D_{KL}(P\|Q) \neq D_{KL}(Q\|P)$). PAI treats P and A as dual, so asymmetric measure *violates* PAI duality. Composition: KL satisfies chain rule but for joint distributions; not directly for formation composition. **FAIL on symmetry**.

**Operational testability**: KL is *easy* to estimate from finite samples (just count outcomes). Standard estimator with known convergence rates. **STRONG**.

**PFE-geometric compatibility**: KL is *not* a metric in the geometric sense; it's a divergence. Doesn't fit PFE's geometric vocabulary naturally. **WEAK**.

**Score**: PAI ✗, Operational ✓, PFE-geometric ✗. **1/3** — eliminated by PAI failure.

### Candidate $\gamma$ (categorical natural transformation defect)

**PAI consistency**: Categorical framework is *the* native PAI language. Natural transformation defect is automatically *coordinate-free* and *composes correctly*. **STRONG**.

**Operational testability**: Defect computation requires specifying *functors* explicitly — PAI's perception functor and action functor not yet operationally defined. Currently *paper-only* (PAI DEFINITION-DRAFT). **VERY WEAK**.

**PFE-geometric compatibility**: Categorical defect can be *interpreted* geometrically but the interpretation is non-trivial. Bridge to PFE requires substantial extra work. **MEDIUM**.

**Score**: PAI ✓, Operational ✗, PFE-geometric ⚬. **1.5/3** — eliminated by operational gap.

### Candidate $\delta$ (Wasserstein distance)

**PAI consistency**: Symmetric ($W_2$ is a metric). Vanishes iff measures coincide. Composes with reasonable rules (e.g., $W_2(\mu_1 \otimes \nu_1, \mu_2 \otimes \nu_2) \leq W_2(\mu_1, \mu_2) + W_2(\nu_1, \nu_2)$ for product measures). **PASS**.

**Operational testability**: $\mu^P, \mu^A$ are probability measures on perception/action outcome spaces — *measurable* from empirical data with standard OT estimators. Convergence rates well-understood. **STRONG**.

**PFE-geometric compatibility**: Wasserstein has *deep* connection to PFE via OT-on-curved-manifold theory (McCann, Sturm, Lott-Villani). Wasserstein gradient flow IS the gradient flow of free energy in the space of measures — direct PFE bridge. SCC's `transport.py` already implements Sinkhorn $W_2$. **VERY STRONG**.

**Score**: PAI ✓, Operational ✓, PFE-geometric ✓. **3/3**.

---

## Verdict

**$\delta$ (Wasserstein distance) is the unique candidate satisfying all 3 criteria.**

| Candidate | PAI | Op | PFE | Total | Status |
|-----------|-----|----|----|-------|--------|
| $\alpha$ (metric geodesic) | ✓ | ✗ | ✓ | 2/3 | viable for theory |
| $\beta$ (KL) | ✗ | ✓ | ✗ | 1/3 | eliminated |
| $\gamma$ (categorical) | ✓ | ✗ | ⚬ | 1.5/3 | eliminated |
| $\delta$ (Wasserstein) | ✓ | ✓ | ✓ | **3/3** | **RECOMMENDED** |

Confidence: high.

---

## Concrete operational form

### Definition (proposed)

Given formation $F$ (an element of PAI's formation category), define:
$$\Delta_{\text{interp}}^{(W_2)}(F) := W_2\big(\mu^P_F, \mu^A_F\big)$$

where:
- $\mu^P_F$ = probability measure on the space of *perceptual outcomes* given $F$
- $\mu^A_F$ = probability measure on the space of *action outcomes* given $F$
- $W_2$ = Wasserstein-2 distance with appropriate ground metric

### Ground metric choice

The Wasserstein-2 distance requires a *ground metric* on the outcome space. Natural choice for PFE-compatibility:

$$d_{\text{ground}}\big(\text{outcome}_1, \text{outcome}_2\big) := d_{\text{geodesic in PFE metric}}\big(\text{outcome}_1, \text{outcome}_2\big)$$

i.e., use PFE's perception cone geodesic distance as the ground metric for $W_2$.

This makes $\Delta_{\text{interp}}^{(W_2)}$ *intrinsically PFE-coupled*: small interpretation gap ⟺ measures coincide in PFE-induced geometry.

### Computational support

SCC `CODE/scc/transport.py` already implements:
- Sinkhorn log-domain $W_2$ computation
- Cohesion-fingerprint OT (function `cohesion_fingerprint_distance`)
- Transport-based persistence (`persist_transport`)

These can be reused for $\Delta_{\text{interp}}^{(W_2)}$ computation with the PFE-ground metric.

---

## Bridge propositions (PAI ↔ PFE via $\Delta_{\text{interp}}^{(W_2)}$)

**Bridge 1** (PA-formation characterization):
> Formation $F$ is a *PA-formation* in PAI iff $\Delta_{\text{interp}}^{(W_2)}(F) < \epsilon$ for empirically calibrated $\epsilon$.

**Bridge 2** (cone-coincidence equivalence):
> $\Delta_{\text{interp}}^{(W_2)}(F) = 0$ iff the perception cone $\mathcal{C}^P[F]$ and action cone $\mathcal{C}^A[F]$ coincide globally (under suitable observability conditions).

**Bridge 3** (gradient flow):
> Under PA-formation dynamics (perception drives action drives perception), $\Delta_{\text{interp}}^{(W_2)}$ evolves by Wasserstein gradient flow in the space of probability measures. The fixed points are $\Delta_{\text{interp}} = 0$ states (PA-coincident formations).

These bridges are *proposals*, not theorems. Their proof is *out of scope for Pass 12* — Bridge 1 requires PAI canonical commitment (substrate decision); Bridges 2, 3 require formal proofs.

---

## PAI substrate dependency

The recommendation of $\delta$ as $\Delta_{\text{interp}}$ is *conditional* on PAI canonical accepting a *Wasserstein-form* operationalization. PAI currently keeps $\Delta_{\text{interp}}$ in DEFINITION-DRAFT register (not committed).

**This is not a Pass 12 decision**. PAI substrate decisions are *outside* the sensing_pipeline scope. The recommendation here is:
- IF PAI commits to operationalization → recommend Wasserstein
- IF PAI keeps draft status → Pass 13 should not promote this commitment

### What was decided (Pass 12)
- Among 4 candidates considered in 12_ and Phase D, Wasserstein is *uniquely best* against the 3 criteria
- SCC's existing `transport.py` provides computational support
- Bridges 1, 2, 3 are *natural* formulations but require PAI substrate decision and formal proofs

### What was NOT decided (Pass 12)
- Empirical $\epsilon$ calibration value for Bridge 1
- Formal proof of Bridge 2 (cone-coincidence equivalence)
- Whether Wasserstein gradient flow (Bridge 3) is consistent with SCC gradient flow (Task 22 dissipation issue)

---

## Aggregate Task 25 verdict

**PASS (recommendation crystallized)**. Confidence: high.

$\delta$ (Wasserstein) is the unique candidate satisfying PAI consistency + operational testability + PFE-geometric compatibility. SCC has the computational infrastructure already. PAI substrate commitment is the upstream gating dependency.

### New OPs registered
- **OP-PFE-17**: Calibrate $\epsilon$ threshold for Bridge 1 (PA-formation iff $\Delta_{\text{interp}}^{(W_2)} < \epsilon$); requires empirical PA-formation dataset
- **OP-PFE-18**: Prove or refute Bridge 2 (cone-coincidence ⟺ zero Wasserstein gap)
- **OP-PFE-19**: Resolve Wasserstein-gradient-flow vs SCC-gradient-flow consistency (interacts with Task 22 dissipation issue and Task 24 noise-scaling discriminator)

---

*Phase F Task 25 v0. 4 candidates ranked, $\delta$ Wasserstein uniquely recommended (3/3 criteria). 3 bridges proposed conditionally on PAI substrate decision. 3 new OPs registered. canonical/SCC/PAI/8-retractions 0 modifications. Next: Task 26 in 20_three_framework_synthesis.md.*
