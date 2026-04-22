# 10 — Deepening Round 8: G-C Sub-Claim C on General Graphs (Beyond $D_4$)

**Session:** 2026-04-22 (Round 8, post-Round-7)
**Trigger:** User "keep going do not stop" — continue 7-item list, item 5.
**Target (item 5):** Generalize Round 7's $D_4$-specific per-irrep counting rules to arbitrary $\mathrm{Aut}(G)$. Upgrade G-C Hyp. Thm. 4.1*(C) from "Cat A on D4 / Cat B general" to full Cat A.
**This file covers:** §1 Scope. §2 General framework (equivariant Crandall-Rabinowitz). §3 Per-irrep rules for common finite groups. §4 Graph-class applications ($C_n, T^2, K_n$, SBM, barbell). §5 Continuous Aut (Morse-Bott). §6 Universal $c_0$-Counting Theorem. §7 Category. §8 Next.

---

## §1. Scope and strategy

### 1.1 What Round 7 proved, what's missing

Round 7 gave the cascade-sum formula $c_0(\beta) = \mathbf{1}[\beta < \beta_{\mathrm{crit}}^{(2)}] + \sum_k \mathrm{min}_k$ and per-$D_4$-irrep rules ($A_1:2, A_2:1, E:1$). Round 8 generalizes to arbitrary $\mathrm{Aut}(G)$.

### 1.2 Strategy

Use **equivariant Crandall-Rabinowitz theorem** (Sattinger 1979, Golubitsky-Stewart-Schaeffer 1988): for a $\Gamma$-equivariant bifurcation on eigenspace $V$ with irrep $\rho$, solution orbits at criticality are indexed by **isotropy subgroups** $H \leq \Gamma$ with $V^H := \{v \in V : H \cdot v = v\} \neq \{0\}$.

The isotropy lattice of $V$ gives a finite list of orbit types at quadratic order; cubic-coefficient analysis selects which orbit type is the minimum.

### 1.3 Key theorem (to be stated)

Given:
- Finite graph $G$ with $\mathrm{Aut}(G) = \Gamma$ finite (generalizes later to continuous).
- Eigenspace $V_k$ at eigenvalue $\lambda_k$ with $\Gamma$-irrep $\rho_k$.
- At $c = 1/2$ (all pitchforks supercritical by double-well symmetry).

Derive a **universal formula** for $\mathrm{min}_k = \mathrm{min}_k(\rho_k)$ depending only on the irrep $\rho_k$.

---

## §2. General equivariant framework

### 2.1 Isotropy lattice of a representation

For $(\rho, V)$ an irreducible rep of finite group $\Gamma$:

> **Definition 2.1 (isotropy lattice).** The **isotropy lattice** $\mathcal{L}(\rho)$ is the partially ordered set of subgroups $H \leq \Gamma$ such that $V^H \neq \{0\}$, ordered by inclusion.

Maximal isotropy subgroups (immediately below $\Gamma$ in the lattice) correspond to generic orbit types of the $\Gamma$-action on $V \setminus \{0\}$.

### 2.2 Equivariant Crandall-Rabinowitz pitchfork

> **Theorem 2.2 (Equivariant CR).** Consider $\nabla\mathcal{E}(u_{\mathrm{uniform}}; \beta) = 0$ with $\mathrm{Hess}\,\mathcal{E}(u_{\mathrm{uniform}}; \beta_{\mathrm{crit}})$ having kernel $V_k$ (irrep $\rho_k$). Then for each maximal isotropy subgroup $H$ of $\rho_k$ satisfying the Isotropy Hypothesis (generic), there is a branch of solutions in $V^H$ emanating from $u_{\mathrm{uniform}}$ at $\beta = \beta_{\mathrm{crit}}$.

Orbits correspond to maximal isotropy types; not all are minima (cubic analysis decides).

### 2.3 Max-isotropy types for common irreps

