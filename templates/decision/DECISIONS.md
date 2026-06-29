# DECISIONS

Record accepted decisions that should influence future work.

## Template

### YYYY-MM-DD: Decision Title

Status: Accepted | Superseded | Rejected

Scope: Global | Workspace | Repo | Experiment

Context:

Decision:

Consequences:

Evidence:

## Decisions

### 2026-06-29: Use Scope First as the primary rule

Status: Accepted

Scope: Workspace

Context: Agent-specific context files become hard to maintain when they contain duplicated knowledge.

Decision: AEWS will classify information by scope and lifecycle before placing it into files.

Consequences: Adapter files should stay thin and reference canonical documents.

Evidence: `docs/scope-first.md`, `standard/adapters.md`
