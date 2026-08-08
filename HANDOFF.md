# HANDOFF

## Current Goal

Publish v1.1.0 and record the resulting external state.

## Current State

- Repository path: repo root
- Last completed step: defined shared progress, checkpoint, evidence, staleness,
  concurrency, and optional runtime boundaries; upgraded the compatibility
  matrix and minimal example to cover Codex and Claude Code projections; set
  runtime fixture, passed the Codex CLI read-only probe, and completed a third
  read-only adoption evaluation that removed generated-artifact warning noise;
  published the tested adoption mapping and completed the local v0.2.0
  release-readiness record; passed the owner-approved Claude Code read-only
  probe with unchanged Git state and fixture hashes; completed the v1.0
  requirement audit, compatibility policy, and local readiness record; added
  tested README Quick Start paths, neutralized the Decisions template, dated
  the changelog, and prepared GitHub Release notes and manual commands.
- Later completed step: added a Secondary support tier and placed GitHub
  Copilot in it, after the owner defined Codex and Claude Code as the main
  drivers and Copilot as an assisting tool; added the thin projection, a root
  entrypoint for this repository, validator discovery for both locations,
  matrix and decision records, and regression coverage. Copilot has structural
  evidence only; no runtime probe was run.
- Latest completed step: measured the cost of writing the working documents in
  Chinese and reverted it. `_validate_duplicates` compares normalized lines
  and skips anything under 60 characters, and Chinese wraps well below that,
  so a constructed duplicate went undetected in every Chinese variant while
  the English one was caught. Documentation stays English; other languages
  are `<name>.<lang>.md` translations. Added
  `tests/test_language_boundary.py` to enforce it, widened the section 10
  privacy scans, which never covered `README.zh-CN.md`, `CONTRIBUTING.md`,
  `tests`, or `.github`, and restated the v1.1.0 classification rationale in
  English so that record stands on its own.
- Next step: `v1.0.0` is tagged at `efb1724` and its GitHub Release is
  published. Push `main`, then tag and publish `v1.1.0` at `6b37bf2`, the
  commit the v1.1.0 readiness record audited. Later commits are not in that
  audit and belong to a following release. Commands are in
  `docs/releases/v1.1.0-readiness.md`. Record post-release state afterwards.
- Blockers: none in repository content. The owner's local `gh` authentication
  must be valid before the manual GitHub Release command.

## Evidence

```bash
find . -maxdepth 6 -path ./.git -prune -o -path ./ECC -prune -o -type f -print
wc -l README.md AGENTS.md PROJECT.md DECISIONS.md HANDOFF.md docs/*.md standard/*.md
git status --short --branch
wc -l AGENTS.md adapters/codex/AGENTS.md adapters/claude-code/CLAUDE.md adapters/cursor/.cursor/rules/aews.mdc adapters/gemini/GEMINI.md
wc -l .github/copilot-instructions.md adapters/copilot/.github/copilot-instructions.md
wc -l examples/migrations/oversized-agents/after/AGENTS.md examples/minimal-repo/VALIDATION.md CONTRIBUTING.md
wc -l docs/adoption-guide.md
wc -l docs/versioning.md
wc -l templates/README.md
wc -l docs/validator-design.md
wc -l docs/validator.md
wc -l docs/cross-agent-continuity.md
sed -n '1,280p' docs/runtime-loading-evidence.md
sed -n '1,340p' docs/adapter-matrix.md
wc -l docs/release-checklist.md
sed -n '1,260p' examples/reference-evaluations/ecc-v2.0.0.md
sed -n '1,260p' examples/reference-evaluations/full-stack-application.md
sed -n '1,280p' examples/reference-evaluations/ai-experiment-service.md
sed -n '1,260p' CHANGELOG.md
sed -n '1,320p' docs/releases/v0.2.0-readiness.md
sed -n '1,320p' docs/releases/v1.0.0-readiness.md
python3 scripts/aews_validate.py . --mode template
python3 scripts/aews_validate.py tests/fixtures/runtime-loading --mode template
python3 -m unittest discover -s tests -p 'test_*.py' -v
git remote -v
git tag --list
git log --oneline --decorate -5
```

## Open Questions

- Whether to create a GitHub Release page for `v0.1.0`.
- Whether missing Decisions should become a failure only after a repository
  explicitly declares full AEWS compliance.

## Expiration

Replace this handoff after any owner-controlled release action changes the
current evidence.
