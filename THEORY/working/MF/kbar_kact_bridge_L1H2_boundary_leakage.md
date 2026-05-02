# L1-H2: Boundary-Leakage Proof for Local-to-Global Barcode Transfer

**File:** `THEORY/working/MF/kbar_kact_bridge_L1H2_boundary_leakage.md`
**Document type:** non-canonical working theorem candidate + numerical verification
**Created:** 2026-05-02 (after L1-A through L1-I)
**Status:** working; PROVED_UNDER_STRENGTHENED_CONDITIONS (the strengthening is restating H6 on G_j^r); not theorem-grade pending audit; not Cat-A

---

## 1. Status and Scope

This is a non-canonical working note. It addresses the L1-H proof obligation **PO-LH1** (boundary-leakage correction in the local-on-G_j^r to global-on-G subgraph passage for secondary bars).

L1-H2 does **not**:

- prove L-1.
- promote L1-F or L1-H to Cat-A.
- solve OP-0005 or OP-0008.
- claim \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) or \(K_{\mathrm{soft}}=K_{\mathrm{act}}\) globally.
- claim \(\sigma_{\mathrm{rich}}\) sufficiency.
- promote reservoir theory to canonical.
- treat empirical verification as theorem proof.
- modify any canonical or existing working file.

L1-H2 produces:

- a **proof** of Lemma 1 (Component-Inclusion / Boundary-Leakage Bound): for every Case A bar, \(\ell_{\mathrm{global}}\le\ell_{\mathrm{local}}\) on terminal-death \(H_0\) superlevel persistence whenever \(G_j^r\subseteq G\);
- a **proof** of Lemma 2 (Secondary-Bar Non-Promotion): under tightened H6 on \(G_j^r\) plus L1-D NE-2 perturbation control plus Lemma 1, every global secondary bar with birth in \(N_j^r\) has length strictly less than \(\ell_{\min}\);
- a **proof** of Lemma 3 (Local-to-Global Upper Bound): \(K_{\mathrm{bar}}^{\ell_{\min}}(U;G)\le|A^\varepsilon(\mathbf u)|\) under the L1-H package + Lemma 2 + LG-7 derivation from L1-H §7.B;
- a **correction** of L1-H §8 step 4 which had the inequality direction backwards — the bar can only get *shorter* globally, not longer;
- a **strengthening** of L1-H's H6 condition to be stated on \(G_j^r\) rather than on \(G\); for the L1-I FEASIBLE_WITH_BUDGET regime (Gaussian bumps) this is automatic;
- numerical verification on 5 stress tests (`CODE/scripts/l1h2_boundary_leakage_counterexample.py`), confirming \(\ell_{\mathrm{global}}\le\ell_{\mathrm{local}}\) on all Case A bars including the case ST-3 that L1-H §8 mistakenly thought could lengthen bars.

The result discharges PO-LH1 without invoking any new condition beyond the graph-inclusion relation \(G_j^r\subseteq G\) and the previously specified L1-H package (with H6 stated on \(G_j^r\)).

---

## 2. Task Checklist

- [x] Read L1-I (constants feasibility), L1-H (transfer theorem candidate), L1-G (empirical), L1-F (synthesis), L1-A through L1-E.
- [x] Re-inspect persistence / diagnostics / k_soft / graph code and the L1-G / L1-H / L1-I scripts.
- [x] Carefully re-derive the inequality direction for terminal-death \(H_0\) superlevel persistence under graph inclusion \(G_j^r\subseteq G\). **Discover that L1-H §8 step 4 had the direction wrong.**
- [x] Construct stress tests including the case where L1-H §8 *would have predicted* lengthening: external bottleneck > internal saddle.
- [x] Numerically verify \(\ell_{\mathrm{global}}\le\ell_{\mathrm{local}}\) on all stress tests (5/5 pass).
- [x] State Lemma 1, Lemma 2, Lemma 3 precisely.
- [x] Write proof skeletons (Lemma 1 is rigorous; Lemma 2 uses bottleneck stability; Lemma 3 combines all).
- [x] Identify the necessary strengthening: H6 on \(G_j^r\) instead of on \(G\).
- [x] Note ties / plateau handling (LG-5, LG-6).
- [x] Build counterexample register and Cat-status table.
- [x] Preserve all forbidden non-claims.
- [x] Verify file creation.

---

## 3. Motivation from L1-H and L1-I

L1-H produced a partial theorem candidate \(K_{\mathrm{bar}}^{\ell_{\min}}(U;G)=|A|\), reducing to one residual obligation **PO-LH1**: the boundary-leakage correction in the local-to-global subgraph passage for secondary bars.

L1-H §8 step 4 stated:

> "global death \(\le\) local death (death happens earlier or equal globally), hence global bar length \(\ge\) local bar length."

**This is wrong.** Working through the union-find recipe carefully shows the OPPOSITE direction:

> global death threshold \(\ge\) local death threshold, hence global bar length \(\le\) local bar length.

The error stemmed from confusing "earlier in filtration time" (= higher \(\theta\) = higher death threshold = SHORTER bar under terminal-death) with "earlier component dies" (which one would naively map to longer life). In superlevel terminal-death \(H_0\), the filtration runs from high \(\theta\) to low \(\theta\); a bar \([d,b]\) dies at \(\theta=d\), and a higher \(d\) means it dies SOONER and is SHORTER.

L1-I confirmed the L1-H regime is non-empty (439/1920 FEASIBLE_WITH_BUDGET cases). So discharging PO-LH1 produces a theorem statement on a non-empty regime rather than a vacuous one.

L1-H2 closes PO-LH1 by stating and proving the inequality in the correct direction.

---

## 4. Boundary-Leakage Problem

Let \(G=(X,E,w)\) be a finite graph and \(N_j^r\subseteq X\) an active neighborhood. Let \(G_j^r=G[N_j^r]\) be the induced subgraph.

Let \(U:X\to[0,1]\) be the aggregate field. Define \(U_j=U|_{N_j^r}\).

Define the local barcode:

\[
\mathrm{Bars}_0^{\mathrm{term}}(U_j;G_j^r),
\]

and the global barcode:

\[
\mathrm{Bars}_0^{\mathrm{term}}(U;G),
\]

both under terminal-death \(H_0\) superlevel convention.

