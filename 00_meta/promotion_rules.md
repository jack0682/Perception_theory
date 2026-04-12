---
id: META-0005
type: meta/promotion_rules
status: accepted
last_updated: 2026-04-12
---

# Promotion Rules: From Draft to Canonical

## Overview

This document defines the formal criteria for promoting documents through the Research OS status hierarchy, particularly the critical transition: **claim → canonical**.

A claim (C-xxxx) becomes part of the formal Canonical Spec only when it satisfies ALL criteria in the checklist below. This prevents ad-hoc theory inflation and maintains canonical rigor.

---

## Promotion Criteria by Document Type

### C-xxxx (Claim) → Canonical Spec

**Definition:** A claim achieves canonical status when it becomes a formal theorem in Canonical Spec vX.Y.

#### Prerequisites (Must Be True)

1. **Proof Exists & Accepted**
   - [ ] P-xxxx folder exists for this claim
   - [ ] proof_attempt_v_final (or later) completes all steps
   - [ ] Proof status = `accepted` (not just `tentative`)
   - [ ] Formal verification by Critic Agent done (line-by-line check)
   - [ ] No outstanding gaps (all lemmas proved or cited)

2. **Experimental Validation**
   - [ ] At least 3 independent experiments (E-xxxx) run
   - [ ] All experiments consistent with claim (no counterexamples)
   - [ ] No contradiction with existing R-xxxx results
   - [ ] Sanity checks passed (no absurd values, sensible units)
   - [ ] Experiment agents sign off on repeatability

3. **No Blocking Criticisms**
   - [ ] Critic Agent has reviewed (formal critique round)
   - [ ] No "challenged" status currently active
   - [ ] If challenges existed, they have been refuted with evidence
   - [ ] All assumptions documented in A-xxxx registry
   - [ ] No hidden dependencies

4. **Spec Integration**
   - [ ] Notation consistent with symbol_registry.md (S-xxxx)
   - [ ] Terminology consistent with concept_registry.md (D-xxxx)
   - [ ] Category assigned (A: fully proved, B: conditional, C: very conditional)
   - [ ] Assumption list explicit (A-xxxx IDs listed in claim header)
   - [ ] Relationship to existing theorems clear (supersedes/depends on)

