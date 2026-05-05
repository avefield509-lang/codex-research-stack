from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

try:
    from public_release_env import CATALOG_DIR, DOCS_DIR, PLUGIN_DIR, PROFILES_DIR, REPO_ROOT, SCHEMAS_DIR, SCRIPTS_DIR
except ModuleNotFoundError:
    from scripts.public_release_env import CATALOG_DIR, DOCS_DIR, PLUGIN_DIR, PROFILES_DIR, REPO_ROOT, SCHEMAS_DIR, SCRIPTS_DIR
from validate_research_stack import collect_catalog_metadata, read_json


def list_markdown(path: Path) -> list[str]:
    if not path.exists():
        return []
    return sorted(item.relative_to(REPO_ROOT).as_posix() for item in path.rglob("*.md"))


def list_profiles() -> list[str]:
    return sorted(path.stem for path in PROFILES_DIR.glob("*.toml"))


def contract_assets() -> dict[str, bool]:
    return {
        "root_agents": (REPO_ROOT / "skills" / "AGENTS.md").exists(),
        "project_scope_rules": (CATALOG_DIR / "project_scope_rules.json").exists(),
        "agent_execution_modes": (CATALOG_DIR / "agent_execution_modes.json").exists(),
        "subagent_registry": (CATALOG_DIR / "subagent_registry.json").exists(),
        "research_team_playbooks": (CATALOG_DIR / "research_team_playbooks.json").exists(),
        "reviewer_allowlist": (CATALOG_DIR / "reviewer_allowlist.json").exists(),
        "quality_gates": (CATALOG_DIR / "quality_gates.json").exists(),
        "research_pipeline_stages": (CATALOG_DIR / "research_pipeline_stages.json").exists(),
        "data_access_matrix": (CATALOG_DIR / "data_access_matrix.json").exists(),
        "writing_quality_rules": (CATALOG_DIR / "writing_quality_rules.json").exists(),
        "dispatch_schema": (SCHEMAS_DIR / "agent_dispatch_card.schema.json").exists(),
        "project_agent_schema": (SCHEMAS_DIR / "project_agent_definition.schema.json").exists(),
        "harness_adapter_schema": (SCHEMAS_DIR / "multi_agent_harness_adapter.schema.json").exists(),
        "plugin_manifest": (PLUGIN_DIR / ".codex-plugin" / "plugin.json").exists(),
        "sync_script": (SCRIPTS_DIR / "sync_research_autopilot_skills.ps1").exists(),
    }


def render_markdown(payload: dict) -> str:
    lines = [
        "# VELA Scan Report",
        "",
        f"- Generated at: {payload['generated_at']}",
        f"- Repository root: `{payload['repo_root']}`",
        "",
        "## Profiles",
        "",
    ]
    for name in payload["profiles"]:
        lines.append(f"- `{name}`")

    lines.extend(["", "## Contract Assets", ""])
    for key, exists in payload["contract_assets"].items():
        lines.append(f"- `{key}`: `{'ok' if exists else 'missing'}`")

    lines.extend(["", "## Docs", ""])
    for item in payload["docs"]:
        lines.append(f"- `{item}`")

    lines.extend(["", "## Catalog Metadata", ""])
    for key, values in payload["catalog_metadata"].items():
        lines.append(f"### {key}")
        if not values:
            lines.append("- none")
        else:
            for value in values:
                lines.append(f"- `{value}`")
        lines.append("")

    lines.extend(["", "## Release Checklist", ""])
    for item in payload["release_checklist"]:
        lines.append(f"- {item}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    catalog = read_json(CATALOG_DIR / "skill_catalog.json")
    routing_table = read_json(CATALOG_DIR / "routing_table.json")
    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "repo_root": str(REPO_ROOT),
        "profiles": list_profiles(),
        "docs": list_markdown(DOCS_DIR),
        "contract_assets": contract_assets(),
        "catalog_metadata": collect_catalog_metadata(catalog, routing_table),
        "release_checklist": [
            "README 与 docs 首页需在 3 分钟内解释清楚项目定位、适用人群和起步方式。",
            "公开版不得包含本机绝对路径、私有 SSH 密钥、云端运维日志和个人专用文档。",
            "plugin manifest 只能指向公开 GitHub 仓库与 GitHub Pages。",
            "脚本默认应使用仓库相对路径或环境变量，而不是作者本机路径。",
            "发布前需要通过 validate_agents_contract、validate_research_pipeline、validate_research_stack。",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_markdown(payload), encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
