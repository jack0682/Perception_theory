---
id: SCC-CT-CH-II-III
type: canonical/axioms-primitives
chapter: II + III
version: SCC-CT v0.1
sealed: 2026-05-14
---

> [!nav] Linked: [[MOC_SCC_CT_v0.1]] · [[THEORY_INDEX]]


# II. Primitive Structure & III. Operator Triad

# II. Primitive Structure

## §1. The formal universe

The formal universe of SCC-CT is the structured tuple:

$$\mathfrak{C}^{\mathrm{soft}} \;=\; \Big( T,\; \{X_t\}_{t \in T},\; \{u_t\}_{t \in T},\; \{\mathrm{Cl}_t\}_{t \in T},\; \{\mathbf{N}_t,\, \mathbf{C}_t,\, \mathbf{D}_t\}_{t \in T},\; \{\mathbf{M}_{t \to s}\}_{t, s \in T} \Big)$$

Components:

| Component | Type | Role |
|---|---|---|
| $T$ | linearly ordered index set | temporal indices (discrete or continuous) |
| $X_t$ | set | relational support at time $t$ |
| $u_t$ | $X_t \to [0,1]$ | **soft cohesion field — the canonical primitive** |
| $\mathrm{Cl}_t$ | $[0,1]^{X_t} \to [0,1]^{X_t}$ | self-completion operator |
| $\mathbf{N}_t$ | symmetric kernel on $X_t \times X_t$ | adjacency / soft neighborhood |
| $\mathbf{C}_t$ | derived operator (resolvent) | self-integration / co-belonging |
| $\mathbf{D}_t$ | $u \mapsto $ field on $X_t$ | self-contrast / distinction |
| $\mathbf{M}_{t \to s}$ | unbalanced OT plan | temporal transport (kernel form) |

**Demoted from primitive (historical, preserved as derived diagnostics):**

- **Transition operator $\mathbf{T}_t$** — demoted v2.0 (zero realizations, zero theorems, zero predicate roles); now served by gradient indicator $g_t$, boundary band $\mathrm{Bd}_t$, and morphological quality $\mathcal{Q}_{\mathrm{morph}}$.
- **Co-belonging $\mathbf{C}_t$** — demoted v2.0 cycle 2 (after Sep predicate corrected to $u$-weighted); resolvent realization preserved as derived diagnostic.

## §2. Five axiomatic groups

The primitive structure is constrained by five axiom groups (per `canonical.md §6`):

| Group | Subject | Axioms |
|---|---|---|
| **A** | Closure | A1′, A2, A3, A4 |
| **B** | Adjacency | B1, B2, B3, B4 |
| **C** | Co-belonging | C1, C2, C3″, C4, C5 |
| **D** | Distinction | D1, D2, D3, D4 |
| **E** | Transport | E1, E2, E3, E4 |

### §2.1 Group A — Closure

| Axiom | Statement |
|---|---|
| **A1′** | *Conditional Extensivity.* $\mathrm{Cl}_t(u)(x) \geq u(x)$ holds when $u(x) \leq c^*$ for some self-support threshold $c^*$. For $u(x) > c^*$, closure may act as relaxation. (A1′ replaces the original A1 which conflicted with A3 contraction; see Cat R in `06_forbidden_claims.md`.) |
| **A2** | *Monotonicity.* If $u \leq v$ pointwise, then $\mathrm{Cl}_t(u) \leq \mathrm{Cl}_t(v)$ pointwise. |
| **A3** | *Contraction.* The closure operator is a strict contraction with rate $a_{\mathrm{cl}} < 4$ in the canonical sigmoid realization. This ensures Cauchy convergence of iterates. |
| **A4** | *Continuity.* $\mathrm{Cl}_t$ is continuous (Lipschitz) in $u$. |

### §2.2 Group B — Adjacency

| Axiom | Statement |
|---|---|
| **B1** | *Non-negativity.* $\mathbf{N}_t(x,y) \geq 0$ for all $x, y \in X_t$. |
| **B2** | *Symmetry.* $\mathbf{N}_t(x,y) = \mathbf{N}_t(y,x)$. |
| **B3** | *Locality.* $\mathbf{N}_t(x,y) > 0$ only for "near" $x, y$ (typically nonzero on a sparse graph). |
| **B4** | *Non-transitivity.* In the minimal (undirected) case, $\mathbf{N}_t$ is not assumed to be a transitive relation. |

### §2.3 Group C — Co-belonging (derived; canonical realization: resolvent)

