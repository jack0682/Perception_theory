---
id: ARCHIVE-0002
type: archive/policy
status: active
created: 2026-04-12
---

# Archival Policy: Retention, Migration, Purge

**Purpose:** Define criteria and timelines for archiving, retention, and purging of documents.

---

## Retention Categories

### Category 1: Permanent Retention (Never Archive)

**Items:** Constitutional foundation, canonical specifications, immutable registries

| Item Type | Location | Retention | Reason |
|-----------|----------|-----------|--------|
| Canonical Spec | 01_canonical/ | ♾️ | Authoritative theory record |
| Constitutional Layer | 00_meta/ | ♾️ | Project governance |
| Registries | 03_context_memory/ | ♾️ | Immutable knowledge base |
| Master Problem Map | 02_roadmap/ | ♾️ | Research direction |
| Milestones | 02_roadmap/milestones/ | ♾️ | Project history |

**Action:** Never archive these items. Keep in active tree permanently.

---

### Category 2: Immediate Archival (Upon Creation)

**Items:** Pre-release versions, retracted theorems, deprecated documents

| Item Type | Example | Timeline | Archive Destination |
|-----------|---------|----------|---------------------|
| Pre-v1.0 specs | canonical_version_0.9.md | Immediate | deprecated_versions/ |
| Retracted theorems | Type A/B classification | Immediate | deprecated_versions/deprecated_theorems.md |
| Superseded release notes | v1.0 release note (after v1.1) | Upon v1.1 release | deprecated_versions/ |
| Draft versions | canonical_v1.2_draft.md | Upon final release | deprecated_versions/ |

**Criteria for immediate archival:**
- Version explicitly superseded by newer version
- Theorem explicitly retracted by audit
- Document marked `status: deprecated` in YAML header

**Action:** Move to 13_archive/deprecated_versions/ within 1 day of deprecation.

---

### Category 3: Time-Based Archival (3+ Months Old)

**Items:** Daily logs, iteration documents, temporary working files

| Item Type | Retention Period | Archive Destination | Trigger |
|-----------|------------------|---------------------|---------|
| Daily logs (04_daily_log/) | 3 months | old_logs_quarterly/ | Q-end or 90 days |
| Iteration docs (docs/) | 3 months | old_docs_migrated/ | After next major version |
| Experiment results | 6 months | experiments_archive/ | S-end or 180 days |
| Weekly summaries | 3 months | old_logs_quarterly/ | Q-end |

**Criteria for time-based archival:**
- Created date is ≥ 90 days ago (for logs)
- Created date is ≥ 6 months ago (for results)
- NOT mentioned in active milestone
- NO 🔴 CRITICAL decisions recorded in document

**Action:** Move to 13_archive/ subdirectory on schedule (quarterly for logs, as-needed for results).

---

### Category 4: Conditional Archival (On Demand)

**Items:** Experimental data, analysis reports, development notes

| Item Type | Archive Condition | Archive Destination |
|-----------|-------------------|---------------------|
| Exp results | After validation in higher-level proof | experiments_archive/ |
| Analysis reports | After summarized in higher-level document | old_docs_migrated/ |
| Dev notes | After feature implemented & tested | [same as source category] |

**Criteria for conditional archival:**
- Content is captured in higher-level document
- Information is no longer actionable
- User explicitly requests archival
- Item explicitly marked `status: archived` in YAML header

**Action:** Archive on request or when condition met; document reason in archival_policy.md entry.

---

## Archival Procedures

### Procedure 1: Immediate Deprecation Archival

**When:** New spec version released, theorem retracted, or item marked deprecated

**Steps:**
1. Add metadata to deprecated item:
   ```yaml
   archived: true
   archived_date: [today]
   archival_reason: "Superseded by [item]" OR "Invalidated by [exp/audit]"
   deprecated_by: "[new item]"
   deprecation_notice: "See [location] for replacement"
   ```

2. Move file to 13_archive/deprecated_versions/

3. Create pointer in active tree (if visible reference needed):
   ```
   ⚠️ **DEPRECATED:** This version has been superseded. See [current version](../01_canonical/canonical_latest.md).
   ```

4. Update archive_index.md

5. Create deprecation entry in release notes of new version

---

### Procedure 2: Quarterly Time-Based Archival

**When:** Quarter ends (2026-06-30, 2026-09-30, etc.) OR Archivist determines 90+ days elapsed

**Trigger:** Archivist role (from Phase 4 daily logs)

**Steps:**
1. Identify all files with `created: YYYY-MM-DD` where date ≥ 90 days old
2. Check conditions: NOT in active milestone, NO 🔴 CRITICAL decisions
3. For each candidate:
   - Add `archived: true` to YAML header
   - Add `archived_date: [today]`
   - Add `archival_reason: "Time-based archival (3+ months old)"`
   - Move to appropriate 13_archive/subdirectory

4. Create migration_index_YYYY-MM-DD.md with full inventory:
   ```markdown
   # Migration Index: YYYY-MM-DD

   **Migration date:** YYYY-MM-DD
   **Files archived:** [N]
   **Destination:** 13_archive/old_logs_quarterly/ OR old_docs_migrated/
   
   | Original Path | New Path | Created Date | Reason |
   |...
   ```

5. Update archive_index.md with migration summary

6. Create Q?_summary_YYYY.md quarterly consolidation report

---

### Procedure 3: Conditional On-Demand Archival

**When:** User requests, or condition becomes true, or item explicitly marked

**Steps:**
1. Verify archival condition is met
2. Document reason in YAML header:
   ```yaml
   archived: true
   archived_date: [today]
   archival_reason: "[specific condition]"
   superseded_by: "[higher-level document]"
   ```

