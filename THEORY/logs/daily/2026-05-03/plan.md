# plan.md — 2026-05-03 (W5 Day 7, L1-M Soft-Count Corollary after T-L1-F)

**Title:** 2026-05-03 Research Plan — L1-M Soft-Count Corollary after T-L1-F.
**Session type:** W5 Day 7 — *post-canonical-promotion soft-count corollary draft*. Day 6 (2026-05-02) closed with **CV-1.5.2** canonical release of **T-L1-F** as Cat-A *conditional* under L1-J package $(P0)$–$(P11)$. Day 7 is the natural continuation: build L1-M soft-count corollary on top of the canonical hard-count bridge.
**W5 scope:** 2026-04-27 (Mon, Day 1 G0) ~ 2026-05-03 (Sun, Day 7 W5 close).
**Session working directory:** `THEORY/logs/daily/2026-05-03/`.
**Weekly buffer target:** `THEORY/logs/weekly/2026-04-W5/weekly_draft_storming.md` (latest-first 05-03 entry append).
**Day 6 EOD references:** `THEORY/logs/daily/2026-05-02/01_T_L1_F_canonical_promotion_closure.md` (Day 6 closure); canonical CV-1.5.2 in `theorem_status.md` + `canonical.md` (T-L1-F entry at §13 Cat A); L1 chain L1-A through L1-L in `THEORY/working/MF/`.
**Active runtime:** no team dispatch Day 7 by default; this is corollary-derivation work, single-thread.
**User calibration:** Day 6 EOD message recommended "L1-M — Soft-Count Corollary under $\Phi_{\mathrm{res}}$" as the next concrete research action. Day 7 executes that.

---

## §1. Starting State

- **Canonical version current:** **CV-1.5.2** (2026-05-02). Previous CV-1.5.1 reflagged "Previous Version" in `theorem_status.md`.
- **T-L1-F** is canonically registered as Cat-A *conditional* in both `theorem_status.md` (CV-1.5.2 section, line 18) and `canonical.md` §13 Category A (line 1462, just before Category B header).
- **Core hard-count bridge** (canonical, conditional):
  \[
  K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u);G)=K_{\mathrm{act}}^\varepsilon(\mathbf u)
  \]
  under hypothesis package $(P0)$–$(P11)$.
- **Labeled bijection** (canonical, conditional):
  \[
  \mathcal A_{\mathrm{bar}}:A^\varepsilon(\mathbf u)\to\mathrm{Bars}_0^{\mathrm{term}}(U;G)
  \]
  defined by $\mathcal A_{\mathrm{bar}}(j)=$ the unique dominant bar with birth in $N_j^r$, equivalently born at $q_j^U=\arg\max^\prec_{x\in N_j^r}U(x)$.
- **`THEORY/canonical/theorem_status.md` unchanged.** OP-0005 (K-Selection) and OP-0008 ($\sigma^A$ K-jump non-determinism) remain open; T-L1-F does not solve either.
- **Empirical anchors**: L1-I 439/1920 FEASIBLE_WITH_BUDGET on $T^2_{20}$; L1-H2 5/5 stress tests; L1-J PO-1 6/6 decay-to-cut configs.
- **L1-M is the next research target** (per Day 6 closure recommendation).

---

## §2. Main Objective

Develop **L1-M — Soft-Count Corollary under $\Phi_{\mathrm{res}}$** as the natural successor to T-L1-F.

**Target theorem candidate:** under T-L1-F's package $(P0)$–$(P11)$ AND $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$,

\[
K_{\mathrm{soft}}^\phi(U)=K_{\mathrm{act}}^\varepsilon(\mathbf u)+O(\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi),
\]

or, in rigorous inequality form,

\[
\bigl|K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{act}}^\varepsilon(\mathbf u)\bigr|\le\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi.
\]

This is **NOT** a global identity. It is a controlled approximation under T-L1-F + $\Phi_{\mathrm{res}}$ envelope class.

---

## §3. Key Inputs

