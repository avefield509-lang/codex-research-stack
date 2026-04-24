# Image2 Visual Generation Pack

This pack defines the replacement image system for Codex Research Stack.

The current public pages should not depend on small text-heavy screenshots. Use image2 assets as product-grade illustrations: readable at GitHub width, usable on Pages, and visually distinct from the surrounding dark cards.

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
| GitHub social preview | `assets/social-preview.png` | `1280x640` | README top image and social sharing |
| Pages hero visual | `docs/assets/hero-overview.png` | `1200x1200` | Homepage hero, desktop and mobile |
| Workspace visual | `docs/assets/multi-agent-workspace.png` | `1600x1000` | Pages project workspace section |
| Pipeline gates visual | `docs/assets/pipeline-gates-overview.png` | `1600x900` | Pages gate/check section |
| Route card visual | `docs/assets/route-explanation-card.png` | `1280x720` | Demo walkthrough card |
| Dispatch visual | `docs/assets/multi-agent-dispatch-flow.png` | `1280x720` | Demo walkthrough card |
| Integration visual | `docs/assets/integration-chain.png` | `1280x720` | Demo walkthrough card |

For README, copy only the social preview and at most one large explanatory image into `assets/`. Do not duplicate every Pages image in `assets/` unless README references it.

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

## Prompt 2: Pages Hero Visual

Create a square product illustration for "Codex Research Stack".

Design brief:
- 1200x1200 square.
- This image will sit inside a dark homepage hero panel, so use a lighter internal surface or clear contrast.
- Show a simple vertical workflow: "Explain route" -> "Dispatch roles" -> "Review gate".
- Use large labels only. No paragraphs.
- The design should feel anchored to a workbench, not like floating stickers.
- Include subtle project-file motifs: dispatch card, result JSON, gate JSON, handoff log.
- Avoid fake app chrome, fake browser windows, fake metrics, real user data, and tiny text.

## Prompt 3: Workspace Visual

Create a wide product illustration showing a research project workspace.

Design brief:
- 1600x1000.
- Show a readable board with four zones: Project State, Roles, Reviewer Gate, Handoff Status.
- The layout should look like a real organized workbench.
- Use large short labels: State, Literature, Evidence, Analysis, Writing, Reviewer Gate, Handoff.
- No text should touch card borders.
- Avoid long sentences, tiny labels, floating panels, and decorative clutter.
- Use light panels or high-contrast surfaces so it does not disappear inside a dark webpage card.

## Prompt 4: Pipeline Gates Visual

Create a wide product illustration for a research workflow gate system.

Design brief:
- 1600x900.
- Show five clear steps: Route, Dispatch, Produce, Review, Handoff.
- The Review step should use warm amber and feel like a blocking gate.
- Add four check chips: Citation, Evidence, Writing, Reproducibility.
- Make it highly readable at README width.
- Do not include paragraphs, fake metrics, screenshots, or small UI text.

## Prompt 5: Route Card Visual

Create a clean card-style illustration called "Route explanation".

Design brief:
- 1280x720.
- Show three large cards: Task, Path, Risk.
- Show one final strip: Next action.
- Text must be short and large:
  - Task: literature review
  - Path: discover + verify
  - Risk: unverified DOI
  - Next action: verify sources first
- Use a product illustration style, not a literal screenshot.
- Leave generous spacing.

## Prompt 6: Dispatch Visual

Create a clean card-style illustration called "Dispatch board".

Design brief:
- 1280x720.
- Show four equal-width cards: Producer, Reviewer, Outputs, State.
- Cards should be aligned on a shared grid.
- Use arrows between cards, not through text.
- Reviewer card uses warm amber; other cards use teal.
- Text:
  - Producer: writes output
  - Reviewer: checks gate
  - Outputs: files + JSON
  - State: next step
- No tiny text, no squeezed card, no vertical narrow State card.

## Prompt 7: Integration Visual

Create a clean layered illustration called "Materials stay separated".

Design brief:
- 1280x720.
- Show separate lanes:
  - Codex workspace
  - Project files
  - Zotero
  - Obsidian
  - Evidence vault
- The point is separation and handoff, not a dense architecture diagram.
- Use large labels only.
- Keep the composition calm, grounded, and readable.

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

