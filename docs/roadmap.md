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

Status: Local release candidate complete. Three reference evaluations, the
first dependency-free read-only validator, a tested adoption mapping template,
an evidence-backed adapter matrix, and the optional cross-agent continuity
protocol are complete. Tag, push, and publication remain owner-controlled.

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

1. review and optionally publish the local v0.2.0 candidate;
2. complete the Claude Code runtime probe after explicit external-transfer
   approval; the Codex probe is complete;
3. keep semantic and runtime-aware checks outside the first validator.

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

Status: All local-only criteria are complete, but v1.0 is blocked by the Claude
Code runtime-loading evidence criterion. Do not claim v1.0 compatibility until
that controlled probe is authorized, passed, and recorded.

## Deferred

These are intentionally deferred until the standard is stable:

- hooks,
- MCP catalog,
- security policy engine,
- memory runtime,
- automatic agent profile generation,
- complex CLI tooling.

Those features are closer to an agent harness. AEWS may integrate with harnesses later, but should not become one by accident.
