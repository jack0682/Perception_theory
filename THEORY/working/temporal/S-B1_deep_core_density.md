---
id: S-B1-v1
type: working/proof
status: Cat B conditional (W7-FINAL, 2026-05-10) — unconditional Cat A open (OP-SB1-DEEP)
created: 2026-05-10
session: W7-FINAL
scope: ρ_deep ≥ 0.84 deep-core density lower bound for T-Temporal-Identity (b,d)
predecessor: temporal_identity_sharp_form_2026-05-07.md §5 (0.84 used in Δ_sep* formula)
target: NQ-T-Identity-2 — iso-ratio / deep-core density S-B1
---

> [!nav] Linked: [[MOC_temporal_audit_W7]] · [[MOC_Q5_temporal_identity]] · [[THEORY_INDEX]]


# S-B1: Deep-Core Density Lower Bound (ρ_deep ≥ 0.84)

**Working proof file. W7-FINAL session, 2026-05-10.**

Goal: Prove or delimit the claim $\rho_\mathrm{deep} \geq 0.84$ for canonical SCC single-formation minimizers.

---

## 0. What is ρ_deep?

### 0.1 Definition (reconstructed from temporal identity sharp form)

From `temporal_identity_sharp_form_2026-05-07.md §5` and Lemma 2:

**$m_i^{t,\mathrm{deep}}$** = mass of the "deep core" of component $C_i^t$:
$$m_i^{t,\mathrm{deep}} = \sum_{x \in C_i^t : d_G(x, \partial C_i^t) \geq \delta_\mathrm{deep}} u_t(x)$$
where $\delta_\mathrm{deep} \geq 2$ is the deep-core depth (default: 2).

**$\rho_\mathrm{deep}$** = deep-core mass fraction:
$$\rho_\mathrm{deep} = \frac{m_i^{t,\mathrm{deep}}}{m_i^t} = \frac{\sum_{x \in C_i^t : d_G(x,\partial C_i^t) \geq 2} u_t(x)}{\sum_{x \in C_i^t} u_t(x)}.$$

### 0.2 Role in T-Temporal-Identity

From the $\Delta_\mathrm{sep}^*$ formula at default parameters:
$$\Delta_\mathrm{sep}^* \geq 1.0 \cdot (\rho_\mathrm{deep} \cdot (1-\eta_\mathrm{self}^K) - \eta_\mathrm{cross}^\mathrm{sharp}) - \lambda_c/\lambda_m \cdot \bar c_\mathrm{intra}$$
$$\geq 1.0 \cdot (0.84 \cdot 0.99976 - 1.2\times10^{-4}) - 0.005 \cdot 0.54 \approx 0.837.$$

For $\Delta_\mathrm{sep}^* > 0$ (required for T-Temporal-Identity (b) uniqueness), we need:
$$\rho_\mathrm{deep} > \frac{\eta_\mathrm{cross}^\mathrm{sharp} + \lambda_c/\lambda_m \cdot \bar c_\mathrm{intra}}{1-\eta_\mathrm{self}^K}.$$

At default parameters, this threshold is approximately $0.84$.

### 0.3 Relationship to canonical theorems

$\rho_\mathrm{deep} \geq 0.84$ enters through Lemma 2 (diagonal mass lower bound):
$$\gamma_{i,\pi(i)} \geq (1-\eta_\mathrm{self}^K) m_i^{t,\mathrm{deep}} = (1-\eta_\mathrm{self}^K) \rho_\mathrm{deep} m_i^t.$$

T-Persist-1(e) (canonical Cat A) bounds $\eta_\mathrm{self}^K$. S-B1 bounds $\rho_\mathrm{deep}$ itself.

---

## 1. Route Audit

### Route 1: Variational lower bound via phase transition

**Idea:** T8-Core (non-uniform minimizer, canonical Cat A) establishes that single-formation minimizers have a phase transition: in the interior, $u(x) \approx 1$; on the boundary, $u(x)$ drops from $\approx 1$ to $\approx 0$ over a narrow transition layer. The deep core is the region where $u(x)$ has not yet dropped.

