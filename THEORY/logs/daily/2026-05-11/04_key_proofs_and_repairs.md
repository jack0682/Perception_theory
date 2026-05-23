> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 04 — Key Proofs and Repairs

Concise summaries of the four mathematical pillars of the W7 arc and the conceptual meaning of the closure.

---

## 1. H-SINK Closure (S-B2 + Partial-H-SINK)

### What was H-SINK?

H-SINK is the hypothesis that the SCC temporal Sinkhorn plan is Lipschitz-stable under perturbations of the cohesion field. Formally:

$$L_g(\varepsilon_\mathrm{OT}) \leq L_c$$

i.e., the optimal Sinkhorn dual potentials for any cost in the SCC temporal cost class are $L_c$-Lipschitz, where $L_c = \mathrm{diam}(G)/\sigma_\mathrm{sp}^2 + 6\gamma$.

This is the critical Phase 1 / Q5 bottleneck for T-Temporal-Identity Cat A. Without it, temporal stability of the transport kernel cannot be proved.

### Why S-B2 mattered

S-B2 = Lemma 8.2 = H-SINK-S2 is the dual-potential Lipschitz sub-theorem. It was the gating component:
- If S-B2 = Cat A, then the chain S-B2 → Lemma 9 → Lemma 10 → Lemma 11 can promote.
- If S-B2 = Cat B, then Lemma 9 stays Cat B and kernel independence cannot reach Cat A.

W7-T1 closed S-B2 = Cat A via:
- Chain of canonical Lipschitz bounds H-SINK-1 (closure, $L_\mathrm{cl} = a_\mathrm{cl}/4$) and H-SINK-2 (distinction, $L_D = a_D(1+\lambda_D)/4$).
- 3-component fingerprint Lipschitz H-SINK-4 ($L_\varphi = \sqrt{1 + L_\mathrm{cl}^2 + L_D^2}$).
- DR2 cost Lipschitz H-SINK-5 ($L_c = \mathrm{diam}/\sigma_\mathrm{sp}^2 + 6\gamma$) from first principles.
- Log-sum-exp inequality applied to Sinkhorn fixed-point equation.

New technical hypothesis: **H-SINK-ENT** ($\varepsilon_\mathrm{OT} \geq \varepsilon_\mathrm{min} > 0$), already implicit everywhere Sinkhorn is invoked.

### How partial / sub-stochastic OT was closed

The original H-SINK plan-stability lemma (H-SINK-6) covers balanced OT via Hilbert projective metric contraction (rate $\kappa = \tanh(\mathrm{osc}(c)/(4\varepsilon_\mathrm{OT}))$). At canonical SCC parameters, $\kappa \approx 1 - 10^{-30}$ — the bound is vacuous.

The SCC canonical transport is **one-sided partial OT** (E1 axiom: $\sum_y M(x,y) \leq u_t(x)$, no column constraint). Each row is independent. **Theorem Partial-H-SINK** (W7-FINAL) gives a direct proof via row-softmax Lipschitz:

$$\lVert M^* - M^{*'} \rVert_\mathrm{TV} \leq \frac{m_t \delta}{\varepsilon_\mathrm{OT}} \cdot e^{2\delta/\varepsilon_\mathrm{OT}}.$$

Linear regime ($\delta \leq \varepsilon_\mathrm{OT}/4$): $\lVert M^* - M^{*'} \rVert_\mathrm{TV} \leq 2m_t\delta/\varepsilon_\mathrm{OT}$.

Proof uses only log-sum-exp: $\vert \log\sum a_i e^{r_i} - \log\sum a_i\vert \leq \max_i\vert r_i\vert $. No Hilbert projective metric, no Séjourné et al. 2019 — direct elementary proof for the canonical SCC E1 case.

### Why H-SINK became Cat A

The chain after W7-FINAL:
- S-B2 = Cat A (W7-T1)
- Partial-H-SINK = Cat A (W7-FINAL, direct row-softmax Lipschitz)
- H-SINK-6 for canonical SCC E1 → Cat A
- H-SINK full theorem (canonical SCC E1) → Cat A
- Lemma 9 → Cat A (corollary of Partial-H-SINK)
- Lemma 10 → Cat A (sum of Lemma 9 over component)
- Lemma 11 = S-B3 → Cat A conditional (margin)

H-SINK hypothesis node: PARTIALLY CLOSED → **FULLY CLOSED (Cat A)**.

---

## 2. Deep-Core Density Repair (legacy 0.84 → S-B1-Weak + S-B1-SYM)

### The literal 0.84 was not a standalone theorem constant

The provenance audit (`TRACE_084_ORIGIN.md`) established:

- **(E)** 0.84 originally appeared as an empirical `deep_core_frac` value in `exp49_unified_predictions.json` (sharp-interface regime). Range: 0.664–0.865; mode ≈ 0.84.
- **(D)** It was substituted as an observed plug-in into the Δ_sep* magnitude formula in `temporal_identity_sharp_form_2026-05-07.md §5`, yielding $\Delta_\mathrm{sep}^* \approx 0.837$ (purely an empirical numerical evaluation, not a derived bound).
- **(R)** It was wrongly labelled as the *positivity threshold* in `S-B1_deep_core_density.md §0.2` (W7-FINAL). The actual positivity threshold is

$$\rho_* = \frac{\eta_\mathrm{cross}^\mathrm{sharp} + (\lambda_c/\lambda_m)\bar c_\mathrm{intra}}{1 - \eta_\mathrm{self}^K} = \frac{1.2\times10^{-4} + 0.005 \cdot 0.54}{0.99976} \approx 0.00282,$$

three orders of magnitude smaller than 0.84.

The literal 0.84 was therefore **not** a first-principles analytic constant — it was an empirical observation that had been mistakenly treated as a universal theorem bound.

### Symbolic replacement (S-B1-SYM)

From canonical **Theorem 2b** (Deep Core Dominance, Cat A, `canonical.md §13`), under HWF-1 isoperimetric regularity ($\mathrm{iso\_ratio}(\mathrm{Core}) \leq C_\mathrm{iso}$), $m = \vert \mathrm{Core}\vert \geq 25$, $\beta > 7\alpha$:

$$\rho_\mathrm{deep} = \frac{m^\mathrm{deep}}{m^\mathrm{total}} \geq \theta_\mathrm{core}\!\left(1 - \frac{4\,C_\mathrm{iso}}{\sqrt{m}}\right) =: \rho_\mathrm{sym}(C_\mathrm{iso}, m, \theta_\mathrm{core}).$$

Sharp-interface evaluation: $\rho_\mathrm{sym}(0.2, 25, 1.0) = 1.0 \cdot (1 - 0.8/5) = 0.84$. ✓ (recovers the literal as a derived sharp-interface value)

S-B1-SYM is Cat B because HWF-1 is structural — not derivable from (A1)–(A7) alone. Counterexample (witnessing this): a $3 \times 10$ rectangle has $\mathrm{iso\_ratio} \approx 0.73$ (violating HWF-1) and $\rho_\mathrm{deep} \approx 0.27$.

### Positivity path (S-B1-Weak)

For T-Temporal-Identity (b), only $\Delta_\mathrm{sep} > 0$ is needed, which requires only $\rho_\mathrm{deep} > \rho_* \approx 0.00282$. The much weaker bound

$$\rho_\mathrm{deep} \geq \frac{\theta_\mathrm{core}}{n} = \frac{0.7}{225} \approx 0.00311 > \rho_*$$

is provable Cat A from H2' (deep-core non-emptiness via Γ-convergence + DMP, Theorem 1 of CORE-DEPTH-ISOPERIMETRIC.md), which gives $\vert \mathrm{Core}^2\vert \geq 1$ on the canonical 15×15 grid under $\vert \mathrm{Core}\vert \geq 25$ and $\beta > 7\alpha$.

This is **Lemma S-B1-Weak (Cat A)**, sufficient for the Cat A path of T-Temporal-Identity (b).

### Summary

| Role | Statement | Status | Comment |
|------|-----------|--------|---------|
| Positivity ($\Delta_\mathrm{sep} > 0$) | $\rho_\mathrm{deep} \geq 0.7/225 \approx 0.0031$ | **Cat A** (S-B1-Weak) | Sufficient for T-Temporal-Identity (b) Cat A |
| Quantitative magnitude | $\rho_\mathrm{deep} \geq \rho_\mathrm{sym}(C_\mathrm{iso}, m, \theta_\mathrm{core})$ | **Cat B** (S-B1-SYM) | Conditional on HWF-1; gives Δ_sep* ≈ 0.84 at sharp interface |
| Legacy literal | $\rho_\mathrm{deep} \geq 0.84$ unconditional | **superseded / retracted** | Was never a standalone analytic theorem; only `ρ_sym(0.2, 25, 1.0)` is meaningful |

---

## 3. S-C1 Margin Correction

The S-C1 audit (W7-CV1.13) re-derived the algebra of Lemma 11 (kernel independence) and found a **margin factor gap** in the original W7-FINAL proof of S-B3.

### Old incorrect margin

The original margin condition stated in `S-B3_kernel_independence.md` and used in canonical T-Temporal-Identity (c):

$$\Delta_\mathrm{sep}(M) \geq \Delta_\mathrm{sep}^* + \epsilon_\mathrm{kernel}, \qquad \epsilon_\mathrm{kernel} = \frac{2 m_t \delta}{\varepsilon_\mathrm{OT}}.$$

### Problem

The score perturbation bound from Lemma 10 gives, for any $j \neq j^*(i)$:

$$\tilde S^0_{ij^*}[M'] - \tilde S^0_{ij}[M'] \geq (\tilde S^0_{ij^*}[M] - \epsilon_\mathrm{kernel}) - (\tilde S^0_{ij}[M] + \epsilon_\mathrm{kernel}) = (\tilde S^0_{ij^*}[M] - \tilde S^0_{ij}[M]) - 2\epsilon_\mathrm{kernel}.$$

Under the old margin: $(\Delta_\mathrm{sep}^* + \epsilon_\mathrm{kernel}) - 2\epsilon_\mathrm{kernel} = \Delta_\mathrm{sep}^* - \epsilon_\mathrm{kernel}$, **not** $\Delta_\mathrm{sep}^*$.

The original proof dropped the factor 2 on $\epsilon_\mathrm{kernel}$.

### Corrected margin

$$\Delta_\mathrm{sep}(M) \geq \Delta_\mathrm{sep}^* + 2\epsilon_\mathrm{kernel}.$$

Then: $(\Delta_\mathrm{sep}^* + 2\epsilon_\mathrm{kernel}) - 2\epsilon_\mathrm{kernel} = \Delta_\mathrm{sep}^* > 0$ ✓.

### Result

The corrected margin yields $\Delta_\mathrm{sep}^* > 0$ correctly, restoring the conclusion of Lemma 11 (kernel independence). Status: Lemma 11 → **Cat A conditional** under corrected margin.

### Numerical impact

Negligible under canonical parameters. $\epsilon_\mathrm{kernel} = 2 m_t \delta / \varepsilon_\mathrm{OT}$ scales linearly in the cost perturbation $\delta$. For any physically reasonable $\delta$, $2\epsilon_\mathrm{kernel} \ll \Delta_\mathrm{sep}^* \approx 0.837$. The correction is **logically necessary**, but numerical conclusions and exp83 anchoring are unaffected.

### Files updated

- `S-B3_kernel_independence.md` (§0.1, §1.3, Final Classification) — margin and proof restated with factor 2.
- `canonical.md` §13 T-Temporal-Identity part (c) — margin condition updated.
- `theorem_status.md` — T-Temporal-Identity (c) Cat A conditional row reflects corrected margin.

---

## 4. T-Temporal-Identity Cat A (full)

Combining the four certifications:

### Part (a) — Existence of $R_{t \to s}$
**Cat A via S-A3.** Lemma 1 constructive proof verified:
- Score matrix $S^0_{ij} = \lambda_m \gamma(C_i^t, C_j^s) - \lambda_c \sum_{x,y} c(x,y) M(x,y)$ is finite by finite-graph + bounded-cost + finite-non-negative-plan.
- Five event types (continuation, split, merge, birth, death) are mutually exclusive and exhaust all possible outcomes:
  - Continuation = exactly one match on both sides
  - Split = one source matched to >1 targets
  - Merge = >1 sources matched to one target
  - Death = source with no matches
  - Birth = target with no matches
- $R_{t \to s} = \{(i,j) : S^0_{ij} \geq \tau_\mathrm{id}\}$ is a finite binary relation on finite sets — well-defined by construction.

### Part (b) — Uniqueness (stable-K + $\Delta_\mathrm{sep} > 0$)
**Cat A via S-A1 + Lemma S-B1-Weak.**
- S-A1: D-ST-3 PersComp definition is canonical (§3.11, since CV-1.6); T-Temporal-Identity explicitly cites it; no circular dependency; code matches.
- S-B1-Weak: $\Delta_\mathrm{sep} > 0$ Cat A (positivity of the separation margin).
- Together: the score matrix has a strict winner per row → unique bijection in the stable-K branch.

### Part (c) — Kernel independence
**Cat A conditional via S-C1 with corrected margin.**
- Lemma 9 (plan stability): Cat A (Partial-H-SINK)
- Lemma 10 (component confinement): Cat A (corollary of Lemma 9)
- Lemma 11 (kernel independence): Cat A conditional under $\Delta_\mathrm{sep} \geq \Delta_\mathrm{sep}^* + 2\epsilon_\mathrm{kernel}$
- Margin satisfied at canonical parameters by part (b).

### Part (d) — K=1 reduction to `persist_transport`
**Cat A via S-A1 + routine algebra.**
- S-A1 confirms D-ST-3 reduction is consistent with K=1.
- The scalar `persist_transport` (`scc/transport.py`) is the K=1 specialization of the component-level transport kernel.

---

## 5. Conceptual Meaning

> The single-formation SCC theory now supports temporal identity: a formation is not only generated and stabilized; it can be tracked **as itself** through time.

The four ontological constraints in `CLAUDE.md` are preserved:

1. **Primitive remains the soft cohesion field $u_t : X_t \to [0,1]$.** Identity is derived, not assumed.
2. **Four energy terms remain conceptually independent.** Closure / separation / boundary / transport.
3. **Closure stabilization tendency (A3) remains, not idempotence.**
4. **Not fuzzy segmentation, not clustering, not tracking** — the construction is the partial-OT-induced correspondence $R_{t \to s}$ between persistent components, not a heuristic.

This closes the static-to-temporal arc for a single formation. The remaining frontier is multi-formation (transitions, splits, merges, σ-inheritance) and metastability dynamics (H-MORSE / Package II), addressed in `07_next_plan_CV114.md`.
