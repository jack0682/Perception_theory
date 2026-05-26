---
type: working/sensing_pipeline/cone_field_equation
version: v0
date: 2026-05-26
status: ACTIVE — Pass 11 framework construction (20 iterations)
purpose: |
  Build the perception cone + Einstein-style field equation framework
  via 20 iterations of derive + adversarial verify.
  Foundation: σ relation (Tier 2) reinterpreted as Minkowski-style perception lightcone.
  Endpoint: candidate field equation R_μν - (1/2)g_μν R = κ T_μν^perception
  with operational tests and connections to SCC + PAI substrates.
register: CONSTRUCTION (each iteration: candidate + adversarial check)
parent: 00_INDEX
prev: 11_minimal_core
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
  pai_canonical_edits: 0
  uses_existing_primitives: σ (P4 from 11_), SCC u_t, SCC E[u]
  introduces_new_named_framework: "perception cone" / "PFE" — used as descriptive labels, not as canonical-track promotion
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[11_minimal_core]] · Builds on: SCC canonical (substrate-preserved) + PAI pivot (substrate-preserved)

# Perception Cone + Einstein-Style Field Equation Framework

**Construction via 20 iterations**: derive postulates → derive σ → derive metric → derive field equation → adversarial gauntlet → operational tests → connections.

Each iteration: (a) what is added/refined, (b) adversarial check, (c) state after iteration. Failure modes documented honestly per iteration.

---

## Iteration 1 — Postulate P1 (perceptual relativity)

### Statement
**P1**: There exists an equivalence class of "observers" (sensor + attention + task configurations) such that the *binary perceptual reachability relation* σ between any two events $e_i, e_j$ is invariant across observers within the class.

Formally: let $\mathcal{O}$ be the set of admissible observers; let $\sigma^{(\omega)}(e_i, e_j) \in \{0, 1\}$ be the σ-relation as judged by observer $\omega \in \mathcal{O}$. Then

$$\forall \omega, \omega' \in \mathcal{O}: \;\; \sigma^{(\omega)}(e_i, e_j) = \sigma^{(\omega')}(e_i, e_j)$$

for some equivalence class $\mathcal{O}$ to be specified.

### Adversarial check (Pattern #11 model misspec)
Does "observer equivalence class" describe a real biological/physical structure? Candidate:
- Same retina (single individual)
- Same task context (fixed attention)
- Same illumination regime

Empirically, σ-judgments vary across individuals (psychophysical inter-subject variance ~10-30%). So P1 holds *only within* a narrowly defined class — *within-subject + within-task + within-illumination*.

### State after Iter 1
P1 holds *conditionally*; equivalence class must be empirically narrow. **Note**: this is *weaker than physical relativity* (which holds across all inertial observers universally) but *operationally checkable*.

---

## Iteration 2 — Postulate P2 (limiting perceptual rate $c_p$)

### Statement
**P2**: There exists $c_p > 0$ such that no perceptual influence between events propagates faster than $c_p$. The value $c_p$ is *invariant within the observer equivalence class* of P1.

Operational definition:
$$c_p := \delta_x / \delta_t$$
where $\delta_x$ is the smallest spatial separation between two events that are perceptually distinguishable, and $\delta_t$ is the smallest temporal separation. Both measured *within the observer class*.

### Adversarial check (Pattern #15 vacuity)
Is there *actually* a unique limiting rate, or are there many different "speeds" at different scales? Honest answer: **the latter**. Different perceptual processes have different limiting rates:
- Photoreceptor integration: $\sim 0.3$ m/s on retina
- Bipolar/amacrine network: $\sim 5$ m/s
- Ganglion spike propagation: $\sim 25-100$ m/s
- Attentional shift: degrees/sec scale

So P2 holds *per-stage*, not *globally*. Each stage has its own $c_p$.

### State after Iter 2
P2 holds *per-stage*. Framework requires *hierarchy of cones*, not single cone. **Pattern #15 partial hit**: not vacuous, but more nuanced than physical analogy.

---

## Iteration 3 — Minkowski-style derivation of σ

### Construction
Given P1 + P2 (per-stage), define for each stage $s$ with rate $c_p^{(s)}$:

