from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from scripts import init_research_project
    from scripts import vela_handoff
    from scripts import public_release_env as pre
    from scripts import vela_contract as contract
    from scripts import vela_initializer as initializer
else:
    from scripts import init_research_project
    from scripts import vela_handoff
    from scripts import public_release_env as pre
    from scripts import vela_contract as contract
    from scripts import vela_initializer as initializer


def _print_json(payload: object) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


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


def cmd_handoff_new(args: argparse.Namespace) -> int:
    result = vela_handoff.create_handoff(Path(args.project or "."), args.template)
    _print_json(result)
    return 0 if result.get("ok") else 1


def cmd_handoff_lint(args: argparse.Namespace) -> int:
    result = vela_handoff.lint_handoff(Path(args.path))
    _print_json(result)
    return 0 if result["ok"] else 1


def cmd_handoff_render(args: argparse.Namespace) -> int:
    path = Path(args.path)
    try:
        rendered = vela_handoff.render_handoff_prompt(path)
    except ValueError:
        _print_json(vela_handoff.lint_handoff(path))
        return 1
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
