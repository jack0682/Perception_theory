# 01 — Exploration: SF Consolidation + Multi-Formation Derivation

**Session:** 2026-04-22 (SF-S1)
**Target (from plan.md):** (A) Formalize 4 Cat A candidates identified yesterday (Prop 1.3a/b, Cor 2.2 qualitative/quantitative) in `working/SF/` and register them in `canonical_sub.md`; (B) Derive multi-formation structure `(K̂, formation size, inter-formation spacing)` as functions of the single-formation invariants `(N_unst, ξ_0)` and re-express F-1 / M-1 / MO-1 dissolutions on that derived basis.
**This file covers:** §1 Restatement (Axis A and Axis B). §2 Multi-approach generation (≥3 mathematically-independent approaches per axis). §3 Primary-approach selection and rationale.
**Depends on reading:** `plan.md` 2026-04-22; `pre_brainstorm.md` 2026-04-22 §A-D, §E-G, §H; `logs/daily/2026-04-21/14_single_formation_audit.md` §1-10 (Round 12-18 integrated); `canonical.md` §11 (Multi-formation paradigm), §12 (K-field architecture), §13 Cat A/B/C lists, §14 CN6/CN8/CN14; `canonical_sub.md` 2026-04-21 Added/Pending entries; `working/E/{F1,M1,MO1}_dissolution.md`; `working/integer_K_dependency_map.md`; `working/E/soft_K_definition.md`.

---

## §1. Restatement

### 1.1 Axis A — Single-formation Cat A consolidation (G1, G2)

Yesterday's Round 12-18 produced **four Cat A candidates** with substantial numerical backing but no formal home in `working/`:

1. **Proposition 1.3a** (pure $\mathcal{E}_{\mathrm{bd}}$ Morse index).
   $\mathrm{Morse}\big(\mathrm{Hess}\,\mathcal{E}_{\mathrm{bd}}|_{u_{\mathrm{uniform}}}\big) = N_{\mathrm{unst}}(\beta, \alpha, c)$ with
   $$N_{\mathrm{unst}} = \#\{k \geq 2 : \mu_k^{\mathrm{bd}} < 0\},\qquad \mu_k^{\mathrm{bd}} = \beta W''(c) + 4\alpha\lambda_k(G).$$
   Numerically confirmed 9/9 PASS at $n=4096$ on the canonical 64×64 grid (Round 16 `exp_hessian_uniform_v2`).

2. **Proposition 1.3b** (cl_sep structural operator).
   $H_{\mathrm{cl,sep}} := H_{\mathrm{full}} - H_{\mathrm{bd}}$ restricted to $T_{u_{\mathrm{uniform}}}\Sigma_m$ is a $\beta$-independent, $(w_{\mathrm{cl}}, w_{\mathrm{sep}}, c, G, \alpha)$-dependent symmetric operator. At canonical defaults on 64×64, its spectrum lies in $[-4.97, +7.00]$ with 1641 negative eigenvalues (~40 %). Because the bd-Hessian contributes $\beta W''(c)$ on the common eigenspace, the full-energy Morse index is
   $$N_{\mathrm{unst}}^{\mathrm{full}}(\beta) = \#\{k \geq 2 : \mu_k^{\mathrm{bd}}(\beta) + \nu_k^{\mathrm{cl,sep}} < 0\},$$
   a shift of the pure-bd spectrum by a $\beta$-invariant perturbation $\{\nu_k^{\mathrm{cl,sep}}\}$.

3. **Corollary 2.2 (qualitative).** Every local minimizer $u^\ast$ of $\mathcal{E}_{\mathrm{bd}}$ on $\Sigma_m$ satisfies
   $$|B(u^\ast)| = O\!\big(\sqrt{\alpha/\beta}\cdot \mathrm{Per}_G(A^\ast)\big),\qquad B(u^\ast) := \{x : 0.1 < u^\ast_x < 0.9\},\;A^\ast := \{x : u^\ast_x \geq 0.5\}.$$
   Confirmed via three independent axes (exp42 slope −0.5, exp_interface_ansatz 20/20 PASS, exp_alpha_scan_v2 asymptotic).

