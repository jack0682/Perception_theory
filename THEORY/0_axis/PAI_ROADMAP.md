---
id: PAI-ROADMAP
type: canonical/roadmap
created: 2026-05-21
status: CANONICAL-DIRECTION (roadmap; phases are research targets, not commitments)
parent: [[perception_action_interpretation_pivot_2026_05_21]]
substrate: CV-1.20 SEALED (unchanged)
description: |
  Roadmap for the 2026-05-21 PAI pivot. Phases 0-6.
  No phase below claims a proof. Phases are *research targets*, ordered by dependency.
  Each phase may take many sessions; some may fail; some may need to be re-scoped.
---

> [!nav] Parent: [[perception_action_interpretation_pivot_2026_05_21]] · [[THEORY_INDEX]] · Substrate: [[canonical]]

# PAI Roadmap (2026-05-21)

**Discipline**: no phase below produces a canonical Cat A/B claim until the relevant OP-PAI is resolved. Phases are sequenced by *dependency*, not by *expected delivery date*.

---

## Phase 0 — Preserve and Audit the Substrate

**Goal**: ensure SCC's 102 claims remain navigable as substrate-canonical without erosion.

**Tasks**:
- Keep `THEORY/2_substrate/canonical/canonical.md` §13 untouched.
- Maintain claim count 102 across all MOCs.
- Pause new SCC SEALs unless they advance a specific PAI OP.
- macro_audit §9 hard-stop gates apply to all candidate new proof work.

**Exit condition**: substrate state remains consistent through W9+; new SCC SEAL frequency drops sharply (no proof-count pressure).

**Status (2026-05-21)**: active.

---

## Phase 1 — Define the Interpretation Gap

**Goal**: produce one (or more) candidate formal definition of $\Delta_{\text{interp}}$.

**OP advanced**: OP-PAI-001.

**Tasks**:
- Survey 3-5 candidate forms for $d(\mathcal{I}_{\text{perception}}, \mathcal{I}_{\text{action}})$.
- For each candidate, identify *which prior work* it most resembles (categorical, metric, information-theoretic, geometric).
- For each candidate, identify *which OP-PAI-002 action class* it pairs naturally with.
- Pick at most one candidate to develop further; mark others as parked alternatives.

**Output**: working file in `THEORY/working/PAI/` (subdirectory to be created) with status DEFINITION-DRAFT.

**Technical substrate (pre-formal, 2026-05-23)**: `THEORY/working/prolegomena/` 의 3 문서가 Phase 1 의 *기술 substrate* 로 등록됨 — `00_field_conditions_v0.md` (perception-side 44 조건) + `01_mathematical_conditions_v0.md` (math-side 평행) + `02_framework_skeleton_v0.md` (4-layer architecture; OP-NEW-C 가 *PAI 핵심 entry point* 로 식별됨, *interpretation invariance* 의 native model 부재가 5 영역 광범위 리서치의 수렴 결과). Phase 1 의 candidate form survey 시 이 substrate 참조.

**Anti-targets**: proving that the chosen form is "the right one." Selection is not justification.

---

## Phase 2 — Define the Action Interpretation Map $\mathcal{A}(u)$

**Goal**: produce a candidate $\mathcal{A}$ for *one specific action class*.

**OP advanced**: OP-PAI-002.

**Tasks**:
- Commit to one action class first (e.g., manipulation, or navigation, or attention). User-driven choice.
- Define $\mathcal{A}(u)$ for that class as a candidate; do not claim generality.
- Verify $\mathcal{A}$ is well-defined on at least a small graph example.
- Mark all other action classes as separate future work.

**Anti-targets**:
- A "universal" $\mathcal{A}$ covering all actions at once. Action is plural; one class at a time.
- Reducing $\mathcal{A}$ to motor output. Action includes affordance, controllability, navigability, task relevance, communication, intervention.

**Status**: blocked on Phase 1 (need $\Delta_{\text{interp}}$ to give $\mathcal{A}$ a target structure).

---

## Phase 3 — Choose an Invariance Criterion

**Goal**: pick one of the three candidate forms in §4.4 of the pivot document and develop it.

**OP advanced**: OP-PAI-003.

**Three candidate forms**:
- equivariance under $G_{\text{action}}$
- commutativity of $\mathcal{A} \circ \mathcal{P} = \mathcal{P} \circ \mathcal{A}'$
- low-distortion $\Delta_{\text{interp}}(F) \leq \epsilon$

**Tasks**:
- Argue *for one* form on the basis of compatibility with Phase 1 + Phase 2 outputs.
- State its limits (where it fails, what it does not cover).
- Mark unchosen forms as parked.