$$\sigma^{(s)}(e_i, e_j) := \mathbf{1}\!\left[ c_p^{(s)} \cdot |t_i - t_j| \;\geq\; |x_i - x_j| \right]$$

This is the *characteristic function of the timelike-or-lightlike cone* in $(t, x)$-space scaled by $c_p^{(s)}$.

### Properties (recovered from Minkowski geometry)
- **Reflexive**: $\sigma^{(s)}(e, e) = 1$ trivially.
- **Symmetric**: $\sigma^{(s)}(e_i, e_j) = \sigma^{(s)}(e_j, e_i)$ (cone is symmetric).
- **Non-transitive**: σ(a,b) ∧ σ(b,c) ⇏ σ(a,c) when $a$ and $c$ are spacelike separated through $b$.
- **Invariance under P1**: by construction.

### Connection to previous σ commitment
The Tier 2 σ relation we committed to in early conversation was *exactly this cone-membership* — but with $\delta_x, \delta_t$ chosen *empirically* rather than as $c_p$ derivation. Now σ has *principled* (postulate-derived) form.

### Adversarial check (Pattern #18 tautology)
Is σ now just a *restatement* of the cone definition? No — the *non-trivial content* is the *invariance claim* (P1) + the *existence of a single $c_p^{(s)}$ per stage* (P2). Both are *empirical claims*, falsifiable by inter-observer / inter-condition variation.

### State after Iter 3
σ is now *derived* from two postulates. Non-trivial content = P1 + P2. **Improvement over Tier 2 primitive**: previously σ was asserted; now it has structural origin.

---

## Iteration 4 — Operational definition of $c_p^{(s)}$

### Procedure
For each stage $s$:
1. Identify the *characteristic timescale* $\tau_s$ (membrane time constant for stage 1; spike rate for stage 3; etc.)
2. Identify the *characteristic length scale* $\ell_s$ (receptor spacing for stage 1; receptive field size for stage 2; etc.)
3. Compute $c_p^{(s)} := \ell_s / \tau_s$

### Stage table (current best estimates)

| Stage $s$ | $\tau_s$ | $\ell_s$ | $c_p^{(s)}$ | Empirical source |
|-----------|----------|----------|-------------|------------------|
| Photoreceptor (cone) | 10 ms | 3 μm | 0.3 mm/s | Baylor 1979; cone density |
| Bipolar/amacrine | 5 ms | 50 μm | 10 mm/s | center-surround radius |
| Ganglion (M cells) | 1 ms | 100 μm | 100 mm/s | spike rate + RF |
| Ganglion (P cells) | 5 ms | 50 μm | 10 mm/s | sustained firing + RF |
| Cortical V1 | 10 ms | 1 mm (column) | 100 mm/s | binding window |
| Attentional binding | 100 ms | 100 mm (visual field) | 1 m/s | psychophysics |

### Adversarial check (Pattern #28 subset support)
Does $c_p^{(s)}$ apply uniformly across the stage's spatial domain? Honest answer: **NO** — fovea vs periphery have different $\ell_s$, hence different $c_p$. Each stage's cone is *spatially inhomogeneous*.

### State after Iter 4
$c_p$ has *operational definition*. **Limitation**: must extend to *spatially inhomogeneous* cone framework. Add: $c_p^{(s)}(x)$ as a *function of position*.

---

## Iteration 5 — Stage hierarchy of cones

### Structure
Define $\mathcal{C}^{(s)} := \{(\Delta t, \Delta x) : c_p^{(s)} \cdot |\Delta t| \geq |\Delta x|\}$ — the per-stage cone.

### Hierarchy claim
**Conjecture**: $\mathcal{C}^{(s_1)} \subseteq \mathcal{C}^{(s_2)}$ if $c_p^{(s_1)} \leq c_p^{(s_2)}$.

This means **slower stages have *smaller* cones** (more events fall outside). Conversely, fast stages can co-perceive widely-separated events.

### Adversarial check (Pattern #40 too-clean lemma)
Is nesting really clean? Counterexample: photoreceptor has *slow time* but *very short spatial*; ganglion has *fast time* but *wider spatial*. Cones may *cross* rather than nest.

