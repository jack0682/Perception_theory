# L1-J: Cat-A Upgrade Attempt for the Hard-Bar / Active-Count Bridge

**File:** `THEORY/working/MF/kbar_kact_bridge_L1J_catA_upgrade_attempt.md`
**Document type:** non-canonical working theorem candidate + Cat-A upgrade audit
**Created:** 2026-05-02 (after L1-A through L1-I, L1-H2)
**Status:** working; **THEOREM_CANDIDATE_STRONG**, not Cat-A; pending external audit and explicit decay-assumption commitment

---

## 1. Status and Scope

This is a non-canonical working note. It attempts the Cat-A upgrade of the L1-F hard-bar / active-count bridge by auditing the proof obligations after L1-H2 closed PO-LH1.

L1-J does **not**:

- prove L-1.
- promote L1-F to Cat-A in this document.
- assign a canonical commitment number.
- solve OP-0005 or OP-0008.
- claim \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) or \(K_{\mathrm{soft}}=K_{\mathrm{act}}\) globally.
- claim \(\sigma_{\mathrm{rich}}\) sufficiency.
- promote reservoir theory to canonical.
- treat empirical feasibility (L1-I) or numerical verification as theorem proof.
- modify any canonical or existing working file.

L1-J produces:

- a precise statement of the L1-F target theorem under a clarified hypothesis package after L1-H2 (with H6 stated on \(G_j^r\), tie convention specified, decay assumption added);
- an honest classification as **THEOREM_CANDIDATE_STRONG** (close to Cat-A, but not Cat-A in this document);
- a discharge of PO-1 (bridge-cut existence) **under an explicit decay assumption \(\psi\)**, classified as a "safe technical condition";
- a proof-grade discharge of PO-2 (labeled slot-to-bar association) under the L1-H2 conditions;
- a definitional resolution of PO-7 (tie convention) via a fixed lexicographic order on \(X\);
- an explicit identification of the remaining blockers: external audit of L1-H2, decision on whether the decay assumption is part of the canonical L1-F package;
- numerical verification (`CODE/scripts/l1j_bridge_cut_decay_diagnostic.py`) that the decay-to-cut bound is non-vacuous on all six tested configurations including the L1-I FEASIBLE_WITH_BUDGET regime and the WQ-1 default σ_b=2.0 configuration.

---

## 2. Task Checklist

- [x] Read L1-H2 (boundary leakage), L1-I (feasibility), L1-H, L1-G, L1-F, L1-A through L1-E.
- [x] Re-inspect L1-G/L1-H/L1-I/L1-H2 scripts and persistence/diagnostics/k_soft/graph code.
- [x] Identify all L1-F hypotheses and their current discharge status after L1-H2.
- [x] Audit each open obligation: PO-1, PO-2, PO-7, L1-H2 audit.
- [x] Attack PO-1 directly: derive low bridge from primitive decay/separation conditions.
- [x] Numerically verify the decay-to-cut bound on the L1-I FEASIBLE_WITH_BUDGET regime AND the WQ-1 default σ_b=2.0 case.
- [x] Discharge PO-2 by defining \(\mathcal A_{\mathrm{bar}}(j)\) = unique dominant bar with birth in \(N_j^r\), and verifying it is well-defined and bijective.
- [x] State the PO-7 deterministic tie convention.
- [x] Build condition-safety audit classifying every condition as DEFINITIONAL / SAFE TECHNICAL / DANGEROUS / FORBIDDEN.
- [x] Build proof-obligation table.
- [x] Build Cat-status table.
- [x] State the upgrade decision honestly.
- [x] Preserve all forbidden non-claims.
- [x] Verify file creation.

---

## 3. Current Proof State After L1-H2

L1-F's original residual proof obligations (L1-F §9):

| Obligation | Original status | Status after L1-H2 |
|---|---|---|
| PO-1 bridge-cut existence | OPEN | OPEN — addressed in L1-J §8 under decay assumption |
| PO-2 slot-to-bar association | LEMMA-CAND | OPEN for labels; count-equality DERIVED |
| PO-3 terminal-death convention | WORKING-DEF | WORKING-DEF / code-aligned (unchanged) |
| PO-4 active secondary-bar suppression | LEMMA-CAND | **CLOSED** by L1-H2 Lemma 2 (under H6 on \(G_j^r\)) |
| PO-5 inactive residual suppression | LEMMA-CAND | **CLOSED** for the count by LG-4 + LG-7 derivation (L1-H §7.B) |
| PO-6 local-to-global barcode transfer (= H10) | OPEN | **CLOSED** by L1-H2 Lemma 1, 2, 3 |
| PO-7 tie / plateau stability | OPEN | OPEN — definitional resolution proposed in L1-J §10 |
| PO-8 constants compatibility | OPEN | **CLOSED** empirically by L1-I (439/1920 FEASIBLE_WITH_BUDGET) |
| PO-9 empirical diagnostic validation | EMP local only | **CLOSED** by L1-G + L1-I + L1-H2 stress tests |

What remains: PO-1, PO-2 (label part), PO-7 (formal convention), and external audit of L1-H2 lemmas.

---

## 4. Target Theorem Statement

**L1-F Hard-Bar / Active-Count Bridge (L1-J Theorem-Candidate-Strong).**

Let \(G=(X,E)\) be a finite graph and \(\mathbf u\in\widetilde\Sigma^{K_{\mathrm{field}}}_M(G)\) a shared-pool multi-formation state. Let

\[
U(\mathbf u)=\sum_{j=1}^{K_{\mathrm{field}}}u^{(j)},
\qquad
A^\varepsilon(\mathbf u)=\{j:m_j(\mathbf u)>\varepsilon\}.
\]

Suppose the **L1-J hypothesis package** holds:

(P0) **Terminal-death \(H_0\) superlevel persistence convention** (PO-3, code-aligned with `scc.diagnostics._persistence_h0_graph`).

(P1) **Deterministic tie convention** (PO-7): a fixed total order \(\prec\) on \(X\); vertices are processed in nonincreasing \(U\) order, breaking ties by \(\prec\); union-find elder rule; surviving component receives death \(0\).

(P2) **Active mass and connected support** (L1-F H1): for each \(j\in A^\varepsilon\), \(m_j(\mathbf u)>\varepsilon\), \(S_j^\delta=\{u^{(j)}>\delta\}\) is non-empty and \(G[S_j^\delta]\) is connected.

(P3) **Disjoint active neighborhoods** (LG-1): \(N_j^r\cap N_k^r=\emptyset\) for \(j\neq k\).

(P4) **Low boundary collar** (LG-2): \(\max_{x\in\partial N_j^r}U(x)\le b_j-\ell_{\min}-r_{\mathrm{assoc}}\) for every \(j\in A^\varepsilon\), where \(b_j=U(p_j)\) is the peak height.

(P5) **Background suppression on U** (LG-4): \(\|U\|_{\infty,X_{\mathrm{bg}}}\le\ell_{\min}-\rho_{\mathrm{bg}}\).

(P6) **Birth height** (L1-F H2): \(b_j\ge h_{\min}\ge\ell_{\min}\) for every \(j\in A^\varepsilon\).

(P7) **Decay-to-cut bound** (PO-1, NEW for L1-J): for each pair \(j\neq k\in A^\varepsilon\), there exists a separating cut \(C_{jk}\) between \(S_j^\delta\) and \(S_k^\delta\) at graph distance at least \(q\) from every active support, and a monotone-decreasing decay profile \(\psi:\mathbb R_{\ge 0}\to[0,1]\) such that

\[
u^{(j)}(x)\le\psi(d_G(x,S_j^\delta))\quad\forall j\in A^\varepsilon,\,x\in X,
\]

and

\[
K_{\mathrm{act}}^\varepsilon\,\psi(q)+\|R_{\mathrm{inact}}\|_{\infty,C_{jk}}
\le
\min(b_j,b_k)-\ell_{\min}-r_{\mathrm{assoc}}.
\]

(P8) **Tightened H6 on \(G_j^r\)** (L1-H2 strengthening of L1-D H6 / L1-F H6): \(\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}\).

(P9) **Local perturbation control** (L1-D NE-2): \(\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2\) where \(R_j=\sum_{k\neq j}u^{(k)}+R_{\mathrm{inact}}\).

(P10) **Inactive residual suppression** (L1-F H7): \(\|R_{\mathrm{inact}}\|_\infty\le\ell_{\min}-\rho_{\mathrm{res}}\).

(P11) **Margin ledger** (L1-F H4): \(h_{\min}-\max_{k\neq j}B_{jk}\ge\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}}\), where \(B_{jk}=K_{\mathrm{act}}\psi(q_{jk})+\|R_{\mathrm{inact}}\|_{\infty,C_{jk}}\) is the cut-height bound from (P7).

Under (P0)–(P11),

\[
\boxed{K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u);G)=K_{\mathrm{act}}^\varepsilon(\mathbf u).}
\]

Moreover, the labeled association map

\[
\mathcal A_{\mathrm{bar}}(j)=\text{(unique dominant bar of }U\text{ on }G\text{ with birth vertex in }N_j^r)
\]

is a well-defined bijection from \(A^\varepsilon(\mathbf u)\) onto the dominant bars of \(\mathrm{Bars}_0^{\mathrm{term}}(U;G)\).

**Status:** **THEOREM_CANDIDATE_STRONG** (close to Cat-A, not Cat-A in this document). Pending: external audit of L1-H2 lemmas; decision on whether (P7)'s decay assumption \(\psi\) is part of the canonical L1-F package or stays as a working-grade hypothesis.

---

## 5. Hypothesis Audit

Each hypothesis classified by role and discharge status:

| Hypothesis | Role | Discharge status | Source / target |
|---|---|---|---|
| (P0) Terminal-death convention | Definitional / code-aligned | DEFINITIONAL | scc.diagnostics |
| (P1) Tie convention \(\prec\) | Definitional | DEFINITIONAL (PO-7) | L1-J §10 |
| (P2) Active mass / connected support | Empirically measurable / definitional | DEFINITIONAL | L1-F H1 |
| (P3) Disjoint neighborhoods (LG-1) | Geometric assumption | EMP-VERIFIABLE; SAFE | L1-H |
| (P4) Low boundary collar (LG-2) | Geometric assumption | EMP-VERIFIABLE; SAFE | L1-H |
| (P5) Background \(U\) bound (LG-4) | Geometric assumption | EMP-VERIFIABLE; SAFE | L1-H |
| (P6) Birth height \(\ge h_{\min}\) | Field-shape | EMP-VERIFIABLE; SAFE | L1-F H2 |
| **(P7) Decay-to-cut bound** | Field-decay / shape (NEW) | DISCHARGED via PO-1 lemma if \(\psi\) given | L1-J §8 |
| (P8) Tightened H6 on \(G_j^r\) | Slot-internal H6 | EMP-VERIFIABLE on slot field; SAFE | L1-H2 |
| (P9) Perturbation control (NE-2) | Slot interaction bound | EMP-VERIFIABLE; SAFE | L1-D |
| (P10) Inactive residual \(\le\ell_{\min}-\rho_{\mathrm{res}}\) | Residual bound | EMP-VERIFIABLE | L1-F H7 |
| (P11) Margin ledger | Constants compatibility | EMP-VERIFIABLE; consistent with L1-I | L1-F H4 |

No hypothesis presupposes the conclusion. (P7) decay-to-cut is the most substantive new hypothesis; it is field-shape, not object-label (see §13).

---

