# 09_sigma_multi_status.md — σ-Multi Status + OP-0009-Pre Compatibility

**Session:** 2026-05-06 (W6 Day 3 G3.9, optional).
**Goal:** σ-multi current state snapshot + compatibility check with G3.2 (unordered class formalism).

---

## §1. σ-Multi Current Status (W6 Day 3)

**Canonical claims (Cat A):**
- T-σ-multi-A-Static: static σ-signature of well-separated multi-formation ∈ anti-aligned set $\mathcal{A}$.
- T-σ-multi-D-Static: static σ-signature ∈ $\mathcal{D}$ (non-dominant neighbor condition).

Both added CV-1.5.1 (W5 Day 3 EOD). Status: Cat A conditional (under well-separated + $\sigma$-BC-1 condition).

**Working files (Cluster 2 staging):**
- `multi_formation_sigma.md` — D-6a primary (σ-multi static framework)
- `sigma_multi_trajectory.md` — dynamic trajectory under gradient flow (Cat C sketch)
- `sigma_rich_augmentation.md` — σ-rich + Φ-rich augmentation (OP-0005 Layer C path)

---

## §2. BC-1 Failure Finding (OP-0009-Emp)

From `single_high_F_equivalence.md` (W5 Day 4, OP-0009-Emp):

**BC-1 (boundary condition 1):** Requires the formation's cohesion field to be non-overlapping with neighboring formations in a well-defined sense.

**Finding:** BC-1 fails generically in the R23 dataset (overlapping regime is generic). Consequence: T-σ-multi-A-Static / T-σ-multi-D-Static Cat A conditional relies on BC-1. If BC-1 is not generically satisfied, the theorems' "production reach" is limited to the non-overlapping sub-regime.

**Severity assessment:** This is a *reach limitation* caveat, not a theorem falsification. The theorems are correct under their stated conditions; the issue is that the conditions are not met in the typical R23 configuration.

**Pattern match:** This is structurally identical to the T-L1-F/M production reach issue (G3.4): headline theorem is correct, but production-load-bearing reach is narrower than expected.

---

## §3. G3.2 Compatibility (from 02e §5.1)

From the Day 3 compatibility check (`02e_compatibility_check.md §5.1`):

**Result:** σ-framework is $S_K$-equivariant:
$$\sigma^A(\sigma \cdot \mathbf{u})_j = \sigma^A(\mathbf{u})_{\sigma^{-1}(j)}$$

**Class-level σ-signature:** $[\sigma^A([\mathbf{u}])]$ = unordered multiset of formation signatures. Well-defined at quotient level $\widetilde{\widetilde\Sigma}^K_M$.

**T-σ-multi-A/D-Static class compatibility:** Per-slot properties → $S_K$-invariant → class inherits. ✓ (sketch, W7 D4 formalization needed).

**New insight from G3.2:** At the class level, the σ-signature is an unordered multiset of formation-level signatures. The "which slot is which" labeling question is dissolved: the class $[\sigma^A]$ captures the *pattern* of formation signatures without labeling. This is the correct ontological level for T-σ-multi-A/D-Static.

---

## §4. OP-0009-Pre Compatibility Check (σ-specific)

**Question:** Does OP-0009-Pre resolution (K-field labels at modeling layer) change the statement of T-σ-multi-A/D-Static?

**Answer:** No change to theorem content. The theorems' content (per-slot σ-signature ∈ $\mathcal{A}$ or $\mathcal{D}$) is $S_K$-invariant (per-slot conditions applied to each $u^{(j)}$ independently). The modeling-layer lift provides ordered $j$-indices for computation, but the theorem's truth value is orbit-invariant.

**Class-level restatement:** For any representative $\mathbf{u}$ of class $[\mathbf{u}] \in \widetilde{\widetilde\Sigma}^K_M$ satisfying well-separated + BC-1:
$$[\sigma^A([\mathbf{u}])] \in \mathcal{A}_\mathrm{multi} \quad \text{(unordered multiset version of anti-aligned condition)}$$
This is the correct class-level version. The ordered version in canonical §13 is the coordinate-level statement.

---

## §5. Next Steps

1. **W7 D4** (G3.6 plan): Formalize $S_K$-equivariance of $\sigma^A$ in `02e` follow-up; check T-σ-Theorem-4 (continuum-vs-discrete caveat) at class level.
2. **W8 D2** (G3.6 plan): BC-1 failure analysis in context of class-level σ-signature. Determine if caveat needed on T-σ-multi-A/D-Static (analogous to T-σ-Theorem-4 pattern).
3. **W9 D3-D5**: σ-rich + Φ-rich augmentation (`sigma_rich_augmentation.md`) under P-F framework. This is a direct OP-0005 Layer C input.

---

**End of `09_sigma_multi_status.md`. σ-multi Cat A claims intact; BC-1 reach limitation flagged; G3.2 compatibility confirmed ✓. G3.9 complete.**
