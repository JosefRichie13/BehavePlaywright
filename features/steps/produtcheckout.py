from behave import *
from assertpy import assert_that

from features.helpers.configs import Configs
from features.helpers.driver import driverMethods
from features.helpers.selectors import Selectors

# This method clicks on the cart
@when('I click on the cart')
def ClickOnTheCart(context):
    #context.page.locator(Selectors.Cart).click()
    driverMethods.ClickButton(context, Selectors.Cart)


# This method clicks on the checkout
@when('I checkout')
def ICheckout(context):
    #context.page.locator(Selectors.Checkout).click()
    driverMethods.ClickButton(context, Selectors.Checkout)


# This method enters the information in the checkout page. It uses a DataTable. Then it proceeds from the page
@when('I enter my information to continue')
def IEnterMyInformation(context):
    for row in context.table:
        # context.page.locator(Selectors.FirstName).type(row['FirstName'])
        # context.page.locator(Selectors.LastName).type(row['LastName'])
        # context.page.locator(Selectors.ZipCode).type(row['Zip'])

        driverMethods.TypeText(context, Selectors.FirstName, row['FirstName'])
        driverMethods.TypeText(context, Selectors.LastName, row['LastName'])
        driverMethods.TypeText(context, Selectors.ZipCode, row['Zip'])

    # context.page.locator(Selectors.ContinueButton).click()
    driverMethods.ClickButton(context, Selectors.ContinueButton)


# This method clicks on the order confirmation
@when('I confirm my order')
def IConfirmTheOrder(context):
    #context.page.locator(Selectors.FinishButton).click()
    driverMethods.ClickButton(context, Selectors.FinishButton)


@then('I should see "{Message}" after the order is placed')
def SeeTheMessageAfterOrder(context, Message):
    #assert_that(context.page.text_content(Selectors.CheckoutBanner)).is_equal_to(Message)
    assert_that(driverMethods.GetTextFromElement(context, Selectors.CheckoutBanner)).is_equal_to(Message)