## 6. Discharged Obligations

After L1-H2 + L1-J:

| Obligation | Discharge mechanism | Status |
|---|---|---|
| PO-3 terminal-death convention | code-aligned definition | WORKING-DEF |
| PO-4 active secondary-bar suppression | L1-H2 Lemma 2 (under H6 on \(G_j^r\)) | PROOF-GRADE in L1-H2 doc, audit pending |
| PO-5 inactive residual suppression for the count | LG-4 + LG-7 derivation (L1-H §7.B) | PROOF-GRADE |
| PO-6 local-to-global barcode transfer (H10) | L1-H2 Lemma 1 + Lemma 3 | PROOF-GRADE in L1-H2 doc, audit pending |
| **PO-1 bridge-cut existence** | L1-J §8 lemma under decay assumption \(\psi\) | DISCHARGED **conditional on (P7)**; the PO-1 lemma itself is PROOF-GRADE in L1-J; (P7) is added to hypothesis package |
| **PO-2 count equality** | L1-H2 Lemma 3 + L1-J §9 (each \(N_j^r\) gives exactly one dominant bar) | PROOF-GRADE under L1-J package |
| **PO-2 labeled association** | L1-J §9 (\(\mathcal A_{\mathrm{bar}}(j)\) = unique dominant bar in \(N_j^r\)) | PROOF-GRADE under L1-J package |
| **PO-7 tie convention** | L1-J §10 deterministic order | DEFINITIONAL |
| PO-8 constants compatibility | L1-I empirical 439/1920 FEASIBLE_WITH_BUDGET | EMPIRICAL — non-empty regime exhibited |
| PO-9 empirical diagnostic | L1-G + L1-I + L1-H2 stress tests | EMPIRICAL — completed |

---

## 7. Remaining Obligations

**Genuinely open after L1-J:**

1. **External audit of L1-H2 Lemma 1, Lemma 2, Lemma 3.** L1-H2 stated these as PROOF-GRADE with detailed proof skeletons; an independent reviewer should verify the union-find / bottleneck-path argument in Lemma 1 and the bottleneck-stability application in Lemma 2.
2. **Decision on (P7) decay-to-cut for canonical adoption.** The PO-1 lemma in L1-J §8 is proof-grade given an explicit decay profile \(\psi\). For the L1-I FEASIBLE_WITH_BUDGET regime (raw Gaussian bumps), \(\psi(d)=\exp(-d^2/(2\sigma_b^2))\) is exact. For SCC dynamics on natural states, the decay profile depends on the energy / convergence; deriving \(\psi\) from primitive SCC theorems is a separate open question that L1-J does not close. The L1-J theorem requires (P7) as a hypothesis; if canonicalization wants to remove it, an SCC-derived decay theorem is needed.
3. **Generalization of L1-H2 Lemma 1 to plateau / non-strict ties under PO-7.** Lemma 1 was stated for strict-tie configurations; the PO-7 convention provides a deterministic tiebreak that should let the strict-version proof carry over. This is a routine extension but needs to be written.

**Not blockers:**

- Tie convention is definitional; PO-7 is closed.
- Constants feasibility is empirical and verified by L1-I; no analytic proof required for Cat-A in the conditional sense.

---

## 8. PO-1 Bridge-Cut Existence Analysis

### 8.1 The PO-1 lemma candidate

**PO-1 Lemma — Decay-to-Cut Bridge Bound.** Let \(G=(X,E)\) be a finite graph, \(\mathbf u\in\widetilde\Sigma^{K_{\mathrm{field}}}_M(G)\), \(A=A^\varepsilon(\mathbf u)\), \(K_{\mathrm{act}}=|A|\). Suppose:

(D1) For each \(j\in A\) and \(x\in X\),

\[
u^{(j)}(x)\le\psi(d_G(x,S_j^\delta)),
\]

where \(\psi:\mathbb R_{\ge 0}\to[0,1]\) is a fixed non-increasing decay profile.

(D2) For each pair \(j\neq k\in A\), there exists a separating vertex cut \(C_{jk}\subset X\) between peaks \(p_j\) and \(p_k\) (or between \(S_j^\delta\) and \(S_k^\delta\)) such that every \(x\in C_{jk}\) satisfies \(d_G(x,S_\ell^\delta)\ge q\) for every \(\ell\in A\).

(D3) Inactive residual on the cut: \(\|R_{\mathrm{inact}}\|_{\infty,C_{jk}}\le h_{\mathrm{noise}}\).

Then for every \(x\in C_{jk}\),

\[
U(x)
=
\sum_{\ell\in A}u^{(\ell)}(x)+R_{\mathrm{inact}}(x)
\le
K_{\mathrm{act}}\psi(q)+h_{\mathrm{noise}},
\]

hence the cut-height bound

\[
H_{C_{jk}}(U)=\max_{x\in C_{jk}}U(x)\le K_{\mathrm{act}}\psi(q)+h_{\mathrm{noise}}.
\]

By the L1-B finite-graph cut lemma (Cat-A local fact),

\[
\theta_{\mathrm{bridge}}^{jk}(U)
\le
H_{C_{jk}}(U)
\le
K_{\mathrm{act}}\psi(q)+h_{\mathrm{noise}}.
\]

**Status:** PROOF-GRADE in L1-J under hypotheses (D1)–(D3). The proof is direct: bound each term in the aggregate sum on \(C_{jk}\) using the decay profile and separator distance, then use L1-B. \(\square\)

### 8.1.bis Heterogeneous decay generalization (added by L1-K R-4)

The PO-1 lemma above uses a **uniform** decay profile \(\psi\) for all active slots and a single separator-distance constant \(q\). The general theorem statement allows **heterogeneous** decay profiles \(\{\psi_\ell\}_{\ell\in A}\) and per-slot separator distances:

**PO-1 (heterogeneous form).** Suppose:

(D1\(^*\)) For each \(\ell\in A\) and \(x\in X\),

\[
u^{(\ell)}(x)\le\psi_\ell(d_G(x,S_\ell^\delta)),
\]

where each \(\psi_\ell:\mathbb R_{\ge 0}\to[0,1]\) is non-increasing.

(D2\(^*\)) For each pair \(j\neq k\in A\), there exists a separating vertex cut \(C_{jk}\) between \(p_j\) and \(p_k\), with per-slot minimum-distance constants

\[
q_{\ell,jk}\;:=\;\min_{x\in C_{jk}}d_G(x,S_\ell^\delta)\quad(\ell\in A).
\]

(D3) Inactive residual on the cut: \(\|R_{\mathrm{inact}}\|_{\infty,C_{jk}}\le h_{\mathrm{noise}}\).

Then for every \(x\in C_{jk}\),

\[
U(x)
\le
\sum_{\ell\in A}u^{(\ell)}(x)+R_{\mathrm{inact}}(x)
\le
\sum_{\ell\in A}\psi_\ell(d_G(x,S_\ell^\delta))+h_{\mathrm{noise}}
\le
\sum_{\ell\in A}\psi_\ell(q_{\ell,jk})+h_{\mathrm{noise}},
\]

using monotonicity of each \(\psi_\ell\) and \(d_G(x,S_\ell^\delta)\ge q_{\ell,jk}\) for every \(\ell\in A\) and every \(x\in C_{jk}\). Hence

\[
\boxed{H_{C_{jk}}(U)\le\sum_{\ell\in A}\psi_\ell(q_{\ell,jk})+h_{\mathrm{noise}}.}
\]

By L1-B,

\[
\theta_{\mathrm{bridge}}^{jk}(U)\le H_{C_{jk}}(U)\le\sum_{\ell\in A}\psi_\ell(q_{\ell,jk})+h_{\mathrm{noise}}.
\]

**Classification.**

- The **heterogeneous form** is the **general theorem statement**.
- The **uniform form** (\(\psi_\ell=\psi\) for all \(\ell\in A\), \(q_{\ell,jk}\ge q\) for some single \(q\), giving \(H_{C_{jk}}(U)\le K_{\mathrm{act}}\psi(q)+h_{\mathrm{noise}}\)) is a **convenient corollary** when slot decays are comparable.

The L1-I numerical verification (§8.3) uses uniform Gaussian decay; the heterogeneous form would apply to mixed slot families (e.g., spectral-mode reservoir slots with different \(\sigma_b\)-equivalent shape parameters).

### 8.2 Compatibility with L1-F ledger

To use PO-1 inside the L1-F ledger, we need

\[
B_{jk}=K_{\mathrm{act}}\psi(q_{jk})+h_{\mathrm{noise}}
\]

to satisfy the L1-F H4 / (P11) margin:

\[
h_{\min}-B_{jk}\ge\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}}.
\]

Equivalently:

\[
K_{\mathrm{act}}\psi(q_{jk})+h_{\mathrm{noise}}
\le
h_{\min}-\ell_{\min}-r_{\mathrm{assoc}}-r_{\mathrm{birth}}.
\]

This is a parameter feasibility question testable empirically. L1-J §8.3 verifies it numerically.

### 8.3 Numerical verification

The script `CODE/scripts/l1j_bridge_cut_decay_diagnostic.py` computes, for six configurations on \(T^2_{20}\), the empirical decay profile \(\psi_{\mathrm{emp}}(q)=\max u^{(j)}(x)\) over \(x\) at distance \(\ge q\) from \(S_j^\delta\), then evaluates \(K_{\mathrm{act}}\psi(q)\) and compares to the actual threshold-scan bridge height.

| σ_b | δ | geom | \(K_{\mathrm{act}}\) | \(U_{\max}\) | actual max bridge | required bound \(h_{\min}-\ell_{\min}\) | LG-3 holds | \(K_{\mathrm{act}}\psi(2)\) |
|---|---|---|---:|---:|---:|---:|---|---:|
| 0.5 | 0.02 | A | 3 | 1.000 | 0.000 | 0.900 | yes | 1.4e-4 |
| 0.5 | 0.05 | A | 3 | 1.000 | 0.000 | 0.900 | yes | 1.4e-4 |
| 0.5 | 0.05 | wide | 3 | 1.000 | 0.000 | 0.900 | yes | 1.4e-4 |
| 1.0 | 0.05 | A | 3 | 1.000 | 0.000 | 0.900 | yes | 4.5e-3 |
| 1.5 | 0.05 | A | 3 | 1.000 | 0.008 | 0.900 | yes | 1.2e-2 |
| 2.0 | 0.05 | A | 3 | 1.000 | 0.088 | 0.900 | yes | 5.5e-2 |

The decay-to-cut bound holds with margin in every configuration. Even σ_b=2.0 (which fails LG-1 by direct support overlap and is the WQ-1 default) has actual bridge 0.088 ≪ required 0.900.

So the PO-1 decay-to-cut lemma is **non-vacuous** on the L1-I FEASIBLE_WITH_BUDGET regime AND a degraded variant. Adding (P7) to the L1-F package does not empty the regime.

### 8.4 Status of PO-1

**PO-1 lemma:** PROOF-GRADE under (D1)–(D3) (L1-J §8.1).
**(P7) decay assumption:** added to the L1-F hypothesis package as a "safe technical condition" (see §13).
**Numerical non-vacuity:** verified on six configurations (L1-J §8.3).
**Open:** deriving (D1) (the decay profile) from primitive SCC dynamics for general states. For Gaussian bumps this is exact; for SCC-converged states this requires an additional theorem outside L1-J's scope.

---

## 9. PO-2 Slot-to-Bar Association Analysis

### 9.1 Count equality

