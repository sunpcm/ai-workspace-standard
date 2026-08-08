# Release Document Template

Copy the two skeletons below when preparing a release. Each release produces
two documents with different jobs:

| File | Audience | Job |
| --- | --- | --- |
| `docs/releases/vX.Y.Z.md` | Adopters | What changed and what it guarantees; used as the GitHub Release body |
| `docs/releases/vX.Y.Z-readiness.md` | Maintainer | Proof the release commit is ready, and what was not verified |

Keep them separate. Notes make claims; the readiness record backs them.

This template is this repository's own release scaffold. It is not part of the
AEWS standard surface, so changing it does not require a version bump and does
not ask anything of adopting repositories.

## Rules

- Record measured results, not copied ones. Re-run every check for the actual
  release commit, even when the previous release passed the same checks.
- Name the release class and the rule from `docs/versioning.md` that justifies
  it. "Minor because it is additive" is a claim; cite the clause.
- Never present structural validation as runtime evidence. If a target has no
  controlled probe, say so in both documents.
- Fill in Known Limitations. An empty limitations section is almost always a
  missing audit, not a clean one.
- Do not edit a published release document. Record the correction in the next
  release and in `DECISIONS.md`.
- Publication stays owner-controlled. A preparation commit must not push, tag,
  or publish.

---

## Skeleton 1: Release Notes

```markdown
# AEWS vX.Y.Z

One paragraph: what this release adds, and its compatibility class.

## Highlights

- Three to six bullets. Each states a user-visible change, not an internal edit.

## Evidence Boundary

What is proven, what is claimed, and what is neither. Name any target that is
maintained without runtime evidence.

## Upgrade From vA.B.C

What an existing adopter must do. Write "No action is required" when true, and
give the optional copy commands when a new file is available.

The full release audit is recorded in `docs/releases/vX.Y.Z-readiness.md`.
```

## Skeleton 2: Readiness Record

```markdown
# vX.Y.Z Release Readiness

## Result

- Status: Release content finalized; external publication delegated to owner
- Audit date:
- Audited baseline:
- Release commit: the commit containing this record; resolve it with
  `git log -1 --format=%H -- docs/releases/vX.Y.Z-readiness.md`
- Published predecessor:
- Release class: major | minor | patch, with the justifying rule

## What Changed

| Change | Kind | Surface impact |
| --- | --- | --- |
|  | Added / Changed / Removed | What an existing repository must do, or nothing |

State whether the stable surface in the last major readiness record is
unchanged, and where the classification rationale is recorded.

## Verification Results

| Area | Result |
| --- | --- |
| Git scope and commit history |  |
| `git diff --check` |  |
| Root validation |  |
| Runtime-fixture validation |  |
| Regression suite |  |
| Runtime fixture hash manifest |  |
| Adapter line counts |  |
| Credential scan |  |
| Personal-path scan |  |
| Customer/confidential scan |  |
| Runtime/harness boundary |  |
| Push, tag, and public release | Pending owner action |

## Compatibility Evidence

| Target | Tier | Evidence | Boundary |
| --- | --- | --- | --- |

Only Primary carries a runtime-loading claim. Do not summarize this table in a
way that extends that claim to other tiers.

## Known Limitations

- Targets without controlled runtime evidence.
- Probes recorded against tool versions older than the currently installed ones.
- Behavior that is intentionally out of scope.
- Checks that remain manual.

## Verification Commands

Paste the exact commands that were run, and run the privacy scans in section 10
of `docs/release-checklist.md`.

## Publication Sequence

Ordered commands for push, tag, and GitHub Release, followed by the
verification commands. State explicitly that the preparation commit performs
none of these.
```

## Where This Fits

`docs/release-checklist.md` is the reusable gate that decides whether a release
may proceed. This template shapes the record that the gate produces. Run the
checklist first, then write these two documents from its actual results.
