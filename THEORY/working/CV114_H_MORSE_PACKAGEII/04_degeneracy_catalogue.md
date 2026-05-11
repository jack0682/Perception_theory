# 04 — Degeneracy Catalogue

Agent B (Mathematical Analyst). Fourteen classes of potential Morse degeneracy for the SCC energy on $\Sigma_m$. For each: description, source, structural vs removable, blocks H-MORSE?, repair option.

---

## Catalogue

### 1. Volume constraint zero mode

**Description:** The direction $\mathbf 1 \in \mathbb R^n$ is in the kernel of the projection $\Pi_T$. Any second-order variation along $\mathbf 1$ violates $\sum u_i = m$.

**Source:** The constraint $\mathbf 1^T u = m$ itself.

**Structural? Removable?:** Structural for full-space Hessian; **removed automatically by tangent projection**.

**Blocks H-MORSE?** No — H-MORSE is defined on $T_{u^*}\Sigma_m = \mathbf 1^\perp$, where this mode is excluded.

**Repair:** Always use the projected Hessian $\Pi_T H \Pi_T$. The "zero" in the un-projected Hessian is a coordinate artifact, not a Morse degeneracy.

---

### 2. Constant direction removed by tangent projection

**Description:** Same as #1 from a different angle. The constant vector $\mathbf 1$ is the 0-eigenvector of $\Pi_T$; on $T_{u^*}\Sigma_m$ it has been excised.

**Source:** Lagrange multiplier formalism on $\Sigma_m$.

**Structural? Removable?:** Coordinate.

**Blocks H-MORSE?** No.

**Repair:** Tangent projection.

---

### 3. Graph automorphism symmetry

**Description:** If $\sigma \in \mathrm{Aut}(G)$ fixes $u^*$ as a function on vertices ($u^* \circ \sigma = u^*$), then any tangent direction in the kernel of $(I - \sigma_*)$ produces a degenerate Hessian block via Schur's lemma applied to the orbital decomposition.

**Source:** Maschke's theorem + canonical.md Theorem 1 (orbital, Cat A).

**Structural? Removable?:** Structural for symmetric minimizers; **removable by working only at symmetry-broken minimizers** (stabilizer $= \{e\}$).

**Blocks H-MORSE?** Yes for symmetric minimizers; no for symmetry-broken.

**Repair:** Either (a) impose M-A2 (stabilizer trivial), or (b) apply orbital quotient — work on $H^\mathrm{proj} / G_u$ and prove block-Morse.

---

### 4. Translation-like near-zero modes on grids

**Description:** On translation-invariant graphs (cycle $C_n$, torus $T^d$), discrete translation $\mathbb Z_L^d$ acts on configurations; a localized blob has orbit of translates. Sub-spinodal: exact zero eigenvalue (V5b-T-zero, Cat A). Super-lattice: $\mu_\mathrm{Gold} \propto e^{-c_d/\xi_0}$ (V5b-T-b Cat A, exponentially small).

**Source:** canonical.md line 1264–1303.

**Structural? Removable?:** Structural; **removable** by working on graphs without translation symmetry (e.g., free boundary 15×15 grid with $D_4$ but not translation invariance).

**Blocks H-MORSE?** Yes for $T^d$ / $C_n$; no for $D_4$-symmetric grids with broken translation.

**Repair:** Restrict canonical scope to free-BC grids (already implicit canonical 15×15 setting). For torus, use orbital quotient or generic perturbation.

---

### 5. Multiple equivalent blob positions

**Description:** Even on $D_4$-symmetric grids, a non-center-located single-blob minimizer has a $D_4$-orbit of 8 (or 4 for axis-aligned) equienergetic translates. Each orbit element has stabilizer $\{e\}$ or $\mathbb Z_2$ but the orbit is structural.

**Source:** $D_4$ action on the grid.

**Structural? Removable?:** Structural at the orbit level; **at each orbit point, the stabilizer is small** (often $\{e\}$).

**Blocks H-MORSE?** No, at the single orbit point — M-A2 still holds locally.

**Repair:** Work locally near a single chosen representative. The orbit gives multiplicity but not local degeneracy.

---

### 6. Formation permutation symmetry for $K > 1$

**Description:** For multi-formation $\widetilde\Sigma_M^{K_\mathrm{field}}$, swapping formation labels $u^{(j)} \leftrightarrow u^{(k)}$ is an exact symmetry of the energy. Gives a permutation orbit of $K!$ equivalent configurations.

**Source:** Multi-formation ontology, canonical §3.x.

**Structural? Removable?:** Structural for $K > 1$.

**Blocks H-MORSE?** Yes for multi-formation; **not applicable to single-formation $K = 1$ scope of CV-1.14**.

**Repair:** Restrict CV-1.14 H-MORSE to $K = 1$ (single-formation), deferring multi-formation Morse to NQ-248 / W7+ (canonical.md line 1322).

---

### 7. Boundary strata of $[0,1]^n \cap \Sigma_m$

**Description:** Critical points on $\partial \Sigma_m$ have active inequality constraints $u_i = 0$ or $u_i = 1$. Stratified Morse (Goresky-MacPherson) applies; ordinary Morse formulas do not.

