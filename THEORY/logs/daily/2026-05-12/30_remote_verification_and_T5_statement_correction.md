---
type: log/followup-correction
date: 2026-05-12
target: Reconcile remote-ultraplan session findings with this-session logs
canonical_version: CV-1.13 (read-only)
session_label: W7-Day3 (post-remote-ultraplan reconciliation pass)
status: verification + framing correction
remote_session_ref: https://claude.ai/code/session_01R5piPpBpftqvKNNDGD91T1
---

# 30 — Remote-ultraplan Verification and AFD-T5 Statement Framing Correction

**Session:** 2026-05-12 (third pass: reconciling this-session output with a parallel remote-ultraplan investigation)

**Why this file exists.** A separate remote-ultraplan agent ran in parallel on the AFD-T5 R1 question and produced two files (`op_afd_003_brainstorm.md`, `t5_r1_promotion_decision.md`) destined for `THEORY/working/AFD_0/` via PR. The remote agent's headline finding — that **AFD-T5's statement does not actually claim infimum attainment** — directly contradicts framing language in this session's `02_development.md`, `02b_L3_tightening_and_op003c.md`, `03_integration_and_new_open.md`, and `99_summary.md`. This file verifies the remote finding against the source and corrects the framing here.

---

## §1. Verification of the remote claim

### 1.1 What the remote agent claimed

> "AFD-T5's *statement* never claims attainment — only the properties bullet does. R1 promotion can therefore be unblocked **today** via a 5-line documentation edit that splits attainment out as a separate Cat B candidate (T5-Strong). The `2 K_field` constant in T5 step (d) similarly weakens cleanly to 'finite', which is all the proof actually needs."

### 1.2 Direct check against `THEORY/working/AFD_0/abstract_formation_dynamics.md`

The AFD-T5 block runs from line 376 to line 401. Three load-bearing fragments:

**(F-1) Statement, line 380:**

> "For any F_i, F_j ∈ V_form with Adm(F_i, F_j) ≠ ∅, `C_AFD(F_i, F_j) ∈ [0, +∞)` is well-defined in the minimal version (λ_D = λ_K = 0). For λ_D, λ_K > 0 and rectifiable γ, `J_AFD(γ; F_i) < +∞`."

**Verbatim parsing:** This is a **finiteness** claim, not an **attainment** claim. It asserts that the infimum is finite and the cost functional is well-defined; it does *not* assert that the infimum is achieved by some admissible γ_*.

