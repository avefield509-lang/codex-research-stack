from __future__ import annotations

import json
import re
import sys
from pathlib import Path, PurePosixPath

try:
    from public_release_env import CATALOG_DIR, SKILLS_ROOT
except ModuleNotFoundError:
    from scripts.public_release_env import CATALOG_DIR, SKILLS_ROOT

ROOT = SKILLS_ROOT
CATALOG = CATALOG_DIR
ISOLATION_RANKS = {
    "shared_thread_context": 0,
    "project_file_context": 1,
    "isolated_subagent_context": 2,
    "isolated_worktree_context": 3,
}
CAPABILITY_TAGS = {
    "project_coordination",
    "milestone_tracking",
    "stack_governance",
    "retrospective_coordination",
    "literature_discovery",
    "citation_verification",
    "zotero_sync",
    "evidence_synthesis",
    "browser_visible_capture",
    "social_evidence_extraction",
    "text_preprocessing",
    "network_seed_extraction",
    "quant_analysis",
    "text_analysis",
    "network_analysis",
    "simulation",
    "reproducibility",
    "writing_export",
    "revision_response",
    "reference_capture",
    "submission_packaging",
    "review_gate",
    "citation_audit",
    "writing_quality_audit",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_template_path(path_value: str, *, allow_target: bool) -> str:
    if not isinstance(path_value, str) or not path_value.strip():
        raise ValueError("path-template-empty")
    if "\\" in path_value:
        raise ValueError("path-template-backslash")
    if path_value.startswith("/") or re.match(r"^[A-Za-z]:", path_value):
        raise ValueError("path-template-absolute")
    variables = set(re.findall(r"<[^>]+>", path_value))
    allowed = {"<run_id>", "<agent_id>"}
    if allow_target:
        allowed.add("<target_agent_id>")
    unknown = variables - allowed
    if unknown:
        raise ValueError(f"path-template-unknown-vars:{sorted(unknown)}")
    if "<target_agent_id>" in variables and not allow_target:
        raise ValueError("path-template-target-var-not-allowed")
    normalized = str(
        PurePosixPath(
            path_value.replace("<run_id>", "RUN")
            .replace("<agent_id>", "AGENT")
            .replace("<target_agent_id>", "TARGET")
        )
    )
    if normalized == "." or normalized.startswith("../") or "/../" in normalized:
        raise ValueError("path-template-parent-reference")
    return path_value


def main() -> None:
    scope_rules = load_json(CATALOG / "project_scope_rules.json")
    mode_catalog = load_json(CATALOG / "agent_execution_modes.json")
    registry = load_json(CATALOG / "subagent_registry.json")
    reviewer_allowlist = load_json(CATALOG / "reviewer_allowlist.json")

    deliverable_types = set(scope_rules["enums"]["deliverable_types"])
    review_subset = set(scope_rules["enums"]["required_review_for"])
    modes = mode_catalog["modes"]
    reviewer_allowed = set(reviewer_allowlist["allowed_skills_mcp"])

    errors: list[str] = []
    warnings: list[str] = []
    seen_ids: set[str] = set()

    agents = registry.get("agents", [])
    if not isinstance(agents, list) or not agents:
        errors.append("subagent_registry.json: agents must be a non-empty list")

    for item in agents:
        agent_id = item.get("agent_id")
        if not agent_id or not isinstance(agent_id, str):
            errors.append(f"registry-entry-invalid-agent-id:{item!r}")
            continue
        if agent_id in seen_ids:
            errors.append(f"registry-duplicate-agent-id:{agent_id}")
        seen_ids.add(agent_id)

        role = item.get("role")
        if not isinstance(role, str) or not role:
            errors.append(f"{agent_id}: missing role")

        display_name = item.get("display_name")
        if not isinstance(display_name, str) or not display_name.strip():
            errors.append(f"{agent_id}: missing display_name")

        preferred_model = item.get("preferred_model")
        if preferred_model is not None and (not isinstance(preferred_model, str) or not preferred_model.strip()):
            errors.append(f"{agent_id}: preferred_model must be a non-empty string or null")

        isolation_method = item.get("isolation_method")
        if isolation_method not in ISOLATION_RANKS:
            errors.append(f"{agent_id}: invalid isolation_method '{isolation_method}'")

        parallel_safe = item.get("parallel_safe")
        if not isinstance(parallel_safe, bool):
            errors.append(f"{agent_id}: parallel_safe must be boolean")

        integration_review_required = item.get("integration_review_required")
        if not isinstance(integration_review_required, bool):
            errors.append(f"{agent_id}: integration_review_required must be boolean")

        capability_tags = item.get("capability_tags")
        if not isinstance(capability_tags, list) or any(not isinstance(x, str) or not x for x in capability_tags):
            errors.append(f"{agent_id}: capability_tags must be a non-empty string list")
            capability_tags = []
        else:
            unknown_tags = set(capability_tags) - CAPABILITY_TAGS
            if unknown_tags:
                errors.append(f"{agent_id}: capability_tags contains invalid values {sorted(unknown_tags)}")

        allowed_skills = item.get("allowed_skills_mcp")
        if not isinstance(allowed_skills, list) or any(not isinstance(x, str) or not x for x in allowed_skills):
            errors.append(f"{agent_id}: allowed_skills_mcp must be a non-empty string list")

        write_scope = item.get("write_scope")
        if not isinstance(write_scope, list) or any(not isinstance(x, str) or not x for x in write_scope):
            errors.append(f"{agent_id}: write_scope must be a string list")
        else:
            for path_value in write_scope:
                try:
                    normalize_template_path(path_value, allow_target=False)
                except ValueError as exc:
                    errors.append(f"{agent_id}: invalid write_scope '{path_value}': {exc}")

        max_execution_mode = item.get("max_execution_mode")
        if max_execution_mode not in modes:
            errors.append(f"{agent_id}: invalid max_execution_mode '{max_execution_mode}'")

        required_review_for = item.get("required_review_for")
        if not isinstance(required_review_for, list) or any(not isinstance(x, str) for x in required_review_for):
            errors.append(f"{agent_id}: required_review_for must be a string list")
        else:
            unknown_review_types = set(required_review_for) - review_subset
            if unknown_review_types:
                errors.append(f"{agent_id}: required_review_for contains invalid values {sorted(unknown_review_types)}")
            if set(required_review_for) - deliverable_types:
                errors.append(f"{agent_id}: required_review_for must also be in deliverable_types")

        if max_execution_mode == "parallel_multi_agent_execution" and parallel_safe is not True:
            errors.append(f"{agent_id}: parallel_multi_agent_execution requires parallel_safe=true")

        if role == "reviewer":
            if set(allowed_skills or []) - reviewer_allowed:
                errors.append(f"{agent_id}: reviewer includes disallowed capabilities")
            if write_scope != ["outputs/agent-runs/<run_id>/<agent_id>/"]:
                errors.append(f"{agent_id}: reviewer write_scope must equal outputs/agent-runs/<run_id>/<agent_id>/")
            if max_execution_mode in modes and modes[max_execution_mode]["rank"] > modes["sequential_multi_agent_execution"]["rank"]:
                errors.append(f"{agent_id}: reviewer max_execution_mode cannot exceed sequential_multi_agent_execution")
            if isolation_method in ISOLATION_RANKS and ISOLATION_RANKS[isolation_method] < ISOLATION_RANKS["isolated_subagent_context"]:
                errors.append(f"{agent_id}: reviewer isolation_method must be at least isolated_subagent_context")
            if parallel_safe:
                warnings.append(f"{agent_id}: reviewer parallel_safe is usually expected to be false")
            if integration_review_required:
                warnings.append(f"{agent_id}: reviewer integration_review_required is usually expected to be false")
            if required_review_for:
                warnings.append(f"{agent_id}: reviewer required_review_for is usually expected to be empty")

    payload = {
        "ok": not errors,
        "registry_entries": len(agents),
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
