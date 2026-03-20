from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageOps


def generate_from_square(source: Image.Image, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    def save_png(size: int, name: str) -> None:
        source.resize((size, size), Image.Resampling.LANCZOS).save(
            out_dir / name, optimize=True
        )

    save_png(512, "android-chrome-512x512.png")
    save_png(192, "android-chrome-192x192.png")
    save_png(180, "apple-touch-icon.png")
    save_png(32, "favicon-32x32.png")
    save_png(16, "favicon-16x16.png")
    save_png(144, "mstile-144x144.png")

    ico = source.resize((256, 256), Image.Resampling.LANCZOS)
    ico.save(
        out_dir / "favicon.ico",
        sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
    )


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    src_path = repo_root / "images" / "luster.jpg"
    out_dir = repo_root / "images"

    if not src_path.exists():
        raise SystemExit(f"Missing source image: {src_path}")

    img = Image.open(src_path)
    img = ImageOps.exif_transpose(img)
    width, height = img.size
    side = min(width, height)
    left = (width - side) // 2
    top = (height - side) // 2
    square = img.crop((left, top, left + side, top + side))

    generate_from_square(square, out_dir)
    print("Generated favicon assets into ./images from images/luster.jpg")


if __name__ == "__main__":
    main()

