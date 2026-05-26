---
type: working/proof
created: 2026-05-08
session: Session 5
project: Observer Moduli Space of SCC
stage: OMS-1.1 → OMS-1.2 candidate
attacks: OP-OMS-018
status: PARTIAL RESOLUTION (local R1/R2 PROVED; global C^1 REJECTED; value function and envelope PROVED)
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# OP-OMS-018 — Regularity of $u^*(\lambda)$

Theoretical attack on OP-OMS-018: under what conditions is $\lambda \mapsto u^*(\lambda)$
continuous / $C^1$ / Lipschitz? This document classifies the question into
three sub-claims (interior local, boundary local, global) and proves what is
provable.

Classification: **DEFINED** | **PROVED** | **PROOF SKETCH** | **HYPOTHESIZED** | **OPEN** | **REJECTED**.

---

## §1. Setup

### Domain.

Fix scene $X_t$ and mass $m \in (0, n)$. The optimization domain is the
mass-fixed box:

$$\Omega := \Sigma_m \cap [0,1]^n = \{u \in \mathbb{R}^n : \mathbf{1}^\top u = m,\ 0 \le u_i \le 1\}.$$

$\Omega$ is a compact convex polytope of dimension $n - 1$ (with corners
at boundaries of the box constraints).

### Energy.

Per `definitions.md` DEF-1 and `CLAUDE.md`:

$$E_\lambda(u) := \lambda_{cl} E_{cl}(u; X_t) + \lambda_{sep} E_{sep}(u; X_t) + \lambda_{bd} E_{bd}(u; X_t) + \lambda_{tr} E_{tr}(u; X_t),$$

with $\lambda \in \Delta^3 = \{\lambda \in \mathbb{R}^4_{\ge 0} : \sum_i \lambda_i = 1\}$.

**Smoothness of components** (verified in `scc/energy.py`, FD-tested to 1e-9):

- $E_{cl}$ is $C^\infty$ (resolvent-based, $b_D = 0$ for analyticity, AUDIT-009).
- $E_{sep}$ is $C^\infty$ (u-weighted average of distinction).
- $E_{bd}(u) = 2\alpha\, u^\top L u + \beta \sum_i W(u_i)$ with
  $W(u) = u^2(1-u)^2$ a $C^\infty$ double-well.
- $E_{tr}$ is $C^\infty$ on $\mathrm{int}(\Omega) \times \mathrm{int}(\Omega)$
  (Sinkhorn OT with $\varepsilon_{OT} > 0$).

**Convexity in $u$.** $E_\lambda$ is **not** globally convex in $u$ (the
double-well $W(u_i)$ has $W''(c) < 0$ for $c \in (\frac{3-\sqrt{3}}{6}, \frac{3+\sqrt{3}}{6})$,
and the sign of $\beta_{bd}$ is positive, so the Hessian has spinodal
negative-curvature directions — this is precisely the T8 mechanism that
drives phase transitions). Hence multiple local minima are possible and
generically present at supercritical $\beta/\alpha$.

**Linearity in $\lambda$.** $E_\lambda(u)$ is **affine** in $\lambda$ for
each fixed $u$. This is the structural feature that makes the value
function $v(\lambda)$ tractable.

### Optimizer map.

The argmin correspondence and value function:

$$S(\lambda) := \mathrm{Argmin}_{u \in \Omega} E_\lambda(u), \qquad v(\lambda) := \min_{u \in \Omega} E_\lambda(u).$$

A **selection** $\lambda \mapsto u^*(\lambda) \in S(\lambda)$ is the object of
OP-OMS-018. The numerical pipeline (`scc/optimizer.py: find_formation`)
produces the **best of several restarts**, which is a particular selection.

---

## §2. Three regimes for the regularity question

| Regime | Hypothesis | Best-case regularity of $u^*$ |
|---|---|---|
| **A. Interior nondegenerate** | $u^*(\lambda_0)$ is a strict local min in $\mathrm{relint}(\Omega)$ with non-degenerate projected Hessian | $C^k$ if energies are $C^{k+1}$ ($k \ge 1$) — **Theorem R1** |
| **B. Boundary, fixed active set** | Active set $A_0$ fixed; strict complementarity in KKT | piecewise $C^1$ — **Theorem R2** |
| **C. Global** | No restriction; multiple local minima present | upper hemicontinuous (Berge); selections are generically discontinuous on branch-switching surfaces — **Proposition R3, REJECTED for $C^1$** |

