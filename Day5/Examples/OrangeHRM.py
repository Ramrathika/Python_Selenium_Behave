import time

from selenium import webdriver

driver =webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element_by_xpath("//input[@name = 'txtUsername']").send_keys("admin")
driver.find_element_by_xpath("//input[@type='password']").send_keys("admin123")
driver.find_element_by_xpath("//input[@class='button']").click()
#driver.close()
#driver.quit()
driver.back()
time.sleep(5)
driver.forward()
print(driver.get_window_size())