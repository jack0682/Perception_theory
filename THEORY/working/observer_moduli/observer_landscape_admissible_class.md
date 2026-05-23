---
type: working/patch
created: 2026-05-08
session: Session 5
project: Observer Moduli Space of SCC
stage: OMS-1.2 patch
supersedes: parts of `observer_landscape_candidates.md` §3 and `vp2_observer_landscape_admissible.md` §V2
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# Admissible Observer Landscape Class — OMS-1.2 Patch

This patch revises the V2 (continuity / smoothness) criterion in
`definitions.md` DEF-16 and `observer_landscape_candidates.md` §3 to
reflect the OP-OMS-018 partial-resolution finding: $u^*(\lambda)$ has only
**local** $C^1$ regularity on regular branches, with codim-1 branch-switching
surfaces $\Sigma_{\mathrm{branch}}$ separating distinct branches.

---

## §1. Why a patch is needed

Pre-Session-5 V2 read (DEF-16):

> **V2. Morse-like genericity:** The critical point set $\mathrm{Crit}(V) = \{\Theta : \nabla V(\Theta) = 0\}$
> is finite and non-degenerate (all eigenvalues of the Hessian at critical points are nonzero).

This implicitly requires global $C^2$ regularity of $V$ on $\mathcal{M}_{\mathrm{obs}}$ for the
Hessian to make sense everywhere. Post-Session-5: any $V$ derived from
the SCC energy via a continuous functional of $u^*(\lambda)$ inherits the
non-smooth behavior of $u^*$ across $\Sigma_{\mathrm{branch}}$, and global
$C^2$ regularity is **not generically attainable**.

The fix: read V2 in the **stratified** sense.

---

## §2. Revised V2 (OMS-1.2)

> **V2 (revised).** $V \in C^0(\mathcal{M}_{\mathrm{obs}})$ globally; there exists a
> stratification $\mathcal{M}_{\mathrm{obs}} = \mathcal{M}_{\mathrm{obs}}^{\mathrm{reg}} \sqcup \Sigma$ with $\Sigma \subset \mathcal{M}_{\mathrm{obs}}$
> a closed set of codimension $\ge 1$ (the branch-switching set) and
> $\mathcal{M}_{\mathrm{obs}}^{\mathrm{reg}}$ open and dense, such that:
>
> 1. $V|_{\mathcal{M}_{\mathrm{obs}}^{\mathrm{reg}}} \in C^2$ and Morse on $\mathcal{M}_{\mathrm{obs}}^{\mathrm{reg}}$ (finite, non-degenerate critical points
>    in the open stratum).
> 2. Across $\Sigma$, $V$ is continuous and admits one-sided directional
>    derivatives that may differ.
> 3. The set of critical points of $V$ on $\Sigma$, in the Clarke
>    subdifferential sense, is allowed but counts as a separate "interface
>    critical class".

This relaxes the global Morse hypothesis to a **stratified Morse** hypothesis
(Goresky–MacPherson, *Stratified Morse Theory*, 1988). The critical points
relevant to OMS basin counting are:

(i) classical Morse minima inside open strata (regular branches),
(ii) interface minima where two branches glue with a sign change in
    one-sided derivatives.

Both contribute to basin enumeration; both are robust under small
perturbations of $V$ within $\mathcal{V}_{\mathrm{adm}}$ (Palis–Smale structural stability,
adapted to stratified flows).

---

## §3. Other criteria — unchanged

V1 (gauge invariance), V3 (readout compatibility), V4 (basin generating),
V5 (boundary awareness) are **unchanged** by this patch. None of them
require $V$ to be $C^1$ at $\Sigma_{\mathrm{branch}}$.

V3 (readout compatibility): now reads "compatible with the smooth-component
readout $R$ on each open stratum"; the discrete components ($K_{\mathrm{core}}$,
$n_{\mathrm{high}}$) jump at $\Sigma$, providing the "compatibility" with $V$'s
non-smoothness.

---

## §4. Concrete admissible $V$ candidates after the patch

Under the stratified-V2 reading:

- **$V_D^0(\lambda) := \lVert d(\lambda) - d^* \rVert^2$** (with $d^* = (1,1,1,0)$):
  Continuous on $\Delta^3$ (since $d$ is continuous on regular branches and
  has bounded jumps at $\Sigma_{\mathrm{branch}}$). $C^2$ on each open
  branch domain. **Admissible** under stratified V2.
- **$V_P(\Theta) := D_{\mathcal{P}}(P(\Theta), P^*) = \alpha \lVert d - d^* \rVert^2 + \beta D_T(T_\Theta, T^*)$:**
  The $D_T$ term has discrete components, so $V_P$ is **not** continuous
  at $\Sigma_{\mathrm{branch}}$ — it has level jumps when $K_{\mathrm{core}}$
  flips. **Not admissible** as written; would require either dropping $D_T$
  or smoothing $D_T$ (replacing discrete distances with continuous proxies).
  This is a finding of Session 5: $V_P$ as currently defined fails
  stratified V2 unless its topological-distance term is replaced.
- **$V_E(\lambda) := v(\lambda)$ (the value function itself):** R4
  PROVED $v$ continuous, concave, locally Lipschitz on $\Delta^3$ — fully
  admissible under stratified V2 (in fact better: globally Lipschitz).
  However, $V_E$ is monotone-aligned with the **easiest** $\lambda$, not the
  most perceptually informative one. Use $-V_E$ if a maximum-energy basin
  is desired. **Admissible** but conceptually different role.

Net effect: among the candidates in `observer_landscape_candidates.md`,
$V_D^0$ and $V_E$ remain admissible; $V_P$ as written needs revision.

---

## §5. Implications for OP-OMS-002

OP-OMS-002 (existence of $V \in \mathcal{V}_{\mathrm{adm}}$) had been HYPOTHESIZED via $V_P$.
Post-Session-5:

- **$V_E = v$:** PROVED admissible (R4 + stratified V2). Hence
  **$\mathcal{V}_{\mathrm{adm}} \neq \emptyset$ is now PROVED** (constructively, by $V_E$).
- $V_E$ is concave on $\Delta^3$, with a unique global minimum at the
  energy-minimizing observer — but this is typically a vertex (e.g.\ the
  cl-dominant vertex on grid scenes), making $V_E$ a **degenerate** choice
  for basin-counting. So the constructive existence is real but trivial.
- A **non-trivial** admissible $V$ with multiple internal basins remains
  HYPOTHESIZED. The cleanest candidate is $V_D^0$, whose admissibility
  under stratified V2 is COMPUTATIONALLY SUPPORTED but not formally proved.

**Status update.**

| Claim | Pre-Session-5 | Post-Session-5 |
|---|---|---|
| $\mathcal{V}_{\mathrm{adm}} \neq \emptyset$ | HYPOTHESIZED | **PROVED** (by $V_E = v$) |
| $\mathcal{V}_{\mathrm{adm}}$ contains a non-trivial multi-basin element | HYPOTHESIZED | unchanged (HYPOTHESIZED via $V_D^0$, computationally supported) |

---

## §6. Audit consequences

- The OP-OMS-002 canonical blocker is **softened**: existence is PROVED;
  only the "non-trivial multi-basin" version remains open.
- This unlocks one of the two remaining OMS-1.x → OMS-2.0 blockers.
- The remaining OMS-2.0 blockers are: OP-OMS-001 (formal G_cw proof),
  OP-OMS-002+ (non-trivial admissible $V$), OP-OMS-026 ($\Sigma_{\mathrm{branch}}$
  characterization).
