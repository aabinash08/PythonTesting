import pytest

import datetime

from playwright.sync_api import Page,expect

def test_screenshot(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    #partillay/visible element
    # page.screenshot(path=f"screenshot/images{timestamp}.png")

    #Full page of the webapage
    # page.screenshot(path=f"screenshot/images{timestamp}.png",full_page=True)


    #specific elemnet
    # logo = page.locator("img[alt='Tricentis Demo Web Shop']")
    # logo.screenshot(path=f"screenshot/images{timestamp}.png")

    specific = page.locator(".product-grid ")
    specific.screenshot(path=f"screenshot/images{timestamp}.png")

    

