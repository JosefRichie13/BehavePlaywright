class driverMethods:

    def NavigateToURL(context, url):
        context.page.goto(url)

    def TypeText(context, selectorElement, textToType):
        context.page.locator(selectorElement).type(textToType)

    def ClickButton(context, selectorElement):
        context.page.locator(selectorElement).click()

    def GetTextFromElement(context, selectorElement):
        return context.page.text_content(selectorElement)

    def ElementVisibleOrNot(context, selectorElement):
        return context.page.locator(selectorElement).is_visible()

    def GetAlistOfElements(context, selectorElement):
        listOfElements = context.page.locator(selectorElement)
        return listOfElements

    def SelectFromDropdownUsingText(context, selectorElement, selectOptionInText):
        context.page.locator(selectorElement).select_option(selectOptionInText)

    def ClickOnNthElement(context, selectorElement, nthOrder):
        context.page.locator(selectorElement).nth(nthOrder).click()

