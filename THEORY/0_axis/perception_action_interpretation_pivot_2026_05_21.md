---
id: PAI-PIVOT-2026-05-21
type: canonical/pivot
created: 2026-05-21
status: CANONICAL-DIRECTION / NOT YET FORMALIZED
parent_substrate: CV-1.20 SEALED (71A / 20B / 6C / 5R = 102 claims)
description: |
  SCC 의 main axis 를 *pre-objective cohesive formation* 에서
  *interpretation-preserving perception-action formation* 으로 pivot.
  기존 102 claims 는 substrate-canonical 로 보존 (변경 0).
  본 문서는 새 thesis, vocabulary, open problems 의 등록만.
  증명·수학적 형식화 0건.
constraint_compliance:
  canonical_theorem_changes: 0
  claim_count: 102 (unchanged)
  substrate_status: all preserved
  scc_edits: 0
  excessive_math: 0 (사용자 명시 제약 준수)
preceded_by:
  - THEORY/working/macro_audit_2026-05-20.md (§11 verdict + §8 macro gaps)
  - THEORY/logs/daily/2026-05-20/05_landscape_local_to_global.md (substrate honest limit)
  - User long-form reasoning (2026-05-20 evening, three messages on perception-action interpretation gap)
---

> [!nav] Parent: [[THEORY_INDEX]] · [[MOC_canonical_authority]] · Substrate: [[canonical]] (CV-1.20) · Pair: [[PAI_ROADMAP]] · Daily: [[../logs/daily/2026-05-21/00_pivot_entry|2026-05-21 pivot entry]]

# Perception-Action Interpretation Pivot (2026-05-21)

**Status**: CANONICAL-DIRECTION. Not yet formalized. No mathematical proof attempted. Substrate (102 SCC claims, CV-1.20) preserved without modification.

---

## §1 — Motivation

The previous main axis of SCC was *pre-objective cohesive formation*:

> "어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?"

This produced 71 Cat A + 20 Cat B + 6 Cat C + 5 Retracted = 102 claims about field-first boundary/formation emergence. These remain *substrate-canonical*.

But the 2026-05-20 macro audit (`THEORY/working/macro_audit_2026-05-20.md` §11) showed that SCC is *fragile* exactly where it tries to be a *complete* perception theory. The deeper motivation — the one that started the project — was not "explain object emergence." It was:

> The interpretation used for perception and the interpretation required for action should not diverge. The system should not need to translate the world twice.

The pattern the user dislikes in modern AI pipelines:

```
sensor → tokenization / feature / embedding → recognition → planning → action
```

In this pipeline, the unit produced by recognition (a "label," "embedding vector," "bounding box") is *not* the unit action operates on (a "grasp point," "collision body," "affordance"). The system silently translates between two different interpretations.

The reframe:

> **Perception must produce the same unit that action can act upon.**

SCC's value is not in being *a* perception theory. SCC's value is in supplying the *substrate layer* — the cohesion field morphology — on top of which a perception-action interpretation invariance can be sought.

---

## §2 — Core Thesis (CANONICAL-DIRECTION)

```
Perception = cohesive individuation + interpretation invariance across action
```

Stated equivalently:

> A formation F is a *perception-action formation* iff
>   (i) its substrate diagnostic d_SCC(F) = (Bind, Sep, Inside, Persist) is high (SCC criterion), AND
>   (ii) its perceptual individuation is invariant — or minimally distorted — under action interpretation.

**Status**: this thesis is *the new direction of canonical effort*. It is **not** a proved theorem. It is **not** a hypothesis with a fixed mathematical form yet. It is a research orientation.

The thesis is more demanding than the SCC criterion alone. Many formations may satisfy SCC's four diagnostics yet still fail action-invariance (e.g., a shadow, a reflection — high cohesion, low action-relevance).

---

## §3 — Status of the Old SCC Layer

The old SCC layer is **not discarded**. It is **substrate-canonical**.

