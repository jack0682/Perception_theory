# L1-F: Synthesis of the Hard-Bar Bridge

## 1. Status and Scope

This is a non-canonical working synthesis. It synthesizes L1-A through L1-E into one theorem-candidate package for the hard-bar / active-count bridge

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

It does not prove the theorem. It does not upgrade L-1 to Cat-A. It does not solve OP-0005 or OP-0008. It does not promote reservoir theory to canonical status. It does not claim \(\sigma_{\mathrm{rich}}\) sufficiency.

The purpose is to make the required hypotheses, constants, proof obligations, failure modes, and non-claims explicit. The equality below is conditional on the integrated hypothesis package \(\mathrm{L1Hyp}\), including terminal-death \(H_0\) convention and local-to-global barcode compatibility.

## 2. Task Checklist

- [x] Read L1-A through L1-E.
- [x] Extract all definitions.
- [x] Extract all constants.
- [x] Identify undercount-prevention conditions.
- [x] Identify overcount-prevention conditions.
- [x] Identify local-to-global barcode transfer gaps.
- [x] Build integrated theorem candidate.
- [x] Build proof skeleton.
- [x] Build constants table.
- [x] Build proof-obligation table.
- [x] Build Cat-status table.
- [x] Preserve non-claims.
- [x] Verify created file.

## 3. Executive Synthesis

The hard-bar bridge has two logical halves.

The lower-bound direction is:

\[
\text{active slots}
\Rightarrow
\text{associated dominant bars}
\Rightarrow
K_{\mathrm{bar}}^{\ell_{\min}}(U)
\ge
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

This direction depends on persistence-margin language, bridge/contact control, terminal-death convention, and an injective slot-to-bar association map.

The upper-bound direction is:

\[
\text{no extra active-slot bars}
+
\text{no inactive/residual bars}
\Rightarrow
K_{\mathrm{bar}}^{\ell_{\min}}(U)
\le
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

This direction depends on active secondary-bar suppression, inactive residual suppression, and a local-to-global barcode transfer theorem.

Together:

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U)
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

Component roles:

| Component | Contribution |
|---|---|
| L1-A | Defines finite superlevel graphs, bridge/contact/death levels, and persistence margins. |
| L1-B | Gives the Cat-A local finite-graph cut lemma: low separating cut implies low bridge height. |
| L1-C | Defines slot-to-bar association and requires terminal-death handling for the surviving \(H_0\) component. |
| L1-D | Prevents overcount from active slots by secondary-bar suppression. |
| L1-E | Prevents overcount from inactive slots and residual aggregate structure. |

The weakest unresolved link is the local-to-global barcode transfer problem: local slot and residual barcode conditions do not automatically certify the global barcode of \(U\).

## 4. Objects and Notation

Let

\[
G=(X,E,w)
\]

be a finite weighted graph. Let

\[
\mathbf u=(u^{(1)},\dots,u^{(K_{\mathrm{field}})})
\in
\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G)
\]

be a finite shared-pool multi-formation state.

The active mass of slot \(j\) is

\[
m_j(\mathbf u)=\sum_{x\in X}u^{(j)}(x).
\]

For \(\varepsilon>0\), define

\[
A=A^\varepsilon(\mathbf u)=\{j:m_j(\mathbf u)>\varepsilon\}.
\]

The inactive index set is

\[
I=I^\varepsilon(\mathbf u)
=
\{1,\dots,K_{\mathrm{field}}\}\setminus A.
\]

The active count is

\[
K_{\mathrm{act}}^\varepsilon(\mathbf u)=|A|.
\]

The aggregate field is

\[
U(\mathbf u)(x)=\sum_{j=1}^{K_{\mathrm{field}}}u^{(j)}(x).
\]

The active aggregate and inactive residual are

\[
U_{\mathrm{act}}(x)=\sum_{j\in A}u^{(j)}(x),
\qquad
R_{\mathrm{inact}}(x)=\sum_{j\in I}u^{(j)}(x),
\]

so that

\[
U=U_{\mathrm{act}}+R_{\mathrm{inact}}.
\]

For \(\theta\in[0,1]\), define the superlevel graph

\[
G^\theta(U)=G[\{x\in X:U(x)\ge\theta\}].
\]

This synthesis uses terminal-death \(H_0\) superlevel bars:

\[
\mathrm{Bars}_0^{\mathrm{term}}(U).
\]

