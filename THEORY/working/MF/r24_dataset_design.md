# r24_dataset_design.md — R24 Dataset Design (R23 Successor) for Bridge B-2 σ-locality

**Status:** working draft (W5 Day 4 PM Wave 3 lead-side direct work, 2026-04-30).
**Type:** Numerical infrastructure design.
**Author:** team-lead@scc-wave3-deep-research.
**Canonical refs:** §13 T-PreObj-1G; T-σ-Theorem-3 (closed form); NQ-188 σ-class enumeration.
**Working refs:** `foundational_bridges_2026.md` §3 Bridge B-2; `theorem_2g_schramm_restatement.md` (Schramm-locality reframing); `sigma_locality_R23_cycle_torus.json` (Wave 3 schramm-locality-prover).

---

## §1. Mission

Bridge B-2 σ-locality theorem (NQ-262 Cat BC target) was numerically verified on 3 graph classes by schramm-locality-prover teammate (Wave 3): R23 D_4 free-BC L=8, Z_n cycle n=20, Z_n×Z_n torus n=10. All 3 satisfied the locality predicate.

To strengthen the empirical evidence:
- **R24 dataset** = R23 + extended graph-class enumeration covering more diverse Aut(G) structures.

---

## §2. R24 specification

### §2.1 Graph classes (8 total)

| Graph | Aut(G) | Order | Notes |
|---|---|---|---|
| R23 D_4 free-BC L=32 | D_4 | 8 | Full R23 baseline (existing 56 stable minimizers) |
| Z_n cycle n=20 | D_n | 40 | 1D translation symmetry |
| Z_n cycle n=50 | D_n | 100 | 1D large-n |
| Z_n × Z_n torus n=10 | (D_n)² wreath | 800 | 2D torus, full D_n action |
| Z_n × Z_n torus n=15 | (D_n)² wreath | 1800 | 2D large-n torus |
| Petersen graph (10 nodes) | (S_5)² | 120 | high-symmetry small graph |
| Cycle 6 (Hexagon) | D_6 | 12 | smaller D-family |
| Truncated tetrahedron | S_4 | 24 | 3D-like graph |

### §2.2 Per-graph protocol

For each graph $G$:
1. Compute Aut(G) explicitly via NetworkX or PyNAUTY.
2. Compute Aut(G)_{u_uniform} (= Aut(G) at uniform vacuum).
3. Compute first non-trivial Laplacian eigenvalue $\lambda_2^{\mathrm{Lap}}$ + Fiedler eigenvector $\phi_2$.
4. Compute $\beta_{\mathrm{crit}}^{(2)} = 4\alpha\lambda_2 / |W''(c)|$ at $\alpha=1$, $c=0.5$, $|W''|=1$.
5. Run `find_formation` from $u_0 = c\mathbf{1} + 0.30 \phi_2$ at $\beta = \beta_{\mathrm{crit}}^{(2)} + 0.05$ (post-pitchfork).
6. Compute σ-tuple at minimizer: bottom-k Hessian eigenvalues (k=4-12 depending on n).
7. Identify Aut(G)_{u_*}-irrep labels via character projection.
8. Output: `R24_<graph_name>.json` with all extracted data.

### §2.3 σ-locality predicate verification

For each pair $(G_i, G_j)$:
- Check if Aut(G_i)_{u_uniform} ≅ Aut(G_j)_{u_uniform} as abstract groups.
- If isomorphic, check σ-tuple agreement up to NQ-188 conjugation rule.
- Tally: `n_iso_pairs`, `n_locality_holds`, `n_locality_fails`.

### §2.4 Cat A criterion strengthening

Original Wave 3 verification (3 graph classes): all 3 locality predicates held.

R24 strengthening (8 graph classes, 28 pairs): if all locality predicates hold (per applicable cases), Bridge B-2 σ-locality theorem gains substantial empirical anchor → Cat A target via continuum-limit theoretical argument feasible.

---

## §3. Implementation outline

CODE/scripts/generate_R24.py (proposal):

```python
"""Generate R24 dataset for Bridge B-2 σ-locality verification.

Reads:
- Graph specs (class + parameters) from inline list.
- α=1, c=0.5, ε=0.05 fixed.

Outputs:
- CODE/data/R24/<graph_name>.json per graph.
- CODE/data/R24/_summary.json with cross-graph σ-locality tallies.

Effort: ~6h compute + 2-3h script writing.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import json
import numpy as np
import networkx as nx
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.optimizer import find_formation

# ... (graph-class generators, Aut(G) computation, σ-tuple extraction, etc.)
```

Key challenges:
- **Aut(G) computation**: PyNAUTY or NetworkX for graph automorphism group. Computational cost is the bottleneck for large graphs (Petersen, large tori).
- **Irrep character projection**: requires character table for each Aut(G); use sage or hand-compute for small groups.
- **find_formation convergence**: may need parameter tuning (η_BB step, max iterations) for unfamiliar graphs.

---

## §4. R24 vs R23 differences

| Aspect | R23 | R24 |
|---|---|---|
| Graph class count | 1 (D_4 free-BC) | 8 |
| Pairs for σ-locality | 0 (single class) | 28 |
| Aut(G) diversity | low (D_4 only) | high (D_4, D_n, (D_n)², (S_5)², D_6, S_4) |
| Stable minimizers per graph | 56 (R23 90-run enumeration) | 10-50 per graph |
| Compute estimate | already done | +6h numerical + 3h analysis |

---

## §5. CV-1.7+ Bridge B-2 promotion target

R24 numerical anchor ⇒ Bridge B-2 σ-locality theorem candidate for Cat A canonical promotion at CV-1.7 (post-CV-1.6 release).

Promotion path:
- W6 D5-D6: R24 dataset generation (this file's protocol).
- W7 D1-D3: R24 σ-locality verification + theoretical proof refinement (continuum extrapolation).
- CV-1.7 release (~W7-W9): canonical T-PreObj-1G Schramm-restatement (Wave 3 theorem_2g_schramm_restatement.md L3) promoted to Cat A with R24 numerical anchor.

---

## §6. Hard constraint verification

- [x] **u_t primitive maintained**: dataset operates on cohesion field minimizers; primitive unchanged.
- [x] **CN10 contrastive**: R24 is a SCC numerical dataset, no external theory imports.
- [x] **CN5 4-energy not merged**: σ-tuples computed on full $\mathcal{E}$ minimizers.
- [x] **OP not silently resolved**: NQ-262 / Bridge B-2 / Schramm-restatement remain as proposed; R24 strengthens but does not resolve.

---

## §7. Cross-references

- `working/MF/foundational_bridges_2026.md` §3 Bridge B-2.
- `working/SF/theorem_2g_schramm_restatement.md` (Wave 3 lead, T-PreObj-1G Schramm-locality reframing).
- `CODE/scripts/sigma_locality_R23_cycle_torus.py` (Wave 3 schramm-locality-prover).
- `CODE/scripts/results/sigma_locality_R23_cycle_torus.json` (Wave 3 verification 3 graphs).
- `CODE/results/exp_orbital_fullscale.json` (R23 56 stable Morse-0 minimizers).

---

**End of r24_dataset_design.md.**

**Status:** R24 dataset specification (8 graph classes, 28 pairs for σ-locality verification). Working-only design doc. Implementation: ~6h compute + 2-3h script. CV-1.7+ promotion target for Bridge B-2 Cat A.
