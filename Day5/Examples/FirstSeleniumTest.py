from selenium import webdriver

#driver =webdriver.Chrome(executable_path="E:\\Webdriver\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
#driver.find_element_by_id("email").send_keys("user1")
#driver.find_element_by_name("pass").send_keys("user1")
#driver.find_element_by_class_name("inputtext _58mg _5dba _2ph-").send_keys("firstname")

#driver.find_element_by_link_text("বাংলা").click()

#driver.find_element_by_partial_link_text("Sign Up").click()

driver.find_element_by_xpath("//input[@type='email']").send_keys("user2")
driver.find_element_by_xpath("//input[@data-testid='royal_pass']").send_keys("pass")
driver.find_element_by_xpath("//input[@value='Log In']").click()