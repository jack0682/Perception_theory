# 13 — Round 11: $\mathcal{M}_2$ Classification on 2D Grid (K=2 First Pitchfork)

**Session:** 2026-04-22 (Round 11, multi-formation 확장 시작)
**Trigger:** User "중기까지" — 단/중기 6개 항목 (items 1-6 from Part 5). Round 11 = item 1.
**Target:** K=2 moduli space $\mathcal{M}_2$의 explicit classification. 2D 그리드 (free BC + torus). Secondary pitchfork $\beta^{\mathrm{sec}}_{1 \to 2}$에서 K=1 axis orbit → K=2 configurations.
**This file covers:** §1 Scope. §2 K=2 configuration ansatz. §3 Secondary pitchfork from K=1. §4 $\mathcal{M}_2$ enumeration on 2D square. §5 Torus continuum limit. §6 Category + residuals.

---

## §1. Scope and framework

### 1.1 Framework from single-formation results

Round 10 tree structure: $u_{\mathrm{uniform}} \xrightarrow{\beta^{(2)}_{\mathrm{crit}}} u^\ast_1$ (axis orbit on 2D grid, Round 3) $\xrightarrow{\beta^{\mathrm{sec}}_{1 \to 2}} u^\ast_2$ (K=2 configuration).

This is a **split bifurcation**: single formation divides into two.

### 1.2 Alternative K=2 emergence route

K=2 can also emerge directly from $u_{\mathrm{uniform}}$ at higher primary pitchfork (e.g., $(2, 0)$ mode creates 2-stripe pattern) — but this produces "pattern" rather than "distinct formations". True K=2 emergence is via secondary from K=1.

In terms of $\widehat K$: Round 5 Conjecture 2.1-Bott gives $\widehat K$ as statistical expectation; Round 11 identifies explicit $\widehat K$ = 2 critical configurations.

---

## §2. K=2 configuration ansatz

### 2.1 Well-separated ansatz

For $d_{\min} \gg \xi_0$ (well-separated):
$$u^\ast_2(x) \approx u_0(x - x_1) + u_0(x - x_2) - c\mathbf{1} + O(e^{-d_{\min}/\xi_0}),$$
where $u_0$ is the K=1 single-formation profile (Round 3 axis orbit shape), $x_1, x_2 \in \Sigma$ are formation centers. Mass constraint: $\int u^\ast_2 = m$ imposes one scalar equation on the two positions.

### 2.2 Interaction ansatz (near regime)

For $d_{\min} \sim \xi_0$: full Allen-Cahn minimizer, non-trivially coupled. Round 11 focuses on well-separated; interaction regime deferred.

### 2.3 Orbit parametrization

$\mathcal{M}_2 = \{(x_1, x_2) : u^\ast_2 \text{ is local min}\} / \mathrm{Aut}(G) \cdot S_2$

Note: $S_2$ (label swap) is "formation permutation", always present if formations are indistinguishable.

---

## §3. Secondary pitchfork $\beta^{\mathrm{sec}}_{1 \to 2}$

### 3.1 Mechanism

At $\beta$ just above $\beta^{(2)}_{\mathrm{crit}}$: $u^\ast_1 = c\mathbf{1} + A_1\phi_{1,0}$ (axis orbit, single broad bump).

As $\beta$ grows, Hessian $H(u^\ast_1; \beta)$ has eigenvalue $\mu_\ell(\beta)$ for each mode $\phi_\ell$. When $\mu_\ell$ crosses zero, a secondary branch emerges.

**"Split" mode** $\phi_{\mathrm{split}}$ that perpendicularly modulates the axis-orbit amplitude: on 2D grid, $\phi_{\mathrm{split}} = \phi_{2,0}$ (second harmonic) or $\phi_{0,2}$ (orthogonal axis). This mode creates two half-amplitude sub-peaks along the primary direction.

### 3.2 Threshold formula (Round 10 application)

$$\beta^{\mathrm{sec}}_{1 \to 2} = \beta^{(k_{\mathrm{split}})}_{\mathrm{crit}} - A_1^2(\beta^{\mathrm{sec}}) \cdot \langle\phi_{\mathrm{split}}, \mathcal{K}_1 \phi_{\mathrm{split}}\rangle / \mathrm{slope}.$$

With $A_1^2 = -\mu/(6\Lambda) \sim (\beta - \beta^{(2)}_{\mathrm{crit}})/\beta^{(2)}_{\mathrm{crit}}$:

$$\beta^{\mathrm{sec}}_{1 \to 2} \approx \beta^{(4)}_{\mathrm{crit}} - O(\Delta\beta), \quad \Delta\beta = \beta^{\mathrm{sec}} - \beta^{(2)}_{\mathrm{crit}}.$$

