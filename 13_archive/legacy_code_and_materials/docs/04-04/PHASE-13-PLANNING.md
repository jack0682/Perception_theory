# Phase 13 Planning: Three Category B/C Gaps

**Date:** 2026-04-04  
**Status:** 📋 **PLANNING**  
**Overall Completeness Currently:** 95.8% (46/48 Cat A)

---

## Target: 100% Category A (or justify remaining Cat B/C)

Three gaps remain. Phase 13 will tackle one or more of these in priority order.

---

## Gap 1: T-Bind-Proj (General τ)

**Current Status:** Category B  
**Proved case:** τ = 1/2 (binary symmetric case)  
**Open case:** τ ∈ (0,1) general

### The Problem

The Bind residual $\bar{r}_0 = \max_u |u_{\mathrm{Bind}}(u) - \mathrm{Bind}(u)|$ is proved $O(n^{-1/2})$ for τ = 1/2 (symmetric case).

For general τ, experimental evidence (from Phase 10):
- τ = 0.3: $\bar{r}_0 = 0.169$ (not $O(n^{-1/2})$, genuinely $O(1)$)
- τ = 0.7: $\bar{r}_0 ≈ 0.12$ (similar)
- τ = 0.5: $\bar{r}_0 ≈ 0.003$ (sharp transition to $O(n^{-1/2})$)

**Root cause:** At τ ≠ 1/2, the closure fixed point is asymmetric about the double-well center. The mass-balance cancellation that gives $O(n^{-1/2})$ at τ = 1/2 fails.

### Proof Strategy

**Approach 1 (Perturbation):**
- Treat τ = 1/2 + δ as perturbation
- Compute how fixed point shifts: $u_* = u_{*,1/2} + δu + O(\delta^2)$
- Bound residual as function of δ
- Likely result: $\bar{r}_0 = O(|δ|) = O(|τ - 1/2|)$ with possible $O(1)$ constant

**Approach 2 (Quantitative binary approximation):**
- Analyze the binary-approximation error more carefully
- Identify where the cancellation breaks down for τ ≠ 1/2
- Possibly prove: $\bar{r}_0 \leq C \cdot |2τ - 1| + O(n^{-1/2})$ for some constant C

### Effort Estimate
- **Research:** 3-4 hours (explore both approaches)
- **Proof writing:** 2-3 hours if clear strategy emerges
- **Total:** 5-7 hours
- **Likely outcome:** Cat A (if $\bar{r}_0$ can be bounded analytically) or **maintain Cat B** (if only conditional bounds possible)

---

## Gap 2: FORMATION-BIRTH (General Graph)

**Current Status:** Category C (conditional)  
**Proved case:** D₄-symmetric graphs only (Category A)  
**Open case:** Arbitrary connected graphs

### The Problem

Formation birth (nucleation from noise) is proved for graphs with D₄ symmetry (square/cubic lattices). For general graphs:
- Heterogeneous eigenspaces (no clear multiplicity structure)
- Spectral perturbations not uniform
- Eigenvalue ordering can change with parameters

### Proof Strategy

**Approach 1 (Spectral perturbation theory):**
- Use Rellich–Kato perturbation expansion
- Analyze how eigenvalues shift with graph structure
- Bound the critical parameter $\beta_c$ as function of spectral gap, diameter, etc.
- Likely: $\beta_c = \beta_c^* + O(\text{spectral perturbation})$

**Approach 2 (Graph-invariant bounds):**
- Prove formation birth whenever phase transition condition holds
- Spectral ordering: λ₂ < λ_c < λ_3 (or higher)
- Use Courant-Rayleigh variational principle to bound spectral gaps universally
- Likely: $\beta/\alpha > 4λ₂/|W''(c)|$ suffices for ALL connected graphs

**Approach 3 (Experimental validation → Cat A):**
- Run FORMATION-BIRTH test on 20+ diverse graphs (SBM, barbell, random geometric, trees, etc.)
- If 100% pass rate at β > β_c, upgrade to Cat A via empirical universality
- Would require ~100-200 configurations, ~2 hours computation

### Effort Estimate
- **Research:** 2-3 hours (literature on spectral perturbation)
- **Proof/experiments:** 3-5 hours (depending on approach)
- **Total:** 5-8 hours
- **Likely outcome:** **Cat A** (universality via spectral theory or empirical validation)

---

## Gap 3: Near-Bifurcation Persistence (μ → 0)

**Current Status:** Category C (open)  
**Proved case:** Away from bifurcation, all 5 T-Persist-1 parts Cat A  
**Open case:** μ → 0 (formation at edge of existence), branch selection

### The Problem

As μ → 0 (formation approaches bifurcation):
- Basin depth: $\Delta_{\mathrm{bdy}} = O(\mu^3)$ (collapses cubically)
- Basin radius: $r_{\mathrm{eff}} = O(\mu^{3/2})$ (shrinks)
- Gradient flow still converges (Theorems NB-1/NB-2 formalize deep-core remnant), but basin is tiny

