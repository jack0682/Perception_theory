# L1-H: Local-to-Global Barcode Transfer

**File:** `THEORY/working/MF/kbar_kact_bridge_L1H_local_to_global_transfer.md`
**Document type:** non-canonical working theorem candidate + counterexample register
**Created:** 2026-05-02 (after L1-A through L1-G)
**Status:** working; partial theorem with explicit residual proof obligations; not theorem-grade; not Cat-A

---

## 1. Status and Scope

This is a non-canonical working note. It addresses the H10 / PO-6 obligation of L1-F: the local-to-global barcode transfer condition.

L1-H does **not**:

- prove L-1.
- promote L1-F to Cat-A.
- solve OP-0005 or OP-0008.
- claim \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) or \(K_{\mathrm{soft}}=K_{\mathrm{act}}\) globally.
- claim \(\sigma_{\mathrm{rich}}\) sufficiency.
- promote reservoir theory to canonical.
- treat empirical evidence as a theorem.
- modify any canonical or existing working file.

L1-H produces:

- a partial theorem candidate stating \(K_{\mathrm{bar}}^{\ell_{\min}}(U;G)=|A^\varepsilon(\mathbf u)|\) under a sharpened L1Hyp package;
- an explicit derivation of the LG-7 coverage condition from LG-4 (so LG-7 is **not** a circular assumption);
- a residual proof gap concentrated in the per-active-neighborhood at-most-one-dominant-bar step, where bottleneck stability adds a perturbation budget in the wrong direction;
- a finite-graph counterexample register verified numerically by `CODE/scripts/l1h_local_to_global_counterexample.py`.

The conclusion is not a Cat-A theorem. The synthesis identifies which constants need tightening in L1Hyp and which proof obligations must be discharged before any Cat-A upgrade attempt of L1-F.

---

## 2. Task Checklist

- [x] Read L1-G empirical diagnostic and L1-F synthesis.
- [x] Read L1-A through L1-E and the surrounding bridge-lemma / proof-status grounding.
- [x] Re-inspect persistence / diagnostics / k_soft / graph code and the L1-G script.
- [x] Identify "local barcode control" precisely (bars of \(U\) on induced subgraph \(G_j^r\)).
- [x] Identify "global barcode control" precisely (bars of \(U\) on the full graph \(G\)).
- [x] Search for finite-graph counterexamples (path graph, dumbbell + isolated spike).
- [x] Numerically verify CE-1 high-corridor and CE-2 background-spike with `CODE/scripts/l1h_local_to_global_counterexample.py`.
- [x] Determine whether the L1Hyp package as stated in L1-F is sufficient for local-to-global transfer.
- [x] Where insufficient, formulate strengthened conditions LG-1..LG-7.
- [x] Distinguish derivable LG-7 (from LG-4 + terminal-death) from genuinely open per-neighborhood single-dominant-bar count.
- [x] State theorem candidate with explicit per-step proof status.
- [x] Build proof-obligation table.
- [x] Build Cat-status table.
- [x] Preserve all non-claims.
- [x] Verify the script runs and produces the expected counterexample exhibits.
- [x] Verify file creation.

---

## 3. Motivation from L1-G

L1-G classified each L1Hyp clause by empirical measurability and ran the diagnostic on the WQ-LAT lineage:

- H10 was reported `NOT_MEASURABLE_FROM_CURRENT_OUTPUTS` and identified as the central theorem-grade gap.
- The WQ-1 production trajectory (201 snapshots) ended with \(K_{\mathrm{bar}}^{0.10}(U)=1\) and \(K_{\mathrm{act}}^{\varepsilon}(\mathbf u)=3\), exhibiting H8 coverage excess of \(-2\) and falsifying L1Hyp on that trajectory.

The L1-G smoke test additionally found that initial Gaussian configurations satisfy H2 through H9 simultaneously, so the L1Hyp regime is non-vacuous in principle on \(T^2_{20}\). What L1-G did not provide is a theorem stating *under what additional precise conditions* the implication

\[
\text{local active-slot barcode controls}
+
\text{local residual controls}
+
\text{bridge-height bounds}
+
\text{tie-stable association}
\Rightarrow
K_{\mathrm{bar}}^{\ell_{\min}}(U;G)
=
|A^\varepsilon(\mathbf u)|
\]

actually holds. Closing this is L1-H's specific task.

---

## 4. The Local-to-Global Problem

Let \(G=(X,E,w)\) be a finite weighted graph. Let

\[
\mathbf u=(u^{(1)},\dots,u^{(K_{\mathrm{field}})})
\]

be a finite shared-pool multi-formation state. Fix the L1-F constants \(\varepsilon,\ell_{\min},\delta,r\), and define

\[
A=A^\varepsilon(\mathbf u)
=
\{j:m_j(\mathbf u)>\varepsilon\},
\qquad
m_j=\sum_x u^{(j)}(x).
\]

Define the per-slot \(\delta\)-support and active neighborhood:

\[
S_j^\delta=\{x:u^{(j)}(x)>\delta\},
\qquad
N_j^r=\{x\in X:d_G(x,S_j^\delta)\le r\}.
\]

Define the background:

\[
X_{\mathrm{bg}}
=
X\setminus\bigcup_{j\in A}N_j^r.
\]

Define the local induced subgraph \(G_j^r=G[N_j^r]\), the local active aggregate \(U_{\mathrm{act}}=\sum_{j\in A}u^{(j)}\), the inactive residual \(R_{\mathrm{inact}}=\sum_{j\notin A}u^{(j)}\), and the global aggregate

\[
U=U_{\mathrm{act}}+R_{\mathrm{inact}}.
\]

Adopt the terminal-death \(H_0\) superlevel convention of L1-C: every birth-vertex contributes a bar, the surviving component is recorded as `(max U, 0)`. Write

