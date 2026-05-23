> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 08 — Pre-Brainstorm: After Temporal Identity, Toward H-MORSE / Package II

Exploratory but disciplined. This file collects candidate routes for CV-1.14 without committing to a proof. Treat as a route audit, not as a plan of record.

---

## 1. Philosophical Transition

**From:** *one formation persists.*

A single pre-objective cohesion field $u_t : X_t \to [0,1]$ forms, possesses a stable core $\mathrm{Core}^2$, and persists as itself through time via the partial-OT-induced correspondence $R_{t \to s}$.

**To:** *formations transition, split, merge, and compete.*

Multiple formations exist on shared sensory substrates. They appear, disappear, split, merge, exchange mass, and compete for stability. Each transition has a finite probability per unit time (Kramers rate); the equilibrium $K$-distribution is determined by sector free energies; the dynamic $K$-distribution is determined by transition rates.

The shift is from **identity** to **dynamics**: not "is this the same formation?" but "how do formations change in number and shape over time?"

---

## 2. Mathematical Transition

**From:** *temporal identity / transport stability.*

T-Temporal-Identity Cat A: $R_{t \to s} \subseteq \mathrm{PersComp}(u_t) \times \mathrm{PersComp}(u_s)$ is well-defined, unique, kernel-independent, and reduces to `persist_transport` at K=1. Stability is Lipschitz in fields + costs.

**To:** *metastable transition rates / energy landscape geometry.*

Eyring-Kramers regime: $\Gamma_K = (1/2\pi)\sqrt{\vert \lambda_-\vert \det H_*/\vert \det H_s\vert}\exp(-\Delta E/T_*)$. Saddle indices, barrier heights, prefactors, and confinement on the polytope $\Sigma_m$.

The shift is from **Lipschitz analysis** (continuity / stability) to **Morse analysis** (critical-point structure / saddle indices / Hessian determinants).

---

## 3. Candidate Route A — H-MORSE

### Core idea

Establish Morse decomposition of the SCC energy on the constrained polytope $\Sigma_m = \{u \in [0,1]^n : \sum_x u(x) = m\}$. Each $K$-sector becomes a basin of attraction; minima and saddles are nondegenerate (modulo symmetry).

### Sub-ideas

- **Finite-dimensional Morse on the polytope.** $\Sigma_m$ is a finite-dim convex polytope with $n-1$ degrees of freedom. Morse theory on convex polytopes is well-developed (Floer, Cohen-Jones).
- **Analytic energy.** $E$ involves $\sigma(z) = (1+e^{-z})^{-1}$, $W(u) = u^2(1-u)^2$, smooth quadratic boundary term $\alpha u^T L u$ — all real-analytic. Łojasiewicz inequality applies; trajectories converge to single critical points.
- **Genericity.** By Smale's transversality / Sard, generic perturbation makes Hessians nondegenerate. But canonical SCC has fixed parameter structure — need to verify the canonical landscape is itself Morse, not just generically so.
- **Symmetry breaking.** Translation on torus, rotation around disk-symmetric centers — these give Morse-Bott structure. Resolve by either (a) fixing gauge (modding out translation), (b) computing on the reduced moduli space, or (c) admitting Morse-Bott and lifting Eyring-Kramers via Bismut-Lebeau.
- **Projected Hessian.** $H(u^*)\vert _{T\Sigma_m}$ — project away the volume-constraint normal direction. Verify projection preserves spectral structure for SCC critical points.
- **Boundary strata.** $\partial \Sigma_m$ has corners; critical points on the boundary face $u_i = 0$ or $u_i = 1$ require boundary-Morse analysis (stratified Morse, Goresky-MacPherson).

### Likely sub-blockers

- Boundary critical points may have rank deficiency due to active inequality constraints.
- Symmetry zero modes need clean resolution.
- If any legacy $b_D \neq 0$ residue exists in the energy, analyticity may break locally.

---

## 4. Candidate Route B — Eyring-Kramers Package II

### Core idea

Given H-MORSE, derive transition rates between $K$ and $K \pm 1$ sectors via Friedlin-Wentzell large-deviation theory + Bovier-Eckhoff-Gayrard prefactor formulas.

### Sub-ideas

- **Transition rates.** Standard Eyring-Kramers: $\Gamma_{K \to K-1} = (1/2\pi)\sqrt{\vert \lambda_-\vert \det H_K/\vert \det H_s\vert}\exp(-\Delta E_{K \to s}/T_*)$.
- **Saddle indices.** Index-1 saddles connect adjacent K-basins; verify uniqueness of minimal-action path (instanton).
- **Barrier heights.** $\Delta E_{K \to s} = E(s) - E(\mathrm{argmin}_K E)$ — already partially Cat B (T-ST-5b, exp02-NEB).
- **Prefactors.** Require Hessian determinants at both minimum and saddle; needs H-MORSE Cat A.
- **Reflected Langevin on polytope.** P-F-A1 Package I (Cat A) gives well-posed SDE on $\Sigma_m$ with reflection. Friedlin-Wentzell action is meaningful.
- **P-F-A1 Package I dependency.** T-PF-A1-AR/SDE/GI/PE are all Cat A — the foundation is in place.

