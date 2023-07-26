@AutomatedTests
@HomePage

Feature: Home Page Scenarios

  Scenario: Product sort Price (high to low)
    Given I open the web page
    When I login as a "standard" user
    And I note all the "prices" in the homepage
    And I select the "Price (high to low)" sort option
    Then I confirm that the "Price (high to low)" sort is correct

  Scenario: Product sort Price (low to high)
    Given I open the web page
    When I login as a "standard" user
    And I note all the "prices" in the homepage
    And I select the "Price (low to high)" sort option
    Then I confirm that the "Price (low to high)" sort is correct

  Scenario: Product sort Name (Z to A)
    Given I open the web page
    When I login as a "standard" user
    And I note all the "names" in the homepage
    And I select the "Name (Z to A)" sort option
    Then I confirm that the "Name (Z to A)" sort is correct

  Scenario: Product sort Name (A to Z)
    Given I open the web page
    When I login as a "standard" user
    And I note all the "names" in the homepage
    And I select the "Name (A to Z)" sort option
    Then I confirm that the "Name (A to Z)" sort is correct

  Scenario: Cart bubble counter increases and decreases
    Given I open the web page
    When I login as a "standard" user
    And I add "Sauce Labs Backpack" to the cart
    And I add "Sauce Labs Onesie" to the cart
    And I add "Sauce Labs Bike Light" to the cart
    And I confirm that the cart has "3" products
    And I remove "Sauce Labs Bike Light" from the cart
    And I confirm that the cart has "2" products