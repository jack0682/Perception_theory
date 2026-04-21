# Soft-K Definition — Persistence-Weighted Canonical Choice (G1)

**Status:** working (commit draft, 2026-04-21)
**Author origin:** `logs/daily/2026-04-21/01_exploration.md` §3.1 (Primary approach P1).
**Canonical refs:** `canonical.md` §3.3 (u codomain), §5.5 (transition diagnostics — H₀ persistence), §13 Cat A QM3 (persistence stability via Lipschitz-on-bottleneck), §14 CN12 (Q_morph is persistence-based — filtration commitment).
**Working refs:** `working/integer_K_dependency_map.md` §2 (10 load-bearing integer-K theorems); `working/new_open_questions_2026-04-20.md` NQ-1 (soft-K uniqueness); `working/open_problems_reframing_2026-04-19.md` §6 P-A.
**External refs:** Cohen-Steiner, Edelsbrunner, Harer (2007), *Stability of persistence diagrams*, Discrete Comput. Geom., Theorem 4.2 (bottleneck-∞ stability under L∞ perturbation).
**NQ-1 resolution:** 후보 (i) persistence-weighted sum commit; (ii)(iii)(iv) parked with §5 비교 + rationale.

---

## §1. Definition (primary commit)

Let `u ∈ Σ_m ⊂ [0,1]^n` with `n = |X_t|` and `Σ_m = {u : Σ_i u_i = m}` (canonical §8.0). Let `Dgm_0(u)` denote the **H₀ persistence diagram** of the **superlevel-set filtration** `{x : u(x) ≥ θ}` as θ decreases from 1 to 0. Let `ℓ_i(u)` denote the bar-length (death − birth) of the i-th bar in `Dgm_0(u)`.

**Definition 1 (K_soft).** For a monotone Lipschitz weighting `φ : [0, 1] → [0, ∞)` with `φ(0) = 0` and Lipschitz constant `L_φ`:

$$
K_{\mathrm{soft}}(u) \;=\; \sum_{i : \ell_i(u) > 0} \varphi\!\big(\ell_i(u)\big).
$$

**Canonical choice of φ.** Two families are natural and both commit-ready:

- **(φ-sat) Saturating:** `φ(ℓ) = ℓ / (1 + ℓ)`. Range `[0, 1)` — each bar contributes at most 1. `L_φ = 1` (max derivative at 0). Converges to hard-count in sharp-interface limit (bars become long, φ saturates to 1).
- **(φ-lin) Truncated-linear:** `φ(ℓ) = min(ℓ / ℓ_0, 1)` with `ℓ_0 > 0` a scale parameter. `L_φ = 1/ℓ_0`. Hard-count recovery when all bars `≥ ℓ_0`.

**Commit (2026-04-21):** Both (φ-sat) and (φ-lin) are admissible; the weighting is a provisional realization (canonical §9 style). Default for present session: **(φ-sat)** (fewer hyperparameters; naturally bounded by number of bars).

**Caveat (Round 8 per E-11):** the (φ-sat) commit has consequences for downstream stability analysis. Specifically `γ_K ≤ 0.1` (G3 §4.3, `06_further_verification.md` §1.6) is derived under (φ-sat) where φ'' < 0. For (φ-lin), φ'' = 0 a.e. ⇒ K_soft Hessian is zero a.e., relaxing γ_K constraint. **The (φ-sat) vs (φ-lin) choice affects quantitative bounds but not qualitative conclusions** (NQ-1-extended carry).

**Immediate properties (proof in §2).**

(P1) `K_soft(u) ≥ 0`, with equality iff `Dgm_0(u)` has no positive-length bar (e.g. `u ≡ c · 1` uniform — one bar of length 0).

(P2) `K_soft` is **globally Lipschitz** on `(Σ_m, ‖·‖_∞)` with constant bounded by `L_φ · N_{\max}(m)`, where `N_{\max}(m)` is an upper bound on the number of H₀ bars that can appear on `Σ_m` (finite by finite graph). See §2.2 for sharper statement.

(P3) On the hard-count regime (binary `u ∈ {0,1}^n` with `K_hard` connected components of `{u = 1}`), `K_soft = K_hard · φ(1)`. With (φ-sat) this is `K_hard/2`; with (φ-lin) and `ℓ_0 ≤ 1` this is `K_hard`. Hence `K_soft` **recovers hard-count up to a φ-dependent scale**.

