---
type: working/log
created: 2026-05-08
session: Session 4 (VP-3)
project: Observer Moduli Space of SCC
attacks: OP-OMS-001
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# VP-3 Initial Reading Log — Core-Weight Symmetry Test

## Mission

VP-3 tests all candidate λ-space transformations against P_top readout to determine
which (if any) are genuine gauge symmetries of the observer moduli space.
Target: attack OP-OMS-001 computationally.

## State at Session Start

### OP-OMS-001 Status (pre-VP-3)

| Sub-question | Pre-VP-3 Status |
|---|---|
| S4 permutation symmetry? | REJECTED (Prop CW1 — theoretical) |
| Closure-separation swap (g1)? | COMPUTATIONALLY TESTABLE (Protocol CW-1) |
| Boundary-closure compensation (g2)? | HYPOTHESIZED local approx. (Protocol CW-2) |
| Boundary-separation compensation (g3)? | COMPUTATIONALLY TESTABLE |
| Transport invariance on static scenes? | PROVED conditional (Prop CW2) |
| Radial perturbations? | COMPUTATIONALLY TESTABLE |
| Default G_cw = {e}? | ASSUMED (conservative) |

### Key Documents Read

1. **core_weight_symmetry.md** — Prop CW1 (S4 REJECTED), Prop CW2 (static transport),
   Def CW1 (G_cw group), Protocols CW-1/CW-2/CW-3. Transformations g1..g4 defined.

2. **observer_landscape_candidates.md** — V_adm class (V1..V5), V-P as best candidate.
   P_top = (d_Θ, T_Θ). Computational placeholder: V_D^0 with d* = (1,1,1,0).

3. **basin_stratification.md** — Prop BS1 (multiple basins on connected M); gradient flow;
   absorbing wall structure; Prop BS1 PROVED (conditional).

4. **readout_map_audit.md (from prior session)** — Prop R1 PROVED by VP-1 (P_min too coarse);
   T_Θ = (K_core, H0 barcode, l_max, l_second, artic, K_mid, K_low);
   counterexample criterion: ||d_A - d_B|| < 0.15 AND D_T > 0.5.

5. **exp86_vp1_p_resolution_audit.py (from prior session)** — Code structure for:
   full_topo_sig, _full_h0_bars, _component_count_at_threshold, D_T metric.

### VP-1 Carry-Forward

VP-1 (exp86) found 4 counterexamples to P_min injectivity:
- CE-1 (tightest): λ_A=(0.6,0.2,0.2) vs λ_B=(0.5,0.3,0.2), ||d||=0.071, D_T=3.028, K_core 2 vs 1
- These confirm Prop R1 and set the baseline: even small λ shifts (0.1 on one coord) can
  change K_core, and this is NOT captured by aggregate diagnostics d.

### VP-3 Test Matrix

Transformations to test (families A-G):

| ID | Name | Transformation | Protocol |
|---|---|---|---|
| A | Closure-sep swap | λ → (λ_sep, λ_cl, λ_bd, λ_tr) | CW-1 |
| B | Closure-bd swap | λ → (λ_bd, λ_sep, λ_cl, λ_tr) | new |
| C | Bd-cl compensation | λ_cl += δ, λ_bd -= δ (vary δ) | CW-2 |
| D | Bd-sep compensation | λ_sep += δ, λ_bd -= δ (vary δ) | new |
| E | Transport ablation | λ_tr → 0, rescale others | CW-3 |
| F | Radial toward center | λ → (1-t)λ + t(1/4,1/4,1/4,1/4) | new |
| G | Random tangent | λ → λ + δ·v, project to Δ³ | new |

### Code Entry Points (from exp86)

```python
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation, project_volume
from scc.diagnostics import diagnostic_vector, bind_predicate, sep_predicate, \
    inside_predicate, persist_predicate, _persistence_h0_graph
# Plus full_topo_sig, _full_h0_bars, _component_count_at_threshold (replicated from exp86)
```

### Success Criterion (VP-3)

Transformation g is NOT a symmetry if:
- For most λ samples: ΔP_top(λ, g(λ)) > 0.05 (combined d + topology distance)
- Alternatively: K_core changes for majority of test cases

Transformation g IS a candidate symmetry if:
- ΔP_top < 0.05 for >90% of samples
- Upgrade status from COMPUTATIONALLY TESTABLE → HYPOTHESIZED (global)

### Scenes Used

- Scene 1: Grid 8×8 (two sub-clusters, left vs right half)
- Scene 2: Path graph n=30 (single elongated formation)
- Scene 3: Grid 6×6 with central clique (structured topology)
- Scene 4: Two disjoint cliques (K_core sensitivity)

### Output Files Planned

- `CODE/experiments/exp87_vp3_core_weight_symmetry.py`
- `CODE/experiments/results/observer_moduli/vp3_symmetry_results.json`
- `CODE/experiments/results/observer_moduli/vp3_symmetry_summary.md`
- `THEORY/2_substrate/foundations/observer_moduli/vp3_core_weight_symmetry_results.md`
