# Image2 Exports

Put generated image2 files here before importing them into the public asset folders.

Expected filenames:

- `social-preview.png`
- `workflow-map.png`
- `research-system-overview.png`
- `research-team-workspace.png`

`social-preview.png` is imported into both `assets/` and `docs/assets/` for the README and GitHub social preview.
`workflow-map.png` is imported into both `assets/` and `docs/assets/` for README and Pages workflow explanations.
`research-system-overview.png` and `research-team-workspace.png` are imported into `docs/assets/` and the Research Autopilot plugin screenshot folder.

Run from the repository root:

```powershell
python .\scripts\import_image2_assets.py
```
