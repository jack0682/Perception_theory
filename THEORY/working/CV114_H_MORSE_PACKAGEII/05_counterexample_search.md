> [!nav] Linked: [[MOC_H_MORSE_packageII]] · [[MOC_Q3_stochastic_dynamics]] · [[THEORY_INDEX]]

# 05 — Counterexample Search

Agent D (Counterexample Hunter) — explicit finite-graph configurations that violate unconditional H-MORSE.

---

## Setup

We test the proposition

> **(H-MORSE-Unconditional):** For every finite connected graph $G$ and every critical point $u^* \in \Sigma_m^\circ$ of the full SCC energy $\mathcal E$ in the canonical parameter window, the projected Hessian $\Pi_T H_\mathcal E(u^*) \Pi_T$ has $\mu_\mathrm{min} > 0$.

If we find a configuration where $\mu_\mathrm{min} = 0$ (exact zero eigenvalue), unconditional H-MORSE is **refuted**.

---

## Counterexample 1 — Cycle $C_n$ with single-blob minimizer

**Graph:** Cycle $C_n$, $n \geq 6$, with $n$ vertices arranged in a ring.

**Configuration:** Localized single-formation minimizer $u^*$ supported on a contiguous arc, e.g., $u^*(i) = \phi(d(i, x_*) / \xi_0)$ for some profile $\phi$ centered at $x_*$ with interface width $\xi_0$.

**Degeneracy:** Discrete translation $\mathbb Z_n$ acts freely. The orbit $\{u^* \circ \mathrm{shift}_k\}_{k=0}^{n-1}$ contains $n$ equienergetic minimizers. The orbit-tangent direction
$$\delta u_x(i) := u^*(i+1) - u^*(i) = \partial_x u^*(i) \text{ (discrete)}$$
satisfies $H_\mathcal E(u^*) \delta u_x = 0$ (sub-spinodal) or $H_\mathcal E(u^*) \delta u_x = O(e^{-c/\xi_0}) \delta u_x$ (super-lattice, V5b-T-b).

**Canonical anchor:** V5b-T-zero (canonical.md line 1303, **Cat A**): on translation-invariant graphs under sub-spinodal $c$, every corner-saturated minimizer has Goldstone eigenvalue exactly 0.

**Verdict:** **Unconditional H-MORSE FAILS on $C_n$ in sub-spinodal regime.** In super-lattice (spinodal interior with $\zeta > \zeta_*$), Goldstone eigenvalue is exponentially small but nonzero — technically Morse, practically degenerate.

**Repair:** Either (a) restrict to non-translation-invariant graphs (canonical 15×15 free-BC), or (b) impose orbital quotient by $\mathbb Z_n$.

---

## Counterexample 2 — Torus $T^d$ with localized minimizer

**Graph:** $d$-dimensional torus $T^d_L$, $d \geq 1$, side length $L$.

**Configuration:** Same as #1, in $d$ dimensions. Localized blob at position $x_*$.

**Degeneracy:** Discrete translation $\mathbb Z_L^d$ acts freely. **$d$-dimensional Goldstone manifold** of translates; all $d$ directions $\delta u_{x_\mu}$ are zero modes (V5b-T-zero) or exponentially small (V5b-T-b).

**Canonical anchor:** canonical.md Theorem 1 line 1406 — translation-derivative Goldstone basis is canonical for translation-invariant graphs.

**Verdict:** **Unconditional H-MORSE FAILS on $T^d$.** Higher-dimensional Morse-Bott (zero subspace of dim $d$).

**Repair:** Same as #1.

---

## Counterexample 3 — $D_4$-symmetric grid with center-located minimizer

**Graph:** $L \times L$ grid with free boundary conditions, $L \geq 5$. Automorphism group includes $D_4$ (rotations and reflections of the square).

**Configuration:** Minimizer $u^*$ centered at the geometric center $(\lceil L/2 \rceil, \lceil L/2 \rceil)$, fixed by the full $D_4$ stabilizer.

**Degeneracy:** $D_4$ has 8 elements; its irreducible representations include two 1-dim and one 2-dim. The 2-dim irrep gives a **doubly degenerate Hessian eigenvalue pair** (Maschke + Schur).

**Canonical anchor:** canonical.md Theorem 1 (orbital, Cat A): orbital decomposition by $G_u$. For $G_u = D_4$, the 2-dim irrep produces an unavoidable eigenvalue degeneracy.

**Verdict:** **Unconditional H-MORSE FAILS at $D_4$-symmetric minimizer.** The Hessian is positive definite (no zero) but has a 2-fold eigenvalue degeneracy, which is a **Morse-Bott** rather than Morse condition. For Eyring-Kramers, Morse-Bott requires Bismut-Lebeau extension.

**Repair:** Either (a) impose M-A2 (trivial stabilizer, excludes center-located minimizer), or (b) extend EK to Morse-Bott via Bismut-Lebeau.

---

## Counterexample 4 — Uniform state at T8-Full bifurcation threshold

**Graph:** Any finite connected graph with Fiedler $\lambda_2 > 0$.

**Configuration:** $u^* \equiv c \mathbf 1$ (uniform state), with $c$ in spinodal interior and $\beta/\alpha = 4\lambda_2 / \lvert W''(c) \rvert$ — exactly at the T8-Full bifurcation threshold.

**Degeneracy:** Projected Hessian is $4\alpha \Pi_T L \Pi_T + \beta W''(c) \Pi_T = 4\alpha \cdot \mathrm{diag}(\lambda_2, \lambda_3, \ldots) - \beta \lvert W''(c) \rvert$. At the threshold, the lowest eigenvalue (along the Fiedler direction $\phi_2$) is exactly $4\alpha\lambda_2 - \beta\vert W''(c)\vert = 0$.

