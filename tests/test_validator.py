from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures"
SCRIPT = ROOT / "scripts" / "aews_validate.py"
ADOPTION_TEMPLATE = ROOT / "templates" / "adoption" / "aews.example.json"

SPEC = importlib.util.spec_from_file_location("aews_validate", SCRIPT)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


def fixture(name: str) -> Path:
    return FIXTURES / name


def tree_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


class ValidatorTests(unittest.TestCase):
    def test_template_fixture_passes(self) -> None:
        result = VALIDATOR.validate_repository(fixture("template-valid"), mode="template")
        self.assertEqual([], result.failures)
        self.assertEqual([], result.warnings)

    def test_runtime_loading_fixture_passes(self) -> None:
        result = VALIDATOR.validate_repository(
            fixture("runtime-loading"), mode="template"
        )
        self.assertEqual([], result.failures)
        self.assertEqual([], result.warnings)

    def test_runtime_loading_fixture_hash_manifest_matches(self) -> None:
        root = fixture("runtime-loading")
        manifest = (root / "SHA256SUMS").read_text(encoding="utf-8").splitlines()
        self.assertEqual(6, len(manifest))
        for entry in manifest:
            expected, name = entry.split(maxsplit=1)
            actual = hashlib.sha256((root / name).read_bytes()).hexdigest()
            self.assertEqual(expected, actual, name)

    def test_readme_quick_start_passes_without_active_handoff(self) -> None:
        sources = {
            "PROJECT.md": ROOT / "templates" / "repo" / "PROJECT.md",
            "DECISIONS.md": ROOT / "templates" / "decision" / "DECISIONS.md",
            "AGENTS.md": ROOT / "adapters" / "codex" / "AGENTS.md",
            "CLAUDE.md": ROOT / "adapters" / "claude-code" / "CLAUDE.md",
            ".github/copilot-instructions.md": (
                ROOT / "adapters" / "copilot" / ".github" / "copilot-instructions.md"
            ),
        }
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "repo"
            target.mkdir()
            (target / "README.md").write_text("# Project\n", encoding="utf-8")
            for name, source in sources.items():
                destination = target / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, destination)

            result = VALIDATOR.validate_repository(target, mode="template")
            tools = {adapter.tool for adapter in result.adapters}

        self.assertEqual([], result.failures)
        self.assertEqual([], result.warnings)
        self.assertEqual({"codex", "claude", "copilot"}, tools)

    def test_copilot_adapter_is_discovered_in_both_locations(self) -> None:
        result = VALIDATOR.validate_repository(ROOT, mode="template")
        paths = {
            adapter.path for adapter in result.adapters if adapter.tool == "copilot"
        }
        self.assertEqual(
            {
                ".github/copilot-instructions.md",
                "adapters/copilot/.github/copilot-instructions.md",
            },
            paths,
        )

    def test_aews_repository_passes_its_validator(self) -> None:
        result = VALIDATOR.validate_repository(ROOT, mode="template")
        self.assertEqual([], result.failures)
        self.assertEqual([], result.warnings)

    def test_adoption_fixture_passes(self) -> None:
        result = VALIDATOR.validate_repository(fixture("adoption-valid"))
        self.assertEqual("adoption", result.mode)
        self.assertEqual([], result.failures)
        self.assertEqual([], result.warnings)

    def test_adoption_mapping_template_passes_contract(self) -> None:
        config = json.loads(ADOPTION_TEMPLATE.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "repo"
            target.mkdir()
            shutil.copyfile(ADOPTION_TEMPLATE, target / "aews.json")

            mapped_primaries: list[str] = []
            for name, role in config["roles"].items():
                primary = role.get("primary")
                if primary is None:
                    continue
                mapped_primaries.append(primary)
                supplements = role.get("supplements", [])
                primary_document = target / primary
                primary_document.parent.mkdir(parents=True, exist_ok=True)
                primary_content = [f"# {name.title()}"]
                primary_content.extend(
                    f"See [{path}]({path})." for path in supplements
                )
                primary_document.write_text(
                    "\n".join(primary_content) + "\n", encoding="utf-8"
                )
                for supplement in supplements:
                    document = target / supplement
                    document.parent.mkdir(parents=True, exist_ok=True)
                    document.write_text(
                        f"# {name.title()} Supplement\n", encoding="utf-8"
                    )

            routes = "\n".join(mapped_primaries) + "\n"
            for adapter in config["adapters"]:
                path = target / adapter["path"]
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(routes, encoding="utf-8")

            result = VALIDATOR.validate_repository(target)

        self.assertEqual([], result.failures)
        self.assertEqual([], result.warnings)

    def test_adoption_warnings_do_not_fail(self) -> None:
        result = VALIDATOR.validate_repository(fixture("adoption-warnings"))
        self.assertEqual([], result.failures)
        output = "\n".join(result.warnings)
        self.assertIn("Decisions role is missing", output)
        self.assertIn("does not route to supplement", output)
        self.assertIn("Broken local document reference", output)
        self.assertNotIn("summary.md", output)
        self.assertNotIn("batch_summary.md", output)
        self.assertIn("does not route to Project primary", output)
        self.assertNotIn("your-skill", output)
        self.assertNotIn("SKILL.md", output)

    def test_invalid_adoption_mapping_fails(self) -> None:
        result = VALIDATOR.validate_repository(fixture("adoption-invalid"))
        output = "\n".join(result.failures)
        self.assertIn("role project cannot be inactive", output)
        self.assertIn("role decisions cannot be inactive", output)
        self.assertIn("path must stay repository-relative", output)
        self.assertIn("unsupported top-level property: notes", output)
        self.assertIn("role project contains unsupported property: description", output)

    def test_adapter_line_limit_is_warning(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "repo"
            shutil.copytree(fixture("adoption-valid"), target)
            adapter = target / "AGENTS.md"
            content = adapter.read_text(encoding="utf-8") + ("\n<!-- padding -->" * 40)
            adapter.write_text(content, encoding="utf-8")
            result = VALIDATOR.validate_repository(target)
        self.assertEqual([], result.failures)
        self.assertTrue(any("soft limit" in warning for warning in result.warnings))

    def test_validation_is_read_only(self) -> None:
        root = fixture("adoption-valid")
        before = tree_hashes(root)
        VALIDATOR.validate_repository(root)
        self.assertEqual(before, tree_hashes(root))

    def test_cli_exit_codes(self) -> None:
        valid = subprocess.run(
            [sys.executable, str(SCRIPT), str(fixture("template-valid")), "--mode", "template"],
            check=False,
            capture_output=True,
            text=True,
        )
        invalid = subprocess.run(
            [sys.executable, str(SCRIPT), str(fixture("adoption-invalid"))],
            check=False,
            capture_output=True,
            text=True,
        )
        usage = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                str(fixture("template-valid")),
                "--mode",
                "adoption",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(0, valid.returncode)
        self.assertIn("Failures:\n- None", valid.stdout)
        self.assertEqual(1, invalid.returncode)
        self.assertIn("role project cannot be inactive", invalid.stdout)
        self.assertEqual(2, usage.returncode)
        self.assertIn("Usage error:", usage.stderr)


if __name__ == "__main__":
    unittest.main()