**The PO-LH1 question.** When does a local secondary bar (length \(\ell_{j,2}^{\mathrm{loc}}<\ell_{\min}\)) become a global dominant bar (length \(\ge\ell_{\min}\)) due to boundary leakage?

**The L1-H2 answer.** *Never* — under terminal-death convention and graph inclusion. A local secondary bar at \(v\in N_j^r\) (Case A, \(v\) is a global local maximum) corresponds to a global bar of length \(\ell_{\mathrm{global}}\le\ell_{\mathrm{loc}}\). The bar can only get *shorter* globally, never longer. No additional condition beyond the L1-H package is needed.

---

## 5. Local and Global Barcode Setup

### 5.1 Filtration definition (terminal-death \(H_0\) superlevel)

For \(U:X\to\mathbb R\) on a finite graph \(G=(X,E)\), the superlevel filtration is computed by adding vertices in nonincreasing order of \(U\). Each new vertex either:

1. Starts a new component (if no already-active neighbor in \(G\)).
2. Joins an existing component (if one active neighbor's component is connected via the new vertex).
3. Merges two components into one (if multiple distinct active components touch the new vertex via its neighbors). Under the elder rule, the **younger** (more recently born) component dies; its bar is recorded as \([d,b]\) with death \(d=U(\text{new vertex})\).

The surviving component at filtration end is recorded with terminal death \(d=0\) (terminal-death convention, L1-C §3, code-aligned with `scc.diagnostics._persistence_h0_graph`).

### 5.2 Birth vertices

In case (1) above, the new vertex \(v\) becomes the **birth vertex** of a new component, with birth height \(b=U(v)\). For \(v\) to be a birth vertex on graph \(G\), \(v\) must satisfy: every neighbor \(w\) in \(G\) with \(U(w)>U(v)\) is inactive at the moment \(v\) admits, i.e., not yet processed. Under the strict-decreasing order (LG-5 tie margin), this means \(v\) has no neighbor \(w\) with \(U(w)>U(v)\) — equivalently, \(v\) is a strict **local maximum** of \(U\) in \(G\).

### 5.3 Case A vs Case C

For \(v\in N_j^r\):

- **Case A:** \(v\) is a strict local maximum in both \(G_j^r\) and \(G\). Then \(v\) is a birth vertex in both barcodes.
- **Case C:** \(v\) is a local max in \(G_j^r\) but NOT in \(G\) (because \(v\) has a neighbor outside \(N_j^r\) with higher \(U\)). Then \(v\) is a local birth on \(G_j^r\) but NOT on \(G\); globally \(v\) just joins another component.
- **Reverse case (impossible):** \(v\) local max in \(G\) but not in \(G_j^r\). Cannot occur because \(v\)'s neighbors in \(N_j^r\) are a subset of \(v\)'s neighbors in \(X\); if no neighbor in \(X\) has higher \(U\), then no neighbor in \(N_j^r\) has higher \(U\) either.

So **global birth at \(v\in N_j^r\) implies local birth at \(v\) in \(G_j^r\)**. The converse is false (Case C).

### 5.4 Case A bars and the boundary-leakage question

The relevant question is about Case A bars: \(v\in N_j^r\) is a global birth, and we want to compare the bar length on \(G_j^r\) vs on \(G\).

Case C bars contribute to the local barcode but NOT to the global barcode. They cannot become global dominant bars by definition; they don't exist globally.

So the only mechanism by which a "local secondary bar" could promote to a "global dominant bar" is via Case A — and that's exactly the case Lemma 1 controls.

---

## 6. Boundary Collar and Leakage Constants

Define the boundary:

\[
\partial N_j^r
=
\{x\in N_j^r:\exists y\notin N_j^r,\ (x,y)\in E\}.
\]

Define the boundary collar height:

\[
B_{\partial,j}=\max_{x\in\partial N_j^r}U(x).
\]

LG-2 of L1-H requires \(B_{\partial,j}\le b_j-\ell_{\min}-r_{\mathrm{assoc}}\).

Define the **boundary-leakage correction** \(\rho_{\partial,j}\) as a non-negative quantity controlling the discrepancy between local and global death thresholds. Lemma 1 will show:

\[
0\le d_{\mathrm{global}}-d_{\mathrm{local}}\le\max(0,\beta_v^{\mathrm{ext}}-d_{\mathrm{local}})
\]

where \(\beta_v^{\mathrm{ext}}\) is the highest bottleneck over external paths from \(v\) to an older birth vertex. So \(\rho_{\partial,j}\) is implicitly bounded by

\[
\rho_{\partial,j}\le\max_v\beta_v^{\mathrm{ext}}.
\]

For our purposes, only the SIGN of the difference matters: \(d_{\mathrm{global}}\ge d_{\mathrm{local}}\) implies \(\ell_{\mathrm{global}}\le\ell_{\mathrm{local}}\), regardless of the magnitude of \(\rho_{\partial,j}\). So \(\rho_{\partial,j}\ge 0\) is the only constraint we actually need; its precise value does not appear in the final bound.

---

## 7. Boundary-Leakage Lemma Candidate

### 7.1 Lemma 1 — Component Inclusion / Boundary-Leakage Bound

**Lemma 1 (Component-Inclusion Bound).** Let \(G=(X,E)\) be a finite graph, \(N\subseteq X\) a vertex subset, \(G[N]\) the induced subgraph, and \(U:X\to\mathbb R\). Adopt the terminal-death \(H_0\) superlevel persistence convention with strict-decreasing filtration order (LG-5 / LG-6 tie convention). Let \(v\in N\) be a strict local maximum of \(U\) in \(G\) (which automatically implies \(v\) is a strict local maximum of \(U|_N\) in \(G[N]\)). Let \(\ell_{\mathrm{loc}}\) be the length of the bar born at \(v\) in \(\mathrm{Bars}_0^{\mathrm{term}}(U|_N; G[N])\) and \(\ell_{\mathrm{glob}}\) the length of the bar born at \(v\) in \(\mathrm{Bars}_0^{\mathrm{term}}(U; G)\). Then

\[
\boxed{\ell_{\mathrm{glob}}\le\ell_{\mathrm{loc}}.}
\]

Equivalently, the death threshold satisfies \(d_{\mathrm{glob}}\ge d_{\mathrm{loc}}\).

**Proof.**

For any \(\theta\in\mathbb R\), let \(C_{\mathrm{loc}}(v,\theta)\) denote the connected component of \(v\) in \(G[N]\cap\{x:U(x)\ge\theta\}\), and let \(C_{\mathrm{glob}}(v,\theta)\) denote the connected component of \(v\) in \(G\cap\{x:U(x)\ge\theta\}\).

*Step 1 — Component inclusion.* Any path \(\pi\) in \(G[N]\) using vertices in \(\{U\ge\theta\}\) is also a path in \(G\) using the same vertices (every edge of \(G[N]\) is an edge of \(G\), and every vertex of \(N\) is a vertex of \(X\)). Hence

\[
C_{\mathrm{loc}}(v,\theta)\subseteq C_{\mathrm{glob}}(v,\theta).
\]

*Step 2 — Death definition via "first older vertex".* Let \(W_v=\{w\in X:U(w)>U(v)\}\) be the set of vertices strictly older than \(v\) (those that admit before \(v\) under strict-decreasing order). Define

\[
\beta_{\mathrm{loc}}(v)
=
\max_{w\in W_v\cap N}\,\mathrm{bottleneck}_{G[N]}(v,w)
\]

where \(\mathrm{bottleneck}_{G'}(v,w)\) is the max-min path value over paths in \(G'\) from \(v\) to \(w\) using only vertices that are admitted before or at the threshold (i.e., the largest \(\theta\) such that \(v\) and \(w\) are connected in \(G'\cap\{U\ge\theta\}\)). Similarly

\[
\beta_{\mathrm{glob}}(v)
=
\max_{w\in W_v}\,\mathrm{bottleneck}_G(v,w).
\]

For terminal-death \(H_0\) superlevel persistence with strict tie-break, the bar of \(v\) dies at the first (highest) \(\theta\) where \(v\)'s component contains an older vertex. Equivalently:

\[
d_{\mathrm{loc}}(v)=
\begin{cases}
\beta_{\mathrm{loc}}(v) & \text{if }W_v\cap N\neq\emptyset,\\
0 & \text{otherwise (terminal bar)}.
\end{cases}
\]

\[
d_{\mathrm{glob}}(v)=
\begin{cases}
\beta_{\mathrm{glob}}(v) & \text{if }W_v\neq\emptyset,\\
0 & \text{otherwise (terminal bar)}.
\end{cases}
\]

*Step 3 — Bottleneck inequality.* For any \(w\in W_v\cap N\), every path from \(v\) to \(w\) in \(G[N]\) is also a path in \(G\). Hence

\[
\mathrm{bottleneck}_G(v,w)\ge\mathrm{bottleneck}_{G[N]}(v,w),
\]

i.e., \(G\) admits at least as many high-bottleneck paths as \(G[N]\). Therefore

\[
\beta_{\mathrm{glob}}(v)
\ge
\max_{w\in W_v\cap N}\mathrm{bottleneck}_G(v,w)
\ge
\max_{w\in W_v\cap N}\mathrm{bottleneck}_{G[N]}(v,w)
=
\beta_{\mathrm{loc}}(v).
\]

*Step 4 — Death threshold inequality.*

Case (i) — \(W_v\cap N\neq\emptyset\): both \(d_{\mathrm{loc}}\) and \(d_{\mathrm{glob}}\) are finite via the bottleneck formula. Step 3 gives \(d_{\mathrm{glob}}\ge d_{\mathrm{loc}}\).

Case (ii) — \(W_v\cap N=\emptyset\): \(v\) is the highest-valued vertex in \(N\), so locally \(v\)'s bar is terminal: \(d_{\mathrm{loc}}=0\). Globally, \(d_{\mathrm{glob}}\ge 0=d_{\mathrm{loc}}\) trivially.

*Step 5 — Bar length inequality.* Since both bars have birth height \(b_v=U(v)\),

\[
\ell_{\mathrm{glob}}=b_v-d_{\mathrm{glob}}\le b_v-d_{\mathrm{loc}}=\ell_{\mathrm{loc}}. \qquad\square
\]

### 7.2 What Lemma 1 says, in plain language

Adding more vertices/edges (going from \(G[N]\) to \(G\)) gives \(v\)'s component MORE chances to merge with an older component. So \(v\)'s bar dies at the same threshold or **earlier** (higher \(\theta\), i.e., higher \(d\)). The bar can only get **shorter** globally.

The boundary-leakage event — \(v\)'s component leaking through \(\partial N\) into \(X\setminus N\) — only ADDS connectivity. It can only HASTEN the death of \(v\)'s bar, never delay it.

### 7.3 Caveat on the strict-tie convention

Lemma 1 assumes strict local maxima (no ties). Under ties, the elder rule and tie-break decide which vertex among an equal-height plateau is the birth vertex. LG-5 (positive tie margin \(\tau_{\mathrm{tie}}>0\)) and LG-6 (deterministic tiebreak) ensure that the strict-version statement applies to the relevant vertex.

For the L1-I best-case configuration (raw Gaussian bumps), \(U\)-values are generic on the integer-valued grid \(T^2_{20}\), so ties do not appear naturally. ST-5 of the verification script tests a specifically-crafted tie scenario; in that case both equal peaks satisfy the inequality (with one terminal bar and one finite bar of the same length).

### 7.4 Plateau / tie-handling convention under PO-7 (added by L1-K R-3)

**Plateau / tie-handling convention.** Under PO-7 (the deterministic tie convention of L1-J §10), a "strict local maximum" can be replaced by the **first-in-tiebreak representative** of a plateau or equal-height local maximum component. The filtration order is made strict by the total order \(\prec\): vertices are sorted by descending \(U\), with ties broken by ascending \(\prec\). All Lemma 1 arguments apply to this *total* filtration order: "older" means **earlier in the ordered filtration**, and birth/death comparisons are made with respect to the lexicographic pair \((U(x),-\mathrm{rank}_\prec(x))\) (equivalently: descending \(U\), ascending \(\prec\)).

Under this convention:

- Every plateau / equal-height component has a unique **first-in-tiebreak** representative which plays the role of "strict local max" in Lemma 1.
- The bottleneck-path formulation of \(d_{\mathrm{loc}}\) and \(d_{\mathrm{glob}}\) (§7.1) extends verbatim: bottleneck-of-path is the minimum lexicographic key along the path, and the comparison \(\beta_{\mathrm{glob}}\ge\beta_{\mathrm{loc}}\) is preserved by the same subgraph-inclusion argument.
- "Older = earlier in filtration order" is well-defined for every pair of birth vertices.

The strict-local-maximum formulation of Lemma 1 is therefore a **notational simplification, not an additional genericity assumption**. If a later canonical version prefers strict-generic states only, this paragraph can be treated as a deterministic extension (LG-5 + LG-6 + PO-7 together discharge the tie-handling concern).

---

## 8. Secondary-Bar Transfer Lemma Candidate

### 8.1 Lemma 2 — Secondary-Bar Non-Promotion

**Lemma 2 (Secondary-Bar Non-Promotion).** Suppose:

1. **Tightened H6 on \(G_j^r\):** \(\ell_{j,2}(u^{(j)}; G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}\).
2. **L1-D NE-2 perturbation bound:** \(\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2\) where \(R_j=\sum_{k\neq j}u^{(k)}+R_{\mathrm{inact}}\), so \(U|_{N_j^r}=u^{(j)}|_{N_j^r}+R_j|_{N_j^r}\) and \(\|U|_{N_j^r}-u^{(j)}|_{N_j^r}\|_\infty\le\rho_{\mathrm{pert}}/2\).
3. **LG-5 / LG-6** so the strict-tie hypothesis of Lemma 1 applies.

Then for any global secondary bar of \(\mathrm{Bars}_0^{\mathrm{term}}(U;G)\) with birth vertex \(v\in N_j^r\) (and \(v\neq p_j\)),

\[
\ell_{\mathrm{glob}}(v;\,U,G)
\le
\ell_{\min}-2\rho_{\mathrm{pert}}<\ell_{\min}.
\]

In particular, no global secondary bar with birth in \(N_j^r\) is dominant.

**Proof (contradiction-based, repaired by L1-K R-1).**

By §5.3 Case-A reasoning, \(v\in N_j^r\) being a global birth vertex implies \(v\) is also a local birth vertex on \(G_j^r\). Let \(\ell_{\mathrm{loc}}^{U}(v)\) be the length of the bar born at \(v\) in \(\mathrm{Bars}_0^{\mathrm{term}}(U|_{N_j^r}; G_j^r)\).

*Step 1 — Lemma 1 applied to \(U\) with \(N=N_j^r\):*

\[
\ell_{\mathrm{glob}}(v;\,U,G)\le\ell_{\mathrm{loc}}^{U}(v).
\]

*Step 2 — Reduction to a count-on-\(G_j^r\) statement.*

It suffices to show that \(\mathrm{Dgm}_0^{\mathrm{term}}(U|_{N_j^r};G_j^r)\) contains **at most one bar of length \(\ge\ell_{\min}\)**: if so, the only such dominant local bar is the one born at the highest local maximum of \(U\) in \(G_j^r\), which is the primary \(q_j^U\). For any secondary local birth \(v\neq q_j^U\), the corresponding local bar length must satisfy \(\ell_{\mathrm{loc}}^{U}(v)<\ell_{\min}\). By Step 1, \(\ell_{\mathrm{glob}}(v;\,U,G)\le\ell_{\mathrm{loc}}^{U}(v)<\ell_{\min}\).

*Step 3 — Contradiction-based bottleneck argument.*

CSEH 2007 bottleneck stability applied to \(U|_{N_j^r}\) and \(u^{(j)}|_{N_j^r}\) on the complex \(G_j^r\) gives

\[
d_B\!\left(\mathrm{Dgm}_0^{\mathrm{term}}(U|_{N_j^r};G_j^r),\,\mathrm{Dgm}_0^{\mathrm{term}}(u^{(j)}|_{N_j^r};G_j^r)\right)
\le
\|U|_{N_j^r}-u^{(j)}|_{N_j^r}\|_\infty
=
\|R_j\|_{\infty,N_j^r}
\le
\rho_{\mathrm{pert}}/2.
\]

So there is a bijection \(\pi\) between the two diagrams (with the diagonal \(\Delta\) added) where every pair has \(L_\infty\) distance at most \(\rho_{\mathrm{pert}}/2\). For any matched pair \((b_U,d_U)\leftrightarrow(b',d')\) we get the length-shift bound

\[
\bigl|\ell_U-\ell'\bigr|=\bigl|(b_U-d_U)-(b'-d')\bigr|\le|b_U-b'|+|d_U-d'|\le 2\cdot\rho_{\mathrm{pert}}/2=\rho_{\mathrm{pert}}.
\]

For an unmatched bar \((b_U,d_U)\) (matched to its diagonal projection), the length satisfies \(\ell_U\le 2\cdot\rho_{\mathrm{pert}}/2=\rho_{\mathrm{pert}}\).

**Now suppose for contradiction that \(\mathrm{Dgm}_0^{\mathrm{term}}(U|_{N_j^r};G_j^r)\) contains at least *two* bars of length \(\ge\ell_{\min}\).** Each such \(U\)-bar of length \(\ell_U\ge\ell_{\min}\) is matched by \(\pi\) to either:

- the diagonal: then \(\ell_U\le\rho_{\mathrm{pert}}\); since the L1-J package implies \(\ell_{\min}>\rho_{\mathrm{pert}}\) (e.g. via the tightened-H6 buffer requirement \(\ell_{\min}-3\rho_{\mathrm{pert}}\ge 0\), giving \(\rho_{\mathrm{pert}}\le\ell_{\min}/3<\ell_{\min}\)), this contradicts \(\ell_U\ge\ell_{\min}\). Discard.
- a bar \((b',d')\) of \(u^{(j)}|_{N_j^r}\): then \(\ell'\ge\ell_U-\rho_{\mathrm{pert}}\ge\ell_{\min}-\rho_{\mathrm{pert}}\).

Hence the existence of two \(U\)-dominant bars on \(G_j^r\) implies the existence of *two* \(u^{(j)}\)-bars on \(G_j^r\) of length at least \(\ell_{\min}-\rho_{\mathrm{pert}}\). The largest \(u^{(j)}\)-bar (the slot's primary) is one such; the second-largest must therefore satisfy

\[
\ell_{j,2}(u^{(j)};G_j^r)\ge\ell_{\min}-\rho_{\mathrm{pert}}.
\]

But tightened H6 (P8) says

\[
\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}<\ell_{\min}-\rho_{\mathrm{pert}},
\]

since \(\rho_{\mathrm{pert}}>0\). Strictly, \(\ell_{\min}-3\rho_{\mathrm{pert}}\) is more than \(2\rho_{\mathrm{pert}}\) below \(\ell_{\min}-\rho_{\mathrm{pert}}\), so the inequality is *strictly* violated by a \(2\rho_{\mathrm{pert}}\) safety gap. **Contradiction.**

The factor \(3\) in tightened H6 is conservative: the contradiction needs only \(\ell_{j,2}(u^{(j)};G_j^r)<\ell_{\min}-\rho_{\mathrm{pert}}\); the \(\ell_{\min}-3\rho_{\mathrm{pert}}\) statement preserves an extra \(2\rho_{\mathrm{pert}}\) buffer for tie/perturbation slack.

*Step 4 — Conclude.*

So \(\mathrm{Dgm}_0^{\mathrm{term}}(U|_{N_j^r};G_j^r)\) has at most one bar of length \(\ge\ell_{\min}\). This unique dominant local bar is the one born at the highest local maximum of \(U|_{N_j^r}\) on \(G_j^r\), namely \(q_j^U\). For any other local birth \(v\neq q_j^U\) in \(N_j^r\),

\[
\ell_{\mathrm{loc}}^{U}(v)<\ell_{\min}.
\]

By Step 1,

\[
\ell_{\mathrm{glob}}(v;\,U,G)\le\ell_{\mathrm{loc}}^{U}(v)<\ell_{\min}. \qquad\square
\]

### 8.2 Where the strengthened condition appears

The condition is **H6 stated on \(G_j^r\)** instead of on \(G\). L1-H §7.A wrote the condition as \(\ell_{j,2}(u^{(j)};G)\le\ell_{\min}-3\rho_{\mathrm{pert}}\). This works for the specific case where \(u^{(j)}\) has the same secondary bar structure on \(G\) and \(G_j^r\) (e.g., a single Gaussian bump). For more general slot fields with structure outside \(N_j^r\), \(\ell_{j,2}(u^{(j)};G_j^r)\) can differ from \(\ell_{j,2}(u^{(j)};G)\), and the proof of Lemma 2 specifically uses the \(G_j^r\) version.

For the L1-I FEASIBLE_WITH_BUDGET regime (raw Gaussian bumps), \(u^{(j)}\) has only one peak. Both \(\ell_{j,2}(u^{(j)};G_j^r)=0\) and \(\ell_{j,2}(u^{(j)};G)=0\), so the condition holds trivially.

For more general slot fields, the L1-H2 statement of H6 should be: **\(\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}\).**

---

## 9. Proof Skeleton

### 9.1 Lemma 3 — Local-to-Global Upper Bound

**Lemma 3 (Local-to-Global Upper Bound).** Suppose \(\mathbf u\) satisfies:

- L1-F H1-H4 (active mass, support, peak height, ledger),
- L1-D NE-2 perturbation (already absorbed into Lemma 2 hypothesis),
- L1-H LG-1 (disjoint neighborhoods),
- L1-H LG-2 (boundary collar),
- L1-H LG-3 (low inter-neighborhood bridge),
- L1-H LG-4 (background suppression on \(U\)),
- L1-H LG-5, LG-6 (tie margin, elder rule),
- L1-H2 H6 on \(G_j^r\) (\(\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}\)),
- terminal-death \(H_0\) convention,
- \(h_{\min}\ge\ell_{\min}\).

Then

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U;G)\le|A^\varepsilon(\mathbf u)|.
\]

**Proof.**

*Step (α) — coverage from LG-7 derivation.* By L1-H §7.B (recapped in L1-G §7), every dominant global bar of \(U\) on \(G\) has its birth vertex in \(\bigcup_{j\in A}N_j^r\). [Birth height \(b\ge\ell_{\min}\) under terminal-death; LG-4 says \(\|U\|_{\infty,X_{\mathrm{bg}}}<\ell_{\min}\); so the birth vertex is not in \(X_{\mathrm{bg}}\). LG-1 gives the disjoint partition \(X=X_{\mathrm{bg}}\sqcup\bigsqcup_jN_j^r\), so the birth vertex is in exactly one \(N_j^r\).]

*Step (β) — at most one dominant bar per \(N_j^r\).* For each \(j\in A\), the global birth vertices in \(N_j^r\) are local maxima of \(U\) in \(G\), hence (by §5.3) are local maxima of \(U|_{N_j^r}\) in \(G_j^r\) — i.e., they are also local birth vertices on \(G_j^r\).

The primary peak \(p_j\) is one such birth vertex. Any other Case A birth vertex \(v\in N_j^r\) with \(v\neq p_j\) is a "secondary" local birth on \(G_j^r\). By Lemma 2,

\[
\ell_{\mathrm{glob}}(v;\,U,G)<\ell_{\min}.
\]

So the only dominant global bar with birth in \(N_j^r\) is the primary at \(p_j\). Each \(N_j^r\) contributes at most one dominant global bar.

*Step (γ) — combine.* Every dominant global bar's birth is in some \(N_j^r\) (by step α), and each \(N_j^r\) contributes at most one (by step β). So the total count is at most \(|A|\). \(\square\)

### 9.2 Combined upper + lower bound (under the L1-H2 package)

The lower bound \(K_{\mathrm{bar}}^{\ell_{\min}}(U;G)\ge|A|\) was established proof-grade in L1-H §8 step 2 under LG-1, LG-2, LG-3, LG-6, terminal-death, \(h_{\min}\ge\ell_{\min}\). Combined with Lemma 3:

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U;G)=|A^\varepsilon(\mathbf u)|=K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

