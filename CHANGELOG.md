# Changelog

All notable AEWS changes are recorded here. Versions follow the compatibility
rules in `docs/versioning.md`.

## Unreleased

### Added

- A dependency-free, read-only validator with template and adoption modes.
- A routing-only `aews.json` contract and tested copy-and-edit adoption mapping.
- Three anonymized real-repository reference evaluations.
- An optional evidence-backed Codex/Claude cross-agent continuity protocol.
- A compatibility matrix that separates structural projection from runtime
  loading evidence.
- A synthetic runtime-loading fixture and controlled Codex CLI evidence.
- Controlled Claude Code runtime-loading evidence after explicit approval for
  the public synthetic fixture transfer.

### Changed

- Canonical roles, rather than preferred filenames, now drive existing-repo
  adoption validation.
- Codex and Claude Code are the primary compatibility targets. Cursor, Gemini
  CLI, and future tools remain open extension references.
- Local Markdown reference checks no longer treat arbitrary generated artifact
  basenames as repository documents.

### Known Limitations

- Runtime evidence is version-scoped to the tested Codex and Claude Code
  configurations and does not prove universal compatibility.
- The validator intentionally leaves lifecycle freshness, decision quality,
  supplement ownership, and other semantic checks to manual review.
- No hooks, MCP catalog, memory runtime, orchestration service, generator, or
  package distribution is part of AEWS core.

The current Unreleased content is the local `v1.0.0` release candidate. The
v0.2 validation phase was completed but never tagged; its local readiness
record is retained as evidence. Neither candidate has been pushed, tagged, or
published by these readiness passes.

## 0.1.0 - 2026-06-29

### Added

- The four-scope model and document lifecycle.
- Canonical Project, Decisions, Handoff, and Experiment roles.
- Minimal document templates and a minimal repository example.
- Thin adapter projections for Codex, Claude Code, Cursor, and Gemini CLI.
- Manual validation, adoption, contribution, versioning, and release guidance.

### Boundary

- AEWS was established as a workspace knowledge standard, not an ECC-style
  agent harness.
