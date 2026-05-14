> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 08_op_0005_k_selection_layer_status.md — OP-0005 K-Selection Layer Status

**Session:** 2026-05-06 (W6 Day 3 G3.8, P1).
**Source:** `theorem_status.md` OP-0005 entry + working file audit (G3.7).
**Goal:** 4-layer progress % + integration plan + next canonical promotion path.

---

## §1. OP-0005 Overview

**OP-0005:** K-Selection Mechanism — what determines the stable value of $K_\mathrm{act}$ under SCC gradient flow.

**Current canonical status:** Cat C (working files only; no canonical theorem for K-selection mechanism). OP-0005 is HIGH priority per theorem_status.md.

**Architecture:** 3 substantive layers (A, B, C) + compatibility verification.

---

## §2. Layer Progress Table

| Layer | Name | Approach | Working file | Progress | W9 target |
|---|---|---|---|---|---|
| **A** | Free energy landscape | $F(K) = -T_* \log Z_K$; equilibrium $K$ minimizes $F(K)$ | `k_selection_a_free_energy.md` | ~30% (sketch; energy landscape geometry unclear) | Cat B with P-F-A3 |
| **B** | Kramers escape rates | Eyring-Kramers $k_{K \to K-1}$ from energy barriers on $\Sigma_M$ | `k_selection_b_kramers.md` | ~60% (barrier formula done; $T_*$ now defined via OP-0014) | Cat B with OP-0014 |
| **C** | Numerical anchor | $K_\mathrm{act}$ distribution from exp sweeps; barrier height $O(\beta^{0.89})$ | `k_selection_c_numerical_anchor.md` | ~40% (empirical data exists; P-F calibration missing) | Cat C extended |
| **Compat** | Compatibility proof | K-selection consistent with T-Persist-K, T-Merge, N-1 asymmetry | `k_selection_compatibility_proof.md` | ~50% (N-1 recovered via P-F-A6 ✓; T-Merge connection partial) | Cat B |

**Overall OP-0005 progress:** ~45% (pre-P-F-A advancement).

---

## §3. Day 3 Advance: Layer B + P-F Integration

**The key Day 3 result** (from G3.3 `03b_op_0005_layer_b_kramers_pf_dependence.md`):
With OP-0014 (P-F framework) providing $T_*$, Layer B becomes substantive:
$$k_{K \to K-1} = \frac{|\lambda_-|}{2\pi}\sqrt{\frac{\det H_{\hat{\mathbf{u}}_K}}{|\det' H_{\mathbf{u}_\mathrm{saddle}}|}}\cdot\exp\!\left(-\frac{\Delta E^{(K \to K-1)}}{T_*}\right)$$

**Before Day 3:** Layer B formula correct but physically vacuous ($T_*$ undefined).
**After Day 3:** Layer B formula has well-defined $T_*$ via P-F-A1; N-1 asymmetry recovered via P-F-A6; detailed balance gives equilibrium $K$ distribution from Layer A.

**Post-Day 3 progress estimate:** Layer B → ~70%; Layer A → ~40% (Layer A free energy now connected to P-F-A3 Boltzmann distribution).

---

## §4. Remaining Gaps Per Layer

### Layer A gaps
1. **Saddle point existence** on $\Sigma_M$ between K-formation and (K-1)-formation basins (OP-0014 open problem §4.1).
2. **Free energy computation:** $Z_K(\mathcal{P}) = \int_{\mathcal{B}_K} \exp(-\mathcal{E}/T_*) D\tilde{u}$ — basin integral not yet computable analytically (needs Laplace approximation + Hessian at minimizer).
3. **Finite $K$ comparison:** Does $F(K) < F(K-1)$ for the production-load-bearing parameter regime?

### Layer B gaps
1. **Saddle existence** (same as Layer A gap 1 — shared blocker).
2. **Hessian non-degeneracy** at saddle: one negative eigenvalue assumed but not verified empirically on $\Sigma_M$.
3. **Multiple saddles** (§4.3 of `03b`): which saddle dominates? Exponential factor vs prefactor competition.
4. **Born-Oppenheimer condition:** $\tau_\mathrm{fast} \ll \tau_\mathrm{MFPT}$ for K-jump master equation validity.

### Layer C gaps
1. **$T_*$ calibration:** $\sigma$ in exp sweeps → $T_*$ in P-F-A7 ($T_* \approx \sigma^2/(2\eta)$) — needs numerical verification.
2. **Barrier height $O(\beta^{0.89})$:** currently informal (deterministic curvature statement). Under P-F: restate as "barrier height relative to $T_*$ scales as $O(\beta^{0.89}/T_*)$" → rate exponent.

### Compatibility gaps
1. T-Merge(b) (merger under gradient flow) ↔ Layer B merger rate: deterministic merger = $T_* \to 0$ limit of Kramers rate. Formal connection not written.
2. N-1 Soft-Hard Asymmetry ↔ P-F-A6: recovered at $T_* \to 0$ ✓ (done in `03b`). Formal proof in P-F framework: W9 D2.

---

## §5. Integration Plan

**OP-0005 requires OP-0014 (P-F) before substantive progress.** This is the key W9 dependency:

```
W9 D1: OP-0014 P-F axiom set v1 (P-F-A1..A8 formal)
W9 D2: Layer B Kramers under P-F-A4/A5 formalized; saddle existence gap addressed
W9 D3: Layer C T_* calibration from exp sweep data
W9 D4: Layer A free energy $Z_K$ Laplace approximation
W9 D5: Compatibility proof completion (T-Merge ↔ Layer B; N-1 ↔ P-F-A6 formal)
W9 D6: OP-0005 Cat B target: write canonical promotion proposal
```

**Expected canonical outcome (W9 D6):** T-K-Select (Cat B, conditional on P-F-A1-A6 + saddle existence) — K-selection via Kramers mechanism under P-F dynamics. Conditional on OP-0014.

**CV-1.7 target:** T-K-Select Cat B promotional (W10 D1-D2 supervised).

---

## §6. Blocking Dependencies

| Layer | Blocker | Resolution |
|---|---|---|
| A + B | Saddle existence on $\Sigma_M$ | OP-0014 W9 D2 (attempt) or NQ-ST-1 (empirical Hessian verification) |
| A | $Z_K$ basin integral | Laplace approximation W9 D4 |
| B | Hessian non-degeneracy | NQ-ST-1 W7/W8 |
| C | $T_*$ calibration | OP-0014 P-F-A7 W9 D1 |
| All | $T_*$ undefined | **OP-0014** — RESOLVED at W9 D1 (P-F axiom set v1) |

**Critical insight:** OP-0014 (P-F) is the only blocking dependency for making substantive forward progress on all 3 OP-0005 layers simultaneously. This justifies the Day 3 escalation of OP-0014 to HIGH.

---

**End of `08_op_0005_k_selection_layer_status.md`. 4-layer status: A~40%, B~70%, C~40%, Compat~55% (post-Day 3 estimates). Integration plan: OP-0014 W9 D1 → all layers unblock → T-K-Select Cat B candidate W9 D6. G3.8 complete.**