| Axiom | Statement |
|---|---|
| **C1** | *Reflexivity.* $\mathbf{C}_t(x,x) > 0$. |
| **C2** | *Symmetry.* $\mathbf{C}_t(x,y) = \mathbf{C}_t(y,x)$ in the symmetric realization. |
| **C3″** | *Local monotonicity (revised).* Via Schur complement; the resolvent form $\mathbf{C}_t = (I - \alpha_C W_{\mathrm{sym}})^{-1}$ satisfies a monotonicity property weaker than transitive Cesàro form. |
| **C4** | *Continuity.* In $u$. |
| **C5** | *Symmetric realization.* Provisional canonical operator: resolvent $(I - \alpha_C W_{\mathrm{sym}})^{-1}$, $\alpha_C \rho(W_{\mathrm{sym}}) < 1$. |

### §2.4 Group D — Distinction

| Axiom | Statement |
|---|---|
| **D1** | *Self-induced exterior.* $\mathbf{D}_t$ evaluates against $1 - u$ as canonical exterior reference. |
| **D2** | *Non-negativity.* $\mathbf{D}_t(x; 1-u) \in [0, 1]$. |
| **D3** | *Asymmetric sensitivity.* $\mathbf{D}_t$ is sensitive to differential between interior and exterior. |
| **D4** | *$b_D = 0$ analyticity.* The distinction operator has $b_D = 0$ (no gradient term) to preserve energy analyticity (required for T14 gradient flow convergence; CN4). |

### §2.5 Group E — Transport

| Axiom | Statement |
|---|---|
| **E1** | *Sub-stochasticity.* $\mathbf{M}_{t \to s}$ has row sums $\leq 1$ (mass loss allowed; unbalanced OT). |
| **E2** | *Non-injectivity.* $\mathbf{M}_{t \to s}$ may merge multiple source sites into one target (or vice versa). |
| **E3** | *Core inheritance.* The core of $u_t$ is mapped to within ε of the core of $u_s$ (solution constraint, not operator axiom; reclassified). |
| **E4** | *Fingerprint cost.* Transport cost depends on the SCC fingerprint $\varphi = (u, \mathrm{Cl}(u), \mathbf{D}(u))$, not on external embeddings. |

### §2.6 Volume constraint

The structural axiom not listed above but enforced at every level:

$$\boxed{\sum_{x \in X_t} u_t(x) \;=\; m}$$

This constrains $u_t$ to the simplex $\Sigma_m = \{u \in [0,1]^n : \mathbf{1}^\top u = m\}$. Without this, the variational problem $\min \mathcal{E}(u)$ admits trivial solutions ($u \equiv 0$). The volume constraint is a structural axiom (not optional), added in v2.0.

## §3. Summation convention (canonical §0)

All sums over $(x, y) \in X_t \times X_t$ are **ordered pairs**. Each undirected edge is counted twice when the kernel is symmetric. Notation:

$$\sum_{x,y \in X_t} \quad := \quad \text{sum over ordered pairs.}$$

Where unordered-pair sums are intended:

$$\sum_{\{x, y\}} \;=\; \frac{1}{2} \sum_{x, y \in X_t} \quad \text{for symmetric } f(x, y).$$

This convention is **load-bearing** in T8-Core (phase transition: factor 4 in $4\lambda_2/\lvert W''(c) \rvert$ ratio, not 2 — see Cat R for the historical 2 vs 4 confusion).

# III. Operator Triad

## §4. Three operators, three modes of self-reference

The canonical core operators are exactly three, corresponding to three modes of self-referential evaluation:

$$\boxed{\mathrm{Cl}_t \;=\; \text{self-completion}}$$

$$\boxed{\mathbf{D}_t \;=\; \text{self-contrast}}$$

$$\boxed{\mathbf{C}_t \;=\; \text{self-integration (derived; resolvent diagnostic)}}$$

The fourth operator-like entity, $\mathbf{M}_{t \to s}$, is **not** in the triad — it acts *between* time slices, not *within* a single $u_t$.

## §5. Canonical realizations

### §5.1 Closure $\mathrm{Cl}_t$ (sigmoid realization)

$$\mathrm{Cl}_t(u)(x) \;=\; \sigma\bigl(a_{\mathrm{cl}} \cdot [(1 - \eta_{\mathrm{cl}}) u(x) + \eta_{\mathrm{cl}} (P_t u)(x) - \tau_{\mathrm{cl}}]\bigr)$$

where:
- $\sigma$ is the logistic sigmoid.
- $a_{\mathrm{cl}} < 4$ is the steepness (A3 contraction).
- $\eta_{\mathrm{cl}} \in [0, 1]$ is the self / neighbor balance.
- $\tau_{\mathrm{cl}}$ is the closure threshold.
- $P_t = D^{-1} \mathbf{N}_t$ is the row-normalized aggregation.

**Critical structural choice — non-idempotent.** $\mathrm{Cl}_t \circ \mathrm{Cl}_t \neq \mathrm{Cl}_t$. Instead, the iteration $u, \mathrm{Cl}(u), \mathrm{Cl}^2(u), \ldots$ converges to a fixed point with strictly positive Hessian (T3 / T6-Stability Cat A). Idempotence would produce zero eigenvalues in the closure direction — a *weaker* stability. Non-idempotence yields *strictly stronger* metastability.

