# AGENTS.md

This repository is the documentation site for Atlas Notes, a small knowledge base product. The app has a static marketing page, a local sync worker, and a command line importer. The public site is deployed from `site/`, the worker lives in `worker/`, and examples live in `examples/`.

The repository uses Markdown as the source format. The importer reads Markdown files, extracts front matter, builds a local search index, and writes generated data into `site/data/`. Generated data must not be edited by hand.

## Commands

Use these commands before sending changes:

```bash
make test
make docs
make verify-links
```

If generated data is stale, run:

```bash
make import
```

## Architecture Notes

The importer is intentionally separate from the site because the site must stay hostable on any static file server. The worker should not require a hosted database. Search index generation happens locally so the runtime has no server dependency.

The sync worker currently reads from a local folder only. Remote sync was discussed but is deferred because it would require credentials, conflict handling, and provider-specific behavior.

## Decisions

Decision from 2026-05-10: keep the site static. The team chose this because static hosting keeps operations simple and avoids a database dependency. The consequence is that import and indexing must happen before deployment.

Decision from 2026-05-18: keep generated files out of reviews unless the source Markdown changed. The goal is to reduce noisy diffs.

## Current Tasks

The current task is to split the importer into parse, validate, and index stages. The parse stage is done. The validate stage still needs better front matter errors. The next step is to add a fixture with a missing title and verify that the command prints the file path.

Blocker: link verification is slow on large example folders.

## Agent Rules

Read this file first. Keep answers short. Do not add a database. Do not change generated data unless the source changed. Update this file whenever any project decision changes.