### Likely sub-blockers

- $T_*$ canonical registration (OP-0021) — still axiomatic. Without it, Kramers rates have an undetermined temperature scale.
- Berestycki-Hamel-Roques boundary regularity needed for reflected Langevin instantons near corners.
- Bovier-Eckhoff-Gayrard formulas require *capacity estimates* — additional analytic work beyond H-MORSE.

---

## 5. Candidate Route C — σ-Inheritance / OP-0008

### Core idea

Multi-formation temporal identity. When K changes ($K_t \neq K_s$), the σ-signatures of components must be inherited across the K-jump in a canonical way.

### Sub-ideas

- **K-jump inheritance.** T-σ-Inherit defines $\Phi$: for each event type, $\sigma(C_j^s) = \Phi(\sigma(C_i^t))$ + residual.
- **MERGE.** Two components $\{C_{i_1}, C_{i_2}\}$ merge to one $C_j$. Centroid is mass-weighted average (Cat B, deterministic). Orientation via parallel-axis theorem (Cat B). σ_standard is Cat C — requires Wigner-projection on multi-axis eigenstructure.
- **SPLIT.** One component $C_i$ splits to two $\{C_{j_1}, C_{j_2}\}$. Split direction = lowest Hessian eigenvector (Goldstone mode) — Cat B under gap condition $\lambda_1 < \lambda_2$. σ_standard Cat C.
- **Wigner projection (OP-0008 sub-task).** Project pre/post σ_rich onto canonical σ_standard via Wigner small-d matrix elements. Requires W9+ formalism — not yet canonical.
- **Multi-formation identity.** Once σ-inheritance is Cat A, the multi-component temporal correspondence acquires a structural backbone — formations are tracked not only as components but as carriers of σ-signatures through K-jumps.

### Likely sub-blockers

- Wigner-projection canonicalization (W9+ scope).
- Gap condition $\lambda_1 < \lambda_2$ at SPLIT — not generic; needs Morse argument (overlaps with Route A).
- σ_standard under MERGE/SPLIT remains Cat C; Cat A path is unclear without H-MORSE.

---

## 6. Risks

Cross-route risks that affect any CV-1.14 attempt:

- **Morse degeneracy due to symmetry.** Translation, rotation, gauge — produces Morse-Bott zero modes. If unresolvable, H-MORSE downgrades to Morse-Bott, and Package II requires Bismut-Lebeau extension.
- **Boundary critical points.** $\partial \Sigma_m$ has corners (active inequality constraints $u_i \in \{0,1\}$). Stratified Morse needed; not all formulas from interior Morse generalize.
- **Non-smoothness if any old $b_D \neq 0$ term reappears.** Łojasiewicz convergence breaks; analyticity is structural to current canonical state.
- **High-dimensional saddle enumeration.** Saddles between $K$ and $K+1$ are not unique; for $n = 225$ canonical grid, the saddle count can be combinatorially large.
- **K-field vs K-act ontology conflict.** K-field treats K as a scalar; K-act (D-ST-3) treats K as #PersComp observable. They agree at equilibrium under stable-K but may diverge during transitions. Canonical reconciliation is registered (T-K-Select-PF + T-K-Select-OBS); but Package II / dynamic K-selection must respect both views.
- **$T_*$ ambiguity (OP-0021).** Currently axiomatic; any rate prediction inherits the $T_*$ uncertainty.
- **HWF-1 derivability (OP-SB1-084, LOW).** Not blocking, but if a clean analytic $C_\mathrm{iso}$ derivation falls out of the H-MORSE analysis (Hessian structure may constrain core shape), it would also close OP-SB1-084 as a side benefit.

---

## 7. Recommended First Move

> **Do not prove H-MORSE immediately.**
> First perform H-MORSE / Package II Entry Audit.

The entry audit should:

1. **Reconstruct the H-MORSE statement.** Read all working/MF/ files mentioning Morse / metastability / nondegenerate critical points; collate into a single proposed canonical form.
2. **Build the dependency graph.** H-MORSE → T-PF-ε0-K → Package II — with cross-links to P-F-A1 Package I (Cat A), H-T* (OP-0021), and T-K-Select-PF/OBS (Cat B).
3. **Identify which questions Q1–Q6 each route addresses.** H-MORSE: Q3 + Q4. Package II: Q3 + Q4. σ-Inherit: Q6. Use the question structure to set priority.
4. **Enumerate failure modes.** For each candidate route, list 3–5 ways it could fail; identify which failure is most likely fatal under canonical SCC.
5. **Produce a CV-1.14 candidate proof plan** — sub-tasks, dependencies, estimated session counts, blockers.

Only after the audit should proof work begin. The audit itself is the CV-1.14 entry deliverable.

See `09_agent_handoff_prompt.md` for the executable handoff.