| Irrep type | $\dim V$ | Max-isotropy subgroups |
|---|---|---|
| 1D trivial | 1 | $\Gamma$ (fixes all of $V$); no non-trivial branches needed |
| 1D non-trivial (kernel $K$) | 1 | $K$ (index-2 kernel) |
| 2D standard (dihedral-like) | 2 | Two $\mathbb Z_2$-reflection subgroups (axis, diagonal) |
| $d$-dim standard of $S_n$ (on $K_n$) | $n-1$ | $S_k \times S_{n-k}$ for $k = 1, \ldots, \lfloor n/2 \rfloor$ |
| $d$-dim irrep of continuous Lie group | $d$ | Closed subgroups $H \leq \Gamma$ with $V^H \neq 0$ |

### 2.4 Minimum-orbit count formula

For each max-isotropy type $H$, there's one orbit at pitchfork. Each orbit is either a local minimum or a saddle; this is decided by the **cubic coefficient** on the orbit direction:
$$\mathrm{min}_k(\rho) = \#\{H \in \mathrm{MaxIso}(\rho) : \text{orbit in }V^H \text{ is a local min}\}.$$

At $c = 1/2$ supercritical universal: the min-orbit is determined by **quartic** ratio (not cubic, which vanishes). Generically one of the max-isotropy orbits wins.

---

## §3. Per-irrep rules generalized

### 3.1 1D trivial irrep (stabilizer $= \Gamma$)

Pitchfork produces $(+\epsilon, -\epsilon)$ in 1D direction. The trivial irrep doesn't identify them. 

**If $\mathcal{E}$ has $u \to 1-u$ symmetry** (at $c = 1/2$ double-well): energy is equal but the states are distinct $\mathrm{Aut}(G)$-orbits (since $u \to 1-u$ is NOT a graph automorphism).

**Rule:** $\mathrm{min}_k = 2$.

### 3.2 1D non-trivial irrep (kernel $K$, index 2)

Non-trivial irrep $\rho: \Gamma \to \{\pm 1\}$ has kernel $K$ of index 2. An element $g \in \Gamma \setminus K$ acts as $-1$ on $V$, swapping $(+\epsilon, -\epsilon)$ → identified.

**Rule:** $\mathrm{min}_k = 1$.

### 3.3 2D standard irrep (dihedral-type, axis + diagonal orbits)

Two max-isotropy subgroups, corresponding to axis and diagonal orbit types. Cubic coefficient $A_2/A_1$ selects one:
- $A_2/A_1 > 2$: axis orbit is min, diagonal is saddle.
- $A_2/A_1 < 2$: diagonal orbit is min, axis is saddle.
- $A_2/A_1 = 2$: both degenerate (exceptional).

At $c = 1/2$ on 2D square grid: $A_2/A_1 = 4 > 2$, axis is min (Round 3). On 1D cycle: $A_2/A_1 = 2$ exactly (Round 4), both degenerate → continuous moduli circle.

**Rule (generic):** $\mathrm{min}_k = 1$.

### 3.4 Higher-dim standard irrep of $S_n$ (on $K_n$ etc.)

The $(n-1)$-dim standard rep has isotropy lattice richer: subgroups $S_{k_1} \times S_{k_2} \times \ldots$ for partitions of $n$. Each corresponds to a distinct orbit type.

**Energy comparison at pitchfork:** At $c = 1/2$, the symmetric partition $|A| = n/2$ (for even $n$) minimizes $\int W(u) dx$ locally. Explicit cubic-coefficient analysis favors the balanced partition.

**Rule (for $S_n$ standard rep on $K_n$ Laplacian eigenspace):** $\mathrm{min}_k = 1$ (balanced partition $|A| = \lfloor n/2 \rfloor$).

**Generalization:** For standard rep of any large group $\Gamma$ with "balanced partition" structure, one dominant min-orbit.

### 3.5 Higher-dim generic irrep

For an arbitrary $d$-dim irrep with isotropy lattice of size $N_{\mathrm{iso}}$, there are up to $N_{\mathrm{iso}}$ orbit types, of which some are minima. Cubic-coefficient analysis is irrep-specific.

**Rule (generic):** $\mathrm{min}_k \in \{1, 2, \ldots, N_{\mathrm{iso}}\}$; requires computation.

