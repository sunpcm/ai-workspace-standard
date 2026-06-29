# AEWS Documents

AEWS defines document roles, not mandatory filenames for every project. Filenames can vary, but each role should have one canonical home.

## Core Roles

| Role | Purpose | Typical File |
| --- | --- | --- |
| Project | Durable repo facts, commands, and boundaries | `PROJECT.md` |
| Handoff | Active continuation state | `HANDOFF.md` |
| Decisions | Accepted decisions and rationale | `DECISIONS.md` |
| Experiment | Temporary hypothesis and evidence | `EXPERIMENT.md` |
| Adapter | Tool-specific read order and behavior | `AGENTS.md`, `CLAUDE.md`, `.cursor/rules`, `GEMINI.md` |

## Required in v0.1

A minimal AEWS repo should include:

- one project document,
- one handoff document when active work is in progress,
- one decision log,
- thin adapters only for tools actually used.

## Optional

Add these only when needed:

- `archive/`
- `runbooks/`
- `operations/`
- `research/`
- `templates/`
- generated adapter outputs.

## Rule

If two files contain the same durable fact, one of them is wrong. Replace duplication with a link or read-order reference.
