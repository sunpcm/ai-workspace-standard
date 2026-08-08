# Changelog

All notable AEWS changes are recorded here. Versions follow the compatibility
rules in `docs/versioning.md`.

## Unreleased

### Changed

- Owner-facing working documents are now written in Chinese: `PROJECT.md`,
  `DECISIONS.md`, `HANDOFF.md`, `docs/roadmap.md`, and `docs/vision.md`.
  The standard surface, adopter documentation, examples, and `README.md` stay
  in English. The language boundary follows audience, not directory.
- `CONTRIBUTING.md` now states the language policy before its read order,
  because items 2 to 6 of that order are Chinese.

### Added

- `tests/test_language_boundary.py` keeps the English contract surface
  complete. New documents are treated as contract surface unless declared as
  working documents, and translations must keep an English original. It is a
  repository policy guard, not part of the AEWS standard.

## 1.1.0 - 2026-08-08

### Added

- A thin GitHub Copilot adapter at
  `adapters/copilot/.github/copilot-instructions.md`.
- Template-mode validator discovery for `.github/copilot-instructions.md` at a
  repository root and inside `adapters/`.
- A root `.github/copilot-instructions.md` entrypoint for this repository.
- A Simplified Chinese translation of the README at `README.zh-CN.md`, linked
  from the English README.

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
