# symmetry_moduli.md — G-D Aut(G) Moduli Space $\mathcal{M}_1$ (First-Step Analysis)

**⚠️ STATUS UPDATE (2026-04-22 R22)**:
- **§3.3 G-D Cubic Coefficient Theorem (2D square)**: Cat A **maintained** (Layer 2 geometric).
- **§3.6 $C_n$/$T^2$ $\Phi_4$ analysis**: Cat A **maintained** (Layer 2).
- **§3.6.3 Universal $A_2/A_1 \in \{2, 4\}$ classification**: Cat A **maintained**.
- **§3.7.3 $C_n$ Lock-In Theorem**: Cat A maintained (Layer 2 structural).
- **§3.7.5 Conjecture 2.1-Bott (extensive scaling on torus)**: **RETRACTED** by R17+R19+V7 data.
  - R17 (c=0.3): torus/square ratio = 0.55 (예측 ~32) — refuted
  - R19 (c=0.7): torus/square ratio = 1.00 (예측 ~32) — refuted
  - **$\mathrm{Vol}(\mathrm{Iso}_0)$ static orbit volume은 Layer 1 topology에서 유효**, 하지만 dynamic K̂으로 전이되는 extensive scaling 주장은 무효.
- **K-sector extensions**: $\mathcal{M}_K$ for K≥2는 **Formation Quantization** framework 아래 각 K-sector의 orbit 구조로 재정의. See `step_cohesion.md` §7.
- **Canonical reorganization**: Moduli theorems은 Layer 1 (topology) vs Layer 2 (geometric) 분리. §3.3 axis-selection은 Layer 2 (energy comparison), $\mathcal{M}_K$ orbit structure는 Layer 1 (topological).

**Status:** first-step scoping, 2026-04-22 Round 2 **+ R22 Conjecture 2.1-Bott retraction + K-sector reorganization**.
**Author origin:** Round 15 identified G-D gap and explicitly scoped it out; Round 2 of 2026-04-22 provides the first-step structural analysis.
**Canonical refs:** §13 Cat A Prop 1.1 (Σ_m convex polytope), T8-Core scaling caveat (Fiedler eigenvalue $\lambda_2$ role on non-expander families), T-Birth-Parametric (D4 supercritical pitchfork).
**Working refs:** `working/SF/mode_count.md` (Prop 1.3a/b spectral base), `working/SF/cardinality_open.md` §8 (Morse index structure), `working/MF/from_single.md` §2 (K̂ graph-class formula).
**External refs:** Crandall-Rabinowitz (1971), *Bifurcation from simple eigenvalues*; Goresky-MacPherson (1988), *Stratified Morse theory*; Fässler-Stiefel (1992), *Group theoretical methods and their applications*.

---

## §1. Setup

### 1.1 Automorphism group

Let $G = (X, E)$ be a finite connected graph. Let $\mathrm{Aut}(G) = \{\pi \in S_n : \pi \text{ preserves adjacency}\}$ be the automorphism group — the symmetry group of the graph. $\pi \in \mathrm{Aut}(G)$ acts on $[0,1]^n$ via $(\pi\cdot u)(x) := u(\pi^{-1}(x))$; this action preserves $\Sigma_m$ (mass is symmetric) and $\mathcal{E}$ (energy depends only on graph structure and the field values).

**Examples:**
- $L \times L$ **square grid (free BC):** $\mathrm{Aut}(G) = D_4$ (dihedral of order 8: 4 rotations + 4 reflections).
- $L \times L$ **torus (periodic BC):** $\mathrm{Aut}(G) = D_4 \times (\mathbb Z_L)^2$ (D4 × translation group).
- **1D cycle $C_n$:** $\mathrm{Aut}(G) = D_n$ (dihedral, $2n$ elements).
- **Complete graph $K_n$:** $\mathrm{Aut}(G) = S_n$ (symmetric group).
- **Generic random graph:** $\mathrm{Aut}(G) = \{e\}$ trivial.

### 1.2 Invariant / equivariant structure

- $\mathcal{E} : \Sigma_m \to \mathbb R$ is $\mathrm{Aut}(G)$-invariant: $\mathcal{E}(\pi\cdot u) = \mathcal{E}(u)$.
- The gradient $\nabla\mathcal{E}$ is $\mathrm{Aut}(G)$-equivariant: $\nabla\mathcal{E}(\pi\cdot u) = \pi\cdot \nabla\mathcal{E}(u)$.
- The Hessian $\mathrm{Hess}\,\mathcal{E}$ commutes with the $\mathrm{Aut}(G)$ action on $T_u\Sigma_m$.

**Consequence:** critical points come in **$\mathrm{Aut}(G)$-orbits**. The set of critical points is a union of $\mathrm{Aut}(G)$-orbits.

---

## §2. The moduli space $\mathcal{M}_1$

### 2.1 Definition

> **Definition 2.1 ($\mathcal{M}_1$).** The **moduli space of K=1 single-formation minimizers** on Σ_m is
> $$\mathcal{M}_1(\beta, \alpha, c, G) := \{u^\ast \in \Sigma_m : u^\ast \text{ is a local min of }\mathcal{E},\; K_{\mathrm{soft}}(u^\ast) \approx 1\}/\mathrm{Aut}(G).$$

This is the quotient of K=1 local minima by the graph automorphism group. It is a **set** (generally discrete) for generic Morse $\mathcal{E}$, with size $|\mathcal{M}_1| = N_{\mathrm{min}}^{K=1} / |\mathrm{Aut}(G)|_{\mathrm{avg}}$.

**Special cases:**
- **D4 square grid:** $|\mathcal{M}_1|$ typically equals number of orbit classes of K=1 minimizers; on 2D grid at $\beta$ slightly above $\beta_{\mathrm{crit}}^{(2)}$, only 1 orbit (all Fiedler-mode minimizers equivalent up to D4). At larger $\beta$ (multi-location possible), more orbits emerge.
- **1D cycle $C_n$:** translations of the single-formation bump all equivalent under $D_n$; $|\mathcal{M}_1| = 1$ at all $\beta$.
- **Random graph:** $\mathrm{Aut} = \{e\}$, so $\mathcal{M}_1 = \{$all K=1 minimizers$\}$ no identification.

