# L1-K: External Audit of L1-H2 / L1-J Hard-Bar Bridge Lemmas

**File:** `THEORY/working/MF/kbar_kact_bridge_L1K_external_audit.md`
**Document type:** non-canonical adversarial audit
**Created:** 2026-05-02 (after L1-A through L1-J)
**Status:** working audit; advisory only; no canonical commitment; no Cat-A promotion

---

## 1. Status and Scope

This is a non-canonical adversarial audit of the proof structure developed in `kbar_kact_bridge_L1H2_boundary_leakage.md` and `kbar_kact_bridge_L1J_catA_upgrade_attempt.md`. The audit's primary role is **verification**, not creative extension.

The audit:

- treats the L1-H2 / L1-J theorem candidate as a target to break;
- attempts counterexamples on the lemma claims;
- checks inequality directions, persistence conventions, tie handling, circularity, and hidden assumptions;
- proposes minimal repairs only when needed.

L1-K does **not**:

- prove L-1 unless the audit genuinely supports it.
- promote L1-F to Cat-A unless the audit genuinely supports it.
- assign a canonical commitment number.
- modify L1-H2 or L1-J or any canonical file.
- claim OP-0005 / OP-0008 solved.
- claim K_bar = K_act / K_soft = K_act globally.
- claim σ_rich sufficiency.
- promote reservoir theory.
- treat empirical feasibility as theorem proof.

---

## 2. Task Checklist

- [x] Read L1-H2 (boundary-leakage), L1-J (Cat-A attempt), L1-I (feasibility), L1-H, L1-G, L1-F, L1-A through L1-E, surrounding bridge-lemma material.
- [x] Re-inspect L1-H2 / L1-J / L1-I scripts and persistence/diagnostics/k_soft/graph code.
- [x] Audit persistence convention (terminal-death, tie-break, code alignment).
- [x] Audit L1-H2 Lemma 1 (Component-Inclusion / Boundary-Leakage Bound).
- [x] Audit L1-H2 Lemma 2 (Secondary-Bar Non-Promotion). **Found a proof-hygiene issue and a rigorous repair.**
- [x] Audit L1-H2 Lemma 3 (Local-to-Global Upper Bound).
- [x] Audit L1-J PO-1 (Decay-to-Cut Bridge Bound).
- [x] Audit L1-J PO-2 (Labeled Slot-to-Bar Association).
- [x] Audit L1-J PO-7 (Tie Convention).
- [x] Check circularity and pre-given object labels.
- [x] Search for counterexamples within the L1-J package and confirm none exists.
- [x] State audit verdict honestly: **THEOREM_CANDIDATE_STRONG_AUDIT_PASSED**.
- [x] Specify required repairs (proof-hygiene only, not substantive).
- [x] Verify file creation.

---

## 3. Audited Claim

**L1-F Hard-Bar / Active-Count Bridge under the L1-J package (P0)–(P11):**

\[
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u);G)=K_{\mathrm{act}}^\varepsilon(\mathbf u),
\]

with labeled bijection

\[
\mathcal A_{\mathrm{bar}}(j)=\text{the unique dominant bar with birth in }N_j^r.
\]

The audit checks every load-bearing inequality, every assumption-discharge step, and circularity hazards.

---

## 4. Persistence Convention Audit

### Conventions used

1. **Superlevel \(H_0\) filtration** with terminal-death convention: surviving component receives death \(0\).
2. **Tie-breaking convention** (PO-7): fixed total order \(\prec\) on \(X\); sort by descending \(U\), break ties by ascending \(\prec\); union-find elder rule.
3. **Code alignment**: `scc.diagnostics._persistence_h0_graph` uses `np.argsort(-u, kind="stable")` which is a row-major lexicographic stable order, exactly matching PO-7.

### Plateau handling

L1-H2 Lemma 1 uses "strict local maxima" hypotheses. Under PO-7, ties are broken deterministically; the strict-version reduces to the tie-broken version verbatim. **Recommended clarification (not a flaw):** L1-H2 should add a one-paragraph note that under PO-7, "strict local maxima" is replaced by "first-in-tiebreak local maxima" and the proof carries over.

