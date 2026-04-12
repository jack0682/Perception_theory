# C1 T-Persist-1(d) Exact Threshold Audit

**Date:** 2026-04-10
**Session:** Cycle 8 — T-Persist exact-threshold audit
**Category:** audit
**Status:** complete
**Depends on:** Canonical Spec v2.1.md §13; docs/04-02/proof/H3-TIGHTENING.md; docs/04-02/analysis/CONDITIONAL-CONDITIONS-ANALYSIS.md; docs/03-31/repair/PERSIST-SYNTHESIS.md

---

## 1. CURRENT GAP

**Canonical item:** C1 — T-Persist-1(d), exact threshold preservation.

**Current category:** Category C.

The exact-threshold claim is:

> core membership at threshold `theta_core` is preserved, not merely at a shifted threshold `theta_core - epsilon`.

---

## 2. Necessary Split

| Persistence statement | Status | Reason |
|---|---|---|
| shifted-threshold core inclusion | Category A / proved | follows from perturbation bound; allows margin loss |
| exact-threshold preservation on deep core | proved under positive interior gap | requires field values stay above `theta_core` after perturbation |
| exact-threshold preservation on all boundary core sites | not generally true | boundary is where field values approach threshold and identity is negotiated |
| exact-threshold preservation near bifurcation | false/unavailable uniformly | `mu -> 0` makes displacement bound blow up |

---

## 3. Dependency Formula

Exact threshold requires an interior margin:

```text
interior_gap(x) = u(x) - theta_core > perturbation_size.
```

Current proof gives a lower bound of the form

```text
u(x) - theta_core >= (1 - theta_core)
                      - 2 exp(-c0 delta(x))
                      - C_op R / beta.
```

Thus exact-threshold preservation is structurally tied to:

1. deep core depth `delta(x) >= 2`,
2. phase separation / large beta,
3. non-bifurcation Hessian gap `mu > 0`,
4. gentle transition size smaller than the interior margin.

---

## 4. Is `beta > 7 alpha` Removable?

**Decision:** no, not as an exact-threshold theorem.

The numerical constant may be tightened, but some phase-separation/interior-gap condition is non-removable. If beta is too weak, deep core may be absent or core values may sit arbitrarily close to threshold. Then arbitrarily small perturbations can cross the exact threshold.

Therefore:

- the number `7` is a proof/formation-conditioned safety constant;
- the existence of a positive lower-bound condition is structural;
- exact threshold cannot be made unconditional over all phase/near-bifurcation regimes.

---

## 5. Corrected Theorem Schema

The honest theorem is:

> For formation-structured minimizers with nonempty deep core, positive interior gap, nondegenerate Hessian gap, and transition displacement smaller than the interior margin, exact-threshold core preservation holds on the protected deep-core subset. Boundary core sites retain only shifted-threshold preservation.

Equivalently, T-Persist-1(d) should be read as a **deep-core exact-threshold theorem**, not a universal all-core theorem.

---

## 6. Decision for C1

| Claim | Decision |
|---|---|
| shifted threshold | proved / safe |
| exact threshold under `beta > 7 alpha` + deep-core/interior-gap hypotheses | conditionally proved |
| exact threshold without any phase-separation margin | false / structurally impossible |
| exact threshold near `mu -> 0` bifurcation | unavailable except shrinking-window/remnant forms |
| Category C status | keep |

---

## 7. Registry Delta

No Canonical Spec category change.

C1 remains Category C, but should be interpreted as:

> PROVED UNDER EXPLICIT CONDITIONS, with non-removable interior-gap / phase-separation hypothesis.

---

## 8. Next Trigger

Proceed to C2 — T-Persist-Full.

First move:

> Since T-Persist-Full chains through C1, update its status as a composition theorem whose only hard conditional component is exact-threshold preservation; separate full persistence from shifted/deep-core remnant persistence.
