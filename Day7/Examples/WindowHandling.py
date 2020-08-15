from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver  = webdriver.Chrome()
driver.get("https://www.openmultipleurl.com/")

driver.find_element_by_name("list_urls").send_keys("https://www.bing.com/")
driver.find_element_by_name("list_urls").send_keys(Keys.ENTER)


driver.find_element_by_name("list_urls").send_keys("https://www.google.com/")
driver.find_element_by_name("list_urls").send_keys(Keys.ENTER)


driver.find_element_by_name("list_urls").send_keys("https://www.yahoo.com/")
driver.find_element_by_name("list_urls").send_keys(Keys.ENTER)


driver.find_element_by_name("list_urls").send_keys("https://www.amazon.com/")
driver.find_element_by_name("list_urls").send_keys(Keys.ENTER)


driver.find_element_by_name("list_urls").send_keys("https://www.flipkart.com/")
driver.find_element_by_name("list_urls").send_keys(Keys.ENTER)

driver.find_element_by_name("list_urls").send_keys("https://www.facebook.com/")
driver.find_element_by_name("list_urls").send_keys(Keys.ENTER)


driver.find_element_by_xpath('//input[@value="Go Now"]').click()

print(driver.current_url)
print(driver.title)

###
print(driver.current_window_handle)
#parent window
firstwindow = driver.current_window_handle #window-id - unique junk numbers to identify it
#All open windows
allopenwindows = driver.window_handles
print(len(allopenwindows))
print(type(allopenwindows))

for a in allopenwindows:
    if a != firstwindow:
        driver.switch_to.window(a)
        print(driver.current_window_handle)
        print(driver.title)
        print(driver.current_url)
        if "Google" in driver.title:
            print("Hi Google")
            driver.find_element_by_name('q').send_keys("Happy Independence Day")

        else:
            driver.close()
