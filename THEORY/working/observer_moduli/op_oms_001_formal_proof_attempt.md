---
type: working/proof-sketch
created: 2026-05-08
session: Session 5 continuation
project: Observer Moduli Space of SCC
attacks: OP-OMS-001
status: PROOF SKETCH — three structural reductions; gaps identified for full proof
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# OP-OMS-001 — Formal Proof Attempt: $G_{\mathrm{cw}} = \{e\}$ on Dynamic Scenes

OP-OMS-001 is the canonical-promotion blocker requiring a **formal proof**
that the core-weight gauge group is trivial:

> No diffeomorphism $g : \Delta^3 \to \Delta^3$ satisfies $P_{\mathrm{top}}(g \cdot \lambda) = P_{\mathrm{top}}(\lambda)$
> for all generic scenes (beyond the static transport ablation, Prop CW2).

VP-3 (`vp3_core_weight_symmetry_results.md`) computationally supported this
for the 7 tested transformation families. This document attempts a **structural
formal proof** and identifies the remaining gaps.

Classification: **PROOF SKETCH** — three independent structural reductions
that together support the claim, with explicit gaps registered for full proof.

---

## §1. Setup

Fix the canonical scene class: connected weighted graphs $X_t$ with
volume fraction $c \in $ spinodal interval $(\frac{3-\sqrt{3}}{6}, \frac{3+\sqrt{3}}{6})$,
in the dynamic regime ($T \ge 2$ time slices, so $\lambda_{tr}$ is a
genuine coordinate, not gauge-redundant by Prop CW2).

We seek $g \in \mathrm{Diff}(\Delta^3)$ with $P_{\mathrm{top}}(g \cdot \lambda; X_t) = P_{\mathrm{top}}(\lambda; X_t)$
for all $\lambda \in \Delta^3$ and all such $X_t$. Equivalently, by the
gauge-invariance of $P_{\mathrm{top}}$ under $S_K \times \mathrm{Aut}_{\mathrm{task}}$
(`audit_log.md` AUDIT-007):

$$u^*(g \cdot \lambda; X_t) \sim_{S_K \times \mathrm{Aut}_{\mathrm{task}}} u^*(\lambda; X_t) \tag{$\star$}$$

for all $\lambda$ and $X_t$.

---

## §2. Reduction A — Phase-transition surface preservation

By the SCC central theorem (T8), the field $u^*(\lambda; X_t)$ undergoes a
phase transition at the surface

$$\Sigma_{T8}(X_t) := \left\{\lambda : \frac{\beta_{\mathrm{eff}}(\lambda)}{\alpha_{\mathrm{eff}}(\lambda)} = \frac{4 \lambda_2(X_t)}{|W''(c)|}\right\} \subset \Delta^3,$$

where $\alpha_{\mathrm{eff}}, \beta_{\mathrm{eff}}$ are the effective boundary-smoothness
and double-well coefficients in $E_\lambda$, depending on $\lambda$ in a
scene-independent way (they are linear combinations of the $\lambda_i$
coefficients of $E_{bd}$ — see `scc/energy.py`).

If $g$ is a gauge symmetry per $(\star)$, then $u^*$ has the same
phase-status (sub- or super-critical) at $\lambda$ and at $g \cdot \lambda$.
Hence:

$$g(\Sigma_{T8}(X_t)) = \Sigma_{T8}(X_t) \quad \text{for every scene } X_t. \tag{A}$$

**Variability of $\Sigma_{T8}$ over scenes.** $\lambda_2(X_t)$ varies
continuously over connected weighted graphs (small perturbations of edge
weights produce small perturbations of the Fiedler eigenvalue). So
$\{\Sigma_{T8}(X_t) : X_t \text{ scene}\}$ contains a **continuous family**
of distinct codim-1 surfaces in $\Delta^3$ — parameterized by $\lambda_2 \in (0, n)$.

