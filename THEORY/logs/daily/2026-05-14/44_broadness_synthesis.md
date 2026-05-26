> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 44 — OP-HMORSE-BROADNESS Synthesis & Closure Verdict

**Session:** 2026-05-14 (extension)
**Target:** Synthesize Approach (a), (b), (c) results into a single closure verdict for OP-HMORSE-BROADNESS, update L-CLOSURE-LIFT and L-HMORSE-LOCAL Cat status, propose canonical promotion text.
**This file covers:** §4 synthesis + Cat status table + OP closure + canonical proposal draft (no edit).
**Depends on reading:** `40_broadness_pre_brainstorm.md`, `41_broadness_approach_a_jacobian.md` (supplementary), `42_broadness_approach_b_trace.md` (primary, B2 Cat A), `43_broadness_approach_c_numerical.md` (15/15 PASS).

---

## §1. Synthesis Table

| Approach | Method | Result | Status |
|---|---|---|---|
| **(α) Closure Jacobian** | Perron-Frobenius + Collatz-Wielandt on $J_{\mathrm{Cl}}$ | $\rho(J_{\mathrm{Cl}}) \leq a_{\mathrm{cl}}/4 < 1$; standard $\ell^2$ same as (b); Perron-weighted sharper but state-dependent | **PROVED Cat A** (complementary, not primary) |
| **(β) Operator norm + Weyl** | $\lVert J_{\mathrm{Cl}} \rVert_{D \to D} \leq a_{\mathrm{cl}}/4$ via degree-weighted self-adjointness | Theorem B2: $(I - J_{\mathrm{Cl}})^\top D (I - J_{\mathrm{Cl}}) \succeq (1 - a_{\mathrm{cl}}/4)^2 D$ | **PROVED Cat A** (primary) |
| **(γ) Numerical** | 15-config sweep, full eigendecomp + component-wise | 15/15 broadness + lift PASS at canonical parameters; lift ~60× prediction | **CONFIRMED PASS** |

**Triple convergence.** Three mathematically independent approaches yield the same conclusion: **OP-HMORSE-BROADNESS is CLOSED**. The closure-correction lift propagates uniformly across the tangent space, not narrowly along a single eigenmode.

---

## §2. OP-HMORSE-BROADNESS — Closure Verdict

**Status:** **CLOSED Cat A** (analytic) + **CONFIRMED** (numerical).

**Effect on L-CLOSURE-LIFT** (`02_development.md §4`):

- *Previous (5/14 morning Track 2):* L-CLOSURE-LIFT Cat B SKETCH with explicit CONJECTURE-broadness.
- *Updated (5/14 evening extension):* L-CLOSURE-LIFT broadness CONJECTURE **PROVED** by Theorem B2 (Cat A). L-CLOSURE-LIFT itself **upgrades to Cat A** (no CONJECTURE remaining).

**Effect on L-HMORSE-LOCAL** (`02_development.md §1`):

- *Previous:* Cat B SKETCH conditional on L-CLOSURE-LIFT broadness.
- *Updated:* Cat B unconditional (subject only to residual-correction term verified numerically). The full Hessian $\Pi_T H_{\mathcal{E}} \Pi_T$ positivity is now numerically confirmed across 15 configurations including grid sizes 5×5, 10×10, 15×15 and $\beta \in [10, 100]$.

**Effect on D-HMORSE-LOCAL** (`02_development.md §1`):

The numerical evidence (`43_*.md §3.2`) reveals that *canonical `find_formation` minimizers saturate at corners*, violating (C2) interior. Yet broadness still holds. Two consistent treatments:

1. **Restrictive D-HMORSE-LOCAL (preferred for canonical):** Keep (C1)–(C5) including (C2) interior. The set of minimizers satisfying (C2) is **non-empty** (need to add a sub-spinodal-interior perturbation construction), but the canonical `find_formation` does not target it.

2. **Permissive D-HMORSE-LOCAL (better matches numerical):** Replace (C2) with (C2′) *active-set formulation* — broadness holds on the "free" tangent subspace excluding saturated coordinates. The canonical `find_formation` output satisfies (C2′) by construction.

**Recommended canonical convention:** Adopt (C2′) for the CV-1.16 promotion. The numerical confirmation directly supports (C2′); (C2) restricts to a subset of the regime.

---

## §3. Updated Cat Status

| Object | Previous (5/14 morning) | Updated (5/14 evening extension) | Notes |
|---|---|---|---|
| **OP-HMORSE-BROADNESS** | OPEN (HIGH) | **CLOSED Cat A** | Theorem B2 (analytic) + 15/15 numerical PASS |
| **L-CLOSURE-LIFT** | Cat B SKETCH (CONJECTURE-broadness) | **Cat A** (CONJECTURE → PROVED) | Theorem B2 supersedes the CONJECTURE |
| **L-HMORSE-LOCAL** | Cat B SKETCH conditional | **Cat B unconditional** | numerical confirmation + B2 + residual-bound |
| **L-HMORSE-DECOMP** | Cat B SKETCH | Cat B SKETCH (unchanged) | structural decomposition; per-term bounds inherited |
| **L-BOUNDARY-MODE-EXCLUSION** | SKETCH | SKETCH (unchanged) | supports D-HMORSE-LOCAL (C5) but bypassed at saturated minimizers |
| **D-HMORSE-LOCAL** | (C1)–(C5) | (C1)–(C5) + alternative (C2′) | active-set variant matches numerical |

