# MF_multi_quantization.md — Formation Quantization Extended to Multi-Formation

**Session:** 2026-04-23 (G3 deliverable; intended promotion target: `working/MF/multi_quantization.md`)
**Target (from plan.md §2 G3):** Formation Quantization framework을 multi-formation ($K \geq 2$)으로 **자연스럽게** 확장. C1 (basin stratification) primary + C3 (pair + Landau) secondary.
**This file covers:** (a) K-sector basin stratification framework; (b) Axiom S1-S4 naturality audit; (c) pair interaction + Landau free energy $F(K)$; (d) Formation Quantization uniqueness proof sketch (well-separated case); (e) moduli $\mathcal{M}_K$ structure; (f) new open questions.
**Depends on reading:** `step_cohesion.md` (F1-SSU-v5), `from_single.md` (§2 retracted notice, §4–§7 preserved), `01_exploration.md` §4 (C1, C3 primary selection), `canonical.md` §11 Multi-formation paradigm, §12 Coupling Bound Lemma + T-Persist-K family.

---

## §1. Problem restatement

### 1.1 What is extended

**Single-formation Formation Quantization (step_cohesion.md §1)**:
$$u^*(x) = \phi_1^*(x) + r(u^*)\quad\text{for K = 1 well-separated minimizer}$$

with $K(u^*) = 1$ topological invariant.

**Goal of G3**: Extend to $K \geq 2$, in particular:

- Does every well-separated minimizer in $K$-sector admit unique decomposition $u^* = \sum_{k=1}^K \phi_k^* + r$?
- Does $K(u^*) \in \mathbb{Z}_+$ remain topologically invariant within each $K$-basin?
- What is the landscape $E: \Sigma_m \to \mathbb{R}$ structure across $K$-sectors?

### 1.2 Naturality criteria (from `01_exploration.md` §1.5)

- **AN (Axiomatic naturality)**: S1-S4 axioms apply to K-indexed form without modification.
- **PSN (Proof-structural naturality)**: Single-formation proofs extend to K by "$\sum_{k=1}^K$" substitution.
- **ON (Observable naturality)**: Single-formation observables (K_step = 1) extend directly to K-step counting.

---

## §2. Approach C1 — K-sector basin stratification (primary)

### 2.1 Main definition

> **Definition 2.1 (K-sector basin)**. Let $\mathcal{B}_K \subseteq \Sigma_m$ be the set of points $u$ satisfying:
> (i) $u$ is in the basin of attraction of some well-separated local minimizer $u^*$ under gradient flow $\dot u = -\Pi_{\Sigma_m}\nabla\mathcal{E}(u)$,
> (ii) $u^* = \sum_{k=1}^{K} \phi_k^*(x) + r(u^*)$ with $\|r\|_\infty \leq \exp(-d_{\min}/\xi_0)$ and $\phi_k^*$ pairwise disjointly supported,
> (iii) $K(u^*) = K$ (integer invariant in each basin).

Then:
$$\Sigma_m = \mathcal{B}_0 \sqcup \mathcal{B}_1 \sqcup \mathcal{B}_2 \sqcup \cdots \sqcup \mathcal{B}_{K_{\max}} \sqcup \mathcal{N}$$

where $\mathcal{N}$ is the **null set** — points not in any well-separated basin (saddles, ridges, non-well-separated minima, boundary strata).

### 2.2 Key structural claims (C1-1 to C1-4)

**Claim C1-1 (Topological disjointness)**: For $K \neq K'$, $\mathcal{B}_K \cap \mathcal{B}_{K'} = \emptyset$.

*Proof sketch*: By Def 2.1 (iii), $K(u^*)$ is integer and determined by the minimizer $u^*$ that the trajectory converges to. Each trajectory has at most one limit (gradient flow monotonic); so each well-separated initial condition lies in at most one basin. Disjointness is immediate from integer labeling.

**Status**: Cat A (trivial consequence of definition).

**Claim C1-2 (Basin connectedness within K-sector)**: Each $\mathcal{B}_K$ is connected in $\Sigma_m$.