Every component born at height \(b\) and dying at merge height \(d>0\) contributes \([d,b]\). The final surviving component is assigned terminal death \(d=0\). This convention is required to avoid an \(r-1\) undercount when \(r\) robust components eventually merge into one connected component.

The hard-bar count is

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U)
=
\#\{[d,b]\in\mathrm{Bars}_0^{\mathrm{term}}(U): b-d\ge\ell_{\min}\}.
\]

This is an unlabeled aggregate morphology count. It is not globally identical to \(K_{\mathrm{act}}^\varepsilon\).

## 5. Integrated Hypothesis Package

Define the working hypothesis package

\[
\mathrm{L1Hyp}
(
\varepsilon,
\ell_{\min},
\delta,
D_{\mathrm{sep}},
h_{\min},
\{B_{jk}\},
r_{\mathrm{assoc}},
r_{\mathrm{birth}},
\rho_{\mathrm{pert}},
\rho_{\mathrm{res}},
\tau_{\mathrm{tie}},
r
).
\]

The package is intentionally strong. Several clauses are currently proof obligations stated as assumptions. This is acceptable for a theorem-candidate synthesis, but not enough for Cat-A promotion.

### H1 - Active Mass and Support

The active set is

\[
A=A^\varepsilon(\mathbf u)=\{j:m_j(\mathbf u)>\varepsilon\}.
\]

For each \(j\in A\), define the \(\delta\)-support

\[
S_j^\delta=\{x:u^{(j)}(x)>\delta\}.
\]

Assume \(S_j^\delta\neq\emptyset\) and \(G[S_j^\delta]\) is connected. For \(j\neq k\in A\), assume support separation

\[
d_G(S_j^\delta,S_k^\delta)\ge D_{\mathrm{sep}}.
\]

This distance condition is not sufficient by itself. It must be paired with bridge-height or cut-height suppression.

### H2 - Birth / Peak Height

For each \(j\in A\), choose an active representative peak \(p_j\in S_j^\delta\), or use a future support-birth representative \(q_j\). The peak-based aggregate birth height is

\[
b_j^U=U(p_j).
\]

Assume

\[
b_j^U\ge h_{\min}.
\]

If \(p_j\) differs from the actual persistence birth vertex \(q_j\), the mismatch must be absorbed by \(r_{\mathrm{birth}}\).

### H3 - Low Bridge Height via Separating Cuts

For each active pair \(j\neq k\), there exists a separating cut \(C_{jk}\subset X\) between \(p_j\) and \(p_k\) such that

\[
H_{C_{jk}}(U)=\max_{x\in C_{jk}}U(x)\le B_{jk}.
\]

By the L1-B finite-graph cut lemma,

\[
\theta_{\mathrm{bridge}}^{jk}(U)
=
\max_{\gamma:p_j\leadsto p_k}\min_{x\in\gamma}U(x)
\le
B_{jk}.
\]

The cut lemma is local and theorem-grade. The existence of such low cuts from primitive SCC field conditions remains open.

### H4 - Persistence-Margin Compatibility

For every \(j\in A\), require

\[
h_{\min}
-
\max_{k\neq j}B_{jk}
\ge
\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}}.
\]

This is the compatibility ledger converting birth and bridge estimates into a candidate persistence margin. Here:

- \(r_{\mathrm{assoc}}\) absorbs the contact-level to persistence-death mismatch, elder-rule effects, and non-slot interference.
- \(r_{\mathrm{birth}}\) absorbs the peak representative to persistence-birth mismatch.

If a later proof works directly with persistence birth/death pairs, these error terms can shrink or disappear. At present they must remain explicit.

### H5 - Slot-to-Bar Association

There exists an injective association map

\[
\mathcal A_{\mathrm{bar}}:
A
\to
\mathrm{Bars}_0^{\mathrm{term}}(U)
\]

such that every \(j\in A\) is assigned a bar of length at least \(\ell_{\min}\).

This is currently a LEMMA-CAND condition inherited from L1-C. It is not yet derived from H1-H4 alone.

### H6 - Active Secondary-Bar Suppression

For each active slot \(j\), let the slot-internal or local slot barcode have sorted lengths

\[
\ell_{j,1}\ge \ell_{j,2}\ge\ell_{j,3}\ge\cdots.
\]

Let

\[
R_j=\sum_{k\neq j}u^{(k)}
\]

and define an active neighborhood

\[
N_j^r=\{x:d_G(x,S_j^\delta)\le r\}.
\]

Assume secondary-bar suppression:

\[
\ell_{j,2}\le\ell_{\min}-\rho_{\mathrm{pert}},
\]

