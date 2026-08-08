# Release Checklist

Use this checklist before tagging or publishing AEWS.

The checklist is intentionally manual. It should confirm that the repository
is ready to share, not add release automation.

Keep this file reusable. Record a concrete release audit under `docs/releases/`
so results, known limitations, and the owner-controlled publication boundary do
not overwrite the checklist itself.

## Target Version

- Version:
- Date:
- Release owner:
- Commit:

## 1. Git State

Required checks:

```bash
git status --short --branch
git log --oneline --decorate -5
```

Pass criteria:

- working tree is clean,
- release commit is identified,
- no unrelated local changes are included.

## 2. License

Required checks:

```bash
test -f LICENSE
sed -n '1,40p' LICENSE
```

Pass criteria:

- `LICENSE` exists,
- license matches the accepted decision in `DECISIONS.md`.

## 3. README

Required checks:

```bash
sed -n '1,220p' README.md
```

Pass criteria:

- README states goals and non-goals,
- README explains the canonical standard and adapter projection model,
- README does not claim AEWS is an agent runtime, hook system, MCP catalog, memory runtime, or security harness.

## 4. Decisions

Required checks:

```bash
sed -n '1,260p' DECISIONS.md
```

Pass criteria:

- major architecture choices are recorded,
- accepted decisions include scope, context, consequences, and evidence,
- release-relevant breaking changes are recorded according to `docs/versioning.md`.

## 5. Handoff

Required checks:

```bash
sed -n '1,220p' HANDOFF.md
```

Pass criteria:

- current goal is accurate,
- last completed step is accurate,
- next step is concrete,
- blockers are recorded,
- completed-work claims identify verifiable evidence,
- stale continuation state has been replaced.

## 6. Minimal Example

Required checks:

```bash
find examples/minimal-repo -maxdepth 2 -type f -print
sed -n '1,220p' examples/minimal-repo/VALIDATION.md
wc -l examples/minimal-repo/AGENTS.md examples/minimal-repo/CLAUDE.md
```

Pass criteria:

- minimal example includes project, decision, handoff, and two thin adapter files,
- `VALIDATION.md` records checklist results and limitations,
- both adapters remain thin and route to the same state.

## 7. Migration Example

Required checks:

```bash
find examples/migrations/oversized-agents -maxdepth 3 -type f -print
wc -l examples/migrations/oversized-agents/after/AGENTS.md
sed -n '1,220p' examples/migrations/oversized-agents/README.md
```

Pass criteria:

- `before/AGENTS.md` shows mixed architecture, command, decision, and task state,
- `after/AGENTS.md` remains under 30 lines,
- README explains what moved where and why.

## 8. Validation Checklist

Required checks:

```bash
git diff --check
find . -maxdepth 6 -path ./.git -prune -o -path ./ECC -prune -o -type f -print
wc -l AGENTS.md adapters/codex/AGENTS.md adapters/claude-code/CLAUDE.md adapters/cursor/.cursor/rules/aews.mdc adapters/gemini/GEMINI.md
rg -n "TODO|TBD|copy|duplicate|harness|MCP|hook|memory" README.md CONTRIBUTING.md docs standard templates adapters examples
python3 scripts/aews_validate.py . --mode template
python3 scripts/aews_validate.py tests/fixtures/runtime-loading --mode template
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Pass criteria:

- no whitespace errors,
- expected files are present,
- adapters remain within soft line limits or have a documented reason,
- keyword hits are reviewed and are either boundary explanations or intentional checklist terms,
- the validator reports no unexplained failures or warnings,
- validator regression tests pass.
- the runtime-loading fixture passes the same structural checks before any
  model-backed probe is considered.

## 9. Adapter Compatibility Evidence

Required checks:

```bash
sed -n '1,320p' docs/adapter-matrix.md
codex --version || true
claude --version || true
test -f .github/copilot-instructions.md || true
```

Pass criteria:

- each compatibility claim names its discovery surface and evidence status,
- structural validation is not presented as a runtime-loading test,
- unrun model-backed checks for any declared target are recorded as limitations,
- only Primary targets carry a runtime-loading claim; Secondary and extension
  targets are never implied to have one,
- each non-primary tool is labelled with its actual tier and does not block
  the primary compatibility track,
- the matrix does not claim hook, memory, or orchestration parity.

## 10. Secret And Private Context Review

Required checks:

```bash
rg -n -i "(token|secret|password|apikey|api_key)[[:space:]]*[:=]|sk-[A-Za-z0-9_-]{20,}|BEGIN .*PRIVATE|PRIVATE KEY|ssh-rsa|ssh-ed25519" . --glob '!docs/release-checklist.md' --glob '!ECC/**'
rg -n "/Users/" README.md README.zh-CN.md CHANGELOG.md CONTRIBUTING.md docs standard templates adapters examples tests PROJECT.md DECISIONS.md HANDOFF.md AGENTS.md .github --glob '!docs/release-checklist.md'
rg -n -i "confidential|customer|client" README.md README.zh-CN.md CHANGELOG.md CONTRIBUTING.md docs standard templates adapters examples tests PROJECT.md DECISIONS.md HANDOFF.md AGENTS.md .github --glob '!docs/release-checklist.md'
```

Pass criteria:

- no tokens, private keys, credentials, or internal secrets are present,
- personal paths appear only when intentionally documenting local development state and are removed before public release if inappropriate,
- no customer, client, or confidential project context is included.

The scan list must cover every tracked document directory. This file is
excluded because it contains the search terms themselves; do not add other
exclusions to silence a match, and do not name a check with the words it
searches for.

## 11. Public Remote Decision

Do not create or push a public remote until sections 1-10 pass.

If publishing publicly, confirm:

```bash
git remote -v
gh repo create ai-workspace-standard --public --source . --remote origin --push
```

Risk:

- `--public` exposes the repository to the internet,
- pushed git history may retain removed sensitive content,
- public release should happen only after a history-level review if sensitive content was ever committed.

## Release Result

Record each release result in `docs/releases/<version>-readiness.md` before
tagging or publishing. Copy the skeletons in `docs/releases/TEMPLATE.md` rather
than editing a previous release's record. Include:

- Status: Not started | Passed | Blocked
- Version:
- Commit:
- Validation summary:
- Known risks:
- Follow-up:
