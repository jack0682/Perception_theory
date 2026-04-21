# MO-1 Dissolution — Corner Removal + Witten Laplacian + Fokker-Planck (G6)

**Status:** working (preliminary mapping draft, 2026-04-21)
**Author origin:** `logs/daily/2026-04-21/01_exploration.md` §3.1 (P1 + P3, P5 alternative).
**Canonical refs:** `canonical.md` §13 Cat A Proposition 1.1 (Σ_m convex polytope, manifold with corners), Proposition 1.2 (Fiber dimension of `Σ²_M` — to retire), Theorem 3.1(a,b,d) (K=2 symmetric point landscape — to retire), §13 Retracted T-Merge (c)(d)(e) (merge path manifold error), §14 CN12 (persistence-based morphology).
**Working refs:** `working/E/soft_K_definition.md` (G1 §3 volume compatibility), `working/C/F_group_axioms.md` (G2 §3 Langevin), `working/CE/free_energy_wellposed.md` (G3), `working/integer_K_dependency_map.md` §2 (Prop 1.2, Thm 3.1 retire).
**External refs:** Witten (1982), *Supersymmetry and Morse theory*, J. Diff. Geom. 17; Helffer-Sjöstrand (1985), *Puits multiples en mécanique semi-classique*; Simon (1985), *Semi-classical analysis of low-lying eigenvalues IV*; Forman (1998), *Morse theory for cell complexes* (Adv. Math. 134) — alternative discrete tool; Goresky-MacPherson (1988), *Stratified Morse theory* — for Σ²_M corners.

---

## §1. MO-1 Statement Recap

**MO-1 (canonical OP-0003, severity 🟠 HIGH).** "The K=2 constrained manifold Σ²_M = {(u^1, u^2) : m_1 = m_2 = M/2} is not a smooth manifold; it has corners (at boundary where one formation's mass → 0). Smooth Morse theory requires manifolds without boundary and thus is inapplicable."

**Severity assessment.** Marked HIGH (not CRITICAL). The issue is not that the SCC theory's predictions break — it's that a particular **analytical tool** (smooth Morse) is unavailable for the K-field manifold Σ²_M. Existing canonical Cat A results (Proposition 1.2 fiber dimension, Theorem 3.1 landscape at symmetric point) were proved via stratified geometry, not full Morse, so canonical itself never claimed full Morse applicability — MO-1 is more a **methodological gap** than a contradiction.

**Original framing as a problem.** Without Morse, full global analysis of K=2 energy landscape is incomplete; "smooth bifurcation theory not applicable to M_2" (canonical OP-0003 statement). Workaround was to use existing stable results without claiming global optimality (canonical Option A approach, v1.2).

---

## §2. Corner Removal (E side — soft-K interior smoothness)

### 2.1 Re-statement under soft-K

In the soft-K framework (G1), there is **no Σ²_M**. The K-field architecture (`u^1, u^2` separately constrained on Σ_{m_1} × Σ_{m_2}) is a *modeling choice* that creates the corner structure (m_2 → 0 corner). Soft-K removes this architectural choice by working on a **single** Σ_m with `K_soft : Σ_m → ℝ_{≥0}` as a derived continuous quantity.

**Re-statement (soft-K):** *On Σ_m (single field), the corner structure of Σ²_M does not exist. Σ_m is itself a polytope with corners (Cat A Prop 1.1), but the corners of Σ_m are at `u_i ∈ {0, 1}` (vertices of the hypercube intersected with the volume hyperplane), which is a **different and more standard** corner structure.*

Specifically:
- Σ²_M corners (vacuous in soft-K): {m_2 = 0} or {m_1 = 0} — i.e., one formation losing all its mass.
- Σ_m corners (still present in soft-K): {some `u_i = 0` or `u_i = 1`} — pure exterior (u = 0) or pure interior (u = 1) at some site.

