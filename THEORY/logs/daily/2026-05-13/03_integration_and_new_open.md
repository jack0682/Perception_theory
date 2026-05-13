# 03 — Integration & New Open Questions

**Session:** 2026-05-13
**Target (from `00_plan.md`):** CV-1.15 promotion application + post-promotion consistency audit.
**This file covers:** §4.5 Integration with canonical / hypothesis_tree / theorem_status / open-problems; §4.6 new open questions raised by the audit; prompt-improvement suggestions (§14 of prompt).
**Depends on reading:**
- `01_exploration.md` and `02_development.md` (today).
- `THEORY/canonical/canonical.md`, `theorem_status.md`, `hypothesis_tree.md`, `CV-1.13_SEAL.md`.
- `THEORY/working/CV115_ACTION_TEMPORAL_COST/` (09_final_audit, 10_patch_plan).
- `THEORY/working/CV114_TEMPORAL_COMPOSITION/05_promotion_draft.md`.

---

## §1. Integration with existing canonical structure

Today's session did not modify canonical. This section enumerates what *would* be integrated under each of the resolution paths (R-A / R-C from `02_development.md` §2.2) and what *cannot* be silently absorbed.

### §1.1 Canonical theorems potentially modified / clarified

No theorem in canonical §13 is *modified* by CV-1.15. The action-cost layer is additive — it introduces new theorems / lemmas / definitions without overwriting existing ones. Specifically:

| Existing canonical item | Touched by CV-1.15? | How |
|---|---|---|
| T-Temporal-Identity (§13 Cat A, CV-1.13) | **NO direct edit.** | CV-1.15 §13.Y header *cross-references* it (refinement-not-replacement framing). Body unchanged. |
| OP-0012-CC reference at canonical.md:1779 | **POSSIBLY cross-linked under R-A.** | Under R-A (co-promote CV-1.14), the OP-0012-CC reference could optionally be cross-linked to "T-CC-StableK-Kernel". Under R-C, no change. |
| §8.5 Transport Term ($\mathcal{E}_{\mathrm{tr}}$, $\mathbf{M}_{t \to s}$) | **NO edit in CV-1.15.** | The patch's (GK) condition explicitly says "*M_{t→s} 정의 변경 필요, CV-1.16 이후*". Deferred. |
| §11 Fixed Commitments | **NO edit.** | Action cost is a layer, not a commitment change. |
| §14 Commitment Notes (CN1–CN14) | **NO edit.** | None of CN1–CN14 is contradicted by CV-1.15. (Verified §1.4 below.) |
| §13 Cat B header line (line 1688) | **STALE pre-existing** | Independently observable: header omits T-Temporal-Identity's Cat B → Cat A promotion of CV-1.13. Hygienic fix when Cat B section touched (Finding 2.4). |
| Retracted section | **NO edit.** | R1–R5 untouched. |
| Appendix OMS (Observer Moduli Space, §17) | **NO edit.** | Orthogonal. |

### §1.2 Existing axioms potentially in tension

The plan asks us to identify tensions with axioms. We scanned canonical §6 (Axiomatic Groups: A. Soft Closure, B. Soft Adjacency, C. Soft Co-belonging, D. Distinction, E. Temporal Transport and Persistence). The action cost interacts most directly with **Group E**.

| Axiom group | Member axioms | CV-1.15 interaction |
|---|---|---|
| A. Soft Closure | A1–A4 (stabilization tendency, contraction etc.) | Indirect: $\mathrm{Cl}_i(u_i)(x)$ is a component of $\varphi_i$; CV-1.15 uses $\varphi_i$ as the fingerprint coordinate but does **not** modify or assume idempotence (CN1). No tension. |
| B. Soft Adjacency | B1–B3 | Indirect: $D_i(x; 1-u_i)$ is also a fingerprint component. No tension. |
| C. Soft Co-belonging | C1–C3 | None. C_t is a derived diagnostic; CV-1.15 does not invoke it. |
| D. Distinction | D1–D3 | Indirect via $D_i$ fingerprint coordinate. No tension. |
| **E. Temporal Transport and Persistence** | E1–E4 (admissibility) | **CV-1.15's action-derived Gibbs kernel $\mathbf{K}_{i\to k}$ is NOT claimed to satisfy E1–E4.** This is the (GK) condition: if and only if we redefine $M_{t\to s} := \mathbf{K}_{t\to s}$, then $M$ inherits E1–E4-like properties (positivity, row-summability after normalization). The current canonical $M_{t\to s}$ is the Sinkhorn partial-OT plan; it is *different* from $\mathbf{K}$. **Tension: latent.** Resolution: canonical §8.5 redefinition is explicitly deferred to CV-1.16+. Under current promotion, T-ACT-KERNEL-COMP→REL is annotated as conditional on the deferred redefinition. |

