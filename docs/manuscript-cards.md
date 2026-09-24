# Manuscript cards

Edit `_data/manuscripts.yml` to update titles, authors, summaries, status, images,
or resource links. `_includes/manuscript-cards.html` renders one article per entry.
Keep submission status distinct from acceptance or publication.

Thumbnails use the figures selected by the site owner:

| Image | Source | PDF page | Figure |
| --- | --- | --- | --- |
| nor-tl.png | files/papers/nor-tl.pdf | 2 | 1 |
| miraus.png | files/papers/miraus.pdf | 5 | 2 |
| prism.png | files/papers/miraus.pdf | 3 | 1, clinical context |
| bioshoulder.png | files/papers/bioshoulder.pdf | 2 | 1 |
| ecg-forecasting.png | Private ecg-waveform-forecasting.pdf | 2 | 1 |
| longitudinal-ecg.png | Private clef.pdf | 10 | 1 |

Regenerate them with `python tools/build_manuscript_thumbnails.py` (PyMuPDF required).
Pass `--private-pdf-dir /path/to/private/manuscripts` to regenerate the two ECG figures.
Private source PDFs must remain outside this website repository.
Figure coordinates must be checked if a manuscript PDF is replaced.

The two ECG forecasting cards intentionally have no PDF links. The owner has
authorized showing their overview figures, but not restoring the full PDFs.
The PRISM thumbnail uses MIRAUS Figure 1 as shared clinical context and is
labeled accordingly, rather than being presented as the PRISM architecture.

Only existing public resource links are displayed. A missing code link should
remain absent until a public repository has been confirmed.
