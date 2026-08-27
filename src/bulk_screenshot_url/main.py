import typer
from playwright.sync_api import ViewportSize, sync_playwright


def run(mobile: bool = False, delay_ms: int = 0) -> None:

    chosen = "desktop"

    if mobile:
        chosen = "mobile"

    viewports: dict[str, ViewportSize] = {
        "desktop": {"width": 1280, "height": 720},
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
        page = browser.new_page(viewport=viewports[chosen])
        for line in file:
            site = line.strip()
            page.goto(site)
            print("Taking screenshot:", site)
            page.wait_for_timeout(delay_ms)
            page.screenshot(
                path=f"screenshots/{site.removeprefix('https://').replace('/', '').replace('.', '').replace('www', '')}_{chosen}.png"
            )
            print("Done")
        browser.close()


def main() -> None:
    typer.run(run)
