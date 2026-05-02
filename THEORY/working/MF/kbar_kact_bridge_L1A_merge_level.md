# L1-A: Merge-Level and Bridge-Height Formalization

## 1. Status and Scope

This is a non-canonical working formalization. It defines finite-graph superlevel merge-level machinery needed by the L-1 hard-bar bridge, but it does not prove L-1.

This document supports the working theorem candidate

\[
\mathrm{WS}(\varepsilon,\delta,D_{\mathrm{sep}},\eta,\ell_{\min},h_{\min},h_{\mathrm{noise}},h_{\mathrm{margin}})
\Rightarrow
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u),
\]

by making the phrases "birth height", "bridge height", "merge level", and "persistence margin" precise on finite superlevel graphs.

This document does not:

- solve OP-0005,
- solve OP-0008,
- promote reservoir theory to canonical status,
- claim \(\sigma_{\mathrm{rich}}\) sufficiency,
- identify \(K_{\mathrm{bar}}\), \(K_{\mathrm{soft}}\), and \(K_{\mathrm{act}}\) globally,
- treat WQ-LAT-1 / WQ-LAT-1.B evidence as a general theorem.

## 2. Motivation from L-1

L-1 needs to justify the implication

\[
\text{one active slot}
\Rightarrow
\text{one dominant aggregate }H_0\text{ bar}.
\]

The missing ingredient is a finite-graph way to relate

\[
\text{birth height} - \text{merge level}
\]

to the length of the associated \(H_0\) persistence bar.

The earlier L-1 formalization used a persistence-facing quantity \(\theta_{\mathrm{merge},j}^U\). This was useful but partly circular: it described the desired death/merge value without yet separating the definitional persistence pairing from primitive graph/field estimates.

This L1-A note separates:

1. definitions that are exact on a finite superlevel graph,
2. pairing-dependent definitions that require a barcode convention,
3. open estimates that must be proven from support separation, overlap, field decay, and inactive suppression.

## 3. Superlevel Filtration Setup

Let

\[
G=(X,E,w)
\]

be a finite weighted graph. The weights \(w\) may be used by downstream dynamics, but the definitions below use only the adjacency relation and the finite vertex set unless otherwise stated.

Let

\[
U:X\to[0,1]
\]

be the aggregate field.

For \(\theta\in[0,1]\), define the superlevel vertex set

\[
X^\theta(U)=\{x\in X:U(x)\ge\theta\}.
\]

Define the superlevel induced graph

\[
G^\theta(U)=G[X^\theta(U)].
\]

If \(\theta_1>\theta_2\), then

\[
X^{\theta_1}(U)\subseteq X^{\theta_2}(U),
\qquad
G^{\theta_1}(U)\subseteq G^{\theta_2}(U).
\]

Thus, as \(\theta\downarrow0\), superlevel components are born at high field values and merge as lower-valued vertices enter the filtration.

For finite computation, it is enough to evaluate the filtration at the finite set of vertex values

\[
\mathrm{Val}(U)=\{U(x):x\in X\}.
\]

The working convention in this document is:

- an \(H_0\) superlevel bar born at height \(b\) and dying at merge height \(d\) has length
  \[
  \ell=b-d;
  \]
- if the final surviving component is retained in an unreduced finite filtration on \(U:X\to[0,1]\), its terminal death value may be taken as \(0\);
- if reduced persistence or essential-bar conventions are used, the final surviving component must be handled explicitly and not silently mixed with finite death bars.

This convention is only for L1-A bookkeeping. Any later theorem-grade version must state the persistence convention used by the actual implementation or proof.

## 4. Active-Slot Representative Peaks

Let

\[
\mathbf u=(u^{(1)},\dots,u^{(K_{\mathrm{field}})})
\]

be a finite-chart multi-formation state, and let

\[
A^\varepsilon(\mathbf u)=\{j:m_j(\mathbf u)>\varepsilon\}
\]

be the active set.

### Peak-Based Version

For each \(j\in A^\varepsilon(\mathbf u)\), define the slot-peak set

\[
P_j=\operatorname{argmax}_{x\in X}u^{(j)}(x).
\]