Under L1-H2 Lemma 3, the count equality is proof-grade:

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U;G)=|A^\varepsilon(\mathbf u)|.
\]

This is a **count statement**, independent of any particular labeling of bars to slots.

### 9.2 Labeled association (clarified by L1-K R-2)

**Primary birth representative — clarification.** Under perturbation \(U=u^{(j)}+R_j\) on \(N_j^r\), the highest local maximum of \(U\) on \(G_j^r\) need not coincide with \(p_j=\arg\max u^{(j)}\). The labeled association is defined using **\(U\)** (the field on which bars are actually born), not \(u^{(j)}\). Concretely, define the **primary birth representative for slot \(j\)** as

\[
q_j^U
\;:=\;
\operatorname*{argmax}_{x\in N_j^r}^{\prec} U(x),
\]

i.e., the first-in-tiebreak local maximum of \(U|_{N_j^r}\) under the PO-7 total order \(\prec\). This is the vertex which actually gives rise to a \(U\)-bar on \(G_j^r\); it may differ from \(p_j=\arg\max u^{(j)}\) under aggregate perturbation but coincides with \(p_j\) in the unperturbed limit (\(R_j\to 0\)).

**Definition.** Under the L1-J package, define

\[
\mathcal A_{\mathrm{bar}}:A^\varepsilon(\mathbf u)\to\mathrm{Bars}_0^{\mathrm{term}}(U;G),
\qquad
\mathcal A_{\mathrm{bar}}(j)
:=
\text{the unique dominant bar born at }q_j^U,
\]

or, equivalently, **the unique dominant bar whose birth vertex lies in \(N_j^r\)** (the two formulations agree by Lemma 2).

**Important distinction.**

- For **count equality** \(K_{\mathrm{bar}}^{\ell_{\min}}(U;G)=K_{\mathrm{act}}^\varepsilon(\mathbf u)\), the exact identity of the primary birth representative does not matter; only the *count* of dominant bars per neighborhood matters.
- For **labeled association** \(\mathcal A_{\mathrm{bar}}\), the representative must be defined using \(U\) (because bars are born in the aggregate field \(U\), not in the individual field \(u^{(j)}\)).

**Lemma (Labeled Association).** Under (P0)–(P11), \(\mathcal A_{\mathrm{bar}}\) is a well-defined bijection onto the dominant bars of \(\mathrm{Bars}_0^{\mathrm{term}}(U;G)\).

**Proof.**

*Well-definedness.* By L1-H2 Lemma 3 step (β) and the contradiction-repaired Lemma 2 (L1-H2 §8.1), \(\mathrm{Dgm}_0^{\mathrm{term}}(U|_{N_j^r};G_j^r)\) has at most one bar of length \(\ge\ell_{\min}\), namely the bar born at \(q_j^U\). Combined with Lemma 1 (\(\ell_{\mathrm{glob}}\le\ell_{\mathrm{loc}}\)), at most one global bar with birth in \(N_j^r\) can be dominant — and the lower-bound argument (using LG-2 collar and \(h_{\min}\ge\ell_{\min}\)) shows there is at least one. Hence "the unique dominant bar with birth in \(N_j^r\)" is well-defined and equals the global bar born at \(q_j^U\).

*Injectivity.* Distinct \(j\neq k\) have disjoint neighborhoods (LG-1, P3), so a bar's birth vertex lies in at most one \(N_j^r\). \(\mathcal A_{\mathrm{bar}}(j)\neq\mathcal A_{\mathrm{bar}}(k)\) for \(j\neq k\).

*Surjectivity onto dominant bars.* By L1-H2 Lemma 3 step (α) (LG-7 derivation from LG-4 + terminal-death), every dominant global bar has its birth vertex in some \(N_j^r\). So every dominant bar is in \(\mathrm{Image}(\mathcal A_{\mathrm{bar}})\).

*Image = dominant bars.* By the L1-H2 lower bound, each \(j\in A\) maps to a dominant bar (length \(\ge\ell_{\min}\)). Combined with the injectivity and the count equality \(|\mathrm{Image}|=|A|=K_{\mathrm{bar}}^{\ell_{\min}}\), the image is exactly the set of dominant bars. \(\square\)

**Status:** PROOF-GRADE under the L1-J package.

### 9.3 Distinguishing count from label

L1-J cleanly separates:

- **Count equality:** \(K_{\mathrm{bar}}^{\ell_{\min}}(U;G)=K_{\mathrm{act}}^\varepsilon(\mathbf u)\). PROOF-GRADE under L1-J package.
- **Labeled equality:** \(\mathcal A_{\mathrm{bar}}\) bijection. PROOF-GRADE under L1-J package.

Both are conditional on (P0)–(P11). Neither is a global statement.

---

## 10. PO-7 Tie Convention Analysis

### 10.1 The convention

**PO-7 Convention — Deterministic Tie-Break for Terminal-Death \(H_0\) Superlevel Persistence.**

Fix a total order \(\prec\) on the vertex set \(X\). Concretely, on \(T^2_{20}\) the convention is: \(\prec\) is the row-major lexicographic order on \((r,c)\in\{0,\dots,19\}^2\).

The terminal-death \(H_0\) superlevel persistence is computed by:

1. Sort \(X\) by descending \(U\). Break ties by ascending \(\prec\) (i.e., earlier-\(\prec\) vertex comes first).
2. Process vertices in that order. When \(v\) is processed:
   - If \(v\) has no already-active neighbor: \(v\) starts a new component with `birth_val[v] = U(v)`.
   - If \(v\) has active neighbors in distinct components: the components merge. Under the elder rule, the **older** component (the one whose birth vertex appeared earlier in the ordered processing list) survives; the younger dies with death threshold \(=U(v)\).
   - If \(v\) has active neighbors all in the same component: \(v\) joins that component.
