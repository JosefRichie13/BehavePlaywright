from behave import *
from assertpy import assert_that

from features.helpers.configs import Configs
from features.helpers.selectors import Selectors


# Opens the Webpage
@given('I open the web page')
def IOpenTheWebPage(context):
    context.page.goto(Configs.MainURL)


# Logs in as a specified user. Enters the corresponding username and password and clicks on the login button
@when('I login as a "{UserType}" user')
def ILoginAsAUser(context, UserType):
    match UserType:
        case "standard":
            context.page.locator(Selectors.UserName).type(Configs.ValidUser)
            context.page.locator(Selectors.Password).type(Configs.Password)
        case "locked":
            context.page.locator(Selectors.UserName).type(Configs.LockedUser)
            context.page.locator(Selectors.Password).type(Configs.Password)
        case "no_username":
            context.page.locator(Selectors.Password).type(Configs.Password)
        case "no_password":
            context.page.locator(Selectors.UserName).type(Configs.ValidUser)
        case "wrong_username":
            context.page.locator(Selectors.UserName).type(Configs.WrongUser)
            context.page.locator(Selectors.Password).type(Configs.Password)
        case "wrong_password":
            context.page.locator(Selectors.UserName).type(Configs.ValidUser)
            context.page.locator(Selectors.Password).type(Configs.WrongUser)
        case _:
            print("Incorrect User Type")

    context.page.locator(Selectors.LoginButton).click()


# Verifies the messages in the corresponding pages
@then('I should see "{Message}" in the "{Page}"')
def IShouldSeeTheHomePageMessage(context, Message, Page):
    match Page:
        case "homepage":
            assert_that(context.page.text_content(Selectors.HomePageTitle)).is_equal_to(Message)
            assert_that(context.page.locator(Selectors.LoginButton).is_visible()).is_false()
        case "loginpage":
            assert_that(context.page.text_content(Selectors.LoginPageTitle)).is_equal_to(Message)
            assert_that(context.page.locator(Selectors.LoginButton).is_visible()).is_true()
        case _:
            print("Incorrect Page")


# Verifies the error messages in the login page
@then('I should see the login error message "{Message}"')
def IShouldSeeTheLoginErrorMessage(context, Message):
    assert_that(context.page.text_content(Selectors.ErrorMessage)).contains(Message)


# Logs out of the webpage. It clicks on the hamburger menu, then on the logout button
@when('I Logout of the webpage')
def ILogoutOfTheWebPage(context):
    context.page.locator(Selectors.Menu).click()
    context.page.locator(Selectors.LogoutButton).click()
