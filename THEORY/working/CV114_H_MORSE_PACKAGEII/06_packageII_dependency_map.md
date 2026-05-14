> [!nav] Linked: [[MOC_H_MORSE_packageII]] · [[MOC_Q3_stochastic_dynamics]] · [[THEORY_INDEX]]

# 06 — Package II Dependency Map

Agent E (Package II / Eyring-Kramers Mapper). What does Package II (Eyring-Kramers + metastable transition rates) require, what is available from Package I, and what is the entry criterion for CV-1.14?

---

## 1. Known Package I inputs (Cat A available)

Package I = T-PF-A1-{AR, SDE, GI, PE}, all canonical Cat A (CV-1.8–CV-1.9).

| Input | Theorem | Status | Content |
|-------|---------|--------|---------|
| Affine reduction (constraint coordinatization) | **T-PF-A1-AR** | Cat A (CV-1.8) | $\Sigma_m$ realized as bounded convex polytope $\tilde C \subset \mathbb R^{n-1}$ via affine map; rigorous tangent-space coordinatization |
| Reflected SDE well-posedness | **T-PF-A1-SDE** | Cat A (CV-1.8) | Lions-Sznitman Thm 1 case (ii) on convex polytope $\tilde C$: bounded Lipschitz drift, $T_* > 0$ nondegenerate noise → unique strong solution $(X_t, K_t)$ to reflected SDE |
| Gibbs invariant measure (existence + uniqueness) | **T-PF-A1-GI** | Cat A (CV-1.9) | $\pi_{T_*} \propto e^{-\mathcal E/T_*}\mathbf 1_{\tilde C}$; zero-current $J[\pi^*] = 0$; heat-kernel positivity → any invariant measure $\nu \ll \pi$; $L^2(\pi)$ kernel argument → $h = 1$ |
| Poincaré inequality + exponential ergodicity | **T-PF-A1-PE** | Cat A (CV-1.9) | Payne-Weinberger 1960 for bounded convex domains; Holley-Stroock perturbation; $\lambda_1 \geq (\pi^2/n)\exp(-\mathrm{osc}/T_*)$; $L^2 \to TV$ via Cauchy-Schwarz |
| Compact constrained domain | (Cat A canonical) | Cat A | $\Sigma_m$ compact polytope; $\tilde C$ bounded convex polytope |
| Analytic energy | $b_D = 0$ canonical | Cat A | $\mathcal E \in C^\omega$ on $\Sigma_m^\circ$; Łojasiewicz applies |
| Gibbs continuity at $\varepsilon = 0$ | **T-P-F-ε0** | Cat A (CV-1.7) | $\mu_\varepsilon \Rightarrow \mu_0$ weakly as $\varepsilon \to 0$ |

**What Package I gives:** Existence of well-posed reflected stochastic dynamics on $\tilde C$ with Gibbs $\pi_{T_*}$ as the unique invariant measure, exponentially ergodic in TV. This is the **dynamics** half of metastability.

**What Package I does NOT give:** Quantitative metastable transition rates, Eyring-Kramers prefactor, sharp Poincaré constant (the $C_P$ from PE is metastable-exponentially large), Freidlin-Wentzell quasipotential, K-transition pathway identification, $T_* \to 0$ asymptotics.

---

## 2. Missing Package II inputs

For Eyring-Kramers transition rates between metastable basins, the following are needed:

### 2.1 Critical-point structure

| Item | Status | Source |
|------|--------|--------|
| Nondegenerate local minima of $\mathcal E$ on $\Sigma_m^\circ$ | **OPEN (H-MORSE)** | this audit |
| Nondegenerate index-1 saddles connecting basins | **OPEN (H-MORSE-Saddle)** | not yet registered |
| Saddle path uniqueness (instanton) | OPEN | requires Freidlin-Wentzell |
| Hessian determinant prefactors $|\det H^\mathrm{proj}|^{1/2}$ at minima and saddles | derives from H-MORSE | conditional |

### 2.2 Barrier structure

