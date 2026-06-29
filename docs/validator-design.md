# Validator Design

This document defines the intended scope for a future lightweight AEWS validator. It does not implement the validator.

The validator should automate only mechanical checks that support `docs/validation-checklist.md`. It must not replace human review of scope, lifecycle, or architectural intent.

## Goals

- Catch obvious adapter bloat.
- Confirm expected canonical files exist.
- Detect likely duplicated durable context.
- Flag forbidden runtime features introduced before they are accepted.
- Produce review hints that point back to `docs/validation-checklist.md`.

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

The first version should inspect a repository directory and a small set of known AEWS paths.

Expected paths:

- `README.md`
- `PROJECT.md`
- `DECISIONS.md`
- `HANDOFF.md` when active work exists
- `docs/validation-checklist.md`
- `standard/scopes.md`
- `standard/adapters.md`
- adapter files that actually exist

The validator should not require every possible adapter. A repository should pass with only the adapters it uses.

## Checks

### 1. Adapter Line Counts

Purpose: catch adapter bloat before it becomes the project knowledge base.

Suggested checks:

- root `AGENTS.md` under 40 lines,
- each tool adapter under 30 lines,
- Cursor rule adapter under 30 lines.

Result type: warning by default.

Rationale: a longer adapter may be justified by tool-specific syntax, but it should trigger review.

### 2. Canonical File Presence

Purpose: confirm that adapters have canonical documents to point at.

Suggested checks:

- `PROJECT.md` exists,
- `DECISIONS.md` exists,
- `docs/validation-checklist.md` exists,
- `standard/scopes.md` exists,
- `standard/adapters.md` exists.

Result type: failure for missing core files in an AEWS template repository; warning for adoption in an existing repository.

Rationale: adoption may be incremental, but the AEWS template itself should keep core files present.

### 3. Adapter Read Order References

Purpose: detect adapters that do not route to canonical documents.

Suggested checks:

- existing adapters mention `PROJECT.md`,
- existing adapters mention `DECISIONS.md`,
- existing adapters mention `HANDOFF.md` or explicitly explain when handoff is absent.

Result type: warning.

Rationale: adapter syntax differs across tools, so this should remain a text-level hint.

### 4. Obvious Duplicate Sentences

Purpose: catch copied durable facts across canonical files and adapters.

Suggested checks:

- compare normalized full sentences across adapter files and canonical files,
- ignore short sentences under a small word threshold,
- ignore boilerplate warnings such as "Do not copy durable knowledge into this file",
- report repeated long sentences with file paths and line numbers.

Result type: warning.

Rationale: duplication detection should guide review, not decide intent.

### 5. Forbidden Runtime Feature Mentions

Purpose: prevent AEWS v0.1 from drifting into an agent harness by accident.

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

### 6. Template Minimality Hints

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

Failures:
- Missing PROJECT.md

Warnings:
- adapters/codex/AGENTS.md has 46 lines; soft limit is 30.
- Possible duplicate sentence in PROJECT.md:12 and AGENTS.md:18.
- Runtime boundary term "MCP" found in docs/new-feature.md:22.

Manual review still required:
- Scope placement
- Lifecycle placement
- Decision quality
```

## Exit Codes

If implemented later:

- `0`: no failures,
- `1`: one or more failures,
- `2`: validator usage error.

Warnings alone should not fail v0.1 validation unless a release checklist explicitly decides otherwise.

## Implementation Constraints

Do not implement this design until the manual checklist has been used on more examples.

When implementation becomes appropriate:

- keep the first version as a local script or documented command,
- avoid dependency-heavy parsing,
- avoid package publishing,
- avoid modifying files,
- prefer transparent text checks over hidden heuristics.

## Open Questions

- Should warning thresholds become configurable before v1.0?
- Should adoption repositories and the AEWS template repository use different failure levels?
- Should duplicate detection ignore all quoted checklist text by default?