If \(P_j\) is a singleton, write

\[
p_j\in P_j.
\]

If multiple maxima exist, a deterministic tie-break may be used for diagnostics, for example a fixed vertex order on \(X\). A theorem-grade statement should either assume uniqueness or work with the full set \(P_j\).

The peak-based aggregate birth height is

\[
b_j^U=U(p_j).
\]

This version is easy to associate with a labeled slot. Its weakness is that \(p_j\) may not be the true birth vertex of the aggregate persistence bar if the aggregate field \(U\) has a higher nearby point due to overlap or residual contribution.

### Persistence-Pairing Version

Let \(q_j\) denote the actual birth vertex in the \(H_0\) superlevel persistence pairing of \(U\) that is associated with active slot \(j\), if such an association has been defined.

The persistence-pairing birth height is

\[
b_j^{\mathrm{pers}}=U(q_j).
\]

This version is mathematically closer to the barcode, but it requires a slot-to-bar association rule. That association rule is not yet supplied by L1-A.

### Working Recommendation

Use the peak-based version \((p_j,b_j^U)\) for current L-1 working diagnostics and use the persistence-pairing version \((q_j,b_j^{\mathrm{pers}})\) as the future theorem-grade target.

The gap between \(p_j\) and \(q_j\) is part of the slot-to-bar association problem.

## 5. Superlevel Components

For \(j\in A^\varepsilon(\mathbf u)\) and \(\theta\le b_j^U\), define

\[
C_j^\theta(U)
\]

as the connected component of \(G^\theta(U)\) containing \(p_j\), whenever \(p_j\in X^\theta(U)\).

If \(p_j\notin X^\theta(U)\), then \(C_j^\theta(U)\) is undefined.

If two representative peaks \(p_j,p_k\) lie in the same connected component of \(G^\theta(U)\), then the corresponding aggregate formations have merged by level \(\theta\) in the peak-based diagnostic sense.

The peak-based non-merge condition at threshold \(\theta\) is

\[
C_j^\theta(U)\cap C_k^\theta(U)=\emptyset
\]

for all \(j\neq k\) for which both components are defined.

Equivalently, \(p_j\) and \(p_k\) are disconnected in \(G^\theta(U)\).

## 6. Pairwise Bridge Height

For \(j\neq k\in A^\varepsilon(\mathbf u)\), define the pairwise bridge height between representative peaks by

\[
\theta_{\mathrm{bridge}}^{jk}(U)
=
\max_{\gamma:p_j\leadsto p_k}
\min_{x\in\gamma}U(x),
\]

where \(\gamma\) ranges over graph paths from \(p_j\) to \(p_k\).

This max-min path definition is finite because \(G\) is finite. It is the cleanest graph-field definition of the highest-valued bridge connecting the two representative peaks.

Equivalently,

\[
\theta_{\mathrm{bridge}}^{jk}(U)
=
\sup\{\theta\in[0,\min(b_j^U,b_k^U)]:
p_j\text{ and }p_k\text{ are connected in }G^\theta(U)\}.
\]

The equivalence follows from:

\[
p_j,p_k\text{ connected in }G^\theta(U)
\quad\Longleftrightarrow\quad
\exists \gamma:p_j\leadsto p_k
\text{ such that }
\min_{x\in\gamma}U(x)\ge\theta.
\]

Thus \(\theta_{\mathrm{bridge}}^{jk}(U)\) is the largest threshold at which the two peaks are connected by a superlevel path. For thresholds above this value, the peaks are disconnected. At or below this value, they are connected, up to tie conventions on equality.

This is a definition. It is not yet an estimate in terms of support separation, overlap, or field decay.

## 7. Slot Merge Level

The term "slot merge level" can mean two different things. They must not be conflated.

### Pairwise First-Contact Level

For \(j\in A^\varepsilon(\mathbf u)\), define the peak-based active-contact level

\[
\theta_{\mathrm{contact},j}^U
=
\max_{k\in A^\varepsilon(\mathbf u),\,k\neq j}
\theta_{\mathrm{bridge}}^{jk}(U).
\]

If \(|A^\varepsilon(\mathbf u)|=1\), set

