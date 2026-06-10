from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()

    page = browser.new_page()

    print("Driving to example.com...")
    page.goto("https://www.google.com")

    title = page.title()
    print("The page title is:", title)

    page.screenshot(path="first_screenshot.png")

    text = page.content()
    print("First 200 letters fo the page:")
    print(text[:200])

    browser.close()

print("Drive complete!!")