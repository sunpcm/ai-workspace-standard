# Contributing

AEWS is a workspace knowledge standard. Contributions should make knowledge easier to place, maintain, and project into agent-specific files without turning the repository into an agent runtime.

## Language

Documentation is written in English. Other languages are added as
`<name>.<lang>.md` translations beside the English original, as in
`README.zh-CN.md`; update both in the same change. `TODO.md` is the exception
and stays in the maintainer's language, because it is a task queue rather than
a canonical knowledge role. `tests/test_language_boundary.py` enforces this,
and the 2026-08-09 entry in `DECISIONS.md` records the measurement behind it.

## Read First

Before changing files, read:

1. `README.md`
2. `PROJECT.md`
3. `DECISIONS.md`
4. `HANDOFF.md` if present
5. `TODO.md` or the active task tracker if present
6. `docs/vision.md`
7. `docs/architecture.md`
8. `docs/document-lifecycle.md`
9. `docs/cross-agent-continuity.md`
10. `standard/scopes.md`
11. `standard/adapters.md`
12. `docs/validation-checklist.md`

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

For cross-agent work, verify the existing checkpoint against Git and tests,
record only meaningful checkpoints, and use separate branches or worktrees for
concurrent changes. A handoff is not a lock or a substitute for implementation
evidence.

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

Current compatibility implementation and runtime evidence prioritize Codex and
Claude Code. Contributions may propose another adapter through the open
contract, but a reference projection must not be presented as actively tested
support without reproducible evidence and an accepted priority change.

## Validate Before Submitting

Run the manual checklist in `docs/validation-checklist.md` against changed files.

At minimum, inspect:

```bash
git status --short --branch
find . -maxdepth 6 -path ./.git -prune -o -path ./ECC -prune -o -type f -print
wc -l AGENTS.md adapters/codex/AGENTS.md adapters/claude-code/CLAUDE.md adapters/cursor/.cursor/rules/aews.mdc adapters/gemini/GEMINI.md
rg -n "TODO|TBD|copy|duplicate|harness|MCP|hook|memory" README.md docs standard templates adapters examples
python3 scripts/aews_validate.py . --mode template
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Then confirm:

- new durable facts have one primary scope,
- lifecycle placement is clear,
- adapters remain thin,
- cross-agent checkpoint claims are verifiable and do not imply live presence,
- templates stay minimal,
- no runtime features are introduced without an accepted decision,
- the validator reports no unexplained failures or warnings,
- validator tests pass when validator code, mapping rules, or fixtures change.
