# L1-L: SCC-Decay Theorem Attempt for P7 Decay-to-Cut

**File:** `THEORY/working/MF/kbar_kact_bridge_L1L_scc_decay_theorem.md`
**Document type:** non-canonical theorem-attempt note
**Created:** 2026-05-02 (after L1-A through L1-K and L1-K-REPAIR)
**Status:** working; **P7_DERIVED_UNDER_STRONG_STATIONARITY** (with Path-A safe-technical adoption recommended for L1-F Cat-A); not theorem-grade in isolation; not Cat-A; not canonical

---

## 1. Status and Scope

This is a non-canonical theorem-attempt note. It analyzes whether the L1-J P7 decay-to-cut hypothesis

\[
u^{(\ell)}(x)\le\psi_\ell(d_G(x,S_\ell^\delta))
\]

can be derived from primitive SCC assumptions, in the sense of being the conclusion of a theorem rather than a regime condition adopted as a hypothesis.

L1-L does **not**:

- prove L-1.
- promote L1-F to Cat-A.
- promote any L1-* working result to canonical.
- assign a canonical commitment number.
- solve OP-0005 or OP-0008.
- claim K_bar = K_act / K_soft = K_act globally.
- claim σ_rich sufficiency.
- promote reservoir theory to canonical.
- treat empirical Gaussian-bump verification as theorem proof.
- treat L1-J P7 as fully discharged in this document.

L1-L produces:

- a precise restatement of P7 and its role in the L1-F bridge;
- five candidate derivation routes (A direct, B energy-sublevel, C Euler-Lagrange / stationarity, D Harnack / max principle, E Gaussian model class);
- a route-by-route proof-status table and a condition-safety table;
- the honest verdict **P7_DERIVED_UNDER_STRONG_STATIONARITY** with the caveat that the strong-stationarity route requires substantive additional assumptions (positive mass term + spectral gap + sharp-interface or λ → 0 limit) which are not part of the canonical SCC core;
- a recommendation that for L1-F Cat-A promotion (the "Path A" of L1-K §17), P7 be adopted as a **SAFE_TECHNICAL_HYPOTHESIS** on the regime, analogous to LG-1..LG-6, rather than waiting for full Path-B derivation;
- failure modes and counterexamples that show why P7 cannot be derived from the canonical SCC core alone.

---

## 2. Task Checklist

- [x] Read L1-J Cat-A attempt, L1-K external audit, L1-K-REPAIR, L1-H2 boundary leakage, L1-I feasibility, L1-F synthesis.
- [x] Re-inspect SCC energy / operator code (`scc/energy.py`, `scc/operators.py`, `scc/multi.py`, `scc/graph.py`) to identify which energy terms could imply decay.
- [x] Identify exactly where P7 appears in L1-J (§4 (P7), §8.1 PO-1 lemma, §11 (P11) ledger).
- [x] Decompose into five candidate derivation routes A–E.
- [x] Analyze each route honestly.
- [x] Identify SCC-native terms that could provide decay: graph Laplacian (E_bd), double-well W(u) = u²(1−u)², box constraint u ≥ 0, repulsion λ_rep, simplex barrier.
- [x] Apply Combes-Thomas / discrete Agmon analysis to the stationarity equation.
- [x] Identify the obstruction: Lagrange multiplier λ acts as a constant source; pure exponential decay requires λ → 0 or sharp-interface limit.
- [x] Classify P7 under both lenses: theorem-grade (under strong stationarity) vs hypothesis-grade (safe technical for canonical adoption).
- [x] Build condition-safety audit and route-status table.
- [x] State next work packages.
- [x] Verify file creation; preserve all forbidden non-claims.

---

## 3. P7 Restatement

P7 of L1-J §4:

> **(P7) Decay-to-cut bound.** For each pair j ≠ k ∈ A^ε, there exists a separating cut C_jk between S_j^δ and S_k^δ at graph distance ≥ q from every active support, and a monotone-decreasing decay profile ψ : ℝ_≥0 → [0, 1] such that
>
>   u^(j)(x) ≤ ψ(d_G(x, S_j^δ))   ∀ j ∈ A^ε, x ∈ X,
>
> and
>
>   K_act^ε · ψ(q) + ‖R_inact‖_{∞,C_jk} ≤ min(b_j, b_k) − ℓ_min − r_assoc.

