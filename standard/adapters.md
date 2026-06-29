# Agent Adapters

Adapters expose AEWS canonical knowledge to specific tools.

Adapters are not sources of truth. They are routing files.

## Adapter Matrix

| Tool | Typical File | Adapter Responsibility |
| --- | --- | --- |
| Codex | `AGENTS.md` | Read order, collaboration rules, repo-specific constraints |
| Claude Code | `CLAUDE.md` | Read order, commands, tool-specific workflow notes |
| Cursor | `.cursor/rules/*.mdc` | Editor rule routing and scoped rule activation |
| Gemini CLI | `GEMINI.md` | Read order and CLI-specific expectations |

## Adapter Rules

- Keep adapters short.
- Link to canonical documents instead of copying them.
- Include only tool-specific behavior in adapters.
- Review adapters when canonical document names or scope rules change.
- Do not expose private Global context in public adapter templates.

## Minimum Adapter Content

Each adapter should contain:

1. purpose,
2. read order,
3. tool-specific rules,
4. duplication warning.

## Bad Adapter Smell

An adapter is probably too large if it includes:

- full architecture,
- full command reference,
- long coding standards,
- stale task lists,
- experiment details,
- copied decision rationale.

Move those sections back into canonical documents.