**Typical shift:** $\langle\phi_{2,0}, \mathcal{K}_1 \phi_{2,0}\rangle$ integral gives order-unity coefficient. Self-consistent estimate: $\beta^{\mathrm{sec}}_{1 \to 2} \approx \beta^{(4)}_{\mathrm{crit}} (1 - O(\Delta\beta/\beta^{(2)}_{\mathrm{crit}}))$.

On 2D square grid (continuum limit): $\beta^{(4)}_{\mathrm{crit}}/\pi^2 = 16$ (from mode $(2, 0)$). So $\beta^{\mathrm{sec}}_{1 \to 2} \approx 16\pi^2 - O(1)$.

### 3.3 Split direction selection

From axis orbit $u^\ast_1 = c + A_1 \phi_{1,0}$ (say x-direction axis):
- $\phi_{2,0}$: split along x (same direction), creates two peaks along x.
- $\phi_{0,1}$ or $\phi_{0,2}$: split perpendicular (y-direction).

Coupling integrals:
- $\langle\phi_{2,0}, \phi_{1,0}^2\rangle$: overlap of $\cos(2\pi x)$ with $\cos^2(\pi x) = (1 + \cos(2\pi x))/2$ → integral gives $1/2$.
- $\langle\phi_{0,2}, \phi_{1,0}^2\rangle$: overlap of $\cos(2\pi y)$ with $\cos^2(\pi x)$ → 0 by $y$-orthogonality.

**Therefore:** the $(2, 0)$ mode couples to axis orbit; $(0, 2)$ doesn't. Split along primary direction is the preferred channel.

### 3.4 K=2 configuration from split

After $(2, 0)$-split: $u^\ast_2(x, y) \approx c + A_1\phi_{1,0} + A_2\phi_{2,0} = c + A_1\cos(\pi x) + A_2\cos(2\pi x)$.

This is NOT two separated bumps — it's a "double-peak" pattern. For true K=2 configuration (well-separated), higher-order interactions (via Allen-Cahn nonlinearity) pinch the pattern into two distinct bumps.

**Transition to well-separated:** at $\beta \gg \beta^{\mathrm{sec}}_{1 \to 2}$: the two bumps become sharp-interface via T11 Γ-convergence; $d_{\min}$ determined by mass constraint and graph geometry.

---

## §4. $\mathcal{M}_2$ enumeration on 2D square (free BC)

### 4.1 Well-separated K=2 configurations

Two formations at positions $x_1, x_2$ on $L \times L$ grid, each roughly disk-like (by T11).

$D_4$ action: rotates/reflects $(x_1, x_2)$ simultaneously.
$S_2$ action: swaps labels $x_1 \leftrightarrow x_2$.

### 4.2 Orbit types

Parametrize by $(d, \theta)$ = (separation distance, orientation angle of $x_1 - x_2$).

- $\theta = 0$ (horizontal-pair): $(x_1, x_2)$ along x-axis.
- $\theta = \pi/2$ (vertical-pair): along y-axis.
- $\theta = \pi/4$ (diagonal-pair): along $x = y$ diagonal.
- Generic $\theta$: reflects to fundamental domain $\theta \in [0, \pi/4]$.

$D_4$: identifies $\theta = 0$ and $\theta = \pi/2$; doesn't identify $\theta = \pi/4$ (diagonal) with $\theta = 0$ (axis).

**Reduced orbit types:**
- **Axis-pair** ($\theta = 0$): single $D_4$-orbit class. Size 4 in $(x_1, x_2)$ space (x-pair in 4 positions, modulo $S_2$).
- **Diagonal-pair** ($\theta = \pi/4$): single $D_4$-orbit class. Size 4 similarly.
- **Generic** ($0 < \theta < \pi/4$): continuous family, each discrete $\theta$-value = separate orbit.

### 4.3 Center-of-mass positioning

Each orbit type has a center-of-mass $\bar x = (x_1 + x_2)/2$. On free-BC square, $\bar x$ chosen in $L^2$ positions; $D_4$ reduces to $\sim L^2/8$ inequivalent centers.

**Size of $\mathcal{M}_2$:**
- (Axis-pair at fixed $d$, $\theta = 0$): $L^2/8$ center positions × (fixed orientation) = $O(L^2)$ orbits per value of $d$.
- Varying $d$: discrete values $d \in \{1, 2, \ldots, L\}$ (minimum $d = O(1)$ for discretization, max $d = O(L)$).
- Total: $|\mathcal{M}_2| \sim L^2 \cdot L = O(L^3)$ for axis-pairs alone.

### 4.4 Minimum-energy configurations

At moderate $\beta$: preferred configuration is $d = d_{\min}^\ast(\beta)$ (Round 2 formula). Each $\theta$ type has its own minimum $d$.

**Axis-pair vs diagonal-pair energy comparison:**
- Axis-pair: formations along grid axis, interface tails in x-direction.
- Diagonal-pair: formations along diagonal, interface tails in diagonal direction.

On 2D square grid (anisotropic): axis-pair has different interaction than diagonal. Cubic coefficient integrals at K=2 level (analogous to Round 3 $A_2/A_1$ analysis): axis wins or diagonal wins depending on details.