| Old framing | New role |
|---|---|
| "SCC is a theory of pre-objective cohesion" | "SCC formalizes the cohesion / morphology substrate of perception-action formation" |
| "Objects emerge from energy minimization" | "Action-interpretable units emerge when cohesion AND PA-invariance both hold" |
| "DECLARATION Q1-Q6 = full perception theory" | "Q1-Q6 = substrate questions; PAI adds Q7 (interpretation invariance)" |
| "Bind/Sep/Inside/Persist = formation diagnostic" | "(Bind, Sep, Inside, Persist) = substrate diagnostic; possible 5th component pending (OP-PAI-004)" |
| "K-selection = perceived object number" | "K-selection = substrate K; perceived-K depends on action context (OP-PAI-005)" |

**No mathematical content of any canonical theorem is changed.** What changes is the *role* each theorem plays in the larger picture: from "main axis claim" to "substrate support."

Concrete preservation:
- All 71 Cat A theorem statements and proofs unchanged.
- All 20 Cat B theorem statements and conditional hypotheses unchanged.
- All 6 Cat C theorem statements and caveats unchanged.
- All 5 Retracted entries remain explicitly retracted.
- 8 retraction list (EW universality / Model A / t_× / D_f / H-int / closure RG / D_f=11/8 / k(k+1)/2-1) remains binding; PAI shall not silently revive them.

---

## §4 — New Canonical Vocabulary (all DEFINITION-DRAFT / OPEN)

The pivot introduces six terms. All six are **DEFINITION-DRAFT** — they are not yet formal mathematical objects. Each has at least one OPEN problem attached. No formula below is committed to be the final form.

### 4.1 Interpretation Gap

**Status**: DEFINITION-DRAFT.
**Draft**:
$$\Delta_{\text{interp}}(F) \;:=\; d\bigl(\mathcal{I}_{\text{perception}}(F),\; \mathcal{I}_{\text{action}}(F)\bigr)$$
where:
- $\mathcal{I}_{\text{perception}}(F)$ = perceptual individuation of formation $F$ (the unit picture from perception side)
- $\mathcal{I}_{\text{action}}(F)$ = action interpretation of formation $F$ (the unit picture from action side)
- $d$ = some structural discrepancy metric

**Three components are undefined**: $\mathcal{I}_{\text{perception}}$, $\mathcal{I}_{\text{action}}$, and $d$. Resolving them is exactly OP-PAI-001 and OP-PAI-002.

### 4.2 Interpretation-Preserving Formation (IPF)

**Status**: DEFINITION-DRAFT (depends on 4.1).
**Draft**: $F$ is an IPF iff $d_{\text{SCC}}(F)$ is high AND $\Delta_{\text{interp}}(F)$ is small.

### 4.3 Perception-Action Formation (PA-formation)

**Status**: DEFINITION-DRAFT.
**Draft**: a cohesive formation usable as an action unit without destructive re-tokenization, re-segmentation, or incompatible semantic remapping. Stronger than "object candidate."

### 4.4 Action Interpretation Invariance

**Status**: HYPOTHESIS / multiple candidate forms; no commitment yet.

Three candidate mathematical forms, none currently preferred:

- *Candidate form 1 — Equivariance*: $\mathcal{P}(g \cdot x) = g \cdot \mathcal{P}(x)$ for $g \in G_{\text{action}}$
- *Candidate form 2 — Commutativity*: $\mathcal{A} \circ \mathcal{P} = \mathcal{P} \circ \mathcal{A}'$ (some natural transformation form)
- *Candidate form 3 — Low-distortion*: $\Delta_{\text{interp}}(F) \leq \epsilon$ for some context-dependent $\epsilon$

Choosing among these = OP-PAI-003.

### 4.5 Shared Unit Principle

**Status**: CANONICAL-DIRECTION (thesis-level only; not a theorem).
**Statement**: the minimal unit of perception should coincide, as far as possible, with the minimal unit of action interpretation.

### 4.6 Meaningless Split / Non-semantic Fragmentation

**Status**: DEFINITION (negative target).
**Statement**: tokenization, encoding, embedding are not inherently wrong. They become wrong when they fragment perceptual structure into units that are *not constrained to preserve perception-action interpretation*. The problem is *unconstrained* fragmentation, not fragmentation itself.

---

## §5 — Open Problems Introduced (OP-PAI-001 ~ OP-PAI-006)