Each regime is treated below.

---

## §3. Theorem R1 — Local $C^1$ branch (interior, non-degenerate)

### Statement.

Let $\lambda_0 \in \mathrm{int}(\Delta^3)$, and suppose there exists
$u^*_0 := u^*(\lambda_0) \in \mathrm{relint}(\Omega)$ — i.e.\ $0 < u^*_{0,i} < 1$
for all $i$ — that is a strict local minimum of $E_{\lambda_0}$ on $\Sigma_m$,
with first-order condition

$$\nabla_u E_{\lambda_0}(u^*_0) + \nu_0 \mathbf{1} = 0, \qquad \mathbf{1}^\top u^*_0 = m,\quad \nu_0 \in \mathbb{R}, \tag{$\star$}$$

and second-order condition: the projected Hessian

$$H^\perp_0 := P^\top \nabla^2_u E_{\lambda_0}(u^*_0) P \quad \text{is positive definite,}$$

where $P : \mathbb{R}^{n-1} \to \mathbb{R}^n$ is any linear injection onto
$\ker(\mathbf{1}^\top)$.

Then there exist a neighborhood $U \subset \mathrm{int}(\Delta^3)$ of $\lambda_0$ and a unique
$C^1$ map

$$\lambda \mapsto (u^*(\lambda), \nu^*(\lambda)) : U \to \mathrm{relint}(\Omega) \times \mathbb{R}$$

satisfying $(\star)$ at every $\lambda \in U$ with $u^*(\lambda_0) = u^*_0$,
$\nu^*(\lambda_0) = \nu_0$, and $u^*(\lambda)$ is a strict local minimum of
$E_\lambda$ on $\Sigma_m \cap [0,1]^n$ with the same regularity profile.

### Proof.

Define $F : \mathbb{R}^n \times \mathbb{R} \times \Delta^3 \to \mathbb{R}^{n+1}$ by

$$F(u, \nu, \lambda) := \begin{pmatrix} \nabla_u E_\lambda(u) + \nu \mathbf{1} \\ \mathbf{1}^\top u - m \end{pmatrix}.$$

By the smoothness of each $E_i$ in $u$ and the linearity of $E_\lambda$ in
$\lambda$, $F$ is $C^1$ on its domain (in fact $C^\infty$ on the relative
interior). $(\star)$ says $F(u^*_0, \nu_0, \lambda_0) = 0$.

Compute the Jacobian of $F$ in $(u, \nu)$:

$$D_{(u,\nu)} F(u^*_0, \nu_0, \lambda_0) = \begin{pmatrix} \nabla^2_u E_{\lambda_0}(u^*_0) & \mathbf{1} \\ \mathbf{1}^\top & 0 \end{pmatrix} =: M_0 \in \mathbb{R}^{(n+1) \times (n+1)}.$$

This is the **bordered Hessian**. We claim $M_0$ is invertible.

**Lemma (bordered nonsingularity).** Let $H \in \mathbb{R}^{n \times n}$ symmetric and
$\mathbf{1} \in \mathbb{R}^n$. The bordered matrix $\begin{pmatrix} H & \mathbf{1} \\ \mathbf{1}^\top & 0 \end{pmatrix}$
is nonsingular if and only if the projected Hessian $H^\perp = P^\top H P$
on $\ker(\mathbf{1}^\top)$ is nonsingular.

