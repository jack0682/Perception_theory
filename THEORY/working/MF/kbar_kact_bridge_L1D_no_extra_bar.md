# L1-D: Internal Unimodality and No-Extra-Bar Criterion

**File:** `THEORY/working/MF/kbar_kact_bridge_L1D_no_extra_bar.md`  
**Document type:** non-canonical working formalization.  
**Created:** 2026-05-02, after L1-A, L1-B, and L1-C.  
**Status:** lemma-candidate layer only; no canonical promotion.

---

## 1. Status and Scope

This is a non-canonical working note. It formalizes the overcount-prevention side of the L-1 hard-bar bridge:

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
$$

It does not prove the full L-1 bridge. It does not solve OP-0005 or OP-0008. It does not claim \(\sigma_{\mathrm{rich}}\) sufficiency. It does not promote reservoir theory to canonical status.

The specific goal is to prevent the overcount failure

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U)
>
K_{\mathrm{act}}^\varepsilon(\mathbf u),
$$

which can occur if one active slot generates multiple dominant aggregate \(H_0\) bars, or if internal / residual topology produces dominant bars not represented by the slot-to-bar association map of L1-C.

The correct condition is not literal pointwise unimodality. The correct persistence-level target is **secondary-bar suppression**.

---

## 2. Motivation from L1-C

L1-C defined a candidate association map

$$
\mathcal A_{\mathrm{bar}}:
A^\varepsilon(\mathbf u)
\to
\mathrm{Bars}_0^{\mathrm{term}}(U),
$$

where \(\mathrm{Bars}_0^{\mathrm{term}}\) uses the terminal-death convention: the surviving \(H_0\) component is counted with death value \(0\). This convention is aligned with current code paths:

- `CODE/scc/persistence.py::persistence_h0` appends the surviving bar as \((\max u,0)\);
- `CODE/scc/diagnostics.py::_persistence_h0_graph` includes `infinite_bar = max(u)`;
- `CODE/scc/k_soft.py::k_soft` explicitly includes the essential bar when its length exceeds `eps`;
- `CODE/scripts/ksoft_kact_diagnostics.py::h0_barcode` appends the terminal bar with death \(0\).

Even if \(\mathcal A_{\mathrm{bar}}\) is injective and every active slot receives one dominant bar, the bridge can still fail if there are additional dominant bars outside the image:

$$
\mathrm{Image}(\mathcal A_{\mathrm{bar}})
\subsetneq
\{B\in\mathrm{Bars}_0^{\mathrm{term}}(U):\ell(B)\ge\ell_{\min}\}.
$$

L1-D addresses one source of this failure: internal multimodality inside an active slot. L1-E is still needed for inactive or residual bars.

---

## 3. Why "One Local Maximum" Is Not the Right Condition

A field can have several local maxima while still producing only one dominant \(H_0\) persistence bar. Secondary peaks may merge rapidly into the primary component and therefore have short persistence.

Therefore L1-D should not impose:

> each active slot has exactly one local maximum.

That condition is too strong and not persistence-native.

The relevant persistence condition is:

$$
\ell_{j,2}<\ell_{\min},
$$

with a perturbation margin, where \(\ell_{j,2}\) is the second-largest \(H_0\) bar length in the slot-internal barcode, or in a local barcode associated with the slot region.

Local maxima are pointwise / geometric features. Dominant bars are topological / persistence features. L1-D controls dominant bars.

---

## 4. Slot-Internal Bar Profile

Let

$$
\mathbf u=(u^{(1)},\dots,u^{(K_{\mathrm{field}})})
$$

and write the \(j\)-th slot field as

$$
u_j:=u^{(j)}.
$$

There are two candidate barcode domains for \(u_j\).

### 4.1 Full-graph slot barcode

Define

$$
\mathrm{Bars}_0^{\mathrm{term}}(u_j;G)
$$

as the terminal-death \(H_0\) superlevel bar multiset of \(u_j:X\to[0,1]\) on the full graph \(G=(X,E,w)\).

This is easiest to compute and matches the current persistence code convention. Its drawback is that it may include tails or exterior artifacts of \(u_j\) far away from the intended active support.

### 4.2 Local slot barcode

Let

