---
type: working/sensing_pipeline/pass12_field_equation_verification
version: v0
date: 2026-05-25
status: ACTIVE — Pass 12 Phase B (Tasks 6-10)
purpose: |
  Adversarial verification of Pass 11's Einstein-form perception field equation (PFE):
  R_μν - (1/2) g_μν R = κ T_μν^perception[u,g].
  Five tasks: dimensional analysis, κ-dimension candidates, vacuum-solution existence (1+2D),
  linearized form vs known retinal linear models, geodesic equation interpretation.
register: VERIFICATION
parent: 00_INDEX
prev: 13_p1_p2_verification
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
  pai_canonical_edits: 0
  modifies_12_perception_cone: 0
  verdict_method: per-task explicit verdict against pre-stated falsification criterion
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[13_p1_p2_verification]] · Pass 12 Phase B

# Pass 12 Phase B — Field Equation Verification (Tasks 6-10)

**Scope**: audit the *structural form* of Pass 11's PFE candidate. Phase A weakened the postulate side; this phase asks whether the equation *itself* is mathematically/physically coherent before any empirical test.

**Method**: each task states (i) what is verified, (ii) falsification criterion, (iii) calculation/argument, (iv) verdict with confidence, (v) downstream consequence.

**Context inherited from Phase A**:
- σ is constructed (not derived) from P1+P2+I1-I4 — the metric $g_{\mu\nu}^{(s)}$ inherits this conditional status
- Stage table values are convention-dependent (Task 2)
- $c_p^{(s)}$ should be treated as *order of magnitude* until OP-PFE-6 resolves convention

---

## Task 6 — Field equation dimensional analysis

### What is verified
The Einstein-form candidate:
$$R_{\mu\nu}^{(s)} - \tfrac{1}{2} g_{\mu\nu}^{(s)} R^{(s)} = \kappa^{(s)} T_{\mu\nu}^{\text{perception}}[u, g^{(s)}]$$

is *dimensionally consistent* only if LHS and RHS have the same units. This task computes those units.

### Falsification criterion
If LHS units cannot be matched by RHS units for *any* choice of $\kappa^{(s)}$ dimensions, the equation form is wrong. If units are matchable, the *required* dimensions of $\kappa^{(s)}$ are extracted (input to Task 7).

### LHS dimensional analysis

Choose base units in the *perception* setting:
- $[t]$ = T (time, e.g., seconds)
- $[x] = [y]$ = L (spatial, e.g., meters on the retina)
- $[c_p^{(s)}]$ = L/T (rate)

Metric: $g_{\mu\nu}^{(s)} = \text{diag}(-c_p^{(s) 2}, 1, 1)$ with coordinate $t$ in $\mu = 0$, $x,y$ in $\mu = 1, 2$.

Then:
- $[g_{00}] = L^2/T^2$
- $[g_{11}] = [g_{22}] = $ dimensionless

This is *non-standard* — different components have different units. The standard trick: use $\tilde{t} := c_p t$ as time coordinate; then $[\tilde{t}] = L$ and all metric components are dimensionless.

**Using $\tilde{t}$ coordinate**:
- All $g_{\mu\nu}$ dimensionless
- $[\partial_\mu] = L^{-1}$
- Christoffel $[\Gamma^\alpha_{\mu\nu}] = L^{-1}$
- Riemann $[R^\alpha_{\beta\mu\nu}] = L^{-2}$
- Ricci $[R_{\mu\nu}] = L^{-2}$
- Scalar $[R] = L^{-2}$
- Einstein tensor $[G_{\mu\nu}] = [R_{\mu\nu} - \tfrac{1}{2} g R] = L^{-2}$ (dimensionless $g$ times $L^{-2}$ scalar)

**LHS units**: $L^{-2}$ (i.e., inverse area).

### RHS dimensional analysis

SCC energy functional $E[u]$ — units depend on convention. From `CODE/scc/energy.py`:
- $E_{cl}[u] = \sum_{ij} W_{ij} u_i (1-u_j)^2$ — for a discrete graph; units: dimensionless (cohesion field $u$ is dimensionless, weights $W_{ij}$ are dimensionless)
- $E_{sep}, E_{bd}, E_{tr}$ similarly dimensionless per the discrete graph code

Continuum analog (which PFE assumes):
- $E[u] = \int e[u, \nabla u] \, d^2x \, dt$ where $e[u, \nabla u]$ is an *energy density*
- For $E[u]$ to be a *number* (dimensionless action), $[e] = L^{-2} T^{-1}$
- Using $\tilde{t}$ coordinate: integration measure $d^2 x \, d\tilde{t}$ has units $L^3$, so $[e] = L^{-3}$

