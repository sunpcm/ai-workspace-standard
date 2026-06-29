# AI Engineering Workspace Standard

AI Engineering Workspace Standard (AEWS) is a minimal, agent-agnostic standard for organizing engineering knowledge so it can be consumed by Codex, Claude Code, Cursor, Gemini CLI, and future agents without binding the workspace to one vendor.

AEWS treats the workspace as the durable asset. Agent-specific files are projections of the standard, not the source of truth.

## Goals

- Keep engineering context small, precise, and task-relevant.
- Define where knowledge belongs before writing it.
- Separate canonical workspace knowledge from agent-specific adapters.
- Make handoffs, decisions, experiments, and repo facts easy to maintain.
- Avoid copying the same knowledge across multiple agent tools.

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

## v0.1 Deliverables

- Architecture: why AEWS uses four scopes and a projection layer.
- Document lifecycle: how information moves from working state to durable knowledge.
- Minimal templates: repo, handoff, decision, and experiment documents.
- Adapter matrix: how canonical documents map to Codex, Claude Code, Cursor, and Gemini CLI.
- Validation checklist: manual checks that prevent context duplication and adapter bloat.
- Roadmap: what belongs in v0.1, v0.2, and v1.0.

## Status

This repository is in architecture-first v0.1. Do not add automation until the canonical model and minimal templates are stable.

## License

MIT
