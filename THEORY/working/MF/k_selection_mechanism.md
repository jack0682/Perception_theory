# k_selection_mechanism.md — Direct Attack on OP-0005 K-Selection Mechanism

**Status:** working draft (W5 Day 4 PM Wave 3, 2026-04-30). Single-topic working file per `THEORY/working/MF/` convention.
**Type:** Theory-only deepening file (no canonical edits, no compute). Targets OP-0005 (HIGH severity, OPEN). Three Cat C selection-mechanism candidates proposed; empirical-verification + W6+ NQ plan attached.
**Author origin:** OAT-track follow-up to Commitment 16 (CV-1.5.1, OAT-1) + CN15 Static/Dynamic Separation (W4 04-23). Wave 3 dispatch alongside Bridge B-7 (foundational_bridges_2026.md §8 AC analog).
**Canonical refs:** §11.1 #16 Commitment 16 (K_field/K_act decomposition); §14 CN6 (kinetic determination, refined); §14 CN15 (Static/Dynamic Separation Principle); §13 T-Merge (b) (single-field static minimum K=1); §13 T-PreObj-1G (graph-class-independent pre-objective mechanism); §13 T-σ-Lemma-1/2/3 + T-σ-Theorem-3/4 (σ-framework supporting structures).
**Working refs:** `K_status_commitment.md` (OAT-1, Commitment 16 origin); `foundational_bridges_2026.md` §8 (Bridge B-7 AC analog); `pre_objective_K_field_tension.md` (OAT-6); `multi_formation_sigma.md` (D-6a static framework, $\mathrm{Aut}(G)_{u^*}$ scaffolding); `sigma_multi_trajectory.md` §2 (K-jump definition).
**Open problems:** OP-0005 K-Selection Mechanism (HIGH, OPEN — direct target of this file); OP-0008 σ^A K-jump non-determinism (closely related, separate); OP-0009-K (RESOLVED via Commitment 16, K-status defined but selection unresolved).

---

## §1. Mission

> **Direct attack on OP-0005 K-Selection Mechanism (HIGH severity, OPEN per `open_problems.md` §286).**
>
> "Theory provides no mechanism for how K (number of formations) is determined." After Commitment 16 (CV-1.5.1) the question sharpens to: **what mechanism selects $K_{\mathrm{act}}$ within the architectural cap $K_{\mathrm{field}}$**, given that CN15 Static/Dynamic Separation forbids identifying the dynamic protocol-endpoint observable with the static energy minimum?

OP-0005 had three pre-Wave-3 partial moves:

1. **σ-framework partial coverage** (W5 Day 1 G0): Lemma 1/2/3 + Theorem 3/4 give labeled-quantization structure refining $K_{\mathrm{step}}$ to a σ-tuple, but do not identify *which* K_act emerges.
2. **CN15 Static/Dynamic Separation** (W4 04-23): explains *why* energy-minimization argument (T-Merge (b) Cat A: $K^*_{\mathrm{step,global}} = 1$) does **not** force $K_{\mathrm{act}}=1$ at protocol endpoint. Forbids reductive answer; does not provide selection law.
3. **Commitment 16 K_field/K_act decomposition** (CV-1.5.1, OAT-1): clarifies *what* is being selected (K_act), establishes K_act as derived integer diagonal of a K-field minimizer, but the *selection rule* $\text{IC} \to K_{\mathrm{act}}(t \to \infty)$ is left open.

This file goes **beyond** all three: it proposes **three concrete K-selection mechanism candidates** (a) free-energy variational, (b) kinetic metastability, (c) symmetry-broken automorphism-stabilizer dimension; checks each against Commitment 16, CN10, CN15, CN5; sketches the empirical-verification plan on the R23 90-run dataset; and registers three new W6+ NQ items. **None of the three is promoted.** All remain Cat C / philosophical-scaffolding pending verification work.

The goal is **not** to silently resolve OP-0005. The goal is to convert OP-0005 from *"no candidate mechanism"* (current state) into *"three explicit Cat C candidates with empirical-verification plan"*, so that subsequent W6+ NQ work has a structured target.

---

## §2. Status Review — Where K-Selection Stands After Commitment 16

### §2.1 What Commitment 16 resolved