4. **Corollary 2.2 (quantitative).** On 2D grids with tanh-profile circular interface of width $\xi_0 = \sqrt{\alpha/\beta}$,
   $$\frac{|B(u^\ast)|}{\mathrm{Per}_G(A^\ast)} = \frac{\pi\ln 9}{2}\cdot \xi_0 + O(1/\sqrt{n}) \approx 3.449\,\xi_0.$$
   Confirmed 20/20 at $n \in \{1024, \ldots, 262144\}$; constant agrees with ansatz to 1‰ at $n=262144$.

**What "formalization" means in this session.** (a) Statement in the canonical style (hypotheses, claim, conditions), (b) proof at the step-granularity of `working/` files (every step cites a canonical theorem, an external theorem, or a lemma proved in the same file), (c) numerical verification table (data file + pass count + grid invariance), (d) a bridge line to multi-formation structure (Axis B).

**Success criterion for Axis A.** `working/SF/` exists with README + four statement-level files; `canonical_sub.md` has a 2026-04-22 entry containing "Added 4" with each claim referenced by its working file; no claim is silently promoted to canonical.

### 1.2 Axis B — Multi-formation derivation from single-formation invariants (G3, G4)

plan.md's central Axis B claim (following yesterday's triple-anchored meta-theorem):

> Single-formation invariants $(N_{\mathrm{unst}}, \xi_0)$ determine the multi-formation triple $(\widehat{K}, \text{formation size}, \text{inter-formation spacing})$ up to graph-topology-dependent $O(1)$ constants.

The concrete derivables:

- $\widehat{K}(\beta, \alpha, T, c, G) = f\!\big(N_{\mathrm{unst}}(\beta, \alpha, T, c, G)\big)$ for some $f$ depending only on the graph's dimension/topology class.
- $m_k \approx m/\widehat{K}$ at short time; long-time $K^\ast = 1$ (isoperimetric limit, T-Merge (b)).
- $d_{\min}^\ast \asymp \xi_0$ (with a graph-topology-dependent prefactor), not $\sqrt{\beta/\alpha}$ as currently fit in canonical's retracted-Cat-B T-d_min-Formula.

**Why Axis B is the key move.** F-1, M-1, MO-1 each assume integer $K$ as the object being quantified. In the derivable framework, integer $K$ is *not a primitive*; it is a one-parameter summary of the continuous mode-count statistics seeded by $N_{\mathrm{unst}}$ instability directions and filtered by isoperimetric competition. Framing the three Critical problems around integer $K$ is therefore an artifact of choosing integer-K language; the problems partially or fully dissolve once the derived view is adopted.

**Success criterion for Axis B.** `working/MF/from_single.md` containing: (a) at least three candidate mode-count laws $f$ tested against Round 12-17 data, (b) a formation-size decomposition, (c) an inter-formation spacing formula in terms of $\xi_0$, (d) an explicit two-timescale dynamical picture (emergence → metastable → coarsening), (e) a quantitative reinterpretation of CN6. The three dissolution files each receive a "Round 18 post-audit" section casting F-1 / M-1 / MO-1 in the new language.

### 1.3 Scope clarification (non-goals restated)

Following plan.md §Non-goals:

- Not a new Langevin run (Stage-5 scripts already present but unexecuted).
- Not a full numerical verification of `K̂ = f(N_unst)` across non-grid graphs (exp_mode_emergence.py carries).
- Not a direct canonical edit.
- Not a commitment beyond the 4 Cat A candidates already identified.

### 1.4 Explicit assumptions surfaced from plan.md

Three assumptions plan.md leaves implicit, flagged here:

1. **"$(N_{\mathrm{unst}}, \xi_0)$ determine $\widehat{K}$" is a conjecture backed by Round 12 heuristic, not a theorem.** The conjectural step is $\widehat{K} - 1 \asymp \sqrt{N_{\mathrm{unst}}}$ on 2D grids. No proof exists; it is the primary target of today's development if primary approach is chosen appropriately.
2. **Cor 2.2 quantitative is established for tanh-profile *ansatz*, not for the true SCC minimizer.** Round 18 exp_alpha_scan_v3 revealed a 16–60 % deviation between the ideal tanh prediction $C = 3.449$ and the measured SCC ratio. This deviation is NQ-32 and must be kept explicit.
3. **"Short-time" vs "long-time" dichotomy presumes a thermal framework.** In the zero-temperature gradient-flow setting of canonical v1.2, there is no genuine "short-time emergence regime" separate from the long-time limit; they coincide at the first critical point reached. The dichotomy is quantitative only at $T > 0$ (Langevin) or on landscapes with multiple local minima traversable by initial conditions. This connects to open problem P-F (metastability framework).

## §2. Multi-approach generation

Three candidate routes for each axis. Each route uses a distinct mathematical tool, has distinct failure modes, and has distinct admissible-hypothesis regimes. (See §2.5 for the independence check.)

### 2.1 Approach A1 — Spectral/Hessian analytic (Axis A)

**Core idea.** Work entirely on the Hessian of the constrained full-energy $\mathcal{E}$ at $u_{\mathrm{uniform}}$, expressed in the Laplacian eigenbasis. Decompose $H_{\mathrm{full}} = H_{\mathrm{bd}} + H_{\mathrm{cl,sep}}$ and characterize each block separately.

**If successful.** Both Prop 1.3a and Prop 1.3b acquire analytic statements: Prop 1.3a exact via eigenvalue counting; Prop 1.3b via explicit construction of $H_{\mathrm{cl,sep}}$ as a sum of rank-$r$ perturbations (closure contributes a PSD Gram matrix; separation contributes an overlap kernel). The structural claim "$H_{\mathrm{cl,sep}}$ has a $\beta$-invariant spectrum" is immediate from the linearity in $\beta$ of $\mathcal{E}_{\mathrm{bd}}$ only (the closure and separation terms carry no explicit $\beta$).

**Failure mode.** The closure Hessian involves $J_{\mathrm{Cl}}(u)$, which at $u_{\mathrm{uniform}}$ may depend on $\beta$ through secondary effects (if closure parameters are $\beta$-coupled — they are not in canonical, but a future axiomatic change could break this). The separation Hessian depends on $\mathbf{C}_t = (I - \alpha W_{\mathrm{sym}})^{-1}$, which depends on $\alpha$ but not $\beta$. So $\beta$-invariance of $H_{\mathrm{cl,sep}}$ is exact; the failure mode is degeneracy — multiple eigenvalues colliding at zero — which would invalidate Morse-index counting.

**Canonical interaction.** Direct use of T8-Core (Cat A) for spinodal condition, T20 (axiom consistency, $a_{\mathrm{cl}} < 4$), Coupling Bound Lemma structure (§12, now flagged for retirement but structurally unchanged at single-formation level).

### 2.2 Approach A2 — Γ-convergence / isoperimetric (Axis A)

**Core idea.** Derive Cor 2.2 as a direct corollary of canonical T11 (Γ-convergence, Cat A) plus the graph-to-continuum interface-width integral.

**If successful.** The qualitative Cor 2.2 is immediate (Γ-convergence bounds boundary measure by perimeter × width). The quantitative constant $C = \pi\ln 9/2$ comes from integrating the tanh profile from $u = 0.1$ to $u = 0.9$ in continuum and applying the 2D-grid edge-count-to-continuum-perimeter factor $2/\pi$. Explicit derivation:
$$C = \underbrace{\ln 9}_{\text{tanh width from 0.1 to 0.9}}\cdot \underbrace{\frac{\pi}{2}}_{\text{grid-to-continuum Per factor}^{-1}} = \frac{\pi\ln 9}{2} \approx 3.449.$$

**Failure mode.** Cor 2.2 quantitative holds for **tanh profile**, not the true SCC minimizer. Round 18 directly shows the SCC minimizer has a perturbed profile due to $H_{\mathrm{cl,sep}}$ (NQ-32). So Approach A2 yields "quantitative for tanh ansatz; asymptotic upper bound for true minimizer".

**Canonical interaction.** Extends T11, intersects T-Merge (b) (isoperimetric energy ordering).

### 2.3 Approach A3 — Numerical-first inductive (Axis A)

