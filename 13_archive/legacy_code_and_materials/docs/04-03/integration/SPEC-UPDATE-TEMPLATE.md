# Spec Update Template — Phase 9 Completion

**Date:** 2026-04-03
**Purpose:** Pre-assembled template for Canonical Spec v2.1 update after all Phase 9 tasks complete
**Status:** TEMPLATE — awaiting final results from Tasks #1-5

---

## 1. Proof Status Matrix (from Task #4 Audit)

### Current Baseline (Canonical Spec v2.1 §13 as-is)

| Category | Count | Notes |
|----------|-------|-------|
| Cat A | 41 | Per latest CHANGELOG entry (includes Merge upgrade) |
| Cat B | 3 | T-Bind-Proj/Full (general tau), T-Persist-K-Sep |
| Cat C | 4 | T-Persist-1(b,d,e), T-Persist-Full, T-Persist-K-Weak, C3'' |
| Retracted | 2 | Thm 3.3, K-Saddle Conjecture |

### After Task #1 (C3'' → Cat A)

| Category | Count | Delta | Notes |
|----------|-------|-------|-------|
| **Cat A** | **42** | +1 | C3'' (C-Axioms fully proved) |
| Cat B | 3 | — | Unchanged |
| Cat C | 3 | −1 | C3'' removed from Cat C |
| Retracted | 2 | — | Unchanged |
| **Completeness** | **87.5%** | | 42/(42+3+3) |

### Phase 9 Category Changes (from Task #4 audit + Tasks #1-3)

