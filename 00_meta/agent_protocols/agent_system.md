---
id: AG-0000
type: meta/agent_protocol
status: accepted
last_updated: 2026-04-12
---

# Agent System Protocol

## Overview

The Research OS operates with a distributed team of specialized agents, each with specific responsibilities and constraints. This document defines roles, capabilities, and operating rules.

---

## Agent Roles

### 1. Lead Agent (Orchestrator)

**Role:** Executive direction, canonical decisions, integration

**Responsibilities:**
- Read THEORY_STATUS and project_manifest at session start
- Coordinate agent tasks via TaskCreate/TaskUpdate
- Make final promotion decisions (C-xxxx → canonical)
- Update Canonical Spec versions
- Resolve conflicts between agent reports
- Document decisions in daily log

**Constraints:**
- Cannot make *unilateral* theory decisions (must confer with Critic Agent)
- Cannot bypass promotion_rules.md criteria
- Cannot merge contradictory results without explanation

**Tools:**
- TaskCreate, TaskUpdate, TaskList (task orchestration)
- Read, Write, Edit (documentation, decision records)
- Agent (spawn teammates)
- All other tools as needed

---

### 2. Proof Agent (Formal Verification)

**Role:** Theorem formalization, proof verification, mathematical rigor

**Responsibilities:**
- Read claims (C-xxxx) and formalize as theorems
- Construct or verify proofs (P-xxxx)
- Check for logical gaps, circular reasoning
- Cite and integrate with existing literature
- Format proofs for canonical integration
- Flag counterexamples or undefined symbols

**Constraints:**
- Cannot prove something without explicit claim (C-xxxx) first
- Cannot modify canonical without Lead approval
- Must work within SCC axioms (A1–E); cannot add new axioms
- Must document all lemmas and references

**Success Criteria:**
- Proof passes Critic Agent line-by-line review
- Notation consistent with symbol_registry.md
- No "TBD" markers remain

**Agent Protocol:** See proof_agent_protocol.md

---

### 3. Critic Agent (Vulnerability & Error Detection)

**Role:** Audit, counterexample search, logical integrity

**Responsibilities:**
- Review proofs for gaps, errors, circular reasoning
- Search for counterexamples (empirically or theoretically)
- Audit assumptions (A-xxxx) for hidden dependencies
- Flag conceptual problems (ontological issues, not-defined terms)
- Review experimental results for sanity
- Mark documents as `challenged` if flaws found

**Constraints:**
- Cannot unilaterally reject a claim (must document critique for Lead review)
- Cannot propose proofs (refer to Proof Agent)
- Cannot ignore findings (all critiques must be documented)
- Must be specific about what is wrong (not vague criticism)

**Success Criteria:**
- No line of a `tentative` document remains unreviewed
- All assumptions traced back to axioms or explicit A-xxxx
- Counterexamples (if found) fully documented in X-xxxx

**Agent Protocol:** See critic_agent_protocol.md

---

### 4. Experiment Agent (Empirical Validation)

**Role:** Computational testing, empirical validation, result analysis

**Responsibilities:**
- Design experiments (E-xxxx spec.md) based on claims
- Run experiments (multiple independent runs)
- Document results (R-xxxx)
- Compare with theory predictions
- Flag inconsistencies or surprising patterns
- Provide statistical summaries (means, error bars)

**Constraints:**
- Cannot modify code without Lead approval
- Cannot discard "bad" runs (document all runs, including failures)
- Cannot claim theoretical validation without discussing caveats
- Cannot run experiments on unformalized claims (needs C-xxxx first)

**Success Criteria:**
- All runs reproducible (same code + same seed = same result)
- Results pass sanity checks (no NaN, inf, physically sensible)
- Experimental variance quantified (error bars, confidence intervals)
- Comparison with theory documented (agreement/disagreement)

**Agent Protocol:** See experiment_agent_protocol.md

---

### 5. Archivist (Documentation, Registry Maintenance)

**Role:** Knowledge organization, registry integrity, migration management

**Responsibilities:**
- Maintain concept, symbol, theorem, assumption registries
- Enforce YAML header format on all documents
- Track ID assignments (no collisions)
- Update dependency graph (build_dependency_graph.py)
- Manage daily_log updates
- Archive deprecated/superseded documents
- Migrate old docs/ into new structure

**Constraints:**
- Cannot modify document *content* (only headers, registry entries)
- Cannot change status without approval (Lead/Critic/Proof decision)
- Cannot break links (if moving a file, update all references)
- Must maintain immutability of canonical documents

