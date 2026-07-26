# Validation Checklist

Use this checklist before accepting changes to AEWS documents, templates, examples, or adapters.

The checklist remains intentionally manual while v0.2 validates it against
real repositories. `scripts/aews_validate.py` now automates the stable
mechanical subset; scope, lifecycle freshness, decision quality, and ownership
still require manual review.

## Applying The Checklist

Use template mode for the AEWS template repository and repositories that adopt
the preferred AEWS filenames. Use adoption mode for an existing repository
that has equivalent canonical documents under different names.

In adoption mode, record the primary file for each applicable Project,
Decisions, Handoff, and Experiment role plus every declared Adapter before
evaluating the sections below. `aews.json` is the optional repeatable mapping
format. Equivalent filenames and narrower supplements are allowed; ambiguous or
duplicated ownership is not.

## 1. Scope Placement

- Every new durable fact has one primary scope: Global, Workspace, Repo, or Experiment.
- Personal preferences are not added to public templates unless they are neutral recommendations.
- Temporary findings are kept in experiment or handoff documents, not canonical standards.
- Cross-repo rules are not mixed into repo-specific templates.

Fail condition: the same fact could reasonably belong to multiple active files because the scope is unclear.

## 2. Lifecycle Placement

- Working state is in `HANDOFF.md` or an equivalent active state document.
- Accepted rationale is in `DECISIONS.md` or an equivalent decision log.
- Stable repo facts are in `PROJECT.md` or an equivalent project document.
- Experiments include hypothesis, method, artifacts, result, conclusion, and close condition.
- Stale handoff or experiment content is archived or removed from active read order.
- A task plan is treated as Handoff only when it records current goal, last
  completed step, next step, blockers, evidence, and expiration.

Fail condition: an agent adapter contains task history, experiment logs, or long-lived decision rationale.

## 3. Adapter Thinness

- Root `AGENTS.md` remains a routing file, not the project knowledge base.
- Adapter files contain read order and tool-specific behavior only.
- Codex, Claude Code, Cursor, and Gemini adapters point to canonical documents instead of copying them.
- Adapter file growth is justified by a tool-specific need.

Suggested soft limits:

- root `AGENTS.md`: under 40 lines,
- individual tool adapter: under 30 lines,
- Cursor rule adapter: under 30 lines.

Fail condition: an adapter repeats a durable project fact already present in canonical docs.

## 4. Canonical Consistency

- `README.md` explains the project at a high level without becoming a full specification.
- `docs/architecture.md` remains the primary architecture explanation.
- `standard/scopes.md` remains the primary scope model.
- `standard/adapters.md` remains the primary adapter rule source.
- `docs/adapter-matrix.md` remains the primary tool mapping source.
- `docs/roadmap.md` matches the current phase.
- In adoption mode, every applicable canonical role has one recorded primary
  document, even when preferred AEWS filenames are not used.
- Every supplement exists, has narrower ownership, and is routed from its
  primary document.
- Adapter references resolve to the recorded canonical documents.
- Repository-local Markdown references in mapped canonical documents resolve.

Fail condition: two canonical documents define conflicting rules for the same concept.

## 5. Template Minimality

- Templates include only fields required to guide placement, continuation, or validation.
- Templates do not assume a programming language, package manager, cloud provider, or AI vendor.
- Optional sections are clearly optional or omitted.
- Examples remain smaller than the standard they demonstrate.

Fail condition: a template starts acting like a framework scaffold instead of
remaining a minimal document-role starting point.

## 6. ECC Boundary

- New features do not turn AEWS into an agent harness by accident.
- Hooks, MCP catalogs, memory runtimes, and security policy engines remain deferred unless explicitly accepted.
- ECC is treated as a reference point, not a structure to clone.

Fail condition: the change adds runtime behavior without first updating `docs/roadmap.md` and `DECISIONS.md`.

## 7. Release Readiness

Before publishing or tagging a version:

- `git status --short --branch` is clean.
- `LICENSE` exists.
- `README.md` states goals and non-goals.
- `DECISIONS.md` records major architectural choices.
- `HANDOFF.md` reflects the current continuation state.
- At least one minimal example passes this checklist.

Suggested commands:

```bash
git status --short --branch
find . -maxdepth 6 -path ./.git -prune -o -path ./ECC -prune -o -type f -print
wc -l AGENTS.md adapters/codex/AGENTS.md adapters/claude-code/CLAUDE.md adapters/cursor/.cursor/rules/aews.mdc adapters/gemini/GEMINI.md
rg -n "TODO|TBD|copy|duplicate|harness|MCP|hook|memory" README.md docs standard templates adapters examples
python3 scripts/aews_validate.py . --mode template
python3 -m unittest discover -s tests -p 'test_*.py' -v
```