**Core idea.** Accept the 20/20 PASS and 9/9 PASS numerical results as sufficient Cat-A-grade evidence and focus formalization effort on hypothesizing the explicit analytic forms that the numerics fit.

**If successful.** Cor 2.2 quantitative committed as "empirical-exact at tested scales" with derivation sketched via tanh ansatz (Approach A2). Prop 1.3a committed as exact at tested parameters with proof via Approach A1.

**Failure mode.** The numerics are run at fixed $(c = 0.5, \alpha = 1, \mathrm{grid type = square})$; extrapolation to other regimes is not justified by the experiments alone. Cat A commitment requires either analytic backing or broader numerical coverage.

**Canonical interaction.** The weakest interaction: this is essentially a commitment to the 4 claims as written, with proofs to be filled in later.

### 2.4 Approach B1 — Linearization → weakly-nonlinear reduction (Axis B)

**Core idea.** Write $u(x,t) = c + \sum_k a_k(t) \phi_k(x)$ in the Laplacian eigenbasis. Near $u_{\mathrm{uniform}}$, amplitudes of unstable modes ($k$ with $\mu_k < 0$) grow exponentially; stable modes decay. At nonlinear saturation, the surviving "active" modes determine $\widehat{K}$. Apply the Cahn-Hilliard amplitude-equation approach (Stuart-Landau / center-manifold reduction near $\beta = \beta_{\mathrm{crit}}^{(k)}$).

**If successful.** Explicit derivation of $\widehat{K}$ as a function of $N_{\mathrm{unst}}$ for generic graph topologies:
- On 1D periodic cycle: active modes come in $(+\phi_k, -\phi_k)$ pairs saturating to half-cycle patterns, so $\widehat{K} \approx N_{\mathrm{unst}}$ (each cycle mode gives two bumps).
- On 2D grid: active modes form a 2D grid $\{(p, q)\}$ of spatial frequencies; isotropic saturation yields $\widehat{K} \approx (1 + \sqrt{N_{\mathrm{unst}}})^2 / 4$ or similar root-scaling law.
- On general graph: $\widehat{K} \approx N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}}$ where $d_{\mathrm{eff}}$ is the graph's spectral dimension (Kac / anomalous diffusion sense).

**Failure mode.** Weakly-nonlinear analysis is valid only in a neighborhood of $\beta_{\mathrm{crit}}^{(k)}$. Far above threshold, saturation is governed by $W(u) = u^2(1-u)^2$ cubic-nonlinear dynamics and by finite-volume constraints $\sum u_i = m$; the "amplitude-equation" picture breaks down. So B1 predicts $\widehat{K}(\beta)$ only in a window around each $\beta_{\mathrm{crit}}^{(k)}$, patching them is ad-hoc.

**Canonical interaction.** Uses canonical T-Birth-Parametric (D4 supercritical pitchfork, Cat A), T8-Core. Introduces no new claim at Cat A level within session — the $\widehat{K}$ law is at best **conjectural** (backing by Round 12 heuristic + B1 weakly-nonlinear sketch).

### 2.5 Approach B2 — Isoperimetric packing (Axis B)

**Core idea.** Forget the Hessian. Treat each formation as a disk of area $\sim m/\widehat{K}$ with interface width $\xi_0$, packed on the grid with mutual exclusion distance $\sim \xi_0$ (from exponential tail overlap). Volume budget constraint: $\widehat{K} \cdot (\text{disk area} + \text{exclusion margin}) \leq L^2$.

**If successful.** $\widehat{K}_{\max}(\beta, \alpha, m, L) = \lfloor L^2 / (\pi r_0^2 + 2\pi r_0 \xi_0) \rfloor$ where $r_0 \approx \sqrt{m/(\pi \widehat{K})}$ — a self-consistency equation yielding $\widehat{K}$ as the packing maximum. In the limit $m \ll L^2$ and $\xi_0 \ll r_0$: $\widehat{K} \to m / (\pi \xi_0^2 \cdot C)$ for a dimensionless packing constant $C$.