Per `K_status_commitment.md` §4.1, Commitment 16 (CV-1.5.1, canonical §11.1 #16):

- **K_field**: architectural cap, modeling-layer commitment, integer set externally before instantiation.
- **K_act(t)**: derived integer diagnostic, $K_{\mathrm{act}}(\mathbf{u}(t)) := \#\{j : \|u^{(j)}(t)\|_1 > \epsilon\}$ for support threshold $\epsilon$.
- Inequality $K_{\mathrm{act}}(t) \leq K_{\mathrm{field}}$.
- CN6 refined: "K kinetically determined" applies to **K_act** within $\{1, \ldots, K_{\mathrm{field}}\}$.

The four-month K-status ambiguity (5 conflicting uses) collapsed to a single two-tier decomposition. **OP-0009-K** (sub-item of OP-0009 Multi-Formation Ontological Foundations) is RESOLVED.

### §2.2 What Commitment 16 explicitly leaves open

Per `K_status_commitment.md` §4.3:
> "**K-Selection mechanism (OP-0005)**: 'What sets K_act(0)?' is OP-0005 (still HIGH severity). Commitment 16 says K_act emerges from dynamics + IC, but doesn't give a *full mechanism* for IC-to-K_act mapping."

So OP-0005 sharpens to:

> **OP-0005 (post-Commitment 16 form)**: Given $(G, K_{\mathrm{field}}, M, \beta, \alpha, c, \lambda_{\mathrm{rep}}, u_0)$ and a gradient-flow protocol $\pi$, what mechanism predicts $K_{\mathrm{act}}(t \to \infty; \pi, u_0)$?

T-Merge (b) Cat A says: at the **global static minimum** (zero noise, infinite time, no kinetic barrier), $K_{\mathrm{act}}^* = 1$. But CN15 forbids identifying this with the protocol-endpoint observable. The R23 90-run empirical dataset (`scripts/sigma_class_count_R23.py` + 56 distinct minimizers) shows non-trivial $K_{\mathrm{act}} \in \{1, 2, 4\}$ distribution under finite-time protocol — proving the gap.

### §2.3 Why no existing canonical theorem closes the gap

| Tool | What it gives | Why it does not select K_act |
|---|---|---|
| T-Merge (b) | Static minimum $K=1$ on single field | Static; CN15 forbids using as endpoint predictor |
| T-PreObj-1G | $\mathcal{F}=1$ disk non-critical (graph-class-independent) | Says "default $\mathcal{F}\geq 2$" — doesn't pick *which* K |
| T-σ-Theorem-3/4 | σ-tuple invariance + first-pitchfork bound | Refines K-quantization label; doesn't select K |
| T-Persist-K-Unified (Cat C) | Multi-formation persistence on smooth segment | Conditional on K already fixed; not a selection rule |
| Commitment 14-Multi (D-6a) | Static σ-class enumeration on $\widetilde\Sigma^{K_{\mathrm{field}},\circ}_M$ | Enumerates classes; selection unspecified |

**Gap diagnosis**: No canonical entry maps initial-data-and-protocol $(\pi, u_0)$ → $K_{\mathrm{act}}(\infty)$ in a constructive way. The theory currently *enumerates* possible K_act values (per architecture cap and σ-class structure) without picking one.

---

## §3. Three Candidate K-Selection Mechanisms (Cat C)

The candidates are listed in increasing departure from current canonical scaffolding. Each is **Cat C target only** — all require either external structural input (free-energy: temperature; kinetic: rate-equation parameters) or a new mathematical primitive (symmetry: $\mathrm{Aut}(G)_{u^*}$ stabilizer dimension), and none is yet empirically anchored on R23 data.

### §3.1 Candidate (a): Free-Energy Variational Principle

**Statement (informal):**
$$K_{\mathrm{act}}^{(a)} = \arg\min_{K \in \{1, \ldots, K_{\mathrm{field}}\}} F(K; \beta, T, m), \qquad F(K) := E^*(K) - T \cdot S_{\mathrm{config}}(K)$$
where $E^*(K)$ is the SCC energy of the K-minimum-energy K-formation configuration on $\Sigma^K_M$ and $S_{\mathrm{config}}(K)$ is a configurational entropy counting the number of distinct σ-classes (or labeled microstates) compatible with active count K.

**Reading**: K_act is selected by free-energy minimization with a temperature-like parameter $T$. At $T=0$: degenerate (any K with $E^*(K) = E^*(1) = E_{\min}$ is admissible). At $T>0$: entropic selection favors $K$ with larger $S_{\mathrm{config}}(K)$.

**SCC-specific subtleties**:

- SCC at zero noise (canonical default) has **no temperature parameter**. The natural $T$-analog is the protocol's noise scale (P-F flag in working/E framing) or the inverse of $\beta$ (closure scale).
- Configurational entropy: per Commitment 14-Multi (D-6a), σ-class count on $\widetilde\Sigma^{K_{\mathrm{field}},\circ}_M$ is finite; one obtains $S_{\mathrm{config}}(K) = \log |\Omega_K|$ where $\Omega_K = \{[\sigma_{\mathrm{multi}}^A] : K_{\mathrm{act}} = K\}$.
- $E^*(K)$ is computable from the K-field minimizer via `scc/multi.py` per fixed K.

**Cat target**: C. Requires (i) explicit T-parameter introduction (extends canonical with thermal layer), (ii) entropy formula validation on R23, (iii) crossover empirical confirmation.

**Reference parallels (CN10 contrastive only)**:
- Bayesian model selection: BIC penalty $-2\log L + k \log n$ (Schwarz 1978).
- AIC penalty $-2\log L + 2k$ (Akaike 1974).
- Statistical mechanics free-energy minimization with fluctuation-driven configurational entropy.

**SCC is not Bayesian inference, not statistical mechanics**. The parallel imports the *variational form*; SCC retains its native primitive $u_t$ and energy $\mathcal{E}$.

### §3.2 Candidate (b): Kinetic Metastability (Kramers / Transition State)

**Statement (informal):** K_act(t→∞) is determined by initial conditions $u_0$ and barrier-crossing rates between K-stratified basins per Kramers' formula:
$$\tau_{K \to K'} \asymp \tau_0 \cdot \exp\left( \beta \cdot \Delta E(K \to K') \right)$$
where $\Delta E(K \to K')$ is the energy barrier separating the K-active basin from the K'-active basin (e.g., merger barrier from K=2 to K=1).

**Reading**: K_act(t) is the active count of the basin of attraction of $u_0$ in the gradient flow. Long-time limit is set by which basin transitions are kinetically accessible at the protocol's finite time horizon $t_{\mathrm{horizon}}$; basins with $\tau_{K \to K'} \gg t_{\mathrm{horizon}}$ are dynamically protected.

**SCC-specific subtleties**:

- Aligns directly with CN6 (kinetic determination) and CN15 (Static/Dynamic Separation) — gives a quantitative version.
- $\Delta E$ barriers are accessible via NQ-242 ridge-tracking or via the merge-path manifold (T-Merge (c)(d)(e) WERE retracted, so barrier characterization is currently Cat B-conditional).
- Connects to N-1 Soft-Hard Switching Asymmetry (`working/open_problems_reframing_2026-04-19.md` §8): the "P-F flag" (path-following finite-noise regime) mediates rate-vs-equilibrium.

