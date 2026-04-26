# Image2 Visual Generation Pack

This pack defines the replacement image system for Codex Research Stack.

The Pages homepage now uses separate image2 assets for brand presentation and workflow explanation, with native HTML/CSS cards as fallback visuals. Future image2 replacements should stay readable at GitHub width, usable on Pages, and visually distinct from the surrounding dark cards.

## Global Direction

- Product: `Codex Research Stack`
- Visual tone: serious research workbench, not cyberpunk, not generic SaaS dashboard.
- Background: warm off-white or translucent light panels preferred for README visuals; dark variants only when the image is not placed inside another dark card.
- Palette: deep teal, muted cyan, warm amber, off-white, graphite.
- Typography in image: minimal. Use large short labels only. Avoid paragraphs inside the image.
- Composition: strong hierarchy, grounded panels, generous margins, no floating sticker effect.
- Prohibited: tiny UI text, fake star counts, fake metrics, fake GitHub badges, real personal data, real paths, API keys, screenshots of private tools.

## Required Assets

| Asset | Output path | Size | Purpose |
| --- | --- | ---: | --- |
| GitHub social preview | `assets/social-preview.png` and `docs/assets/social-preview.png` | `16:9` or `2:1`, ideally `1600px` wide or larger | README top image and social sharing |
| Workflow map | `assets/workflow-map.png` and `docs/assets/workflow-map.png` | `16:9`, ideally `1600x900` or larger | README and Pages workflow explanation |
| Research system overview | `docs/assets/research-system-overview.png` and `skills/plugins/research-autopilot/assets/research-system-overview.png` | `16:9`, ideally `1600x900` or larger | Pages product direction and plugin screenshot |
| Research team workspace | `docs/assets/research-team-workspace.png` and `skills/plugins/research-autopilot/assets/research-team-workspace.png` | `16:9`, ideally `1600x900` or larger | Pages product direction and plugin screenshot |

For README, copy only the social preview and at most one large explanatory image into `assets/`. Do not duplicate every Pages image in `assets/` unless README references it.

The current `social-preview.png` is the brand reference image: project name, tagline, multi-agent research framing, and a polished high-level product mood.
The current `workflow-map.png` is the workflow reference image: research routing, multi-agent orchestration, quality gates, citation verification, Zotero/Obsidian sync, social evidence capture, and evidence-to-writing handoff.
New assets should simplify these directions rather than returning to small text-heavy screenshot cards.

## Prompt 1: GitHub Social Preview

Create a polished GitHub repository social preview image for an open-source project named "Codex Research Stack".

Design brief:
- 1280x640 landscape.
- Product-grade, elegant, academic research workbench aesthetic.
- Light-on-dark or light-panel-on-dark composition, but not cyberpunk.
- Large readable title: "Codex Research Stack".
- Subtitle: "Readable research projects in Codex".
- Show three simple visual ideas only: route first, multi-agent ready, review gates.
- Use a grounded layout with one large title block and one clean product diagram block.
- No fake metrics, no star counts, no usernames, no personal data.
- No tiny text. Every label must be readable at GitHub preview size.
- Colors: deep teal, muted cyan, warm amber, off-white, graphite.

## Prompt 2: Workflow Map

Create a polished workflow map illustration for "Codex Research Stack".

Design brief:
- 16:9 landscape, ideally 1600x900 or larger.
- Show the research workflow as connected panels, not as a literal screenshot.
- Required panels: Research routing, Multi-agent orchestration, Quality gates, Citation verification, Zotero and Obsidian sync, Social evidence capture, Evidence to writing.
- Use short readable labels only.
- Keep the composition grounded with visible connection lines and generous spacing.
- Colors: deep teal, muted cyan, warm amber, off-white, graphite.
- No fake star counts, fake metrics, personal data, API keys, or unreadable tiny paragraphs.

## Prompt 3: Research System Overview

Create a polished product overview illustration for "Codex Research Stack".

Design brief:
- 16:9 landscape, ideally 1600x900 or larger.
- Show the system as one readable research workbench, not a literal screenshot.
- Required ideas: route planning, evidence capture, citation verification, writing, reproducibility, knowledge sync.
- Use large short labels only.
- Avoid fake metrics, fake screenshots, real user data, and tiny text.

## Prompt 4: Research Team Workspace

Create a polished product illustration showing a multi-agent research workspace.

Design brief:
- 16:9 landscape, ideally 1600x900 or larger.
- Show a readable board with zones for project state, agent roles, reviewer gate, handoff log, active dispatches, sources, and outputs.
- The layout should look like a real organized workbench.
- Use large short labels only.
- No text should touch card borders.
- Avoid long sentences, tiny labels, floating panels, and decorative clutter.
- Use light panels or high-contrast surfaces so it does not disappear inside a dark webpage card.

## Import Rule

Place generated files in:

```text
image2-exports/
```

Then run:

```powershell
python .\scripts\import_image2_assets.py
```

The script copies approved files into public asset paths.
