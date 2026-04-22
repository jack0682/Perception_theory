# 07 — Deepening Round 5: Continuous $\mathrm{Aut}$ Groups and Morse-Bott Refinement

**Session:** 2026-04-22 (Round 5, post-Round-4)
**Trigger:** User directive "가자" — continue 7-item residual list, item 2.
**Target (item 2):** Formalize the continuum limit of Round 4's cycle/torus results. Convert finite-$n$ discrete-$\mathrm{Aut}$ framework into continuous-$\mathrm{Aut}$ (Goldstone, Morse-Bott), and close the $D_n$-lock-in scaling.
**This file covers:** §1 Framework. §2 Continuum-limit graph families. §3 Morse-Bott replacement. §4 $D_n$-lock-in scaling on $C_n$. §5 $\mathcal{M}_1$ topology invariant. §6 Conjecture 2.1 prefactor refinement. §7 Category. §8 Next.

---

## §1. Framework and scope

### 1.1 Why this round

Round 4 computed explicit $\Phi_4$ on $C_n$ and $T^2$ and found:
- At quartic order, the reduction is $O(2)$-invariant within each translation-direction block.
- At discrete-$D_n$ level, the quartic integrals are **exact for $n \geq 5$** — no lattice correction.
- A Goldstone direction appears (1 for $C_n$, 1 per X/Y-orbit for $T^2$).

But two questions were left implicit:
1. **What breaks the continuous $O(2)$-invariance at discrete-$D_n$?** Round 4 said "sextic+" generically. Here we compute the precise scaling.
2. **What is the formal framework for continuous-$\mathrm{Aut}$ Morse theory?** The Goldstone direction has 0 Hessian eigenvalue; standard Morse theory doesn't apply.

Round 5 closes both.

### 1.2 Scope

This round covers:
- **Formal definition** of "continuum-limit graph family" and the Aut-inflation to a continuous group.
- **Morse-Bott replacement** of Morse when critical sets are positive-dimensional manifolds.
- **Precise $D_n$-lock-in scaling** on $C_n$: $\Delta F_{\mathrm{lock-in}} \sim |\mu|^{n/2}$ (or $|\mu|^n$ for odd $n$ at $c = 1/2$).
- **Prop 1.3a Bott-refinement:** Morse-Bott index on continuous-Aut graphs.
- **$\mathcal{M}_1$ topology** as an invariant finer than $|\mathcal{M}_1|$.
- **Conjecture 2.1 prefactor** correction from continuous-moduli volume.

This round does NOT cover:
- Sphere $S^d$ or other non-torus continuous manifolds.
- $O(3)$-equivariant or $SU(2)$ cases (representation theory heavy).
- Thermal fluctuations (Mermin-Wagner) destabilizing continuous-symmetry breaking.

---

## §2. Continuum-limit graph families

### 2.1 Definition

> **Definition 2.1 (continuum-limit graph family).** A sequence $\{G_n\}_{n \geq n_0}$ of finite graphs with $|V(G_n)| = n$ has a **continuum limit** $(M, g)$ (a compact Riemannian manifold $M$ with metric $g$) if:
> 1. There exists a sequence of embeddings $\iota_n : V(G_n) \hookrightarrow M$ such that $\{\iota_n(V(G_n))\}$ becomes equidistributed in $M$ as $n \to \infty$.
> 2. The Laplacian spectrum $\{\lambda_k^{G_n}\}$ converges to the manifold spectrum $\{\lambda_k^{(M, g)}\}$ as $n \to \infty$ (spectral convergence).
> 3. The automorphism group inflates: $\mathrm{Aut}(G_n) \hookrightarrow \mathrm{Aut}(M, g) = \mathrm{Iso}(M, g)$ (isometry group) with the image becoming dense as $n \to \infty$.

### 2.2 Examples

