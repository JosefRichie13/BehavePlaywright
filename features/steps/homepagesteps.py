from behave import *
from assertpy import assert_that
from features.helpers.selectors import Selectors
from features.helpers.pythonmethods import HelperMethods

@when('I note all the "{Filter}" in the homepage')
def NoteAllThePrices(context, Filter):
    match Filter:
        case "prices":
            Prices = context.page.locator(Selectors.PricesList)
            FormattedPrices = HelperMethods.ConvertPricesToFloat(Prices.all_text_contents())
            PricesInDataFile = {"PriceList": FormattedPrices}
            HelperMethods.WriteToFile(PricesInDataFile, "features/helpers/tempdata.json")
        case "names":
            Names = context.page.locator(Selectors.ProductList)
            FormattedNames = HelperMethods.FormatNames(Names.all_text_contents())
            NamesInDataFile = {"NamesList": FormattedNames}
            HelperMethods.WriteToFile(NamesInDataFile, "features/helpers/tempdata.json")
        case _:
            print(Filter + " not supported")


# This method will select a sort option from a dropdown
@when('I select the "{SortOption}" sort option')
def SelectTheSortOption(context, SortOption):
    context.page.locator(Selectors.SortOption).select_option(SortOption)

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
            Prices = context.page.locator(Selectors.PricesList)
            FormattedPricesInUI = HelperMethods.ConvertPricesToFloat(Prices.all_text_contents())

            # Get unsorted prices from tempdata and then sort them using sorted()
            # and keep them in FormattedPricesAfterSort
            PricesFromDataFile = HelperMethods.ReadFromFile("features/helpers/tempdata.json")
            FormattedPricesBeforeSort = PricesFromDataFile["PriceList"]
            FormattedPricesAfterSort = sorted(FormattedPricesBeforeSort, reverse=True)

            # Compare if both are same
            assert_that(FormattedPricesInUI).is_equal_to(FormattedPricesAfterSort)

        case "Price (low to high)":
            Prices = context.page.locator(Selectors.PricesList)
            FormattedPricesInUI = HelperMethods.ConvertPricesToFloat(Prices.all_text_contents())

            PricesFromDataFile = HelperMethods.ReadFromFile("features/helpers/tempdata.json")
            FormattedPricesBeforeSort = PricesFromDataFile["PriceList"]
            FormattedPricesAfterSort = sorted(FormattedPricesBeforeSort)

            assert_that(FormattedPricesInUI).is_equal_to(FormattedPricesAfterSort)

        case "Name (Z to A)":
            Names = context.page.locator(Selectors.ProductList)
            NamesFromUI = HelperMethods.FormatNames(Names.all_text_contents())

            NamesFromDataFile = HelperMethods.ReadFromFile("features/helpers/tempdata.json")
            NamesFromDataFileBeforeSort = NamesFromDataFile["NamesList"]
            NamesFromDataFileAfterSort = sorted(NamesFromDataFileBeforeSort, reverse=True)

            assert_that(NamesFromUI).is_equal_to(NamesFromDataFileAfterSort)

        case "Name (A to Z)":
            Names = context.page.locator(Selectors.ProductList)
            NamesFromUI = HelperMethods.FormatNames(Names.all_text_contents())

            NamesFromDataFile = HelperMethods.ReadFromFile("features/helpers/tempdata.json")
            NamesFromDataFileBeforeSort = NamesFromDataFile["NamesList"]
            NamesFromDataFileAfterSort = sorted(NamesFromDataFileBeforeSort)

            assert_that(NamesFromUI).is_equal_to(NamesFromDataFileAfterSort)

        case _:
            print(SortOption + " not supported")