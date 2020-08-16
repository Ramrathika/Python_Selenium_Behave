import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("http://leafground.com/pages/upload.html")

driver.find_element_by_name("filename").send_keys("C:\\Users\\Vignesh\\OneDrive\\Desktop\\New Text Document.txt")

