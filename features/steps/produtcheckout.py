from behave import *
from assertpy import assert_that

from features.helpers.selectors import Selectors
from features.helpers.configs import Configs

# This method clicks on the cart
@when('I click on the cart')
def ClickOnTheCart(context):
    context.page.locator(Selectors.Cart).click()


# This method clicks on the checkout
@when('I checkout')
def ICheckout(context):
    context.page.locator(Selectors.Checkout).click()


# This method enters the information in the checkout page. It uses a DataTable. Then it proceeds from the page
@when('I enter my information to continue')
def IEnterMyInformation(context):
    for row in context.table:
        context.page.locator(Selectors.FirstName).type(row['FirstName'])
        context.page.locator(Selectors.LastName).type(row['LastName'])
        context.page.locator(Selectors.ZipCode).type(row['Zip'])

    context.page.locator(Selectors.ContinueButton).click()


# This method clicks on the order confirmation
@when('I confirm my order')
def IConfirmTheOrder(context):
    context.page.locator(Selectors.FinishButton).click()


@then('I should see "{Message}" after the order is placed')
def SeeTheMessageAfterOrder(context, Message):
    assert_that(context.page.text_content(Selectors.CheckoutBanner)).is_equal_to(Message)