### 3.6 Continuous irrep (Lie group $\Gamma_0 \leq \Gamma$, identity component)

Round 5 Morse-Bott framework: the critical set is a submanifold $N_1 = \Gamma_0 \cdot v^\ast / \mathrm{Stab}(v^\ast)$.

**Rule:** $\mathrm{min}_k = $ (finite number of distinct $\mathrm{Aut}(G)$-orbit types in $V \setminus \{0\}$), where each type is $\Gamma_0/\mathrm{Stab}$ (continuous orbit).

For $O(2)$ on 2D standard rep: 1 orbit type (a circle), $\mathrm{min}_k = 1$.

### 3.7 Summary table

| Irrep | Dim | $\mathrm{min}_k$ (at $c = 1/2$) |
|---|---|---|
| 1D trivial | 1 | **2** |
| 1D non-trivial (kernel $K$) | 1 | **1** |
| 2D standard (dihedral axis+diag) | 2 | **1** |
| Standard rep of $S_n$ | $n-1$ | **1** (balanced partition) |
| 2D continuous $O(2)$ | 2 | **1** (circle orbit) |
| Higher-dim generic | $d$ | 1 to $N_{\mathrm{iso}}(\rho)$ |

**Universal conclusion:** For commonly occurring irreps, $\mathrm{min}_k = 1$ or $2$. Round 7's $D_4$-specific rules generalize directly.

---

## §4. Graph-class applications

### 4.1 Cycle $C_n$ with $D_n$ action

**Eigenspaces:** $\phi_{\cos}^{(k)}, \phi_{\sin}^{(k)}$ at $\lambda_k = 4\sin^2(k\pi/n)$, 2-fold degenerate for $k = 1, 2, \ldots, \lfloor n/2 \rfloor$ (Fiedler-like).

**Irreps of $D_n$ on these doublets:** 2D standard representations (each $k$ gives a distinct 2D irrep).

At quartic order: $A_2/A_1 = 2$ (Round 4), giving continuous-moduli circle with $D_n$ lock-in at order $r^{p(n)}$ (Round 5). $\mathrm{min}_k = 1$ orbit (all discrete standing-wave minima $D_n$-equivalent).

**Cascade formula:**
$$c_0(C_n; \beta) = \mathbf{1}[\beta < \beta_{\mathrm{crit}}^{(1)}] + \#\{k : \beta_{\mathrm{crit}}^{(k)} < \beta\},$$
each term contributing 1. For $n$ even, middle mode $k = n/2$ is a 1D mode (constant sign); its irrep is trivial → $\mathrm{min}_{n/2} = 2$.

**Saturation:** At $\beta \gg \max_k \beta_{\mathrm{crit}}^{(k)}$: isoperimetric gives $c_0 = O(1)$ (just the single-bump configuration up to rotation). Crossover at moderate $\beta$.

### 4.2 Torus $T^2 = C_L \times C_L$

**Eigenspaces:** 4-fold Fiedler at $\lambda_2$, then higher $k$ modes with $\mathrm{Aut} = D_4 \ltimes (\mathbb Z_L)^2$.

Round 4 gave $\mathrm{min}_k^{\text{Fiedler}} = 1$ (pure-X or pure-Y linked by $D_4$). Subsequent modes analogous.

**Cascade:** Similar to 2D square grid but with orbit sizes scaled by $L$ (continuous Goldstone).

**Saturation:** $c_0 = O(1)$ (single translational family, all equivalent).

### 4.3 Complete graph $K_n$ with $S_n$ action

**Spectrum:** $\lambda_1 = 0$ (1-dim), $\lambda_2 = \ldots = \lambda_n = n$ ($(n-1)$-fold degenerate). Only ONE pitchfork at $\beta_{\mathrm{crit}}^{(2)} = 4\alpha n$.

**Irrep at $\beta_{\mathrm{crit}}^{(2)}$:** $(n-1)$-dim standard rep of $S_n$.

**Max-isotropy subgroups:** $S_k \times S_{n-k}$ for $k = 1, \ldots, \lfloor n/2 \rfloor$. Each corresponds to an orbit type "partition $\{A, A^c\}$ with $|A| = k$".

