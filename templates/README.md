# Templates

Templates are starting points for AEWS document roles. They are not project scaffolds and should not define a language stack, package manager, cloud provider, AI vendor, or runtime workflow.

Use only the templates that match real repository needs.

## Available Templates

| Template | Purpose | Use When |
| --- | --- | --- |
| `repo/PROJECT.md` | Durable repo facts, commands, architecture boundaries, verification, and known risks | A repository needs one canonical project context file |
| `decision/DECISIONS.md` | Accepted decisions with context, consequences, and evidence | Future work should be constrained by prior choices |
| `handoff/HANDOFF.md` | Active continuation state | Work is in progress and another person or agent needs exact next context |
| `experiment/EXPERIMENT.md` | Temporary hypothesis, method, artifacts, result, and conclusion | A trial or investigation needs evidence before becoming durable knowledge |

## When Not To Use A Template

Do not add a template just because AEWS has one.

Avoid a template when:

- the repository does not have that lifecycle state,
- the information already has a clear canonical home,
- the content would duplicate another active file,
- the document would be empty placeholder structure,
- the need is tool-specific and belongs in an adapter,
- the need is a runtime feature outside AEWS v0.1.

For example, a repository with no active work does not need `HANDOFF.md` until there is continuation state to preserve.

The Handoff template includes optional actor and commit metadata for
cross-agent continuity. These fields do not make the document a runtime log or
locking mechanism; omit them when they do not improve continuation.

## Keep Templates Minimal

Templates should include only fields that help with:

- scope placement,
- lifecycle placement,
- continuation,
- validation,
- decision evidence.

Do not add fields for:

- programming language,
- dependency manager,
- hosting platform,
- cloud provider,
- AI model or vendor,
- CI system,
- hook configuration,
- MCP server configuration,
- generated adapter output.

If a field is useful only for one project type, keep it out of the shared template and document it in that repo's `PROJECT.md`.

## Changing Templates

Before changing a template, check:

- Does this field support scope or lifecycle placement?
- Is it required for most adopters, or only one repo type?
- Does it duplicate content from a canonical standard document?
- Would existing adopters need to change their files?
- Should the change be recorded in `DECISIONS.md` under the versioning rules?

When changing templates, review these files:

1. `standard/documents.md`
2. `docs/document-lifecycle.md`
3. `docs/validation-checklist.md`
4. `docs/versioning.md`
5. relevant examples under `examples/`

Template changes that add required sections should include a migration note before release.

## Review Checklist

Accept a template change only when:

- it keeps the template smaller than the standard it supports,
- it does not bind AEWS to a vendor or stack,
- it does not turn templates into a framework scaffold,
- it preserves thin adapter rules,
- examples can still be understood without scripts or generators.
