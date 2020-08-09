import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications":2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver =webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.redbus.in/")
#driver.maximize_window()

driver.find_element_by_id("src").send_keys("Bang")
time.sleep(3)
srclist = driver.find_elements_by_xpath("//input[@id='src']/following-sibling::ul/li")
for s in srclist:
    print(s.text)
    if s.text == 'White Field, Bangalore':
        s.click()
        break

driver.find_element_by_id("dest").send_keys("Del")
time.sleep(3)
destlist = driver.find_elements_by_xpath("//input[@id='dest']/following-sibling::ul/li")
for d in destlist:
    print(d.text)
    if "Metro Station" in d.text:
        d.click()
        break