### 2.2 Relation to Prop 1.3a

From Prop 1.3a: $u_{\mathrm{uniform}}$ has Morse index $N_{\mathrm{unst}}^{\mathrm{bd}}$; each "descent direction" is a Laplacian eigenvector $\phi_k$ with $\mu_k^{\mathrm{bd}} < 0$. Eigenvectors transform under $\mathrm{Aut}(G)$ in irreducible representations (irreps).

**On 2D square grid ($D_4$-equivariance):** Laplacian eigenspaces decompose into $D_4$ irreps (trivial, sign, $(1,1)$, two 2D irreps — total five irreps of $D_4$). Degenerate eigenspaces (same $\lambda_k$) occur when eigenvalues cluster, e.g., the Fiedler eigenspace $\{\phi_{1,0}, \phi_{0,1}\}$ carries the 2D irrep (standard representation of $D_4$).

**Descent from $u_{\mathrm{uniform}}$ along this 2D irrep** yields a $D_4$-orbit of minimizers, not a single pair. Specifically: the parametrized direction $a\phi_{1,0} + b\phi_{0,1}$ has amplitude that saturates to $|(a,b)| = O(1)$ via the nonlinear Allen-Cahn dynamics. Rotating $(a,b) \to (a\cos\theta - b\sin\theta, a\sin\theta + b\cos\theta)$ moves through a **continuous family** if the descent were rotationally invariant — but the grid discretization breaks continuous $SO(2)$ to $D_4$ (4 rotations + 4 reflections = 8 discrete orbit points).

So the first Fiedler pitchfork at $\beta = \beta_{\mathrm{crit}}^{(2)}$ on 2D grid gives an **8-point orbit** of minimizers. After quotienting: $|\mathcal{M}_1| = 1$ at $\beta$ just above $\beta_{\mathrm{crit}}^{(2)}$.

---

## §3. Equivariant bifurcation theory

### 3.1 Crandall-Rabinowitz under $D_4$

At $\beta = \beta_{\mathrm{crit}}^{(2)}$, $u_{\mathrm{uniform}}$ loses stability along the Fiedler subspace $V_2 = \mathrm{span}(\phi_{1,0}, \phi_{0,1})$ (2D representation of $D_4$). Equivariant Crandall-Rabinowitz theorem (Sattinger 1979, *Group theoretic methods in bifurcation theory*) states: given a branching eigenspace $V_2$ with irrep $\rho$ of $D_4$, the bifurcating solutions lie in **isotropy subgroups** of $D_4$'s action on $V_2$.

**Isotropy subgroups of $D_4$ on $V_2$:**
- Subgroup $\langle r^2 \rangle = \mathbb Z_2$ (180° rotation): fixes lines through origin; solutions $a\phi_{1,0} + b\phi_{0,1}$ with arbitrary $(a,b)$ but $(a,b) \sim (-a,-b)$.
- Subgroup $\langle s, r^2\rangle = \mathbb Z_2 \times \mathbb Z_2$: fixes vertical axis $(b = 0)$ and horizontal axis $(a = 0)$ — "axis-aligned" Fiedler modes.
- Subgroup $\langle sr\rangle$: fixes diagonal axes $(a = \pm b)$ — "diagonal" Fiedler modes.
- Trivial subgroup: generic $(a, b)$.

**Consequence.** The first pitchfork yields **two distinct orbit types**:
- **Axis-aligned orbits** (4 orbit points: $\pm(1,0)$ and $\pm(0,1)$ scaled): correspond to single-formation pattern aligned with grid axes.
- **Diagonal orbits** (4 orbit points: $\pm(1,1)$ and $\pm(1,-1)$ scaled): correspond to patterns aligned with grid diagonals.

**Which orbit has lower energy?** This is a nonlinear question (the linearization is degenerate in the 2D subspace); equivariant branching lemma (Golubitsky-Schaeffer-Stewart 1988) gives:
- If the **cubic coefficient** $A_{\mathrm{axis}}$ at axis-aligned is larger (in magnitude) than $A_{\mathrm{diag}}$, then diagonal is selected.
- Computation of $A_{\mathrm{axis}}, A_{\mathrm{diag}}$ requires $\Phi_4 = \int \phi^4$ integrals against each symmetry pattern.

**Status update (Round 3, 2026-04-22 evening).** Computation now carried out; see §3.3 below.

### 3.3 Explicit $\Phi_4$ computation — axis-aligned orbit is selected (Round 3 Cat A)

**Continuum reduction on $[0,1]^2$.** For the first Fiedler eigenspace of the 2D Laplacian on the unit square (free BC), eigenvectors (normalized to $\int \phi^2 = 1$):
$$\phi_{1,0}(x, y) = \sqrt 2\, \cos(\pi x),\qquad \phi_{0,1}(x, y) = \sqrt 2\, \cos(\pi y).$$

**Parametrized descent.** Write the reduced field along the Fiedler subspace as
$$u(x, y) = c + a\,\phi_{1,0}(x, y) + b\,\phi_{0,1}(x, y).$$
Energy expansion around $u_{\mathrm{uniform}}$ (gradient-flow Lyapunov function $F$) to fourth order in $(a, b)$:

Recall $W(c + \delta) = W(c) - \tfrac{1}{4}\delta + \tfrac{1}{2}\delta^2 + \text{cubic} + \delta^4 + \ldots$ with cubic/quartic specifically (at $c = 1/2$, $W(u) = u^2(1-u)^2$):
$W(1/2 + \delta) = 1/16 - \delta^2/2 + \delta^4$ (no cubic at $c = 1/2$ by odd symmetry).

So $W_4$-coefficient = $+1$, and $W' = -\delta + 4\delta^3$ with cubic coefficient $+4$. (Confirms `energy.py::double_well_deriv`.)

