from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "image2-exports"

ASSETS = {
    "social-preview.png": [ROOT / "assets" / "social-preview.png"],
    "hero-overview.png": [ROOT / "docs" / "assets" / "hero-overview.png"],
    "multi-agent-workspace.png": [ROOT / "docs" / "assets" / "multi-agent-workspace.png"],
    "pipeline-gates-overview.png": [ROOT / "docs" / "assets" / "pipeline-gates-overview.png"],
    "route-explanation-card.png": [ROOT / "docs" / "assets" / "route-explanation-card.png"],
    "multi-agent-dispatch-flow.png": [ROOT / "docs" / "assets" / "multi-agent-dispatch-flow.png"],
    "integration-chain.png": [ROOT / "docs" / "assets" / "integration-chain.png"],
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
