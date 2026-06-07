from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print("Drive to wikipedia!!!")
    page.goto("https://www.wikipedia.org")

    page.screenshot(path="wikipedia.png")

    print("Pressing Enter!!")
    page.press("#searchInput", "Enter")

    page.wait_for_load_state("networkidle")

    page.screenshot(path="wikipedia.after.png")

    print("New page title:", page.title())

    browser.close()

print("Mission Complete!!")