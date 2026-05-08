---
type: working/separation
created: 2026-05-08
session: Session 7 (proof closure)
project: Observer Moduli Space of SCC
attacks: OP-OMS-034 — temporal Δ³ separation
status: SEPARATED — static OMS-2.0 does NOT require temporal Δ³; full temporal remains Conditional
---

# OP-OMS-034 — Temporal Δ³ Separation

OP-OMS-034 was registered in Session 6 as the requirement for full
temporal Δ³ branch-map evidence (with non-degenerate $E_{tr}$). The
Session-6 Gate-7 audit listed it as a blocker for OMS-2.0 Accepted.

This file argues that **OMS-2.0 Static** (i.e.\ OMS-2.0 restricted to the
static face $\Delta^2_{\mathrm{static}} = \{\lambda_{tr} = 0\}$) does **not** require
temporal Δ³ evidence, and so OP-OMS-034 is **separated** from the static
acceptance: full temporal OMS remains Conditional.

Final status (declared at the bottom): **SEPARATED**. Static OMS-2.0 promotion proceeds; full temporal OMS remains Conditional on OP-OMS-034.

---

## §1. The two regimes

| Regime | Domain | Status |
|---|---|---|
| **OMS-2.0 Static** | $\Delta^2_{\mathrm{static}} = \{\lambda \in \Delta^3 : \lambda_{tr} = 0\}$ on a **static scene** ($X_{t+1} = X_t$, single time slice) | (this audit) |
| **OMS-2.0 Full Temporal** | Full $\Delta^3$ on a **dynamic scene** ($X_{t+1} \ne X_t$, two or more time slices, non-degenerate $E_{tr}$) | Conditional on OP-OMS-034 |

The static regime is the canonical SCC setting that has been the focus of all VP-1 through VP-10 experiments. The temporal regime requires `scc.multi.transport_k_formations` infrastructure with a multi-time-slice scene graph.

---

## §2. Why static OMS-2.0 does not require temporal Δ³

### Theorem TS1 (Static-temporal independence). [PROVED]

The static-face theorems C1.1, C1.1', C1.2 (corrected), C1.3, C1.4
(honest), C1.5 of `gap_c1_final_theorem_package.md` and SB5, SB7, SB8,
SN3 of `op_oms_026_sigma_branch_full.md` + `op_oms_033_sigma_sn_arnold.md`
are all stated and proved on the **static face** $\Delta^2_{\mathrm{static}}$ for a
**static scene**. None of these theorems use a non-trivial $\lambda_{tr}$
or a non-degenerate $E_{tr}$.

In particular:

- The sensitivity formula (C1.1) involves the 3-component static-face
  energy $(E_{cl}, E_{sep}, E_{bd})$.
- The rank theorem (C1.3) asks for a non-vanishing $3 \times 3$ minor of
  the $(n-1) \times 3$ matrix $G_T$. The dimension of the minor is
  determined by the number of static-face components, not by the
  presence or absence of $E_{tr}$.
- The vertex-fixing argument (C1.4) uses the three vertices
  $\{e_{cl}, e_{sep}, e_{bd}\}$ of $\Delta^2_{\mathrm{static}}$, not the four vertices
  of $\Delta^3$.
- The branch decomposition (SB11 + SN3) is stated for $\Delta^3$ but
  reduces to its $\Delta^2_{\mathrm{static}}$ trace upon imposing $\lambda_{tr} = 0$.

So the entire static OMS-2.0 chain is logically self-contained on the
static face.

### Computational support.

VP-6 (smooth-component Jacobian), VP-7 (Δ² branch map), VP-8 (rank
witness), VP-9 (basin test) all use the static face. VP-10 (pseudo-Δ³)
uses the full simplex but with a static scene where $\lambda_{tr}$ is
degenerate by Prop CW2 — the VP-10 result therefore tests the static
chain on the natural extension to $\Delta^3$ where $\lambda_{tr}$ acts
trivially.

**No experiment in the OMS-2.0 chain actually probes the temporal
direction.** This is by design: the static face is where the SCC-OMS
theory is best understood and where the present results live.

### Static OMS-2.0 is the maximal conservative claim.

Promotion to OMS-2.0 Accepted **at the static-face level** is the maximal
honest claim from the present evidence. Promotion to full temporal Δ³ is
a **strict superset** that requires additional evidence (OP-OMS-034).

---