$$
S_j^\delta=\{x:u_j(x)>\delta\}
$$

and choose a local radius \(r\ge0\). Define

$$
N_j^r=\{x\in X:d_G(x,S_j^\delta)\le r\},
\qquad
G_j^r=G[N_j^r].
$$

The local slot barcode is

$$
\mathrm{Bars}_0^{\mathrm{term}}(u_j;G_j^r).
$$

This is more relevant to the active support, but it requires a local-to-global transfer theorem before it can control the aggregate barcode of \(U\) on \(G\).

### 4.3 Sorted bar lengths

For either chosen barcode domain, sort the bar lengths in nonincreasing order:

$$
\ell_{j,1}\ge \ell_{j,2}\ge \ell_{j,3}\ge\cdots.
$$

Define

$$
\ell_{j,\mathrm{sec}}:=\ell_{j,2},
$$

with the convention

$$
\ell_{j,2}=0
$$

if the barcode has fewer than two positive-length bars.

The first bar \(\ell_{j,1}\) is the candidate primary slot bar. The second bar \(\ell_{j,2}\) is the first possible overcount source internal to slot \(j\).

---

## 5. Secondary-Bar Suppression Condition

Let \(\rho_{\mathrm{pert}}\ge0\) be a margin reserved for aggregate perturbations, code/tie conventions, and local-to-global transfer error.

Define the working condition

$$
\mathrm{SecSupp}_j(\ell_{\min},\rho_{\mathrm{pert}})
$$

by:

$$
\ell_{j,1}\ge \ell_{\min}+\rho_{\mathrm{pert}},
$$

and

$$
\ell_{j,2}\le \ell_{\min}-\rho_{\mathrm{pert}}.
$$

Interpretation:

- The first inequality says slot \(j\) has at least one robust bar. This supports L1-C association and undercount prevention.
- The second inequality says slot \(j\) has no second bar near the dominance threshold. This is the overcount-prevention condition used by L1-D.

If the only objective is to prevent overcount from slot \(j\), the essential part is:

$$
\ell_{j,2}\le \ell_{\min}-\rho_{\mathrm{pert}}.
$$

The stronger two-sided form is useful when L1-C and L1-D are later combined.

---

## 6. Aggregate Perturbation by Other Slots

Write the aggregate field as

$$
U=u_j+R_j,
$$

where

$$
R_j=\sum_{k\neq j}u^{(k)}.
$$

On a local neighborhood \(N_j^r\), define the residual perturbation size

$$
\|R_j\|_{\infty,N_j^r}
=
\max_{x\in N_j^r}|R_j(x)|.
$$

The standard persistence-stability input is the bottleneck stability theorem for tame finite filtrations:

$$
d_B\!\left(\mathrm{Dgm}_0(f),\mathrm{Dgm}_0(g)\right)
\le
\|f-g\|_\infty.
$$

For bar lengths, a conservative consequence is that matched lengths can shift by at most roughly

$$
2\|f-g\|_\infty,
$$

because both birth and death values may move by \(\|f-g\|_\infty\). Therefore, if

$$
\|R_j\|_{\infty,N_j^r}\le \rho_{\mathrm{pert}}/2,
$$

then a local secondary bar satisfying

$$
\ell_{j,2}\le \ell_{\min}-\rho_{\mathrm{pert}}
$$

should remain below \(\ell_{\min}\) after adding \(R_j\), provided the local barcode comparison and matching are valid.

This is a standard-tool route, not yet a finished SCC theorem. The exact perturbation constant, the handling of unmatched bars, and the transfer from local \(G_j^r\) bars to global \(G\) bars remain open.

---

## 7. No-Extra-Bar Criterion

Define

$$
\mathrm{NoExtra}_j(\ell_{\min},\rho_{\mathrm{pert}})
$$

as the conjunction of the following working requirements.

**NE-1 Secondary-bar suppression.**

$$
\ell_{j,2}\le\ell_{\min}-\rho_{\mathrm{pert}}.
$$

**NE-2 Local residual perturbation bound.**

$$
\|R_j\|_{\infty,N_j^r}\le \rho_{\mathrm{pert}}/2.
$$

**NE-3 No residual dominant birth inside the slot neighborhood.**

