---
type: working/sensing_pipeline/pass12_op_pfe_advancement
version: v0
date: 2026-05-26
status: ACTIVE — Pass 12 Phase D (Tasks 16-20)
purpose: |
  Advance (not resolve) the 5 OP-PFE entries from 12_ Iter 19, plus the 6 new OPs registered in Phases A-C.
  Each task: formal draft / candidate enumeration / proof attempt / comparison / extension proposal.
  Honest goal: turn open problems from "unspecified" to "specifically articulated with attack routes".
register: ADVANCEMENT (open problems advanced; not closed)
parent: 00_INDEX
prev: 15_operational_test_protocols
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
  pai_canonical_edits: 0
  modifies_12_perception_cone: 0
  ops_advanced: 5 original + 6 Pass-12-added = 11 OPs in scope
  ops_closed: 0 (Pass 12 advances; closure is Pass 13+)
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[15_operational_test_protocols]] · Pass 12 Phase D

# Pass 12 Phase D — OP-PFE Advancement (Tasks 16-20)

**Scope**: each of the 5 original OP-PFE entries (Iter 19) receives substantive development. OPs registered in Phases A-C (OP-PFE-6 through OP-PFE-11) are also noted but not separately advanced — they emerged from Phase A-C verification and inherit the development of their parent issues.

**Method**: each task selects one of the 5 OP-PFE entries and produces (i) formal restatement, (ii) candidate solution sketches with pros/cons, (iii) explicit obstacle that prevents closure, (iv) recommended next step.

---

## Task 16 — OP-PFE-1: Multi-metric coupling framework draft

### OP statement (restated)
Pass 11 derives a *per-stage* metric $g_{\mu\nu}^{(s)}$ but treats stages as *independent*. Real retinal stages are *coupled* (feedback, gain control, adaptation). A multi-metric framework must formalize this coupling without violating the per-stage cone structure.

### Three candidate formalisms

**Candidate A: Bundle of metrics (vertical product)**

Construct a fiber bundle $\pi: E \to B$ where:
- $B$ = base spacetime $(t, x, y)$ shared across stages
- Fiber over each point = a copy of all metrics $\{g_{\mu\nu}^{(s)}\}_{s=1}^{S}$
- Sections of $E$ = stage-wise metric assignments

Inter-stage coupling: introduce a *connection* on $E$ that relates $g^{(s)}$ to $g^{(s+1)}$.

**Pros**: standard differential-geometric machinery; well-defined.
**Cons**: connection is *free* — no principle to choose it; just bookkeeping.

**Candidate B: Sheaf of cones (categorical)**

For each open set $U$ of spacetime, assign the set of *consistent* cone configurations $\{\mathcal{C}^{(s)}|_U\}$ such that the *intersection* $\bigcap_s \mathcal{C}^{(s)}|_U$ is non-empty.

Restriction maps: when $U' \subset U$, restrict cones to smaller open set. Sheafification ensures local consistency glues to global.

**Pros**: handles intersection-cone structure naturally (Test 4 hypothesis is just *sections of the intersection sheaf*); topological invariance under coordinate change.
**Cons**: heavy categorical machinery for what may be a simple physical question; computing with sheaves is hard.

**Candidate C: Effective combined metric**

Define a single *effective* metric:
$$g_{\mu\nu}^{\text{eff}}(x) := \sum_s w_s(x) \, g_{\mu\nu}^{(s)}(x)$$
where $w_s(x)$ are stage-weight functions with $\sum_s w_s = 1$.

Weights $w_s$ encode which stage *dominates* perception at each position/condition (foveal vs peripheral, high-contrast vs low-contrast, etc.).

**Pros**: single metric — standard GR-like analysis applies; weights are operationally measurable (e.g., via lesion studies).
**Cons**: collapses per-stage cone structure; loses the *intersection-cone* prediction that distinguishes PFE.

### Recommendation

**Hybrid**: Candidate B (sheaf) for *theoretical formulation*, Candidate A (bundle) for *practical computation*, Candidate C (effective) for *coarse-grained predictions* like average binding strength.

The three are *not in conflict* — they are different levels of detail.

