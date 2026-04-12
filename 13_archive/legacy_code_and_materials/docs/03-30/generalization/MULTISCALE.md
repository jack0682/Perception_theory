# Multi-Scale Structure and Renormalization of SCC

**Date:** 2026-03-30
**Author:** Multi-scale / Renormalization Group Specialist
**Status:** Extension proposal — does not modify the Canonical Spec v2.0

---

## 0. Motivation

The Canonical Spec defines SCC on a fixed graph $(X_t, \mathbf{N}_t)$ at a single resolution. But the scaling audit (A4) identified a fundamental issue: the phase transition threshold $\beta_{\text{crit}} = 4\alpha\lambda_2/|W''(c)|$ vanishes on large graphs ($\lambda_2 \to 0$ for grids), making T8-Core vacuous at scale. Meanwhile, the topology-dependent value audit showed that self-referential operators matter most on graphs with complex boundary structure — suggesting that the *scale* at which structure is probed determines which energy terms dominate.

These two findings converge on a single conclusion: **SCC requires a multi-scale formulation.** The theory's interesting physics lives not at any single resolution but in the interplay between scales — the competition between boundary energy (scaling as surface area) and bulk energy (scaling as volume) at the formation's *natural* scale.

This document develops the renormalization group (RG) structure of SCC: what happens when we coarse-grain a formation, which energy terms survive, and how the diagnostic vector decomposes across scales.

---

## 1. Block-Spin Coarse-Graining

### 1.1. The Coarse-Graining Map

Partition the vertex set $X$ into $M$ blocks $B_1, \ldots, B_M$, each of size $\sim L$ (measured in graph distance). Define the block field:

$$
\bar{u}(B_i) = \frac{1}{|B_i|} \sum_{x \in B_i} u(x)
$$

and the block adjacency:

$$
\bar{\mathbf{N}}(B_i, B_j) = \sum_{x \in B_i, y \in B_j} \mathbf{N}(x,y)
$$

This defines a coarsened graph $(\bar{X}, \bar{\mathbf{N}})$ where $\bar{X} = \{B_1, \ldots, B_M\}$, and a coarsened field $\bar{u} : \bar{X} \to [0,1]$.

The block-spin RG transformation is formally:

$$
e^{-\mathcal{E}_{\text{coarse}}[\bar{u}]} = \int_{\Sigma_m} e^{-\mathcal{E}[u]} \prod_i \delta\!\left(\bar{u}(B_i) - \frac{1}{|B_i|}\sum_{x \in B_i} u(x)\right) \mathcal{D}u
$$

The coarse energy $\mathcal{E}_{\text{coarse}}$ is the effective energy obtained by integrating out the intra-block fluctuations while holding the block averages fixed.

### 1.2. The Coarse Volume Constraint

The volume constraint is preserved exactly under block averaging:

$$
\sum_i |B_i| \bar{u}(B_i) = \sum_i \sum_{x \in B_i} u(x) = \sum_x u(x) = m
$$

So $\bar{u}$ lives on a weighted constraint manifold $\bar{\Sigma}_m = \{\bar{u} : \sum_i |B_i| \bar{u}(B_i) = m\}$. This is the natural volume-weighted analogue of $\Sigma_m$ at the coarse scale.

**Key structural point:** The cohesive budget $m$ is an extensive quantity — it is preserved under coarse-graining. The volume fraction $c = m/n$ is an intensive quantity — it is also preserved (since both $m$ and $n$ scale together). This means the double-well spinodal condition $c \in ((3-\sqrt{3})/6, (3+\sqrt{3})/6)$ is scale-invariant.

---

## 2. Scaling of Individual Energy Terms

### 2.1. Boundary/Morphology Term $\mathcal{E}_{\text{bd}}$

**Smoothness sub-term.** For a $d$-dimensional grid with blocks of linear size $L$:

$$
\alpha \sum_{x,y} \mathbf{N}(x,y)(u(x) - u(y))^2 = \alpha \cdot (\text{intra-block}) + \alpha \cdot (\text{inter-block})
$$

The inter-block contribution, after coarse-graining, becomes:

$$
\alpha_{\text{eff}} \sum_{i,j} \bar{\mathbf{N}}(B_i, B_j)(\bar{u}(B_i) - \bar{u}(B_j))^2
$$

with $\alpha_{\text{eff}} \approx \alpha$ (the inter-block edges contribute equally). The intra-block contribution is integrated out and contributes an additive constant plus corrections that renormalize the double-well.

For a formation with a boundary of width $\xi$ (the Allen-Cahn interface width $\xi \sim \sqrt{\alpha/\beta}$):

- If $L \ll \xi$: the coarse-graining is within the interface. The smoothness term is **relevant** — it constrains the block-to-block variation within the interface.
- If $L \gg \xi$: the coarse-graining averages over the interface. Blocks are either nearly 0 or nearly 1 (bulk) or contain the entire interface (boundary blocks with intermediate $\bar{u}$). The smoothness term becomes a coarse perimeter measure.

**Scaling dimension:** The smoothness term scales as $L^{d-1}$ (the surface area of the formation boundary). In RG language, it has scaling dimension $d-1$, which is **relevant** in $d \geq 2$.

