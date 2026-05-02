# L1-B: Bridge-Height Bound via Separating Cuts

## 1. Status and Scope

This is a non-canonical working formalization. It formalizes bridge-height bounds needed for the L-1 hard-bar bridge, but it does not prove L-1.

This document separates two layers:

1. **Layer B1 - exact finite-graph fact.** A separating cut whose aggregate field height is bounded gives an upper bound on the max-min bridge height.
2. **Layer B2 - SCC-specific estimate candidate.** Primitive SCC field conditions such as support separation, overlap, field decay, inactive residual height, and graph geometry may imply the required low cut-height bound.

Layer B1 is theorem-grade as a local finite-graph proposition. Layer B2 is not theorem-grade here. It is an estimate program that still requires decay profiles, residual bounds, and graph-geometric separator assumptions.

This document does not:

- solve OP-0005,
- solve OP-0008,
- claim L-1 is proved,
- claim L1-B fully solves the hard-bar bridge,
- promote reservoir theory to canonical status,
- claim \(\sigma_{\mathrm{rich}}\) sufficiency,
- globally identify \(K_{\mathrm{bar}}\), \(K_{\mathrm{soft}}\), and \(K_{\mathrm{act}}\),
- treat WQ-LAT-1 / WQ-LAT-1.B evidence on \(T^2_{20}\) as a general theorem.

## 2. Motivation from L1-A

L1-A defined the pairwise bridge height

\[
\theta_{\mathrm{bridge}}^{jk}(U)
=
\max_{\gamma:p_j\leadsto p_k}
\min_{x\in\gamma}U(x).
\]

It also isolated the persistence-margin requirement. To support a dominant bar associated with active slot \(j\), one wants a condition of the form

\[
b_j^U-\theta_{\mathrm{bridge}}^{jk}(U)
\ge
\ell_{\min}+r_{\mathrm{assoc}},
\]

or more globally

\[
b_j^U-\max_{k\neq j}\theta_{\mathrm{bridge}}^{jk}(U)
\ge
\ell_{\min}+r_{\mathrm{assoc}}.
\]

Thus the next bottleneck is an upper bound on \(\theta_{\mathrm{bridge}}^{jk}(U)\).

Graph distance alone is insufficient. The correct primitive object is a low aggregate-field separator: a cut that every path from \(p_j\) to \(p_k\) must cross, and on which \(U\) is uniformly small.

## 3. Objects and Setup

Let

\[
G=(X,E,w)
\]

be a finite connected graph. The edge weights \(w\) may matter for SCC dynamics, but the cut and path definitions below use only graph adjacency unless stated otherwise.

Let

\[
U:X\to[0,1]
\]

be the aggregate field.

Let \(p_j,p_k\in X\) be active representative peaks for two distinct active slots \(j\neq k\).

Recall the L1-A bridge height:

\[
\theta_{\mathrm{bridge}}^{jk}(U)
=
\max_{\gamma:p_j\leadsto p_k}
\min_{x\in\gamma}U(x),
\]

where \(\gamma\) ranges over graph paths from \(p_j\) to \(p_k\).

Let the \(\delta\)-support of slot \(j\) be

\[
S_j^\delta=\{x:u^{(j)}(x)>\delta\}.
\]

The goal of L1-B is to bound \(\theta_{\mathrm{bridge}}^{jk}(U)\) for \(j\neq k\) from primitive graph/field quantities.

## 4. Why Graph Distance Alone Is Insufficient

Even if

\[
d_G(S_j^\delta,S_k^\delta)\ge D_{\mathrm{sep}},
\]

it does not follow that

\[
\theta_{\mathrm{bridge}}^{jk}(U)
\]

is small.

Counterexample idea: take a path graph with \(p_j\) and \(p_k\) far apart, and set

\[
U(x)=1
\]

on every vertex along the corridor between them. Then the graph distance between active supports can be arbitrarily large, but every path corridor vertex has high aggregate field, so

\[
\theta_{\mathrm{bridge}}^{jk}(U)=1.
\]

Therefore L1-B cannot use distance-only separation. It needs a field-height condition on a separator, or a primitive SCC decay theorem that implies such a condition.