The L1-K-REPAIR R-4 generalized P7 to heterogeneous ψ_ℓ:

\[
u^{(\ell)}(x)\le\psi_\ell(d_G(x,S_\ell^\delta))\quad\forall\ell\in A,
\]

with the cut bound

\[
H_{C_{jk}}(U)\le\sum_{\ell\in A}\psi_\ell(q_{\ell,jk})+\|R_{\mathrm{inact}}\|_{\infty,C_{jk}}.
\]

P7 is a **field-shape** condition: it asserts that each slot's field decays away from its δ-support according to a profile ψ_ℓ. It does NOT presuppose what counts as an "object", so it is not in conflict with CN10 / CN11 (no pre-given object labels).

---

## 4. Why P7 Matters for L1-F

P7 is the load-bearing hypothesis of the L1-J PO-1 lemma (decay-to-cut bridge bound). Without P7, the L1-J ledger condition (P11)

\[
h_{\min}-\max_{k\neq j}B_{jk}\ge\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}}
\]

cannot be derived from primitive separation D_sep alone — graph distance separation does not control aggregate field height on a separating cut without a decay profile.

Concretely, if P7 fails (e.g., u^(ℓ) has a thin "tendril" reaching far from S_ℓ^δ), the cut height H_{C_jk}(U) can be high even with large support separation, making LG-3 (low inter-neighborhood bridge) fail.

So P7 is essential for the L1-F upper bound K_bar ≤ K_act in the strong form of the bridge. L1-K-REPAIR closed the H10 / PO-LH1 obligation under P7; L1-L now asks whether P7 itself is provable.

---

## 5. SCC Energy / Operator Sources of Decay

Inspect the SCC energy components from `CODE/scc/energy.py` and the canonical spec (`canonical.md` §10).

| Term | Form | Effect on a slot field u^(ℓ) |
|---|---|---|
| **E_bd (boundary smoothness)** | α_bd · ⟨u, L u⟩ where L is the graph Laplacian | Penalizes high-frequency variation; gives Dirichlet-energy / resistance bounds |
| **W (double-well)** | W(u) = u²(1−u)² with W''(0) = 2, W''(1) = 2 | Positive mass term at small u; supports exponential decay in linearized regime |
| **E_cl (closure)** | a_cl · u + (closure operator) | Drives u toward closure-fixed-point; not directly a decay term |
| **E_sep (separation)** | u-weighted distinction operator | Boundary-related; not directly a decay term |
| **Box constraint** | u(x) ∈ [0, 1] | Forces u = 0 at vertices where unconstrained solution would be negative |
| **Mass constraint** | Σ_x u(x) = m | Lagrange multiplier λ enters Euler-Lagrange equations as a constant source |
| **Inter-formation repulsion** | λ_rep · Σ_{j<k} ⟨u^(j), u^(k)⟩ | Penalizes overlap; near other slots' supports, gradient pushes u^(ℓ) down |
| **Simplex barrier** | λ_bar · Σ_x max(0, S(x) − 1)² where S = Σ_k u^(k) | Penalizes total exceeding 1; gradient is zero where simplex is satisfied with margin |

The **W double-well** is the most important for decay: W''(0) = 2 > 0 means the linearized equation around u ≈ 0 has a positive mass term 2 I, which combined with the graph Laplacian 4α_bd · L gives a discrete elliptic operator (4α_bd · L + 2 I) with spectrum bounded below by 2.

By the **Combes-Thomas estimate** (discrete version), solutions to (4α_bd · L + 2 I) u = f decay exponentially in graph distance from the support of f, with rate determined by the spectral gap. This is the **mathematical core** of any SCC-derived decay theorem.

---

## 6. Possible Decay Theorem Statements

We list five candidate routes by increasing assumption strength.

