from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from scripts import public_release_env as pre
else:
    from scripts import public_release_env as pre


PROJECT_AGENT_TEMPLATES: list[dict[str, Any]] = [
    {
        "file": "project-manager.json",
        "payload": {
            "agent_id": "project-manager",
            "display_name": "Project Manager Agent",
            "preferred_model": None,
            "role": "manager",
            "enabled": True,
            "isolation_method": None,
            "parallel_safe": None,
            "integration_review_required": None,
            "capability_tags_subset": None,
            "allowed_skills_mcp_subset": ["research-stack-manager", "project-retrospective-evolver"],
            "write_scope_subset": ["outputs/agent-runs/<run_id>/<agent_id>/"],
            "max_execution_mode": "sequential_multi_agent_execution",
            "required_inputs": ["route_id", "clarification_card", "dispatch_contract"],
            "expected_outputs": ["summary.md", "result.json"],
            "review_gate": None,
        },
    },
    {
        "file": "literature-producer.json",
        "payload": {
            "agent_id": "literature-producer",
            "display_name": "Literature Agent",
            "preferred_model": None,
            "role": "producer",
            "enabled": False,
            "isolation_method": None,
            "parallel_safe": None,
            "integration_review_required": None,
            "capability_tags_subset": None,
            "allowed_skills_mcp_subset": None,
            "write_scope_subset": ["outputs/agent-runs/<run_id>/<agent_id>/"],
            "max_execution_mode": None,
            "required_inputs": ["clarification_card", "project_truth_sources"],
            "expected_outputs": ["summary.md", "result.json"],
            "review_gate": "mandatory-review-when-required",
        },
    },
    {
        "file": "social-platform-producer.json",
        "payload": {
            "agent_id": "social-platform-producer",
            "display_name": "Platform Evidence Agent",
            "preferred_model": None,
            "role": "producer",
            "enabled": False,
            "isolation_method": None,
            "parallel_safe": None,
            "integration_review_required": None,
            "capability_tags_subset": None,
            "allowed_skills_mcp_subset": None,
            "write_scope_subset": ["outputs/agent-runs/<run_id>/<agent_id>/"],
            "max_execution_mode": None,
            "required_inputs": ["clarification_card", "evidence_scope"],
            "expected_outputs": ["summary.md", "result.json"],
            "review_gate": "mandatory-review-when-required",
        },
    },
    {
        "file": "analysis-producer.json",
        "payload": {
            "agent_id": "analysis-producer",
            "display_name": "Analysis Agent",
            "preferred_model": None,
            "role": "producer",
            "enabled": False,
            "isolation_method": None,
            "parallel_safe": None,
            "integration_review_required": None,
            "capability_tags_subset": None,
            "allowed_skills_mcp_subset": None,
            "write_scope_subset": ["outputs/agent-runs/<run_id>/<agent_id>/"],
            "max_execution_mode": None,
            "required_inputs": ["dataset_scope", "analysis_plan"],
            "expected_outputs": ["summary.md", "result.json"],
            "review_gate": "mandatory-review-when-required",
        },
    },
    {
        "file": "writing-producer.json",
        "payload": {
            "agent_id": "writing-producer",
            "display_name": "Writing Agent",
            "preferred_model": None,
            "role": "producer",
            "enabled": False,
            "isolation_method": None,
            "parallel_safe": None,
            "integration_review_required": None,
            "capability_tags_subset": None,
            "allowed_skills_mcp_subset": None,
            "write_scope_subset": ["outputs/agent-runs/<run_id>/<agent_id>/"],
            "max_execution_mode": None,
            "required_inputs": ["writing_scope", "verified_citations"],
            "expected_outputs": ["summary.md", "result.json"],
            "review_gate": "mandatory-review-when-required",
        },
    },
    {
        "file": "reviewer.json",
        "payload": {
            "agent_id": "reviewer",
            "display_name": "Reviewer Agent",
            "preferred_model": None,
            "role": "reviewer",
            "enabled": True,
            "isolation_method": None,
            "parallel_safe": None,
            "integration_review_required": None,
            "capability_tags_subset": None,
            "allowed_skills_mcp_subset": [
                "citation-verifier",
                "academic-paper-review",
                "openalex-mcp",
                "semantic-scholar-mcp",
            ],
            "write_scope_subset": ["outputs/agent-runs/<run_id>/<agent_id>/"],
            "max_execution_mode": "sequential_multi_agent_execution",
            "required_inputs": ["target_agent_result", "target_agent_summary"],
            "expected_outputs": ["review.<target_agent_id>.md", "gate.<target_agent_id>.json"],
            "review_gate": "target-specific",
        },
    },
]


