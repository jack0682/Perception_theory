# Stratified Morse Theory of the K-Field Merge Landscape

**Date:** 2026-04-06
**Category:** proof
**Status:** rigorous analysis (mixed Cat A / Cat B)
**Depends on:** Canonical Spec v2.1 §4 (K-field architecture), MERGE-CRITIQUE.md (Flaws #1, #2, #9, F)

---

## 0. Purpose

The prior merge barrier documents operate on either $\Sigma^K_M = \Sigma_{m_1} \times \Sigma_{m_2}$ (where merge is trivially impossible) or $\Sigma_M^{\mathrm{relax}}$ (where local minimality was claimed but not proved on the correct tangent space). This document provides a rigorous topological and differential-geometric analysis of the **mass-transfer manifold** $\mathcal{M}_2$, which is the correct arena for studying merge as a continuous process. We apply stratified Morse theory (Goresky–MacPherson) to the K-field energy on this stratified space.

**Convention.** Throughout, $G = (V, E)$ is a finite connected graph with $n = |V|$ nodes, $K = 2$ formations, total mass $M > 0$.

---

## 1. The Spaces

### 1.1 The Volume Simplex

For $m > 0$, define the **volume-constrained polytope**:

$$\Sigma_m := \{u \in [0,1]^n : \textstyle\sum_{i=1}^n u_i = m\}$$

This is the intersection of the hyperplane $H_m = \{\mathbf{1}^T u = m\}$ with the unit cube $[0,1]^n$.

**Proposition 1.1 (Topology of $\Sigma_m$).** For $0 < m < n$:
- $\Sigma_m$ is a convex polytope of dimension $n - 1$.
- $\Sigma_m$ is a manifold with corners, homeomorphic to the closed $(n-1)$-ball $\overline{B}^{n-1}$.
- $\mathrm{int}(\Sigma_m) = \{u \in (0,1)^n : \sum u_i = m\}$ is an open convex subset of $H_m \cong \mathbb{R}^{n-1}$, hence diffeomorphic to $\mathbb{R}^{n-1}$.
- The boundary $\partial \Sigma_m$ consists of faces where at least one coordinate saturates ($u_i = 0$ or $u_i = 1$).

*Proof.* $\Sigma_m$ is a bounded intersection of closed half-spaces in the affine hyperplane $H_m$, hence a convex polytope. Every convex polytope in $\mathbb{R}^{n-1}$ with non-empty interior is homeomorphic to $\overline{B}^{n-1}$ (Brouwer). The interior is open and convex in $H_m$; every open convex subset of $\mathbb{R}^{n-1}$ is diffeomorphic to $\mathbb{R}^{n-1}$ (Whitehead 1961). $\square$

**Degenerate cases:**
- $m = 0$: $\Sigma_0 = \{0\}$ (a single point).
- $m = n$: $\Sigma_n = \{\mathbf{1}\}$ (a single point).
- $0 < m \leq 1$: $\Sigma_m$ is the standard $(n-1)$-simplex scaled by $m$ (no coordinate can reach 1 if $m \leq 1$ and $n \geq 2$, so the $u_i \leq 1$ constraints are inactive).

**Homotopy type:** $\Sigma_m$ is contractible for all $m \in [0, n]$ (convex sets are contractible). Therefore $\pi_k(\Sigma_m) = 0$ for all $k \geq 0$.

### 1.2 The Product Manifold (Fixed Masses)

$$\Sigma^2_M := \Sigma_{m_1} \times \Sigma_{m_2}, \qquad m_1 + m_2 = M$$

- Dimension: $(n-1) + (n-1) = 2n - 2$.
- Topology: product of two contractible spaces, hence contractible.
- This is the constraint manifold used by `multi.py`. Merge is **topologically impossible** here because $\Sigma_{m_2}$ does not contain the zero vector when $m_2 > 0$. (This is Theorem 1 of MERGE-BARRIER-KFIELD.md — trivially correct.)

### 1.3 The Mass-Transfer Manifold $\mathcal{M}_2$

**Definition.** The mass-transfer manifold is the fibered space:

$$\mathcal{M}_2 := \{(u_1, u_2, m_1, m_2) \in [0,1]^{2n} \times \mathbb{R}^2_{\geq 0} : \textstyle\sum u_1^i = m_1,\; \sum u_2^i = m_2,\; m_1 + m_2 = M\}$$

Eliminating $m_1 = M - m_2$, we can parametrize by $(u_1, u_2, m_2)$ subject to $\sum u_1^i = M - m_2$, $\sum u_2^i = m_2$, $u_k \in [0,1]^n$, $m_2 \in [0, M]$.

**Equivalently:** $\mathcal{M}_2$ is the total space of a fiber bundle

$$\pi : \mathcal{M}_2 \to [0, M], \qquad \pi(u_1, u_2) = m_2 = \textstyle\sum u_2^i$$

with fiber $\pi^{-1}(m_2) = \Sigma_{M - m_2} \times \Sigma_{m_2}$.

**Proposition 1.2 (Dimension of $\mathcal{M}_2$).**
- For $m_2 \in (0, M)$: fiber dimension $= (n-1) + (n-1) = 2n-2$. Total dimension $= 2n - 2 + 1 = 2n - 1$.
- At $m_2 = 0$: fiber $= \Sigma_M \times \{0\}$, dimension $= n - 1$. Dimension drop of $n - 1$.
- At $m_2 = M$: fiber $= \{0\} \times \Sigma_M$, dimension $= n - 1$. Dimension drop of $n - 1$.

**Proof.** The fiber $\Sigma_{M-m_2} \times \Sigma_{m_2}$ has dimension $(n-1) + (n-1)$ when both factors are full-dimensional polytopes (i.e., $0 < m_2 < M$ and $M - m_2 < n$ and $m_2 < n$). At $m_2 = 0$, $\Sigma_0 = \{0\}$ is a point, so the fiber collapses to $\Sigma_M \times \{0\}$, which is $(n-1)$-dimensional. $\square$

**Key observation:** $\mathcal{M}_2$ is NOT a manifold — it is a **stratified space** with singularities at $m_2 \in \{0, M\}$ where the fiber dimension drops.

### 1.4 Relationship to $\Sigma_M^{\mathrm{relax}}$

The relaxed manifold from MERGE-BARRIER-KFIELD.md is:

$$\Sigma_M^{\mathrm{relax}} = \{(u_1, u_2) \in [0,1]^{2n} : \textstyle\sum(u_1^i + u_2^i) = M\}$$

There is a natural identification $\mathcal{M}_2 \cong \Sigma_M^{\mathrm{relax}}$: given $(u_1, u_2) \in \Sigma_M^{\mathrm{relax}}$, set $m_2 = \sum u_2^i$ and $m_1 = M - m_2$. The map $\pi$ is simply $(u_1, u_2) \mapsto \sum u_2^i$.

Thus $\Sigma_M^{\mathrm{relax}}$ IS $\mathcal{M}_2$, viewed without the explicit mass decomposition. The fibration $\pi$ endows $\Sigma_M^{\mathrm{relax}}$ with a natural stratification by the value of $m_2$.

**Proposition 1.3.** $\Sigma_M^{\mathrm{relax}}$ is a convex polytope of dimension $2n - 1$ (the intersection of the hyperplane $\sum(u_1^i + u_2^i) = M$ with $[0,1]^{2n}$). It is contractible, with interior diffeomorphic to $\mathbb{R}^{2n-1}$.

*Proof.* Same argument as Proposition 1.1, applied in $\mathbb{R}^{2n}$. $\square$

**Critical distinction:** $\Sigma_M^{\mathrm{relax}}$ is a genuine $(2n-1)$-dimensional manifold with corners. It contains the K=2 point $(u_1^*, u_2^*)$ in its interior (when formations have $u_k^i \in (0,1)$) AND the K=1 point $(u_{\mathrm{merged}}, 0)$ on its boundary (since $u_2 = 0$ saturates $n$ box constraints). The merge path is a path from interior to boundary.

---

## 2. The Singularity at $m_2 = 0$: Blow-Up Analysis

### 2.1 The Degeneration

The fiber $\pi^{-1}(m_2) = \Sigma_{M-m_2} \times \Sigma_{m_2}$ degenerates as $m_2 \to 0$:
- For $m_2 > 0$: $\Sigma_{m_2}$ is an $(n-1)$-dimensional polytope.
- At $m_2 = 0$: $\Sigma_0 = \{0\}$ is a point.

This is a **collapsing fiber** singularity. The total space $\mathcal{M}_2$ is smooth (as a subset of $\Sigma_M^{\mathrm{relax}}$), but the fibration structure degenerates.

### 2.2 Local Coordinates Near $m_2 = 0$

Introduce **rescaled coordinates** for the second formation:

$$v_2 := \frac{u_2}{m_2} \in \Sigma_1 \quad \text{(when } m_2 > 0\text{)}$$

so that $u_2 = m_2 \cdot v_2$ with $v_2$ on the **unit-mass simplex** $\Sigma_1 = \{v \in [0,1]^n : \sum v_i = 1\}$.

In coordinates $(u_1, v_2, m_2)$:
- $u_1 \in \Sigma_{M - m_2}$ (first formation at mass $M - m_2$)
- $v_2 \in \Sigma_1$ (normalized shape of second formation)
- $m_2 \in (0, M]$ (mass of second formation)
- The actual second field is recovered as $u_2 = m_2 \cdot v_2$.

**The blow-up.** The map $(u_1, v_2, m_2) \mapsto (u_1, m_2 \cdot v_2)$ is a **real blow-up** of $\mathcal{M}_2$ along the submanifold $\{m_2 = 0\}$. The blown-up space is:

$$\widetilde{\mathcal{M}}_2 := \{(u_1, v_2, m_2) : u_1 \in \Sigma_{M - m_2},\; v_2 \in \Sigma_1,\; m_2 \in [0, M]\}$$

At $m_2 = 0$: the fiber of $\widetilde{\mathcal{M}}_2$ is $\Sigma_M \times \Sigma_1$, which is $(n-1) + (n-1) = (2n-2)$-dimensional. The blow-up **resolves** the dimension drop by replacing the collapsed point $\{0\}$ with the **projectivized fiber** $\Sigma_1$ (the space of directions from which $u_2$ can approach zero).

**Proposition 2.1 (Blow-up structure).** The exceptional divisor $\widetilde{\mathcal{M}}_2|_{m_2=0} = \Sigma_M \times \Sigma_1$ parametrizes pairs $(u_1, v_2)$ where $u_1$ is a single formation at mass $M$ and $v_2$ is the "ghost shape" of the vanished second formation.

**Geometric interpretation:** The singularity at $m_2 = 0$ is a **cone point** — a neighborhood of $(u_{\mathrm{merged}}, 0)$ in $\mathcal{M}_2$ is locally modeled by the cone $C(\Sigma_1) \times \Sigma_M$, where $C(\Sigma_1) = (\Sigma_1 \times [0, \epsilon]) / (\Sigma_1 \times \{0\})$ is the cone on the unit simplex. The blow-up replaces the cone point with its base $\Sigma_1$.

### 2.3 Classification of the Singularity

The singularity is **not** a normal crossing (those involve transverse hypersurfaces). It is **not** a cusp (those have non-convex local models). It is precisely a **conifold singularity** of the fibration — the fiber collapses to a point, and the local model is the product of a smooth factor ($\Sigma_M$) with a cone over $\Sigma_1 \simeq \overline{B}^{n-2}$.

Since $\Sigma_1$ is contractible, the cone $C(\Sigma_1)$ is contractible, and the singularity does not introduce any topological obstruction. The homotopy type of $\mathcal{M}_2$ is unchanged by the singularity — $\mathcal{M}_2$ remains contractible.

---

## 3. Energy Landscape on $\mathcal{M}_2$

### 3.1 Energy Decomposition

The K-field energy on $\mathcal{M}_2$ is:

$$\mathcal{E}_K(u_1, u_2) = \underbrace{\mathcal{E}_{\mathrm{self}}(u_1) + \mathcal{E}_{\mathrm{self}}(u_2)}_{\text{self-energies}} + \underbrace{\lambda_{\mathrm{rep}} \langle u_1, u_2 \rangle}_{\text{repulsion}}$$

In blown-up coordinates $(u_1, v_2, m_2)$ with $u_2 = m_2 v_2$:

$$\mathcal{E}_K = \mathcal{E}_{\mathrm{self}}(u_1) + \mathcal{E}_{\mathrm{self}}(m_2 v_2) + \lambda_{\mathrm{rep}} m_2 \langle u_1, v_2 \rangle$$

### 3.2 Energy at $m_2 = 0$ (K=1 Boundary)

At $m_2 = 0$, $u_2 = 0$:

$$\mathcal{E}_K|_{m_2=0} = \mathcal{E}_{\mathrm{self}}(u_1) + \mathcal{E}_{\mathrm{self}}(0) + 0$$

Now $\mathcal{E}_{\mathrm{self}}(0)$ depends on the self-energy's behavior at the zero field. For the SCC energy:

$$\mathcal{E}_{\mathrm{self}}(0) = \lambda_{\mathrm{cl}} E_{\mathrm{cl}}(0) + \lambda_{\mathrm{sep}} E_{\mathrm{sep}}(0) + \lambda_{\mathrm{bd}} E_{\mathrm{bd}}(0)$$

Since $E_{\mathrm{cl}}(u) = \sum_i \sigma^2(a_{\mathrm{cl}}[(Pu)_i - \tau])$ and $P \cdot 0 = 0$, we have $E_{\mathrm{cl}}(0) = n \cdot \sigma^2(-a_{\mathrm{cl}} \tau)$ (the "closure floor" — the penalty for having no closure anywhere). Similarly $E_{\mathrm{sep}}(0) = 0$ (no separation penalty at zero field) and $E_{\mathrm{bd}}(0) = 0$ (no boundary energy at zero field). So:

$$\mathcal{E}_{\mathrm{self}}(0) = \lambda_{\mathrm{cl}} \cdot n \cdot \sigma^2(-a_{\mathrm{cl}} \tau)$$

This is a **positive constant** — the closure energy floor.

### 3.3 The Mass-Transfer Energy Function

Define the **reduced energy** as a function of mass partition alone, optimized over field configurations:

$$\mathcal{F}(m_2) := \inf_{(u_1, u_2) \in \pi^{-1}(m_2)} \mathcal{E}_K(u_1, u_2)$$

This is the energy of the best K-field configuration at mass partition $(M - m_2, m_2)$.

**Proposition 3.1 (Properties of $\mathcal{F}$).**

(a) $\mathcal{F}$ is continuous on $[0, M]$ (energy is continuous, fiber varies continuously in Hausdorff metric on compact subsets).

(b) $\mathcal{F}$ is symmetric under the exchange $m_2 \leftrightarrow M - m_2$ when the graph has sufficient symmetry (so the two formations are equivalent up to repositioning).

(c) $\mathcal{F}(0) = \mathcal{E}_{\mathrm{self}}(u^*_M) + \lambda_{\mathrm{cl}} n \sigma^2(-a_{\mathrm{cl}}\tau)$ where $u^*_M$ is the single-formation minimizer at mass $M$.

(d) $\mathcal{F}(M/2) = 2\mathcal{E}_{\mathrm{self}}(u^*_{M/2}) + \lambda_{\mathrm{rep}} \langle u^*_{M/2,\mathrm{left}}, u^*_{M/2,\mathrm{right}} \rangle$ when the two formations can be well-separated ($\approx 2\mathcal{E}_{\mathrm{self}}(u^*_{M/2})$ for large enough graphs).

*Proof of (a).* The constraint set $\{(u_1, u_2) : \sum u_1^i = M - m_2, \sum u_2^i = m_2, u_k \in [0,1]^n\}$ varies continuously with $m_2$ in the Hausdorff metric (intersection of a continuously moving hyperplane with a fixed compact set). The energy $\mathcal{E}_K$ is continuous. By Berge's maximum theorem, $\mathcal{F}(m_2)$ is continuous. $\square$

### 3.4 Key Question: Curvature of $\mathcal{F}$ at the Symmetric Point

**This is the central question of the merge landscape analysis.**

We compute $\mathcal{F}''(M/2)$ — the curvature of the reduced energy at the symmetric mass partition.

**Informal argument.** At $m_2 = M/2$ with well-separated formations on a large enough graph:

$$\mathcal{F}(m_2) \approx \mathcal{E}_{\mathrm{self}}(u^*_{M-m_2}) + \mathcal{E}_{\mathrm{self}}(u^*_{m_2})$$

(repulsion $\approx 0$ when formations are well-separated). Thus:

$$\mathcal{F}'(m_2) \approx -\frac{\partial}{\partial m} \mathcal{E}_{\mathrm{self}}(u^*_m)\Big|_{m = M-m_2} + \frac{\partial}{\partial m} \mathcal{E}_{\mathrm{self}}(u^*_m)\Big|_{m = m_2}$$

At $m_2 = M/2$ (symmetric point): $\mathcal{F}'(M/2) = 0$ by symmetry.

$$\mathcal{F}''(M/2) \approx \frac{\partial^2}{\partial m^2} \mathcal{E}_{\mathrm{self}}(u^*_m)\Big|_{m=M/2} + \frac{\partial^2}{\partial m^2} \mathcal{E}_{\mathrm{self}}(u^*_m)\Big|_{m=M/2} = 2 \frac{d^2}{dm^2} \mathcal{E}_{\mathrm{self}}(u^*_m)\Big|_{m=M/2}$$

**The sign of $\mathcal{F}''(M/2)$ determines the landscape structure:**

- **If $\frac{d^2}{dm^2} \mathcal{E}_{\mathrm{self}}(u^*_m) > 0$** (self-energy is convex in mass): $\mathcal{F}''(M/2) > 0$, so $m_2 = M/2$ is a **local minimum** of $\mathcal{F}$. Equal-mass partition is stable. Merge (moving mass to one formation) increases energy.

- **If $\frac{d^2}{dm^2} \mathcal{E}_{\mathrm{self}}(u^*_m) < 0$** (self-energy is concave in mass): $\mathcal{F}''(M/2) < 0$, so $m_2 = M/2$ is a **local maximum** of $\mathcal{F}$. Equal-mass partition is unstable. The system spontaneously breaks symmetry, funneling mass toward one formation.

### 3.5 Convexity of Self-Energy in Mass (Isoperimetric Argument)

**Proposition 3.2 (Subadditivity of optimized self-energy).** On graphs with non-increasing isoperimetric ratio (including 2D grids), the optimized self-energy $m \mapsto \mathcal{E}_{\mathrm{self}}(u^*_m)$ is **strictly subadditive**:

$$\mathcal{E}_{\mathrm{self}}(u^*_{m_1+m_2}) < \mathcal{E}_{\mathrm{self}}(u^*_{m_1}) + \mathcal{E}_{\mathrm{self}}(u^*_{m_2})$$

for $m_1, m_2 > 0$. This is the isoperimetric ordering from the Merge Theorem Part (b).

**Connection to convexity.** Subadditivity of $\mathcal{E}_{\mathrm{self}}(u^*_m)$ does NOT immediately determine the sign of $\mathcal{F}''(M/2)$. Subadditivity says $\mathcal{E}_{\mathrm{self}}(u^*_M) < 2\mathcal{E}_{\mathrm{self}}(u^*_{M/2})$ (one big formation is better than two small ones), but this is a global comparison, not a local curvature statement.

**What is actually needed:** the local behavior of $g(m) := \mathcal{E}_{\mathrm{self}}(u^*_m)$ near $m = M/2$. This function encodes how the optimal formation energy changes as mass varies. The key contributions are:

1. **Boundary energy** $\sim \sigma_{\mathrm{eff}} \cdot m^{(d-1)/d}$ (isoperimetric): this is **concave** in $m$ (second derivative $< 0$), which would make $\mathcal{F}''(M/2) < 0$ — favoring asymmetry.

2. **Closure energy** $\sim -\kappa_{\mathrm{cl}} \cdot m$ (roughly linear for concentrated formations): neutral contribution to curvature.

3. **Separation energy**: depends on the double-well and graph geometry; contribution to curvature is parameter-dependent.

**Proposition 3.3 (Boundary-dominated regime).** When the boundary energy term dominates (large $\lambda_{\mathrm{bd}}$ or small $\lambda_{\mathrm{cl}}$), $g''(M/2) < 0$, hence $\mathcal{F}''(M/2) < 0$. The symmetric point is a LOCAL MAXIMUM of $\mathcal{F}$ on the mass-transfer line. This means:

> **In the boundary-dominated regime, the equal-mass K=2 state is unstable to mass transfer. One formation spontaneously cannibalizes the other.**

**Category: B.** (The isoperimetric scaling is proved, but the dominance of the boundary term over closure/separation corrections requires parameter-specific verification.)

### 3.6 Critical Points of $\mathcal{E}_K$ on $\mathcal{M}_2$

A critical point of $\mathcal{E}_K$ on $\mathcal{M}_2$ (equivalently, on $\Sigma_M^{\mathrm{relax}}$) satisfies the first-order condition:

$$\nabla_{u_1} \mathcal{E}_K = \mu_1 \mathbf{1}, \qquad \nabla_{u_2} \mathcal{E}_K = \mu_2 \mathbf{1}$$

with a **single** Lagrange multiplier for total mass (NOT two independent multipliers). That is, $\mu_1 = \mu_2 =: \mu$ (the "chemical potential" is equal across formations).

**Contrast with $\Sigma^2_M$:** On the product manifold with independent mass constraints, each formation has its own Lagrange multiplier. The equal-chemical-potential condition is additional and typically NOT satisfied at the K=2 minimizer of $\Sigma^2_M$.

**Proposition 3.4.** If the K=2 minimizer $(u_1^*, u_2^*)$ on $\Sigma_{m_1} \times \Sigma_{m_2}$ has $\mu_1 \neq \mu_2$ (unequal chemical potentials), then $(u_1^*, u_2^*)$ is NOT a critical point of $\mathcal{E}_K$ on $\Sigma_M^{\mathrm{relax}}$.

*Proof.* On $\Sigma_M^{\mathrm{relax}}$, the tangent space includes mass-transfer directions $\delta = (\epsilon \mathbf{e}_i, -\epsilon \mathbf{e}_j)$ for any nodes $i, j$. The directional derivative along this direction is:

$$D_\delta \mathcal{E}_K = (\nabla_{u_1} \mathcal{E}_K)_i - (\nabla_{u_2} \mathcal{E}_K)_j$$

At the K=2 minimizer on $\Sigma^2_M$: $(\nabla_{u_1} \mathcal{E}_K)_i = \mu_1$ for all interior $i$, and $(\nabla_{u_2} \mathcal{E}_K)_j = \mu_2$ for all interior $j$. So $D_\delta \mathcal{E}_K = \mu_1 - \mu_2 \neq 0$. Hence the gradient on $\Sigma_M^{\mathrm{relax}}$ is nonzero. $\square$

**This is the precise content of Flaw #9 from the critique:** the K=2 minimizer on $\Sigma^2_M$ is generically NOT a critical point on $\Sigma_M^{\mathrm{relax}}$. There is a **mass-transfer force** $\mu_1 - \mu_2$ driving the system away from the fixed-mass equilibrium.

### 3.7 Is $(m_1, m_2) = (M/2, M/2)$ a Saddle, Minimum, or Maximum of $\mathcal{E}_K$ on $\mathcal{M}_2$?

We now have the tools to answer the key question precisely.

**Theorem 3.1 (Landscape at the symmetric point).** Let $(u_1^*, u_2^*)$ be the K=2 minimizer on $\Sigma_{M/2} \times \Sigma_{M/2}$ with well-separated supports. The nature of this point on $\mathcal{M}_2 \cong \Sigma_M^{\mathrm{relax}}$ is:

**(a) Tangent space decomposition.** $T_{(u_1^*,u_2^*)} \Sigma_M^{\mathrm{relax}}$ decomposes as:

$$T = \underbrace{T_{\mathrm{intra}}}_{\text{within-formation}} \oplus \underbrace{T_{\mathrm{transfer}}}_{\text{mass-transfer}}$$

where $T_{\mathrm{intra}} = \{(v_1, v_2) : \sum v_1^i = 0, \sum v_2^i = 0\}$ (dimension $2n-2$) and $T_{\mathrm{transfer}}$ is the 1-dimensional complement (directions where $\sum v_1^i = -\sum v_2^i = \epsilon$).

**(b) Intra-formation curvature.** On $T_{\mathrm{intra}}$, the Hessian is positive definite (this IS the Hessian on $\Sigma^2_M$, proved in Part (a) of the Merge Theorem under $\mu_1 \mu_2 > \lambda_{\mathrm{rep}}^2$).

**(c) Mass-transfer curvature.** The Hessian restricted to $T_{\mathrm{transfer}}$ is:

$$\mathcal{F}''(M/2) = 2g''(M/2) + \text{(repulsion correction)}$$

where $g(m) = \mathcal{E}_{\mathrm{self}}(u^*_m)$ and the repulsion correction depends on how overlap changes with mass redistribution.

- If $g''(M/2) > 0$ (self-energy convex in mass) AND repulsion correction $\geq 0$: the symmetric point is a **local minimum** on $\mathcal{M}_2$ (merge has a barrier in ALL directions).
- If $g''(M/2) < 0$ sufficiently (boundary-dominated): the symmetric point is a **saddle** on $\mathcal{M}_2$ — stable within each fiber (intra-formation), unstable along the mass-transfer direction. **Merge proceeds spontaneously via mass transfer.**

**(d) Symmetry at equal masses.** By the exchange symmetry $u_1 \leftrightarrow u_2$ on homogeneous graphs, the symmetric point has $\mu_1 = \mu_2$ and IS a critical point of $\mathcal{E}_K$ on $\Sigma_M^{\mathrm{relax}}$. This is the unique mass partition where the critique's Flaw #9 does NOT apply.

**Category: A for (a), (b), (d). Category B for (c)** (requires parameter-specific verification of $g''$).

---

## 4. Morse–Bott Analysis

### 4.1 Translation Degeneracy

On a 2D grid, a formation can be **translated** continuously (shifting the field pattern) without changing energy (up to boundary effects). If the graph is a torus (periodic boundary), translation is exact; on a finite grid, it is approximate for formations far from the boundary.

**Proposition 4.1.** On a torus graph $\mathbb{Z}_L^2$, the single-formation minimizer $u^*_m$ at mass $m$ has a continuous $(d = 2)$-dimensional family of translates, all with equal energy. The critical set is diffeomorphic to $\mathbb{T}^2$ (the torus itself).

For K=2 on a torus, the critical manifold is $\mathbb{T}^2 \times \mathbb{T}^2 / \mathbb{Z}_2$ (two independent translation modes, modulo exchange of formations). Dimension of the degenerate critical manifold: $4$ (on a 2D graph) or $2d$ in general.

### 4.2 Morse–Bott Structure

**Definition.** A critical point $p$ of a smooth function $f : M \to \mathbb{R}$ is **Morse–Bott** if the critical set $C$ containing $p$ is a smooth submanifold and $\mathrm{ker}(\mathrm{Hess}_p f) = T_p C$ (the null directions of the Hessian are exactly the tangent directions to the critical manifold).

**Proposition 4.2 (Morse–Bott at K=2 minimizer).** On a torus graph, the K=2 minimizer on $\Sigma^2_M$ (fixed masses) has:
- Critical manifold $C \cong \mathbb{T}^2 \times \mathbb{T}^2 / \mathbb{Z}_2$ (dimension $2d$)
- $\mathrm{ker}(\mathrm{Hess}) = T C$ (translation modes are the only zero-curvature directions)
- Morse–Bott index = 0 (all non-degenerate directions have positive curvature)

On $\mathcal{M}_2$ (relaxed mass), the critical manifold gains one additional dimension (the mass-transfer direction), and the index depends on $\mathrm{sgn}(\mathcal{F}''(M/2))$:
- If $\mathcal{F}''(M/2) > 0$: Morse–Bott index = 0 (still a minimum)
- If $\mathcal{F}''(M/2) < 0$: Morse–Bott index = 1 (saddle with one unstable direction = mass transfer)

### 4.3 Normal Morse Data

The **normal Morse data** at the critical manifold $C$ (in the sense of Goresky–MacPherson) consists of the pair $(D^{\lambda}, D^{n-\lambda-\dim C})$ where $\lambda$ is the Morse–Bott index. For $\lambda = 0$: the normal Morse data is $(D^0, D^{n - \dim C}) = (\mathrm{pt}, D^{n - \dim C})$. This means $C$ contributes to the topology of sublevel sets as an attaching of cells of dimension $\dim C$ — specifically, a thickened copy of $C$.

For $\lambda = 1$: the normal Morse data is $(D^1, D^{n - 1 - \dim C})$. This means $C$ contributes a handle attachment along the unstable direction, changing the topology of sublevel sets by attaching $C \times D^1$.

---

## 5. Stratified Morse Theory (Goresky–MacPherson Framework)

### 5.1 Stratification of $\mathcal{M}_2$

$\mathcal{M}_2$ admits a natural Whitney stratification:

$$\mathcal{M}_2 = S_{\mathrm{int}} \sqcup S_{\partial,0} \sqcup S_{\partial,M} \sqcup S_{\partial,\mathrm{box}}$$

where:
- $S_{\mathrm{int}} = \{(u_1, u_2) : u_k \in (0,1)^n,\; 0 < m_2 < M\}$ — the **open stratum** (smooth manifold of dimension $2n - 1$).
- $S_{\partial,0} = \{(u_1, 0) : u_1 \in \mathrm{int}(\Sigma_M)\}$ — the **K=1 boundary stratum** ($u_2 = 0$, dimension $n - 1$). This is where merged states live.
- $S_{\partial,M} = \{(0, u_2) : u_2 \in \mathrm{int}(\Sigma_M)\}$ — the **symmetric K=1 boundary stratum** ($u_1 = 0$, dimension $n - 1$).
- $S_{\partial,\mathrm{box}}$ — the **box boundary strata** (where some $u_k^i \in \{0, 1\}$), which are further decomposed into faces of various dimensions.

**Whitney conditions.** The stratification satisfies Whitney's conditions (a) and (b) because each stratum is a face of the convex polytope $\Sigma_M^{\mathrm{relax}}$, and the faces of convex polytopes form Whitney stratifications (this is a standard result, cf. Goresky–MacPherson §1.2).

### 5.2 Critical Sets on Each Stratum

**On $S_{\mathrm{int}}$:** Critical points satisfy $\nabla_{u_1} \mathcal{E}_K = \mu \mathbf{1}$, $\nabla_{u_2} \mathcal{E}_K = \mu \mathbf{1}$ (equal chemical potentials). These are the "true" K=2 critical points on the relaxed manifold. By Proposition 3.4, they occur at mass partitions where the chemical potentials happen to be equal — generically, only the symmetric partition $m_1 = m_2 = M/2$ (on homogeneous graphs).

**On $S_{\partial,0}$:** Critical points satisfy $\nabla_{u_1} \mathcal{E}_{\mathrm{self}}(u_1) = \mu \mathbf{1}$ (single-formation criticality) plus the **inward normal condition**: $\frac{\partial \mathcal{E}_K}{\partial u_2^i}\Big|_{u_2=0} \geq \mu$ for all $i$ (KKT condition for the $u_2 \geq 0$ constraint). This means:

$$\frac{\partial \mathcal{E}_{\mathrm{self}}}{\partial u_2^i}\Big|_{u_2=0} + \lambda_{\mathrm{rep}} u_1^i \geq \mu$$

The repulsion term $\lambda_{\mathrm{rep}} u_1^i > 0$ wherever $u_1$ is nonzero, which **helps satisfy** the KKT condition. Repulsion makes it energetically unfavorable to "nucleate" the second formation near the first, reinforcing the K=1 state.

**On $S_{\partial,M}$:** Symmetric to $S_{\partial,0}$.

### 5.3 How Critical Sets Connect Across Strata

The central question of stratified Morse theory: how do the critical sets on $S_{\mathrm{int}}$ and $S_{\partial,0}$ relate?

**Scenario A (Merge has barrier).** If $\mathcal{F}''(M/2) > 0$ (symmetric K=2 is a local min on $\mathcal{M}_2$):
- The K=2 critical set on $S_{\mathrm{int}}$ is a local minimum.
- The K=1 critical set on $S_{\partial,0}$ is also a local minimum (on its stratum).
- Between them, there must be a **saddle** (by the mountain pass theorem on the stratified space).
- This saddle may lie on $S_{\mathrm{int}}$ (an interior saddle with $m_2$ small but positive) or on a boundary stratum (a saddle where some $u_k^i$ saturates).

**Scenario B (Merge is downhill along mass-transfer).** If $\mathcal{F}''(M/2) < 0$ (symmetric K=2 is a saddle on $\mathcal{M}_2$):
- The K=2 critical set on $S_{\mathrm{int}}$ has Morse–Bott index 1.
- There is a **gradient flow line** from the K=2 saddle to the K=1 minimum on $S_{\partial,0}$, passing through configurations with decreasing $m_2$.
- No barrier — merge proceeds along the unstable manifold of the saddle.
- However, the K=2 point is still a minimum of the RESTRICTED energy on each fiber $\Sigma_{M/2} \times \Sigma_{M/2}$. The instability is ONLY in the mass-transfer direction.

**Scenario C (Non-symmetric masses).** If $m_1 \neq m_2$, Proposition 3.4 says the K=2 minimizer on $\Sigma^2_M$ is NOT a critical point on $\mathcal{M}_2$. In this case, there is a nonzero mass-transfer force, and the system flows along $\mathcal{M}_2$ toward the mass partition where chemical potentials equalize — or directly to $S_{\partial,0}$ if no interior equilibrium exists.

### 5.4 Stratified Mountain Pass

**Theorem 5.1 (Stratified Mountain Pass).** Let $\mathcal{E}_K : \mathcal{M}_2 \to \mathbb{R}$ be the K-field energy on the stratified space $\mathcal{M}_2$. Suppose:
- (H1) There exists a critical point $p \in S_{\mathrm{int}}$ that is a strict local minimum of $\mathcal{E}_K|_{S_{\mathrm{int}}}$.
- (H2) There exists a point $q \in S_{\partial,0}$ with $\mathcal{E}_K(q) < \mathcal{E}_K(p)$.
- (H3) $p$ and $q$ can be connected by a continuous path in $\mathcal{M}_2$.

Then the minimax value $c = \inf_{\gamma \in \Gamma} \max_{t} \mathcal{E}_K(\gamma(t))$ satisfies $c > \mathcal{E}_K(p)$, and either:
- (i) There exists a critical point $r \in S_{\mathrm{int}}$ with $\mathcal{E}_K(r) = c$ (interior mountain pass), or
- (ii) The minimax is achieved on a boundary stratum, and $c$ is a "stratified critical value" in the sense of Goresky–MacPherson.

*Proof sketch.* The argument follows the standard deformation lemma, adapted for stratified spaces (Goresky–MacPherson, Part II, §3). The key point is that the negative gradient flow of $\mathcal{E}_K$ preserves the stratification (the boundary $u_k^i \geq 0$ is respected by projected gradient flow). Therefore the flow cannot "jump" from $S_{\mathrm{int}}$ to $S_{\partial,0}$ in finite time unless the energy at $S_{\partial,0}$ is already lower — which is exactly the condition for a barrier to exist.

The Mountain Pass theorem for manifolds with boundary (cf. Ghoussoub 1993) guarantees a critical point at level $c$, but it may be a boundary critical point (satisfying KKT conditions rather than $\nabla \mathcal{E}_K = 0$). $\square$

**Hypothesis verification:**
- (H1): Requires $\mathcal{F}''(M/2) > 0$ (the symmetric K=2 point must be a local min on ALL of $\mathcal{M}_2$, not just on the fiber). This is the content of Scenario A and is parameter-dependent.
- (H2): Follows from isoperimetric ordering (Merge Theorem Part (b)), provided the closure floor $\mathcal{E}_{\mathrm{self}}(0)$ is not too large. We need $\mathcal{E}_{\mathrm{self}}(u^*_M) + \mathcal{E}_{\mathrm{self}}(0) < 2\mathcal{E}_{\mathrm{self}}(u^*_{M/2})$. Since $\mathcal{E}_{\mathrm{self}}(u^*_M) < 2\mathcal{E}_{\mathrm{self}}(u^*_{M/2})$ (isoperimetric) and $\mathcal{E}_{\mathrm{self}}(0) > 0$ (closure floor), this requires $\mathcal{E}_{\mathrm{self}}(0) < 2\mathcal{E}_{\mathrm{self}}(u^*_{M/2}) - \mathcal{E}_{\mathrm{self}}(u^*_M)$.
- (H3): Trivially satisfied — $\mathcal{M}_2$ is path-connected (it is a convex polytope).

**Category: B.** (H1 is the unresolved parameter-dependent condition.)

---

## 6. Summary: The Complete Landscape Picture

### 6.1 What Is Rigorously Established (Cat A)

1. **Manifold structure:** $\mathcal{M}_2 \cong \Sigma_M^{\mathrm{relax}}$ is a convex polytope of dimension $2n - 1$, contractible, with the fibration $\pi : \mathcal{M}_2 \to [0,M]$ having degenerate fibers at $m_2 \in \{0, M\}$ (cone singularities resolved by blow-up).

2. **K=2 on $\Sigma^2_M$ is a local minimum** (of the restricted energy, under $\mu_1 \mu_2 > \lambda_{\mathrm{rep}}^2$).

3. **K=2 on $\mathcal{M}_2$ has zero mass-transfer gradient at equal masses** ($\mu_1 = \mu_2$ by symmetry). At unequal masses, the K=2 minimizer on $\Sigma^2_M$ is NOT a critical point on $\mathcal{M}_2$ (Proposition 3.4).

4. **The K=1 point $(u^*_M, 0)$ lies on the boundary stratum $S_{\partial,0}$** and is a KKT critical point. Repulsion reinforces its stability.

5. **Path connectivity:** A continuous path from K=2 to K=1 exists on $\mathcal{M}_2$ (convexity).

6. **Blow-up resolution:** The singularity at $m_2 = 0$ is a cone point with exceptional divisor $\Sigma_M \times \Sigma_1$, parametrizing the "ghost shape" of the vanishing formation.

### 6.2 What Is Parameter-Dependent (Cat B)

7. **The sign of $\mathcal{F}''(M/2)$** determines whether the symmetric K=2 point is a local minimum (barrier exists) or a saddle (merge is spontaneous along mass-transfer direction). The boundary-energy-dominated regime has $\mathcal{F}'' < 0$ (saddle), while strong closure energy or repulsion may yield $\mathcal{F}'' > 0$ (minimum).

8. **If $\mathcal{F}''(M/2) > 0$:** Stratified Mountain Pass guarantees a barrier and a critical point (interior or boundary) between K=2 and K=1. The Morse–Bott index of the K=2 critical manifold is 0.

9. **If $\mathcal{F}''(M/2) < 0$:** The K=2 critical manifold has Morse–Bott index 1 on $\mathcal{M}_2$. Merge proceeds along the unstable direction without a barrier. The K=2 state is still a minimum on each fixed-mass fiber $\Sigma^2_M$, so per-formation mass constraints provide absolute protection.

### 6.3 What Is Not Determined by This Analysis

10. **The precise value of $\mathcal{F}''(M/2)$ for specific SCC parameters.** This requires numerical computation (differentiating the optimized self-energy with respect to mass).

11. **The nature of the transition state** (if it exists): whether it is an interior or boundary critical point, its Morse index, and its energy.

12. **The Kramers rate:** requires the transition state to be identified and its Hessian computed. This analysis provides the framework but not the numerical values.

### 6.4 Resolution of Prior Issues

| Issue | Resolution |
|-------|------------|
| Flaw #1 (endpoint $\notin \Sigma^K_M$) | **Resolved:** work on $\mathcal{M}_2 \cong \Sigma_M^{\mathrm{relax}}$ where $(u^*_M, 0) \in S_{\partial,0} \subset \mathcal{M}_2$ |
| Flaw #2 (Mountain Pass on manifold with boundary) | **Addressed:** use stratified Mountain Pass (Ghoussoub 1993) with KKT conditions on boundary strata |
| Flaw #9 (local minimality on wrong manifold) | **Diagnosed precisely:** Proposition 3.4 shows K=2 min on $\Sigma^2_M$ is NOT critical on $\mathcal{M}_2$ unless $\mu_1 = \mu_2$. Equal-mass case is special |
| Flaw F (merge undefined in fixed-K) | **Resolved:** merge is a path on $\mathcal{M}_2$ from interior to boundary stratum; the fibration gives the mass-transfer interpretation |

---

## 7. Directions for Numerical Verification

The key empirical question is the sign of $\mathcal{F}''(M/2)$. This can be tested by:

1. **Mass sweep experiment:** For a fixed graph, compute $\mathcal{E}_{\mathrm{self}}(u^*_m)$ for $m \in [m_{\min}, m_{\max}]$ (sweeping mass through the admissible range) and fitting a quadratic to determine $g''$.

2. **Chemical potential comparison:** At the K=2 minimizer on $\Sigma_{m_1} \times \Sigma_{m_2}$ with $m_1 \neq m_2$, compute $\mu_1$ and $\mu_2$. The sign of $\mu_1 - \mu_2$ indicates the direction of mass-transfer force. If $\mu_1 > \mu_2$ when $m_1 > m_2$, the force drives toward equal masses (stabilizing); if $\mu_1 < \mu_2$, the force drives toward asymmetry (destabilizing).

3. **Direct Hessian computation:** At the symmetric K=2 point on $\Sigma_M^{\mathrm{relax}}$, compute the full Hessian projected onto $T(\Sigma_M^{\mathrm{relax}})$, including the mass-transfer direction. Check for negative eigenvalues.

---

## References

1. Goresky, M. & MacPherson, R. (1988). *Stratified Morse Theory*. Springer. — Stratified critical point theory.
2. Ghoussoub, N. (1993). *Duality and Perturbation Methods in Critical Point Theory*. Cambridge Univ. Press. — Mountain Pass on manifolds with boundary.
3. Ambrosetti, A. & Rabinowitz, P. H. (1973). Dual variational methods in critical point theory. *J. Funct. Anal.*, 14, 349–381. — Mountain Pass Theorem.
4. Bott, R. (1954). Nondegenerate critical manifolds. *Ann. Math.*, 60, 248–261. — Morse–Bott theory.
5. Whitney, H. (1965). Tangents to an analytic variety. *Ann. Math.*, 81, 496–549. — Whitney stratifications.
6. Berge, C. (1963). *Topological Spaces*. Oliver & Boyd. — Maximum theorem for continuous optimization.
