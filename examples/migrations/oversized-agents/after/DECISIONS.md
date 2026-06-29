# DECISIONS

## Decisions

### 2026-05-10: Keep the site static

Status: Accepted

Scope: Repo

Context: The site should be deployable to a generic static host without a hosted database.

Decision: Atlas Notes will generate site data before deployment and serve the runtime as static assets.

Consequences: Import and search indexing must happen before deployment. Runtime operations stay simple.

Evidence: `PROJECT.md`
### 2026-05-18: Keep generated files out of routine reviews

Status: Accepted

Scope: Repo

Context: Generated data can create noisy diffs that obscure source changes.

Decision: Reviews should focus on source Markdown and generator code. Generated files should change only when their source changed or regeneration is the explicit task.

Consequences: Contributors must state when generated output is intentionally refreshed.

Evidence: `PROJECT.md`
