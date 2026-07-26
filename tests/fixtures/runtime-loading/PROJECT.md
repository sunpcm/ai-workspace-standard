# PROJECT

## Purpose

Provide a public, non-sensitive fixture for AEWS adapter runtime-loading tests.

## Scope

- Scope: Repo
- Runtime targets: Codex and Claude Code

## Commands

```bash
python3 scripts/aews_validate.py tests/fixtures/runtime-loading --mode template
```

## Verification

Each agent must report its adapter-specific startup marker and the shared next
step without reading the adapter file explicitly or modifying the fixture.
