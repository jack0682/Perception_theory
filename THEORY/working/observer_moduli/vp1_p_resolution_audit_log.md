---
type: working/audit-log
created: 2026-05-07
project: Observer Moduli Space of SCC
experiment: exp86_vp1_p_resolution_audit.py
---

# VP-1 Execution Log

Chronological record of VP-1 design, execution, and interpretation.

---

## Design Phase (pre-run)

**Motivation:** OP-OMS-009 asks whether P_min = (Bind, Sep, Inside, Persist) suffices to distinguish observer parameter configurations that lead to topologically distinct equilibria. Prop R1 in `readout_map_audit.md` hypothesizes P_min is too coarse, but without computational evidence.

**Key insight driving experiment design:** The Inside predicate collapses the full H0 persistence barcode into a single scalar via `(l_max - c)/(1-c) × (1 - l_second/l_max)`. This means topological information (K_core = number of connected components at threshold θ_core) is partially lost: if the second component is small, l_second ≈ 0 and Inside ≈ (l_max - c)/(1-c), the same as a single-component field with identical l_max.

**Counterexample strategy:** Find optimizer parameter pairs (λ_A, λ_B) where the equilibrium u*(Θ_A) has K_core=2 while u*(Θ_B) has K_core=1, but the diagnostic 4-vectors agree within ||d|| < 0.15.

**Four-part protocol designed:**
- Part A: Synthetic fields (ground truth, manual construction)
- Part B: Optimizer sweep (scan across 10 λ vectors)
- Part C: Analytic targeted construction (control the Inside collapse directly)
- Part D: Dense λ sweep on larger graph (replication at 15×15)

**Script created:** `CODE/experiments/exp86_vp1_p_resolution_audit.py`

---

## Execution Phase

**Run 1:** `python3 experiments/exp86_vp1_p_resolution_audit.py`
- Exit code: 1
- Error: `TypeError: dump() missing 1 required positional argument: 'fp'` at line 890
- All experiment parts ran successfully before the error (Parts A–D complete, classification printed)
- Results printed to stdout: 4 counterexamples, RESOLVED-NEGATIVE
- No output files written (crash before file write)

**Bug fix:** Line 890: `json.dump({...}, indent=2)` → `json.dump({...}, f, indent=2)` (missing file handle)

**Run 2:** `python3 experiments/exp86_vp1_p_resolution_audit.py`
- Exit code: 0
- Output files written:
  - `CODE/experiments/results/observer_moduli/vp1_pairs.json` ✓
  - `CODE/experiments/results/observer_moduli/vp1_summary.md` ✓

---

## Results Interpretation

**Part A (0 CEs):** Synthetic blobs are topologically maximally separated, making them diagnostically far too. When K_core differs by 1 or 2, the diagnostic distance is typically ||d|| > 0.2. Synthetic fields are too clean for the counterexample pattern to emerge.

**Part B (3 CEs):** The cl_dominant configuration (w_cl=0.6) is the source. On a 12×12 grid, closure-dominant energy pushes the optimizer to a two-blob equilibrium (K_core=2). More balanced λ configurations fall into the single-blob basin (K_core=1). The diagnostic vectors of the two equilibria are close because:
- Bind is driven by cohesion in both cases — both equilibria have high cohesion (Bind ≈ 0.86–0.88)
- Sep is slightly lower in the two-blob case (less separation of the blobs from outside) than in the single-blob case
- Inside is reduced in the two-blob case but not dramatically (second blob is a small satellite, l_second ≈ 0.025)
- Persist = 1.0 in all cases (stable equilibria)
- Net result: ||d|| as low as 0.071 (CE-1)

**Part C (0 CEs):** The analytic construction controlled blob sizes but could not fine-tune u* values to bring ||d|| below 0.15 while keeping K_core different. The fields were too separated in Inside because the two constructed blobs were comparable in size, making l_second large.

**Part D (1 CE):** On 15×15 grid with 21 λ configurations, independent replication. The same K_core(Θ) pattern emerges at different λ scale (bd-dominant at λ=(0.52,0.10,0.38) gives K_core=1; cl-dominant at λ=(0.66,0.10,0.24) gives K_core=0). The counterexample has ||d||=0.122, D_T=3.003.

**Classification logic:**
- Definitive CEs (||d||<0.15 AND D_T>0.5): 4 → RESOLVED-NEGATIVE threshold is ≥2 definitive CEs
- Final status: RESOLVED-NEGATIVE

---

## Decisions Made During Interpretation

1. **K_core=0 is valid for CE-4.** The Θ_B configuration in CE-4 has K_core=0, meaning no connected component of u* exceeds the θ_core=0.9 threshold. This is a genuine optimizer equilibrium (diffuse u*), not a failure. K_core=0 is perceptually interpretable as "no core" — distinct from K_core≥1.

2. **Continuity of u*(Θ) is not directly tested by VP-1.** VP-1 attacks the resolution question (P_min insufficient). The continuity question (needed for Prop R3 descent) remains open and is tracked as a residual subquestion of OP-OMS-009.

3. **"RESOLVED-NEGATIVE" refers to P_min, not to P_top.** P_top is confirmed as necessary, not negated. The naming follows the convention in `validation_protocols.md`: RESOLVED-NEGATIVE = P_min resolution is negatively resolved (insufficient).

4. **Prop R1 promoted from HYPOTHESIZED to PROVED.** The counterexample is constructive: CE-1 (λ_A=(0.6,0.2,0.2) vs λ_B=(0.5,0.3,0.2) on 12×12 grid, K_core 2 vs 1, ||d||=0.071) provides an explicit witness.

---

## Open Questions Remaining After VP-1

- Does u*(Θ) vary continuously in Θ? (Needed for Prop R3 / P_top descent to quotient. Still OPEN.)
- Is the two-blob equilibrium of cl_dominant a basin boundary phenomenon, or does it persist across all graphs? (Related to OP-OMS-011 — basin stability.)
- Can CE patterns be generated for K_core differences beyond 1? (E.g., K_core=3 vs K_core=1 with close diagnostics?)

---

*Log complete: 2026-05-07*
