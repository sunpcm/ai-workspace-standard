# HANDOFF

## Current Goal

Verify that Codex and Claude Code load separate thin adapters and continue from
one shared AEWS checkpoint.

## Current State

- Updated by: AEWS runtime fixture
- Updated at: 2026-07-26
- Branch or worktree: isolated temporary copy
- Last verified commit: supplied by the evidence record
- Last completed step: prepared the static fixture
- Next step: record both read-only runtime-loading results
- Blockers: none

## Evidence

- `PROJECT.md`
- `DECISIONS.md`
- `TODO.md`
- tool-specific startup marker supplied through the automatically loaded adapter

## Open Questions

- None.

## Expiration

Replace this checkpoint when the adapter discovery contract changes.
