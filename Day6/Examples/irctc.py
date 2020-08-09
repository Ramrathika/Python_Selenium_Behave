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
driver.get("https://www.irctc.co.in/")
#driver.maximize_window()
#driver.implicitly_wait(30)


wait = WebDriverWait(driver,15,poll_frequency=2,ignored_exceptions=[ElementNotVisibleException])
element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[text()='Ok']")))
driver.find_element_by_xpath("//button[text()='Ok']").click()
