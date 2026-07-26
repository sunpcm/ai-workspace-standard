# AGENTS.md

This is a thin Codex adapter for an AEWS-compatible repository.

## Read Order

1. `PROJECT.md`
2. `DECISIONS.md`
3. `HANDOFF.md` if present
4. `TODO.md` or the declared task tracker if present
5. Relevant files named by the current task

## Rules

- Keep responses concise and evidence-based.
- Prefer canonical AEWS documents over duplicated agent instructions.
- Do not expand this file with project architecture or task history.
- Verify `HANDOFF.md` against Git and tests before continuing prior work.
- Update shared progress only at a meaningful checkpoint.