Resolution: cones are defined in $(t, x)$-space; nesting requires comparison along *both* axes. **Cones nest only if $c_p$ comparison is unambiguous**. Otherwise — *crossing cones* — events may be in one cone but not the other.

### Honest revision
The hierarchy is *not* strictly nested. Each stage's cone is *its own region* in $(t, x)$. *Multi-stage co-perceivability* requires events in the *intersection* $\bigcap_s \mathcal{C}^{(s)}$.

### State after Iter 5
Per-stage cones exist; *not nested*. **Refinement**: framework must use *intersection of cones* for multi-stage analysis, not nesting.

---

## Iteration 6 — Local Lorentz metric from cone

### Construction
For each stage $s$, the *infinitesimal* form of the cone defines a local (1+1 or 1+2) Minkowski metric:

$$g_{\mu\nu}^{(s)} = \text{diag}(-c_p^{(s) 2}, 1)$$ (1+1 spacetime)

or

$$g_{\mu\nu}^{(s)} = \text{diag}(-c_p^{(s) 2}, 1, 1)$$ (1+2 spacetime for retinal 2D + time)

### Line element
$$ds^2_{(s)} = -c_p^{(s) 2} dt^2 + dx^2 + dy^2$$

The set $\{ds^2 = 0\}$ is the *null cone* for stage $s$.

### Adversarial check (Pattern #7 implicit regularity)
Does this metric require *smoothness* of $c_p^{(s)}(x)$? Yes — if $c_p$ varies sharply (e.g., at fovea/periphery boundary), the metric is *not smooth*; differential geometry tools require $C^k$ regularity.

Honest acknowledgment: this is a *piecewise smooth* metric at best; truly *singular* at sharp transitions.

### State after Iter 6
Local Lorentz metric exists *per stage*, *piecewise smooth*. **Limitation**: singular at sharp $c_p$ transitions; differential geometry requires smoothing or piecewise treatment.

---

## Iteration 7 — Curvature operators on perception manifold

### Construction
Given metric $g_{\mu\nu}^{(s)}$, compute (where smooth):
- Christoffel symbols: $\Gamma^\alpha_{\mu\nu}$
- Riemann tensor: $R^\alpha_{\beta\mu\nu}$
- Ricci tensor: $R_{\mu\nu} := R^\alpha_{\mu\alpha\nu}$
- Scalar curvature: $R := g^{\mu\nu} R_{\mu\nu}$

### What curvature could mean
- $R_{\mu\nu} = 0$: *flat* perception region — uniform $c_p^{(s)}$
- $R_{\mu\nu} \neq 0$: *curved* — $c_p^{(s)}$ varying with position (e.g., fovea→periphery transition)
- *Sign of curvature*: positive = focusing perception (geodesics converge); negative = defocusing

### Adversarial check (Pattern #11 model misspec)
Does *curvature* correspond to a measurable retinal phenomenon? Candidate: *perceptual binding strength variations* — strong binding in fovea (focused), weak in periphery (defocused). 

This is a *hypothesis*, not a derivation. Falsification route: measure binding strength as function of eccentricity; check if it correlates with curvature computed from $c_p^{(s)}(x)$.

### State after Iter 7
Curvature operators are *mathematically defined*. **Operational interpretation as binding strength** is a *hypothesis* requiring empirical test. Currently E0 (motivation only).

---

## Iteration 8 — Perceptual stress-energy from SCC E[u]

### Construction
Use SCC canonical framework. SCC has energy functional:
$$E[u] = \lambda_{cl} E_{cl}[u] + \lambda_{sep} E_{sep}[u] + \lambda_{bd} E_{bd}[u] + \lambda_{tr} E_{tr}[u]$$

Define *perceptual stress-energy tensor* via variational derivative w.r.t. metric:
$$T_{\mu\nu}^{\text{perception}}[u, g] := \frac{2}{\sqrt{-g}} \frac{\delta (\sqrt{-g} \, E[u])}{\delta g^{\mu\nu}}$$

This *follows* SCC canonical framework (no modification to SCC); just *applies* SCC's variational structure to the metric-coupled case.

