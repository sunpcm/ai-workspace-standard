# CLAUDE.md

This is a thin Claude Code adapter for an AEWS-compatible repository.

## Read Order

1. `PROJECT.md`
2. `DECISIONS.md`
3. `HANDOFF.md` if present
4. `TODO.md` or the declared task tracker if present
5. Relevant source files

## Rules

- Treat this file as routing, not canonical knowledge.
- Put durable repo facts in `PROJECT.md`.
- Put accepted rationale in `DECISIONS.md`.
- Put active continuation state in `HANDOFF.md`.
- Verify prior-agent claims against Git and tests before continuing.
- Update shared progress only at a meaningful checkpoint.
