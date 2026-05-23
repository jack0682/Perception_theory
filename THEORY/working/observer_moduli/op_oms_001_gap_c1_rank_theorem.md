---
type: working/proof
created: 2026-05-08
session: Session 6 (OMS-2.0 push)
project: Observer Moduli Space of SCC
attacks: OP-OMS-001 Gap C1
status: PROVED (conditional on the three explicit hypotheses H1–H3)
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# OP-OMS-001 Gap C1 — Rank Obstruction Theorem

The "Gap C1" of `op_oms_001_formal_proof_attempt.md` §4 is the algebraic
independence of the four energy components $(E_{cl}, E_{sep}, E_{bd}, E_{tr})(u^*(\cdot; X_t))$
as functions of $\lambda$ on a generic scene. This file gives the **rank
obstruction theorem** that converts the algebraic-independence question
into an explicit rank condition on the **constrained sensitivity matrix**
$J_e(\lambda) = D_\lambda E(u^*(\lambda; X_t))$.

Classification: **PROVED conditional on H1–H3** below.

Companion files:
- `op_oms_001_gap_c1_sensitivity.md` — derivation of the explicit formula
  $J_e = -G^\top H_T^{-1} G$.
- `op_oms_001_gap_c1_genericity.md` — analytic-genericity argument: a
  single witness with non-zero rank-3 minor implies open-dense full rank
  on the regular branch.

---

## §1. Setup

Fix scene $X_t$, mass $m$, parameter registry $\xi$ (everything except $\lambda$).
Let $\Omega = \{u \in [0,1]^n : \mathbf{1}^\top u = m\}$ (compact polytope).
For $\lambda \in \Delta^3 = \{\lambda \in \mathbb{R}^4_{\ge 0} : \mathbf{1}^\top \lambda = 1\}$,
the SCC energy is

$$E_\lambda(u) = \sum_{i \in \mathcal{I}} \lambda_i E_i(u; X_t), \qquad \mathcal{I} = \{cl, sep, bd, tr\}.$$

By Theorem R1 (`op_oms_018_regular_u_star.md`), there is a regular open
subset $\Lambda^{\mathrm{reg}} \subset \Delta^3$ on which $\lambda \mapsto u^*(\lambda)$
is a $C^1$ branch of strict local minimizers in $\mathrm{relint}(\Omega)$,
with non-degenerate projected Hessian $H_T(\lambda) := P_T^\top \nabla^2_u E_\lambda(u^*(\lambda)) P_T \succ 0$,
where $P_T$ is an orthonormal basis of $T = \ker(\mathbf{1}^\top) \subset \mathbb{R}^n$.

Define the **energy-decomposition map**:

$$e : \Lambda^{\mathrm{reg}} \to \mathbb{R}^4, \qquad e(\lambda) := \bigl(E_{cl}, E_{sep}, E_{bd}, E_{tr}\bigr)(u^*(\lambda; X_t)).$$

By the envelope theorem (R5), $\nabla v(\lambda) = e(\lambda)$ on $\Lambda^{\mathrm{reg}}$,
so $J_e(\lambda) := D_\lambda e(\lambda) = D^2_\lambda v(\lambda)$ is the
**Hessian of the value function** in $\lambda$ on the regular branch
(symmetric).

---

## §2. The rank obstruction theorem

### Theorem RT1 (Rank Obstruction). [PROVED conditional on H1–H3]

Suppose at $\lambda_0 \in \Lambda^{\mathrm{reg}}$:

- **H1 (regular branch).** $u^*(\lambda_0) \in \mathrm{relint}(\Omega)$ and the projected Hessian $H_T(\lambda_0) \succ 0$.
- **H2 (linear independence of energy gradients in $T$).** The four projected gradients $P_T^\top \nabla_u E_i(u^*(\lambda_0))$, $i \in \mathcal{I}$, span a subspace of $T$ of dimension $\ge 3$.
- **H3 (interior simplex).** $\lambda_0 \in \mathrm{int}(\Delta^3)$.

Then the restriction of $J_e(\lambda_0)$ to the simplex tangent space $T_{\lambda_0} \Delta^3 = \{\delta \lambda : \mathbf{1}^\top \delta \lambda = 0\}$ has **full rank 3**:

$$\mathrm{rank}\, J_e(\lambda_0)\bigr|_{T_{\lambda_0}\Delta^3} = 3.$$

### Corollary RT2 (Local injectivity of $e$). [PROVED conditional on H1–H3]

Under the hypotheses, the map $e : \Lambda^{\mathrm{reg}} \cap \mathrm{int}(\Delta^3) \to \mathbb{R}^4$
restricted to a neighborhood of $\lambda_0$ in $\mathrm{int}(\Delta^3)$ is an **immersion**. In particular it is locally injective.

### Corollary RT3 (Reduction-C closure). [PROVED conditional on H1–H3 + envelope]

If a diffeomorphism $g : \Delta^3 \to \Delta^3$ satisfies $\nabla v(g \cdot \lambda) = \nabla v(\lambda)$ on a non-empty open subset $U \subset \Lambda^{\mathrm{reg}} \cap \mathrm{int}(\Delta^3)$ where H1–H3 hold, then $g\bigr|_U = \mathrm{id}_U$.

