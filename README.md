# Bulk Screenshot URL

Take screenshots of URLs listed in `sites/sites.txt` using Playwright.

## Setup

```bash
uv sync
uv run playwright install
```

## Usage

Add one URL per line to `sites/sites.txt`, then run:

```bash
uv run bulk-screenshot-url
```

Desktop is used by default. Choose another viewport or add a render delay:

```bash
uv run bulk-screenshot-url --device mobile
uv run bulk-screenshot-url --device tablet --delay-ms 2000
```

Screenshots are saved in `screenshots/`. Run `uv run bulk-screenshot-url --help` for all options.