\[
\mathrm{Bars}_0^{\mathrm{term}}(U;G)
\]

for the global barcode of \(U\) on \(G\), and

\[
\mathrm{Bars}_0^{\mathrm{term}}(U|_{N_j^r};G_j^r)
\]

for the local barcode of \(U\) restricted to vertices in \(N_j^r\) on the induced subgraph \(G_j^r\). The hard-bar count is

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U;G)
=
\#\{B\in\mathrm{Bars}_0^{\mathrm{term}}(U;G):\ell(B)\ge\ell_{\min}\}.
\]

**Critical structural fact.** The global barcode of \(U\) is **not** the disjoint union of local barcodes. Concretely:

- Bars born in \(N_j^r\) can have global death levels strictly **lower** than their local death levels because globally a component can leak through \(\partial N_j^r\) into \(X_{\mathrm{bg}}\) before reaching its local merge inside \(N_j^r\). Global bar lengths can therefore be **longer** than the corresponding local bar lengths.
- Bars can be born in \(X_{\mathrm{bg}}\) when no active neighborhood-local barcode contains them.
- The global terminal bar is always exactly one bar with death \(d=0\); it is associated with the *oldest* birth vertex by elder rule, regardless of where it was born locally.

So a naive identification "global barcode = sum of local barcodes" is forbidden. L1-H gives sufficient conditions under which the *count* (not the multiset) agrees on the dominant-bar threshold \(\ell_{\min}\).

---

## 5. Minimal Counterexamples and Why Local Data Is Insufficient

The following finite-graph exhibits were constructed in `CODE/scripts/l1h_local_to_global_counterexample.py` and the global / local terminal-death barcodes were computed numerically. All numbers below are verified, not estimated.

### CE-1 — High corridor merge

**Graph.** Path \(0-1-2-3-4\). Active neighborhoods \(N_1=\{0,1\}\), \(N_2=\{3,4\}\), background \(X_{\mathrm{bg}}=\{2\}\).

**High-corridor variant.** \(U=(1.0,0.5,0.95,0.5,1.0)\).

| Object | \(K_{\mathrm{bar}}^{0.10}\) | Bars (length) |
|---|---|---|
| Local on \(N_1\) | 1 | terminal length 1.0 |
| Local on \(N_2\) | 1 | terminal length 1.0 |
| Global | **3** | terminal 1.0; finite 0.50 (\(p_2\) dies at 0.5); finite **0.45 born at the corridor** (\(b=0.95,\,d=0.5\)) |

The corridor vertex \(x=2\) is in \(X_{\mathrm{bg}}\) and has \(U(2)=0.95\ge\ell_{\min}\). It produces an extra global bar of length \(0.45\). Defeated by **LG-4** (background suppression).

**Low-corridor variant.** \(U=(1.0,0.5,0.05,0.5,1.0)\).

| Object | \(K_{\mathrm{bar}}^{0.10}\) | Bars (length) |
|---|---|---|
| Local on \(N_1\) | 1 | terminal length 1.0 |
| Local on \(N_2\) | 1 | terminal length 1.0 |
| Global | **2** | terminal 1.0; finite 0.95 |

LG-4 holds (\(U(2)=0.05<\ell_{\min}\)); global \(K_{\mathrm{bar}}\) matches sum of local dominant bars.

**Lesson.** LG-4 is necessary. The high-corridor regime is the L1F-F2 / L1H-F2 failure mode realized concretely.

### CE-2 — Background dominant residual on a dumbbell

**Graph.** Vertices \(0,\dots,6\). Edges \((0,1),(1,2),(2,3),(3,4),(4,5),(3,6)\). \(N_A=\{0,1\},N_B=\{4,5\}\); \(X_{\mathrm{bg}}=\{2,3,6\}\).

**\(U\).** \((1.0,0.9,0.05,0.05,0.9,1.0,\mathbf{0.5})\) — vertex 6 carries an isolated background spike of height \(0.5\).

| Object | \(K_{\mathrm{bar}}^{0.10}\) |
|---|---|
| Local on \(N_A\) | 1 (terminal length 1.0) |
| Local on \(N_B\) | 1 (terminal length 1.0) |
| Global | **3** (terminal 1.0; finite ≈0.95; finite 0.45 born at vertex 6) |

LG-4 fails because \(U(6)=0.5\ge\ell_{\min}\). Defeated by **LG-4**. Realises the L1H-F3 background-bar failure mode.

### CE-3 — Local secondary near \(\ell_{\min}\), perturbation-defeated

**Graph.** Path \(0-1-2-3-4\), single active slot.

**Slot field \(u^{(j)}\).** \((1.0,0.5,0.4,0.5,0.55)\). Slot-internal \(\ell_{j,2}=0.150\) (numerically verified).

**Perturbation.** \(\rho_{\mathrm{pert}}\)-targeted residual `(0,0,0,0,0.04)`. Resulting \(U=(1.0,0.5,0.4,0.5,0.59)\). \(\ell_{j,2}\) on \(U\) is \(\mathbf{0.190}\) — increased by \(0.04\) in the **wrong direction** relative to \(\ell_{\min}\).

**Lesson.** Bottleneck-stability for \(H_0\) gives \(|\ell_{j,2}(U)-\ell_{j,2}(u^{(j)})|\le 2\rho_{\mathrm{pert}}\). The numerical exhibit shows the perturbation can **enlarge** the secondary bar. So H6 (slot-internal secondary suppression \(\ell_{j,2}\le\ell_{\min}-\rho_{\mathrm{pert}}\)) is *not* preserved under residual perturbation by \(\rho_{\mathrm{pert}}/2\); we need

\[
\ell_{j,2}(u^{(j)})\le\ell_{\min}-3\rho_{\mathrm{pert}}
\]

