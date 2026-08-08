"""Guard this repository's bilingual policy.

This is NOT part of the AEWS standard. It enforces one repository-local rule:
the English contract surface must stay complete on its own, so a reader who
cannot read Chinese can still adopt AEWS end to end.

Owner-facing working documents may be written in Chinese. Any file named like
`README.zh-CN.md` is an intentional translation. Every other tracked Markdown
file must be free of CJK text, except on a line that links to a translation.

The rule is deliberately default-deny: a new document is treated as contract
surface unless it is explicitly declared below.
"""

from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# Documents the owner reads and writes daily. Chinese is allowed here.
WORKING_DOCUMENTS = {
    "PROJECT.md",
    "DECISIONS.md",
    "HANDOFF.md",
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
            "contract-surface files must stay English; declare a working "
            "document or add a `<name>.<lang>.md` translation instead",
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
