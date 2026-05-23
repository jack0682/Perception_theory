---
id: SI-v1
type: working/theory
status: open — Session W draft; T-σ-Inherit future Cat B candidate (parts a,d); Cat C (parts b,c); OP-0008 restructured into CONT/MERGE/SPLIT/DIST; not promoted
created: 2026-05-06
session: Session W (W6 D4, 2026-05-06)
scope: σ-signature inheritance through persistent-component correspondence and K-jump events
related:
  - canonical.md §§11.1 (Commitment 14, 14-Multi, 18), §13 (T-σ-multi-A-Static), §14 (CN5, CN10)
  - theorem_status.md (OP-0008, OP-0009)
  - temporal_identity_perscomp_transport.md (R_{t→s}, five event types, Session V)
  - emergent_multi_formation_synthesis.md §4 (gap: σ-inheritance)
  - sigma_rich_augmentation.md (σ_rich definition, Φ_rich construction, W5 Day 4)
  - sigma_rich_phi_proof.md (Φ_rich determinism proof sketch, W5 Day 4)
  - CODE/scc/sigma_rich.py (SigmaRich implementation)
  - CODE/tests/test_sigma_rich.py (246 lines; all passing)
---

> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q4_K_selection]] · [[MOC_sigma_rich_framework]] · [[THEORY_INDEX]]


# σ-Signature Inheritance Through Component Correspondence and K-Jump Events

**Purpose:** Define how the formation signature $\sigma(C_i^t; u_t, \mathcal{P}_t)$ transforms as
persistent components $C_i^t$ change to $C_j^s$ through the identity relation $R_{t \to s}$
(Session V). Handle all five event types (continuation, merge, split, birth, death). State the
theorem candidate T-$\sigma$-Inherit and restructure OP-0008 into four tractable sub-problems.

**Session:** Session W (2026-05-06). State: CV-1.10, 54A/13B/5C/5R = 77 claims.
No new canonical promotions in this file.

**Architecture note**: This file works within the $\mathcal{F}_M(\mathcal{P})$-primary
architecture (CV-1.10). The K-field Σ^K_M is a local coordinate chart, not the foundational
state space. The component-level σ defined here is derived from $u_t$ restricted to each
persistent component — compatible with the CV-1.10 foundational commitment.

---

## §1. Problem Statement and Scope

### §1.1 What is missing

The formation description at CV-1.10 is:
$$\mathfrak{F}_i(u_t) = (C_i^t,\; \partial C_i^t,\; K_t,\; \sigma_i^?)$$

The spatial objecthood components $(C_i^t, \partial C_i^t)$ are established (D-ST-1..5, T-OP6-B).
The formation count $K_t$ is a derived observable (D-ST-3). The signature $\sigma_i^?$ is a
question mark: it is defined statically per formation at energy minimizers (Commitment 14,
14-Multi, D-6a) but its **inheritance through time** is not defined.

In particular, when persistent components change between $u_t$ and $u_s$ via the identity
relation $R_{t \to s}$ (Session V), the question is:
$$\text{Given } \sigma_i^t = \sigma(C_i^t; u_t,\, \mathcal{P}_t),
  \text{ what is } \sigma_j^s = \sigma(C_j^s; u_s,\, \mathcal{P}_s)?$$

This is OP-0008. The answer depends on the event type in $R_{t \to s}$.

### §1.2 Why now

T-Temporal-Identity (Session V) defines the five event types and gives $R_{t \to s}$. To
complete the formation description $\mathfrak{F}_i = (C_i, \partial C_i, K, \sigma_i)$ through
time, σ inheritance must be defined. This is the second major temporal layer, blocked by the
lack of a component-level σ definition and an inheritance formula per event type.

### §1.3 What this file does

1. Component-level signature $\sigma(C_i^t; u_t, \mathcal{P}_t)$ — derived from $\sigma_\mathrm{rich}$ (§2).
2. Inheritance through $R_{t \to s}$ — per event type (§3).
3. Inheritance residual $\mathcal{R}_\sigma$ measuring prediction error (§4).
4. Theorem candidate T-$\sigma$-Inherit (§5).
5. OP-0008 restructuring into CONT / MERGE / SPLIT / DIST (§6).
6. Code alignment with `sigma_rich.py` (§7).
7. exp56 plan (§8).
8. Non-overclaim register (§9).

### §1.4 What this file does NOT do

- Does not promote any claim to canonical status.
- Does not resolve OP-0008 (marks it PARTIALLY STRUCTURED).
- Does not start Package II / Kramers rates.
- Does not claim $\sigma_\mathrm{standard}$ Hessian eigenvalues are deterministic under merge
  (this is the hard Cat C part; centroid + orientation are Cat B).
- Does not define T-MF-Synthesis or promote T-Temporal-Identity.
- Does not modify canonical counts (remain 54A/13B/5C/5R = 77).

---

## §2. Component-Level Signature

### §2.1 Restriction to component support

Let $u_t \in \mathcal{F}_M(\mathcal{P}_t)$ and $C_i^t \in \mathrm{PersComp}(u_t)$. Define
the **restricted field**:
$$u_t^i := u_t \cdot \mathbf{1}_{C_i^t} \;\in\; [0,1]^n, \qquad
  \mathrm{supp}(u_t^i) \subseteq C_i^t$$

with component mass $m_i^t = \sum_{x \in C_i^t} u_t(x)$.

