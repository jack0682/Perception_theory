# L1-C: Slot-to-Bar Association Rule

## 1. Status and Scope

This is a non-canonical working formalization. It defines a slot-to-bar association rule needed for the L-1 hard-bar bridge, but it does not prove the full L-1 bridge.

The target object is a controlled association map

\[
\mathcal A_{\mathrm{bar}}:
A^\varepsilon(\mathbf u)
\to
\mathrm{Bars}_0^{\mathrm{term}}(U),
\]

assigning each active labeled slot to an \(H_0\) superlevel persistence bar of the aggregate field \(U\).

This document does not:

- solve OP-0005,
- solve OP-0008,
- promote any canonical claim,
- promote reservoir theory to canonical status,
- claim \(\sigma_{\mathrm{rich}}\) sufficiency,
- claim \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) globally,
- claim \(K_{\mathrm{soft}}=K_{\mathrm{act}}\) globally,
- treat empirical \(T^2_{20}\) evidence as a general theorem.

## 2. Motivation from L1-A / L1-B

L1-A supplied finite-graph superlevel machinery:

\[
G^\theta(U)=G[\{x:U(x)\ge\theta\}],
\]

\[
\theta_{\mathrm{bridge}}^{jk}(U)
=
\max_{\gamma:p_j\leadsto p_k}
\min_{x\in\gamma}U(x).
\]

L1-B supplied a cut-based way to bound bridge height:

\[
C_{jk}\text{ separates }p_j,p_k
\Rightarrow
\theta_{\mathrm{bridge}}^{jk}(U)
\le
\max_{x\in C_{jk}}U(x).
\]

Those results control contact and bridge levels. They still do not say which persistence bar belongs to which active slot.

To conclude

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U)
=
K_{\mathrm{act}}^\varepsilon(\mathbf u),
\]

one still needs:

1. an active slot \(\mapsto\) aggregate \(H_0\) bar association rule,
2. injectivity of that association,
3. a guarantee that each associated bar has length at least \(\ell_{\min}\),
4. a guarantee that every dominant bar is accounted for by some active slot.

L1-C formalizes this association layer.

## 3. Persistence Convention for \(H_0\) Superlevel Bars

For \(U:X\to[0,1]\) on a finite connected graph \(G=(X,E,w)\), define

\[
\mathrm{Bars}_0^{\mathrm{term}}(U)
\]

as the multiset of \(H_0\) superlevel bars under the **terminal-death convention**.

For each component born at height \(b\):

- if it merges into an older component at death level \(d>0\), include the finite bar
  \[
  [d,b];
  \]
- if it survives to the terminal filtration level, assign terminal death
  \[
  d=0
  \]
  and include the bar
  \[
  [0,b].
  \]

The bar length is

\[
\ell=b-d.
\]

The hard-bar count used for L-1 is therefore

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U)
=
\#\{[d,b]\in\mathrm{Bars}_0^{\mathrm{term}}(U):b-d\ge\ell_{\min}\}.
\]

This terminal convention avoids the \(r-1\) finite-bar problem. If \(r\) robust superlevel components are born and eventually merge into one connected component, unreduced persistence with finite bars only records \(r-1\) finite death events. The surviving component would be essential/infinite and could be silently omitted from a finite-bar count. That would make \(K_{\mathrm{bar}}\) undercount robust components by one.

For the L-1 bridge, the surviving component must be counted. The working convention is therefore:

\[
\mathrm{death}(\text{surviving component})=0.
\]

This is a working SCC morphology convention, not a canonical promotion.

### Code Convention Check

The current code already follows the terminal-death convention:

- `CODE/scc/persistence.py::persistence_h0` appends the surviving component as `(birth=max(u), death=0.0)`.
- `CODE/scc/diagnostics.py::_persistence_h0_graph` includes the surviving component as `infinite_bar = max(u)` when computing the two longest bar lengths.
- `CODE/scripts/ksoft_kact_diagnostics.py::h0_barcode` appends `(max(u), 0.0)`.
- `CODE/scc/k_soft.py::k_soft` states that the essential bar is included if its length is positive.
- `CODE/scripts/wq_lat1b_phi_envelope_refinement.py` reuses the WQ-2 barcode function, so its \(K_{\mathrm{bar}}\) and \(K_{\mathrm{soft}}\) post-processing includes the terminal bar.

The implementation uses terminal death \(0\), not omission of the essential bar. Therefore the present L1-C convention is aligned with existing code.

Remaining code caveat: the union-find implementation processes equal field values according to array sorting order. This is deterministic for a fixed run but is not yet a mathematically declared tie convention for plateaus.

## 4. Active Slot Representatives

For each active slot

\[
j\in A^\varepsilon(\mathbf u),
\]

define the slot-peak set

\[
P_j=\operatorname{argmax}_{x\in X}u^{(j)}(x).
\]

If \(P_j\) has a single vertex, write

\[
p_j\in P_j.
\]

If \(P_j\) has multiple vertices, the working diagnostic convention is to choose a deterministic representative, such as the lexicographically first vertex under a fixed vertex ordering.

The peak-based aggregate height is

\[
b_{j,\mathrm{peak}}^U=U(p_j).
\]

This peak representative may not be the actual persistence birth vertex of the aggregate field. The aggregate \(U\) can have a higher nearby point due to overlap, residual fields, or a plateau. Therefore the association rule must distinguish:

- the slot representative \(p_j\),
- the actual aggregate birth vertex \(q_j\),
- the persistence bar born at \(q_j\).

A future theorem-grade version may replace single-vertex representatives by plateau clusters or high-level active regions.

## 5. Candidate Bar Association Map

Define the desired association map

\[
\mathcal A_{\mathrm{bar}}:
A^\varepsilon(\mathbf u)
\to
\mathrm{Bars}_0^{\mathrm{term}}(U).
\]

There are two natural candidate rules.

### Peak-Tracking Rule

For active slot \(j\):

1. Start from representative peak \(p_j\).
2. Follow the connected component \(C_j^\theta(U)\) containing \(p_j\) in the superlevel filtration as \(\theta\downarrow0\).
3. Let \(B_j\) be the \(H_0\) bar whose birth component contains \(p_j\) once \(p_j\) enters the filtration, under the chosen persistence pairing and elder rule.
4. Set
   \[
   \mathcal A_{\mathrm{bar}}(j)=B_j.
   \]

This rule is easy to compute and aligns with L1-A peak/contact notation. It is fragile because \(p_j\) may enter a component that was born elsewhere.

### Support-Birth Rule

For active slot \(j\), let \(S_j^\delta\) be its active support. Associate \(j\) to the unique dominant bar \(B_j=[d_j,b_j]\in\mathrm{Bars}_0^{\mathrm{term}}(U)\) whose birth vertex \(q_j\) lies in \(S_j^\delta\), if such a unique bar exists and has length above the intended dominance scale.

Formally:

\[
\mathcal A_{\mathrm{bar}}(j)=B_j
\quad\text{where}\quad
q_j\in S_j^\delta
\]

and \(B_j\) is the unique dominant bar born at \(q_j\) or in the active birth region associated with \(S_j^\delta\).

This rule is more robust conceptually because it does not require the selected representative \(p_j\) to be the exact birth vertex. It does, however, require a birth-in-support theorem.

### Working Recommendation

Use the support-birth rule as the theorem-target association. Use the peak-tracking rule as a diagnostic approximation.

This choice is stricter but safer: L-1 should not depend on an arbitrary peak tie-break if the actual aggregate birth is a nearby vertex in the same active support.

## 6. Elder Rule and Essential Bar Handling

In \(H_0\) persistence, when two superlevel components merge:

- one component survives,
- one bar dies,
- the surviving component may eventually become the terminal bar.

Thus an active slot can be associated with:

- a finite bar, if its component dies at a merge;
- the terminal bar, if its component survives to the terminal filtration level.

The terminal bar must be counted if every robust component is supposed to contribute to \(K_{\mathrm{bar}}\).

If the terminal bar is not counted, then a configuration of \(r\) robust components that eventually merge into one connected component typically produces only \(r-1\) finite death events. In that convention,

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U)
\]

could equal

\[
K_{\mathrm{act}}^\varepsilon(\mathbf u)-1
\]

even in an otherwise perfectly well-separated regime.

This is why the terminal-death convention is adopted for L-1.

Elder-rule ambiguity remains a separate issue: the slot with the oldest/highest birth may receive the terminal bar, while younger slots receive finite bars. This is acceptable if the terminal bar is included and the slot-to-bar association rule records which active support generated the birth.

## 7. High-Margin Association Regime

Define a working high-margin association regime

\[
\mathrm{HM}(\alpha,\ell_{\min},r_{\mathrm{assoc}},\tau_{\mathrm{tie}})
\]

