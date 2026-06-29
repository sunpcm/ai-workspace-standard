# Minimal Repo Validation

This file records a manual pass through `docs/validation-checklist.md` for the minimal AEWS repo example.

## Result

Status: Pass with documented limitations.

The example demonstrates the smallest useful AEWS document set for one repository. It does not claim to validate every adapter type, release process, or future automation boundary.

## 1. Scope Placement

Pass.

- Repo facts are in `PROJECT.md`.
- Active continuation state is in `HANDOFF.md`.
- Accepted rationale is in `DECISIONS.md`.
- The adapter contains only read order and a duplication warning.

No Global or Workspace facts are introduced by this example.

## 2. Lifecycle Placement

Pass.

- `PROJECT.md` contains stable repo facts.
- `DECISIONS.md` records the accepted decision to keep the example documentation-only.
- `HANDOFF.md` records current goal, state, evidence, open question, and expiration.
- No experiment document is present because the example does not run an experiment.

## 3. Adapter Thinness

Pass.

- `AGENTS.md` is 11 lines.
- It points to canonical files instead of copying durable knowledge.
- No task history, decision rationale, architecture detail, or command reference appears in the adapter.

Not applicable: Claude Code, Cursor, and Gemini adapters are not included in this minimal example. The example intentionally validates one thin adapter, not the full adapter matrix.

## 4. Canonical Consistency

Pass.

- The example README states the example purpose without becoming a specification.
- `PROJECT.md`, `DECISIONS.md`, and `HANDOFF.md` follow the lifecycle model used by the root standard.
- No rule in the example conflicts with `standard/scopes.md` or `standard/adapters.md`.

## 5. Template Minimality

Pass.

- The example is smaller than the standard it demonstrates.
- It does not introduce a language, package manager, cloud provider, AI vendor, hook, or generator.
- It uses only the minimum files needed to demonstrate repo facts, decisions, handoff state, and a thin adapter.

## 6. ECC Boundary

Pass.

- The example does not add hooks, MCP catalogs, memory runtimes, security policy engines, or agent harness behavior.
- The handoff explicitly keeps the next step at adapter comparison rather than runtime automation.

## 7. Release Readiness

Not applicable.

This example is not a release candidate. The relevant release-readiness contribution is that the example can be inspected manually and passes the scope, lifecycle, adapter, consistency, template, and ECC boundary checks above.

## Issues Found

- The minimal example does not cover multi-agent adapter comparison. This is intentional and should remain outside the minimal example unless the v0.1 scope changes.
- During this validation pass, the repository-level checklist command needed to inspect nested migration examples and only existing adapter files. The command was updated in `docs/validation-checklist.md`.

## Template or Standard Updates Needed

No template update is required from this validation pass.

The checklist remains usable for the minimal example when unsupported adapter types are recorded as not applicable.
