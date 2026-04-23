# T_time_evolution.md — Time Evolution Theory Scoping

**Session:** 2026-04-23 (G4 deliverable; intended promotion target: `working/T/time_evolution.md`)
**Target (from plan.md §2 G4):** Sharp interface dynamics + coarsening framework scoping. 3-4 Cat C hypotheses.
**This file covers:** (a) gradient-flow on $\Sigma_m$ as primary dynamics; (b) sharp interface limit (MCF); (c) LSW coarsening for multi-formation; (d) nucleation Kramers rate; (e) open questions.
**Depends on reading:** `01_exploration.md` §5.1 (D1-D4 approach candidates), `canonical.md` §11 Three Pillars of Kinetic Multi-Formation, `canonical.md` §13 T14 (gradient flow), T11 (Γ-convergence), Cor 2.2 (tanh profile).

---

## §1. Framework overview

### 1.1 Hierarchy of dynamical regimes

| Regime | Dynamics | Time scale | Cat |
|---|---|---|---|
| **R-GF** | Deterministic gradient flow on $\Sigma_m$ | $t \in [0, \infty)$ | Established (T14 Cat A) |
| **R-SI** | Sharp interface limit ($\beta \to \infty$) | Leading order $t$ | T11 Γ-convergence Cat A |
| **R-LSW** | Long-time multi-formation coarsening | $t \gg t_{\mathrm{metastable}}$ | Sketched |
| **R-NUC** | Nucleation of new formation (zero → K=1) | $t \sim \tau_{\mathrm{nuc}}$ | Sketched |
| **R-LGV** | Langevin with noise $T > 0$ | any | G5 scope |

### 1.2 Primary equation

Gradient flow on constraint manifold:
$$\dot u = -\Pi_{\Sigma_m}\nabla \mathcal{E}(u) = -\nabla\mathcal{E}(u) + \frac{\langle\nabla\mathcal{E}, \mathbf{1}\rangle}{\langle \mathbf{1}, \mathbf{1}\rangle}\mathbf{1},$$

where $\Pi_{\Sigma_m}$ projects onto $T_u\Sigma_m = \{v : \sum v_i = 0\}$.

### 1.3 Existing canonical coverage

- **T14 (Gradient Flow Convergence)**: Converges to critical point; exponential via Łojasiewicz under analyticity ($b_D = 0$).
- **T11 (Γ-convergence)**: $\varepsilon = \alpha/\beta \to 0$ limit.
- **§11 Three Pillars**: Nucleation (Pillar I), Metastability (Pillar II), Coarsening (Pillar III). Pillar III is **kinetically determined** but no explicit time-dynamics theory in canonical.

---

## §2. Hypothesis H-T1: Sharp-interface limit is graph-MCF

### 2.1 Statement

> **Hypothesis H-T1 (Sharp-interface graph MCF)**. As $\beta \to \infty$ (equivalently $\xi_0 \to 0$), gradient flow of SCC energy $\mathcal{E}$ on $\Sigma_m$ converges (in appropriate sense) to a graph-analog of mean curvature flow:
> $$v_n(x, t) = \alpha \kappa_G(x, t) + \text{(self-referential correction)}$$
> on the moving interface $\partial A_t = \{x : u(x, t) = 1/2\}$, where $\kappa_G$ is a graph-discretized mean curvature and $v_n$ is normal velocity.

### 2.2 Motivating derivation

From T11 Γ-convergence: $\mathcal{E}_{\mathrm{bd}} / \sqrt{\alpha\beta} \to C_* \mathrm{Per}$ as $\xi_0 \to 0$. Gradient flow of perimeter = mean curvature flow in continuum limit (Brakke flow).

On graph: perimeter = edge boundary $|\partial A| = \#\{\text{edges between } A \text{ and } A^c\}$. Gradient flow of $|\partial A|$ on graph = edge-boundary minimization = **graph mean curvature flow** (discrete analog).

### 2.3 Self-referential correction

Closure term $\mathcal{E}_{\mathrm{cl}}$ and separation term $\mathcal{E}_{\mathrm{sep}}$ modify the surface tension in Γ-limit. From canonical T11: "self-referential correction terms modify the effective surface tension."

