import base64

from playwright.sync_api import sync_playwright
from features.helpers.pythonmethods import HelperMethods


def before_all(context):
    # This is the before, the browser is initialized here. Chromimum, Firefox and Webkit are supported
    playwright = sync_playwright().start()
    context.browser = playwright.webkit.launch(headless=False)
    context.page = context.browser.new_page()

# This will be executed after each scenario. Currently we are using it to take screenshots and attach it to the HTML report
def after_scenario(context, scenario):

    HelperMethods.ResetAppState(context)

    def embed_data(mime_type, data, caption):
        # If data is empty we want to finish html tag with at least one character
        non_empty_data = " " if not data else data
        for formatter in context._runner.formatters:
            if "html" in formatter.name:
                formatter.embed(mime_type=mime_type, data=non_empty_data, caption=caption)
                return

    context.embed = embed_data
    image_encoded = context.page.screenshot()
    context.embed(mime_type="image/png", data=base64.b64encode(image_encoded).decode(), caption="Screenshot")
