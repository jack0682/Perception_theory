---
id: SCC-CT-CH-IV-V
type: canonical/energy-diagnostics
chapter: IV + V
version: SCC-CT v0.1
sealed: 2026-05-14
---

> [!nav] Linked: [[MOC_SCC_CT_v0.1]] · [[THEORY_INDEX]]


# IV. Diagnostic Vector & V. Energy Principle

# IV. Diagnostic Vector

## §1. The four-component diagnostic

The canonical formation-quality diagnostic is a 4-component vector in $[0, 1]^4$:

$$\boxed{\mathbf{d}(u) \;=\; (\mathsf{Bind},\;\mathsf{Sep},\;\mathsf{Inside},\;\mathsf{Persist}) \;\in\; [0, 1]^4}$$

**This diagnostic replaces the historical single-Pragnanz scalar.** A scalar quality measure cannot distinguish formations that differ in (e.g.) binding-without-separation from separation-without-binding. The 4-vector preserves these distinctions.

## §2. Component definitions and roles

| Component | Meaning | Canonical formula | Ontological role |
|---|---|---|---|
| **$\mathsf{Bind}$** | self-support / closure fidelity | $\mathsf{Bind}(u) = 1 - \tfrac{\|u - \mathrm{Cl}(u)\|}{\sqrt{n}}$ | Does the formation support itself under closure? |
| **$\mathsf{Sep}$** | exterior contrast | $\mathsf{Sep}(u) = 1 - \mathcal{E}_{\mathrm{sep}}(u) / m$ (exact $u$-weighted; CN5 bridge) | Is the formation distinguishable from its self-induced exterior? |
| **$\mathsf{Inside}$** | morphological articulation | $\mathsf{Inside}(u) = \mathcal{Q}_{\mathrm{morph}}(u)$ normalized form | Does the formation have core-boundary-exterior morphology? |
| **$\mathsf{Persist}$** | temporal inheritance | $\mathsf{Persist}(u_t, u_s) = $ core-overlap via $\mathbf{M}_{t \to s}$ | Does the formation's structure carry across time? |

## §3. Predicate-Energy Bridge (Cat A)

Two of the four components are tied to specific energy terms by **exact bridges** (registered Cat A in `THEORY/canonical/canonical.md` §13):

### §3.1 Sep — exact $u$-weighted bridge

$$\mathsf{Sep}(u) \;=\; 1 - \frac{\mathcal{E}_{\mathrm{sep}}(u)}{m} \quad \text{(exact bidirectional equality)}$$

This is registered as **Predicate-Energy Bridge** Cat A. Sep is computable directly from $\mathcal{E}_{\mathrm{sep}}$ via the $u$-weighted form $\mathsf{Sep} = \sum_x u(x) \mathbf{D}(x; 1-u) / m$.

Historical note: an earlier $\mathbf{C}_t$-weighted form was diagnostically degenerate (Sep ≈ 0.5 regardless of formation quality). Corrected to $u$-weighted form in v2.0; the $\mathbf{C}_t$-weighted form is Cat R (`06_forbidden_claims.md`).

### §3.2 Bind — directional bridge with KKT reversal at minimizers

$$\mathsf{Bind}(u) \;\geq\; 1 - \sqrt{\frac{\mathcal{E}_{\mathrm{cl}}(u)}{n}}$$

is unconditional (Cat A forward direction). At KKT-optimal $u^*$, this becomes an *equality up to first-order conditions* (Cat A reverse direction at minimizers, via T-Bind-Proj / T-Bind-Full).

## §4. Inside (morphological quality)

$$\mathsf{Inside}(u) \;=\; \frac{\ell_{\max}(u) - c}{1 - c} \cdot \mathrm{Artic}(u) \quad \text{(normalized form; QM1 axiom-satisfying)}$$

The normalization removes the bug of the historical $\ell_{\max} \cdot \mathrm{Artic}$ form (non-zero on uniform fields). The current form vanishes at $u \equiv c$ and increases monotonically as the formation acquires articulated structure.