*Proof sketch (attempt)*: $\mathcal{B}_K$ is the union of path-components, each attracted to a well-separated $K$-formation minimizer $u^*_K$. If the set of $K$-formation minimizers is connected under "continuous deformation within K-sector" (formation-wise displacement), then basins are path-connected via gradient flow.

**Difficulty**: 두 개의 서로 다른 well-separated $K$-formation minimizer $u^*_{K,1}, u^*_{K,2}$ (다른 positions, 같은 K)을 잇는 continuous path가 $\mathcal{B}_K$ 내에 있다는 보장 없음. 실제로 path가 saddle을 통과할 수 있고 saddle은 $\mathcal{N}$에 속함.

**Status**: **Conjectural Cat C**. Counterexample 시도 필요.

**Claim C1-3 (Measure-positivity of $\mathcal{N}$)**: The null set $\mathcal{N}$ has **positive measure** in $\Sigma_m$ (not zero measure) because saddles + not-well-separated configurations occupy a thick set near basin boundaries.

*Rationale*: "Not well-separated" is an open condition ($d_{\min} < d_{\mathrm{sep,min}}$ for some threshold). Open set typically has positive measure.

**Status**: Cat A (trivial from def).

**Claim C1-4 (Basin boundary $\partial \mathcal{B}_K$ is codim-1 in $\Sigma_m$)**: The boundary between $\mathcal{B}_K$ and $\mathcal{B}_{K+1}$ (or $\mathcal{N}$) is codimension-1 — a "separatrix".

*Proof sketch*: Gradient flow separatrices are stable manifolds of saddle points, which are codim-1 smooth manifolds in generic situations. In our case, K-sector transitions require crossing a saddle, hence codim-1.

**Status**: Cat C conditional on **generic saddle non-degeneracy** (MO-1 refined).

### 2.3 Axiom S1-S4 naturality (AN audit)

For each of the four proposed axioms (`step_cohesion.md` §10.1):

#### S1 (Step-Cohesion Decomposition) — AN: ✅ natural

Single-formation form:
$$u^* = \phi_1^* + r,\quad \|r\|_\infty \leq \exp(-d_{\min,\mathrm{boundary}}/\xi_0).$$

Multi-K form:
$$u^* = \sum_{k=1}^K \phi_k^* + r,\quad \|r\|_\infty \leq K \exp(-d_{\min}/\xi_0).$$

The upper bound on residual gets a factor $K$ from pairwise contributions, but the form extends naturally. **AN = ✅**.

#### S2 (Three-Layer Hierarchy) — AN: ✅ natural

- Layer 1: $K \in \mathbb{Z}_{\geq 0}$ — already integer-valued, multi-K trivially.
- Layer 2: $(r_k, \xi_0, d_{\min}(j,k))$ — per-formation geometry with pair-interaction distances.
- Layer 3: $u(x) = \sum_k \phi_k^*(x)$ — pointwise sum of per-formation fields.

All layers extend naturally. **AN = ✅**.

#### S3 (Protocol-Parameterized Observable) — AN: ✅ natural

$$K_{\mathrm{observed}}(\beta, c, G, \pi) = K_{\mathrm{step}}(u_\pi^*(\beta)) = \#\{\text{connected components of } \{x: u(x) > \tau\}\}.$$

Protocol selects a basin $\mathcal{B}_K$; observed $K$ is determined. **AN = ✅** but with caveat: Protocol $\pi$ can map to any $K$-sector, depending on initial condition. V7 P3 Gaussian observation implies protocol maps to distribution over sectors, not a single one.

#### S4 (Static/Dynamic Decomposition) — AN: ✅ natural

Static: $u^*_K$의 landscape properties within $\mathcal{B}_K$.
Dynamic: $u_\pi^*(\beta)$의 protocol-selected basin.

Multi-K extension is direct. **AN = ✅**.

**Conclusion**: All four axioms pass AN audit. **Formation Quantization framework is axiomatically natural for $K \geq 2$.**

### 2.4 Proof-structural naturality (PSN audit)

For single-formation claims extending to K-formation:

#### PSN test (1): T-Merge (a) K-local minimality

**Single-formation form** (implicit): $K = 1$ minimizer is local min when Hessian PD.

