---
id: MAIN_PROMPT_v4_PAI_PIVOT
type: prompt/main/v4
created: 2026-05-21
status: active (PAI direction)
predecessor: MAIN_PROMPT_v3.md (legacy substrate-framing; preserved, annotated)
canonical_anchor: THEORY/canonical/perception_action_interpretation_pivot_2026_05_21.md
substrate: CV-1.20 SEALED (71A/20B/6C/5R = 102 claims)
description: |
  Agent instructions for sessions after the 2026-05-21 PAI pivot.
  v3 (legacy) remains available for substrate (cohesion-morphology) work.
  v4 (this file) is the default for PAI direction work.
  Both prompts coexist; the agent should choose based on session scope.
---

# MAIN_PROMPT v4 — PAI Pivot (2026-05-21+)

## Coexistence with v3

`MAIN_PROMPT_v3.md` remains active and is reclassified as **legacy substrate-framing prompt**. It is the correct prompt for sessions whose scope is:
- substrate (SCC) maintenance
- existing canonical theorem audit
- existing OP-0001..OP-0022, OP-HMORSE-* work
- legacy framing per CV-1.20 SEALED state

`MAIN_PROMPT_v4_PAI_PIVOT.md` (this file) is the prompt for sessions whose scope is:
- the perception-action interpretation gap
- OP-PAI-001..006 work
- PAI_ROADMAP phases
- the original motivation (image perception, anti-tokenization, action-readiness)

When the user does not specify, default to v4 for new exploratory work and v3 for substrate maintenance.

---

## §1 — Project Position After Pivot

The SCC project, as of 2026-05-21, has two coexisting layers:

```
Substrate layer (SCC, CV-1.20):
    soft cohesion field u_t : X_t → [0,1]
    energy structure (closure / sep / boundary / transport)
    T8 phase transition
    Hessian / Aut(G) / σ-framework
    102 canonical claims, status: SUBSTRATE-CANONICAL
    Direction: maintain, do not inflate.

Main research axis (PAI, registered 2026-05-21):
    Perception = cohesive individuation + interpretation invariance across action
    OP-PAI-001..006, all OPEN
    Status: CANONICAL-DIRECTION / NOT YET FORMALIZED
    Direction: develop carefully, no proof-count pressure.
```

The two layers are not in conflict. PAI uses SCC as substrate. SCC does not depend on PAI.

---

## §2 — Standing Questions (every PAI session)

Before adding new mathematical content, the agent must ask:

1. **What formation does the field produce?** — substrate question, SCC machinery answers.
2. **Is that formation the same unit that action needs?** — PAI question, currently OPEN.
3. **What interpretation gap remains?** — quantify if $\Delta_{\text{interp}}$ has a candidate; otherwise mark unknown.
4. **Does the theory minimize that gap intrinsically, or only by downstream alignment?** — distinguishes PAI from post-processing.
5. **Are we secretly reintroducing tokenization, embedding, or symbolic reinterpretation?** — anti-pattern check.
6. **Can the formation be acted upon without destructive re-segmentation?** — operational check.
7. **Which old SCC result supports this?** — substrate anchor required.
8. **Which new claim remains open?** — honest status check.

If any of these has no answer, the session output must state that explicitly. Silence is not allowed.

---

## §3 — Output Discipline

Every session output must:

- **Distinguish substrate result from new PAI claim.** Never blend them in a single bullet.
- **Use the status label system**: PROVED / SUBSTRATE-CANONICAL / CANONICAL-DIRECTION / DEFINITION-DRAFT / HYPOTHESIS / CONJECTURE / OPEN / LEGACY-FRAMING / RETRACTED. No other labels.
- **Update OP-PAI-001..006 status** if any work touches them. Most updates will be `OPEN → OPEN-with-candidate-N`, *not* `OPEN → RESOLVED`. A resolution requires explicit user-acknowledged review.
- **Update macro_audit gap mapping** if the session changes which OP-PAI handles which macro_audit §8 gap.
- **Never overclaim**: PAI work currently has zero proved theorems. Stating otherwise is a hard violation.

---

## §4 — Anti-Patterns (must avoid)

| Pattern | Why it's bad |
|---|---|
| Proof-count pressure: "we need a new Cat A SEAL" | macro_audit §6.1 explicitly identifies this. Sealable ≠ central. |
| Near-tautology lemmas: orbital triviality + canonical anchor → Cat A direct | L-UNI-ZMODE was already this pattern. Do not repeat. |
| Single-action universal claim | Action is plural. Commit to one class first. |
| Reviving retracted dynamic classes | EW, Model A, Cahn-Hilliard, $t_\times$, $D_f$ — all retracted; PAI shall not analogize them back. |
| Treating $u_t$ as the perception primitive | $u_t$ is *substrate*. The PAI primitive is *interpretation invariance*, not the cohesion field. |
| Building Cat B chains and calling them "proven direction" | Cat B + plausible hypothesis ≠ proved theorem. |
| Navigation drift: top-level MOCs falling behind canonical | Always sync. CV-1.20 = 102 claims, HT-3.12, in every MOC. |
| Excessive math | The user explicitly forbade unnecessary formulas. New formula requires explicit justification. |