*Proof of lemma.* Suppose $\begin{pmatrix} H & \mathbf{1} \\ \mathbf{1}^\top & 0 \end{pmatrix} \begin{pmatrix} \delta u \\ \delta \nu \end{pmatrix} = 0$.
Then $H \delta u + \delta \nu \mathbf{1} = 0$ and $\mathbf{1}^\top \delta u = 0$.
The second equation says $\delta u \in \ker(\mathbf{1}^\top)$. Pre-multiply
the first by $P^\top$: $H^\perp (P^\top \delta u) + \delta \nu P^\top \mathbf{1} = 0$. Since
$P^\top \mathbf{1} = 0$ (because $P$ maps into $\ker(\mathbf{1}^\top)$, but the
relevant identity is $\mathbf{1}^\top P = 0$, hence $P^\top \mathbf{1} = 0$),
we get $H^\perp (P^\top \delta u) = 0$. By assumption $H^\perp$ is invertible,
so $P^\top \delta u = 0$, hence $\delta u \in \ker(\mathbf{1}^\top) \cap \mathrm{im}(P)^\perp = \{0\}$,
hence $\delta u = 0$. Plug back: $\delta \nu \mathbf{1} = 0$, so $\delta \nu = 0$. $\square$

By the hypothesis that $H^\perp_0 \succ 0$ (in particular nonsingular), $M_0$
is invertible. By the Implicit Function Theorem (Lee, *Smooth Manifolds*,
Thm C.40), there exist a neighborhood $U \ni \lambda_0$ and unique $C^1$
maps $u^* : U \to \mathbb{R}^n$, $\nu^* : U \to \mathbb{R}$ such that
$F(u^*(\lambda), \nu^*(\lambda), \lambda) \equiv 0$ on $U$ and
$u^*(\lambda_0) = u^*_0$, $\nu^*(\lambda_0) = \nu_0$.

By continuity of $u^*$, shrinking $U$ keeps $u^*(\lambda) \in \mathrm{relint}(\Omega)$
(box constraints stay strictly inactive), so $(\star)$ remains the full KKT
system on $U$. By continuity of the Hessian eigenvalues, $H^\perp(\lambda) \succ 0$
on $U$ after shrinking, so $u^*(\lambda)$ is a strict local minimum on $U$.

**Higher regularity.** If each $E_i$ is $C^{k+1}$ in $u$ (which is true for
$E_{cl}, E_{sep}, E_{bd}$; $C^\infty$), then $F$ is $C^k$ jointly, and the
IFT yields $u^*, \nu^* \in C^k(U)$. Since the SCC components used are
$C^\infty$, we obtain $u^* \in C^\infty(U)$ on this branch. $\square$

### Status.

**PROVED.** This is a textbook IFT argument; the only non-trivial step is
the bordered-nonsingularity lemma, which is standard in nonlinear
programming (Bertsekas, *Nonlinear Programming*, App. C). The hypothesis is
sharp: examples below show $u^*$ can fail to be even continuous when the
projected Hessian is singular.

### Remark — derivative of the branch.

By implicit differentiation,

$$D_\lambda \begin{pmatrix} u^*(\lambda) \\ \nu^*(\lambda) \end{pmatrix} = -M(\lambda)^{-1} \begin{pmatrix} D_\lambda \nabla_u E_\lambda(u^*(\lambda)) \\ 0 \end{pmatrix} = -M(\lambda)^{-1} \begin{pmatrix} \nabla_u E_{cl} - \nabla_u E_{tr} & \cdots \\ 0 & \cdots \end{pmatrix},$$

where the right-hand block comes from $\partial_{\lambda_i} \nabla_u E_\lambda(u) = \nabla_u E_i(u)$.
Concretely, **the perceptual Jacobian (DEF-22) along simplex tangent
directions can be evaluated analytically once $M^{-1}$ and the energy gradients are
in hand** — this is the formal foundation of VP-6 and the empirical alternative
to FD-Jacobian when a smooth branch is identified.

---

## §4. Theorem R2 — Local piecewise $C^1$ on a fixed active set (boundary case)

### Statement.

Let $\lambda_0 \in \mathrm{int}(\Delta^3)$ and $u^*_0 := u^*(\lambda_0) \in \Omega$
with active sets

$$A^=_0 := \{i : u^*_{0,i} = 0\}, \qquad A^=_n := \{i : u^*_{0,i} = 1\}, \qquad I_0 := \{i : 0 < u^*_{0,i} < 1\}.$$

Assume the **KKT first-order conditions** hold with multipliers
$\nu_0 \in \mathbb{R}$, $\mu^-_{0,i} \ge 0$ (for $i \in A^=_0$), $\mu^+_{0,i} \ge 0$ (for $i \in A^=_n$):