and local aggregate perturbation control:

\[
\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2.
\]

This prevents one active slot from contributing more than one dominant aggregate bar, conditional on local-to-global barcode transfer.

### H7 - Inactive Residual Suppression

Assume the inactive residual satisfies a suppression condition such as

\[
\|R_{\mathrm{inact}}\|_\infty
\le
\ell_{\min}-\rho_{\mathrm{res}},
\]

plus the L1-E local and background clauses:

\[
\|R_{\mathrm{inact}}\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2
\quad
\text{for every }j\in A,
\]

and no residual-born component outside \(\bigcup_{j\in A}N_j^r\) has \(H_0\) terminal bar length \(\ge\ell_{\min}\).

This condition must also prevent inactive residuals from raising corridor heights enough to violate H3.

### H8 - No Non-Slot Dominant Bars

Every dominant bar of \(U\) is in the image of the association map:

\[
\{B\in\mathrm{Bars}_0^{\mathrm{term}}(U):\ell(B)\ge\ell_{\min}\}
\subseteq
\operatorname{Image}(\mathcal A_{\mathrm{bar}}).
\]

This is the coverage condition. It depends on H6, H7, and H10. It is currently a proof-obligation assumption, not an established theorem.

### H9 - Tie / Plateau Stability

Birth heights, bridge heights, death levels, and the threshold \(\ell_{\min}\) are separated by a positive tie margin

\[
\tau_{\mathrm{tie}}>0.
\]

This prevents plateau/tie ambiguity from changing association or bar counting under arbitrarily small perturbations.

### H10 - Local-to-Global Barcode Compatibility

Local active-slot barcode controls and local residual barcode controls transfer to the global aggregate barcode of \(U\).

This is currently open. It is the main theorem-grade gap in the synthesis because H6 and H7 are mostly local conditions while \(K_{\mathrm{bar}}^{\ell_{\min}}(U)\) is global.

## 6. Main Theorem Candidate

**L1-F Theorem Candidate - Conditional Hard-Bar / Active-Count Bridge.**  
Let \(\mathbf u\in\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G)\) be a finite shared-pool multi-formation state on a finite graph \(G\). Suppose \(\mathbf u\) satisfies

\[
\mathrm{L1Hyp}
(
\varepsilon,
\ell_{\min},
\delta,
D_{\mathrm{sep}},
h_{\min},
\{B_{jk}\},
r_{\mathrm{assoc}},
r_{\mathrm{birth}},
\rho_{\mathrm{pert}},
\rho_{\mathrm{res}},
\tau_{\mathrm{tie}},
r
)
\]

with terminal-death \(H_0\) convention. Then

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

**Status:** THEOREM-CAND / LEMMA-CAND, not Cat-A.

The statement splits into two conditional inequalities.

Lower bound:

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U)
\ge
K_{\mathrm{act}}^\varepsilon(\mathbf u)
\]

follows from H5, because \(\mathcal A_{\mathrm{bar}}\) injectively assigns every active slot to a distinct dominant bar.

Upper bound:

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U)
\le
K_{\mathrm{act}}^\varepsilon(\mathbf u)
\]

follows from H8, supported by H6, H7, and H10, because no dominant bar exists outside the active-slot image.

Thus equality follows once all hypotheses are accepted.

## 7. Proof Skeleton

1. Let \(A=A^\varepsilon(\mathbf u)\). By definition,
   \[
   K_{\mathrm{act}}^\varepsilon(\mathbf u)=|A|.
   \]

2. By H5, there is an injective map
   \[
   \mathcal A_{\mathrm{bar}}:A\to\mathrm{Bars}_0^{\mathrm{term}}(U)
   \]
   assigning each active slot a bar of length at least \(\ell_{\min}\). Therefore
   \[
   K_{\mathrm{bar}}^{\ell_{\min}}(U)\ge |A|.
   \]

3. H3 and L1-B bound pairwise bridge heights by \(B_{jk}\). H4 gives the margin needed to convert bridge/contact control into candidate persistence margin, subject to \(r_{\mathrm{assoc}}\) and \(r_{\mathrm{birth}}\).

4. H6 prevents each active slot from producing a second dominant bar, conditional on local-to-global barcode transfer.

5. H7 prevents inactive slots and inactive residual mass from producing independent dominant bars or promoting active secondary bars above threshold, again conditional on local-to-global barcode transfer.

6. By H8, every dominant bar of \(U\) lies in \(\operatorname{Image}(\mathcal A_{\mathrm{bar}})\). Since H5 is injective,
   \[
   K_{\mathrm{bar}}^{\ell_{\min}}(U)\le |A|.
   \]

