from __future__ import annotations

import json
import sys
from pathlib import Path
import re

try:
    from public_release_env import (
        ASSETS_DIR,
        CATALOG_DIR,
        CODEX_CONFIG_PATH,
        CODEX_HOME,
        CODEX_SKILLS_DIR,
        DOCS_DIR,
        PLUGIN_DIR,
        PROFILES_DIR,
        REPO_ROOT,
        SCHEMAS_DIR,
        SCRIPTS_DIR,
        SKILLS_ROOT,
    )
except ModuleNotFoundError:
    from scripts.public_release_env import (
        ASSETS_DIR,
        CATALOG_DIR,
        CODEX_CONFIG_PATH,
        CODEX_HOME,
        CODEX_SKILLS_DIR,
        DOCS_DIR,
        PLUGIN_DIR,
        PROFILES_DIR,
        REPO_ROOT,
        SCHEMAS_DIR,
        SCRIPTS_DIR,
        SKILLS_ROOT,
    )
from validate_research_pipeline import validate_static as validate_pipeline_static


TASK_TYPE_ENUM = {
    "orchestration",
    "project_retrospective",
    "stack_governance",
    "paper_review",
    "literature_review",
    "citation_integrity",
    "literature_discovery",
    "quant_analysis",
    "text_analysis",
    "network_analysis",
    "research_design",
    "dataset_discovery",
    "digital_trace_capture",
    "simulation",
    "reproducibility",
    "runtime_ops",
    "figure_table",
    "social_evidence",
    "writing_export",
    "writing_capture",
    "response_revision",
    "submission_packaging",
    "knowledge_sync",
    "cloud_routing",
    "skill_vetting",
    "environment_ops",
    "computational_social_science",
    "general_research",
}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def collect_catalog_metadata(catalog: dict, routing_table: dict) -> dict:
    gates = read_json(CATALOG_DIR / "quality_gates.json")
    stages = read_json(CATALOG_DIR / "research_pipeline_stages.json")
    access = read_json(CATALOG_DIR / "data_access_matrix.json")
    valid_gate_ids = {item["id"] for item in gates.get("gates", [])}
    valid_stage_ids = {item["id"] for item in stages.get("stages", [])}
    valid_access_levels = {item["id"] for item in access.get("levels", [])}

    active_skill_missing: list[str] = []
    active_skill_invalid: list[str] = []
    for name, item in catalog.get("skills", {}).items():
        if item.get("status") != "active":
            continue
        for required in ("task_type", "data_access_level", "quality_gate_required", "stage_scope", "subagent_allowed"):
            if required not in item:
                active_skill_missing.append(f"{name}:{required}")
        if item.get("task_type") not in TASK_TYPE_ENUM:
            active_skill_invalid.append(f"{name}:task_type")
        if item.get("data_access_level") not in valid_access_levels:
            active_skill_invalid.append(f"{name}:data_access_level")
        if not isinstance(item.get("subagent_allowed"), bool):
            active_skill_invalid.append(f"{name}:subagent_allowed")
        if set(item.get("quality_gate_required", [])) - valid_gate_ids:
            active_skill_invalid.append(f"{name}:quality_gate_required")
        if set(item.get("stage_scope", [])) - valid_stage_ids:
            active_skill_invalid.append(f"{name}:stage_scope")

    route_missing: list[str] = []
    route_invalid: list[str] = []
    for route in routing_table.get("routes", []):
        route_id = route.get("id", "<unknown>")
        for required in ("task_type", "data_access_level", "quality_gate_required", "stage_scope", "subagent_allowed"):
            if required not in route:
                route_missing.append(f"{route_id}:{required}")
        if route.get("task_type") not in TASK_TYPE_ENUM:
            route_invalid.append(f"{route_id}:task_type")
        if route.get("data_access_level") not in valid_access_levels:
            route_invalid.append(f"{route_id}:data_access_level")
        if not isinstance(route.get("subagent_allowed"), bool):
            route_invalid.append(f"{route_id}:subagent_allowed")
        if set(route.get("quality_gate_required", [])) - valid_gate_ids:
            route_invalid.append(f"{route_id}:quality_gate_required")
        if set(route.get("stage_scope", [])) - valid_stage_ids:
            route_invalid.append(f"{route_id}:stage_scope")

    return {
        "active_skill_missing_metadata": sorted(active_skill_missing),
        "active_skill_invalid_metadata": sorted(active_skill_invalid),
        "route_missing_metadata": sorted(route_missing),
        "route_invalid_metadata": sorted(route_invalid),
    }