$$\partial_i E_{\lambda_0}(u^*_0) - \mu^-_{0,i} + \mu^+_{0,i} + \nu_0 = 0, \qquad \mathbf{1}^\top u^*_0 = m,$$

with $\mu^-_{0,i} = 0$ for $i \notin A^=_0$ and $\mu^+_{0,i} = 0$ for $i \notin A^=_n$.

Suppose:

1. **Strict complementarity:** $\mu^-_{0,i} > 0$ for $i \in A^=_0$ and $\mu^+_{0,i} > 0$ for $i \in A^=_n$.
2. **LICQ:** the gradients of the active constraints (the basis vectors $e_i$ for
   $i \in A^=_0 \cup A^=_n$, plus $\mathbf{1}$) are linearly independent in $\mathbb{R}^n$.
   (Automatic when $\vert A^=_0 \cup A^=_n\vert < n$.)
3. **Second-order sufficiency:** the projected Hessian on the tangent space
   to the active constraint manifold is positive definite:
   $H^{\perp,\mathrm{act}}_0 := \tilde P^\top \nabla^2_u E_{\lambda_0}(u^*_0) \tilde P \succ 0$,
   where $\tilde P$ is a basis of $\{\delta u : \delta u_i = 0\ \forall i \in A^=_0 \cup A^=_n,\ \mathbf{1}^\top \delta u = 0\}$.

Then there exist a neighborhood $U \ni \lambda_0$ and unique $C^1$ functions
$u^*, \nu^*, \mu^{\pm,*}$ on $U$ such that $u^*(\lambda)$ is a strict local
minimum of $E_\lambda$ on $\Omega$, the active set $A^=_0(\lambda) \cup A^=_n(\lambda) = A^=_0 \cup A^=_n$ is fixed on $U$, and $u^*(\lambda_0) = u^*_0$, etc.

### Proof.

This is the parametric NLP sensitivity theorem of Robinson (1980) and Fiacco
(1976). Specifically: writing the active-set-restricted KKT system as a $C^1$
function of $(u_{I_0}, \nu, \mu^\pm_{A^=_0 \cup A^=_n}, \lambda)$ and applying the IFT
under LICQ + strict complementarity + second-order sufficiency, the active
set is fixed in a neighborhood of $\lambda_0$ and the KKT tuple varies
$C^1$ in $\lambda$. Strict complementarity preserves the active-set
identification under perturbation: $\mu^-_{0,i} > 0$ stays positive after a
small change; $u^*_{0,i} > 0$ for $i \in I_0$ stays positive. $\square$

### Status.

**PROVED.** Standard nonlinear programming sensitivity analysis (Robinson, *Strongly
regular generalized equations*, 1980; Fiacco, *Sensitivity in NLP*, 1976).

### Failure mode (registered).

If strict complementarity fails ($\mu = 0$ at some active site), the active
set may change without warning: $u^*_{0,i} = 0$ with $\mu^-_{0,i} = 0$ admits both
"stay at 0" and "lift off" branches. The IFT does not apply. This is one
of the two main mechanisms behind branch switching (the other being the
non-convex spinodal Hessian).

---

## §5. Proposition R3 — Global Argmin correspondence is upper hemicontinuous

### Statement.

The map $S : \Delta^3 \rightrightarrows \Omega$, $\lambda \mapsto S(\lambda) = \mathrm{Argmin}_{u \in \Omega} E_\lambda(u)$,
is

1. **non-empty**, **compact-valued**;
2. **upper hemicontinuous** (u.h.c.);
3. generically **not** lower hemicontinuous, and admits **no global continuous
   selection** when $E_\lambda$ has multiple isolated local minima exchanging
   dominance across $\Delta^3$.

### Proof of (1)+(2): Berge's maximum theorem.

$\Omega$ compact, $E_\lambda$ jointly continuous in $(u, \lambda) \in \Omega \times \Delta^3$
(since each $E_i$ is continuous in $u$ and $E_\lambda$ is linear in $\lambda$).
Berge's maximum theorem (Aliprantis & Border, *Infinite-Dimensional Analysis*, Thm 17.31):

- $v(\lambda) = \min_{u \in \Omega} E_\lambda(u)$ is continuous.
- $S$ is non-empty (compactness), compact-valued (closed subset of compact),
  and u.h.c. $\square$

