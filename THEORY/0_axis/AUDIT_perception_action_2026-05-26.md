---
id: AUDIT-PA-2026-05-26
type: axis/audit
created: 2026-05-26
status: rationale-of-record (basis for the perception-action stack reorganization)
description: Adversarial audit verdict that motivated the 2026-05-26 reorganization of the repo into a perception-action stack. Read alongside CANONICAL_AXIS.md and DECLARATION.md (DECL-2.0).
---

> [!nav] Parent: [[THEORY_INDEX]] · Pair: [[CANONICAL_AXIS]] · [[DECLARATION]] · [[perception_action_interpretation_pivot_2026_05_21]]

# Perception-Action Axis Audit (2026-05-26)

Adversarial research-architecture audit answering: *is the framework structurally organized around the perception-action interpretation gap* — the double-translation defect where a system interprets the world once as objects/labels/tokens, then re-interprets those into action-relevant structure (affordance, contact, reachability, compliance), so that `perception representation ≠ action representation`?

This document is the rationale of record for the reorganization executed on 2026-05-26. It is preserved unedited as the "why."

---

## A. Executive Verdict — PARTIAL

*Named and reframed, not solved, and (at audit time) not structurally load-bearing.*

The repo recognized the gap explicitly (the 2026-05-21 PAI pivot states the thesis verbatim) and had a pivot doc, roadmap, six open problems (OP-PAI-001..006), and a vocabulary. But by the real standard — *is the framework organized around the gap?* — no, not yet:

1. **The mathematical body was 100% object-cohesion.** All 102 sealed claims, the four energy terms, the four diagnostics, T8, and Q1–Q6 are about *when a difference-cluster becomes an object*. Zero proved content touched action/affordance/intervention/control.
2. **The PAI layer carried 0 proofs and 0 code** — 6 DEFINITION-DRAFTs + 6 OPEN problems. The pivot itself says (§7) "PAI solves the perception problem. It does not" and (§2) "It is not a proved theorem… a research orientation."
3. **The pivot was explicitly parallel, not central** (pivot §8; `DECLARATION` L183 deferred DECL-2.0). The canonical center remained objecthood by the repo's own bookkeeping.

Characterization: a sealed, serious phase-field morphology theory of objecthood, with an honest sticky-note declaring the real goal is perception-action unity — a goal the theory did not yet reach.

## B. Repository Map of Alignment (at audit time)

- **[A] strongly aligned:** `perception_action_interpretation_pivot_2026_05_21.md`, `PAI_ROADMAP.md`, `macro_audit_2026-05-20.md`, the 2026-05-19 phenomenology pre-brainstorm.
- **[B] partial/object-first:** `DECLARATION.md` (objecthood body + subordinate PAI annotation), `theorem_status.md`, `hypothesis_tree.md`, `CV-1.15_SEAL` (action=kinematic path-cost), sensing-pipeline cones, observer-moduli (agent policy π).
- **[C] legacy object-cohesion:** `canonical.md`, `CODE/scc/*` (grep: zero action/affordance/control), `transport.py`, `multi.py`, MF/.
- **[R] revise:** `CLAUDE.md` (session-start omitted the pivot), `THEORY_INDEX.md` (called PAI "main axis" while DECLARATION called it subordinate — contradiction).

Pattern: alignment concentrated in declaration/log/roadmap files (the talk), absent from canonical math + code (the work) — a reframing-in-name, not a reorganization-in-substance.

## C. Conceptual Fault Lines

- **C-1 [Critical] "Participation field" asserted but morphological.** `DECLARATION` defines u_t as 응집 참여 강도 (cohesive participation intensity) — but participation in a *morphological cohesion structure* (closure/sep/boundary/transport), not an *action structure*. The word "participation" was present without the actional content. The PAI target is participation in an *intervention-possibility* structure; the gap between the two is OP-PAI-002.
- **C-2 [Critical] Index/substance mismatch.** `THEORY_INDEX` said PAI = "main axis"; `DECLARATION` L172 + pivot §8 said subordinate "parallel layer." A reader could not tell what the project *is*.
- **C-3 [Major] "Action" overloaded.** CV-1.15's "Action-Based Temporal Succession" `a_i(x,y)=d²/Δt+γ‖Δφ‖²/Δt` is kinematic path-cost, not agentive action. Risk of double-counting 8 theorems as PAI progress.
- **C-4 [Major] Affordance treated as downstream.** MF synthesis: formations are "purely spatial-cohesive; no affordance." OP-PAI-006 framed affordance as *generated from* formations. The stronger (adopted) thesis inverts this: objecthood *is* stabilized affordance/intervention structure.
- **C-5 [Major] Action/control absent from code.** `CODE/scc/` had zero action structure; langevin = thermal landscape sampling, not intervention dynamics.
- **C-6 [Major] The gap is named but its two maps don't exist.** `Δ_interp(F):=d(𝓘_perception, 𝓘_action)` had all three components undefined. OP-PAI-001 cannot be stated rigorously until OP-PAI-002 yields a concrete 𝓘_action.

