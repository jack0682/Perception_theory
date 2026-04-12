# R3 — Temporal Theory Reconstruction Plan

**Author:** Temporal-Theory Reconstruction Planner | **Date:** 2026-03-30

**Inputs consumed:**
- `docs/audit/SYNTHESIS.md` — unified synthesis (fault map, theorem ledger, missing math)
- `docs/audit/A3-temporal-audit.md` — complete temporal gap analysis (primary input)
- `docs/I7-temporal-prover.md` — original T-Persist-1, T-Persist-2, Sep covariance claims
- `docs/I7-temporal-audit.md` — adversarial audit of I7 claims (6 gaps identified)
- `docs/I7-transport-designer.md` — self-referential fingerprint + Brouwer sketch
- `docs/I13-temporal-repair.md` — closures of Gaps 1-3 (ε-gentle, IFT, re-projection)
- `scc/diagnostics.py` — Persist code (L2 similarity placeholder)
- `papers/paper1_math.tex` lines 580-687 — Theorem 6.1 and Theorem "Temporal Core Inheritance"

---

## EXECUTIVE SUMMARY

The temporal theory has two separate problems that require separate strategies:

1. **Transport fixed-point existence** (Theorem 6.1 / Brouwer argument) — broken by discontinuity at Maxwell points. This is about whether the self-referential loop *has* a solution.

2. **Temporal core inheritance** (T-Persist-1) — a conditional IFT-based result with 3/6 gaps closed. This is about whether formations *persist* under gentle transitions.

These are logically independent. T-Persist-1 does not require the Brouwer fixed point. The reconstruction should treat them separately and not let the broken existence proof contaminate the sound persistence result.

After analyzing four strategic options, **Option C (Restrict to local/conditional) is recommended**, with a specific enhancement: fold in the local-IFT-tracked minimizer as a partial replacement for the global Brouwer argument. This is honest, maximally publishable, and consistent with the static core.

---

## PART I: CURRENT STATE ASSESSMENT

### What is solid

| Result | Status | Evidence |
|--------|--------|----------|
| Sep_new covariance identity | **Category A: Proved** | Exact algebraic identity, verified line-by-line in A3 audit |
| T-Persist-1(a): minimizer persistence | **Category B: 3/6 gaps closed** | IFT on Σ_m sound; Gaps 1-3 credibly closed in I13 |
| T-Persist-1(c): core inclusion (shifted) | **Correct modulo (a)** | ℓ∞ ≤ ℓ₂ direction confirmed correct |
| ε-gentle definition | **Well-posed** | 3-part condition (G1-G3), properly specified in I13 |
| Contraction (weak regime) | **Category B** | Structurally sound chain-rule argument, constants unverified |

### What is broken

| Result | Status | Failure mode |
|--------|--------|-------------|
| Brouwer FP (Theorem 6.1) | **Broken** | Continuity fails at Maxwell points; argmin jumps between minimizers |
| T-Persist-1(b): basin containment | **Open (Gap 4)** | Requires Morse persistence of saddle points under perturbation |
| T-Persist-1(d): exact threshold | **Open (Gap 6)** | Requires interior gap lower bound from double-well |
| T-Persist-2: Persist predicate | **Open (Gap 5)** | Requires transport concentration (M maps core→core) — independent, hardest gap |
| Sep bridge formula | **Incorrect as equality** | Should be |Sep_new - Sep_old| ≤ TV(C/S, u/m), a bound |
| Sep_new ≥ D̄ corollary | **Unproved** | Requires Cov(C,D) ≥ 0 at formation minimizers |
| Code Persist | **Critical disconnect** | L2 similarity ≠ core-to-core transport inheritance |
| "No OT precedent" | **False** | Mean-field games (Lasry-Lions 2007) are direct structural precedent |

---

## PART II: STRATEGIC OPTIONS ANALYSIS

### Option A: Fix the Brouwer Argument