**Reduction of double-well term to $(a, b)$:**
$\int W(c + \delta u)\, dx\,dy = W(c) - \tfrac{1}{2}\int (\delta u)^2 + \int (\delta u)^4$.

$\int (a\phi_{10} + b\phi_{01})^2 = a^2 + b^2$ (orthonormal).

$\int (a\phi_{10} + b\phi_{01})^4 = a^4 I_4 + 4 a^3 b J + 6 a^2 b^2 K + 4 a b^3 J + b^4 I_4,$
where $I_4 = \int \phi_{10}^4$, $K = \int \phi_{10}^2 \phi_{01}^2$, $J = \int \phi_{10}^3 \phi_{01}$.

**Evaluation of $J$.** By reflection $x \to 1-x$: $\phi_{10}(1-x, y) = -\phi_{10}(x, y)$ (odd), $\phi_{01}(1-x, y) = \phi_{01}(x, y)$ (even in $x$). So integrand $\phi_{10}^3 \phi_{01}$ is odd in $x$, integral = 0. **$J = 0$.**

**Evaluation of $I_4$:**
$$I_4 = \int_0^1 \int_0^1 [\sqrt 2 \cos(\pi x)]^4 \, dx\, dy = 4\int_0^1 \cos^4(\pi x)\, dx = 4 \cdot \frac{3}{8} = \frac{3}{2}.$$

**Evaluation of $K$:**
$$K = \int_0^1 \int_0^1 [\sqrt 2 \cos(\pi x)]^2 [\sqrt 2 \cos(\pi y)]^2\, dx\, dy = 4 \cdot \int_0^1 \cos^2(\pi x)\, dx \cdot \int_0^1 \cos^2(\pi y)\, dy = 4 \cdot \tfrac{1}{2}\cdot \tfrac{1}{2} = 1.$$

**Key ratio:** $K/I_4 = 2/3$.

**Reduced Lyapunov function (gradient-flow energy):**
$$F(a, b) = \tfrac{1}{2}\mu(a^2 + b^2) + \tfrac{1}{4}\alpha(a^4 + b^4) + \tfrac{1}{2}\beta\, a^2 b^2,$$
where $\mu < 0$ (unstable uniform), $\alpha = \beta_{\mathrm{bd}}\cdot 4 \cdot I_4 = 4\beta_{\mathrm{bd}}\cdot 3/2 = 6\beta_{\mathrm{bd}}$, $\beta = \beta_{\mathrm{bd}}\cdot 4 \cdot 6 K / 2 = 12\beta_{\mathrm{bd}}K = 12\beta_{\mathrm{bd}}$ (the factor 6 comes from the $6a^2b^2 K$ term; factor 1/2 from $F$ normalization; factor 4 from quartic coefficient of $W$; note we absorb $\beta_{\mathrm{bd}}$ for the double-well weight).

**Cleaner form:** write $F(a, b) = \tfrac{\mu}{2}(a^2+b^2) + A_1(a^4 + b^4) + A_2 a^2 b^2$ with $A_1 = \beta_{\mathrm{bd}}I_4 = 3\beta_{\mathrm{bd}}/2$, $A_2 = 6\beta_{\mathrm{bd}}K = 6\beta_{\mathrm{bd}}$. The ratio $A_2/A_1 = 6 K/I_4 = 4$.

**Equilibria.**

(a) **Axis-aligned** $(A, 0)$: $\partial F/\partial a = 0 \Rightarrow \mu A + 4A_1 A^3 = 0 \Rightarrow A^2 = -\mu/(4A_1)$.
Energy: $F_{\mathrm{axis}} = \tfrac{\mu}{2}A^2 + A_1 A^4 = -\tfrac{\mu^2}{8A_1} + A_1 \cdot \tfrac{\mu^2}{16 A_1^2} = -\tfrac{\mu^2}{16 A_1}$.

(b) **Diagonal** $(B, B)$: $\partial F/\partial a = \mu B + 4 A_1 B^3 + 2 A_2 B \cdot B^2 = 0 \Rightarrow B^2 = -\mu/(4A_1 + 2A_2)$.
Energy: $F_{\mathrm{diag}} = \mu B^2 + A_1(2B^4) + A_2 B^4 = \mu B^2 + (2A_1 + A_2) B^4$.
Substituting $B^2 = -\mu/(4A_1 + 2A_2)$: $F_{\mathrm{diag}} = -\tfrac{\mu^2}{4A_1 + 2A_2} + (2A_1 + A_2)\tfrac{\mu^2}{(4A_1 + 2A_2)^2} = -\tfrac{\mu^2}{4A_1 + 2A_2}\cdot (1 - \tfrac{2A_1+A_2}{4A_1+2A_2}) = -\tfrac{\mu^2}{4A_1 + 2A_2}\cdot \tfrac{2A_1 + A_2}{4A_1 + 2A_2} = -\tfrac{\mu^2(2A_1+A_2)}{(4A_1+2A_2)^2}$.

Simplify with $A_2/A_1 = 4$: $2A_1 + A_2 = 2A_1 + 4A_1 = 6A_1$. $4A_1 + 2A_2 = 4A_1 + 8A_1 = 12 A_1$.
$F_{\mathrm{diag}} = -\tfrac{\mu^2 \cdot 6 A_1}{(12 A_1)^2} = -\tfrac{\mu^2}{24 A_1}$.

$F_{\mathrm{axis}} = -\tfrac{\mu^2}{16 A_1}$, $F_{\mathrm{diag}} = -\tfrac{\mu^2}{24 A_1}$.

**Comparison:** $|F_{\mathrm{axis}}| = \mu^2/(16 A_1) > \mu^2/(24 A_1) = |F_{\mathrm{diag}}|$ ⇒ **axis energy is LOWER (more negative)** since $1/16 > 1/24$.

