# AI Engineering Workspace Standard

AI Engineering Workspace Standard (AEWS) is a minimal, agent-agnostic standard for organizing engineering knowledge so it can be consumed by Codex, Claude Code, Cursor, Gemini CLI, and future agents without binding the workspace to one vendor.

AEWS treats the workspace as the durable asset. Agent-specific files are projections of the standard, not the source of truth.

## Goals

- Keep engineering context small, precise, and task-relevant.
- Define where knowledge belongs before writing it.
- Separate canonical workspace knowledge from agent-specific adapters.
- Make handoffs, decisions, experiments, and repo facts easy to maintain.
- Avoid copying the same knowledge across multiple agent tools.
- Let multiple agents resume the same project state through a shared,
  evidence-backed checkpoint protocol.

## Non-Goals

- AEWS is not an ECC clone.
- AEWS is not an agent runtime, hook system, MCP catalog, or security harness.
- AEWS is not a collection of large `AGENTS.md`, `CLAUDE.md`, or editor rule files.
- AEWS does not replace project documentation, tests, CI, or operational runbooks.

## Core Principle

Scope first:

1. Decide whether the information is Global, Workspace, Repo, or Experiment scope.
2. Decide whether it is Knowledge, Decision, Task, Working State, or Archive.
3. Only then decide which document or adapter should expose it.

## Repository Layout

```text
docs/                 Human-readable design documents
standard/             Canonical AEWS model and rules
templates/            Minimal document templates
examples/             Small reference workspaces
adapters/             Agent-specific projections
PROJECT.md            Durable facts for this repo
DECISIONS.md          Accepted project decisions
HANDOFF.md            Current working state
AGENTS.md             Thin Codex entrypoint for this repo
```

## Cross-Agent Continuity

AEWS can let Codex, Claude Code, and other agents understand the same project
progress by routing them to shared Project, Decisions, Handoff, and task-queue
roles. Git and test artifacts verify what actually changed.

This is checkpoint-based continuity, not real-time presence or transcript
sharing. See `docs/cross-agent-continuity.md` for the start, checkpoint,
staleness, concurrency, and optional harness-integration rules.

## v0.1 Deliverables

- Architecture: why AEWS uses four scopes and a projection layer.
- Document lifecycle: how information moves from working state to durable knowledge.
- Minimal templates: repo, handoff, decision, and experiment documents.
- Adapter matrix: how canonical documents map to Codex, Claude Code, Cursor, and Gemini CLI.
- Validation checklist: manual checks that prevent context duplication and adapter bloat.
- Adoption guide: how to migrate existing repositories with minimal change.
- Versioning policy: how to evaluate standard, template, example, and adapter changes.
- Roadmap: what belongs in v0.1, v0.2, and v1.0.

## v0.2 Validation

The first dependency-free, read-only validator is available at
`scripts/aews_validate.py`. See `docs/validator.md` for template/adoption usage,
the optional `aews.json` mapping, implemented checks, and manual-review limits.

v0.2 also defines evidence-backed adapter compatibility and optional
cross-agent continuity without copying task history or treating runtime memory
as project truth.

## Status

AEWS v0.1.0 is published. v0.2 validation and template hardening are in
progress. The first validator slice is implemented after two reference
evaluations. The evidence-backed compatibility matrix and optional cross-agent
continuity protocol are documented; controlled runtime adapter smoke tests are
the next evidence gap. Keep harness runtime features outside the core standard.

## License

MIT