**Setup:** Let $\hat{u}$ be a single-formation minimizer with mass $m$. Define:
- $\text{Core} = \{x : \hat{u}(x) \geq \theta_\mathrm{core}\}$ (default $\theta_\mathrm{core} = 0.7$)
- $\text{Core}^2 = \{x \in \text{Core} : d_G(x, \partial\text{Core}) \geq 2\}$ (deep core)
- $m^\mathrm{deep} = \sum_{x \in \text{Core}^2} \hat{u}(x)$, $m = \sum_{x \in \text{Core}} \hat{u}(x)$

**From T-Persist-1(e) §T-Persist-1(e) deep core statement (canonical Cat A):**
- The interior gap: for $x \in \text{Core}^2$, $\hat{u}(x) \geq \theta_\mathrm{core} + g_\mathrm{int}(x)$ where $g_\mathrm{int}(x) > 0$ by the Interior Gap Lower Bound.
- The boundary layer: $|\partial\text{Core}| \leq |\{x : d_G(x, \partial\text{Core}) = 1\}|$ — the "thin shell" of one-step boundary nodes.

**Deep-core mass decomposition:**
$$m = m^\mathrm{deep} + m^\mathrm{boundary}$$
where $m^\mathrm{boundary} = \sum_{x \in \text{Core} \setminus \text{Core}^2} \hat{u}(x)$.

**Boundary mass bound:**
Since $\hat{u}(x) \leq 1$ for all $x$: $m^\mathrm{boundary} \leq |\partial_2\text{Core}|$ where $\partial_2\text{Core} = \text{Core} \setminus \text{Core}^2$ (the two-step boundary layer).

For a convex set of size $m$ on a 2D grid: $|\partial_2\text{Core}| \leq 2\sqrt{2\pi m}$ (discrete isoperimetric: boundary layer $\approx 2 \times$ perimeter width).

Actually, from T-Persist-1(e) "Boundary thinness": $\text{Core} \setminus \text{Core}^{\delta \geq 2} = \partial\text{Core}$ (one-step boundary). So $|\partial_2\text{Core}\lvert = \rvert\partial_1\text{Core}|$ (one-step boundary nodes).

For a disk-like core of area $m$ on 2D grid: perimeter $\approx 2\sqrt{\pi m}$, so $|\partial_1\text{Core}| \approx 2\sqrt{\pi m}$.

**Ratio bound:**
$$\rho_\mathrm{deep} \geq 1 - \frac{m^\mathrm{boundary}}{m} \geq 1 - \frac{|\partial_1\text{Core}|}{m \cdot \theta_\mathrm{core}/1} \geq 1 - \frac{2\sqrt{\pi m}}{m \cdot \theta_\mathrm{core}} = 1 - \frac{2\sqrt{\pi}}{\sqrt{m} \cdot \theta_\mathrm{core}}.$$

For $\rho_\mathrm{deep} \geq 0.84$: need $\frac{2\sqrt{\pi}}{\sqrt{m} \cdot 0.7} \leq 0.16$, i.e., $\sqrt{m} \geq \frac{2\sqrt{\pi}}{0.7 \cdot 0.16} \approx \frac{3.54}{0.112} \approx 31.6$, i.e., $m \geq 1000$.

**Problem:** On the canonical 15×15 grid (225 nodes), a single-formation core typically has $m = 50$–$150$ nodes. With $m = 100$: $\rho_\mathrm{deep} \geq 1 - 2\sqrt{\pi}/(\sqrt{100} \cdot 0.7) \approx 1 - 3.54/(7) \approx 1 - 0.506 = 0.494$ — far below 0.84.

**Conclusion Route 1:** The global geometric bound via isoperimetric inequality is too weak for small grids. Does NOT yield $\rho_\mathrm{deep} \geq 0.84$ on canonical grids. Route 1 FAILS for the unconditional bound.

---

### Route 2: Phase transition + exponential interior saturation

**Improved idea:** T8-Core + T-Persist-1(e) give exponential interior saturation. In the sharp-interface regime ($\beta \gg \alpha$):
$$\hat{u}(x) \approx 1 - C_\mathrm{int} \cdot e^{-\sqrt{\beta/(2\alpha)} \cdot d_G(x, \partial\text{Core})}$$

for $x$ deep inside the core (distance $d \geq 1$). So deep-core sites have $\hat{u}(x) \approx 1$.