The stress-energy tensor (per its variational definition):
$$T_{\mu\nu}^{\text{perception}} = \frac{2}{\sqrt{-g}} \frac{\delta (\sqrt{-g} \, E[u])}{\delta g^{\mu\nu}}$$

$[T_{\mu\nu}] = $ same as $[e]$ = energy density = $L^{-3}$ (under $\tilde{t}$ coordinate).

### Required $\kappa^{(s)}$ dimensions

$[\kappa^{(s)} T_{\mu\nu}] = L^{-2}$ (matching LHS)
$[T_{\mu\nu}] = L^{-3}$

Therefore $[\kappa^{(s)}] = L^{-2} / L^{-3} = L$.

### Comparison to general relativity

In GR: $G_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu}$
- $[G_{\mu\nu}^{GR}] = L^{-2}$
- $[T_{\mu\nu}^{GR}] = M L^{-1} T^{-2}$ (energy density)
- $[\kappa^{GR}] = [8\pi G / c^4] = L^{-2} / (M L^{-1} T^{-2}) = M^{-1} L^{-1} T^2$

In PFE (perception): no mass dimension; only space-time-and-rate. $[\kappa^{PFE}] = L$.

### Verdict

**PASS**. Confidence: high.

LHS and RHS are *dimensionally matchable* with $[\kappa^{(s)}] = L$ (i.e., a length scale). The conversion to $\tilde{t} := c_p^{(s)} t$ is required for the calculation to be clean.

### Downstream consequence
- $\kappa^{(s)}$ must have units of length
- Natural candidates: a *characteristic length scale* for stage $s$ (receptive field radius? cone column spacing? mean free path of a perceptual signal?)
- Task 7 will explore biological candidates with the correct $L$ dimension

### What was NOT verified
- Whether $\kappa^{(s)}$ is a *positive* constant (sign convention: in GR, $\kappa > 0$ ensures attractive gravity; in PFE, sign determines whether cohesion creates "positive" or "negative" curvature)
- Whether the action $\int E[u] \sqrt{-g} d^3x$ has a *minimum* (need Lorentzian-action coercivity, problematic in Lorentzian signature)

### Register
MATH-FACT (purely calculational, no empirical content beyond unit convention).

---

## Task 7 — Coupling constant $\kappa^{(s)}$ candidate dimensions

### What is verified
Given Task 6's requirement $[\kappa^{(s)}] = L$, what *biologically/physically motivated* length scale could $\kappa^{(s)}$ be?

### Falsification criterion
If no biologically plausible candidate gives the correct units *and* a sensible magnitude, $\kappa^{(s)}$ is *unmotivated* — the field equation form would survive only as a *purely mathematical* structure, not as a substantive empirical prediction.

### Candidate length scales (per stage)

**Per-stage list** for retinal stage $s$:
1. $\ell_s$ = characteristic spatial correlation length used to define $c_p^{(s)}$ in Task 2
2. $\bar{\ell}_s$ = mean inter-cell distance for the dominant cell type
3. $\lambda_s$ = "perceptual wavelength" (length × time × ... composite — but needs to reduce to L)
4. $\sqrt{A_s / N_s}$ where $A_s$ = retinal area at stage, $N_s$ = number of independent units
5. $\hbar^*$-like quantum-scale analog (rejected — no biological quantization at this scale)

### Evaluation

**Candidate 1: $\kappa^{(s)} \propto \ell_s$**
- Units: $L$ — PASS
- Magnitude: μm-mm range; varies 3 orders of magnitude across stages
- *Interpretation*: cohesion field of strength $T_{\mu\nu}$ creates curvature on scale $\ell_s \cdot T_{\mu\nu}$
- *Sensibility*: larger receptive fields ⟹ more curvature per unit cohesion ⟹ broader binding kernels in fovea (small $\ell$) vs periphery (large $\ell$). Matches qualitative psychophysics: foveal binding is *sharper*, periphery is *more diffuse*.
- **Plausible**

**Candidate 2: $\kappa^{(s)} \propto \bar{\ell}_s$**
- Same units, similar magnitude
- Differs from Candidate 1 only by a constant factor in stages where $\ell_s$ ≠ $\bar{\ell}_s$ (e.g., $\ell_s$ is RF radius, $\bar{\ell}_s$ is cell spacing — typically related by factor 2-5)
- **Plausible but indistinguishable from Candidate 1 without high-precision data**

