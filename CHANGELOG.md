# Changelog

All notable AEWS changes are recorded here. Versions follow the compatibility
rules in `docs/versioning.md`.

## Unreleased

## 1.1.0 - 2026-08-08

### Added

- A thin GitHub Copilot adapter at
  `adapters/copilot/.github/copilot-instructions.md`.
- Template-mode validator discovery for `.github/copilot-instructions.md` at a
  repository root and inside `adapters/`.
- A root `.github/copilot-instructions.md` entrypoint for this repository.

### Changed

- Support policy now has three tiers. Codex and Claude Code remain Primary
  with runtime-loading evidence. GitHub Copilot joins as Secondary: maintained
  adapter and discovery, no runtime-evidence claim. Extension reference is
  unchanged.

## 1.0.0 - 2026-07-27

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
- README Quick Start paths for new repositories, existing repositories, and
  daily Codex/Claude checkpoint work.

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

The v0.2 validation phase was completed but never tagged; its local readiness
record is retained as evidence and its changes are included in v1.0.0.

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