**Status**: blocked on Phases 1 + 2.

---

## Phase 4 — Diagnostic Vector Extension

**Goal**: decide whether SCC's $d = (\text{Bind, Sep, Inside, Persist})$ needs a fifth component for action-readiness.

**OP advanced**: OP-PAI-004.

**Tasks**:
- Check the mapping (Bind ↔ graspability, Sep ↔ separability, Inside ↔ enterability, Persist ↔ trackability). Is it tight or loose?
- If loose, propose a candidate fifth: $\text{Act}(F)$ or $\text{Inv}_{PA}(F)$.
- Do *not* modify existing 4 components or their definitions.

**Anti-targets**: redefining Bind/Sep/Inside/Persist. The substrate diagnostic is unchanged.

**Status**: blocked on Phases 1-3.

---

## Phase 5 — Connect to Concrete Actions

**Goal**: relate the formalized PAI machinery (Phases 1-4 outputs) to at least one concrete action *family*.

**OP advanced**: OP-PAI-006, OP-PAI-005.

**Tasks**:
- Pick one concrete action: grasp, avoid, inspect, follow, repair, navigate, or communicate.
- Show what unit a PA-formation produces, *if* the pipeline closes.
- Compare against what current AI pipelines (tokenization + post-processing) produce.

**Anti-targets**:
- Claiming this is "the perception theory of grasping" (or any specific action). The result is a *candidate*, one of many.
- Reviving any of the 8 retractions (EW, Model A, dynamic class, $t_\times$, $D_f^{(k)}$, H-int, closure RG, $D_f = 11/8$, $k(k+1)/2-1$).

**Status**: blocked on Phases 1-4.

---

## Phase 6 — Toy Experiments

**Goal**: design and run a *small* numerical or thought experiment that *could* falsify the chosen PAI form.

**OP advanced**: OP-PAI-006 (validation).

**Candidate experiments** (not commitments):
- A small graph + two action interpretations (e.g., grasp-partition vs collision-partition). Compute SCC formations. Measure invariance.
- Compare token/embedding segmentation against SCC formation under action consistency.
- Test whether $d_{\text{SCC}}$ predicts action-readiness for a simple grasp metric.

**Anti-targets**:
- Claiming an experiment "validates the theory" if it just succeeds at a narrow benchmark.
- Inferring general perception claims from a single graph or single action class.

**Status**: blocked on Phases 1-5 *if a chosen invariance form exists*. Could run independently as a probe experiment.

---

## Cross-Phase Discipline (mandatory)

1. **Substrate preservation**: at every phase, the 102 SCC claims must remain unchanged. Phase work happens in `THEORY/working/PAI/`, not in `canonical/`.
2. **No version inflation**: CV-1.20 stays. CV-1.21+ should only happen on a genuine substrate addition (a new Cat A/B canonical lemma about SCC), not on PAI progress alone.
3. **OP-PAI status updates**: when a phase produces a candidate, the matching OP-PAI moves from `OPEN` to `OPEN-with-candidate-N`. It does *not* move to `RESOLVED` without explicit review.
4. **Action class commitment**: every PAI working file must state which OP-PAI-002 action class it is working in (manipulation / navigation / attention / etc.). Universal claims are off-limits.
5. **8 retractions**: re-check at every phase that PAI work does not silently revive any retracted claim.
6. **macro_audit §9 hard stop gates**: apply to every proposed new proof.

---

## Stopping Conditions

The roadmap may stop or be re-planned at any of the following points:

- Phase 1 fails to produce a usable $\Delta_{\text{interp}}$ candidate after reasonable effort. Action: re-think whether PAI is the right framing.
- Phase 2 reveals that $\mathcal{A}$ cannot be defined intrinsically (requires external observer/oracle). Action: accept that PAI requires an *agent* parameter and adjust framing.
- Phase 3 shows all three invariance forms are equivalent in practice. Action: collapse, simplify.
- Phase 5 connection produces no genuine difference from tokenization+postprocessing baselines. Action: re-examine the original motivation.
- Any phase reactivates a retracted claim. Action: pause; audit.

---

## Reading Order for This Roadmap

1. `THEORY/0_axis/perception_action_interpretation_pivot_2026_05_21.md` (pivot doc, §1-§11)
2. This file
3. macro_audit_2026-05-20 §8 macro gaps and §9 hard stops
4. The specific OP-PAI body the next session targets

---

*PAI Roadmap is a plan, not a commitment. Phases may shift. Substrate remains.*
