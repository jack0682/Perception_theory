> [!nav] Linked: [[MOC_H_MORSE_packageII]] · [[MOC_Q3_stochastic_dynamics]] · [[THEORY_INDEX]]

# 07 — Eyring-Kramers Requirements

Agent E (Package II Mapper). Six EK variants compared against SCC structure; compatibility analysis.

---

## Comparison table

| # | Variant | Domain | Hypotheses | SCC compatible? | Literature |
|---|---------|--------|------------|------------------|------------|
| 1 | Classical overdamped Langevin EK | $\mathbb R^n$ | Smooth Morse $\mathcal E$, confining; $T_* \to 0$ | **No** — SCC domain is bounded polytope, not $\mathbb R^n$ | Bovier-Eckhoff-Gayrard-Klein 2004; Berglund-Gentz 2010 |
| 2 | Manifold-constrained Langevin EK | Smooth Riemannian manifold | Smooth Morse on compact manifold | Partial — SCC manifold is polytope with corners, not smooth | Lelièvre-Rousset-Stoltz 2010 (book); Hsu (book) |
| 3 | Reflected Langevin EK on convex polytope | Convex polytope $\tilde C$ | Smooth Morse on interior; reflection at $\partial \tilde C$ | **Yes** for interior critical points | Bovier-Den Hollander 2015 (book); Bouchet-Reygner 2016 |
| 4 | Finite-state metastable reduction | Discrete state set | Spectral gap separation; metastable mode identification | Possible if SCC reduces to K-sector hierarchy | Bovier-Den Hollander 2015 §10 |
| 5 | Graph-based discrete EK | Graph + transition rates | Discrete master equation | Tangential — SCC is continuous-state, not discrete-state | Various |
| 6 | Custom SCC EK | $\Sigma_m^\circ$ + boundary | TBD | **Required** for full sharp result | none — to be derived |

---

## Detailed analysis per variant

### Variant 1 — Classical (Bovier-Eckhoff-Gayrard-Klein 2004)

**Assumptions:**
- Smooth $\mathcal E : \mathbb R^n \to \mathbb R$ confining ($\mathcal E \to \infty$ at infinity).
- Morse: all critical points nondegenerate.
- $\mathcal E$ has finite set of local minima $\{\mathfrak m_i\}$ and index-1 saddles $\{\mathfrak s_{ij}\}$.
- Sharp $T_* \to 0$ limit.

**Theorem (informal):**
$$k_{\mathfrak m_i \to \mathfrak m_j} = \frac{|\lambda_-(\mathfrak s_{ij})|}{2\pi} \sqrt{\frac{|\det \nabla^2 \mathcal E(\mathfrak s_{ij})|}{\det \nabla^2 \mathcal E(\mathfrak m_i)}}\, e^{-(\mathcal E(\mathfrak s_{ij}) - \mathcal E(\mathfrak m_i))/T_*} (1 + o(1))$$

**SCC compatibility:** SCC dynamics are on bounded $\tilde C$, not $\mathbb R^n$. The confining assumption fails (or is replaced by reflection). Cannot apply directly.

**Status:** Not applicable; framework reference only.

---

### Variant 2 — Manifold-constrained Langevin

**Assumptions:**
- Smooth Riemannian manifold $M$, compact.
- $\mathcal E \in C^\infty(M)$, Morse.
- Langevin generator $L = T_* \Delta_M - \nabla \mathcal E \cdot \nabla$.

**Theorem:** Same form as Variant 1 with Hessians replaced by **manifold Hessians** $\mathrm{Hess}_M \mathcal E$.

**SCC compatibility:**
- The interior $\Sigma_m^\circ$ is a smooth $(n-1)$-manifold ✓
- The closure $\Sigma_m$ is a manifold with corners ✗ (not smooth)
- The induced Riemannian metric on $\Sigma_m^\circ$ from $\mathbb R^n$ is the **Euclidean** metric (canonical convention). T-PF-A1-AR Cat A provides the AR coordinatization $\tilde C \cong \Sigma_m \subset \mathbb R^n$ as a convex polytope.

**Partial compatibility:** Applies on $\Sigma_m^\circ$ if all critical points are strictly interior. Fails at $\partial \Sigma_m$.

**Status:** Useful intermediate; effectively absorbed into Variant 3.

---

### Variant 3 — Reflected Langevin EK on convex polytope (recommended)

**Assumptions (Bovier-Den Hollander style):**
- $\tilde C \subset \mathbb R^n$ bounded convex polytope.
- Reflected SDE: $dX_t = -\nabla \mathcal E(X_t) dt + \sqrt{2T_*} dW_t + dK_t$ with $K_t$ the Skorokhod local-time term enforcing $X_t \in \tilde C$.
- Smooth Morse $\mathcal E$ on **interior** $\tilde C^\circ$.
- Critical points (minima, saddles) all in $\tilde C^\circ$ (no critical points on $\partial \tilde C$).
- $T_* \to 0$ asymptotic regime.

**Theorem:** Same form as Variant 1 (interior critical points behave the same; reflection at boundary contributes only to instanton paths that touch boundary, which are exponentially suppressed if all relevant minima/saddles are interior).

**SCC compatibility:**

