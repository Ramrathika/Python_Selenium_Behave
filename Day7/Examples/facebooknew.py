from selenium import webdriver
import time
driver  = webdriver.Chrome()
driver.get("https://www.facebook.com/")

driver.find_element_by_xpath('//a[@rel="async"]').click()
time.sleep(3)
driver.find_element_by_name("firstname").send_keys("India")