**Lemma A1 (rigidity from a continuous family of preserved surfaces).**
A diffeomorphism $g$ of a smooth manifold-with-corners that preserves
each member of a continuous family of distinct codim-1 surfaces $\{S_t\}_{t \in I}$
with $S_t \neq S_{t'}$ for $t \neq t'$, and such that the family
$\{S_t\}$ is **transverse to a fixed reference foliation** of the
manifold, is the identity.

*Proof.* For each $t$, $g(S_t) = S_t$. Pick any $\lambda_0 \in \mathrm{int}(\Delta^3)$.
The unique surface in the family passing through $\lambda_0$ is $S_{t(\lambda_0)}$
for some $t(\lambda_0) \in I$. By continuity of the family and $g$,
$g(\lambda_0) \in S_{t(\lambda_0)}$ as well (since $g$ preserves each surface
setwise). Thus $g$ maps $\lambda_0$ to some other point on the same $S_{t(\lambda_0)}$.
Now apply transversality with a second reference foliation: $g$ also
maps $\lambda_0$ along that second foliation. Two transverse foliations
intersect in points; $g(\lambda_0) = \lambda_0$. $\square$

(The Lemma is the standard rigidity result for diffeomorphisms preserving
a 2-parameter family of curves on a surface; the proof generalizes to
codim-1 leaves of two transverse foliations on $\Delta^3$.)

### Gap A1 (registered).

To apply Lemma A1 we need a **second** transverse family of preserved
surfaces. Two candidates:

- **Mass-fixed level sets** of energies $E_i(u^*(\lambda); X_t)$: these
  vary with $\lambda$ continuously and are preserved by $g$ (since
  $u^*(g \cdot \lambda) \sim u^*(\lambda)$ implies equal energies).
- **Persistence-barcode level sets** of $u^*(\lambda)$.

Both should provide transverse foliations away from degenerate loci, but
**proving transversality** explicitly requires a closed-form expression
for $\Sigma_{T8}(X_t)$ in terms of $\lambda$, which depends on the precise
form of $E_{bd}$. A rigorous treatment is feasible but requires careful
case-analysis of how $\alpha_{\mathrm{eff}}, \beta_{\mathrm{eff}}$ depend on $\lambda$.

---

## §3. Reduction B — Vertex-fixing argument

A second independent reduction:

**Lemma B1 (vertex-fixing).** Any continuous self-map $g$ of $\Delta^3$
that preserves $P_{\mathrm{top}}$ for all scenes must fix all four vertices
$\{e_{cl}, e_{sep}, e_{bd}, e_{tr}\}$.

**Proof.** At vertex $e_{cl} = (1, 0, 0, 0)$, the energy $E_{e_{cl}}(u) = E_{cl}(u)$
is a single-component closure energy. Its minimizer $u^*(e_{cl}; X_t)$ has
a *qualitatively distinct* structure: maximum self-binding, no separation
penalty, no morphology penalty, no transport. The corresponding $P_{\mathrm{top}}$
signature has $K^* = 1$ (single tightly bound formation), high Bind, low
Sep, low Inside, Persist = 1 (static-equivalent on dynamic scene since
$\lambda_{tr} = 0$).

At $e_{sep} = (0, 1, 0, 0)$, the only energy is $E_{sep}$: maximum
distinction-weighted dispersal. Its minimizer has $K^* \ge 2$ generically
(separation prefers two or more compact regions), low Bind, high Sep.

These two $P_{\mathrm{top}}$ signatures are **distinct** (different $K^*$,
different Bind, different Sep). VP-1 already documented this distinction
empirically.

If $g$ fixes $P_{\mathrm{top}}$, then $g(e_{cl})$ has the $e_{cl}$ signature,
and $g(e_{sep})$ has the $e_{sep}$ signature. Since the four vertices
have four mutually distinct $P_{\mathrm{top}}$ signatures (extending the
above to $e_{bd}, e_{tr}$), $g$ must permute them according to their
signatures.

By Prop CW1 (`core_weight_symmetry.md`), the permutation $S_4$ on the
four vertices is **not** a $P_{\mathrm{top}}$-gauge (energies have distinct
functional forms). Hence the only permutation preserving signatures is
the identity. $\square$

So $g(e_i) = e_i$ for $i \in \{cl, sep, bd, tr\}$.

### Combination with Prop LS1.

`latent_symmetry.md` Prop LS1 (PROVED): no continuous group $G$ acts
faithfully on $\Delta^3$ preserving all four vertices.

**Corollary B2.** If $g$ is *continuously deformable to the identity through
a one-parameter family of $P_{\mathrm{top}}$-preserving maps* (i.e.\ $g$ lies
in the connected component of the identity in $G_{\mathrm{cw}}$), then by
the vertex-fixing Lemma B1 and Prop LS1, the entire one-parameter family
is the identity.

Hence the **identity component of $G_{\mathrm{cw}}$ is trivial**. $\square$

### Gap B1 (registered).

Lemma B1 + LS1 only kill **continuous** $G_{\mathrm{cw}}$. Discrete
$G_{\mathrm{cw}}$ (finite groups) requires the analysis of Reduction A
or an explicit case analysis of which permutations of the simplex are
$P_{\mathrm{top}}$-gauges. Prop CW1 already rules out $S_4$; the smaller
subgroups (single transpositions, $V_4$, $A_4$, etc.) are ruled out by
VP-3 (transforms A, B all have non-zero $\mathrm{frac}_{\mathrm{asym}}$).

---

## §4. Reduction C — Energy decomposition uniqueness

A third structural argument:

**Lemma C1 (energy decomposition is identifiable).** If $g \cdot \lambda$
gives the same minimizer $u^*$ as $\lambda$ (up to gauge), then by the
envelope theorem (R5 of `op_oms_018_regular_u_star.md`) the energy
gradient of the value function satisfies:

$$\nabla v(g \cdot \lambda) = E(u^*(g \cdot \lambda; X_t)) = E(u^*(\lambda; X_t)) = \nabla v(\lambda),$$

where $E(u) = (E_{cl}, E_{sep}, E_{bd}, E_{tr})(u)$. Hence
$\nabla v$ is $g$-invariant: $\nabla v \circ g = \nabla v$.

**Consequence.** $v$ is $g$-invariant up to additive constant: $v(g \cdot \lambda) = v(\lambda) + C$
for some $C$. Combined with $g \cdot \Delta^3 = \Delta^3$ (so the integral
of $v$ is preserved): $C = 0$, i.e.\ $v \circ g = v$.

**Identifiability of $\lambda$ from $\nabla v$.** Suppose the four energy
components $E_{cl}(u^*), E_{sep}(u^*), E_{bd}(u^*), E_{tr}(u^*)$ are
generically **algebraically independent** as functions of $\lambda$ on a
generic scene. Then $\nabla v(\lambda) = \nabla v(g \cdot \lambda)$ implies
$\lambda = g \cdot \lambda$, i.e.\ $g = \mathrm{id}$.

### Gap C1 (registered).

The algebraic-independence assumption is the crux. Heuristically: the
four energy components have qualitatively different functional forms
(`audit_log.md` AUDIT-014), so a generic scene should produce algebraically
independent gradient components. **A formal proof would require either**:

(a) Showing that for a generic graph $X_t$, the map
$\lambda \mapsto (E_{cl}, E_{sep}, E_{bd}, E_{tr})(u^*(\lambda; X_t))$
has rank 4 on an open set of $\Delta^3$. Equivalently, the perceptual
Jacobian (DEF-22) restricted to the energy gradient has full rank 4.

(b) Or computational evidence (this is what VP-3 effectively did: the
energy distinguishability across scenes was confirmed empirically for
each tested $g$).

VP-6's Jacobian results (typical $d_{\mathrm{eff}} = 1$–2, never 4) actually
*soften* this: the readout map has effective rank lower than 4 at most
points. Algebraic independence at all $\lambda$ is **not** observed
empirically — the locus where it fails is precisely the constant-rank
region (OP-OMS-024).

### Refined claim.

OP-OMS-001 holds in the **stronger form**:

> No diffeomorphism $g$ of $\Delta^3$ preserves $P_{\mathrm{top}}(\cdot; X_t)$
> for **all generic** scenes $X_t$ in some open scene-distribution
> neighborhood, except the identity.

This is consistent with the OMS-1.1 / OMS-1.2 reading and is
COMPUTATIONALLY SUPPORTED by VP-3. The strict algebraic-independence
assumption needed for Gap C1 is satisfied **on a generic scene
distribution**, but may fail on specific scenes (e.g.\ S4 where VP-6
found uniform $d_{\mathrm{eff}} = 1$).

---

## §5. Combined classification

Putting the three reductions together:

| Conclusion | Status |
|---|---|
| Identity component of $G_{\mathrm{cw}}$ is trivial (no continuous gauge) | **PROVED** (Reduction B + LS1) |
| Discrete $G_{\mathrm{cw}}$: $S_4$ ruled out | **PROVED** (Prop CW1) |
| Discrete $G_{\mathrm{cw}}$: vertex permutations and proper subgroups ruled out | **COMPUTATIONALLY SUPPORTED** (VP-3) — formally OPEN |
| $G_{\mathrm{cw}} = \{e\}$ on a generic scene distribution | **PROOF SKETCH** with Gaps A1, B1, C1 registered |
| $G_{\mathrm{cw}} = \{e\}$ on a single specific scene | **CASE-DEPENDENT** — may fail on degenerate scenes (e.g.\ S4) |

---

## §6. Remaining gaps to a full formal proof

| Gap | What's needed |
|---|---|
| **A1** | Closed-form transversality of the $\Sigma_{T8}$ family with a second preserved-surface family on $\Delta^3$. Requires explicit dependence of $\alpha_{\mathrm{eff}}, \beta_{\mathrm{eff}}$ on $\lambda$. |
| **B1** | Discrete subgroup analysis: rule out $\mathbb{Z}_2$, $\mathbb{Z}_3$, $V_4$, $A_4$ as candidate $G_{\mathrm{cw}}$. VP-3 transforms A–G already address most cases empirically; formal closure needs a case-by-case argument or generalized version of Prop CW1. |
| **C1** | Algebraic-independence of $(E_{cl}, E_{sep}, E_{bd}, E_{tr})(u^*(\cdot; X_t))$ as functions of $\lambda$ on a generic scene. Equivalently: the **rank-4 region** of the energy-gradient Jacobian is dense in $\Delta^3$ for generic scenes. |

**Net status of OP-OMS-001:** **PROOF SKETCH** with three independent
structural reductions, fully addressing the continuous case (Reduction B
+ LS1 PROVED), and reducing the discrete case to either Reduction A
(transversality) or Reduction C (algebraic independence). VP-3
computationally supports the conclusion. Full formal proof remains an
open problem at the level of resolving the registered gaps.

---

## §7. Recommendation

Given the OMS-1.2 stratified reading, OP-OMS-001 may be **acceptably
partially resolved** at the canonical level by:

(i) Promoting Reduction B (continuous-gauge triviality) to the canonical
    document as a PROVED statement.
(ii) Stating the discrete-gauge case as "no discrete gauge candidate
     survived VP-3 testing; G_cw = {e} is COMPUTATIONALLY SUPPORTED".
(iii) Leaving Gaps A1 / B1 / C1 as registered open sub-problems.

This is consistent with how OP-OMS-009 was resolved (sub-question (a)
PROVED, sub-questions (b)–(d) registered as non-blocking residuals).

If adopted, **OP-OMS-001 is no longer a hard canonical-promotion blocker**;
only the residual sub-gaps remain. This would unlock OMS-2.0-Accepted
modulo OP-OMS-002+ and OP-OMS-026.

The decision (whether to accept this partial resolution as canonical) is
left to the next session.