No component created primarily by \(R_j\) inside \(N_j^r\) has terminal-death bar length at least \(\ell_{\min}\).

**NE-4 Local-to-global compatibility.**

Bars born inside the \(j\)-th slot neighborhood in the local comparison correspond to the same aggregate-born bars in the global graph \(G\), up to the stated perturbation margin.

**NE-5 Tie margin.**

Birth, merge, and secondary-bar lengths relevant to \(N_j^r\) are separated from \(\ell_{\min}\) and from each other by a positive tie margin, so the conclusion is not an artifact of equal vertex values or arbitrary sorting.

Under \(\mathrm{NoExtra}_j\), the intended conclusion is:

$$
\text{slot }j\text{ contributes at most one dominant aggregate }H_0\text{ bar.}
$$

This remains a lemma candidate because NE-4 is not yet proven.

---

## 8. Lemma Candidate: One Slot Contributes At Most One Dominant Bar

**L1-D Lemma Candidate - Secondary-Bar Suppression Prevents Overcount.**  
Let \(j\in A^\varepsilon(\mathbf u)\). Suppose the slot-internal bar profile satisfies

$$
\ell_{j,2}\le\ell_{\min}-\rho_{\mathrm{pert}},
$$

and the aggregate perturbation from other slots in the relevant local neighborhood satisfies

$$
\|R_j\|_{\infty,N_j^r}\le \rho_{\mathrm{pert}}/2.
$$

Assume also local-to-global barcode compatibility for bars born in \(N_j^r\), no residual dominant birth inside \(N_j^r\), and a positive tie margin. Then no secondary bar generated inside the \(j\)-th active support can cross the dominance threshold \(\ell_{\min}\) in the aggregate field \(U\). Hence active slot \(j\) contributes at most one dominant \(H_0\) bar to

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U).
$$

**Status:** LEMMA-CAND.

**Missing:**

- exact localization from global barcode to local slot region;
- exact perturbation constant under the terminal-death convention;
- proof that \(R_j\) does not create a new birth component inside \(N_j^r\);
- plateau / tie handling;
- compatibility with elder-rule association from L1-C.

---

## 9. Failure Modes

### L1D-F1 - Internal multimodality

A single active slot has two or more internal bars with length at least \(\ell_{\min}\):

$$
\ell_{j,2}\ge\ell_{\min}.
$$

Then the slot can produce multiple dominant bars and overcount is possible.

### L1D-F2 - Local maximum confusion

A slot has multiple local maxima but only one dominant persistence bar. This is not a failure unless a secondary bar crosses \(\ell_{\min}\). Counting local maxima alone would falsely reject valid states.

### L1D-F3 - Aggregate perturbation creates extra bar

Other slots or residual field \(R_j\) create a new dominant component inside \(N_j^r\), even if \(u_j\) alone has suppressed secondary bars.

### L1D-F4 - Perturbation margin too small

The second bar is too close to threshold:

$$
\ell_{j,2}\approx\ell_{\min}.
$$

Small perturbations, tie-breaking changes, or graph discretization changes can push it above \(\ell_{\min}\).

### L1D-F5 - Local/global barcode mismatch

The local barcode on \(G_j^r\) does not predict the global aggregate barcode on \(G\), because a component born locally later merges through an exterior path or is affected by a global terminal component.

### L1D-F6 - Plateau / tie ambiguity

Equal vertex values create unstable birth/death assignments. The sorted bar profile may be deterministic in code but not yet a mathematical tie convention.

### L1D-F7 - Threshold too low

The threshold \(\ell_{\min}\) is below the noise-band or sub-resolution bar scale, so internal noise features become dominant by definition.

### L1D-F8 - Multi-slot interference

Two nearby slots jointly generate extra internal bars that are not attributable to either \(u_j\) or \(u_k\) alone. This is a failure of local decomposition as well as overcount control.

---

## 10. Cat-Status Table

