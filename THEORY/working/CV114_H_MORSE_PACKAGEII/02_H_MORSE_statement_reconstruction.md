> [!nav] Linked: [[MOC_H_MORSE_packageII]] · [[MOC_Q3_stochastic_dynamics]] · [[THEORY_INDEX]]

# 02 — H-MORSE Statement Reconstruction

Agent C (Long-Form Theorem Writer) + Agent A (Aristotle-style formal discipline).

---

## 1. What is H-MORSE supposed to state?

The H-MORSE hypothesis node (HT-3.5 Q3) and the embedded H5 (Morse stability) hypothesis inside T-P-F-ε0-K refer to **nondegeneracy of the constrained Hessian of the SCC energy at relevant critical points**.

The intended informal content:

> Every critical point of the SCC energy $\mathcal E$ on the volume-constrained polytope $\Sigma_m$, *relevant to metastable transitions*, is a nondegenerate critical point in the Morse sense — its constrained Hessian has no zero eigenvalues other than those forced by structural symmetry.

This serves two downstream consumers:
1. **T-P-F-ε0-K Cat A promotion** — requires H5 (Morse stability) of the barrier saddle and minimum under the Bernoulli regularization perturbation $\mathcal E + \varepsilon R$.
2. **Package II Eyring-Kramers** — the Bovier-Eckhoff-Gayrard or Berglund-Gentz prefactor formulas require Morse nondegeneracy of every metastable minimum and every index-1 saddle connecting them.

---

## 2. Domain

The canonical state space hierarchy (canonical.md §3.9–§3.11):

| Symbol | Definition | Use |
|--------|------------|------|
| $\mathcal F_M(\mathcal P) = [0,1]^n \cap \Sigma_m$ | Field space — closed cube intersected with volume hyperplane | Static, $K=1$ |
| $\Sigma_m = \{u \in [0,1]^n : \sum_i u_i = m\}$ | Volume-constrained polytope | Single-formation |
| $\Sigma_m^\circ$ | Interior (strict inequalities $0 < u_i < 1$) | Interior critical points (canonical scope) |
| $\widetilde\Sigma_M^{K_\mathrm{field}}$ | K-field shared-pool manifold | Multi-formation (canonical §3.x) |
| $\widetilde\Sigma_M^{K_\mathrm{field},\circ}$ | Interior of K-field manifold | Multi-formation interior (current σ-framework scope) |

**For CV-1.14 H-MORSE entry, the primary domain is $\Sigma_m$** (single-formation polytope, $K=1$). Multi-formation Morse on $\widetilde\Sigma_M^{K_\mathrm{field}}$ requires NQ-248 / OP-0009 work and is W7+ scope (canonical.md line 1322 explicitly defers full corner handling via Option B stratified Morse to NQ-248).

**The boundary $\partial\Sigma_m$** consists of faces where $u_i \in \{0,1\}$. Critical points on the boundary require **stratified Morse** (Goresky-MacPherson) treatment. CV-1.14 should restrict to **interior critical points** $u^* \in \Sigma_m^\circ$ unless explicitly stated.

---

## 3. Which energy?

Three candidate energies appear in canonical:

| Energy | Definition | Use |
|--------|------------|------|
| $\mathcal E_\mathrm{bd}$ | $\frac{\alpha}{2} u^T L u + \beta \sum_i W(u_i)$ — Allen-Cahn / boundary morphology | Pure boundary-morphology subset |
| $\mathcal E = \lambda_\mathrm{cl}\mathcal E_\mathrm{cl} + \lambda_\mathrm{sep}\mathcal E_\mathrm{sep} + \lambda_\mathrm{bd}\mathcal E_\mathrm{bd}$ | Full static SCC energy | T8-Full, T-Persist-1, σ-framework |
| $\mathcal E + \varepsilon R$ where $R = -T_* S_\mathrm{Bern}$ | Bernoulli-regularized SCC energy | T-P-F-ε0-K |

H-MORSE / H5 refers to nondegeneracy at critical points of the **full static SCC energy $\mathcal E$** (or its Bernoulli regularization $\mathcal E + \varepsilon R$) on $\Sigma_m$.

**Temporal energy** (with transport term, $\mathcal E_\mathrm{tr}$ from temporal identity) is NOT in scope for CV-1.14 H-MORSE: the metastable picture is **static**, and temporal transport enters via the Langevin dynamics, not via critical-point structure of an enlarged energy.

---

## 4. What does "Morse" mean here?

Four candidate interpretations:

| Interpretation | Formal content | Difficulty | Necessity |
|---|---|---|---|
| **(i)** All critical points nondegenerate | $\det \Pi_T H_\mathcal E(u^*) \Pi_T \neq 0$ for all critical $u^*$ on $\Sigma_m^\circ$ | Extremely hard — equivalent to H-MORSE-Global | Not strictly needed |
| **(ii)** Local minima nondegenerate | Same restricted to $u^*$ with index 0 | Hard but tractable | Needed for EK prefactor at minima |
| **(iii)** Index-1 saddles nondegenerate | Same restricted to $u^*$ with index 1 (one negative eigenvalue) | Hard | Needed for EK prefactor at saddles |
| **(iv)** Generic perturbation Morse | After arbitrarily small perturbation $\delta R$, energy is Morse | Standard Smale transversality | Sidesteps but breaks canonical |

For Package II Eyring-Kramers, **(ii) AND (iii)** are needed: minima for the basin Hessian determinant, saddles for the index-1 saddle Hessian determinant. (i) is overkill.

H-MORSE-Local (Path A candidate) addresses (ii); a separate H-MORSE-Saddle candidate would address (iii).

---

## 5. Global vs local?

Phase 2 needs H-MORSE only **locally near canonical formations**. Specifically:

- Near the canonical single-formation minimizer $u^*$ produced by T8-Core (Cat A): need (ii).
- Near the saddle separating $u^*$ from a competing K=2 configuration: need (iii).
- Need NOT prove Morse on the entire $\Sigma_m^\circ$ — only on a neighborhood of the metastable basin endpoints.

Once H-MORSE-Local (minima + saddles) is established, Eyring-Kramers gives transition rates between known critical points. Global Morse decomposition (the full Morse complex on $\Sigma_m$) is a deeper, multi-session program.

---

## 6. Assumptions already canonical

The following inputs are Cat A and available:

| Input | Source | Use |
|-------|--------|------|
| Volume constraint manifold structure | canonical.md Prop 1.1, §11.1 | $\Sigma_m$ is convex polytope, manifold with corners, contractible |
| Tangent space at interior point | canonical.md §11.1 | $T_u\Sigma_m^\circ = \mathbf 1^\perp = \{v : \sum_i v_i = 0\}$ |
| Energy analytic | canonical.md §9.2 + axiom A4 + $b_D = 0$ | $\mathcal E \in C^\omega$ on $\Sigma_m^\circ$ |
| Łojasiewicz convergence (T14 Cat A) | canonical.md line 1131–1132 | Gradient flow converges to critical points |
| Closure-correction Hessian gap (Cat A) | canonical.md line 1139 | Non-trivial constrained minimizers of SCC energy have strictly larger min Hessian eigenvalue than corresponding Allen-Cahn minimizers |
| Existence of non-uniform minimizer (T8-Core Cat A) | canonical.md line 1090–1132 | T8-Full conditions imply non-uniform global minimizer |
| Symmetry quotient (Theorem 1, orbital, Cat A) | canonical.md line 1362 | $G_u = \mathrm{Stab}_{\mathrm{Aut}(G)}(u^*)$ acts on $T_{u^*}\Sigma_m$; orbital decomposition by Maschke |
| Translation-invariant Goldstone (V5b-T-b Cat A) | canonical.md line 1264–1303 | Super-lattice regime: $\mu_\mathrm{Gold} \propto e^{-c_d/\xi_0}$, positive but exponentially small |
| Sub-spinodal exact zero Goldstone (V5b-T-zero Cat A) | canonical.md line 1303 | Sub-spinodal: $\mu_\mathrm{Gold} = 0$ exactly on translation-invariant graphs |

These together provide most of the technical machinery; what is missing is a **uniform positive lower bound** on the projected Hessian spectrum modulo the structural zero modes.

---

## 7. Assumptions missing for H-MORSE