**Stability check (Hessian at each orbit).** At axis $(A, 0)$:
$F_{aa} = \mu + 12 A_1 A^2 + 2 A_2 \cdot 0 = \mu + 12 A_1\cdot(-\mu/(4A_1)) = \mu - 3\mu = -2\mu > 0$ (since $\mu < 0$). ✓ 
$F_{bb} = \mu + 2 A_2 A^2 = \mu + 2\cdot 4A_1\cdot(-\mu/(4A_1)) = \mu - 2\mu = -\mu > 0$. ✓
Both positive ⇒ **axis is minimum**.

At diagonal $(B, B)$:
$F_{aa} = \mu + 12 A_1 B^2 + 2 A_2 B^2 = \mu + (12 A_1 + 2 A_2) B^2 = \mu + (12 + 8) A_1\cdot(-\mu/(12 A_1)) = \mu - 20\mu/12 = -8\mu/12 = -2\mu/3 > 0$. ✓
$F_{ab} = 4 A_2 B\cdot B = 4 A_2 B^2 = 32 A_1 \cdot (-\mu/(12 A_1)) = -32\mu/12 = -8\mu/3 > 0$. 
Hessian eigenvalues at diagonal $= F_{aa} \pm F_{ab} = -2\mu/3 \pm -8\mu/3 = \{-10\mu/3, +2\mu\}$. With $\mu < 0$: $\{+10|\mu|/3, -2|\mu|\}$ — **one negative eigenvalue, diagonal is SADDLE** (Morse index 1).

**Summary (Round 3 Cat A):**

> **G-D Cubic Coefficient Theorem (2D square grid, continuum limit, $c = 1/2$).** At the first Fiedler pitchfork on 2D square grid (free BC), equivariant Crandall-Rabinowitz reduction gives $F(a, b) = \tfrac{\mu}{2}(a^2 + b^2) + A_1(a^4 + b^4) + A_2 a^2 b^2$ with $A_1 = \tfrac{3}{2}\beta_{\mathrm{bd}}$, $A_2 = 6\beta_{\mathrm{bd}}$, ratio $A_2/A_1 = 4$. The **axis-aligned orbit** $\{(\pm A, 0), (0, \pm A)\}$ is a 4-point minimum orbit with $F_{\mathrm{axis}} = -\mu^2/(16A_1)$. The **diagonal orbit** $\{(\pm B, \pm B)\}$ is a 4-point saddle orbit (Morse index 1) with $F_{\mathrm{diag}} = -\mu^2/(24 A_1)$. Axis is selected.

**Category:** **Cat A** — explicit integral computation + elementary algebra at each step.

### 3.4 Lattice correction to $(I_4, K)$

For finite $L \times L$ grid, eigenvectors:
$\phi_{1,0}(i, j) = (2/L)\cos(\pi(i+1/2)/L)$ (normalization $\sum \phi^2 = 1$).

Using Riemann-sum-to-integral with $O(1/L^2)$ correction:
$I_4^{\mathrm{lattice}} = \sum_{i,j} \phi_{10}(i,j)^4 = \int_0^1\phi_{10}^4 dx\cdot \int_0^1 dy \cdot (1 + O(1/L^2)) = \tfrac{3}{2}(1 + O(1/L^2))$.
$K^{\mathrm{lattice}} = 1 \cdot (1 + O(1/L^2))$.

The ratio $A_2/A_1 = 4$ is preserved up to $O(1/L^2)$. **Axis selection holds at any $L \geq 4$** (finite-grid correction too small to flip the inequality $1/16 > 1/24$, which has 50% margin).

### 3.5 Implication for $\mathcal{M}_1$ structure

**At $\beta$ just above $\beta_{\mathrm{crit}}^{(2)}$ on 2D square grid:**
- $|\mathcal{M}_1| = 1$ (single minimum orbit = axis-aligned).
- Orbit size = 4 (4 axis directions: $\pm x, \pm y$).
- Diagonal orbit (4 saddles) present but not minimum.
- Prop 1.3a's $N_{\mathrm{unst}}^{\mathrm{bd}} = 2$ (Fiedler eigenspace is 2D), but $c_1$ (Morse index-1 saddles) gets contribution from the 4 diagonal saddles.

