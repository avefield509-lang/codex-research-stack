from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from scripts import init_research_project
    from scripts import public_release_env as pre
    from scripts import vela_contract as contract
    from scripts import vela_initializer as initializer
else:
    from scripts import init_research_project
    from scripts import public_release_env as pre
    from scripts import vela_contract as contract
    from scripts import vela_initializer as initializer


HANDOFF_REQUIRED_MARKERS = (
    "schema_version:",
    "handoff_id:",
    "task:",
    "relevant_files:",
    "constraints:",
    "expected_output:",
    "review_standard:",
)


def _print_json(payload: object) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def _next_handoff_id(handoffs_dir: Path) -> str:
    handoffs_dir.mkdir(parents=True, exist_ok=True)
    existing = sorted(handoffs_dir.glob("H*.yaml"))
    if not existing:
        return "H001"
    numbers = []
    for path in existing:
        stem = path.stem.upper()
        if stem.startswith("H") and stem[1:].isdigit():
            numbers.append(int(stem[1:]))
    return f"H{(max(numbers) + 1 if numbers else 1):03d}"


def cmd_doctor(_args: argparse.Namespace) -> int:
    pre.ensure_app_state_dirs()
    codex_home = pre.CODEX_HOME
    initializer_report = initializer.validate_manifest()
    payload = {
        "ok": True,
        "vela_repo": str(pre.REPO_ROOT),
        "python": sys.executable,
        "codex_home": str(codex_home),
        "codex_home_exists": codex_home.exists(),
        "vela_home": str(pre.APP_STATE_HOME),
        "package_exists": contract.package_root().exists(),
        "initializer_manifest": str(initializer.default_manifest_path()),
        "initializer_manifest_ok": initializer_report["ok"],
        "initializer_manifest_errors": initializer_report["errors"],
        "git": shutil.which("git"),
        "next_action": "Run `vela init <project>` or `python scripts/vela.py init <project>`.",
    }
    payload["ok"] = bool(payload["package_exists"] and payload["initializer_manifest_ok"])
    _print_json(payload)
    return 0 if payload["ok"] else 1


def cmd_init(args: argparse.Namespace) -> int:
    result = init_research_project.initialize_project(
        Path(args.path),
        skip_codex_trust=args.skip_codex_trust,
        route_hint=args.route_hint or args.profile,
    )
    _print_json(result)
    return 0


def _handoff_template(handoff_id: str, template: str) -> str:
    task = "Review whether a claim is supported by named evidence." if template == "claim-check" else "Read the relevant files and produce a bounded next-step note."
    return "\n".join(
        [
            "schema_version: vela.codex.handoff.v1",
            f"handoff_id: {handoff_id}",
            f"created_at: {contract.utc_now()}",
            "created_by: human",
            "surface: cli",
            "mode: review_only",
            "project:",
            "  title: TODO",
            "  stage: research_design",
            "scope:",
            f"  task: {task}",
            "  relevant_files:",
            "    - research-map.md",
            "    - evidence-ledger.yaml",
            "  excluded_files:",
            "    - private-notes/",
            "    - credentials/",
            "constraints:",
            "  - Do not add new claims.",
            "  - Do not treat material notes as verified evidence.",
            "expected_output:",
            "  format: markdown",
            f"  path: logs/codex-runs/{handoff_id}-result.md",
            "review_standard:",
            "  - Every support judgment must cite an evidence_id.",
            "  - Unsupported or uncertain claims must remain marked as needs_review.",
            "completion:",
            "  validation_commands:",
            f"    - vela handoff lint handoffs/{handoff_id}.yaml",
            "  human_review_required: true",
            "",
        ]
    )


def cmd_handoff_new(args: argparse.Namespace) -> int:
    project_root = Path(args.project or ".").expanduser().resolve()
    handoffs_dir = project_root / "handoffs"
    handoff_id = _next_handoff_id(handoffs_dir)
    target = handoffs_dir / f"{handoff_id}.yaml"
    target.write_text(_handoff_template(handoff_id, args.template), encoding="utf-8")
    prompt_target = handoffs_dir / f"{handoff_id}.prompt.md"
    prompt_target.write_text(_render_handoff_prompt(target), encoding="utf-8")
    _print_json({"ok": True, "handoff": str(target), "prompt": str(prompt_target)})
    return 0