| Item | Status | Source |
|------|--------|--------|
| Positive barrier $\Delta\mathcal E = \mathcal E(\text{saddle}) - \mathcal E(\text{minimum}) > 0$ | Cat A (numerical) / Cat B (analytical for SCC) | T-ST-5a Cat A; T-ST-5b Cat B; T-P-F-ε0-K Cat B |
| Quantitative lower bound on $\Delta\mathcal E$ | Cat B (T-P-F-ε0-K) | conditional on H5 |
| Barrier stability under regularization | Cat B (T-P-F-ε0-K) | $\Delta\mathcal E_\varepsilon = \Delta\mathcal E_0 + \varepsilon \Delta R$ |

### 2.3 Basin geometry

| Item | Status | Source |
|------|--------|--------|
| Basin boundaries (stable manifolds of saddles) | OPEN | requires Morse + flow analysis |
| Basin metric in projected coordinates | partial | T-PF-A1-AR coordinates available |
| Boundary regularity (interior vs $\partial \Sigma_m$) | OPEN | stratified Morse W7+ |

### 2.4 Small noise / large deviation

| Item | Status | Source |
|------|--------|--------|
| Freidlin-Wentzell action functional | OPEN | references in pf_a1_lions_sznitman_freidlin_route.md |
| Quasipotential $V(x, y)$ on $\tilde C$ | OPEN | open derivation |
| Small-$T_*$ limit existence | open ($T_*$ axiomatic, OP-0021) | conditional |
| Bovier-Eckhoff-Gayrard prefactor formula | requires H-MORSE + FW | literature-available, but adaptation needed for reflected Langevin |

### 2.5 Reflected diffusion correction

| Item | Status |
|------|--------|
| EK formula adapted to reflected Langevin on convex polytope with corners | literature-needed |
| Boundary contribution to escape rate near saddle on $\partial \Sigma_m$ | OPEN (deferred to W7+) |
| Saddle accessibility from reflected dynamics | conditional on basin boundary regularity |

---

## 3. Eyring-Kramers form needed

### 3.1 Classical Eyring-Kramers (interior, smooth domain)

For overdamped Langevin $dX = -\nabla \mathcal E(X) dt + \sqrt{2T_*} dW_t$ on $\mathbb R^n$ with Morse $\mathcal E$ having two basins $\mathfrak m_1, \mathfrak m_2$ separated by index-1 saddle $\mathfrak s$:

$$k_{1 \to 2} = \frac{|\lambda_-(\mathfrak s)|}{2\pi} \cdot \sqrt{\frac{|\det H^\mathrm{proj}_\mathcal E(\mathfrak s)|}{\det H^\mathrm{proj}_\mathcal E(\mathfrak m_1)}} \cdot e^{-(\mathcal E(\mathfrak s) - \mathcal E(\mathfrak m_1))/T_*}$$

where $\lambda_-(\mathfrak s)$ is the unique negative eigenvalue of $H^\mathrm{proj}$ at the saddle.

### 3.2 SCC-adapted (reflected Langevin on convex polytope $\tilde C$)

On the **interior** of $\tilde C$, the same formula applies in the projected coordinates $T_{u^*}\Sigma_m^\circ = \mathbf 1^\perp$ (canonical AR coordinatization from T-PF-A1-AR Cat A).

**Required modifications for SCC:**

1. **Projection.** Hessians are projected: $H^\mathrm{proj} = \Pi_T H_\mathcal E \Pi_T$. The volume-constraint direction $\mathbf 1$ is excluded. Determinants are computed over $\mathbf 1^\perp$ ($n - 1$ dimensions).

2. **Boundary effect.** If either the minimum or saddle lies in $\partial \Sigma_m$ (or close to it), the reflected diffusion contributes a boundary correction. Bovier-Eckhoff (2003) gives:
   $$k_{1 \to 2}^\mathrm{refl} = (1 + \text{boundary correction}) \cdot k_{1 \to 2}^\mathrm{classical}$$
   with explicit form depending on the angle of $\partial \Sigma_m$ at the critical point.