**Cat target**: C. Requires (i) Kramers-formula validation on $\Sigma^K_M$ (currently no canonical Kramers theorem in SCC), (ii) barrier-energy quantification (post T-Merge retraction, no validated $\Delta E$ formula), (iii) empirical horizon-dependent test.

**Reference parallels (CN10 contrastive only)**:
- Kramers, H. A. (1940). *Brownian motion in a field of force and the diffusion model of chemical reactions.* Physica 7, 284–304.
- Eyring, H. (1935) transition state theory; Hänggi-Talkner-Borkovec (1990) review.

### §3.3 Candidate (c): Symmetry-Broken Automorphism-Stabilizer Selection (NEW)

**Statement (informal):** Among the K-minimum configurations $\{u^*(K) : K \in \{1, \ldots, K_{\mathrm{field}}\}\}$, the protocol selects the K with **smallest local automorphism stabilizer**:
$$K_{\mathrm{act}}^{(c)} = \arg\min_{K} \dim \mathrm{Aut}(G)_{u^*(K)} \quad \text{(or } \arg\min_K |\mathrm{Aut}(G)_{u^*(K)}|\text{ for finite groups)}$$
where $\mathrm{Aut}(G)_{u^*(K)} := \{\phi \in \mathrm{Aut}(G) : \phi^* u^*(K) = u^*(K)\}$ is the stabilizer of $u^*(K)$ under graph-automorphism action.

**Reading**: K_act is the most **symmetry-broken** value — the configuration whose automorphism stabilizer is smallest among the candidates.

