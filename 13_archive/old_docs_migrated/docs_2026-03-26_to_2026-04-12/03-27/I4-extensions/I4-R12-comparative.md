# Iteration 4 R12 — Comparative Framework Analysis

**Author:** CogSci Bridge | **Iteration:** 4, Round 12

---

## DISTINCTIVENESS MATRIX (7 Properties vs 7 Frameworks)

| Framework | P1 NI-Cl | P2 Triad | P3 Transport | P4 Recovery | P5 Self-Sep | P6 NL-Dyn | P7 Meta | Score |
|---|---|---|---|---|---|---|---|---|
| Mumford-Shah | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **7/7** |
| Chan-Vese | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | 6.5 |
| Potts/Ising | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | 6.5 |
| Spectral Cluster | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | 6.5 |
| Persistent Homology | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | 6.5 |
| **Allen-Cahn** | ✓ | ✓ | ~ | ✓ | ✓ | ~ | ~ | **5/7** |
| **Turing R-D** | ✓ | ✓ | ~ | ✓ | ✓ | ~ | ~ | **5/7** |

SCC most similar to Allen-Cahn/Turing (sharing dynamics + metastability). Most different from Mumford-Shah (sharing nothing).

## DISTINCTIVE CORE

**Operator triad (P2)** and **self-referential separation energy (P5)** have NO analogue in any comparison framework.

## SINGLE SENTENCE

"SCC is a self-referential Allen-Cahn with an axiomatized operator algebra, a structurally novel separation energy, and a topological recovery interface — where 'self-referential' means the field generates the operators that generate the energy that determines the field."

## KEY COMPARISON: SCC vs Allen-Cahn (closest relative)

- E_bd IS Allen-Cahn. Shared.
- E_cl (closure self-consistency) has NO Allen-Cahn analogue. Deepens basins (T7).
- E_sep (self-referential distinction) has NO analogue in ANY phase-field theory.
- Sharp-interface limit (T11) gives MODIFIED surface tension. Proved.
- Anti-Turing instability (R10 preliminary) — SCC may have opposite instability structure.