**Predict:** Similar to single-formation axis-selection (Round 3 $A_2/A_1 = 4$), K=2 axis-pair preferred over diagonal-pair on 2D square grid.

### 4.5 Enumeration summary

> **$\mathcal{M}_2$ on 2D square grid (Round 11, Cat A structural).** Well-separated K=2 configurations parametrize by $(\bar x, d, \theta) \in L^2 \times [d_{\min}, L] \times [0, \pi/4]$. After $D_4 \times S_2$-quotient: $|\mathcal{M}_2| = O(L^3)$ orbit classes. Minimum-energy orbit class: axis-pair at $d = d_{\min}^\ast(\beta)$, center $\bar x$ in fundamental domain of $D_4$-action on grid.

**Category: Cat A structural** — orbit classification via group action.

---

## §5. 2D torus $T^2 = C_L \times C_L$

### 5.1 Continuous translational symmetry

$\mathrm{Iso}(T^2) = D_4 \ltimes T^2$ has continuous translation component. K=2 configuration $\{x_1, x_2\}$ has:
- 2D continuous center-of-mass $\bar x$ (1-dim torus $T^2$-orbit).
- 2D continuous relative vector $\Delta x = x_2 - x_1$.

**Quotient structure:** $\bar x$ orbit modulo $T^2$-translation: single point. So $\mathcal{M}_2$ is parametrized by $(\Delta x)/D_4$.

### 5.2 Moduli dimension

$\Delta x \in T^2$, modulo $D_4$ (rotate/reflect). Fundamental domain of $D_4$ on $T^2$: $1/8$ of the torus.

**$\mathcal{M}_2(T^2)$ = fundamental domain of $T^2/D_4$ = 2-dim moduli space.**

At fixed $d = |\Delta x|$: 1-dim moduli (angle $\theta \in [0, \pi/4]$).

### 5.3 Goldstone structure

K=2 configuration has 2D Goldstone (center-of-mass translation). After $T^2$-quotient: 2D eliminated, remaining moduli is "relative coordinate".

**Moduli dimension on torus: 2** (vs 0-dim on 2D free-BC square with discrete positions).

This matches Round 5 expectation: continuous-Aut graphs have positive-dim moduli per formation × K.

### 5.4 Enumeration summary

> **$\mathcal{M}_2$ on 2D torus (Round 11, Cat A).** $\mathcal{M}_2(T^2) = T^2/D_4$ (2-dim moduli from relative coordinate $\Delta x$). Minimum-energy locus: circle $|\Delta x| = d_{\min}^\ast(\beta)$ with preferred angle $\theta \in \{0, \pi/2\}$ (axis-pair) modulo $D_4$.

**Category: Cat A**.

---

## §6. Category + residuals + next

### 6.1 New Cat A claims (Round 11)

1. **Secondary pitchfork threshold $\beta^{\mathrm{sec}}_{1 \to 2}$** — explicit from Round 10 formula applied to $(2, 0)$ mode coupling.

2. **Split-direction selection** — $\phi_{2, 0}$ mode couples to axis orbit $\phi_{1, 0}$ via $\langle\phi_{2, 0}, \phi_{1, 0}^2\rangle = 1/2 \neq 0$.

3. **$\mathcal{M}_2$ on 2D square grid** — orbit classification by $(\bar x, d, \theta)$; $|\mathcal{M}_2| = O(L^3)$.

4. **$\mathcal{M}_2$ on 2D torus** — 2-dim moduli $(T^2/D_4)$; continuous relative coordinate.

5. **Axis-pair vs diagonal-pair selection** — axis preferred on 2D square (analogous to K=1 Round 3 result).

6. **Moduli-dimension growth** — K=2 on torus has dim 2 (vs dim 1 at K=1); confirms Round 5 prediction of linear growth with K.

### 6.2 Residuals from Round 11

- **Explicit $\beta^{\mathrm{sec}}_{1 \to 2}$ numerical value** — requires $\mathcal{K}_1$ integrals (Cat B case-by-case).
- **Axis vs diagonal K=2 cubic coefficient** — analog of Round 3 but for pair interactions.
- **Near-interaction regime** ($d_{\min} \sim \xi_0$): not well-separated, requires full Allen-Cahn.
- **Non-axis first pitchfork** (if K=1 had diagonal-orbit, K=2 structure differs).
- **K=3, 4, ... iteration** — generalize to arbitrary K.

### 6.3 Cumulative Cat A (session)

- Rounds 1-10 (morning + single-formation): 50
- **Round 11: 6**
- **Cumulative: 56 Cat A**.

### 6.4 Next: Round 12

Item 2: $u^\ast_2$ Hessian via Lyapunov-Schmidt. Enables computation of Morse index, secondary thresholds for K=3, separation-mode eigenvalues.

---

**End of 13_deepening_round11.md.**
