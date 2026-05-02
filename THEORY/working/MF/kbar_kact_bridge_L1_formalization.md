# L-1 Formalization: Well-Separated \(K_{\mathrm{bar}}\) / \(K_{\mathrm{act}}\) Bridge

## 1. Status and Scope

This is a non-canonical working formalization. It does not modify canonical SCC / Multi-Formation theory, does not promote reservoir theory to canonical status, and does not solve OP-0005 or OP-0008.

The target bridge is the hard-count statement

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u)
\]

under explicit well-separated hypotheses.

This document does not claim a completed Cat-A proof. Its role is to isolate the exact theorem candidate, the hypotheses needed for the proof, the proof skeleton, the failure modes, and the missing quantitative ingredients.

This document supports the downstream soft-count bridge

\[
K_{\mathrm{soft}}^\phi
\approx
K_{\mathrm{bar}}
\approx
K_{\mathrm{act}},
\]

but only under the two separate requirements:

1. a well-separated hard-bar bridge,
2. a reservoir-admissible envelope \(\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)\).

It does not globally identify \(K_{\mathrm{bar}}\), \(K_{\mathrm{soft}}^\phi\), and \(K_{\mathrm{act}}^\varepsilon\).

## 2. Motivation

The proof-status audit identified L-1 as the upstream theorem gap:

\[
\text{active slot structure}
\Rightarrow
\text{dominant aggregate }H_0\text{ bars}.
\]

WQ-LAT-1.B gave empirical support for L-2, namely that the soft-count approximation can be made reservoir-stable when \(\phi\) is restricted to sub-threshold suppressing envelopes. That does not by itself connect the field-native morphology count to the labeled active-coordinate count.

The missing step is:

\[
\text{well-separated active slots}
\Rightarrow
\text{one dominant aggregate }H_0\text{ bar per active slot}.
\]

Without this L-1 bridge, the chain

\[
K_{\mathrm{soft}}^\phi(U(\mathbf u))
\approx
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u)
\]

remains incomplete.

## 3. Objects and Notation

Let \(G=(X,E,w)\) be a finite weighted support graph. Here \(X\) is the finite vertex set, \(E\) is the adjacency relation, and \(w\) denotes edge weights or graph-neighborhood weights when needed. The current L-1 bridge uses only the finite graph, its graph distance \(d_G\), and induced subgraphs.

Let

\[
\mathbf u=(u^{(1)},\dots,u^{(K_{\mathrm{field}})})
\in
\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G)
\]

be a finite-chart multi-formation state. The ambient \(\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G)\) is treated here as working notation for a shared-pool multi-formation state over graph \(G\), with finite chart rank \(K_{\mathrm{field}}\) and total mass \(M\).

The active mass of slot \(j\) is

\[
m_j(\mathbf u)=\sum_{x\in X}u^{(j)}(x).
\]

For a fixed activity threshold \(\varepsilon>0\), define the active set

\[
A^\varepsilon(\mathbf u)=\{j:m_j(\mathbf u)>\varepsilon\}.
\]

The active count is

\[
K_{\mathrm{act}}^\varepsilon(\mathbf u)=|A^\varepsilon(\mathbf u)|.
\]

The aggregate field is

\[
U(\mathbf u)(x)=\sum_{j=1}^{K_{\mathrm{field}}}u^{(j)}(x).
\]

For a threshold \(\theta\), the superlevel graph of \(U\) is

\[
G^\theta(U)=G[\{x:U(x)\ge\theta\}],
\]

the induced subgraph on vertices whose aggregate field value is at least \(\theta\).

The \(H_0\) persistence used here is the superlevel persistence of \(U\), with \(\theta\) decreasing from high field values toward low field values. Components are born at local superlevel maxima and die when they merge into older components. For a finite graph, this produces bar lengths \(\ell_i(U)\).

The hard-bar count is

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U)
=
\#\{i:\ell_i(U)\ge\ell_{\min}\}.
\]

