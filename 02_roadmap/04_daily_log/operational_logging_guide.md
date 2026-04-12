---
id: ROADMAP-0005
type: roadmap/operational_logging_guide
status: active
created: 2026-04-12
---

# Operational Logging Guide: Detailed Protocols

**Purpose:** Provide detailed templates, examples, and decision protocols for Phase 4+ daily operational logging.

---

## Session Log Template (All Roles)

```markdown
---
id: DAILY-[YYYY-MM-DD]-[ROLE]
type: daily_log/session_log
date: [YYYY-MM-DD]
role: [lead|proof|critic|experiment]
status: active
session_duration_minutes: [N]
created: [YYYY-MM-DD HH:MM:SS]
phase: [current phase number]
related_tasks: [comma-separated task IDs if applicable]
blockers: [severity: 🔴 CRITICAL | 🟠 HIGH | 🟡 MEDIUM | 🟢 LOW]
---

# Session Log: [ROLE] — [YYYY-MM-DD]

## Session Objective
[One sentence: what this role aimed to accomplish today]

## Progress Summary
- ✅ **Completed:** [list items completed]
- 🔄 **In Progress:** [list items actively being worked on]
- ⏸️ **Blocked:** [list items waiting on external factors]

## Findings & Discoveries
[Key empirical, theoretical, or procedural discoveries made today]

### Finding 1: [Title]
- **What:** [Description]
- **Evidence:** [Data, proof, or observation]
- **Impact:** [Consequence for theory or research direction]
- **Action:** [Next step]

## Assumptions & Gaps Identified
[New assumptions surfaced; logical gaps in reasoning]

### Gap 1: [Title]
- **Description:** [What's missing or unclear?]
- **Related to:** [Existing D-xxxx, A-xxxx, or OP-xxxx]
- **Severity:** 🔴|🟠|🟡|🟢
- **Owner:** [Role that should address this]

## Questions Raised
[Open questions for discussion]

### Q-[N]: [Question]
- **Context:** [Why this matters]
- **Related:** [Concepts, theorems, or problems this touches]

## Registry Updates Needed
- [ ] concept_registry.md — new D-xxxx concepts
- [ ] assumption_registry.md — new A-xxxx assumptions
- [ ] theorem_registry.md — if proofs completed
- [ ] open_problems.md — if new OP-xxxx identified

## Blockers & Escalations
[Issues requiring Lead decision or cross-role coordination]

### Blocker: [Title] — Severity 🔴
- **Issue:** [What's blocking progress?]
- **Why:** [Root cause]
- **Attempted:** [What was tried to unblock?]
- **Requires:** [What's needed to unblock?]
- **Escalate to:** [Lead | Proof | Critic | Experiment]

## Notes for Next Session
- [Continuity notes for same role tomorrow]
- [Handoff to other roles if applicable]

## End-of-Session Checklist
- [ ] All findings documented
- [ ] Registry update list compiled
- [ ] Blockers escalated to Lead
- [ ] Next-session notes written
```

---

## Role-Specific Protocols

### LEAD Role: session_log_lead.md

**Objective:** Coordinate all roles; track milestone progress; make/escalate decisions.

**Key Sections:**
- Phase Progress (current phase, tasks completed, timeline)
- Critical Path (dependencies, blockers, critical path items)
- Decisions Made (what was decided, why, impact)
- Cross-Role Coordination (which roles collaborated, what was coordinated)
- Escalations (decisions requiring user input or external approval)

**Example Entry:**

```markdown
### Decision: F-1/M-1/MO-1 Resolution Option

**Date:** 2026-04-13
**Status:** Pending user input

**Options:**
- Option A: Accept current state (publish v1.2 as conditional theory)
- Option B: Develop K-selection mechanism (4–6 weeks)
- Option C: Reformulate as kinetic theory (4–6 weeks)

**Recommendation:** Option B (k-selection mechanism)
- Reason: Makes theory self-contained; most aligned with empirical findings
- Timeline: 4–6 weeks → v2.0 ready for M4
- Resource: Proof role leads; Critic audits; Experiment validates

**Status:** Waiting for user confirmation → proceed with Option B development

**Impact:** Phase 4+ will focus on K-selection axioms, proofs, validation
```

---

### PROOF Role: session_log_proof.md

**Objective:** Drive forward theorem development, lemma proving, rigorous formalism.

