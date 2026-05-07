---
type: working/plan
created: 2026-05-07
project: Observer Moduli Space of SCC
status: active
---

# Observer Moduli Space — Execution Plan

## Objective

Produce the first canonical mathematical definition of the SCC Observer Moduli Space:

$$\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} = \mathcal{M}_{\mathrm{obs}} / G_{\mathrm{SCC}}^{(0)}$$

This converts the informal idea (developed 2026-05-07 in conversation) into a precise mathematical object with definitions, propositions, toy models, and open problems.

## Context

This work originates from a conversation about:
1. Observer parameters not being fully independent
2. Compact gauge groups needed to preserve perceptual core
3. Observer as a dynamical system with attractor basins
4. Effective degrees of freedom being low (1-3)
5. Moduli space as the right framing for perceptual equivalence classes

This is a **Level-2 SCC extension** — lifting the SCC field machinery one level to observer parameter space. Not yet canonical; lives in `THEORY/working/observer_moduli/`.

## 7-Step Execution Plan

### Step 1: Parameter space definition
**File:** `definitions.md`
- List all components of Θ = (q, λ, ξ)
- Specify domain of each component
- Classify: observer-controlled / scene-determined / diagnostic / fixed
- Define M_raw, M_obs, M_obs^crit

### Step 2: Readout map
**File:** `definitions.md` (continued)
- Define P_min, P_top, P_full
- Justify topology inclusion over diagnostic-only
- Define perceptual core formally

### Step 3: Gauge group
**File:** `definitions.md` (continued)
- Define G_SCC^(0) = S_K × Aut_task
- Define Aut_task carefully (task-anchored)
- Set G_core-weight = {e} as default
- Register future symmetry as OP-OMS-001

### Step 4: Moduli space and orbifold
**File:** `observer_moduli_space.md` (main document)
- Define quotient formally
- State finite gauge dimension theorem
- Describe stabilizer stratification
- Orbifold structure

### Step 5: Toy models
**File:** `toy_models.md`
- K=1: compute Δ³ topology
- K=2: compute Sym²(A), diagonal singularity

### Step 6: Open problems + audit
**Files:** `open_problems.md`, `audit_log.md`
- OP-OMS-001 through OP-OMS-008
- Overclaim warnings
- Rejected candidates

### Step 7: Integration
**Files:** `THEORY/working/INDEX.md`, `THEORY/CHANGELOG.md`
- Add observer_moduli to INDEX.md
- Log creation in CHANGELOG.md

## File Manifest

| File | Status | Priority |
|---|---|---|
| `plan.md` | ✓ Done | — |
| `pre_brainstorm.md` | pending | high |
| `daily_log.md` | pending | high |
| `definitions.md` | pending | critical |
| `toy_models.md` | pending | critical |
| `open_problems.md` | pending | high |
| `audit_log.md` | pending | high |
| `checkpoints.md` | pending | medium |
| `observer_moduli_space.md` | pending | critical |

## Key Mathematical Decisions (Pre-committed)

1. **U(1) rejected**: Not valid for real positive (α, β). Use ℝ_{>0}-scale quotient + normalization.
2. **G_core-weight = {e}**: Not assumed, must be discovered.
3. **Finite gauge groups**: Do NOT reduce dimension. Only remove representation redundancy.
4. **Criticality hypothesis**: q = q_c(X_t) = 4λ₂/|W''(c)| — makes q scene-determined.
5. **P_top recommended**: Topology-including readout over diagnostic-only.
6. **M_obs is compact**: By finite product of compact sets (Tychonoff).
7. **Δ³ is contractible**: Perceptual discontinuity from V(Θ), not from M topology.

## Dependency Order

```
plan.md ← done
    ↓
pre_brainstorm.md + daily_log.md
    ↓
definitions.md
    ↓
toy_models.md + open_problems.md + audit_log.md  [parallel]
    ↓
observer_moduli_space.md  [integrates all above]
    ↓
INDEX.md + CHANGELOG.md  [integration]
```

## Success Criteria

- [ ] M_obs formally defined with all components listed
- [ ] M_obs^crit defined (criticality hypothesis applied)
- [ ] P formally defined (P_top recommended)
- [ ] G_SCC^(0) formally defined
- [ ] 𝔐_SCC^obs = M_obs/G defined
- [ ] K=1 toy model fully computed
- [ ] K=2 toy model fully computed (Sym², diagonal singularity)
- [ ] Finite gauge dimension issue explicitly stated
- [ ] V(Θ) requirements listed (not over-defined)
- [ ] OP-OMS-001 through OP-OMS-008 registered
- [ ] Audit log written with overclaim warnings

## Notes for Future Agents

- This is **working/ material**, not canonical. Do not promote without proof.
- The main theoretical question: "Is the moduli space connected?" Answer: For minimal Δ³, yes. For larger M_obs, unclear (OP-OMS-003).
- The observer dynamics (Θ_o(t) = F^t(s_o)) are NOT formalized here — that is a separate extension (Level-3 SCC).
- Connection to RelationWorld Theory: compact gauge groups on finite graphs may share mathematical structure.
