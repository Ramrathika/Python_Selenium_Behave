from behave import *
from Sele_Pyt_Sreeni.BDDDemo.steps.driver import *


@given(u'the user launches google url')
def google_url(context):
    context.driver = driver
    driver.get("https://www.google.com/")

    #raise NotImplementedError(u'STEP: Given the user launches google url')

@when(u'the user is on google Home page')
def logo_verify(context):
    context.driver = driver
    logo = driver.find_element_by_id("hplogo").is_displayed()
    assert logo is True

@then(u'the user enters selenium in google search bar')
def enter_selenium(context):
    #raise NotImplementedError(u'STEP: Then the user enters selenium in google search bar')
    context.driver = driver
    driver.find_element_by_name('q').send_keys("Selenium")

@then(u'the user clicks on google search')
def click_searchbar(context):
    context.driver = driver
    driver.find_element_by_name('q').send_keys(Keys.ENTER)
    #driver.close()


@given(u'the user launches Bing url')
def bingurl(context):
    context.driver = driver
    driver.get("https://www.bing.com/")
    driver.maximize_window()

@when(u'the user is on Bing Home page')
def bing_logo(context):
    context.driver = driver
    logo = driver.find_element_by_id("bLogo").is_displayed()
    assert logo is True
@then(u'the user enters selenium in Bing search bar')
def seleniumsearch(context):
    context.driver = driver
    driver.find_element_by_name('q').send_keys("Selenium")

@then(u'the user clicks on Bing search')
def search_selenium(context):
    context.driver = driver
    driver.find_element_by_name('q').send_keys(Keys.ENTER)
    #driver.quit()
