from playwright.sync_api import Page, expect
from testdata.config import *
from testdata.locators import *
from testdata.Variables import *
class Test_MyInfo_Personal_Data:
    def test_myinfo_profile_img(self, login_application):
        # # Verify whether image is present or not [get_by_alt_text, is_visible, is_hidden, wait_for_load_state and to_be_visible]

        #login_application.locator(Click_MyInfo).click()

        # #image_name = (login_application.get_by_alt_text(PROFILE_NAME).first)
        # employee_section = login_application.locator(IMAGE_CLASS_NAME)
        # image_name = employee_section.get_by_alt_text(PROFILE_NAME)
        # login_application.wait_for_load_state("networkidle")
        # expect(image_name).to_be_visible(timeout=5000)

        # print("URL:", login_application.url)
        # print("Count:", image_name.count())
        # print("Visible:", image_name.is_visible())
        # print("Hidden:", image_name.is_hidden())
        # login_application.screenshot(path="debug.png", full_page=True)
        pass
        
        # Verify the properties [get_by_text,get_by_role]
    def test_Personal_details(self, login_application):
        login_application.locator(Click_MyInfo).click()
        expect(login_application.get_by_role("heading", name="Personal Details")).to_be_visible()
        emp_textName = login_application.get_by_text("Employee Full Name")
        expect(emp_textName).to_be_visible(timeout=3000)
        
        login_application.locator(FirstName).fill(EMP_FNAME)
        login_application.locator(lastName).fill(EMP_FNAME)
        login_application.locator(Emp_ID).fill(EMP_ID)
        login_application.locator(Other_ID).fill(OTHER_ID)
        male_radio = login_application.get_by_role("radio", name="Male")
        print(male_radio.count())
        # login_application.locator(Radio_Male).check()
        # login_application.locator(Test_Field).fill(TEST_FIELD)