def _write_json_if_missing(target: Path, payload: Any) -> None:
    if target.exists():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _write_text_if_missing(target: Path, content: str) -> None:
    if target.exists():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def _ensure_git_repo(project_root: Path) -> bool:
    if (project_root / ".git").exists():
        return True
    git = shutil.which("git")
    if not git:
        return False
    result = subprocess.run([git, "init", "-b", "main", str(project_root)], capture_output=True, text=True)
    return result.returncode == 0


def _append_codex_trust(project_root: Path) -> bool:
    if not pre.CODEX_CONFIG_PATH.exists():
        return False
    pre.CODEX_CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    project_key = f"[projects.'{project_root.as_posix()}']"
    desired_block = f'{project_key}\ntrust_level = "trusted"\n'
    config_text = pre.CODEX_CONFIG_PATH.read_text(encoding="utf-8")
    if project_key in config_text:
        return True
    updated = config_text.rstrip() + "\n\n" + desired_block
    pre.CODEX_CONFIG_PATH.write_text(updated, encoding="utf-8")
    return True


def _load_registry() -> dict[str, Any]:
    pre.ensure_app_state_dirs()
    if not pre.APP_PROJECTS_REGISTRY.exists():
        return {"projects": []}
    try:
        return json.loads(pre.APP_PROJECTS_REGISTRY.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"projects": []}


def _save_registry(payload: dict[str, Any]) -> None:
    pre.ensure_app_state_dirs()
    pre.APP_PROJECTS_REGISTRY.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def register_project(project_root: Path, route_hint: str | None = None) -> None:
    registry = _load_registry()
    rows = registry.setdefault("projects", [])
    normalized = str(project_root.resolve())
    existing = [row for row in rows if row.get("path") == normalized]
    if existing:
        if route_hint:
            existing[0]["route_hint"] = route_hint
        _save_registry(registry)
        return
    rows.append(
        {
            "name": project_root.name,
            "path": normalized,
            "route_hint": route_hint,
            "source": "local",
        }
    )
    _save_registry(registry)


