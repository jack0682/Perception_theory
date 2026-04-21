# 11 — Round 8 Apply Errata + E-14 (T-7 in C+E Conflation)

**Session:** 2026-04-21 (Round 8, post critical self-review)
**Mode:** **Apply errata** (concrete file fixes) + **critique of critique** (1 more errata found in Round 7's analysis itself).
**Format:** ~150 줄.

---

## §1. Errata Applied This Round

### E-10 Applied — Filippov caveat to F3.1

**File:** `working/C/F_group_axioms.md` Theorem F3.1.

**Change:** statement now explicit Filippov / mollified; proof breaks into:
- Lipschitz on `Σ_m^ε \ V`. ✓
- V-discontinuity acknowledged.
- Mollification repair (smooth ℱ_ε := ℱ * ρ_ε) + Lions-Sznitman, then ε → 0 limit.
- Filippov alternative (V Lebesgue null, hit with P=0).
- Status downgrade: "Cat A" → "Cat A modulo Filippov repair".

**Impact:** F3 well-posedness is now **rigorously stated**. Original statement was technically incorrect; corrected version is mathematically precise.

### E-11 Applied — (φ-sat) commit explicit

**Files:** `working/CE/free_energy_wellposed.md` §4.3 + `working/E/soft_K_definition.md` §1.

**Change:** γ_K ∈ [0.01, 0.1] now annotated as "(φ-sat) specific". (φ-lin) generalization noted as having different (more permissive) γ_K range.

**Impact:** distinguishes between commit-level scope (φ-sat) and framework-level scope (φ admits multiple choices). Removes implicit assumption.

### E-12, E-13 NOT applied this round

- E-12 (τ_mix factor 2 conservatism): primarily affects daily file `08_round5_compact.md` §3. Daily files are historical record; correction noted in `10_critical_self_review.md` §3 suffices. Future merge of canonical can incorporate.
- E-13 (T*_uniform sep-sign): formula in daily file `07_round4_verification.md` §1.3. Holds at canonical default params; caveat already noted in self-review §4.3. Could promote to a `working/CE/T_uniform_stab.md` if user wants — left as task for next session.

---

## §2. E-14 (NEW) — T-7 in C+E Conflation

### 2.1 The conflation discovered (critique of critique)

Round 3 §2 named Proposition 2.1 "T-7 in C+E, strengthened". Re-examining post Round 7:

**T-7 (canonical Cat A):** "At a closure FP, the closure Hessian `2(I - J_Cl)^T(I - J_Cl)` is strictly positive definite." This is a statement about **closure FPs specifically** (where Cl(u) = u, residual r = 0).

**Round 3 §2 Prop 2.1:** "At K_soft ≈ K local minimizers of ℱ_C+E, the Hessian eigenvalue is `≥` ℰ Hessian eigenvalue + entropy positive contribution - small λ_K negative." This is a statement about **ℱ_C+E critical points**.

**Conflation:** ℱ_C+E critical points are **NOT** closure FPs in general. KKT for ℱ_C+E:

$$
\nabla\mathcal{E}(u^*) - T\,\nabla S(u^*) + \lambda_K\,\nabla K_{\mathrm{soft}}(u^*) - \mu\,\mathbf{1} \;=\; 0,
$$

implies ∇ℰ(u^*) = T∇S - λ_K∇K_soft + μ·1, which is **NOT zero** in general.

Closure residual at u^*:
$$
r(u^*) \;=\; u^* - \mathrm{Cl}(u^*) \;=\; \nabla\mathcal{E}_{cl}/(2) \cdot (I - J_{Cl})^{-T} \;\neq\; 0
$$

(some nonzero combination of T, λ_K corrections).

Hence **T-7's "closure Hessian at FP" formula doesn't directly apply at ℱ_C+E critical points**.

### 2.2 What's actually correct

What IS true: at ℱ_C+E critical points, the Hessian has the form:
$$
H_{C+E}(u^*) = \nabla^2\mathcal{E}(u^*) + T\nabla^2(-S)(u^*) + \lambda_K\nabla^2 K_{\mathrm{soft}}(u^*).
$$

The first term ∇²ℰ(u^*) is **NOT** the same as canonical T-7's `2(I-J_Cl)^T(I-J_Cl)` because u^* is not a closure FP. ∇²ℰ(u^*) includes **higher-order** corrections proportional to r(u^*) (the residual).

For small T and small λ_K (perturbation regime), u^* is close to ℰ minimizer (which IS close to closure FP), and the corrections are small. Round 3 §2 Prop 2.1 is **approximately correct in this perturbation regime** but **NOT a direct extension of T-7** to C+E.

### 2.3 Honest restatement

**Prop 2.1 (corrected, Round 8 per E-14):** At ℱ_C+E critical points u^* close (in IFT-perturbation sense) to canonical ℰ critical points, the constrained Hessian satisfies:

$$
\mu_{\min}(H_{C+E}(u^*)) \;\geq\; \mu_{\min}(H_\mathcal{E}(u^*)) + T\cdot \mu_{-S}^{\min}(u^*) - \lambda_K\cdot \|\nabla^2 K_{\mathrm{soft}}\|_{op},
$$

where `μ_{min}(H_ℰ(u^*))` is the constrained ℰ Hessian eigenvalue **at u^*** (NOT at the canonical ℰ minimizer; the two differ by IFT-displacement of order T + λ_K).

**This is a Hessian-decomposition statement, NOT "T-7 strengthened".** T-7 itself (closure positive Hessian at closure FP) is **unchanged**, but applies to closure FPs which are generically NOT ℱ_C+E critical points.

### 2.4 What this affects

| Round 3-7 claim | Affected by E-14? |
|---|---|
| Round 3 §1.7 "T-7 survives strengthened" | **YES** — should be "Prop 2.1 (Hessian decomp at C+E critical point)", not "T-7 strengthened" |
| Round 3 §2 Prop 2.1 statement | **YES** — needs IFT-perturbation caveat |
| Round 4 T-Uniform-Stab-T (Hessian at uniform) | **NO** — uniform IS a closure FP at u = c·1 (when c is closure FP scalar; per canonical definition c* = solution of σ(a_cl(c-τ)) = c) |
| Round 5 Witten Laplacian | **NO** — independent |
| F3 / F4 commitments | **NO** |
| F-1 / M-1 / MO-1 dissolutions | **NO** — they don't directly use T-7 |

So E-14 affects **Round 3 §2 statement only**. Repair: rename Prop 2.1 from "T-7 in C+E strengthened" to "Hessian decomposition at C+E critical points (perturbation regime)".

### 2.5 New errata E-14 status

- **Severity:** Low (affects naming + framing of one Round 3 result; does not invalidate the math).
- **Fix:** Rename + IFT-perturbation caveat.
- **Applied?** Not yet — daily file `06_further_verification.md` §2 is historical record. Can note in `99_summary.md`.

---

## §3. Critique of Critique Saturation Check

Round 7 critique found 4 errata (E-10~E-13). Round 8 critique-of-critique found 1 errata (E-14).

| Round mode | New positives | New negatives (errata) |
|---|---|---|
| Verification (Rounds 2-6) | 19 Cat A | 9 errata |
| Critique (Round 7) | 0 | +4 errata |
| Critique-of-critique (Round 8) | 0 | +1 errata |

Each meta-level adds errata at decreasing rate (Round 7 = 4 errata, Round 8 = 1 errata). Round 9 (critique³) expected ≤ 1 errata at most.

**Recursive critique reaches saturation by Round 8-9.** Each layer of meta-analysis exposes finer issues, but the rate of discovery diminishes as obvious issues are caught at lower rounds.

---

## §4. Final Status (Truly)

Cumulative errata: **14** (E-1 through E-14).

| Errata | Severity | Status |
|---|---|---|
| E-1, E-2, E-3 (L_K factor 2 → 4) | Low | Applied (Round 2 → working files) |
| E-4 (entropy η-parameterization) | Low | Pending user review |
| E-5 (T-Beyond-Weyl, T-d_min retire) | Medium | Pending |
| E-6 (Cat A 22 update) | Low | Pending |
| E-7 (γ_K range tighten) | Medium | Applied (Round 3 → working files) |
| E-8 (F3 Cat A on Σ_m^ε) | Medium | Applied (Round 3 → working files) |
| E-9 (linear-interp ℰ_bd) | Low | Applied (Round 4 → daily file note) |
| E-10 (F3 Filippov caveat) | Medium-High | **Applied Round 8 → working/C** |
| E-11 ((φ-sat) commit explicit) | Medium | **Applied Round 8 → working/CE, working/E** |
| E-12 (τ_mix factor 2 conservatism) | Medium | Note in `10_critical_self_review.md` §3 |
| E-13 (T*_uniform sep-sign) | Low | Note in `10_critical_self_review.md` §4 |
| E-14 (T-7 conflation) | Low | Note here in `11_round8` §2 |

**Applied: 8 (E-1, E-2, E-3, E-7, E-8, E-9, E-10, E-11). Notes-in-daily-files: 3 (E-12, E-13, E-14). Pending user review: 3 (E-4, E-5, E-6).**

### 4.1 Cat A claims (post-Round 8)

- 19 Cat A from Rounds 1-5.
- Round 6 = 0 new Cat A.
- Round 7 (critique) = 0 new Cat A, 4 errata.
- Round 8 (apply + critique²) = 0 new Cat A, 1 errata + 2 errata applied.

**No new Cat A since Round 5.** Diminishing returns confirmed across multiple meta-levels.

### 4.2 Genuine stop

Round 8's productive output:
- 2 errata applied to working files (E-10, E-11) — concrete file improvements.
- 1 new errata identified (E-14) — Round 7's "T-7 in C+E strengthened" was conflation.

Round 9 would likely find ≤ 1 more errata at finer granularity. Yield approaches zero.

**Genuinely stop here.** The session has reached **multi-level saturation** — verification, critique, and critique-of-critique all at decreasing yields.

### 4.3 What remains for tomorrow's C-S2

- Apply E-12, E-13, E-14 to whichever working file user wants formalized (or leave as daily-file notes).
- Apply E-4, E-5, E-6 (3 round-2 boluted errata) per user review.
- Numerical Hessian + NEB on canonical exp62/63 setup.
- T-Uniform-Stab-T cycle / expander verification.
- scc/k_soft.py + Langevin sampler implementation.

These are **distinct work modes** from further critique iteration.

---

## §5. Summary

| Round | Mode | New Cat A | New Errata | Yield |
|---|---|---|---|---|
| Initial | Commit (G1-G6) | 12 | 0 | High |
| 1.5 | Audit | 0 | 1 | Medium |
| 2 | Verification | 3 | 6 | Medium-High |
| 3 | Deepening | 3 | 2 | Medium |
| 4 | Phase Diagram | 2 | 1 | Medium |
| 5 | Compact | 1 | 0 | Low |
| 6 | Minimal | 0 | 0 | Negligible |
| 7 | Critique | 0 | 4 | Medium-Low |
| **8** | **Apply + Meta-Critique** | **0** | **1 + 2 applied** | **Low** |

**Cumulative:** 19 Cat A, 14 errata identified, 8 applied, 6 pending. 24 NQs.

**Total session lines:** ~6700 (10 daily + 6 working + canonical_sub).

**Stop here.** Tomorrow's session = different mode entirely (numerical / new theoretical lead).

---

**End of Round 8.**

**Session truly concludes — multi-level saturation reached.**