## 5. Separating Cut Definition

A vertex set \(C_{jk}\subset X\) is a **peak-separating cut** between \(p_j\) and \(p_k\) if every graph path

\[
\gamma:p_j\leadsto p_k
\]

intersects \(C_{jk}\):

\[
\gamma\cap C_{jk}\neq\emptyset.
\]

Equivalently, assuming \(p_j,p_k\notin C_{jk}\), the vertices \(p_j\) and \(p_k\) lie in different connected components of

\[
G[X\setminus C_{jk}].
\]

Let

\[
\mathcal C_{jk}
\]

denote the family of peak-separating vertex cuts between \(p_j\) and \(p_k\).

A vertex set \(C_{jk}\subset X\) is a **support-separating cut** between \(S_j^\delta\) and \(S_k^\delta\) if every graph path from any vertex in \(S_j^\delta\) to any vertex in \(S_k^\delta\) intersects \(C_{jk}\).

Support-separating cuts are stronger. Peak-separating cuts are enough to bound \(\theta_{\mathrm{bridge}}^{jk}(U)\) as defined between \(p_j\) and \(p_k\).

## 6. Cut-Height Bound

For a vertex cut \(C\subset X\), define its aggregate cut height by

\[
H_C(U)=\max_{x\in C}U(x).
\]

For a chosen pair cut \(C_{jk}\), write

\[
H_{C_{jk}}(U)=\max_{x\in C_{jk}}U(x).
\]

This is a primitive graph/field quantity. It uses the actual aggregate field \(U\), not the persistence diagram.

Define the best available cut height by

\[
H_{\mathrm{cut}}^{jk}(U)
=
\min_{C\in\mathcal C_{jk}}
\max_{x\in C}U(x),
\]

when \(\mathcal C_{jk}\) is nonempty.

This best-cut quantity is useful diagnostically, but L1-B only needs any explicit cut \(C_{jk}\) with a usable height bound.

## 7. Graph Cut Lemma

**Lemma B1 - Separating Cut Bounds Bridge Height.**  
Let \(C_{jk}\subset X\) be a vertex cut separating \(p_j\) and \(p_k\). Then

\[
\theta_{\mathrm{bridge}}^{jk}(U)
\le
H_{C_{jk}}(U).
\]

In particular, if

\[
H_{C_{jk}}(U)\le B_{jk},
\]

then

\[
\theta_{\mathrm{bridge}}^{jk}(U)\le B_{jk}.
\]

**Proof.**  
Let \(\gamma:p_j\leadsto p_k\) be any graph path. Since \(C_{jk}\) separates \(p_j\) and \(p_k\),

\[
\gamma\cap C_{jk}\neq\emptyset.
\]

Choose \(c\in\gamma\cap C_{jk}\). Then

\[
\min_{x\in\gamma}U(x)
\le
U(c)
\le
\max_{x\in C_{jk}}U(x)
=
H_{C_{jk}}(U).
\]

This holds for every path \(\gamma\). Taking the maximum over all paths gives

\[
\theta_{\mathrm{bridge}}^{jk}(U)
=
\max_{\gamma:p_j\leadsto p_k}\min_{x\in\gamma}U(x)
\le
H_{C_{jk}}(U).
\]

If \(H_{C_{jk}}(U)\le B_{jk}\), the final bound follows immediately. \(\square\)

**Status:** Cat-A local finite-graph fact, conditional only on the stated finite graph and separating-cut definitions.

### Best-Cut Corollary

If \(\mathcal C_{jk}\) is nonempty, then Lemma B1 implies

\[
\theta_{\mathrm{bridge}}^{jk}(U)
\le
H_{\mathrm{cut}}^{jk}(U).
\]

This is immediate because the inequality holds for every \(C\in\mathcal C_{jk}\).

### Bottleneck Cut-Path Duality

There is a likely finite-graph bottleneck duality of the form

\[
\theta_{\mathrm{bridge}}^{jk}(U)
=
\min_{C\in\mathcal C_{jk}}
\max_{x\in C}U(x),
\]

but this equality depends on the precise vertex-cut convention, endpoint exclusion, and plateau/tie handling.

