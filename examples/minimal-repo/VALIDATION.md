# Minimal Repo Validation

This file records a manual pass through `docs/validation-checklist.md` for the minimal AEWS repo example.

## Result

Status: Pass with documented limitations.

The example demonstrates a small AEWS document set shared by Codex and Claude
Code projections. It does not claim to validate every adapter type, release
process, or runtime automation boundary.

## 1. Scope Placement

Pass.

- Repo facts are in `PROJECT.md`.
- Active continuation state is in `HANDOFF.md`.
- Accepted rationale is in `DECISIONS.md`.
- Both adapters contain only shared-state routing, a duplication warning, and
  the evidence-verification rule.

No Global or Workspace facts are introduced by this example.

## 2. Lifecycle Placement

Pass.

- `PROJECT.md` contains stable repo facts.
- `DECISIONS.md` records the accepted decision to keep the example documentation-only.
- `TODO.md` records the shared queue without copying it into either adapter.
- `HANDOFF.md` records current goal, state, evidence, open question, and expiration.
- No experiment document is present because the example does not run an experiment.

## 3. Adapter Thinness

Pass.

- `AGENTS.md` and `CLAUDE.md` stay below the adapter soft limit.
- Both point to the same canonical files instead of copying durable knowledge.
- No task history, decision rationale, architecture detail, or command reference appears in the adapter.

Not applicable: Cursor and Gemini adapters are not included in this minimal
example. Runtime discovery is recorded separately in the compatibility matrix.

## 4. Cross-Agent Continuity

Pass at the document-protocol level.

- Codex and Claude Code route to the same Project, Decisions, Handoff, and task
  queue roles.
- The handoff names the last completed and next steps plus inspectable evidence.
- Both adapters require verification rather than trusting prior-agent prose.
- The example does not claim real-time presence, locking, or transcript sync.

## 5. Canonical Consistency

Pass.

- The example README states the example purpose without becoming a specification.
- `PROJECT.md`, `DECISIONS.md`, and `HANDOFF.md` follow the lifecycle model used by the root standard.
- No rule in the example conflicts with `standard/scopes.md` or `standard/adapters.md`.

## 6. Template Minimality

Pass.

- The example is smaller than the standard it demonstrates.
- It does not introduce a language, package manager, cloud provider, AI vendor, hook, or generator.
- It uses only the minimum files needed to demonstrate repo facts, decisions,
  handoff state, a task queue, and two thin adapters.

## 7. ECC Boundary

Pass.

- The example does not add hooks, MCP catalogs, memory runtimes, security policy engines, or agent harness behavior.
- The handoff explicitly keeps the next step at controlled compatibility
  evidence rather than runtime implementation.

## 8. Release Readiness

Not applicable.

This example is not a release candidate. The relevant release-readiness
contribution is that it can be inspected manually and passes the scope,
lifecycle, adapter, continuity, consistency, template, and ECC boundary checks
above.

## Issues Found

- The minimal example covers two document projections but does not prove
  runtime discovery for every tool version.
- During this validation pass, the repository-level checklist command needed to inspect nested migration examples and only existing adapter files. The command was updated in `docs/validation-checklist.md`.

## Template or Standard Updates Needed

The optional Handoff metadata now makes actor, freshness, worktree, and commit
evidence easier to record without requiring a runtime.

The checklist remains usable for the minimal example when unsupported adapter types are recorded as not applicable.