**Verdict:** **Unconditional H-MORSE FAILS at the bifurcation parameter.** This is a codimension-1 set in parameter space — measure zero, but structural.

**Repair:** Impose M-A1' that **excludes the bifurcation locus** — work in the open set $\beta/\alpha > 4\lambda_2 / \lvert W''(c) \rvert + \eta$ for some $\eta > 0$, away from threshold.

---

## Counterexample 5 — Reflection-symmetric minimizer on path $P_n$

**Graph:** Path $P_n$, $n \geq 3$, with reflection symmetry $\sigma : i \mapsto n + 1 - i$.

**Configuration:** Minimizer $u^*$ that is reflection-symmetric: $u^*(i) = u^*(n+1-i)$.

**Degeneracy:** $G_u \supseteq \mathbb Z_2$ (the reflection). The orbital decomposition splits tangent space into symmetric ($+1$ irrep) and antisymmetric ($-1$ irrep) blocks. Each block separately Morse, but if both blocks have the same lowest eigenvalue (which can happen at fine-tuned parameters), the combined eigenvalue is doubly degenerate.

**Canonical anchor:** canonical.md Theorem 1 orbital decomposition (Cat A).

**Verdict:** **Generic fine-tuning failure.** At typical parameters, the two blocks have distinct eigenvalues; only at a codimension-1 surface in parameter space do they collide.

**Repair:** Generic-parameter assumption (off codimension-1 surface) suffices. Or impose M-A2 to break reflection.

---

## Counterexample 6 — Boundary critical point with active constraints

**Graph:** Any 2D grid.

**Configuration:** $u^*$ has $u^*_i = 1$ on a "core" subset and $u^*_i = 0$ on "void" subset, with thin "interface" in between. Critical points where active inequality constraints saturate (boundary of $[0, 1]^n$).

**Degeneracy:** Tangent space at such a point includes directions $v$ where $v_i = 0$ for $i$ in either active-0 or active-1 region. Hessian eigenvalues in these directions can be zero (no Hessian contribution from saturated component).

**Source:** canonical.md Prop 1.2 (Fiber Dimension, "Stratified Morse Analysis"); boundary stratum.

**Verdict:** **Unconditional H-MORSE FAILS on $\partial \Sigma_m$.** Stratified Morse required.

**Repair:** Impose M-A3 strict interiority $0 < \delta_0 \leq u^*_i \leq 1 - \delta_0$.

---

## Counterexample 7 — Two identical formations with permutation symmetry ($K = 2$)

**Graph:** Any with $K = 2$ multi-formation scope.

**Configuration:** $(u^{(1)}, u^{(2)}) \in \widetilde\Sigma_M^{K_\mathrm{field}}$ with $u^{(1)} = u^{(2)}$ (two identical formations).

**Degeneracy:** Permutation $(u^{(1)} \leftrightarrow u^{(2)})$ fixes the configuration; antisymmetric tangent direction $(\delta u^{(1)}, -\delta u^{(1)})$ has trivial Hessian contribution from the off-diagonal cross-coupling.

**Source:** Multi-formation permutation symmetry (degeneracy #6).

**Verdict:** **Not in CV-1.14 scope.** CV-1.14 is single-formation $K = 1$; multi-formation Morse deferred to W7+.

**Repair:** Stay in $K = 1$ scope.

---

## Conclusion

**Unconditional H-MORSE is FALSE** — at least four classes of counterexample exist:

| # | Counterexample | Type | Canonical anchor |
|---|----------------|------|------------------|
| 1 | Cycle $C_n$ with localized minimizer | Exact zero (V5b-T-zero) | canonical.md line 1303 Cat A |
| 2 | Torus $T^d$ with localized minimizer | $d$-dim Morse-Bott | canonical.md Theorem 1 line 1406 |
| 3 | $D_4$-centered minimizer on grid | Morse-Bott (doubly degenerate) | canonical.md Theorem 1 line 1362 Cat A |
| 4 | T8-Full bifurcation threshold | Codim-1 zero | T8-Full Cat A |
| 5 | Reflection-symmetric on $P_n$ | Conditional fine-tuning | Theorem 1 orbital |
| 6 | Boundary stratum critical point | Saturation degeneracy | Prop 1.2 stratified |
| 7 | $K = 2$ permutation symmetric | Multi-formation perm | Multi-formation |

**Corrected H-MORSE statement:**

H-MORSE must be **conditional / generic / local / quotient**. The realistic form (H-MORSE-Local) imposes:

- (M-A1) canonical parameter window **strictly off** the T8-Full bifurcation locus → excludes #4
- (M-A2) trivial automorphism stabilizer $G_u = \{e\}$ → excludes #3 (and #5 in symmetric cases)
- (M-A3) strict interiority $0 < \delta_0 \leq u^* \leq 1 - \delta_0$ → excludes #6
- **Implicit**: non-translation-invariant graph (canonical 15×15 free-BC) → excludes #1 and #2
- **Scope**: single-formation $K = 1$ → excludes #7

Under these assumptions, the closure-correction gap (canonical.md line 1139 Cat A) plus orbital decomposition (canonical.md Theorem 1 Cat A) yields positive definite projected Hessian.

**This is the recommended CV-1.14 target.** See `02_H_MORSE_statement_reconstruction.md §8 Path A` and `08_candidate_lemma_chain.md Path B`.
