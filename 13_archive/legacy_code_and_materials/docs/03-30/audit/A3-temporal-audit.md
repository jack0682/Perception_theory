# A3 — Temporal Theory and Transport Audit

**Auditor:** Temporal Theory and Transport Auditor | **Date:** 2026-03-30 | **Posture:** Maximally Adversarial

**Scope:** All temporal persistence claims, transport claims, self-referential OT claims, and core inheritance claims across I7, I13, Canonical Spec v2.0, paper1_math.tex, and scc/diagnostics.py.

---

## EXECUTIVE VERDICT

**The temporal theory has made genuine progress from I7 to I13, but remains far from proved.** Of 6 originally identified gaps, 3 are credibly closed (Gaps 1-3) and 3 remain fully open (Gaps 4-6). However, the I13 closures themselves contain second-order issues. The self-referential transport existence claim (Brouwer) has a fundamental continuity gap that was flagged in I7-temporal-audit and **has NOT been fixed** — it persists into paper1_math.tex as Theorem 6.1. The code implementation of Persist is a crude L2 similarity measure bearing no structural relationship to the theory's Persist definition. The "novel mathematical object" claim for self-referential OT is overstated — precedent exists in mean-field games and self-consistent equilibrium transport.

**Bottom line:** One clean algebraic identity (Sep covariance). One proof strategy with 3/6 gaps closed (T-Persist-1). One broken existence proof (Brouwer for self-referential transport). One severe theory-implementation disconnect (Persist predicate in code). Zero fully proved temporal results.

---

## PART I: T-PERSIST-1 (TEMPORAL CORE INHERITANCE)

### Gap 1 (epsilon-gentle): CREDIBLY CLOSED with residual issues

**I13 closure:** Definition 1 gives a 3-part condition: (G1) C^2 energy closeness, (G2) transport displacement, (G3) adjacency kernel closeness.

**Verdict: ADEQUATE but with issues.**

1. **The three parts are NOT independent as claimed.** I13 itself acknowledges (Remark 2) that G3 implies a bound on G1 through operator dependence on N. If G3 → G1 (up to constants), then G1 is redundant as an independent hypothesis — it is a derived bound. The "logically independent" claim is false. The correct statement is: G3 is the primitive condition; G1 is a derived but more directly consumable form for the IFT. This is a presentation issue, not a mathematical error.

2. **The smooth parameterization (Remark 3) is sound.** Linear interpolation E_λ = (1-λ)E_t + λE_s is C^2 in (u,λ) because both energies are analytic (sigmoid closure, b_D=0). This is correct. However, it is a CONVENIENCE, not a necessity — the IFT only needs a smooth path, and linearity is the simplest. The question of whether the ACTUAL temporal evolution follows a linear path in energy space is separate (and likely false for large time steps).

3. **Fixed support space X_t = X_s is now explicit.** This is an honest hypothesis. But it severely restricts the theorem's applicability: any formation that gains or loses support sites (e.g., merging, splitting, expanding into new regions) is excluded. The Canonical Spec explicitly allows X_t to vary (§3.2). T-Persist-1 applies to a restricted class of transitions.

**Residual gap:** The C^2 norm is defined as a sup over Σ_m, but Σ_m is compact, so the sup is attained. No issue there. However, computing or bounding ε_1 in practice requires knowledge of the full energy landscape at both times — this is not a "checkable" condition in the same way that, say, a Lipschitz constant is. It is an oracle condition.

### Gap 2 (IFT on Σ_m): CREDIBLY CLOSED

**I13 closure:** Proposition 1 applies the IFT to F(v,λ) = Π_Σ ∇E_λ(û_t + v) on TΣ_m × [0,1].

**Verification of the argument:**

1. **F(0,0) = 0**: Follows from û_t being a critical point. CORRECT.

2. **D_v F(0,0) = H_Σ invertible on TΣ_m with ‖H_Σ^{-1}‖ ≤ 1/μ**: This is the definition of non-degeneracy with spectral gap μ. CORRECT by hypothesis.

