import pytest
from playwright.sync_api import Page, expect
from testdata.config import *
from testdata.config import USERNAME, PASSWORD
from testdata.locators import *
from testdata.Variables import *

@pytest.fixture
def login_application(page:Page):
    page.goto(BASE_URL)
    page.locator(Login_UserName).fill(USERNAME)
    page.locator(Login_Password).fill(PASSWORD)
    page.locator(Login_Button).click()
    return page