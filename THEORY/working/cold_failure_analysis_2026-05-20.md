---
type: working/failure-analysis
created: 2026-05-20
status: working
canonical_effect: none
baseline: CV-1.20 / HT-3.11
description: Cold root-cause analysis of suspected structural problems in SCC theory.
---

> [!nav] Parent: [[macro_audit_2026-05-20]] · Evidence: [[DECLARATION]] · [[theorem_status]] · [[hypothesis_tree]] · [[README]]

# SCC Cold Failure Analysis — 2026-05-20

## 0. Verdict

The theory is not "false" in the simple sense. The stronger diagnosis is:

> SCC has a real local mathematical core, but its macro claim is currently under-specified. The theory has proved many mechanisms around field formation, boundary emergence, count diagnostics, stochastic foundations, and stable temporal correspondence, but it has not yet proved one integrated objecthood theorem. The gap is not one lemma; it is a missing interface between local field theorems and the global claim "this is when an object exists."

This is painful because the core is not empty. The problem is subtler: the theory may be locally true but globally overinterpreted.

---

## 1. Symptom

The felt symptom:

> Proofs are chasing hypotheses, hypotheses are chasing proof gaps, and the theory's original center is harder to see.

Concrete signs:

- The declaration asks one question: "어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?" (`DECLARATION.md` lines 20-26).
- The same declaration jumps from T8 boundary emergence to "객체성이 발생한다" (`DECLARATION.md` lines 69-83).
- Yet the active status table still marks Q4 as Cat B and Q6 as ongoing (`DECLARATION.md` lines 91-98).
- The README explicitly says objecthood is an interpretation of stabilized field patterns, not a primitive (`README.md` lines 14-32).
- The README also preserves non-claims: model slots are not true object count, active channels do not always equal topological components, field-capacity selection is not solved, and merge/split inheritance is not solved (`README.md` lines 142-153).

So the central tension is already visible in the repository:

> The motivating prose says the theory answers objecthood. The non-claim ledger admits that several ingredients of objecthood are not yet solved.

---

## 2. Root Cause

### Root Cause 1 — "Objecthood" is doing too much work

The word objecthood currently compresses at least six distinct properties:

1. non-trivial field formation;
2. boundary emergence;
3. separation from background;
4. count/readout stability;
5. temporal persistence;
6. identity through split/merge.

The theory has strong evidence for 1-3, significant progress for stable 5, partial machinery for 4, and weak/open status for 6.

Therefore the sentence

> boundary emerges, therefore objecthood emerges

is too strong unless "objecthood" is explicitly weakened to "object candidate" or "proto-object formation."

Minimal repair:

> Replace the macro target with a tiered theorem: proto-formation -> object candidate -> stable object reading -> identity-bearing object. Do not let T8 alone carry all four tiers.

### Root Cause 2 — K-selection is not a side problem; it is part of objecthood

If the theory cannot explain why a scene stabilizes as one object, two objects, or no object, then it has not fully answered objecthood.

Evidence:

- OP-0005 says the theory provides no complete mechanism for how K is determined (`theorem_status.md` lines 784-794).
- OP-0005-DYN remains OPEN; EQ and OBS are only partially resolved Cat B (`theorem_status.md` lines 798-806).
- The README explicitly says field-capacity selection is not solved (`README.md` lines 144-151).

This means count is not merely an extension. It is central. The theory can often say:

> under a resolved regime, this is how to read a count.

It cannot yet fully say:

> this is why that count is selected dynamically.

Minimal repair:

> Treat Q4 as macro-blocking for any full objecthood claim. Allow Q1 to prove proto-object formation only.

### Root Cause 3 — Merge/split identity is exactly where the theory is weakest

Object identity is easy in stable continuation. It is hard at topology change.

Evidence:

- T-σ-Inherit has Cat B pieces for centroid/orientation, but sigma-standard under MERGE/SPLIT is Cat C (`theorem_status.md` lines 184-207).
- OP-0008 states post-merger sigma is not deterministic from pre-merger sigma alone and requires extra merger geometry (`theorem_status.md` lines 680-696).
- OP-0008-MERGE/SPLIT remain partially structured / structured with Cat C Wigner-projection blockers (`theorem_status.md` lines 700-707).

This matters because "same object through change" is not a decorative extension. It is one of the intuitive meanings of objecthood.

Minimal repair:

> State explicitly: SCC currently has stable-regime temporal correspondence, not a complete identity theory through merge/split.

### Root Cause 4 — The observer/readout layer is under-derived

The declaration says object count, boundary, and identity are observation-condition dependent (`DECLARATION.md` lines 102-113). That is likely correct. But the observer-dependent part currently relies heavily on registered/axiomatic structure.

Evidence:

- OP-0021 says $T_*$ remains OPEN with scope revision (`theorem_status.md` lines 910-915).
- Routes A/B were deprecated because they require external environmental statistics and violate CN-COB (`theorem_status.md` lines 916-920).
- Route C is accepted as an observer-personal parameter, but fixed-point existence and multiplicity remain open (`theorem_status.md` lines 922-932).