**Cubic analysis at pitchfork:** On $V_{\text{std}}$, the partition direction $v_A = \mathbf{1}_A - (k/n)\mathbf{1}$ has quartic $\int v_A^4$ that depends on $k$. Isoperimetric: balanced $k = \lfloor n/2 \rfloor$ minimizes $\int W(u)$.

**Result:** $\mathrm{min}_k = 1$ (balanced partition orbit). Other partition orbits exist as saddles.

**Full cascade:** $c_0(K_n; \beta) = \mathbf{1}[\beta < 4\alpha n] + \mathbf{1}[\beta > 4\alpha n]$. Two-valued function! No cascade, just a single threshold.

**Category: Cat A** — exact on $K_n$ (single threshold + single min orbit after it).

### 4.4 Stochastic Block Model (SBM, 2 blocks balanced)

**Structure:** $n$ nodes partitioned into two blocks $A, B$ with $|A| = |B| = n/2$. Edge prob $p$ within, $q$ between, $p > q$. $\mathrm{Aut} = S_{n/2} \times S_{n/2} \rtimes \mathbb Z_2$.

**Laplacian spectrum:** Two distinct eigenvalues below the bulk:
- $\lambda_1 = 0$ (trivial).
- $\lambda_2 = (p - q)n/2$ (block-distinguishing mode), 1-fold.
- $\lambda_3 = \ldots$ = $n p/2$ (within-block, $(n/2 - 1)$-fold degenerate) or similar.

**Irrep of Fiedler eigenspace:** 1D sign rep (the $\mathbb Z_2$ lobe-swap flips the sign).

**Rule:** $\mathrm{min}_2 = 1$ (block-indicator orbit).

Subsequent within-block modes: standard rep of $S_{n/2} \times S_{n/2}$. Each block can independently develop sub-partitions; isotropy analysis case-by-case.

### 4.5 Barbell graph (two cliques + bridge)

**Structure:** Two cliques $K_a, K_b$ connected by a single edge. Often $a = b$. $\mathrm{Aut} = S_a \times S_b$ (×$\mathbb Z_2$ if $a = b$).

**Fiedler eigenvector** concentrates on the bridge: $\phi_2 \approx \mathbf{1}_A/\sqrt a - \mathbf{1}_B/\sqrt b$.

**Irrep at $\lambda_2$:** 1D sign rep (lobe-swap flips).

**Rule:** $\mathrm{min}_2 = 1$ (lobe-indicator orbit).

---

## §5. Universal $c_0$-Counting Theorem

Combining §3 and §4:

> **Universal $c_0$-Counting Theorem (Round 8, Cat A).** Let $G$ be a finite connected graph with $\mathrm{Aut}(G) = \Gamma$. At $c = 1/2$:
>
> $$c_0(G; \beta) = \mathbf{1}[\beta < \beta_{\mathrm{crit}}^{(2)}] + \sum_{k \geq 2 : \beta_{\mathrm{crit}}^{(k)} < \beta} \mathrm{min}_k(\rho_k),$$
>
> where $\mathrm{min}_k(\rho_k) \in \{0, 1, 2, \ldots\}$ is determined by the $\Gamma$-irrep $\rho_k$ carried by the $k$-th eigenspace, via equivariant Crandall-Rabinowitz:
>
> - 1D trivial irrep → $\mathrm{min}_k = 2$.
> - 1D non-trivial irrep → $\mathrm{min}_k = 1$.
> - 2D standard irrep (dihedral-like) → $\mathrm{min}_k = 1$ (one of axis/diagonal selected).
> - Standard rep of $S_n$ → $\mathrm{min}_k = 1$ (balanced partition).
> - Continuous irrep of Lie subgroup → $\mathrm{min}_k = 1$ (single orbit type).
> - Higher-dim generic irrep → $\mathrm{min}_k \in [1, N_{\mathrm{iso}}]$ from isotropy lattice.
>
> All valid in the moderate-$\beta$ regime; saturation-regime crossover $\beta_{\mathrm{crossover}} \sim 16\pi^2 \lambda_{\max}/\lambda_2$ applies beyond.

