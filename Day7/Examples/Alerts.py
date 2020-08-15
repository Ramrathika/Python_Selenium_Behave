from selenium import webdriver
import time
driver  = webdriver.Chrome()

'''
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
#https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_xpath('//a[@onclick="retheme()"]').click()
time.sleep(5)

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='iframeResult']"))

driver.find_element_by_xpath("//button[text()='Try it']").click()
time.sleep(5)

#accept - positive cases yes, okay, true - accept
#dismiss - negative cases cancel, no, false - dismiss
#text - to get the text of popup
#Sendkeys - to send the values to popup

driver.switch_to.alert.accept()

driver.switch_to.parent_frame()
driver.find_element_by_xpath('//a[@onclick="retheme()"]').click()


'''
driver.get("http://www.leafground.com/pages/Alert.html")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//button[text()='Prompt Box']").click()
time.sleep(5)
#driver.switch_to.alert.dismiss()

print(driver.switch_to.alert.text)
driver.switch_to.alert.send_keys("Google")
driver.switch_to.alert.accept()
