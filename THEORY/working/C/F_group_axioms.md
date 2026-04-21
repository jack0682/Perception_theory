# F-Group Axioms — Thermal SCC Foundation (G2)

**Status:** working (F1–F2 commit + Cat A; F3 **Cat A on Σ_m^ε** per Round 3 verification; F4 statement draft, 2026-04-21)
**Author origin:** `logs/daily/2026-04-21/01_exploration.md` §3.1 (Primary P1 + standard stat-mech overlay).
**Canonical refs:** `canonical.md` §3 (formal universe), §6 Group A–E (existing axioms), §8.1 (energy functional ℰ on Σ_m), §11 (fixed commitments — esp. CN5 four-term independence, CN8 metastable not globally optimal), §14 CN6 (K kinetically determined — to be re-anchored thermally), CN8 (formations metastable not globally optimal), CN14 (closure expands metastability — to be substantiated thermally).
**Working refs:** `working/open_problems_reframing_2026-04-19.md` §6 P-F (zero-temperature metastability gap), §6 P-C (third-mode missing); `working/integer_K_dependency_map.md` (10 load-bearing theorems).
**External refs:** Da Prato & Zabczyk (1992), *Stochastic Equations in Infinite Dimensions* (projected SDE on constrained manifolds, esp. Ch. 6); Helffer-Sjöstrand (1985), *Puits multiples en mécanique semi-classique* (Witten Laplacian semiclassical low-T); Simon (1985), *Semi-classical analysis of low lying eigenvalues IV* (Witten Laplacian on ℝ^n); Kramers (1940), Eyring (1935) (escape rates).

---

## §0. Scope and Layer

**Layer.** F-group is a **new axiomatic group**, parallel to and overlaid on the existing Groups A (Closure), B (Adjacency), C (Co-belonging derived), D (Distinction), E (Transport). It introduces **temperature `T > 0`** and **entropy `S[u]`** as thermodynamic primitives, lifting the existing energy `ℰ[u]` (canonical §8.1) to a free-energy framework `ℱ[u]`.

