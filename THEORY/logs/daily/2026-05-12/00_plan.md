---
type: log/daily-plan
date: 2026-05-12
canonical_version_at_start: CV-1.13
claim_count_at_start: 59A / 14B / 5C / 5R = 83 claims
note: originally drafted under wrong date 2026-05-13; relocated to actual session date 2026-05-12. "Day 3" framing in body preserved as authored intent.
---

> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]


# Day 3 Plan — 2026-05-12 (relocated from 2026-05-13)

AFD-0 is in working state with OP-AFD-004 Cat B resolved. Two parallel tracks today.

---

## Priority 1 — M-A2 Numeric Verification (Track A, CV-1.14)

**Goal.** Verify Stab_{Aut(G)}(u*) = {e} on canonical 15×15 minimizer.

**Why this is the blocker.** CV-1.14 requires H-MORSE-Local Cat B. H-MORSE-Local requires M-A1+M-A2+M-A3. M-A2 (trivial stabilizer) is the hardest condition to verify.

**Method.**
1. Run find_formation on canonical 15×15 grid (free BC, β=50, vol_frac=0.3) to get u*.
2. Compute Aut(G) for the 15×15 grid (grid symmetries: D4 or Z2×Z2 depending on BC).
3. Check if any g ∈ Aut(G) satisfies g·u* = u* (i.e., u* is fixed by any nontrivial symmetry).
4. If no nontrivial g fixes u*: M-A2 PASSES → proceed to H-MORSE-Local Cat B proof.
5. If some g fixes u*: M-A2 FAILS → consider orbital quotient path or Path C (generic minimizers).

**Expected outputs.**
- Symmetry group Aut(G) structure for 15×15 grid, free BC
- u* numerics (coordinates or heatmap description)
- Table: for each g ∈ Aut(G), does ||g·u* − u*|| < ε?
- Verdict: M-A2 PASS / FAIL / PARTIAL

**Files to read first.**
- THEORY/working/CV114_H_MORSE_PACKAGEII/09_CV114_recommendation.md
- THEORY/working/CV114_H_MORSE_PACKAGEII/02_H_MORSE_statement_reconstruction.md
- CODE/scc/graph.py (for Aut(G) construction)

---

## Priority 2 — AFD-0 External Audit (TeamCreate)

**Goal.** Independent cold review of AFD-D1..D15 and AFD-T1..T9.

**3 reviewer agents.**

Agent A — Mathematical rigor:
- Check AFD-D1..D15 for hidden H-MORSE dependencies or unstated regularity assumptions
- Check AFD-T1..T7 proofs against claimed Cat A inputs
- Check AFD-T9 by-inspection proof (H-MORSE Non-Necessity)

Agent B — Canonical consistency:
- Check each AFD definition against canonical.md CV-1.13 for conflicts
- Verify all Layer-1 inputs cited exist and have the claimed Cat A status
- Check no circular dependencies (AFD using AFD in proof)

Agent C — Overclaim audit:
- Re-run the 20-question audit from afd_audit.md independently
- Flag any language that overstates certainty
- Flag any claims that implicitly assume H-MORSE or Morse nondegeneracy

**Output file:** THEORY/working/AFD_0/afd_external_audit_round1.md

**Promotion gate.** If audit passes: promote AFD-T9 + AFD-D1..D5 + AFD-T1 + AFD-T6 + AFD-T3 to canonical consideration (next CV bump, likely CV-1.14-AFD or separate track).

---

## Priority 3 — OP-AFD-003 Infimum Attainment

**Goal.** Prove (or disprove) that the infimum in AFD-D7 is attained.

**Statement.** Is there a minimizing path γ_* ∈ Adm(F_i, F_j) achieving C_AFD(F_i, F_j) = J_AFD(γ_*)?

**Approach.**
1. In the minimal version (λ_D = λ_K = 0): is there a path achieving Bar(F_i, F_j)?
2. Σ_m is compact (closed bounded polytope in R^n). Admissible paths are continuous on [0,1] → Σ_m.
3. Restrict to rectifiable paths of bounded total variation ||γ||_BV ≤ L for fixed L large.
4. Apply Arzelà-Ascoli: sequence of paths with bounded length and uniformly bounded sup-energy is equicontinuous and has convergent subsequence.
5. Show Bar(γ, F_i) = max_s [E(γ(s)) − E_F_i] is lower semicontinuous under uniform convergence.
6. Conclude: minimizing sequence has a convergent subsequence whose limit achieves the infimum.

**Key issue.** If the admissible class includes paths of unbounded length (as in AFD-D6), the above fails unless we restrict to length-bounded paths and prove the infimum over length-bounded paths equals the infimum over all paths.

**Expected output.** OP-AFD-003 proof attempt file. Classify as:
- Theorem (unconditional): if inf is attained for all admissible pairs
- Proposition (conditional): if inf is attained only for length-bounded paths
- Conjecture with gap: if key step fails

---

## References

- THEORY/working/AFD_0/ (all 12 files after today)
- THEORY/canonical/canonical.md (CV-1.13, sealed 2026-05-10)
- THEORY/working/CV114_H_MORSE_PACKAGEII/
- CODE/scc/graph.py, optimizer.py
