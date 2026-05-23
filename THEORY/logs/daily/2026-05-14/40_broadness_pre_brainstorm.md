> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 40 — OP-HMORSE-BROADNESS Pre-Brainstorm

**Session:** 2026-05-14 (extension after CV-1.15 P7 + Track 2 working draft)
**Target:** Close OP-HMORSE-BROADNESS — analytic / numerical proof that T7-Enhanced closure-correction lift propagates to *all* tangent eigenmodes.
**This file covers:** brief framing of the broadness question + execution plan.
**Depends on reading:** `02_development.md` §4 (L-CLOSURE-LIFT CONJECTURE-broadness statement); `03_integration_and_new_open.md` §2.1 (OP-HMORSE-BROADNESS registered); CV114 `02_H_MORSE_statement_reconstruction.md` §6–§7; canonical.md T7-Enhanced (line 1138); `CODE/scc/operators.py` (J_Cl formula).

---

## §1. What is "broadness"?

**Narrow lift (T7-Enhanced as canonically stated):** Closure correction quadratic form $\langle v, (I-J_{\mathrm{Cl}})^\top(I-J_{\mathrm{Cl}}) v\rangle \geq (1-a_{\mathrm{cl}}/4)^2 \lVert v \rVert^2$ holds along *some* closure-aligned direction $v$.

**Broad lift (target):** The same inequality holds **uniformly** on the entire tangent space $T_{u^*}\Sigma_m$ (mod volume Goldstone $\mathbf{1}$).

**Why broadness matters.** Without it, $\mu_{\min}(\Pi_T H_{\mathrm{cl}} \Pi_T) \geq 2\lambda_{\mathrm{cl}}(1-a_{\mathrm{cl}}/4)^2$ is unproven. The bound applies only to closure-aligned eigenmode; some other eigenmode (e.g., boundary-localized) could be lower. L-CLOSURE-LIFT remains Cat B *conditional* on broadness.

---

## §2. Key insight emerging from operator inspection

From `CODE/scc/operators.py` (lines 63–101) and canonical Spec §9.2:

$$J_{\mathrm{Cl}}(u^*) = \mathrm{diag}(\sigma'(u^*) \cdot a_{\mathrm{cl}}) \cdot \bigl((1 - \eta_{\mathrm{cl}})I + \eta_{\mathrm{cl}} P\bigr)$$

where $\sigma'(z) = \sigma(z)(1-\sigma(z)) \leq 1/4$ (logistic sigmoid derivative bound).

For the mixing operator $M := (1-\eta_{\mathrm{cl}})I + \eta_{\mathrm{cl}} P$ on $\ell^2(\mathbb{R}^n)$:

- $P$ is *row-stochastic* (row sums = 1, $P\mathbf{1} = \mathbf{1}$).
- Per canonical §9.1 + scc.graph.py, $P = D^{-1}W$ where $W$ is symmetric adjacency, $D$ diagonal degree.
- $P$ is **similar to a symmetric matrix**: $P = D^{-1/2}(D^{-1/2}WD^{-1/2})D^{1/2}$, with $D^{-1/2}WD^{-1/2}$ symmetric.
- The spectral radius of $P$ is 1 (Perron eigenvalue, eigenvector $\mathbf{1}$).

For $v \perp \mathbf{1}$ (tangent vectors), $\lVert Pv \rVert \leq$ (something < 1)? Need more care since $P$ isn't symmetric. The relevant operator norm for $\ell^2$:

$$\lVert M \rVert_{\ell^2 \to \ell^2} = \sqrt{\rho(M^\top M)}.$$

For $M = (1-\eta)I + \eta P$, in general $\lVert M \rVert_{\ell^2 \to \ell^2}$ depends on $P$'s singular values. However, **the canonical claim A3** ($a_{\mathrm{cl}} < 4$ enforces contraction) requires:

$$\lVert J_{\mathrm{Cl}} \rVert_{\ell^2 \to \ell^2} \leq \frac{a_{\mathrm{cl}}}{4} \cdot \lVert M \rVert_{\ell^2 \to \ell^2} < 1.$$

If $\lVert M \rVert_{\ell^2 \to \ell^2} \leq 1$ (which holds at least for symmetric edge weights — to be verified for $P$ non-symmetric), then $\lVert J_{\mathrm{Cl}} \rVert_{\ell^2 \to \ell^2} \leq a_{\mathrm{cl}}/4$.

**Consequence (the broadness route).** If $\lVert J_{\mathrm{Cl}} \rVert_{\ell^2 \to \ell^2} \leq a_{\mathrm{cl}}/4 < 1$, then

$$\sigma_{\min}(I - J_{\mathrm{Cl}}) \;\geq\; 1 - \lVert J_{\mathrm{Cl}} \rVert_{\ell^2 \to \ell^2} \;\geq\; 1 - a_{\mathrm{cl}}/4,$$

so

$$(I - J_{\mathrm{Cl}})^\top (I - J_{\mathrm{Cl}}) \;\succeq\; (1 - a_{\mathrm{cl}}/4)^2 \cdot I$$

**uniformly on $\mathbb{R}^n$**, hence on tangent space — broad lift achieved.

This is essentially **Approach (b) collapsed to an operator-norm argument** — much sharper than the trace-based fallback. It also subsumes Approach (a) — irreducibility is not needed; the result is direct.

---

## §3. Open question for operator norm

The decisive question: **is $\lVert M \rVert_{\ell^2 \to \ell^2} \leq 1$?** I.e., is the mixing operator $M = (1-\eta_{\mathrm{cl}})I + \eta_{\mathrm{cl}} P$ a contraction on $\ell^2$?

**Sub-claims to verify:**
1. $\lVert P \rVert_{\ell^2 \to \ell^2} \leq 1$ when $P$ is row-stochastic over symmetric edge weights — **YES** when $P$ is similar to a symmetric matrix with spectrum in $[-1, 1]$. Standard graph-theoretic fact for $P = D^{-1}W$ on undirected graphs.
2. Convex combination $(1-\eta)I + \eta P$ inherits $\lVert \cdot \rVert_{\ell^2} \leq 1$ when both $I$ and $P$ are non-expansive — YES (convex combination of contractions).

**Verification needed.** Confirm $\lVert P \rVert_{\ell^2 \to \ell^2} = 1$ for the canonical $P = D^{-1}W$ on undirected graph. If yes, the broadness route is immediate.

---

## §4. Three-approach plan recap

| Approach | Strategy | Status estimate |
|---|---|---|
| **(a)** Closure Jacobian off-diagonal + Perron-Frobenius | Spectral mixing via irreducibility | likely *subsumed* by (b) — keep as complementary sharper bound if available |
| **(b)** Operator norm $\lVert I - J_{\mathrm{Cl}} \rVert$ + Weyl | Direct contraction argument | **leading candidate** — proves broadness uniformly |
| **(c)** Numerical full spectrum at canonical 15×15 | Direct verification | **always works** — confirms or refutes |

**Execution order.**
1. **Approach (b) first** — fastest path to analytic closure. If it works, OP-HMORSE-BROADNESS is closed Cat A (proof) for the closure term.
2. **Approach (c) numerically** — confirm + check residual term $2\sum_k r_k \nabla^2 Cl_k$ doesn't ruin things at the actual minimizer.
3. **Approach (a) optional** — if (b) succeeds, (a) may give a *sharper* constant or alternative form; document.

---

## §5. Full Hessian, not just $H_{\mathrm{cl}}$

Reminder: the goal is bound on $\mu_{\min}(\Pi_T H_{\mathcal{E}} \Pi_T)$ where $H_{\mathcal{E}} = H_{\mathrm{bd}} + H_{\mathrm{cl}} + H_{\mathrm{sep}}$ (per L-HMORSE-DECOMP in `02_development.md §3`).

- $H_{\mathrm{bd}}$ contributes $\geq -\beta \lvert W''(u^*) \rvert$ in worst case (boundary band) — attenuated via T-OP6-B's $\rho_{\mathrm{bd-band}}$ bound, but worst-case eigenvalue can be $-\beta$ in spinodal band.
- $H_{\mathrm{cl}}$ contributes $+2\lambda_{\mathrm{cl}}(1-a_{\mathrm{cl}}/4)^2$ (broad, if Approach (b) succeeds).
- $H_{\mathrm{sep}}$ contributes $\geq 0$ on tangent space.

**Residual correction.** $H_{\mathrm{cl}}$ has actual form $2(J_{\mathrm{Cl}} - I)^\top(J_{\mathrm{Cl}} - I) + 2\sum_k (Cl(u^*)_k - u^*_k) \nabla^2 Cl_k$. At a *critical point of full $\mathcal{E}$* (not $E_{\mathrm{cl}}$ alone), the residual $r = Cl(u^*) - u^*$ does not necessarily vanish. We need:

$$\bigl\lVert \sum_k r_k \nabla^2 Cl_k\bigr \rVert_{op} \;\leq\; \lVert r \rVert_\infty \cdot \max_k \lVert \nabla^2 Cl_k \rVert_{op}.$$

At an interior minimizer of $\mathcal{E}$, $\lVert r \rVert_\infty$ is empirically small (close to closure fixed point); $\lVert \nabla^2 Cl_k \rVert_{op}$ bounded by $\vert \sigma''\vert _{\max} \cdot a_{\mathrm{cl}}^2 \cdot \lVert M \rVert^2 \leq 0.1 \cdot a_{\mathrm{cl}}^2$ (since $\vert \sigma''\vert \leq 0.1$).

Numerical verification of $\lVert r \rVert_\infty$ at the canonical minimizer is part of Approach (c).

---

## §6. Operational decision

**Proceed with Approach (b)** as primary. Verify $\lVert P \rVert_{\ell^2 \to \ell^2} \leq 1$ first (literature: standard for $P = D^{-1}W$, undirected graph) — this is the only non-trivial step in the argument.

Numerical Approach (c) runs concurrently. Approach (a) deferred unless (b) hits unexpected obstacle.

**Decision Gate R2** (canonical alignment pre-check):
```
grep "operator norm\|J_Cl norm\|||J_Cl||\|sigma_min(I - J_Cl)" canonical/ working/
```
to be performed in `41_approach_a_jacobian.md` § R2 record.

---

## §7. Anticipated outcome

If (b) succeeds — and we have reasonable confidence it does — then:

- L-CLOSURE-LIFT broadness CONJECTURE → **PROVED** in `44_synthesis.md`.
- L-HMORSE-LOCAL Cat B becomes **unconditional** (subject only to residual-correction term being negligible at minimizers, verified via Approach (c) numerically).
- OP-HMORSE-BROADNESS → **CLOSED**.
- Proposed canonical promotion for CV-1.16 as L-CLOSURE-LIFT Cat A (instead of Cat B conditional). Actual promotion is separate P7 turn.

---

*End of `40_broadness_pre_brainstorm.md`. Next: `41_approach_a_jacobian.md` (deferred — Approach (a) optional) and `42_approach_b_trace.md` (PRIMARY, executed first).*