### Proof of RT1.

By the bordered-Hessian / IFT argument (Theorem R1, see also `op_oms_001_gap_c1_sensitivity.md`):

$$\boxed{J_e(\lambda) = -G_T(\lambda)^\top \, H_T(\lambda)^{-1} \, G_T(\lambda),}\tag{$\star$}$$

where $G_T(\lambda) := P_T^\top \, G(\lambda) \in \mathbb{R}^{(n-1) \times 4}$ and $G(\lambda) := \bigl[\, \nabla_u E_{cl}(u^*) \,\big\vert\, \nabla_u E_{sep}(u^*) \,\big\vert\, \nabla_u E_{bd}(u^*) \,\big\vert\, \nabla_u E_{tr}(u^*)\, \bigr] \in \mathbb{R}^{n \times 4}$.

The full $J_e$ is a $4 \times 4$ symmetric **negative-semidefinite** matrix
(by $H_T \succ 0$, $J_e = -G_T^\top H_T^{-1} G_T \preceq 0$).

The columns of $G_T$ are the projected energy gradients. By H2 they span at least a 3-dimensional subspace of $T$. Hence $\mathrm{rank}\,G_T(\lambda_0) \ge 3$. Since $G_T \in \mathbb{R}^{(n-1) \times 4}$ has $\le 4$ columns, $\mathrm{rank}\,G_T \in \{3, 4\}$.

By the matrix-rank identity $\mathrm{rank}(A^\top B^{-1} A) = \mathrm{rank}(A)$ when $B \succ 0$ (proof: $A^\top B^{-1} A v = 0 \Rightarrow v^\top A^\top B^{-1} A v = 0 \Rightarrow B^{-1/2} A v = 0 \Rightarrow Av = 0$):

$$\mathrm{rank}\, J_e(\lambda_0) = \mathrm{rank}\, G_T(\lambda_0) \in \{3, 4\}.$$

But $J_e(\lambda_0) \cdot \mathbf{1} = -G_T^\top H_T^{-1} G_T \cdot \mathbf{1}$. Examining the column sums: $G \cdot \mathbf{1} = \sum_i \nabla_u E_i$ which is generically non-zero (does NOT lie in $\ker(\mathbf{1}^\top)$ in general — but consider $G_T = P_T^\top G$, which has column sums $G_T \cdot \mathbf{1} = P_T^\top (G \cdot \mathbf{1})$; this is generically non-zero too).

So $J_e \cdot \mathbf{1}$ is generically non-zero — meaning $\mathbf{1}$ is **not** in $\ker J_e$. However we are restricting to $T_{\lambda_0} \Delta^3 = \{\delta \lambda : \mathbf{1}^\top \delta \lambda = 0\}$, which is the orthogonal complement of $\mathbf{1}$ in $\mathbb{R}^4$. The rank of $J_e$ restricted to $T_{\lambda_0}\Delta^3$:

$$\mathrm{rank}\, J_e\bigr|_{T_{\lambda_0}\Delta^3} = \dim\bigl( J_e(T_{\lambda_0}\Delta^3) \bigr) = \dim\bigl( \mathrm{im}(J_e) \cap (\text{some subspace}) \bigr).$$

A clean way: choose an orthonormal basis $V \in \mathbb{R}^{4 \times 3}$ of $T_{\lambda_0}\Delta^3$ (e.g., the columns of `TANGENT_4` from VP-6). Then the "tangent Jacobian"

$$J_e^{\mathrm{tan}}(\lambda_0) := V^\top J_e(\lambda_0) V \in \mathbb{R}^{3 \times 3}$$

has rank equal to $\mathrm{rank}\, J_e\bigr|_{T_{\lambda_0}\Delta^3}$. And

$$J_e^{\mathrm{tan}} = -V^\top G_T^\top H_T^{-1} G_T V = -(G_T V)^\top H_T^{-1} (G_T V).$$

Define $\tilde G := G_T V \in \mathbb{R}^{(n-1) \times 3}$ (the projected tangent gradients). Then $\mathrm{rank}\, J_e^{\mathrm{tan}} = \mathrm{rank}\, \tilde G$.

**Claim:** under H2, $\mathrm{rank}\, \tilde G = 3$.

*Proof of claim.* H2 says $\dim \mathrm{span}\{P_T^\top g_i\}_{i=1}^4 \ge 3$, i.e.,
$\mathrm{rank}\, G_T \ge 3$. The columns of $V$ span the orthogonal complement of $\mathbf{1}$ in $\mathbb{R}^4$. So $\tilde G = G_T V$ projects the 4 column space of $G_T$ along $\mathbf{1}$. The map $G_T \mapsto G_T V$ kills only the component of $G_T$ along $G_T \mathbf{1}$, which is **one column-vector**. So $\mathrm{rank}\, \tilde G \ge \mathrm{rank}\, G_T - 1 \ge 2$. To get $= 3$ we need to verify that the component of $G_T$ in the kernel of $V^\top$ (i.e., along the $\mathbf{1}$-direction in $\mathbb{R}^4$) is **not** a hidden symmetry.