def main() -> None:
    errors: list[str] = []
    warnings: list[str] = []

    required_root = [
        REPO_ROOT / "README.md",
        REPO_ROOT / "README.zh-CN.md",
        REPO_ROOT / "LICENSE",
        REPO_ROOT / ".gitignore",
        REPO_ROOT / "CONTRIBUTING.md",
        REPO_ROOT / "PRIVACY-BOUNDARIES.md",
        REPO_ROOT / "_config.yml",
    ]
    required_docs = [
        DOCS_DIR / "index.md",
        DOCS_DIR / "getting-started.md",
        DOCS_DIR / "index.html",
        DOCS_DIR / "zh" / "index.html",
        DOCS_DIR / "operator-guide.md",
        DOCS_DIR / "new-project-guide.md",
        DOCS_DIR / "architecture.md",
        DOCS_DIR / "use-cases.md",
        DOCS_DIR / "public-boundary.md",
        DOCS_DIR / "integrations.md",
        DOCS_DIR / "roadmap.md",
    ]
    required_assets = [
        ASSETS_DIR / "hero-overview.png",
        ASSETS_DIR / "social-preview.png",
        ASSETS_DIR / "social-preview.svg",
        ASSETS_DIR / "multi-agent-workspace.png",
        ASSETS_DIR / "pipeline-gates-overview.png",
        DOCS_DIR / "assets" / "site.css",
        DOCS_DIR / "assets" / "social-preview.png",
        DOCS_DIR / "assets" / "hero-overview.png",
        DOCS_DIR / "assets" / "multi-agent-workspace.png",
        DOCS_DIR / "assets" / "pipeline-gates-overview.png",
        DOCS_DIR / "assets" / "architecture-map.svg",
        PLUGIN_DIR / "assets" / "route-explanation-card.svg",
        PLUGIN_DIR / "assets" / "multi-agent-dispatch.svg",
        PLUGIN_DIR / "assets" / "research-system-overview.png",
        PLUGIN_DIR / "assets" / "research-team-workspace.png",
    ]
    required_scripts = [
        SCRIPTS_DIR / "bootstrap_agent_dispatch.py",
        SCRIPTS_DIR / "init-research-project.ps1",
        SCRIPTS_DIR / "plan_research_team.py",
        SCRIPTS_DIR / "scan_research_stack.py",
        SCRIPTS_DIR / "sync_research_autopilot_skills.ps1",
        SCRIPTS_DIR / "validate_agents_contract.py",
        SCRIPTS_DIR / "validate_external_systems_research.py",
        SCRIPTS_DIR / "validate_harness_adapter_contract.py",
        SCRIPTS_DIR / "validate_research_pipeline.py",
        SCRIPTS_DIR / "validate_research_stack.py",
        SCRIPTS_DIR / "validate_subagent_registry.py",
        SCRIPTS_DIR / "writing_reference_capture_local.py",
    ]
    required_catalog = [
        CATALOG_DIR / "agent_execution_modes.json",
        CATALOG_DIR / "conflict_matrix.json",
        CATALOG_DIR / "data_access_matrix.json",
        CATALOG_DIR / "external_systems_research.json",
        CATALOG_DIR / "multi_agent_harness_adapter.json",
        CATALOG_DIR / "project_scope_rules.json",
        CATALOG_DIR / "quality_gates.json",
        CATALOG_DIR / "research_team_playbooks.json",
        CATALOG_DIR / "research_pipeline_stages.json",
        CATALOG_DIR / "reviewer_allowlist.json",
        CATALOG_DIR / "routing_table.json",
        CATALOG_DIR / "settings.toml",
        CATALOG_DIR / "skill_catalog.json",
        CATALOG_DIR / "subagent_registry.json",
        CATALOG_DIR / "writing_quality_rules.json",
    ]
    required_schemas = [
        SCHEMAS_DIR / "agent_dispatch_card.schema.json",
        SCHEMAS_DIR / "multi_agent_harness_adapter.schema.json",
        SCHEMAS_DIR / "project_agent_definition.schema.json",
    ]

    for group in (required_root, required_docs, required_assets, required_scripts, required_catalog, required_schemas):
        for path in group:
            if not path.exists():
                errors.append(f"missing-required-file:{path.relative_to(REPO_ROOT).as_posix()}")

    plugin_manifest_path = PLUGIN_DIR / ".codex-plugin" / "plugin.json"
    if plugin_manifest_path.exists():
        plugin = read_json(plugin_manifest_path)
        bad_values = json.dumps(plugin, ensure_ascii=False)
        forbidden_patterns = {
            "placeholder-local-host": r"example\.local",
            "placeholder-local-email": r"local-user@example\.com",
        }
        for label, pattern in forbidden_patterns.items():
            if re.search(pattern, bad_values):
                errors.append(f"plugin-manifest-contains-forbidden-value:{label}")
        if re.search(r"[A-Za-z]:\\\\Users\\\\", bad_values):
            errors.append("plugin-manifest-contains-local-user-path")
        homepage = str(plugin.get("homepage", ""))
        if not (homepage.startswith("https://github.com/") or homepage.startswith("https://") and "github.io" in homepage):
            errors.append("plugin-manifest-homepage-not-public")
        if not str(plugin.get("repository", "")).startswith("https://github.com/"):
            errors.append("plugin-manifest-repository-not-github")

    catalog = read_json(CATALOG_DIR / "skill_catalog.json")
    routing_table = read_json(CATALOG_DIR / "routing_table.json")
    metadata_report = collect_catalog_metadata(catalog, routing_table)
    for values in metadata_report.values():
        if values:
            errors.extend([f"catalog-metadata:{value}" for value in values])

    pipeline_errors, pipeline_warnings, _ = validate_pipeline_static()
    errors.extend([f"pipeline:{value}" for value in pipeline_errors])
    warnings.extend([f"pipeline:{value}" for value in pipeline_warnings])

    codex_runtime = {
        "codex_home": str(CODEX_HOME),
        "config_exists": CODEX_CONFIG_PATH.exists(),
        "skills_dir_exists": CODEX_SKILLS_DIR.exists(),
    }

    payload = {
        "ok": not errors,
        "repo_root": str(REPO_ROOT),
        "skills_root": str(SKILLS_ROOT),
        "codex_runtime": codex_runtime,
        "errors": errors,
        "warnings": warnings,
        "catalog_metadata": metadata_report,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
