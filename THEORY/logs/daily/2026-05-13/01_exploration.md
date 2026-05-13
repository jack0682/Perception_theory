# 01 — Exploration (Restatement + Multi-Approach + Primary Selection)

**Session:** 2026-05-13
**Target (from `00_plan.md`):** CV-1.15 Action-Based Temporal Succession Package promotion application + post-promotion consistency audit (or, if P7 not granted, completion of approval-ready package).
**This file covers:** §4.1 Restatement, §4.2 Multi-approach (≥3 independent), §4.3 Primary selection rationale.
**Depends on reading:**
- `THEORY/logs/daily/2026-05-13/00_plan.md`
- `THEORY/working/CV115_ACTION_TEMPORAL_COST/09_final_audit.md` (READY FOR USER APPROVAL judgment)
- `THEORY/working/CV115_ACTION_TEMPORAL_COST/10_patch_plan.md` (canonical / theorem_status / hypothesis_tree / CHANGELOG draft blocks)
- `THEORY/working/CV114_TEMPORAL_COMPOSITION/05_promotion_draft.md` (T-CC-StableK-Kernel CV-1.14 candidate; **NOT YET PROMOTED**)
- `THEORY/canonical/canonical.md` §13 (current CV-1.13 state), §8.5 (M_{t→s} definition), §11/§14 (commitments / commitment notes)
- `THEORY/canonical/theorem_status.md` (CV-1.13: 59A/14B/5C/5R = 83 claims)
- `THEORY/canonical/hypothesis_tree.md` (HT-3.5)
- `THEORY/CHANGELOG.md` (newest-on-top header)
- `CODE/experiments/results/exp89_results.json`

---

## §4.1 Restatement

### §4.1.1 What is being asked

Today's target is **not** a new mathematical proof; it is a **structural transition** in the canonical layer: take the 10-file CV-1.15 working package (action-based temporal succession theorems, completed 2026-05-12) plus its numerical sanity check (exp89, 3-case PASS, 2026-05-13 morning) and either (a) apply the promotion to `canonical.md` / `theorem_status.md` / `hypothesis_tree.md` / `CHANGELOG.md` if user grant P7 in this turn, or (b) complete the approval-ready package and execute a *dry-run* post-promotion consistency audit against the canonical-as-is.

### §4.1.2 Decomposition of the request

The plan (`00_plan.md`) decomposes the request into seven blocks (A–G):

| Block | Status under P7-not-yet-granted | Status under P7-granted |
|---|---|---|
| A. Pre-approval final review | **EXECUTE** | (already done) |
| B. User approval gate | **WAIT** | (consumed) |
| C. Patch application | **FORBIDDEN** | EXECUTE |
| D. Post-promotion consistency audit | **DRY-RUN against canonical-as-is** | EXECUTE on post-patch canonical |
| E. exp89 registration check | EXECUTE | EXECUTE |
| F. New OP refinement (OP-0012-SINK) | EXECUTE | EXECUTE |
| G. Final readiness report | EXECUTE | EXECUTE |