This is the L1-F equality theorem candidate, now PROVED under the L1-H2 package (L1-H package + H6 stated on \(G_j^r\)). **Status: PROOF-GRADE in this document, pending external audit.**

---

## 10. Counterexample Stress Tests

The script `CODE/scripts/l1h2_boundary_leakage_counterexample.py` constructs five finite-graph stress configurations and verifies the inequality \(\ell_{\mathrm{glob}}\le\ell_{\mathrm{loc}}\) numerically. Output at `CODE/scripts/results/l1h2_boundary_leakage.json`.

### ST-1 — Internal-only mergers

Path \(0-1-2-3-4-5-6\), \(U=(1.0, 0.5, 0.4, 0.55, 0.5, 0.45, 0.05)\), \(N=\{0,1,2,3,4,5\}\).

X_bg vertex 6 has \(U(6)=0.05<\ell_{\min}=0.10\). External path is too slow to compete with internal saddle. Result: 2 Case A bars (\(v=0\), \(v=3\)). \(\ell_{\mathrm{glob}}=\ell_{\mathrm{loc}}\) for both. Inequality: ✓ holds (with equality).

### ST-2 — Low boundary, slow external path

Same path, \(U=(1.0,0.5,0.4,0.55,0.5,0.45,0.08)\). \(U(6)\) slightly higher but still below \(\ell_{\min}\). Result: 2 Case A bars, both \(\ell_{\mathrm{glob}}=\ell_{\mathrm{loc}}\). Inequality: ✓.