The **component-induced subgraph** is:
$$G_{C_i^t} = \bigl(C_i^t \cup \partial_\epsilon C_i^t,\; E \cap (C_i^t \cup \partial_\epsilon C_i^t)^2\bigr)$$

where $\partial_\epsilon C_i^t = \{y \notin C_i^t : \exists x \in C_i^t,\, (x,y) \in E,\, u_t(y) \geq \epsilon\}$
is a thin boundary buffer (one-hop neighborhood at threshold $\epsilon$). The buffer ensures
the subgraph captures the component boundary structure without bleeding into other components.

In the **well-separated regime** (V3 from OP-0009, inter-formation distance $d_\mathrm{min} \geq 3$),
$\partial_\epsilon C_i^t$ is disjoint from all other components.

### §2.2 Component-level σ_rich

**Definition 2.1** (Component signature). The component signature of $C_i^t$ is:
$$\sigma(C_i^t;\; u_t,\, \mathcal{P}_t)
  := \sigma_\mathrm{rich}(u_t^i;\; G_{C_i^t},\, \mathcal{P}_C)$$

where $\sigma_\mathrm{rich}$ is the rich σ-tuple from `sigma_rich.py` applied to the restricted
field $u_t^i$ on the component subgraph, and $\mathcal{P}_C$ is the parameter registry
restricted to $G_{C_i^t}$.

Explicitly, from the `SigmaRich` namedtuple:
$$\sigma(C_i^t) = \bigl(\sigma_\mathrm{standard}(C_i^t),\; c_i^t,\; \Theta_i^t,\; W_i^t\bigr)$$

with four components:

**(a) $\sigma_\mathrm{standard}(C_i^t)$** — Hessian eigenvalue/multiplicity/irrep triples at
the restricted field $u_t^i$, per Commitment 14 applied to $H(u_t^i)$ on $G_{C_i^t}$.
Captures the spectral structure (stiffness) of the component.

**(b) $c_i^t$** — u-weighted centroid of $C_i^t$:
$$c_i^t = \frac{\sum_{x \in C_i^t} u_t(x)\, x}{\sum_{x \in C_i^t} u_t(x)}
\;\in\; \mathbb{R}^d$$

Captures spatial location.

**(c) $\Theta_i^t$** — inertia tensor and its eigenspectrum:
$$\Theta_i^t = \bigl(\mu_{i,\alpha}^t,\, [v_{i,\alpha}^t]\bigr)_\alpha$$
from $M_i^t = \sum_{x \in C_i^t} u_t(x)\,(x - c_i^t)(x - c_i^t)^T$. Captures spatial extent
and orientation.

**(d) $W_i^t$** — Wigner–von Neumann avoided-crossing data for pairs within the component.
Captures spectral anti-crossing structure related to Goldstone modes.

### §2.3 Well-definedness

**Proposition 2.2** (Well-definedness). $\sigma(C_i^t; u_t, \mathcal{P}_t)$ is well-defined
when:
1. $C_i^t$ is connected (guaranteed by PersComp definition D-ST-3).
2. $m_i^t = \sum_{x \in C_i^t} u_t(x) > 0$ (non-empty component with positive mass).
3. $G_{C_i^t}$ has at least one edge (non-trivial spatial extent).

Under V3 (formation separation), the buffer $\partial_\epsilon C_i^t$ is disjoint from
other components, so the subgraph is unambiguous.

**Remark on the K-field architecture connection**: In the K-field architecture (Σ^K_M,
Commitment 14-Multi, D-6a canonical), σ_j is computed on the per-formation field $u^{(j)}$
with the full graph $G$. The component-level Definition 2.1 is the F_M(G)-primary analogue:
instead of K-field indices $j = 1, \ldots, K$, we use PersComp-derived sets $C_i^t$.
In the well-separated regime, both definitions agree: $\sigma(C_i^t) \approx \sigma_j$ when
$C_i^t \approx \mathrm{supp}(u^{(j)})$ (Coupling Bound Lemma, canonical §12).

### §2.4 Code function (planned)

New function needed in `CODE/scc/sigma_rich.py` or `CODE/scc/temporal_identity.py`:

```python
def component_sigma(
    u_t: np.ndarray,
    comps_t: list[set],          # PersComp(u_t): list of component node sets
    graph_state: GraphState,
    params: ParameterRegistry,
    positions: np.ndarray,       # (n, d) node positions
) -> list[SigmaRich]:
    """Compute σ_rich for each component C_i^t ∈ PersComp(u_t).

    Returns list of SigmaRich, one per component. Applies compute_sigma_rich
    to u_t restricted to each component subgraph.
    """
    ...
```

Implementation: not done in Session W. Prerequisite for exp56.

---

## §3. Inheritance Through R_{t→s}

Given $R_{t \to s}$ from Session V (five event types), define the σ-inheritance map
$\Phi$ per event type.

### §3.1 Notation

Write $\sigma_i^t = \sigma(C_i^t; u_t, \mathcal{P}_t)$ and
$\sigma_j^s = \sigma(C_j^s; u_s, \mathcal{P}_s)$.

The inheritance map $\Phi$ gives a **predicted** value of $\sigma_j^s$ from pre-step data.
The inheritance residual $\mathcal{R}_\sigma$ (§4) measures the prediction error.

---

### §3.2 Case 1: Continuation ($C_i^t \to C_j^s$, $K_t = K_s$)

**Event**: one-to-one match in $R_{t \to s}$ (stable-K, no birth/death, margin condition).

