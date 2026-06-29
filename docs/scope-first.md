# Scope First

Scope First is the primary AEWS rule:

> Define where information belongs before deciding what file should contain it.

## Scope Questions

Before writing new context, ask:

1. Does this apply to every project I work on?
2. Does this apply to multiple repos in one workspace?
3. Does this apply only to one repo?
4. Is this temporary experiment state?

The answer determines the scope.

## Placement Matrix

| Information | Scope | Default Placement |
| --- | --- | --- |
| Personal response language preference | Global | Personal agent config, not repo template |
| Cross-repo naming convention | Workspace | Workspace standard document |
| Repo setup command | Repo | `PROJECT.md` |
| Current failing test during active work | Repo / Working State | `HANDOFF.md` |
| Temporary benchmark result | Experiment | `EXPERIMENT.md` |
| Accepted architecture choice | Repo or Workspace | `DECISIONS.md` |

## Anti-Patterns

- Put all context into `AGENTS.md`.
- Copy the same instruction into `AGENTS.md`, `CLAUDE.md`, Cursor rules, and `GEMINI.md`.
- Keep old experiment notes in active read order.
- Write tool-specific files before defining canonical knowledge.
- Store personal habits inside an open-source repo template.

## Review Checklist

- Can this information be assigned to exactly one scope?
- Is the information stable enough for a durable document?
- If temporary, does it have a close condition?
- If agent-specific, is the canonical source linked or obvious?