**Candidate 3: composite "perceptual wavelength"**
- Try: $\lambda_s := c_p^{(s)} \cdot \tau_s = \ell_s$ (by construction of $c_p$)
- Reduces to Candidate 1; not independent
- **Not independent**

**Candidate 4: $\sqrt{A_s / N_s}$**
- Units: $\sqrt{L^2 / 1} = L$ — PASS
- Magnitude: for a stage with $N$ cells covering area $A$, this is the *Voronoi cell length* ≈ $\bar{\ell}_s$ to within $\sqrt{\pi}$
- **Reduces to Candidate 2; not independent**

**Candidate from photon-Fisher analogy** (if we want a *physical* derivation):
- In information geometry, the Fisher metric has natural length scale $\sigma_{\text{noise}} / \sqrt{N}$ for $N$ independent measurements with noise $\sigma$
- Per stage: $\kappa^{(s)} \sim \sigma_{\text{photon}}^{(s)} / \sqrt{N_{\text{events}}^{(s)}}$
- This has units $L$ if $\sigma_{\text{photon}}$ is interpreted as a *positional uncertainty per detected photon* on the retina (∼ photoreceptor diameter for Stage 1)
- Magnitude: ~1-10 μm at Stage 1, scaling up at later stages where $N_{\text{events}}$ may be smaller
- **Plausible, gives a different prediction from Candidate 1 for later stages**

**Candidate from neural conductance** (rejected):
- Neural conductance has units $T \cdot M^{-1} \cdot L^{-2}$ (Siemens per area), incompatible with $L$ requirement after any natural scaling
- **REJECTED**

### Convergent estimate

**Estimated $\kappa^{(s)}$ range**:

| Stage | $\ell_s$ (Task 2 corrected) | $\kappa^{(s)}$ candidate range |
|-------|------------------------------|---------------------------------|
| Cone photoreceptor | 2.2 μm | 1-10 μm |
| Bipolar/amacrine | 50-200 μm | 50-500 μm |
| M ganglion | 100-300 μm | 100-500 μm |
| P ganglion | 30-100 μm | 30-200 μm |
| V1 column | 500-1000 μm | 0.5-2 mm |
| Attentional | 1-10 cm | 1-10 cm |

These match the corrected Task 2 values. The interpretation: *cohesion field of magnitude 1 creates curvature on scale $\kappa^{(s)}$*.

### Verdict

**PASS with WEAKEN caveat**. Confidence: medium.

There are *biologically plausible* length-scale candidates with correct units. The strongest candidate is $\kappa^{(s)} = c \cdot \ell_s$ for some dimensionless constant $c$ of order unity. However:
- The *dimensionless prefactor* $c$ is unknown and could only be measured empirically
- Multiple candidates (RF radius, cell spacing, Voronoi length) are *indistinguishable* without high-precision data
- The Fisher-information candidate gives a *different* per-stage scaling that *could* be empirically distinguished — but the experiment hasn't been done

### Downstream consequence
- $\kappa^{(s)}$ is *operationally undetermined* without empirical fit (OP-PFE-2 confirmed)
- The PFE has *one free parameter per stage* (the dimensionless prefactor); this is the *minimum* parameter cost of any local-coupling theory
- For OP-PFE-2 (Task 17 of this pass), the *measurement procedure* must:
  - Fix the dimensionless prefactor by fitting one observed curvature value
  - Cross-validate by predicting another curvature value at a different position
- If cross-validation fails (predicted ≠ measured by >2×), the candidate $\kappa^{(s)} = c \ell_s$ form is wrong

### What was NOT verified
- Whether $\kappa^{(s)}$ is constant or varies with cohesion field magnitude (could be $\kappa[u]$ in a non-minimal coupling)
- Whether sign of $\kappa$ is fixed across stages (likely yes, but unverified)

### Register
MODELING-MOTIVATION (no biological evidence yet — candidates are *consistent* with units but not *forced* by data).

---

## Task 8 — Vacuum solution existence (1+2D Lorentzian)

### What is verified
Iter 10 lists "vacuum: free perception evolution" as an approximation regime. This task asks: in 1+2D Lorentzian signature with $T_{\mu\nu} = 0$, does the equation $R_{\mu\nu} = 0$ have *non-trivial* solutions?

**Critical background**: in *3+1D* GR, vacuum solutions are rich (Schwarzschild, Kerr, gravitational waves). In *2+1D* GR, the situation is dramatically different — vacuum Einstein equations admit only *locally flat* solutions (with global topological choices).

