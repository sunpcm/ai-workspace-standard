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
`templates/adoption/aews.example.json`,
`examples/reference-evaluations/full-stack-application.md`

### 2026-07-26: Keep the first validator dependency-free and read-only

Status: Accepted

Scope: Repo

Context: The ECC and ordinary application evaluations stabilized a small set of
mechanical checks. Adding a package, Markdown parser, semantic model, or rewrite
behavior would increase adoption and trust costs before those capabilities have
evidence.

Decision: The first validator is a Python 3.10+ standard-library script. It
reads a target repository and optional JSON mapping, produces text findings and
stable exit codes, and never modifies the target. Tests use `unittest` and
checked-in fixtures without third-party dependencies.

Consequences: The implementation remains inspectable and portable but local
document parsing is intentionally conservative. Install-generated paths and
semantic lifecycle questions remain manual-review warnings rather than hidden
heuristics.

Evidence: `scripts/aews_validate.py`, `tests/test_validator.py`,
`docs/validator.md`

### 2026-07-26: Define cross-agent continuity as an optional document protocol

Status: Accepted

Scope: Workspace

Context: Codex and Claude Code can read the same canonical project documents,
but shared documents alone do not prove what another agent changed or prevent
concurrent edits. ECC demonstrates useful explicit handoff and memory transport,
while also confirming that session capture, MCP, presence, and orchestration are
harness-runtime concerns.

Decision: AEWS will define an optional cross-agent continuity profile. All
participating agents read the same Project, Decisions, Handoff, and task-queue
roles; Git and verified artifacts provide implementation evidence; checkpoint
updates replace transcript-style activity logs. Runtime memory may transport
unreviewed handoffs but remains outside AEWS core and cannot become governed
truth automatically.

Consequences: Repositories can support Codex-to-Claude continuation without
adopting a runtime. AEWS does not promise real-time awareness, file locking, or
automatic transcript synchronization. Concurrent agents should use separate
branches or worktrees, and runtime-specific automation remains an optional
integration.

Evidence: `docs/cross-agent-continuity.md`, `docs/adapter-matrix.md`,
`examples/reference-evaluations/ecc-v2.0.0.md`

### 2026-07-26: Prioritize Codex and Claude Code compatibility evidence

Status: Accepted

Scope: Workspace

Context: The project owner currently uses Codex and Claude Code. Treating every
possible agent tool as an equal implementation target would spread validation
effort across tools that are not part of the active workflow and would make
compatibility claims difficult to maintain.

Decision: Codex and Claude Code are the primary compatibility targets for the
current AEWS roadmap. The canonical role model, adapter rules, and adoption
mapping remain vendor-neutral so Cursor, Gemini CLI, and future tools can add
thin adapters. Existing non-primary projections may remain as reference
examples, but AEWS does not commit to developing or runtime-testing them unless
real usage or new evidence changes the priority.

Consequences: Runtime-loading tests, cross-agent continuity examples, and
near-term compatibility documentation will focus on Codex and Claude Code.
Non-primary adapter entries must be labelled as extension references rather
than equivalent support commitments. The canonical standard must not acquire
Codex- or Claude-specific knowledge.

Evidence: `PROJECT.md`, `docs/adapter-matrix.md`, `docs/roadmap.md`

### 2026-07-26: Do not infer document links from arbitrary bare Markdown basenames

Status: Accepted

Scope: Repo

Context: The third adoption evaluation found twenty-five false warnings because
an application repository documents generated artifacts such as `summary.md`
and `batch_summary.md` in inline code. Their `.md` suffix does not make them
checked-in repository documents.

Decision: The dependency-free validator will continue checking normal Markdown
links, directory-qualified inline paths, explicit relative paths, and known
canonical root filenames. It will not treat every other bare inline-code `.md`
basename as a repository link.

Consequences: Generated report catalogs no longer dominate adoption output.
An author who intends to reference another checked-in document with a bare
custom filename should use a normal Markdown link or an explicit relative path.

Evidence: `scripts/aews_validate.py`, `tests/fixtures/adoption-warnings/README.md`,
`examples/reference-evaluations/ai-experiment-service.md`

### 2026-07-27: Promote the completed validation phase directly to a v1.0 candidate

Status: Accepted

Scope: Repo

Context: The v0.2 validation phase produced three real-repository evaluations,
a stable mapping contract, a tested read-only validator, a migration path, and
version-scoped runtime-loading evidence for both primary tools. No v0.2 tag was
published and therefore no external v0.2 consumers depend on an intermediate
release. All documented v1.0 exit criteria now have evidence.

Decision: Preserve the v0.2.0 readiness record as phase evidence, but make the
next local release candidate `v1.0.0` rather than publishing an intermediate
v0.2.0 tag. The v1 stable surface is the scope model, canonical roles,
thin-adapter contract, adoption mapping version 1, read-only validator, and
optional checkpoint continuity protocol.