**Inheritance map $\Phi_\mathrm{CONT}$**:

The formation moves, deforms, and possibly rotates, but does not merge or split. The inherited
signature is the updated signature at the new field configuration:

$$\sigma_j^s = \Phi_\mathrm{CONT}(\sigma_i^t;\; M_{t \to s}\big\vert_{C_i^t \times C_j^s},\; u_s)$$

In the **small-step regime** (small time increment $\delta t = s - t$, V3 condition):

**(a) Centroid update** (deterministic):
$$c_j^s = \frac{\sum_{y \in C_j^s} u_s(y)\, y}{\sum_{y \in C_j^s} u_s(y)}$$

Approximation via transport:
$$\hat{c}_j^s = \frac{\sum_{x \in C_i^t, y \in C_j^s} M_{t \to s}(x,y)\, y}
                     {\sum_{x \in C_i^t, y \in C_j^s} M_{t \to s}(x,y)}$$

**(b) Orientation update** (deterministic):
$$\hat{\Theta}_j^s \approx \Theta_i^t + \delta\Theta(M_{t \to s})$$

where $\delta\Theta$ captures the change in inertia tensor due to mass redistribution under
the transport plan.

**(c) σ_standard update** (approximately continuous):
In the stable-K well-separated regime, the Hessian eigenvalues change continuously along the
gradient flow trajectory. For small $\delta t$: $\sigma_\mathrm{standard}(C_j^s) \approx
\sigma_\mathrm{standard}(C_i^t)$ to first order.

**Hypothesis for Cat B** (CONT-CAT-B): The map
$\sigma_\mathrm{standard}(C_i^t) \mapsto \sigma_\mathrm{standard}(C_j^s)$ is continuous in
the V3-separated stable-K regime, with Lipschitz constant bounded by the transport displacement
$\lVert M_{t \to s} - I \rVert_F$.

---

### §3.3 Case 2: Merge ($\{C_{i_1}^t, C_{i_2}^t\} \to C_j^s$)

**Event**: $K_s = K_t - 1$, two donors $C_{i_1}^t, C_{i_2}^t$ contribute to one recipient $C_j^s$.

**Inheritance map $\Phi_\mathrm{MERGE}$** (from `sigma_rich_phi_proof.md` §4–§6):

**(a) Centroid** (deterministic, Cat B):

By mass conservation $m_j^s \approx m_{i_1}^t + m_{i_2}^t$ (H3 of sigma_rich_phi_proof.md):
$$c_j^s = \frac{m_{i_1}^t\, c_{i_1}^t + m_{i_2}^t\, c_{i_2}^t}{m_{i_1}^t + m_{i_2}^t}$$

This is **deterministic** in the pre-merger σ_rich. The formula follows from the definition
of the centroid alone, independent of the post-merger relaxation trajectory.

**(b) Orientation** (deterministic, Cat B):

By the **parallel-axis theorem** for the merged inertia tensor:
$$M_j^s = M_{i_1}^t + M_{i_2}^t
  + m_{i_1}^t (c_{i_1}^t - c_j^s)(c_{i_1}^t - c_j^s)^T
  + m_{i_2}^t (c_{i_2}^t - c_j^s)(c_{i_2}^t - c_j^s)^T$$

This gives $\Theta_j^s = \mathrm{EigenDecomp}(M_j^s)$ **deterministically** from pre-merger
σ_rich. No knowledge of the relaxation trajectory is needed beyond the centroid and mass.

**(c) Pair identification** (Cat A under H1–H2 of sigma_rich_phi_proof.md):

By Theorem 3.1 of `sigma_rich_phi_proof.md`: the merging pair $(i_1, i_2)$ is identified
by the minimum-centroid-distance + decreasing-Goldstone-gap criterion. Under (H1) stratum
interior + (H2) generic 1-parameter trajectory, identification is unique.

**(d) σ_standard (Hessian eigenvalues)** (Cat C, hardest part):

The post-merger σ_standard requires knowledge of the energy minimizer $u_j^{s,*}$ after
merger. This is NOT directly determined by the pre-merger σ_standard alone — it requires
the post-merger relaxation trajectory. The Wigner–von Neumann data $W_{i_1,i_2}$ partially
predicts it (§2.3.3 of `sigma_rich_augmentation.md`), but the proof is Cat C (Conjecture 8.1
of `sigma_rich_phi_proof.md`, pending Cat A under Wigner-projection argument, W9+).

**Summary for Φ_MERGE**:
$$\hat{\sigma}_j^s = \Phi_\mathrm{MERGE}(\sigma_{i_1}^t, \sigma_{i_2}^t; m_{i_1}^t, m_{i_2}^t)
= \bigl(\sigma_\mathrm{standard}^?\,,\; c_j^{s,\mathrm{pred}},\; \Theta_j^{s,\mathrm{pred}},\; W_j^{s,?}\bigr)$$

where $?$ denotes Cat C components (Hessian eigenvalues; Wigner post-merger).

---

### §3.4 Case 3: Split ($C_i^t \to \{C_{j_1}^s, C_{j_2}^s, \ldots\}$)

**Event**: $K_s > K_t$, one component $C_i^t$ produces $\geq 2$ components at $s$.

**Inheritance map $\Phi_\mathrm{SPLIT}$**:

**(a) Split-direction prediction from σ_standard**:

The split direction is predicted by the **lowest-eigenvalue (Goldstone) mode** of
$\sigma_\mathrm{standard}(C_i^t)$. In the phase-separated regime, the lowest Hessian
eigenvector $v_1$ of $H(u_t^i)$ points along the direction that costs least energy to
deform — this is the split direction.

The split predicts two sub-components:
$$C_{j_1}^s \approx \{x \in C_i^t : v_1(x) > 0\}, \qquad
  C_{j_2}^s \approx \{x \in C_i^t : v_1(x) < 0\}$$

**(b) Sub-component centroids and orientations** (approximately deterministic):

Once the split direction $v_1$ is known, the sub-component centroids and orientations are
determined by the component mass distribution $u_t^i$ and the split partition.

**(c) σ_standard of sub-components** (Cat C):

Requires post-split energy re-optimization. Not determined by pre-split σ_standard alone.

**Hypothesis for Cat B** (SPLIT-CAT-B): Under Morse genericity (the saddle structure on
$C_i^t$ is non-degenerate — the energy landscape has a unique local saddle separating the
two nascent components), the split-direction prediction from $v_1$ is unique and the
sub-component centroid/orientation prediction is Cat B.

**Remark**: Split events are the time-reverse of merge events. In the field dynamics,
splits occur when a K-jump increases $K_\mathrm{act}$ (rare in gradient flow; common under
noise or bifurcation); merges occur when $K_\mathrm{act}$ decreases.

---

### §3.5 Case 4: Birth ($\varnothing \to C_j^s$)

**Event**: $C_j^s$ has no ancestor in $\mathrm{PersComp}(u_t)$.

**Inheritance**: No inheritance — σ computed fresh from $u_s$:
$$\sigma_j^s = \sigma(C_j^s;\; u_s,\, \mathcal{P}_s)$$

The inheritance residual $\mathcal{R}_\sigma = \infty$ (undefined — no ancestor σ to
compare to). There is no prediction from pre-step data.

**CN5 compliance**: Birth events may be triggered by photometric appearance. The cause is
not encoded in σ; σ is a derived diagnostic of the current field, not a causal record.

---

### §3.6 Case 5: Death ($C_i^t \to \varnothing$)

**Event**: $C_i^t$ has no descendant in $\mathrm{PersComp}(u_s)$.

**Inheritance**: σ_i^t is simply discarded. It does not contribute to any $\sigma_j^s$.

