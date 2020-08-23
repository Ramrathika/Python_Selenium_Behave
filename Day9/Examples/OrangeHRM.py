import time
from AugBatch.ReadExcel import *
from selenium import webdriver

driver =webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element_by_xpath("//input[@name = 'txtUsername']").send_keys(readExcel("HRM","Username"))
driver.find_element_by_xpath("//input[@type='password']").send_keys(readExcel("HRM","Password"))
driver.find_element_by_xpath("//input[@class='button']").click()
