# AGENTS.md

This file is intentionally small. The durable project knowledge lives in the AEWS canonical documents, not in this agent entrypoint.

## Read Order

1. `README.md`
2. `PROJECT.md`
3. `DECISIONS.md`
4. `HANDOFF.md` if present
5. `TODO.md` or the active task tracker if present
6. `docs/vision.md`
7. `docs/architecture.md`
8. `docs/document-lifecycle.md`
9. `docs/cross-agent-continuity.md`
10. `standard/scopes.md`
11. `standard/adapters.md`

## Working Rules

- Answer in Chinese when collaborating with the project owner.
- Keep agent-facing context minimal and task-specific.
- Do not duplicate canonical knowledge into adapter files.
- Update templates only when the lifecycle or scope rules require it.
- Treat `adapters/` as projections from `standard/`, not as independent sources of truth.
- Verify handoff claims against Git and tests before continuing another agent's
  work.

## Current Phase

AEWS v0.1.0 is published. v0.2 now has a read-only validator, an
evidence-backed adapter matrix, and an optional cross-agent continuity
protocol. Codex, Claude Code, and GitHub Copilot are the primary compatibility
targets; keep other tools available through the open adapter contract without
expanding their implementation scope. Prefer controlled compatibility evidence
before adding broader automation, hooks, or generator tools.