This creates a real weakness:

> The theory says perception is condition-dependent, but the formal observer condition package is not fully derived.

Minimal repair:

> Separate "observer-conditioned interpretation" from "derived observer model." The first is canonical thesis; the second is not yet complete.

### Root Cause 5 — Conditional results are accumulating faster than the assumption ledger

The theory is careful in many local places, but the conditions are scattered.

Evidence:

- Count bridge is explicitly not global and only valid in a resolved regime (`README.md` lines 76-96).
- Action temporal cost closes one layer but explicitly does not close OP-0012 overall, Sinkhorn plan semigroup, OP-0008, OP-0005-DYN, or OP-0021 (`theorem_status.md` lines 406-414).
- H-MORSE local work leaves OP-HMORSE-LOCAL-A, saddle regularity, SBM robustness, and OP-0005-DYN open (`theorem_status.md` lines 420-435).
- The macro audit identifies Cat B chain inflation as a danger: "Cat B theorem + plausible condition + numerical anchor + narrative necessity = macro conclusion" (`macro_audit_2026-05-20.md` lines 270-276).

Minimal repair:

> Every major narrative sentence needs a minimal-assumption row. If the row contains Cat B/C conditions, the sentence cannot be stated as a global theorem.

---

## 3. The Most Serious Possible Failure Mode

The most serious failure is not that SCC has no mathematics.

The most serious failure is:

> SCC may only prove a theory of proto-cohesive field morphology, while its prose sometimes speaks as if it has proved a theory of objecthood.

That would still be a valuable theory, but it is a smaller theory.

If this diagnosis is right, the correct move is not to abandon SCC. It is to demote the macro claim:

| Current risky claim | Safer claim |
|---|---|
| SCC explains when an object exists | SCC explains when a proto-objective cohesive formation becomes available for object reading |
| T8 gives objecthood | T8 gives non-uniform boundary/formation emergence |
| K is object count | K is a regime-dependent readout, with selection still open |
| Temporal identity is solved | Stable-regime correspondence is solved; merge/split identity is open |
| Observer dependence is formalized | Observer dependence is registered; derivation of observer parameters is incomplete |

---

## 4. Rival Hypotheses

### Rival A — SCC is basically right, but overclaims its integration

This is the most charitable diagnosis.

Local theorems are meaningful. The fix is a macro ledger and a tiered objecthood theorem.

Prediction:

> After careful tiering, most current work survives, but many statements move from "object" to "proto-object candidate."

### Rival B — SCC is mostly a morphology theory, not an objecthood theory

Here the field machinery is valid, but the leap to cognition/perception/objecthood is not mathematically forced.

Prediction:

> The strongest publishable core becomes "variational topology of pre-objective cohesion fields," while objecthood remains an interpretation layer.

### Rival C — SCC's objecthood target requires external observer/semantic structure

If objecthood cannot be derived from field geometry alone, then SCC must import an observer/readout/semantic layer. That would weaken the original "field-first" purity.

Prediction:

> Any complete object theorem will require non-field primitives: task, sensor, policy, action, or semantic equivalence.

This is the dangerous rival because it directly challenges the founding ambition.

---

## 5. Cold Triage

### Keep

- Field-first primitive $u_t$.
- T8 as boundary / non-uniform formation mechanism.
- Count-language separation.
- Resolved-regime count bridge.
- Package I stochastic foundation.
- Stable-regime temporal identity.
- Non-claim / retraction discipline.

### Demote

- "Objecthood emerges" -> "proto-object candidate emerges" unless Q4/Q5/Q6/readout assumptions are present.
- "K is count" -> "K is a family of readouts; equality is regime-conditioned."
- "$T_*$ is derived" -> "$T_*$ is observer-personal registered; derivation remains open."
- "Identity survives events" -> "stable correspondence survives; merge/split identity is open."

### Stop

- Adding H-MORSE / spectral lemmas unless they explicitly close Package II, K-selection, or objecthood tiering.
- Promoting Cat B chains as if they were macro conclusions.
- Using numerical anchors to carry conceptual load.
- Treating "not false" as "macro solved."

---

## 6. Minimal Recovery Plan

1. Write a tiered objecthood theorem draft:
   - Tier 0: field formation;
   - Tier 1: boundary-bearing proto-object candidate;
   - Tier 2: count-stable object reading;
   - Tier 3: temporally stable object;
   - Tier 4: identity-bearing object through topology change.

2. For each tier, list:
   - theorem support;
   - conditions;
   - open blockers;
   - non-claims.

3. Freeze new proof work unless it moves a tier upward.

4. Decide whether the full target is:
   - a pure field theory of proto-object formation; or
   - a field-plus-observer theory of perceived objecthood.

This decision is not cosmetic. It determines whether SCC's current gaps are normal open problems or signs that the original target was too broad.

---

## 7. One-Line Diagnosis

SCC's local mathematics is substantial, but the theory's current problem is a category mismatch: it has mostly proved field-formation and regime-conditioned readout machinery, while the motivating claim still wants a full objecthood theorem.

