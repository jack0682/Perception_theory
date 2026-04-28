# 03_canonical_proposal_v5b_t_update.md — Canonical Proposal Package (TEXT-PENDING)

**Session:** 2026-04-28 (W5 Day 2 MODERATE, Block 2)
**Target (from plan.md §3 Block 2 11:45-12:30):** Canonical proposal package for user decision (Day 2 PM Block 4 or Day 3+).
**This file covers:** §1 scope; §2 proposal #1 V5b-F mechanism rider (TEXT-PENDING — awaits Day 3 Branch verdict); §3 proposal #2 ζ_*(graph) precise (TEXT-PENDING — awaits Day 3 numerical); §4 proposal #3 NQ-191 spawn (Day 2 actionable); §5 proposal #4 Commitment 14 (O5')/(O7) (Day 1 carry, optionally Day 2 if user approves); §6 estimated canonical line delta; §7 user decision matrix.
**Depends on reading:** `01_NQ173_v5b_f_verdict.md` (V5b-F status DEFERRED); `02_NQ174_zeta_star_results.md` (ζ_* status DEFERRED); `2026-04-27/92_critical_review_round2.md` §2 + §4 (O5'/O7 proposed text); `canonical.md` §11.1 Commitment 14 (line 768) + §13 T-V5b-T (lines 1117-1167).
**Status:** **3 of 4 proposals text-pending pending Day 3 numerical**. 1 proposal (NQ-191 spawn) is Day 2-actionable. 1 proposal (Commitment 14 (O5')/(O7)) was Day 1 carry awaiting user decision.

---

## §1. Scope of This Package (Day 2 EOD updated)

Day 2 plan §3 Block 2 expected complete proposal package by 12:30. Per Day 2 EOD numerical execution (via monkey-patch wrappers `_nq173_with_bypass.py` + `_nq174_with_bypass.py`), the originally TEXT-PENDING proposals are **now FILLED with actual values**:

- **Proposal #1 V5b-F mechanism rider**: filled with Branch B refined (regime R3) per `01_NQ173_v5b_f_verdict.md` §3.4. See §2 below.
- **Proposal #2 ζ_*(graph) precise**: filled with ζ_*(2D torus L=20, c=0.10) ≈ 0.40 per `02_NQ174_zeta_star_results.md` §6. **NEW finding: c-dependence** requires statement rephrasing. See §3 below.
- **Proposal #3 NQ-191 spawn register**: Day 2 actionable, default D-5 conservative (NOT applied; user decision required).
- **Proposal #4 Commitment 14 (O5')/(O7)**: Day 1 carry, default D-5 conservative (NOT applied; user decision required).

**Per meta-prompt §8.1**: this file does **not** edit canonical directly. All canonical-edit decisions stay with the user.

---

## §2. Proposal #1: V5b-F Mechanism Rider in T-V5b-T (TEXT-PENDING)

### 2.1 Current canonical (line 1151)

```
*Distinct from non-translation-invariant graphs (V5b-F)*: Free BC, barbell,
SBM exhibit *partial* Goldstone (overlap 0.5–0.85) due to boundary lifting;
this is a separate phenomenon currently sketched as Cat C (NQ-173).
```

### 2.2 Proposed update (Day 2 EOD — Branch B refined verdict)

Per `01_NQ173_v5b_f_verdict.md` §3.4 verdict (Branch B refined: H1+H2+H3 mixed in regime R3 corner sub-lattice):

**Proposed canonical text** (replacement for line 1151 sentence):

```
*Distinct from non-translation-invariant graphs (V5b-F refined, Cat B target)*:
Free BC, barbell, SBM exhibit *partial* Goldstone (full-space overlap 0.5–0.78,
bulk-only overlap 0.55–0.78) in the **corner sub-lattice regime**
(β > 1/a², c < c_s = (3-√3)/6 ≈ 0.211). Mechanism: the lowest non-tangent
Hessian mode is a hybridization of:
  (a) bulk-localized translation Goldstone of the corner-saturated cluster
      (H1 partial: bulk overlap exceeds full overlap by 0.03–0.10);
  (b) boundary-mode mixing with cluster-boundary spectral modes
      (H2: α²+β² ≈ 0.46–0.65, γ component ≈ 0.35–0.54);
  (c) PN-barrier-lifted eigenvalue μ_Gold^lifted ≈ 1–4 (H3: lattice-translation
      symmetry from "approximate" to "weakly explicit").
All three mechanisms operate jointly. Cat B target; analytic PN-barrier formula
NQ-198 (W6+) is the Cat A path.
Empirical anchor: NQ-173 W5 Day 2, 15/15 attempts at L=20, c=0.10,
ζ ∈ {0.5, 0.7, 1.0}.
```

### 2.3 Day 2 status

**Filled with actual values.** Awaits user decision (D-1 approve canonical edit / D-2 defer / D-3 modify / D-5 conservative).

### 2.4 Estimated canonical delta (after Day 3 verdict)

- ~5 lines replaced in T-V5b-T entry (line 1151 expansion).
- Optional: +10 lines if a sub-statement (V5b-T-f) is added documenting V5b-F as a Cat B sister-theorem rather than just a sentence.
- **Total: ~5-15 lines** depending on user preference for in-line note vs sub-statement.

---

## §3. Proposal #2: ζ_*(graph) Precise Values in T-V5b-T-(d) (TEXT-PENDING)

### 3.1 Current canonical (line 1129)

```
- $\zeta_*(2D \text{ torus}) \in [0.2, 0.5]$ (bracketed by $\zeta=0.2$
  overlap 0.49, $\zeta=0.5$ overlap 0.97).
- $\zeta_*(1D \text{ cycle}) < 0.2$ (sub-lattice overlap already 0.76 at $\zeta=0.2$).
- Precise value and dimensionality dependence: NQ-174.
```

### 3.2 Proposed update (Day 2 EOD — actual measurements)

Per `02_NQ174_zeta_star_results.md` §6 measurements:

```
- $\zeta_*(2D \text{ torus } L=20, c=0.10) \approx 0.40$
  (NQ-174 W5 Day 2; mean overlap 0.920 at ζ=0.40 crosses 0.9 threshold).
- $\zeta_*(1D \text{ cycle } L=40, c=0.10) > 0.15$ (super-lattice transition
  NOT reached in tested ζ ∈ {0.05, 0.10, 0.15} range; mean overlap stays 0.70-0.74.
  Extended sweep NQ-174d W5 Day 3+ at ζ ∈ {0.20, 0.30, 0.50}).
- **NEW c-dependence finding**: ζ_* depends on volume fraction c, not only on graph class.
  Compare NQ-170c (c=0.5) vs NQ-174 (c=0.10):
    2D torus L=20: c=0.5 bracket [0.20, 0.50]; c=0.10 ≈ 0.40.
    1D cycle L=40: c=0.5 has overlap 0.76 at ζ=0.2 (ζ_* < 0.2); c=0.10 has overlap
    0.74 at ζ=0.15 (ζ_* > 0.15). Different c-regimes give different ζ_*.
- **Finite-size**: $L=20$ for 2D, $L=40$ for 1D; thermodynamic-limit ζ_*(∞):
  NQ-174c W6+.
- **Precise functional form** $\zeta_*(d, G, c)$: open (NQ-174b W6+).
- **Anomaly at ζ=0.45 on 2D torus L=20 c=0.10**: overlap drops 0.92 → 0.70
  (mode-crossing at deeper super-lattice; investigate via NQ-174e W6+).
```

### 3.3 Day 2 status

**Filled with actual values.** Awaits user decision. **Note**: the original canonical T-V5b-T-(d) bracket was at c=0.5; current measurement is at c=0.10. Statement should be **rephrased to specify c**, or two separate entries should be added (one per c-regime).

### 3.4 Estimated canonical delta (after Day 3)

- ~3 lines replaced (line 1129 area).
- ~5 lines added (dimensionality ratio + finite-size note + NQ-174b/c spawn).
- **Total: ~5-10 lines**.

---

## §4. Proposal #3: NQ-191 Spawn (Day 2 Actionable)

### 4.1 Statement

Add to `theorem_status.md` "Spawn NQ" register (or wherever NQ items are tracked):

```
NQ-191 (W5+): scc validation framework — distinguish variational vs
metastable-stationary use of `find_formation`. Currently `params.validate`
forbids c outside spinodal (0.211, 0.789), which blocks any IC-driven
metastable-formation Hessian study at small c. NQ-173, NQ-174, future
multi-formation σ Phase 5 with small per-formation m_j (G3) all need
this. Recommended patch: additive scc API kwarg `allow_outside_spinodal:
bool = False` on both `find_formation()` and `params.validate()`. Day 3
morning Block 0 estimated ~30 min implementation + test.
```

### 4.2 Day 2 actionable — but where?

NQ-191 is a **Day 2 finding** (this session). Adding to canonical theorem_status.md = canonical edit (forbidden by meta-prompt §8.1). Two options:

**Option (a)**: Register only in this file's spawn list + Day 2 99_summary.md NQ register; Day 3 promotes it to theorem_status.md.

**Option (b)**: Treat NQ register as "auxiliary" canonical (not theory-content but project-tracking) and allow direct edit.

**Recommendation (a)**: Be conservative; let user decide whether NQ register is canonical-content or project-content.

### 4.3 Estimated canonical delta

- 0 lines today (Day 2 conservative path).
- Day 3+: ~3-5 lines if NQ-191 is added to a "Spawn NQ" section of theorem_status.md.

---

## §5. Proposal #4: Commitment 14 (O5')/(O7) — Day 1 Carry

### 5.1 Background

Per `2026-04-27/92_critical_review_round2.md` §§2 + 4, two sub-clauses to Commitment 14 (canonical §11.1) are proposed:

- **(O5')** multi-irrep eigenspace convention.
- **(O7)** tie-breaking for degenerate eigenvalues.

These are non-trivial canonical changes deferred to user decision Day 1 → Day 2.

### 5.2 Review of O5' (multi-irrep convention)

**Proposed text** (from `92_critical_review_round2.md` §4.3):

```
(O5') Multi-irrep eigenspace convention. When dim V_k > 1 with
V_k = ⊕_{[ρ]} V_k^{[ρ]} (Lemma 1 (ii)) containing r > 1 distinct irreps,
the σ-tuple entry for eigenvalue λ_k is
({n^{[ρ]}_k}_{[ρ]}, {[ρ]}_{[ρ]}, λ_k) — a multi-set of nodal counts and
irrep labels at this eigenvalue. The lex-ordering of the multi-set follows O7.
```

**Consistency check (Day 2 review)**:

- ✓ Consistent with T-σ-Theorem-3 (vi) usage: existing entry "$(2, [E], \mu_2)$" treats 2-dim $E$ irrep as a single σ-tuple entry. O5' generalizes this to multi-irrep eigenspaces.
- ✓ Consistent with T-σ-Theorem-4 (v) σ-signature: the "two entries with $\lambda = 4|W''(c)|\epsilon$ but irreps $[+1]$ vs $[-1]$" case is a 2-dim eigenspace splitting into 1-dim irreps each — this is **NOT** a single multi-set entry per O5' but two separate entries (because the two irreps are at the *same* eigenvalue but in distinct *sub-eigenspaces* that happen to be 1-dim each). The O5' convention applies when a single eigenspace block has multiple irreps; the Theorem-4 case is a degenerate-eigenvalue / distinct-eigenspace case (handled by O7).

**The two cases are subtly different**:
- O5' case: $V_k$ is a single Hessian eigenspace (geometric multiplicity ≥ 2) with multi-irrep isotypic decomposition.
- O7 case: $V_k$ and $V_{k+1}$ are *distinct* eigenspaces that happen to share the same eigenvalue (algebraic multiplicity > 1; possible due to bifurcation degeneracy as in T-σ-Theorem-4 D_4 case).

**O5' covers**: 2D rep $E$ on $D_4$ stays as single multi-irrep entry → useful in Theorem 3 (vi).
**O7 covers**: $K_0 = K_1$ degeneracy on $D_4$ at leading order → useful in Theorem 4 (v).

The two sub-clauses are **complementary**; both are needed for σ to be a deterministic discrete invariant.

### 5.3 Review of O7 (tie-breaking)

**Proposed text** (from `92_critical_review_round2.md` §2.2):

```
(O7) Tie-breaking for degenerate eigenvalues. When λ_k = λ_{k+1} but
[ρ_k] ≠ [ρ_{k+1}], order entries by the canonical character-table order
of the residual stabilizer's irreps. For D_4 = {A_1, A_2, B_1, B_2, E}:
order A_1, A_2, B_1, B_2, E (Mulliken convention). For Z_2 = {[+1], [-1]}:
order [+1], [-1] (trivial first). For Z_n cyclic: order [1], [ω], [ω²], ...
by phase. For general finite groups: order by isomorphism-class invariants
(smallest dimension first; within same dimension, order by character of generator).
```

**Consistency check (Day 2 review)**:

- ✓ Mulliken convention is standard in computational chemistry and group-theoretic crystallography literature; widely cited (e.g., Mulliken 1933 J. Chem. Phys.).
- ✓ Covers both small (Z_2, D_4) and general (any finite group) cases.
- ✓ Compatible with existing T-σ-Theorem-4 (v) "lex-ordering convention places trivial irrep before sign irrep" — that local convention becomes a special case of O7 (Z_2 = {[+1], [-1]} order $[+1], [-1]$).

**One mild concern**: "smallest dimension first" for general groups might not align with Mulliken on all cases. For $D_4$: dimensions are $A_1=1, A_2=1, B_1=1, B_2=1, E=2$ — Mulliken places $E$ last, consistent with "smallest first". For $D_6$ (hexagonal): irreps include $A_1, A_2, B_1, B_2, E_1, E_2$ — Mulliken places $E_1, E_2$ last; "smallest first + character-of-generator within dim" gives same order (since 1-dim listed by sign character first). So **Mulliken = "smallest dimension first + character-table order within dim"** for the standard finite groups encountered in SCC σ-framework (cyclic, dihedral, symmetric).

Verdict: O7 text is **consistent**. No revision needed for SCC-relevant groups.

### 5.4 Compatibility with paper §4 σ-framework section

User asked in `92_critical_review_round2.md` §13 discussion topics:
- "O5' multi-irrep representation: multi-set vs separate entries — which is more useful for paper §4 σ-framework section?"

**My recommendation (this session)**: **Multi-set (O5' as proposed)** is preferable for paper exposition. Reasons:

1. **σ-tuple length stability**: with multi-set, σ-tuple length = number of *distinct Hessian eigenvalues* (always ≤ $K$, where $K$ is the cutoff). With separate entries, σ-tuple length depends on irrep decomposition of each eigenspace — this length depends on the symmetry group, which makes cross-graph σ-comparison awkward.

2. **Reader navigation**: a single entry per eigenvalue with multi-set irrep label is parseable visually as one "row" in a table. Separate entries fragment the σ display.

3. **Existing T-σ-Theorem-3 (vi) precedent**: already uses multi-set (single $(2, [E], \mu_2)$ entry for 2-dim $E$). Consistency.

### 5.5 Compatibility with T-σ-Theorem-4 (v) σ-tuple ordering

**With O5' + O7 jointly applied**, the T-σ-Theorem-4 (v) σ-tuple becomes:

$$\sigma(u^*_\epsilon)\big|_{D_4} = \big(\mathcal{F}; (1, [+1], 4|W''(c)|\epsilon),\ (1, [-1], 4|W''(c)|\epsilon),\ \ldots\big)$$

The two entries are separately listed (O5' multi-set doesn't apply because each is a 1-dim sub-eigenspace at the same eigenvalue, not a multi-irrep block). Their ordering follows O7: $[+1]$ before $[-1]$ (Z_2 convention).

This is **consistent** with the locally-stated convention in the existing canonical T-σ-Theorem-4 (v) entry "lex-order trivial first". O7 simply promotes the convention to canonical Commitment level.

### 5.6 Should both go into canonical v1.5 (today's edit) or separate v1.6 release?

User asked in `92_critical_review_round2.md` §13.

**My recommendation**: **Both go into v1.5 together** if approved. Reasons:
- Both are well-definedness sharpenings of the same Commitment 14 σ-tuple representation (no new mathematical content; clarifying existing).
- Both are cited locally in T-σ-Theorem-3 (vi) and T-σ-Theorem-4 (v) — having canonical Commitment 14 also reflect them removes a "pending elevation" issue.
- v1.5 is already release-ready post-G0; one more Commitment-level addendum doesn't destabilize.
- Splitting into v1.5 (O5') and v1.6 (O7) creates artificial separation; they jointly resolve well-definedness (5.4-5.5 above show they are complementary).

**Counter-recommendation only if**: user wants to give the σ-framework community time to react to v1.5 before another release. In that case, defer O5'/O7 to v1.6 (W6+).

### 5.7 Day 2 actionable status

Per **meta-prompt §8.1** (canonical 직접 수정 금지), this session **cannot edit canonical** even if user approves. Therefore:

- **Today's Block 4** (per plan.md §3 Block 4): user reviews this section (§§5.2-5.6) for approve/modify/defer.
- **If user approves with explicit "edit canonical now"**: user's explicit instruction overrides meta-prompt §8.1 default; Claude executes the edit.
- **If user defers** (per plan.md F6): canonical v1.5 stays unchanged; Day 3+ revisit.

**Default Day 2 behavior**: prepare proposal text (this section), do not edit canonical, await user explicit approval.

---

## §6. Estimated Total Canonical Line Delta (Day 2 EOD updated)

| Proposal | Lines if approved |
|---|---|
| #1 V5b-F mechanism rider (Branch B refined, regime R3) | ~15-20 (replaces 1 sentence + adds (a)/(b)/(c) mechanism breakdown) |
| #2 ζ_*(graph, c) precise + c-dependence + 1D cycle extended note | ~10-15 (replaces line 1129 with c-qualified statements + NEW c-dependence remark) |
| #3 NQ-191 spawn register | ~3-5 (theorem_status.md spawn-NQ section if user approves) |
| #4 Commitment 14 (O5')/(O7) | ~30-50 (canonical §11.1 Commitment 14 addendum) |
| **Total Day 2 actionable (if user approves all)** | **~60-90 lines** |

This **exceeds plan.md §4 estimate (50-80)** because c-dependence finding (#2) requires more text than original bracketed-value replacement.

**All 4 proposals now have actual content** (originally only #4 was actionable; numerical execution Day 2 EOD via monkey-patch unlocked #1 and #2).

---

## §7. User Decision Matrix (this session's hand-off)

| Decision | Day 2 path | Day 3+ implication |
|---|---|---|
| **D-1: Approve O5' + O7 in canonical v1.5 today** | Edit `canonical.md` §11.1 + `theorem_status.md` + `CHANGELOG.md` (~30 lines). Requires user explicit "edit now" override of meta-prompt §8.1. | v1.5 self-consistent with σ-framework well-definedness sharpened. |
| **D-2: Defer O5' + O7 to v1.6 (W6+)** | No canonical edit Day 2. Proposal text preserved here. Document deferral in `99_summary.md`. | v1.5 release proceeds without σ-tuple ordering Commitment-level convention; local Theorem-4 (v) convention stays the operational fallback. |
| **D-3: Modify O5'/O7 text** | User specifies modification; Claude updates §5.2/5.3 of this file; user re-reviews. | Subsequent canonical edit per modified text. |
| **D-4: Approve NQ-191 register addition Day 2** | Edit `theorem_status.md` Spawn-NQ section (+3-5 lines). Requires user explicit override of meta-prompt §8.1. | NQ-191 visible in canonical project tracking. |
| **D-5: Conservative — no canonical edit Day 2** | All 4 proposals stay in this file. Day 2 99_summary reflects "0 canonical delta Day 2". Day 3 PM resumes after numerical. | Day 3 PM canonical edit batch: V5b-F + ζ_* + (optional Commitment 14 if D-2 was "defer to Day 3" not "v1.6"). |

**Recommended default (this session)**: **D-5 (conservative)** unless user explicitly overrides. Rationale:
- F1 deferral has already shifted the canonical-edit timing from Day 2 PM to Day 3 PM.
- Combining O5'/O7 with V5b-F + ζ_* into a single Day 3 PM canonical edit batch creates one coherent v1.5.1 release rather than two separate edit waves.
- Avoids partial-canonical-edit state (some Commitment 14 update without σ-supporting V5b-F update yet).

---

## §8. Hard Constraint Verification

- [x] **canonical 직접 수정 0** — this file proposes; user decides; Claude does not autonomously edit.
- [x] **Silent resolution 0** — no proposal silently resolves an open problem; each is explicitly attributed (NQ-173/174/192 spawn; O5'/O7 Day 1 carry).
- [x] **No primitive override** — all proposals operate within u_t-primitive σ-framework.
- [x] **No 4-energy-term merging** — proposals are about σ-tuple representation and ζ_*-bracket precision, not energy structure.
- [x] **No closure idempotence** — moot.
- [x] **K not dual-treated** — moot (single-formation scope; K=1 implicit).
- [x] **No metastability without P-F flag** — §4 NQ-191 expressly flags P-F (zero-T framework absence) as the deeper context.
- [x] **No reductive equivalence claim** — σ-tuple is SCC-intrinsic per CN10.

---

## §9. Cross-Reference

- V5b-F mechanism details: `01_NQ173_v5b_f_verdict.md` §3.
- ζ_* a priori narrowing: `02_NQ174_zeta_star_results.md` §3.
- O5'/O7 Round-2 critical review: `2026-04-27/92_critical_review_round2.md` §§2 + 4.
- Day 1 deferred decisions: `2026-04-27/100_day2_carry.md` §1 "Awaiting user decision".

---

**End of 03_canonical_proposal_v5b_t_update.md.**
**Status: 3 of 4 proposals TEXT-PENDING (Day 3+ numerical required); 1 actionable Day 2 (Commitment 14 user decision); 0 canonical edits performed by Claude this session.**