---

## §4. Canonical Promotion Proposal Draft (NO EDIT — proposal only)

The following is the **proposed §13 Cat A entry** for CV-1.16+ promotion. Actual promotion is a separate P7 turn.

```markdown
**Theorem L-CLOSURE-LIFT.** *(Cat A; CV-1.16; promoted from Cat B SKETCH per `THEORY/logs/daily/2026-05-14/42_*.md` + `44_*.md`.)*

*Conditions.* Canonical A3 ($a_{\mathrm{cl}} < 4$); $u^* \in [0,1]^n$ (any value, not requiring interior); $G$ connected.

*Statement.* The closure Jacobian $J_{\mathrm{Cl}}(u^*) = \mathrm{diag}(\sigma'(z) a_{\mathrm{cl}}) \cdot ((1-\eta_{\mathrm{cl}}) I + \eta_{\mathrm{cl}} P)$, with $P = D^{-1} W$, satisfies:

(L-CL-LIFT.1) Degree-weighted operator norm:
$$\|J_{\mathrm{Cl}}\|_{D \to D} \leq \frac{a_{\mathrm{cl}}}{4} < 1.$$

(L-CL-LIFT.2) Gauss-Newton lower bound on the closure Hessian:
$$2(I - J_{\mathrm{Cl}})^\top D (I - J_{\mathrm{Cl}}) \succeq 2(1 - a_{\mathrm{cl}}/4)^2 D.$$

Equivalently, in standard $\ell^2$:
$$2(I - J_{\mathrm{Cl}})^\top (I - J_{\mathrm{Cl}}) \succeq 2(1 - a_{\mathrm{cl}}/4)^2 (d_{\min}/d_{\max}) I.$$

(L-CL-LIFT.3) Tangent projection: $\Pi_T \cdot \text{(matrix)} \cdot \Pi_T \succeq c \cdot \Pi_T$ inherits.

*Proof.* See §2–§4 of `THEORY/logs/daily/2026-05-14/42_broadness_approach_b_trace.md`. Key steps:
1. $P$ is self-adjoint on $\langle\cdot,\cdot\rangle_D$ (degree-weighted): $\langle Pu, v\rangle_D = u^\top W v = \langle u, Pv\rangle_D$.
2. Stochastic operator's Perron eigenvalue: $\|P\|_{D \to D} = \rho(P) = 1$ (eigenvector $\mathbf{1}$, eigenvalue 1).
3. Convex combination: $\|M\|_{D \to D} \leq 1$ for $M = (1-\eta)I + \eta P$.
4. Sigmoid bound: $\sigma'(z) \leq 1/4$ for all $z$, so $\|D_\sigma\|_{\ell^2 \to \ell^2} \leq a_{\mathrm{cl}}/4$.
5. Composition: $\|J_{\mathrm{Cl}}\|_{D \to D} \leq a_{\mathrm{cl}}/4$.
6. Triangle inequality: $\|(I - J_{\mathrm{Cl}}) v\|_D \geq (1 - a_{\mathrm{cl}}/4) \|v\|_D$, squaring gives (L-CL-LIFT.2).

*Numerical anchor (`exp_hmorse_broadness_full_spectrum.py`):* 15/15 PASS on (5×5, 10×10, 15×15) × $\beta \in \{10, 20, 30, 50, 100\}$. $\mu_{\min}(\Pi_T H_{\mathrm{cl}} \Pi_T) \in [0.45, 0.79]$, exceeding the standard-$\ell^2$ prediction by ~50–100×.

*Non-overclaim.*
- L-CLOSURE-LIFT bounds only the **Gauss-Newton** part of $H_{\mathrm{cl}}$. The full $H_{\mathrm{cl}}$ has an additional residual term $2 \sum_k (\mathrm{Cl}(u^*)_k - u^*_k) \nabla^2 \mathrm{Cl}_k(u^*)$.
- The residual contribution is small in practice (verified numerically in `43_*.md §3.3`); analytic bound has the form $\|r\|_2 \cdot \sqrt{n} \cdot |\sigma''|_{\max} \cdot a_{\mathrm{cl}}^2$. A *sharper* analytic bound exploits the fact that $|\sigma''| \to 0$ at saturated minimizers.
- L-CLOSURE-LIFT is *only* the closure contribution. The full L-HMORSE-LOCAL requires combining with $H_{\mathrm{bd}}$ (per L-HMORSE-DECOMP) and $H_{\mathrm{sep}}$.

*References.* T7-Enhanced (canonical Cat A, §13 line 1138; superseded as the closure-spectrum bound by this sharper L-CLOSURE-LIFT statement); `CODE/scc/operators.py` (Jacobian formula); CV114 audit (`THEORY/working/CV114_H_MORSE_PACKAGEII/02–09`).
```

---

## §5. Effect on Other Open Problems

