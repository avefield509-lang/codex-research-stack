from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

try:
    from public_release_env import CATALOG_DIR, SKILLS_ROOT
except ModuleNotFoundError:
    from scripts.public_release_env import CATALOG_DIR, SKILLS_ROOT

ROOT = SKILLS_ROOT
CATALOG = CATALOG_DIR


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def validate_static() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []

    routing = load_json(CATALOG / "routing_table.json")
    stages_payload = load_json(CATALOG / "research_pipeline_stages.json")
    gates_payload = load_json(CATALOG / "quality_gates.json")
    access_payload = load_json(CATALOG / "data_access_matrix.json")
    writing_rules_payload = load_json(CATALOG / "writing_quality_rules.json")

    route_ids = {route["id"] for route in routing.get("routes", [])}

    stages = stages_payload.get("stages", [])
    stage_ids = [stage["id"] for stage in stages]
    if len(stage_ids) != len(set(stage_ids)):
        errors.append("duplicate-stage-id")

    orders = [stage["order"] for stage in stages]
    if orders != sorted(orders):
        errors.append("stage-orders-must-be-sorted")

    gate_items = gates_payload.get("gates", [])
    gate_ids = [gate["id"] for gate in gate_items]
    if len(gate_ids) != len(set(gate_ids)):
        errors.append("duplicate-gate-id")

    stage_id_set = set(stage_ids)
    gate_id_set = set(gate_ids)

    for gate in gate_items:
        unknown_stages = set(gate.get("stage_ids", [])) - stage_id_set
        unknown_routes = set(gate.get("route_ids", [])) - route_ids
        if unknown_stages:
            errors.append(f"gate:{gate['id']}:unknown-stage-ids:{sorted(unknown_stages)}")
        if unknown_routes:
            errors.append(f"gate:{gate['id']}:unknown-route-ids:{sorted(unknown_routes)}")

    writing_report_path = writing_rules_payload.get("report_path")
    writing_checks = writing_rules_payload.get("checks", [])
    writing_check_ids = [item.get("id") for item in writing_checks]
    if not writing_report_path:
        errors.append("writing-quality-rules-missing-report-path")
    if not writing_checks:
        errors.append("writing-quality-rules-missing-checks")
    if len(writing_check_ids) != len(set(writing_check_ids)):
        errors.append("writing-quality-rules-duplicate-check-id")
    if not isinstance(writing_rules_payload.get("banned_phrases", []), list) or not writing_rules_payload.get("banned_phrases", []):
        errors.append("writing-quality-rules-missing-banned-phrases")

    route_focus = writing_rules_payload.get("route_focus", {})
    unknown_focus_routes = set(route_focus) - route_ids
    if unknown_focus_routes:
        errors.append(f"writing-quality-rules-unknown-route-focus:{sorted(unknown_focus_routes)}")
    for route_id, focus in route_focus.items():
        unknown_checks = set(focus.get("required_checks", [])) - set(writing_check_ids)
        if unknown_checks:
            errors.append(f"writing-quality-rules:{route_id}:unknown-required-checks:{sorted(unknown_checks)}")

    writing_gate = next((gate for gate in gate_items if gate.get("id") == "writing_quality_checked"), None)
    if writing_gate is None:
        errors.append("missing-writing-quality-gate")
    else:
        if writing_gate.get("required_report") != writing_report_path:
            errors.append("writing-quality-gate-report-path-mismatch")
        if set(writing_gate.get("required_checks", [])) != set(writing_check_ids):
            errors.append("writing-quality-gate-checks-mismatch")
        if writing_gate.get("helper_rules") != "catalog/writing_quality_rules.json":
            errors.append("writing-quality-gate-helper-rules-mismatch")

    required_stage_gates = stages_payload.get("required_stage_gates", {})
    if set(required_stage_gates) != stage_id_set:
        missing = sorted(stage_id_set - set(required_stage_gates))
        extra = sorted(set(required_stage_gates) - stage_id_set)
        if missing:
            errors.append(f"required-stage-gates-missing-stages:{missing}")
        if extra:
            errors.append(f"required-stage-gates-extra-stages:{extra}")

    for stage_id, gates in required_stage_gates.items():
        unknown_gates = set(gates) - gate_id_set
        if unknown_gates:
            errors.append(f"stage:{stage_id}:unknown-required-gates:{sorted(unknown_gates)}")

    route_stage_sequences = stages_payload.get("route_stage_sequences", {})
    if set(route_stage_sequences) != route_ids:
        missing = sorted(route_ids - set(route_stage_sequences))
        extra = sorted(set(route_stage_sequences) - route_ids)
        if missing:
            errors.append(f"route-stage-sequences-missing-routes:{missing}")
        if extra:
            errors.append(f"route-stage-sequences-extra-routes:{extra}")

    for route_id, sequence in route_stage_sequences.items():
        if not sequence:
            errors.append(f"route:{route_id}:empty-stage-sequence")
            continue
        unknown_stages = set(sequence) - stage_id_set
        if unknown_stages:
            errors.append(f"route:{route_id}:unknown-stages:{sorted(unknown_stages)}")
        sequence_orders = [next(stage["order"] for stage in stages if stage["id"] == stage_id) for stage_id in sequence if stage_id in stage_id_set]
        if sequence_orders != sorted(sequence_orders):
            errors.append(f"route:{route_id}:stage-order-not-monotonic")

    route_stage_gate_overrides = stages_payload.get("route_stage_gate_overrides", {})
    unknown_override_routes = set(route_stage_gate_overrides) - route_ids
    if unknown_override_routes:
        errors.append(f"route-stage-gate-overrides-unknown-routes:{sorted(unknown_override_routes)}")

    for route_id, stage_map in route_stage_gate_overrides.items():
        sequence = set(route_stage_sequences.get(route_id, []))
        for stage_id, gates in stage_map.items():
            if stage_id not in sequence:
                errors.append(f"route:{route_id}:override-stage-not-in-sequence:{stage_id}")
            unknown_gates = set(gates) - gate_id_set
            if unknown_gates:
                errors.append(f"route:{route_id}:override-stage:{stage_id}:unknown-gates:{sorted(unknown_gates)}")

    access_levels = access_payload.get("levels", [])
    level_ids = [item["id"] for item in access_levels]
    if len(level_ids) != len(set(level_ids)):
        errors.append("duplicate-data-access-level-id")
    level_id_set = set(level_ids)

    route_defaults = access_payload.get("route_defaults", {})
    if set(route_defaults) != route_ids:
        missing = sorted(route_ids - set(route_defaults))
        extra = sorted(set(route_defaults) - route_ids)
        if missing:
            errors.append(f"data-access-route-defaults-missing-routes:{missing}")
        if extra:
            errors.append(f"data-access-route-defaults-extra-routes:{extra}")

    for route_id, policy in route_defaults.items():
        default_level = policy.get("default_level")
        allowed_levels = set(policy.get("allowed_levels", []))
        if default_level not in level_id_set:
            errors.append(f"route:{route_id}:unknown-default-level:{default_level}")
        if default_level not in allowed_levels:
            errors.append(f"route:{route_id}:default-level-not-in-allowed-levels")
        unknown_levels = allowed_levels - level_id_set
        if unknown_levels:
            errors.append(f"route:{route_id}:unknown-allowed-levels:{sorted(unknown_levels)}")
        unknown_gates = set(policy.get("required_gates", [])) - gate_id_set
        if unknown_gates:
            errors.append(f"route:{route_id}:unknown-required-gates:{sorted(unknown_gates)}")

    payload = {
        "routing": routing,
        "stages": stages_payload,
        "gates": gates_payload,
        "access": access_payload,
        "writing_rules": writing_rules_payload,
    }
    return errors, warnings, payload


