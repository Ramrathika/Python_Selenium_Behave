from AugBatch.POMDemo.Locators.locators import Locators
#from selenium import webdriver
#driver = webdriver.Chrome()
class LoginPage():

    def __init__(self,driver):
        self.driver = driver
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id

    def enterUsername(self,Username):
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(Username)

    def enterPassword(self,Password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(Password)

    def clickLogin(self):
        self.driver.find_element_by_id(Locators.login_button_id).click()