### Proof of (3) by counterexample (the $K_{\mathrm{core}}$-branch obstruction).

Take the VP-1 / VP-4 evidence: at $\lambda_A = (0.6, 0.2, 0.2, 0)$ on a
12×12 path graph, $u^*$ has $K_{\mathrm{core}} = 2$ (two-blob branch). At
$\lambda_B = (0.5, 0.3, 0.2, 0)$, $u^*$ has $K_{\mathrm{core}} = 1$ (single-blob
branch). On the line segment from $\lambda_A$ to $\lambda_B$, the global
minimizer must transition between these two branches at some
$\lambda_c \in (\lambda_A, \lambda_B)$.

At $\lambda_c$ both branches achieve the same energy; $S(\lambda_c)$
contains at least two distinct points $u^{*,(1)}, u^{*,(2)}$ with
$\lVert u^{*,(1)} - u^{*,(2)} \rVert_{L^2} > 0$. **Any** selection $u^*(\lambda)$ that
agrees with the two-blob branch on one side of $\lambda_c$ and the
single-blob branch on the other has a discontinuity at $\lambda_c$. There
is no continuous global selection. $\square$

### Status.

**PROVED.** (1) and (2) by Berge; (3) by explicit construction from VP-1
counterexamples.

### Consequence.

Global $C^1$ regularity of $u^*(\lambda)$ on $\Delta^3$ is **REJECTED**.
The set of $\lambda$ at which a continuous selection fails to exist is
the **branch-switching locus** $\Sigma_{\mathrm{branch}}$ (registered as
OP-OMS-026). $\Sigma_{\mathrm{branch}}$ is generically a codim-1 surface in
$\Delta^3$ — these surfaces are exactly the **observer-type transition
surfaces** (basin boundaries of $V_D^0$, VP-4).

---

## §6. Proposition R4 — Value function is continuous and concave

### Statement.

The value function $v : \Delta^3 \to \mathbb{R}$,
$\lambda \mapsto \min_{u \in \Omega} E_\lambda(u)$, is

1. **continuous** on $\Delta^3$;
2. **concave** on $\Delta^3$;
3. (consequence of 2) **locally Lipschitz** on $\mathrm{int}(\Delta^3)$ and
   sub-differentiable everywhere with sub-differential
   $\partial v(\lambda) \supseteq \mathrm{conv}\{(E_1(u^*), \ldots, E_4(u^*)) : u^* \in S(\lambda)\}$.

### Proof.

**(1)** By Berge (R3 above), $v$ is continuous.

**(2)** For each fixed $u \in \Omega$, $L_u(\lambda) := E_\lambda(u) = \sum_i \lambda_i E_i(u)$
is linear, hence affine, in $\lambda$. The value function is the **pointwise
infimum** over $u$:

$$v(\lambda) = \inf_{u \in \Omega} L_u(\lambda).$$

The pointwise infimum of a family of affine functions is concave (e.g.\
Rockafellar, *Convex Analysis*, Thm 5.5). $\square$

**(3)** Concave functions on a convex open set in $\mathbb{R}^k$ are locally
Lipschitz on the interior (Rockafellar, Thm 10.4). The subdifferential
characterization follows from Danskin's theorem applied to the family
$\{L_u\}_{u \in S(\lambda)}$. $\square$

### Status.

**PROVED.** (1)–(3) follow from standard convex analysis applied to a
continuous, affine-parameterized family.

### Remark.

Concavity of $v$ is a **non-trivial structural fact**: the SCC value
function as a function of observer weights is concave, even though
$E_\lambda$ is non-convex in $u$ for any fixed $\lambda$. This is the
Lagrangian-duality side of the coin: maximizing concave duals
of non-convex primals.

---

## §7. Theorem R5 — Envelope theorem on the regular branch

### Statement.

If at $\lambda_0 \in \mathrm{int}(\Delta^3)$ the hypotheses of Theorem R1
(or R2 with fixed active set and strict complementarity) hold, and the
$C^1$ branch $u^*(\lambda)$ is the unique global minimum on a neighborhood
$U \ni \lambda_0$, then $v$ is $C^1$ on $U$ with

