"""Guard this repository's bilingual policy.

This is NOT part of the AEWS standard. It enforces one repository-local rule.

A document must be English when either test applies:

1. The validator compares it. `_validate_duplicates` and
   `_validate_document_references` only read files returned by `_mapped_files`,
   which in template mode are `PROJECT.md`, `DECISIONS.md`, and `HANDOFF.md`.
   Those comparisons are literal: `_statements` skips lines under 60
   characters, and Chinese wraps at roughly 35 to 40, so an in-place
   translation silently disables the check that keeps adapters from becoming
   knowledge stores.
2. An adopter must read it to use AEWS. That covers the standard, templates,
   adapters, examples, release records, and the adoption, validator, and
   compatibility documents under `docs/`.

Documents failing both tests may use the maintainer's language and are listed
below. Other languages otherwise arrive as `<name>.<lang>.md` translations
beside the English original. See the 2026-08-09 entry in `DECISIONS.md`.

The rule is deliberately default-deny: a new document must be English unless it
is explicitly declared here.
"""

from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# Neither compared by the validator nor on the adopter path. Verified: no
# README or adoption document links the two `docs/` entries, and `_mapped_files`
# returns only the three root canonical documents.
WORKING_DOCUMENTS = {
    "TODO.md",
    "docs/roadmap.md",
    "docs/vision.md",
}

# `<name>.<lang>.md`, for example `README.zh-CN.md`.
TRANSLATION = re.compile(r"\.[a-z]{2}(?:-[A-Za-z]{2,4})?\.md$")

# CJK ideographs plus kana, so a future Japanese translation is also detected.
CJK = re.compile(r"[぀-ヿ一-鿿]")

# A pointer to a translation may carry a translated label.
TRANSLATION_LINK = re.compile(r"\]\([^)]*" + TRANSLATION.pattern[:-1] + r"\)")


def tracked_markdown() -> list[str]:
    output = subprocess.run(
        ["git", "ls-files", "*.md", "*.mdc"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    return [line for line in output.splitlines() if line]


class LanguageBoundaryTests(unittest.TestCase):
    def test_declared_working_documents_exist(self) -> None:
        missing = sorted(
            name for name in WORKING_DOCUMENTS if not (ROOT / name).is_file()
        )
        self.assertEqual([], missing, "declared working document no longer exists")

    def test_contract_surface_has_no_cjk(self) -> None:
        offenders: list[str] = []
        for name in tracked_markdown():
            if name in WORKING_DOCUMENTS or TRANSLATION.search(name):
                continue
            for number, line in enumerate(
                (ROOT / name).read_text(encoding="utf-8").splitlines(), start=1
            ):
                if CJK.search(line) and not TRANSLATION_LINK.search(line):
                    offenders.append(f"{name}:{number}")
        self.assertEqual(
            [],
            offenders,
            "a validator-compared or adopter-facing document must stay English; "
            "add a `<name>.<lang>.md` translation instead of translating it "
            "in place",
        )

    def test_translation_has_an_english_original(self) -> None:
        orphans: list[str] = []
        for name in tracked_markdown():
            if not TRANSLATION.search(name):
                continue
            original = TRANSLATION.sub(".md", name)
            if not (ROOT / original).is_file():
                orphans.append(name)
        self.assertEqual(
            [], orphans, "a translation must not outlive its English original"
        )


if __name__ == "__main__":
    unittest.main()