A proof is straightforward under a strict generic condition such as

\[
U(p_j),U(p_k)>\theta_{\mathrm{bridge}}^{jk}(U),
\]

and with cuts excluding \(p_j,p_k\): take the connected component of \(p_j\) in the strict superlevel graph \(\{U>\theta_{\mathrm{bridge}}^{jk}(U)\}\); its vertex boundary separates \(p_j\) from \(p_k\) and has height at most \(\theta_{\mathrm{bridge}}^{jk}(U)\).

Without such convention details, L1-B does not rely on equality. The upper-bound Lemma B1 is enough.

**Status of equality:** conditional Cat-A under explicit generic / endpoint conventions; otherwise LEMMA-CAND / tie-dependent.

## 8. Corridor Suppression Condition

Define the pairwise corridor-suppression condition

\[
\mathrm{CorrSupp}_{jk}(B_{jk})
\]

to mean:

there exists a peak-separating cut \(C_{jk}\in\mathcal C_{jk}\) such that

\[
H_{C_{jk}}(U)\le B_{jk}.
\]

By Lemma B1,

\[
\mathrm{CorrSupp}_{jk}(B_{jk})
\Rightarrow
\theta_{\mathrm{bridge}}^{jk}(U)\le B_{jk}.
\]

This is the correct replacement for graph-distance-only separation:

\[
d_G(S_j^\delta,S_k^\delta)\ge D_{\mathrm{sep}}
\]

is not enough, while

\[
\exists C_{jk}\text{ separating }p_j,p_k
\text{ with }H_{C_{jk}}(U)\le B_{jk}
\]

is sufficient.

## 9. Field-Decays-to-Cut Bound Candidate

This section gives an SCC-specific candidate route to corridor suppression. It is not theorem-grade until the decay profiles and residual bounds are proven or explicitly assumed.

Suppose there exists a support-separating cut \(C_{jk}\) between \(S_j^\delta\) and \(S_k^\delta\). Suppose further that for every \(x\in C_{jk}\),

\[
u^{(j)}(x)\le a_j(D_{\mathrm{sep}},x),
\]

\[
u^{(k)}(x)\le a_k(D_{\mathrm{sep}},x),
\]

and the contribution of all other active and inactive slots is bounded by

\[
\sum_{\ell\notin\{j,k\}}u^{(\ell)}(x)
\le
h_{\mathrm{noise}}.
\]

Then, for \(x\in C_{jk}\),

\[
U(x)
=
\sum_\ell u^{(\ell)}(x)
\le
a_j(D_{\mathrm{sep}},x)
+
a_k(D_{\mathrm{sep}},x)
+
h_{\mathrm{noise}}.
\]

Therefore

\[
H_{C_{jk}}(U)
\le
\max_{x\in C_{jk}}
\left[
a_j(D_{\mathrm{sep}},x)
+
a_k(D_{\mathrm{sep}},x)
+
h_{\mathrm{noise}}
\right].
\]

If the decay envelopes are uniform on the cut,

\[
a_j(D_{\mathrm{sep}},x)\le a_j(D_{\mathrm{sep}}),
\qquad
a_k(D_{\mathrm{sep}},x)\le a_k(D_{\mathrm{sep}}),
\]

then

\[
H_{C_{jk}}(U)
\le
a_j(D_{\mathrm{sep}})
+
a_k(D_{\mathrm{sep}})
+
h_{\mathrm{noise}}.
\]

Thus one may set

\[
B_{jk}
=
a_j(D_{\mathrm{sep}})
+
a_k(D_{\mathrm{sep}})
+
h_{\mathrm{noise}}.
\]

More generally, the desired SCC estimate has the form

\[
B_{jk}
=
B(D_{\mathrm{sep}},\eta,h_{\mathrm{noise}},\text{decay},\text{graph geometry}).
\]

This requires a decay model. Without field decay, local interference bounds, inactive residual bounds, or a directly measured cut-height bound, no such estimate follows from graph distance alone.

## 10. Bridge-Height Bound Candidate

**L1-B Candidate - Primitive Bridge-Height Bound.**  
Suppose for an active pair \(j,k\) there exists a separating cut \(C_{jk}\) satisfying corridor suppression:

\[
H_{C_{jk}}(U)\le B_{jk}.
\]

Then

\[
\theta_{\mathrm{bridge}}^{jk}(U)\le B_{jk}.
\]

This first implication is exactly Lemma B1.

If additionally

\[
b_j^U\ge h_{\min}
\]

and

\[
B_{jk}\le h_{\min}-\ell_{\min}-r_{\mathrm{assoc}},
\]

then

\[
b_j^U-\theta_{\mathrm{bridge}}^{jk}(U)
\ge
\ell_{\min}+r_{\mathrm{assoc}}.
\]

The second implication is algebraic once the cut bound and birth-height lower bound are assumed:

\[
b_j^U-\theta_{\mathrm{bridge}}^{jk}(U)
\ge
h_{\min}-B_{jk}
\ge
\ell_{\min}+r_{\mathrm{assoc}}.
\]

**Status split.**

- Cut-to-bridge implication: Cat-A local finite-graph fact.
- Birth-minus-bridge margin consequence: lemma candidate, because \(r_{\mathrm{assoc}}\) and slot-to-bar association belong to L1-C.
- SCC field-decay route to \(B_{jk}\): open estimate candidate.

## 11. Relationship to Persistence Margin

Using L1-A notation, if

\[
b_j^U\ge h_{\min}
\]

and for all \(k\neq j\),

\[
\theta_{\mathrm{bridge}}^{jk}(U)\le B_{jk},
\]

then

\[
b_j^U-\max_{k\neq j}\theta_{\mathrm{bridge}}^{jk}(U)
\ge
h_{\min}-\max_{k\neq j}B_{jk}.
\]

Thus if

\[
h_{\min}-\max_{k\neq j}B_{jk}
\ge
\ell_{\min}+r_{\mathrm{assoc}},
\]

then slot \(j\) has enough peak/contact margin to potentially support a dominant bar.

However, this still does not prove a counted persistence bar. L1-A showed that contact margin must be converted to a pairing/death margin. That conversion requires:

- a slot-to-bar association rule,
- elder-rule death/contact control,
- plateau/tie handling,
- no non-slot bar interference.

Those are L1-C and later tasks.

## 12. Failure Modes

### L1B-F1 - Distance-only fallacy

Large graph distance without low corridor height does not bound bridge height.

### L1B-F2 - High-valued corridor

A path between active supports has high \(U\), so

\[
\theta_{\mathrm{bridge}}^{jk}(U)
\]

is high even when the supports are far apart.

### L1B-F3 - No low separating cut

Every separating cut contains at least one high-\(U\) vertex. Then no useful cut-height upper bound exists.

### L1B-F4 - Noise accumulation on cut

Many weak inactive or residual slots have small individual values but large aggregate sum on the cut, raising \(H_{C_{jk}}(U)\).

### L1B-F5 - Decay profile absent

No model controls \(u^{(j)}\) away from its active support. Then \(D_{\mathrm{sep}}\) cannot be converted into cut-height suppression.

### L1B-F6 - Association error too large

Even if bridge height is bounded, a large \(r_{\mathrm{assoc}}\) can prevent the persistence-margin conclusion.

### L1B-F7 - Plateau / tie instability

Cut height sits at the same value as birth or merge levels, making the path-cut equality, persistence pairing, or elder-rule death unstable.

### L1B-F8 - Graph-resolution artifact

Cut height changes strongly under graph refinement, torus boundary behavior, or discretization choices.

## 13. Cat-Status Table

