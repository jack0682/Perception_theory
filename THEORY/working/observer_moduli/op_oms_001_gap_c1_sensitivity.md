---
type: working/proof
created: 2026-05-08
session: Session 6 (OMS-2.0 push)
project: Observer Moduli Space of SCC
attacks: OP-OMS-001 Gap C1
status: PROVED — explicit sensitivity formula
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# OP-OMS-001 Gap C1 — Sensitivity Formula

Derives the explicit formula $J_e(\lambda) = -G_T(\lambda)^\top H_T(\lambda)^{-1} G_T(\lambda)$
used in `op_oms_001_gap_c1_rank_theorem.md`. Includes the active-set
correction.

Classification: **PROVED** for the interior case; **PROVED** for the
fixed-active-set case under strict complementarity.

---

## §1. Notation

- $\Omega = \Sigma_m \cap [0,1]^n = \{u \in [0,1]^n : \mathbf{1}^\top u = m\}$.
- $T = \ker(\mathbf{1}^\top) \subset \mathbb{R}^n$, of dimension $n - 1$.
- $P_T \in \mathbb{R}^{n \times (n-1)}$ orthonormal columns spanning $T$ (e.g.\ Householder of $\mathbf{1}$).
- For each $i \in \mathcal{I} = \{cl, sep, bd, tr\}$: $g_i(u) = \nabla_u E_i(u) \in \mathbb{R}^n$.
- $G(u) = [g_{cl}\,|\,g_{sep}\,|\,g_{bd}\,|\,g_{tr}](u) \in \mathbb{R}^{n \times 4}$.
- $G_T(u) = P_T^\top G(u) \in \mathbb{R}^{(n-1) \times 4}$.
- $H(u; \lambda) = \nabla^2_u E_\lambda(u) = \sum_i \lambda_i \, \nabla^2_u E_i(u) \in \mathbb{R}^{n \times n}$ symmetric.
- $H_T(u; \lambda) = P_T^\top H(u; \lambda) P_T \in \mathbb{R}^{(n-1) \times (n-1)}$ symmetric, the projected Hessian.
- $u^*(\lambda) \in \Omega$: an interior local minimizer (R1 hypothesis).
- $\nu^*(\lambda) \in \mathbb{R}$: the Lagrange multiplier for $\mathbf{1}^\top u = m$.
- $e(\lambda) := E(u^*(\lambda)) := \bigl(E_{cl}, E_{sep}, E_{bd}, E_{tr}\bigr)(u^*(\lambda)) \in \mathbb{R}^4$.

---

## §2. Sensitivity formula — interior case

### Theorem S1 (Interior sensitivity). [PROVED]

Suppose $u^*(\lambda_0) \in \mathrm{relint}(\Omega)$ with first-order condition
$\nabla_u E_{\lambda_0}(u^*) + \nu_0 \mathbf{1} = 0$ and $H_T(u^*; \lambda_0) \succ 0$.
Then:

(a) $u^*(\lambda)$ is $C^1$ on a neighborhood $U \ni \lambda_0$, with **sensitivity matrix**

$$\frac{\partial u^*}{\partial \lambda_j}(\lambda_0) = -P_T \, H_T^{-1} \, G_T(u^*)\, e_j \qquad \text{for } j \in \mathcal{I},$$

where $e_j$ is the $j$-th standard basis vector. Stacking columns:

$$D_\lambda u^*(\lambda_0) = -P_T \, H_T^{-1} \, G_T(u^*) \in \mathbb{R}^{n \times 4}.$$

(b) The energy-decomposition Jacobian is

$$\boxed{J_e(\lambda_0) := D_\lambda e(\lambda_0) = -G_T(u^*)^\top H_T^{-1} G_T(u^*) \in \mathbb{R}^{4 \times 4}.}$$

In particular $J_e$ is symmetric and **negative semi-definite** (equivalently, $-J_e$ is positive semi-definite).

(c) $J_e = D^2_\lambda v(\lambda_0)$, the Hessian of the value function. (Consistent with $v$ concave, R4.)

### Proof.

(a) Define $F : \mathbb{R}^n \times \mathbb{R} \times \Delta^3 \to \mathbb{R}^{n+1}$:

$$F(u, \nu, \lambda) := \begin{pmatrix} \nabla_u E_\lambda(u) + \nu \mathbf{1} \\ \mathbf{1}^\top u - m \end{pmatrix}.$$

We have $F(u^*, \nu_0, \lambda_0) = 0$. Compute partial derivatives:

$$D_{(u, \nu)} F = \begin{pmatrix} H(u; \lambda) & \mathbf{1} \\ \mathbf{1}^\top & 0 \end{pmatrix} =: M(u; \lambda).$$

$$D_\lambda F(u, \nu, \lambda) = \begin{pmatrix} \frac{\partial}{\partial \lambda_j}\nabla_u E_\lambda(u) \\ 0 \end{pmatrix}_{j} = \begin{pmatrix} G(u) \\ \mathbf{0} \end{pmatrix} \in \mathbb{R}^{(n+1) \times 4}.$$

By the bordered-Hessian lemma (`op_oms_018_regular_u_star.md` §3) and $H_T(u^*; \lambda_0) \succ 0$, $M(u^*; \lambda_0)$ is non-singular. By the IFT,

$$D_\lambda \begin{pmatrix} u^* \\ \nu^* \end{pmatrix}(\lambda_0) = -M(u^*; \lambda_0)^{-1} \begin{pmatrix} G(u^*) \\ \mathbf{0} \end{pmatrix}.$$

Now solve the bordered system column by column. Fix $j$ and set $\delta u = \partial u^* / \partial \lambda_j$, $\delta \nu = \partial \nu^* / \partial \lambda_j$, $g_j = G(u^*) e_j$. The system

$$\begin{cases} H \, \delta u + \delta \nu \, \mathbf{1} = -g_j \\ \mathbf{1}^\top \delta u = 0 \end{cases}$$

means $\delta u \in T = \ker(\mathbf{1}^\top)$. Project the first equation by $P_T^\top$:

$$P_T^\top H \delta u + \delta \nu \, P_T^\top \mathbf{1} = -P_T^\top g_j.$$

Since $P_T^\top \mathbf{1} = 0$ (columns of $P_T$ orthogonal to $\mathbf{1}$),

$$P_T^\top H \, \delta u = -P_T^\top g_j.$$

Write $\delta u = P_T \alpha$ for $\alpha \in \mathbb{R}^{n-1}$. Then $P_T^\top H P_T \alpha = -P_T^\top g_j$, i.e., $H_T \alpha = -P_T^\top g_j$, so $\alpha = -H_T^{-1} P_T^\top g_j$. Therefore

$$\delta u = P_T \alpha = -P_T H_T^{-1} P_T^\top g_j.$$

Equivalently $D_\lambda u^*(\lambda_0) = -P_T H_T^{-1} G_T$ where $G_T = P_T^\top G$. This is (a).

(b) Compute $J_e = D_\lambda e(\lambda_0)$ entry-wise:

$$\bigl[J_e\bigr]_{i,j} = \frac{\partial}{\partial \lambda_j} E_i(u^*(\lambda)) = \nabla_u E_i(u^*)^\top \frac{\partial u^*}{\partial \lambda_j} = g_i^\top \bigl( -P_T H_T^{-1} P_T^\top g_j \bigr).$$