This session enters with P7 **NOT** granted (the `ultrawork` skill invocation by the user is not the same as user approval to overwrite `canonical/*` — and the plan's prompt body explicitly forbids canonical writes; §8.1 of `MAIN_PROMPT.md`). Therefore this session is in the "P7-not-yet-granted" column: Block A + D-dry + E + F + G are in scope; Blocks B + C are out of scope.

### §4.1.3 What counts as success today

The plan provides two success criteria (`00_plan.md` lines 77–81):

> **Pre-approval success:** "approval-ready package가 모든 검토를 통과하고, 내일 바로 적용 가능한 상태이다."
> **Post-approval success:** "CV-1.15가 canonical에 반영되었고, post-promotion consistency audit를 통과하며, OP-0012-SINK OPEN이 hypothesis_tree에 명확히 기록되었다."

Under the no-canonical-write constraint, **only the pre-approval criterion is achievable in this session.** The post-approval criterion can only be reached after a separate user turn explicitly authorizes canonical edits.

### §4.1.4 What counts as failure today

Failure modes the session must avoid (in priority order):

1. **Silent canonical write** — modifying `canonical.md` / `theorem_status.md` / `hypothesis_tree.md` / `CHANGELOG.md` without explicit P7 approval. (Hard prohibition; `00_plan.md` lines 60–62 + 110–113; prompt §8.1.)
2. **Silent CV-1.14 absorption** — applying the CV-1.15 patch as if CV-1.14 T-CC-StableK-Kernel were already canonical, when in fact it is still in `working/CV114_TEMPORAL_COMPOSITION/05_promotion_draft.md` (Cat B draft, not promoted). The 10_patch_plan §1 background sentence ("**배경**: CV-1.14 T-CC-StableK-Kernel (Cat B)은 ...") **silently assumes** a canonical fact that is not in canonical. This must be flagged.
3. **Silent OP-0012 resolution** — declaring OP-0012 or OP-0012-SINK "resolved" by CV-1.15 when only the cost-level $\delta_\mathrm{eff}$ blocker is removed *under the redefinition* `c^{\mathrm{direct}} := c^{\mathrm{act}}`. The Sinkhorn-scaling-gap blocker is untouched. (`00_plan.md` line 60.)
4. **Treating exp89 as proof** — exp89 is a *numerical sanity check*; Cat A judgments rest on the closed-form proofs in CV115 files 01–04. (`00_plan.md` line 97.)
5. **Reintroducing Research OS scaffolding** — prompt §8.3.

### §4.1.5 Surfaced assumptions in `00_plan.md` (made explicit)

The plan implicitly assumes:

- **(A-1)** CV-1.14 T-CC-StableK-Kernel is canonically available. → **FALSE** under current canonical state. `theorem_status.md` lists OP-0012 as "PARTIALLY STRUCTURED (Session V, 2026-05-06)" with **no** Cat B row for T-CC-StableK-Kernel. Resolution required (see §4.2 Approach P1).
- **(A-2)** The CV-1.15 patch can be inserted as a single `§13.Y` block at the end of canonical §13. → **Style-mismatch** with canonical's category-stratified §13 (Category A / Category B / Category C / Retracted). Either restructure the patch by category, or accept a stylistically anomalous single-version-named subsection. (Audit finding; not blocking.)
- **(A-3)** The claim-count delta is +8A +2B with current baseline 83 → target 93. → **Correct iff (A-1) holds**, since CV-1.14 brings +1B which is unaccounted-for in this delta. If CV-1.14 + CV-1.15 are co-promoted, the correct target is 67A/17B/5C/5R = 94 (or 95 if `P-ACTION-PATH-INHERITANCE` is included as Interpretation row). If CV-1.14 is **not** co-promoted, then CV-1.15's T-ACT-KERNEL-COMP→REL Cat B row contains a dangling forward reference to a non-canonical lemma.
- **(A-4)** "refinement not replacement" framing is sufficient to inoculate against the perception that action cost displaces T-Temporal-Identity. → Substantive, but verifiable only by reading the draft block; verified below in §4.2 Approach P3.
- **(A-5)** OP-0012-SINK is a single, well-defined open problem. → Holds, but the name is misleading (the gap is at the scaling-vector level, not the Sinkhorn algorithm level). Plan §F defers rename to CV-1.16; this is conservative.

These five surfaced assumptions are the audit's actual workload.

---

## §4.2 Multi-Approach (≥3 mathematically independent paths)

Today's "approach" is not a mathematical proof strategy but a **promotion-workflow strategy**. The independence criterion is: each approach must produce a different *deliverable shape* under the no-canonical-write constraint, must fail differently if its premise is wrong, and must compose-or-substitute with the others.

### §4.2.1 Approach P1 — Two-step promotion with explicit CV-1.14 pre-promotion gate

**Core idea.** Recognize that CV-1.15's draft block references CV-1.14 T-CC-StableK-Kernel as "**배경**" canonical lemma, but CV-1.14 is **not** in canonical. Resolve by treating CV-1.14 and CV-1.15 as *two separate gates*: P7-A (CV-1.14 approval) and P7-B (CV-1.15 approval), with P7-B conditional on P7-A. Produce a unified pre-approval package covering **both** versions, plus a unified count-delta table.

**Successful output shape.**
- Two CHANGELOG draft blocks (CV-1.14 entry above the CV-1.13 entry; CV-1.15 entry above the CV-1.14 entry).
- A unified count table: 83 → 84 (CV-1.14, +1B) → 93 (CV-1.15, +8A +2B) → 94 (if P-ACTION-PATH-INHERITANCE counted).
- A unified theorem_status table: T-CC-StableK-Kernel Cat B inserted **before** the CV-1.15 Cat B rows.
- An updated `H-COMP` branch in hypothesis_tree that places `H-COMP-KERNEL` (CV-1.14, Cat B) **above** `H-COMP-ACTION` (CV-1.15) — matching the 10_patch_plan §3 draft exactly.
- An updated 10_patch_plan §1 to either include CV-1.14's Cat B theorem block *immediately above* the CV-1.15 §13.Y subsection, or to footnote the CV-1.14 reference as "working candidate, pending canonical."

**Failure modes.**
- If the user wants CV-1.15 promoted *without* CV-1.14 (e.g., wants to defer CV-1.14 to a separate review session), the unified package must be split. P1 then fails as written but is recoverable: drop the CV-1.14 row and downgrade the CV-1.15 background sentence to "T-CC-StableK-Kernel (CV-1.14 working candidate)."
- If CV-1.14's 05_promotion_draft has its own audit issues we have not surfaced (we did not run an audit of the CV-1.14 proof here), the co-promotion can compound risk. Mitigation: this session does not promote; the user's P7 gate is the final check.

**Interaction with existing axioms / theorems.**
- Touches `canonical §13` Cat B section directly (two new rows: T-CC-StableK-Kernel from CV-1.14; T-ACT-KERNEL-COMP→REL + P-SINKHORN-STABILITY-CONDITIONAL from CV-1.15).
- Touches `canonical §8.5` *only as commentary* — the patch does not redefine $M_{t\to s}$; that is deferred to a hypothetical CV-1.16.
- Does **not** modify §11 (Fixed Commitments) or §14 (Commitment Notes).
- Interacts with T-Temporal-Identity (§13 Cat A, CV-1.13) by *explicit non-interference statement* in the §13.Y header.

### §4.2.2 Approach P2 — CV-1.15-only promotion with CV-1.14 demoted to working-citation

**Core idea.** Preserve the current canonical's CV-1.14-absent state. Rewrite the CV-1.15 §13.Y background and T-ACT-KERNEL-COMP→REL statement to cite CV-1.14 as a *working* candidate, not a canonical lemma. Promote only CV-1.15.

**Successful output shape.**
- Single CHANGELOG block for CV-1.15.
- 10_patch_plan §1 amendments: the background sentence becomes "T-CC-StableK-Kernel (working candidate, `THEORY/working/CV114_TEMPORAL_COMPOSITION/05_promotion_draft.md`, Cat B not yet canonical) ..."; the T-ACT-KERNEL-COMP→REL "조건 의존성" note becomes "depends on T-CC-StableK-Kernel; canonical instance pending CV-1.14 promotion."
- Count delta: 83 → 93 (+8A +2B) — clean.
- Hypothesis-tree update would create only `H-COMP-ACTION` and `H-COMP-SINK` nodes; `H-COMP-KERNEL` remains a *working* branch outside the tree until CV-1.14 promotes.

**Failure modes.**
- The CV-1.15 Cat B claim T-ACT-KERNEL-COMP→REL becomes structurally weaker: it asserts "(GK) + (stable-K) + (margin) → R composition," but the "→ R composition" step is exactly the content of CV-1.14's T-CC-StableK-Kernel. If CV-1.14 is not canonical, T-ACT-KERNEL-COMP→REL is reduced to a *conditional* claim about R composition that depends on a non-canonical lemma — i.e., it should drop to Cat C, not Cat B.
- This is a meaningful weakening. It may be a *correct* weakening (we should not Cat-B-judge a theorem whose key premise is non-canonical), but it changes the CV-1.15 promotion table.

**Interaction with existing axioms / theorems.**
- Same surface as P1 but with one fewer row touched.
- Forces a Cat reclassification of T-ACT-KERNEL-COMP→REL (Cat B → Cat C until CV-1.14 promotes).

### §4.2.3 Approach P3 — Pure audit-only session (no patch shape change)

**Core idea.** Treat today as a *pure pre-approval audit + dry-run post-audit*. Do not propose any modification to the 10_patch_plan draft blocks. Instead, produce: (i) a written terminology / symbol / category audit of the existing 09_final_audit + 10_patch_plan; (ii) a dry-run of the Block D consistency grep against canonical-as-is, expressed as "what *would* be the audit findings if the user applied 10_patch_plan §1–§4 unchanged"; (iii) a recommendation list for the user (rather than rewritten drafts).

**Successful output shape.**
- `02_development.md` § "Block A audit findings" — terminology + symbol + category + framing audit.
- `02_development.md` § "Block D dry-run" — grep results on canonical-as-is for each of the 8 grep terms in `00_plan.md` lines 148–157.
- `02_development.md` § "Block E + F" — exp89 verification + OP-0012-SINK structure notes.
- `03_integration_and_new_open.md` — integration recommendations as bullet recommendations (not as rewritten drafts).

**Failure modes.**
- This approach does not deliver a *promotion-ready* package — it delivers an *audit report on the existing package*. If the existing package has hard blockers (e.g., the CV-1.14 dependency), P3 surfaces them but does not fix them. Mitigation: feed audit output back to plan author (the user) for next-session disposition.

**Interaction with existing axioms / theorems.**
- Zero modification proposed to working/* or canonical/*. Pure observation.

### §4.2.4 Approach P4 (rejected) — Inline canonical patch application "trial run" in a fork

**Core idea.** Create a `THEORY/logs/daily/2026-05-13/canonical_TRIAL.md` containing the post-patch canonical state for visual inspection.

**Why rejected.** This creates a synthetic canonical copy outside the promotion pipeline. Even if labeled "trial," its presence in the repo invites accidental promotion. Violates the contamination-barrier principle (CONVENTIONS.md §2; `00_plan.md` lines 60–62). Same audit goal is achieved more safely by P3.

### §4.2.5 Approach P5 (rejected) — Direct mathematical extension (e.g., proving L-δ_eff-SINK)

**Core idea.** Use today's session to attack OP-0012-SINK's L-δ_eff-SINK Cat C lemma.

**Why rejected.** Out of scope per `00_plan.md` lines 58–60 ("Sinkhorn-scaled plan semigroup 증명 시도 금지"). This is correctly deferred to CV-1.16 or later.

---

## §4.3 Primary Selection Rationale

### §4.3.1 Decision

**Primary approach: P3 (pure audit-only).** Secondary: P1 (two-step promotion package). P2 is preserved as a fallback if user signals "do not co-promote CV-1.14."

### §4.3.2 Why P3 is primary

Four reasons, in priority order:

1. **No-canonical-write constraint is absolute today.** Both P1 and P2 produce *modified 10_patch_plan drafts* as their deliverable; even though these are in working/, they would be silently consumed by the next promotion session. P3 produces explicit audit findings *separately* from the existing drafts. This preserves a clean separation between "what the plan said to apply" (10_patch_plan as-is) and "what the audit found needs amendment" (this session's 02 file). The user can choose to update 10_patch_plan or to apply with the audit findings in-mind.
2. **CV-1.14 dependency is the dominant audit finding.** Both P1 and P2 commit to a resolution of this dependency *before* the user has signaled which they prefer. P3 surfaces the dependency and lets the user choose.
3. **Symbol collisions and framing fixes are already noted in 09_final_audit §10 (READY AFTER MINOR FIXES).** P3 verifies these and adds *new* findings; P1/P2 would re-litigate them.
4. **The plan's primary deliverable today is the audit + readiness report (Block A + D + G).** Blocks C is forbidden. P3 is the most direct match to that deliverable shape.

### §4.3.3 Preservation of alternatives

P1 and P2 are preserved in this file's §4.2 because:

- If the user, after reading 02_development.md's audit findings, signals "apply CV-1.14 + CV-1.15 together," P1 becomes the active plan.
- If the user signals "apply CV-1.15 only and downgrade T-ACT-KERNEL-COMP→REL," P2 becomes active.
- If the user signals "fix and apply as drafted," neither is needed — but a 10_patch_plan §1 amendment is required (covered in `03_integration_and_new_open.md` §recommendations).

Each alternative is preserved at a granularity sufficient to reactivate in a follow-up session without re-deriving.

### §4.3.4 What P3 commits to producing

`02_development.md` will contain the following subsections (numbered for follow-up references):

- §1. Block A — Pre-approval final review
  - §1.1 Cross-file consistency check (09_final_audit ↔ 10_patch_plan ↔ exp89_results.json)
  - §1.2 Terminology audit (8 vocabulary terms)
  - §1.3 Symbol audit (K-collision, M vs Π vs **K**)
  - §1.4 Category-A condition explicitness audit (per the 8 Cat A entries)
  - §1.5 "Refinement vs replacement" framing audit
  - §1.6 δ_eff=0 scope-restriction audit
  - §1.7 exp89 framing audit (numerical, not proof)
- §2. CV-1.14 dependency finding (new, not in 09_final_audit)
  - §2.1 Statement of dependency
  - §2.2 Three resolution paths (R-A: co-promote; R-B: demote T-ACT-KERNEL-COMP→REL; R-C: rewrite background)
  - §2.3 Recommendation
- §3. Style-mismatch finding (new)
  - §3.1 §13.Y as single block vs §13's existing Category-stratification
  - §3.2 Resolution options
- §4. Block D — Post-promotion consistency audit (dry-run on canonical-as-is)
  - §4.1 Grep checklist execution
  - §4.2 Findings
- §5. Block E — exp89 numerical sanity check verification
- §6. Block F — OP-0012-SINK structural notes
- §7. Block G — Final readiness report (today's state)
- §8. Self-classification of this session's findings (which are blocking vs advisory)

---

*End of 01_exploration.md. Next file: `02_development.md`.*
