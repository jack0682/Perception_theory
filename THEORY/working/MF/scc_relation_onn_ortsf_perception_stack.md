---
id: NOTE-STACK-001
type: conceptual-note
status: stub
created: 2026-05-06
session: EOD Closeout
---

> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q4_K_selection]] · [[MOC_sigma_rich_framework]] · [[THEORY_INDEX]]


# SCC → RelationWorld → ONN → ORTSF: Perceptual Pipeline Note

*Conceptual note only. Not a theorem. Not a canonical claim. Created EOD closeout 2026-05-06.*

---

## 1. The Perceptual Pipeline

```
SCC (cohesion-first field)
  ↓ formations: PersComp(u_t), K_act, σ(C_i)
RelationWorld (relation/world grammar over SCC formations)
  ↓ world-state: relational structure between formations
ONN (ontological/semantic placement)
  ↓ ontological commitments: category assignment, constraint satisfaction
ORTSF (action, attention, memory, delay-robust control)
  ↓ action commands, memory updates, attention allocation
```

**Perceptual generation order**: cohesion → relation → meaning → action.

---

## 2. Layer Descriptions

### 2.1 SCC — Soft Cognitive Cohesion

- **Primitive:** soft cohesion field u_t : X_t → [0,1].
- **Output:** formations — cohesion regions detected before discrete objecthood.
- **Key theorems in play:** T8 (minimizer existence), T-OP6-B (boundary precision), T-K-Select-PF/OBS (K-selection), T-Temporal-Identity (inter-frame correspondence), T-σ-Inherit (signature inheritance).
- **Ontological stance:** formations are pre-objective. Crisp objects (discrete, labeled) are derivative and emerge only after RelationWorld assignment.

### 2.2 RelationWorld — Relation/World Grammar

- **Input:** SCC formations (as graph-structured cohesion regions with σ-signatures).
- **Role:** assigns discrete relational structure between formations (closure, distinction, co-belonging in the relational sense). Produces a "world-state" as a relational configuration.
- **Note on ontological breadth:** RelationWorld theory may be stated for any relational primitive — it is not inherently restricted to SCC-derived formations. However, in the perceptual generation pipeline, SCC is the entry point and RelationWorld receives SCC output.

### 2.3 ONN — Ontology Neural Networks

- **Input:** RelationWorld relational world-state.
- **Role:** constraint-based fixed-point solver. Maps relational structure to ontological categories (semantic placement).
- **Output:** ontological commitments — which formations are instances of which categories, under which relational constraints.

### 2.4 ORTSF — Ontology-based Robust Topological Sequencing Framework

- **Input:** ONN outputs + temporal identity (T-Temporal-Identity correspondence R_{t→s}) + σ-signatures.
- **Role:** delay-robust control stabilization, attention allocation, memory formation, action command generation.
- **Output:** action commands, updated attention, memory trace.

---

## 3. Ontological vs. Perceptual Ordering

| Dimension | Ordering |
|---|---|
| Perceptual generation | SCC → RelationWorld → ONN → ORTSF |
| Ontological generality | RelationWorld ≥ SCC (RelationWorld is not restricted to SCC primitives) |
| Foundational primitive | u_t : X_t → [0,1] (SCC); objects are derivative |

The two orderings are not contradictory: RelationWorld may be ontologically broader (applicable to any relational primitive), but perceptually, the system generates coherence (SCC) before grammar (RelationWorld).

---

## 4. Open Questions (as of CV-1.11)

1. **SCC → RelationWorld boundary:** How do SCC formation boundaries (T-OP6-B: d_H ≤ 2(α/β)^{1/2}) map to RelationWorld node boundaries? Is there a formal translation?

2. **Temporal identity as memory:** How does T-Temporal-Identity (R_{t→s} correspondence) feed into ORTSF memory formation? Does σ-inheritance (T-σ-Inherit) provide the semantic continuity signal?

3. **K-selection as attention:** Does T-K-Select-OBS (posterior K* given observation O_t) implement a form of attentional selection? The K* = argmin F_obs(K) chooses the perceptually-preferred object count.

4. **T-MF-Synthesis formal statement:** The future T-MF-Synthesis candidate will assert that SCC + RelationWorld layers together constitute a static + equilibrium emergent multi-formation theory. Formal statement pending T-Temporal-Identity + T-σ-Inherit canonical.

---

## 5. Status and Caveats

- This document is a **conceptual note**, not a theorem.
- No formal proofs are made here.
- RelationWorld theory is a separate research project (see `theory/` directory in the parent repo).
- ONN and ORTSF are separate projects (see `ONN/` directory).
- The pipeline description is the author's current working model and may evolve.
- **This document does NOT promote T-MF-Synthesis or any working candidate.**

---

*End of stub. To be fleshed out once T-Temporal-Identity and T-σ-Inherit reach canonical status.*