**Key Sections:**
- Proofs Completed (what was proved, Category assignment, rigor level)
- Proofs In Progress (current lemmas, stuck points, next steps)
- Rigor Gaps (places needing stronger justification)
- New Lemmas Needed (lemmas identified as prerequisites)

**Example Entry:**

```markdown
### Proof Completed: K-Selection via BIC

**Lemma Title:** BIC Criterion Favors Parsimonious K
**Status:** ✅ COMPLETE (Category A candidate)

**Proof Summary:**
- BIC = -2 log L(K) + K log(n)
- For K=1 with full mass M: BIC₁ ≈ baseline
- For K=2 with equal masses: BIC₂ > BIC₁ (extra term dominates despite likelihood)
- Therefore: BIC always selects K=1 under unconstrained model selection

**Rigor Level:** High (follows standard Bayesian model selection theory)
**FD Validation:** exp76 confirms BIC ranking across 50 configurations

**Next:** Extend to free energy variant (entropy penalty) to allow K>1 emergence
```

---

### CRITIC Role: session_log_critic.md

**Objective:** Audit assumptions, find contradictions, identify hidden dependencies.

**Key Sections:**
- Assumptions Audited (which A-xxxx examined today)
- Contradictions Found (internal inconsistencies discovered)
- Hidden Dependencies (assumptions that were implicit, now explicit)
- Rigor Issues (proofs with weak justifications)

**Example Entry:**

```markdown
### Audit Finding: Assumption A-0013 Circular

**Assumption Audited:** A-0013 (Fixed per-formation mass m_j)

**Finding:** Circular Logic Detected
- Proof of T-Persist-K-Sep assumes A-0013 (m_j fixed)
- But A-0013 is justified by F-1 mitigation strategy (Option B/C)
- Option B (K-selection) aims to derive m_j dynamically
- Circular: deriving what we assume fixed

**Severity:** 🟠 HIGH
**Resolution Required:** Separate "empirically fixed" m_j from "theoretically derived" m_j
- Use A-0013' for empirical regime (observations where m_j appears fixed)
- Keep K-selection mechanism independent (derive m_j from optimization)

**Action:** Update assumption_registry.md to split A-0013 into empirical/theoretical contexts
```

---

### EXPERIMENT Role: session_log_experiment.md

**Objective:** Run validations, gather empirical evidence, discover anomalies.

**Key Sections:**
- Experiments Completed (exp_ID, results, FD error, validation status)
- Key Findings (anomalies, surprises, unexpected behaviors)
- Validation Status (which theorems confirmed, which remain uncertain)
- Next Experiments (which exp should be run to address open questions)

**Example Entry:**

```markdown
### Experiment: exp76_bic_model_selection

**Config:** K=1 (full mass M) vs K=2 (equal masses M/2)
**Runs:** 50 configurations (random λ sweep)
**Result:** ✅ BIC consistently selects K=1

**Key Data:**
- BIC₁ (mean) = -2.34
- BIC₂ (mean) = -1.18
- Selection accuracy: 100% (all 50 runs favor K=1)

**Anomaly:** None; result matches theory prediction exactly

**Validation Status:**
- ✅ Supports K-selection mechanism (Option B direction)
- ✅ BIC criterion discriminates K values reliably
- ⚠️ Still need entropy penalty variant (exp77) to show K>1 can be selected

**Next:** exp77 (free energy with entropy penalty) to test K>1 selection
```

---

## Decision Recording Format (decisions_YYYY-MM-DD.md)

```markdown
---
id: DAILY-[YYYY-MM-DD]-DECISIONS
type: daily_log/decisions
date: [YYYY-MM-DD]
status: [pending|approved|implemented|archived]
---

# Daily Decisions: [YYYY-MM-DD]

## Critical Decision 1: [Title]

**Decision:** [What was decided?]
**Options Considered:** [A, B, C, ...]
**Rationale:** [Why this choice?]
**Impact:** [What changes as a result?]
**Owner:** [Who executes?]
**Timeline:** [By when?]
**Status:** 🔴 Pending user approval | ✅ Approved | 🔄 In progress | ✅ Implemented

---

## Minor Decision: [Title]

**Decision:** [What was decided?]
**Rationale:** [Brief justification]
**Status:** ✅ Implemented

---

## Escalations to Lead/User

### Escalation: [Title] — Severity 🔴

**Issue:** [What needs to be decided?]
**Options:** [A, B, C]
**Recommendation:** [Which option is best?]
**Timeline:** [Urgency]
**Waiting For:** [User input / Lead decision / Proof completion]
```

