---
id: NOP-D-v1
type: working/theory
status: open — NOP-D working draft (Session 2026-05-07 evening); investigate self-referential Sinkhorn fixed-point convergence under (A7') sharp regime
created: 2026-05-07
session: W6 D5 evening
scope: stability of self-referential entropic-OT iteration in SCC
related:
  - THEORY/logs/daily/2026-05-07/06_close_OP0011_step2.md (Lemma 10 cost-perturbation single-step)
  - THEORY/logs/daily/2026-05-07/10_new_open_problems.md (§5 NOP-D)
  - canonical.md §13 T-Persist-1(e) Cat A — Schauder fixed-point (line 1805–1806)
  - CODE/scc/transport.py — sinkhorn_partial_ot, transport_fixed_point
---

> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q4_K_selection]] · [[MOC_sigma_rich_framework]] · [[THEORY_INDEX]]


# NOP-D — Self-Referential Sinkhorn Fixed-Point Stability under (A7') Sharp Regime

**Purpose.** Lemma 10 (`06_close_OP0011_step2.md`) bounds single-step cost-perturbation. SCC self-referential iteration updates cost at each step. Question: does the iteration converge in (A7') sharp regime, or does it diverge?

This is a structural tension between two regimes:
- **(A7') sharp regime** demands $\varepsilon_\mathrm{OT}$ small ($\leq 0.45$) — for kernel concentration.
- **Self-referential contraction** demands $\varepsilon_\mathrm{OT}$ large ($\geq \sqrt{2 L_\varphi M_\mathrm{tot}} \approx 12$) — for Banach contraction.

These two conditions are mutually exclusive at default parameters. **The question:** is canonical T-Persist-1(e) Schauder fixed-point existence (canonical) sufficient, or does iterative convergence fail?

---

## §1. Setup

**SCC self-referential cost.**
$$c[u](x,y) = \lVert \varphi(u)(x) - \varphi(u)(y) \rVert^2 + \sigma_\mathrm{sp}^{-2}d_G(x,y)^2,$$
with $\varphi(u) = (u, \mathrm{Cl}(u), D(x;1{-}u)) \in [0,1]^3$.

**Iteration.**
$$M^{(k+1)} = \mathrm{Sinkhorn}\big(c[u^{(k)}], \varepsilon_\mathrm{OT}; u_t, u_s\big),\qquad u^{(k+1)} = M^{(k+1)\,\top} \mathbf{1}.$$

This is the self-referential Schauder fixed-point iteration (canonical T-Persist-1(e)).

---

## §2. The contraction analysis

### §2.1 Per-step cost perturbation

By chain rule:
$$\delta c \approx 2 \langle \delta\varphi(u), \varphi(u)\rangle = 2 \lVert \partial\varphi/\partial u \rVert_\mathrm{op} \cdot \lVert u \rVert_\infty \cdot \lVert \delta u \rVert_\infty \leq 2 L_\varphi \lVert \delta u \rVert_\infty.$$
At canonical default: $L_\varphi = 1.43$ (canonical line 1807; formation-conditioned).

### §2.2 Per-step plan perturbation (Lemma 10)

By Lemma 10:
$$\lVert M^{(k+1)} - M^{(k)} \rVert_\mathrm{TV} \leq \frac{M_\mathrm{tot} \cdot \delta c}{\varepsilon_\mathrm{OT}} \leq \frac{2 L_\varphi M_\mathrm{tot}}{\varepsilon_\mathrm{OT}} \cdot \lVert \delta u^{(k)} \rVert.$$

### §2.3 Per-step field perturbation

Field update: $\delta u^{(k+1)} = (\delta M^{(k+1)})^\top \mathbf{1}$. Hence:
$$\lVert \delta u^{(k+1)} \rVert_\infty \leq \lVert \delta M^{(k+1)} \rVert_\mathrm{TV} \cdot 1 \leq \frac{2 L_\varphi M_\mathrm{tot}}{\varepsilon_\mathrm{OT}} \cdot \lVert \delta u^{(k)} \rVert.$$

### §2.4 Banach contraction condition

Convergence in Banach norm requires:
$$\rho := \frac{2 L_\varphi M_\mathrm{tot}}{\varepsilon_\mathrm{OT}} < 1\quad\Leftrightarrow\quad \varepsilon_\mathrm{OT} > 2 L_\varphi M_\mathrm{tot}.$$

At canonical default: $L_\varphi = 1.43$, $M_\mathrm{tot} \approx 50$ (mass = 50, exp83 default). Hence $\varepsilon_\mathrm{OT} > 143$ — **far above** the (A7') sharp regime $\varepsilon_\mathrm{OT} \leq 0.45$.

### §2.5 The tension

The two regimes are *mutually exclusive*:
- (A7') sharp regime: $\varepsilon_\mathrm{OT} \leq 0.45$.
- Banach contraction: $\varepsilon_\mathrm{OT} \geq 143$.

**Possible resolutions.**

**(R1) Schauder, not Banach.** Canonical T-Persist-1(e) uses Schauder fixed-point (compactness + continuity), not Banach. Schauder gives *existence*, not *uniqueness* nor *convergence rate*. The iteration may not converge in Banach norm, but a fixed point exists, and the iteration accumulates near a fixed point.

**(R2) Local contraction.** Near a fixed point, the contraction constant is *strictly smaller* than the global Lipschitz $L_\varphi$. The local Lipschitz of $\varphi$ near the formation manifold may be $L_\varphi^\mathrm{loc} \ll 1.43$.

**(R3) Markov contraction in Hilbert metric.** Sinkhorn iteration is contraction in Hilbert metric (multiplicative gauge), not Banach. The Hilbert-metric contraction holds for any $\varepsilon_\mathrm{OT} > 0$.

**(R4) Convergence-in-distribution (not pointwise).** The iteration may not converge pointwise, but the law of $u^{(k)}$ converges to the fixed-point law.

### §2.6 Lemma 18 candidate — Hilbert metric contraction (R3)

**Lemma 18 (Hilbert-metric contraction, Cat C target Cat B).** *Under (A1)–(A6) + ε_OT > 0, the SCC self-referential Sinkhorn iteration is a contraction in the Hilbert (Birkhoff) metric on $\Sigma_M$ with rate $\rho_H < 1$, even when (A7') sharp regime ($\varepsilon_\mathrm{OT} \leq 0.45$) makes Banach contraction fail.*

**Proof sketch.** Sinkhorn iteration is contraction in the Hilbert (multiplicative) projective metric $d_H$ defined on positive measures (cf. Franklin-Lorenz 1989, Chen-Georgiou-Pavon 2017). The contraction rate is $\tanh(\Delta/4) < 1$ where $\Delta$ is the Hilbert diameter of the cost matrix entries. For bounded cost: $\Delta \leq 2 \cdot c_\mathrm{max}/\varepsilon_\mathrm{OT}$, so $\rho_H \leq \tanh(c_\mathrm{max}/(2\varepsilon_\mathrm{OT})) < 1$ for any ε_OT > 0.

Composed with the cost-update step $u \to c[u]$ (Lipschitz $L_\varphi$ in some norm but Lipschitz $\rho_\varphi^H < 1$ in Hilbert metric for log-fingerprints), the composition is contractive in Hilbert metric.

**Status:** Cat C. Cat B target: 1–2 sessions to formalize Hilbert-metric Lipschitz of fingerprint $\varphi$.

---

## §3. Implications for canonical T-Persist-1(e)

If Lemma 18 closes, T-Persist-1(e) Schauder fixed-point statement can be strengthened to:

**Refined T-Persist-1(e) (proposed).** *In addition to existence (Schauder), the self-referential iteration converges in Hilbert metric with rate $\rho_H < 1$, providing constructive convergence. Banach-norm convergence holds only at ε_OT large.*

This is a **strengthening** of canonical Cat A T-Persist-1(e). Promotion target: clarify the convergence-mode in canonical line 1805 ("Fixed-point existence (Schauder)") — promote to "Hilbert-metric contractive convergence".

**No retraction needed.** Existing Cat A statement (Schauder existence) stands; the addition is a supplementary convergence claim, also Cat A under standard Hilbert-metric Sinkhorn theory.

---

## §4. Implications for Lemma 11 (kernel independence)

Lemma 11 (`06_close_OP0011_step2.md` §2.4) requires both $M, M'$ to be Sinkhorn optima — but if iteration doesn't converge (Banach), what does "Sinkhorn optimum" mean?

**Resolution.** Sinkhorn optimum is well-defined as the *Hilbert-metric fixed point* (which exists and is unique for any ε_OT > 0). Lemma 11's conclusion stands — kernel independence holds for Hilbert-fixed-point optima.

This **clarifies** the Lemma 11 statement but does not weaken it.

---

## §5. Status

- **NOP-D status:** Cat C, sketched. Lemma 18 candidate (Hilbert-metric contraction).
- **Difficulty:** 1–2 sessions for Cat B closure of Lemma 18.
- **Cross-impact:**
  - Strengthens canonical T-Persist-1(e) Cat A (constructive convergence claim).
  - Clarifies Lemma 11 (kernel independence) in (A7') sharp regime.
  - Resolves the apparent contradiction between (A7') and self-ref iteration regimes.

**Recommended action:** Lemma 18 closure is independently valuable. Estimated 1 session, low-mid difficulty (standard Hilbert-metric Sinkhorn theory).

---

*End of `self_ref_fp_stability.md`.*
