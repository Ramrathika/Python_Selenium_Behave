import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver =webdriver.Chrome()
driver.get("https://signup.mail.com/#.1258-header-signup2-1")
driver.maximize_window()



nooftextbox = driver.find_elements_by_xpath("//input[@type='text']")
print(len(nooftextbox))

noofvalues = driver.find_elements_by_xpath('//select[@data-test="check-email-availability-email-domain-input"]//option')
print(len(noofvalues))
for n in noofvalues:
    print(n.text)


maildropdown = Select(driver.find_elements_by_xpath('//select[@data-test="check-email-availability-email-domain-input"]'))
for n in maildropdown.options:
    print(n.get_attribute('value'))
