# Adapter Compatibility Matrix

This matrix maps AEWS canonical documents to common agent-specific files and
records the evidence behind each compatibility claim. Compatibility here means
document discovery and projection. It does not imply hook, memory, orchestration,
or real-time runtime parity.

## Support Policy

- **Primary:** Codex and Claude Code receive current compatibility evidence,
  continuity examples, and planned runtime-loading checks.
- **Extension reference:** Cursor, Gemini CLI, and future tools may use the open
  adapter contract, but AEWS does not currently commit to implementation work
  or runtime validation for them.

The priority is based on current project usage, not a permanent vendor
restriction. A non-primary tool can be promoted when there is real usage,
maintainer capacity, and reproducible evidence.

## Canonical Sources

| AEWS Role | Canonical File | Purpose |
| --- | --- | --- |
| Project | `PROJECT.md` | Durable repo facts, commands, boundaries |
| Decisions | `DECISIONS.md` | Accepted decisions and rationale |
| Handoff | `HANDOFF.md` | Active continuation state |
| Experiment | `EXPERIMENT.md` | Temporary hypothesis and evidence |
| Scope rules | `standard/scopes.md` | Placement model |
| Adapter rules | `standard/adapters.md` | Projection rules |
| Continuity protocol | `docs/cross-agent-continuity.md` | Shared progress, handoff, and evidence rules |

## Tool Projection

| Tool | Priority | Discovery Surface | AEWS Projection | Continuity Behavior | Current Evidence | Known Limitation |
| --- | --- | --- | --- | --- | --- | --- |
| Codex | Primary | Root `AGENTS.md` | `adapters/codex/AGENTS.md` | Reads shared handoff and task state; verifies it with Git | Static projection and AEWS validator pass; local `codex-cli 0.145.0` present on 2026-07-26 | Controlled runtime-loading fixture not yet run |
| Claude Code | Primary | Root `CLAUDE.md` | `adapters/claude-code/CLAUDE.md` | Uses the same checkpoint protocol as Codex | Static projection and AEWS validator pass; local Claude Code `2.1.218` help confirms `CLAUDE.md` auto-discovery outside bare/safe modes | Projection is stored as an installable example, not a root file in this standard repo; runtime fixture not yet run |
| Cursor | Extension reference | `.cursor/rules/*.mdc` | `adapters/cursor/.cursor/rules/aews.mdc` | Demonstrates how an editor adapter could route to shared state | Static projection and AEWS validator pass on 2026-07-26 | No current implementation or runtime-validation commitment |
| Gemini CLI | Extension reference | Root `GEMINI.md` | `adapters/gemini/GEMINI.md` | Demonstrates how a CLI adapter could route to shared state | Static projection and AEWS validator pass on 2026-07-26 | No current implementation or runtime-validation commitment |

Evidence status must remain explicit. A checked-in adapter plus validator pass
proves structural compatibility; only a controlled tool run can prove runtime
discovery for a specific tool version.

## Verification Commands

Run the no-model, local checks first:

```bash
python3 scripts/aews_validate.py . --mode template
python3 -m unittest discover -s tests -p 'test_*.py' -v
codex --version
claude --version
claude --help | rg "CLAUDE.md auto-discovery"
command -v cursor || true
command -v gemini || true
```

The Cursor and Gemini commands only document local availability. Their absence
does not block the Codex and Claude Code compatibility track.

A controlled runtime-loading test, when explicitly authorized, should use a
temporary fixture and a read-only prompt such as:

```text
Read the repository instructions. Report the canonical Project, Decisions,
Handoff, and task-queue files plus the current next step. Do not modify files.
```

Record the tool version, fixture commit, command shape, observed files, result,
and test date. Do not record credentials, raw private transcripts, or an
unsupported claim of general compatibility.

## Projection Rule

If the same sentence appears in both a canonical document and an adapter, the adapter should usually be replaced with a pointer.

## Minimal Codex Projection

```text
Read:
1. PROJECT.md
2. DECISIONS.md
3. HANDOFF.md if present
4. TODO.md or the declared task tracker if present

Do not copy durable project knowledge into AGENTS.md.
```

## Minimal Claude Code Projection

```text
Read:
1. PROJECT.md
2. DECISIONS.md
3. HANDOFF.md if present
4. TODO.md or the declared task tracker if present

Put durable decisions in DECISIONS.md, not CLAUDE.md.
```

## Minimal Cursor Projection

```text
Use Cursor rules for activation and editor behavior.
Use AEWS canonical documents for repo knowledge.
```

## Minimal Gemini Projection

```text
Read canonical AEWS documents before task files.
Keep GEMINI.md short and tool-specific.
```

## Cross-Agent Boundary

Adapters should route every participating agent to the same canonical state.
They should not copy a per-agent task history. Follow
`docs/cross-agent-continuity.md` for checkpoint, evidence, staleness, and
concurrency rules. Optional harness memory may transport a handoff, but it is
not governed project truth.