3. **Cauchy interlacing:** The claim λ_1 ≤ μ_1 ≤ λ_2 ≤ ... is standard for eigenvalues of a symmetric matrix restricted to a codimension-1 subspace. **CORRECT.** The observation that μ_1 > λ_1 is possible (if the volume direction is a descent direction of the unconstrained energy) is load-bearing and correctly stated.

4. **Quantitative bound:** The integration bound ‖v(λ)‖_2 ≤ ∫₀^λ ε_1/(μ - τε_1) dτ ≤ λε_1/(μ - ε_1) ≤ 2λε_1/μ. The last step uses ε_1 < μ/2, so μ - ε_1 > μ/2. **CORRECT.**

5. **Box constraint caveat:** The projection onto Σ_m (the hyperplane {1^T u = m}) may violate u ∈ [0,1]^n. I13 dismisses this as O(ε_2/√n) per component. This is correct for large n but could matter for small graphs. More importantly, if box constraints are active (some u_t(x) = 0 or 1), the KKT conditions change, and H1 (the Lagrange condition ∇E = ν1) is only correct at INTERIOR points. For boundary-active constraints, additional multipliers are needed. **This is not addressed.**

**Verdict: SOUND for formations where all components of û_t are in (0,1). May fail if box constraints are active (sites with u = 0 or u = 1 exactly).**

### Gap 3 (Volume re-projection): CREDIBLY CLOSED

**I13 closure:** Proposition 2 bounds the mass deficit δ_m ≤ √n · ε_2 and shows the projection cost is δ_m/√n ≤ ε_2.

**Verification:**

1. **δ_m = 1^T(û_t - Mû_t) ≤ ‖û_t - Mû_t‖_1 ≤ √n · ε_2**: By Cauchy-Schwarz (‖·‖_1 ≤ √n · ‖·‖_2). **CORRECT.**

2. **π_Σ(ũ) = ũ + (δ_m/n)1**: Orthogonal projection onto {1^T u = m}. **CORRECT.**

3. **‖π_Σ(ũ) - ũ‖_2 = δ_m/√n**: Direct computation. **CORRECT.**

4. **Combined displacement ≤ 2ε_2**: Triangle inequality. **CORRECT.**

**Issue: The bound δ_m ≤ √n · ε_2 is LOOSE.** The √n factor means the mass deficit can be O(√n · ε_2), which grows with graph size. For the projection cost to be O(ε_2), we need δ_m/√n ≤ ε_2, which requires δ_m ≤ √n · ε_2 → δ_m/√n ≤ ε_2. So the bound is self-consistent but the intermediate mass deficit bound involves √n. This is noted correctly in I13.

**Verdict: CORRECT. The √n in the mass deficit is a feature of the Cauchy-Schwarz bound, not an error.**

### Gaps 4, 5, 6: REMAIN FULLY OPEN

#### Gap 4 (Basin radius / Morse persistence)

**What is needed:** A lower bound on the basin of attraction radius r_s of û_s sufficient to contain π_Σ(ũ).