| Required | SCC status |
|----------|-----------|
| Convex polytope $\tilde C$ | ✓ T-PF-A1-AR Cat A |
| Reflected SDE well-posed | ✓ T-PF-A1-SDE Cat A (Lions-Sznitman case (ii)) |
| Gibbs invariant | ✓ T-PF-A1-GI Cat A |
| Poincaré ergodicity | ✓ T-PF-A1-PE Cat A |
| Smooth Morse $\mathcal E$ on interior | **OPEN — needs H-MORSE-Local + H-MORSE-Saddle** |
| Interior critical points (no boundary saddles) | conditional on M-A3 strict interiority |
| $T_* \to 0$ regime | **OPEN — OP-0021 registered status** |

**Status:** **Most compatible**; the recommended EK form for SCC. All four Package I gates are satisfied; the missing piece is H-MORSE + OP-0021.

**Literature need:** The reflected-Langevin EK with prefactor for a convex polytope with corners is in **Bouchet-Reygner 2016** (`Generalisation of the Eyring-Kramers transition rate formula to irreversible diffusion processes`) and **Bovier-Den Hollander 2015** (book §10–§11). These are standard references; not yet cited in canonical files. Status: **literature-available, not yet bibliographically integrated** into the SCC canonical.

---

### Variant 4 — Finite-state metastable reduction

**Assumptions:**
- Continuous Markov process with spectral gap structure: $\lambda_2 \gg \lambda_K \gg \lambda_{K+1}$ (clear separation between $K$ metastable modes and the rest).
- Effective dynamics on finite state set $\{\mathfrak m_1, \ldots, \mathfrak m_K\}$ via projection onto the slowest $K-1$ non-trivial eigenmodes.

**Theorem:** Reduced master equation $\dot p_i = \sum_j (k_{ji} p_j - k_{ij} p_i)$ with rates given by Variant 3 formula.

**SCC compatibility:** Compatible if SCC has clear metastable mode hierarchy. T-K-Select-PF + T-K-Select-OBS (Cat B) provide K-sector decomposition; spectral gap separation requires combined H-MORSE + ΔE Cat A bounds.

**Status:** Useful for downstream Q4-DYN; depends on Variant 3 being established.

---

### Variant 5 — Graph-based discrete EK

**Assumptions:**
- Discrete state set with prescribed transition rates.
- Master equation in graph form.

**SCC compatibility:** Tangential. SCC is continuous-state; reduction to discrete graph would happen at the K-sector level, which is Variant 4 territory. Not directly applicable.

**Status:** Not relevant for CV-1.14.

---

### Variant 6 — Custom SCC EK

**Hypothetical content:** A theorem stated in canonical SCC language, with:
- Domain $\Sigma_m$ (or $\widetilde\Sigma_M^{K_\mathrm{field}}$).
- SCC energy decomposition $\mathcal E = \lambda_\mathrm{cl}\mathcal E_\mathrm{cl} + \lambda_\mathrm{sep}\mathcal E_\mathrm{sep} + \lambda_\mathrm{bd}\mathcal E_\mathrm{bd}$.
- Closure-correction Hessian gap as the explicit lower bound on prefactor.
- Bernoulli regularization (consistent with T-P-F-ε0-K).
- D-ST-4 / K-Select notation.

**SCC compatibility:** Maximally compatible — but requires writing the theorem.

**Status:** Long-term canonical target. Most efficient route: prove Variant 3 (reflected EK adapted to SCC) and rename it.

---

## Compatibility summary

| Variant | Status for SCC | What's needed |
|---------|----------------|---------------|
| 1 Classical | Not applicable | — |
| 2 Manifold | Useful intermediate | Absorbed into V3 |
| **3 Reflected polytope** | **Recommended** | H-MORSE + OP-0021 + literature integration |
| 4 Finite-state reduction | Downstream | V3 first |
| 5 Graph-based | Tangential | — |
| 6 Custom SCC | Long-term | V3 + canonical rewrite |

---

## What Package I already covers vs what is needed for EK

**Package I covers** (Cat A):
- Reflected SDE well-posedness ✓
- Gibbs invariant measure ✓
- Poincaré ergodicity (TV convergence) ✓
- Convex polytope structure ✓

**Package II needs additionally:**
- Morse structure of $\mathcal E$ on $\Sigma_m^\circ$ — **H-MORSE OPEN**
- Saddle existence and structure — **OPEN**
- $T_* \to 0$ asymptotic regime — **OP-0021 OPEN** ($T_*$ axiomatic)
- Quantitative ΔE separation — Cat B (T-P-F-ε0-K conditional)
- Freidlin-Wentzell quasipotential — OPEN
- Bovier-Eckhoff-Gayrard prefactor derivation adapted to reflected polytope — **literature available, integration OPEN**

**Verdict:** Package I is **fully sufficient as a dynamics foundation**; the gap is entirely in the static Morse/critical-point structure (H-MORSE) and the parameter $T_*$ (OP-0021). Both gaps are addressed separately from Package I and from each other.

---

## Literature integration status

The repository **does not** yet cite:
- Bovier-Eckhoff-Gayrard-Klein 2004 (classical sharp EK)
- Berglund-Gentz 2010 (review)
- Bovier-Den Hollander 2015 (book, reflected case)
- Bouchet-Reygner 2016 (irreversible / reflected EK)
- Lelièvre-Rousset-Stoltz 2010 (constrained Langevin)
- Friedlin-Wentzell 1998 / 2012 (large deviations book)

These are standard references; the gap is bibliographic only. For CV-1.14, recommend **including bibliographic references** in the H-MORSE-Local working file so future Package II work can build on them without re-discovery.

**Status: literature-needed for the bibliographic integration step (low effort, ~0.25 session).** No new mathematics required at this stage.
