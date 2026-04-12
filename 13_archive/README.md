---
id: ARCHIVE-0001
type: archive/readme
status: active
created: 2026-04-12
---

# Archive Layer (13_archive/)

**Purpose:** Centralized storage for retired, migrated, and historical documentation.

**Scope:** Contains only items 3+ months old OR explicitly deprecated/superseded by newer versions.

---

## Archive Subdirectories

```
13_archive/
├── README.md (this file)
├── archive_index.md (master index, updated quarterly)
├── archival_policy.md (retention, retention periods, purge criteria)
│
├── old_docs_migrated/
│   ├── docs_2026-03-26_to_2026-04-12/
│   │   ├── iteration_01_0326_*.md
│   │   ├── iteration_02_0329_*.md
│   │   ├── [... up to iteration_12_0412]
│   │   └── migration_index_2026-04-12.md
│   │
│   ├── docs_2026-04-13_to_2026-07-12/
│   │   └── [future: quarterly migrations]
│   │
│   └── archive_index_docs.md (pointer index)
│
├── old_logs_quarterly/
│   ├── daily_logs_2026-Q2/
│   │   ├── 2026-04-13_to_2026-06-30/
│   │   │   ├── 2026-04-13/
│   │   │   ├── 2026-04-14/
│   │   │   └── [... daily directories]
│   │   └── Q2_summary_2026.md
│   │
│   └── archive_index_logs.md (pointer index)
│
├── deprecated_versions/
│   ├── canonical_version_0.9.md (pre-v1.0 baseline)
│   ├── canonical_version_1.0_draft.md (draft versions)
│   └── deprecated_theorems.md (retracted/superseded theorems)
│
├── experiments_archive/
│   ├── exp_001_to_035.md (single-formation validation, archived after v1.2)
│   ├── exp_036_to_063.md (K-field investigation, archived after audit)
│   └── experiments_archive_index.md
│
└── reference_pdfs/
    ├── [PDF versions of canonical specs]
    └── [exported papers & supplementary materials]
```

---

## Archival Timeline

### Immediate (Phase 5: 2026-04-12 onwards)

**Trigger:** M3 validation complete; Phase 4 operational logging begins

**Actions:**
1. Create 13_archive/ directory structure ✅
2. Move docs/ (all iterations 2026-03-26 to 2026-04-12) → old_docs_migrated/docs_2026-03-26_to_2026-04-12/
3. Create archival index & migration documentation
4. **DO NOT delete originals yet** (keep during Phase 4 for reference)

### Quarterly (Every 3 months)

**Trigger:** End of quarter (2026-06-30, 2026-09-30, etc.)

**Actions:**
1. Move daily_log/ (3 months old) → old_logs_quarterly/
2. Archive old experimental results → experiments_archive/
3. Create quarterly summary report
4. Update archive_index.md

### On Demand (When deprecated)

**Trigger:** Theorem retraction, major reformulation, version obsolescence

**Actions:**
1. Move deprecated item to deprecated_versions/
2. Document reason for deprecation
3. Create deprecation notice (link from canonical spec)

---

## Archive Access

### Finding Archived Items

1. **By date:** archive_index_docs.md, archive_index_logs.md
2. **By type:** deprecation index, experiments index
3. **By reason:** archival_policy.md (search by retention category)

### Citing Archived Items

**Format:** `@archive:ARCHIVE-XXXX-YY` (item ID + archive date)

**Example:** `@archive:docs_2026-03-26_to_2026-04-12` (Q1 iteration docs)

### Retrieving Archived Items

1. Check archive_index.md (master pointer)
2. Navigate to subdirectory (old_docs_migrated/, old_logs_quarterly/, etc.)
3. Locate migration_index_YYYY-MM-DD.md (detailed item listing)

---

## Retention Policy

### Documents Archived Immediately (Upon Creation)

- **Pre-v1.0 versions** → deprecated_versions/
- **Retracted theorems** → deprecated_versions/deprecated_theorems.md
- **Superseded release notes** → deprecated_versions/

### Documents Archived After 3 Months

- Daily logs (YYYY-MM-DD/) after 90 days
- Iteration documents (after next major version)
- Deprecated experimental results

### Documents Never Archived

- Canonical specifications (v1.0, v1.1, v1.2, etc.) — kept in 01_canonical/ permanently
- Immutable registries (concept, symbol, theorem, assumption) — kept in 03_context_memory/ permanently
- Active problem maps & dependencies — kept in 02_roadmap/ permanently
- Constitutional layer (00_meta/) — kept in 00_meta/ permanently

### Purge Policy

**Never purge without explicit approval.** All archived items are retained indefinitely for historical reference.

---

## Archive Metadata

Each archived item includes:

```yaml
archived_date: YYYY-MM-DD
original_location: [path in main tree]
archival_reason: [immediate deprecation | expired retention | quarterly consolidation | user request]
retrieval_instructions: [how to find and use this item]
deprecation_notice: [if applicable; link to replacement]
related_items: [other archived items or active documents related to this]
```

---

## Archive Index Files

### archive_index.md (Master)
- Complete listing of all archived items
- Organized by subdirectory & date
- Updated quarterly or upon new archival

### archive_index_docs.md (Docs only)
- Pointer to all docs_YYYY-MM-DD_to_YYYY-MM-DD/ subdirectories
- Iteration-level detail (01, 02, ..., 12)
- Links to migration_index files

### archive_index_logs.md (Daily logs only)
- Pointer to all daily log quarters
- Summary of key decisions/blockers archived
- Links to Q?_summary_YYYY.md files

### migration_index_YYYY-MM-DD.md (Per-migration detail)
- Line-by-line listing of all files moved
- Original paths → archive paths
- Checksum verification

---

## Current Status

| Subdirectory | Status | Contents | Last Updated |
|--------------|--------|----------|--------------|
| old_docs_migrated/ | ⏳ READY | Docs 2026-03-26 to 2026-04-12 (awaiting migration) | 2026-04-12 |
| old_logs_quarterly/ | 📋 READY | Will receive daily logs after 2026-07-12 | N/A |
| deprecated_versions/ | 📋 READY | Will receive deprecated items on demand | N/A |
| experiments_archive/ | 📋 READY | Will receive archived exp results | N/A |
| reference_pdfs/ | 📋 READY | For future PDF exports | N/A |

---

## Phase 5 Milestones

### M5a: Documentation Migration (2026-04-13 onwards)

**Trigger:** Direction decision (F-1/M-1/MO-1 Option A/B/C) made

**Actions:**
1. Move docs/ → old_docs_migrated/docs_2026-03-26_to_2026-04-12/
2. Create migration_index_2026-04-12.md with full inventory
3. Update archive_index.md
4. Create deprecation notices in 01_canonical/ if any versions deprecated

**Timeline:** 1–2 days

### M5b: Experiment Organization (2026-04-13 onwards)

**Trigger:** Phase 4 operational logging begins

**Actions:**
1. Create 09_experiments/ directory (primary experiments tree)
2. Move experiments/ → 09_experiments_legacy/ OR reorganize as needed
3. Create experiment registry (by exp_ID, by category, by theorem)
4. Archive old experiment results → experiments_archive/

**Timeline:** 2–3 days

### M5c: Results & Data Organization (2026-04-13 onwards)

**Trigger:** Same as M5b

**Actions:**
1. Create 10_results/ directory (primary results tree)
2. Move results/ → 10_results_legacy/ OR reorganize
3. Create results index (by date, by category, by relevance)
4. Establish data retention policy (which results to archive, which to keep active)

**Timeline:** 2–3 days

---

## Archival Procedures

### Archiving a Document

1. **Add metadata** to document YAML header:
   ```yaml
   archived: true
   archived_date: YYYY-MM-DD
   archival_reason: [reason]
   new_location: [13_archive/subdirectory/path]
   ```

2. **Move file** to 13_archive/subdirectory/

3. **Create pointer** in active tree (if visible reference needed):
   ```markdown
   *This document has been archived. See [archived version](../13_archive/...)*
   ```

4. **Update archive_index.md** with new entry

### Retrieving an Archived Document

1. **Search archive_index.md** by date or filename
2. **Check migration_index_YYYY-MM-DD.md** for exact path
3. **Navigate to 13_archive/subdirectory/path/filename**

### Unarchiving an Item

Rare, but possible if an archived item becomes relevant again:

1. **Move file** back to original location (or new location)
2. **Remove** `archived: true` from YAML header
3. **Update archive_index.md** (remove entry)
4. **Update** source directory index

---

## Integration with Daily Logs (Phase 4)

**Archivist role (Phase 4) responsibilities:**
- After 3 months, move daily logs from 04_daily_log/YYYY-MM-DD/ → 13_archive/old_logs_quarterly/
- After 3 months, archive experimental results → 13_archive/experiments_archive/
- Quarterly: Create Q?_summary_YYYY.md consolidation report
- Update archive_index.md with new entries

---

## See Also

- archival_policy.md (detailed retention & purge criteria)
- archive_index.md (master pointer index)
- 04_daily_log/README.md (daily logging that feeds archival)
- 02_roadmap/04_daily_log/operational_logging_guide.md (Archivist role procedures)

---

**Last updated:** 2026-04-12  
**Ready for:** Phase 5 execution (after direction decision 2026-04-13)