Explicit form: $\sigma_{\mathrm{eff}} = C_*\sqrt{\alpha\beta}(1 + \delta_{\mathrm{cl}} + \delta_{\mathrm{sep}})$ where $\delta$ are small corrections O($\lambda_{\mathrm{cl}}/\beta$). Direction of correction (stabilizing or destabilizing) depends on $a_{\mathrm{cl}}$ vs $\tau_{\mathrm{cl}}$ setup.

### 2.4 Category

- **Statement H-T1**: Cat C (requires graph-MCF convergence proof analogous to Almgren-Taylor-Wang 1993 on lattice).
- **Self-referential correction existence**: Cat B sketched (T11 already gives correction).
- **Quantitative $\sigma_{\mathrm{eff}}$ form**: Open (NQ candidate).

### 2.5 Failure modes

- **On irregular graphs** (SBM, barbell), graph-MCF concept itself is ill-defined (no natural curvature). H-T1 restricts to lattice-like graphs.
- **Finite-$\beta$ corrections**: Γ-convergence is asymptotic; for finite $\beta$, motion is not pure MCF. Intermediate regime (moderate $\xi_0/a$) is open.

---

## §3. Hypothesis H-T2: LSW coarsening on multi-formation

### 3.1 Statement

> **Hypothesis H-T2 (LSW coarsening on graph)**. In multi-formation regime ($K \geq 2$, well-separated), long-time gradient flow exhibits **Lifshitz-Slyozov-Wagner-type coarsening**: small formations shrink, large formations grow, mean formation size scales as $\langle r \rangle \sim t^{1/\gamma_{\mathrm{LSW}}}$ with SCC-modified exponent $\gamma_{\mathrm{LSW}}$.

### 3.2 Classical LSW context

- **Standard 2D Allen-Cahn / Cahn-Hilliard** coarsening: $\langle r \rangle \sim t^{1/3}$ (Ostwald ripening) or $\langle r \rangle \sim t^{1/2}$ (Allen-Cahn curvature-driven).
- **Scaling**: $\widehat K(t) \sim t^{-d/3}$ for Cahn-Hilliard in d-dim, $\widehat K(t) \sim t^{-d/2}$ for Allen-Cahn.

### 3.3 SCC modification

Closure enhances metastability (CN14, canonical §11, T7-Enhanced Cat A). 이로 인해 coarsening barrier 증가 — **coarsening slows down**.

Hypothesis: $\widehat K(t) \sim t^{-\beta_{\mathrm{LSW}}}$ with $\beta_{\mathrm{LSW}} < \beta_{\mathrm{standard}}$. Specifically (tentative):

$$\beta_{\mathrm{LSW}}^{\mathrm{SCC}} = \beta_{\mathrm{LSW}}^{\mathrm{AC}} \cdot \frac{1}{1 + \delta_{\mathrm{cl}}(a_{\mathrm{cl}})}.$$

### 3.4 Testable predictions

- 2D square c=0.3, running gradient flow from $\widehat K(0) = 10$ (random initialization), measure $\widehat K(t)$ over $t \in [10^2, 10^5]$ iterations.
- Expected: $\widehat K(t) \sim t^{-\beta_{\mathrm{LSW}}}$ with $\beta_{\mathrm{LSW}} < 1/2$ (slower than Allen-Cahn).

### 3.5 Category

- **Scaling law existence**: Cat C.
- **SCC-modified exponent < standard**: Cat C (plausible from closure barrier); direction consistent with CN14 claim.
- **Specific exponent value**: Open numerical experiment.

### 3.6 Failure modes

- **Short-time non-LSW**: At $t < t_{\mathrm{emerge}} + t_{\mathrm{metastable}}$, system is in trapped metastable, not coarsening. LSW applies only in long-time asymptotic.
- **Graph topology**: Coarsening exponent depends on $d_{\mathrm{eff}}$; for non-lattice graphs, $d_{\mathrm{eff}}$ may not be well-defined.
- **Freeze-out at zero T**: Deterministic gradient flow may reach K-sector and never escape (protocol-selection). Coarsening → K=1 global min may never be observed at zero T.