\[
\theta_{\mathrm{contact},j}^U=0
\]

under the finite lower-end convention \(U:X\to[0,1]\).

This is the highest threshold at which the representative peak for slot \(j\) first connects to any other active-slot representative peak.

### Persistence Death Level

Let

\[
\theta_{\mathrm{death},j}^U
\]

denote the death value assigned to the bar associated with active slot \(j\) by a chosen \(H_0\) superlevel persistence pairing.

This definition requires:

1. a persistence convention for final surviving components,
2. a tie rule for equal vertex values and plateaus,
3. a slot-to-bar association rule assigning an active slot \(j\) to a persistence bar.

In elder-rule \(H_0\) persistence, when two components merge, the older component survives and the younger component dies. Therefore the first active contact of a slot is not always its persistence death:

- if slot \(j\)'s component merges into an older active component at first contact, then \(\theta_{\mathrm{death},j}^U=\theta_{\mathrm{contact},j}^U\);
- if slot \(j\)'s component is older and survives the first contact, then its death may occur later at a lower threshold or it may be the final surviving component;
- if a non-slot artifact kills or perturbs the associated component, then death may not be governed by active-contact levels.

Therefore no unconditional equality between \(\theta_{\mathrm{death},j}^U\) and \(\theta_{\mathrm{contact},j}^U\) is licensed.

A useful future association estimate would have the form

\[
\theta_{\mathrm{death},j}^U
\le
\theta_{\mathrm{contact},j}^U+r_{\mathrm{assoc}},
\]

where \(r_{\mathrm{assoc}}\) measures elder-rule, peak-mismatch, plateau, and non-slot interference errors. If such an estimate holds, then contact-level margins can be converted into persistence-death margins.

## 8. Persistence Margin

Define the peak/contact margin

\[
\Delta_{j,\mathrm{contact}}^U
=
b_j^U-\theta_{\mathrm{contact},j}^U.
\]

Define the pairing/death margin, when a slot-to-bar association has been fixed, by

\[
\Delta_j^U
=
b_j^{\mathrm{pers}}-\theta_{\mathrm{death},j}^U.
\]

If the peak representative is also the persistence birth representative, this becomes

\[
\Delta_j^U
=
b_j^U-\theta_{\mathrm{death},j}^U.
\]

A dominant bar condition is exact only for the pairing/death margin:

\[
\Delta_j^U\ge\ell_{\min}
\quad\Rightarrow\quad
\text{the associated bar is counted by }
K_{\mathrm{bar}}^{\ell_{\min}}(U).
\]

The peak/contact margin is a candidate sufficient proxy only after an association error bound is supplied. For example, if

\[
\theta_{\mathrm{death},j}^U
\le
\theta_{\mathrm{contact},j}^U+r_{\mathrm{assoc}}
\]

and

\[
b_j^{\mathrm{pers}}\ge b_j^U-r_{\mathrm{birth}},
\]

then

\[
\Delta_j^U
\ge
\Delta_{j,\mathrm{contact}}^U-r_{\mathrm{assoc}}-r_{\mathrm{birth}}.
\]

Thus the sufficient condition

\[
\Delta_{j,\mathrm{contact}}^U
\ge
\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}}
\]

would imply a dominant associated bar.

## 9. Basic Persistence-Margin Lemma Candidate

**L1-A Lemma Candidate — Persistence Margin Gives Dominant Bar.**  
Suppose an active slot \(j\) admits a representative birth vertex \(q_j\) in the \(H_0\) superlevel persistence pairing of \(U\), with birth height

\[
b_j=U(q_j)
\]

and death height

\[
d_j=\theta_{\mathrm{death},j}^U.
\]

If

\[
b_j-d_j\ge\ell_{\min},
\]

then \(U\) has an \(H_0\) bar associated with slot \(j\) counted by

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U).
\]

If this holds for every active slot \(j\in A^\varepsilon(\mathbf u)\), and no non-slot bar has length \(\ge\ell_{\min}\), then

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U)
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

**Status.** The first implication is almost definitional once the slot-to-bar association is fixed. The association rule and no-extra-bar condition remain open. Therefore the full statement is LEMMA-CAND, not Cat-A.