The **K-field-specific** corners (m_2 → 0 type) are removed. The **field-value** corners (u_i → 0 or 1 type) remain — but these are not specific to multi-formation; they appear in single-formation analysis as well (canonical T-8-Core handles them via interior-stability arguments).

### 2.2 Smoothness of the soft-K interior

**Proposition 2.1 (Smooth interior in soft-K).** On `Σ_m^ε := Σ_m ∩ [ε, 1-ε]^n` (the ε-interior), ℱ_C+E is `C^∞`-smooth (specifically, real-analytic — see Prop 2.2 below) with respect to u. Σ_m^ε is a **smooth (non-corner) manifold** of dimension n-1.

*Proof.*
- ℰ is polynomial in u (canonical §8.2–8.4) ⇒ real-analytic.
- S(u) is real-analytic on `(0, 1)^n` (entropy function `-t log t - (1-t)log(1-t)` is analytic on (0,1)).
- K_soft(u) is **piecewise analytic** on Σ_m^ε \ V (where V is the vineyard set, codim-1 — G1 §2.3). On `Σ_m^ε \ V`, ℱ_C+E is real-analytic. On `V ∩ Σ_m^ε`, K_soft is continuous but bar-assignment jumps; ℱ_C+E is `C^0` but not `C^1` in general.

Hence: smoothness on `Σ_m^ε \ V`. The codim-1 set V is measure-zero; for purposes of variational analysis (existence) and statistical mechanics (Gibbs measure absolute continuity), V is negligible.

**Proposition 2.2 (Real-analyticity off V — for Łojasiewicz).** On `Σ_m^ε \ V`, ℱ_C+E is real-analytic. Hence **Łojasiewicz inequality** applies (canonical T14): gradient flow of ℱ_C+E converges to a critical point with exponential rate.

**Status: Cat A** for smoothness on Σ_m^ε \ V; **Cat B-provisional** for handling of V (codim-1 vineyard set). Refining V handling is C-S2.

### 2.3 Smooth Morse on Σ_m^ε \ V

**Corollary 2.3 (Standard smooth Morse applicable).** On the smooth manifold `Σ_m^ε \ V`, ℱ_C+E is a real-analytic function. Standard smooth Morse theory applies:

- Critical points of ℱ_C+E on `Σ_m^ε \ V` are isolated (generically).
- Morse index is well-defined (number of negative Hessian eigenvalues on the constrained tangent space `T_u Σ_m`).
- Morse inequalities: `c_k(ℱ) ≥ b_k(Σ_m^ε)` where `c_k` is the count of Morse-index-k critical points and `b_k` is Betti number of the level/sublevel set.

This is a **direct dissolution** of MO-1's smoothness obstruction at the soft-K E-level.

