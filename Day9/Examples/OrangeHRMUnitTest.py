import unittest
from AugBatch.ReadExcel import *
from selenium import webdriver
import time
import HtmlTestRunner


class OrangeHRMTest(unittest.TestCase):

    #Setup
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        cls.driver.maximize_window()

    def test_1_login(self):
        self.driver.find_element_by_xpath("//input[@name = 'txtUsername']").send_keys(readExcel("HRM", "Username"))
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(readExcel("HRM", "Password"))
        self.driver.find_element_by_xpath("//input[@class='button']").click()

    def test_2_logout(self):
        self.driver.find_element_by_id("welcome").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[text()='Logout']").click()

    @classmethod
    def tearDownClass(cls):
        print("Successfully executed")
        #cls.driver.quit()

if __name__ == '__main__':
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:\\Python\\Results'))
