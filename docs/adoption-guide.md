# Adoption Guide

This guide explains how to adopt AEWS in an existing repository without turning the migration into a rewrite.

Start with the smallest useful change: create canonical documents for durable knowledge, then make agent adapters point to those documents.

## When AEWS Fits

Adopt AEWS when a repository has one or more of these problems:

- agent instruction files are becoming long and hard to review,
- the same project facts are copied into multiple agent tools,
- decisions and task state are mixed into `AGENTS.md`, `CLAUDE.md`, Cursor rules, or `GEMINI.md`,
- handoffs become stale because they are stored beside durable architecture notes,
- multiple agents need the same repo context without binding the repo to one vendor.

AEWS is especially useful when a team wants agents to share one source of truth while keeping each tool's adapter small.

## When AEWS Does Not Fit

Do not adopt AEWS as a substitute for:

- project documentation,
- tests,
- CI,
- release process,
- operational runbooks,
- security policy,
- an agent runtime or harness.

AEWS v0.1 is a documentation standard. It does not provide hooks, MCP catalogs, memory runtimes, policy engines, or automated agent orchestration.

If a repository has no durable agent-facing context yet, start with the minimal example rather than adding every AEWS document at once.

## Minimal Adoption Path

Use this path first. Expand only when the repository proves it needs more structure.

1. Create `PROJECT.md` for durable repo facts, commands, boundaries, verification, and known risks.
2. Create `DECISIONS.md` for accepted decisions that should influence future work.
3. Create `HANDOFF.md` only if active continuation state needs to be preserved.
4. Keep the existing agent file as a thin adapter with read order and tool-specific behavior.
5. Run `docs/validation-checklist.md` manually before accepting the migration.

The first migration should not add scripts, generators, hooks, or new tool-specific behavior.

## Migrating From One Large `AGENTS.md`

Use `examples/migrations/oversized-agents/` as the reference pattern.

Move content by lifecycle:

- durable repo facts and commands go to `PROJECT.md`,
- accepted rationale goes to `DECISIONS.md`,
- current task state, blockers, and next steps go to `HANDOFF.md`,
- temporary investigation notes go to an experiment document or stay out of active read order,
- tool-specific read order and behavior stay in `AGENTS.md`.

After migration, `AGENTS.md` should answer only:

- what to read first,
- what behavior is specific to this agent,
- what must not be copied into the adapter.

If the migrated `AGENTS.md` still contains architecture, command reference, task history, or decision rationale, the migration is not done.

## Migrating From Multiple Agent Configs

When a repo already has `AGENTS.md`, `CLAUDE.md`, Cursor rules, `GEMINI.md`, or other agent files, do not merge them into one larger adapter.

Instead:

1. List the durable facts repeated across agent files.
2. Move those facts into `PROJECT.md`, `DECISIONS.md`, or another canonical document.
3. Keep each adapter focused on the read order and the behavior required by that tool.
4. Remove copied project knowledge from the adapters.
5. Review adapters together whenever canonical file names or read order changes.

Agent adapters may differ in syntax, but they should not define separate project realities.

## Common Mistakes

- Migrating everything at once instead of starting with the minimal path.
- Treating `AGENTS.md` as the project knowledge base.
- Copying the same durable fact into every adapter.
- Moving unstable task notes into `PROJECT.md`.
- Keeping old experiments in active read order.
- Adding automation before the manual checklist is stable.
- Publishing public templates that include private Global preferences.
- Describing harness features as AEWS v0.1 capabilities.

## Adoption Check

Before considering adoption complete, confirm:

- every durable fact has one primary canonical home,
- every adapter is thin and tool-specific,
- active state has an expiration or next review point,
- accepted decisions have context and consequences,
- examples or migrations can be understood without scripts,
- the repository still relies on its own docs, tests, CI, and runbooks for engineering correctness.