### Verdict

**OK_WITH_CLARIFICATION.** Conventions are consistent and code-aligned. The plateau extension under PO-7 should be explicitly documented in a follow-up note (L1-H2-EXT, already listed as a follow-up task in L1-H2 §16).

---

## 5. L1-H2 Lemma 1 Audit — Component-Inclusion / Boundary-Leakage Bound

### Claim

For \(G[N]\subseteq G\), if \(v\in N\) is a strict local maximum of \(U\) in \(G\) (auto: also a strict local maximum of \(U|_N\) in \(G[N]\)), then

\[
\ell_{\mathrm{glob}}(v;\,U,G)\le\ell_{\mathrm{loc}}(v;\,U|_N,G[N]).
\]

### Audit

**Bottleneck-path formulation (proof step in L1-H2 §7.1):**

Let \(W_v=\{w:U(w)>U(v)\}\). Define

\[
\beta_{\mathrm{loc}}(v)=\max_{w\in W_v\cap N}\mathrm{bottleneck}_{G[N]}(v,w),
\quad
\beta_{\mathrm{glob}}(v)=\max_{w\in W_v}\mathrm{bottleneck}_G(v,w).
\]

By bottleneck-path = "highest \(\theta\) at which \(v\) and \(w\) are in the same component of \(G\cap\{U\ge\theta\}\)", we have \(d_{\mathrm{loc}}=\beta_{\mathrm{loc}}\) and \(d_{\mathrm{glob}}=\beta_{\mathrm{glob}}\) (under terminal-death convention; \(d=0\) if the set is empty).

**Inclusion check:**
- Every path in \(G[N]\) is a path in \(G\) (vertices in \(N\subseteq X\); edges of \(G[N]\) are edges of \(G\)). Hence \(\mathrm{bottleneck}_G(v,w)\ge\mathrm{bottleneck}_{G[N]}(v,w)\) for any \(w\in N\).
- \(W_v\cap N\subseteq W_v\). Taking max over a larger set:
  \[
  \beta_{\mathrm{glob}}(v)\ge\max_{w\in W_v\cap N}\mathrm{bottleneck}_G(v,w)\ge\max_{w\in W_v\cap N}\mathrm{bottleneck}_{G[N]}(v,w)=\beta_{\mathrm{loc}}(v).
  \]
- Hence \(d_{\mathrm{glob}}\ge d_{\mathrm{loc}}\), so \(\ell_{\mathrm{glob}}=U(v)-d_{\mathrm{glob}}\le U(v)-d_{\mathrm{loc}}=\ell_{\mathrm{loc}}\).

**Edge case: \(W_v\cap N=\emptyset\) (v is highest in N).** Locally, \(d_{\mathrm{loc}}=0\) (terminal). Globally, either \(W_v=\emptyset\) (v is highest in X too, \(d_{\mathrm{glob}}=0\), bars equal) or \(W_v\neq\emptyset\) (v is not highest in X; \(d_{\mathrm{glob}}\) finite, \(\ell_{\mathrm{glob}}<U(v)=\ell_{\mathrm{loc}}\)).

**Edge case: v is local-max in G[N] but NOT in G.** Then \(v\) has a neighbor in \(X\setminus N\) with \(U>U(v)\), so globally \(v\) is NOT a birth vertex. The lemma's hypothesis "v is strict local max in G" excludes this case, so it is correctly handled.

### Counterexample search

Tested 5 stress configurations in `CODE/scripts/results/l1h2_boundary_leakage.json`:

| Stress test | Result |
|---|---|
| ST-1 internal-only mergers | inequality holds (equality) |
| ST-2 low boundary, slow external | inequality holds (equality) |
| ST-3 external-faster-than-internal | inequality holds (equality) — **the case L1-H §8 mistakenly thought could lengthen bars** |
| ST-4 LG-2 violated (high collar) | inequality holds (equality) |
| ST-5 equal-height ties | inequality holds (equality) |

