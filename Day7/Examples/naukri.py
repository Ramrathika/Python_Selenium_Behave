from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.actions import *
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications":2,"profile.default_content_setting_values.geolocation":2}
print(type(prefs))
#prefs = {"profile.default_content_setting_values.geolocation":2}

chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver =webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.naukri.com/")
driver.maximize_window()
driver.implicitly_wait(30)
homewindow = driver.current_window_handle
allwindows = driver.window_handles
print(len(allwindows))
for a in allwindows:
    if a != homewindow:
        driver.switch_to.window(a)
        driver.close()
            #print("Closed unwanted pages")

driver.switch_to.window(homewindow)
print(driver.current_url)
wait = WebDriverWait(driver,30)
element = wait.until(EC.element_to_be_clickable((By.ID,"block")))
driver.find_element_by_id('block').click()

action = ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath("//a[@data-ga-track='Main Navigation Insights|Insights Icon']"))
action.move_to_element(driver.find_element_by_xpath("//a[@title='Boomerang']"))
action.click()
action.perform()