## D. Mathematical Compatibility

- u_t : X_t→[0,1] is **compatible as a carrier**, **insufficient as content**: its meaning is fixed by the morphological energy it minimizes.
- Cleanest path (minimal-structure, honoring the "projections" framing): **keep u_t and E as the morphology substrate; add one map 𝒜(u; Θ) and one invariance criterion; derive objecthood/affordance/control as projections.** No reopening of the 102 claims required — they become substrate lemmas.
- Required: an action-interpretation map 𝒜(u) (OP-PAI-002, class-agnostic but operational) + an invariance criterion (OP-PAI-003). Likely needed: embodiment parameter Θ. Resist for now: a 5th diagnostic, a standalone E_act term, impedance/compliance/recovery dynamics (these are *control-projection* concerns — name them, don't model them yet).

## E. Canonical Reframing (the adopted center)

> **SCC is a theory of actional perception: perception is the formation of a field of possible robot intervention. A scene is organized as graded participation u_t in an emerging intervention-possibility structure; objecthood, affordances, action units, trajectories, control modes, and recovery behaviors are not primitives but action-class-specific projections of that one field. The cohesion morphology SCC already formalizes (closure, separation, boundary, temporal transport) is the substrate the intervention field is carried on; an object is a region where intervention-possibility has stabilized into a reusable, interpretation-invariant unit — objecthood is stabilized affordance structure.**

Promote as the *stated destination* now; the 102 substrate claims stay sealed; the PAI projection maps stay OPEN. (The 2026-05-26 reorganization promotes this to DECL-2.0 as the ontological center per explicit user decision, while preserving these guardrails.)

## F. Controlled Vocabulary (see PAI_GLOSSARY)

perception = formation of graded participation u_t in an emerging intervention-possibility structure · object = region where intervention-possibility stabilized into a reusable action-invariant unit · affordance = the intervention-possibility content of the field (prior to objects, not appended) · action = any admissible robot intervention (not reducible to motor output) · participation field = participation in an intervention-possibility structure · {semantic, actional, control, temporal} projection = readouts of one field · 𝒜(u; Θ) = action-interpretation map · interpretation/translation gap = the double-interpretation defect SCC aims to dissolve.

## G. Structural Changes Recommended (executed via the 2026-05-26 reorg)

1. CANONICAL_AXIS.md (stated destination) + PAI_GLOSSARY.md.
2. Align the three entry points (THEORY_INDEX / DECLARATION / CLAUDE.md) to one substrate→destination story.
3. CHANGELOG entry marking the shift.
4. Annotate substrate as substrate; disambiguate CV-1.15 "action."
5. Reframe OP-PAI-006 (intervention-field → object+affordance joint projection).
6. New OPs: OP-ACTIONAL-U (make u_t a participation-in-intervention field via projection bundle), OP-PROJECTION (consistency of the projection bundle), OP-CONTROL-GROUNDING (𝒜 ↔ impedance/compliance/trajectory, parameter Θ).
7. Redraw the pipeline: `sensory difference → u_t intervention-possibility field → stable actional cohesion → {object, affordance, trajectory, control-mode, recovery} projections`.

## H. Final Judgment

The project SHOULD be reorganized around the perception-action interpretation gap. At audit time the reorganization was declarative, not structural; the correct next move was to make the axis load-bearing — define a concrete 𝒜(u; Θ), commit to one-field-many-projections as the canonical destination, align the contradictory entry points, and relabel the 102 claims honestly as substrate. This reorganization (2026-05-26) enacts the structural half; the formal 𝒜(u) remains open work on the PAI roadmap.

---

*PERCEPTION-ACTION AXIS AUDIT — preserved as rationale of record for the 2026-05-26 perception-action stack reorganization.*
