---
type: dashboard
status: active
cluster: lab
id: LAB_DASHBOARD
last_updated: 2026-05-14
description: Dataview 중심의 SCC 연구 랩 진입 화면.
cssclasses:
  - research-lab
---

# Research Lab Dashboard

> [!nav] Authority
> [[THEORY_INDEX]] · [[canonical|canonical]] · [[theorem_status|theorem_status]] · [[hypothesis_tree|hypothesis_tree]] · [[CHANGELOG|CHANGELOG]]

> [!status] Current posture
> Canonical authority remains in `THEORY/canonical/`; active reasoning moves through `THEORY/working/`; session history stays in `THEORY/logs/`. This dashboard indexes the system without changing the theory files.

## Authority Files

```dataview
TABLE type, status, cluster, last_updated AS updated, description
FROM "Perception_theory"
WHERE file.path = "Perception_theory/THEORY_INDEX.md"
   OR file.path = "Perception_theory/THEORY/2_substrate/canonical/canonical.md"
   OR file.path = "Perception_theory/THEORY/2_substrate/canonical/theorem_status.md"
   OR file.path = "Perception_theory/THEORY/2_substrate/canonical/hypothesis_tree.md"
   OR file.path = "Perception_theory/THEORY/CHANGELOG.md"
SORT file.path ASC
```

## Active Working Notes

```dataview
TABLE status, type, last_updated AS updated, file.mtime AS modified
FROM "Perception_theory/THEORY/working"
WHERE !contains(file.path, "/_archive/")
SORT file.mtime DESC
LIMIT 24
```

## Recent Logs

```dataview
TABLE type, status, file.folder AS folder, file.mtime AS modified
FROM "Perception_theory/THEORY/logs"
SORT file.mtime DESC
LIMIT 18
```

## Open Tasks

```dataview
TASK
FROM "Perception_theory"
WHERE !completed
SORT file.mtime DESC
LIMIT 40
```

## Experiments And Validation

> [!nav] Entry points
> [[MOC_experiments_validation|MOC_experiments_validation]] · [[CODE/README|CODE README]] · `CODE/experiments/` · `CODE/results/`

```dataview
TABLE file.folder AS folder, file.mtime AS modified
FROM "Perception_theory/CODE"
WHERE contains(file.path, "experiments")
   OR contains(file.path, "results")
   OR contains(file.path, "README.md")
SORT file.mtime DESC
LIMIT 24
```

## Plugin Tiers

| Tier | Plugins | Use |
| --- | --- | --- |
| Core research | Dataview, Omnisearch, Tasks, Advanced Tables, Templater, Calendar, Metadata Menu, Minimal, Style Settings, Git | Search, index, task flow, tables, templates, visual baseline, manual backup |
| Supporting | PDF++, Excalidraw, Breadcrumbs | PDF reading, diagrams, relation navigation |
| Dormant | Zotero Integration, Citations, Pretty BibTeX, Annotator, Juggl, Kanban, CardBoard, Editing Toolbar | Kept installed but not active in this configuration |