It is an integer, thresholded, non-smooth morphology observable on the aggregate field. It is not a labeled slot count by definition.

## 4. Well-Separated Regime Definition

Define the working well-separated regime

\[
\mathrm{WS}(\varepsilon,\delta,D_{\mathrm{sep}},\eta,\ell_{\min},h_{\min},h_{\mathrm{noise}},h_{\mathrm{margin}})
\]

for \(\mathbf u\in\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G)\) as follows. Let

\[
A=A^\varepsilon(\mathbf u).
\]

These hypotheses are intentionally strong. They are designed as sufficient conditions for the L-1 bridge, not as a canonical characterization of all valid SCC multi-formation states.

### WS-1 Active mass

For all \(j\in A\),

\[
m_j(\mathbf u)>\varepsilon.
\]

For all \(j\notin A\),

\[
m_j(\mathbf u)\le\varepsilon.
\]

This is definitional once \(\varepsilon\) is fixed.

### WS-2 Connected active support

For each \(j\in A\), define the \(\delta\)-active support

\[
S_j^\delta=\{x\in X:u^{(j)}(x)>\delta\}.
\]

Require:

1. \(S_j^\delta\neq\emptyset\),
2. \(G[S_j^\delta]\) is connected.

This prevents a single active slot from being split into multiple disconnected high-support regions at the slot level.

### WS-3 Pairwise separation

For distinct \(j,k\in A\), require

\[
d_G(S_j^\delta,S_k^\delta)\ge D_{\mathrm{sep}}.
\]

This is a graph-separation hypothesis. By itself, it does not prove persistence separation; it must eventually be paired with a bound on aggregate bridge height between the supports.

### WS-4 Low overlap / low interference

For distinct \(j,k\in A\), require a low-overlap condition such as

\[
\langle u^{(j)},u^{(k)}\rangle
\le
\eta,
\]

or the normalized variant

\[
\frac{\langle u^{(j)},u^{(k)}\rangle}
{\|u^{(j)}\|_2\|u^{(k)}\|_2}
\le
\eta.
\]

A stronger and more proof-facing version is the local interference bound

\[
\left\|\sum_{k\neq j}u^{(k)}\right\|_{\infty,S_j^\delta}
\le
\eta_{\mathrm{loc}}
\quad
\text{for each }j\in A.
\]

The inner-product condition is easier to measure. The local interference bound is more directly useful for persistence estimates.

### WS-5 Dominant height / persistence margin

Each active slot must produce a robust component in the aggregate field. Choose a representative birth vertex

\[
p_j\in S_j^\delta
\]

where \(U\) attains a local maximum associated with slot \(j\), and set

\[
b_j=U(p_j).
\]

Let \(\theta_{\mathrm{merge},j}^U\) denote the superlevel merge level of the \(H_0\) component born at \(p_j\): the highest threshold at which that component merges into an older component in the superlevel filtration of \(U\). Equivalently, if the associated bar has birth \(b_j\) and death \(d_j\), then \(\theta_{\mathrm{merge},j}^U=d_j\).

Require

\[
b_j-\theta_{\mathrm{merge},j}^U
\ge
\ell_{\min}+h_{\mathrm{margin}}.
\]

This condition is currently partly circular because \(\theta_{\mathrm{merge},j}^U\) is defined using the persistence pairing. A later work package should replace it with primitive graph/field inequalities that imply this persistence margin.

### WS-6 Internal unimodality / no extra dominant bars

Each active slot must not contain multiple separated internal peaks above the persistence threshold. A direct working condition is:

\[
\text{all secondary }H_0\text{ bars of }u^{(j)}
\text{ have length }<\ell_{\min}-h_{\mathrm{margin}}
\quad
\text{for every }j\in A.
\]

An even stronger but simpler diagnostic version is:

\[
K_{\mathrm{bar}}^{\ell_{\min}}(u^{(j)})=1
\quad
\text{for each }j\in A,
\]