3. The surviving component at the end of processing receives terminal death \(0\). Its bar is recorded as `(max U over the component, 0)`.

### 10.2 Code alignment

This convention matches `scc.diagnostics._persistence_h0_graph` and `scc.persistence.persistence_h0` exactly:

```python
order = np.argsort(-u, kind="stable")  # descending U; stable tiebreak by index
```

`np.argsort` with `kind="stable"` is row-major lexicographic on the flattened array, which under the row-major flattening of a 2D grid is exactly the lexicographic order on \((r,c)\).

The terminal-death `(max(u), 0.0)` is appended explicitly.

### 10.3 Status

**Definitional.** PO-7 is closed.

The convention does not change any prior theorem statement; it only makes the bar assignment deterministic. Lemma 1 of L1-H2 (which assumed strict local maxima) extends to the non-strict case under this convention: tied vertices admit in lexicographic order, the first one becomes a birth vertex, the others join its component.

---

## 11. Cat-A Upgrade Decision

**Decision: THEOREM_CANDIDATE_STRONG, not CAT_A_READY.**

Rationale:

- **Closed obligations:** PO-3, PO-4, PO-5, PO-6, PO-7, PO-8 (empirical), PO-9 (empirical). PO-1 closed conditional on (P7). PO-2 closed (both count and label).
- **Remaining obligations:** External audit of L1-H2 Lemma 1, 2, 3. Decision on whether (P7) decay assumption belongs in the canonical L1-F package or stays as a working-grade hypothesis. Generalization of L1-H2 Lemma 1 to the non-strict-tie case under PO-7 (routine).
- **Decay assumption (P7) audit:** classified as "safe technical condition" in §13. It is field-shape (decay-with-distance), not object-identification. For the L1-I FEASIBLE regime it is exact (Gaussian). For SCC-derived states a separate theorem is needed; this is outside L1-J's scope.

A rigorous Cat-A upgrade would require:

1. External audit of L1-H2 Lemma 1, 2, 3 with sign-off.
2. Either (a) accept (P7) as part of the canonical L1-F package, or (b) prove (P7) from primitive SCC dynamics.
3. Write up the non-strict-tie generalization of L1-H2 Lemma 1.

Until those three are done, L1-J's theorem candidate is **strong but not Cat-A**. It is **stronger than L1-F's original LEMMA-CAND** because PO-1, PO-2, PO-7 are all addressed; the residual uncertainty is concentrated on audit and on the canonical adoption of (P7).

---

## 12. Proof Skeleton

Combining L1-H2 + L1-J:

**Step 1 — Lower bound \(K_{\mathrm{bar}}\ge|A|\):**

By (P3), (P4), (P6), (P11), terminal-death (P0):

For each \(j\in A\), \(p_j\)'s component grows inside \(N_j^r\) (by LG-2, P4, no boundary admission until \(\theta\le B_{\partial,j}\le b_j-\ell_{\min}-r_{\mathrm{assoc}}\)). Hence \(p_j\)'s bar has length \(\ge\ell_{\min}+r_{\mathrm{assoc}}\). Either \(p_j\) survives to terminal (length \(=b_j\ge\ell_{\min}\)) or dies at the inter-neighborhood bridge \(\theta_{\mathrm{bridge}}^{jk}\le B_{jk}\) (P11), giving length \(\ge\ell_{\min}+r_{\mathrm{assoc}}\). All \(|A|\) primary bars are dominant.

**Step 2 — Upper bound \(K_{\mathrm{bar}}\le|A|\):**

*Step 2(a) coverage.* By (P5) LG-4 + terminal-death (P0): every dominant global bar has birth height \(\ge\ell_{\min}\), hence birth vertex with \(U\ge\ell_{\min}>\|U\|_{\infty,X_{\mathrm{bg}}}\). So birth vertex \(\notin X_{\mathrm{bg}}\). Combined with the disjoint partition \(X=X_{\mathrm{bg}}\sqcup\bigsqcup_jN_j^r\) (P3 LG-1), birth vertex is in exactly one \(N_j^r\). [LG-7 derivation, L1-H §7.B, PROOF-GRADE.]

*Step 2(b) per-neighborhood single dominant bar.* By L1-H2 Lemma 1 (Component-Inclusion), for any global birth vertex \(v\in N_j^r\) (\(v\) is also a local max in \(G_j^r\)),

\[
\ell_{\mathrm{glob}}(v;\,U,G)\le\ell_{\mathrm{loc}}(v;\,U|_{N_j^r},G_j^r).
\]

By bottleneck stability (CSEH 2007) and (P9) NE-2,

\[
\ell_{\mathrm{loc}}(v;\,U|_{N_j^r},G_j^r)
\le
\ell_{j,2}(u^{(j)};G_j^r)+\rho_{\mathrm{pert}}.
\]

By (P8) tightened H6,

\[
\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}.
\]

Combining, for any secondary global bar \(v\neq p_j\),

\[
\ell_{\mathrm{glob}}(v;\,U,G)\le(\ell_{\min}-3\rho_{\mathrm{pert}})+\rho_{\mathrm{pert}}=\ell_{\min}-2\rho_{\mathrm{pert}}<\ell_{\min}.
\]

Hence at most the primary \(p_j\) gives a dominant global bar in \(N_j^r\). [L1-H2 Lemma 2, PROOF-GRADE.]

*Step 2(c) combine.* Steps 2(a) and 2(b): every dominant global bar is in some \(N_j^r\) (2a), and each \(N_j^r\) contributes at most one dominant global bar (2b). So \(K_{\mathrm{bar}}^{\ell_{\min}}(U;G)\le|A|\).

**Step 3 — Equality:** Steps 1 and 2 give \(K_{\mathrm{bar}}^{\ell_{\min}}(U;G)=|A|=K_{\mathrm{act}}^\varepsilon(\mathbf u)\).

