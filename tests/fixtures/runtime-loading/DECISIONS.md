# DECISIONS

## Decisions

### 2026-07-26: Keep runtime probes read-only

Status: Accepted

Scope: Repo

Context: Compatibility evidence must not depend on an agent editing its test
fixture.

Decision: Runtime-loading probes may read canonical documents but must not
modify files or explicitly open the adapter file under test.

Consequences: A reported startup marker is evidence of adapter discovery, and
the shared Handoff result is evidence of canonical-state routing.

Evidence: `AGENTS.md`, `CLAUDE.md`, `HANDOFF.md`
