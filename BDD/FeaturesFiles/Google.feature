Feature: Google Search
  @Regression
  Scenario: To search anything on Google

    Given the user launches google url
    When the user is on google Home page
    Then the user enters selenium in google search bar
    And the user clicks on google search