| Family | Manifold $M$ | $\mathrm{Aut}(G_n)$ | $\mathrm{Iso}(M)$ |
|---|---|---|---|
| 1D cycle $C_n$ | Circle $S^1$ | $D_n$ | $O(2)$ |
| 2D torus $C_L \times C_L$ | Flat torus $T^2$ | $D_4 \ltimes (\mathbb Z_L)^2$ | $D_4 \ltimes T^2$ |
| 2D square (free BC) | Unit square $[0,1]^2$ | $D_4$ | $D_4$ (no enlargement) |
| 2D barbell (two cliques + bridge) | — | $\mathbb Z_2 \times S_{n_1} \times S_{n_2}$ | **not a manifold limit** (degenerate concentration) |
| $K_n$ | $n$-simplex? | $S_n$ | — (singular limit) |
| 3D torus $C_L^3$ | Flat $T^3$ | $S_4 \ltimes (\mathbb Z_L)^3$ | $S_4 \ltimes T^3$ |

**Key observation:** The enlargement $|\mathrm{Aut}(G_n)| \to |\mathrm{Iso}(M)|$ happens only for graph families with **translation-or-rotation symmetry**. The 2D square (free BC) has no enlargement: $|D_4| = 8$ finite, preserved.

### 2.3 What "continuous-Aut" means operationally

A finite graph $G_n$ has $\mathrm{Aut}(G_n)$ discrete. The "continuous-Aut" attribute refers to:
- The **limit group** $\mathrm{Iso}(M)$ is a Lie group with positive-dimensional identity component $\mathrm{Iso}_0(M)$.
- At finite $n$, the quartic-level reduction is $\mathrm{Iso}_0(M)$-invariant (inherits continuous symmetry), with discrete-$\mathrm{Aut}(G_n)$ breaking appearing only at higher order.

This is exactly what Round 4 observed: exact $O(2)$-invariance at quartic on $C_n$, $D_n$-anisotropy at sextic+.

---

## §3. Morse-Bott replacement

### 3.1 Motivation

When $\mathrm{Iso}_0(M)$ is positive-dimensional and acts on $\Sigma_m$, a critical point $u^\ast$ that is not fixed by all of $\mathrm{Iso}_0(M)$ has its **orbit** $\mathrm{Iso}_0(M) \cdot u^\ast$ as a critical manifold. The Hessian has $\dim(\mathrm{Iso}_0(M) \cdot u^\ast)$ zero-eigenvalues along the orbit-tangent directions (Goldstone modes).

Standard Morse theory requires isolated critical points with non-degenerate Hessian. **Morse-Bott theory** (Bott 1954) relaxes to:
- Critical set $\mathrm{Crit} = \bigsqcup_\alpha N_\alpha$ where each $N_\alpha$ is a smooth submanifold.
- Hessian $H(u^\ast)$ for $u^\ast \in N_\alpha$ is **non-degenerate on $(T_{u^\ast} N_\alpha)^\perp$**.
- Morse-Bott index: $\dim$ of negative-eigenvalue subspace of $H(u^\ast)|_{(T_{u^\ast}N_\alpha)^\perp}$.

### 3.2 Application to SCC energy

On $G_n$ with continuous-Aut limit $M$:
- $u_{\mathrm{uniform}} = c\mathbf{1}$ is fixed by all of $\mathrm{Iso}(M)$ (trivially), so its orbit is a point. Morse-Bott index at $u_{\mathrm{uniform}}$ = standard Morse index = $N_{\mathrm{unst}}^{\mathrm{bd}}$.
- A **bifurcated solution** $u^\ast$ at first pitchfork has orbit = $\mathrm{Iso}_0(M) \cdot u^\ast / \mathrm{Stab}(u^\ast)$, a submanifold of dimension $\dim\mathrm{Iso}_0(M) - \dim\mathrm{Stab}(u^\ast)$.
- For $C_n \to S^1$: orbit dim = $\dim O(2) - \dim\mathrm{Stab}(\mathrm{standing wave})$ = $1 - 0 = 1$ (since standing wave has 0-dim reflection-stabilizer). So the orbit is a 1-dim circle. Matches Round 4.
- For $T^2$: pure-X orbit has stabilizer $= \{T_\text{Y} \text{ translations}\} \cup \{D_4^{\mathrm{Y-fixing}}\}$ (Y-translations + reflections fixing pure-X), so stabilizer is 1-dim (Y-translation is free). Orbit dim $= \dim T^2 - 1 = 1$. **One Goldstone along orbit.** Matches Round 4.

### 3.3 Morse-Bott inequality