**Euler constraint verification (`cardinality_open.md` §8.1):** $c_0 - c_1 + \ldots = 1$.
At $\beta$ just above $\beta_{\mathrm{crit}}^{(2)}$: $c_0 = 1$ (axis orbit, 1 class), $c_1 \geq 1$ (diagonal orbit + $u_{\mathrm{uniform}}$'s contribution via its Morse index 2)... this gets intricate.

Actually $u_{\mathrm{uniform}}$ is index-$N_{\mathrm{unst}}^{\mathrm{bd}} = 2$ at this $\beta$. $c_2 \geq 1$ (for $u_{\mathrm{uniform}}$). Diagonal saddle is index 1 on the Fiedler-only reduction, but full Σ_m Hessian adds the orthogonal modes (all positive since $\lambda_k > \lambda_2$ for $k \geq 3$); so diagonal orbit is index 1 on full Σ_m. $c_1 \geq 1$ (diagonal class).

Checking: $c_0 - c_1 + c_2 \geq 1 - 1 + 1 = 1$. ✓ (Exact if no other critical points; otherwise $\geq$.)

**Consistent with Hypothetical Theorem 4.1* (`cardinality_open.md` §8.5) (A)-(D).**

### 3.2 Consequence for $\mathcal{M}_1$ at $\beta$ just above $\beta_{\mathrm{crit}}^{(2)}$

$|\mathcal{M}_1| = $ number of orbit types selected by the cubic coefficient analysis.
- If axis-aligned selected: $|\mathcal{M}_1| = 1$ (the axis-aligned orbit).
- If diagonal selected: $|\mathcal{M}_1| = 1$ (diagonal orbit).
- Symmetric case ($A_{\mathrm{axis}} = A_{\mathrm{diag}}$ accidentally): both orbit types are local minima, $|\mathcal{M}_1| = 2$.

For generic parameters, either axis or diagonal is selected, not both; $|\mathcal{M}_1| = 1$ near $\beta_{\mathrm{crit}}^{(2)}$.

---

## §3.6. Non-D4 graph classes — 1D cycle and 2D torus (Round 4, 2026-04-22)

Round 3's result (§3.3) covered 2D square with free BC ($\mathrm{Aut} = D_4$). Round 4 extends to two graph classes where **translation symmetry** enlarges $\mathrm{Aut}(G)$: the 1D cycle $C_n$ and the 2D torus $T^2$.

### 3.6.1 1D cycle $C_n$

Fiedler eigenvalue $\lambda_2 = 4\sin^2(\pi/n)$ is 2-fold degenerate (from $k = 1, n-1$). Real basis:
$$\phi_1(j) = \sqrt 2\cos(2\pi j/n),\qquad \phi_2(j) = \sqrt 2\sin(2\pi j/n).$$

$D_n$ acts as dihedral subgroup of $O(2)$: translation by $m$ = rotation by $2\pi m/n$, reflection $j \to -j$ = $(\phi_1, \phi_2) \mapsto (\phi_1, -\phi_2)$.

**Quartic integrals (exact for $n \geq 5$, using $\sum_{j=0}^{n-1}\cos^{2k}(2\pi j/n) = n \binom{2k}{k}/4^k$):**
- $I_4 = \langle \phi_1^4 \rangle = \langle \phi_2^4 \rangle = 3/2$.
- $K = \langle \phi_1^2 \phi_2^2 \rangle = \langle \sin^2(4\pi j/n) \rangle = 1/2$.
- $J = \langle \phi_1^3 \phi_2 \rangle = 0$.

**Reduced Lyapunov:**
$$F(a, b) = \tfrac{\mu}{2}(a^2 + b^2) + \Lambda\!\left[\tfrac{3}{2}(a^4 + b^4) + 3 a^2 b^2\right] = \tfrac{\mu}{2}(a^2+b^2) + \tfrac{3\Lambda}{2}(a^2+b^2)^2.$$

**Ratio $A_2/A_1 = 6K/I_4 = 2$** — the $O(2)$-invariant case. Reduced $F$ is purely radial.

**Critical set.** 1-dim circle $r^2 = a^2 + b^2 = -\mu/(6\Lambda)$. Energy $F_{\min} = -\mu^2/(24\Lambda)$.

**Hessian at any circle point** (e.g., $(R, 0)$): eigenvalues $\{-2\mu, 0\}$ = $\{$radial stable, angular Goldstone$\}$.

**$D_n$ breaks $O(2)$** at sextic or higher order via $\cos(n\theta)$ anisotropy; leading-order (quartic) is genuinely $O(2)$-invariant. At finite $n$, the circle is broken into $2n$ discrete standing-wave orbits, but all $2n$ are $D_n$-equivalent.

**$\mathcal{M}_1(C_n) \cong $ point** (after $D_n$ quotient), orbit size $n$, continuous-moduli dimension 1 at quartic order.

> **$C_n$ First-Pitchfork Theorem (Round 4, Cat A).** On cycle $C_n$ ($n \geq 5$) at $c = 1/2$, first Fiedler pitchfork gives a 1-parameter circle of degenerate quartic-level minima (radius $R = \sqrt{-\mu/(6\Lambda)}$). $|\mathcal{M}_1(C_n)| = 1$ with orbit size $n$.

**Category: Cat A** — exact discrete integrals via trig identities.

### 3.6.2 2D torus $T^2 = C_L \times C_L$

Fiedler eigenvalue $\lambda_2 = 4\sin^2(\pi/L)$ is **4-fold degenerate** from $(k_1, k_2) \in \{(\pm 1, 0), (0, \pm 1)\}$.

Real basis $\{\phi_X^c, \phi_X^s, \phi_Y^c, \phi_Y^s\}$ with $\phi_X^c(i, j) = \sqrt 2\cos(2\pi i/L)$, etc.

$\mathrm{Aut}(T^2) = D_4 \ltimes (\mathbb Z_L)^2$: X/Y translations rotate each block separately; $D_4$ swaps blocks.

**Quartic integrals (exact for $L \geq 5$):**
- 4th powers (each): $3/2$.
- Within-block cross ($(\phi_X^c)^2 (\phi_X^s)^2$ etc.): $1/2$.
- Between-block cross ($(\phi_X^c)^2 (\phi_Y^c)^2$ etc.): $1$.
- All odd-power monomials: $0$.

With $r_1^2 := a^2 + b^2$ (X-amplitude), $r_2^2 := c'^2 + d^2$ (Y-amplitude):
$$\int v^4 = \tfrac{3}{2}(r_1^2 + r_2^2)^2 + 3 r_1^2 r_2^2.$$

**Reduced Lyapunov:**
$$F(r_1, r_2) = \tfrac{\mu}{2}(r_1^2+r_2^2) + \Lambda\!\left[\tfrac{3}{2}(r_1^2+r_2^2)^2 + 3 r_1^2 r_2^2\right].$$

Within each block: $O(2)$-invariant (inherited from 1D-cycle factor). Between blocks: $+3 r_1^2 r_2^2$ is the isotropy-breaking cross term.

**Critical points:**
- **Pure-X** $(R, 0)$: $R^2 = -\mu/(6\Lambda)$, $F_X = -\mu^2/(24\Lambda)$. Hessian spectrum $\{-2\mu, 0, -\mu, -\mu\}$: minimum modulo 1 Goldstone (X-translation).
- **Pure-Y** $(0, R)$: by symmetry, $F_Y = F_X$, same structure (Goldstone in Y-translation).
- **Diagonal** $(s, s)$: $s^2 = -\mu/(18\Lambda)$, $F_\Delta = -\mu^2/(36\Lambda)$. Hessian in $(a, c')$-block $\{36\Lambda s^2, -12\Lambda s^2\}$ plus 2 Goldstones: **Morse saddle index 1**.

**Orbit selection:** $|F_X| = |F_Y| > |F_\Delta|$, so pure-X and pure-Y orbits are selected. $D_4$ links X ↔ Y (via 90° rotation), so after quotient $|\mathcal{M}_1(T^2)| = 1$ with orbit size $2L^2$.

> **$T^2$ First-Pitchfork Theorem (Round 4, Cat A).** On 2D torus $C_L \times C_L$ ($L \geq 5$) at $c = 1/2$, first Fiedler pitchfork selects the **pure-X and pure-Y orbit class** (linked by $D_4$); the diagonal orbit is a saddle (Morse index 1). $|\mathcal{M}_1(T^2)| = 1$ with orbit size $2L^2$.

**Category: Cat A** — exact discrete integrals.

### 3.6.3 Universal ratio classification

Assembling Rounds 3 and 4:

| Graph | $\mathrm{Aut}(G)$ | Fiedler dim | $A_2/A_1$ within-block | Selected orbit | $|\mathcal{M}_1|$ | Orbit size | Goldstones |
|---|---|---|---|---|---|---|---|
| 2D square (free BC) | $D_4$ | 2 | **4** (product-structure) | Axis-aligned | 1 | 4 | 0 |
| 1D cycle $C_n$ | $D_n$ | 2 | **2** (single-translation) | Continuous circle | 1 | $n$ | 1 |
| 2D torus $T^2$ | $D_4 \ltimes (\mathbb Z_L)^2$ | 4 | **2 within, 4 inter-block** | Pure-X or pure-Y | 1 | $2L^2$ | 1 (per orbit) |

**Universal takeaway.** The ratio $A_2/A_1$ at **within-block** level encodes the type of translation symmetry:
- $A_2/A_1 = 2$ ⇔ single direction of free translation (isotropic $O(2)$ at quartic).
- $A_2/A_1 = 4$ ⇔ product-structure two-direction decomposition ($D_4$-anisotropic).

The torus combines both: within each X or Y block, ratio is $2$ (isotropic); between blocks, the effective ratio is $4$ (anisotropic). This explains why the torus result is "pure axis selected among Cartesian orbits" rather than either "fully continuous (like $C_n$)" or "discrete 4-point (like free-BC square)".

### 3.6.4 Moduli dimension is the sharp invariant, not $|\mathcal{M}_1|$

All three cases give $|\mathcal{M}_1| = 1$ (after Aut quotient), but the continuous-moduli dimension differs:
- 2D square: 0-dim (discrete 4-point orbit).
- $C_n$: 1-dim (circle modulo discrete $D_n$, exponentially small lock-in at sextic+).
- $T^2$: 1-dim (two circles glued by $D_4$; each continuous in translation direction).

**Implication for multi-formation bridge.** On graphs with positive-dimensional $\mathcal{M}_1$ (torus, cycle), the emergence kinetics of K=2 has **continuous choice of formation locations** (positions on the circle); nucleation rate sums over this continuum, giving additional factor of orbit size or circumference. On discrete-moduli graphs (square free BC), only 4 nucleation sites per orbit.

This refinement is relevant to `from_single.md` §2 Conjecture 2.1's multiplicity prefactor (does NOT change scaling $\widehat K \sim N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}}$, but modulates the $O(1)$ prefactor).

---

## §3.7. Continuous $\mathrm{Aut}$ and Morse-Bott refinement (Round 5, 2026-04-22)

Round 4 treated $C_n$ and $T^2$ at discrete finite $n$ (exact quartic). Round 5 extends to the **continuum limit** where $\mathrm{Aut}$ enlarges to a Lie group.

### 3.7.1 Continuum-limit graph family (definition)

> **Definition.** A sequence $\{G_n\}$ of finite graphs has **continuum limit** $(M, g)$ (compact Riemannian manifold) if:
> (i) vertices become equidistributed in $M$;
> (ii) Laplacian spectrum converges: $\{\lambda_k^{G_n}\} \to \{\lambda_k^{(M, g)}\}$;
> (iii) $\mathrm{Aut}(G_n) \hookrightarrow \mathrm{Iso}(M, g)$ with image dense as $n \to \infty$.

Examples: $C_n \to S^1$ with $\mathrm{Iso}(S^1) = O(2)$; $C_L \times C_L \to T^2$ with $\mathrm{Iso}(T^2) = T^2 \rtimes D_4$. 2D square (free BC) does NOT have continuum enlargement ($D_4$ remains finite).

### 3.7.2 Morse-Bott replacement

When $\mathrm{Iso}_0(M)$ is positive-dim, a critical orbit $\mathrm{Iso}_0(M) \cdot u^\ast$ is a submanifold of dim $= \dim\mathrm{Iso}_0(M) - \dim\mathrm{Stab}(u^\ast)$. Hessian has Goldstone zero-eigenvalues along orbit-tangent directions.

**Morse-Bott theory (Bott 1954):** Replace Morse index with **Morse-Bott index** = dim of negative-Hessian subspace on orbit-normal bundle.

> **Prop 1.3a-Bott (Round 5, Cat A).** At $u_{\mathrm{uniform}}$ (fixed by full $\mathrm{Iso}(M)$): orbit dim 0, Morse-Bott index = $N_{\mathrm{unst}}^{\mathrm{bd}}$ (standard Prop 1.3a). At bifurcated orbit on $C_n \to S^1$: orbit dim 1 (translation Goldstone), Morse-Bott index 0. At pure-X orbit on $T^2$: orbit dim 1 (Y-translation fixes X-pattern? **No** — Y-translation leaves pure-X invariant only if the pattern is Y-constant, which it is), so $\dim\mathrm{Stab} = 1$ (Y-translations), $\dim N = \dim T^2 - \dim\mathrm{Stab} = 1$. One Goldstone along orbit. Matches Round 4 Hessian spectrum $\{-2\mu, 0, -\mu, -\mu\}$.

### 3.7.3 $D_n$-lock-in scaling on $C_n$

At first pitchfork on $C_n$, the reduced Lyapunov at full order is
$$F(r, \theta) = \tfrac{\mu}{2}r^2 + \tfrac{3\Lambda}{2}r^4 + \Lambda_n r^{p(n)}\cos(p(n)\theta) + O(r^{p(n)+2}),$$
with
$$p(n) = \begin{cases} n & n \text{ even} \\ 2n & n \text{ odd at } c = 1/2 \end{cases}$$
(parity at $c = 1/2$ eliminates odd-$n$ lowest invariants).

**Lock-in scaling:** At critical minimum $r^\ast \sim |\mu|^{1/2}$, lock-in energy
$$\Delta F_{\mathrm{lock-in}} \sim |\Lambda_n| \cdot |\mu|^{p(n)/2}.$$

Goldstone mass at lock-in site: $m_G^2 \sim |\mu|^{p(n)/2}$.

> **$C_n$ Lock-In Theorem (Round 5, Cat A).** For $C_n$ at $c = 1/2$, the $D_n$-anisotropy appears at order $r^{p(n)}$ with $p(n)$ as above. The Goldstone acquires a small mass $\sim |\mu|^{p(n)/4}$ at finite $n$, vanishing in $n \to \infty$ continuum limit. Lock-in energy $\sim |\mu|^{p(n)/2}$, exponentially small for large $n$ fixed $|\mu|$.

**Category: Cat A structural.** $D_n$-invariant polynomial classification ($\{r^{2k}, r^{n+2k}\cos(n\theta)\}$ generators) + parity argument at $c = 1/2$. Explicit $\Lambda_n$ coefficient requires Lyapunov-Schmidt reduction (open).

### 3.7.4 $\mathcal{M}_1$ topology: moduli-dim + orbit-volume invariant

| Graph | $\dim_{\mathrm{moduli}}$ | $\mathrm{Vol}(N_1)$ (orbit volume, continuum) |
|---|---|---|
| 2D square (free BC) | 0 | 4 (counting measure) |
| $C_n \to S^1$ | 0 | $2\pi$ (circumference; $n$ in lattice units) |
| $T^2$ | 0 | $2 \cdot (2\pi)^2$ (two X/Y circles) |

$|\mathcal{M}_1| = 1$ after $\mathrm{Iso}(M)$-quotient is not the sharp invariant; **$\mathrm{Vol}(N_1)$** distinguishes the three cases quantitatively.

### 3.7.5 Conjecture 2.1-Bott refinement

Round 4 noted continuous-moduli modifies the $O(1)$ prefactor in Conjecture 2.1. Round 5 quantifies:

> **Conjecture 2.1-Bott (Round 5).** $\widehat K(G_n; \beta) = 1 + \mathrm{Vol}(\mathrm{Iso}_0(M)/\mathrm{Stab}) \cdot N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}(M)} + O(1)$.