$$\boxed{\frac{\partial v}{\partial \lambda_i}(\lambda_0) = E_i\bigl(u^*(\lambda_0)\bigr).}$$

### Proof.

By R1/R2, $u^*$ is $C^1$ on $U$. Writing $v(\lambda) = E_\lambda(u^*(\lambda))$
and applying the chain rule:

$$\frac{\partial v}{\partial \lambda_i} = \underbrace{\frac{\partial E_\lambda}{\partial \lambda_i}}_{= E_i(u^*(\lambda))} + \underbrace{\nabla_u E_\lambda(u^*(\lambda))}_{= -\nu^*(\lambda) \mathbf{1} \text{ on } I_0; = 0 \text{ on tangent component}} \cdot \frac{\partial u^*}{\partial \lambda_i}.$$

The second term: by KKT first-order, $\nabla_u E_\lambda(u^*(\lambda)) + \nu^*(\lambda) \mathbf{1} \in N_\Omega(u^*(\lambda))$,
the normal cone to $\Omega$ at $u^*$. Differentiating the constraint
$\mathbf{1}^\top u^*(\lambda) = m$ in $\lambda$ gives
$\mathbf{1}^\top \frac{\partial u^*}{\partial \lambda_i} = 0$, so
$\nu^*(\lambda) \mathbf{1}^\top \frac{\partial u^*}{\partial \lambda_i} = 0$.
For sites in the active set $A^=_0 \cup A^=_n$ (R2 case),
$u^*(\lambda) = $ const on $U$, so $\frac{\partial u^*_i}{\partial \lambda_j} = 0$
on those sites. The remaining gradient component is in
$\ker(\mathbf{1}^\top)$, where the sum $\nabla_u E_\lambda(u^*(\lambda)) + \nu^*(\lambda) \mathbf{1}$
vanishes by $(\star)$ on $I_0$. So the second term is identically zero. $\square$

### Status.

**PROVED.** Standard envelope (Danskin) theorem applied to the regular
branch.

### Consequence.

$\nabla v(\lambda) = (E_{cl}(u^*), E_{sep}(u^*), E_{bd}(u^*), E_{tr}(u^*))$ on
the regular branch. The right-hand side is exactly the **energy decomposition**
already returned by `find_formation` in `result.energy_terms` — meaning
$\nabla v$ can be read off directly from the optimizer output, with no
finite differences. This is the analytic counterpart to the FD Jacobian in
VP-6.

---

## §8. Failure modes — exhaustive registry

| Mechanism | Where | Effect on $u^*(\lambda)$ |
|---|---|---|
| **Spinodal Hessian direction** | $H^\perp$ has a zero eigenvalue (inflection in concave-envelope sense) | $u^*$ may bifurcate; pitchfork or saddle-node |
| **Active-set change without strict complementarity** | $\mu^\pm_i = 0$ at active site | $u^*$ may exit / enter the boundary discontinuously |
| **Two separated local minima exchange dominance** | $\lambda \in \Sigma_{\mathrm{branch}}$ | $u^*$ jumps; selection discontinuous |
| **Phase transition (T8: $\beta/\alpha > 4\lambda_2/\lvert W''(c) \rvert$)** | scene-dependent threshold; here $\lambda_{cl}, \lambda_{bd}$ enter via the effective $\alpha, \beta$ | bifurcation surface in $\Delta^3$ |
| **OT singularity** | $\varepsilon_{OT} \to 0$ regime | not relevant here; we keep $\varepsilon_{OT}$ bounded away from 0 |

The first three are the dominant concerns inside $\mathrm{int}(\Delta^3)$.
The fourth is the canonical SCC phase transition translated to OMS coordinates.

---

## §9. Final classification of OP-OMS-018

