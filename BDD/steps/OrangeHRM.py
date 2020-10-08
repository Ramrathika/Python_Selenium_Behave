from Sele_Pyt_Sreeni.BDDDemo.steps.driver import *



@given(u'the user launches "{url}" url')
def launching_url(context,url):
    context.driver = driver
    driver.get(url)

@when(u'the user enters "{username}" in username field')
def enter_username(context,username):
    context.driver = driver
    driver.find_element_by_id("txtUsername").send_keys(username)


@then(u'the user enters "{password}" in password field')
def enter_password(context,password):
    context.driver = driver
    driver.find_element_by_id("txtPassword").send_keys(password)


@then(u'the user clicks on Login button')
def login_click(context):
    context.driver = driver
    driver.find_element_by_name("Submit").click()