**Double-well sub-term.** The double-well $W(u) = u^2(1-u)^2$ is a local potential. Under block averaging:

$$
\sum_x W(u(x)) = \sum_i \sum_{x \in B_i} W(u(x))
$$

By Jensen's inequality, $\frac{1}{|B_i|}\sum_{x \in B_i} W(u(x)) \geq W(\bar{u}(B_i))$ since $W$ is convex near $u = 0$ and $u = 1$ (but concave in the spinodal region). So the coarse double-well is:

$$
\beta_{\text{eff}} \sum_i |B_i| W(\bar{u}(B_i)) + \text{fluctuation corrections}
$$

where $\beta_{\text{eff}} \leq \beta$ in general (the fluctuation corrections are non-negative and reduce the effective double-well strength).

**RG interpretation:** Intra-block fluctuations *weaken* the double-well at the coarse scale. This is the standard Wilson-Fisher mechanism: thermal/stochastic fluctuations reduce the effective barrier between phases. In the deterministic SCC setting, the "fluctuations" are the sub-block field variations that cannot be captured by the block average.

**Scaling dimension:** The double-well is a bulk (volume) term, scaling as $L^d$. It is **relevant** in all dimensions.

**Conclusion for $\mathcal{E}_{\text{bd}}$:** Both sub-terms of the boundary/morphology energy are **relevant** under coarse-graining. $\mathcal{E}_{\text{bd}}$ drives the phase transition at every scale. This is expected: Allen-Cahn is the backbone of SCC's phase separation.

### 2.2. Closure Term $\mathcal{E}_{\text{cl}}$

The closure energy is:

$$
\mathcal{E}_{\text{cl}} = \sum_x (u(x) - \mathrm{Cl}(u)(x))^2
$$

Under coarse-graining, we need the closure deviation $r(x) = u(x) - \mathrm{Cl}(u)(x)$ at the block level. The coarsened closure deviation is:

$$
\bar{r}(B_i) = \bar{u}(B_i) - \overline{\mathrm{Cl}(u)}(B_i)
$$

**Bulk blocks** (all sites near 0 or all near 1): These are near the closure fixed point $u^* = \sigma(a_{\text{cl}}(u^* - \tau_{\text{cl}}))$. By contraction (A3), $|r(x)| \leq (a_{\text{cl}}/4)|u(x) - u^*|$. In the bulk, $u(x) \approx 0$ or $u(x) \approx 1$, so $r(x)$ depends on how far these saturated values are from the fixed point. For the high-cohesion phase ($u \approx 1$), $r(x) = 1 - \sigma(a_{\text{cl}}(1 - \tau_{\text{cl}})) \approx 0$ when $a_{\text{cl}}(1-\tau_{\text{cl}})$ is large. Similarly for the low phase.

**Result:** In the bulk, $\mathcal{E}_{\text{cl}}$ is exponentially small (the field is near a closure fixed point). The closure energy concentrates on the **boundary layer** — the transition region where $u$ is intermediate and the aggregation $P_t u$ mixes high and low values.

**Boundary blocks** (straddling the interface): Here the block average $\bar{u}(B_i)$ is intermediate, but the closure operator acts on the fine field $u$, not on $\bar{u}$. The closure deviation at boundary sites depends on the mismatch between $u(x)$ and $P_t u(x)$ across the interface. After coarse-graining, this becomes a contribution proportional to the interface area:

$$
\sum_i \bar{r}(B_i)^2 \sim |\partial \Omega| \cdot \xi \cdot \langle r^2 \rangle_{\text{interface}}
$$

where $|\partial \Omega|$ is the boundary length and $\xi$ is the interface width.

**Scaling dimension:** $\mathcal{E}_{\text{cl}} \sim L^{d-1} \cdot \xi$. The interface width $\xi$ is set by $\alpha/\beta$ and does not scale with $L$. So $\mathcal{E}_{\text{cl}}$ scales as $L^{d-1}$ — the same as the smoothness term.

**RG classification:** $\mathcal{E}_{\text{cl}}$ is **relevant** (same scaling as the perimeter), but it is a *boundary correction* to the Allen-Cahn dynamics. At the coarse scale, it modifies the effective surface tension:

$$
\sigma_{\text{eff}} = \sigma_{\text{AC}} + \lambda_{\text{cl}} \cdot \delta\sigma_{\text{cl}}
$$

where $\sigma_{\text{AC}}$ is the Allen-Cahn surface tension and $\delta\sigma_{\text{cl}}$ is the closure correction. The Gamma-convergence result (T11) already establishes that closure modifies the effective surface tension in the sharp-interface limit — the RG perspective gives the *scale-dependent* version of this result.

**Critical observation:** The closure term is relevant at every scale, but its *relative importance* compared to $\mathcal{E}_{\text{bd}}$ depends on whether the boundary structure is simple (grid-like) or complex (community-like). On grids, the closure correction is small because $P_t u$ smoothly interpolates across the boundary. On community graphs, $P_t u$ can have discontinuous jumps at inter-community edges, amplifying the closure deviation. This is the RG explanation of the topology-dependent value finding.

