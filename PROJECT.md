# PROJECT

## Purpose

AI Engineering Workspace Standard (AEWS) defines a minimal, agent-agnostic way to organize engineering knowledge for AI-assisted development.

The project focuses on durable workspace knowledge, document lifecycle, scope
boundaries, thin projections into tool-specific adapter files, and optional
evidence-backed continuity between agents.

## Scope

- Scope: Workspace standard
- Current version: local v0.2.0 release candidate; v0.1.0 published
- Primary audience: engineers who use multiple AI coding agents across repositories
- Primary compatibility targets: Codex and Claude Code
- Extension policy: keep the adapter contract vendor-neutral and open to other
  tools without committing to implement or runtime-test them now

## Architecture

AEWS has two layers:

- Canonical standard: `docs/`, `standard/`, `templates/`, and `examples/`.
- Agent adapters: `adapters/` and thin root agent entrypoints.

The canonical standard is the source of truth. Adapters should reference canonical documents rather than copy their content.

Cross-agent continuity is a document protocol layered on those sources. Git
and verified artifacts establish implementation state; optional harness memory
may transport a handoff but does not become governed truth.

Current compatibility work prioritizes Codex and Claude Code because they are
the owner's active tools. Existing Cursor and Gemini projections remain useful
reference implementations, but they are not active development or runtime
validation commitments.

## Commands

```bash
# Inspect files
find . -maxdepth 6 -path ./.git -prune -o -path ./ECC -prune -o -type f -print

# Check for large markdown files
wc -l README.md AGENTS.md PROJECT.md DECISIONS.md HANDOFF.md docs/*.md standard/*.md

# Search for adapter references
rg -n "AGENTS.md|CLAUDE.md|GEMINI.md|PROJECT.md|HANDOFF.md|DECISIONS.md"

# Inspect local adapter runtime availability without invoking a model
codex --version
claude --version

# Run the read-only validator
python3 scripts/aews_validate.py . --mode template

# Run validator regression tests
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

## Verification

Before considering changes complete:

- root `AGENTS.md` remains thin,
- canonical concepts live under `docs/` or `standard/`,
- templates are minimal,
- adapters do not duplicate durable architecture content,
- declared adapters route to the same active handoff and task queue when the
  continuity profile is used,
- examples can be understood without scripts,
- `docs/validation-checklist.md` passes for the changed files,
- `python3 scripts/aews_validate.py . --mode template` reports no failures or
  warnings,
- validator regression tests pass.

## Known Risks

- The project can drift into an ECC-style harness if hooks, MCP, security, and runtime features are added too early.
- Adapter files can become duplicated sources of truth if the projection rule is not enforced.
- Personal preferences can leak into public templates if Global scope is not treated carefully.
- A stale handoff can mislead another agent unless it is checked against Git
  and tests.
- Concurrent agents in one worktree can overwrite or accidentally commit each
  other's changes; use separate branches or worktrees.
- Compatibility wording can overstate support if reference projections for
  non-primary tools are mistaken for tested integrations.