## §3. What the temporal extension would add

### TE1. Non-degenerate $E_{tr}$ enriches the simplex tangent.

On a dynamic scene, $E_{tr}(u_t, u_{t+1})$ depends non-trivially on the
field at both time slices. The 4th simplex direction $\lambda_{tr}$ becomes a
genuine perturbation direction (not gauge-redundant by Prop CW2).

For Theorem C1.3, this would extend the projected matrix $G_T$ from
$(n-1) \times 3$ to $(n-1) \times 4$, asking for non-vanishing
$4 \times 4$ minors of an $(n-1) \times 4$ matrix. This requires
$n - 1 \ge 4$, i.e.\ $n \ge 5$ — easily satisfied by typical scenes.

### TE2. Temporal $\Sigma_{\mathrm{branch}}$ gains a dimension.

In the temporal regime, $\Sigma_{\mathrm{branch}}$ becomes a codim-1
**hypersurface** in $\Delta^3$ (3-D), with local "fibers" along the
$\lambda_{tr}$ direction. The Σ_ab / Σ_Hess / Σ_AS / Σ_SN decomposition
extends naturally.

### TE3. Temporal $V_2$ basins inherit a transport-cost component.

In the temporal regime, $V_2(\lambda)$ as a function on $\Delta^3$ may
exhibit basins separated also by transport behavior. This is a rich
extension but orthogonal to the static OMS-2.0 question.

### What's *needed* to verify the temporal extension.

1. A **non-degenerate dynamic scene** (e.g.\ a 6×6 grid with a moving
   blob or a graph with edge weights changing across time).
2. `scc.multi.transport_k_formations` infrastructure to compute
   $E_{tr}(u_t, u_{t+1})$ and gradients at a transport solution.
3. Re-running VP-8, VP-9, VP-10 on the temporal scene with $\lambda_{tr}$
   varying.
4. A separate temporal-rank-witness experiment to verify $4 \times 4$ minor
   non-vanishing.

These are doable but require non-trivial scene construction. **OP-OMS-034
remains as the precise specification of this work.**

---

## §4. Separation theorem

### Theorem TS2 (Separation). [DECLARED]

OMS canonical promotion proceeds in two **independent** layers:

(a) **OMS-2.0 Static.** All static-face theorems (C1.1–C1.5, SB5/SB7/SB8/SN3 reduced to $\lambda_{tr} = 0$, NV3–NV10 on $\Delta^2_{\mathrm{static}}$, R1–R5, ED1–ED2, L1) PROVED. Status: **Accepted** at the static-face level.

(b) **OMS-2.0 Full Temporal.** Extension to $\Delta^3$ with non-degenerate $E_{tr}$. Status: **Conditional on OP-OMS-034**.

The two layers are logically decoupled: (a) does not assume anything about (b), and (b) reduces to (a) when $\lambda_{tr} = 0$.

### Implication.

The OMS-2.0 promotion verdict (Gate 7 of Session 6, originally Conditional Accepted) **upgrades** to:

$$\boxed{\text{OMS-2.0 Accepted — Static}} \;+\; \boxed{\text{Full Temporal Conditional on OP-OMS-034}}$$

This is the strongest defensible conservative claim.

---

## §5. Final status

$$\boxed{\text{OP-OMS-034: SEPARATED. Static OMS-2.0 does not require it; full temporal OMS-2.0 conditional on it.}}$$

**Action items (none required for static promotion):**

- OP-OMS-034 remains open as a future research direction.
- A 2-time-slice experiment is the natural next step *after* OMS-2.0 Static is canonicalized.
- No theorem in the static chain is invalidated by the unresolved status of OP-OMS-034.

**Implication for OMS-2.0 Accepted (Static) audit:**

The Gate-7 audit objection "(iii) pseudo-Δ³ ≠ full temporal Δ³" is now **separated** rather than blocking. Static OMS-2.0 is fully self-contained.

Combined with:

- `op_oms_032_closed_form_h4.md` (CLOSED UNDER CERTIFIED WITNESS) → Gap C1 closed.
- `op_oms_033_sigma_sn_arnold.md` (PROVED conditional theorem) → Σ_SN closed at the conditional-theorem level.
- This file (SEPARATED) → temporal extension out of the static promotion path.

The path to **OMS-2.0 Accepted — Static** is now clear. The full audit is `oms_2_0_accepted_audit.md`.
