# Validator Design

This document defines the scope and contract of the lightweight AEWS validator.
The first implementation lives in `scripts/aews_validate.py`; usage belongs in
`docs/validator.md`.

The validator should automate only mechanical checks that support `docs/validation-checklist.md`. It must not replace human review of scope, lifecycle, or architectural intent.

## Goals

- Catch obvious adapter bloat.
- Confirm expected canonical files exist.
- Detect likely duplicated durable context.
- Flag forbidden runtime features introduced before they are accepted.
- Produce review hints that point back to `docs/validation-checklist.md`.

## Implementation Status

Implemented in the first read-only slice:

- template and adoption modes;
- routing-only `aews.json` validation;
- canonical primary and supplement path checks;
- mapped local document reference warnings;
- adapter routing and line-count warnings;
- obvious exact duplicate sentence warnings;
- text output and exit codes;
- dependency-free fixtures and tests.

Still manual or deferred:

- lifecycle freshness and semantic decision quality;
- forbidden runtime feature classification;
- template stack/vendor minimality hints;
- configurable thresholds;
- package publication and automatic rewrites.

## Non-Goals

The validator should not include:

- complex AST parsing,
- agent-specific parsers,
- automatic document rewrites,
- package publishing,
- npm or Python distribution,
- semantic judgment about whether a decision is correct,
- enforcement of one team's private Global preferences.

## Inputs

The validator inspects a repository directory in one of two modes.

### Template Mode

Template mode validates the AEWS template repository or a repository that
explicitly adopts the preferred AEWS filenames.

Preferred paths:

- `README.md`
- `PROJECT.md`
- `DECISIONS.md`
- `HANDOFF.md` when active work exists
- `docs/validation-checklist.md`
- `standard/scopes.md`
- `standard/adapters.md`
- adapter files that actually exist

Missing required canonical files may be failures in template mode.

### Adoption Mode

Adoption mode validates an existing repository without requiring it to rename
equivalent documents.

It should identify or accept mappings for these roles:

- Project: durable repository facts, commands, and boundaries;
- Decisions: accepted choices and rationale;
- Handoff: active continuation state, when present;
- Experiment: temporary evidence, when present;
- Adapter: harness-specific loading and behavior.

For example, an existing repository may use `ARCHITECTURE.md`, `RULES.md`, or
`WORKING-CONTEXT.md` for part of these roles. The validator should report the
mapping it used. A preferred filename that is absent should not be a failure
when an explicit equivalent role is mapped.

### Adoption Mapping Contract

The ordinary application evaluation showed that a mature Project role may need
one primary router plus narrower supplemental documents. Adoption mode
therefore accepts a small JSON mapping:

```json
{
  "version": 1,
  "mode": "adoption",
  "roles": {
    "project": {
      "primary": "README.md",
      "supplements": ["docs/architecture.md"]
    },
    "decisions": {"status": "missing"},
    "handoff": {"status": "inactive"},
    "experiment": {"status": "inactive"}
  },
  "adapters": [
    {"tool": "codex", "path": "AGENTS.md"}
  ]
}
```

The default checked-in filename is `aews.json`. A caller may provide another
path explicitly so a repository can be evaluated without modification. The
validator must never generate or rewrite this file.

Mapping rules:

- every mapped role has exactly one primary path;
- a role may have zero or more narrower supplements;
- all paths are repository-relative and must resolve inside the repository;
- `missing` means the role should exist but has no canonical owner yet and must
  produce a warning;
- `inactive` is allowed only for lifecycle-dependent Handoff and Experiment
  roles;
- adapters are declared explicitly by tool and path;
- the manifest contains routing metadata only, never architecture facts,
  decisions, commands, task state, or copied adapter instructions.

The first implementation must not guess canonical ownership from content and
silently treat that guess as authoritative.

Both modes should require only the adapters actually used by the repository.

## Checks

### 1. Adapter Line Counts

Purpose: catch adapter bloat before it becomes the project knowledge base.

Suggested checks:

- root `AGENTS.md` under 40 lines,
- each tool adapter under 30 lines,
- Cursor rule adapter under 30 lines.

Result type: warning by default.

Rationale: a longer adapter may be justified by tool-specific syntax, but it should trigger review.

### 2. Canonical Role Presence

Purpose: confirm that adapters have canonical document roles to point at.

Suggested template-mode checks:

- `PROJECT.md` exists,
- `DECISIONS.md` exists,
- `docs/validation-checklist.md` exists,
- `standard/scopes.md` exists,
- `standard/adapters.md` exists.

Suggested adoption-mode checks:

- the Project role has one identified primary home,
- the Decisions role is mapped or explicitly marked `missing`,
- active work has a mapped Handoff and inactive work may mark it `inactive`,
- each mapped primary and supplement resolves to an existing file,
- each supplement has narrower ownership and is routed from its primary,
- `missing` produces a warning and `inactive` is used only for allowed roles,
- no role mapping silently claims the same section as two independent sources
  of truth.

Result type: failure for missing core roles in the AEWS template repository;
warning for missing or ambiguous roles during incremental adoption.

Rationale: AEWS defines document roles and preferred filenames. Adoption may be
incremental and may use equivalent documents, but canonical ownership must
remain explicit.

### 3. Adapter Read Order References

Purpose: detect adapters that do not route to canonical documents.

Suggested checks against the resolved role mapping:

- existing adapters route to the Project role,
- existing adapters route to the Decisions role,
- existing adapters route to the Handoff role or explicitly explain when
  handoff is absent,
- adapter references resolve to existing files.

Result type: warning.

Rationale: adapter syntax differs across tools, so this should remain a text-level hint.

### 4. Mapped Document References

Purpose: catch stale local links that make a canonical router unreliable.

Suggested checks:

- repository-local Markdown paths in mapped documents resolve,
- mapped supplements are referenced by their primary document,
- missing paths include the referring file and line number,
- fenced code, URLs, anchors, globs, angle-bracket placeholders, common example
  paths, and a standalone generic `SKILL.md` are excluded.

Result type: warning.

Install-generated or tool-generated paths may still warn because determining
their runtime existence would require tool-specific semantic behavior.

Rationale: the ordinary application evaluation found intended canonical files
under a documentation directory while primary documents still referenced old
root paths. Modification time alone could not determine which content was
authoritative.

### 5. Obvious Duplicate Sentences

Purpose: catch copied durable facts across canonical files and adapters.

Suggested checks:

- compare normalized full sentences across adapter files and canonical files,
- ignore short sentences under a small word threshold,
- ignore boilerplate warnings such as "Do not copy durable knowledge into this file",
- report repeated long sentences with file paths and line numbers.

Result type: warning.

Rationale: duplication detection should guide review, not decide intent.

### 6. Forbidden Runtime Feature Mentions

Purpose: prevent the AEWS core standard from drifting into an agent harness by
accident.

Suggested terms:

- `hook`
- `MCP`
- `memory runtime`
- `security policy engine`
- `agent runtime`
- `automatic agent profile generation`
- `complex CLI`

Result type: warning.

Allowed contexts:

- non-goal sections,
- deferred roadmap sections,
- validation warnings,
- boundary explanations.

Rationale: the validator should flag these terms for review, not ban them outright.

### 7. Template Minimality Hints

Purpose: catch templates that start acting like framework scaffolds.

Suggested terms in templates:

- language-specific package managers,
- cloud providers,
- AI vendors,
- CI products,
- deployment platforms,
- framework-specific commands.

Result type: warning.

Rationale: templates should stay neutral unless a future accepted decision changes that rule.

## Output

The validator should produce plain text suitable for a pull request comment or local terminal output.

Suggested format:

```text
AEWS validation

Mode: adoption
Role mapping:
- Project: docs/architecture.md
- Project supplements: docs/operations.md
- Decisions: missing
- Handoff: WORKING-CONTEXT.md

Failures:
- None

Warnings:
- Decisions role is missing.
- adapters/codex/AGENTS.md has 46 lines; soft limit is 30.
- Broken local document reference in README.md:42: docs/setup.md.
- Possible duplicate sentence in PROJECT.md:12 and AGENTS.md:18.
- Runtime boundary term "MCP" found in docs/new-feature.md:22.

Manual review still required:
- Scope placement
- Lifecycle placement
- Decision quality
```

## Exit Codes

The first implementation uses:

- `0`: no failures,
- `1`: one or more failures,
- `2`: validator usage error.

Warnings alone should not fail validation unless a release checklist explicitly
decides otherwise.

## First Implementation

The implementation evidence gate is satisfied: the manual checklist has been
used on ECC and one ordinary full-stack application repository.

The evaluations are recorded in:

- `examples/reference-evaluations/ecc-v2.0.0.md`;
- `examples/reference-evaluations/full-stack-application.md`.

Together they demonstrate why adoption mode must be role-aware, why Project may
have a primary router plus supplements, and why adapter length remains a
warning.

The implementation:

- is a local documented Python standard-library script,
- does not publish a package,
- does not modify target files,
- uses transparent text checks instead of hidden heuristics.

## Open Questions

- Should warning thresholds become configurable before v1.0?
- Should duplicate detection ignore all quoted checklist text by default?
- Which repository-local Markdown link forms can be checked without adding a
  Markdown parser dependency?
- Should a missing Decisions role become a failure after an adoption repository
  explicitly declares itself fully AEWS-compliant?