| Sub-claim | Status |
|---|---|
| Local $C^1$ regularity at non-degenerate interior minimum (Theorem R1) | **PROVED** |
| Local piecewise $C^1$ regularity under fixed active set + strict complementarity (Theorem R2) | **PROVED** |
| Global continuity of $u^*$ as a function of $\lambda$ on $\Delta^3$ | **REJECTED** (Prop R3 (3) — VP-1/VP-4 counterexamples) |
| Global $C^1$ regularity of $u^*$ as a function of $\lambda$ on $\Delta^3$ | **REJECTED** |
| Continuity / concavity of value function $v(\lambda)$ on $\Delta^3$ | **PROVED** (R4) |
| Local Lipschitz, subdifferentiability of $v$ | **PROVED** (R4 (3)) |
| Envelope theorem on regular branches | **PROVED** (R5) |
| Characterization of the branch-switching locus $\Sigma_{\mathrm{branch}}$ | **OPEN** (OP-OMS-026) |

**Net OP-OMS-018 status: PARTIALLY RESOLVED.**

- **Local regularity is proved** under nondegeneracy / strict complementarity;
  this validates the Jacobian analysis of VP-6 within branch-clean
  neighborhoods.
- **Global regularity is rejected**; the discontinuities of $u^*$ are not
  numerical defects but the very phenomenon — observer-type transitions —
  that VP-1 and VP-4 detected empirically.
- **The value function $v$ is well-behaved** (continuous, concave,
  locally Lipschitz, subdifferentiable). $v$, not $u^*$, is the appropriate
  smooth object on all of $\Delta^3$.

---

## §10. Implications for OMS

### Inside the OMS framework.

1. The Jacobian $J_R(\lambda)$ used in VP-6 is **analytically defined** on
   regular branches (R1 / R2). On those branches, $J_R$ can be computed
   either by finite differences (VP-6, $h = 10^{-3}$) or analytically via
   the implicit-function formula in §3. The two should agree to FD error.
2. At the branch-switching locus $\Sigma_{\mathrm{branch}}$, $J_R$ is
   undefined. The VP-6 finite-difference experiment **detects** these
   surfaces by branch-id changes ($K_{\mathrm{core}}$, $n_{\mathrm{high}}$
   flip). They are not noise; they encode the perceptual structure.
3. The **basin stratification** of `basin_stratification.md` is a stratified
   smooth structure: smooth on each open branch domain, with codim-1
   gluing surfaces $\Sigma_{\mathrm{branch}}$.
4. The admissibility class $\mathcal{V}_{\mathrm{adm}}$ should be **revised** to allow
   stratified-smooth (rather than globally smooth) landscapes. The current
   V2 (continuity) and V3 (readout-compat) are still expected, but V4
   (basin-generating) and the implicit smoothness reading of V2 must
   accept piecewise-smooth landscapes. See the update to
   `observer_landscape_admissible_class.md` (Session 5 patch).
5. The OMS canonical theory is **not blocked** by the global $C^1$ failure
   of $u^*$ — provided we adopt the **value-function** / **stratified**
   reading. The value function $v(\lambda)$ is concave and continuous on all
   of $\Delta^3$; gradient flow of an admissible $V$ on $\Delta^3$ is
   well-posed in the projected sense (Prop SD1 + R4); the branch-switching
   locus is a stratification feature that the theory **predicts** rather
   than a regularity defect that the theory **fails to handle**.

### Outside the OMS framework.

1. T-Stability and basin claims of the main SCC theory are unaffected:
   they are statements at fixed $\lambda$.
2. The Jacobian-spectrum claim of `rg_relevance_flow.md` (Hyp RG1) becomes
   **branch-conditioned**: $d_{\mathrm{eff}}$ is a property of a regular
   branch, not of a single point on $\Delta^3$ in isolation.

---

## §11. Suggested next theoretical work

- **Explicit examples** where the bordered Hessian $M_0$ of R1 fails: these
  identify $\Sigma_{\mathrm{branch}}$ in the simplest path-graph cases.
- **Tangent-cone analysis at corners** of $\Omega$: when several box
  constraints are simultaneously active, R2 must be replaced by a directional
  derivative result (Mordukhovich).
- **Quantitative Lipschitz estimates** for $v(\lambda)$ via the explicit
  energy bounds — these would give a priori control on
  $\vert v(\lambda + h\xi) - v(\lambda)\vert \le L \lVert h\xi \rVert$ and constrain the
  geometry of basin level sets.

These are the concrete OPs to register: OP-OMS-027 (corner cases),
OP-OMS-028 (quantitative Lipschitz). Registered in `open_problems.md`
update.
