from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    print("Drive to Wikipedia...")
    page.goto("https://www.wikipedia.org")

    page.screenshot(path="wiki.png")

    print("Typing in search box..")
    page.fill("#searchInput", "Python programming language..")

    print("Pressing Button...")
    page.press("#searchInput", "Enter")

    page.wait_for_load_state("networkidle")

    page.screenshot(path="wiki2.png")

    print("New page title:", page.title())

    browser.close()

print("Mission complete!!")
