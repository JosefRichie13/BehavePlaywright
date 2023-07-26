@AutomatedTests
@LoginAndLogout

Feature: User login and logout scenarios

  Scenario: Valid user login
    Given I open the web page
    When I login as a "standard" user
    Then I should see "Swag Labs" in the "homepage"

  Scenario: Locked out user cannot login
    Given I open the web page
    When I login as a "locked" user
    Then I should see the login error message "Sorry, this user has been locked out"

  Scenario: Cannot login without a username
    Given I open the web page
    When I login as a "no_username" user
    Then I should see the login error message "Username is required"

  Scenario: Cannot login without a password
    Given I open the web page
    When I login as a "no_password" user
    Then I should see the login error message "Password is required"

  Scenario: Cannot login with a wrong user name
    Given I open the web page
    When I login as a "wrong_username" user
    Then I should see the login error message "Username and password do not match any user in this service"

  Scenario: Cannot login with a wrong password
    Given I open the web page
    When I login as a "wrong_password" user
    Then I should see the login error message "Username and password do not match any user in this service"

  Scenario: Valid user can login and logout
    Given I open the web page
    When I login as a "standard" user
    Then I should see "Swag Labs" in the "homepage"
    When I logout of the webpage
    Then I should see "Swag Labs" in the "loginpage"