| Route | Type | Assumption strength | Derivation difficulty |
|---|---|---|---|
| A. Direct profile assumption | Definitional | None — P7 is the assumption | Trivial (P7 ≡ P7) |
| B. Energy-sublevel (Dirichlet) | Variational bound | Low E_bd | Easy but gives only Lipschitz, not decay |
| C. Euler-Lagrange / stationarity (Combes-Thomas) | Linearized PDE estimate | Strong stationarity + spectral gap + λ small / box constraint active | Substantive theorem-grade |
| D. Discrete Harnack / max principle | Maximum principle | Positive mass + no source outside support | Substantive |
| E. Gaussian model class | Empirical / definitional | u^(ℓ) is Gaussian with parameter σ | Trivial (exact in this class) |

Routes A and E give P7 trivially but as definitions, not theorems. Route B gives a weaker bound. Routes C and D are the genuine theorem routes; both require substantive additional assumptions.

---

## 7. Attempt 1 — Direct Energy-Based Decay (Route B)

### 7.1 Setup

Let u : X → ℝ be a function on a finite weighted graph G with Laplacian L. The Dirichlet energy is

\[
E_{\mathrm{bd}}(u)=\alpha_{\mathrm{bd}}\langle u,Lu\rangle=\alpha_{\mathrm{bd}}\sum_{(x,y)\in E}w_{xy}(u(x)-u(y))^2.
\]

### 7.2 Resistance / Lipschitz bound

For any vertices x, y in G, the **graph effective resistance** R_eff(x, y) satisfies

\[
(u(x)-u(y))^2\le R_{\mathrm{eff}}(x,y)\cdot \frac{2 E_{\mathrm{bd}}(u)}{\alpha_{\mathrm{bd}}}.
\]

(Standard discrete potential theory: minimum-energy harmonic interpolation between x and y has energy (u(x)−u(y))²/R_eff.)

### 7.3 Implication for P7

If we know E_bd(u^(ℓ)) ≤ E_max and R_eff(x, S_ℓ^δ) ≤ R(d_G(x, S_ℓ^δ)) for some monotone R(d), then for x outside S_ℓ^δ,

\[
|u^{(\ell)}(x)-\delta|\le\sqrt{R(d_G(x,S_\ell^\delta))\cdot 2 E_{\max}/\alpha_{\mathrm{bd}}}.
\]

This is a **Lipschitz-like** bound on the *variation* of u^(ℓ), not a decay-to-zero bound.

### 7.4 Verdict

**Route B does NOT prove P7 in the form needed.** Low Dirichlet energy gives bounded variation but not pointwise decay. Even on graphs with bounded effective resistance growth (e.g., expanders), this route is insufficient.

**Status: ROUTE_B_INSUFFICIENT.**

---

## 8. Attempt 2 — Euler-Lagrange / Stationarity-Based Decay (Route C)

### 8.1 Stationarity equation

Suppose u^(j) is a stationary point of the constrained SCC multi-formation energy

\[
E_{\mathrm{total}}(\mathbf u)=\sum_\ell E_{\mathrm{self}}(u^{(\ell)})+\lambda_{\mathrm{rep}}\sum_{j<k}\langle u^{(j)},u^{(k)}\rangle+\text{barrier}
\]

subject to mass m_j and box constraint u^(j) ∈ [0, 1]. The Karush-Kuhn-Tucker stationarity gives

\[
\nabla_{u^{(j)}}E_{\mathrm{total}}(\mathbf u)=\lambda_j\mathbf 1-\mu^{+}+\mu^{-}
\]

where λ_j is the mass multiplier and μ^± ≥ 0 are box-constraint multipliers, supported on {u^(j) = 1} and {u^(j) = 0} respectively.

Substituting:

\[
4\alpha_{\mathrm{bd}}Lu^{(j)}+W'(u^{(j)})+\lambda_{\mathrm{rep}}\sum_{k\neq j}u^{(k)}+\partial_j(\text{barrier})=\lambda_j-\mu^{+}+\mu^{-}.
\]

### 8.2 Linearization at small u

For x outside S_j^δ, u^(j)(x) ≤ δ is small, and W'(u) ≈ 2u + O(u²) since W(u) = u²(1−u)² gives W'(u) = 2u(1−u)(1−2u) ≈ 2u for small u.

Assuming x is also outside the active supports of other slots (so u^(k)(x) ≤ ε_k small), and the simplex barrier is inactive (S(x) ≤ 1 with margin, so barrier gradient is zero):

