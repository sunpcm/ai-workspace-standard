# GitHub Copilot Instructions

This file is intentionally small. The durable project knowledge lives in the
AEWS canonical documents, not in this agent entrypoint.

## Read Order

1. `README.md`
2. `PROJECT.md`
3. `DECISIONS.md`
4. `HANDOFF.md` if present
5. `TODO.md` or the active task tracker if present
6. `standard/scopes.md`
7. `standard/adapters.md`

## Working Rules

- Answer in Chinese when collaborating with the project owner.
- Keep agent-facing context minimal and task-specific.
- Do not duplicate canonical knowledge into adapter files.
- Treat `adapters/` as projections from `standard/`, not as independent sources
  of truth.
- Verify handoff claims against Git and tests before continuing another agent's
  work.