No counterexample. The proof is rigorous.

### Verdict

**VERIFIED.** No issue. The L1-H2 §7.1 proof is correct as stated.

---

## 6. L1-H2 Lemma 2 Audit — Secondary-Bar Non-Promotion

### Claim

Under tightened H6 (\(\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}\)) and L1-D NE-2 (\(\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2\)), any global secondary bar with birth in \(N_j^r\) has length \(<\ell_{\min}\).

### Audit — proof-hygiene issue identified

The L1-H2 §8.1 proof step 2 says:

> "For matched bars in the optimal bottleneck matching, \(|\ell_i(U)-\ell_i(u^{(j)})|\le 2W_\infty\le\rho_{\mathrm{pert}}\). For unmatched bars, length \(\le 2W_\infty\le\rho_{\mathrm{pert}}\). Hence the secondary bar of \(U|_{N_j^r}\) has length \(\ell_{\mathrm{loc}}^U(v)\le\ell_{j,2}(u^{(j)};G_j^r)+\rho_{\mathrm{pert}}\)."

**Issue:** Bottleneck stability \(d_B(\mathrm{Dgm}(U|_{G_j^r}),\mathrm{Dgm}(u^{(j)}|_{G_j^r}))\le\rho_{\mathrm{pert}}/2\) gives a bijection \(\pi\) with max L\(_\infty\) distance \(\le\rho_{\mathrm{pert}}/2\). This implies for matched pairs \(|\ell-\ell'|\le\rho_{\mathrm{pert}}\) and for unmatched (matched to diagonal) \(\ell\le\rho_{\mathrm{pert}}\). However, the optimal \(\pi\) does **not** necessarily map "second-largest of U" to "second-largest of u^{(j)}". The U-secondary could match to u^{(j)}-primary, giving \(\ell_{\mathrm{loc}}^U\le\ell_{\mathrm{primary}}(u^{(j)})+\rho_{\mathrm{pert}}\approx 1+\rho_{\mathrm{pert}}\), which is useless for bounding by \(\ell_{\min}\).

**Repair: contradiction-based argument.**

**Lemma 2 (corrected proof).** Suppose for contradiction \(\ell_{j,2}(U;G_j^r)\ge\ell_{\min}\). Then \(U|_{G_j^r}\) has at least two bars of length \(\ge\ell_{\min}\). For each such \(U\)-bar \((b_U,d_U)\), the optimal \(\pi\) maps it to either:

- **Diagonal:** then \(\ell_U\le 2\cdot(\rho_{\mathrm{pert}}/2)=\rho_{\mathrm{pert}}<\ell_{\min}\) (assuming \(\rho_{\mathrm{pert}}<\ell_{\min}\)). Contradicts \(\ell_U\ge\ell_{\min}\).
- **A bar of \(u^{(j)}\)** with \(|\ell_U-\ell'|\le\rho_{\mathrm{pert}}\). Hence \(\ell'\ge\ell_{\min}-\rho_{\mathrm{pert}}\).

So each \(U\)-bar of length \(\ge\ell_{\min}\) must match to a \(u^{(j)}\)-bar of length \(\ge\ell_{\min}-\rho_{\mathrm{pert}}\). The \(u^{(j)}\)-secondary has length \(\le\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}<\ell_{\min}-\rho_{\mathrm{pert}}\), so it can't be the match. Hence each must match to the \(u^{(j)}\)-primary (or another non-secondary bar of length \(\ge\ell_{\min}-\rho_{\mathrm{pert}}\)).

But \(u^{(j)}\) on \(G_j^r\) has only ONE bar of length \(\ge\ell_{\min}-\rho_{\mathrm{pert}}\) — namely the primary (under tightened H6, secondary \(\le\ell_{\min}-3\rho_{\mathrm{pert}}\), so any non-primary bar is \(<\ell_{\min}-\rho_{\mathrm{pert}}\)).

