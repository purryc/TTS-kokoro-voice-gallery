# Kokoro Voice Gallery

## Scope and structure
- Public, independent community audition gallery for 157 official Kokoro preset voices.
- `data/voices.json`: sanitized catalog, source model revisions, demo text, waveform, and relative public audio paths.
- `templates/index.html`: editable HTML source. `scripts/build.py`: deterministic standard-library build.
- `site/`: generated public website; `site/audio/`: locally generated MP3 demo samples. Deploy only `site/`.
- `scripts/validate.py`: catalog completeness, order, media, and publication-content checks.
- `README.md`, `NOTICE.md`, `LICENSE`: usage, provenance and attribution. `site/about.html`: visitor-facing provenance.
- `.github/workflows/pages.yml`: validation, build and GitHub Pages deployment.
- Never include environments, model weights, caches, private paths, logs, credentials or personal artifacts.

## Product rules
- Show female and male voice groups and per-language distribution.
- Sort groups female then male; within each group, Chinese, English, then other languages; natural-sort official voice IDs. Assign stable catalog row numbers 001–157 without renaming official IDs.
- Preserve single-player behavior, search, language/gender filters, favorites and downloads; no autoplay on page load.
- Clearly identify the site as an independent community project, not the official model website.
- Audio is pre-generated, not browser TTS or a live generation API.

## Verification and publishing
- Run `python3 scripts/build.py` and `python3 scripts/validate.py` before commits.
- Public publishing is explicitly authorized for this task. Create the public GitHub repo and enable Pages.
- Deploy through the documented Pages workflow. Push alone is not proof of deployment.
- Verify the completed workflow, live page, complete media inventory and representative playback before reporting publication.
- Subsequent pushes require user authorization unless part of this authorized initial release/fix verification.