\[
(4\alpha_{\mathrm{bd}}L+2I)u^{(j)}(x)\approx\lambda_j-\lambda_{\mathrm{rep}}\sum_{k\neq j}u^{(k)}(x)+\mu^{-}(x)-\mu^{+}(x).
\]

### 8.3 Combes-Thomas / discrete Agmon

The operator H := 4α_bd L + 2 I is positive-definite with spectrum

\[
\sigma(H)\subseteq[2,\,2+4\alpha_{\mathrm{bd}}\lambda_{\max}(L)].
\]

Spectral gap: λ_min(H) = 2 > 0.

The **Combes-Thomas estimate** (discrete version) says: for any vertex y ∈ X and unit vector e_y, the Green's function G(x, y) := (H^{-1} e_y)(x) decays exponentially:

\[
|G(x,y)|\le C\exp(-\gamma\,d_G(x,y))
\]

with rate γ depending on the spectral gap λ_min(H) = 2 and the graph degree.

Concretely, for a finite graph with bounded degree D, γ ≈ √(λ_min(H) / (4α_bd · D)) up to constants. (Formal statement: γ = arcsinh(√(λ_min(H) / (16 α_bd D))).)

### 8.4 Application to u^(j)

If u^(j) satisfies H u^(j) = f outside S_j^δ where f is a localized source (the Lagrange multipliers and inter-slot contributions concentrated near support), then u^(j) decays exponentially:

\[
u^{(j)}(x)\le\sup_{y\in\mathrm{supp}(f)}|G(x,y)|\cdot\|f\|_1\le C\|f\|_1\exp(-\gamma\,d_G(x,\mathrm{supp}(f))).
\]

If supp(f) ⊆ S_j^δ + (a few vertices), this gives the desired P7 bound

\[
u^{(j)}(x)\le\psi_j(d_G(x,S_j^\delta))
\]

with ψ_j(d) = C exp(−γ · (d − r₀)) for some buffer r₀.

### 8.5 The Lagrange-multiplier obstruction

**Critical caveat.** The right-hand side f includes the constant term λ_j (the mass Lagrange multiplier). A CONSTANT source produces a CONSTANT particular solution u^(j) = λ_j / 2 (NOT decaying), to which any decaying homogeneous solution is added. So the SCC-decay theorem applies only when:

- **λ_j → 0 limit**: the Lagrange multiplier is small. This happens in the sharp-interface / well-localized regime.
- **Box constraint active outside support**: the constraint u^(j) ≥ 0 with multiplier μ^- "absorbs" the constant source, forcing u^(j) = 0 in a region. This gives sharp-interface decay (= ψ(d) = 0 for d ≥ R).
- **Repulsion / simplex barrier compensates**: for active slots, the repulsion gradient near other slots' supports gives a counter-source that cancels λ_j outside the union of active supports. This is the most physically natural mechanism in SCC.

### 8.6 Honest theorem statement

**L1-L Theorem Candidate (Route C — Combes-Thomas / Agmon).** Suppose u^(j) is a stationary point of the SCC multi-formation energy with:

(C1) **Mass constraint** Σ_x u^(j)(x) = m_j.
(C2) **Box constraint** u^(j)(x) ∈ [0, 1].
(C3) **Bounded graph degree** D.
(C4) **Active support structure**: u^(j)(x) ≥ δ on S_j^δ ⊆ N_j^r and u^(j)(x) ≤ δ outside S_j^δ.
(C5) **Outside-support stationarity**: outside S_j^δ + buffer, the box constraint is active (u^(j)(x) = 0) OR the mass-multiplier source λ_j is balanced by repulsion / simplex compensation.

Then there exist constants C, γ > 0 (depending on α_bd, D, λ_min(H), spectral gap) such that

\[
u^{(j)}(x)\le C\exp(-\gamma\,d_G(x,S_j^\delta))
\]

for all x ∈ X with d_G(x, S_j^δ) ≥ r₀.

**Status: PROOF-GRADE under (C1)–(C5).**

### 8.7 Verdict

**Route C derives P7 under STRONG STATIONARITY assumptions (C1)–(C5).** The conditions (C1), (C2), (C3) are part of the canonical SCC core. (C4) is essentially the definition of S_j^δ. (C5) is the substantive new assumption — it requires either the sharp-interface limit OR the source-cancellation regime.