---

## §4. Hypothesis H-T3: Nucleation via Kramers (finite T)

### 4.1 Statement

> **Hypothesis H-T3 (Nucleation rate)**. At finite temperature $T > 0$, the nucleation rate for $\mathcal{B}_0 \to \mathcal{B}_1$ (uniform → K=1 formation) follows Kramers form:
> $$\tau_{\mathrm{nuc}}^{-1}(T, \beta) = \tau_0^{-1} \exp(-\Delta\mathcal{F}_c(\beta) / T),$$
> where $\Delta\mathcal{F}_c(\beta)$ is the critical-nucleus energy (saddle-point energy minus uniform energy).

### 4.2 Motivation

Classical Kramers theory for escape from metastable state over barrier: rate $\tau^{-1} = \tau_0^{-1} \exp(-\Delta\mathcal{F}/T)$ with $\tau_0$ attempt frequency.

In SCC: uniform $u = c$ state at $\beta > \beta_{\mathrm{crit}}^{(2)}$ is **unstable** (saddle). Nucleation of non-uniform state doesn't require barrier crossing — deterministic pitchfork suffices.

**But**: at $\beta < \beta_{\mathrm{crit}}^{(2)}$, uniform is **stable** (local min). Nucleation of K=1 requires thermal fluctuation over barrier.

### 4.3 Critical nucleus energy

From pitchfork structure: $\beta_{\mathrm{crit}}^{(2)}$에서 barrier는 $0$ (inflection). Below threshold, $\Delta\mathcal{F}_c(\beta) = A(\beta_{\mathrm{crit}}^{(2)} - \beta)^{3/2}$ (power $3/2$ universal for supercritical pitchfork).

So:
$$\tau_{\mathrm{nuc}}^{-1}(T, \beta) \sim \exp(-A(\beta_{\mathrm{crit}}^{(2)} - \beta)^{3/2}/T).$$

For $\beta$ near critical, nucleation rate rises sharply.

### 4.4 Category

- **Existence of Kramers rate**: Cat C (requires finite-T Langevin framework P-F, currently open).
- **Exponent $3/2$ form**: Cat C (from Crandall-Rabinowitz structure).
- **Prefactor $\tau_0$**: Open (requires Langevin friction specification).

### 4.5 Failure modes

- **P-F (thermal framework) absence**: Current canonical is zero-T. Without P-F, "metastability with escape rate" is informal. Must flag per Hard Constraint #9.
- **On supercritical side**: At $\beta > \beta_{\mathrm{crit}}^{(2)}$, uniform is unstable — no barrier to cross. Nucleation is deterministic, not Kramers. Hypothesis applies only subcritical.

---

## §5. Hypothesis H-T4: Protocol-dependent short-time dynamics

### 5.1 Statement

> **Hypothesis H-T4 (Short-time protocol dependence)**. Gradient flow from initial condition $u_0 \sim \mu_{\pi, \mathrm{init}}$ passes through three phases:
> (a) **Emergence**: $t \in [0, t_{\mathrm{emerge}}]$, unstable Fiedler modes grow exponentially. $t_{\mathrm{emerge}} \sim \ln(1/\sigma_0) / |\mu_{\min}|$.
> (b) **Metastable plateau**: $t \in [t_{\mathrm{emerge}}, t_{\mathrm{coarsen}}]$, $\widehat K(t) \approx \widehat K_{\mathrm{emergence}}$ constant.
> (c) **Coarsening** (if $T > 0$ or slow noise): $t > t_{\mathrm{coarsen}}$, $\widehat K(t) \to 1$.
> Protocol $\pi$ determines $\widehat K_{\mathrm{emergence}}$ via Fiedler-mode initial alignment.

### 5.2 Relation to canonical §11 Three Pillars

- Pillar I (Nucleation): phase (a).
- Pillar II (Metastability): phase (b).
- Pillar III (Coarsening): phase (c).

H-T4 quantifies the three pillars as a **three-phase dynamical decomposition**.

### 5.3 Falsifiability

