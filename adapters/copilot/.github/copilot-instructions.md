# GitHub Copilot Instructions

This is a thin GitHub Copilot adapter for an AEWS-compatible repository.

## Read Order

1. `PROJECT.md`
2. `DECISIONS.md`
3. `HANDOFF.md` if present
4. `TODO.md` or the declared task tracker if present
5. Relevant task files

## Rules

- Prefer canonical AEWS documents.
- Keep this adapter short.
- Do not store experiment logs or long architecture notes here.
- Verify prior-agent progress against Git and tests before continuing it.
- Copilot coding agent may also read a root `AGENTS.md`. Keep both thin and
  route them to the same canonical documents.