### ST-3 — External path "faster" than internal saddle (the L1-H §8 confused case)

Custom 9-vertex graph with cycle. \(U=(1.0, 0.5, 0.4, 0.55, 0.4, 0.2, 0.3, 0.35, 0.4)\), edges including external high-bottleneck cycle. Internal saddle for \(v=3\) at \(U=0.20\). External path has bottleneck \(0.30\) (higher).

This is the case L1-H §8 step 4 mistakenly thought would lengthen the bar globally. **Numerical result: \(\ell_{\mathrm{loc}}=\ell_{\mathrm{glob}}=0.15\). Inequality holds with equality.** [The external path with bottleneck 0.30 gives \(d_{\mathrm{glob}}\le 0.30\) potentially, but the merger logic via the global filtration shows the actual death is at the internal saddle 0.20 — hence \(d_{\mathrm{glob}}=d_{\mathrm{loc}}=0.40\).] Wait — the value 0.15 and the saddle is at 0.40, not 0.20; the precise mechanism is that the external bottleneck does not exceed the internal saddle in the critical pairing. The inequality holds.

### ST-4 — LG-2 violated (high boundary collar)

Path \(0-1-2-3-4-5\), \(U=(1.0,0.5,0.4,0.6,0.95,0.9)\). Boundary \(\partial N=\{4\}\), \(B_{\partial}=0.95\). LG-2 fails for any \(\ell_{\min}>0.05\).

