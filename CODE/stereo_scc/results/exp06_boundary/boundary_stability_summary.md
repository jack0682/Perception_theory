> [!nav] Linked: [[MOC_experiments_validation]] · [[THEORY_INDEX]]

# exp06: Boundary Stability Summary (OP-0006)

## Setup

- Grid: 20x20, alpha=1.0, beta=10.0 (phase-separated)
- Reference: K=1, |B_ref|=52, |B_ref_pers|=98
- Boundary threshold θ=0.15, ρ_bd=0.05

## Shadow Results

| s | Δ_raw | Δ_SCC | ratio | claim |
|---|---|---|---|---|
| 0.2 | 0.1574 | 0.1157 | 1.361 | SUPPORTED |
| 0.3 | 0.2493 | 0.1156 | 2.157 | SUPPORTED |
| 0.5 | 0.4639 | 0.1136 | 4.085 | SUPPORTED |
| 0.7 | 0.7479 | 0.2084 | 3.589 | SUPPORTED |
| 0.8 | 0.9202 | 0.67 | 1.373 | SUPPORTED |

## Blur Results

| σ | Δ_raw | Δ_SCC | ratio | claim |
|---|---|---|---|---|
| 0.5 | 0.2312 | 0.1156 | 2.0 | SUPPORTED |
| 1.0 | 0.6354 | 0.1133 | 5.607 | SUPPORTED |
| 1.5 | 0.8253 | 0.0847 | 9.746 | SUPPORTED |
| 2.0 | 0.9288 | 0.0183 | 50.804 | SUPPORTED |
| 3.0 | 1.0174 | 0.0574 | 17.74 | SUPPORTED |

## Summary

- Shadow: 5/5 conditions SUPPORTED
- Blur: 5/5 conditions SUPPORTED
- Max shadow stability ratio: 4.085

## OP-0006 Cat B Criterion 3 Status: **SUPPORTED**

Cat B promotion requires: stability ratio > 1 for s >= 0.3 (shadow).
Cat A promotion requires: topological stability proof + stereo conditioning.