| Item | Status | Reason | Upgrade requirement |
|---|---|---|---|
| Peak-separating cut \(C_{jk}\) | DEF | path-intersection separator between \(p_j,p_k\) | none |
| Support-separating cut | DEF | stronger separator between \(S_j^\delta,S_k^\delta\) | none |
| Cut height \(H_C(U)\) | DEF | maximum aggregate field value on a cut | none |
| Best cut height \(H_{\mathrm{cut}}^{jk}(U)\) | DEF | minimum cut height over separating cuts | nonempty cut family and endpoint convention |
| Lemma B1 cut bounds bridge | CAT-A local finite-graph fact | every path crosses the cut, so every path bottleneck is bounded by cut height | none |
| Bottleneck cut-path equality | CONDITIONAL CAT-A / LEMMA-CAND | true under explicit generic endpoint and tie conventions; not needed for L1-B | fix vertex-cut convention and plateau handling |
| Corridor suppression \(\mathrm{CorrSupp}_{jk}(B_{jk})\) | WORKING-DEF | existence of low-height separating cut | none |
| Field-decays-to-cut estimate | OPEN / LEMMA-CAND | requires decay, residual, and graph-geometry assumptions | prove or measure \(B(D_{\mathrm{sep}},\eta,h_{\mathrm{noise}},\text{decay})\) |
| L1-B bridge-height bound candidate | LEMMA-CAND with CAT-A core | cut-to-bridge is proven; SCC route to the cut bound is open | establish corridor suppression from primitive SCC hypotheses |
| Persistence-margin consequence | LEMMA-CAND | requires \(b_j^U\ge h_{\min}\), cut bound, and \(r_{\mathrm{assoc}}\) control | L1-C slot-to-bar association |
| L-1 full hard-bar bridge | LEMMA-CAND | L1-B controls only bridge/contact height | add association, no-extra-bars, inactive suppression |
| Global \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) | FORBIDDEN | false outside well-separated high-margin regimes | state only under explicit hypotheses |
| Global \(K_{\mathrm{soft}}^\phi=K_{\mathrm{act}}\) | FORBIDDEN | requires L-1 plus \(\phi\in\Phi_{\mathrm{res}}\), and still only conditionally approximate | keep as conditional bridge only |

## 14. Relationship to L-1

L1-B supplies a primitive route for controlling the merge/contact level in L-1:

\[
\text{low separating cut}
\Rightarrow
\theta_{\mathrm{bridge}}\text{ low}
\Rightarrow
\text{large contact margin}.
\]

More explicitly:

\[
H_{C_{jk}}(U)\le B_{jk}
\Rightarrow
\theta_{\mathrm{bridge}}^{jk}(U)\le B_{jk}
\Rightarrow
b_j^U-\theta_{\mathrm{bridge}}^{jk}(U)
\ge
b_j^U-B_{jk}.
\]

This addresses the bridge-height part of L-1 Proof Step 3.

L1-B still does not handle:

- slot-to-bar association,
- elder-rule death versus contact level,
- internal extra bars,
- inactive dominant artifacts,
- graph perturbation stability,
- \(\Phi_{\mathrm{res}}\)-based soft-count approximation.

Therefore L1-B does not prove

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

It only reduces the bridge-height problem to corridor suppression and field-decay estimates.

## 15. Next Work Packages

### L1-C - Slot-to-Bar Association Rule

Define a map

\[
\mathcal A_{\mathrm{bar}}:
A^\varepsilon(\mathbf u)
\to
\mathrm{Bars}_0(U)
\]

under well-separated / high-margin conditions.

### L1-D - Internal Unimodality / No-Extra-Bar Criterion

Prevent

\[
K_{\mathrm{bar}}>K_{\mathrm{act}}
\]

by ruling out multiple dominant internal bars per active slot.

### L1-E - Inactive Suppression Bound

Prevent inactive or residual fields from producing dominant bars and from raising cut heights enough to destroy persistence margins.

### L1-F - Empirical WS Diagnostic

Implement diagnostics for:

- cut height,
- bridge height,
- contact margin,
- peak margin,
- active support separation,
- overlap,
- inactive residual contribution.

Do not implement this unless explicitly requested.

## 16. Summary

Graph distance alone is insufficient.

Separating cuts with bounded aggregate height are sufficient to bound bridge height:

\[
H_{C_{jk}}(U)\le B_{jk}
\Rightarrow
\theta_{\mathrm{bridge}}^{jk}(U)\le B_{jk}.
\]

Lemma B1 is a local finite-graph fact. The SCC-specific work is proving that well-separated slots create low separating cuts.

L1-B reduces the bridge-height problem to corridor suppression and field-decay estimates. It does not prove the full \(K_{\mathrm{bar}}\) / \(K_{\mathrm{act}}\) bridge.