7. Combine the lower and upper bounds:
   \[
   K_{\mathrm{bar}}^{\ell_{\min}}(U)=|A|=K_{\mathrm{act}}^\varepsilon(\mathbf u).
   \]

This proof is formal if H5, H8, and H10 are assumed. It becomes theorem-grade only when H5, H8, and H10 are derived from primitive SCC graph/field hypotheses with compatible constants.

## 8. Constants and Compatibility Table

| Constant | Role | Appears in | Required relation | Status |
|---|---|---|---|---|
| \(\varepsilon\) | active mass threshold | H1, \(K_{\mathrm{act}}\) | \(j\in A\iff m_j>\varepsilon\) | DEF; not enough to control topology |
| \(\ell_{\min}\) | dominant bar threshold | \(K_{\mathrm{bar}}\), H4, H6, H7 | bar counted iff \(b-d\ge\ell_{\min}\) | WORKING parameter; threshold sensitivity remains |
| \(\delta\) | active support threshold | H1 | \(S_j^\delta\neq\emptyset\), connected | WORKING parameter |
| \(D_{\mathrm{sep}}\) | support separation | H1 | \(d_G(S_j^\delta,S_k^\delta)\ge D_{\mathrm{sep}}\) | Insufficient alone; needs cut/decay estimate |
| \(h_{\min}\) | minimum active birth/peak height | H2, H4 | \(b_j^U\ge h_{\min}\) | WORKING lower bound |
| \(B_{jk}\) | bridge/cut-height upper bound | H3, H4 | \(H_{C_{jk}}(U)\le B_{jk}\), hence \(\theta_{\mathrm{bridge}}^{jk}\le B_{jk}\) | Cut implication Cat-A; SCC derivation open |
| \(r_{\mathrm{assoc}}\) | contact-to-death / elder-rule error | H4, H5 | \(h_{\min}-\max B_{jk}\ge\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}}\) | OPEN constant |
| \(r_{\mathrm{birth}}\) | peak-to-birth representative error | H2, H4 | absorbs \(p_j\) vs persistence birth \(q_j\) mismatch | OPEN constant |
| \(\rho_{\mathrm{pert}}\) | active secondary-bar perturbation budget | H6, H7 | \(\ell_{j,2}\le\ell_{\min}-\rho_{\mathrm{pert}}\), \(\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2\) | LEMMA-CAND margin |
| \(\rho_{\mathrm{res}}\) | inactive residual margin | H7 | \(\|R_{\mathrm{inact}}\|_\infty\le\ell_{\min}-\rho_{\mathrm{res}}\) | LEMMA-CAND margin |
| \(\tau_{\mathrm{tie}}\) | tie / plateau stability margin | H9 | relevant birth/death/threshold values separated | OPEN; needed for stable association |
| \(r\) | active neighborhood radius | H6, H7 | \(N_j^r=\{x:d_G(x,S_j^\delta)\le r\}\) | WORKING localization scale |

Core compatibility inequalities:

\[
h_{\min}-\max_{k\neq j}B_{jk}
\ge
\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}}.
\]

\[
\ell_{j,2}\le\ell_{\min}-\rho_{\mathrm{pert}}.
\]

\[
\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2.
\]

\[
\|R_{\mathrm{inact}}\|_\infty\le\ell_{\min}-\rho_{\mathrm{res}}.
\]

The synthesis is not complete until these inequalities are shown to be simultaneously satisfiable in a nonempty regime.

## 9. Proof-Obligation Table

| Obligation | Source | Needed for | Current status | How to close |
|---|---|---|---|---|
| PO-1 Bridge-height estimate from primitive conditions | L1-B | H3, H4 | Cut lemma Cat-A; SCC cut existence/bound OPEN | Prove field-decays-to-cut or corridor-suppression estimate; diagnose on data |
| PO-2 Slot-to-bar association map existence | L1-C | H5 and lower bound | LEMMA-CAND / OPEN | Prove support-birth association under high-margin and tie-stable regime |
| PO-3 Terminal-death convention alignment | L1-C plus code check | Count all robust components, avoid \(r-1\) undercount | WORKING-DEF / code-aligned | Keep convention explicit; add tests if promoted |
| PO-4 Active secondary-bar suppression proof | L1-D | H6 and upper bound | LEMMA-CAND / OPEN | Prove secondary-bar stability under aggregate perturbation |
| PO-5 Inactive residual suppression proof | L1-E | H7 and upper bound | LEMMA-CAND / OPEN | Prove residual height/persistence conditions prevent residual-born dominant bars |
| PO-6 Local-to-global barcode transfer | L1-D, L1-E | H8, H10 | OPEN, weakest link | Develop theorem transferring local slot/residual controls to global \(U\) barcode |
| PO-7 Tie / plateau stability | L1-A, L1-C | H9, stable association | OPEN | Define deterministic tie rule or prove positive separation margin |
| PO-8 Constants compatibility / nonempty regime | L1-F synthesis | theorem viability | OPEN | Solve or empirically map inequality feasibility region |
| PO-9 Empirical diagnostic validation | WQ-LAT lineage | evidence for assumptions | EMP local only | Implement L1Hyp diagnostic on WQ-LAT, R23, graph families |