(a 1-buffer plus 2 from bottleneck) for the perturbed-secondary to remain below \(\ell_{\min}\). This is the **constant-tightening obligation** for the upper bound; it is the residual gap of L1-H.

### CE-4 — Terminal-bar reassignment under equal peaks

**Graph.** Path 5, \(U=(1.0,0.5,0.05,0.5,1.0)\). Two equal-height peaks.

| Object | \(K_{\mathrm{bar}}^{0.10}\) |
|---|---|
| Global | 2 (terminal length 1.0; finite 0.95) |

The terminal bar is assigned to one of the two peaks by elder rule (index-tiebreak in the code). The *count* is unchanged. CE-4 is **not** a counterexample to the count theorem; it documents that LG-6 (elder-rule compatibility) is required to make the bar-to-slot assignment well-defined when peaks tie.

### Summary of CE roles

CE-1 motivates LG-4. CE-2 motivates LG-4. CE-3 motivates the H6 tightening. CE-4 motivates LG-6 (label only, not count).

The script output is at `CODE/scripts/results/l1h_counterexample.json`.

---

## 6. Required Strengthening Conditions

The following conditions are the L1-H strengthening on top of L1Hyp.

**LG-1 — disjoint active neighborhoods.**

\[
N_j^r\cap N_k^r=\emptyset\qquad (j\neq k\in A).
\]

This rules out double-counting of vertices and lets the perturbation argument treat \(R_j=\sum_{k\neq j}u^{(k)}\) as a small additive in \(N_j^r\).

**LG-2 — low boundary collar.**

\[
\max_{x\in\partial N_j^r}U(x)
\le
B_{\partial,j}
\le
b_j-\ell_{\min}-r_{\mathrm{assoc}}.
\]

Boundary vertices of \(N_j^r\) have \(U\) values low enough that, before threshold drops to \(B_{\partial,j}\), no boundary vertex has been admitted to the filtration. The \(p_j\) component grows entirely inside \(N_j^r\) until then, accumulating at least \(\ell_{\min}+r_{\mathrm{assoc}}\) of persistence.

**LG-3 — low inter-neighborhood bridge.** For each active pair,

\[
\theta_{\mathrm{bridge}}^{jk}(U)
\le
B_{jk}
\le
\min(b_j,b_k)-\ell_{\min}-r_{\mathrm{assoc}}.
\]

Two active components cannot merge until threshold drops far enough that both have already accumulated \(\ge\ell_{\min}\) persistence.

**LG-4 — background suppression on \(U\) (not just on \(R_{\mathrm{inact}}\)).**

\[
\|U\|_{\infty,X_{\mathrm{bg}}}
\le
\ell_{\min}-\rho_{\mathrm{bg}}.
\]

This is **stronger** than L1-E IS-H1 on \(R_{\mathrm{inact}}\) alone, because \(U=U_{\mathrm{act}}+R_{\mathrm{inact}}\) and active tails leak into \(X_{\mathrm{bg}}\). Active-slot decay must combine with residual suppression to give \(U|_{X_{\mathrm{bg}}}<\ell_{\min}-\rho_{\mathrm{bg}}\).

**LG-5 — boundary tie margin.**

\[
\min_{v_1,v_2\in V_{\mathrm{relevant}}}|v_1-v_2|\ge\tau_{\mathrm{tie}}>0,
\]

where \(V_{\mathrm{relevant}}\) is the set of birth heights \(b_j\), boundary collar values \(B_{\partial,j}\), bridge heights \(\theta_{\mathrm{bridge}}^{jk}\), the threshold \(\ell_{\min}\), and the dominant-bar lengths.

**LG-6 — elder-rule compatibility.** Birth representatives \(p_j\) satisfy a deterministic ordering rule (lexicographic on \(X\) under tie of \(U(p_j)\)) so that the global terminal bar is assigned to a definite active neighborhood. Equivalent statement: under the chosen tie convention, the union-find merge sequence is deterministic given \(U\) and \(G\).

**LG-7 — coverage of dominant bars by active neighborhoods.**

> Every global bar of length \(\ge\ell_{\min}\) has its birth vertex inside \(\bigcup_{j\in A}N_j^r\).

LG-7 is **not** assumed; it is a *derived consequence* of LG-4 plus the terminal-death convention. The derivation is given in §7.B and §8 step (α). Stating LG-7 here is for clarity; using it as an axiom would be circular and is explicitly avoided in the proof skeleton.

---

## 7. Local-to-Global Transfer Theorem Candidate

This section states the theorem candidate, lists its conditions, and **separates** the part that follows from LG-4 alone (LG-7) from the part that requires the full set LG-1..LG-6 plus a tightened H6.

### 7.A. Theorem candidate

**L1-H Theorem Candidate — Local-to-Global Dominant-Bar Transfer.**
Let \(G=(X,E,w)\) be a finite weighted graph and \(\mathbf u\) a finite shared-pool multi-formation state. Suppose:

1. L1-F's working hypotheses H1-H4 (active mass, support, peak height, persistence margin) and L1-D's H6 hold for \(u^{(j)}\) on \(G\) **with the tightened secondary-bar bound**

   \[
   \ell_{j,2}(u^{(j)};G)\le\ell_{\min}-3\rho_{\mathrm{pert}}
   \quad\forall j\in A,
   \]
2. LG-1, LG-2, LG-3, LG-4, LG-5, LG-6 hold,
3. the terminal-death \(H_0\) convention is used throughout,
4. \(h_{\min}\ge\ell_{\min}\) (so the terminal bar is itself dominant).

Then

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U;G)
=
|A^\varepsilon(\mathbf u)|
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

**Status.** LEMMA-CAND with one residual proof obligation (PO-LH1, see §8 step (β)). The lower bound \(K_{\mathrm{bar}}\ge|A|\) is proof-grade modulo standard tie handling. The upper bound \(K_{\mathrm{bar}}\le|A|\) reduces to two sub-claims:

- (α) any dominant global bar has its birth vertex inside \(\bigcup_j N_j^r\) — **proof-grade** under LG-4 and terminal-death.
- (β) each \(N_j^r\) contributes at most one dominant global bar — **partial proof**: it requires the perturbation propagation
  \[
  \ell_{j,2}(U;G)\le\ell_{j,2}(U|_{N_j^r};G_j^r)\le\ell_{j,2}(u^{(j)};G_j^r)+2\rho_{\mathrm{pert}}\le\ell_{j,2}(u^{(j)};G)+\text{boundary leakage correction}+2\rho_{\mathrm{pert}},
  \]
  where each inequality uses bottleneck stability or LG-2 boundary control. The boundary-leakage correction is the residual obligation; CE-3 demonstrates that without the H6 tightening to \(\ell_{\min}-3\rho_{\mathrm{pert}}\) the chain can fail by exactly one perturbation budget.

### 7.B. Why LG-7 is derivable, not assumed

The desired claim "every dominant global bar has birth vertex in \(\bigcup_jN_j^r\)" follows directly from LG-4 and terminal-death convention without invoking any property of the local barcodes:

> **Lemma (LG-7 derivation).** Under terminal-death \(H_0\) on a finite graph and LG-4, every \(B\in\mathrm{Bars}_0^{\mathrm{term}}(U;G)\) with \(\ell(B)\ge\ell_{\min}\) has a birth vertex \(v_B\) with \(v_B\notin X_{\mathrm{bg}}\), hence \(v_B\in\bigcup_{j\in A}N_j^r\).
>
> **Proof.** A bar in superlevel \(H_0\) is \([d_B,b_B]\) with \(b_B=U(v_B)\) for the birth vertex \(v_B\) and \(d_B\ge 0\) under terminal-death. Length \(\ell(B)=b_B-d_B\le b_B\). If \(\ell(B)\ge\ell_{\min}\) then \(b_B\ge\ell_{\min}\), so \(U(v_B)\ge\ell_{\min}\). LG-4 says \(U(x)\le\ell_{\min}-\rho_{\mathrm{bg}}<\ell_{\min}\) for every \(x\in X_{\mathrm{bg}}\). Hence \(v_B\notin X_{\mathrm{bg}}\). \(\square\)

This is the LG-7 condition stated as a derived consequence rather than an axiom. The user instruction to **not hide circularity** is honored: LG-7 is *not* assumed; the theorem candidate is built from LG-1..LG-6 (plus L1Hyp) and LG-7 is recovered as a step inside the proof.

### 7.C. What is *not* derivable from LG-1..LG-6

The remaining proof obligation **PO-LH1** is per-neighborhood at-most-one-dominant-bar. As CE-3 shows, the bottleneck stability bound

\[
|\ell_{j,2}(U;G_j^r)-\ell_{j,2}(u^{(j)};G_j^r)|\le 2\rho_{\mathrm{pert}}
\]

adds the perturbation in the *unfavorable* direction. This is not circular — it is a quantitative gap. The proof closes if H6 is sharpened to

\[
\ell_{j,2}(u^{(j)})\le\ell_{\min}-3\rho_{\mathrm{pert}}
\]

and a separate argument (using LG-2 boundary collar and LG-1 disjointness) shows that the local-on-\(G_j^r\)-to-global-on-\(G\) inclusion does not *further* enlarge \(\ell_{j,2}\). The local-on-\(G_j^r\)-to-global step is the genuine residual gap.

This gap is **not** equivalent to LG-7. It concerns the lengths of secondary local-born bars under the local-to-global subgraph passage, not the location of dominant bar births.

---

## 8. Proof Skeleton

### Step 0 — set up

Let \(A=A^\varepsilon(\mathbf u)\). Goal: show \(K_{\mathrm{bar}}^{\ell_{\min}}(U;G)=|A|\).

Split into

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U;G)\ge |A|
\quad\text{and}\quad
K_{\mathrm{bar}}^{\ell_{\min}}(U;G)\le |A|.
\]

### Step 1 — order of vertex entry under the filtration

The terminal-death \(H_0\) superlevel filtration adds vertices in nonincreasing order of \(U(x)\). Under LG-2 every vertex \(v\in\bigcup_jN_j^r\) with \(U(v)>B_{\partial,j_v}\) (where \(j_v\) is the unique neighborhood containing \(v\), well-defined by LG-1) enters before the boundary vertex of its neighborhood. Under LG-4 every vertex of \(X_{\mathrm{bg}}\) enters at threshold \(\le\ell_{\min}-\rho_{\mathrm{bg}}<B_{\partial,j}\) for every active \(j\) (assuming the typical regime \(B_{\partial,j}>\ell_{\min}\)).

Consequence: as \(\theta\) decreases from \(b_j\) toward \(B_{\partial,j}\), the active component of \(p_j\) is grown entirely inside \(N_j^r\). At \(\theta=B_{\partial,j}\), boundary vertices admit and the component can leak. Below \(\ell_{\min}-\rho_{\mathrm{bg}}\), background vertices admit.

### Step 2 — lower bound \(K_{\mathrm{bar}}\ge|A|\)

For each \(j\in A\):

- \(p_j\) is born at threshold \(b_j\ge h_{\min}\ge\ell_{\min}\).
- \(p_j\)-component grows through \(N_j^r\) interior; cannot merge with any other active component or background until threshold drops below \(\min(B_{\partial,j},\theta_{\mathrm{bridge}}^{jk})\le b_j-\ell_{\min}-r_{\mathrm{assoc}}\) (LG-2 + LG-3).
- Hence \(p_j\)'s component has at least \(\ell_{\min}+r_{\mathrm{assoc}}\) persistence before its first inter-component merge. Bar length \(\ge\ell_{\min}\).

