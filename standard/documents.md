# AEWS Documents

AEWS defines document roles, not mandatory filenames for every project.
Filenames can vary, but each role should have one primary canonical home.
Mature repositories may route from that primary document to narrower
supplements with explicit ownership.

## Core Roles

| Role | Purpose | Typical File |
| --- | --- | --- |
| Project | Durable repo facts, commands, and boundaries | `PROJECT.md` |
| Handoff | Active continuation state | `HANDOFF.md` |
| Decisions | Accepted decisions and rationale | `DECISIONS.md` |
| Experiment | Temporary hypothesis and evidence | `EXPERIMENT.md` |
| Adapter | Tool-specific read order and behavior | `AGENTS.md`, `CLAUDE.md`, `.cursor/rules`, `GEMINI.md` |

A task queue such as `TODO.md` or an external issue tracker is a supporting
execution surface, not a new canonical knowledge role. Under the optional
cross-agent continuity profile, every participating adapter should route to
the same queue.

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
- generated adapter outputs,
- `aews.json` when adoption validation needs repeatable role mapping.
- optional actor, timestamp, worktree, and commit evidence in an active
  Handoff when multiple agents need continuation context.

## Adoption Mapping

`aews.json` is not a canonical knowledge document. It may contain only role,
path, lifecycle-state, and adapter routing metadata. Do not put project facts,
decisions, commands, or task state in it.

## Rule

If two files contain the same durable fact, one of them is wrong. Replace
duplication with a link or read-order reference. A supplement is valid only
when its primary document routes to it and its narrower ownership is clear.