Boundary sites: $\hat{u}(x)$ varies from $\theta_\mathrm{core} \approx 0.7$ to $\approx 1$ over 1–2 steps.

**Deep-core mass:**
$$m^\mathrm{deep} = \sum_{x \in \text{Core}^2} \hat{u}(x) \approx |\text{Core}^2| \cdot (1 - \epsilon_\mathrm{int})$$

where $\epsilon_\mathrm{int} \approx C_\mathrm{int} e^{-2\sqrt{\beta/(2\alpha)}} \ll 1$ at default parameters ($\beta \gg \alpha$).

**Boundary mass:**
$$m^\mathrm{boundary} = \sum_{x \in \partial_1\text{Core}} \hat{u}(x) \approx |\partial_1\text{Core}| \cdot \bar u_\partial$$

where $\bar u_\partial \in [\theta_\mathrm{core}, 1]$ is the average cohesion on the boundary ring.

**Ratio:**
$$\rho_\mathrm{deep} \approx \frac{|\text{Core}^2|}{|\text{Core}|} \cdot \frac{1 - \epsilon_\mathrm{int}}{1} \approx 1 - \frac{|\partial_1\text{Core}\lvert }{ \rvert\text{Core}|}.$$

The $\rho_\mathrm{deep}$ depends purely on the geometric ratio $|\partial_1\text{Core}\lvert / \rvert\text{Core}|$. For typical SCC formations on 15×15 grid, we need this ratio $\leq 0.16$ (for $\rho_\mathrm{deep} \geq 0.84$).

**For a circular core of radius $r$ on 2D grid:**
- $|\text{Core}| = \pi r^2$ (approximately)
- $|\partial_1\text{Core}| \approx 2\pi r$ (boundary ring of width 1)
- Ratio: $|\partial_1\text{Core}\lvert / \rvert\text{Core}| \approx 2/r$

For ratio $\leq 0.16$: need $r \geq 12.5$, i.e., core area $\geq \pi \cdot 12.5^2 \approx 491$ nodes.

The canonical 15×15 grid has 225 nodes total. A single-formation with mass $m \approx 0.5 \times 225 = 112$ nodes in the core would have $r \approx 6$, giving ratio $\approx 0.33$, hence $\rho_\mathrm{deep} \approx 0.67$ — well below 0.84.

**Problem:** Even with exponential interior saturation, the geometric constraint prevents $\rho_\mathrm{deep} \geq 0.84$ on small grids. Route 2 FAILS for unconditional bound on canonical 15×15 grid.

---

### Route 3: Reinterpretation — ρ_deep as transport self-concentration

**Alternative hypothesis:** $\rho_\mathrm{deep}$ in the $\Delta_\mathrm{sep}^*$ formula might refer NOT to the geometric deep-core fraction, but to the transport self-concentration fraction (T-Persist-1(e)):
$$\rho_\mathrm{deep}^{\mathrm{transport}} = 1 - n \cdot e^{-(\gamma\Delta_\varphi^2(\delta \geq 2) - \mathrm{diam}^2/\sigma^2)/\varepsilon_\mathrm{OT}}.$$

At default parameters: $n=225$, $\gamma=1$, $\Delta_\varphi^2(2) \approx 2.44$, $\varepsilon_\mathrm{OT}=0.1$, $\mathrm{diam}^2/\sigma^2 = 2$:
$$\rho_\mathrm{deep}^{\mathrm{transport}} = 1 - 225 \cdot e^{-(2.44-2)/0.1} = 1 - 225 \cdot e^{-4.4} \approx 1 - 225 \cdot 0.0123 \approx 1 - 2.77 \approx \text{negative?}$$

Hmm, let me recalculate: $e^{-4.4} \approx 0.0123$, $225 \times 0.0123 = 2.77$. This gives $\rho_\mathrm{deep}^{\mathrm{transport}} < 0$ — but T-Persist-1(e) gives $\sum_{y \in \text{Core}_s} M(x,y) / \sum_y M(x,y) \geq 1 - n \cdot e^{-...}$, which can be negative only if the bound is vacuous (the true fraction is bounded below by 0).