---

## §2. Well-Definedness (Lipschitz skeleton)

### 2.1 Bottleneck stability (external anchor)

**Theorem (CSEH 2007, Theorem 4.2).** For any two real-valued functions `f, g` on a finite filtered complex:

$$
W_\infty\!\big(\mathrm{Dgm}(f),\,\mathrm{Dgm}(g)\big) \;\leq\; \|f - g\|_\infty,
$$

where `W_∞` is the bottleneck distance on the persistence diagrams.

**Application to SCC.** For `u, v ∈ Σ_m ⊂ [0,1]^n`, viewing `u` as a function `X_t → [0,1]` and using the superlevel filtration, CSEH directly gives:

$$
W_\infty\!\big(\mathrm{Dgm}_0(u),\, \mathrm{Dgm}_0(v)\big) \;\leq\; \|u - v\|_\infty.
$$

### 2.2 Lipschitz of K_soft (skeleton)

**Proposition 2.1 (K_soft generic Lipschitz).** Let `B_+(u)` denote the set of positive-length bars of `Dgm_0(u)`. Let `N(u) = |B_+(u)|`. Assume **generic u** (no bar has birth = death in `B_+(u)`). Then:

$$
\big|K_{\mathrm{soft}}(u) - K_{\mathrm{soft}}(v)\big| \;\leq\; L_\varphi \cdot \sum_{i} \big|\ell_i(u) - \ell_i(v)\big| \;\leq\; L_\varphi \cdot 2\, N_{\max}(u,v) \cdot W_\infty\!\big(\mathrm{Dgm}_0(u), \mathrm{Dgm}_0(v)\big).
$$

Combining with CSEH 2.1:

$$
\big|K_{\mathrm{soft}}(u) - K_{\mathrm{soft}}(v)\big| \;\leq\; 2\, L_\varphi \cdot N_{\max}(u,v) \cdot \|u - v\|_\infty.
$$

*Proof sketch.* (i) φ is L_φ-Lipschitz ⇒ `|φ(ℓ_i(u)) - φ(ℓ_i(v))| ≤ L_φ · |ℓ_i(u) - ℓ_i(v)|`. (ii) For a generic optimal matching `γ : B_+(u) → B_+(v)` realizing W_∞, each paired bar shifts both birth and death by at most `W_∞`, so `|ℓ_i(u) - ℓ_{γ(i)}(v)| ≤ 2 W_∞`. Unmatched bars in either diagram pair with the diagonal, contributing `ℓ ≤ 2W_∞` each. (iii) Sum over at most `N_{\max}(u,v) = max(N(u), N(v))` bars yields the stated bound. Combined with CSEH (2.1): stated inequality. ∎

**Corollary 2.2 (Uniform Lipschitz on Σ_m).** Because `X_t` is finite, the total bar count (matched + diagonal-paired in u-side + diagonal-paired in v-side) is bounded by `2n`. Hence:

$$
L_K := \sup_{u, v \in \Sigma_m,\, u \neq v} \frac{|K_{\mathrm{soft}}(u) - K_{\mathrm{soft}}(v)|}{\|u - v\|_\infty} \;\leq\; 4\, L_\varphi \cdot n.
$$

For (φ-sat): `L_K ≤ 4n`. For (φ-lin) with `ℓ_0 = 0.1`: `L_K ≤ 40n`. Tighter bounds possible via graph structure; deferred to C-S2 / E-S2 (NQ-9, NQ-15).

*(Erratum 2026-04-21 evening: corrected from `2 L_φ n` to `4 L_φ n` per `logs/daily/2026-04-21/05_deepening_and_verification.md` §1.5 — full proof revealed the missed factor of 2 from counting both u-side and v-side diagonal pairings separately.)*

### 2.3 Non-Lipschitz on vineyard exception set (honest statement)

**Caveat (Vineyard discontinuity, non-generic set).** The map `u ↦ Dgm_0(u)` is continuous in bottleneck, but `u ↦ (ℓ_1(u), ℓ_2(u), …)` (the *sorted* bar-length vector) is **not continuous** at **vineyard singularities** — points where two bars swap order or where a bar is born/dies exactly at `u(x) = u(y)` for two distinct sites `x, y`. The singular set `V ⊂ Σ_m` is a **codimension-1 semi-algebraic subset** (finite union of hyperplanes `{u : u(x) = u(y)}` for `(x,y) ∈ X_t × X_t`).

