# PROJECT

## Purpose

Atlas Notes is a documentation site and local importer for Markdown-based knowledge bases.

## Scope

- Scope: Repo
- Runtime model: static site plus local generation
- Generated output: `site/data/`

## Architecture

The repository separates the static site from local import work:

- `site/` contains the static site.
- `worker/` contains local import and search index generation.
- `examples/` contains sample Markdown content.

The importer reads Markdown files, extracts front matter, validates metadata, builds a local search index, and writes generated data into `site/data/`.

Generated data is derived output and should not be edited by hand.

## Commands

```bash
make test
make docs
make verify-links
make import
```

Run `make import` when generated data is stale.

## Verification

Before completing changes, run the relevant test, documentation, and link verification commands.

## Known Risks

Link verification can be slow on large example folders.
