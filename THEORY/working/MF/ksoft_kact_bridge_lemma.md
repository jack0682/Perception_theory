# WQ-2: $K_{\mathrm{soft}}$ / $K_{\mathrm{act}}$ Bridge Lemma

**File:** `THEORY/working/MF/ksoft_kact_bridge_lemma.md`
**Document type:** Working-grade bridge-lemma analysis (non-canonical).
**Created:** 2026-05-02 (WQ-2 of layered ambient-state architecture work queue).
**Status:** working draft. Bridge lemma stated as candidate; failure modes enumerated; computational diagnostics specified; WQ-1 retry decision rule provided.

**Companion artifacts:**
- `THEORY/working/MF/layered_ambient_architecture_candidate.md` — Layer I/II/III definitions, $K_{\mathrm{soft}}^\phi$ (§6.4), $K_{\mathrm{act}}^\varepsilon$ (§6.2), $S_A^\varepsilon$ (§7), regime discipline (§9).
- `THEORY/working/MF/layered_ambient_architecture_next_work.md` — WQ-2 specification.
- `THEORY/working/MF/nq242c_counterexample_protocol.md` — WQ-1 protocol.
- `THEORY/working/MF/nq242c_results.md` — WQ-1 F2 outcome.
- `THEORY/working/MF/wq_lat1_reservoir_resolution_sweep_results.md` — WQ-LAT-1 reservoir-resolution sweep; integer morphology stable, default smooth envelope unstable.
- `THEORY/working/MF/wq_lat1b_phi_envelope_refinement_results.md` — WQ-LAT-1.B phi-envelope refinement; sub-threshold suppressing envelopes restore tested chart-invariance.
- `THEORY/working/E/soft_K_definition.md` — pre-existing $K_{\mathrm{soft}}$ definition with (φ-sat) and (φ-lin) families and CSEH stability proof. **This memo reuses it; it does not redefine it.**
- `THEORY/working/MF/F_Kstep_K_triple.md` — 4-quantity bridge ($\mathcal{F}, K_{\mathrm{step}}, K_{\mathrm{act}}, K_{\mathrm{field}}$); BC-1 well-separated bijection (R23 generic regime fails BC-1).
- `CODE/scripts/ksoft_kact_diagnostics.py` — companion diagnostics script.

---

## 1. Status and Scope

This is a **working bridge-lemma candidate**. It is non-canonical. It does not edit any canonical file. It does not assign a Commitment number.

It does **not**:

- claim $K_{\mathrm{soft}}^\phi = K_{\mathrm{act}}^\varepsilon$ globally;
- claim $K_{\mathrm{soft}}^\phi$ resolves K-Selection (OP-0005);
- claim WQ-1 succeeded;
- claim σ-standard incompleteness;
- claim σ-rich sufficiency;
- prove WQ-1 retry path is correct.

It **does**:

- specify when $K_{\mathrm{soft}}^\phi(U(\mathbf u))$ and $K_{\mathrm{act}}^\varepsilon(\mathbf u)$ may be compared and what error term governs the comparison;
- enumerate explicit failure modes;
- provide a concrete diagnostic protocol so the question "does the aggregate field carry topological transitions while $K_{\mathrm{act}}$ stays static?" can be answered numerically on existing or rerunnable trajectories;
- give a decision rule for whether WQ-1 should be retried as WQ-1.A, WQ-1.B, or WQ-1.C.

The bridge is between Layer II's labelled count discipline and Layer I's unlabelled topological count, mediated by the aggregate projection $U$. It is a comparison statement, not an identification.

---

## 2. Motivation from WQ-1 F2

WQ-1 (NQ-242c protocol) was executed (2026-05-02) on $T^2_{20}$ with $K_{\mathrm{field}} = 4$, $M = 90$, three active slots and one spare. Across **14 trajectories** spanning a primary run plus two parameter sweeps:

| Sweep | Range | Outcome |
|---|---|---|
| primary | $\lambda_{\mathrm{rep}} = 10$, default centers | F2 (no K-jump) |
| λ_rep sweep | $\lambda_{\mathrm{rep}} \in \{30, 100, 300\}$ | F2 for all three |
| B-compression sweep | $c_3^B \in \{(10,8), (10,7), (10,6)\}$, $\lambda_{\mathrm{rep}} = 100$ | F2 for all three |

In every run, $K_{\mathrm{act}}^\varepsilon$ stayed at 3 and the minimum slot mass ever observed was 23.94 — over 100× the activity threshold $\varepsilon = 0.225$.

**Structural reading.** Under the protocol's Option D-2 integrator (per-slot gradient + uniform total-mass rescale), each slot's intra-energy basin is sufficiently deep that the slot retains a coherent localized profile. The rescale step preserves total mass globally but does not preferentially drain a single slot. The dynamics finds a stable 3-formation fixed point.

**The key observation that motivates WQ-2.** Even though $K_{\mathrm{act}}^\varepsilon(\mathbf u(t))$ stayed constant across the F2 trajectories, the *aggregate field* $U(\mathbf u(t)) = \sum_j u^{(j)}(t)$ — a single field on $G$ — could nevertheless have undergone topological transitions: $H_0$ bars in the superlevel persistence diagram of $U$ could merge, split, or change prominence as the per-formation profiles evolved. **$K_{\mathrm{act}}^\varepsilon$ counts labels; it does not see aggregate-field topology.**

Concretely: when two labelled slots overlap such that $u^{(j)}(x) + u^{(k)}(x) > $ threshold across a connected region, the aggregate $U$ sees a single $H_0$ feature there, regardless of the labelling. As the F2 dynamics redistributed mass — slot 0's mass grew from 30 → 33 in primary run; slot 1 dropped 30 → 27.5 — the aggregate's $H_0$ bar lengths could change. $K_{\mathrm{soft}}^\phi(U(\mathbf u(t)))$ is sensitive to this.

**This is the exact relevance of WQ-2.** If $K_{\mathrm{soft}}^\phi(U(\mathbf u(t)))$ does change during F2 trajectories, then the architecture has *aggregate-field-level* transitions even when the labelled $K_{\mathrm{act}}$ is static. WQ-1.C (Layer I $H_0$-jump reframe) becomes empirically promising. Conversely, if $K_{\mathrm{soft}}^\phi$ is also static under F2 dynamics, then aggregate-field topology and labelled count are both rigid in this regime, and only WQ-1.A (true joint projection driving genuine inter-slot mass transfer) or WQ-1.B (forced extinction) remain.

---

## 3. Objects and Type Discipline

| Object | Layer | Type | Labelled? | Threshold? | Meaning |
|---|---|---|---|---|---|
| $K_{\mathrm{field}}$ | architectural | integer cap | yes (slot indexing) | no | architectural cap on number of distinguishable formations; modeling-layer commitment per Commitment 16 |
| $K_{\mathrm{act}}^\varepsilon(\mathbf u)$ | Layer II | integer | yes (counts active labels) | yes ($\varepsilon$) | active count diagnostic; stratum/region index on $\widetilde\Sigma^{K_{\mathrm{field}}}_M$ |
| $U(\mathbf u) = \sum_j u^{(j)}$ | projection II → I | field $U \in \Sigma_M(G)$ | n/a (forgets) | no | aggregate field; bridge object |
| $K_{\mathrm{soft}}^\phi(U)$ | Layer I (computed via $U$) | real | no | envelope-mediated by $\phi$ | persistence-weighted soft count of robust $H_0$ features |
| $K_{\mathrm{bar}}^{\ell_{\min}}(U)$ | Layer I (computed via $U$) | integer | no | yes ($\ell_{\min}$) | hard-bar count: number of $H_0$ bars with persistence $\ge \ell_{\min}$ |
| $\mathcal{F}(v)$ | Layer I | integer | no | no | strict local maxima count; threshold-free; per `F_Kstep_K_triple.md` §2.1 |
| $K_{\mathrm{step}}(v; \tau)$ | Layer I | integer | no | yes ($\tau$) | $\#$ connected components of $\{v > \tau\}$ |