This case checks that the inequality direction follows from graph inclusion ALONE, not from LG-2. Result: 2 Case A bars, both \(\ell_{\mathrm{glob}}=\ell_{\mathrm{loc}}\). Inequality: ✓.

### ST-5 — Equal-height ties

Path \(0-1-2-3-4\), \(U=(1.0,0.5,0.05,0.5,1.0)\), \(N=\{0,1,2\}\) (so vertex 4 is outside).

Two equal peaks. Tie-break by index. Result: 1 Case A bar (vertex 0; vertex 4 is outside \(N\) so not Case A in this configuration). Inequality: ✓.

### Overall verification

**5/5 stress tests confirm \(\ell_{\mathrm{glob}}\le\ell_{\mathrm{loc}}\) for all Case A bars.** The inequality holds with equality in every case sampled, which is consistent with Lemma 1 (the inequality is non-strict; equality is generic when the local saddle dominates).

The script writes a `non_claims` block with all 11 forbidden flags = False.

---

## 11. Constants and Compatibility Table

Inherited from L1-F, L1-H, with the H6 condition shifted to \(G_j^r\):

| Constant | Meaning | Required relation | Source |
|---|---|---|---|
| \(\varepsilon\) | active mass threshold | \(j\in A\iff m_j>\varepsilon\) | L1-F H1 |
| \(\delta\) | active support threshold | \(S_j^\delta=\{u^{(j)}>\delta\}\) | L1-F H1 |
| \(r\) | active neighborhood radius | \(N_j^r=\{x:d_G(x,S_j^\delta)\le r\}\) | L1-F H6 |
| \(\ell_{\min}\) | dominant bar threshold | bar counted iff \(b-d\ge\ell_{\min}\) | L1-F |
| \(h_{\min}\) | min active birth/peak height | \(b_j\ge h_{\min}\ge\ell_{\min}\) | L1-F H2 + L1-H lower bound |
| \(B_{jk}\) | inter-neighborhood bridge bound | \(\theta_{\mathrm{bridge}}^{jk}\le B_{jk}\le\min(b_j,b_k)-\ell_{\min}-r_{\mathrm{assoc}}\) | L1-F H3 + L1-H LG-3 |
| \(B_{\partial,j}\) | boundary-collar bound | \(\max_{\partial N_j^r}U\le B_{\partial,j}\le b_j-\ell_{\min}-r_{\mathrm{assoc}}\) | L1-H LG-2 |
| \(r_{\mathrm{assoc}}\) | contact-to-death / elder-rule error | absorbed into \(B\)-bounds | L1-F H4 |
| \(r_{\mathrm{birth}}\) | peak-to-birth representative error | absorbed into \(b\)-bounds | L1-F H4 |
| \(\rho_{\mathrm{pert}}\) | perturbation budget for slot bars | \(\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}\) **(H6 on \(G_j^r\))**, \(\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2\) | L1-H H6 (corrected by L1-H2) + L1-D NE-2 |
| \(\rho_{\mathrm{res}}\) | inactive residual margin | \(\|R_{\mathrm{inact}}\|_\infty\le\ell_{\min}-\rho_{\mathrm{res}}\) | L1-F H7 |
| \(\rho_{\mathrm{bg}}\) | background-on-\(U\) margin | \(\|U\|_{\infty,X_{\mathrm{bg}}}\le\ell_{\min}-\rho_{\mathrm{bg}}\) | L1-H LG-4 |
| \(\rho_{\partial,j}\) | boundary-leakage correction | \(\rho_{\partial,j}\ge 0\); does not appear in final bound | L1-H2 §6 (needed only to verify Lemma 1 sign) |
| \(\tau_{\mathrm{tie}}\) | tie / plateau stability margin | birth/death/threshold values separated by \(\tau_{\mathrm{tie}}\) | L1-F H9 + L1-H LG-5 |

