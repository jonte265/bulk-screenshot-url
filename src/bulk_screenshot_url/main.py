from playwright.sync_api import sync_playwright


def main() -> None:

    with open(
        "sites/sites.txt",
        "r",
    ) as file:
        for line in file:
            site = line.strip()
            print(site)

            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto(site)
                print("Taking screenshot: ", site)
                page.screenshot(
                    path=f"screenshots/{site.removeprefix('https://').replace('/', '').replace('.', '').replace('www', '')}.png"
                )
                # print(page.title())
                print("Done")
                browser.close()