Consequences: Future breaking changes to this stable surface require the
major-version process in `docs/versioning.md`. Push, tag, changelog dating, and
release publication remain owner-controlled. The absence of a v0.2 tag must not
be represented as a missing migration dependency because v0.2 was never a
published compatibility baseline.

Evidence: `docs/releases/v0.2.0-readiness.md`,
`docs/releases/v1.0.0-readiness.md`, `docs/runtime-loading-evidence.md`,
`docs/roadmap.md`

### 2026-08-08: Add a Secondary tier and place GitHub Copilot in it

Status: Accepted

Scope: Repo

Context: The 2026-07-26 decision made Codex and Claude Code the primary
compatibility targets because they were the owner's active tools, and it
allowed promotion when a tool gains real usage. The owner now uses GitHub
Copilot daily, but in an assisting role rather than as a main driver. Copilot
coding agent can read a root `AGENTS.md`, while the IDE surface reads
`.github/copilot-instructions.md`, so the existing Codex projection did not
cover everyday editor usage.

The existing two-tier model could not express this. Calling Copilot Primary
would imply runtime-loading evidence it does not have; calling it an extension
reference would understate a real maintenance commitment.

Decision: Add a third tier. Primary means an actively used main driver with a
maintained adapter, validator discovery, and controlled runtime-loading
evidence; Codex and Claude Code stay there. Secondary means the same
maintenance commitment without a runtime-evidence claim; GitHub Copilot goes
there, with a thin `.github/copilot-instructions.md` projection and
template-mode discovery. Extension reference is unchanged.

Project only the repository-wide instructions file. Path-scoped
`.github/instructions/*.instructions.md` rules stay with the adopting
repository, because activation globs are editor behavior rather than canonical
knowledge routing.

Consequences: Each tier now states what it guarantees, so a runtime claim
cannot leak across tiers, and no per-tool caveat is needed to correct the tier
label. Promotion of Copilot to Primary requires a manual editor probe, because
its IDE surface has no headless read-only invocation comparable to `codex` or
`claude`. The minimal example continues to demonstrate the two Primary tools
only, which stays consistent under this model.

Evidence: `adapters/copilot/.github/copilot-instructions.md`,
`docs/adapter-matrix.md`, `standard/adapters.md`, `scripts/aews_validate.py`

### 2026-08-08: Classify adapter discovery additions as a minor release

Status: Accepted

Scope: Repo

Context: Adding GitHub Copilot required a new branch in template-mode adapter
discovery. It was unclear whether changing validator discovery touches the v1
stable surface, which would force the major-version process in
`docs/versioning.md`.

Decision: Treat a discovery addition that recognizes one more adapter surface as
a backward-compatible minor change, and ship this one as `1.1.0`. The rule
generalizes: recognizing an additional surface is minor because no existing
repository must change a file, mapping, or read order to keep passing. Such a
change becomes breaking only when it stops recognizing a previously valid
surface, or makes a previously passing repository fail.

Consequences: Future adapter additions follow the same path and do not require a
major version. The adoption mapping contract version stays at 1 because the
`aews.json` schema is unchanged. Release notes and a readiness record for
`1.1.0` remain owner-controlled release-preparation work.

Evidence: `docs/versioning.md`, `scripts/aews_validate.py`

### 2026-08-09: Keep documentation in English and use translations for other languages

Status: Accepted

Scope: Repo

Context: The owner's readers are Chinese today, so writing the working
documents in Chinese was tried. Measuring the cost first showed it was larger
than expected. `_validate_duplicates` is the check that enforces the central
AEWS rule that adapters are projections rather than knowledge stores. It
compares normalized lines, and `_statements` ignores any line shorter than 60
characters.

Measured on the translated files: `PROJECT.md` produced 1 qualifying statement
from 67 non-empty lines and `DECISIONS.md` produced 9 from 208, against 11 from
30 lines in the English root `AGENTS.md`. Chinese wraps at roughly 35 to 40
characters per line, so almost no line reached the threshold. A constructed
duplicate was detected between an English document and an English adapter, and
went undetected in all three Chinese variants, including a verbatim Chinese
copy wrapped in the repository's normal style.

Decision: Documentation is written in English. Other languages are added as
`<name>.<lang>.md` translations beside the English original, as in
`README.zh-CN.md`. `TODO.md` stays Chinese because it is a task queue, not a
canonical knowledge role.

Consequences: Duplicate detection keeps working for the three mapped canonical
documents, which are the only files it compares against adapters. Chinese
readers are served by translations, at the cost of keeping each translation in
sync by hand. The narrower fact is worth recording: only `PROJECT.md`,
`DECISIONS.md`, and `HANDOFF.md` lose the check when translated in place, since
`docs/roadmap.md`, `docs/vision.md`, `TODO.md`, and any README are not mapped
roles. Lowering the 60-character threshold for CJK would be the alternative,
but it was not measured and is not part of this decision.

Evidence: `scripts/aews_validate.py`, `tests/test_language_boundary.py`,
`README.zh-CN.md`
