---
type: working/afd
status: AFD-0 Draft (2026-05-12)
---

> [!nav] Linked: [[MOC_AFD_0_foundation]] · [[THEORY_INDEX]]


# AFD-0 — Compact Handoff for Next Agent

Read time: 5 minutes.

---

## UPDATE 2026-05-12 — OP-AFD-004 Cat B Resolved

### What was closed today

- **OP-AFD-004: Cat B resolved** (qualitative + quantitative)
  - Strategy A (qualitative basin-exit): depends only on T8-Core + T14 + T-Merge(b), all Cat A. H-MORSE NOT used.
  - Strategy B (quantitative): c_low = 0.0221β derived from T-Persist-1(b) Δ_core ≥ 0.0441β, under H1-H4 + WS + SR.
- **AFD-T7: Lemma Candidate → Cat B Proposition** (C_K(K, K-1) ≥ 0.0221β, conditional on H1-H4 + WS + SR)

### Why it matters

- Merge transitions now have a positive lower-bound theory at Layer 2: every K→K-1 transition costs at least 0.0221β in barrier height.
- The K-stratum transition graph G_form has nontrivial positive cost structure: AFD-T7 provides the first analytic edge-weight lower bound for E_form.
- H-MORSE is NOT required for Layer 2 merge-barrier positivity. The basin-exit argument uses only gradient flow convergence (T14) and strict local minimality (T8-Core).
- AFD-T9 (H-MORSE Non-Necessity) is reinforced: OP-AFD-004 Cat B is further evidence that the Layer 2 / Layer 3 boundary is sharp.

### What remains open

- **OP-AFD-004a** (Layer 3): tight β exponent β^0.89 or β^1.2 analytic derivation. Requires H-MORSE-Saddle + Modica neck geometry. Does NOT block AFD-0.
- **OP-AFD-004b** (Layer 2): broader constants / weaker conditions — general K without WS/SR.
- **OP-AFD-004c** (Layer 2+): near-bifurcation lower bound (μ → 0 regime).

### Day 3 priorities

- **Priority 1:** M-A2 numeric verification (Track A, CV-1.14 blocker) — verify Stab_{Aut(G)}(u*) = {e} on canonical 15×15 minimizer.
- **Priority 2:** AFD-0 external audit (3-agent TeamCreate) — cold review of AFD-D1..D15 and AFD-T1..T9.
- **Priority 3:** OP-AFD-003 infimum attainment (Arzelà-Ascoli argument on Σ_m for rectifiable paths).

### Warnings (critical — do NOT remove)

- Do NOT promote OP-AFD-004 to Cat A without verifying H1-H4 + WS + SR unconditionally.
- Do NOT claim H-MORSE-Saddle.
- Do NOT claim sharp β exponent.
- Do NOT let OP-AFD-004a block AFD-0 promotion.

---

## 1. What was done

AFD-0 (Abstract Formation Dynamics Foundation) drafted as the Layer-2 abstract dynamics layer of SCC. The directory `THEORY/working/AFD_0/` now contains 11 files.

**Definitions added (AFD-D1..D15):**

- D1 Formation Representative — local min of E on Σ_m (no Morse requirement).
- D2 Formation Basin (Deterministic) — gradient-flow basin via T14.
- D2' Formation Basin (Stochastic, optional) — quasi-stationary distribution.
- D3 Formation State — tuple (u_F^*, B_F, d_F, K_F, τ_F, E_F).
- D4 Formation Equivalence — optional refinement (not used by default).
- D5 Formation State Graph G_form = (V_form, E_form, w).
- D6 Admissible Path (P1)–(P4).
- D7 Abstract Transition Cost C_AFD = inf_γ J_AFD(γ; F_i).
- D8 Barrier term Bar(γ, F_i) and Bar(F_i, F_j); asymmetric.
- D9 Diagnostic Variation Var_D(γ).
- D10 K-Jump Cost J_K(γ) = TV(K_act ∘ γ).
- D11 Topological Signature Distance d_top (bottleneck / W_2).
- D12 K-Stratum S_K (set-theoretic only — *warning*).
- D13 K-Jump Event (vineyard crossing).
- D14 Barrier Preorder ≼_bar via ExitCost (total preorder, not antisymmetric).
- D15 EK Refinement Compatibility (Layer-3 interface).

**Theorems added (AFD-T1..T10):**

