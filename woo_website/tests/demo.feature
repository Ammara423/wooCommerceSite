# Created by owner at 12/4/24
Feature: Login on the dashboard with secure credentials
As a user I want to login the website with the secure credentials.

  Feature: OrangeHRM Login

  Scenario: User logs in with valid credentials
    Given I am on the OrangeHRM login page
    When I enter the username and password from environment variables
    And I click the login button
#    Then I should see the dashboard

