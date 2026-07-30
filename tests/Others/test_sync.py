from playwright.sync_api import sync_playwright
from testdata.config import *

def test_syncmethod():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(BASE_URL)

        print(page.title())

        browser.close()