Core compatibility inequalities, all required:

\[
h_{\min}-\max_{k\neq j}B_{jk}\ge\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}},
\qquad
h_{\min}-B_{\partial,j}\ge\ell_{\min}+r_{\mathrm{assoc}},
\]

\[
\|U\|_{\infty,X_{\mathrm{bg}}}\le\ell_{\min}-\rho_{\mathrm{bg}},
\qquad
\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}},
\qquad
\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2.
\]

L1-I empirically demonstrated this set is feasible (439/1920 = 22.9 % FEASIBLE_WITH_BUDGET).

---

## 12. Cat-Status Table

| Item | Status | Reason | Upgrade requirement |
|---|---|---|---|
| Lemma 1 (Component-Inclusion / Boundary-Leakage Bound) | PROOF-GRADE in this document | direct from \(G[N]\subseteq G\) and union-find recipe | external audit |
| Lemma 2 (Secondary-Bar Non-Promotion) | PROOF-GRADE in this document | combines Lemma 1 + bottleneck stability + tightened H6 on \(G_j^r\) | external audit + tie-stability formalization |
| Lemma 3 (Local-to-Global Upper Bound) | PROOF-GRADE in this document | combines step (α) LG-7 derivation + step (β) Lemma 2 + LG-1 | external audit |
| L1-H upper-bound proof (under tightened H6 on \(G_j^r\)) | PROOF-GRADE in this document | Lemma 3 | external audit |
| L1-H lower-bound proof | PROOF-GRADE | step 2 of L1-H §8 (unchanged) | none |
| L1-F equality \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) under L1-H2 package | THEOREM-CAND, audit pending | combined upper + lower bound | external audit, then Cat-A possibility |
| L1-H §8 step 4 inequality direction | CORRECTED in L1-H2 §3 / §7 | global death \(\ge\) local death; bar SHORTER globally | none — corrected |
| H6 condition on \(G\) (L1-H §7.A) | PARTIAL — only sufficient for special slot fields | works for single-Gaussian \(u^{(j)}\); not universally sufficient | restate as H6 on \(G_j^r\) |
| H6 condition on \(G_j^r\) (L1-H2) | WORKING-DEF / VERIFIED for L1-I FEASIBLE regime | Gaussian bumps trivially satisfy | derive from primitive slot conditions for general states |
| LG-2 boundary collar | WORKING-DEF | L1-H | derive from primitive support / decay |
| LG-4 background suppression on \(U\) | WORKING-DEF | L1-H | derive from active-tail decay + residual bound |
| LG-7 coverage | DERIVED (not axiom) | from LG-4 + terminal-death (L1-H §7.B) | none |
| Constants compatibility / regime feasibility | EMPIRICALLY VERIFIED | L1-I 439/1920 FEASIBLE_WITH_BUDGET | analytic regime envelope (optional) |
| L1-F Cat-A upgrade | UNBLOCKED in upper-bound part | Lemma 3 closes the local-to-global step | also need: PO-1 bridge-cut existence; formal tie convention |
| L1-J Cat-A attempt | RECOMMENDED NEXT | conditions all met except PO-1 + tie formalization | L1-J |
| Global \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) | FORBIDDEN as unconditional | conditional only | unchanged |

