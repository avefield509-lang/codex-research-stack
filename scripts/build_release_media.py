from __future__ import annotations

from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFilter, ImageFont

try:
    from public_release_env import ASSETS_DIR
except ModuleNotFoundError:
    from scripts.public_release_env import ASSETS_DIR


WIDTH = 1280
HEIGHT = 720
BG_TOP = (8, 25, 27)
BG_BOTTOM = (17, 48, 60)
CREAM = (246, 244, 236)
MUTED = (172, 199, 194)
ACCENT = (229, 190, 103)
TEAL = (21, 59, 65)
TEAL_ALT = (26, 83, 93)
PANEL = (18, 42, 46)
FRAME_SOURCES = [
    "hero-overview.png",
    "multi-agent-workspace.png",
    "pipeline-gates-overview.png",
]


def find_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates: list[Path] = []
    font_dir = Path("C:/Windows/Fonts")
    if bold:
        candidates.extend([font_dir / "segoeuib.ttf", font_dir / "arialbd.ttf"])
    candidates.extend([font_dir / "segoeui.ttf", font_dir / "arial.ttf"])
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


FONT_H1 = find_font(64, bold=True)
FONT_H2 = find_font(36, bold=True)
FONT_H3 = find_font(24, bold=True)
FONT_BODY = find_font(24)
FONT_SMALL = find_font(18)
FONT_PILL = find_font(22, bold=True)


def lerp(a: int, b: int, t: float) -> int:
    return int(a + (b - a) * t)


def gradient_background() -> Image.Image:
    image = Image.new("RGBA", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)
    for y in range(HEIGHT):
        t = y / max(1, HEIGHT - 1)
        color = tuple(lerp(BG_TOP[i], BG_BOTTOM[i], t) for i in range(3))
        draw.line((0, y, WIDTH, y), fill=color, width=1)
    return image


def rounded_panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: tuple[int, int, int], outline: tuple[int, int, int] | None = None, width: int = 2) -> None:
    draw.rounded_rectangle(box, radius=28, fill=fill, outline=outline, width=width)


def pill(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fill: tuple[int, int, int], text_fill: tuple[int, int, int]) -> None:
    x, y = xy
    bbox = draw.textbbox((0, 0), text, font=FONT_PILL)
    w = bbox[2] - bbox[0] + 40
    h = 46
    draw.rounded_rectangle((x, y, x + w, y + h), radius=23, fill=fill)
    draw.text((x + 20, y + 10), text, font=FONT_PILL, fill=text_fill)


def draw_header(draw: ImageDraw.ImageDraw) -> None:
    draw.text((78, 70), "Codex Research Stack", font=FONT_H1, fill=CREAM)
    draw.text(
        (82, 148),
        "A plugin-first research operating layer for Codex",
        font=FONT_H2,
        fill=MUTED,
    )
    pill(draw, (82, 212), "Plugin-first", TEAL_ALT, CREAM)
    pill(draw, (252, 212), "Multi-agent squads", TEAL_ALT, CREAM)
    pill(draw, (502, 212), "Pipeline gates", TEAL_ALT, CREAM)


def draw_glow(base: Image.Image, center: tuple[int, int], radius: int, color: tuple[int, int, int], alpha: int) -> None:
    glow = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    x, y = center
    gdraw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*color, alpha))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=36))
    base.alpha_composite(glow)


def cover_crop(image: Image.Image) -> Image.Image:
    source_ratio = image.width / image.height
    target_ratio = WIDTH / HEIGHT
    if source_ratio > target_ratio:
        new_height = image.height
        new_width = int(new_height * target_ratio)
        left = (image.width - new_width) // 2
        top = 0
    else:
        new_width = image.width
        new_height = int(new_width / target_ratio)
        left = 0
        top = (image.height - new_height) // 2
    cropped = image.crop((left, top, left + new_width, top + new_height))
    return cropped.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)


def build_slide(image_name: str, title: str, subtitle: str) -> Image.Image:
    base = gradient_background()
    source = Image.open(ASSETS_DIR / image_name).convert("RGBA")
    visual = cover_crop(source)
    visual = visual.filter(ImageFilter.GaussianBlur(radius=0.3))
    base.alpha_composite(visual, (0, 0))

    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    odraw.rounded_rectangle((42, 42, WIDTH - 42, HEIGHT - 42), radius=34, fill=(4, 12, 16, 118), outline=(42, 90, 98, 180), width=2)
    draw_glow(overlay, (180, 132), 140, (26, 114, 115), 60)
    draw_glow(overlay, (1100, 590), 160, (181, 142, 72), 44)
    base.alpha_composite(overlay)

    draw = ImageDraw.Draw(base)
    draw.text((72, 66), "Codex Research Stack", font=FONT_H1, fill=CREAM)
    draw.text((76, 140), title, font=FONT_H2, fill=ACCENT)
    draw.text((76, 186), subtitle, font=FONT_BODY, fill=MUTED)
    pill(draw, (76, 246), "Plugin-first", TEAL_ALT, CREAM)
    pill(draw, (246, 246), "Multi-agent", TEAL_ALT, CREAM)
    pill(draw, (430, 246), "Research gates", TEAL_ALT, CREAM)
    return base


def scene(progress: float) -> Image.Image:
    if progress < 0.34:
        base = build_slide(
            "hero-overview.png",
            "Route, evidence, writing, and knowledge in one visible system",
            "A visual overview of the public research stack without fabricated metrics.",
        )
    elif progress < 0.67:
        base = build_slide(
            "multi-agent-workspace.png",
            "Project work becomes a readable multi-agent workspace",
            "Dispatch, reviewer mapping, handoff, and project state move together.",
        )
    else:
        base = build_slide(
            "pipeline-gates-overview.png",
            "Quality gates stay visible across the research lifecycle",
            "Citation, provenance, writing, validity, and packaging remain explicit.",
        )
    return base.convert("P", palette=Image.ADAPTIVE, colors=255)


def build_frames() -> Iterable[Image.Image]:
    steps = [0.0] * 6 + [0.4] * 6 + [0.8] * 6
    for value in steps:
        yield scene(value)


def main() -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    frames = list(build_frames())
    target = ASSETS_DIR / "hero-demo.gif"
    frames[0].save(
        target,
        save_all=True,
        append_images=frames[1:],
        duration=[520] * len(frames),
        loop=0,
        optimize=False,
        disposal=2,
    )
    print(target)


if __name__ == "__main__":
    main()