**Assessment:** This requires tracking not just the minimizer but ALL nearby saddle points under perturbation. The Morse condition (all critical points non-degenerate) is:
- **Generic** (holds for a dense open set of energies by Sard's theorem)
- **NOT guaranteed** for any specific SCC energy
- **Checkable in principle** (compute all critical points and their Hessians)
- **Infeasible in practice** (exponentially many critical points on Σ_m)

The natural approach (IFT at each saddle point, preserving Morse index) is sound but gives a basin radius bound r_s ≥ r_t - O(ε_1/μ_saddle) where μ_saddle is the spectral gap at the saddle. If there is a saddle with μ_saddle → 0 (nearly degenerate saddle), the basin radius guarantee degrades.

**What would close this gap:** Either:
(a) A quantitative Morse lemma for SCC energies showing all critical points have spectral gap ≥ μ_min > 0 (very hard, probably false in general)
(b) A basin characterization via energy level sets: basin(û_s) ⊇ {u : E_s(u) < E_s(û_s) + ΔE_s} for some energy barrier ΔE_s that can be tracked under perturbation (more feasible but still requires barrier tracking)
(c) A probabilistic/genericity argument: for "most" parameter choices, the basin is large (weakest but most achievable)

**Morse theory IS applicable on Σ_m** (it is a smooth compact manifold with boundary). The complication is the boundary ∂Σ_m = {u ∈ Σ_m : some u_i = 0 or 1}, which requires Morse theory with boundary (well-developed but adds complexity).

#### Gap 5 (Transport concentration: M maps core to core)

**What is needed:** Σ_{y ∈ Core_s} M(x,y) ≥ 1 - ε_core for x ∈ Core_t.

**This is the most serious structural gap.** T-Persist-1 proves FIELD continuity (û_s is close to û_t), not TRANSPORT continuity (M sends core to core). These are logically independent:

- **Field continuity:** The minimizer at time s has high values where the minimizer at time t had high values. This is about the ENERGY LANDSCAPE.
- **Transport concentration:** The transport KERNEL assigns most of the mass from core sites at t to core sites at s. This is about the TRANSPORT PLAN.

For a general sub-stochastic M satisfying E1-E4, transport concentration does not follow from field continuity. Consider: M could transport a core site x to a boundary site y (low u_s(y)), but the re-optimization step could then push u_s(y) up to form a new core. The transport plan and the re-optimization are SEQUENTIAL, not simultaneous.

**The self-referential OT framework COULD provide this** if the structural cost (Option B: |u_t(x) - u_s(y)|^2 + |g_t(x) - g_s(y)|^2) penalizes core-to-non-core matching. But this requires:
1. The self-referential fixed point to exist (Brouwer gap, unresolved)
2. The optimal plan at the fixed point to satisfy transport concentration (a property of the SOLUTION, not the PROBLEM)
3. Quantitative bounds on how much the structural cost concentrates transport

**What would close this gap:** A proof that for the OT problem with morphological cost, the optimal plan sends high-u sites to high-u sites with bounded leakage. This is related to monotonicity of optimal transport (Brenier-like), but on discrete spaces with self-referential cost, no such result exists.

**Precise statement needed:** For û_t, û_s formation-structured minimizers with ‖û_s - û_t‖_2 ≤ η, and M* the optimal transport plan with morphological cost, prove: Σ_{y: û_s(y) ≥ θ_core - η} M*(x,y) ≥ 1 - f(η) for x with û_t(x) ≥ θ_core, where f(η) → 0 as η → 0.

#### Gap 6 (Interior gap lower bound)

**What is needed:** min_{x ∈ Core_t} (û_t(x) - θ_core) ≥ γ > 0 for formation-structured minimizers.

**Why it is plausible:** The double-well W(u) = u^2(1-u)^2 has minima at u=0 and u=1. For β/α large (deep phase transition), Γ-convergence (T11) predicts that minimizers approach characteristic functions — core sites should have u ≈ 1. The interior gap should be ≈ 1 - θ_core for well-formed formations.

**Why it is hard:** The Γ-convergence limit gives sharp interfaces, but at FINITE β/α, the transition layer has width O(1/√(β/α)). Interior sites within this layer can have u values between θ_core and 1. The interior gap depends on the MINIMUM over all core sites, which is achieved at the innermost boundary of the core — precisely in the transition layer.

**What would close this gap:** A quantitative estimate from the Euler-Lagrange equation showing that at formation-structured minimizers, interior sites (not in the boundary layer) satisfy u ≥ 1 - Ce^{-c√(β/α)} for constants C, c > 0. This would give γ ≈ 1 - θ_core - Ce^{-c√(β/α)}, which is positive for β/α large enough.

---

## PART II: T-PERSIST-2 (PERSIST PREDICATE)

### What is "core concentration"?

T-Persist-2 claims Persist ≥ |Core_t| · (1-ε_core) · θ_core / ρ_persist. This requires:
1. For each x ∈ Core_t: Σ_{y ∈ Core_s} M(x,y) ≥ 1 - ε_core (transport concentration — Gap 5)
2. For each y ∈ Core_s: u_s(y) ≥ θ_core (field concentration — from T-Persist-1(c) with η small)

"Core concentration" in the theorem title conflates these two distinct properties. Field concentration is partially addressed by T-Persist-1. Transport concentration (Gap 5) is NOT addressed.

### Status of each quantity in the formula

| Quantity | Well-defined? | Source | Status |
|----------|--------------|--------|--------|
| \|Core_t\| | Yes | Cardinality of {x : û_t(x) ≥ θ_core} | Defined |
| ε_core | Defined but uncomputable | Transport leakage from core | Depends on Gap 5 |
| θ_core | Yes | Parameter | Defined |
| ρ_persist | Yes | Normalization constant (Spec §7.1) | Defined but value not specified |

**Verdict: T-Persist-2 is CONDITIONAL on an UNPROVED and INDEPENDENTLY NECESSARY hypothesis (transport concentration). It is NOT a corollary of T-Persist-1. Status: UNPROVED.**

---

## PART III: Sep_new COVARIANCE IDENTITY

### Sep_new = D̄ + (n/S)·Cov_unif(C_t, D_t)

**Verification:** This is an exact algebraic identity. The I7-temporal-audit verified it line by line (lines 196-216). The key step:

Sep_new = (1/S) Σ_x C_t(x,x) D_t(x) = D̄ + (1/S) Σ_x (C_t(x,x) - S/n) D_t(x) = D̄ + (n/S) Cov_unif(C_t(·,·), D_t(·))

The last equality uses Σ_x (C_t(x,x) - S/n) = 0, which allows subtracting D̄ from D_t(x) inside the sum.

**"Uniform distribution":** The covariance is over the COUNTING MEASURE on sites (uniform distribution over {1,...,n}). This is well-defined on any finite graph.

**Verdict: CORRECT. Exact algebraic identity, no assumptions needed.**

### Corollary Sep_new ≥ D̄

Requires Cov_unif(C_t, D_t) ≥ 0 for formation-structured fields. This is a structural claim about the correlation between self-co-belonging and distinction. **Plausible but UNPROVED.**

For formation-structured fields: interior sites have high C(x,x) (deeply integrated) and high D(x) (strongly distinguished from exterior). Exterior sites have low C(x,x) and low D(x). So C and D should be positively correlated. But this requires a formal argument about the joint distribution of C and D at formation-structured minimizers — currently missing.

### Bridge formula: Sep_new = 1 - E_sep/m + TV(C/S, u/m)

**TV** is total variation distance between two probability distributions on sites:
- C/S = C_t(x,x)/S (co-belonging distribution)
- u/m = u_t(x)/m (cohesion distribution)

**Verification:** Sep_old = Σ_x u(x)D(x)/m = 1 - E_sep/m (this is the Sep-energy relationship). Sep_new = Σ_x (C(x,x)/S) D(x). The difference Sep_new - Sep_old = Σ_x (C(x,x)/S - u(x)/m) D(x). Since D(x) ∈ [0,1], this is bounded by Σ_x |C(x,x)/S - u(x)/m| = TV(C/S, u/m) (if we interpret TV as L1 distance between distributions).

**Issue:** The bridge claims Sep_new = 1 - E_sep/m + TV(...), but actually Sep_new - Sep_old = Σ (C/S - u/m)D, which is NOT the TV distance — it is a SIGNED quantity (could be positive or negative depending on the correlation between (C/S - u/m) and D). The bound |Sep_new - Sep_old| ≤ TV(C/S, u/m) is correct, but the EQUALITY claim requires a specific sign assumption.

**Verdict: The bridge formula as an EQUALITY is INCORRECT. The correct statement is |Sep_new - Sep_old| ≤ TV(C/S, u/m), which is a BOUND, not an identity.**

---

## PART IV: SELF-REFERENTIAL TRANSPORT

### Brouwer Fixed-Point Argument: FUNDAMENTAL GAP PERSISTS

**The I7-temporal-audit (lines 276-292) identified this gap: the re-optimization step u → argmin E(·; M(u)) is DISCONTINUOUS at bifurcation/degenerate points.**

**Has this been fixed in I13?** NO. I13 addresses Gaps 1-3 of T-Persist-1 but does NOT address the Brouwer continuity gap.

**Has this been fixed in paper1_math.tex?** NO. The paper states (Theorem 6.1 proof sketch, item 3): "The energy minimizer varies continuously in M by the IFT at non-degenerate critical points." This is the SAME flawed argument. "At non-degenerate critical points" is not "everywhere on the domain." Brouwer requires continuity EVERYWHERE.

**The gap in detail:** Consider the composed map Φ: Σ_m → Σ_m defined by u → fingerprint → OT plan → re-optimize. The step OT plan → re-optimize is:

M ↦ argmin_{v ∈ Σ_m} E(v; M)

This is the argmin of a non-convex function. The argmin correspondence is:
- **Upper hemicontinuous** (by Berge's maximum theorem, since E is continuous and Σ_m is compact)
- **NOT necessarily single-valued** (multiple minimizers can exist)
- **NOT necessarily continuous as a function** (when two minimizers exchange role as the global minimizer, the argmin jumps)

At a parameter value M₀ where two minimizers have equal energy (a "Maxwell point"), the global minimizer is discontinuous in M. This is not a pathological edge case — it occurs whenever the energy landscape has multiple metastable states, which is EXPECTED in the phase-transition regime (β/α > critical threshold).

**Proposed fix (I7-temporal-audit):** Kakutani's fixed-point theorem for upper-hemicontinuous correspondences. This requires:
1. Upper hemicontinuity: YES (Berge's theorem)
2. Compact convex domain: YES (Σ_m)
3. Convex values: **UNKNOWN** — is argmin E(·; M) a convex set? For non-convex E, the answer is generally NO.

**Alternative fix:** Use a SELECTION — choose a specific minimizer by some rule (e.g., closest to the previous minimizer, or lowest-index Morse minimizer). This gives a well-defined function, but continuity of the selection is not guaranteed.

**The most promising fix (not explored in I7 or I13):** Work with LOCAL minimizers, not GLOBAL minimizers. Define Φ using the IFT-tracked local minimizer (which IS continuous by Proposition 1, as long as non-degeneracy holds). This avoids the Maxwell point discontinuity at the cost of requiring the initial point to be near a non-degenerate minimizer. This is essentially what T-Persist-1 does — but it was never connected back to the Brouwer argument.

**Verdict: UNRESOLVED. The Brouwer argument is a sketch with a known fundamental gap. The paper presents it as a theorem (Theorem 6.1 in paper1_math.tex) which is intellectually dishonest.**

### Three Regimes (Weak/Moderate/Strong)

These are heuristic descriptions, not rigorously delineated regimes:
- **Weak:** λ_tr small, ε large. Claimed to be a contraction. The contraction constant is λ_tr · γ · ‖∂φ/∂u‖ / (ε · λ_min(H_static)). This is a REASONABLE dimensional analysis but the specific constants (especially ‖∂φ/∂u‖ and the factor of 2 in the "master condition") are not derived.
- **Moderate:** "Multiple fixed points = different identity assignments." This is an INTERPRETATION, not a theorem. No proof that multiple fixed points correspond to distinct identity assignments rather than numerical artifacts.
- **Strong:** "May diverge." Honest but uninformative.

**Verdict: Heuristic classification with some structural support. NOT rigorous regime boundaries.**

### Local Uniqueness Condition

The condition λ_tr · γ · ‖∂φ/∂u‖ / (ε · λ_min(H_static)) < 1 is POSTULATED based on a chain-rule argument (I7-temporal-audit lines 296-318), not derived from a formal contraction mapping proof. The chain rule structure is sound:

‖J_Φ‖ ≈ (1/λ_min(H)) · λ_tr · (1/ε) · γ · ‖∂φ/∂u‖

Each factor has the correct dependence. But:
1. The operator norms are all estimated separately (submultiplicativity), which can be loose
2. ‖∂φ/∂u‖ involves the resolvent derivative ∂C(x,x)/∂u, which can be large near the spectral radius bound
3. The factor γ is a tuning parameter in the cost, not a derived quantity

**Verdict: STRUCTURALLY SOUND as a sufficient condition for contraction. Constants not rigorously derived. Practical utility limited by the difficulty of estimating ‖∂φ/∂u‖.**

### "Novel Mathematical Object" Claim

The claim that self-referential OT (where cost depends on the transported measures) has "no precedent in OT literature" is **OVERSTATED**.

**Precedents and near-precedents:**

1. **Mean-field games (Lasry-Lions, 2006-2007):** The cost of an agent depends on the distribution of all agents. The equilibrium is a fixed point where the distribution and the optimal strategy are mutually consistent. This is structurally identical to SCC's self-referential loop: fields determine cost, cost determines transport, transport determines fields. The MFG literature has extensive existence and uniqueness theory, including monotonicity conditions for uniqueness.

2. **Self-consistent equilibrium in economics (Kantorovitch-type):** Market equilibrium where prices depend on allocations which depend on prices.

3. **Wasserstein gradient flows with interaction energies:** In the JKO scheme with an energy F(μ) = ∫∫ W(x-y) dμ(x) dμ(y), the "cost" of the proximal step implicitly depends on the target measure μ through the energy.

4. **Congestion in optimal transport (Carlier-Santambrogio):** Transport cost depends on the congestion (how much mass passes through each point), creating a self-referential loop.

**What IS novel about SCC's version:** The cost depends on the cohesion fields through the OPERATOR TRIAD (Cl, D, C), which are themselves nonlinear functions of the fields. This is more complex than mean-field games (where the cost depends on the distribution directly) because the operator triad introduces an additional layer of nonlinearity. The fingerprint φ = (u, Cl(u), D(u), C(u)) is richer than a simple distribution-dependent cost.

**Verdict: The self-referential OT is NOT entirely novel (mean-field games are a direct structural analogue). What IS novel is the specific structure of the cost through the operator triad. The paper should cite mean-field games and clarify the distinction.**

---

## PART V: TRANSPORT OPERATOR M_{t→s}

### Is M defined with mathematical precision?

**In the Canonical Spec (§9.5):** Yes, provisionally. The kernel is:

M(x,y) ∝ exp(-d_X(Ψ(x),y)^2 / (2σ_M^2)) · exp(-‖φ_t(x) - φ_s(y)‖^2 / (2σ_φ^2))

normalized to be sub-stochastic. This is precise but depends on external Ψ and φ.

**In the OT reformulation (I7-ot-transport §3.3):** M* = argmin of the entropic partial OT problem. This IS mathematically precise (unique minimizer of a strictly convex problem on a compact feasible set), for FIXED fields (u_t, u_s). The self-referential version (where u_s also depends on M) creates the fixed-point problem.

**Constraints on M:**
- Sub-stochastic: Σ_y M(x,y) ≤ 1 (E1). YES, by construction.
- Mass-preserving: NO — sub-stochastic means mass can be lost.
- Support: No explicit support constraint. M(x,y) > 0 for all x,y (entropic regularization makes M strictly positive).

### Do the axioms E1-E4 constrain M sufficiently?

- **E1 (sub-stochastic):** Well-defined constraint. Satisfied by the OT formulation.
- **E2 (non-injectivity):** Not a constraint in the standard sense — it is a permission. Satisfied by entropic OT (soft plans).
- **E3 (core inheritance):** RECLASSIFIED to solution constraint in v2.0. Not a constraint on M itself.
- **E4 (structural sensitivity):** Vague requirement ("should depend on structural features"). Satisfied by any cost function that includes structural terms.

**The axioms are very permissive.** Almost any sub-stochastic kernel with structural features in its cost function satisfies E1-E4. They do not pin down M — they describe a broad class. The OT formulation selects a specific M from this class (the optimal one), but the axioms themselves are underdetermining.

---

## PART VI: PERSIST PREDICATE IN CODE vs. THEORY

### Code implementation (diagnostics.py:142-149)

```python
def persist_predicate(u_prev, u_curr):
    if u_prev is None:
        return 1.0
    norm_prev = np.linalg.norm(u_prev)
    if norm_prev < 1e-12:
        return 0.0
    return float(max(0.0, 1.0 - np.linalg.norm(u_curr - u_prev) / norm_prev))
```

This computes: Persist = 1 - ‖u_curr - u_prev‖_2 / ‖u_prev‖_2

### Theory definition (Canonical Spec §7.1)

Persist_W(u) = min_{t<s ∈ W} Σ_{x ∈ Core_t} Σ_{y ∈ Core_s} M(x,y) u_s(y) / ρ_persist

### Analysis of the disconnect

| Aspect | Theory | Code |
|--------|--------|------|
| What is compared | Core-to-core transport weighted by u_s | Raw L2 field difference |
| Involves transport M? | YES — core structural element | NO — purely spatial comparison |
| Involves Core identification? | YES — restricted to Core_t, Core_s | NO — all nodes equally weighted |
| Involves the transport kernel? | YES — M_{t→s}(x,y) is central | NO — no transport kernel used |
| Normalization | ρ_persist (a parameter) | ‖u_prev‖_2 (the L2 norm of previous field) |
| Temporal window | min over all pairs in W | Single pair (prev, curr) |
| Semantic content | Structural inheritance of cohesive core | Simple L2 similarity |

**Severity: CRITICAL DISCONNECT.** The code Persist is not an approximation of the theory's Persist — it is a DIFFERENT QUANTITY entirely. The theory's Persist involves:
1. Identifying the core at both times
2. Evaluating the transport kernel between core sites
3. Weighting by cohesion values at the receiving sites
4. Normalizing by ρ_persist

The code does none of these. It is a generic field similarity measure that would assign high Persist to ANY pair of similar fields, regardless of whether their cores are structurally related through transport.

**Mitigating context:** The code comment says "1.0 for static optimization" — suggesting this is a PLACEHOLDER for the unimplemented temporal theory, not a deliberate implementation. The `u_prev = None` default gives Persist = 1.0, which is what the static experiments use. But the code should be clearly marked as a placeholder, not presented as implementing the theory's Persist predicate.

**Impact on paper claims:** paper1_math.tex states "Persist = 1.0 (theoretical)" for static experiments — this is correct (no temporal variation means perfect persistence trivially). The disconnect only matters if/when multi-time experiments are run with this code.

---

## TEMPORAL GAP MAP

| Claimed Result | Actual Status | Missing Lemmas | Missing Assumptions | What Must Be Proved |
|---------------|---------------|----------------|--------------------|--------------------|
| T-Persist-1(a): Minimizer exists near û_t | **Gaps 1-3 closed; conditional on Gap 4** | Basin containment (Gap 4) | X_t = X_s; non-degeneracy μ > 0; ε_1 < μ/2; box constraints inactive | Quantitative basin radius lower bound for SCC energies on Σ_m |
| T-Persist-1(b): Gradient flow → û_s | **Restates basin argument, not independent** | Same as (a) | Same as (a) | (Subsumed by (a) + T14) |
| T-Persist-1(c): Core inclusion (shifted threshold) | **Correct modulo (a)** | None beyond (a) | η < 1 - θ_core (gentleness relative to interior gap) | (Follows from (a) by ℓ∞ ≤ ℓ2) |
| T-Persist-1(d): Exact threshold preservation | **Vacuous without Gap 6** | Interior gap lower bound | Double-well dominance: β/α sufficiently large | Quantitative bound: min_{x ∈ Core}(û(x) - θ_core) ≥ f(β/α) > 0 |
| T-Persist-1(e): Diagnostic stability | **Bind: plausible. Inside: questionable** | Artic continuity when ℓ_max ≈ ℓ_second | Operator smoothness (G3); persistence gap non-degeneracy | Artic = 1 - ℓ_second/ℓ_max is Lipschitz when ℓ_max - ℓ_second > δ > 0 |
| T-Persist-2: Persist predicate bound | **UNPROVED** (conditional on Gap 5) | Transport concentration lemma | M maps core to core | Σ_{y ∈ Core_s} M(x,y) ≥ 1 - ε_core for x ∈ Core_t |
| Sep_new covariance identity | **PROVED** (algebraic) | None | None | N/A — complete |
| Sep_new ≥ D̄ corollary | **UNPROVED** | Positive correlation of C_t(x,x) and D_t(x) | Formation-structured field | Cov_unif(C,D) ≥ 0 at formation minimizers |
| Sep bridge formula | **INCORRECT as equality** | — | — | Correct version: \|Sep_new - Sep_old\| ≤ TV(C/S, u/m) |
| Brouwer fixed point (transport) | **BROKEN** — continuity gap | Continuity of argmin at Maxwell points | Non-degeneracy of ALL minimizers along the loop | Either: (i) prove generic non-degeneracy, (ii) switch to Kakutani with convex values, or (iii) restrict to local IFT-tracked minimizer |
| Contraction (weak regime) | **Structurally sound, constants unverified** | Rigorous operator norm bounds | ‖∂φ/∂u‖ bounded; spectral radius away from 1/α | Full contraction mapping proof with derived constants |
| Self-referential OT novelty | **OVERSTATED** | — | — | Must cite mean-field games (Lasry-Lions) and clarify distinction |
| Code Persist implementation | **CRITICAL DISCONNECT from theory** | — | — | Implement theory's Persist or clearly label as placeholder |

---

## RECOMMENDATIONS

### Must-fix before publication

1. **Theorem 6.1 in paper1_math.tex (Brouwer existence):** Either downgrade to "Conjecture" / "Proposition (conditional)" or fix the continuity gap. The current presentation as a theorem with a proof sketch that silently assumes generic non-degeneracy is misleading.

2. **Sep bridge formula:** Correct from equality to bound, or remove.

3. **"No precedent" claim for self-referential OT:** Add citation to mean-field games literature and clarify what specifically is novel (operator triad structure in cost, not the self-referential loop per se).

4. **Code Persist:** Add explicit docstring marking it as a PLACEHOLDER for the unimplemented temporal theory. Current comment is insufficient.

### Should-fix for theoretical completeness

5. **Gap 4 (basin radius):** Most tractable of the remaining gaps. A Morse-theoretic argument on Σ_m using the energy barrier from T7-Enhanced seems feasible.

6. **Gap 6 (interior gap):** Second most tractable. Γ-convergence (T11) already gives the qualitative result; quantitative estimates from the Euler-Lagrange equation are standard PDE techniques.

7. **Gap 5 (transport concentration):** Hardest remaining gap. Requires coupling the OT structure to the energy minimizer structure in a way that has not been attempted.

### Registry recommendation

| Result | Recommended Status |
|--------|-------------------|
| T-Persist-1(a-c) | **Category B: Proof strategy with 3/6 gaps closed** |
| T-Persist-1(d) | **Category C: Conditional on unproved interior gap bound** |
| T-Persist-1(e) | **Category C: Bind plausible, Inside questionable** |
| T-Persist-2 | **Category D: Depends on unproved independent hypothesis** |
| Sep_new covariance identity | **Category A: Fully proved** |
| Sep_new ≥ D̄ | **Category C: Unproved structural claim** |
| Sep bridge formula | **INCORRECT as stated; correct version is Category A bound** |
| Brouwer fixed point | **Category D: Broken proof, fundamental gap unresolved** |
| Contraction (weak regime) | **Category B: Sound structure, constants unverified** |

---

## SUMMARY

The temporal theory is the project's largest gap and its most important frontier. The I13 repairs (Gaps 1-3) are genuine, technically sound contributions that move the theory from "ill-posed proof sketch" to "conditional theorem with well-defined remaining gaps." This is real progress.

But the remaining gaps are not minor cleanup. Gap 4 (basin radius) requires Morse theory on a constrained manifold. Gap 5 (transport concentration) requires a structural OT result that does not exist in the literature. Gap 6 (interior gap) requires quantitative PDE estimates. The Brouwer existence argument for self-referential transport has a fundamental continuity gap that has been known since I7 and remains unfixed.

The code implementation of Persist (L2 similarity) bears no structural relationship to the theory's Persist (core-to-core transport inheritance). This must be addressed before any computational claims about temporal persistence.

The single cleanest result across all temporal work remains the Sep_new covariance identity — an exact algebraic identity requiring no assumptions.