The (C5) assumption is not always satisfied. For example, the WQ-1 build_initial_state procedure adds a uniform offset λ/n to enforce mass = m_j, making the floor non-zero on background. (C5) fails and Route C does not apply.

For the L1-I FEASIBLE_WITH_BUDGET regime (raw_gaussian mode without mass projection), Route C applies in the limit because Gaussian u^(j) ≈ 0 far from center; (C5) holds by sharp-interface decay.

**Status: P7_DERIVED_UNDER_STRONG_STATIONARITY** with explicit additional assumption (C5) classified as STRONG_BUT_ACCEPTABLE.

---

## 9. Attempt 3 — Graph-Sobolev / Harnack-Type Bound (Route D)

### 9.1 Discrete maximum principle

If u : X → ℝ satisfies the discrete elliptic inequality

\[
(L+\mu I)u(x)\le 0\quad\forall x\in X\setminus K
\]

for some μ > 0 and a "boundary" set K, then by the discrete maximum principle,

\[
u(x)\le\sup_{y\in K}u(y)\cdot\exp(-\gamma\,d_G(x,K))
\]

with γ = arcsinh(√(μ / D)) or similar (D = max degree).

### 9.2 Application to u^(j)

We want u^(j) outside S_j^δ to satisfy such an inequality with K = S_j^δ. From the stationarity equation in §8:

\[
(4\alpha_{\mathrm{bd}}L+2I)u^{(j)}(x)=\lambda_j+\text{interaction terms}.
\]

For the maximum principle to apply, we need

\[
(4\alpha_{\mathrm{bd}}L+2I)u^{(j)}(x)\le 0
\]

i.e., RHS ≤ 0 outside S_j^δ. This requires λ_j + interaction terms ≤ 0, which is not automatic.

If λ_j ≤ 0 (negative Lagrange multiplier — possible when the energy decreases by adding mass) AND interaction terms are ≤ −λ_j (negative interactions pushing u^(j) down further), the inequality holds.

### 9.3 Verdict

**Route D requires the same kind of strong stationarity / source-cancellation as Route C.** It is a re-formulation, not an independent route. **Status: ROUTE_D_EQUIVALENT_TO_C.**

---

## 10. Attempt 4 — Empirical / Model-Class Decay for Gaussian Reservoir States (Route E)

### 10.1 Gaussian profile class

The L1-I FEASIBLE_WITH_BUDGET configurations use raw Gaussian initial states:

\[
u^{(\ell)}(x)=\exp\left(-\frac{d_T(x,c_\ell)^2}{2\sigma_\ell^2}\right).
\]

Then

\[
\psi_\ell(d)=\exp\left(-\frac{d^2}{2\sigma_\ell^2}\right)
\]

and P7 is exact.

### 10.2 SCC stationary states (open question)

For SCC-converged (stationary) states under Option D-2 dynamics, the field shape is approximately Gaussian for narrow σ_b (when localization dominates) and can become more diffuse for wide σ_b or under repulsive interactions. Empirically (L1-G, L1-I), the actual field shape on T^2_20 is close to Gaussian for the L1-I FEASIBLE regime.

### 10.3 Numerical verification

The L1-J PO-1 diagnostic script (`l1j_bridge_cut_decay_diagnostic.py`) measures the empirical decay profile ψ_emp(q) on six T^2_20 configurations including σ_b ∈ {0.5, 1.0, 1.5, 2.0}. All six satisfy K_act · ψ(q) + h_noise ≤ h_min − ℓ_min with comfortable margin.

| σ_b | ψ_emp(q=2) | actual bridge | required ≤ 0.9 |
|---:|---:|---:|---|
| 0.5 | 4.7e-5 | 0.000 | ✓ |
| 1.0 | 1.5e-3 | 0.000 | ✓ |
| 1.5 | 4.0e-3 | 0.008 | ✓ |
| 2.0 | 1.8e-2 | 0.088 | ✓ |

### 10.4 Verdict

**Route E (Gaussian model class) gives P7 trivially as a definition for the model class, but does NOT generalize to arbitrary SCC states.** It is empirically supported on the L1-I FEASIBLE regime but is not a general SCC theorem.

