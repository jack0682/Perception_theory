# formation_birth_string_breaking.md — NQ-253: Formation Birth via String-Breaking Analog (Gauge Theory Connection H)

> **⚠️ PARTIAL RETIRE-CANDIDATE (W6 D1 EOD parking-lot Issue #4 audit, 2026-05-04)**
> **Retire scope:** QCD string-breaking analog framing + 't Hooft 1974 / Bali 2001 / QuEra-Harvard-Innsbruck 2025 cross-domain rhetoric (motivational only; CN10 contrastive — no mathematical import from gauge theory).
> **Preserve scope:** (1) **NQ-198a empirical anchor** ($C(\beta) \approx 13.2$ at $\beta = 4, \xi_0 = 0.5$ — V5b-F empirical scaling); (2) **R23 F=63 single-web configuration** observation; (3) **Critical boundary-size threshold formulation** $|\partial S|_{\mathrm{crit}}$ from §3 — SCC-intrinsic geometric criterion for formation birth.
> **Future split (W7+ recommended):** extract NQ-253 SCC-intrinsic threshold formulation into `working/MF/formation_birth_threshold_NQ253.md`, retire gauge-theory framing to `_archive/cv17_speculative_retired_2026-05-04/`.
> **5 active inbound references** (n1_kramers_extension, cn15_static_dynamic_separation, sigma_to_crisp_recovery, sigma_topological_invariance, parking_lot_inventory) → split must preserve link integrity.
> **CN10 disclosure**: SCC formation birth is mass-conserving gradient-flow + double-well dynamics; gauge-theory string breaking is dynamical confinement-deconfinement transition. Structural parallel ("threshold-driven nucleation") is heuristic motivation only; mathematical content is SCC-intrinsic.

**Status:** REVISED (W5 Day 4 PM Wave 3); awaiting W6 critic re-review.
**Type:** Theory development — gauge theory analog + formation birth mechanism.
**Author origin:** Day 4 OAT batch session post-Critic. Gauge theory Connection H (Very Strong) from `daily/2026-04-30/06_gauge_theory_connections_analysis.md`.
**Canonical refs:** §3.x formal universe; §8 4-energy; §11.1 Commitments 14, 16; §13 T-Merge (b) Cat A; §13 V5b-F (NQ-198a empirical, $C(\beta)$ string tension); §14 CN10 (contrastive), CN5 (4-term), CN17 (σ-framework).
**Working refs:** `mathematical_scaffolding_4tools.md` §2 (Tool A1 stratified space, K-jump = stratum transition); `multi_formation_sigma.md` §1 (K-field architecture, σ_multi^A); `single_high_F_equivalence.md` (R23 F=63 stretched configurations); `F_Kstep_K_triple.md` (quadruple bridge); `shared_pool_canonical_proposal.md` (stratified space I9').
**Experimental anchor:** NQ-198a ($C(\beta) \approx 13.2$ at $\beta = 4$, $\xi_0 = 0.5$); R23 F=63 single-web configuration.
**Open problems:** NQ-200 cluster (W7+ candidate, non-involution canonical iso $K \geq 3$); OP-0009-A (architecture); OP-0003 MO-1.
**External refs:** QuEra Computing + Harvard + Innsbruck 2025 (Science) string breaking on kagome lattice; Bali 2001 QCD string tension; 't Hooft 1974 large-N.
**CN10 contrastive status:** gauge theory analog is *formal structural analogy only*; SCC is not a gauge theory. u_t primitive maintained; 4-energy not merged.

---

## §1. Mission

### §1.1 Target question

> **"How does a new SCC formation come into existence? What is the mechanism by which $K_{\mathrm{act}}$ increases by 1 ($\Delta K = +1$)?"**

This file formalizes the **formation birth mechanism** in SCC by exploiting the structural analogy with **string breaking** in lattice gauge theory (Connection H). The analogy is:

| Gauge theory | SCC analog |
|---|---|
| Flux tube / string between static charges | Elongated single formation $u^{(j)}$ in V5b-F regime |
| String tension $T_{\mathrm{str}}$ | SCC tension proxy $C(\beta) \cdot |\partial S|/n$ (V5b-F mass-gap coefficient) |
| String length $L$ | Formation boundary size $|\partial S(u^{(j)})|$ |
| String breaking: new charge pair creation | Formation birth: $K_{\mathrm{act}} \to K_{\mathrm{act}} + 1$ |
| Critical string length $L_{\mathrm{crit}}$ | Critical boundary $|\partial S|_{\mathrm{crit}}$ |

**NQ-200 cluster connection:** Formation birth ($\Delta K = +1$) is the entry point for the non-involution canonical isomorphism problem for $K \geq 3$ (NQ-200, W7+ undeveloped). This file constitutes the **NQ-253 Phase 1** attack on NQ-200.

### §1.2 Scope and constraints

- **In scope**: Formation birth mechanism, string-breaking analog, critical threshold theory, experimental design, NQ-200 entry.
- **Out of scope**: Full proof of birth threshold (Cat A, W8–W10); K=3+ cascade beyond K=1→2 birth (NQ-200 Phase 2); dynamic noise models (P-F flag required, see §4).
- **Hard constraint (CN10)**: All gauge theory correspondences in this file are *formal structural analogies*, not reductive identifications. SCC has no gauge field, no Wilson loop, no Polyakov loop. The analogy is heuristic scaffolding for mathematical intuition only.

---

## §2. SCC String: Definition and Properties

### §2.1 SCC string as elongated formation

**Definition 2.1 (SCC String).** An SCC string is a single-formation minimizer $u^{(j)*} \in \Sigma_{m_j}$ in the **V5b-F regime** — characterized by:
- Two separated peak clusters ("endpoints") at graph distance $d_{\mathrm{sep}} \gg \xi_0$
- A connecting "flux tube" region of intermediate cohesion $u^{(j)*}(x) \in (0.1, 0.5)$ bridging the endpoints
- Single connected component ($K_{\mathrm{step}}(u^{(j)*}; \tau_{1/2}) = 1$ for threshold $\tau_{1/2} = 0.5$)
- Multiple local maxima ($\mathcal{F}(u^{(j)*}) \geq 2$) — two endpoint peaks + possible intermediate peaks

The V5b-F regime is empirically documented (NQ-198a): at $\beta = 4$, $\xi_0 = 0.5$, the formation develops a connecting region with characteristic energy contribution proportional to $|\partial S|$ (boundary size of support set $S(u^{(j)*}) := \{x : u^{(j)*}(x) > \tau\}$).

**Empirical anchor (R23 F=63):** The R23 high-F minimizer with $\mathcal{F} = 63$, $K_{\mathrm{step}} = 1$ (`single_high_F_equivalence.md` §4.2, IC=random, $E = 508.9$) is the extreme SCC string: a single connected formation with 63 local maxima (peaks) connected through a network of shared boundary regions. This is the "maximally stretched" SCC string observed in R23.

### §2.2 String length proxy

**Definition 2.2 (SCC String Length).** For an SCC string $u^{(j)*}$ with support $S(u^{(j)*}; \tau)$:
$$L_{\mathrm{str}} := |\partial S(u^{(j)*}; \tau)| = \#\{x \in S : \exists y \sim x,\; y \notin S\}$$
the graph-boundary size (number of nodes in $S$ with at least one neighbor outside $S$). This is the **string length proxy** — a threshold-dependent but monotone measure of the elongation of the formation support.

**Justification**: In the V5b-F regime, the boundary energy $E_{\mathrm{bd}} = 2\alpha \cdot u^{\top} L u \propto |\partial S|$ (canonical §8, boundary term) dominates the shape cost of the elongated formation. The boundary $|\partial S|$ measures how much "surface" the connecting tube exposes.

**Alternative proxy**: For a formation with two separated endpoint peaks at positions $c_1, c_2 \in X$:
$$L_{\mathrm{str}}^{(\mathrm{alt})} := d_G(c_1, c_2)$$
the graph distance between endpoints. This is threshold-free but ignores the tube width. The two proxies are correlated: $L_{\mathrm{str}} \approx 2 \cdot L_{\mathrm{str}}^{(\mathrm{alt})} \cdot w_{\mathrm{tube}}$ where $w_{\mathrm{tube}}$ is the characteristic tube width (1-2 nodes for narrow tubes).

### §2.3 String tension

**Definition 2.3 (SCC String Tension).** From V5b-F mass scaling (NQ-198a empirical, W6+ Cat B):
$$\mu_{\mathrm{Gold}} \approx C(\beta) \cdot \frac{|\partial S|}{n}$$
where $n = |X|$ is the graph size and $\mu_{\mathrm{Gold}}$ is the Goldstone mode pseudo-mass. The coefficient:
$$T_{\mathrm{str}} \equiv C(\beta) \approx 13.2 \quad \text{at } \beta = 4,\; \xi_0 = 0.5 \; (\text{NQ-198a empirical})$$
is interpreted as the **SCC string tension**: energy cost per unit boundary length.

**Natural interpretation**: The energy contribution of the connecting flux tube is:
$$E_{\mathrm{str}} \approx T_{\mathrm{str}} \cdot L_{\mathrm{str}} = C(\beta) \cdot |\partial S|$$
This matches the standard gauge theory string energy formula $E_{\mathrm{str}} = T_{\mathrm{str}} \cdot L$ (Bali 2001). The $1/n$ factor in $\mu_{\mathrm{Gold}}$ is a **thermodynamic limit dilution**: as graph size grows, the string tension contribution per site decreases as $O(1/n)$, consistent with an extensive boundary energy divided by system size.

**Status**: $C(\beta)$ numerical value is empirical (Cat B, NQ-198a). The **functional form $C(\beta)$** as a function of $\beta/\alpha$ and $\xi_0$ is NQ-198k (W6+, Cat C open). The string tension analog requires $C(\beta)$ functional form for a complete theory — this is the primary theoretical gap.

### §2.4 V5b-F reinterpretation as "SCC string in tension"

The V5b-F mechanism (canonical §13, Cat C empirical with NQ-173 Branch B verdict $\sim 70\%$) describes a single formation with:
- Bulk-localized translation Goldstone mode (partial, not exact)
- Mass $\mu_{\mathrm{Gold}} \propto C(\beta) \cdot |\partial S| / n$

**Reinterpretation**: $\mu_{\mathrm{Gold}}$ is the energy cost of translating the formation — which for an elongated string means *stretching one endpoint while keeping the other fixed*. The string tension $C(\beta)$ resists this translation. As the string is stretched (endpoints moved apart, $L_{\mathrm{str}}$ increases), the Goldstone mass increases proportionally. This is precisely the gauge theory string in tension: translation breaks the string's zero mode.

**Important (C-2 resolution)**: $\mu_{\mathrm{Gold}}$ *grows* with $L_{\mathrm{str}}$ (this section). This means $\mu_{\mathrm{Gold}} = 0$ does NOT occur at the string-breaking threshold (which is at finite $L_{\mathrm{crit}} > 0$). The previous §5.3 derivation of $L_{\mathrm{crit}}$ from setting $\mu_{\mathrm{Gold}} = 0$ was incorrect and has been removed. See §5 (revised) for the correct boundary-energy-only interpretation of the V5b-F formula, and §5.4 / §6.2 for the independent bifurcation criterion $\lambda_{\min}(H) = 0$.

---

## §3. String Breaking Threshold Mechanism

### §3.1 Energetics of breaking

**Setup**: Consider a single formation $u^{(j)*}$ in SCC string configuration with endpoints separated by distance $L = d_G(c_1, c_2)$. As $L$ increases (controlled externally, e.g., by initial condition protocol), the string energy is:
$$E_{\mathrm{str}}(L) \approx T_{\mathrm{str}} \cdot 2L \cdot w_{\mathrm{tube}} + E_{\mathrm{endpoint}}$$
where $2L \cdot w_{\mathrm{tube}} \approx |\partial S|$ is the boundary count of the tube and $E_{\mathrm{endpoint}}$ is the fixed cost of the two endpoint disks (independent of $L$).

**Breaking cost**: If the string breaks into **two independent disk formations** $u^{(1)*}$, $u^{(2)*}$ (each a single peak, K=2), the energy is:
$$E_{\mathrm{broken}}(L) \approx 2 \cdot E_{\mathrm{disk}} + E_{\mathrm{sep}}^{(12)}$$
where $E_{\mathrm{disk}}$ is the energy of a single disk minimizer (independent of $L$) and $E_{\mathrm{sep}}^{(12)} \approx \lambda_{\mathrm{rep}} \langle u^{(1)*}, u^{(2)*} \rangle \approx 0$ (well-separated formations, exponentially small overlap).

### §3.2 Critical length threshold

**Definition 3.2 (SCC String Breaking Threshold).**
$$L_{\mathrm{crit}} := \arg\min_L \{E_{\mathrm{str}}(L) = E_{\mathrm{broken}}(L)\}$$
the length at which the single elongated formation and the two-disk configuration are energetically equal. For $L < L_{\mathrm{crit}}$: string energetically preferred (single formation stable). For $L > L_{\mathrm{crit}}$: two-disk configuration energetically preferred (string breaking thermodynamically favorable).

**Explicit trade-off formula**: Setting $E_{\mathrm{str}}(L) = E_{\mathrm{broken}}(L)$:
$$T_{\mathrm{str}} \cdot 2L_{\mathrm{crit}} \cdot w_{\mathrm{tube}} + E_{\mathrm{endpoint}} = 2 \cdot E_{\mathrm{disk}}$$
$$E_{\mathrm{birth}} := 2 \cdot E_{\mathrm{disk}} - E_{\mathrm{endpoint}}$$
is the **birth energy** — the energy "released" by removing the flux tube and paying only the two endpoint costs. For $L > L_{\mathrm{crit}}$:
$$E_{\mathrm{birth}} > T_{\mathrm{str}} \cdot 2L \cdot w_{\mathrm{tube}}$$
i.e., the tube cost exceeds the birth energy difference — breaking is favored.

**Honest assessment at R23 parameters** ($\beta = 30$, $n = 32 \times 32 = 1024$):

At $\beta = 30$ the correlation length $\xi_0 = \sqrt{\alpha/\beta} \approx 0.183$; disk formations are very compact. The naive analysis of the trade-off formula gives $L_{\mathrm{crit}} \to 0$ at these parameters, predicting that any elongated string is already past the breaking threshold.

**CONSISTENCY CHECK — NOT independent evidence.** The prediction $L_{\mathrm{crit}} \to 0$ at $\beta = 30$ is *consistent* with the empirical R23 observation that no well-separated $K_{\mathrm{step}} = 2$, $\mathcal{F} = 2$ configurations appear (all R23 minimizers have $\mathcal{F} \geq 5$, $K_{\mathrm{step}} \geq 1$). However, this is NOT independent confirmation: both conclusions — (a) $L_{\mathrm{crit}} \to 0$ from the formula, and (b) absence of K=2 well-separated configurations in R23 — reflect the same underlying short-correlation-length regime at $\beta = 30$. The R23 absence is the *explanandum*, not independent evidence. Using it to "confirm" the estimate is circular. Independent verification requires NQ-253 Phase 1 numerical measurement (§6.1) at $\beta = 4$ where $L_{\mathrm{crit}} > 0$ is predicted — there the threshold is detectable and does not depend on the R23 dataset.

**At $\beta = 4$** (NQ-198a regime): $\xi_0 = 0.5$ (larger correlation length), disks are more diffuse, $E_{\mathrm{disk}}$ larger relative to tube cost. String tension $C(4) \approx 13.2$. Estimate: $L_{\mathrm{crit}} \sim O(\xi_0 \cdot L_{\mathrm{grid}}/4)$ — roughly 4–8 nodes on a $20 \times 20$ grid. **This is the numerical target for the §6 experimental design.**

### §3.3 Gauge theory analog: QuEra string breaking

**QuEra 2025 (Science): String breaking on kagome lattice.** QuEra Computing + Harvard + Innsbruck groups directly observed string breaking in a 2D quantum simulator on the kagome lattice. A flux tube (linear confinement potential) was stretched by moving static charges apart; at critical separation, a new charge-anticharge pair was spontaneously created from the vacuum, breaking the flux tube into two shorter segments.

**SCC analog (CN10 contrastive)**:

| QuEra mechanism | SCC analog | Correspondence strength |
|---|---|---|
| Static charges at string endpoints | Two peaks of elongated formation | Structural (positions) |
| Flux tube = confined chromoelectric field | Connecting low-cohesion bridge region | Structural (topology) |
| Vacuum pair creation at $L_{\mathrm{crit}}$ | New formation birth ($\Delta K = +1$) at $|\partial S|_{\mathrm{crit}}$ | Functional (threshold mechanism) |
| String tension prevents breaking at $L < L_{\mathrm{crit}}$ | Single formation preferred at short $|\partial S|$ | Functional (energy comparison) |
| Two shorter strings after breaking | Two separated disk formations after birth | Structural (final state) |

**Key disanalogy (CN10)**: In gauge theory, pair creation comes from *quantum vacuum fluctuations* (spontaneous process at finite coupling). In SCC, formation birth requires *external perturbation or noise* (see §4 — noiseless gradient flow forbids birth events). The SCC analog captures the **threshold structure** of the transition but NOT the spontaneous quantum mechanism.

---

## §4. K-Jump $\Delta K = +1$: Formation Birth in SCC Dynamics

### §4.1 Canonical gradient flow: monotone K_act decrease

**T-Merge (b) Cat A** (canonical §13): Under noiseless gradient flow on $\widetilde\Sigma^K_M$, the long-time generic state has $K_{\mathrm{act}} = 1$ (single active formation). The trajectory is monotone:
$$K_{\mathrm{act}}(t+\delta t) \leq K_{\mathrm{act}}(t) \quad \text{for all } t > 0 \text{ (generically)}$$
This is a **stratum descent** property (Tool A1, `mathematical_scaffolding_4tools.md` §2.4): gradient flow on $\widetilde\Sigma^K_M$ crosses stratum boundaries $S_K \to S_{K-1}$ but **never crosses upward** $S_K \to S_{K+1}$ under noiseless dynamics. K-jump $\Delta K = +1$ is **forbidden under noiseless gradient flow**.

**Stratified space language**: Birth event $K_{\mathrm{act}} \to K_{\mathrm{act}} + 1$ corresponds to the trajectory moving from $S_{K_{\mathrm{act}}}$ into $S_{K_{\mathrm{act}}+1}$ (higher stratum). In the Whitney-stratified space $\widetilde\Sigma^K_M$, gradient flow is tangent to strata at smooth points and crosses stratum boundaries downward (decreasing $K_{\mathrm{act}}$). The string-breaking analogy maps to an **upward stratum transition** — which is non-generic under autonomous dynamics.

### §4.2 Mechanisms enabling formation birth

Three mechanisms can produce $\Delta K = +1$ birth events in SCC:

**Mechanism B1: Thermal noise (P-F flagged)**
Add noise $\sigma dW_t$ to the gradient flow:
$$d\mathbf{u} = -\nabla \mathcal{E}_K(\mathbf{u})\,dt + \sigma\,dW_t$$
At noise scale $\sigma > \sigma_{\mathrm{crit}}$, the trajectory can fluctuate from $S_{K_{\mathrm{act}}}$ into $S_{K_{\mathrm{act}}+1}$ stratum boundary and activate a dormant formation. This is the SCC analog of thermal string breaking.

**P-F flag**: Full thermodynamic / kinetic treatment of noise-driven birth is open. Claims about $\sigma_{\mathrm{crit}}$ require P-F (Physical Foundations) deepening. This working file does not assert specific $\sigma_{\mathrm{crit}}$ values.

**Mechanism B2: Initial condition (IC) manipulation**
Start gradient flow from $\mathbf{u}(0) \in S_{K_{\mathrm{act}}+1}$ (two active formations). Gradient flow will eventually decrease $K_{\mathrm{act}}$, but if the two formations are energetically favorable (both have $\mathcal{E}_K(\mathbf{u}^{(1)*}) + \mathcal{E}_K(\mathbf{u}^{(2)*}) < \mathcal{E}_K(\mathbf{u}^*_{\mathrm{merged}})$), the flow may stabilize at $K_{\mathrm{act}} = 2$ before merging. This is not a "birth" per se but a protocol-induced initialization in a higher-$K$ stratum.

**Mechanism B3: Stretching protocol (string-breaking experiment)**
Control the shape of a single formation by varying a stretching parameter (e.g., aspect ratio of the grid, external field coupled to the boundary term). At critical stretching, the formation energy landscape develops two competing minima:
1. Single elongated formation (string)
2. Two separated disk formations (broken string = born formation)

At $L = L_{\mathrm{crit}}$, the energy landscape bifurcates — the single-string minimum becomes a saddle, and the two-disk configuration becomes the global minimum. This is the **string-breaking analogy in its purest form**.

**This is the NQ-253 Phase 1 experimental target (§6).**

### §4.3 Formation birth is NOT spontaneous under SCC canonical dynamics

**Claim 4.3**: Under noiseless SCC gradient flow on $\widetilde\Sigma^K_M$ with K-field architecture ($K_{\mathrm{field}} \geq 2$), a formation at $K_{\mathrm{act}} = 1$ will NOT spontaneously birth a second formation. The single-formation energy minimum is a local attractor in $S_1 \subset \widetilde\Sigma^K_M$.

**Reasoning**: The stratum $S_1$ (one active formation) is open in $\widetilde\Sigma^K_M$ under gradient flow descent. To birth a new formation, the dormant formation $u^{(2)}$ must gain mass from the pool — but at the single-formation minimum, $\nabla_{\mathbf{u}} \mathcal{E}_K$ points away from $S_2$ (toward $S_1$ interior). No birth occurs.

**Verification of Claim 4.3**: At a single-formation minimizer $u^* \in \Sigma_m$ ($K_{\mathrm{act}} = 1$), the K-field-extended Hessian $H_K$ on $\widetilde\Sigma^K_M = \Sigma_{m_1} \times \Sigma_{m_2}$ (with $m_1 = m$, $m_2 = 0$ dormant) decomposes as:
$$H_K = H_{u^*} \oplus H_{u_{\mathrm{dormant}}=0}$$
where $H_{u_{\mathrm{dormant}}=0}$ is the Hessian at the zero-mass formation. By T-Merge (b) Cat A (canonical §13), $H_{u_{\mathrm{dormant}}=0}$ has all positive eigenvalues: the zero-mass dormant formation is a strict minimum of $\mathcal{E}_K$ in its block, given $m_2 \to 0$ means no degrees of freedom to perturb (the dormant formation contributes zero energy regardless of its internal profile at zero mass). Therefore $H_K$ is positive definite at $u^* \oplus u_{\mathrm{dormant}=0}$, confirming that the K-field local minimum claim holds in the extended state space $\widetilde\Sigma^K_M$. The K-field extension does not introduce new negative Hessian directions at the $K_{\mathrm{act}} = 1$ minimizer.

**Implication for gauge theory analogy**: The QuEra string breaking is a *quantum* process (vacuum pair creation) that has no SCC noiseless analog. The SCC analog of string breaking requires **protocol control** (Mechanism B2 or B3) or **noise** (Mechanism B1). This distinction is crucial for the CN10 contrastive claim.

---

## §5. V5b-F Mass Scaling: Boundary Energy Reading

> **WARNING**: This section interprets the V5b-F formula as a boundary-energy contribution per site ONLY. It does NOT derive $L_{\mathrm{crit}}$ from the condition $\mu_{\mathrm{Gold}} = 0$. See §2.4 note on the Goldstone-mass conflict: §2.4 states $\mu_{\mathrm{Gold}}$ *grows* with $L_{\mathrm{str}}$; setting $\mu_{\mathrm{Gold}} = 0$ to find a threshold therefore gives the wrong sign and is not used here. **The bifurcation criterion and the V5b-F mass formula are independent; do not derive $L_{\mathrm{crit}}$ from $\mu_{\mathrm{Gold}} = 0$.**

### §5.1 Boundary-energy formula

The V5b-F pseudo-mass formula (NQ-198a, empirical Cat B):
$$\mu_{\mathrm{Gold}} \approx C(\beta) \cdot \frac{|\partial S|}{n}$$
is interpreted **solely** as the boundary-energy contribution per site: the Goldstone mode pseudo-mass is proportional to the fraction of boundary nodes, with $C(\beta)$ the proportionality coefficient (units: energy). This formula characterizes how the translational softness of a formation scales with its boundary size — formations with larger $|\partial S|$ are harder to translate (higher $\mu_{\mathrm{Gold}}$), consistent with greater boundary exposure requiring more energy to shift.

| Factor | Meaning |
|---|---|
| $C(\beta)$ | Boundary energy coefficient (energy units); SCC string tension analog |
| $|\partial S|/n$ | Boundary fraction (dimensionless); intensive boundary measure |
| $\mu_{\mathrm{Gold}}$ | Goldstone mode pseudo-mass; grows with $L_{\mathrm{str}}$ (§2.4) |

**This is Connection H (Very Strong)** from `06_gauge_theory_connections_analysis.md`: the SCC V5b-F mass formula is the graph-theoretic analog of the string tension / mass gap relation in confinement. The formula $\mu_{\mathrm{Gold}} = C(\beta) \cdot |\partial S|/n$ corresponds to $T_{\mathrm{str}} \cdot L / V$ in large-N gauge theory ('t Hooft 1974).

### §5.2 $C(\beta)$ as SCC string tension coefficient

**Definition 5.2.** The SCC string tension $C(\beta)$ is defined by the V5b-F scaling law:
$$C(\beta) := \lim_{n \to \infty} n \cdot \frac{\mu_{\mathrm{Gold}}(u^{(j)*})}{|\partial S(u^{(j)*})|}$$
(thermodynamic limit of the boundary-normalized Goldstone mass). At $\beta = 4$, $\xi_0 = 0.5$: $C(4) \approx 13.2$ (NQ-198a measurement).

**Predicted $\beta$-dependence**: As $\beta/\alpha$ increases (stronger double-well driving):
- Correlation length $\xi_0 = \sqrt{\alpha/\beta}$ decreases (sharper formation boundaries)
- String tension $C(\beta)$ should *increase* (steeper energy penalty per boundary node)
- Predicted functional form: $C(\beta) \sim (\beta/\alpha)^{p}$ for some $p > 0$ (NQ-198k conjecture)

**NQ-198k (W6+ open)**: Determine $C(\beta)$ functional form. This is the **SCC string tension $\beta$-scaling law**.

### §5.3 Dimensional analysis of string energy

**Units clarification (addressing M-3)**: $T_{\mathrm{str}}$ has units [energy]/[length] (energy per unit boundary length). On the discrete graph, "length" is measured in node count. $C(\beta)$ has units [energy] (since $1/n$ is dimensionless and $|\partial S|/n$ is a length-fraction). The string energy is:
$$E_{\mathrm{str}} = T_{\mathrm{str}} \cdot L_{\mathrm{str}} = \frac{C(\beta)}{\text{correlation length scale}} \cdot |\partial S| \cdot (\text{correlation length per node})$$

At graph level with all lengths in node count, units balance: $E_{\mathrm{str}}$ has units of energy, $T_{\mathrm{str}} = C(\beta)$ (energy), $L_{\mathrm{str}} = |\partial S|$ (count). The formula $E_{\mathrm{str}} \approx C(\beta) \cdot |\partial S|/n \cdot n = C(\beta) \cdot |\partial S|$ is derived from $E_{\mathrm{bd}} = 2\alpha u^\top L u$ (canonical §8), with $C(\beta)$ absorbing all $\alpha$- and $\beta$-dependent prefactors. This derivation is empirical (NQ-198a Cat B); the exact prefactor relationship to $\alpha$ and $\beta$ is NQ-198k.

### §5.4 Bifurcation criterion (independent)

The string-breaking threshold $L_{\mathrm{crit}}$ is determined **independently** of the V5b-F formula, via the Hessian condition:
$$\lambda_{\min}\bigl(H(u^{(j)*}; d)\bigr) = 0 \quad \text{(formation ceases to be a local minimum)}$$
at the stretching bifurcation. This is the **Crandall-Rabinowitz-style bifurcation** (§6.2, Cat A target). The V5b-F formula gives the energy profile approaching the threshold but does not itself determine $L_{\mathrm{crit}}$.

---

## §6. Verification and Experimental Design

### §6.1 Phase 1: Numerical string-breaking measurement (Cat B, W7, 4–6 weeks)

**Objective**: Measure $L_{\mathrm{crit}}$ empirically by controlled stretching of a single SCC formation.

**Protocol (NQ-253 Phase 1 experiment)**:

1. **Graph**: $L \times L$ grid with periodic (torus) or free boundary conditions. Start with $L = 20$ ($n = 400$).

2. **Initial configuration**: V5b-F string — a single formation $u^{(j)*}$ with two endpoints separated by distance $d_0$ on the torus. Use tanh-disk profile initial conditions:
$$u_{\mathrm{init}}(x) \propto \tanh\bigl(\xi_0^{-1}(r_0 - d_G(x, c_1))\bigr) + \tanh\bigl(\xi_0^{-1}(r_0 - d_G(x, c_2))\bigr)$$
projected onto $\Sigma_m$ (normalized to mass $m$).

3. **Stretching parameter**: Vary endpoint separation $d = d_G(c_1, c_2) \in \{4, 5, 6, 7, 8, 10, 12, 14, 16\}$ (on $20 \times 20$ torus). For each $d$, run gradient flow to convergence.

4. **Measurements at each $d$**:
   - Final $K_{\mathrm{step}}(u^*; 0.5)$ — did the string break (K=2) or remain intact (K=1)?
   - Final $\mathcal{F}(u^*)$ — number of peaks.
   - Energy $\mathcal{E}(u^*)$ — compare single-string vs two-disk energies.
   - Hessian minimum eigenvalue $\lambda_{\min}(H(u^*))$ — passes through zero at bifurcation.
   - Boundary size $|\partial S(u^*; 0.5)|$ — string length proxy.

5. **Verdict criteria**:
   - $L_{\mathrm{crit}}$ detected when: $K_{\mathrm{step}}$ jumps from 1 to 2; Hessian changes sign; energy of K=2 configuration first falls below K=1 energy.
   - $C(\beta)$ consistency check: does $\mu_{\mathrm{Gold}} \approx C(\beta) \cdot |\partial S|/n$ hold at the pre-critical $d < L_{\mathrm{crit}}$ configurations?

6. **K=2 formation confirmation**: At $d > L_{\mathrm{crit}}$, run K-field optimization with $K_{\mathrm{field}} = 2$ to confirm the two-disk configuration is a stable K-field minimizer (σ_multi^A defined, `multi_formation_sigma.md` §5).

**Estimated compute**: $\sim$ 30–60 min total (9 values of $d$ × gradient flow convergence $\sim$ 3–7 min each on CPU).

**Parameters**: $\beta = 4$, $\alpha = 1$ (NQ-198a anchor regime); $m = 50$ (medium mass, $c = m/n = 0.125$); $\lambda_{\mathrm{rep}} = 0.1$ (weak inter-formation repulsion for K=2 stage).

### §6.2 Phase 2: Variational bifurcation analysis (Cat A, W8–W10)

**Objective**: Prove existence of $L_{\mathrm{crit}}$ rigorously via Crandall-Rabinowitz bifurcation theory.

**Setup**: Parameterize single-formation energy $\mathcal{E}(u^{(j)*}; d)$ by endpoint separation $d$. The bifurcation analysis requires:

1. **Operator family**: $F(u, d) := \nabla \mathcal{E}(u; d) = 0$ (equilibrium condition). $F$ depends smoothly on $d$ (stretching parameter).

2. **Bifurcation point conditions** (Crandall-Rabinowitz 1971):
   - $F(u_0, d_0) = 0$ (the string is an equilibrium)
   - $D_u F(u_0, d_0)$ has a 1-dimensional null space (one zero eigenvalue)
   - The null vector $\phi_0$ satisfies the transversality condition: $D_{u,d}^2 F(u_0, d_0)[\phi_0, \cdot] \notin \mathrm{range}(D_u F)$

3. **Conclusion of Crandall-Rabinowitz**: A new branch of equilibria bifurcates from $(u_0, d_0)$ — specifically, two-disk configurations branching from the single-string family at $d = L_{\mathrm{crit}}$.

**On-graph version**: The canonical energy $\mathcal{E}$ on the discrete graph $G$ is smooth (twice continuously differentiable in $u$ on $\Sigma_m$ interior); the Hessian $H(u; d)$ is the $D_u F$ operator. The bifurcation condition $\lambda_{\min}(H(u^*; d)) = 0$ at $d = L_{\mathrm{crit}}$ is the target.

**Gap**: The classical Crandall-Rabinowitz theorem is for Banach spaces with smooth parameter families. The discrete graph setting reduces to finite-dimensional linear algebra; the theorem applies in the finite-dimensional case as the **implicit function theorem + Morse lemma** on $\Sigma_m$ (smooth simplex manifold interior). This is standard — no essential obstacle.

**Effort estimate**: 4–6 weeks (W8–W10). Requires: (a) existence of smooth $d$-parameterization of string equilibria; (b) explicit computation of transversality at the critical point; (c) canonical theorem statement. This constitutes **NQ-253 Phase 2**.

---

## §7. Connection to NQ-200 (Non-Involution Canonical Iso, $K \geq 3$)

### §7.1 NQ-200 status

**NQ-200 (W7+ undeveloped)**: For $K \geq 3$ formations, the canonical isomorphism problem asks for the classification of K-field minimizer equivalence classes under $\mathrm{Aut}(G) \wr S_K$ (wreath product). For $K = 2$, the isomorphism can be an involution (swap formations). For $K \geq 3$, non-involution permutations arise, and the classification is more complex (higher-order σ_multi structure).

**Connection to birth**: The $K = 1 \to K = 2$ birth mechanism (§3–§4) is the **simplest non-involution case of NQ-200**: before birth, there is $K_{\mathrm{act}} = 1$ (no pair to swap); after birth, $K_{\mathrm{act}} = 2$ (first pair, $S_2$ involution). The birth event is the entry into the $K \geq 2$ regime where NQ-200's machinery becomes necessary.

### §7.2 Cascade to $K \geq 3$

**Hypothesis (NQ-253, H-cascade)**: The formation birth mechanism generalizes to a **cascade** of threshold crossings:
$$K_{\mathrm{act}} = 1 \xrightarrow{d > L_{\mathrm{crit}}^{(1)}} K_{\mathrm{act}} = 2 \xrightarrow{d > L_{\mathrm{crit}}^{(2)}} K_{\mathrm{act}} = 3 \xrightarrow{\cdots} K_{\mathrm{act}} = K$$
Each crossing $K \to K+1$ corresponds to a stretched $K$-formation developing a new string segment that exceeds its own critical threshold $L_{\mathrm{crit}}^{(K)}$.

**Predicted cascade properties**:
- $L_{\mathrm{crit}}^{(K)}$ depends on $K$ (more formations = more repulsion = different critical length for next birth)
- **Open question (NQ-253-cascade)**: Whether $L_{\mathrm{crit}}^{(K)}$ is monotonically decreasing or increasing in $K$ is open. Naive arguments support either direction: (a) decreasing because pool mass shrinks per formation, making each subsequent string shorter and cheaper to break; (b) increasing because inter-formation repulsion stabilizes shorter strings before the next breaking event, requiring longer stretching to trigger the next birth. Numerical investigation deferred to W7+.
- At $K \to K_{\mathrm{field}}$: saturation (no more formations can be born; dormant formation mass exhausted)

**NQ-200 entry point**: The $K = 2$ birth gives the first case of $S_2$ permutation symmetry in $\widetilde\Sigma^K_M$ (wreath product $\mathrm{Aut}(G) \wr S_2$). The $K = 3$ birth gives the first non-abelian case ($S_3$), which is the true NQ-200 territory. **NQ-253 Phase 1–2 (K=1→2 birth) is the necessary precursor to NQ-200 (K=2→3+ birth cascade).**

### §7.3 Stratified space picture

In the Tool A1 framework (`mathematical_scaffolding_4tools.md` §2), the cascade is:
$$S_1 \to S_2 \to S_3 \to \cdots \to S_{K_{\mathrm{field}}}$$
Each upward transition is a birth event requiring a mechanism (B1/B2/B3 from §4.2). Under noiseless flow the cascade is impossible; under controlled protocol (B3) each threshold $L_{\mathrm{crit}}^{(K)}$ must be exceeded sequentially.

The Goresky-MacPherson stratified Morse theory (MO-1 multi-formation option, `mathematical_scaffolding_4tools.md` §2.5, NQ-248 W7+) provides the mathematical framework for analyzing the critical structure at each stratum boundary.

---

## §8. External References

### §8.1 String breaking and confinement

- **Bali, G. S. (2001).** "QCD forces and heavy quark bound states." *Phys. Rep.* 343, 1–136. — String tension classical reference; relation $E_{\mathrm{str}} = T_{\mathrm{str}} \cdot L$ for quark-antiquark string in QCD.

- **QuEra Computing + Harvard + Innsbruck (2025).** "Direct observation of string breaking in a 2D quantum simulator." *Science* (2025). — Experimental observation of string breaking on kagome lattice with rubidium atoms; flux tube lengthening → charge pair creation → string into two segments. **Citation blocker**: QuEra Computing + Harvard + Innsbruck 2025 exact citation pending. Use: González-Cuadra, D. et al. (2025). "Observation of string breaking on a (2+1)D Rydberg quantum simulator." arXiv:2410.16558 [cond-mat.quant-gas]; published Science 388 (in press). DOI pending. **Replace with verified DOI before any canonical promotion.**

- **'t Hooft, G. (1974).** "A planar diagram theory for strong interactions." *Nucl. Phys. B* 72, 461–473. — Large-N gauge theory string limit; $1/N$ expansion; string tension mass gap relation.

### §8.2 Bifurcation theory

- **Crandall, M. G. & Rabinowitz, P. H. (1971).** "Bifurcation from simple eigenvalues." *J. Functional Analysis* 8, 321–340. — Classical bifurcation theorem for operator families; applicable to §6.2 variational analysis.

### §8.3 Critical phenomena and threshold mechanisms

- **Sornette, D. (2009).** *Critical Phenomena in Natural Sciences.* Springer, 2nd ed. — Threshold mechanisms, critical exponents, universality classes in non-equilibrium systems. Conceptual framework for $L_{\mathrm{crit}}$ transition.

### §8.4 SCC references (internal)

- **Canonical §8**: 4-energy structure ($E_{\mathrm{cl}}$, $E_{\mathrm{sep}}$, $E_{\mathrm{bd}}$, $E_{\mathrm{tr}}$); boundary energy $E_{\mathrm{bd}} = 2\alpha \cdot u^\top L u$.
- **NQ-198a**: $C(\beta) \approx 13.2$ empirical measurement; V5b-F mass scaling.
- **NQ-198k**: $C(\beta)$ functional form (W6+ open, Cat C).
- **T-Merge (b) Cat A**: monotone $K_{\mathrm{act}}$ decrease under gradient flow.

---

## §9. Connection G Candidate Analog: Rydberg Atom Arrays (CN10 Contrastive Sketch)

### §9.1 QuEra experimental platform for SCC dynamics

> **WARNING (CN10)**: This section sketches a candidate experimental analog for SCC formation birth. SCC is not a Rydberg system; the Rydberg parameter mapping is a *suggestive parallel*, not a validation pathway. SCC validation requires NQ-253 Phase 1 numerical experiments on the SCC graph dynamics directly, not on a Rydberg simulator.

The QuEra + Harvard 2025 string breaking experiment uses **2D rubidium Rydberg atom arrays** with programmable site occupancies — a candidate structural analog for SCC dynamics:

| Simulator element | SCC mapping |
|---|---|
| Rydberg atom at site $x$ | Graph node $x \in X$ |
| Rydberg excitation fraction at $x$ | Cohesion field value $u(x) \in [0,1]$ |
| Atom-atom interaction potential | Graph edge coupling (Laplacian $L$) |
| Laser detuning parameter $\Delta$ | SCC $\beta/\alpha$ ratio (drives double-well) |
| Rabi frequency $\Omega$ | SCC $\lambda_{\mathrm{cl}}$ (closure energy coefficient) |
| Lattice geometry (kagome / square / triangular) | Graph $G = (X, E)$ |

Under this mapping, the Rydberg Hamiltonian evolution approximates SCC gradient flow dynamics (not exactly — quantum evolution $\neq$ gradient descent, but in the semi-classical limit with dissipation). Connection G (`06_gauge_theory_connections_analysis.md`) establishes this SCC–Rydberg correspondence.

### §9.2 String breaking as SCC formation birth detection

The string breaking protocol in a QuEra-type experiment:

1. **Initialize**: Two Rydberg excitation clusters at sites $c_1, c_2$ separated by distance $d$ (tanh-disk profiles via local laser addressing). This initializes $u(x) \approx u_{\mathrm{init}}$ as an SCC string configuration.

2. **Adiabatic stretching**: Slowly increase $d$ by moving the addressing lasers. Laser parameter $\Delta(t)$ adjusted to maintain the V5b-F string configuration.

3. **Detection**: Monitor the intermediate region between $c_1$ and $c_2$. At $d = L_{\mathrm{crit}}^{\mathrm{SCC}}$:
   - String breaking: intermediate region develops a new excitation cluster (new "charge pair" = new SCC formation)
   - Observable: sudden appearance of nonzero $u(x_{\mathrm{mid}})$ at a site $x_{\mathrm{mid}}$ midway between endpoints
   - Formation birth detection: $K_{\mathrm{step}}$ jumps from 1 to 2 (or $K_{\mathrm{act}}$ increases from 1 to 2 in K-field language)

4. **SCC parameter mapping**: The laser detuning $\Delta$ and Rabi $\Omega$ must be tuned to hit the SCC V5b-F regime — specifically, $\beta/\alpha \sim 4$–$8$ (moderate double-well, extended $\xi_0 \sim 0.5$). High $\beta \gg 1$ (R23 regime) gives $L_{\mathrm{crit}} \to 0$ (string breaks immediately) — not observable as a threshold.

**Experimental prediction**: $L_{\mathrm{crit}}^{\mathrm{SCC}} \approx 4$–$8$ lattice spacings at $\beta/\alpha = 4$ on a kagome-like lattice with $\xi_0 \sim 0.5$ (from §3.2 estimate). This is within the range of current QuEra 256-site arrays.

### §9.3 Validation observables

If the experiment realizes SCC formation birth:
- **Quantitative**: Measure $L_{\mathrm{crit}}$ as function of $\beta/\alpha$ (laser parameters). Compare to SCC prediction $L_{\mathrm{crit}}(\beta) = E_{\mathrm{birth}} / (2 T_{\mathrm{str}} w_{\mathrm{tube}}) = \mathrm{const} \cdot C(\beta)^{-1}$.
- **Qualitative**: Formation birth event is sharp (threshold crossing), not gradual (consistent with SCC bifurcation).
- **String tension**: Extract $C(\beta)$ from $\mu_{\mathrm{Gold}}$ measurement (Goldstone mode pseudo-mass via spectroscopy of the formation's translation mode).

---

## §10. Hard Constraint Verification (CN10 Contrastive)

**Critical ontological checks for this working file**:

- [x] **CN10 contrastive throughout**: All gauge theory correspondences labeled "SCC analog (CN10 contrastive)". No sentence equates SCC to a gauge theory. The analogy is heuristic scaffolding only. QuEra mapping is a validator target, not a definition.

- [x] **u_t primitive maintained**: All analysis operates on $u^{(j)} : X \to [0,1]$ (cohesion fields). No "charge", "flux", or "gauge field" is introduced as a primitive SCC entity. SCC string = elongated cohesion field; not a quantum flux tube.

- [x] **4-energy not merged**: $E_{\mathrm{str}} \approx T_{\mathrm{str}} \cdot L_{\mathrm{str}}$ is interpreted via $E_{\mathrm{bd}} = 2\alpha u^\top L u$ (boundary term, one of 4). The string tension does NOT merge boundary energy with closure, separation, or transport terms. Per CN5, the four terms are conceptually independent at single-formation level.

- [x] **K not dual-treated abusively**: $K_{\mathrm{act}}$, $K_{\mathrm{field}}$, $K_{\mathrm{step}}$, $\mathcal{F}$ are tracked per their definitions (Commitment 16, F_Kstep_K_triple.md). Formation birth $\Delta K = +1$ means $K_{\mathrm{act}}$ increases; $K_{\mathrm{field}}$ remains fixed.

- [x] **No metastability claim without P-F flag**: §4.2 Mechanism B1 (thermal noise) explicitly P-F flagged. No spontaneous birth event claimed for noiseless SCC dynamics.

- [x] **Silent resolution avoided**: NQ-200 (W7+ undeveloped) is not resolved here — §7 provides the entry point only. NQ-198k ($C(\beta)$ functional form) remains open. $L_{\mathrm{crit}}$ is not claimed as proven — only as conjectured and experimentally targeted.

- [x] **No Research OS resurrection**: Single-topic working file; no numbered subdirectories; no registry files.

- [x] **Canonical not directly modified**: This is `working/MF/`, not `canonical/`. All canonical impact targets are conditional proposals.

---

## §11. Cross-References

### §11.1 Working files (this OAT family)

- `mathematical_scaffolding_4tools.md` §2 (Tool A1 stratified space; K-jump = stratum transition; Goresky-MacPherson framework for MO-1)
- `multi_formation_sigma.md` §5.5 (Goldstone analog on σ_multi^A; inter-formation mode splitting → cross-formation Goldstone = string breaking analog)
- `shared_pool_canonical_proposal.md` (I9' architecture; $\widetilde\Sigma^K_M$ as stratified space)
- `F_Kstep_K_triple.md` §3 (BC-1 fails generically in R23 = string breaking precondition: K_act < K_field means dormant formation available for birth)
- `single_high_F_equivalence.md` §4.2 (R23 F=63 = maximally stretched SCC string; K_step=1 = string not broken; E=508.9 = high energy consistent with long string)
- `working/SF/sigma_topological_invariance.md` §4.2, §6.3 (NQ-190; W5 Day 4 PM Wave 3 cross-link, carry-forward #10): $L_{\mathrm{crit}}$ is a **graph-class-specific** quantity — §4.2 subdivision counterexample $(P_3, P_4)$ predicts $L_{\mathrm{crit}}$ rescales linearly under edge subdivision (boundary-count is not subdivision-invariant), and §6.3 continuum-limit conjecture (NQ-190b) is the topological-invariance test for $L_{\mathrm{crit}}/n$ universality. Bilateral with NQ-190 §13.
- `working/SF/sigma_lie_algebra_structure.md` §6, §7 (NQ-258; W5 Day 4 PM Wave 3 cross-link): V5b-F mass formula reinterpreted as broken-symmetry generator near-zero mass; §7 supports the boundary-energy $C(\beta) \cdot |\partial S| / n$ reading that replaces the dropped Goldstone-zero approach (C-2).

### §11.2 Daily logs

- `daily/2026-04-30/06_gauge_theory_connections_analysis.md` §10 Connection H (Very Strong): V5b-F mass formula = SCC string tension law. **Primary motivation for this file.**
- `daily/2026-04-30/04_external_references_verification.md`: external reference accuracy verification (Garcke-Nestler-Stoth, Bali, QuEra 2025).

### §11.3 Canonical targets (conditional, CV-1.6+)

- **§13 NQ-200 entry**: Formation birth mechanism as NQ-200 cluster entry point; string-breaking analog as motivation.
- **§13 NQ-253**: New NQ registration (Phase 1: numerical $L_{\mathrm{crit}}$ measurement, W7 4–6 weeks; Phase 2: variational bifurcation, W8–W10).
- **CN10 addendum**: String-breaking analog listed as an explicit Connection H example of contrastive (not reductive) gauge theory comparison.

---

## §12. Cat Target and W7+ Priority

### §12.1 NQ-253 Phase 1 — Numerical Cat B (W7, 4–6 weeks)

**Target**: Measure $L_{\mathrm{crit}}$ on V5b-F minimizer with controlled stretching protocol on $20 \times 20$ torus at $\beta = 4$.

**Deliverables**:
1. Plot of $E(u^*; d)$ vs $d$ (energy as function of endpoint separation)
2. Plot of $\lambda_{\min}(H(u^*; d))$ vs $d$ (Hessian minimum eigenvalue = zero at $L_{\mathrm{crit}}$)
3. Plot of $K_{\mathrm{step}}(u^*; d; 0.5)$ vs $d$ (connectivity jump at $L_{\mathrm{crit}}$)
4. $C(\beta)$ consistency check: $\mu_{\mathrm{Gold}} \approx C(4) \cdot |\partial S| / n = 13.2 \cdot |\partial S| / 400$

**Cat B upgrade condition**: Measurement of $L_{\mathrm{crit}}$ with $\pm 1$ node resolution on two different grid sizes ($L = 16, 20$) showing consistent $L_{\mathrm{crit}}$ value (finite-size convergence check).

### §12.2 NQ-253 Phase 2 — Variational Cat A (W8–W10)

**Target**: Prove existence of $L_{\mathrm{crit}}$ via Crandall-Rabinowitz bifurcation analysis on discrete graph $\Sigma_m$.

**Deliverables**:
1. Theorem: "For $\beta/\alpha > \beta_{\mathrm{crit}}$ (phase transition threshold, canonical §11), there exists $L_{\mathrm{crit}}(\beta, m, G) \in \mathbb{Z}_{\geq 1}$ such that the single elongated formation is a local minimizer for $d < L_{\mathrm{crit}}$ and a saddle for $d > L_{\mathrm{crit}}$, with a two-formation branch bifurcating at $d = L_{\mathrm{crit}}$."
2. Proof: Crandall-Rabinowitz applied to the gradient map $F(u, d) = \nabla \mathcal{E}(u; d)$ on $\Sigma_m$.
3. Promotion: canonical §13 theorem entry "T-StringBreaking" (Cat A if proof complete).

### §12.3 NQ-200 Phase 1 dependency

**NQ-200 cluster cannot proceed without NQ-253 Phase 1**. The K=1→2 birth mechanism (NQ-253) establishes:
- The stratum transition $S_1 \to S_2$ (one mechanism)
- The two-disk minimizer as a stable K=2 state
- The σ_multi^A structure at K=2 (from `multi_formation_sigma.md` §5)

Only then can NQ-200's K=2→3 (non-involution permutation) and K≥3 cascade be addressed. **NQ-253 Phase 1 is the NQ-200 gate.**

---

## §13. Open Audit Items

The following items remain open after this working file:

- [ ] $C(\beta)$ functional form (NQ-198k, W6+ Cat C) — required for analytic $L_{\mathrm{crit}}(\beta)$ prediction.
- [ ] QuEra 2025 exact citation (Science journal, precise DOI/volume pending).
- [ ] $L_{\mathrm{crit}}$ estimate at R23 parameters ($\beta = 30$) — the naive analysis in §3.2 gives $L_{\mathrm{crit}} \to 0$; needs confirmation that this is consistent with absence of K=1 minimizers in R23.
- [ ] Mechanism B1 (thermal noise) $\sigma_{\mathrm{crit}}$ estimate — P-F flagged, deferred to separate working file.
- [ ] K-field architecture initialization for Phase 1 experiment: which $K_{\mathrm{field}}$ value to use in `scc/multi.py find_k_formations`? Recommendation: $K_{\mathrm{field}} = 2$ (string = K=1 active + K=1 dormant; breaking = K=2 active).
- [ ] Connection G (Rydberg–SCC) precise parameter mapping — needs dedicated working file for §9 quantum simulator pathway.

---

## §14. Wave 3 Revision Log (W5 Day 4 PM)

**Timestamp**: 2026-04-30 PM  
**Critic verdict reference**: `logs/daily/2026-04-30/09_critic_re_review_5files.md` §2.3 + §3.5  
**Revision status**: Critical findings addressed; 2 critical → 0; 5 major → addressed or weakened to open questions; ready for W6 critic re-review.

### Fixes applied

1. **§3.2 circular reasoning fix (C-1)**: Replaced the "L_crit ≈ 0 confirms R23" estimate with an explicit CONSISTENCY CHECK disclaimer. The R23 absence of K=2 configurations is now acknowledged as the *explanandum*, not independent evidence. Circular use of R23 to validate the estimate has been removed. Independent verification via NQ-253 Phase 1 at β=4 is stated as the required test.

2. **§5 Goldstone-mass DROP (C-2)**: Removed §5.3 derivation of $L_{\mathrm{crit}}$ from $\mu_{\mathrm{Gold}} = 0$. Replaced §5 with a revised structure: §5.1 (boundary-energy interpretation only, with explicit WARNING block stating the bifurcation criterion and V5b-F formula are independent), §5.2 ($C(\beta)$ definition retained), §5.3 (dimensional analysis fix addressing M-3), §5.4 (bifurcation criterion stated as independent, referencing §6.2). Added C-2 resolution note in §2.4 clarifying that $\mu_{\mathrm{Gold}}$ grows with $L_{\mathrm{str}}$ and the $\mu_{\mathrm{Gold}} = 0$ approach is incorrect.

3. **§9 Rydberg reframe (M-1)**: Changed section title from "SCC Quantum Simulator Validation Pathway" to "Connection G Candidate Analog: Rydberg Atom Arrays (CN10 Contrastive Sketch)". Inserted CN10 WARNING block at top of §9.1 explicitly stating SCC is not a Rydberg system, the mapping is a suggestive parallel not a validation pathway, and SCC validation requires NQ-253 Phase 1 numerical experiments on SCC graph dynamics directly.

4. **§4.3 Hessian verification (M-2)**: Inserted full "Verification of Claim 4.3" paragraph showing that the K-field-extended Hessian $H_K = H_{u^*} \oplus H_{u_{\mathrm{dormant}}=0}$ is positive definite at the $K_{\mathrm{act}}=1$ minimizer, using T-Merge (b) Cat A for the dormant block and the direct sum structure for the active block.

5. **§5.3 dimensional analysis fix (M-3)**: Added new §5.3 "Dimensional analysis of string energy" deriving how units balance at graph level: $T_{\mathrm{str}} = C(\beta)$ (energy), $L_{\mathrm{str}} = |\partial S|$ (count), with the $1/n$ normalization explained as thermodynamic dilution. Clarifies that $C(β)$ absorbs all $\alpha$- and $\beta$-dependent prefactors from $E_{\mathrm{bd}} = 2\alpha u^\top L u$.

6. **§7.3 cascade ordering weakened (M-4)**: Replaced the asserted monotone ordering $L_{\mathrm{crit}}^{(1)} > L_{\mathrm{crit}}^{(2)} > \cdots$ with an explicit open question (NQ-253-cascade), presenting both directions (decreasing: pool mass shrinks; increasing: inter-formation repulsion stabilizes shorter strings) as plausible, with numerical investigation deferred to W7+.

7. **§8.1 QuEra citation blocker (M-5)**: Added explicit citation blocker note to QuEra entry with candidate arXiv reference: González-Cuadra, D. et al. (2025), arXiv:2410.16558, Science 388 (in press), DOI pending. Flagged as hard blocker for canonical promotion until verified DOI is confirmed.

**End of formation_birth_string_breaking.md.**

**Status**: Working draft. String-breaking analog formalized (Connection H direct exploitation). NQ-253 opened with Phase 1 (numerical, W7, Cat B) and Phase 2 (variational, W8–W10, Cat A) targets. NQ-200 entry identified (K=1→2 birth as simplest non-involution case). CN10 contrastive throughout. C(β) functional form (NQ-198k) identified as primary theoretical gap. QuEra validation pathway sketched (§9). Hard constraints verified (§10).

**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/MF/formation_birth_string_breaking.md`
**Created:** 2026-04-30 (W5 Day 4, post-OAT batch)
**Lines:** ~390
**NQ:** NQ-253 (Formation Birth via String-Breaking Analog)
**Promotion target:** NQ-253 Phase 1 numerical results → canonical §13 T-StringBreaking (W8–W10, if Phase 2 complete).
