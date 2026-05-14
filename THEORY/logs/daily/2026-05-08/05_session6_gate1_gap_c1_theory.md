---
type: log/daily
date: 2026-05-08
session: Session 6 (OMS-2.0 push) — Gate 1
attacks: OP-OMS-001 Gap C1
deliverables: op_oms_001_gap_c1_rank_theorem.md, _sensitivity.md, _genericity.md
---

> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]


# Session 6 Gate 1 — OP-OMS-001 Gap C1 Theory (Three Files)

## Mission

Close OP-OMS-001 Gap C1 (algebraic independence of energy gradients) at
the **theorem + witness** level. Three theory files were mandated.

## Files produced

### 1. `op_oms_001_gap_c1_rank_theorem.md` — Rank Obstruction

**Theorem RT1 (Rank Obstruction).** Under hypotheses
- H1: regular branch ($u^* \in \mathrm{relint}(\Omega)$, $H_T \succ 0$);
- H2: energy gradients span $\ge 3$-dim subspace of $T$;
- H3: interior simplex,

we have $\mathrm{rank}\, J_e(\lambda_0)\bigr|_{T_{\lambda_0}\Delta^3} = 3$.

**Corollary RT2.** $e : \Lambda^{\mathrm{reg}} \to \mathbb{R}^4$ is locally an immersion.

**Corollary RT3 (Reduction-C closure).** Any $g \in G_{\mathrm{cw}}$ with $\nabla v(g \cdot \lambda) = \nabla v(\lambda)$ on an open subset where H1–H3 hold is the identity there.

Proof structure:
- Bordered-Hessian non-singularity + matrix rank identity $\mathrm{rank}(A^\top B^{-1} A) = \mathrm{rank}(A)$ for $B \succ 0$.
- Tangent restriction via orthonormal $V \in \mathbb{R}^{4 \times 3}$.

### 2. `op_oms_001_gap_c1_sensitivity.md` — Sensitivity Formula

**Theorem S1 (Interior sensitivity).** On the regular branch,

$$\boxed{J_e(\lambda) = -G_T(\lambda)^\top H_T(\lambda)^{-1} G_T(\lambda) \in \mathbb{R}^{4 \times 4}}$$

with $G$ the energy-gradient matrix and $H_T$ the projected Hessian.

Proof: bordered IFT. $D_{(u,\nu)} F(u^*, \nu_0, \lambda_0)$ invertible by hypothesis; $D_\lambda F = (G^\top, 0)^\top$. Solving the bordered system yields $\partial u^* / \partial \lambda_j = -P_T H_T^{-1} P_T^\top g_j$. Then $\partial E_i(u^*) / \partial \lambda_j = g_i^\top \partial u^*/\partial \lambda_j = -[G_T^\top H_T^{-1} G_T]_{i,j}$.

**Theorem S2 (Active-set sensitivity).** Same form but projected to inactive subspace under LICQ + strict complementarity + 2nd-order sufficiency.

**Properties of $J_e$:**
- Symmetric, **negative semi-definite**.
- $\mathrm{rank}\, J_e = \mathrm{rank}\, G_T$.
- $J_e = D^2_\lambda v$ (Hessian of value function), consistent with $v$ concave (R4).

### 3. `op_oms_001_gap_c1_genericity.md` — Analytic Genericity

**Lemma G1 (analyticity of $E_i$):** $E_{cl}, E_{sep}, E_{bd}$ are real-analytic in $u$ (resolvent / polynomial / polynomial respectively).

**Lemma G2:** $u^*$ is real-analytic on $\Lambda^{\mathrm{reg}}$ (analytic IFT).

**Corollary G3:** $G_T$ is real-analytic in $(\lambda, X_t)$.

**Theorem G4 (Analytic dichotomy).** A real-analytic function on a connected real-analytic manifold is either identically zero or the zero locus is closed nowhere-dense (Krantz–Parks).

**Corollary G5 (Witness ⇒ open dense rank-3).** If at one $\lambda^\star \in \Lambda^{\mathrm{reg}}$ some 3×3 minor of $G_T$ is non-zero, then the rank-3 set is open dense.

**Theorem G7 (Generic-scene H2).** Under H4 (one witness exists across $(\lambda, X_t)$), H2 of RT1 holds on an open dense subset of regular pairs.

**Corollary G8 (Density extension).** A continuous $g$ that equals identity on a dense subset is identity everywhere.

**Theorem GAP-C1.** Under H4, the only diffeomorphism preserving $P_{\mathrm{top}}$ is the identity, modulo a closed nowhere-dense set extended to all of $\Delta^3$ by G8.

## Net status of Gap C1

**PROVED conditional on H4** (the existence-of-witness hypothesis). H4
itself is the target of Gate 2 (VP-8).

This converts the OP-OMS-001 closure into a **single computational
witness check** — a classical analytic-genericity argument: one
non-vanishing minor establishes generic non-vanishing on the connected
real-analytic moduli space.

## Connection to OMS-2.0

- Combined with Reduction B (continuous-component triviality, OP-OMS-029
  PROVED Session 5 cont.) and Prop CW1 ($S_4$ rejected) and VP-3
  elimination of all 7 transformation families, the only remaining case
  is finite discrete subgroups not addressed by VP-3.
- Theorem GAP-C1 + G8 (continuity to identity from dense set) closes
  this remaining case modulo H4.

OP-OMS-001 reads as **PROVED conditional on H4**. With H4 confirmed in
Gate 2, OP-OMS-001 is **PROVED at the conditional level** for OMS-2.0.