def required_gates_for_stage(payload: dict, route_id: str, stage_id: str) -> list[str]:
    base = list(payload["stages"].get("required_stage_gates", {}).get(stage_id, []))
    override = payload["stages"].get("route_stage_gate_overrides", {}).get(route_id, {}).get(stage_id, [])
    result: list[str] = []
    for gate_id in base + list(override):
        if gate_id not in result:
            result.append(gate_id)
    return result


def validate_project(project_root: Path, payload: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    research_map_path = project_root / "research-map.md"
    material_passport_path = project_root / "material-passport.yaml"
    evidence_ledger_path = project_root / "evidence-ledger.yaml"
    pipeline_status_path = project_root / "logs" / "quality-gates" / "pipeline-status.json"
    writing_quality_report_path = project_root / Path(payload["writing_rules"].get("report_path", "logs/quality-gates/writing-quality-report.json"))
    project_state_current_path = project_root / "logs" / "project-state" / "current.json"
    project_state_history_path = project_root / "logs" / "project-state" / "history.md"

    for required in (research_map_path, material_passport_path, evidence_ledger_path, pipeline_status_path):
        if not required.exists():
            errors.append(f"missing-project-pipeline-file:{required}")

    if not project_state_current_path.exists():
        warnings.append(f"missing-project-state-file:{project_state_current_path}")
    if not project_state_history_path.exists():
        warnings.append(f"missing-project-state-history:{project_state_history_path}")

    material_passport = load_yaml(material_passport_path) if material_passport_path.exists() else {}
    pipeline_status = load_json(pipeline_status_path) if pipeline_status_path.exists() else {}
    writing_quality_report = load_json(writing_quality_report_path) if writing_quality_report_path.exists() else {}
    project_state = load_json(project_state_current_path) if project_state_current_path.exists() else {}

    route_sequences = payload["stages"]["route_stage_sequences"]
    route_policies = payload["access"]["route_defaults"]
    allowed_decisions = set(payload["gates"]["allowed_decisions"])
    valid_gate_ids = {gate["id"] for gate in payload["gates"]["gates"]}
    valid_level_ids = {level["id"] for level in payload["access"]["levels"]}
    valid_writing_check_ids = {
        item["id"] for item in payload["writing_rules"].get("checks", [])
        if isinstance(item, dict) and item.get("id")
    }

    route_id = material_passport.get("route_id") or pipeline_status.get("route_id")
    current_stage = material_passport.get("current_stage") or pipeline_status.get("current_stage")
    data_access_level = material_passport.get("data_access_level")
    completed_stages = pipeline_status.get("completed_stages", []) or []
    gate_decisions = pipeline_status.get("gate_decisions", {}) or {}
    allowed_to_advance = bool(pipeline_status.get("allowed_to_advance", False))

    if route_id is None:
        warnings.append("project-route-id-not-set")
    elif route_id not in route_sequences:
        errors.append(f"unknown-project-route-id:{route_id}")

    if current_stage is None:
        errors.append("project-current-stage-not-set")
    elif current_stage not in {stage["id"] for stage in payload["stages"]["stages"]}:
        errors.append(f"unknown-project-current-stage:{current_stage}")

    if data_access_level is None:
        warnings.append("project-data-access-level-not-set")
    elif data_access_level not in valid_level_ids:
        errors.append(f"unknown-project-data-access-level:{data_access_level}")

    if route_id in route_policies and data_access_level is not None:
        allowed_levels = set(route_policies[route_id]["allowed_levels"])
        if data_access_level not in allowed_levels:
            errors.append(f"route:{route_id}:data-access-level-not-allowed:{data_access_level}")

    if project_state:
        if project_state.get("route_id") != route_id:
            warnings.append("project-state-route-id-differs-from-passport-or-pipeline-status")
        if project_state.get("pipeline_stage") != current_stage:
            warnings.append("project-state-pipeline-stage-differs-from-passport-or-pipeline-status")
        if not isinstance(project_state.get("blockers", []), list):
            errors.append("project-state-blockers-must-be-list")
        if not isinstance(project_state.get("milestones", []), list):
            errors.append("project-state-milestones-must-be-list")
        if not project_state.get("current_owner_agent_id"):
            warnings.append("project-state-current-owner-not-set")

    if route_id in route_sequences and current_stage in route_sequences[route_id]:
        sequence = route_sequences[route_id]
        current_index = sequence.index(current_stage)
        previous_stages = sequence[:current_index]
        missing_previous = [stage_id for stage_id in previous_stages if stage_id not in completed_stages]
        if missing_previous:
            errors.append(f"project-stage-skip-detected:{missing_previous}")
        invalid_completed = [stage_id for stage_id in completed_stages if stage_id not in sequence]
        if invalid_completed:
            errors.append(f"project-completed-stages-not-in-route-sequence:{invalid_completed}")

    for gate_id, decision in gate_decisions.items():
        if gate_id not in valid_gate_ids:
            errors.append(f"unknown-project-gate-id:{gate_id}")
        if decision not in allowed_decisions:
            errors.append(f"invalid-project-gate-decision:{gate_id}:{decision}")

    if route_id in route_sequences:
        for stage_id in completed_stages:
            for gate_id in required_gates_for_stage(payload, route_id, stage_id):
                if gate_decisions.get(gate_id) != "pass":
                    errors.append(f"completed-stage-missing-pass-gate:{stage_id}:{gate_id}")
        if current_stage in route_sequences[route_id] and allowed_to_advance:
            for gate_id in required_gates_for_stage(payload, route_id, current_stage):
                if gate_decisions.get(gate_id) != "pass":
                    errors.append(f"current-stage-cannot-advance:{current_stage}:{gate_id}")

    writing_quality_required = False
    if route_id in route_sequences:
        writing_stages = [stage_id for stage_id in completed_stages if "writing_quality_checked" in required_gates_for_stage(payload, route_id, stage_id)]
        if current_stage and "writing_quality_checked" in required_gates_for_stage(payload, route_id, current_stage):
            writing_stages.append(current_stage)
        writing_quality_required = bool(writing_stages)

    if gate_decisions.get("writing_quality_checked") == "pass" or writing_quality_required:
        if not writing_quality_report_path.exists():
            errors.append(f"missing-writing-quality-report:{writing_quality_report_path}")
        else:
            report_status = writing_quality_report.get("status")
            if report_status not in allowed_decisions:
                errors.append("writing-quality-report-invalid-status")
            checks_payload = writing_quality_report.get("checks", {})
            if not isinstance(checks_payload, dict):
                errors.append("writing-quality-report-checks-must-be-object")
                checks_payload = {}
            missing_checks = sorted(valid_writing_check_ids - set(checks_payload))
            if missing_checks:
                errors.append(f"writing-quality-report-missing-checks:{missing_checks}")
            for check_id in set(checks_payload) & valid_writing_check_ids:
                check_payload = checks_payload.get(check_id, {})
                if not isinstance(check_payload, dict):
                    errors.append(f"writing-quality-report-check-not-object:{check_id}")
                    continue
                if check_payload.get("decision") not in allowed_decisions:
                    errors.append(f"writing-quality-report-invalid-decision:{check_id}")
            if gate_decisions.get("writing_quality_checked") == "pass":
                if report_status != "pass":
                    errors.append("writing-quality-gate-pass-without-pass-report")
                for check_id in valid_writing_check_ids:
                    decision = checks_payload.get(check_id, {}).get("decision")
                    if decision != "pass":
                        errors.append(f"writing-quality-pass-missing-check-pass:{check_id}")
                empty_phrase_hits = checks_payload.get("empty_phrase_scan", {}).get("hits", [])
                if empty_phrase_hits:
                    errors.append("writing-quality-pass-has-empty-phrase-hits")

    truth_sources = material_passport.get("truth_sources", []) or []
    if truth_sources and len(set(truth_sources)) != len(truth_sources):
        warnings.append("material-passport-truth-sources-contains-duplicates")

    return errors, warnings


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path)
    args = parser.parse_args()

    static_errors, static_warnings, payload = validate_static()
    project_errors: list[str] = []
    project_warnings: list[str] = []

    if args.project_root:
        project_errors, project_warnings = validate_project(args.project_root, payload)

    report = {
        "ok": not (static_errors or project_errors),
        "static_errors": static_errors,
        "static_warnings": static_warnings,
        "project_errors": project_errors,
        "project_warnings": project_warnings,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if static_errors or project_errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