- **Canonical T-L1-F** in `THEORY/canonical/canonical.md` §13 Cat A + `theorem_status.md` CV-1.5.2.
- **WQ-LAT-1.B phi-envelope refinement results** (`THEORY/working/MF/wq_lat1b_phi_envelope_refinement_results.md`): 13 envelope variants tested; 5 pass chart-invariance (hard, logistic-$s=100$, logistic-$s=50$, shifted-sat-$\beta=20$, shift-lin); default $\phi$-sat fails.
- **Existing soft-count bridge candidate** (`THEORY/working/MF/ksoft_kact_bridge_lemma.md` §5.3): pre-canonical sketch with $\rho_{\mathrm{sub}},\rho_{\mathrm{edge}},\rho_\phi$ error decomposition. L1-M makes this rigorous under T-L1-F.
- **Proof-status audit** (`THEORY/working/MF/ksoft_kact_bridge_proof_status.md`): C-09, C-10, C-11 lemma candidates already enumerated.
- **Soft-K definition** (`THEORY/working/E/soft_K_definition.md`): $K_{\mathrm{soft}}^\phi(u)=\sum_i\phi(\ell_i(u))$ with monotone Lipschitz $\phi$, $\phi(0)=0$. $L_K\le 4L_\phi n$ via CSEH 2007 bottleneck stability.
- **CSEH 2007 bottleneck stability** (already used in repo for $K_{\mathrm{soft}}$ Lipschitz proofs).
- **Existing $\Phi_{\mathrm{res}}$ definition** (`ksoft_kact_bridge_lemma.md` §5.3.2): nonnegativity + lower normalization + dominant-bar normalization + sub-threshold suppression + dominant-bar retention + regularity + sharpness parameter.

---

## §4. Work Packages

### L1-M.1 — Definition Audit

- Verify $K_{\mathrm{soft}}^\phi(U)=\sum_i\phi(\ell_i)$ with $\ell_i\ge 0$ and terminal-death convention (matches T-L1-F's P0).
- Verify $K_{\mathrm{bar}}^{\ell_{\min}}(U)=\#\{i:\ell_i\ge\ell_{\min}\}$ (canonical, T-L1-F conclusion).
- Verify $\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ definition: $\phi:[0,1]\to[0,\infty)$ with (1) $\phi(\ell)\ge 0$, (2) $\phi(0)=0$, (3) $\phi(\ell)\approx 1$ on $[\ell_{\min}+\tau,\infty)$, (4) $\phi(\ell)\approx 0$ on $[0,\ell_{\min}-\tau)$, (5) sharpness parameter (logistic $s$, shifted-sat $\beta$, etc).
- **Forbidden**: arbitrary monotone Lipschitz $\phi$. WQ-LAT-1.B showed default $\phi$-sat fails by sub-resolution accumulation. $\phi$ MUST be in $\Phi_{\mathrm{res}}$.
- **Required envelope sub-classes** (already empirically verified in WQ-LAT-1.B):
  - $\phi_{\mathrm{hard}}(\ell)=\mathbf 1_{\ell\ge\ell_{\min}}$ (exact integer count = $K_{\mathrm{bar}}^{\ell_{\min}}$);
  - $\phi_{\mathrm{logistic}}^s(\ell)=\mathrm{sig}(s(\ell-\ell_{\min}))-\mathrm{sig}(-s\ell_{\min})$ for $s\ge 50$;
  - $\phi_{\mathrm{shift\text{-}sat}}^\beta(\ell)=1-\exp(-\beta\max(0,\ell-\ell_{\min}))$ for $\beta\ge 20$.

### L1-M.2 — Error Decomposition

Define three error components partitioning the bar set $\{\ell_i\}_i$ at three thresholds:

\[
\rho_{\mathrm{sub}}=\sum_{\ell_i<\ell_{\min}-\tau}\phi(\ell_i)
\quad\text{(sub-threshold tail; should be small under (4))},
\]

\[
\rho_{\mathrm{edge}}^\phi=\sum_{|\ell_i-\ell_{\min}|\le\tau}\bigl|\phi(\ell_i)-\mathbf 1_{\ell_i\ge\ell_{\min}}\bigr|
\quad\text{(edge band; bounded by transition-width $\tau$)},
\]

\[
\rho_\phi=\sum_{\ell_i\ge\ell_{\min}+\tau}|1-\phi(\ell_i)|
\quad\text{(dominant-bar normalization deviation; should be small under (3))}.
\]

Then by triangle inequality:

\[
\bigl|K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{bar}}^{\ell_{\min}}(U)\bigr|
=
\biggl|\sum_i\bigl[\phi(\ell_i)-\mathbf 1_{\ell_i\ge\ell_{\min}}\bigr]\biggr|
\le\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi.
\]

