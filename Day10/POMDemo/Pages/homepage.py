import time

from AugBatch.POMDemo.Locators.locators import Locators

class HomePage():
    def __init__(self,driver):
        self.driver = driver
        self.welcome_link_id = Locators.welcome_link_id
        self.logout_link_xpath = Locators.logout_link_xpath

    def clickWelcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def clickLogout(self):

        try:
            self.driver.find_element_by_xpath(self.logout_link_xpath).click()
        except:
            time.sleep(2)
            self.driver.find_element_by_xpath(self.logout_link_xpath).click()
