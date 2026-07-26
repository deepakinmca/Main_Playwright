# This file contains all the XPATH's which are related to this Application.
#----------------------------------------------------------------------------------------------------------------#
# Login Screen

Login_Button         = "button[type='submit']"
Login_UserName       = "input[name='username']"
Login_Password       = "input[name='password']"

#----------------------------------------------------------------------------------------------------------------#
# Profile Password Updation
Password_first        = "input[type='password']"           #"input[type='password']"
Confirm_Pwd_last      = "input[type='password']"   #"input[type='password']"
Current_Password      = "input[type='password']"
Save_Button           = "button[type='submit']"
Cancel_Button         = "button[type='button']"
Clicking_User_Profile = "p.oxd-userdropdown-name"
Change_Password_link  = "//a[@role='menuitem' and text()='Change Password']"

#-----------------------------------------------------------------------------------------------------------------#
# Create New Admin user
Save_button            = "//button[@type='submit']"
Click_Admin            = "//span[normalize-space()='Admin']"
Click_Add              = "//button[normalize-space()='Add']"
Emp_Name               = "//input[@placeholder='Type for hints...']"
d_Select_Status        = "('div').filter({ hasText: '-- Select --' }).last()"
Cancel_Button          = "//button[@type='button' and normalize-space()='Cancel']"
UserName               = "//label[normalize-space()='Username']/ancestor::div[contains(@class,'oxd-input-group')]//input"
Confirm_pwd            = "//label[normalize-space()='Confirm Password']/ancestor::div[contains(@class,'oxd-input-group')]//input"
Xpath_Role             = "//label[normalize-space()='User Role']/../following-sibling::div//div[contains(@class,'oxd-select-text-input')]"
Xpath_Status           = "//label[normalize-space()='Status']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text-input')]"

#------------------------------------------------------------------------------------------------------------------#
# Create My Info - Personal Details
PROFILE_NAME            = "profile picture"
FirstName               = "//input[@name='firstName']"
lastName                = "//input[@name='lastName']"
IMAGE_CLASS_NAME        = ".orangehrm-edit-employee-image"
Click_MyInfo            = "//span[normalize-space()='My Info']"
Other_ID                = "//label[normalize-space()='Other Id']/following::input[1]"
Radio_Male              = "//label[normalize-space()='Male']/preceding-sibling::input"
Test_Field              = "//label[normalize-space()='Test_Field']/following::input[1]"
License_Num             = "//label[normalize-space()='Driver's License Number']/following::input"
Emp_ID                  = "//label[@class='oxd-label' and normalize-space()='Employee Id']/following::input[1]"


