import argparse
from pathlib import Path

import pymupdf


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--private-pdf-dir", type=Path)
    arguments = parser.parse_args()
    repository = Path(__file__).resolve().parents[1]
    destination = repository / "images" / "manuscripts"
    destination.mkdir(parents=True, exist_ok=True)
    figures = [
        ("nor-tl", repository / "files/papers/nor-tl.pdf", 1, (56, 73, 558, 296)),
        ("miraus", repository / "files/papers/miraus.pdf", 4, (51, 55, 541, 250)),
        ("prism", repository / "files/papers/miraus.pdf", 2, (51, 56, 288, 222)),
        ("bioshoulder", repository / "files/papers/bioshoulder.pdf", 1, (311, 49, 565, 254)),
    ]
    if arguments.private_pdf_dir:
        figures.extend([
            ("ecg-forecasting", arguments.private_pdf_dir / "ecg-waveform-forecasting.pdf", 1, (123, 349, 497, 561)),
            ("longitudinal-ecg", arguments.private_pdf_dir / "clef.pdf", 9, (110, 125, 501, 304)),
        ])
    for name, source, page_index, bounds in figures:
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
