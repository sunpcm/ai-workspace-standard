# AGENTS.md

This file is intentionally small. The durable project knowledge lives in the AEWS canonical documents, not in this agent entrypoint.

## Read Order

1. `README.md`
2. `PROJECT.md`
3. `DECISIONS.md`
4. `HANDOFF.md` if present
5. `docs/vision.md`
6. `docs/architecture.md`
7. `docs/document-lifecycle.md`
8. `standard/scopes.md`
9. `standard/adapters.md`

## Working Rules

- Answer in Chinese when collaborating with the project owner.
- Keep agent-facing context minimal and task-specific.
- Do not duplicate canonical knowledge into adapter files.
- Update templates only when the lifecycle or scope rules require it.
- Treat `adapters/` as projections from `standard/`, not as independent sources of truth.

## Current Phase

AEWS v0.1.0 is published. v0.2 has a first read-only validator backed by two
reference evaluations and dependency-free fixtures. Prefer strengthening
evidence and compatibility reporting before adding broader automation, hooks,
or generator tools.
