# Versioning

AEWS uses lightweight versioning so users can understand when a standard, template, example, or adapter change may affect their repositories.

v0.x remains allowed to change structure, but important changes must be explained in `DECISIONS.md` before release.

## Version Goals

- Make `v0.1.0` publishable without adding a complex release process.
- Clarify what counts as a breaking change during v0.x.
- Keep adapters and templates compatible with the canonical standard.
- Let examples follow the standard without becoming separate products.

## v0.x Compatibility

During v0.x, AEWS is still stabilizing. Structural changes are acceptable when they improve scope placement, lifecycle clarity, or adapter thinness.

A v0.x change is breaking when it requires adopters to change an existing AEWS repo to preserve the same behavior or meaning.

Examples of breaking changes:

- renaming a canonical role such as Project, Handoff, Decisions, or Experiment,
- changing the required minimal document set,
- changing the meaning of Global, Workspace, Repo, or Experiment scope,
- changing adapter rules so existing thin adapters become invalid,
- adding required template fields that existing repositories must fill.

Examples of non-breaking changes:

- clarifying wording without changing placement rules,
- adding optional examples,
- adding a new optional adapter pattern,
- adding validation guidance that does not change acceptance rules,
- fixing commands in documentation.

## Adapter Changes

Adapter files are projections from canonical documents.

An adapter change is breaking only when it changes what users must put in an adapter or changes the expected read order in a way that existing repositories must follow.

Non-breaking adapter changes include:

- adding an optional adapter for a new tool,
- adding or refining the optional cross-agent continuity profile without
  changing the core document roles,
- clarifying that durable knowledge belongs in canonical documents,
- tightening examples while preserving the same adapter responsibility,
- documenting tool-specific syntax without changing AEWS roles.

Adapter changes must not create a second source of truth. If an adapter needs new durable content, update the canonical documents first.

## Template Changes

Templates should stay minimal. A template change is breaking when it changes the expected shape of a repository adopting AEWS.

Breaking template changes include:

- adding a required section,
- renaming a required section,
- changing a section from optional to required,
- removing a section that existing validation expects.

Non-breaking template changes include:

- adding optional prompts,
- improving wording,
- removing vendor-specific phrasing,
- simplifying examples without changing required roles.

When a template change is breaking, record the rationale in `DECISIONS.md` and explain the migration path in the release notes or release checklist.

## Example Changes

Examples should track the current standard version. They are evidence for the standard, not independent compatibility targets.

An example change is breaking only if users are told to treat that example as a stable template and the example structure changes in a required way.

Otherwise, examples may change to:

- better demonstrate scope placement,
- remove duplicated adapter knowledge,
- improve validation coverage,
- align with updated templates.

When examples reveal a problem in the standard, update the standard or checklist instead of working around the problem in the example.

## Release Notes

Before tagging a version, summarize:

- changed canonical roles or scope rules,
- changed template requirements,
- changed adapter expectations,
- added or updated examples,
- known migration actions for adopters.

For v0.1.0, keep release notes short and link to `docs/release-checklist.md` once it exists.

## Decision Rule

Record a decision when a versioning change:

- changes a canonical role,
- changes required minimal adoption,
- changes adapter responsibilities,
- changes template requirements,
- introduces or removes a validation acceptance rule.

Do not record a decision for wording-only improvements unless they change future behavior.