def _lint_handoff(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    errors = []
    if not path.exists():
        errors.append(f"Handoff file not found: {path}")
    for marker in HANDOFF_REQUIRED_MARKERS:
        if marker not in text:
            errors.append(f"Missing marker: {marker}")
    return {
        "schema_version": "vela.validation.report.v1",
        "scope": str(path),
        "decision": "pass" if not errors else "needs_review",
        "errors": errors,
        "warnings": [],
    }


def cmd_handoff_lint(args: argparse.Namespace) -> int:
    result = _lint_handoff(Path(args.path))
    _print_json(result)
    return 0 if result["decision"] == "pass" else 1


def _render_handoff_prompt(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return "\n".join(
        [
            "# VELA Codex Handoff",
            "",
            "Read this bounded handoff before acting. Do not expand scope unless the user approves.",
            "",
            "```yaml",
            text.rstrip(),
            "```",
            "",
            "Return changed files, validation results, unsupported claims, and remaining blockers.",
            "",
        ]
    )


def cmd_handoff_render(args: argparse.Namespace) -> int:
    path = Path(args.path)
    rendered = _render_handoff_prompt(path)
    if args.out:
        target = Path(args.out)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rendered, encoding="utf-8")
        _print_json({"ok": True, "output": str(target)})
    else:
        print(rendered)
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    result = contract.validate_project(Path(args.path), repair_context=args.repair_context)
    _print_json(result)
    return 0 if result["decision"] == "pass" else 1


def cmd_export_helm_context(args: argparse.Namespace) -> int:
    context = contract.write_project_context(Path(args.path))
    _print_json({"ok": True, "context": str(Path(args.path).expanduser().resolve() / ".vela" / "context.json"), "schema_version": context["schema_version"]})
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="VELA workflow wrapper CLI.")
    sub = parser.add_subparsers(dest="command", required=True)

    doctor = sub.add_parser("doctor", help="Check the local VELA/Codex environment.")
    doctor.set_defaults(func=cmd_doctor)

    init = sub.add_parser("init", help="Initialize a VELA wrapper project.")
    init.add_argument("path", help="Project root path.")
    init.add_argument("--profile", default="codex-research", help="Starter profile name.")
    init.add_argument("--route-hint", default=None, help="Optional route hint.")
    init.add_argument("--skip-codex-trust", action="store_true", help="Do not modify Codex trust config.")
    init.set_defaults(func=cmd_init)

    validate = sub.add_parser("validate", help="Validate a VELA project.")
    validate.add_argument("path", nargs="?", default=".", help="Project root path.")
    validate.add_argument("--repair-context", action="store_true", help="Regenerate .vela/context.json before validating.")
    validate.set_defaults(func=cmd_validate)

    export = sub.add_parser("export-helm-context", help="Regenerate .vela/context.json for HELM.")
    export.add_argument("path", nargs="?", default=".", help="Project root path.")
    export.set_defaults(func=cmd_export_helm_context)

    handoff = sub.add_parser("handoff", help="Create, lint, or render Codex handoffs.")
    handoff_sub = handoff.add_subparsers(dest="handoff_command", required=True)
    handoff_new = handoff_sub.add_parser("new", help="Create a bounded handoff packet.")
    handoff_new.add_argument("--project", default=".", help="Project root path.")
    handoff_new.add_argument("--template", default="claim-check", choices=["claim-check", "read-project"], help="Handoff template.")
    handoff_new.set_defaults(func=cmd_handoff_new)
    handoff_lint = handoff_sub.add_parser("lint", help="Lint a handoff packet.")
    handoff_lint.add_argument("path", help="Handoff YAML path.")
    handoff_lint.set_defaults(func=cmd_handoff_lint)
    handoff_render = handoff_sub.add_parser("render", help="Render a handoff packet into a Codex prompt.")
    handoff_render.add_argument("path", help="Handoff YAML path.")
    handoff_render.add_argument("--out", default=None, help="Optional prompt output path.")
    handoff_render.set_defaults(func=cmd_handoff_render)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    raise SystemExit(args.func(args))


if __name__ == "__main__":
    main()