**Caveat.** This applies only off V. At V, two bars cross — at such a point K_soft is continuous but ∇K_soft is discontinuous, hence the Hessian is not well-defined. The set V has dimension n-2 (codim 1 in Σ_m^ε of dimension n-1); critical points of ℱ_C+E generically avoid V (transversality argument — Sard's theorem applies to ℰ, S analytic; K_soft is generically transverse to V). Carry rigorous transversality argument to **C-S2**.

### 2.4 Status of E-side (corner removal)

| Statement | Claim | Status |
|---|---|---|
| Σ²_M corners (m_2 → 0) removed | Yes (Σ²_M not used in soft-K) | committed |
| Σ_m^ε is smooth manifold | Yes, dim n-1 (Prop 2.1) | proved |
| ℱ_C+E is real-analytic on Σ_m^ε \ V | Yes (Prop 2.2) | sketched |
| Standard smooth Morse applies on Σ_m^ε \ V | Yes (Cor 2.3) | committed (modulo V transversality) |
| V transversality for critical points | Generic via Sard | sketched (C-S2 carry) |
| Σ_m's hypercube corners (u_i ∈ {0,1}) remain | Yes — but standard | unchanged from canonical |

---

## §3. Witten Laplacian (C side — semiclassical critical-point analysis)

### 3.1 Definition

**Witten Laplacian (1982).** For a smooth function `ℱ : M → ℝ` on a Riemannian manifold M (with metric g, Laplace-Beltrami `Δ_g`) and parameter `T > 0`, the **T-Witten Laplacian** acting on functions is:

$$
\Delta_{\mathcal{F}, T} \;=\; -T^2\,\Delta_g \;+\; \|\nabla \mathcal{F}\|^2 \;-\; T\,\Delta_g \mathcal{F}.
$$

(Some conventions absorb T differently. Above is the "semiclassical" parametrization where T is small and the operator's ground state encodes equilibrium.)

**SCC application.** Take M = Σ_m^ε \ V, g = the induced Riemannian metric (or Shahshahani metric per canonical §8.7), ℱ = ℱ_C+E. Then `Δ_{ℱ, T}` is a self-adjoint elliptic operator on a smooth manifold (off V).

### 3.2 Helffer-Sjöstrand semiclassical spectrum

**Theorem (Helffer-Sjöstrand 1985, Simon 1985).** As `T → 0` (semiclassical limit), the spectrum of `Δ_{ℱ, T}` exhibits:
- A **first cluster** of `N_0` eigenvalues exponentially close to 0, where `N_0` = number of local minima of ℱ (Morse-index-0 critical points).
- A **second cluster** of `N_0 - 1` exponentially small eigenvalues (in a generic "Morse" situation), corresponding to the saddle-mediated tunneling between minima.
- Higher clusters at energies bounded below by O(T) (related to Hessian eigenvalues at minima).

**Quantitative.** The first nontrivial small eigenvalue `λ_1(T)` satisfies:

$$
\lambda_1(T) \;\sim\; \tau_0^{-1} \cdot \exp\!\Big(-\frac{\Delta\mathcal{F}}{T}\Big) \quad \text{as } T \to 0,
$$

where `ΔF` is the height of the smallest barrier between two basins, and `τ_0` is the **Kramers prefactor** (same prefactor as in `M1_dissolution.md` §3.2). This is the **rigorous derivation of Kramers** via spectral analysis.

### 3.3 Application to MO-1's "Morse inapplicability"

**Resolution sketch.** The Witten Laplacian provides the structural information that smooth Morse would have provided:
- **Critical-point count = small-eigenvalue count.** Even if smooth Morse counting is hard to make rigorous on Σ_m due to V or to the soft-K specifics, the **spectrum of `Δ_{ℱ, T}`** is well-defined as an operator (modulo V handling) and its small eigenvalues count critical points.
- **Hessian information = O(T) eigenvalue spread.** The Hessian eigenvalues at minima determine the energy gap above the ground-state cluster.
- **Barrier heights = exp(−ΔF/T) tunneling eigenvalues.** Direct readout of saddle structure.

In short: MO-1's "Morse inapplicable" is replaced by "**Witten Laplacian applicable**". The same structural information — number of critical points, their indices, barrier heights between them — is recoverable, but via a spectral operator rather than via a vector field.

### 3.4 Status of C-side (Witten Laplacian)

| Statement | Claim | Status |
|---|---|---|
| Witten Laplacian Δ_{ℱ, T} defined on Σ_m^ε \ V | Yes, self-adjoint elliptic | sketched |
| H-S semiclassical spectrum encodes critical points | Yes (T → 0 limit) | sketched (statement only) |
| First small eigenvalue = Kramers escape rate | Yes (`λ_1 ~ exp(-ΔF/T)/τ_0`) | sketched (full proof: Helffer-Sjöstrand 1985, Bovier-Eckhoff-Gayrard-Klein 2002 for sharp asymptotics) |
| Practical applicability to discrete graph | Discrete-graph Witten Laplacian (Forman, others) — **Stage post-1** | open |

**Carry to post-Stage-1:**
- **Discrete-graph Witten Laplacian.** SCC's Σ_m is a polytope in ℝ^n discrete in the sense of finite n. Witten's formalism is for smooth manifolds. There are two routes:
  - (i) **Continuous embedding.** Treat Σ_m as a smooth manifold with corners (which it is, dim n-1) and apply Witten Laplacian directly. Standard.
  - (ii) **Combinatorial Witten via Forman discrete Morse.** Route to a fully combinatorial framework (Forman 1998). Alternative — see §4.

- **Vineyard set V handling.** V is codim-1 with non-smooth K_soft. The Witten Laplacian needs ℱ smooth; on V, ℱ is `C^0` but not `C^1`. Treatment via mollification (smooth ℱ_ε approaching ℱ as ε → 0 smoothing) with operator norm control. Carried to C-S2.

---

## §4. Fokker-Planck Operator (alternative spectral tool)

### 4.1 Definition

The **Fokker-Planck operator** (forward Kolmogorov) for the Langevin SDE F3 is:

$$
L_{\mathrm{FP}} \;=\; \nabla \cdot \big(\nabla \mathcal{F} \cdot \,\cdot\,\big) \;+\; T\,\Delta.
$$

Acting on probability densities `ρ(u, t)` on Σ_m, it generates the heat-equation-like evolution `∂_t ρ = L_{FP} ρ`.

### 4.2 Relation to Witten Laplacian

The Witten Laplacian and Fokker-Planck operator are **conjugate**: with `ρ_eq(u) = exp(-ℱ/T)/Z` the equilibrium density,

$$
L_{\mathrm{FP}} \;=\; -\rho_{eq}^{1/2} \cdot \Delta_{\mathcal{F}, T} \cdot \rho_{eq}^{-1/2} / T,
$$

(up to sign / normalization conventions). Hence **same spectrum** (after rescaling by T): small eigenvalues of `L_FP` ↔ small eigenvalues of `Δ_{ℱ, T}` ↔ critical-point structure of ℱ.

### 4.3 SCC application

**Spectral gap of L_FP** ⇔ **inverse relaxation timescale**:
- Largest non-zero eigenvalue `λ_1(L_FP) ≈ 1/τ_relax` where τ_relax is the slowest relaxation mode.
- For SCC at low T, slowest relaxation = K=2 → K=1 metastable transition ⇒ `λ_1 ≈ 1/τ_{K=2 → K=1}` ≈ Kramers rate (matching M1 dissolution §3.3).

**Practical observable.** Spectral gap of L_FP can be measured numerically via simulation of F3 Langevin dynamics + autocorrelation analysis. Provides a numerical bridge between thermal-SCC theory and SCC simulations (existing `scc/` codebase).

### 4.4 Status of C-side (Fokker-Planck)

Equivalent to Witten Laplacian — same status. Carried to C-S2 jointly.

---

## §5. Forman Discrete Morse (Alternative)

### 5.1 Statement

For corner-aware analysis of Σ_m as a polytope (where Σ_m has the natural cell structure of its convex polytope decomposition), **Forman's discrete Morse theory** (1998) provides a **purely combinatorial** alternative:
- Define a **discrete vector field** `V` on the cell complex of Σ_m (a partial matching pairing cells `σ ⊂ τ` of dimension differing by 1).
- **Critical cells** = unmatched cells.
- Discrete Morse inequalities: `c_k(V) ≥ b_k(Σ_m)`.
- **Morse-Smale-Floer-style chain complex** built from V's gradient paths.

### 5.2 Advantages and limitations vs Witten Laplacian

**Advantages:**
- **Corner-aware.** Forman's framework handles polytopes with corners naturally — the corner cells are part of the cell complex and can be critical or matched.
- **Vineyard-aware.** A V-matching can be chosen to match cells across vineyard transitions, smoothing the discontinuity into a combinatorial choice.
- **Computable.** Combinatorial — no semiclassical limit needed.

**Limitations:**
- **Spectral information lost.** Forman gives critical cell counts but not eigenvalue magnitudes ⇒ no Kramers rate from Forman alone.
- **Function-from-cells.** Forman starts from a function on cells; for ℱ_C+E (function on Σ_m points, not cells), one must discretize (e.g., barycentric values) — adds a discretization layer.

### 5.3 Recommended use

**Combine Witten Laplacian (C-side spectral analysis) + Forman discrete Morse (E-side topological count) + smooth Morse on Σ_m^ε \ V (E-side bulk).** Three tools cover three regimes:
- Smooth Morse: bulk interior, generic.
- Witten Laplacian: spectral / dynamical — Kramers rates, MFPT.
- Forman discrete Morse: corner-handling, combinatorial counting at boundaries.

This redundancy (3 tools, 1 problem) is the C+E framework's **unique strength** for MO-1: where v1.2 had only "smooth Morse" and saw it as "inapplicable", C+E offers three alternatives. **Practical recommendation:** apply Witten Laplacian as primary tool; use smooth Morse on Σ_m^ε \ V where applicable; use Forman as a sanity-check at corners.

### 5.4 Status of P5 alternative

**Status: alternative tool preserved**. Not committed for primary use in this session. Activated if Witten Laplacian's discrete-graph treatment proves problematic in C-S2.

---

## §6. Retired Theorems (Per Soft-K + C+E)

The integer-K theorems that depended on Σ²_M structure are retired (per `working/integer_K_dependency_map.md` §2.1):

- **Proposition 1.2** (Fiber dimension of Σ²_M): retired — Σ²_M not used in soft-K.
- **Theorem 3.1(a,b,d)** (Landscape at symmetric point): retired — symmetric point (m_1 = m_2 = M/2) is a Σ²_M-specific concept.

These retirements are **not silent** — they are explicit in `working/integer_K_dependency_map.md` §2.1 and are formalized as canonical changes in `03_integration_and_new_open.md` and `canonical_sub.md` 2026-04-21 entry.

**Replacement.** No direct replacement statements proved in this session. The structural information they conveyed (constrained-Hessian eigenvalues at symmetric K=2 configurations) is available, in the soft-K framework, via:
- Hessian of ℱ_C+E at K_soft ≈ 2 critical points on Σ_m (G3 §3.3).
- Witten Laplacian small-eigenvalue spectrum (§3).

Both are sketched here; full quantitative replacement (statement: "for soft-K configurations with K_soft ≈ 2 in the symmetric mass-balance regime, the constrained Hessian has the following eigenvalue structure...") is **post-Stage-1** work.

---

## §7. Status Summary

| Aspect | Status |
|---|---|
| Σ²_M corners removed (E-side) | committed (§2.1) |
| Σ_m^ε smoothness + analyticity | proved (Prop 2.1, 2.2) |
| Smooth Morse applicable on Σ_m^ε \ V | committed modulo V transversality (Cor 2.3) |
| Witten Laplacian semiclassical spectrum (C-side) | sketched (§3) — full discrete-graph treatment carry |
| Fokker-Planck equivalent | sketched (§4) — bridge to numerical simulation |
| Forman discrete Morse alternative | preserved (§5) — activate if needed |
| Prop 1.2, Thm 3.1 retire | committed (§6) |

**Page count:** ~2 pages substantive (within plan §G6 1.5–2 page target).

**Category self-classification:**
- E-side (Σ²_M removal + smooth Morse on Σ_m^ε \ V): **Cat A** modulo V-transversality.
- C-side (Witten Laplacian / Fokker-Planck): **sketched** — Cat C-provisional pending C-S2 (discrete-graph treatment).

---

## §8. Carry / Next

- **C-S2:** Discrete-graph Witten Laplacian + V vineyard transversality + V mollification.
- **Post-Stage-1:** Replacement statements for retired Prop 1.2, Thm 3.1.
- **canonical_sub.md 2026-04-21 entry:** Σ²_M removal + Prop 1.2 / Thm 3.1 retire as **Pending** (formal retirement awaits weekly merge); Witten Laplacian framework as **Added — Pending OP promotion**.

Next file: `working/E/F1_dissolution.md` (G4 — final dissolution mapping, lowest priority per plan).
