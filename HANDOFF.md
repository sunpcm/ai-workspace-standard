# HANDOFF

## Current Goal

Complete the v1.0 release-readiness audit after both primary runtime-loading
probes passed.

## Current State

- Repository path: repo root
- Last completed step: defined shared progress, checkpoint, evidence, staleness,
  concurrency, and optional runtime boundaries; upgraded the compatibility
  matrix and minimal example to cover Codex and Claude Code projections; set
  runtime fixture, passed the Codex CLI read-only probe, and completed a third
  read-only adoption evaluation that removed generated-artifact warning noise;
  published the tested adoption mapping and completed the local v0.2.0
  release-readiness record; passed the owner-approved Claude Code read-only
  probe with unchanged Git state and fixture hashes.
- Next step: run the full v1.0 requirement and release-readiness audit, update
  version documents, and stop before push, tag, or release publication.
- Blockers: none for local release readiness. Push, tag, and publication remain
  owner-controlled external actions.

## Evidence

```bash
find . -maxdepth 6 -path ./.git -prune -o -path ./ECC -prune -o -type f -print
wc -l README.md AGENTS.md PROJECT.md DECISIONS.md HANDOFF.md docs/*.md standard/*.md
git status --short --branch
wc -l AGENTS.md adapters/codex/AGENTS.md adapters/claude-code/CLAUDE.md adapters/cursor/.cursor/rules/aews.mdc adapters/gemini/GEMINI.md
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
python3 scripts/aews_validate.py . --mode template
python3 scripts/aews_validate.py tests/fixtures/runtime-loading --mode template
python3 -m unittest discover -s tests -p 'test_*.py' -v
git remote -v
git tag --list
git log --oneline --decorate -5
```

## Open Questions

- Whether to create a GitHub Release page for `v0.1.0`.
- Whether the owner wants to publish the resulting local release candidate.
- Whether missing Decisions should become a failure only after a repository
  explicitly declares full AEWS compliance.

## Expiration

Replace this handoff after the Claude probe or any owner-controlled release
action changes the current evidence.
