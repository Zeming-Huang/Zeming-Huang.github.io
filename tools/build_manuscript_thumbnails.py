from pathlib import Path

import pymupdf


def main():
    repository = Path(__file__).resolve().parents[1]
    destination = repository / "images" / "manuscripts"
    destination.mkdir(parents=True, exist_ok=True)
    figures = [
        ("nor-tl", 1, (56, 73, 558, 296)),
        ("miraus", 2, (51, 56, 288, 222)),
        ("prism", 1, (89, 52, 563, 298)),
        ("bioshoulder", 1, (311, 49, 565, 254)),
    ]
    for name, page_index, bounds in figures:
        source = repository / "files" / "papers" / f"{name}.pdf"
        with pymupdf.open(source) as document:
            preview = document[page_index].get_pixmap(
                matrix=pymupdf.Matrix(3, 3),
                clip=pymupdf.Rect(bounds),
                alpha=False,
            )
            preview.save(destination / f"{name}.png")
        print(f"Rendered {name}: page {page_index + 1}")


if __name__ == "__main__":
    main()
