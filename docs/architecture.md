# Architecture

AEWS has two layers:

1. Canonical workspace standard.
2. Agent-specific adapters.

The canonical layer is the source of truth. Adapters expose a minimal projection of that truth to each tool.

```text
Human / Team
    |
    v
AEWS Canonical Standard
    |
    +-- Scope model
    +-- Document lifecycle
    +-- Templates
    +-- Examples
    +-- Optional continuity protocol
    |
    v
Agent Adapters
    +-- Codex: AGENTS.md
    +-- Claude Code: CLAUDE.md, commands, hooks
    +-- Cursor: .cursor/rules
    +-- Gemini CLI: GEMINI.md
    +-- Future tools
```

## Why Four Scopes

Two layers, such as "global" and "repo", are not enough for AI engineering work. They collapse temporary experiments, cross-repo workspace conventions, and repo facts into the same files.

AEWS uses four scopes:

- Global: personal or organization-wide preferences that should rarely change.
- Workspace: rules shared by multiple repositories in one working environment.
- Repo: facts, commands, boundaries, and workflows for one repository.
- Experiment: temporary hypotheses, runs, artifacts, and conclusions.

This separation prevents context from spreading into the wrong files.

## Canonical Documents

Canonical documents are written for humans first and agents second. They should be concise, stable, and easy to verify.

Examples:

- `PROJECT.md`: durable repo facts and commands.
- `HANDOFF.md`: current working state for continuation.
- `DECISIONS.md`: accepted decisions with rationale.
- `EXPERIMENT.md`: temporary research or validation state.

## Adapter Documents

Adapter documents should answer only:

- Which canonical files should this agent read first?
- What tool-specific behavior is required?
- What should not be duplicated here?

Adapter files must stay thin. If an adapter grows large, that usually means canonical knowledge is missing or poorly scoped.

## Boundary With ECC

ECC is an agent harness: it organizes agents, skills, hooks, commands, memory, MCP, security, and cross-tool runtime behavior.

AEWS is a workspace knowledge standard. It can learn from harness design, but
runtime harness capabilities remain outside the core standard.

The ECC v2.0.0 reference evaluation confirms a shared architectural principle:
durable behavior should have one shared source and harness-specific files should
adapt only loading or platform differences. It also shows why AEWS validation
must distinguish document roles from preferred filenames and warnings from
runtime-specific exceptions.

Evidence: `examples/reference-evaluations/ecc-v2.0.0.md`

## Cross-Agent Continuity

Codex, Claude Code, and other agents can share project progress by reading the
same Project, Decisions, Handoff, and task-queue roles. Git commits, diffs, and
test artifacts remain the evidence for what actually changed.

AEWS defines the start, checkpoint, staleness, and concurrency protocol in
`docs/cross-agent-continuity.md`. It deliberately does not record vendor
transcripts, provide live presence, or lock files. A harness such as ECC may be
used as an optional handoff transport without becoming the canonical source of
project truth.

## Acceptance Criteria

- A new contributor can identify where a piece of information belongs before writing it.
- Codex, Claude Code, GitHub Copilot, Cursor, and Gemini can consume the same canonical knowledge through thin adapters.
- Two agents can identify the same current and next steps through shared
  canonical state and verify the completed work against repository evidence.
- No durable engineering fact must be copied into multiple adapter files.
- Temporary experiment notes have a clear path to become decisions, knowledge, tasks, or archive.
