from selenium import webdriver
import time
import unittest
from AugBatch.POMDemo.Locators.locators import Locators
from AugBatch.POMDemo.Pages.homepage import HomePage
from AugBatch.POMDemo.Pages.loginpage import LoginPage
from AugBatch.POMDemo.DataTable.DataReader import Exceldata
from AugBatch.POMDemo.Config.ConfigReader import ReadProperties
class OrangeHRMTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        Read = ReadProperties()
        print(Read.configReader("url"))
        cls.driver.get(Read.configReader('url'))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

    def test_1_login(self):
        login = LoginPage(self.driver)
        exceldata = Exceldata()
        #login.enterUsername("Admin")
        username = exceldata.readExcel("HRM","Username")

        login.enterUsername(username)
        pwd = exceldata.readExcel("HRM", "Password")

        login.enterPassword(pwd)
        login.clickLogin()

    def test_2_logout(self):
        homepage = HomePage(self.driver)
        time.sleep(3)
        homepage.clickWelcome()
        homepage.clickLogout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
