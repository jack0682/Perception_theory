---
type: log/extension-summary
date: 2026-05-14
target: OP-HMORSE-SBM numerical robustness extension (CV-1.17 candidate first deliverable)
session_label: W7-Day5 post-CV-1.16-SEAL continuation
status_at_start: CV-1.16 SEALED (97 claims); L-HMORSE-LOCAL Cat B unconditional in canonical
status_at_end: OP-HMORSE-SBM partially resolved (lift 11/11 PASS; broadness 6/11 PASS with refinement-needed analysis on barbell)
extension_files: [50_hmorse_sbm_results, 59_hmorse_sbm_summary]
canonical_state_at_end: CV-1.16 SEALED unchanged (no canonical edits in this OP-HMORSE-SBM continuation)
---

# 59 — OP-HMORSE-SBM Robustness Extension Summary

## Headline

**OP-HMORSE-SBM partially resolved — 11/11 lift PASS, 6/11 broadness PASS with structural-degeneracy analysis on barbell.**

L-CLOSURE-LIFT Cat A (CV-1.16 canonical) is **fully robust** across all 11 valid runs (100% lift PASS): operator-norm $\|J_{\mathrm{Cl}}\|_{D \to D} \leq a_{\mathrm{cl}}/4 < 1$ propagates to every tested graph class (SBM, barbell, small-world).

L-HMORSE-LOCAL Cat B (CV-1.16 canonical) holds **on graphs satisfying effective (C3) single-formation**: SBM (high Fiedler) + small-world PASS, barbell at canonical $c = 0.2$ produces (C3)-violating minimizers (mass split across two near-disconnected cliques creates a *second near-zero eigenmode* beyond the volume Goldstone). The barbell "FAIL" is **not** a counterexample but a *condition violation*: D-HMORSE-LOCAL (C3) + effective (C4) symmetry-breaking are needed.

2 new open questions registered (`50_hmorse_sbm_results.md §5`):
- **OP-HMORSE-FIEDLER-BOUND** (MEDIUM): determine $\lambda_2^{\min}(\beta, n, c)$ for (C3) single-formation guarantee.
- **OP-HMORSE-ACTIVE-SET-EXTENSION** (LOW-MEDIUM): extend active set $A^*$ to include near-zero eigenmodes.

**No canonical revision needed.** CV-1.16 entries are correctly stated; OP-HMORSE-SBM refines applicability conditions rather than refuting them.

---

## Three-sentence summary

1. `exp_hmorse_sbm_robustness.py` executed 18-run sweep across SBM (n=40, 60), barbell (n=20, 30), small-world WS (n=40, 60) × $\beta \in \{10, 30, 100\}$; 7 runs hit T8-Core β_crit validation errors (well-connected graphs need β > 80–127 to enter phase-separation) and 11 valid runs were analyzed.
2. L-CLOSURE-LIFT Cat A is **fully robust** (11/11 lift PASS) — the operator-norm bound holds graph-independently in the degree-weighted form, and the standard-$\ell^2$ form's $d_{\min}/d_{\max}$ factor (as small as 0.165 on barbell_12_6) does not break the lift.
3. L-HMORSE-LOCAL Cat B holds for SBM + small-world but barbell produces (C3)-violating minimizers (Fiedler ~ 0.02–0.05, mass split between cliques, second-near-zero eigenmode at machine epsilon ~10⁻¹⁶); this is a *structural condition violation*, not a counterexample — refinement candidate via OP-HMORSE-FIEDLER-BOUND or OP-HMORSE-ACTIVE-SET-EXTENSION (both registered).

---

## Most-urgent next OP (for 5/15 plan author)

**OP-HMORSE-FIEDLER-BOUND** (MEDIUM severity, 1-2 sessions ETA).

**Why most urgent.** Directly refines the D-HMORSE-LOCAL applicability scope established in CV-1.16. The barbell counterexample analysis (`50_hmorse_sbm_results.md §3.3`) suggests $\lambda_2^{\min} \in [0.1, 0.2]$ at canonical β; explicit determination strengthens L-HMORSE-LOCAL Cat B to *quantitative* unconditional in a specific regime.

**Recommended deliverable for 5/15 (extend OP-HMORSE-SBM with quantitative Fiedler sweep):**
- `CODE/experiments/exp_hmorse_fiedler_sweep.py`: vary Fiedler systematically via barbell bridge_len (smaller bridge → larger Fiedler) or ring-rewire intermediate graphs.
- Determine the Fiedler threshold below which (C3) single-formation fails.
- Working file `THEORY/working/CV114_H_MORSE_PACKAGEII/12_fiedler_threshold.md`.
- If clean threshold emerges: CV-1.17 P7 promotion candidate (refine D-HMORSE-LOCAL (C3) → (C3+λ₂) bound).

---

## Alternative next priorities

