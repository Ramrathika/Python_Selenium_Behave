Feature: Bing Search
  @Sanity
  Scenario: To search anything on Bing

    Given the user launches Bing url
    When the user is on Bing Home page
    Then the user enters selenium in Bing search bar
    And the user clicks on Bing search
    