# Runtime Loading Fixture

This fixture supports controlled, read-only checks that Codex and Claude Code
load their own thin adapter and then read the same AEWS canonical state.

The marker values are test data. They are intentionally tool-specific and do
not belong in canonical project documents.

`SHA256SUMS` locks the six probe inputs. Verify it before and after a runtime
call; update it only when an intentional fixture change also updates the
evidence record.