T-OP6-B (canonical Cat A conditional, §5.3b) gives a sharper geometric bound: the Hausdorff distance between the boundary band and the persistent ridge is $d_H \leq 2\sqrt{\alpha/\beta}$ under hypotheses H1–H5.

## §5. Persist (temporal inheritance)

Two canonical formulations (both Cat A as of CV-1.13):

### §5.1 Core-overlap (single-formation, K=1 case)

For consecutive time slices $u_t, u_s$ with persistent components $C_t, C_s$:

$$\mathsf{Persist}_{\mathrm{core}}(u_t, u_s) \;=\; \frac{|C_t \cap C_s|}{|C_t \cup C_s|} \cdot \text{(transport-weighted)}$$

### §5.2 Component-level correspondence (multi-formation, T-Temporal-Identity)

For $u_t, u_s$ with $K_t = K_s$ persistent components and admissible plan $\mathbf{M}_{t \to s}$:

$$R_{t \to s} \subseteq \mathrm{PersComp}(u_t) \times \mathrm{PersComp}(u_s)$$

a well-defined component-level correspondence relation. Five event types are exhausted: continuation (1-to-1), split (1-to-many), merge (many-to-1), birth, death. Under stable-K + margin condition $\Delta_{\mathrm{sep}} \geq \Delta_{\mathrm{sep}}^* + 2\epsilon_{\mathrm{kernel}}$, $R_{t \to s}$ is a unique bijection.

This is **T-Temporal-Identity (a, b, c, d)** Cat A (CV-1.13 SEALED, all four parts).

## §6. Why the diagnostic is a *vector*, not a scalar

The four components capture four independent failure modes:

