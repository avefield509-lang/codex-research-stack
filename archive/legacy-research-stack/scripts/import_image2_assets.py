from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "image2-exports"

ASSETS = {
    "vela-workflow-mark.png": [ROOT / "docs" / "assets" / "brand" / "vela-workflow-mark.png"],
    "vela-brand-board-reference.png": [ROOT / "docs" / "assets" / "brand" / "vela-brand-board-reference.png"],
    "vela-helm-relationship-board-reference.png": [
        ROOT / "docs" / "assets" / "brand" / "vela-helm-relationship-board-reference.png",
    ],
    "vela-helm-design-language-reference.png": [
        ROOT / "docs" / "assets" / "brand" / "vela-helm-design-language-reference.png",
    ],
    "helm-local-board-icon-master.png": [ROOT / "docs" / "assets" / "brand" / "helm-local-board-icon-master.png"],
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
