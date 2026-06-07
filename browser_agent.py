from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()

    page = browser.new_page()


    print("Driving to www.google.com...")
    page.goto("https://instagram.com")

    title = page.title()

    print("The page title is:", title)

    page.screenshot(path="my_first_photo.png")
    print("photo saved as my_first_photo")

    text = page.content()
    print("first 200 char of the page")
    print(text[:200])

    browser.close()
print("Drive complete")
