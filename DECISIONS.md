# DECISIONS

Record accepted decisions that should influence future AEWS work.

## Decisions

### 2026-06-29: Build AEWS as a standard, not an ECC clone

Status: Accepted

Scope: Workspace

Context: ECC is a broad agent harness covering agents, skills, hooks, commands, MCP, security, and memory.

Decision: AEWS v0.1 will focus on workspace knowledge structure, scope, lifecycle, templates, and adapter projection.

Consequences: Runtime features are deferred. The repo stays documentation-first until the canonical model is stable.

Evidence: `docs/architecture.md`, `docs/roadmap.md`

### 2026-06-29: Use Scope First as the primary placement rule

Status: Accepted

Scope: Workspace

Context: Large agent instruction files tend to accumulate mixed concerns and stale context.

Decision: AEWS will classify information as Global, Workspace, Repo, or Experiment before choosing a document or adapter.

Consequences: New documents and templates must state their intended scope.

Evidence: `docs/scope-first.md`, `standard/scopes.md`

### 2026-06-29: Keep adapters thin

Status: Accepted

Scope: Workspace

Context: Codex, Claude Code, Cursor, Gemini CLI, and future agents need different file formats, but they should not own separate knowledge copies.

Decision: Adapter files should contain read order and tool-specific behavior only.

Consequences: Durable project facts belong in canonical documents, not adapter files.

Evidence: `standard/adapters.md`, `docs/adapter-matrix.md`