**(F-2) Proof steps (a)–(f), lines 384–394:** All six steps prove finiteness. No step constructs or asserts existence of a minimizer. Step (a) uses extreme-value theorem on `E` (E attains its max on Σ_m — *that's* attainment, but of E on Σ_m, not of `Bar` over Adm). Step (b) uses non-emptiness of Adm to assert `inf` is in `[0, +∞)`, which only requires that *some* admissible path has finite `Bar`, again unrelated to minimizer existence.

**(F-3) Properties bullet, line 401:**

> "**Infimum attainment** is OPEN (OP-AFD-003); compactness of Σ_m + continuity of E suggests it is attainable via Arzelà-Ascoli on rectifiable curves of bounded length, but for the minimal version (λ_D = λ_K = 0) and continuous (non-rectifiable) admissible class the attainment is non-trivial."

**Verbatim parsing:** Attainment is listed as a property of the theorem, but the property is itself **flagged OPEN** with explicit reference to OP-AFD-003. The properties bullet is a *commentary* on what AFD-T5 does *not* say.

### 1.3 Verification verdict

**Remote agent is correct.** The current `abstract_formation_dynamics.md` makes a clean separation:

- **AFD-T5 (the theorem):** finiteness of `C_AFD` ∈ [0, +∞). Provable Cat A unconditional from continuity + compactness + AFD-T2 + Commitment 16 (no o-minimal, no Lemma L3).
- **Attainment of `inf`:** separate proposition, currently OPEN (OP-AFD-003). What this session's `02_development.md` actually proved is *this* proposition — the **stronger** claim — under Claim B.3.

This-session output described the result as "closing AFD-T5's last gap." That description is **partially incorrect**:

- The gap closed by `02_development.md` T-OP-AFD-003-A is **not** part of AFD-T5's statement.
- It is part of AFD-T5's *commentary* (Property bullet), and a separate OP (OP-AFD-003).
- The correct claim is: "AFD-T5 remains as-is, **and** a separate new theorem (call it **AFD-T5-Strong** or **AFD-T11**) about attainment is now proved Cat A modulo Claim B.3."

### 1.4 The `2 K_field` constant remark

Remote also noted that line 390's bound `J_K(γ) ≤ 2 K_field` is *stronger* than the proof requires. Re-reading step (d):

> "K_act takes only finitely many integer values; `J_K(γ) = TV(K_act ∘ γ) ≤ 2 K_field` for any γ of bounded total variation (since each level can be entered/exited a bounded number of times along a finite-length curve in the semi-algebraic setting; for the formal statement see OP-AFD-002)."

**Analysis.** The "`≤ 2 K_field`" claim relies on a semi-algebraic-finite-crossings argument that is itself flagged "see OP-AFD-002". For step (e) — "thus `J_AFD < ∞`" — all that is needed is `J_K(γ) < ∞`. The "`finite, see OP-AFD-002`" version achieves this without committing to the `2 K_field` constant. **Remote's observation is accurate**: weakening "`≤ 2 K_field`" to "`< ∞ (semi-algebraic crossings, see OP-AFD-002)`" preserves AFD-T5's proof and removes one citation dependency.

---

## §2. Correction of this-session framing

The following statements in this session's logs are **misleading** in light of §1:

### 2.1 In `99_summary.md`

(Pre-correction:) "AFD-T5 (Cost Existence) — last open property 'infimum attainment' CLOSED modulo Claim B.3."

**Corrected:** AFD-T5 statement (finiteness) is **already Cat A unconditional** — no work this session needed. What was proved today is a **separate, stronger** proposition: **T5-Strong** (= AFD-T11 candidate = T-OP-AFD-003-A), namely "the infimum is **attained** by some Lipschitz γ_*". This is **Cat A modulo Claim B.3**, and it can be promoted alongside AFD-T5 *or* deferred — they are now decoupled.

### 2.2 In `02_development.md` §11.1

(Pre-correction:) "AFD-T5 (Abstract Transition Cost Existence; abstract_formation_dynamics.md §14) currently states ... 'Infimum attainment is OPEN (OP-AFD-003); ...'"

**Corrected:** This quote is from the **properties commentary** of AFD-T5, not from the theorem statement. The theorem statement (line 380) asserts finiteness only. The properties commentary should be updated to:

> "**Infimum attainment.** Separately proved (Cat A modulo Claim B.3) as **T5-Strong** (= AFD-T11 candidate) in `logs/daily/2026-05-12/02_development.md` §5. AFD-T5 itself remains the finiteness statement."

### 2.3 In `03_integration_and_new_open.md` §1.3

(Pre-correction:) "§14 AFD-T5 'Properties' bullet ('**Infimum attainment** is OPEN (OP-AFD-003)...'): **replace** with: '**Infimum attainment.** **PROVED (Cat A, 2026-05-12).** ...'"

**Corrected:** The replacement is *correct in content*, but should be framed not as "updating AFD-T5" but as "adding T5-Strong (= AFD-T11) as a new adjacent theorem". The Properties bullet of AFD-T5 should then *reference* T5-Strong rather than claim AFD-T5 itself now includes attainment.

### 2.4 In `02b_L3_tightening_and_op003c.md` §H

(Pre-correction:) "Audit-corrected headline: 'OP-AFD-003 RESOLVED Cat A modulo Claim B.3 ...'"

**No correction needed for OP-AFD-003 itself** — that OP *is* about attainment, and the audit-corrected headline is accurate. The correction is upstream: AFD-T5 and OP-AFD-003 were partially conflated in `02_development.md` §11.1's wording.

### 2.5 In `99_summary.md` "Effect on AFD-0 promotion roadmap"

(Pre-correction:) "AFD-T5 — conditionally ready (today's OP-AFD-003 resolution closes the last gap modulo Claim B.3; verify Claim B.3 before promoting at unconditional Cat A)."

**Corrected:**

- AFD-T5 (finiteness): **already ready at Cat A unconditional**. No Claim B.3 dependency. Can promote today.
- **T5-Strong** (= AFD-T11 candidate, attainment): **Cat A modulo Claim B.3**. Can be promoted alongside AFD-T5 *with* an explicit "modulo o-minimal sublevel-set continuity" qualifier, or held for a follow-up after Claim B.3 verification.

The R1 promotion package therefore splits cleanly:

- **R1-Weak (immediate):** AFD-T5 (finiteness), AFD-T9, AFD-D1..D5, AFD-T1, AFD-T6. **Cat A unconditional.** No Claim B.3 dependency.
- **R1-Strong (immediate, with qualifier):** add AFD-T11 = T5-Strong (attainment). Cat A modulo Claim B.3.
- **R1-Full (after Claim B.3 verification):** AFD-T11 promoted Cat A unconditional.

---

## §3. Track A (5-line documentation edit) viability check

Remote claims R1 promotion can be unblocked today via a 5-line edit to `abstract_formation_dynamics.md`. Concrete check:

### 3.1 Current text (line 401, single bullet)

```
- **Infimum attainment** is OPEN (OP-AFD-003); compactness of Σ_m + continuity of E suggests it is attainable via Arzelà-Ascoli on rectifiable curves of bounded length, but for the minimal version (λ_D = λ_K = 0) and continuous (non-rectifiable) admissible class the attainment is non-trivial.
```

### 3.2 Proposed minimal edit (5 lines)

```
- **Infimum attainment.** **PROVED (Cat A modulo Claim B.3, 2026-05-12)** as a
  separate theorem **T5-Strong** (registered as **AFD-T11 candidate**); see
  `logs/daily/2026-05-12/02_development.md` §5 and `02b_L3_tightening_and_op003c.md`
  §B for the o-minimal-sublevel-set lemma. AFD-T5 itself remains the finiteness
  statement; T5-Strong is the adjacent attainment result.
```

### 3.3 Additional edit (line 390, weakening "2 K_field" to "finite")

```
- **J_K(γ) < ∞** by Commitment 16 (semi-algebraic-finite-crossings argument;
  precise enumeration is OP-AFD-002).
```

Five replaced lines total. This is exactly what Remote characterized as the "5-line documentation edit" that unblocks AFD-T5 R1 promotion at Cat A unconditional, decoupled from Claim B.3.

### 3.4 Whether to actually do this edit

**Caveat from SCC prompt §8.1:** "canonical 직접 수정 금지. THEORY/canonical/*.md 에 쓰기 금지." `THEORY/working/AFD_0/abstract_formation_dynamics.md` is **working layer, not canonical**, so the prohibition does not strictly apply. However, the more general prompt language (§2 of this prompt template) says: "당신의 모든 출력은 THEORY/logs/daily/2026-05-12/ 디렉토리 내부에만 씁니다. working/ 과 canonical/ 에는 직접 쓰지 않습니다. 승급은 사용자가 별도 단계에서 수행."

So **even though the working layer is technically not canonical, this session is instructed to write only to logs/daily/.** Therefore Track A's edit must be **proposed**, not executed, by this agent. The Remote agent (in a separate session, presumably with different instructions) wrote to `working/AFD_0/`; this session does not.

**Action.** Record the proposed 5-line edit in this file as a deliverable for the user / next promotion session. Do not execute.

---

## §4. Consolidated post-verification picture

After reconciling Remote's findings with this-session's output, the honest status of the AFD-T5 R1 question is:

### 4.1 Three-claim split

| Claim | Status | Promotion-readiness |
|---|---|---|
| **AFD-T5** (finiteness of C_AFD) | Cat A unconditional (already, no work needed) | **Ready R1 immediately**, no dependencies |
| **T5-Strong** = AFD-T11 candidate (attainment of inf) | Cat A modulo Claim B.3 | Ready R1 with qualifier; or hold for Claim B.3 verification (1 session) |
| **OP-AFD-003** (the OP about attainment) | RESOLVED (when T5-Strong promoted) | Triggers on T5-Strong promotion |

### 4.2 What this session's logs *did* prove (re-attributed)

| File | Original framing | Corrected framing |
|---|---|---|
| `02_development.md` §5 (T-OP-AFD-003-A) | Closing AFD-T5's attainment gap | Proving the **new** theorem T5-Strong / AFD-T11 |
| `02_development.md` §6 (T-OP-AFD-003-B) | Parallel attainment proof | Parallel proof of T5-Strong |
| `02_development.md` §7 (T-OP-AFD-003-C) | Extension to (λ_D, λ_K) | T5-Strong with weighted cost |
| `02b` §C (T-OP-AFD-003-C-soft) | K_soft variant Cat A | T5-Strong-soft Cat A unconditional |
| Audit `02b` §B (Claim B.3) | AFD-T5 modulo B.3 | T5-Strong modulo B.3 (AFD-T5 itself unaffected) |

### 4.3 Two new commitments after reconciliation

(N-1) **AFD-T5 stays a finiteness theorem.** R1 promotion of AFD-T5 = R1 promotion of finiteness only. Clean Cat A. No o-minimal dependency in the promoted theorem; only in the *adjacent* T5-Strong.

(N-2) **AFD-T11 (= T5-Strong, attainment) becomes the natural new entry.** This was already foreshadowed in `03_integration_and_new_open.md` §1.4 as an "optional new AFD theorem registry entry" — and Remote's framing elevates "optional" to "primary, this is the actual new theorem". The recommendation `03_integration_and_new_open.md` §1.4 made — *"absorb into AFD-T5"* — should be **reversed**: register AFD-T11 as a **separate** theorem, since it is genuinely an independent claim with different proof dependencies.

### 4.4 Why this matters

The pre-correction framing implied that AFD-T5 R1 promotion was **gated** on Claim B.3 verification. The post-correction framing shows AFD-T5 R1 is **not gated** on Claim B.3; only AFD-T11 (T5-Strong) is. This **unblocks** the AFD-R1 promotion package:

- Promote AFD-T5 + T9 + T1 + T6 + D1..D5 **today** (Cat A unconditional). 
- AFD-T11 promotion is a **separate decision** with its own timing (immediate-with-qualifier or wait-for-B.3).

**Net effect.** AFD-T5 R1 was always promotion-ready in its current form; this-session's logs over-stated the gap-closing significance. The genuine new result is AFD-T11.

---

## §5. Updates to the new-OP list

Based on §1–§4 reconciliation, the new-OP list from `03_integration_and_new_open.md` §5 / `02b` §F is **further refined**:

| ID | Severity | Statement | Net change |
|---|---|---|---|
| (none) | — | AFD-T5 (finiteness) | **No OP; already Cat A unconditional**. Documentation edit only. |
| **AFD-T11-Promotion-Decision** | M | Decide whether T5-Strong (= AFD-T11) is promoted with B.3 qualifier (immediate) or held for B.3 verification | New decision point arising from §4 split |
| OP-AFD-003a-revised | M | Claim B.3 uniform o-minimal diameter | unchanged |
| OP-AFD-003b | L | Drop A3 b_D = 0 | unchanged |
| OP-AFD-003c-K_act | M | Vineyard transversality for K_act case | unchanged |
| OP-AFD-003c-K_soft | closed | T-OP-AFD-003-C-soft | unchanged |
| OP-AFD-003d, OP-AFD-003e | L | Smoothness, sensitivity | unchanged |

---

## §6. Recommended actions for the user (revised after §1–§4)

### 6.1 Action set (in priority order)

1. **(Immediate)** Promote AFD-T5 (finiteness) + AFD-T9 + AFD-D1..D5 + AFD-T1 + AFD-T6 to canonical CV-1.14-AFD R1. **No Claim B.3 dependency**. +5A claims, count 64A / 14B / 5C / 5R = 88.

2. **(Decision)** Choose AFD-T11 (T5-Strong) promotion timing:
   - (Option A) Immediate with explicit "Cat A modulo Claim B.3" qualifier in `theorem_status.md`.
   - (Option B) Wait for Claim B.3 verification session (~30–60 min), then promote at Cat A unconditional.
   - **Recommendation:** Option B for cleanliness.

3. **(Documentation)** Apply the 5-line edit to `working/AFD_0/abstract_formation_dynamics.md` lines 390 and 401 (§3.2, §3.3 above). User-executed; this agent records the proposed edit but does not write to working/.

4. **(Cross-reference fix)** Update `00_index.md` and `99_summary.md` of this date to reflect the corrected framing. (Pending user approval — these are in `logs/daily/` so this agent *can* write them.)

5. **(Optional polish)** Once Remote's PR lands (`op_afd_003_brainstorm.md` + `t5_r1_promotion_decision.md` → `working/AFD_0/`), cross-reference them in `99_summary.md`.

### 6.2 Decision points (revised)

(D-1) **Promote AFD-T5 now or together with AFD-T11?** Recommendation: split — promote T5 now (clean), T11 later (after B.3 or with qualifier).

(D-2) **5-line edit to working/AFD_0/abstract_formation_dynamics.md.** Recommendation: yes, user-executed in next working-layer pass.

(D-3) **Register AFD-T11 separately or absorb into AFD-T5.** Recommendation reversed from `03_integration_and_new_open.md` §1.4: **register separately as AFD-T11**. They have different proof dependencies (T5 has none beyond continuity+compactness; T11 has o-minimal).

### 6.3 What does not change

- The mathematical content of `02_development.md` (T-OP-AFD-003-A, B, C, C-soft) is unchanged — it is still correct as a proof of attainment.
- The audit content of `02b` is unchanged — Claim B.3 is still the load-bearing gap for the attainment claim.
- The brainstorm content of `20_AFD_T5_R1_mathematical_toolkit_brainstorm.md` is unchanged — the catalog of tools applies to T5-Strong / AFD-T11 as well as to AFD-T5 itself.

Only the **labeling** changes: what was called "AFD-T5 last gap" is more accurately "T5-Strong / AFD-T11 (a new theorem)".

---

## §7. Self-audit of this correction file

Has this file introduced any new error or silent claim?

- [x] Does not re-edit canonical. (Only writes to logs/daily/.)
- [x] Does not silently resolve any OP. (OP-AFD-003 remains tied to T5-Strong / AFD-T11; renaming, not resolving.)
- [x] Re-cites Remote's two specific findings verbatim and verifies each against `abstract_formation_dynamics.md` line numbers.
- [x] Identifies a real labeling error in this-session's prior logs (not in the math).
- [x] Proposes 5-line working-layer edit but does not execute it.
- [x] Preserves all proof content from `02_development.md`, `02b`, `03`.

**Verdict.** Correction is honest, narrow, and traceable. No new claims; only re-attribution of existing claims to their correct theorem names.

---

## §8. Closing note

The pattern here — *a remote/external agent surfacing a labeling error that a self-audit pass had not caught* — is a **healthy multi-agent dynamic**. The self-audit in `02b` correctly identified Claim B.3 as load-bearing, but did not question *which* theorem Claim B.3 was load-bearing *for*. Remote did. Both passes are necessary.

For future sessions: when this-session output describes a theorem as having "closed a gap", explicitly check whether the gap is in the **theorem's statement** or in a **commentary bullet** attached to the theorem. The two are routinely confused in working drafts and the conflation can mis-attribute the proof's significance.

---

*End of `30_remote_verification_and_T5_statement_correction.md`.*