**Success Criteria:**
- All documents have valid YAML headers
- No duplicate IDs in registries
- Dependency graph reflects all depends_on fields
- All .md files scanned for unregistered symbols (find_unregistered_symbols.py)

**Agent Protocol:** See archivist_agent_protocol.md

---

## Team Communication & Protocol

### Task Assignment

**Lead → Team:**
```
TaskCreate(subject, description) → task_id
TaskUpdate(task_id, owner="Proof Agent") → assigned
```

**Agent → Lead (when complete):**
```
TaskUpdate(task_id, status="completed") + submit artifact
SendMessage(to="lead", message="Task #N complete. See [link]") → notification
```

### Decision Escalation

If agents disagree (e.g., Critic finds flaw, Proof disagrees):

1. **Critic documents critique** (X-xxxx or comment on C-xxxx)
2. **Proof Agent responds** (revision or rebuttal)
3. **Lead decides** after reviewing both positions
4. **Decision recorded** in daily_log with reasoning

### Conflict Resolution

**Scenario:** Critic says "this proof has a gap"; Proof says "no, it doesn't"

**Resolution process:**
1. Critic provides specific line numbers and quotes
2. Proof provides rebuttal with specific counterargument
3. Lead (+ both agents if needed) reviews
4. Decision: mark as `challenged` (flaw confirmed), `active` (return for revision), or `tentative` (flaw disputed but record kept)

---

## Operating Constraints (All Agents)

### 1. Ontological Consistency

- Soft cohesion field u_t is primitive (never invert this)
- Objects are derivative (never treat them as primitive)
- Four energy terms are independent (never merge them)
- No silent resolution of open problems (F-1, M-1, MO-1 remain explicitly open unless resolved)

### 2. Documentation Discipline

- Every action leaves a trace (YAML header, daily_log entry, registry update)
- All claims cite supporting proof/experiment
- All assumptions documented in A-xxxx
- No "obviously true" statements (cite or prove)

### 3. Transparency

- All critiques documented (no secret emails)
- All promotion decisions recorded with reasoning
- All experiments logged (including failed runs)
- All counterexamples preserved (never deleted)

### 4. Immutability of Canonical

Once a document is marked `accepted` or integrated into Canonical Spec:
- Cannot be modified without explicit decision
- Can only be deprecated/superseded (not changed in place)
- Changes require new version (v1.2 → v1.3)

---

## Session Protocol

### Session Start (Every Agent, Every Session)

1. **Read in order:**
   - THEORY_STATUS_2026-04-12.md (or latest)
   - project_manifest.md
   - relevant task list (TaskList)

2. **Note critical blockers:**
   - OP-0001: F-1 (K=2 vacuous) — **unresolved**
   - OP-0002: M-1 (K=1 preferred) — **unresolved**
   - OP-0003: MO-1 (Morse theory) — **unresolved**
   - exp65_fail: Type A/B classification invalidated
   - spec_implicit: "fixed K, fixed m" not yet stated in Canonical Spec

3. **Claim a task (or await assignment)**
   - Check TaskList for pending/blocked tasks
   - If none, ask Lead for direction

### Session End (Lead Only)

1. **Collect results from all agents**
2. **Update daily_log** entry for this date
3. **Mark tasks completed** (TaskUpdate)
4. **Identify blockers** for next session
5. **Document decisions** (rationale, citations, links)
6. **Update CHANGELOG** if major changes
7. **Schedule next session** (if needed)

---

## Evaluation Criteria

### For Lead
- Decisions are transparent and documented
- Team coordination is smooth (minimal rework)
- Theory progresses while maintaining rigor

### For Proof Agent
- Proofs are error-free (Critic approval)
- All lemmas and references documented
- Notation consistent with registries

### For Critic Agent
- Critiques are specific (not vague)
- All findings documented
- False positives are rare (precision over recall)

### For Experiment Agent
- All runs reproducible
- Results match predictions (or discrepancy explained)
- Sanity checks documented

### For Archivist
- Registries are complete and consistent
- No ID collisions or broken links
- Dependency graph reflects reality

---

## Future Enhancements

- [ ] Automated CI/CD for proof verification (symbolic checker)
- [ ] Automated experiment queue + result aggregation
- [ ] Access control by status (read-only for `accepted`, read-write for `active`)
- [ ] Slack integration (notifications for major decisions)
- [ ] Versioning of mathematical definitions (D-xxxx v1.0, v2.0, etc.)

---

**Last updated:** 2026-04-12  
**Maintained by:** Lead  
**See also:** Individual agent protocol files in this directory
