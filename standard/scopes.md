# AEWS Scope Model

AEWS uses four scopes.

## Global

Global context applies across most or all work.

Examples:

- preferred response language,
- general engineering style,
- personal review expectations,
- safe shell command preferences.

Global context is usually private or local. It should not be embedded in public templates unless it is a neutral recommendation.

## Workspace

Workspace context applies across several repos in one environment.

Examples:

- directory conventions,
- shared infrastructure assumptions,
- cross-repo release process,
- shared agent handoff pattern.

Workspace context is useful when several repos need the same operating model.

## Repo

Repo context applies to one repository.

Examples:

- architecture,
- setup commands,
- test commands,
- service boundaries,
- known operational risks,
- contribution rules.

Repo context is the most common source for agent-facing instructions.

## Experiment

Experiment context is temporary and evidence-oriented.

Examples:

- benchmark notes,
- prototype comparison,
- prompt trial,
- migration dry run,
- tool evaluation.

Experiment context must not become durable knowledge until its conclusion is reviewed.

## Scope Decision Algorithm

```text
if applies to most future work:
    Global
else if applies to multiple repos in one environment:
    Workspace
else if applies to one repo and is durable:
    Repo
else:
    Experiment or Working State
```
