---
type: working/vp1-results
created: 2026-05-07
version: 1.0
project: Observer Moduli Space of SCC
experiment: exp86_vp1_p_resolution_audit.py
op_target: OP-OMS-009
result: RESOLVED-NEGATIVE
---

# VP-1 Results: P-Resolution Audit

## Final Classification

**OP-OMS-009 (Readout resolution completeness):** RESOLVED-NEGATIVE

P_min = (Bind, Sep, Inside, Persist) is too coarse to serve as a canonical readout map for the Observer Moduli Space. Explicit counterexamples show that diagnostically-near observer configurations (||d|| < 0.15) can have distinct topological types (K_core differs by 1).

**Counterexamples found:** 4 definitive (||d|| < 0.15 AND D_T > 0.5)

---

## Summary Table

| Part | Grid | Configs | Pairs | CEs | ||d||_min |
|------|------|---------|-------|-----|----------|
| A — Synthetic fields | 12×12 | 6 fields | 15 | 0 | — |
| B — Optimizer λ sweep | 12×12 | 10 λ configs | 45 | **3** | 0.071 |
| C — Analytic construction | 10×10 | 3 fields | 3 | 0 | — |
| D — Dense λ sweep | 15×15 | 21 λ configs | 210 | **1** | 0.122 |

**Tightest counterexample:** CE-1 (Part B), ||d||=0.071, D_T=3.028, K_core 2 vs 1.

---

## Updated Proposition Status

| Proposition | Previous status | New status |
|---|---|---|
| Prop R1 (P_min too coarse) | HYPOTHESIZED | **PROVED** (exp86 CE-1) |
| Prop R3 (P_top descent) | CONDITIONAL (u* continuity) | CONDITIONAL (unchanged) |

---

## Updated Open Problem Status

| OP | Title | Previous | New |
|---|---|---|---|
| OP-OMS-009 | Readout resolution + u* continuity | OPEN (blocker) | **RESOLVED-NEGATIVE** |

**Note:** OP-OMS-009 had two sub-questions:
1. Is P_min sufficient? → **No** (RESOLVED, this VP-1)
2. Is u*(Θ) continuous? → Still **OPEN** (required for Prop R3 descent)

The resolution sub-question is closed. The continuity sub-question is retained as an ongoing concern but is no longer a blocker for the P_min finding.

---

## Canonical Promotion Impact

OP-OMS-009 was one of three canonical blockers. Its resolution removes one blocker:

| Blocker | Status |
|---|---|
| OP-OMS-001 (G_core-weight trivial?) | OPEN — VP-3 needed |
| OP-OMS-002 (V ∈ V_adm exists?) | OPEN — VP-2 needed |
| **OP-OMS-009 (P_min insufficient?)** | **RESOLVED-NEGATIVE** |

OMS canonical promotion now requires: VP-3 (OP-OMS-001) and VP-2 (OP-OMS-002).

---

## Recommended Next Steps

1. **VP-3 (core-weight symmetry)** — attacks OP-OMS-001. If G_core-weight = {e} is confirmed computationally, the second blocker is addressed.
2. **VP-2 (basin discovery)** — attacks OP-OMS-002. Demonstrate that at least one V ∈ V_adm exists by showing V_D^0 satisfies criteria V1–V5.
3. **Prove u*(Θ) continuity** — closes the residual subquestion of OP-OMS-009, enabling Prop R3.

---

## Evidence File

`CODE/experiments/results/observer_moduli/vp1_pairs.json` — full counterexample data (4 CEs with diagnostics, topology signatures, λ vectors)

`CODE/experiments/results/observer_moduli/vp1_summary.md` — machine-readable summary

`THEORY/working/observer_moduli/vp1_counterexamples.md` — detailed analysis of each CE

`CODE/experiments/exp86_vp1_p_resolution_audit.py` — reproducible experiment script

---

*Results finalized: 2026-05-07*