On torus with $\mathrm{Vol} = L$ (X-translation orbit), $\widehat K \approx 1 + L \cdot 2 = 1 + 2L$ at first pitchfork ($N_{\mathrm{unst}} = 4$). **Extensive in $L$**, in contrast to intensive $\widehat K = 3$ on 2D square.

**Implication:** Numerical validation of $\widehat K$ on torus should measure $\widehat K/L$ (intensive per nucleation position), not raw $\widehat K$.

**Category: Cat A conjecture** — scaling inherits from moduli-dimension argument; numerical verification open.

---

## §4. Higher $\beta$ structure — mode cascades

At $\beta = \beta_{\mathrm{crit}}^{(k)}$ for $k \geq 3$, additional Fiedler-like modes activate. Each new active irrep contributes independently to $\mathcal{M}_1$.

**Counting on 2D grid:** Laplacian eigenspaces on $L\times L$ grid carry $D_4$ irreps:
- 1D trivial ($\phi_{0,0} = \mathbf{1}$, $\lambda_1 = 0$).
- Sign ($\phi_{L-1,L-1}$, highest mode).
- $(1,1)$ reflection irreps (diagonal modes).
- 2D standard ($\phi_{p,q}$ with $p \neq q$).
- 1D trivial-reflected (diagonal symmetric).