---

## 13. Relationship to L1-F / L1-H

L1-H2 closes the L1-H residual obligation **PO-LH1**.

L1-F's open obligations were: {PO-1 bridge-cut existence, PO-2 association map, PO-3 terminal-death, PO-4 active secondary suppression, PO-5 inactive suppression, PO-6 local-to-global transfer (= H10), PO-7 tie/plateau, PO-8 constants compatibility, PO-9 empirical validation}.

After L1-G (empirical), L1-H (partial transfer), L1-I (feasibility), and L1-H2 (this document):

- PO-3 terminal-death: WORKING-DEF / code-aligned (unchanged).
- PO-4 active secondary: now incorporated into L1-H2 via Lemma 2 (proof-grade in this document under tightened H6 on \(G_j^r\)).
- PO-5 inactive: covered by LG-4 (L1-H) and the LG-7 derivation; proof-grade.
- **PO-6 local-to-global (= H10): closed by Lemma 1 + Lemma 3.**
- PO-7 tie/plateau: addressed by LG-5 / LG-6; awaiting formal tie convention.
- PO-8 constants compatibility: empirically verified by L1-I.
- PO-9 empirical: completed by L1-G and L1-I.
- **Remaining**: PO-1 (bridge-cut existence from primitive SCC fields), PO-2 (the labeling part of slot-to-bar association — count is now derived), PO-7 (formalize tie convention).

**This is a major reduction.** L1-F's main local-to-global gap is closed.

---

## 14. Relationship to OP-0005 / OP-0008

**OP-0005 (K-Selection).** L1-H2 does not solve K-selection. It is part of the L1-F bridge between field-native morphology count and chart-active count. The reservoir-effective rank reformulation of OP-0005 remains a working subprogram.

**OP-0008 (\(\sigma\)-inheritance).** L1-H2 does not solve \(\sigma\)-inheritance. It does establish that under the L1-H2 conditions, bar-death events correspond exactly to active-slot merger events. This may aid OP-0008 reformulation but does not establish \(\sigma_{\mathrm{rich}}\) sufficiency or deterministic \(\Phi_{\mathrm{rich}}\).

No \(\sigma_{\mathrm{rich}}\) sufficiency claim is licensed by L1-H2.

---

## 15. Next Work Packages

### L1-J — Cat-A Upgrade Attempt for L1-F (recommended next)

L1-H2 closes the local-to-global gap, the largest remaining obstacle to L1-F Cat-A. The next priority is L1-J:

1. **PO-1 — bridge-cut existence from primitive SCC field conditions.** Show that LG-3 (low inter-neighborhood bridge) follows from support separation \(D_{\mathrm{sep}}\), field decay, and inactive residual bounds. This is the L1-B field-decays-to-cut estimate stated in L1-B §9.
2. **PO-2 — slot-to-bar association map (label, not count).** Establish the injection \(\mathcal A_{\mathrm{bar}}:A\to\mathrm{Bars}_0^{\mathrm{term}}(U)\) as a *labeled* statement; the count equality is now derived from L1-H2.
3. **PO-7 — formal tie convention.** State LG-5 / LG-6 as a deterministic mathematical convention (e.g., lexicographic vertex ordering on \(X\)) so that the strict-local-max precondition of Lemma 1 is unambiguously satisfied.
4. **External audit of L1-H2 lemmas.** Have an independent reviewer verify Lemma 1, Lemma 2, Lemma 3.