**Verdict:** No active tension with canonical axioms. The latent tension at §8.5 is correctly footnoted in 10_patch_plan §1.

### §1.3 Open problems partially affected

Per prompt §8.2, partial effect on open problems must be made explicit; silent resolution is forbidden. CV-1.15 affects:

| Open problem | Pre-CV-1.15 status | CV-1.15 effect | Post-CV-1.15 status | Silent resolution risk |
|---|---|---|---|---|
| **OP-0012 (overall)** | PARTIALLY STRUCTURED (Session V, 2026-05-06). OP-0012-CC Cat B path defined. | None directly. Sub-substructure clarified. | PARTIALLY STRUCTURED + sub-substructure refined (CC: Cat B path canonical; SINK: OPEN with narrowed gap; ACTION-KERNEL: Cat B conditional). | **NONE — overall remains OPEN.** Explicit in 10_patch_plan §2. |
| **OP-0012-CC** | Cat B path defined (Session V). | None. | Same. | None. |
| **OP-0012-SINK** | (not previously registered as a labeled subproblem) | Registered as a labeled subproblem with explicit structure. Cost-level δ_eff blocker noted as "closed under action redefinition; not closed for Sinkhorn-derived $c^{\mathrm{eff}}$". | OPEN, narrowed (scaling-gap blocker stands). | **NONE.** Explicit "OPEN" tag in both theorem_status.md proposed body and hypothesis_tree.md H-COMP-SINK leaf. |
| OP-0011 (T-Temporal-Identity) | RESOLVED CV-1.12 | None. | Same. | n/a |
| OP-0008 (σ-Inherit / MERGE/SPLIT / K-jump) | OPEN | None. CV-1.15 stays within stable-K regime. | Same. | None. (Plan `00_plan.md` line 58 forbids entry into K-jump.) |
| OP-0005-DYN (Kramers rates) | OPEN (Package II) | None. CV-1.15 is zero-temperature deterministic; action smoothing $\varepsilon$ is a regularization, not a thermal $T_*$. | Same. | None. (Plan line 59 forbids H-MORSE entry.) |
| OP-0021 (canonical $T_*$ registration) | OPEN | None. | Same. | None. |
| OP-0022 (continuous-time action limit) | Not registered. | **Candidate raised** in `02_development.md` §6.3. Not registered in this session. | Candidate status. | None — explicitly a candidate, not a resolution. |
| OP-AFD-003a–e (yesterday's session) | Various — see 2026-05-12 03_integration_and_new_open.md | None. | Same. | None. (Orthogonal scope.) |

**Verdict:** Zero silent resolutions. OP-0012-SINK's narrowing is explicit and structurally documented; the residual blocker is named (scaling gap; $b_1 \odot a_2 \neq c \cdot \mathbf{1}$).

### §1.4 Commitment Notes (CN1–CN14) cross-check

| CN | Subject | CV-1.15 interaction |
|---|---|---|
| CN1 | Closure non-idempotence | Respected. CV-1.15 does not invoke idempotence; the action functional $a_i$ uses Cl(u) as a fingerprint coordinate but treats it as a function value, not an idempotent. |
| CN2 | u_t soft primitive | Respected. CV-1.15 quantities $a_i, \mathcal{A}_{i:k}, c^{\mathrm{act}}, \mathbf{K}_{i\to k}$ are all functions of u-derived $\varphi$. No object-first inversion. |
| CN3 | Volume constraint on $\Sigma_m$ | Respected. CV-1.15 paths live in $\Sigma_m \times \Sigma_m \times \dots$; volume preserved at each time. |
| CN4 | Four-term energy independence | Respected. CV-1.15 does **not** propose merging $E_{\mathrm{tr}}$ with $E_{\mathrm{cl}}$ or any other term. Action cost is a *transport-side* layer; it is parallel to $E_{\mathrm{tr}}$, not a replacement. |
| CN5 | $\Phi_{\mathrm{obs}}$ in likelihood only | Not invoked. |
| CN6 | Cat A/B/C judgment discipline | Respected. CV-1.15 patches use the Cat system; the dependency issue (Finding §2) is the audit's job to surface. |
| CN7 | Dual-mode self-referentiality (closure + distinction) | Respected. CV-1.15 uses both Cl and D as fingerprint coordinates. |
| CN8 | Soft / hard regime distinction | Respected. T-ACT-DP is hard-min; T-ACT-GIBBS is soft-min; both are clearly labeled. |
| CN9 | K_act = #PersComp (D-ST-3) | Respected. CV-1.15 does not redefine K_act. The action cost is a per-edge / per-path quantity, independent of K. |
| CN10 | No reductive claims to external frameworks | Respected. CV-1.15 cites Chapman-Kolmogorov as a *technique* and Sinkhorn as a *comparison*, never as a reductive identification. |
| CN11 | Threshold-derived structures unprincipled | Respected. CV-1.15 does not introduce new thresholds. |
| CN12 | Erratum / Retraction discipline | Respected. CV-1.15 does not retract anything. |
| CN13 | Multi-formation status separate | Respected. CV-1.15 is single-formation-or-stable-K; explicit non-overclaim. |
| CN14 | Sub-conventions for $S_n$-equivariance | Respected. CV-1.15 does not break $S_n$-equivariance. |

**Verdict:** No commitment-note tension.

### §1.5 Where new CV-1.15 entries belong in canonical (insertion map)

Under **R-C (recommended) + S-i (per-category insertion, recommended)**:

| New entry | Category | Insertion target |
|---|---|---|
| D-LOCAL-ACTION (Definition) | not a theorem | In `canonical §3` (Formal Universe), perhaps as a new §3.12, OR in §13.Y as a "Definitions" preamble. **Recommendation:** §13.Y preamble, since the definition is theorem-package-local. |
| L-ENDPOINT-NONSEMI | Cat A | End of `### Category A`, after T-PF-A1-PE (last CV-1.9 entry). |
| L-ACTION-NORMALIZATION | Cat A | Same. |
| L-FINGERPRINT-ACTION-ADMISSIBLE | Cat A | Same. |
| T-ACT-DP | Cat A | Same. |
| L-ACTION-DELTA-EFF-ZERO | Cat A | Same. |
| D-GIBBS-KERNEL (Definition) | not a theorem | Same as D-LOCAL-ACTION — §13.Y preamble or §3 extension. |
| T-ACT-GIBBS | Cat A | End of Cat A, after L-ACTION-DELTA-EFF-ZERO. |
| L-SOFTMIN-HARDMIN-BOUND | Cat A | Same. |
| L-SOFT-ACTION-DELTA-EFF-ZERO | Cat A | Same. |
| P-ACTION-PATH-INHERITANCE | Interpretation | Either at the end of Cat A as "P-" prefixed Proposition (interpretive), OR in a new "Definition Justifications" subsection in §13. The 09_final_audit defers this counting decision; I recommend "Interpretation, not counted in A/B/C/R tally" and place at the end of §13.Y or in a new §13.Z "Interpretive Propositions". |
| T-ACT-KERNEL-COMP→REL | Cat B (conditional under R-C; Cat B unconditional under R-A) | End of `### Category B`. |
| T-SINKHORN-PLAN-SEMIGROUP-FAILS | OPEN (proved failure) | Not in §13 (the §13 categories are A/B/C/Retracted). Either in `§12. Open Problems and Next Formalization Layers` as a "proved failure" entry, OR in a new "Warning" subsection at the §13 end. **Recommendation:** §12 entry, mirroring OP-0012-SINK. |
| P-SINKHORN-STABILITY-CONDITIONAL | Cat B | End of `### Category B`. |
| OP-0012-SINK | OPEN (labeled open problem) | `theorem_status.md` Open Problems Catalog after OP-0012 entry (line 771). |

**Recommendation:** the 10_patch_plan §1 single-block style be re-organized to match this insertion map. This is the substantive form of Finding §3 (style mismatch) resolution.

---

## §2. Proposed amendments to canonical (proposal only — no edits)

Per prompt §8.1, only proposals — no writes.

### §2.1 canonical.md amendments (proposed)

```
[PROPOSED INSERT AT END OF "### Category A" — between T-PF-A1-PE and "### Category B"]

#### CV-1.15 Action-Based Temporal Succession Lemmas and Theorems (proposed insertion)

> (기호 주의) In the CV-1.15 entries below, $\mathbf{K}_{i\to k}$ (boldface, matrix)
> denotes the action-derived Gibbs transition kernel; $K$ (italic, scalar) elsewhere
> in canonical denotes the formation count. $\varepsilon$ here denotes the action
> smoothing temperature; $\varepsilon_{\mathrm{OT}}$ in §8.5 / T-Temporal-Identity
> denotes the Sinkhorn entropic regularization, a separate parameter.
>
> (Refinement framing) The action cost defined here is a composition-compatible
> refinement of temporal cost structures; it does not replace T-Temporal-Identity
> (§13 Cat A; based on score matrix $S^0_{ij}$ derived from $c[u_t, u_s]$ of §8.5).

**Definition D-LOCAL-ACTION.** Conditions: $\gamma_\varphi \geq 0$, $\Delta t_i > 0$,
$\varphi_i : X_i \to \mathbb{R}^3$ Lipschitz. ...

[L-ENDPOINT-NONSEMI, L-ACTION-NORMALIZATION, L-FINGERPRINT-ACTION-ADMISSIBLE,
 T-ACT-DP, L-ACTION-DELTA-EFF-ZERO, D-GIBBS-KERNEL, T-ACT-GIBBS,
 L-SOFTMIN-HARDMIN-BOUND, L-SOFT-ACTION-DELTA-EFF-ZERO,
 P-ACTION-PATH-INHERITANCE (Interpretation)]

[PROPOSED INSERT AT END OF "### Category B" — after T-Temporal-Identity body]

(Note: the Category B section header should be updated to add
"; T-Temporal-Identity promoted to Cat A W7-CV1.13 2026-05-10 (CV-1.13)"
to record the prior promotion that was not propagated to the header.)

**Theorem T-ACT-KERNEL-COMP→REL.** Cat B (conditional on CV-1.14 T-CC-StableK-Kernel
canonical promotion; currently working-candidate). ...

**Proposition P-SINKHORN-STABILITY-CONDITIONAL.** Cat B (conditional on
H-SINK + MARGIN + SMALL-SINK-GAP). ...

[PROPOSED INSERT AT END OF "## 12. Open Problems and Next Formalization Layers"]

**T-SINKHORN-PLAN-SEMIGROUP-FAILS (Warning).** Proved failure:
$M^{\mathrm{sink}}(\mathbf{K}_{ts}) \cdot M^{\mathrm{sink}}(\mathbf{K}_{sr})
\neq M^{\mathrm{sink}}(\mathbf{K}_{tr})$ generically.
See OP-0012-SINK.
```

### §2.2 theorem_status.md amendments (proposed)

```
[PROPOSED ROWS APPENDED TO Cat A section, after T-PF-A1-PE row]

| ID | Statement | Status | Cat | Notes |
|---|---|---|---|---|
| L-ENDPOINT-NONSEMI | ... | Cat A (CV-1.15, 2026-05-13) | A | counterexample 1D |
| L-ACTION-NORMALIZATION | ... | Cat A | A | uniform-speed only |
| L-FINGERPRINT-ACTION-ADMISSIBLE | ... | Cat A | A | conditions: φ_i Lipschitz, Δt_i > 0 |
| T-ACT-DP | ... | Cat A | A | finite site, additive A |
| L-ACTION-DELTA-EFF-ZERO | ... | Cat A | A | under c^direct := c^act redefinition |
| T-ACT-GIBBS | ... | Cat A | A | finite site, ε > 0 |
| L-SOFTMIN-HARDMIN-BOUND | ... | Cat A | A | N finite, ε > 0 |
| L-SOFT-ACTION-DELTA-EFF-ZERO | ... | Cat A | A | T-ACT-GIBBS corollary |

[PROPOSED ROW APPENDED TO Cat B section]

| T-ACT-KERNEL-COMP→REL | ... | Cat B (conditional, CV-1.15) | B | (GK)+(stable-K)+(margin); (GK) requires CV-1.14 T-CC-StableK-Kernel promotion |
| P-SINKHORN-STABILITY-CONDITIONAL | ... | Cat B | B | H-SINK+MARGIN+SMALL-SINK-GAP |

[PROPOSED AMENDMENT TO OP-0012 entry at lines 517 + 771–793]

OP-0012 (Persistence Composition): PARTIALLY STRUCTURED, sub-structure refined CV-1.15.
  - OP-0012-CC: Cat B (Lemma 6, 2026-05-07)
  - OP-0012-SINK: OPEN (new sub-label CV-1.15). Cost-level δ_eff blocker closed under
    action redefinition (L-ACTION-DELTA-EFF-ZERO Cat A); plan-level scaling-gap blocker
    OPEN. Required: L-δ_eff-SINK (Cat C target), L-Eff-Sinkhorn (Cat C target).
  - K-jump general: Cat C, dependency on OP-0008, OP-0021.

[PROPOSED CLAIM COUNT UPDATE — header line in theorem_status.md]

Current: "CV-1.13 — 59A / 14B / 5C / 5R = 83 claims"
Target under R-C: "CV-1.15 — 67A / 16B / 5C / 5R = 93 claims (P-ACTION-PATH-INHERITANCE
                  counted as Interpretation row, not in 93 tally)"
```

### §2.3 hypothesis_tree.md amendments (proposed)

```
[NEW BRANCH UNDER Q5 — temporal identity, currently HT-3.5]

## H-COMP — Temporal Correspondence Composition (OP-0012)

### H-COMP-CC (CV-1.12, Cat B closed)
- OP-0012-CC: under stable-K + margin, R_{t→r} = R_{s→r} ∘ R_{t→s}.

### H-COMP-ACTION (CV-1.15, 2026-05-13) [NEW]
- L-ENDPOINT-NONSEMI: endpoint² 합성 불가 (Cat A)
- T-ACT-DP: hard-min Bellman DP (Cat A)
- T-ACT-GIBBS: Gibbs kernel semigroup K_{i→k}=K_{i→j}K_{j→k} (Cat A)
- T-ACT-KERNEL-COMP→REL: (GK)+(stable-K)+(margin) → R composition (Cat B conditional)

### H-COMP-SINK (OP-0012-SINK, OPEN) [NEW]
- T-SINKHORN-PLAN-SEMIGROUP-FAILS: scaling-gap obstruction (proved failure)
- CV-1.15: cost-level δ_eff blocker closed under action redefinition; scaling-gap
  blocker remains.
- Required lemmas: L-δ_eff-SINK (Cat C target), L-Eff-Sinkhorn (Cat C target).

[VERSION INCREMENT]

HT-3.5 → HT-3.6. CV-1.15 H-COMP branch added. T-Temporal-Identity Cat A status
unchanged.
```

### §2.4 CHANGELOG.md amendment (proposed)

```
[PROPOSED INSERT AT TOP OF FILE, ABOVE THE CV-1.13 SEAL ENTRY]

## [CV-1.15] 2026-05-13 — Action-Based Temporal Succession Package

**Trigger:** CV-1.15 working-package completion 2026-05-12 + exp89 3-case PASS 2026-05-13 + audit pass (THEORY/logs/daily/2026-05-13/02_development.md).

### Added — Cat A (Eight Lemmas/Theorems)
- L-ENDPOINT-NONSEMI: endpoint² 합성 불가 반례 (1D)
- L-ACTION-NORMALIZATION: 등속 경로 시간 정규화 cost additive
- L-FINGERPRINT-ACTION-ADMISSIBLE: SCC fingerprint action DP/Gibbs 전제 충족
- T-ACT-DP: hard-min action cost Bellman DP
- L-ACTION-DELTA-EFF-ZERO: δ_eff = 0 (action direct cost 재정의)
- T-ACT-GIBBS: Gibbs kernel semigroup (Chapman-Kolmogorov)
- L-SOFTMIN-HARDMIN-BOUND: soft/hard-min 오차 bound
- L-SOFT-ACTION-DELTA-EFF-ZERO: soft δ_eff^ε = 0

### Added — Cat B Conditional (Two)
- T-ACT-KERNEL-COMP→REL: (GK)+(stable-K)+(margin) → R composition (조건: CV-1.14
  T-CC-StableK-Kernel canonical 승급)
- P-SINKHORN-STABILITY-CONDITIONAL: H-SINK+MARGIN+SMALL-SINK-GAP 조건부

### Added — Interpretation (Not in Claim Count)
- P-ACTION-PATH-INHERITANCE: action cost = path inheritance interpretation

### OPEN — preserved / structured
- T-SINKHORN-PLAN-SEMIGROUP-FAILS: scaling-gap obstruction (proved failure)
- OP-0012-SINK: Sinkhorn scaling-gap blocker (new sub-label; cost-level blocker
  closed under action redefinition)

### Claim count
- CV-1.13 baseline: 59A / 14B / 5C / 5R = 83 claims
- CV-1.15 delta: +8A, +2B
- New: 67A / 16B / 5C / 5R = 93 claims (P-ACTION-PATH-INHERITANCE as Interpretation
  row, not counted)

### Files
- THEORY/working/CV115_ACTION_TEMPORAL_COST/ (00–10, ten working files completed 2026-05-12)
- CODE/experiments/exp89_endpoint_vs_action_temporal_cost.py + exp89_results.json
  (3-case PASS, numerical sanity check only — not proof)
- THEORY/logs/daily/2026-05-13/01_exploration.md, 02_development.md,
  03_integration_and_new_open.md, 99_summary.md (pre-promotion audit + post-audit dry-run)

### Audit findings applied
- Symbol clarity: $\mathbf{K}_{i\to k}$ vs $K$, $\varepsilon$ vs $\varepsilon_{\mathrm{OT}}$
- Refinement framing: action cost is composition-compatible refinement of temporal cost,
  not replacement of T-Temporal-Identity
- δ_eff scope: closed only under action direct cost redefinition; Sinkhorn case OPEN
- exp89 framing: numerical validation only, not proof

### Did NOT close
- OP-0012 overall (still PARTIALLY STRUCTURED)
- OP-0012-SINK (OPEN, structure refined)
- OP-0008, OP-0021 (untouched)
- Sinkhorn-scaled plan semigroup (proved failure stands)
- canonical §8.5 M_{t→s} redefinition (deferred CV-1.16+)
```

### §2.5 What is *not* changed in canonical (explicit no-edit zones)

To prevent silent contamination, the following canonical regions are explicitly out of scope of CV-1.15:

- §0 Summation Convention
- §1 Status Note (except for the Cat A/B claim count header line, which is mechanically updated)
- §2 Foundational Orientation
- §3 Formal Universe and Primitive Structure (no new D-ST entries; D-LOCAL-ACTION / D-GIBBS-KERNEL live in §13.Y, not §3)
- §4 Why the Soft Form Is Primary
- §5 Derived Geometric and Morphological Notions
- §6 Axiomatic Groups
- §7 Proto-Cohesion and Pre-Objective Cohesion
- §8.0–§8.4 Energy term subsections (only the §8.5 cross-reference in CV-1.15 patch header is *cited*, not edited)
- §8.5 Transport Term (no $\mathbf{M}_{t \to s}$ redefinition; deferred CV-1.16+)
- §8.6–§8.7
- §9 Provisional Concrete Operator Forms
- §10 Structural Interpretation
- §11 Fixed Commitments
- §14 Commitment Notes (CN1–CN14)
- §15 Closing Summary
- §16 Stereo Extension
- Appendix OMS

---

## §3. Where this work could fit if CV-1.14 is also promoted (R-A scenario, sketch only)

R-A is **not** the recommended path of this session, but we sketch the integration shape for completeness so the user can choose informed.

### §3.1 Pre-CV-1.15 prerequisite: CV-1.14 T-CC-StableK-Kernel insert

Per `THEORY/working/CV114_TEMPORAL_COMPOSITION/05_promotion_draft.md` §2:

```
Insert into canonical §13 Cat B (after T-K-Select-OBS):

T-CC-StableK-Kernel. Cat B (CV-1.14 candidate). [body from working/CV114 §2 lines 44–93]

theorem_status.md:
  Add Cat B row: "T-CC-StableK-Kernel | Compositional Consistency under stable-K + margin,
  M_{t→r} := M_{s→r}∘M_{t→s} | Cat B (Lemma 6) | margin Δ_sep > 0 |"
  Amend OP-0012 entry to add Sub-case A (Cat B closed) — Sub-case B (OPEN-SINK)
  — Sub-case C (OPEN-Kjump) — Sub-case D (OPEN-Markov).

hypothesis_tree.md:
  Add H-COMP-KERNEL node under H-COMP.

CHANGELOG.md:
  Add CV-1.14 entry below the CV-1.15 entry.

Count: 83 → 84.
```

### §3.2 Then CV-1.15 insert with R-A reading

Same as §2.1–§2.4 above, but with:

- T-ACT-KERNEL-COMP→REL annotation simplified: "*depends on T-CC-StableK-Kernel (canonical §13 Cat B)*" — no "conditional on CV-1.14 promotion" caveat.
- H-COMP-KERNEL pre-exists (from CV-1.14); H-COMP-ACTION + H-COMP-SINK get added as sibling branches.
- Total count: 84 → 94 (P-ACTION-PATH-INHERITANCE as Interpretation row, not counted in 94).

### §3.3 R-A risk: CV-1.14 audit parity

If R-A is chosen, the CV-1.14 working layer should receive an audit pass equivalent to 09_final_audit. That audit was not produced (the CV-1.14 directory has 03_gap_audit.md but no 09-style READY-FOR-USER-APPROVAL judgment). **Recommendation if R-A:** insert a CV-1.14 audit session before R-A apply.

---

## §4. New Open Questions (raised by this session)

Per prompt §4.6, list open questions raised but not answered. Each is 3–5 lines, candidate for next session's plan target.

### §4.1 OQ-2026-05-13-A — CV-1.14 promotion audit parity

T-CC-StableK-Kernel CV-1.14 promotion draft (`working/CV114/05_promotion_draft.md`) contains a complete Cat B proof and proposal draft for canonical insert, but lacks a 09-style READY-FOR-USER-APPROVAL audit at the same rigor as CV-1.15's 09_final_audit. Before R-A or any co-promotion path, this audit should be performed. Estimated 1–2 sessions. Output: `CV114/09_final_audit.md` parallel.

### §4.2 OQ-2026-05-13-B — L-δ_eff-SINK Cat C lemma attempt

OP-0012-SINK's remaining blocker after CV-1.15 narrowing is the Sinkhorn-scaling gap. The first proof attempt should be L-δ_eff-SINK: a quantitative bound on
$\delta_{\mathrm{eff}}^{\mathrm{sink}} := \|c_{\mathrm{direct}}(u_t, u_r) - c^{\mathrm{eff}}(M^{\mathrm{sink}}_{t\to s}, M^{\mathrm{sink}}_{s\to r})\|_\infty$
in terms of marginals, $\varepsilon_{\mathrm{OT}}$, and the structural separation $\Delta_{\mathrm{sep}}$. Estimated 2–4 sessions. Output: `working/CV115/.../L-delta-eff-SINK.md` Cat C draft.

### §4.3 OQ-2026-05-13-C — Continuous-time action limit (OP-0022 candidate)

Whether the discrete-time action functional $\mathcal{A}_{i:k}(P)$ Γ-converges to a continuous-time SCC action functional as the temporal discretization refines. Open: framework choice (Γ-convergence vs viscosity vs $\Gamma$-Mosco), compactness of bounded-action paths on $\Sigma_m$, coercivity of the limit. Estimated 3–5 sessions of foundational work before a first Cat C statement. Output: working/CV116_CONTINUOUS_ACTION/ directory.

### §4.4 OQ-2026-05-13-D — §8.5 $M_{t \to s}$ canonical redefinition decision

CV-1.15's T-ACT-KERNEL-COMP→REL Cat B status depends on whether canonical §8.5 redefines $M_{t \to s} := \mathbf{K}_{t \to s}$ (the action-derived Gibbs kernel). Currently deferred to CV-1.16. The decision is: (D1) yes — redefine, sacrificing the OT-derived transport plan for the action-derived one; (D2) no — keep $M$ as Sinkhorn partial-OT, treat $\mathbf{K}$ as a separate kernel layer; (D3) hybrid — $M$ remains $M^{\mathrm{sink}}$, but a *new* canonical kernel symbol $\mathbf{K}_{t \to s}$ enters at §8.5 with explicit interaction rules. Each has consequences for T-Temporal-Identity (D1 changes the score matrix; D2/D3 preserve it). Estimated 1 session for the decision + 1–2 sessions for the patch.

### §4.5 OQ-2026-05-13-E — Categorization of P-ACTION-PATH-INHERITANCE

P-ACTION-PATH-INHERITANCE is currently labeled "Interpretation, not counted." But what is the canonical convention for Interpretation-class statements? Are they:
- (E1) excluded from the A/B/C/R tally but tracked in a separate "Interpretations" register?
- (E2) included in a generalized "all canonical statements" tally?
- (E3) marked only inline in canonical text without theorem_status registration?

`canonical §13` does not currently have an Interpretation category. CV-1.5.1 D-6a Multi-Static added "3 Cat A definitional entries grounding Commitment 14-Multi" — so the precedent is to fold *definitional* entries into Cat A. P-ACTION-PATH-INHERITANCE is *interpretive*, not definitional. A small canonical convention decision is needed. Estimated 0.5 session.

### §4.6 OQ-2026-05-13-F — Style-mismatch (Finding §3) resolution as a meta-convention

The audit found that 10_patch_plan §1 uses a "single-block per CV-version" style at the §13 end, but canonical practice (CV-1.6 through CV-1.13) uses per-category insertion. This is a meta-convention question: should canonical §13 evolve toward CV-versioned subsections (cleaner version provenance, harder per-category navigation) or stay per-category (easier navigation, slightly murkier provenance)? `00_plan.md` does not specify. Each subsequent CV-X.Y patch session will face this decision unless a meta-convention is established. Estimated 0.5 session.

### §4.7 OQ-2026-05-13-G — Pre-existing Cat B header staleness (Finding §2.4)

A pre-existing inconsistency: `canonical §13 Cat B section header` (line 1688) does not record T-Temporal-Identity's CV-1.13 promotion to Cat A, though it records T-OP6-B, T-PF-A1-GI, T-PF-A1-PE promotions. This is hygiene, not theory. Cleanup costs 1 line edit. Estimated 0.1 session, can be folded into any CV-1.15 promotion session that touches the Cat B header.

---

## §5. Prompt-improvement suggestions (§14 of prompt)

Per prompt §14, record observations on the reusable template.

### §5.1 What worked

- The "multi-approach + primary selection" structure (§4.2 of prompt) was usable for *workflow* selection, not only proof strategy. The plan author's open-ended phrasing of "approach" survives this generalization.
- The hard prohibitions list (§8.1–§8.10) caught the canonical-no-write boundary cleanly.
- §10 self-checklist was useful — it forced explicit inclusion of multi-approach + primary selection even when the task was 80% audit (not novel proof).

### §5.2 What was awkward

- **Mismatch between today's task (audit) and the template's prooffulness:** the template is heavily oriented toward "prove an open problem" tasks. Today's task was "audit a promotion." Sections §4.2 (multi-approach) and §4.4 (proof development) had to be reinterpreted as "workflow paths" and "audit findings", respectively. This stretched the template but did not break it. A small addition to the template might help: e.g. a one-line note in §4 that "approach" can be a workflow or audit strategy when the day's target is non-proof.
- The template's §13 stopping criteria ("Primary 접근이 완결된 형태의 proof 또는 counterexample에 도달") does not naturally apply to audit work. For audit days, a more natural stop criterion is "all blocking findings raised + all advisory findings raised + readiness verdict delivered". Minor adjustment.
- The template requires three core files (`01_`, `02_`, `03_`). For audit-heavy days, the natural deliverables are `02_` (substantive audit) and `99_summary.md` (readiness report). `01_exploration.md` is somewhat redundant in audit mode. We complied with the template anyway, but a future template version could allow "audit-mode" with reduced file requirements.

### §5.3 Concrete additions (suggested for prompt v2)

Add to §4 of prompt body:

> *Audit-mode variant: If today's target is a promotion application or consistency audit (rather than a novel proof), §4.2 "multi-approach" may be reinterpreted as "workflow strategies" (e.g., audit-only / patch-amend / co-promote / demote). §4.4 "primary approach development" then becomes the audit body. §13 stopping criterion becomes "all findings raised + readiness verdict delivered."*

Add to §8 of prompt body (forbidden patterns):

> *11. When promoting CV-X.Y, audit cross-references to prior CV-X.(Y-1) or CV-X.(Y-2) candidates: verify each cited prior theorem is canonical *as of patch application time*, not "candidate in working/". Silent assumption of un-promoted CV is a recurring failure mode (caught in CV-1.15 audit, 2026-05-13).*

Add to §12 (anticipated error patterns):

> *7. Cross-CV dependency drift: a CV-X.Y patch that cites "CV-X.(Y-1) lemma" without verifying that CV-X.(Y-1) is canonically promoted. This was observed in CV-1.15's reference to CV-1.14 T-CC-StableK-Kernel (which was working, not canonical).*

---

## §6. Outputs of this session (delivery summary)

This session produced four files in `THEORY/logs/daily/2026-05-13/`:

| File | Content |
|---|---|
| `01_exploration.md` | Restatement (§4.1), three workflow approaches P1/P2/P3 + two rejected P4/P5 (§4.2), primary selection P3 with P1/P2 preserved as fallbacks (§4.3). |
| `02_development.md` | Block A pre-approval audit (8 checks, 10 findings, all LOW–MEDIUM, none blocking — §1); CV-1.14 dependency finding with three resolution paths (§2); style-mismatch finding with three resolution options (§3); Block D dry-run on canonical-as-is, audit script for post-patch state (§4); Block E exp89 verification (PASS, §5); Block F OP-0012-SINK structural notes (§6); Block G readiness report (§7); self-classification of findings (§8). |
| `03_integration_and_new_open.md` (this file) | Integration map (§1), proposed canonical/theorem_status/hypothesis_tree/CHANGELOG amendments without canonical write (§2), R-A path sketch (§3), seven new open questions OQ-A through OQ-G (§4), prompt-improvement suggestions (§5). |
| `99_summary.md` | 3–5 sentence summary + tomorrow seed. |

No canonical files were modified. No working files were modified (this session's outputs are pure log/daily entries).

---

*End of 03_integration_and_new_open.md. Next file: `99_summary.md`.*