relative to \(\mathbf u\), \(U\), active set \(A^\varepsilon(\mathbf u)\), and supports \(S_j^\delta\).

### HM-1 Distinct active birth regions

For each active \(j\), there is a high-level component near \(p_j\) that is disjoint from all other active high-level components. A candidate condition is:

\[
C_j^{b_{j,\mathrm{peak}}^U-\alpha}(U)
\cap
C_k^{b_{k,\mathrm{peak}}^U-\alpha}(U)
=
\emptyset
\]

for all \(j\neq k\), whenever both components are defined.

### HM-2 Birth inside active support

The birth vertex \(q_j\) of the bar associated with slot \(j\) lies in or near the slot support:

\[
q_j\in S_j^\delta
\]

or, in a softened version,

\[
d_G(q_j,S_j^\delta)\le r_{\mathrm{birth}}.
\]

### HM-3 Contact margin

The peak/contact margin exceeds the desired persistence threshold plus association error:

\[
b_{j,\mathrm{peak}}^U-\theta_{\mathrm{contact},j}^U
\ge
\ell_{\min}+r_{\mathrm{assoc}}.
\]

The bridge-height bound from L1-B is one route to this condition.

### HM-4 No high inactive births

No inactive or residual component creates a terminal or finite bar of length at least \(\ell_{\min}\):

\[
\text{every non-slot bar has length }<\ell_{\min}.
\]

### HM-5 Tie separation

Birth heights, bridge/contact heights, and relevant death values are separated by a positive tie margin:

\[
|v_1-v_2|\ge\tau_{\mathrm{tie}}
\]

for all distinct relevant critical values \(v_1,v_2\). This avoids plateau ambiguity and unstable elder-rule reassignment.

Under HM-1 through HM-5, the association map is expected to be well-defined and stable under perturbations smaller than the margin constants.

## 8. Injectivity and Coverage

### Injectivity Candidate

If active high-level components are disjoint and remain distinct above their relevant bridge/contact levels, then distinct active slots cannot be assigned to the same bar:

\[
j\neq k
\Rightarrow
\mathcal A_{\mathrm{bar}}(j)\neq\mathcal A_{\mathrm{bar}}(k).
\]

This is plausible under HM-1 and HM-3, but it still requires a formal slot-to-bar birth association proof.

### Coverage Candidate

If no non-slot bar has length at least \(\ell_{\min}\), then every dominant bar belongs to the image of the association map:

\[
\{B\in\mathrm{Bars}_0^{\mathrm{term}}(U):\ell(B)\ge\ell_{\min}\}
\subseteq
\operatorname{Image}(\mathcal A_{\mathrm{bar}}).
\]

Together, injectivity and coverage give:

\[
\#\operatorname{Image}(\mathcal A_{\mathrm{bar}})
=
|A^\varepsilon(\mathbf u)|
=
K_{\mathrm{act}}^\varepsilon(\mathbf u),
\]

and

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U)
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

These are lemma candidates, not theorem-grade claims.

## 9. Association Lemma Candidate

**L1-C Lemma Candidate - Stable Slot-to-Bar Association.**  
Suppose \(\mathbf u\) satisfies the high-margin association regime HM-1 through HM-5, terminal-death \(H_0\) convention is used, and no non-slot bar has length \(\ge\ell_{\min}\). Then there exists an injective association map

\[
\mathcal A_{\mathrm{bar}}:
A^\varepsilon(\mathbf u)
\to
\mathrm{Bars}_0^{\mathrm{term}}(U)
\]

such that each active slot \(j\) is assigned a bar of length at least \(\ell_{\min}\). If coverage holds, then

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U)
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

**Status:** LEMMA-CAND, not Cat-A.

**Missing:** a formal proof that HM-1 through HM-5 follow from primitive SCC assumptions such as support separation, cut-height suppression, field decay, inactive residual bounds, and internal unimodality.

## 10. Failure Modes

### L1C-F1 - Essential bar omitted

If the terminal bar is not counted, \(K_{\mathrm{bar}}\) may equal \(K_{\mathrm{act}}-1\) in a regime with \(r\) robust components that eventually merge into one survivor.

### L1C-F2 - Peak not birth vertex

The representative \(p_j\) is not the persistence birth vertex \(q_j\). Peak-tracking can associate the slot to the wrong bar unless the birth-in-support condition holds.

### L1C-F3 - Two slots share one high-level component

Two active slots already lie in the same high-level aggregate component. The association map is not injective.

