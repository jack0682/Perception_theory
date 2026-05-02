# L1-E: Inactive Suppression Bound

**File:** `THEORY/working/MF/kbar_kact_bridge_L1E_inactive_suppression.md`  
**Document type:** non-canonical working formalization.  
**Created:** 2026-05-02, after L1-A through L1-D.  
**Status:** lemma-candidate layer only; no canonical promotion.

---

## 1. Status and Scope

This is a non-canonical working note. It formalizes inactive / residual suppression for the L-1 hard-bar bridge:

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u)
$$

under explicit well-separated hypotheses.

It does not prove the full L-1 bridge. It does not solve OP-0005 or OP-0008. It does not claim \(\sigma_{\mathrm{rich}}\) sufficiency. It does not promote reservoir theory to canonical status. It does not identify \(K_{\mathrm{bar}}\), \(K_{\mathrm{soft}}\), and \(K_{\mathrm{act}}\) globally.

The specific goal is to prevent the residual overcount failure

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U)
>
K_{\mathrm{act}}^\varepsilon(\mathbf u),
$$

when the extra dominant bar is created by inactive slots, inactive residual mass, weak slots, noise, or background aggregate structure.

The correct target is not:

$$
m_j(\mathbf u)\le\varepsilon.
$$

The correct target is:

$$
\text{inactive / residual structure contributes no bar of length }\ge\ell_{\min}.
$$

---

## 2. Task Checklist

Actual checklist used for this task:

- [x] Read L1-D, L1-C, L1-B, L1-A, and L1.
- [x] Read bridge/proof-status grounding files for \(K_{\mathrm{soft}}\), \(K_{\mathrm{bar}}\), \(K_{\mathrm{act}}\).
- [x] Read WQ-LAT-1 and WQ-LAT-1.B empirical boundary notes.
- [x] Check persistence / \(K_{\mathrm{soft}}\) code convention where relevant.
- [x] Separate mass suppression from height suppression.
- [x] Define inactive residual field.
- [x] Define inactive persistence suppression.
- [x] State no-dominant-bar lemma candidate.
- [x] List failure modes.
- [x] Build Cat-status table.
- [x] Preserve non-claims.
- [x] Verify created file.

Theory-lab pressure test:

- **Deeper question:** Can inactive suppression be derived from the shared-pool dynamics, or must it remain a diagnostic hypothesis on finite states?
- **Objection:** A residual-only barcode condition may not control aggregate \(U=U_{\mathrm{act}}+R_{\mathrm{inact}}\), because residual mass can interact with active shoulders, bridges, and plateaus.
- **Rival view:** Instead of suppressing inactive residuals by height, one could define the bridge directly by dominant bars of \(U\) and treat \(K_{\mathrm{act}}\) as purely chart-local. That is safer globally but does not prove the desired L-1 equality.
- **Next trigger question:** What local-to-global barcode theorem is strong enough to transfer residual suppression on \(X_{\mathrm{bg}}\) and active neighborhoods into a global \(U\)-barcode bound?

---

## 3. Motivation from L1-D

L1-D prevents one active slot from generating more than one dominant bar. Its target failure direction is:

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U)
>
K_{\mathrm{act}}^\varepsilon(\mathbf u)
$$

caused by internal active-slot multimodality.

Even if L1-D succeeds for every active slot, overcount can still occur if a bar of length at least \(\ell_{\min}\) is born from inactive or residual structure rather than from an active slot. Such a bar is not in the image of the L1-C association map

$$
\mathcal A_{\mathrm{bar}}:
A^\varepsilon(\mathbf u)
\to
\mathrm{Bars}_0^{\mathrm{term}}(U).
$$

Thus L1-E must control bars that are not associated with active slots.

The residual problem is distinct from L1-D:

- L1-D: one active slot should contribute at most one dominant bar.
- L1-E: inactive / residual structure should contribute no dominant bars.

Both are needed for the coverage step in L1-C.

---

## 4. Why Low Mass Is Not Enough

The inactivity condition

$$
m_j(\mathbf u)\le\varepsilon
$$

does not by itself imply that \(u^{(j)}\) creates no dominant \(H_0\) bar.