The terminal bar is one such: under elder rule (LG-6) one of the active births survives to \(d=0\) with length \(b_{\mathrm{oldest}}\ge h_{\min}\ge\ell_{\min}\). The other \(|A|-1\) active births die at their respective merges, each with length \(\ge\ell_{\min}\). So at least \(|A|\) bars of length \(\ge\ell_{\min}\) exist. \(\square\) (proof-grade)

### Step 3 — upper bound \(K_{\mathrm{bar}}\le|A|\), part (α) coverage

Goal: every dominant global bar has birth vertex in some \(N_j^r\).

This is the LG-7 derivation in §7.B: under terminal-death, length \(\ge\ell_{\min}\Rightarrow\) birth height \(\ge\ell_{\min}\Rightarrow\) birth vertex outside \(X_{\mathrm{bg}}\). Combined with \(X=X_{\mathrm{bg}}\sqcup\bigcup_jN_j^r\) (which uses LG-1 to make \(\bigcup_jN_j^r\) a disjoint union), the birth vertex lies in exactly one \(N_j^r\). \(\square\) (proof-grade, given LG-1, LG-4, terminal-death)

### Step 4 — upper bound \(K_{\mathrm{bar}}\le|A|\), part (β) per-neighborhood single-bar

Goal: for each \(j\in A\), at most one global bar with birth in \(N_j^r\) has length \(\ge\ell_{\min}\).

Proof attempt:

- Slot-internal: H6 tightened gives \(\ell_{j,2}(u^{(j)};G)\le\ell_{\min}-3\rho_{\mathrm{pert}}\). In particular \(\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}\) (restricting to \(G_j^r\) cannot increase any bar length under terminal-death, since restriction can only break components earlier and shorten bars, **but** the surviving terminal bar of the restriction has death \(0\) at the local terminal level; the maximum length of the surviving bar on \(G_j^r\) is at most \(\max_{N_j^r}U\), unchanged from \(G\)).
- Aggregate perturbation: \(U|_{G_j^r}=u^{(j)}|_{G_j^r}+R_j|_{N_j^r}\) where \(R_j=\sum_{k\neq j}u^{(k)}\). Under LG-1 (disjoint neighborhoods) the contribution from other active slots on \(N_j^r\) is small; under LG-4 (background suppression on \(U\)) the residual is small on \(N_j^r\) too if active tails don't accumulate. Thus \(\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2\).
- Bottleneck stability: \(|\ell_{j,2}(U;G_j^r)-\ell_{j,2}(u^{(j)};G_j^r)|\le 2\rho_{\mathrm{pert}}\).
  Combining: \(\ell_{j,2}(U;G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}+2\rho_{\mathrm{pert}}=\ell_{\min}-\rho_{\mathrm{pert}}<\ell_{\min}\).
- **Local-to-global subgraph passage (residual obligation, PO-LH1).** A secondary global bar with birth in \(N_j^r\) corresponds to some local secondary bar on \(G_j^r\), but the global death level may differ from the local death level by the boundary-leakage event. CE-3 plus the LG-2 collar argument suggests global death \(\le\) local death (death happens earlier or equal globally), hence global bar length \(\ge\) local bar length. So a global secondary bar of length \(\ell\) corresponds to a local secondary bar of length \(\le\ell\). The implication chain
  \[
  \ell_{j,2}(\text{global on }G)
  \le
  \ell_{j,2}(\text{local on }G_j^r)+\text{boundary-correction}
  \]
  is the residual obligation. If the boundary correction can be shown to be at most some \(\rho_{\partial}\) and absorbed into \(\rho_{\mathrm{pert}}\) in H6 tightening, the proof closes.

Status: **PO-LH1 is the L1-H residual obligation**. Without it, the upper bound is a strong sketch but not theorem-grade.

### Step 5 — combine

Steps 2 and (3+4) give \(|A|\le K_{\mathrm{bar}}^{\ell_{\min}}(U;G)\le |A|\), i.e. equality. \(\square\) (modulo PO-LH1)

---

## 9. Counterexample Register

| Counterexample | Shows | Defeated by | Status (in script) |
|---|---|---|---|
| CE-1 high-corridor (path 5, \(U(2)=0.95\)) | Background corridor with high \(U\) creates extra global dominant bar | LG-4 | numerically verified, \(K_{\mathrm{bar}}^{\mathrm{global}}=3\) vs sum local \(=2\) |
| CE-1 low-corridor (path 5, \(U(2)=0.05\)) | Same configuration with \(X_{\mathrm{bg}}<\ell_{\min}\) does not break | LG-4 holds | numerically verified, \(K_{\mathrm{bar}}^{\mathrm{global}}=2\) |
| CE-2 background spike (dumbbell with \(U(6)=0.5\)) | Isolated \(X_{\mathrm{bg}}\) vertex with \(U\ge\ell_{\min}\) creates extra finite bar | LG-4 | numerically verified, \(K_{\mathrm{bar}}^{\mathrm{global}}=3\) |
| CE-3 perturbation-boost of secondary | Aggregate perturbation can increase \(\ell_{j,2}\) — bottleneck stability is one-sided in the wrong direction | H6 must be tightened to \(\ell_{\min}-3\rho_{\mathrm{pert}}\); PO-LH1 boundary correction | numerically verified, \(\ell_{j,2}\) goes from \(0.150\) to \(0.190\) |
| CE-4 elder-rule reassignment | Equal peaks; terminal bar assigned to one by index tiebreak | LG-6 (count unchanged) | numerically verified, \(K_{\mathrm{bar}}=2\) |

The script `CODE/scripts/l1h_local_to_global_counterexample.py` writes its full output to `CODE/scripts/results/l1h_counterexample.json`. All values above are computed with the same terminal-death \(H_0\) union-find as `scc.diagnostics._persistence_h0_graph`.

