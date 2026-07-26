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

Status: In progress. Two reference evaluations, the first dependency-free
read-only validator, an evidence-backed adapter matrix, and the optional
cross-agent continuity protocol are complete.

Primary compatibility targets: Codex and Claude Code. Other tools remain
possible through the open adapter contract but are not active implementation
or runtime-validation targets.

Possible deliverables:

- checklist-based validator,
- duplicate-context detector,
- sample migration guide from large `AGENTS.md`,
- more examples from real repo types,
- optional bootstrap script,
- evidence-backed cross-agent checkpoint protocol.

Current sequence:

1. use the validator on another adoption candidate before tightening warnings;
2. decide whether to add a reusable adoption mapping template;
3. complete the Claude Code runtime probe after explicit external-transfer
   approval; the Codex probe is complete;
4. keep semantic and runtime-aware checks outside the first validator.

Exit criteria:

- The template can be applied to a real repo and reviewed with a repeatable checklist.
- Adapter files can be checked for obvious duplication.
- Two agents can consume one evidence-backed continuation checkpoint without
  requiring a shared runtime.

## v1.0: Stable Template and Migration Path

Goal: make AEWS usable as a long-term open-source template.

Possible deliverables:

- versioned standard,
- changelog,
- migration guide,
- template repository,
- compatibility notes for Codex and Claude Code plus an extension contract for
  other tools,
- public contribution guidelines.

Exit criteria:

- Users can adopt AEWS without reading the entire design discussion.
- Breaking changes are versioned and documented.
- Agent adapters remain projections, not independent knowledge stores.
- Codex and Claude Code have repeatable compatibility evidence; adding another
  primary tool does not require changing canonical roles.

## Deferred

These are intentionally deferred until the standard is stable:

- hooks,
- MCP catalog,
- security policy engine,
- memory runtime,
- automatic agent profile generation,
- complex CLI tooling.

Those features are closer to an agent harness. AEWS may integrate with harnesses later, but should not become one by accident.