On a finite graph, take one inactive slot concentrated at a single vertex:

$$
u^{(j)}(x_0)=h,
\qquad
u^{(j)}(x)=0\quad\text{for }x\neq x_0.
$$

Then

$$
m_j(\mathbf u)=h.
$$

Under the terminal-death \(H_0\) convention used by L1-C and current code, the spike creates a terminal bar of length

$$
\ell=h.
$$

If

$$
\ell_{\min}\le h\le\varepsilon,
$$

then the slot is inactive by mass but dominant by persistence:

$$
m_j(\mathbf u)\le\varepsilon,
\qquad
K_{\mathrm{bar}}^{\ell_{\min}}(u^{(j)})\ge1.
$$

Therefore mass suppression is only an activity-label definition. It is not a morphology suppression theorem.

For nonnegative fields, a stronger special case exists:

$$
\|u^{(j)}\|_\infty\le \|u^{(j)}\|_1=m_j(\mathbf u).
$$

Thus if one additionally assumes \(\varepsilon<\ell_{\min}\), then individual inactive slots have height below \(\ell_{\min}\). But this still does not control the aggregate residual sum

$$
R_{\mathrm{inact}}=\sum_{j\in I^\varepsilon}u^{(j)},
$$

because many small inactive slots can accumulate at the same vertex or along a corridor. L1-E therefore separates mass suppression, height suppression, persistence suppression, and aggregate residual suppression.

---

## 5. Inactive Slot and Residual Definitions

Let

$$
\mathbf u=(u^{(1)},\dots,u^{(K_{\mathrm{field}})})
$$

be a finite-chart multi-formation state on a finite graph \(G=(X,E,w)\).

The active mass of slot \(j\) is

$$
m_j(\mathbf u)=\sum_{x\in X}u^{(j)}(x).
$$

For a fixed activity threshold \(\varepsilon>0\), define the active set

$$
A^\varepsilon(\mathbf u)
=
\{j:m_j(\mathbf u)>\varepsilon\}.
$$

Define the inactive index set

$$
I^\varepsilon(\mathbf u)
=
\{1,\dots,K_{\mathrm{field}}\}\setminus A^\varepsilon(\mathbf u).
$$

Define the inactive residual field

$$
R_{\mathrm{inact}}(x)
=
\sum_{j\in I^\varepsilon(\mathbf u)}u^{(j)}(x).
$$

Define the active aggregate

$$
U_{\mathrm{act}}(x)
=
\sum_{j\in A^\varepsilon(\mathbf u)}u^{(j)}(x).
$$

Then the full aggregate decomposes as

$$
U(x)=U_{\mathrm{act}}(x)+R_{\mathrm{inact}}(x).
$$

Define the inactive aggregate height

$$
h_{\mathrm{inact}}
=
\|R_{\mathrm{inact}}\|_\infty
=
\max_{x\in X}R_{\mathrm{inact}}(x).
$$

For each inactive slot \(j\in I^\varepsilon(\mathbf u)\), define its per-slot height

$$
h_j^\infty
=
\|u^{(j)}\|_\infty.
$$

For active-slot neighborhoods from L1-D, let

$$
N_j^r=\{x\in X:d_G(x,S_j^\delta)\le r\},
\qquad j\in A^\varepsilon(\mathbf u).
$$

Define the background region

$$
X_{\mathrm{bg}}
=
X\setminus\bigcup_{j\in A^\varepsilon(\mathbf u)}N_j^r.
$$

The inactive residual has two roles:

1. inside \(N_j^r\), it perturbs active-slot bars;
2. on \(X_{\mathrm{bg}}\), it can create independent residual-born bars.

---

## 6. Mass, Height, and Persistence Suppression

There are three distinct levels of inactive suppression. They should not be conflated.

### E1 - Mass suppression

For inactive slots,

$$
m_j(\mathbf u)\le\varepsilon,
\qquad
j\in I^\varepsilon(\mathbf u).
$$

**Status:** definitional for inactivity.

**Limitation:** insufficient by itself. A low-mass slot can be a tall narrow spike, and many low-mass slots can accumulate in the aggregate.

### E2 - Height suppression