## 10. Failure Modes

### L1F-F1 - Undercount by omitted terminal bar

If the terminal surviving component is not counted, \(r\) robust components that eventually merge into one connected component can produce only \(r-1\) finite death events. Then \(K_{\mathrm{bar}}\) can undercount \(K_{\mathrm{act}}\).

### L1F-F2 - High bridge / corridor

Two active slots may be graph-distant but connected by a high-valued corridor in \(U\). Then \(\theta_{\mathrm{bridge}}^{jk}\) is too high and persistence margins collapse.

### L1F-F3 - Association failure

An active slot cannot be assigned a unique dominant bar because of peak/birth mismatch, elder-rule reassignment, shared high-level component, or plateau ambiguity.

### L1F-F4 - Active internal overcount

One active slot produces multiple dominant \(H_0\) bars. Then \(K_{\mathrm{bar}}>K_{\mathrm{act}}\) even without inactive artifacts.

### L1F-F5 - Inactive residual overcount

Inactive slots or residual aggregate mass create a dominant bar despite having mass below \(\varepsilon\). Low mass alone does not prevent a high, narrow persistent spike.

### L1F-F6 - Local-to-global mismatch

Local slot or residual barcode controls fail to predict the global barcode of \(U\). This is the main unresolved theorem gap.

### L1F-F7 - Threshold incompatibility

\(\varepsilon\), \(\ell_{\min}\), \(h_{\min}\), \(B_{jk}\), and residual margins may be mutually incompatible, leaving \(\mathrm{L1Hyp}\) empty.

### L1F-F8 - Tie / plateau instability

Equal or near-equal vertex values change birth/death pairing or bar association under small perturbations.

### L1F-F9 - Graph-resolution artifact

The equality holds or fails because of graph discretization, torus boundary effects, or sampling artifacts rather than stable SCC structure.

### L1F-F10 - Arbitrary \(\phi\)-soft-count leakage

The hard-bar theorem is incorrectly transferred to \(K_{\mathrm{soft}}^\phi\) for arbitrary monotone Lipschitz \(\phi\). WQ-LAT-1.B forbids this; soft-count use requires \(\phi\in\Phi_{\mathrm{res}}\).

## 11. Cat-Status Table

| Item | Status | Reason | Upgrade requirement |
|---|---|---|---|
| Integrated \(\mathrm{L1Hyp}\) package | WORKING-DEF | explicit sufficient-condition package | prove clauses from primitive SCC conditions |
| L1-F theorem candidate | THEOREM-CAND / LEMMA-CAND | equality follows if H5/H8/H10 are assumed | derive H5/H8/H10 and constants |
| Lower bound \(K_{\mathrm{bar}}\ge K_{\mathrm{act}}\) | CONDITIONAL | follows from injective H5 | prove stable association |
| Upper bound \(K_{\mathrm{bar}}\le K_{\mathrm{act}}\) | CONDITIONAL | follows from H8 plus no-extra-bar/no-residual conditions | prove local-to-global coverage |
| Terminal-death convention | WORKING-DEF / CODE-ALIGNED | code includes surviving component with death \(0\) | keep convention explicit; test if canonicalized |
| Bridge-cut lemma | CAT-A local finite-graph fact | separating cut height bounds max-min bridge height | none locally; SCC cut existence still open |
| Slot-to-bar association | OPEN / LEMMA-CAND | elder rule, ties, birth support, terminal bar still need proof | L1-C upgrade |
| No-extra active bars | OPEN / LEMMA-CAND | secondary-bar suppression is local and perturbative | L1-D local-to-global proof |
| Inactive suppression | OPEN / LEMMA-CAND | residual height/persistence conditions need global control | L1-E residual theorem |
| Local-to-global barcode transfer | OPEN | needed by H8/H10 | new theorem or counterexample boundary |
| Constants compatibility | OPEN | margins may be mutually empty | L1-I feasibility study |
| Global \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) | FORBIDDEN | false outside \(\mathrm{L1Hyp}\) | state only conditionally |
| Soft-count corollary | LEMMA-CAND with \(\phi\in\Phi_{\mathrm{res}}\) | depends on hard bridge and envelope restriction | barcode error bounds for \(\rho_{\mathrm{sub}},\rho_{\mathrm{edge}},\rho_\phi\) |

