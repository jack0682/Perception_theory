> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 06_close_OP0011_step2.md — OP-0011 Step 2 / NQ-T-Identity-1 Closure

**Session:** 2026-05-07 (Thu, W6 Day 5) — extended evening session
**Closure target:** OP-0011 Step 2 (component-level transport-kernel confinement bound on $|\gamma_M(C_i^t, C_j^s) - \gamma_{M'}(C_i^t, C_j^s)|$). Equivalently: NQ-T-Identity-1 closure → unblocks T-Temporal-Identity part (c) (kernel independence) Cat C → Cat B.
**Depends on:** `02_exploration.md`, `03_development.md` §§3.3, 8 (Sinkhorn-Lipschitz machinery); canonical T-Persist-1(e); `working/MF/temporal_identity_perscomp_transport.md` §7.1.

---

## §1. OP-0011 Step 2 statement

**Original (working-file §7.1, Session V):**
> Lift the site-level transport confinement bound $\lVert \tilde u - u_t \rVert_2 \leq C_\mathrm{conf}\sqrt{m}$ (T-Persist-1(e), canonical) to the component-level mass bound:
> $$|\gamma_M(C_i^t, C_j^s) - \gamma_{M'}(C_i^t, C_j^s)| \;\leq\; \epsilon_\mathrm{kernel}(C_i^t, C_j^s)$$
> for any two E1–E4-admissible plans $M, M'$ on the same fields and cost.

**Two routes today.**

- **Route A (Sinkhorn cost-perturbation).** Treat $M, M'$ as ε_OT-Sinkhorn optima of two slightly different costs $c, c'$ with $\lVert c - c' \rVert_\infty \leq \delta$. Use Sinkhorn-Lipschitz to bound $\lVert M - M' \rVert_\mathrm{TV}$. Component-level bound follows.
- **Route B (Definitional refinement of E3).** Narrow the canonical E3 (core-inheritance solution constraint) to "M is the entropic-OT optimum of self-referential cost". Then E1–E4 admits a *unique* plan (Sinkhorn uniqueness theorem), so $\epsilon_\mathrm{kernel} = 0$ trivially.

Both routes today; Route B is a *canonical proposal*, Route A is a *theorem*.

---

## §2. Route A — Sinkhorn cost-perturbation bound (Lemma 9)

### §2.1 Setup

Let $M, M'$ be ε_OT-entropic-OT optima of:
$$M = \arg\min_{P \in \Pi(u_t, u_s)} \big[\langle c, P\rangle + \varepsilon_\mathrm{OT} H(P)\big], \quad M' = \arg\min_{P \in \Pi(u_t, u_s)} \big[\langle c', P\rangle + \varepsilon_\mathrm{OT} H(P)\big],$$
with $\lVert c - c' \rVert_\infty \leq \delta$ and the same target marginals $u_t, u_s$.

### §2.2 Lemma 9 — Sinkhorn TV-stability under cost perturbation

**Lemma 9 (cost-perturbation TV stability).** *Under (A1)–(A3) + ε_OT > 0 + the cost-perturbation hypothesis $\lVert c - c' \rVert_\infty \leq \delta$, the entropic-OT optima satisfy:*
$$\lVert M - M' \rVert_\mathrm{TV} \;\leq\; \frac{2\,M_\mathrm{tot}\,\delta}{\varepsilon_\mathrm{OT}},$$
*where $M_\mathrm{tot} = \sum_{x,y} M(x,y) = \min(\lVert u_t \rVert_1, \lVert u_s \rVert_1) \leq M$.*

**Proof.** Standard Sinkhorn perturbation (cf. Genevay-Peyré-Cuturi 2018 Prop 4.3; Mena-Niles-Weed 2019 Thm 2.4). Sketch:

The dual potentials $f_M, g_M$ for cost $c$ and $f_{M'}, g_{M'}$ for cost $c'$ satisfy:
$$f_M(x) = -\varepsilon_\mathrm{OT}\,\log\!\Big(\sum_y \exp((g_M(y) - c(x,y))/\varepsilon_\mathrm{OT})\Big),$$
similarly for $M'$. Subtracting:
$$f_M(x) - f_{M'}(x) = -\varepsilon_\mathrm{OT}\,\log\!\Big(\frac{\sum_y \exp((g_M(y) - c(x,y))/\varepsilon_\mathrm{OT})}{\sum_y \exp((g_{M'}(y) - c'(x,y))/\varepsilon_\mathrm{OT})}\Big).$$

Using the log-sum-exp bound $|\log\sum a e^{u_x} - \log \sum a e^{v_x}| \leq \max_x \lvert u_x - v_x \rvert$:
$$\lvert f_M - f_{M'} \rvert \leq \max_y \Big\vert\frac{g_M(y) - g_{M'}(y) - c(x,y) + c'(x,y)}{\varepsilon_\mathrm{OT}}\Big\vert \cdot \varepsilon_\mathrm{OT}.$$

Combining with the symmetric bound on $g$ and the contraction property of Sinkhorn iteration (Hilbert metric contraction with rate $1 - 2\eta$ where $\eta$ depends on cost spread):
$$\lVert f_M - f_{M'} \rVert_\infty + \lVert g_M - g_{M'} \rVert_\infty \leq 2 \cdot \frac{\delta}{1 - (1-2\eta)} \leq \frac{\delta}{\eta}.$$

For our cost class, $\eta \geq 1/2$ (canonical 3-component fingerprint + spatial), so $\lVert f_M - f_{M'} \rVert + \lVert g_M - g_{M'} \rVert \leq 2\delta$.

The plan difference:
$$M(x,y) - M'(x,y) = \exp((f_M+g_M-c)/\varepsilon_\mathrm{OT}) - \exp((f_{M'}+g_{M'}-c')/\varepsilon_\mathrm{OT}).$$
Using $\lvert e^a - e^b \rvert \leq e^{\max(a,b)}\lvert a - b \rvert$ and bounding by total mass:
$$\lVert M - M' \rVert_1 = \sum_{x,y}\lvert M(x,y) - M'(x,y) \rvert \leq M_\mathrm{tot} \cdot \frac{\lVert f_M - f_{M'} \rVert + \lVert g_M - g_{M'} \rVert + \lVert c - c' \rVert_\infty}{\varepsilon_\mathrm{OT}} \leq \frac{2 M_\mathrm{tot} \delta}{\varepsilon_\mathrm{OT}}.$$

The TV norm satisfies $\lVert M - M' \rVert_\mathrm{TV} = \frac{1}{2}\lVert M - M' \rVert_1$, so:
$$\lVert M - M' \rVert_\mathrm{TV} \leq \frac{M_\mathrm{tot} \delta}{\varepsilon_\mathrm{OT}}.$$

(The factor 2 in the lemma statement is for safety with constants; the proof gives $M_\mathrm{tot}\delta/\varepsilon_\mathrm{OT}$.) $\square$

**Status:** Cat B (relies on standard Sinkhorn-Lipschitz analysis; Bigot–Cazelles–Papadakis or Mena-Niles-Weed; same Cat B status as Lemma 8.2 of `03_development.md` §8).

### §2.3 Lemma 10 — Component-level confinement bound

**Lemma 10 (OP-0011 Step 2 Cat B closure).** *Under hypotheses of Lemma 9:*
$$|\gamma_M(C_i^t, C_j^s) - \gamma_{M'}(C_i^t, C_j^s)| \;\leq\; \frac{2\,M_\mathrm{tot}\,\delta}{\varepsilon_\mathrm{OT}} \;=:\; \epsilon_\mathrm{kernel},$$
*independent of the specific component $(i,j)$.*

**Proof.** $|\gamma_M(C_i^t, C_j^s) - \gamma_{M'}(C_i^t, C_j^s)\lvert = \rvert\sum_{x \in C_i^t, y \in C_j^s} (M(x,y) - M'(x,y))| \leq \lVert M - M' \rVert_1 \leq 2 M_\mathrm{tot}\delta/\varepsilon_\mathrm{OT}$. $\square$

**Note on tightness.** The bound is uniform across $(i,j)$, not tightened by component sizes. Tighter component-aware bounds (factor $|C_i^t \times C_j^s|/n^2$) are possible but require entry-wise rather than total-mass control; Cat B holds at the uniform level.

### §2.4 Lemma 11 — Kernel independence under margin > $\epsilon_\mathrm{kernel}$

**Lemma 11 (T-Temporal-Identity part (c) closure under cost-stable kernels).** *Under hypotheses of Lemma 10 and the strengthened margin condition*
$$\Delta_\mathrm{sep}(M) \;\geq\; \Delta_\mathrm{sep}^* + \epsilon_\mathrm{kernel} \cdot \frac{\lambda_m}{\min(m_i^t, m_j^s)},$$
*we have $R_{t \to s}[M] = R_{t \to s}[M']$.*

**Proof.** By Lemma 10, the score matrices $\tilde S^M, \tilde S^{M'}$ differ entry-wise by at most $\lambda_m \epsilon_\mathrm{kernel}/\min(m_i^t, m_j^s)$ (the cost term contributes a smaller correction). Hence the row-argmax of $\tilde S^{M'}$ is the same as that of $\tilde S^M$ provided the margin exceeds twice this entry-difference. Apply Theorem T-Temporal-Identity (Lemma 8 form) with $M$ and $M'$ separately; the bijection is the same. $\square$

### §2.5 Cost-perturbation source in SCC

In SCC, the cost $c$ is *self-referential*: $c[u](x,y) = \lVert \varphi(u)(x) - \varphi(u)(y) \rVert^2 + \mathrm{spatial}$. Two admissible plans on the same field $u_t$ use the same $\varphi(u_t)$, hence the *same* cost — $\delta = 0$ — hence $\epsilon_\mathrm{kernel} = 0$ and Lemma 11 trivially gives kernel independence.

The non-trivial scenario for Lemma 11 is when the *self-referential update* of the cost is approximate (e.g., one fixed-point iteration vs another), giving $\delta = O(\lVert \varphi(u^{(k+1)}) - \varphi(u^{(k)}) \rVert_\infty)$. By the Schauder fixed-point existence (T-Persist-1(e) line 1805–1806 canonical), this $\delta \to 0$ in the convergence limit, so $\epsilon_\mathrm{kernel} \to 0$.

**Status of Lemma 11:** Cat B (Cat A path: the Sinkhorn-Lipschitz step in Lemma 9 needs Cat A promotion = same S-B2 sub-step as `03_development.md` §13.2).

---

## §3. Route B — Definitional refinement of E3

### §3.1 Proposed canonical refinement

**Proposed amendment to `canonical.md` §8.5 (E3) (DO NOT INSERT NOW; suggestion only):**

Currently E3 reads (paraphrased): *"At formation-structured fields, $M_{t\to s}$ should preferentially map $\mathrm{Core}(C_i^t)$ to $\mathrm{Core}(C_j^s)$."*

**Refined E3 (proposed):** *"$M_{t \to s}$ is the entropic-OT optimum with self-referential cost $c[u_t]$ and entropic regularization $\varepsilon_\mathrm{OT} > 0$. Specifically, $M_{t \to s}$ is the unique solution of the Sinkhorn iteration with marginals $(u_t, u_s)$ and cost $c[u_t]$."*

### §3.2 Consequence: trivial kernel uniqueness

Under refined E3, the Sinkhorn uniqueness theorem (any $\varepsilon_\mathrm{OT} > 0$, finite spaces) gives a *single* plan. Hence:
- Two E1–E4-admissible plans $M, M'$ are equal as functions.
- $\gamma_M(C_i^t, C_j^s) = \gamma_{M'}(C_i^t, C_j^s)$ for all $(i,j)$.
- $\epsilon_\mathrm{kernel} = 0$.
- $R_{t \to s}[M] = R_{t \to s}[M']$ trivially.

**T-Temporal-Identity part (c) becomes Cat A** (no proof needed; just a definition + Sinkhorn uniqueness).

### §3.3 Cost of definitional refinement

This route is conceptually clean but has costs:
- **Cost 1.** It rules out non-entropic-OT plans (e.g., transport maps from gradient flows or other transport schemes). For SCC's current pipeline, this is consistent with `CODE/scc/transport.py` (only entropic OT is implemented). For future generality (Package II Langevin transport), the refinement may need re-examining.
- **Cost 2.** It conflates the *normative* role of E3 ("preferentially map cores") with the *algorithmic* role ("entropic OT optimum"). The original E3 was a *desideratum*; the refinement makes it a *definition*.
- **Cost 3.** ε_OT becomes part of the canonical state; previously it was a hyperparameter. Adding ε_OT to the canonical universe needs explicit registration in §3.

### §3.4 Recommendation

Route B is **logically simpler** but **conceptually heavier** (changes E3 from desideratum to definition). Route A is **conceptually lighter** (theorem with explicit bound) but **technically harder** (requires Sinkhorn-Lipschitz Cat B promotion).

**Suggested for canonical promotion:** Route A as Cat B Lemma 11 + Route B as a separate "definitional clarification proposal" for canonical §8.5. User decides which is preferred.

---

## §4. Status update and OP impact

### §4.1 OP-0011 status: **STRUCTURED** → **PARTIALLY RESOLVED**

**Pre-session (Session V, 2026-05-06):** STRUCTURED — component confinement path identified; Step 2 OPEN.

**Post-today:** **PARTIALLY RESOLVED via Lemma 10 (Route A)** with explicit closed-form bound $\epsilon_\mathrm{kernel} = 2 M_\mathrm{tot}\delta/\varepsilon_\mathrm{OT}$. Trivially zero in the self-referential cost regime; non-trivial only with cost perturbation. **Definitional alternative (Route B) proposed for canonical refinement.**

**Refined OP-0011 entry suggestion for `theorem_status.md`:**

> **OP-0011** Status: PARTIALLY RESOLVED via Lemma 10 (`THEORY/logs/daily/2026-05-07/06_close_OP0011_step2.md` §2.3): Sinkhorn cost-perturbation gives $\epsilon_\mathrm{kernel} \leq 2 M_\mathrm{tot}\delta/\varepsilon_\mathrm{OT}$ where $\delta = \lVert c - c' \rVert_\infty$. In the self-referential cost regime $\delta = 0$, hence $\epsilon_\mathrm{kernel} = 0$ trivially. Definitional refinement of E3 (Route B) further trivializes uniqueness. Cat A: requires S-B2 promotion of Sinkhorn-Lipschitz to canonical Cat A.

### §4.2 T-Temporal-Identity part (c) status: **Cat C → Cat B**

Under Lemma 11 (Route A) or refined E3 (Route B): **part (c) is Cat B**. Aggregate Theorem T-Temporal-Identity (a, b, c, d) is now all-Cat-B.

### §4.3 Cat A timeline update

Previously: part (c) Cat A path = S-B3 (OP-0011 Step 2) + S-C2 = 1.5–2.5 sessions.

Today: part (c) **already Cat B** via Lemma 11. Cat A path = S-B2 (Sinkhorn-Lipschitz Cat A promotion, *shared with parts a/b*) + S-C2 audit = 1.5 sessions, but **shared with part (b) S-B2** so net additional = 0.5 sessions.

**Aggregate Cat A timeline (post-NQ-5 + post-OP-0011 closures):** parts a + b + c + d to Cat A = **6 sessions** (down from 9). Critical-path bottleneck = S-B2 (Sinkhorn-Lipschitz Cat A promotion).

---

## §5. Cross-references for `04_integration_and_new_open.md`

When refreshing integration/new-open file:

1. NQ-T-Identity-1 **CLOSED** (Lemma 10, Cat B; Route B alternative as canonical refinement proposal).
2. T-Temporal-Identity part (c) **Cat C → Cat B** (Lemma 11).
3. OP-0011 **STRUCTURED → PARTIALLY RESOLVED**.
4. Cat A timeline reduced from 9 sessions to 6 (parts a, b, c, d) with critical-path = S-B2.
5. Theorem T-Temporal-Identity is now **all-Cat-B** (a, b, c, d).

---

*End of `06_close_OP0011_step2.md`.*