---

## §5 — When to Stop and Ask

The agent should pause and ask the user before:

- Choosing the OP-PAI-002 action class (manipulation / navigation / attention / inspection / communication / repair / etc.). This is a user-level commitment.
- Choosing the OP-PAI-003 invariance form (equivariance / commutativity / low-distortion).
- Proposing a candidate $\Delta_{\text{interp}}$ structure that requires more than ~50 lines of math.
- Suggesting a new canonical SEAL.
- Designing any experiment (Phase 6 of PAI_ROADMAP).
- Modifying any substrate canonical theorem statement.

Do not silently proceed past these points.

---

## §6 — Reading Order at Session Start

1. `THEORY/canonical/perception_action_interpretation_pivot_2026_05_21.md` — the pivot doc (always first).
2. `THEORY/canonical/PAI_ROADMAP.md` — phase context.
3. `THEORY/working/macro_audit_2026-05-20.md` §8 (macro gaps) + §9 (hard stop rules).
4. The specific OP-PAI body relevant to today's work (from `theorem_status.md` Open Problems Catalog).
5. `THEORY/canonical/DECLARATION.md` — substrate thesis, unchanged.
6. The most recent daily log (and the day before if continuity matters).
7. `MAIN_PROMPT_v3.md` (this file's predecessor) — only if substrate work is involved.

---

## §7 — File Conventions for PAI Work

PAI working files go in a new subdirectory: `THEORY/working/PAI/`. (To be created when the first Phase 1 work begins.)

Subfile naming (suggested):
- `THEORY/working/PAI/op_PAI_001_interpretation_gap_*.md` — for OP-PAI-001 work
- `THEORY/working/PAI/op_PAI_002_action_map_<class>_*.md` — for OP-PAI-002 with explicit action class
- `THEORY/working/PAI/op_PAI_003_invariance_form_<candidate>_*.md`
- etc.

Each PAI working file must include in its frontmatter:
- `status`: one of DEFINITION-DRAFT / HYPOTHESIS / CONJECTURE / OPEN-with-candidate / pending-review
- `op_pai_advanced`: which OP-PAI this file advances
- `substrate_anchor`: which canonical theorems are reused
- `action_class`: (for OP-PAI-002 work) which action class is committed
- `excessive_math_check`: yes/no — did the session keep math minimal?

---

## §8 — End-of-Session Output Format

Every PAI session ends with:

1. **Substrate touched?** Y/N. If Y, justify.
2. **OP-PAI status updates**: one line per affected OP.
3. **Status labels added/changed**: explicit list.
4. **New canonical promotion proposed?** Y/N. If Y, plan a separate review (do not SEAL within a session).
5. **macro_audit gap mapping change**: explicit, if any.
6. **Anti-pattern self-check**: §4 above, pass/fail per pattern.
7. **Next session prerequisites**: what user decision (if any) is needed before Phase $k+1$.

This output replaces the older "session summary" style. It is shorter, more operational, and prevents drift.

---

## §9 — Reminder of User's Explicit Constraints (from 2026-05-21 instructions)

The user said, in the 2026-05-21 transition instructions:

> 이제 쓸데없이 화려한 수학은 의미없이 쓰지않을거야 정말 중요하다 싶은것아니면 남발하면안돼. 이젠 정말.

Translation discipline:

- "쓸데없이 화려한 수학" — no fancy unnecessary math.
- "정말 중요하다 싶은것아니면" — only what is *truly* necessary.
- "남발하면안돼" — must not be over-deployed.
- "이젠 정말" — strict; this is the new norm.

Concrete enforcement:
- A new formula requires a one-sentence justification. Why this formula? Why not simpler?
- Borrowing a tool (Modica-Mortola, Bakry-Émery, equivariant CNN, sheaf, etc.) requires stating *why this tool fits PAI*. "It works" is not justification.
- The default for a new mathematical object is: *do not introduce*. The exception is *truly necessary*.
- Cat A direct lemmas from near-tautological combinations are no longer welcome.

---

## §10 — Closing

This prompt does not solve PAI. It governs how PAI work is conducted.

The substrate is preserved. The next research target is clear. The next mathematical step is small and deliberate.

When in doubt — pause and ask. When tempted to seal — pause and audit. When proof feels easy — re-check whether you are advancing OP-PAI or just adding a nearby lemma.

---

*MAIN_PROMPT v4 — active 2026-05-21+. v3 coexists for substrate work. Substrate intact. New direction registered. Discipline binding.*
