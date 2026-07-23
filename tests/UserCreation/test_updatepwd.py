from playwright.sync_api import Page, expect
from testdata.config import *
from testdata.locators import *
from testdata.Variables import *

class Test_UpdatePassword():
    def test_UpdatePwd(self,login_application, pwd=NEW_PWD, Current_Pwd=PASSWORD,Confirm_Pwd=CONFIRM_PWD):
        login_application.locator(Clicking_User_Profile).click()
        login_application.locator(Change_Password_link).click()
        login_application.locator(Current_Password).nth(0).fill(Current_Pwd)
        login_application.locator(Password_first).nth(1).fill(pwd)
        login_application.locator(Confirm_Pwd_last).nth(2).fill(Confirm_Pwd)
        login_application.locator(Save_Button).click()
        