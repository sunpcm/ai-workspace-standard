# HANDOFF

## Current Goal

Implement the first read-only AEWS v0.2 validator from the stabilized manual
evidence.

## Current State

- Repository path: repo root
- Last completed step: evaluated one ordinary full-stack application repository
  without modifying it, recorded sanitized evidence, and selected a routing-only
  `aews.json` contract for adoption mapping.
- Next step: implement the first read-only validator with template/adoption
  fixtures and stable text output.
- Blockers: none.

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
wc -l docs/release-checklist.md
sed -n '1,260p' examples/reference-evaluations/ecc-v2.0.0.md
sed -n '1,260p' examples/reference-evaluations/full-stack-application.md
git remote -v
git tag --list
git log --oneline --decorate -5
```

## Open Questions

- Whether to create a GitHub Release page for `v0.1.0`.
- Which dependency-free repository-local Markdown link forms the first
  validator should recognize.
- Whether missing Decisions should become a failure only after a repository
  explicitly declares full AEWS compliance.

## Expiration

Replace this handoff after the first validator implementation and fixture suite
are complete.