**Step 4 — Labeled bijection:** \(\mathcal A_{\mathrm{bar}}(j)=\) unique dominant bar with birth in \(N_j^r\) is well-defined (by Step 2b), injective (by P3 LG-1), and surjective onto dominant bars (by Step 2a + Step 1). [L1-J §9.2.]

**Step 5 — PO-1 ledger compatibility:** (P11) \(B_{jk}=K_{\mathrm{act}}\psi(q_{jk})+h_{\mathrm{noise}}\) is the cut-height bound from PO-1. (P11) requires \(h_{\min}-B_{jk}\ge\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}}\). L1-I empirically and L1-J §8.3 numerically verify this is satisfiable. \(\square\)

---

## 13. Condition Safety Audit

| Condition | Role | Safe / Dangerous | Reason |
|---|---|---|---|
| (P0) Terminal-death convention | Definitional | DEFINITIONAL | code-aligned; not an empirical claim |
| (P1) Tie convention \(\prec\) | Definitional | DEFINITIONAL | fixed total order on \(X\); no smuggling |
| (P2) Active mass + connected support | Empirical / definitional | SAFE | measured per-state; no conclusion smuggling |
| (P3) Disjoint neighborhoods (LG-1) | Geometric | SAFE | structural separation; verifiable |
| (P4) Low boundary collar (LG-2) | Geometric | SAFE | shape / decay-near-boundary; verifiable |
| (P5) Background \(U\) bound (LG-4) | Geometric | SAFE | aggregate-field decay on background; verifiable |
| (P6) Birth height \(\ge h_{\min}\) | Field-shape | SAFE | peak height bound; verifiable |
| (P7) Decay-to-cut (NEW) | Field-shape (decay profile + separator distance) | **SAFE TECHNICAL** | shape condition on \(u^{(j)}\); not object-identity; reduces to geometric / graph separator + decay-at-distance; non-vacuous on L1-I FEASIBLE |
| (P8) Tightened H6 on \(G_j^r\) | Slot-internal H6 | SAFE | local barcode condition on slot field |
| (P9) Perturbation control (NE-2) | Slot interaction | SAFE | aggregate residual bound on \(N_j^r\) |
| (P10) Inactive residual \(\le\ell_{\min}-\rho_{\mathrm{res}}\) | Residual bound | SAFE | aggregate inactive-slot bound |
| (P11) Margin ledger | Constants compatibility | SAFE | empirically verifiable; consistent with L1-I |
| Global \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) as hypothesis | (NOT used in L1-J) | **FORBIDDEN** | smuggles the conclusion |
| Pre-given external object labels | (NOT used in L1-J) | **FORBIDDEN** | theory-destroying; violates CN10 / CN11 |
| H6 stated on \(G\) only (L1-H §7.A original) | (replaced in L1-H2 / L1-J) | DANGEROUS | not always equivalent to H6 on \(G_j^r\); can fail to give upper-bound proof for general slot fields |
| LG-7 as axiom (NOT used) | (NOT used in L1-J) | DANGEROUS | conclusion-like; actually derived from LG-4 + terminal-death |

**Summary.** L1-J adds (P7) decay-to-cut as the most substantive new condition. It is classified SAFE TECHNICAL because:

1. It is a SHAPE condition on \(u^{(j)}\) (decay-with-distance), not an object-identity condition.
2. It does not presuppose \(K_{\mathrm{bar}}=K_{\mathrm{act}}\); it bounds aggregate \(U\) on a graph separator.
3. It is non-vacuous on the L1-I FEASIBLE regime (verified numerically).
4. It is a refinement of "well-separated bumps", not a stipulation that the field IS Gaussian.

For SCC-derived states under natural dynamics, deriving (P7) requires an SCC-decay theorem; L1-J does not provide that, but identifies it as the next substantive proof obligation outside the L1-J package.

---

## 14. Counterexample / Failure Modes

### Failure modes within the L1-J package

**L1J-F1 — (P7) violated by slow decay.** If \(\psi\) decays too slowly (e.g., \(\sigma_b\) too large on \(T^2_{20}\)), the cut-height bound \(K_{\mathrm{act}}\psi(q)+h_{\mathrm{noise}}\) exceeds \(h_{\min}-\ell_{\min}\). The L1-J theorem's antecedent (P11) fails. K_bar = K_act may still hold or fail depending on actual bridge structure; no contradiction with the theorem.

**L1J-F2 — (P3) LG-1 violated.** Active neighborhoods overlap. The L1-H2 perturbation argument (Lemma 2 step 2) breaks because \(\|R_j\|_{\infty,N_j^r}\) is no longer small. Not a counterexample to L1-J; it violates the antecedent.

**L1J-F3 — (P5) LG-4 violated.** Background dominant bars exist. Step 2(a) of the upper-bound proof breaks. K_bar > K_act becomes possible. Not a counterexample to L1-J.

**L1J-F4 — Tied peaks.** Under PO-7 the tie is broken deterministically; if the tie order is acceptable to the theorem statement, no problem. The strict-tie hypothesis of L1-H2 Lemma 1 needs the routine extension noted in §7.

### No counterexamples to L1-J's conditional theorem

The five L1-H2 stress tests (CE-1, CE-2, CE-3, CE-4, ST-1..ST-5 of L1-H2 script) all violate at least one L1-J hypothesis (typically LG-4 or LG-1). Within those configurations, K_bar ≠ K_act is observed, but L1-J's antecedent fails, so no contradiction.

For configurations satisfying the full L1-J package (e.g., the L1-I FEASIBLE_WITH_BUDGET regime), K_bar = K_act can be verified numerically; the L1-J theorem candidate is consistent with all empirical evidence.

---

## 15. Relationship to OP-0005 / OP-0008

