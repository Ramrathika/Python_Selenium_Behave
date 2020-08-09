from selenium import webdriver
from selenium.webdriver.support.ui import Select
#driver =webdriver.Chrome(executable_path="E:\\Webdriver\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

driver.find_element_by_xpath("//label[text()='Male']").click()
driver.find_element_by_xpath("//input[@type='radio' and @value= '-1']").click()

Day = Select(driver.find_element_by_id('day'))
Day.select_by_value("28")

Month = Select(driver.find_element_by_name("birthday_month"))
Month.select_by_index(5)

Year = Select(driver.find_element_by_id("year"))
Year.select_by_visible_text("2012")

for y in Year.options:
    print(y.text)