---

## Registry Update Protocol

**At end of each session**, the Archivist role updates:

1. **concept_registry.md** — Add new D-xxxx if discovered
2. **assumption_registry.md** — Add new A-xxxx if identified
3. **theorem_registry.md** — Update T-xxxx status if proofs completed
4. **open_problems.md** — Add new OP-xxxx if identified
5. **symbol_registry.md** — Add new S-xxxx symbols if introduced

**Example Update Entry:**

```yaml
D-0026: K-Selection Mechanism
- Status: draft
- Definition: Formal criterion (BIC, free energy, etc.) for determining optimal K from data
- First introduced: 2026-04-13 (exp76)
- Related: A-0013, F-1, OP-0005
- References: session_log_proof.md (2026-04-13), exp76_bic_model_selection.py
```

---

## Weekly Consolidation (Every Friday)

**Archivist compiles:** weekly_summary_report_[YYYY-WW].md

**Contents:**
- All decisions made during week
- Critical findings & discoveries
- Blockers & escalations
- Progress on current milestone
- Registry changes & new concepts
- Recommendations for next week

**Example:**

```markdown
# Weekly Summary: Week 15 (2026-04-07 to 2026-04-13)

## Milestone Progress
- M3 (Validation & Audit): ✅ COMPLETE (2026-04-12)
- M4 (Publication): 🔄 Awaiting F-1/M-1/MO-1 decision

## Critical Decision Made
- Option A/B/C choice for F-1/M-1/MO-1 resolution
  - **Chosen:** Option B (K-selection mechanism)
  - **Timeline:** 4–6 weeks
  - **Start Date:** 2026-04-13

## Key Findings
- exp76: BIC criterion reliably selects K=1
- A-0013 has circular logic; needs split into empirical/theoretical contexts
- New concept D-0026 (K-Selection Mechanism) introduced

## New Registrations
- D-0026: K-Selection Mechanism
- A-0013': Fixed m_j (empirical regime)
- OP-0025: Entropy penalty for K>1 selection

## Next Week Priorities
1. Begin K-selection axiom formalization (Proof role)
2. Run exp77 (free energy validation)
3. Update canonical_version_1.2.md with K-selection roadmap
```

---

## Blocker Escalation Protocol

**When a blocker is identified:**

1. **Document** in session_log_[ROLE].md with details
2. **Escalate** to blockers_YYYY-MM-DD.md by end of day
3. **Lead reads** blockers_YYYY-MM-DD.md at session start
4. **Lead decides** escalation path (resolve locally, ask user, delay milestone)
5. **Record decision** in decisions_YYYY-MM-DD.md

**Example Blocker:**

```markdown
## Blocker: Circular Logic in A-0013

**Severity:** 🟠 HIGH
**Type:** Assumption → Logic → Derivation

**Details:**
- A-0013 (fixed m_j) justifies T-Persist-K-Sep
- K-selection mechanism (Option B) aims to derive m_j dynamically
- Circular: proving something we assume fixed

**Impact on Timeline:**
- Proof role stuck on K-selection axiom formalization
- Cannot complete proofs until A-0013 scope is clarified

**Proposed Resolution:**
- Split A-0013 into A-0013 (empirical, fixed) and A-0013' (theoretical, derived)
- Allow both contexts in theory

**Required Decision:**
- Should we maintain two contexts for m_j? (Critic: yes)
- Or reformulate single context? (Proof: unclear)

**Escalate To:** Lead (decide logic resolution), then User if needed
```

---

## Archive & Retention

**After Session Completion:**
- Move session logs to daily_log_index.md (reference only)
- Keep decisions_YYYY-MM-DD.md in 04_daily_log/ for 3 months
- Archive older logs to 13_archive/old_logs_[YYYY]/

**Retention Policy:**
- 🔴 CRITICAL decisions: Keep indefinitely
- Other decisions: Archive after 3 months
- Session logs: Archive after 1 month (but indexed)

---

**Next:** daily_log_index.md (master index), first operational day log (2026-04-13)
