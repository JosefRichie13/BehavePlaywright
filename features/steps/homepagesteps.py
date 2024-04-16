import time

from behave import *
from assertpy import assert_that
from features.helpers.pythonmethods import HelperMethods
from features.helpers.driver import driverMethods
from features.helpers.selectors import Selectors

@when('I note all the "{Filter}" in the homepage')
def NoteAllThePrices(context, Filter):
    match Filter:
        case "prices":
            Prices = driverMethods.GetAlistOfElements(context, Selectors.PricesList)
            FormattedPrices = HelperMethods.ConvertPricesToFloat(Prices.all_text_contents())
            PricesInDataFile = {"PriceList": FormattedPrices}
            HelperMethods.WriteToFile(PricesInDataFile, "features/helpers/tempdata.json")
        case "names":
            Names = driverMethods.GetAlistOfElements(context, Selectors.ProductList)
            FormattedNames = HelperMethods.FormatNames(Names.all_text_contents())
            NamesInDataFile = {"NamesList": FormattedNames}
            HelperMethods.WriteToFile(NamesInDataFile, "features/helpers/tempdata.json")
        case _:
            print(Filter + " not supported")


# This method will select a sort option from a dropdown
@when('I select the "{SortOption}" sort option')
def SelectTheSortOption(context, SortOption):
    driverMethods.SelectFromDropdownUsingText(context, Selectors.SortOption, SortOption)


# This method will confirm whether a sort is correct in the UI or not
# It first will get all the sorted prices/names from the UI and puts them in a list (List A) after formatting them
# Then it will read the unsorted prices/names from the tempdata file and sort them using Python's sorted method
# Then puts them into a list (List B)
# Finally it compares if List A is the same as List B
@then('I confirm that the "{SortOption}" sort is correct')
def SortIsCorrect(context, SortOption):
    match SortOption:
        case "Price (high to low)":
            # Get sorted prices from UI and keep them in FormattedPricesInUI after formatting
            Prices = driverMethods.GetAlistOfElements(context, Selectors.PricesList)
            FormattedPricesInUI = HelperMethods.ConvertPricesToFloat(Prices.all_text_contents())

            # Get unsorted prices from tempdata and then sort them using sorted()
            # and keep them in FormattedPricesAfterSort
            PricesFromDataFile = HelperMethods.ReadFromFile("features/helpers/tempdata.json")
            FormattedPricesBeforeSort = PricesFromDataFile["PriceList"]
            FormattedPricesAfterSort = sorted(FormattedPricesBeforeSort, reverse=True)

            # Compare if both are same
            assert_that(FormattedPricesInUI).is_equal_to(FormattedPricesAfterSort)

        case "Price (low to high)":
            Prices = driverMethods.GetAlistOfElements(context, Selectors.PricesList)
            FormattedPricesInUI = HelperMethods.ConvertPricesToFloat(Prices.all_text_contents())

            PricesFromDataFile = HelperMethods.ReadFromFile("features/helpers/tempdata.json")
            FormattedPricesBeforeSort = PricesFromDataFile["PriceList"]
            FormattedPricesAfterSort = sorted(FormattedPricesBeforeSort)

            assert_that(FormattedPricesInUI).is_equal_to(FormattedPricesAfterSort)

        case "Name (Z to A)":
            Names = driverMethods.GetAlistOfElements(context, Selectors.ProductList)
            NamesFromUI = HelperMethods.FormatNames(Names.all_text_contents())

            NamesFromDataFile = HelperMethods.ReadFromFile("features/helpers/tempdata.json")
            NamesFromDataFileBeforeSort = NamesFromDataFile["NamesList"]
            NamesFromDataFileAfterSort = sorted(NamesFromDataFileBeforeSort, reverse=True)

            assert_that(NamesFromUI).is_equal_to(NamesFromDataFileAfterSort)

        case "Name (A to Z)":
            Names = driverMethods.GetAlistOfElements(context, Selectors.ProductList)
            NamesFromUI = HelperMethods.FormatNames(Names.all_text_contents())

            NamesFromDataFile = HelperMethods.ReadFromFile("features/helpers/tempdata.json")
            NamesFromDataFileBeforeSort = NamesFromDataFile["NamesList"]
            NamesFromDataFileAfterSort = sorted(NamesFromDataFileBeforeSort)

            assert_that(NamesFromUI).is_equal_to(NamesFromDataFileAfterSort)

        case _:
            print(SortOption + " not supported")


# This method adds a product to the cart. It gets all the names of the product and calls a helper method which puts the
# names in a list. Then gets the index of the product from the feature file and then clicks on it.
@when('I add "{Product}" to the cart')
def SelectTheProduct(context, Product):
    Names = driverMethods.GetAlistOfElements(context, Selectors.ProductList)
    NamesFromUI = HelperMethods.FormatNames(Names.all_text_contents())

    Index = NamesFromUI.index(Product)
    driverMethods.ClickOnNthElement(context, Selectors.AddToCartButton, Index)


# This method confirms the number of products in the cart
@when('I confirm that the cart has "{Number}" products')
def ConfirmNumberInCart(context, Number):
    assert_that(driverMethods.GetTextFromElement(context, Selectors.CartNumber)).is_equal_to(Number)


# This method removes a product from the cart. It gets all the names of the product and calls a helper method which
# puts the names in a list. Then gets the index of the product from the feature file and then clicks on it.
@when('I remove "{Product}" from the cart')
def RemoveTheProduct(context, Product):
    Names = driverMethods.GetAlistOfElements(context, Selectors.ProductList)
    NamesFromUI = HelperMethods.FormatNames(Names.all_text_contents())

    Index = NamesFromUI.index(Product)
    driverMethods.ClickOnNthElement(context, Selectors.RemoveFromCartButton, Index)
