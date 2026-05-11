---
type: log/brainstorm
date: 2026-05-13
session: Day 3 pre-session rough notes
---

# Day 3 Pre-Session Brainstorm — 2026-05-13

Rough practical notes for the three priorities. No polish, just key questions and approaches.

---

## 1. M-A2: Trivial Stabilizer Verification

**The computation.** 15×15 grid with free BC has symmetry group Aut(G) = D4 = {e, r90, r180, r270, s_h, s_v, s_d1, s_d2} (8 elements: 4 rotations + 4 reflections), since the grid is square. For free BC specifically — check whether corner/edge nodes break any symmetry. With free BC (all nodes equivalent via graph structure) D4 is the full symmetry group.

**How to check M-A2.** Run find_formation with β=50, vol_frac=0.3 on 15×15 to get u* (an n=225 vector). For each g ∈ Aut(G) \ {e}: compute g·u* by permuting coordinates (g acts as a permutation matrix P_g on R^225). Check ||P_g u* - u*||_2 < ε (use ε = 1e-4).

**If M-A2 PASSES (most likely outcome).** The formation u* sits asymmetrically — one blob in a corner or off-center. No nontrivial symmetry fixes it. This is the generic case. Proceed to H-MORSE-Local Cat B proof (M-A1 + M-A2 + M-A3 all satisfied).

**If M-A2 FAILS.** The minimizer u* is D4-symmetric (blob at center, or perfectly centered ring). This happens when vol_frac and β conspire to place the formation at a symmetric point. Fix: use a different vol_frac or break symmetry via initialization (random seed). Alternatively use Path C: argue M-A2 holds generically (dense open set of parameters) even if it fails for this specific (β, vol_frac) value.

**Key implementation detail.** The permutation P_g for a grid graph: for g = r90 (90-degree rotation), node (i,j) maps to (j, n-1-i) for an n×n grid. Build the permutation index array once and apply it to the u* vector.

**Expected result.** For a 15×15 grid with vol_frac=0.3 (formation mass = 0.3×225 = 67.5), the minimizer should break symmetry — the blob typically nucleates off-center or in a corner under generic initialization. M-A2 should pass.

---

## 2. AFD-0 External Audit: 3 Agents in Parallel

**Setup.** TeamCreate with 3 agents reading different aspects of AFD-0. Each agent gets: the full `abstract_formation_dynamics.md` (main doc), the relevant registry/audit files, and a focused question set.

**Agent A (definitions).** Target: hidden H-MORSE in AFD-D1..D15. The most likely places to find hidden dependencies:
- AFD-D1: "strict local minimizer" — does this require nondegeneracy? No: strict local min is weaker than Morse minimum.
- AFD-D2: "gradient-flow basin" — does this require uniqueness of limit? T14 (Lojasiewicz) guarantees it without Morse.
- AFD-D11: TopSig τ uses persistence — no Morse assumption.
Key question for Agent A: Is AFD-D2' (stochastic basin, QSD) subtly using H-MORSE via QSD uniqueness? This is the most plausible hidden dependency.

**Agent B (canonical consistency).** Target: every Cat A citation in AFD-0 is genuine. Check:
- T-Persist-1(b) at canonical.md line 1804 — does it actually say Δ_core ≥ 0.0441β?
- T-Merge(b) at line 1163 — does it actually say K=1 is the global minimum?
- T14 (Lojasiewicz) — confirmed Cat A? Check theorem_status.md.
The main risk: a Cat A citation that was retracted or downgraded after the AFD draft was written.

**Agent C (overclaim audit).** Target: the 20-question audit in `afd_audit.md`. Re-run each question independently without looking at the recorded answers. Focus questions where overclaims are most likely:
- Q11 (C_AFD is a metric?): must be answered NO — it is asymmetric.
- Q15 (K-strata are smooth?): must be answered NO — set-theoretic only.
- Q19 (AFD resolves OP-0005?): must be answered NO.
- Q20 (AFD-T9 proven rigorously?): answer is YES (by inspection) — verify the inspection is complete.