**Strategy:** Strengthen hypotheses to ensure continuity of the re-optimization step everywhere on Σ_m. Specifically, require that ALL critical points of E(·; M) are non-degenerate for every M in the image of the self-referential loop.

**Mathematical content:**
- Need: for all u_s ∈ Σ_m, the energy E(·; M(φ(u_s))) has only non-degenerate critical points
- This is a "generic non-degeneracy along the loop" condition
- If satisfied, argmin is locally unique and IFT gives continuity; Brouwer applies

**Evaluation:**

| Criterion | Assessment |
|-----------|-----------|
| **Mathematical soundness** | WEAK. Generic non-degeneracy along the entire self-referential loop is not provable without strong structural assumptions. The SCC energy in the phase-transition regime β/α > critical is *expected* to have multiple minimizers with Maxwell crossings — this is the whole point of the phase transition. Requiring non-degeneracy everywhere essentially excludes the interesting regime. |
| **Publishability** | LOW. Reviewers will ask "under what conditions is the hypothesis satisfied?" and the answer is "we don't know, and it probably fails in the phase-transition regime." |
| **Consistency with static core** | TENSION. The static theory *relies* on phase transitions and metastability. Requiring non-degeneracy everywhere contradicts the metastable landscape that T8-Core establishes. |
| **Effort required** | MEDIUM. The technical work is manageable (state the hypothesis, verify Brouwer conditions), but the hypothesis itself is unrealistic. |

**Verdict: REJECT.** The hypothesis needed to make Brouwer work is incompatible with the phase-transition regime that makes the theory interesting.

---

### Option B: Switch to Kakutani Fixed-Point Theorem

**Strategy:** Replace Brouwer (requires single-valued continuous map) with Kakutani (requires upper-hemicontinuous correspondence with convex compact values). The re-optimization step defines a set-valued map u_s ↦ argmin E(·; M(φ(u_s))).

**Mathematical content:**
- Upper hemicontinuity: YES by Berge's Maximum Theorem (E continuous, Σ_m compact)
- Compact values: YES (argmin of continuous function on compact set)
- Convex values: **UNKNOWN and likely NO** — argmin of non-convex E is generally a discrete set of points, not a convex set
- Kakutani requires convex values; Fan-Glicksberg generalizes to locally convex spaces but still needs convex values

