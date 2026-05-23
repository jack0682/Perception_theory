> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 07_close_NQ4_robust.md — NQ-T-Identity-4 Partial Closure (Large $\varepsilon_\mathrm{OT}$ Robustness)

**Session:** 2026-05-07 (Thu, W6 Day 5) — extended evening session
**Closure target:** NQ-T-Identity-4 partial — push the certified regime $\varepsilon_\mathrm{OT}^*$ from sharp-form value $\approx 0.45$ closer to exp83's $\varepsilon_\mathrm{OT} = 1$. The session goal is to advance the sharp form by replacing the Lipschitz-based argument with a tighter variance-corrected concentration analysis.
**Depends on:** `02_exploration.md`, `03_development.md` §§3.3, 8, 9; canonical T-Persist-1(e); standard concentration theory (Hoeffding / Bernstein).

---

## §1. NQ-T-Identity-4 statement

**NQ-T-Identity-4 (full).** Find a tighter bound on $\eta_\mathrm{cross}$ that certifies T-Temporal-Identity at $\varepsilon_\mathrm{OT} = 1$ (exp83's regime).

**Status before this file:**
- Coarse: $\varepsilon_\mathrm{OT}^* \approx 0.05$ (factor-20 gap to exp83).
- Sharp (today's `03_development.md` §8): $\varepsilon_\mathrm{OT}^* \approx 0.45$ (factor-2.2 gap).
- Goal: push closer to or past 1.

---

## §2. The bottleneck in the sharp form

The sharp form (`03_development.md` §8.3) produces:
$$\eta_\mathrm{cross}^\mathrm{sharp} = \exp\!\Big(-\frac{\gamma_\mathrm{OT}\Delta_\varphi^2_\mathrm{inter} - L_g\,d_\mathrm{eff}}{\varepsilon_\mathrm{OT}}\Big).$$

The numerator $\gamma_\mathrm{OT}\Delta_\varphi^2_\mathrm{inter} - L_g d_\mathrm{eff}$ is the *effective concentration gap*. At default parameters it's $\approx 0.9$.

**The key observation:** the Lipschitz bound $\lvert g(y) - g(y_0) \rvert \leq L_g d_G(y,y_0)$ is *worst-case*. In the actual entropic-OT optimum, $g$ is much smoother on the support — its *average* variation is much smaller than the Lipschitz constant suggests.

**Replacement strategy.** Use a *variance-corrected* bound: replace $L_g d_\mathrm{eff}$ in the exponent with $\sqrt{\mathrm{Var}_y(g)}$, the standard deviation of $g$ on the relevant support.

---

## §3. Lemma 12 — Variance bound on Sinkhorn dual potentials

**Lemma 12 (Variance-corrected dual potential).** *Under (DR1)–(DR2) + (S) (Sinkhorn-ball restriction), and additionally:*
- *(VR) The Sinkhorn dual potential $g$ has bounded variance on the support: $\mathrm{Var}_{M^*(\cdot, y)}\!(g) \leq V_g \cdot \varepsilon_\mathrm{OT}$ for some constant $V_g$ depending only on the cost regularity.*

*Then the off-diagonal mass bound improves:*
$$\eta_\mathrm{cross}^\mathrm{var} \leq \exp\!\Big(-\frac{\gamma_\mathrm{OT}\Delta_\varphi^2_\mathrm{inter} - \sqrt{2 V_g \varepsilon_\mathrm{OT}\,\mathrm{diam}(G)}}{\varepsilon_\mathrm{OT}}\Big).$$

In the variance-corrected form, the effective concentration gap scales as $\Delta_\varphi^2_\mathrm{inter} - \sqrt{V_g \varepsilon_\mathrm{OT} \mathrm{diam}}$ instead of $\Delta_\varphi^2_\mathrm{inter} - L_g d_\mathrm{eff}$. The variance term grows as $\sqrt{\varepsilon_\mathrm{OT}}$ (slower than the linear $L_g d_\mathrm{eff}$ term), giving a wider certified regime.

**Proof sketch.** The Boltzmann factor $\exp(g(y)/\varepsilon_\mathrm{OT})$ over the support of $M^*$ has effective variance bounded by $V_g$. By Hoeffding-like concentration (variance-aware Bernstein):
$$\Pr_{y \sim M^*(\cdot, y)}\big[g(y) - \mathbb{E}g \geq t\big] \leq \exp(-t^2 / (2 V_g \varepsilon_\mathrm{OT})).$$

Choosing $t = L_g d_\mathrm{eff}$ as before gives recovery of the Lipschitz bound, but in the *typical* regime the $t$ that determines effective concentration is $\sqrt{2 V_g \varepsilon_\mathrm{OT} \log(1/\eta)}$, not the worst-case Lipschitz product.

The argument analogous to Lemma 8.2 then gives, with $L_g \cdot d_\mathrm{eff}$ replaced by $\sqrt{2 V_g \varepsilon_\mathrm{OT} \mathrm{diam}}$:
$$\eta_\mathrm{cross}^\mathrm{var} \leq \exp\!\Big(-\frac{\gamma_\mathrm{OT}\Delta_\varphi^2_\mathrm{inter} - \sqrt{2 V_g \varepsilon_\mathrm{OT} \mathrm{diam}}}{\varepsilon_\mathrm{OT}}\Big). \qquad \square$$

**Status:** Cat B — relies on (VR) which is a non-trivial regularity hypothesis. Bounding $V_g$ in terms of canonical-grade quantities is the analytic step; conjecturally $V_g \leq L_c^2 \cdot \mathrm{diam}_\mathrm{cost}^2 / 4$ by Poincaré inequality on the support.

### §3.1 Quantitative comparison

At default parameters with $V_g \leq L_c^2 \cdot \mathrm{diam}^2 / 4 \leq 5.86^2 \cdot 28^2 / 4 \approx 6730$ (worst case) — too large.

Better: Poincaré-conditioned $V_g$ on the formation manifold. For deep-core × deep-core supports (small effective volume), $V_g$ can be much smaller. Empirical (T-Persist-1(e) measured: dual-potential range at deep core $\approx 0.5$) gives $V_g \approx 0.25$.

With $V_g = 0.25$ and $\mathrm{diam} = 28$, the variance term is $\sqrt{2 \cdot 0.25 \cdot \varepsilon_\mathrm{OT} \cdot 28} = \sqrt{14 \varepsilon_\mathrm{OT}}$.

$$\eta_\mathrm{cross}^\mathrm{var} \leq \exp\!\Big(-\frac{\Delta_\varphi^2_\mathrm{inter} - \sqrt{14\varepsilon_\mathrm{OT}}}{\varepsilon_\mathrm{OT}}\Big).$$

Solving $\Delta_\varphi^2_\mathrm{inter} = \sqrt{14\varepsilon_\mathrm{OT}^*}$ for $\varepsilon_\mathrm{OT}^*$ at $\Delta_\varphi^2_\mathrm{inter} = 2.33$:
$$\varepsilon_\mathrm{OT}^* \;=\; (\Delta_\varphi^2_\mathrm{inter})^2 / 14 \;=\; 5.43 / 14 \;\approx\; 0.39.$$

Hmm — *worse* than sharp form (0.45). The variance-correction loses to the Lipschitz form when $\Delta_\varphi^2_\mathrm{inter}$ is moderate.

**Reason.** The Lipschitz form has linear-in-$\varepsilon$ correction; variance form has square-root. At moderate $\varepsilon_\mathrm{OT}$ the linear is smaller. The variance form *only* dominates at *small* $\varepsilon_\mathrm{OT}$ where the variance term is square-root small.

Therefore Lemma 12 is **not the right instrument** to push $\varepsilon_\mathrm{OT}^*$ higher. The variance-correction *helps* in the deep-concentration regime but hurts in the moderate regime.

### §3.2 Combined bound (best-of-two)

**Combined sharp/variance bound.**
$$\eta_\mathrm{cross}^\mathrm{best} = \min(\eta_\mathrm{cross}^\mathrm{sharp},\, \eta_\mathrm{cross}^\mathrm{var}).$$

At small $\varepsilon_\mathrm{OT} \leq 0.1$: variance bound dominates (tighter).
At moderate $\varepsilon_\mathrm{OT} \in [0.1, 0.5]$: Lipschitz bound dominates.
At large $\varepsilon_\mathrm{OT} > 0.5$: both vacuous.

**Conclusion for NQ-T-Identity-4:** Variance correction does not push $\varepsilon_\mathrm{OT}^*$ past Lipschitz form. **Larger-$\varepsilon_\mathrm{OT}$ robustness is genuinely outside the variance-corrected and Lipschitz-corrected analytical reach.**

---

## §4. Alternative route — Empirical-robustness theorem (Cat C-grade)

If analytical sharp-form bounds cap at $\varepsilon_\mathrm{OT}^* \approx 0.45$, the gap to exp83's $\varepsilon_\mathrm{OT} = 1$ remains open analytically. We can register this as a Cat C-grade *empirical robustness theorem*.

**Theorem ER (T-Temporal-Identity Empirical Robustness, Cat C).** *Given an instance where the row+column margin condition $\Delta_\mathrm{sep}(M_{t \to s}) > 0$ is verified empirically (post-hoc on the realized plan), Theorem T-Temporal-Identity (refined Cat B form, parts a, b, d, c via Lemma 11) holds even if (A7') is violated. The bijection is determined by the realized plan, not the theoretical regime.*

**Status.** Cat C — *post-hoc robustness*. The theorem is true (since the proof of T-Temporal-Identity uses (A7') only to *guarantee* margin > 0; if margin > 0 is already verified, (A7') is unnecessary). But it does not give a *predictive* bound — only a *verificational* one.

**Use case.** exp83 measures $\Delta_\mathrm{sep} = 0.726$ at $\varepsilon_\mathrm{OT} = 1$. Apply Theorem ER: the bijection is uniquely determined. exp83 PASS validated. Cat C grade because the regime was not certified a priori.

This is the precise non-overclaim register entry from `03_development.md` §6.2 item 5, now upgraded to a named Cat C theorem.

---

## §5. Closure status

### §5.1 NQ-T-Identity-4 status: **PARTIALLY CLOSED**

**Resolution:**
- Sharp form $\varepsilon_\mathrm{OT}^* \approx 0.45$ (factor-9 improvement over coarse 0.05; factor-2.2 gap to exp83 $\varepsilon_\mathrm{OT} = 1$).
- Variance correction (Lemma 12) does NOT push $\varepsilon_\mathrm{OT}^*$ higher; useful at small ε_OT only.
- Theorem ER (Cat C empirical robustness) covers exp83 PASS as post-hoc verified bijection.

**Genuinely open:**
- Analytical certification at $\varepsilon_\mathrm{OT} \in [0.45, 1]$. Conjecturally requires *non-OT-concentration* approach — possibly NQ-T-Identity-6 spectral-gap path (which bypasses Sinkhorn-Lipschitz entirely) or a different transport framework.

### §5.2 NQ-T-Identity-4 reclassification

Reclassify NQ-T-Identity-4 as:
- **NQ-T-Identity-4a (CLOSED via sharp form §8 + Theorem ER Cat C):** $\varepsilon_\mathrm{OT} \in (0, 0.45]$ analytically certified; $\varepsilon_\mathrm{OT} \in [0.45, \infty)$ post-hoc verifiable via Theorem ER.
- **NQ-T-Identity-4b (OPEN, low priority):** analytical extension to $\varepsilon_\mathrm{OT} > 0.45$. Likely requires NQ-T-Identity-6 or alternative framework. Not a priority for the current Cat A path.

---

## §6. Cross-references for `04_integration_and_new_open.md`

When refreshing integration/new-open file:

1. NQ-T-Identity-4 **PARTIALLY CLOSED** (4a closed; 4b open low priority).
2. New: **Theorem ER** (T-Temporal-Identity Empirical Robustness, Cat C) covers exp83 PASS post-hoc.
3. Lemma 12 (variance correction) registered but does not extend $\varepsilon_\mathrm{OT}^*$ — kept as theoretical-completeness lemma.
4. Recommended exp variant: re-run exp83 at $\varepsilon_\mathrm{OT} \in \{0.01, 0.05, 0.1, 0.3, 0.45\}$ (all inside certified regime) — confirms sharp-form prediction.

---

*End of `07_close_NQ4_robust.md`.*