Combine with **canonical T-L1-F** ($K_{\mathrm{bar}}^{\ell_{\min}}=K_{\mathrm{act}}^\varepsilon$ under (P0)–(P11)) to substitute $K_{\mathrm{bar}}\to K_{\mathrm{act}}$:

\[
\bigl|K_{\mathrm{soft}}^\phi(U)-K_{\mathrm{act}}^\varepsilon(\mathbf u)\bigr|\le\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi.
\]

### L1-M.3 — Theorem Candidate

**L1-M Theorem Candidate (to be drafted in `kbar_kact_bridge_L1M_soft_count_corollary.md`).** Under T-L1-F's L1-J package $(P0)$–$(P11)$, $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$, and edge-band control hypothesis (E): $\rho_{\mathrm{edge}}^\phi$ small (e.g., no bars of $U$ within $\tau$ of $\ell_{\min}$, or sharpness parameter $s,\beta$ large enough that envelope transitions are confined), the soft count approximates the active count with explicit error:

\[
\bigl|K_{\mathrm{soft}}^\phi(U(\mathbf u))-K_{\mathrm{act}}^\varepsilon(\mathbf u)\bigr|\le\rho_{\mathrm{sub}}+\rho_{\mathrm{edge}}^\phi+\rho_\phi.
\]

**Status:** L1-M to start as **THEOREM_CANDIDATE_DRAFT** under (P0)–(P11) + $\Phi_{\mathrm{res}}$ + (E). Cat-A status pending audit.

### L1-M.4 — Empirical Reuse

Use existing WQ-LAT-1.B numerical results without rerunning:

| Envelope | Range $\Delta K_{\mathrm{soft}}$ at $\ell_{\min}=0.10$ | Verdict |
|---|---:|---|
| Phi-0 default $\phi$-sat | 0.943 | FAIL (sub-resolution leak) |
| Phi-1 hard threshold | 0.000 | PASS (exact integer = $K_{\mathrm{bar}}$) |
| Phi-4c logistic $s=100$ | 0.001 | PASS (smooth approx of hard) |
| Phi-3d shift-sat $\beta=20$ | 0.005 | PASS (smooth differentiable everywhere) |
| Phi-2 shift-lin | 0.005 | PASS-with-different-meaning (excess persistence, mean 0.154) |

These empirically anchor the theorem-candidate's regime: $\phi\in\{$hard, logistic$_{s=100}$, shift-sat$_{\beta=20}\}$ are confirmed-stable; default $\phi$-sat is forbidden under L1-M.

### L1-M.5 — Proof Status Table

Classify each envelope sub-class in L1-M:

| Envelope | $\rho_{\mathrm{sub}}$ | $\rho_{\mathrm{edge}}^\phi$ | $\rho_\phi$ | L1-M status |
|---|---|---|---|---|
| $\phi_{\mathrm{hard}}$ | 0 (by def) | 0 (no edge band; step at $\ell_{\min}$) | 0 (constant 1 above) | **EXACT corollary**: $K_{\mathrm{soft}}^{\phi_{\mathrm{hard}}}(U)=K_{\mathrm{bar}}^{\ell_{\min}}(U)=K_{\mathrm{act}}^\varepsilon(\mathbf u)$. Direct from definition + T-L1-F. |
| $\phi_{\mathrm{logistic}}^{s\ge 50}$ | $\le e^{-s\tau}$ tail | $O(\tau\cdot$ # edge-band bars) | $\le e^{-s\tau}$ | **THEOREM CANDIDATE** with edge-band control (E). |
| $\phi_{\mathrm{shift\text{-}sat}}^{\beta\ge 20}$ | 0 (zero on $[0,\ell_{\min}]$) | $O(\tau\cdot$ # edge-band bars) | $\le e^{-\beta\tau}$ | **THEOREM CANDIDATE** with edge-band control. |
| Arbitrary monotone Lipschitz $\phi$ (WQ-2 default) | UNCONTROLLED | UNCONTROLLED | UNCONTROLLED | **FORBIDDEN** under L1-M. |

### L1-M.6 — Non-Claims

Must preserve in the L1-M document:
- No global $K_{\mathrm{soft}}^\phi=K_{\mathrm{act}}^\varepsilon$. Equality only under (P0)–(P11) + $\phi\in\Phi_{\mathrm{res}}$ + edge-band control.
- No arbitrary $\phi$. The default WQ-2 $\phi$-sat is excluded; the theorem only applies for $\phi\in\Phi_{\mathrm{res}}$.
- OP-0005 (K-Selection) NOT solved. L1-M is a soft-count corollary, not a K-selection mechanism.
- OP-0008 ($\sigma^A$ K-jump non-determinism) NOT solved. L1-M is restricted to the resolved regime.
- $\sigma_{\mathrm{rich}}$ sufficiency NOT claimed.
- Reservoir theory NOT promoted to canonical.
- P7 NOT generally derived for all SCC states (inherited from T-L1-F).
- No application / robotics / vision claims.

---

## §5. Success Criteria

Day 7 is successful if:

1. `THEORY/working/MF/ksoft_kact_bridge_L1M_soft_count_corollary.md` is **created** (working-grade document, NOT canonical).
2. The document contains a **theorem candidate** (L1-M-Theorem-Candidate) or **corollary candidate** with explicit hypothesis package (T-L1-F (P0)–(P11) + $\Phi_{\mathrm{res}}$ + edge-band control (E)).
3. **Error terms** are explicit: $\rho_{\mathrm{sub}},\rho_{\mathrm{edge}}^\phi,\rho_\phi$ with formulas + envelope-sub-class bounds.
4. **$\Phi_{\mathrm{res}}$** is formalized or referenced cleanly (point to `ksoft_kact_bridge_lemma.md` §5.3.2 + WQ-LAT-1.B empirical sub-classes).
5. **Relation to T-L1-F is explicit**: T-L1-F gives $K_{\mathrm{bar}}=K_{\mathrm{act}}$; L1-M gives $|K_{\mathrm{soft}}^\phi-K_{\mathrm{bar}}|\le\rho$; combine for $|K_{\mathrm{soft}}^\phi-K_{\mathrm{act}}|\le\rho$.
6. **Non-claims preserved** explicitly in the document.
7. **Next step after L1-M is identified** (L1-M-AUDIT, L1-M-FORMALIZE, or canonical adoption path).

---

## §6. Risk Register

- **Risk 1 — Arbitrary $\phi$ creates chart-rank drift.** Default $\phi$-sat fails (WQ-LAT-1.B Phi-0 range 0.943). L1-M MUST restrict to $\Phi_{\mathrm{res}}$. **Mitigation**: §L1-M.1 audit; §L1-M.6 non-claim.
- **Risk 2 — Edge bars near $\ell_{\min}$ create instability.** Bars with $|\ell_i-\ell_{\min}|\le\tau$ are envelope-sensitive. **Mitigation**: edge-band control hypothesis (E) — either no bars in edge band (margin assumption) OR sharpness parameter large enough.
- **Risk 3 — $K_{\mathrm{soft}}$ is real-valued, not integer-valued.** $K_{\mathrm{soft}}^\phi(U)\in\mathbb R_{\ge 0}$ while $K_{\mathrm{act}}\in\mathbb N$. **Mitigation**: state corollary as an INEQUALITY, not equality; absolute-value error bound is the natural form.
- **Risk 4 — Hard threshold is non-smooth.** $\phi_{\mathrm{hard}}$ is exact but not differentiable; smooth $\phi$ is needed for variational analysis. **Mitigation**: distinguish "exact integer" branch (hard) from "smooth approximation" branch (logistic, shift-sat).
- **Risk 5 — Smooth logistic approximation needs sharpness parameter.** $s,\beta$ values must be large enough; $s=100$, $\beta=20$ are empirically supported. **Mitigation**: state explicit sharpness threshold; cite WQ-LAT-1.B.
- **Risk 6 — Empirical WQ-LAT-1.B evidence is not theorem proof.** Numerical tests on $T^2_{20}$ at $\sigma_b\in\{0.5,1.0,1.5,2.0\}$ are anchors, not proofs. **Mitigation**: theorem proof must use T-L1-F (canonical) + $\Phi_{\mathrm{res}}$ definition + CSEH 2007 stability + edge-band hypothesis. Empirical results are supporting evidence, not part of the proof.
- **Risk 7 — $K_{\mathrm{soft}}$ should not be globally identified with $K_{\mathrm{act}}$.** L1-M is a controlled approximation under explicit conditions, not a global identity. **Mitigation**: §L1-M.6 non-claims; explicit error bound in the statement.
- **Risk 8 — Premature canonical adoption.** L1-M is working-grade in Day 7; canonical promotion (analogous to T-L1-F's CV-1.5.2 path) requires audit + repair cycle similar to L1-K + L1-K-REPAIR. **Mitigation**: L1-M is THEOREM_CANDIDATE_DRAFT only; canonical adoption is L1-M-W6 or later.

---

## §7. Expected Output Files

**Likely:**

- `THEORY/working/MF/ksoft_kact_bridge_L1M_soft_count_corollary.md` (working-grade, ~30–50 KB, mirror of L1-J/L1-L style).

**Optional (only if needed):**

- `CODE/scripts/l1m_phi_error_diagnostic.py` — measures $\rho_{\mathrm{sub}},\rho_{\mathrm{edge}}^\phi,\rho_\phi$ on existing L1-I FEASIBLE_WITH_BUDGET states (raw_gaussian) for envelopes $\phi_{\mathrm{hard}}$, $\phi_{\mathrm{logistic}}^{s=100}$, $\phi_{\mathrm{shift\text{-}sat}}^{\beta=20}$. Reuses L1-I state construction + WQ-LAT-1.B envelope catalog. Estimated 1-2 hours if needed.
- `CODE/scripts/results/l1m_phi_error_diagnostic.json` — output.

Code is OPTIONAL; the corollary statement + error decomposition is the priority. Numerical verification is supporting evidence, not blocking.

---

## §8. End-of-Day Target for 2026-05-03

By the end of 2026-05-03, the goal is to have **L1-M drafted as a disciplined soft-count corollary candidate built on top of the canonical T-L1-F hard-count bridge**. The document should:

- State the theorem candidate explicitly with $(P0)$–$(P11)$ + $\Phi_{\mathrm{res}}$ + edge-band control (E).
- Decompose the error into $\rho_{\mathrm{sub}},\rho_{\mathrm{edge}}^\phi,\rho_\phi$ with formulas.
- Tabulate the envelope-sub-class proof status (exact for hard; theorem-candidate for logistic / shift-sat; forbidden for arbitrary).
- Cite T-L1-F canonically (CV-1.5.2 §13 Cat A).
- Preserve all non-claims.
- Identify L1-M's own next steps (L1-M-AUDIT external review; possible L1-M-FORMALIZE; eventual canonical promotion path).

Day 7 is also the **W5 close ceremony** — `weekly_summary.md` finalize for W5 + W6 strategic plan should be addressed in parallel (planned for Day 7 morning per Day 6 plan §3 Block 5). L1-M corollary work is the substantive Day 7 content; W5 close + W6 plan are the procedural Day 7 content.

---

**Source files for Day 7:**
- Day 6 EOD: `THEORY/logs/daily/2026-05-02/01_T_L1_F_canonical_promotion_closure.md`
- L1 chain: `THEORY/working/MF/kbar_kact_bridge_L1*.md` (L1-A through L1-L, 13 documents)
- Canonical: `THEORY/canonical/canonical.md` §13 Cat A T-L1-F entry; `theorem_status.md` CV-1.5.2 section
- WQ-LAT-1.B: `THEORY/working/MF/wq_lat1b_phi_envelope_refinement_results.md`
- ksoft proof status: `THEORY/working/MF/ksoft_kact_bridge_proof_status.md`, `ksoft_kact_bridge_lemma.md`
- Soft-K definition: `THEORY/working/E/soft_K_definition.md`