Two \(U\)-bars of length \(\ge\ell_{\min}\) can't both match to a single \(u^{(j)}\)-primary bar (\(\pi\) is a bijection). Contradiction. \(\square\)

By Lemma 1: \(\ell_{j,2}(U;G)\le\ell_{j,2}(U;G_j^r)<\ell_{\min}\). Conclusion holds.

### Counterexample search

Direct numerical test on L1-I FEASIBLE configurations (raw Gaussian bumps): \(\ell_{j,2}(u^{(j)};G_j^r)=0\) (single peak), \(\ell_{j,2}(U;G)\) consistently small. No counterexample observed.

### Verdict

**VERIFIED_WITH_CONSTANT_CORRECTION.** Conclusion is correct; the L1-H2 §8.1 proof step 2 needs to be replaced by the contradiction-based argument above. Required repair: rewrite step 2 in L1-H2 §8.1 (proof-hygiene; not a substantive flaw).

---

## 7. L1-H2 Lemma 3 Audit — Local-to-Global Upper Bound

### Claim

Under the L1-H2 package, \(K_{\mathrm{bar}}^{\ell_{\min}}(U;G)\le|A^\varepsilon(\mathbf u)|\).

### Audit

**Step (α) coverage from LG-7 derivation.** A dominant bar has length \(\ge\ell_{\min}\), so under terminal-death (death \(\ge 0\)) the birth height \(\ge\ell_{\min}\). The birth vertex \(v\) has \(U(v)\ge\ell_{\min}\). LG-4 gives \(\|U\|_{\infty,X_{\mathrm{bg}}}\le\ell_{\min}-\rho_{\mathrm{bg}}<\ell_{\min}\). Hence \(v\notin X_{\mathrm{bg}}\). Combined with LG-1 disjoint partition, \(v\in N_j^r\) for exactly one \(j\). **Verified.**

**Step (β) per-neighborhood at most one dominant bar.** Direct from Lemma 2 applied to each \(N_j^r\) plus the lower-bound proof showing the primary contributes one dominant bar. **Verified subject to the Lemma 2 repair.**

### Clarification needed

The L1-J §9.2 Labeled Association proof says "the primary peak \(p_j\) is one such birth vertex." This is imprecise: under the perturbation \(R_j=\sum_{k\neq j}u^{(k)}+R_{\mathrm{inact}}\), the highest local maximum of \(U|_{N_j^r}\) may be a vertex \(q_j\) different from \(p_j=\arg\max u^{(j)}\). The lower-bound argument for the primary global bar should be stated on \(U\) directly using LG-2 (boundary collar in \(U\) values), not on \(u^{(j)}\). The L1-J proof skeleton step 1 already does this correctly; the Labeled Association §9.2 statement should be tightened to:

> 𝒜_bar(j) = the unique dominant global bar with birth vertex in \(N_j^r\) (which is the bar at the highest local max of \(U|_{N_j^r}\) on \(G_j^r\), not necessarily at \(p_j=\arg\max u^{(j)}\)).

### Counterexample search

L1-I empirical: 1233/1920 INFEASIBLE configurations all violate at least one L1-J hypothesis (LG-1, LG-2, LG-4, or H6). For configurations satisfying all hypotheses (439 FEASIBLE_WITH_BUDGET), no observed K_bar > K_act. No counterexample.

### Verdict

**VERIFIED_WITH_CLARIFICATION.** The proof is correct in conclusion; the labeled association statement should clarify the "primary" identification. Required repair: minor wording update in L1-J §9.

---

## 8. L1-J PO-1 Audit — Decay-to-Cut Bridge Bound

### Claim

Under (D1) decay profile \(u^{(j)}(x)\le\psi(d_G(x,S_j^\delta))\), (D2) separator \(C_{jk}\) at distance \(\ge q\) from every active support, (D3) inactive residual on cut \(\le h_{\mathrm{noise}}\):