**Source:** $\Sigma_m$ is polytope with corners.

**Structural? Removable?:** Structural; **deferrable** by restricting to $\Sigma_m^\circ$ (strict interior).

**Blocks H-MORSE?** Only if minimizer reaches boundary. Canonical T-PreObj-1 minimizers in spinodal interior are strictly interior under typical parameters.

**Repair:** Add (M-A3) strict interiority assumption; defer boundary stratum to Option B (canonical.md §11.1, NQ-248 W7+).

---

### 8. Saturation at $u = 0$ or $u = 1$

**Description:** Sigmoid-driven energy components ($\mathcal E_\mathrm{cl}$, $\mathcal E_\mathrm{sep}$) have flat regions near $u = 0$ and $u = 1$ where the sigmoid Jacobian $\sigma'(\cdot) \to 0$. Hessian contribution from these components vanishes.

**Source:** Operator definitions canonical.md §9.2.

**Structural? Removable?:** Structural near boundary; **removable** by strict interiority M-A3.

**Blocks H-MORSE?** Only at near-saturated configurations. The boundary energy $\mathcal E_\mathrm{bd}$ still contributes (the $4\alpha L$ term is non-zero), so partial Morse is retained.

**Repair:** Either (a) impose M-A3 with explicit $\delta_0 > 0$ bound, or (b) extend EK formula to handle near-saturated saddles (Bovier extension).

---

### 9. Closure fixed-point degeneracy

**Description:** When $u = \mathrm{Cl}(u)$ (closure fixed point), the closure residual $r = 0$ and the contribution $(I - J_\mathrm{Cl})^T (I - J_\mathrm{Cl})$ to the Hessian is in canonical position but the second-order terms vanish.

**Source:** A3 stabilization tendency (canonical.md §10).

**Structural? Removable?:** Structural; the closure-correction gap (canonical.md line 1139, Cat A) still gives a positive contribution because $J_\mathrm{Cl}$ has spectral norm $< 1$ under $a_\mathrm{cl} < 4$.

**Blocks H-MORSE?** No — the closure-correction gap is precisely the proof that closure fixed-point minimizers are Morse-stable in the constrained direction. This is the **key positive ingredient** for H-MORSE-Local.

**Repair:** None needed; this is in fact the friend, not the foe.

---

### 10. Separation operator flat regions

**Description:** $\mathcal E_\mathrm{sep}$ depends on the distinction operator $D(u)$, which is sigmoid-based. In the "all-cohered" or "all-distinct" extremes, $\partial \mathcal E_\mathrm{sep} / \partial u \to 0$ and Hessian contribution vanishes.

**Source:** Sigmoid-based distinction operator.

**Structural? Removable?:** Structural at parameter extremes; in the canonical $K = 1$ formation with mixed interior/boundary, separation Hessian contributes positively in the spinodal-interior regime.

**Blocks H-MORSE?** Only in degenerate parameter regimes (e.g., $\lambda_\mathrm{sep} = 0$).

**Repair:** Canonical parameter window keeps $\lambda_\mathrm{sep} > 0$ and avoids extremes.

---

### 11. Resolvent co-belonging spectral margin

**Description:** The resolvent $C_u = (I - \alpha_C W_\mathrm{sym}(u))^{-1}$ becomes singular when $\alpha_C \rho(W_\mathrm{sym}) \to 1$. Although the 4-component fingerprint was demoted (W7-T1 H-SINK audit), residual references to $C_u$ in some Hessian terms could carry spectral degeneracy.

**Source:** Resolvent canonical.md §9.4.

**Structural? Removable?:** Removable — the canonical 3-component fingerprint excludes $C_u$ from Hessian-critical quantities. Canonical SCC energy components ($\mathcal E_\mathrm{cl}, \mathcal E_\mathrm{sep}, \mathcal E_\mathrm{bd}$) use 3-component formulation.

**Blocks H-MORSE?** No — assuming canonical 3-component fingerprint (H-SINK-4, Cat A).

**Repair:** Verify canonical energy components in `scc/energy.py` use 3-component formulation; do not invoke 4-component resolvent variant.

---

### 12. Shared-pool vs K-field ontology mismatch

