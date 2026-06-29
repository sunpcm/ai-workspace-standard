# PROJECT

## Purpose

AI Engineering Workspace Standard (AEWS) defines a minimal, agent-agnostic way to organize engineering knowledge for AI-assisted development.

The project focuses on durable workspace knowledge, document lifecycle, scope boundaries, and thin projections into tool-specific adapter files.

## Scope

- Scope: Workspace standard
- Current version: v0.1 architecture-first draft
- Primary audience: engineers who use multiple AI coding agents across repositories

## Architecture

AEWS has two layers:

- Canonical standard: `docs/`, `standard/`, `templates/`, and `examples/`.
- Agent adapters: `adapters/` and thin root agent entrypoints.

The canonical standard is the source of truth. Adapters should reference canonical documents rather than copy their content.

## Commands

```bash
# Inspect files
find . -maxdepth 4 -type f -print

# Check for large markdown files
wc -l README.md AGENTS.md PROJECT.md DECISIONS.md HANDOFF.md docs/*.md standard/*.md

# Search for adapter references
rg -n "AGENTS.md|CLAUDE.md|GEMINI.md|PROJECT.md|HANDOFF.md|DECISIONS.md"
```

## Verification

Before considering v0.1 changes complete:

- root `AGENTS.md` remains thin,
- canonical concepts live under `docs/` or `standard/`,
- templates are minimal,
- adapters do not duplicate durable architecture content,
- examples can be understood without scripts.

## Known Risks

- The project can drift into an ECC-style harness if hooks, MCP, security, and runtime features are added too early.
- Adapter files can become duplicated sources of truth if the projection rule is not enforced.
- Personal preferences can leak into public templates if Global scope is not treated carefully.