R17/R19/R20 empirical:
- 2D c=0.3, $t \to \infty$ under zero-T: $\widehat K$ saturates at metastable ≈ 7.76 (R17). Phase (b) persists indefinitely at T=0.
- c=0.5 torus: $\widehat K = 1.00$. Fast coarsening; phase (b) short or absent.

**Consistent** with H-T4 if $t_{\mathrm{coarsen}}$ depends on protocol / c regime.

### 5.4 Category

- **Three-phase decomposition**: Cat A empirical (confirmed by R17-R22).
- **$t_{\mathrm{emerge}} \sim \ln(1/\sigma_0)/|\mu_{\min}|$**: Cat A (standard linearization).
- **$\widehat K_{\mathrm{emergence}}$ from protocol**: Cat B (R22 V5 confirmed protocol-dependence, quantitative formula open).
- **$t_{\mathrm{coarsen}}$ at T=0**: Open, depends on whether landscape has kinetic traps.

---

## §6. Sharp-interface dynamics formalism

### 6.1 Moving interface description

For $u_t$ in sharp-interface regime, define $A_t = \{x : u_t(x) > 1/2\}$. Evolution of $\partial A_t$ is the primary object.

Graph-MCF equation (heuristic):
$$v_n(x; \partial A_t) = -\alpha \kappa_G(x; \partial A_t) + C_{\mathrm{cl}}(x; A_t) + C_{\mathrm{sep}}(x; A_t)$$

where:
- $\kappa_G$ = mean curvature analog (number of neighbors outside $A_t$ minus inside, sign conventions).
- $C_{\mathrm{cl}}$ = closure correction from $\mathcal{E}_{\mathrm{cl}}$ (self-referential).
- $C_{\mathrm{sep}}$ = separation correction from $\mathcal{E}_{\mathrm{sep}}$.

### 6.2 Continuum limit

On $k \times k$ 2D grid as $k \to \infty$: graph Laplacian → continuous Laplacian; graph MCF → continuous MCF ($v_n = \kappa$). Continuum limit is Brakke flow with surface tension $C_*\sqrt{\alpha\beta}$.

### 6.3 Category

- **Graph-MCF heuristic equation**: Cat C.
- **Continuum limit to Brakke flow**: Cat C (standard in Allen-Cahn; SCC modification unverified).
- **Self-referential corrections in moving-interface form**: Open.

---

## §7. Coarsening on multi-formation — detailed scoping

### 7.1 Starting point: multi-formation at emergence

After phase (a), $\widehat K_{\mathrm{emergence}}$ formations exist at random positions with approximately equal mass $m/\widehat K$.

### 7.2 Coarsening mechanism

Two mechanisms:
- **(C1) Direct merger**: Two formations with overlapping support merge into one (if support overlap large enough; strong-overlap regime).
- **(C2) Indirect shrinkage**: Small formations lose mass to large (Ostwald ripening), eventually disappear.

At zero T, **(C1)** requires sufficient initial overlap (nucleation-set geometry). **(C2)** requires mass transfer channel (diffusion via constraint).

### 7.3 Well-separated regime's freezing

For $d_{\min} \gg \xi_0$ (well-separated):
- (C1) direct merger: blocked (no overlap).
- (C2) Ostwald: blocked (mass transport requires tunneling).

**Result**: Well-separated $\widehat K$ formations are **frozen at zero T** (no coarsening, at least within finite time). This matches R17/R18 empirical: K-sector stays constant.

### 7.4 Escape to K=1 requires noise

At T > 0, barrier-crossing via Kramers rate. Expected:
$$t_{\mathrm{merger}}(j,k) \sim \tau_0 \exp(\Delta\mathcal{F}_{\mathrm{merger}}(d_{\min}(j,k)) / T).$$

Barrier $\Delta\mathcal{F}_{\mathrm{merger}}$ decreases with $d_{\min}$ (closer formations merge more easily).

### 7.5 LSW scaling from escape rates

If merger rates follow Kramers distribution across formation pairs, mean $\widehat K(t)$ evolution integrates to power law. Classical LSW derivation gives $\langle r \rangle \sim t^{1/3}$ (2D) under diffusion-limited mass transfer.