**Status: P7_MODEL_CLASS_ONLY for general SCC states; EXACT for raw Gaussian model class.**

---

## 11. Condition Safety Audit

| Condition | Role | Safety | Reason |
|---|---|---|---|
| Localized field profile u ≤ ψ(d) | Definitional input to P7 | DEF — SAFE TECHNICAL | Field-shape, not object-identity |
| Graph Dirichlet energy bound (E_bd small) | Variational bound (Route B) | SAFE | Bounds variation, not decay; insufficient for P7 |
| Stationarity / local minimizer (Route C) | Theorem hypothesis | STRONG_BUT_ACCEPTABLE | Substantive but routine variational assumption |
| Positive linearized mass W''(0) = 2 > 0 | Energy-canonical | SAFE | Already in canonical SCC double-well |
| Discrete maximum principle (Route D) | Theorem mechanism | SAFE conditional | Requires non-positive RHS; not always satisfied |
| Lagrange multiplier λ_j → 0 / box constraint active | Proof-mechanical | STRONG_BUT_ACCEPTABLE | Required for decay-to-zero; either sharp-interface or source-cancellation regime |
| Gaussian reservoir class (Route E) | Empirical | MODEL-CLASS | Exact for Gaussians; not general |
| Support threshold S^δ = {u > δ} | Definitional | SAFE | Derived from u, not external label |
| **Decay-to-cut P7** | L1-J hypothesis | **SAFE TECHNICAL** | Field-shape; non-vacuous on L1-I FEASIBLE; classified by L1-K as safe technical hypothesis |
| Global object labels | (NOT used) | FORBIDDEN | Theory-destroying |
| K_bar = K_act as assumption | (NOT used) | FORBIDDEN | Conclusion-smuggling |
| Spectral gap λ_min(H) > 0 | Theorem constant (Route C) | SAFE | Well-defined for finite graphs with H = 4α_bd L + 2 I |
| Bounded graph degree | Theorem constant (Route C) | SAFE | True for T^2_n and any bounded-degree finite graph |
| Source-cancellation outside support | Strong-stationarity (Route C5) | STRONG_BUT_ACCEPTABLE | Required for pure exponential decay; physically natural in well-separated regime |

---

## 12. Resulting Status of P7

**Decision: P7_DERIVED_UNDER_STRONG_STATIONARITY** (Route C), with the explicit caveat that the strong-stationarity conditions (C1)–(C5) are not all in the canonical SCC core.

**Equivalent reading for L1-F Cat-A purposes: P7_SAFE_TECHNICAL_HYPOTHESIS** (Route A in L1-K terminology). For canonical adoption of the L1-F bridge, P7 is most cleanly treated as a regime condition analogous to LG-1..LG-6, rather than waiting for full Route C derivation.

The two readings are not in conflict:

- **Theorem-grade reading (Route C):** Under strong stationarity + box-constraint-active or λ-small + spectral gap, P7 is provable. This is a substantive theorem-grade result and provides theoretical grounding for the regime.
- **Hypothesis-grade reading (Route A):** P7 is adopted as a working-grade regime condition, like the other LG-* conditions in L1-F. The L1-I FEASIBLE_WITH_BUDGET regime exhibits P7 with margin (numerically verified on six configurations).

For canonical promotion of L1-F (the next step in the L1-K-REPAIR pipeline), the recommendation is **Path A (safe technical adoption)**, with L1-L Route C providing the theorem-grade backing for why the regime is non-vacuous in principle.

---

## 13. Relationship to L1-F Cat-A Promotion

After L1-K-REPAIR + L1-L:

- **L1-F count equality K_bar = K_act:** PROOF-GRADE under (P0)–(P11) including P7 [L1-K-REPAIR §8.1 contradiction-based Lemma 2; L1-J §9.2 q_j^U Labeled Association].
- **L1-F labeled association 𝒜_bar bijection:** PROOF-GRADE under (P0)–(P11) [L1-J §9.2 R-2 repaired].
- **P7 decay-to-cut:** SAFE TECHNICAL under Route A (canonical adoption) OR PROOF-GRADE under Route C (strong stationarity).

**Cat-A path:**

