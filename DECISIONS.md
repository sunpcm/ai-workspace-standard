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

### 2026-06-29: Use MIT license for the initial open-source standard

Status: Accepted

Scope: Repo

Context: AEWS is intended to be cloned, adapted, and used as a template across different teams and tools.

Decision: The repository will use the MIT License.

Consequences: Adoption friction stays low, but warranty and liability are disclaimed.

Evidence: `LICENSE`

### 2026-06-29: Add a manual validation checklist before automation

Status: Accepted

Scope: Repo

Context: v0.1 should prove the standard manually before adding scripts or generated behavior.

Decision: AEWS will use `docs/validation-checklist.md` as the acceptance gate for document, template, example, and adapter changes.

Consequences: Automation is deferred until the checklist stabilizes through
real use. The first v0.2 evidence gate was satisfied on 2026-07-26; only the
validated mechanical checks may now proceed.

Evidence: `docs/validation-checklist.md`, `docs/roadmap.md`

### 2026-07-26: Validate canonical roles before preferred filenames

Status: Accepted

Scope: Workspace

Context: The ECC v2.0.0 reference evaluation showed that an existing repository
can have governed project facts, decisions, working state, and adapters under
different filenames. A filename-only validator would report avoidable warnings
and could encourage duplicated documents during adoption.

Decision: The v0.2 validator design will distinguish AEWS template mode from
existing-repository adoption mode. Template mode may require preferred AEWS
paths. Adoption mode must validate explicitly mapped canonical roles and report
the mapping it used before applying filename-specific checks.

Consequences: AEWS keeps preferred filenames without making them universal.
The mapping input format was intentionally deferred until one ordinary
application repository was manually evaluated and is now recorded in the
following decision.

Evidence: `docs/validator-design.md`,
`examples/reference-evaluations/ecc-v2.0.0.md`

### 2026-07-26: Use a routing-only JSON manifest for adoption mapping

Status: Accepted

Scope: Workspace

Context: The ordinary full-stack application evaluation found durable project
knowledge split across a root router, an architecture overview, and component
runbooks. It also found truly missing Decisions and Handoff roles. CLI-only
flags would not provide repeatable CI input, while a prose convention would be
difficult to validate mechanically.

Decision: Adoption mode will accept an optional `aews.json` manifest or an
explicit path to an equivalent JSON file. It maps one primary document and
optional supplements for each role, explicit `missing` or allowed `inactive`
states, and declared adapter paths.

Consequences: Existing repositories can be validated without renaming or
duplicating documents. The manifest is a routing projection and must never hold
project facts, decisions, commands, or working state. The validator must not
generate or rewrite it.

Evidence: `docs/validator-design.md`, `standard/documents.md`,
`examples/reference-evaluations/full-stack-application.md`