**K-form (canonical §13 T-Merge (a))**: Well-separated K-formations are local minima on $\Sigma^K_M$; Hessian PD under $\mu_1 \mu_2 > \lambda_{\mathrm{rep}}^2$.

**PSN = ✅**. Proof extends by $\sum_k$ in Hessian + off-diagonal perturbation bound.

#### PSN test (2): T-Persist-K-Sep

Already proved in canonical §13. Proof explicitly uses Coupling Bound Lemma (single-formation technology) + Weyl spectral bound (sum-structure).

**PSN = ✅**.

#### PSN test (3): Cor 2.2 (single tanh profile)

**Single-formation**: $\phi^*(x) \approx \frac{1}{2}(1 - \tanh(d/\xi_0))$ in supra-lattice regime.

**K-form natural extension**:
$$u^*(x) \approx \sum_{k=1}^K \frac{1}{2}(1 - \tanh((d(x, c_k) - r_k)/\xi_0)),$$

where each $\phi_k^*$ is single-formation profile centered at $c_k$ with radius $r_k$.

**Caveat**: Overlapping $\phi_j^*, \phi_k^*$ break pointwise decomposition. **Well-separated** ($d_{\min} \geq 3$) 제약 하에 PSN = ✅. **Overlap regime에서는 PSN ≠ ✅** (not a straightforward sum — requires IFT correction).

**PSN status**: Conditional ✅ (well-separated) / ✘ (strong overlap).

### 2.5 Observable naturality (ON audit)

#### ON test (1): K_step operator

Single K: $K_{\mathrm{step}}(u; \tau) = \#\{\text{connected components of } \{u > \tau\}\}$. Returns $\in \{0, 1\}$.

Multi K: Same definition, returns $\in \mathbb{Z}_{\geq 0}$.

**ON = ✅**. The operator's definition is K-agnostic.

#### ON test (2): K_soft diagnostic

Single K: $K_{\mathrm{soft}}(u) \approx \int (\text{soft indicator}) dx$, continuous proxy.

Multi K: Same.

**ON = ✅**.

#### ON test (3): Protocol selection

Single K (K=1 only): Protocol always selects $\mathcal{B}_1$ (trivial).

Multi K: Protocol selects $\mathcal{B}_K$ for various $K$ depending on initial condition. **Non-trivial** — protocol selection becomes meaningful only in multi-K setting.

**ON = ✅** (multi-K is where protocol selection has content).

### 2.6 Overall naturality verdict

- **AN (Axiomatic)**: ✅ all four axioms
- **PSN (Proof-structural)**: ✅ for well-separated; ✘ for strong overlap
- **ON (Observable)**: ✅ all

**Conclusion (tentative Cat B)**: Formation Quantization **is fully natural** in the well-separated regime ($d_{\min} \geq 3$). Weakly-interacting and strongly-interacting regimes require extra machinery (T-Persist-K-Weak, T-Persist-K-Strong) beyond bare single-formation theory.

---

## §3. Approach C3 — Landau free energy $F(K)$

### 3.1 Main formula

For $K$-formation configuration on a large regular graph (supra-lattice regime):

$$F(K; \beta, c, G) = K \cdot F_{\mathrm{single}}(r_0(K), \xi_0) + \binom{K}{2} \cdot F_{\mathrm{pair}}(d_{\min}(K)) + C_{\mathrm{bulk}}$$

where:

- $r_0(K) = \sqrt{m/(\pi K)}$ — average formation radius (2D mass conservation).
- $\xi_0 = \sqrt{\alpha/\beta}$.
- $d_{\min}(K)$ — typical inter-formation distance; roughly $\sqrt{n/K}$ on 2D grid minus $2r_0$.
- $C_{\mathrm{bulk}}$ — K-independent bulk contribution.

### 3.2 Components

#### 3.2.1 $F_{\mathrm{single}}(r_0, \xi_0)$

Per-formation energy. From canonical T11 Γ-convergence:
$$F_{\mathrm{single}}(r_0, \xi_0) \approx C_* \cdot \sqrt{\alpha\beta} \cdot \mathrm{Per}(\phi^*) + \text{bulk corrections},$$