### Falsification criterion
If the only vacuum solutions are flat (Minkowski) in 1+2D, then the PFE has *no autonomous perception dynamics* — the field equation predicts perception evolves *trivially* in the absence of cohesion. This would *weaken* the field-equation interpretation: PFE is then a *coupling rule* only, with no independent geometric content.

### 1+2D vacuum Einstein equation analysis

In $n$ spacetime dimensions, the Riemann tensor has $\frac{n^2(n^2-1)}{12}$ independent components and the Ricci tensor has $\frac{n(n+1)}{2}$. For $n = 3$ (1+2D):
- Riemann: 6 independent components
- Ricci: 6 independent components
- $R^\alpha_{\beta\mu\nu}$ can be *fully reconstructed* from $R_{\mu\nu}$ (and the metric)

Explicit identity (Weyl tensor vanishes identically in 3D):
$$R_{\alpha\beta\mu\nu} = g_{\alpha\mu} R_{\beta\nu} - g_{\alpha\nu} R_{\beta\mu} - g_{\beta\mu} R_{\alpha\nu} + g_{\beta\nu} R_{\alpha\mu} - \tfrac{R}{2}(g_{\alpha\mu} g_{\beta\nu} - g_{\alpha\nu} g_{\beta\mu})$$

**Consequence**: $R_{\mu\nu} = 0$ ⟹ $R_{\alpha\beta\mu\nu} = 0$ ⟹ *locally flat*.