At $\varepsilon_\mathrm{OT} = 0.01$ (sharp regime):
$$\rho_\mathrm{deep}^{\mathrm{transport}} = 1 - 225 \cdot e^{-(2.44-2)/0.01} = 1 - 225 \cdot e^{-44} \approx 1 - \text{negligible} \approx 1.0$$

So the transport deep-core concentration is ~1.0 at the canonical sharp-OT regime, NOT 0.84.

**Conclusion:** The 0.84 value in the $\Delta_\mathrm{sep}^*$ formula is NOT the transport concentration. It is used in a different context.

---

### Route 4: Diagonal bound formula reconstruction

Looking at the Lemma 2 formula more carefully: $\gamma_{i,\pi(i)} \geq (1-\eta_\mathrm{self}^K) m_i^{t,\mathrm{deep}}$.

The normalized score: $\tilde S_{ii}^0 / (\lambda_m/\min(m_i^t,m_i^s)) \geq (1-\eta_\mathrm{self}^K) \rho_\mathrm{deep}$.

The formula $\Delta_\mathrm{sep}^* \geq 0.837$ with $\rho_\mathrm{deep} = 0.84$, $\eta_\mathrm{self}^K = 2.4 \times 10^{-4}$ comes from the sharp-form analysis.

**The value 0.84 is a NUMERICAL OBSERVATION from exp83 Scenario A** at $\varepsilon_\mathrm{OT} \in$ sharp regime, not an analytical lower bound from first principles.

This is confirmed by the Cat B status of Lemma 2 in the lemma table: Lemma 2 is "Cat B" precisely because it uses the unproven $\rho_\mathrm{deep} \geq 0.84$ as an empirical input.

---

### Route 5: Conditional theorem under HWF (well-formedness) assumptions

**Hypothesis HWF-1 (Deep-core non-degenerate):** Core $C_i^t$ has isoperimetric ratio $|\partial_1 C_i^t| / \lvert C_i^t \rvert \leq 0.16$ (a "round enough" formation).

**Hypothesis HWF-2 (Interior saturation):** For all $x \in C_i^t$ with $d_G(x, \partial C_i^t) \geq 2$: $u_t(x) \geq 0.90$.

**Hypothesis HWF-3 (Boundary regularity):** For $x \in \partial_1 C_i^t$: $u_t(x) \geq \theta_\mathrm{core} = 0.70$.

**Under HWF-1, HWF-2, HWF-3:**
$$m_i^{t,\mathrm{deep}} = \sum_{x \in C_i^t : d \geq 2} u_t(x) \geq 0.90 \cdot |\text{Core}^2| = 0.90 \cdot (\lvert C_i^t \rvert - |\partial_1 C_i^t|)$$
$$\geq 0.90 \cdot \lvert C_i^t \rvert \cdot (1 - 0.16) = 0.90 \cdot 0.84 \cdot \lvert C_i^t \rvert.$$

$$m_i^t = \sum_{x \in C_i^t} u_t(x) \leq 1 \cdot \lvert C_i^t \rvert.$$

$$\rho_\mathrm{deep} \geq \frac{0.90 \cdot 0.84 \cdot \lvert C_i^t \rvert}{\lvert C_i^t \rvert} = 0.756.$$

Hmm, this gives 0.756, below the 0.84 target. We need sharper bounds.

**Refined under HWF-1,2:**
$$\rho_\mathrm{deep} = \frac{m_i^{t,\mathrm{deep}}}{m_i^t} \geq \frac{0.90 (1 - 0.16) \lvert C_i^t \rvert}{1.0 \cdot \lvert C_i^t \rvert} = 0.756.$$

For $\rho_\mathrm{deep} \geq 0.84$, we need interior saturation $\geq 1.0$ (i.e., $u(x) = 1$ in deep core) and boundary fraction $\leq 0.16$:
$$\rho_\mathrm{deep} = \frac{\lvert C_i^t \rvert - |\partial_1 C_i^t|}{\lvert C_i^t \rvert} \geq 1 - 0.16 = 0.84.$$

So $\rho_\mathrm{deep} \geq 0.84$ **exactly when HWF-1 holds** ($|\partial_1 C_i^t|/\lvert C_i^t \rvert \leq 0.16$) AND deep-core values are $u(x) = 1$ (phase-transition regime).

