# Phase 13 Execution Plan: T-Bind-Proj (General τ)

**Date:** 2026-04-04  
**Phase Goal:** Upgrade T-Bind-Proj from Category B to Category A  
**Target Completeness:** 96.7% (47/48 Cat A)  
**Status:** 📋 **READY TO EXECUTE**

---

## Mission

**T-Bind-Proj (Binding Residual Projection)** is currently Category B because:
- **Proved case:** τ = 1/2 (symmetric, gives $\bar{r}_0 = O(n^{-1/2})$)
- **Open case:** τ ∈ (0,1) general (empirically $\bar{r}_0 = O(1)$ for τ ≠ 1/2)

**Phase 13 objective:** Either prove T-Bind-Proj for general τ (Cat A) or rigorously establish the conditional bound (improve Cat B documentation).

---

## Team Structure (3-4 agents)

**Recommended composition for T-Bind focus:**

| Role | Name | Tools | Responsibility |
|------|------|-------|-----------------|
| **Lead** | team-lead | All | Orchestration, synthesis, Spec update |
| **Analyst 1** | bind-analyst | Read/Grep/Bash | Analyze τ-dependence experimentally & theoretically |
| **Analyst 2** | perturbation-analyst | Math theory | Perturbation expansion, binary approximation gap |
| **Auditor** | auditor | Verification | Gap verification, proof consistency check |

---

## Task Breakdown (5 tasks)

### Task #1: Experimental Baseline Analysis (bind-analyst)
**Objective:** Understand $\bar{r}_0(τ)$ behavior quantitatively

**Work:**
1. Read Phase 10 Bind analysis documents (T-BIND-PROJ.md, exp5 data)
2. Extract raw data: τ values, grid sizes, measured $\bar{r}_0$
3. Fit curve: Is $\bar{r}_0(τ)$ polynomial in $(τ - 1/2)$? Exponential?
4. Hypothesis formation: Propose functional form $\bar{r}_0(τ) = f(τ) + O(n^{-1/2})$
5. Document findings in BIND-TAU-ANALYSIS.md

**Deliverable:** BIND-TAU-ANALYSIS.md (4-5 pages, experimental baseline)  
**Blocked by:** Nothing  
**Time estimate:** 2-3 hours

---

### Task #2: Perturbation Theory Development (perturbation-analyst)
**Objective:** Develop analytical proof strategy for general τ

**Work:**
1. Setup: Treat τ = 1/2 + δ as small perturbation
2. Compute closure fixed point shift: $u_*(τ) = u_*(1/2) + δu(\delta) + O(\delta^2)$
3. Linearize around τ = 1/2:
   - First-order: How does residual change? Is cancellation linear in δ?
   - Second-order: Quadratic terms; do they break symmetry?
4. Bound residual as function of δ: Establish $\bar{r}_0(τ) = O(|τ - 1/2|)$ or $O(|τ - 1/2|^2)$
5. Compare theory prediction to Task #1 experimental baseline

**Deliverable:** BIND-PERTURBATION-THEORY.md (6-8 pages, rigorous derivation)  
**Blocked by:** Nothing  
**Dependencies:** Task #1 results for validation  
**Time estimate:** 3-4 hours

---

### Task #3: Binary Approximation Gap Analysis (perturbation-analyst)
**Objective:** Identify where the O(n^{-1/2}) cancellation breaks down

**Work:**
1. Review Phase 10 binary approximation derivation (why it works at τ = 1/2)
2. Identify the key cancellation: closure term cancels against separation term
3. For τ ≠ 1/2: Asymmetric fixed point breaks cancellation
4. Quantify the gap: How much residual remains after cancellation?
5. Derive: $\bar{r}_0 = \text{[cancellation term]} + \text{[asymmetry correction]}$
6. Prove correction is $O(|τ - 1/2|)$ or larger

