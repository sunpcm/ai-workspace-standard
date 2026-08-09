# AI Engineering Workspace Standard

[中文（简体）译本](README.zh-CN.md)

AI Engineering Workspace Standard (AEWS) is a minimal, agent-agnostic standard for organizing engineering knowledge so it can be consumed by Codex, Claude Code, GitHub Copilot, Cursor, Gemini CLI, and future agents without binding the workspace to one vendor.

AEWS treats the workspace as the durable asset. Agent-specific files are projections of the standard, not the source of truth.

The standard remains open to any thin agent adapter. Codex and Claude Code are
the primary targets and carry controlled runtime-loading evidence. GitHub
Copilot is a secondary target: actively used and maintained, but without a
runtime-evidence claim. Cursor, Gemini CLI, and future tools are extension
references rather than active runtime commitments.

## Goals

- Keep engineering context small, precise, and task-relevant.
- Define where knowledge belongs before writing it.
- Separate canonical workspace knowledge from agent-specific adapters.
- Make handoffs, decisions, experiments, and repo facts easy to maintain.
- Avoid copying the same knowledge across multiple agent tools.
- Let multiple agents resume the same project state through a shared,
  evidence-backed checkpoint protocol.

## Non-Goals

- AEWS is not an ECC clone.
- AEWS is not an agent runtime, hook system, MCP catalog, or security harness.
- AEWS is not a collection of large `AGENTS.md`, `CLAUDE.md`, or editor rule files.
- AEWS does not replace project documentation, tests, CI, or operational runbooks.

## Core Principle

Scope first:

1. Decide whether the information is Global, Workspace, Repo, or Experiment scope.
2. Decide whether it is Knowledge, Decision, Task, Working State, or Archive.
3. Only then decide which document or adapter should expose it.

## Repository Layout

```text
docs/                 Human-readable design documents
standard/             Canonical AEWS model and rules
templates/            Minimal document templates
examples/             Small reference workspaces
adapters/             Agent-specific projections
PROJECT.md            Durable facts for this repo
DECISIONS.md          Accepted project decisions
HANDOFF.md            Current working state
AGENTS.md             Thin Codex entrypoint for this repo
.github/copilot-instructions.md
                      Thin GitHub Copilot entrypoint for this repo
```

## Quick Start

Choose one path. Do not create duplicate canonical documents merely to match
AEWS filenames.

Fetch the stable standard with:

```bash
git clone --branch v1.1.0 --depth 1 \
  https://github.com/sunpcm/ai-workspace-standard.git <aews-repo>
```

### New Or Minimal Repository

From the target repository, copy the minimal canonical documents and only the
adapters you actually use:

```bash
cp <aews-repo>/templates/repo/PROJECT.md ./PROJECT.md
cp <aews-repo>/templates/decision/DECISIONS.md ./DECISIONS.md
cp <aews-repo>/adapters/codex/AGENTS.md ./AGENTS.md
cp <aews-repo>/adapters/claude-code/CLAUDE.md ./CLAUDE.md
mkdir -p .github && cp <aews-repo>/adapters/copilot/.github/copilot-instructions.md \
  ./.github/copilot-instructions.md
```

Keep the repository's existing `README.md`, or create one before validation.

Then:

1. Replace every prompt in `PROJECT.md` with real repository facts and
   verification commands.
2. Add accepted decisions to `DECISIONS.md`; do not invent historical entries.
3. Copy `templates/handoff/HANDOFF.md` only while active work needs a shared
   continuation checkpoint.
4. Use the repository's existing issue tracker or `TODO.md` as the shared task
   queue.
5. Remove any adapter whose tool is not used.

Validate from the AEWS checkout:

```bash
python3 <aews-repo>/scripts/aews_validate.py <target-repo> --mode template
```

### Existing Repository

Keep existing architecture, decision, and working-context documents. Copy and
edit the routing manifest instead of renaming or duplicating them:

```bash
cp <aews-repo>/templates/adoption/aews.example.json ./aews.json
$EDITOR ./aews.json
python3 <aews-repo>/scripts/aews_validate.py .
```

Use an external mapping for a first read-only evaluation:

```bash
cp <aews-repo>/templates/adoption/aews.example.json /tmp/aews-target.json
$EDITOR /tmp/aews-target.json
python3 <aews-repo>/scripts/aews_validate.py <target-repo> \
  --mode adoption \
  --config /tmp/aews-target.json
```

See `docs/adoption-guide.md` for migration decisions and
`templates/adoption/README.md` for every mapping field.

## Daily Multi-Agent Workflow

At the start of work, every adapter should route its agent to the same:

1. Project facts and verification commands;
2. accepted Decisions;
3. active Handoff, when one exists;
4. task queue;
5. Git and test evidence.

At a meaningful verified checkpoint, update the shared task state and replace
the Handoff with the completed step, exact evidence, next step, blockers, and
expiration condition. Record durable rationale in Decisions and stable facts
in Project. Do not copy transcripts or separate per-agent progress histories
into any adapter file.

For concurrent work, use separate branches or worktrees. AEWS does not provide
live presence or file locking.

## Cross-Agent Continuity

AEWS can let Codex, Claude Code, and other agents understand the same project
progress by routing them to shared Project, Decisions, Handoff, and task-queue
roles. Git and test artifacts verify what actually changed.

This is checkpoint-based continuity, not real-time presence or transcript
sharing. See `docs/cross-agent-continuity.md` for the start, checkpoint,
staleness, concurrency, and optional harness-integration rules.

## v0.1 Deliverables

- Architecture: why AEWS uses four scopes and a projection layer.
- Document lifecycle: how information moves from working state to durable knowledge.
- Minimal templates: repo, handoff, decision, and experiment documents.
- Adapter matrix: how canonical documents map to Codex, Claude Code, GitHub Copilot, Cursor, and Gemini CLI.
- Validation checklist: manual checks that prevent context duplication and adapter bloat.
- Adoption guide: how to migrate existing repositories with minimal change.
- Versioning policy: how to evaluate standard, template, example, and adapter changes.
- Roadmap: what belongs in v0.1, v0.2, and v1.0.

## v0.2 Validation

The first dependency-free, read-only validator is available at
`scripts/aews_validate.py`. See `docs/validator.md` for template/adoption usage,
the tested `templates/adoption/aews.example.json` mapping, implemented checks,
and manual-review limits.

v0.2 also defines evidence-backed adapter compatibility and optional
cross-agent continuity without copying task history or treating runtime memory
as project truth. Runtime evidence focuses on Codex and Claude Code while the
generic adapter contract remains open.

## v1.0 Stable Surface

AEWS v1.0.0 stabilizes the scope model, canonical roles, thin
adapter contract, adoption mapping version 1, read-only validator, and optional
checkpoint continuity protocol. `docs/adoption-guide.md` and
`templates/adoption/aews.example.json` are the shortest adoption route.

Breaking changes to this surface follow `docs/versioning.md`. Runtime evidence
is recorded per tested tool version and does not turn AEWS into an agent
harness.

## Status

AEWS v1.0.0 is published. v1.1.0 adds a Secondary support tier and a GitHub
Copilot projection, and v1.1.1 is a documentation release. Release notes are in
`docs/releases/`.

Controlled, version-scoped runtime-loading probes have passed for both Codex
and Claude Code against the same public synthetic checkpoint. These results do
not imply universal version compatibility or harness-runtime parity. Keep
harness runtime features outside the core standard.

Known limits on those claims: GitHub Copilot is maintained without any
controlled probe; the recorded Codex and Claude Code probes ran against
`codex-cli 0.145.0` and Claude Code `2.1.218` rather than newer versions; and
no external adopter evidence exists for any release. The per-release audits
under `docs/releases/` record these in full, and are written in Chinese from
v1.1.1 onward.

## License

MIT