### Stronger Graph-Field Candidate

If a peak/contact margin and association error bound satisfy

\[
b_j^U-\theta_{\mathrm{contact},j}^U
\ge
\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}},
\]

then slot \(j\) should contribute a dominant bar, provided the association inequalities from §8 hold.

This exposes the missing proof obligation: produce \(r_{\mathrm{assoc}}\) and \(r_{\mathrm{birth}}\) from primitive graph/field hypotheses.

## 10. Bridge-Height Estimate Problem

The key future proof problem is to bound

\[
\theta_{\mathrm{bridge}}^{jk}(U)
=
\max_{\gamma:p_j\leadsto p_k}\min_{x\in\gamma}U(x)
\]

using primitive slot conditions rather than persistence output.

The desired estimate has the form

\[
\theta_{\mathrm{bridge}}^{jk}(U)
\le
B(D_{\mathrm{sep}},\eta,h_{\mathrm{noise}},\text{decay profile}),
\]

where \(B\) should be derived from:

- graph distance \(D_{\mathrm{sep}}\),
- field decay away from active supports,
- pairwise overlap \(\eta\),
- local interference bounds,
- aggregate bridge height,
- inactive residual height \(h_{\mathrm{noise}}\),
- boundary smoothness or tail leakage.

If active births satisfy

\[
b_j^U\ge h_{\min},
\]

then a bridge-height bound would imply

\[
b_j^U-\theta_{\mathrm{bridge}}^{jk}(U)
\ge
h_{\min}-B(D_{\mathrm{sep}},\eta,h_{\mathrm{noise}},\text{decay profile}).
\]

A sufficient condition for dominant persistence would be

\[
h_{\min}-B(D_{\mathrm{sep}},\eta,h_{\mathrm{noise}},\text{decay profile})
\ge
\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}}.
\]

This is not proved in this document. L1-A only isolates the estimate needed for L-1.

Graph distance alone is not enough. Two supports can be far in \(d_G\) while \(U\) contains a high-valued corridor connecting them. Conversely, supports can be close but still separated in superlevel persistence if the corridor field value is low.

## 11. Failure Modes

### L1A-F1 — Representative peak mismatch

The chosen peak

\[
p_j\in\operatorname{argmax}u^{(j)}
\]

is not the birth vertex of the aggregate \(H_0\) bar. Then \(b_j^U\) may not equal the persistence birth height.

### L1A-F2 — Elder-rule ambiguity

Two components merge, but elder-rule persistence kills the other component. The active-contact level is then not necessarily the death level of slot \(j\)'s associated bar.

### L1A-F3 — High bridge path

Even if active supports are graph-distant, the aggregate \(U\) has a high-valued path connecting them, causing early merge and shorter persistence.

### L1A-F4 — Low peak margin

The slot peak height is not sufficiently above bridge height:

\[
b_j^U-\theta_{\mathrm{bridge}}^{jk}(U)<\ell_{\min}.
\]

The associated bar may fail to be counted.

### L1A-F5 — Internal secondary peak

A slot contributes multiple candidate birth vertices. This threatens the one-slot / one-bar association needed by L-1.

### L1A-F6 — Inactive peak artifact

An inactive slot or residual field creates a birth vertex with a bar length above \(\ell_{\min}\).

### L1A-F7 — Plateau / tie ambiguity

Multiple vertices share identical values, making birth/death pairing or representative peak selection unstable without an explicit tie rule.

### L1A-F8 — Discrete graph artifact

Bridge height depends strongly on graph resolution, torus boundary conditions, or sampling artifacts rather than the intended SCC geometry.

## 12. Cat-Status Table