**Failure mode.** Packing gives an **upper bound** on $\widehat{K}$ (the largest number of disks that fit), not the dynamical $\widehat{K}$. The dynamical $\widehat{K}$ is often much smaller than the packing bound because few initial-condition mode directions actually activate. So B2 alone predicts the *wrong* thing (always gives the ceiling $\widehat{K}_{\max}$, whereas observations show $\widehat{K}$ scaling with the instability count).

**Canonical interaction.** Uses isoperimetric inequality (Deep Core Dominance 2b), $\xi_0$ from Cor 2.2.

### 2.6 Approach B3 — Dimensional analysis + graph-class classification (Axis B)

**Core idea.** $\widehat{K}$ is dimensionless; it must be a function of dimensionless invariants constructible from the parameters. The natural dimensionless combinations: (i) $\beta/\beta_{\mathrm{crit}}^{(2)}$ (supercriticality measure), (ii) the graph's "effective dimension" (number of Fiedler-like eigenvectors below threshold), (iii) volume fraction $c \in (c_-, c_+)$, and (iv) temperature $T/T^\ast_{\mathrm{uniform}}$.

**If successful.** $\widehat{K}$ is parameterized by a graph-class $\mathcal{G}$ (2D grid, cycle, SBM, barbell, expander, …) and a two-parameter curve in $(\beta/\beta_{\mathrm{crit}}, T/T^\ast)$ with universal form *within the class*. Computing $\widehat{K}$ for specific $\mathcal{G}$ reduces to counting unstable modes modulo $\mathrm{Aut}(G)$ symmetry.

**Failure mode.** Dimensional analysis by itself is non-predictive; it merely constrains the form of any dependence. It does not yield a specific $f$.

**Canonical interaction.** Uses T-Birth-Parametric's $\beta_{\mathrm{crit}}$, T*_uniform's $T$-axis. Generates the right taxonomy but not a concrete formula.

### 2.7 Independence check (§5 of prompt)

| Approach pair | Shared idea? | Same failure mode? | Same admissible regime? |
|---|---|---|---|
| A1 vs A2 | No (Hessian vs perimeter) | No (degeneracy vs profile deviation) | Both: $c \in$ spinodal |
| A1 vs A3 | No (analytic vs numerical) | No (degeneracy vs extrapolation) | A1 broader (all $c$, $\beta$); A3 fixed params |
| A2 vs A3 | Partial (both use tanh) | Partial (both fail for true SCC profile) | Both: sharp-interface |
| B1 vs B2 | No (amplitude eq vs packing) | Different (range validity vs over-prediction) | B1: near threshold; B2: large $\beta$ |
| B1 vs B3 | Weakly (both use spectra) | Different (local saturation vs under-prediction) | B1: specific $\beta$; B3: any |
| B2 vs B3 | No (packing vs dimension count) | Different (ceiling vs vacuity) | Orthogonal |

A2 and A3 overlap substantially on the tanh-profile assumption and share the NQ-32 failure mode. Keeping both is redundant; Approach A2 subsumes A3 once the analytic derivation is in hand. Retaining **A1, A2** as the two substantive approaches for Axis A.

For Axis B: **B1, B2, B3** are substantively independent. B1 gives the dynamical emergence law; B2 gives the upper envelope; B3 gives the classification scaffold.

## §3. Primary approach selection

### 3.1 Axis A — Primary: A1 (Hessian analytic) + A2 (Γ-convergence) as dual pillars

**Rationale.** Prop 1.3a/b naturally belong to A1 (Hessian decomposition). Cor 2.2 qualitative/quantitative naturally belong to A2 (Modica-Mortola + explicit profile integration). The two are not a single approach; they are complementary proofs for independent claims. This is reflected in plan.md's G1: `mode_count.md` and `interface_scale.md` are separate files.

**Development priority:**
1. Prop 1.3a full analytic statement + proof via A1.
2. Prop 1.3b structural characterization via A1 (decomposition, $\beta$-invariance, spectrum estimation); fine-spectrum claim ($[-4.97, +7.00]$) is config-specific.
3. Cor 2.2 qualitative via A2 (Modica-Mortola upper bound).
4. Cor 2.2 quantitative via A2 (tanh ansatz integration); keep NQ-32 explicit as the gap between "quantitative on ansatz" and "quantitative on SCC minimizer".