---

## 10. Constants and Compatibility

| Constant | Meaning | Required relation | Source |
|---|---|---|---|
| \(\varepsilon\) | active mass threshold | \(j\in A\iff m_j>\varepsilon\) | L1-F H1 |
| \(\delta\) | active support threshold | \(S_j^\delta=\{u^{(j)}>\delta\}\) | L1-F H1 |
| \(r\) | active neighborhood radius | \(N_j^r=\{x:d_G(x,S_j^\delta)\le r\}\) | L1-F H6 |
| \(\ell_{\min}\) | dominant bar threshold | bar counted iff \(b-d\ge\ell_{\min}\) | L1-F |
| \(h_{\min}\) | minimum active birth/peak height | \(b_j\ge h_{\min}\ge\ell_{\min}\) | L1-F H2 + L1-H lower bound |
| \(B_{jk}\) | inter-neighborhood bridge bound | \(\theta_{\mathrm{bridge}}^{jk}\le B_{jk}\le\min(b_j,b_k)-\ell_{\min}-r_{\mathrm{assoc}}\) | L1-F H3 + L1-H LG-3 |
| \(B_{\partial,j}\) | boundary-collar bound | \(\max_{\partial N_j^r}U\le B_{\partial,j}\le b_j-\ell_{\min}-r_{\mathrm{assoc}}\) | L1-H LG-2 (new) |
| \(r_{\mathrm{assoc}}\) | contact-to-death / elder-rule error | absorbed into B-bounds | L1-F H4 |
| \(r_{\mathrm{birth}}\) | peak-to-birth representative error | absorbed into b-bounds | L1-F H4 |
| \(\rho_{\mathrm{pert}}\) | active secondary-bar perturbation budget | \(\ell_{j,2}(u^{(j)})\le\ell_{\min}-3\rho_{\mathrm{pert}}\) (tightened from L1-D), \(\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2\) | L1-H H6 tightening (new) |
| \(\rho_{\mathrm{res}}\) | inactive residual margin | \(\|R_{\mathrm{inact}}\|_\infty\le\ell_{\min}-\rho_{\mathrm{res}}\) | L1-F H7 |
| \(\rho_{\mathrm{bg}}\) | background-on-\(U\) margin | \(\|U\|_{\infty,X_{\mathrm{bg}}}\le\ell_{\min}-\rho_{\mathrm{bg}}\) | L1-H LG-4 (new) |
| \(\tau_{\mathrm{tie}}\) | tie / plateau stability margin | birth/death/threshold values separated by \(\tau_{\mathrm{tie}}\) | L1-F H9 + L1-H LG-5 |

Core compatibility inequalities (all required for the theorem candidate):

\[
h_{\min}-\max_{k\neq j}B_{jk}
\ge
\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}}.
\]

\[
h_{\min}-B_{\partial,j}
\ge
\ell_{\min}+r_{\mathrm{assoc}}.
\]

\[
\|U\|_{\infty,X_{\mathrm{bg}}}
\le
\ell_{\min}-\rho_{\mathrm{bg}}.
\]

\[
\ell_{j,2}(u^{(j)})
\le
\ell_{\min}-3\rho_{\mathrm{pert}}.
\]

\[
\|R_j\|_{\infty,N_j^r}
\le
\rho_{\mathrm{pert}}/2.
\]

\[
B_{\partial,j}\ge\ell_{\min}-\rho_{\mathrm{bg}}\quad(\text{usual regime, ensures correct entry order}).
\]

The constants compatibility study (whether all of the above admit a non-empty regime) is L1-I.

---

## 11. Failure Modes

### L1H-F1 — Local barcode illusion

Local bars on \(G_j^r\) look correct in number and length, but the global barcode on \(G\) differs because of inter-neighborhood merging or background inclusion. CE-1 high-corridor and CE-2 are realizations.

### L1H-F2 — High corridor

\(\theta_{\mathrm{bridge}}^{jk}(U)\) is high, pairwise active components merge before accumulating \(\ell_{\min}\) persistence; or, the corridor itself contributes a global birth.

### L1H-F3 — Background dominant bar

Some \(x\in X_{\mathrm{bg}}\) has \(U(x)\ge\ell_{\min}\); LG-4 fails; an extra global terminal or finite bar is created.

### L1H-F4 — Elder-rule reassignment

Equal birth heights or unstable tiebreak change the slot \(\to\) bar assignment without changing \(K_{\mathrm{bar}}\). LG-6 controls labeling but is irrelevant for the count.

### L1H-F5 — Boundary collar too high

LG-2 fails: \(\partial N_j^r\) admits to the filtration before the slot has accumulated \(\ell_{\min}\) of internal persistence. The active component leaks early and the lower-bound argument fails.

### L1H-F6 — Overlapping neighborhoods

LG-1 fails: \(N_j^r\cap N_k^r\neq\emptyset\). Vertices are double-counted, perturbation \(R_j\) on \(N_j^r\) is no longer small.

### L1H-F7 — Coverage assumption circularity

Treating LG-7 as an *assumption* rather than a derivation would make the theorem candidate near-tautological: assume coverage \(\Rightarrow\) coverage holds. L1-H avoids this by deriving LG-7 from LG-4 + terminal-death (§7.B). Failure of this derivation would correspond to dropping LG-4 or losing the terminal-death convention.

### L1H-F8 — Tie / plateau instability

Equal vertex values can change birth/death pairing or which component carries the terminal bar. LG-5 (positive tie margin) is required; L1G-F4 in L1-G observed that the script's index-stable tiebreak is deterministic but not field-natural.

### L1H-F9 — Perturbation goes the wrong way (CE-3)

