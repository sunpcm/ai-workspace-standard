# Contributing

AEWS is a workspace knowledge standard. Contributions should make knowledge easier to place, maintain, and project into agent-specific files without turning the repository into an agent runtime.

## Read First

Before changing files, read:

1. `README.md`
2. `PROJECT.md`
3. `DECISIONS.md`
4. `HANDOFF.md` if present
5. `docs/vision.md`
6. `docs/architecture.md`
7. `docs/document-lifecycle.md`
8. `standard/scopes.md`
9. `standard/adapters.md`
10. `docs/validation-checklist.md`

For example-only changes, also read the relevant `examples/*/README.md`.

## Decide Scope Before Writing

Classify new information before choosing a file:

- Global: applies across most future work. Keep this out of public templates unless it is a neutral recommendation.
- Workspace: applies across multiple repositories in one working environment.
- Repo: durable facts, commands, boundaries, and risks for one repository.
- Experiment: temporary hypotheses, trials, artifacts, and conclusions.

If the same fact seems to belong in multiple active files, the scope is not clear enough yet. Clarify the scope before writing more content.

## Place Information by Lifecycle

Use the lifecycle model in `docs/document-lifecycle.md`:

- Put stable repo facts in `PROJECT.md` or canonical docs.
- Put accepted rationale in `DECISIONS.md`.
- Put active continuation state in `HANDOFF.md`.
- Put temporary exploration in an experiment document.
- Archive or remove stale active context when it no longer guides future work.

## Update Decisions and Handoffs

Update `DECISIONS.md` when a contribution accepts a durable choice that should constrain future work. Include status, scope, context, decision, consequences, and evidence.

Update `HANDOFF.md` when the next contributor needs current state, blockers, evidence, or the next concrete step. Do not promote handoff notes into durable knowledge until they are stable and reviewed.

## Keep Adapters Thin

Adapters are projections, not sources of truth.

Do not copy durable knowledge into:

- root `AGENTS.md`,
- tool-specific `AGENTS.md`,
- `CLAUDE.md`,
- Cursor rules,
- `GEMINI.md`,
- future agent adapter files.

Adapters should contain read order, tool-specific behavior, and a warning not to duplicate canonical knowledge. If an adapter needs architecture, task history, decisions, or command references, move that content into canonical documents and link to it.

## Validate Before Submitting

Run the manual checklist in `docs/validation-checklist.md` against changed files.

At minimum, inspect:

```bash
git status --short --branch
find . -maxdepth 6 -path ./.git -prune -o -path ./ECC -prune -o -type f -print
wc -l AGENTS.md adapters/codex/AGENTS.md adapters/claude-code/CLAUDE.md adapters/cursor/.cursor/rules/aews.mdc adapters/gemini/GEMINI.md
rg -n "TODO|TBD|copy|duplicate|harness|MCP|hook|memory" README.md docs standard templates adapters examples
```

Then confirm:

- new durable facts have one primary scope,
- lifecycle placement is clear,
- adapters remain thin,
- templates stay minimal,
- no runtime features are introduced without an accepted decision.
