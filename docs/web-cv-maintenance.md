# Web CV maintenance

The permanent CV URL is `https://zeming-huang.github.io/cv/`.
It is an HTML page, not a dated PDF link.

The existing local `CV.tex` remains the content source for the print and web
versions. `tools/render_web_cv.py` converts its content sections into
`_pages/cv.md`. The contact header and LaTeX layout remain local; no phone
number or local source path is published. The website sidebar provides contact
information using its existing settings.

For the owner's Windows workspace:

1. Edit `CV.tex` as usual.
2. From the application workspace, run `./Update-CVWebsite.ps1 -Publish`.
3. Wait for the GitHub Pages deployment to complete. The public CV URL stays
   the same.

The script requires no unrelated local changes before publishing, pulls remote changes
without rewriting history, and commits only the generated CV page. Local edits
are not automatically uploaded. If new LaTeX commands are introduced, the
converter stops rather than silently dropping unsupported content.

To render in another environment:

```sh
python tools/render_web_cv.py --source /path/to/CV.tex
```

Review and commit `_pages/cv.md` to publish. This converter does not modify the
LaTeX source, the PDF, the homepage research summary, or paper links.