5. **Documentation Complete**
   - [ ] C-xxxx overview written (statement + intuition)
   - [ ] P-xxxx proof properly formatted (theorem statement + proof body)
   - [ ] E-xxxx results exist (all runs documented)
   - [ ] R-xxxx interpretation written (what this means, implications)
   - [ ] CHANGELOG entry prepared (what's new in this version)

6. **Category Determination**
   - [ ] **Category A (unconditional):** Proved, no special assumptions beyond foundational axioms
   - [ ] **Category B (conditional):** Proved under stated conditions (e.g., "for generic parameters")
   - [ ] **Category C (very conditional):** Proved only under restrictive regime (e.g., "well-separated K-field formation")
   - [ ] **Retracted:** Counterexample found; no longer claimed

#### Decision Process

1. **Author/Proof Agent:** Submit C-xxxx + P-xxxx as `tentative`
2. **Experiment Agent:** Run E-xxxx suite; provide R-xxxx report
3. **Critic Agent:** Formal review; publish critique or approval
4. **Lead:** Decide category (A/B/C) and integration point in Canonical Spec
5. **Lead:** Update Canonical Spec vX.Y; add to theorem registry; mark C-xxxx as `accepted`

#### Checklist Template

```markdown
## Promotion Checklist for C-xxxx

### Proof (P-xxxx)
- [ ] P-xxxx folder exists
- [ ] All proof steps complete
- [ ] Critic Agent verification: ___________

### Experiments (E-xxxx)
- [ ] E-0001 results: _____ (description)
- [ ] E-0002 results: _____ (description)
- [ ] E-0003 results: _____ (description)
- [ ] No counterexamples found: [ ]

### Assumptions (A-xxxx)
- [ ] A-0001: ___________
- [ ] A-0002: ___________
- [ ] All dependencies documented: [ ]

### Specification
- [ ] Notation consistent: [ ]
- [ ] Category assigned: [ ] A [ ] B [ ] C
- [ ] Intended Canonical Spec version: v1._

### Decision
- [ ] Lead approval: _____________ (signature)
- [ ] Promoted to: [ ] accepted
- [ ] Canonical integration date: __________
```

---

### P-xxxx (Proof) → Accepted Status

**Definition:** A proof is accepted when it is mathematically rigorous and error-free (to human verification standard).

#### Criteria

1. **Completeness**
   - [ ] All major steps present (no "obviously true" gaps)
   - [ ] All lemmas either proved or cited with reference
   - [ ] QED or explicit conclusion statement
   - [ ] No TBD markers

2. **Correctness (Formal)**
   - [ ] No circular reasoning
   - [ ] All quantifiers explicit (∀/∃)
   - [ ] All sets well-defined
   - [ ] No undefined symbols (all in S-xxxx registry)

3. **Correctness (Semantic)**
   - [ ] Critic Agent has independently verified
   - [ ] Line-by-line check documented
   - [ ] Any ambiguities resolved in writing

4. **Clarity**
   - [ ] Reader can follow without external references (or references clearly cited)
   - [ ] Intuition provided (not just symbolic manipulation)
   - [ ] Failed proof attempts documented (why they didn't work)

#### Decision Process

1. **Author:** Submit proof_attempt_final (or Vn)
2. **Critic Agent:** Review + publish formal verification report
3. **Lead:** Approve or request revisions
4. **Mark as:** `accepted` (with Critic signature in YAML header)

---

### E-xxxx (Experiment) → Validated Status

**Definition:** An experiment is validated when results are reproducible and consistent with theoretical claims.

#### Criteria

1. **Design Specification**
   - [ ] spec.md written (hypothesis, method, expected result)
   - [ ] Parameters and grid details explicit
   - [ ] Sanity checks defined (what would mean "result is clearly wrong")

2. **Execution**
   - [ ] Multiple runs (≥3 independent runs with same config)
   - [ ] Results consistent across runs
   - [ ] Random seeds documented
   - [ ] Code reproducible (script in scc/ or experiments/)

3. **Sanity Checks**
   - [ ] No NaN, inf, or absurd values
   - [ ] Units consistent (energy ∈ reasonable range, etc.)
   - [ ] Scaling behavior sensible (doubling grid → expected change)
   - [ ] Edge cases handled (tiny λ, huge λ, boundary cases)

4. **Documentation**
   - [ ] Results logged (run_001/, run_002/, etc.)
   - [ ] Summary.md written (aggregate findings)
   - [ ] Figures/plots generated if relevant
   - [ ] Error bars or confidence intervals estimated

#### Decision Process

1. **Experiment Agent:** Run E-xxxx; document all runs
2. **Experiment Agent:** Publish summary.md
3. **Lead/Critic:** Review for sanity + reproducibility
4. **Mark as:** `validated` (with Experiment Agent signature in YAML header)

---

### D-xxxx (Definition/Concept) → Registry Acceptance

**Definition:** A concept is registered when it is semantically clear and integrated with related concepts.

#### Criteria

1. **Semantic Clarity**
   - [ ] Definition is unambiguous (not circular)
   - [ ] Scope is explicit (when does this concept apply?)
   - [ ] Relationship to similar concepts documented (how different from X, Y?)

2. **Consistency**
   - [ ] No notation collision (S-xxxx check)
   - [ ] Consistent with axioms (A-xxxx)
   - [ ] Consistent with other D-xxxx definitions

3. **Usage Documentation**
   - [ ] At least one claim (C-xxxx) uses this concept
   - [ ] At least one experiment (E-xxxx) operationalizes this
   - [ ] Usage examples provided

#### Decision Process

1. **Author:** Write D-xxxx definition
2. **Lead:** Add to concept_registry.md
3. **Mark as:** `accepted` (in registry)

---

## Canonical Spec Update Process

When a claim is promoted to canonical, the following steps occur:

1. **Version Bump**
   - If Category A claim: v1.Y → v1.Y+1 (minor version)
   - If Category B claim: v1.Y → v1.Y+1 (minor version, with disclaimer)
   - If Category C claim: reference version stays same, new result goes to "Conditional Theorems" section

2. **Spec Integration**
   - Add theorem statement to appropriate section (§1–§13 per Canonical Spec structure)
   - Add proof sketch or "See P-xxxx for full proof"
   - Update theorem index
   - Add to theorem_registry.md with new T-xxxx ID

3. **Release Note**
   - Write brief summary of new theorem
   - List key references (P-xxxx, E-xxxx, R-xxxx)
   - Document any new assumptions (A-xxxx)

4. **CHANGELOG**
   - Entry: "Promoted C-xxxx to canonical, new Theorem T-xxxx in v1.Y"
   - Author credit
   - Date

### Example: C-0001 → T-Persist-1(b) (04-03)

```markdown
# Canonical Spec v1.1 Release Notes (2026-04-03)

## New Theorems

### T-Persist-1(b): Basin Containment (Unconditional)

**Status:** Category A → A (upgraded from B)

**Source:** 
- Claim: C-0001 (in 06_claims/C-0001_t_persist_1b.md)
- Proof: P-0001/proof_attempt_v3.md
- Experiments: E-0008, E-0009, E-0010

**New Assumption Resolved:**
- Generic transversality (GT) and non-degeneracy (NB) are now shown to hold generically
- Removed "Category B" condition; now unconditional

**Statement:**
For any SCC field u_t on relational space X, with transport kernel M_{t→s},
the basin of attraction for the empirical transport-based persistence contains
all initial configurations within ε of the true core.

(See Canonical Spec v1.1 §7.1 for full statement and proof sketch.)
```

---

## Rejection & Returning to Active

If a claim fails promotion:

1. **Reason documented** in critique/rejection memo
2. **Assigned category:** `challenged` (+ severity code if applicable)
3. **Returned to author:** back to `active` status
4. **Revision plan:** Author proposes next steps (more experiments? Different proof strategy?)
5. **Retry:** When ready, resubmit (same C-xxxx ID, proof attempt Vn+1)

No claim is permanently rejected unless Lead explicitly marks it `archived` (terminal).

---

## Timeline & SLAs

**Typical promotion timeline:**

- **Draft → Active:** 1–3 days
- **Active → Tentative:** 3–7 days (when author confident)
- **Tentative → Validated:** 7–14 days (experiment + critique rounds)
- **Validated → Accepted:** 1–3 days (Lead decision)
- **Accepted → Canonical:** 0–1 days (automatic upon acceptance)

**SLAs:**
- Critic Agent must review within 3 days of tentative submission
- Experiment Agent must complete runs within 5 days of tentative submission
- Lead must decide within 2 days of all reviews in

---

## Special Cases

### Claims with Pre-Existing Proofs (04-03 PLAN_0403)

Some claims already have proofs from earlier iterations (e.g., C3'', T-Persist-1(b)).

**Shortcut promotion:**

1. **Collect existing proof** (e.g., from docs/04-03/proof/)
2. **Format as P-xxxx** (update notation, add YAML header)
3. **Critic Agent:** Verify existing proof still valid
4. **Submit as tentative** (same process, but proof is pre-validated)

### Retracted Claims

If a claim is refuted by counterexample (X-xxxx), mark it as `archived` and update Canonical Spec:

- **Before:** "Theorem T-N: [statement]" (§X.Y)
- **After:** "(Retracted 2026-04-12) Theorem T-N was refuted by counterexample X-0001"

Link to the counterexample for transparency.

---

## Checklist Summary (One-Pager)

```markdown
# Quick Promotion Checklist

## C-xxxx → Canonical

- [ ] P-xxxx exists and is `accepted`
- [ ] E-xxxx ≥3 runs, all consistent
- [ ] No X-xxxx counterexamples
- [ ] Critic Agent approval obtained
- [ ] A-xxxx all listed & defined
- [ ] Notation (S-xxxx) consistent
- [ ] Category (A/B/C) assigned
- [ ] CHANGELOG entry ready
- [ ] Lead approval obtained

**→ Mark as `accepted` and integrate into Canonical Spec v1.Y**
```

---

**Last updated:** 2026-04-12  
**Maintained by:** Lead + Research OS Architect  
**See also:** status_codes.md, theorem_registry.md
