---
id: ROADMAP-0004
type: roadmap/daily_log_guide
status: active
created: 2026-04-12
last_updated: 2026-04-12
---

# Phase 4: Operational Logging (04_daily_log/)

**Purpose:** Record daily research progress, decisions, findings, and blockers in real-time. Prevent knowledge loss; provide audit trail; support context continuity across sessions.

**Structure:** One directory per day (YYYY-MM-DD/). Each day contains up to 4 documents from 5 agent roles (Lead, Proof, Critic, Experiment, Archivist).

---

## Daily Log Format

### Directory Structure

```
04_daily_log/
├── README.md (this file)
├── daily_log_index.md (master index of all days)
├── operational_logging_guide.md (detailed protocols)
├── 2026-04-13/
│   ├── session_log_lead.md
│   ├── session_log_proof.md
│   ├── session_log_critic.md
│   ├── session_log_experiment.md
│   └── decisions_2026-04-13.md (consolidated decisions)
├── 2026-04-14/
│   ├── session_log_lead.md
│   ├── ...
└── [YYYY-MM-DD]/
    └── ...
```

### File Naming Convention

- `session_log_[ROLE].md` — Perspective-specific session notes (role ∈ {lead, proof, critic, experiment})
- `decisions_[YYYY-MM-DD].md` — Consolidated daily decisions, blockers, escalations
- `findings_[YYYY-MM-DD].md` — Key empirical/theoretical discoveries
- `blockers_[YYYY-MM-DD].md` — Issues blocking progress (escalations to lead)

### YAML Header Template

```yaml
---
id: DAILY-YYYY-MM-DD-[ROLE]
type: daily_log/session_log
date: YYYY-MM-DD
role: [lead|proof|critic|experiment|archivist]
status: [active|archived]
session_duration_minutes: [N]
created: YYYY-MM-DD HH:MM:SS
phase: [1|2|3|4|5]
related_tasks: [TASK-IDs, comma-separated]
---
```

---

## Five Agent Roles

| Role | Responsibility | Focus | Output |
|------|-----------------|-------|--------|
| **Lead** | Session coordination, decision-making, escalations | High-level progress, blockers, direction | session_log_lead.md, decisions_YYYY-MM-DD.md |
| **Proof** | Theorem proving, formalism development | Proof status, lemmas, rigor issues | session_log_proof.md, proofs_status.md |
| **Critic** | Assumption auditing, contradiction detection | Hidden assumptions, logical gaps, errors | session_log_critic.md, critical_findings.md |
| **Experiment** | Empirical validation, data analysis, exp runs | Exp results, validation status, anomalies | session_log_experiment.md, findings_YYYY-MM-DD.md |
| **Archivist** | Documentation, registry updates, file management | Meta-changes, new registries, migrations | session_log_archivist.md, changelog.md |

---

## Daily Session Protocol

### Session Start (All roles)

1. **Read** 02_roadmap/milestones/M[current].md to understand current milestone
2. **Read** 00_meta/ constitutional layer for context
3. **Review** decisions_[YYYY-MM-DD-1].md from previous day (blockers, escalations)
4. **Open** session_log_[ROLE].md and begin logging

### During Session

- **Lead:** Log progress against current phase, decisions, new blockers
- **Proof:** Log proof status, lemmas completed, rigor issues discovered
- **Critic:** Log assumptions identified, contradictions found, gaps in logic
- **Experiment:** Log exp runs, results, anomalies, validation status
- **Archivist:** Log file changes, registry updates, migrations

### Session End (All roles)

1. **Summarize** findings in session_log_[ROLE].md
2. **Lead consolidates** all role logs into decisions_YYYY-MM-DD.md
3. **Archivist commits** session logs to daily_log_index.md
4. **Update** 00_meta/ registries with any new concepts, assumptions, or theorems discovered

---

## Integration Points

### With 00_meta/ (Constitutional Layer)

- New **concepts (D-xxxx)** discovered → concept_registry.md updated
- New **assumptions (A-xxxx)** discovered → assumption_registry.md updated
- New **theorems (T-xxxx)** proved → theorem_registry.md + promotion_rules.md
- New **open problems (OP-xxxx)** identified → open_problems.md updated

### With 01_canonical/ (Specifications)

- **Release notes** generated from weekly_summary_report.md (Friday consolidation)
- **Version bumps** trigger canonical version updates
- **Major findings** trigger canonical spec revisions

### With 02_roadmap/ (Milestones & Dependency)

- **Milestone completion** logged in session_log_lead.md
- **Critical blockers** escalated to dependency_graph.md
- **Go/no-go decisions** recorded in decisions_YYYY-MM-DD.md

### With 03_context_memory/ (Immutable Registries)

- **Registries read** at session start (cache for fast lookups)
- **Changes written back** at session end via Archivist role
- **Conflicts resolved** by Critic role before commit

---

## Critical Decision Point: F-1/M-1/MO-1 Resolution

**Current Status (M3 Complete):** Three unresolved critical problems must be addressed before M4 (Publication).

**Logging Approach (Phases 4+):**

- **If Option A chosen:** Phase 4 logs focus on publication preparation, paper writing, communication strategy
- **If Option B chosen:** Phase 4 logs focus on K-selection mechanism development, new proofs, BIC/free energy integration
- **If Option C chosen:** Phase 4 logs focus on kinetic theory reformulation, barrier analysis, new axiomatics

The daily log structure supports all three paths. Decision should be recorded in **decisions_2026-04-13.md** (first operational day).

---

## Archival Protocol

**Weekly:** Friday consolidation → weekly_summary_report.md (generated by Archivist)

**Monthly:** Month-end review → MONTHLY_REVIEW_[YYYY-MM].md (consolidated by Lead)

**Annually:** Year-end archival → 13_archive/old_logs_[YYYY]/ (moved by Archivist after 3-month decay)

---

## Examples and Templates

See **operational_logging_guide.md** for:
- Detailed session_log template
- Example entries from prior research
- Blocker escalation protocol
- Finding documentation standards
- Decision recording format

---

**Next:** operational_logging_guide.md (detailed protocols), daily_log_index.md (master index)