with the added requirement that this one bar is stable under the aggregate perturbation

\[
u^{(j)}
\mapsto
U=\sum_k u^{(k)}.
\]

This condition prevents one active slot from contributing more than one dominant aggregate bar.

### WS-7 Inactive-slot suppression

Let

\[
R_A=\sum_{j\notin A}u^{(j)}
\]

be the inactive residual field. Require either the hard-bar suppression condition

\[
K_{\mathrm{bar}}^{\ell_{\min}}(R_A)=0,
\]

or a stronger norm bound such as

\[
\|R_A\|_\infty\le h_{\mathrm{noise}}
\]

with \(h_{\mathrm{noise}}\) small enough that inactive residuals cannot create or extend a bar above \(\ell_{\min}\) after being added to the active aggregate.

### WS-8 Aggregate bridge suppression

For active supports \(S_j^\delta,S_k^\delta\), let \(P_{jk}\) range over graph paths connecting the two supports. Define the aggregate bridge height along a path by

\[
\operatorname{bridge}_U(P_{jk})
=
\min_{x\in P_{jk}}U(x).
\]

A proof-facing condition should bound the highest bridge level between active supports:

\[
\theta_{\mathrm{bridge}}^{jk}
=
\max_{P_{jk}}\operatorname{bridge}_U(P_{jk})
\le
\min(b_j,b_k)-(\ell_{\min}+h_{\mathrm{margin}}).
\]

This condition prevents aggregate low-amplitude corridors from connecting active components too early in the superlevel filtration.

## 5. L-1 Theorem Candidate

**L-1 Candidate — Well-Separated Hard-Bar Bridge.**  
Let \(\mathbf u\in\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G)\) satisfy

\[
\mathrm{WS}(\varepsilon,\delta,D_{\mathrm{sep}},\eta,\ell_{\min},h_{\min},h_{\mathrm{noise}},h_{\mathrm{margin}}).
\]

Then

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

More precisely, if \(A=A^\varepsilon(\mathbf u)\), then the superlevel persistence diagram of \(U(\mathbf u)\) contains exactly \(|A|\) bars of length at least \(\ell_{\min}\), one associated to each active slot, and all other bars have length below \(\ell_{\min}\). Therefore

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
|A|
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

**Status:** LEMMA-CAND, not Cat-A.

The statement is theorem-shaped but still depends on hypotheses that are partly persistence-level rather than fully primitive. In particular, WS-5, WS-6, and WS-8 still need non-circular sufficient conditions stated directly in terms of graph geometry and field values.

## 6. Proof Skeleton

### Step 1 — Birth localization

For each \(j\in A\), use \(S_j^\delta\neq\emptyset\), connectedness of \(G[S_j^\delta]\), and the existence of a representative local maximum \(p_j\in S_j^\delta\) to associate one superlevel component birth to active slot \(j\).

Current status: partial. This is straightforward once the birth vertex \(p_j\) is chosen, but a canonical rule for selecting or identifying \(p_j\) has not yet been fixed.

### Step 2 — Component persistence lower bound

Use the height / merge margin

\[
b_j-\theta_{\mathrm{merge},j}^U
\ge
\ell_{\min}+h_{\mathrm{margin}}
\]

to show that the bar associated with active slot \(j\) has length at least \(\ell_{\min}\).

Current status: conditional. This is proof-level if \(\theta_{\mathrm{merge},j}^U\) is accepted as the death level of the associated persistence pair. It is not yet a primitive sufficient condition.

### Step 3 — Separation prevents early merging

Use graph separation, low overlap, and aggregate bridge suppression to show that distinct active-slot components remain separate above the threshold level needed for persistence length \(\ell_{\min}\).

The desired estimate is that any superlevel path joining the components born near \(S_j^\delta\) and \(S_k^\delta\) appears only at a level at least \(\ell_{\min}+h_{\mathrm{margin}}\) below the relevant birth height.

Current status: open. This is one of the main proof obligations.

