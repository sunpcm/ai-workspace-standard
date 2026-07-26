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

## v1.x Compatibility

Starting with v1.0, the stable surface includes the four scopes, canonical
document roles, thin-adapter responsibility, routing-only adoption mapping
version 1, and the validator's failure/warning boundary.

A change to that surface is breaking and requires a new AEWS major version when
it requires a conforming adopter to rename, move, reinterpret, or add required
content to preserve the same meaning. Examples include:

- renaming or removing a scope or canonical role;
- changing a currently optional lifecycle role into a required active file;
- making adapters own durable project knowledge;
- removing or changing the meaning of an `aews.json` version 1 field;
- promoting a warning to a failure without a migration path;
- adding a required template section or runtime dependency.

Backward-compatible optional roles, adapters, examples, and validator hints may
ship in a minor release. Clarifications and fixes that do not change acceptance
rules may ship in a patch release. Deprecate before removing whenever a
practical compatibility path exists.

The adoption mapping's `version` is its contract version, not automatically the
same as the AEWS release version. Breaking that JSON contract requires both a
new mapping version and the applicable AEWS major-version process.

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

Before tagging a version, update `CHANGELOG.md` and summarize:

- changed canonical roles or scope rules,
- changed template requirements,
- changed adapter expectations,
- added or updated examples,
- known migration actions for adopters.

Keep the checklist reusable and store the concrete audit under
`docs/releases/<version>-readiness.md`. A local readiness record must state
explicitly when tag, push, and release publication have not occurred.

For a stable release, the readiness record must map every published exit
criterion to authoritative evidence and distinguish local readiness from
external publication state.

## Decision Rule

Record a decision when a versioning change:

- changes a canonical role,
- changes required minimal adoption,
- changes adapter responsibilities,
- changes template requirements,
- introduces or removes a validation acceptance rule.

Do not record a decision for wording-only improvements unless they change future behavior.
