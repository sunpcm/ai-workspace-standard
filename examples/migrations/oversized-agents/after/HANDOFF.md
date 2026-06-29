# HANDOFF

## Current Goal

Split the importer into parse, validate, and index stages.

## Current State

- Last completed step: parse stage extracted from the importer.
- Next step: add a validation fixture with missing title front matter.
- Blockers: link verification is slow on large example folders.

## Evidence

- `worker/`
- `examples/`
- `PROJECT.md`

## Open Questions

- Should link verification support a smaller fixture set for local iteration?

## Expiration

Archive this handoff after the importer split is complete or the task is replaced.