**Combined verdict.** Pass / Conditional (list of fixable issues) / Fail. Target: Conditional at worst. If Pass: initiate R1 promotion (AFD-T9 first, then AFD-D1..D5, AFD-T1, AFD-T6, AFD-T3).

**Prize result.** AFD-T9 (H-MORSE Non-Necessity Theorem) is the highest-value item. If the audit confirms it, AFD-T9 can be promoted to canonical as a standalone theorem without waiting for the full AFD-0 package. This would be a CV-1.14 addition independent of H-MORSE-Local Cat B.

---

## 3. OP-AFD-003: Infimum Attainment via Arzelà-Ascoli

**Core insight.** Σ_m = {u ∈ [0,1]^n : Σu_i = m} is a compact convex polytope. Continuous functions on compact spaces attain their extrema. The question is whether the functional γ ↦ max_s E(γ(s)) is lower semicontinuous in a topology that gives compactness for sequences of admissible paths.

**The argument outline.**
1. Fix a minimizing sequence γ_k ∈ Adm(F_i, F_j) with J_AFD(γ_k; F_i) → Bar(F_i, F_j).
2. The barrier term max_s [E(γ_k(s)) - E_F_i] is bounded (it converges to a finite limit).
3. Restrict to γ_k of bounded length: ||γ_k||_{BV} ≤ L. This is WLOG if any path of infinite length can be reparametrized to finite length without increasing max_s E(γ(s)).
4. Why WLOG? A path γ : [0,1] → Σ_m of infinite total variation visits many points but max_s E(γ(s)) depends only on the image. Reparametrize by arc length on the image — the image is a compact subset of Σ_m. The curve length on the image is finite if and only if the image is a rectifiable curve. For any ε > 0, there is a rectifiable curve in Adm(F_i, F_j) achieving within ε of the infimum (otherwise the infimum over rectifiable paths would be strictly above the infimum over all paths, which is impossible since rectifiable paths are a subset of all admissible paths — wait, this goes the wrong direction). The correct argument: any admissible path with finite barrier can be approximated by a piecewise-linear (hence rectifiable) path with nearly the same barrier. Piecewise-linear paths are dense in the uniform topology among continuous paths from u*_i to u*_j.
5. Arzelà-Ascoli: a sequence of Lipschitz-L curves γ_k : [0,1] → Σ_m (Lipschitz constant bounded by L, the arc-length bound) is uniformly equicontinuous and pointwise bounded (in compact Σ_m). Extract uniformly convergent subsequence γ_{k_j} → γ_*.
6. Lower semicontinuity: max_s E(γ(s)) is lower semicontinuous under uniform convergence? Actually it is continuous: E is continuous on compact Σ_m, γ_k → γ_* uniformly → E(γ_k(s)) → E(γ_*(s)) uniformly in s → max_s E(γ_k(s)) → max_s E(γ_*(s)).
7. Conclude: Bar(γ_*, F_i) = lim Bar(γ_{k_j}, F_i) = Bar(F_i, F_j). So γ_* achieves the infimum.

**The key gap.** Step 4 — is the infimum over rectifiable paths equal to the infimum over all admissible paths? This holds if piecewise-linear paths are dense among admissible paths in the barrier metric. Claim: for any continuous γ ∈ Adm and ε > 0, there exists a piecewise-linear γ' ∈ Adm with |Bar(γ', F_i) - Bar(γ, F_i)| < ε. Proof sketch: approximate γ uniformly by piecewise-linear interpolation on a fine partition; E is uniformly continuous on compact Σ_m; uniform approximation of γ gives uniform approximation of E ∘ γ; max_s is continuous in the sup norm.

**Classification target.** If the above gap closes: Theorem (unconditional, at least for the minimal version λ_D = λ_K = 0). The full version (with λ_D, λ_K) requires lower semicontinuity of Var_D and TV(K_act ∘ γ) under uniform convergence — TV is lower semicontinuous, so this likely works too.

**Write as.** A proof attempt file `op_afd_003_proof.md`, classifying result as Theorem (conditional on the density claim for piecewise-linear paths) or full Theorem if the density claim closes.
