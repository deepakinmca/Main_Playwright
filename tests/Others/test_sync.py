from playwright.sync_api import sync_playwright

def test_syncmethod():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.google.com")
        page.screenshot(path="Demo3.png")
        page.goto("https://www.flipkart.com", wait_until="domcontentloaded", timeout=10000)
        page.screenshot(path="Demo4.png")
        page.close()