### Obstacle to closure
The actual *coupling rule* between stages (i.e., how does Stage 2 metric influence Stage 3 metric) is not derivable from PFE alone. It requires *biological input*: which inter-stage signals exist (feedback, adaptation), and how they transform metric components.

For a formal closure, need:
- Empirical measurement of inter-stage signal magnitudes
- Mapping from biological signals to metric perturbations

This is *not* purely theoretical — it requires data.

### Next step
Define a *minimal model*: assume *one* coupling parameter $\gamma$ between Stage 2 and Stage 3 (the most biologically established coupling: bipolar→ganglion feedforward + amacrine feedback). Compute predictions as function of $\gamma$. If predictions are testable, $\gamma$ becomes a measurable parameter; OP-PFE-1 partially closes.

### Status after Task 16
**ADVANCED** from "unspecified" to "three formal candidates + recommended hybrid + minimal model proposal". Closure requires empirical input.

---

## Task 17 — OP-PFE-2: $\kappa^{(s)}$ empirical determination plan

### OP statement (restated)
Task 7 established $\kappa^{(s)} = c \cdot \ell_s$ with $c$ a dimensionless prefactor of order unity. The *value* of $c$ is empirically undetermined.

### Measurement procedure (proposed)

**Step 1 — choose a regime where curvature is computable from first principles**

Foveal-periphery transition for Stage 3 (M ganglion): $c_p^{(s)}(x)$ varies systematically (Task 13 setup). $R^{(s)}(x)$ at the transition is computable:
$$R^{(s)}(x) \sim \frac{(\partial_x c_p)^2}{c_p^2}$$

For $c_p$ varying by factor of ~3 across a ~5° eccentricity range (≈ 4 mm on retina):
$$R^{(s)} \sim (3/4)^2 / c_p^2 \approx 0.5 / c_p^2 \text{ in (rate units)}^{-2}$$

In dimensional units after $\tilde{t} = c_p t$ substitution: $[R] = L^{-2}$.

**Step 2 — choose an observable that depends on $\kappa$**

From the field equation: a cohesion-source perturbation $\delta u$ creates metric perturbation $\delta g \sim \kappa \delta T \sim \kappa \delta u^2$ (since $T \sim u^2$ for SCC energies). The resulting *binding-strength change* relative to background should be observable.

**Step 3 — measure binding-change vs cohesion-change**

Vary stimulus contrast (proxy for $\delta u$). Measure resulting binding-strength change. Fit:
$$\Delta \text{Bind}(x) \propto \kappa^{(s)} \cdot \rho_{\text{stim}}(x)$$

The proportionality constant gives $\kappa^{(s)}$.

**Step 4 — cross-validate**