| Missing item | Severity |
|--------------|----------|
| Uniform lower bound on $\mu_\mathrm{min}(\Pi_T H_\mathcal E(u^*) \Pi_T)$ at canonical minimizers (Theorem 1 orbital block | HIGH |
| Symmetry quotient: identify which discrete-symmetry zero modes are structurally unavoidable | HIGH |
| Index-1 saddle existence between two K-distinct basins | HIGH (separate from minima audit) |
| Boundary stratum critical point characterization | MEDIUM (deferrable; restrict to $\Sigma_m^\circ$ in CV-1.14) |
| Genericity / transversality argument for symmetry-breaking perturbation | MEDIUM |
| Independence from $\lambda_\mathrm{cl}, \lambda_\mathrm{sep}, \beta, a_\mathrm{cl}$ regularity windows | MEDIUM (Cat B-conditional acceptable) |

---

## 8. Draft theorem candidates

### A. H-MORSE-Local

> Let $G$ be a finite connected graph and $u^* \in \Sigma_m^\circ$ be a non-uniform single-formation local minimizer of the full SCC energy $\mathcal E = \lambda_\mathrm{cl}\mathcal E_\mathrm{cl} + \lambda_\mathrm{sep}\mathcal E_\mathrm{sep} + \lambda_\mathrm{bd}\mathcal E_\mathrm{bd}$ satisfying:
> - **(M-A1)** Sub-critical canonical parameter window: $a_\mathrm{cl} \in (0, 4)$ (axiom A3), $b_D = 0$, $\beta > 7\alpha$ (phase-separation).
> - **(M-A2)** Symmetry-broken: $\mathrm{Stab}_{\mathrm{Aut}(G)}(u^*) = \{e\}$ (no nontrivial automorphism fixes $u^*$).
> - **(M-A3)** Strict interiority: $0 < \delta_0 \leq u^*_i \leq 1 - \delta_0$ for some $\delta_0 > 0$ on the support of $u^*$.
>
> Then the projected Hessian $H^\mathrm{proj}_\mathcal E(u^*) := \Pi_T H_\mathcal E(u^*) \Pi_T$ on $T_{u^*}\Sigma_m = \mathbf 1^\perp$ is positive definite, with explicit lower bound
> $$\mu_\mathrm{min}(H^\mathrm{proj}_\mathcal E(u^*)) \geq \mu_0(\lambda_\mathrm{cl}, \lambda_\mathrm{sep}, \beta, a_\mathrm{cl}, \delta_0)$$
> where $\mu_0$ is the closure-correction Hessian gap of canonical.md §13 line 1139.

**Difficulty:** Tractable. The closure-correction gap (Cat A) gives the positive contribution; (M-A2) excludes discrete-symmetry zero modes; (M-A3) excludes boundary saturation.

**Status target:** **Cat B** (conditional on M-A1, M-A2, M-A3). Cat A path: derive M-A2 and M-A3 from canonical axioms for the specific T8-Core minimizer.

### B. H-MORSE-Generic

> For every fixed graph $G$ and parameter set $(\lambda_\mathrm{cl}, \lambda_\mathrm{sep}, \beta, a_\mathrm{cl})$ in the canonical window, there exists an open dense subset $U \subset \mathbb R^n$ of small symmetry-breaking perturbations $\rho \in U$ such that the perturbed SCC energy $\mathcal E + \langle \rho, u \rangle$ restricted to $\Sigma_m$ is Morse.

**Difficulty:** Standard transversality argument (Smale, Sard). The challenge is showing the SCC-specific perturbation class is non-empty and respects ontological constraints (e.g., doesn't introduce $b_D \neq 0$ breaking analyticity).

**Status target:** **Cat B** for generic statement, **Cat A** for the existence of perturbation class.

### C. H-MORSE-Conditional

> Under M-A1 + the spectral repulsion condition H-SR ($\min_k \mu_k > (K-1)\lambda_\mathrm{rep}$) and well-separation H-WS, the constrained Hessian at the canonical minimizer is nondegenerate.

**Difficulty:** H-SR and H-WS are themselves OPEN (Q2 Phase 2). This shifts the problem.

**Status target:** **Cat B conditional**, useful as a way station.

### D. H-MORSE-PackageII

> The specific set of minima and index-1 saddles relevant to the K = 1 → K = 2 metastable transition pathway is Morse (in the constrained sense).

**Difficulty:** Same as A + a separate saddle argument. Requires identifying the saddle explicitly.

**Status target:** **Cat B**, but immediately useful for Package II entry.

---

## 9. Recommended candidate for CV-1.14

**Path A (H-MORSE-Local)** is most realistic and most useful:

- It directly addresses what Package II needs at minima.
- All required inputs are canonical Cat A (closure-correction gap, orbital symmetry, etc.).
- Hypotheses M-A1, M-A2, M-A3 are testable and natural.
- It does **not** attempt the boundary stratum, the saddle, the K-transition, or the regularization perturbation simultaneously — each is a separate future advance.

A companion **H-MORSE-Saddle** statement (Path D variant, restricted to a single explicit saddle) would complete the minimum needed for Eyring-Kramers but is a follow-up, not the first deliverable.

**Path B (Generic) and Path C (Conditional)** are useful framing but do not produce a single concrete Cat A theorem easily.

**Path A is the recommended CV-1.14 first theorem.** Cat B classification at registration; Cat A path requires deriving M-A2 / M-A3 from canonical axioms.

See `08_candidate_lemma_chain.md` for the full lemma chain and `09_CV114_recommendation.md` for the final recommendation.
