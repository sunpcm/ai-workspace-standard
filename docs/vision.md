# Vision

Modern AI coding tools change quickly. Codex, Claude Code, GitHub Copilot, Cursor, Gemini CLI, and future agents all need repository context, but each tool asks for that context in a different shape.

If every tool becomes a separate source of truth, teams accumulate duplicated instructions, stale handoff notes, conflicting rules, and oversized context files. That makes agents more expensive to run and less reliable.

AEWS exists to make engineering knowledge portable.

Portability does not require equal implementation investment in every tool.
The current project prioritizes Codex and Claude Code compatibility evidence,
maintains GitHub Copilot as a secondary target without a runtime claim, and
keeps the canonical model and adapter contract open to other agents.

## Problem

Most AI workspace setups start by asking:

> What should go into `AGENTS.md`, `CLAUDE.md`, or editor rules?

AEWS starts with a different question:

> What is the scope and lifecycle of this information?

Only after answering that question should the workspace decide which agent adapter exposes the information.

## Desired Outcome

A well-maintained AEWS workspace should make it clear:

- Which facts are global personal preferences.
- Which rules apply across a workspace.
- Which instructions belong to a single repository.
- Which notes are temporary experiment state.
- Which decisions are durable and why they were made.
- Which files an agent should read for a given task.

## Design Bias

AEWS favors:

- small context over complete context,
- durable decisions over transient chat logs,
- references over duplication,
- explicit scope over implicit convention,
- adapter projection over vendor lock-in.