For each new active mode, an orbit of minimizers is added to $\mathcal{M}_1$. Total:
$$|\mathcal{M}_1(\beta)| = \sum_{k \geq 2 : \beta_{\mathrm{crit}}^{(k)} < \beta} \mathbf{1}[\text{orbit}_k \text{ is a local min}].$$

**Relation to `cardinality_open.md` §8.2 (pitchfork lower bound $c_0 \geq 1 + N_{\mathrm{unst}}^{\mathrm{orbit}}$).** The $\mathrm{Aut}(G)$-orbit enumeration gives the precise meaning of $N_{\mathrm{unst}}^{\mathrm{orbit}}$: it is the number of distinct $\mathrm{Aut}(G)$-irrep components of the unstable Laplacian eigenspaces up to $\beta$.

### 4.1 Connection to $\widehat{K}$ formula

`working/MF/from_single.md` §2 Conjecture 2.1: $\widehat{K} = 1 + N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}(G)} + O(1)$.

$\mathrm{Aut}(G)$ plays a **multiplicity role**, not a scaling role. On 2D grid: $N_{\mathrm{unst}}$ (total unstable mode count) is the dimensional quantity setting $\widehat{K}$; $N_{\mathrm{unst}}^{\mathrm{orbit}} \approx N_{\mathrm{unst}}/|D_4| \approx N_{\mathrm{unst}}/8$ is the orbit count. Thus:
$$|\mathcal{M}_1(\beta)| \approx N_{\mathrm{unst}}(\beta)/|\mathrm{Aut}(G)|$$
while $\widehat{K}(\beta) \approx \sqrt{N_{\mathrm{unst}}(\beta)}$. These are two different statistical quantifications of the landscape.

---

## §5. Role of $\mathrm{Aut}(G)$ in other open problems

### 5.1 F-1 dissolution