### Step 4 — No extra dominant bars inside slots

Use internal unimodality / secondary-bar control to show that each active slot contributes at most one dominant aggregate \(H_0\) bar.

Current status: open. The condition can be assumed directly, but proving it from primitive SCC dynamics or field regularity is not yet done.

### Step 5 — Inactive slots do not contribute

Use inactive-slot suppression to show that inactive residuals create no bars of length at least \(\ell_{\min}\), and do not promote sub-threshold active-slot features into dominant aggregate bars.

Current status: open. The cleanest current version assumes \(K_{\mathrm{bar}}^{\ell_{\min}}(R_A)=0\), but a theorem-grade bridge needs an aggregate perturbation bound.

### Step 6 — Count equality

Steps 1-5 imply:

1. at least one dominant bar per active slot,
2. at most one dominant bar per active slot,
3. no dominant bars from inactive slots or residual artifacts.

Therefore the aggregate superlevel persistence diagram contains exactly \(|A|\) bars of length at least \(\ell_{\min}\). Hence

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U)
=
|A|
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

Current status: conditional. The counting step is direct once the previous steps are established.

## 7. Required Quantitative Constants

| Constant | Role | Current status | Proof need |
|---|---|---|---|
| \(\varepsilon\) | active mass threshold defining \(A^\varepsilon\) | definitional | must be chosen relative to inactive residual scale |
| \(\delta\) | support threshold defining \(S_j^\delta\) | working parameter | must separate genuine slot support from tail/noise |
| \(D_{\mathrm{sep}}\) | graph-distance separation between active supports | working parameter | must imply low bridge height or combine with decay estimates |
| \(\eta\) | pairwise overlap bound | working parameter | needs translation into persistence perturbation control |
| \(\eta_{\mathrm{loc}}\) | local interference bound near active supports | proof-facing parameter | needs measurable diagnostic or derivation |
| \(\ell_{\min}\) | hard-bar persistence threshold | empirical/working | must avoid edge bars and match intended morphology scale |
| \(h_{\min}\) | minimum active peak height | not yet fixed | should lower-bound births \(b_j\) |
| \(h_{\mathrm{noise}}\) | inactive/noise amplitude bound | not yet fixed | should prevent residual dominant bars |
| \(h_{\mathrm{margin}}\) | buffer around \(\ell_{\min}\) | not yet fixed | should absorb perturbation and threshold uncertainty |
| \(\theta_{\mathrm{merge},j}^U\) | death/merge level of slot \(j\)'s aggregate component | persistence-level definition | needs primitive graph/field sufficient condition |
| \(\theta_{\mathrm{bridge}}^{jk}\) | highest aggregate bridge level between active supports | working definition | needs efficient computation and relation to graph separation |
| graph degree / adjacency regularity | controls path and perturbation estimates | not yet used | may be needed for graph-general theorem |

The current WQ-LAT evidence supports \(\ell_{\min}=0.10\) on \(T^2_{20}\) for the tested Option D-2 dynamics. It does not canonically fix \(\ell_{\min}\), nor does it provide general constants for arbitrary graphs or dynamics.

## 8. Failure Modes

### L1-F1 — Overlap collapse

Two active slots overlap or connect above the relevant merge threshold. Then two labeled active coordinates may appear as one aggregate component:

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U)
<
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

### L1-F2 — Internal multimodality

One active slot contains multiple robust internal peaks. Then one labeled active coordinate may produce multiple aggregate bars:

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U)
>
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

### L1-F3 — Weak active slot

An active slot has mass above \(\varepsilon\) but no dominant persistent bar. This can occur when mass is diffuse, flat, or connected to a stronger component at a high merge level.

### L1-F4 — Inactive dominant artifact

An inactive slot or residual field creates a dominant aggregate bar despite having mass below \(\varepsilon\). This breaks the implication from labeled activity to field-native morphology.

### L1-F5 — Threshold instability

