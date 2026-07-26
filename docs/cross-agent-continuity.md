# Cross-Agent Continuity

AEWS can let Codex, Claude Code, and other agents share project progress
without sharing vendor transcripts or turning each adapter into a separate
project log.

This profile is optional. It defines a document and evidence protocol, not a
runtime, lock service, or real-time presence system.

## Capability Levels

| Level | Capability | AEWS Support |
| --- | --- | --- |
| Shared progress | Agents read the same project state and task queue | Core document protocol |
| Directed handoff | One agent records what another agent should continue | `HANDOFF.md`, optionally transported by a harness |
| Live coordination | Agents see concurrent edits, ownership, and presence | Outside AEWS core |

AEWS supports the first two levels. Live coordination requires a harness,
issue tracker, worktree manager, or another runtime with concurrency control.

## Sources Of Truth

Use each surface for one responsibility:

| Surface | Responsibility | Trust |
| --- | --- | --- |
| `PROJECT.md` | Durable repo facts, commands, and boundaries | Governed project knowledge |
| `DECISIONS.md` | Accepted choices and rationale | Governed project knowledge |
| `TODO.md` or task tracker | Priorities and execution queue | Current planning state |
| `HANDOFF.md` | Latest continuation checkpoint | Working state; verify freshness |
| Git commit, diff, and test output | Evidence of what changed | Authoritative implementation evidence |
| Harness memory or session log | Recall and transport | Unreviewed context |

An agent must not treat a handoff or recalled memory as proof that code is
correct. Important claims must be checked against Git, files, tests, CI, or the
relevant external work item.

## Start Protocol

At the beginning of work, an agent should:

1. read `PROJECT.md` and `DECISIONS.md`;
2. read `HANDOFF.md` and the relevant `TODO.md` item or external task;
3. inspect `git status --short --branch` and recent commits;
4. compare the handoff claims with repository evidence;
5. report stale or conflicting state before continuing.

The order is deliberate: canonical documents explain the project, the handoff
provides the latest checkpoint, and Git verifies what actually happened.

## Checkpoint Protocol

Update shared progress only at a meaningful checkpoint, such as a completed
task, a verified partial result, a blocker, or an intentional transfer to
another agent.

A useful checkpoint records:

- who or which harness produced it, when that helps coordination;
- branch or worktree;
- last completed step;
- next concrete step;
- blockers and unresolved risks;
- relevant commit, changed area, test command, or artifact;
- the condition that makes the handoff stale.

Update the task queue only when task status or priority changes. Do not turn
`HANDOFF.md` into a transcript or append-only activity log; replace stale
working state and let Git preserve implementation history.

## Conflict And Concurrency Rules

- A handoff is not a lock and does not claim exclusive file ownership.
- Concurrent agents should use separate branches or Git worktrees.
- Before committing, each agent must re-check the worktree and avoid staging
  changes it did not create or review.
- If `HANDOFF.md`, `TODO.md`, and Git disagree, Git and verified artifacts
  establish implementation state; the documents should then be refreshed.
- Do not have multiple agents continuously rewrite one shared status file.
  Checkpoint updates are safer than per-action updates.

## Optional Runtime Integration

A harness may automate recall or transport while preserving the AEWS trust
model. ECC Memory Vault is one example: it can target a handoff from one
harness to another through local Markdown, CLI, or MCP surfaces.

When integrating a runtime:

1. keep runtime memories unreviewed;
2. link them to commits, tasks, and governed documents;
3. promote accepted decisions or durable facts into canonical project docs;
4. do not auto-import raw transcripts into active project context;
5. keep the runtime optional so the repository remains understandable without
   installing it.

ECC's current reference implementation provides explicit save, search, read,
doctor, and handoff operations. It does not make AEWS a real-time coordination
system, and its automatic cross-harness session capture remains a separate
runtime concern.

## Acceptance Criteria

A repository may claim AEWS cross-agent continuity when:

- at least two declared adapters route to the same canonical project,
  decision, task, and handoff roles;
- both agents can identify the latest completed and next steps without copied
  task histories in their adapters;
- checkpoint claims include verifiable repository or task evidence;
- stale-state and concurrent-edit behavior are documented;
- any memory runtime is optional and is not presented as governed truth.