### Adversarial check (Pattern #15 vacuity)
Does $T_{\mu\nu}^{\text{perception}}$ actually depend on $u$ in a non-trivial way? 

Check: SCC energy terms depend on $u$ and its gradient $\nabla u$ (closure, separation, boundary terms include $|\nabla u|^2$-like terms). Hence $T_{\mu\nu}$ contains $\partial_\mu u \, \partial_\nu u$ contributions — *non-trivially metric-dependent*.

### Connection to Iter 6-7
$T_{\mu\nu}$ becomes the *source term* for curvature in the field equation. Cohesion field $u$ acts as *matter content*; metric responds.

### State after Iter 8
$T_{\mu\nu}^{\text{perception}}$ has *concrete construction* via SCC variational framework. **Constraint compliance verified**: SCC canonical not modified; this is *application* of SCC framework, not extension.

---

## Iteration 9 — Candidate field equation

### Statement
$$\boxed{\;R_{\mu\nu}^{(s)} - \tfrac{1}{2} g_{\mu\nu}^{(s)} R^{(s)} = \kappa^{(s)} \, T_{\mu\nu}^{\text{perception}}[u, g^{(s)}]\;}$$

**Per-stage** (since $c_p^{(s)}$ is per-stage). Coupling $\kappa^{(s)}$ to be determined empirically.

### Interpretation
- LHS: *geometry of perception cone* at stage $s$ (Einstein tensor)
- RHS: *cohesion-field content* coupled to stage's metric
- *Cohesion field* $u$ generates curvature; *cone structure* determines causal reach

### Adversarial check (Pattern #4 RH-specialization)
If true for *all* fields and *all* metrics, does it specialize to a famous open problem? Answer: this is *literally Einstein's equation form* — solving it in general is *as hard as general relativity*. **No general solution claim**.

But: *specific solutions* (Schwarzschild-like for single formation; FLRW-like for uniform field) are tractable analogs.

### State after Iter 9
Field equation candidate is *stated*. **No general-solution claim** (NS-analogy honest). Specific solutions for specific regimes.

---

## Iteration 10 — Approximation regimes

### Identified regimes (NS-analogy)

| Regime | Approximation | Validity | What it computes |
|--------|---------------|----------|------------------|
| **Weak field (Newtonian)** | $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$, $|h| \ll 1$ | Small stimulus; near-uniform $c_p$ | Linear perturbations |
| **Vacuum** | $T_{\mu\nu} = 0$ | No active cohesion field | Free perception evolution |
| **Linearized** | $h_{\mu\nu}$ first order in input | Subthreshold stimulus | Linear response (matches DoG, motion energy in respective stages) |
| **Cosmological** | Homogeneous + isotropic | Uniform field of view | Uniform perception background |
| **Schwarzschild-like** | Single point source | Single isolated formation | One-object perception |
| **Geodesic equation** | Free particle motion | Trajectory of perception unit | Motion perception, saccade trajectories |

### Adversarial check (Pattern #50 typicality vs guarantee)
Each "approximation" is *typical case* under stated regime; not uniform guarantees. *Validity range* must be established per approximation, not asserted globally.

### State after Iter 10
6 approximation regimes identified. **Each is independently testable** — operational program emerges. Field equation does not need general solution.

---

## Iteration 11 — Adversarial gauntlet: Pattern #11 (model misspec)

### Attack
Does the new framework conflate mathematical objects with biological reality?

**Specifically**:
- "Perception cone" = mathematical structure on $(t, x)$-space
- Is this what *retina actually does*? Or is it a *useful idealization*?

### Honest assessment
The cone is a *useful idealization* — like fluid mechanics' "continuum" is for actual molecules. Real retina has:
- Discrete cells (not continuous fields)
- Spatially inhomogeneous $c_p$ (cone breaks at sharp boundaries)
- Stage-specific cones (not single cone)
- Non-instantaneous transitions between stages

### Verdict
Pass — **as a modeling motivation, with explicit Q-conditions**. Statement form:
> *"Under continuum approximation, smooth $c_p^{(s)}(x)$, and stage isolation, the perception cone of stage $s$ admits the Minkowski structure derived above."*

### State after Iter 11
Framework survives #11 *as conditional observation*, not as biological theorem.

