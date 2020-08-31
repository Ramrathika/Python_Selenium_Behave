from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome()
#driver.maximize_window()
#driver.implicitly_wait(30)


@given('the user launches google url')
def url_launch(context):
    context.driver = driver
    context.driver.get("https://www.google.com/")


@when('the user is on google home page')
def google_Logo(context):
    context.driver = driver
    logo = context.driver.find_element_by_id("hplogo").is_displayed()
    assert logo is True

@then('the user searches Python in search box')
def google_SearchBar(context):
    context.driver = driver
    context.driver.find_element_by_xpath('//input[@maxlength="2048"]').send_keys("Python")

@then('the user clicks enter')
def google_Search(context):
    context.driver = driver
    context.driver.find_element_by_xpath('//input[@maxlength="2048"]').send_keys(Keys.ENTER)


@given(u'the user launches bing url')
def bing_url(context):
    context.driver = driver
    context.driver.get("https://www.bing.com/")

@when(u'the user is on bing home page')
def bing_home_page(context):
    context.driver = driver
    logo = context.driver.find_element_by_id("b_logo").is_displayed()
    assert logo is True

@then(u'the user searches Python in bing search box')
def bing_search(context):
    context.driver = webdriver.Chrome()
    context.driver.find_element_by_xpath('//input[@name="q"]').send_keys("Python")

@then(u'the user clicks bing enter')
def bing_search_enter(context):
    context.driver = driver
    context.driver.find_element_by_xpath('//input[@name="q"]').send_keys(Keys.ENTER)


@given(u'the user hits "{url}"')
def step_impl(context,url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)


@then(u'the user enters username as "{username}"')
def facebook_username(context,username):
    #ontext.driver = driver
    context.driver.refresh()
    context.driver.find_element_by_id("email").send_keys(username)



@then(u'the user enters password as "{password}"')
def facebook_password(context,password):
    #context.driver = driver
    context.driver.find_element_by_id("pass").send_keys(password)


@then(u'the user clicks on submit')
def facebook_click(context):
    #context.driver = driver
    context.driver.find_element_by_name("login").click()