| ID | Label | One-liner |
|---|---|---|
| T1 | Proposition | V_form ≠ ∅ (from T8-Core) |
| T2 | Theorem | D Lipschitz (from Pred-E + A3 + QM3 + CSEH) |
| T3 | Proposition | Σ_m = ⊔ S_K (set-theoretic) |
| T4 | Proposition | G_form well-defined |
| T5 | Theorem | C_AFD ∈ [0,∞); NOT a metric |
| T6 | Proposition | ≼_bar total preorder via ExitCost |
| T7 | Proposition | C_K(K, K') well-defined; +Lemma Candidate C_K(K, K−1) > 0 |
| T8 | Lemma Candidate (Conditional) | T_* log E[τ] → Bar under H-MORSE + small noise |
| T9 | **Theorem** | **AFD does NOT require H-MORSE** |
| T10 | Design Principle | Degeneracy-handling strategies |

**Central claim.** AFD-T9 (Theorem, proved by inspection): definitions AFD-D1..D15 and results AFD-T1..T7 do not require nondegenerate Hessians, index-1 saddles, Hessian determinants, or Morse genericity.

**Reclassification.** `afd_hmorse_reclassification.md` formalizes: H-MORSE ∈ Layer 3, H-MORSE ∉ Layer 2.

---

## 2. What remains (Open Problems)

Ten OP-AFD problems documented in `afd_open_problems.md`. Top three by severity:

- **OP-AFD-003 (H).** Existence of minimizing transition paths — does the inf in AFD-D7 attain?
- **OP-AFD-004 (H).** Positive merge barrier C_K(K, K−1) ≥ c(β, n, G) > 0 — analytic lower bound replacing numerical evidence.
- **OP-AFD-005 (H).** FW-to-SCC refinement — full proof of AFD-T8 (EK compatibility).

Medium:

- OP-AFD-001 (topology-signature stability at V).
- OP-AFD-002 (K_act stratification regularity).
- OP-AFD-006 (diagnostic coarse-graining / Markov).
- OP-AFD-007 (multi-formation K-field state graph).
- OP-AFD-010 (finiteness of V_form).

Low:

- OP-AFD-008 (topology-aware K-jump cost).
- OP-AFD-009 (Conley-index AFD-1 extension).

---

## 3. Exact next commands

### Action 1 — Prove OP-AFD-004 (positive merge barrier)

```
Read:  THEORY/2_substrate/canonical/canonical.md §13 (T7-Enhanced, T-Merge(b), T-Persist-1(b))
       CODE/experiments/exp38_*.py, exp60_*.py (numerical barrier scans)
       THEORY/2_substrate/Q2_multiformation/from_single.md (single→multi nucleation)
Goal:  Analytic lower bound C_K(K, K−1) ≥ c(β, n, G) > 0.
Method: Combine T7-Enhanced metastability gap (Hessian eigenvalue separation
        > Allen-Cahn) with T-Persist-1(b) basin radius
        r_basin = sqrt(2 Δ_min / λ_max). Argue that any merging path
        γ ∈ Adm(F_K, F_{K-1}) must traverse the inter-basin valley whose
        depth is bounded below by Δ_min, hence Bar ≥ Δ_min.
Output: write THEORY/2_substrate/foundations/AFD/op_afd_004_proof.md (Cat B target).
```

### Action 2 — Resolve OP-AFD-003 (infimum attainment)

```
Read:  AFD-T5 proof in abstract_formation_dynamics.md §14.
       Standard references on direct method of calculus of variations on
       compact sets (e.g. Buttazzo-Giaquinta-Hildebrandt).
Goal:  Prove inf in AFD-D7 attained on rectifiable γ for the minimal version
       (λ_D = λ_K = 0), at least on rectifiable curves of bounded length.
Method: Restrict admissible class to rectifiable γ with length ≤ L (large
        but finite); apply Arzelà-Ascoli to extract a convergent
        subsequence; show Bar(γ, F_i) is lower semicontinuous along uniform
        convergence.
Output: AFD-T5 promoted from Theorem-with-attainment-OPEN to Theorem
        unconditional. Write THEORY/working/AFD_0/op_afd_003_proof.md.
```

### Action 3 — External audit of AFD-0

```
Goal:  Independent cold-review of AFD-D1..D15 and AFD-T1..T10.
Process: TeamCreate with 3 reviewer agents
  (a) Definition reviewer — check AFD-D1..D15 for hidden H-MORSE
      dependencies and unstated regularity assumptions.
  (b) Proof reviewer — check AFD-T1..T7 proofs against Cat A inputs
      claimed; check AFD-T9 by-inspection proof.
  (c) Overclaim reviewer — re-run the 20-question audit independently.
Output: THEORY/working/AFD_0/afd_external_audit_<date>.md.
Promotion gate: if audit PASSes, promote AFD-T9 + AFD-D1..D5 + AFD-T1 +
                AFD-T6 + AFD-T3 to canonical (CV-1.14-AFD or new CV bump).
```

### Action 4 (parallel) — CV-1.14 H-MORSE-Local Cat B

```
Read:  THEORY/2_substrate/Q3_dynamics/h_morse_packageII/09_CV114_recommendation.md
       THEORY/2_substrate/Q3_dynamics/h_morse_packageII/08_candidate_lemma_chain.md
Goal:  Promote H-MORSE-Local to Cat B (Layer-3 prerequisite for AFD-T8).
Note:  This is independent of AFD-0 promotion. The two can proceed in
       parallel. AFD-T8 stays Lemma Candidate until CV-1.14 + reflected-EK
       adaptation (OP-AFD-005) both land.
```

---

## 4. Theorem status (brief table)

| ID | Status | Promoted? | Gap |
|---|---|---|---|
| AFD-T1 | Proposition | No (recommended R1) | none |
| AFD-T2 | Theorem | No (R2 — needs exact Lipschitz constants) | bookkeeping |
| AFD-T3 | Proposition | No (recommended R1) | warning re stratum |
| AFD-T4 | Proposition | No | none |
| AFD-T5 | Theorem | No (R2 — needs OP-AFD-003) | inf attainment |
| AFD-T6 | Proposition | No (recommended R1) | none |
| AFD-T7 | Proposition (+ LC) | No | OP-AFD-004 |
| AFD-T8 | Lemma Candidate (Conditional, L3) | No (hold for CV-1.14) | OP-AFD-005 + H-MORSE |
| AFD-T9 | **Theorem** | **No (top R1 candidate)** | **none** |
| AFD-T10 | Design Principle | No (architectural only) | full Conley AFD-1 |

R1 = first promotion round candidates: T9, D1..D5, T1, T6, T3.
R2 = second promotion round candidates: T2, T5, T7.
Hold: T8 (Layer 3).

---

## 5. Critical warnings (DO NOT lose these)

1. **C_AFD is NOT a metric.** Asymmetric. May fail triangle inequality. State as cost / edge weight. (AFD-T5, audit Q11.)

2. **K-strata are NOT smooth.** S_K is a set-theoretic level set only. Whitney/smooth structure is OP-AFD-002. (AFD-D12, AFD-T3.)

3. **C_AFD is asymmetric in general.** Bar(F_i, F_j) ≠ Bar(F_j, F_i) when energies differ. Symmetric variant Bar_sym is offered but not default. (AFD-D8.)

4. **H-MORSE is Layer 3, not Layer 2.** AFD-D1..D15 and AFD-T1..T7 do not use H-MORSE. AFD-T8 / AFD-D15 use H-MORSE *only* to interface with Layer 3. (AFD-T9, `afd_hmorse_reclassification.md`.)

5. **Pairwise C_AFD comparison is NOT a preorder.** Use only the ExitCost-based scalar version for ≼_bar. (AFD-D14, AFD-T6, audit Q12.)

6. **K-jumps are vineyard crossings, not Morse saddles.** A K-jump is first a topological event in K_act, not (necessarily) a single Morse saddle crossing. (§13 slogan 3, AFD-D13 comment.)

7. **AFD-T8 is Conditional.** Do not promote ahead of CV-1.14 (H-MORSE-Local Cat B). Stays Lemma Candidate until OP-AFD-005 + H-MORSE both land.

8. **AFD-0 does NOT resolve any open SCC problem.** Specifically OP-0005, OP-0006-quantitative extensions, OP-0008, OP-0009, OP-0021 all remain. AFD-0 is a *language* for stating them at Layer 2, not a resolution.

---

## 6. Suggested CV-1.14 parallel action

Per `CV114_H_MORSE_PACKAGEII/09_CV114_recommendation.md`:

- H-MORSE-Local Cat B target via Hessian-positivity at generic minimizers under "non-Goldstone, non-bifurcation" regime.
- Counterexamples catalogued in `04_degeneracy_catalogue.md` — these become AFD-T10 Design-Principle cases (no Cat-B obstruction, just regime restriction).
- CV-1.14 promotion + AFD-0 promotion are *independent*. Both can land in parallel.

Once both land:

- AFD-T8 can be upgraded to **Theorem (Layer 3, Conditional on small noise)** once OP-AFD-005 (reflected-Langevin FW-EK identification) is resolved.
- A canonical Layer-3 section can be added stating EK = AFD × prefactor exactly.

---

## 7. File reference

| File | Read priority |
|---|---|
| `README.md` | Always first (1 min). |
| `afd_layer_diagram.md` | First picture (1 min). |
| `abstract_formation_dynamics.md` | Main document (15 min for skim). |
| `afd_hmorse_reclassification.md` | Central architectural claim (5 min). |
| `afd_audit.md` | 20-question honesty audit (5 min). |
| `afd_theorem_registry.md` | Table reference (2 min). |
| `afd_open_problems.md` | OP-AFD-001..010 (3 min). |
| `afd_examples.md` | 7 worked examples (10 min). |
| `afd_framework_comparison.md` | 15 candidate frameworks (10 min). |
| `afd_log.md` | This session's record (5 min). |
| `afd_summary_for_next_agent.md` | (this file) handoff (5 min). |

---

## 8. Slogan to remember

> **AFD separates transition order from transition rate. EK refines AFD; AFD does not require EK. H-MORSE is Layer 3.**