Bottleneck stability gives \(|\ell_{j,2}(U)-\ell_{j,2}(u^{(j)})|\le 2\rho_{\mathrm{pert}}\), so a perturbation can *increase* \(\ell_{j,2}\). The H6 condition stated in L1-D / L1-F is \(\ell_{j,2}\le\ell_{\min}-\rho_{\mathrm{pert}}\); after perturbation this may give \(\ell_{j,2}\le\ell_{\min}+\rho_{\mathrm{pert}}\), which is **above** \(\ell_{\min}\). H6 must be tightened to \(\ell_{\min}-3\rho_{\mathrm{pert}}\) (1 buffer + 2 from bottleneck) for the closure.

### L1H-F10 — Local-to-global subgraph passage gap (PO-LH1)

The genuine residual proof gap. Bottleneck stability bounds \(\ell_{j,2}\) on \(G_j^r\); we need a bound on the corresponding bar in the global \(G\)-barcode. CE-3 demonstrates the perturbation effect; the boundary-leakage correction term remains to be quantified.

---

## 12. Cat-Status Table

| Item | Status | Reason | Upgrade requirement |
|---|---|---|---|
| Local neighborhood \(N_j^r\) | DEF | exact once \(j\), \(\delta\), \(r\) fixed | none |
| Background \(X_{\mathrm{bg}}\) | DEF | complement of \(\bigcup_jN_j^r\) | none |
| Local barcode on \(G_j^r\) | DEF | terminal-death \(H_0\) on induced subgraph | tie convention |
| Global barcode on \(G\) | DEF | terminal-death \(H_0\) on full graph | tie convention |
| "global barcode = union of local barcodes" | FORBIDDEN | global barcode is not the disjoint union of local barcodes; CE-1, CE-2 give explicit counterexamples | never; only the count agrees, and only under L1-H conditions |
| LG-1 disjoint neighborhoods | WORKING-DEF | structural separation; verifiable | none |
| LG-2 low boundary collar | WORKING-DEF / LEMMA-CAND | sufficient for entry-order argument | derive from primitive support / decay assumptions |
| LG-3 low inter-neighborhood bridge | LEMMA-CAND | inherited from L1-B + L1-F H3; cut existence still open | L1-B / L1-F |
| LG-4 background \(U\) suppression | WORKING-DEF | strictly stronger than L1-E IS-H1 on \(R_{\mathrm{inact}}\) | derive from active-tail decay + residual bound |
| LG-5 boundary tie margin | WORKING-DEF | structural; small perturbation gives \(\tau_{\mathrm{tie}}>0\) generically | formal tie convention |
| LG-6 elder-rule compatibility | WORKING-DEF / CODE-ALIGNED | index-stable tiebreak is deterministic | mathematical tie convention |
| LG-7 coverage of dominant bars | DERIVED LEMMA (not axiom) | follows from LG-4 + terminal-death (§7.B) | none — but only because LG-4 is assumed |
| L1-H theorem candidate | LEMMA-CAND | lower bound proof-grade; upper bound proof-grade modulo PO-LH1 | discharge PO-LH1 (boundary-leakage correction) |
| Lower bound \(K_{\mathrm{bar}}\ge|A|\) | PROOF-GRADE (under LG-1, LG-2, LG-3, LG-6, terminal-death, \(h_{\min}\ge\ell_{\min}\)) | step 2 of skeleton | none |
| Upper bound \(K_{\mathrm{bar}}\le|A|\), part (α) | PROOF-GRADE (under LG-1, LG-4, terminal-death) | LG-7 derivation | none |
| Upper bound \(K_{\mathrm{bar}}\le|A|\), part (β) | PARTIAL PROOF | bottleneck stability + tightened H6 + boundary correction | discharge PO-LH1 |
| Tightened H6 \(\ell_{j,2}\le\ell_{\min}-3\rho_{\mathrm{pert}}\) | WORKING-DEF (new) | required by perturbation accounting in CE-3 | replace with primitive geometric assumption |
| L1-F upper-bound proof using L1-H | CONDITIONAL on PO-LH1 | strengthens L1-F H8 from assumption to derivation in part | discharge PO-LH1 |
| Constants compatibility (regime feasibility) | OPEN | depends on graph + dynamics + initialization | L1-I |
| L1-F Cat-A upgrade | BLOCKED | requires PO-LH1 (this) + L1-I (constants) | sequence L1-H \(\to\) L1-I \(\to\) L1-J |
| Global \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) | FORBIDDEN | conditional only | state under L1-H + L1-I + tightened H6 |
| Global \(K_{\mathrm{soft}}=K_{\mathrm{act}}\) | FORBIDDEN | additionally requires \(\Phi_{\mathrm{res}}\) and remains approximate | unchanged |

---

## 13. Relationship to L1-F

L1-H targets L1-F's H10 / PO-6 obligation.

L1-F's upper-bound proof (\(K_{\mathrm{bar}}\le K_{\mathrm{act}}\)) was conditional on:

- H8 coverage (every dominant bar in \(\mathrm{Image}(\mathcal A_{\mathrm{bar}})\)) — assumed.
- H10 local-to-global compatibility — open.

L1-H provides:

- a **derivation** of LG-7 (the coverage statement at the level of birth-vertex location) from LG-4 + terminal-death, replacing the H8 assumption with a derivation **in the part (α) of upper bound**.
- a **partial** discharge of H10 via the proof skeleton in §8, with one residual obligation PO-LH1 concerning boundary-leakage in the \(G_j^r\to G\) passage.
- an explicit constant-tightening of H6 to \(\ell_{\min}-3\rho_{\mathrm{pert}}\), motivated by CE-3.

L1-F's status is **not promoted** by L1-H. L1-H reduces L1-F's open obligations from {bridge-cut existence, H5 association, H8 coverage, H10 transfer, constants compatibility} to {bridge-cut existence, H5 association (only the labeling part, count is now derived), PO-LH1 boundary correction, constants compatibility}.

