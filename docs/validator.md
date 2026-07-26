# Validator

AEWS v0.2 includes a dependency-free, read-only validator for the mechanical
checks that stabilized through manual reference evaluations.

The validator supports Python 3.10 or newer and does not install packages,
modify the target repository, generate mappings, or replace manual review.

## Run Template Mode

Use template mode for the AEWS repository or a repository using preferred AEWS
filenames:

```bash
python3 scripts/aews_validate.py . --mode template
```

Template mode requires `README.md`, `PROJECT.md`, and `DECISIONS.md`. When the
repository contains the AEWS `standard/` directory, it also requires the core
standard and validation documents.

## Run Adoption Mode

If `aews.json` exists at the target repository root, adoption mode is selected
automatically:

```bash
python3 <aews-repo>/scripts/aews_validate.py <target-repo>
```

Use an external mapping to evaluate a repository without modifying it:

```bash
python3 <aews-repo>/scripts/aews_validate.py <target-repo> \
  --mode adoption \
  --config <mapping-file>.json
```

The mapping contract is defined in `docs/validator-design.md`. `aews.json` is
routing metadata only and must not contain project facts, decisions, commands,
or task state.

## Implemented Checks

The first version checks:

- template and adoption mode requirements;
- `aews.json` version, allowed properties, roles, lifecycle states, and adapter
  entries;
- repository-relative path containment, file presence, duplicate ownership,
  and direct symlinks;
- primary-to-supplement routing;
- declared adapter references and soft line limits;
- repository-local Markdown document references in mapped files;
- obvious exact durable-sentence duplication between mapped documents and
  adapters;
- stable failures, warnings, manual-review reminders, and exit codes.

Warnings do not fail validation.

## Document Reference Boundary

The dependency-free reference check recognizes:

- normal Markdown links to `.md` or `.mdc` files;
- inline-code paths ending in `.md` or `.mdc`;
- repository-root paths beginning with `/`;
- repository-relative paths in mapped documents.

It ignores fenced code blocks, URLs, anchors, globs, angle-bracket placeholders,
common `your-*` / `example-*` paths, and a standalone generic `SKILL.md` name.

Install-generated or tool-generated document paths cannot always be identified
mechanically. They may produce warnings and require manual review.

## Exit Codes

- `0`: no failures; warnings may still exist;
- `1`: one or more validation failures;
- `2`: invocation or mapping-read error.

## Run Tests

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

The fixtures cover valid template mode, valid adoption mode, warning-only
adoption, invalid mapping, line-count warnings, CLI exit codes, and read-only
behavior. The AEWS repository itself is also validated by the test suite.

## Manual Review Still Required

The validator does not decide:

- whether scope placement is correct;
- whether handoff or experiment state is fresh;
- whether a decision is technically sound;
- whether supplemental ownership is appropriately narrow;
- whether an install-generated path warning is acceptable;
- whether a repository is ready to claim full AEWS compliance.
