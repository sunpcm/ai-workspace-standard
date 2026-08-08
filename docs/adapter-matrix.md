# Adapter Compatibility Matrix

This matrix maps AEWS canonical documents to common agent-specific files and
records the evidence behind each compatibility claim. Compatibility here means
document discovery and projection. It does not imply hook, memory, orchestration,
or real-time runtime parity.

## Support Policy

- **Primary:** Codex and Claude Code. Actively used as the main drivers, with
  maintained thin adapters, validator discovery, continuity examples, and
  controlled runtime-loading evidence.
- **Secondary:** GitHub Copilot. Actively used in an assisting role, with the
  same adapter and discovery maintenance, but no runtime-evidence commitment.
- **Extension reference:** Cursor, Gemini CLI, and future tools may use the open
  adapter contract, but AEWS does not currently commit to implementation work
  or runtime validation for them.

Each tier states what it guarantees. Only Primary carries a runtime-loading
claim, so a Secondary target is never implied to be runtime verified.

Tiers reflect current project usage, not a permanent vendor restriction. A tool
moves up when there is real usage, maintainer capacity, and, for Primary,
reproducible runtime evidence.

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
| Codex | Primary | Root `AGENTS.md` | `adapters/codex/AGENTS.md` | Reads shared handoff and task state; verifies it with Git | Controlled read-only pass on `codex-cli 0.145.0`; see `docs/runtime-loading-evidence.md` | One local version and fixture do not prove universal compatibility |
| Claude Code | Primary | Root `CLAUDE.md` | `adapters/claude-code/CLAUDE.md` | Uses the same checkpoint protocol as Codex | Controlled read-only pass on Claude Code `2.1.218`; see `docs/runtime-loading-evidence.md` | One local version, fixture, and approved external call do not prove universal compatibility |
| GitHub Copilot | Secondary | `.github/copilot-instructions.md` in the IDE; root `AGENTS.md` for Copilot coding agent | `adapters/copilot/.github/copilot-instructions.md` | Uses the same checkpoint protocol as Codex and Claude Code | Static projection and AEWS validator pass on 2026-08-08 | No controlled runtime-loading probe yet; the IDE surface has no headless read-only command comparable to `codex` or `claude` |
| Cursor | Extension reference | `.cursor/rules/*.mdc` | `adapters/cursor/.cursor/rules/aews.mdc` | Demonstrates how an editor adapter could route to shared state | Static projection and AEWS validator pass on 2026-07-26 | No current implementation or runtime-validation commitment |
| Gemini CLI | Extension reference | Root `GEMINI.md` | `adapters/gemini/GEMINI.md` | Demonstrates how a CLI adapter could route to shared state | Static projection and AEWS validator pass on 2026-07-26 | No current implementation or runtime-validation commitment |

Evidence status must remain explicit. A checked-in adapter plus validator pass
proves structural compatibility; only a controlled tool run can prove runtime
discovery for a specific tool version.

The latest primary-target runtime result is recorded in
`docs/runtime-loading-evidence.md`.

## Verification Commands

Run the no-model, local checks first:

```bash
python3 scripts/aews_validate.py . --mode template
python3 -m unittest discover -s tests -p 'test_*.py' -v
codex --version
claude --version
claude --help | rg "CLAUDE.md auto-discovery"
test -f .github/copilot-instructions.md && echo "copilot instructions present"
command -v cursor || true
command -v gemini || true
```

The Cursor and Gemini commands only document local availability. Their absence
does not block the primary or secondary compatibility track.

The GitHub Copilot check is a file-presence check only. Copilot's IDE surface
has no headless, read-only invocation comparable to `codex` or `claude`, so a
controlled runtime-loading probe would require a manual editor session. Do not
report structural presence as runtime evidence.

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

## Minimal GitHub Copilot Projection

```text
Read:
1. PROJECT.md
2. DECISIONS.md
3. HANDOFF.md if present
4. TODO.md or the declared task tracker if present

Keep .github/copilot-instructions.md and any root AGENTS.md thin and
pointed at the same canonical documents.
```

Only the repository-wide instructions file is part of the AEWS projection.
Path-scoped `.github/instructions/*.instructions.md` rules stay with the
adopting repository, because activation globs are editor behavior rather than
canonical knowledge routing.

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
