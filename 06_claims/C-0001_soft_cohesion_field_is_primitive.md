---
id: C-0001
type: claim
category: conceptual
status: validated
confidence: 100%
date_proposed: 2026-03-26
evidence: [A-0001, Canonical Spec §2–3]
depends_on: [Q-0001]
---

# Claim: C-0001 — Soft Cohesion Field is Primitive

## Statement

The soft cohesion field u_t : X_t → [0,1] is the ontological primitive of the theory. Objects are derivative — they are distinguished regions where u is high, stable, and temporally persistent.

---

## Rationale

**Avoids circular presupposition:** Starting from objects presupposes that individuation is already complete. The theory needs to account for how individuation emerges, not assume it.

**Captures pre-objective states:** Graded fields can represent partially-formed, ambiguous, or transitional coherence states that discrete objects cannot express.

**Empirical adequacy:** Soft fields naturally match neural population codes, visual saliency maps, and other biological instantiations.

---

## Evidence

- **Theoretical:** A-0001 (axiom of ontological primitivity); full formalization in Canonical Spec §3
- **Conceptual:** §2 Foundational Orientation provides philosophical justification
- **Computational:** scc/graph.py, scc/operators.py implement u_t as central data structure

---

## Assumptions

1. Relational support space X_t is well-defined (sites can be identified even if objects cannot)
2. Graded membership (degree ∈ [0,1]) is meaningful for cohesion
3. Temporal evolution u_t → u_{t+1} can be formally specified

---

## Limitations

- Does not address where X_t itself comes from (that is a separate modeling choice)
- Requires formal specification of operators (closure, distinction, aggregation) to be non-vacuous
- Does not automatically resolve what threshold makes a "crisp object" — that remains a downstream question

---

## Related Claims

- C-0002: Objects are distinguished formations (not primitives)
- C-0003: Formations are defined by proto-cohesion (Bind ∧ Sep ∧ Artic ∧ Persist)

---

## Validation Status

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Axiomatically formalized | ✅ | A-0001 |
| Operationally specified | ✅ | scc/ implementation |
| Empirically applied | ✅ | exp1–exp65 (all use u_t) |
| Theoretically fertile | ✅ | 27 Category A theorems derived |
| No contradiction found | ✅ | v1.2 audit complete |

---

## Confidence Assessment

**Current confidence:** 100% (foundational axiom, validated by entire theory)

**Factors increasing confidence:**
- Used consistently across all theorems
- No counterexamples
- Explains pre-objective phenomena
- Enables graded representations

**Factors decreasing confidence:**
- (None known)

---

## Next Steps

This claim requires no further validation. It is canonical.

---

**Last Updated:** 2026-04-12
**Status:** Canonical (v1.2 §3)
