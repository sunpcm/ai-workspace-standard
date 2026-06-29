# Oversized AGENTS.md Migration

This example shows how to migrate an oversized agent entrypoint into AEWS canonical documents plus a thin adapter.

## Before

`before/AGENTS.md` mixes four different lifecycles:

- stable repo facts and architecture,
- command reference,
- accepted decisions and rationale,
- active task state and blockers.

That file is hard to maintain because every agent must read stale or irrelevant context before it can start work.

## After

The same information is split by scope and lifecycle:

- `after/PROJECT.md` keeps durable repo facts, architecture, commands, verification, and known risks.
- `after/DECISIONS.md` records accepted choices with context and consequences.
- `after/HANDOFF.md` keeps the current continuation state, evidence, next step, and expiration rule.
- `after/AGENTS.md` remains a thin adapter with read order and a duplication warning.

## Why This Helps

AEWS does not add files for their own sake. It separates content that changes at different speeds:

- adapters can stay small and tool-specific,
- decisions remain auditable,
- handoffs can expire without deleting durable knowledge,
- project facts can be reused by multiple agents without copying.

Use this pattern when an agent file starts containing architecture notes, task history, experiments, or decision rationale.
