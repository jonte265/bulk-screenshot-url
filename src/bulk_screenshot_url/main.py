from playwright.sync_api import sync_playwright


def main() -> None:

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://playwright.dev")
        page.screenshot(path="screenshots/example.png")
        # print(page.title())
        print("Done")
        browser.close()
