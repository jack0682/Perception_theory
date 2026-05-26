---
type: working/sensing_pipeline/pass12_adversarial_extensions
version: v0
date: 2026-05-26
status: ACTIVE — Pass 12 Phase E (Tasks 21-23)
purpose: |
  Three new adversarial patterns extending the 15-pattern gauntlet used in Pass 3-9.
  Pattern #61: gauge invariance / general covariance.
  Pattern #62: Cauchy problem / initial value well-posedness.
  Pattern #63: conservation laws / Noether currents.
  Each attack: verdict + downstream consequence + repair candidate.
register: ADVERSARIAL_GAUNTLET
parent: 00_INDEX
prev: 16_op_pfe_advancement
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
  pai_canonical_edits: 0
  modifies_12_perception_cone: 0
  patterns_executed: 3 (extending the 15-pattern gauntlet of Pass 3-9)
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[16_op_pfe_advancement]] · Pass 12 Phase E

# Pass 12 Phase E — Extended Adversarial Gauntlet (Tasks 21-23)

**Scope**: extend the 15-pattern gauntlet (Patterns #4, #5, #6, #7, #11, #15, #18, #22, #28, #29, #37, #40, #41, #46, #50, #51, #52) by three GR-inspired patterns specifically targeted at Einstein-form theories.

**Inherited state**: Phase B established PFE dimensional consistency, partial linear-regime match, vacuum-is-defects-only. Phases A, D weakened postulates and advanced OPs. Phase E asks: can PFE survive the *structural* attacks that GR itself must survive?

---

## Task 21 — Pattern #61: Gauge invariance / general covariance

### Attack
Einstein's GR is *generally covariant*: physical content is invariant under arbitrary smooth coordinate transformations of spacetime. The equations have the *same form* in any coordinate system.

Does PFE have this property? If not, PFE has *preferred coordinates* — it picks out a specific time direction, specific spatial orientations — and is therefore *not* a fully covariant theory. Such a theory may *appear* geometric but is *actually* coordinate-dependent.

### Specific test

**Test A: Time-reparametrization invariance**

Under $t \mapsto t' = f(t)$ with $f$ smooth and monotonic, does PFE transform covariantly?

- Metric: $g_{\mu\nu}^{(s)} = \text{diag}(-c_p^{(s)2}, 1, 1)$ depends on coordinate $t$ through implicit choice of unit. Under $t \mapsto t' = f(t)$:
  $$g_{00}'(t') = -c_p^{(s)2} (dt/dt')^2 = -c_p^{(s)2} / (df/dt)^2$$
- Other components unchanged.
- This is *covariant* iff we let $c_p^{(s)}$ be a *function of spacetime point* (not a constant) that transforms as $c_p'^{(s)} = c_p^{(s)} / (df/dt)$.

But P2 commits to $c_p^{(s)}$ being *invariant within $\mathcal{O}$*. If $\mathcal{O}$ is closed under time reparametrization, $c_p^{(s)}$ transforms — contradicting P2's invariance claim.

**Resolution candidate**: P2 is *not* time-reparametrization invariant. The equivalence class $\mathcal{O}$ is restricted to observers with *the same clock* (i.e., the same time parametrization).

**Verdict on Test A**: PFE is NOT time-reparametrization invariant. $\mathcal{O}$ restricts to "same-clock observers" (within-individual same-recording-rate).

**Test B: Spatial coordinate reparametrization**

Under spatial diffeomorphism $x \mapsto x' = \phi(x)$, $g_{ij}$ transforms tensorially. The flat spatial part of $g_{\mu\nu}^{(s)}$ (Iter 6: $\text{diag}(1, 1)$ in spatial slots) remains *Euclidean* in new coordinates only if $\phi$ is an isometry (rotation + translation).

If $\phi$ is a general diffeomorphism (e.g., warping), the spatial metric becomes non-Euclidean. PFE in new coordinates would have:
$$g_{ij}' = (\partial \phi / \partial x)^T (\partial \phi / \partial x)$$

This is *not* the original PFE form ($\text{diag}(1,1)$). The equation $G_{\mu\nu} = \kappa T_{\mu\nu}$ is still *tensorially* valid (both sides transform as $(0, 2)$ tensors), but the *interpretation* changes — the physical "flat retina" is now described in warped coordinates.

**Verdict on Test B**: PFE IS spatial-diffeomorphism covariant in the *tensorial* sense. But the *interpretation* (flat retina, isotropic, etc.) is preserved only under isometries.

**Test C: Combined Lorentz boost analog**

In GR, the strong equivalence principle implies *local* Lorentz invariance: physics looks the same in any locally-inertial frame. Does PFE have this?

PFE's $c_p^{(s)}$ is *per-stage*, not per-observer. There is no analog of Lorentz boost — observers in $\mathcal{O}$ all share the same $c_p^{(s)}$ (P2). A "boosted observer" would have a *different* $c_p$ in the boosted frame, but P2 says no.

**Resolution**: PFE has *no Lorentz-boost analog*. It is *not* relativistically invariant in the physical sense. It is a *geometric structure with a preferred rest frame* (the retina + observer fixed).

**Verdict on Test C**: PFE has NO Lorentz-boost invariance. The geometry is *fixed* relative to the observer; not invariant under boosts.

### Aggregate verdict

**WEAKEN**. Confidence: high.

PFE is:
- Spatial-diffeomorphism *tensorially* covariant (Test B passes)
- NOT time-reparametrization invariant (Test A fails — restricts $\mathcal{O}$)
- NOT Lorentz-boost invariant (Test C fails — has preferred rest frame)

The "Einstein form" of the equation is *tensorially well-formed* but PFE is *less symmetric than GR*. It is more like *Newton-Cartan theory* (Newtonian gravity in covariant form) than *Lorentz-invariant relativity*.

### Downstream consequence
- PFE should be honestly framed as *Newton-Cartan-like* geometric structure for perception, not as *fully relativistic*
- The "Lorentz cone" of PFE is *not* an absolute cone like Minkowski's — it's a *per-observer* cone with preferred rest frame
- This is *appropriate* for biological perception (the observer is fixed in their body; no boost transformations)
- But it weakens the elegant "Einstein-form" interpretation: PFE is not deeply analogous to GR; it's a *coordinate-dependent geometric structure*

### Repair candidate
Reformulate PFE as a *Newton-Cartan*-like theory with explicit *absolute time* (the observer's clock). The equations remain in tensor form but the *causal structure* is the absolute observer's cone, not a Lorentz-invariant cone.

This is *less aesthetically pleasing* but *more honest*.

### New OP registered
**OP-PFE-13**: Reformulate PFE in Newton-Cartan-like absolute-time framework. Verify that all 4 operational tests (Tests 1-4) and predictions still hold under this reformulation.

### Status after Task 21
PFE survives gauge-invariance attack but is *demoted* from "fully relativistic Einstein-form" to "Newton-Cartan-like geometric structure". The cosmetic Einstein form is preserved; the deep physical analogy is weaker.

---

## Task 22 — Pattern #62: Initial conditions / Cauchy problem

### Attack
Einstein's equations in GR have well-posed Cauchy problem (ADM formalism, 3+1 split, Choquet-Bruhat theorem). Given initial data on a *spacelike slice* (induced 3-metric + extrinsic curvature), the equations determine $g_{\mu\nu}$ in the future (up to gauge).

Does PFE have an analogous well-posed Cauchy problem? If not, PFE cannot *predict* — it can only *describe* steady states.

### Specific test

**Cauchy slice in PFE**

In 1+2D, a spacelike slice is a 1D curve in the retinal $(x, y)$ plane at fixed perception-time $t$. Initial data: induced spatial metric (Euclidean) + extrinsic curvature.

Initial data analog in PFE: 
- *Spatial cohesion configuration*: $u(x, y, t = t_0)$
- *Initial time derivative*: $\partial_t u (x, y, t = t_0)$
- *Initial metric*: $g_{\mu\nu}^{(s)}|_{t = t_0}$ — derived from initial $u$ via field equation (constraint)

The field equation $G_{\mu\nu} = \kappa T_{\mu\nu}$ is a *second-order PDE* in time for $g_{\mu\nu}$, sourced by $T_{\mu\nu}[u]$. SCC's dynamics for $u$ is *first-order* (gradient descent on energy, see `CODE/scc/optimizer.py`).

**Combined system**:
- $\partial_t u = -\nabla_u E[u]$ (SCC dynamics, first-order)
- $G_{\mu\nu}^{(s)} = \kappa T_{\mu\nu}^{\text{perception}}[u, g]$ (PFE, second-order in $g$)

The coupled system: given $u(t_0), \partial_t u(t_0)$ — but SCC only needs $u(t_0)$ — and $g(t_0), \partial_t g(t_0)$ at constraint slice — determines evolution forward.

**Question**: is this system *well-posed*? (Existence + uniqueness + continuous dependence on initial data.)

### Analysis

**Existence**: The system is *quasi-linear hyperbolic* (PFE wave equation) coupled to *parabolic* (SCC gradient flow). Mixed parabolic-hyperbolic systems can be well-posed but require careful treatment.

**Uniqueness**: SCC gradient flow is unique given $u(t_0)$ if $E[u]$ is sufficiently smooth (Lojasiewicz convergence applies — already in SCC canonical Cat A). PFE wave equation is unique given Cauchy data + gauge fixing.

**Continuous dependence**: Both parabolic (SCC) and hyperbolic (PFE) have continuous dependence under suitable function-space norms.

**Constraint preservation**: In GR, the Hamiltonian and momentum constraints must be preserved under evolution. In PFE, the analog is: $G_{0\nu} - \kappa T_{0\nu} = 0$ at $t_0$ must remain zero for all $t > t_0$. This requires the *Bianchi identity* $\nabla^\mu G_{\mu\nu} = 0$ to imply $\nabla^\mu T_{\mu\nu} = 0$ (energy-momentum conservation, see Task 23).

If $T_{\mu\nu}^{\text{perception}}[u, g]$ does *not* satisfy $\nabla^\mu T_{\mu\nu} = 0$ on the SCC dynamics, then the constraint is *not preserved*, and the system is *inconsistent*.

### Verification of $\nabla^\mu T_{\mu\nu} = 0$ for SCC variational tensor

The stress-energy was defined as $T_{\mu\nu} = (2/\sqrt{-g}) \delta(\sqrt{-g} E[u]) / \delta g^{\mu\nu}$. If $E[u]$ depends on $g$ *only through the volume form $\sqrt{-g}$* and *kinetic gradients $\partial_\mu u$*, then $\nabla^\mu T_{\mu\nu} = 0$ *automatically* whenever $u$ satisfies its own Euler-Lagrange equation.

But SCC dynamics is *gradient descent*, not Euler-Lagrange of an action functional. Gradient descent: $\partial_t u = -\nabla_u E[u]$. Euler-Lagrange (if existed): $\delta E / \delta u = 0$, which means $u$ is at a critical point — *not* a dynamical equation.

**Crucial mismatch**: SCC's gradient descent is *dissipative* (energy decreases monotonically). The stress-energy tensor from variational derivative *assumes* Euler-Lagrange dynamics (conservative).

**Consequence**: $\nabla^\mu T_{\mu\nu} \neq 0$ for SCC gradient flow, *unless* we extend the energy with a "dissipation" term (analogous to a friction term in mechanics).

### Verdict

**FAIL or WEAKEN** (depending on framing). Confidence: high.

The Cauchy problem for PFE-SCC coupled system is **inconsistent without modification**:
- PFE requires $\nabla^\mu T_{\mu\nu} = 0$ for constraint preservation
- SCC's $T_{\mu\nu}$ from $E[u]$ variational derivative satisfies $\nabla^\mu T_{\mu\nu} = 0$ only if $u$ obeys Euler-Lagrange (conservative dynamics)
- SCC's actual dynamics is *gradient flow* (dissipative)
- These are *incompatible*

### Repair candidates

**Repair A: Replace SCC gradient flow with conservative dynamics**
- Replace $\partial_t u = -\nabla_u E[u]$ with $\partial_t^2 u = -\nabla_u E[u]$ (Hamiltonian dynamics)
- *Violates*: SCC canonical (gradient flow is part of canonical dynamics)
- **REJECTED** (canonical preservation discipline)

**Repair B: Add dissipative stress-energy**
- $T_{\mu\nu}^{\text{total}} := T_{\mu\nu}^{\text{variational}} + T_{\mu\nu}^{\text{dissipation}}$ where dissipation term *absorbs* the divergence
- *Concern*: adding dissipation is *ad hoc*; needs principled construction
- **TENTATIVE** — requires careful formulation

**Repair C: Reinterpret PFE as effective theory**
- Accept that PFE is *not* a fundamental dynamical theory; it's an *effective description* on time-scales where SCC has equilibrated
- "Quasi-static" PFE: at each instant, $u$ is at SCC equilibrium for the current metric; metric evolves slowly
- Cauchy problem reduces to: given $g(t_0)$ (with $u$ at equilibrium), evolve $g(t)$
- Equilibrium $u$ satisfies $\nabla_u E[u] = 0$, i.e., Euler-Lagrange — conservation holds
- **RECOMMENDED**

### Status after Task 22

PFE Cauchy problem is *well-posed only in quasi-static regime* (Repair C). Full dynamical PFE-SCC coupling is inconsistent without explicit dissipation modeling.

This is a **significant restriction**: PFE applies to *equilibrium* perception configurations, not *transient* ones. Tests 1-4 measurements should be conducted in equilibrium regimes (long stimulus exposures, after adaptation transients).

### New OP registered
**OP-PFE-14**: Develop dissipative extension of PFE consistent with SCC gradient flow (Repair B). Requires principled construction of dissipation tensor.

### Downstream consequence
- PFE's "predictive" capability is restricted to *equilibrium perception*
- Saccades, attentional shifts, rapid stimulus changes — all outside PFE's strict validity
- This narrows the empirical scope substantially
- Tests 1-4 protocols (Phase C) should specify *equilibrium* conditions (steady gaze, long exposure, post-adaptation)

---

## Task 23 — Pattern #63: Conservation laws / Noether currents

### Attack
GR has rigid structure from Noether's theorem: every continuous symmetry of the action gives a conserved current. PFE's symmetries (after Task 21 weakening) are limited but should still give *some* conservation laws.

Does PFE have non-trivial conserved quantities? If not, the framework lacks the *structural rigidity* that makes GR predictive (energy-momentum conservation, angular momentum conservation).

### Symmetries of PFE

Per Task 21:
- *Spatial translation* (within retinal frame): YES, $\mathcal{O}$ includes translated observers? Actually no — P1's $\mathcal{O}$ is observer-specific. Spatial *translation of stimulus pattern* keeps the same observer; this is a different symmetry.
- *Spatial rotation* (within retinal frame): YES if retina is isotropic (assumption I2 from Task 3); not exactly true (foveal-peripheral asymmetry)
- *Time translation*: YES if conditions are stationary (no adaptation drift)
- *Lorentz boost*: NO (Task 21)

### Noether currents

**Time translation → perception energy conservation**
- If conditions are stationary, total perception energy $E[u]$ is conserved over time
- In gradient flow: $E[u]$ *decreases* monotonically (not conserved). 
- Contradicts time-translation symmetry naively expected
- Resolution: stationary conditions + gradient flow is *not* a time-symmetric dynamics
- **Perception energy is NOT conserved** in SCC gradient flow

**Spatial translation → perception momentum conservation**
- If retinal background is uniform (no spatial inhomogeneity in $c_p^{(s)}$), then spatial translation is a symmetry
- Noether current: $\int T_{0i}^{\text{perception}} dx dy$ should be conserved
- In gradient flow: $T_{0i}$ depends on $\partial_i u$, and the spatial integral over $\partial_i u$ for a localized $u$ is *boundary-term-only* — conserved up to boundary fluxes
- **Perception momentum is approximately conserved** in localized configurations

**Spatial rotation → perception angular momentum conservation**
- Similar to spatial translation; conserved up to boundary fluxes
- **Perception angular momentum approximately conserved**

### Verdict

**PASS with WEAKEN**. Confidence: medium-high.

PFE has *spatial conservation laws* (momentum, angular momentum) approximately, but *not energy conservation* (because SCC dynamics is dissipative — same issue as Task 22).

### Downstream consequence
- PFE has *some* structural rigidity from spatial symmetries
- But the *most powerful* conservation law (energy) is broken by dissipative SCC dynamics
- This *reinforces* Task 22's finding: PFE is best understood as *equilibrium-effective* theory, where energy *minimization* (not conservation) is the dynamical principle

### Testable predictions from spatial conservation

**Prediction (Task 23 contribution)**:
- For a *localized* cohesion configuration evolving under SCC + PFE, the *centroid* of the configuration moves at *constant velocity* in absence of external perturbation
- This is the analog of momentum conservation
- **Empirical test**: presented with isolated visual object, perceived object centroid should drift at constant rate (or stay put) when retinal motion is null; should accelerate only in presence of external "force" (e.g., gradient in $c_p^{(s)}$)

This is *consistent* with motion perception: stationary objects appear stationary; moving objects appear to move at constant velocity in absence of acceleration.

### Status after Task 23

PFE has *spatial conservation laws* (momentum-like, angular-momentum-like) approximately. *Energy* is not conserved (dissipative SCC dynamics). The spatial conservation provides:
- Justification for "free perception trajectory = straight line in flat metric" (Task 10)
- Prediction: perceptual centroids should drift at constant velocity in absence of perturbation (testable)

### New OP registered
**OP-PFE-15**: Verify perceptual-centroid constant-velocity drift prediction. Psychophysics test: track perceived position of localized stimulus over time; check whether drift is constant in absence of external perturbation.

---

## Phase E Summary

| Task | Pattern | Verdict | Confidence | Effect on framework |
|------|---------|---------|------------|---------------------|
| 21 | #61 gauge invariance | WEAKEN | High | PFE is Newton-Cartan-like, not Lorentz-invariant; demoted from "Einstein-form" |
| 22 | #62 Cauchy problem | WEAKEN (effective theory only) | High | PFE-SCC coupling inconsistent dynamically; only quasi-static equilibrium PFE is well-posed |
| 23 | #63 conservation laws | PASS with WEAKEN | Medium-high | Spatial conservation laws (momentum-like) hold; energy not conserved (dissipative) |

### Aggregate Phase E verdict

**WEAKEN substantially**. PFE survives all three patterns but is *substantially demoted*:

1. **Not relativistically invariant** (Task 21): Newton-Cartan-like, observer-fixed cone; not deeply analogous to GR
2. **Only quasi-static well-posed** (Task 22): cannot describe transient perception dynamics; SCC dissipation breaks dynamical coupling
3. **Limited conservation** (Task 23): spatial momentum-like conservation works; energy does not

### Most damaging finding (Phase E)
**Task 22's Cauchy problem failure**. PFE-SCC coupling is *dynamically inconsistent* unless PFE is restricted to *equilibrium-effective* regime. This is a *substantial narrowing* of the framework's scope — Phase A's σ-fuzzy-edge and Phase B's vacuum-defects-only are *less consequential* than this.

### Updated framework register (post-Phase E)

| Component | Pre-Phase-E | Post-Phase-E |
|-----------|-------------|--------------|
| Geometric framing | Einstein-form GR-analog | Newton-Cartan-like; observer-fixed |
| Dynamical scope | "field equation with operational tests" | Equilibrium-effective; quasi-static regime only |
| Predictive Cauchy | implicit | RESTRICTED to equilibrium |
| Conservation laws | implicit | Spatial yes, energy no |
| Testing regime | Tests 1-4 generic | Tests 1-4 must specify equilibrium conditions |

### New OPs registered in Phase E
- **OP-PFE-13**: Newton-Cartan-like reformulation with absolute time
- **OP-PFE-14**: Dissipative extension of PFE consistent with SCC gradient flow
- **OP-PFE-15**: Perceptual-centroid constant-velocity drift prediction

### Combined OPs after Phases A-E: 15 OPs in framework
Original 5 (Iter 19): OP-PFE-1..5
Phase A: OP-PFE-6, 7
Phase B: OP-PFE-8, 9, 10
Phase C: OP-PFE-11
Phase D: OP-PFE-12
Phase E: OP-PFE-13, 14, 15

### What was NOT done in Phase E
- No rigorous proof of constraint inconsistency (Task 22 is sketch; needs full Hamiltonian analysis)
- No Newton-Cartan-like reformulation (Task 21 identifies need, doesn't construct)
- No dissipative tensor construction (Task 22 Repair B not pursued)
- No empirical drift test (Task 23 prediction untested)
- Patterns #61, #62, #63 are *new* additions to the 15-pattern gauntlet; not previously catalogued elsewhere

---

*Phase E v0. 3 tasks, 3 patterns, all attack verdicts WEAKEN or PASS-with-WEAKEN. Most significant: Task 22 restricts PFE to quasi-static equilibrium. canonical/SCC/PAI/8-retractions 0 modifications. Next: Phase F Connections & Synthesis (Tasks 24-26).*