**Deliverable:** BIND-ASYMMETRY-GAP.md (4-6 pages, cancellation analysis)  
**Blocked by:** Task #2 (need perturbation structure first)  
**Time estimate:** 2-3 hours

---

### Task #4: Synthesis & Category Decision (team-lead)
**Objective:** Consolidate Tasks #1-3 into final proof and Category determination

**Work:**
1. Read all three analytic documents (Tasks #1-3)
2. Decision point: Can we prove Cat A?
   - **If yes:** Write T-BIND-PROJ-GENERAL-TAU.md (final proof, τ-dependent bound)
   - **If no (conditional only):** Improve Cat B documentation with explicit τ-dependence
3. If Cat A: $\bar{r}_0(τ) = O(|τ - 1/2|)$ or $O(n^{-1/2})$ whichever larger
4. Update Canonical Spec line 1075 (T-Bind-Proj status)
5. Compute new completeness: 96.7% (47/48 Cat A) if successful

**Deliverable:** T-BIND-PROJ-GENERAL-TAU.md or improved Cat B statement  
**Blocked by:** Tasks #1-3  
**Time estimate:** 1-2 hours

---

### Task #5: Audit & Verification (auditor)
**Objective:** Verify proof is rigorous and consistent

**Work:**
1. Read T-BIND-PROJ-GENERAL-TAU.md (or Cat B update)
2. Checklist:
   - [ ] Theorem statement clear? ($\bar{r}_0$ bounded as function of τ)
   - [ ] All perturbation steps justified? (δ is small, higher-order bounded)
   - [ ] Cancellation analysis explicit? (where does symmetry break?)
   - [ ] Experimental validation matches theory? (Task #1 vs #2/#3)
   - [ ] Category decision justified? (Cat A if analytical, Cat B if conditional)
   - [ ] Spec update correct? (Canonical Spec line 1075)
3. Audit report: Score, publication readiness
4. If issues found: Send feedback to team-lead for refinement

**Deliverable:** PHASE-13-AUDIT-REPORT.md  
**Blocked by:** Task #4  
**Time estimate:** 1 hour

---

## Dependency Graph

```
Task #1: Experimental Baseline     [2-3 hrs]
          ↓
Task #2: Perturbation Theory        [3-4 hrs]
Task #3: Asymmetry Gap Analysis     [2-3 hrs]  (blocked on #2)
          ↓        ↓
Task #4: Synthesis                  [1-2 hrs]  (blocked on #2, #3)
          ↓
Task #5: Audit & Verification       [1 hr]     (blocked on #4)
```

**Critical path:** Task #1 → Task #2 → Task #3 → Task #4 → Task #5  
**Total time estimate:** 9-13 hours (sequential; 5-7 if Tasks #2/#3 can run in parallel)

---

## Success Criteria

### ✅ Category A Path (Best case)
- [ ] Prove $\bar{r}_0(τ)$ is analytically bounded for all τ ∈ (0,1)
- [ ] Perturbation analysis gives explicit formula: $\bar{r}_0(τ) = O(|τ - 1/2|) + O(n^{-1/2})$
- [ ] Experimental data (Task #1) matches theory (Task #2/#3) within margins
- [ ] Spec updated: "Proved (Category A, Phase 13)"
- [ ] Completeness upgraded to 96.7% (47/48 Cat A)

### ✅ Category B Path (Fallback)
- [ ] Cannot prove universal bound, but characterize τ-dependence rigorously
- [ ] Document: "Proved for τ = 1/2 (Category A); for general τ: $\bar{r}_0 \leq C|τ - 1/2| + O(n^{-1/2})$ conditional on binary approximation validity"
- [ ] Spec updated: Improve Cat B statement with explicit τ-dependence
- [ ] Maintain 95.8% completeness, but documentation clearer

### ❌ Dead End
- [ ] No clear pattern emerges; τ-dependence is chaotic
- [ ] Keep Cat B as is, defer to Phase 14
- [ ] Move to FORMATION-BIRTH in Phase 13b

---

## Execution Timeline

**Parallel Work (can overlap):**
- Tasks #1 and #2 can start simultaneously (1-2 hrs shared setup)
- Task #3 starts after Task #2 produces perturbation framework

**Sequential Bottleneck:**
- Task #4 must wait for Tasks #2 and #3
- Task #5 must wait for Task #4

**Realistic timeline:**
- **Hours 0-3:** Tasks #1 and #2 in parallel (experimental baseline + perturbation setup)
- **Hours 3-6:** Task #3 (asymmetry analysis, blocking on #2 output)
- **Hours 6-8:** Task #4 (synthesis, decision point)
- **Hours 8-9:** Task #5 (audit, final sign-off)

---

## Handoff & Team Management

**Team Setup:**
- Create team: `phase-13-tbind`
- 4 agents: bind-analyst, perturbation-analyst, team-lead, auditor
- All work in bypassPermissions mode

**Between-Task Handoff:**
- bind-analyst → perturbation-analyst: Pass BIND-TAU-ANALYSIS.md experimental data
- perturbation-analyst → team-lead: Pass BIND-PERTURBATION-THEORY.md + BIND-ASYMMETRY-GAP.md
- team-lead → auditor: Pass T-BIND-PROJ-GENERAL-TAU.md
- auditor → team-lead: Pass PHASE-13-AUDIT-REPORT.md with sign-off

**Team Cleanup:**
- After Task #5 complete: TeamDelete phase-13-tbind
- Archive all deliverables to `/docs/04-04/proof/`
- Commit Phase 13 results to git
- Proceed to Phase 14 (or Phase 13b if time permits)

---

## Decision Gates

**Gate 1 (after Task #2):** Does perturbation analysis show clear pattern?
- **Yes:** Proceed to Task #3 (asymmetry analysis)
- **No:** team-lead may pivot to FORMATION-BIRTH instead (Phase 13b)

**Gate 2 (after Task #3):** Can asymmetry gap be bounded rigorously?
- **Yes:** Target Cat A in Task #4
- **No:** Accept Cat B with improved documentation

**Gate 3 (after Task #4):** Does audit find issues?
- **Yes:** Send back for refinement (max 1-2 hours)
- **No:** Proceed to finalize, commit, cleanup

---

## Expected Deliverables

✅ **BIND-TAU-ANALYSIS.md** (4-5 pages)
- Experimental baseline: $\bar{r}_0(τ)$ measurements across τ values
- Curve fitting: Proposed functional form
- Confidence intervals from multiple grid sizes

✅ **BIND-PERTURBATION-THEORY.md** (6-8 pages)
- Perturbation setup: τ = 1/2 + δ, closure fixed point shift
- First/second-order analysis: Residual as function of δ
- Bound: $\bar{r}_0(τ) = f(\delta) + O(n^{-1/2})$

✅ **BIND-ASYMMETRY-GAP.md** (4-6 pages)
- Binary approximation mechanism at τ = 1/2
- Asymmetry breakdown for τ ≠ 1/2
- Quantified correction term

✅ **T-BIND-PROJ-GENERAL-TAU.md** (8-12 pages)
- Final unified proof: $\bar{r}_0$ bounded for general τ
- Theorem statement: Category A or improved Category B
- Integration with Phase 10 T-Bind-Proj τ=1/2 proof

✅ **PHASE-13-AUDIT-REPORT.md** (3-5 pages)
- Gap verification checklist
- Score & publication readiness
- Sign-off or refinement notes

✅ **Canonical Spec v2.1.md** (updated)
- Line 1075: T-Bind-Proj status change (if Cat A upgrade)
- New completeness: 96.7% (47/48 Cat A)

---

## Ready to Launch Phase 13

**Next step:** Form team and assign Task #1 to bind-analyst.

Confirm readiness:
- [ ] Team structure approved
- [ ] Task breakdown clear
- [ ] Agents selected
- [ ] Proceed with TeamCreate & task assignment

