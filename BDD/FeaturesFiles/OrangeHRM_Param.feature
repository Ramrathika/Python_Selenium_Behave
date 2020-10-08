Feature: OrangeHRM

  Scenario: To login

    Given the user launches "https://opensource-demo.orangehrmlive.com/" url
    When the user enters "Admin" in username field
    Then the user enters "admin123" in password field
    And the user clicks on Login button

  @Google
  Scenario: To launch google
      Given the user launches "https://google.com/" url


  @Yahoo
  Scenario: To launch Yahoo
      Given the user launches "https://yahoo.com/" url