| Item | Status | Reason | Upgrade requirement |
|---|---|---|---|
| Slot-internal bar profile \(\mathrm{Bars}_0^{\mathrm{term}}(u_j)\) | DEF | terminal-death \(H_0\) barcode once graph domain is chosen | choose full graph or local graph explicitly |
| Sorted lengths \(\ell_{j,1}\ge\ell_{j,2}\ge\cdots\) | DEF / TIE-DEPENDENT | deterministic after barcode and tie convention | formal tie convention for equal values |
| Secondary-bar suppression \(\mathrm{SecSupp}_j\) | WORKING-DEF | encodes one dominant slot bar plus no second dominant bar | decide whether first-bar lower bound belongs here or only L1-C |
| Residual perturbation \(R_j=\sum_{k\neq j}u^{(k)}\) | DEF | exact aggregate decomposition \(U=u_j+R_j\) | none |
| Local neighborhood \(N_j^r\) | WORKING-DEF | required for local perturbation control | choose \(r\) from support / corridor assumptions |
| Persistence stability use | LEMMA-CAND / STANDARD TOOL | bottleneck stability is standard; length shift factor needs convention handling | prove exact bound for terminal-death finite graph barcode |
| \(\mathrm{NoExtra}_j\) condition | WORKING-DEF | combines secondary suppression, perturbation, no residual birth, and local-to-global transfer | formalize NE-3 to NE-5 |
| L1-D no-extra-bar lemma | LEMMA-CAND | plausible by persistence stability plus localization | prove local-to-global barcode transfer and perturbation constants |
| Local/global barcode transfer | OPEN | local slot bars may not match global aggregate bars | prove inclusion/matching theorem for \(G_j^r\subset G\) |
| Aggregate perturbation bound | OPEN | \(\|R_j\|_{\infty,N_j^r}\) must be estimated from primitive SCC hypotheses | derive from separation, corridor suppression, and inactive residual bounds |
| Global no-overcount | LEMMA-CAND | requires \(\mathrm{NoExtra}_j\) for all active slots plus inactive suppression | add L1-E and combine with L1-C |
| Global \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) | FORBIDDEN as an unconditional claim | L1-D only prevents one overcount mechanism | state only under full L1 hypotheses |

---

## 11. Relationship to L-1

L1-D controls the failure direction

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U)
>
K_{\mathrm{act}}^\varepsilon(\mathbf u).
$$

It complements the previous L1 components:

- L1-A defines birth, bridge, contact, death, and persistence margins.
- L1-B gives a finite-graph cut lemma for controlling bridge height.
- L1-C defines slot-to-bar association and terminal-bar handling.
- L1-D prevents each active slot from contributing more than one dominant bar.
- L1-E still needs to prevent inactive / residual fields from contributing dominant bars.

L1-D alone does not prove

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U)
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
$$

The full bridge still requires association, bridge-height bounds, inactive suppression, and local-to-global barcode transfer.

---

## 12. Next Work Packages

### L1-E - Inactive Suppression Bound

Show that inactive slots and residual mass cannot create dominant bars:

$$
K_{\mathrm{bar}}^{\ell_{\min}}
\left(
\sum_{j\notin A^\varepsilon}u^{(j)}
\right)=0
$$

or prove an aggregate version inside the full \(U\)-barcode.

### L1-F - Local-to-Global Barcode Stability

Formalize how local slot bar profiles on \(G_j^r\) transfer to global aggregate bars on \(G\). This is the main missing proof layer for L1-D.

### L1-G - Empirical NoExtra Diagnostic

Specify or implement a diagnostic computing:

- \(\ell_{j,1}\), \(\ell_{j,2}\);
- \(\ell_{\min}-\ell_{j,2}\);
- \(\|R_j\|_{\infty,N_j^r}\);
- local/global barcode mismatch indicators;
- threshold and tie margins.

Do not implement this diagnostic unless explicitly requested.

---

## 13. Summary

L1-D refines "internal unimodality" into secondary-bar suppression. Multiple local maxima are allowed if their secondary persistence is below the dominance threshold.

The central condition is:

$$
\ell_{j,2}\le\ell_{\min}-\rho_{\mathrm{pert}},
$$

plus a residual perturbation margin such as

$$
\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2.
$$

This controls overcount from active slots, but it does not control inactive residual bars and does not prove the full L-1 bridge. The next proof target is L1-E, with L1-F needed soon after to make the local-to-global barcode transfer theorem-grade.