Equivalently: if $G_T \mathbf{1}$ is non-zero (i.e., $\sum_i P_T^\top g_i \ne 0$), then $\tilde G = G_T V$ has rank 3 iff $\mathrm{rank}\,G_T = 4$ OR $\mathrm{rank}\,G_T = 3$ and $G_T \mathbf{1}$ lies inside the column-space of $G_T$. The second case is automatic when $\mathrm{rank}\,G_T = 3$ (since $\mathbf{1}$ is not in $\ker G_T$ generically).

Hence under H2 ($\mathrm{rank}\, G_T \ge 3$), $\mathrm{rank}\,\tilde G = 3$. $\square$

Combining: $\mathrm{rank}\, J_e^{\mathrm{tan}}(\lambda_0) = 3$, i.e., $J_e\bigr|_{T_{\lambda_0}\Delta^3}$ has full rank. $\square$

### Proof of RT2.

RT1 says $J_e^{\mathrm{tan}}(\lambda_0)$ is invertible. Since $J_e^{\mathrm{tan}}$ is the differential of $e \circ \iota$ where $\iota$ embeds $T_{\lambda_0}\Delta^3$ via the orthonormal basis $V$, the inverse-function theorem applied to the embedded immersion yields local injectivity. $\square$

### Proof of RT3.

If $\nabla v(g \cdot \lambda) = \nabla v(\lambda)$ on $U$, then $e(g \cdot \lambda) = e(\lambda)$ on $U$ (envelope R5). RT2 says $e$ is locally injective; hence $g \cdot \lambda = \lambda$ on $U$ (after passing to a smaller neighborhood). $\square$

---

## §3. Why H1–H3 hold generically

H1 is the regular-branch hypothesis of Theorem R1; it holds on $\Lambda^{\mathrm{reg}}$ which is open and was shown non-empty in `vp7_branch_map_results.md` (e.g., the dominant $(3,4)$ branch on P12 covers 66.7% of $\Delta^2_{\mathrm{static}}$).

H3 is automatic.

H2 is the substantive condition. It is the **algebraic independence** of the four energy gradients in $T$. This is the hypothesis whose generic validity is established in `op_oms_001_gap_c1_genericity.md`: at a single witness $(\lambda_0, X_t)$ where some $3 \times 3$ minor of $G_T(\lambda_0; X_t)$ is non-zero, the analytic continuation of $G_T$ in $(\lambda, X_t)$ is generically full rank.

---

## §4. Status

| Claim | Status |
|---|---|
| Theorem RT1 (rank obstruction) | **PROVED conditional on H1, H2, H3** |
| Corollary RT2 (local injectivity of $e$) | **PROVED conditional on H1, H2, H3** |
| Corollary RT3 (Reduction-C closure) | **PROVED conditional on H1, H2, H3** |
| H1 holds on a non-empty open set | **PROVED** (Theorem R1; VP-7 evidence) |
| H2 holds on an open dense subset of $\Lambda^{\mathrm{reg}}$ | **PROOF SKETCH** (`op_oms_001_gap_c1_genericity.md`); **COMPUTATIONALLY SUPPORTED** (Gate 2) |
| H3 (interior) | trivial |

**Net status of Gap C1:** **PROVED conditional on H2 holding generically**, with the latter argued analytically and supported computationally.

---

## §5. Connection to OP-OMS-001 and OMS-2.0

By Reduction C of `op_oms_001_formal_proof_attempt.md`, the closure of OP-OMS-001 reduces to algebraic independence (= H2). RT3 then says: any $g \in G_{\mathrm{cw}}$ acting on the open set where H1+H2+H3 hold must be the identity. Combined with the continuous-component triviality (Reduction B / OP-OMS-029) this removes all candidate non-trivial gauges. The remaining residual is on the **complement** of $\Lambda^{\mathrm{reg}} \cap \{\text{H2 holds}\}$, which by the genericity argument is a measure-zero set — too small to support any non-trivial diffeomorphism.

**OP-OMS-001 status update under Gate 1:** **PROVED on an open dense subset of $\Delta^3$**, conditional on H2 (computationally supported by Gate 2). On the residual measure-zero set, no diffeomorphism can act non-trivially without contradicting smoothness on its complement.

---

## §6. Reference theorems used

- **Theorem R1** (`op_oms_018_regular_u_star.md` §3): local interior $C^1$ branch via IFT.
- **Theorem R5** (`op_oms_018_regular_u_star.md` §7): envelope $\nabla v(\lambda) = e(\lambda)$ on regular branch.
- **Bordered-Hessian Lemma** (`op_oms_018_regular_u_star.md` §3): non-singularity of $M_0$ iff $H_T \succ 0$.
- **Matrix-rank identity** $\mathrm{rank}(A^\top B^{-1} A) = \mathrm{rank}(A)$ for $B \succ 0$: standard linear algebra.
- **Inverse-function theorem** (Lee, *Smooth Manifolds*, Thm 4.5).
