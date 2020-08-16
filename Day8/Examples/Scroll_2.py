import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications":2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver =webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.bluevertigo.com.ar/")
#driver.switch_to.frame("iframeResult")
time.sleep(10)

#scrolling down
driver.execute_script("window.scrollBy(1000,0);") #width, height

time.sleep(10)
#scrolling up
#driver.execute_script("window.scrollBy(0,-1000);") #width, height
