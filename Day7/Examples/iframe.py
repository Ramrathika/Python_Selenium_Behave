from selenium import webdriver
import time
driver  = webdriver.Chrome()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_xpath('//a[@onclick="retheme()"]').click()

#index
#driver.switch_to.frame(0)

#name/id
driver.switch_to.frame("iResult")

#locators
#driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='iframeResult']"))

driver.find_element_by_xpath("//button[text()='Try it']").click()

#Parent frame

#default frame