Per-slot height suppression is:

$$
\|u^{(j)}\|_\infty\le h_{\mathrm{slot}},
\qquad
j\in I^\varepsilon(\mathbf u).
$$

Aggregate residual height suppression is:

$$
\|R_{\mathrm{inact}}\|_\infty\le h_{\mathrm{res}}.
$$

Height suppression is more primitive than a barcode condition and directly bounds residual birth heights. Because terminal-death bar lengths satisfy

$$
\ell=b-d\le b\le \|R_{\mathrm{inact}}\|_\infty
$$

for residual-only bars with death \(d\ge0\), the strong condition

$$
\|R_{\mathrm{inact}}\|_\infty<\ell_{\min}
$$

implies the residual field alone has no terminal-death bar of length at least \(\ell_{\min}\).

**Limitation:** residual height suppression for \(R_{\mathrm{inact}}\) alone does not automatically control interactions with \(U_{\mathrm{act}}\).

### E3 - Persistence suppression

Residual persistence suppression is:

$$
K_{\mathrm{bar}}^{\ell_{\min}}(R_{\mathrm{inact}})=0,
$$

or equivalently

$$
\max\{\ell:\ell\in\mathrm{Bars}_0^{\mathrm{term}}(R_{\mathrm{inact}})\}<\ell_{\min}.
$$

With margin \(\rho_{\mathrm{res}}>0\), use:

$$
K_{\mathrm{bar}}^{\ell_{\min}-\rho_{\mathrm{res}}}(R_{\mathrm{inact}})=0.
$$

This is the direct topological condition. It is persistence-facing rather than primitive, but it is closest to the desired no-extra-bar conclusion.

### E4 - Aggregate residual suppression

Aggregate suppression controls the effect of \(R_{\mathrm{inact}}\) after it is added to \(U_{\mathrm{act}}\):

$$
U=U_{\mathrm{act}}+R_{\mathrm{inact}}.
$$

This requires at least:

1. small residual perturbation in active neighborhoods,
2. no residual-born dominant bars in the background,
3. no residual-raised corridor that changes bridge/contact levels enough to break active bar margins.

E4 is the theorem-grade target. E1, E2, and E3 are ingredients.

---

## 7. Aggregate Residual Suppression Condition

Define a working condition

$$
\mathrm{InactSupp}(\ell_{\min},\rho_{\mathrm{res}},\rho_{\mathrm{pert}},r)
$$

relative to \(\mathbf u\), \(G\), the active set \(A=A^\varepsilon(\mathbf u)\), active neighborhoods \(N_j^r\), and background \(X_{\mathrm{bg}}\).

### Strong height-based sufficient condition

The strongest simple version requires:

**IS-H1 Global residual height bound.**

$$
\|R_{\mathrm{inact}}\|_\infty
\le
\ell_{\min}-\rho_{\mathrm{res}}.
$$

This implies that residual-only bars cannot reach \(\ell_{\min}\), since all residual-only bar births are below \(\ell_{\min}-\rho_{\mathrm{res}}\).

**IS-H2 Active-neighborhood perturbation bound.**

For every active slot \(j\in A\),

$$
\|R_{\mathrm{inact}}\|_{\infty,N_j^r}
\le
\rho_{\mathrm{pert}}/2.
$$

This is the L1-D style perturbation margin needed to keep active-slot secondary bars from being promoted above \(\ell_{\min}\).

**IS-H3 Background residual no-birth condition.**

Every component born primarily from \(R_{\mathrm{inact}}\) on \(X_{\mathrm{bg}}\) has terminal-death bar length below \(\ell_{\min}\).

Under IS-H1 this is redundant for the residual-alone field, but it is retained because the aggregate \(U_{\mathrm{act}}+R_{\mathrm{inact}}\) can have background shoulders or bridges not present in \(R_{\mathrm{inact}}\) alone.

**IS-H4 Corridor reinforcement bound.**

For every active pair \(j,k\), the residual contribution on any separating cut used by L1-B is bounded so that

$$
H_{C_{jk}}(U_{\mathrm{act}}+R_{\mathrm{inact}})
\le
B_{jk}
$$

