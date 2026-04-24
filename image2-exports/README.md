# Image2 Exports

Put generated image2 files here before importing them into the public asset folders.

Expected filenames:

- `social-preview.png`
- `hero-overview.png`
- `multi-agent-workspace.png`
- `pipeline-gates-overview.png`
- `route-explanation-card.png`
- `multi-agent-dispatch-flow.png`
- `integration-chain.png`

`social-preview.png` is imported into both `assets/` and `docs/assets/` so README and Pages use the same approved overview image.

Run from the repository root:

```powershell
python .\scripts\import_image2_assets.py
```