**The convexity obstacle in detail:** At a Maxwell point where two minimizers u* and u** have equal energy, argmin = {u*, u**}. The convex hull conv({u*, u**}) = the line segment [u*, u**], which contains points that are NOT minimizers (they're saddle points or local maxima along the segment). So argmin is not convex.

**Possible fix:** Replace argmin with the set of *approximate* minimizers: S_δ(M) = {u : E(u; M) ≤ min E + δ}. This IS convex? No — sublevel sets of non-convex functions are not convex either.

**Alternative:** Use the convex hull of argmin as the correspondence. Kakutani applies, giving a fixed point in conv(argmin). But this fixed point may not be a minimizer — it could be a convex combination of two minimizers, which is typically higher energy. The fixed point exists but is *meaningless* (not an energy minimizer).

**Evaluation:**

| Criterion | Assessment |
|-----------|-----------|
| **Mathematical soundness** | MODERATE. Kakutani applies IF convex values can be established. The natural argmin correspondence does not have convex values. Workarounds (convex hull, δ-relaxation) give existence of a fixed point that may not be physically meaningful. |
| **Publishability** | MODERATE. Kakutani existence results are standard and publishable, but a reviewer will immediately ask "is the fixed point actually a minimizer?" If it's a convex combination of minimizers, it's not. |
| **Consistency with static core** | NEUTRAL. Does not contradict the static theory, but the fixed point may not be an energy minimizer, which disconnects it from the variational framework. |
| **Effort required** | HIGH. Need to either (a) prove convexity of argmin (likely impossible), (b) find a meaningful convex relaxation, or (c) use a different FP theorem entirely (e.g., Schauder-type for non-convex settings). |

**Verdict: REJECT as primary strategy.** The convexity obstacle is genuine and workarounds produce meaningless fixed points. However, **retain Kakutani as a remark** — it shows that *some* fixed point exists (in a relaxed sense), which is useful context even if the fixed point isn't a minimizer.

---

### Option C: Restrict to Local/Conditional Results

**Strategy:** Abandon the global existence theorem (Brouwer/Kakutani) entirely. Keep T-Persist-1 as a *conditional* theorem: IF the transition is ε-gentle and IF the local IFT-tracked minimizer exists, THEN the formation persists with quantitative bounds.

**The key insight:** T-Persist-1 does NOT need the Brouwer fixed point. It uses IFT to track a *local* minimizer continuously in the perturbation parameter λ. This is the observation from A3-temporal-audit: "Work with LOCAL minimizers, not GLOBAL minimizers. Define Φ using the IFT-tracked local minimizer (which IS continuous by Proposition 1, as long as non-degeneracy holds)."

**What this gives us:**

1. **T-Persist-1(a)** becomes a clean conditional theorem: non-degenerate minimizer + ε-gentle transition → minimizer persists with quantitative bound ‖û_s - û_t‖₂ ≤ 2ε₁/μ. *No global existence needed.*

2. **T-Persist-1(c)** follows directly: core inclusion with shifted threshold. *Sound.*

3. **For the self-referential loop:** Instead of proving a global fixed point, prove that *alternating minimization converges in the weak regime* (contraction argument). This gives a constructive, implementable result rather than a pure existence theorem.

4. **T-Persist-1(b)** remains conditional on Gap 4 (basin radius). *Honest.*

5. **T-Persist-2** remains conditional on Gap 5 (transport concentration). *Honest.*

**What we lose:** The claim "a self-referential transport fixed point exists" becomes "in the weak-transport regime, alternating minimization converges to a consistent state." This is weaker but *true*.

**Evaluation:**

| Criterion | Assessment |
|-----------|-----------|
| **Mathematical soundness** | STRONG. Every claim is either proved or honestly marked as conditional/open. No handwaving, no broken proofs presented as theorems. |
| **Publishability** | HIGH. Conditional results with clearly stated hypotheses are standard in mathematics. The paper becomes more credible, not less, by being honest about what's proved and what's open. Reviewers respect gap-honesty. The T-Persist-1(a,c) results are genuine contributions even without global FP existence. |
| **Consistency with static core** | EXCELLENT. The IFT-based persistence is the temporal analogue of the IFT-based phase transition (T8-Core). The pattern "prove a local result under non-degeneracy, note global questions as open" is exactly what the static theory does. |
| **Effort required** | LOW-MEDIUM. Most work is already done (I13 closed Gaps 1-3). Remaining effort: (1) rewrite paper section to present conditional results honestly, (2) downgrade Theorem 6.1 to Conjecture/Discussion, (3) state remaining gaps as explicit open problems. |

**Verdict: RECOMMENDED.** This is the only option that is both mathematically honest and publishable. It preserves the genuine contributions (IFT persistence, Sep identity, ε-gentle framework) while removing the broken claims.

---

### Option D: Rewrite via JKO/Wasserstein Gradient Flow

**Strategy:** Abandon the OT fixed-point formulation entirely. Instead, model temporal evolution as a JKO (Jordan-Kinderlehrer-Otto) scheme: at each time step, minimize E(u_s) + W₂²(u_s, u_t)/(2τ), where W₂ is the Wasserstein-2 distance and τ is the time step.

**Mathematical content:**
- JKO scheme on Σ_m: well-studied on continuous spaces, less so on graphs
- Discrete Wasserstein gradient flows exist (Maas 2011, Mielke 2011, Chow-Huang-Li-Zhou 2012)
- The static energy E is the driving functional; temporal evolution is the gradient flow of E in Wasserstein space
- No self-referential loop — the transport is *defined* by the energy landscape, not by a fixed-point equation

**What this gives us:**
- Well-posedness of the temporal evolution (by convexity of the Wasserstein distance)
- Convergence to equilibrium (if E is displacement convex)
- Connection to a large body of literature on Wasserstein gradient flows

**What this loses:**
- The self-referential fingerprint — the entire I7 transport designer contribution
- The conceptual claim that "transport inherits the operator triad's self-referential character"
- The interesting multiple-fixed-point phenomenon (different identity assignments)
- Distinctiveness from standard Wasserstein gradient flow literature

**Evaluation:**

| Criterion | Assessment |
|-----------|-----------|
| **Mathematical soundness** | STRONG. JKO schemes are mathematically mature with extensive theory. |
| **Publishability** | MODERATE. The results would be technically sound but less novel — "we run JKO on our energy" is not a distinctive contribution. The paper would read as an application of existing theory, not a new framework. |
| **Consistency with static core** | MODERATE. JKO naturally pairs with variational energies, so the static core is preserved. But the self-referential character of the operator triad — the theory's distinguishing feature — is lost in the temporal dimension. |
| **Effort required** | HIGH. Requires re-deriving everything from scratch. Discrete Wasserstein gradient flows on graphs have technical subtleties (choice of metric, definition of Wasserstein on graphs). The existing I7/I13 work would be discarded. |

**Verdict: REJECT for current papers.** Too much effort, too little novelty gain. The self-referential fingerprint is genuinely interesting and worth preserving even if the existence proof needs weakening. **Consider for future work** (a third paper or revision cycle).

---

## PART III: RECOMMENDED STRATEGY — OPTION C WITH ENHANCEMENTS

### Overall approach

**Keep the conditional results. Downgrade the broken existence claim. Strengthen what's provable. Be explicit about what's open.**

### Detailed plan

#### 1. KEEP: T-Persist-1(a,c) as conditional theorem

**Current paper1 status:** Theorem "Temporal Core Inheritance — Conditional" (lines 665-674). Already well-structured.

**Required changes:**
- Ensure the theorem title says "Conditional" prominently
- List ALL hypotheses in the theorem statement (non-degeneracy μ > 0, ε-gentle with G1-G3, fixed X_t = X_s, ε₁ < μ/2)
- Part (a): clean, keep as is
- Part (c): clean, keep as is
- Part (b): explicitly mark "conditional on Gap 4 (basin radius)"
- Part (d): REMOVE from the theorem statement. Move to a remark: "If additionally the interior gap min_{x ∈ Core_t}(û_t(x) - θ_core) > η, then exact threshold preservation holds. A quantitative interior gap bound from the double-well structure is an open problem."

**No new mathematics needed.** This is editorial restructuring of existing I13 results.

#### 2. DOWNGRADE: Theorem 6.1 (Brouwer existence)

**Current paper1 status:** Presented as a theorem with proof sketch (lines 610-629). The proof sketch silently assumes generic non-degeneracy, which fails at Maxwell points.

**Required change:** Replace "Theorem" with either:
- **(Preferred) Conjecture + Discussion.** State: "We conjecture that Φ has at least one fixed point. The natural approach via Brouwer requires continuity of the re-optimization step, which holds at non-degenerate minimizers (by IFT) but may fail at Maxwell points where two minimizers exchange global optimality. Possible approaches to resolve this include Kakutani's theorem (which requires convex-valued correspondences, currently unverified) or restriction to the weak-transport regime where the contraction argument applies."
- **(Alternative) Proposition under strong hypothesis.** State: "If all critical points of E(·; M) are non-degenerate for every M in the image of the self-referential loop, then Φ is continuous and Brouwer gives a fixed point." Note this excludes the phase-transition regime.

**The key message to preserve:** The self-referential fingerprint loop is conceptually sound and closes the temporal self-reference elegantly. The *existence of the fixed point* is the open mathematical question, not the *formulation*.

#### 3. KEEP: Sep_new covariance identity

**Status:** Category A, fully proved, no changes needed. This should remain as Theorem/Proposition in the paper.

#### 4. FIX: Sep bridge formula

**Current status:** Stated as equality Sep_new = 1 - E_sep/m + TV(C/S, u/m). A3 audit shows this is **incorrect as equality** — the correct statement is the bound |Sep_new - Sep_old| ≤ TV(C/S, u/m).

**Required change:** Replace the equality claim with:
- State Sep_old = 1 - E_sep/m (proved, algebraic)
- State |Sep_new - Sep_old| ≤ TV(C/S, u/m) (proved, bound)
- State Sep_new ≥ D̄ as a "structural conjecture for formation-structured fields" (not proved; requires Cov(C,D) ≥ 0)

#### 5. FIX: "No OT precedent" claim

**Current paper1 status (line 649):** "The self-referential transport formulation... has no precedent in the optimal transport literature."

**Required change:** Replace with honest contextualization:

> The closest structural precedent is mean-field game theory (Lasry-Lions 2007), where the cost depends on the distribution of agents. Our formulation differs in that the cost depends on the *specific field values* through the operator triad (closure, distinction, co-belonging), introducing a richer dependence structure than the distribution-level coupling in mean-field games.

This preserves the genuine novelty claim (operator triad in cost) while citing the structural precedent.

#### 6. KEEP: Weak-regime contraction as the primary temporal existence result

The contraction argument for the weak-transport regime (λ_tr small, ε_OT large) is structurally sound:
- The Jacobian of Φ is bounded by λ_tr · γ · ‖∂φ/∂u‖ / (ε_OT · λ_min(H_static))
- When this is < 1, Banach contraction gives unique FP and convergent alternating minimization

**Upgrade this from a "remark" to a "Proposition."** It is the strongest existence result we can honestly claim. State the contraction condition explicitly, note that the constants are estimated (not derived), and that this restricts to the weak-coupling regime.

#### 7. STATE EXPLICITLY: Remaining open gaps as open problems

In the paper, add a "Open Problems" subsection to the temporal section:

> **Open Problem 1 (Basin radius).** Prove a quantitative lower bound on the basin of attraction of û_s sufficient for gradient flow convergence (Gap 4). The natural approach is Morse persistence of saddle points under perturbation.
>
> **Open Problem 2 (Transport concentration).** Prove that the self-referential transport kernel maps core sites to core sites: Σ_{y ∈ Core_s} M(x,y) ≥ 1 - ε_core for x ∈ Core_t (Gap 5). This is the key missing step for the Persist predicate bound (T-Persist-2).
>
> **Open Problem 3 (Interior gap).** Prove a quantitative lower bound min_{x ∈ Core}(û(x) - θ_core) ≥ γ > 0 at formation-structured minimizers, using the double-well structure of E_bd (Gap 6).
>
> **Open Problem 4 (Global transport FP existence).** Prove existence of a fixed point of the self-referential transport map Φ without the weak-transport contraction hypothesis.

---

## PART IV: PERSIST CODE RECONSTRUCTION

### Current state

The code (`scc/diagnostics.py:142-149`) computes:

```python
Persist = 1 - ||u_curr - u_prev||_2 / ||u_prev||_2
```

This is L2 field similarity — a **completely different quantity** from the theory's Persist:

```
Persist_W(u) = min_{t<s ∈ W} Σ_{x ∈ Core_t} Σ_{y ∈ Core_s} M(x,y) u_s(y) / ρ_persist
```

### Why the disconnect exists

The theory's Persist requires:
1. A transport kernel M_{t→s}
2. Core identification at both times (thresholding u ≥ θ_core)
3. Transport concentration (Gap 5, unproved)

None of these exist in the current static-only codebase. The L2 placeholder was reasonable for static experiments (where Persist = 1.0 trivially), but it would give wrong results for any temporal experiment.

### Minimal correct Persist implementation

Three tiers, from simplest to most theory-faithful:

#### Tier 1: Core-overlap Persist (no transport kernel needed)

Replace L2 similarity with core-to-core overlap:

```python
def persist_predicate(u_prev, u_curr, theta_core=0.5):
    """Persist via core overlap: fraction of previous core retained in current core."""
    if u_prev is None:
        return 1.0
    core_prev = u_prev >= theta_core
    core_curr = u_curr >= theta_core
    n_prev = np.sum(core_prev)
    if n_prev == 0:
        return 0.0
    # Fraction of prev core sites that remain in current core, weighted by u_curr
    overlap = np.sum(u_curr[core_prev & core_curr])
    max_possible = np.sum(u_prev[core_prev])
    if max_possible < 1e-12:
        return 0.0
    return float(min(1.0, overlap / max_possible))
```

**Pros:** Uses core identification (matching theory), computable without transport kernel, strictly better than L2 similarity.

**Cons:** No transport kernel, assumes spatial correspondence (same sites), not theory-complete.

**When to use:** Immediately, as a better placeholder. Clearly docstring as "core-overlap approximation, not full theory Persist."

#### Tier 2: Gaussian-kernel Persist (heuristic transport)

Use a simple Gaussian spatial kernel as a proxy for M:

```python
def persist_predicate(u_prev, u_curr, graph, theta_core=0.5, sigma=2.0):
    """Persist via Gaussian spatial kernel approximating transport."""
    if u_prev is None:
        return 1.0
    core_prev = u_prev >= theta_core
    core_curr = u_curr >= theta_core
    if not np.any(core_prev):
        return 0.0
    # Build Gaussian kernel (spatial proximity)
    # M(x,y) ∝ exp(-d(x,y)^2 / (2σ^2))
    from scipy.sparse.csgraph import shortest_path
    D = shortest_path(graph.W, directed=False)
    M = np.exp(-D**2 / (2 * sigma**2))
    # Restrict to core_prev rows, core_curr columns
    M_cc = M[np.ix_(core_prev, core_curr)]
    # Row-normalize to sub-stochastic
    row_sums = M_cc.sum(axis=1, keepdims=True)
    row_sums = np.maximum(row_sums, 1e-12)
    M_cc = M_cc / row_sums
    # Persist = sum over core_prev sites of (sum over core_curr of M * u_curr) / rho
    u_at_core_curr = u_curr[core_curr]
    transport_val = M_cc @ u_at_core_curr  # per-site transported cohesion
    persist = np.mean(transport_val)  # average over core_prev
    return float(min(1.0, max(0.0, persist)))
```

**Pros:** Includes transport kernel, core identification, weighted by u_curr — structurally matches the theory. Uses graph distance.

**Cons:** Heuristic kernel (not the theory's OT solution), shortest_path is O(n³) which is expensive, sigma is a free parameter.

**When to use:** For temporal experiments. Clearly label as "heuristic transport-kernel Persist."

#### Tier 3: Full OT-based Persist (theory-faithful)

Requires implementing the entropic OT solver with fingerprint cost:
1. Compute fingerprints φ_t, φ_s
2. Build cost matrix c(x,y) per equation (6) in paper1
3. Solve entropic partial OT (Sinkhorn on sub-stochastic constraints)
4. Extract M*, restrict to Core_t × Core_s
5. Compute Persist = Σ_{x ∈ Core_t} Σ_{y ∈ Core_s} M*(x,y) u_s(y) / ρ_persist

**Pros:** Exactly implements the theory.

**Cons:** Requires Sinkhorn solver, fingerprint computation, and self-referential loop (or a fixed-point iteration). Substantial new code.

**When to use:** Only when the temporal theory is mature enough to warrant it. NOT needed for current papers (which are static-only experimentally).

### Recommendation

**Implement Tier 1 now.** It is a strict improvement over L2 similarity, requires no new dependencies, and correctly identifies cores. Mark it clearly as an approximation. Implement Tier 2 when temporal experiments begin. Defer Tier 3 until the theoretical gaps (especially Gap 5) are resolved.

**Immediate action for current code:** Add a prominent docstring to the existing `persist_predicate`:

```python
def persist_predicate(u_prev, u_curr):
    """PLACEHOLDER: L2 field similarity. Returns 1.0 for static optimization.

    WARNING: This does NOT implement the theory's Persist predicate (Spec §7.1),
    which requires core identification, a transport kernel M_{t→s}, and
    core-to-core transport weighting. This is an interim measure for static
    experiments only. See docs/repair/R3-temporal-reconstruction.md for the
    reconstruction plan.
    """
```

---

## PART V: SUMMARY TABLE

| Item | Action | Priority | Effort |
|------|--------|----------|--------|
| Theorem 6.1 (Brouwer FP) | Downgrade to Conjecture + Discussion | **CRITICAL** | Low (editorial) |
| T-Persist-1(a,c) | Keep as conditional theorem, verify all hypotheses listed | **HIGH** | Low (already done in I13) |
| T-Persist-1(b) | Keep, mark "conditional on Gap 4" | HIGH | None (editorial) |
| T-Persist-1(d) | Move to Remark, mark "conditional on Gap 6" | HIGH | None (editorial) |
| Weak-regime contraction | Upgrade from Remark to Proposition | HIGH | Low (formalize existing argument) |
| Sep bridge formula | Correct from equality to bound | **CRITICAL** | Low (editorial) |
| "No OT precedent" | Add MFG citation, clarify genuine novelty | **CRITICAL** | Low (editorial) |
| Code Persist docstring | Add PLACEHOLDER warning | HIGH | Trivial |
| Tier 1 Persist implementation | Implement core-overlap version | MEDIUM | Low (~30 lines) |
| Sep_new ≥ D̄ | Downgrade from "proved" to "structural conjecture" | MEDIUM | None (editorial) |
| Open problems subsection | Write for paper | MEDIUM | Low (editorial) |
| Gap 4 (basin radius) | State as open problem; attempt Morse argument | LOW (for papers) | High (new math) |
| Gap 5 (transport concentration) | State as permanent hypothesis | LOW (for papers) | Very high (may be unresolvable) |
| Gap 6 (interior gap) | State as open problem; note Γ-convergence gives qualitative support | LOW (for papers) | Medium (new math) |

---

## PART VI: WHAT THE TEMPORAL SECTION SHOULD LOOK LIKE AFTER REPAIR

### Structure for paper1_math.tex §6 (Transport and Persistence)

1. **§6.1 Cohesion Fingerprint** — define φ(x), explain self-referential structure. *No changes needed.*

2. **§6.2 Self-Referential Transport Cost** — define c(x,y), explain the fixed-point formulation. *No changes needed.*

3. **§6.3 Fixed-Point Existence** — **REWRITE:**
   - State the self-referential map Φ: Σ_m → Σ_m
   - **Proposition (Weak-Regime Existence and Uniqueness):** Under the contraction condition (eq. current 6.3), Φ has a unique fixed point and alternating minimization converges.
   - **Remark (General Existence):** For the general case, Brouwer's theorem requires continuity of the re-optimization step, which holds at non-degenerate minimizers but may fail at Maxwell points (bifurcation discontinuity). Kakutani's theorem for set-valued maps gives existence of generalized fixed points but requires convex values, which is not guaranteed. Global existence of a self-referential transport fixed point remains an open problem outside the weak regime.
   - **Remark (Mean-field game precedent):** Cite Lasry-Lions (2007). Clarify: MFG has distribution-level cost dependence; SCC has operator-triad-level cost dependence. The self-referential loop structure is shared; the specific dependence through (Cl, D, C) is novel.

4. **§6.4 Temporal Core Inheritance** — **KEEP with edits:**
   - Definition of ε-gentle (already good)
   - Theorem T-Persist-1 with parts (a), (b) [conditional], (c)
   - Move part (d) to a Remark
   - Move part (e) Bind stability to Remark; note Inside instability issue
   - Proof sketch (already good in current paper)
   - Explicit listing of open gaps (4, 5, 6)

5. **§6.5 Open Problems** — NEW subsection listing the four open problems from Part III.7 above.

### What to cut entirely

- Remove the "PROVED" label from the original I7 claims in any internal documents
- Remove the Sep bridge formula as an equality (replace with bound)
- Remove "no precedent in OT literature" (replace with contextualized novelty claim)

---

## PART VII: RATIONALE FOR OPTION C

### Why not fix the Brouwer argument?

The Brouwer argument fails at Maxwell points — parameter values where two minimizers have equal energy and the global argmin jumps discontinuously. This is not a technical inconvenience; it is a *structural feature* of non-convex energy landscapes in the phase-transition regime. The theory's static core (T8-Core) *depends* on the existence of phase transitions and multiple metastable states. Requiring non-degeneracy everywhere would exclude the regime that makes the theory interesting.

### Why not switch to Kakutani?

Kakutani requires convex-valued correspondences. The argmin of a non-convex energy is generically a finite set of isolated points — not convex. Taking convex hulls gives fixed points that are not energy minimizers. The result would be technically correct but physically meaningless.

### Why conditional results are sufficient for publication

The best mathematical papers prove what they can and honestly state what they can't. T-Persist-1(a,c) with the IFT argument is a *genuine contribution*: the first quantitative temporal persistence result for the SCC framework, with explicit dependence on the spectral gap μ and the gentleness parameters. The ε-gentle framework (Definition 1 from I13) is well-designed and worth publishing in its own right.

Conditional results with clearly marked gaps are standard in mathematical journals. The paper gains credibility by being honest about the gaps rather than papering over them with broken Brouwer arguments.

### Why the self-referential fingerprint is still worth including

Even without a proved global fixed point, the fingerprint φ = (u, Cl(u), D(x;1-u), C(x,x)) is a conceptually important construction that:
- Closes the temporal self-referential loop using only the operator triad
- Defines a natural transport cost that respects formation structure
- Leads to a well-defined contraction argument in the weak regime
- Opens interesting questions about multiple fixed points / identity ambiguity

The *formulation* is the contribution. The *existence proof* is the open problem. These are separable, and the paper should present them as such.

---

## APPENDIX: DEPENDENCY GRAPH OF TEMPORAL RESULTS

```
Sep_new covariance identity [PROVED, algebraic]
    └── Sep_new ≥ D̄ [UNPROVED, needs Cov(C,D) ≥ 0]

Fingerprint φ definition [WELL-DEFINED]
    ├── Transport cost c(x,y) [WELL-DEFINED]
    │   ├── Entropic OT → M* [WELL-DEFINED, unique for fixed fields]
    │   └── Self-referential loop Φ [WELL-DEFINED as a map]
    │       ├── Weak-regime contraction [STRUCTURALLY SOUND, constants unverified]
    │       └── Global FP existence [BROKEN — Brouwer continuity gap]
    │
    └── T-Persist-1 (IFT on Σ_m)
        ├── (a) Minimizer persistence [PROVED conditional on ε-gentle + non-degeneracy]
        ├── (b) Gradient flow → û_s [CONDITIONAL on Gap 4: basin radius]
        ├── (c) Core inclusion (shifted θ) [PROVED, follows from (a)]
        ├── (d) Exact threshold [CONDITIONAL on Gap 6: interior gap bound]
        └── T-Persist-2 (Persist predicate)
            └── [CONDITIONAL on Gap 5: transport concentration — independent, hardest]
```

The dependency graph shows that the proved results (Sep identity, T-Persist-1(a,c), weak contraction) form a coherent publishable cluster that does not depend on the broken Brouwer argument or the three open gaps. The recommendation to focus on this cluster is structurally supported.
