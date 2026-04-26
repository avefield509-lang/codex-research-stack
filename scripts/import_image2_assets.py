from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "image2-exports"

ASSETS = {
    "social-preview.png": [
        ROOT / "assets" / "social-preview.png",
        ROOT / "docs" / "assets" / "social-preview.png",
    ],
    "workflow-map.png": [
        ROOT / "assets" / "workflow-map.png",
        ROOT / "docs" / "assets" / "workflow-map.png",
    ],
    "research-system-overview.png": [
        ROOT / "docs" / "assets" / "research-system-overview.png",
        ROOT / "skills" / "plugins" / "research-autopilot" / "assets" / "research-system-overview.png",
    ],
    "research-team-workspace.png": [
        ROOT / "docs" / "assets" / "research-team-workspace.png",
        ROOT / "skills" / "plugins" / "research-autopilot" / "assets" / "research-team-workspace.png",
    ],
}


def main() -> int:
    missing: list[str] = []
    copied: list[str] = []

    for filename, targets in ASSETS.items():
        source = SOURCE / filename
        if not source.exists():
            missing.append(filename)
            continue

        for target in targets:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            copied.append(str(target.relative_to(ROOT)))

    print("copied:")
    for item in copied:
        print(f"  - {item}")

    if missing:
        print("missing:")
        for item in missing:
            print(f"  - {item}")

    return 0 if copied else 1


if __name__ == "__main__":
    raise SystemExit(main())