| Item | Status | Reason | Upgrade requirement |
|---|---|---|---|
| Superlevel vertex set \(X^\theta(U)\) | DEF | exact once \(G\), \(U\), and \(\theta\) are fixed | none |
| Superlevel graph \(G^\theta(U)\) | DEF | induced finite graph definition | none |
| Peak set \(P_j=\arg\max u^{(j)}\) | DEF / TIE-DEPENDENT | exact as a set; single representative needs tie rule | uniqueness assumption or canonical tie rule |
| Peak birth height \(b_j^U=U(p_j)\) | DEF / DIAGNOSTIC | exact after \(p_j\) is chosen | prove \(p_j\) corresponds to aggregate persistence birth or bound mismatch |
| Pairwise bridge height \(\theta_{\mathrm{bridge}}^{jk}(U)\) | DEF | max-min path value on finite graph | none for definition; estimates still open |
| Contact level \(\theta_{\mathrm{contact},j}^U\) | DEF | maximum active pairwise bridge involving slot \(j\) | active-set and representative-peak choices fixed |
| Persistence death level \(\theta_{\mathrm{death},j}^U\) | PAIRING-DEPENDENT DEF | exact after persistence convention and slot-to-bar association | pairing convention, tie rule, association rule |
| Persistence margin \(\Delta_j^U\) | DEF / PAIRING-DEPENDENT | exact for associated birth/death pair | slot-to-bar association |
| Persistence-margin lemma | LEMMA-CAND / NEAR-DEF | bar counted if associated length \(\ge\ell_{\min}\) | association rule plus no-extra-bar condition |
| Bridge-height estimate | OPEN | graph distance/overlap do not yet imply bridge bound | prove \(B(D_{\mathrm{sep}},\eta,h_{\mathrm{noise}},\text{decay})\) |
| Slot-to-bar association | OPEN | needed to connect labeled slots to barcode bars | define and prove stable association in WS regime |
| L-1 full hard-bar bridge | LEMMA-CAND | L1-A only handles merge/persistence language | add bridge bound, unimodality, inactive suppression |
| Global \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) | FORBIDDEN | false outside well-separated regimes | state only under explicit hypotheses |
| Global \(K_{\mathrm{soft}}^\phi=K_{\mathrm{act}}\) | FORBIDDEN | requires L-1 plus \(\phi\in\Phi_{\mathrm{res}}\), and still only approximate | keep as conditional bridge only |

## 13. Relationship to L-1

L1-A supplies the missing language for L-1 Proof Step 2 and Proof Step 3:

- Step 2 needs a birth-minus-death persistence margin.
- Step 3 needs a bridge-height estimate preventing early merge.

The max-min bridge height

\[
\theta_{\mathrm{bridge}}^{jk}(U)
=
\max_{\gamma:p_j\leadsto p_k}\min_{x\in\gamma}U(x)
\]

is the main finite-graph object that can connect primitive field geometry to superlevel persistence.

L1-A alone does not prove

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

L-1 still also needs:

- internal unimodality / no-extra-bars,
- inactive suppression,
- slot-to-bar association,
- graph perturbation and resolution stability,
- quantitative constants.

## 14. Next Work Packages

### L1-B — Bridge-Height Bound

Derive or test an estimate of the form

\[
\theta_{\mathrm{bridge}}^{jk}(U)
\le
B(D_{\mathrm{sep}},\eta,h_{\mathrm{noise}},\text{decay})
\]

from primitive field/graph conditions.

### L1-C — Slot-to-Bar Association Rule

Define how active slots are associated with persistence bars under elder rule, ties, plateaus, and representative peak mismatch.

### L1-D — Internal Unimodality / No-Extra-Bar Criterion

Guarantee one dominant bar per active slot and rule out extra dominant internal bars.

### L1-E — Inactive Suppression Bound

Show that inactive slots and residual fields produce no dominant bars and do not kill or distort active-slot bars.

## 15. Summary

Merge level and bridge height are now defined on finite superlevel graphs.

The key usable definition is the max-min path bridge height:

\[
\theta_{\mathrm{bridge}}^{jk}(U)
=
\max_{\gamma:p_j\leadsto p_k}\min_{x\in\gamma}U(x).
\]

Dominant persistence follows from a birth-minus-death margin once slot-to-bar association is fixed. The association rule, bridge-height estimate, no-extra-bar condition, and inactive suppression remain open.

L1-A reduces the L-1 bottleneck to explicit subproblems rather than proving the full \(K_{\mathrm{bar}}\) / \(K_{\mathrm{act}}\) bridge.