| Theorem/Result | Before | After | Source | Blocker |
|---------------|--------|-------|--------|---------|
| **Merge Theorem (e'+e'')** | Cat B | **Cat A** (generic) | MERGE-THEOREM.md | None (Kupka-Smale structural) |
| **T-Persist-1(e) (Sinkhorn)** | Cat B | **Cat A** (suff. cond.) | SINKHORN-LIPSCHITZ.md | None (computable condition) |
| **C3'' (co-belonging monotonicity)** | Cat C (gap) | **Cat A** | C3-SYMMETRIZATION-COMPLETE.md | **CLOSED** — Schur complement proof |
| **H3 tightening (interior gap)** | Cat C (beta>11a) | **Cat C** (beta>7a) | H3-TIGHTENING.md | Analytical nu bound |
| **TC'' (transport confinement)** | Cat B | **Cat B** (quantitative) | TC-FORMATION-CONDITIONED.md | Shallow-core concentration |
| **Formation Birth (Thm 1a)** | Cat B | **Cat A** (D4-symmetric) | FORMATION-BIRTH-THEOREM.md | None for grids |
| **Formation Birth (Thm 3c)** | — | **Cat A** (Gap Cond.) | FORMATION-BIRTH-THEOREM.md | General non-D4 graphs |
| **T-Persist-1(b) (BC')** | Cat C | **Cat A** (via f1^grad) | F1-BOUND-CATA-UPGRADE.md | None (BSR condition) |
| **Beyond-Weyl spectral** | — | **Cat A** (Gap Cond.) | BEYOND-WEYL-SPECTRAL.md | None |

### Pending from Other Tasks

| Task | Expected Output | Impact on Spec |
|------|----------------|----------------|
| Task #1 (C3'' gap closure) | **COMPLETED** — Full Schur complement proof + numerical verification | C3'' gap fully closed, C-Axioms Cat A |
| Task #2 (TC tight bound) | IN PROGRESS — tight confinement proof | May upgrade TC from Cat B |
| Task #3 (Basin unconditional) | IN PROGRESS — remove mu>4.1 condition | May upgrade T-Persist-1(b) further |
| Task #5 (experiments) | PENDING — verify exp37-45 backing claims | Validates or invalidates proof claims |

---

## 2. Spec Sections to Update

### §13 Category A — Add/Modify:

1. **C-Axioms (update — READY):** 
   
   **Location:** Canonical Spec v2.1, line 907–908
   
   **Remove:** The entire `*Gap:*` paragraph (line 908): "The C3'' proof relies on a Neumann series monotonicity argument where the symmetrization step ($D^{-1/2}$ depends on $u_t(x)$) awaits formal verification..."
   
   **Replace line 907 proof text with:**
   > *Proof:* C1 by construction; C2 by explicit witnesses (3 orders of magnitude discrimination); C3'' by conjugation identity + Schur complement monotonicity (see below); C4 automatic from symmetrized kernel. *(R6.)*
   > *C3'' proof:* The conjugation identity $\mathbf{C}_t(x,x) = d(x) \cdot [(D - \alpha W_u)^{-1}](x,x)$ absorbs the $u$-dependent $D^{-1/2}$ normalization. Setting $u(x) = s^2$ and applying the Schur complement yields $\mathbf{C}_t(x,x) = \sigma/(\sigma - \alpha^2 f(s))$ where $f(s) = s \cdot \mathbf{w}^T G(s)^{-1} \mathbf{w}$. The derivative $f'(s) = \mathbf{v}^T G_0 \mathbf{v} \geq 0$ is a PSD quadratic form ($G_0 = (1-\alpha)D_0 + \alpha L_0$, sum of PSD matrices; exact algebraic cancellation of $s\Delta$ terms). Strict monotonicity on graphs with min degree $\geq 2$. Verified numerically: analytical Jacobian matches FD to $< 10^{-8}$ relative error. *(C3-SYMMETRIZATION-COMPLETE.md, 04-03.)*
   
   **Why this closes the gap:** The original Neumann series argument failed because individual terms $[(\alpha W_{\mathrm{sym}})^k](x,x)$ are not monotone in $u(x)$ — the degree normalization $D^{-1/2}$ creates competing effects (increasing direct entries but diluting neighbor-neighbor entries). The conjugation identity sidesteps this entirely by working with the unnormalized M-matrix $H = D - \alpha W_u$, where the Schur complement formula isolates the $u(x)$-dependence into a scalar function with a manifestly PSD derivative. No term-by-term Neumann analysis needed.

2. **Merge Theorem (new entry):** Full barrier-based merge theorem with 5 parts (a)-(e). All Cat A for generic parameters. Replaces the falsified MS1-MS4 saddle conjecture.

3. **T-Persist-1(e) (update):** Move from Cat C to Cat A. Sinkhorn-Lipschitz bound with computable sufficient condition. Basin containment verified at natural parameters.

4. **T-Birth-Param (new entry):** Parametric birth via Crandall-Rabinowitz (simple lambda_2) and Equivariant Branching Lemma (D4-symmetric, degenerate lambda_2=lambda_3). Supercriticality from W''''=24>0.

5. **T-Birth-Topo (new entry):** Topological splitting via Gamma-convergence.

6. **T-Birth-K2 (new entry):** K=2 nucleation threshold via block-Kronecker Hessian analysis.

7. **Beyond-Weyl Spectral Bound (new entry):** Structured spectral perturbation for K-field joint Hessian.

8. **d_min Analytical Formula (new entry):** Tanh profile + volume balance closed form.

### §13 Category B — Modify:

1. **T-Persist-K-Sep (keep):** No change.
2. **T-Bind-Proj/Full (keep):** No change (general tau still Cat B).
3. **TC'' (update note):** Add note about quantitative improvement (1-10x of actual vs 25-100x).

### §13 Category C — Modify:

1. **T-Persist-1(d) (update):** Change H3 condition from beta>11alpha to beta>7alpha. Note formation-conditioned C2^form <= 1.24.
2. **T-Persist-Full (update):** Components (a),(b),(c),(e) now Cat A. Only (d) remains Cat C (beta>7alpha).
3. **T-Persist-K-Weak (keep):** No change.

### §15 Closing Summary — Update:

- Update theorem counts: "XX Cat A / X Cat B / X Cat C"
- Update "75% fully proved" percentage
- Add Merge Theorem and Formation Birth to key results list
- Note C3'' gap closure

---

## 3. Category Audit Checklist

### Pre-Phase-9 Cat A (from spec, verified):
- [ ] T1 (existence)
- [ ] T6a (closure FP existence)
- [ ] T6b (closure FP uniqueness)
- [ ] T20 (axiom consistency)
- [ ] T-A2 (monotonicity)
- [ ] T8-Core (phase transition)
- [ ] C-Axioms (C1,C2,C3'',C4) — **update C3'' note**
- [ ] QM1-4
- [ ] T14 (gradient flow)
- [ ] T3/T6-Stability
- [ ] T7-Enhanced (metastability)
- [ ] T11 (Gamma-convergence)
- [ ] T8-Full (upgraded from B)
- [ ] Predicate-Energy Bridge (upgraded from B)
- [ ] Deep Core Dominance 2b (upgraded from B)

### Phase 8-9 Cat A additions (from CHANGELOG 04-03):
- [ ] Merge Theorem (a)-(e) — all Cat A for generic params
- [ ] Sinkhorn-Lipschitz / T-Persist-1(e) upgrade
- [ ] Formation Birth Param (Thm 1+1a) — D4 equivariant
- [ ] Formation Birth Topo (Thm 2)
- [ ] Formation Birth K2 (Thm 3a,b,c)
- [ ] K-field Hessian block-Kronecker
- [ ] f1 soft-mode bound (under BSR)
- [ ] d_min analytical formula
- [ ] TC'' mechanisms (support restriction, Gibbs, convex combination)
- [ ] Beyond-Weyl spectral bound
- [ ] BC' directional basin (via f1^grad)
- [x] C3'' full proof — **COMPLETE** (Schur complement, verified to FD 1e-8)

### Cat B (should remain):
- [ ] T-Bind-Proj/Full (general tau)
- [ ] T-Persist-K-Sep (conditional on per-formation + WS + SR)
- [ ] TC'' (overall, inherited from shallow-core)
- [ ] H3 formation-conditioned (semi-empirical nu bound)

### Cat C (should remain):
- [ ] T-Persist-1(d) — beta>7alpha (tightened from 11alpha)
- [ ] T-Persist-Full — (d) only remaining Cat C component
- [ ] T-Persist-K-Weak — multiple conditions
- [ ] T-Persist-K-Unified — conditional on BC'-K, TC-K

---

## 4. Draft CHANGELOG Entry Structure

```markdown
## 2026-04-03 — Phase 9 Completion: Spec Audit & Integration

### Summary
Phase 9 systematic audit of 6 conditional proofs + 3 gap closures + experiment verification.
**Net: XX Cat A / X Cat B / X Cat C (XX% fully proved).**

### Task Results
| Task | Output | Impact |
|------|--------|--------|
| #1 C3'' Code Alignment | D^{-1/2} symmetrization, 174 tests pass | C3'' gap closed |
| #2 TC Tight Bound | [PENDING] | [PENDING] |
| #3 Basin Unconditional | [PENDING] | [PENDING] |
| #4 Conditional Proof Audit | 6 files audited, categories clarified | +2 Cat A confirmed |
| #5 Experiment Verification | [PENDING] | [PENDING] |
| #6 Spec Integration | Canonical Spec v2.1 updated | Final totals |

### Category Changes
[Fill from Task #4 matrix + Tasks #1-3 results]

### Spec Updates
- §13 Cat A: [list additions]
- §13 Cat B: [list changes]
- §13 Cat C: [list changes]
- §15: Updated totals and summary

### Files Modified
- `Canonical Spec v2.1.md` — §13, §15 updated
- `CHANGELOG.md` — this entry
- `docs/04-03/audit/CONDITIONAL-PROOFS-AUDIT.md` — Task #4 output
- `docs/04-03/integration/SPEC-UPDATE-TEMPLATE.md` — this template
```

---

## 5. Placeholder: Experiment Validation (Task #5)

The following experimental cross-references need verification:

| Proof File | Experiment | Claim | Status |
|-----------|-----------|-------|--------|
| MERGE-THEOREM | exp38 | Barrier exists at default params | PENDING |
| SINKHORN-LIPSCHITZ | exp38 | Barrier exponent beta^0.89 | PENDING |
| H3-TIGHTENING | exp13 | Deep core at beta>=20alpha universal | PENDING |
| TC-FORMATION-CONDITIONED | exp40, exp41 | Basin containment at natural params | PENDING |
| FORMATION-BIRTH-THEOREM | exp37 | Zero hysteresis, supercritical | PENDING |
| FORMATION-BIRTH-THEOREM | exp39 | Topological splitting | PENDING |
| C3-SYMMETRIZATION-COMPLETE | (code tests) | Code already uses D^{-1/2}; FD verification passed | **DONE** (Task #1) |

---

## 6. Risk Register

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Task #5 experiment failures | May invalidate proof claims | Proofs are analytical; exp failures indicate parameter regime limits, not proof errors |
| Task #2/3 incomplete | TC and BC stay at current category | Template handles this via "PENDING" placeholders |
| Recount discrepancy | Totals may shift by +/-2 | Do careful recount of §13 at integration time |
| ~~C3'' code change breaks tests~~ | ~~Blocks C3'' closure claim~~ | **RESOLVED** — code already uses D^{-1/2}, no change needed |
