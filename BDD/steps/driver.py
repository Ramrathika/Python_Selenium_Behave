from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from behave import *

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)