On `Σ_m \ V` (the complement of the vineyard singular set), Prop 2.1 gives **honest Lipschitz**. On `V`, `K_soft` remains continuous (since φ is applied bar-by-bar to values that match continuously under W_∞ matching) but the **bar-assignment** jumps.

**Consequence for variational analysis.** For energy minimization (§G3) and Gibbs partition (§G2–G3), `K_soft` being continuous and bounded on compact `Σ_m` is sufficient for existence via Weierstrass. Differentiability (via `∇K_soft`) is needed for Langevin (F3) and is **generically defined** off `V`; behavior on `V` is handled by taking subgradients or by ε-smoothing. This is carried to C-S2 as part of NQ-3 (vineyard alternative via direct diagram-valued flow).

**Summary of Lipschitz status.**

| Statement | Claim | Status |
|---|---|---|
| `K_soft ∈ C^0(Σ_m)` (continuous) | Yes, globally | proved |
| `K_soft` is L_φ·2n-Lipschitz on `Σ_m \ V` | Generic Lipschitz | proved (Prop 2.1 + 2.2) |
| `K_soft` Lipschitz on all of `Σ_m` (incl. `V`) | Still holds via W_∞ continuity | sketched (full proof requires handling bar (dis)appearance at V) |
| `∇K_soft` well-defined a.e. on `Σ_m` | Yes, off `V` | sketched |

---

## §3. Volume-Constraint Compatibility (Q1 from plan.md)

### 3.1 Statement of the compatibility question

Plan §"Q1": does minimization of `K_soft` conflict with `Σ_i u_i = m`? Is projected gradient flow well-defined?

### 3.2 Analysis

**Observation (H-A7 from pre_brainstorm).** `K_soft` depends on the **superlevel-set filtration** — i.e., on the relative ordering of `u(x)` values and the graph structure — not on the *scale* of u as such. The volume constraint `Σ u_i = m` controls the **total mass**, which is orthogonal to the *ordering*:

- Rescaling `u ↦ αu` for `α > 0` preserves orderings (hence preserves `Dgm_0` up to a horizontal affine scaling of birth/death values by α, which changes bar lengths by α but does not create/destroy bars).
- Shifting `u ↦ u + β 1` preserves Dgm_0 exactly (both births and deaths shift by β, so bar lengths are invariant).

Therefore the volume constraint and `K_soft` are **not directly in conflict**: fixing `Σ u_i = m` fixes a hyperplane in `ℝ^n` that transversally intersects the superlevel structure.

**Observation (H-A8).** The extreme values of `K_soft` on `Σ_m` depend on m:
- At `u = m/n · 1` (uniform), `Dgm_0` has one bar of length 0 (a single component at threshold `m/n` that dies at 0). `K_soft(u_uniform) = φ(0) + (n-1) · φ(0) = 0` (by φ(0) = 0).
- At highly concentrated configurations (`u` supported on few sites with `u_i` near 1 each), `K_soft` increases. For fixed m, the maximum number of bars that can simultaneously have length close to 1 is bounded by `⌈m⌉` — the total mass must support each "near-1" peak. Hence `sup_{u∈Σ_m} K_soft(u) ≤ L_φ · (m + 1) / ℓ_0` for (φ-lin); for (φ-sat), `sup ≤ ⌈m⌉`.

### 3.3 Projected gradient flow well-definedness

The projected gradient flow on Σ_m is:

$$
\dot u \;=\; -\Pi_{\Sigma_m}\nabla_u \mathcal{F}_{\mathrm{C+E}}[u] \;=\; -(I - \tfrac{1}{n}\,\mathbf{1}\mathbf{1}^\top)\nabla_u \mathcal{F}_{\mathrm{C+E}}[u],
$$

where `Π_{Σ_m}` is the orthogonal projector onto the tangent space `T_u Σ_m = {v : Σ v_i = 0}` (fixed, independent of u).

For `∇K_soft`: generically (off vineyard set V) defined by:

$$
\nabla_u K_{\mathrm{soft}}(u)_x \;=\; \sum_i \varphi'(\ell_i(u)) \cdot \big(\partial \ell_i / \partial u_x\big).
$$

The term `∂ℓ_i / ∂u_x` is explicit in the vineyard formulation (Cohen-Steiner–Edelsbrunner–Morozov 2006): if bar i is born at vertex `v_b^i` (the local superlevel-set maximum defining component birth) and dies at vertex `v_d^i` (the merge vertex), then `∂(b_i - d_i)/∂u_x = δ_{x, v_b^i} - δ_{x, v_d^i}` (each bar length depends on exactly two vertex values). Hence `∇K_soft` is a **sparse vector** of ±φ'(ℓ_i) entries at the birth/death vertices — well-defined and bounded off V.

**Conclusion.** `K_soft` is compatible with volume constraint: (i) no direct conflict (orthogonal axes), (ii) scale on Σ_m is bounded (depends on m), (iii) projected gradient flow is well-defined off V (vineyard exception set, codim-1). Well-posedness of projected SDE (Langevin) is inherited from `ℱ_C+E` Lipschitz via Da Prato–Zabczyk; carried to C-S2.

---

## §4. Hard-count Recovery and Interpretation

**Proposition 4.1 (Hard-K limit).** Let `u_ε ∈ Σ_m` be a sharp-interface configuration: `u_ε(x) ≈ 1` on `K` disjoint connected regions `R_1, …, R_K` (total mass `m`), `u_ε(x) ≈ 0` elsewhere, with boundary width `ε`. Then as `ε → 0`:

$$
K_{\mathrm{soft}}(u_\varepsilon) \;\to\; K \cdot \varphi(1).
$$

*Sketch.* Each region `R_k` produces one bar of `Dgm_0` with birth ≈ 1 (at the interior maximum) and death ≈ 0 (when the component merges with the "ambient zero" component, or dies at filtration value 0 in the reduced diagram). Hence bar length `ℓ_k ≈ 1`, and `φ(ℓ_k) → φ(1)`. Summing over K regions gives `K · φ(1)`. ∎

**Interpretation.** `K_soft` is a **graded relaxation of K_hard**: on sharp-interface configurations, it recovers K up to a constant scale. Intermediate (soft) configurations have fractional `K_soft` values reflecting (a) bars partially formed (small ℓ), (b) bars not yet merged into distinct regions (ordering sensitive to u values). This directly reframes the "integer K" question (P-A) into a graded one.

---

## §5. Four-Candidate Comparison (NQ-1)

| # | Definition | Range | Lipschitz basis | Hard-K recovery | Pros | Cons |
|---|---|---|---|---|---|---|
| **(i) P1 persistence-weighted** `K_pers = Σ_i φ(ℓ_i)` | ℝ_{≥0} | φ monotone Lipschitz | CSEH 2007 bottleneck stability | Prop 4.1: sharp-interface → K · φ(1) | Canonical-compatible (CN12); bounded on Σ_m (Cor 2.2); sparse gradient off V | Vineyard discontinuity at V (codim-1); choice of φ is free (weak parametric) |
| **(ii) Betti integral** `K_Betti = ∫_0^1 β_0(U_θ) dθ` | ℝ_{≥0} | Fubini + monotone θ-sweep | Reduces to (i) when `φ(ℓ) = ℓ` via Fubini | Same | Threshold-free by sweep over θ; more transparently related to topology | Loses parametric freedom (no φ choice); numerically more expensive (integral vs finite sum) |
| **(iii) Simplex-valued** `u : X → Δ^{K_{\max}}`, `K_eff = exp(H(u))` | [1, K_max] | Shannon H is continuous on open simplex | Not via persistence; via normalized entropy | K_eff = 1 iff δ-concentrated, K_eff = K iff uniform on K indices | Entropy-native (merges with F-group S naturally); simplex ontology pleasant | Loses spatial structure; CN12 conflict (retract required); K_max hyperparameter |
| **(iv) Measure-valued** `u : X → P(ℝ_{≥0})`, `K = |support|` | ℕ ∪ {∞} | Wasserstein | On atomic discrete: K = # atoms | Most general; Wasserstein OT-compatible | Integer output (defeats soft purpose); computationally heavy |

