# 2026-04-W5 — Not Opened (Reverted to W4 Extended Close)

**Status:** Placeholder. W5 was not actually opened.

## What happened

Initially (2026-04-26 morning), this directory was created when 04-26 was treated as
"W5 Day 1" — first day of the new week per the standard weekly rotation rule.
A skeleton `weekly_draft_storming.md` was drafted with W5 entry state and 04-26 entry.

Mid-session (2026-04-26), user direction reverted this:

> "아직 내용은 전부 W4로 간주해"

The 04-26 work (V5b verification cycle: NQ-170 → NQ-172 → NQ-170b → NQ-170c) is
**part of W4 extended close**, not W5 Day 1. W4 weekly scope extended:

- Original W4: 2026-04-19 ~ 2026-04-25 (7 days)
- Extended W4: 2026-04-19 ~ 2026-04-26 (8 days)

## Where the actual work lives

- `THEORY/logs/daily/2026-04-26/*.md` — daily session artifacts (W4 final day, NOT W5).
- `THEORY/logs/weekly/2026-04-W4/weekly_draft_storming.md` — W4 buffer with 04-26 entry appended.
- `THEORY/logs/weekly/2026-04-W4/weekly_summary.md` — W4 closing summary (updated 2026-04-26 to include extended-close V5b verification).

## When does W5 actually start

W5 starts whenever user opens it explicitly (likely 2026-04-27 or after final V5b
canonical merge decision). At that point:
- `weekly_draft_storming.md` will be created in `2026-04-W5/` (replacing the
  reverted skeleton).
- This README will be removed or updated.

## Skeleton draft retained

The previously-drafted `weekly_draft_storming.md` skeleton is retained in this
directory as historical record (reverted to draft status). Contents that need
to live in W4 are mirrored to `2026-04-W4/weekly_draft_storming.md`.
