# Adapter Matrix

This matrix maps AEWS canonical documents to common agent-specific files.

## Canonical Sources

| AEWS Role | Canonical File | Purpose |
| --- | --- | --- |
| Project | `PROJECT.md` | Durable repo facts, commands, boundaries |
| Decisions | `DECISIONS.md` | Accepted decisions and rationale |
| Handoff | `HANDOFF.md` | Active continuation state |
| Experiment | `EXPERIMENT.md` | Temporary hypothesis and evidence |
| Scope rules | `standard/scopes.md` | Placement model |
| Adapter rules | `standard/adapters.md` | Projection rules |

## Tool Projection

| Tool | File | Should Contain | Should Not Contain |
| --- | --- | --- | --- |
| Codex | `AGENTS.md` | read order, collaboration constraints, Codex-specific workflow notes | architecture, task history, full command reference |
| Claude Code | `CLAUDE.md` | read order, Claude-specific command conventions | copied decision records, long project background |
| Cursor | `.cursor/rules/*.mdc` | scoped editor activation rules, canonical file routing | durable repo facts, experiment logs |
| Gemini CLI | `GEMINI.md` | read order and CLI-specific expectations | large context blocks copied from canonical docs |

## Projection Rule

If the same sentence appears in both a canonical document and an adapter, the adapter should usually be replaced with a pointer.

## Minimal Codex Projection

```text
Read:
1. PROJECT.md
2. DECISIONS.md
3. HANDOFF.md if present

Do not copy durable project knowledge into AGENTS.md.
```

## Minimal Claude Code Projection

```text
Read:
1. PROJECT.md
2. DECISIONS.md
3. HANDOFF.md if present

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
