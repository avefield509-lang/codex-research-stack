from __future__ import annotations

import os
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
CATALOG_DIR = SKILLS_ROOT / "catalog"
SCHEMAS_DIR = SKILLS_ROOT / "schemas"
PROFILES_DIR = SKILLS_ROOT / "profiles"
TEMPLATES_DIR = SKILLS_ROOT / "templates"
PLUGIN_DIR = SKILLS_ROOT / "plugins" / "research-autopilot"
PLUGIN_SKILLS_DIR = PLUGIN_DIR / "skills"
DOCS_DIR = REPO_ROOT / "docs"
ASSETS_DIR = REPO_ROOT / "assets"
EXAMPLES_DIR = REPO_ROOT / "examples"
SCRIPTS_DIR = REPO_ROOT / "scripts"

CODEX_HOME = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))).expanduser()
CODEX_SKILLS_DIR = CODEX_HOME / "skills"
CODEX_CONFIG_PATH = CODEX_HOME / "config.toml"
AGENTS_HOME = Path(os.environ.get("AGENTS_HOME", str(Path.home() / ".agents"))).expanduser()
HOME_MARKETPLACE = AGENTS_HOME / "plugins" / "marketplace.json"

ARTIFACTS_DIR = REPO_ROOT / "artifacts"
DOWNLOADS_DIR = ARTIFACTS_DIR / "downloads"
REPORTS_DIR = SKILLS_ROOT / "outputs" / "reports"


def repo_relative(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
