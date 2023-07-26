# This file will contain all the helper methods which are related to python

import json


class HelperMethods:

    # This function will write to a JSON file, it takes in the JSON data and the path of the JSON file
    def WriteToFile(data, path):
        with open(path, "w") as outfile:
            json.dump(data, outfile)

    # This function will update a JSON file, it takes in the JSON data and the path of the JSON file
    def UpdateTheFile(data, path):
        with open(path, "r") as outfile:
            old_data = json.load(outfile)
            newData = old_data | data

        with open(path, "w") as outfile:
            json.dump(newData, outfile)

    # This function will read from a JSON file, it takes in the JSON data and the path of the JSON file and
    # returns the data
    def ReadFromFile(path):
        with open(path, "r") as openfile:
            data = json.load(openfile)
            return data

    # This function will accept a list of elements (prices), then extract the text(prices) from those elements
    # and put them into a new list.
    # Then it removes the $ symbol from all the prices and converts the list of strings
    # into a list of numbers and returns it
    def ConvertPricesToFloat(Prices):
        RawPrices = []

        i = 0
        while (i < len(Prices)):
            RawPrices.append(Prices[i].text)
            i = i + 1

        StringPrices = [sub[1:] for sub in RawPrices]
        NumberPrices = [eval(i) for i in StringPrices]

        return NumberPrices

    # This function will accept a list of elements (Names), then extract the text(Names) from those elements
    # and put them into a new list and returns it
    def FormatNames(Names):
        RawNames = []

        i = 0
        while (i < len(Names)):
            RawNames.append(Names[i].text)
            i = i + 1

        return RawNames

    @staticmethod
    def ClearTempData():
        open("features/helpers/tempdata.json", 'w').close()
