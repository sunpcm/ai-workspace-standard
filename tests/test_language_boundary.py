"""Guard this repository's bilingual policy.

This is NOT part of the AEWS standard. It enforces one repository-local rule:
documentation is written in English, and other languages arrive as
`<name>.<lang>.md` translations beside the English original.

The rule exists because `_validate_duplicates` compares normalized lines and
skips anything under 60 characters. Chinese wraps well below that, so an
in-place translation silently disables the check that keeps adapters from
becoming knowledge stores. See the 2026-08-09 entry in `DECISIONS.md`.

The rule is deliberately default-deny: a new document must be English unless it
is explicitly declared below.
"""

from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# Task queue rather than a canonical knowledge role, so it is not compared
# against adapters and may stay in the owner's language.
WORKING_DOCUMENTS = {
    "TODO.md",
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
            "documentation must stay English; add a `<name>.<lang>.md` "
            "translation instead of translating a document in place",
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
