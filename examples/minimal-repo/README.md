# Minimal AEWS Repo Example

This example shows the smallest useful AEWS-compatible repository.

It intentionally has:

- one project document,
- one decision log,
- one small task queue,
- one active handoff,
- thin Codex and Claude Code adapters that route to the same state.

It intentionally does not include hooks, generators, MCP configuration, or large tool-specific instruction files.

The example demonstrates checkpoint-based continuity. It does not claim that
the two agents can observe each other in real time.