**Heuristic justification (genericity principle)**: A symmetric minimizer is non-generic — small generic perturbations of initial data drive the trajectory away from high-symmetry fixed manifolds toward broken-symmetry manifolds (echoes Goldstone / spontaneous symmetry breaking in physics; see V5b-T canonical §13 for SCC's translation-Goldstone analog). On generic IC distributions, the protocol-endpoint should land in the manifold with **the most freedom** — i.e., the smallest stabilizer.

**SCC-specific subtleties**:

- Naturally graph-theoretic: $\mathrm{Aut}(G)_{u^*}$ is fully determined by the graph $G$ and the configuration $u^*$, requires no external thermal or kinetic parameter.
- Connects to Bridge B-2 (Hutchcroft-Easo Schramm locality, `foundational_bridges_2026.md` §3): σ-tuples at first pitchfork depend on local automorphism structure.
- Connects to Bridge B-3 (Geometric Langlands, §4): formation fundamental group $\pi_1(\mathcal{F})$ candidate is exactly $\mathrm{Aut}(G)_{u^*}$.

**R23 D₄ free-BC concrete prediction (32×32 canonical config)**:

| K_act | Configuration | $\mathrm{Aut}(G)_{u^*(K)}$ | Order |
|---|---|---|---|
| 1 | central blob | full $D_4$ | 8 |
| 2 | axis-aligned twin | $\mathbb{Z}_2$ (axis reflection) | 2 |
| 4 | quadrant-localized | trivial $\{e\}$ | 1 |

**Prediction**: K_act = 4 has smallest stabilizer (order 1) → **Candidate (c) predicts K=4** as the selected count.

**Empirical comparison**: R23 90-run dataset (W4 04-23, c=0.5, β=30) gives a stratified $K_{\mathrm{act}}$ distribution. If the empirical **modal** K_act on adaptive-IC mode matches K=4, candidate (c) gains a Cat B-grade empirical anchor.

**Cat target**: C. Promoted to Cat B candidate target if R23 verification (NQ-302 below) confirms.

**Reference parallels (CN10 contrastive only)**:
- Spontaneous symmetry breaking in physics (Goldstone 1961; Anderson 1963).
- Chossat-Lauterbach equivariant bifurcation theory (1994) — bifurcation branches in $G$-equivariant systems classified by isotropy subgroups.
- Generic principle in algebraic geometry: generic point of variety has trivial stabilizer.

**SCC is not equivariant bifurcation theory, not gauge theory.** Imports the genericity heuristic; retains its native energy and primitive.

---

## §4. AC Philosophical Analog (CN10 Contrastive)

Per Bridge B-7 (`foundational_bridges_2026.md` §8) and Quanta Magazine 2026-04 retrospective on the Axiom of Choice (AC):

| Axiom of Choice | OP-0005 K-Selection |
|---|---|
| Selection function exists, no construction | $K_{\mathrm{act}}(\infty)$ exists in observed dynamics, no canonical selection law |
| ZF + AC vs ZF + ¬AC: independence | SCC + (a)/(b)/(c) mutual independence prior to empirical anchor |
| Forcing: $V[G]$ extension realizes alternative selection | Protocol $\pi$ extension realizes alternative K_act |
| Constructive vs non-constructive | Energy-minimization (constructive) vs additional-axiom (non-constructive) |

The structural lesson: AC's *"selection without construction"* is exactly the form of OP-0005 in current canonical state. T-Merge (b) is *constructive* (gives $K^*_{\mathrm{static}} = 1$); but CN15 says this is the wrong question. The *right* question (K_act(∞) given protocol) is **non-constructive in canonical** — no canonical theorem produces it. The candidates §3.1–§3.3 each propose an axiom-like extension ("introduce $T$"; "introduce kinetic timescale"; "introduce stabilizer order") that turns non-constructive selection into constructive choice.

**CN10 status (strict)**: SCC is **not** foundational set theory. The AC analog is *philosophical orientation only* — it does not import any AC theorem nor identify SCC's selection problem with cardinal selection. The bridge methodology imports *the recognition that selection problems can be axiomatized rather than reduced*; SCC retains its own primitives.

---

## §5. Free-Energy Formulation (Most Concrete Candidate)

This section unpacks Candidate (a) §3.1 in computable detail.

### §5.1 Setup

For a fixed K-field architecture with cap $K_{\mathrm{field}}$ and per-formation mass partition $\{m_j\}$, define:

$$E^*(K; G, \beta, \alpha, c) := \min_{\mathbf{u} \in \widetilde\Sigma^{K_{\mathrm{field}},\circ}_M, \, K_{\mathrm{act}}(\mathbf{u}) = K} \mathcal{E}_K(\mathbf{u}; G, \beta, \alpha, c)$$

i.e., the minimum SCC energy over K-field minimizers with specified active count $K$. (Computable via `scc/multi.py` per fixed K, restricted to active-count stratum.)

For configurational entropy, define
$$S_{\mathrm{config}}(K; G) := \log\left|\Omega_K\right|, \qquad \Omega_K := \{[\sigma_{\mathrm{multi}}^A(\mathbf{u}^*(K))] : \mathbf{u}^*(K) \in \arg\min_{K_{\mathrm{act}} = K} \mathcal{E}_K\}$$
i.e., the log of the number of distinct σ-classes (under $S_{K_{\mathrm{field}}}$ multi-set treatment, Definition 5.1(c) of `multi_formation_sigma.md`) achievable at active count K. Finite by Commitment 14-Multi finiteness (D-6a, CV-1.5.1, Cat A).

### §5.2 Free-energy form

$$F(K; G, \beta, \alpha, c, T) := E^*(K) - T \cdot S_{\mathrm{config}}(K)$$

**Zero-noise limit ($T = 0$)**: $F(K) = E^*(K)$. Per T-Merge (b) Cat A, $E^*(1) \leq E^*(K)$ for $K > 1$ on single-field landscape; on K-field with $\lambda_{\mathrm{rep}} > 0$, the inequality flips for some regimes. **Degenerate** when energy tie occurs.

**Finite-noise limit ($T > 0$)**: entropic selection. Generic prediction: as $T$ increases from 0, the minimizer of $F$ jumps from $K^* = 1$ (energy-dominated) to $K^* > 1$ (entropy-dominated) at a crossover temperature
$$T_c \approx \frac{E^*(K^* > 1) - E^*(1)}{S_{\mathrm{config}}(K^* > 1) - S_{\mathrm{config}}(1)}$$

### §5.3 Predictions for R23 (32×32, c=0.5, β=30, free-BC, D₄)

Using the 56 distinct minimizers from `sigma_class_count_R23.json`:

| K_act | # σ-classes | $E^*(K)$ rank | $F(K)$ at $T=0$ | $F(K)$ at $T = T_c$ |
|---|---|---|---|---|
| 1 | (small, central) | lowest | preferred | crossed by K>1 |
| 2 | (axis or diagonal split) | mid | suppressed | competitive |
| 4 | (quadrant-localized) | highest | suppressed | competitive |

**Concrete numeric prediction (NQ-301 deliverable)**: Run `scc/multi.py` per fixed-K_act stratum; extract $E^*(K)$ and $|\Omega_K|$; compute $T_c$; check whether observed adaptive-IC R23 distribution (W4 04-23, 90 runs) matches $T_c$ implied by protocol noise.

If protocol noise scale $T_{\mathrm{eff}} \approx T_c$, candidate (a) is *empirically anchored*. Otherwise, candidate (a) is rejected (or refined with non-trivial $S_{\mathrm{config}}$ formula).

### §5.4 P-F flag connection

The N-1 Soft-Hard Switching Asymmetry (`working/open_problems_reframing_2026-04-19.md` §8) introduces a "P-F flag" distinguishing protocol-endpoint regimes (path-following / finite-noise) from full minimization. Candidate (a) is **the natural quantification of P-F flag**:

- P-F flag OFF (zero noise): $T = 0$ → $K^* = 1$ per T-Merge (b).
- P-F flag ON (finite noise / finite time): $T > 0$ → entropic selection of $K^* > 1$.

The crossover temperature $T_c$ converts the qualitative N-1 flag into a quantitative selection rule.

---

## §6. Symmetry-Broken Selection (NEW Cat C Candidate, §3.3 unpacked)

This section unpacks Candidate (c) — the genuinely new mechanism candidate.

### §6.1 Definition: Local Automorphism Stabilizer

For graph $G = (V, E)$ with automorphism group $\mathrm{Aut}(G)$ and configuration $u^* : V \to [0,1]$:
$$\mathrm{Aut}(G)_{u^*} := \{\phi \in \mathrm{Aut}(G) : u^*(\phi(v)) = u^*(v) \, \forall v \in V\}$$

For K-field configurations $\mathbf{u}^* = (u^{(1)*}, \ldots, u^{(K_{\mathrm{field}})*})$, the stabilizer acts on a *labeled* configuration; for the **unlabeled** symmetry class (per Tool A2 quotient picture, `mathematical_scaffolding_4tools.md`), use:
$$\mathrm{Aut}(G)_{[\mathbf{u}^*]} := (\mathrm{Aut}(G) \times S_{K_{\mathrm{field}}})_{[\mathbf{u}^*]}$$
quotienting by the joint graph-automorphism × formation-permutation action.

### §6.2 Selection rule

$$K_{\mathrm{act}}^{(c)} := \arg\min_{K \in \{1, \ldots, K_{\mathrm{field}}\}} \left|\mathrm{Aut}(G)_{[\mathbf{u}^*(K)]}\right|$$

with ties broken by lower energy ($E^*$).

### §6.3 R23 32×32 D₄ free-BC concrete computation

R23 graph: 32×32 grid with free boundary conditions; $\mathrm{Aut}(G) = D_4$ (order 8: 4 rotations + 4 reflections).

For canonical-mass K-field minimizers ($M = $ total mass):

**K = 1 (central blob)**: minimizer concentrates near center. $\mathrm{Aut}(G)_{u^*(1)} = D_4$ (order 8). All rotations and reflections preserve the central blob.

**K = 2 (axis-aligned twin, e.g., left/right halves)**: minimizer breaks rotation but preserves one reflection (say horizontal axis reflection). $\mathrm{Aut}(G)_{[\mathbf{u}^*(2)]} = \mathbb{Z}_2$ (order 2). Note: the formation-permutation $S_2$ swap of the two formations *is identified* with the reflection, by the joint quotient.

**K = 4 (quadrant-localized)**: each formation in one quadrant. The graph automorphism $D_4$ acts by **permuting formations**; the joint $\mathrm{Aut}(G) \times S_4$ orbit collapses the stabilizer to **trivial** (order 1). Specifically: $D_4$ acts on quadrants $\{1,2,3,4\}$ as a transitive subgroup of $S_4$; the joint action $(D_4 \times S_4)$ on the K=4 configuration has trivial stabilizer modulo this identification.

| K_act | $\mathrm{Aut}(G)_{[\mathbf{u}^*]}$ | Order | Rank by symmetry-broken |
|---|---|---|---|
| 1 | $D_4$ | 8 | 3 (most symmetric) |
| 2 | $\mathbb{Z}_2$ | 2 | 2 |
| 4 | $\{e\}$ | 1 | 1 (most symmetry-broken) |

**Candidate (c) prediction**: $K_{\mathrm{act}}^{(c)} = 4$.

### §6.4 Falsifiability on R23 90-run

The R23 90-run dataset (`scripts/sigma_class_count_R23.py`) gives the empirical $K_{\mathrm{act}}$ distribution under three IC modes (random / adaptive / structured). If the **adaptive-IC modal** $K_{\mathrm{act}}$ is 4, candidate (c) advances to Cat B. If the modal is 1 (matching T-Merge static), candidate (c) is falsified — but then CN15 also implies the protocol is in the energy-minimization-dominant regime, suggesting candidate (a) at $T \approx 0$.

NQ-302 (W6+) executes this verification.

### §6.5 Stabilizer dimension vs order

For continuous symmetry groups (e.g., translation-invariant graphs per V5b-T canonical), the order is infinite; replace order with Lie-algebra dimension. SCC default graphs are finite, so order suffices. (For 1D cycle / 2D torus extensions, see Bridge B-2 §3.)

---

## §7. Connection to N-1 (Canonical Soft-Hard Switching)

N-1 Soft-Hard Switching Asymmetry (`working/open_problems_reframing_2026-04-19.md` §8) is the canonical-adjacent "single-source" mechanism unifying F-1, M-1, MO-1, OP-0004, OP-0005, OP-0006, P-A, P-D, P-G. The P-F flag is its switching variable.

### §7.1 N-1 already provides partial K-selection

Per `K_status_commitment.md` §2.5 inventory Use 5 (N-1 commitment to integer K), N-1 implies:
- P-F flag OFF: minimization regime → $K_{\mathrm{act}} = K^*_{\mathrm{static}} = 1$.
- P-F flag ON: protocol regime → $K_{\mathrm{act}}$ underdetermined (current state of OP-0005).

N-1 *frames* the dichotomy but does not *resolve* the underdetermined branch.

### §7.2 Extension paths

Each candidate §3.1–§3.3 extends N-1 differently:

- **Candidate (a) (Free-energy)**: P-F flag ON regime parametrized by effective temperature $T$; $K_{\mathrm{act}}^{(a)}$ determined by $\arg\min F(K; T)$.
- **Candidate (b) (Kinetic)**: P-F flag ON regime parametrized by horizon $t_{\mathrm{horizon}}$ and IC distribution; $K_{\mathrm{act}}^{(b)}$ determined by accessible Kramers basins.
- **Candidate (c) (Symmetry)**: P-F flag ON regime determined by genericity; $K_{\mathrm{act}}^{(c)}$ deterministic-given-graph (no IC dependence).

Candidates (a) and (b) are protocol-dependent (CN15-compatible: protocol-endpoint observable). Candidate (c) is protocol-*independent* (graph-invariant prediction). The three give different falsifiable signatures on R23.

---

## §8. Bayesian K-Detection (Statistical Framework)

A complementary candidate framework: given an *observed* cohesion-field outcome $u_{\mathrm{obs}}$, infer $K_{\mathrm{act}}$ via Bayesian posterior:
$$P(K \mid u_{\mathrm{obs}}, G, \mathrm{prior}) \propto P(u_{\mathrm{obs}} \mid K, G) \cdot P(K \mid \mathrm{prior})$$

with BIC penalty (Schwarz 1978):
$$\mathrm{BIC}(K) = -2 \log P(u_{\mathrm{obs}} \mid K, G; \hat\theta_K) + k(K) \log n$$

where $k(K)$ is the parameter count for the K-field model and $n = |V|$.

**Cat target**: B (with structural parameter) — provided a specific likelihood model $P(u_{\mathrm{obs}} \mid K, G)$ is adopted. Natural choice: Gibbs measure $P(u \mid K, G) \propto \exp(-\beta \mathcal{E}_K(u))$ for a thermal SCC extension.

**SCC ontological caveat**: Bayesian K-detection is **inverse**: it answers "given $u_{\mathrm{obs}}$, what K?" — this is *diagnostic* (Commitment 11 derived-construct), not *generative*. It does not select K_act for protocol prediction; it post-hoc identifies K_act from observation. So it complements but does not replace candidates §3.1–§3.3.

**Cat C → B promotion gate**: requires a thermal-SCC layer (P-F flag ON quantification; ties to candidate (a)).

NQ-303 (W6+) explores the Bayesian framework.

---

## §9. Compatibility Audit — Each Candidate vs Canonical Commitments

| Commitment / Constraint | Candidate (a) Free-energy | Candidate (b) Kinetic | Candidate (c) Symmetry |
|---|---|---|---|
| **Commitment 1** (u_t primitive) | ✓ preserved | ✓ preserved | ✓ preserved |
| **Commitment 11** (crisp derivative) | ✓ K_act derived from K-min argmin | ✓ K_act derived from basin | ✓ K_act derived from stabilizer order |
| **Commitment 14** (σ-signature) | ✓ uses σ-class count | ✓ orthogonal | ✓ refines via $\mathrm{Aut}(G)_{u^*}$-irrep |
| **Commitment 16** (K_field/K_act) | ✓ selects K_act ≤ K_field | ✓ K_act emerges via Kramers | ✓ K_act selected by stabilizer comparison |
| **CN5** (4-energy independence) | ✓ no merge | ✓ no merge | ✓ no merge |
| **CN6** (K kinetically determined) | ⚠️ entropic ≠ pure kinetic; reframe needed | ✓ direct match | ⚠️ symmetry ≠ kinetic; complementary |
| **CN10** (contrastive vs reductive) | ✓ Bayesian/AIC contrastive only | ✓ Kramers contrastive only | ✓ SSB/genericity contrastive only |
| **CN15** (Static/Dynamic Separation) | ✓ T>0 endpoint ≠ static | ✓ horizon-dependent endpoint | ⚠️ deterministic — risk of static-endpoint identification |
| **OP-0005 silent-resolution constraint** | ✓ Cat C only | ✓ Cat C only | ✓ Cat C only |

**All three candidates preserve Commitment 16** (since they only constrain K_act selection within K_field bound). **CN15 risk** for candidate (c): if symmetry-broken K_act is independent of protocol, it might be confused with a static prediction; mitigation — frame candidate (c) as *generic-IC asymptotic* rather than *static*. **CN6 reframe** for candidate (a): "kinetic" must be read as "non-static, includes thermal/entropic dynamics" — not pure gradient-flow kinetic. This is consistent with N-1 P-F flag framing.

No candidate forces a canonical edit. All three are W6+ working-level candidates pending empirical anchor.

---

## §10. Empirical Verification Plan — R23 90-Run Dataset

The R23 90-run dataset (W4 04-23, c=0.5, β=30, 32×32 free-BC D₄, 3 IC modes × 30 runs) is the canonical multi-formation empirical anchor. Each of (a)/(b)/(c) makes a falsifiable prediction:

### §10.1 Candidate-specific test design

| Candidate | Predicted modal $K_{\mathrm{act}}$ | Test |
|---|---|---|
| (a) Free-energy at $T=0$ | 1 | Match adaptive-IC modal? |
| (a) Free-energy at $T = T_c^{\mathrm{est}}$ | $K^*(T_c)$ | $T_c$ from §5.2 formula; compare adaptive-IC distribution shape |
| (b) Kinetic | IC-distribution dependent | Per-IC-mode horizon scan; check basin-crossing rates |
| (c) Symmetry | 4 | Match adaptive-IC modal? |

### §10.2 Data products needed

Existing: `scripts/sigma_class_count_R23.py` + `results/sigma_class_count_R23.json` give 56 distinct minimizers and σ-class enumeration. **Missing**:

1. Per-K_act-stratum $E^*(K)$ values (subset of existing minimizers, organized by K_act).
2. $|\Omega_K|$ = σ-class count per K_act stratum (computable from existing JSON).
3. Per-IC-mode $K_{\mathrm{act}}$ histogram (was the dataset organized by IC mode? verify in scripts/results/).
4. $\mathrm{Aut}(G)_{[\mathbf{u}^*]}$ per minimizer (NEW computation — graph-automorphism stabilizer).
5. Per-IC-mode horizon-dependent K_act trajectory (for kinetic candidate (b)).

### §10.3 Acceptance criteria

A candidate is **promoted to Cat B** if its predicted modal K_act matches the empirical adaptive-IC modal at p < 0.05 (chi-squared on 30-run histogram). Otherwise the candidate stays Cat C with refinement notes.

If multiple candidates pass: this is *acceptable* — the candidates are not mutually exclusive (free-energy + symmetry could both contribute; kinetic governs transient).

If none passes: OP-0005 stays HIGH OPEN, and a fourth candidate must be sought (OP-0005 W7+).

### §10.4 Promotion budget

If candidate (c) — the most novel — passes, it earns:
- Cat C → Cat B: empirical anchor on R23 modal match.
- New definitional entry: "$\mathrm{Aut}(G)_{u^*}$ stabilizer" — cross-references Bridge B-2 / B-3.
- Reframes OP-0005 as "K-Selection mechanism: symmetry-broken stabilizer minimization (verified on R23, conjectured general)".

Promotion path: working file (this) → CV-1.7 ontological packet (Wave 4 +6 weeks) → canonical entry pending Critic + 7-agent review.

---

## §11. W6+ Priority Summary

Three new NQ items registered:

| NQ | Candidate | Cat target | Effort | W-band | Priority |
|---|---|---|---|---|---|
| **NQ-301** | (a) Free-energy K-selection numerical | B | ~3 weeks | W6 Day 7 – W7 Day 14 | **HIGH** |
| **NQ-302** | (c) Symmetry-broken K-selection numerical | B | ~2 weeks | W6 Day 7 – W7 Day 7 | **HIGH** |
| **NQ-303** | (b)+(refactor) Bayesian K-detection statistical | C | ~4 weeks | W7 Day 1 – W8 Day 7 | MEDIUM |

### §11.1 NQ-301 (Free-energy)

- Compute $E^*(K)$ and $|\Omega_K|$ from existing R23 56-minimizer data; estimate $T_c$.
- Run `scc/multi.py` with synthetic-noise injection at $T \in \{0, 0.5 T_c^{\mathrm{est}}, T_c^{\mathrm{est}}, 2 T_c^{\mathrm{est}}\}$; check K_act crossover.
- Deliverable: `working/MF/k_selection_free_energy.md` (Wave 4) + numerical results.

### §11.2 NQ-302 (Symmetry)

- Compute $\mathrm{Aut}(G)_{[\mathbf{u}^*]}$ for all 56 R23 minimizers via SageMath / NetworkX `is_isomorphic` automorphism.
- Group minimizers by stabilizer order; verify stabilizer-1 minimizers are predominantly $K_{\mathrm{act}} = 4$.
- Match against adaptive-IC modal in 90-run dataset.
- Deliverable: `working/MF/k_selection_symmetry.md` (Wave 4) + automorphism table.

### §11.3 NQ-303 (Bayesian)

- Specify Gibbs likelihood $P(u | K, G; \beta) \propto \exp(-\beta \mathcal{E}_K)$.
- Compute BIC per K on R23 minimizers; identify K minimizing BIC.
- Compare with chi-squared on adaptive-IC histogram.
- Deliverable: `working/MF/k_selection_bayesian.md` (Wave 4 W8+) + BIC table.

### §11.4 Critic gate

Wave 4 NQ-301..303 packet must pass Critic + 7-agent review before any candidate is promoted toward CV-1.7. Specifically: verify Commitment 16 preservation, CN10 contrastive-only language, no silent resolution of OP-0005.

---

## §12. Hard Constraint Verification

- [x] **u_t primitive maintained** — All three candidates derive K_act from u via post-hoc selection (energy comparison / basin assignment / stabilizer computation). u_t remains the sole primitive.
- [x] **CN10 contrastive throughout** — §3.1 Bayesian/AIC parallels are contrastive only; §3.2 Kramers parallel is contrastive only; §3.3 SSB/genericity parallel is contrastive only; §4 AC analog is explicitly contrastive only.
- [x] **CN5 4-energy not merged** — No candidate touches energy-term structure. Candidate (a) introduces a thermal layer above $\mathcal{E}$, not within it.
- [x] **OP-0005 not silently resolved** — All three candidates are explicitly Cat C target (none promoted). OP-0005 stays HIGH OPEN. Promotion requires NQ-301..303 empirical verification + Critic + 7-agent review.
- [x] **Commitment 16 preserved** — All candidates respect K_field/K_act decomposition (constrain only K_act selection within K_field bound).
- [x] **CN15 Static/Dynamic Separation respected** — Candidates (a) and (b) operate in dynamic-protocol regime; candidate (c) carries a CN15 risk note (§9 mitigation: frame as generic-IC asymptotic, not static).
- [x] **No canonical edits proposed** — This file is `working/MF/`, not canonical/. Any promotion path runs through CV-1.7+ packet review.
- [x] **No Research OS resurrection** — Single-topic working file per `working/README.md` convention. No D-/S-/T-/A-/E-/Q-/C-/P-/X- registry. No 5-role daily logs. No numbered subdirs.
- [x] **Closure not assumed idempotent** — N/A to K-selection.
- [x] **No reductive equation to external framework** — Each candidate has explicit "SCC is not [external framework]" tag in §3.

---

## §13. References

### §13.1 Canonical (verified entries)

- **OP-0005 K-Selection Mechanism**: `THEORY/canonical/open_problems.md` §286–§309 (HIGH severity, OPEN, last reviewed 2026-04-17 phase 4 evidence-boundary alignment note).
- **Commitment 16 (K_field/K_act decomposition)**: `THEORY/canonical/canonical.md` §11.1 #16 line 812 (CV-1.5.1, 2026-04-29).
- **CN6 (K kinetically determined, refined)**: `canonical.md` §14 line 1605 (refined per Commitment 16, CV-1.5.1).
- **CN10 (contrastive vs reductive)**: `canonical.md` §14 line 1546.
- **CN15 (Static/Dynamic Separation Principle)**: `canonical.md` §14 line 1627 (W4 added 2026-04-25).
- **T-Merge (b)** Cat A: `canonical.md` §13 (single-field static minimum K=1).
- **T-PreObj-1G** Cat A: `canonical.md` §13 (graph-class-independent pre-objective mechanism, W4 04-24).
- **T-σ-Lemma-1/2/3 + T-σ-Theorem-3/4**: `canonical.md` §13 (σ-framework supporting structures, W5 Day 1 G0).
- **T-Persist-K-Unified** Cat C: `canonical.md` §13 (multi-formation persistence on smooth segment).
- **Commitment 14-Multi (D-6a)** Cat A: `canonical.md` §11.1 (D-6a Multi-Static, CV-1.5.1).

### §13.2 Working (this Wave 3 / OAT track)

- `K_status_commitment.md` (OAT-1, W5 Day 3 EOD): Commitment 16 origin and 5-use inventory.
- `foundational_bridges_2026.md` §8 Bridge B-7: AC analog source for §4.
- `pre_objective_K_field_tension.md` (OAT-6): pre-objective ↔ K-field tension framing.
- `multi_formation_sigma.md` (D-6a): static σ-framework, Definition 5.1(c) multi-set treatment.
- `sigma_multi_trajectory.md` §2: K-jump definition (Definition 2.2).
- `mathematical_scaffolding_4tools.md`: Tool A2 quotient picture; Tool A3 PH framework.
- `lambda_rep_ontology.md` (OAT-3): λ_rep ontological status.
- `cobelonging_vs_sigmaD.md` (OAT-5): C_t multi-formation status.
- `working/open_problems_reframing_2026-04-19.md` §8: N-1 Soft-Hard Switching Asymmetry; P-F flag.

### §13.3 External (CN10 contrastive only)

- **Schwarz, G. (1978).** *Estimating the dimension of a model.* Annals of Statistics 6(2), 461–464. (BIC; Candidate (a) parallel.)
- **Akaike, H. (1974).** *A new look at the statistical model identification.* IEEE TAC 19(6), 716–723. (AIC; Candidate (a) parallel.)
- **Kramers, H. A. (1940).** *Brownian motion in a field of force and the diffusion model of chemical reactions.* Physica 7(4), 284–304. (Candidate (b).)
- **Hänggi, P., Talkner, P., Borkovec, M. (1990).** *Reaction-rate theory: fifty years after Kramers.* Rev. Mod. Phys. 62(2), 251–341. (Candidate (b) review.)
- **Eyring, H. (1935).** *The activated complex in chemical reactions.* J. Chem. Phys. 3(2), 107–115. (Candidate (b) transition state theory.)
- **Goldstone, J. (1961).** *Field theories with superconductor solutions.* Nuovo Cimento 19, 154–164. (Candidate (c) SSB philosophy.)
- **Anderson, P. W. (1963).** *Plasmons, gauge invariance, and mass.* Phys. Rev. 130(1), 439–442. (Candidate (c) SSB.)
- **Chossat, P., Lauterbach, R. (1994).** *Methods in equivariant bifurcations and dynamical systems.* (Candidate (c) equivariant bifurcation.)
- **Quanta Magazine (2026-04).** Axiom of Choice retrospective. (§4 AC analog; Bridge B-7 source — `foundational_bridges_2026.md` §8.)

### §13.4 Pending verification

None directly cited in this file. (Bridge B-7 source verification handled in `foundational_bridges_2026.md` §12.1.)

---

## §14. Self-Audit (per `working/` convention)

### §14.1 What this file is

- A **theory-only deepening file** directly attacking OP-0005.
- A **3-candidate proposal** with empirical-verification plan (R23 90-run).
- A **single-topic working file** per `working/README.md` convention (W5 Day 4 PM Wave 3).
- A **W6+ NQ packet** (NQ-301/302/303) framework.

### §14.2 What this file is NOT

- Not a numerical experiment (no compute; references existing `scripts/sigma_class_count_R23.py` data).
- Not a canonical edit (no `THEORY/canonical/` modifications).
- Not a new theorem (all three candidates are Cat C definitional / mechanistic).
- Not a silent resolution of OP-0005 (OP-0005 stays HIGH OPEN; promotion gated on NQ-301..303 verification + Critic + 7-agent review).
- Not a resolution of OP-0008 σ^A K-jump non-determinism (separate problem; Commitment 16 frames; this file extends only K_act selection mechanism).
- Not a replacement for Commitment 16 (this file builds on, does not supersede).

### §14.3 Promotion path

```
this file (working/MF/k_selection_mechanism.md, W5 Day 4 PM Wave 3 spawn)
  ↓ NQ-301/302/303 W6+ numerical work
  ↓ verification on R23 90-run modal match
  ↓ Critic + 7-agent review
  ↓ Wave 4 packet integration
  ↓ user-decision at CV-1.7 (W12+)
canonical/canonical.md §11.1 + §13 + §14 + open_problems.md OP-0005 update
```

If verified, OP-0005 status update: HIGH OPEN → PARTIALLY RESOLVED (Cat B candidate anchored).
If falsified across all three, OP-0005 stays HIGH OPEN; W7+ search for fourth candidate.

### §14.4 Estimated read time

~12–15 minutes for full file. ~5 minutes for §1 (Mission), §3 (Three candidates), §10 (Empirical plan), §11 (W6+ priorities) only.

---

**End of k_selection_mechanism.md (W5 Day 4 PM Wave 3 deliverable).**

**Status:** working draft, theory-only deepening file. **Recommendation:** ACCEPT as W6+ NQ-301/302/303 framework; preserve OP-0005 HIGH OPEN until verification. **Effort:** ~3–4 weeks numerical (NQ-302 first, NQ-301 second, NQ-303 third). **Net effect:** OP-0005 transformed from "no candidate mechanism" to "three explicit Cat C candidates with R23 falsifiability plan"; one (candidate (c) symmetry-broken stabilizer) is genuinely new and graph-theoretic. **Carries:** OP-0005 selection-mechanism scaffolding (HIGH); cross-references Commitment 16 (CV-1.5.1), CN15 (W4 04-23), N-1 (working W4 04-19), Bridge B-7 (Wave 3, `foundational_bridges_2026.md` §8 AC analog).

**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/MF/k_selection_mechanism.md`
**Created:** 2026-04-30 W5 Day 4 PM Wave 3 (post-Commitment-16, post-Bridge-B-7).
**Lines:** ~370
**Promotion target:** CV-1.7 (W12+) pending Wave 4 NQ-301..303 verification.