**Description:** $\widetilde\Sigma_M^{K_\mathrm{field}}$ (K-field shared-pool) and $\Sigma_m$ (single-formation) differ in the index structure. Multi-formation $K \geq 2$ on $\widetilde\Sigma$ has additional permutation symmetry (degeneracy #6) and shared-pool resource constraints not present on $\Sigma_m$.

**Source:** canonical.md §3.x, §11.1 Commitment 16.

**Structural? Removable?:** Structural; **avoided** by single-formation $K = 1$ scope.

**Blocks H-MORSE?** No — CV-1.14 single-formation scope.

**Repair:** Defer multi-formation Morse on $\widetilde\Sigma_M^{K_\mathrm{field}}$ to NQ-248 / W7+ (canonical.md line 1322).

---

### 13. Gauge-like λ-space degeneracy

**Description:** The parameter tuple $(\lambda_\mathrm{cl}, \lambda_\mathrm{sep}, \lambda_\mathrm{bd})$ has a one-dimensional rescaling redundancy: $\mathcal E$ and $c \mathcal E$ have the same critical points. Hessian eigenvalues scale linearly in $c$ but their signs and ratios are preserved.

**Source:** Energy normalization convention.

**Structural? Removable?:** Removable by fixing a normalization (e.g., $\lambda_\mathrm{bd} = 1$).

**Blocks H-MORSE?** No — Morse nondegeneracy is invariant under global rescaling.

**Repair:** Use canonical normalization $\lambda_\mathrm{bd} = 1$ (or whatever convention `params.py` enforces).

---

### 14. Numerical degeneracy vs analytic degeneracy

**Description:** Numerical Hessian eigenvalue computation has finite precision; "near-zero" eigenvalues ($|\mu| < 10^{-8}$) may be either analytically zero (structural) or analytically positive but numerically too small to distinguish. The hypothesis_tree numerical claim "$\mu_\mathrm{min} \in [0.96, 60.2]$" sits above numerical noise but is finite-grid-specific.

**Source:** Finite-precision arithmetic.

**Structural? Removable?:** Numerical issue; **resolved** by combining analytic proof (Cat A closure-correction gap) with explicit lower bound formula.

**Blocks H-MORSE?** Only if the claimed positive bound is below numerical noise. H-MORSE-Local with explicit analytic $\mu_0 > 0$ formula avoids this.

**Repair:** State explicit analytic lower bound $\mu_\mathrm{min} \geq \mu_0(\lambda_\mathrm{cl}, \lambda_\mathrm{sep}, \beta, a_\mathrm{cl}, \delta_0) > 0$ rather than relying on numerical evidence.

---

## Summary table

| # | Degeneracy | Structural? | Blocks H-MORSE? | Repair |
|---|-----------|-------------|------------------|--------|
| 1 | Volume constraint zero mode | Coordinate | No | Tangent projection |
| 2 | Constant direction removed | Coordinate | No | Same |
| 3 | Graph automorphism | Structural | Yes for symmetric u* | M-A2 + orbital quotient |
| 4 | Translation-like (V5b-T-zero) | Structural | Yes for $C_n, T^d$ | Restrict to non-translation-invariant graphs |
| 5 | Multiple equivalent positions | Structural orbit | No locally | Work near a single representative |
| 6 | $K > 1$ permutation | Structural | N/A for K=1 | Defer multi-formation |
| 7 | Boundary strata | Structural | Yes at boundary | M-A3 strict interiority |
| 8 | Saturation at u=0 or u=1 | Near-boundary | Marginal | M-A3 |
| 9 | Closure fixed-point | Friendly | **NO** — gives the positive gap | None |
| 10 | Separation flat regions | Parameter regime | Only at extremes | Canonical parameter window |
| 11 | Resolvent spectral margin | Resolvable | No (3-comp fingerprint) | Use canonical fingerprint |
| 12 | Shared-pool vs K-field | K-only | N/A for K=1 | Single-formation scope |
| 13 | Gauge-like λ rescaling | Coordinate | No | Fix normalization |
| 14 | Numerical vs analytic | Numerical | Conditional | Explicit analytic lower bound |

---

## Conclusion (final part of catalogue)

### Which degeneracies must be excluded for CV-1.14?

For **H-MORSE-Local Cat B** registration at CV-1.14:

- **Must exclude (assumption):** #3 (assume M-A2 trivial stabilizer), #4 (avoid translation-invariant graphs OR add quotient), #7 (assume M-A3 strict interiority), #8 (subsumed under M-A3).
- **Must use (positive input):** #9 — the closure-correction gap is the proof's foundation.
- **Naturally avoided:** #6 (single-formation scope), #11 (canonical 3-component fingerprint), #12 (K=1 only).
- **Coordinate / non-issues:** #1, #2, #13, #14.

### Which can be handled by quotienting?

- #3 (graph automorphism) — Theorem 1 orbital decomposition Cat A handles this if M-A2 is too restrictive; one can work modulo $G_u$ and prove block-Morse on each irrep.
- #4 (translation) — similarly, on $T^d$ one can quotient by $\mathbb Z_L^d$ to a moduli space of single translates; the resulting H-MORSE-Quotient is harder but feasible.
- #5 (multiple equivalent positions) — orbit-level, not a true degeneracy.

### Which require generic perturbation?

- #3, #4 in their unconditional form: if one wants H-MORSE without quotient and without M-A2, then **a small symmetry-breaking perturbation** is required (Smale transversality). This is Path B (H-MORSE-Generic) of `08_candidate_lemma_chain.md`.

### Which are harmless for Package II?

- #5 (orbit) — Eyring-Kramers naturally aggregates over equivalent saddles by symmetry.
- #9 (closure fixed-point) — friendly.
- #13 (gauge) — invariant under scaling.
- #11 (resolvent) — outside canonical fingerprint.

### Which are gating for Package II?

- **#3, #4, #7 are gating.** They must be either excluded (M-A2/M-A3) or quotiented before Eyring-Kramers can be applied.