One or more bars lie near \(\ell_{\min}\). Then small perturbations of \(U\), graph resolution, or \(\ell_{\min}\) can change \(K_{\mathrm{bar}}^{\ell_{\min}}\).

### L1-F6 — Aggregate bridge connection

A low-amplitude bridge in \(U\) connects components earlier than expected in the superlevel filtration, shortening one or more bars below \(\ell_{\min}\).

### L1-F7 — Graph-resolution artifact

The bridge holds or fails due to discretization, torus boundary effects, or graph-specific sampling artifacts rather than intrinsic SCC structure.

## 9. Relationship to \(K_{\mathrm{soft}}^\phi\) and \(\Phi_{\mathrm{res}}\)

The corrected bridge is a two-step bridge.

First, L-1 aims to prove:

\[
\mathrm{WS}
\Rightarrow
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

Second, the WQ-LAT-1.C correction restricts the soft-count approximation to reservoir-admissible envelopes:

\[
\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)
\Rightarrow
K_{\mathrm{soft}}^\phi(U)
\approx
K_{\mathrm{bar}}^{\ell_{\min}}(U).
\]

Together, the intended conditional bridge is:

\[
\mathrm{WS}
+
\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)
\Rightarrow
K_{\mathrm{soft}}^\phi(U(\mathbf u))
\approx
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

But globally:

\[
K_{\mathrm{soft}}^\phi
\not\equiv
K_{\mathrm{act}}^\varepsilon,
\]

and

\[
K_{\mathrm{bar}}^{\ell_{\min}}
\not\equiv
K_{\mathrm{act}}^\varepsilon.
\]

The soft bridge must not be stated for arbitrary monotone Lipschitz \(\phi\). WQ-LAT-1.B showed that the default smooth saturating envelope accumulated sub-resolution bars and drifted with \(K_{\mathrm{field}}\).

## 10. Relationship to WQ-LAT-1 / WQ-LAT-1.B Evidence

WQ-LAT-1 supports the distinction between finite chart rank and field-native morphology:

1. \(K_{\mathrm{field}}\in\{3,4,6,8,12\}\) was swept.
2. \(K_{\mathrm{act}}\) tracked finite chart rank in the tested LAT-C split-bump setting.
3. \(K_{\mathrm{bar}}^{0.10}(U)\) stayed stable across the tested reservoir refinements.
4. Aggregate fields \(U_K\) and dominant persistence profiles stabilized within the reported tolerances.
5. The default smooth \(K_{\mathrm{soft}}^\phi\) drifted because sub-resolution positive bars accumulated.

WQ-LAT-1.B supports the phi-envelope correction:

1. default \(\phi\)-sat failed chart-invariance,
2. hard threshold had range \(0.000\),
3. logistic threshold with \(s=100\) had range about \(0.001\),
4. shifted-saturating threshold with \(\beta=20\) had range about \(0.005\),
5. the failure mode was sub-resolution bar accumulation.

These results support the need for L-1 but do not prove it. They are empirical results on \(T^2_{20}\), Option D-2 dynamics, and tested geometries / initialization schemes. They should not be treated as a theorem for arbitrary graphs, arbitrary dynamics, or arbitrary SCC states.

## 11. Cat-Status Table