For SCC with closure barrier: $t^{1/3}$ scaling may modify to $t^{\beta_{\mathrm{SCC}}}$ with $\beta_{\mathrm{SCC}} < 1/3$.

### 7.6 Category

- **Coarsening mechanisms (C1, C2)**: Cat A (standard classical).
- **Well-separated freezing at T=0**: Cat A (from (C1), (C2) combined analysis).
- **LSW power law at T>0**: Cat C (requires P-F + detailed barrier analysis).
- **SCC-modified exponent**: Open.

---

## §8. Integration with canonical

### 8.1 Canonical §11 Three Pillars → quantitative form

Canonical §11 Three Pillars qualitative:
- Pillar I: Fiedler-mode seeded.
- Pillar II: metastability via Hessian PD.
- Pillar III: kinetic coarsening.

This session's contribution:
- Three-phase time decomposition (§5 H-T4) as quantitative Pillar framework.
- Well-separated freezing (§7.3) as explicit Pillar II statement at zero T.
- LSW scaling conjecture (§3) as Pillar III refinement.

### 8.2 Canonical §13 T14 Gradient Flow

T14 says gradient flow converges. **H-T4 refines**: convergence may be "to metastable plateau, frozen at zero T", not "to global minimum". T14 convergence is **to critical point**, not global min — consistent.

### 8.3 Canonical §11 "Multi-formation is kinetic"

Expanded with explicit timescale decomposition. Closure's barrier enhancement (CN14) quantified as **slower LSW exponent**.

---

## §9. Open questions

### 9.1 NQ-62 — $t_{\mathrm{coarsen}}$ at zero T: finite or infinite?

Does a zero-T gradient flow from random IC eventually reach K=1 (after very long time)? Or does it freeze in K-sector indefinitely?

**Hypothesis**: Well-separated case → freezes indefinitely (barrier infinite in ellipsoidal coordinate).  
**Empirical**: R17 at T=0 saturates at K=7.76 (apparently frozen).  
**Candidates**: 실험으로 초장기 (t > 10^6) gradient flow 관측.

### 9.2 NQ-63 — Nonuniform coarsening rate

In LSW classical, rate is exponent-constant. Does SCC show **different rates in different K-sectors**? Predicts non-universal exponent.

### 9.3 NQ-64 — Interaction with protocol

If $\pi$ changes mid-flow (warm-start $\to$ re-normalize), does K evolve non-monotonically?

### 9.4 NQ-65 — Continuous limit existence

Does $(u_t, t \in \mathbb{R}_+)$ on increasing graphs $G_k$ have continuum limit? Related to OP-0022.

### 9.5 NQ-66 — Noise-assisted nucleation rate

Scaling of nucleation rate with noise amplitude $\sigma$? H-T3 Kramers form assumes Gaussian white noise; physical protocol noise may be non-Gaussian.

---

## §10. Hypothesis summary table

| Hypothesis | Content | Category | Main failure mode |
|---|---|---|---|
| H-T1 | Graph-MCF sharp-interface limit | Cat C | Non-lattice graphs |
| H-T2 | LSW coarsening with SCC-modified exponent | Cat C | Zero-T freeze-out |
| H-T3 | Kramers nucleation rate at finite T | Cat C | Requires P-F (open) |
| H-T4 | Three-phase emergence → plateau → coarsening | Cat A (empirical R17-R22 sufficient) | Quantitative $\widehat K_{\mathrm{emergence}}$ formula open |

---

## §11. Connection to G5 (thermal)

H-T3 (Kramers nucleation) **explicitly requires finite-T framework**. This overlap makes G4 and G5 deeply linked:
- G4 (this file): zero-T deterministic dynamics + scoping of what thermal would change.
- G5 (next file `T_thermal_softmax.md`): finite-T framework + Layer 1 selector smoothing.

---

## §12. File status

- **Primary deliverable**: 4 hypotheses (H-T1, H-T2, H-T3, H-T4) with Cat assessment + failure modes + testability.
- **Methodology**: scoping (not proof-focused) per plan.md §2 G4.
- **Intended promotion**: `working/T/time_evolution.md` (신규 디렉토리 + 파일).

**End of T_time_evolution.md.**
