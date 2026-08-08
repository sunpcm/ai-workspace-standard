# Agent Adapters

Adapters expose AEWS canonical knowledge to specific tools.

Adapters are not sources of truth. They are routing files.

## Adapter Matrix

| Tool | Typical File | Adapter Responsibility |
| --- | --- | --- |
| Codex | `AGENTS.md` | Read order, collaboration rules, repo-specific constraints |
| Claude Code | `CLAUDE.md` | Read order, commands, tool-specific workflow notes |
| GitHub Copilot | `.github/copilot-instructions.md` | Read order and IDE-side repository instructions |
| Cursor | `.cursor/rules/*.mdc` | Editor rule routing and scoped rule activation |
| Gemini CLI | `GEMINI.md` | Read order and CLI-specific expectations |

A tool may expose more than one discovery surface. GitHub Copilot reads
`.github/copilot-instructions.md` in the IDE, while Copilot coding agent can
also read a root `AGENTS.md`. Project both surfaces from the same canonical
documents instead of letting either accumulate its own knowledge.

The adapter contract is open: adoption mappings accept a lowercase tool slug
and repository-relative adapter path rather than a closed vendor enum. A
project may still designate a smaller set of primary compatibility targets and
keep other adapters as untested extension references.

## Adapter Rules

- Keep adapters short.
- Link to canonical documents instead of copying them.
- Include only tool-specific behavior in adapters.
- Review adapters when canonical document names or scope rules change.
- Do not expose private Global context in public adapter templates.
- Route participating agents to the same Handoff and task-queue roles when
  cross-agent continuity is enabled.
- Require agents to verify working-state claims against Git or other declared
  evidence before continuing.

## Minimum Adapter Content

Each adapter should contain:

1. purpose,
2. read order,
3. tool-specific rules,
4. duplication warning.

For repositories using the optional cross-agent continuity profile, an adapter
should also route to the active Handoff and task queue. The shared checkpoint
protocol belongs in `docs/cross-agent-continuity.md` or an equivalent canonical
document; do not copy a growing activity history into every adapter.

## Continuity Is Not Presence

Thin adapters can make multiple agents read the same reviewed project state.
They cannot show live file ownership, concurrent edits, or whether another
agent is still running. Those capabilities require a runtime or coordination
service and remain outside the adapter contract.

## Bad Adapter Smell

An adapter is probably too large if it includes:

- full architecture,
- full command reference,
- long coding standards,
- stale task lists,
- experiment details,
- copied decision rationale.

Move those sections back into canonical documents.