Since $P_T H_T^{-1} P_T^\top$ is symmetric (it's the pseudo-inverse of $H$ on $T$ extended by zero on $\mathbf{1}$):

$$\bigl[J_e\bigr]_{i,j} = -g_i^\top P_T H_T^{-1} P_T^\top g_j = -(P_T^\top g_i)^\top H_T^{-1} (P_T^\top g_j) = -\bigl[G_T^\top H_T^{-1} G_T\bigr]_{i,j}.$$

So $J_e = -G_T^\top H_T^{-1} G_T$. Symmetry is manifest. Negative semi-definiteness: for any $w \in \mathbb{R}^4$,

$$w^\top J_e w = -(G_T w)^\top H_T^{-1} (G_T w) \le 0$$

since $H_T \succ 0 \Rightarrow H_T^{-1} \succ 0$. Equality iff $G_T w = 0$. So $\ker J_e = \ker G_T$, which combined with $\mathrm{rank}\,J_e = \mathrm{rank}\,G_T$ (a standard rank identity).

(c) By Theorem R5 (envelope), $\nabla v(\lambda) = e(\lambda)$ on $\Lambda^{\mathrm{reg}}$. So $J_e = D_\lambda \nabla v = D^2_\lambda v$, i.e., $J_e$ is the (symmetric) Hessian of $v$ on the regular branch. Negative semi-definiteness reproduces concavity (R4). $\square$

---

## §3. Sensitivity formula — fixed active set

### Theorem S2 (Active-set sensitivity). [PROVED]

Suppose $u^*(\lambda_0) \in \Omega$ has active sets $A^=_0(\lambda_0), A^=_n(\lambda_0)$
(box constraints $u_i = 0$ or $u_i = 1$), and the hypotheses of R2 hold:
LICQ + strict complementarity + second-order sufficiency. Let
$I_0 = \mathcal{N} \setminus (A^=_0 \cup A^=_n)$ be the inactive index set.

Then there is a neighborhood $U \ni \lambda_0$ on which $A^=_0, A^=_n$
are constant, and:

(a) The sensitivity matrix on the **inactive sub-space** $T^{I_0} = \{\delta u \in T : \delta u_i = 0\ \forall i \in A^=_0 \cup A^=_n\}$ is

$$\frac{\partial u^*}{\partial \lambda_j}\bigg\vert_{I_0}(\lambda_0) = -P_{T^{I_0}}\, H_{T^{I_0}}^{-1}\, G_{T^{I_0}}\, e_j,$$

where $H_{T^{I_0}}$ is the Hessian projected onto $T^{I_0}$ and $G_{T^{I_0}}$ are the energy gradients restricted to $I_0$ and projected.

On the active sites, $\partial u^* / \partial \lambda_j = 0$.

(b) $J_e(\lambda_0) = -G_{T^{I_0}}^\top H_{T^{I_0}}^{-1} G_{T^{I_0}}$ — same form, just with the smaller projector.

### Proof.

Identical to S1 with $T$ replaced by $T^{I_0}$ throughout. The active-set
constraint $u^*_i = $ const for $i \in A^=_0 \cup A^=_n$ implies $\partial u^*_i / \partial \lambda_j = 0$ on those sites, which is precisely the projection onto $T^{I_0}$. LICQ + strict complementarity ensure the active set is locally constant; second-order sufficiency ensures $H_{T^{I_0}} \succ 0$. $\square$

---

## §4. Numerical / FD form

For computational verification (Gate 2 / VP-8), the formula is implemented as:

```
G[:, i]   = energy_grad_i(u_star, graph, params)   for i in {cl, sep, bd, tr}
P_T       = orthonormal basis of T  (n × (n-1))    e.g. Householder of 1
G_T       = P_T.T @ G                              # ((n-1) × 4)
H_T       = P_T.T @ Hessian @ P_T                  # via FD if needed
J_e       = - G_T.T @ inv(H_T) @ G_T               # 4 × 4
J_e_tan   = V.T @ J_e @ V                          # 3 × 3 simplex tangent
rank      = numpy.linalg.matrix_rank(J_e_tan, tol=1e-8)
sigma     = numpy.linalg.svd(J_e_tan, compute_uv=False)
```

VP-8 implements both (i) a closed-form $G$ via `grad_cl/grad_sep/grad_bd`
from `scc/energy.py` and (ii) a finite-difference $H_T$. FD step
$h = 10^{-4}$. The result is compared against the empirical $J_e$
obtained by a $4 \times 4$ finite-difference of $e(\lambda)$.

---

## §5. Status

| Claim | Status |
|---|---|
| Theorem S1 (interior sensitivity, $J_e = -G_T^\top H_T^{-1} G_T$) | **PROVED** |
| Theorem S2 (active-set sensitivity, projected to $T^{I_0}$) | **PROVED** |
| $J_e$ is symmetric, negative semi-definite, equals $D^2_\lambda v$ | **PROVED** |
| $\ker J_e = \ker G_T$ | **PROVED** |
| Numerical FD form usable for VP-8 verification | **DEFINED** |