**Mandatory distinctions.**

- $K_{\mathrm{act}}^\varepsilon$ is a *labelled-slot count*. It depends on the partition $(u^{(1)}, \ldots, u^{(K_{\mathrm{field}})})$ and on $\varepsilon$.
- $K_{\mathrm{soft}}^\phi(U)$ is an *unlabelled topological count* on the aggregate. It depends on $G$, the superlevel filtration, $\phi$, and the finite graph resolution.
- They answer different questions:
  - $K_{\mathrm{act}}^\varepsilon$: "how many slots carry detectable mass?"
  - $K_{\mathrm{soft}}^\phi(U)$: "how many topologically-robust object-like features does the aggregate carry?"
- The two questions agree only in regimes where labelled slots correspond bijectively to aggregate $H_0$ features. Outside such regimes, divergence is expected and is *not a contradiction*.

---

## 4. Well-Separated Regime

Following `..._candidate.md` §9.1 and refining for the bridge:

A state $\mathbf u \in S_A^\varepsilon(G_t)$ is **$(\varepsilon, \delta, D_{\mathrm{sep}}, \ell_{\min}, \eta)$-well-separated** if:

1. **Active mass.** $m_j(\mathbf u) > \varepsilon$ for all $j \in A$.

2. **Connected $\delta$-supports.** For each $j \in A$, the support
   $$
   \mathrm{Supp}_\delta(u^{(j)}) := \{x \in X_t : u^{(j)}(x) > \delta\}, \qquad \delta \in (0, 1),
   $$
   is non-empty and connected as an induced subgraph of $G_t$.

3. **Pairwise graph-distance separation.** For all $j \ne k$ in $A$,
   $$
   d_{G_t}\!\big(\mathrm{Supp}_\delta(u^{(j)}), \mathrm{Supp}_\delta(u^{(k)})\big) \;\ge\; D_{\mathrm{sep}}.
   $$

4. **Low pairwise overlap.** For all $j \ne k$ in $A$,
   $$
   \langle u^{(j)}, u^{(k)} \rangle := \sum_x u^{(j)}(x) u^{(k)}(x) \;\le\; \eta.
   $$

5. **Single-mode per formation (aggregate-side).** The aggregate $U(\mathbf u)$ has exactly $|A|$ $H_0$ bars of length $\ge \ell_{\min}$ in the superlevel filtration $\mathrm{Dgm}_0^{\sup}(U)$, and all remaining bars have length below an auxiliary noise threshold $\ell_{\mathrm{noise}} \ll \ell_{\min}$.

These hypotheses are sufficient. They are not minimal. Condition 5 is the load-bearing one for the bridge: it says each labelled slot contributes exactly one robust aggregate-$H_0$ feature, and no additional features arise from per-formation internal multimodality, overlap-induced peak fission, or substrate noise.

**Status:** working-definition safe (the regime). The hypotheses (2), (3), (4), (5) need to be checked numerically per state; the regime is not assumed throughout a trajectory.

**This is not the same as canonical-target Whitney stratification.** $S_A^\varepsilon$ remains an operational ε-active region (per `..._candidate.md` §7.3). The well-separated regime is an additional refinement over $S_A^\varepsilon$.

---

## 5. Bridge Lemma Candidate

### 5.1 Hard-bar count

Define the **hard-bar count** for any single field $v \in [0, 1]^{X_t}$ and threshold $\ell_{\min} > 0$:

$$
K_{\mathrm{bar}}^{\ell_{\min}}(v) \;:=\; \#\big\{ i \;:\; \ell_i(v) \ge \ell_{\min} \big\}
$$

where $\ell_i(v)$ are the lengths of the bars in the $H_0$ superlevel persistence diagram $\mathrm{Dgm}_0^{\sup}(v; G_t)$. This is the integer-valued indicator-form of $K_{\mathrm{soft}}^\phi$ obtained by replacing the smooth envelope $\phi$ with a step function at $\ell_{\min}$.

### 5.2 Exact bridge identity (single-mode, well-separated)

**Bridge identity (exact).** Suppose $\mathbf u \in S_A^\varepsilon(G_t)$ is $(\varepsilon, \delta, D_{\mathrm{sep}}, \ell_{\min}, \eta)$-well-separated per §4 with condition (5) holding. Then

$$
K_{\mathrm{bar}}^{\ell_{\min}}\!\big(U(\mathbf u)\big) \;=\; K_{\mathrm{act}}^\varepsilon(\mathbf u) \;=\; |A|.
$$

**Status:** theorem-grade under the stated hypotheses (Cat B target). The proof is by reduction: condition (5) directly states the equality $K_{\mathrm{bar}}^{\ell_{\min}}(U) = |A|$; condition (1) directly states $K_{\mathrm{act}}^\varepsilon = |A|$. The work is in the *hypothesis verification*: when does (5) hold given (1)–(4)?

A sketch of the implication (1)–(4) ⇒ (5):

- Conditions (3), (4) imply that on each $\delta$-support $\mathrm{Supp}_\delta(u^{(j)})$, the aggregate $U(\mathbf u) = u^{(j)} + \sum_{k \ne j} u^{(k)}$ is dominated by $u^{(j)}$ alone (since $u^{(k)}|_{\mathrm{Supp}_\delta(u^{(j)})} \le \delta$ in the disjoint case, plus a small overlap correction $\le \eta$).
- By condition (2), $\mathrm{Supp}_\delta(u^{(j)})$ is graph-connected. Thus on $\mathrm{Supp}_\delta(u^{(j)})$, $U$ is a single peak (one $H_0$ feature in the local superlevel filtration).
- Condition (3) ensures the $|A|$ peaks remain separated under aggregation: the inter-support graph distance $\ge D_{\mathrm{sep}}$ guarantees the peaks do not merge in the superlevel filtration above any $\theta > \delta$.
- Therefore $U$ has exactly $|A|$ robust peaks, and their bar lengths in $\mathrm{Dgm}_0^{\sup}(U)$ are bounded below by $\min_j \max_x u^{(j)}(x) - O(\delta + \eta)$, which can be made $\ge \ell_{\min}$ for appropriate parameter choice.

The above is a **sketch, not a proof**. A full proof would quantify the constants and the parameter range over which (1)–(4) ⇒ (5) holds. This is downstream work — see §11 next-step item.

### 5.3 Corrected smooth bridge for $K_{\mathrm{soft}}^\phi$ with a phi-class restriction

The previous smooth bridge formulation was too broad. It is **not** enough for $\phi$ to be monotone Lipschitz with $\phi(0)=0$.

WQ-LAT-1 and WQ-LAT-1.B show the correction: the integer hard-bar count can be reservoir-stable in the tested split-bump refinement, while a smooth $K_{\mathrm{soft}}^\phi$ can drift if $\phi$ assigns non-negligible mass to sub-resolution bars. Therefore the smooth bridge must be stated only for a restricted envelope class.

#### 5.3.1 Two observables

The integer hard-bar count is:

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U)
=
\#\{i:\ell_i(U)\ge \ell_{\min}\}.
$$

It is integer-valued, thresholded, and non-smooth. WQ-LAT-1 found it chart-invariant under the tested reservoir refinement

$$
K_{\mathrm{field}}\in\{3,4,6,8,12\}
$$

on $T^2_{20}$, Option D-2 dynamics, LAT-C split-bump refinement, for the tested $\ell_{\min}$ values.