Take measured $\kappa^{(s)}$ from Stage 3, *predict* $\kappa^{(s')}$ for Stage 2 via $\kappa^{(s')} = c \cdot \ell_{s'}$ with the *same* dimensionless $c$. Test the prediction with Stage 2 binding measurements.

If $c$ is *consistent* across stages (same value of dimensionless prefactor), candidate $\kappa = c \ell$ form is supported. If $c$ differs >2× across stages, the form is wrong (e.g., $\kappa$ depends on stage in a non-$\ell$ way).

### Obstacle
The procedure requires *measuring binding change as function of contrast* — this is psychophysics protocol Test 2 extended. Substantial empirical effort.

Additionally: the proportionality $T \sim u^2$ assumed above is *one* candidate; SCC's $E[u]$ has multiple terms (closure, separation, boundary, transport) with different $u$-dependences. The actual variational derivative is more complex than $u^2$.

### Status after Task 17
**ADVANCED** from "unspecified" to "4-step measurement procedure with cross-validation". Closure requires empirical execution (Tests 2-3 extended).

### Connection to other tasks
- Test 2 (Task 12) is *step 3* in disguise — extending Test 2 to multiple contrasts gives $\kappa$ measurement
- Test 3 (Task 13) is the *background curvature map* needed for context
- Multi-stage cross-validation requires Tests at multiple stages — significant new experiments

---

## Task 18 — OP-PFE-3: Vacuum solution existence formal proof attempt

### OP statement (restated)
Iter 19 asked for "existence/uniqueness theorem for stage-1 vacuum solution". After Task 8, we know 1+2D Lorentzian vacuum has only locally-flat solutions plus conical defects (no Schwarzschild). This task attempts a *formal* existence theorem.

### Theorem candidate

**Theorem (proposed)**: Let $(M, g^{(s)})$ be a 1+2D Lorentzian manifold with metric $g^{(s)}$ such that $R_{\mu\nu}^{(s)} = 0$ everywhere except at a finite set of points $\{p_1, \ldots, p_n\}$ where conical singularities are allowed. Then:

(a) $g^{(s)}$ is *locally Minkowski* on $M \setminus \{p_i\}$, with rate $c_p^{(s)}$.

(b) Each conical singularity $p_i$ has *deficit angle* $\Delta\theta_i \in [0, 2\pi)$ characterized by:
$$\Delta\theta_i = 2\pi - \theta_{\text{measured}}(p_i)$$
where $\theta_{\text{measured}}(p_i)$ is the angle obtained by integrating around a small loop encircling $p_i$.

(c) Global topology is constrained by Gauss-Bonnet:
$$\sum_i \Delta\theta_i = 2\pi \chi(M)$$
where $\chi(M)$ is the Euler characteristic of $M$.

### Proof sketch

(a) follows from the 3D Weyl-vanishing identity (Task 8): $R_{\mu\nu} = 0 \Rightarrow R_{\alpha\beta\mu\nu} = 0$ pointwise. Hence local flatness.

(b) The deficit-angle definition is standard for conical singularities — coordinatize a small disk around $p_i$ and measure how much the angular coordinate fails to close at $2\pi$.

(c) Gauss-Bonnet for a Lorentzian 2D surface (after appropriate Wick rotation or in the spatial slice at fixed $t$) — the curvature concentrated at conical singularities sums to $2\pi \chi$.

### Status of "proof"

This is a *sketch* — the rigorous proof would require:
- Careful treatment of Lorentzian signature in Gauss-Bonnet (the standard theorem is Riemannian)
- Specification of regularity class for $g^{(s)}$ (smooth except at $\{p_i\}$? distributional curvature?)
- Verification that conical singularities are the *only* admissible singularities in 1+2D vacuum (no curvature concentrated on lines or 2-surfaces?)

Reference: Deser, Jackiw, 't Hooft (1984) "Three-dimensional Einstein gravity: dynamics of flat space" — proves analogous theorem for 2+1 gravity. Their setup is *exactly* the perception cone analog (replace gravitational $G$ with PFE's $\kappa$).

### Obstacle to closure
The proof in Deser-Jackiw-'t Hooft is for *exact* 2+1 gravity. Adapting to PFE requires:
- Establishing that $\kappa T_{\mu\nu}^{\text{perception}}$ has the same defect-creating effect as $G T_{\mu\nu}^{\text{matter}}$ — likely yes if $T$ is concentrated at a point (single-cohesion source)
- The defect-angle formula $\Delta\theta = 8\pi G m$ in 2+1 gravity becomes $\Delta\theta = \kappa^{(s)} U_{\text{cohesion}}$ in PFE, where $U_{\text{cohesion}}$ is the integrated cohesion energy at the source
- Verifying this is the *correct* analog

### Status after Task 18
**ADVANCED** from "unspecified" to "theorem stated, proof sketched, references to closest analog (Deser-Jackiw-'t Hooft)". Closure requires rigorous adaptation of DJ'tH to PFE setting.

### Recommended next step
Read Deser, Jackiw, 't Hooft (1984) in detail. Map each step to PFE notation. Identify any step that fails to adapt (likely candidate: how the SCC $E[u]$ source differs from a point-mass source).

---

## Task 19 — OP-PFE-4: Alternative $\Delta_{\text{interp}}$ candidates comparison

### OP statement (restated)
Iter 18 proposed $\Delta_{\text{interp}}(F) \sim \text{geodesic distance between } (g^{\text{perception}}, g^{\text{action}})$. The "geodesic distance between two metrics" choice is one of *several* candidates for operationalizing PAI's interpretation gap.

### Four candidate operationalizations

**Candidate $\alpha$: Geodesic distance in metric space**

