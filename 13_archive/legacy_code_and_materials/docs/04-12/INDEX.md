# 04-12 Index

**Date:** 2026-04-12
**Focus:** fixed-protocol theorem lane after the H4-vs-fixed-protocol decision

---

## 1. Proof Notes

| File | Description | Status |
|---|---|---|
| `proof/FIXED-PROTOCOL-BASIN-ACCESS-THEOREM-CANDIDATE.md` | Protocol-tagged theorem candidate with raw-entry, seeded-entry, and protocol-gap quantities | active |

## 2. Audit Notes

| File | Description | Status |
|---|---|---|
| `audit/Q2-VS-Q4-LANE-DECISION.md` | Chooses the protocol-comparison gap before the harder raw-entry upper-bound lane | complete |
| `proof/FIXED-PROTOCOL-ACCESSIBILITY-GAP-STATEMENT.md` | Introduces the protocol-gap quantity and states the strongest current theorem-support reading | active |
| `audit/ASTAR-VS-UB-LANE-DECISION.md` | Chooses sharpening the target neighborhood before choosing the theorem-usable accessibility surrogate | complete |
| `proof/UB-NEIGHBORHOOD-DEFINITION.md` | Proposes a theorem-facing neighborhood for the target branch family using family-distance plus energy tolerance | active |
| `audit/DISTFAMILY-VS-ENERGY-CAPTURE-DECISION.md` | Chooses energy/capture formalization before the harder branch-family metric formalization | complete |\n| `proof/ENERGY-CAPTURE-CRITERION.md` | Formalizes the energy tolerance and capture side of the theorem-facing neighborhood | active |\n| `proof/WEAKEST-USEFUL-DISTFAMILY-NOTION.md` | Argues that the theorem lane only needs a local target-family pseudodistance, not a global branch metric | active |
| `proof/LOCAL-TARGET-FAMILY-PSEUDODISTANCE-INGREDIENTS.md` | Lists the minimum ingredients for a theorem-serving local target-family pseudodistance | active |
| `audit/ANCHOR-VS-VALIDITY-DECISION.md` | Chooses target representative and identifications before validity/exclusion refinement | complete |
| `proof/TARGET-REPRESENTATIVE-AND-IDENTIFICATIONS.md` | Fixes the anchor representative and minimum allowed identifications for the local pseudodistance | active |
| `proof/LOCAL-VALIDITY-AND-EXCLUSION-RULE.md` | Formalizes the local chart range and wrong-family exclusion side of the target pseudodistance | active |
| `proof/CONSOLIDATED-LOCAL-NEIGHBORHOOD-STATEMENT.md` | Merges anchor, validity, energy/capture, and exclusion into one theorem-facing local neighborhood template | active |
| `audit/BRANCHDISTANCE-VS-ASTAR-DECISION.md` | Chooses accessibility-surrogate refinement before more branch-distance polishing | complete |
| `proof/WEAKEST-USEFUL-ASTAR-SURROGATE.md` | Defines accessibility as protocol-tagged entry probability into the local target neighborhood | active |
| `audit/ENTRY-EVENT-VS-HORIZON-DECISION.md` | Chooses formalizing the entry event before the protocol horizon/stopping rule | complete |
| `proof/ENTRY-EVENT-DEFINITION.md` | Defines entry into the theorem-facing local neighborhood as the core event of the accessibility surrogate | active |
| `proof/PROTOCOL-HORIZON-AND-STOPPING-RULE.md` | Fixes the protocol-native finite horizon used by the accessibility surrogate | active |
| `proof/FINALIZED-FIXED-PROTOCOL-ASTAR-STATEMENT.md` | Merges the entry event and protocol-native finite horizon into one compact accessibility surrogate | active |
| `audit/STABLE-ENTRY-VS-NORMALIZED-HORIZON-DECISION.md` | Chooses strengthening the event side before normalizing horizons | complete |
| `proof/STABLE-ENTRY-CRITERION.md` | Strengthens the accessibility event from first-hit to a local stable-entry notion | active |
| `audit/PROTOCOL-NATIVE-VS-NORMALIZED-HORIZON-DECISION.md` | Chooses to keep the protocol-native finite horizon before introducing any normalized stopping notion | complete |
| `proof/PROTOCOL-NATIVE-HORIZON-SUFFICIENCY.md` | Argues that the protocol-native finite horizon is sufficient for the current theorem lane | active |
| `audit/ARAW-VS-ASEED-VS-GAP-DECISION.md` | Chooses the direct protocol-gap inequality before one-sided accessibility bounds | complete |
| `proof/DIRECT-PROTOCOL-GAP-BOUND-TEMPLATE.md` | States the weakest useful direct-gap inequality template for the accessibility surrogate | active |
| `audit/ARAW-UPPER-VS-ASEED-LOWER-DECISION.md` | Chooses the raw upper-bound route before the seeded lower-bound route | complete |
| `proof/ARAW-UPPER-BOUND-TEMPLATE.md` | States the weakest useful upper-bound template for raw accessibility | active |
| `audit/EPSRAW-BRANCHDISTANCE-VS-ENERGYCAPTURE-DECISION.md` | Chooses branch-distance exclusion before energy/capture as the first control on `eps_raw` | complete |
| `proof/BRANCH-DISTANCE-EXCLUSION-TEMPLATE.md` | States the weakest useful branch-distance-exclusion template for the raw upper bound | active |
| `proof/SYMBOLIC-LOCAL-CHART-EXCLUSION-CONDITION.md` | Rewrites strict branch-distance exclusion as a pathwise local-chart exclusion condition | active |
| `proof/ASEED-LOWER-BOUND-TEMPLATE.md` | States the weakest useful lower-bound template for seeded accessibility | active |
| `proof/DELTA-ACCESS-COMBINATION-PATTERN.md` | Combines the one-sided accessibility bounds into a lower-bound template for the direct protocol gap | active |
| `audit/EPSRAW-VS-ETASEED-POSITIVITY-DECISION.md` | Chooses shrinking eps_raw before strengthening eta_seed in the positivity route | complete |
| `proof/EPSRAW-STRUCTURAL-CONTROL-NOTE.md` | Asks for the weakest useful structural control that makes eps_raw small | active |
| `audit/ALL-ITERATE-VS-SAMPLED-EXCLUSION-DECISION.md` | Chooses sampled/checkpointed raw exclusion before all-iterate exclusion | complete |
| `proof/SAMPLED-RAW-EXCLUSION-PRINCIPLE.md` | States the evidence-aligned raw obstruction principle at the sampled/checkpointed level | active |
| `proof/EPSRAW-POSITIVITY-ROLE-NOTE.md` | Explains how sampled raw exclusion sharpens the role of eps_raw in the positivity condition | active |
| `audit/ETASEED-VS-EPSRAW-REFINEMENT-DECISION.md` | Chooses strengthening the seeded floor before further sharpening the raw ceiling | complete |
| `proof/ETASEED-STRUCTURAL-SUPPORT-NOTE.md` | States the weakest useful structural support for a positive seeded-access floor | active |
| `proof/CLEAN-ETASEED-EPSRAW-COMPARISON.md` | States the cleanest theorem-facing comparison between the seeded access floor and raw obstruction ceiling | active |
