# Adoption Mapping Template

`aews.example.json` is a copy-and-edit example for repositories that already
have project documentation. It maps AEWS roles to existing files; it does not
create new sources of truth.

## Use It

1. Copy `aews.example.json` to the target repository as `aews.json`, or keep an
   edited copy outside the target for a read-only evaluation.
2. Replace every example path with a repository-relative path that already
   exists.
3. Remove adapters the repository does not use. Add another adapter only when
   that adapter file exists.
4. For Handoff or Experiment, use `inactive` only when that lifecycle state is
   genuinely inactive. Otherwise map its primary document.
5. Use `missing` when a role should exist but has no canonical owner yet. A
   missing role is an adoption warning, not a substitute document.
6. Run the validator and then complete the manual adoption review.

Checked-in usage:

```bash
cp <aews-repo>/templates/adoption/aews.example.json ./aews.json
$EDITOR ./aews.json
python3 <aews-repo>/scripts/aews_validate.py .
```

Read-only evaluation:

```bash
cp <aews-repo>/templates/adoption/aews.example.json /tmp/aews-target.json
$EDITOR /tmp/aews-target.json
python3 <aews-repo>/scripts/aews_validate.py <target-repo> \
  --mode adoption \
  --config /tmp/aews-target.json
```

## Field Rules

- `version` is currently `1`.
- `mode` is `adoption`.
- `roles` contains Project, Decisions, Handoff, and Experiment.
- A mapped role has exactly one `primary` and optional narrower `supplements`.
- An unmapped role has one `status`: `missing`, or `inactive` for Handoff and
  Experiment only.
- `adapters` declares only adapter files that the repository actually uses.
- Every path is repository-relative and must remain inside the target.

Do not add architecture facts, commands, decisions, task state, timestamps,
runtime memory, or tool instructions to this file. Put that information in the
canonical document that owns the corresponding role.

The authoritative contract and failure behavior are in
`docs/validator-design.md`; validator usage is in `docs/validator.md`.