### L1C-F4 - Elder-rule reassignment

The component associated with a slot survives or dies differently than expected. This is harmless only if the terminal bar is included and association follows birth support rather than death event alone.

### L1C-F5 - Plateau / tie ambiguity

Equal vertex values make birth/death pairing non-unique or implementation-order dependent.

### L1C-F6 - Non-slot dominant bar

An inactive residual, background artifact, or noise component creates an extra dominant bar.

### L1C-F7 - Internal multimodality

One active slot produces multiple dominant bars. Then coverage can hold but injectivity is not enough to prove equality.

### L1C-F8 - Low-margin instability

Small perturbations of \(U\) change the birth/death pairing or the slot-to-bar association.

### L1C-F9 - Code convention mismatch

The theoretical terminal-death convention differs from the code output. Current code appears aligned, but future code paths must preserve or explicitly convert this convention.

## 11. Cat-Status Table

| Item | Status | Reason | Upgrade requirement |
|---|---|---|---|
| Terminal-death convention | WORKING-DEF | assigns surviving component death \(0\) | canonical decision if promoted |
| Essential bar inclusion | REQUIRED FOR L-1 | avoids \(r-1\) undercount | keep in theory/code or document conversion |
| Code convention check | EMP / CODE-AUDIT | current code appends surviving bar with death \(0\) | add tests if this becomes theorem-critical |
| Peak set \(P_j\) | DEF / TIE-DEPENDENT | exact as a set; representative needs tie rule | plateau/tie convention |
| Peak-based association | WORKING-DEF / FRAGILE | easy diagnostic but representative-dependent | prove peak equals or tracks birth region |
| Support-birth association | LEMMA-CAND | robust theorem target | prove unique dominant birth in \(S_j^\delta\) |
| High-margin regime HM | WORKING-DEF | sufficient-condition package for association | derive HM from primitive SCC assumptions |
| Injectivity | LEMMA-CAND | follows if active birth components remain distinct | formal proof using HM and bridge bounds |
| Coverage | LEMMA-CAND | requires no non-slot dominant bars | L1-D and L1-E |
| Stable association lemma | LEMMA-CAND | theorem-shaped but not fully proven | prove HM conditions and perturbation stability |
| Global association | FORBIDDEN | overlap and multimodality break association | state only under high-margin hypotheses |
| L-1 full hard-bar bridge | LEMMA-CAND | L1-C only handles association | add no-extra-bar and inactive suppression proofs |

## 12. Relationship to L-1

L1-C supplies the missing association map needed to turn L1-A and L1-B contact-margin bounds into actual \(H_0\) bars.

The chain is:

\[
\text{low bridge/contact level}
\Rightarrow
\text{large contact margin}
\Rightarrow
\text{dominant associated bar}
\Rightarrow
\text{count contribution}.
\]

L1-C addresses the third arrow:

\[
\text{large margin}
\Rightarrow
\text{dominant associated bar}.
\]

It still does not prove

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U)
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
\]

The full L-1 bridge still depends on:

- bridge-height bounds from L1-B,
- internal unimodality / no-extra-bar criteria from L1-D,
- inactive suppression from L1-E,
- graph perturbation and tie stability.

## 13. Next Work Packages

### L1-D - Internal Unimodality / No-Extra-Bar Criterion

Guarantee that one active slot contributes at most one dominant bar. This prevents

\[
K_{\mathrm{bar}}>K_{\mathrm{act}}.
\]

### L1-E - Inactive Suppression Bound

Guarantee inactive and residual components do not create dominant bars and do not interfere with active-slot association.

### L1-F - Code Convention Alignment

Add tests or explicit diagnostic conversion ensuring `CODE/scc/persistence.py`, `CODE/scc/diagnostics.py`, and WQ scripts preserve the terminal-death convention.

### L1-G - Empirical Association Diagnostic

Track which slot peak or support maps to which \(H_0\) bar in WQ-LAT trajectories.

## 14. Summary

L1-C defines the slot-to-bar association problem.

The terminal-death convention is necessary to avoid \(r-1\) undercount when robust components eventually merge into one surviving component. Current code already includes the surviving component with death \(0\).

Association is stable only under high-margin, low-tie, no-extra-bar, and no-inactive-artifact hypotheses.

L1-C moves the L-1 bridge closer to theorem-grade, but it does not prove L-1. The next proof targets are internal unimodality / no-extra-bar control and inactive suppression.
