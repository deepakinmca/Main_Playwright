from playwright.sync_api import Page, expect
from testdata.config import *
from testdata.locators import *
from testdata.Variables import *

class Test_UserCreation():
    def test_adminUserCreation(self, login_application):
        login_application.locator(Click_Admin).click()
        login_application.locator(Click_Add).click()
        user = DICT_ADMIN_USER
        login_application.locator(Xpath_Role).click()
        login_application.get_by_role("option", name=user["role"]).click()
        login_application.locator(Xpath_Status).click()
        login_application.get_by_role("option", name=user["status"]).click()
        login_application.locator(Emp_Name).fill(EMP_FNAME)
        login_application.locator(UserName).fill(USER_NAME)
        login_application.locator(Confirm_pwd)
        login_application.locator(Confirm_pwd)
        login_application.locator(Save_button).click()
        
        
    
    