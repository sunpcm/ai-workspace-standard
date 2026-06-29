# Roadmap

AEWS should evolve from a small standard into a templateable workspace system. Each phase must preserve minimal context and avoid vendor lock-in.

## v0.1: Architecture and Minimal Standard

Goal: define the canonical model.

Deliverables:

- four-scope model,
- document lifecycle,
- thin adapter rules,
- minimal repo template,
- one minimal example,
- adapter matrix for Codex, Claude Code, Cursor, and Gemini CLI,
- manual validation checklist.

Exit criteria:

- A user can decide where a new piece of context belongs.
- A repo can expose the same canonical knowledge to at least two agents without copying content.
- No generator script is required to understand the standard.
- A change can be reviewed against `docs/validation-checklist.md`.

## v0.2: Validation and Template Hardening

Goal: make the standard testable.

Possible deliverables:

- checklist-based validator,
- duplicate-context detector,
- sample migration guide from large `AGENTS.md`,
- more examples from real repo types,
- optional bootstrap script.

Exit criteria:

- The template can be applied to a real repo and reviewed with a repeatable checklist.
- Adapter files can be checked for obvious duplication.

## v1.0: Stable Template and Migration Path

Goal: make AEWS usable as a long-term open-source template.

Possible deliverables:

- versioned standard,
- changelog,
- migration guide,
- template repository,
- compatibility notes for major agent tools,
- public contribution guidelines.

Exit criteria:

- Users can adopt AEWS without reading the entire design discussion.
- Breaking changes are versioned and documented.
- Agent adapters remain projections, not independent knowledge stores.

## Deferred

These are intentionally deferred until the standard is stable:

- hooks,
- MCP catalog,
- security policy engine,
- memory runtime,
- automatic agent profile generation,
- complex CLI tooling.

Those features are closer to an agent harness. AEWS may integrate with harnesses later, but should not become one by accident.
