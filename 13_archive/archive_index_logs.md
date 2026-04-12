---
id: ARCHIVE-0005
type: archive/index_logs
status: active
created: 2026-04-12
last_updated: 2026-04-12
---

# Archive Index: Daily Logs

**Purpose:** Pointer index for all archived daily logs (04_daily_log/ contents after 90+ days)

**Scope:** Covers old_logs_quarterly/ subdirectory

---

## Q2 2026: daily_logs_2026-Q2 (Future)

**Status:** Not yet created (will be populated starting 2026-04-13)

**Period:** April 13 – June 30, 2026  
**Archival Trigger:** 2026-07-13 (90 days after first log created)  
**Expected Entries:** ~80 daily directories (weekdays + some weekends)  

**Destination (upon archival):**
```
13_archive/old_logs_quarterly/daily_logs_2026-Q2/
├── 2026-04-13/
│   ├── session_log_lead.md
│   ├── session_log_proof.md
│   ├── session_log_critic.md
│   ├── session_log_experiment.md
│   └── decisions_2026-04-13.md
├── 2026-04-14/
├── ...
├── 2026-06-30/
└── Q2_summary_2026.md
```

**Archive Index:** Will receive daily_logs_2026-Q2_index.md upon archival

---

## Q3 2026: daily_logs_2026-Q3 (Future)

**Status:** Not yet created (future)

**Period:** July 1 – September 30, 2026  
**Archival Trigger:** 2026-10-30 (90 days after Q3 start)  

**Destination (upon archival):**
```
13_archive/old_logs_quarterly/daily_logs_2026-Q3/
├── 2026-07-01/
├── ...
├── 2026-09-30/
└── Q3_summary_2026.md
```

---

## Quarterly Summary Reports

**Purpose:** Consolidated summary of critical decisions, findings, blockers during quarter

**Schedule:** Generated at Q-end by Archivist role

**Format:** Q?_summary_YYYY.md (e.g., Q2_summary_2026.md)

**Content:**
```markdown
# Q2 2026 Summary

## Critical Decisions Made
- [List of 🔴 CRITICAL decisions]

## Key Findings
- [Major discoveries, proofs completed, experiments]

## Blockers & Escalations
- [Unresolved issues at Q-end]

## Registry Changes
- [New D-xxxx, A-xxxx, OP-xxxx registered]

## Milestone Progress
- [M4 status, M5 planning, etc.]

## Next Quarter Priorities
- [Planned for Q3]

## Stats
- Total session logs: [N]
- Critical blockers: [N]
- Decisions made: [N]
- New registrations: [N]
```

---

## Log Archival Triggers

**Logs are archived when:**

1. **Date is ≥ 90 days old** (Q-end + buffer)
2. **No 🔴 CRITICAL decision recorded in log** (CRITICAL decisions stay active)
3. **No ongoing blocker references this log**
4. **Archivist confirms archival is safe** (Critic role reviews)

**When archiving:**
1. Move YYYY-MM-DD/ directory to old_logs_quarterly/daily_logs_Q?_YYYY/
2. Add `archived: true` to YAML headers of all files in directory
3. Add `archived_date: [archival_date]` to each file
4. Update archive_index_logs.md with quarterly summary

---

## Retrieval Examples

### Example 1: "Find decision made on 2026-05-15"

```
Query: decision from 2026-05-15
↓
Check Q2 2026 section (May is in Q2)
↓
Navigate to: 13_archive/old_logs_quarterly/daily_logs_2026-Q2/
↓
Locate: 2026-05-15/decisions_2026-05-15.md
↓
Full path: 13_archive/old_logs_quarterly/daily_logs_2026-Q2/2026-05-15/decisions_2026-05-15.md
```

### Example 2: "What critical findings from Q2?"

```
Query: key findings from April–June 2026
↓
Navigate to: 13_archive/old_logs_quarterly/daily_logs_2026-Q2/
↓
Open: Q2_summary_2026.md
↓
Section: "Key Findings" → review critical discoveries
```

### Example 3: "When did we make the K-selection decision?"

```
Query: K-selection decision date
↓
Check Q2 2026 summary or use daily_logs_2026-Q2_index.md
↓
Search: "K-selection" → find decision_YYYY-MM-DD.md with matching content
↓
Example: decisions_2026-04-13.md → F-1/M-1/MO-1 decision (Option A/B/C)
```

---

## Log Organization by Type

### Session Logs (Per Role)

**Files:** session_log_lead.md, session_log_proof.md, session_log_critic.md, session_log_experiment.md

**Frequency:** Daily (during active Phase 4)  
**Archive:** 90+ days old → old_logs_quarterly/  
**Index:** By date → Q?_YYYY directory structure  

### Decision Logs

**Files:** decisions_YYYY-MM-DD.md

**Frequency:** Daily (end of session)  
**Content:** All decisions made on date, options considered, rationale  
**Archive:** 90+ days old OR moved to Q?_summary if critical  

### Blocker Logs (As Needed)

**Files:** blockers_YYYY-MM-DD.md

**Frequency:** Created when blockers exist  
**Archive:** 90+ days old, UNLESS 🔴 CRITICAL (stays active)  

---

## Search by Phase

**Phase 4 (2026-04-13 to 2026-06-30):**
- Q2 2026: daily_logs_2026-Q2/
- 80+ daily directories
- Archive trigger: 2026-07-13

**Phase 4 continued (2026-07-01 to 2026-09-30):**
- Q3 2026: daily_logs_2026-Q3/
- 80+ daily directories
- Archive trigger: 2026-10-30

---

## Migration Checklist

**Before archival (Archivist role, end of each quarter):**

- [ ] Verify all daily logs for quarter exist in 04_daily_log/
- [ ] Count total entries (target: ~80 for typical Q)
- [ ] Create 13_archive/old_logs_quarterly/daily_logs_Q?_YYYY/ directory
- [ ] Move all YYYY-MM-DD/ directories to archive
- [ ] Create Q?_summary_YYYY.md consolidation report
- [ ] Create daily_logs_Q?_YYYY_index.md (optional, detailed index per day)
- [ ] Update archive_index_logs.md with quarterly summary
- [ ] Update archive_index.md with migration confirmation
- [ ] Add checksum verification (optional)

---

## Special Cases

### 🔴 CRITICAL Decisions

Logs containing 🔴 CRITICAL decisions may be archived, but the decision itself is:
- Replicated to canonical spec or release notes (if version-critical)
- Referenced in archive_index.md (searchable by severity)
- Linked from active decision registry (if ongoing impact)

**Action:** Archive YYYY-MM-DD/ directory, but note in Q?_summary_YYYY.md that critical decision is replicated elsewhere.

### Ongoing Blockers

If a blocker from April is still open in June:
- DO NOT archive log containing blocker
- Move to new blocker_registry.md (ongoing blockers)
- Archive only after blocker is resolved

---

## See Also

- archive_index.md (master pointer)
- archive_index_docs.md (documentation index)
- archival_policy.md (retention rules)
- 04_daily_log/operational_logging_guide.md (session log templates)
- 04_daily_log/daily_log_index.md (active daily log registry)

---

**Status:** Template created; awaiting Phase 4 start (2026-04-13)  
**Ready for:** First quarterly archival (Q2 end, 2026-07-13)  
**Maintained by:** Archivist role (Phase 4+)