| OP / Task | Severity | ETA |
|---|---|---|
| OP-HMORSE-FIEDLER-BOUND (Fiedler threshold for (C3)) | MEDIUM | 1–2 sessions |
| OP-HMORSE-ACTIVE-SET-EXTENSION (T^free,ext) | LOW-MEDIUM | 1 session |
| OP-HMORSE-LOCAL-A Cat A path (residual + SBM combined) | MEDIUM | 2 sessions |
| Package II Eyring-Kramers prefactor Cat B | HIGH | 3–5 sessions (needs OP-0021) |
| §F Step 2 housekeeping (CV-1.15 working file) | LOW | 0.5 session |
| OP-0021 dual-naming reconciliation | LOW (hygiene) | 0.5 session |

---

## Decision Gate self-check (Rule R1–R7)

| Rule | Check | Result |
|---|---|---|
| R1 — No language refactor | Used canonical/CV114/CV-1.16 vocabulary only | ✓ PASS |
| R2 — Canonical alignment pre-check | grep — no name collisions for `exp_hmorse_sbm_robustness.py` or new OPs | ✓ PASS |
| R3 — Numerical demo | Executed `exp_hmorse_sbm_robustness.py` 18 runs; mixed but interpretable results | ✓ PASS |
| R4 — Cat status honest | All claims labeled CONFIRMED / PARTIAL / NEEDS-REFINEMENT; barbell explicitly NOT counterexample | ✓ PASS |
| R5 — Round 4 external audit | Flagged for follow-up; deferred | ✓ flagged |
| R6 — Lifetime ceiling | Existing CV114 + daily log directory; no new working folder | ✓ PASS |
| R7 — Cat A precision | Did NOT claim L-HMORSE-LOCAL Cat A; (C3)/(C4) condition refinement noted honestly | ✓ PASS |

---

## Files Produced This Continuation

| File | Purpose |
|---|---|
| `CODE/experiments/exp_hmorse_sbm_robustness.py` | SBM/barbell/small-world robustness extension script |
| `CODE/experiments/results/exp_hmorse_sbm_robustness.json` | Raw 18-run results (7 errors + 11 valid) |
| `CODE/experiments/results/exp_hmorse_sbm_robustness.md` | Markdown summary |
| `THEORY/logs/daily/2026-05-14/50_hmorse_sbm_results.md` | Full analysis: per-graph breakdown, condition-violation diagnosis, 2 new OPs registered |
| `THEORY/logs/daily/2026-05-14/59_hmorse_sbm_summary.md` | (this file) — extension summary |

**NOT modified:**
- canonical files (CV-1.16 SEALED preserved; OP-HMORSE-SBM result refines rather than refutes).
- CV114 working folder (50_*.md serves as record; no separate working file needed yet).
- Test suite (215 passed, 1 xfailed regression check confirmed).

---

## Methodological Highlights

**Honest mixed-result reporting pattern.** Unlike CV-1.16 evening extension (clean 15/15 PASS), this OP-HMORSE-SBM continuation produced a *mixed* result. Two response patterns are available:

1. **Reframe as falsification:** "L-HMORSE-LOCAL Cat B falsified by barbell" → would trigger Cat B retraction, V-AFD/R-2 pattern (premature claim crumbling).
2. **Refine conditions:** Diagnose barbell as (C3) condition violation, register OP-HMORSE-FIEDLER-BOUND as refinement → keeps L-HMORSE-LOCAL Cat B intact in its valid scope while expanding the OP catalog.

This session adopted **pattern (2)**: honest condition-violation analysis preserves the canonical claim while transparently registering new refinement work. Compare V-AFD failure mode (premature Cat A claim → retraction); here the Cat B claim survives because its conditions are correctly stated (and explicitly require (C3)).

**Preserve as session-design template** for handling mixed numerical results on conditional theorems.

---

## Extension Session Slogan

> CV-1.16 SEALED → OP-HMORSE-SBM partial closure → 2 refinement OPs registered.
> L-CLOSURE-LIFT Cat A robustness fully confirmed (11/11 lift PASS) across SBM, barbell, small-world.
> L-HMORSE-LOCAL Cat B holds where (C3) single-formation is non-vacuous; barbell at canonical params produces (C3)-borderline minimizers — *not* a counterexample, *not* a Cat A claim crumbling; refinement via OP-HMORSE-FIEDLER-BOUND.
> Honest mixed-result reporting preserves CV-1.16 canonical state while expanding OP catalog.

---

## Cross-References

This continuation **extends** the CV-1.16 P7 promotion of the same session:
- CV-1.16 SEALED → 97 claims (~70% fully proved).
- OP-HMORSE-SBM was registered in CV-1.16_SEAL.md §"Outstanding Items" as 1-session ETA Tier 2 priority.
- This session executes that priority and produces the deliverable.

The 2 new OPs (OP-HMORSE-FIEDLER-BOUND, OP-HMORSE-ACTIVE-SET-EXTENSION) become CV-1.17 candidates alongside the previously-identified Package II / OP-HMORSE-LOCAL-A / OP-HMORSE-SBM tasks.

---

*Continuation session 2026-05-14 (post CV-1.16 SEAL) closed. Canonical state: CV-1.16 SEALED, 68A/18B/6C/5R = 97 claims, preserved unchanged. Next session 2026-05-15+: recommended first action = OP-HMORSE-FIEDLER-BOUND quantitative Fiedler sweep (extends `exp_hmorse_sbm_robustness.py` infrastructure).*