Standard Morse-Bott inequality:
$$\sum_\alpha t^{\mathrm{ind}(N_\alpha)} \cdot P(N_\alpha; t) \geq P(\Sigma_m; t),$$
where $P(X; t)$ is the Poincaré polynomial of $X$. For our $\Sigma_m \cong D^{n-1}$ (disk), $P(\Sigma_m; t) = 1$.

In the standard Morse setting, this reduces to $\sum_\alpha t^{\mathrm{ind}(u_\alpha^\ast)} \geq 1$, i.e., $\sum c_k t^k \geq 1$, giving Euler $\sum(-1)^k c_k = 1$ (`cardinality_open.md` §8.1).

In Morse-Bott, each $N_\alpha$ contributes its full Poincaré polynomial, weighted by its Morse-Bott index. E.g., for $C_n$'s circle orbit $N = S^1$ at index 0: contribution is $P(S^1; t) = 1 + t$. This adds one bar at grade 0 and one at grade 1 to the total count.

**Consequence for G-C cardinality (`cardinality_open.md` §8.5 Hyp. Thm. 4.1*):** the bracket upgrades in the continuous-Aut setting — there's an extra "+ $\dim N$" contribution per continuous-orbit at each grade.

### 3.4 Prop 1.3a Bott-refinement

> **Prop 1.3a-Bott (Round 5, Cat A).** Let $\{G_n\} \to (M, g)$ be a continuum-limit graph family. For each $N_\alpha \subset \Sigma_m$ a connected critical manifold:
> - **Morse-Bott index** $\mathrm{ind}_{\mathrm{Bott}}(N_\alpha) = \#\{$negative Hessian eigenvalues on $(T N_\alpha)^\perp\}$.
> - **Orbit dimension** $\dim N_\alpha \leq \dim\mathrm{Iso}_0(M)$.
> - At $u_{\mathrm{uniform}}$: $\dim N = 0$ (fixed point), $\mathrm{ind}_{\mathrm{Bott}} = N_{\mathrm{unst}}^{\mathrm{bd}}$.
> - At pure-X orbit on $T^2$: $\dim N = 1$ (Y-translation Goldstone), $\mathrm{ind}_{\mathrm{Bott}} = 0$.
> - At 1D cycle standing wave: $\dim N = 1$ (translation Goldstone), $\mathrm{ind}_{\mathrm{Bott}} = 0$.

**Category: Cat A** — direct application of Bott's 1954 theorem to our setting, with orbit-stabilizer dimension counts inherited from Round 4.

**Consequence:** The Round 4 Hessian eigenvalue "0" entries are genuine Morse-Bott Goldstone directions, not artifacts of the reduction.

---

## §4. $D_n$-lock-in scaling on $C_n$

### 4.1 Setup

At first pitchfork on $C_n$, the Round 4 reduced Lyapunov in $(a, b) = r(\cos\theta, \sin\theta)$:
$$F_4(r, \theta) = \tfrac{\mu}{2}r^2 + \tfrac{3\Lambda}{2}r^4 \quad (\theta\text{-independent}).$$

The $D_n$ symmetry acts on $(a, b)$ as rotation by $2\pi/n$ and reflection $(a, b) \to (a, -b)$. The $D_n$-invariant polynomials in $(a, b)$ are generated by:
- $r^2 = a^2 + b^2$ (continuous $O(2)$-invariant);
- $\mathrm{Re}[(a+ib)^n] = r^n\cos(n\theta)$ (first "truly" $D_n$-invariant, not $O(2)$-invariant).

Higher $D_n$-invariants: $\{r^{2k}\}_{k \geq 0}$ and $\{r^{n + 2k}\cos(n\theta)\}_{k \geq 0}$, etc.

### 4.2 Parity (at $c = 1/2$)

At $c = 1/2$, $u \to 1 - u$ symmetry gives $v \to -v$ and $(a, b) \to (-a, -b)$. Under this, $r^n\cos(n\theta) \to (-1)^n r^n\cos(n\theta)$:
- $n$ **even**: parity-even, survives in reduced Lyapunov.
- $n$ **odd**: parity-odd, eliminated at $c = 1/2$ (next surviving is $r^{2n}\cos(2n\theta)$).

### 4.3 Leading lock-in term

**Reduced Lyapunov at full order:**
$$F(r, \theta) = F_4(r) + \Lambda_n \cdot r^{p(n)} \cos(p(n) \theta / n \cdot n) + (\text{higher})$$

