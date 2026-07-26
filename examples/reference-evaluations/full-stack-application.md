# Full-Stack Application Reference Evaluation

This document records a sanitized manual AEWS evaluation of a private local
application repository. It preserves structural evidence without copying
business details, source code, credentials, internal URLs, or absolute paths.

## Snapshot

- Repository type: ordinary full-stack application
- Application shape: browser frontend, HTTP backend, relational database,
  container-based local runtime
- Review date: 2026-07-26
- Git state during review: clean tracked worktree
- Evaluation method: read-only document and repository-structure inspection

No dependencies, tests, services, containers, or deployment commands were run.

## Existing Knowledge Surfaces

The repository already had:

- a root README with purpose, stack, runtime commands, service access, and
  document navigation;
- a separate architecture overview with module boundaries and durable
  implementation constraints;
- a hidden planning-directory document that declared itself the single source
  of truth for phases, priorities, and acceptance criteria;
- component-level runbooks containing newer operational and test evidence;
- a working draft containing requirements, technical choices, research
  findings, boundaries, and open questions;
- no tracked agent adapter and no dedicated decision or handoff document.

This is a normal brownfield documentation layout. Requiring new preferred AEWS
filenames before understanding these surfaces would create duplication.

## Proposed Adoption Mapping

### Project

Result: mapped with ambiguity.

The root README is the best primary router because it contains the repository
overview, commands, and document navigation. The architecture overview and
component runbooks are supplements that own deeper boundaries and operational
facts.

One file cannot practically contain every durable project fact in a mature
application. AEWS should therefore allow one primary role owner plus explicit
supplements. Supplements do not become co-equal sources: the primary document
must route readers to them and define their narrower ownership.

### Decisions

Result: missing canonical role.

Decision-like content existed in architecture notes, a working draft, component
runbooks, and planning documents. No single document owned accepted decisions,
rationale, consequences, and supersession.

This is a real role gap, not a filename mismatch. Adoption mode should report it
as a warning during incremental adoption.

### Handoff

Result: missing or stale.

The main plan contained phase state and next work, but its baseline lagged newer
architecture, runtime, and component evidence. Recent edits to the file did not
make all of its claimed current state authoritative.

A task plan is not automatically a handoff. Adoption validation should check
whether a mapped Handoff contains current goal, last completed step, next step,
blockers, evidence, and an expiration condition.

### Experiment

Result: inactive.

The working draft contained research findings and technical choices but no
method, observed result, conclusion, or close condition. It is Working State,
not a completed Experiment.

The absence of an Experiment role is valid when no active experiment exists.

### Adapter

Result: none declared.

No tracked Codex, Claude Code, Cursor, or Gemini adapter was present. Adoption
mode should validate only declared adapters. It should not infer tool use from
local or external agent activity.

## Canonical Consistency Findings

The primary documentation linked to preferred architecture and database paths
that did not exist at those locations; equivalent files existed under a
documentation directory. The planning document repeated one of the stale
references.

This demonstrates that a validator should check:

- every mapped primary and supplement path exists;
- the primary document actually references its declared supplements;
- referenced repository-local Markdown paths resolve;
- a document claiming current or single-source-of-truth status has lifecycle
  evidence, not merely a recent Git timestamp.

The last check remains manual in the first validator because freshness cannot be
derived safely from modification time alone.

## Minimum Mapping Input

The evaluation supports an optional repository-local `aews.json` for adoption
mode. It should be a routing manifest, not a new knowledge source.

Required properties:

- schema version;
- mode set to `adoption`;
- one primary path for the Project role;
- optional Project supplements;
- explicit state for Decisions, Handoff, and Experiment when not mapped;
- zero or more declared adapter paths.

Allowed unmapped states:

- `missing`: the role should exist but has no canonical owner yet;
- `inactive`: the lifecycle role is not currently needed.

Project cannot be `inactive`. Decisions may be `missing` during incremental
adoption. Handoff and Experiment may be `inactive`. A `missing` state must
produce a warning and cannot be used to suppress validation.

The manifest must contain paths and lifecycle state only. It must not contain
architecture facts, decisions, task details, commands, or copied adapter rules.

## Outcome

The ordinary application evaluation completes the evidence gate defined before
validator implementation.

The first validator can now proceed with:

1. template and adoption modes;
2. optional `aews.json` role mapping;
3. primary plus supplement path validation;
4. adapter reference and line-count checks;
5. obvious duplicate durable sentence warnings;
6. stable text output and exit codes.

Human review remains required for scope, lifecycle freshness, decision quality,
and whether a supplement's ownership is appropriately narrow.
