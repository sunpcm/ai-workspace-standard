# Runtime Loading Evidence

This record distinguishes static adapter validation from controlled runtime
discovery for the primary Codex and Claude Code targets.

## Probe Contract

- Date: 2026-07-26
- Fixture: `tests/fixtures/runtime-loading/`
- Isolated temporary Git commit: `5559b72d670b79829ff05998d5e3a2b03da9453b`
- Target documents: `PROJECT.md`, `DECISIONS.md`, `HANDOFF.md`, `TODO.md`
- Prohibited reads: `AGENTS.md`, `CLAUDE.md`
- Prohibited actions: every file modification
- Expected proof: tool-specific startup marker plus the shared current goal,
  completed step, and next step

The temporary repository was clean before and after the Codex probe. The
following SHA-256 values were unchanged:

| File | SHA-256 |
| --- | --- |
| `AGENTS.md` | `e291628e787438f20a0656da262f69011ec3c534c908877b514c4e47fa2e3628` |
| `CLAUDE.md` | `09e309de183a9cf118a300c6a1459a1d983380558977a9ec04df722aaeb34358` |
| `PROJECT.md` | `5a7f928a083a0de937317290e9d03f4ffadcc82ea9faa35370c342c2ebf70413` |
| `DECISIONS.md` | `7b7ab57c7052789682b2c871958eae74431e451aee162313094c39a46bcdd85d` |
| `HANDOFF.md` | `adaab0281d028c5ad0dacbed303d79ed72d0698949dadee15fc2cd374516c4e3` |
| `TODO.md` | `e1660e611bb3ddb8f0d1f1bd910efeceb989ee5665dde47662513d924c1f0547` |

Raw model transcripts are not checked in. The fixture contains only public,
synthetic test data. The six inputs are now locked by the checked-in
`SHA256SUMS` manifest and a regression test for future probes.

## Codex Result

Status: Pass.

- CLI version: `codex-cli 0.145.0`
- Model reported by CLI: `gpt-5.6-sol`
- Environment: isolated temporary Git repository
- Sandbox: read-only
- Session persistence: ephemeral
- User configuration: ignored
- Adapter read during probe: none
- Canonical files read: `PROJECT.md`, `DECISIONS.md`, `HANDOFF.md`, `TODO.md`
- Startup marker returned: `AEWS_CODEX_STARTUP_20260726`
- Shared next step returned: `record both read-only runtime-loading results`
- Modified files: none, confirmed by Git status and hashes

Command shape:

```bash
codex exec \
  --cd <isolated-fixture> \
  --sandbox read-only \
  --ephemeral \
  --ignore-user-config \
  --output-last-message <temporary-result-file> \
  '<read-only probe prompt>'
```

This proves that the tested Codex version loaded its root `AGENTS.md` marker
and could follow that adapter into the shared AEWS checkpoint. It does not
prove compatibility for every Codex version or configuration.

## Claude Code Result

Status: Not run; explicit external-transfer approval required.

- CLI version available locally: `2.1.218`
- Static discovery evidence: local help documents `CLAUDE.md` auto-discovery
  outside bare and safe modes
- Intended file capability: `Read` only
- Intended model-call budget: at most USD 1
- Process result: rejected by the host approval reviewer before Claude Code
  started because sending the concrete fixture to the external Claude service
  requires explicit approval for that destination
- External data sent by this probe: none
- Modified files: none

Do not reinterpret this result as a Claude Code failure. It is missing runtime
evidence. A future operator may rerun exactly one probe after approving the
transfer of the public synthetic fixture to Claude.

### Prepared Claude Command

Status: locally reviewed on 2026-07-27; model call not executed.

Claude Code `2.1.218 --help` confirms every option below. The command preserves
root `CLAUDE.md` auto-discovery while limiting built-in tools to `Read`, loading
only project settings, disabling slash commands and browser integration,
excluding configured MCP servers, disabling session persistence, and capping
the model-call budget. Passing the complete option set and JSON schema together
with `--help` returned exit code `0`, so the current CLI parser accepts the
prepared shape without invoking a model.

Run it only from a clean, isolated copy of the fixture after explicit approval:

```bash
claude --print \
  --tools Read \
  --permission-mode plan \
  --setting-sources project \
  --strict-mcp-config \
  --mcp-config '{"mcpServers":{}}' \
  --disable-slash-commands \
  --no-chrome \
  --no-session-persistence \
  --prompt-suggestions false \
  --effort low \
  --max-budget-usd 1 \
  --output-format json \
  --json-schema '{"type":"object","properties":{"startup_marker":{"type":"string"},"project_file":{"type":"string"},"decisions_file":{"type":"string"},"handoff_file":{"type":"string"},"task_file":{"type":"string"},"current_goal":{"type":"string"},"last_completed_step":{"type":"string"},"next_step":{"type":"string"}},"required":["startup_marker","project_file","decisions_file","handoff_file","task_file","current_goal","last_completed_step","next_step"],"additionalProperties":false}' \
  'Without explicitly opening AGENTS.md or CLAUDE.md, read PROJECT.md, DECISIONS.md, HANDOFF.md, and TODO.md. Report the startup marker supplied by repository instructions, the four canonical filenames, and the shared current goal, last completed step, and next step. Do not modify any file.'
```

The marker value is deliberately absent from the prompt and schema. A pass
requires the returned marker to equal `AEWS_CLAUDE_STARTUP_20260726`, all four
filenames to match the fixture, and the returned checkpoint to match
`HANDOFF.md` and `TODO.md`.

Before and after the command, run:

```bash
git status --porcelain=v1 -uall
shasum -a 256 -c SHA256SUMS
```

A pass also requires an unchanged clean status and all six hashes above. Keep
only the structured result needed for the evidence summary; do not commit the
raw response.

## Reproduction

Validate the fixture without invoking a model:

```bash
python3 scripts/aews_validate.py tests/fixtures/runtime-loading --mode template
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

For a runtime probe, copy the fixture into a temporary directory, initialize a
temporary Git repository, record its commit and file hashes, run one read-only
tool call, and verify the same commit and hashes afterward. Use the prepared
Claude command above for this evidence record; do not run it without explicit
approval for the external transfer.