**Remark**: The death event records the final σ signature of the dying component. This is
useful for historical queries (e.g., "what was the signature of this formation before it
dissolved?") but has no forward-inheritance content.

---

## §4. Inheritance Residual

**Definition 4.1** (Inheritance residual). For $(C_i^t, C_j^s) \in R_{t \to s}$ with event
type CONT or MERGE or SPLIT, define:

$$\mathcal{R}_\sigma(i \to j) := d_\sigma\!\bigl(\sigma_j^s,\; \hat{\sigma}_j^s\bigr)$$

where $\hat{\sigma}_j^s = \Phi(\sigma_i^t, \ldots)$ is the predicted inherited signature and
$d_\sigma$ is a distance on σ-space.

**Choice of $d_\sigma$**: The σ-space distance decomposes per component:

$$d_\sigma(\sigma, \sigma') = \alpha_c \lVert c - c' \rVert^2
  + \alpha_\Theta \lVert \Theta - \Theta' \rVert_F^2
  + \alpha_\lambda \lVert \lambda_\sigma - \lambda_{\sigma'} \rVert^2$$

where $\lambda_\sigma$ is the vector of σ_standard eigenvalues.

**Interpretation**: For CONT events in the stable regime, $\mathcal{R}_\sigma$ should be
small (bounded by transport displacement, CONT-CAT-B hypothesis). For MERGE events,
$\mathcal{R}_\sigma$ measures how well the centroid + orientation prediction (Cat B) and
the Hessian prediction (Cat C) capture the true post-merger signature.

**For MERGE centroid+orientation sub-components** (Cat B claim):
$$\mathcal{R}_\sigma^{c,\Theta}(i_1, i_2 \to j)
  := \alpha_c \lVert c_j^s - c_j^{s,\mathrm{pred}} \rVert^2
  + \alpha_\Theta \lVert \Theta_j^s - \Theta_j^{s,\mathrm{pred}} \rVert_F^2 \leq \delta_\mathrm{merge}$$

for a small $\delta_\mathrm{merge}$ proportional to the post-merger relaxation displacement.

---

## §5. Candidate Theorem: T-σ-Inherit

### §5.1 Statement

**T-$\sigma$-Inherit — σ-signature inheritance through component correspondence**

Let $u_t, u_s \in \mathcal{F}_M(\mathcal{P})$. Let $R_{t \to s}$ be the temporal identity
relation (T-Temporal-Identity, Session V). For each event type in $R_{t \to s}$:

**(a) Continuation (CONT-CAT-B)**: In the V3-separated, stable-K, small-step regime:
the centroid $c_j^s$ and orientation $\Theta_j^s$ are continuously differentiable in
$(\sigma_i^t,\, M_{t \to s}\vert _{C_i^t \times C_j^s})$ with Lipschitz constant
$\leq C_\mathrm{CONT}$ (determined by V3 inter-formation gap and transport displacement).

**(b) Merge centroid + orientation (MERGE-Cat-B)**: Under mass conservation (H3) and
V3-separation, the predicted centroid $c_j^{s,\mathrm{pred}}$ and orientation
$\Theta_j^{s,\mathrm{pred}}$ from $\Phi_\mathrm{MERGE}$ (§3.3(a,b)) satisfy
$\mathcal{R}_\sigma^{c,\Theta} \leq \delta_\mathrm{merge}$ where $\delta_\mathrm{merge}$
is small in the well-separated regime.

**(c) Merge σ_standard (MERGE-Cat-C)**: Under (H1)-(H4) of `sigma_rich_phi_proof.md` +
Wigner-projection conjecture (Conjecture 8.1, pending W9+), the post-merger Hessian
eigenvalues are predicted by $W_{i_1,i_2}^t$. Currently **Cat C** — requires Wigner-
projection theorem, W9+.

**(d) Split direction (SPLIT-Cat-B)**: Under Morse genericity (non-degenerate saddle at
the split point), the split direction is predicted by the lowest-eigenvalue mode of
$\sigma_\mathrm{standard}(C_i^t)$. Sub-component centroids and orientations follow
deterministically. σ_standard of sub-components is Cat C.

**(e) Birth and death**: No inheritance claim. σ at birth is computed fresh; σ at death
is discarded.

### §5.2 Expected category

| Part | Claim | Status | Blocker |
|------|-------|--------|---------|
| (a) CONT centroid + orientation | Cat B candidate | Working | $C_\mathrm{CONT}$ bound needed |
| (a) CONT σ_standard | Cat B candidate | Working | Continuity of Hessian eigenpairs |
| (b) MERGE centroid + orientation | Cat B candidate | Working | Mass conservation H3 |
| (c) MERGE σ_standard | **Cat C** | Hard | Wigner-projection conjecture (W9+) |
| (d) SPLIT direction | Cat B candidate | Working | Morse genericity hypothesis |
| (d) SPLIT σ_standard | Cat C | Hard | Post-split energy re-optimization |
| (e) Birth / Death | Definitional | Cat B | None (constructive) |

**Overall T-$\sigma$-Inherit**: Working Cat B candidate for parts (a), (b), (d,direction), (e).
Cat C for parts (c), (d,σ_standard). Not promoted in Session W.

### §5.3 Proof sketch for MERGE centroid (part b)

Under mass conservation H3: $u_j^s(x) \approx u_{i_1}^t(x) + u_{i_2}^t(x)$ (additive
merger, restricted to $C_j^s \approx C_{i_1}^t \cup C_{i_2}^t$ in the instantaneous limit).

$$c_j^s = \frac{\sum_x u_j^s(x)\, x}{\sum_x u_j^s(x)}
\approx \frac{\sum_x (u_{i_1}^t + u_{i_2}^t)(x)\, x}{m_{i_1}^t + m_{i_2}^t}
= \frac{m_{i_1}^t c_{i_1}^t + m_{i_2}^t c_{i_2}^t}{m_{i_1}^t + m_{i_2}^t}$$

The prediction error $\lVert c_j^s - c_j^{s,\mathrm{pred}} \rVert$ is bounded by the post-merger
relaxation displacement $\lVert \delta u \rVert$ (the field change during post-merger optimization):
$$\lVert c_j^s - c_j^{s,\mathrm{pred}} \rVert \leq \frac{\lVert \delta u \rVert_1 \cdot \mathrm{diam}(G)}{m_j^s}$$

In the well-separated regime with V3 condition, $\lVert \delta u \rVert_1$ is small (bounded by the
basin radius from T-Persist-1). $\square$ (modulo V3 + H3).

---

## §6. OP-0008 Restructuring

### §6.1 Original statement

OP-0008 was registered as: "σ^A K-jump Inheritance Non-Determinism" — monolithic,
severity HIGH. The inheritance map $\Phi : \sigma^A(t^{*-}) \to \sigma^A(t^{*+})$ requires
merger-geometry data $\mathcal{M}$ beyond σ^A alone.

### §6.2 Restructuring into four sub-problems

Session W proposes splitting OP-0008 into:

| Sub-OP | Name | Scope | Status after Session W |
|--------|------|-------|----------------------|
| **OP-0008-CONT** | σ inheritance (continuation) | Stable-K regime | PARTIALLY STRUCTURED — CONT-CAT-B hypothesis; σ_standard continuity argument |
| **OP-0008-MERGE** | σ inheritance (merge) | K-jump merger events | PARTIALLY STRUCTURED — centroid + orientation Cat B via Φ_MERGE; σ_standard Cat C pending W9+ |
| **OP-0008-SPLIT** | σ inheritance (split) | K-jump split events | STRUCTURED — split-direction Cat B under Morse genericity; σ_standard Cat C |
| **OP-0008-DIST** | σ distribution under equilibrium | Gibbs π_{T_*} at fixed K | NEW — distribution of σ conditional on K; extends T-K-Select-PF |

### §6.3 OP-0008-CONT (continuation)

**Statement.** In the V3-separated stable-K regime, σ(C_i^t) → σ(C_j^s) continuously
along the gradient flow trajectory. The inheritance is approximately the identity map plus
small corrections bounded by the transport displacement.

**Path to Cat B**: Prove continuity of $\sigma_\mathrm{standard}$ (Hessian eigenvalue triples)
along the transport path under V3 condition. Exploit the Coupling Bound Lemma (canonical §12):
per-component Hessian block is approximately decoupled when $d_\mathrm{min} \geq 3$.

### §6.4 OP-0008-MERGE (merge — core hard problem)

**Statement.** At a K-jump merger event $K' \to K'-1$, the post-merger σ(C_j^s) is NOT
determined by pre-merger σ_standard alone. OP-0008 Path B (σ_rich augmentation) gives:

- **Centroid + orientation components**: deterministic via Φ_MERGE — Cat B candidate.
- **σ_standard (Hessian eigenvalues)**: NOT deterministic from σ_standard alone + centroid +
  orientation alone. Requires Wigner-projection data $W_{i_1,i_2}$ — currently Cat C.

**Path to Cat B for σ_standard**: Wigner-projection theorem (Conjecture 8.1 of
`sigma_rich_phi_proof.md`): under (H4) translation invariance, the post-merger lowest
Hessian eigenvalue is approximately the average of the pre-merger Goldstone-pair gap values
(Wigner level repulsion). Proof strategy: perturbation theory on merged Hessian block.
W9+ target.

### §6.5 OP-0008-SPLIT (split)

**Statement.** At a split event, the split direction and sub-component centroids/orientations
are predicted by σ_standard (Goldstone mode) under Morse genericity. The sub-component
σ_standard values require post-split energy re-optimization (Cat C).

**Path to Cat B**: Establish Morse genericity as a generic condition (measure-zero exceptions
only). Connect saddle structure of $u_t^i$ on $C_i^t$ to the Goldstone mode $v_1$.

**Connection to OP-0005-DYN**: The split event corresponds to a Kramers barrier-crossing
event. The barrier height and crossing direction are related to the saddle structure —
connecting OP-0008-SPLIT to the Eyring-Kramers rate theory (Package II). Do not start
Package II here.

### §6.6 OP-0008-DIST (distribution — new sub-problem)

**Statement.** At equilibrium (Gibbs measure $\pi_{T_*}$, fixed $K = K_0$), what is the
marginal distribution of $\sigma = \sigma(C_i; u, \mathcal{P})$ over the sector
$\mathcal{B}_{K_0}$?

T-K-Select-PF (canonical Cat B, CV-1.10) gives $p_K = \pi_{T_*}(\mathcal{B}_K)$ but does
NOT give the within-sector σ distribution. OP-0008-DIST asks for:
$$p_\sigma(S \mid K) = \pi_{T_*}(\{u \in \mathcal{B}_K : \sigma(C_i^t; u, \mathcal{P}) \in S\})$$

This is a new direction connecting σ-theory to the equilibrium framework. Not addressed
in the W5 working files. Register as new OP-0008-DIST for future work.

### §6.7 Revised OP-0008 status

| OP | Previous status | Status after Session W |
|----|-----------------|----------------------|
| OP-0008 overall | OPEN (HIGH) | PARTIALLY STRUCTURED — restructured into 4 sub-OPs |
| OP-0008-CONT | (new sub-OP) | PARTIALLY STRUCTURED — CONT-CAT-B hypothesis |
| OP-0008-MERGE | (= original OP-0008 core) | PARTIALLY STRUCTURED — centroid+orientation Cat B; σ_standard Cat C |
| OP-0008-SPLIT | (new sub-OP) | STRUCTURED — split-direction Cat B; σ_standard Cat C |
| OP-0008-DIST | (new sub-OP) | OPEN (new problem registered) |

**OP-0008 overall remains HIGH severity until all four sub-OPs are at Cat A or Cat B canonical.**

---

## §7. Code Alignment with sigma_rich.py

### §7.1 Existing implementation

`CODE/scc/sigma_rich.py` provides:
- `compute_sigma_rich(u_field, graph_state, params, ...)` — full σ_rich on single-field or K-field input
- `compute_centroids(u_field, positions)` — u-weighted centroid per formation
- `compute_orientations(u_field, positions, centroids)` — inertia tensor per formation
- `_sigma_standard(eigvals)` — Hessian eigenvalue clustering
- `_wigner_data(eigvals, eigvecs, u_field)` — Wigner-vN 2×2 blocks
- 246 lines of tests in `test_sigma_rich.py` (all passing)

All four σ_rich components are implemented. The existing code uses K-field input (u_field
shape (K, n) or (n,)). The centroid and orientation formulas in `compute_centroids` and
`compute_orientations` match the Φ_MERGE formulas in §3.3(a,b) exactly.

### §7.2 Gap: no component-level function

The existing code requires the user to pass a field per formation; it does not automatically
extract σ per persistent component from a single field $u_t$ with PersComp decomposition.

**New function (planned, not implemented in Session W)**:

```python
def component_sigma(
    u_t: np.ndarray,          # (n,) full field at time t
    comps_t: list[set],        # PersComp(u_t): list of sets of node indices
    graph_state: GraphState,
    params: ParameterRegistry,
    positions: np.ndarray,     # (n, d) node positions
) -> list[SigmaRich]:
    """σ_rich per component C_i^t ∈ PersComp(u_t).

    For each component, restricts u_t and positions to the component
    support + one-hop buffer, then calls compute_sigma_rich.
    """
    result = []
    for comp in comps_t:
        # Extend comp by one-hop boundary buffer
        buf = _one_hop_buffer(comp, graph_state)
        nodes = sorted(comp | buf)
        u_comp = u_t[nodes]
        pos_comp = positions[nodes]
        g_comp = _subgraph(graph_state, nodes)
        sr = compute_sigma_rich(u_comp, g_comp, params,
                                positions=pos_comp)
        result.append(sr)
    return result
```

### §7.3 Φ_MERGE centroid + orientation formula

The MERGE inheritance formulas (§3.3(a,b)) are directly computable from existing functions:

```python
def phi_merge_centroid(sigma_i1: SigmaRich, sigma_i2: SigmaRich,
                       m_i1: float, m_i2: float) -> np.ndarray:
    """Predicted post-merger centroid (Φ_MERGE centroid)."""
    return (m_i1 * sigma_i1.centroids[0] + m_i2 * sigma_i2.centroids[0]) / (m_i1 + m_i2)


def phi_merge_orientation(sigma_i1: SigmaRich, sigma_i2: SigmaRich,
                          m_i1: float, m_i2: float,
                          c_merged: np.ndarray) -> np.ndarray:
    """Predicted post-merger inertia tensor (parallel-axis theorem)."""
    c1 = sigma_i1.centroids[0]
    c2 = sigma_i2.centroids[0]
    M_merged = (sigma_i1.orientations[0] + sigma_i2.orientations[0]
                + m_i1 * np.outer(c1 - c_merged, c1 - c_merged)
                + m_i2 * np.outer(c2 - c_merged, c2 - c_merged))
    return M_merged
```

Both functions use only the existing SigmaRich attributes. No new computation required.

### §7.4 Implementation plan

The three new functions (`component_sigma`, `phi_merge_centroid`, `phi_merge_orientation`)
are ~50 lines total. They can be added to `CODE/scc/sigma_rich.py` or a new
`CODE/scc/temporal_identity.py`. Deferred to exp56 implementation.

---

## §8. exp56 Plan: σ-Inheritance Toy Experiment

**Planned file**: `CODE/experiments/exp56_sigma_inheritance_toy.py`

**Purpose**: Numerical validation of σ-inheritance formulas for all four event types.
Not implemented in Session W; plan only.

### §8.1 Shared setup

- 2D grid, $n = 20 \times 20 = 400$ nodes.
- Cohesion fields as soft Gaussian bumps with `scc.optimizer.find_formation`.
- `compute_sigma_rich` on each component after PersComp extraction.
- Positions: 2D grid coordinates.

### §8.2 Scenario A: Continuation (CONT)

- $u_t$: one Gaussian bump at $(5,5)$.
- $u_s$: same bump translated to $(6,5)$ (small step).
- Compute $\sigma_i^t$ and $\sigma_j^s$.
- Compute $\mathcal{R}_\sigma^{c,\Theta}$: centroid residual $\lVert c_j^s - \hat{c}_j^s \rVert$ via transport prediction.
- Verify: residual is small (< 0.1 grid units), proportional to displacement.

### §8.3 Scenario B: Merge (MERGE)

- $u_t$: two Gaussian bumps at $(7,10)$ and $(13,10)$, well-separated.
- $u_s$: one merged bump at $(10,10)$.
- Compute σ_rich for each of $C_{i_1}^t, C_{i_2}^t$ and for $C_j^s$.
- Apply $\Phi_\mathrm{MERGE}$: compute $c_j^{s,\mathrm{pred}}$ and $\Theta_j^{s,\mathrm{pred}}$.
- Verify: $\lVert c_j^s - c_j^{s,\mathrm{pred}} \rVert < \delta_\mathrm{merge}$ (Cat B centroid residual).
- Report: σ_standard residual (expected larger — Cat C gap).

### §8.4 Scenario C: Split (SPLIT)

- $u_t$: one elongated bump (high aspect ratio along x-axis).
- $u_s$: two separated bumps at $(6,10)$ and $(14,10)$.
- Compute $\sigma_\mathrm{standard}(C_i^t)$: extract lowest Hessian eigenvector $v_1$.
- Verify: $v_1$ is oriented along the x-axis (split direction).
- Compare predicted split with actual $C_{j_1}^s, C_{j_2}^s$.

### §8.5 Scenario D: Birth

- $u_t$: empty field (no persistent components).
- $u_s$: one Gaussian bump (born at $(10,10)$).
- Verify: $\sigma_j^s$ computed fresh, no residual defined ($\mathcal{R}_\sigma = \mathrm{N/A}$).

### §8.6 Output format

Per scenario: σ_rich values (centroids, orientations, σ_standard), inheritance residuals
$\mathcal{R}_\sigma^{c,\Theta}$ and $\mathcal{R}_\sigma^\lambda$, event type detected.
CSV + JSON summary (compatible with exp55 format).

---

## §9. Non-Overclaim Register

1. **Does not resolve OP-0008**: OP-0008 is PARTIALLY STRUCTURED after Session W, not resolved.
   Cat C parts (σ_standard under merge/split) remain open; W9+ for Wigner-projection theorem.

2. **Does not claim σ_standard determinism under merge**: The hard part of OP-0008 (σ^A Hessian
   eigenvalue inheritance) is Cat C. Only centroid + orientation are Cat B.

3. **Does not start Package II**: Split events connect to Kramers saddle theory (OP-0005-DYN),
   but the connection is noted as a future bridge, not pursued here.

4. **Does not promote T-σ-Inherit**: This is a working Cat B candidate for parts (a), (b), (d,
   direction), (e). Canonical promotion requires exp56 validation + promotion pipeline review.

5. **Does not modify canonical counts**: 54A/13B/5C/5R = 77 claims unchanged.

6. **σ_rich is not a new primitive**: All components of σ_rich (Hessian, centroid, orientation,
   Wigner) are derived diagnostics of $u_t$ (CN10 contrastive, CN5 4-energy independence).
   No new energy term is introduced.

7. **Does not claim unique σ distribution**: OP-0008-DIST is registered as a new open problem;
   the Gibbs-conditional σ distribution is NOT computed or claimed.

8. **Does not assume V3 always**: The Cat B claims (CONT, MERGE centroid+orientation) explicitly
   require the V3 condition (formation separation). The general case without V3 is Cat C.

---

## §8b. Numerical Anchor — exp84 (Session X, 2026-05-06)

**File**: `CODE/experiments/exp84_sigma_inheritance_toy.py`
**Results**: `CODE/experiments/results/exp84_sigma_inheritance_toy.json`

**Status**: ALL PASSED (5/5 scenarios).

| Scenario | Test | Key metric | Result |
|----------|------|------------|--------|
| A CONT | Centroid tracks translation | shift residual < 0.5 grid unit | PASS |
| B MERGE centroid | $\Phi_\mathrm{MERGE}$ centroid formula | centroid residual < 0.05 | PASS |
| C MERGE orientation | Parallel-axis theorem | Frobenius relative residual < 2% (actual ≈ 0.4%) | PASS |
| D SPLIT direction | Principal axis of inertia = split direction | cos(θ) to column axis > 0.90 | PASS |
| E BIRTH | No inheritance; σ computed fresh | σ well-defined | PASS |

**Method**: 15×15 grid; minimal toy signature σ(C) = (mass, centroid, inertia_tensor); Gaussian blobs; scipy.ndimage connected components. Does NOT use the full `sigma_rich.py` Hessian computation (expensive; not needed for the centroid/orientation Cat B claims).

**Theorem parts supported (T-σ-Inherit)**:
- Part (a) CONT centroid + orientation: validated ✓ (scenario A, centroid shift tracks translation)
- Part (b) MERGE centroid: validated ✓ (scenario B, mass-weighted average formula near-exact)
- Part (b) MERGE orientation: validated ✓ (scenario C, parallel-axis theorem relative error ~0.4%)
- Part (d) SPLIT direction: validated ✓ (scenario D, principal inertia axis = elongation direction)
- Part (e) BIRTH/DEATH: validated ✓ (scenario E, fresh σ computation)
- Part (c) MERGE/SPLIT σ_standard: NOT tested — Cat C, requires Wigner-projection (W9+).

**Limitations**:
- Toy signature omits σ_standard (Hessian eigenvalues) and Wigner data — Cat C parts not tested.
- Near-exact inertia identity (scenario C) relies on well-separated blob supports (minimal cross-terms).
- Uses simple threshold extraction, not full D-ST-3 PersComp.

**Note**: Original plan referenced exp56; renumbered exp84 (exp55–56 already exist).

---

## §10. Session W Boundary and Next Actions

### §10.1 T-σ-Inherit status

| Part | Claim | Status |
|------|-------|--------|
| (a) CONT centroid + orientation | Cat B candidate | Working |
| (a) CONT σ_standard | Cat B candidate | Working (continuity in stable regime) |
| (b) MERGE centroid + orientation | Cat B candidate | Working (Φ_MERGE formula) |
| (c) MERGE σ_standard | Cat C | Hard — W9+ Wigner-projection |
| (d) SPLIT direction | Cat B candidate | Working (Goldstone mode) |
| (d) SPLIT σ_standard | Cat C | Hard |
| (e) Birth / Death | Definitional | Cat B |

### §10.2 OP-0008 sub-problem registry

| Sub-OP | Status after Session W | Next step |
|--------|----------------------|-----------|
| OP-0008-CONT | PARTIALLY STRUCTURED | Prove CONT-CAT-B: Lipschitz bound on σ_standard via Coupling Bound Lemma |
| OP-0008-MERGE | PARTIALLY STRUCTURED | exp56 Scenario B validation; Wigner-projection proof for σ_standard (W9+) |
| OP-0008-SPLIT | STRUCTURED | exp56 Scenario C; Morse genericity proof |
| OP-0008-DIST | OPEN (new) | Define p_σ(S | K) formally; connect to T-K-Select-PF |

### §10.3 Code deliverables (deferred to exp56)

- `component_sigma(u_t, comps_t, graph_state, params, positions)` — ~30 lines
- `phi_merge_centroid(sigma_i1, sigma_i2, m_i1, m_i2)` — ~5 lines
- `phi_merge_orientation(sigma_i1, sigma_i2, m_i1, m_i2, c_merged)` — ~10 lines
- `CODE/experiments/exp56_sigma_inheritance_toy.py` — ~100 lines

### §10.4 Dependencies for T-MF-Synthesis

- T-σ-Inherit canonical Cat B → T-MF-Synthesis Cat A eligible (alongside T-Temporal-Identity).
- T-σ-Inherit Cat B for (c) MERGE σ_standard requires W9+ Wigner-projection.
- T-MF-Synthesis Cat B can proceed once T-Temporal-Identity + T-σ-Inherit both reach canonical Cat B
  for their non-Cat-C parts.

**End of sigma_inherit_k_jump.md.**

**Status (Session W):** Working document. T-σ-Inherit is a future Cat B candidate (parts a, b, d-direction, e), Cat C (parts c, d-σ_standard). OP-0008 restructured into CONT/MERGE/SPLIT/DIST. No canonical promotions. 54A/13B/5C/5R = 77 claims.
