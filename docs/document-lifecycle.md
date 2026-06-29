# Document Lifecycle

AEWS separates information by lifecycle as well as scope.

```text
Working State -> Task -> Decision -> Knowledge -> Archive
        |
        v
Experiment
```

The direction is not strictly linear. A task can create an experiment. An experiment can produce a decision. A decision can update durable knowledge.

## Lifecycle Types

### Working State

Short-lived context needed to continue active work.

Examples:

- current branch and uncommitted intent,
- failing command and exact error,
- next concrete step,
- known blocker.

Default document: `HANDOFF.md`.

### Task

A concrete unit of work with expected output and verification.

Examples:

- implement adapter matrix,
- validate a template on a sample repo,
- remove duplicated context from an agent file.

Default document: project issue tracker or task list. AEWS does not require a specific tool.

### Decision

A durable choice with rationale and consequences.

Examples:

- use four scopes instead of two,
- keep adapters thin,
- delay automation until v0.2.

Default document: `DECISIONS.md`.

### Knowledge

Stable facts that help future work.

Examples:

- repo architecture,
- command reference,
- document placement rules,
- ownership boundaries.

Default document: `PROJECT.md`, `standard/*.md`, or dedicated docs.

### Experiment

Temporary exploration with a hypothesis, method, artifacts, and conclusion.

Examples:

- compare adapter formats across tools,
- test whether a minimal Codex `AGENTS.md` is sufficient,
- evaluate a generated template against a real repo.

Default document: `EXPERIMENT.md`.

### Archive

Information kept for record but not part of active context.

Examples:

- superseded experiments,
- old handoffs,
- rejected approaches.

Default location: `archive/` when needed. Avoid creating archive structure until there is real content to archive.

## Promotion Rules

- Working state becomes knowledge only when it is stable and reusable.
- Experiment output becomes a decision only when the conclusion changes future behavior.
- Tasks should not be copied into agent instruction files.
- Decisions should link to evidence when possible.
- Archive stale context instead of keeping it in active agent files.

## Expiration Rules

- `HANDOFF.md` should be updated at the end of active work.
- Experiment notes should include a review date or close condition.
- Adapter files should be reviewed whenever canonical document names or read order changes.