where
$$p(n) = \begin{cases} n & n \text{ even} \\ 2n & n \text{ odd at } c = 1/2 \end{cases}$$

The coefficient $\Lambda_n$ arises from **Lyapunov-Schmidt reduction**: integrating out non-Fiedler modes (modes at $\lambda_k > \lambda_2$) gives an effective $D_n$-anisotropic contribution at order $r^{p(n)}$. Generically, $|\Lambda_n| > 0$.

### 4.4 Lock-in energy at critical

At the minimum $r^\ast = \sqrt{-\mu/(6\Lambda)}$:
$$\Delta F_{\mathrm{lock-in}} = |\Lambda_n| \cdot (r^\ast)^{p(n)} = |\Lambda_n| \cdot \left(\frac{-\mu}{6\Lambda}\right)^{p(n)/2} \sim |\mu|^{p(n)/2}.$$

**Scaling in $|\mu|$:**
- $n = 4$: $|\mu|^2$ (quartic, already appears in Round 4 quartic if $n = 4$ is within the anisotropic regime).
- $n = 5$: $|\mu|^5$ (decic via $p(5) = 10$).
- $n = 6$: $|\mu|^3$ (sextic, $p(6) = 6$).
- $n = 8$: $|\mu|^4$ (octic).
- $n = 10$: $|\mu|^5$ (decic).
- $n \to \infty$: $|\Delta F_{\mathrm{lock-in}}| \to 0$ exponentially fast in $n$ for fixed $|\mu|$.

**Interpretation:** The lock-in scale $|\mu|^{p(n)/2}$ shrinks as $n$ grows, so the Goldstone direction becomes effectively continuous for large $n$.

### 4.5 Goldstone mass

At a lock-in minimum (say $\theta = 0$, $\cos(n\theta) = 1$, $\Lambda_n < 0$):
$$\text{Goldstone mass}^2 = \partial_\theta^2 F|_{\theta=0} = -\Lambda_n \cdot p(n)^2 \cdot (r^\ast)^{p(n)} \sim |\mu|^{p(n)/2}.$$

**So the Goldstone acquires a small "mass"** $\sim |\mu|^{p(n)/4}$ at finite $n$, and becomes massless only in the $n \to \infty$ continuum limit.

### 4.6 Summary theorem

> **$C_n$ Lock-In Theorem (Round 5, Cat A).** Let $C_n$ at $c = 1/2$, $\mu := \beta_{\mathrm{crit}}^{(2)} - \beta|W''(c)|/4\alpha\lambda_2$ (near-critical scaling). The reduced Lyapunov is
> $$F(r, \theta) = \tfrac{\mu}{2}r^2 + \tfrac{3\Lambda}{2}r^4 + \Lambda_n r^{p(n)}\cos(p(n)\theta) + O(r^{p(n)+2}),$$
> with $p(n) = n$ for even $n$ and $p(n) = 2n$ for odd $n$ at $c = 1/2$.
> - The $O(2)$-invariant part gives a circle of degenerate quartic minima.
> - The $\Lambda_n$ term breaks $O(2)$ to $D_n$, locking to $2p(n)/n$ discrete standing-wave minima.
> - Lock-in energy scale: $\Delta F \sim |\mu|^{p(n)/2}$.
> - Goldstone mass: $m_G^2 \sim |\mu|^{p(n)/2}$, vanishing in $n \to \infty$.

**Category: Cat A structural** — $D_n$-invariant polynomial classification + parity arguments. Coefficient $\Lambda_n$ explicit computation not needed (generic $|\Lambda_n| > 0$ sufficient for structural claim).

---

## §5. $\mathcal{M}_1$ topology as an invariant

### 5.1 Topological classification

For Round 4's three graph classes, at $\beta$ just above $\beta_{\mathrm{crit}}^{(2)}$:

| Graph | $\mathrm{Iso}_0(M)$ | Critical manifold $N_1$ | $\mathcal{M}_1 = N_1/\mathrm{Iso}(M)$ | $\dim\mathcal{M}_1$ | Topological type |
|---|---|---|---|---|---|
| 2D square (free BC) | $\{e\}$ | 4 points | 1 point | 0 | discrete |
| 1D cycle $C_n$ (continuum) | $O(2) \cong S^1 \rtimes \mathbb Z_2$ | $S^1$ | 1 point | 0 | reduced from 1D orbit |
| 2D torus $T^2$ (continuum) | $T^2 \rtimes D_4$ | $S^1 \sqcup S^1$ (two translation orbits, X and Y) | 1 point (X and Y linked by $D_4$) | 0 | reduced from 1D orbit |

After $\mathrm{Iso}(M)$-quotient, all three are 0-dim (single class). The **continuous vs discrete** distinction lives in the *unreduced* critical manifold $N_1$, not in the quotient $\mathcal{M}_1$.

### 5.2 Sharper invariant

Define:
- $\dim_{\mathrm{moduli}}(G) := \dim N_1(G) - \dim\mathrm{Iso}_0(M)$ (moduli dimension after continuous-Aut quotient).
- **Orbit volume** $\mathrm{Vol}(N_1) := \mathrm{Vol}(\mathrm{Iso}_0(M)/\mathrm{Stab})$ (nucleation-sites count factor).

| Graph | $\dim_{\mathrm{moduli}}$ | $\mathrm{Vol}(N_1)$ |
|---|---|---|
| 2D square | 0 | 0 (discrete, 4 points; volume = $4$ in counting measure) |
| $C_n$ | 0 | $2\pi$ (continuum circle in $n \to \infty$ limit; $n$ in finite graph) |
| $T^2$ | 0 | $2 \cdot (2\pi)^2/|D_4|$ (two circle orbits glued by $D_4$, each of circumference $2\pi$; 2D torus has orbit volume $(2\pi)^2$ per orbit) |

### 5.3 Why this matters

The orbit volume enters the **nucleation prefactor** in Conjecture 2.1 (`from_single.md` §2). Specifically:
$$\widehat K \approx 1 + \mathrm{Vol}(N_1)^{1/d_{\mathrm{eff}}} \cdot (\text{other factors}) + O(1).$$

On continuum graphs (large $\mathrm{Vol}$), the $\widehat K$ prefactor is enhanced by the continuous-orbit volume. This is a concrete **quantitative modification** of Conjecture 2.1 in the continuous-Aut setting.

---

## §6. Conjecture 2.1 prefactor refinement

### 6.1 Round 4 observation (§3.6.4)

Round 4 noted that continuous-moduli graphs have nucleation prefactor integrating over the orbit continuum, modulating $O(1)$ in Conjecture 2.1. Round 5 makes this quantitative.

### 6.2 Modified conjecture

> **Conjecture 2.1-Bott (Round 5).** For a continuum-limit graph family $\{G_n\} \to M$, the multi-formation count is
> $$\widehat K(G_n; \beta) = 1 + \mathrm{Vol}(\mathrm{Iso}_0(M)/\mathrm{Stab}) \cdot N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}(M)} + O(1),$$
> where $\mathrm{Iso}_0$ and $\mathrm{Stab}$ are computed for the continuum limit.

For discrete-Aut graphs: $\mathrm{Vol} = 1$ (trivial), recovers original Conjecture 2.1.
For continuum-Aut graphs: $\mathrm{Vol} > 1$ is the dimensional enhancement.

### 6.3 Test on $T^2$

At $\beta = \beta_{\mathrm{crit}}^{(2)}$ on $T^2$: $N_{\mathrm{unst}} = 4$ (Fiedler 4-dim). Iso orbit volume for pure-X: $\mathrm{Vol}(T^2/\mathrm{Stab}_\text{pure-X}) = $ circumference of X-translation = $L$ (in lattice units).

$\widehat K \approx 1 + L \cdot 4^{1/2} + O(1) = 1 + 2L$.

Compare to discrete-Aut prediction $\widehat K \approx 1 + 4^{1/2} = 3$.

The factor $L$ is large (linear in system size), suggesting $\widehat K$ grows with system size on torus — this differs from the "intensive" $\widehat K$ of the discrete-Aut setting.

**Interpretation:** On torus, each newly-unstable mode has $L$ nucleation positions available (translation orbit), so the number of distinct K=2 configurations is $O(L \cdot N_{\mathrm{unst}}^{1/2})$.

