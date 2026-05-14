---
type: working/afd
status: AFD-0 Draft (2026-05-12)
version: 0.1
---

> [!nav] Linked: [[MOC_AFD_0_foundation]] · [[THEORY_INDEX]]


# AFD-0 — Abstract Formation Dynamics Foundation

## Purpose

AFD-0 is the Layer-2 abstract dynamics layer of the SCC architecture. It sits between:

- **Layer 1 — SCC Core** (the field `u_t : X_t -> [0,1]`, the energy `E = lambda_cl E_cl + lambda_sep E_sep + lambda_bd E_bd`, the diagnostic vector `D = (Bind, Sep, Inside, Persist)`, the K-field architecture, and all Cat A/B results in `canonical/canonical.md`);
- **Layer 3 — Exact Stochastic Rate Theory** (Eyring-Kramers prefactors, Hessian-determinant formulae, Bovier-Eckhoff-Gayrard refinement, requiring H-MORSE-Local + H-MORSE-Saddle as Layer-3 regularity hypotheses).

AFD-0 isolates the **abstract** part of formation dynamics — formation states, their basins, barrier orderings, K-strata, diagnostic dynamics, topology signatures, and admissible transitions — from the Hessian-quantitative part. This separation is the central architectural commitment of AFD-0.

## Why a separate layer

The W6–W7 trajectory revealed that Package II / Eyring-Kramers requires nondegenerate Hessians at minima and at index-1 saddles (H-MORSE-Local + H-MORSE-Saddle, both currently Cat B targets, see `CV114_H_MORSE_PACKAGEII/`). Without those, exact rates are unavailable. However, almost every actually-needed downstream claim in SCC — basin existence, barrier ordering, K-stratum decomposition, diagnostic dynamics, formation-state transitions — does *not* need Hessian determinants. AFD-0 makes this independence explicit and proves it (Theorem AFD-T9).

The slogan: **AFD separates transition order from transition rate. EK refines AFD; AFD does not require EK.**

## Three-layer architecture (overview)

```
Layer 1 — SCC Core           [Cat A — canonical.md CV-1.13, 83 claims]
   |
   |  builds on
   v
Layer 2 — AFD-0              [this directory, draft v0.1]
   |
   |  optionally refined by
   v
Layer 3 — Refined Rate Theory [H-MORSE required, Package II target]
```

## File map

| File | Role |
|---|---|
| `README.md` | (this file) overview, status |
| `abstract_formation_dynamics.md` | main document — definitions AFD-D1..D15, theorems AFD-T1..T10, proofs |
| `afd_theorem_registry.md` | tabular index of AFD theorems with status/dependencies/gaps |
| `afd_open_problems.md` | OP-AFD-001 through OP-AFD-010 |
| `afd_audit.md` | 20-question honesty audit with overclaim corrections |
| `afd_hmorse_reclassification.md` | formal reclassification of H-MORSE as Layer 3 |
| `afd_examples.md` | 7 concrete worked examples on small graphs |
| `afd_framework_comparison.md` | comparison of 15 candidate frameworks (Conley, FW, EK, Morse, ...) |
| `afd_log.md` | chronological work log for AFD-0 |
| `afd_summary_for_next_agent.md` | compact handoff |
| `afd_layer_diagram.md` | ASCII layer diagram |

## Current status

- AFD-0 is **Draft v0.1** (2026-05-12).
- No definitions or theorems have been promoted to canonical.
- Status labels follow the SCC convention (Definition / Proposition / Theorem / Lemma Candidate / Conjecture / Design Principle / Open Problem / Warning).
- One Theorem in the formal sense (AFD-T9) is established by direct inspection of definitions. The remainder are Propositions, Theorems with partial proof using Cat A Layer-1 inputs, Lemma Candidates, or Design Principles.
- AFD-0 does *not* claim to resolve any open SCC problem (in particular it does not resolve OP-0005, OP-0008, OP-0009, OP-0021, or OP-0006-style barrier-quantification questions).

## Reading order

1. `afd_layer_diagram.md` (1 minute, picture).
2. `abstract_formation_dynamics.md` §0–§3 (architecture and SCC inputs).
3. `abstract_formation_dynamics.md` §4–§9 (the actual definitions).
4. `afd_hmorse_reclassification.md` (the central reclassification claim).
5. `afd_audit.md` (honesty check).
6. `afd_open_problems.md` (where to go next).

## Carry-forward (for next agent)

See `afd_summary_for_next_agent.md`. Top recommended next actions:

1. Prove OP-AFD-004 (positive merge barrier) analytically, using T7-Enhanced + T-Merge(b).
2. Pursue OP-AFD-005 (FW-to-SCC refinement) in parallel with the CV-1.14 H-MORSE-Local Cat B target in `CV114_H_MORSE_PACKAGEII/`.
3. Decide on canonical promotion of AFD-D1, AFD-D2, AFD-D5, AFD-T9.
