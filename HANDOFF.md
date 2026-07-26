# HANDOFF

## Current Goal

Add an evidence-backed adapter compatibility matrix after completing the first
read-only AEWS v0.2 validator.

## Current State

- Repository path: repo root
- Last completed step: implemented and documented the dependency-free validator,
  added template/adoption fixtures, passed eight regression tests, and replayed
  both real reference evaluations with zero failures.
- Next step: define evidence fields and current verification state for Codex,
  Claude Code, Cursor, and Gemini document adapters.
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
wc -l docs/validator.md
wc -l docs/release-checklist.md
sed -n '1,260p' examples/reference-evaluations/ecc-v2.0.0.md
sed -n '1,260p' examples/reference-evaluations/full-stack-application.md
python3 scripts/aews_validate.py . --mode template
python3 -m unittest discover -s tests -p 'test_*.py' -v
git remote -v
git tag --list
git log --oneline --decorate -5
```

## Open Questions

- Whether to create a GitHub Release page for `v0.1.0`.
- Which evidence fields make adapter compatibility claims useful without
  copying ECC runtime parity semantics.
- Whether missing Decisions should become a failure only after a repository
  explicitly declares full AEWS compliance.

## Expiration

Replace this handoff after the evidence-backed adapter compatibility matrix is
complete.
