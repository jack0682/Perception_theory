---
id: NOP-A-v1
type: working/theory
status: open — NOP-A working draft (Session 2026-05-07 evening); reconcile sharp form (Lemma 3-sharp) and spectral form (Lemma 13) bounds
created: 2026-05-07
session: W6 D5 evening
scope: structural reconciliation of two off-diagonal mass bounds in T-Temporal-Identity
related:
  - THEORY/logs/daily/2026-05-07/03_development.md (§8 sharp form Lemma 3-sharp)
  - THEORY/logs/daily/2026-05-07/08_NQ6_spectral_gap_advance.md (§3 spectral form Lemma 13)
  - THEORY/logs/daily/2026-05-07/10_new_open_problems.md (§2 NOP-A)
  - working/MF/temporal_identity_sharp_form_2026-05-07.md (uses both forms)
  - canonical.md §13 T-Persist-1(e) Cat A; §12 T-Persist-K-Sep
---

> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q4_K_selection]] · [[MOC_sigma_rich_framework]] · [[THEORY_INDEX]]


# NOP-A — Sharp ↔ Spectral Bound Reconciliation

**Purpose.** T-Temporal-Identity's off-diagonal mass bound has two distinct closed forms today (sharp form via Sinkhorn-Lipschitz; spectral form via joint Hessian gap). Their ε_OT-dependent ceilings differ structurally. This file establishes the reconciliation.

---

## §1. The two bounds in canonical-grade form

### Sharp form (Lemma 3-sharp; canonical-side)
$$\eta_\mathrm{cross}^\mathrm{sharp} = \exp\!\left(-\frac{\gamma_\mathrm{OT}\,\Delta_\varphi^2_\mathrm{inter} - L_g\,d_\mathrm{eff}}{\varepsilon_\mathrm{OT}}\right).$$

Vacuous when $\varepsilon_\mathrm{OT} \geq (\gamma_\mathrm{OT}\Delta_\varphi^2_\mathrm{inter}- L_g d_\mathrm{eff})/2 = \varepsilon_\mathrm{OT}^* \approx 0.45$ at default.

### Spectral form (Lemma 13 sketch)
$$\eta_\mathrm{cross}^\mathrm{spec} = \exp\!\left(-\frac{\mu_\mathrm{joint}\,(d_\mathrm{inter}^*)^2}{2\varepsilon_\mathrm{OT}}\right).$$

No ceiling — exponent grows linearly in $\mu_\mathrm{joint}\,d_\mathrm{inter}^{*\,2}$ at any $\varepsilon_\mathrm{OT}$.

---

## §2. The reconciliation question

**Question.** Are the two forms equivalent (different parametrizations of the same exponent), or genuinely distinct (one is tighter)?

**Working hypothesis.** Spectral form is *strictly tighter* than sharp form. Sharp form is a *Lipschitz-worst-case bound* derivable from spectral form by additional slack.

**Test.** Algebraic reduction: $L_g$ should be expressible in terms of $\mu_\mathrm{joint}$, $d_\mathrm{inter}^*$, and graph constants. If $L_g = O(1/\sqrt{\mu_\mathrm{joint}\,d_\mathrm{inter}^{*\,2}})$, then the sharp exponent reduces to the spectral exponent (modulo factor 2).

---

## §3. Lemma 15 — CORRECTED form (closure 2026-05-07 late-evening)

**Discovery during development (`THEORY/logs/daily/2026-05-07/12_NOP_A_lemma15_reconciliation.md`):** Both sharp and spectral forms are *conservative*. The truly tight bound uses cost-comparison + component-level union bound, with $K{-}1$ prefactor (not $n$, not $1$ with Lipschitz subtraction).

**Spectral form Lemma 13 has a scaling error** (energy cost of swap-mode is quadratic in $\eta_\mathrm{cross}$, not linear in $d_\mathrm{inter}^*$); **withdrawn** with erratum.

### §3.1 Lemma 15 (corrected, Cat B closure)

**Lemma 15 (NOP-A corrected, Cat B).** *Under (A1)–(A8)+(A7') + comparable component masses ($C_\mathrm{mass} := \max_j m_j^s/\min_j m_j^s = O(1)$):*
$$\eta_\mathrm{cross}^\mathrm{corrected} \;\leq\; C_\mathrm{mass}\,\exp\!\Big(-\frac{\Delta_\varphi^2_\mathrm{inter} + \sigma_\mathrm{sp}^{-2}\,d_\mathrm{inter}^{*\,2} - O(c_\mathrm{intra}^\mathrm{max})}{\varepsilon_\mathrm{OT}}\Big).$$

### §3.2 Proof

For source $x \in C_i^t$ and target $y$: $M^*(x, y) = u_t(x) \cdot u_s(y)\,e^{-c(x,y)/\varepsilon_\mathrm{OT}} / Z(x)$ where $Z(x) = \sum_y u_s(y)\,e^{-c(x,y)/\varepsilon_\mathrm{OT}}$.

For $y \in C_j^s$ ($j \neq \pi(i)$): $c(x, y) \geq c_\mathrm{cross}^\mathrm{min} = \Delta_\varphi^2_\mathrm{inter} + \sigma_\mathrm{sp}^{-2} d_\mathrm{inter}^{*2}$.
For $y' \in C_{\pi(i)}^s$: $c(x, y') \leq c_\mathrm{intra}^\mathrm{max}$.

$Z(x) \geq m_{\pi(i)}^s \cdot e^{-c_\mathrm{intra}^\mathrm{max}/\varepsilon_\mathrm{OT}}$. Cross-component fraction:
$$\frac{\sum_{y \in C_j^s} M^*(x,y)}{u_t(x)} \leq \frac{m_j^s\,e^{-c_\mathrm{cross}^\mathrm{min}/\varepsilon_\mathrm{OT}}}{m_{\pi(i)}^s\,e^{-c_\mathrm{intra}^\mathrm{max}/\varepsilon_\mathrm{OT}}} = \frac{m_j^s}{m_{\pi(i)}^s}\,e^{-(c_\mathrm{cross}^\mathrm{min}-c_\mathrm{intra}^\mathrm{max})/\varepsilon_\mathrm{OT}}.$$

Sum over $x \in C_i^t$, normalize by $\min(m_i^t, m_j^s)$:
$$\eta_\mathrm{cross} = \frac{\gamma(C_i^t, C_j^s)}{\min(m_i^t, m_j^s)} \leq C_\mathrm{mass}\,\exp(-\Delta_c/\varepsilon_\mathrm{OT}). \qquad \square$$

**Cat B status.** Cost-comparison only (no Sinkhorn-Lipschitz, no Hessian eigenvalue bound). Chains canonical T-Persist-1(e) Cat A.

### §3.3 Numerical comparison at default ($n=225$, $\Delta_\varphi^2_\mathrm{inter}=2.33$)

| Form | At $\varepsilon_\mathrm{OT}=0.1$ | At $\varepsilon_\mathrm{OT}=1$ | Match exp83 ($\eta\approx 0.1$ at $\varepsilon=1$)? |
|------|----------------------------------|---------------------------------|-----|
| Coarse ($n=225$) | $3 \times 10^{-8}$ | $23$ (vacuous) | No |
| Sharp ($L_g d=1.43$) | $1.2 \times 10^{-4}$ | $0.41$ | Medium |
| Spectral (incorrect, $\mu d^2 = 875$) | $\sim 0$ | $\sim 0$ | No |
| **Corrected (Lemma 15)** | $\boxed{10^{-10}}$ | $\boxed{0.10}$ | **Yes** |

### §3.4 Implications

1. **Sharp form's $L_g d_\mathrm{eff}$ subtraction is a Lipschitz-worst-case slack** — replace with cost-comparison.
2. **Spectral form's $\mu_\mathrm{joint} d_\mathrm{inter}^{*2}$ is a scaling error** — quadratic, not linear; algebraic decay, not exponential.
3. **Coarse form's $n$ prefactor reflects site-level union bound** — replace with component-level $K-1$ or $C_\mathrm{mass}$.

### §3.5 New certified regime

Lemma 15 is non-vacuous when $\Delta_c/\varepsilon_\mathrm{OT} > \log C_\mathrm{mass}$, i.e., $\varepsilon_\mathrm{OT}^* \approx \Delta_c \approx 2.29$ at default.

**This covers exp83's $\varepsilon_\mathrm{OT} = 1$.** NQ-T-Identity-4b **partially resolved**.

---

## §4. Status

- **NOP-A status:** **CLOSED Cat B via Lemma 15** (corrected form, today's late evening).
- **Impact:**
  - Cat A timeline reduced to ~3 sessions (no longer needs S-B2 Sinkhorn-Lipschitz Cat A promotion).
  - Spectral form Lemma 13 withdrawn (erratum needed in `08_NQ6_spectral_gap_advance.md`).
  - exp83 $\varepsilon_\mathrm{OT}=1$ now within certified regime.
  - T-Temporal-Identity Cat B's $\eta_\mathrm{cross}$ replaced with corrected form.
- **Cross-impacts:** NQ-T-Identity-4b PARTIALLY CLOSED. NQ-T-Identity-6 reclassified.
- **Promotion-pipeline action:** Update `temporal_identity_sharp_form_2026-05-07.md` Theorem 4.2 with Lemma 15 corrected $\eta_\mathrm{cross}$.

---

*End of `sharp_vs_spectral_2026-05-07.md`.*
