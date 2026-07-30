from playwright.sync_api import Page, expect
from testdata.config import *
from testdata.locators import *
from testdata.Variables import *
from utils import *

class Test_FileUpload():
    def test_fileupload(self,login_application):
        login_application.locator(Click_MyInfo).click()
        login_application.get_by_text("Memberships").click()
        print(login_application.url)
        login_application.screenshot(path="upload_page.png", full_page=True)
        print(login_application.locator("input[type='file']").count())
        # login_application.get_by_role('button', name=' Add ').click()
        print(login_application.get_by_role("button", name="Add").count())
        buttons = login_application.get_by_role("button", name="Add")

        for i in range(buttons.count()):
            print(buttons.nth(i).text_content())
        login_application.locator("input[type='file']").set_input_files("C:/Users/i9884/OneDrive/Desktop/Learnings/Playwright/Deepak_Natarajan_Resume.pdf")