3. Move to appropriate 13_archive/subdirectory

4. Update archive_index.md

5. Create deprecation notice in active tree if visible reference needed

---

## Non-Archival Conditions

**DO NOT ARCHIVE if ANY of these conditions are true:**

- [ ] Document is in 00_meta/ (constitutional layer)
- [ ] Document is in 01_canonical/ (canonical specs)
- [ ] Document is in 03_context_memory/ (immutable registries)
- [ ] Document is in 02_roadmap/milestones/ (milestone definitions)
- [ ] Document contains 🔴 CRITICAL decisions or findings
- [ ] Document is referenced in active milestone with status `in_progress`
- [ ] User explicitly marks `archived: false` or `keep_active: true`
- [ ] Document is actively being edited (status: `active` and created within 30 days)

**If ANY of above is true:** Keep document in active tree.

---

## Purge Policy

### Conservative Approach: Archive Forever, Never Purge

**Current policy:** All archived items are retained indefinitely.

**Rationale:**
- Storage is cheap
- Historical reference is valuable
- No information loss risk
- Future research may need old data

**Action:** NEVER purge archived items without explicit executive decision.

---

## Archive Lifecycle Example: Daily Logs

**Timeline:**

| Date | Phase | Item Status | Location |
|------|-------|-------------|----------|
| 2026-04-13 | 4 | Created | 04_daily_log/2026-04-13/ |
| 2026-04-13 to 2026-06-30 | 4 | Active (in use, referenced) | 04_daily_log/2026-04-13/ |
| 2026-06-30 | 5 | 78+ days old | 04_daily_log/2026-04-13/ (still active) |
| 2026-07-13 | 5 | 90 days old → archive trigger | → 13_archive/old_logs_quarterly/daily_logs_2026-Q2/2026-04-13/ |
| 2026-07-13+ | Archive | Historical reference | 13_archive/old_logs_quarterly/ (indexed) |
| ♾️ | — | Permanent retention | No purge date |

**Key moments:**
- **Transition point:** 90 days after creation (Q-end or +90 days, whichever earlier)
- **Archival:** Move with full metadata + migration index
- **Retrieval:** Via archive_index.md → archive_index_logs.md → Q?_summary → daily log directory
- **Retention:** Indefinite (never purged)

---

## Archival Metadata Standards

Every archived item must include:

```yaml
archived: true
archived_date: YYYY-MM-DD
archival_reason: [one of: "Immediate deprecation", "Time-based (90+ days)", "Superseded by X", "On-demand user request"]
original_location: /path/to/original/location
new_location: 13_archive/subdirectory/path
created: YYYY-MM-DD [original creation date, preserve]
last_modified: YYYY-MM-DD [before archival]
migration_index: archive_index.md or specific migration_index_YYYY-MM-DD.md
related_items: [comma-separated list of related active or archived items]
retrieval_instructions: "See [index file] → [subdirectory] → [filename]"
deprecation_notice: "[if applicable; what replaces this item]"
```

---

## Archive Organization by Archival Reason

### By Reason: Immediate Deprecation
- **Pattern:** Versions, retracted theorems, marked deprecated
- **Location:** 13_archive/deprecated_versions/
- **Index:** archive_index.md (deprecated_theorems section)
- **Lifespan:** Created → Archived immediately

### By Reason: Time-Based Expiry
- **Pattern:** 90+ day old logs, documents, iteration notes
- **Location:** 13_archive/old_logs_quarterly/, 13_archive/old_docs_migrated/
- **Index:** archive_index_logs.md, archive_index_docs.md
- **Lifespan:** Created → 90 days → Archived (quarterly batch)

### By Reason: Results Archival
- **Pattern:** Experimental results, analysis reports
- **Location:** 13_archive/experiments_archive/
- **Index:** experiments_archive_index.md
- **Lifespan:** Created → 6 months → Archived (or on-demand if obsolete)

### By Reason: Reference PDFs
- **Pattern:** Exported papers, PDF versions of specs
- **Location:** 13_archive/reference_pdfs/
- **Index:** archive_index.md (PDF section)
- **Lifespan:** Created → Retained indefinitely

---

## Key Dates & Timeline

| Date | Event | Action |
|------|-------|--------|
| **2026-04-12** | Archival framework created | README.md, archival_policy.md |
| **2026-04-13+** | Phase 4 operational logging begins | Start 04_daily_log/YYYY-MM-DD/ |
| **2026-06-30** | Q2 ends | Move Q2 logs to old_logs_quarterly/ |
| **2026-07-12** | docs/ ready for migration | Move docs_2026-03-26_to_2026-04-12/ |
| **2026-09-30** | Q3 ends | Move Q3 logs to old_logs_quarterly/ |
| **2026-10-12** | Archivist review | Check for on-demand archival requests |
| ♾️ | Ongoing | Quarterly consolidation, on-demand archival |

---

## Responsibilities

| Role | Responsibility |
|------|-----------------|
| **User** | Request archival of specific items (conditional on-demand) |
| **Archivist** (Phase 4) | Implement time-based archival quarterly; maintain archive_index.md |
| **Lead** (Phase 4) | Approve conditional archival requests |
| **Critic** (Phase 4) | Audit archival to ensure no critical items archived accidentally |

---

## See Also

- 13_archive/README.md (archival overview)
- 13_archive/archive_index.md (master pointer index)
- 02_roadmap/04_daily_log/operational_logging_guide.md (Archivist role procedures)

---

**Last updated:** 2026-04-12  
**Effective:** 2026-04-13 (when Phase 4 begins and first items become eligible for archival)
