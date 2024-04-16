from behave import *
from assertpy import assert_that

from features.helpers.configs import Configs
from features.helpers.driver import driverMethods
from features.helpers.selectors import Selectors


# Opens the Webpage
@given('I open the web page')
def IOpenTheWebPage(context):
    driverMethods.NavigateToURL(context, Configs.MainURL)


# Logs in as a specified user. Enters the corresponding username and password and clicks on the login button
@when('I login as a "{UserType}" user')
def ILoginAsAUser(context, UserType):
    match UserType:
        case "standard":
            driverMethods.TypeText(context, Selectors.UserName, Configs.ValidUser)
            driverMethods.TypeText(context, Selectors.Password, Configs.Password)
        case "locked":
            driverMethods.TypeText(context, Selectors.UserName, Configs.LockedUser)
            driverMethods.TypeText(context, Selectors.Password, Configs.Password)
        case "no_username":
            driverMethods.TypeText(context, Selectors.Password, Configs.Password)
        case "no_password":
            driverMethods.TypeText(context, Selectors.UserName, Configs.ValidUser)
        case "wrong_username":
            driverMethods.TypeText(context, Selectors.UserName, Configs.WrongUser)
            driverMethods.TypeText(context, Selectors.Password, Configs.Password)
        case "wrong_password":
            driverMethods.TypeText(context, Selectors.UserName, Configs.ValidUser)
            driverMethods.TypeText(context, Selectors.Password, Configs.WrongUser)
        case _:
            print("Incorrect User Type")

    driverMethods.ClickButton(context, Selectors.LoginButton)


# Verifies the messages in the corresponding pages
@then('I should see "{Message}" in the "{Page}"')
def IShouldSeeTheHomePageMessage(context, Message, Page):
    match Page:
        case "homepage":
            assert_that(driverMethods.GetTextFromElement(context, Selectors.HomePageTitle)).is_equal_to(Message)
            assert_that(driverMethods.ElementVisibleOrNot(context, Selectors.LoginButton)).is_false()
        case "loginpage":
            assert_that(driverMethods.GetTextFromElement(context, Selectors.LoginPageTitle)).is_equal_to(Message)
            assert_that(driverMethods.ElementVisibleOrNot(context, Selectors.LoginButton)).is_true()
        case _:
            print("Incorrect Page")


# Verifies the error messages in the login page
@then('I should see the login error message "{Message}"')
def IShouldSeeTheLoginErrorMessage(context, Message):
    assert_that(driverMethods.GetTextFromElement(context, Selectors.ErrorMessage)).contains(Message)


# Logs out of the webpage. It clicks on the hamburger menu, then on the logout button
@when('I Logout of the webpage')
def ILogoutOfTheWebPage(context):
    driverMethods.ClickButton(context, Selectors.Menu)
    driverMethods.ClickButton(context, Selectors.LogoutButton)
