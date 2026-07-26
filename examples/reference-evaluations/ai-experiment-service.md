# AI Experiment Service Reference Evaluation

This document records a read-only AEWS adoption evaluation of an existing
Python service repository with both Codex and Claude Code instructions,
long-running experiment documentation, and generated Markdown result artifacts.
Business implementation details are intentionally omitted.

## Snapshot

- Repository type: AI experiment and HTTP service
- Reviewed commit: `449c408`
- Review date: 2026-07-26
- Working tree: contained pre-existing tracked and untracked changes
- Status digest before evaluation:
  `5e079c8e8c72865e6fa82d832c8ed93837e0df0fa2439528433f4856cef66b27`
- Status digest after evaluation: identical

The target repository was never modified. No dependencies, tests, notebooks,
models, services, APIs, or deployment commands were run.

## External Role Mapping

The evaluation used an external mapping rather than asking the target to adopt
AEWS filenames:

| AEWS Role | Existing Surface | Result |
| --- | --- | --- |
| Project | root `README.md` | Present |
| Project supplement | `docs/script-first-development.md` | Present and routed from the primary |
| Decisions | none | Missing |
| Handoff | none | Missing |
| Experiment | active dataset evaluation document | Present |
| Codex adapter | root `AGENTS.md` | Present in working tree |
| Claude adapter | root `CLAUDE.md` | Present |

An active experiment report was not reclassified as Handoff because it did not
own the complete continuation contract: current goal, last completed step, next
step, blockers, evidence, and expiration.

## First Validator Result

The first adoption run reported zero failures and 33 warnings:

- eight useful role or adapter warnings;
- twenty-five noisy broken-reference warnings for generated output names such
  as bare inline-code `summary.md`, `batch_summary.md`, and similar artifacts.

Those artifact names describe files produced inside result directories at
runtime. They are not links to checked-in repository documents.

## Validator Refinement

The reference rule was narrowed using evidence from this repository:

- normal Markdown links remain checked;
- directory-qualified inline paths remain checked;
- explicit `./` and `../` inline paths remain checked;
- known canonical root filenames remain checked;
- other bare `.md` names in inline code are treated as ambiguous prose or
  generated artifacts, not repository links.

The adoption-warning fixture now proves that an explicit Markdown link to a
missing document is still reported while generated artifact basenames are not.

## Final Validator Result

The second run reported zero failures and eight warnings:

- Decisions role missing;
- Handoff role missing;
- both adapters exceed their soft line limits;
- neither adapter routes to the Project primary;
- neither adapter routes to the active Experiment primary.

These warnings match the manual review and are actionable without requiring the
target repository to rename documents. No remaining warning was identified as
generated-artifact noise.

## Findings

1. Existing services may use `.md` as a generated report extension, so file
   suffix alone is insufficient evidence of a repository document link.
2. A dirty target can still be evaluated safely when the mapping is external
   and before/after status digests are recorded.
3. A development change log can be a valid Project supplement when the primary
   explicitly routes to it and its ownership is narrower.
4. An active experiment is not automatically the current Handoff.
5. Codex and Claude Code files can both exist while still exposing separate,
   oversized copies of project knowledge rather than one canonical route.

## Mapping Template Implication

The three reference evaluations now cover a large harness, an ordinary
full-stack application, and an experiment-heavy service. Their mappings use the
same version, mode, role, supplement, missing/inactive, and adapter fields.
This is enough evidence to publish a reusable routing-only mapping template;
the template does not need another schema field.
