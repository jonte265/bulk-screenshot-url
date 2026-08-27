from typing import Literal

import typer
from playwright.sync_api import ViewportSize, sync_playwright


def run(
    device: Literal["desktop", "mobile", "tablet"] = "desktop", delay_ms: int = 0
) -> None:

    viewports: dict[str, ViewportSize] = {
        "desktop": {"width": 1280, "height": 720},
        "tablet": {"width": 768, "height": 1024},
        "mobile": {"width": 390, "height": 844},
    }

    with (
        open(
            "sites/sites.txt",
            "r",
        ) as file,
        sync_playwright() as p,
    ):
        browser = p.chromium.launch()
        page = browser.new_page(viewport=viewports[device])
        for line in file:
            site = line.strip()
            page.goto(site)
            print(f"Taking screenshot: {site} ({device}) (delay-ms: {delay_ms})")
            page.wait_for_timeout(delay_ms)
            page.screenshot(
                path=f"screenshots/{site.removeprefix('https://').replace('/', '').replace('.', '').replace('www', '')}_{device}.png"
            )
            print("Done")
        browser.close()


def main() -> None:
    typer.run(run)
