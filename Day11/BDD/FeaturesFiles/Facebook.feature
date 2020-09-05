Feature: Example of Scenario Outline
    @Regression
Scenario Outline: TC_0010_Facebook Login Check

    Given the user hits "<url>"
    Then the user enters username as "<username>"
    And the user enters password as "<password>"
    Then the user clicks on submit

    Examples:
    |username|password| url|
    |user1   |pass1   | https://www.facebook.com/|
    |user2   |pass2   | https://www.facebook.com/|
    |user3   |pass3   | https://www.facebook.com/|

    #Allure - reporting