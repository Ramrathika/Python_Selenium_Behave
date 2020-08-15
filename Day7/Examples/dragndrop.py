from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver  = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@class="demo-frame"]'))

drag = driver.find_element_by_id("draggable")
drop = driver.find_element_by_id("droppable")

act = ActionChains(driver)
act.drag_and_drop(drag,drop)
act.perform()
#act.drag_and_drop_by_offset(drag,100,600)