\[
H_{C_{jk}}(U)\le K_{\mathrm{act}}\psi(q)+h_{\mathrm{noise}}.
\]

By L1-B finite-graph cut lemma:

\[
\theta_{\mathrm{bridge}}^{jk}(U)\le H_{C_{jk}}(U)\le K_{\mathrm{act}}\psi(q)+h_{\mathrm{noise}}.
\]

### Audit

**Sum bound:** For \(x\in C_{jk}\),

\[
U(x)=\sum_{\ell\in A}u^{(\ell)}(x)+R_{\mathrm{inact}}(x)
\le
\sum_{\ell\in A}\psi(d_G(x,S_\ell^\delta))+h_{\mathrm{noise}}
\le
K_{\mathrm{act}}\psi(q)+h_{\mathrm{noise}},
\]

using monotone-decreasing \(\psi\) and \(d_G(x,S_\ell^\delta)\ge q\) for every \(\ell\in A\) (D2). \(\sup\) over \(C_{jk}\) gives \(H_{C_{jk}}(U)\). **Verified.**

**Heterogeneous decay clarification:** If different active fields have different decay profiles \(\psi_\ell\), the bound generalizes to

\[
H_{C_{jk}}(U)\le\sum_{\ell\in A}\psi_\ell(q)+h_{\mathrm{noise}}.
\]

L1-J uses uniform \(\psi\) for simplicity; this is acceptable but should be noted as a simplification.

**Separator existence:** Existence of \(C_{jk}\) at distance \(\ge q\) from every active support is hypothesis (D2), not derived. On \(T^2_{20}\) with raw Gaussian bumps (L1-I FEASIBLE regime), the separator exists by construction. On dense graphs without good separators, (D2) might fail.

### Numerical verification

`CODE/scripts/results/l1j_decay_to_cut.json` tested 6 configurations including σ_b=2.0 (WQ-1 default). All 6 satisfy the bound with margin. ✓

### Verdict

**VERIFIED_AS_CONDITIONAL.** PO-1 lemma is proof-grade under (D1)–(D3). The bound is non-vacuous on the L1-I FEASIBLE regime. Heterogeneous-decay clarification recommended but not required.

---

## 9. L1-J PO-2 Audit — Labeled Slot-to-Bar Association

### Claim

Define \(\mathcal A_{\mathrm{bar}}(j)=\) the unique dominant bar with birth vertex in \(N_j^r\). Under L1-J package:

- well-defined (exactly one dominant bar per \(N_j^r\)),
- injective (LG-1 disjoint neighborhoods),
- surjective onto dominant bars (coverage from LG-7 derivation).

### Audit

**Existence per neighborhood.** The lower-bound argument shows the highest local max \(q_j\) of \(U|_{N_j^r}\) gives a global bar of length \(\ge\ell_{\min}\). So at least one. **Verified.**

**Uniqueness per neighborhood.** From Lemma 2 (with repair): no secondary global bar with birth in \(N_j^r\) is dominant. **Verified.**

**Injectivity.** LG-1: \(N_j^r\cap N_k^r=\emptyset\). A bar's birth is in at most one \(N_j^r\). **Verified.**

**Surjectivity onto dominant bars.** From step (α) coverage: every dominant global bar has its birth in some \(N_j^r\). **Verified.**

### Static vs dynamic stability

The label \(\mathcal A_{\mathrm{bar}}(j)\) is **deterministic for a fixed \(U\) and PO-7 tie convention**. Under perturbation of \(\mathbf u\) (e.g., dynamics), the label can change. This is expected behavior — the bridge is a static statement about a fixed state.

### Verdict

**VERIFIED_AS_STATIC_ONLY.** The bijection is well-defined for any fixed state in the L1-J regime. Dynamic stability under SCC dynamics is a separate question not addressed by L1-J or this audit.

---

## 10. L1-J PO-7 Audit — Tie Convention

### Convention