The smooth / soft count is:

$$
K_{\mathrm{soft}}^\phi(U)
=
\sum_i \phi(\ell_i(U)).
$$

This observable is chart-invariant only when $\phi$ suppresses sub-threshold bars. No chart-invariance claim is licensed for arbitrary monotone Lipschitz $\phi$.

#### 5.3.2 Reservoir-admissible phi envelopes

For a persistence threshold $\ell_{\min}>0$ and an edge width / transition parameter $\tau\ge 0$, define a working class

$$
\Phi_{\mathrm{res}}(\ell_{\min},\tau)
$$

of **reservoir-admissible $\phi$-envelopes**. A candidate $\phi:[0,1]\to[0,\infty)$ belongs to this class, for the present working purpose, if it satisfies:

1. **Nonnegativity.**
   $$
   \phi(\ell)\ge 0.
   $$

2. **Lower normalization.**
   $$
   \phi(0)=0.
   $$

3. **Upper / dominant-bar normalization.** Either $\phi(1)\approx 1$, or an explicit alternative scale is declared. Count-like envelopes should satisfy $\phi(\ell)\approx 1$ on the dominant-bar region.

4. **Sub-threshold suppression.**
   $$
   \phi(\ell)\approx 0
   \qquad
   0\le \ell<\ell_{\min}.
   $$
   Strong versions satisfy $\phi(\ell)=0$ for $\ell<\ell_{\min}$.

5. **Dominant-bar retention.**
   $$
   \phi(\ell)\approx 1
   \qquad
   \ell\ge \ell_{\min}+\tau
   $$
   for count-like envelopes. Excess-persistence variants may instead retain a scaled excess value and must not be interpreted as unit counts.

6. **Regularity.** For count diagnostics, $C^0$ or even discontinuous threshold envelopes may be acceptable. For variational or gradient use, require Lipschitz, $C^0$ with controlled kink, or a smooth approximation; state the chosen regularity explicitly.

7. **Sharpness parameter.** A parameter such as $s,\beta,\tau$ must control the transition width near $\ell_{\min}$ and be reported with every diagnostic.

Empirically supported WQ-LAT-1.B families:

**Hard threshold.**

$$
\phi_{\mathrm{hard}}(\ell)
=
\mathbf 1_{\ell\ge\ell_{\min}}.
$$

This gives $K_{\mathrm{bar}}^{\ell_{\min}}$ exactly. It is best for integer count and is not differentiable.

**Sharp logistic threshold.**

$$
\phi_{\mathrm{logistic}}(\ell;\ell_{\min},s)
=
\frac{1}{1+\exp(-s(\ell-\ell_{\min}))}
-
\frac{1}{1+\exp(s\ell_{\min})}.
$$

Use an additional upper normalization if exact unit dominant-bar scale is required. WQ-LAT-1.B supports sharp choices $s\ge 50$, with $s=100$ best in the tested configuration.

**Shifted saturating threshold.**

$$
\phi_{\mathrm{shift\text{-}sat}}(\ell;\ell_{\min},\beta)
=
1-\exp(-\beta(\ell-\ell_{\min})_+).
$$

WQ-LAT-1.B supports $\beta\ge20$ in the tested configuration. This is a shifted suppressing envelope; if differentiability at $\ell_{\min}$ is required, replace $(\cdot)_+$ by a smooth positive-part approximation and re-test.

**Shifted linear excess persistence.**

$$
\phi_{\mathrm{shift\text{-}lin}}(\ell)
=
\max\left(0,\frac{\ell-\ell_{\min}}{1-\ell_{\min}}\right).
$$

This was stable in WQ-LAT-1.B, but it measures excess persistence above $\ell_{\min}$, not unit object count.

#### 5.3.3 Corrected smooth bridge candidate

**Corrected Smooth Bridge Candidate.** Suppose $\mathbf u\in S_A^\varepsilon(G_t)$ is well-separated and the aggregate persistence diagram has exactly $|A|$ dominant $H_0$ bars above $\ell_{\min}$, with all subdominant bars below $\ell_{\min}$. If $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ suppresses sub-threshold bars and retains dominant bars, then

$$
K_{\mathrm{soft}}^\phi\!\big(U(\mathbf u)\big)
=
K_{\mathrm{bar}}^{\ell_{\min}}\!\big(U(\mathbf u)\big)
+
O(\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}+\rho_{\phi}),
$$

and therefore, under the bridge conditions linking robust aggregate bars to active labels,

$$
K_{\mathrm{soft}}^\phi\!\big(U(\mathbf u)\big)
=
K_{\mathrm{act}}^\varepsilon(\mathbf u)
+
O(\rho_{\mathrm{sep}}+\rho_{\mathrm{sub}}+\rho_{\phi}).
$$

The error terms are:

- $\rho_{\mathrm{sub}} := \sum_{i:\ell_i(U)<\ell_{\min}}\phi(\ell_i(U))$ — residual contribution from sub-threshold bars.
- $\rho_{\mathrm{edge}}$ — contribution from bars in the edge band $|\ell_i(U)-\ell_{\min}|\le\tau$, where soft-threshold uncertainty matters.
- $\rho_\phi := \sum_{i:\ell_i(U)\ge\ell_{\min}+\tau}|\phi(\ell_i(U))-1|$ — dominant-bar normalization / envelope bias for count-like envelopes.
- $\rho_{\mathrm{sep}}$ — separation / overlap error linking $K_{\mathrm{bar}}^{\ell_{\min}}(U)$ to $K_{\mathrm{act}}^\varepsilon(\mathbf u)$; this is small only in the well-separated single-mode regime.

For the hard threshold, $\rho_{\mathrm{sub}}=0$ by definition. For sharp logistic and shifted-saturating envelopes, $\rho_{\mathrm{sub}}$ is small only when all sub-threshold bars lie sufficiently below $\ell_{\min}$ relative to the transition width / sharpness parameter.

**Status:** conjectural / downstream (Cat C target). The corrected bridge is more precise than the previous §5.3 statement, but still not theorem-grade. The rigorous version requires CSEH stability (per `soft_K_definition.md` §2.1 + Cor 2.2), a quantitative analysis of the (1)–(4) ⇒ (5) implication, and envelope-specific bounds on $\rho_{\mathrm{sub}},\rho_{\mathrm{edge}},\rho_\phi$.

#### 5.3.4 WQ-LAT-1.B empirical correction

WQ-LAT-1.B on $T^2_{20}$, Option D-2 dynamics, $K_{\mathrm{field}}\in\{3,4,6,8,12\}$, LAT-C split-bump refinement found:

- default $\phi$-sat failed at $\ell_{\min}=0.10$: range $\approx 0.943$, monotone drift with $K_{\mathrm{field}}$, caused by sub-resolution positive bars increasing from 4 to 18;
- hard threshold succeeded: range $0.000$;
- logistic $s=100$ succeeded: range $\approx 0.001$, mean $\approx 1.001$;
- shifted-saturating $\beta=20$ succeeded: range $\approx 0.005$, mean $\approx 0.938$.

Interpretation: the old smooth-envelope bridge error was dominated by sub-resolution bar accumulation. Sub-threshold suppressing envelopes correct this in the tested configuration. This is empirical evidence for the restricted envelope class, not a theorem and not a graph/dynamics-general result.

### 5.4 Honest separation

The bridge is a **comparison lemma under hypotheses**, not a global identity:

- The exact identity §5.2 holds *under condition (5) directly*; the work to establish (5) from a weaker set of hypotheses (1)–(4) is non-trivial.
- The approximate bridge §5.3 has an error term whose form is correct in spirit but whose constants are not yet bounded.
- Both forms are restricted to the well-separated regime. Outside this regime, the bridge fails — see §6.
- Even within the well-separated regime, the bridge depends on choices of $\varepsilon, \delta, D_{\mathrm{sep}}, \ell_{\min}, \eta, \phi$. Sensitivity to these choices is part of the diagnostic protocol (§8).

**The bridge is between specific, computable objects, on a clearly-specified subset of Layer II.** It is not an ontological identification of $K_{\mathrm{soft}}$ and $K_{\mathrm{act}}$.

---

## 6. Failure Modes

The bridge fails generically outside the well-separated regime. Seven failure modes are explicitly catalogued.

### F-B1 — Overlap collapse

Multiple labelled active slots overlap such that $\sum_j u^{(j)}(x) > \theta$ across a connected region for a wide range of $\theta$. The aggregate $U$ sees a single $H_0$ feature; the labelled count sees several.

$$
K_{\mathrm{act}}^\varepsilon(\mathbf u) \;>\; K_{\mathrm{soft}}^\phi\!\big(U(\mathbf u)\big), \qquad K_{\mathrm{act}}^\varepsilon \;>\; K_{\mathrm{bar}}^{\ell_{\min}}(U).
$$

This is the **R23 generic regime** per `F_Kstep_K_triple.md` §3.6: in the R23 fullscale dataset (56 minimizers on $32\times32$ $D_4$ free-BC grid), all 56 satisfy $\mathcal{F}(u^*) > K_{\mathrm{step}}(u^*; \tau)$, indicating the well-separated bijection BC-1 (per-formation lobes ↔ aggregate $H_0$ peaks) **fails generically**. F-B1 is therefore the *generic* failure, not an edge case.

### F-B2 — Internal multimodality

A single active slot $u^{(j)}$ has two or more separated peaks within its own $\delta$-support. Each peak contributes a separate $H_0$ feature in $\mathrm{Dgm}_0^{\sup}(u^{(j)})$, hence in $\mathrm{Dgm}_0^{\sup}(U)$ as well.

$$
K_{\mathrm{soft}}^\phi\!\big(U(\mathbf u)\big) \;>\; K_{\mathrm{act}}^\varepsilon(\mathbf u).
$$

This is the **per-formation $\mathcal{F} \ge 2$ regime** that T-PreObj-1 (canonical Cat A) establishes as the *default ground state* under full SCC. Per `F_Kstep_K_triple.md` §2.1, $\mathcal{F}(u^{(j)}) \ge 2$ generically for active formations. F-B2 is therefore *also* generic, not edge-case.

In R23 fullscale, $\mathcal{F} \in [5, 63]$ and $K_{\mathrm{step}} \in [1, 8]$ — the gap $\mathcal{F} - K_{\mathrm{step}}$ is *large* (max gap = 61). The aggregate field is *highly multimodal* in the typical SCC ground state.

### F-B3 — Low-mass active slot without robust aggregate bar

A slot has mass $m_j(\mathbf u) > \varepsilon$ (counted by $K_{\mathrm{act}}^\varepsilon$) but its profile contributes only a short, sub-$\ell_{\min}$ bar to the aggregate persistence diagram (e.g. mass spread thinly over a large region, no high-amplitude peak).

$$
K_{\mathrm{act}}^\varepsilon \text{ counts the slot, but } K_{\mathrm{bar}}^{\ell_{\min}}(U) \text{ ignores it.}
$$

This is a "barely-active" slot. Sensitive to both $\varepsilon$ and $\ell_{\min}$ choices; one threshold may register the slot while the other does not.

### F-B4 — Aggregate cancellation / saturation

At sites where $\sum_j u^{(j)}(x) \to 1$, the simplex constraint saturates. Aggregate values cluster near 1, and the superlevel filtration's high-$\theta$ slices may contain $X_t$ entirely connected (no peak structure to reveal). Conversely, in regions where multiple slots are diffuse, aggregate values are low and the noise tail of $\mathrm{Dgm}_0^{\sup}(U)$ swells.

This is the **corner-saturated regime** of `..._candidate.md` §9.3 viewed from the $K_{\mathrm{soft}}$ angle: bar lengths and counts in $\mathrm{Dgm}_0^{\sup}(U)$ become sensitive to the field-boundary $\{u^{(j)}(x) \in \{0, 1\}\}$ and simplex-saturation $\{\sum_j u^{(j)}(x) = 1\}$ loci.

### F-B5 — Threshold and envelope sensitivity

The bridge is sensitive to the choice of $\varepsilon$, $\ell_{\min}$, and $\phi$. Different choices may yield different conclusions on the same configuration.

- $\varepsilon$ controls $K_{\mathrm{act}}$ — a near-extinction slot is in or out depending on $\varepsilon$.
- $\ell_{\min}$ controls $K_{\mathrm{bar}}$ — a near-noise bar is in or out depending on $\ell_{\min}$.
- $\phi$ controls $K_{\mathrm{soft}}$ — sub-threshold suppressing envelopes are required for reservoir-invariant count diagnostics; default (φ-sat) may accumulate sub-resolution bars.

A robust bridge must specify these choices and report sensitivity. Defaults:

- $\varepsilon = 0.01 \cdot \bar m$ where $\bar m = M / K_{\mathrm{field}}$ (per `K_status_commitment.md` §6.1).
- $\ell_{\min} = 0.10$ (heuristic; needs tuning per graph and parameter regime).
- $\phi(\ell) = \ell / (\ell + \ell_{\min})$ (legacy WQ-2 diagnostic default; **not** recommended for reservoir-invariant count under LAT-C split-bump refinement).

These are provisional and must be reported in any result.

### F-B6 — WQ-1 F2-style active-count preservation with mobile aggregate topology

This is the failure mode that motivated WQ-2.

Under WQ-1 F2 conditions: $K_{\mathrm{act}}^\varepsilon$ is constant, but per-formation masses *drift* under Option D-2 dynamics (slot 0 grew 30 → 33; slot 1 dropped 30 → 27.5). As masses drift, per-formation profiles redistribute spatially, and the aggregate field $U(\mathbf u(t))$ may undergo:

- bar prominence change (longest-bar-length increases for one slot, decreases for another);
- bar deaths via overlap (two slots' contributions merge into one $H_0$ feature in $\mathrm{Dgm}_0^{\sup}(U)$);
- bar births via internal peak fission (a single slot's profile develops two peaks);
- noise-tail variation (subdominant bars below $\ell_{\min}$).

If any of these happen, $K_{\mathrm{soft}}^\phi(U(\mathbf u(t)))$ varies even though $K_{\mathrm{act}}^\varepsilon(\mathbf u(t))$ is static. F-B6 is the *empirical question* WQ-2 diagnostics (§8) directly answer.

The decision rule for WQ-1 retry (§9) depends on this: **if F-B6 manifests in F2 trajectories, then aggregate-field topology is a richer diagnostic than labelled count, and WQ-1.C is the most informative retry path; if not, WQ-1.A or WQ-1.B are required.**

### F-B7 — Non-admissible $\phi$-envelope drift

If $\phi$ assigns non-negligible mass to sub-resolution bars, then $K_{\mathrm{soft}}^\phi$ may drift with $K_{\mathrm{field}}$ even when the aggregate field, dominant bars, and integer hard-bar count are stable.

This failure mode was empirically observed in WQ-LAT-1 and explained in WQ-LAT-1.B. Under LAT-C split-bump refinement on $T^2_{20}$, the default saturating envelope accumulated contributions from a growing tail of positive sub-threshold bars, causing $K_{\mathrm{soft}}^\phi$ to drift monotonically with $K_{\mathrm{field}}$. The integer observable $K_{\mathrm{bar}}^{0.10}$ remained constant, and sub-threshold suppressing envelopes removed the drift in the tested configuration.

F-B7 is a $\phi$-choice failure, not by itself a failure of the aggregate-field observable. It forbids using arbitrary monotone Lipschitz $\phi$ in the smooth bridge statement.

---

## 7. Relationship to $K_{\mathrm{step}}$, $\mathcal{F}$, and Existing SCC Diagnostics

### 7.1 The four-quantity bridge

Per `F_Kstep_K_triple.md` §3, the existing SCC quantities form a chain:

$$
K_{\mathrm{step}}(v; \tau) \;\le\; \mathcal{F}(v) \quad \text{(single field, all } \tau \text{)},
$$

$$
K_{\mathrm{act}}^\varepsilon(\mathbf u) \;\le\; K_{\mathrm{field}} \quad \text{(architectural)},
$$

$$
\mathcal{F}(U(\mathbf u)) \;=\; \sum_j \mathcal{F}(u^{(j)}) \quad \text{(well-separated K-field)},
$$

$$
\mathcal{F}(U(\mathbf u)) \;\le\; \sum_j \mathcal{F}(u^{(j)}) \quad \text{(overlapping)}.
$$

### 7.2 Where does $K_{\mathrm{soft}}^\phi$ fit?

$K_{\mathrm{soft}}^\phi$ is a *smooth* relative of $K_{\mathrm{step}}$ and $\mathcal{F}$:

- $K_{\mathrm{step}}(v; \tau) = \dim H_0(G|_{\{v > \tau\}})$ is a single-slice count of the superlevel filtration. Threshold-dependent.
- $\mathcal{F}(v)$ is the total number of $H_0$ generators ever born in the superlevel filtration of $v$ (per `F_Kstep_K_triple.md` §7.4.2). Threshold-free, integer.
- $K_{\mathrm{soft}}^\phi(v) = \sum_i \phi(\ell_i(v))$ weights each generator by an envelope of its bar length. Threshold-free in the *birth-threshold* sense. It acts as a prominence-filtered count only when $\phi$ suppresses sub-threshold bars; default smooth saturating envelopes can leak sub-resolution bar count.
- $K_{\mathrm{bar}}^{\ell_{\min}}(v) = \#\{i : \ell_i(v) \ge \ell_{\min}\}$ is the integer-valued step-function form of $K_{\mathrm{soft}}^\phi$.

**Inequalities (single field $v$):**

$$
K_{\mathrm{step}}(v; \tau) \;\le\; K_{\mathrm{bar}}^{\ell_{\min}}(v) \;\le\; \mathcal{F}(v), \qquad K_{\mathrm{soft}}^\phi(v) \;\to\; \mathcal{F}(v) \cdot \phi(1) \;\text{ as bars sharpen.}
$$

The first inequality: at threshold $\tau$, only bars *alive* at $\tau$ are counted — at most $K_{\mathrm{bar}}^{\ell_{\min}}$ if $\tau$ chosen so all bars of length $\ge \ell_{\min}$ are alive.

### 7.3 Existing diagnostics and naming risks

| Existing diagnostic | Relation to bridge objects | Naming risk |
|---|---|---|
| $\mathsf{Inside}(u)$ in `scc/diagnostics.py` | uses $\ell_{\max} \cdot \mathsf{Artic}$, articulation; built on `_persistence_h0_graph` | uses same $H_0$ pipeline as $K_{\mathrm{soft}}^\phi$; do not conflate the diagnostic vector entry with $K_{\mathrm{soft}}$ |
| $\mathcal{F}$ (peak count) per `F_Kstep_K_triple.md` | total number of $H_0$ generators in superlevel filtration | per `F_Kstep_K_triple.md` §7.4.2, $\mathcal{F}(v) = $ # generators in $\mathrm{Dgm}_0^{\sup}(v)$; this is a *birth-counting* quantity, ignoring death/prominence |
| $K_{\mathrm{step}}$ (connectivity at threshold) | $\dim H_0(G\|_{\{v > \tau\}})$ | threshold-dependent slice; not a bar-length quantity |
| $\mathsf{Q}_{\mathrm{morph}} = \ell_{\max} \cdot \mathsf{Artic}$ | uses dominant-bar prominence | morphological quality measure; conceptually related to $K_{\mathrm{soft}}^\phi$ but for $K=1$ context |

**Naming risk: $K_{\mathrm{soft}}$.** The dormant `working/E/soft_K_definition.md` defines $K_{\mathrm{soft}}(u)$ for a *single field* $u$, not for aggregate $U$ derived from a multi-formation state. WQ-2 *reuses* that definition with $v = U(\mathbf u)$. Any working file that wants to compute "$K_{\mathrm{soft}}$ of a multi-formation state" must specify which: $K_{\mathrm{soft}}^\phi(u^{(j)})$ for some specific slot $j$, or $K_{\mathrm{soft}}^\phi(U(\mathbf u))$ for the aggregate. Default for WQ-2 is the aggregate.

### 7.4 What is *not* claimed about these relationships

- $\mathcal{F}(U) = K_{\mathrm{soft}}^\phi(U)$: false in general. $\mathcal{F}$ counts births, $K_{\mathrm{soft}}^\phi$ weights by bar length.
- $K_{\mathrm{step}}(U; \tau) = K_{\mathrm{bar}}^{\ell_{\min}}(U)$: false. They are different slices of the same diagram.
- $K_{\mathrm{act}}^\varepsilon = \mathcal{F}(U)$: false in overlapping regime (R23 generic).
- The four-quantity bridge of `F_Kstep_K_triple.md` is a global identity: *no*, it is a chain of inequalities with regime-conditional equalities.

---

## 8. Computational Diagnostics

For each snapshot $\mathbf u(t)$ of a Layer II trajectory, compute the following diagnostics. The protocol of WQ-1 already records $\mathbf u(t)$ snapshots in memory; the diagnostics module reads them and adds derived quantities.

### 8.1 Per-snapshot diagnostics

| # | Quantity | Source | Computation cost |
|---|---|---|---|
| 1 | per-slot mass $m_j(t) = \sum_x u^{(j)}(t, x)$ | direct sum | $O(K \cdot |X|)$ |
| 2 | active count $K_{\mathrm{act}}^\varepsilon(t) = \#\{j : m_j(t) > \varepsilon\}$ | direct | $O(K)$ |
| 3 | active set $A(t) = \{j : m_j(t) > \varepsilon\}$ | direct | $O(K)$ |
| 4 | aggregate field $U(t) = \sum_j u^{(j)}(t)$ | sum | $O(K \cdot |X|)$ |
| 5 | $H_0$ superlevel barcode $\mathrm{Dgm}_0^{\sup}(U(t); G)$ | `scc.persistence.persistence_h0` (adapted to general `GraphState`) or `_persistence_h0_graph` | $O(|X| \log |X| + |E|)$ Union-Find |
| 6 | dominant bar lengths $\ell_1, \ell_2, \ldots$ of $\mathrm{Dgm}_0^{\sup}(U(t))$ | sort barcode by length descending | $O(|X| \log |X|)$ |
| 7 | hard-bar count $K_{\mathrm{bar}}^{\ell_{\min}}(U(t)) = \#\{i : \ell_i(U(t)) \ge \ell_{\min}\}$ | direct | $O(|X|)$ |
| 8 | soft count $K_{\mathrm{soft}}^\phi(U(t)) = \sum_i \phi(\ell_i(U(t)))$ | with explicitly reported $\phi$; use §5.3.2 envelopes for reservoir-invariant count diagnostics | $O(|X|)$ |
| 9 | pairwise overlaps $O_{jk}(t) = \langle u^{(j)}(t), u^{(k)}(t) \rangle$ | dot products | $O(K^2 \cdot |X|)$ |
| 10 | pairwise $\delta$-support graph distances $d^\delta_{jk}(t)$ | multi-source BFS via `scc.multi.inter_formation_distances` | $O(K \cdot |E|)$ |
| 11 | regime label | classify into well-separated / overlap / corner-saturated / ambiguous (§8.2) | $O(K^2)$ |

### 8.2 Regime classification

Given the per-snapshot diagnostics, classify each snapshot into one of:

- **well-separated:** all of (a) $K_{\mathrm{act}}^\varepsilon = K_{\mathrm{bar}}^{\ell_{\min}}$, (b) $\min_{j \ne k} d^\delta_{jk}(t) \ge D_{\mathrm{sep}}$, (c) $\max_{j \ne k} O_{jk}(t) \le \eta$, (d) per-formation $\mathcal{F}(u^{(j)}(t)) = 1$ for all $j \in A(t)$.
- **overlap:** $K_{\mathrm{act}}^\varepsilon > K_{\mathrm{bar}}^{\ell_{\min}}$ (F-B1) and not corner-saturated. *or* $\max_{j \ne k} O_{jk}(t) > \eta$.
- **multimodal:** $K_{\mathrm{bar}}^{\ell_{\min}}(U) > K_{\mathrm{act}}^\varepsilon$ or $K_{\mathrm{soft}}^\phi(U) > K_{\mathrm{act}}^\varepsilon$ with $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ (F-B2): aggregate has more robust features than labelled slots, e.g. one slot internally multimodal.
- **corner-saturated:** at least one of (a) $\min_j m_j(t)$ within $2\varepsilon$ of $\varepsilon$ (extinction-imminent), (b) $\max_{j, x} u^{(j)}(t, x) > 1 - 10^{-3}$ (field-boundary), (c) $\max_x \sum_j u^{(j)}(t, x) > 1 - 10^{-3}$ (simplex-saturation).
- **ambiguous:** none of the above cleanly applies.

### 8.3 JSON schema extension

Add the following block to the WQ-1 result JSON (additive, optional, does not break the existing schema):

```json
{
  "ksoft_kact_diagnostics": {
    "epsilon": 0.225,
    "l_min": 0.10,
    "phi_family": "phi-sat",
    "phi_params": {"l_min": 0.10},
    "delta": 0.05,
    "D_sep_threshold": 3,
    "eta_threshold": 0.5,
    "snapshot_times": [0, 25, 50, ...],
    "K_act": [3, 3, 3, ...],
    "K_bar": [3, 3, 2, ...],
    "K_soft": [2.91, 2.93, 2.30, ...],
    "F_aggregate": [3, 3, 4, ...],
    "F_per_formation": [[1,1,1,0], ...],
    "dominant_bar_lengths": [[0.85, 0.83, 0.81], ...],
    "subdominant_bar_count": [12, 14, 11, ...],
    "pairwise_overlaps": [[[1.0, 0.02, 0.01], ...], ...],
    "min_support_distance": [9, 9, 4, ...],
    "max_overlap": [0.02, 0.05, 0.31, ...],
    "regime_label": ["well-separated", "well-separated", "overlap", ...]
  }
}
```

The example records the legacy WQ-2 diagnostic default. Future reservoir-invariance diagnostics should report the chosen envelope explicitly and prefer `hard`, `logistic_s100`, or `shift_sat_b20` style names when using the WQ-LAT-1.B-supported families.

The block is keyed by its own top-level identifier (`ksoft_kact_diagnostics`) so it does not conflict with the existing `diagnostics` block of `nq242c_result_schema.json`.

### 8.4 Concrete inquiry on F2 trajectories

Run the diagnostics on the seven F2 results from WQ-1 (primary + λ_rep ∈ {30, 100, 300} + B-compression {y8, y7, y6}). Inspect:

- **(I-1) Does $K_{\mathrm{soft}}^\phi(U(t))$ vary along the trajectory?** Compare values at $t = 0$ and $t = $ final.
- **(I-2) Does $K_{\mathrm{bar}}^{\ell_{\min}}(U(t))$ vary?** This is the integer-valued analog of (I-1). A change in $K_{\mathrm{bar}}$ would be the unlabelled analog of a "K-jump" at the aggregate-field level.
- **(I-3) Does the regime label change?** A transition from well-separated to overlap (or vice versa) is itself a topological transition even if no $K_{\mathrm{bar}}$ jump occurs.
- **(I-4) Do dominant bar lengths drift?** Even if counts are stable, prominence variation may carry distinguishability.

The answers to (I-1)–(I-4) determine the WQ-1 retry decision (§9).

### 8.5 Companion script

`CODE/scripts/ksoft_kact_diagnostics.py` (created in this WQ-2 batch) implements the diagnostics. It reuses `nq242c_counterexample.RunConfig` and `run_trajectory`, then post-processes per-snapshot fields with `_persistence_h0_graph` from `scc/diagnostics.py`. Output is a JSON conforming to §8.3. The script does *not* edit canonical or unrelated code.

The current WQ-1 script (`nq242c_counterexample.py`) does not serialize the per-snapshot $\mathbf u$ fields (only $m_j$ and $K_{\mathrm{act}}$). The diagnostics script must therefore *rerun* the trajectory with diagnostics computed inline. Single trajectory runs in 1–2 s; 14-trajectory sweep in <1 min.

---

## 9. Implications for WQ-1 Retry Strategy

### 9.1 The decision rule

Run the diagnostics of §8 on the WQ-1 F2 trajectories. The outcome of (I-1), (I-2), (I-3), (I-4) selects the retry path:

| Diagnostic outcome | Interpretation | Recommended retry |
|---|---|---|
| $K_{\mathrm{bar}}^{\ell_{\min}}$ changes during F2 trajectory | Aggregate field has topological transitions even with $K_{\mathrm{act}}$ static (F-B6 manifest) | **WQ-1.C** — Layer I $H_0$-jump reframe is empirically promising |
| $K_{\mathrm{soft}}^\phi$ changes (smooth) but $K_{\mathrm{bar}}$ static | Aggregate prominence drifts; soft transition without hard jump | **WQ-1.C** with smooth-$K_{\mathrm{soft}}$ comparison; still informative |
| Regime label changes (e.g. well-separated → overlap) | Topological transition without count change; still relevant for σ-standard | **WQ-1.C** with regime-transition comparison |
| All four diagnostics static | Aggregate topology is also rigid under F2 dynamics; WQ-1.C uninformative | **WQ-1.A** (true joint projection) or **WQ-1.B** (forced extinction) |

### 9.2 Path evaluation

**WQ-1.A — true joint projection (Option D-1).**

- *Purpose:* implement Dykstra-style joint projection onto $\widetilde\Sigma^{K_{\mathrm{field}}}_M$ (mass plane ∩ box [0,1] ∩ simplex). May permit inter-slot mass transfer that Option D-2 cannot.
- *Needs:* projection rule on shared-pool ambient. Modify `project_to_layer_II_D2` → `project_to_layer_II_D1`.
- *Risk:* defines a different effective dynamics from the current SCC implementation (`scc/multi.py::find_k_formations` uses per-slot `project_volume` = Option D-2-like). The Layer II ambient theory is correct, but the resulting trajectories may not match canonical or literature dynamics. Mitigation: run both Option D-1 and Option D-2 and report each separately.
- *Estimated effort:* ~1 day to implement; ~30 min to run.

**WQ-1.B — forced extinction intervention.**

- *Purpose:* equilibrate at $K_{\mathrm{act}} = 3$, force $u^{(\mathrm{argmin}_j m_j)} \leftarrow 0$, re-equilibrate at $K_{\mathrm{act}} = 2$, compare σ-standard pre/post.
- *Risk:* not natural dynamics. Tests σ-standard *response* to a prescribed extinction, not σ-standard *predictive sufficiency* across a natural extinction. Different question. Acceptable if explicitly framed as such.
- *Estimated effort:* ~half day.

**WQ-1.C — Layer I $H_0$-jump reframe.**

- *Purpose:* abandon labelled K-field for the σ-test. Equilibrate a single field on $\Sigma_M(G)$, perturb, observe whether $H_0$ bar-death occurs in $\mathrm{Dgm}_0^{\sup}(u(t))$. Compare σ-standard (Hessian eigenvalue cluster of single field) pre/post.
- *Needs:* WQ-2 bridge lemma (this document) for interpretation.
- *Risk:* tests topological-feature transition, not labelled-slot extinction. The "K-jump" being tested is *unlabelled*. The result, if positive, is about σ-standard sensitivity to aggregate-field topology changes, not about labelled-slot inheritance.
- *Estimated effort:* ~1 day; depends on WQ-2 diagnostics outcome.

### 9.3 Recommendation (provisional)

**Run §8 diagnostics on WQ-1 F2 trajectories first.** This is cheap (<1 min compute) and decisive.

If F-B6 manifests (aggregate-field topology changes during F2 trajectories): **prioritize WQ-1.C**. The architecture's bridge between labelled count and unlabelled topology becomes empirically active, and σ-standard sensitivity to aggregate transitions becomes the cleanest test.

If F-B6 does not manifest: **prioritize WQ-1.A**. Implement Option D-1 (joint projection) and rerun NQ-242c. WQ-1.B (intervention) is the fallback if Option D-1 also fails to drive a K-jump.

In all cases: do **not** weaken OP-0008 severity, do **not** claim σ-rich sufficiency, do **not** claim any global theorem on the basis of a single numerical anchor.

### 9.4 Phi-envelope recommendation after WQ-LAT-1.B

For integer object-count diagnostics, use:

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U).
$$

For differentiable or smooth approximations to the integer count, use a reservoir-admissible envelope from §5.3.2, with parameters reported:

$$
K_{\mathrm{soft}}^{\phi_{\mathrm{logistic}}}(U)
\quad\text{with}\quad s\ge 50
$$

or

$$
K_{\mathrm{soft}}^{\phi_{\mathrm{shift\text{-}sat}}}(U)
\quad\text{with}\quad \beta\ge 20.
$$

Avoid the default $\phi$-sat envelope for reservoir-invariant count under LAT-C split-bump refinement. It remains a meaningful persistence-weighted observable, but WQ-LAT-1 and WQ-LAT-1.B show it is not chart-invariant in the tested refinement because it accumulates sub-resolution bars.

Treat $\ell_{\min}=0.10$ as empirically supported only for the tested $T^2_{20}$, Option D-2, seed-42 WQ-LAT-1 / WQ-LAT-1.B configuration. It is not canonical and should be re-tested on other graphs, dynamics, or initialization families.

---

## 10. Non-Claims

This document does not:

- claim $K_{\mathrm{soft}}^\phi(U(\mathbf u)) = K_{\mathrm{act}}^\varepsilon(\mathbf u)$ globally;
- claim $K_{\mathrm{soft}}^\phi$ resolves K-Selection (OP-0005);
- claim σ-standard incompleteness;
- claim σ-rich sufficiency;
- claim Φ_rich determinism;
- promote any object to canonical;
- assert $\{S_A^\varepsilon\}$ are Whitney strata;
- invoke stratified Morse theory as established machinery;
- import gauge theory, full category theory, sheaf cohomology beyond $H_0$ persistence, CBF/CLF, neural operators, Koopman operators, or formal verification;
- make any vision / robotics / control / application claim;
- prove the (1)–(4) ⇒ (5) implication with bounded constants;
- claim the bridge lemma holds outside the well-separated regime;
- claim WQ-1 succeeded;
- claim the WQ-1.C retry is correct in advance of running §8 diagnostics.

OP-0008 retains 🟠 HIGH severity unconditionally.

---

## 11. Next Work Packages

In execution order:

### WQ-2.D-1 — Diagnostics on F2 trajectories

- Run `CODE/scripts/ksoft_kact_diagnostics.py` on the WQ-1 sweep configurations.
- Output: per-trajectory JSON conforming to §8.3 schema; summary table of (I-1)–(I-4) outcomes.
- Estimated effort: <30 min compute + ~1 hour analysis writeup.

### WQ-2.A — Bridge lemma proof sketch upgrade

- Upgrade §5.2 sketch to a quantitative (1)–(4) ⇒ (5) implication with explicit constants.
- Cite CSEH stability for the perturbation analysis; explicit graph-spectral dependence.
- Estimated effort: ~2–3 days.

### WQ-2.B — Sensitivity sweep on $(\varepsilon, \ell_{\min}, \phi)$ defaults

- Vary $\ell_{\min} \in \{0.05, 0.10, 0.15, 0.20\}$; report sensitivity of $K_{\mathrm{bar}}, K_{\mathrm{soft}}$ on a fixed configuration.
- Compare (φ-sat) vs (φ-lin) families on the same diagram.
- Estimated effort: ~1 day.

### WQ-2.C — R23 dataset diagnostic

- Run §8 diagnostics on the R23 fullscale dataset (`single_high_F_equivalence.md`); confirm F-B1, F-B2 are generic.
- Quantify the gap between $K_{\mathrm{act}}^\varepsilon$ (if defined for R23 minimizers via per-formation extraction), $K_{\mathrm{bar}}^{\ell_{\min}}(U^*)$, $K_{\mathrm{step}}(U^*; \tau)$, $\mathcal{F}(U^*)$ across all 56 minimizers.
- Output: empirical fingerprint of the SCC ground-state regime under the four-quantity bridge.
- Estimated effort: ~1 day.

### WQ-1 retry (deferred)

- Selected per §9 decision rule after WQ-2.D-1 completes.

### After WQ-2 + WQ-1 retry

- WQ-3 (σ-rich minimal packet analysis) becomes meaningful only if a K-jump or aggregate-topological-transition is in hand from one of the retry paths.

---

## 12. Summary

- $K_{\mathrm{act}}^\varepsilon(\mathbf u)$ counts active labels; $K_{\mathrm{soft}}^\phi(U(\mathbf u))$ measures robust connected topological features of the aggregate field. They answer different questions.
- They agree, within an explicit error term, only under the well-separated single-mode regime (§4 conditions (1)–(5)). The exact identity $K_{\mathrm{bar}}^{\ell_{\min}}(U) = K_{\mathrm{act}}^\varepsilon$ holds under condition (5) directly; the smooth $K_{\mathrm{soft}}^\phi$ version is restricted to reservoir-admissible envelopes $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ and has an error term (§5.3) bounded by separation residual, sub-threshold tail, edge-band uncertainty, and envelope normalization.
- Outside the well-separated regime, seven failure modes (§6) cause the bridge to fail, with **F-B1 (overlap collapse) and F-B2 (internal multimodality) generic in the R23 SCC ground-state regime** per `F_Kstep_K_triple.md` §3.6, and **F-B7 (non-admissible $\phi$ drift)** empirically observed in WQ-LAT-1 / WQ-LAT-1.B.
- WQ-1's F2 outcome (no K-jump under Option D-2) shows that $K_{\mathrm{act}}^\varepsilon$ is rigid under the current dynamics. Whether $K_{\mathrm{soft}}^\phi(U(t))$ is *also* rigid along the same trajectories is the empirical question the WQ-2 diagnostics (§8) directly answer.
- The answer determines the WQ-1 retry path: WQ-1.C (Layer I aggregate-topology reframe) if the aggregate sees transitions; WQ-1.A (joint projection) or WQ-1.B (intervention) if it does not.
- WQ-2 creates the bridge needed to make the next WQ-1 retry mathematically meaningful. It does not by itself produce a counterexample, prove a theorem, or resolve any open problem.

---

---

## 13. WQ-2.D-1 Empirical Outcome (2026-05-02 production run)

**Run.** `CODE/scripts/ksoft_kact_diagnostics.py --max_iter 5000 --seed 42 --output CODE/scripts/results/ksoft_kact_diag.json`. Wall-clock 7.3 s. Default WQ-1 configuration: $T^2_{20}$, $K_{\mathrm{field}}=4$, $M=90$, equilateral A vs isosceles B, $\lambda_{\mathrm{rep}}=10$, $\lambda_{\mathrm{bar}}=100$, $\sigma_b=2.0$, $\varepsilon=0.225$, $\ell_{\min}=0.10$, $\delta=0.05$, $\phi(\ell)=\ell/(\ell+\ell_{\min})$ (φ-sat).

**Per-trajectory diagnostic summary.**

| Quantity | Trajectory A | Trajectory B |
|---|---|---|
| $K_{\mathrm{act}}^\varepsilon$ start → end | **3 → 3 (changed: no)** | **3 → 3 (changed: no)** |
| $K_{\mathrm{bar}}^{0.10}(U)$ start → end | **3 → 1 (changed: yes)** | **3 → 1 (changed: yes)** |
| $K_{\mathrm{soft}}^\phi(U)$ range | **1.797 (smooth-changed: yes)** | **1.788 (smooth-changed: yes)** |
| Regime label start → end | corner-saturated → overlap | corner-saturated → overlap |
| Dominant-bar drift (longest bar) | 0.760 | 0.759 |
| $\mathcal{F}(U)$ at $t = 0$, mid, final | 9, 3, 4 | 9, 3, 4 (similar) |

**$K_{\mathrm{soft}}^\phi$ time series (Trajectory A, sampled).**

- $t = 0$: 2.711 (initial Gaussian saturated state with three near-unity peaks → three bars near 1.0).
- early phase: 2.71 → 2.57 → ... → ~0.92 (rapid descent as peaks lose height under inter-formation repulsion + simplex barrier).
- mid → final: 0.916 (stable on all subsequent snapshots).

The trajectory descended from a 3-bar regime (each bar contributing $\approx 0.9$ to $K_{\mathrm{soft}}^\phi$, total $\approx 2.7$) to a 1-bar regime (one dominant bar contributing $\approx 0.92$, the other two having shrunk below $\ell_{\min} = 0.10$, hence not counted in $K_{\mathrm{bar}}^{0.10}$ but still smoothly contributing very little to $K_{\mathrm{soft}}^\phi$). The number of integer-counted topologically-robust features in the *aggregate* dropped from 3 to 1.

**Diagnostic decision rule outcome (per §9.1).**

Both A and B exhibit:

- $K_{\mathrm{bar}}$ changes (yes for both) — F-B6 manifest at the integer level;
- $K_{\mathrm{soft}}$ smooth changes (yes for both) — F-B6 manifest at the smooth level;
- regime transitions (corner-saturated → overlap, both).

Per §9.1 decision table, the recommended retry path is **WQ-1.C — Layer I $H_0$-jump reframe**.

**Interpretation.**

- The aggregate field $U(\mathbf u(t))$ undergoes a clear *unlabelled topological transition* even when the labelled $K_{\mathrm{act}}^\varepsilon$ is rigid. This is exactly the F-B6 failure mode of the bridge lemma — the bridge lemma's well-separated single-mode hypothesis (5) does not hold along the F2 trajectory.
- The transition is *not* an OP-0008-style K-jump (no slot extincts), but it *is* a topological transition at the Layer I level: the aggregate's $H_0$ persistence diagram changes its dominant-bar structure.
- A and B trajectories show *qualitatively identical* aggregate-topology trajectories ($K_{\mathrm{bar}}$ both go 3 → 1; $K_{\mathrm{soft}}$ ranges both ≈ 1.79). This is a constraint on how WQ-1.C must be designed: the σ-standard test on Layer I aggregates must compare A and B *during* or *after* the topological transition, not by relying on the transition itself to differentiate them.

**Caveats.**

- $\ell_{\min} = 0.10$ default is provisional. Sensitivity to $\ell_{\min}$ is a WQ-2.B item (§11). The integer drop $K_{\mathrm{bar}}^{0.10}$ : 3 → 1 may shift to 3 → 2 or 3 → 0 under different $\ell_{\min}$.
- The "corner-saturated" initial regime is an artifact of the Gaussian-bump initial state with $\sigma_b = 2$, where peaks reach $u^{(j)}(c_j) \approx 1$. The transition to "overlap" reflects descent of those peaks under the simplex barrier, not a fundamental topological change.
- $K_{\mathrm{soft}}^\phi$ stabilizes to 0.916, which equals $\phi(\ell_{\dom}) \approx \ell_{\dom} / (\ell_{\dom} + 0.10)$ for a single dominant bar of length $\ell_{\dom} \approx 1.0$. The aggregate field at equilibrium has effectively *one* dominant feature (the merged supports of all three slots viewed as a single connected superlevel-set component for most thresholds).
- $\mathcal{F}(U)$ at equilibrium is 4 (for A) — this means the aggregate has 4 strict local maxima but they are not topologically robust (their bars are below $\ell_{\min}$). The peak count and the bar count diverge in the overlap regime, consistent with `F_Kstep_K_triple.md` BC-1 failure.

**Status:** working-grade empirical observation. Single configuration, single seed. Sensitivity sweeps deferred to WQ-2.B. R23 dataset diagnostic deferred to WQ-2.C. Bridge lemma proof sketch upgrade deferred to WQ-2.A.

**Output artifact:** `CODE/scripts/results/ksoft_kact_diag.json` contains 201 snapshots × per-snapshot diagnostics for both A and B trajectories, including pairwise overlap matrices, support distances, full bar-length lists, and regime labels.

**Implication for WQ-1 retry.** Pursue WQ-1.C. Specifically:

1. Initialize a single field $u(0) \in \Sigma_M(G)$ (Layer I) with a 3-bump configuration (analog of A or B but as a single field, not labelled).
2. Run gradient flow on the SCC single-field energy.
3. Monitor $\mathrm{Dgm}_0^{\sup}(u(t))$ for bar-deaths.
4. At a bar-death event $t^*$, sample σ-standard at $t^{*-}$ and $t^{*+}$.
5. Repeat for two analogously-distinct initial configurations A_I, B_I (single-field analogues of A and B).
6. Test the σ-standard incompleteness claim at the Layer I bar-death event level.

This is a different test than NQ-242c. It is not OP-0008. It is a Layer I analog whose theoretical interpretation depends on the bridge lemma (this document) for connection back to the multi-formation OP-0008 question. Whether the Layer I result, even if positive, *implies* multi-formation σ-standard incompleteness is a downstream theoretical question not settled by WQ-2 alone.

---

**End of `ksoft_kact_bridge_lemma.md`.**

**Status: working draft. Bridge lemma stated as candidate (Cat B target hypotheses + Cat C target error term); failure modes catalogued; computational diagnostics specified; WQ-1 retry decision rule provided. WQ-2.D-1 production run completed (2026-05-02): F-B6 manifest, WQ-1.C recommended.**

**Companion script:** `CODE/scripts/ksoft_kact_diagnostics.py`.
**Output JSON:** `CODE/scripts/results/ksoft_kact_diag.json`.