---

## Iteration 12 — Pattern #15 (vacuity at biological boundary)

### Attack
Is the perception cone hypothesis class *empty* in actual retina?

### Honest check
- Does *some* version of the cone hold? **Yes**, in approximations.
- Does *the exact cone* (as derived) hold? **No** — sharp $c_p$ transitions break it.

### Mitigation
The framework's claim is *not* "retina exactly satisfies the cone". The claim is:
> *"Under continuum + smoothness + stage-isolation approximations, the cone provides a tractable framework. Deviations from the cone are themselves measurable (e.g., at fovea/periphery boundary)."*

### Verdict
Pass — by *operationally framing deviations as measurable*, the framework is *not vacuous* even when retina doesn't exactly match.

### State after Iter 12
Vacuity attack mitigated by *operational framing of deviations*. Framework becomes a *measurement scaffold*, not a strict description.

---

## Iteration 13 — Pattern #51 (independence assumption)

### Attack
Does the field equation assume independent stages? Independent observers?

### Honest check
- *Stage independence*: framework derives *per-stage* cones. But actual retinal stages are *coupled* (feedback, adaptation).
- *Observer independence*: P1 requires observer-class invariance — but real observers are correlated (shared retinal anatomy).

### Mitigation
- Stage coupling: *intersection of cones* (from Iter 5) partially handles inter-stage relations. Full coupling requires *multi-metric framework* (one per stage, with coupling terms).
- Observer correlation: P1 restricts to *single observer + single condition* — within-subject only. This is honest scoping.

### Verdict
Partial pass. Multi-metric formulation needed for full inter-stage coupling. *Add as OP* (operational problem):

**OP-PFE-1**: Formal multi-metric framework with stage-coupling terms.

### State after Iter 13
Single-stage framework verified; multi-stage needs extension. *OP-PFE-1 registered*.

---

## Iteration 14 — Pattern #28 (subset support)

### Attack
Does the field equation hold on the *entire* stated domain (all of $(t, x)$ × all stages)?

### Honest check
- *Spatial domain*: only where $c_p^{(s)}(x)$ is smooth. Excludes sharp boundaries.
- *Temporal domain*: only on intervals shorter than adaptation time scales ($\tau_a$). Beyond that, $c_p$ itself drifts.
- *Stage domain*: only for stages where cone structure is meaningful. Stage 0 (photons) — cone of light, true $c$. Cortical stages — attention dynamics, attention-cone is *very different*.

### Refined domain
**Effective domain of validity**:
- Spatial: smooth-$c_p$ regions (away from fovea/periphery transition)
- Temporal: short windows (< adaptation time)
- Stage: stages 1–3 (intermediate; not photon Stage 0 or attentional Stage 5)

### Verdict
Subset support significant. *Effective domain* is much smaller than "all retina". Honest scope: medium-spatial + short-temporal + intermediate-stages.

### State after Iter 14
Domain narrowed. Field equation applies to *intermediate-stage smooth-region short-window* regime.

---

## Iteration 15 — Patterns #7, #37, #50 (regularity, uniformity, typicality)

### Combined attack

- **#7 regularity**: requires $c_p^{(s)}(x)$ ∈ $C^2$ for Ricci to exist. Not always satisfied.
- **#37 uniformity**: derivatives in field equation are *pointwise*; uniform validity requires bounded $c_p$ gradients. May fail at transitions.
- **#50 typicality**: "approximation regimes" are *typical case*; uniform guarantees absent.

### Combined mitigation
- Acknowledge: framework is *pointwise* on smooth domain; *uniform* only on bounded-derivative regions.
- *Approximation regimes* are *expected to hold* in typical retinal conditions; *atypical conditions* (rapid eye movement, saccades, sharp boundaries) require separate analysis.

### Verdict
Conditional pass. Framework is *honest about its smooth-regime applicability*.