**Alternative A3 preservation.** Approach A3 (numerical-first) is held in reserve for claims that cannot be fully analytically justified in one session — specifically, the 1641-negative-eigenvalue count for Prop 1.3b at the canonical 64×64 configuration.

### 3.2 Axis B — Primary: B1 (weakly-nonlinear / amplitude) with B3 as scaffolding

**Rationale.** B1 is the only approach among the three that yields a *specific dynamical law* for $\widehat{K}$, which is what plan.md's G3 requires. B2 (packing) and B3 (dimensional analysis) are kept as supporting frameworks: B2 for checking consistency in the large-$\beta$ limit and B3 for stating the universality class.

**Development priority:**
1. $\widehat{K} = f(N_{\mathrm{unst}})$ on 2D grid: derive via B1 amplitude saturation + B3 graph-class restriction. Show $\widehat{K} \approx 1 + \sqrt{N_{\mathrm{unst}}}$ as the Round 12 heuristic.
2. Formation size $m_k$ via mass conservation + B1 amplitude isotropy.
3. Inter-formation spacing $d_{\min}^\ast \asymp \xi_0$ via Coupling Bound Lemma item 5 (exponential tail decay) — this is a standalone single-formation result already Cat A, merely reinterpreted.
4. Two-timescale picture (emergence vs coarsening) via B1 linearization for $t_{\mathrm{emerge}}$ and T-Merge (b) + CN14 for $t_{\mathrm{coarsen}}$.
5. Quantitative CN6 restatement: $\widehat{K}$ is set by $N_{\mathrm{unst}}$ at the emergence timescale; thermodynamic K=1 is reached only at the coarsening timescale.

**Alternative B2 preservation.** B2 (packing) is the fallback if B1's amplitude-equation reduction proves analytically intractable on non-grid graphs. It gives the $\widehat{K}_{\max}$ upper envelope for sanity-checking.

### 3.3 Approaches rejected

- **A3 (numerical-first)** — subsumed by A1 + A2 once analytic backing is in hand.
- **None fully rejected for Axis B** — B2/B3 are retained as supporting, not rejected.

### 3.4 Explicit hypotheses kept for reactivation

If B1 fails on non-2D-grid graphs (e.g., SBM, barbell), activate:
- **H-A1** (1D cycle: $\widehat{K} \approx N_{\mathrm{unst}}$ via cosine-pair saturation, pre_brainstorm §A).
- **H-A4** (SBM: $\widehat{K} \approx K_{\mathrm{block}}$ via block-indicator Fiedler eigenvectors).
- **H-A5** (Barbell: $\widehat{K} = 2$ from bridge-cut Fiedler).

These become concrete experiments for later sessions (exp_mode_emergence.py extensions).

### 3.5 Non-primary tracks explicitly parked

- **G-D (Aut(G) symmetry-breaking moduli space $\mathcal{M}_1$):** scoped out per Round 15, carried to post-Stage-1.
- **NQ-32 full profile deviation analysis:** G5 produces only the `exp_profile_fit.py` script; numerical execution carried to later sessions.
- **Langevin-based verification of two-timescale picture:** scripts exist but are not run.
- **$d_{\min}^\ast$ remeasurement at NQ-30 resolution:** flagged as open; re-measurement carried to later numerical session.

---

## §4. Summary of file outputs anticipated

| Section | Output |
|---|---|
| Axis A primary | `02_development.md` §2, §3; `working/SF/mode_count.md`, `working/SF/interface_scale.md` |
| Axis B primary | `02_development.md` §4, §5; `working/MF/from_single.md` |
| Integration | `03_integration_and_new_open.md`; `canonical_sub.md` 2026-04-22 entry |
| Dissolution updates | `working/E/{F1,M1,MO1}_dissolution.md` Round 18 post-audit sections |
| Dependency-map update | `working/integer_K_dependency_map.md` rewrite |
| NQ-32 script | `CODE/experiments/exp_profile_fit.py` |
| Errata batch | E-4/5/6 and E-18/19/20 application notes inline |
| Summary | `99_summary.md` |

**End of 01_exploration.md.**
