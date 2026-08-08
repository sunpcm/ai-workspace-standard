#!/usr/bin/env python3
"""Dependency-free, read-only validator for AEWS repositories."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Iterable


ROLE_ORDER = ("project", "decisions", "handoff", "experiment")
INACTIVE_ROLES = {"handoff", "experiment"}
MARKDOWN_SUFFIXES = {".md", ".mdc"}
KNOWN_ROOT_ADAPTERS = ("AGENTS.md", "CLAUDE.md", "GEMINI.md")
COPILOT_INSTRUCTIONS = ".github/copilot-instructions.md"
ADAPTER_FILENAME_TOOLS = {
    "AGENTS.md": "codex",
    "CLAUDE.md": "claude",
    "GEMINI.md": "gemini",
    "copilot-instructions.md": "copilot",
}
KNOWN_INLINE_ROOT_DOCUMENTS = {
    "README.md",
    "PROJECT.md",
    "DECISIONS.md",
    "HANDOFF.md",
    "TODO.md",
    "EXPERIMENT.md",
    *KNOWN_ROOT_ADAPTERS,
}
BOILERPLATE_DUPLICATE_FRAGMENTS = (
    "do not copy durable knowledge",
    "do not duplicate canonical knowledge",
    "adapters are projections",
)


class UsageError(Exception):
    """Raised when the validator cannot interpret its invocation or config."""


@dataclass(frozen=True)
class Role:
    name: str
    primary: str | None = None
    supplements: tuple[str, ...] = ()
    status: str | None = None


@dataclass(frozen=True)
class Adapter:
    tool: str
    path: str


@dataclass
class ValidationResult:
    root: Path
    mode: str
    roles: dict[str, Role] = field(default_factory=dict)
    adapters: list[Adapter] = field(default_factory=list)
    failures: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def fail(self, message: str) -> None:
        if message not in self.failures:
            self.failures.append(message)

    def warn(self, message: str) -> None:
        if message not in self.warnings:
            self.warnings.append(message)


def _repo_relative_path(root: Path, value: str) -> tuple[Path | None, str | None]:
    if not isinstance(value, str) or not value.strip():
        return None, "path must be a non-empty string"
    if "\\" in value:
        return None, f"path must use forward slashes: {value}"

    pure = PurePosixPath(value)
    if pure.is_absolute() or ".." in pure.parts:
        return None, f"path must stay repository-relative: {value}"

    candidate = root.joinpath(*pure.parts)
    try:
        candidate.resolve(strict=False).relative_to(root.resolve())
    except ValueError:
        return None, f"path escapes repository root: {value}"
    return candidate, None


def _validate_existing_file(
    result: ValidationResult, value: str, *, label: str
) -> Path | None:
    candidate, error = _repo_relative_path(result.root, value)
    if error:
        result.fail(f"{label}: {error}")
        return None
    assert candidate is not None
    if candidate.is_symlink():
        result.fail(f"{label} must not be a symlink: {value}")
        return None
    if not candidate.is_file():
        result.fail(f"{label} does not exist: {value}")
        return None
    return candidate


def _template_roles(root: Path) -> dict[str, Role]:
    return {
        "project": Role("project", primary="PROJECT.md"),
        "decisions": Role("decisions", primary="DECISIONS.md"),
        "handoff": (
            Role("handoff", primary="HANDOFF.md")
            if (root / "HANDOFF.md").is_file()
            else Role("handoff", status="inactive")
        ),
        "experiment": (
            Role("experiment", primary="EXPERIMENT.md")
            if (root / "EXPERIMENT.md").is_file()
            else Role("experiment", status="inactive")
        ),
    }


def _discover_template_adapters(root: Path) -> list[Adapter]:
    adapters: list[Adapter] = []
    seen: set[str] = set()

    def add(tool: str, path: Path) -> None:
        relative = path.relative_to(root).as_posix()
        if relative not in seen and path.is_file() and not path.is_symlink():
            seen.add(relative)
            adapters.append(Adapter(tool=tool, path=relative))

    for name in KNOWN_ROOT_ADAPTERS:
        add(ADAPTER_FILENAME_TOOLS[name], root / name)

    add("copilot", root.joinpath(*COPILOT_INSTRUCTIONS.split("/")))

    cursor_rules = root / ".cursor" / "rules"
    if cursor_rules.is_dir():
        for path in sorted(cursor_rules.glob("*.mdc")):
            add("cursor", path)

    adapters_root = root / "adapters"
    if adapters_root.is_dir():
        for path in sorted(adapters_root.rglob("*")):
            if not path.is_file():
                continue
            tool = ADAPTER_FILENAME_TOOLS.get(path.name)
            if tool:
                add(tool, path)
            elif path.suffix == ".mdc":
                add("cursor", path)

    return adapters


def _load_adoption_config(config_path: Path) -> dict[str, object]:
    if not config_path.is_file():
        raise UsageError(f"adoption config does not exist: {config_path}")
    try:
        value = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise UsageError(f"cannot read adoption config {config_path}: {exc}") from exc
    if not isinstance(value, dict):
        raise UsageError("adoption config root must be a JSON object")
    return value


def _parse_adoption_mapping(
    result: ValidationResult, config: dict[str, object]
) -> None:
    for key in sorted(set(config) - {"version", "mode", "roles", "adapters"}):
        result.fail(f"aews.json contains unsupported top-level property: {key}")

    if type(config.get("version")) is not int or config.get("version") != 1:
        result.fail("aews.json version must be 1")
    if config.get("mode") != "adoption":
        result.fail('aews.json mode must be "adoption"')

    roles_value = config.get("roles")
    if not isinstance(roles_value, dict):
        result.fail("aews.json roles must be an object")
        roles_value = {}

    unknown_roles = sorted(set(roles_value) - set(ROLE_ORDER))
    for name in unknown_roles:
        result.fail(f"aews.json contains unknown role: {name}")

    claimed_paths: dict[str, str] = {}
    for name in ROLE_ORDER:
        raw = roles_value.get(name)
        if not isinstance(raw, dict):
            result.fail(f"aews.json role {name} must be an object")
            result.roles[name] = Role(name, status="missing")
            continue

        for key in sorted(set(raw) - {"primary", "supplements", "status"}):
            result.fail(f"role {name} contains unsupported property: {key}")

        primary = raw.get("primary")
        status = raw.get("status")
        supplements = raw.get("supplements", [])

        if primary is not None and status is not None:
            result.fail(f"role {name} cannot define both primary and status")

        if primary is not None:
            if not isinstance(primary, str) or not primary.strip():
                result.fail(f"role {name} primary must be a non-empty string")
                primary = None
            if not isinstance(supplements, list) or not all(
                isinstance(item, str) and item.strip() for item in supplements
            ):
                result.fail(f"role {name} supplements must be a list of paths")
                supplements = []
            if len(set(supplements)) != len(supplements):
                result.fail(f"role {name} contains duplicate supplements")

            role = Role(name, primary=primary, supplements=tuple(supplements))
            result.roles[name] = role
            for kind, path in (("primary", primary), *[("supplement", p) for p in supplements]):
                if not path:
                    continue
                owner = f"{name} {kind}"
                if path in claimed_paths:
                    result.fail(
                        f"mapped path {path} is claimed by both {claimed_paths[path]} and {owner}"
                    )
                else:
                    claimed_paths[path] = owner
                _validate_existing_file(result, path, label=owner)
            continue

        if status not in {"missing", "inactive"}:
            result.fail(f"role {name} must define primary or status")
            status = "missing"
        if status == "inactive" and name not in INACTIVE_ROLES:
            result.fail(f"role {name} cannot be inactive")
        if supplements not in ([], None):
            result.fail(f"unmapped role {name} cannot define supplements")
        result.roles[name] = Role(name, status=status)
        if status == "missing":
            result.warn(f"{name.title()} role is missing")

    adapters_value = config.get("adapters", [])
    if not isinstance(adapters_value, list):
        result.fail("aews.json adapters must be a list")
        adapters_value = []

    seen_adapters: set[str] = set()
    for index, raw in enumerate(adapters_value):
        if not isinstance(raw, dict):
            result.fail(f"adapter entry {index} must be an object")
            continue
        for key in sorted(set(raw) - {"tool", "path"}):
            result.fail(f"adapter entry {index} contains unsupported property: {key}")
        tool = raw.get("tool")
        path = raw.get("path")
        if not isinstance(tool, str) or not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", tool):
            result.fail(f"adapter entry {index} has invalid tool")
            continue
        if not isinstance(path, str) or not path.strip():
            result.fail(f"adapter entry {index} has invalid path")
            continue
        if path in seen_adapters:
            result.fail(f"adapter path is declared more than once: {path}")
            continue
        seen_adapters.add(path)
        _validate_existing_file(result, path, label=f"{tool} adapter")
        result.adapters.append(Adapter(tool=tool, path=path))


def _validate_template_presence(result: ValidationResult) -> None:
    for path in ("README.md", "PROJECT.md", "DECISIONS.md"):
        _validate_existing_file(result, path, label="required template file")

    if (result.root / "standard").is_dir():
        for path in (
            "docs/validation-checklist.md",
            "standard/scopes.md",
            "standard/adapters.md",
        ):
            _validate_existing_file(result, path, label="required standard file")


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return ""


def _mapped_files(result: ValidationResult) -> list[tuple[str, Path]]:
    mapped: list[tuple[str, Path]] = []
    for name in ROLE_ORDER:
        role = result.roles.get(name)
        if not role or not role.primary:
            continue
        role_paths = [(f"{name} primary", role.primary)]
        role_paths.extend((f"{name} supplement", path) for path in role.supplements)
        for label, value in role_paths:
            candidate, error = _repo_relative_path(result.root, value)
            if not error and candidate and candidate.is_file() and not candidate.is_symlink():
                mapped.append((label, candidate))
    return mapped


def _validate_supplement_routing(result: ValidationResult) -> None:
    for name in ROLE_ORDER:
        role = result.roles.get(name)
        if not role or not role.primary or not role.supplements:
            continue
        primary, error = _repo_relative_path(result.root, role.primary)
        if error or not primary or not primary.is_file():
            continue
        content = _read_text(primary)
        for supplement in role.supplements:
            if supplement not in content:
                result.warn(
                    f"{name.title()} primary {role.primary} does not route to "
                    f"supplement {supplement}"
                )


def _strip_fragment_and_title(value: str) -> str:
    value = value.strip().strip("<>")
    if " " in value and not value.startswith(("./", "../")):
        value = value.split(" ", 1)[0]
    return value.split("#", 1)[0]


def _looks_like_local_document(value: str, *, markdown_link: bool) -> bool:
    if not value or value.startswith(("http://", "https://", "mailto:", "#")):
        return False
    if any(token in value for token in ("*", "{", "}", "<", ">", "|")):
        return False
    path = PurePosixPath(value)
    if any(part.startswith(("your-", "example-")) for part in path.parts):
        return False
    if (
        len(path.parts) == 1
        and not markdown_link
        and not value.startswith(("./", "../"))
        and path.name not in KNOWN_INLINE_ROOT_DOCUMENTS
    ):
        return False
    return path.suffix.lower() in MARKDOWN_SUFFIXES


def _document_references(path: Path) -> Iterable[tuple[int, str, bool]]:
    fenced = False
    for number, line in enumerate(_read_text(path).splitlines(), start=1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue

        for match in re.finditer(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", line):
            value = _strip_fragment_and_title(match.group(1))
            if _looks_like_local_document(value, markdown_link=True):
                yield number, value, True
        for match in re.finditer(r"`([^`\n]+)`", line):
            value = _strip_fragment_and_title(match.group(1))
            if _looks_like_local_document(value, markdown_link=False):
                yield number, value, False


def _resolve_document_reference(
    root: Path, source: Path, value: str, markdown_link: bool
) -> Path | None:
    if value.startswith("/"):
        relative = value[1:]
        base = root
    elif markdown_link or value.startswith(("./", "../")):
        relative = value
        base = source.parent
    else:
        relative = value
        base = root

    candidate = base.joinpath(*PurePosixPath(relative).parts)
    try:
        candidate.resolve(strict=False).relative_to(root.resolve())
    except ValueError:
        return None
    return candidate


def _validate_document_references(result: ValidationResult) -> None:
    seen: set[tuple[str, int, str]] = set()
    for _, path in _mapped_files(result):
        relative_source = path.relative_to(result.root).as_posix()
        for line, value, markdown_link in _document_references(path):
            key = (relative_source, line, value)
            if key in seen:
                continue
            seen.add(key)
            target = _resolve_document_reference(result.root, path, value, markdown_link)
            if target is None or not target.is_file():
                result.warn(
                    f"Broken local document reference in {relative_source}:{line}: {value}"
                )


def _validate_adapters(result: ValidationResult) -> None:
    mapped_roles = [
        role
        for name in ROLE_ORDER
        if (role := result.roles.get(name)) is not None and role.primary
    ]
    for adapter in result.adapters:
        path, error = _repo_relative_path(result.root, adapter.path)
        if error or not path or not path.is_file():
            continue
        content = _read_text(path)
        line_count = len(content.splitlines())
        limit = 40 if adapter.path == "AGENTS.md" else 30
        if line_count >= limit:
            result.warn(
                f"{adapter.path} has {line_count} lines; soft limit is under {limit}"
            )
        for role in mapped_roles:
            assert role.primary is not None
            if role.primary not in content:
                result.warn(
                    f"{adapter.path} does not route to {role.name.title()} primary {role.primary}"
                )


def _normalize_statement(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("`", "")
    value = re.sub(r"^[#>*+\-\d.()\s]+", "", value)
    value = re.sub(r"\s+", " ", value).strip().lower()
    return value


def _statements(path: Path) -> Iterable[tuple[int, str]]:
    fenced = False
    for number, line in enumerate(_read_text(path).splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            fenced = not fenced
            continue
        if fenced or not stripped or stripped.startswith("|"):
            continue
        normalized = _normalize_statement(stripped)
        if len(normalized) < 60:
            continue
        if any(fragment in normalized for fragment in BOILERPLATE_DUPLICATE_FRAGMENTS):
            continue
        yield number, normalized


def _validate_duplicates(result: ValidationResult) -> None:
    canonical: dict[str, tuple[str, int]] = {}
    for _, path in _mapped_files(result):
        relative = path.relative_to(result.root).as_posix()
        for line, statement in _statements(path):
            canonical.setdefault(statement, (relative, line))

    for adapter in result.adapters:
        path, error = _repo_relative_path(result.root, adapter.path)
        if error or not path or not path.is_file():
            continue
        for line, statement in _statements(path):
            source = canonical.get(statement)
            if source:
                result.warn(
                    "Possible duplicate durable sentence in "
                    f"{source[0]}:{source[1]} and {adapter.path}:{line}"
                )


def validate_repository(
    repository: Path | str,
    *,
    mode: str | None = None,
    config_path: Path | str | None = None,
) -> ValidationResult:
    root = Path(repository).resolve()
    if not root.is_dir():
        raise UsageError(f"repository is not a directory: {repository}")

    requested_config = Path(config_path).resolve() if config_path else None
    default_config = root / "aews.json"
    selected_mode = mode or (
        "adoption" if requested_config or default_config.is_file() else "template"
    )
    if selected_mode not in {"template", "adoption"}:
        raise UsageError(f"unsupported mode: {selected_mode}")
    if selected_mode == "template" and requested_config is not None:
        raise UsageError("--config is only valid in adoption mode")

    result = ValidationResult(root=root, mode=selected_mode)
    if selected_mode == "template":
        result.roles = _template_roles(root)
        result.adapters = _discover_template_adapters(root)
        _validate_template_presence(result)
        for name, role in result.roles.items():
            if role.primary:
                _validate_existing_file(result, role.primary, label=f"{name} primary")
    else:
        selected_config = requested_config or default_config
        config = _load_adoption_config(selected_config)
        _parse_adoption_mapping(result, config)

    _validate_supplement_routing(result)
    _validate_document_references(result)
    _validate_adapters(result)
    _validate_duplicates(result)
    result.failures.sort()
    result.warnings.sort()
    return result


def format_result(result: ValidationResult) -> str:
    try:
        repository_label = result.root.relative_to(Path.cwd().resolve()).as_posix() or "."
    except ValueError:
        repository_label = result.root.as_posix()

    lines = [
        "AEWS validation",
        "",
        f"Mode: {result.mode}",
        f"Repository: {repository_label}",
        "Role mapping:",
    ]
    for name in ROLE_ORDER:
        role = result.roles.get(name)
        label = name.title()
        if role is None:
            lines.append(f"- {label}: missing")
        elif role.primary:
            lines.append(f"- {label}: {role.primary}")
            if role.supplements:
                lines.append(f"- {label} supplements: {', '.join(role.supplements)}")
        else:
            lines.append(f"- {label}: {role.status}")

    lines.extend(["", "Adapters:"])
    if result.adapters:
        lines.extend(f"- {adapter.tool}: {adapter.path}" for adapter in result.adapters)
    else:
        lines.append("- None")

    lines.extend(["", "Failures:"])
    lines.extend(f"- {message}" for message in result.failures or ["None"])
    lines.extend(["", "Warnings:"])
    lines.extend(f"- {message}" for message in result.warnings or ["None"])
    lines.extend(
        [
            "",
            "Manual review still required:",
            "- Scope placement",
            "- Lifecycle freshness",
            "- Decision quality",
            "- Supplement ownership",
        ]
    )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", nargs="?", default=".")
    parser.add_argument("--mode", choices=("template", "adoption"))
    parser.add_argument("--config", help="Path to an adoption mapping JSON file")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        result = validate_repository(
            args.repository,
            mode=args.mode,
            config_path=args.config,
        )
    except UsageError as exc:
        print("AEWS validation", file=sys.stderr)
        print(f"Usage error: {exc}", file=sys.stderr)
        return 2

    print(format_result(result))
    return 1 if result.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