A Cat-A upgrade attempt (L1-J) still requires:

- PO-1 bridge-cut existence from primitive SCC field conditions.
- PO-LH1 boundary correction.
- L1-I constants feasibility.
- formal tie convention (LG-5 / LG-6).

---

## 14. Relationship to OP-0005 / OP-0008

### OP-0005 (K-Selection)

L1-H does **not** solve K-selection. It clarifies the conditions under which the field-native morphology count \(K_{\mathrm{bar}}^{\ell_{\min}}(U)\) and the chart-active count \(K_{\mathrm{act}}^{\varepsilon}(\mathbf u)\) agree on a given configuration. This is a *bridge*, not a *selection mechanism*. The reservoir-effective rank reformulation of OP-0005 (§11.2 of `latent_index_space_design.md`) remains a working subprogram.

### OP-0008 (\(\sigma^A\) K-jump inheritance)

L1-H does **not** solve \(\sigma\)-inheritance. It does help define when bar-death events correspond to active-slot events (a global merge between two active components is a bar-death; under L1-H conditions this corresponds to one of \(|A|\to|A|-1\)). This may later support OP-0008 analysis but does not establish \(\sigma_{\mathrm{rich}}\) sufficiency or deterministic \(\Phi_{\mathrm{rich}}\).

No \(\sigma_{\mathrm{rich}}\) sufficiency claim is licensed by L1-H.

---

## 15. Next Work Packages

### L1-I — Constants Feasibility Study (recommended next)

Test whether the L1-H constants admit a non-empty regime on canonical configurations. Specifically check:

- on the L1-G smoke-test snapshot \(\tau=0\), with \(b_j\approx 1\), \(B_{\partial,j}\) measured on the actual \(N_j^r\), \(\ell_{\min}=0.1\), \(\rho_{\mathrm{pert}}\) measured from \(\|R_j\|_{\infty,N_j^r}\), do all of LG-2, LG-3, LG-4 and the tightened H6 hold simultaneously?
- vary \(\sigma_b\), \(r\), \(\delta\) to find the largest regime that satisfies all of L1-H simultaneously.
- examine whether the WQ-LAT-1 LAT-A control configuration (frozen extras) sits inside the L1-H regime.

L1-I gives empirical and parameter-feasibility evidence supporting (or falsifying) the regime assumption.

### L1-H2 — Boundary-leakage correction proof (PO-LH1)

Discharge the residual proof obligation. Two paths:

1. directly bound \(\ell_{j,2}\) on \(G\) from \(\ell_{j,2}\) on \(G_j^r\) using the LG-2 collar (showing global death \(\le\) local death by at most \(\rho_\partial\), and identifying \(\rho_\partial\le\rho_{\mathrm{pert}}\) from the boundary-value bound).
2. give a counterexample (perhaps an extension of CE-3 with a more elaborate boundary that demonstrably enlarges \(\ell_{j,2}\) globally beyond \(\ell_{\min}\)) showing PO-LH1 is unprovable from LG-1..LG-6 alone.

### L1-G2 — Full-state trajectory rerun (optional, supports L1-I)

Refactor `wq_lat1_reservoir_resolution_sweep.py` to optionally save per-snapshot fields. Then L1-G summary mode can run on the LAT-A / LAT-C lineage without rerun, supporting L1-I parameter-feasibility analysis.

### L1-J — Cat-A upgrade attempt

Defer until L1-H2 closes PO-LH1, L1-I confirms a non-empty regime, and PO-1 (bridge-cut existence from primitive SCC) is also addressed. L1-H alone does not unblock L1-J.

---

## 16. Summary

- Local barcode control alone is **insufficient**. Two finite-graph counterexamples (CE-1 high corridor and CE-2 background spike) demonstrate concretely that \(\mathrm{Bars}_0^{\mathrm{term}}(U;G)\) is not the disjoint union of local barcodes.
- Strengthened conditions LG-1 (disjoint neighborhoods), LG-2 (low boundary collar), LG-3 (low inter-neighborhood bridge), LG-4 (background suppression on \(U\)), LG-5 (tie margin), LG-6 (elder-rule compatibility) are required.
- LG-7 (coverage of dominant bars by active neighborhoods) is **not assumed**. It follows from LG-4 + terminal-death via the lemma in §7.B. Treating LG-7 as an axiom would be circular; treating it as a derived consequence is the honest move and is what L1-H does.
- The genuinely open part of the upper bound is **PO-LH1**: the local-to-global subgraph passage for secondary bars. Bottleneck stability bounds \(\ell_{j,2}\) on \(G_j^r\) by \(\ell_{\min}-\rho_{\mathrm{pert}}\) under tightened H6, but the global \(\ell_{j,2}\) on \(G\) requires the LG-2 boundary collar to control the boundary leakage. CE-3 numerically demonstrates the bottleneck-stability one-sidedness and motivates the H6 tightening to \(\ell_{\min}-3\rho_{\mathrm{pert}}\).
- The L1-H theorem candidate is **LEMMA-CAND**, not Cat-A. The lower bound is proof-grade. The upper-bound part (α) coverage is proof-grade. The upper-bound part (β) per-neighborhood single-bar is partial pending PO-LH1.
- L1-F is not promoted. L1-H reduces L1-F's residual obligations from "H10 = open" to "PO-LH1 + tightened H6 + L1-I constants feasibility".
- The next concrete proof task is either (i) **L1-I constants feasibility** to test whether the L1-H regime is non-empty on canonical configurations, or (ii) **L1-H2** to discharge PO-LH1 via boundary-leakage analysis. L1-I is recommended first because it is fast and informs whether L1-H2 is worth pursuing.