| Failure mode | Diagnostic signature |
|---|---|
| Closure failure (formation doesn't self-support) | low $\mathsf{Bind}$ |
| Exterior failure (formation indistinguishable from background) | low $\mathsf{Sep}$ |
| Morphology failure (formation is uniform blob without articulation) | low $\mathsf{Inside}$ |
| Temporal failure (formation doesn't persist across time) | low $\mathsf{Persist}$ |

A single scalar would collapse these into one number, destroying the diagnostic information. The 4-vector is therefore the **minimal sufficient diagnostic** for formation quality.

## §7. Aggregation as application-layer choice

When a single scalar is needed for downstream applications (e.g., ranking formations, deciding object-vs-non-object), the aggregation function is an **application-layer choice**, not a canonical commitment:

- $\min(\mathbf{d})$ — strictest (formation passes only if all four pass).
- $\prod \mathbf{d}$ — multiplicative (any low component drags down the whole).
- weighted sum — application-specific weights.

SCC-CT canonically reports the 4-vector; the application chooses the aggregator.

---

# V. Energy Principle

## §8. The four-term energy

$$\boxed{\mathcal{E}(u) \;=\; \lambda_{\mathrm{cl}} \mathcal{E}_{\mathrm{cl}}(u) \;+\; \lambda_{\mathrm{sep}} \mathcal{E}_{\mathrm{sep}}(u) \;+\; \lambda_{\mathrm{bd}} \mathcal{E}_{\mathrm{bd}}(u) \;+\; \lambda_{\mathrm{tr}} \mathcal{E}_{\mathrm{tr}}(u, \mathbf{M})}$$

defined on the volume-constrained simplex $\Sigma_m = \{u \in [0, 1]^n : \mathbf{1}^\top u = m\}$.

## §9. Term-by-term canonical forms

### §9.1 Closure energy

$$\mathcal{E}_{\mathrm{cl}}(u) \;=\; \|u - \mathrm{Cl}(u)\|^2 \;=\; \sum_x (u(x) - \mathrm{Cl}(u)(x))^2$$

Measures deviation from closure fixed-point. Vanishes only at $u = \mathrm{Cl}(u)$ (fixed-point condition).

### §9.2 Separation energy ($u$-weighted form)

$$\mathcal{E}_{\mathrm{sep}}(u) \;=\; \sum_x u(x) \cdot (1 - \mathbf{D}(x; 1 - u))$$

Low when high-$u$ regions are distinguished from their self-induced exterior. Bridged to $\mathsf{Sep}$ predicate (Cat A, §3.1).

### §9.3 Boundary / morphology energy (Allen-Cahn type)

$$\mathcal{E}_{\mathrm{bd}}(u) \;=\; \alpha \sum_{x, y \in X} \mathbf{N}(x, y) (u(x) - u(y))^2 \;+\; \beta \sum_x W(u(x))$$

with $W(u) = u^2 (1 - u)^2$ double-well potential, $W''(u) = 2(1 - 6u + 6u^2)$.

By ordered-pair summation convention (§II.3):

$$\mathcal{E}_{\mathrm{bd}}(u) \;=\; 2\alpha \cdot u^\top L u \;+\; \beta \sum_x W(u(x))$$

with $L = D - \mathbf{N}$ the graph Laplacian.

### §9.4 Transport energy

$$\mathcal{E}_{\mathrm{tr}}(u_t, u_s, \mathbf{M}) \;=\; \langle \mathbf{M},\; c[u_t, u_s] \rangle \;+\; \varepsilon_{\mathrm{OT}} \cdot H(\mathbf{M})$$

with self-referential fingerprint cost $c[u_t, u_s]$, entropic regularization $\varepsilon_{\mathrm{OT}} > 0$, unbalanced partial OT structure (E1-E4).

**CV-1.15 extension.** Action-Based Temporal Succession Package (CV-1.15) provides an alternative *action-cost* formulation $c^{\mathrm{act}}_{i \to k}$ satisfying T-ACT-DP Bellman composition (Cat A); see `THEORY/canonical/canonical.md` §13 CV-1.15 Cat A insert. The action-cost form is *composition-compatible* in a way the standard $c[u_t, u_s]$ is not (Sinkhorn plan semigroup generically fails — T-SINKHORN-PLAN-SEMIGROUP-FAILS Cat R / OPEN warning).

## §10. The 4-term independence commitment (CN5)

The four terms are **conceptually independent**. They correspond to:

| Term | Ontological role | Why independent |
|---|---|---|
| $\mathcal{E}_{\mathrm{cl}}$ | Self-completion | Depends on closure operator $\mathrm{Cl}$ — cannot be derived from boundary structure. |
| $\mathcal{E}_{\mathrm{sep}}$ | Self-contrast | Depends on distinction operator $\mathbf{D}$ — measures interior-vs-exterior asymmetry, not internal connectivity. |
| $\mathcal{E}_{\mathrm{bd}}$ | Self-articulation | Allen-Cahn type smoothness + double-well — the *only* term that directly drives phase separation. |
| $\mathcal{E}_{\mathrm{tr}}$ | Self-continuation | Acts *between* time slices; cannot be defined intrinsically at a single time. |

**Forbidden:** merging any two terms into one. Mathematical correlation is admitted (terms may share gradient directions); ontological merging is forbidden.

## §11. Weighting and normalization

The weights $\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}}$ are not arbitrary. Canonical convention (`CODE/scc/energy.py:EnergyComputer.normalize_weights`):

$$\lambda_i \;=\; \frac{w_i}{\sigma_i + \varepsilon} \quad \text{(Hessian-spectral-norm normalization)}$$

where $\sigma_i$ is the Hessian spectral norm at the uniform reference $u = c \mathbf{1}$. This brings all four terms to a common scale before optimization.

## §12. Critical canonical results

### §12.1 T8-Core (phase transition; Cat A)

$$\boxed{\frac{\beta}{\alpha} \;>\; \frac{4 \lambda_2(L)}{|W''(c)|}}$$

is the necessary-and-sufficient condition for a non-uniform global minimizer of $\mathcal{E}_{\mathrm{bd}}$ to exist on $\Sigma_m$ with volume fraction $c = m/n$.

**Critical clarification (Cat R historical).** The factor "4" is correct under the ordered-pair summation convention (§II.3). An earlier "2" appeared in informal calculations using unordered-pair sums; this is a *notation* error, not a substantive one. Canonical: **4λ₂**.

