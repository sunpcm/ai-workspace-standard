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

Status: Phase complete. Three reference evaluations, the
first dependency-free read-only validator, a tested adoption mapping template,
an evidence-backed adapter matrix, and the optional cross-agent continuity
protocol are complete. The unpublished v0.2.0 candidate is retained as phase
evidence and superseded by the local v1.0.0 candidate.

Primary compatibility targets: Codex and Claude Code. Other tools remain
possible through the open adapter contract but are not active implementation
or runtime-validation targets.

Delivered:

- checklist-based validator,
- duplicate-context detector,
- sample migration guide from large `AGENTS.md`,
- more examples from real repo types,
- evidence-backed cross-agent checkpoint protocol.

Current sequence:

1. retain the v0.2.0 readiness record as phase evidence;
2. use the completed Codex and Claude Code probes in the v1.0 evidence chain;
3. keep semantic and runtime-aware checks outside the validator core.

Exit criteria:

- The template can be applied to a real repo and reviewed with a repeatable checklist.
- Adapter files can be checked for obvious duplication.
- Two agents can consume one evidence-backed continuation checkpoint without
  requiring a shared runtime.

## v1.0: Stable Template and Migration Path

Goal: make AEWS usable as a long-term open-source template.

Delivered:

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

Status: Published. All exit criteria had evidence after the controlled Claude
Code probe passed on 2026-07-27. The full readiness audit is recorded in
`docs/releases/v1.0.0-readiness.md`. The `v1.0.0` tag and GitHub Release were
published on 2026-08-08.

## v1.1: Secondary Support Tier

Status: Local release candidate complete on 2026-08-08. A Secondary support
tier was added and GitHub Copilot placed in it, after the owner confirmed daily
use of Copilot in an assisting role alongside the two main drivers.

Primary: Codex and Claude Code. Secondary: GitHub Copilot. Cursor, Gemini CLI,
and future tools remain possible through the open adapter contract but are not
active implementation or runtime-validation targets.

This release tested the v1.0 exit criterion that adding another tool does not
require changing canonical roles. It did not: only an adapter file, validator
discovery, and documentation changed.

Outstanding for this track:

- no controlled runtime probe exists for GitHub Copilot,
- recorded Codex and Claude Code probes have not been re-run against newer
  local tool versions.

## Deferred

These are intentionally deferred until the standard is stable:

- hooks,
- MCP catalog,
- security policy engine,
- memory runtime,
- automatic agent profile generation,
- complex CLI tooling.

Those features are closer to an agent harness. AEWS may integrate with harnesses later, but should not become one by accident.
