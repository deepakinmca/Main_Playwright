from playwright.sync_api import Page, expect
from testdata.config import *
from testdata.locators import *
from testdata.Variables import *
from utils import *
class Test_MyInfo_Personal_Data:
    def test_myinfo_profile_img(self, login_application):
        # Verify whether image is present or not [get_by_alt_text, is_visible, is_hidden, wait_for_load_state and to_be_visible]

        login_application.locator(Click_MyInfo).click()

        #image_name = (login_application.get_by_alt_text(PROFILE_NAME).first)
        employee_section = login_application.locator(IMAGE_CLASS_NAME)
        image_name = employee_section.get_by_alt_text(PROFILE_NAME)
        login_application.wait_for_load_state("networkidle")
        expect(image_name).to_be_visible(timeout=5000)

        print("URL:", login_application.url)
        print("Count:", image_name.count())
        print("Visible:", image_name.is_visible())
        print("Hidden:", image_name.is_hidden())
        login_application.screenshot(path="debug.png", full_page=True)
        
        # Verify the properties [get_by_text,get_by_role]
    def test_Personal_details(self, login_application):
        login_application.locator(Click_MyInfo).click()
        expect(login_application.get_by_role("heading", name="Personal Details")).to_be_visible()

        emp_textName = login_application.get_by_text("Employee Full Name")
        expect(emp_textName).to_be_visible(timeout=3000)

        #login_application.locator(FirstName).fill(EMP_FNAME)
        fname = login_application.locator(FirstName)
        print("Before:", fname.input_value())
        fname.fill(EMP_FNAME)
        print("After:", fname.input_value())

        #login_application.locator(lastName).fill(EMP_FNAME)
        lname = login_application.locator(lastName)
        print("Before:", lname.input_value())
        lname.fill(EMP_LNAME)
        print("After:", lname.input_value())

        #login_application.locator(Emp_ID).fill(EMP_ID)
        emp_ID = login_application.locator(Emp_ID)
        print("Before:", emp_ID.input_value())
        emp_ID.fill(EMP_ID)
        print("After:", emp_ID.input_value())
        
        #login_application.locator(Other_ID).fill(OTHER_ID)
        other_ID = login_application.locator(Other_ID)
        print("Before:", other_ID.input_value())
        print(other_ID.input_value())
        other_ID.fill(OTHER_ID)
        print("After:", other_ID.input_value())

        male_radio = login_application.get_by_role("radio", name="Male")
        print(male_radio.count())
        #login_application.locator(Radio_Male).check()
        login_application.locator(Test_Field).fill(TEST_FIELD)
        login_application.wait_for_timeout(20000)
    
    def test_Contact_Details(self, login_application):
        login_application.locator(Click_MyInfo).click()
        login_application.get_by_text("Contact Details").click()
        expect(login_application.get_by_role("heading", name="Contact Details")).to_be_visible()
        
        streetName1 = login_application.locator(Street_1)
        print("Before:", streetName1.input_value())
        streetName1.fill(STREET_NAME_1)
        print("After:", streetName1.input_value())
        
        streetName2 = login_application.locator(Street_2)
        print("Before:", streetName2.input_value())
        streetName2.fill(STREET_NAME_2)
        print("After:", streetName2.input_value())
    
        City_Nme = login_application.locator(City_Name)
        print("Before:", City_Nme.input_value())
        City_Nme.fill(CITY_NAME)
        print("After:", City_Nme.input_value())
        
        State_Nme = login_application.locator(State_Name)
        #print("Before:", State_Nme.input_value())
        State_Nme.fill(STATE_NAME)
        print("After:", State_Nme.input_value())
        
        ZipCode = login_application.locator(Zip_Code)
        #print("Before:", ZipCode.input_value())
        ZipCode.fill(PIN_CODE)
        print("After:", ZipCode.input_value())
        