### §12.2 T14 (gradient flow convergence; Cat A)

Projected gradient flow $\dot{u} = -\Pi_{\Sigma_m} \nabla \mathcal{E}(u)$ converges to a critical point of $\mathcal{E}$ from any initial condition, via Łojasiewicz-Simon inequality. Requires analyticity (CN4 $b_D = 0$).

### §12.3 T11 (Γ-convergence; Cat A)

As $\varepsilon = \alpha/\beta \to 0$, $\mathcal{E}_{\mathrm{bd}}$ Γ-converges to a perimeter functional. The self-referential corrections from $\mathcal{E}_{\mathrm{cl}}$ and $\mathcal{E}_{\mathrm{sep}}$ modify the effective surface tension.

### §12.4 T3 / T6-Stability (non-idempotent closure; Cat A)

At non-idempotent fixed point, $H_{\mathrm{cl}} = 2(I - J_{\mathrm{Cl}})^\top (I - J_{\mathrm{Cl}})$ is *strictly positive definite* (no zero eigenvalues in the closure direction). Idempotence would yield a zero eigenvalue, weakening stability. Non-idempotence is therefore a *positive* structural choice.

### §12.5 L-CLOSURE-LIFT (broadness; Cat A, CV-1.16)

$$\|J_{\mathrm{Cl}}\|_{D \to D} \;\leq\; \frac{a_{\mathrm{cl}}}{4} \;<\; 1$$

in the degree-weighted inner product. Consequence:

$$(I - J_{\mathrm{Cl}})^\top D (I - J_{\mathrm{Cl}}) \;\succeq\; (1 - a_{\mathrm{cl}}/4)^2 D$$

**uniformly** on the tangent space — broadness (not narrow-eigenmode-only). Supersedes T7-Enhanced as the broadness statement; T7-Enhanced canonical Cat A is preserved as historical context.

## §13. Energy on multi-formation

For multi-formation states $\mathbf{u} = (u^{(1)}, \ldots, u^{(K)})$ on the shared-pool simplex $\widetilde{\Sigma}_M^K$, the canonical extension is:

$$\mathcal{E}_{\mathrm{multi}}(\mathbf{u}) \;=\; \sum_{j=1}^K \mathcal{E}(u^{(j)}) \;+\; \lambda_{\mathrm{rep}} \mathcal{R}_{\mathrm{rep}}(\mathbf{u})$$

where $\mathcal{R}_{\mathrm{rep}}$ is a multi-formation repulsion term (its precise form is OPEN — `05_open_problems.md` OP-0009).

T-L1-F (Cat A conditional on hypothesis package (P0)-(P11)) provides the multi-formation **count bridge** $K_{\mathrm{bar}}^{\ell_{\min}} = K_{\mathrm{act}}^\varepsilon$. This is the only multi-formation Cat A available; full multi-formation ontology is open.

## §14. Forbidden energy constructions

The following energy-level constructions are excluded (Cat R `06_forbidden_claims.md`):

- **Merging $\mathcal{E}_{\mathrm{cl}}$ and $\mathcal{E}_{\mathrm{sep}}$** into a single "cohesion" term. Forbidden by CN5.
- **Replacing $\mathcal{E}_{\mathrm{bd}}$ with pure perimeter functional.** Γ-convergence is asymptotic; the finite-$\varepsilon$ regime carries information lost in the perimeter limit.
- **Adding a fifth energy term** without explicit ontological justification (e.g., entropic priors, label-driven costs).
- **External-label distinction** in $\mathcal{E}_{\mathrm{sep}}$ (would re-introduce object primitive).
- **Mountain-pass construction on $\Sigma_M^K$** (Cat R retraction 2026-04-07; merge path does not exist on the proper manifold).

---

*Chapters IV & V sealed within SCC-CT v0.1. References: `THEORY/canonical/canonical.md` §7 (Energy), §8 (Diagnostic Vector), §13 (Cat A theorems on energy and predicates), §14 CN5 (4-term independence). Next: `04_theorem_registry.md` (Ch. VI Static Core Theorems + Ch. VII Computational Validation).*
