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

#scrolling down
driver.execute_script("window.scrollBy(0,1000);") #width, height


#scrolling up
driver.execute_script("window.scrollBy(0,-1000);") #width, height

#scrolling left to right
#driver.execute_script("window.scrollBy(100,0);") #width, height

#scrolling right to left
#driver.execute_script("window.scrollBy(-100,0);") #width, height


#scroll to end of the page
driver.execute_script(("window.scrollTo(0,document.body.scrollHeight);"))

#scroll to top of the page
driver.execute_script(("window.scrollTo(0,-document.body.scrollHeight);"))

#scrol to particular element

smsTXTBOX = driver.find_element_by_id("smsTXTBOX")
driver.execute_script("arguments[0].scrollIntoView(true);",smsTXTBOX)