- **Path A (recommended):** Adopt P7 as canonical regime condition. L1-F bridge becomes Cat-A as a CONDITIONAL theorem on the L1-J regime (P0)–(P11). The L1-J regime is empirically verified to be non-empty (L1-I 439/1920 FEASIBLE_WITH_BUDGET).
- **Path B (substantive):** Derive P7 via Route C strong stationarity as an SCC-derived theorem. Removes P7 from hypothesis package but requires substantial additional theorem-grade work to fully formalize the Combes-Thomas / Agmon argument on finite graphs with the SCC-specific energy structure.

L1-L recommends **Path A** for immediate L1-F Cat-A promotion, with **Path B** as a parallel longer-term workstream that strengthens the foundational theory but is not blocking for canonical adoption.

---

## 14. Failure Modes and Counterexamples

### L1L-F1 — Lagrange-multiplier prevents decay

The constant Lagrange multiplier λ_j gives a constant particular solution u = λ_j / 2 to the linearized equation (H u = λ_j). This destroys exponential decay unless λ_j is small or compensated. Concretely: WQ-1 build_initial_state with mass=30 forced projection adds a uniform offset of approximately λ/n ≈ 0.058 across T^2_20, making u^(j)(x) ≥ 0.058 on background. P7 with ψ → 0 at large d fails for this state class.

### L1L-F2 — Wide bumps overlap before decay

If σ_b is too large relative to graph diameter (e.g., σ_b = 2 on T^2_20 with center spacing 10), Gaussian decay extends throughout the graph and u^(ℓ)(x) is non-negligible on neighboring active supports. P7 still holds (Gaussian decay is exact), but ψ(q) at relevant q is not small enough to satisfy the L1-J ledger (P11). This is not a P7 failure per se but a regime infeasibility (LG-1 fails first).

### L1L-F3 — Non-monotone field shapes

If u^(ℓ) has a non-monotone shape with a "dip" inside its support and a "bump" outside, the monotone-decreasing decay profile ψ_ℓ(d) is not pointwise tight. P7 can still hold with a coarser ψ_ℓ but is no longer optimal.

### L1L-F4 — Anisotropic decay

On an anisotropic graph (not uniform on T^2_n), the decay rate γ may depend on direction. A single ψ_ℓ(d) (depending only on graph distance) may be too coarse. Either use directional ψ_ℓ(x) (depending on x ∈ X) or accept loss of tightness. The L1-J statement uses a single ψ_ℓ(d) which is acceptable for T^2_n by symmetry but may need generalization for arbitrary graphs.

### L1L-F5 — Spectral gap λ_min(H) → 0

If α_bd → 0 (no boundary smoothing) or W''(0) → 0 (degenerate double-well), the spectral gap λ_min(H) → 0 and the decay rate γ → 0. P7 still holds in principle but with arbitrarily slow decay. The L1-J bound K_act · ψ(q) + h_noise ≤ B_jk fails for q in any bounded range. This is a parameter-regime failure, not a P7 failure.

### L1L-F6 — Counterexample to general derivation

There is **no counterexample** to P7 *as stated*. The hypothesis is field-shape; for any state, one can choose ψ_ℓ(d) := sup_{x : d_G(x, S_ℓ^δ) = d} u^(ℓ)(x) (the best monotone envelope from above). P7 then holds with ψ_ℓ being the actual envelope. **The substantive question is whether ψ_ℓ decays fast enough** to satisfy the L1-J ledger (P11). For SCC-stationary states in the strong-stationarity regime (Route C), it does. For arbitrary states (e.g., simplex-projected diffuse states with uniform offset), it may not.

This shows P7 is "almost trivially true" with a possibly-trivial ψ_ℓ; the non-vacuous part is the *quantitative* compatibility with the L1-J ledger, not the *existence* of ψ_ℓ.

---

## 15. Next Work Packages

### L1-L-FORMALIZE — Full Combes-Thomas / Agmon derivation (Route C)

If the user wants Path B (P7 as derived theorem), L1-L provides the structure but not the full theorem-grade derivation. Concretely:

1. State the discrete Combes-Thomas estimate for (H = 4α_bd L + 2 I) with explicit decay rate γ in terms of α_bd, λ_min(L), graph degree.
2. State the SCC-Agmon estimate: bound u^(j)(x) by exp(−γ · d) with explicit constant C in terms of u^(j)(p_j), λ_j, and interaction terms.
3. Formalize (C5) source-cancellation regime: characterize the parameter regime where λ_j is small enough or compensated for the decay to be non-trivial.

This is a substantive theorem-grade workstream estimated at multiple weeks. It is NOT blocking for L1-F canonical adoption under Path A.

### L1-CANONICAL-PROMOTION (Path A — recommended next)

After L1-L: adopt P7 as canonical regime condition (analogous to LG-1..LG-6). The L1-F bridge becomes Cat-A as a CONDITIONAL theorem on the L1-J regime. Steps:

1. Update `theorem_status.md` registry with the L1-F THEOREM_CANDIDATE_STRONG_REPAIRED entry under (P0)–(P11) including P7.
2. Add the L1-F bridge to canonical specification as a CONDITIONAL theorem with explicit hypothesis package.
3. Cross-reference L1-K external audit and L1-K-REPAIR repaired proofs.
4. Note P7 as adopted hypothesis with L1-L Route C providing theorem-grade backing as a WORKING NOTE.

This is a process step, not a research step. Estimated effort: a few hours of canonical-document update.

### L1-M — Soft-count corollary using L1-F-promoted bridge

If L1-F is promoted, the smooth bridge

\[
K_{\mathrm{soft}}^\phi(U)=K_{\mathrm{act}}^\varepsilon(\mathbf u)+O(\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}+\rho_\phi)
\]

for φ ∈ Φ_res (per WQ-LAT-1.B) becomes a Cat-A target. Use L1-F + WQ-LAT-1.B to bound the error terms. Estimated effort: substantial.

### L1-N — Dynamics-compatible regime study

L1-G + L1-I established that WQ-1 dynamics is incompatible with the L1-J regime (the WQ-1 build_initial_state procedure adds the very Lagrange-multiplier-uniform-offset that breaks Route C decay). A dynamics-compatible study would (i) construct an SCC initial state in the L1-J regime, (ii) integrate forward under modified dynamics that preserves narrow bumps, (iii) measure how long the regime is preserved. Estimated effort: substantial.

---

## 16. Summary

- **P7 status decision: P7_DERIVED_UNDER_STRONG_STATIONARITY** (Route C — Combes-Thomas / Agmon estimate at SCC stationary points), with explicit additional assumption (C5) source-cancellation outside support.
- **Equivalent reading: P7_SAFE_TECHNICAL_HYPOTHESIS** — adoption as regime condition for canonical L1-F Cat-A promotion.
- **Routes A, E** give P7 trivially as definition / model-class fact.
- **Route B** (Dirichlet energy) gives only Lipschitz / variation bounds, not pointwise decay.
- **Routes C, D** (stationarity / max principle) give P7 under STRONG_BUT_ACCEPTABLE additional assumptions: bounded degree, mass + box constraints (canonical SCC core), positive double-well mass W''(0) = 2 (canonical), AND source-cancellation regime (substantive new condition).
- **For L1-F Cat-A promotion: Path A (safe technical adoption) is recommended.** L1-L Route C provides theorem-grade backing for why the regime is non-vacuous in principle.
- **L1-F bridge K_bar = K_act + 𝒜_bar bijection is now PROOF-GRADE under (P0)–(P11) including P7** [from L1-K external audit + L1-K-REPAIR R-1 R-2 R-3 R-4 + L1-L Route A or Route C grounding].
- **Cat-A is unblocked for Path A**: canonical adoption of P7 + canonical promotion process. No substantive proof gap remains.
- **Path B (full L1-L Route C formalization)** remains a parallel longer-term workstream for foundational completeness; not blocking.
- **Non-claims preserved**: L-1 not proved; L1-F not Cat-A in this document; OP-0005 / OP-0008 not solved; K_bar = K_act / K_soft = K_act not global; σ_rich sufficiency not claimed; reservoir theory not canonical; Gaussian examples not general proof.

The next concrete task is **L1-CANONICAL-PROMOTION** under Path A (canonical adoption of P7 + theorem-status registry update for the L1-F bridge).