$\Delta^{(\alpha)} := d_{\text{Wasserstein}}(g^{P}, g^{A})$ where $d$ is computed in the *space of metrics on $M$* (a Riemannian metric on the space of metrics).

**Pros**:
- Geometric, matches PFE framework
- Symmetric ($\Delta^{(\alpha)}(F) = \Delta^{(\alpha)}(F')$ for permutation)
- Vanishes iff metrics coincide
**Cons**:
- "Distance in space of metrics" requires choosing a Riemannian structure on the space of metrics (DeWitt metric is one choice; not unique)
- Computationally hard

**Candidate $\beta$: KL divergence between perception/action probability distributions**

$\Delta^{(\beta)}(F) := D_{KL}(P_{\text{percept}}(F) \| P_{\text{action}}(F))$ where the probabilities are over outcomes given the formation.

**Pros**:
- Information-theoretic
- Operationally measurable (just count outcomes)
- Standard in cognitive science
**Cons**:
- Asymmetric ($D_{KL}(P\|Q) \neq D_{KL}(Q\|P)$); doesn't match symmetry of PFE
- Requires probabilistic structure not derived from PFE
- "Outcome" definition is task-specific

**Candidate $\gamma$: Categorical natural transformation defect**

$\Delta^{(\gamma)}(F) := $ obstruction to a natural transformation between *perception functor* and *action functor* in PAI's categorical framework.

**Pros**:
- Matches PAI's categorical vocabulary
- Coordinate-free
- Composes well across formations
**Cons**:
- Categorical "obstruction" is itself an open problem in PAI (PAI-CAT-001 if it existed)
- Hard to compute
- May require category theory tools not yet developed

**Candidate $\delta$: Wasserstein distance between perception/action measures**

$\Delta^{(\delta)}(F) := W_2(\mu^{P}_F, \mu^{A}_F)$ where $\mu^{P}_F$ is the perception-induced probability measure on outcomes given $F$, and similarly $\mu^{A}_F$ for action.

**Pros**:
- Symmetric (unlike KL)
- Geometric (transport-based)
- Connects to PFE via OT structure
- SCC code already has `transport.py` with Sinkhorn OT (immediate computational support)
**Cons**:
- Requires probability measures (same difficulty as $\beta$)
- Wasserstein-2 has choice of ground metric

### Comparison matrix

| Candidate | PAI fit | Falsifiable | Computable | Geometric | Recommendation |
|-----------|---------|-------------|------------|-----------|----------------|
| $\alpha$ (metric geodesic) | High | Indirect | Low | Yes | Theory framework |
| $\beta$ (KL) | Medium (asymmetric) | High | High | No | Easy test |
| $\gamma$ (categorical) | High | Low | Very low | Coord-free | Long-term theory |
| $\delta$ (Wasserstein) | High | High | Medium-high (SCC has OT) | Yes | **Recommended** |

### Recommendation

Use **$\delta$ (Wasserstein)** as the primary operationalization. Justifications:
- Symmetric (matches geometric character of PFE)
- Computable via existing SCC `transport.py` infrastructure
- Falsifiable (provides numerical $\Delta_{\text{interp}}$ value testable against PAI substrate predictions)
- Connects naturally to PFE via OT-on-curved-spacetime literature

Keep $\alpha$ as theoretical framework (geodesic in space of metrics is the geometric interpretation; Wasserstein is the operational shadow).

### Obstacle to closure
PAI canonical doesn't yet *commit* to an operationalization for $\Delta_{\text{interp}}$ (it remains in DEFINITION-DRAFT register). PFE's choice ($\delta$ Wasserstein) is a *proposal*; binding it to PAI requires PAI substrate update — which is *outside Pass 12 scope* (PAI canonical edits = 0).

### Status after Task 19
**ADVANCED** from "geodesic distance only" to "4 candidates compared, $\delta$ Wasserstein recommended with computational support already in SCC code". PAI substrate decision is upstream gating dependency.

---

## Task 20 — OP-PFE-5: Cortical (Stage 5) cone formulation

### OP statement (restated)
Pass 11 framework treats stages 1-4 (photoreceptor through ganglion) and *attentional* binding (Stage 5) but doesn't precisely formulate Stage 5's cone. Iter 4 lists attentional $c_p \approx 1$ m/s (revised to 0.3 m/s in Task 2). The *cortical* (V1/V2) stage is intermediate; its cone is unspecified.

### Three formulation attempts

**Attempt 1: Cortical cone via V1 receptive field geometry**

Set $\ell_{\text{V1}} := $ orientation column width (~500 μm) or hypercolumn width (~1-2 mm)
Set $\tau_{\text{V1}} := $ membrane time constant (~10 ms) or response onset (~40 ms)

$c_p^{\text{V1}} \approx 0.5\text{mm} / 0.01\text{s} = 50$ mm/s using membrane time
$c_p^{\text{V1}} \approx 1.5\text{mm} / 0.04\text{s} = 37.5$ mm/s using onset

Both ≈ 40-50 mm/s. Within the ganglion-to-attentional range. **Plausible.**

**Concern**: V1 has *long-range horizontal connections* (1-3 mm spread). Long-range connections create *non-local* interactions that may break the cone structure (which assumes local-only propagation).

**Resolution**: long-range connections enable *fast lateral propagation* — effectively *increasing* $c_p^{\text{V1}}$ for some stimuli (oriented edges aligned with horizontal connection direction). Anisotropic cone — wider along the dominant orientation, narrower across.

**Refined**: $c_p^{\text{V1}}(\theta) := \ell(\theta) / \tau$ where $\ell(\theta)$ depends on orientation $\theta$ relative to the horizontal-connection axis. Cone becomes *direction-dependent ellipse*, not a circle.

**Attempt 2: Cortical cone via cortical wave propagation**

Cortical traveling waves (gamma, alpha) propagate at ~10-100 mm/s across cortex (Sato et al. 2012). Use this as $c_p^{\text{V1}}$:

$c_p^{\text{V1,wave}} \approx 10-100$ mm/s

Consistent with Attempt 1. **Same order.**

**Concern**: cortical waves are *not* propagation of perceptual reachability — they are *correlations* among already-active neurons. The σ relation should be about *what can causally influence what perceptually*, not about *spontaneous wave activity*.

**Resolution**: when a stimulus arrives and propagates through cortical machinery, the relevant rate *is* limited by the local cortical conduction velocity. Cortical waves and stimulus-driven propagation share the same conduction substrate. So $c_p^{\text{V1}}$ from wave measurements is operationally relevant.

**Attempt 3: Cortical cone via gamma-band binding window**

Gamma oscillations (~40 Hz, period ~25 ms) are hypothesized substrates for binding (Singer 1999; Fries 2005). Binding window for gamma-coupled binding: ~25 ms.

Spatial extent of synchronous gamma: ~5-10 mm of cortex.

$c_p^{\text{V1,gamma}} \approx 7\text{mm} / 0.025\text{s} \approx 280$ mm/s

**Larger by ~5×** than Attempts 1, 2. Reflects the *binding-mediated* effective propagation, which is faster than local conduction because gamma synchronization is *phase-coupled* not *signal-propagated*.

**Verdict on cortical $c_p$**: depends on which substrate we're modeling. Conduction-velocity ≈ 50 mm/s; gamma-binding ≈ 280 mm/s. PFE could use *either* — but they describe *different* perceptual processes.

### Multi-process cortical cone

Recommendation: split Stage 5 into substages:
- **Stage 5a (V1 local)**: $c_p^{\text{5a}} \approx 50$ mm/s — local feature binding
- **Stage 5b (V1-V2 gamma)**: $c_p^{\text{5b}} \approx 280$ mm/s — cross-area phase binding
- **Stage 6 (attentional)**: $c_p^{\text{6}} \approx 300$ mm/s — top-down attention shift (corrected from Iter 4's 1 m/s = 1000 mm/s)

Each substage gets its own cone. *Hierarchical multi-cone* structure extends naturally from retinal stages.

### Obstacle to closure
- Anisotropic cone (Attempt 1 refinement) requires *direction-dependent* metric, which generalizes $g_{\mu\nu}^{(s)} = \text{diag}(-c_p^{(s)2}, 1, 1)$ to non-diagonal forms
- The *split* into 5a/5b/6 is a *hypothesis* — needs empirical justification
- Long-range connections may not have simple cone description (Pattern #11 misspec attack possible)

### Status after Task 20
**ADVANCED** from "Stage 5 formulation deferred" to "three formulation attempts, multi-process split recommended, anisotropic cone identified as required extension".

### New OP registered
**OP-PFE-12**: Formalize anisotropic perception cone (direction-dependent $c_p^{(s)}(\theta, x)$) consistent with PFE structure. Required for V1 long-range connection modeling.

### Connection to Phase B Task 9
The multi-stage motion-energy reproduction (OP-PFE-9) could be tested at cortical stages with the substage split: 5a (local), 5b (gamma-binding), 6 (attentional) span ~50, 280, 300 mm/s. Combined with retinal 0.05, 10, 100 mm/s (Task 2 corrected), the full velocity range covered by PFE is *0.05 to 300 mm/s* — over 4 orders of magnitude. Motion-energy filters cover ~1-1000 mm/s, so PFE multi-stage substantially covers this range. **OP-PFE-9 partially satisfied** by cortical-stage inclusion.

---

## Phase D Summary

| Task | OP | Verdict | Confidence | Effect on framework |
|------|----|---------| -----------|---------------------|
| 16 | OP-PFE-1 (multi-metric) | ADVANCED | Medium | 3 candidates + hybrid recommendation; closure needs empirical input |
| 17 | OP-PFE-2 ($\kappa$ measurement) | ADVANCED | Medium-high | 4-step procedure with cross-validation; closure via Tests 2-3 extension |
| 18 | OP-PFE-3 (vacuum) | ADVANCED | Medium | Theorem stated + DJ'tH analog; closure via rigorous adaptation |
| 19 | OP-PFE-4 ($\Delta_{\text{interp}}$) | ADVANCED | Medium-high | Wasserstein recommended; SCC `transport.py` already supports computation |
| 20 | OP-PFE-5 (cortical cone) | ADVANCED | Medium | Multi-process split (5a/5b/6); anisotropic cone as new requirement |

### Aggregate Phase D verdict

**All 5 original OP-PFE entries ADVANCED**. None closed. Closure paths identified for each:
- OP-PFE-1: empirical inter-stage coupling measurements
- OP-PFE-2: extended Test 2 with contrast variation
- OP-PFE-3: rigorous adaptation of DJ'tH theorem
- OP-PFE-4: PAI canonical decision (out of Pass 12 scope)
- OP-PFE-5: anisotropic cone formalization (new OP-PFE-12)

### Aggregate after Phases A-D

Pass 12 has added these OPs to the framework:
- **OP-PFE-6**: Consistent operational convention for $c_p^{(s)}$ (Task 2)
- **OP-PFE-7**: Resolve P1 circularity via reachability reformulation (Task 3)
- **OP-PFE-8**: Conical-defect angle vs perceived-angle near salient point stimulus (Task 8)
- **OP-PFE-9**: Multi-stage PFE motion-energy spectrum (Task 9; partially satisfied by Task 20)
- **OP-PFE-10**: Attentional-capture geodesic-bending prediction (Task 10)
- **OP-PFE-11**: Execute Test 1 on Chichilnisky CRCNS dataset (Task 15)
- **OP-PFE-12**: Anisotropic perception cone (Task 20)

Original 5 OPs + 7 Pass-12 added OPs = **12 OPs in framework**. Status:
- 12 advanced/open
- 0 closed

### What was NOT done in Phase D
- No OP closed (closure is Pass 13+)
- No rigorous proof of vacuum theorem (sketch only)
- No numerical computation of $\kappa^{(s)}$ value
- No actual Wasserstein computation for $\Delta_{\text{interp}}$ (SCC code exists but not invoked here)
- No anisotropic cone formalization (just identified as required)

---

*Phase D v0. 5 tasks, 5 OP-PFE advancements. 5 original OPs + 7 new = 12 OPs in framework. canonical/SCC/PAI/8-retractions 0 modifications. Next: Phase E Extended Adversarial Gauntlet (Tasks 21-23).*