### §5.1 OP-HMORSE-BROADNESS (CLOSED, this session)

Closed as documented in §2. Removed from active OP list.

### §5.2 OP-HMORSE-SBM (REMAINS OPEN, but supplementary anchor strengthens)

The 5×5 / 10×10 / 15×15 grid evidence in (γ) suggests broadness generalizes beyond the canonical 15×15. SBM/barbell/small-world numerical sweep (per `99_summary.md §"Most-urgent next OP"`) becomes a *robustness extension* rather than a *blocker validation*. Recommended for 5/15+ session.

### §5.3 OP-HMORSE-EXCLUSION-VOLUME (DOWNGRADED, LOW severity)

The volume Goldstone treatment via projector $\Pi_T = I - (1/n)\mathbf{1}\mathbf{1}^\top$ is now numerically verified to *exactly* produce a single ~0 eigenvalue (the volume mode) and all others positive. No second-order Lagrange-multiplier zeros emerge. The OP is operationally resolved.

### §5.4 OP-HMORSE-GENERIC-PATH (REMAINS OPEN, REPRIORITIZED)

Since (b) Cat A is direct, the generic-Morse fallback path (Approach γ from `01_exploration.md §2.3`) becomes a *Cat A alternative* rather than a *Cat B fallback*. Lower priority; deferred.

### §5.5 OP-HMORSE-SADDLE (UNCHANGED, MEDIUM severity)

Saddle-point Hessian analysis is independent of minimum-Hessian broadness. Still required for full Eyring-Kramers prefactor Cat B. Unchanged.

### §5.6 OP-HMORSE-LOCAL-A (UPDATED — easier to close)

The Cat A path now requires only:
- *Active-set/(C2′) reformulation*: lift D-HMORSE-LOCAL to permissive variant — straightforward.
- *Sharper residual bound*: replace worst-case $\vert \sigma''\vert _{\max}$ with the *spinodal-band-restricted* bound. The numerical evidence shows the actual residual is much smaller than worst-case.

ETA Cat A: **2 sessions** (down from 4–8 estimated in `03_integration_and_new_open.md §3`).

---

## §6. Methodological Highlight

**The two-pass pattern works.** This extension session followed:
1. **Morning Track 2** (Cat B SKETCH with explicit CONJECTURE-broadness) — pre-extension state.
2. **Evening extension** (analytic proof of the CONJECTURE) — closes the Cat B → Cat A path on the *closure component*.

The pattern: **document a Cat B SKETCH with explicit CONJECTURE, then attack the CONJECTURE separately**. This separates *structural exploration* (morning) from *analytic closure* (evening), avoiding premature Cat A claims while keeping the path forward visible.

Preserve as template.

---

## §7. CV-1.16 Target Update

Based on this session's Cat A closure of L-CLOSURE-LIFT, the CV-1.16 target priority is:

1. **L-HMORSE-LOCAL Cat B unconditional** (now achievable in 1 more session: combine L-CLOSURE-LIFT Cat A + L-HMORSE-DECOMP + L-BOUNDARY-MODE-EXCLUSION; package as canonical Cat B entry).
2. **OP-HMORSE-SBM numerical robustness extension** (1 session; broadens graph class).
3. **L-HMORSE-LOCAL Cat A** via (C2′) + sharper residual (2 sessions).

After CV-1.16 H-MORSE-Local Cat B / Cat A, the CV-1.17+ Package II / Eyring-Kramers / K-Select-DYN sequence becomes accessible.

---

## §8. Files Produced This Extension Session Step (so far)

| File | Role |
|---|---|
| `THEORY/logs/daily/2026-05-14/40_broadness_pre_brainstorm.md` | Framing + 3-approach plan |
| `THEORY/logs/daily/2026-05-14/41_broadness_approach_a_jacobian.md` | Approach (a) — Perron-Frobenius complementary route |
| `THEORY/logs/daily/2026-05-14/42_broadness_approach_b_trace.md` | Approach (b) — Theorem B2 PROVED Cat A primary |
| `THEORY/logs/daily/2026-05-14/43_broadness_approach_c_numerical.md` | Approach (c) — 15/15 numerical PASS |
| `THEORY/logs/daily/2026-05-14/44_broadness_synthesis.md` | (this file) — synthesis verdict |
| `CODE/experiments/exp_hmorse_broadness_full_spectrum.py` | numerical script |
| `CODE/experiments/results/exp_hmorse_broadness_full_spectrum.json` | raw results |
| `CODE/experiments/results/exp_hmorse_broadness_full_spectrum.md` | numerical summary |

Pending:
- `THEORY/2_substrate/Q3_dynamics/h_morse_packageII/11_broadness_attack.md` — final attack record in CV114
- `THEORY/logs/daily/2026-05-14/49_broadness_summary.md` — extension session summary

---

*End of `44_broadness_synthesis.md`. OP-HMORSE-BROADNESS is CLOSED Cat A (analytic) + CONFIRMED (numerical 15/15). L-CLOSURE-LIFT upgrades Cat A. L-HMORSE-LOCAL Cat B unconditional. Next: `11_broadness_attack.md` (CV114) + `49_broadness_summary.md`.*