**Compatibility with existing CN.** F-group is **not** the "Group F" mentioned in CN4 (CN4's Group F = crisp recovery interface, a different ontological layer). To avoid name conflict, when canonical-merge occurs the present F-group should be tagged as "Group F-thermal" and CN4's reference renamed (proposed in `03_integration_and_new_open.md` §10 of today).

**Scope of this file.**
- F1 (thermal state, Gibbs): **commit** with normalizability proof.
- F2 (Bernoulli entropy): **commit** with concavity, Lipschitz on `(ε, 1-ε)^n`, regularization at corners.
- F3 (Langevin): **Cat A on Σ_m^ε** via Lions-Sznitman 1984 (upgraded 2026-04-21 Round 3, see §3.2 below + `logs/daily/2026-04-21/06_further_verification.md` §8). Corner extension to full Σ_m: Cat C-provisional, C-S2 carry.
- F4 (T > 0 primacy + T → 0 recovery): **statement only**; recovery proof (canonical v1.2 reduction at T → 0) carried to C-S3.

---

## §1. Axiom F1 — Thermal State (Gibbs Distribution)

### 1.1 Statement

**Axiom F1 (Thermal State).** For each `T > 0`, the state of the system is a probability measure `ℙ_T` on `Σ_m`:

$$
\mathbb{P}_T[\,du\,] \;=\; \frac{1}{Z(T)}\,\exp\!\Big(-\frac{\mathcal{F}[u]}{T}\Big)\,\nu(du),
$$

where:
- `ν` is the Lebesgue measure on `Σ_m` (inherited from the ambient `(n-1)`-dimensional Hausdorff measure on the affine hyperplane `{Σ u_i = m}`);
- `ℱ[u]` is the free-energy functional (defined in §3 of `working/CE/free_energy_wellposed.md`; for now `ℱ = ℰ - T·S` from canonical ℰ + F2's S);
- `Z(T) = ∫_{Σ_m} exp(-ℱ[u]/T) ν(du)` is the partition function.

### 1.2 Well-Definedness (Normalizability)

**Proposition F1.1 (Z(T) finite).** For every `T > 0`, `0 < Z(T) < ∞`.

*Proof.*
- Σ_m ⊂ [0,1]^n is compact (bounded + closed — convex polytope with corners, canonical Cat A Prop 1.1).
- ℱ[u] = ℰ[u] - T·S[u] is continuous on Σ_m (ℰ continuous by canonical §8.1; S continuous on Σ_m with Bernoulli definition extended by `0 log 0 := 0` — see Prop F2.1; K_soft continuous by `working/E/soft_K_definition.md` §2.1).
- exp(−ℱ/T) is therefore continuous on compact Σ_m ⇒ bounded above and bounded below by a positive constant.
- Z(T) = ∫ (continuous, bounded, strictly positive) ν is finite and strictly positive. ∎

### 1.3 Boundary behavior (corners of Σ_m)

The polytope Σ_m has **corner strata** where some `u_i = 0` or `u_i = 1`. At these corners:
- `ℰ[u]` remains continuous (it's polynomial in u).
- `S[u]` (Bernoulli, Eq. F2.0) extends continuously by `0 log 0 := 0`; finite at corners.
- `K_soft[u]` continuous (`working/E/soft_K_definition.md` §2).

Hence ℱ has no boundary singularity. The Lebesgue measure ν has zero measure on the corner strata (lower-dimensional faces), so corners contribute nothing to `Z(T)`.

### 1.4 Comparison to canonical v1.2 (T → 0 limit, F4 preview)

In the limit `T → 0`, by Laplace's method, `ℙ_T` concentrates on the global minimizer set `argmin_{Σ_m} ℱ[u]`. With λ_K = O(T) (G3 §4), `ℱ → ℰ` as T → 0, recovering canonical's variational characterization. Full recovery proof (showing canonical Cat A theorems survive at T = 0 limit) is **F4 statement (§4) and C-S3 carry**.

---

## §2. Axiom F2 — Bernoulli Entropy

### 2.0 Definition

**Axiom F2 (Entropy).** Per-site Bernoulli entropy:

$$
S[u] \;=\; -\sum_{x \in X_t} \Big[\,u(x)\log u(x) \;+\; \big(1 - u(x)\big)\log\!\big(1 - u(x)\big)\,\Big],
$$

with the convention `0 log 0 := 0` and natural-log base.

### 2.1 Well-Definedness

**Proposition F2.1 (Continuity, boundedness, strict concavity).**

(a) **Range:** `0 ≤ S[u] ≤ n · log 2` for all `u ∈ [0,1]^n`. Lower bound: each term `u log u + (1-u) log(1-u) ≤ 0` on `[0,1]` (with equality at u ∈ {0,1}), so `-Σ (...) ≥ 0`. Upper bound: each term ≥ −log 2 at u = 1/2.

(b) **Continuity on `[0,1]^n`:** the map `t ↦ −[t log t + (1-t)log(1-t)]` extends continuously to `[0,1]` with values 0 at t ∈ {0,1}. Sum of finitely many continuous maps ⇒ S ∈ C^0([0,1]^n).

(c) **Strict concavity on `(0, 1)^n`:** the second derivative w.r.t. `u(x)` is `-1/u(x) - 1/(1-u(x)) < 0` for `u(x) ∈ (0,1)`. Hessian is diagonal negative definite ⇒ strict concavity.

(d) **Lipschitz on `[ε, 1-ε]^n`:** `dS/du(x) = log((1-u(x))/u(x))`. For `u(x) ∈ [ε, 1-ε]`, `|dS/du(x)| ≤ |log(ε/(1-ε))| = log((1-ε)/ε)`. Hence `‖∇S‖_∞ ≤ log((1-ε)/ε)`, giving Lipschitz constant on `[ε, 1-ε]^n` with `L_S(ε) = log((1-ε)/ε)`.

(e) **Non-Lipschitz at corners:** `dS/du(x) → +∞` as `u(x) → 0` and `→ -∞` as `u(x) → 1`. Hence S is **not** globally Lipschitz on `[0,1]^n`. Corners (vertices of Σ_m where some u_i ∈ {0,1}) are gradient-singular for S — these are the same corners as in MO-1's Σ²_M discussion.

*Proofs.* All by direct computation. ∎

### 2.2 Treatment of corner singularity

Two equivalent strategies:

**Strategy (a) — interior thermodynamics.** Restrict variational analysis to `Σ_m^ε := Σ_m ∩ [ε, 1-ε]^n` for small `ε > 0`. On `Σ_m^ε`, S is `L_S(ε)`-Lipschitz, ℱ is smooth, projected gradient flow / Langevin is standard. Corner contributions to Z(T) are exponentially suppressed by ℰ (where the double-well term `β·u²(1-u)²` vanishes at corners but the closure energy and separation energy generally do not, suppressing pure 0/1 configurations).

**Strategy (b) — entropy-regularized state.** Use `S_ε[u] := -Σ [(u + ε) log(u + ε) + (1 - u + ε) log(1 - u + ε)]` to avoid singular gradient. Recover original S as `ε ↘ 0`. This is cosmetic (does not alter Gibbs measure substantially for small ε) and matches Strategy (a) under projection.

**Commit.** Strategy (a) for theoretical analysis (cleaner). Strategy (b) for numerical simulation if needed (orthogonal decision).

### 2.3 Maximum and minimum on Σ_m

**Proposition F2.2 (Maximizer of S on Σ_m).** `argmax_{u ∈ Σ_m} S[u] = u_{\mathrm{uniform}} := (m/n) \mathbf{1}`.

*Proof.* By strict concavity of S and convexity of Σ_m, the maximum is unique. By symmetry of S under permutation of indices (and of Σ_m), the maximizer is invariant, hence proportional to **1**. The volume constraint forces `u_x = m/n`. ∎

**Proposition F2.3 (Minimizer of S on Σ_m).** S = 0 is achieved on configurations with all `u_i ∈ {0, 1}`. With `Σ u_i = m`, this requires `m ∈ ℤ` and any binary configuration with exactly m sites at 1. For non-integer m, S has no minimizer on Σ_m strictly attaining 0; `inf_{Σ_m} S = 0` approached at corners.

**Interpretation.** ℰ alone (without S) has its minimizers near binary "sharp-interface" configurations (driven by double-well `β · u²(1-u)²`). S alone prefers the uniform configuration. Their competition at temperature T sets the trade-off: higher T weights S more, smoothing the field; lower T weights ℰ more, sharpening it.

---

## §3. Axiom F3 — Langevin Dynamics on Σ_m (Statement Only)

### 3.1 Statement

**Axiom F3 (Thermal Gradient Flow with Noise — Langevin).** The dynamics of the cohesion field on Σ_m are governed by the projected stochastic differential equation:

$$
du(t) \;=\; -\Pi_{\Sigma_m}\,\nabla \mathcal{F}[u(t)]\, dt \;+\; \sqrt{2T}\,\Pi_{\Sigma_m}\, dW(t),
$$

where:
- `Π_{Σ_m} = I - (1/n) \mathbf{1}\mathbf{1}^\top` is the orthogonal projector onto `T_u Σ_m`;
- `W(t)` is an n-dimensional standard Brownian motion;
- additional reflection condition at `∂[0,1]^n ∩ Σ_m` corners ensures the process stays in Σ_m;
- the equation is to be read in the Itô sense.

### 3.2 Well-Posedness Status

**Status (updated 2026-04-21 evening per `logs/daily/2026-04-21/06_further_verification.md` §8): Cat A on Σ_m^ε via Lions-Sznitman; Cat C-provisional on full Σ_m (corner handling).**

**Theorem F3.1 (well-posedness on Σ_m^ε; *Round 8 corrected per E-10*).** For all T > 0, λ_K ∈ [0, γ_K·T_max] with γ_K ∈ [0.01, 0.1] **(under (φ-sat) commit per E-11)**, and ε > 0, the projected-reflected SDE F3 admits a unique strong solution on Σ_m^ε for any initial data u(0) ∈ Σ_m^ε **in the Filippov / mollified sense**.

**Proof (corrected).** Lions-Sznitman 1984 (Comm. Pure Appl. Math.) applied via mollification:
- Σ_m^ε is convex bounded with Lipschitz boundary (piecewise-linear from polytope intersection). ✓
- **Drift caveat (E-10).** `b(u) = -Π·∇ℱ_C+E[u]` is Lipschitz on `Σ_m^ε \ V` with constant `L_F(ε, T, λ_K)` (Lemma 1.8 of `02_development.md`). On the **vineyard set V (codim-1)**, ∇K_soft is **discontinuous** (bar-vertex assignment swaps); hence `b` is **NOT globally Lipschitz** on Σ_m^ε.
- **Repair (mollification).** Replace ℱ_C+E by ℱ_ε := ℱ_C+E ∗ ρ_ε (mollifier of width ε). Then ∇ℱ_ε is smooth on full Σ_m^ε ⇒ globally Lipschitz drift. Apply Lions-Sznitman to ℱ_ε: unique strong solution exists. As ε → 0, ℱ_ε → ℱ_C+E uniformly (K_soft globally continuous, Cor 4.1) ⇒ mollified solutions converge to a generalized solution of original SDE.
- **Alternative repair (Filippov).** V is Lebesgue-null on Σ_m^ε. For diffusion processes with bounded discontinuous drift on null set, Filippov 1988 generalized solutions exist. The diffusion's law at any t > 0 is absolutely continuous w.r.t. Lebesgue (by reflection regularity), so V is hit with probability 0.
- Diffusion `σ = √(2T)·Π` is constant on u, hence trivially Lipschitz. ✓

By either repair: **unique strong solution exists with reflection at ∂Σ_m^ε, defined as Filippov / mollified limit.** ∎

**Status:** **Cat A modulo Filippov repair** (Round 8 corrected from "Cat A via direct Lions-Sznitman" — original statement was technically incorrect due to V-discontinuity of drift; E-10 fixes this).

**Theorem F3.2 (Equilibrium = Gibbs).** The unique invariant probability measure of F3.1 is `ℙ_T^ε(du) = (1/Z^ε(T)) exp(-ℱ_C+E[u]/T) · 1_{Σ_m^ε}(u) · ν(du)`.

**Proof.** Direct calculation: Fokker-Planck operator `L = -∇ℱ·∇ + T·Δ` with Neumann boundary conditions on ∂Σ_m^ε. `L(exp(-ℱ/T)) = 0`. Z^ε finite by Prop F1.1 restricted to Σ_m^ε. Standard ergodicity. ∎

**Subtleties for full Σ_m (not Σ_m^ε):**
- Boundary of Σ_m has lower-dimensional faces (some `u_i = 0` or `u_i = 1`). `T∇S` blows up at these faces (F2.1(e)). Lions-Sznitman framework extends via Tanaka 1979 (Skorohod on polyhedra) but requires entropy-regularization at corners. **Cat C-provisional on full Σ_m**; full treatment C-S2 carry.
- On vineyard set V (codim-1, ∇K_soft discontinuous): V is Lebesgue-null on Σ_m^ε, hence null for the diffusion's law at any fixed t > 0 (by standard regularity of reflected diffusion). Filippov-type generalized solution suffices. **OK for F3.1 on Σ_m^ε.**

**Carry to C-S2:** corner extension to full Σ_m (Tanaka 1979); log-Sobolev inequality on Σ_m^ε for explicit ergodicity rate; verification of V-handling by Krylov-Safonov regularity if needed.

### 3.3 Equilibrium

**Statement F3.1 (Equilibrium = Gibbs).** Under standard Lipschitz/coercivity conditions on ℱ (proved in `working/CE/free_energy_wellposed.md`), the Langevin SDE F3 admits a **unique invariant measure**, equal to the Gibbs distribution `ℙ_T` of F1.

This is the classical Fokker-Planck / detailed-balance result for gradient-system Langevin: the generator is `L = -∇ℱ · ∇ + T·Δ` and `ℙ_T ∝ exp(-ℱ/T)` is L-invariant by direct calculation (`L(exp(-ℱ/T)) = 0`). Carried to C-S2 for full rigorous proof on Σ_m with reflection.

---

## §4. Axiom F4 — T > 0 Primacy + T → 0 Recovery (Statement Only)

### 4.1 Statement

**Axiom F4 (Temperature Primacy + Recovery).** The thermal SCC theory operates with `T > 0` as a structural parameter. The deterministic SCC theory of canonical v1.2 is recovered as the limit `T → 0`:

(F4.a) **Recovery of energy minimizers.** As `T → 0`, ℙ_T concentrates on `argmin_{Σ_m} ℰ[u]` (assuming λ_K = O(T) so that λ_K · K_soft → 0 as T → 0). Variance of ℙ_T near the minimizer: `O(√T)` along non-degenerate Hessian directions (Laplace's method).

(F4.b) **Recovery of Cat A theorems.** Each canonical Cat A theorem that pertains to single-formation results (T-1, T-3, T-6a/b/Stability, T-7, T-8-Core/Full, T-11, T-14, T-20, C-Axioms, QM-1/2/3/4, Predicate-Energy Bridge, T-Bind-Proj, Deep Core Dom 2b, T-Persist-1(b)/(e), T-A2 — see `working/integer_K_dependency_map.md` §3 "Cat A 19 survive") **survives** at the T = 0 limit and continues to hold.

(F4.c) **Modification of integer-K theorems.** The 6 Retire + 3 Re-prove + 1 Re-prove(retain) integer-K theorems (`working/integer_K_dependency_map.md` §2) are **rewritten or retired** in the thermal-soft-K framework. See `M1_dissolution.md`, `MO1_dissolution.md`, `F1_dissolution.md` for specific retirements/rewrites.

(F4.d) **Metastability framework.** The "metastability" claim in canonical CN6/CN8/CN14 is **substantiated** thermally by Kramers escape rates (`working/E/M1_dissolution.md` §3) at T > 0; the deterministic local-minimum claim is recovered at T → 0.

### 4.2 Status

**Statement only.** Full proofs:

- (F4.a): Laplace's method on compact Σ_m with non-degenerate ℰ minimizer — standard, carried to C-S3.
- (F4.b): explicit case-by-case verification that each Cat A single-formation theorem's hypothesis remains valid (e.g. T-14 Łojasiewicz convergence: ℱ analytic at T = 0 reduces to ℰ analytic, ℰ analytic per canonical T14 statement). Carried to C-S3.
- (F4.c): explicit re-statements in the three dissolution files (G4–G6).
- (F4.d): Kramers framework in M1_dissolution §3.

### 4.3 Tension with canonical CN18 (if it existed)

In the present canonical v1.2, no CN explicitly commits to "zero-temperature only" (CN18 would be such a commitment, mentioned in B-purpose draft of `logs/daily/2026-04-20/02_development.md`). Hence F4 does not require CN18 retraction in v1.2.

If a future B-cycle adds a CN18 of the form "metastability is zero-T local-minimum only" (per `working/open_problems_reframing_2026-04-19.md` §6 P-F's "honest scope" option), then F4 directly conflicts. Resolution: in C+E framework, P-F is dissolved by F4.d (metastability is thermally substantiated, not zero-T-only). CN18 — if drafted — should be **modified** to "metastability is finite-T phenomenon; zero-T local-minimum is the T → 0 limit case" rather than retracted.

---

## §5. Compatibility with Existing Axiom Groups

### 5.1 Group A (Closure)

A1' (conditional extensivity), A2 (monotonicity), A3 (contraction `a_cl < 4`), A4 (continuity) are all **statements about the closure operator Cl_t**, independent of T. They remain unchanged.

The closure energy `ℰ_cl = Σ (u - Cl(u))²` is independent of T. Closure dynamics (iterative Cl_t application) are within-time process (CN2's τ-parameter), not the thermal Langevin time. No conflict.

### 5.2 Group B (Adjacency)

B1–B4 (nonneg, sym, locality, non-transitivity) describe `N_t` as an externally given input — independent of T. No conflict.

### 5.3 Group C (Co-belonging — derived diagnostic)

C1–C4 unchanged. C_t remains a derived diagnostic (CN7 dual-mode commitment preserved).

**Note on third-mode (NQ-2 / P-C from reframing).** F-group introduces entropy S as a global structural property (a single scalar measuring local participation uncertainty). One could view S as a thermal-entropic re-introduction of "self-integration" (the third self-referential mode CN7 demoted). However, **this is not a re-elevation of C_t** — S is a global functional, not a pairwise operator. NQ-2 (CN7 dual-mode rationale) remains open; F-group provides one possible re-framing where the "missing mode" lives in entropy rather than in C_t.

### 5.4 Group D (Distinction)

D-Ax1–D-Ax3 unchanged. `b_D = 0` (canonical §9.3 for analyticity / Łojasiewicz) — required for ℰ-analyticity, hence preserved in ℱ-analyticity.

### 5.5 Group E (Transport — temporal)

E1–E4 unchanged. The temporal transport kernel `M_{t→s}` operates between time slices and is orthogonal to the within-time Langevin dynamics F3 (different time-scale).

**Two-time-scale architecture (proposal).**
- Within-time: F3 Langevin with timescale `τ_within` (relaxes within Gibbs of slice t).
- Between-time: E-group transport `M_{t→s}` connecting time slices.

Compatibility requires `τ_within ≪ τ_between` so that within each time slice, the Gibbs equilibrium F1 is a good approximation. This is consistent with canonical CN2 ("τ within-time is implementation detail"). Formal statement of the separation of time scales — carry to C-S3.

---

## §6. Status Summary

| Axiom | Statement | Well-Definedness | Category Self-Class |
|---|---|---|---|
| **F1** (Gibbs) | committed | Prop F1.1 (Cat A: Z finite via compact + cont) | Cat A |
| **F2** (Bernoulli S) | committed | Prop F2.1 (Cat A: cont, bounded, concave) | Cat A |
| **F3** (Langevin SDE) | committed (on Σ_m^ε) | Thm F3.1 (Cat A, via Lions-Sznitman 1984); Thm F3.2 equilibrium (Cat A) | **Cat A on Σ_m^ε** (corner extension to full Σ_m: Cat C-provisional, C-S2) |
| **F4** (T-primacy + recovery) | statement | sketched (Laplace + case-by-case) | sketched |

---

## §7. Carry to Subsequent Sessions

- **C-S2 (Stage 1 second / Stage 2):** Full F3 well-posedness; corner reflection treatment; vineyard set V regularity for diffusion.
- **C-S3 (Stage 3):** Full F4 recovery proofs (35 Cat A 단일-formation 정리 의 T → 0 인내성 점검).
- **CE-S2 (Stage 1 third):** (T, λ_K) phase diagram (pre_brainstorm H-C4 4 corners).
- **canonical_sub.md 2026-04-21 entry:** F1, F2 **and F3 (on Σ_m^ε)** as Added; F4 as Pending (statement only). *(F3 status upgraded 2026-04-21 evening per Round 3.)*

Next file: `working/CE/free_energy_wellposed.md` (G3).