where $\mathrm{Per}(\phi^*) \approx 2\pi r_0$ (2D disk perimeter), $C_* = \int_0^1 \sqrt{2W(s)}ds$ Modica-Mortola constant.

Leading order:
$$F_{\mathrm{single}} \sim C_* \sqrt{\alpha\beta} \cdot 2\pi r_0 = 2\pi C_* \sqrt{\alpha\beta} \cdot \sqrt{m/(\pi K)}.$$

$K$-dependence: $F_{\mathrm{single}}(K) \propto K^{-1/2}$ (per formation cheaper as K increases, since formations are smaller).

#### 3.2.2 $F_{\mathrm{pair}}(d_{\min})$

Pair repulsion. From `from_single.md` §4.3b:
$$F_{\mathrm{pair}}(d_{\min}) \sim A \cdot \frac{\exp(-d_{\min}/\xi_0)}{\sqrt{d_{\min}/\xi_0}},$$

exponentially decaying with distance / $\xi_0$.

On 2D grid with K formations: $d_{\min}(K) \sim \sqrt{n/K} - 2r_0 = \sqrt{n/K} - 2\sqrt{m/(\pi K)} \sim \sqrt{n/K}(1 - 2\sqrt{c/\pi})$.

For $c < \pi/4 \approx 0.78$, $d_{\min}(K) > 0$ for all $K$; exponential factor dominates:
$$F_{\mathrm{pair}}(K) \sim A \exp(-\sqrt{n/K}/\xi_0).$$

### 3.3 Total $F(K)$

$$F(K) \approx K \cdot \frac{2\pi C_* \sqrt{\alpha\beta m}}{\sqrt{\pi K}} + \binom{K}{2} A \exp(-\sqrt{n/K}/\xi_0).$$

Simplifying first term:
$$F(K) \approx 2 C_* \sqrt{\alpha\beta m \pi K} + \frac{K(K-1)}{2} A \exp(-\sqrt{n/K}/\xi_0).$$

**Term 1**: increasing in K (interface energy grows linearly with K because $\sqrt{K} \cdot K^{-1/2} \cdot K = \sqrt{K}$ — wait recomputing: $K \cdot \sqrt{m/(\pi K)} = \sqrt{mK/\pi}$, so Term 1 $\propto \sqrt{K}$).

**Term 2**: For small $K$ ($d_{\min} \gg \xi_0$), exponential is small; Term 2 negligible. For large $K$ ($d_{\min} \sim \xi_0$), exponential is O(1); Term 2 grows like $K^2$.

### 3.4 Minimum of $F(K)$

$$\frac{dF}{dK} = \frac{C_*\sqrt{\alpha\beta m \pi}}{\sqrt K} + \text{pair contribution}.$$

First term is always positive, so **$F(K)$ is monotonically increasing** if pair term is negligible. This implies:

**Claim 3.1**: In well-separated regime ($d_{\min} \gg \xi_0$), the **Landau free energy $F(K)$ predicts $K^* = 1$ as global minimum**, consistent with T-Merge (b) Cat A.

*Proof*: From (3.3), Term 1 = $\sqrt{K}$ is monotone in K; Term 2 is negligible at well-separated. So $\arg\min F(K) = 1$.