1. Fix total order \(\prec\) on \(X\) (lexicographic on coordinates for \(T^2_n\)).
2. Sort by descending \(U\); break ties by ascending \(\prec\).
3. Process in that order; union-find with elder rule (older = earlier in sorted list).
4. Surviving component receives terminal death \(0\).

### Audit

**Code alignment.** `np.argsort(-u, kind="stable")` is row-major lexicographic stable order. Matches PO-7. ✓

**Determinism.** Every step deterministic given \((U, G, \prec)\). ✓

**Plateau handling.** Tied vertices are processed in \(\prec\)-order. If non-adjacent, both can become birth vertices (separate components). If adjacent, the second joins the first's component (no new birth). Consistent with elder rule. ✓

**Effect on prior theorems.** PO-7 reduces "strict local max" hypotheses to "first-in-tiebreak local max" which is well-defined on every finite graph. All Lemma 1 / Lemma 2 / Lemma 3 arguments carry over verbatim. ✓

### Verdict

**VERIFIED (DEFINITIONAL).** PO-7 is closed.

---

## 11. Circularity and Condition Safety Audit

| Condition | Role | Verdict | Reason |
|---|---|---|---|
| (P0) Terminal-death convention | Definitional | SAFE | code-aligned; no smuggling |
| (P1) Tie convention \(\prec\) | Definitional | SAFE | fixed total order on \(X\) |
| (P2) Active mass + connected support | Definitional / measurable | SAFE | per-state condition; \(S_j^\delta\) derived from \(u^{(j)}\), not external labels |
| (P3) LG-1 disjoint neighborhoods | Geometric | SAFE | structural separation; verifiable |
| (P4) LG-2 boundary collar | Geometric | SAFE | shape near boundary; verifiable |
| (P5) LG-4 background \(U\) bound | Geometric | SAFE | aggregate-field bound on \(X_{\mathrm{bg}}\); verifiable |
| (P6) Birth height \(\ge h_{\min}\) | Field-shape | SAFE | peak height; verifiable |
| **(P7) Decay-to-cut** | Field-shape | **SAFE TECHNICAL** | shape on \(u^{(j)}\); decay-with-distance, not object-identity |
| (P8) H6 on \(G_j^r\) | Slot-internal | SAFE | local barcode bound on slot field |
| (P9) NE-2 perturbation | Slot interaction | SAFE | aggregate residual bound |
| (P10) Inactive residual ≤ \(\ell_{\min}-\rho_{\mathrm{res}}\) | Residual bound | SAFE | aggregate inactive |
| (P11) Margin ledger | Constants compatibility | SAFE | empirically verifiable; consistent with L1-I |
| LG-7 coverage | Derived (NOT axiom) | SAFE | proven from LG-4 + terminal-death |
| Global \(K_{\mathrm{bar}}=K_{\mathrm{act}}\) as hypothesis | (NOT used) | FORBIDDEN if assumed | conclusion-smuggling |
| Pre-given external object labels | (NOT used) | FORBIDDEN if assumed | violates CN10 / CN11 |
| \(N_j^r\) derived from \(u^{(j)}\) | Derived from field, not external | SAFE | not a pre-given label |
| \(S_j^\delta\) derived from \(u^{(j)}\) | Derived from field, not external | SAFE | not a pre-given label |
| \(\psi\) decay profile shape on \(u^{(j)}\) | Field-shape | SAFE | shape-of-bump, not object-identity |

### Verdict

**SAFE_WITH_CLARIFICATIONS.** No circularity. No conclusion-like hypothesis. No pre-given external object labels. (P7) decay-to-cut is field-shape and is the most substantive new assumption; it is classified SAFE TECHNICAL. The clarifications are:

- (P7) heterogeneous-decay generalization should be noted (audit §8 issue).
- Lemma 2 proof step 2 should be replaced by contradiction argument (audit §6 issue).
- Labeled association §9.2 should clarify "primary" = highest local max of \(U|_{N_j^r}\) (audit §7 issue).
- Plateau handling under PO-7 should be explicitly noted (audit §4 issue).