def initialize_project(project_root: Path, skip_codex_trust: bool = False, route_hint: str | None = None) -> dict[str, Any]:
    project_root = project_root.expanduser().resolve()
    project_name = project_root.name

    root_agents_path = pre.SKILLS_ROOT / "AGENTS.md"
    if not root_agents_path.exists():
        raise FileNotFoundError(f"公开版 skills/AGENTS.md 不存在：{root_agents_path}")

    project_agents_dir = project_root / ".codex" / "agents"
    dispatch_dir = project_root / ".codex" / "dispatch"
    context_packets_dir = project_root / ".codex" / "context-packets"
    agent_runs_dir = project_root / "outputs" / "agent-runs"
    handoff_logs_dir = project_root / "logs" / "agent-handoffs"
    gate_logs_dir = project_root / "logs" / "quality-gates"
    project_state_dir = project_root / "logs" / "project-state"

    for path in (
        project_agents_dir,
        dispatch_dir,
        context_packets_dir,
        agent_runs_dir,
        handoff_logs_dir,
        gate_logs_dir,
        project_state_dir,
    ):
        path.mkdir(parents=True, exist_ok=True)

    git_initialized = _ensure_git_repo(project_root)

    _write_text_if_missing(
        project_root / ".gitignore",
        ".venv/\n__pycache__/\n.ipynb_checkpoints/\noutputs/\nartifacts/\n*.log\n*.tmp\n.env\n.env.*\n",
    )

    _write_text_if_missing(
        project_root / "README.md",
        "\n".join(
            [
                f"# {project_name}",
                "",
                "This project was initialized from Codex Research Stack.",
                "",
                "## What you get",
                "",
                "- A Git repository when Git is available",
                "- Project-level AGENTS.md",
                "- .codex/agents starter definitions",
                "- Canonical dispatch, handoff, gate, and project-state directories",
                "- Pipeline status and writing-quality report templates",
                "",
                "## Recommended next step",
                "",
                "Use the desktop app or the public bridge to preview a route and scaffold the first research squad.",
            ]
        )
        + "\n",
    )

    _write_text_if_missing(
        project_root / "AGENTS.md",
        "\n".join(
            [
                "# AGENTS",
                "",
                "This project inherits the global constraints from skills/AGENTS.md in the Codex Research Stack repository.",
                "Project rules may only become stricter; they must not expand permissions or bypass the required citation, evidence, writing-capture, or reproducibility chains.",
                "",
                "```yaml",
                "agent_constraints:",
                "  forbid_skills_mcp: []",
                "  forbid_write_roots: []",
                "  max_execution_mode: null",
                "  require_review_for:",
                "    - paper_draft",
                "    - revision_package",
                "    - submission_package",
                "    - figures_tables",
                "    - reproducibility_bundle",
                "    - literature_synthesis",
                "    - case_dataset",
                "    - project_map",
                "  project_truth_sources:",
                "    - research-map.md",
                "    - findings-memory.md",
                "    - material-passport.yaml",
                "    - evidence-ledger.yaml",
                "```",
            ]
        )
        + "\n",
    )

    _write_text_if_missing(
        project_root / "research-map.md",
        "# Research Map\n\n- Research question:\n- Active route:\n- Current stage:\n- Expected deliverables:\n",
    )
    _write_text_if_missing(
        project_root / "findings-memory.md",
        "# Findings Memory\n\n- Confirmed facts:\n- Rejected paths:\n- Pending verification:\n",
    )
    _write_text_if_missing(
        project_root / "material-passport.yaml",
        "\n".join(
            [
                f"project_name: {project_name}",
                f"route_id: {route_hint if route_hint else 'null'}",
                "current_stage: research_design",
                "data_access_level: public_open",
                "materials: []",
                "ethics_notes: []",
                "truth_sources:",
                "  - research-map.md",
                "  - findings-memory.md",
                "  - material-passport.yaml",
                "  - evidence-ledger.yaml",
            ]
        )
        + "\n",
    )
    _write_text_if_missing(project_root / "evidence-ledger.yaml", "entries: []\n")

    _write_json_if_missing(
        gate_logs_dir / "pipeline-status.json",
        {
            "route_id": route_hint,
            "current_stage": "research_design",
            "completed_stages": [],
            "gate_decisions": {},
            "allowed_to_advance": False,
        },
    )
    _write_json_if_missing(
        gate_logs_dir / "writing-quality-report.json",
        {
            "status": "pending",
            "checked_deliverable": None,
            "target_paths": [],
            "checks": {
                "style_calibration": {"decision": "pending", "notes": []},
                "argument_chain_closure": {"decision": "pending", "notes": []},
                "citation_alignment": {"decision": "pending", "notes": []},
                "empty_phrase_scan": {"decision": "pending", "hits": [], "notes": []},
            },
            "banned_phrases": ["总而言之", "双刃剑", "多维度视角"],
            "generated_by": None,
            "updated_at": None,
        },
    )
    _write_json_if_missing(
        project_state_dir / "current.json",
        {
            "project_name": project_name,
            "route_id": route_hint,
            "project_type": None,
            "dispatch_run_id": None,
            "dispatch_stage": "planning",
            "pipeline_stage": "research_design",
            "status": "initialized",
            "current_owner_agent_id": "project-manager",
            "current_owner_display_name": "Project Manager Agent",
            "blockers": [],
            "next_quality_gates": [],
            "selected_agents": [],
            "selected_producers": [],
            "selected_reviewers": [],
            "review_agents": {},
            "milestones": [{"id": "project_initialized", "label": "Project initialized", "status": "complete"}],
        },
    )
    _write_text_if_missing(project_state_dir / "history.md", "# Project State History\n\n- Project initialized.\n")

    for template in PROJECT_AGENT_TEMPLATES:
        _write_json_if_missing(project_agents_dir / template["file"], template["payload"])

    trust_updated = False
    if not skip_codex_trust:
        trust_updated = _append_codex_trust(project_root)

    register_project(project_root, route_hint=route_hint)

    return {
        "ok": True,
        "project_root": str(project_root),
        "project_name": project_name,
        "git_initialized": git_initialized,
        "codex_trust_updated": trust_updated,
        "route_hint": route_hint,
        "paths": {
            "project_agents_dir": str(project_agents_dir),
            "dispatch_dir": str(dispatch_dir),
            "context_packets_dir": str(context_packets_dir),
            "gate_logs_dir": str(gate_logs_dir),
            "project_state_dir": str(project_state_dir),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize a public Codex Research Stack project scaffold.")
    parser.add_argument("--path", required=True, help="Project root path.")
    parser.add_argument("--route-hint", default=None, help="Optional route hint.")
    parser.add_argument("--skip-codex-trust", action="store_true", help="Do not write Codex trust config.")
    args = parser.parse_args()
    result = initialize_project(Path(args.path), skip_codex_trust=args.skip_codex_trust, route_hint=args.route_hint)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