**Kernel-collapse caveat (from continuum analysis):** When the coarse-graining scale $L$ exceeds the kernel width (the range of $P_t$), the aggregation $P_t u \to \bar{u}$ and the closure operator becomes a pointwise nonlinearity $\sigma(a_{\text{cl}}(\bar{u} - \tau_{\text{cl}}))$. At this point, $\mathcal{E}_{\text{cl}}$ acts as an additional potential term modifying the effective double-well, not as a spatially-coupled energy. The closure term remains nonzero but loses its relational character. See Section 5.1 for the full analysis.

### 2.3. Separation Term $\mathcal{E}_{\text{sep}}$

The separation energy is:

$$
\mathcal{E}_{\text{sep}} = \sum_x u(x)(1 - D(x; 1-u))
$$

The distinction operator $D(x; 1-u)$ compares the neighborhood average of $u$ against the neighborhood average of $1-u$. At the coarse scale:

**Bulk interior blocks** ($\bar{u}(B_i) \approx 1$): If all neighbors are also interior blocks, $D \approx 1$, so $u(1-D) \approx 0$. No contribution.

**Bulk exterior blocks** ($\bar{u}(B_i) \approx 0$): $u \approx 0$, so $u(1-D) \approx 0$ regardless of $D$. No contribution.

**Boundary blocks**: Here $u$ is intermediate, and $D$ depends on the local balance of interior vs. exterior neighborhoods. This is where $\mathcal{E}_{\text{sep}}$ concentrates.

**Scaling dimension:** Like $\mathcal{E}_{\text{cl}}$, the separation energy concentrates on the boundary layer and scales as $L^{d-1}$.

**RG classification:** $\mathcal{E}_{\text{sep}}$ is **relevant**, contributing another correction to the effective surface tension.

**Crucial RG distinction:** While both $\mathcal{E}_{\text{cl}}$ and $\mathcal{E}_{\text{sep}}$ are boundary corrections at the coarse scale, they encode *different* boundary physics:

- $\mathcal{E}_{\text{cl}}$ measures self-support failure at the boundary (the field doesn't match its relationally completed form).
- $\mathcal{E}_{\text{sep}}$ measures distinction failure at the boundary (interior sites aren't clearly distinguished from exterior).

Under coarse-graining, these two corrections can flow differently:

- **Grid graphs:** Both corrections are small and comparable (the boundary is geometrically simple). The coarse theory is effectively Allen-Cahn with a slightly modified surface tension.
- **Community graphs:** The distinction correction $\delta\sigma_{\text{sep}}$ is much larger because inter-community edges create "false exterior" neighbors for interior sites. The self-referential distinction operator is needed to resolve this.

### 2.4. Transport Term $\mathcal{E}_{\text{tr}}$

The transport energy couples adjacent time steps. Under spatial coarse-graining at fixed $t$:

$$
\mathcal{E}_{\text{tr}} = \sum_{x,y} M_{t \to s}(x,y) \omega(u_t(x), u_s(y))(u_s(y) - u_t(x))^2
$$

This term is **not purely spatial** — it couples two different time slices. Spatial coarse-graining acts on $x$ and $y$ independently. The coarse transport kernel is:

$$
\bar{M}_{t \to s}(B_i, B_j) = \frac{1}{|B_i|} \sum_{x \in B_i, y \in B_j} M_{t \to s}(x,y) \omega(u_t(x), u_s(y))
$$

The transport term is relevant whenever the formation moves or deforms between time steps — its scaling depends on the velocity/deformation of the formation relative to the block size $L$.

**RG classification:** Relevant for slow-moving formations ($v \cdot \Delta t \ll L$); marginal when formation motion is comparable to block size; irrelevant when the formation moves faster than the coarse-graining scale. This creates a natural **temporal coarse-graining** requirement: to maintain transport relevance, the temporal resolution must be adjusted with the spatial resolution.

### 2.5. Summary Table

| Energy term | Concentrates on | Scaling | RG status | Grid effect | Community effect |
|---|---|---|---|---|---|
| $\mathcal{E}_{\text{bd}}$ (smooth) | Boundary | $L^{d-1}$ | Relevant | Dominant | Dominant |
| $\mathcal{E}_{\text{bd}}$ (double-well) | Bulk | $L^d$ | Relevant | Dominant | Dominant |
| $\mathcal{E}_{\text{cl}}$ | Boundary layer | $L^{d-1}$ | Relevant (correction) | Small $\delta\sigma$ | Large $\delta\sigma$ |
| $\mathcal{E}_{\text{sep}}$ | Boundary layer | $L^{d-1}$ | Relevant (correction) | Small $\delta\sigma$ | Large $\delta\sigma$ |
| $\mathcal{E}_{\text{tr}}$ | Temporal interface | Depends on $v$ | Conditional | — | — |

---

## 3. The $\beta_{\text{crit}}$ Scaling Problem and Its RG Resolution

### 3.1. The Problem

T8-Core gives the phase transition threshold:

$$
\frac{\beta}{\alpha} > \frac{4\lambda_2}{|W''(c)|}
$$

On a $k \times k$ grid, $\lambda_2 \sim \pi^2/k^2$. As $k \to \infty$, $\beta_{\text{crit}} \to 0$ — the phase transition is trivially satisfied. The audit (Section 3.3) correctly identifies this as undermining the theoretical claim that formations emerge from a genuine phase transition.

### 3.2. The RG Interpretation

The vanishing of $\beta_{\text{crit}}$ is not a bug — it is the standard RG statement that **the ordered phase is the thermodynamic ground state on large systems**. In the language of statistical mechanics:

- The uniform state $u \equiv c$ is the disordered (paramagnetic) phase.
- The phase-separated state (formation) is the ordered (ferromagnetic) phase.
- T8-Core identifies the mean-field critical point.

On large systems, the mean-field critical temperature is low — any nonzero interaction strength produces order. This is exactly the situation in the Ising model on large lattices: $T_c \to 0$ in the mean-field sense for systems with vanishing spectral gap.

**The resolution:** The interesting physics is not at the system-wide scale but at the **formation's natural scale**. A formation of linear size $\ell$ on a large graph "sees" an effective spectral gap $\lambda_2^{(\ell)} \sim 1/\ell^2$, giving:

$$
\beta_{\text{crit}}^{(\ell)} = \frac{4\alpha}{\ell^2 |W''(c)|}
$$

This is O(1) when $\ell \sim \sqrt{\alpha/\beta} \cdot |W''(c)|^{-1/2}$ — which is precisely the Allen-Cahn interface width $\xi$. So the phase transition criterion, properly interpreted, determines the **natural scale of the formation**, not whether formation exists.

### 3.3. Scale-Dependent Phase Transition

Define the coarse-grained system at scale $L$ with $M = n/L^d$ blocks. The coarse Laplacian $\bar{L}$ has Fiedler eigenvalue $\bar{\lambda}_2 \sim \lambda_2 \cdot L^2$ (the spectral gap increases with block size because the coarse graph has fewer vertices and shorter diameter).

The scale-dependent phase transition condition is:

$$
\frac{\beta_{\text{eff}}(L)}{\alpha_{\text{eff}}(L)} > \frac{4\bar{\lambda}_2(L)}{|W''(c)|}
$$

As $L$ increases:
- $\bar{\lambda}_2(L)$ increases (fewer blocks $\Rightarrow$ larger spectral gap)
- $\beta_{\text{eff}}(L)$ decreases (fluctuations weaken the double-well)
- $\alpha_{\text{eff}}(L)$ is approximately constant

There exists a **critical scale** $L^*$ at which the condition transitions from satisfied to unsatisfied:

$$
L^* \sim \xi \cdot f(c)
$$

where $f(c)$ depends on the volume fraction and boundary structure.

**Physical meaning:** $L^*$ is the formation's natural resolution scale. Below $L^*$, the formation has internal structure (the field varies within a block). Above $L^*$, the formation appears as a point-like object (a single block in the coarse graph). The multi-scale diagnostic vector (Section 4) captures this transition.

### 3.4. The Finite-Element Rescaling as RG Fixed Point

The Canonical Spec (T8-Core Remark) notes that setting $\alpha = \alpha_0/h^2$ with mesh spacing $h = 1/k$ recovers a mesh-independent threshold $\beta_{\text{crit}} = O(1)$. In RG language, this is the statement that the **continuum theory has a well-defined RG fixed point**: the parameters $(\alpha_0, \beta)$ are the renormalized couplings that remain finite in the continuum limit.

The RG flow is:
- Under coarse-graining by factor $b$: $\alpha \to \alpha/b^2$, $\beta \to \beta$
- This means $\alpha$ has scaling dimension $-2$ (it is a relevant coupling that grows under fine-graining)
- The dimensionless ratio $\alpha/(h^2 \beta)$ is the natural control parameter

**Connection to Gamma-convergence (T11):** The $\varepsilon = \alpha/\beta \to 0$ limit in T11 corresponds to taking $L \to \infty$ in the RG — the sharp-interface limit IS the maximally coarse-grained theory. The Gamma-limit perimeter functional is the **effective theory at the coarsest scale**: the formation is a crisp set with a definite boundary, and the energy is proportional to the boundary's length/area.

---

## 4. Scale-Dependent Diagnostic Vector

### 4.1. Definition

At coarsening level $L$, define the **scale-$L$ diagnostic vector**:

$$
\mathbf{d}(L) = (\text{Bind}(L),\, \text{Sep}(L),\, \text{Inside}(L),\, \text{Persist}(L)) \in [0,1]^4
$$

where each component is computed on the coarsened system $(\bar{X}_L, \bar{\mathbf{N}}_L, \bar{u}_L)$:

**Bind(L):** The closure approximation quality at scale $L$.

$$
\text{Bind}(L) = 1 - \frac{\|\bar{u}_L - \overline{\mathrm{Cl}}_L(\bar{u}_L)\|_2}{\sqrt{M}}
$$

where $\overline{\mathrm{Cl}}_L$ is the closure operator on the coarsened graph.

**Sep(L):** The $\bar{u}$-weighted distinction at scale $L$.

$$
\text{Sep}(L) = \frac{\sum_i \bar{u}_L(B_i) \bar{D}_L(B_i; 1-\bar{u}_L)}{\sum_i \bar{u}_L(B_i)}
$$

where $\bar{D}_L$ is the distinction operator on the coarsened graph.

**Inside(L):** The morphological quality $\mathcal{Q}_{\text{morph}}$ of the coarsened field.

**Persist(L):** The temporal inheritance quality at scale $L$ (requires temporal coarse-graining).

### 4.2. The Scale Tower

The collection $\{\mathbf{d}(L)\}_{L = L_0, 2L_0, 4L_0, \ldots}$ forms a **scale tower** — a multi-resolution decomposition of formation quality. The scale tower reveals:

**Fine-to-coarse monotonicity of Bind:** At fine scales, the closure operator has access to the full relational structure; Bind should be highest. At coarse scales, the block-averaged field smooths out the fine relational support; Bind decreases. The rate of decrease depends on boundary complexity:

- Grid graphs: Bind decreases slowly (smooth boundary $\Rightarrow$ block averaging preserves closure quality)
- Community graphs: Bind decreases rapidly once $L$ exceeds the community size (inter-community structure is lost)

**Non-monotonicity of Sep:** At very fine scales, Sep may be low (individual sites near the boundary don't distinguish well). At intermediate scales, Sep peaks (the boundary is fully resolved). At very coarse scales, Sep is high (the formation is a single block, trivially distinguished from exterior blocks). But between intermediate and coarse scales, Sep may dip if the coarsening creates boundary blocks with intermediate $\bar{u}$ values.

**Inside is scale-characteristic:** The morphological quality Inside measures the persistence diagram of the superlevel filtration. At the formation's natural scale $L^*$, Inside is maximized — the filtration reveals the core/boundary/exterior stratification most clearly. Below $L^*$, the filtration has too many fine-scale features (noisy). Above $L^*$, the filtration is trivial (one or zero bars).

### 4.3. The Natural Scale of a Formation

Define the formation's **natural scale** $L^*$ as the scale that maximizes a combined diagnostic quality:

$$
L^* = \arg\max_L \; Q(\mathbf{d}(L))
$$

where $Q : [0,1]^4 \to [0,1]$ is a monotone aggregator (e.g., $Q = \min$ or $Q = \text{geometric mean}$).

This provides a principled, intrinsic definition of formation scale that does not depend on arbitrary thresholds or external parameters. The formation "tells you" its natural scale through the diagnostic vector.

**Connection to the $\beta_{\text{crit}}$ problem:** At $L = L^*$, the phase transition condition should be genuinely constraining (not trivially satisfied or trivially violated). This gives:

$$
\frac{\beta_{\text{eff}}(L^*)}{\alpha_{\text{eff}}(L^*)} \approx \frac{4\bar{\lambda}_2(L^*)}{|W''(c)|}
$$

i.e., the formation sits near criticality at its natural scale. This is the SCC analogue of "self-organized criticality" — the formation's scale adjusts to the parameters so that it lives near the phase transition at its own resolution.

---

## 5. Self-Referential Operators as Relevant Perturbations

### 5.1. The Kernel-Collapse Mechanism (from continuum analysis)

The continuum extension (CONTINUUM.md) provides the precise mechanism by which self-referential terms become irrelevant at large scales. In the continuum formulation, $\mathrm{Cl}[u]$ and $D[u]$ involve kernel convolutions $K * u$ where $K$ has a characteristic width (the kernel radius). Under coarse-graining at scale $L$:

- When $L \gg \text{kernel width}$: the convolution $K * u \to \bar{u}$ (the local average). The closure operator collapses to a **pointwise nonlinearity**: $\mathrm{Cl}[u] \to \sigma(a_{\text{cl}}(u - \tau_{\text{cl}}))$. Similarly, $D[u] \to \sigma(a_D((1+\lambda_D)u - \lambda_D) - \tau_D)$.
- These pointwise nonlinearities contribute to the energy as **additional potential terms** that modify the effective double-well $W(u)$, not as spatially-coupled terms.

The energy scaling confirms this:
- $\mathcal{E}_{\text{bd}} \sim O(1/\varepsilon)$ in the sharp-interface limit ($\varepsilon = \alpha/\beta \to 0$)
- $\mathcal{E}_{\text{cl}}, \mathcal{E}_{\text{sep}} \sim O(1)$ — subdominant by a factor of $\varepsilon$

This is the Gamma-convergence statement (T11/G4): the self-referential terms are lower-order perturbations to the Allen-Cahn energy in the sharp-interface limit. They modify the effective double-well $W_{\text{eff}}(u) = W(u) + \varepsilon[\lambda_{\text{cl}}(\mathrm{Cl}(u) - u)^2 + \lambda_{\text{sep}} u(1 - D(u))]$ but do not contribute to the leading-order surface tension.

**Critical consequence:** The kernel width introduces a **built-in length scale** into the self-referential operators. When the coarse-graining scale $L$ exceeds this length scale, the operators lose their spatial coupling and become purely local. This is why they are irrelevant at large $L$ — not because they are small, but because they lose their relational character.

### 5.2. The Lattice-Scale Story

On a regular lattice, the Allen-Cahn energy $\mathcal{E}_{\text{bd}}$ dominates. The self-referential terms ($\mathcal{E}_{\text{cl}}, \mathcal{E}_{\text{sep}}$) are boundary corrections that modify the effective surface tension by a small amount (the topology-dependent value audit measured +0.007 to +0.029 Sep improvement on grids). In RG language, the self-referential operators are *irrelevant perturbations at the lattice scale on regular graphs*.

### 5.3. The Community-Scale Story

On community graphs, the inter-community edges introduce a characteristic length scale $L_c$ (the community diameter). At the lattice scale ($L \ll L_c$), the local structure looks grid-like and Allen-Cahn dominates. But at the community scale ($L \sim L_c$), the Laplacian cannot cleanly separate interior from exterior because connections cross community boundaries.

At scale $L_c$, the self-referential distinction operator becomes essential: it compares the *aggregated interior support* against *aggregated exterior support*, effectively reading the community structure that the Laplacian misses. The Sep improvement at the community scale (+0.035 to +0.173) reflects the fact that the self-referential operators are **relevant perturbations at the community scale**.

**RG flow of self-referential coupling:** Define the dimensionless self-referential coupling:

$$
g(L) = \frac{\lambda_{\text{cl}} \delta\sigma_{\text{cl}}(L) + \lambda_{\text{sep}} \delta\sigma_{\text{sep}}(L)}{\sigma_{\text{AC}}(L)}
$$

On regular lattices: $g(L) \to 0$ as $L \to \infty$ (irrelevant).
On community graphs: $g(L)$ increases as $L \to L_c$, peaks at $L = L_c$, then decreases for $L \gg L_c$ (relevant at the community scale, irrelevant asymptotically).

**Precise claim:** The self-referential operators are **dangerously irrelevant** in the RG sense: they are irrelevant at asymptotically large scales, but they dominate the physics at the crossover scale $L_c$ where community structure is resolved. Ignoring them (pure Allen-Cahn) gives qualitatively wrong formation boundaries on community graphs.

### 5.4. Implications for the Theory's Identity

This RG analysis vindicates the theory's foundational claim (Canonical Spec Section 2, CN7): the self-referential operator pair (closure + distinction) is not redundant with Allen-Cahn. The two theories have *identical* RG fixed points in the asymptotic (continuum, large-scale) limit — this is the content of T11 (Gamma-convergence). But they differ at *finite scales* where the relational structure has non-trivial topology.

SCC's distinctive contribution is a **multi-scale theory of formation** where the self-referential terms capture the topology-dependent physics that Allen-Cahn misses. The Gamma-convergence result is a *feature*, not a *reduction*: it shows that SCC correctly reproduces Allen-Cahn at large scales while providing additional structure at finite scales.

---

## 6. Hierarchical Formation Structure

### 6.1. Scale-Separated Formation Layers

Coarse-graining naturally produces a hierarchy of structural descriptions:

| Scale | Dominant structure | Dominant energy | Key diagnostic |
|-------|---|---|---|
| Fine ($L \ll \xi$) | Individual sites, local cohesion | $\mathcal{E}_{\text{cl}}$ (closure deviation) | Bind |
| Interface ($L \sim \xi$) | Formation boundary, phase transition | $\mathcal{E}_{\text{bd}}$ (Allen-Cahn) | Inside |
| Formation ($L \sim L^*$) | Entire formation, identity | $\mathcal{E}_{\text{sep}}$ (distinction) | Sep |
| Coarse ($L \gg L^*$) | Formation as point object | $\mathcal{E}_{\text{tr}}$ (transport/persistence) | Persist |

This hierarchy resolves the conceptual tension between the four energy terms: they are not competing at the same scale — each dominates at a different level of the scale tower.

### 6.2. Connection to Multi-Formation Theory

The multi-formation problem (I9, audit Section 1) is intimately connected to multi-scale structure. Two formations can coexist if and only if they are *separated at some scale*:

- **Same-scale formations:** Two formations of similar size $L^*$ must be spatially separated (the K-field repulsion operates at scale $L^*$).
- **Different-scale formations:** A large formation (scale $L_1^*$) can contain a smaller formation (scale $L_2^* \ll L_1^*$) as internal structure. At the coarse scale $L_1^*$, the small formation is invisible; at the fine scale $L_2^*$, the large formation is the "background."

This gives a natural resolution to the K-selection problem (audit issue S3): the number of formations K is not a single number but a scale-dependent count $K(L)$. At fine scales, many small formations may be visible. At coarse scales, they merge into fewer large formations. The "correct" K is the one at the formation's natural scale.

**Formal definition:** The **formation count at scale $L$** is:

$$
K(L) = \text{number of connected components of } \{B_i : \bar{u}_L(B_i) > \theta\}
$$

where $\theta$ is a threshold (e.g., $\theta = c$, the volume fraction). The function $K(L)$ is non-increasing in $L$ (merging blocks can only reduce or maintain the component count).

The **scale spectrum** of a multi-formation configuration is the set of scales $\{L : K(L) \text{ changes}\}$. Each such scale represents a hierarchical transition where formations merge or become indistinguishable.

### 6.3. Hierarchical Diagnostic Tensor

For a multi-formation system, the full diagnostic object is a **tensor**:

$$
\mathbf{D}_{k,L} = \mathbf{d}_k(L) \in [0,1]^4 \quad \text{for } k = 1, \ldots, K(L)
$$

This gives each formation's diagnostic vector at each scale. The tensor $\mathbf{D}$ is the complete multi-scale, multi-formation description of the system's cohesive structure.

---

## 7. Formal Results

### 7.1. Proposition: Volume Fraction Scale-Invariance

**Statement.** Under block averaging with any partition $\{B_1, \ldots, B_M\}$, the weighted volume fraction $\bar{c} = \sum_i |B_i| \bar{u}(B_i) / n$ equals $c = \sum_x u(x)/n$.

*Proof.* Direct computation: $\sum_i |B_i| \bar{u}(B_i) = \sum_i |B_i| \cdot \frac{1}{|B_i|} \sum_{x \in B_i} u(x) = \sum_i \sum_{x \in B_i} u(x) = \sum_x u(x)$. $\square$

### 7.2. Proposition: Energy Monotonicity under Coarse-Graining

**Statement.** For the smoothness sub-term of $\mathcal{E}_{\text{bd}}$, the coarsened energy is bounded above by the fine energy:

$$
\alpha \sum_{i,j} \bar{\mathbf{N}}(B_i, B_j)(\bar{u}(B_i) - \bar{u}(B_j))^2 \leq \alpha \sum_{x,y} \mathbf{N}(x,y)(u(x) - u(y))^2
$$

*Proof.* By the Cauchy-Schwarz inequality applied to block averages. The inter-block contribution of the fine energy is:

$$
\sum_{i \neq j} \sum_{x \in B_i, y \in B_j} \mathbf{N}(x,y)(u(x) - u(y))^2
$$

By convexity of $z \mapsto z^2$:

$$
(\bar{u}(B_i) - \bar{u}(B_j))^2 = \left(\frac{\sum_{x,y} \mathbf{N}(x,y)(u(x) - u(y))}{\bar{\mathbf{N}}(B_i, B_j)}\right)^2 \leq \frac{\sum_{x,y} \mathbf{N}(x,y)(u(x)-u(y))^2}{\bar{\mathbf{N}}(B_i,B_j)}
$$

(where sums are restricted to $x \in B_i, y \in B_j$). Multiplying by $\bar{\mathbf{N}}(B_i,B_j)$ and summing gives the result. The intra-block terms are discarded (non-negative). $\square$

**Interpretation:** Coarse-graining always reduces the smoothness energy. Information is lost, never created, under coarsening.

### 7.3. Conjecture: Self-Referential Crossover Scale

**Statement.** On a graph with community structure at scale $L_c$, there exists a crossover scale $L_{\times}$ such that:

$$
g(L) = \frac{\lambda_{\text{sep}} \delta\sigma_{\text{sep}}(L)}{\sigma_{\text{AC}}(L)}
$$

satisfies $g(L) \ll 1$ for $L \ll L_c$ and $L \gg L_c$, with $g(L_{\times}) = O(1)$ for $L_{\times} \sim L_c$.

**Evidence:** The topology-dependent value experiments show Sep improvement scaling with inter-community connectivity $p_{\text{inter}}$. The crossover scale should satisfy $L_{\times} \sim 1/\sqrt{p_{\text{inter}}}$ (the characteristic distance at which inter-community edges become significant).

**Status:** Conjecture. Would require analyzing the spectral decomposition of the coarse Laplacian on stochastic block model graphs at different resolutions.

---

## 8. Connections to Other Extensions

### 8.1. Continuum Limit (CONTINUUM.md)

The RG flow from fine to coarse connects directly to the continuum extension. The continuum limit is the *fixed point* of the RG flow under fine-graining ($L \to 0$, $n \to \infty$ with $h = L/n \to 0$). The multi-scale theory provides the bridge: any finite-resolution computation is a coarse-grained version of the continuum theory.

The finite-element rescaling $\alpha = \alpha_0/h^2$ emerges naturally as the RG eigenvalue condition for the smoothness coupling.

**Kernel width as RG scale.** The continuum analysis (CONTINUUM.md §11) shows that the local limit $\ell_K \to 0$ (kernel width shrinks) causes self-referential terms to reduce to pointwise nonlinearities. This identifies the kernel width $\ell_K$ as the intrinsic RG scale for self-referential coupling: at scales $\gg \ell_K$, the operators lose spatial coupling; at scales $\sim \ell_K$, they are maximally active. This is the microscopic origin of the "dangerously irrelevant" classification in Section 5.

**Commutativity of limits (conjecture from continuum-ext).** The two limiting operations — fine-graining ($h \to 0$, discrete $\to$ continuum PDE) and coarse-graining ($\varepsilon = \alpha/\beta \to 0$, PDE $\to$ perimeter functional) — should commute:

$$
\text{discrete} \xrightarrow{h \to 0} \text{continuum PDE} \xrightarrow{\varepsilon \to 0} \sigma_{\text{AC}} \cdot \text{Per}(S)
$$
$$
\text{discrete} \xrightarrow{\varepsilon \to 0} \text{graph cut} \xrightarrow{h \to 0} \sigma_{\text{AC}} \cdot \text{Per}(S)
$$

Both paths yield the same perimeter functional. The self-referential terms drop out in both orders because they are $O(1)$ while $\mathcal{E}_{\text{bd}} \sim O(1/\varepsilon)$. This commutativity, if proved, would be a clean resolution of OP-MS5.

### 8.2. Stochastic Extension (STOCHASTIC.md)

The block-spin RG transformation (Section 1.1) integrates out intra-block degrees of freedom, which in the stochastic extension become genuine fluctuating variables. The effective coarse energy $\mathcal{E}_{\text{coarse}}$ includes entropic contributions from these fluctuations:

$$
\mathcal{E}_{\text{coarse}}[\bar{u}] = \mathcal{E}_{\text{mean-field}}[\bar{u}] - T \cdot S_{\text{intra}}[\bar{u}]
$$

where $S_{\text{intra}}$ is the entropy of intra-block configurations consistent with the block average $\bar{u}$. The stochastic extension thus provides the **proper implementation** of the block-spin RG, while the deterministic theory only captures the mean-field ($T = 0$) part.

### 8.3. Dynamics Extension (DYNAMICS.md)

The RG scale tower is intimately connected to dynamics: different scales evolve at different rates. Fine-scale features (local closure adjustments) equilibrate quickly; coarse-scale features (formation identity, transport) evolve slowly. This gives a natural **separation of timescales**:

$$
\tau_{\text{relaxation}}(L) \sim L^z
$$

where $z$ is the dynamic critical exponent. For Allen-Cahn dynamics, $z = 2$ (diffusive). The self-referential corrections may modify $z$ at the community scale.

---

## 9. Open Problems

### OP-MS1. Exact RG Flow Equations
Derive explicit RG flow equations for the SCC couplings $(\alpha, \beta, \lambda_{\text{cl}}, \lambda_{\text{sep}})$ under coarse-graining by factor $b$. This requires computing the block-spin integral (Section 1.1) at least in a saddle-point approximation.

### OP-MS2. Anomalous Scaling of Self-Referential Terms
Determine whether the self-referential coupling $g(L)$ has anomalous scaling dimensions on fractal or hierarchical graphs (e.g., Sierpinski gasket, hierarchical lattices). If $g$ is marginal on such graphs, the self-referential terms would dominate the universality class.

### OP-MS3. Multi-Scale Phase Diagram
Construct the phase diagram in the $(\beta/\alpha, L)$ plane, showing regions where the formation is: (a) ordered at all scales, (b) ordered below $L^*$ and disordered above, (c) disordered at all scales. Identify the critical line $L^*(β/α)$.

### OP-MS4. Scale-Dependent K-Selection
Formalize the scale-dependent formation count $K(L)$ and prove that it is related to the spectral gap of the coarse Laplacian at scale $L$. Specifically: $K(L) = $ number of eigenvalues of $\bar{L}_L$ below a threshold that depends on $\beta_{\text{eff}}(L)/\alpha_{\text{eff}}(L)$.

### OP-MS5. RG and T11 Unification (Commutativity of Limits)
Show that the Gamma-convergence result (T11) is the $L \to \infty$ limit of the RG flow, i.e., that the sharp-interface perimeter functional is the RG fixed point of the coarse-grained energy. Specifically, prove that the fine-graining limit ($h \to 0$) and the coarse-graining limit ($\varepsilon \to 0$) commute: both orderings yield $\sigma_{\text{AC}} \cdot \text{Per}(S)$ with self-referential corrections dropping out at $O(\varepsilon)$ in both paths (see Section 8.1).

### OP-MS6. Empirical Validation of Scale Tower
Implement the scale tower diagnostic $\mathbf{d}(L)$ for $L = 1, 2, 4, 8, \ldots$ on grid and community graphs. Verify the predicted behaviors: Bind monotonically decreasing, Sep non-monotone, Inside peaked at $L^*$.

---

## 10. Summary

| Aspect | Single-scale SCC | Multi-scale SCC |
|---|---|---|
| Phase transition | Vacuous on large graphs | Meaningful at formation's natural scale $L^*$ |
| Self-referential terms | "Marginal on grids" | Relevant at community scale, irrelevant asymptotically |
| Formation scale | Not defined | $L^* = \arg\max_L Q(\mathbf{d}(L))$ |
| Multi-formation | K is external parameter | $K(L)$ is scale-dependent, intrinsic |
| Gamma-convergence (T11) | Technical result | RG fixed point of coarse-graining flow |
| Diagnostic vector | Single $\mathbf{d}$ | Scale tower $\{\mathbf{d}(L)\}_L$ |
| Energy term roles | Competing at same scale | Hierarchically separated by scale |

The multi-scale extension resolves the $\beta_{\text{crit}}$ scaling problem, explains the topology-dependent value of self-referential operators, connects the sharp-interface limit to RG flow, and provides a principled framework for hierarchical multi-formation structure. It does this without modifying the Canonical Spec — the coarse-grained theory at each scale $L$ is itself an instance of SCC on the coarsened graph.