All six OPEN. No solution attempted. These are *registration entries*, not work products.

### OP-PAI-001 — Formal definition of interpretation gap

**Question**: what is the mathematical object measuring discrepancy between perceptual individuation and action interpretation?
**Candidate directions**: structural distance on partitions; Hausdorff distance between segmentation maps; mutual information loss; categorical natural transformation defect; affordance-preservation distortion.
**Status**: OPEN. Severity: High.

### OP-PAI-002 — Action interpretation map $\mathcal{A}(u)$

**Question**: how should $\mathcal{A}(u)$ — the action-level interpretation of a cohesion field or formation — be defined?
**Candidate directions** (action is plural; the choice of class matters):
- affordance map (Gibsonian)
- control constraint map (manipulation, robotics)
- reachable interaction region (navigation)
- manipulation primitive map (grasp, pour, etc.)
- navigation cost / action field (path planning)
- policy-conditioned semantic map (reinforcement learning)
- communication referential map (linguistic affordance)

**Critical constraint**: action is not reducible to motor output. It includes affordance, controllability, manipulability, navigability, collision relevance, task relevance, temporal intervention, and policy-conditioned meaning.

**Status**: OPEN. Severity: High.

### OP-PAI-003 — Interpretation invariance criterion

**Question**: which mathematical form expresses "perception unit = action unit"?
**Candidate forms** (see §4.4):
- equivariance under action group $G_{\text{action}}$
- commutative diagram between perception and action functors
- low-distortion $\Delta_{\text{interp}}(F) \leq \epsilon$
- preservation of formation equivalence class
- action-stable quotient

**Status**: OPEN. Severity: High.

### OP-PAI-004 — Diagnostic vector extension

**Question**: should the SCC vector $d = (\text{Bind, Sep, Inside, Persist})$ be extended with an action-readiness or invariance component?
**Candidate**:
$$d_{PA} \;=\; (\text{Bind, Sep, Inside, Persist, } \text{Act} \text{ or } \text{Inv}_{PA})$$
**Status**: OPEN. Severity: Medium. *Does not modify the existing 4-component diagnostic; this is a candidate extension.*

### OP-PAI-005 — Tokenization / embedding critique formalization

**Question**: how can the theory distinguish meaningful action-preserving decomposition from arbitrary computational tokenization?
**Constraint**: must not silently revive any of the 8 retractions. Must not claim a "dynamic class" without explicit evidence.
**Status**: OPEN. Severity: Medium.

### OP-PAI-006 — Formation-to-affordance bridge

**Question**: under what conditions does a cohesive formation generate affordances without a separate symbolic reinterpretation layer?
**Status**: OPEN. Severity: Medium. *Bridge to Gibsonian ecology / active inference is candidate, not committed.*

---

## §6 — Relation to macro_audit_2026-05-20

The pivot directly inherits the macro audit's structural diagnosis:

| macro_audit §8 macro gap | PAI mapping |
|---|---|
| Gap A — objecthood theorem not yet explicit | OP-PAI-001..003 collectively address the missing closure form |
| Gap B — observer/readout layer under-axiomatized | OP-PAI-002 specifies action interpretation; observer layer is one source of action context |
| Gap C — K-selection not closed | OP-PAI-005 + OP-PAI-002 — perceived K depends on action context; substrate K (current SCC Cat B) is preserved |
| Gap D — merge/split identity not solved | OP-PAI-001 + OP-PAI-006 — identity through topology change depends on which action-invariant is preserved |
| Gap E — conditionality ledger scattered | This pivot document, together with PAI_ROADMAP.md, serves as the first explicit ledger |

The pivot does **not** solve any of these gaps. It reframes them so that the next work has a coherent target.

The macro audit's §9 hard-stop rules continue to apply, with one addition:

> Before adding new proof work, ask: which OP-PAI-001..006 does it advance? If none, and it is not maintenance, pause it.

---

## §7 — Non-Overclaim (mandatory)

The following statements are **not** made by this pivot:

1. PAI solves the perception problem. It does not. It only reframes the next research target.
2. SCC + PAI = a complete theory of perception. It is not. It is a substrate + a new direction.
3. The vocabulary in §4 is mathematically settled. It is not. Six DEFINITION-DRAFTs awaiting OP-PAI resolution.
4. Action = motor output. It does not. Action means: affordance, controllability, manipulability, navigability, collision-relevance, task-relevance, temporal intervention, policy-conditioned meaning.
5. Perception = recognition / labeling. It does not. Perception means: formation of an action-addressable interpretation unit.
6. Tokenization is inherently wrong. It is not. *Unconstrained* fragmentation (without PA-invariance) is the problem.
7. The 8 retractions are reactivated. They are not. They remain explicitly retracted; PAI shall not revive them by analogy.
8. CV version is incremented. It is not. Pivot is *parallel* to the SCC claim ladder, not an addition to it. CV-1.20 remains current.

---

## §8 — What This Pivot Does Not Do

- Does not modify any of the 71 Cat A or 20 Cat B canonical theorem statements.
- Does not change claim count (102 unchanged).
- Does not advance the CV version (CV-1.20 unchanged; pivot is a parallel layer).
- Does not propose a fifth energy term (no $E_{\text{act}}$ commitment; only candidate among others — see §9).
- Does not formalize $\mathcal{A}(u)$, $\Delta_{\text{interp}}$, or the invariance criterion. These are OPEN.
- Does not design experiments. Experimental design is Phase 6 of `PAI_ROADMAP.md` (W9+).
- Does not delete, demote, or relocate any prior SCC working file.
- Does not change `DECLARATION.md` body (only an annotation pointer is added).
- Does not modify `MAIN_PROMPT_v3.md` body (only a legacy-framing header annotation).

---

## §9 — Recorded Mathematical Directions (not solutions)

For completeness, three structural directions exist in the literature that *might* eventually formalize §4. None is committed.

- *Commutative-diagram form*: a category-theoretic structure where perception and action are functors and the pivot asks them to commute on formation objects.
- *Low-distortion metric form*: $\Delta_{\text{interp}}(F)$ as a measurable structural distance to be minimized.
- *Constraint-vs-energy form*: action interpretation may enter as an additional *energy term* $E_{\text{act}}$, or as a *constraint* $\Delta_{\text{interp}}(F) \leq \epsilon$. Constraint form may be cleaner; both are candidates.

These three are recorded for OP-PAI-003 reference. *Choosing among them is part of OP-PAI-003*, not part of this pivot.

---

## §10 — Reading Order for Future Agents

1. `THEORY/working/macro_audit_2026-05-20.md` — first.
2. This document — second.
3. `THEORY/canonical/PAI_ROADMAP.md` — third (W9+ planning context).
4. `THEORY/logs/daily/2026-05-21/00_pivot_entry.md` — fourth (the day the pivot was made).
5. `THEORY/logs/daily/MAIN_PROMPT_v4_PAI_PIVOT.md` — fifth (agent instructions).
6. `THEORY/canonical/DECLARATION.md` (DECL-1.0) — substrate thesis, unchanged.
7. `THEORY/canonical/canonical.md` — substrate body, unchanged.
8. `THEORY/canonical/CV-1.20_SEAL.md` — most recent substrate seal.

---

## §11 — Final Status

```
This document:                 CANONICAL-DIRECTION / NOT YET FORMALIZED
Substrate (CV-1.20):           Preserved unchanged (102 claims, 71A/20B/6C/5R)
New thesis:                    "Perception must produce the same unit action can act upon"
New vocabulary:                6 items, all DEFINITION-DRAFT
New open problems:             OP-PAI-001..006, all OPEN
CV version:                    CV-1.20 (unchanged)
Hypothesis tree version:       HT-3.12 (adds H-PAI branch; existing branches unchanged)
Mathematical proofs:           0
Experimental commitments:      0
Excessive math discipline:     enforced
```

The pivot is registered. The next session begins from PAI_ROADMAP Phase 1 or stays with substrate maintenance, depending on user direction.

---

*PAI Pivot 2026-05-21. SCC's mathematical contribution is preserved. The original motivation — interpretation should not split between perception and action — is restored as the main axis. No proof attempted. No fancy math.*