**OP-0005 (K-Selection).** L1-J does not address K-selection. It establishes the bridge \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) under explicit conditions; it does not explain *which* \(K\) emerges. The reservoir-effective rank reformulation of OP-0005 remains a working subprogram.

**OP-0008 (\(\sigma\)-inheritance).** L1-J does not address \(\sigma\)-inheritance. It establishes that under the L1-J conditions, bar-death events correspond exactly to active-slot merger events; this clarifies what kind of "K-jump" is detectable at the field level, but does not establish \(\sigma_{\mathrm{rich}}\) sufficiency or deterministic \(\Phi_{\mathrm{rich}}\).

No \(\sigma_{\mathrm{rich}}\) sufficiency claim is licensed by L1-J.

---

## 16. Next Work Packages

### L1-K — External audit of L1-H2 + L1-J (recommended next)

A blocking item for Cat-A. Specifically:

1. Audit Lemma 1 (Component-Inclusion / Boundary-Leakage Bound) of L1-H2 §7.1.
2. Audit Lemma 2 (Secondary-Bar Non-Promotion) of L1-H2 §8.1.
3. Audit Lemma 3 (Local-to-Global Upper Bound) of L1-H2 §9.1.
4. Audit PO-1 lemma (Decay-to-Cut Bridge Bound) of L1-J §8.1.
5. Audit Labeled Association lemma of L1-J §9.2.

Independent reviewer should verify: (i) the union-find / bottleneck-path argument; (ii) the bottleneck-stability application; (iii) the LG-7 derivation from LG-4 + terminal-death; (iv) the decay-bound term-by-term argument.

### L1-L — SCC-Decay Theorem Attempt

If (P7) is to become canonical, it must be derivable from primitive SCC dynamics. The target:

> **L1-L Theorem Candidate.** For SCC-stationary states under appropriate energy / regularity conditions, the slot field \(u^{(j)}\) admits a decay profile \(\psi(d)\) bounded by a quantity computable from the SCC parameters (energy, \(\sigma_b\)-equivalent shape parameter, dynamics).

This is outside L1-J's scope. It is the natural "SCC-Bumpy-Profile" theorem that L1-A/L1-B sketched.

### L1-H2-EXT — Plateau / non-strict tie extension of Lemma 1

Under PO-7 deterministic tiebreak, the strict-decreasing filtration order is well-defined. Extending L1-H2 Lemma 1 to plateau cases is a routine rewriting; the proof should follow verbatim with "strict local maximum" replaced by "first-in-tiebreak local maximum".

### L1-M — Soft-count corollary using L1-J

If L1-J's theorem becomes Cat-A after L1-K + L1-L, the smooth bridge

\[
K_{\mathrm{soft}}^\phi(U)=K_{\mathrm{act}}^\varepsilon(\mathbf u)+O(\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}+\rho_\phi)
\]

for \(\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)\) (per WQ-LAT-1.B) becomes a Cat-A corollary. The error terms can be bounded using L1-H2 + L1-J secondary-bar suppression.

### L1-N — Dynamics-compatible regime study

L1-G + L1-I established that WQ-1 dynamics is incompatible with the L1-J regime. A dynamics-compatible study would (i) construct an SCC initial state in the L1-J regime, (ii) integrate forward, (iii) measure how long the regime is preserved. This bridges static feasibility (L1-I) to dynamic applicability.

---

## 17. Summary

- **Upgrade decision: THEOREM_CANDIDATE_STRONG, not CAT_A_READY.** Honest classification: most obligations closed, two genuine blockers remain (external audit of L1-H2 and decision on canonical adoption of (P7) decay assumption).
- **PO-1 (bridge-cut existence) is discharged conditional on (P7) decay-to-cut.** The PO-1 lemma is PROOF-GRADE in L1-J §8.1: \(H_{C_{jk}}(U)\le K_{\mathrm{act}}\psi(q)+h_{\mathrm{noise}}\). The decay assumption (P7) is added to the L1-J hypothesis package; it is a SAFE TECHNICAL condition (field-shape, not object-identity).
- **PO-2 (slot-to-bar association) is fully discharged.** Count equality and labeled bijection are both PROOF-GRADE under the L1-J package. The labeled map is \(\mathcal A_{\mathrm{bar}}(j)=\) unique dominant bar with birth in \(N_j^r\); well-defined, injective, surjective onto dominant bars.
- **PO-7 (tie convention) is closed by definition.** Fix lexicographic order \(\prec\) on \(X\); break ties in descending-\(U\) processing by ascending \(\prec\). Code-aligned with `np.argsort(-u, kind="stable")`.
- **Numerical verification.** The L1-J PO-1 decay-to-cut bound is non-vacuous on six configurations including L1-I FEASIBLE_WITH_BUDGET (σ_b=0.5, narrow bumps) AND the WQ-1 default (σ_b=2.0). For all six, actual bridge ≪ required bound \(h_{\min}-\ell_{\min}=0.9\).
- **No counterexamples.** All previous L1-H2 stress tests and L1-G/L1-I empirical observations either satisfy the L1-J package (no contradiction) or violate at least one antecedent (no contradiction with the conditional theorem).
- **Remaining blockers.** External audit of L1-H2 Lemma 1, 2, 3 + L1-J §8.1 PO-1 lemma + L1-J §9.2 Labeled Association lemma. Decision on whether (P7) is canonical or stays working-grade. Routine extension of L1-H2 Lemma 1 to plateau case under PO-7.
- **Non-claims.** L-1 is not proved. L1-F is not Cat-A in this document. OP-0005 / OP-0008 are not solved. Reservoir theory is not promoted to canonical. Empirical / numerical verification is not theorem proof.

The L1-J upgrade is honest at THEOREM_CANDIDATE_STRONG; the path to Cat-A is now narrow and concrete (audit + decay-canonical decision + plateau extension).