---

## 12. Counterexample / Stress-Test Register

| Stress test | Source | Targets | Result |
|---|---|---|---|
| CE-1 high corridor (path 5, U(2)=0.95) | `l1h_counterexample.py` | LG-4 | LG-4 violated; defeats (P5); no contradiction with L1-J |
| CE-1 low corridor | same | LG-4 holds | LG-4 holds; K_bar = sum local; consistent |
| CE-2 background spike (dumbbell) | same | LG-4 | LG-4 violated; defeats (P5); no contradiction |
| CE-3 perturbation-boost | same | bottleneck stability | tightened H6 not yet violated by perturbation; consistent |
| CE-4 equal-height ties | same | PO-7 | tie convention handles correctly; consistent |
| ST-1..ST-5 boundary leakage stress | `l1h2_boundary_leakage.py` | Lemma 1 | inequality \(\ell_{\mathrm{glob}}\le\ell_{\mathrm{loc}}\) holds in all 5 cases (with equality) |
| L1-I FEASIBLE (439/1920) | `l1i_constants_feasibility.py` | full L1-J package | satisfies all (P0)–(P11); empirical regime non-empty |
| L1-I INFEASIBLE (1233/1920) | same | violates ≥1 hypothesis | (P0)–(P11) violated; no contradiction with L1-J theorem |
| L1-J decay-to-cut (6 configs) | `l1j_bridge_cut_decay_diagnostic.py` | PO-1 (D1)-(D3) | bound holds with margin in all 6 configs |
| Adversarial Lemma 2 attempt | this audit | matching argument | contradiction-based repair gives rigorous proof |

**No counterexample to the conditional theorem under (P0)–(P11).**

---

## 13. Cat-Status Recommendation

**Recommendation: THEOREM_CANDIDATE_STRONG_AUDIT_PASSED.**

The audit confirms:

- Lemma 1 (Component-Inclusion) is rigorous as stated.
- Lemma 2 (Secondary-Bar Non-Promotion) is rigorous after replacing the §8.1 proof step 2 with the contradiction-based argument; the conclusion is correct.
- Lemma 3 (Local-to-Global Upper Bound) is rigorous as stated; the labeled association statement should clarify "primary" identification.
- PO-1 (Decay-to-Cut) is rigorous under (D1)–(D3).
- PO-2 (Labeled Association) is rigorous (static).
- PO-7 (Tie Convention) is definitional and well-stated.
- No circularity. No pre-given object labels. No conclusion-smuggling.
- No counterexample within the L1-J package.

Cat-A still requires:

1. Apply the four required repairs (proof-hygiene; not substantive).
2. Decision on canonical adoption of (P7) decay-to-cut, OR derive (P7) from primitive SCC dynamics (L1-L theorem).
3. Plateau extension under PO-7 explicitly written (L1-H2-EXT).

---

## 14. Required Repairs or Clarifications

| ID | File | Section | Issue | Repair |
|---|---|---|---|---|
| R-1 | `kbar_kact_bridge_L1H2_boundary_leakage.md` | §8.1 Lemma 2 proof step 2 | "secondary-to-secondary matching" not enforced by bottleneck distance | Replace step 2 with contradiction-based argument: assume \(\ell_{j,2}(U;G_j^r)\ge\ell_{\min}\); show two bars must match to single \(u^{(j)}\)-primary; contradiction |
| R-2 | `kbar_kact_bridge_L1J_catA_upgrade_attempt.md` | §9.2 Labeled Association | "primary peak \(p_j\)" imprecise under perturbation | Replace with "the highest local max of \(U|_{N_j^r}\) on \(G_j^r\)" |
| R-3 | `kbar_kact_bridge_L1H2_boundary_leakage.md` | §7.3 (or new appendix) | strict-tie hypothesis assumed; PO-7 plateau handling not explicit | Add paragraph: "Under PO-7, strict local maxima reduce to first-in-tiebreak local maxima; the proof carries over." |
| R-4 | `kbar_kact_bridge_L1J_catA_upgrade_attempt.md` | §8.1 PO-1 lemma | uniform \(\psi\) for all active fields | Add: "If different active fields have different decay profiles \(\psi_\ell\), the bound generalizes to \(H_{C_{jk}}(U)\le\sum_\ell\psi_\ell(q)+h_{\mathrm{noise}}\)." |