### §5.2 Distinction $\mathbf{D}_t$ (self-induced exterior)

$$\mathbf{D}_t(x; 1 - u) \;=\; \sigma\bigl(a_D \cdot [(P_t u)(x) - \lambda_D (P_t (1 - u))(x)] - \tau_D\bigr)$$

with $b_D = 0$ for analyticity (CN4). Uses the canonical exterior reference $1 - u$, evaluated through the aggregation kernel.

### §5.3 Co-belonging $\mathbf{C}_t$ (resolvent diagnostic)

$$\mathbf{C}_t \;=\; (I - \alpha_C W_{\mathrm{sym}})^{-1} \quad \text{(Neumann series; } \alpha_C \rho(W_{\mathrm{sym}}) < 1)$$

where $W_{\mathrm{sym}}$ is the cohesion-weighted symmetrized adjacency.

**Demoted from primitive to derived diagnostic** in v2.0 cycle 2. The previous Cesàro form did not preserve pairwise structure; resolvent form does, but $\mathbf{C}_t$ no longer enters any predicate or energy. It remains a useful structural readout.

### §5.4 Transport $\mathbf{M}_{t \to s}$ (entropic partial OT kernel)

Canonical form: entropic partial OT plan with cost $c[u_t, u_s]$ (fingerprint similarity cost), regularized by $\varepsilon_{\mathrm{OT}} > 0$. Solved via Sinkhorn iteration; canonical stability via H-SINK Cat A (CV-1.12 / CV-1.13 sealed).

## §6. Operator interactions and structural constraints

| Interaction | Statement |
|---|---|
| **Closure self-fixed-point** | At critical points of $\mathcal{E}_{\mathrm{cl}}$, the closure residual $\mathrm{Cl}(u^*) - u^*$ is "small" but generally non-zero. At canonical interior minimizers, the residual is concentrated in the boundary band (saturated nodes have $\sigma'(z) \to 0$). |
| **Distinction self-reference** | $\mathbf{D}_t$ uses $1 - u$ as exterior; this self-induced exterior makes the distinction operator entirely intrinsic. |
| **Co-belonging Jacobian role** | The closure Jacobian $J_{\mathrm{Cl}} = \mathrm{diag}(\sigma' a_{\mathrm{cl}}) \cdot M$ with $M = (1-\eta_{\mathrm{cl}})I + \eta_{\mathrm{cl}} P$ governs both energy gradient and Hessian. Via the degree-weighted operator norm (L-CLOSURE-LIFT Cat A CV-1.16), $\lVert J_{\mathrm{Cl}} \rVert_{D \to D} \leq a_{\mathrm{cl}}/4 < 1$. |
| **Transport vs static** | $\mathbf{M}_{t \to s}$ is the *only* operator linking distinct time slices. Static structure ($\mathrm{Cl}, \mathbf{D}, \mathbf{C}$) acts within a single $u_t$; dynamic structure acts between $u_t$ and $u_s$. |

## §7. Why exactly three operators in the triad

The three modes (completion, contrast, integration) are *the* three independent modes of self-evaluation a cohesion field can have:

- **Completion** — does $u$ agree with its own self-induced aggregate?
- **Contrast** — does $u$ differ from its self-induced exterior $1 - u$?
- **Integration** — does $u$ acknowledge its global relational embedding (via resolvent / Neumann series)?

A fourth independent mode is not known, and historical attempts to introduce one (e.g., transition operator $\mathbf{T}_t$) have collapsed into derived diagnostics. SCC-CT therefore commits to *three* as the operator count, recognizing this as a non-trivial ontological claim.

## §8. Forbidden operator constructions

The following operator-level constructions are explicitly excluded from SCC-CT primitives (registered in `06_forbidden_claims.md`):

- **Idempotent closure** (would weaken stability — Cat R).
- **Symmetric transport** $\mathbf{M}_{t \to s} = \mathbf{M}_{s \to t}^\top$ as default (transport may be asymmetric; the temporal arrow matters).
- **Linear transition operator** $\mathbf{T}_t$ (demoted v2.0 — Cat R historical).
- **Cesàro co-belonging** (does not preserve pairwise structure — Cat R).
- **External label-based distinction** (would re-introduce object primitive — violates §I).

---

*Chapters II & III sealed within SCC-CT v0.1. References: `THEORY/canonical/canonical.md` §3 (Formal Universe), §6 (Axiomatic Groups A–E), §9 (Operators), §14 CN1/CN2/CN3/CN4. Next: `03_energy_and_diagnostics.md` (Ch. IV Diagnostic Vector + Ch. V Energy Principle).*