3. **Symmetry quotient.** If multiple equivalent saddles exist by graph automorphism (degeneracy class #5), the EK formula aggregates rates over the orbit.

**Determinant form (SCC):**
$$k_{1 \to 2} = \frac{|\lambda_-^\mathrm{proj}(\mathfrak s)|}{2\pi} \sqrt{\frac{|\det \Pi_T H_\mathcal E(\mathfrak s) \Pi_T|_{\mathbf 1^\perp}}{\det \Pi_T H_\mathcal E(\mathfrak m_1) \Pi_T|_{\mathbf 1^\perp}}} e^{-\Delta\mathcal E / T_*}$$

with $\Delta\mathcal E = \mathcal E(\mathfrak s) - \mathcal E(\mathfrak m_1)$.

For Cat A: need H-MORSE-Local (Hessian at minimum) + H-MORSE-Saddle (Hessian at saddle) + ΔE Cat A (currently Cat B via T-P-F-ε0-K) + $T_*$ registered (OP-0021).

---

## 4. Dependency graph

```
                          ┌─────────────────┐
                          │  P-F-A1         │
                          │  Package I      │
                          │  (CAT A, ALL 4) │
                          │ AR/SDE/GI/PE    │
                          └────────┬────────┘
                                   │ reflected Langevin
                                   │ + Gibbs invariant
                                   │ + Poincaré ergodic
                                   ▼
            ┌────────────────────────────────────────────────┐
            │  Package II prerequisites (all OPEN)            │
            ├────────────────────────────────────────────────┤
            │                                                 │
            │  H-MORSE  ──────────┐                          │
            │  (minima nondegen)  │                          │
            │                     ├──→ Hessian determinant   │
            │  H-MORSE-Saddle ────┤    prefactors            │
            │  (saddle nondegen)  │                          │
            │                     │                          │
            │  H-BARRIER  ────────┤ ΔE separation            │
            │  (currently Cat B,  │                          │
            │   T-P-F-ε0-K)       │                          │
            │                     │                          │
            │  H-BASIN  ──────────┤ basin geometry,          │
            │  (basin boundaries) │ saddle accessibility     │
            │                     │                          │
            │  H-T*  / OP-0021 ───┤ canonical T* registration│
            │  (axiomatic)        │                          │
            │                     ▼                          │
            │           Freidlin-Wentzell action            │
            │           quasipotential V(x,y)               │
            │                     │                          │
            │                     ▼                          │
            │           Bovier-Eckhoff-Gayrard /             │
            │           reflected EK prefactor               │
            │                     │                          │
            └─────────────────────┼──────────────────────────┘
                                  ▼
                       ┌─────────────────────┐
                       │   Package II        │
                       │   Eyring-Kramers    │
                       │   transition rates  │
                       └──────────┬──────────┘
                                  │
                                  ▼
                       K-Select-DYN (OP-0005-DYN)
                                  │
                                  ▼
                       D-ST-4 rate claims (Γ, Z_K, π_K)
                                  │
                                  ▼
                       Q4-DYN — Dynamic K-selection
                                  │
                                  ▼
                       Q3-Q4 SCC dynamic completion
```

**Critical gates:** H-MORSE (top), OP-0021 ($T_*$). Both must close before Package II becomes meaningful. They are independent — can be attacked in parallel.

---

## 5. Package II entry criterion

**Minimum theorem needed for CV-1.14 Package II registration:**

> *(Working Cat B)* Let $u^*_1, u^*_2 \in \Sigma_m^\circ$ be two non-uniform single-formation local minimizers of $\mathcal E$ satisfying M-A1, M-A2, M-A3 (cf. `02_H_MORSE_statement_reconstruction.md §8`), with $\mathcal E(u^*_1) \leq \mathcal E(u^*_2)$. Suppose there exists an index-1 saddle $\mathfrak s$ connecting their basins, also satisfying M-A1, M-A2, M-A3. Then, in the limit $T_* \to 0$ (axiomatic via OP-0021), the reflected Langevin transition rate $k_{2 \to 1}$ satisfies the Eyring-Kramers formula with projected Hessian determinants.

**Required closures for this entry criterion:**

1. **H-MORSE-Local Cat B** (Path B of `08_candidate_lemma_chain.md`) — minimum Hessians.
2. **H-MORSE-Saddle Cat B** — saddle Hessian (separate but parallel).
3. **Existence of index-1 saddle** between two known minimizers — needs Freidlin-Wentzell or explicit construction.
4. **OP-0021 / T_* registration** — can remain axiomatic for the working theorem, just acknowledged.

**Realistic CV-1.14 deliverable for Package II:** Not the full entry theorem, but the **first prerequisite** — H-MORSE-Local Cat B (which addresses item 1). Items 2, 3, 4 remain Cat B-conditional or OPEN at CV-1.14 close.

**See `09_CV114_recommendation.md` for the final recommendation.**
