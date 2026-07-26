import pytest
from playwright.sync_api import Page, expect
from testdata.config import *
from testdata.config import USERNAME, PASSWORD
from testdata.locators import *
from testdata.Variables import *

@pytest.fixture
def login_application(page:Page):
    page.goto(BASE_URL)
    page_url = page.url
    expect(page).to_have_url(page_url)
    page_title = page.title()
    expect(page).to_have_title(page_title)
    page.locator(Login_UserName).fill(USERNAME)
    page.locator(Login_Password).fill(PASSWORD)
    page.locator(Login_Button).click()
    return page