`working/E/F1_dissolution.md` §7 Round 18: F-1 "K=2 vacuity" dissolved via derived view. At $N_{\mathrm{unst}} \geq 1$, K=2 emerges naturally. $\mathrm{Aut}(G)$ here plays no direct role — the emergence is generic, regardless of symmetry. However, the **location** of the K=2 split is parameterized by orbit choice.

### 5.2 M-1 two-timescale

`working/E/M1_dissolution.md` §8: two-timescale emergence-coarsening. $\mathrm{Aut}(G)$ affects Kramers prefactor: if transition states come in orbit of multiplicity $m$, the effective rate is $m \cdot \tau_0^{-1} \exp(-\Delta\mathcal{F}/T)$. Not critical for qualitative picture.

### 5.3 MO-1 Morse theory

`working/E/MO1_dissolution.md` §9: single-Σ_m Morse applies. $\mathrm{Aut}(G)$-equivariant Morse theory (Wasserman 1969, *Equivariant differential topology*) provides the refined framework: critical orbit counting + equivariant Euler characteristic. This enhances Prop 1.3a beyond plain Morse.

### 5.4 Isolation of grid symmetry effects

On 2D square grid: $D_4$ is small (8 elements). On larger grids (torus, 3D lattice, SBM with block symmetry), $\mathrm{Aut}(G)$ can be much larger (torus: $D_4 \times T^2$ infinite). The "moduli space size" $|\mathcal{M}_1|$ is much smaller than the raw minimizer count at high-symmetry graphs.

---

## §6. Scope limits of this file

**What this file covers (first-step):**
- Definition of $\mathcal{M}_1$.
- Equivariant bifurcation framework (Crandall-Rabinowitz with $D_4$).
- Two orbit types at first pitchfork (axis-aligned vs diagonal) on 2D grid.
- Relation to `cardinality_open.md` §8 pitchfork lower bound.

**What this file does NOT cover (post-Stage-1):**
- ~~Computation of cubic coefficients $A_{\mathrm{axis}}, A_{\mathrm{diag}}$ for specific grid parameters~~ — **DONE** in Round 3 (§3.3).
- ~~1D cycle $C_n$ / 2D torus $T^2$ $\Phi_4$ analysis~~ — **DONE** in Round 4 (§3.6).
- Multi-formation moduli space $\mathcal{M}_K$ for $K \geq 2$ — requires $\mathrm{Aut}(G)$-action on K-formation configurations.
- Equivariant Morse homology / equivariant cohomology of $\Sigma_m$ under $\mathrm{Aut}(G)$.
- Other non-$D_4$ graph classes (SBM block symmetry, barbell reflection, complete graph $K_n$, 3D torus) — case-by-case analysis needed.
- Sextic-order lock-in of cycle / torus Goldstone direction — exponentially-small $D_n$-anisotropy at sextic+ orders.

---

## §7. Category self-classification

| Claim | Category |
|---|---|
| §1-2 Definition + $\mathrm{Aut}(G)$ action on Σ_m | **Cat A** (elementary) |
| §3.1 Equivariant Crandall-Rabinowitz on $V_2$ | **Cat A** — reuses Sattinger 1979 + canonical T-Birth-Parametric (D4) |
| §3.1 Axis vs diagonal orbit types | **Cat A** — $D_4$ isotropy analysis |
| §3.1 Which orbit is selected (cubic coefficient) | **Cat A** (Round 3, §3.3 explicit computation: axis selected, $A_2/A_1 = 4$ on 2D grid) |
| §3.6.1 $C_n$ first-pitchfork radial reduction | **Cat A** (Round 4, exact discrete integrals) |
| §3.6.2 $T^2$ first-pitchfork orbit selection | **Cat A** (Round 4, pure-X/Y minima, diagonal saddle) |
| §3.6.3 Universal $A_2/A_1$ classification (2 vs 4) | **Cat A** (Round 4, structural) |
| §3.7.2 Prop 1.3a-Bott (continuous-Aut Morse-Bott refinement) | **Cat A** (Round 5, direct Bott 1954 application) |
| §3.7.3 $C_n$ Lock-In Theorem ($D_n$-anisotropy at order $r^{p(n)}$) | **Cat A structural** (Round 5, $D_n$-invariant polynomial classification) |
| §3.7.4 $\mathcal{M}_1$ topology invariant (moduli-dim + orbit-volume) | **Cat A** (Round 5, structural) |
| §3.7.5 Conjecture 2.1-Bott ($\widehat K$ extensive on continuum-Aut) | **Cat A conjecture** (Round 5, numerical verification open) |
| §4 mode cascade $|\mathcal{M}_1(\beta)|$ | **Sketched Cat B** — each new irrep contributes but specifics config-dependent |
| §5 integration with other OPs | **Cat A commitment** |

---

## §8. Canonical merge (pending Stage 6)

- **§13 proposed Cat A entry** (optional): "equivariant Crandall-Rabinowitz applies to Prop 1.3a's bifurcations; pitchfork orbits are $\mathrm{Aut}(G)$-irrep-structured, not generic 2-point."
- **§14 CN19 proposal (optional):** "$\mathrm{Aut}(G)$-orbit quotient $\mathcal{M}_1$ is the relevant landscape cardinality; raw minimizer counts include redundant symmetry-equivalent copies."
- **G-D status update:** post-Stage-1 scope confirmed, first-step structural framework in place.

---

## §9. File status

- **Definition + first-step analysis:** committed.
- **Cubic coefficient / selection of axis-vs-diagonal (2D square):** committed (Round 3).
- **$\Phi_4$ on $C_n$ and $T^2$:** committed (Round 4).
- **Universal $A_2/A_1 \in \{2, 4\}$ classification:** committed (Round 4).
- **Multi-formation $\mathcal{M}_K$:** NOT in scope; post-Stage-1.
- **Other graph classes (SBM, barbell, $K_n$, 3D torus):** open (Round 5+ or case-by-case).
- **Canonical merge:** expanded (~25-35 lines) if all Round 3+4 Cat A included.

**End of symmetry_moduli.md.**
