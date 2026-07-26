# PROJECT

## Purpose

This example repository demonstrates the minimum AEWS document set for a single repo.

## Scope

- Scope: Repo
- Owner: Example owner
- Related workspace: AEWS examples

## Architecture

No application architecture exists in this example. The repository is documentation-only.

## Commands

```bash
# No build step
```

## Agent Read Order

1. `PROJECT.md`
2. `DECISIONS.md`
3. `HANDOFF.md`
4. `TODO.md` if present

## Verification

Check that both adapter files reference the same canonical documents instead of
copying their content.

## Known Risks

The main risk is adding tool-specific detail before the canonical model is clear.
