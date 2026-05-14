---
id: NOP-B-v1
type: working/theory
status: open — Cat B-ready Lemma 16 (Session 2026-05-07 late evening); closes OP-0008-DIST
created: 2026-05-07
session: W6 D5 late evening
scope: σ_rich Lipschitz constant; OP-0008-DIST (Disturbance/perturbation σ-stability) closure
related:
  - THEORY/logs/daily/2026-05-07/11_NOP_B_sigma_lipschitz_development.md (full development)
  - THEORY/logs/daily/2026-05-07/10_new_open_problems.md (§3 NOP-B)
  - working/MF/sigma_rich_centroid_derivation.md
  - working/MF/sigma_rich_orientation_derivation.md
  - working/MF/multi_formation_sigma.md
  - canonical Commitment 18 candidate (σ-rich packet, NQ-242 W6+)
  - theorem_status.md OP-0008 entries
---

> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q4_K_selection]] · [[MOC_sigma_rich_framework]] · [[THEORY_INDEX]]


# σ_rich Lipschitz Constant (NOP-B / OP-0008-DIST Closure)

**Purpose.** Promotion-ready Cat B working draft of Lemma 16 — the σ_rich Lipschitz constant under field perturbation. Closes OP-0008-DIST and unblocks T-σ-Inherit Cat B (parts a, b, d-direction, e).

---

## §1. Statement

**Lemma 16 (σ_rich Lipschitz, Cat B).** *Let $C \subseteq \mathcal{P}$ be a persistent component (D-ST-3) with $|C| \geq 1$. Let $u, u' \in [0,1]^n$ be two soft cohesion fields with $u'|_{\mathcal{P}\setminus C} = u|_{\mathcal{P}\setminus C}$ (component-localized perturbation). Suppose:*

- *(MP) Mass positivity:* $m(C; u) = \sum_{x \in C} u(x) \geq m_\mathrm{min} := \rho_\mathrm{pers}\,|C|/4 > 0$.
- *(DB) Diameter bound:* $\mathrm{diam}_\mathrm{intra}(C) := \max_{x,y\in C} d_G(x,y) \leq D_C$.
- *Smallness:* $\varepsilon := \|\delta u|_C\|_2 \leq m_\mathrm{min}/(2\sqrt{|C|})$ where $\delta u = u' - u$.

*Then:*
$$\big\|\sigma_\mathrm{rich}(C; u + \delta u, P) - \sigma_\mathrm{rich}(C; u, P)\big\|_\Sigma \;\leq\; L_\sigma \cdot \varepsilon,$$
*with explicit constant:*
$$\boxed{\;L_\sigma = \sqrt{|C|}\,\Big(1 + \frac{2 D_C}{m_\mathrm{min}} + \frac{2 D_C^2}{m_\mathrm{min}}\Big) \;\approx\; \frac{2\sqrt{|C|}\,D_C^2}{m_\mathrm{min}}.\;}$$

*The σ-component product norm $\|\cdot\|_\Sigma$ is the natural product on $\mathbb{R}_{\geq 0} \times \mathbb{R}^d \times \mathrm{Sym}^+_d$ (mass, centroid, inertia tensor).*

---

## §2. Proof outline

(Full development in `THEORY/logs/daily/2026-05-07/11_NOP_B_sigma_lipschitz_development.md` §3.)

### §2.1 Mass

$|m' - m| = |\sum_C \delta u| \leq \sqrt{|C|} \varepsilon$ (Cauchy-Schwarz). Lipschitz constant: $\sqrt{|C|}$.

### §2.2 Centroid

Identity: $\bar x' - \bar x = \sum_C \delta u(x) (x - \bar x)/m'$. Cauchy-Schwarz + (DB):
$$\|\bar x' - \bar x\|_2 \leq D_C \sqrt{|C|}\,\varepsilon / m'.$$
Smallness gives $m' \geq m_\mathrm{min}/2$, so Lipschitz: $2 D_C\sqrt{|C|}/m_\mathrm{min}$.

### §2.3 Inertia

Similar with second moments. Lipschitz: $2 D_C^2 \sqrt{|C|}/m_\mathrm{min}$.

### §2.4 Combination

Product-norm Lipschitz = sum of components: $\sqrt{|C|}\,(1 + 2D_C/m_\mathrm{min} + 2D_C^2/m_\mathrm{min})$.

$\square$

---

## §3. Numerical instance

At exp83 default ($|C| \leq 25$, $D_C \leq 7$, $\rho_\mathrm{pers} = 0.5$, $m_\mathrm{min} \geq 3.125$):
$$L_\sigma \leq 5 \cdot (1 + 4.48 + 31.36) \approx 185.$$

For 1% noise ($\varepsilon = 0.01$): σ-shift bounded by $1.85$. Mass shift $\leq 0.05$, centroid shift $\leq 0.224$, inertia shift $\leq 1.568$. All small relative to natural scales.

---

## §4. Status

- Cat B (chains Cauchy-Schwarz Cat A + (MP) D-ST-3 derived + (DB) instance-verifiable).
- Cat A path: relax (PL) component-localization to general perturbations, requires NOP-E (D-ST-3 ↔ proxy phase boundary).

## §5. OP-0008-DIST closure

**OP-0008-DIST status:** OPEN → **CLOSED Cat B via Lemma 16**.

T-σ-Inherit Cat B (parts a, b, d-direction, e) now unblocked for OP-0008-DIST sub-problem.

## §6. Refinement opportunities (future work)

1. **Probabilistic refinement (Angle B5):** Talagrand concentration gives smaller average $L_\sigma \approx 30$ at default — useful for noise-robustness theorems.
2. **Spectral refinement (Angle B1):** σ_standard Lipschitz via Davis-Kahan; complementary to σ_rich.
3. **Topology-aware (Angle B3):** handle component-boundary crossings via NOP-E phase boundary lemma.

## §7. References

- `THEORY/logs/daily/2026-05-07/11_NOP_B_sigma_lipschitz_development.md` — full multi-tool development
- `THEORY/logs/daily/2026-05-07/10_new_open_problems.md` §3 — NOP-B catalog
- `working/MF/sigma_rich_centroid_derivation.md` — companion centroid derivation
- `working/MF/sigma_rich_orientation_derivation.md` — companion orientation
- `working/MF/multi_formation_sigma.md` — multi-formation σ context

---

*End of `sigma_rich_lipschitz_2026-05-07.md`. Cat B-ready for T-σ-Inherit promotion-pipeline review.*