## 12. Downstream Soft-Count Corollary Candidate

If the L1-F hard-bar bridge holds:

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u),
\]

and if

\[
\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau),
\]

then the corrected soft bridge candidate is

\[
K_{\mathrm{soft}}^\phi(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u)
+
O(\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}+\rho_\phi).
\]

Here:

\[
\rho_{\mathrm{sub}}=\sum_{\ell_i<\ell_{\min}}\phi(\ell_i),
\]

\(\rho_{\mathrm{edge}}\) controls bars near \(\ell_{\min}\), and \(\rho_\phi\) controls dominant-bar normalization bias.

This is downstream. It is not valid for arbitrary monotone Lipschitz \(\phi\). WQ-LAT-1.B showed that default smooth saturating envelopes can drift with chart refinement by accumulating sub-resolution bars.

## 13. What Is Still Missing for Cat-A

1. Derive bridge-height bounds from primitive SCC field conditions.
2. Prove slot-to-bar association under a high-margin regime.
3. Prove local-to-global barcode transfer.
4. Prove active no-extra-bar condition from primitive slot structure.
5. Prove inactive suppression from primitive residual bounds.
6. Show constants are simultaneously satisfiable.
7. Add diagnostic tests on WQ-LAT / R23 / other graph families.
8. Decide whether \(\mathrm{L1Hyp}\) should become canonical or remain working-only.

Until these are done, L1-F remains theorem-candidate structure, not theorem-grade mathematics.

## 14. Relationship to OP-0005 / OP-0008

### OP-0005

This does not solve K-selection. It only gives a conditional bridge between a chart-active count and a field-native morphology count:

\[
K_{\mathrm{act}}
\leftrightarrow
K_{\mathrm{bar}}
\leftrightarrow
K_{\mathrm{soft}}^{\Phi_{\mathrm{res}}}
\]

under a well-separated, high-margin, no-extra-bar, inactive-suppressed regime.

It may help reformulate OP-0005 around reservoir-effective morphology, but it does not explain which \(K_{\mathrm{act}}\) emerges.

### OP-0008

This does not solve \(\sigma\)-inheritance or K-jump non-determinism. It only clarifies when active slots and aggregate bars agree.

The bar/slot association machinery may later help describe merger events, but it does not prove \(\sigma_{\mathrm{rich}}\) sufficiency and does not construct a deterministic inheritance map.

## 15. Next Work Packages

### L1-G - Empirical L1Hyp Diagnostic

Implement a diagnostic script checking all \(\mathrm{L1Hyp}\) clauses on existing WQ-LAT outputs:

- active mass and support,
- support separation,
- cut height / bridge height,
- slot association,
- active secondary-bar suppression,
- inactive residual height and residual background bars,
- tie margins,
- constants compatibility.

### L1-H - Local-to-Global Barcode Transfer Theorem

Develop a theorem controlling how local slot and residual barcode conditions transfer to the global aggregate \(U\).

### L1-I - Constants Feasibility Study

Determine whether nonempty parameter regimes satisfy all inequalities in the constants ledger.

### L1-J - Cat-A Upgrade Attempt

Attempt Cat-A upgrade only after L1-G, L1-H, and L1-I produce positive evidence or proof.

## 16. Summary

L1-F synthesizes the hard-bar bridge:

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

The equality is conditional and not theorem-grade. The proof skeleton is clear:

- lower bound by injective slot-to-bar association;
- upper bound by active no-extra-bar, inactive suppression, and coverage;
- terminal-death convention is required to count the surviving component;
- local-to-global barcode transfer is the central unresolved theorem gap.

The next move should be L1-G empirical \(\mathrm{L1Hyp}\) diagnostics or L1-H local-to-global theorem work. For immediate continuation, L1-G is the most concrete next task because it tests whether the synthesized hypothesis package describes a nonempty observed regime before attempting Cat-A proof.
