Feature: Search Engine Automation

  Scenario: TC_001_Google Search

    Given the user launches google url
    When the user is on google home page
    Then the user searches Python in search box
    And the user clicks enter


  Scenario: TC_002_Google Search

    Given the user launches bing url
    When the user is on bing home page
    Then the user searches Python in bing search box
    And the user clicks bing enter