These four repairs are **proof-hygiene**, not substantive. The audit's verdict (THEOREM_CANDIDATE_STRONG_AUDIT_PASSED) holds with or without them; the repairs improve the documents' precision and prepare them for canonical adoption.

---

## 15. Relationship to OP-0005 / OP-0008

L1-K does not change the standing of OP-0005 or OP-0008.

- **OP-0005 (K-Selection):** L1-J / L1-K deal with the bridge \(K_{\mathrm{bar}}=K_{\mathrm{act}}\), not K-selection. Reservoir-effective rank reformulation remains a working subprogram.
- **OP-0008 (\(\sigma\)-inheritance):** L1-J / L1-K do not establish \(\sigma_{\mathrm{rich}}\) sufficiency or deterministic \(\Phi_{\mathrm{rich}}\).

No \(\sigma_{\mathrm{rich}}\) sufficiency claim is licensed by L1-K.

---

## 16. Final Verdict

**THEOREM_CANDIDATE_STRONG_AUDIT_PASSED.**

The L1-H2 / L1-J theorem candidate passes external audit. Lemmas 1, 2 (with proof repair), 3, PO-1, PO-2, and PO-7 are all rigorously proved under the L1-J package. No circularity, no pre-given object labels, no conclusion-smuggling. No counterexample within the package.

Cat-A remains pending:

- Application of the four required proof-hygiene repairs.
- Decision on canonical adoption of (P7) decay-to-cut OR derivation of (P7) from primitive SCC dynamics.
- Plateau-handling under PO-7 written out.

These are narrow, concrete, achievable next steps. The theorem is **closer to Cat-A than at any prior point** in the L1-A through L1-J chain.

---

## 17. Next Work Packages

### L1-K-REPAIR — Apply audit repairs (recommended next, fast)

Apply the four repairs from §14 to `kbar_kact_bridge_L1H2_boundary_leakage.md` and `kbar_kact_bridge_L1J_catA_upgrade_attempt.md`. These are proof-hygiene only; no new mathematics. Estimated effort: < 1 hour.

### L1-L — SCC-Decay Theorem (separate workstream)

If (P7) decay-to-cut is to become canonical without being a hypothesis, derive it from primitive SCC dynamics. Target:

> For SCC-stationary states under appropriate energy / regularity conditions, \(u^{(j)}\) admits a decay profile \(\psi(d)\) bounded by SCC-derived quantities.

This is a substantive theorem-grade task outside L1-K's scope.

### L1-H2-EXT — Plateau / non-strict tie extension

Routine rewriting of Lemma 1 under PO-7. Estimated effort: 1–2 hours.

### L1-M — Soft-count corollary using L1-K-passed bridge

If the four repairs are applied and the bridge is ready for canonical adoption, the soft-count corollary

\[
K_{\mathrm{soft}}^\phi(U)=K_{\mathrm{act}}^\varepsilon(\mathbf u)+O(\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}+\rho_\phi)
\]

for \(\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)\) (per WQ-LAT-1.B) becomes a Cat-A target. Use L1-J + L1-K + WQ-LAT-1.B to bound the error terms.

### L1-CANONICAL-PROMOTION (deferred)

After repairs + (P7) decision + L1-H2-EXT, canonicalization can proceed: assign theorem-status registry entry, update `theorem_status.md`, propagate to canonical specification. This is a process step, not a research step.

---

**End of L1-K external audit.** Verdict: **THEOREM_CANDIDATE_STRONG_AUDIT_PASSED**. Four required proof-hygiene repairs identified; no substantive flaw. Cat-A path is now narrow and concrete.