still holds with the margin required by L1-B and L1-C.

### Persistence-facing sufficient condition

A weaker but more direct topological version replaces IS-H1 with:

**IS-P1 Residual barcode suppression.**

$$
K_{\mathrm{bar}}^{\ell_{\min}-\rho_{\mathrm{res}}}(R_{\mathrm{inact}})=0.
$$

IS-P1 is weaker than global height suppression but more circular: it already uses the \(H_0\) barcode. It is useful diagnostically and may be enough for a conditional lemma, but a primitive theorem should eventually derive it from graph/field estimates.

### Working reading

The default L1-E working condition is:

$$
\mathrm{InactSupp}
=
\text{IS-H1 + IS-H2 + IS-H4}
$$

with IS-H3 or IS-P1 added when the background is not empty or when residual-only topology is being audited directly.

The clauses are intentionally stronger than necessary. Their purpose is to prevent residual overcount without claiming a global equivalence between label activity and field morphology.

---

## 8. Inactive No-Dominant-Bar Lemma Candidate

**L1-E Lemma Candidate - Inactive Suppression Prevents Residual Overcount.**  
Let

$$
U=U_{\mathrm{act}}+R_{\mathrm{inact}}
$$

be the aggregate decomposition associated with \(A^\varepsilon(\mathbf u)\). Suppose \(R_{\mathrm{inact}}\) satisfies

$$
\mathrm{InactSupp}(\ell_{\min},\rho_{\mathrm{res}},\rho_{\mathrm{pert}},r),
$$

including the global residual height bound

$$
\|R_{\mathrm{inact}}\|_\infty
\le
\ell_{\min}-\rho_{\mathrm{res}},
$$

and local perturbation bounds near all active supports:

$$
\|R_{\mathrm{inact}}\|_{\infty,N_j^r}
\le
\rho_{\mathrm{pert}}/2,
\qquad
j\in A^\varepsilon(\mathbf u).
$$

Assume also a local-to-global residual control theorem: residual-born components in \(X_{\mathrm{bg}}\) and residual perturbations inside active neighborhoods do not create new global aggregate bars of length at least \(\ell_{\min}\). Then inactive slots and residual aggregate mass do not create any additional \(H_0\) bar of length \(\ge\ell_{\min}\) in \(U\) outside the bars associated with active slots. Therefore inactive residuals do not increase

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U)
$$

beyond the active-slot contribution.

**Status:** LEMMA-CAND, not Cat-A.

**Proof skeleton.**

1. IS-H1 implies all residual-only birth heights are below \(\ell_{\min}-\rho_{\mathrm{res}}\), so residual-only terminal bars are below \(\ell_{\min}\).
2. IS-H2 bounds residual perturbation in active neighborhoods, so L1-D secondary-bar suppression is not destroyed by inactive residuals.
3. IS-H4 prevents residuals from raising active-to-active corridors enough to break L1-B bridge-height margins.
4. The assumed local-to-global residual control theorem rules out global aggregate bars born from background residual artifacts.
5. Thus every dominant bar of \(U\) remains attributable to an active slot, modulo L1-C association and L1-D no-extra-bar hypotheses.

**Missing:**

- rigorous local-to-global barcode perturbation theorem;
- proof that residual does not merge active components in a way that creates extra births or changes elder-rule assignments;
- exact constants connecting \(\rho_{\mathrm{res}}\), \(\rho_{\mathrm{pert}}\), \(\ell_{\min}\), L1-B margins, and L1-D margins;
- background/active-neighborhood decomposition stability under graph refinement.

---

## 9. Interaction with Active Slot Neighborhoods

Inactive residuals affect the L-1 bridge in two different locations.

### 9.1 Active neighborhoods

Inside active neighborhoods \(N_j^r\), residuals perturb active slot topology:

$$
U|_{N_j^r}
=
U_{\mathrm{act}}|_{N_j^r}
+
R_{\mathrm{inact}}|_{N_j^r}.
$$

The needed bound is:

$$
\|R_{\mathrm{inact}}\|_{\infty,N_j^r}
\le
\rho_{\mathrm{pert}}/2.
$$

This connects directly to L1-D:

- L1-D controls active secondary bars under a perturbation budget.
- L1-E supplies the inactive part of that perturbation budget.

If this bound fails, inactive residuals can promote a secondary active-slot bar above \(\ell_{\min}\), producing overcount.

### 9.2 Background region

Decompose

$$
X
=
\left(\bigcup_{j\in A}N_j^r\right)
\cup
X_{\mathrm{bg}}.
$$

On the background region, the required condition is:

$$
K_{\mathrm{bar}}^{\ell_{\min}}
\left(
R_{\mathrm{inact}}|_{X_{\mathrm{bg}}}
\right)
=
0,
$$

or a stronger height version:

$$
\|R_{\mathrm{inact}}\|_{\infty,X_{\mathrm{bg}}}
<
\ell_{\min}.
$$

This prevents independent residual-born components from becoming dominant bars.

### 9.3 Corridors between active slots

Residuals can also raise the field on corridors between active components. In L1-B notation, if \(C_{jk}\) is a separating cut, then:

$$
H_{C_{jk}}(U)
=
\max_{x\in C_{jk}}
\left[
U_{\mathrm{act}}(x)+R_{\mathrm{inact}}(x)
\right].
$$

Even if \(U_{\mathrm{act}}\) has a low cut height, \(R_{\mathrm{inact}}\) can raise the cut height and increase

$$
\theta_{\mathrm{bridge}}^{jk}(U).
$$

This usually threatens undercount by early merge rather than residual overcount, but it is still part of L-1 because it can destroy persistence margins and elder-rule associations.

Therefore L1-E is not only a no-extra-bar condition. It also supplies the residual term needed in L1-B corridor suppression.

---

## 10. Failure Modes

### L1E-F1 - Low-mass high-spike inactive slot

A slot satisfies \(m_j(\mathbf u)\le\varepsilon\) but has a spike with height at least \(\ell_{\min}\). Under terminal-death convention it can create a dominant bar even though it is inactive by mass.

### L1E-F2 - Residual accumulation

Many inactive slots are individually small, but their sum satisfies

$$
\|R_{\mathrm{inact}}\|_\infty\ge\ell_{\min}
$$

or creates a persistent residual component. The aggregate residual, not each slot alone, is the dangerous object.

### L1E-F3 - Background residual component

Residual field outside active neighborhoods creates an independent background component with bar length at least \(\ell_{\min}\).

### L1E-F4 - Active-neighborhood perturbation

Residual field inside \(N_j^r\) pushes a secondary active-slot bar above \(\ell_{\min}\), invalidating L1-D.

### L1E-F5 - Bridge reinforcement

Residual field raises a corridor or separating cut between active supports. This can increase bridge height, cause earlier merge, and alter persistence margins.

### L1E-F6 - Threshold mismatch

\(\varepsilon\) and \(\ell_{\min}\) are incompatible. A slot can be inactive by mass but active by persistence if

$$
\ell_{\min}\le m_j(\mathbf u)\le\varepsilon.
$$

### L1E-F7 - Local/global mismatch

Residual barcode on \(X_{\mathrm{bg}}\) does not predict the global aggregate barcode on \(G\). Background residuals may connect to active shoulders or terminal components in the full graph.

### L1E-F8 - Terminal-bar artifact

With terminal-death convention, any residual component with maximum height \(h\) can produce a terminal bar of length \(h\). It is counted whenever

$$
h\ge\ell_{\min}.
$$

This makes height suppression especially important for residual fields.

---

## 11. Cat-Status Table