**Theorem S-B1 (Cat B conditional).** *Under:*
- **(HWF-1)** $|\partial_1 C_i^t| / \lvert C_i^t \rvert \leq 0.16$ (isoperimetric ratio bound),
- **(HWF-2')** $u_t(x) \geq 0.99$ for all $x \in C_i^t$ with $d_G(x, \partial C_i^t) \geq 2$ (near-unit interior),
- **(HWF-3')** Standard SCC well-formedness: $\beta > 7\alpha$, $m_i^t \geq 25$ (from canonical T-Persist-1(d) Cat C + T8-Core):

$$\rho_\mathrm{deep}(C_i^t) \geq (1 - 0.16) \cdot 0.99 / 1.0 \approx 0.831.$$

*With HWF-1 strengthened to $|\partial_1 C_i^t| / \lvert C_i^t \rvert \leq 0.155$ and near-unit interior $u \geq 0.99$: $\rho_\mathrm{deep} \geq 0.84$.*

**Status: Cat B conditional** under HWF-1 (tightened) + HWF-2' + standard SCC well-formedness.

---

### Route 6: Experimental certification

**exp83 Scenario A** (continuation scenario): measures $\rho_\mathrm{deep}$ directly at $\varepsilon_\mathrm{OT} \in \{0.01, 0.05, 0.1, 0.3\}$.

From `temporal_identity_sharp_form_2026-05-07.md §5`: exp83 measurement $\Delta_\mathrm{sep} \approx 0.726$ at $\varepsilon_\mathrm{OT} = 1$ (outside (A7') by factor 2.2). The formula uses $\rho_\mathrm{deep} = 0.84$ to derive $\Delta_\mathrm{sep}^* = 0.837$.

**Numerical certification from exp83 ALL PASSED (4/4 scenarios, Session X 2026-05-06):**
The fact that $\Delta_\mathrm{sep} \approx 0.726 > 0$ at $\varepsilon_\mathrm{OT}=1$ implies $\rho_\mathrm{deep}$ is effectively ≥ the analytically computed threshold. This is **Cat C numerical support** for $\rho_\mathrm{deep} \geq 0.84$ at default parameters.

**Cat C route result:** $\rho_\mathrm{deep} \geq 0.84$ is empirically observed in exp83 at canonical parameters.

---

### Route 7: Counterexample search

**Attempt:** Can we construct a legal SCC formation satisfying canonical assumptions but with $\rho_\mathrm{deep} < 0.84$?

**Construction:** Take a thin elongated formation (high aspect ratio). On a 15×15 grid, a 2×10 rectangular core has $\lvert C \rvert = 20$, $|\partial_1 C| = 18$ (almost all boundary!), $\rho_\mathrm{deep} \approx 2/20 = 0.10$.

But is a 2×10 rectangle a legal SCC single-formation minimizer? With SCC separation energy, thin elongated formations are penalized — the separation energy $\mathcal{E}_\mathrm{sep}$ favors compact round formations. The canonical SCC minimizer is "disk-like" by the morphological constraint $\mathcal{Q}_\mathrm{morph}$.

**However:** If $\mathcal{Q}_\mathrm{morph}$ is NOT enforced as a hard constraint (only as a diagnostic), then elongated formations CAN be SCC minimizers in special parameter regimes.

**Conclusion:** Elongated formations CAN violate $\rho_\mathrm{deep} \geq 0.84$. Therefore the 0.84 threshold REQUIRES additional shape assumptions (not derivable from canonical axioms alone).

---

## 2. Final Classification

**Theorem S-B1 (Cat B conditional).** $\rho_\mathrm{deep}(C_i^t) \geq 0.84$ holds under:
1. **HWF-1:** $|\partial_1 C_i^t|/\lvert C_i^t \rvert \leq 0.155$ (round formation, isoperimetric bound)
2. **HWF-2':** Near-unit interior: $u_t(x) \geq 0.99$ for $x$ in deep core
3. **SCC well-formedness:** $\beta > 7\alpha$ (canonical H3 condition, T-Persist-1(d) Cat C), core size ≥ 25

**Status:** Cat B — HWF-1 is the critical assumption; analytically holds for canonical disk-like formations but not for arbitrary SCC minimizers.

**Open problem OP-SB1-DEEP:** Prove HWF-1 unconditionally from canonical SCC axioms, OR prove that canonical SCC energy minimizers satisfy HWF-1 with probability 1 under any natural randomness model.

**Cat C certification:** $\rho_\mathrm{deep} \geq 0.84$ empirically observed in exp83 at canonical parameters (4/4 scenarios PASSED).

---

## 3. Impact on T-Temporal-Identity

**T-Temporal-Identity (b) and (d):** Require $\rho_\mathrm{deep} \geq 0.84$ for Cat A promotion.

- Under S-B1 Cat B (HWF-1-3): T-Temporal-Identity (b,d) status remains Cat B (dependencies not all Cat A)
- Under S-B1 Cat A (OP-SB1-DEEP resolved): T-Temporal-Identity (b,d) → Cat A after S-A1-A3

**T-Temporal-Identity (a) and (c):** Do NOT depend on $\rho_\mathrm{deep}$.

---

## 4. Open Problem Registration

**OP-SB1-DEEP:** Deep-core density lower bound $\rho_\mathrm{deep} \geq 0.84$ unconditionally.

- **Statement:** For all canonical SCC single-formation minimizers $\hat{u}$ on a finite graph $G$ with formation $C$ satisfying canonical assumptions (A1)–(A7) of T-Temporal-Identity, the deep-core mass fraction satisfies $\rho_\mathrm{deep} \geq 0.84$.
- **Evidence:** exp83 numerical support (Cat C). Counterexample possible for elongated formations.
- **Resolution mechanism:** Either (a) prove HWF-1 from canonical SCC variational structure; (b) restrict to round-formation canonical sub-class; (c) weaken the threshold to $\rho_\mathrm{deep} \geq \rho_\mathrm{min}$ with an analytically computable $\rho_\mathrm{min}$ derived from the canonical energy.
- **Estimated:** ~1 session (NQ-T-Identity-2).
- **Severity (revised W7-CV113):** LOW (no longer blocking T-Temporal-Identity Cat A — see §5).

---

## 5. W7-CV113 Correction — Positivity Threshold vs Observed Value

**Registered: W7-CV113, 2026-05-10. See `CV113_S-B1_DEEP_CORE_CLOSURE.md` for full audit.**

### 5.1 Error in §0.2

§0.2 above states: *"At default parameters, this threshold is approximately 0.84."*

**This is incorrect.** The threshold $\rho_*$ for $\Delta_\mathrm{sep} > 0$ is:
$$\rho_* = \frac{\eta_\mathrm{cross}^\mathrm{sharp} + \frac{\lambda_c}{\lambda_m} \bar c_\mathrm{intra}}{1 - \eta_\mathrm{self}^K} = \frac{1.2\times10^{-4} + 0.005 \times 0.54}{0.99976} \approx 0.00282.$$

The value $0.84$ in the formula is the **observed** $\rho_\mathrm{deep}$ from exp83, used to compute the magnitude $\Delta_\mathrm{sep}^* \approx 0.837$ — not the positivity threshold.

### 5.2 New result: Lemma S-B1-Weak (Cat A)

**Lemma S-B1-Weak (Cat A).** Under canonical SCC single-formation assumptions with $\lvert C_i^t \rvert \geq 25$ and $\beta > 7\alpha$:
$$\rho_\mathrm{deep}(C_i^t) \geq \frac{\theta_\mathrm{core}}{n} = \frac{0.7}{225} \approx 0.00311 > \rho_*.$$

*Proof.* H2' (deep core non-emptiness, proved via Γ-convergence + DMP, Theorem 1 CORE-DEPTH-ISOPERIMETRIC.md) gives $|\mathrm{Core}^2| \geq 1$. For any $x^* \in \mathrm{Core}^2$: $u(x^*) \geq \theta_\mathrm{core} = 0.7$, so $m^\mathrm{deep} \geq 0.7$. Since $m \leq \lvert C_i^t \rvert \leq n = 225$: $\rho_\mathrm{deep} \geq 0.7/225 > \rho_*$. ∎

**Corollary (Cat A):** $\Delta_\mathrm{sep} > 0$ under canonical assumptions. Therefore T-Temporal-Identity (b,d) Cat A is NOT blocked by ρ_deep ≥ 0.84. Remaining blockers: S-A1, S-A3.

### 5.3 Revised OP-SB1-DEEP status

**OP-SB1-DEEP** (ρ_deep ≥ 0.84 unconditional) is downgraded to **non-blocking quantitative refinement**. The blocking concern was based on the erroneous threshold identification. Now registered as low-priority Cat B conditional (HWF-1–3), relevant only for numerical magnitude claims.

---

## 6. W7-CV113A Symbolic Reframing — `ρ_sym` Identity

**Registered: W7-CV113A, 2026-05-10. Working file: `SYMBOLIC_DEEP_CORE_NECESSITY.md`.
Provenance audit: `TRACE_084_ORIGIN.md`.**

### 6.1 The literal 0.84 is retracted as a standalone claim

Per W7-CV113A audit (`TRACE_084_ORIGIN.md`), the literal `ρ_deep ≥ 0.84` is **not** an independent
empirical observation — it is the value of the symbolic expression
$$\rho_\mathrm{sym}(C_\mathrm{iso}, m, \theta_\mathrm{core}) := \theta_\mathrm{core}\!\left(1 - \frac{4\,C_\mathrm{iso}}{\sqrt{m}}\right)$$
at the canonical sharp-interface parameter triple $(C_\mathrm{iso}, m, \theta_\mathrm{core}) = (0.2, 25, \sim\!1.0)$:
$$\rho_\mathrm{sym}(0.2, 25, 1.0) = 1.0 \times (1 - 0.8/5) = 0.84.$$

### 6.2 New canonical statement: Theorem S-B1-SYM (Cat B)

Under canonical SCC single-formation assumptions with $m = |\mathrm{Core}| \geq 25$,
$\beta > 7\alpha$ (H2' applies), and HWF-1 ($\mathrm{iso\_ratio}(\mathrm{Core}) \leq C_\mathrm{iso}$):
$$\rho_\mathrm{deep} \geq \theta_\mathrm{core}\!\left(1 - \frac{4\,C_\mathrm{iso}}{\sqrt{m}}\right).$$
Proof: Theorem 2b (Deep Core Dominance, Cat A) + pointwise core lower bound
+ trivial total mass upper bound. See `SYMBOLIC_DEEP_CORE_NECESSITY.md §2`.

Cat B is inherited from HWF-1 (iso_ratio bound not derivable from (A1)–(A7) alone;
counterexample: 3×10 rectangle, $\rho_\mathrm{deep} \approx 0.27$).

### 6.3 Three-tier numerical evaluation

| Regime | C_iso | m | θ_core | ρ_sym |
|--------|-------|---|--------|-------|
| Default canonical | 0.155 | 25 | 0.7 | **0.613** |
| HWF-2' tight interior | 0.155 | 25 | 0.99 | **0.867** |
| Sharp interface | 0.2 | 25 | ~1.0 | **0.840** ← recovers literal |

### 6.4 Historical sections §0–§5

§0.2, §1 Route 5, and §2 Final Classification are **superseded** by S-B1-SYM.
The sections remain in this file as historical record of the W7-FINAL / W7-CV113 derivation chain.
The canonical claim is now **S-B1-SYM** (`theorem_status.md` row `Lemma S-B1-SYM`, Cat B).

### 6.5 New open problem: OP-SB1-084

Determine the smallest provable $C_\mathrm{iso}$ on canonical 15×15 such that
$\rho_\mathrm{sym}(C_\mathrm{iso}, \bar{m}, \bar{\theta}_\mathrm{core}) = 0.84$. Severity LOW.
See `SYMBOLIC_DEEP_CORE_NECESSITY.md §6` and `theorem_status.md` row `OP-SB1-084`.

### 6.6 Status of OP-SB1-DEEP

OP-SB1-DEEP (W7-FINAL) and its W7-CV113 downgrade are **superseded** by OP-SB1-084 +
the Cat B structural status of S-B1-SYM. The original "ρ_deep ≥ 0.84 unconditional" framing
is closed: it would require deriving HWF-1 from (A1)–(A7), which is precisely OP-SB1-084(a).