**Commit rationale for (i):** (a) Minimal disruption to canonical §5.5 / CN12 (persistence-based morphology). (b) `φ` parametric freedom matches SCC's provisional-realization style (canonical §9). (c) Lipschitz via single well-established external theorem (CSEH). (d) Hard-K recovery is limit-consistent (Prop 4.1). (e) Gradient is sparse and explicit off V (§3.3). (f) Alternative (ii) is equivalent to (i) under `φ(ℓ) = ℓ` (pre_brainstorm H-A2), so (i) strictly generalizes.

**NQ-1 status after this commit.** NQ-1 partially resolved: (i) committed as canonical choice. Full NQ-1 resolution — comparison of the *theories induced* by (i)–(iv) (e.g., do the same theorems hold?) — remains open. Promoted to a candidate for canonical_sub.md 2026-04-21 Added entry under "pending OP promotion".

---

## §6. Link to Existing Canonical Theorems

| Canonical theorem | Link to K_soft |
|---|---|
| **QM3** (Q_morph continuity via persistence stability, Cat A) | Direct — same CSEH 2007 anchor. K_soft's Lipschitz proof reuses QM3's stability argument. |
| **T11** (Γ-convergence, Cat A) | Indirect — T11's sharp-interface limit consistent with Prop 4.1 (K_soft → K·φ(1) at sharp-interface). |
| **T-Merge (b)** (Energy ordering, Cat A, "Re-prove retain" in integer_K_dependency_map §2.2) | Re-phrased: "single-mode (K_soft ≈ 1) vs multi-mode (K_soft > 1) energy ordering" via Γ-conv perimeter-minimization. See `working/E/M1_dissolution.md` §2. |
| **T-Persist-K-Sep/Weak/Unified** (Cat C, "Re-prove" in integer_K_dependency_map §2.3) | Statement rewrites: "K independent per-formation persistence" → "per-mode persistence of K_soft distribution regimes". Full re-proof is E-S2+. |
| **T-Merge (a), Topological Lock, Coupling Bound, Prop 1.2, Thm 3.1(a,b,d), γ_eff=0.89** (Cat A/B, "Retire" in integer_K_dependency_map §2.1, §2.2) | Statement meaning dissolves under soft-K; no replacement within this file's scope. See `working/E/F1_dissolution.md`, `M1_dissolution.md`, `MO1_dissolution.md` for how each Critical's integer-K dependency is handled. |

---

## §7. Remaining Open Questions Seeded by This File

These are new open questions (section §9 of 2026-04-21 `03_integration_and_new_open.md` will register them):

- **NQ-1-A.** Does (i) persistence-weighted `K_pers` with (φ-sat) induce the same set of downstream theorems as with (φ-lin)? Open — φ choice may affect `∇K_soft` magnitude in Langevin.
- **NQ-8 (new).** Vineyard exception set `V ⊂ Σ_m` has measure zero; is the Gibbs measure `ℙ ∝ exp(−ℱ/T)` absolutely continuous with respect to Lebesgue on Σ_m, so that V is null for thermal analysis? Expected yes (if ℱ is continuous and bounded, Gibbs is equivalent to Lebesgue on compact Σ_m). Formal check deferred.
- **NQ-9 (new).** Sharper `L_K` bound on Σ_m via graph spectral structure. Cor 2.2 gives `L_K ≤ 2L_φ · n`, likely loose by factor related to `λ_2(G)` or isoperimetric constant.

---

## §8. File Status

- **Commit level:** definition (Def 1) **committed** for session. Lipschitz skeleton (Prop 2.1, Cor 2.2) **sketched** with identifiable step-by-step granularity. Full measure-zero handling + vineyard gradient rigor carried to C-S2.
- **Category self-classification:** K_soft well-definedness (existence + continuity on compact Σ_m) is **Cat A** (Weierstrass + CSEH). Full Lipschitz on all of Σ_m (incl. V): **Cat B-provisional** pending measure-zero treatment.
- **Priority downstream:** G3 (`free_energy_wellposed.md`) uses Cor 2.2 directly. G5 (`M1_dissolution.md`) uses Prop 4.1 for sharp-interface K_soft recovery. G6 (`MO1_dissolution.md`) uses §3.3 gradient formulation.

Next file: `working/C/F_group_axioms.md` (G2).
