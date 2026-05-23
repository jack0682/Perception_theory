> [!nav] Linked: [[MOC_H_MORSE_packageII]] · [[MOC_Q3_stochastic_dynamics]] · [[THEORY_INDEX]]

# 11 — OP-HMORSE-BROADNESS Closure (Attack Record)

**Working folder:** `THEORY/working/CV114_H_MORSE_PACKAGEII/`
**Session:** 2026-05-14 (W7-Day5 extension after CV-1.15 P7 promotion + H-MORSE-Local Cat B working draft)
**Status:** **CLOSED Cat A** (analytic) + **CONFIRMED** (numerical 15/15 PASS)

This file is the **canonical-promotion-ready record** of the OP-HMORSE-BROADNESS attack. It consolidates the daily-log analytic and numerical work into a single document suitable for canonical Cat A entry in CV-1.16+.

**Prerequisites (must read before promotion):**
- `THEORY/logs/daily/2026-05-14/01_exploration.md` — 3-approach plan, primary selection.
- `THEORY/logs/daily/2026-05-14/02_development.md` §3-§4 — L-HMORSE-DECOMP, L-CLOSURE-LIFT (now upgraded by this file).
- `THEORY/logs/daily/2026-05-14/42_broadness_approach_b_trace.md` — full Theorem B2 proof.
- `THEORY/logs/daily/2026-05-14/41_broadness_approach_a_jacobian.md` — Perron-Frobenius alternative route.
- `THEORY/logs/daily/2026-05-14/43_broadness_approach_c_numerical.md` — 15/15 numerical PASS.
- `THEORY/logs/daily/2026-05-14/44_broadness_synthesis.md` — synthesis + canonical proposal text.

---

## §1. Result Statement

**Theorem L-CLOSURE-LIFT (CV-1.16+ promotion candidate).** *(Cat A.)*

Let $G = (X, W)$ be a connected, undirected, weighted graph with symmetric adjacency $W$, degree matrix $D = \mathrm{diag}(\sum_y W(x,y))$, and row-normalized aggregation $P = D^{-1} W$. Let
$$\mathrm{Cl}(u) = \sigma\bigl(a_{\mathrm{cl}}\bigl((1-\eta_{\mathrm{cl}}) u + \eta_{\mathrm{cl}} P u - \tau_{\mathrm{cl}}\bigr)\bigr)$$
be the canonical sigmoid closure (canonical §9.2). Assume the canonical A3 contraction $a_{\mathrm{cl}} < 4$.

Then for any $u^* \in [0,1]^n$:

(i) The closure Jacobian $J_{\mathrm{Cl}}(u^*) = \mathrm{diag}(\sigma'(z(u^*)) \cdot a_{\mathrm{cl}}) \cdot M$ with $M = (1-\eta_{\mathrm{cl}})I + \eta_{\mathrm{cl}} P$ satisfies
$$\lVert J_{\mathrm{Cl}}(u^*) \rVert_{D \to D} \leq \frac{a_{\mathrm{cl}}}{4} < 1.$$

(ii) The Gauss-Newton lower bound on the closure Hessian holds uniformly:
$$2 (I - J_{\mathrm{Cl}}(u^*))^\top D (I - J_{\mathrm{Cl}}(u^*)) \;\succeq\; 2(1 - a_{\mathrm{cl}}/4)^2 \cdot D.$$

(iii) Equivalently, in the standard $\ell^2$ inner product:
$$2 (I - J_{\mathrm{Cl}}(u^*))^\top (I - J_{\mathrm{Cl}}(u^*)) \;\succeq\; 2(1 - a_{\mathrm{cl}}/4)^2 \cdot (d_{\min}/d_{\max}) \cdot I.$$

(iv) Tangent restriction. For the tangent projector $\Pi_T = I - (1/n) \mathbf{1} \mathbf{1}^\top$ associated with the volume constraint $\mathbf{1}^\top u = m$, the same lower bound holds on $\Pi_T \cdot$ (matrix) $\cdot \Pi_T$ relative to $\Pi_T \cdot D \cdot \Pi_T$ (resp. $\Pi_T$).

**Significance.** This is the **broadness** statement: the closure-correction lift propagates *uniformly* across the entire tangent space — not narrowly along a single closure-aligned eigenmode. It is **stronger** than the canonical T7-Enhanced bound (which gives the same lower bound *along a specific direction* but not uniformly).

---

## §2. Proof (Cat A, complete)

The proof is in `THEORY/logs/daily/2026-05-14/42_broadness_approach_b_trace.md §2-§4`. Outline:

**Step 1 (Lemma B1' — degree-weighted self-adjointness of $P$).** For symmetric $W$, the row-stochastic operator $P = D^{-1} W$ is self-adjoint on the degree-weighted inner product $\langle u, v\rangle_D := u^\top D v$:
$$\langle Pu, v\rangle_D = u^\top P^\top D v = u^\top W v = u^\top D P v = \langle u, P v\rangle_D.$$
Hence $\lVert P \rVert_{D \to D} = \rho(P) = 1$ (Perron eigenvalue, eigenvector $\mathbf{1}$).

**Step 2 (Convex combination).** $M = (1 - \eta_{\mathrm{cl}}) I + \eta_{\mathrm{cl}} P$ with $\eta_{\mathrm{cl}} \in [0,1]$. Since $\lVert I \rVert_{D \to D} = 1 = \lVert P \rVert_{D \to D}$, by convexity $\lVert M \rVert_{D \to D} \leq 1$.

**Step 3 (Sigmoid bound).** $\sigma'(z) = \sigma(z)(1 - \sigma(z)) \leq 1/4$ for all real $z$. Hence $\lVert \mathrm{diag}(\sigma' \cdot a_{\mathrm{cl}}) \rVert_{\ell^2 \to \ell^2} \leq a_{\mathrm{cl}}/4$.

**Step 4 (Composition).** $J_{\mathrm{Cl}} = D_\sigma M$ with $D_\sigma = \mathrm{diag}(\sigma' a_{\mathrm{cl}})$. We have $D_\sigma$ as a diagonal positive scaling, which is self-adjoint on $\langle\cdot,\cdot\rangle_D$ (since diagonal matrices commute with $D$ in the inner-product structure). Then
$$\lVert J_{\mathrm{Cl}} \rVert_{D \to D} = \lVert D_\sigma M \rVert_{D \to D} \leq \lVert D_\sigma \rVert_{D \to D} \cdot \lVert M \rVert_{D \to D} \leq \frac{a_{\mathrm{cl}}}{4} \cdot 1 = \frac{a_{\mathrm{cl}}}{4}.$$

This is *less than 1* by canonical A3 ($a_{\mathrm{cl}} < 4$). Statement (i) proved.

**Step 5 (Lower bound on $I - J_{\mathrm{Cl}}$).** For any $v \in \mathbb{R}^n$:
$$\lVert (I - J_{\mathrm{Cl}}) v \rVert_D \geq \lVert v \rVert_D - \lVert J_{\mathrm{Cl}} v \rVert_D \geq (1 - a_{\mathrm{cl}}/4) \lVert v \rVert_D.$$
Squaring: $\langle (I - J_{\mathrm{Cl}}) v, (I - J_{\mathrm{Cl}}) v\rangle_D \geq (1 - a_{\mathrm{cl}}/4)^2 \lVert v \rVert_D^2$. Statement (ii) proved.

**Step 6 (Standard-$\ell^2$ form).** Using $d_{\min} I \preceq D \preceq d_{\max} I$:
$$d_{\max} \cdot A^\top A \succeq A^\top D A \succeq (1 - a_{\mathrm{cl}}/4)^2 D \succeq (1 - a_{\mathrm{cl}}/4)^2 d_{\min} \cdot I,$$
giving statement (iii).

**Step 7 (Tangent projection).** If $A \succeq c \cdot B$ with $B \succeq 0$, then $\Pi^\top A \Pi \succeq c \cdot \Pi^\top B \Pi$ for any projection $\Pi$ (standard quadratic-form fact). Statement (iv) follows. $\square$

---

## §3. Alternative Route (Approach (a), supplementary)

Per `THEORY/logs/daily/2026-05-14/41_broadness_approach_a_jacobian.md`, an alternative analytic route via Perron-Frobenius / Collatz-Wielandt:

- $\rho(J_{\mathrm{Cl}}) \leq a_{\mathrm{cl}}/4 < 1$ (Collatz-Wielandt, irreducibility on connected support).
- Standard-$\ell^2$ bound matches Theorem B2.
- Perron-weighted bound is sharper but state-dependent.

Approach (a) is **redundant** with (b) but provides independent verification. The canonical promotion uses (b) because of state-independent constants.

---

## §4. Numerical Confirmation

`CODE/experiments/exp_hmorse_broadness_full_spectrum.py` (created 2026-05-14):

- **Sweep:** 3 grid sizes (5×5, 10×10, 15×15) × 5 β values ({10, 20, 30, 50, 100}) = 15 configs.
- **Asymmetric edge weights** (perturb=0.1, seed=42) to satisfy (C4) symmetry-broken.
- **Procedure:** `find_formation` → projected Hessian via FD → eigendecomposition → check $\mu_{\min} > 0$ + L-CLOSURE-LIFT prediction.
- **Result:** **15/15 PASS** for both broadness and lift.
- **Quantitative:** $\mu_{\min}(\Pi_T H_{\mathrm{cl}} \Pi_T) \in [0.45, 0.79]$, exceeding Theorem B2 standard-form prediction (~0.0075) by ~60×. The conservative prediction reflects $d_{\min}/d_{\max}$ and worst-case $\sigma'$; actual sigmoid derivative at saturated minimizers is much smaller, making the lift stronger.
- **Residual norm:** $\lVert r \rVert_2 \in [0.73, 2.33]$ — large in absolute terms but does not break $\mu_{\min} > 0$, because residual contribution is concentrated in the boundary band where $|\sigma''| \approx 0$ at saturated minimizers.
- **Regression check:** Full test suite passes (215 passed, 1 xfailed).

Results: `CODE/experiments/results/exp_hmorse_broadness_full_spectrum.{json, md}`.

---

## §5. Effect on CV114 Audit Outputs

This file *supersedes* the broadness-related portions of the following CV114 audit documents:

- `02_H_MORSE_statement_reconstruction.md §6` "Closure correction gap" — the bound holds *uniformly* across the tangent space, not narrowly along closure-aligned direction.
- `03_energy_landscape_and_hessian.md` $H_{\mathrm{cl}}$ analysis — the operator-norm route obviates the worry about "narrow vs broad lift."
- `08_candidate_lemma_chain.md` Path B — Cat B "with broadness conjecture" → Cat B "unconditional with L-CLOSURE-LIFT Cat A".

The CV114 final recommendation in `09_CV114_recommendation.md` ("Path B — H-MORSE-Local Cat B candidate") is **substantively strengthened**: the closure-component is now Cat A; the *full* L-HMORSE-LOCAL is Cat B unconditional pending only the residual-correction term verified numerically.

---

## §6. Status Table (CV114 working folder)

| Document | Pre-attack status | Post-attack status |
|---|---|---|
| `02_H_MORSE_statement_reconstruction.md` | Candidate A/B/C/D classification | UNCHANGED; broadness clarified by §5 |
| `03_energy_landscape_and_hessian.md` | $H_{\mathrm{cl}} \succeq$ ? | UPDATED: $H_{\mathrm{cl}}^{\mathrm{GN}} \succeq 2(1-a_{\mathrm{cl}}/4)^2 D$ uniformly |
| `04_degeneracy_catalogue.md` | 14 degeneracy classes | UNCHANGED; (C4) symmetry-broken still required for non-degeneracy |
| `05_counterexample_search.md` | 7 CE to unconditional H-MORSE | UNCHANGED; all CE excluded by (C4) ∪ (C2′) in D-HMORSE-LOCAL |
| `06_packageII_dependency_map.md` | H-MORSE → Package II | UPDATED: H-MORSE-Local Cat B unblocks partial Package II |
| `08_candidate_lemma_chain.md` Path B | Cat B SKETCH with CONJECTURE | **L-CLOSURE-LIFT Cat A**; Path B Cat B unconditional |
| `09_CV114_recommendation.md` Path B | Recommended target | **Strengthened**; CV-1.16 promotion ready |
| `11_broadness_attack.md` (this file) | (not existed) | **CREATED**; closure record |

---

## §7. CV-1.16 Promotion Readiness Checklist

| Requirement | Status |
|---|---|
| Theorem statement (Cat A) with precise conditions | ✓ §1 above |
| Complete proof | ✓ §2 above (per `42_*.md`) |
| Alternative independent proof | ✓ §3 (per `41_*.md`) |
| Numerical confirmation across multiple regimes | ✓ §4 (15/15 PASS) |
| Counterexample exclusion documented | ✓ (CV114 `05_*.md` 7 CE all excluded) |
| Effect on dependent canonical theorems | ✓ T-P-F-ε0-K H5 partial upgrade possible; Package II Cat B path opens |
| Test-suite regression check | ✓ 215 passed, 1 xfailed |
| Naming and convention alignment | ✓ Uses canonical: $J_{\mathrm{Cl}}$, $M$, $P$, $a_{\mathrm{cl}}$, $\eta_{\mathrm{cl}}$, $\sigma'$ from `CODE/scc/operators.py` |
| Audit chain (this file + 41 + 42 + 43 + 44) | ✓ Five-document chain in `THEORY/logs/daily/2026-05-14/` |
| **READY for P7 promotion turn** | ✓ |

---

## §8. Non-Overclaim (preserved into CV-1.16+ entry)

- **L-CLOSURE-LIFT is the Gauss-Newton (linearized) part.** The full $H_{\mathrm{cl}}$ has an additional residual-correction term $2 \sum_k (Cl(u^*)_k - u^*_k) \nabla^2 \mathrm{Cl}_k(u^*)$. At full-energy critical points, this residual is small but nonzero. Numerical: $\lVert r \rVert_2$ moderate (up to ~2.3 on 15×15) but residual-correction *contribution* to $\mu_{\min}$ is small because $|\sigma''| \approx 0$ at saturated nodes.
- **L-CLOSURE-LIFT is only the closure component.** Full L-HMORSE-LOCAL also requires $H_{\mathrm{bd}} + H_{\mathrm{sep}}$ contributions. Total $\mu_{\min}$ depends on combined behavior; see L-HMORSE-DECOMP (`02_development.md §3`).
- **D-HMORSE-LOCAL conditions (C1)–(C5) or (C2′) variant required.** L-CLOSURE-LIFT alone is parameter-graph-independent (just needs $a_{\mathrm{cl}} < 4$ + connected graph). L-HMORSE-LOCAL needs the symmetry-broken + active-set conditions of D-HMORSE-LOCAL.
- **Cat A is for the closure-component bound, not for L-HMORSE-LOCAL as a whole.** L-HMORSE-LOCAL is Cat B unconditional (analytic + numerical); Cat A path goes via OP-HMORSE-LOCAL-A (OP-HMORSE-SBM extension + sharper residual + active-set treatment).

---

*End of `11_broadness_attack.md`. This is the CV-1.16+ canonical promotion candidate record. Actual promotion is a separate P7 turn in a future session.*