| Item | Status | Reason | Upgrade requirement |
|---|---|---|---|
| Inactive index set \(I^\varepsilon(\mathbf u)\) | DEF | complement of active set after \(\varepsilon\) is fixed | none |
| Inactive residual \(R_{\mathrm{inact}}\) | DEF | exact sum over inactive slots | none |
| Active aggregate \(U_{\mathrm{act}}\) | DEF | exact sum over active slots | none |
| Mass suppression | DEF but insufficient | defines inactive labels, not morphology | add height/persistence/aggregate bounds |
| Low-mass does not imply no dominant bar | CAT-A finite-graph observation | one-vertex spike gives bar length equal to height | none |
| Height suppression | WORKING-DEF / strong sufficient condition | bounds residual-only birth heights | prove interaction control after adding \(U_{\mathrm{act}}\) |
| Persistence suppression | WORKING-DEF / direct but persistence-facing | directly states no residual dominant bar | derive from primitive graph/field conditions |
| \(\mathrm{InactSupp}\) condition | WORKING-DEF | combines residual height, local perturbation, background, and corridor bounds | choose minimal nonredundant hypotheses |
| Inactive no-dominant-bar lemma | LEMMA-CAND | plausible under strong residual bounds plus local-to-global control | prove local-to-global residual theorem and constants |
| Local-to-global residual control | OPEN | residual-only bars may not match global aggregate bars | theorem for background/active-neighborhood decomposition |
| Corridor residual contribution | OPEN / LEMMA-CAND | residual can raise L1-B cut heights | integrate into \(B_{jk}\) estimates |
| Global no-overcount | LEMMA-CAND | requires L1-D plus L1-E for all active/inactive regions | synthesize with L1-A/B/C |
| Global \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) | FORBIDDEN as an unconditional claim | L1-E handles only inactive residual overcount | state only under full L1 hypotheses |
| Global \(K_{\mathrm{soft}}=K_{\mathrm{act}}\) | FORBIDDEN | additionally requires \(\Phi_{\mathrm{res}}\) and remains approximate | keep as conditional bridge only |

---

## 12. Relationship to L-1

L1-E closes the inactive residual overcount side of the L-1 bridge.

The L1 proof architecture is now:

- L1-A defines persistence margins, bridge/contact/death levels, and terminal-death bookkeeping.
- L1-B bounds bridge height using separating cuts and corridor suppression.
- L1-C associates active slots to terminal-death \(H_0\) bars.
- L1-D prevents active slots from creating multiple dominant bars.
- L1-E prevents inactive / residual structure from creating extra dominant bars and supplies residual bounds needed for corridor suppression.

Even after L1-E, L-1 is not automatically Cat-A. The components still need to be synthesized into one theorem statement with compatible constants:

$$
\rho_{\mathrm{res}},\rho_{\mathrm{pert}},\rho_{\mathrm{assoc}},h_{\mathrm{margin}},B_{jk},\ell_{\min}.
$$

The remaining theorem-grade gap is not conceptual naming; it is the local-to-global barcode and perturbation transfer needed to combine all components on the global aggregate field \(U\).

---

## 13. Next Work Packages

### L1-F - Synthesis of L1-A through L1-E

Combine L1-A through L1-E into one theorem-candidate statement with all hypotheses and constants. The target is a single conditional statement:

$$
\mathrm{WS}_{\mathrm{full}}
\Rightarrow
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u))
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
$$

### L1-G - Empirical WS / NoExtra / Inact Diagnostic

Implement diagnostic checks for:

- active mass;
- support separation;
- cut height;
- bridge height;
- slot association;
- secondary bar suppression;
- inactive residual height;
- residual background bars.

Do not implement this diagnostic unless explicitly requested.

### L1-H - Local-to-Global Barcode Transfer

Formalize how local active-slot and residual barcode conditions transfer to the global aggregate \(U\). This is the main proof-theoretic upgrade path for L1-D and L1-E.

---

## 14. Summary

Low inactive mass is insufficient. A mass-inactive slot can still create a dominant terminal-death bar if it contains a tall narrow spike.

Inactive suppression must control height and persistence:

$$
\|R_{\mathrm{inact}}\|_\infty<\ell_{\min}
\quad\text{or}\quad
K_{\mathrm{bar}}^{\ell_{\min}}(R_{\mathrm{inact}})=0,
$$

plus aggregate perturbation bounds after adding \(R_{\mathrm{inact}}\) to \(U_{\mathrm{act}}\).

The terminal-death convention makes residual spikes especially important: a residual component of height \(h\) can produce a terminal bar of length \(h\).

L1-E prevents inactive residual overcount only under strong working hypotheses. It does not prove full L-1. The next step is synthesis across L1-A through L1-E, followed by a local-to-global barcode transfer theorem.