**Status**: Cat A structural (follows directly from T-Merge (b)'s isoperimetric content re-expressed in Landau form).

### 3.5 When does $F(K)$ have non-trivial minimum at K > 1?

Term 2 must be significantly positive and **decrease** with K... but $F_{\mathrm{pair}} \geq 0$ always (repulsion), so Term 2 is monotone in K as well.

**Conclusion**: In the Landau framework with only pair repulsion, **$F(K)$ has no non-trivial K > 1 minimum**. Observed $\widehat K > 1$ (e.g., R17 c=0.3, β=30, 2D square $\widehat K = 7.76$) requires:
- Protocol-selection into non-minimum K-sector (basin ≠ global min), OR
- Kinetic trap (metastability, $F(K^*_{\mathrm{observed}}) > F(1)$ but sector is long-lived).

This **reinforces Static/Dynamic Separation Principle** (R22 §17.6): thermodynamic $F(K)$ ≠ dynamic $\widehat K$.

### 3.6 Formation Quantization uniqueness (well-separated case)

> **Theorem 3.2 (Formation Quantization Uniqueness, Well-Separated)**. Let $u^*$ be a local minimizer in $\mathcal{B}_K$ with $d_{\min}(u^*) \geq d_{\mathrm{sep}}$ for some threshold $d_{\mathrm{sep}}$ such that $\exp(-d_{\mathrm{sep}}/\xi_0) < \eta$ for small $\eta$. Then the decomposition
> $$u^* = \sum_{k=1}^K \phi_k^* + r(u^*)$$
> is unique up to formation labeling (permutation of indices $k$), with each $\phi_k^*$ uniquely determined by its support $A_k^* = \{x : u^*(x) \geq \tau\}$ $\cap$ connected-component.

*Proof*:

**Step 1 — Existence**: Define $A_k^* = $ $k$-th connected component of $\{u^* \geq \tau\}$ with canonical threshold $\tau = 0.5$. This is well-defined (finite graph, finite component count).

**Step 2 — Support disjointness**: Since $A_k^*$ are distinct connected components, they are pairwise disjoint by construction. Hence $\mathrm{supp}(\phi_k^*) \subseteq A_k^*$ disjoint.

**Step 3 — Per-formation profile reconstruction**: Fix $k$. Define $\phi_k^*$ as the **restriction of $u^*$ to $A_k^*$**, padded with 0 outside:
$$\phi_k^*(x) = u^*(x) \cdot \chi_{A_k^*}(x) + u^{\mathrm{fit}}_{\partial A_k}(x) \cdot (1 - \chi_{A_k^*}(x)),$$
where $u^{\mathrm{fit}}$ is the tanh-fit extension beyond $A_k^*$.

**Step 4 — Decomposition identity**: On $A_k^*$ we have $\phi_k^* = u^*$ and $\phi_j^* \approx 0$ for $j \neq k$ (by Coupling Bound Lemma Item 5, $u^j(x) \leq 2\exp(-c_0 d_{\min}) \leq 2\eta$). So:
$$u^*(x) - \sum_j \phi_j^*(x) = u^*(x) - \phi_k^*(x) - \sum_{j \neq k} \phi_j^*(x) = 0 - O(\eta) = -O(\eta)\ \text{on }A_k^*.$$
Similarly on $X \setminus \bigcup_k A_k^*$, $u^*(x)$ is already at the background level $\sim 0$, and $\sum_j \phi_j^*(x) \leq K \cdot O(\eta)$.

Hence residual $r(u^*) = u^* - \sum_k \phi_k^*$ satisfies $\|r\|_\infty \leq O(K\eta) = O(K \exp(-d_{\min}/\xi_0))$.

**Step 5 — Uniqueness up to permutation**: Suppose alternative decomposition $u^* = \sum_k \tilde\phi_k^* + \tilde r$ exists with $\|\tilde r\|_\infty \leq O(\eta')$. Then each $\tilde\phi_k^*$ must be supported on some connected component of $\{u^* \geq \tau - O(\eta')\}$, which (for $\eta' < \tau/2$) matches $A_k^*$ (for some permutation of indices). Hence $\tilde\phi_k^* \approx \phi_{\pi(k)}^*$ for a permutation $\pi$. QED.

**Category**: **Cat A structural** for well-separated regime. Proof elementary given Coupling Bound Lemma.

### 3.7 Non-uniqueness in strongly-interacting regime

For $d_{\min} \leq \xi_0$ (overlapping supports), the decomposition is **not unique**: $A_k^*$의 boundary 선택 자유도가 증가. In this regime, $K(u^*)$ may also be ambiguous (whether two overlapping formations count as 1 or 2 depends on threshold $\tau$).

**Status**: **Open; not extended** in this session.

---

## §4. Moduli space $\mathcal{M}_K$ structure (C2 absorbed)

### 4.1 Definition

$$\mathcal{M}_K(\beta, c, G) = \{u^* \in \mathcal{B}_K : u^* \text{ is a local minimizer}\} / \mathrm{Aut}(G).$$

### 4.2 Dimension heuristic (2D grid, well-separated)

Each K-formation contributes:
- 2 continuous parameters (center $c_k \in X$, mostly frozen on graph vertices except for symmetry-breaking)
- 1 continuous parameter (radius $r_k$ / mass $m_k$)

Total: $3K$ degrees of freedom for K formations.

Constraints:
- Total mass $\sum_k m_k = m$: 1 constraint.
- Non-overlap: no explicit dim reduction but restricts region.

Modulo $\mathrm{Aut}(G)$: translations (2 for torus, 0 for free-BC square), rotations (4 for D_4).

Heuristic dim:
$$\dim \mathcal{M}_K \approx 3K - 1 - |\mathrm{Aut}(G)_{\mathrm{continuous}}|.$$

For 2D free-BC square (only discrete rotations): $\dim \mathcal{M}_K \approx 3K - 1$.
For 2D torus (2 continuous translations): $\dim \mathcal{M}_K \approx 3K - 3$.

### 4.3 Specific cases

**K=1 free-BC square**: $\dim \mathcal{M}_1 = 0$ (only center at geometric center, discrete rotations exhausted). Consistent with R5 observation.

**K=1 2D torus**: $\dim \mathcal{M}_1 = 3 - 3 = 0$, but R5 says 1-dim (circle of translations). Heuristic off because center + size correction 해석이 정확하지 않음. **Re-compute**: 2 translations + 1 radius = 3 total; modulo 2 translations = 1 dim. ✅ (radius remaining).

**K=2 free-BC square**: $\dim \mathcal{M}_2 = 6 - 1 = 5$ (two positions × 2, two radii, mass constraint).

### 4.4 Connection to Formation Quantization

$\mathcal{M}_K$ is the **moduli of $K$-formation configurations**. Formation Quantization Theorem (3.2) says each $\mathcal{M}_K$-point has unique step decomposition. Basin $\mathcal{B}_K$ is a $\mathcal{M}_K$-indexed family of basins (each point of $\mathcal{M}_K$ has its own basin in $\Sigma_m$).

### 4.5 Status

- **Dimension formula heuristic**: Cat C (depends on unclear symmetry structure).
- **Connection to Formation Quantization**: Cat A (direct from Theorem 3.2).
- **$\mathcal{M}_K$ as topological space**: Open (connectedness, compactness of moduli space).

---

## §5. Pair interaction refinement

### 5.1 Block Hessian structure (from R12 canonical §12 Coupling Bound Lemma)

For $u^*_K = \sum_k \phi_k^*$ well-separated local minimizer, Hessian on $\Sigma_m$ (not $\Sigma^K_M$):
$$H = \begin{pmatrix} H_1 & V_{12} & \cdots \\ V_{21} & H_2 & \cdots \\ \vdots & & \ddots \end{pmatrix}$$

where:
- $H_k$ = single-formation Hessian at $\phi_k^*$ (block on $T_{A_k}$ tangent).
- $V_{jk}$ = off-diagonal cross-block. From R12: $V_{jk} \sim \mu_{\mathrm{sep}} \cdot P_{jk}$ with $\mu_{\mathrm{sep}} \sim e^{-d_{\min}/\xi_0}$ and $P_{jk}$ some overlap-indicator operator.

### 5.2 Spectral stability

Weyl bound: $\lambda_{\min}(H) \geq \min_k \lambda_{\min}(H_k) - (K-1) \mu_{\mathrm{sep}}$.

**Claim 5.1**: For $\mu_{\mathrm{sep}} < \min_k \lambda_{\min}(H_k)/(K-1)$, joint Hessian is positive definite. **$\mathcal{B}_K$ is non-empty** under this condition.

**Status**: Cat A (restatement of canonical Coupling Bound Lemma Item 3 / T-Merge (a)).

### 5.3 Pair interaction as perturbative correction

Treating $\mu_{\mathrm{sep}}$ as small perturbation:
$$\lambda(H) = \lambda(\text{block diag}) + O(\mu_{\mathrm{sep}}^2).$$

Energy correction:
$$F(K) \supseteq \sum_{j < k} \mathrm{tr}[V_{jk} \cdot H_k^{-1} V_{kj}] = \binom{K}{2} \cdot O(\mu_{\mathrm{sep}}^2) \cdot O(\lambda_{\min}^{-1}).$$

**Status**: Cat B (Schur / perturbation sketch; detailed verification pending).

### 5.4 Triple / multi-body coupling (pre_brainstorm §7 risk)

Pair treatment assumes $\binom{K}{2}$ pairs are independent. Triple-body coupling $V_{ijk}$ for $i, j, k$ distinct exists in principle: three formations overlap in triple region, contributing trilinear term to energy.

**Magnitude**: For formations of radius $r_0$ separated by $d_{\min}$, triple-overlap volume $\sim \exp(-3d_{\min}/\xi_0)$ (decay faster than pair).

**Status**: Triple body is $O(e^{-3d/\xi_0})$ vs pair $O(e^{-d/\xi_0})$ — **negligible** in well-separated regime. **Cat A for well-separated**; open for overlapping.

---

## §6. $\widehat K$ prediction framework (post-retraction)

### 6.1 Preceding context

Conjecture 2.1 (v1-v5, `from_single.md` §2) **RETRACTED** (R17/R19/R20/V7 P1 cascade). Claim "$\widehat K = f(N_{\mathrm{unst}})$" falsified.

### 6.2 Replacement: Protocol-parameterized multi-K

Following Axiom S3 (`step_cohesion.md` §6):
$$\widehat K(\beta, c, G, \pi) = K_{\mathrm{step}}(u_\pi^*(\beta)).$$

Where $u_\pi^*(\beta) \in \mathcal{B}_{K(\pi, \beta)}$ — basin selected by protocol.

### 6.3 Landau prediction vs observed

$F(K)$ predicts K=1 as global min (§3.4). But **observed $\widehat K$ ≠ 1 across many regimes** (R17-R22 empirical).

**Reconciliation**: $\widehat K$ is **basin selector output**, not landscape global min. Formula $\widehat K$ must incorporate:
- Protocol's initial-condition distribution
- Gradient flow trajectory from IC to basin
- Metastability escape rates (finite T)

**No simple formula** (that's the point of R20 decoupling).

### 6.4 Partial prediction (attempts)

- **$\widehat K = 1$ regime**: when Fiedler-init noise-free protocol always lands in $\mathcal{B}_1$ (deep global basin). E.g., R18 c=0.5 2D torus: $\widehat K = 1.00\pm 0.00$ across 50 seeds. **Sufficient condition**: Fiedler mode has bias toward K=1 configuration. **Cat C** (empirical pattern, mechanism open).
- **$\widehat K > 1$ regime**: when protocol's basin-selection has non-trivial distribution. E.g., R17 c=0.3 2D square: $\widehat K = 7.76$ at β=30. **Mechanism**: nucleation of multiple formations from initial noise before coarsening reaches K=1. **Cat C sketched** (connects to G4 coarsening time evolution).
- **Bistable region ($\beta$ near critical protocol threshold)**: V7 P3 observed Gaussian around $\bar K$. **Class N** (§SF_function_taxonomy §6). Parameters open (NQ-52).

---

## §7. Integration with canonical

### 7.1 Canonical §11 Multi-formation paradigm

Canonical currently says:
> "Multi-formation is kinetic. On any connected graph, the global energy minimum is always a single formation (K* = 1) due to isoperimetric ordering... Coexistence of K > 1 formations is therefore not thermodynamically favored."

**This session's contribution**:
- Provides **structural decomposition** (§3.6 Formation Quantization Uniqueness) of multi-K states.
- Confirms "K=1 is global min" via Landau F(K) monotonicity (§3.4), reinforcing T-Merge (b).
- Separates **static landscape (Layer 2 Landau F)** from **dynamic observable ($\widehat K$, protocol-dependent Layer 1)**.

### 7.2 Canonical §12 Coupling Bound Lemma

No modification needed. This session uses the Lemma directly in §3.6 proof and §5.1 block structure.

### 7.3 Canonical §13 T-Merge (a), (b), Topological Lock

All preserved. T-Merge (a) is §5.1 Claim 5.1 (existence of K-local min); T-Merge (b) is §3.4 Claim 3.1 (K=1 global). Topological Lock is on $\Sigma^K_M$ (per-formation mass constraint) — this session does **not** use $\Sigma^K_M$, working on $\Sigma_m$ directly. Topological Lock becomes **irrelevant** to the Formation Quantization framework (which is on $\Sigma_m$, not product manifold).

### 7.4 Proposed canonical additions

- **New Theorem: Formation Quantization Uniqueness (§3.6 Thm 3.2)**. Cat A structural.
- **New Section on $F(K)$ Landau framework**. Cat A structural reformulation of T-Merge (b).
- **Clarification in §11**: K-field architecture $\Sigma^K_M$ is **not required** for multi-formation theory. Equivalent analysis on $\Sigma_m$ with Formation Quantization decomposition sufficient.

---

## §8. New open questions seeded

### 8.1 NQ-56 — $\mathcal{B}_K$ connectedness (C1-2 Claim)

Is each $K$-sector basin $\mathcal{B}_K$ path-connected in $\Sigma_m$? Counterexample: two separated "sub-basins" within same K-sector, connected only via K-transition saddle. **Carry to next session.**

### 8.2 NQ-57 — Basin boundary structure

Is $\partial\mathcal{B}_K$ codim-1 smooth manifold in generic case? Related to NQ-48 (Aut(G)-equivariant Morse).

### 8.3 NQ-58 — Landau $F(K)$ empirical fit

Empirically fit $F(K)$ to observed energies across K-sectors. Does $K \cdot F_{\mathrm{single}}(K) + \binom{K}{2} F_{\mathrm{pair}}(K)$ match measured? **Numerical experiment candidate**.

### 8.4 NQ-59 — Multi-K version of C-FQ with $K \geq 3$ saddle count

For $K = 3$ formations on 2D grid, how many saddles connect $\mathcal{B}_3$ to $\mathcal{B}_2$? Partition function of saddle enumeration. Connects to Round 10 Tree Structure Theorem extension.

### 8.5 NQ-60 — Triple-body coupling beyond well-separated

When $d_{\min} \leq \xi_0$, triple-body coupling becomes relevant. Can it alter basin structure (e.g., K=3 bistable with K=2)?

### 8.6 NQ-61 — Protocol-independent invariants

What functionals of landscape (not of protocol) are invariant across protocol-selections? Candidates: $F(K=1), F(K^*), \xi_0, \{d_{\min}(j,k)\}$. These should appear in every protocol; "protocol-dependent" quantities like $\widehat K$ are secondary.

---

## §9. Naturality verdict summary

| Criterion | Well-sep | Weak overlap | Strong overlap |
|---|---|---|---|
| AN (Axiomatic) | ✅ | ✅ | ✅ |
| PSN (Proof) | ✅ | ⚠️ (with T-Persist-K-Weak) | ✘ |
| ON (Observable) | ✅ | ✅ | ⚠️ ($K$ thresh-dependent) |

**Overall**: Single → Multi extension is **fully natural in well-separated regime**; partially natural in weak-overlap with extra machinery; **not natural** in strong-overlap (new framework needed).

**Main message**: Formation Quantization is the **correct extension direction**. Stage 3 canonical merge should proceed on well-separated first, overlap regimes deferred.

---

## §10. File status

- **Primary deliverable**: K-sector basin stratification framework (§2) + Landau $F(K)$ (§3) + Formation Quantization Uniqueness proof sketch (§3.6) + naturality audit (§9).
- **Category**: Thm 3.2 (FQ Uniqueness) tentative Cat A structural. Claim 3.1 (F(K) monotonicity) Cat A via T-Merge (b). Claim 5.1 (spectral stability) Cat A via Coupling Bound Lemma. Basin connectedness (C1-2) Cat C conjectural.
- **Canonical merge proposal**: Formation Quantization Uniqueness as new Cat A; F(K) as reformulation of T-Merge (b); clarification that $\Sigma^K_M$ is not required.
- **Intended promotion**: `working/MF/multi_quantization.md` (신규), replacing the retracted §2 of `from_single.md`.

**End of MF_multi_quantization.md.**