### State after Iter 15
After 5 adversarial passes (Patterns #11, #15, #51, #28, #7+#37+#50): framework survives as *conditional observation with operational deviations measurement*. Not a biological theorem; a *measurement scaffold*.

---

## Iteration 16 — Operational tests

### Test 1: $c_p^{(s)}$ measurement
**Procedure**: For each stage $s$, measure
- $\tau_s$ from membrane / spike rate
- $\ell_s$ from receptive field / column spacing
- Compute $c_p^{(s)} = \ell_s / \tau_s$
- Verify across multiple recordings; check stability.

**Falsification**: if $c_p^{(s)}$ varies wildly across recordings (e.g., 10× variation), the *per-stage cone* hypothesis fails.

### Test 2: Cone-membership ↔ binding
**Procedure**: Present two stimuli with controlled spatiotemporal separation $(\Delta t, \Delta x)$. Measure perceptual binding (e.g., apparent motion strength).

**Prediction**: Binding is strong iff stimuli are inside the cone ($c_p^{(s)} \Delta t \geq \Delta x$). At the cone boundary, binding is marginal. Outside, no binding.

**Falsification**: If binding strength doesn't correlate with cone membership, the *cone-as-binding-scaffold* hypothesis fails.

### Test 3: Curvature ↔ binding strength variation
**Procedure**: Map $c_p^{(s)}(x)$ across the retinal field. Compute curvature $R^{(s)}(x)$. Compare to *binding strength heatmap* from psychophysics.

**Prediction**: High curvature ↔ rapid binding strength change.

**Falsification**: If binding strength is uniform across regions of different curvature, the *curvature-as-binding* hypothesis fails.

### Test 4: Multi-stage cone intersection ↔ unified perception
**Procedure**: For events $\{e_1, ..., e_n\}$, check whether they lie in $\bigcap_s \mathcal{C}^{(s)}$. Compare to whether they're perceived as a *unified object*.

**Prediction**: Unified perception ⟺ intersection-cone-connected.

**Falsification**: If intersection-cone-connection doesn't predict unification, the *multi-stage intersection* hypothesis fails.

### State after Iter 16
4 operational tests defined. Each *falsifiable*. **First non-aesthetic content**.

---

## Iteration 17 — Connection to SCC E[u]

### Claim
The perceptual stress-energy $T_{\mu\nu}^{\text{perception}}$ defined in Iter 8 is the *variational derivative* of SCC energy functional. This means:

$$T_{\mu\nu}^{\text{perception}}[u, g] = \frac{2}{\sqrt{-g}} \frac{\delta (\sqrt{-g} \, E[u])}{\delta g^{\mu\nu}}$$

### Constraint compliance
- **SCC canonical (CV-1.20) is NOT modified**: $E[u]$ is preserved exactly.
- *New* in this document: the *coupling* of $E[u]$ to a *metric* (via $\sqrt{-g}$ density). This is *application* of SCC, not redefinition.

### What changes
SCC, viewed under this framework:
- $u$ minimizes $E[u]$ on *flat* perception space (Stage 1-2 weak field limit)
- $u$ + curvature: $u$ minimizes $E[u]$ *subject to* curvature constraint imposed by stage geometry
- Field equation: *geometry adapts to cohesion field*; *cohesion field minimizes energy in adapted geometry*

This is *self-consistent dynamics*, exactly like Einstein's equation: spacetime curvature ↔ matter distribution.

### Adversarial check (Pattern #11 misspec)
Does SCC's $E[u]$ actually represent *perceptual energy*? Or is it a *modeling convenience*?

Honest answer: SCC's $E[u]$ is a *modeling framework* — its components (E_cl, E_sep, E_bd, E_tr) are *abstractions of perceptual cohesion phenomena*. Connection to *physical energy* is *analogical*.

But: this is also true of Einstein's $T_{\mu\nu}$ — it represents *physical energy-momentum*, but the deeper *origin* of energy-momentum (Standard Model fields) is *physics*, not the equation itself. The equation *couples* geometry to whatever energy-momentum is *given*.

Similarly: PFE *couples* perception cone geometry to whatever cohesion-energy is *given*. The *specific form* of $E[u]$ comes from SCC (substrate); PFE just *couples* it geometrically.

### State after Iter 17
SCC E[u] connects naturally as the stress-energy source. **SCC substrate** (preserved canonical) and **PFE** (constructed here) are *complementary* — SCC provides energy content, PFE provides geometric framework.

---

## Iteration 18 — Connection to PAI $\Delta_{\text{interp}}$

### Claim
PAI's *interpretation gap* $\Delta_{\text{interp}}$ between perception and action interpretations of a formation has a natural realization in PFE:

$$\Delta_{\text{interp}}(F) \sim \text{geodesic distance between } (g_{\mu\nu}^{\text{perception}}[F], g_{\mu\nu}^{\text{action}}[F])$$

where the two metrics arise from cohesion field $u$ viewed under *perception observer class* vs *action observer class*.

### What this means operationally
- *Small* $\Delta_{\text{interp}}$ = perception cone and action cone *coincide* → formation is *PA-formation* (per PAI vocabulary)
- *Large* $\Delta_{\text{interp}}$ = cones diverge → formation is *PA-incompatible*
- *Bridge condition*: a formation is action-grasped iff perception cone *includes* action cone

### Constraint compliance
- **PAI canonical (PAI-PIVOT-2026-05-21) NOT modified**: all PAI vocabulary preserved as DEFINITION-DRAFT.
- *New* in PFE: $\Delta_{\text{interp}}$ has *candidate operationalization* via geodesic distance.

### Adversarial check (Pattern #11)
Does *geodesic distance between two metrics* really capture interpretation gap?

Honest answer: it's *a candidate*. Other candidates exist (KL divergence between perception/action probability distributions; categorical natural transformation defect). Geodesic-distance candidate has *specific advantage*: it's *geometric*, matching PFE's framework.

### State after Iter 18
PAI's $\Delta_{\text{interp}}$ has *candidate operational form* via PFE geodesic distance. **PAI substrate** (preserved canonical) and PFE are *complementary*.

---

## Iteration 19 — Minimal compression of framework

### Reduced form

**Primitives** (replaces 11_minimal_core's P1-P5):
1. *Event* $(t, x)$ — operationally defined per stage
2. *Stage rate* $c_p^{(s)}$ — operationally measurable per stage
3. *Cohesion field* $u_t$ — SCC substrate primitive (reused)
4. *Perception cone* $\mathcal{C}^{(s)}$ — derived from postulates
5. *Per-stage metric* $g_{\mu\nu}^{(s)}$ — derived from cone

**Postulates** (replaces 11_minimal_core's constraints):
1. **P1 perceptual relativity** (within observer equivalence class)
2. **P2 limiting rate per stage** ($c_p^{(s)}$ exists)

**Derived**:
- σ relation (Tier 2): *consequence* of P1, P2
- Perception cone: *consequence* of P2
- Local metric: *cone in infinitesimal form*
- Stress-energy: *SCC E[u] variational derivative*
- Field equation: *Einstein form coupling curvature and energy*
- Approximation regimes: *standard relativity approximations* (weak field, vacuum, geodesic, etc.)

**Operational tests** (4 falsification routes):
1. $c_p^{(s)}$ stability across recordings
2. Cone membership ↔ binding strength
3. Curvature ↔ binding variation
4. Multi-stage intersection ↔ unified perception

**Open problems**:
- OP-PFE-1: Multi-metric framework for stage coupling
- OP-PFE-2: Empirical determination of coupling constant $\kappa^{(s)}$
- OP-PFE-3: Existence/uniqueness theorem for stage-1 vacuum solution
- OP-PFE-4: Connection to PAI $\Delta_{\text{interp}}$ alternative candidates
- OP-PFE-5: Cortical (Stage 5) cone formulation

### Compression check
2 postulates + 5 primitives + 4 tests + 5 OPs = **16 items** to characterize entire framework. Versus 11_minimal_core's 5+5+5 = 15 items. **Similar compression**, but PFE has *more structure* (field equation form) and *more falsifiability* (4 explicit operational tests).

### State after Iter 19
Framework compressed. Structure visible. **Compression succeeded** — framework is *not bloated*.

---

## Iteration 20 — Final report

### Executive summary
20 iterations of derive + adversarial verify produced a **conditional, operationally testable framework** for perception cone + Einstein-style field equation, built on existing SCC + PAI substrates without modifying canonical files.

### What was added (vs prior state)
- **Two postulates** (P1, P2) — *empirical claims*, falsifiable
- **Derived σ relation** — replaces Tier 2 primitive assertion
- **Per-stage cone hierarchy** — operational, not nested
- **Local Lorentz metric** per stage — piecewise smooth
- **Field equation candidate** (Einstein form) — no general solution claim
- **6 approximation regimes** — testable per regime
- **4 operational tests** — falsifiable
- **5 OPs** (OP-PFE-1..5) — precise routes

### What was NOT done (audit trail)
- SCC canonical: 0 modifications
- PAI canonical: 0 modifications
- 8 SCC retractions: 0 revivals
- 31 prior TC deletions: preserved as audit trail
- No new framework name registered as canonical (PFE is descriptive label only)

### Adversarial gauntlet results
- Pattern #11 (misspec): pass *as conditional observation*, not biological theorem
- Pattern #15 (vacuity): pass via *operational framing of deviations*
- Pattern #51 (independence): partial pass; OP-PFE-1 for multi-stage coupling
- Pattern #28 (subset): pass with *narrow effective domain*
- Patterns #7, #37, #50: conditional pass on *smooth regime*
- Pattern #18 (tautology): pass — σ now *derived* from postulates, not asserted

### Final standard compliance
- *Smaller*: 16 framework items vs prior 32 TCs
- *Sharper*: each item operational or precisely scoped
- *More falsifiable*: 4 explicit tests + 5 OPs with routes
- *Not merely longer*: replaced exploration with *structured framework*

### Where framework currently sits

| Register | Content |
|----------|---------|
| MODELING-MOTIVATION | Einstein-style form of perception field equation |
| OPERATIONAL-DEFINITION | $c_p^{(s)} = \ell_s / \tau_s$ per stage |
| CONDITIONAL-OBSERVATION | σ = cone-membership *under continuum approximation* |
| MATH-FACT | Standard tensor calculus on $g_{\mu\nu}^{(s)}$ |
| OPEN-PROBLEM | OP-PFE-1..5 |
| EXPLORATION-RECORD | All 20 iterations themselves (this document) |

### Most important open question
**The load-bearing question**: is *SCC E[u]* really the *correct* stress-energy source? Alternatives:
- Friston's free energy F
- Fisher information density
- Predictive coding precision-weighted error
- Sparse coding L1-penalized loss

Each alternative gives a *different* PFE. SCC E[u] is chosen because:
- Preserves canonical (no modification)
- Variational structure already exists
- Diagnostic vector (Bind, Sep, Inside, Persist) provides interpretable components

But **this choice is empirical** — must be tested by checking which $E$-functional produces field equation predictions matching retinal data.

### Next cuts recommended
1. **Cut perception-cone smoothness**: framework requires $c_p^{(s)} \in C^2$. At sharp transitions (fovea/periphery), framework fails. *Need: piecewise treatment*.
2. **Cut single-rate-per-stage**: $c_p^{(s)}$ varies spatially. *Need: $c_p^{(s)}(x)$ field formulation*.
3. **Cut Einstein-form aesthetic**: maybe field equation should be *different* — e.g., *Yang-Mills* or *gauge theory* form for perception channels. Test alternatives.
4. **Cut SCC E[u] selection**: test alternative energy functionals.
5. **Cut continuum approximation**: discrete cell structure may matter — explore *cellular automaton* or *discrete differential geometry* version.

---

## 21 (Reflection — meta-iteration)

Reading the 20 iterations: the framework *survives* adversarial gauntlet — but always *conditionally*. The *honest assessment*:

> Framework is **structurally well-defined**, **operationally testable** (4 falsification routes), and **constraint-compliant** (no canonical modification). But its *truth* depends on empirical validation of tests 1-4, which are *not yet done*.

Whether the perception cone exists in retina *as a real structure* is **an empirical question**, not yet answered. The framework provides *a way to ask* the question precisely.

This is *the* right register: framework as *measurement scaffold*, not as *theorem*.

---

*Pass 11 v0. 20 iterations of derive + adversarial verify. Single framework document. Constraint-compliant. Operationally testable. Awaits empirical validation. Substrate SCC + PAI preserved unchanged.*
