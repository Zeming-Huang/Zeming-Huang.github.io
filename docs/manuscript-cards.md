# Manuscript cards

Edit `_data/manuscripts.yml` to update titles, authors, summaries, status, images,
or resource links. `_includes/manuscript-cards.html` renders one article per entry.
Keep submission status distinct from acceptance or publication.

Four thumbnails are extracted from the PDFs already public on this website:

| Image | Source | PDF page | Figure |
| --- | --- | --- | --- |
| nor-tl.png | files/papers/nor-tl.pdf | 2 | 1 |
| miraus.png | files/papers/miraus.pdf | 3 | 1 |
| prism.png | files/papers/prism.pdf | 2 | 1 |
| bioshoulder.png | files/papers/bioshoulder.pdf | 2 | 1 |

Regenerate them with `python tools/build_manuscript_thumbnails.py` (PyMuPDF required).
Figure coordinates must be checked if a manuscript PDF is replaced.

The two ECG forecasting cards intentionally have no PDF links. Their SVGs are
concept illustrations with synthetic waveforms, not manuscript figures, patient
data, experimental results, or disclosures of the unpublished architectures.
Do not restore withdrawn PDFs when editing these cards.

Only existing public resource links are displayed. A missing code link should
remain absent until a public repository has been confirmed.