| Item | Status | Reason | Upgrade requirement |
|---|---|---|---|
| \(K_{\mathrm{act}}^\varepsilon(\mathbf u)\) definition | DEF | exact once \(m_j\) and \(\varepsilon\) are fixed | none |
| \(K_{\mathrm{bar}}^{\ell_{\min}}(U)\) definition | DEF | exact hard count once the superlevel barcode and \(\ell_{\min}\) are fixed | none |
| \(\mathrm{WS}\) regime | WORKING-DEF | explicit sufficient-condition package, intentionally strong | replace circular persistence-level clauses with primitive graph/field inequalities |
| L-1 hard-bar bridge | LEMMA-CAND | theorem-shaped conditional statement | prove WS implies exactly one dominant aggregate bar per active slot and no extra bars |
| Proof Step 1: birth localization | PARTIAL | follows after choosing active-slot birth representatives | canonical birth association rule |
| Proof Step 2: persistence lower bound | PARTIAL / OPEN | direct if merge level is already the persistence death level | primitive lower bound for \(b_j-\theta_{\mathrm{merge},j}^U\) |
| Proof Step 3: separation prevents early merging | OPEN | graph distance alone does not control aggregate bridge height | bridge-height estimate from separation, overlap, and field decay |
| Proof Step 4: no extra dominant bars | OPEN | internal multimodality can violate the bridge | unimodality or secondary-bar suppression theorem |
| Proof Step 5: inactive suppression | OPEN | inactive mass below \(\varepsilon\) need not prevent a dominant bar | residual perturbation bound or inactive barcode bound |
| \(\Phi_{\mathrm{res}}\) soft bridge | LEMMA-CAND + EMP | WQ-LAT-1.B supports restricted envelopes | explicit barcode error bound for sub-bars, edge bars, and envelope bias |
| Global \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) | FORBIDDEN | overlap, multimodality, weak slots, and residual artifacts can break equality | only state under explicit hypotheses |
| Global \(K_{\mathrm{soft}}^\phi=K_{\mathrm{act}}\) | FORBIDDEN | depends on both L-1 and admissible \(\phi\), and fails for arbitrary \(\phi\) | only state approximate conditional bridge |

## 12. What Is Still Missing

The main missing proof ingredient is a non-circular implication:

\[
\text{active slot support/separation/overlap conditions}
\Rightarrow
\text{dominant aggregate }H_0\text{ bars}.
\]

Specifically:

1. A precise primitive definition of \(\theta_{\mathrm{merge},j}^U\) or a replacement that does not presuppose the persistence pairing.
2. A theorem linking support separation plus low overlap to persistence separation.
3. A no-extra-dominant-bar criterion inside each active slot.
4. An inactive-slot suppression bound that controls residual contribution to \(U\).
5. Stability under graph perturbations and resolution changes.
6. Quantitative constants, not just qualitative terms like "well-separated" or "low overlap."
7. A diagnostic method for checking WS-1 through WS-8 on actual WQ-LAT trajectories.

Until these are supplied, L-1 remains a lemma candidate rather than a Cat-A theorem.

## 13. Next Work Packages

### L1-A — Merge-Level Formalization

Define \(\theta_{\mathrm{merge},j}^U\) without relying on informal component language. Produce a persistence-margin lemma of the form

\[
b_j-\theta_{\mathrm{merge},j}^U\ge\ell_{\min}+h_{\mathrm{margin}}
\Rightarrow
\ell_j(U)\ge\ell_{\min}.
\]

### L1-B — Internal Unimodality Criterion

Find sufficient conditions ensuring each active slot contributes at most one dominant aggregate bar. Candidate routes include secondary-bar suppression, discrete quasi-concavity on the active support, or a direct barcode assumption.

### L1-C — Inactive-Slot Suppression Bound

Bound the inactive residual field \(R_A\) so it cannot create dominant aggregate bars and cannot promote sub-threshold active-slot features above \(\ell_{\min}\).

### L1-D — Empirical WS Diagnostic

Write a diagnostic script that checks WS-1 through WS-8 on existing WQ-LAT trajectories. This should be done only after the constants and conditions are fixed clearly enough to measure.

## 14. Summary

L-1 is the upstream bottleneck for the \(K_{\mathrm{soft}}\), \(K_{\mathrm{bar}}\), and \(K_{\mathrm{act}}\) bridge.

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u)
\]

can be claimed only under explicit well-separated conditions. It is not a global identity.

The current document provides a theorem candidate, a working well-separated regime, a proof skeleton, quantitative constants, and failure modes. It does not provide a Cat-A proof.

The next mathematical target is merge-level and persistence-margin formalization, followed by internal unimodality and inactive-residual suppression.
