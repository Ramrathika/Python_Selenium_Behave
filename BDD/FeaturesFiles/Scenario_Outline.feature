Feature: Perform Parameterization

  Scenario Outline: To launch different URLS

     Given the user launches "<url>" url

    Examples:
    |url|
    |https://www.google.com/|
    |https://www.bing.com/|
    |https://www.yahoo.com/|
    |https://www.amazon.com/|