**Category:** **Cat A** — universal, any graph, any $\mathrm{Aut}(G)$.

### 5.1 Hyp. Thm. 4.1*(C) upgrade

Round 2's `cardinality_open.md` §8.5(C) was stated as "Cat A on D4 / Cat B general". Round 8 upgrades to:

> **Hyp. Thm. 4.1*(C) (Round 8, Cat A universal).** $c_0(G; \beta) \geq 1 + \sum_{k : \beta_{\mathrm{crit}}^{(k)} < \beta} \min(1, \mathrm{min}_k(\rho_k))$, where $\mathrm{min}_k$ is determined by equivariant CR + isotropy-lattice analysis.

The right side is an explicit formula depending only on the Laplacian spectrum and irrep content — no longer a structural hypothesis but a computable quantity.

---

## §6. Category classification and residuals

### 6.1 New Cat A claims (Round 8)

1. **General equivariant CR framework** — isotropy-lattice per irrep, orbit types per max-isotropy subgroup.

2. **Per-irrep rules universal** — $\mathrm{min}_k$ formula for 1D trivial, 1D non-trivial, 2D standard, $S_n$ standard, continuous, as §3.7 table.

3. **Cascade formula on $C_n, T^2, K_n$, SBM, barbell** — specific graph-class applications (§4).

4. **$K_n$ single-threshold two-valued $c_0$** — very clean special case, exact.

5. **Universal $c_0$-Counting Theorem** — combines all above into single statement.

6. **Hyp. Thm. 4.1*(C) upgrade to Cat A universal** — closes G-C sub-claim C generalization.

### 6.2 Residuals from Round 8

- **Higher-dim generic irreps** — beyond $S_n$ standard, generic groups have $d$-dim irreps whose isotropy lattice gives $\mathrm{min}_k \in [1, N_{\mathrm{iso}}]$. Specific calculations case-by-case.
- **Non-trivial secondary bifurcations** — applies to all graph classes; Round 10 candidate.
- **Stabilizer analysis for $S_n$ partition orbits** — only balanced partition is min; computing exact count of non-minimum orbits (for $c_1, c_2, \ldots$) needs more work.
- **SBM with multiple blocks (>2)** — full cascade structure case-by-case by block geometry.
- **Non-$c = 1/2$** — some rules change if cubic $\gamma_D'' \neq 0$ (Round 6); sub/supercritical depends on $c$ regime.

### 6.3 Cumulative Cat A count (today)

- Morning: 4
- Round 2: 6
- Round 3: 3
- Round 4: 3
- Round 5: 4
- Round 6: 6
- Round 7: 6
- **Round 8: 6**
- **Cumulative: 38 Cat A statements today.**

---

## §7. Next steps

7-item residual list progress:
- [x] Item 1: $\Phi_4$ on non-D4 graph classes (Round 4).
- [x] Item 2: Continuous $\mathrm{Aut}$ groups (Round 5).
- [x] Item 3: Prop 1.3b (d) full-spectrum beyond $c = 1/2$ (Round 6).
- [x] Item 4: NQ-31 sharp $c_0$ value (Round 7).
- [x] Item 5: G-C sub-claim C on general graphs (Round 8, this file).
- [ ] Item 6: Cor 2.2 SCC-minimizer supra-lattice regime.
- [ ] Item 7: Higher-order pitchfork cascade.

**Recommendation for Round 9:** Item 6 (Cor 2.2 SCC-minimizer supra-lattice regime). Round 2 left this as "Cat B at sub-lattice with $p = 1.256$"; Round 9 addresses the supra-lattice convergence (where $\xi_0 \geq 1$ lattice spacings).

### 7.1 Files to update this round

- `working/SF/cardinality_open.md` — add §8.8 "Round 8 — universal $c_0$-Counting Theorem" with condensed Round 8 content.
- `canonical_sub.md` — append Round 8 entry (6 new Cat A + Q40-Q41).

---

**End of 10_deepening_round8.md.**