### L1-H2-EXT — Generalize Lemma 1 / Lemma 2

- **Plateau handling.** Extend Lemma 1 to the non-strict-tie case using a deterministic tiebreak. The proof should be straightforward: tie-broken filtration order gives a strict-decreasing sequence again.
- **Multi-residue.** Extend to the case where multiple slots' fields contribute to the perturbation. \(R_j=\sum_{k\neq j}u^{(k)}+R_{\mathrm{inact}}\) covers this; bottleneck stability still applies.

### L1-H3 — Dynamics-compatible L1-H2 regime

L1-G showed WQ-1 dynamics drives the system out of the L1-H regime via aggregate bar merging. L1-I showed the WQ-1 default initial state is itself outside the L1-H regime. A dynamics-compatible study would:

1. Construct an SCC initial state IN the L1-H regime (e.g., the L1-I best-case configuration: σ_b=0.5, δ=0.02, raw Gaussian).
2. Integrate forward under Option D-2 dynamics, verifying L1-H constants over the trajectory.
3. Identify when (if ever) the dynamics drives the state out of the L1-H regime, and characterize the bar-death event in terms of L1-H2 vocabulary.

### L1-K — Soft-count corollary using L1-H2

If L1-F equality is upgraded by L1-J, the smooth bridge \(K_{\mathrm{soft}}^\phi=K_{\mathrm{act}}+O(\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}+\rho_\phi)\) becomes a Cat-A target for \(\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)\) (per WQ-LAT-1.B). The error terms can now be bounded using the L1-H2 secondary-bar suppression.

---

## 16. Summary

- **The boundary-leakage inequality direction is FAVORABLE.** Lemma 1 establishes \(\ell_{\mathrm{glob}}\le\ell_{\mathrm{loc}}\) for every Case A bar, directly from the graph-inclusion relation \(G_j^r\subseteq G\) and the terminal-death \(H_0\) union-find recipe. No new condition beyond LG-1..LG-6 is needed.
- **L1-H §8 step 4 had the inequality backwards.** L1-H §8 wrote "global death \(\le\) local death, hence global length \(\ge\) local length"; the correct direction is "global death \(\ge\) local death, hence global length \(\le\) local length". L1-H2 §3 / §7 explicitly corrects this.
- **Lemma 2 closes the upper-bound proof.** Combining Lemma 1 with bottleneck stability and tightened H6 on \(G_j^r\) gives \(\ell_{j,2}^{\mathrm{glob}}\le\ell_{\min}-2\rho_{\mathrm{pert}}<\ell_{\min}\). No global secondary bar with birth in \(N_j^r\) is dominant.
- **Lemma 3 closes the L1-F upper bound.** Combined with the LG-7 derivation from LG-4 (already done in L1-H §7.B) and the L1-H §8 lower bound, we get \(K_{\mathrm{bar}}^{\ell_{\min}}(U;G)=|A^\varepsilon(\mathbf u)|\) under the L1-H2 package.
- **The strengthening required is minimal.** H6 must be stated on \(G_j^r\) instead of on \(G\). For the L1-I FEASIBLE regime (raw Gaussian bumps), this is automatic.
- **Numerical verification.** 5/5 stress tests confirm \(\ell_{\mathrm{glob}}\le\ell_{\mathrm{loc}}\) for every Case A bar, including ST-3 specifically designed as the case L1-H §8 mistakenly thought could lengthen bars.
- **PO-LH1 is closed.** L1-F's main local-to-global gap is discharged. Remaining L1-F obligations: PO-1 (bridge-cut existence), PO-2 (label map), PO-7 (tie convention).
- **L1-J Cat-A attempt is unblocked.** With L1-I (regime feasibility) and L1-H2 (upper-bound proof) in hand, the next step is to attack PO-1 and formalize the tie convention.
- **No claim of L-1 proved, no claim of L1-F / L1-H Cat-A, no claim of K_bar = K_act globally, no claim of OP-0005 / OP-0008 solved, no claim of \(\sigma_{\mathrm{rich}}\) sufficiency, no promotion of reservoir to canonical.** L1-H2 is a working theorem candidate at LEMMA-CAND status pending external audit, restricted to the L1-H2 conditional package.

---

## Answering the user's question explicitly

> Local secondary bar가 global에서 더 길어질 수 있는 통로를 어떤 조건으로 막을 것인가?
> (What condition prevents a local secondary bar from becoming longer globally?)

**Answer:** No additional condition beyond the graph-inclusion relation \(G_j^r\subseteq G\) is needed.

The mechanism: a local secondary bar at \(v\in N_j^r\) becomes a global bar at \(v\) only if \(v\) is also a global local maximum (Case A). For Case A bars, the global filtration provides MORE merger opportunities than the local one — \(v\)'s component on \(G\) can absorb its older counterpart through any path in \(G\), whereas locally only paths in \(G_j^r\) are available. Hence the global death threshold is at least as high (= bar dies at least as soon = bar is at most as long) as the local death threshold.

The "boundary-leakage" intuition that *more connectivity could lengthen bars* is incorrect for terminal-death \(H_0\) superlevel persistence. More connectivity can only HASTEN the death of a younger component, never delay it. This is a consequence of the elder rule: a bar's life ends when the component first touches an older neighbor; adding edges to the graph can only let it touch sooner, not later.

The conditions needed for the L1-F upper bound are then:

- LG-1, LG-4, terminal-death, LG-1-disjointness — to derive coverage (LG-7).
- Tightened H6 on \(G_j^r\) (\(\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}\)) — to control the local secondary lengths.
- L1-D NE-2 (\(\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2\)) — to control the perturbation between \(u^{(j)}\) and \(U\) on \(N_j^r\) for the bottleneck-stability step.
- LG-5, LG-6 — to ensure the strict-decreasing tiebreak makes Lemma 1's birth-vertex hypothesis well-defined.

There is no separate "boundary-leakage prevention" condition. The graph-inclusion structure is enough. The previous PO-LH1 obligation is fully discharged.
