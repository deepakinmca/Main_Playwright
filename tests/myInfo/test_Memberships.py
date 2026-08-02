import pytest 
from utils import *

from testdata.config import *
from utils.logger import logger
from testdata.locators import *
from testdata.Variables import *
from playwright.sync_api import Page, expect



#pytest.mark.flaky(reruns=1, reruns_delay=0)
class Test_FileUpload():
    @pytest.mark.regression
    def test_fileupload(self,login_application):
        logger.info("Regression Test Started")
        login_application.locator(Click_MyInfo).click()
        login_application.get_by_text("Memberships").click()
        print(login_application.url)
        expect(login_application).to_have_title('Test')
        login_application.screenshot(path="upload_page.png", full_page=True)
        print(login_application.locator("input[type='file']").count())
        # login_application.get_by_role('button', name=' Add ').click()
        print(login_application.get_by_role("button", name="Add").count())
        buttons = login_application.get_by_role("button", name="Add")
        logger.info("Regression Test Completed")

        # for i in range(buttons.count()):
        #     print(buttons.nth(i).text_content())
        # login_application.locator("input[type='file']").set_input_files("C:/Users/i9884/OneDrive/Desktop/Learnings/Playwright/Deepak_Natarajan_Resume.pdf")