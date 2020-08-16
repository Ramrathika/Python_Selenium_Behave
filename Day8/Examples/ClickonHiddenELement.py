import time
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications":2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver =webdriver.Chrome(chrome_options=chrome_options)
#driver.set_page_load_timeout(60)
driver.get("www.irctc.co.in/")
time.sleep(5)

pnrstatus = driver.find_element_by_xpath("label{//text()='PNR STATUS'}")
#driver.execute_script("arguments[0].click();",pnrstatus)
pnrstatus.click()