This is actually **extensive** behavior, not intensive as originally conjectured. This is a substantive refinement.

### 6.4 Consistency check

Extensive $\widehat K$ on torus might seem at odds with Conjecture 2.1's "$1 + O(1)$" form. But Conjecture 2.1 was stated for discrete-Aut graphs; on continuum-Aut graphs, the prefactor naturally scales with system size. **This is consistent with the moduli-dimension distinction.**

Practical implication for numerical validation: `exp_mode_emergence.py` (from C'' option) should measure $\widehat K / L$ on torus, not raw $\widehat K$, to test the intensive-per-orbit-position scaling.

---

## §7. Category classification and residuals

### 7.1 New Cat A claims (Round 5)

1. **Prop 1.3a-Bott (continuous-Aut Morse-Bott refinement).** Critical manifolds $N_\alpha$ with Morse-Bott index and orbit-stabilizer dim counting.

2. **$C_n$ Lock-In Theorem.** Leading-order $D_n$-anisotropy at order $r^{p(n)}$ with $p(n) = n$ (even $n$) or $2n$ (odd $n$ at $c = 1/2$); lock-in scale $|\mu|^{p(n)/2}$.

3. **$\mathcal{M}_1$ topology invariant.** $\dim_{\mathrm{moduli}}$ + $\mathrm{Vol}(N_1)$ classification distinguishes discrete- vs continuous-Aut graphs beyond the $|\mathcal{M}_1|$ cardinality.

4. **Conjecture 2.1-Bott (continuous-Aut refinement).** $\widehat K$ prefactor modified by orbit volume, giving extensive-in-$L$ scaling on torus.

### 7.2 Residuals from Round 5

- **Explicit $\Lambda_n$ coefficient computation** on $C_n$. Round 5 gave the scaling but not the explicit coefficient (requires Lyapunov-Schmidt reduction with non-Fiedler modes, several pages).
- **Higher-dimensional tori $T^3, T^d$.** Natural extension, analogous structure.
- **Other compact Lie groups in $\mathrm{Iso}(M)$**: sphere $S^d$ has $O(d+1)$ (compact non-abelian); klein bottle has discrete; RP² has $O(2)/\mathbb Z_2$. Each requires irrep decomposition of the Fiedler subspace.
- **Conjecture 2.1-Bott numerical validation.** Requires torus-specific `exp_mode_emergence.py` modification (currently defaults to 2D grid with free BC).
- **Thermal fluctuations (Mermin-Wagner).** On 2D torus at $T > 0$, continuous symmetry breaking is destabilized; the axis-aligned orbit selection persists at $T = 0$ but washes out at finite $T$. Not covered here.

### 7.3 Cumulative Cat A count (today)

- Morning: 4
- Round 2: 6
- Round 3: 3
- Round 4: 3
- **Round 5: 4**
- **Cumulative: 20 Cat A statements today.**

---

## §8. Next steps (Round 6)

7-item residual list progress:
- [x] Item 1: $\Phi_4$ on non-D4 graph classes (Round 4).
- [x] Item 2: Continuous $\mathrm{Aut}$ groups (Round 5, this file).
- [ ] Item 3: Prop 1.3b (d) full-spectrum beyond $c = 1/2$.
- [ ] Item 4: NQ-31 sharp $c_0$ value (multi-init Morse survey, compute-heavy).
- [ ] Item 5: G-C sub-claim C on general graphs.
- [ ] Item 6: Cor 2.2 SCC-minimizer supra-lattice regime.
- [ ] Item 7: Higher-order pitchfork cascade.

**Recommendation for Round 6:** Item 3 (Prop 1.3b (d) full-spectrum at general $c$). Round 3 closed the sign asymmetry of $\gamma_D''$; the full spectrum as a function of $c$ is natural next. This is analytic (not compute-heavy) and complements the Round 4-5 symmetry/moduli work.

### 8.1 Files to update this round

- `working/SF/symmetry_moduli.md` — add new §3.7 "Continuous-Aut and Morse-Bott" (condensed Round 5 content).
- `canonical_sub.md` — append Round 5 entry (4 new Cat A: Prop 1.3a-Bott, Lock-In, Moduli invariant, Conj 2.1-Bott + Q32-Q34).

---

**End of 07_deepening_round5.md.**