So vacuum solutions in 1+2D are *locally Minkowski*. **Globally**, however, non-trivial topology can produce *conical singularities* (Deser-Jackiw-'t Hooft 1984: point particles in 2+1 gravity are conical defects).

### Implication for PFE

PFE in vacuum ($T_{\mu\nu}^{\text{perception}} = 0$, i.e., $u \equiv $ constant or zero) admits only:
- **Local flat solutions**: cone is rigidly Minkowskian with rate $c_p^{(s)}$
- **Global topological solutions**: e.g., periodic identifications (retinal annulus topology, cylinder topology)
- **Conical singularities**: point-like "perceptual defects" — could correspond to *attentional foci* or *blind spots*?

### Honest assessment

**Pro**: vacuum is *not* completely trivial — topology and conical defects exist. The "perception field has no autonomous dynamics" claim is *partially* true (no propagating gravitational waves) but *not entirely* trivial (defects exist).

**Con**: the *richness* of GR vacuum is absent. In 1+2D PFE:
- No "perception waves" propagating in absence of stimulus (cohesion field)
- No "perceptual black holes" with horizons (well, conical defects but those are degenerate)
- Schwarzschild-like solution from Iter 10 actually *doesn't exist* in 1+2D vacuum

This contradicts Iter 10's listing of "Schwarzschild-like" as a 1+2D PFE regime.

### Verdict

**WEAKEN** (with surprise finding). Confidence: high.

The Iter 10 mention of *Schwarzschild-like* is **wrong** for 1+2D — Schwarzschild only exists in $\geq$ 3+1D vacuum. The actual 1+2D vacuum is:
- Locally flat (Minkowski rate $c_p^{(s)}$)
- Globally constrained by topology
- Defect solutions = conical singularities (analog of point masses in 2+1 gravity)

### Downstream consequence

**Three implications**:

1. **Iter 10 "Schwarzschild-like" regime must be retracted** (or restricted to 3+1D extension of PFE, which would require adding a *retinal-depth* dimension)

2. **PFE vacuum content is *only* topological + defects** — this is *non-trivial* but *narrow*. Potential interpretation: a *point cohesion source* (single object on retina) creates a *conical defect* around it; the retinal space is locally flat away from the source but globally non-Euclidean. Visual angle around the source ≠ 2π. **This is testable** — perceived angular geometry near a salient point object.

3. **Genuine field dynamics require $T_{\mu\nu} \neq 0$** — the framework lives *almost entirely* in the matter-coupled regime. "Free perception evolution" is *trivial* (just flat Minkowski advection at rate $c_p$).

### New OP registered
**OP-PFE-8**: Compute the conical-defect angle as a function of point-source cohesion magnitude. Compare to perceived-angle psychophysics around a salient point stimulus.

### Vacuum solution catalog

| Solution | Exists in 1+2D vacuum? | Description |
|----------|-------------------------|-------------|
| Minkowski (flat) | YES | Uniform $c_p^{(s)}$, no cohesion |
| Conical defect | YES (point cohesion source as boundary) | Angular deficit $2\pi(1-\sqrt{1-\kappa M / 2\pi})$ |
| BTZ black hole | YES (with negative $\Lambda$) | Requires negative cosmological constant — adds *one parameter* |
| Schwarzschild (3+1D) | NO | Iter 10 claim is wrong for 1+2D |
| Kerr | NO | Same — only ≥ 3+1D |
| Gravitational waves | NO | No propagating modes in 1+2D vacuum |

### What was NOT verified
- BTZ-like solutions (would require introducing a *perception cosmological constant* $\Lambda$, which is a new parameter — not currently in PFE)
- 3+1D extensions of PFE (would need a retinal-depth dimension)
- Whether conical defects are *physically realized* in perceptual experience

### Register
MATH-FACT (vacuum analysis), with retraction note attached to Iter 10's Schwarzschild claim.

---

## Task 9 — Linearized field equation explicit form

### What is verified
Iter 10 lists "weak field (Newtonian)" and "linearized" as regimes. This task computes the *actual* linear equation and compares it to known retinal linear models (DoG, Wiener filter, motion energy).

### Falsification criterion
If the linear PFE *cannot* reduce to (or approximate) known retinal linear models like DoG and motion energy, then PFE *contradicts established biology* — at minimum, the *weak-field regime* of PFE must agree with well-validated retinal linear theory.

### Setup

Write $g_{\mu\nu}^{(s)} = \eta_{\mu\nu}^{(s)} + h_{\mu\nu}^{(s)}$ where $\eta = \text{diag}(-c_p^{(s) 2}, 1, 1)$ (background, using $t$ coordinate) and $|h_{\mu\nu}^{(s)}| \ll |\eta_{\mu\nu}^{(s)}|$.

To first order in $h$:
- $\Gamma^\alpha_{\mu\nu} \approx \tfrac{1}{2} \eta^{\alpha\beta} (\partial_\mu h_{\nu\beta} + \partial_\nu h_{\mu\beta} - \partial_\beta h_{\mu\nu})$
- $R_{\mu\nu} \approx \tfrac{1}{2}(\partial^\alpha \partial_\mu h_{\nu\alpha} + \partial^\alpha \partial_\nu h_{\mu\alpha} - \Box h_{\mu\nu} - \partial_\mu \partial_\nu h)$

where $h := \eta^{\mu\nu} h_{\mu\nu}$ (trace) and $\Box := \eta^{\alpha\beta} \partial_\alpha \partial_\beta$.

In *transverse traceless* gauge ($\partial_\mu h^{\mu\nu} = 0$, $h = 0$):
$$\Box h_{\mu\nu} = -2 \kappa^{(s)} T_{\mu\nu}^{\text{perception}}$$

### Explicit wave operator

In the perception cone coordinates $(t, x, y)$ with $\eta = \text{diag}(-c_p^{(s)2}, 1, 1)$:
$$\Box = -\frac{1}{c_p^{(s) 2}} \partial_t^2 + \partial_x^2 + \partial_y^2$$

So:
$$\left( -\frac{1}{c_p^{(s) 2}} \partial_t^2 + \nabla^2 \right) h_{\mu\nu} = -2 \kappa^{(s)} T_{\mu\nu}^{\text{perception}}$$

This is a **wave equation** with propagation speed $c_p^{(s)}$, sourced by the stress-energy.

### Comparison to known retinal linear models

**DoG (Difference of Gaussians)** — classical Stage 2 model:
- Linear filter: $f_{DoG}(x) = G_{\sigma_c}(x) - G_{\sigma_s}(x)$ where $G_\sigma$ is 2D Gaussian
- This is a *spatial* filter, no explicit time dependence in static form
- Dynamical DoG with separable time: $f(x, t) = f_{DoG}(x) \cdot g(t)$ where $g(t)$ is biphasic temporal kernel
- Underlying equation: linear convolution; equivalent to a *steady-state Poisson-like equation* $(\nabla^2 - 1/\sigma^2) f = -\delta(x)$ in suitable parametrization

**Wiener filter for optimal linear estimation**:
- $f_{Wiener}$ in Fourier: $\hat{f}(\omega, k) = \hat{S}(\omega, k) / (\hat{S} + \hat{N})$ where $S$ is signal spectrum, $N$ noise
- Time domain: convolution equation linear in input

**Adelson-Bergen motion energy** — Stage 2/3 model:
- Linear *spatiotemporal* filter: separable form $f(x, t)$ with oriented receptive fields
- Equivalent equation: wave-like response along motion direction, $(\partial_t + v \partial_x) f = $ input

### Reduction of linear PFE to retinal models

Set $T_{\mu\nu}^{\text{perception}}$ to specific forms:
- **Static localized cohesion**: $T_{00} = \rho(x) \delta(t)$, other components zero
  - Wave equation reduces to *Poisson-like*: $\nabla^2 h_{00} \approx 2 \kappa \rho$ (after averaging over time)
  - Solution: $h_{00} \sim \int G(x - x') \rho(x') dx'$ where $G$ is the 2D Green's function $\sim \log|x-x'|/(2\pi)$
  - This is *NOT* DoG — it's a *single-Gaussian-like* kernel (or in 2D, logarithmic). DoG requires *two* scales.

- **Two cohesion fields with center-surround structure**: $T_{00} = \rho_c(x) - \rho_s(x)$ with $\rho_c$ tight, $\rho_s$ broad
  - Linear PFE gives $h_{00} = G * \rho_c - G * \rho_s$ — center-surround response
  - This *does* recover a DoG-like response *given* a center-surround source

- **Traveling cohesion wave**: $T_{\mu\nu}(x - v t)$
  - Linear PFE supports wave propagation at $c_p^{(s)}$, but only at *that specific rate*
  - Motion energy filters respond to *arbitrary* velocities, not just $c_p^{(s)}$
  - PFE linear regime is *too rigid* to match motion energy — it only sees waves at $c_p$, not at arbitrary $v$

### Verdict

**WEAKEN**. Confidence: high.

The linear PFE is a *wave equation with propagation speed $c_p^{(s)}$*. It can recover:
- DoG-like response *if the cohesion source has center-surround structure* (i.e., DoG is *not derived* from PFE; it's *consistent* if input is structured)
- Single-scale spatial filtering (single Green's function)

The linear PFE *fails* to recover:
- Arbitrary-velocity motion energy filters (PFE is locked to one speed)
- Asymmetric biphasic temporal kernels (PFE's wave operator is symmetric in time)
- Sparse-coding / overcomplete representations (PFE has one field $u$, not many)

### Downstream consequence
- Linear PFE is *consistent* with retinal linear models *for special sources*, not *forced* by them
- The Iter 10 claim "Linearized matches DoG, motion energy in respective stages" is *too strong* — it matches DoG conditional on source structure, but does NOT match motion energy without additional structure
- For motion-energy match, need: *multiple stages with different $c_p^{(s)}$* covering a velocity range. Speed-tuned channels each at their own $c_p$. This is consistent with the multi-stage framework but is non-trivial to make precise.

### New OP registered
**OP-PFE-9**: Establish whether the multi-stage PFE (with stage-specific $c_p^{(s)}$ spanning a velocity range) can collectively reproduce the motion-energy spectrum. If not, PFE undershoots known retinal capability.

### What was NOT verified
- Higher-order (nonlinear) corrections — possibly add capability missing in linear regime
- Whether the "DoG-from-structured-source" reduction is *unique* or has free parameters
- The Wiener-filter optimality criterion (would require introducing a *noise model*, not currently in PFE)

### Register
CONDITIONAL-OBSERVATION (linear PFE = wave equation; matches DoG conditionally; fails to match motion-energy without multi-stage extension).

---

## Task 10 — Geodesic equation for "free perception"

### What is verified
Iter 10 lists "Geodesic equation → trajectory of perception unit" — i.e., motion perception, saccade trajectories. This task computes the geodesic equation in $g_{\mu\nu}^{(s)}$ and asks whether it has a sensible operational interpretation.

### Falsification criterion
If the geodesic equation requires *unphysical assumptions* (e.g., negative perceptual mass, complex-valued trajectories, no boundary conditions) to give finite physical trajectories, the geodesic interpretation is *purely formal* and Iter 10's claim that it describes "motion perception, saccade trajectories" is *unwarranted*.

### Geodesic equation

For a curve $x^\mu(\lambda)$ parametrized by affine $\lambda$:
$$\frac{d^2 x^\mu}{d\lambda^2} + \Gamma^\mu_{\nu\rho} \frac{dx^\nu}{d\lambda} \frac{dx^\rho}{d\lambda} = 0$$

In *flat* perception space ($\Gamma = 0$), geodesics are *straight lines* in $(t, x, y)$ with constant velocity. The "free perceptual trajectory" is:
$$x(t) = x_0 + v \cdot (t - t_0)$$

For a *timelike* geodesic ($g_{\mu\nu} \dot x^\mu \dot x^\nu < 0$): $|v| < c_p^{(s)}$. The trajectory is "inside the cone" at every point.

For a *null* geodesic ($g_{\mu\nu} \dot x^\mu \dot x^\nu = 0$): $|v| = c_p^{(s)}$. Light-cone trajectory.

For a *spacelike* geodesic: $|v| > c_p^{(s)}$ — *not realizable* as a perceptual trajectory (cannot trace it).

### Operational interpretation candidates

**Candidate 1: Saccade trajectory**
- Saccades sweep across the visual field at angular velocities up to ~500°/s ≈ 25 cm/s on the retina (for 50cm viewing distance)
- For Stage 1 (cone, $c_p \approx 0.05$ mm/s): saccade velocity $\gg c_p$ — saccades are *spacelike* in Stage 1's cone — they are *not* Stage-1 geodesics
- For Stage 5 (attention, $c_p \approx 0.3$ m/s = 300 mm/s): saccade velocity ≈ $c_p$ — saccades are *near-null* in Stage 5's cone
- **Interpretation**: saccades are *physical motions* that cross many Stage-1 perceptual cones but stay near Stage-5's null cone. Saccade trajectory could be a "null geodesic at the attentional stage".
- **But** saccades are *not free* (they are ballistic, driven by extraocular muscles, with specific velocity profile) — not a *geodesic in absence of forces*. Calling them "geodesics" requires identifying the source of the force (which is *not* PFE's $T_{\mu\nu}$ — saccades are *motor*, not *perceptual*).

**Candidate 2: Motion perception**
- A moving object at retinal velocity $v$ traces a *worldline* $x(t) = v t$ in $(t, x)$
- If the worldline is *inside* the Stage-$s$ cone ($|v| < c_p^{(s)}$), the object is perceived as motion at stage $s$
- A *free* (unaccelerated) motion percept is a *straight worldline* — that's a *geodesic in flat metric*
- Yes — **motion perception trajectories are timelike geodesics** in the appropriate stage's metric
- This is *operational* and *consistent*. PASS for this candidate.

**Candidate 3: Apparent motion**
- Two stimuli at $(t_1, x_1)$ and $(t_2, x_2)$ inside the cone get *connected* by a *perceived* trajectory
- The perceived trajectory is the *shortest path* between them, which (in flat Lorentzian) is the *straight line* — a geodesic
- Apparent motion trajectory = geodesic between stimuli. **Matches Korte's laws** (the perceived velocity is the straight-line connection)
- **PASS for this candidate**

**Candidate 4: Eye-tracking / smooth pursuit**
- Smooth pursuit of a moving target: eye follows target with brief latency
- Eye velocity in pursuit is the perceived target velocity
- Pursuit trajectory in perceptual space is a *geodesic* of the perceived target — *consistent* with the timelike geodesic of the percept
- **PASS**

### Boundary conditions / well-posedness

Geodesic equation is a *second-order ODE*: initial position + initial velocity uniquely determine trajectory (in flat metric, just a straight line; in curved metric, integrate the ODE).

In curved PFE metric (from cohesion-field source): geodesics *bend*. A salient point cohesion source produces a conical defect (Task 8); a moving target's perceived trajectory near a distractor bends toward/away depending on the sign of $\kappa$.

This is *qualitatively* like *attentional capture* — a salient distractor bends the trajectory of perceptual tracking. **Operationally testable**.

### Verdict

**PASS with REFINEMENT**. Confidence: medium-high.

The geodesic equation has *coherent* operational interpretations for:
- Motion perception (timelike geodesic in flat metric)
- Apparent motion connection (geodesic between cone-connected stimuli)
- Smooth pursuit (trajectory = percept's geodesic)
- Attentional capture (bending of geodesic near cohesion source) — TESTABLE prediction

It does *NOT* have a clean interpretation for:
- Saccade trajectories (saccades are *motor*, not *free perceptual motion*)

The Iter 10 claim "Geodesic equation → trajectory of perception unit ... saccade trajectories" *partially* fails: saccades are not geodesics. The motion-perception and apparent-motion interpretations *do* hold.

### Downstream consequence
- Iter 10 should be refined: drop "saccade trajectories" from geodesic interpretation, keep "motion perception" and add "apparent motion connection" + "attentional capture bending"
- The attentional capture prediction is *novel* — PFE predicts that a salient distractor (high local cohesion) should *bend* the trajectory of pursued targets nearby. Measurable with smooth-pursuit + distractor psychophysics.

### New OP registered
**OP-PFE-10**: Empirically test the attentional-capture geodesic-bending prediction with smooth-pursuit + distractor paradigm. Direction and magnitude of bending should depend on sign of $\kappa$ and magnitude of distractor cohesion.

### What was NOT verified
- The full curved-spacetime geodesic numerical integration (would require choosing a cohesion profile $u(x)$ and computing $g_{\mu\nu}[u]$)
- Whether the geodesic interpretation is *unique* among possible "natural trajectory" choices (might also use minimal-action curves with non-geodesic Lagrangian — these would differ if PFE has additional fields)
- Comparison to known motion-perception models (Adelson-Bergen, Reichardt detectors)

### Register
CONDITIONAL-OBSERVATION (geodesic = motion-perception / apparent-motion / pursuit trajectories under flat or weakly curved regime; ATTENTIONAL-CAPTURE bending is novel testable prediction).

---

## Phase B Summary

| Task | Target | Verdict | Confidence | Effect on framework |
|------|--------|---------|------------|---------------------|
| 6 | Dimensional analysis | PASS | High | $[\kappa^{(s)}] = L$; conversion $\tilde{t} = c_p t$ required |
| 7 | $\kappa^{(s)}$ candidates | PASS with WEAKEN caveat | Medium | $\kappa^{(s)} = c \cdot \ell_s$ candidate is plausible; dimensionless $c$ free parameter |
| 8 | Vacuum existence | WEAKEN with surprise | High | 1+2D vacuum is only flat + defects; Iter 10's Schwarzschild claim is wrong |
| 9 | Linearized form | WEAKEN | High | Linear PFE = wave equation at $c_p$; matches DoG conditionally; fails motion-energy without multi-stage |
| 10 | Geodesic interpretation | PASS with REFINEMENT | Medium-high | Motion/apparent-motion/pursuit work; saccades don't; attentional capture is novel prediction |

### Aggregate Phase B verdict

**PASS the field equation structurally** with multiple substantive REFINEMENTS:

1. **Iter 10 must drop the Schwarzschild-like regime** for 1+2D PFE (Task 8). It would require either a 3+1D extension or be restricted to the conical-defect case.

2. **Iter 10's linearized regime is partial-match to retinal linear models** (Task 9). DoG-from-source structure works; motion-energy fails without multi-stage extension.

3. **Iter 10's geodesic regime keeps motion perception** but loses saccades; **adds attentional capture** as a novel testable prediction (Task 10).

4. **$\kappa^{(s)}$ has correct units** (Task 6) and *biologically plausible candidates* (Task 7), but the dimensionless prefactor is empirically undetermined — OP-PFE-2 is *real and non-trivial*.

5. **Vacuum is non-trivial but narrow** (Task 8) — topological + defect content only; the framework lives almost entirely in the matter-coupled regime.

### New OPs registered in Phase B
- **OP-PFE-8**: Conical-defect angle vs perceived-angle near salient point stimulus
- **OP-PFE-9**: Multi-stage PFE collectively reproducing motion-energy spectrum
- **OP-PFE-10**: Attentional-capture geodesic-bending prediction (smooth pursuit + distractor)

### Pass 11 framework status after Phase B

| Component | Pre-Phase-B | Post-Phase-B |
|-----------|-------------|--------------|
| Dimensional consistency | implicit | verified, $[\kappa] = L$ |
| $\kappa^{(s)}$ origin | unspecified | $c \cdot \ell_s$ candidate, $c$ free |
| Vacuum regime | "Schwarzschild-like" claim in Iter 10 | flat + conical defects only (Schwarzschild claim wrong) |
| Linear regime | "matches DoG, motion energy" | matches DoG conditionally, fails motion-energy without multi-stage |
| Geodesic regime | "trajectories incl. saccades" | motion perception ✓; apparent motion ✓; pursuit ✓; saccades ✗ |
| Novel testable predictions | 4 (Tests 1-4) | 4 + OP-PFE-8 (defect angle) + OP-PFE-10 (attentional bending) |

### What was NOT done in Phase B
- Iter 10 not modified in 12_ (per discipline); refinements live here in 14_
- No numerical integration of geodesics or vacuum solutions
- No multi-stage motion-energy spectrum derivation (deferred to OP-PFE-9 / Pass 13)
- No fit of $\kappa^{(s)}$ prefactor against any specific dataset (Phase C protocols + Phase D OP-PFE-2 plan)

---

*Phase B v0. 5 tasks, 5 verdicts. Field equation structurally PASSES but with refinements: Schwarzschild claim wrong, linear regime partial-match, saccades dropped from geodesic interpretation, $\kappa$ remains free parameter. canonical/SCC/PAI/8-retractions 0 modifications. Next: Phase C Operational Test Protocols (Tasks 11-15).*
