# ECC v2.0.0 Reference Evaluation

This document records a manual AEWS evaluation of a local ECC checkout. ECC is
used as external design evidence, not vendored source and not an AEWS adoption
example.

## Snapshot

- Reference repository: `affaan-m/ECC`
- Version file: `2.0.0`
- Reviewed commit: `6a9f075c`
- Review date: 2026-07-26
- Local checkout: `ECC/`, ignored by the AEWS repository

The reviewed checkout contained 67 agent definitions, 281 top-level skills, 94
legacy command files, 232 script files, and 211 test files. These counts
describe the reviewed snapshot only and are not compatibility guarantees.

## Evaluation Boundary

ECC and AEWS have different purposes:

- ECC is an installable agent harness and workflow layer.
- AEWS is a workspace knowledge standard.

Hooks, MCP configuration, orchestration, memory runtime, installers, dashboards,
and domain skill catalogs are therefore reference surfaces, not missing AEWS
v0.2 deliverables.

The useful comparison is whether ECC provides evidence that improves AEWS scope,
lifecycle, projection, and validation rules.

## Checklist Findings

### Scope Placement

Result: useful evidence, not an AEWS pass or fail.

ECC's memory contract distinguishes project, team, and user scopes. AEWS adds a
separate Experiment scope and keeps scope classification independent from
document lifecycle. The models are compatible at a conceptual level but should
not be treated as identical.

Validator implication: an adoption repository may use different scope names and
document layouts. Validation should look for equivalent governed roles before
warning about preferred AEWS filenames.

### Lifecycle Placement

Result: strong reference evidence.

ECC separates working context, rules, skills, sessions, and memory kinds. Its
memory vault also distinguishes unreviewed context from governed project
artifacts and requires human promotion.

AEWS already defines promotion from working state or experiment output into
decisions and knowledge. A future standard revision should consider making the
review boundary explicit without adopting the ECC memory runtime.

### Adapter Thinness

Result: warning under AEWS rules.

ECC's cross-harness architecture says harness adapters should adapt loading,
event shapes, command names, and platform limits. The reviewed root `AGENTS.md`
was 172 lines and `CLAUDE.md` was 82 lines, so a line-count check would warn.

This does not prove the files are invalid for ECC. It proves that adapter size
must remain a warning with evidence, not an automatic failure. Duplicate durable
facts and unclear source ownership are stronger findings than length alone.

### Canonical Consistency

Result: partial manual pass.

ECC documents shared workflow sources and harness-specific adaptation. It also
has manifests, schemas, validation scripts, and a generated adapter compliance
matrix. A complete consistency audit of all ECC surfaces was outside this
evaluation.

Validator implication: compatibility claims should carry an install or onramp
path, a verification method, known limitations, and a last-reviewed reference.

### Template Minimality

Result: not applicable.

ECC install profiles and scaffolds are harness distribution artifacts, not AEWS
document templates. Their size should not be evaluated using AEWS template
minimality rules.

### ECC Boundary

Result: pass for the AEWS boundary.

The comparison confirms that agents, skills, hooks, MCP configuration, memory
runtime, orchestration, installers, and dashboards belong to the harness layer.
AEWS may document integration boundaries but should not absorb those runtime
surfaces into the core standard.

### Release Readiness

Result: not evaluated.

The local clone was used as design evidence only. No ECC dependencies, tests,
installers, hooks, or runtime commands were executed.

## Validator Design Lessons

The first AEWS validator should:

1. distinguish the AEWS template repository from an existing adoption repo;
2. validate canonical document roles before requiring preferred filenames;
3. accept explicit role mappings or report equivalent-document hints;
4. keep adapter line limits as warnings;
5. prioritize duplicate durable facts and missing source ownership;
6. report compatibility evidence separately from document placement;
7. remain read-only and require manual scope and lifecycle review.

## Follow-Up Result

The required ordinary application evaluation is complete and recorded in
`examples/reference-evaluations/full-stack-application.md`. It confirmed the
need for a primary router plus supplements and produced the routing-only
`aews.json` mapping contract. The evidence gate for implementing stable
mechanical checks is satisfied.
