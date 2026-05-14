> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 04 — Proposed Amendments (R-C + S-i, copy-paste-ready)

**Session:** 2026-05-13
**Target:** Apply audit findings (`02_development.md`) as copy-paste-ready blocks for the user's eventual working-file edit + canonical promotion turn.
**Decision (this turn):**
- **R-C** for Finding §2 (CV-1.14 dependency): rewrite CV-1.15 background + T-ACT-KERNEL-COMP→REL annotation to cite CV-1.14 as *working candidate* (not canonical).
- **S-i** for Finding §3 (style mismatch): split the single `§13.Y` block into per-category inserts matching canonical practice.
- **Findings applied:** 1.2a, 1.2b, 1.3b, 1.4a, 1.4b, 1.5, 1.7, 2.4. Deferred: 1.3a (Sinkhorn $a$ rename — purely internal stylistic; low priority).

**Scope of this file:** *Proposal text only.* Per session prompt §2, no working/* or canonical/* file is modified. The blocks below are intended for one-step copy-paste into `THEORY/working/CV115_ACTION_TEMPORAL_COST/10_patch_plan.md` (replacing §1–§4 of that file) by a follow-up session or by the user directly.

**Depends on reading:** `00_plan.md`, `01_exploration.md`, `02_development.md`, `03_integration_and_new_open.md`.

---

## §A. Replacement for `10_patch_plan.md §1` (canonical.md updates)

### §A.1. Header notes (3 lines, applied uniformly to all inserts below)

Insert all three notes at the **top of each insert block** (Cat A insert + Cat B insert + §12 OPEN insert):

```markdown
> **(기호 주의 — 1)** $\mathbf{K}_{i\to k}$ (볼드)는 Gibbs 전이 kernel을 뜻하며,
> 기존 canonical 표기 $K$ (이탤릭, formation 수)와 다른 기호이다.

> **(기호 주의 — 2)** $\varepsilon$ (action smoothing temperature)는
> canonical §8.5 / T-Temporal-Identity의 $\varepsilon_{\mathrm{OT}}$ (Sinkhorn
> entropic regularization)와 별개 파라미터이다. 두 기호의 역할은 독립이며,
> 명시적으로 구별된다.

> **(refinement framing)** CV-1.15의 action cost는 기존 temporal cost 정의의
> **대체가 아니라 composition-compatible refinement**이다. T-Temporal-Identity
> (§13 Cat A; component score matrix $S^0_{ij}$ derived from $c[u_t, u_s]$ of §8.5)는
> 독립적으로 유효하며, CV-1.15 patch에 의해 수정되지 않는다.
```

(Changes vs. prior 10_patch_plan §1: added (기호 주의 — 2) for ε vs ε_OT (Finding 1.3b); §13 Cat A reference clarified (Finding 1.5). Old §8.5 only-reference replaced.)

### §A.2. Cat A insert — to be appended at the end of `canonical.md ### Category A`

Place *after* the T-PF-A1-PE entry (last CV-1.9 Cat A entry).

```markdown
[Insert all three header notes from §A.1 above this block]

---

**Definition D-LOCAL-ACTION** *(Definition; CV-1.15)*

*Conditions.* $\gamma_\varphi \geq 0$, $\Delta t_i > 0$, $\varphi_i : X_i \to \mathbb{R}^3$
the standard SCC 3-component cohesion fingerprint
$\varphi_i(x) = (u_i(x), \mathrm{Cl}_i(u_i)(x), D_i(x; 1{-}u_i))$ (canonical §8.5;
canonical §7.1 erratum 2026-04-01).

SCC local action between consecutive time-slices:

$$a_i(x,y) \;=\; \frac{d_i(x,y)^2}{\Delta t_i}
\;+\; \gamma_\varphi \frac{\|\varphi_{i+1}(y) - \varphi_i(x)\|^2}{\Delta t_i}.$$

Path action: $\mathcal{A}_{i:k}(P) = \sum_{\ell=i}^{k-1} a_\ell(x_\ell, x_{\ell+1})$
for path $P = (x_i, x_{i+1}, \ldots, x_k)$.
Hard-min action cost: $c^{\mathrm{act}}_{i\to k}(x, z) = \min_{P: x_i=x, x_k=z} \mathcal{A}_{i:k}(P)$.

---

**Lemma L-ENDPOINT-NONSEMI** *(Cat A; CV-1.15)*

Squared endpoint cost $c^\mathrm{end}(x,z) = \|z-x\|^2$ is generically **not**
temporal-composition-compatible:

$$c^\mathrm{end}_{t\to r}(x,z) \;\neq\; \min_y\bigl[c^\mathrm{end}_{t\to s}(x,y) + c^\mathrm{end}_{s\to r}(y,z)\bigr].$$

*Counterexample (1D).* $x=0, z=2 \in \mathbb{R}$: LHS = $|2-0|^2 = 4$; RHS = $\min_y[y^2 + (2-y)^2] = 2$ (at $y=1$). $4 \neq 2$. $\square$

---

**Lemma L-ACTION-NORMALIZATION** *(Cat A; CV-1.15)*

*Conditions.* $t < s < r$, uniform-speed path.

For midpoint $y^* = \frac{r-s}{r-t}\,x + \frac{s-t}{r-t}\,z$:

$$\frac{\|z-x\|^2}{r-t} \;=\; \frac{\|y^* - x\|^2}{s-t} \;+\; \frac{\|z - y^*\|^2}{r-s}.$$

*Note.* Holds for uniform-speed parametrization only.

---

**Lemma L-FINGERPRINT-ACTION-ADMISSIBLE** *(Cat A; CV-1.15)*

*Conditions.*
- $\varphi_i : X_i \to \mathbb{R}^3$ Lipschitz in $u_i$ (canonical §8.5 fingerprint structure ensures Lipschitz on bounded $u \in [0,1]^n$).
- $\Delta t_i > 0$ for each consecutive pair.
- $d_i(\cdot, \cdot) \geq 0$ symmetric pseudo-distance on $X_i \times X_{i+1}$.
- $a_i$ defined per D-LOCAL-ACTION.

Then $a_i(x,y) \geq 0$ for all $(x, y)$ and $\mathcal{A}_{i:k}(P) = \sum_\ell a_\ell$ is
additive over path concatenation. Both T-ACT-DP and T-ACT-GIBBS hypotheses are
satisfied.

*Proof.* Each summand of $a_i$ is a non-negative real ($d_i^2 \geq 0$; $\gamma_\varphi \|\Delta\varphi\|^2 \geq 0$), so $a_i \geq 0$. Additivity is by definition: for $P = P_1 \cdot P_2$ joined at $x_j$, $\mathcal{A}(P) = \sum_{\ell=i}^{j-1} a_\ell + \sum_{\ell=j}^{k-1} a_\ell = \mathcal{A}(P_1) + \mathcal{A}(P_2)$. $\square$

---

**Theorem T-ACT-DP** *(Cat A; CV-1.15)*

*Conditions.* Each $X_i$ finite; $\mathcal{A}$ additive (L-FINGERPRINT-ACTION-ADMISSIBLE); $i < j < k$.

$$\boxed{\;c^{\mathrm{act}}_{i\to k}(x, z) \;=\; \min_{y \in X_j}\bigl[c^{\mathrm{act}}_{i\to j}(x, y) + c^{\mathrm{act}}_{j\to k}(y, z)\bigr]\;}$$

*Proof.* ($\geq$): For any path $P$ from $x$ to $z$, $P$ passes through some $y_P \in X_j$, and $\mathcal{A}(P) = \mathcal{A}(P|_{i:j}) + \mathcal{A}(P|_{j:k}) \geq c^{\mathrm{act}}_{i\to j}(x, y_P) + c^{\mathrm{act}}_{j\to k}(y_P, z) \geq \min_y[\cdots]$. Taking infimum (= min since $X$ finite) over $P$ yields $\geq$. ($\leq$): Let $y^* = \arg\min_y$ and $P^*_1, P^*_2$ optimal paths $x \to y^*$ and $y^* \to z$. The concatenation $P^*_1 \cdot P^*_2$ has action $c^{\mathrm{act}}_{i\to j}(x, y^*) + c^{\mathrm{act}}_{j\to k}(y^*, z) = \min_y[\cdots]$, providing an upper witness for $c^{\mathrm{act}}_{i\to k}(x, z)$. $\square$

---

**Lemma L-ACTION-DELTA-EFF-ZERO** *(Cat A; CV-1.15; under action direct cost redefinition only)*

*Conditions.* T-ACT-DP conditions.

If we redefine the direct cost on temporal interval $(t, r)$ as
$c^{\mathrm{direct}}_{i \to k} := c^{\mathrm{act}}_{i \to k}$, then

$$\delta_{\mathrm{eff}} \;:=\; \bigl\|c^{\mathrm{act}}_{i\to k} - c^{\mathrm{eff}}_{i\to k}\bigr\|_\infty \;=\; 0,$$

where $c^{\mathrm{eff}}_{i\to k}(x,z) = \min_y[c^{\mathrm{act}}_{i\to j}(x,y) + c^{\mathrm{act}}_{j\to k}(y,z)]$.

*Scope restriction (CRITICAL).* This holds **only** when the direct cost is redefined as the action cost. It does **NOT** apply to endpoint cost $c^{\mathrm{end}}$, fingerprint similarity cost (the standard SCC self-referential cost $c[u_t, u_s]$ used in single-formation transport, canonical §8.5; cf. T-Temporal-Identity score matrix derivation), or Sinkhorn plan-derived effective costs (cf. T-SINKHORN-PLAN-SEMIGROUP-FAILS).

*Proof.* Direct application of T-ACT-DP. $\square$

---

**Definition D-GIBBS-KERNEL** *(Definition; CV-1.15)*

*Conditions.* L-FINGERPRINT-ACTION-ADMISSIBLE conditions; $\varepsilon > 0$ (action smoothing temperature; distinct from $\varepsilon_{\mathrm{OT}}$ per (기호 주의 — 2)).

Local Gibbs kernel: $\mathbf{K}_{\ell, \ell+1}(x, y) = \exp(-a_\ell(x, y) / \varepsilon)$.
Long-horizon kernel: $\mathbf{K}_{i\to k}(x, z) = \sum_{P: x_i=x, x_k=z} \exp(-\mathcal{A}_{i:k}(P) / \varepsilon)$.
Soft-min action cost: $c^\varepsilon_{i \to k}(x, z) = -\varepsilon \log \mathbf{K}_{i\to k}(x, z)$.

---

**Theorem T-ACT-GIBBS** *(Cat A; CV-1.15)*

*Conditions.* Each $X_j$ finite; $\mathcal{A}$ additive; $\varepsilon > 0$; $i < j < k$.

$$\boxed{\;\mathbf{K}_{i\to k}(x, z) \;=\; \sum_{y \in X_j} \mathbf{K}_{i\to j}(x, y) \cdot \mathbf{K}_{j\to k}(y, z)\;}$$

equivalently, $\mathbf{K}_{i\to k} = \mathbf{K}_{i\to j} \cdot \mathbf{K}_{j\to k}$ (matrix product). Soft-min recursion:

$$c^\varepsilon_{i\to k}(x, z) \;=\; -\varepsilon \log\!\sum_{y \in X_j} \exp\!\left(-\frac{c^\varepsilon_{i\to j}(x, y) + c^\varepsilon_{j\to k}(y, z)}{\varepsilon}\right).$$

*Proof.* Path-integral disjoint-union over the intermediate site $y \in X_j$: $\mathbf{K}_{i\to k}(x, z) = \sum_P \exp(-\mathcal{A}(P)/\varepsilon) = \sum_{y \in X_j} \sum_{P_1: x \to y, P_2: y \to z} \exp(-[\mathcal{A}(P_1) + \mathcal{A}(P_2)]/\varepsilon) = \sum_y \bigl[\sum_{P_1} e^{-\mathcal{A}(P_1)/\varepsilon}\bigr] \bigl[\sum_{P_2} e^{-\mathcal{A}(P_2)/\varepsilon}\bigr] = \sum_y \mathbf{K}_{i\to j}(x, y) \cdot \mathbf{K}_{j\to k}(y, z)$. Soft-min recursion is the $-\varepsilon \log$ image of this identity. $\square$

*Remark.* This is a Chapman-Kolmogorov-type identity in the action-derived setting; it is distinct from the Markov / probabilistic Chapman-Kolmogorov referenced in OP-0012-CC (theorem_status.md line 777).

---

**Lemma L-SOFTMIN-HARDMIN-BOUND** *(Cat A; CV-1.15)*

*Conditions.* $a \in \mathbb{R}^N$ with $N$ finite; $\varepsilon > 0$.

$$\min_i a_i - \varepsilon \log N \;\leq\; \mathrm{smin}_\varepsilon(a) \;\leq\; \min_i a_i,$$

where $\mathrm{smin}_\varepsilon(a) = -\varepsilon \log \sum_i e^{-a_i / \varepsilon}$.

*Proof.* Standard log-sum-exp identities. Upper bound: $\sum_i e^{-a_i/\varepsilon} \geq e^{-\min a / \varepsilon}$, so $-\varepsilon \log(\cdot) \leq \min a$. Lower bound: $\sum_i e^{-a_i/\varepsilon} \leq N \cdot e^{-\min a / \varepsilon}$, so $-\varepsilon \log(\cdot) \geq \min a - \varepsilon \log N$. $\square$

---

**Lemma L-SOFT-ACTION-DELTA-EFF-ZERO** *(Cat A; CV-1.15)*

*Conditions.* T-ACT-GIBBS conditions.

For the soft-min action cost $c^\varepsilon$ obtained from D-GIBBS-KERNEL:

$$c^\varepsilon_{i\to k} \;=\; c^{\mathrm{eff},\varepsilon}_{i\to k}, \qquad \delta^\varepsilon_{\mathrm{eff}} = 0,$$

where $c^{\mathrm{eff},\varepsilon}_{i\to k}(x, z) = -\varepsilon \log \sum_y e^{-(c^\varepsilon_{i\to j}(x, y) + c^\varepsilon_{j\to k}(y, z))/\varepsilon}$.

*Proof.* Direct $-\varepsilon \log$ image of T-ACT-GIBBS Chapman-Kolmogorov identity. $\square$

*Scope restriction.* Same as L-ACTION-DELTA-EFF-ZERO: holds for action-derived $c^\varepsilon$ only; does NOT apply to Sinkhorn plan-derived effective costs.
```

(Eight Cat A entries. P-ACTION-PATH-INHERITANCE goes to §A.5 as Interpretation, not Cat A.)

### §A.3. Cat B insert — to be appended at the end of `canonical.md ### Category B`

Place *after* the T-Temporal-Identity body (currently the last Cat B entry, though the body indicates Cat A promotion in CV-1.13 — see §A.3.0 below).

#### §A.3.0. Pre-existing Cat B header hygiene (Finding 2.4)

The Category B section header (canonical.md line 1688) currently reads:

> "### Category B: Proved with Explicit Structural Parameter (5 theorems + T-P-F-ε0-K CV-1.7 + T-K-Select-PF Session R 2026-05-06 + T-K-Select-OBS Session Y 2026-05-06 CV-1.11 + T-Temporal-Identity W7-FINAL 2026-05-10 CV-1.12; T-OP6-B promoted to Cat A Session K 2026-05-06; T-PF-A1-GI + T-PF-A1-PE promoted to Cat A Session P 2026-05-06)"

Update the header in the same patch turn to add the T-Temporal-Identity promotion (currently un-recorded in the header although the body has it):

```markdown
### Category B: Proved with Explicit Structural Parameter (5 theorems + T-P-F-ε0-K CV-1.7 + T-K-Select-PF Session R 2026-05-06 + T-K-Select-OBS Session Y 2026-05-06 CV-1.11 + T-Temporal-Identity W7-FINAL 2026-05-10 CV-1.12; T-OP6-B promoted to Cat A Session K 2026-05-06; T-PF-A1-GI + T-PF-A1-PE promoted to Cat A Session P 2026-05-06; **T-Temporal-Identity promoted to Cat A W7-CV1.13 2026-05-10 (CV-1.13)**; **CV-1.15 adds T-ACT-KERNEL-COMP→REL conditional + P-SINKHORN-STABILITY-CONDITIONAL**)
```

#### §A.3.1. T-ACT-KERNEL-COMP→REL — Cat B conditional under R-C

```markdown
[Insert the three header notes from §A.1 above this block, if not already inserted by §A.2]

---

**Theorem T-ACT-KERNEL-COMP→REL** *(Cat B conditional; CV-1.15)*

*Conditions.*
- *(GK) [pending CV-1.14 canonical promotion]:* Adopt $M_{t\to s} := \mathbf{K}_{t\to s}$ (action-derived Gibbs kernel) as the canonical transport kernel. This requires either (a) CV-1.14 T-CC-StableK-Kernel promotion (currently a working candidate in `THEORY/working/CV114_TEMPORAL_COMPOSITION/05_promotion_draft.md`, Cat B not yet canonical), or (b) a future canonical §8.5 $M_{t\to s}$ redefinition. Both are deferred to CV-1.16+.
- *(stable-K)* $K_t = K_s = K_r$, $d_{\mathrm{inter}}^* \geq 3$, $\varepsilon_{\mathrm{OT}} \leq \varepsilon_{\mathrm{OT}}^*$.
- *(margin)* $\Delta_{\mathrm{sep}}(M) \geq \Delta_{\mathrm{sep}}^* + 2\epsilon_{\mathrm{kernel}}$ (per S-C1 CERTIFIED correction, CV-1.13).

*Conclusion.* Under (GK) + (stable-K) + (margin):

$$R\bigl[\mathbf{K}_{t\to r}\bigr] \;=\; R\bigl[\mathbf{K}_{t\to s}\bigr] \;\circ\; R\bigl[\mathbf{K}_{s\to r}\bigr],$$

where $R[\cdot]$ is the persistence-correspondence relation extracted from a transport kernel (per T-Temporal-Identity, canonical §13 Cat A).

*Proof sketch.* By T-ACT-GIBBS (this section, Cat A), $\mathbf{K}_{t\to r} = \mathbf{K}_{t\to s} \cdot \mathbf{K}_{s\to r}$ (matrix product). Under (GK), this matrix product is a composition-structured canonical transport kernel. Apply T-CC-StableK-Kernel **(working candidate, CV-1.14; not yet canonical)** to the composition under (stable-K) + (margin), obtaining $R[M_{t\to r}^{\mathrm{comp}}] = R[M_{s\to r}] \circ R[M_{t\to s}]$ with $M_{t\to r}^{\mathrm{comp}} = \mathbf{K}_{t\to r}$. $\square$

*Cat B conditional status.* The Cat B rating is conditional on the working-candidate status of T-CC-StableK-Kernel. If the user has reason to defer CV-1.14, the present theorem is consequently weaker than Cat B as defined in canonical convention. Two consistent readings:
  - **Reading 1 (preferred under R-C):** Mark Cat B but annotate inline as "conditional on CV-1.14 promotion." This row remains Cat B pending CV-1.14, and would resolve to unconditional Cat B once CV-1.14 promotes.
  - **Reading 2 (under R-B fallback):** Demote to Cat C until CV-1.14 promotes.

This row uses Reading 1.

*References.* T-ACT-GIBBS (§A.2 above); T-CC-StableK-Kernel (`THEORY/working/CV114_TEMPORAL_COMPOSITION/05_promotion_draft.md` §2); T-Temporal-Identity (canonical §13 Cat A, CV-1.13).

---

**Proposition P-SINKHORN-STABILITY-CONDITIONAL** *(Cat B; CV-1.15)*

*Conditions.* Hypothesis package (H-SINK) + (MARGIN) + (SMALL-SINK-GAP), as defined in `THEORY/working/CV115_ACTION_TEMPORAL_COST/05_relation_to_sinkhorn.md`.

*Conclusion.* The Sinkhorn-scaled relation $R[M^{\mathrm{sink}}_{t \to s}]$ is stable under the hypothesis package, in the sense that $R[M^{\mathrm{sink}}_{t \to r}]$ approximates $R[M^{\mathrm{sink}}_{s \to r}] \circ R[M^{\mathrm{sink}}_{t \to s}]$ up to terms controlled by the small-sink-gap parameter.

*Cat B conditional status.* H-SINK is itself a hypothesis (the Sinkhorn-scaling regime) not yet promoted as a Cat A property; SMALL-SINK-GAP is a regime restriction. Both are explicit.

*Reference.* Working draft, `THEORY/working/CV115_ACTION_TEMPORAL_COST/05_relation_to_sinkhorn.md`.
```

### §A.4. OPEN insert — to be appended to `canonical.md ## 12. Open Problems and Next Formalization Layers` (or as new "Warning" subsection at the end of §13)

Preferred location: **§12** (Open Problems and Next Formalization Layers) — mirroring OP-0012-SINK structure.

```markdown
**Warning T-SINKHORN-PLAN-SEMIGROUP-FAILS** *(OPEN — proved failure; CV-1.15)*

The independent Sinkhorn-scaled plan $M^{\mathrm{sink}}(\mathbf{K}) = \mathrm{diag}(a)\,\mathbf{K}\,\mathrm{diag}(b)$ does **not** satisfy temporal composition in general:

$$M^{\mathrm{sink}}(\mathbf{K}_{ts}) \cdot M^{\mathrm{sink}}(\mathbf{K}_{sr}) \;\neq\; M^{\mathrm{sink}}(\mathbf{K}_{tr})$$

generically. *Reason.* The intermediate scaling product $b_1 \odot a_2$ is determined independently for each transport problem and is not generically of the form $c \cdot \mathbf{1}$ (a constant vector). Specifically, the LHS expands as $\mathrm{diag}(a_1) \mathbf{K}_{ts} \mathrm{diag}(b_1 \odot a_2) \mathbf{K}_{sr} \mathrm{diag}(b_2)$, while the RHS is $\mathrm{diag}(a_3) \mathbf{K}_{tr} \mathrm{diag}(b_3)$.

*Cat-status.* OPEN (proved failure). The failure direction is closed (counterexample family explicit). The *workable-alternative-with-bound* direction is open: see **OP-0012-SINK** (theorem_status.md Open Problems Catalog) for the structural decomposition of remaining blockers (cost-level gap $\delta_{\mathrm{eff}}^{\mathrm{sink}}$ and plan-level gap).

*Cross-reference.* T-ACT-KERNEL-COMP→REL (§13 Cat B, CV-1.15) provides a kernel-composed alternative under (GK) condition; this is a *different* construction, not a repair of $M^{\mathrm{sink}}$ composition.
```

### §A.5. Interpretation insert — Proposition P-ACTION-PATH-INHERITANCE

Placement options:

- **Option 1 (recommended):** Place at the end of the Cat A insert (§A.2), as the last entry, with a header note "**Proposition (Interpretation)**" to indicate it is not counted in the Cat A/B/C tally.
- **Option 2:** Create a new `### Interpretive Propositions` subsection under §13 (no canonical precedent — first time).

Recommendation: Option 1, with explicit tally note.

```markdown
**Proposition P-ACTION-PATH-INHERITANCE** *(Definition Justification — Interpretation; not counted in A/B/C tally; CV-1.15)*

The SCC temporal identity is more naturally captured by a *low-action path inheritance* criterion than by an *endpoint similarity* criterion. SCC axiom A3 (stabilization tendency; canonical §6 Group A) implies that consecutive time-slices of a stably persisting formation realize a small-action transition path: $a_i(x, y)$ is small along the inherited support. Hence the action cost is the canonical refinement of "small temporal change" suggested by A3.

*Status.* Interpretive justification, not a theorem. Not counted in the canonical A/B/C/R tally. Provides motivation for the canonical adoption of D-LOCAL-ACTION and T-ACT-DP / T-ACT-GIBBS.

*Reference.* Canonical §6 Group A (A3 stabilization); canonical §10 Structural Interpretation.
```

---

## §B. Replacement for `10_patch_plan.md §2` (theorem_status.md updates)

### §B.1. New CV-1.15 section block

Place at the end of `theorem_status.md ## Canonical Theorems (Accepted into Canonical Spec)` (after CV-1.13 section, before "## Active Claims" at line ≈376).

```markdown
### CV-1.15 Canonical Additions — Action-Based Temporal Succession Package (2026-05-13)

*CV-1.15 adds 8 Cat A entries + 2 Cat B entries (T-ACT-KERNEL-COMP→REL Cat B conditional on CV-1.14 working candidate; P-SINKHORN-STABILITY-CONDITIONAL Cat B under H-SINK+MARGIN+SMALL-SINK-GAP) + 1 Interpretation entry (P-ACTION-PATH-INHERITANCE, not counted). Source: `THEORY/working/CV115_ACTION_TEMPORAL_COST/` ten working files completed 2026-05-12; numerical sanity check exp89 3-case PASS 2026-05-13; pre-promotion audit 2026-05-13 (`THEORY/logs/daily/2026-05-13/02_development.md`). Count: +8A, +2B → 67A / 16B / 5C / 5R = 93 claims (Interpretation row excluded from tally).*

| ID | Statement | Status | Cat | Conditions |
|---|---|---|---|---|
| **L-ENDPOINT-NONSEMI** | endpoint² cost is generically not temporal-composition-compatible | Cat A (CV-1.15, 2026-05-13) | A | 1D counterexample explicit ($x=0, z=2$) |
| **L-ACTION-NORMALIZATION** | time-normalized cost additive under uniform-speed path | Cat A | A | uniform-speed parametrization only |
| **L-FINGERPRINT-ACTION-ADMISSIBLE** | SCC fingerprint action satisfies T-ACT-DP / T-ACT-GIBBS premises | Cat A | A | $\varphi_i$ Lipschitz, $\Delta t_i > 0$, $d_i \geq 0$ |
| **T-ACT-DP** | hard-min action cost Bellman DP: $c^{\mathrm{act}}_{i\to k}(x,z) = \min_y[\cdots]$ | Cat A | A | each $X_i$ finite, $\mathcal{A}$ additive |
| **L-ACTION-DELTA-EFF-ZERO** | $\delta_{\mathrm{eff}} = 0$ under direct-cost redefinition $c^{\mathrm{direct}} := c^{\mathrm{act}}$ | Cat A | A | **scope restriction:** action direct cost only |
| **T-ACT-GIBBS** | Gibbs kernel semigroup $\mathbf{K}_{i\to k} = \mathbf{K}_{i\to j} \cdot \mathbf{K}_{j\to k}$ | Cat A | A | $X_j$ finite, $\varepsilon > 0$ |
| **L-SOFTMIN-HARDMIN-BOUND** | $\min a - \varepsilon \log N \leq \mathrm{smin}_\varepsilon(a) \leq \min a$ | Cat A | A | $a \in \mathbb{R}^N$, $N$ finite, $\varepsilon > 0$ |
| **L-SOFT-ACTION-DELTA-EFF-ZERO** | $\delta^\varepsilon_{\mathrm{eff}} = 0$ (T-ACT-GIBBS image) | Cat A | A | scope: action soft-min only |
| **T-ACT-KERNEL-COMP→REL** | $(GK)+(stable-K)+(margin) \Rightarrow R[\mathbf{K}_{t\to r}] = R[\mathbf{K}_{t\to s}] \circ R[\mathbf{K}_{s\to r}]$ | Cat B (conditional, CV-1.15) | B | (GK) requires CV-1.14 T-CC-StableK-Kernel promotion; currently working-candidate |
| **P-SINKHORN-STABILITY-CONDITIONAL** | $R[M^{\mathrm{sink}}]$ stable under (H-SINK)+(MARGIN)+(SMALL-SINK-GAP) | Cat B | B | H-SINK is a regime hypothesis; SMALL-SINK-GAP explicit |
| **P-ACTION-PATH-INHERITANCE** | action cost = path inheritance interpretation (refinement framing) | Interpretation | — | not counted in tally |

**OP-0012 sub-structure update (CV-1.15):**

- OP-0012-CC: Cat B path (unchanged; canonical §13 Cat B body of T-Temporal-Identity at line 1779).
- **OP-0012-SINK (NEW SUB-LABEL):** OPEN. Cost-level $\delta_{\mathrm{eff}}$ blocker closed *under action direct-cost redefinition* (L-ACTION-DELTA-EFF-ZERO Cat A); plan-level scaling-gap blocker OPEN. Required: L-δ_eff-SINK (Cat C target), L-Eff-Sinkhorn (Cat C target).
- OP-0012-Kjump: Cat C, depends on OP-0008, OP-0021.

**Did NOT close:**

- OP-0012 overall (still PARTIALLY STRUCTURED).
- Sinkhorn-scaled plan semigroup (T-SINKHORN-PLAN-SEMIGROUP-FAILS: proved failure stands).
- canonical §8.5 $M_{t\to s}$ redefinition (deferred CV-1.16+).
- OP-0011 (resolved CV-1.12, unchanged).
- OP-0008 (untouched).
- OP-0005-DYN, OP-0021 (untouched).

**Numerical sanity check:** exp89 (3 cases A/B/C) ALL PASS — endpoint nonzero, action zero, soft ≈ machine ε, sinkhorn nonzero. exp89 is a *numerical validation only*, not a proof; Cat A judgments rest on closed-form proofs in `THEORY/working/CV115_ACTION_TEMPORAL_COST/` files 01–04.

*Audit reference:* `THEORY/logs/daily/2026-05-13/02_development.md` + `03_integration_and_new_open.md` + `04_proposed_amendments.md`.
```

### §B.2. OP-0012 entry amendment (lines 517 + 771–793 of theorem_status.md)

**Replace line 517** (quick-index row) with:

```markdown
| **OP-0012** | Persistence composition | Medium | PARTIALLY STRUCTURED (Session V, 2026-05-06); sub-structure refined CV-1.15: OP-0012-CC Cat B path; OP-0012-SINK OPEN; OP-0012-Kjump Cat C |
```

**Replace lines 771–793** (full OP-0012 body) with:

```markdown
#### OP-0012: Persistence Composition

**Quick status:** PARTIALLY STRUCTURED (Session V, 2026-05-06); sub-structure refined (CV-1.15, 2026-05-13). Three sub-labels: OP-0012-CC (Cat B path), OP-0012-SINK (OPEN), OP-0012-Kjump (Cat C). Overall problem **OPEN** — full general-K-jump composition unresolved.

**Sub-case A — OP-0012-CC (compositional consistency, Cat B path):** under stable-K + margin (compositional consistency, Definition 7.1 in `temporal_identity_perscomp_transport.md`), $R_{t \to r} = R_{s \to r} \circ R_{t \to s}$ holds. Cat B via Lemma 6 (`THEORY/logs/daily/2026-05-07/03_development.md §10`) and canonical §13 T-Temporal-Identity composition note at line 1779. See also **T-CC-StableK-Kernel** (working candidate, CV-1.14: `THEORY/working/CV114_TEMPORAL_COMPOSITION/05_promotion_draft.md`) — not yet canonical.

**Sub-case B — OP-0012-SINK (Sinkhorn temporal scaling compatibility, OPEN):** *(CV-1.15 update, 2026-05-13.)*

**Statement.** Independent Sinkhorn-scaled plans $M^{\mathrm{sink}}_{t\to s}, M^{\mathrm{sink}}_{s\to r}, M^{\mathrm{sink}}_{t\to r}$ — computed separately on $(u_t, u_s), (u_s, u_r), (u_t, u_r)$ — do not satisfy temporal composition: $M^{\mathrm{sink}}_{s\to r} \cdot M^{\mathrm{sink}}_{t\to s} \neq M^{\mathrm{sink}}_{t\to r}$ generically (cf. canonical §12 Warning T-SINKHORN-PLAN-SEMIGROUP-FAILS).

**CV-1.15 contribution to OP-0012-SINK structure:**
- Cost-level $\delta_{\mathrm{eff}}$ blocker (gap between direct and effective costs) is *closed* under the redefinition $c^{\mathrm{direct}} := c^{\mathrm{act}}$ (L-ACTION-DELTA-EFF-ZERO Cat A; L-SOFT-ACTION-DELTA-EFF-ZERO Cat A).
- Plan-level *scaling-gap* blocker is **not closed**: the obstruction $b_1 \odot a_2 \neq c \cdot \mathbf{1}$ remains.

**Remaining required lemmas:**
- **L-δ_eff-SINK** (Cat C target): quantitative bound on $\delta_{\mathrm{eff}}^{\mathrm{sink}} := \|c_{\mathrm{direct}}(u_t, u_r) - c^{\mathrm{eff}}(M^{\mathrm{sink}}_{t\to s}, M^{\mathrm{sink}}_{s\to r})\|_\infty$ in terms of marginals, $\varepsilon_{\mathrm{OT}}$, structural separation $\Delta_{\mathrm{sep}}$.
- **L-Eff-Sinkhorn** (Cat C target): quantitative bound on $\|M^{\mathrm{sink}}(\mathbf{K}_{t\to r}) - M^{\mathrm{sink}}_{s\to r} \cdot M^{\mathrm{sink}}_{t\to s}\|_\infty$ in terms of $\|b_1 \odot a_2 - c \cdot \mathbf{1}\|$.

**Path to Cat B (proposed for CV-1.16+):** L-δ_eff-SINK + L-Eff-Sinkhorn both reach Cat C → under stable-K + margin + small-sink-gap → conditional Cat B theorem T-CC-StableK-Sinkhorn.

**Adjacent candidate (not registered):** OP-0022 continuous-time action limit (Γ-convergence of discrete-time $\mathcal{A}_{i:k}$ to a continuous action functional on path space). Deferred CV-1.16+.

**Sub-case C — OP-0012-Kjump (K-jump general, Cat C):** depends on OP-0008 (σ-Inherit, MERGE/SPLIT) and OP-0021 ($T_*$ registration). Unchanged from CV-1.13.

**Sub-case D — OP-0012-Markov (Markov-kernel formulation):** deferred post OP-0021. Unchanged.

**Naming note.** OP-0012-SINK ↦ "Sinkhorn Temporal Scaling Compatibility Problem" rename deferred to CV-1.16+ (when L-δ_eff-SINK or L-Eff-Sinkhorn is attempted). Current session preserves the OP-0012-SINK abbreviation.
```

### §B.3. Header claim-count line update

In the file header (line ~12):

> "**Structure:** Rows are organized by canonical version (CV-1.0 .. CV-1.12; current = **CV-1.13**)"

Update to:

> "**Structure:** Rows are organized by canonical version (CV-1.0 .. CV-1.15; current = **CV-1.15**)"

And append a session-note row at line ~62 (after the CV-1.12 update line):

> *CV-1.15 count update (2026-05-13): action-based temporal succession package — L-ENDPOINT-NONSEMI, L-ACTION-NORMALIZATION, L-FINGERPRINT-ACTION-ADMISSIBLE, T-ACT-DP, L-ACTION-DELTA-EFF-ZERO, T-ACT-GIBBS, L-SOFTMIN-HARDMIN-BOUND, L-SOFT-ACTION-DELTA-EFF-ZERO Cat A (+8A); T-ACT-KERNEL-COMP→REL Cat B conditional on CV-1.14 working candidate; P-SINKHORN-STABILITY-CONDITIONAL Cat B (+2B). P-ACTION-PATH-INHERITANCE Interpretation (not counted). OP-0012-SINK new sub-label (OPEN; cost-level blocker closed under action redefinition, scaling-gap blocker remains). Running total: **67A / 16B / 5C / 5R = 93 claims, ~72% fully proved.** exp89 ALL PASSED (3/3 cases, numerical sanity check only).*

---

## §C. Replacement for `10_patch_plan.md §3` (hypothesis_tree.md updates)

Under R-C, **only two** new H-COMP subbranches are introduced (H-COMP-ACTION + H-COMP-SINK). H-COMP-KERNEL is *not* introduced now because CV-1.14 T-CC-StableK-Kernel is still a working candidate; it would be added at CV-1.14 promotion.

### §C.1. Insert new H-COMP parent branch + two subbranches

Insert under Q5 ("시간이 지나도 같은 것인가?") — currently at line 216 of `hypothesis_tree.md`.

```markdown
### H-COMP — Temporal Correspondence Composition (OP-0012 family)

#### H-COMP-CC (CV-1.12, Cat B path closed)
- **OP-0012-CC**: under stable-K + margin (Definition 7.1, `temporal_identity_perscomp_transport.md`), $R_{t \to r} = R_{s \to r} \circ R_{t \to s}$. Cat B via Lemma 6 (W6 D5).
- Canonical reference: T-Temporal-Identity composition note (canonical.md line 1779).

#### H-COMP-ACTION (CV-1.15, 2026-05-13) [NEW]
- **L-ENDPOINT-NONSEMI** (Cat A): endpoint² 합성 불가 반례 (1D).
- **T-ACT-DP** (Cat A): hard-min action cost Bellman DP.
- **T-ACT-GIBBS** (Cat A): Gibbs kernel semigroup $\mathbf{K}_{i\to k} = \mathbf{K}_{i\to j} \cdot \mathbf{K}_{j\to k}$.
- **T-ACT-KERNEL-COMP→REL** (Cat B conditional): $(GK)+(stable-K)+(margin) \Rightarrow R$ composition.
- *조건 의존성:* (GK) requires CV-1.14 T-CC-StableK-Kernel promotion (working candidate, `THEORY/working/CV114_TEMPORAL_COMPOSITION/05_promotion_draft.md`) or canonical §8.5 $M_{t\to s}$ redefinition. Deferred CV-1.16+.

#### H-COMP-SINK (OP-0012-SINK, OPEN) [NEW]
- **T-SINKHORN-PLAN-SEMIGROUP-FAILS**: scaling-gap obstruction $b_1 \odot a_2 \neq c \cdot \mathbf{1}$ (proved failure).
- **CV-1.15 contribution**: cost-level $\delta_{\mathrm{eff}}$ blocker closed under action direct-cost redefinition (L-ACTION-DELTA-EFF-ZERO Cat A).
- **Remaining**: plan-level scaling-gap blocker; required lemmas L-δ_eff-SINK + L-Eff-Sinkhorn (Cat C targets).

#### H-COMP-Kjump (OP-0012-Kjump, Cat C)
- K-jump general case. Depends on OP-0008 (σ-Inherit), OP-0021 (T_* registration).
- Unchanged from CV-1.13.

#### H-COMP-Markov (OP-0012-Markov, deferred)
- Probabilistic / Markov-kernel formulation. Deferred post OP-0021.
- Unchanged from CV-1.13.

*Note.* H-COMP-KERNEL (CV-1.14 candidate) will be inserted between H-COMP-CC and H-COMP-ACTION when CV-1.14 T-CC-StableK-Kernel is promoted to canonical. Under R-C (this turn), it remains a working-layer concept.
```

### §C.2. HT version increment + changelog row

At the bottom of `hypothesis_tree.md` (changelog section, currently ending at HT-3.5 line 355):

```markdown
| HT-3.6 | 2026-05-13 | **CV-1.15 H-COMP branch added.** Three new subbranches under Q5: H-COMP-ACTION (CV-1.15, Cat A + Cat B conditional), H-COMP-SINK (OP-0012-SINK OPEN), H-COMP-CC (CV-1.12 reference). Under R-C (audit decision 2026-05-13), H-COMP-KERNEL is **not** added at this turn because CV-1.14 T-CC-StableK-Kernel remains a working candidate. CV-1.15 count: +8A +2B → **67A / 14B+2 (one conditional on CV-1.14 promotion) / 5C / 5R = 93 claims**. T-Temporal-Identity Cat A unchanged. Audit reference: `THEORY/logs/daily/2026-05-13/`. |
```

Update the "다음 목표 (CV-1.14 타겟)" line (line 27) to:

> **다음 목표 (CV-1.16 타겟):** OP-0012-SINK 잔여 blocker — L-δ_eff-SINK + L-Eff-Sinkhorn (Cat C). 또는 CV-1.14 T-CC-StableK-Kernel canonical promotion (작업 후보).

---

## §D. Replacement for `10_patch_plan.md §4` (CHANGELOG.md update)

Insert at the **very top of CHANGELOG.md**, above the CV-1.13 entry (line ~5).

```markdown
## [CV-1.15] 2026-05-13 — Action-Based Temporal Succession Package

**Trigger:** CV-1.15 ten working files completed 2026-05-12 (`THEORY/working/CV115_ACTION_TEMPORAL_COST/00–10`); numerical sanity check exp89 3-case PASS 2026-05-13; pre-promotion audit + amendments package 2026-05-13 (`THEORY/logs/daily/2026-05-13/02_development.md + 04_proposed_amendments.md`); user P7 approval [DATE].

### Summary

- **CV-1.15 promotion applied** under decision R-C (Finding §2: CV-1.14 cited as working candidate, not canonical) + S-i (Finding §3: per-category insertion). Audit findings 1.2a, 1.2b, 1.3b, 1.4a, 1.4b, 1.5, 1.7, 2.4 applied (working amendments + canonical insertion).
- **Eight new Cat A entries** (L-ENDPOINT-NONSEMI, L-ACTION-NORMALIZATION, L-FINGERPRINT-ACTION-ADMISSIBLE, T-ACT-DP, L-ACTION-DELTA-EFF-ZERO, T-ACT-GIBBS, L-SOFTMIN-HARDMIN-BOUND, L-SOFT-ACTION-DELTA-EFF-ZERO).
- **Two new Cat B entries** (T-ACT-KERNEL-COMP→REL Cat B *conditional* on CV-1.14 working candidate; P-SINKHORN-STABILITY-CONDITIONAL Cat B under H-SINK+MARGIN+SMALL-SINK-GAP).
- **One new Interpretation entry** (P-ACTION-PATH-INHERITANCE; not counted in A/B/C tally).
- **One new OPEN sub-label**: OP-0012-SINK registered under OP-0012; cost-level $\delta_{\mathrm{eff}}$ blocker closed under action redefinition (L-ACTION-DELTA-EFF-ZERO); plan-level scaling-gap blocker remains.
- **Net count:** +8A, +2B → **67A / 16B / 5C / 5R = 93 claims** (P-ACTION-PATH-INHERITANCE Interpretation row not in tally).
- **HT-3.5 → HT-3.6** (H-COMP branch added; three new subbranches; H-COMP-KERNEL deferred to CV-1.14 promotion under R-C).
- **Cat B header hygiene fix (Finding §2.4):** the §13 Cat B section header now records T-Temporal-Identity's CV-1.13 promotion to Cat A (previously omitted).

### Theorem block summary

| ID | Category | Conditions | Notes |
|---|---|---|---|
| L-ENDPOINT-NONSEMI | Cat A | counterexample | 1D explicit |
| L-ACTION-NORMALIZATION | Cat A | uniform-speed | linear interpolation |
| L-FINGERPRINT-ACTION-ADMISSIBLE | Cat A | φ_i Lipschitz, Δt_i > 0 | DP / Gibbs prerequisites |
| T-ACT-DP | Cat A | X finite, A additive | Bellman DP |
| L-ACTION-DELTA-EFF-ZERO | Cat A | action direct cost redef | δ_eff = 0 (scope-restricted) |
| T-ACT-GIBBS | Cat A | X finite, ε > 0 | Chapman-Kolmogorov-type |
| L-SOFTMIN-HARDMIN-BOUND | Cat A | N finite, ε > 0 | log-sum-exp bound |
| L-SOFT-ACTION-DELTA-EFF-ZERO | Cat A | T-ACT-GIBBS conditions | δ_eff^ε = 0 (scope-restricted) |
| T-ACT-KERNEL-COMP→REL | Cat B (conditional) | (GK)+(stable-K)+(margin) | (GK) pending CV-1.14 promotion |
| P-SINKHORN-STABILITY-CONDITIONAL | Cat B | H-SINK+MARGIN+SMALL-SINK-GAP | H-SINK is regime hypothesis |
| P-ACTION-PATH-INHERITANCE | Interpretation | — | not counted |
| T-SINKHORN-PLAN-SEMIGROUP-FAILS | OPEN (proved failure) | — | canonical §12 Warning |

### Symbol conventions introduced

- $\mathbf{K}_{i \to k}$ (boldface, matrix): action-derived Gibbs transition kernel (D-GIBBS-KERNEL). Distinct from $K$ (italic, scalar) = formation count.
- $\varepsilon$: action smoothing temperature (D-GIBBS-KERNEL). Distinct from $\varepsilon_{\mathrm{OT}}$ in canonical §8.5 / T-Temporal-Identity (Sinkhorn entropic regularization).
- $c^{\mathrm{end}}, c^{\mathrm{act}}, c^{\mathrm{direct}}, c^{\mathrm{eff}}, c^\varepsilon, c^{\mathrm{eff}, \varepsilon}$: cost variants (all defined in §13 Cat A insert).

### Did NOT change

- canonical §8.5 $M_{t \to s}$ definition (deferred CV-1.16+; (GK) requires this).
- canonical §6 Axiomatic Groups (A–E, unchanged).
- canonical §11 Fixed Commitments (CN1–CN14, unchanged).
- canonical §14 Commitment Notes (unchanged).
- T-Temporal-Identity body (canonical §13 Cat A; cross-referenced but not modified).
- OP-0011 (resolved CV-1.12, unchanged).
- OP-0008 (σ-Inherit / MERGE/SPLIT, untouched).
- OP-0005-DYN, OP-0021 (untouched).
- Sinkhorn-scaled plan semigroup status (proved failure stands).

### Files updated

| File | Action |
|---|---|
| `THEORY/canonical/canonical.md` | **UPDATED** — §13 Cat A insert (8 Cat A entries + D-LOCAL-ACTION + D-GIBBS-KERNEL definitions + P-ACTION-PATH-INHERITANCE Interpretation row); §13 Cat B insert (2 Cat B entries); §13 Cat B header amended to record T-Temporal-Identity CV-1.13 promotion (hygiene fix); §12 Warning T-SINKHORN-PLAN-SEMIGROUP-FAILS added. |
| `THEORY/canonical/theorem_status.md` | **UPDATED** — CV-1.15 section block added (10 rows); OP-0012 entry refactored to three sub-labels; header CV version updated to CV-1.15; claim count updated. |
| `THEORY/canonical/hypothesis_tree.md` | **UPDATED** — H-COMP parent branch + four subbranches added under Q5; HT-3.5 → HT-3.6; next-target line updated to CV-1.16. |
| `THEORY/CHANGELOG.md` | **UPDATED** — this entry prepended. |
| `THEORY/working/CV115_ACTION_TEMPORAL_COST/` | (working files; ten files 00–10 completed 2026-05-12; pre-promotion audit + amendments package 2026-05-13) |
| `THEORY/working/CV114_TEMPORAL_COMPOSITION/05_promotion_draft.md` | **NOT MODIFIED** (T-CC-StableK-Kernel CV-1.14 candidate; remains working under R-C) |
| `CODE/experiments/exp89_endpoint_vs_action_temporal_cost.py` | numerical validation script (referenced; not modified this session) |
| `CODE/experiments/results/exp89_results.json` | **REFERENCED** — 3-case PASS (2026-05-13); numerical sanity check, not proof |
| `THEORY/logs/daily/2026-05-13/01_exploration.md, 02_development.md, 03_integration_and_new_open.md, 04_proposed_amendments.md, 99_summary.md` | **CREATED** — pre-promotion audit + amendments package (this session) |

### Outstanding items registered

- **OQ-A** CV-1.14 promotion audit parity — 09-style audit of T-CC-StableK-Kernel draft; precondition for any future R-A path.
- **OQ-B** L-δ_eff-SINK Cat C lemma attempt — first proof attack on OP-0012-SINK plan-level scaling-gap blocker.
- **OQ-C** Continuous-time action limit (OP-0022 candidate) — Γ-convergence framework.
- **OQ-D** canonical §8.5 $M_{t\to s}$ redefinition decision (D1/D2/D3) — affects T-ACT-KERNEL-COMP→REL Cat B status.
- **OQ-E** Interpretation entry convention (P-ACTION-PATH-INHERITANCE prototype).
- **OQ-F** §13 versioned-subsection vs per-category style meta-convention.
- **OQ-G** Pre-existing Cat B header staleness (resolved in this CV-1.15 patch by §2.4 fix).

### Audit reference

`THEORY/logs/daily/2026-05-13/` — five files (00_plan, 01_exploration, 02_development, 03_integration_and_new_open, 04_proposed_amendments, 99_summary). Block A 8 checks executed (10 findings, all LOW–MEDIUM, none blocking). Block D dry-run audit script written (executed for real against post-patch canonical at promotion turn). Block E exp89 PASS verified. Block F OP-0012-SINK structural notes drafted. Block G readiness report delivered.

```

(Note: the date in the header changes from 10_patch_plan's "2026-05-12" to "2026-05-13" since the promotion + exp89 PASS verification both fall on 2026-05-13.)

---

## §E. Status update text for `09_final_audit.md`

Append the following as a new section §12 to `THEORY/working/CV115_ACTION_TEMPORAL_COST/09_final_audit.md`:

```markdown
## §12. 2026-05-13 audit pass — amendments applied (R-C + S-i)

This section records the second-pass audit performed 2026-05-13 (after exp89 PASS), which expanded the "READY AFTER MINOR FIXES" judgment of §10 with additional findings and applied them as amendments.

### §12.1 Findings applied to 10_patch_plan.md (via 04_proposed_amendments.md)

| Finding (label from 2026-05-13 audit) | Severity | Action applied |
|---|---|---|
| §2 CV-1.14 dependency | MEDIUM | **R-C** chosen: CV-1.15 §13.Y background + T-ACT-KERNEL-COMP→REL annotation rewritten to cite CV-1.14 T-CC-StableK-Kernel as *working candidate*, not canonical. T-ACT-KERNEL-COMP→REL Cat B status preserved with explicit "conditional on CV-1.14 promotion" annotation. |
| §3 style mismatch | LOW | **S-i** chosen: single §13.Y block split into per-category inserts (Cat A insert + Cat B insert + §12 OPEN insert + Interpretation insert). |
| 1.2a "fingerprint similarity cost" undefined | LOW | Parenthetical added inside L-ACTION-DELTA-EFF-ZERO 주의-line: "(the standard SCC self-referential cost $c[u_t, u_s]$ used in single-formation transport, canonical §8.5; cf. T-Temporal-Identity score matrix derivation)" |
| 1.2b "temporal identity cost" semantic slip | LOW | §13.Y refinement-framing note rephrased to reference "T-Temporal-Identity (§13 Cat A; based on score matrix $S^0_{ij}$ derived from $c[u_t, u_s]$ of §8.5)" instead of "T-Temporal-Identity (§8.5)". |
| 1.3b $\varepsilon$ vs $\varepsilon_{\mathrm{OT}}$ collision | MEDIUM | (기호 주의 — 2) note added to canonical insert header explicitly distinguishing the two parameters. |
| 1.4a L-FINGERPRINT-ACTION-ADMISSIBLE under-stated conditions | LOW | Explicit condition list added: "$\varphi_i$ Lipschitz, $\Delta t_i > 0$, $d_i \geq 0$, $a_i$ per D-LOCAL-ACTION". |
| 1.4b L-SOFTMIN-HARDMIN-BOUND under-stated conditions | LOW | Explicit condition list added: "$a \in \mathbb{R}^N$, $N$ finite, $\varepsilon > 0$". |
| 1.5 §8.5 cross-reference target | LOW | Header note updated to "(§13 Cat A; $S^0_{ij}$ from §8.5)" — see 1.2b. |
| 1.7 exp89 missing from CHANGELOG file list | LOW | CHANGELOG draft §D §"Files updated" includes exp89 file paths. |
| §2.4 Cat B header staleness (pre-existing) | LOW (hygiene) | Cat B header amended to record T-Temporal-Identity's CV-1.13 promotion to Cat A. |
| 1.3a $a_\ell$ vs $a$ (Sinkhorn row scaling) | LOW | **DEFERRED.** Purely internal stylistic; revisit if T-SINKHORN-PLAN-SEMIGROUP-FAILS body becomes a canonical Cat B + theorem (currently OPEN in §12 Warning subsection). |
| 1.3c $c$ has six superscripts | LOW | **ACCEPTED.** All six superscripts are defined inline in the Cat A insert; no rename. |

### §12.2 Updated readiness judgment

- §10 (2026-05-12): READY AFTER MINOR FIXES (K symbol clarity + refinement framing).
- §11 (2026-05-13 morning, post exp89 PASS): READY FOR USER APPROVAL.
- **§12 (2026-05-13 audit pass): READY FOR USER APPROVAL + AMENDMENTS APPLIED.**

All Cat A 8-entry proofs unchanged. All claim counts unchanged (+8A +2B → 67A/16B/5C/5R = 93 claims, Interpretation row excluded). Symbol clarity, refinement framing, scope restrictions, condition explicitness all updated.

The amendments draft is `THEORY/logs/daily/2026-05-13/04_proposed_amendments.md` (§A through §D). To apply, copy §A blocks into canonical.md, §B into theorem_status.md, §C into hypothesis_tree.md, §D into CHANGELOG.md, and §E (this update) into 09_final_audit.md, all in the user's P7-authorized promotion turn.

*Updated: 2026-05-13. Audit reference: `THEORY/logs/daily/2026-05-13/02_development.md + 04_proposed_amendments.md`.*
```

---

## §F. Apply-order checklist (for the user's P7 promotion turn)

Per `00_plan.md` §C, the application order is:

| Step | File | Action | Source block in this file |
|---|---|---|---|
| 1 | `THEORY/working/CV115_ACTION_TEMPORAL_COST/09_final_audit.md` | Append §12 amendments-applied section | §E |
| 2 | `THEORY/working/CV115_ACTION_TEMPORAL_COST/10_patch_plan.md` | Replace §1, §2, §3, §4 with §A, §B, §C, §D from this file | §A, §B, §C, §D |
| 3 | `THEORY/CHANGELOG.md` | Prepend §D block at top | §D |
| 4 | `THEORY/canonical/theorem_status.md` | Insert §B.1 (CV-1.15 section block); apply §B.2 (OP-0012 amendment); apply §B.3 (header update) | §B |
| 5 | `THEORY/canonical/hypothesis_tree.md` | Insert §C.1 (H-COMP branch); apply §C.2 (HT-3.6 changelog row + next-target line) | §C |
| 6 | `THEORY/canonical/canonical.md` | Apply §A.3.0 (Cat B header hygiene); insert §A.2 (Cat A entries); §A.3 (Cat B entries); §A.4 (§12 Warning); §A.5 (Interpretation) | §A |

After step 6, execute the Block D consistency audit from `02_development.md` §4.2 against the post-patch canonical.

### §F.1 Post-patch invariant verification commands

```bash
# §4.2.1 cardinality invariants
grep -rn "T-CC-StableK-Kernel" THEORY/canonical/  # should return 0 (R-C; CV-1.14 not promoted)
grep -rn "T-ACT-DP" THEORY/canonical/             # should return ≥2 (canonical + theorem_status)
grep -rn "T-ACT-GIBBS" THEORY/canonical/          # should return ≥2
grep -rn "L-ENDPOINT-NONSEMI" THEORY/canonical/    # should return ≥2
grep -rn "OP-0012-SINK" THEORY/canonical/          # should return ≥2 (theorem_status + hypothesis_tree)
grep -rn "Sinkhorn-scaled" THEORY/canonical/       # should return ≥1
grep -rn "action cost" THEORY/canonical/           # should return ≥1
grep -rn "endpoint cost" THEORY/canonical/         # should return ≥1
grep -rn "δ_eff" THEORY/canonical/                 # always qualified by "action direct cost" or "scope"
grep -rn "T-Temporal-Identity" THEORY/canonical/ | wc -l  # should be unchanged from pre-patch + some new cross-references

# §4.2.2 no-double-classification
grep -n "T-ACT-DP" THEORY/canonical/theorem_status.md | wc -l   # exactly 1 (Cat A only)
grep -n "T-ACT-KERNEL-COMP" THEORY/canonical/theorem_status.md | wc -l  # exactly 1 (Cat B only)

# §4.2.3 cross-reference
grep -n "OP-0012-CC" THEORY/canonical/canonical.md  # line 1779 preserved
grep -n "Cat A" THEORY/canonical/CV-1.13_SEAL.md     # T-Temporal-Identity Cat A status preserved

# §4.2.4 hypothesis-tree
grep -n "H-COMP" THEORY/canonical/hypothesis_tree.md  # new branch present
grep -n "HT-3.6" THEORY/canonical/hypothesis_tree.md  # version incremented

# §4.2.5 CHANGELOG ordering
head -5 THEORY/CHANGELOG.md  # CV-1.15 first
```

Each command's expected output is documented inline in `02_development.md` §4.2.

---

## §G. Decision audit trail

| Decision | Source | Rationale |
|---|---|---|
| R-C over R-A | `02_development.md §2.3` | Lightest path; preserves R-A option for follow-up; CV-1.14 audit parity not yet established (OQ-A) |
| R-C over R-B | `02_development.md §2.2 R-B section` | Cat B → Cat C demotion is only because of *cited* lemma non-canonical-status, not weak math; preserve Cat B with explicit conditional |
| S-i over S-ii | `02_development.md §3.4` | Matches CV-1.6 ~ CV-1.13 canonical practice (per-category insertion) |
| S-i over S-iii | `02_development.md §3.3 S-iii` | S-iii (new "Category A.CV-1.15") would proliferate version-named subcategories; no precedent |
| 1.3a deferred | this file §E §12.1 | Internal stylistic only; deferred until T-SINKHORN-PLAN-SEMIGROUP-FAILS gets canonical-theorem promotion (which is OPEN) |
| Interpretation handling: P-ACTION-PATH-INHERITANCE → Cat A insert tail, not counted | this file §A.5 | No precedent for "Interpretive Propositions" subsection (OQ-E open); minimal-precedent-breaking choice |
| All other amendments | this file §E §12.1 | Per-finding from `02_development.md` §1.8 |

---

## §H. What this file does NOT do

Per session prompt §2 (no working/ direct writes):

- This file does **NOT** modify `THEORY/working/CV115_ACTION_TEMPORAL_COST/10_patch_plan.md`.
- This file does **NOT** modify `THEORY/working/CV115_ACTION_TEMPORAL_COST/09_final_audit.md`.
- This file does **NOT** modify any file under `THEORY/canonical/`, `THEORY/working/`, or `CODE/`.

All amendments are *proposal text*. To apply, follow §F apply-order in a P7-authorized turn.

The session has now produced its complete output package: `01_`, `02_`, `03_`, `04_`, `99_` in `THEORY/logs/daily/2026-05-13/`.

---

*End of 04_proposed_amendments.md. This file completes the 2026-05-13 audit session's output.*