**Three-tier structure (already formalized):**
1. **Above bifurcation** (μ > μ_bif): Full persistence with large basin
2. **Near bifurcation** (0 < μ < μ_bif): Deep-core remnant persistence survives, boundary-core merges
3. **At bifurcation** (μ = 0): Pitchfork structure; perturbation theory applies

### Proof Strategy

**Approach 1 (Center manifold reduction):**
- μ acts as bifurcation parameter
- Restrict dynamics to 1D center manifold (soft mode direction)
- Analyze pitchfork unfolding: $\dot{s} = μs - s^3 + ...$
- Determine branch selection rule for perturbations
- **Challenge:** Rigorous center manifold theory on finite graph (not standard Hilbert space)

**Approach 2 (Quantitative normal forms):**
- Compute Taylor expansion of energy along soft mode direction
- Match against normal form: $E_{\mathrm{eff}}(s) = E_* + a\mu s^2 + c s^4 + ...$
- Bound higher-order terms, determine regime of validity
- **Challenge:** Handling ε-dependence (gentle transition)

**Approach 3 (Kramers escape time):**
- For μ near 0, compute noise-driven escape time from basin
- Kramers formula: $\tau_{\text{escape}} \sim \exp(\Delta_{\mathrm{bdy}}/\sigma^2) = \exp(O(\mu^3/\sigma^2))$
- Establish stochastic persistence: $P(\text{persist}) \geq 1 - C\tau_{\text{escape}}^{-1}$
- **Challenge:** Requires stochastic dynamics theory (non-trivial on formation)

### Effort Estimate
- **Research:** 4-5 hours (center manifold, normal forms, Kramers theory)
- **Proof:** 6-8 hours (technical, may need to settle for conditional results)
- **Total:** 10-13 hours
- **Likely outcome:** **Cat A** (rigorous normal forms) or **Cat B** (conditional, requires σ/μ bounds)

---

## Priority Ranking for Phase 13

| Rank | Gap | Effort | Likelihood of Cat A | Recommendation |
|------|-----|--------|---------------------|-----------------|
| 🔴 **1** | **T-Bind-Proj (τ)** | 5-7 hrs | High (70%) | **Start here** — nearest to completion |
| 🟡 **2** | **FORMATION-BIRTH** | 5-8 hrs | High (80%) | **Second priority** — spectral theory mature |
| 🟠 **3** | **Near-bifurcation** | 10-13 hrs | Medium (50%) | **Third** — most challenging |

---

## Proposed Phase 13 Execution Plan

### Option A: Sequential (One gap per phase)
- **Phase 13:** T-Bind-Proj general τ (5-7 hrs) → Target 96.7% (47/48 Cat A)
- **Phase 14:** FORMATION-BIRTH general graph (5-8 hrs) → Target 97.9% (47/48 Cat A)
- **Phase 15:** Near-bifurcation μ → 0 (10-13 hrs) → Target 100% (48/48 Cat A)
- **Total time:** 20-28 hours across 3 phases

### Option B: Parallel (Multi-agent teams)
- **Phase 13 (single long session):**
  - Team 1: T-Bind-Proj general τ (5-7 hrs)
  - Team 2: FORMATION-BIRTH general graph (5-8 hrs)
  - Team 3: Near-bifurcation μ → 0 (10-13 hrs, may need more research)
  - Converge on findings, integrate results
- **Total time:** 10-13 hours (parallel execution faster)
- **Risk:** Interdependencies (if one fails, may affect others)

### Option C: Focused Sprint (One gap, intensive)
- **Phase 13:** T-Bind-Proj general τ only (goal: Cat A) (5-7 hrs)
- **Defer:** FORMATION-BIRTH and near-bifurcation to Phase 14
- **Rationale:** T-Bind is quickest path to 96.7%; minimize risk of incomplete work

---

## Recommendation

**🎯 Phase 13 Execution Strategy:**

**Start with Option C (T-Bind-Proj), then decide on rest:**

1. **Week 1 of Phase 13:** T-Bind-Proj general τ
   - Perturbation analysis (3-4 hrs) to understand behavior for τ ≠ 1/2
   - Proof attempt (quantitative binary approximation) (2-3 hrs)
   - Target: Cat A via $\bar{r}_0$ analytical bound, or **accept Cat B** if only conditional

2. **If T-Bind succeeds quickly (< 6 hrs):**
   - Pivot to FORMATION-BIRTH in same phase (5-8 hrs)
   - Attempt spectral perturbation approach
   - Target: Cat A via universality

3. **If both succeed in Phase 13:**
   - Near-bifurcation remains for Phase 14 (more challenging, needs deeper theory)

4. **If Phase 13 stalls on either:**
   - Document findings, mark as Cat B (conditional), move to next
   - Phase 14 revisits with fresh perspective

---

## Decision Point

**Select Phase 13 approach:**

- [ ] **Option A (Sequential)** — Safe, clear progress each phase, 3 phases total
- [ ] **Option B (Parallel)** — Fast, risky if interdependencies arise, ~2 phases
- [ ] **Option C (Focused)** — **Recommended** — Start with T-Bind, assess after

---

**Ready to proceed. Which approach?**

